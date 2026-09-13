# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **88:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_3/macro.discovery.json` and modify nothing
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
  "ayah_ref": "88:3",
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
{"branch_registry":[{"boundary":"Includes continuing provision, stipend, grant, or charity, and ajraytu lahu meaning I made it continue for him","branch_kind":null,"branch_ref":"root_000240/B006","candidate_links":[{"candidate_id":"cand_8e5fc53d5e94adf52da3","lane":"macro"}],"focus_root_occurrences":[],"gloss":"ongoing provision or grant","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"دوام الرزق والعطاء","image_en":"ongoing provision or grant"}}],"root_ar":"ج ر ي","root_id":"root_000240","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"دوام الرزق والعطاء","image_en":"ongoing provision or grant","scope_ar":"يدخل فيه الرزق أو العطاء أو الصدقة الجارية وما أجري للمرء بمعنى أديم له","scope_en":"Includes continuing provision, stipend, grant, or charity, and ajraytu lahu meaning I made it continue for him"},"support_links":["sup_b0457721f1f3b8948cdf"]},{"boundary":"This branch covers action, earning, work, endeavor, and active conduct in good or bad matters.","branch_kind":null,"branch_ref":"root_000709/B002","candidate_links":[{"candidate_id":"cand_8e5fc53d5e94adf52da3","lane":"macro"},{"candidate_id":"cand_4d35782418e948ab7ab5","lane":"macro"}],"focus_root_occurrences":[],"gloss":"work, earning, and active endeavor","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"عمل وكسب وتصرف","image_en":"work, earning, and active endeavor"}}],"root_ar":"س ع ي","root_id":"root_000709","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"عمل وكسب وتصرف","image_en":"work, earning, and active endeavor","scope_ar":"يدخل فيه كل عمل من خير أو شر، والكسب، والتصرف في كل عمل، والجد في الأمر، والسعي على العيال أو في الصلاح والفساد.","scope_en":"This branch covers action, earning, work, endeavor, and active conduct in good or bad matters."},"support_links":["sup_173417c5c70549c3170f","sup_b0457721f1f3b8948cdf"]},{"boundary":"Includes being well provided, receiving provision, generous feeding, earnings, estate grants, revenue, tribute, and legal share.","branch_kind":null,"branch_ref":"root_000934/B004","candidate_links":[{"candidate_id":"cand_8e5fc53d5e94adf52da3","lane":"macro"},{"candidate_id":"cand_1a4c72f4247fbd42755c","lane":"macro"}],"focus_root_occurrences":[],"gloss":"Provision, livelihood, and good condition","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"رزق ومعاش وحسن حال","image_en":"Provision, livelihood, and good condition"}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"رزق ومعاش وحسن حال","image_en":"Provision, livelihood, and good condition","scope_ar":"يدخل فيه الطاعم حسن الحال والمطعم المرزوق والمطعام كثير القرى والطعمة مأكلة أو وجه مكسب أو ضيعة أو فيء وخراج","scope_en":"Includes being well provided, receiving provision, generous feeding, earnings, estate grants, revenue, tribute, and legal share."},"support_links":["sup_b0457721f1f3b8948cdf","sup_b54537c25533fd9ee37d"]},{"boundary":"Kapsam, bilinçli yapılan iş ve eylemle sınırlıdır; ücret, resmi görev, karşılıklı alışveriş ve nesne ya da beden parçası adları ayrı kollardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001046/B001","candidate_links":[{"candidate_id":"cand_dade14e1aaeecd43ee99","lane":"macro"},{"candidate_id":"cand_4d35782418e948ab7ab5","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَامِلَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAmilap|ROOT:Eml|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:1:1","qac_word_ref":"88:3:1","surface_ar":"عَامِلَةٌ"}],"gloss":"bilerek yapılan iş veya eylem","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yapanın bilerek ortaya koyduğu iş veya eylem anlamı çekirdektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İyi ve kötü davranışlar da bilinçli eylem alanı içinde yer alır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişinin kendisi için çalışması veya işe dalması bu çekirdeğin özel bir görünümüdür."}}],"root_ar":"ع م ل","root_id":"root_001046","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bilinçli yapma ve iş görme çekirdeğini karşılar; ahlaki iyi veya kötü davranış bağlamlarında da kullanılabilir.","boundary_detail":"Kapsam, bilinçli yapılan iş ve eylemle sınırlıdır; ücret, resmi görev, karşılıklı alışveriş ve nesne ya da beden parçası adları ayrı kollardır.","concept_gloss":"bilerek yapılan iş veya eylem","contextual_glosses":[{"applicability":"Bir kişinin iş görmesi veya emek vermesi anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel bilinçli eylem ve iyi ya da kötü davranış kapsamını daraltır.","preserves":"İş görme ve çaba harcama yanını korur."},"facet_ids":["F001","F003"],"text":"çalışmak","usage_role":"contextual"},{"applicability":"İyi veya kötü tutum ve eylemlerden söz eden ahlaki bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Somut iş görme ve çalışma tarafını geri plana iter.","preserves":"Bilinçli eylemin ahlaki davranışa uygulanmasını korur."},"facet_ids":["F002"],"text":"davranış","usage_role":"contextual"}],"definition":"Canlı bir yapanın bilerek gerçekleştirdiği iş veya eylemdir; iyi ya da kötü davranışları da kapsayabilir. Kendisi için çalışmak ya da işe yoğun biçimde girişmek bu çekirdeğin özel kullanımıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yapanın bilerek ortaya koyduğu iş veya eylem anlamı çekirdektir."},{"facet_id":"F002","role":"extension","statement":"İyi ve kötü davranışlar da bilinçli eylem alanı içinde yer alır."},{"facet_id":"F003","role":"specialization","statement":"Kişinin kendisi için çalışması veya işe dalması bu çekirdeğin özel bir görünümüdür."}],"identity_rationale":"Kaynak ifadesi bu kolu, canlı bir yapanın bilerek ortaya koyduğu iş veya eylem olarak kurar. İyi ve kötü davranış örnekleri bu çekirdeğin ahlaki alanlara da uygulanabildiğini gösterir; ücret, görev, karşılıklı işlem veya özel adlar bu kola ait değildir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bilerek yapılan iş veya eylem"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"iş yapan kimse"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kendisi için çalışmak veya işe koyulmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"iş veya uğraş"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"işte kullanılan sığırlar"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"iyi ve kötü davranışlar"}],"lexicalization_note":"Hem yalın iş anlamı hem de belirli kalıplı kullanımlar vardır; tanım yalın çekirdeği verir, kalıplı örnekleri bu çekirdeğe bağlı tutar.","neighbor_coverage_note":"Adayların çoğu iş, yapma, kazanç, görev veya terk alanından gelir; en yararlı sınırlar iş yapma, işe koşma, ücret ve yapma komşularında görünür.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol işi gerçekleştiren yapanın eylemini tanımlar; komşu kol ise başka bir kişiyi ya da aracı çalıştırma, kullanma veya ondan iş isteme yönüne geçer.","focus_only":"İşi yapan öznenin kendi bilinçli eylemini bildirir.","gloss":"iş yapmak ile işe koşmak","neighbor_only":"Bir kişiyi, nesneyi, düşünceyi veya aracı işe koşma ve kullanma ilişkisini bildirir.","neighbor_ref":"root_001046/B002","relation_type":"near_neighbor","shared_zone":"Her ikisi de iş görme ve etkinliği yürütme alanındadır."},{"boundary_match":"field_only","distinction":"Bu kol işin yapılmasını anlatır; komşu kol, işin sonucunda çalışana verilen karşılığı adlandırır.","focus_only":"Yapılan işin veya eylemin kendisidir.","gloss":"iş ile iş ücreti","neighbor_only":"O işin karşılığında verilen ücret veya paydır.","neighbor_ref":"root_001046/B004","relation_type":"same_field","shared_zone":"İş alanını paylaşırlar, fakat biri eylem, diğeri karşılıktır."},{"boundary_match":"partial","distinction":"Komşu kol üretme ve yapma alanına daha çok yaslanır; bu kol ise bilinçli iş ve davranış kapsamını çekirdekte tutar.","focus_only":"Canlı yapanın bilinçli işini ve iyi ya da kötü davranışını kapsar.","gloss":"iş yapmak ile yapmak","neighbor_only":"Bir şeyi yapma veya meydana getirme tarafı daha belirgindir.","neighbor_ref":"root_000885/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de bir eylemin ortaya konmasını anlatabilir."}],"source_summary":"Kanıt, anlamı canlı bir yapanın bilinçli biçimde yaptığı iş veya eylem olarak toplar; bu kapsam iyi ve kötü davranış örneklerine de uygulanır."},"support_links":["sup_173417c5c70549c3170f","sup_7c7aa593f7a7ba764f63"]},{"boundary":"Tanım işe koşma ve kullanma yapılarıyla sınırlıdır; resmi görev üstlenme ve ücret alma bu kola taşınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001046/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَامِلَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAmilap|ROOT:Eml|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:1:1","qac_word_ref":"88:3:1","surface_ar":"عَامِلَةٌ"}],"gloss":"işe koşmak veya kullanmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birini veya bir şeyi işe koşma ve kullanma ana anlamdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birinden çalışma isteme de aynı kullanım alanına bağlıdır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Görüş, söz, mızrak, yapı malzemesi veya zihin gibi araçlar bu işe koşma alanında geçer."}}],"root_ar":"ع م ل","root_id":"root_001046","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiyi, aracı, düşünceyi ya da malzemeyi bir işlev için devreye sokma bağlamlarında uygundur.","boundary_detail":"Tanım işe koşma ve kullanma yapılarıyla sınırlıdır; resmi görev üstlenme ve ücret alma bu kola taşınmaz.","concept_gloss":"işe koşmak veya kullanmak","contextual_glosses":[{"applicability":"Bir kişinin iş yapması sağlandığında ya da ondan çalışma istendiğinde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesne, düşünce, söz veya malzeme kullanma kapsamını daraltır.","preserves":"Başkasını işe sokma tarafını korur."},"facet_ids":["F001","F002"],"text":"çalıştırmak","usage_role":"contextual"},{"applicability":"Düşünerek bir işi kavrama veya tasarlama örneğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka kişi, nesne ve araç kullanma alanını dışarıda bırakır.","preserves":"Zihni bir işlev için devreye sokmayı korur."},"facet_ids":["F003"],"text":"zihnini işletmek","usage_role":"contextual"}],"definition":"Bir kişiyi, nesneyi, düşünce gücünü ya da aracı işe koşmak ve ondan yararlanmaktır; bazen birinden iş yapmasını istemeyi de kapsar. Anlam, kullanma ve çalıştırma yapılarında kalır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birini veya bir şeyi işe koşma ve kullanma ana anlamdır."},{"facet_id":"F002","role":"extension","statement":"Birinden çalışma isteme de aynı kullanım alanına bağlıdır."},{"facet_id":"F003","role":"example","statement":"Görüş, söz, mızrak, yapı malzemesi veya zihin gibi araçlar bu işe koşma alanında geçer."}],"identity_rationale":"Kaynak ifadesi, başkasını çalıştırma, birinden iş isteme ve görüş, söz, mızrak, yapı malzemesi veya zihin gibi şeyleri kullanma örneklerini aynı işe koşma alanında toplar. Bu, genel iş yapma değil, bir şeyi veya birini işlevde kullanma anlamıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"onu çalıştırdı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"onu kullandı veya çalıştırdı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"ondan çalışmasını istedi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"görüşünü, sözünü veya mızrağını kullandı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kerpici yapıda kullandı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"zihnini işletip düşündü"}],"lexicalization_note":"Yalın olmayan formlar ve kalıplı kullanımlar birlikte gelir; tanım bu kullanma ve çalıştırma yapılarının sınırı içinde kalır.","neighbor_coverage_note":"Adaylar kullanma, hizmet, araç ve görev alanlarına yayılır; en net sınırlar genel iş, hizmet ve görevlendirme komşularındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol çalıştırma ve kullanma yönündedir; komşu kol, işi yapanın kendi eylemini adlandırır.","focus_only":"Birini veya bir şeyi işlev için devreye sokar.","gloss":"işe koşmak ile iş yapmak","neighbor_only":"Yapanın kendi bilinçli işini veya davranışını anlatır.","neighbor_ref":"root_001046/B001","relation_type":"near_neighbor","shared_zone":"İş görme alanını paylaşırlar."},{"boundary_match":"partial","distinction":"Komşu kol hizmet ilişkisinin toplumsal yönünü taşır; bu kol kullanım ve çalıştırma işleminin kendisini tanımlar.","focus_only":"Kişi, araç, zihin veya malzemeyi işe koşabilir.","gloss":"kullanmak ile hizmet etmek","neighbor_only":"Hizmet etme, hizmet eden kişi ve hizmet ilişkisi öne çıkar.","neighbor_ref":"root_001511/B004","relation_type":"near_neighbor","shared_zone":"Bir kişinin ya da şeyin bir iş için kullanılması alanında buluşurlar."},{"boundary_match":"field_only","distinction":"Bu kol kullanma ve işe koşmayı anlatır; komşu kol, resmi veya belirli bir iş üzerinde yetki ve görev verilmesini anlatır.","focus_only":"Bir şeyi veya kişiyi işlevde kullanma eylemidir.","gloss":"kullanma ile görevlendirme","neighbor_only":"Bir göreve yetkili kılma veya o görevi yürütme alanıdır.","neighbor_ref":"root_001046/B003","relation_type":"same_field","shared_zone":"İş ve görev alanı ortaktır."}],"source_summary":"Kanıt, başkasını veya bir aracı işe koşmayı ana anlam yapar; çalışma isteme, düşünceyi işletme ve yapı malzemesini kullanma örnekleri bu çekirdeğe bağlıdır."},"support_links":[]},{"boundary":"Kapsam iş üzerinde görev ve yetkiyle sınırlıdır; genel eylem, işe koşma ve ücret anlamları ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_001046/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَامِلَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAmilap|ROOT:Eml|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:1:1","qac_word_ref":"88:3:1","surface_ar":"عَامِلَةٌ"}],"gloss":"işe görevli kılma veya görev üstlenme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş üzerinde görev ve yetki üstlenme ana anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağış toplama görevlileri bu yetkili iş yürütme alanına girer."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birini bir işin başına geçirmek, görevlendirme tarafını gösterir."}}],"root_ar":"ع م ل","root_id":"root_001046","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin başına geçirilme, resmi görev alma veya bağış toplama işiyle yetkili olma bağlamlarında uygundur.","boundary_detail":"Kapsam iş üzerinde görev ve yetkiyle sınırlıdır; genel eylem, işe koşma ve ücret anlamları ayrı tutulur.","concept_gloss":"işe görevli kılma veya görev üstlenme","contextual_glosses":[{"applicability":"Bir kimseyi belirli bir işin başına getirme bağlamında en doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Görevi fiilen üstlenme ve yürütme tarafını tek başına vermez.","preserves":"Birine görev verme tarafını korur."},"facet_ids":["F003"],"text":"görevlendirmek","usage_role":"contextual"},{"applicability":"İş üzerinde yetkili kişi veya bağış toplayan kişi anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Görevlendirme eylemini ve işin başına geçme sürecini daraltır.","preserves":"Yetkili kişi anlamını korur."},"facet_ids":["F001","F002"],"text":"görevli","usage_role":"contextual"}],"definition":"Bir kimseye belirli veya resmi bir iş üzerinde görev ve yetki verilmesi ya da onun bu işi yürütmesidir. Bağış toplama görevlileri bu anlamın özel bir alanıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş üzerinde görev ve yetki üstlenme ana anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Bağış toplama görevlileri bu yetkili iş yürütme alanına girer."},{"facet_id":"F003","role":"extension","statement":"Birini bir işin başına geçirmek, görevlendirme tarafını gösterir."}],"identity_rationale":"Kaynak ifadesi bu kolu, belirli bir işin başına geçirilme, resmi iş üstlenme ve bağış toplama görevlileri üzerinden kurar. Bu, işi yapmakla bağlantılı olsa da çekirdeği yetki ve görev üstlenmedir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bağışları toplayan görevliler"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bağış işi görevlisi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"resmi bir işi üstlendi"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"birine iş görevi verme"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bir kimseyi bir şehirde görevli kılmak"}],"lexicalization_note":"Formlar ve kalıplar birlikte görünür; tanım görev üstlenme ve göreve atama sınırını korur.","neighbor_coverage_note":"Adaylar yetki, gözetim, idare ve ödeme alanındadır; en güçlü sınırlar genel yetki kolları ve ücret koluyla kurulur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol iş görevine atanma ve onu yürütme çevresinde daralır; komşu kol daha genel yetki ve idare anlamına açılır.","focus_only":"Belirli bir iş veya bağış toplama işi üzerinde görevli olma sınırı vardır.","gloss":"iş görevi ile yönetim","neighbor_only":"Genel yetki, yönetim ve bir kişinin işini gözetme alanı daha geniştir.","neighbor_ref":"root_001684/B003","relation_type":"near_synonym","shared_zone":"Her ikisi de bir işi veya durumu üstlenip yürütme alanındadır."},{"boundary_match":"partial","distinction":"Komşu kol topluluğu yöneten veya izleyen kişiye genişler; bu kol iş görevinin verilmesi ve yürütülmesine bağlı kalır.","focus_only":"İş üzerinde görevlendirme ve görev üstlenme vurgusu taşır.","gloss":"görevli ile yönetici","neighbor_only":"Bir topluluk üzerinde yetki, başkanlık veya izleme tarafı daha belirgindir.","neighbor_ref":"root_000709/B003","relation_type":"near_synonym","shared_zone":"Bağış toplama görevlisi ve bir işin başında bulunma alanları örtüşür."},{"boundary_match":"field_only","distinction":"Bu kol görev ve yetkiyi tanımlar; komşu kol görev veya iş karşılığında alınan maddi karşılığı tanımlar.","focus_only":"İşin yetkili biçimde üstlenilmesidir.","gloss":"görev ile ücret","neighbor_only":"İşin karşılığında verilen ücrettir.","neighbor_ref":"root_001046/B004","relation_type":"same_field","shared_zone":"Her ikisi de iş kurumuyla ilgilidir."}],"source_summary":"Kanıt, anlamı iş üzerinde yetki ve görev üstlenme etrafında toplar; bağış toplama görevlileri ve birini bir bölge ya da iş için görevlendirme örnekleri bu çekirdeğe bağlıdır."},"support_links":[]},{"boundary":"Kapsam iş karşılığı verilen ücret ya da paydır; işçi topluluğu ve iş eylemi ayrı kollardır.","branch_kind":"bare","branch_ref":"root_001046/B004","candidate_links":[{"candidate_id":"cand_8e5fc53d5e94adf52da3","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَامِلَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAmilap|ROOT:Eml|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:1:1","qac_word_ref":"88:3:1","surface_ar":"عَامِلَةٌ"}],"gloss":"iş ücreti","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İş karşılığı verilen ücret veya çalışanın payı ana anlamdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çalışanın geçimliği veya kazancı olarak da anlaşılır."}}],"root_ar":"ع م ل","root_id":"root_001046","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çalışana yaptığı işin karşılığı olarak verilen ücret veya pay anlatıldığında doğrudan uygundur.","boundary_detail":"Kapsam iş karşılığı verilen ücret ya da paydır; işçi topluluğu ve iş eylemi ayrı kollardır.","concept_gloss":"iş ücreti","contextual_glosses":[{"applicability":"Ücretin yapılan işe bağlı olduğunu vurgulamak gereken yerlerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İş ve karşılık ilişkisini korur."},"facet_ids":["F001"],"text":"çalışma karşılığı","usage_role":"contextual"}],"definition":"Bir işin karşılığında çalışana verilen ücret, pay veya geçimliktir. Bu anlam işin kendisi ya da işi yapan kişilerin topluluğu değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İş karşılığı verilen ücret veya çalışanın payı ana anlamdır."},{"facet_id":"F002","role":"associated_use","statement":"Çalışanın geçimliği veya kazancı olarak da anlaşılır."}],"identity_rationale":"Kaynak ifadesi bu kolu iş karşılığı verilen ücret, pay veya çalışanın geçimliği olarak açıklar. İşin kendisi ve işi yapan topluluk özellikle dışarıda kalır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"iş karşılığı ücret veya pay"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"iş ücreti"}],"lexicalization_note":"Mekanik profil yalın anlam verir; tanım yalnız ücret ve pay çekirdeğini işler, kalıplı görev veya eylem anlamı eklemez.","neighbor_coverage_note":"Adaylar karşılık, geçim, kazanç ve işçi alanlarındadır; ücretin eylemden ve işçi topluluğundan ayrılması ana sınırdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu kol genel karşılık ve ödül alanına yayılır; bu kol iş yapanın iş karşılığı aldığı ücrette kalır.","focus_only":"Özellikle iş yapan kişinin iş karşılığı aldığı paydır.","gloss":"iş ücreti ile karşılık","neighbor_only":"Karşılık, ödül, kira, yarar ve sözleşme ücreti gibi daha geniş alanları kapsar.","neighbor_ref":"root_000015/B001","relation_type":"near_synonym","shared_zone":"Yapılan bir iş için verilen karşılık alanında örtüşürler."},{"boundary_match":"partial","distinction":"Bu kol çalışan payı veya ücretidir; komşu kol belirli bir işi yaptırmak için konmuş ödül ya da anlaşılmış karşılık anlamına kayar.","focus_only":"Çalışanın yaptığı işin olağan karşılığıdır.","gloss":"iş ücreti ile vaatli ödül","neighbor_only":"Bir iş için önceden belirlenmiş ödül veya vaat edilen karşılık yönü öne çıkar.","neighbor_ref":"root_000248/B005","relation_type":"near_synonym","shared_zone":"Her ikisi de bir işin karşılığında verilen şeydir."},{"boundary_match":"field_only","distinction":"Bu kol maddi karşılığı adlandırır; komşu kol işi yapan insan topluluğunu adlandırır.","focus_only":"İş karşılığında verilen ücrettir.","gloss":"ücret ile işçiler","neighbor_only":"Elle çalışan işçi topluluğudur.","neighbor_ref":"root_001046/B006","relation_type":"same_field","shared_zone":"İş ve çalışma alanını paylaşırlar."}],"source_summary":"Kanıt, anlamı yapılan işin karşılığı olan ücret, pay veya çalışana ayrılan geçimlik olarak birleştirir."},"support_links":["sup_b0457721f1f3b8948cdf"]},{"boundary":"Kapsam kişiler arasındaki karşılıklı işlemle sınırlıdır; genel iş, ücret ve resmi görev anlamları dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_001046/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَامِلَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAmilap|ROOT:Eml|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:1:1","qac_word_ref":"88:3:1","surface_ar":"عَامِلَةٌ"}],"gloss":"karşılıklı işlem","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiyle karşılıklı işlem yürütme ana anlamdır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Alışveriş bu karşılıklı işlem alanının belirgin örneğidir."}}],"root_ar":"ع م ل","root_id":"root_001046","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki taraf arasında alışveriş veya benzeri iş ilişkisi yürütüldüğünde uygundur.","boundary_detail":"Kapsam kişiler arasındaki karşılıklı işlemle sınırlıdır; genel iş, ücret ve resmi görev anlamları dışarıda kalır.","concept_gloss":"karşılıklı işlem","contextual_glosses":[{"applicability":"Karşılıklı işlemin satış ve satın alma bağlamında geçtiği yerlerde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Alışveriş dışındaki karşılıklı işlem alanlarını dışarıda bırakır.","preserves":"İki taraflı alışveriş ilişkisini korur."},"facet_ids":["F001","F002"],"text":"alışveriş yapmak","usage_role":"contextual"}],"definition":"İki kişi arasında alışverişte veya benzeri işlerde karşılıklı işlem yürütmektir. Tek taraflı iş yapma ya da iş karşılığı ücret alma anlamı taşımaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiyle karşılıklı işlem yürütme ana anlamdır."},{"facet_id":"F002","role":"example","statement":"Alışveriş bu karşılıklı işlem alanının belirgin örneğidir."}],"identity_rationale":"Kaynak ifadesi, bir kişiyle alışverişte ve benzeri işlerde karşılıklı işlem yürütmeyi anlatır. Bu nedenle kol, tek başına iş yapma ya da iş ücreti değil, kişiler arası işlem ilişkisidir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"karşılıklı işlem veya alışveriş ilişkisi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir kimseyle alışveriş veya benzeri işlem yaptı"}],"lexicalization_note":"Form ve kalıp birlikte verilir; tanım karşılıklı işlem yapısına bağlı kalır ve yalın iş anlamına genişletilmez.","neighbor_coverage_note":"Adaylar alışveriş, bedel, iki taraflılık ve borç ilişkisi çevresindedir; sınır en çok alım satım kollarıyla belirginleşir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu kol alım satımın kendi yönlerine odaklanır; bu kol kişiyle işlem yürütme ilişkisini daha genel tutar.","focus_only":"Alışveriş dışındaki karşılıklı işlemleri de kapsayabilir.","gloss":"işlem ile alım satım","neighbor_only":"Satış ve satın alma eylemleri ile bedel ilişkisi daha belirgindir.","neighbor_ref":"root_000169/B001","relation_type":"near_synonym","shared_zone":"İki taraf arasında mal veya bedel üzerinden işlem yapma alanında örtüşürler."},{"boundary_match":"partial","distinction":"Bu kol işlem ilişkisinin kişisel yönünü taşır; komşu kol alım ve satımın bedelli değişimini öne çıkarır.","focus_only":"Bir kişiyle işlem görme ilişkisi alışverişten daha geniştir.","gloss":"karşılıklı işlem ile alışveriş","neighbor_only":"Satın alma ve satma karşılıklılığı daha doğrudan adlandırılır.","neighbor_ref":"root_000792/B001","relation_type":"near_synonym","shared_zone":"Alışverişte iki taraflı değiş tokuş alanını paylaşırlar."},{"boundary_match":"field_only","distinction":"Bu kol karşılıklı ilişki şartı taşır; komşu kol tek yapanın eylemini de kapsayan genel iş alanıdır.","focus_only":"İki taraf arasında işlem yürütür.","gloss":"işlem ile iş","neighbor_only":"Bir yapanın bilinçli işini veya davranışını anlatır.","neighbor_ref":"root_001046/B001","relation_type":"same_field","shared_zone":"İş ve eylem alanı ortaktır."}],"source_summary":"Kanıt, anlamı bir kişiyle alışverişte veya başka işlerde karşılıklı işlem yürütme olarak verir; ilişki iki taraflıdır."},"support_links":[]},{"boundary":"Kapsam elle çalışan işçi topluluğudur; iş karşılığı ücret ve yaya yolcular anlamları ayrı kollardır.","branch_kind":"bare","branch_ref":"root_001046/B006","candidate_links":[{"candidate_id":"cand_19ec15bb49d40f156be0","lane":"macro"},{"candidate_id":"cand_8ecacbaebfbed32f1fe8","lane":"macro"},{"candidate_id":"cand_2a685e998ac06d27dee0","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَامِلَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAmilap|ROOT:Eml|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:1:1","qac_word_ref":"88:3:1","surface_ar":"عَامِلَةٌ"}],"gloss":"el işçileri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ellerini kullanarak çeşitli ağır işleri yapan insan topluluğu ana anlamdır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kazı, kuyu kaplama ve çamur işi verilen örnek iş türleridir."}}],"root_ar":"ع م ل","root_id":"root_001046","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ellerini kullanarak kazı, çamur işi veya benzeri işleri yapan insan topluluğu anlatıldığında uygundur.","boundary_detail":"Kapsam elle çalışan işçi topluluğudur; iş karşılığı ücret ve yaya yolcular anlamları ayrı kollardır.","concept_gloss":"el işçileri","contextual_glosses":[{"applicability":"El emeğiyle ağır iş yapan grup için konuşma diline yakın bir karşılık gerektiğinde kullanılabilir.","error_profile":{"adds":"Güncel Türkçede toplumsal ton ve kaba işçilik çağrışımı ekleyebilir.","collision":"Kaynak köke bağlı ödünç biçim olduğu için açıklayıcı ana karşılık yerine kullanılmamalıdır.","fit":"drifted_loanword","loses":null,"preserves":"Elle çalışan işçi topluluğu yanını korur."},"facet_ids":["F001"],"text":"amele takımı","usage_role":"contextual"}],"definition":"El emeğiyle kazı, kuyu kaplama, çamur işi ve benzeri işleri yapan işçi topluluğudur. Anlam, ücret veya yalnızca yapılan iş değil, işi yapan insan grubudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ellerini kullanarak çeşitli ağır işleri yapan insan topluluğu ana anlamdır."},{"facet_id":"F002","role":"example","statement":"Kazı, kuyu kaplama ve çamur işi verilen örnek iş türleridir."}],"identity_rationale":"Kaynak ifadesi bu kolu, elleriyle kazı, kuyu kaplama, çamur işi ve benzeri işleri yapan topluluk olarak verir. Bu, aynı yazılışla görülen ücret anlamından ve genel iş eyleminden ayrıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"elleriyle çalışan işçi topluluğu"}],"lexicalization_note":"Mekanik profil yalın ad anlamı verir; tanım işçi topluluğunu açıklar ve ücret ya da yolculuk anlamı eklemez.","neighbor_coverage_note":"Adaylar işçi, zanaat, araç, kazı ve ücret alanlarında toplanır; topluluk ile ücret ve beceri ayrımı en yararlı sınırdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu kol işçi veya zanaat yapan kişi alanını daha geniş tutar; bu kol özellikle elle çalışan topluluk olarak sınırlandırılır.","focus_only":"Elle çalışan topluluk anlamına bağlıdır.","gloss":"el işçileri","neighbor_only":"İşçi topluluğunun yanında belirli zanaat sahibi kişiye de açılabilir.","neighbor_ref":"root_001167/B003","relation_type":"near_synonym","shared_zone":"Her ikisi de çamur, kazı ve benzeri el işleri yapanları anlatır."},{"boundary_match":"field_only","distinction":"Bu kol insan grubudur; komşu kol beceri, meslek ve ustalık niteliğidir.","focus_only":"Elle çalışan işçi topluluğunu adlandırır.","gloss":"işçiler ile ustalık","neighbor_only":"El işi becerisi, zanaat ve ustalık niteliğini adlandırır.","neighbor_ref":"root_000885/B002","relation_type":"same_field","shared_zone":"El işi ve zanaat ortamını paylaşırlar."},{"boundary_match":"field_only","distinction":"Bu kol çalışanları gösterir; komşu kol çalışanlara verilen karşılığı gösterir.","focus_only":"İşi yapan insan topluluğudur.","gloss":"işçiler ile ücret","neighbor_only":"İşin karşılığı olan ücrettir.","neighbor_ref":"root_001046/B004","relation_type":"same_field","shared_zone":"İş ve çalışma alanını paylaşırlar."}],"source_summary":"Kanıt, anlamı elleriyle çeşitli işler yapan topluluk olarak verir; kazı, kuyu kaplama ve çamur işi bu iş türlerine örnektir."},"support_links":["sup_15967cee13181a9d7512","sup_411118ab1ab472386bde","sup_8bfde22d07df29c05989"]},{"boundary":"Kapsam kalıplı söyleyişlerde zahmet çekmedir; yalın iş yapmak veya kendisi için çalışmak anlamına genişletilmez.","branch_kind":"collocation","branch_ref":"root_001046/B007","candidate_links":[{"candidate_id":"cand_1a4c72f4247fbd42755c","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَامِلَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAmilap|ROOT:Eml|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:1:1","qac_word_ref":"88:3:1","surface_ar":"عَامِلَةٌ"}],"gloss":"zahmete girmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş uğruna zahmete girme ve kendini yorma ana anlamdır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yasaklama kalıbı, kişinin kendini yormamasını isteme olarak kullanılır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birinin ihtiyacı için zahmete girmeyi bildiren yardım bağlamı da verilir."}}],"root_ar":"ع م ل","root_id":"root_001046","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir iş veya başkasının ihtiyacı için kendini yorma anlatıldığında uygundur.","boundary_detail":"Kapsam kalıplı söyleyişlerde zahmet çekmedir; yalın iş yapmak veya kendisi için çalışmak anlamına genişletilmez.","concept_gloss":"zahmete girmek","contextual_glosses":[{"applicability":"Yasaklama veya uyarı bağlamında kişinin zahmet çekmemesi istendiğinde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasının ihtiyacı için olumlu biçimde zahmete girme yanını daraltır.","preserves":"Kendini yorma ve zahmet çekme yanını korur."},"facet_ids":["F001","F002"],"text":"kendini yorma","usage_role":"contextual"}],"definition":"Belirli anlatımlarda bir iş veya ihtiyaç için zahmete girme, kendini yorma anlamıdır. Bu kol genel çalışma ya da kendisi için iş yapma anlamına taşınmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş uğruna zahmete girme ve kendini yorma ana anlamdır."},{"facet_id":"F002","role":"example","statement":"Yasaklama kalıbı, kişinin kendini yormamasını isteme olarak kullanılır."},{"facet_id":"F003","role":"example","statement":"Birinin ihtiyacı için zahmete girmeyi bildiren yardım bağlamı da verilir."}],"identity_rationale":"Kaynak ifadesi bu kolu belirli kalıplarda zahmete girme veya kendini yorma anlamıyla verir. Genel çalışma ve kendisi için çalışma anlamları özellikle dışarıda bırakılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"kendini yorma"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"ihtiyacın için zahmete gireceğim"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"zahmet etme"}],"lexicalization_note":"Mekanik profil kalıplı kullanım verir; tanım yalnız bu yapılardaki zahmete girme anlamını kapsar.","neighbor_coverage_note":"Adaylar zorluk, güç harcama, ağır yük ve iş alanındadır; kalıplı zahmet anlamı genel çalışma anlamından ayrılmalıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol bir iş için bilerek zahmete girmeyi anlatır; komşu kol genel zorluk ve sıkıntı durumunu anlatır.","focus_only":"Zahmete girme anlamı belirli iş kalıplarına bağlıdır.","gloss":"zahmet ile zorluk","neighbor_only":"Sıkıntı, zorluk ve genel yorulma alanı daha geniştir.","neighbor_ref":"root_000809/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de yorgunluk ve sıkıntı veren uğraşı anlatabilir."},{"boundary_match":"partial","distinction":"Komşu kol kapasite ve sınırına kadar zorlanma anlamını taşır; bu kol belirli söz kalıplarında zahmet çekmeye bağlıdır.","focus_only":"Kalıplı söyleyişte kendini yorma veya zahmet etme anlamıdır.","gloss":"zahmet etmek ile güç harcamak","neighbor_only":"Gücü sonuna kadar harcama, yemin veya zorlu geçim gibi daha geniş alanları vardır.","neighbor_ref":"root_000268/B001","relation_type":"near_neighbor","shared_zone":"Çaba ve güç harcama alanı ortaktır."},{"boundary_match":"field_only","distinction":"Bu kol zahmet ve yorgunluk tarafını taşır; komşu kol her bilinçli işi kapsayan daha temel eylem alanıdır.","focus_only":"Zahmet çekme anlamı yalnız kalıplı kullanımdadır.","gloss":"zahmet etmek ile iş yapmak","neighbor_only":"Genel bilinçli iş veya eylem anlamıdır.","neighbor_ref":"root_001046/B001","relation_type":"same_field","shared_zone":"İş ve uğraş alanını paylaşırlar."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı tanıklık, hem yasaklama hem yardım bağlamında zahmete girme anlamını verir."}],"source_summary":"Kanıt, anlamı yalnız kalıplı söyleyişlerde zahmete girme veya kendini yorma olarak sınırlar; genel iş yapma anlamı burada taşınmaz."},"support_links":["sup_b54537c25533fd9ee37d"]},{"boundary":"Kapsam işe yatkınlık ve iş için yaratılıştan elverişliliktir; genel yapan kişi veya işçi topluluğu anlamı eklenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001046/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَامِلَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAmilap|ROOT:Eml|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:1:1","qac_word_ref":"88:3:1","surface_ar":"عَامِلَةٌ"}],"gloss":"işe yatkın ve dayanıklı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İşe yatkın ve çalışmaya elverişli olma niteliği ana anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan için çalışmaya yaratılıştan yatkın kişi niteliği verilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Deve için üstün, güçlü ve işe dayanıklı dişi deve adı olarak kullanılır."}}],"root_ar":"ع م ل","root_id":"root_001046","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çalışmaya yaratılıştan elverişli kişi veya işe dayanıklı üstün dişi deve anlatıldığında uygundur.","boundary_detail":"Kapsam işe yatkınlık ve iş için yaratılıştan elverişliliktir; genel yapan kişi veya işçi topluluğu anlamı eklenmez.","concept_gloss":"işe yatkın ve dayanıklı","contextual_glosses":[{"applicability":"Kişinin çalışmaya doğal olarak yatkın oluşu anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deve adı ve hayvana ilişkin üstünlük tarafını dışarıda bırakır.","preserves":"İnsan için işe yatkınlık niteliğini korur."},"facet_ids":["F001","F002"],"text":"çalışkan yaradılışlı","usage_role":"contextual"},{"applicability":"Deve adı veya nitelikli dişi deve bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan için çalışkan yaradılış anlamını dışarıda bırakır.","preserves":"Deveye ilişkin işe dayanıklılık ve üstünlük yanını korur."},"facet_ids":["F003"],"text":"işe dayanıklı dişi deve","usage_role":"contextual"}],"definition":"İşe yatkın veya çalışmaya yaratılıştan elverişli olma niteliğidir. İnsan için çalışkan yaradılış, deve için üstün ve işe dayanıklı dişi deve adı olarak görülür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İşe yatkın ve çalışmaya elverişli olma niteliği ana anlamdır."},{"facet_id":"F002","role":"specialization","statement":"İnsan için çalışmaya yaratılıştan yatkın kişi niteliği verilir."},{"facet_id":"F003","role":"specialization","statement":"Deve için üstün, güçlü ve işe dayanıklı dişi deve adı olarak kullanılır."}],"identity_rationale":"Kaynak ifadesi insan ve deve için işe yatkın, çalışmaya yaratılıştan elverişli olma niteliğini; deve adlarında ise üstün ve işe dayanıklı oluşu gösterir. Bu, sadece işi yapan kişi veya işçi topluluğu anlamı değildir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"işe yatkın üstün dişi deve"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"işe nispet edilen dişi deve"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"işe yatkın adam"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"işe yatkın çalışkan adam"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"işe yatkın, güçlü ve üstün dişi deve"}],"lexicalization_note":"Formlar ve kalıplar birlikte verilir; tanım insan niteliği ile deve adı arasındaki işe yatkınlık bağını korur.","neighbor_coverage_note":"Adaylar yatkınlık, dayanıklılık, hayvan niteliği ve çalışma alanındadır; kişi veya hayvan niteliği işçi ya da eylem anlamından ayrılmalıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu kol genel uygunluk ve hazırlığa açılır; bu kol iş görmeye yatkınlık ve dayanıklılık sınırındadır.","focus_only":"İşe ve çalışmaya yatkınlık alanına bağlıdır.","gloss":"işe yatkın ile elverişli","neighbor_only":"Genel elverişlilik, hazırlanmışlık ve iyiye yatkınlık daha geniştir.","neighbor_ref":"root_000434/B005","relation_type":"near_synonym","shared_zone":"Bir şey için uygun ve yatkın olma alanında örtüşürler."},{"boundary_match":"partial","distinction":"Bu kol iş görmeye doğal yatkınlık verir; komşu kol herhangi bir eyleme elverişli olma yargısına yayılır.","focus_only":"Çalışma ve işe dayanıklılık niteliğini taşır.","gloss":"işe yatkın ile yapmaya yatkın","neighbor_only":"Bir eylemi yapmaya yakın veya layık olma anlamı daha geneldir.","neighbor_ref":"root_001220/B008","relation_type":"near_synonym","shared_zone":"Bir eyleme uygun veya yatkın görülme alanını paylaşırlar."},{"boundary_match":"field_only","distinction":"Bu kol bir nitelik veya hayvan adıdır; komşu kol işi yapan insan topluluğunu adlandırır.","focus_only":"Kişi veya hayvan için iş görmeye yatkın niteliktir.","gloss":"işe yatkınlık ile işçiler","neighbor_only":"Elle çalışan işçi topluluğudur.","neighbor_ref":"root_001046/B006","relation_type":"same_field","shared_zone":"Çalışma ve iş görme alanı ortaktır."}],"source_summary":"Kanıt, insan ve deve örneklerini işe yatkınlık çevresinde birleştirir; deve adları üstünlük ve işe dayanıklılık niteliğini taşır."},"support_links":[]},{"boundary":"Kapsam mızrağın ucuna yakın gövde bölümüdür; mızrağın kendisi, sivri ucu ve kullanılması ayrı tutulur.","branch_kind":"non_bare","branch_ref":"root_001046/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَامِلَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAmilap|ROOT:Eml|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:1:1","qac_word_ref":"88:3:1","surface_ar":"عَامِلَةٌ"}],"gloss":"mızrak ucunun alt bölümü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Mızrağın sivri ucuna yakın ön gövde bölümü ana anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu bölüm sivri ucun kendisinden ve ucun dibindeki ayrı parçadan ayırt edilir."}}],"root_ar":"ع م ل","root_id":"root_001046","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Mızrağın sivri ucuna yakın, fakat ucun kendisi olmayan gövde parçası anlatıldığında uygundur.","boundary_detail":"Kapsam mızrağın ucuna yakın gövde bölümüdür; mızrağın kendisi, sivri ucu ve kullanılması ayrı tutulur.","concept_gloss":"mızrak ucunun alt bölümü","contextual_glosses":[{"applicability":"Parçanın mızraktaki konumunu okuyucuya açıklamak gerektiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sivri ucun hemen altındaki teknik sınırı tam belirtmeyebilir.","preserves":"Mızrağın ön bölümünü korur."},"facet_ids":["F001"],"text":"mızrağın ön gövdesi","usage_role":"explanatory"}],"definition":"Mızrağın sivri ucuna en yakın ön gövde bölümüdür; sivri uçtan ve uç dibindeki ayrı parçadan ayrılır. Anlam, mızrağın kullanılması değil mızraktaki konumdur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Mızrağın sivri ucuna yakın ön gövde bölümü ana anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Bu bölüm sivri ucun kendisinden ve ucun dibindeki ayrı parçadan ayırt edilir."}],"identity_rationale":"Kaynak ifadesi, mızrağın sivri ucuna yakın ön gövde bölümünü anlatır ve bunu uçtan ve uç dibindeki parçadan ayırır. Bu, mızrağı kullanma eylemi ya da hayvanın beden parçaları değildir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"mızrağın sivri ucuna yakın ön gövde bölümü"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"mızrağın ucuna yakın gövde bölümü"}],"lexicalization_note":"Mekanik profil yalın olmayan özel bir birim verir; tanım yalnız mızrak parçası ifadesine bağlıdır.","neighbor_coverage_note":"Adaylar mızrak, uç, bıçak kenarı ve silah parçaları çevresindedir; parçanın bütün silahtan ve sivri uçtan ayrımı yeterlidir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu kol mızrak üzerindeki konumlu bir parçadır; komşu kol çubuk ve silah parçaları alanında daha geniş adlandırmalar içerir.","focus_only":"Mızrağın ucuna yakın belli bir gövde bölümüdür.","gloss":"mızrak bölümü ile çubuk ve uç","neighbor_only":"İnce çubuk, mızrak, kısa mızrak ve sivri uç adları gibi daha geniş nesneler verir.","neighbor_ref":"root_000403/B007","relation_type":"same_field","shared_zone":"Mızrak, çubuk ve sivri uç çevresindeki nesne alanını paylaşırlar."},{"boundary_match":"partial","distinction":"Bu kol uca komşu gövde bölümünü anlatır; komşu kol silahın sivri ucunu veya ucu olan silahı anlatır.","focus_only":"Sivri ucun altında kalan gövde bölümüdür.","gloss":"mızrak gövdesi ile sivri uç","neighbor_only":"Sivri uç veya kesici uç kendisidir.","neighbor_ref":"root_000302/B004","relation_type":"near_neighbor","shared_zone":"Mızrağın ön kısmı ve saldırı ucu çevresinde buluşurlar."},{"boundary_match":"field_only","distinction":"Bu kol bütün silahı değil, silahın ucuna yakın bir parçasını adlandırır.","focus_only":"Mızrağın bir parçasıdır.","gloss":"mızrak parçası ile mızrak","neighbor_only":"Mızrağın bütünü, onu taşıyan veya onunla vuran kişi ve yapımıdır.","neighbor_ref":"root_000597/B001","relation_type":"same_field","shared_zone":"Mızrak nesnesi alanını paylaşırlar."}],"source_summary":"Kanıt, anlamı mızrağın sivri ucuna yakın ön gövde bölümü olarak birleştirir; bölüm, sivri uçtan ve ona komşu ayrı parçadan ayrılır."},"support_links":[]},{"boundary":"Kapsam kalıplı beden parçası adlarıdır; hayvanın ayakları ve uzağı gören göz örnekleri yalın bir genel organ anlamına genişletilmez.","branch_kind":"collocation","branch_ref":"root_001046/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَامِلَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAmilap|ROOT:Eml|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:1:1","qac_word_ref":"88:3:1","surface_ar":"عَامِلَةٌ"}],"gloss":"iş gören beden parçası","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalıplı kullanımlarda bedenin iş gören parçasını adlandırma ortak çerçevedir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvan için bu ad, onun ayaklarına uygulanır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Uzağı gören göz örneği de kalıplı ve şiirsel bir kullanımdır."}}],"root_ar":"ع م ل","root_id":"root_001046","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın ayakları veya uzağı gören göz gibi kalıplı beden parçası kullanımlarında açıklayıcı karşılıktır.","boundary_detail":"Kapsam kalıplı beden parçası adlarıdır; hayvanın ayakları ve uzağı gören göz örnekleri yalın bir genel organ anlamına genişletilmez.","concept_gloss":"iş gören beden parçası","contextual_glosses":[{"applicability":"Hayvanın yürümeyi sağlayan üyeleri anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzağı gören göz örneğini ve ortak iş gören parça çerçevesini daraltır.","preserves":"Hayvana ilişkin ayaklar kullanımını korur."},"facet_ids":["F002"],"text":"hayvanın ayakları","usage_role":"contextual"},{"applicability":"Gözün uzak görüş yeteneğiyle anıldığı örnekte uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanın ayakları kullanımını dışarıda bırakır.","preserves":"Göz ve uzak görüş örneğini korur."},"facet_ids":["F003"],"text":"uzağı gören göz","usage_role":"contextual"}],"definition":"Belirli tamlamalarda bedenin iş gören parçasına verilen addır: hayvan için ayaklar, bir örnekte uzağı gören göz. Bunlar çıplak bir genel organ adı olarak genelleştirilemez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalıplı kullanımlarda bedenin iş gören parçasını adlandırma ortak çerçevedir."},{"facet_id":"F002","role":"specialization","statement":"Hayvan için bu ad, onun ayaklarına uygulanır."},{"facet_id":"F003","role":"example","statement":"Uzağı gören göz örneği de kalıplı ve şiirsel bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi iki kalıplı kullanımı birlikte verir: hayvanın ayakları ve uzağı gören göz. Bunlar tek bir yalın organ adı değildir; kol ancak iş gören beden parçası fikriyle, kalıplı kullanımların sınırı açık tutulursa korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"hayvanın ayakları"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"uzağı gören göz"}],"lexicalization_note":"Mekanik profil kalıplı kullanımlar verir; tanım bu iki beden parçası örneğini genelleştirmeden açıklar.","neighbor_coverage_note":"Adaylar organ, göz, uzuv bozukluğu ve parça adlarıdır; bu kol kalıplı beden parçası kullanımı olarak sınırlandırılmalıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol iki özel beden parçası kullanımına bağlıdır; komşu kol organ veya parça anlamını genel olarak verir.","focus_only":"Yalnız kalıplı kullanımlarda iş gören parça adıdır.","gloss":"iş gören organ ile organ","neighbor_only":"Genel beden parçası, pay veya bölüm adıdır.","neighbor_ref":"root_000024/B003","relation_type":"near_neighbor","shared_zone":"Beden parçası ve bölüm adlandırması alanını paylaşırlar."},{"boundary_match":"field_only","distinction":"Bu kol göz örneğini iş gören beden parçası çerçevesinde kullanır; komşu kol göz adının kendisini ve bakış noktasını tanımlar.","focus_only":"Göz yalnız uzağı görme örneğinde, kalıplı bir kullanım olarak geçer.","gloss":"uzağı gören göz ile göz","neighbor_only":"Gözün kendisi ve gözdeki bakış yeri ana anlamdır.","neighbor_ref":"root_001520/B008","relation_type":"same_field","shared_zone":"Göz ve görme alanını paylaşırlar."},{"boundary_match":"field_only","distinction":"Bu kol canlı bedeniyle ilgilidir; komşu kol bir silahın yapısal parçasını adlandırır.","focus_only":"Beden parçası örneklerini verir.","gloss":"beden parçası ile mızrak parçası","neighbor_only":"Mızrağın ucuna yakın gövde parçasını verir.","neighbor_ref":"root_001046/B009","relation_type":"same_field","shared_zone":"Parça adı olma bakımından biçimsel bir komşuluk vardır."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı tanıklık, hayvanın ayaklarını ve uzağı gören gözü aynı kalıplı beden parçası alanında verir."}],"source_summary":"Kanıt, anlamı kalıplı beden parçası adlarıyla sınırlar; hayvanın ayakları ile uzağı gören göz aynı yalın anlam değil, iki özel kullanımdır."},"support_links":[]},{"boundary":"Kapsam kalıplı yol niteliğidir; genel yol anlamı ve yolculuk yapan kişiler ayrı tutulur.","branch_kind":"collocation","branch_ref":"root_001046/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَامِلَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAmilap|ROOT:Eml|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:1:1","qac_word_ref":"88:3:1","surface_ar":"عَامِلَةٌ"}],"gloss":"işlek yol","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yürünmüş ve işlek hale gelmiş yol ana anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yolun açık ve belirgin oluşu anlamın ayrılmaz parçasıdır."}}],"root_ar":"ع م ل","root_id":"root_001046","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Üzerinden geçile geçile belirginleşmiş açık yol anlatıldığında uygundur.","boundary_detail":"Kapsam kalıplı yol niteliğidir; genel yol anlamı ve yolculuk yapan kişiler ayrı tutulur.","concept_gloss":"işlek yol","contextual_glosses":[{"applicability":"Yolun açıklığı ve seçilebilirliği vurgulandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Üzerinden çok geçilerek işlekleşme tarafını zayıflatır.","preserves":"Yolun açık ve belirgin oluşunu korur."},"facet_ids":["F002"],"text":"belirgin yol","usage_role":"contextual"}],"definition":"Yürünerek belirginleşmiş, işlek ve açık yol anlamındaki kalıplı yol niteliğidir. Genel çalışma ya da işçi anlamı taşımaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yürünmüş ve işlek hale gelmiş yol ana anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Yolun açık ve belirgin oluşu anlamın ayrılmaz parçasıdır."}],"identity_rationale":"Kaynak ifadesi yalnızca işlek, yürünmüş ve belirgin yol niteliğini verir. Bu anlam iş yapmak, işçi topluluğu veya yaya yolcu adlandırması değildir.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"işlek ve belirgin yol"}],"lexicalization_note":"Mekanik profil kalıplı kullanım verir; tanım yalnız işlek yol ifadesi için geçerlidir.","neighbor_coverage_note":"Adaylar yol, ana yol, iz ve yolculuk alanındadır; en gerekli ayrım işlek yolun kişilerden ayrılmasıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol yolun kullanıla kullanıla belirginleşmesini öne çıkarır; komşu kol daha genel ana yol veya yolun kendisini anlatır.","focus_only":"İşlekleşmiş ve belirgin yol niteliğine bağlıdır.","gloss":"işlek yol ile ana yol","neighbor_only":"Ana yol veya geniş yol anlamı daha genel ve yerleşik olabilir.","neighbor_ref":"root_000214/B008","relation_type":"near_synonym","shared_zone":"Açık ve izlenen yol alanında örtüşürler."},{"boundary_match":"partial","distinction":"Bu kol işlekleşme niteliğine bağlıdır; komşu kol yolun açıklığını ve gidilen ana hattı daha geniş verir.","focus_only":"Yolun işlek ve yürünmüş oluşunu taşır.","gloss":"işlek yol ile açık yol","neighbor_only":"Yolun amaçlı, açık veya bazen kıvrımlı oluşu daha geniş anlatılır.","neighbor_ref":"root_000295/B002","relation_type":"near_synonym","shared_zone":"Belirgin ve izlenebilir yol alanını paylaşırlar."},{"boundary_match":"thematic_only","distinction":"Bu kol mekan ya da güzergah niteliğidir; komşu kol o güzergahı yürüyerek aşan kişilere aittir.","focus_only":"Yolun kendisini nitelendirir.","gloss":"işlek yol ile yaya yolcular","neighbor_only":"Yolda yürüyen yaya yolcuları adlandırır.","neighbor_ref":"root_001046/B012","relation_type":"thematic","shared_zone":"Yolculuk ve yolda yürüme sahnesini paylaşırlar."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı tanıklık, yolun yürünmüş, işlek ve açık niteliğini bildirir."}],"source_summary":"Kanıt, anlamı kalıplı biçimde işlek ve belirgin yol olarak verir; çalışma veya işçi alanına genişleme yoktur."},"support_links":[]},{"boundary":"Kapsam yaya yolcuları adlandıran kalıplı topluluk ifadesidir; el işçileri ve işlek yol anlamları dışarıda kalır.","branch_kind":"collocation","branch_ref":"root_001046/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَامِلَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAmilap|ROOT:Eml|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:1:1","qac_word_ref":"88:3:1","surface_ar":"عَامِلَةٌ"}],"gloss":"yaya yolcular","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yolculuk eden kişilerin yaya gitmesi ana anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırma kişilere yöneliktir, yolun kendisine veya işçilere değil."}}],"root_ar":"ع م ل","root_id":"root_001046","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yolculuk eden kişilerin yürüyerek gittiği topluluk bağlamında uygundur.","boundary_detail":"Kapsam yaya yolcuları adlandıran kalıplı topluluk ifadesidir; el işçileri ve işlek yol anlamları dışarıda kalır.","concept_gloss":"yaya yolcular","contextual_glosses":[{"applicability":"Kalıplı topluluk adını açıkça çözmek gerektiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yolcu, yaya gitme ve topluluk anlamını korur."},"facet_ids":["F001","F002"],"text":"yürüyerek giden yolcular","usage_role":"explanatory"}],"definition":"Yolculukta binek kullanmadan yürüyen yolcuları adlandıran kalıplı topluluk ifadesidir. El işçileri ya da yolun kendisi anlamına gelmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yolculuk eden kişilerin yaya gitmesi ana anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Adlandırma kişilere yöneliktir, yolun kendisine veya işçilere değil."}],"identity_rationale":"Kaynak ifadesi bu kolu yolculukta binek kullanmadan yürüyen kişiler için kalıplı bir topluluk adı olarak verir. İşçi topluluğu ve yolun kendisi bu kapsamda değildir.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"yaya giden yolcular"}],"lexicalization_note":"Mekanik profil kalıplı kullanım verir; tanım yalnız yaya yolcu topluluğu ifadesi için geçerlidir.","neighbor_coverage_note":"Adaylar yolcu, yol, yürüyüş ve yolculuk alanındadır; yaya yolcu topluluğu yolun kendisinden ve genel yolculardan ayrılır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol yolculuk eden yaya topluluğa bağlıdır; komşu kol yaya olma durumunu daha genel işler.","focus_only":"Yolculukta yaya giden kişilerin kalıplı topluluk adıdır.","gloss":"yaya yolcular ile yayalar","neighbor_only":"Yaya olma, bineksiz kalma, yürüme gücü ve yürüyerek gitme daha geniş biçimde anlatılır.","neighbor_ref":"root_000546/B003","relation_type":"near_synonym","shared_zone":"Binek kullanmadan ayakla gitme alanında örtüşürler."},{"boundary_match":"partial","distinction":"Bu kol yürüme şartını taşır; komşu kol yolcu veya yol ehli olmayı daha genel biçimde verir.","focus_only":"Yaya olarak yürüyen yolcuları belirtir.","gloss":"yaya yolcular ile yolcular","neighbor_only":"Yol ehli, yolcular ve gelip gidenler daha geniştir; yaya olma şartı gerekmez.","neighbor_ref":"root_000672/B002","relation_type":"near_synonym","shared_zone":"Yolda bulunan veya yolculuk eden kişiler alanını paylaşırlar."},{"boundary_match":"thematic_only","distinction":"Bu kol kişilere aittir; komşu kol yolun niteliğine aittir.","focus_only":"Yolda yürüyen kişileri adlandırır.","gloss":"yaya yolcular ile işlek yol","neighbor_only":"Üzerinden geçilen işlek yolu adlandırır.","neighbor_ref":"root_001046/B011","relation_type":"thematic","shared_zone":"Yolculuk ve yürüyüş sahnesini paylaşırlar."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı tanıklık, bu topluluk adını binek kullanmadan yürüyen yolcularla sınırlar."}],"source_summary":"Kanıt, anlamı yolculuk sırasında yürüyerek giden kişiler için kalıplı bir adlandırma olarak sınırlar."},"support_links":[]},{"boundary":"Bu dal yalnızca fiziksel dikme, dik durma ve yükselme alanındadır; tapınma taşı, pay, yorgunluk ve öteki dalların özel anlamlarını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B001","candidate_links":[{"candidate_id":"cand_19ec15bb49d40f156be0","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاصِبَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:n~aASibap|ROOT:nSb|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:2:1","qac_word_ref":"88:3:2","surface_ar":"نَّاصِبَةٌ"}],"gloss":"dikme, dik durma ve yükselme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi dik, çıkıntılı veya belirgin duracak biçimde yerleştirme ya da yükseltme."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir insanın, hayvanın, boynuzun veya göğsün dik ve yükselmiş durumda bulunması."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Toz gibi dağınık bir maddenin havaya yükselerek belirginleşmesi."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Perdeyi kaldırma, av için tuzak kurma veya kazanı taşıyacak demir desteği yerleştirme gibi nesneye bağlı uygulamalar."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel bir nesnenin dik konuma getirilmesini veya bir varlığın dik ve yükselmiş durumda bulunmasını birlikte anlatır.","boundary_detail":"Bu dal yalnızca fiziksel dikme, dik durma ve yükselme alanındadır; tapınma taşı, pay, yorgunluk ve öteki dalların özel anlamlarını içermez.","branch_image_ar":"إقامة الشيء منتصبا بارزا","concept_gloss":"dikme, dik durma ve yükselme","contextual_glosses":[{"applicability":"Mızrak, taş, direk, yapı veya benzeri bir nesne dik konuma getirildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesneyi dik ve belirgin konuma getiren fiziksel işlemi tam olarak korur."},"facet_ids":["F001"],"text":"dikmek","usage_role":"contextual"},{"applicability":"Bir insanın, hayvanın ya da beden bölümünün yükselmiş ve dik durumda bulunmasını anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlı veya beden bölümü için dik ve yükselmiş durumu eksiksiz korur."},"facet_ids":["F002"],"text":"dik durmak","usage_role":"contextual"},{"applicability":"Tozun yerden kalkıp havada belirginleştiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tozun yukarı doğru hareket edip görünür hâle gelmesini korur."},"facet_ids":["F003"],"text":"havaya yükselmek","usage_role":"contextual"}],"definition":"Bir şeyi dik, çıkıntılı veya belirgin duracak biçimde yerleştirmek ya da yükseltmek; ayrıca bir varlığın veya bölümünün bu biçimde dik durmasıdır. Tozun yükselmesi ve belirli nesnelerin kurulması bu uzamsal çekirdeğin bağlama bağlı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi dik, çıkıntılı veya belirgin duracak biçimde yerleştirme ya da yükseltme."},{"facet_id":"F002","role":"core","statement":"Bir insanın, hayvanın, boynuzun veya göğsün dik ve yükselmiş durumda bulunması."},{"facet_id":"F003","role":"extension","statement":"Toz gibi dağınık bir maddenin havaya yükselerek belirginleşmesi."},{"facet_id":"F004","role":"associated_use","statement":"Perdeyi kaldırma, av için tuzak kurma veya kazanı taşıyacak demir desteği yerleştirme gibi nesneye bağlı uygulamalar."}],"identity_rationale":"Dalın kimliği, bir şeyi dik ve belirgin duracak biçimde yerleştirme veya yükseltme çekirdeğini doğru yansıtır. Boynuz, göğüs ve baş gibi bölümlerin dik durması ile tozun yükselmesi aynı uzamsal görünümün geçişsiz gerçekleşmeleridir; perde kaldırma ve tuzak kurma ise belirli nesnelerle sınırlı kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi dikmek veya dik konuma kaldırmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"boynuzları dik olan"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"boynuzu dik veya göğsü yüksek dişi hayvan"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"havaya yükselmiş toz"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"perdeyi kaldırmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kuş avlamak için tuzak kurmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kazanın üzerine konduğu demir destek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dikili direk veya sütun"}],"lexicalization_note":"Tanım, yalın dikme ve dik durma çekirdeğini özel nesnelerle kurulan perde kaldırma, tuzak kurma ve kazan desteği gibi kullanımlardan açıkça ayırır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; çoğu yalnızca diklik senaryosunu paylaşan nesne, özel kullanım veya diğer kök anlamıdır. Okur açısından en yakın sınır karışıklığını dikilme ve sabit kalma adayı verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın merkezi yerleştirme ve yükseltmedir; komşu dalın merkezi ise dik duruşla birlikte sabitlik ve bir yere bağlı kalmadır.","focus_only":"Odak dal, bir nesneyi dik konuma getiren geçişli işlemi ve toz gibi şeylerin yükselmesini de kapsar.","gloss":"dikilme ve sabit kalma","neighbor_only":"Komşu dal, yerde veya bir şey üzerinde sabit kalma, bağlanma ve sıkıca yapışma anlamlarını da taşır.","neighbor_ref":"root_000232/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir varlığın dik veya yükselmiş durumda bulunmasını anlatabilir."}],"source_phrase_ar":"أصل صحيح يدل على إقامة شيء وإهداف في استواء (maqayis)؛ النصب رفعك شيئا تنصبه قائما منتصبا (ayn;tahdhib)؛ نصب الشيء وضعه وضعا ناتئا كنصب الرمح والبناء والحجر (mufradat)؛ نصبت الشئ إذا أقمته (sihah)؛ كل شيء رفعته فقد نصبته (jamhara)؛ تيس أنصب وعنزة نصباء وناقة نصباء وغبار منتصب (maqayis;ayn;sihah;tahdhib;mufradat)؛ نصبت للقطاة شركا ونصبت للقدر نصبا (tahdhib)؛ نصب الستر رفعه (mufradat)","source_summary":"Anlamın ortak çekirdeği, bir şeyi dik ve görünür konuma getirme ile bu konumda bulunmadır. Nesne örnekleri mızrak, yapı, taş, perde ve tuzağı; durum örnekleri ise dik boynuz, yükselmiş göğüs ve havaya kalkmış tozu kapsar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه نصب الشيء وإقامته ورفعه قائما، كنصب الرمح والبناء والحجر والستر والشرك، وقيام الشخص أو الحيوان منتصب الرأس أو القرن أو الصدر، وارتفاع الغبار ونحوه","what_is_not_ar":"لا يختص بالعبادة ولا بالحظ ولا بالتعب إلا إذا صرحت العبارة بذلك"},"support_links":["sup_8bfde22d07df29c05989"]},{"boundary":"Sıradan sınır taşı, kuyu çevresi taşı veya başka bir dikili nesne bu dala ancak tapınma ya da adak kesme işlevi varsa girer.","branch_kind":"bare","branch_ref":"root_001507/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاصِبَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:n~aASibap|ROOT:nSb|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:2:1","qac_word_ref":"88:3:2","surface_ar":"نَّاصِبَةٌ"}],"gloss":"tapınma veya adak kesme taşı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tapınılmak veya çevresinde dinsel tören yapılmak üzere dikilmiş taş."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üzerinde adak hayvanı kesilen veya kan dökülen dikili taş."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dinsel amaçla dikilmiş, tapınılan ya da üzerinde adak hayvanı kesilen taş için kullanılır.","boundary_detail":"Sıradan sınır taşı, kuyu çevresi taşı veya başka bir dikili nesne bu dala ancak tapınma ya da adak kesme işlevi varsa girer.","branch_image_ar":"حجر منصوب للعبادة والذبح","concept_gloss":"tapınma veya adak kesme taşı","contextual_glosses":[{"applicability":"Taşın doğrudan kutsal nesne sayılıp kendisine tapınıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikili taşın doğrudan tapınma nesnesi olmasını tam olarak korur."},"facet_ids":["F001"],"text":"tapınılan dikili taş","usage_role":"contextual"},{"applicability":"Hayvanın taş üzerinde kesildiği veya kanının taş üzerine döküldüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşın kesim ve kan dökme törenindeki özel işlevini korur."},"facet_ids":["F002"],"text":"adak kesme taşı","usage_role":"contextual"}],"definition":"Tapınmak, çevresinde dönmek, yakınlık sunmak veya üzerinde adak kesip kan dökmek için dikilmiş taş ya da bu tür taşlardan oluşan kutsal nesnedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tapınılmak veya çevresinde dinsel tören yapılmak üzere dikilmiş taş."},{"facet_id":"F002","role":"core","statement":"Üzerinde adak hayvanı kesilen veya kan dökülen dikili taş."}],"identity_rationale":"Dal, dikilmiş taşın tapınma, çevresinde dönme, adak kesme veya kan dökme amacıyla kullanılan kutsal nesne oluşunu doğru biçimde birleştirir. Taşın yalnızca dikili olması yeterli değildir; dinsel yönelim ya da kesim işlevi anlamın ayırt edici koşuludur.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"tapınılan veya üzerinde adak kesilen dikili taş"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"tapınılan ya da adak kesilen dikili taşlar"}],"lexicalization_note":"Tanım yalın taş adını dinsel işleviyle verir ve başka dallardaki sıradan dikili taş anlamlarını bu çekirdeğe katmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; kesme, adak, çevresinde dönme ve belirli put adları senaryonun ayrı parçalarıdır. En yararlı karşılaştırma, dikili tören taşı ile genel tapınma nesnesi arasındaki sınırdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dikili taş ve onun kesim törenindeki kullanımıyla sınırlıdır; komşu dal ise tapınılan nesnenin biçimini veya tören işlevini böyle sınırlamaz.","focus_only":"Odak dal, taşın dikili olmasını ve üzerinde kesim yapılıp kan dökülmesi işlevini özellikle içerir.","gloss":"tapınma nesnesi","neighbor_only":"Komşu dal, taşla sınırlı olmayan tapınma nesnelerini ve putları daha genel biçimde kapsar.","neighbor_ref":"root_001624/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da insanların tapındığı cansız ve kutsallaştırılmış bir nesneyi kapsayabilir."}],"source_phrase_ar":"النصب حجر كان ينصب فيعبد وتصب عليه دماء الذبائح للأصنام (maqayis)؛ حجر كان ينصب فيعبد وتصب عليه دماء الذبائح وجمعه أنصاب (ayn)؛ حجارة كانت تنصب في الجاهلية ويطاف بها ويتقرب عندها (jamhara)؛ ما نصب فعبد من دون الله والجمع الأنصاب (sihah)؛ النصب الآلهة التي كانت تعبد من أحجار (tahdhib)؛ حجارة تعبدها وتذبح عليها (mufradat)","source_summary":"Ortak anlatım, taşın dikilmiş olmasını tapınma ve kesim törenleriyle birlikte verir. Taş hem tapınılan bir nesne hem de adak hayvanının kesildiği ve kanının döküldüğü tören odağı olabilir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه النصب والأنصاب: حجارة منصوبة كانت تعبد أو يذبح عليها أو تصب عليها دماء الذبائح","what_is_not_ar":"لا يدخل مطلق العلامة أو حجارة الحوض إذا لم تكن عبادة أو ذبحا"},"support_links":[]},{"boundary":"Ayırt edici özellik, taşın işaret, sınır veya su yapısının kenar elemanı olmasıdır; dinsel kullanım ve pay anlamı dışarıda kalır.","branch_kind":"bare","branch_ref":"root_001507/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاصِبَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:n~aASibap|ROOT:nSb|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:2:1","qac_word_ref":"88:3:2","surface_ar":"نَّاصِبَةٌ"}],"gloss":"sınır işareti veya kuyu-havuz taşı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun yerini veya bir bölgenin sınırını bildirmek üzere dikilmiş işaret taşı."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuyu ya da havuz ağzının çevresine kenar ve destek oluşturacak biçimde yerleştirilen taş."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çevresi taşlarla kurulmuş havuzun kendisi."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir yeri belirleyen dikili işaretlerle kuyu ya da havuz çevresine yerleştirilen taşları kapsar.","boundary_detail":"Ayırt edici özellik, taşın işaret, sınır veya su yapısının kenar elemanı olmasıdır; dinsel kullanım ve pay anlamı dışarıda kalır.","branch_image_ar":"علامة أو حجارة منصوبة للحد أو الحوض","concept_gloss":"sınır işareti veya kuyu-havuz taşı","contextual_glosses":[{"applicability":"Bir topluluğun yerini veya kutsal sayılan bir bölgenin sınırını belirtme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikili taşın yer veya sınır bildiren işaret işlevini korur."},"facet_ids":["F001"],"text":"dikili sınır taşı","usage_role":"contextual"},{"applicability":"Kuyu veya havuz ağzının çevresine yerleştirilen taşlardan söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşın su yapısının çevresini ve kenarını oluşturma işlevini korur."},"facet_ids":["F002"],"text":"kuyu ya da havuz kenarı taşı","usage_role":"contextual"}],"definition":"Bir topluluğu veya sınırı göstermek için dikilen işaret ya da kuyu ve havuz kenarına destek veya çevre oluşturacak biçimde yerleştirilen taştır. Taşlardan kurulmuş havuzun kendisi de bu düzenlemeden doğan adlaşmış bir anlamdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun yerini veya bir bölgenin sınırını bildirmek üzere dikilmiş işaret taşı."},{"facet_id":"F002","role":"specialization","statement":"Kuyu ya da havuz ağzının çevresine kenar ve destek oluşturacak biçimde yerleştirilen taş."},{"facet_id":"F003","role":"extension","statement":"Çevresi taşlarla kurulmuş havuzun kendisi."}],"identity_rationale":"Dal, bir topluluğu ya da sınırı gösteren dikili işaret ile kuyu veya havuz kenarına yerleştirilen taşları kaynak ifadesine uygun biçimde kapsar. Taşlardan yapılmış havuz adı bu yerleştirme düzeninden doğan adlaşmış bir uzantıdır; tapınma işlevi bu dalın parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"dikili işaret veya havuz kenarı taşı"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kuyu ya da havuz ağzının çevresine dizilen taşlar"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"taşlardan kurulmuş havuz"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"topluluk veya sınır için dikilmiş işaret"}],"lexicalization_note":"Tanım, yalın adların işaret ve su yapısı anlamlarını kapsar; başka bir yapıya özgü deyimsel anlam eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sınır, kıyı ve uç anlamları işaret edilen çizgiye, su yapısı adayları ise yapının kenarına odaklanır. En yakın karışıklık, dikili kenar taşları ile kenarın genel adı arasındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kenarı oluşturan dikili taşlara dayanır; komşu dal ise kenarın kendisini malzemesinden ve kurulma biçiminden bağımsız olarak belirtir.","focus_only":"Odak dal, kuyu ve havuz çevresindeki belirli taşları ayrıca bağımsız sınır ve topluluk işaretlerini kapsar.","gloss":"kuyu veya havuz kenarı","neighbor_only":"Komşu dal, taş olma veya dikilme koşulu aramadan kuyu ve havuzun yanlarını genel olarak adlandırır.","neighbor_ref":"root_001370/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da kuyu ve havuz ağzının çevresindeki kenar yapısını gösterebilir."}],"source_phrase_ar":"النصائب حجارة تنصب حوالي شفير البئر فتجعل عضائد (maqayis)؛ النصيب الحوض ينصب من الحجارة (maqayis)؛ النصب العلم؛ النصيبة علامة تنصب للقوم؛ نصائب الحوض (ayn)؛ أنصاب الحرم حجارة تنصب لتعرف حدوده بها (jamhara)؛ النصيبة حجارة تنصب حول الحوض؛ النصيب الحوض (sihah)؛ النصائب ما نصب حول الحوض من الأحجار؛ النصب جماعة النصيبة وهي علامة تنصب للقوم (tahdhib)؛ النصيب الحجارة تنصب على الشيء وجمعه نصائب ونصب (mufradat)","source_summary":"Ortak anlam, bir yeri belli eden veya bir su yapısının kenarını oluşturan dikili taştır. Kullanım, topluluk işaretinden bölge sınırına, kuyu ve havuz çevresindeki taşlara ve bu taşlarla yapılmış havuz adına uzanır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه العلامات المنصوبة للقوم أو حدود الحرم، ونصائب الحوض وحجارته المنصوبة على شفيره، والحوض المبني من الحجارة","what_is_not_ar":"لا يدخل الحجر المعبود أو المذبوح عليه، ولا نصيب الحظ"},"support_links":[]},{"boundary":"Dik durma ile kurulan açıklama tarihsel bir anlamlandırmadır; fiziksel diklik bu dalın güncel kavramsal koşulu değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B004","candidate_links":[{"candidate_id":"cand_dade14e1aaeecd43ee99","lane":"macro"},{"candidate_id":"cand_1a4c72f4247fbd42755c","lane":"macro"},{"candidate_id":"cand_4d35782418e948ab7ab5","lane":"macro"},{"candidate_id":"cand_8ecacbaebfbed32f1fe8","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاصِبَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:n~aASibap|ROOT:nSb|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:2:1","qac_word_ref":"88:3:2","surface_ar":"نَّاصِبَةٌ"}],"gloss":"yorgunluk ve yıpratıcı sıkıntı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedensel ya da ruhsal yükün doğurduğu yorgunluk, bitkinlik ve tükenmişlik."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hastalık, kaygı, üzüntü, kötülük veya bela nedeniyle yaşanan yıpratıcı sıkıntı."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir olayın, hastalığın veya düşüncenin kişiyi yorup huzursuz etmesi."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel bitkinliği ve hastalık, kaygı ya da belanın insan üzerinde bıraktığı yorucu etkiyi kapsar.","boundary_detail":"Dik durma ile kurulan açıklama tarihsel bir anlamlandırmadır; fiziksel diklik bu dalın güncel kavramsal koşulu değildir.","branch_image_ar":"تعب وعناء وبلاء ينهك الإنسان","concept_gloss":"yorgunluk ve yıpratıcı sıkıntı","contextual_glosses":[{"applicability":"İnsan bedeninin emek, yürüyüş veya hastalık yüzünden gücünü yitirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel gücün azalmasıyla ortaya çıkan yoğun yorgunluğu korur."},"facet_ids":["F001"],"text":"bitkinlik","usage_role":"contextual"},{"applicability":"Bir olayın, kaygının veya hastalığın kişide yorgunluk ve tedirginlik oluşturduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dış etkenin kişide yorgunluk ve huzursuzluk oluşturmasını korur."},"facet_ids":["F003"],"text":"yorup huzursuz etmek","usage_role":"contextual"}],"definition":"Emek, hastalık, kaygı, üzüntü veya başka bir sıkıntının insanı yıpratmasıyla oluşan yorgunluk ve bitkinliktir. Aynı anlam alanı, bir etkenin kişiyi yorup huzursuz etmesini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedensel ya da ruhsal yükün doğurduğu yorgunluk, bitkinlik ve tükenmişlik."},{"facet_id":"F002","role":"extension","statement":"Hastalık, kaygı, üzüntü, kötülük veya bela nedeniyle yaşanan yıpratıcı sıkıntı."},{"facet_id":"F003","role":"associated_use","statement":"Bir olayın, hastalığın veya düşüncenin kişiyi yorup huzursuz etmesi."}],"identity_rationale":"Dal, bedensel bitkinlik ve yorulmayı, insanı yıpratan emek, hastalık, kaygı, üzüntü ve belayı ortak bir etkilenme ekseninde doğru toplar. Bir şeyin kişiyi yormasını bildiren ettirgen kullanım da aynı etkinin katılımcı yönünü değiştirir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yorgunluk, bitkinlik, zahmet ve sıkıntı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"hastalığın verdiği bitkinlik"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"beni yordu ve huzursuz etti"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yorucu veya yorgunluk içindeki"}],"lexicalization_note":"Tanım yalın yorgunluk anlamını korur; hastalık, kaygı ve bir şeyin kişiyi yorması gibi yapıya bağlı kullanımları ayrı yüzler olarak gösterir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bazıları yalnızca bedensel bitkinliği, bazıları zorluğu, bazıları da başkasını yorma eylemini öne çıkarır. En geniş gerçek örtüşme yorgunluk ve güçsüzlük dalındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal etkileyen hastalık ve ruhsal sıkıntıya kadar uzanır; komşu dal ise güçsüzlük ile süregelen emek ve meşakkat boyutunu daha belirgin taşır.","focus_only":"Odak dal, yorgunluğun yanında hastalık, kaygı, üzüntü ve belanın doğurduğu yıpratıcı etkiyi özellikle kapsar.","gloss":"yorgunluk ve güçsüzlük","neighbor_only":"Komşu dal, yorgunlukla birlikte güçsüzlük durumunu ve uzun uğraşın getirdiği genel meşakkati daha açık biçimde kapsar.","neighbor_ref":"root_001360/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da yorgunluk, bitkinlik ve bir başkasını yorma anlamlarında geniş ölçüde örtüşür."}],"source_phrase_ar":"النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي (maqayis)؛ النصب الإعياء والتعب؛ النصب الشر والبلاء؛ نصب الداء (ayn)؛ تغير الحال من مرض أو تعب؛ الحزن إذا أثر فيه؛ المنصبة كد وتعب (jamhara)؛ نصب الرجل تعبا؛ النصب الشر والبلاء (sihah)؛ النصب الإعياء من العناء؛ نصب له الهم وأنصبه؛ نصب الداء (tahdhib)؛ النصب التعب؛ أنصبني كذا أي أتعبني وأزعجني (mufradat)","source_summary":"Ortak çekirdek yorgunluk, bitkinlik ve zahmettir. Anlam bedensel emekten hastalık ve ruhsal sıkıntının etkisine uzanır; geçişli kullanımda ise bu durumu doğuran olay veya hastalık özne olur.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه النصب بمعنى الإعياء والتعب والعناء والكد، وما ينشأ من مرض أو هم أو حزن أو بلاء، وأنصبني الشيء إذا أتعبني","what_is_not_ar":"لا يدخل القيام المنتصب الحسي إلا من جهة تفسير التعب بالملازمة حتى الإعياء"},"support_links":["sup_15967cee13181a9d7512","sup_173417c5c70549c3170f","sup_7c7aa593f7a7ba764f63","sup_b54537c25533fd9ee37d"]},{"boundary":"Anlam bir bütünden ayrılan belirli payla sınırlıdır; borç, hak, ölçü eşiği veya bölüştürme işleminin kendisi zorunlu değildir.","branch_kind":"bare","branch_ref":"root_001507/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاصِبَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:n~aASibap|ROOT:nSb|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:2:1","qac_word_ref":"88:3:2","surface_ar":"نَّاصِبَةٌ"}],"gloss":"belirlenmiş pay","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünden belirli bir kişiye ayrılan veya ona düşen pay."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bütünden kişiye ayrılmış veya ona düşmüş belirli bölümü en kısa biçimde karşılar.","boundary_detail":"Anlam bir bütünden ayrılan belirli payla sınırlıdır; borç, hak, ölçü eşiği veya bölüştürme işleminin kendisi zorunlu değildir.","branch_image_ar":"حظ معين مرفوع لصاحبه","concept_gloss":"belirlenmiş pay","contextual_glosses":[{"applicability":"Bağlam, bir bütünden kime ne kadar düştüğünü zaten belirgin kılıyorsa doğal kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir bütünden kişiye düşen veya ayrılan bölüm anlamını korur."},"facet_ids":["F001"],"text":"pay","usage_role":"general"}],"definition":"Bir şeyden bir kişi için ayrılan, ona düşen veya onun adına belirlenen paydır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünden belirli bir kişiye ayrılan veya ona düşen pay."}],"identity_rationale":"Dal, bir bütünden bir kişiye düşen veya onun için belirlenen pay anlamını doğru verir. Payın belirlenmiş olması çekirdektir; dikili taş, taş havuz, köken ya da ölçü eşiği anlamları aynı ses biçimini paylaşsa da bu dala girmez.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"pay veya bir şeyden ayrılan belirli bölüm"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"pay"}],"lexicalization_note":"Tanım yalın pay anlamını verir ve belirli hukuk, miras, ceza ya da ölçü kalıplarını genel anlama eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hak, borç, ceza payı ve hesap terimleri daha dar bağlamlara bağlıdır. En yakın sınır, belirlenmiş pay ile paylaştırma işlemini de kapsayan komşu anlam arasındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bölüştürmenin sonucundaki paydır; komşu dal hem bu sonucu hem de paylara ayırma işlemini içerir.","focus_only":"Odak dal, yalnızca kişiye düşen veya onun için belirlenen payı adlandırır.","gloss":"pay ve paylaştırma","neighbor_only":"Komşu dal, payın yanı sıra şeyi kişiler arasında bölme, denkleştirme ve paylaştırma işlemini de kapsar.","neighbor_ref":"root_001224/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir bütünden kişinin aldığı belirli bölümü pay olarak adlandırır."}],"source_phrase_ar":"النصيب الحظ من الشيء (maqayis;sihah)؛ النصب النصيب لغة (ayn;tahdhib)؛ النصيب معروف والجمع أنصباء وأنصبة (jamhara)؛ النصيب الحظ المنصوب أي المعين (mufradat)","source_summary":"Ortak anlatım, bir şeyden kişiye düşen belirli payı gösterir. Çoğul biçimler bu payların birden çok kişiye veya bölüme ait olabileceğini belirtir, fakat çekirdeği değiştirmez.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه النصيب بمعنى الحظ أو القسم المعين من الشيء، وما سمي منصوبا أو مرفوعا لصاحبه","what_is_not_ar":"لا يدخل الحجارة أو الحوض المسمى نصيبا، ولا النصاب بمعنى الأصل أو القدر"},"support_links":[]},{"boundary":"Genel bir pay veya rastgele miktar anlamı çıkarılamaz; her özel gerçekleşme kanıtlanan nesne ve söz kalıbıyla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاصِبَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:n~aASibap|ROOT:nSb|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:2:1","qac_word_ref":"88:3:2","surface_ar":"نَّاصِبَةٌ"}],"gloss":"temel veya sabit başvuru noktası","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin dayandığı temel, köken, dönüş noktası veya sabit başvuru ölçüsü."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bıçağın elde tutulan sapı veya arka bölümü."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Malın belirli bir mali yükümlülüğü doğurduğu sabit alt miktar."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kişinin geldiği köken, yetiştiği soy ve bu kökene dayanan saygınlık."}},{"facet_id":"F005","role":"specialization","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Güneşin gün sonunda döner gibi görünüp battığı yer."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın söz kalıplarına göre köken, dayanak, dönüş noktası veya belirlenmiş eşik olarak gerçekleşen ortak çekirdeğini verir.","boundary_detail":"Genel bir pay veya rastgele miktar anlamı çıkarılamaz; her özel gerçekleşme kanıtlanan nesne ve söz kalıbıyla sınırlıdır.","branch_image_ar":"نصاب الشيء: أصله ومقداره الثابت","concept_gloss":"temel veya sabit başvuru noktası","contextual_glosses":[{"applicability":"Bıçağın elde tutulan arka bölümü veya ona sonradan takılan sap anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bıçağın elde tutulan sap veya arka bölümünü eksiksiz karşılar."},"facet_ids":["F002"],"text":"bıçak sapı","usage_role":"contextual"},{"applicability":"Mal miktarının belirli bir mali yükümlülüğü doğurduğu alt sınırdan söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sabit mal miktarının yükümlülüğü başlatan alt eşik oluşunu korur."},"facet_ids":["F003"],"text":"yükümlülük eşiği","usage_role":"explanatory"},{"applicability":"Kişinin geldiği aile çizgisi, kökeni ve buna bağlı saygınlığı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin ailesel kökenini ve geldiği soy çizgisini korur."},"facet_ids":["F004"],"text":"soy kökeni","usage_role":"contextual"},{"applicability":"Güneşin ufukta kaybolduğu yön veya yer bir dönüş noktası gibi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güneşin gün sonunda ufukta kaybolduğu yeri tam olarak korur."},"facet_ids":["F005"],"text":"güneşin battığı yer","usage_role":"contextual"}],"definition":"Bir şeyin dayandığı temel, döndüğü başvuru noktası veya sabitlenmiş ölçüsüdür. Bu çekirdek, yalnızca belirli kullanımlarda bıçağın sapını, mali yükümlülük doğuran alt eşiği, kişinin köken ve soyunu ya da güneşin batış yerini gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin dayandığı temel, köken, dönüş noktası veya sabit başvuru ölçüsü."},{"facet_id":"F002","role":"specialization","statement":"Bıçağın elde tutulan sapı veya arka bölümü."},{"facet_id":"F003","role":"specialization","statement":"Malın belirli bir mali yükümlülüğü doğurduğu sabit alt miktar."},{"facet_id":"F004","role":"specialization","statement":"Bir kişinin geldiği köken, yetiştiği soy ve bu kökene dayanan saygınlık."},{"facet_id":"F005","role":"specialization","statement":"Güneşin gün sonunda döner gibi görünüp battığı yer."}],"identity_rationale":"Dal, temel, dönüş noktası ve sabit ölçü düşüncesini taşıyan kullanımları doğru toplar; ancak bunlar tek bir yalın ve her bağlama uygulanabilir anlam değildir. Bıçak sapı, mali yükümlülük eşiği, soy kökeni ve güneşin batış yeri yalnızca kendi söz kalıpları içinde korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir şeyin temeli ve dönülen başvuru noktası"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bıçağın sapı veya arka bölümü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"mal için mali yükümlülük doğuran alt miktar"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"köken, soy ve aileden gelen saygınlık"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"güneşin battığı ve döndüğü yer"}],"lexicalization_note":"Tanım ortak temel ve sabit başvuru noktasını verir; bıçak, mal, soy ve güneşle kurulan anlamları ayrı ve kalıba bağlı uzmanlaşmalar olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hesap, ağırlık ve ölçme dalları yalnızca sabit miktar yüzünü, köken dalları ise yalnızca temel yüzünü paylaşır. Bu nedenle yayımlanan ilişki eş anlamlılık değil aynı alan karşılaştırmasıdır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortak köken alanına rağmen odak dal farklı nesnelerde sabit başvuru ve eşik anlamları taşıyan bir kullanım ailesidir; komşu dalın nesne kapsamı ayrıdır.","focus_only":"Odak dal, kökenin yanı sıra bıçak sapı, mali eşik ve güneşin batış yeri gibi kalıplaşmış başvuru noktalarını kapsar.","gloss":"köken ve çıkış yeri","neighbor_only":"Komşu dal, kişinin soy kökenini ve hörgücün kök bölümünü kendi sözlüksel alanında adlandırır.","neighbor_ref":"root_000340/B005","relation_type":"same_field","shared_zone":"Her iki dal da bir varlığın geldiği temel veya köken noktasını gösterebilir."}],"source_phrase_ar":"نصاب الشيء أصله؛ نصاب السكين؛ بلغ المال النصاب الذي تجب فيه الزكاة (maqayis)؛ نصاب كل شيء أصله ومرجعه؛ رجع إلى مركبه ومنصبه أي أصل منبته وحسبه؛ نصاب الشمس مغيبها (ayn)؛ نصاب السكين؛ نصاب صدق أي حسب ثابت (jamhara)؛ المنصب الأصل وكذلك النصاب؛ النصاب من المال القدر الذي تجب فيه الزكاة؛ نصاب السكين مقبضه (sihah)؛ نصاب كل شيء أصله ومرجعه؛ نصاب الشمس مغيبها؛ أنصبت السكين جعلت لها نصابا (tahdhib)؛ نصاب السكين ونصبه؛ نصاب الشيء أصله؛ رجع فلان إلى منصبه أي أصله (mufradat)","source_summary":"Ortak malzeme temel ve geri dönülen başvuru noktası çevresinde toplanır, fakat kullanımlar güçlü biçimde sözlüksel sınırlıdır. Bıçak sapı, mali eşik, soy kökeni ve güneşin batış yeri aynı genel sözcük ailesinin ayrı gerçekleşmeleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه نصاب الشيء أي أصله ومرجعه، ونصاب السكين ومقبضها أو عجزها، ونصاب المال الذي تجب فيه الزكاة، ونصاب الشمس مغيبها، والمنصب بمعنى الأصل والحسب","what_is_not_ar":"لا يدخل النصيب بمعنى الحظ، ولا النصب بمعنى التعب أو الحجر المعبود"},"support_links":[]},{"boundary":"Bu anlam yalnızca belirtilen dil bilgisi terimi ve ona bağlı sözcük biçimleri için geçerlidir; fiziksel yükseltme veya şarkı söyleme anlamına genellenmez.","branch_kind":"collocation","branch_ref":"root_001507/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاصِبَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:n~aASibap|ROOT:nSb|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:2:1","qac_word_ref":"88:3:2","surface_ar":"نَّاصِبَةٌ"}],"gloss":"dil bilgisinde yükleme konumu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekimli sözcüklerde üst konumun karşısında bulunan yükleme konumu."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Değişmez sözcük biçimlerinde açık ünlülü yapıya denk sayılan terimsel kullanım."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca çekim ve değişmez biçim çözümlemesindeki özel dil bilgisi kategorisini adlandırır.","boundary_detail":"Bu anlam yalnızca belirtilen dil bilgisi terimi ve ona bağlı sözcük biçimleri için geçerlidir; fiziksel yükseltme veya şarkı söyleme anlamına genellenmez.","branch_image_ar":"نصب الكلمة في الإعراب","concept_gloss":"dil bilgisinde yükleme konumu","contextual_glosses":[{"applicability":"Bir sözcüğün cümle içindeki çekim konumu özel olarak belirtilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözcüğün yükleme konumuna yerleştirilmiş olmasını tam olarak korur."},"facet_ids":["F001"],"text":"yükleme konumundaki sözcük","usage_role":"explanatory"}],"definition":"Çekimli dil bilgisinde üst konumun karşıtı olan yükleme konumu; değişmez yapılarda ise açık ünlülü biçime denk sayılan dil bilgisel kategoridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekimli sözcüklerde üst konumun karşısında bulunan yükleme konumu."},{"facet_id":"F002","role":"source_variant","statement":"Değişmez sözcük biçimlerinde açık ünlülü yapıya denk sayılan terimsel kullanım."}],"identity_rationale":"Dal, çekimli dil bilgisinde üst konumun karşısında yer alan yükleme konumunu ve değişmez biçimlerde açık ünlülü yapıyla kurulan benzerliği doğru verir. Ağız içindeki ses yükselişine ilişkin açıklama kategori tanımının kendisi değil, sesletim temelli bir gerekçelendirmedir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"çekimde üst konumun karşıtı olan yükleme konumu"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yükleme konumuna getirilmiş sözcük"}],"lexicalization_note":"Tanım açıkça dil bilgisi yapısına bağlıdır ve bu terimsel kullanımdan yalın kök için genel bir anlam çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; diğerleri dil bilgisinin farklı bölümlerini veya genel anlatımı paylaşır, fakat aynı çekim ekseninde yer almaz. Doğrudan karşıtlık yalnızca üst konum dalıyla kuruludur.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bunlar aynı eksenin karşıt kutuplarıdır: odak dal yükleme yönündeki konumu, komşu dal ise üst konumu belirtir.","focus_only":"Odak dal, çekimde yükleme yönündeki alt konumu ve değişmez biçimde açık ünlülü yapıyı gösterir.","gloss":"karşıt çekim konumları","neighbor_only":"Komşu dal, aynı çekim düzenindeki karşıt üst konumu ve değişmez biçimde yuvarlak ünlülü yapıyı gösterir.","neighbor_ref":"root_000582/B012","relation_type":"polarity_pair","shared_zone":"İki dal aynı dil bilgisi sisteminde sözcüğün biçimsel çekim konumunu belirler."}],"source_phrase_ar":"في الفتح هو النصب كأن الكلمة تنتصب في الفم (maqayis)؛ النصب ضد الرفع في الإعراب؛ الكلمة المنصوبة يرفع صوتها إلى الغار الأعلى (ayn)؛ النصب في الإعراب كالفتح في البناء (sihah)؛ الكلمة المنصوبة يرفع صوتها إلى الغار الأعلى (tahdhib)؛ النصب في الإعراب معروف (mufradat)","source_summary":"Ortak çekirdek belirli bir dil bilgisi konumudur ve karşıt üst konumla tanımlanır. Bazı açıklamalar bunu değişmez yapılardaki açık ünlülü biçime veya sözcüğün ağızda daha yukarıdan seslendirilmesine benzetir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النصب النحوي ضد الرفع أو كالفتح في البناء، والكلمة المنصوبة والحرف المنصوب","what_is_not_ar":"لا يدخل رفع الشيء حسيا ولا رفع الصوت في الغناء إلا من جهة التشبيه الذي ذكرته المصادر"},"support_links":[]},{"boundary":"Kullanım kişiyle ve düşmanlık ya da savaş içeriğiyle sınırlıdır; genel karşı koyma, savunma veya fiziksel dikme tek başına bu dala girmez.","branch_kind":"non_bare","branch_ref":"root_001507/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاصِبَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:n~aASibap|ROOT:nSb|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:2:1","qac_word_ref":"88:3:2","surface_ar":"نَّاصِبَةٌ"}],"gloss":"birine savaş veya düşmanlıkla karşı çıkma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin karşısına savaş veya düşmanlıkla çıkıp ona hasım olmak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Düşmanlığı veya savaşı belirli bir kişiye yöneltilmiş bir tutum olarak kurmak."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli bir kişiye açıkça hasım olma, savaş açma veya düşmanlık yöneltme bağlamlarında kullanılır.","boundary_detail":"Kullanım kişiyle ve düşmanlık ya da savaş içeriğiyle sınırlıdır; genel karşı koyma, savunma veya fiziksel dikme tek başına bu dala girmez.","branch_image_ar":"مواجهة العداوة والحرب","concept_gloss":"birine savaş veya düşmanlıkla karşı çıkma","contextual_glosses":[{"applicability":"Bir kişinin başka bir kişiye açıkça düşmanlık besleyip bunu davranışa dönüştürdüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Düşmanlığın belirli bir kişiye yönelmesini ve açık hâle gelmesini korur."},"facet_ids":["F001"],"text":"ona düşman kesilmek","usage_role":"contextual"},{"applicability":"Hasmane yönelişin doğrudan savaş başlatma veya savaşla karşı karşıya gelme biçiminde gerçekleştiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Savaşın belirli bir kişiye yöneltilmesini açık biçimde korur."},"facet_ids":["F002"],"text":"ona savaş açmak","usage_role":"contextual"}],"definition":"Bir kişiye savaş, kötülük veya düşmanlıkla yönelmek; onun karşısına açıkça hasım olarak çıkmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin karşısına savaş veya düşmanlıkla çıkıp ona hasım olmak."},{"facet_id":"F002","role":"specialization","statement":"Düşmanlığı veya savaşı belirli bir kişiye yöneltilmiş bir tutum olarak kurmak."}],"identity_rationale":"Dal, belirli bir kişiye savaş, kötülük veya düşmanlıkla açıkça yönelme anlamını doğru verir. Anlam sıradan bir nesneyi dikmekten değil, karşı tarafa hasmane bir tutum veya savaş durumu kurmaktan oluşur.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"birine savaş veya düşmanlıkla karşı çıkmak"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"ona düşman olmak veya düşmanlık yöneltmek"}],"lexicalization_note":"Tanım yalnızca kişiyle kurulan düşmanlık ve savaş yapılarına bağlıdır; bu kullanımlardan yalın ve genel bir kök anlamı üretilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; savaş, savunma, mücadele ve uzun süreli husumet dalları aynı senaryonun farklı bölümleridir. En yakın sınır, genel hasmane yöneliş ile düşmanlığı ilk kez açık etme arasındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hasmane karşılaşmanın genel durumunu verir; komşu dal ise düşmanlığın ilk açık ilanı veya başlangıç anıyla sınırlıdır.","focus_only":"Odak dal, bir kişiye savaş veya düşmanlıkla yönelmeyi, bunun başlamış ya da sürmekte olmasını kapsar.","gloss":"açık düşmanlık başlatma","neighbor_only":"Komşu dal, düşmanlığın ilk kez açıkça ortaya konmasını ve karşı tarafa bildirilmesini özellikle şart koşar.","neighbor_ref":"root_001302/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da düşmanlığın belirli bir kişiye açıkça yöneltilmesini anlatır."}],"source_phrase_ar":"ناصبت فلانا الشر والحرب والعداوة (ayn;tahdhib)؛ نصبت لفلان نصبا إذا عاديته؛ ناصبته الحرب مناصبة (sihah)؛ ناصبه الحرب والعداوة ونصب له (mufradat)","source_summary":"Ortak anlatım, savaşın veya düşmanlığın belirli bir kişiye yöneltilmesini ve kişinin karşısına hasım olarak çıkılmasını gösterir. Fiil, hem karşılıklı savaşmayı hem de birine düşmanlık kurmayı anlatabilir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه ناصب فلانا الشر أو الحرب أو العداوة، ونصب له أو نصب لهم حربا، أي واجهه وعداه","what_is_not_ar":"لا يدخل مجرد نصب الشيء الحسي إلا إذا كان المنصوب هو الحرب أو العداوة"},"support_links":[]},{"boundary":"Dal belirli ezgi türüyle sınırlıdır; genel şarkı söyleme, güzel ses, çalgı sesi veya yalnızca yüksek sesle söyleme bu anlamı tek başına karşılamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B009","candidate_links":[{"candidate_id":"cand_2a685e998ac06d27dee0","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاصِبَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:n~aASibap|ROOT:nSb|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:2:1","qac_word_ref":"88:3:2","surface_ar":"نَّاصِبَةٌ"}],"gloss":"özel bir şarkı veya ezgi türü","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kendine özgü bir şarkı veya ezgi türü."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yolcuların söylediği, hayvan sürme çağrılı ezgisine benzeyen fakat ondan daha yumuşak olabilen ezgi."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tür adını sesi yükseltme düşüncesine bağlayan kesin olmayan açıklama."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel olarak kanıtlanan özel şarkı veya ezgi türünü belirtir; bazı kullanımlarda yolculukta söylenen, hayvan sürme çağrısına benzer görece yumuşak biçimi kapsar.","boundary_detail":"Dal belirli ezgi türüyle sınırlıdır; genel şarkı söyleme, güzel ses, çalgı sesi veya yalnızca yüksek sesle söyleme bu anlamı tek başına karşılamaz.","branch_image_ar":"غناء يرفع به الصوت","concept_gloss":"özel bir şarkı veya ezgi türü","contextual_glosses":[{"applicability":"Bağlam ezginin özel türünü ve yolculuk sırasında söylendiğini zaten gösteriyorsa kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özel şarkı türünün yolculuk bağlamındaki kullanımını korur."},"facet_ids":["F001","F002"],"text":"yolcu ezgisi","usage_role":"contextual"},{"applicability":"Bir yolcunun bu özel ezgi türünü seslendirmesi eylem olarak anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yolcunun belirli ezgi türünü söylemesi eylemini tam olarak korur."},"facet_ids":["F001","F002"],"text":"yolcu ezgisini söylemek","usage_role":"contextual"}],"definition":"Belirli bir şarkı veya ezgi türüdür. Bazı kaynaklarda yolcuların söylediği, hayvan sürerken kullanılan çağrılı ezgiye benzeyen ve ondan daha yumuşak olabilen bir tür olarak açıklanır. Adının sesi yükseltmeyle ilişkisi kesin anlam değil, olası bir türetme açıklamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kendine özgü bir şarkı veya ezgi türü."},{"facet_id":"F002","role":"specialization","statement":"Yolcuların söylediği, hayvan sürme çağrılı ezgisine benzeyen fakat ondan daha yumuşak olabilen ezgi."},{"facet_id":"F003","role":"source_variant","statement":"Tür adını sesi yükseltme düşüncesine bağlayan kesin olmayan açıklama."}],"identity_rationale":"Kaynak ifadesinin çekirdeği sesi yükseltmenin kendisi değil, belirli bir şarkı ve ezgi türüdür. Yolcuların söylediği ve hayvan sürme ezgisine benzediği, fakat daha yumuşak olabildiği belirtilir; ses yükseltme bağlantısı yalnızca olası bir adlandırma açıklamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"yolcuların söylediği özel ezgi türü"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"hayvan sürme çağrısına benzeyen yumuşak yolcu ezgisi"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"yolcu ezgisini söyledi"}],"lexicalization_note":"Tanım ezgi türünün yalın adını, onun yolcu şarkısı kalıbını ve bu ezgiyi söyleme fiilini ayırır; yüksek ses varsayımını çekirdeğe dönüştürmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çalgı, ses yineleme, yüksek ses ve biçimlenmiş ezgi adayları yalnızca müzik senaryosunu paylaşır. En yakın sınır özel yolcu ezgisi ile genel şarkı ve ezgili ses alanıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir yolcu ezgisi türüdür; komşu dal ise şarkı ve ezgili ses alanının genel adıdır.","focus_only":"Odak dal, yolcularla ve hayvan sürme çağrılı ezgisine benzer yumuşak söyleyişle sınırlı özel bir türdür.","gloss":"şarkı ve ezgili ses","neighbor_only":"Komşu dal, şarkıyı, güzel sesi, ezgili dinletiyi ve okumanın duygulu ya da ince söylenişini daha genel kapsar.","neighbor_ref":"root_001110/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da insan sesiyle ezgili ve dinlenebilir bir söyleyişi anlatır."}],"source_phrase_ar":"النصب جنس من الغناء ولعله مما ينصب أي يعلي به الصوت (maqayis)؛ غناء النصب ضرب من الألحان؛ غناء لهم يشبه الحداء إلا أنه أرق منه (sihah)؛ النصب ضرب من أغاني الأعراب؛ نصب الراكب إذا غنى النصب؛ غناء الركبان؛ حداء يشبه الغناء (tahdhib)؛ في الغناء ضرب منه (mufradat)","source_summary":"Ortak çekirdek belirli bir ezgi türüdür. Bu tür yolculuk ve hayvan sürme bağlamıyla ilişkilendirilir, benzer çağrılı ezgiden daha yumuşak sayılabilir ve adının sesi yükseltmekten geldiği yalnızca olasılık olarak açıklanır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه النصب ضربا من الغناء أو الألحان، وغناء الركبان أو الحداء المشبه بالغناء، والفعل نصب الراكب إذا غناه","what_is_not_ar":"لا يدخل النصب النحوي ولا رفع الشيء الحسي إلا من جهة رفع الصوت"},"support_links":["sup_411118ab1ab472386bde"]},{"boundary":"Anlam, yolculuğu sürdürme yapısına bağlıdır; yorgunluk sonucu, gece yolculuğu, hızlı geçiş veya kesintisiz ilerleme tek başına bu dal değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B010","candidate_links":[{"candidate_id":"cand_8ecacbaebfbed32f1fe8","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاصِبَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:n~aASibap|ROOT:nSb|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:2:1","qac_word_ref":"88:3:2","surface_ar":"نَّاصِبَةٌ"}],"gloss":"yolculuğu yumuşak sürdürme veya artırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun yolculuk hâlinde ilerlemesi ve yol alışını sürdürmesi."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluğun gün boyunca yumuşak bir yürüyüşle yol alması."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Topluluğun yol alışını yükseltmesi veya ilerleyişini artırması."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel söz yapısında hem gün boyu yumuşak ilerleme hem de yol alışını yükseltme çeşitlemesini kapsar.","boundary_detail":"Anlam, yolculuğu sürdürme yapısına bağlıdır; yorgunluk sonucu, gece yolculuğu, hızlı geçiş veya kesintisiz ilerleme tek başına bu dal değildir.","branch_image_ar":"سير اليوم سيرا لينا","concept_gloss":"yolculuğu yumuşak sürdürme veya artırma","contextual_glosses":[{"applicability":"Topluluğun gündüz boyunca hafif ve yumuşak bir yürüyüşle yol aldığı anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gün boyu süren yumuşak ilerleyiş çeşitlemesini eksiksiz korur."},"facet_ids":["F001","F002"],"text":"gün boyu yumuşak ilerlemek","usage_role":"contextual"},{"applicability":"Topluluğun ilerleyişini yükselttiği veya yolculuk çabasını artırdığı anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yol alışını yükseltme ve ilerleyişi artırma çeşitlemesini korur."},"facet_ids":["F001","F003"],"text":"yol alışını artırmak","usage_role":"contextual"}],"definition":"Bir topluluğun yolculuğu sürdürmesiyle ilgili özel kullanımdır. Bağlama göre gün boyunca yumuşak biçimde ilerlemeyi veya yol alışını yükseltip artırmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun yolculuk hâlinde ilerlemesi ve yol alışını sürdürmesi."},{"facet_id":"F002","role":"source_variant","statement":"Topluluğun gün boyunca yumuşak bir yürüyüşle yol alması."},{"facet_id":"F003","role":"source_variant","statement":"Topluluğun yol alışını yükseltmesi veya ilerleyişini artırması."}],"identity_rationale":"Dalın yolculukla ilgili kimliği doğrudur, ancak kaynak ifadesi tek biçimli bir hız niteliği vermez. Bir anlatım yol alışını yükseltip artırmayı, diğer anlatımlar ise gün boyunca yumuşak biçimde ilerlemeyi bildirir; iki çeşitleme aynı özel söz yapısı içinde ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"gün boyunca yumuşak biçimde ilerlediler"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"yol alışlarını yükseltip artırdılar"}],"lexicalization_note":"Tanım yalnızca topluluğun yol alması ve yolculuğu sürdürmesi yapılarında geçerlidir; gün boyu yumuşak ilerleme ile yol alışını artırma çeşitlemelerini birbirine karıştırmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kesintisiz, geceleyin, hızlı veya uzaklara yapılan yolculuklar farklı koşullar taşır. En yakın örtüşme yumuşak ilerleyiştedir, ancak odak dalın gün boyu sürme ve artırma çeşitlemeleri daha geniştir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli topluluk ve yolculuk yapısında gün boyu sürme ya da artırma seçeneklerini taşır; komşu dal yalnızca yumuşak hız niteliğine odaklanır.","focus_only":"Odak dal, topluluğun gün boyunca yol almasını ve ayrıca yol alışını artırma çeşitlemesini içerir.","gloss":"yumuşak yol alma","neighbor_only":"Komşu dal, gün boyu sürme veya ilerleyişi artırma koşulu olmadan yalnızca yumuşak yürüyüşü belirtir.","neighbor_ref":"root_000664/B013","relation_type":"near_synonym","shared_zone":"Her iki dal da yolculuğun yumuşak ve hafif bir ilerleyişle yapılmasını anlatabilir."}],"source_phrase_ar":"نصب القوم السير نصبا إذا رفعوه (jamhara)؛ نصب القوم ساروا يومهم وهو سير لين (sihah)؛ نصبوا نصبا وهو سير لين (tahdhib)","source_summary":"Ortak bağlam bir topluluğun yol almasıdır, fakat nitelik anlatımı ikiye ayrılır: gün boyunca yumuşak ilerleme ve yol alışını yükseltip artırma. Bu karşıt görünümler tek bir hız özelliğine indirgenmeden korunmalıdır.","sources":["JA","SI","TA"],"what_is_ar":"يدخل فيه نصب القوم أو نصب السير: ساروا يومهم أو رفعوا السير، وهو سير لين في بعض المصادر","what_is_not_ar":"لا يدخل التعب من السفر إلا إذا دل السياق على الإعياء لا على نوع السير"},"support_links":["sup_15967cee13181a9d7512"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000083/B001","candidate_links":[{"candidate_id":"cand_19ec15bb49d40f156be0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a099e2ae190659ab3f35","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Dispersing and spreading supplies the final distribution of the furnished field.","root":"ب ث ث","source_ref":"88:16","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000083","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8bfde22d07df29c05989"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000278/B001","candidate_links":[{"candidate_id":"cand_1a4c72f4247fbd42755c","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_06f1e37c3945d9dbfe88","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"An empty belly supplies the unresolved deficit that closes the failed recovery loop.","root":"ج و ع","source_ref":"88:7","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000278","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b54537c25533fd9ee37d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000358/B001","candidate_links":[{"candidate_id":"cand_1a4c72f4247fbd42755c","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_06f1e37c3945d9dbfe88","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Heating intensifies bodily demand and accelerates depletion.","root":"ح م ي","source_ref":"88:4","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000358","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b54537c25533fd9ee37d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000412/B001","candidate_links":[{"candidate_id":"cand_dade14e1aaeecd43ee99","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_92f36c8290d8cc2495fd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Lowering and submission give the face a defeated posture into which the focus predicates continue.","root":"خ ش ع","source_ref":"88:2","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000412","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7c7aa593f7a7ba764f63"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000569/B001","candidate_links":[{"candidate_id":"cand_4d35782418e948ab7ab5","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6dabc67db6cf885ba745","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Satisfaction supplies the successful relation between the second faces and their striving.","root":"ر ض و","source_ref":"88:9","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000569","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_173417c5c70549c3170f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000582/B001","candidate_links":[{"candidate_id":"cand_19ec15bb49d40f156be0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a099e2ae190659ab3f35","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Raising supplies the first visible completed operation.","root":"ر ف ع","source_ref":"88:13","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000582","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8bfde22d07df29c05989"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000697/B011","candidate_links":[{"candidate_id":"cand_19ec15bb49d40f156be0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a099e2ae190659ab3f35","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A place of settled reclining supplies the use-value produced by the installation sequence.","root":"س ر ر","source_ref":"88:13","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000697","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8bfde22d07df29c05989"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000722/B001","candidate_links":[{"candidate_id":"cand_1a4c72f4247fbd42755c","lane":"macro"},{"candidate_id":"cand_8ecacbaebfbed32f1fe8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_06f1e37c3945d9dbfe88","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Giving drink supplies intake, but its passive administration does not restore agency or strength.","root":"س ق ي","source_ref":"88:5","source_word_indices":["1"]},{"hft_ref":"hft_36c64bef73ebeceb563c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Literal giving of drink supplies the apparent watering station in the movement cycle.","root":"س ق ي","source_ref":"88:5","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000722","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_15967cee13181a9d7512","sup_b54537c25533fd9ee37d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000741/B007","candidate_links":[{"candidate_id":"cand_2a685e998ac06d27dee0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_731589e2c10c8ffe073e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Pleasurable hearing and song supply the positive acoustic category against which the focus chant can be tested.","root":"س م ع","source_ref":"88:11","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000741","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_411118ab1ab472386bde"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000744/B001","candidate_links":[{"candidate_id":"cand_1a4c72f4247fbd42755c","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_06f1e37c3945d9dbfe88","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Bodily fattening supplies the first explicitly negated sign of nourishment.","root":"س م ن","source_ref":"88:7","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000744","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b54537c25533fd9ee37d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000762/B001","candidate_links":[{"candidate_id":"cand_8ecacbaebfbed32f1fe8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_36c64bef73ebeceb563c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The split mapped image of driving and herding supplies coercive propulsion through that station.","root":"س ق ي","source_ref":"88:5","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000762","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_15967cee13181a9d7512"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000871/B001","candidate_links":[{"candidate_id":"cand_19ec15bb49d40f156be0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a099e2ae190659ab3f35","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Alignment on an even line supplies ordered arrangement.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000871","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8bfde22d07df29c05989"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000880/B003","candidate_links":[{"candidate_id":"cand_1a4c72f4247fbd42755c","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_06f1e37c3945d9dbfe88","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Encountering fire supplies the punishing environment in which exertion continues.","root":"ص ل ي","source_ref":"88:4","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000880","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b54537c25533fd9ee37d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000908/B005","candidate_links":[{"candidate_id":"cand_1a4c72f4247fbd42755c","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_06f1e37c3945d9dbfe88","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The named plant supplies the sole material input in the restrictive food clause.","root":"ض ر ع","source_ref":"88:6","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000908","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b54537c25533fd9ee37d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001088/B002","candidate_links":[{"candidate_id":"cand_dade14e1aaeecd43ee99","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_92f36c8290d8cc2495fd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"An encompassing cover supplies the event that surrounds and overwhelms the displayed subject.","root":"غ ش و","source_ref":"88:1","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001088","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7c7aa593f7a7ba764f63"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001110/B002","candidate_links":[{"candidate_id":"cand_1a4c72f4247fbd42755c","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_06f1e37c3945d9dbfe88","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Sufficiency supplies the second restorative function explicitly denied.","root":"غ ن ي","source_ref":"88:7","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001110","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b54537c25533fd9ee37d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001361/B003","candidate_links":[{"candidate_id":"cand_2a685e998ac06d27dee0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_731589e2c10c8ffe073e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Mixed noisy sound supplies the acoustic condition excluded from the contrasting garden.","root":"ل غ و","source_ref":"88:11","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001361","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_411118ab1ab472386bde"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001525/B001","candidate_links":[{"candidate_id":"cand_4d35782418e948ab7ab5","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6dabc67db6cf885ba745","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Good condition and blessing reverse the first panel's visible depletion.","root":"ن ع م","source_ref":"88:8","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001525","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_173417c5c70549c3170f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001630/B004","candidate_links":[{"candidate_id":"cand_dade14e1aaeecd43ee99","lane":"macro"},{"candidate_id":"cand_4d35782418e948ab7ab5","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_92f36c8290d8cc2495fd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The face standing for the self makes the bodily surface represent the whole person.","root":"و ج ه","source_ref":"88:2","source_word_indices":["1"]},{"hft_ref":"hft_6dabc67db6cf885ba745","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The face as self repeats the same display unit and permits a controlled comparison.","root":"و ج ه","source_ref":"88:8","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001630","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_173417c5c70549c3170f","sup_7c7aa593f7a7ba764f63"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001657/B001","candidate_links":[{"candidate_id":"cand_19ec15bb49d40f156be0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a099e2ae190659ab3f35","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Putting an object in a fixed place supplies deliberate placement.","root":"و ض ع","source_ref":"88:14","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001657","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8bfde22d07df29c05989"]}],"candidate_inventory":[{"anchor_refs":["88:12","88:3","88:6","88:9"],"branch_refs":["root_000240/B006","root_000709/B002","root_000934/B004","root_001046/B004"],"candidate_id":"cand_8e5fc53d5e94adf52da3","commentary_obligation":"review","focus_branch_refs":["root_001046/B004"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000240/B006","root_000709/B002","root_000934/B004"],"root_ids":[],"scope":"pericope","source_local_id":"C:Wage, Stipend, and Livelihood","source_type":"channel","support_ids":["sup_68fb5b0f30f61d3cfa4b","sup_9df5070203cf78f5cf6c","sup_a1e42e451d372a3afba0","sup_b0457721f1f3b8948cdf","sup_fd59a7fd37d79a981cdf"],"title":"Wage, Stipend, and Livelihood","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:1","88:2","88:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:3","branch_refs":["root_000412/B001","root_001046/B001","root_001088/B002","root_001507/B004","root_001630/B004"],"candidate_id":"cand_dade14e1aaeecd43ee99","commentary_obligation":"review","hft_ref":"hft_92f36c8290d8cc2495fd","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_faces_as_exposed_transcript","source_type":"hft","support_ids":["sup_7c7aa593f7a7ba764f63"],"title":"delta_faces_as_exposed_transcript","trust":"legacy_unbound"},{"anchor_refs":["88:3","88:4","88:5","88:6","88:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:3","branch_refs":["root_000278/B001","root_000358/B001","root_000722/B001","root_000744/B001","root_000880/B003","root_000908/B005","root_000934/B004","root_001046/B007","root_001110/B002","root_001507/B004"],"candidate_id":"cand_1a4c72f4247fbd42755c","commentary_obligation":"review","hft_ref":"hft_06f1e37c3945d9dbfe88","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_nonrecuperating_labor_circuit","source_type":"hft","support_ids":["sup_b54537c25533fd9ee37d"],"title":"delta_nonrecuperating_labor_circuit","trust":"legacy_unbound"},{"anchor_refs":["88:3","88:8","88:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:3","branch_refs":["root_000569/B001","root_000709/B002","root_001046/B001","root_001507/B004","root_001525/B001","root_001630/B004"],"candidate_id":"cand_4d35782418e948ab7ab5","commentary_obligation":"review","hft_ref":"hft_6dabc67db6cf885ba745","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_contrastive_work_outcomes","source_type":"hft","support_ids":["sup_173417c5c70549c3170f"],"title":"delta_contrastive_work_outcomes","trust":"legacy_unbound"},{"anchor_refs":["88:13","88:14","88:15","88:16","88:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:3","branch_refs":["root_000083/B001","root_000582/B001","root_000697/B011","root_000871/B001","root_001046/B006","root_001507/B001","root_001657/B001"],"candidate_id":"cand_19ec15bb49d40f156be0","commentary_obligation":"review","hft_ref":"hft_a099e2ae190659ab3f35","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_hidden_installation_crew","source_type":"hft","support_ids":["sup_8bfde22d07df29c05989"],"title":"delta_hidden_installation_crew","trust":"legacy_unbound"},{"anchor_refs":["88:3","88:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:3","branch_refs":["root_000722/B001","root_000762/B001","root_001046/B006","root_001507/B004","root_001507/B010"],"candidate_id":"cand_8ecacbaebfbed32f1fe8","commentary_obligation":"review","hft_ref":"hft_36c64bef73ebeceb563c","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_split_root_coercive_caravan","source_type":"hft","support_ids":["sup_15967cee13181a9d7512"],"title":"outlier_split_root_coercive_caravan","trust":"legacy_unbound"},{"anchor_refs":["88:11","88:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:3","branch_refs":["root_000741/B007","root_001046/B006","root_001361/B003","root_001507/B009"],"candidate_id":"cand_2a685e998ac06d27dee0","commentary_obligation":"review","hft_ref":"hft_731589e2c10c8ffe073e","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_manual_labor_chant","source_type":"hft","support_ids":["sup_411118ab1ab472386bde"],"title":"outlier_manual_labor_chant","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_85699d8e124a8c155483","connection_ref":"conn_d56b75a8a72cdd66eb0c","note":"The satisfied face and its striving form the immediate contrary outcome to 88:3.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_a60e34ec5b99168007f1","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:9","source_note":"The exhausted working face is the immediate contrary foil to 88:9.","source_row_role":"ranked_review","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:9","source_target_components":["88:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:9","target_evidence":{"arabic_uthmani":"لِّسَعْيِهَا رَاضِيَةٌۭ","ayah_ref":"88:9"},"target_ref":"88:9"},{"connection_evidence_ref":"conn_ev_6484743b7a397146f124","connection_ref":"conn_b12c6893e15307f9d360","note":"The opening Ghāshiyah names the encompassing event governing the focus.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_70e5fc7d783842f7f652","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:1","source_note":"The adjacent exhausted face begins the announced scene's concrete consequences.","source_row_role":"ranked_review","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:1","source_target_components":["88:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:1","target_evidence":{"arabic_uthmani":"هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ","ayah_ref":"88:1"},"target_ref":"88:1"},{"connection_evidence_ref":"conn_ev_6c9fb77519b3edaf0ace","connection_ref":"conn_bfe2700cc108b89291b4","note":"The hot fire is the immediate destination of the exhausted faces.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_b6affa6c14f0f2b86ef4","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:4","source_note":"Immediate preceding human-state frame identifies those addressed by 88:4.","source_row_role":"ranked_review","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:4","source_target_components":["88:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:4","target_evidence":{"arabic_uthmani":"تَصْلَىٰ نَارًا حَامِيَةًۭ","ayah_ref":"88:4"},"target_ref":"88:4"},{"connection_evidence_ref":"conn_ev_710368b8bdd3b38ea53f","connection_ref":"conn_6834541641a8af1d5295","note":"The flowing spring belongs to the contrasting blessed scene, without explaining the toil pair directly.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_4ab81e9138adccccec21","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"88:12","source_note":"Opposing opening scene provides only broad passage contrast.","source_row_role":"ranked_review","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:12","source_target_components":["88:12"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:12","target_evidence":{"arabic_uthmani":"فِيهَا عَيْنٌۭ جَارِيَةٌۭ","ayah_ref":"88:12"},"target_ref":"88:12"},{"connection_evidence_ref":"conn_ev_8832bfac920c512e2b0d","connection_ref":"conn_9d9249d5927567d10b41","note":"Humbled faces immediately specify the subjects qualified by 88:3.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_1e49da430c51a079f8f8","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:2","source_note":"Working and exhaustion directly unpack the condition following 88:2.","source_row_role":"ranked_review","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:2","source_target_components":["88:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:2","target_evidence":{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ","ayah_ref":"88:2"},"target_ref":"88:2"},{"connection_evidence_ref":"conn_ev_809a716003debdff1978","connection_ref":"conn_73e11cf0bc5e9047aefc","note":"The hunger that is not relieved completes the focus's futile, exhausting condition.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_104211b01aa79645b0ec","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:7","source_note":"Exhausting labor immediately precedes the food and shows the afflicted bodily condition.","source_row_role":"ranked_review","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:7","source_target_components":["88:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:7","target_evidence":{"arabic_uthmani":"لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ","ayah_ref":"88:7"},"target_ref":"88:7"},{"connection_evidence_ref":"conn_ev_02cacf6b60334f3a1dc0","connection_ref":"conn_fe76dd805ca32441a3f3","note":"The placed cups do not clarify the focus.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_8ff67450bc64fb688b23","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"88:14","source_note":"Toil and exhaustion form a broad contrary backdrop to the favorable provisions.","source_row_role":"ranked_review","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14","target_evidence":{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","ayah_ref":"88:14"},"target_ref":"88:14"},{"connection_evidence_ref":"conn_ev_fe7efd8a2d34a501b2e2","connection_ref":"conn_b8210ffc3707f01e1b42","note":"The flourishing faces begin the direct contrary portrait to 88:3.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_b74fe2d066072cb4388a","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:8","source_note":"Immediate exhausted labor is the central bodily counterpoint to ناعمة.","source_row_role":"ranked_review","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:8","source_target_components":["88:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:8","target_evidence":{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ","ayah_ref":"88:8"},"target_ref":"88:8"},{"connection_evidence_ref":"conn_ev_5d9f821f251dd23d2507","connection_ref":"conn_e831c78e6f7425b43176","note":"The scalding drink immediately develops the bodily consequence after 88:3-4.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":true,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_84797e333348a00bab68","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:5","source_note":"The toiling, exhausted faces directly complete the portrait of those made to drink from the scalding spring.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3"}],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:5","source_target_components":["88:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:5","target_evidence":{"arabic_uthmani":"تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ","ayah_ref":"88:5"},"target_ref":"88:5"},{"connection_evidence_ref":"conn_ev_ff7ffe2b59da3b1ec7b0","connection_ref":"conn_af1abd5fd5e6eec0475d","note":"The harmful food immediately develops the futility and deprivation of the exhausted faces.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":true,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_0ff712df5c808c596a21","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:6","source_note":"Immediate description of toil and exhaustion strengthens f03's depleted bodily state.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3"}],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:6","source_target_components":["88:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:6","target_evidence":{"arabic_uthmani":"لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ","ayah_ref":"88:6"},"target_ref":"88:6"},{"connection_evidence_ref":"conn_ev_4f040fe148611bf1414b","connection_ref":"conn_ded6549e77ba6a943fca","note":"The elevated garden begins the surah's contrary destination.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:10","source_target_components":["88:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:10","target_evidence":{"arabic_uthmani":"فِى جَنَّةٍ عَالِيَةٍۢ","ayah_ref":"88:10"},"target_ref":"88:10"},{"connection_evidence_ref":"conn_ev_e0244cc0d177e7335ca7","connection_ref":"conn_11776512ba13ace6e9cf","note":"Absence of idle speech helps characterize the contrary settled scene.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:11","source_target_components":["88:11"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:11","target_evidence":{"arabic_uthmani":"لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ","ayah_ref":"88:11"},"target_ref":"88:11"},{"connection_evidence_ref":"conn_ev_136dd069d58d8cc4093a","connection_ref":"conn_4e2c20440184d54d7f1c","note":"Raised couches contribute to the contrary condition of repose.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":true,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_90f630e1389b9e8f4a27","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:13","source_note":"Labor and fatigue form a contrary bodily condition to raised repose.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3"}],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:13","source_target_components":["88:13"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:13","target_evidence":{"arabic_uthmani":"فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ","ayah_ref":"88:13"},"target_ref":"88:13"},{"connection_evidence_ref":"conn_ev_74a0ebfba2116ea55261","connection_ref":"conn_617f92b3a22860c9aa55","note":"Ordered cushions contribute to the contrary condition of repose.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_4f5c1b73ae1004739fbf","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"88:15","source_note":"Toil and exhaustion provide a local contrary state to the prepared rest.","source_row_role":"ranked_review","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3"}],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:15","source_target_components":["88:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:15","target_evidence":{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","ayah_ref":"88:15"},"target_ref":"88:15"},{"connection_evidence_ref":"conn_ev_d675d608700f7050f2b5","connection_ref":"conn_254d88b4f4641a4ab0a8","note":"Spread carpets complete the contrast with bodily strain.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_5e5e49588b844a389e11","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"88:16","source_note":"The toil of the contrary faces does not clarify the image.","source_row_role":"ranked_review","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3"}],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:16","source_target_components":["88:16"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:16","target_evidence":{"arabic_uthmani":"وَزَرَابِىُّ مَبْثُوثَةٌ","ayah_ref":"88:16"},"target_ref":"88:16"}],"focus":{"arabic_uthmani":"عَامِلَةٌۭ نَّاصِبَةٌۭ","qac_morphemes":[{"lemma_ar":"عَامِلَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAmilap|ROOT:Eml|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:1:1","qac_word_ref":"88:3:1","root_ar":"ع م ل","surface_ar":"عَامِلَةٌ"},{"lemma_ar":"نَّاصِبَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:n~aASibap|ROOT:nSb|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:2:1","qac_word_ref":"88:3:2","root_ar":"ن ص ب","surface_ar":"نَّاصِبَةٌ"}],"word_analysis_qac_refs":[["88:3:1:1"],["88:3:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:3:1","88:3:2"]},"focus_surface_evidence":{"arabic_uthmani":"عَامِلَةٌۭ نَّاصِبَةٌۭ","qac_morphemes":[{"lemma_ar":"عَامِلَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAmilap|ROOT:Eml|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:1:1","qac_word_ref":"88:3:1","root_ar":"ع م ل","surface_ar":"عَامِلَةٌ"},{"lemma_ar":"نَّاصِبَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:n~aASibap|ROOT:nSb|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:3:2:1","qac_word_ref":"88:3:2","root_ar":"ن ص ب","surface_ar":"نَّاصِبَةٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:3:1:1"],["88:3:2:1"]],"word_analysis_refs":["88:3:1","88:3:2"],"word_rows":[{"analysis_record_ref":"88:3:1","analytic_gloss_range_en":"a laboring, action-bearing state carried by the faces from 88:2; the local pair with exhaustion narrows broad doing or work into exposed, unrewarded exertion without stated object, product, or accepted purpose","analytic_root_gloss_range_en":"broad range of intentional doing, work, making something work, appointment, pay, transaction, manual labor, exertion, suitability, and a few concrete or travel-related branches; this ayah selects the laboring/exertion branch while allowing cautious pressure from imposed operation","qac_refs":["88:3:1:1"],"root":{"arabic":"ع م ل","transliteration":"ʿ-m-l"},"surface":{"arabic":"عَامِلَةٌۭ","transliteration":"ʿāmilatun"}},{"analysis_record_ref":"88:3:2","analytic_gloss_range_en":"exhausted, strain-bearing active participial state co-predicated with the preceding labor; local grammar selects weariness as embodied condition, while upright-setting and assignedness branches add posture and imposed-burden pressure only within that limit","analytic_root_gloss_range_en":"broad range covering upright setting, set-up stones or markers, weariness and affliction, assigned share, fixed base, grammatical case-setting, hostility, chant, and travel; this ayah selects the weariness/strain branch and cautiously preserves posture and allotment pressure","qac_refs":["88:3:2:1"],"root":{"arabic":"ن ص ب","transliteration":"n-ṣ-b"},"surface":{"arabic":"نَّاصِبَةٌۭ","transliteration":"nāṣibatun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":2,"words_total":2,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":14,"missing_anchor_refs":[],"supplied_unique_anchor_count":14},"assigned_record_count":6,"assigned_records":[{"anchor_refs":["88:1","88:2","88:3"],"branch_refs":["root_000412/B001","root_001046/B001","root_001088/B002","root_001507/B004","root_001630/B004"],"candidate_id":"cand_dade14e1aaeecd43ee99","evidence_scope":"declared_pericope","hft_ref":"hft_92f36c8290d8cc2495fd","item_id":"delta_faces_as_exposed_transcript","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_faces_as_exposed_transcript","support_id":"sup_7c7aa593f7a7ba764f63"},{"anchor_refs":["88:3","88:4","88:5","88:6","88:7"],"branch_refs":["root_000278/B001","root_000358/B001","root_000722/B001","root_000744/B001","root_000880/B003","root_000908/B005","root_000934/B004","root_001046/B007","root_001110/B002","root_001507/B004"],"candidate_id":"cand_1a4c72f4247fbd42755c","evidence_scope":"declared_pericope","hft_ref":"hft_06f1e37c3945d9dbfe88","item_id":"delta_nonrecuperating_labor_circuit","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_nonrecuperating_labor_circuit","support_id":"sup_b54537c25533fd9ee37d"},{"anchor_refs":["88:3","88:8","88:9"],"branch_refs":["root_000569/B001","root_000709/B002","root_001046/B001","root_001507/B004","root_001525/B001","root_001630/B004"],"candidate_id":"cand_4d35782418e948ab7ab5","evidence_scope":"declared_pericope","hft_ref":"hft_6dabc67db6cf885ba745","item_id":"delta_contrastive_work_outcomes","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_contrastive_work_outcomes","support_id":"sup_173417c5c70549c3170f"},{"anchor_refs":["88:13","88:14","88:15","88:16","88:3"],"branch_refs":["root_000083/B001","root_000582/B001","root_000697/B011","root_000871/B001","root_001046/B006","root_001507/B001","root_001657/B001"],"candidate_id":"cand_19ec15bb49d40f156be0","evidence_scope":"declared_pericope","hft_ref":"hft_a099e2ae190659ab3f35","item_id":"delta_hidden_installation_crew","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_hidden_installation_crew","support_id":"sup_8bfde22d07df29c05989"},{"anchor_refs":["88:3","88:5"],"branch_refs":["root_000722/B001","root_000762/B001","root_001046/B006","root_001507/B004","root_001507/B010"],"candidate_id":"cand_8ecacbaebfbed32f1fe8","evidence_scope":"declared_pericope","hft_ref":"hft_36c64bef73ebeceb563c","item_id":"outlier_split_root_coercive_caravan","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_split_root_coercive_caravan","support_id":"sup_15967cee13181a9d7512"},{"anchor_refs":["88:11","88:3"],"branch_refs":["root_000741/B007","root_001046/B006","root_001361/B003","root_001507/B009"],"candidate_id":"cand_2a685e998ac06d27dee0","evidence_scope":"declared_pericope","hft_ref":"hft_731589e2c10c8ffe073e","item_id":"outlier_manual_labor_chant","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_manual_labor_chant","support_id":"sup_411118ab1ab472386bde"}],"diagnostics":[],"lane_counts":{"global":15,"macro":6,"micro":5},"packet_summary":{"ayah_count":26,"focus_ref":"88:3","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"88:3","lane":"macro","linguistic_source_ref":"88:3","surface_ref":"88:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:3","target_tokens":[["Çalışmış",["88:3:1"]],["yorulmuştur",["88:3:2"]]],"text":"Çalışmış, yorulmuştur."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":6,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":16,"id":"s088-p01-001-016","label":"Faces at the overwhelming event","number":1,"refs":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"88:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"88:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["88:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"88:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Wage, Stipend, and Livelihood","source_type":"channel","support_id":"sup_68fb5b0f30f61d3cfa4b","text":"Work produces compensation that continues as personal subsistence.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Wage, Stipend, and Livelihood","source_type":"channel","support_id":"sup_9df5070203cf78f5cf6c","text":"Labor, earned return, continuing payment, and livelihood form one compensation process.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Wage, Stipend, and Livelihood","source_type":"channel","support_id":"sup_a1e42e451d372a3afba0","text":"Value or responsibility passes between parties through agreement, payment, credit, wage, levy, gift, or redemption.","trust":"trusted"},{"branch_refs":["root_000240/B006","root_000709/B002","root_000934/B004","root_001046/B004"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"C:Wage, Stipend, and Livelihood","source_type":"channel","support_id":"sup_b0457721f1f3b8948cdf","text":"worker's wage `ع م ل:B004/m01`; continuing stipend `ج ر ي:B006/m01`; livelihood and good condition `ط ع م:B004/m02`; earned activity `س ع ي:B002/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Wage, Stipend, and Livelihood","source_type":"channel","support_id":"sup_fd59a7fd37d79a981cdf","text":"88:3 `عاملة` (`ع م ل`); 88:12 `جارية` (`ج ر ي`); 88:6 `طعام` (`ط ع م`); 88:9 `سعيها` (`س ع ي`)","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ","ayah_ref":"88:1"},{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ","ayah_ref":"88:2"},{"arabic_uthmani":"عَامِلَةٌۭ نَّاصِبَةٌۭ","ayah_ref":"88:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000412/B001","root_001046/B001","root_001088/B002","root_001507/B004","root_001630/B004"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001046","role":"Intentional work supplies the prior or continuing activity displayed on the face.","root":"ع م ل","source_ref":"88:3","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_001507","role":"Weariness supplies the visible condition produced by that activity.","root":"ن ص ب","source_ref":"88:3","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001088","role":"An encompassing cover supplies the event that surrounds and overwhelms the displayed subject.","root":"غ ش و","source_ref":"88:1","source_word_indices":["4"]},{"branch_id":"B004","mapped_root_id":"root_001630","role":"The face standing for the self makes the bodily surface represent the whole person.","root":"و ج ه","source_ref":"88:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000412","role":"Lowering and submission give the face a defeated posture into which the focus predicates continue.","root":"خ ش ع","source_ref":"88:2","source_word_indices":["3"]}],"changed_reading":{"after":"Faces, and through them whole selves, visibly bearing the trace of work after being overtaken and lowered.","before":"Unnamed workers described by their occupation and fatigue."},"confidence":"strong","mechanism":"The covering event overtakes exposed selves, and the lowered face becomes the display surface on which work and weariness can be seen. The focus pair therefore reads as a public bodily transcript, not only an inner biography.","model_id":"delta_faces_as_exposed_transcript","reader_inference":"The packet supplies an encompassing event, faces-as-selves, lowering, work, and strain; I infer that the grammar carries the faces into 88:3 and that their strain is visually diagnostic. A live alternative is a simple list of states with no causal order between engulfment, work, and fatigue.","status":"revised","structural_cues":["The feminine singular predicate in 88:2 is followed by two matching indefinite feminine singular predicates in 88:3, favoring continued predication of the faces.","The order encompassing event, lowered faces, then working and weariness makes the state readable as an aftermath."],"trigger_roots":["غ ش و","و ج ه","خ ش ع"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_faces_as_exposed_transcript","source_type":"hft","support_id":"sup_7c7aa593f7a7ba764f63","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"عَامِلَةٌۭ نَّاصِبَةٌۭ","ayah_ref":"88:3"},{"arabic_uthmani":"تَصْلَىٰ نَارًا حَامِيَةًۭ","ayah_ref":"88:4"},{"arabic_uthmani":"تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ","ayah_ref":"88:5"},{"arabic_uthmani":"لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ","ayah_ref":"88:6"},{"arabic_uthmani":"لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ","ayah_ref":"88:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":5,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":5,"target_morphology_supplied":false},"branch_refs":["root_000278/B001","root_000358/B001","root_000722/B001","root_000744/B001","root_000880/B003","root_000908/B005","root_000934/B004","root_001046/B007","root_001110/B002","root_001507/B004"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_001046","role":"Self-exertion supplies the energy expenditure that requires recovery.","root":"ع م ل","source_ref":"88:3","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_001507","role":"Weariness supplies the accumulating deficit when recovery fails.","root":"ن ص ب","source_ref":"88:3","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000880","role":"Encountering fire supplies the punishing environment in which exertion continues.","root":"ص ل ي","source_ref":"88:4","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000358","role":"Heating intensifies bodily demand and accelerates depletion.","root":"ح م ي","source_ref":"88:4","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000722","role":"Giving drink supplies intake, but its passive administration does not restore agency or strength.","root":"س ق ي","source_ref":"88:5","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000934","role":"Food as livelihood and sound condition supplies the restorative function that the restrictive clause frustrates.","root":"ط ع م","source_ref":"88:6","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_000908","role":"The named plant supplies the sole material input in the restrictive food clause.","root":"ض ر ع","source_ref":"88:6","source_word_indices":["6"]},{"branch_id":"B001","mapped_root_id":"root_000744","role":"Bodily fattening supplies the first explicitly negated sign of nourishment.","root":"س م ن","source_ref":"88:7","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001110","role":"Sufficiency supplies the second restorative function explicitly denied.","root":"غ ن ي","source_ref":"88:7","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000278","role":"An empty belly supplies the unresolved deficit that closes the failed recovery loop.","root":"ج و ع","source_ref":"88:7","source_word_indices":["6"]}],"changed_reading":{"after":"Work is trapped in a hostile metabolic system that supplies consumption without restoration, making exhaustion self-renewing.","before":"Work happens first and fatigue simply follows."},"confidence":"strong","mechanism":"Exertion occurs inside a closed depletion circuit: heat raises bodily demand, drink and plant-food are administered, but the intake neither builds the body nor suffices against hunger. Work therefore cannot recuperate into strength and keeps terminating in strain.","model_id":"delta_nonrecuperating_labor_circuit","reader_inference":"The packet supplies exertion, weariness, heat, administered intake, and explicit non-benefit; I supply the energetic arrow that labor requires recuperation and therefore worsens when nourishment fails. The live alternative is a punitive inventory whose food clauses do not explain the earlier work.","status":"revised","structural_cues":["The focus predicates are immediately followed by fire, passive watering, restrictive food, and two coordinated negations of benefit.","The sequence distinguishes the presence of intake from the absence of nourishment."],"trigger_roots":["ص ل ي","ح م ي","س ق ي","ط ع م","ض ر ع","س م ن","غ ن ي","ج و ع"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_nonrecuperating_labor_circuit","source_type":"hft","support_id":"sup_b54537c25533fd9ee37d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"عَامِلَةٌۭ نَّاصِبَةٌۭ","ayah_ref":"88:3"},{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ","ayah_ref":"88:8"},{"arabic_uthmani":"لِّسَعْيِهَا رَاضِيَةٌۭ","ayah_ref":"88:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000569/B001","root_000709/B002","root_001046/B001","root_001507/B004","root_001525/B001","root_001630/B004"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001046","role":"Intentional work supplies the activity whose outcome the two face panels differentiate.","root":"ع م ل","source_ref":"88:3","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_001507","role":"Weariness supplies the failed or adverse outcome in the first panel.","root":"ن ص ب","source_ref":"88:3","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001630","role":"The face as self repeats the same display unit and permits a controlled comparison.","root":"و ج ه","source_ref":"88:8","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001525","role":"Good condition and blessing reverse the first panel's visible depletion.","root":"ن ع م","source_ref":"88:8","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000709","role":"Work and earning provide a near counterpart to the focus ayah's intentional doing.","root":"س ع ي","source_ref":"88:9","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000569","role":"Satisfaction supplies the successful relation between the second faces and their striving.","root":"ر ض و","source_ref":"88:9","source_word_indices":["2"]}],"changed_reading":{"after":"The ayah marks work whose result has inverted: one face's activity resolves into exhaustion while the counterpart's striving resolves into satisfaction.","before":"Work itself is the damaging condition."},"confidence":"strong","mechanism":"A second face panel repeats the human display surface but reverses its condition: good state and satisfaction attach to its own striving. The contrast separates work from outcome, so work itself is not the differentiator; whether striving culminates in depletion or satisfaction is.","model_id":"delta_contrastive_work_outcomes","reader_inference":"The packet supplies parallel faces, adverse work-weariness, good condition, striving, and satisfaction; I infer that the panels compare outcomes of activity. A live alternative is that the groups are contrasted without making a general claim about work.","status":"revised","structural_cues":["The phrase pattern of faces on that day recurs at 88:8, establishing two parallel panels.","The possessive attachment in 88:9 makes the second faces satisfied with their own striving, not with an unrelated gift."],"trigger_roots":["و ج ه","ن ع م","س ع ي","ر ض و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_contrastive_work_outcomes","source_type":"hft","support_id":"sup_173417c5c70549c3170f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ","ayah_ref":"88:13"},{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","ayah_ref":"88:14"},{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","ayah_ref":"88:15"},{"arabic_uthmani":"وَزَرَابِىُّ مَبْثُوثَةٌ","ayah_ref":"88:16"},{"arabic_uthmani":"عَامِلَةٌۭ نَّاصِبَةٌۭ","ayah_ref":"88:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":5,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":5,"target_morphology_supplied":false},"branch_refs":["root_000083/B001","root_000582/B001","root_000697/B011","root_000871/B001","root_001046/B006","root_001507/B001","root_001657/B001"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001046","role":"Manual crews supply the hidden producers behind a furnished material environment.","root":"ع م ل","source_ref":"88:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001507","role":"Setting things upright supplies installation as one component of the crew's work.","root":"ن ص ب","source_ref":"88:3","source_word_indices":["2"]},{"branch_id":"B011","mapped_root_id":"root_000697","role":"A place of settled reclining supplies the use-value produced by the installation sequence.","root":"س ر ر","source_ref":"88:13","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000582","role":"Raising supplies the first visible completed operation.","root":"ر ف ع","source_ref":"88:13","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001657","role":"Putting an object in a fixed place supplies deliberate placement.","root":"و ض ع","source_ref":"88:14","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000871","role":"Alignment on an even line supplies ordered arrangement.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000083","role":"Dispersing and spreading supplies the final distribution of the furnished field.","root":"ب ث ث","source_ref":"88:16","source_word_indices":["2"]}],"changed_reading":{"after":"The focus can also disclose an invisible installation crew whose work is erased from the later passive display of repose and abundance.","before":"The focus names visible sufferers, while the later furnishings simply exist."},"confidence":"exploratory","mechanism":"The garden inventory is a chain of completed material operations: a resting place is raised, vessels are placed, cushions aligned, and carpets distributed. Read beside the focus roots, those passive results briefly expose the otherwise absent labor of operating, lifting, installing, arranging, and spreading.","model_id":"delta_hidden_installation_crew","reader_inference":"The packet supplies manual-work and installation branches plus a sequence of passively completed furnishings; I infer an absent production process and let it reactivate the focus pair as its worker/operator. The live alternative is that the furnishings are only a scenic inventory and have no relation to the exhausted faces.","status":"new","structural_cues":["Four successive feminine passive participles in 88:13-16 echo the compact participial texture of 88:3 while presenting results without agents.","The operations proceed from elevation to placement, alignment, and distribution."],"trigger_roots":["س ر ر","ر ف ع","و ض ع","ص ف ف","ب ث ث"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_hidden_installation_crew","source_type":"hft","support_id":"sup_8bfde22d07df29c05989","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"عَامِلَةٌۭ نَّاصِبَةٌۭ","ayah_ref":"88:3"},{"arabic_uthmani":"تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ","ayah_ref":"88:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000722/B001","root_000762/B001","root_001046/B006","root_001507/B004","root_001507/B010"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001046","role":"Manual labor crews supply the group subjected to the movement regime.","root":"ع م ل","source_ref":"88:3","source_word_indices":["1"]},{"branch_id":"B010","mapped_root_id":"root_001507","role":"A full-day march supplies the caravan-like duration of the labor.","root":"ن ص ب","source_ref":"88:3","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001507","role":"Weariness supplies the bodily cost of being kept in motion.","root":"ن ص ب","source_ref":"88:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000722","role":"Literal giving of drink supplies the apparent watering station in the movement cycle.","root":"س ق ي","source_ref":"88:5","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000762","role":"The split mapped image of driving and herding supplies coercive propulsion through that station.","root":"س ق ي","source_ref":"88:5","source_word_indices":["1"]}],"changed_reading":{"after":"A contained caravan reading sees laborers driven from stage to stage, with watering itself functioning as part of the system that keeps them moving.","before":"Exhausted workers are later given a punishing drink."},"confidence":"exploratory","containment":"This is surprising because it uses the packet's non-dominant mapped root for س ق ي to activate driving and herding beside literal watering. It remains anchored through the focus branches for manual crews, day-long marching, and weariness, but downstream prose should present it only as a split-root material analogy, not as a claim that the surface verb lexically means driving here.","focus_anchor":"The focus can picture a hand-working group kept moving through a full day's march until exhausted.","outlier_id":"outlier_split_root_coercive_caravan"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_split_root_coercive_caravan","source_type":"hft","support_id":"sup_15967cee13181a9d7512","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ","ayah_ref":"88:11"},{"arabic_uthmani":"عَامِلَةٌۭ نَّاصِبَةٌۭ","ayah_ref":"88:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000741/B007","root_001046/B006","root_001361/B003","root_001507/B009"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001046","role":"Manual labor crews supply the collective body capable of coordinating effort by sound.","root":"ع م ل","source_ref":"88:3","source_word_indices":["1"]},{"branch_id":"B009","mapped_root_id":"root_001507","role":"A raised-voice song or riders' chant supplies an acoustic rhythm for collective exertion.","root":"ن ص ب","source_ref":"88:3","source_word_indices":["2"]},{"branch_id":"B007","mapped_root_id":"root_000741","role":"Pleasurable hearing and song supply the positive acoustic category against which the focus chant can be tested.","root":"س م ع","source_ref":"88:11","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001361","role":"Mixed noisy sound supplies the acoustic condition excluded from the contrasting garden.","root":"ل غ و","source_ref":"88:11","source_word_indices":["4"]}],"changed_reading":{"after":"A fragile acoustic reading hears a manual or traveling crew marked by raised chant, later countered by a space free of mixed, empty noise.","before":"The focus is a silent visual report of labor and fatigue."},"confidence":"exploratory","containment":"This is surprising because it activates the rare raised-voice song branch of ن ص ب and combines it with a manual crew and the later acoustic contrast. It remains focus-anchored by an exact branch for word 2, but no syntax requires a song sense; downstream prose should label it a fragile acoustic overlay rather than a translation.","focus_anchor":"The focus inventories permit manual workers at word 1 and a raised-voice riders' song or chant at word 2.","outlier_id":"outlier_manual_labor_chant"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_manual_labor_chant","source_type":"hft","support_id":"sup_411118ab1ab472386bde","trust":"legacy_unbound"}]}
</lane_packet_json>
