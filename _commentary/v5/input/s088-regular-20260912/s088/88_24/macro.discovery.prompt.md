# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **88:24**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_24/macro.discovery.json` and modify nothing
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
  "ayah_ref": "88:24",
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
{"branch_registry":[{"boundary":"the earth/ground itself, and by extension the lower part of a thing, including an animal's lower legs or hoof-ground side","branch_kind":null,"branch_ref":"root_000025/B001","candidate_links":[{"candidate_id":"cand_0bb75bdb84d64cf1228b","lane":"macro"}],"focus_root_occurrences":[],"gloss":"the lower ground opposite the sky","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"السفل المقابل للسماء","image_en":"the lower ground opposite the sky"}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"السفل المقابل للسماء","image_en":"the lower ground opposite the sky","scope_ar":"الأرض التي نحن عليها؛ كل ما سفل وقابل السماء؛ أسفل الشيء وقوائم الدابة وما يلي الأرض منها","scope_en":"the earth/ground itself, and by extension the lower part of a thing, including an animal's lower legs or hoof-ground side"},"support_links":["sup_af13f67dc9e4f4f956e8"]},{"boundary":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"88:24:2:1","qac_word_ref":"88:24:2","surface_ar":"ٱللَّهُ"}],"gloss":"tapınma ve tapınılan varlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylem çekirdeğiyle ondan türeyen tapınılan varlık anlamının birlikte temsil edilmesi gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_image_ar":"التعبد والمعبود","concept_gloss":"tapınma ve tapınılan varlık","contextual_glosses":[{"applicability":"Bir kişinin tapınma eylemini veya kendini tapınmaya vermesini bildiren eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylem olarak tapınma çekirdeğini eksiksiz korur."},"facet_ids":["F001"],"text":"tapınmak","usage_role":"general"},{"applicability":"Bir topluluğun kendisine tapındığı varlık veya nesneden söz edilen ad bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tapınmanın yöneldiği varlık veya nesne anlamını korur."},"facet_ids":["F002"],"text":"tapınılan varlık","usage_role":"contextual"},{"applicability":"Bir varlığın başkalarına tapınma konusu olarak benimsetilmesini anlatan ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir varlığı tapınma konusu durumuna getirme işlemini korur."},"facet_ids":["F003"],"text":"tapınılır kılmak","usage_role":"explanatory"}],"definition":"Bir varlığa tapınma eylemini ve kişinin kendini tapınmaya vermesini anlatır. Türemiş kullanımlarda bir varlığı tapınılır kılmayı, tapınılan varlığı ve tapınma konusu sayılan varlıkları da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."},{"facet_id":"F002","role":"extension","statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."},{"facet_id":"F003","role":"specialization","statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."},{"facet_id":"F004","role":"example","statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca belirli bir varlık türünü adlandırdığı için bütün dalın karşılığı sanılabilir.","fit":"narrowing","loses":"Tapınma eylemini, kişinin tapınmaya yönelmesini ve tapınılır kılma işlemini karşılamaz.","preserves":"Tapınılan varlık anlamını kısa ve doğal biçimde korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi tapınma eylemini, kişinin kendini tapınmaya vermesini, bir varlığı tapınılır kılmayı ve tapınılan varlığı aynı anlam örgüsü içinde açıkça birleştirir. Geçici dal çerçevesi bu çekirdeği ve ondan türeyen varlık adlarını doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tapınmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kendini tapınmaya vermek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tapınılır kılmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"tapınılan varlık, tanrı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"tapınılan varlık"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"tanrılar, tapınılan nesneler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"tapınma"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kimi toplulukların tapındığı için bu adla anılan güneş"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"senin tapınman"}],"lexicalization_note":"Tanım, yalın eylem çekirdeğini türemiş eylem ve varlık adlarından ayırır; türemiş biçimlerin kapsamı yalın eylemin tamamına aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Tapınma eylemi, korkuya bağlı özel tapınma yaşayışı ve aynı kökün özel ad dalı sınırı keskinleştirdi; peygamberlik, büyücülük, belirli tapınma nesneleri, sahiplik ve tarihsel hizmet grubu adayları ise yalnızca aynı dinsel alana veya tekil örneklere temas ettiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal eylem ve yaklaşma yönünde yoğunlaşırken bu dal aynı çekirdekten tapınılan varlık ile ettirgen kılma anlamlarını da türetir; bu yüzden yalnızca eylem bağlamında yakınlaşırlar.","focus_only":"Tapınılan varlığı ve bir varlığı tapınılır kılma işlemini de adlandırır.","gloss":"tapınma ve yaklaşarak yönelme","neighbor_only":"Tapınmayla birlikte yaklaşma ve kendini bu işe verme yönünü öne çıkarır.","neighbor_ref":"root_001498/B001","relation_type":"near_synonym","shared_zone":"İki dal da tapınma eylemini ve kişinin bu eyleme yönelmesini kapsar."},{"boundary_match":"partial","distinction":"Bu dal genel tapınma çekirdeğini ve ondan türeyen varlık anlamlarını kapsar; komşu dal ise korku, inziva ve olağanın üstündeki uygulamalarla sınırlı özel bir yaşayışı anlatır.","focus_only":"Tapınmayı korku, inziva veya aşırı uygulama koşuluna bağlamaz ve tapınılan varlığı da adlandırabilir.","gloss":"korkuyla yoğunlaşan özel tapınma yaşayışı","neighbor_only":"Korkudan doğan, inziva veya ek yüklenme biçimindeki özel bir tapınma yaşayışını bildirir.","neighbor_ref":"root_000604/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kişinin kendini tapınmaya vermesi bulunur."},{"boundary_match":"partial","distinction":"Bu dal genel anlam örgüsünü verir; komşu dal ise o örgüden türemiş özel adı ve adın belirli söz kalıplarındaki kullanımını ayrı bir biçim alanı olarak sınırlar.","focus_only":"Genel tapınma eylemini, tapınılan varlığı ve tapınılır kılmayı kapsar.","gloss":"Yaratıcıya özgü ad ve kullanım kalıpları","neighbor_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek ve ant kalıplarını kapsar.","neighbor_ref":"root_000047/B002","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlık düşüncesi üzerinden bu dalın varlık anlamıyla bağlantılıdır."}],"source_phrase_ar":"أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)","source_summary":"Kaynakların ortak çizgisi, tapınmayı anlamın temeli sayar; kişinin tapınmaya yönelmesini, tapınılan varlığı ve tapınılır kılma işlemini bu temelden türetir. Tapınma konusu sayılan yontular ve güneş örneği, varlık anlamının belirli uygulamalarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.","what_is_not_ar":"لا يدخل فيه أله بمعنى تحير، ولا ألهت على فلان بمعنى اشتد جزعي عليه، ولا أسماء المواضع أو الحية أو الهلال إلا من جهة التسمية لا معنى العبادة."},"support_links":[]},{"boundary":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B002","candidate_links":[{"candidate_id":"cand_d4f39ffb0b40140e2a26","lane":"macro"},{"candidate_id":"cand_a3eb339df6f5c9fde9b0","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"88:24:2:1","qac_word_ref":"88:24:2","surface_ar":"ٱللَّهُ"}],"gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel adın kendisiyle ona bağlı seslenme, dilek ve ant kullanımlarının birlikte açıklanması gereken dal düzeyinde kullanılır.","boundary_detail":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_image_ar":"اسم الله في القسم والنداء","concept_gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","contextual_glosses":[{"applicability":"Söz konusu adın yalnız Yaratıcıyı gösteren yalın ad olarak ele alındığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın Yaratıcıya özgü olmasını ve ayırt edici ad işlevini korur."},"facet_ids":["F001"],"text":"Yaratıcı'nın özel adı","usage_role":"general"},{"applicability":"Yakarış veya dilek sırasında Yaratıcıya doğrudan seslenilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya yöneltilen doğrudan seslenme işlevini doğal biçimde korur."},"facet_ids":["F004"],"text":"ey Tanrı","usage_role":"contextual"},{"applicability":"Özel adın bir bildirimin doğruluğunu pekiştiren ant değeri taşıdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya dayanarak ant verme işlevini açık biçimde korur."},"facet_ids":["F003"],"text":"Tanrı adına ant olsun","usage_role":"contextual"},{"applicability":"Özel adın ses veya parçaları düşürülmüş tarihsel kalıplarının işlevini açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kısaltılma biçimini ve şaşma ya da ant işlevini birlikte korur."},"facet_ids":["F005"],"text":"kısaltılmış şaşma veya ant sözü","usage_role":"explanatory"}],"definition":"Yaratıcıya özgü adın kendisini ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar. Bu biçimler doğrudan seslenme, adın ant değeriyle kullanılması veya ses ve parçaların düşürülmesiyle kısaltılma yollarını gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."},{"facet_id":"F002","role":"source_variant","statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."},{"facet_id":"F003","role":"associated_use","statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."},{"facet_id":"F004","role":"associated_use","statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."},{"facet_id":"F005","role":"source_variant","statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Genel tür adı olarak başka tapınılan varlıklar için de kullanılabildiğinden özel adla karışır.","fit":"narrowing","loses":"Adın tek bir varlığa özgü özel ad oluşunu ve seslenme ile ant biçimlerini karşılamaz.","preserves":"Yüce bir tapınılan varlığa gönderimde bulunma yönünü korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi Yaratıcıya özgü adın kendisini, genel tapınılan-varlık adından türetiliş açıklamasını ve bu özel adla kurulan seslenme ile ant biçimlerini birlikte verir. Geçici çerçeve kullanılabilir, ancak dal yalnızca seslenme ve ant kalıpları değildir; özel adın yalın kullanımı da çekirdekte tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"Yaratıcıya özgü ad"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"Tanrı adına ant olsun, bunu yapmadım"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ey Tanrı; yakarma seslenişi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ey Tanrı; doğrudan seslenme"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"Tanrı adına sen veya baban; şaşma ya da ant kalıbı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları"}],"lexicalization_note":"Yalın özel ad, doğrudan seslenme biçimleri ve ant ya da şaşma kalıpları ayrı tutulur; kalıplara özgü işlevler özel adın her kullanımına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Genel tapınma dalı, yaşam üzerine ant, genel seslenme, kısaltılmış kişi seslenmesi ve yakarışa karşılık sözü gerçek sınır karşılaştırmaları sağladı; baba hitapları, genel dışlama yapıları, başka ant sözleri ve sesçe eşlik eden kalıplar daha zayıf ya da yalnızca biçimsel temas gösterdiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir özel adın biçim ve kullanım alanıdır; komşu dal ise özel adla sınırlanmayan genel tapınma eylemini ve tapınılan varlık anlamını verir.","focus_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar.","gloss":"tapınma ve tapınılan varlık","neighbor_only":"Genel tapınma eylemini, tapınılan varlığı ve bir varlığı tapınılır kılma işlemini kapsar.","neighbor_ref":"root_000047/B001","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlığı göstermesi bakımından genel varlık anlamına dayanır."},{"boundary_match":"partial","distinction":"Ortak işlev ant vermedir, fakat bu dalın dayanağı Yaratıcıya özgü addır; komşu dal yaşam süresini bildiren sözleri kullanır ve ayrıca ısrarlı istemeye uzanabilir.","focus_only":"Ant işlevini Yaratıcıya özgü adın yalın veya kısalmış biçimleriyle kurar.","gloss":"ömür üzerine ant ve ısrarlı isteme","neighbor_only":"Ant veya ısrarlı isteme işlevini yaşam süresini bildiren sözlerle kurar.","neighbor_ref":"root_001044/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir sözü güçlendiren ant işlevli kalıplar içerir."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir muhatabın özel adı çevresinde oluşur; komşu dal ise muhatabın kimliğinden bağımsız genel seslenme araçlarını ve uzaklık ayrımını konu edinir.","focus_only":"Belirli bir özel adı ve o adın yakarma ile ant kullanımlarını içerir.","gloss":"genel seslenme öğeleri","neighbor_only":"Yakın veya uzaktaki muhataba yöneltilen genel seslenme öğelerini bildirir.","neighbor_ref":"root_000074/B008","relation_type":"same_field","shared_zone":"Her iki dal da doğrudan seslenme sırasında kullanılan biçimlerle ilgilidir."},{"boundary_match":"field_only","distinction":"Bu dalın kısalmaları belirli özel adın dinsel seslenme ve ant işlevlerine bağlıdır; komşu dalın kısalmaları ise belirsiz bir kişiye seslenmenin dilbilgisel biçimleridir.","focus_only":"Yaratıcıya özgü adı ve ona bağlı seslenme ile ant biçimlerini kapsar.","gloss":"kişiye yönelik kısaltılmış seslenme","neighbor_only":"Belirsiz bir kişiye yönelen kısaltılmış seslenme biçimlerini kapsar.","neighbor_ref":"root_001178/B003","relation_type":"same_field","shared_zone":"Her iki dalda da seslenme sırasında biçimsel kısalma görülebilir."},{"boundary_match":"thematic_only","distinction":"Bu dal bir muhataba seslenir; komşu dal ise söylenmiş yakarışa kabul dileği veya onayla karşılık verir. Aynı sahnede bulunsalar da anlam çekirdekleri örtüşmez.","focus_only":"Yakarışın yöneltildiği Yaratıcıyı özel adıyla çağırır.","gloss":"yakarışın kabulünü isteyen karşılık","neighbor_only":"Yakarışın kabul edilmesini isteyen veya söyleneni onaylayan karşılık sözünü bildirir.","neighbor_ref":"root_000054/B003","relation_type":"thematic","shared_zone":"İki dal da yakarış ortamında kullanılan kısa söz biçimlerine katılır."}],"source_phrase_ar":"فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)","source_summary":"Kaynaklar özel adı Yaratıcıya özgü bir ad olarak tanımlar ve onu tapınılan varlığı gösteren genel adla köken bakımından ilişkilendirir. Aynı adın doğrudan seslenmede, yakarmada, ant bildiriminde ve parçaları düşürülmüş kalıplarda kullanıldığı birlikte gösterilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.","what_is_not_ar":"ليس فرعا مستقلا عن معنى الإله المعبود من جهة الاشتقاق، ولا يدخل فيه إطلاق إله أو آلهة على كل معبود إذا لم يكن الكلام على صيغة الاسم أو النداء أو القسم."},"support_links":["sup_2bd954b82da380d10d2a","sup_4c37eec3c70b74c43d7f"]},{"boundary":"The sky or any upper covering/surface, with source-attested extensions to cloud, rain, vegetation from rain, and an animal's upper back.","branch_kind":null,"branch_ref":"root_000745/B004","candidate_links":[{"candidate_id":"cand_0bb75bdb84d64cf1228b","lane":"macro"}],"focus_root_occurrences":[],"gloss":"overhead sky and cover","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"السماء وما علا فأظل","image_en":"overhead sky and cover"}}],"root_ar":"س م و","root_id":"root_000745","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"السماء وما علا فأظل","image_en":"overhead sky and cover","scope_ar":"يدخل فيه السماء لما علا وأظل، والسقف، والسحاب، والمطر، والنبات المنسوب إلى المطر، وظهر الفرس أو أعلى الشيء.","scope_en":"The sky or any upper covering/surface, with source-attested extensions to cloud, rain, vegetation from rain, and an animal's upper back."},"support_links":["sup_af13f67dc9e4f4f956e8"]},{"boundary":"Çekirdek tat ve tüketim hoşluğudur; cezalandırma, yeme içmeden kesilme ve sudaki yabancı madde bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:24:1:2","qac_word_ref":"88:24:1","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:24:3:2","qac_word_ref":"88:24:3","surface_ar":"عَذَابَ"}],"gloss":"tatlı ve kolay tüketilen yiyecek ya da içecek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yiyecek veya içeceğin damakta hoş, tatlı ve kolay tüketilir olmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Su söz konusu olduğunda hoş içimin yanında tuzlu olmama niteliği belirgindir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli yapılarda tatlı su edinme veya arama ve bir şeyi tatlı sayma anlatılır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir ikili adlandırma tükürük ile şarabı birlikte bu hoşluk niteliği altında anar."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yiyecek ve içeceklerdeki ortak tat ve tüketim hoşluğu çekirdeğini, suyun tuzlu olmaması dahil, birlikte karşılar.","boundary_detail":"Çekirdek tat ve tüketim hoşluğudur; cezalandırma, yeme içmeden kesilme ve sudaki yabancı madde bu dala girmez.","branch_image_ar":"العذوبة والطيب في الماء والمطعوم","concept_gloss":"tatlı ve kolay tüketilen yiyecek ya da içecek","contextual_glosses":[{"applicability":"Suyun tuzlu olmayıp hoş ve kolay içilmesini anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka yiyecek ve içeceklere uzanan genel kapsamı dışarıda bırakır.","preserves":"Suyun tatlılığını ve hoş içimini eksiksiz korur."},"facet_ids":["F002"],"text":"tatlı ve içimi hoş su","usage_role":"contextual"},{"applicability":"Tatlı içme suyu bulma veya bir yerden böyle su sağlama yapılarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tatlı suyu amaç edinme ve onu sağlama işlemini korur."},"facet_ids":["F003"],"text":"tatlı su aramak","usage_role":"contextual"}],"definition":"Su başta olmak üzere bir yiyecek veya içeceğin tatlı, hoş ve kolay tüketilir olması; su için ayrıca tuzlu olmama niteliğini taşır. Bu niteliğe bağlı yapılar tatlı su edinmeyi, aramayı ya da bir şeyi tatlı saymayı anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yiyecek veya içeceğin damakta hoş, tatlı ve kolay tüketilir olmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Su söz konusu olduğunda hoş içimin yanında tuzlu olmama niteliği belirgindir."},{"facet_id":"F003","role":"associated_use","statement":"Belirli yapılarda tatlı su edinme veya arama ve bir şeyi tatlı sayma anlatılır."},{"facet_id":"F004","role":"source_variant","statement":"Bir ikili adlandırma tükürük ile şarabı birlikte bu hoşluk niteliği altında anar."}],"identity_rationale":"Yetkili ifade, suyun tatlı, hoş ve tuzlu olmayan niteliğini merkeze alırken kolay tüketilen başka yiyecek ve içecekleri de kapsar. Tatlı su arama, suyu tatlı bulma ve iki belirli sıvıyı birlikte adlandırma kullanımları bu niteliğe bağlı yan kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tatlı, hoş ve kolay tüketilir"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tatlılık ve içim hoşluğu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"suları tatlılaştı veya tatlı suya kavuştular"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"tatlı içme suyu aradılar veya sağladılar"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onu tatlı saydı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onun için şu kuyudan su çekilir"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birlikte anılan tükürük ve şarap"}],"lexicalization_note":"Tanım hem yalın nitelik bildiren biçimleri hem de tatlı su edinme, arama veya öyle sayma yapılarıyla sınırlı kullanımları ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tatlı su ve berrak içme suyu adayları sınırı en iyi gösterdiği için yayımlandı, ötekiler örnek, uzak alan veya aynı kökün ayrı dalıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yalnız tatlı su alanında odak dalıyla örtüşür; odak dalının yiyecek-içecek genellemesi ve niteliğe bağlı işlemleri komşunun sınırını aşar.","focus_only":"Odak dalı su dışındaki kolay tüketilen yiyecek ve içecekleri, ayrıca tatlı su edinme ve değerlendirme yapılarını da kapsar.","gloss":"tatlı su","neighbor_only":null,"neighbor_ref":"root_001137/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de tatlı, tuzlu olmayan ve hoş içilen suyu adlandırır."},{"boundary_match":"partial","distinction":"Odak dalında belirleyici eksen tatlılık ve tuzlu olmamadır; komşuda ise berraklıktan doğan içim kolaylığı öne çıkar.","focus_only":"Odak dalı berraklık şartı koymaz ve hoş tüketilen başka yiyecek ve içecekleri de kapsar.","gloss":"berrak ve kolay içilen su","neighbor_only":"Komşu dal içim kolaylığını özellikle suyun berraklığına bağlar.","neighbor_ref":"root_000638/B003","relation_type":"near_synonym","shared_zone":"Her ikisi de suyun zorlanmadan içilmesini ve damakta hoş olmasını kapsar."}],"source_phrase_ar":"عذب الماء عذوبة فهو عذب طيب (maqayis;ayn;tahdhib)؛ العذب ضد الملح وكل مستسيغ من طعام أو شراب (jamhara)؛ ماء عذب طيب بارد (mufradat)؛ استعذب القوم ماءهم إذا استقوه عذبا (sihah)","source_summary":"Kaynakların ortak çekirdeği tatlı, hoş ve kolay tüketilen su, yiyecek veya içecektir; su edinme, arama ve tatlı sayma kullanımları bu çekirdeğe bağlanır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الماء العذب الطيب والمستساغ من طعام أو شراب، والاستعذاب بمعنى طلب الماء العذب أو عده عذبا، وما ألحقته المصادر بالريق والخمر.","what_is_not_ar":"ليس العذاب والعقوبة، ولا الامتناع عن الأكل والشرب."},"support_links":[]},{"boundary":"Bu dal başkasını engellemekten değil, kişinin veya hayvanın fiilen yemeyip içmemesinden söz eder.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:24:1:2","qac_word_ref":"88:24:1","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:24:3:2","qac_word_ref":"88:24:3","surface_ar":"عَذَابَ"}],"gloss":"yemeden içmeden durma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan veya hayvan fiilen yiyecek ve içecek tüketmeden durur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanda yememenin nedeni özellikle şiddetli susuzluk olabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hal, geceyi hiçbir şey yemeden ve içmeden geçirmek biçiminde anlatılabilir."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya hayvanın tüketmeme halini, nedeni ve süresi ayrıca belirtilebilen genel bir karşılıkla verir.","boundary_detail":"Bu dal başkasını engellemekten değil, kişinin veya hayvanın fiilen yemeyip içmemesinden söz eder.","branch_image_ar":"العذوب امتناع الجسد عن الأكل والشرب","concept_gloss":"yemeden içmeden durma","contextual_glosses":[{"applicability":"Şiddetli susuzluk yüzünden yemeyen hayvanın anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İçmeme bileşenini ve neden belirtilmeyen kullanımları açıkça söylemez.","preserves":"Susuzluğun yol açtığı yememe durumunu korur."},"facet_ids":["F002"],"text":"susuzluktan yemiyor","usage_role":"contextual"},{"applicability":"Tüketmeme halinin gece boyunca sürdüğünü anlatan yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yememeyi, içmemeyi ve gece boyunca sürmeyi birlikte korur."},"facet_ids":["F001","F003"],"text":"geceyi yemeden içmeden geçirdi","usage_role":"contextual"}],"definition":"Bir insanın veya hayvanın, çoğu kez şiddetli susuzluk yüzünden, hiçbir şey yemeden ve içmeden durmasıdır. Bu hal bir gece boyunca sürme veya yemek karşısında belirsiz bir ara durumda kalma biçiminde de anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan veya hayvan fiilen yiyecek ve içecek tüketmeden durur."},{"facet_id":"F002","role":"specialization","statement":"Hayvanda yememenin nedeni özellikle şiddetli susuzluk olabilir."},{"facet_id":"F003","role":"associated_use","statement":"Hal, geceyi hiçbir şey yemeden ve içmeden geçirmek biçiminde anlatılabilir."}],"identity_rationale":"Yetkili ifade hayvan ya da insanın yemeden ve içmeden durduğu bir hali açıkça bildirir. Şiddetli susuzluk sık bir neden olsa da tüm tanıklarda zorunlu değildir; bu yüzden hal, açlık duygusuna veya dinî oruca indirgenmez.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"susuzluktan yemedi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yiyip içmeden duran"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yiyip içmeden duran"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yemekten kaçınır"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"geceyi yemeden içmeden geçirdi"}],"lexicalization_note":"Tanım, hal bildiren biçimleri ve hayvanın, insanın ya da gecenin özne olduğu belirli yapıları ayırarak birlikte kapsar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; oruç, açlık ve aynı kökün alıkoyma dalı en olası karışmaları gösterir, öteki adaylar neden, sonuç veya daha uzak bedensel alanlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bir canlıda gözlenen yememe-içmeme halidir; komşu ise iradeli veya kurallı bir kaçınma uygulamasını ve daha geniş yasak alanını anlatır.","focus_only":"Odak, hayvanda susuzluktan doğabilen ve amaç ya da kural gerektirmeyen bir tüketmeme halini de kapsar.","gloss":"oruç tutma","neighbor_only":"Komşu, amaçlı veya kurallı perhizde yiyecek ve içecek dışındaki yasaklardan da kaçınmayı kapsar.","neighbor_ref":"root_000894/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da belirli bir süre yiyecek ve içecekten uzak durma vardır."},{"boundary_match":"partial","distinction":"Açlık mide boşluğu ve duyumdur; odak ise açlık duyulsun ya da duyulmasın, yememe ve içmeme davranışının sürmesidir.","focus_only":"Odak, içmemeyi ve özellikle susuzluğun yemeyi durdurduğu hayvan davranışını da içerir.","gloss":"açlık","neighbor_only":"Komşu, boş midenin yarattığı açlık duyusunu ve aç kişi halini merkez alır.","neighbor_ref":"root_000278/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal yiyecek tüketilmemesiyle bağlantılı bedensel bir durumu anlatır."},{"boundary_match":"partial","distinction":"Odak sonucu oluşan yeme-içmeme halini adlandırır; komşu ise yönelinen şeyden çekilme veya birini çekme işlemini anlatır.","focus_only":"Odak, belirli bir nesneye yönelik iradeli vazgeçiş olmadan da görülen bedensel tüketmeme halidir.","gloss":"vazgeçme veya alıkoyma","neighbor_only":"Komşu, herhangi bir işten vazgeçmeyi veya başkasını o işten alıkoymayı kapsar.","neighbor_ref":"root_000994/B003","relation_type":"near_neighbor","shared_zone":"Yemekten uzak durma bağlamında iki dal yüzeyde birbirine yaklaşabilir."}],"source_phrase_ar":"عذب الحمار يعذب عذبا وعذوبا فهو عاذب وعذوب لا يأكل من شدة العطش (maqayis;ayn)؛ العذوب من الدواب وغيرها القائم الذي لا يأكل ولا يشرب (sihah)؛ بات عذوبا إذا لم يأكل شيئا ولم يشرب (tahdhib)","source_summary":"Tanıklıklar, insan veya hayvanın yemeyip içmediği hali ortaklaştırır; şiddetli susuzluk bunun belirgin fakat her kullanım için zorunlu olmayan nedenidir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه عذوب الحمار أو الفرس أو الرجل إذا لم يأكل ولم يشرب، خاصة من شدة العطش أو بوصف قائم لا يذوق شيئا.","what_is_not_ar":"ليس منع الغير عن الشيء ولا العذاب بمعنى العقوبة."},"support_links":[]},{"boundary":"Dal, tüketmeme halini değil bir hedefe yönelişin kesilmesini veya kestirilmesini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:24:1:2","qac_word_ref":"88:24:1","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:24:3:2","qac_word_ref":"88:24:3","surface_ar":"عَذَابَ"}],"gloss":"vazgeçme veya alıkoyma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Özne yöneldiği bir şeyden vazgeçer veya geri durur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi başkasını bir işten uzak tutar veya o işi ona bıraktırır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Alıkoyma, birini bir işten sütten keser gibi kesme biçiminde anlatılabilir."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın dönüşlü ve ettirgen iki katılımcı düzenini kısa ve doğal biçimde birlikte karşılar.","boundary_detail":"Dal, tüketmeme halini değil bir hedefe yönelişin kesilmesini veya kestirilmesini anlatır.","branch_image_ar":"الكف والمنع والفطام عن الشيء","concept_gloss":"vazgeçme veya alıkoyma","contextual_glosses":[{"applicability":"Öznenin bir konuyu veya davranışı kendi isteğiyle bıraktığı yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öznenin yöneldiği şeyden geri durmasını korur."},"facet_ids":["F001"],"text":"ondan vazgeçti","usage_role":"contextual"},{"applicability":"Bir kişinin başka bir kişiyi belirli bir işten uzak tuttuğu yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ettirgen katılımcı düzenini ve engellenen işi korur."},"facet_ids":["F002"],"text":"onu bu işten alıkoydu","usage_role":"contextual"}],"definition":"Bir şeyden vazgeçip ona yönelmeyi bırakmak veya bir başkasını o şeyden uzak tutup alıkoymaktır. Sütten kesmeye benzer biçimde bir alışkanlığı ya da işi kestirmek bu ikinci yönün özel bir anlatımıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Özne yöneldiği bir şeyden vazgeçer veya geri durur."},{"facet_id":"F002","role":"core","statement":"Bir kişi başkasını bir işten uzak tutar veya o işi ona bıraktırır."},{"facet_id":"F003","role":"specialization","statement":"Alıkoyma, birini bir işten sütten keser gibi kesme biçiminde anlatılabilir."}],"identity_rationale":"Yetkili ifade hem öznenin bir şeyden vazgeçmesini hem de bir başkasını ondan alıkoymasını açıkça bir araya getirir. Bir işten kesme ve sütten kesmeye benzetilen uzaklaştırma bu yön değişiminin özel gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"o şeyden vazgeçti"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kadınlardan söz etmekten kaçının"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"onu o işten alıkoydu"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"onu o işten kesti"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"senden vazgeçtim"}],"lexicalization_note":"Anlam belirli edatlı ve ettirgen yapılara bağlıdır; öznenin vazgeçmesi ile başkasını alıkoyması tanımda ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel geri durma ile geniş engelleme alanları yayımlandı, daha dar tutma ve ayırma adayları bunlara göre yinelenen ya da uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak, belirli yapılarda kendi vazgeçişiyle başkasını alıkoymayı eşler; komşu daha genel geri çekilme ve yüz çevirme alanına yayılır.","focus_only":"Odak, başkasını bir işten kesme ve sütten kesmeye benzer ettirgen alıkoyma kullanımını açıkça içerir.","gloss":"geri durma ve bırakma","neighbor_only":"Komşu, geri çekilmenin yanında bir işi bir yana bırakma ve evde kalma gibi daha geniş uzak durma görünümlerine uzanır.","neighbor_ref":"root_000906/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir şeye yönelişi kesme, ondan geri durma veya onu bırakma alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak yönelişin kesilmesine odaklanır; komşu ise fiziksel, hukuki veya kurumsal engel ve yasağı daha geniş bir çekirdek olarak taşır.","focus_only":"Odak, kişinin kendi isteğiyle vazgeçmesini ve kişisel bir ettirgen alıkoymayı kapsar.","gloss":"engelleme ve yasaklama","neighbor_only":"Komşu, giriş, çıkış veya eylem üzerinde engel, yasak, görevli ve yaptırım gibi kurumsal sınırlar da kurar.","neighbor_ref":"root_000002/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal bir kişinin belirli bir eylemi yapmasını önleme alanında buluşur."}],"source_phrase_ar":"أعذب عن الشيء إذا لها عنه وتركه (maqayis)؛ أعذب عن الشيء إذا امتنع عنه (jamhara;tahdhib)؛ أعذبته عن الأمر إذا منعته عنه (sihah)؛ عذبته تعذيبا كقولك فطمته عن هذا الأمر (ayn;tahdhib)","source_summary":"Ortak anlam, bir şeye yönelişi kesmektir; bu kesilme öznenin kendi vazgeçişi veya başka bir kişinin onu engellemesi biçiminde gerçekleşir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه أعذب عن الشيء إذا تركه أو امتنع عنه، وأعذب غيره أو عذبه إذا منعه، والفطام عن أمر، وصيغة أعذبوا عن النساء في الذكر.","what_is_not_ar":"ليس العذوبة في الماء، ولا العقوبة والإيجاع."},"support_links":[]},{"boundary":"Genel çıplaklıktan daha dardır: belirleyici koşul, varlıkla gökyüzü arasındaki üst örtünün yokluğudur.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B004","candidate_links":[{"candidate_id":"cand_0bb75bdb84d64cf1228b","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:24:1:2","qac_word_ref":"88:24:1","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:24:3:2","qac_word_ref":"88:24:3","surface_ar":"عَذَابَ"}],"gloss":"gökyüzüne karşı örtüsüz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Varlık ile gökyüzü arasında onu örten hiçbir engel bulunmaz."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu durum geceyi gökyüzüne açık ve örtüsüz geçirme örneğiyle anlatılır."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Üstünde hiçbir örtü olmadan doğrudan gökyüzüne açık kalan kişi veya nesne için kullanılır.","boundary_detail":"Genel çıplaklıktan daha dardır: belirleyici koşul, varlıkla gökyüzü arasındaki üst örtünün yokluğudur.","branch_image_ar":"العذوب المكشوف للسماء","concept_gloss":"gökyüzüne karşı örtüsüz","contextual_glosses":[{"applicability":"Birinin geceyi üstünde dam veya örtü bulunmadan geçirdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geceleme olayını ve gökyüzüne açık kalmayı korur."},"facet_ids":["F001","F002"],"text":"geceyi açıkta geçirdi","usage_role":"contextual"}],"definition":"Bir varlığın kendisiyle gökyüzü arasında hiçbir dam, örtü veya siper bulunmadan açıkta kalmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Varlık ile gökyüzü arasında onu örten hiçbir engel bulunmaz."},{"facet_id":"F002","role":"example","statement":"Bu durum geceyi gökyüzüne açık ve örtüsüz geçirme örneğiyle anlatılır."}],"identity_rationale":"Yetkili ifade, bir varlık ile gökyüzü arasında hiçbir örtü bulunmamasını doğrudan bildirir. Aynı biçimlerin yememe-içmeme dalında da bulunması bu mekânsal anlamı değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"gökyüzüne karşı örtüsüz olan"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"gökyüzüne karşı örtüsüz olan"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"geceyi gökyüzüne açık geçirdi"}],"lexicalization_note":"Yalın durum bildiren biçimler ile geceyi gökyüzüne açık geçirme yapısı aynı mekânsal çekirdek altında, yapı sınırları korunarak verilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel örtüsüzlük ile açık alan adayları sınırı en iyi gösterdi, öteki adaylar belirli yüzeyler, görünürlük veya uzak mekân ilişkileridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dikey olarak gökyüzüne açık kalma durumudur; komşu beden, yer ve hayvan üzerinde çok daha genel bir örtüsüzlük alanı kurar.","focus_only":"Odak özellikle üst örtünün yokluğunu ve gökyüzüne doğrudan açık olmayı şart koşar.","gloss":"çıplaklık ve örtüsüzlük","neighbor_only":"Komşu giysisizliği, genel örtüsüzlüğü, açık araziyi ve eyersiz hayvanı da kapsar.","neighbor_ref":"root_001004/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir varlığı örten veya gizleyen bir katmanın bulunmaması vardır."},{"boundary_match":"partial","distinction":"Odak kişinin veya nesnenin örtüsüz durumudur; komşu ise bulunulan yerin geniş ve açık oluşunu merkez alır.","focus_only":"Odak, yerdeki genişlikten bağımsız olarak bir varlığın üstünde örtü bulunmamasını anlatır.","gloss":"açık alan","neighbor_only":"Komşu, geniş ve açık bir alanı ve kişinin o alana çıkmasını adlandırır.","neighbor_ref":"root_000105/B002","relation_type":"near_neighbor","shared_zone":"Açık gökyüzü altında bulunma sahnesinde iki dal birlikte gerçekleşebilir."}],"source_phrase_ar":"العذوب الذي ليس بينه وبين السماء ستر وكذلك العاذب (maqayis;tahdhib)؛ فبات عذوبا للسماء كأنه سهيل (maqayis;tahdhib)","source_summary":"Tanıklıklar, gökyüzüyle kişi veya nesne arasında örtü bulunmayan açıkta kalma durumunda birleşir ve bunu geceleme örneğiyle gösterir.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه العذوب أو العاذب الذي لا ستر بينه وبين السماء.","what_is_not_ar":"ليس مجرد الامتناع عن الطعام والشراب إلا حيث احتملته الشواهد."},"support_links":["sup_af13f67dc9e4f4f956e8"]},{"boundary":"Çekirdek ağır acı çektirme veya cezadır; her güçlük kendiliğinden bu dala girmez ve bildirilen dayak kökeni tanımın şartı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B005","candidate_links":[{"candidate_id":"cand_a3eb339df6f5c9fde9b0","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:24:1:2","qac_word_ref":"88:24:1","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:24:3:2","qac_word_ref":"88:24:3","surface_ar":"عَذَابَ"}],"gloss":"ağır acı çektirme ve cezalandırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye ağır acı verilir veya ağır bir ceza uygulanır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir yapı, bütünüyle yok etmeye yönelik cezayı anlatır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bildirilen bir görüş anlamı dayaktan başlatır ve sonra her ağır sıkıntıya genişletir."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem uygulanan ağır cezayı hem de birine şiddetli acı verme eylemini karşılayan çekirdek ifadedir.","boundary_detail":"Çekirdek ağır acı çektirme veya cezadır; her güçlük kendiliğinden bu dala girmez ve bildirilen dayak kökeni tanımın şartı değildir.","branch_image_ar":"العذاب إيلام وعقوبة","concept_gloss":"ağır acı çektirme ve cezalandırma","contextual_glosses":[{"applicability":"Eyleyenin başka bir kişiye şiddetli acı verdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eyleyeni, etkileneni ve ağır acının verilmesini korur."},"facet_ids":["F001"],"text":"ona ağır acı çektirdi","usage_role":"contextual"},{"applicability":"Cezanın hedefi bütünüyle ortadan kaldırmak olduğunda kullanılan özel karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Cezalandırmayı ve yok etmeye yönelik özel sonucu korur."},"facet_ids":["F002"],"text":"yok edici ceza","usage_role":"contextual"}],"definition":"Birine ağır acı çektirme veya onu ağır biçimde cezalandırmadır. Dayak kökeni ve anlamın her türlü ağır sıkıntıya yayılması, çekirdeğin parçası değil aktarılan bir açıklamadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye ağır acı verilir veya ağır bir ceza uygulanır."},{"facet_id":"F002","role":"specialization","statement":"Belirli bir yapı, bütünüyle yok etmeye yönelik cezayı anlatır."},{"facet_id":"F003","role":"source_variant","statement":"Bildirilen bir görüş anlamı dayaktan başlatır ve sonra her ağır sıkıntıya genişletir."}],"identity_rationale":"Yetkili ifade ağır acı verme ve cezalandırma çekirdeğini doğrular. Bunun dayaktan türediği ve sonra her ağır sıkıntıya aktarıldığı açıklaması ortak zorunlu anlam değil, bildirilen bir köken ve genişleme görüşüdür; dal ancak bu kayıtla kabul edilebilir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ağır acı ve ceza"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ona ağır acı çektirdi veya ceza verdi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yok edici ceza"}],"lexicalization_note":"Tanım ad, eylem ve yok etmeye yönelik ceza yapısını ayırır; yapıya bağlı özel ceza bütün dala genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; acı verme, acı duyma ve sınanma adayları temel sınırları gösterdi, diğerleri belirli ceza türleri veya daha uzak şiddet sahneleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak ağır acı ve ceza eksenindedir; komşu ise şiddet veya ceza şartı olmadan acı verme eylemini ve acı verici niteliği kapsar.","focus_only":"Odak, acı vermenin yanında ağır ceza uygulamayı ve cezayı ad olarak da kapsar.","gloss":"acı verme veya acı verici olma","neighbor_only":"Komşu, bir şeyin veya kişinin acı verici olduğunu nitelemeyi de kapsar.","neighbor_ref":"root_000046/B002","relation_type":"near_synonym","shared_zone":"İki dal da başka bir kişide acı meydana getirme alanında doğrudan örtüşür."},{"boundary_match":"partial","distinction":"Odak acının uygulanması ve cezalandırma yönündedir; komşu ise etkilenen kişinin acıyı hissetmesi durumudur.","focus_only":"Odak, acının bir başkasına uygulanmasını ve bunun ceza niteliği taşımasını içerir.","gloss":"acı duyma","neighbor_only":"Komşu, acıyı yaşayan kişinin bedensel veya ruhsal duyumunu merkez alır.","neighbor_ref":"root_000046/B001","relation_type":"near_neighbor","shared_zone":"Uygulanan ağır acı, etkilenen kişide acı duyumuna yol açar."},{"boundary_match":"partial","distinction":"Odakta acı verme ve ceza vardır; komşuda belirleyici unsur iyi veya kötü bir durumun sınama işlevi görmesidir.","focus_only":"Odak, birine ağır acı veya ceza uygulanmasını çekirdek edinir.","gloss":"sınanma ve sıkıntı","neighbor_only":"Komşu, sınanma niteliğindeki sıkıntıların yanında rahatlığı ve mal ya da çocuklarla sınanmayı da kapsar.","neighbor_ref":"root_001128/B004","relation_type":"near_neighbor","shared_zone":"Ağır sıkıntı veya ceza, iki dalın kesiştiği deneyim alanıdır."}],"source_phrase_ar":"العذاب يقال منه عذب تعذيبا وناس يقولون أصل العذاب الضرب ثم استعير ذلك في كل شدة (maqayis)؛ عذبت الرجل وغيره تعذيبا والاسم العذاب (jamhara)؛ العذاب العقوبة وقد عذبته تعذيبا (sihah)؛ العذاب هو الإيجاع الشديد (mufradat)","source_summary":"Ortak çekirdek ağır acı verme ve cezalandırmadır; dayak kökeni ile her ağır sıkıntıya yayılma ise zorunlu anlamdan ayrı, aktarılan bir açıklamadır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه العذاب والعقوبة والإيجاع الشديد، والتعذيب، وما يذكره المصدر من أصل الضرب ثم استعارة كل شدة.","what_is_not_ar":"ليس الماء العذب ولا طرف السوط المسمى عذبة."},"support_links":["sup_4c37eec3c70b74c43d7f"]},{"boundary":"Dal, bir şeyin ince ucu veya ona bağlı sarkan parçadır; su kirliliği, ceza ve hayvanın ayakları bu kapsama girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:24:1:2","qac_word_ref":"88:24:1","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:24:3:2","qac_word_ref":"88:24:3","surface_ar":"عَذَابَ"}],"gloss":"ince uç veya sarkan bağlı parça","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kamçı veya dil gibi bir şeyin ince, dışa uzanan son bölümüdür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir nesneye bağlanan veya ondan sarkan ip, kayış, bez ya da deri parçasıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ağaçta aynı biçimsel alan dışa uzanan dalı karşılar."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem doğal uçlarını hem de bir araca bağlanan ip, kayış, bez veya deri parçalarını kapsar.","boundary_detail":"Dal, bir şeyin ince ucu veya ona bağlı sarkan parçadır; su kirliliği, ceza ve hayvanın ayakları bu kapsama girmez.","branch_image_ar":"العذبة طرف أو علاقة متدلية","concept_gloss":"ince uç veya sarkan bağlı parça","contextual_glosses":[{"applicability":"Kamçının son bölümü ya da ona takılmış sarkan bağ anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kamçıya ait uç ve sarkan bağ seçeneklerini korur."},"facet_ids":["F001","F002"],"text":"kamçının ucu veya askısı","usage_role":"contextual"},{"applicability":"Ayakkabı bağı, eyer veya başka bir kayışın serbestçe sarkan ucunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kayışa bağlı olmayı, uç konumunu ve sarkmayı korur."},"facet_ids":["F002"],"text":"sarkan kayış ucu","usage_role":"contextual"}],"definition":"Bir nesnenin ince veya dışa uzanan ucu ya da ona bağlanıp sarkan ip, kayış, bez, deri veya dal parçasıdır. Belirli araç ve beden bölümlerinde parçanın yeri ve işlevi ayrıca belirlenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kamçı veya dil gibi bir şeyin ince, dışa uzanan son bölümüdür."},{"facet_id":"F002","role":"core","statement":"Bir nesneye bağlanan veya ondan sarkan ip, kayış, bez ya da deri parçasıdır."},{"facet_id":"F003","role":"extension","statement":"Ağaçta aynı biçimsel alan dışa uzanan dalı karşılar."}],"identity_rationale":"Yetkili ifade kamçı ve dil ucu gibi uçları; mızrağa bağlanan bez, teraziyi kaldıran ip, ayakkabı bağı ucu ve dal gibi uzanan ya da sarkan parçaları birlikte verir. Geçici çerçeve bu ortak biçimsel alanı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kamçının ucu veya askısı"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"mızrak başına bağlanan bez"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"dilin ince ucu"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"teraziyi kaldıran ip"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"ağaç dalı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"deve kamışının öndeki sivri ucu"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"ayakkabı bağının serbest ucu"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"kayışların uçları"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"eyerin arkasından sarkan deri parçası"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"ağıtçı kadının bezi"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"kamçıya askı yaptı"}],"lexicalization_note":"Anlam çoğunlukla belirtilen nesneyle kurulan yapılara bağlıdır; uç, bağ, bez, ip ve dal gerçekleşmeleri tek bir yalın ada indirgenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kamçı ve dil ucunu paylaşan aday ile sarkan bağ adayının ayrımı yayımlandı, diğerleri yalnız biçimsel benzerlik veya uzak parça ilişkisi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu uç ve çıkıntı çevresinde kalır; odak bu alanı aşarak çeşitli nesnelere bağlı veya onlardan sarkan ince parçaları da adlandırır.","focus_only":"Odak, uçların yanında mızrağa bağlanan bez, terazi ipi, dal ve sarkan kayış gibi bağlı parçaları da kapsar.","gloss":"uç veya uçtaki çıkıntı","neighbor_only":"Komşu, uçtaki belirgin düğüm veya çıkıntıyı özellikle öne çıkarır.","neighbor_ref":"root_000205/B005","relation_type":"near_synonym","shared_zone":"Kamçı ucu ve ona benzetilen dil ucu iki dalın doğrudan ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak uç ve bağlı ince parça düzenine dayanır; komşu saç örgüsü, en üst bölüm ve sarkan eklenti arasında daha geniş bir biçim alanı kurar.","focus_only":"Odak, araçların işlevli uçlarını ve terazi ipi ya da mızrak bezi gibi özel bağlı parçaları içerir.","gloss":"örgü, üst bölüm veya sarkan bağ","neighbor_only":"Komşu, saç örgüsünü ve bir şeyin en üst bölümünü de kapsar.","neighbor_ref":"root_000505/B009","relation_type":"near_neighbor","shared_zone":"Ayakkabı, kılıç veya eyerden sarkan bağ ve uzantılar iki dalda kesişir."}],"source_phrase_ar":"عذبة السوط طرفه (maqayis;tahdhib)؛ عذبة الرمح الخرقة التي تشد على رأسه (jamhara)؛ عذبة اللسان طرفه (jamhara;sihah;tahdhib)؛ عذبة الميزان الخيط الذي يرفع به (sihah;tahdhib)؛ عذبة الشجر غصنه (sihah;tahdhib)؛ عذبة شراك النعل المرسلة من الشراك (tahdhib)","source_summary":"Tanıklıklar uçta bulunan veya bir şeye bağlanıp sarkan ince parçaları ortaklaştırır; kamçı, dil, mızrak, terazi, ağaç ve ayakkabı bağı bunun belirli gerçekleşmeleridir.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه طرف السوط واللسان، والخرقة أو السير المشدود، والخيط، والغصن، وأطراف السيور والشراك، وما كان من علاقة أو ذوابة متدلية.","what_is_not_ar":"ليس العذاب ولا العذوبة في الماء، ولا القوائم المسماة عذوبات الناقة."},"support_links":[]},{"boundary":"Bu dalın öğeleri genel kök anlamı gibi genişletilmemeli, birbirinin yerine geçebilen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtta verilen biçim veya bağlam sınırı içinde tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:24:1:2","qac_word_ref":"88:24:1","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:24:3:2","qac_word_ref":"88:24:3","surface_ar":"عَذَابَ"}],"gloss":"yalıtık adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Suyun içinde çer çöp bulunur veya havuzun yüzeyini yosunsu bir tabaka kaplar."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Havuzdaki çer çöpü çıkarmak ya da yüzey tabakasını kırıp suyu görünür kılmak anlatılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ayrı bir yapı, su başının çevresinde otlak veya ot bulunmamasını bildirir."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki dağınık veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu dalın öğeleri genel kök anlamı gibi genişletilmemeli, birbirinin yerine geçebilen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtta verilen biçim veya bağlam sınırı içinde tutulmalıdır.","branch_image_ar":"العذبة شوائب الماء أو سطحه","concept_gloss":"yalıtık adlandırmalar","contextual_glosses":[{"applicability":"Suda bulunan küçük yabancı maddeler veya bunların çokluğu anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suyun içindeki küçük yabancı maddeyi ve çokluk olasılığını korur."},"facet_ids":["F001"],"text":"sudaki çer çöp","usage_role":"contextual"},{"applicability":"Suyun kendisini değil, çevresinde hayvanların otlayacağı bitki bulunmamasını anlatan ayrı yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Su başını ve çevresindeki otlak yokluğunu birlikte korur."},"facet_ids":["F003"],"text":"çevresinde otlak bulunmayan su başı","usage_role":"explanatory"}],"definition":"Bir kullanım kümesi sudaki çer çöpü veya havuz yüzeyindeki yosunsu tabakayı ve bunların temizlenmesini anlatır. Ayrı bir kullanım ise bir su başının çevresinde otlak ve ot bulunmadığını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Suyun içinde çer çöp bulunur veya havuzun yüzeyini yosunsu bir tabaka kaplar."},{"facet_id":"F002","role":"associated_use","statement":"Havuzdaki çer çöpü çıkarmak ya da yüzey tabakasını kırıp suyu görünür kılmak anlatılır."},{"facet_id":"F003","role":"source_variant","statement":"Ayrı bir yapı, su başının çevresinde otlak veya ot bulunmamasını bildirir."}],"identity_rationale":"Bu dal packet düzeyinde inceleme statüsünde tutulmuş sınır-riskli malzemeyi taşır. Kanıt, tek bir yalın kök imgesinden çok biçime veya özel kullanıma bağlı dağınık adlandırmaları gösterdiği için dal yapısal bölme şartı koşmadan sınırlı bir adlandırma kümesi olarak okunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"sudaki çer çöp veya yüzey tabakası"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"çer çöpü bol su"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"havuzundaki çer çöpü çıkar"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"havuzun yüzey tabakasını kır"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"çevresinde otlak bulunmayan su başı"}],"lexicalization_note":"Kapsam verilen biçim veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"العذبة القذاة وماء ذو عذب أي كثير القذى (sihah)؛ أعذب حوضك أي انزع ما فيه من القذى (sihah)؛ اضرب عذبة الحوض حتى يظهر الماء أي اضرب عرمضه (tahdhib)؛ ماء ما به عذبة أي لا رعي فيه ولا كلأ (tahdhib)","source_summary":"İnceleme statüsündeki kanıt, tek bir birleşik anlamdan çok biçime veya özel bağlama bağlı sınırlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["SI","TA"],"what_is_ar":"يدخل فيه العذبة بمعنى القذاة في الماء، وكثرة القذى، وإزالة ما في الحوض من القذى أو عرمضه، مع شاهد تهذيب عن ماء لا رعي فيه ولا كلأ.","what_is_not_ar":"ليس الماء العذب الطيب؛ بل مادة غير مرغوبة أو محيطة بالماء."},"support_links":[]},{"boundary":"Dal tat, su veya içim hoşluğu değil, kişinin iyi ve cömert karakterini bildirir.","branch_kind":"bare","branch_ref":"root_000994/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:24:1:2","qac_word_ref":"88:24:1","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:24:3:2","qac_word_ref":"88:24:3","surface_ar":"عَذَابَ"}],"gloss":"iyi ve cömert huylu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi iyi, cömert ve değerli bir karakter taşır."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin ahlaki karakterinin iyi, cömert ve değerli olduğunu bildiren genel karşılıktır.","boundary_detail":"Dal tat, su veya içim hoşluğu değil, kişinin iyi ve cömert karakterini bildirir.","branch_image_ar":"العذبي كريم الأخلاق","concept_gloss":"iyi ve cömert huylu","contextual_glosses":[{"applicability":"Kişinin karakterini doğal bir ad öbeği içinde anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İyi huyu, cömertliği ve kişi niteliğini korur."},"facet_ids":["F001"],"text":"iyi huylu ve cömert biri","usage_role":"general"}],"definition":"İyi, cömert ve değerli huylara sahip kişi niteliğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi iyi, cömert ve değerli bir karakter taşır."}],"identity_rationale":"Yetkili ifade tek ve açık biçimde iyi, cömert ve değerli huylara sahip kişiyi niteler. Geçici çerçeve bu ahlaki kişilik niteliğini eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"iyi ve cömert huylu"}],"lexicalization_note":"Tanım yalnız yalın kişi niteliğini verir; komşu erdem adları veya belirli davranış kalıpları bu dala taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşleşen iyi karakter dalı ile daha geniş erdemli olgunluk alanı yayımlandı, diğerleri cömertliğin özel görünümleri veya uzak kişi tipleridir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kanıt sınırlarında iki dal arasında kapsam, katılımcı veya koşul farkı görünmez.","focus_only":null,"gloss":"iyi ve cömert huylu kişi","neighbor_only":null,"neighbor_ref":"root_001075/B003","relation_type":"synonym","shared_zone":"Her iki dal da kişiyi iyi ve cömert karakterli olması bakımından niteler."},{"boundary_match":"partial","distinction":"Odak yalın bir iyi ve cömert huy sıfatıdır; komşu daha geniş bir kişilik ve toplumsal olgunluk idealini adlandırır.","focus_only":"Odak doğrudan kişinin iyi ve cömert huylu oluşunu bildiren bir niteliktir.","gloss":"erdemli olgunluk","neighbor_only":"Komşu, toplumsal olarak kabul edilen insanlık ve olgunluk idealini ve bu niteliği edinme çabasını da kapsar.","neighbor_ref":"root_001409/B002","relation_type":"near_neighbor","shared_zone":"İyi karakter ve toplumca değer verilen davranış niteliği iki dalda kesişir."}],"source_phrase_ar":"العذبي الكريم الأخلاق (sihah)","source_summary":"Tek tanıklık kişiyi iyi ve cömert karakterli olarak niteleyen yalın bir sıfat anlamı verir.","sources":["SI"],"what_is_ar":"يدخل فيه وصف العذبي بمعنى الكريم الأخلاق.","what_is_not_ar":"ليس العذب بمعنى الطيب من الماء إلا من جهة اللفظ المشترك في المادة."},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_000994/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:24:1:2","qac_word_ref":"88:24:1","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:24:3:2","qac_word_ref":"88:24:3","surface_ar":"عَذَابَ"}],"gloss":"biçime bağlı adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğumdan sonra çocuğun ardından döl yatağından bir madde çıkar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir biçim kadının döl yatağını, yani doğacak çocuğun geliştiği organı adlandırır."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"العذابة والرحم والخرج بعد الولد","concept_gloss":"biçime bağlı adlandırmalar","contextual_glosses":[{"applicability":"Çocuğun doğumunu izleyerek döl yatağından çıkan madde anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Maddenin doğumdan sonra ve döl yatağından çıkmasını korur."},"facet_ids":["F001"],"text":"doğumdan sonra çıkan madde","usage_role":"explanatory"},{"applicability":"Doğacak çocuğun geliştiği kadın organının doğrudan adlandırıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına ait anatomik organ referentini korur."},"facet_ids":["F002"],"text":"kadının döl yatağı","usage_role":"contextual"}],"definition":"Bir anlam doğumdan sonra çocuğun ardından döl yatağından çıkan maddeyi bildirir. Ayrı bir anlam ise kadının döl yatağının kendisini adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğumdan sonra çocuğun ardından döl yatağından bir madde çıkar."},{"facet_id":"F002","role":"core","statement":"Ayrı bir biçim kadının döl yatağını, yani doğacak çocuğun geliştiği organı adlandırır."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"doğumdan sonra döl yatağından çıkan madde"},{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"kadının döl yatağı"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"العذب ما يخرج على أثر الولد من الرحم (tahdhib)؛ العذابة رحم المرأة (tahdhib)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["TA"],"what_is_ar":"يدخل فيه العذب الخارج على أثر الولد من الرحم، والعذابة بمعنى الرحم.","what_is_not_ar":"ليس العذاب ولا العذوبة ولا العذبة الطرفية."},"support_links":[]},{"boundary":"Bu dal genel büyüklüğü anlatır; yaş, ahlaki üstünlük, kibir ve bir bütünün en büyük payı ayrı dallardadır.","branch_kind":"bare","branch_ref":"root_001281/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","surface_ar":"أَكْبَرَ"}],"gloss":"küçüğün karşıtı olan büyüklük","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlık veya değerin küçüğe göre daha büyük ölçü ya da derece taşıması temel anlamdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Büyüklük somut hacim yanında miktar, sayı ve genel konum bakımından da kurulabilir."}}],"root_ar":"ك ب ر","root_id":"root_001281","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölçü, miktar, sayı veya genel derece bakımından küçüğün karşıtı kastedildiğinde kullanılır.","boundary_detail":"Bu dal genel büyüklüğü anlatır; yaş, ahlaki üstünlük, kibir ve bir bütünün en büyük payı ayrı dallardadır.","branch_image_ar":"العظم خلاف الصغر","concept_gloss":"küçüğün karşıtı olan büyüklük","contextual_glosses":[{"applicability":"Bağlam hangi ölçü veya derece ekseninin söz konusu olduğunu zaten gösterdiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlam içinde küçüğün karşıtı olan genel büyüklüğü eksiksiz biçimde taşır."},"facet_ids":["F001","F002"],"text":"büyük","usage_role":"general"}],"definition":"Bir şeyin ölçü, miktar, sayı ya da göreli derecede küçüğün karşıtı olacak ölçüde büyük olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlık veya değerin küçüğe göre daha büyük ölçü ya da derece taşıması temel anlamdır."},{"facet_id":"F002","role":"extension","statement":"Büyüklük somut hacim yanında miktar, sayı ve genel konum bakımından da kurulabilir."}],"identity_rationale":"Kaynak ifadesi, küçüklüğün karşıtı olan genel büyüklüğü; ölçü, miktar, sayı veya göreli derecede büyük olma üzerinden açıkça kurar. Geçici çerçeve bu çekirdeği yaşlılık, kibir ya da bir işin ana bölümü gibi komşu anlamlardan doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"büyük"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"pek büyük"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"daha büyük veya en büyük"}],"lexicalization_note":"Tanım yalın büyüklük alanıyla sınırlıdır ve yalnız belirli bir kalıba bağlı olan anlamları içine almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; karşıt küçüklük ile kısmen örtüşen irilik, sınırı en açık gösteren iki karşılaştırma olarak seçildi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal büyüklüğü, komşu dal ise küçüklüğü bildirir; aynı göreli ölçeğin karşıt kutuplarıdır.","focus_only":"Bu dal aynı eksenin büyük olan kutbunu bildirir.","gloss":"küçüklük","neighbor_only":"Komşu dal aynı eksenin küçük olan kutbunu bildirir.","neighbor_ref":"root_000865/B001","relation_type":"antonym","shared_zone":"İki dal da ölçü, sayı, yaş veya konum gibi karşılaştırılabilir bir derece ekseninde çalışır."},{"boundary_match":"partial","distinction":"Odak daha genel bir karşılaştırmalı büyüklük alanıdır; komşu ise özellikle iri yapı ve hacimli oluş üzerinde yoğunlaşır.","focus_only":"Odak dal sayı, miktar ve genel dereceyi de kapsar.","gloss":"irilik ve hacimlilik","neighbor_only":"Komşu dal özellikle beden veya bir işteki irilik ve hacimliliği öne çıkarır.","neighbor_ref":"root_000247/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da somut bir şeyin büyük ve hacimli oluşunu anlatabilir."}],"source_phrase_ar":"أصل صحيح يدل على خلاف الصغر (maqayis)؛ كبر كل شيء عظمه (ayn)؛ الكبر ضد الصغر (jamhara)؛ كبر بالضم يكبر أي عظم فهو كبير وكبار (sihah)؛ الكبير والصغير من الأسماء المتضايفة (mufradat)","source_summary":"Kaynaklar ortak biçimde bu alanı küçüklüğün karşıtı sayar ve büyüklüğü nesnenin ölçüsüne, miktarına, sayısına veya göreli derecesine uygular.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الحجم أو القدر أو العدد إذا عظم في مقابلة الصغر، ومنه الكبير والكبار والأكبر","what_is_not_ar":"ليس خصوص الهرم ولا معظم الأمر وحده ولا التكبر المذموم"},"support_links":[]},{"boundary":"Anlam bir bütünün ana payı veya bir işin başlıca yüküdür; genel büyüklük tek başına bu dalı karşılamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001281/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","surface_ar":"أَكْبَرَ"}],"gloss":"bir işin ana payı ve başlıca yükü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünün en büyük, ana veya belirleyici bölümü temel anlamdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ana bölüm fikri, bir olayın başlıca yükünü üstlenme veya ondan en büyük payı taşıma anlamına uzanır."}}],"root_ar":"ك ب ر","root_id":"root_001281","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bütünün en büyük bölümü ile o bölümün getirdiği başlıca sorumluluk birlikte kastedildiğinde kullanılır.","boundary_detail":"Anlam bir bütünün ana payı veya bir işin başlıca yüküdür; genel büyüklük tek başına bu dalı karşılamaz.","branch_image_ar":"معظم الأمر","concept_gloss":"bir işin ana payı ve başlıca yükü","contextual_glosses":[{"applicability":"Söz konusu olan bir olayın veya meselenin nicelikçe ya da önemce ana payıysa kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütün içindeki en büyük ve başlıca payı açıkça belirtir."},"facet_ids":["F001"],"text":"işin büyük bölümü","usage_role":"contextual"},{"applicability":"Bir kişinin olayın en büyük yükünü üstlenmesi veya olaydan başlıca sorumlu olması kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ana payın bir kişi tarafından yüklenmesi ve sorumluluk doğurması yönünü korur."},"facet_ids":["F002"],"text":"başlıca sorumluluk","usage_role":"contextual"}],"definition":"Bir işin ya da bütünün en büyük ve başlıca bölümü, bundan hareketle de o işin başlıca yükü veya sorumluluğudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünün en büyük, ana veya belirleyici bölümü temel anlamdır."},{"facet_id":"F002","role":"extension","statement":"Ana bölüm fikri, bir olayın başlıca yükünü üstlenme veya ondan en büyük payı taşıma anlamına uzanır."}],"identity_rationale":"Kaynak ifadesi bir şeyin en büyük veya ana bölümünü, ayrıca bir olayın başlıca yükünü üstlenen kişiye uzanan kullanımı destekler. Geçici çerçeve bunu salt hacim büyüklüğünden ve yaşlılıktan doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"işin büyük bölümü veya ağır yükü"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onun işinin en önemli bölümü"}],"lexicalization_note":"Yalın ad biçimindeki ana pay anlamı ile belirli söz öbeklerinde görülen işin önemli bölümü anlamı ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ana bölümle en yakın örtüşen çoğunluk dalı ve sık karışabilecek genel büyüklük dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu nicel çoğunluğu doğrudan anlatır; odak ise ana bölümün önemini ve onu yüklenme sorumluluğunu da kapsar.","focus_only":"Odak dal ana paydan doğan başlıca yük ve sorumluluğa da uzanır.","gloss":"bir şeyin çoğu","neighbor_only":"Komşu dal bir şeyin çoğu veya büyük kısmı olmakla sınırlı kalır.","neighbor_ref":"root_001029/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir bütünün en büyük veya çoğunluğu oluşturan bölümünü gösterebilir."},{"boundary_match":"partial","distinction":"Genel büyüklük bir nesnenin derecesidir; bu dal ise bütün içinden başlıca bölümü ve ona bağlı yükü ayırır.","focus_only":"Odak bir bütün içindeki ana payı veya işin yükünü seçer.","gloss":"genel büyüklük","neighbor_only":"Komşu bir şeyin genel olarak küçük olmayıp büyük olmasını bildirir.","neighbor_ref":"root_001281/B001","relation_type":"near_neighbor","shared_zone":"Ana payın belirlenmesi çoğu zaman onun öteki parçalardan daha büyük oluşuna dayanır."}],"source_phrase_ar":"والكبر معظم الأمر (maqayis)؛ كبر كل شيء عظمه (ayn)؛ كبر الشيء معظمه (jamhara)؛ كبر الشيء أيضا معظمه (sihah)؛ كبر الشيء معظمه بالكسر (tahdhib)؛ والذي تولى كبره إشارة إلى من أوقع حديث الإفك (mufradat)","source_summary":"Kaynaklar bir şeyin ana ve en büyük bölümünde birleşir; toplu aktarım ayrıca bir olayın başlıca yükünü üstlenen kişiye yapılan göndermeyi de içerir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"معظم الشيء أو شأنه وما يتحمله أو يتولاه المرء من أكبر نصيب الأمر","what_is_not_ar":"ليس مجرد كبر الحجم ولا الهرم"},"support_links":[]},{"boundary":"Çekirdek, bir şeyi gözünde büyütüp büyük saymaktır; sırf sevinme, güzel bulma veya korkma tek başına yeterli değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001281/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","surface_ar":"أَكْبَرَ"}],"gloss":"gözünde büyütüp hayrete düşmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi zihinde büyük görmek ve önemini olduğundan ya da sıradan düzeyden yüksek değerlendirmek çekirdektir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu zihinsel büyütmeye, görülen şey karşısında hayret etme tepkisi eşlik edebilir."}}],"root_ar":"ك ب ر","root_id":"root_001281","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya şeyin zihinde büyük görülmesi ve bu değerlendirmenin hayret doğurması kastedildiğinde kullanılır.","boundary_detail":"Çekirdek, bir şeyi gözünde büyütüp büyük saymaktır; sırf sevinme, güzel bulma veya korkma tek başına yeterli değildir.","branch_image_ar":"إعظام الشيء في الصدر","concept_gloss":"gözünde büyütüp hayrete düşmek","contextual_glosses":[{"applicability":"Hayret açıkça belirtilmese de nesnenin zihinde büyük ve önemli sayıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesneyi zihinde büyük görme ve ona yüksek önem verme çekirdeğini korur."},"facet_ids":["F001"],"text":"gözünde büyütmek","usage_role":"contextual"},{"applicability":"Büyük görmenin doğrudan bir hayret tepkisi doğurduğu bağlamlarda açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Büyük sayma ile ondan doğan şaşırma arasındaki bağı korur."},"facet_ids":["F001","F002"],"text":"büyüklüğü karşısında şaşırmak","usage_role":"explanatory"}],"definition":"Bir şeyi veya kişiyi zihninde büyük ve önemli saymak, onu gözünde büyütmek ve bunun etkisiyle hayrete düşmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi zihinde büyük görmek ve önemini olduğundan ya da sıradan düzeyden yüksek değerlendirmek çekirdektir."},{"facet_id":"F002","role":"associated_use","statement":"Bu zihinsel büyütmeye, görülen şey karşısında hayret etme tepkisi eşlik edebilir."}],"identity_rationale":"Kaynak ifadesi bir şeyi zihinde büyük saymayı, büyük görmeyi ve bundan doğan hayreti açıkça bildirir. Geçici çerçevenin hayranlık yönü ancak bu zihinsel büyütme ve şaşırma sınırında anlaşılmalıdır; ayrı bir bedensel yorum bu dala alınmaz.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onu gözünde büyüttü ve ona hayret etti"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"onu gözlerinde büyüttüler"}],"lexicalization_note":"Anlam, nesne alan yapılar ve tanıklanmış özel çekimli kullanım üzerinden verilir; genel büyüklük anlamıyla birleştirilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; zihinsel büyütmeyle en çok örtüşen heybet ve beğeni alanları, gerçek sınır farkları taşıdıkları için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak gözünde büyütme ve hayret üzerindedir; komşu ise bu değerlendirmeyi korkutucu heybet veya yadırgamaya doğru genişletir.","focus_only":"Odak dal büyük görmenin yanında hayret tepkisine açıkça yer verir.","gloss":"büyük görme ve heybet","neighbor_only":"Komşu dal büyüklük algısına ürkme, yadırgama veya heybet duygusunu da bağlar.","neighbor_ref":"root_001029/B007","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir şey zihinde olağan ölçünün üstünde ve büyük değerlendirilir."},{"boundary_match":"partial","distinction":"Beğeni ve sevinç nesneyi büyük saymayı gerektirmez; odak dalın kurucu işlemi ise onu zihinde büyütmektir.","focus_only":"Odak nesneyi büyük sayma ve şaşırma değerlendirmesini içerir.","gloss":"beğenme ve sevinme","neighbor_only":"Komşu beğenme ile sevinmeyi birlikte bildirir.","neighbor_ref":"root_000832/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da olumlu veya çarpıcı bir şey karşısındaki etkilenmeyi anlatabilir."}],"source_phrase_ar":"أكبرت الشيء استعظمته (maqayis)؛ أكبرت الشيء أكبره إكبارا إذا عظم في صدرك وعجبت منه (jamhara)؛ أكبرت الشيء استعظمته (sihah)؛ أكبرنه أعظمنه (tahdhib)؛ أكبرت الشيء رأيته كبيرا (mufradat)","source_summary":"Kaynaklar bir şeyi büyük sayma ve gözünde büyütme anlamında birleşir; bazı aktarımlar bunun doğurduğu hayreti de açıkça belirtir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"إكبار الشيء أو الشخص بمعنى استعظامه ورؤيته كبيرا في الصدر أو العجب","what_is_not_ar":"ليس الحيض المنسوب إلى بعض تفسير أكبرنه"},"support_links":[]},{"boundary":"İnsan ve hayvanda yaşlanma, eski nesnede köhneme anlatılır; genel büyüklük veya makam yüksekliği anlatılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001281/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","surface_ar":"أَكْبَرَ"}],"gloss":"yaşlanma ve zamanla eskime","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan ya da hayvanın yaşının ilerlemesi ve yaşlı hale gelmesi temel kullanımdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zamanın etkisi, ok veya kılıç ağzı gibi eski bir nesnede köhneme ve kir tutma biçiminde de anlatılır."}}],"root_ar":"ك ب ر","root_id":"root_001281","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlının ileri yaşa ulaşması ya da eski bir nesnenin zaman etkisiyle köhnemesi kastedildiğinde kullanılır.","boundary_detail":"İnsan ve hayvanda yaşlanma, eski nesnede köhneme anlatılır; genel büyüklük veya makam yüksekliği anlatılmaz.","branch_image_ar":"كبر السن والقدم","concept_gloss":"yaşlanma ve zamanla eskime","contextual_glosses":[{"applicability":"İnsan veya hayvanın yaşının ilerlediği canlı bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlının ileri yaşa varması yönünü tam olarak korur."},"facet_ids":["F001"],"text":"yaşlanmak","usage_role":"contextual"},{"applicability":"Eski bir araç veya metal parçanın zaman ve kir etkisiyle yıprandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin uzun zaman sonunda eskilik niteliği kazanmasını korur."},"facet_ids":["F002"],"text":"zamanla köhnemek","usage_role":"contextual"}],"definition":"Canlıların ileri yaşa varması veya eski bir nesnenin üzerinden uzun zaman geçmesiyle yaşlılık ve eskilik niteliği kazanmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan ya da hayvanın yaşının ilerlemesi ve yaşlı hale gelmesi temel kullanımdır."},{"facet_id":"F002","role":"extension","statement":"Zamanın etkisi, ok veya kılıç ağzı gibi eski bir nesnede köhneme ve kir tutma biçiminde de anlatılır."}],"identity_rationale":"Kaynak ifadesi insan ve hayvanlarda ileri yaşı, ayrıca ok ve kılıç ağzı gibi eski nesnelerde zamanla yerleşen eskiliği birlikte destekler. Geçici çerçeve yaşlanma ile nesne eskiliğini ayırmadan aynı zaman ekseninde, fakat başkanlık ve kibirden ayrı tutar.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"adam yaşlandı"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yaşlılık veya eskilik hali"}],"lexicalization_note":"İnsan ve hayvanın yaşlanmasını bildiren kullanım ile nesnenin eskiliğini bildiren özel biçim aynı dalda ayrı yüzler olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; insan yaşlılığı ve genel nesne eskiliği, dalın iki temel uygulama alanını en iyi sınırlayan komşulardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu insan yaşlılığına odaklanır; odak dal canlıları daha geniş tutar ve nesne eskiliğine uzanır.","focus_only":"Odak hayvanların yaşlanmasını ve eski nesnelerin köhnemesini de kapsar.","gloss":"yaşlı insan ve yaşlılık","neighbor_only":"Komşu özellikle yaşlı erkek ve kadın ile yaşlılık durumunu adlandırır.","neighbor_ref":"root_000834/B001","relation_type":"near_synonym","shared_zone":"İki dal insanın ileri yaşa ulaşması ve yaşlılık durumunda bütünüyle örtüşür."},{"boundary_match":"partial","distinction":"Odakta yaşlanma çekirdeğinden nesne eskiliğine bir uzanım vardır; komşuda genel ve yerleşik eskilik başlı başına çekirdektir.","focus_only":"Odak canlıların ileri yaşını kurucu alan olarak içerir.","gloss":"köklü eskilik","neighbor_only":"Komşu her tür nesnede uzun zaman geçmesi ve köklü eskilik üzerinde durur.","neighbor_ref":"root_000979/B003","relation_type":"near_synonym","shared_zone":"Her iki dal eski bir nesnenin üzerinden uzun zaman geçmiş olmasını anlatabilir."}],"source_phrase_ar":"ومن الباب الكبر وهو الهرم (maqayis)؛ الكبرة السن يقال علته كبرة (ayn)؛ بلغ فلان الكبر في السن (jamhara)؛ الكبر في السن وقد كبر الرجل أي أسن (sihah)؛ الكبر مصدر الكبير في السن من الناس والدواب (tahdhib)؛ يقال فلان كبير أي مسن (mufradat)؛ السهم والنصل العتيق الذي أفسده الوسخ قد علته كبرة (ayn)؛ للسيف والنصل العتيق الذي قدم علته كبرة (tahdhib)","source_summary":"Kaynaklar canlılarda ileri yaş anlamını ortaklaşa verir; toplu aktarım, eskimiş ok ve kılıç ağzındaki zaman ve kir izini de bu alana bağlar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"السن والهرم وامتداد القدم حتى يقال علته كبرة في الإنسان أو الدابة أو السهم والنصل","what_is_not_ar":"ليس الرئاسة ولا التكبر ولا معظم الأمر"},"support_links":[]},{"boundary":"Buradaki büyüklük toplumsal saygınlık, önderlik veya bilgi konumudur; salt yaş ve beden büyüklüğü değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001281/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","surface_ar":"أَكْبَرَ"}],"gloss":"saygınlık ve önderlikte yüksek konum","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Şeref ve toplumsal konum bakımından yüksek ve saygın olma çekirdektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yüksek konum, topluluğun başı, öğreticisi veya en bilgili kişisi olma biçiminde gerçekleşebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Şeref ve itibarın büyük ve saygın atalardan sonraki kuşaklara aktarılması da bu alandadır."}}],"root_ar":"ك ب ر","root_id":"root_001281","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Şerefli soy, topluluk başkanlığı, öğreticilik veya bilgi üstünlüğüyle oluşan yüksek konum kastedildiğinde kullanılır.","boundary_detail":"Buradaki büyüklük toplumsal saygınlık, önderlik veya bilgi konumudur; salt yaş ve beden büyüklüğü değildir.","branch_image_ar":"رفعة الشرف والرئاسة","concept_gloss":"saygınlık ve önderlikte yüksek konum","contextual_glosses":[{"applicability":"Bir kişinin topluluk içindeki saygın, bilgili veya yönetici konumu öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Toplumsal saygınlık ile önderlik konumunu birlikte korur."},"facet_ids":["F001","F002"],"text":"topluluğun ileri geleni","usage_role":"contextual"},{"applicability":"Şeref ve itibarın saygın atalardan sonraki kuşaklara geçtiği anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Miras alınan toplumsal itibarın kuşaklar boyunca sürmesini korur."},"facet_ids":["F001","F003"],"text":"kuşaktan kuşağa saygınlık","usage_role":"explanatory"}],"definition":"Bir kişinin şeref, saygınlık, bilgi veya önderlik bakımından topluluk içinde yüksek konumda bulunması; bu konumun kuşaktan kuşağa aktarılabilmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Şeref ve toplumsal konum bakımından yüksek ve saygın olma çekirdektir."},{"facet_id":"F002","role":"specialization","statement":"Yüksek konum, topluluğun başı, öğreticisi veya en bilgili kişisi olma biçiminde gerçekleşebilir."},{"facet_id":"F003","role":"extension","statement":"Şeref ve itibarın büyük ve saygın atalardan sonraki kuşaklara aktarılması da bu alandadır."}],"identity_rationale":"Kaynak ifadesi şeref yüksekliğini, kuşaktan kuşağa aktarılan itibarı ve topluluk içindeki başkanlık ya da bilgi üstünlüğünü birlikte verir. Geçici çerçeve bu toplumsal yüksekliği yaş büyüklüğünden ve doğum sırasından doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kuşaktan kuşağa soylu ve saygın biçimde"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"onların başı veya en bilgilisi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sizin öğreticiniz veya başınız"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"önder veya en büyük ata"}],"lexicalization_note":"Önder ve saygın kişi bildiren biçimler ile kuşaklar arası soyluluğu anlatan kalıp ayrı yüzler olarak tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel şeref yüksekliği ile işlevsel başkanlık, odak dalın saygınlık ve önderlik sınırlarını en iyi açan iki komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu genel şeref yüksekliğidir; odak bu yüksekliği topluluk içi önderlik ve kuşaktan kuşağa aktarılan itibara bağlar.","focus_only":"Odak önderlik, öğreticilik ve atalardan aktarılan itibarı da içerir.","gloss":"yüksek değer ve şeref","neighbor_only":"Komşu daha genel biçimde değer ve şeref yüksekliğini bildirir.","neighbor_ref":"root_001042/B002","relation_type":"near_synonym","shared_zone":"İki dal kişinin şeref ve toplumsal değer bakımından yüksek konumunu anlatır."},{"boundary_match":"partial","distinction":"Komşuda temsil ve başkanlık kurucudur; odakta ise bu, şeref ve bilgi yüksekliğinin olası gerçekleşmelerinden biridir.","focus_only":"Odak şerefli soy ve bilgide üstünlüğü başkanlık dışında da kapsar.","gloss":"topluluk başkanlığı","neighbor_only":"Komşu topluluk adına duran başkanlık ve temsil görevini özellikle öne çıkarır.","neighbor_ref":"root_000633/B004","relation_type":"near_synonym","shared_zone":"Her iki dal topluluğun başı veya önderi olan saygın kişiyi gösterebilir."}],"source_phrase_ar":"الرفعة في الشرف (ayn)؛ ورثوا المجد كابرا عن كابر (maqayis;jamhara;sihah;tahdhib;mufradat)؛ كبيرهم أعلمهم كأنه كان رئيسهم (tahdhib)؛ إنه لكبيركم أي رئيسكم (mufradat)؛ الكابر السيد والكابر الجد الأكبر (tahdhib)","source_summary":"Toplu kaynak aktarımı şeref yüksekliği, önderlik ve bilgide üstün konumu bir araya getirir; ayrıca itibarın saygın atalardan kuşaklara aktarılmasını belirtir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"العلو في الشرف أو المنزلة أو الرئاسة أو التعليم أو السيادة والمجد الموروث","what_is_not_ar":"ليس ترتيب الولادة المختلف فيه ولا كبر السن وحده"},"support_links":[]},{"boundary":"Dal, ululuk ve kendini üstün görme alanındadır; özel inançsal niteleme yalnız ilgili söz biriminin karşılığında korunur.","branch_kind":"bare","branch_ref":"root_001281/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","surface_ar":"أَكْبَرَ"}],"gloss":"ululuk ve kendini üstün görme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ululuk, üstünlük ve başkalarından yukarıda olma düşüncesi anlamın temel eksenidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanda bu eksen, kendini beğenme, başkalarından üstün sayma ve büyüklük taslama biçiminde gerçekleşir."}}],"root_ar":"ك ب ر","root_id":"root_001281","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ululuk niteliği veya insanın kendisini başkalarından üstün sayarak büyüklük taslaması kastedildiğinde kullanılır.","boundary_detail":"Dal, ululuk ve kendini üstün görme alanındadır; özel inançsal niteleme yalnız ilgili söz biriminin karşılığında korunur.","branch_image_ar":"العظمة والكبرياء","concept_gloss":"ululuk ve kendini üstün görme","contextual_glosses":[{"applicability":"Bir insanın kendisini üstün görüp başkalarına karşı böbürlendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kendini üstün sayma ve bunu davranışla gösterme yönünü korur."},"facet_ids":["F001","F002"],"text":"büyüklük taslamak","usage_role":"contextual"},{"applicability":"Ahlaki olarak olumlu ya da olumsuz insan davranışı belirtilmeden salt yücelik niteliği kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Üstün ve yüce olma biçimindeki genel büyüklük eksenini korur."},"facet_ids":["F001"],"text":"ululuk","usage_role":"general"}],"definition":"Ululuk ve üstünlük niteliği ya da kişinin kendisini başkalarından üstün görerek büyüklük taslaması ve boyun eğmemesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ululuk, üstünlük ve başkalarından yukarıda olma düşüncesi anlamın temel eksenidir."},{"facet_id":"F002","role":"specialization","statement":"İnsanda bu eksen, kendini beğenme, başkalarından üstün sayma ve büyüklük taslama biçiminde gerçekleşir."}],"identity_rationale":"Kaynak ifadesi büyüklük ve ululuk yanında insanın kendini üstün görmesiyle ortaya çıkan böbürlenmeyi açıkça destekler. Geçici çerçevenin Tanrı'ya özgü hak edilmiş ululuk yönü ayrı söz birimi kanıtında bulunur, fakat yetkili dal iddiasında açıkça kurulmadığı için dal tanımının çekirdeğine alınmamıştır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"büyüklük taslama ve kendini üstün görme"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ululuk ve boyun eğmeme; Tanrı'ya özgü yücelik"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"büyüklendi ve kendini üstün gösterdi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"gerçeği inatla reddedip büyüklük tasladı"}],"lexicalization_note":"Tanım yalın ululuk ve üstünlük taslama alanını verir; başka dallardaki büyüklük, yaş veya başkanlık anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kendine hayranlık ve davranışsal böbürlenme, odak dalın iç değerlendirme ile dış tutum arasındaki sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşuda içsel kendine hayranlık çekirdektir; odakta ululuk düşüncesi büyüklük taslama ve boyun eğmeme davranışına dönüşebilir.","focus_only":"Odak genel ululuk niteliğini ve üstünlüğün dışa vurulmasını da kapsar.","gloss":"kendine hayranlık","neighbor_only":"Komşu kişinin kendi benliği veya görüşü karşısındaki iç hayranlığına odaklanır.","neighbor_ref":"root_000984/B002","relation_type":"near_synonym","shared_zone":"Her iki dal insanın kendisini veya kendi değerini olağan ölçünün üstünde görmesini anlatır."},{"boundary_match":"partial","distinction":"Komşu davranışsal kurumlanmaya daha dardır; odak hem ululuk kavramını hem üstünlük iddiasını hem de dirençli boyun eğmezliği kapsar.","focus_only":"Odak ululuk niteliğini ve gerçeğe boyun eğmemeyi de içerir.","gloss":"böbürlenme ve kurumlanma","neighbor_only":"Komşu böbürlenme ile gösterişli kurumlanma davranışına yoğunlaşır.","neighbor_ref":"root_000191/B004","relation_type":"near_synonym","shared_zone":"İki dal da insanın kendisini üstün göstererek kibirli davranmasını anlatabilir."}],"source_phrase_ar":"الكبر العظمة وكذلك الكبرياء (maqayis)؛ الكبرياء اسم للتكبر والعظمة (ayn)؛ تكبر إذا تعظم (jamhara)؛ الكبر بالكسر العظمة وكذلك الكبرياء (sihah)؛ يتكبرون أي يرون أنهم أفضل الخلق (tahdhib)؛ الكبر الحالة التي يتخصص بها الإنسان من إعجابه بنفسه (mufradat)","source_summary":"Kaynaklar ululuk ve büyüklük anlamında birleşir; insan davranışında bunun kendini beğenme, üstün sayma ve büyüklük taslama biçimini aldığını belirtir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"العظمة والكبرياء والتعالي، ومنه تكبر الإنسان واستكباره عن الحق، ومنه العظمة المستحقة لله","what_is_not_ar":"ليس مجرد كبر الحجم ولا كبر السن ولا الرئاسة العملية"},"support_links":[]},{"boundary":"Her yanlış veya günah değil, büyüklüğü ve cezasının ağırlığıyla ayrılan günah bu dala girer.","branch_kind":"bare","branch_ref":"root_001281/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","surface_ar":"أَكْبَرَ"}],"gloss":"ağır cezalık büyük günah","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sıradan kusurdan ayrılan büyük ve ciddi günah temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Günahın büyüklüğü, ona bağlanan cezanın ağır olmasıyla belirginleşir."}}],"root_ar":"ك ب ر","root_id":"root_001281","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir günahın sıradan kusurlardan ayrılacak ölçüde ağır ve ciddi olduğu kastedildiğinde kullanılır.","boundary_detail":"Her yanlış veya günah değil, büyüklüğü ve cezasının ağırlığıyla ayrılan günah bu dala girer.","branch_image_ar":"الإثم الكبير والذنوب الكبائر","concept_gloss":"ağır cezalık büyük günah","contextual_glosses":[{"applicability":"Ağır yaptırıma bağlanan ciddi bir günah tekil olarak anıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sıradan günahtan ayrılan ciddi ve ağır günah kategorisini korur."},"facet_ids":["F001","F002"],"text":"büyük günah","usage_role":"general"}],"definition":"Ağırlığı ve karşılığındaki ceza büyük sayılan ciddi günah, ayrıca bu nitelikteki günahların oluşturduğu sınıftır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sıradan kusurdan ayrılan büyük ve ciddi günah temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Günahın büyüklüğü, ona bağlanan cezanın ağır olmasıyla belirginleşir."}],"identity_rationale":"Kaynak ifadesi sıradan bir yanlışın ötesinde, cezası ağır sayılan büyük günahı ve bunun çoğulunu açıkça tanımlar. Geçici çerçeve bu ahlaki ve yaptırımsal ağırlığı genel büyüklükten doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ağır cezalık büyük günah"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ağır cezalık büyük günahlar"}],"lexicalization_note":"Tanım yalın büyük günah kategorisini verir ve genel büyüklük ya da yalnız kötü sonuç fikrini bu dala taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel günah alanı ve büyük günahla kısmen örtüşen sapma alanı, ceza ağırlığı sınırını en açık gösteren adaylardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu genel günah kavramıdır; odak ise bunun içinden cezası ağır olan büyük günah sınıfını seçer.","focus_only":"Odak yalnız büyüklüğü ve cezasının ağırlığıyla ayrılan günahı kapsar.","gloss":"günah ve suç","neighbor_only":"Komşu ağır veya hafif ayrımı yapmadan günah ve suç alanını genel olarak kapsar.","neighbor_ref":"root_000521/B001","relation_type":"near_synonym","shared_zone":"Her iki dal ahlaken yanlış ve yaptırıma konu olan bir fiili günah olarak adlandırabilir."},{"boundary_match":"partial","distinction":"Odak ceza büyüklüğüne göre kurulan genel sınıftır; komşu belirli inanç ve doğruluk sapmalarına da uzanan daha karma bir alandır.","focus_only":"Odak ağır ceza ölçütüyle tanımlanmış günah kategorisidir.","gloss":"ağır günah ve sapma","neighbor_only":"Komşu büyük günah yanında ortak koşma, gerçeğe aykırı söz ve haktan sapma gibi belirli alanları da içerir.","neighbor_ref":"root_000359/B001","relation_type":"near_synonym","shared_zone":"İki dal ciddi ve büyük bir günahı anlatma noktasında örtüşür."}],"source_phrase_ar":"الكبر الإثم الكبير من الكبيرة (ayn)؛ الكبيرة من الذنوب والجمع كبائر (jamhara)؛ كبيرة من الكبائر يعني الذنوب (ayn)؛ الكبيرة متعارفة في كل ذنب تعظم عقوبته (mufradat)؛ إثم كبير (mufradat)","source_summary":"Kaynaklar büyük günah ve onun çoğul kategorisi üzerinde birleşir; toplu ifade bu büyüklüğü cezanın ağırlaşmasıyla açıklar.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"الذنب العظيم أو الكبيرة من الكبائر أو الإثم الذي تعظم عقوبته","what_is_not_ar":"ليس كل أمر كبير ولا مجرد العظمة المحمودة"},"support_links":[]},{"boundary":"Soydaki yakınlık ile doğum sırası aynı alan içindedir; son doğan ve en büyük çocuk aktarımları kaynak varyantları olarak ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_001281/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","surface_ar":"أَكْبَرَ"}],"gloss":"soy yakınlığı veya aile içi doğum sırası","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Soy zincirinde daha yakın ve öncelikli konumda bulunma anlam alanının bir bölümüdür."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aile içi söz öbeği bazı aktarımlarda son doğan çocuğu, başka bir aktarımda en büyük çocuğu bildirir."}}],"root_ar":"ك ب ر","root_id":"root_001281","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Soy zincirindeki öncelik ya da aktarıma göre ailenin en büyük veya son doğan çocuğu kastedildiğinde kullanılır.","boundary_detail":"Soydaki yakınlık ile doğum sırası aynı alan içindedir; son doğan ve en büyük çocuk aktarımları kaynak varyantları olarak ayrı tutulur.","branch_image_ar":"كبر النسب والولادة","concept_gloss":"soy yakınlığı veya aile içi doğum sırası","contextual_glosses":[{"applicability":"Soy veya bağlılık hakkının soy zincirinde daha yakın konumdaki kişiye göre belirlendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soy zincirindeki yakın ve öncelikli konumu korur."},"facet_ids":["F001"],"text":"soyda en yakın olan","usage_role":"contextual"},{"applicability":"Uyuşmayan aktarımlardaki aile içi sıra değerinin açıkça gösterilmesi gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Son doğan ve en büyük çocuk biçimindeki iki ayrı kaynak değerini uzlaştırmadan korur."},"facet_ids":["F002"],"text":"son doğan veya en büyük çocuk","usage_role":"explanatory"}],"definition":"Bir kişinin soy zincirindeki yakınlık veya aile içindeki doğum sırası bakımından belirli bir konum taşımasıdır; aktarımlar ilgili aile söz öbeğini kimi yerde son doğan, kimi yerde en büyük çocuk olarak açıklar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Soy zincirinde daha yakın ve öncelikli konumda bulunma anlam alanının bir bölümüdür."},{"facet_id":"F002","role":"source_variant","statement":"Aile içi söz öbeği bazı aktarımlarda son doğan çocuğu, başka bir aktarımda en büyük çocuğu bildirir."}],"identity_rationale":"Kaynak ifadesi soy yakınlığındaki önceliği ve en büyük çocuğu aktarırken, aynı aile içi söz öbeği için bazı aktarımlar son doğanı, bir başkası en büyük olanı bildirir. Dal soy ve doğum sırasındaki konumu ortak çatı olarak koruyabilir, ancak tek ve uzlaştırılmış bir sıra değeri ileri süremez.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"soyda en yakın olan veya en büyük evlat"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"babasının son çocuğu; başka aktarımda en büyük çocuğu"}],"lexicalization_note":"Soy bakımından öncelik bildiren biçim ile aile içi doğum sırasını bildiren kalıp ayrılır; çelişen sıra değerleri birleştirilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel akrabalık alanı ile saygın aile büyüğü alanı, soy sırası ve toplumsal konumun karıştırılmasını en iyi önler.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komşu akrabalık bağının varlığını anlatır; odak bu bağ içindeki yakınlık derecesi veya doğum sırası konumunu seçer.","focus_only":"Odak soy zincirindeki öncelik veya aile içi doğum sırasını belirler.","gloss":"soy ve kan yakınlığı","neighbor_only":"Komşu sıra belirtmeden kan ve soy yakınlığını genel olarak adlandırır.","neighbor_ref":"root_001212/B003","relation_type":"same_field","shared_zone":"İki dal da kişiler arasındaki soy bağı ve aile içindeki konumla ilgilidir."},{"boundary_match":"partial","distinction":"Doğum ve soy sırası toplumsal önderliği zorunlu kılmaz; komşu dalın çekirdeği sıra değil saygınlık ve başkanlıktır.","focus_only":"Odak aile ve soy içindeki sıra ya da yakınlık konumudur.","gloss":"saygın büyük ve önder","neighbor_only":"Komşu kişinin toplumsal saygınlık, bilgi veya önderlik bakımından yüksekliğidir.","neighbor_ref":"root_001281/B005","relation_type":"near_neighbor","shared_zone":"Ailede büyük veya soyda önde olan kişi kimi bağlamlarda toplumsal saygınlık da taşıyabilir."}],"source_phrase_ar":"الولاء للكبر يراد به أقعد القوم في النسب (maqayis)؛ الكبر أكبر ولد الرجل (ayn)؛ فلان كبرة ولد أبويه إذا كان آخرهم (sihah)؛ كبرة ولد أبيه بمعنى عجزة أي آخرهم (tahdhib)؛ هو صغرة ولد أبيه وكبرتهم أي أكبرهم (tahdhib)","source_summary":"Toplu iddia soy yakınlığı ve doğum sırasını aynı alanda toplar; aile içi sıra için kaynaklar son doğan ile en büyük çocuk arasında uzlaşmayan iki değer aktarır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"السبق أو التأخر في الولادة أو الأقعدية في النسب والولاء بحسب الصيغ المروية","what_is_not_ar":"ليس الرئاسة العامة ولا كبر السن المطلق"},"support_links":[]},{"boundary":"Bu dal Tanrı'yı belirli bir yüceltme sözüyle anma eylemidir; insan kibri veya genel büyüklük betimi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001281/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","surface_ar":"أَكْبَرَ"}],"gloss":"Tanrı'yı en büyük diye yüceltme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tanrı'yı en büyük ilan eden söz aracılığıyla yüceltme temel eylemdir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu yüceltme sözü ibadet sırasında ve ibadete çağrıda yerleşik biçimde söylenir."}}],"root_ar":"ك ب ر","root_id":"root_001281","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tanrı'nın en büyük olduğunu bildiren sözün ibadette veya başka bir durumda söylenmesi kastedildiğinde kullanılır.","boundary_detail":"Bu dal Tanrı'yı belirli bir yüceltme sözüyle anma eylemidir; insan kibri veya genel büyüklük betimi değildir.","branch_image_ar":"التكبير بقول الله أكبر","concept_gloss":"Tanrı'yı en büyük diye yüceltme","contextual_glosses":[{"applicability":"Eylemin hem söylenen içeriğinin hem de yüceltme işlevinin açıkça verilmesi gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli söz içeriğini ve bu sözü söylemenin yüceltme işlevini birlikte korur."},"facet_ids":["F001","F002"],"text":"Tanrı en büyüktür diye yüceltmek","usage_role":"explanatory"}],"definition":"Tanrı'nın en büyük olduğunu sözle ilan ederek onu yüceltmek; bu sözü ibadet, ibadete çağrı veya başka bir durumda söylemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tanrı'yı en büyük ilan eden söz aracılığıyla yüceltme temel eylemdir."},{"facet_id":"F002","role":"specialization","statement":"Bu yüceltme sözü ibadet sırasında ve ibadete çağrıda yerleşik biçimde söylenir."}],"identity_rationale":"Kaynak ifadesi Tanrı'yı en büyük ilan eden sözü söyleyerek yüceltmeyi, özellikle ibadet ve çağrı bağlamlarındaki kullanımı açıkça destekler. Geçici çerçeve bunu insanın büyüklük taslamasından ve sıradan bir büyüklük nitelemesinden doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"Tanrı'yı en büyük diye yüceltme"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"Tanrı en büyüktür"}],"lexicalization_note":"Yüceltme eylemini adlandıran biçim ile söylenen belirli ifade ayrı söz birimi yüzleri olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ululuk dalı anlam yakınlığını, ibadette susma dalı ise aynı sahnedeki karşıt söz davranışını en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta büyüklük Tanrı'ya yöneltilen bir yüceltme sözüdür; komşuda ise ululuk niteliği veya insanın üstünlük iddiası çekirdektir.","focus_only":"Odak Tanrı'yı belirli bir sözle yüceltme eylemidir.","gloss":"ululuk ve üstünlük taslama","neighbor_only":"Komşu genel ululuk niteliğini ve insanın kendini üstün görmesini kapsar.","neighbor_ref":"root_001281/B006","relation_type":"near_neighbor","shared_zone":"İki dal da büyüklük ve ululuk düşüncesini dilsel olarak işleyebilir."},{"boundary_match":"thematic_only","distinction":"Ortak alan ibadettir; odak belirli bir yüceltme sözünü üretirken komşu gündelik insan sözünü bırakmayı bildirir.","focus_only":"Odak ibadette yüceltme sözünü söylemeyi gerektirir.","gloss":"ibadette susma","neighbor_only":"Komşu ibadet sırasında insan sözünden susmayı ve ibadete yönelmeyi gerektirir.","neighbor_ref":"root_001260/B004","relation_type":"thematic","shared_zone":"Her iki dal ibadet sırasında söz ve sessizlik düzenine ilişkin bir davranışı anlatır."}],"source_phrase_ar":"التكبير في الصلاة وغيرها تفعيل من قولهم الله أكبر (jamhara)؛ التكبير التعظيم (sihah)؛ قول المصلي الله أكبر وكذلك قول المؤذن (tahdhib)؛ التكبير يقال لتعظيم الله تعالى بقولهم الله أكبر (mufradat)","source_summary":"Kaynaklar eylemi Tanrı'yı en büyük ilan eden sözle yüceltme olarak açıklar ve bunun ibadet ile ibadete çağrıdaki kullanımını belirtir.","sources":["JA","SI","TA","MU"],"what_is_ar":"تعظيم الله بالقول والعبادة، ولا سيما قول الله أكبر في الصلاة والأذان وغيرها","what_is_not_ar":"ليس تكبر الإنسان ولا مجرد وصف شيء بأنه كبير"},"support_links":[]},{"boundary":"Anlam, bir işin birine ağır ve güç gelmesidir; her tür fiziksel ağırlık veya genel zorluk bu yapı dışında kapsanmaz.","branch_kind":"collocation","branch_ref":"root_001281/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","surface_ar":"أَكْبَرَ"}],"gloss":"bir işin birine ağır ve güç gelmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işin kişi üzerinde ağır bir yük ve güçlük oluşturması yapı içindeki temel anlamdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güçlük, kişinin çağrı veya öneriyi kabul etmekte zorlanması biçiminde gerçekleşebilir."}}],"root_ar":"ك ب ر","root_id":"root_001281","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin belirli bir kişi için kabulü, taşınması veya yapılması zorlaştığında bu yapıya bağlı karşılık kullanılır.","boundary_detail":"Anlam, bir işin birine ağır ve güç gelmesidir; her tür fiziksel ağırlık veya genel zorluk bu yapı dışında kapsanmaz.","branch_image_ar":"الكبر مشقة وثقل","concept_gloss":"bir işin birine ağır ve güç gelmesi","contextual_glosses":[{"applicability":"İşin konuşan topluluk için zor, ağır veya kabul edilmesi güç olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güçlüğün belirli kişilere yönelmesini ve onlar üzerinde ağırlık oluşturmasını korur."},"facet_ids":["F001","F002"],"text":"bize çok ağır geldi","usage_role":"contextual"}],"definition":"Bir işin belirli bir kişiye büyük gelerek kabul edilmesi, taşınması veya yapılması güç ve ağır olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işin kişi üzerinde ağır bir yük ve güçlük oluşturması yapı içindeki temel anlamdır."},{"facet_id":"F002","role":"associated_use","statement":"Güçlük, kişinin çağrı veya öneriyi kabul etmekte zorlanması biçiminde gerçekleşebilir."}],"identity_rationale":"Kaynak ifadesi bir işin kişi için büyük gelmesini, bunun sonucunda kabulünün veya taşınmasının güç ve ağır olmasını belirli bir yapı içinde açıkça verir. Geçici çerçeve bu deneyimsel zorluğu salt hacim büyüklüğünden ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bize çok ağır ve güç geldi"}],"lexicalization_note":"Tanım yalnız bir işin birine büyük ve ağır gelmesini bildiren tanıklanmış yapıya bağlıdır; yalın kök anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel meşakkat ve olayın şiddeti, yapı bağı ile kişiye yönelen ağırlığı en iyi karşılaştıran iki yakın alandır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu genel güçlük alanıdır; odak yalnız bir işin belirli kişiye büyük ve ağır gelmesini bildiren yapıya bağlıdır.","focus_only":"Odak belirli bir yapıda işin kişiye ağır gelmesini bildirir.","gloss":"meşakkat ve güçlük","neighbor_only":"Komşu yolculuk ve çalışma dahil genel çaba, meşakkat ve güçlük alanını kapsar.","neighbor_ref":"root_000807/B003","relation_type":"near_synonym","shared_zone":"Her iki dal bir işin kişiyi zorlamasını ve ağır bir deneyim oluşturmasını anlatabilir."},{"boundary_match":"partial","distinction":"Komşuda olayın şiddeti çekirdektir; odakta ise işin belirli kişiye ağır gelmesi ve kabul ya da taşıma güçlüğü kurucudur.","focus_only":"Odak güçlüğü belirli bir kişiye yönelen yapı içinde kurar.","gloss":"şiddetli ve zor oluş","neighbor_only":"Komşu olayın kendi şiddetini ve ruh üzerindeki sert etkisini öne çıkarır.","neighbor_ref":"root_001008/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir olayın insan için zor ve etkisi ağır olmasını anlatır."}],"source_phrase_ar":"إذا أردت الأمر العظيم قلت كبر علينا كبارة (ayn)؛ فإذا أردت الأمر العظيم قلت كبر علينا كبارة (sihah)؛ كبر الأمر يكبر كبارة (tahdhib)؛ تستعمل الكبيرة فيما يشق ويصعب (mufradat)؛ كبر على المشركين ما تدعوهم إليه (mufradat)","source_summary":"Kaynaklar belirli yapıda bir işin büyük, ağır ve güç gelmesi üzerinde birleşir; toplu aktarım bunun bir çağrıyı kabullenme güçlüğüne uygulanmasını da içerir.","sources":["AY","SI","TA","MU"],"what_is_ar":"ما يعظم حتى يشق ويثقل أو يكبر على المرء قبوله أو حمله","what_is_not_ar":"ليس مجرد عظم الحجم ولا الإثم الكبير وحده"},"support_links":[]},{"boundary":"Bu dal karşılıklı üstünlük yarışını ve ardından gelen yenme sonucunu birlikte gerektirir.","branch_kind":"collocation","branch_ref":"root_001281/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","surface_ar":"أَكْبَرَ"}],"gloss":"üstünlük yarışına girip yenmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki kişinin üstünlük için karşı karşıya gelmesi ve birinin ötekini yenmesi tek yapının iki zorunlu aşamasıdır."}}],"root_ar":"ك ب ر","root_id":"root_001281","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşı tarafla üstünlük mücadelesine girme ve onu yenme aşamaları birlikte kastedildiğinde kullanılır.","boundary_detail":"Bu dal karşılıklı üstünlük yarışını ve ardından gelen yenme sonucunu birlikte gerektirir.","branch_image_ar":"المكابرة والغلبة","concept_gloss":"üstünlük yarışına girip yenmek","contextual_glosses":[{"applicability":"Karşı tarafın üstünlük yarışına giriştiği ve konuşanın galip geldiği anlatı bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı yarışmayı, katılımcı yönlerini ve konuşanın galibiyetini korur."},"facet_ids":["F001"],"text":"benimle yarıştı, ben de onu yendim","usage_role":"contextual"}],"definition":"Bir kişinin başkasıyla üstünlük yarışına girmesi ve karşılıklı mücadelenin sonunda onu yenmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki kişinin üstünlük için karşı karşıya gelmesi ve birinin ötekini yenmesi tek yapının iki zorunlu aşamasıdır."}],"identity_rationale":"Tek kaynaklı ifade karşılıklı üstünlük mücadelesini ve konuşanın karşı tarafı yenmesiyle sonuçlanan aşamayı açıkça verir. Geçici çerçeve bu iki katılımcılı süreç ile sonucu korur ve onu genel ululuk ya da başkanlık anlamına dönüştürmez.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"benimle üstünlük yarışına girdi, ben de onu yendim"}],"lexicalization_note":"Tanım yalnız karşılıklı yarışma ve yenme sonucunu birlikte bildiren tanıklanmış söz dizisine bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam sınır eşleşmesi gösteren yarışma yapısı ile daha geniş genel galibiyet alanı en yararlı iki karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlardaki katılımcı yapısı, mücadele aşaması ve galibiyet sonucu bakımından anlam sınırları aynıdır.","focus_only":null,"gloss":"karşılıklı yarışıp yenmek","neighbor_only":null,"neighbor_ref":"root_001028/B007","relation_type":"synonym","shared_zone":"Her iki dal iki tarafın karşılıklı üstünlük mücadelesine girmesini ve anlatıcının karşı tarafı yenmesini bildirir."},{"boundary_match":"partial","distinction":"Komşu genel galibiyet alanıdır; odak karşılıklı yarışma başlangıcını ve konuşanın sonuçtaki galibiyetini birlikte kodlayan yapıya bağlıdır.","focus_only":"Odak belirli söz dizisinde mücadeleye girişme ve ardından yenme sırasını verir.","gloss":"yenme ve baskın çıkma","neighbor_only":"Komşu genel yenme, baskın çıkma ve sözlü ya da fiili çekişmede üstün gelme alanını kapsar.","neighbor_ref":"root_001008/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir rakibe karşı üstün gelip onu yenme sonucunu anlatır."}],"source_phrase_ar":"كابرني فكبرته أي غلبته (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, karşı tarafın mücadele başlatmasını ve konuşanın onu yenmesini ardışık biçimde verir."}],"source_summary":"Bu kullanım tek bir sözlük aktarımında, karşılıklı üstünlük mücadelesi ve ardından gelen yenme sonucu olarak tanıklanır.","sources":["AY"],"what_is_ar":"مغالبة الخصم حتى يقال كابرني فكبرته أي غلبته","what_is_not_ar":"ليس الكبر بمعنى العظمة ولا الرئاسة"},"support_links":[]},{"boundary":"Bu dal yalnız tek yüzlü davul adıyla ilgilidir; büyüklük, ululuk veya büyük günah anlamı taşımaz.","branch_kind":"bare","branch_ref":"root_001281/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","surface_ar":"أَكْبَرَ"}],"gloss":"tek yüzlü davul","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Vurularak çalınan davulun tek yüzlü olması nesneyi ayıran temel özelliktir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toplu aktarım bu davul adının çoğul biçiminin de sözlüklerde verildiğini bildirir."}}],"root_ar":"ك ب ر","root_id":"root_001281","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız bir yüzü kaplı belirli davul türünün araç adı kastedildiğinde kullanılır.","boundary_detail":"Bu dal yalnız tek yüzlü davul adıyla ilgilidir; büyüklük, ululuk veya büyük günah anlamı taşımaz.","branch_image_ar":"الكَبَر طبل","concept_gloss":"tek yüzlü davul","contextual_glosses":[{"applicability":"Araç adının Türkçede açıklanarak verilmesi gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Davul türünü ve ayırıcı tek yüzlü yapısını açıkça korur."},"facet_ids":["F001"],"text":"tek yüzlü bir davul","usage_role":"explanatory"}],"definition":"Yalnız bir yüzü deriyle kaplı olan belirli bir davul türüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Vurularak çalınan davulun tek yüzlü olması nesneyi ayıran temel özelliktir."},{"facet_id":"F002","role":"source_variant","statement":"Toplu aktarım bu davul adının çoğul biçiminin de sözlüklerde verildiğini bildirir."}],"identity_rationale":"Kaynak ifadesi sözcüğü tek yüzlü bir davulun adı olarak açıkça tanımlar ve çoğul bilgisini de aynı nesne alanında verir. Geçici çerçeve bu bağımsız araç adını büyüklük ve günah dallarından doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"tek yüzlü davul"}],"lexicalization_note":"Tanım yalın araç adını verir ve herhangi bir söz öbeği ya da mecazi büyüklük anlamı eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; davulu da kapsayan geniş araç adı ile vurmalı çalgı sesi, nesne türü ve ses ayrımını en açık gösteren adaylardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak tek yüzlü davulla sınırlıdır; komşu küçük davuldan başka çalgı türlerine uzanan daha geniş ve değişken bir araç alanıdır.","focus_only":"Odak yalnız tek yüzlü olan belirli davul türünü bildirir.","gloss":"davul ve başka çalgılar","neighbor_only":"Komşu davul yanında telli ve üflemeli çalgılara kadar uzanan değişken bir araç adını kapsar.","neighbor_ref":"root_001328/B002","relation_type":"near_synonym","shared_zone":"Her iki dal vurmalı bir çalgı olarak davulu adlandırabilir."},{"boundary_match":"thematic_only","distinction":"Odak somut bir davul türüdür; komşu farklı bir çalgıdan çıkan sesi bildirir ve nesne adı değildir.","focus_only":"Odak vurmalı çalgının kendisini adlandırır.","gloss":"zil çınlaması","neighbor_only":"Komşu zilden çıkan çınlama sesini adlandırır.","neighbor_ref":"root_000897/B009","relation_type":"thematic","shared_zone":"İki dal müzikte vurmayla ses çıkaran araçların bulunduğu aynı ses ortamına katılır."}],"source_phrase_ar":"الكبر طبل له وجه (ayn)؛ الكبر الطبل الذي له وجه واحد (tahdhib)؛ الكبر الطبل وجمعه كبار (tahdhib)","source_summary":"Kaynaklar sözcüğü tek yüzlü bir davul olarak tanımlar; toplu aktarım ayrıca aynı araç adının çoğul biçimini kaydeder.","sources":["AY","TA"],"what_is_ar":"الكَبَر اسم طبل له وجه واحد وجمعه كبار بحسب النقل المعجمي","what_is_not_ar":"ليس الكبر بمعنى العظمة ولا الكبر بمعنى الإثم"},"support_links":[]},{"boundary":"Bu dal yalnız gün yükseldikten sonraki vakti bildiren zaman sözüdür; bütün gün veya gün batımı değildir.","branch_kind":"collocation","branch_ref":"root_001281/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","surface_ar":"أَكْبَرَ"}],"gloss":"günün yükseldiği vakit","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gün ışığının yükselmesiyle belirlenen gün içi zaman noktası temel anlamdır."}}],"root_ar":"ك ب ر","root_id":"root_001281","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir olayın sabahın ilerleyip günün yükseldiği evrede gerçekleştiği kastedildiğinde kullanılır.","boundary_detail":"Bu dal yalnız gün yükseldikten sonraki vakti bildiren zaman sözüdür; bütün gün veya gün batımı değildir.","branch_image_ar":"أكبر النهار","concept_gloss":"günün yükseldiği vakit","contextual_glosses":[{"applicability":"Bir eylemin günün yükselmiş olduğu sabah evresinde gerçekleştiği anlatı bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemin zamanını günün yükselme evresine yerleştirir."},"facet_ids":["F001"],"text":"gün yükselirken","usage_role":"contextual"}],"definition":"Günün yükselip ilerlemeye başladığı, sabahın artık belirgin biçimde yükseldiği vakittir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gün ışığının yükselmesiyle belirlenen gün içi zaman noktası temel anlamdır."}],"identity_rationale":"Tek kaynaklı ifade günün yükseldiği vakti iki eşdeğer zaman sözüyle açıkça tanımlar. Geçici çerçeve bu gün içi evreyi yaş, önem veya günün tamamı anlamlarından doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"günün yükseldiği vakit"}],"lexicalization_note":"Tanım yalnız günün yükseldiği vakti bildiren tanıklanmış zaman sözüne bağlıdır ve yalın büyüklük anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; günün yükselmesi olayı ile gündüzün tamamı, zaman sözünün evre ve süre sınırını en açık gösteren iki komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu yükselme olayını anlatır; odak bu olayla belirlenen vakitte bir şeyin gerçekleşmesini bildiren zaman sözüdür.","focus_only":"Odak günün yükselmesini belirli bir zaman sözü olarak kullanır.","gloss":"günün yükselmesi","neighbor_only":"Komşu günün yükselmesi olayını doğrudan bildirir.","neighbor_ref":"root_000782/B005","relation_type":"near_synonym","shared_zone":"İki dal da gün ışığının yükseldiği sabah evresini temel alır."},{"boundary_match":"field_only","distinction":"Komşu bütün gündüz süresidir; odak bu sürenin yalnız yükselen sabah bölümündeki belirli vakittir.","focus_only":"Odak günün içindeki yükselme evresini seçer.","gloss":"gündüzün tamamı","neighbor_only":"Komşu güneşin doğuşundan batışına kadar olan günün tamamını adlandırır.","neighbor_ref":"root_001700/B001","relation_type":"same_field","shared_zone":"Her iki dal gündüz zamanının sınırlandırılması ve bir vaktin belirlenmesiyle ilgilidir."}],"source_phrase_ar":"أكبر النهار وشباب النهار أي حين ارتفع النهار (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, ziyaret vaktini günün yükselmiş olduğu evreyle açıklar."}],"source_summary":"Bu zaman sözü tek bir sözlük aktarımında, günün yükseldiği vakit olarak tanıklanır ve günün gençliğiyle eşdeğer gösterilir.","sources":["TA"],"what_is_ar":"أكبر النهار أو شباب النهار حين يرتفع النهار","what_is_not_ar":"ليس كبر السن ولا كبر الشأن"},"support_links":[]},{"boundary":"Atonement or expiation that covers, effaces, or removes sin, oath liability, or wrongdoing.","branch_kind":null,"branch_ref":"root_001307/B009","candidate_links":[{"candidate_id":"cand_d4f39ffb0b40140e2a26","lane":"macro"}],"focus_root_occurrences":[],"gloss":"covering or effacing sin","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"محو الإثم بتغطيته","image_en":"covering or effacing sin"}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"محو الإثم بتغطيته","image_en":"covering or effacing sin","scope_ar":"يدخل فيه الكفارة لما يكفر الخطيئة أو اليمين والتكفير للسيئات والمعاصي حتى تصير كأن لم تعمل","scope_en":"Atonement or expiation that covers, effaces, or removes sin, oath liability, or wrongdoing."},"support_links":["sup_2bd954b82da380d10d2a"]},{"boundary":"Includes conferring, granting, assigning, or directing good or evil to someone.","branch_kind":null,"branch_ref":"root_001684/B013","candidate_links":[{"candidate_id":"cand_d4f39ffb0b40140e2a26","lane":"macro"}],"focus_root_occurrences":[],"gloss":"granting or assigning something","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"إيلاء وإسناد معروف أو شر","image_en":"granting or assigning something"}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"إيلاء وإسناد معروف أو شر","image_en":"granting or assigning something","scope_ar":"يدخل فيه أوليته الشيء أو معروفا أو خيرا أو شرا بمعنى جعلته له أو أسديته إليه","scope_en":"Includes conferring, granting, assigning, or directing good or evil to someone."},"support_links":["sup_2bd954b82da380d10d2a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000065/B001","candidate_links":[{"candidate_id":"cand_a3eb339df6f5c9fde9b0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d590337796d5514c97f5","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Return to a destination supplies the movement back into divine jurisdiction.","root":"ء و ب","source_ref":"88:25","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000065","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4c37eec3c70b74c43d7f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000318/B001","candidate_links":[{"candidate_id":"cand_a3eb339df6f5c9fde9b0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d590337796d5514c97f5","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Counting and accounting supply the final adjudicative function assigned to the divine side.","root":"ح س ب","source_ref":"88:26","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000318","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4c37eec3c70b74c43d7f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000516/B009","candidate_links":[{"candidate_id":"cand_a3eb339df6f5c9fde9b0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d590337796d5514c97f5","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Reminder as what makes one remember supplies the messenger's positively assigned function.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000516","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4c37eec3c70b74c43d7f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000704/B003","candidate_links":[{"candidate_id":"cand_a3eb339df6f5c9fde9b0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d590337796d5514c97f5","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The controlling overseer supplies the authority specifically denied to the reminder.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000704","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4c37eec3c70b74c43d7f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001307/B003","candidate_links":[{"candidate_id":"cand_a3eb339df6f5c9fde9b0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d590337796d5514c97f5","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Concealing the truth supplies the accountable obstruction attributed to the refuser.","root":"ك ف ر","source_ref":"88:23","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001307","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4c37eec3c70b74c43d7f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001390/B001","candidate_links":[{"candidate_id":"cand_a3eb339df6f5c9fde9b0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d590337796d5514c97f5","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Negation of a present state supplies the explicit removal of coercive status.","root":"ل ي س","source_ref":"88:22","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001390","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4c37eec3c70b74c43d7f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001684/B007","candidate_links":[{"candidate_id":"cand_a3eb339df6f5c9fde9b0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d590337796d5514c97f5","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Turning away supplies the addressee's own refusal rather than an act produced by the reminder.","root":"و ل ي","source_ref":"88:23","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001684","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4c37eec3c70b74c43d7f"]}],"candidate_inventory":[{"anchor_refs":["88:17","88:23","88:24","88:25"],"branch_refs":["root_000047/B002","root_001307/B009","root_001684/B013"],"candidate_id":"cand_d4f39ffb0b40140e2a26","commentary_obligation":"review","focus_branch_refs":["root_000047/B002"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001307/B009","root_001684/B013"],"root_ids":[],"scope":"pericope","source_local_id":"D:Oath and Expiation","source_type":"channel","support_ids":["sup_2bd954b82da380d10d2a","sup_2c8868bb77fbb62054f5","sup_85cb12b53daa99256103","sup_8c0410c7bd9628698548","sup_b1e1cf079c4cc549c3a6"],"title":"Oath and Expiation","trust":"trusted","unresolved_branch_citations":[{"citation":"ء ل ي/B007","reason":"no registered branch match"}],"unresolved_branch_refs":[]},{"anchor_refs":["88:18","88:20","88:24"],"branch_refs":["root_000025/B001","root_000745/B004","root_000994/B004"],"candidate_id":"cand_0bb75bdb84d64cf1228b","commentary_obligation":"review","focus_branch_refs":["root_000994/B004"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000025/B001","root_000745/B004"],"root_ids":[],"scope":"pericope","source_local_id":"E:Exposure Beneath the Sky","source_type":"channel","support_ids":["sup_0aded112a7803783e8e1","sup_39a8da1f1463562670b9","sup_703c0f12f291a80cd556","sup_af13f67dc9e4f4f956e8","sup_c788ad6253c6aba53714"],"title":"Exposure Beneath the Sky","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:21","88:22","88:23","88:24","88:25","88:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:24","branch_refs":["root_000047/B002","root_000065/B001","root_000318/B001","root_000516/B009","root_000704/B003","root_000994/B005","root_001307/B003","root_001390/B001","root_001684/B007"],"candidate_id":"cand_a3eb339df6f5c9fde9b0","commentary_obligation":"review","hft_ref":"hft_d590337796d5514c97f5","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_jurisdictional_handoff","source_type":"hft","support_ids":["sup_4c37eec3c70b74c43d7f"],"title":"delta_jurisdictional_handoff","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_0216a0cf01d4ada0d555","connection_ref":"conn_3613afabcac9466a2db1","note":"States the immediate condition, turning away and disbelief, before the focus.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_ab0f7d9f16556d1c1322","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:23","source_note":"The immediately following maximum-punishment clause completes 88:23's consequence.","source_row_role":"ranked_review","source_target_component_ref":"88:24","source_target_components":["88:24"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:24"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:23","source_target_components":["88:23"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:23","target_evidence":{"arabic_uthmani":"إِلَّا مَن تَوَلَّىٰ وَكَفَرَ","ayah_ref":"88:23"},"target_ref":"88:23"},{"connection_evidence_ref":"conn_ev_d3c5ff4f08f5ddbaf6ba","connection_ref":"conn_3f2553e73b935e2cd9e3","note":"Contrasts the messenger's lack of control with Allah's role in the focus.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_9438af347addaf3281a7","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:22","source_note":"The next verse assigns the greatest punishment explicitly to Allah.","source_row_role":"ranked_review","source_target_component_ref":"88:24","source_target_components":["88:24"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:24"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:22","source_target_components":["88:22"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:22","target_evidence":{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","ayah_ref":"88:22"},"target_ref":"88:22"},{"connection_evidence_ref":"conn_ev_8bedca8654c3c00bed0c","connection_ref":"conn_4798b801f07d760261ed","note":"Places the focus after the surah's call to attend to created signs.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_298f6c1a319db8871e09","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"88:18","source_note":"Judgment context is too indirect for the sky's elevation.","source_row_role":"ranked_review","source_target_component_ref":"88:24","source_target_components":["88:24"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:24"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:18","source_target_components":["88:18"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:18","target_evidence":{"arabic_uthmani":"وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ","ayah_ref":"88:18"},"target_ref":"88:18"},{"connection_evidence_ref":"conn_ev_53f0e7e38efb2f426c2e","connection_ref":"conn_bd6057d50a070248af38","note":"Begins the immediate sequence of signs preceding the response and consequence.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_c135b7290e736df635a8","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"88:17","source_note":"Punishment does not clarify observing the camel's creation.","source_row_role":"ranked_review","source_target_component_ref":"88:24","source_target_components":["88:24"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:24"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:17","source_target_components":["88:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:17","target_evidence":{"arabic_uthmani":"أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ","ayah_ref":"88:17"},"target_ref":"88:17"},{"connection_evidence_ref":"conn_ev_9f15880f79924a04a3de","connection_ref":"conn_9670165a4e109031f9ec","note":"Completes the immediate sequence of signs preceding the focus.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_0665f7330f26b4e92e41","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:20","source_note":"Later consequence contrasts with the focus's invitation to observe, but adds little detail.","source_row_role":"ranked_review","source_target_component_ref":"88:24","source_target_components":["88:24"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:24"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:20","source_target_components":["88:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:20","target_evidence":{"arabic_uthmani":"وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ","ayah_ref":"88:20"},"target_ref":"88:20"},{"connection_evidence_ref":"conn_ev_fe98b16938ca462c82b9","connection_ref":"conn_14ebbc749dc84de73ec7","note":"Continues the immediate signs that precede the focus's response and consequence.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_91363615ec911a380278","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"88:19","source_note":"No distinct addition to the mountain's placement or function.","source_row_role":"ranked_review","source_target_component_ref":"88:24","source_target_components":["88:24"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:24"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:19","source_target_components":["88:19"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:19","target_evidence":{"arabic_uthmani":"وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ","ayah_ref":"88:19"},"target_ref":"88:19"}],"focus":{"arabic_uthmani":"فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"88:24:1:1","qac_word_ref":"88:24:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:24:1:2","qac_word_ref":"88:24:1","root_ar":"ع ذ ب","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:24:1:3","qac_word_ref":"88:24:1","root_ar":"","surface_ar":"هُ"},{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"88:24:2:1","qac_word_ref":"88:24:2","root_ar":"ء ل ه","surface_ar":"ٱللَّهُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"88:24:3:1","qac_word_ref":"88:24:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:24:3:2","qac_word_ref":"88:24:3","root_ar":"ع ذ ب","surface_ar":"عَذَابَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"88:24:4:1","qac_word_ref":"88:24:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","root_ar":"ك ب ر","surface_ar":"أَكْبَرَ"}],"word_analysis_qac_refs":[["88:24:1:1"],["88:24:1:2","88:24:1:3"],["88:24:2:1"],["88:24:3:1","88:24:3:2"],["88:24:4:1","88:24:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:24:1","88:24:2","88:24:3","88:24:4","88:24:5"]},"focus_surface_evidence":{"arabic_uthmani":"فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"88:24:1:1","qac_word_ref":"88:24:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:24:1:2","qac_word_ref":"88:24:1","root_ar":"ع ذ ب","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:24:1:3","qac_word_ref":"88:24:1","root_ar":"","surface_ar":"هُ"},{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"88:24:2:1","qac_word_ref":"88:24:2","root_ar":"ء ل ه","surface_ar":"ٱللَّهُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"88:24:3:1","qac_word_ref":"88:24:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:24:3:2","qac_word_ref":"88:24:3","root_ar":"ع ذ ب","surface_ar":"عَذَابَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"88:24:4:1","qac_word_ref":"88:24:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَكْبَر","morph_features":"STEM|POS:ADJ|LEM:>akobar|ROOT:kbr|MS|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:24:4:2","qac_word_ref":"88:24:4","root_ar":"ك ب ر","surface_ar":"أَكْبَرَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:24:1:1"],["88:24:1:2","88:24:1:3"],["88:24:2:1"],["88:24:3:1","88:24:3:2"],["88:24:4:1","88:24:4:2"]],"word_analysis_refs":["88:24:1","88:24:2","88:24:3","88:24:4","88:24:5"],"word_rows":[{"analysis_record_ref":"88:24:1","analytic_gloss_range_en":"prefixed consequence particle linking the punishment clause to the prior exception and refusal frame","analytic_root_gloss_range_en":null,"qac_refs":["88:24:1:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"88:24:2","analytic_gloss_range_en":"Form II punitive infliction on a singular attached patient, immediately under the consequence frame and anticipating a same-root punishment noun","analytic_root_gloss_range_en":"broad root range includes sweet or fresh palatability, abstention, withholding, uncoveredness, punishment and torment, and other branch images; the local Form II verb selects punitive infliction while the pleasant pole survives only as reversal-pressure","qac_refs":["88:24:1:2","88:24:1:3"],"root":{"arabic":"ع ذ ب","transliteration":"ʿ-dh-b"},"surface":{"arabic":"يُعَذِّبُهُ","transliteration":"yuʿadhdhibuhu"}},{"analysis_record_ref":"88:24:3","analytic_gloss_range_en":"proper divine name as explicit nominative agent of the punishment verb, centered between act and named punishment","analytic_root_gloss_range_en":"root field associated with deity, worshipward orientation, refuge, and related derivational debate; local use is the proper divine name functioning as agent, not a generic deity category","qac_refs":["88:24:2:1"],"root":{"arabic":"أ ل ه","transliteration":"ʾ-l-h"},"surface":{"arabic":"ٱللَّهُ","transliteration":"Allāhu"}},{"analysis_record_ref":"88:24:4","analytic_gloss_range_en":"definite cognate punishment noun naming the punitive event imposed by the verb and serving as head for the final elative adjective","analytic_root_gloss_range_en":"broad root range includes sweet or fresh palatability, abstention, withholding, uncoveredness, punishment and torment, and other branch images; the local verbal noun selects the punishment branch while nonpunitive branches remain only contrastive background","qac_refs":["88:24:3:1","88:24:3:2"],"root":{"arabic":"ع ذ ب","transliteration":"ʿ-dh-b"},"surface":{"arabic":"ٱلْعَذَابَ","transliteration":"al-ʿadhāba"}},{"analysis_record_ref":"88:24:5","analytic_gloss_range_en":"definite elative adjective modifying the punishment noun, ranking it as greater or greatest in severity and closing the clause","analytic_root_gloss_range_en":"root range includes greatness, largeness, rank, reverence, self-magnification, major gravity, hardship, and formulaic magnification; the local elative adjective selects ranked punitive severity rather than age, leadership, drum, or other nonlocal branches","qac_refs":["88:24:4:1","88:24:4:2"],"root":{"arabic":"ك ب ر","transliteration":"k-b-r"},"surface":{"arabic":"ٱلْأَكْبَرَ","transliteration":"al-akbara"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":6,"missing_anchor_refs":[],"supplied_unique_anchor_count":6},"assigned_record_count":1,"assigned_records":[{"anchor_refs":["88:21","88:22","88:23","88:24","88:25","88:26"],"branch_refs":["root_000047/B002","root_000065/B001","root_000318/B001","root_000516/B009","root_000704/B003","root_000994/B005","root_001307/B003","root_001390/B001","root_001684/B007"],"candidate_id":"cand_a3eb339df6f5c9fde9b0","evidence_scope":"declared_pericope","hft_ref":"hft_d590337796d5514c97f5","item_id":"delta_jurisdictional_handoff","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_jurisdictional_handoff","support_id":"sup_4c37eec3c70b74c43d7f"}],"diagnostics":[],"lane_counts":{"global":19,"macro":1,"micro":3},"packet_summary":{"ayah_count":26,"focus_ref":"88:24","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:24","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"88:24","lane":"macro","linguistic_source_ref":"88:24","surface_ref":"88:24","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:24","target_tokens":[["Allah",["88:24:2"]],["da",["88:24:1"]],["onu",["88:24:1"]],["en",["88:24:4"]],["büyük",["88:24:4"]],["cezayla",["88:24:3"]],["cezalandırır",["88:24:1"]]],"text":"Allah da onu en büyük cezayla cezalandırır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":1,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":17,"ayah_to":26,"id":"s088-p02-017-026","label":"Creation signs and the duty to remind","number":2,"refs":["88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"88:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"88:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["88:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"88:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"E:Exposure Beneath the Sky","source_type":"channel","support_id":"sup_0aded112a7803783e8e1","text":"An uncovered object or place stands open beneath the overhead sky.","trust":"trusted"},{"branch_refs":["root_000047/B002","root_001307/B009","root_001684/B013"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"D:Oath and Expiation","source_type":"channel","support_id":"sup_2bd954b82da380d10d2a","text":"oath `ء ل ي:B007/m01`; divine invocation `ء ل ه:B002/m01`; expiation `ك ف ر:B009/m01`; assigned pledge `و ل ي:B013/m02`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Oath and Expiation","source_type":"channel","support_id":"sup_2c8868bb77fbb62054f5","text":"A person directs worship, sacrifice, blessing, or sworn obligation toward a sacred addressee and becomes answerable for the act.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"E:Exposure Beneath the Sky","source_type":"channel","support_id":"sup_39a8da1f1463562670b9","text":"A layer, enclosure, or obscurity limits access to what lies within.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"E:Exposure Beneath the Sky","source_type":"channel","support_id":"sup_703c0f12f291a80cd556","text":"88:18 `السماء` (`س م و`); 88:20 `الأرض` (`ء ر ض`); 88:24 `العذاب` (`ع ذ ب`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Oath and Expiation","source_type":"channel","support_id":"sup_85cb12b53daa99256103","text":"Invocation, commitment, assigned liability, and expiation form a complete cycle of sworn responsibility.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Oath and Expiation","source_type":"channel","support_id":"sup_8c0410c7bd9628698548","text":"A speaker invokes the divine name, assumes a sworn obligation, and must discharge or expiate it.","trust":"trusted"},{"branch_refs":["root_000025/B001","root_000745/B004","root_000994/B004"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"E:Exposure Beneath the Sky","source_type":"channel","support_id":"sup_af13f67dc9e4f4f956e8","text":"exposed to the sky `ع ذ ب:B004/m01`; overhead expanse `س م و:B004/m01`; lower ground beneath it `ء ر ض:B001/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Oath and Expiation","source_type":"channel","support_id":"sup_b1e1cf079c4cc549c3a6","text":"88:17-20, 88:25 `إلى`, `إلينا` (`ء ل ي`); 88:24 `الله` (`ء ل ه`); 88:23 `كفر` (`ك ف ر`); 88:23 `تولى` (`و ل ي`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"E:Exposure Beneath the Sky","source_type":"channel","support_id":"sup_c788ad6253c6aba53714","text":"Exposure reverses the covering relation: the lower surface remains directly open to what arches above it.","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","ayah_ref":"88:21"},{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","ayah_ref":"88:22"},{"arabic_uthmani":"إِلَّا مَن تَوَلَّىٰ وَكَفَرَ","ayah_ref":"88:23"},{"arabic_uthmani":"فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ","ayah_ref":"88:24"},{"arabic_uthmani":"إِنَّ إِلَيْنَآ إِيَابَهُمْ","ayah_ref":"88:25"},{"arabic_uthmani":"ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم","ayah_ref":"88:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":6,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":6,"target_morphology_supplied":false},"branch_refs":["root_000047/B002","root_000065/B001","root_000318/B001","root_000516/B009","root_000704/B003","root_000994/B005","root_001307/B003","root_001390/B001","root_001684/B007"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000047","role":"The fixed divine name explicitly assigns the punitive act to Allah.","root":"ء ل ه","source_ref":"88:24","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_000994","role":"Punishment supplies the sanction whose proper agent and place in the sequence are delimited.","root":"ع ذ ب","source_ref":"88:24","source_word_indices":["1","3"]},{"branch_id":"B009","mapped_root_id":"root_000516","role":"Reminder as what makes one remember supplies the messenger's positively assigned function.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]},{"branch_id":"B001","mapped_root_id":"root_001390","role":"Negation of a present state supplies the explicit removal of coercive status.","root":"ل ي س","source_ref":"88:22","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000704","role":"The controlling overseer supplies the authority specifically denied to the reminder.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]},{"branch_id":"B007","mapped_root_id":"root_001684","role":"Turning away supplies the addressee's own refusal rather than an act produced by the reminder.","root":"و ل ي","source_ref":"88:23","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001307","role":"Concealing the truth supplies the accountable obstruction attributed to the refuser.","root":"ك ف ر","source_ref":"88:23","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000065","role":"Return to a destination supplies the movement back into divine jurisdiction.","root":"ء و ب","source_ref":"88:25","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000318","role":"Counting and accounting supply the final adjudicative function assigned to the divine side.","root":"ح س ب","source_ref":"88:26","source_word_indices":["4"]}],"changed_reading":{"after":"The focus instead seals a division of authority: the messenger reminds but does not control; the refuser chooses turning and concealment; Allah alone punishes, receives the return, and accounts.","before":"The threat could be heard as intensifying the preceding address into a mandate to compel."},"confidence":"strong","mechanism":"The reminder is assigned to the human addressee, control is explicitly negated, refusal is assigned to the one who turns away and covers, and punishment, return, and accounting are assigned to Allah. The focus is therefore a jurisdictional transfer, not an extension of human coercive authority.","model_id":"delta_jurisdictional_handoff","reader_inference":"The packet supplies restricted reminder, negated control, refusal, explicit divine agency, return, and accounting; I infer a jurisdictional handoff that blocks human enforcement from the focus threat. A live alternative concerns the exact syntactic reach of the exception in 88:23, but no reading erases the explicit subject shift in 88:24.","status":"strengthened","structural_cues":["إِنَّمَا in 88:21 restricts the human role, and لَّسْتَ in 88:22 negates control.","The grammatical subject changes to ٱللَّهُ in 88:24, followed by إِلَيْنَا in 88:25 and عَلَيْنَا in 88:26.","The object pronoun in يُعَذِّبُهُ links the sanction to the singular refuser of 88:23 without transferring agency to the reminder."],"trigger_roots":["ذ ك ر","ل ي س","س ط ر","و ل ي","ك ف ر","ء و ب","ح س ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_jurisdictional_handoff","source_type":"hft","support_id":"sup_4c37eec3c70b74c43d7f","trust":"legacy_unbound"}]}
</lane_packet_json>
