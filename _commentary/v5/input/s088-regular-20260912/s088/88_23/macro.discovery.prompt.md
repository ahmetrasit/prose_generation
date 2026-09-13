# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **88:23**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_23/macro.discovery.json` and modify nothing
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
  "ayah_ref": "88:23",
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
{"branch_registry":[{"boundary":"Includes أبابيل for birds or groups arriving scattered, successive, or in separate bands","branch_kind":null,"branch_ref":"root_000006/B003","candidate_links":[{"candidate_id":"cand_cf5b732356a2c14586ed","lane":"macro"}],"focus_root_occurrences":[],"gloss":"successive or scattered groups","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الجماعات الأبابيل","image_en":"successive or scattered groups"}}],"root_ar":"ء ب ل","root_id":"root_000006","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الجماعات الأبابيل","image_en":"successive or scattered groups","scope_ar":"يدخل فيه أبابيل للطير أو الجماعات المتفرقة أو المتتابعة بعضا بعد بعض","scope_en":"Includes أبابيل for birds or groups arriving scattered, successive, or in separate bands"},"support_links":["sup_c10ff24f40bd6b5ad803"]},{"boundary":"Covers the fixed divine name and oath or invocation formulas built on it, including Allah, O Allah, and reduced/formulaic forms cited by the dictionaries.","branch_kind":null,"branch_ref":"root_000047/B002","candidate_links":[{"candidate_id":"cand_bee48b9068fee4761962","lane":"macro"}],"focus_root_occurrences":[],"gloss":"Allah as a fixed name in oath and invocation formulas","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"اسم الله في القسم والنداء","image_en":"Allah as a fixed name in oath and invocation formulas"}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"اسم الله في القسم والنداء","image_en":"Allah as a fixed name in oath and invocation formulas","scope_ar":"يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.","scope_en":"Covers the fixed divine name and oath or invocation formulas built on it, including Allah, O Allah, and reduced/formulaic forms cited by the dictionaries."},"support_links":["sup_0c6dae45056bdd70f0cd"]},{"boundary":"Includes returning, coming back, the act of return, and a return-place or gathering point.","branch_kind":null,"branch_ref":"root_000065/B001","candidate_links":[{"candidate_id":"cand_35a71a2826af60921ef3","lane":"macro"},{"candidate_id":"cand_bd9c6a892aaff4cff6cb","lane":"macro"}],"focus_root_occurrences":[],"gloss":"turning back to a return-place","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الرجوع إلى المآب والموضع","image_en":"turning back to a return-place"}}],"root_ar":"ء و ب","root_id":"root_000065","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الرجوع إلى المآب والموضع","image_en":"turning back to a return-place","scope_ar":"يدخل فيه آب يؤوب بمعنى رجع، والإياب والأوبة والمآب مرجعا أو موضعا، وما يرجع إلى مأواه أو يجتمع في موضعه.","scope_en":"Includes returning, coming back, the act of return, and a return-place or gathering point."},"support_links":["sup_af17eee031fdcbe1d3e6","sup_b35576db6122b0333bd2"]},{"boundary":"The word السطر used for a young male goat.","branch_kind":null,"branch_ref":"root_000704/B007","candidate_links":[{"candidate_id":"cand_cf5b732356a2c14586ed","lane":"macro"}],"focus_root_occurrences":[],"gloss":"young goat named satr","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"السطر العتود","image_en":"young goat named satr"}}],"root_ar":"س ط ر","root_id":"root_000704","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"السطر العتود","image_en":"young goat named satr","scope_ar":"السطر بمعنى العتود من الغنم","scope_en":"The word السطر used for a young male goat."},"support_links":["sup_c10ff24f40bd6b5ad803"]},{"boundary":"Çekirdek fiziksel örtmedir; dinî inkâr, nimeti yadsıma ve günahı giderme bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001307/B001","candidate_links":[{"candidate_id":"cand_f3867b72479dda30b840","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"örtmek, kapatmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesnenin üstünü kapatarak onu görünmez veya örtülü duruma getirme işlemi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zırhı giysiyle kaplama, silahla örtünme ve külün üstünün toprakla kapanması çekirdeğin özel gerçekleşmeleridir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Güneşin yıldızları görünmez kılması da görsel örtme sonucu üzerinden bu çekirdeğe bağlanır."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin üstünü başka bir şeyle kapatıp görünmesini engelleyen genel çekirdek için uygundur.","boundary_detail":"Çekirdek fiziksel örtmedir; dinî inkâr, nimeti yadsıma ve günahı giderme bu dala girmez.","branch_image_ar":"ستر وتغطية","concept_gloss":"örtmek, kapatmak","contextual_glosses":[{"applicability":"Zırhın giysiyle veya külün toprakla kaplanması gibi somut bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Somut bir nesnenin üstünün kapatılması işlemini eksiksiz korur."},"facet_ids":["F001","F002"],"text":"üstünü örtmek","usage_role":"contextual"},{"applicability":"Güneş ışığının yıldızları görünmez kıldığı göksel bağlamda sonuç odaklı doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görsel örtmenin görünürlüğü ortadan kaldıran sonucunu korur."},"facet_ids":["F003"],"text":"görünmez kılmak","usage_role":"contextual"}],"definition":"Bir şeyi başka bir şeyle örterek görünmesini engellemek veya kapalı duruma getirmektir. Zırhın giysiyle, kişinin silahla ya da külün savrulan toprakla örtülmesi bu işlemin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesnenin üstünü kapatarak onu görünmez veya örtülü duruma getirme işlemi."},{"facet_id":"F002","role":"specialization","statement":"Zırhı giysiyle kaplama, silahla örtünme ve külün üstünün toprakla kapanması çekirdeğin özel gerçekleşmeleridir."},{"facet_id":"F003","role":"extension","statement":"Güneşin yıldızları görünmez kılması da görsel örtme sonucu üzerinden bu çekirdeğe bağlanır."}],"identity_rationale":"Kaynak ifadesi, bir şeyi örtme ve görünmez kılma çekirdeğini; zırhı giysiyle kaplama, silahla örtünme, külün toprakla kapanması ve yıldızların güneş ışığında görünmemesi gibi gerçekleşmelerle açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi örtmek ve kapatmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"zırhının üstüne bir giysi geçirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"silahlarıyla örtünmek veya silah kuşanmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"rüzgârın savurduğu toprakla örtülmüş kül"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"güneşin yıldızları görünmez kılması"}],"lexicalization_note":"Tanım yalın örtme çekirdeğini korur; zırh, silah, kül ve gök cisimleriyle ilgili kullanımlar bu çekirdeğin yapıya bağlı gerçekleşmeleri olarak ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel örtme dalı en yakın karışma olasılığını taşıdığı için yayımlandı, öteki adaylar yalnızca örnek veya ortak senaryo düzeyinde kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdek büyük ölçüde örtüşür; ancak komşu dal soyut gizlemeyi ve örtü nesnelerini de kapsarken bu dalın kanıtı belirli somut ve görsel gerçekleşmelere dayanır.","focus_only":"Bu dal zırh, silah, kül ve güneş ışığı gibi belirli gerçekleşmeleri de taşır.","gloss":"örtmek, kapatmak","neighbor_only":"Komşu dal haber veya tanıklığı gizleme ve örtü adı gibi daha geniş kullanımlara da uzanır.","neighbor_ref":"root_000438/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde bir şeyi örterek görünmesini engelleme vardır."}],"source_phrase_ar":"الستر والتغطية (maqayis)؛ كل شيء غطى شيئا فقد كفره (ayn;sihah;tahdhib)؛ كفرت الشيء أي سترته ورماد مكفور (sihah)؛ تكفر في السلاح (mufradat)؛ كفرت الشمس النجوم (mufradat)","source_summary":"Kaynaklar örtme ve kapatma çekirdeğinde birleşir; farklı örnekler bu işlemin nesne, giysi, silah, kül ve gök görünümü üzerindeki gerçekleşmelerini gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه ستر الشيء وتغطيته وكفر الدرع بثوب وتغطية السلاح والرماد المكفور وستر الشمس النجوم والسحاب الشمس","what_is_not_ar":"ليس الكفر الديني ولا كفران النعمة ولا الكفارة ولا الزراعة"},"support_links":["sup_d8d61ae7f0534b9fac9d"]},{"boundary":"Dal genel karanlık ya da genel su kütlesi değildir; kaynakta örtücü etkisiyle adlandırılan belirli varlıklarla sınırlıdır.","branch_kind":"bare","branch_ref":"root_001307/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"örten karanlık veya enginlik","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Karanlık, genişlik ya da kapatma etkisiyle başka şeylerin görünmesini veya seçilmesini engelleyen varlık."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gece, deniz, büyük ırmak, gün batımı ve bulut kaynaklarda bu nitelemenin farklı gönderimleri olarak sıralanır."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Farklı gönderimleri tek bir nesne türüne indirgemeden ortak örtücü etkiyi anlatmak için uygundur.","boundary_detail":"Dal genel karanlık ya da genel su kütlesi değildir; kaynakta örtücü etkisiyle adlandırılan belirli varlıklarla sınırlıdır.","branch_image_ar":"غمر ساتر","concept_gloss":"örten karanlık veya enginlik","contextual_glosses":[{"applicability":"Sözün karanlık geceyi nitelediği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deniz, büyük ırmak, gün batımı ve bulut gönderimlerini dışarıda bırakır.","preserves":"Gecenin karanlığıyla kişileri ve görünümü örtmesi özelliğini korur."},"facet_ids":["F001","F002"],"text":"karanlığıyla örten gece","usage_role":"contextual"},{"applicability":"Sözün deniz veya büyük ırmak için kullanıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gece, gün batımı ve bulut gönderimlerini dışarıda bırakır.","preserves":"Deniz ve büyük ırmak gönderimlerinin genişlik ve kuşatıcılık yönünü korur."},"facet_ids":["F001","F002"],"text":"engin su kütlesi","usage_role":"contextual"}],"definition":"Karanlığı, genişliği veya kapatma etkisi nedeniyle kişileri ya da görünümü örten karanlık gece, deniz, büyük ırmak, gün batımı veya bulut için kullanılan bir nitelemedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Karanlık, genişlik ya da kapatma etkisiyle başka şeylerin görünmesini veya seçilmesini engelleyen varlık."},{"facet_id":"F002","role":"source_variant","statement":"Gece, deniz, büyük ırmak, gün batımı ve bulut kaynaklarda bu nitelemenin farklı gönderimleri olarak sıralanır."}],"identity_rationale":"Kaynak ifadesi karanlık geceyi, denizi, büyük ırmağı, gün batımını ve bulutu aynı adlandırma çevresinde toplar; bunların tümünü tek bir gerçek 'kuşatan örtü' türü saymak yerine, karanlık, genişlik veya kapatma etkisiyle örten farklı varlıklar olarak anlamak gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"karanlık gece, deniz, büyük ırmak, gün batımı veya bulut"}],"lexicalization_note":"Yalın dal, kaynakta doğrudan adlandırılan gece, deniz, büyük ırmak, gün batımı ve bulut kapsamıyla tanımlanır; yapıya özgü başka anlam eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; suyla örtme ve gece karanlığı adayları dalın iki temel gönderim alanını sınırlandırdığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli varlıklara verilen bir nitelemeyi anlatır; komşu dal ise çok suyun örtmesi ve suya gömülme süreçlerini merkez alır.","focus_only":"Bu dal karanlık geceyi, gün batımını ve bulutu da aynı örtücü nitelemeye dahil eder.","gloss":"örten enginlik","neighbor_only":"Komşu dal suyun yükselmesi, dalma ve suyla kaplanma olaylarını da kapsar.","neighbor_ref":"root_001105/B001","relation_type":"near_neighbor","shared_zone":"Deniz ve büyük ırmak, genişlikleri ve örtücü etkileri bakımından iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Ortak gece örneğine rağmen bu dal çok gönderimli bir adlandırmadır; komşu dalın çekirdeği doğrudan gece karanlığıdır.","focus_only":"Bu dal gece dışında deniz, büyük ırmak, gün batımı ve bulutu da kapsar.","gloss":"karanlık gece","neighbor_only":"Komşu dal yalnızca gece karanlığının gölge veya karanlık örtü oluşunu işler.","neighbor_ref":"root_000966/B002","relation_type":"near_neighbor","shared_zone":"Karanlık gecenin görüşü örtmesi iki dalda da bulunur."}],"source_phrase_ar":"الكافر مغيب الشمس ويقال بل البحر والنهر العظيم كافر (maqayis)؛ الكافر الليل والبحر ومغيب الشمس والكافر النهر العظيم (ayn)؛ الكافر الليل المظلم والكافر البحر والنهر العظيم (sihah)؛ الليل كافر لأنه ستر بظلمته (tahdhib)؛ وصف الليل بالكافر لستره الأشخاص والكافر للسحاب (mufradat)","source_summary":"Kaynaklar aynı sözü karanlık gece, deniz ve büyük ırmak için verir; bazı aktarımlar gün batımını ve bulutu da örtücü etkileri nedeniyle bu listeye ekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الكافر للليل المظلم والبحر والنهر العظيم ومغيب الشمس وما يستر بظلمته أو سعته","what_is_not_ar":"ليس الأرض البعيدة ولا القرية ولا الجبل ولا الكفر الديني"},"support_links":[]},{"boundary":"Dal dinî gerçeği ve inancı reddetmeyle sınırlıdır; nimeti yadsıma veya yalnızca genel bir gerçeği inkâr etme bunun tamamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001307/B003","candidate_links":[{"candidate_id":"cand_2a6a78a71a541a12c98f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"dinî gerçeği reddetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnancın karşıtı olarak dinî gerçeği, birliği, dinî hükmü veya peygamberliği reddetme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalben bilip sözle kabul etmeme, bilip boyun eğmeme, dıştan inanmış görünme ve hem kalple hem dille inkâr etme farklı türlerdir."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnancın karşıtı olan çekirdeği ve reddedilen dinî içeriği birlikte ifade eder.","boundary_detail":"Dal dinî gerçeği ve inancı reddetmeyle sınırlıdır; nimeti yadsıma veya yalnızca genel bir gerçeği inkâr etme bunun tamamı değildir.","branch_image_ar":"حجب الحق","concept_gloss":"dinî gerçeği reddetme","contextual_glosses":[{"applicability":"Dalın genel dinî karşıtlık bağlamında eylem olarak çevrilmesi gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnancı kabul etmeme ve ona karşı durma çekirdeğini korur."},"facet_ids":["F001"],"text":"inancı reddetmek","usage_role":"general"},{"applicability":"Bile bile yadsıma veya direnme türünün açıklandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İkiyüzlülük ve bütünüyle bilgisiz inkâr gibi öteki türleri dışarıda bırakır.","preserves":"Bilgi ile dışa vurulan ret arasındaki ayrımı korur."},"facet_ids":["F002"],"text":"kalben bilip kabul etmemek","usage_role":"explanatory"}],"definition":"İnancı, birliği, dinî hükmü veya peygamberliği reddederek dinî gerçeği örtmek ya da kabul etmemektir. Kaynaklar bunu inkâr, bile bile direnme, ikiyüzlülük, ortak koşma ve yalanlama gibi türlere ayırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnancın karşıtı olarak dinî gerçeği, birliği, dinî hükmü veya peygamberliği reddetme."},{"facet_id":"F002","role":"specialization","statement":"Kalben bilip sözle kabul etmeme, bilip boyun eğmeme, dıştan inanmış görünme ve hem kalple hem dille inkâr etme farklı türlerdir."}],"identity_rationale":"Kaynak ifadesi bu dalı inancın karşıtı ve gerçeğin örtülmesi olarak tanımlar; birliği, dinî hükmü veya peygamberliği yadsıma ile inkâr, bile bile direnme, ikiyüzlülük ve ortak koşma türlerini açıkça içerir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"dinî gerçeği veya inancı reddetme"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kalben bildiği gerçeği diliyle kabul etmeme"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"gerçeği bildiği hâlde inatla kabul etmemek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kalben reddederken diliyle inanmış görünmek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"gerçeği hem kalple hem dille inkâr etmek"}],"lexicalization_note":"Yalın dinî reddetme çekirdeği korunur; kalben bilip söylememe, bilip kabul etmeme, dıştan inanmış görünme ve hem kalple hem dille reddetme yapıya bağlı türlerdir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yadsıma en yakın anlam komşusu, inanma ise açık karşıt kutup olduğu için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın dinî kapsamı ve birden çok tutum türü vardır; komşu dal ise konusu ne olursa olsun bilgiye rağmen yadsımayı merkez alır.","focus_only":"Bu dal özellikle dinî inancı ve gerçeği reddeder; ikiyüzlülük ve ortak koşma gibi türleri de kapsar.","gloss":"bile bile reddetme","neighbor_only":"Komşu dal, doğruluğu bilinen herhangi bir şeyi inkâr etmeyi din alanıyla sınırlamadan anlatır.","neighbor_ref":"root_000224/B001","relation_type":"near_synonym","shared_zone":"Bilinen bir gerçeği kabul etmeme iki dalın ortak alanıdır."},{"boundary_match":"opposed","distinction":"Biri gerçeği reddetme, diğeri onu doğrulayıp benimseme yönündedir.","focus_only":"Bu dal dinî gerçeği kabul etmemeyi ve reddetmeyi bildirir.","gloss":"reddetme / inanma","neighbor_only":"Komşu dal haberi veya dinî gerçeği doğrulayıp kalben benimsemeyi bildirir.","neighbor_ref":"root_000054/B002","relation_type":"polarity_pair","shared_zone":"İki dal aynı kabul-ret ekseninde dinî veya doğrulanabilir içerikle ilişki kurar."}],"source_phrase_ar":"الكفر ضد الإيمان سمى لأنه تغطية الحق (maqayis)؛ الكفر نقيض الإيمان والكفر أربعة أنحاء كفر الجحود وكفر المعاندة وكفر النفاق وكفر الإنكار (ayn)؛ الكفر ضد الإيمان (sihah)؛ الكفر نقيض الإيمان وكفر إنكار وكفر جحود وكفر معاندة وكفر نفاق وكفر هو شرك وكفر بكتاب الله ورسوله والتكذيب بالله (tahdhib)؛ أعظم الكفر جحود الوحدانية أو الشريعة أو النبوة (mufradat)","source_summary":"Kaynaklar dalı inancın karşıtı sayar ve gerçeği örtme düşüncesiyle açıklar; toplu aktarım çeşitli inkâr, direnme ve ikiyüzlülük biçimlerini de sıralar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الكفر نقيض الإيمان وجحود الوحدانية أو الشريعة أو النبوة والإنكار والجحود والمعاندة والنفاق والشرك والتكذيب","what_is_not_ar":"ليس كفران النعمة وحده ولا البراءة ولا التكفير عن السيئات"},"support_links":["sup_64449116e4f17ecfc878"]},{"boundary":"Nesne özellikle nimettir ve belirleyici sonuç şükrün terkidir; genel dinî ret bu dala kendiliğinden girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001307/B004","candidate_links":[{"candidate_id":"cand_2a6a78a71a541a12c98f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"nimeti yadsıma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nimeti yadsıma veya şükrünü yerine getirmeyerek değerini örtme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nimetleri sürekli ve aşırı biçimde yadsıyan kişi bu tutumun yoğunlaşmış taşıyıcısıdır."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nimeti tanımama ile ona şükretmeme çekirdeğini kısa ve doğal biçimde verir.","boundary_detail":"Nesne özellikle nimettir ve belirleyici sonuç şükrün terkidir; genel dinî ret bu dala kendiliğinden girmez.","branch_image_ar":"ستر النعمة","concept_gloss":"nimeti yadsıma","contextual_glosses":[{"applicability":"Bir nimetin veya yapılan iyiliğin tanınmadığı gündelik bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapılan iyiliği tanımama ve karşılığında şükretmeme tutumunu korur."},"facet_ids":["F001"],"text":"iyiliğin kıymetini bilmemek","usage_role":"contextual"}],"definition":"Bir nimeti tanımamak, değerini örtmek veya onun gerektirdiği şükrü yerine getirmemektir. Bu tutumda aşırı olan kişi de aynı anlam alanında nitelenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nimeti yadsıma veya şükrünü yerine getirmeyerek değerini örtme."},{"facet_id":"F002","role":"specialization","statement":"Nimetleri sürekli ve aşırı biçimde yadsıyan kişi bu tutumun yoğunlaşmış taşıyıcısıdır."}],"identity_rationale":"Kaynak ifadesi nimeti yadsımayı, onu örtmeyi ve gereği olan şükrü yerine getirmemeyi aynı çekirdekte birleştirir; dalın geçici çerçevesi bu koşulu doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"nimeti yadsımak ve şükrünü yerine getirmemek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"nimeti yadsıma ve şükretmeme"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"nimetleri aşırı biçimde yadsıyan kimse"},{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"iyilikleri karşılıksız ve teşekkürsüz kalan cömert adam"}],"lexicalization_note":"Nimeti yadsıma çekirdeği yalın ve türemiş kullanımlarda korunur; nimetle kurulan yapı ve aşırılık bildiren kişi nitelemesi ayrı gerçekleşmelerdir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; daha geniş nankörlük dalı yakın eş, şükür dalı ise doğrudan karşıt kutup olarak yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal nankörlüğü daha geniş bir davranış kümesine yayar; bu dal doğrudan nimet ile şükür arasındaki ilişkiyle sınırlıdır.","focus_only":"Bu dal nimetin yadsınmasını ve şükrünün terkini doğrudan çekirdek yapar.","gloss":"nimeti yadsıma","neighbor_only":"Komşu dal nimet yanında dostluğu kesme, felaketleri sayıp nimetleri unutma ve yardımı esirgeme gibi tutumları da kapsar.","neighbor_ref":"root_001321/B002","relation_type":"near_synonym","shared_zone":"Nimeti tanımama ve ona şükretmeme iki dalda da merkezîdir."},{"boundary_match":"opposed","distinction":"Biri nimetin değerini örter ve şükrü bırakır; diğeri nimeti tanır ve şükrü gösterir.","focus_only":"Bu dal nimeti tanımamayı ve şükrünü terk etmeyi bildirir.","gloss":"nankörlük / şükür","neighbor_only":"Komşu dal nimeti tanımayı, övmeyi ve şükrü sözle ya da davranışla göstermeyi bildirir.","neighbor_ref":"root_000810/B001","relation_type":"polarity_pair","shared_zone":"İki dal nimetin tanınması ve karşılığının verilmesi eksenindedir."}],"source_phrase_ar":"كفران النعمة جحودها وسترها (maqayis)؛ الكفر نقيض الشكر كفر النعمة أي لم يشكرها (ayn)؛ الكفر أيضا جحود النعمة وهو ضد الشكر (sihah)؛ الكفر كفر النعمة وهو نقيض الشكر (tahdhib)؛ كفر النعمة وكفرانها سترها بترك أداء شكرها (mufradat)","source_summary":"Kaynaklar nimeti yadsımayı şükrün karşıtı sayar; örtme açıklaması, nimetin gerektirdiği şükrü yerine getirmemeyi bu karşıtlığın belirleyici davranışı yapar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه كفر النعمة وكفرانها وجحودها وترك شكرها والكفور في كفران النعمة","what_is_not_ar":"ليس الكفر الديني عند الإطلاق ولا الكفارة ولا البراءة"},"support_links":["sup_64449116e4f17ecfc878"]},{"boundary":"Bu dal bir inancı yadsımak değil, belirli bir şeyle bağı reddedip ondan uzaklaşmaktır.","branch_kind":"non_bare","branch_ref":"root_001307/B005","candidate_links":[{"candidate_id":"cand_bd9c6a892aaff4cff6cb","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"bağını reddedip uzaklaşmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir şeyle bağı reddederek ondan uzaklaşma ve kendini onun dışında tutma."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi, görüş, eylem veya sorumlulukla ilişkiyi açıkça reddeden bağlı kullanım için uygundur.","boundary_detail":"Bu dal bir inancı yadsımak değil, belirli bir şeyle bağı reddedip ondan uzaklaşmaktır.","branch_image_ar":"تبرؤ وتنصل","concept_gloss":"bağını reddedip uzaklaşmak","contextual_glosses":[{"applicability":"Aidiyet veya sorumluluk bağının reddedildiği bağlamlarda açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aidiyet bağını reddetme ve kendini dışarıda konumlandırma sonucunu korur."},"facet_ids":["F001"],"text":"ondan olmadığını açıklamak","usage_role":"explanatory"}],"definition":"Bir şeyle olan bağı reddetmek, ondan uzak olduğunu açıklamak ve sorumluluk ya da aidiyet bağından sıyrılmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir şeyle bağı reddederek ondan uzaklaşma ve kendini onun dışında tutma."}],"identity_rationale":"Kaynak ifadesi sözün bir şeyden uzak olduğunu bildirme, onunla bağını reddetme ve ondan sıyrılma anlamında kullanılabildiğini açıkça söyler.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bir şeyle bağını reddedip ondan uzaklaşmak"}],"lexicalization_note":"Anlam yalnızca bir şeyden uzaklaşmayı bildiren bağlı yapıda korunur; yalın köke genel bir ayrılma anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel bağ kesme ve uzak durma dalı en yakın anlam sınırını verdiği için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yapısal olarak bağlı ve dar bir ilişki reddidir; komşu dal genel uzaklık, arınmışlık ve sorumsuzluk bildirimlerini de içerir.","focus_only":"Bu dal belirli bir bağlı söz yapısında ilişkiyi reddetmeyi anlatır.","gloss":"bağını reddedip uzaklaşmak","neighbor_only":"Komşu dal kişi, iş, kusur ve kötülükten arınma, uzak durma, uyarma ve mazeret bildirme gibi daha geniş bir alanı kapsar.","neighbor_ref":"root_000100/B002","relation_type":"near_synonym","shared_zone":"Bir kişi veya şeyle ilişkiyi reddetme ve ondan uzak durma iki dalda ortaktır."}],"source_phrase_ar":"يكون الكفر أيضا بمعنى البراءة (tahdhib)؛ قد يعبر عن التبري بالكفر (mufradat)","source_summary":"Kaynaklar bağlı kullanımın bir şeyden uzak olduğunu ilan etme ve onunla ilişkiden sıyrılma anlamı taşıdığında birleşir.","sources":["TA","MU"],"what_is_ar":"يدخل فيه الكفر بمعنى البراءة والتنصل من الشيء أو بعضهم من بعض","what_is_not_ar":"ليس جحود الإيمان ولا كفران النعمة ولا تغطية الشيء حسيا"},"support_links":["sup_af17eee031fdcbe1d3e6"]},{"boundary":"Eylem kişinin kendi reddi değil, başka bir kişinin durumu hakkında adlandırma veya hüküm vermedir.","branch_kind":"bare","branch_ref":"root_001307/B006","candidate_links":[{"candidate_id":"cand_2a6a78a71a541a12c98f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"inançsız saymak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başka bir kişiyi inançsız diye niteleme veya bu yönde hüküm verme."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir başkasını dinî inancı reddeden kişi diye adlandırma veya böyle hükmetme bağlamında uygundur.","boundary_detail":"Eylem kişinin kendi reddi değil, başka bir kişinin durumu hakkında adlandırma veya hüküm vermedir.","branch_image_ar":"نسبة إلى الكفر","concept_gloss":"inançsız saymak","contextual_glosses":[{"applicability":"Resmî veya öğretisel bir hükmün vurgulandığı bağlamlarda daha açık karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin dinî durumu hakkında hüküm verme yönünü açıkça korur."},"facet_ids":["F001"],"text":"inancı reddettiğine hükmetmek","usage_role":"explanatory"}],"definition":"Bir kişiyi inançsız diye adlandırmak veya onun dinî gerçeği reddettiğine hükmetmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başka bir kişiyi inançsız diye niteleme veya bu yönde hüküm verme."}],"identity_rationale":"Kaynak ifadesi bir kişiyi inançsız diye adlandırma ve onun inancı reddettiğine hükmetme işlemlerini doğrudan verir; geçici çerçeve bu katılımcı ilişkisini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birini inançsız saymak veya öyle adlandırmak"}],"lexicalization_note":"Yalın biçimin ettirgen-hüküm verici anlamı korunur; suçlama veya zorlama gibi başka yapısal anlamlar eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hırsızlık isnadı yalnızca katılımcı yapısını açıklayan yararlı bir yakın komşu olarak yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İsnat yapısı ortaktır; ancak yüklenen içerik ve hükmün dinî niteliği bütünüyle farklıdır, bu yüzden olağan ikame mümkün değildir.","focus_only":"Bu dal bir kişinin dinî inancı reddettiğine ilişkin niteleme veya hüküm verir.","gloss":"birine nitelik yüklemek","neighbor_only":"Komşu dal bir kişiye hırsızlık eylemini yükler.","neighbor_ref":"root_000700/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda konuşan, başka bir kişiye olumsuz bir nitelik veya eylem isnat eder."}],"source_phrase_ar":"أكفرت الرجل أي دعوته كافرا لا تكفر أحدا (sihah)؛ أكفره إكفارا حكم بكفره (mufradat)","source_summary":"Kaynaklar eylemi bir kişiye inançsız nitelemesi yöneltmek veya onun hakkında bu hükmü vermek olarak açıklar.","sources":["SI","MU"],"what_is_ar":"يدخل فيه أكفر الرجل بمعنى دعاه كافرا أو حكم بكفره أو نسبه إلى الكفر","what_is_not_ar":"ليس الإلجاء إلى العصيان ولا الكفر نفسه ولا التكفير عن السيئات"},"support_links":["sup_64449116e4f17ecfc878"]},{"boundary":"Genel zorlama değildir; itaat eden kişinin zorlanarak itaatsizliğe geçirilmesi şarttır.","branch_kind":"bare","branch_ref":"root_001307/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"itaatsizliğe zorlamak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İtaat eden bir kişiyi zorlayarak itaatsizliğe geçirmek."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Başlangıçta itaat eden bir kişinin baskıyla itaatsiz davranmaya sürüklendiği bağlam için tam karşılıktır.","boundary_detail":"Genel zorlama değildir; itaat eden kişinin zorlanarak itaatsizliğe geçirilmesi şarttır.","branch_image_ar":"إلجاء إلى العصيان","concept_gloss":"itaatsizliğe zorlamak","contextual_glosses":[{"applicability":"İtaatsizliğin açık bir başkaldırı olarak gerçekleştiği anlatı bağlamlarında kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkaldırı düzeyine varmayan itaatsiz davranışları dışarıda bırakır.","preserves":"Dış baskıyla itaatten karşı koymaya geçişi korur."},"facet_ids":["F001"],"text":"başkaldırmaya mecbur bırakmak","usage_role":"contextual"}],"definition":"Başlangıçta itaat eden bir kişiyi baskı veya zorlamayla itaatsiz davranmaya mecbur bırakmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İtaat eden bir kişiyi zorlayarak itaatsizliğe geçirmek."}],"identity_rationale":"Kaynak ifadesi başlangıçta itaat eden bir kişiyi baskıyla itaatsizliğe sürükleme sürecini açıkça belirtir; geçici çerçeve başlangıç durumu, zorlama ve sonuç ayrımını korur.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"itaat eden birini itaatsizliğe zorlamak"}],"lexicalization_note":"Yalın biçim, itaat eden kişiyi itaatsizliğe zorlama anlamıyla sınırlanır; yalnızca hüküm verme anlamına veya genel baskıya genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel zorlama sınırı ve zorlamasız saptırma ayrımı dalın koşullarını en iyi açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın başlangıç ve sonuç koşulları belirgindir; komşu dalın zorlama çekirdeğinde itaatten itaatsizliğe geçiş şartı yoktur.","focus_only":"Bu dal hedefin önceden itaat etmesini ve zorlamanın onu itaatsizliğe götürmesini şart koşar.","gloss":"itaatsizliğe zorlamak","neighbor_only":"Komşu dal herhangi bir kişiyi herhangi bir şeye zorlamayı genel olarak kapsar.","neighbor_ref":"root_001343/B002","relation_type":"near_synonym","shared_zone":"Bir kişiyi istemediği bir davranışa baskıyla mecbur bırakma iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Burada belirleyici araç zorlamadır; komşu dalda ise yöneltme ve ayartma bulunabilir, mecbur bırakma zorunlu değildir.","focus_only":"Bu dal sonucu doğrudan baskı ve mecbur bırakma yoluyla oluşturur.","gloss":"itaatten saptırmak","neighbor_only":"Komşu dal ayartma, aldatma veya isteği süsleme yoluyla doğru yoldan saptırmayı da kapsar.","neighbor_ref":"root_001128/B003","relation_type":"near_neighbor","shared_zone":"Bir kişiyi önceki doğru veya itaatkâr durumundan uzaklaştırma iki dalda ortaktır."}],"source_phrase_ar":"إذا ألجأت مطيعك إلى أن يعصيك فقد أكفرته (ayn;tahdhib)","source_summary":"Kaynaklar aynı katılımcı değişimini verir: itaat eden kişi dış baskıyla itaatsiz davranmaya mecbur bırakılır.","sources":["AY","TA"],"what_is_ar":"يدخل فيه أكفرته إذا ألجأت المطيع إلى أن يعصي","what_is_not_ar":"ليس الحكم بكفر شخص ولا دعوته كافرا ولا الكفر الديني نفسه"},"support_links":[]},{"boundary":"Dal ekimin bütünü değil, tohumu toprağa koyup üstünü örtme işlemi üzerinden çiftçiyi adlandırır.","branch_kind":"bare","branch_ref":"root_001307/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"tohumu örten çiftçi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tohumu toprağa yerleştirip üzerini toprakla örten kişi."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişiyi yalnızca meslek adıyla değil, tohumu toprakla örtme gerekçesiyle birlikte anlatır.","boundary_detail":"Dal ekimin bütünü değil, tohumu toprağa koyup üstünü örtme işlemi üzerinden çiftçiyi adlandırır.","branch_image_ar":"تغطية البذر","concept_gloss":"tohumu örten çiftçi","contextual_glosses":[{"applicability":"Eylemin gerekçesi bağlamdan açıkça anlaşıldığında doğal kişi adı olarak kullanılabilir.","error_profile":{"adds":"Tohumu örtme işiyle sınırlandırılmayan bütün çiftçilik faaliyetlerini kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Toprağı işleyip ekim yapan kişi rolünü korur."},"facet_ids":["F001"],"text":"çiftçi","usage_role":"contextual"}],"definition":"Tohumu veya taneyi toprağa yerleştirip üstünü toprakla örten çiftçidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tohumu toprağa yerleştirip üzerini toprakla örten kişi."}],"identity_rationale":"Kaynak ifadesi çiftçinin tohumu veya taneyi toprakla örtme işlemini adlandırmanın gerekçesi yapar; tekil ve çoğul kişi adları aynı eyleyen rolünü taşır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"tohumu toprakla örten çiftçi"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"tohumları toprakla örten çiftçiler"}],"lexicalization_note":"Yalın kişi adları, tohumu toprakla örten çiftçi anlamında tutulur; dinî kişi nitelemesine veya genel ekim sürecine genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ekim süreci ile genel çiftçi adı, eylem ve eyleyen sınırını açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal eyleyen kişiyi örtme gerekçesiyle niteler; komşu dal ise ekim işlemi, ürün ve tarla dâhil daha geniş bir tarım sürecidir.","focus_only":"Bu dal tohumu toprakla örten kişiyi adlandırır.","gloss":"tohumu örten çiftçi","neighbor_only":"Komşu dal tohumu atma, toprağı ekime hazırlama, ekin ve ekili tarla gibi bütün ekim alanını kapsar.","neighbor_ref":"root_000303/B002","relation_type":"near_neighbor","shared_zone":"Tohumun toprağa verilmesi ve çiftçinin bu süreçteki rolü iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Gönderim örtüşse de adlandırma sınırı farklıdır: biri tohumu örtme, diğeri toprağı işleme ve meslek yönünü öne çıkarır.","focus_only":"Bu dal çiftçiyi özellikle tohumu toprakla örtmesi bakımından adlandırır.","gloss":"çiftçi","neighbor_only":"Komşu dal çiftçiyi toprağı yarıp işleyen kişi ve çiftçilik mesleğinin taşıyıcısı olarak adlandırır.","neighbor_ref":"root_001175/B003","relation_type":"near_synonym","shared_zone":"Her iki dalın gönderimi ekim yapan çiftçidir."}],"source_phrase_ar":"يقال للزارع كافر لأنه يغطى الحب بتراب الأرض (maqayis)؛ الكافر الزارع لأنه يغطي البذر بالتراب (sihah)؛ الزراع لستره البذر في الأرض (mufradat)؛ الكفار الزراع (mufradat)","source_summary":"Kaynaklar çiftçinin adlandırılmasını tohumu veya taneyi toprakla örtmesine bağlar; tekil ve çoğul biçimler aynı eyleyen rolünü gösterir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه الكافر للزارع والكفار للزراع لأنهم يغطون الحب أو البذر بالتراب","what_is_not_ar":"ليس الكافر المضاد للإيمان ولا الكافر للبحر أو الليل"},"support_links":[]},{"boundary":"Çekirdek yalnızca bağışlama değildir; günah veya bozulmuş yemin karşısında yükü gideren bir işlem ya da karşılık bulunur.","branch_kind":"mixed_non_bare","branch_ref":"root_001307/B009","candidate_links":[{"candidate_id":"cand_bee48b9068fee4761962","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"günah yükünü giderme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Günahın yükünü örten veya silen karşılık ya da işlem."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bozulan yemin için gereken yükümlülüğü yerine getirme, çekirdeğin yapıya bağlı özel türüdür."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İşlemin sonucu, kötülüğün işlenmemiş gibi değerlendirilmesi veya etkisinin silinmesidir."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem giderici işlemi hem de günahın etkisinin silinmesi sonucunu kapsayan genel karşılıktır.","boundary_detail":"Çekirdek yalnızca bağışlama değildir; günah veya bozulmuş yemin karşısında yükü gideren bir işlem ya da karşılık bulunur.","branch_image_ar":"محو الإثم بتغطيته","concept_gloss":"günah yükünü giderme","contextual_glosses":[{"applicability":"Yemin bozulduğunda doğan özel yükümlülüğün yerine getirildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yemin dışındaki günah ve kötülüklerin giderilmesini dışarıda bırakır.","preserves":"Bozulan yemin nedeniyle gereken karşılığın yerine getirilmesini korur."},"facet_ids":["F002"],"text":"bozulan yeminin gereğini yerine getirmek","usage_role":"contextual"},{"applicability":"İşlemin günahı işlenmemiş gibi kılan sonucunun öne çıktığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günahın etkisini ve yükünü ortadan kaldırma sonucunu korur."},"facet_ids":["F001","F003"],"text":"günahı silmek","usage_role":"contextual"}],"definition":"Bir günahın ya da bozulan yeminin doğurduğu yükü, gereken karşılığı veya işlemi yerine getirerek örtmek, silmek ve işlenmemiş sayılacak duruma getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Günahın yükünü örten veya silen karşılık ya da işlem."},{"facet_id":"F002","role":"specialization","statement":"Bozulan yemin için gereken yükümlülüğü yerine getirme, çekirdeğin yapıya bağlı özel türüdür."},{"facet_id":"F003","role":"extension","statement":"İşlemin sonucu, kötülüğün işlenmemiş gibi değerlendirilmesi veya etkisinin silinmesidir."}],"identity_rationale":"Kaynak ifadesi günahı veya bozulan yeminin doğurduğu yükü belirli bir karşılıkla örtme, silme ve işlenmemiş gibi kılma sürecini açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"günahı veya bozulan yeminin yükünü gideren karşılık"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bozulan yeminin gerektirdiği yükümlülüğü yerine getirme"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"günahları örtüp etkisini silme"}],"lexicalization_note":"Günah yükünü giderme çekirdeği korunur; bozulmuş yemin için gerekeni yapma yalnızca ilgili söz öbeğine bağlı özel gerçekleşmedir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bağışlama ile günahtan dönme, giderici işlem ile sonuç arasındaki sınırı en iyi açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda giderici karşılık veya yükümlülük belirleyicidir; komşu dalda belirleyici olan cezadan vazgeçme ve bağışlamadır.","focus_only":"Bu dal günah veya yemin yükünü belirli bir karşılık ya da işlemle giderir.","gloss":"günah yükünü giderme","neighbor_only":"Komşu dal hak edilmiş cezayı uygulamamayı ve suçu bağışlayarak silmeyi merkez alır.","neighbor_ref":"root_001032/B001","relation_type":"near_synonym","shared_zone":"Günahın sonucunu ortadan kaldırma ve onu silinmiş sayma iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Burada odak yükün silinmesidir; komşu dalda odak kişinin geri dönüşü ve davranışı bırakmasıdır.","focus_only":"Bu dal geçmiş eylemin yükünü gideren karşılığı veya işlemi bildirir.","gloss":"günahı giderme","neighbor_only":"Komşu dal kişinin günahtan dönmesini ve davranış yönünü değiştirmesini bildirir.","neighbor_ref":"root_000544/B003","relation_type":"near_neighbor","shared_zone":"İki dal da işlenmiş bir günahla ilişkiyi değiştiren dinî-ahlaki bir süreçtir."}],"source_phrase_ar":"الكفارة ما يكفر به من الخطيئة واليمين فيمحى به (ayn)؛ تكفير اليمين فعل ما يجب بالحنث فيها والاسم الكفارة والتكفير في المعاصي (sihah)؛ الكفارة ما يغطي الإثم والتكفير ستره وتغطيته حتى يصير بمنزلة ما لم يعمل (mufradat)","source_summary":"Kaynaklar günahın veya yeminin yükünü gideren karşılıkta birleşir; toplu anlatım hem gereken eylemi hem de günahın silinmiş sayılması sonucunu korur.","sources":["AY","SI","MU"],"what_is_ar":"يدخل فيه الكفارة لما يكفر الخطيئة أو اليمين والتكفير للسيئات والمعاصي حتى تصير كأن لم تعمل","what_is_not_ar":"ليس الكفر ضد الإيمان ولا كفران النعمة ولا ستر الأشياء الحسية"},"support_links":["sup_0c6dae45056bdd70f0cd"]},{"boundary":"Dal güzel kokulu maddeyi değil, üzüm veya hurma çiçeği ile meyveyi gelişme aşamasında örten bitkisel kılıfları kapsar.","branch_kind":"bare","branch_ref":"root_001307/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"çiçek veya meyve kılıfı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gelişen çiçek veya meyveyi dıştan örten bitkisel kılıf ya da kap."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üzüm salkımının çiçek öncesi kılıfı, hurma çiçeğinin kabı ve meyveyi örten yaprak farklı gönderimlerdir."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Üzüm ve hurma dâhil gelişen bitki bölümünü örten kap veya yaprağı genel olarak karşılar.","boundary_detail":"Dal güzel kokulu maddeyi değil, üzüm veya hurma çiçeği ile meyveyi gelişme aşamasında örten bitkisel kılıfları kapsar.","branch_image_ar":"كمام الثمر","concept_gloss":"çiçek veya meyve kılıfı","contextual_glosses":[{"applicability":"Söz hurma ağacından çıkan çiçek kabını gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Üzüm salkımı ve başka meyve örtülerini dışarıda bırakır.","preserves":"Hurma çiçeğini örten kap biçimli bitki yapısını korur."},"facet_ids":["F001","F002"],"text":"hurma çiçeğinin kılıfı","usage_role":"contextual"}],"definition":"Üzüm salkımını çiçeklenmeden önce, hurma çiçeğini ya da gelişen meyveyi örten bitkisel kılıf, kap veya yapraktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gelişen çiçek veya meyveyi dıştan örten bitkisel kılıf ya da kap."},{"facet_id":"F002","role":"source_variant","statement":"Üzüm salkımının çiçek öncesi kılıfı, hurma çiçeğinin kabı ve meyveyi örten yaprak farklı gönderimlerdir."}],"identity_rationale":"Kaynak ifadesi üzüm salkımının çiçeklenmeden önceki kılıfını, hurma çiçeğinin kabını ve meyveyi örten yaprağı aynı örtücü bitki yapıları kümesinde toplar; bunlar yalnızca olgun meyvenin tek tip kabuğu değildir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"üzüm salkımının veya hurma çiçeğinin kılıfı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"hurma çiçeğinin ya da meyvenin kılıfı"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"hurma ağacından çıkan kapalı çiçek kılıfları"}],"lexicalization_note":"Yalın ad biçimleri bitkisel kılıf ve kap anlamında tutulur; güzel kokulu madde, su kaynağı veya bitki anlamları bu dala alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tahıl tanesi örtüsü ve ekinin kılıfa girme durumu, nesne ve gelişim aşaması sınırlarını açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtülen bölüm ve yapı ölçeği farklıdır: bu dal salkım, çiçek veya meyve kabıdır; komşu dal tanenin başak içindeki ince örtüsüdür.","focus_only":"Bu dal üzüm salkımı, hurma çiçeği veya meyvenin dış kılıfını kapsar.","gloss":"bitkisel kılıf","neighbor_only":"Komşu dal yalnızca başaktaki tek bir tahıl tanesinin ince örtüsünü kapsar.","neighbor_ref":"root_000384/B008","relation_type":"near_neighbor","shared_zone":"Bir bitki üreme yapısını dıştan örten doğal kılıf iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Bu dal nesne adıdır; komşu dal ürünün kılıf içine girme aşamasını ve durumunu merkez alır.","focus_only":"Bu dal örtücü kılıfın kendisini adlandırır.","gloss":"ürün kılıfı","neighbor_only":"Komşu dal ekinin kendi kılıfına girip korunmuş duruma gelmesini anlatır.","neighbor_ref":"root_001019/B010","relation_type":"near_neighbor","shared_zone":"Gelişen bitki ürününün doğal bir kılıf içinde korunması iki dalda ortaktır."}],"source_phrase_ar":"الكافور كم العنب قبل أن ينور وسمى كافورا لأنه كفر الوليع أي غطاه (maqayis)؛ الكافور كم العنب قبل أن ينور وكافوره ورقة الذي يستره والكافور الطلع والكفرى والكوافير (ayn)؛ الكافور الطلع ووعاء طلع النخل وكذلك الكفرى (sihah)؛ الكافور اسم أكمام الثمرة التي تكفرها والكافور أكمام الثمرة (mufradat)","source_summary":"Kaynaklar çiçek veya meyveyi örten bitkisel kapta birleşir; üzüm salkımı, hurma çiçeği ve meyve yaprağı bu üst kavramın farklı gönderimleridir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الكافور والكفرى والكوافير لأكمام العنب أو طلع النخل أو الورقة التي تستر الثمرة","what_is_not_ar":"ليس الكافور الطيب ولا عين الماء ولا النبات ولا الكفر الديني"},"support_links":[]},{"boundary":"Üç gönderim birbirinin örneği değildir; dal yalnızca kaynakta aynı ad altında toplanan bu ayrı sözlük anlamlarını korur.","branch_kind":"bare","branch_ref":"root_001307/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"koku maddesi, su kaynağı veya bitki","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güzel kokulu karışımlarda kullanılan bir madde."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Cennette bulunduğu belirtilen bir su kaynağı."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çiçeği papatya çiçeğine benzeyen bir bitki."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Birbirinden ayrı üç sözlük gönderimini yapay bir ortak nesne türüne indirgemeden birlikte gösterir.","boundary_detail":"Üç gönderim birbirinin örneği değildir; dal yalnızca kaynakta aynı ad altında toplanan bu ayrı sözlük anlamlarını korur.","branch_image_ar":"كافور طيب","concept_gloss":"koku maddesi, su kaynağı veya bitki","contextual_glosses":[{"applicability":"Sözün güzel koku hazırlamada kullanılan maddeyi gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Su kaynağı ve çiçekli bitki gönderimlerini dışarıda bırakır.","preserves":"Güzel kokulu karışımlarda kullanılan madde gönderimini korur."},"facet_ids":["F001"],"text":"güzel kokulu karışım maddesi","usage_role":"contextual"}],"definition":"Aynı sözle adlandırılan üç ayrı gönderimden oluşan bir sözlük kümesidir: güzel kokulu bir karışım maddesi, cennette bulunduğu belirtilen bir su kaynağı ve çiçeği papatyaya benzeyen bir bitki.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güzel kokulu karışımlarda kullanılan bir madde."},{"facet_id":"F002","role":"source_variant","statement":"Cennette bulunduğu belirtilen bir su kaynağı."},{"facet_id":"F003","role":"source_variant","statement":"Çiçeği papatya çiçeğine benzeyen bir bitki."}],"identity_rationale":"Kaynak ifadesi tek bir kavramsal tür vermek yerine aynı sözle anılan üç ayrı gönderimi sıralar: güzel kokulu bir madde, cennetteki bir su kaynağı ve çiçeği papatyaya benzeyen bir bitki. Tanım bu nedenle birleşik bir nesne sınıfı kurmadan sözlüksel çokanlamlılık kümesi olarak düzenlenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"güzel kokulu karışımlarda kullanılan madde"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"cennetteki bir su kaynağı"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"çiçeği papatyaya benzeyen bir bitki"}],"lexicalization_note":"Yalın biçimin üç ayrı gönderimi birbirine karıştırılmadan verilir; meyve ve çiçek kılıfı anlamı bu dala aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca güzel kokulu bitki ve madde adayı bir facet için yararlı alan karşılaştırması sağladı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortak alan yalnızca koku maddesi yönüdür; gönderimler ve bu dalın öteki iki sözlük anlamı farklı olduğu için ikame edilemezler.","focus_only":"Bu dalın güzel kokulu madde yanında su kaynağı ve ayrı bir bitki gönderimi de vardır.","gloss":"güzel kokulu madde","neighbor_only":"Komşu dal güzel kokulu kökü olan belirli bitkileri ve onlardan elde edilen kokuyu adlandırır.","neighbor_ref":"root_000707/B006","relation_type":"same_field","shared_zone":"İki dal güzel koku veren bitkisel madde alanında buluşur."}],"source_phrase_ar":"الكافور شيء من أخلاط الطيب والكافور عين ماء في الجنة والكافور نبات نوره كنور الأقحوان (ayn)؛ الكافور من الطيب (sihah)؛ الكافور الذي هو من الطيب (mufradat)","source_summary":"Toplu kaynak kanıtı güzel kokulu madde anlamını ortaklaştırır; aynı aggregate aktarım ayrıca su kaynağı ve papatyaya benzer çiçekli bitki anlamlarını ayrı gönderimler olarak kaydeder.","sources":["AY","SI","MU"],"what_is_ar":"يدخل فيه الكافور من الطيب وعين ماء في الجنة والنبات المسمى كافورا","what_is_not_ar":"ليس أكمام الثمر ولا الطلع ولا الكفر الديني"},"support_links":[]},{"boundary":"Uzak arazi çekirdeği ile köy, halk ve mezar kullanımları ayrı facetlerdir; dağ geçidi bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001307/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"uzak arazi; köy, uzak yer halkı veya mezar","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanlardan uzak, pek uğranmayan veya geçilmeyen arazi."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Köy, köyler ve uzak yerlerin halkı aynı söz ailesinin ayrı yer ve topluluk kullanımlarıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Mezar anlamı tek kaynaklı aktarım içinde verilen ayrı bir sözlük kullanımıdır."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ana uzak arazi anlamını öne alır ve kaynakta aynı dalda tutulan ayrı yer kullanımlarını açıkça işaretler.","boundary_detail":"Uzak arazi çekirdeği ile köy, halk ve mezar kullanımları ayrı facetlerdir; dağ geçidi bu dala girmez.","branch_image_ar":"موضع منقطع","concept_gloss":"uzak arazi; köy, uzak yer halkı veya mezar","contextual_glosses":[{"applicability":"Söz öbeğinin pek uğranmayan uzak araziyi gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Köy, halk ve mezar kullanımlarını dışarıda bırakır.","preserves":"Uzaklık ve insan uğrağından yoksunluk özelliklerini korur."},"facet_ids":["F001"],"text":"insanlardan uzak ıssız yer","usage_role":"contextual"}],"definition":"İnsanlardan uzak, pek inilmez ve geçilmez bir araziyi anlatır. Aynı söz ailesinde köy, köyler veya bu yerlerin halkı ve mezar için kaydedilmiş ayrı kullanımlar da bulunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanlardan uzak, pek uğranmayan veya geçilmeyen arazi."},{"facet_id":"F002","role":"source_variant","statement":"Köy, köyler ve uzak yerlerin halkı aynı söz ailesinin ayrı yer ve topluluk kullanımlarıdır."},{"facet_id":"F003","role":"source_variant","statement":"Mezar anlamı tek kaynaklı aktarım içinde verilen ayrı bir sözlük kullanımıdır."}],"identity_rationale":"Kaynak ifadesi insanlardan uzak araziyi temel gönderim olarak verir; köy, köyler, bu yerlerin halkı ve mezar anlamları ise aynı söz ailesinin ayrı sözlük kullanımlarıdır. Tanım bunları tek bir 'ıssız yer' nesnesi gibi özdeşleştirmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"insanlardan uzak, pek uğranmayan arazi"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"köy veya mezar"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"köyler veya uzak yerlerin halkı"}],"lexicalization_note":"Uzak araziye bağlı söz öbeği ile yalın köy, mezar ve çoğul yer-halk kullanımları ayrı tutulur; kapsamları tek anlamda eritilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yer kavramı ile fiziksel kopuk yer, uzaklık koşulunun sınırını açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli sözlük gönderimlerine ve uzaklık koşuluna bağlıdır; komşu dalın çekirdeği genel yer kavramıdır.","focus_only":"Bu dal insanlardan uzak araziyi öne çıkarır ve köy ile mezarı ayrı sözlük kullanımları olarak taşır.","gloss":"uzak arazi veya yer","neighbor_only":"Komşu dal her türlü sınırlı yeri; mamur, boş, yerleşik veya ıssız oluşuna bakmadan genel olarak kapsar.","neighbor_ref":"root_000148/B001","relation_type":"near_neighbor","shared_zone":"Arazi, köy ve mezar gibi yer gönderimleri iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Bu dalda uzaklık insanlarla ilişkilidir; komşu dalda fiziksel kopukluk ve ada yapısı belirleyicidir.","focus_only":"Bu dalın ana yeri insanlardan uzak arazidir; ayrıca köy ve mezar kullanımları vardır.","gloss":"uzak veya kopuk yer","neighbor_only":"Komşu dal belirli bir yer adı yanında deniz içindeki veya karadan kopuk adayı anlatır.","neighbor_ref":"root_000123/B005","relation_type":"near_neighbor","shared_zone":"İnsan yerleşiminden ya da ana karadan ayrılık düşüncesi iki dalı yakınlaştırır."}],"source_phrase_ar":"الكفر من الأرض ما بعد من الناس وأهل الكفور والقرى (maqayis)؛ الكافر من الأرض ما بعد عن الناس والكفور القرى (ayn)؛ الكفر أيضا القرية والكفر أيضا القبر (sihah)؛ الكافر من الأرض ما بعد عن الناس (tahdhib)","source_summary":"Kaynaklar insanlardan uzak arazi anlamında birleşir; toplu kanıt ayrıca köy, köylerin halkı ve mezar anlamlarını ortak çekirdekten ayrılması gereken sözlük kullanımları olarak taşır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الكافر من الأرض البعيد عن الناس والكفور للقرى والكفر للقرية والقبر","what_is_not_ar":"ليس الثنايا من الجبال ولا البحر ولا الليل ولا الزرع"},"support_links":[]},{"boundary":"Dağ geçidi ve iri dağ coğrafi facetlerdir; alçak duvar ayrı bir sözlük varyantıdır, köy veya uzak arazi değildir.","branch_kind":"bare","branch_ref":"root_001307/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"dağ geçidi; iri dağ veya alçak duvar","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dağlar arasındaki geçit veya geçitler."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İri bir dağ, coğrafi alan içindeki ayrı bir kaynak varyantıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Alçak duvar, coğrafi çekirdekten ayrı bir sözlük kullanımıdır."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dağ geçidi çekirdeğini öne alırken aynı dalda korunan iki ayrı sözlük varyantını da eksiltmeden gösterir.","boundary_detail":"Dağ geçidi ve iri dağ coğrafi facetlerdir; alçak duvar ayrı bir sözlük varyantıdır, köy veya uzak arazi değildir.","branch_image_ar":"ثنية مستورة","concept_gloss":"dağ geçidi; iri dağ veya alçak duvar","contextual_glosses":[{"applicability":"Çoğul veya tekil biçimin dağlar arasındaki geçidi gösterdiği coğrafi bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İri dağ ve alçak duvar varyantlarını dışarıda bırakır.","preserves":"Dağlık arazideki geçit gönderimini doğal biçimde korur."},"facet_ids":["F001"],"text":"dağ geçidi","usage_role":"contextual"}],"definition":"Dağlar arasındaki geçitler veya iri bir dağ için kullanılan coğrafi bir adlandırmadır; aynı söz ailesinde alçak duvar anlamı da ayrı bir sözlük kullanımı olarak kaydedilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dağlar arasındaki geçit veya geçitler."},{"facet_id":"F002","role":"source_variant","statement":"İri bir dağ, coğrafi alan içindeki ayrı bir kaynak varyantıdır."},{"facet_id":"F003","role":"source_variant","statement":"Alçak duvar, coğrafi çekirdekten ayrı bir sözlük kullanımıdır."}],"identity_rationale":"Kaynak ifadesi dağ geçitlerini, iri bir dağı ve alçak duvarı aynı söz ailesinde sıralar; geçitleri 'örtülü' saymak kaynakta kurucu bir koşul değildir. Dal bu nedenle örtülülük altında birleştirilmeden coğrafi çekirdek ve ayrı duvar kullanımı olarak düzenlenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"dağ geçitleri"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"dağ geçidi veya iri dağ"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"alçak duvar"}],"lexicalization_note":"Yalın biçimlerin dağ geçidi, iri dağ ve alçak duvar gönderimleri ayrı tutulur; uzak yer veya genel örtme anlamı eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel dağ geçidi ile sarp dağ yolu, geçit türünün ve zorluk koşulunun sınırını açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Geçit gönderiminde yakınlık yüksektir; ancak komşu dal yolun kıvrım ve güzergâh yapısını, bu dal ise ayrı dağ ve duvar varyantlarını da içerir.","focus_only":"Bu dal dağ geçidi yanında iri dağ ve alçak duvar varyantlarını da taşır.","gloss":"dağ geçidi","neighbor_only":"Komşu dal geçidi özellikle dağ veya vadideki yol kıvrımı ve yürünür güzergâh olarak tanımlar.","neighbor_ref":"root_000208/B006","relation_type":"near_synonym","shared_zone":"Dağlık arazideki geçit iki dalın ortak gönderimidir."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeğinde sarplık veya tırmanış şartı yoktur; komşu dalda güç çıkılan yükselen yol belirleyicidir.","focus_only":"Bu dal geçidin yalnızca dağlık yer türünü adlandırır ve zorluk koşulu taşımaz.","gloss":"dağ geçidi","neighbor_only":"Komşu dal dik, engebeli ve çıkılması güç bir dağ yolunu veya benzer yükseltileri merkez alır.","neighbor_ref":"root_001033/B012","relation_type":"near_neighbor","shared_zone":"Dağlık arazide geçiş sağlayan yer iki dalda da bulunabilir."}],"source_phrase_ar":"الكفرات والكفر الثنايا من الجبال (maqayis)؛ الكفر الثنايا من الجبال (ayn)؛ الكفر العظيم من الجبال (sihah)؛ الكافر الحائط الواطىء (tahdhib)","source_summary":"Kaynakların çoğu dağ geçitlerini verir; toplu kanıt iri dağ ve alçak duvar anlamlarını da aynı söz ailesinin ayrı varyantları olarak kaydeder.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الكفرات والثنايا من الجبال والكفر العظيم من الجبال والحائط الواطئ","what_is_not_ar":"ليس القرية ولا القبر ولا الأرض البعيدة العامة"},"support_links":[]},{"boundary":"Dal genel içsel alçakgönüllülük değil, baş veya el ve gövdeyle yapılan belirli bir boyun eğme gösterisidir.","branch_kind":"bare","branch_ref":"root_001307/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"eğilerek boyun eğme gösterisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedeni alçaltan bir hareketle başka birine boyun eğme gösterisi yapma."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koruma altındaki gayrimüslim tebaanın başıyla işaret etmesi veya bir kişinin elini göğsüne koyup eğilmesi, bu gösterinin belirtilen bedensel biçimleridir."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İçsel tutumdan çok baş, el ve gövdeyle yapılan belirli gösteriyi anlatır.","boundary_detail":"Dal genel içsel alçakgönüllülük değil, baş veya el ve gövdeyle yapılan belirli bir boyun eğme gösterisidir.","branch_image_ar":"خضوع متطامن","concept_gloss":"eğilerek boyun eğme gösterisi","contextual_glosses":[{"applicability":"Koruma altındaki gayrimüslim tebaanın başıyla boyun eğme işareti yaptığı tarihî bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Elin göğse konduğu ve bütün bedenin alçaldığı biçimi dışarıda bırakır.","preserves":"Koruma altındaki gayrimüslim tebaanın başıyla yaptığı boyun eğme işaretini korur."},"facet_ids":["F001","F002"],"text":"koruma altındaki gayrimüslim tebaanın başıyla boyun eğmesi","usage_role":"contextual"}],"definition":"Koruma altındaki gayrimüslim tebaanın başıyla işaret etmesi veya bir kişinin elini göğsüne koyup bedenini alçaltması yoluyla başka birine boyun eğdiğini göstermesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedeni alçaltan bir hareketle başka birine boyun eğme gösterisi yapma."},{"facet_id":"F002","role":"example","statement":"Koruma altındaki gayrimüslim tebaanın başıyla işaret etmesi veya bir kişinin elini göğsüne koyup eğilmesi, bu gösterinin belirtilen bedensel biçimleridir."}],"identity_rationale":"Kaynak ifadesi başla işaret etme ile eli göğse koyup bedenini alçaltmayı, başka birine boyun eğme gösterisinin iki bedensel gerçekleşmesi olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"başını eğmek veya elini göğsüne koyup eğilmek"}],"lexicalization_note":"Yalın eylem adı belirli bedensel boyun eğme hareketleriyle sınırlanır; günah giderme veya kişiyi inançsız sayma anlamı eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel alçakgönüllülük ve yere kapanma, bu dalın belirli beden hareketi sınırını açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli törensel beden hareketidir; komşu dal daha geniş bir içsel ve dışsal alçakgönüllülük alanıdır.","focus_only":"Bu dal başla işaret veya eli göğse koyup eğilme gibi belirli bir kişiye yönelmiş hareketleri şart koşar.","gloss":"eğilerek boyun eğmek","neighbor_only":"Komşu dal içsel alçalışı, ses ve bakışın sakinleşmesini, ibadet duruşunu ve genel gönüllü boyun eğmeyi de kapsar.","neighbor_ref":"root_000412/B001","relation_type":"near_synonym","shared_zone":"Başın ve bedenin alçaltılmasıyla boyun eğme iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Hareketin biçimi farklıdır: bu dal ayakta yapılan eğilme işaretlerini, komşu dal yere kapanmaya kadar uzanan secdeyi kapsar.","focus_only":"Bu dalda alnı yere koymak şart değildir; baş işareti veya göğüste elle eğilme yeterlidir.","gloss":"bedensel boyun eğme","neighbor_only":"Komşu dal alnı yere koymayı ve secde biçimindeki boyun eğmeyi de çekirdeğe alır.","neighbor_ref":"root_000675/B001","relation_type":"near_neighbor","shared_zone":"Bedeni alçaltarak itaat ve saygı gösterme iki dalda ortaktır."}],"source_phrase_ar":"التكفير إيماء الذمي برأسه لا يقال سجد له وإنما يقال كفر له (ayn)؛ التكفير أن يخضع الإنسان لغيره يضع يده على صدره ويتطامن له (sihah)","source_summary":"Kaynaklar başka birine bedensel olarak boyun eğme çekirdeğinde birleşir; başla işaret ve eli göğse koyarak eğilme iki farklı hareket biçimidir.","sources":["AY","SI"],"what_is_ar":"يدخل فيه التكفير بمعنى إيماء الذمي برأسه أو وضع اليد على الصدر والتطامن خضوعا","what_is_not_ar":"ليس تكفير اليمين ولا التكفير عن السيئات ولا نسبة الشخص إلى الكفر"},"support_links":[]},{"boundary":"Dal hükümdarlık tacı ve taç giydirme töreniyle sınırlıdır; genel baş örtüsü veya boyun eğme hareketi değildir.","branch_kind":"bare","branch_ref":"root_001307/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","surface_ar":"كَفَرَ"}],"gloss":"hükümdara taç giydirme veya taç","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hükümdarın başına taç koyarak onu taçlandırma işlemi."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Taçlandırma işleminde kullanılan tacın kendisi için aktarılan nesne anlamı."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Süreç ile nesne gönderimini birbirine indirgemeden aynı sözlük alanında birlikte korur.","boundary_detail":"Dal hükümdarlık tacı ve taç giydirme töreniyle sınırlıdır; genel baş örtüsü veya boyun eğme hareketi değildir.","branch_image_ar":"تاج يغطي","concept_gloss":"hükümdara taç giydirme veya taç","contextual_glosses":[{"applicability":"Sözün törensel işlemi bildirdiği eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tacın kendisini adlandıran nesne gönderimini dışarıda bırakır.","preserves":"Hükümdarın başına taç koyma işlemini korur."},"facet_ids":["F001"],"text":"hükümdara taç giydirmek","usage_role":"contextual"}],"definition":"Bir hükümdarın başına taç koyarak onu taçlandırma işlemidir; aynı söz bu işlemde kullanılan tacın kendisini de adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hükümdarın başına taç koyarak onu taçlandırma işlemi."},{"facet_id":"F002","role":"source_variant","statement":"Taçlandırma işleminde kullanılan tacın kendisi için aktarılan nesne anlamı."}],"identity_rationale":"Kaynak ifadesi hem hükümdara taç giydirme işlemini hem de bu işlemde kullanılan tacın kendisini açıkça verir; ancak geçici dal imgesindeki tacın örttüğü düşüncesi bir kaynak iddiası değildir. Süreç ve nesne ayrımı korunarak aynı dalda gösterilebilir.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"hükümdara taç giydirme veya tacın kendisi"}],"lexicalization_note":"Yalın eylem adının taç giydirme süreci ve taç nesnesi gönderimleri birlikte fakat ayrı facetlerde korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; egemenlik için baş bağlama ve genel baş süsü dalları, taçlandırmanın işlevsel sınırını açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal taç ve hükümdarla sınırlıdır; komşu dal sarık, başa geçirme ve topluluğun kişiyi önder sayması gibi daha geniş süreçleri de içerir.","focus_only":"Bu dal özellikle hükümdara taç giydirme işlemini ve tacın kendisini adlandırır.","gloss":"taçlandırma","neighbor_only":"Komşu dal taç yanında sarık bağlamayı, kişiyi başa geçirmeyi ve egemenlik işaretini daha geniş biçimde kapsar.","neighbor_ref":"root_001018/B008","relation_type":"near_neighbor","shared_zone":"Baş üzerine taç koyma ve bunu egemenlik işareti yapma iki dalda ortaktır."},{"boundary_match":"field_only","distinction":"Bu dal hükümdarlık ve taçlandırma işlevine bağlıdır; komşu dalın çekirdeği başa konan nesnelerin genel sınıfıdır.","focus_only":"Bu dal taç giydirme eylemini ve hükümdarlık tacını bildirir.","gloss":"başa konan taç","neighbor_only":"Komşu dal başa süs veya örtü olarak konan sarık, başlık, taç ve bitki gibi nesneleri genel olarak kapsar.","neighbor_ref":"root_001044/B005","relation_type":"same_field","shared_zone":"Taç, başın üstüne konan bir nesne olarak iki dalın ortak alanıdır."}],"source_phrase_ar":"التكفير تتويج الملك بتاج والتكفير ههنا التاج نفسه (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Söz hem hükümdara taç giydirme işlemi hem de bu işlemde kullanılan tacın adı olarak aktarılır."}],"source_summary":"Tek kaynaklı kanıt, hükümdarı taçlandırma süreci ile bu süreçte kullanılan taç nesnesini aynı sözün iki bağlı gönderimi olarak kaydeder.","sources":["AY"],"what_is_ar":"يدخل فيه التكفير بمعنى تتويج الملك بتاج أو التاج نفسه","what_is_not_ar":"ليس الخضوع ولا الكفارة ولا الكفر الديني"},"support_links":[]},{"boundary":"Dal, zamansal sıralanma veya yönetim anlamını değil, yakınlık ve bitişiklik sınırını taşır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"aralıksız yakınlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Arada ayırıcı unsur olmadan yakın, bitişik veya yanında olma."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin başka bir şeye bitişik ya da hemen yakın olduğunu anlatan genel çekirdek için uygundur.","boundary_detail":"Dal, zamansal sıralanma veya yönetim anlamını değil, yakınlık ve bitişiklik sınırını taşır.","concept_gloss":"aralıksız yakınlık","contextual_glosses":[{"applicability":"Bir kişinin hemen yanında veya yakınında bulunan şeyi doğal Türkçe bağlamda karşılar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yanındalık ve yakın bulunma değerini korur."},"facet_ids":["F001"],"text":"yanında bulunan","usage_role":"contextual"},{"applicability":"Ev veya yer örneklerinde arada mesafe bırakmayan komşuluğu verir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bitişiklik ve yakın komşuluk sınırını korur."},"facet_ids":["F001"],"text":"bitişik komşu","usage_role":"contextual"}],"definition":"Bir şeyin başka bir şeye araya yabancı bir unsur girmeden yakın, bitişik veya yanında olmasıdır. Bu yakınlık yer bakımından olabileceği gibi ilişki bakımından da kurulabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Arada ayırıcı unsur olmadan yakın, bitişik veya yanında olma."}],"identity_rationale":"Kaynak ifadesi, dalın temelini arada yabancı bir unsur bulunmadan yakın olma, bitişik durma veya yanında bulunma olarak verir. Yer, ilişki ve bir evin başka bir eve bitişik olması gibi kullanımlar bu aynı yakınlık çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yakınlık ve bitişiklik"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sana yakın veya yanında olan şey"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir eve bitişik olan ev"}],"lexicalization_note":"Çıplak yakınlık değeri ile kalıp içindeki ev veya yanındalık kullanımları ayrılarak korunur.","neighbor_coverage_note":"Tüm aday komşular yakınlık, yanındalık veya aynı kökün diğer dalları bakımından değerlendirildi; yalnız sınırı gerçekten keskinleştirenler yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda yakınlık çoğu kez şeyin hemen yanında veya onu izleyen konumda bulunmasıyla sınırlanır; komşu dal daha genel yakınlaşma ve yaklaştırma eylemlerine de açıktır.","focus_only":"Arada yabancı bir unsur bulunmaması ve bitişik yanındalık daha belirgindir.","gloss":"yakınlık","neighbor_only":"Genel yaklaşma, yakınlaştırma ve iki şey arasında yakınlık kurma alanı daha geniştir.","neighbor_ref":"root_000493/B001","relation_type":"near_synonym","shared_zone":"İki dal da yakın olma ve mesafenin azlığı alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği bitişik yakınlıktır; B002 aynı kesintisizlik fikrini zamansal veya eylemsel sıra halinde gerçekleşen öğelere uygular.","focus_only":"Yakınlık yer veya ilişki bakımından yan yana durma olarak kurulur.","gloss":"yakınlık ile ardışıklık","neighbor_only":"Ardışıklıkta bir şeyin başka bir şeyden sonra gelmesi ve sıra düzeni öne çıkar.","neighbor_ref":"root_001684/B002","relation_type":"near_neighbor","shared_zone":"İkisinde de araya yabancı bir unsur girmemesi önemlidir."}],"source_summary":"Kaynakların ortak anlatımı, bu dalı yakınlık ve bitişiklik çekirdeği etrafında toplar; kişinin yanındaki şey ve birbirine komşu ev örnekleri bu çekirdeğin uygulamalarıdır."},"support_links":[]},{"boundary":"Dal, mekansal yakınlık veya dostça destek anlamına genişletilmeden ardışık gerçekleşme ile sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B002","candidate_links":[{"candidate_id":"cand_35a71a2826af60921ef3","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"kesintisiz ardışıklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Şeylerin veya eylemlerin kesintisiz biçimde peş peşe gerçekleşmesi."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Peş peşe gelen şeyler, eylemler veya dönemler için dalın bütün çekirdeğini verir.","boundary_detail":"Dal, mekansal yakınlık veya dostça destek anlamına genişletilmeden ardışık gerçekleşme ile sınırlıdır.","concept_gloss":"kesintisiz ardışıklık","contextual_glosses":[{"applicability":"Atış, iş veya haberlerin ardı ardına geldiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sıra ve kesintisiz takip anlamını korur."},"facet_ids":["F001"],"text":"peş peşe","usage_role":"contextual"},{"applicability":"İki iş veya iki nesne arasında ardışık düzen kuran eylem bağlamına uyar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemler arasında sıra kurma değerini korur."},"facet_ids":["F001"],"text":"art arda yapmak","usage_role":"contextual"}],"definition":"İki veya daha çok şeyin ya da eylemin araya ilgisiz bir kesinti girmeden peş peşe gerçekleşmesidir. Düzen, art arda geliş ve süreklilik çekirdeği birlikte korunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Şeylerin veya eylemlerin kesintisiz biçimde peş peşe gerçekleşmesi."}],"identity_rationale":"Kaynak ifadesi, iki veya daha çok şeyin araya başka bir şey girmeden biri diğerinin ardından gelmesini anlatır. Atış, iş, ay ve yazıların peş peşe gelişi örnekleri bu sıra ve kesintisizlik çekirdeğini doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kesintisiz sıra"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"araya kesinti girmeden peş peşe oluş"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"şeyleri veya işleri peş peşe getirme"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"iki şeyi peş peşe getirmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"peş peşe isabet eden üç ok"}],"lexicalization_note":"Çıplak sıralanma değeri ile iki şey arasında kurulan veya örneklerdeki kalıplı kullanım ayrı tutulur.","neighbor_coverage_note":"Adaylar ardışıklık, takip ve aynı kökün yakın dalları açısından denetlendi; örnek tekrarı yapan adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal, aynı kökün yakınlık fikrinden gelen aralıksız sıra değerini taşır; komşu dal daha genel takip ve düzenli akış alanını kapsar.","focus_only":"Araya aynı diziden olmayan bir unsur girmemesi özellikle vurgulanır.","gloss":"kesintisiz takip","neighbor_only":"Okuma, konuşma veya ayların akışı gibi süreklilik örnekleri daha geniştir.","neighbor_ref":"root_000695/B001","relation_type":"near_synonym","shared_zone":"İki dal da şeylerin biri diğerinin ardından gelmesine dayanır."},{"boundary_match":"field_only","distinction":"B002 nesne ya da eylemlerin sıra halinde gelişiyle ilgilidir; B004 kişiler veya topluluklar arasında destekleyici bağlılık kurar.","focus_only":"Peş peşe gerçekleşme ve düzen anlamı vardır.","gloss":"sıra ile destek","neighbor_only":"Dostça yakınlık, sevgi, destek ve karşıtlığa karşı taraf tutma anlamı vardır.","neighbor_ref":"root_001684/B004","relation_type":"same_field","shared_zone":"İkisi de yakınlık veya bağ kurma alanında aynı kökten ayrılır."}],"source_summary":"Kaynakların ortak anlatımı, dalı şeyin şeyden sonra gelmesi, işlerin düzenli biçimde sıralanması ve araya yabancı bir kesinti girmemesi etrafında birleştirir."},"support_links":["sup_b35576db6122b0333bd2"]},{"boundary":"Dal, yalnız sevgi ve yardım anlamı değil, bir işin başına geçip onu yürütme anlamıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"bir işi üstlenip yönetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işi veya başkasının durumunu üstlenip yönetme ve yürütme."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yönetim, görev alma ve başkasının işini yürütme bağlamlarının hepsine uygulanabilir.","boundary_detail":"Dal, yalnız sevgi ve yardım anlamı değil, bir işin başına geçip onu yürütme anlamıdır.","concept_gloss":"bir işi üstlenip yönetme","contextual_glosses":[{"applicability":"Bir yer, iş veya görevin başına geçme bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başına geçme ve yürütme değerini korur."},"facet_ids":["F001"],"text":"yönetimini üstlenmek","usage_role":"contextual"},{"applicability":"Yetim, kadın veya başka bir kişinin işini gözetme bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sorumluluk ve gözetim değerini korur."},"facet_ids":["F001"],"text":"işlerine bakmak","usage_role":"contextual"}],"definition":"Bir işin, yerin veya başkasına ait durumun sorumluluğunu üstlenip onu yönetmek ve yürütmektir. Bu, resmi yönetimden bakım ve gözetim sorumluluğuna kadar uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işi veya başkasının durumunu üstlenip yönetme ve yürütme."}],"identity_rationale":"Kaynak ifadesi, bir işin, yerin veya kişinin işlerinin sorumluluğunu üstlenip yürütmeyi açıkça verir. Yönetim, yetki, görev üstlenme ve yetim ya da kadınla ilgili sorumluluk örnekleri aynı idare etme çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yönetim ve yetki alanı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir yeri veya işi yöneten kişi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"başkasının işlerinden sorumlu kişi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bir işi üstlenmek"}],"lexicalization_note":"Yönetim adı, görevli kişi ve işi üstlenme kalıbı aynı dalda ama kapsamları ayrılarak tutulur.","neighbor_coverage_note":"Yönetim, yetki, yardım ve aynı kökün ilişki dalları karşılaştırıldı; yalnız gerçek kapsam ayrımı veren komşular seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal görev üstlenme ve gözetimi birlikte içerir; komşu dal daha çok emir ve resmi yönetici konumunu öne çıkarır.","focus_only":"Gözetim ve başkasının işlerini yürütme gibi resmi olmayan sorumlulukları da kapsar.","gloss":"yönetim yetkisi","neighbor_only":"Buyruk sahibi yönetici ve resmen yönetici kılma alanı daha baskındır.","neighbor_ref":"root_000051/B003","relation_type":"near_synonym","shared_zone":"İki dal da yönetim ve işlerin başında bulunma alanında örtüşür."},{"boundary_match":"field_only","distinction":"B003 sorumluluk ve idare çekirdeğindedir; B004 birini sevmek, desteklemek veya onun yanında yer almakla sınırlıdır.","focus_only":"İşin başına geçme ve onu yürütme vardır.","gloss":"yönetim ile destek","neighbor_only":"Sevgi, dostluk ve yardım ederek taraf olma vardır.","neighbor_ref":"root_001684/B004","relation_type":"same_field","shared_zone":"İkisi de insanlar arası bağlılık ve yakın ilişki alanına dokunur."}],"source_summary":"Kaynakların ortak anlatımı, bu dalı yönetme, sorumluluk alma, bir yerin veya işin başına geçme ve korunmaya muhtaç kişinin işini yürütme alanında toplar."},"support_links":[]},{"boundary":"Dal, resmi yönetim veya özgür bırakmaya bağlı hukuki bağ anlamına indirgenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"yakın durup destek olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sevgi, dostluk, inanç veya yardım bağıyla birinin yanında yer alma."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sevgi, dostluk, inanç veya yardım bağıyla bir tarafı tutma bağlamlarında uygundur.","boundary_detail":"Dal, resmi yönetim veya özgür bırakmaya bağlı hukuki bağ anlamına indirgenmez.","concept_gloss":"yakın durup destek olma","contextual_glosses":[{"applicability":"Kişi veya topluluk için düşmanın karşıtı olan yakın destekçi bağlamına uyar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dostluk ve destek değerini korur."},"facet_ids":["F001"],"text":"dost ve destekçi","usage_role":"contextual"},{"applicability":"Birini sevme, kayırma veya yardım ederek destekleme eyleminde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taraf olma ve destekleme anlamını korur."},"facet_ids":["F001"],"text":"yanında yer almak","usage_role":"contextual"}],"definition":"Bir kişi veya topluluğa sevgi, dostluk, inanç ya da yardım bağıyla yakın durup onun yanında yer almaktır. Karşıtlık ekseninde düşmanın değil desteklenen tarafın yanında olma anlamı taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sevgi, dostluk, inanç veya yardım bağıyla birinin yanında yer alma."}],"identity_rationale":"Kaynak ifadesi, düşmanın karşıtı olan yakın tarafı, sevgi, destek, dostluk, inanç veya anlaşma bağıyla yanında olmayı birlikte verir. Bu dalda yakınlık, yönetim değil, taraf tutan ve yardım eden ilişki olarak işler.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"dost, seven veya destekleyen kişi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"destekçi, anlaşmalı dost veya yakın yoldaş"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"birini sevip destekleme veya kayırma"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birini sevmek, desteklemek veya kayırmak"}],"lexicalization_note":"Kişi adı, destek ilişkisi ve birini destekleme kalıbı karıştırılmadan aynı ilişki alanında açıklanır.","neighbor_coverage_note":"Sevgi, dostluk, destek ve akrabalık adayları karşılaştırıldı; yalnız okuyucunun karıştırabileceği sınırlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal sevgi bağını destek ve taraf olma ile birlikte kurar; komşu dal daha çok dostluğun içtenlik yönünü anlatır.","focus_only":"Sevgiyle birlikte yardım, taraf tutma ve düşmanın karşıtı olma vardır.","gloss":"dostluk ve destek","neighbor_only":"İçten dostluk ve sevgi bağı daha baskındır; yardım veya taraf tutma zorunlu değildir.","neighbor_ref":"root_000435/B003","relation_type":"near_neighbor","shared_zone":"İki dal da yakın dostluk ve sevgi ilişkisine dokunur."},{"boundary_match":"partial","distinction":"B004 yardım eden dost tarafı anlatır; B005 hukuki, soyla ilgili veya toplumsal statüden doğan özel bağı anlatır.","focus_only":"Destek, sevgi ve taraf olma ilişkisi öne çıkar.","gloss":"destek bağı ile statü bağı","neighbor_only":"Soy, özgür bırakma, komşuluk veya miras bağlantısı gibi statü bağı öne çıkar.","neighbor_ref":"root_001684/B005","relation_type":"near_neighbor","shared_zone":"İki dal da insanlar arasında yakın bağ ve karşılıklı yükümlülük alanına girer."}],"source_summary":"Kaynakların ortak anlatımı, dalı düşmana karşı yakın taraf olmak, sevmek, desteklemek, dost veya anlaşmalı yardımcı olmak ve inanç yahut arkadaşlık bakımından yakınlaşmak etrafında toplar."},"support_links":[]},{"boundary":"Dal, dostça destekten ayrılır; soy, özgür bırakma, komşuluk veya özel bağlılık ilişkisi ister.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"özel yakınlık ve bağlılık bağı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Soy, özgür bırakma, komşuluk veya hısımlıktan doğan özel bağlılık."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Soy, özgür bırakma, komşuluk veya hısımlıkla kurulan toplumsal ve hukuki bağlar için uygundur.","boundary_detail":"Dal, dostça destekten ayrılır; soy, özgür bırakma, komşuluk veya özel bağlılık ilişkisi ister.","concept_gloss":"özel yakınlık ve bağlılık bağı","contextual_glosses":[{"applicability":"Akrabalık ve özgür bırakmadan doğan özel ilişkiyi açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soy ve özgür bırakma kaynaklı bağı korur."},"facet_ids":["F001"],"text":"soy veya özgür bırakma bağı","usage_role":"explanatory"},{"applicability":"Soydan, anlaşmadan veya özel statüden bağlı kişiler topluluğu için doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlı kişiler ve yakınlık değerini korur."},"facet_ids":["F001"],"text":"yakın bağlılar","usage_role":"contextual"}],"definition":"Soy, özgür bırakma, komşuluk, hısımlık veya özel bağlılık sebebiyle kişileri birbirine bağlayan toplumsal ve hukuki yakınlık ilişkisidir. Bağ, miras, destek veya mensubiyet sonucunu doğurabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Soy, özgür bırakma, komşuluk veya hısımlıktan doğan özel bağlılık."}],"identity_rationale":"Kaynak ifadesi, özgür bırakan ve özgür bırakılan kişi, soy yakınları, destek veren anlaşmalı kişi, komşu, hısım ve bunlardan doğan özel bağları birlikte sayar. Bu dalda anlam genel yardım değil, belirli sosyal veya hukuki yakınlık statüsüdür.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"özgür bırakan, özgür bırakılan, soy yakını veya komşu gibi bağlı kişi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"özgür bırakma ilişkisine bağlı özel hak ve mensubiyet"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"soy yakınları veya özgür bırakma bağıyla bağlı kişiler"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"nimet veya özgür bırakma bağı kuran kişi"}],"lexicalization_note":"Çeşitli kişi adları ve özel bağ adı aynı statü alanında tutulur, genel destek anlamına yayılmaz.","neighbor_coverage_note":"Soy, hısımlık, özgür bırakma ve aynı kökün destek dalları denetlendi; genel destek adayları ayrı tutuldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal, belirli sözlük birimleriyle özgür bırakma ve statü adlarını da içerir; komşu dal daha genel soy ve bağlılık dokusunu anlatır.","focus_only":"Özgür bırakan ve özgür bırakılan kişi, komşu ve çeşitli bağlı kişi adları da sayılır.","gloss":"bağlılık bağı","neighbor_only":"Soy ve bağlılığın dokusu daha genel bir ilişki alanı olarak verilir.","neighbor_ref":"root_001348/B007","relation_type":"near_synonym","shared_zone":"İki dal da soy veya benzeri bağlılık ilişkisinin insanları birbirine bağlamasına dayanır."},{"boundary_match":"field_only","distinction":"B005 soy yakınlığını aşarak özgür bırakma ve komşuluk gibi statü bağlarını da içerir; komşu dal kan ve rahim yakınlığına odaklanır.","focus_only":"Özgür bırakma, komşuluk ve özel mensubiyet bağları da kapsamdadır.","gloss":"özel bağ ile akrabalık","neighbor_only":"Rahim ve kan bağına dayalı akrabalık çekirdeği öne çıkar.","neighbor_ref":"root_000552/B002","relation_type":"same_field","shared_zone":"İki dal da kişiler arasındaki yakın bağ alanındadır."}],"source_summary":"Kaynaklar bu dalı, soy yakınlığı, özgür bırakma ilişkisi, komşuluk, hısımlık, anlaşmalı bağlılık ve bunlara eşlik eden destek veya miras yükümlülüğü etrafında toplar."},"support_links":[]},{"boundary":"Dal, iş üstlenme veya yüz çevirme anlamına değil, bir şeye yönelme ve ona dönme anlamına bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"yüzünü veya dikkatini yöneltme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüz, duyu veya dikkati bir şeye doğru çevirip ona yönelme."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel yöneliş, dinleme veya dikkat verme bağlamlarını birlikte karşılar.","boundary_detail":"Dal, iş üstlenme veya yüz çevirme anlamına değil, bir şeye yönelme ve ona dönme anlamına bağlıdır.","concept_gloss":"yüzünü veya dikkatini yöneltme","contextual_glosses":[{"applicability":"Yüzün belirli bir yöne çevrildiği bağlamda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüzle yönelme değerini korur."},"facet_ids":["F001"],"text":"yüzünü çevirmek","usage_role":"contextual"},{"applicability":"İşitme, görme veya ilginin bir şeye yöneldiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duyu ve dikkat yönelişini korur."},"facet_ids":["F001"],"text":"dikkatini vermek","usage_role":"contextual"}],"definition":"Yüzü, gözü, kulağı veya dikkati bir şeye çevirip ona yönelmektir. Bazı kullanımlarda bu yönelme takip etme ya da razı olma tutumunu da taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüz, duyu veya dikkati bir şeye doğru çevirip ona yönelme."}],"identity_rationale":"Kaynak ifadesi, yüzü, kulağı veya gözü bir şeye yöneltmeyi ve ona dönük kabul, takip veya razı oluşu verir. Bu dal açıkça uzaklaşma değil, bedensel ya da dikkat yönünden yönelmedir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yüzünü bir şeye çevirmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yüzünü o yöne dönmüş veya ona uyan kişi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kulağını veya dikkatini bir şeye vermek"}],"lexicalization_note":"Yüz, işitme ve dikkat kalıpları yönelme çekirdeğinde tutulur; çıplak yönetim anlamı içeri alınmaz.","neighbor_coverage_note":"Yönelme, işitme, karşıya dönme ve yüz çevirme adayları değerlendirildi; ters kutup özellikle yayımlandı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"B006 yönelişi ve karşıya dönmeyi anlatır; B007 aynı eksenin tersinde, dönüp gitme veya ilgiyi kesme anlamını taşır.","focus_only":"Bir şeye doğru dönme, kabul veya dikkat verme vardır.","gloss":"yönelme ile yüz çevirme","neighbor_only":"Bir şeyden dönüp uzaklaşma, yüz çevirme veya dinlemeyi bırakma vardır.","neighbor_ref":"root_001684/B007","relation_type":"polarity_pair","shared_zone":"İki dal da yön değiştirme ve tutum alma ekseninde durur."},{"boundary_match":"partial","distinction":"Bu dal duyu ve dikkat yönelişini de içerir; komşu dal daha genel karşı karşıya oluş ve cephe yönünü anlatır.","focus_only":"Yüzün yanında işitme, göz ve razı oluş gibi tutum yönelişleri de kapsamdadır.","gloss":"yönelme","neighbor_only":"Karşı karşıya gelme ve genel cephe oluşturma alanı daha geniştir.","neighbor_ref":"root_001198/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeye yüzünü veya yönünü çevirme alanında örtüşür."}],"source_summary":"Kaynakların ortak anlatımı, dalı yüze, işitmeye veya göze yön verme, bir şeyi karşıya alıp ona dönme ve bu yönelişten doğan takip ya da razı oluş ile açıklar."},"support_links":[]},{"boundary":"Dal yalnız bedensel dönüp gitme değildir; bedensel uzaklaşma ile tutum olarak yüz çevirme birlikte bulunur.","branch_kind":"collocation","branch_ref":"root_001684/B007","candidate_links":[{"candidate_id":"cand_bd9c6a892aaff4cff6cb","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"dönüp yüz çevirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dönüp uzaklaşma, yüz çevirme veya dinleme ve uyma bağını kesme."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel uzaklaşma ve tutum olarak ilgiyi kesme bağlamlarını birlikte karşılar.","boundary_detail":"Dal yalnız bedensel dönüp gitme değildir; bedensel uzaklaşma ile tutum olarak yüz çevirme birlikte bulunur.","concept_gloss":"dönüp yüz çevirme","contextual_glosses":[{"applicability":"Kaçış veya bedensel uzaklaşma bağlamlarında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dönüp gitme ve uzaklaşma değerini korur."},"facet_ids":["F001"],"text":"arkasını dönüp kaçmak","usage_role":"contextual"},{"applicability":"Birinden, bir işten veya buyruktan ilgiyi kesme bağlamına uyar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İlgiyi kesme ve reddedici uzaklaşmayı korur."},"facet_ids":["F001"],"text":"yüz çevirmek","usage_role":"contextual"}],"definition":"Bir şeyden bedenen dönüp uzaklaşmak veya ona kulak vermeyi ve uymayı bırakarak yüz çevirmektir. Kaçış, ayrılma ve ilgiyi kesme aynı sınır içinde kalır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dönüp uzaklaşma, yüz çevirme veya dinleme ve uyma bağını kesme."}],"identity_rationale":"Kaynak ifadesi, kişinin dönüp gitmesini, kaçarken arkasını dönmesini, birinden yüz çevirmesini ve dinleme ya da buyruğa uymayı bırakmasını verir. Bu nedenle dal, yönelmenin karşıtı olan uzaklaşma ve ilgiyi kesme anlamındadır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"arkasını dönüp kaçarak uzaklaşmak"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"birinden yüz çevirmek ve ilgiyi kesmek"}],"lexicalization_note":"Anlam kalıplı kullanımlara bağlıdır; çıplak köke yönetim veya destek anlamı yüklenmez.","neighbor_coverage_note":"Kaçış, reddetme, ilgiyi kesme ve aynı kökün yönelme dalı denetlendi; en keskin karşıtlıklar yayımlandı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"B007 uzaklaşma ve reddedici yön değişimini anlatır; B006 kabul edici veya dikkat veren yönelişi anlatır.","focus_only":"Bir şeyden dönüp uzaklaşma ve ilgiyi kesme vardır.","gloss":"yüz çevirme ile yönelme","neighbor_only":"Bir şeye doğru dönme, dikkat verme veya razı oluş vardır.","neighbor_ref":"root_001684/B006","relation_type":"polarity_pair","shared_zone":"İki dal da bedenin veya tutumun yön değiştirmesiyle ilgilidir."},{"boundary_match":"partial","distinction":"Bu dal bedensel uzaklaşmayı tutum olarak ilgiyi kesmeyle birleştirir; komşu dal arka taraf ve bozgun görüntüsünü daha açık taşır.","focus_only":"Dinlemeyi ve buyruğa uymayı bırakma gibi iç tutum boyutu da vardır.","gloss":"dönüp uzaklaşma","neighbor_only":"Savaşta arkayı dönme, bozgun ve arka yön vurgusu daha belirgindir.","neighbor_ref":"root_000458/B003","relation_type":"near_synonym","shared_zone":"İki dal da arkasını dönme, uzaklaşma ve yüz çevirme alanında örtüşür."}],"source_summary":"Kaynakların ortak anlatımı, dalı kaçışla dönüp gitme, birinden yüz çevirme ve dinleme ya da buyruğa uyma bağını kesme biçimlerinde açıklar."},"support_links":["sup_af17eee031fdcbe1d3e6"]},{"boundary":"Dal, kötü sonuç tehdidi taşıyan kalıptan ayrılır; burada uygunluk ve haklı öncelik vardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"daha uygun ve hak sahibi olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeye daha uygun, daha layık veya daha hak sahibi olma."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işe, şeye veya konuma en layık olanı belirtme bağlamlarında uygundur.","boundary_detail":"Dal, kötü sonuç tehdidi taşıyan kalıptan ayrılır; burada uygunluk ve haklı öncelik vardır.","concept_gloss":"daha uygun ve hak sahibi olma","contextual_glosses":[{"applicability":"Kişinin bir iş veya konuma başkasından daha uygun olduğu bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Layık olma ve öncelik değerini korur."},"facet_ids":["F001"],"text":"daha layık","usage_role":"contextual"},{"applicability":"Bir şey üzerinde haklı öncelik veya sahiplik önceliği belirtilirken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Haklı öncelik ve uygunluk anlamını korur."},"facet_ids":["F001"],"text":"daha hak sahibi","usage_role":"contextual"}],"definition":"Bir kişinin veya tarafın bir şeye başkasından daha uygun, daha layık ya da daha hak sahibi olmasıdır. Anlam bir tehdit değil, uygunluk ve öncelik yargısıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeye daha uygun, daha layık veya daha hak sahibi olma."}],"identity_rationale":"Kaynak ifadesi, bir kişinin bir şeye daha uygun, daha layık veya daha hak sahibi olmasını anlatır. Dal, tehdit kalıbıyla değil, öncelik ve yerindelik karşılaştırmasıyla tanımlanır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bir şeye daha uygun, daha layık veya daha hak sahibi olmak"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"iki daha haklı veya daha uygun kişi"}],"lexicalization_note":"Karşılaştırmalı uygunluk kalıbı ile iki kişinin daha haklı olması biçimi aynı öncelik sınırında tutulur.","neighbor_coverage_note":"Hak, uygunluk, öncelik ve aynı yüzey kalıbı adayları denetlendi; tehdit anlamı ayrı dalda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bir şeye en layık veya daha hak sahibi olmayı karşılaştırmalı verir; komşu dal hakkın kendisini ve ona sahip olmayı daha özel anlatır.","focus_only":"Karşılaştırmalı olarak daha layık veya daha uygun olma vurgusu vardır.","gloss":"haklı öncelik","neighbor_only":"Belirli bir hakkın mülk veya talep olarak sabit olması daha baskındır.","neighbor_ref":"root_000347/B003","relation_type":"near_synonym","shared_zone":"İki dal da hak, uygunluk ve öncelik alanında örtüşür."},{"boundary_match":"partial","distinction":"B008 uygunluğu öncelik ve haklılık karşılaştırmasıyla kurar; komşu dal genel ehillik ve yaraşırlık alanında kalabilir.","focus_only":"Hak sahibi olma ve öncelik karşılaştırması açıkça bulunur.","gloss":"uygun olma","neighbor_only":"Bir kişi veya şeyin uygun, ehil ya da yaraşır olması daha genel verilir.","neighbor_ref":"root_000064/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir şeye yaraşma ve uygunluk alanında buluşur."}],"source_summary":"Kaynakların ortak anlatımı, dalı bir işe veya nesneye daha layık, daha uygun ve daha hak sahibi olma karşılaştırması olarak verir; iki kişinin en haklı olması da bu kapsamdadır."},"support_links":[]},{"boundary":"Dal yalnız belirli tehdit ve uyarı kalıbında geçerlidir; uygunluk karşılaştırması değildir.","branch_kind":"non_bare","branch_ref":"root_001684/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"yaklaşan kötü sonuç tehdidi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yaklaşan kötü sonuçla tehdit etme, uyarma veya kaçırılana hayıflandırma."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Muhataba kötü akıbetin yaklaştığını bildiren uyarı ve tehdit sözü için uygundur.","boundary_detail":"Dal yalnız belirli tehdit ve uyarı kalıbında geçerlidir; uygunluk karşılaştırması değildir.","concept_gloss":"yaklaşan kötü sonuç tehdidi","contextual_glosses":[{"applicability":"Kötü sonucun yaklaştığını sezdiren tehditli hitap bağlamlarında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tehdit ve yaklaşan kötü sonuç değerini korur."},"facet_ids":["F001"],"text":"yazık sana, başına gelecek var","usage_role":"contextual"},{"applicability":"Kaçırılan şey üzerine acı hatırlatma anlamı öne çıktığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayıflandırma ve uyarı değerini korur."},"facet_ids":["F001"],"text":"kaçırdığına hayıflanma","usage_role":"explanatory"}],"definition":"Muhataba kötü bir sonucun yaklaştığını bildiren tehdit ya da uyarı kalıbıdır. Bazı kullanımlarda kaçırılan şey için acı bir hatırlatma veya hayıflanma da taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yaklaşan kötü sonuçla tehdit etme, uyarma veya kaçırılana hayıflandırma."}],"identity_rationale":"Kaynak ifadesi, kalıbın tehdit, uyarı, yaklaşan kötü sonuç veya kaçırılan şey için acı hatırlatma değeri taşıdığını söyler. Bu nedenle dal, B008'deki uygunluk ve hak sahibi olma anlamından ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"tehdit ve uyarı sözü; sana kötü şey yaklaştı"}],"lexicalization_note":"Anlam belirli sözlü kalıba bağlıdır; çıplak öncelik veya yakınlık anlamı olarak genellenmez.","neighbor_coverage_note":"Tehdit, yıkım ve aynı kalıptan doğan uygunluk adayı denetlendi; söz kalıbı dışındaki zarar dalları ayrı tutuldu.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"B009 kalıplaşmış bir uyarı ve tehdit sözüdür; B008 uygunluk ve haklı öncelik yargısıdır.","focus_only":"Tehdit, kötü sonuç ve hayıflanma kalıbı vardır.","gloss":"tehdit ile öncelik","neighbor_only":"Bir şeye daha layık, daha uygun veya daha hak sahibi olma vardır.","neighbor_ref":"root_001684/B008","relation_type":"other","shared_zone":"Aynı yüzey kalıbı okuyucuda karışıklık yaratabilir."},{"boundary_match":"partial","distinction":"Bu dal zararın kendisini değil, muhataba yaklaşan zararı bildiren kalıbı anlatır; komşu dal yıkım veya yok oluşun kendisidir.","focus_only":"Kötü sonucun yaklaştığını söyleyen sözlü tehdit vardır.","gloss":"tehdit ve yıkım","neighbor_only":"Gerçek yıkım, yok etme veya bozma eylemi anlatılır.","neighbor_ref":"root_000174/B001","relation_type":"near_neighbor","shared_zone":"İki dal da kötü sonuç ve zarar alanına dokunur."}],"source_summary":"Kaynakların ortak anlatımı, dalı muhataba kötü ya da yıkıcı bir şeyin yaklaştığını sezdiren tehdit ve uyarı sözü olarak verir; ayrıca kaçırılan şey üzerine acı hatırlatma değeri bulunur."},"support_links":[]},{"boundary":"Dal genel yağmur adı değildir; önceki yağmuru izleyen özel yağmurla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"önceki yağmuru izleyen yağmur","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Önceki veya erken mevsim yağmurunu izleyen yağmur."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yağmurun özel ad olarak bir önceki yağmurdan sonra gelişini anlatan bağlamlarda uygundur.","boundary_detail":"Dal genel yağmur adı değildir; önceki yağmuru izleyen özel yağmurla sınırlıdır.","concept_gloss":"önceki yağmuru izleyen yağmur","contextual_glosses":[{"applicability":"Önceki mevsim yağmurunu izleyen yağmur bağlamında doğal ve kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İzleyen yağmur anlamını korur."},"facet_ids":["F001"],"text":"sonraki yağmur","usage_role":"contextual"},{"applicability":"Toprağın özel izleyen yağmurla ıslanması bağlamında açıklayıcıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Toprağın izleyen yağmuru alması değerini korur."},"facet_ids":["F001"],"text":"toprak bu yağmuru aldı","usage_role":"explanatory"}],"definition":"İlk mevsim yağmurundan ya da önceki yağmurdan sonra gelen yağmurdur. Toprağın bu yağmuru alması ve iyiliğin iyilik ardınca gelmesi gibi özel kullanımlar bu izleme fikrine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Önceki veya erken mevsim yağmurunu izleyen yağmur."}],"identity_rationale":"Kaynak ifadesi, bu dalı erken mevsim yağmurundan veya önceki yağmurdan sonra gelen yağmur adı olarak verir. Toprağın bu yağmuru alması ve dua kalıbındaki ardışık iyilik ifadesi de aynı izleme ilişkisine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"önceki yağmurdan sonra gelen yağmur"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"erken mevsim yağmurunu izleyen yağmur adı"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"toprağa izleyen yağmurun yağması"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"iyilik ardından gelen yağmur veya iyilik"}],"lexicalization_note":"Yağmur adı, toprağın bu yağmuru alması ve dua kalıbındaki özel kullanım ayrı ayrı korunur.","neighbor_coverage_note":"Yağmur adayları sıralanma, miktar ve toprakla ilişki bakımından değerlendirildi; genel yağmur adları yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal adlandırmayı önceki yağmurun ardından gelmeye bağlar; komşu dal toprağın tekrar yağmur alması veya erken mevsim zamanı yönünden daha geniştir.","focus_only":"Özellikle erken mevsim yağmurunu veya önceki yağmuru izleyen yağmur adı olarak verilir.","gloss":"izleyen yağmur","neighbor_only":"Daha önce ıslanmış toprağı tekrar yoklayan yağmur veya erken mevsim yağmuru alanı daha geniştir.","neighbor_ref":"root_001055/B007","relation_type":"near_synonym","shared_zone":"İki dal da önceki yağmurla ilişkili sonraki yağmur alanında örtüşür."},{"boundary_match":"field_only","distinction":"B010 yağmurun sırasını ve önceki yağmurla ilişkisini tanımlar; komşu dal yağmurun miktarı ve bolluğunu tanımlar.","focus_only":"Yağmurun önceki yağmuru izlemesi belirleyicidir.","gloss":"sonraki yağmur ile bol yağmur","neighbor_only":"Yağmurun çokluğu ve bereketli oluşu belirleyicidir.","neighbor_ref":"root_000274/B002","relation_type":"same_field","shared_zone":"İki dal da yağmur adlandırması alanındadır."}],"source_summary":"Kaynakların ortak anlatımı, dalı önceki yağmuru veya erken mevsim yağmurunu izleyen yağmur olarak açıklar; toprağın bu yağmuru alması da aynı adlandırmaya bağlanır."},"support_links":[]},{"boundary":"Dal çıplak somut addır; yönetim, yağmur veya başka aynı sesli kullanımlar buna taşınmaz.","branch_kind":"bare","branch_ref":"root_001684/B011","candidate_links":[{"candidate_id":"cand_f3867b72479dda30b840","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"deve sırtı alt örtüsü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Deve sırtında semer veya yük takımı altında kullanılan örtü ya da altlık."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Devenin sırtında semer veya yük takımı altında kullanılan örtü için uygundur.","boundary_detail":"Dal çıplak somut addır; yönetim, yağmur veya başka aynı sesli kullanımlar buna taşınmaz.","concept_gloss":"deve sırtı alt örtüsü","contextual_glosses":[{"applicability":"Deve veya yük hayvanı takımının altında kullanılan örtü bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alt örtü ve semerle ilişkiyi korur."},"facet_ids":["F001"],"text":"semer altı örtüsü","usage_role":"contextual"}],"definition":"Devenin sırtına, semer ya da yük takımı altına konan örtü, keçe veya benzeri altlıktır. Tekil ve çoğul biçimler aynı eşya sınıfına bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Deve sırtında semer veya yük takımı altında kullanılan örtü ya da altlık."}],"identity_rationale":"Kaynak ifadesi, dalı devenin sırtına konan, semer veya yük altındaki örtü ya da benzeri parça olarak verir. Bu somut eşya anlamı yönetim, yağmur veya yakınlık dallarından ayrı tutulur.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"deve sırtında semer altında kullanılan örtü"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"semer altı örtüleri"}],"lexicalization_note":"Çıplak eşya adı tanımlanır; kalıp dışı soyut anlamlar bu dala alınmaz.","neighbor_coverage_note":"Deve takımı, örtü, yastık ve taşıma araçları adayları denetlendi; nesnenin altlık işlevini ayıranlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal altlık olarak kullanılan örtüyü tanımlar; komşu dal deve sırtındaki daha genel binek veya örtü takımını kapsar.","focus_only":"Örtünün semer veya takım altında yer alması belirleyicidir.","gloss":"semer altı örtüsü","neighbor_only":"Deve sırtındaki daha genel örtü, küçük semer veya takım parçası alanı vardır.","neighbor_ref":"root_000766/B010","relation_type":"near_neighbor","shared_zone":"İki dal da deve sırtında kullanılan örtü veya takım parçası alanındadır."},{"boundary_match":"field_only","distinction":"B011 asıl takımın altında kalan örtüyü belirtir; komşu dal semer veya binek takımının kendisini anlatır.","focus_only":"Semerin altında kalan örtü veya altlık nesnedir.","gloss":"alt örtü ile semer","neighbor_only":"Devenin asıl binek takımı veya semeri anlatılır.","neighbor_ref":"root_000551/B002","relation_type":"same_field","shared_zone":"İki dal da deve üzerinde kullanılan binek takımı alanındadır."}],"source_summary":"Kaynakların ortak anlatımı, dalı devenin sırtında semer veya benzeri takım altında kullanılan örtü, keçe ya da altlık olarak verir; çoğul biçim aynı nesnenin çoğuludur."},"support_links":["sup_d8d61ae7f0534b9fac9d"]},{"boundary":"Dal, görev üstlenme değil, kalıplı olarak bir şeyi ele geçirme veya hedefe varmadır.","branch_kind":"collocation","branch_ref":"root_001684/B012","candidate_links":[{"candidate_id":"cand_35a71a2826af60921ef3","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"ele geçirip hedefe ulaşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi ele geçirip ona üstün gelme veya yarış hedefine ulaşma."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyi kontrol altına alma veya yarışta son noktaya varma bağlamlarında uygundur.","boundary_detail":"Dal, görev üstlenme değil, kalıplı olarak bir şeyi ele geçirme veya hedefe varmadır.","concept_gloss":"ele geçirip hedefe ulaşma","contextual_glosses":[{"applicability":"Mal veya nesne üzerinde üstünlük kurma bağlamlarında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ele geçirme ve kontrol değerini korur."},"facet_ids":["F001"],"text":"eline geçirmek","usage_role":"contextual"},{"applicability":"Yarış veya mesafe sonuna ulaşma bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hedefe ulaşma değerini korur."},"facet_ids":["F001"],"text":"hedefe varmak","usage_role":"contextual"}],"definition":"Bir şeyin kişinin eline geçmesi, onun üzerinde üstünlük kurması veya yarışta hedefe varıp onu elde etmesidir. Sahip olma, galip gelme ve hedefe ulaşma sonuçları birlikte korunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi ele geçirip ona üstün gelme veya yarış hedefine ulaşma."}],"identity_rationale":"Kaynak ifadesi, bir şeyin kişinin eline geçmesini veya onun üzerinde üstün gelmesini ve yarış bağlamında son noktaya varıp onu geçerek elde etmesini verir. Dalda ele geçirme ile hedefe varma aynı üstün gelme sonucuna bağlanır.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"bir şeyi ele geçirmek veya ona üstün gelmek"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"hedefe varmak veya ona önce ulaşmak"}],"lexicalization_note":"Anlam belirli kalıplara bağlıdır; çıplak yönetim veya yakınlık anlamına genellenmez.","neighbor_coverage_note":"Ele geçirme, üstünlük, hedefe varma ve yönetim adayları denetlendi; görev üstlenme dalları ayrı tutuldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B012 ele geçirmeyi hedefe varma kullanımıyla birlikte verir; komşu dal daha genel üstünlük, kuşatma ve toplama alanını kapsar.","focus_only":"Yarış hedefine varma ve hedefi önde alma kullanımı da vardır.","gloss":"ele geçirme","neighbor_only":"Toplama, kuşatma ve geniş anlamda kontrol altına alma alanı daha geniştir.","neighbor_ref":"root_000368/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir şey üzerinde üstünlük ve kontrol kurma alanında örtüşür."},{"boundary_match":"field_only","distinction":"B012 sonuç olarak elde etme veya hedefe ulaşmayı ister; komşu dal üstünlük ve galiplik alanında daha geniştir.","focus_only":"Bir şeyin elde edilmesi veya hedefe varılması belirleyicidir.","gloss":"ele geçirme ile üstünlük","neighbor_only":"Üstünlük, yükseklik veya galiplik niteliği daha genel anlatılır.","neighbor_ref":"root_000104/B008","relation_type":"same_field","shared_zone":"İki dal da galip gelme ve üstün konuma geçme alanına dokunur."}],"source_summary":"Kaynakların ortak anlatımı, dalı bir şeyin ele geçmesi, mal üzerinde üstünlük kurulması ve yarış ya da mesafe bağlamında hedefe varılıp orada üstün gelinmesi olarak açıklar."},"support_links":["sup_b35576db6122b0333bd2"]},{"boundary":"Dal kalıplı verme ve yöneltme anlamındadır; yönetim veya öncelik anlamına genellenmez.","branch_kind":"collocation","branch_ref":"root_001684/B013","candidate_links":[{"candidate_id":"cand_bee48b9068fee4761962","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"birine iyi ya da kötü şey yöneltme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birine iyi veya kötü bir şeyi yöneltip ulaştırma ya da payına kılma."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye yarar, iyilik, zarar veya başka bir şeyi ulaştırma bağlamlarında uygundur.","boundary_detail":"Dal kalıplı verme ve yöneltme anlamındadır; yönetim veya öncelik anlamına genellenmez.","concept_gloss":"birine iyi ya da kötü şey yöneltme","contextual_glosses":[{"applicability":"Birine iyilik ulaştırma bağlamında doğal Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İyiliği kişiye ulaştırma değerini korur."},"facet_ids":["F001"],"text":"iyilikte bulunmak","usage_role":"contextual"},{"applicability":"Birine kötü bir şey yöneltme bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kötü şeyi kişiye yöneltme değerini korur."},"facet_ids":["F001"],"text":"zarar yöneltmek","usage_role":"contextual"}],"definition":"Bir şeyi, iyiliği, yararı veya kötülüğü bir kişiye yöneltip ona ulaştırmak ya da onun payına kılmaktır. Verilen şeyin iyi veya kötü olması dalın kapsamını değiştirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birine iyi veya kötü bir şeyi yöneltip ulaştırma ya da payına kılma."}],"identity_rationale":"Kaynak ifadesi, birine bir şey, iyilik, kötülük veya yarar yöneltmeyi ve onu o kişiye ulaştırmayı verir. Dal, görevi üstlenmek veya daha haklı olmak değil, bir şeyi birine tahsis edip ulaştırmaktır.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"birine iyilik yapmak veya bir şeyi ona ulaştırmak"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"birine iyilik veya kötülük yöneltmek"}],"lexicalization_note":"Anlam birine bir şey, iyilik veya kötülük yöneltme kalıbına bağlı tutulur.","neighbor_coverage_note":"Verme, ulaştırma, kazandırma ve satış adayları değerlendirildi; yalnız yöneltme çekirdeğini aydınlatanlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B013 verilen şeyin kişiye yöneltilmesini ve iyilik ya da kötülük olabilmesini vurgular; komşu dal genel verme ve getirme anlamındadır.","focus_only":"İyi ya da kötü bir şeyin belirli kişiye yöneltilmesi vurgulanır.","gloss":"birine verme","neighbor_only":"Genel verme, getirme veya bir şeyi birine sunma alanı daha geniştir.","neighbor_ref":"root_000009/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi bir kişiye ulaştırma alanında örtüşür."},{"boundary_match":"partial","distinction":"B013 iyi ve kötü yöneltmeyi birlikte kapsar; komşu dal başkasına yarar veya mal kazandırmaya odaklanır.","focus_only":"Kötülük veya zarar yöneltme de kapsam içindedir.","gloss":"yarar ulaştırma","neighbor_only":"Başkasına mal veya yarar kazandırma daha özel ve olumlu yöndedir.","neighbor_ref":"root_001296/B002","relation_type":"near_neighbor","shared_zone":"İki dal da kişiye bir yarar veya şey kazandırma alanına yaklaşır."}],"source_summary":"Kaynakların ortak anlatımı, dalı bir kişiye iyilik, yarar, kötülük veya herhangi bir şeyi ulaştırma ve onun üzerine yöneltme olarak açıklar."},"support_links":["sup_0c6dae45056bdd70f0cd"]},{"boundary":"Dal yalnız satıştaki özel devir işlemidir; genel alım satım veya bağış anlamına genişletilmez.","branch_kind":"non_bare","branch_ref":"root_001684/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"aldığı fiyatla devretme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Satın alınan malı bilinen aynı fiyatla başka birine devretme."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Alım satımda malın satın alındığı bilinen fiyat üzerinden devredildiği özel işlem için uygundur.","boundary_detail":"Dal yalnız satıştaki özel devir işlemidir; genel alım satım veya bağış anlamına genişletilmez.","concept_gloss":"aldığı fiyatla devretme","contextual_glosses":[{"applicability":"Ticari işlem bağlamında malın alındığı fiyatla başkasına geçirilmesini doğal biçimde verir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aynı fiyatla devir şartını korur."},"facet_ids":["F001"],"text":"maliyet fiyatına devretmek","usage_role":"contextual"}],"definition":"Bir malı bilinen bir fiyatla satın aldıktan sonra aynı fiyatla başka birine devretme işlemidir. Anlam, satış içindeki özel fiyat ve devir şartına bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Satın alınan malı bilinen aynı fiyatla başka birine devretme."}],"identity_rationale":"Kaynak ifadesi, bir malı bilinen bir fiyatla satın aldıktan sonra aynı fiyatla başka birine devretme işlemini açıkça verir. Bu tekil ticaret terimi, yönetim veya genel verme anlamlarından ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"satın alınan malı bilinen aynı fiyatla başkasına devretme"}],"lexicalization_note":"Anlam satış alanındaki belirli terime bağlıdır; çıplak kök anlamına taşınmaz.","neighbor_coverage_note":"Satış, fiyat, devir ve genel verme adayları denetlendi; yalnız ticari işlem sınırını gösterenler yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"B014 genel satış değil, alınmış malı alış fiyatıyla devretme terimidir; komşu dal satış ve satın alma işlemini genel olarak anlatır.","focus_only":"Malın önce alınması ve aynı bilinen fiyatla devredilmesi şarttır.","gloss":"özel devir ile alım satım","neighbor_only":"Alım ve satımın genel karşılıklı işlem alanı vardır.","neighbor_ref":"root_000169/B001","relation_type":"same_field","shared_zone":"İki dal da ticari alım satım alanındadır."},{"boundary_match":"field_only","distinction":"B014 fiyatı şart olarak kullanan bir işlem adıdır; komşu dal bedel veya fiyat kavramının kendisini verir.","focus_only":"Aynı fiyatla başka kişiye devir işlemi anlatılır.","gloss":"devir işlemi ile fiyat","neighbor_only":"Fiyatın, bedelin veya değerin kendisi anlatılır.","neighbor_ref":"root_000206/B001","relation_type":"same_field","shared_zone":"İki dal da satışta bedel ve fiyat alanına dokunur."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanık, bu kullanımı bilinen fiyatla alınan malın aynı fiyatla başka kişiye devri olarak verir."}],"source_summary":"Bu dal, satış alanında belirli bir işlem adı olarak sunulur; malın önce bilinen fiyatla alınması ve sonra aynı fiyatla başka kişiye devredilmesi şartı belirleyicidir."},"support_links":[]},{"boundary":"Dal hayvan sürüsündeki ayırma ve sütten kesme uygulamasına bağlıdır; genel ardışıklık değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B015","candidate_links":[{"candidate_id":"cand_cf5b732356a2c14586ed","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"küçük sürü hayvanlarını ayırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Küçük sürü hayvanlarını büyüklerinden veya yavruları analarından ayırma."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Küçük hayvanları büyüklerinden veya yavruları analarından ayırma bağlamlarında uygundur.","boundary_detail":"Dal hayvan sürüsündeki ayırma ve sütten kesme uygulamasına bağlıdır; genel ardışıklık değildir.","concept_gloss":"küçük sürü hayvanlarını ayırma","contextual_glosses":[{"applicability":"Yavru develerin analarından kesilmesi ve alıştırılması bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Anadan ayırma ve alıştırma değerini korur."},"facet_ids":["F001"],"text":"yavruları anadan ayırmak","usage_role":"contextual"},{"applicability":"Sürü içindeki küçük hayvanların büyüklerden ayrıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sürü içinde ayırma değerini korur."},"facet_ids":["F001"],"text":"küçükleri büyüklerden ayırmak","usage_role":"contextual"}],"definition":"Küçük sürü hayvanlarını büyüklerinden veya yavruları analarından ayırarak bağımsızlaşmaya ve yola gelmeye alıştırmaktır. Anlam, hayvancılıktaki ayırma ve sütten kesme uygulamasına bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Küçük sürü hayvanlarını büyüklerinden veya yavruları analarından ayırma."}],"identity_rationale":"Kaynak ifadesi, küçük sürü hayvanlarını büyüklerinden ayırmayı ve yavru develeri analarından keserek alıştırmayı verir. Bu dal, peş peşe geliş veya dostça destek anlamından farklı, hayvancılıkta ayırma ve alıştırma işlemidir.","lexical_glosses":[{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"küçük sürü hayvanlarını büyüklerinden ayırmak"},{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"yavru develeri analarından ayırıp alıştırma"}],"lexicalization_note":"Kalıplı sürü ayırma ve yavruyu anadan kesme kullanımları birlikte ama hayvancılık alanıyla sınırlı tutulur.","neighbor_coverage_note":"Küçük hayvan adları, buzağı ve deve yavrusu adayları ile aynı kökün ardışıklık dalı denetlendi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"B015 hayvancılık uygulaması olarak ayırmayı anlatır; komşu dal küçük hayvanların kendisini adlandırır.","focus_only":"Küçüklerin büyüklerden ayrılması veya yavruların anadan kesilmesi eylemi vardır.","gloss":"ayırma ile küçük hayvan adı","neighbor_only":"Küçük hayvanların adlandırılması ve sınıflanması öne çıkar.","neighbor_ref":"root_000160/B004","relation_type":"same_field","shared_zone":"İki dal da küçük sürü hayvanları alanındadır."},{"boundary_match":"field_only","distinction":"B015 sürüde ayırma işlemidir; B002 herhangi bir hayvancılık işlemi gerektirmeyen ardışık sıra anlamıdır.","focus_only":"Hayvanları ayırma ve alıştırma uygulamasıdır.","gloss":"ayırma ile ardışıklık","neighbor_only":"Şeylerin peş peşe gelişi ve kesintisiz sıra anlamıdır.","neighbor_ref":"root_001684/B002","relation_type":"other","shared_zone":"Aynı kökteki benzer yüzey biçimi karışıklık yaratabilir."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanık, kullanımı küçük hayvanları büyüklerden ve yavruları analarından ayırma uygulaması olarak verir."}],"source_summary":"Bu dal, sürü hayvanlarında küçükleri büyüklerden ayırma ve yavru develeri analarından kesip alışmalarını sağlama biçimindeki özel uygulamayı özetler."},"support_links":["sup_c10ff24f40bd6b5ad803"]},{"boundary":"Dal bitki ve meyve olgunlaşma evresine bağlıdır; insana ait uzaklaşma anlamı buraya taşınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"taze hurmanın kurumaya dönmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taze hurmanın solup açık renge dönerek kurumaya başlaması."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Taze hurmanın solgunlaşıp kurumaya yöneldiği olgunluk sonrası evre için uygundur.","boundary_detail":"Dal bitki ve meyve olgunlaşma evresine bağlıdır; insana ait uzaklaşma anlamı buraya taşınmaz.","concept_gloss":"taze hurmanın kurumaya dönmesi","contextual_glosses":[{"applicability":"Taze hurmanın açık renkli kuruma evresine girmesi bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Solma ve kurumaya başlama değerini korur."},"facet_ids":["F001"],"text":"solup kurumaya başlamak","usage_role":"contextual"},{"applicability":"Evrenin rengini veya solgunluğunu açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Renk değişimi ve solgunluk değerini korur."},"facet_ids":["F001"],"text":"solgun kuruma rengi","usage_role":"explanatory"}],"definition":"Taze hurmanın olgunluk sonrası solup açık renge dönerek kurumaya yönelen evreye girmesidir. Bu evrenin belirgin rengi veya solgunluğu da adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taze hurmanın solup açık renge dönerek kurumaya başlaması."}],"identity_rationale":"Kaynak ifadesi, taze hurmanın solma, sararma veya kurumaya dönme evresine girmesini ve bu evrenin açık rengini verir. Dal, yüz çevirme değil, meyvenin olgunluk sonrası değişim aşamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"taze hurmanın solup kurumaya başlaması"},{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"taze hurmadaki solgun kuruma rengi"}],"lexicalization_note":"Meyvenin evreye girmesi ve bu evrenin adı birlikte korunur; soyut yüz çevirme anlamına yayılmaz.","neighbor_coverage_note":"Hurma, meyve olgunlaşması, sararma ve kuruma adayları değerlendirildi; uzaklaşma anlamlı dallar ayrı tutuldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B016 taze hurmanın özel geçiş evresini anlatır; komşu dal bitki ve sapların daha genel sararıp kuruma durumunu verir.","focus_only":"Taze hurmanın belirli solgun kuruma evresine bağlıdır.","gloss":"sararıp kurumaya dönme","neighbor_only":"Bitkinin veya sapın sararıp kuruması daha genel bir bitki evresidir.","neighbor_ref":"root_001033/B015","relation_type":"near_synonym","shared_zone":"İki dal da bitkisel ürünün sararma veya kuruma evresine girmesi alanında örtüşür."},{"boundary_match":"partial","distinction":"B016 geçiş evresidir; komşu dal kurumuş olma durumunu daha doğrudan anlatır.","focus_only":"Kurumaya başlama ve solgun renk evresi vurgulanır.","gloss":"kurumaya başlama ile kurumuşluk","neighbor_only":"Hurmanın kurumuş olması veya kuruluk durumu öne çıkar.","neighbor_ref":"root_000242/B005","relation_type":"near_neighbor","shared_zone":"İki dal da hurma veya meyve kuruması alanına yaklaşır."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanık, kullanımı taze hurmanın kurumaya dönerken aldığı solgun ve açık renkli evre olarak verir."}],"source_summary":"Bu dal, taze hurmanın solma ve açık renge dönme yoluyla kurumaya başladığı evreyi ve bu evrenin rengini özetler."},"support_links":[]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000006/B004","candidate_links":[{"candidate_id":"cand_f3867b72479dda30b840","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b7e76aadee3dcb193ba0","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Burden and liability in the camel field supply what the hidden layer continues to carry.","root":"ء ب ل","source_ref":"88:17","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000006","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d8d61ae7f0534b9fac9d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000065/B003","candidate_links":[{"candidate_id":"cand_f3867b72479dda30b840","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b7e76aadee3dcb193ba0","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Repeated bodily movement in travel and return supplies the route across which the concealed load persists.","root":"ء و ب","source_ref":"88:25","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000065","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d8d61ae7f0534b9fac9d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000318/B001","candidate_links":[{"candidate_id":"cand_bd9c6a892aaff4cff6cb","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7d026e47fa30824010d2","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Counting and accounting preserve the acts as liabilities even after the person disowns the bond.","root":"ح س ب","source_ref":"88:26","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000318","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_af17eee031fdcbe1d3e6"]}],"candidate_inventory":[{"anchor_refs":["88:23"],"branch_refs":["root_001307/B003","root_001307/B004","root_001307/B006"],"candidate_id":"cand_2a6a78a71a541a12c98f","commentary_obligation":"review","focus_branch_refs":["root_001307/B003","root_001307/B004","root_001307/B006"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":[],"root_ids":[],"scope":"pericope","source_local_id":"B:Disbelief and Ingratitude","source_type":"channel","support_ids":["sup_0f6695f9ff21df865be3","sup_1fb8fb01b284d4088a31","sup_64449116e4f17ecfc878","sup_e7b764fb3a24b15714db","sup_ec4ab63a498046d0871a"],"title":"Disbelief and Ingratitude","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:17","88:20","88:23"],"branch_refs":["root_000006/B003","root_000704/B007","root_001684/B015"],"candidate_id":"cand_cf5b732356a2c14586ed","commentary_obligation":"review","focus_branch_refs":["root_001684/B015"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000006/B003","root_000704/B007"],"root_ids":[],"scope":"pericope","source_local_id":"D:Goat and Separated Young Stock","source_type":"channel","support_ids":["sup_281c2464617b0da80fe3","sup_947424e6de401bf25361","sup_a98cadbae3c48dbad291","sup_c10ff24f40bd6b5ad803","sup_eca1cccf8c6ad967ef3e"],"title":"Goat and Separated Young Stock","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:17","88:23","88:24","88:25"],"branch_refs":["root_000047/B002","root_001307/B009","root_001684/B013"],"candidate_id":"cand_bee48b9068fee4761962","commentary_obligation":"review","focus_branch_refs":["root_001307/B009","root_001684/B013"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000047/B002"],"root_ids":[],"scope":"pericope","source_local_id":"D:Oath and Expiation","source_type":"channel","support_ids":["sup_0c6dae45056bdd70f0cd","sup_6ee9761fc619b8e6dbee","sup_a842245d16d4b249e9bf","sup_e9448aa2ee4d33b4c162","sup_ec815253d8cf81dfa4ad"],"title":"Oath and Expiation","trust":"trusted","unresolved_branch_citations":[{"citation":"ء ل ي/B007","reason":"no registered branch match"}],"unresolved_branch_refs":[]},{"anchor_refs":["88:17","88:23","88:25"],"branch_refs":["root_000065/B001","root_001684/B002","root_001684/B012"],"candidate_id":"cand_35a71a2826af60921ef3","commentary_obligation":"review","focus_branch_refs":["root_001684/B002","root_001684/B012"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000065/B001"],"root_ids":[],"scope":"pericope","source_local_id":"E:Endpoint, Homecoming, and Attainment","source_type":"channel","support_ids":["sup_1788d4e3a2b6dad95817","sup_1d057a7f7b755adc89b7","sup_af412afd1248453ef567","sup_b35576db6122b0333bd2","sup_d089418fbf4dc7ee4d05"],"title":"Endpoint, Homecoming, and Attainment","trust":"trusted","unresolved_branch_citations":[{"citation":"ء ل ي/B001","reason":"no registered branch match"}],"unresolved_branch_refs":[]},{"anchor_refs":["88:23","88:25","88:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:23","branch_refs":["root_000065/B001","root_000318/B001","root_001307/B005","root_001684/B007"],"candidate_id":"cand_bd9c6a892aaff4cff6cb","commentary_obligation":"review","hft_ref":"hft_7d026e47fa30824010d2","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_return_cancels_exit","source_type":"hft","support_ids":["sup_af17eee031fdcbe1d3e6"],"title":"d_return_cancels_exit","trust":"legacy_unbound"},{"anchor_refs":["88:17","88:23","88:25"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:23","branch_refs":["root_000006/B004","root_000065/B003","root_001307/B001","root_001684/B011"],"candidate_id":"cand_f3867b72479dda30b840","commentary_obligation":"review","hft_ref":"hft_b7e76aadee3dcb193ba0","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_under_saddle_burden","source_type":"hft","support_ids":["sup_d8d61ae7f0534b9fac9d"],"title":"o_under_saddle_burden","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_228cb29c48b4fdc76082","connection_ref":"conn_b56435a6f496489f2afa","note":"The immediate return clause specifies the next frame after the exception.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_66e9006e7bdb34947195","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:25","source_note":"Immediately supplies the turning-away and denial addressed by f01.","source_row_role":"ranked_review","source_target_component_ref":"88:23","source_target_components":["88:23"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:23"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:25","source_target_components":["88:25"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:25","target_evidence":{"arabic_uthmani":"إِنَّ إِلَيْنَآ إِيَابَهُمْ","ayah_ref":"88:25"},"target_ref":"88:25"},{"connection_evidence_ref":"conn_ev_77d106d24428500126f7","connection_ref":"conn_740287a487b2b955fbec","note":"The immediately following maximum-punishment clause completes 88:23's consequence.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_7fa510ffa0c2257002d1","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:24","source_note":"States the immediate condition, turning away and disbelief, before the focus.","source_row_role":"ranked_review","source_target_component_ref":"88:23","source_target_components":["88:23"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:23"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:24","source_target_components":["88:24"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:24","target_evidence":{"arabic_uthmani":"فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ","ayah_ref":"88:24"},"target_ref":"88:24"},{"connection_evidence_ref":"conn_ev_101d4653cfccf51079e3","connection_ref":"conn_121e1c8bfae18e625c32","note":"One of the immediately preceding observation-signs that f01 treats as the refused evidence.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_d35735f0b11145aac17b","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"88:19","source_note":"No distinct addition to the mountain's placement or function.","source_row_role":"ranked_review","source_target_component_ref":"88:23","source_target_components":["88:23"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:23"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:19","source_target_components":["88:19"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:19","target_evidence":{"arabic_uthmani":"وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ","ayah_ref":"88:19"},"target_ref":"88:19"},{"connection_evidence_ref":"conn_ev_6dfba0a2e93bb1399164","connection_ref":"conn_b963045fa95ee98fc204","note":"Another preceding observation-sign; redundant after 88:19.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_fc2ec8abc38553756567","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"88:18","source_note":"Rejection context adds no distinct contribution to 88:18.","source_row_role":"ranked_review","source_target_component_ref":"88:23","source_target_components":["88:23"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:23"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:18","source_target_components":["88:18"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:18","target_evidence":{"arabic_uthmani":"وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ","ayah_ref":"88:18"},"target_ref":"88:18"},{"connection_evidence_ref":"conn_ev_b2d71ed57589f140a88b","connection_ref":"conn_f27dc6300e0dbc88af0f","note":"A further observation-sign, now redundant within the same immediate sequence.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_bbdf0bc7c0c5cf77adfb","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"88:20","source_note":"Nearby refusal is consequence framing, not an added reading of earth.","source_row_role":"ranked_review","source_target_component_ref":"88:23","source_target_components":["88:23"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:23"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:20","source_target_components":["88:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:20","target_evidence":{"arabic_uthmani":"وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ","ayah_ref":"88:20"},"target_ref":"88:20"},{"connection_evidence_ref":"conn_ev_9f50e742f5711e9a9c3c","connection_ref":"conn_7097f4e3fd4f9c4bae74","note":"The opening observation-command directly anchors f01's already-opened evidence.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_52dd9d90c93f906be9f2","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"88:17","source_note":"Rejection and disbelief do not clarify the observational instruction.","source_row_role":"ranked_review","source_target_component_ref":"88:23","source_target_components":["88:23"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:23"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:17","source_target_components":["88:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:17","target_evidence":{"arabic_uthmani":"أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ","ayah_ref":"88:17"},"target_ref":"88:17"},{"connection_evidence_ref":"conn_ev_800997348b8cf369f143","connection_ref":"conn_3f4c657af7f830a1074a","note":"Missing immediate command to remind; it establishes the function preceding the exception.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:21","source_target_components":["88:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:21","target_evidence":{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","ayah_ref":"88:21"},"target_ref":"88:21"},{"connection_evidence_ref":"conn_ev_56af67c2e83742f9d70f","connection_ref":"conn_a11768f1b132d4f1a1e7","note":"Missing immediate non-controller boundary for the addressee.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":true,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_6c7516607e168509477f","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:22","source_note":"The exception identifies turning away and disbelief as the response whose punishment remains Allah's.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:23","source_target_components":["88:23"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:23"}],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:22","source_target_components":["88:22"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:22","target_evidence":{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","ayah_ref":"88:22"},"target_ref":"88:22"},{"connection_evidence_ref":"conn_ev_864d098f79ee95bb0c7c","connection_ref":"conn_7ffe08f98918b652b2c5","note":"Missing immediate accounting clause completing 88:23-25's return-and-punishment sequence.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:26","source_target_components":["88:26"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:26","target_evidence":{"arabic_uthmani":"ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم","ayah_ref":"88:26"},"target_ref":"88:26"}],"focus":{"arabic_uthmani":"إِلَّا مَن تَوَلَّىٰ وَكَفَرَ","qac_morphemes":[{"lemma_ar":"إِلَّا","morph_features":"STEM|POS:EXP|LEM:<il~aA","morpheme_role":"STEM","pos":"EXP","qac_ref":"88:23:1:1","qac_word_ref":"88:23:1","root_ar":"","surface_ar":"إِلَّا"},{"lemma_ar":"مَن","morph_features":"STEM|POS:REL|LEM:man","morpheme_role":"STEM","pos":"REL","qac_ref":"88:23:2:1","qac_word_ref":"88:23:2","root_ar":"","surface_ar":"مَن"},{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","root_ar":"و ل ي","surface_ar":"تَوَلَّىٰ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:23:4:1","qac_word_ref":"88:23:4","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","root_ar":"ك ف ر","surface_ar":"كَفَرَ"}],"word_analysis_qac_refs":[["88:23:1:1"],["88:23:2:1"],["88:23:3:1"],["88:23:4:1"],["88:23:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:23:1","88:23:2","88:23:3","88:23:4","88:23:5"]},"focus_surface_evidence":{"arabic_uthmani":"إِلَّا مَن تَوَلَّىٰ وَكَفَرَ","qac_morphemes":[{"lemma_ar":"إِلَّا","morph_features":"STEM|POS:EXP|LEM:<il~aA","morpheme_role":"STEM","pos":"EXP","qac_ref":"88:23:1:1","qac_word_ref":"88:23:1","root_ar":"","surface_ar":"إِلَّا"},{"lemma_ar":"مَن","morph_features":"STEM|POS:REL|LEM:man","morpheme_role":"STEM","pos":"REL","qac_ref":"88:23:2:1","qac_word_ref":"88:23:2","root_ar":"","surface_ar":"مَن"},{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:3:1","qac_word_ref":"88:23:3","root_ar":"و ل ي","surface_ar":"تَوَلَّىٰ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:23:4:1","qac_word_ref":"88:23:4","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"كَفَرَ","morph_features":"STEM|POS:V|PERF|LEM:kafara|ROOT:kfr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:23:4:2","qac_word_ref":"88:23:4","root_ar":"ك ف ر","surface_ar":"كَفَرَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:23:1:1"],["88:23:2:1"],["88:23:3:1"],["88:23:4:1"],["88:23:4:2"]],"word_analysis_refs":["88:23:1","88:23:2","88:23:3","88:23:4","88:23:5"],"word_rows":[{"analysis_record_ref":"88:23:1","analytic_gloss_range_en":"exceptive or adversative boundary particle tying the refuser clause to the prior denial of coercive control and opening a consequence-bearing exception","analytic_root_gloss_range_en":null,"qac_refs":["88:23:1:1"],"root":{},"surface":{"arabic":"إِلَّا","transliteration":"illā"}},{"analysis_record_ref":"88:23:2","analytic_gloss_range_en":"indefinite human relative or conditional head; locally singular in grammar but open as a portable behavior-defined person from the prior plural domain","analytic_root_gloss_range_en":null,"qac_refs":["88:23:2:1"],"root":{},"surface":{"arabic":"مَن","transliteration":"man"}},{"analysis_record_ref":"88:23:3","analytic_gloss_range_en":"Form V perfect turning away or self-reorientation; locally objectless withdrawal from reminder, address, and truth, with nearness, allegiance, and authority branches narrowed to relational pressure rather than separate active senses","analytic_root_gloss_range_en":"broad range around nearness, succession, authority, loyal alliance, facing, and turning away; this occurrence selects turning away while allowing relation and allegiance pressure under that sense","qac_refs":["88:23:3:1"],"root":{"arabic":"و ل ي","transliteration":"w-l-y"},"surface":{"arabic":"تَوَلَّىٰ","transliteration":"tawallā"}},{"analysis_record_ref":"88:23:4","analytic_gloss_range_en":"coordinating conjunction joining the second perfect predicate to the first under the same human subject; locally additive and binding, not an explicit marker of temporal sequence","analytic_root_gloss_range_en":null,"qac_refs":["88:23:4:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"88:23:5","analytic_gloss_range_en":"Form I perfect active denial or unbelief as covered recognition; locally objectless, morally accountable, and the closing second predicate of the refusal profile","analytic_root_gloss_range_en":"broad covering range including concealment, rejecting truth, ingratitude, disavowal, expiation, and other concrete covering branches; this occurrence selects religious denial while retaining the covering image and acknowledgment-refusal pressure","qac_refs":["88:23:4:2"],"root":{"arabic":"ك ف ر","transliteration":"k-f-r"},"surface":{"arabic":"كَفَرَ","transliteration":"kafara"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":4,"missing_anchor_refs":[],"supplied_unique_anchor_count":4},"assigned_record_count":2,"assigned_records":[{"anchor_refs":["88:23","88:25","88:26"],"branch_refs":["root_000065/B001","root_000318/B001","root_001307/B005","root_001684/B007"],"candidate_id":"cand_bd9c6a892aaff4cff6cb","evidence_scope":"declared_pericope","hft_ref":"hft_7d026e47fa30824010d2","item_id":"d_return_cancels_exit","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_return_cancels_exit","support_id":"sup_af17eee031fdcbe1d3e6"},{"anchor_refs":["88:17","88:23","88:25"],"branch_refs":["root_000006/B004","root_000065/B003","root_001307/B001","root_001684/B011"],"candidate_id":"cand_f3867b72479dda30b840","evidence_scope":"declared_pericope","hft_ref":"hft_b7e76aadee3dcb193ba0","item_id":"o_under_saddle_burden","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_under_saddle_burden","support_id":"sup_d8d61ae7f0534b9fac9d"}],"diagnostics":[],"lane_counts":{"global":18,"macro":2,"micro":4},"packet_summary":{"ayah_count":26,"focus_ref":"88:23","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:23","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"88:23","lane":"macro","linguistic_source_ref":"88:23","surface_ref":"88:23","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:23","target_tokens":[["Ancak",["88:23:1"]],["kim",["88:23:2"]],["yüz",["88:23:3"]],["çevirir",["88:23:3"]],["ve",["88:23:4"]],["inkâr",["88:23:4"]],["ederse",["88:23:4"]]],"text":"Ancak kim yüz çevirir ve inkâr ederse,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":2,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":17,"ayah_to":26,"id":"s088-p02-017-026","label":"Creation signs and the duty to remind","number":2,"refs":["88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"88:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"88:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["88:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"88:0"}],"support_registry":[{"branch_refs":["root_000047/B002","root_001307/B009","root_001684/B013"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"D:Oath and Expiation","source_type":"channel","support_id":"sup_0c6dae45056bdd70f0cd","text":"oath `ء ل ي:B007/m01`; divine invocation `ء ل ه:B002/m01`; expiation `ك ف ر:B009/m01`; assigned pledge `و ل ي:B013/m02`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Disbelief and Ingratitude","source_type":"channel","support_id":"sup_0f6695f9ff21df865be3","text":"88:23 `وكفر` (`ك ف ر`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"E:Endpoint, Homecoming, and Attainment","source_type":"channel","support_id":"sup_1788d4e3a2b6dad95817","text":"A terminal limit, a place of return, and attained possession give directed movement its completed outcome.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"E:Endpoint, Homecoming, and Attainment","source_type":"channel","support_id":"sup_1d057a7f7b755adc89b7","text":"88:17-20 `إلى` and 88:25 `إلينا` (`ء ل ي`); 88:25 `إيابهم` (`ء و ب`); 88:23 `تولى` (`و ل ي`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Disbelief and Ingratitude","source_type":"channel","support_id":"sup_1fb8fb01b284d4088a31","text":"A recipient covers or denies a recognized truth and the benefit that should have elicited gratitude.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Goat and Separated Young Stock","source_type":"channel","support_id":"sup_281c2464617b0da80fe3","text":"Age classification becomes a management practice when young stock are sorted from the larger herd.","trust":"trusted"},{"branch_refs":["root_001307/B003","root_001307/B004","root_001307/B006"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"B:Disbelief and Ingratitude","source_type":"channel","support_id":"sup_64449116e4f17ecfc878","text":"explicit disbelief `ك ف ر:B003/m01`; ingratitude or covering benefit `ك ف ر:B004/m02`; settled unbelief `ك ف ر:B006/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Oath and Expiation","source_type":"channel","support_id":"sup_6ee9761fc619b8e6dbee","text":"A person directs worship, sacrifice, blessing, or sworn obligation toward a sacred addressee and becomes answerable for the act.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Goat and Separated Young Stock","source_type":"channel","support_id":"sup_947424e6de401bf25361","text":"Animals outside ordinary domestic use are pursued, trapped, classified, or distinguished by age and form.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Oath and Expiation","source_type":"channel","support_id":"sup_a842245d16d4b249e9bf","text":"Invocation, commitment, assigned liability, and expiation form a complete cycle of sworn responsibility.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Goat and Separated Young Stock","source_type":"channel","support_id":"sup_a98cadbae3c48dbad291","text":"88:20 `سطحت` (`س ط ر`); 88:23 `تولى` (`و ل ي`); 88:17 `الإبل` (`ء ب ل`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"E:Endpoint, Homecoming, and Attainment","source_type":"channel","support_id":"sup_af412afd1248453ef567","text":"Movement terminates at a homeward destination or achieved goal.","trust":"trusted"},{"branch_refs":["root_000065/B001","root_001684/B002","root_001684/B012"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"E:Endpoint, Homecoming, and Attainment","source_type":"channel","support_id":"sup_b35576db6122b0333bd2","text":"endpoint and termination `ء ل ي:B001/m01`; homeward return `ء و ب:B001/m01`; attaining and taking possession `و ل ي:B012/m01`; ordered succession toward a goal `و ل ي:B002/m01`","trust":"trusted"},{"branch_refs":["root_000006/B003","root_000704/B007","root_001684/B015"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"D:Goat and Separated Young Stock","source_type":"channel","support_id":"sup_c10ff24f40bd6b5ad803","text":"young goat `س ط ر:B007/m01`; separated young livestock `و ل ي:B015/m02`; herd group `ء ب ل:B003/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"E:Endpoint, Homecoming, and Attainment","source_type":"channel","support_id":"sup_d089418fbf4dc7ee4d05","text":"Movement is oriented along a route toward arrival, an endpoint, or a return.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Disbelief and Ingratitude","source_type":"channel","support_id":"sup_e7b764fb3a24b15714db","text":"A person rejects rightful orientation through pride, disbelief, or disavowal and thereby enters a corresponding field of blame and punishment.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Oath and Expiation","source_type":"channel","support_id":"sup_e9448aa2ee4d33b4c162","text":"88:17-20, 88:25 `إلى`, `إلينا` (`ء ل ي`); 88:24 `الله` (`ء ل ه`); 88:23 `كفر` (`ك ف ر`); 88:23 `تولى` (`و ل ي`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Disbelief and Ingratitude","source_type":"channel","support_id":"sup_ec4ab63a498046d0871a","text":"The same refusal can target truth as disbelief or target received good as ingratitude.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Oath and Expiation","source_type":"channel","support_id":"sup_ec815253d8cf81dfa4ad","text":"A speaker invokes the divine name, assumes a sworn obligation, and must discharge or expiate it.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Goat and Separated Young Stock","source_type":"channel","support_id":"sup_eca1cccf8c6ad967ef3e","text":"Young animals are identified, divided from the main herd, and managed as a distinct group.","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"إِلَّا مَن تَوَلَّىٰ وَكَفَرَ","ayah_ref":"88:23"},{"arabic_uthmani":"إِنَّ إِلَيْنَآ إِيَابَهُمْ","ayah_ref":"88:25"},{"arabic_uthmani":"ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم","ayah_ref":"88:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000065/B001","root_000318/B001","root_001307/B005","root_001684/B007"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_001684","role":"Turning away supplies the apparent outbound motion that the closing return reverses.","root":"و ل ي","source_ref":"88:23","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_001307","role":"Disavowal supplies the attempted severance that accounting refuses to treat as a vanished relation.","root":"ك ف ر","source_ref":"88:23","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000065","role":"Return to a destination folds the person's apparent exit back toward the speaker's domain.","root":"ء و ب","source_ref":"88:25","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000318","role":"Counting and accounting preserve the acts as liabilities even after the person disowns the bond.","root":"ح س ب","source_ref":"88:26","source_word_indices":["4"]}],"changed_reading":{"after":"The turn is only an outbound leg: return cancels spatial escape, and accounting cancels the attempted social or epistemic disavowal.","before":"The person turns away and successfully terminates the relation."},"confidence":"strong","mechanism":"The closing return and accounting reverse both verbs of the focus clause. Withdrawal fails to become escape because it bends into return; disavowal fails to dissolve relation because every act remains countable.","model_id":"d_return_cancels_exit","reader_inference":"The packet supplies withdrawal, disavowal, return, and counting; I supply the failed-exit trajectory linking them. The alternative is that return and account are general closure and do not specifically reverse the two focus verbs.","status":"strengthened","structural_cues":["The three-clause close moves from turning away, to return toward 'Us,' to an account borne by 'Us.'","The possessive plurals in 88:25-26 keep the refusers grammatically held after their attempted withdrawal."],"trigger_roots":["ء و ب","ح س ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_return_cancels_exit","source_type":"hft","support_id":"sup_af17eee031fdcbe1d3e6","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ","ayah_ref":"88:17"},{"arabic_uthmani":"إِلَّا مَن تَوَلَّىٰ وَكَفَرَ","ayah_ref":"88:23"},{"arabic_uthmani":"إِنَّ إِلَيْنَآ إِيَابَهُمْ","ayah_ref":"88:25"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000006/B004","root_000065/B003","root_001307/B001","root_001684/B011"],"payload":{"activation_trace":[{"branch_id":"B011","mapped_root_id":"root_001684","role":"The cloth beneath a saddle supplies a hidden interface that receives and transmits load.","root":"و ل ي","source_ref":"88:23","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001307","role":"Literal covering makes the burden-bearing layer invisible without removing its pressure.","root":"ك ف ر","source_ref":"88:23","source_word_indices":["4"]},{"branch_id":"B004","mapped_root_id":"root_000006","role":"Burden and liability in the camel field supply what the hidden layer continues to carry.","root":"ء ب ل","source_ref":"88:17","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_000065","role":"Repeated bodily movement in travel and return supplies the route across which the concealed load persists.","root":"ء و ب","source_ref":"88:25","source_word_indices":["3"]}],"changed_reading":{"after":"As a contained camel-load image, the covered burden remains in transmission beneath the journey and comes back with the returning traveler.","before":"Turning away appears to shed the burden, and covering appears to erase it."},"confidence":"exploratory","containment":"This is surprising because the under-saddle cloth is a remote nominal branch and cannot translate تَوَلَّىٰ. It remains visibly anchored through the focus cover branch, the packet's camel liability branch, and the closing travel-return image. Downstream prose should present it only as a material topology of hidden burden: a covered layer carries pressure through departure and return.","focus_anchor":"The focus root و ل ي contains an under-saddle layer, while ك ف ر supplies literal covering.","outlier_id":"o_under_saddle_burden"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_under_saddle_burden","source_type":"hft","support_id":"sup_d8d61ae7f0534b9fac9d","trust":"legacy_unbound"}]}
</lane_packet_json>
