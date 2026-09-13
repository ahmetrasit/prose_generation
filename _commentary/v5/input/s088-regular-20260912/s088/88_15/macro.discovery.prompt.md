# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **88:15**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_15/macro.discovery.json` and modify nothing
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
  "ayah_ref": "88:15",
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
{"branch_registry":[{"boundary":"Physical elevation of objects or structures from a lower place to a higher one","branch_kind":null,"branch_ref":"root_000582/B001","candidate_links":[{"candidate_id":"cand_c53e6a59433d0b7bc244","lane":"macro"},{"candidate_id":"cand_d43511b8df50871cc697","lane":"macro"}],"focus_root_occurrences":[],"gloss":"raising something upward","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"إعلاء الشيء","image_en":"raising something upward"}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"إعلاء الشيء","image_en":"raising something upward","scope_ar":"إعلاء الأجسام أو البناء وإزالة الشيء عن موضعه إلى علو","scope_en":"Physical elevation of objects or structures from a lower place to a higher one"},"support_links":["sup_ce2ab0ef41aa0e3dac91","sup_cfa66887abd9775cafcb"]},{"boundary":"The bed, couch, throne-like seat, head base, and settled ease or support.","branch_kind":null,"branch_ref":"root_000697/B011","candidate_links":[{"candidate_id":"cand_c53e6a59433d0b7bc244","lane":"macro"},{"candidate_id":"cand_d43511b8df50871cc697","lane":"macro"}],"focus_root_occurrences":[],"gloss":"place of settled support","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"موضع الاستقرار والاتكاء","image_en":"place of settled support"}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"موضع الاستقرار والاتكاء","image_en":"place of settled support","scope_ar":"السرير والسرر والأسرة وسرير الرأس وسرير العيش وما يستقر عليه أو عنده","scope_en":"The bed, couch, throne-like seat, head base, and settled ease or support."},"support_links":["sup_ce2ab0ef41aa0e3dac91","sup_cfa66887abd9775cafcb"]},{"boundary":"Çekirdek, yalnızca bir araya gelmeyi değil, düz bir çizgi üzerinde yan yana düzenlenmeyi gerektirir.","branch_kind":"bare","branch_ref":"root_000871/B001","candidate_links":[{"candidate_id":"cand_1cd45178a3d3c4760359","lane":"macro"},{"candidate_id":"cand_0b542f3fc17000575fc9","lane":"macro"},{"candidate_id":"cand_d24aaee211327bd9bc1b","lane":"macro"},{"candidate_id":"cand_d43511b8df50871cc697","lane":"macro"},{"candidate_id":"cand_4a6d7d94f85a2bbbae38","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","surface_ar":"مَصْفُوفَةٌ"}],"gloss":"düz bir sıra oluşturma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birden çok ögeyi düz bir çizgi üzerinde yan yana yerleştirme ya da bu biçimde düzenlenmiş olma."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanların, özellikle savaş bağlamında, yan yana bir çizgi düzeninde durması ve bu düzenin kurulduğu mevki."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kuşların kanatlarını açıp kıpırdatmadan durması veya kesilecek hayvanların yan yana dizilmesi."}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ögeleri yan yana düz bir çizgide düzenleme ve bu düzende bulunma çekirdeğini doğal ve kısa biçimde karşılar.","boundary_detail":"Çekirdek, yalnızca bir araya gelmeyi değil, düz bir çizgi üzerinde yan yana düzenlenmeyi gerektirir.","branch_image_ar":"الاصطفاف على خط مستو","concept_gloss":"düz bir sıra oluşturma","contextual_glosses":[{"applicability":"Bir topluluğun ya da nesne kümesinin kendi üzerinde gerçekleşen düzenlenmeyi anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yan yana bir çizgi düzenine girme ve sonuçta o düzende bulunma korunur."},"facet_ids":["F001","F002"],"text":"sıraya dizilmek","usage_role":"contextual"},{"applicability":"Kuşların uçuş sırasında kanatlarını yanlara açıp hareket ettirmeden tuttuğu özel bağlam için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuş bağlamındaki açılmış kanatların düzenli ve hareketsiz tutulması korunur."},"facet_ids":["F003"],"text":"kanatlarını açıp sabit tutmak","usage_role":"explanatory"}],"definition":"Nesneleri ya da bir topluluğu düz bir çizgi üzerinde yan yana dizmek veya kişilerin ve varlıkların böyle bir düzen içinde durmasıdır. Savaş düzeni ile kanatlarını açıp sabit tutan kuşlar gibi kullanımlar bu temel uzamsal düzenin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birden çok ögeyi düz bir çizgi üzerinde yan yana yerleştirme ya da bu biçimde düzenlenmiş olma."},{"facet_id":"F002","role":"specialization","statement":"İnsanların, özellikle savaş bağlamında, yan yana bir çizgi düzeninde durması ve bu düzenin kurulduğu mevki."},{"facet_id":"F003","role":"example","statement":"Kuşların kanatlarını açıp kıpırdatmadan durması veya kesilecek hayvanların yan yana dizilmesi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Düz çizgi ve yan yanalık bulunmadan gerçekleşen her türlü bir araya gelmeyi de kapsar.","collision":"Su başında toplanma dalıyla kolayca karışır.","fit":"broadening","loses":null,"preserves":"Birden çok kişinin ya da ögenin birlikte bulunması korunur."},"text":"toplanma"}],"identity_rationale":"Kaynak ifadesi, nesneleri ya da kişileri düz bir çizgi üzerinde yan yana yerleştirme ve bu düzende durma çekirdeğini açıkça destekler. Savaşta durulan yer, hareketsiz açılmış kanatlarla duran kuşlar ve kesim için yan yana duran hayvanlar bu çekirdeğin bağlama özgü gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"düz çizgi üzerinde yan yana duran ögelerden oluşan sıra"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yan yana sıraya dizmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yan yana sıraya girmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sıra halinde duran; kanatlarını açıp sabit tutan"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"savaş sırasının kurulduğu mevki"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"sıra halinde dizilmiş"}],"lexicalization_note":"Dal yalın kullanımlarla tanıklanmıştır; tanım herhangi bir özel tamlamaya ya da tek bir bağlama bağlanmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çizgisel düzeni topluluk adı, sıra içi hareket ve su başında toplanmadan ayıran üç karşılaştırma sınırı en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal düzenleme eylemi ile çizgisel sonucu temel alır; komşu dal ise belirli bir topluluk ya da düzenli küme türünü adlandırır.","focus_only":"Düz çizgi üzerinde yan yana dizme eylemini ve bu düzende durmayı genel olarak kapsar.","gloss":"düzenli bir sıra ya da bölük","neighbor_only":"İnsan bölüğü, asker topluluğu veya aynı düzen üzerinde sıralanmış evler gibi belirli kümeleri ve bunların birbirine geçişli örgüsünü adlandırır.","neighbor_ref":"root_000812/B005","relation_type":"near_synonym","shared_zone":"Her iki dalda da çok sayıda ögenin yan yana ve düzenli biçimde yerleşmesi vardır."},{"boundary_match":"field_only","distinction":"Odak dal sıranın kendisini kurar veya adlandırır; komşu dal mevcut sıra içindeki konumları ileri geri değiştirir.","focus_only":"Sıranın kurulmasını ve çizgi üzerindeki düzenli duruşu bildirir.","gloss":"savaş sırasında yer değiştirme","neighbor_only":"Kurulmuş savaş sıralarında bazı kişileri öne, bazılarını geriye kaydırarak düzenleme yapmayı bildirir.","neighbor_ref":"root_000316/B011","relation_type":"same_field","shared_zone":"İki dal da savaş sıralarının mekânsal düzeniyle ilgilidir."},{"boundary_match":"partial","distinction":"Su başında toplanmak çizgisel bir düzen gerektirmez; odak dalın ayırıcı özelliği düz sıra biçimidir.","focus_only":"Bir çizgi üzerinde yan yana düzenlenmeyi zorunlu kılar.","gloss":"su başında toplanma","neighbor_only":"Yalnızca su başında bir araya gelmeyi bildiren kalıpla sınırlıdır.","neighbor_ref":"root_000871/B007","relation_type":"near_neighbor","shared_zone":"Her iki dalda da birden çok katılımcının aynı yerde bulunması söz konusudur."}],"source_phrase_ar":"الصف معروف (ayn;tahdhib); الصف أن تجعل الشيء على خط مستو (mufradat); صففت القوم فاصطفوا (ayn;sihah;tahdhib); المصف الموقف والجمع المصاف (ayn;sihah;tahdhib); الصافات صفا يعني الملائكة (mufradat;tahdhib); الطير الصواف التي تصف أجنحتها فلا تحركها (ayn;tahdhib); البدن الصواف التي تصفف ثم تنحر (ayn;tahdhib)","source_summary":"Kaynaklar, düz çizgi üzerinde yan yana düzenlenme çekirdeğinde birleşir ve insan, savaş, kuş ve kesim hayvanı bağlamlarını bu çekirdeğe bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"جعل الشيء أو الجماعة صفا على خط مستو، ووقوف القوم والملائكة والخيل والطير والبدن مصطفة، والمصف في الحرب","what_is_not_ar":"ليس ناقة الصفوف ولا الصفيف من اللحم ولا الصفصف من الأرض"},"support_links":["sup_04514900ae6d8fec7866","sup_0f51d6251290fafdcc90","sup_568a493fbe1cc62a81d2","sup_800b077d573c0b7a322b","sup_ce2ab0ef41aa0e3dac91"]},{"boundary":"Çokluk, tek sağımda kullanılan süt kaplarına ilişkindir; ikinci kullanım ise süt miktarından bağımsız bir ayak duruşudur.","branch_kind":"bare","branch_ref":"root_000871/B002","candidate_links":[{"candidate_id":"cand_41f0e8c29661826927d5","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","surface_ar":"مَصْفُوفَةٌ"}],"gloss":"bir sağımda birden çok kabı dolduran ya da ön ayaklarını hizalayan dişi deve","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi devenin tek bir sağımda iki ya da daha çok süt kabını doldurması."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi devenin sağım sırasında ön ayaklarını yan yana hizalayarak durması."}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kap sayısına dayalı ana kullanımını ve sağım sırasındaki duruş varyantını birlikte belirtmek gerektiğinde kullanılır.","boundary_detail":"Çokluk, tek sağımda kullanılan süt kaplarına ilişkindir; ikinci kullanım ise süt miktarından bağımsız bir ayak duruşudur.","branch_image_ar":"ناقة تجمع محالبها","concept_gloss":"bir sağımda birden çok kabı dolduran ya da ön ayaklarını hizalayan dişi deve","contextual_glosses":[{"applicability":"Süt bolluğu ve tek sağımda doldurulan kap sayısı öne çıktığında kullanılan doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişi deve, tek sağım ve birden çok kabı dolduracak süt verme özellikleri korunur."},"facet_ids":["F001"],"text":"bir sağımda birkaç kap süt veren dişi deve","usage_role":"contextual"},{"applicability":"Kaynaklardaki duruşa dayalı kullanımın özellikle anlatıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişi devenin sağım anındaki ön ayaklarını yan yana getirme duruşu korunur."},"facet_ids":["F002"],"text":"sağılırken ön ayaklarını hizalayan dişi deve","usage_role":"explanatory"}],"definition":"Tek bir sağımda iki ya da daha çok kabı sütle dolduran dişi deve veya sağılırken ön ayaklarını yan yana hizalayan dişi devedir. İlk kullanım süt bolluğuna ve kap sayısına, ikincisi ise hayvanın duruşuna dayanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi devenin tek bir sağımda iki ya da daha çok süt kabını doldurması."},{"facet_id":"F002","role":"source_variant","statement":"Dişi devenin sağım sırasında ön ayaklarını yan yana hizalayarak durması."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kap sayısıyla ölçülmeyen her türlü süt bolluğunu da kapsar.","collision":"Genel süt bolluğunu bildiren komşu dalla karışır.","fit":"broadening","loses":null,"preserves":"Süt bolluğu ve deve niteliği korunur."},"text":"bol sütlü deve"}],"identity_rationale":"Kaynak ifadesi iki bağlı fakat farklı betimlemeyi aynı dalda toplar: dişi devenin tek sağımda iki veya daha çok kabı doldurması ve sağılırken ön ayaklarını yan yana hizalaması. Dal korunabilir, ancak kapları doldurma ile ayrı sağımları birleştirme birbirine karıştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir sağımda birden çok kabı dolduran ya da ön ayaklarını hizalayan dişi deve"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dişi deveyi tek sağımda iki veya üç kaba sağma"}],"lexicalization_note":"Dalın iki yalın biçimi vardır; tanım hem çok kap doldurma niteliğini hem de sağım sırasındaki ayak duruşunu ayrı tutar.","neighbor_coverage_note":"Adayların tümü incelendi; iki kaplık yakın karşılık, üçlü sağım niteliği ve genel süt bolluğu dalın kap sayısı ile duruş sınırlarını yeterince belirginleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal iki kapla sınırlı daha dar bir karşılıktır; odak dal iki veya daha çok kabı ve ayrıca ayak duruşu varyantını içerir.","focus_only":"İki kabın ötesine çıkabilmeyi ve sağımda ön ayakları hizalama varyantını da kapsar.","gloss":"tek sağımda iki kap dolduran dişi deve","neighbor_only":"Özellikle iki kaplık sütün tek sağımda bir araya getirilmesini adlandırır.","neighbor_ref":"root_000802/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da dişi devenin tek sağımda birden çok kabı sütle doldurmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalın eşiği iki kaptır ve ayak duruşu varyantı bulunur; komşu dal üç sayısına ve farklı meme durumlarına bağlıdır.","focus_only":"İki ya da daha çok kap doldurmayı genel olarak veya ön ayakların hizalanmasını bildirir.","gloss":"üçlü sağım özelliği taşıyan dişi deve","neighbor_only":"Üç kap doldurma yanında üç meme ucundan sağılma, üçünün kuruması ya da bağlanması gibi başka üçlü özellikleri de kapsar.","neighbor_ref":"root_000203/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda da dişi devenin sağımı ve kap sayısı üzerinden nitelenmesi vardır."},{"boundary_match":"field_only","distinction":"Komşu dal genel ve karşılaştırmalı bolluğu, odak dal ise tek sağımda doldurulan kapları ve ayrıca ayak duruşunu temel alır.","focus_only":"Süt bolluğunu doldurulan kap sayısıyla somutlaştırır ve bir duruş varyantı içerir.","gloss":"çok bol sütlü dişi deve","neighbor_only":"Sütün başka bol sütlü develerle karşılaştırıldığında daha da bol oluşunu bildirir.","neighbor_ref":"root_000200/B005","relation_type":"same_field","shared_zone":"İki dal da dişi devenin süt veriminin yüksekliğini konu edinir."}],"source_phrase_ar":"الصفوف الناقة التي تجمع بين محلبين في حلبة (maqayis;tahdhib); الصف أن تحلب الناقة في محلبين أو ثلاثة تصف بينها (sihah); ناقة صفوف للتي تصف أقداحا من لبنها (sihah); الصفوف ناقة تصف بين محلبين فصاعدا لغزارتها (mufradat); الصفوف أيضا التي تصف يديها عند الحلب (maqayis;sihah;tahdhib)","source_summary":"Kaynaklar, aynı adlandırma altında hem tek sağımda birden çok kap dolduran sütlü dişi deveyi hem de sağılırken ön ayaklarını hizalayan dişi deveyi aktarır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الناقة الصفوف التي تجمع بين محلبين أو ثلاثة في حلبة، أو تصف يديها عند الحلب","what_is_not_ar":"ليس صف القوم ولا صفيف اللحم ولا صفة البناء"},"support_links":["sup_6f85fdbc70dd994f5112"]},{"boundary":"Güneşte kurutma, közde pişirme, yolculuk eti ve inceltici dilimleme tek bir zorunlu süreç gibi birleştirilmemelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000871/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","surface_ar":"مَصْفُوفَةٌ"}],"gloss":"kurutmak ya da közlemek için sıra sıra serilmiş et","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Etin şeritlere ayrılıp güneşte kurutulmak veya közde pişirilmek üzere sıra sıra serilmesi ve böyle hazırlanmış et."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yolculukta pişmiş ya da kızartılmış olarak taşınan, ancak tam pişmemiş kalan et."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir et parçasını genişletip inceltecek biçimde dilimleme."}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın et şeritlerini düzenli biçimde serme ve güneş ya da közle hazırlama çekirdeğini karşılar.","boundary_detail":"Güneşte kurutma, közde pişirme, yolculuk eti ve inceltici dilimleme tek bir zorunlu süreç gibi birleştirilmemelidir.","branch_image_ar":"الصَّفيف من اللحم","concept_gloss":"kurutmak ya da közlemek için sıra sıra serilmiş et","contextual_glosses":[{"applicability":"Güneşte kurutmaya yönelik et hazırlama eyleminin anlatıldığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Etin şeritlenmesi, sıra sıra serilmesi ve kurutma amacı korunur."},"facet_ids":["F001"],"text":"eti şeritler halinde serip kurutmak","usage_role":"contextual"},{"applicability":"Yolculukta taşınan pişmiş ya da kızartılmış etin içinin tam pişmemiş kaldığı kaynak varyantına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yolculukta taşınma, et olma ve tam pişmeme özellikleri korunur."},"facet_ids":["F002"],"text":"tam pişmemiş yolculuk eti","usage_role":"explanatory"},{"applicability":"Et parçasını genişletip incelten dilimleme kullanımını açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Etin kesilmesi ve kesim sonucunda incelmesi korunur."},"facet_ids":["F003"],"text":"eti inceltecek biçimde dilimlemek","usage_role":"explanatory"}],"definition":"Etin şeritlenerek güneşte kurutulmak ya da köz üzerinde pişirilmek üzere sıra sıra serilmesi ve bu biçimde hazırlanmış ettir. Bunun yanında yolculukta taşınan fakat tam pişmemiş et ile eti inceltecek biçimde dilimleme de kaynakta ilişkili kullanımlar olarak yer alır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Etin şeritlere ayrılıp güneşte kurutulmak veya közde pişirilmek üzere sıra sıra serilmesi ve böyle hazırlanmış et."},{"facet_id":"F002","role":"source_variant","statement":"Yolculukta pişmiş ya da kızartılmış olarak taşınan, ancak tam pişmemiş kalan et."},{"facet_id":"F003","role":"extension","statement":"Bir et parçasını genişletip inceltecek biçimde dilimleme."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Etin sıra sıra serilmesini, közde pişirme kullanımını ve işlem yönünü siler.","preserves":"Etin güneşte hazırlanmış bir ürün olabilmesi korunur."},"text":"kurutulmuş et"},{"category":"confusable","error_profile":{"adds":null,"collision":"Genel pişirme ve kızartma dallarıyla karışır.","fit":"narrowing","loses":"Şeritlere ayırıp sıra sıra serme ile güneşte kurutma seçeneklerini kaybeder.","preserves":"Etin ateş ısısıyla hazırlanması korunur."},"text":"ızgara et"}],"identity_rationale":"Kaynak ifadesi tek bir işlemden çok, etin şeritlenip güneşte kurutulmak veya közde pişirilmek üzere sıra sıra serilmesi çevresindeki kullanımları toplar. Yolculukta taşınan fakat tam pişmemiş et ve eti inceltecek biçimde dilimleme, bu çekirdekle ilişkili fakat ondan ayrı varyantlardır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"güneşte kurutulmak veya közde pişirilmek üzere sıra sıra serilmiş et"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"eti şeritlere ayırıp sıra sıra sermek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"eti genişletip inceltecek biçimde dilimleme"}],"lexicalization_note":"Dal hem yalın adları hem de ete bağlı bir kalıbı içerir; yalın et adı, eti sıra sıra serme kalıbı ve inceltici dilimleme ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; dilimleme, kurutup saklama ve kor üzerinde pişirme dalları, odak dalın sıra sıra serme ile çoklu hazırlama yöntemlerini en iyi sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kesme biçimini temel alır; odak dalın çekirdeğinde kesilen etin kurutma veya közleme için düzenli biçimde serilmesi vardır.","focus_only":"Dilimlenen eti güneşte veya közde hazırlamak üzere sıra sıra sermeyi içerir.","gloss":"eti kesip yayvan dilimlere ayırma","neighbor_only":"Eti uzuvdan ya da kemik üzerinden ayırma ve genel olarak yayvan ya da ince parçalara kesme işlemlerini kapsar.","neighbor_ref":"root_000784/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da etin kesilerek ince veya yayvan parçalara dönüştürülmesini içerebilir."},{"boundary_match":"partial","distinction":"Odak dal düzenli serme biçimine bağlıdır ve köz kullanımına uzanır; komşu dal kurutma ve saklama sürecini daha geniş ürün alanında ele alır.","focus_only":"Et şeritlerinin sıra sıra serilmesini ve közde pişirme seçeneğini de kapsar.","gloss":"eti veya hurmayı kurutup saklama","neighbor_only":"Et yanında hurmanın kurutulması ve genel kurutma ya da saklama işlemlerini kapsar.","neighbor_ref":"root_000187/B002","relation_type":"near_neighbor","shared_zone":"İki dal etin kesilip kurutularak hazırlanması alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal ısıyla pişirme yöntemidir; odak dal ise sıra sıra serilen etin hem kurutma hem közleme yoluyla hazırlanmasını adlandırır.","focus_only":"Etin sıra sıra serilmesini ve güneşte kurutulmasını da içerir.","gloss":"eti kor üzerinde pişirme","neighbor_only":"Etin doğrudan kor üzerine konmasını ve pişmesi için ısının yeniden yemeğe yöneltilmesini temel alır.","neighbor_ref":"root_000321/B008","relation_type":"near_neighbor","shared_zone":"Her iki dalda etin közle temas ederek pişirilmesi bulunabilir."}],"source_phrase_ar":"الصفيف قال قوم هو القديد (maqayis); اللحم يحمل في الأسفار طبيخا أو شواء فلا ينضج (maqayis); الصفيف القديد اذا شر في الشمس (ayn;tahdhib); الصفيف ما صف من اللحم على الجمر لينشوي (sihah); صففت اللحم قددته وألقيته صفا صفا (mufradat); التصفيف نحو التشريح (tahdhib)","source_summary":"Kaynaklar etin şeritlenmesi, sıra sıra serilmesi ve güneş ya da közle hazırlanması çevresinde birleşir; tam pişmemiş yolculuk eti ve inceltici dilimleme de ilişkili varyantlar olarak aktarılır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الصَّفيف، وهو اللحم المشرر أو المصفوف في الشمس أو على الجمر، واللحم المحمول في السفر طبيخا أو شواء فلا ينضج","what_is_not_ar":"ليس الصف المعروف ولا الصُّفَّة من البناء ولا الصفصف من الأرض"},"support_links":[]},{"boundary":"Yapıdaki bölüm ile eyer düzeneği aynı ad altında yer alır, fakat kanıt bunların biçimsel ayrıntılarını belirtmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000871/B004","candidate_links":[{"candidate_id":"cand_c53e6a59433d0b7bc244","lane":"macro"},{"candidate_id":"cand_0b542f3fc17000575fc9","lane":"macro"},{"candidate_id":"cand_d43511b8df50871cc697","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","surface_ar":"مَصْفُوفَةٌ"}],"gloss":"yapı ya da eyer bölümü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yapıda veya eyerde bulunan özel bir bölüm ya da düzenek."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir hayvan için söz konusu eyer düzeneğini yapma."}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynağın fiziksel biçimini belirtmediği yalın adın iki kullanım alanını ihtiyatlı biçimde karşılar.","boundary_detail":"Yapıdaki bölüm ile eyer düzeneği aynı ad altında yer alır, fakat kanıt bunların biçimsel ayrıntılarını belirtmez.","branch_image_ar":"الصُّفَّة في البناء والسرج","concept_gloss":"yapı ya da eyer bölümü","contextual_glosses":[{"applicability":"Yalnızca hayvan için ilgili parçanın yapıldığını bildiren kalıp kullanımı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan, eyer düzeneği ve bunu yapma eylemi korunur."},"facet_ids":["F002"],"text":"hayvan için eyer düzeneği yapmak","usage_role":"explanatory"}],"definition":"Bir yapıda ya da eyerde bulunan, biçimi kaynakta ayrıntılandırılmamış bölüm veya düzenektir. Hayvan için bu tür bir eyer düzeneği yapma eylemi de yalnızca ilgili kalıp içinde bu dala bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yapıda veya eyerde bulunan özel bir bölüm ya da düzenek."},{"facet_id":"F002","role":"associated_use","statement":"Bir hayvan için söz konusu eyer düzeneğini yapma."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Kaynağın belirtmediği belirli bir mimari biçimi varsayar.","fit":"narrowing","loses":"Eyer kullanımını ve hayvan için düzenek yapma kalıbını bütünüyle kaybeder.","preserves":"Bir yapı bölümü olma olasılığını korur."},"text":"sundurma"}],"identity_rationale":"Kaynak ifadesi bir yapıda ve eyerde bulunan bölüm ya da düzenek ile hayvan için böyle bir eyer düzeneği yapma kullanımını destekler. Ancak parçanın fiziksel biçimi kaynak ifadesinde açıklanmadığından, tanım onu belirli bir mimari tür veya belirli bir eyer parçasıyla özdeşleştirmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yapıda ya da eyerde bulunan bölüm veya düzenek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"hayvan için eyer düzeneği yapmak"}],"lexicalization_note":"Yalın ad yapı ve eyer alanlarına uzanırken, kalıp yalnızca hayvan için ilgili eyer düzeneğini yapma eylemini bildirir.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; destek parçası, belirli semer biçimi ve bütün binek takımı karşılaştırmaları kanıtta biçimi belirsiz kalan bölümün sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal parçayı destek işleviyle tanımlar; odak dalın kanıtı ise işlevi ve biçimi ayrıntılandırmadan yapı veya eyer bölümünü adlandırır.","focus_only":"Yapı veya eyer üzerindeki adlandırılmış bölümü ve onun hayvan için yapılmasını kapsar.","gloss":"taşıyıcı destek parçası","neighbor_only":"Duvar, çatı, yara ve eyer gibi şeylere destek ya da dayanak olarak eklenen yardımcı parçaların genel alanını kapsar.","neighbor_ref":"root_000580/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da eyer veya yapı üzerinde bulunan işlevsel bir parça söz konusu olabilir."},{"boundary_match":"partial","distinction":"Komşu dal belirli biçimdeki bir semeri adlandırır; odak dal biçimi belirsiz bir eyer bölümünü ve ayrıca yapıdaki kullanımı kapsar.","focus_only":"Yapı alanına da uzanır ve hayvan için ilgili düzeneği yapma eylemini içerir.","gloss":"yayılmış ve ayrılmamış semer","neighbor_only":"Özellikle yayılmış, ayrılmamış bir semer türünü ve onun belirli yapısını adlandırır.","neighbor_ref":"root_000116/B013","relation_type":"near_neighbor","shared_zone":"İki dal hayvanın sırtında kullanılan eyer veya semer donanımı alanında buluşur."},{"boundary_match":"field_only","distinction":"Komşu dal bütün binek takımını, odak dal ise eyer üzerindeki bir bölüm veya düzeneği belirtir.","focus_only":"Eyerin bir bölümünü veya düzeneğini ve bunun yapılmasını bildirir.","gloss":"deve binek takımı","neighbor_only":"Devenin sırtına konan bütün binek takımını adlandırır.","neighbor_ref":"root_000551/B002","relation_type":"same_field","shared_zone":"Her iki dal da hayvanın sırtındaki binme donanımıyla ilgilidir."}],"source_phrase_ar":"الصفة من البنيان والسرج ايضا (ayn); صفة الدار والسرج واحدة الصفف (sihah); صفة السرج (tahdhib); صففت للدابة صفة أي عملتها له (tahdhib); الصفة من البنيان وصفة السرج (mufradat)","source_summary":"Kaynaklar, yapıdaki bölüm ile eyer üzerindeki düzeneği aynı yalın ad altında verir ve hayvan için bu düzeneği yapma eylemini ayrı bir kalıpla tanıklar.","sources":["AY","SI","TA","MU"],"what_is_ar":"الصُّفَّة من البنيان، وصُفَّة السرج، وما يعمل للدابة من ذلك","what_is_not_ar":"ليست صفة الوصف ولا صف القوم ولا الصفيف"},"support_links":["sup_0f51d6251290fafdcc90","sup_ce2ab0ef41aa0e3dac91","sup_cfa66887abd9775cafcb"]},{"boundary":"Düzlük ve pürüzsüzlük çekirdektir; bitkisizlik ise tanıklanmış fakat zorunlu olmayan bir varyanttır.","branch_kind":"bare","branch_ref":"root_000871/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","surface_ar":"مَصْفُوفَةٌ"}],"gloss":"düz ve pürüzsüz arazi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüzeyi düz ve pürüzsüz olan arazi ya da geniş düzlük."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bitki örtüsü bulunmayan, çıplak düz arazi."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yüzeyin tek bir sıra gibi kesintisiz ve aynı düzeyde görünmesi."}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bütün tanıklardaki ortak arazi ve yüzey çekirdeğini en kısa doğal biçimde karşılar.","boundary_detail":"Düzlük ve pürüzsüzlük çekirdektir; bitkisizlik ise tanıklanmış fakat zorunlu olmayan bir varyanttır.","branch_image_ar":"الأرض الصفصف","concept_gloss":"düz ve pürüzsüz arazi","contextual_glosses":[{"applicability":"Bitki örtüsünün bulunmadığının ayrıca belirtildiği kaynak varyantı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Arazi, düzlük, pürüzsüzlük ve bitkisizlik özellikleri birlikte korunur."},"facet_ids":["F001","F002"],"text":"bitkisiz, düz ve pürüzsüz arazi","usage_role":"contextual"},{"applicability":"Arazinin tek bir sıra gibi aynı düzeyde uzanması benzetmesini öne çıkaran bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Arazi yüzeyinin aynı düzeyde ve kesintisiz görünmesi korunur."},"facet_ids":["F003"],"text":"kesintisiz düzlük","usage_role":"explanatory"}],"definition":"Yüzeyi düz ve pürüzsüz olan arazi veya geniş düzlük alanıdır. Bazı kullanımlarda bu arazinin bitkisiz ve çıplak olduğu da özellikle belirtilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüzeyi düz ve pürüzsüz olan arazi ya da geniş düzlük."},{"facet_id":"F002","role":"source_variant","statement":"Bitki örtüsü bulunmayan, çıplak düz arazi."},{"facet_id":"F003","role":"extension","statement":"Yüzeyin tek bir sıra gibi kesintisiz ve aynı düzeyde görünmesi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"İklimsel bir arazi türünü gereksiz yere varsayar.","fit":"narrowing","loses":"Düzlük ve pürüzsüzlük çekirdeğini zorunlu olarak taşımaz, bitkili olabilen çekirdek kullanımları dışarıda bırakır.","preserves":"Geniş ve bitkisiz arazi olabilme özelliği korunur."},"text":"çöl"}],"identity_rationale":"Kaynak ifadesinin ortak çekirdeği arazinin düz, pürüzsüz ve geniş bir düzlük olmasıdır. Bitkisizlik ve çıplaklık bazı tanımlarda eklenen bir yüzey niteliğidir; her düz ve pürüzsüz arazi için zorunlu koşul gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"düz ve pürüzsüz, kimi kullanımda bitkisiz arazi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"düz ve pürüzsüz araziler"}],"lexicalization_note":"Dal yalın arazi adlarıyla tanıklanır; tanım başka bir tamlamaya dayanmaz ve yüzey özelliklerini arazi çekirdeğine bağlar.","neighbor_coverage_note":"Bütün adaylar incelendi; tam eşdeğer arazi dalı ile çakıllı, beyaz ve genel düz yer komşuları pürüzsüzlük, bitkisizlik ve ek yüzey niteliklerini ayırır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve sınırlar örtüşür; tek sıra görünümü veya bitkisizlik gibi betimlemeler aynı arazi kavramının bağımlı özellikleridir.","focus_only":null,"gloss":"düz ve pürüzsüz arazi","neighbor_only":null,"neighbor_ref":"root_000870/B001","relation_type":"synonym","shared_zone":"Her iki dalın çekirdeği düz, pürüzsüz ve geniş arazi yüzeyidir."},{"boundary_match":"partial","distinction":"Komşu dal çakıllı yüzey ve belirli arazi türlerini ekler; odak dalın çekirdeği yalnızca düzlük ile pürüzsüzlüktür.","focus_only":"Çakıllı olmayı gerektirmeden düz ve pürüzsüz araziyi adlandırır.","gloss":"çıplak ve çakıllı düzlük","neighbor_only":"Bozkır veya geçit alanını çıplak ve özellikle çakıllı olabilen yüzeyiyle niteler.","neighbor_ref":"root_001420/B009","relation_type":"near_synonym","shared_zone":"İki dal da düz, çıplak ve geniş arazi için kullanılabilir."},{"boundary_match":"partial","distinction":"Komşu dal beyazlık ve adlandırılmış yer kapsamını ekler; odak dal düz yüzey yapısıyla sınırlıdır.","focus_only":"Beyazlık veya kum niteliği olmadan düz ve pürüzsüz araziyi karşılar.","gloss":"beyaz ve pürüzsüz arazi","neighbor_only":"Beyazlık, kum tepesi ve yer adı kullanımlarını da kapsar.","neighbor_ref":"root_000168/B013","relation_type":"near_synonym","shared_zone":"Her iki dal bitkisiz ve pürüzsüz bir araziyi adlandırabilir."},{"boundary_match":"partial","distinction":"Odak dal yüzeyin pürüzsüzlüğünü çekirdeğe alır; komşu dal daha genel bir düz yer adıdır.","focus_only":"Pürüzsüz yüzeyi ve kimi kullanımlarda bitkisizliği özellikle taşır.","gloss":"düz tabanlı yer","neighbor_only":"Genel olarak düz bir tabanı veya düz yeri adlandırır, pürüzsüzlük koşulu taşımaz.","neighbor_ref":"root_001204/B008","relation_type":"near_neighbor","shared_zone":"Her iki dalın referansı düz bir arazi veya yer olabilir."}],"source_phrase_ar":"الصفصف وهو المستوي من الأرض (maqayis); الصفصف الفلاة المستوية الملساء (ayn); الصفصف المستوى من الأرض (sihah); الصفصف الذي لا نبات فيه (tahdhib); الصفصف القرعاء (tahdhib); الصفصف المستوي الأملس (tahdhib); الصفصف المستوي من الأرض كأنه على صف واحد (mufradat)","source_summary":"Kaynaklar düz ve pürüzsüz arazi çekirdeğinde birleşir; bitkisizlik, çıplaklık ve tek bir sıra gibi aynı düzeyde görünme bu yüzeyin ek betimlemeleridir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الصَّفْصَف والقاع المستوي الأملس من الأرض، وما لا نبات فيه أو القرعاء","what_is_not_ar":"ليس صف القوم ولا الصفيف ولا شجر الصفصاف"},"support_links":[]},{"boundary":"Bu dal yalnızca söğüt ağacını adlandırır; düz ve pürüzsüz arazi anlamını içermez.","branch_kind":"bare","branch_ref":"root_000871/B006","candidate_links":[{"candidate_id":"cand_4a6d7d94f85a2bbbae38","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","surface_ar":"مَصْفُوفَةٌ"}],"gloss":"söğüt ağacı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söğüt ağacı türünün adı."}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın tek ve doğrudan botanik referansını doğal Türkçe ağaç adıyla eksiksiz karşılar.","boundary_detail":"Bu dal yalnızca söğüt ağacını adlandırır; düz ve pürüzsüz arazi anlamını içermez.","branch_image_ar":"الصفصاف شجر الخلاف","concept_gloss":"söğüt ağacı","definition":"Söğüt ağacını adlandıran yalın bir bitki adıdır. Benzer sesli arazi adından bağımsız bir botanik referansa sahiptir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söğüt ağacı türünün adı."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bitki yerine arazi yüzeyi anlamı ekler.","collision":"Düz ve pürüzsüz arazi dalıyla doğrudan karışır.","fit":"displacement","loses":"Ağaç türü olma ve söğüt kimliğini bütünüyle kaybeder.","preserves":"Benzer sesli başka bir dalın yüzeyle ilgili referansını taşır."},"text":"düz arazi"}],"identity_rationale":"Kaynak ifadesi dalı açık ve tutarlı biçimde belirli bir ağaç türü olarak tanımlar. Arazi adıyla yazılış benzerliği bulunsa da referans ağaçtır ve düz arazi dalından ayrı tutulması gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"söğüt ağacı"}],"lexicalization_note":"Dal tek bir yalın ağaç adıyla tanıklanmıştır; tanım herhangi bir kalıp ya da mecazi uzantı eklemez.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; aynı ağaç türünü adlandıran tam eşdeğer dal yararlı tek doğrudan karşılaştırmadır, öteki adaylar yalnızca genel bitki alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kavramsal çekirdek ve kapsam bakımından bir ayrım yoktur; iki dal aynı ağaç referansında örtüşür.","focus_only":null,"gloss":"söğüt ağacı","neighbor_only":null,"neighbor_ref":"root_000870/B002","relation_type":"synonym","shared_zone":"Her iki dal da aynı söğüt ağacı türünü doğrudan adlandırır."}],"source_phrase_ar":"الصفصف شجر الخلاف الواحدة بالهاء (ayn); الصفصاف شجر الخلاف (sihah;mufradat); الصفصاف الخلاف (tahdhib); هو شجر الخلاف بلغة أهل الشام (tahdhib)","source_summary":"Kaynaklar, yalın adın söğüt ağacını gösterdiğinde birleşir; bölgesel kullanım bilgisi kavramın ağaç türü sınırını değiştirmez.","sources":["AY","SI","TA","MU"],"what_is_ar":"الصَّفصاف شجر الخلاف","what_is_not_ar":"ليس الصفصف من الأرض ولا الصف المعروف"},"support_links":["sup_800b077d573c0b7a322b"]},{"boundary":"Anlam genel toplanma değil, yalnızca suyla kurulan belirtilmiş kalıp içindeki bir araya gelmedir.","branch_kind":"collocation","branch_ref":"root_000871/B007","candidate_links":[{"candidate_id":"cand_41f0e8c29661826927d5","lane":"macro"},{"candidate_id":"cand_d24aaee211327bd9bc1b","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","surface_ar":"مَصْفُوفَةٌ"}],"gloss":"su başında toplanma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun su başında bir araya gelmesi."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı su başında toplanma anlamının iki ayrı fiil biçimiyle ifade edilmesi."}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca topluluğun su çevresinde bir araya geldiği tanıklı kalıpların ortak kavramını karşılar.","boundary_detail":"Anlam genel toplanma değil, yalnızca suyla kurulan belirtilmiş kalıp içindeki bir araya gelmedir.","branch_image_ar":"التصافّ على الماء","concept_gloss":"su başında toplanma","contextual_glosses":[{"applicability":"İki tanıklı kalıbın da cümle içinde doğal Türkçe karşılığı olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Katılımcıların su başında aynı yere gelmesi ve kalıbın suyla sınırlı oluşu korunur."},"facet_ids":["F001","F002"],"text":"suyun başında bir araya gelmek","usage_role":"contextual"}],"definition":"Bir topluluğun su başında bir araya gelmesidir. Anlam, suyu tamamlayıcı olarak alan iki eşdeğer kalıpla sınırlıdır ve düz sıra oluşturmayı gerektirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun su başında bir araya gelmesi."},{"facet_id":"F002","role":"source_variant","statement":"Aynı su başında toplanma anlamının iki ayrı fiil biçimiyle ifade edilmesi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kaynakta bulunmayan çizgisel yan yanalık ve sıra düzeni ekler.","collision":"Düz çizgi üzerinde sıralanma dalıyla doğrudan karışır.","fit":"displacement","loses":"Su başında bir araya gelme koşulunu kaybeder.","preserves":"Bir topluluğun ortak bir yerde bulunmasını korur."},"text":"sıraya girmek"},{"category":"alternative","error_profile":{"adds":"Suyla bağlantısı olmayan her türlü toplanmayı da kapsar.","collision":"Genel toplanma komşularıyla sınırı belirsizleştirir.","fit":"broadening","loses":null,"preserves":"Birden çok katılımcının bir araya gelmesi korunur."},"text":"toplanmak"}],"identity_rationale":"Kaynak ifadesi iki fiil biçimini aynı anlamda verir ve kullanımı su başında bir araya gelme durumuyla açıkça sınırlar. Çizgi halinde dizilme anlamı bu tanıklığın parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"su başında toplanmak"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"su başında toplanmak"}],"lexicalization_note":"Dal yalnızca suyla kurulan iki tanıklı kalıpta geçer; buradan yalın fiile genel bir toplanma anlamı aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; nesne çevresinde genel toplanma, tek yerde toplanma ve çizgisel sıralanma karşılaştırmaları suya bağlı kalıbın sınırını açıkça gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın odak noktası zorunlu olarak sudur; komşu dal farklı nesneler çevresindeki toplanmayı ve yönelmeyi daha genel biçimde kapsar.","focus_only":"Toplanmayı özellikle su başına bağlayan tanıklı iki kalıpla sınırlıdır.","gloss":"bir şeyin çevresinde toplanma","neighbor_only":"İnsan veya hayvanların herhangi bir şeyin çevresinde ya da üzerinde durup ona yönelmesini genel olarak kapsar.","neighbor_ref":"root_001038/B004","relation_type":"near_synonym","shared_zone":"Her iki dalda bir topluluk belirli bir odak noktasının çevresinde bir araya gelir."},{"boundary_match":"partial","distinction":"Komşu dal genel yer birliğini anlatır; odak dal yalnızca su başındaki toplanmanın kalıplaşmış ifadesidir.","focus_only":"Su tamamlayıcısıyla kurulan belirli söz dizimsel kalıba bağlıdır.","gloss":"tek bir yerde toplanma","neighbor_only":"Özellikle develer başta olmak üzere şeylerin tek bir yere toplanmasını su koşulu olmadan bildirir.","neighbor_ref":"root_001616/B001","relation_type":"near_synonym","shared_zone":"İki dal da birden çok katılımcının aynı yerde bir araya gelmesini ifade eder."},{"boundary_match":"partial","distinction":"Odak dal suya bağlı toplanmadır; komşu dalın belirleyici özelliği su değil, düz çizgi üzerindeki yan yanalıktır.","focus_only":"Su başında bir araya gelmeyi gerektirir, çizgisel düzen istemez.","gloss":"düz bir sıra oluşturma","neighbor_only":"Ögelerin düz bir çizgi üzerinde yan yana sıralanmasını gerektirir, su koşulu taşımaz.","neighbor_ref":"root_000871/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal bir topluluğun ortak bir mekânsal düzen içinde bulunmasını anlatabilir."}],"source_phrase_ar":"تضافوا على الماء وتصافوا عليه بمعنى واحد إذا اجتمعوا عليه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, iki fiil biçiminin su başında toplanma anlamında eşdeğer kullanıldığını bildirir."}],"source_summary":"Kanıt, anlamı su başında bir araya gelme kalıbıyla sınırlar ve iki fiil biçimini bu sınırlı kullanımda eşdeğer gösterir.","sources":["TA"],"what_is_ar":"تصافوا على الماء، أي اجتمعوا عليه","what_is_not_ar":"ليس الاصطفاف في صف للحرب أو الصلاة، ولا صفيف اللحم"},"support_links":["sup_568a493fbe1cc62a81d2","sup_6f85fdbc70dd994f5112"]},{"boundary":"putting, setting down, locating, building, or manifesting something in a place","branch_kind":null,"branch_ref":"root_001657/B001","candidate_links":[{"candidate_id":"cand_c53e6a59433d0b7bc244","lane":"macro"},{"candidate_id":"cand_d43511b8df50871cc697","lane":"macro"}],"focus_root_occurrences":[],"gloss":"setting something down or in its place","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"وضع الشيء في موضع أخفض أو مقرر","image_en":"setting something down or in its place"}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"وضع الشيء في موضع أخفض أو مقرر","image_en":"setting something down or in its place","scope_ar":"وضع الشيء من اليد أو على الأرض أو في موضعه، والموضع، وما يتفرع عن البناء والإبراز","scope_en":"putting, setting down, locating, building, or manifesting something in a place"},"support_links":["sup_ce2ab0ef41aa0e3dac91","sup_cfa66887abd9775cafcb"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000083/B001","candidate_links":[{"candidate_id":"cand_d43511b8df50871cc697","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_0e883656e74acaf59322","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Dispersal supplies the broad floor field that prevents the row from becoming total regimentation.","root":"ب ث ث","source_ref":"88:16","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000083","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_ce2ab0ef41aa0e3dac91"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000240/B001","candidate_links":[{"candidate_id":"cand_4a6d7d94f85a2bbbae38","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_590c3a2c331a6aa8a4e3","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Flow gives direction to the edge and keeps the image spatial rather than merely botanical.","root":"ج ر ي","source_ref":"88:12","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000240","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_800b077d573c0b7a322b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000266/B003","candidate_links":[{"candidate_id":"cand_d24aaee211327bd9bc1b","lane":"macro"},{"candidate_id":"cand_4a6d7d94f85a2bbbae38","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9ee8ce6338f0e9e9ac3f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The tree-sheltered garden supplies the bounded social environment in which the row operates.","root":"ج ن ن","source_ref":"88:10","source_word_indices":["2"]},{"hft_ref":"hft_590c3a2c331a6aa8a4e3","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The tree-sheltered garden provides an ecological setting for the remote willow image.","root":"ج ن ن","source_ref":"88:10","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000266","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_568a493fbe1cc62a81d2","sup_800b077d573c0b7a322b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000412/B001","candidate_links":[{"candidate_id":"cand_1cd45178a3d3c4760359","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_009822fbc5fe2324f0d1","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The lowered, submissive posture supplies the bodily state from which fitted rest is a reversal.","root":"خ ش ع","source_ref":"88:2","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000412","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_04514900ae6d8fec7866"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000569/B001","candidate_links":[{"candidate_id":"cand_0b542f3fc17000575fc9","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_548baf34bd627ac1b0c6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Contentment closes the causal arc from effort to a fitting place of repose.","root":"ر ض و","source_ref":"88:9","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000569","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_0f51d6251290fafdcc90"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000709/B002","candidate_links":[{"candidate_id":"cand_0b542f3fc17000575fc9","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_548baf34bd627ac1b0c6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Work and earned action supply the completed movement whose result is now inhabitable.","root":"س ع ي","source_ref":"88:9","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000709","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_0f51d6251290fafdcc90"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000722/B001","candidate_links":[{"candidate_id":"cand_41f0e8c29661826927d5","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6b77c8d5201c0e5ddced","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Serving drink supplies the service relation whose harmful form is later reversed.","root":"س ق ي","source_ref":"88:5","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000722","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6f85fdbc70dd994f5112"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000741/B001","candidate_links":[{"candidate_id":"cand_d24aaee211327bd9bc1b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9ee8ce6338f0e9e9ac3f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Literal hearing makes acoustic experience an explicit property of the setting.","root":"س م ع","source_ref":"88:11","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000741","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_568a493fbe1cc62a81d2"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000934/B004","candidate_links":[{"candidate_id":"cand_41f0e8c29661826927d5","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6b77c8d5201c0e5ddced","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Food as sustenance and good condition makes nourishment, not mere presentation, the relevant test.","root":"ط ع م","source_ref":"88:6","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000934","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6f85fdbc70dd994f5112"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001046/B001","candidate_links":[{"candidate_id":"cand_1cd45178a3d3c4760359","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_009822fbc5fe2324f0d1","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Purposeful labor supplies the exertion that the prepared seating suspends.","root":"ع م ل","source_ref":"88:3","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001046","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_04514900ae6d8fec7866"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001069/B006","candidate_links":[{"candidate_id":"cand_41f0e8c29661826927d5","lane":"macro"},{"candidate_id":"cand_4a6d7d94f85a2bbbae38","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6b77c8d5201c0e5ddced","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The flowing water source supplies the adequate center around which serial access can be organized.","root":"ع ي ن","source_ref":"88:12","source_word_indices":["2"]},{"hft_ref":"hft_590c3a2c331a6aa8a4e3","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The water source supplies the riparian center beside which a willow-like edge can be imagined.","root":"ع ي ن","source_ref":"88:12","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001069","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6f85fdbc70dd994f5112","sup_800b077d573c0b7a322b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001110/B002","candidate_links":[{"candidate_id":"cand_41f0e8c29661826927d5","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6b77c8d5201c0e5ddced","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The sufficiency branch identifies what the earlier provisioning explicitly fails to achieve.","root":"غ ن ي","source_ref":"88:7","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001110","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6f85fdbc70dd994f5112"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001361/B003","candidate_links":[{"candidate_id":"cand_d24aaee211327bd9bc1b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9ee8ce6338f0e9e9ac3f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Mixed din supplies the excluded crowd-condition against which ordered gathering is heard.","root":"ل غ و","source_ref":"88:11","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001361","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_568a493fbe1cc62a81d2"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001507/B004","candidate_links":[{"candidate_id":"cand_1cd45178a3d3c4760359","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_009822fbc5fe2324f0d1","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Exhausting toil gives the contrast causal force: ordered supports answer bodily depletion.","root":"ن ص ب","source_ref":"88:3","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001507","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_04514900ae6d8fec7866"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001525/B002","candidate_links":[{"candidate_id":"cand_0b542f3fc17000575fc9","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_548baf34bd627ac1b0c6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Softness and ease supply the bodily quality realized by the cushions.","root":"ن ع م","source_ref":"88:8","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001525","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_0f51d6251290fafdcc90"]}],"candidate_inventory":[{"anchor_refs":["88:13","88:14","88:15"],"branch_refs":["root_000582/B001","root_000697/B011","root_000871/B004","root_001657/B001"],"candidate_id":"cand_c53e6a59433d0b7bc244","commentary_obligation":"review","focus_branch_refs":["root_000871/B004"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000582/B001","root_000697/B011","root_001657/B001"],"root_ids":[],"scope":"pericope","source_local_id":"A:Raised Couch and Seat","source_type":"channel","support_ids":["sup_3f0e3fde702f98ff06e2","sup_5eab647facb844adf4b6","sup_864db6a36a51e7f5c840","sup_b0038bff32bfbb04660a","sup_cfa66887abd9775cafcb"],"title":"Raised Couch and Seat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:15","88:2","88:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:15","branch_refs":["root_000412/B001","root_000871/B001","root_001046/B001","root_001507/B004"],"candidate_id":"cand_1cd45178a3d3c4760359","commentary_obligation":"review","hft_ref":"hft_009822fbc5fe2324f0d1","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:ctx_toil_transferred_to_furnishing","source_type":"hft","support_ids":["sup_04514900ae6d8fec7866"],"title":"ctx_toil_transferred_to_furnishing","trust":"legacy_unbound"},{"anchor_refs":["88:12","88:15","88:5","88:6","88:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:15","branch_refs":["root_000722/B001","root_000871/B002","root_000871/B007","root_000934/B004","root_001069/B006","root_001110/B002"],"candidate_id":"cand_41f0e8c29661826927d5","commentary_obligation":"review","hft_ref":"hft_6b77c8d5201c0e5ddced","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:ctx_provision_distributed_without_failure","source_type":"hft","support_ids":["sup_6f85fdbc70dd994f5112"],"title":"ctx_provision_distributed_without_failure","trust":"legacy_unbound"},{"anchor_refs":["88:15","88:8","88:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:15","branch_refs":["root_000569/B001","root_000709/B002","root_000871/B001","root_000871/B004","root_001525/B002"],"candidate_id":"cand_0b542f3fc17000575fc9","commentary_obligation":"review","hft_ref":"hft_548baf34bd627ac1b0c6","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:ctx_earned_rest_made_spatial","source_type":"hft","support_ids":["sup_0f51d6251290fafdcc90"],"title":"ctx_earned_rest_made_spatial","trust":"legacy_unbound"},{"anchor_refs":["88:10","88:11","88:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:15","branch_refs":["root_000266/B003","root_000741/B001","root_000871/B001","root_000871/B007","root_001361/B003"],"candidate_id":"cand_d24aaee211327bd9bc1b","commentary_obligation":"review","hft_ref":"hft_9ee8ce6338f0e9e9ac3f","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:ctx_quiet_social_choreography","source_type":"hft","support_ids":["sup_568a493fbe1cc62a81d2"],"title":"ctx_quiet_social_choreography","trust":"legacy_unbound"},{"anchor_refs":["88:13","88:14","88:15","88:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:15","branch_refs":["root_000083/B001","root_000582/B001","root_000697/B011","root_000871/B001","root_000871/B004","root_001657/B001"],"candidate_id":"cand_d43511b8df50871cc697","commentary_obligation":"review","hft_ref":"hft_0e883656e74acaf59322","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:ctx_four_operation_furnishing_field","source_type":"hft","support_ids":["sup_ce2ab0ef41aa0e3dac91"],"title":"ctx_four_operation_furnishing_field","trust":"legacy_unbound"},{"anchor_refs":["88:10","88:12","88:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:15","branch_refs":["root_000240/B001","root_000266/B003","root_000871/B001","root_000871/B006","root_001069/B006"],"candidate_id":"cand_4a6d7d94f85a2bbbae38","commentary_obligation":"review","hft_ref":"hft_590c3a2c331a6aa8a4e3","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_riparian_soft_boundary","source_type":"hft","support_ids":["sup_800b077d573c0b7a322b"],"title":"outlier_riparian_soft_boundary","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_982e66d1f64198c7d36a","connection_ref":"conn_84d91ed037a9b63bb222","note":"The adjacent مَبْثُوثَة furnishing continues the local presentation of prepared surfaces.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_97098f5851e898b52a1d","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:16","source_note":"The immediately preceding ordered cushions define the furnishings that carpets complete.","source_row_role":"ranked_review","source_target_component_ref":"88:15","source_target_components":["88:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:15"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:16","source_target_components":["88:16"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:16","target_evidence":{"arabic_uthmani":"وَزَرَابِىُّ مَبْثُوثَةٌ","ayah_ref":"88:16"},"target_ref":"88:16"},{"connection_evidence_ref":"conn_ev_886fff6329927d08ea1b","connection_ref":"conn_b0e051df358db597d298","note":"The opening face-state establishes the surah's contrary register but adds no furnishing detail.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_d550a7ef85ea054e1be6","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"88:2","source_note":"The arranged cushions do not clarify 88:2.","source_row_role":"ranked_review","source_target_component_ref":"88:15","source_target_components":["88:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:15"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:2","source_target_components":["88:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:2","target_evidence":{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ","ayah_ref":"88:2"},"target_ref":"88:2"},{"connection_evidence_ref":"conn_ev_aa9cf266d31b492bbc37","connection_ref":"conn_24f2d020924ca78d9196","note":"The immediately preceding سُرُر مرفوعة supplies the larger prepared-resting setting for the نمارق.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_4e005dba0ea48686e028","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:13","source_note":"Immediate furnishing sequence: arranged cushions specify the couch setting.","source_row_role":"ranked_review","source_target_component_ref":"88:15","source_target_components":["88:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:15"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:13","source_target_components":["88:13"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:13","target_evidence":{"arabic_uthmani":"فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ","ayah_ref":"88:13"},"target_ref":"88:13"},{"connection_evidence_ref":"conn_ev_b924d20934f2e043930f","connection_ref":"conn_2188890de1ce822d14f7","note":"The adjacent أكواب موضوعة locates the نمارق within a deliberately prepared sequence of objects.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_35ade2bf10701fcd7474","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:14","source_note":"Immediate continuation adds arranged furnishings beside the positioned cups.","source_row_role":"ranked_review","source_target_component_ref":"88:15","source_target_components":["88:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:15"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14","target_evidence":{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","ayah_ref":"88:14"},"target_ref":"88:14"},{"connection_evidence_ref":"conn_ev_f375b3a1dd048da3704c","connection_ref":"conn_5f3f0c286ff552f8951b","note":"The favorable face-state identifies the local register in which the furnishings are shown.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_10ce448f5c1ae8ead995","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:8","source_note":"Immediate arranged cushions concretize the ease-setting around 88:8.","source_row_role":"ranked_review","source_target_component_ref":"88:15","source_target_components":["88:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:15"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:8","source_target_components":["88:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:8","target_evidence":{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ","ayah_ref":"88:8"},"target_ref":"88:8"},{"connection_evidence_ref":"conn_ev_8f2a0f2cbd3e149dd9f6","connection_ref":"conn_338053e8f6cd10c3032e","note":"The non-nourishing food sharpens the surah's contrary provision scene against the prepared comfort of 88:15.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_424fc2b9202457dbdecd","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:7","source_note":"The arranged cushions further develop the immediate scene opposed to deprivation.","source_row_role":"ranked_review","source_target_component_ref":"88:15","source_target_components":["88:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:15"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:7","source_target_components":["88:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:7","target_evidence":{"arabic_uthmani":"لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ","ayah_ref":"88:7"},"target_ref":"88:7"},{"connection_evidence_ref":"conn_ev_590d21347c441a8db54c","connection_ref":"conn_3819eddc7f98240bfd38","note":"The restricted food scene gives the nearest contrary provision context within the surah.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_822d53bc63a576c127fb","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"88:6","source_note":"No material link to the focus reading.","source_row_role":"ranked_review","source_target_component_ref":"88:15","source_target_components":["88:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:15"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:6","source_target_components":["88:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:6","target_evidence":{"arabic_uthmani":"لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ","ayah_ref":"88:6"},"target_ref":"88:6"},{"connection_evidence_ref":"conn_ev_01d3642b9fe95a3ac108","connection_ref":"conn_fd8b8c3b425b80a0265b","note":"Toil and exhaustion provide a local contrary state to the prepared rest.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":true,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_f18cf7f3701e5b321797","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:3","source_note":"Ordered cushions contribute to the contrary condition of repose.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:15","source_target_components":["88:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:15"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3","target_evidence":{"arabic_uthmani":"عَامِلَةٌۭ نَّاصِبَةٌۭ","ayah_ref":"88:3"},"target_ref":"88:3"},{"connection_ref":"conn_1366790926c0dfd48f93","note":null,"origin":"derived_reciprocal_seed","prior_label":null,"qualification":{"boundary":"At least one source-direction review meaningfully linked this target back to the focus ayah. Treat its note and label only as a discovery nomination. Reassess the relation from the focus ayah using the supplied exact target Arabic; do not invent missing target morphology or inherit the source label.","derived_reciprocal_counterevidence":false,"derived_reciprocal_seed":true,"has_missing_ayah_suggestion_source_row":true,"has_ranked_review_source_row":false,"has_reciprocal_counterevidence":false,"has_reciprocal_nomination":true,"receiving_direction_requires_fresh_assessment":true,"source_direction_labels_are_not_focus_decisions":true,"source_row_roles_are_provenance_not_decisions":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_49ad5702b07319a907b2","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"88:1","source_note":"Adjacent garden furnishing completes a local scene detail.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:15","source_target_components":["88:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:15"}],"relation_scope":"declared_pericope_reciprocal_evidence","target_evidence":{"arabic_uthmani":"هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ","ayah_ref":"88:1"},"target_ref":"88:1"},{"connection_ref":"conn_f40e2e916f1dc151c5c2","note":null,"origin":"derived_reciprocal_seed","prior_label":null,"qualification":{"boundary":"At least one source-direction review meaningfully linked this target back to the focus ayah. Treat its note and label only as a discovery nomination. Reassess the relation from the focus ayah using the supplied exact target Arabic; do not invent missing target morphology or inherit the source label.","derived_reciprocal_counterevidence":false,"derived_reciprocal_seed":true,"has_missing_ayah_suggestion_source_row":true,"has_ranked_review_source_row":false,"has_reciprocal_counterevidence":false,"has_reciprocal_nomination":true,"receiving_direction_requires_fresh_assessment":true,"source_direction_labels_are_not_focus_decisions":true,"source_row_roles_are_provenance_not_decisions":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_54a7e92cb739458d7b96","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:10","source_note":"The arranged cushions make the elevated garden hospitable and accessible.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:15","source_target_components":["88:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:15"}],"relation_scope":"declared_pericope_reciprocal_evidence","target_evidence":{"arabic_uthmani":"فِى جَنَّةٍ عَالِيَةٍۢ","ayah_ref":"88:10"},"target_ref":"88:10"},{"connection_ref":"conn_35aefe0a325e1a1de43b","note":null,"origin":"derived_reciprocal_seed","prior_label":null,"qualification":{"boundary":"At least one source-direction review meaningfully linked this target back to the focus ayah. Treat its note and label only as a discovery nomination. Reassess the relation from the focus ayah using the supplied exact target Arabic; do not invent missing target morphology or inherit the source label.","derived_reciprocal_counterevidence":false,"derived_reciprocal_seed":true,"has_missing_ayah_suggestion_source_row":true,"has_ranked_review_source_row":false,"has_reciprocal_counterevidence":false,"has_reciprocal_nomination":true,"receiving_direction_requires_fresh_assessment":true,"source_direction_labels_are_not_focus_decisions":true,"source_row_roles_are_provenance_not_decisions":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_e6d85faba5bb7e962382","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:12","source_note":"Immediate continuation adds another item within the same فِيهَا scene.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:15","source_target_components":["88:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:15"}],"relation_scope":"declared_pericope_reciprocal_evidence","target_evidence":{"arabic_uthmani":"فِيهَا عَيْنٌۭ جَارِيَةٌۭ","ayah_ref":"88:12"},"target_ref":"88:12"}],"focus":{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:15:1:1","qac_word_ref":"88:15:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"نَمَارِق","morph_features":"STEM|POS:N|LEM:namaAriq|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:15:1:2","qac_word_ref":"88:15:1","root_ar":"","surface_ar":"نَمَارِقُ"},{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","root_ar":"ص ف ف","surface_ar":"مَصْفُوفَةٌ"}],"word_analysis_qac_refs":[["88:15:1:1"],["88:15:1:2"],["88:15:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:15:1","88:15:2","88:15:3"]},"focus_surface_evidence":{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:15:1:1","qac_word_ref":"88:15:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"نَمَارِق","morph_features":"STEM|POS:N|LEM:namaAriq|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:15:1:2","qac_word_ref":"88:15:1","root_ar":"","surface_ar":"نَمَارِقُ"},{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","root_ar":"ص ف ف","surface_ar":"مَصْفُوفَةٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:15:1:1"],["88:15:1:2"],["88:15:2:1"]],"word_analysis_refs":["88:15:1","88:15:2","88:15:3"],"word_rows":[{"analysis_record_ref":"88:15:1","analytic_gloss_range_en":"additive coordination that carries the already established garden-inventory frame forward into another furnishing item","analytic_root_gloss_range_en":null,"qac_refs":["88:15:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"88:15:2","analytic_gloss_range_en":"indefinite plural cushion-supports, materially present in the garden inventory and then gathered by the following ordering adjective","analytic_root_gloss_range_en":"tight concrete object field for a small cushion, pad, bolster, or saddle-cover; the local noun selects the cushion-support branch","qac_refs":["88:15:1:2"],"root":{"arabic":"ن م ر ق","transliteration":"n-m-r-q"},"surface":{"arabic":"نَمَارِقُ","transliteration":"namāriq"}},{"analysis_record_ref":"88:15:3","analytic_gloss_range_en":"rowed or arranged as a completed collective state modifying the cushion group","analytic_root_gloss_range_en":"root range centered on lining up or arranging side by side in rows, ranks, or formations; other lexical branches exist, but the local adjective selects ordered alignment","qac_refs":["88:15:2:1"],"root":{"arabic":"ص ف ف","transliteration":"ṣ-f-f"},"surface":{"arabic":"مَصْفُوفَةٌۭ","transliteration":"maṣfūfatun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":14,"missing_anchor_refs":[],"supplied_unique_anchor_count":14},"assigned_record_count":6,"assigned_records":[{"anchor_refs":["88:15","88:2","88:3"],"branch_refs":["root_000412/B001","root_000871/B001","root_001046/B001","root_001507/B004"],"candidate_id":"cand_1cd45178a3d3c4760359","evidence_scope":"declared_pericope","hft_ref":"hft_009822fbc5fe2324f0d1","item_id":"ctx_toil_transferred_to_furnishing","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:ctx_toil_transferred_to_furnishing","support_id":"sup_04514900ae6d8fec7866"},{"anchor_refs":["88:12","88:15","88:5","88:6","88:7"],"branch_refs":["root_000722/B001","root_000871/B002","root_000871/B007","root_000934/B004","root_001069/B006","root_001110/B002"],"candidate_id":"cand_41f0e8c29661826927d5","evidence_scope":"declared_pericope","hft_ref":"hft_6b77c8d5201c0e5ddced","item_id":"ctx_provision_distributed_without_failure","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:ctx_provision_distributed_without_failure","support_id":"sup_6f85fdbc70dd994f5112"},{"anchor_refs":["88:15","88:8","88:9"],"branch_refs":["root_000569/B001","root_000709/B002","root_000871/B001","root_000871/B004","root_001525/B002"],"candidate_id":"cand_0b542f3fc17000575fc9","evidence_scope":"declared_pericope","hft_ref":"hft_548baf34bd627ac1b0c6","item_id":"ctx_earned_rest_made_spatial","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:ctx_earned_rest_made_spatial","support_id":"sup_0f51d6251290fafdcc90"},{"anchor_refs":["88:10","88:11","88:15"],"branch_refs":["root_000266/B003","root_000741/B001","root_000871/B001","root_000871/B007","root_001361/B003"],"candidate_id":"cand_d24aaee211327bd9bc1b","evidence_scope":"declared_pericope","hft_ref":"hft_9ee8ce6338f0e9e9ac3f","item_id":"ctx_quiet_social_choreography","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:ctx_quiet_social_choreography","support_id":"sup_568a493fbe1cc62a81d2"},{"anchor_refs":["88:13","88:14","88:15","88:16"],"branch_refs":["root_000083/B001","root_000582/B001","root_000697/B011","root_000871/B001","root_000871/B004","root_001657/B001"],"candidate_id":"cand_d43511b8df50871cc697","evidence_scope":"declared_pericope","hft_ref":"hft_0e883656e74acaf59322","item_id":"ctx_four_operation_furnishing_field","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:ctx_four_operation_furnishing_field","support_id":"sup_ce2ab0ef41aa0e3dac91"},{"anchor_refs":["88:10","88:12","88:15"],"branch_refs":["root_000240/B001","root_000266/B003","root_000871/B001","root_000871/B006","root_001069/B006"],"candidate_id":"cand_4a6d7d94f85a2bbbae38","evidence_scope":"declared_pericope","hft_ref":"hft_590c3a2c331a6aa8a4e3","item_id":"outlier_riparian_soft_boundary","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_riparian_soft_boundary","support_id":"sup_800b077d573c0b7a322b"}],"diagnostics":[],"lane_counts":{"global":14,"macro":6,"micro":4},"packet_summary":{"ayah_count":26,"focus_ref":"88:15","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:15","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"88:15","lane":"macro","linguistic_source_ref":"88:15","surface_ref":"88:15","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:15","target_tokens":[["Dizilmiş",["88:15:2"]],["yastıklar",["88:15:1"]],["da",["88:15:1"]],["vardır",["88:15:1"]]],"text":"Dizilmiş yastıklar da vardır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":6,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":16,"id":"s088-p01-001-016","label":"Faces at the overwhelming event","number":1,"refs":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"88:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"88:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["88:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"88:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Raised Couch and Seat","source_type":"channel","support_id":"sup_3f0e3fde702f98ff06e2","text":"Resting surface, elevation, support, and placement describe one prepared seat.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Raised Couch and Seat","source_type":"channel","support_id":"sup_5eab647facb844adf4b6","text":"Soft, ordered supports receive a reclining or seated body.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Raised Couch and Seat","source_type":"channel","support_id":"sup_864db6a36a51e7f5c840","text":"A resting platform is raised, placed, and prepared for reclining.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Raised Couch and Seat","source_type":"channel","support_id":"sup_b0038bff32bfbb04660a","text":"88:13 `سرر مرفوعة` (`س ر ر`, `ر ف ع`); 88:15 `مصفوفة` (`ص ف ف`); 88:14 `موضوعة` (`و ض ع`)","trust":"trusted"},{"branch_refs":["root_000582/B001","root_000697/B011","root_000871/B004","root_001657/B001"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Raised Couch and Seat","source_type":"channel","support_id":"sup_cfa66887abd9775cafcb","text":"couch or resting place `س ر ر:B011/m01`; raised placement `ر ف ع:B001/m01`; building or saddle platform `ص ف ف:B004/m01`; settled placement `و ض ع:B001/m01`","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","ayah_ref":"88:15"},{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ","ayah_ref":"88:2"},{"arabic_uthmani":"عَامِلَةٌۭ نَّاصِبَةٌۭ","ayah_ref":"88:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000412/B001","root_000871/B001","root_001046/B001","root_001507/B004"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000871","role":"The branch ranges from ordinary rows to human and battle lines, allowing the focus to shift the burden of ranking onto cushions.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000412","role":"The lowered, submissive posture supplies the bodily state from which fitted rest is a reversal.","root":"خ ش ع","source_ref":"88:2","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001046","role":"Purposeful labor supplies the exertion that the prepared seating suspends.","root":"ع م ل","source_ref":"88:3","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_001507","role":"Exhausting toil gives the contrast causal force: ordered supports answer bodily depletion.","root":"ن ص ب","source_ref":"88:3","source_word_indices":["2"]}],"changed_reading":{"after":"The row is a reversal of coerced exertion: objects hold formation so restored bodies no longer have to.","before":"The cushion row is tidy furnishing."},"confidence":"strong","mechanism":"The earlier bodies are lowered, working, and exhausted. Against that sequence, the focus passive transfers disciplined alignment from persons to furnishings: the cushions now bear the row, leaving their recipients free to rest rather than stand in a laboring or martial rank.","model_id":"ctx_toil_transferred_to_furnishing","reader_inference":"The packet supplies exhausted bodies and a focus branch that can include human or battle ranks; I infer a transfer of alignment from occupant to object. A live alternative is simple reward contrast with no deliberate agency transfer.","status":"revised","structural_cues":["The sequence first predicates lowered posture, labor, and exhaustion of faces, then later predicates alignment of cushions.","The focus passive assigns the work of standing in formation to the furnishings rather than to their users."],"trigger_roots":["خ ش ع","ع م ل","ن ص ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:ctx_toil_transferred_to_furnishing","source_type":"hft","support_id":"sup_04514900ae6d8fec7866","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِيهَا عَيْنٌۭ جَارِيَةٌۭ","ayah_ref":"88:12"},{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","ayah_ref":"88:15"},{"arabic_uthmani":"تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ","ayah_ref":"88:5"},{"arabic_uthmani":"لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ","ayah_ref":"88:6"},{"arabic_uthmani":"لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ","ayah_ref":"88:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":5,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":5,"target_morphology_supplied":false},"branch_refs":["root_000722/B001","root_000871/B002","root_000871/B007","root_000934/B004","root_001069/B006","root_001110/B002"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_000871","role":"Gathering at water makes the cushion line organize access to a shared source.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000871","role":"The several-vessel image supplies a serial model for distributing one abundance among many receivers.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000722","role":"Serving drink supplies the service relation whose harmful form is later reversed.","root":"س ق ي","source_ref":"88:5","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000934","role":"Food as sustenance and good condition makes nourishment, not mere presentation, the relevant test.","root":"ط ع م","source_ref":"88:6","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001110","role":"The sufficiency branch identifies what the earlier provisioning explicitly fails to achieve.","root":"غ ن ي","source_ref":"88:7","source_word_indices":["4"]},{"branch_id":"B006","mapped_root_id":"root_001069","role":"The flowing water source supplies the adequate center around which serial access can be organized.","root":"ع ي ن","source_ref":"88:12","source_word_indices":["2"]}],"changed_reading":{"after":"The row becomes an operational hospitality network that turns a shared, sufficient provision into many accessible places.","before":"Serial abundance is an abstract implication of having many cushions."},"confidence":"medium","mechanism":"An earlier service chain delivers drink and food yet fails to give sufficiency; the later flowing source reverses that failure. The focus branches for gathering at water and filling several vessels let the row function as a distribution topology, with many resting positions arranged around adequate provision.","model_id":"ctx_provision_distributed_without_failure","reader_inference":"The packet supplies failed provisioning, a flowing source, and focus branches of water-gathering and multiple vessels; I infer that the row distributes access to adequate hospitality. The alternative is a sensory contrast in which furniture has no service function.","status":"strengthened","structural_cues":["Verses 5-7 form a negated provisioning chain: service occurs, but nourishment and sufficiency do not.","Verse 12 replaces the harmful source with a flowing one before the cups and cushions appear."],"trigger_roots":["س ق ي","ط ع م","غ ن ي","ع ي ن"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:ctx_provision_distributed_without_failure","source_type":"hft","support_id":"sup_6f85fdbc70dd994f5112","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","ayah_ref":"88:15"},{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ","ayah_ref":"88:8"},{"arabic_uthmani":"لِّسَعْيِهَا رَاضِيَةٌۭ","ayah_ref":"88:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000569/B001","root_000709/B002","root_000871/B001","root_000871/B004","root_001525/B002"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000871","role":"The fitted support branch gives bodily form to the transition from effort into rest.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000871","role":"Repeated alignment makes the rest publicly and plurally available rather than private or accidental.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001525","role":"Softness and ease supply the bodily quality realized by the cushions.","root":"ن ع م","source_ref":"88:8","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000709","role":"Work and earned action supply the completed movement whose result is now inhabitable.","root":"س ع ي","source_ref":"88:9","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000569","role":"Contentment closes the causal arc from effort to a fitting place of repose.","root":"ر ض و","source_ref":"88:9","source_word_indices":["2"]}],"changed_reading":{"after":"The cushions are effort's completed spatial answer: satisfaction has become a prepared place where the body can stop striving.","before":"The cushions indicate generic luxury."},"confidence":"strong","mechanism":"Soft well-being is explicitly related to completed effort and satisfaction. The fitted row makes that relation spatial: prior striving has an outcome one can physically enter, occupy, and lean into.","model_id":"ctx_earned_rest_made_spatial","reader_inference":"The packet supplies ease, striving, satisfaction, and fitted supports; I infer that the environment materializes the result of the striving. The alternative is that effort and furniture are independent items in a reward list.","status":"strengthened","structural_cues":["The satisfied faces and their striving immediately precede the environmental inventory.","The furnishing sequence converts an affective result into occupiable material conditions."],"trigger_roots":["ن ع م","س ع ي","ر ض و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:ctx_earned_rest_made_spatial","source_type":"hft","support_id":"sup_0f51d6251290fafdcc90","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِى جَنَّةٍ عَالِيَةٍۢ","ayah_ref":"88:10"},{"arabic_uthmani":"لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ","ayah_ref":"88:11"},{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","ayah_ref":"88:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000266/B003","root_000741/B001","root_000871/B001","root_000871/B007","root_001361/B003"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_000871","role":"The gathering branch supplies plural convergence rather than solitary comfort.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000871","role":"Even spacing converts convergence into calm social choreography.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000266","role":"The tree-sheltered garden supplies the bounded social environment in which the row operates.","root":"ج ن ن","source_ref":"88:10","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000741","role":"Literal hearing makes acoustic experience an explicit property of the setting.","root":"س م ع","source_ref":"88:11","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001361","role":"Mixed din supplies the excluded crowd-condition against which ordered gathering is heard.","root":"ل غ و","source_ref":"88:11","source_word_indices":["4"]}],"changed_reading":{"after":"The alignment is social and acoustic architecture, permitting communal presence without crowd-noise or rivalry.","before":"The alignment has only visual symmetry."},"confidence":"medium","mechanism":"A sheltered garden removes mixed, worthless noise. Within it, rows do social work: they gather people while preserving intervals and orientation, producing co-presence without the acoustic disorder of an undifferentiated crowd.","model_id":"ctx_quiet_social_choreography","reader_inference":"The packet supplies sheltered space, excluded din, gathering, and even rows; I infer that spatial ordering helps produce quiet co-presence. The alternative is that silence is guaranteed independently of seating form.","status":"new","structural_cues":["The absence of futile sound is stated before the sequence of communal furnishings.","Plural objects are arranged by distinct spatial operations rather than heaped together."],"trigger_roots":["ج ن ن","س م ع","ل غ و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:ctx_quiet_social_choreography","source_type":"hft","support_id":"sup_568a493fbe1cc62a81d2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ","ayah_ref":"88:13"},{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","ayah_ref":"88:14"},{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","ayah_ref":"88:15"},{"arabic_uthmani":"وَزَرَابِىُّ مَبْثُوثَةٌ","ayah_ref":"88:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000083/B001","root_000582/B001","root_000697/B011","root_000871/B001","root_000871/B004","root_001657/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000871","role":"Linear serialization supplies the connector between isolated placements and wide dispersal.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000871","role":"The fitted bench-or-pad image makes that connector usable at bodily scale.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B011","mapped_root_id":"root_000697","role":"A place of settling and leaning supplies the supported resting station.","root":"س ر ر","source_ref":"88:13","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000582","role":"Elevation establishes the vertical layer of the furnishing field.","root":"ر ف ع","source_ref":"88:13","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001657","role":"Placement in a determined position establishes discrete service points.","root":"و ض ع","source_ref":"88:14","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000083","role":"Dispersal supplies the broad floor field that prevents the row from becoming total regimentation.","root":"ب ث ث","source_ref":"88:16","source_word_indices":["2"]}],"changed_reading":{"after":"It contributes the linear operator in a designed field: elevated support, fixed service, serial bodily access, and distributed floor space work together.","before":"The verse contributes one more luxurious object to a list."},"confidence":"strong","mechanism":"The adjacent furnishings enact four nonredundant operations: support is elevated, vessels are set at access points, cushions are serialized, and floor coverings are dispersed. The cushion row is the middle-scale connector between fixed stations and an open field.","model_id":"ctx_four_operation_furnishing_field","reader_inference":"The packet supplies adjacent passive placement forms and distinct branch mechanics; I infer a coordinated spatial system with the row as mediator. The alternative is a cumulative inventory of abundance with no designed interaction among operations.","status":"revised","structural_cues":["Four neighboring passive descriptions vary the spatial operation while keeping a parallel grammatical frame.","The focus lies between determined placement and broad dispersal, giving linear order a mediating scale."],"trigger_roots":["س ر ر","ر ف ع","و ض ع","ب ث ث"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:ctx_four_operation_furnishing_field","source_type":"hft","support_id":"sup_ce2ab0ef41aa0e3dac91","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِى جَنَّةٍ عَالِيَةٍۢ","ayah_ref":"88:10"},{"arabic_uthmani":"فِيهَا عَيْنٌۭ جَارِيَةٌۭ","ayah_ref":"88:12"},{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","ayah_ref":"88:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000240/B001","root_000266/B003","root_000871/B001","root_000871/B006","root_001069/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000871","role":"The willow offshoot supplies a soft linear vegetation image at the edge of water.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000871","role":"The even row gives the vegetative image a bounded edge rather than an unstructured thicket.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000266","role":"The tree-sheltered garden provides an ecological setting for the remote willow image.","root":"ج ن ن","source_ref":"88:10","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_001069","role":"The water source supplies the riparian center beside which a willow-like edge can be imagined.","root":"ع ي ن","source_ref":"88:12","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000240","role":"Flow gives direction to the edge and keeps the image spatial rather than merely botanical.","root":"ج ر ي","source_ref":"88:12","source_word_indices":["3"]}],"changed_reading":{"after":"Exploratorily, its soft linearity echoes a planted riparian boundary, integrating bodily comfort with garden and flowing-water form.","before":"The cushion row is an indoor line detached from the garden ecology."},"confidence":"exploratory","containment":"This is surprising because it carries the remote willow branch of the focus root into a garden scene. It remains anchored by the focus root, linear arrangement, sheltered vegetation, and flowing water. Downstream prose should retain it only as a visual-spatial undertone of a soft planted edge, never as a lexical replacement of cushions by trees.","focus_anchor":"A willow branch exists inside the focus root inventory, while the literal focus still provides a row capable of reading as an edge.","outlier_id":"outlier_riparian_soft_boundary"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_riparian_soft_boundary","source_type":"hft","support_id":"sup_800b077d573c0b7a322b","trust":"legacy_unbound"}]}
</lane_packet_json>
