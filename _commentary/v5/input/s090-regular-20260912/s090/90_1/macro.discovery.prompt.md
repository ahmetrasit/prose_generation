# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **90:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s090-regular-20260912/s090/90_1/macro.discovery.json` and modify nothing
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
  "ayah_ref": "90:1",
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
{"branch_registry":[{"boundary":"Dal, göğüs bölgesini, kaş arası açıklığı ve göksel durağı değil, yeryüzündeki sınırlı yeri ve buna bağlı özel adlandırmaları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000148/B001","candidate_links":[{"candidate_id":"cand_c68d843c1c65d54b69b7","lane":"macro"},{"candidate_id":"cand_5f655045bc1def917c73","lane":"macro"},{"candidate_id":"cand_9438f41b241fdc6c7539","lane":"macro"},{"candidate_id":"cand_b610bfdccb8389cabf39","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:1:4:2","qac_word_ref":"90:1:4","surface_ar":"بَلَدِ"}],"gloss":"sınırları belirli yer; ayrıca mezarlık, mezar, toprak veya açık alan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, sınırları seçilebilen ve yerleşim durumu anlamı değiştirmeyen bir yeryüzü parçasıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Mezarlık, tek bir mezar ve toprak da bu adla anılabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yerleşim dışındaki açık ve çıplak alan da özel bir kullanım olarak kapsama girer."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın genel yer çekirdeğini ve kaynaklarda ayrıca verilen özel yer adlandırmalarını birlikte temsil eder.","boundary_detail":"Dal, göğüs bölgesini, kaş arası açıklığı ve göksel durağı değil, yeryüzündeki sınırlı yeri ve buna bağlı özel adlandırmaları kapsar.","branch_image_ar":"الموضع المحدود من الأرض","concept_gloss":"sınırları belirli yer; ayrıca mezarlık, mezar, toprak veya açık alan","contextual_glosses":[{"applicability":"Yerleşim durumundan bağımsız olarak genel coğrafi çekirdeğin anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mezarlık, mezar, toprak ve açık alan için verilen özel kullanımları dışarıda bırakır.","preserves":"Sınırlı yeryüzü parçası olan temel anlamı korur."},"facet_ids":["F001"],"text":"sınırları belirli yeryüzü parçası","usage_role":"general"},{"applicability":"Sözcüğün yerleşim dışındaki geniş ve açık bir alanı gösterdiği özel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel sınırlı yer anlamını ve mezarlık, mezar ile toprak kullanımlarını vermez.","preserves":"Açık alan için verilen özel kullanımı korur."},"facet_ids":["F003"],"text":"açık, çıplak alan","usage_role":"contextual"}],"definition":"Bayındır veya bayındır olmayan, boş veya yerleşilmiş olabilen, sınırları belirli bir yeryüzü parçasıdır. Aynı ad mezarlık, mezar, toprak veya açık alan için de özel olarak kullanılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, sınırları seçilebilen ve yerleşim durumu anlamı değiştirmeyen bir yeryüzü parçasıdır."},{"facet_id":"F002","role":"extension","statement":"Mezarlık, tek bir mezar ve toprak da bu adla anılabilir."},{"facet_id":"F003","role":"extension","statement":"Yerleşim dışındaki açık ve çıplak alan da özel bir kullanım olarak kapsama girer."}],"identity_rationale":"Kaynak ifade, yerleşilmiş olup olmamasına bakılmaksızın sınırları belirli bir yeryüzü parçasını çekirdek anlam olarak verir; mezarlık, mezar, toprak ve açık alan kullanımlarını da ayrıca bildirir. Bu nedenle dal korunabilir, ancak ikincil adlandırmalar genel yer anlamıyla özdeşleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yerleşilmiş ya da boş, sınırları belirli yer"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yerler, yöreler"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"mezarlık, mezar veya toprak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"açık, çıplak alan"}],"lexicalization_note":"Temel biçimler sınırlı yeryüzü parçasını gösterir; mezarlık, mezar, toprak ve açık alan anlamları ayrı sözlüksel kullanımlardır ve çekirdeğin bütün kapsamına genellenmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel yeryüzü ile işlenmemiş arazi adayları sınırı en iyi aydınlattığı için seçildi, öteki adaylar yalnızca belirli arazi türleri ya da aynı kökün ayrı anlamlarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak, sınırları belirli bir yer birimini adlandırır; komşu ise bütün yeryüzünü veya göğe göre aşağı konumu anlatır.","focus_only":"Odak dalı, çevresi belirlenmiş bir yeri ve mezar ya da açık alan gibi özel adlandırmaları içerir.","gloss":"yeryüzü ve aşağı taraf","neighbor_only":"Komşu dal, göğün karşısındaki bütün yeryüzünü ve genel olarak aşağıda olanı kapsar.","neighbor_ref":"root_000025/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da yeryüzündeki alanlardan söz edebilir."},{"boundary_match":"partial","distinction":"Komşunun bayındır veya yerleşilmiş olmama koşulu zorunludur; odakta böyle bir koşul yoktur.","focus_only":"Odak yerleşilmiş veya boş her türlü sınırlı yeri kapsar.","gloss":"bayındır veya yerleşilmiş olmayan arazi","neighbor_only":"Komşu yalnızca bayındır veya yerleşilmiş olmayan araziyi belirtir.","neighbor_ref":"root_001535/B011","relation_type":"near_synonym","shared_zone":"Bayındır veya yerleşilmiş olmayan bir arazi iki dalın da kapsamına girebilir."}],"source_phrase_ar":"البلد معروف والبلدة أيضا والبلاد جمع بلد (jamhara)؛ البلد كل موضع مستحيز من الأرض عامر أو غير عامر أو خال أو مسكون (tahdhib)؛ البلد المكان المحيط المحدود المتأثر باجتماع قطانه وإقامتهم فيه (mufradat)؛ البلد المقبرة ويقال هو نفس القبر وربما جاء البلد يعني به التراب (tahdhib)؛ من البلد وهو الفضاء البراز (maqayis)","source_summary":"Kaynaklar sınırlı yeryüzü parçası anlamında birleşir ve bu parçanın bayındır veya bayındır olmayan, boş veya yerleşilmiş olabileceğini gösterir. Toprak, mezarlık, mezar ve açık alan kullanımları çekirdeğe bağlı özel genişlemelerdir.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه البلد والبلدة والبلاد والبلدان، وكل موضع من الأرض عامر أو غير عامر أو خال أو مسكون، والمفازة، والمقبرة والقبر، والتراب، والفضاء البراز.","what_is_not_ar":"ليس فيه الصدر ولا البلجة ولا منزلة القمر إلا من جهة التشبيه أو التسمية الخاصة."},"support_links":["sup_2845fd15b54a3d723e25","sup_41535c4caf8fdf90a0b4","sup_54154efd8595ba64b78d","sup_bd1e762a3efedbfb8e99"]},{"boundary":"Dal genel bir yer adını değil, göğüs ve boğaz altı bölgesini; eylem kalıbında ise devenin bu bölgeyi yere koymasını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000148/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:1:4:2","qac_word_ref":"90:1:4","surface_ar":"بَلَدِ"}],"gloss":"göğüs ve boğaz altındaki göğüs çukuru; devede göğsü yere koyma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, göğüs ile boğaz altındaki orta çukur ve çevresidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad, insan göğsüne ve hayvanın göğüs altındaki etli bölümüne uygulanabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Devenin çökerken göğsünü yere koyması belirli bir söz kalıbıyla ifade edilir."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Beden bölgesini ve yalnızca ilgili eylem kalıbında görülen deve hareketini birlikte kapsar.","boundary_detail":"Dal genel bir yer adını değil, göğüs ve boğaz altı bölgesini; eylem kalıbında ise devenin bu bölgeyi yere koymasını kapsar.","branch_image_ar":"الصدر وبلدة النحر","concept_gloss":"göğüs ve boğaz altındaki göğüs çukuru; devede göğsü yere koyma","contextual_glosses":[{"applicability":"Beden bölgesinin dar ve anatomik olarak belirli merkezi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Göğsün daha geniş kullanımını ve devenin çöküş eylemini dışarıda bırakır.","preserves":"Boğaz altındaki orta göğüs bölgesini korur."},"facet_ids":["F001"],"text":"boğazın altındaki göğüs çukuru","usage_role":"contextual"}],"definition":"Göğsün, özellikle boğazın altındaki çukurun ve çevresinin bulunduğu ön beden bölgesidir. Devenin çöküşünde bu bölgeyi yere koyması ayrıca kalıplaşmış bir eylem olarak anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, göğüs ile boğaz altındaki orta çukur ve çevresidir."},{"facet_id":"F002","role":"extension","statement":"Ad, insan göğsüne ve hayvanın göğüs altındaki etli bölümüne uygulanabilir."},{"facet_id":"F003","role":"associated_use","statement":"Devenin çökerken göğsünü yere koyması belirli bir söz kalıbıyla ifade edilir."}],"identity_rationale":"Kaynak ifade, göğsü ve özellikle boğaz altındaki göğüs çukurunu temel beden bölgesi olarak verir; insan göğsüne aktarımı, hayvanın göğüs altı bölgesini ve devenin çökerken göğsünü yere koymasını da açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"boğazın altındaki göğüs çukuru ve çevresi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"göğüs"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"deve çökerken göğsünü yere koydu"}],"lexicalization_note":"Bağımsız biçim göğsü gösterebilir; boğaz altı merkezi ve devenin göğsünü yere koyması yalnız kendi kalıplarında okunmalı, bütün dala genellenmemelidir.","neighbor_coverage_note":"Bütün beden bölgesi ve kök içi adaylar değerlendirildi; boğaz önü ile genel göğüs adayları en yakın sınır karşılaştırmalarını sağladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak göğüs çukuru merkezli ve belirli bir deve eylemine bağlıdır; komşu boğaz önü ve kesim yeri merkezlidir.","focus_only":"Odak, bütün göğse aktarılabilir ve devenin çökerken göğsünü yere koyması kullanımını içerir.","gloss":"boğaz önü ve üst göğüs","neighbor_only":"Komşu, boğaz önü ile üst göğsü, kesim yerini ve kolye bölgesini daha geniş ayrıntıyla kapsar.","neighbor_ref":"root_001479/B001","relation_type":"near_synonym","shared_zone":"İki dal boğazın altındaki üst göğüs bölgesinde örtüşür."},{"boundary_match":"partial","distinction":"Komşu genel göğüs adıdır; odak göğsün belirli merkezini ve ona bağlı kullanımları öne çıkarır.","focus_only":"Odak boğaz altındaki çukuru ve devenin çökme kalıbını ayrıca belirtir.","gloss":"göğüs","neighbor_only":"Komşu göğsü ayrıntılandırmadan genel bir beden bölgesi olarak adlandırır.","neighbor_ref":"root_001315/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da göğüs bölgesini adlandırabilir."}],"source_phrase_ar":"بلدة النحر وسطه (jamhara)؛ البلدة الصدر وفلان واسع البلدة أي واسع الصدر (sihah)؛ البلدة بلدة النحر وهي الثغرة وما حولها (tahdhib)؛ سميت الكركرة بلدة لذلك وربما استعير ذلك لصدر الإنسان (mufradat)؛ الأصل الصدر ويقال وضعت الناقة بلدتها بالأرض إذا بركت (maqayis)","source_summary":"Kaynaklar göğüs ile boğaz altındaki orta çukur çevresini aynı beden bölgesi altında toplar. İnsan göğsüne aktarım ve devenin çökerken göğsünü yere koyması, bu çekirdeğe bağlı fakat ayrı kapsamlı kullanımlardır.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الصدر، وبلدة النحر والثغرة وما حولها، والكركرة، ووضع الناقة صدرها على الأرض في البروك.","what_is_not_ar":"ليس فيه الموضع الأرضي العام ولا البلجة بين الحاجبين إلا إذا نص المصدر على التشبيه."},"support_links":[]},{"boundary":"Dal, alın bütünü veya kaşın kendisi değil, iki kaş arasındaki açık bölge ve bu açıklığa sahip kişiyle sınırlıdır.","branch_kind":"bare","branch_ref":"root_000148/B003","candidate_links":[{"candidate_id":"cand_266c5efc419fba24d8a9","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:1:4:2","qac_word_ref":"90:1:4","surface_ar":"بَلَدِ"}],"gloss":"kaşların arasındaki açıklık ve kaşları birleşmemiş olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki kaş arasındaki temiz ve açık bölge çekirdeği oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaşları birbirine birleşmemiş kişi bu görünüş üzerinden nitelenir."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem yüz bölgesini hem de bu bölgenin görünüşüyle nitelenen kişiyi kapsar.","boundary_detail":"Dal, alın bütünü veya kaşın kendisi değil, iki kaş arasındaki açık bölge ve bu açıklığa sahip kişiyle sınırlıdır.","branch_image_ar":"البلجة بين الحاجبين","concept_gloss":"kaşların arasındaki açıklık ve kaşları birleşmemiş olma","contextual_glosses":[{"applicability":"Doğrudan yüz bölgesinin kendisi anlatıldığında kullanılan kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaşları birleşmemiş kişiye yönelik nitelemeyi dışarıda bırakır.","preserves":"İki kaş arasındaki açık bölgeyi korur."},"facet_ids":["F001"],"text":"kaş arası açıklık","usage_role":"general"}],"definition":"İki kaşın arasında kalan temiz, açık ve kılsız görünümlü bölgedir; bu açıklığa sahip, yani kaşları birleşmemiş kişi de aynı anlam alanında nitelenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki kaş arasındaki temiz ve açık bölge çekirdeği oluşturur."},{"facet_id":"F002","role":"extension","statement":"Kaşları birbirine birleşmemiş kişi bu görünüş üzerinden nitelenir."}],"identity_rationale":"Kaynak ifade, kaşların arasındaki temiz ve açık bölgeyi ve kaşları birleşmemiş kişiyi tutarlı biçimde aynı görünüş altında tanımlar. Beden iriliği ve zihinsel yavaşlık yalnızca benzer biçimli başka anlamlardır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kaşların arasındaki açık ve temiz bölge"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kaşları birleşmemiş"}],"lexicalization_note":"Tanım, çıplak biçimin kaşlar arasındaki açıklık anlamıyla sınırlıdır; aynı biçimin beden iriliği ya da zihinsel yavaşlık anlamları içeri alınmaz.","neighbor_coverage_note":"Bütün yüz ve görünüş adayları değerlendirildi; alın ve kaş, odak bölgesinin iki doğrudan anatomik sınırını gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak iki kaş arasındaki boşluğa, komşu ise kaşların üstündeki daha geniş alın bölgesine yönelir.","focus_only":"Odak kaşların arasındaki açıklığı ve kaşların birleşmemiş olmasını belirtir.","gloss":"alın","neighbor_only":"Komşu alın bölgesini ve alın kemiğini daha geniş olarak kapsar.","neighbor_ref":"root_000219/B001","relation_type":"near_neighbor","shared_zone":"İki dal yüzün kaşların çevresindeki ön bölümüne ilişkindir."},{"boundary_match":"field_only","distinction":"Biri kaşların arasındaki boşluğu, öteki kaş yapısının kendisini gösterir.","focus_only":"Odak, iki kaşın arasında kalan açıklığı adlandırır.","gloss":"kaş","neighbor_only":"Komşu, gözün üstündeki kıl, et ve kemikten oluşan kaşın kendisini adlandırır.","neighbor_ref":"root_000294/B005","relation_type":"near_neighbor","shared_zone":"İki dal aynı yüz bölgesinde yan yana bulunan yapılara ilişkindir."}],"source_phrase_ar":"ربما سميت البلجة بلدة (jamhara)؛ البلدة والبلدة نقاوة ما بين الحاجبين ورجل أبلد أي أبلج بين البلد (sihah)؛ الأبلد من الرجال الذي ليس بمقرون وهي البلدة والبلدة (tahdhib)؛ البلدة البلجة ما بين الحاجبين تشبيها بالبلد لتمددها (mufradat)؛ الأبلد الذي ليس بمقرون الحاجبين يقال لما بين حاجبيه بلدة (maqayis)","source_summary":"Kaynaklar iki kaş arasındaki açıklıkta ve bu açıklığın kaşları birleşmemiş kişiyi nitelemesinde birleşir. Benzetme açıklığın yayılmış görünüşüne dayanır.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه البلجة أو النقاوة بين الحاجبين، والرجل الأبلد الذي ليس بمقرون الحاجبين.","what_is_not_ar":"ليس فيه عظم الخلق ولا بلادة الذهن، وإن اشترك معها لفظ أبلد."},"support_links":["sup_59c023bb0995d074fe6f"]},{"boundary":"Dal yeryüzündeki yer anlamından ayrıdır; Ay durağına verilen adın farklı göksel tasvirlerini birlikte, fakat kaynak değişkeleri olarak kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000148/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:1:4:2","qac_word_ref":"90:1:4","surface_ar":"بَلَدِ"}],"gloss":"yıldız kümesi ya da yıldızsız alan diye tasvir edilen Ay durağı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, Ay'ın konaklarından biri sayılan belirli bir gök bölgesidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir tasvir bu durağı bir göksel yay içinde yer alan altı yıldız olarak açıklar."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir tasvir onu iki belirli göksel işaret arasındaki yıldızsız alan olarak açıklar."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Göksel aslanın göğsü de bu adla anılan özel bir gök konumudur."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ortak göksel durak çekirdeğini ve birbirinden farklı iki fiziksel tasviri birlikte gösterir.","boundary_detail":"Dal yeryüzündeki yer anlamından ayrıdır; Ay durağına verilen adın farklı göksel tasvirlerini birlikte, fakat kaynak değişkeleri olarak kapsar.","branch_image_ar":"منزلة القمر والموضع السماوي الخالي","concept_gloss":"yıldız kümesi ya da yıldızsız alan diye tasvir edilen Ay durağı","contextual_glosses":[{"applicability":"Durağın yıldız düzeni hakkında hüküm vermeden yalnız ortak göksel işlevi anlatır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Altı yıldız, yıldızsız alan ve göksel aslanın göğsü tasvirlerini belirtmez.","preserves":"Ay durağı olan ortak çekirdeği korur."},"facet_ids":["F001"],"text":"Ay'ın belirli bir durağı","usage_role":"general"}],"definition":"Ay'ın konaklarından biri olarak adlandırılan bir gök bölgesidir; kaynaklarda altı yıldızlık bir küme veya iki belirli göksel işaret arasındaki yıldızsız alan olarak farklı biçimlerde tasvir edilir. Göksel aslanın göğsü için kullanılan ad da bu dala bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, Ay'ın konaklarından biri sayılan belirli bir gök bölgesidir."},{"facet_id":"F002","role":"source_variant","statement":"Bir tasvir bu durağı bir göksel yay içinde yer alan altı yıldız olarak açıklar."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir tasvir onu iki belirli göksel işaret arasındaki yıldızsız alan olarak açıklar."},{"facet_id":"F004","role":"extension","statement":"Göksel aslanın göğsü de bu adla anılan özel bir gök konumudur."}],"identity_rationale":"Kaynak ifade dalı bir Ay durağı olarak destekler, fakat fiziksel tasvirler tam olarak birleşmez: bir anlatım onu altı yıldızlık bir küme, bir başkası iki göksel işaret arasındaki yıldızsız alan, bir diğeri göksel aslanın göğsü olarak verir. Dal korunabilir, ancak bu tasvirler tek bir değişmez gök biçimiymiş gibi birleştirilemez.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"Ay durağı veya yıldızsız gök bölgesi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"göksel aslanın göğüs bölgesi"}],"lexicalization_note":"Temel biçim Ay durağını veya yıldızsız gök alanını gösterir; göksel aslanın göğsü olan özel adlandırma yalnız kendi sözlüksel biriminde tutulur.","neighbor_coverage_note":"Bütün göksel adaylar karşılaştırıldı; başka bir Ay durağı ile daha geniş göksel bölümleme, durağın kimliği ve sınıf sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Aynı tür göksel birimler olsalar da gökte farklı konumları ve farklı özel adları gösterirler.","focus_only":"Odak farklı kaynaklarda yıldız kümesi veya yıldızsız alan olarak tasvir edilen ayrı bir Ay durağıdır.","gloss":"başka bir Ay durağı","neighbor_only":"Komşu, başka iki göksel işaretin yanında konumlandırılan farklı bir Ay durağının özel adıdır.","neighbor_ref":"root_000925/B004","relation_type":"same_field","shared_zone":"Her ikisi de Ay'ın konaklarından birini adlandırır."},{"boundary_match":"field_only","distinction":"Odak Ay'ın hareket dizisindeki tek bir duraktır; komşu daha geniş bir göksel bölümleme sistemini anlatır.","focus_only":"Odak belirli bir Ay durağını ve onun değişken fiziksel tasvirlerini gösterir.","gloss":"göksel bölümler","neighbor_only":"Komşu göğün on iki geniş bölümünü, yıldız kümelerini veya göksel yapıları kapsar.","neighbor_ref":"root_000101/B002","relation_type":"same_field","shared_zone":"İki dal da göğün adlandırılmış bölümleriyle ilgilidir."}],"source_phrase_ar":"البلدة منزل من منازل القمر (jamhara)؛ البلدة من منازل القمر وهي ستة أنجم من القوس (sihah)؛ البلدة في السماء موضع لا نجوم فيه بين النعائم وسعد الذابح (tahdhib)؛ البلدة منزل من منازل القمر (mufradat)؛ البلدة النجم يقولون هو بلدة الأسد أي صدره (maqayis)","source_summary":"Ortak çekirdek bir Ay durağına verilen addır. Toplu kanıt, durağın altı yıldızlık bir küme ile yıldızsız bir gök alanı arasında değişen tasvirlerini ve göksel aslanın göğsü adlandırmasını birlikte aktarır; bu tasvirler tek bir fiziksel tanıma indirgenemez.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه البلدة منزلة من منازل القمر، والموضع الخالي في السماء بين النعائم وسعد الذابح، وبلدة الأسد إذا أريد صدره السماوي.","what_is_not_ar":"ليس فيه الأرض والبلد المسكون إلا من جهة الاسم المشترك أو التشبيه."},"support_links":[]},{"boundary":"Dal kalıcı zeka düşüklüğünü değil, şaşkınlıktan doğan duraksamayı; ayrı kullanımda ise metaneti yitirip boyun eğmeyi anlatır.","branch_kind":"bare","branch_ref":"root_000148/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:1:4:2","qac_word_ref":"90:1:4","surface_ar":"بَلَدِ"}],"gloss":"şaşkınlıkla duraksama; metaneti yitirip boyun eğme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi şaşkınlık yüzünden kararsız kalır, duraksar ve ilerleyemez."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Şaşkın kişi elini göğsünün üstüne koyabilir; bu hareket durumun kendisi değil, ona eşlik eden belirtidir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Metaneti korumanın karşıtı olarak sinme, teslim olma ve boyun eğme de aynı biçimle anlatılır."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem kararsız şaşkınlık çekirdeğini hem de ayrı teslimiyet değişkesini kapsar.","boundary_detail":"Dal kalıcı zeka düşüklüğünü değil, şaşkınlıktan doğan duraksamayı; ayrı kullanımda ise metaneti yitirip boyun eğmeyi anlatır.","branch_image_ar":"الحيرة والتبلد","concept_gloss":"şaşkınlıkla duraksama; metaneti yitirip boyun eğme","contextual_glosses":[{"applicability":"Bir iş karşısında kararsızca duraksama ve yönünü bulamama öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eli göğse koyma belirtisini ve metaneti yitirip boyun eğme değişkesini dışarıda bırakır.","preserves":"Şaşkınlık ve kararsız duraksama çekirdeğini korur."},"facet_ids":["F001"],"text":"şaşkınlıktan ne yapacağını bilememek","usage_role":"general"},{"applicability":"Metaneti korumanın karşıtı olan teslimiyet ve sinme anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Şaşkınlıkla kararsız duraksamayı ve ona eşlik eden göğüs hareketini vermez.","preserves":"Sinme ve boyun eğme değişkesini korur."},"facet_ids":["F003"],"text":"sinip boyun eğmek","usage_role":"contextual"}],"definition":"Bir iş karşısında şaşkınlığa düşüp kararsızca duraksamak ve ne yapacağını bilememektir; bu durumda eli göğse koyma hareketi eşlik edebilir. Ayrı bir kullanımda metaneti yitirerek sinmek ve boyun eğmek anlamına gelir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi şaşkınlık yüzünden kararsız kalır, duraksar ve ilerleyemez."},{"facet_id":"F002","role":"associated_use","statement":"Şaşkın kişi elini göğsünün üstüne koyabilir; bu hareket durumun kendisi değil, ona eşlik eden belirtidir."},{"facet_id":"F003","role":"source_variant","statement":"Metaneti korumanın karşıtı olarak sinme, teslim olma ve boyun eğme de aynı biçimle anlatılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kaynak çekirdeğinde bulunmayan kalıcı zihinsel yetersizlik yargısını ekler.","collision":"Zihinsel yavaşlık dalıyla karışır.","fit":"displacement","loses":"Geçici şaşkınlığı, kararsız duraksamayı, göğüs hareketini ve boyun eğme değişkesini kaybeder.","preserves":"İlerleyememe görünüşünü çok genel biçimde çağrıştırır."},"text":"aptallık"}],"identity_rationale":"Kaynak ifade şaşkınlık içinde duraksama ve ne yapacağını bilememe çekirdeğini, buna eşlik eden eli göğse koyma hareketini ve metanetin karşıtı olan boyun eğmeyi destekler. Provisional çerçevedeki yoğun üzüntü koşulu kaynak ifadesinde kurulmadığı için tanımdan çıkarılmalı, boyun eğme ise ayrı bir anlam değişkesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"şaşkınlığa düşüp kararsızca duraksamak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bir işte şaşırıp ne yapacağını bilememek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"metaneti yitirip sinme ve boyun eğme"}],"lexicalization_note":"Tanım çıplak biçimlerin şaşkınlık, duraksama ve boyun eğme kullanımlarını kapsar; zihinsel yetersizlik anlamı bu dala aktarılmaz.","neighbor_coverage_note":"Bütün şaşkınlık, üzüntü ve belirsizlik adayları değerlendirildi; yön bulamayan bocalama ile ani afallama en yakın iki karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak şaşkın duraksama ve teslimiyet görünüşüne, komşu ise yön ve doğru yol bulamama koşuluna ağırlık verir.","focus_only":"Odak eli göğse koyma belirtisini ve metaneti yitirip boyun eğme değişkesini içerir.","gloss":"yönünü bulamadan bocalama","neighbor_only":"Komşu şaşkınlığın yanı sıra yol, görüş veya yön bulamama ve sapkınlıkta bocalama kapsamına uzanır.","neighbor_ref":"root_001048/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir işte ne yapacağını bilemeyip kararsızca bocalamayı kapsar."},{"boundary_match":"partial","distinction":"Komşuda ani şaşkınlık ve korku daha geniştir; odakta kararsızca duraksama belirleyicidir.","focus_only":"Odak kararsız duraksamayı, göğüs hareketini ve boyun eğme değişkesini belirtir.","gloss":"afallama ve şaşkınlık","neighbor_only":"Komşu korku, ani afallama ve şaşkın kişinin başka olumsuz nitelendirmelerini de kapsar.","neighbor_ref":"root_000086/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin şaşkın ve afallamış duruma düşmesini anlatabilir."}],"source_phrase_ar":"تبلد الرجل من هذا إذا لحقته حيرة فضرب بيده على بلدة نحره (jamhara)؛ تبلد أي تردد متحيرا (sihah)؛ المتبلد الذي يتردد متحيرا (tahdhib)؛ التبلد نقيض التجلد وهو استكانة وخضوع (tahdhib)؛ قيل للمتحير بلد في أمره وأبلد وتبلد (mufradat)؛ تبلد الرجل إذا وضع يده على صدره عند تحيره في الأمر (maqayis)","source_summary":"Toplu kanıt şaşkınlıkla kararsızca duraksamayı ortak merkez yapar ve eli göğse koymayı buna eşlik eden hareket olarak verir. Metanetin karşıtı olan sinme ve boyun eğme, yoğun üzüntü koşulu gerektirmeyen ayrı bir kullanım değişkesidir.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه تبلد وبلد وأبلد إذا تردد متحيرا، ووضع يده على صدره عند الحيرة، والاستكانة والخضوع عند غلبة الحزن.","what_is_not_ar":"ليس هو البلادة بمعنى ضد الذكاء إلا حيث يصرح المصدر بانتقال المعنى إليها."},"support_links":[]},{"boundary":"Dal izin kendisini kapsar; yara, deri hastalığı, ben veya tanıtma amacıyla yapılan işaret gibi belirli nedenler zorunlu değildir.","branch_kind":"bare","branch_ref":"root_000148/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:1:4:2","qac_word_ref":"90:1:4","surface_ar":"بَلَدِ"}],"gloss":"bedende, deride veya başka bir yüzeyde kalan iz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir beden veya yüzey üzerinde seçilebilen kalıcı ya da belirgin iz çekirdeği oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlam yalnız deriye değil, bedenin başka bölümlerine ve başka yüzeylere de uzanabilir."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nedeni belirtilmemiş genel iz anlamını ve beden dışına uzanan kapsamı birlikte verir.","boundary_detail":"Dal izin kendisini kapsar; yara, deri hastalığı, ben veya tanıtma amacıyla yapılan işaret gibi belirli nedenler zorunlu değildir.","branch_image_ar":"الأثر في الجلد والبدن","concept_gloss":"bedende, deride veya başka bir yüzeyde kalan iz","contextual_glosses":[{"applicability":"İzin özellikle insan ya da hayvan derisinde bulunduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bedenin başka bölümlerindeki ve beden dışındaki yüzeylerdeki izleri dışarıda bırakır.","preserves":"Deride görülen iz çekirdeğini korur."},"facet_ids":["F001"],"text":"deride kalan iz","usage_role":"contextual"}],"definition":"Bedende, deride veya başka bir yüzeyde kalmış görünür izdir; tekil ya da çoğul olarak, izin nedenini zorunlu biçimde belirtmeden kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir beden veya yüzey üzerinde seçilebilen kalıcı ya da belirgin iz çekirdeği oluşturur."},{"facet_id":"F002","role":"extension","statement":"Anlam yalnız deriye değil, bedenin başka bölümlerine ve başka yüzeylere de uzanabilir."}],"identity_rationale":"Kaynak ifade, bedende, deride veya başka bir yüzeyde bulunan izi doğrudan ve tutarlı biçimde verir; çoğul biçimi de aynı izi topluca gösterir. İzin yaradan, hastalıktan veya bilinçli işaretlemeden doğması çekirdek tanımın zorunlu koşulu değildir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bedende veya başka bir yüzeyde kalan iz; izler"}],"lexicalization_note":"Çıplak dal genel iz anlamıyla sınırlıdır; izin belirli bir yara, hastalık ya da işaretleme türünden doğduğu varsayılmaz.","neighbor_coverage_note":"Bütün iz, yara, ben ve işaretleme adayları değerlendirildi; genel kalıntı ile amaçlı tanıtma işareti, neden ve işlev sınırını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak izin oluşumunu belirtmez; komşu önceki bir olaydan ya da yaradan geriye kalma ilişkisini daha açık taşır.","focus_only":"Odak bedende veya başka bir yüzeyde nedeni belirtilmemiş genel izi kapsar.","gloss":"geride kalan belirti","neighbor_only":"Komşu bir şeyden geriye kalan belirtiyi ve özellikle iyileşmiş yaranın deride bıraktığı kalıntıyı öne çıkarır.","neighbor_ref":"root_000287/B001","relation_type":"near_synonym","shared_zone":"İki dal da deride veya başka bir nesnede kalan görünür izi anlatabilir."},{"boundary_match":"partial","distinction":"Odakta amaç ve yapılış biçimi belirsizdir; komşuda bilinçli işaretleme ve tanıtma işlevi kurucudur.","focus_only":"Odak kendiliğinden ya da herhangi bir nedenle oluşmuş genel izi kapsar.","gloss":"tanıtıcı işaret","neighbor_only":"Komşu tanıtma veya ayırt etme amacıyla bilerek yapılan damga, yakı ya da kesik işaretini gerektirir.","neighbor_ref":"root_001650/B001","relation_type":"near_neighbor","shared_zone":"Bilerek yapılan bir işaret de yüzeyde iz bırakabilir."}],"source_phrase_ar":"البلد الأثر في البدن وغيره والجمع أبلاد (jamhara)؛ البلد الأثر والجمع أبلاد (sihah)؛ البلد الأثر بالجسد وجمعه أبلاد (tahdhib)؛ ولاعتبار الأثر قيل بجلده بلد أي أثر وجمعه أبلاد (mufradat)؛ البلد الأثر وجمعه أبلاد (maqayis)","source_summary":"Kaynaklar bedende veya başka bir yerde kalan iz anlamında birleşir ve çoğul biçimin birden çok izi gösterdiğini bildirir. İzin nedeni belirtilmediğinden anlam yara ya da işaretleme gibi tek bir oluşum yoluyla sınırlandırılamaz.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه البلد بمعنى الأثر في البدن أو الجلد أو غيره، وجمعه أبلاد.","what_is_not_ar":"ليس فيه البلد بمعنى الأرض ولا البلادة بمعنى قلة الذكاء."},"support_links":[]},{"boundary":"Dal geçici şaşkınlıktan ve sırf iri bedenden ayrılır; kalıcı yavaş kavrayış, ilerleyememe veya işte güçsüz kalma odağındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000148/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:1:4:2","qac_word_ref":"90:1:4","surface_ar":"بَلَدِ"}],"gloss":"kavrayışta, ilerlemede veya işte ağır ve yetersiz kalma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Zeka, kavrayış, nüfuz ve işleri hızla yürütme gücünün düşük olması çekirdektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir atın öndeki atlara yetişemeyip geride kalması aynı yavaşlık niteliğiyle anlatılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli eylem kalıbında kişi çalışmada ve cömertçe vermede geriler ve güçsüzleşir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kaba ve iri bedenli kişilerde sık görülmesi anlamın nedeni olarak anılır, fakat zorunlu bir özellik değildir."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan, hayvan ve belirli iş bağlamlarındaki ortak yavaşlık ve yetersizlik çekirdeğini kapsar.","boundary_detail":"Dal geçici şaşkınlıktan ve sırf iri bedenden ayrılır; kalıcı yavaş kavrayış, ilerleyememe veya işte güçsüz kalma odağındadır.","branch_image_ar":"البلادة وضعف النفاذ","concept_gloss":"kavrayışta, ilerlemede veya işte ağır ve yetersiz kalma","contextual_glosses":[{"applicability":"Bir insanın zeka, kavrayış ve işlerde ilerleme çevikliği düşük olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Atın yarışta geri kalmasını ve iş ile vermedeki özel güçsüzleşmeyi dışarıda bırakır.","preserves":"Zihinsel ve pratik kavrayış yavaşlığını korur."},"facet_ids":["F001"],"text":"ağır kavrayışlı","usage_role":"general"},{"applicability":"Bir atın öndeki atlara yetişememesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsandaki kavrayış yavaşlığını ve işteki güçsüzleşmeyi vermez.","preserves":"İlerleme ve yarış bakımından geri kalmayı korur."},"facet_ids":["F002"],"text":"yarışta geri kalan","usage_role":"contextual"}],"definition":"Kavrayışta, karar vermede veya ilerlemede ağır ve yetersiz kalma niteliğidir; insanın zihinsel ve pratik çevikliğini, hayvanın yarışta geri kalmasını kapsayabilir. Belirli bir kullanımda işte ve vermede güçsüzleşmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Zeka, kavrayış, nüfuz ve işleri hızla yürütme gücünün düşük olması çekirdektir."},{"facet_id":"F002","role":"extension","statement":"Bir atın öndeki atlara yetişemeyip geride kalması aynı yavaşlık niteliğiyle anlatılır."},{"facet_id":"F003","role":"specialization","statement":"Belirli eylem kalıbında kişi çalışmada ve cömertçe vermede geriler ve güçsüzleşir."},{"facet_id":"F004","role":"associated_use","statement":"Kaba ve iri bedenli kişilerde sık görülmesi anlamın nedeni olarak anılır, fakat zorunlu bir özellik değildir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kaynakta bu dal için zorunlu olmayan geçici afallama durumunu ekler.","collision":"Şaşkınlıkla duraksama dalıyla karışır.","fit":"displacement","loses":"Kalıcı kavrayış yavaşlığını, yarışta geri kalmayı ve işte güçsüzleşmeyi kaybeder.","preserves":"Kişinin bir işte ilerleyememesi görünüşünü kısmen çağrıştırır."},"text":"şaşkın"}],"identity_rationale":"Kaynak ifade insan için zeka, kavrayış ve işlerde atılganlık eksikliğini; hayvan için yarışta geri kalmayı; belirli bir iş kalıbında çalışma ve cömertlikte güçsüzleşmeyi bildirir. İri ve kaba bedenle kurulan ilişki açıklayıcı bir çağrışımdır, anlamın zorunlu koşulu değildir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"zeka, kavrayış ve atılganlık düşüklüğü"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ağır kavrayışlı; yarışta geri kalan"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"işte ve cömertlikte gerileyip güçsüzleşti"}],"lexicalization_note":"Temel biçimler zeka ve ilerleme yavaşlığını gösterir; işte ve vermede güçsüzleşme yalnız belirtilen eylem kalıbına bağlıdır ve bütün dala yayılmaz.","neighbor_coverage_note":"Bütün yavaşlık, zayıflık ve işte geri kalma adayları değerlendirildi; genel yetersizlik ile salt yavaşlık odak dalının iki temel sınırını gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak ağır kavrayış ve yavaş ilerleme merkezlidir; komşu genel güçsüzlük ve değer ölçüsünde eksik kalmaya uzanır.","focus_only":"Odak zeka ve kavrayış düşüklüğünü, ayrıca işte güçsüzleşmeyi açıkça kapsar.","gloss":"zayıf ve hedefe erişemeyen","neighbor_only":"Komşu düşük değer, yiğitlik ve soyluluk ölçüsüne erişememe ile başını kaldıramayan atı da kapsar.","neighbor_ref":"root_001551/B005","relation_type":"near_synonym","shared_zone":"İki dal insanın yetersizliğini ve atın öndekilere yetişememesini anlatabilir."},{"boundary_match":"partial","distinction":"Komşu yalnız hız eksikliğidir; odakta kavrayış ve yeterlilik düşüklüğü de kurucudur.","focus_only":"Odak zeka ve kavrayış düşüklüğü ile işte yetersizliği içerir.","gloss":"yavaşlık ve gecikme","neighbor_only":"Komşu hareket, geliş ve yolculuk dahil her türlü salt yavaşlığı anlatır.","neighbor_ref":"root_000124/B001","relation_type":"near_neighbor","shared_zone":"Yavaş ilerleme ve geride kalma iki dalda da görülebilir."}],"source_phrase_ar":"رجل بليد بين البلادة ضد النحرير (jamhara)؛ البلادة ضد الذكاء وقد بلد بالضم فهو بليد (sihah)؛ أبلد الرجل إذا كانت دابته بليدة (sihah)؛ البلادة نقيض النفاذ والمضاء في الأمور (tahdhib)؛ فرس بليد إذا تأخر عن الخيل السوابق (tahdhib)؛ بلد إذا نكس في العمل وضعف حتى في الجود (tahdhib)؛ لكثرة وجود البلادة فيمن كان جلف البدن (mufradat)","source_summary":"Toplu kanıt zeka, kavrayış, nüfuz ve ilerleme gücündeki düşüklüğü ortaklaştırır; atın yarışta geri kalması ve kişinin işte ya da cömertlikte güçsüzleşmesi bu çekirdeğin özel gerçekleşmeleridir. Kaba bedenle bağlantı zorunlu tanım değil, açıklayıcı bir ilişkilendirmedir.","sources":["JA","SI","TA","MU"],"what_is_ar":"يدخل فيه البلادة ضد الذكاء والنفاذ والمضاء، والبليد من الناس أو الدواب، وتأخر الفرس عن الخيل السوابق، وضعف المرء في العمل والجود.","what_is_not_ar":"ليس فيه الحيرة العابرة ولا عظم الخلق إلا إذا نص المصدر على علاقة بينهما."},"support_links":[]},{"boundary":"Dal yalnız fiziksel irilik, enlilik, kabalık ve sağlamlıkla ilgilidir; kaş görünüşü veya zihinsel yavaşlık anlamlarını içermez.","branch_kind":"bare","branch_ref":"root_000148/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:1:4:2","qac_word_ref":"90:1:4","surface_ar":"بَلَدِ"}],"gloss":"iri, enli ve kaba yapılı; hayvanda sert ve dayanıklı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İri ve kaba beden yapısı çekirdek fiziksel niteliktir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İlgili bir biçim özellikle enli ve geniş bedeni anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Deve için kullanılan biçim iri bedenle birlikte sertlik ve dayanıklılığı belirtir."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve hayvan bedenine ilişkin irilik, enlilik, kabalık ve dayanıklılık niteliklerini kapsar.","boundary_detail":"Dal yalnız fiziksel irilik, enlilik, kabalık ve sağlamlıkla ilgilidir; kaş görünüşü veya zihinsel yavaşlık anlamlarını içermez.","branch_image_ar":"غلظ الخلق وعظم الجسم","concept_gloss":"iri, enli ve kaba yapılı; hayvanda sert ve dayanıklı","contextual_glosses":[{"applicability":"İnsan bedeninin büyüklüğü ve kaba yapısı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Enlilik özel biçimini ve devedeki sert, dayanıklı yapı vurgusunu dışarıda bırakır.","preserves":"İri ve kaba beden çekirdeğini korur."},"facet_ids":["F001"],"text":"iri ve kaba yapılı","usage_role":"general"}],"definition":"Bir insanın veya hayvanın iri, enli ve kaba yapılı olmasıdır; deve söz konusu olduğunda bedenin sert ve dayanıklı oluşu da kapsama girer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İri ve kaba beden yapısı çekirdek fiziksel niteliktir."},{"facet_id":"F002","role":"specialization","statement":"İlgili bir biçim özellikle enli ve geniş bedeni anlatır."},{"facet_id":"F003","role":"specialization","statement":"Deve için kullanılan biçim iri bedenle birlikte sertlik ve dayanıklılığı belirtir."}],"identity_rationale":"Kaynak ifade insan için iri ve kaba yapıyı, ilgili başka biçimler için enli olmayı ve devenin sağlam, sert bedenini açıkça destekler. Zihinsel yavaşlıkla kurulan açıklayıcı ilişki bu fiziksel yapının tanımına katılmaz.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"iri ve kaba yapılı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"enli; deve için sert ve dayanıklı"}],"lexicalization_note":"Çıplak biçimlerin fiziksel beden yapısı anlamı tanımlanır; zihinsel nitelik ve kaşların görünüşüyle ilgili eş biçimli anlamlar dışarıda tutulur.","neighbor_coverage_note":"Bütün irilik ve beden bölgesi adayları değerlendirildi; genel kalın yapı ile iri-ağır yapı, odaktaki enlilik ve dayanıklılık sınırını en iyi açıkladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bütün bedenin iriliği ve enliliğine yönelir; komşu tek tek dokuların ve beden bölümlerinin kalınlığına da uzanır.","focus_only":"Odak enli insanı ve sert, dayanıklı deveyi belirli biçimlerle kapsar.","gloss":"kalın ve kaba beden yapısı","neighbor_only":"Komşu kalınlığı deri, kemik, baş derisi ve hörgüç gibi tek tek beden bölümlerine de uygular.","neighbor_ref":"root_000217/B003","relation_type":"near_synonym","shared_zone":"İki dal iri, kalın ve kaba fiziksel yapıyı anlatır."},{"boundary_match":"partial","distinction":"Komşuda ağırlık, belirli dişi varlıklar ve hoyratlık öne çıkar; odakta bu koşullar zorunlu değildir.","focus_only":"Odak insan ve hayvanda kaba yapı ile dayanıklılığı kapsar.","gloss":"iri ve ağır yapılı","neighbor_only":"Komşu özellikle dişi deve veya kadında irilikle birlikte ağırlık ve hoyratlığı belirtir.","neighbor_ref":"root_001250/B020","relation_type":"near_synonym","shared_zone":"İki dal iri ve geniş bedenli olmayı anlatabilir."}],"source_phrase_ar":"رجل أبلد غليظ الخلق (jamhara)؛ الأبلد الرجل العظيم الخلق والبلندى العريض والمبلندى من الجمال الصلب الشديد (sihah)؛ رجل أبلد عبارة عن عظيم الخلق (mufradat)","source_summary":"Kaynaklar iri ve kaba beden yapısında birleşir; enli insan ile sert ve dayanıklı deve nitelemeleri bu fiziksel çekirdeğin özel biçimleridir. Zihinsel yavaşlık bu dalın tanımsal parçası değildir.","sources":["JA","SI","MU"],"what_is_ar":"يدخل فيه الأبلد العظيم أو الغليظ الخلق، والبلندى العريض، والمبلندى من الجمال الصلب الشديد.","what_is_not_ar":"ليس فيه الأبلد الذي ليس بمقرون الحاجبين، ولا البليد ضد الذكي إلا على جهة التعليل الذي ذكره بعض المصادر."},"support_links":[]},{"boundary":"Dal bir yerde kalıp ikamet etmeyi kapsar; yere temas edip yapışmayı, yalnızca bir yere varmayı veya oraya dönmeyi içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_000148/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:1:4:2","qac_word_ref":"90:1:4","surface_ar":"بَلَدِ"}],"gloss":"bir yerde kalıp ikamet etme ve orada oturan kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yerde bulunmayı sürdürmek ve orayı terk etmeden kalmak çekirdektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu eylemi sürdüren kişi, bulunduğu yerde oturan kimse olarak adlandırılır."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer belirten eylem kalıbını ve bu eylemden türeyen sakin adını birlikte kapsar.","boundary_detail":"Dal bir yerde kalıp ikamet etmeyi kapsar; yere temas edip yapışmayı, yalnızca bir yere varmayı veya oraya dönmeyi içermez.","branch_image_ar":"الإقامة ولزوم البلد","concept_gloss":"bir yerde kalıp ikamet etme ve orada oturan kişi","contextual_glosses":[{"applicability":"Kişinin bir yeri terk etmeyip orada ikamet etmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"O yerde oturan kişiyi adlandıran türemiş anlamı dışarıda bırakır.","preserves":"Kalma ve ikamet etme eylemini korur."},"facet_ids":["F001"],"text":"bir yerde kalıp oturmak","usage_role":"general"}],"definition":"Bir yerde kalmak, orayı terk etmeyip orada ikamet etmektir; aynı anlam alanındaki kişi adı, o yerde oturan ve kalan kimseyi gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yerde bulunmayı sürdürmek ve orayı terk etmeden kalmak çekirdektir."},{"facet_id":"F002","role":"extension","statement":"Bu eylemi sürdüren kişi, bulunduğu yerde oturan kimse olarak adlandırılır."}],"identity_rationale":"Kaynak ifade bir yerde kalmayı, orayı terk etmeyip yerleşmeyi ve bu durumda olan kişiyi tutarlı biçimde verir. Yere fiziksel olarak yapışma ve memlekete dönme isteği bu eylemin parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir yerde kalıp ikamet etmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bir yerde oturan, sakin"}],"lexicalization_note":"Kalma eylemi yer belirten tamamlayıcıyla kurulur; kişi adı ise orada oturanı gösterir. Bu yapılar fiziksel yapışma anlamına genellenmez.","neighbor_coverage_note":"Bütün ikamet, varış, yurt ve dönüş adayları değerlendirildi; yerleşip oturma ile birkaç günlük kalış, süre ve süreklilik sınırlarını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak genel olarak yerde kalma ve sakin adıdır; komşuda yerleşme ve konutu sürekli tutma görünüşü daha belirgindir.","focus_only":"Odak yerle ilişkili kişi adını ayrıca verir ve kalmayı yer adından hareketle anlatır.","gloss":"yerleşip oturma","neighbor_only":"Komşu yerleşme, sakin durma ve bir konutu sürekli tutma görünüşünü daha açık taşır.","neighbor_ref":"root_001243/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir yerde kalmayı ve orada oturmayı anlatır."},{"boundary_match":"partial","distinction":"Komşunun birkaç günlük süre sınırı vardır; odakta süre belirtilmez ve daha sürekli ikamet mümkün olabilir.","focus_only":"Odak süresi belirtilmeyen ikameti ve orada oturan kişiyi kapsar.","gloss":"birkaç gün bir yerde kalma","neighbor_only":"Komşu bir yerde birkaç gün kalmayı özellikle sınırlar.","neighbor_ref":"root_000377/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin bir yerde bir süre kalmasını anlatır."}],"source_phrase_ar":"بلد بالمكان أقام به فهو بالد (sihah)؛ بلدت بالمكان أبلد بلودا أي أقمت به (tahdhib)؛ بلد لزم البلد (mufradat)؛ البالد قياسا المقيم بالبلد (maqayis)","source_summary":"Kaynaklar bir yerde kalma ve orayı sürekli tutma anlamında birleşir; kişi biçimi de aynı yerle ilişkisini sürdüren sakini gösterir. Kalışın süresi veya yere fiziksel temas zorunlu değildir.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه بلد بالمكان إذا أقام به، وبلد إذا لزم البلد، والبالد المقيم بالبلد.","what_is_not_ar":"ليس فيه اللصوق بالأرض ولا الحيرة التي تحصل لمن خرج عن موطنه إلا حيث يصرح المصدر بالاشتقاق."},"support_links":[]},{"boundary":"Dal yere fiziksel olarak uzanma veya yapışmayı ve yere yapışık eski havuzu kapsar; çökme veya aynı yerde yaşamayı sürdürme anlamını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_000148/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:1:4:2","qac_word_ref":"90:1:4","surface_ar":"بَلَدِ"}],"gloss":"kendini yere atıp yapışma; yere yapışık eski havuz","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedenin yere atılması, uzanması veya yere sıkıca yapışması çekirdek eylemdir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yere yapışık eski havuz aynı fiziksel ilişkiyle adlandırılır."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan bedeninin yere teması ile eski havuzun yere yapışık konumunu birlikte kapsar.","boundary_detail":"Dal yere fiziksel olarak uzanma veya yapışmayı ve yere yapışık eski havuzu kapsar; çökme veya aynı yerde yaşamayı sürdürme anlamını içermez.","branch_image_ar":"اللصوق بالأرض","concept_gloss":"kendini yere atıp yapışma; yere yapışık eski havuz","contextual_glosses":[{"applicability":"Bir kişinin bedeniyle yere uzanması veya yere yapışması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eski su yapısının yere oturmuş veya çökmüş görünümünü dışarıda bırakır.","preserves":"Bedenin yere atılması ve yapışması eylemini korur."},"facet_ids":["F001"],"text":"kendini yere atıp yapışmak","usage_role":"general"}],"definition":"Bir kişinin kendini yere atarak yere uzanması veya yere yapışmasıdır. Aynı ad, yere yapışık eski havuz için de kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedenin yere atılması, uzanması veya yere sıkıca yapışması çekirdek eylemdir."},{"facet_id":"F002","role":"extension","statement":"Yere yapışık eski havuz aynı fiziksel ilişkiyle adlandırılır."}],"identity_rationale":"Kaynak ifade kişinin kendini yere atmasını veya yere yapışmasını ve yere yapışık eski havuz kullanımını destekler. Çökme yorumu kaynak ifadesinin ötesine geçtiğinden dışarıda tutulmalı; bu fiziksel temas da bir yerde ikamet etme anlamından ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kendini yere atmak veya yere yapışmak"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yere yapışık eski havuz"}],"lexicalization_note":"Kişinin yere yapışması yer tamamlayıcılı kalıba bağlıdır; eski su yapısı için kullanılan ad ise ayrı bir nesne kullanımını gösterir ve genel ikamet anlamına açılmaz.","neighbor_coverage_note":"Bütün yapışma, yayılma, çökme ve ikamet adayları değerlendirildi; yere yayılma ile çömelip kalma, hareket ve sonuç farkını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kendini yere atma ve belirli nesne kullanımına bağlıdır; komşu uzanma ile yüzeye yayılmayı daha geniş kapsar.","focus_only":"Odak yere yapışmış eski su yapısı için nesne adını da kapsar.","gloss":"yere uzanıp yayılma","neighbor_only":"Komşu insan ve hayvandan yere yayılan bitkiye kadar daha geniş uzanma ve yayılma örneklerini içerir.","neighbor_ref":"root_000928/B006","relation_type":"near_synonym","shared_zone":"İki dal da bedenin yere uzanmasını ve yere yapışmasını anlatır."},{"boundary_match":"partial","distinction":"Odakta yere atılma ya da yapışma, komşuda ise çömelip aynı noktada kalma belirleyicidir.","focus_only":"Odak kendini yere atma hareketini ve yere oturmuş eski su yapısını kapsar.","gloss":"yere çömelip yerinde kalma","neighbor_only":"Komşu kuş, yırtıcı, insan veya ağır nesnenin bulunduğu yeri terk etmeyip çömelerek kalmasını içerir.","neighbor_ref":"root_000222/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığın yere yakın biçimde yapışık ve hareketsiz görünmesini anlatabilir."}],"source_phrase_ar":"بلد تبليدا ضرب بنفسه الأرض وأبلد لصق بالأرض (sihah)؛ المبلد الحوض القديم ههنا وأراد ملبد فقلب وهو اللاصق بالأرض (tahdhib)؛ بلد الرجل بالأرض إذا لزق بها (maqayis)؛ مبلد بين موماة يذكر حوضا لاصقا بالأرض (maqayis)","source_summary":"Kaynaklar yere atılma ve yere yapışma eyleminde birleşir. Yere yapışık eski havuza verilen ad, bu özel nesne kullanımını aynı fiziksel çekirdeğe bağlar.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه بلد تبليدا إذا ضرب بنفسه الأرض، وأبلد إذا لصق بالأرض، والمبلد من الحوض القديم اللاصق بالأرض أو المتداعي.","what_is_not_ar":"ليس فيه الإقامة بالمكان ولا الصدر إلا في بروك الناقة إذا نص المصدر على وضع الصدر."},"support_links":[]},{"boundary":"Dal genel savaşmayı değil, tarafların kılıç veya sopalarla karşılıklı vuruşmasını kapsar; yerde kalma yalnız türetim açıklamasıdır.","branch_kind":"bare","branch_ref":"root_000148/B011","candidate_links":[{"candidate_id":"cand_1d09325403f9b60cb561","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:1:4:2","qac_word_ref":"90:1:4","surface_ar":"بَلَدِ"}],"gloss":"kılıç veya sopalarla karşılıklı vuruşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tarafların kılıç veya sopalarla birbirine karşılıklı vurması çekirdek eylemdir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yerde tutunup onun üzerinde savaşma düşüncesi, eyleme ilişkin olası bir türetim açıklamasıdır."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Silahlı karşılıklılık çekirdeğini ve bunun çatışma niteliğini doğrudan temsil eder.","boundary_detail":"Dal genel savaşmayı değil, tarafların kılıç veya sopalarla karşılıklı vuruşmasını kapsar; yerde kalma yalnız türetim açıklamasıdır.","branch_image_ar":"المبالدة بالسيوف والعصي","concept_gloss":"kılıç veya sopalarla karşılıklı vuruşma","contextual_glosses":[{"applicability":"Araçların kılıç veya sopa olduğu karşılıklı çatışma bağlamında doğal eylem karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yerde tutunarak savaşmaya dayanan olası türetim açıklamasını belirtmez.","preserves":"Karşılıklı silahlı dövüşme çekirdeğini korur."},"facet_ids":["F001"],"text":"silahlarla karşılıklı dövüşmek","usage_role":"general"}],"definition":"İki tarafın kılıç veya sopalarla birbirine karşılıklı vurup çatışmasıdır. Savaşçıların yerde tutunarak dövüşmesiyle kurulan bağlantı, anlamın kendisi değil olası bir türetim açıklamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tarafların kılıç veya sopalarla birbirine karşılıklı vurması çekirdek eylemdir."},{"facet_id":"F002","role":"associated_use","statement":"Yerde tutunup onun üzerinde savaşma düşüncesi, eyleme ilişkin olası bir türetim açıklamasıdır."}],"identity_rationale":"Kaynak ifade iki tarafın kılıç veya sopalarla karşılıklı vuruşmasını doğrudan verir; yerde tutunarak savaşma açıklaması ise olası bir türetim yorumudur. Bu yorum eylemin zorunlu parçası yapılmadan dal korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"kılıç veya sopalarla karşılıklı dövüşme"}],"lexicalization_note":"Çıplak biçim karşılıklı silahlı vuruşma anlamıyla tanımlanır; olası yerle bağlantı eylemin zorunlu koşulu sayılmaz.","neighbor_coverage_note":"Bütün savaş, düello, silah ve tek yönlü vurma adayları değerlendirildi; genel karşılıklı çarpışma ile öldürme amaçlı savaş en yararlı iki sınırı verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta belirli vurma araçları kurucudur; komşuda araç sınırlaması yoktur ve üstün gelme görünüşü öne çıkabilir.","focus_only":"Odak kılıç veya sopa araçlarını ve karşılıklı vuruşmayı açıkça sınırlar.","gloss":"rakiple çarpışma","neighbor_only":"Komşu kahramanların çarpışmasını, rakibe üstün gelmeyi ve daha genel karşılıklı mücadeleyi kapsar.","neighbor_ref":"root_001219/B002","relation_type":"near_synonym","shared_zone":"İki dal da rakip tarafların karşılıklı vuruşup mücadele etmesini anlatır."},{"boundary_match":"partial","distinction":"Komşu daha geniş savaş eylemi ve öldürme amacıyla tanımlanır; odak belirli araçlarla vuruşma biçimine dayanır.","focus_only":"Odak kılıç ve sopalarla karşılıklı vuruşma biçimini belirtir.","gloss":"karşılıklı savaşma","neighbor_only":"Komşu iki veya daha çok tarafın öldürme amacı taşıyan genel savaşmasını kapsar.","neighbor_ref":"root_001200/B011","relation_type":"near_neighbor","shared_zone":"Karşılıklı silahlı dövüş iki dalın da kapsamına girebilir."}],"source_phrase_ar":"المبالدة مثل المباطلة (sihah)؛ المبالدة كالمبالطة بالسيوف والعصي إذا تجالدوا بها (tahdhib)؛ المبالدة بالسيوف مثل المبالطة وقال بعضهم اشتق من الأول كأنهم لزموا الأرض فقاتلوا عليها (maqayis)","source_summary":"Kaynaklar kılıç ve sopalarla karşılıklı vuruşma anlamında birleşir. Eylemin yerde tutunarak savaşmadan türediği görüşü açıklayıcı bir öneridir ve çatışmanın zorunlu koşulu değildir.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه المبالدة بمعنى المجالدة أو المباطلة بالسيوف والعصي، واشتقاقها من لزوم الأرض في القتال إذا ذكر المصدر ذلك.","what_is_not_ar":"ليس فيه البلادة ضد الذكاء ولا مجرد الإقامة بالبلد."},"support_links":["sup_ded257294b490fcdcd06"]},{"boundary":"Dal deve kuşunun yumurta çukuru ile terk edilmiş yumurtasına özgüdür; genel yer, başka kuşların yumurtası veya yavru anlamını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000148/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:1:4:2","qac_word_ref":"90:1:4","surface_ar":"بَلَدِ"}],"gloss":"deve kuşunun yumurta çukuru ve orada bırakılmış yumurtası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Deve kuşunun yumurta bıraktığı çukur veya yuva çekirdektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli ad tamlaması, deve kuşunun bırakıp gittiği yumurtayı gösterir."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yuva niteliğindeki çukuru ve yalnız özel ad tamlamasındaki terk edilmiş yumurtayı birlikte kapsar.","boundary_detail":"Dal deve kuşunun yumurta çukuru ile terk edilmiş yumurtasına özgüdür; genel yer, başka kuşların yumurtası veya yavru anlamını kapsamaz.","branch_image_ar":"أدحي النعام","concept_gloss":"deve kuşunun yumurta çukuru ve orada bırakılmış yumurtası","contextual_glosses":[{"applicability":"Sözcük doğrudan kuşun yumurtladığı yer için kullanıldığında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Özel ad tamlamasında gösterilen bırakılmış yumurta anlamını dışarıda bırakır.","preserves":"Deve kuşunun yumurtlama çukuru olan çekirdeği korur."},"facet_ids":["F001"],"text":"deve kuşunun yumurta çukuru","usage_role":"general"},{"applicability":"Yalnız terk edilmiş yumurtayı gösteren belirli ad tamlamasında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yumurtanın bırakıldığı çukur veya yuva anlamını vermez.","preserves":"Bırakılmış deve kuşu yumurtası anlamını korur."},"facet_ids":["F002"],"text":"deve kuşunun bırakıp gittiği yumurta","usage_role":"contextual"}],"definition":"Deve kuşunun yumurtlamak için kullandığı çukur veya yuvadır; belirli bir ad tamlamasında, deve kuşunun bu yerde bırakıp gittiği yumurtayı da gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Deve kuşunun yumurta bıraktığı çukur veya yuva çekirdektir."},{"facet_id":"F002","role":"specialization","statement":"Belirli ad tamlaması, deve kuşunun bırakıp gittiği yumurtayı gösterir."}],"identity_rationale":"Kaynak ifade aynı dalda deve kuşunun yumurtlamak için kullandığı çukuru ve bu kuşun orada bırakıp gittiği yumurtayı açıkça verir. Genel yeryüzü parçası anlamı burada yalnız ortak biçimdir ve tanıma katılmaz.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"deve kuşunun yumurta çukuru"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"deve kuşunun bırakıp gittiği yumurta"}],"lexicalization_note":"Temel biçim deve kuşunun yumurta çukurunu gösterir; terk edilmiş yumurta anlamı yalnız belirtilen ad tamlamasına bağlıdır ve genel yumurta anlamına genişletilmez.","neighbor_coverage_note":"Bütün yumurta, yavru, yuva ve çöl adayları değerlendirildi; deve kuşu çukuru ile bırakılmış yumurta adayları dalın iki kurucu unsuruna doğrudan karşılık verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yuva anlamında büyük ölçüde örtüşürler; odak terk edilmiş yumurtaya, komşu ise çukurun hazırlanışına ve göksel kullanıma ayrıca uzanır.","focus_only":"Odak özel ad tamlamasında bırakılmış deve kuşu yumurtasını da kapsar.","gloss":"deve kuşunun yumurtlama çukuru","neighbor_only":"Komşu yuvanın kuş tarafından ayağıyla hazırlanmasını ve ayrıca göksel bir yer kullanımını bildirir.","neighbor_ref":"root_000462/B003","relation_type":"near_synonym","shared_zone":"İki dal da deve kuşunun yumurtlamak için kullandığı çukuru adlandırır."},{"boundary_match":"partial","distinction":"Odak yuva ile yumurtayı aynı dalda tutar; komşu yumurtadan benzetmeyle türeyen başka nesne adlarını kapsar.","focus_only":"Odak yumurtanın yanında deve kuşunun yumurta çukurunu da kapsar.","gloss":"bırakılmış deve kuşu yumurtası","neighbor_only":"Komşu bırakılmış yumurtadan başlık ve baş gibi benzetmeli nesnelere de genişler.","neighbor_ref":"root_000180/B008","relation_type":"near_synonym","shared_zone":"İki dal da kırda bırakılmış deve kuşu yumurtasını anlatabilir."}],"source_phrase_ar":"البلد أدحي النعام يقال هو أذل من بيضة البلد أي من بيضة النعام التي تتركها (sihah)","source_summary":"Tek kaynaklı kanıt deve kuşunun yumurta çukurunu temel kullanım, kuşun bırakıp gittiği yumurtayı ise belirli ad tamlamasına bağlı kullanım olarak verir. Yuva ile yumurta aynı varlık değildir ve tanımda ayrı tutulmalıdır.","sources":["SI"],"what_is_ar":"يدخل فيه البلد بمعنى أدحي النعام، وبيضة البلد أي بيضة النعام التي تتركها.","what_is_not_ar":"ليس فيه البلد بمعنى القرية أو الأرض العامة إلا على جهة الموضع الخاص."},"support_links":[]},{"boundary":"Supposing, considering, or mentally reckoning something to be the case.","branch_kind":null,"branch_ref":"root_000318/B002","candidate_links":[{"candidate_id":"cand_d5d7cddf4f13827e1e75","lane":"macro"}],"focus_root_occurrences":[],"gloss":"reckoning as supposition","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الحسبان والظن","image_en":"reckoning as supposition"}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الحسبان والظن","image_en":"reckoning as supposition","scope_ar":"يدخل فيه حسب الشيء أو الأمر بمعنى ظنه وقدره في النفس وما يقاربه من توقع غير جازم","scope_en":"Supposing, considering, or mentally reckoning something to be the case."},"support_links":["sup_4b7cbb824ef2374ff790"]},{"boundary":"Managing an affair well, holding someone to account, objecting to wrongdoing, and the public function of a محتسب.","branch_kind":null,"branch_ref":"root_000318/B006","candidate_links":[{"candidate_id":"cand_d5d7cddf4f13827e1e75","lane":"macro"}],"focus_root_occurrences":[],"gloss":"supervision and accountable management","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الحسبة والنظر في الأمر","image_en":"supervision and accountable management"}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الحسبة والنظر في الأمر","image_en":"supervision and accountable management","scope_ar":"يدخل فيه حسن التدبير في الأمر والإنكار على القبيح والمحاسبة العملية ومحتسب البلد","scope_en":"Managing an affair well, holding someone to account, objecting to wrongdoing, and the public function of a محتسب."},"support_links":["sup_4b7cbb824ef2374ff790"]},{"boundary":"Includes opinion, judgment, supposition, knowledge, deliberation, and seeking counsel","branch_kind":null,"branch_ref":"root_000531/B002","candidate_links":[{"candidate_id":"cand_d5d7cddf4f13827e1e75","lane":"macro"}],"focus_root_occurrences":[],"gloss":"opinion and reflective judgment","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"رأي القلب والتفكر","image_en":"opinion and reflective judgment"}}],"root_ar":"ر ء ي","root_id":"root_000531","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"رأي القلب والتفكر","image_en":"opinion and reflective judgment","scope_ar":"يدخل فيه الرأي والظن والعلم والتدبير والتروية والاستشارة في الرأي","scope_en":"Includes opinion, judgment, supposition, knowledge, deliberation, and seeking counsel"},"support_links":["sup_4b7cbb824ef2374ff790"]},{"boundary":"Includes the mirror, visible appearance, handsome aspect, and visible facial sign","branch_kind":null,"branch_ref":"root_000531/B006","candidate_links":[{"candidate_id":"cand_266c5efc419fba24d8a9","lane":"macro"}],"focus_root_occurrences":[],"gloss":"visible appearance and mirror","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"مرأى ومنظر ومرآة","image_en":"visible appearance and mirror"}}],"root_ar":"ر ء ي","root_id":"root_000531","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"مرأى ومنظر ومرآة","image_en":"visible appearance and mirror","scope_ar":"يدخل فيه المرآة التي ينظر فيها وحسن المرأى والرواء والرئي وما يظهر على الوجه من علامة","scope_en":"Includes the mirror, visible appearance, handsome aspect, and visible facial sign"},"support_links":["sup_59c023bb0995d074fe6f"]},{"boundary":"Wide, beautiful, prominent eyes, including descriptions of people, wild cattle, and حور عين.","branch_kind":null,"branch_ref":"root_001069/B016","candidate_links":[{"candidate_id":"cand_266c5efc419fba24d8a9","lane":"macro"}],"focus_root_occurrences":[],"gloss":"Wide beautiful eyes","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"سعة العين وحسنها","image_en":"Wide beautiful eyes"}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"سعة العين وحسنها","image_en":"Wide beautiful eyes","scope_ar":"العين والعيناء والأعين وما دل على سعة العين وحسنها، ومنه بقر الوحش والحور العين بحسب نصوص المصادر.","scope_en":"Wide, beautiful, prominent eyes, including descriptions of people, wild cattle, and حور عين."},"support_links":["sup_59c023bb0995d074fe6f"]},{"boundary":"Estimating, planning, intending, preparing, proportioning, or making something orderly by calculation or deliberation.","branch_kind":null,"branch_ref":"root_001205/B005","candidate_links":[{"candidate_id":"cand_d5d7cddf4f13827e1e75","lane":"macro"}],"focus_root_occurrences":[],"gloss":"arranging by estimate and deliberation","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"تدبير الأمر بتقدير ونظر","image_en":"arranging by estimate and deliberation"}}],"root_ar":"ق د ر","root_id":"root_001205","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"تدبير الأمر بتقدير ونظر","image_en":"arranging by estimate and deliberation","scope_ar":"يدخل فيه تقدير الأمر بالنظر والتفكير والقياس والنية، وتهيئة الشيء وتسويته وإحكامه، وحساب الهلال أو العدد.","scope_en":"Estimating, planning, intending, preparing, proportioning, or making something orderly by calculation or deliberation."},"support_links":["sup_4b7cbb824ef2374ff790"]},{"boundary":"Dal, malı bölme, yemin etme, öğle sıcağı ve öteki eşsesli anlamları kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001226/B001","candidate_links":[{"candidate_id":"cand_266c5efc419fba24d8a9","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَقْسَمُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aqosamu|ROOT:qsm|1S","morpheme_role":"STEM","pos":"V","qac_ref":"90:1:2:1","qac_word_ref":"90:1:2","surface_ar":"أُقْسِمُ"}],"gloss":"yüz güzelliği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüzde veya insan görünüşünde algılanan güzellik niteliğini bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güzel yüzün kendisini ya da güzel yüzlü kişiyi niteleyen kullanımları kapsar."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın soyut güzellik çekirdeğini ve güzelliğin özellikle yüzde görünmesini birlikte karşılar.","boundary_detail":"Dal, malı bölme, yemin etme, öğle sıcağı ve öteki eşsesli anlamları kapsamaz.","branch_image_ar":"حسن موزع في الوجه","concept_gloss":"yüz güzelliği","contextual_glosses":[{"applicability":"Bir kişiyi yüzünün güzelliğiyle niteleyen kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Soyut güzellik adı olarak kullanılabilme yönünü dışarıda bırakır.","preserves":"Kişinin yüz güzelliğini ve olumlu görünüşünü korur."},"facet_ids":["F002"],"text":"güzel yüzlü","usage_role":"contextual"},{"applicability":"Doğrudan yüzün kendisinin güzel diye nitelendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin bütünü için kullanılan niteleme ve soyut nitelik adı kapsamını kaybeder.","preserves":"Güzelliğin yüzde gerçekleşmesi yönünü korur."},"facet_ids":["F001","F002"],"text":"güzel yüz","usage_role":"contextual"}],"definition":"Yüzde ya da kişinin görünüşünde beliren güzellik ve yüz güzelliği niteliğidir. Bazı kullanımlar doğrudan güzel yüzü, bazıları da böyle bir yüze sahip kişiyi niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüzde veya insan görünüşünde algılanan güzellik niteliğini bildirir."},{"facet_id":"F002","role":"specialization","statement":"Güzel yüzün kendisini ya da güzel yüzlü kişiyi niteleyen kullanımları kapsar."}],"identity_rationale":"Kaynak ifadesi, güzelliği özellikle yüzde görülen bir nitelik olarak verir; hem soyut güzellik adlarını hem de güzel yüzlü kişi ve yüz betimlemelerini kapsar. Bu nedenle dalın yüz güzelliği ekseni kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"güzellik, güzel görünüş"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"eksiksiz güzellik"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yüz, özellikle yüzün güzel bölümü"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yakışıklı ya da güzel yaradılışlı erkek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"güzel yüzlü"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yüzü güzel ve uyumlu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"güzel yüz"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"güzel yüzlü kadın"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"güzel"}],"lexicalization_note":"Tanım, yalın güzellik adlarıyla yüzü niteleyen kalıpları ayırır; kalıba bağlı kişi nitelemelerini bütün dalın tek biçimi saymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca genel güzellik ve yüz uyumu dalları, yüz merkezli sınırı açıklayan yararlı karşılaştırmalar sundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yüz merkezli ve kişi nitelemelerine açıkken komşu dal nesnelere de uzanan genel güzellik ile kusursuzluğu bir araya getirir.","focus_only":"Güzelliği özellikle insan yüzünde ve güzel yüzlü kişi nitelemelerinde toplar.","gloss":"güzellik ve kusursuzluk","neighbor_only":"Her türlü şeyin güzelliğini ve kusurdan arınmışlığını daha geniş biçimde kapsar.","neighbor_ref":"root_000660/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin ya da yüzün güzel oluşunu bildirir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği güzelliktir; komşu dalın çekirdeği ise güzelliği doğuran yüz oranlarının karşılıklı dengelenmesidir.","focus_only":"Yüz güzelliğini uyumun nasıl kurulduğunu şart koşmadan bildirir.","gloss":"yüz güzelliğindeki uyum","neighbor_only":"Yüz parçalarının birbirine denk ve dengeli oluşunu güzelliğin belirleyici koşulu yapar.","neighbor_ref":"root_001511/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal yüzün güzel görünmesi alanında buluşur."}],"source_phrase_ar":"القسام وهو الحسن والجمال (maqayis)؛ القسيم من الرجال الحسن الخلق والقسمة الوجه (ayn)؛ القسام: الحسن وفلان قسيم الوجه ومقسم الوجه (sihah)؛ القسامة: الحسن التام ووجه مقسم أي حسن (tahdhib)؛ فلان مقسم الوجه وقسيم الوجه والقسامة الحسن (mufradat)","source_summary":"Kaynaklar, bu anlam alanında güzelliği ve yüz güzelliğini ortak çekirdek olarak verir; ad ve niteleme biçimleri güzel yüzü veya güzel yüzlü kişiyi anlatır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه حسن الوجه والقسمة والقسامة بمعنى الحسن، ووصف الرجل أو الوجه بأنه قسيم أو مقسم.","what_is_not_ar":"ليس هو تقسيم المال أو الحظوظ، ولا اليمين، ولا الاستقسام بالأزلام."},"support_links":["sup_59c023bb0995d074fe6f"]},{"boundary":"Anlam, genel sıcaklığa değil özellikle gün ortasındaki şiddetli sıcağa veya onun vaktine bağlıdır.","branch_kind":"bare","branch_ref":"root_001226/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَقْسَمُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aqosamu|ROOT:qsm|1S","morpheme_role":"STEM","pos":"V","qac_ref":"90:1:2:1","qac_word_ref":"90:1:2","surface_ar":"أُقْسِمُ"}],"gloss":"şiddetli öğle sıcağı veya vakti","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gün ortasında hissedilen şiddetli sıcağı bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı söz, şiddetli öğle sıcağının yaşandığı vakti de adlandırır."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynaklardaki sıcaklık yoğunluğu ile gün ortası zamanı okumalarının ikisini de açıkça taşır.","boundary_detail":"Anlam, genel sıcaklığa değil özellikle gün ortasındaki şiddetli sıcağa veya onun vaktine bağlıdır.","branch_image_ar":"حر الهاجرة","concept_gloss":"şiddetli öğle sıcağı veya vakti","contextual_glosses":[{"applicability":"Sözün sıcaklığın şiddetini anlattığı metinlerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sözcüğün doğrudan bir vakti adlandırabildiği okumasını kaybeder.","preserves":"Gün ortasındaki sıcaklığın yüksek şiddetini korur."},"facet_ids":["F001"],"text":"kavurucu öğle sıcağı","usage_role":"contextual"},{"applicability":"Sözün günün sıcak bir zaman dilimini adlandırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıcağın şiddetini başlı başına adlandıran okumayı geri plana iter.","preserves":"Gün ortasıyla sıcaklığın birlikte belirlediği vakti korur."},"facet_ids":["F002"],"text":"öğle sıcağı vakti","usage_role":"contextual"}],"definition":"Gün ortasında bastıran şiddetli sıcak ya da bu sıcağın yaşandığı vakittir. Kaynak anlatımı yoğunluk ile zaman adlandırmasını yan yana bırakır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gün ortasında hissedilen şiddetli sıcağı bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı söz, şiddetli öğle sıcağının yaşandığı vakti de adlandırır."}],"identity_rationale":"Kaynak ifadesi tek bir noktada birleşmez: bir aktarım sözcüğü öğle sıcağının şiddeti, diğeri ise bu sıcağın görüldüğü vakit olarak açıklar. Dal korunabilir, ancak hem yoğunluk hem zaman okuması açıkça belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"şiddetli öğle sıcağı veya öğle sıcağı vakti"}],"lexicalization_note":"Tanım yalın dalı kapsar ve başka dallardaki güzellik, bölüştürme ya da yemin anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gün ortası sıcağı dalı tam örtüşme, yaz sıcağı dalı ise zaman sınırını gösteren yakın karşılaştırma sağladı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek anlam ve sınırlar aynıdır; komşu karttaki hareket ve yemek bağlantıları bu ortak çekirdeğin bağımlı kullanımlarıdır.","focus_only":null,"gloss":"öğle sıcağı ve vakti","neighbor_only":null,"neighbor_ref":"root_001578/B005","relation_type":"synonym","shared_zone":"Her iki dal da gün ortasındaki şiddetli sıcağı ve bu sıcağın vaktini çekirdek anlam yapar."},{"boundary_match":"partial","distinction":"Odak dal gün ortasıyla sınırlıyken komşu dal yaz mevsimi ve sıcak dönemin süresi üzerinden daha geniş bir zaman çerçevesi kurar.","focus_only":"Sıcağı özellikle gün ortasına bağlar ve vakit adı olarak da kullanır.","gloss":"şiddetli yaz sıcağı","neighbor_only":"Şiddetli yaz sıcağını veya bunun sürdüğü dönemi gün ortası şartı olmadan anlatır.","neighbor_ref":"root_001672/B004","relation_type":"near_synonym","shared_zone":"İki dal da ağır ve bunaltıcı sıcaklık alanını paylaşır."}],"source_phrase_ar":"والقسام في شعر النابغة شدة الحر (maqayis)؛ القسام: وقت الهاجرة (tahdhib)","source_summary":"Toplu kaynak anlatımı, sözü bir yandan şiddetli öğle sıcağına, öte yandan bu sıcağın vaktine bağlar; bu iki okuma tek bir yoğun gün ortası sahnesinde birleşir.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه القسام بمعنى شدة الحر أو وقت الهاجرة كما في الشواهد.","what_is_not_ar":"ليس هو القسام بمعنى الحسن، ولا القسام الذي يقسم بين الناس."},"support_links":[]},{"boundary":"Dal, yemin etmeyi ve payın ok çekerek aranmasını değil gerçek bölme, dağıtma ve belirlenmiş payı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001226/B003","candidate_links":[{"candidate_id":"cand_5f655045bc1def917c73","lane":"macro"},{"candidate_id":"cand_9438f41b241fdc6c7539","lane":"macro"},{"candidate_id":"cand_b610bfdccb8389cabf39","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَقْسَمُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aqosamu|ROOT:qsm|1S","morpheme_role":"STEM","pos":"V","qac_ref":"90:1:2:1","qac_word_ref":"90:1:2","surface_ar":"أُقْسِمُ"}],"gloss":"paylara ayırma ve ayrılmış pay","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünü parçalara, kişilere veya belirlenmiş paylara ayırma ve dağıtma işlemini bildirir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayırma işlemi sonunda bir kimseye düşen belirli payı veya hakkı bildirir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birlikte paylaşan kişiyi ve miras ya da savaş kazancının hak sahiplerine dağıtılmasını kapsar."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İşlem olarak bölüştürmeyi ve sonuç olarak belirlenen payı aynı kısa karşılıkta korur.","boundary_detail":"Dal, yemin etmeyi ve payın ok çekerek aranmasını değil gerçek bölme, dağıtma ve belirlenmiş payı kapsar.","branch_image_ar":"إفراز النصيب وتقسيم الشيء","concept_gloss":"paylara ayırma ve ayrılmış pay","contextual_glosses":[{"applicability":"Bir şeyin kişiler veya paylar arasında dağıtıldığı işlem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşlem sonunda ortaya çıkan belirli payı ad olarak karşılamaz.","preserves":"Bütünü paylara ayırma ve dağıtma işlemini korur."},"facet_ids":["F001","F003"],"text":"bölüştürme","usage_role":"general"},{"applicability":"Bir bölüştürme sonucunda kişiye düşen bölümün anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bütünü ayırma ve payları dağıtma işlemini karşılamaz.","preserves":"Bir kimseye ayrılan belirli bölüm veya hak sonucunu korur."},"facet_ids":["F002"],"text":"pay","usage_role":"contextual"}],"definition":"Bir şeyi parçalara ya da hak sahiplerinin paylarına ayırma ve dağıtma işlemidir; ayrıca bu işlem sonunda ayrılan payı bildirir. Paylaşmaya katılan kişi ve miras ya da ganimetin sahiplerine dağıtılması bu çekirdeğin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünü parçalara, kişilere veya belirlenmiş paylara ayırma ve dağıtma işlemini bildirir."},{"facet_id":"F002","role":"core","statement":"Ayırma işlemi sonunda bir kimseye düşen belirli payı veya hakkı bildirir."},{"facet_id":"F003","role":"specialization","statement":"Birlikte paylaşan kişiyi ve miras ya da savaş kazancının hak sahiplerine dağıtılmasını kapsar."}],"identity_rationale":"Kaynak ifadesi bir bütünü parçalara veya hak sahiplerine ayırma işlemini, bu işlemle belirlenen payı ve paylaşmaya katılan kişiyi birlikte verir. Dalın işlem ve sonuç ayrımı bu içeriği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir şeyi parçalara veya paylara ayırmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"paylara ayırma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"pay, kişiye düşen bölüm"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bölüştürme, paylaşma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"arazi veya evleri paylaştıran kimse"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"birlikte paylaşan ortak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"öteki araziden ayrılmış arazi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"az suyu eşit paylaştırmaya yarayan taş"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kişilere ayrılmış paylar"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ayırma ve dağıtma"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"zaman onları ayırıp dağıttı"}],"lexicalization_note":"Tanım yalın bölme ve pay anlamlarını korurken belirli nesne, kişi ve araç kalıplarını bağımlı özel kullanımlar olarak ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel dağıtma, belirli hisse ve ortaklık dalları işlem, sonuç ve ortak sahiplik sınırlarını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirlenmiş pay ve hak sahibi yapısını korurken komşu dalın çekirdeği daha genel ayırma ve dağıtmadır.","focus_only":"Bölme işleminin yanında ayrılmış payı ve paylaşmaya katılan kişiyi de kapsar.","gloss":"bölme ve dağıtma","neighbor_only":"Dağılma ve genel dağıtma yönünü, belirli bir pay sonucu gerektirmeden öne çıkarır.","neighbor_ref":"root_001644/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir bütünü parçalara ayırma ve parçaları dağıtma işlemini bildirir."},{"boundary_match":"partial","distinction":"Odak dal işlem ile sonucu dengeler; komşu dalda belirli parça veya hisse, işlemin kendisinden daha merkezîdir.","focus_only":"Bütünün bölünme işlemini ve bölüştüren ya da birlikte paylaşan kişileri de kapsar.","gloss":"hisse ve pay","neighbor_only":"Bütünden kopan parçayı ve o parçanın birine verilmesini daha doğrudan öne çıkarır.","neighbor_ref":"root_000329/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir bütünden kişiye ayrılan payı ve payların bölüşülmesini kapsar."},{"boundary_match":"field_only","distinction":"Odak dalın çekirdeği ayırma ve pay belirlemedir; komşu dalın çekirdeği ise henüz ayrılmamış ortak sahiplik veya katılımdır.","focus_only":"Ortak veya tekil bir bütünü fiilen paylara ayırır ve her payı belirler.","gloss":"ortaklık ve katılma","neighbor_only":"Bir şeyin birden çok kişi arasında ortak olmasını ve ortakların ilişki kurmasını bildirir.","neighbor_ref":"root_000791/B001","relation_type":"same_field","shared_zone":"Her iki dal pay, ortaklar ve birden çok kişinin aynı mal üzerindeki ilişkisi alanında bulunur."}],"source_phrase_ar":"تجزئة شيء والنصيب قسم (maqayis)؛ القسم مصدر قسم والقسم الحظ من الخير والقسيم الذي يقاسمك أرضا أو مالا (ayn)؛ القسم مصدر قسمت الشئ والقسم الحظ والنصيب والتقسيم التفريق (sihah)؛ قسمت الشيء بينهم قسما وقسمة والقسم الحظ والنصيب (tahdhib)؛ القسم: إفراز النصيب وقسمة الميراث والغنيمة تفريقهما على أربابهما (mufradat)","source_summary":"Kaynaklar bölme, paylara ayırma ve dağıtma işlemiyle bu işlemden doğan pay üzerinde birleşir; ortaklaşa paylaşan kişi ile miras ve savaş kazancının sahiplerine verilmesi de bu çekirdeğe bağlanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه قسم الشيء وقسمته، وإفراز النصيب، والحظ والنصيب المقسوم، والقاسم والقسام، والقسيم الذي يقاسمك، وعزل أرض عن أرض، وتفريق الشيء أو الناس، وحصاة القسم في تسوية الماء.","what_is_not_ar":"ليس هو اليمين، ولا جمال الوجه، ولا طي القسامي، ولا حر الهاجرة."},"support_links":["sup_2845fd15b54a3d723e25","sup_41535c4caf8fdf90a0b4","sup_54154efd8595ba64b78d"]},{"boundary":"Buradaki dağıtma, mal paylaştırma anlamı değil; öldürme davasında yeminlerin ilgililere bölüştürülmesidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001226/B004","candidate_links":[{"candidate_id":"cand_c68d843c1c65d54b69b7","lane":"macro"},{"candidate_id":"cand_9438f41b241fdc6c7539","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَقْسَمُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aqosamu|ROOT:qsm|1S","morpheme_role":"STEM","pos":"V","qac_ref":"90:1:2:1","qac_word_ref":"90:1:2","surface_ar":"أُقْسِمُ"}],"gloss":"yemin etme ve öldürme davasında paylaştırılan yeminler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iddia veya söz için yemin etmeyi ve karşılıklı yeminleşmeyi bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Öldürme iddiasında yeminlerin öldürülen kişinin yakınlarına bölüştürüldüğü hukuk uygulamasını kapsar."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel yemin eylemiyle özel hukuk uygulamasındaki dağıtılmış yeminleri birlikte temsil eder.","boundary_detail":"Buradaki dağıtma, mal paylaştırma anlamı değil; öldürme davasında yeminlerin ilgililere bölüştürülmesidir.","branch_image_ar":"يمين مقسومة على أهلها","concept_gloss":"yemin etme ve öldürme davasında paylaştırılan yeminler","contextual_glosses":[{"applicability":"Genel olarak yemin etme veya verilen güçlü sözün adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öldürme davasında yeminlerin yakınlara paylaştırılması düzenini göstermez.","preserves":"Sözü yeminle güvenceye bağlama çekirdeğini korur."},"facet_ids":["F001"],"text":"yemin","usage_role":"general"},{"applicability":"Öldürme iddiasına özgü toplu yemin uygulamasının açıklanması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Her türlü yemin için geçerli olan genel eylem anlamını dışarıda bırakır.","preserves":"Yeminlerin öldürülen kişinin yakınları arasında dağıtılması özelliğini korur."},"facet_ids":["F002"],"text":"öldürme davasındaki paylaştırılmış yeminler","usage_role":"explanatory"}],"definition":"Bir sözün doğruluğunu güçlü bir tanıklık çağrısıyla güvenceye bağlayarak yemin etmedir. Özel hukuk kullanımında, öldürme iddiasında yeminlerin öldürülen kişinin yakınları arasında paylaştırılmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iddia veya söz için yemin etmeyi ve karşılıklı yeminleşmeyi bildirir."},{"facet_id":"F002","role":"specialization","statement":"Öldürme iddiasında yeminlerin öldürülen kişinin yakınlarına bölüştürüldüğü hukuk uygulamasını kapsar."}],"identity_rationale":"Kaynak ifadesi genel olarak yemin etmeyi ve bunun özel bir kökeni sayılan, öldürme davasında maktulün yakınlarına dağıtılan yeminleri birlikte açıklar. Dalın genel yemin ile özel hukuk uygulaması ayrımı bu yapıya uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yemin"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yemin etti"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"ona yemin etti veya onunla antlaştı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"Tanrı adına karşılıklı yemin ettiler"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"öldürme davasında yakınlara paylaştırılan yeminler"}],"lexicalization_note":"Tanım yalın yemin anlamıyla belirli yeminleşme ve öldürme davası kalıplarını ayırır; özel uygulamayı her yeminin zorunlu içeriği yapmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yemin dalı anlam yakınlığını, öldürme bedeli dalı ise özel hukuk alanındaki araç farkını görünür kıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Genel yemin alanında yakın olsalar da odak dalın belirleyici ek sınırı öldürme davasındaki dağıtılmış yeminlerdir.","focus_only":"Öldürme davasında yakınlara paylaştırılan yeminlerden oluşan özel uygulamayı da kapsar.","gloss":"yemin ve yemin etme","neighbor_only":"Çok yemin etme, birine yemin ettirme ve üzerine yemin edilen şeyi daha geniş biçimde kapsar.","neighbor_ref":"root_000349/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir sözü yemin yoluyla güçlü biçimde doğrulamayı bildirir."},{"boundary_match":"field_only","distinction":"Odak dal kanıtlama veya iddiayı destekleme aracı olarak yeminleri, komşu dal ise ceza yerine ödenen maddi bedeli merkez alır.","focus_only":"Öldürme iddiasını yeminlerin yakınlar arasında paylaştırılması yoluyla ele alır.","gloss":"öldürme bedeli","neighbor_only":"Öldürme karşılığında ödenen bedeli, bu bedeli ödeyen topluluğu ve bedel yoluyla çözümü bildirir.","neighbor_ref":"root_001036/B004","relation_type":"same_field","shared_zone":"İki dal da öldürme olayının hukukî sonuçları ve yakınların hak iddiası alanında yer alır."}],"source_phrase_ar":"اليمين فالقسم وأصل ذلك من القسامة وهي الأيمان تقسم على أولياء المقتول (maqayis)؛ القسم اليمين والفعل أقسم (ayn)؛ أقسمت حلفت وأصله من القسامة (sihah)؛ القسم اليمين وأقسمت إقساما وقسما والقسامة في الدم (tahdhib)؛ وأقسم: حلف وأصله من القسامة ثم صار اسما لكل حلف (mufradat)","source_summary":"Kaynaklar genel yemin anlamında birleşir ve bu anlamı, öldürme davasında yeminlerin yakınlara paylaştırıldığı özel uygulamayla ilişkilendirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه القسم بمعنى اليمين، وأقسم وحلف، وقاسمه حلف له، وتقاسموا بالله، والقسامة في الدم بوصفها أيمانا تقسم على أولياء المقتول.","what_is_not_ar":"ليس هو قسمة المال أو النصيب إلا من جهة الأصل الذي ترده المصادر إلى القسامة."},"support_links":["sup_54154efd8595ba64b78d","sup_bd1e762a3efedbfb8e99"]},{"boundary":"Dal yalnızca işaretli oklarla karar veya ayrılmış sonuç arama uygulamasına bağlıdır; genel bölüştürme ya da oyun oku anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001226/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَقْسَمُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aqosamu|ROOT:qsm|1S","morpheme_role":"STEM","pos":"V","qac_ref":"90:1:2:1","qac_word_ref":"90:1:2","surface_ar":"أُقْسِمُ"}],"gloss":"işaretli ok çekerek karar arama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İşaretli oklar çekerek ayrılmış sonucu ya da bir işi yapma veya bırakma kararını aramayı bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı türetim ayrıca birinden bir şeyi paylaştırmasını isteme anlamında aktarılır."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca işaretli oklarla yapılacak işi veya kişiye ayrılan sonucu belirleme uygulamasını karşılar.","boundary_detail":"Dal yalnızca işaretli oklarla karar veya ayrılmış sonuç arama uygulamasına bağlıdır; genel bölüştürme ya da oyun oku anlamı değildir.","branch_image_ar":"طلب القسم بالأزلام","concept_gloss":"işaretli ok çekerek karar arama","contextual_glosses":[{"applicability":"Bir eyleme girişme ya da ondan vazgeçme kararının ok çekmeyle arandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiye önceden ayrılmış sonucu öğrenme yönünü açıkça karşılamaz.","preserves":"Ok çekme aracını ve yapma ya da bırakma kararını korur."},"facet_ids":["F001"],"text":"işaretli oklarla yapıp yapmamaya karar vermek","usage_role":"explanatory"}],"definition":"Üzerinde yönlendirme işaretleri bulunan okları çekerek kişiye ayrılmış sonucu veya bir işi yapıp yapmamayı belirlemeye çalışma uygulamasıdır. Aynı türetimin birinden paylaştırmasını isteme kullanımı, çekirdeğin dışında bir kaynak çeşitlemesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İşaretli oklar çekerek ayrılmış sonucu ya da bir işi yapma veya bırakma kararını aramayı bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı türetim ayrıca birinden bir şeyi paylaştırmasını isteme anlamında aktarılır."}],"identity_rationale":"Kaynak ifadesinin ana bölümü, üzerinde yönlendirme işaretleri bulunan okları çekerek kişiye ayrılan sonucu veya yapılacak işi aramayı anlatır. Aynı toplu iddia daha geniş biçimde birinden paylaştırmasını istemeyi de anar; bu ikinci kullanım, oklarla yapılan uygulamanın çekirdeğine genellenemez.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"işaretli ok çekerek ayrılmış sonucu veya yapılacak işi belirleme"}],"lexicalization_note":"Tanım açıkça işaretli oklarla kurulan yapıya bağlıdır; aynı türetimin genel olarak paylaştırma isteme kullanımı yalın dal anlamına çevrilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; fiziksel ok ve araç adları anlam sınırını keskinleştirmedi, yalnızca gerçek paylaştırma dalı yararlı bir karşıtlık sundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal işaretli oklarla bilgi ya da karar arayan bir uygulamadır; komşu dal ise gerçek bir nesneyi veya hakkı paylaştırma işlemidir.","focus_only":"İşaretli oklar çekerek gelecekte yapılacak işi veya kişiye ayrıldığı düşünülen sonucu arar.","gloss":"paylara ayırma","neighbor_only":"Bir bütünü fiilen parçalara ve hak sahiplerinin paylarına ayırır.","neighbor_ref":"root_001226/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişiye düşen bölüm veya sonuç düşüncesi çevresinde ilişki kurar."}],"source_phrase_ar":"الاستقسام أنهم كانوا يجيلون السهام أي الأزلام (ayn)؛ واستقسم: طلب القسم بالازلام (sihah)؛ تستقسموا بالأزلام معناه تطلبوا من جهة الأزلام وما كتب عليها ما قسم لكم (tahdhib)؛ واستقسمته: سألته أن يقسم ثم قد يستعمل في معنى قسم (mufradat)","source_summary":"Toplu kaynak anlatımı, işaretli okları çevirip çekerek kişiye ayrılmış sonucu veya yapılacak işi arama uygulamasında birleşir; ayrıca aynı türetimin genel paylaştırma isteme kullanımı bulunduğunu belirtir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الاستقسام بالأزلام والقداح، أي طلب ما قسم أو تعيين المضي والترك بضرب السهام.","what_is_not_ar":"ليس هو مطلق القسمة بين الشركاء، ولا اليمين، ولا قداح الميسر حين تفرقها المصادر عن أزلام الأمر والنهي."},"support_links":[]},{"boundary":"Bu dal maddi bir şeyi paylaştırmayı değil, kararın seçeneklere ayrılmasını veya zihnin kaygılarla dağılmasını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001226/B006","candidate_links":[{"candidate_id":"cand_d5d7cddf4f13827e1e75","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَقْسَمُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aqosamu|ROOT:qsm|1S","morpheme_role":"STEM","pos":"V","qac_ref":"90:1:2:1","qac_word_ref":"90:1:2","surface_ar":"أُقْسِمُ"}],"gloss":"işi ölçüp biçme; kaygıyla zihnin dağılması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işin nasıl yapılacağını ölçüp biçme ve seçenekleri değerlendirme sürecini bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaygıların zihni veya kalbi farklı yönlere çekerek düşünceyi dağıtmasını bildirir."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın karar değerlendirmesi ile kaygı kaynaklı zihinsel dağılma kullanımlarını ayrı bölümler halinde korur.","boundary_detail":"Bu dal maddi bir şeyi paylaştırmayı değil, kararın seçeneklere ayrılmasını veya zihnin kaygılarla dağılmasını anlatır.","branch_image_ar":"بال مقسم بين وجوه الأمر","concept_gloss":"işi ölçüp biçme; kaygıyla zihnin dağılması","contextual_glosses":[{"applicability":"Bir kişinin nasıl davranacağını düşünüp seçenekleri değerlendirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaygıların zihni farklı yönlere dağıtması anlamını dışarıda bırakır.","preserves":"Bir işin uygulanışını düşünme ve seçenekleri değerlendirme sürecini korur."},"facet_ids":["F001"],"text":"işi ölçüp biçmek","usage_role":"contextual"},{"applicability":"Kaygıların kişinin düşüncesini birçok yöne çektiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işi planlayarak nasıl yapacağını değerlendirme anlamını karşılamaz.","preserves":"Kaygı nedeniyle düşüncenin bölünüp dağılması sonucunu korur."},"facet_ids":["F002"],"text":"kaygıdan zihni dağılmak","usage_role":"contextual"}],"definition":"Bir işi nasıl yürüteceğini ölçüp biçerek seçenekleri değerlendirmeyi anlatır. Başka bir kullanımda, kaygıların kişinin düşüncesini farklı yönlere çekip dağıtmasını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işin nasıl yapılacağını ölçüp biçme ve seçenekleri değerlendirme sürecini bildirir."},{"facet_id":"F002","role":"extension","statement":"Kaygıların zihni veya kalbi farklı yönlere çekerek düşünceyi dağıtmasını bildirir."}],"identity_rationale":"Kaynak ifadesi bölme düşüncesini zihinsel alana iki ayrı biçimde taşır: kişi bir işi nasıl yapacağını ölçüp biçer veya kaygılar düşüncesini farklı yönlere dağıtır. Dal, bu iki kullanımı birbirine karıştırmadan ayırdığı sürece kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"işini ölçüp biçiyor ve nasıl yapacağını düşünüyor"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"kaygının dağıttığı zihin"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"kaygılar yüzünden düşüncesi dağılmış"}],"lexicalization_note":"Tanım, işi ölçüp biçme yapısıyla kaygılı zihin nitelemelerini ayrı tutar ve bunlardan genel bir yalın bölme anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; görüş karışıklığı ve tek olmayan görüş dalları zihinsel bölünmenin nedenini ve katılımcı yapısını ayırt etmeye yaradı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal değerlendirme sürecini de içerebilir ve dağılmayı kaygıya bağlar; komşu dalda belirleyici olan kuşku ve görüş karışıklığıdır.","focus_only":"Ya bilinçli seçenek değerlendirmesini ya da kaygının düşünceyi yönlere ayırmasını bildirir.","gloss":"kararsız ve karışık görüş","neighbor_only":"Kişinin görüşünde kuşkuya düşmesini ve ne yapacağını bilemeyecek ölçüde karışmasını bildirir.","neighbor_ref":"root_000576/B005","relation_type":"near_neighbor","shared_zone":"İki dal da düşüncenin tek bir kararlı yönde ilerleyemediği zihinsel durumu kapsar."},{"boundary_match":"partial","distinction":"Odak dal içsel değerlendirme ya da kaygı kaynaklı dağılmadır; komşu dalın ayrılığı ise görüşün ortaklaşa taşınması veya kişinin kendine seslenmesidir.","focus_only":"Tek kişinin zihninin seçenekler veya kaygılar arasında bölünmesini anlatır.","gloss":"ortak veya tek olmayan görüş","neighbor_only":"Bir görüşün birden çok kişi arasında ortak olmasını veya kişinin kendi kendine konuşmasını anlatır.","neighbor_ref":"root_000791/B008","relation_type":"near_neighbor","shared_zone":"İki dal da düşüncenin tek ve yalın bir yön taşımaması noktasında buluşur."}],"source_phrase_ar":"أمسى فلان متقسما أي كأن خواطر الهموم تقسمته (maqayis)؛ هو يقسم أمره قسما أي يقدره وينظر فيه كيف يفعل (sihah)؛ يقسم أمره قسما أي يقدره ينظر كيف يعمل فيه (tahdhib)؛ رجل منقسم القلب أي اقتسمه الهم (mufradat)","source_summary":"Kaynaklar bölünme tasarımını zihinsel alana taşır: bir kullanım işi nasıl yapacağını düşünüp tartmayı, öteki kullanım ise kaygıların zihni bölüp dağıtmasını anlatır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه تقسيم الأمر بمعنى تقديره والنظر كيف يفعل، وتوزع القلب أو الخاطر بالهموم.","what_is_not_ar":"ليس هو التقسيم الحسي للمال أو الأرض، ولا الاستقسام بالأزلام."},"support_links":["sup_4b7cbb824ef2374ff790"]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_001226/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَقْسَمُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aqosamu|ROOT:qsm|1S","morpheme_role":"STEM","pos":"V","qac_ref":"90:1:2:1","qac_word_ref":"90:1:2","surface_ar":"أُقْسِمُ"}],"gloss":"yalıtık adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Giysileri ilk kez katlayıp kumaşta ilk kat izlerini oluşturan kişiyi bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin iki durum arasında bulunmasını, özellikle bir atın iki gelişim evresi arasında kalmasını bildirir."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"طي القسامي أول الثوب","concept_gloss":"yalıtık adlandırmalar","contextual_glosses":[{"applicability":"Kumaşın ilk kez katlanıp kat izlerinin oluşturulduğu meslek veya iş bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki durum arasında bulunan şey veya hayvan anlamını dışarıda bırakır.","preserves":"Giysiyi ilk kez katlayan kişiyi ve ilk kat oluşturma işini korur."},"facet_ids":["F001"],"text":"giysinin ilk katını yapan kimse","usage_role":"explanatory"},{"applicability":"Bir varlığın iki gelişim durumu arasında kaldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Giysiyi ilk kez katlayan kişi anlamını dışarıda bırakır.","preserves":"Bir varlığın iki ayrı durum arasında bulunması özelliğini korur."},"facet_ids":["F002"],"text":"iki durum arasında bulunan","usage_role":"explanatory"}],"definition":"Kayıt, bir yanda giysileri ilk kez katlayarak kat yerlerini oluşturan kişiyi, öte yanda iki durum arasında bulunan şeyi anlatır. Bu iki anlam tek bir kavram değildir ve ayrı dallar gerektirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Giysileri ilk kez katlayıp kumaşta ilk kat izlerini oluşturan kişiyi bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Bir şeyin iki durum arasında bulunmasını, özellikle bir atın iki gelişim evresi arasında kalmasını bildirir."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"giysiyi ilk kez katlayıp kat izlerini oluşturan kimse"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"iki durum arasında bulunan, özellikle iki gelişim evresi arasındaki at"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"القسامى وهو الذي يطوى الثياب أول طيها (maqayis)؛ القسامى الذى يطوى الثياب أول طيها حتى تتكسر على طيه (sihah)؛ القسامي الذي يطوي الثياب أول طيها والقسامي الذي يكون بين شيئين (tahdhib)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه القسامي الذي يطوي الثياب أول طيها، وما ألحق به من كونه بين شيئين في وصف الفرس.","what_is_not_ar":"ليس هو القاسم الذي يقسم المال، ولا القسام بمعنى الحسن أو الحر."},"support_links":[]},{"boundary":"Bu dal genel barışın bütün türlerini, yüz güzelliğini veya öldürme davasındaki yeminleri kapsamaz.","branch_kind":"bare","branch_ref":"root_001226/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَقْسَمُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aqosamu|ROOT:qsm|1S","morpheme_role":"STEM","pos":"V","qac_ref":"90:1:2:1","qac_word_ref":"90:1:2","surface_ar":"أُقْسِمُ"}],"gloss":"düşman ile Müslümanlar arasındaki ateşkes","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Düşman ile Müslümanlar arasında çatışmayı durduran ateşkesi bildirir."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakta belirtilen iki taraf arasında çatışmanın durdurulduğu özel ateşkes anlamını karşılar.","boundary_detail":"Bu dal genel barışın bütün türlerini, yüz güzelliğini veya öldürme davasındaki yeminleri kapsamaz.","branch_image_ar":"هدنة قسامة","concept_gloss":"düşman ile Müslümanlar arasındaki ateşkes","contextual_glosses":[{"applicability":"Tarafların metinde zaten açık olduğu ve çatışmaya ara verilmesinin anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":"Kaynakta belirtilen taraflar dışındaki her türlü ateşkese uygulanabilen daha geniş bir kapsam ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Çatışmanın anlaşmayla durdurulması çekirdeğini korur."},"facet_ids":["F001"],"text":"ateşkes","usage_role":"contextual"}],"definition":"Düşman ile Müslümanlar arasında çatışmaya ara veren ateşkestir. Kaynak, tarafları ve savaşın geçici olarak durmasını anlamın sınırı olarak verir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Düşman ile Müslümanlar arasında çatışmayı durduran ateşkesi bildirir."}],"identity_rationale":"Kaynak ifadesi anlamı doğrudan düşman ile Müslümanlar arasındaki çatışmasızlık anlaşması olarak verir. Dalın ateşkes çerçevesi bu tekil aktarımı eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"düşman ile Müslümanlar arasındaki ateşkes"}],"lexicalization_note":"Tanım yalın dalı kaynakta belirtilen taraflar arasındaki ateşkesle sınırlar ve başka barış türlerine kendiliğinden genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; karşılıklı çatışmayı bırakma ve genel barış dalları ateşkesin taraf ve süre bakımından daha dar sınırını gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli taraflar arasındaki ateşkestir; komşu dal tarafları sınırlamayan ve uzlaşma ile saldırmama sözünü de kapsayan daha geniş bir bırakışmadır.","focus_only":"Tarafları özellikle düşman ile Müslümanlar olarak sınırlar.","gloss":"karşılıklı çatışmayı bırakma","neighbor_only":"Karşılıklı saldırmama, uzlaşma, savaşı bırakma ve savaş açmama sözü gibi daha geniş anlaşma türlerini kapsar.","neighbor_ref":"root_001635/B004","relation_type":"near_synonym","shared_zone":"İki dal da karşıt tarafların çatışmayı bırakması ve bir süre saldırmaması alanında buluşur."},{"boundary_match":"partial","distinction":"Ateşkes geçici ve tarafları belirli bir çatışma düzenlemesidir; komşu dal daha genel ve kalıcı olabilen barış durumunu anlatır.","focus_only":"Belirli taraflar arasında çatışmaya ara veren sınırlı ateşkesi bildirir.","gloss":"barış ve uzlaşma","neighbor_only":"Savaşın karşıtı olarak genel barış, uzlaşma ve barış içinde olma durumunu kapsar.","neighbor_ref":"root_000737/B004","relation_type":"near_synonym","shared_zone":"Her iki dal silahlı çatışmanın durması ve tarafların savaşmaması durumunu içerir."}],"source_phrase_ar":"القسامة: الهدنة بين العدو وبين المسلمين (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu anlam yalnızca bir kaynakta, düşman ile Müslümanlar arasındaki ateşkes olarak aktarılır."}],"source_summary":"Tek kaynaklı aktarım, sözü düşman ile Müslümanlar arasındaki ateşkes olarak tanımlar ve başka bir barış ya da yemin anlamı eklemez.","sources":["TA"],"what_is_ar":"يدخل فيه القسامة بمعنى الهدنة بين العدو وبين المسلمين.","what_is_not_ar":"ليس هو القسامة بمعنى الحسن، ولا القسامة في الدم والأيمان."},"support_links":[]},{"boundary":"Includes al-qal as the stick used to strike the qilla.","branch_kind":null,"branch_ref":"root_001272/B008","candidate_links":[{"candidate_id":"cand_1d09325403f9b60cb561","lane":"macro"}],"focus_root_occurrences":[],"gloss":"the qal stick used in the game of qilla","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"عود القال لضرب القلة","image_en":"the qal stick used in the game of qilla"}}],"root_ar":"ق و ل","root_id":"root_001272","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"عود القال لضرب القلة","image_en":"the qal stick used in the game of qilla","scope_ar":"يدخل فيه القال، الخشبة التي تضرب بها القلة.","scope_en":"Includes al-qal as the stick used to strike the qilla."},"support_links":["sup_ded257294b490fcdcd06"]},{"boundary":"Includes qala/taqulu when used grammatically like zanna, taking the work of supposing, especially in questions and in the reported Banu Sulaym usage.","branch_kind":null,"branch_ref":"root_001272/B011","candidate_links":[{"candidate_id":"cand_d5d7cddf4f13827e1e75","lane":"macro"}],"focus_root_occurrences":[],"gloss":"saying used with the force of supposing","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"قول يجري مجرى الظن","image_en":"saying used with the force of supposing"}}],"root_ar":"ق و ل","root_id":"root_001272","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"قول يجري مجرى الظن","image_en":"saying used with the force of supposing","scope_ar":"يدخل فيه تقول إذا أجري مجرى تظن في العمل، وخاصة في الاستفهام، وما ذكر عن بني سليم من إجراء متصرف قلت مجرى الظن في غير الاستفهام.","scope_en":"Includes qala/taqulu when used grammatically like zanna, taking the work of supposing, especially in questions and in the reported Banu Sulaym usage."},"support_links":["sup_4b7cbb824ef2374ff790"]},{"boundary":"Includes a thought or inner saying conceived in the self before being expressed in words.","branch_kind":null,"branch_ref":"root_001272/B012","candidate_links":[{"candidate_id":"cand_d5d7cddf4f13827e1e75","lane":"macro"}],"focus_root_occurrences":[],"gloss":"unspoken inner saying","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"قول في النفس لم يظهر","image_en":"unspoken inner saying"}}],"root_ar":"ق و ل","root_id":"root_001272","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"قول في النفس لم يظهر","image_en":"unspoken inner saying","scope_ar":"يدخل فيه المتصور في النفس قبل الإبراز باللفظ، كما في قول في نفسي لم أظهره.","scope_en":"Includes a thought or inner saying conceived in the self before being expressed in words."},"support_links":["sup_4b7cbb824ef2374ff790"]},{"boundary":"the bow's grip or thick central area where the hand or arrow is set","branch_kind":null,"branch_ref":"root_001280/B004","candidate_links":[{"candidate_id":"cand_1d09325403f9b60cb561","lane":"macro"}],"focus_root_occurrences":[],"gloss":"the bow grip or central grip area","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"كَبِد القوس","image_en":"the bow grip or central grip area"}}],"root_ar":"ك ب د","root_id":"root_001280","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"كَبِد القوس","image_en":"the bow grip or central grip area","scope_ar":"مقبض القوس وغلظ موضعه وما بين مقبضها ومجرى السهم","scope_en":"the bow's grip or thick central area where the hand or arrow is set"},"support_links":["sup_ded257294b490fcdcd06"]},{"boundary":"Includes courage, strength, valor, calling for help, giving help, fighting, overcoming, and becoming strong after weakness or illness","branch_kind":null,"branch_ref":"root_001473/B003","candidate_links":[{"candidate_id":"cand_1d09325403f9b60cb561","lane":"macro"}],"focus_root_occurrences":[],"gloss":"strong courage and help","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"البأس والنصرة","image_en":"strong courage and help"}}],"root_ar":"ن ج د","root_id":"root_001473","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"البأس والنصرة","image_en":"strong courage and help","scope_ar":"يدخل فيه شجاعة الرجل وقوته وبأسه؛ والنجدة؛ والاستنجاد طلبا للعون؛ والإعانة؛ والمناجدة في القتال؛ والغلبة؛ والقوة بعد ضعف أو مرض","scope_en":"Includes courage, strength, valor, calling for help, giving help, fighting, overcoming, and becoming strong after weakness or illness"},"support_links":["sup_ded257294b490fcdcd06"]},{"boundary":"Includes a person tested, hardened, strengthened, or made experienced by time and events","branch_kind":null,"branch_ref":"root_001473/B010","candidate_links":[{"candidate_id":"cand_d5d7cddf4f13827e1e75","lane":"macro"}],"focus_root_occurrences":[],"gloss":"tempering by experience","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"تجربة الدهر","image_en":"tempering by experience"}}],"root_ar":"ن ج د","root_id":"root_001473","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"تجربة الدهر","image_en":"tempering by experience","scope_ar":"يدخل فيه المنجد الذي عرف وجرب؛ ومن نجده الدهر أو قواه وشدده بما رأى من التجربة","scope_en":"Includes a person tested, hardened, strengthened, or made experienced by time and events"},"support_links":["sup_4b7cbb824ef2374ff790"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000318/B001","candidate_links":[{"candidate_id":"cand_9438f41b241fdc6c7539","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a185e39047a46a55a953","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies counting and reckoning and turns the interrogative thought into an audit operation.","root":"ح س ب","source_ref":"90:5","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000318","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_54154efd8595ba64b78d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000351/B001","candidate_links":[{"candidate_id":"cand_c68d843c1c65d54b69b7","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7c5d261d246695f0cef4","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies the literal untying of a knot and recasts the oath-place relation as something that can be loosened.","root":"ح ل ل","source_ref":"90:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000351","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bd1e762a3efedbfb8e99"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000351/B002","candidate_links":[{"candidate_id":"cand_c68d843c1c65d54b69b7","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7c5d261d246695f0cef4","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies settling in a place and makes the addressee's presence inside the boundary operational.","root":"ح ل ل","source_ref":"90:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000351","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bd1e762a3efedbfb8e99"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000351/B003","candidate_links":[{"candidate_id":"cand_c68d843c1c65d54b69b7","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7c5d261d246695f0cef4","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies dissolution of a prohibition and gives the repeated city a changing legal status.","root":"ح ل ل","source_ref":"90:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000351","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bd1e762a3efedbfb8e99"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000351/B005","candidate_links":[{"candidate_id":"cand_c68d843c1c65d54b69b7","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7c5d261d246695f0cef4","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies release or discharge from an oath and directly feeds back upon the opening oath mechanism.","root":"ح ل ل","source_ref":"90:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000351","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bd1e762a3efedbfb8e99"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000531/B001","candidate_links":[{"candidate_id":"cand_9438f41b241fdc6c7539","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a185e39047a46a55a953","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies sight by eye and insight and closes the account under an observing witness.","root":"ر ء ي","source_ref":"90:7","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000531","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_54154efd8595ba64b78d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001205/B001","candidate_links":[{"candidate_id":"cand_9438f41b241fdc6c7539","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a185e39047a46a55a953","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies a measure reaching its limit and gives the audit a scale against which claims are bounded.","root":"ق د ر","source_ref":"90:5","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001205","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_54154efd8595ba64b78d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001251/B001","candidate_links":[{"candidate_id":"cand_b610bfdccb8389cabf39","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_0c49882a40e7f8ccb64d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies smallness from the non-dominant mapped root and reverses the asserted magnitude of the spoken claim.","root":"ق و ل","source_ref":"90:6","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001251","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2845fd15b54a3d723e25"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001272/B001","candidate_links":[{"candidate_id":"cand_9438f41b241fdc6c7539","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a185e39047a46a55a953","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies an uttered statement and identifies the wealth expenditure as a claim rather than self-validating fact.","root":"ق و ل","source_ref":"90:6","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001272","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_54154efd8595ba64b78d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001340/B002","candidate_links":[{"candidate_id":"cand_9438f41b241fdc6c7539","lane":"macro"},{"candidate_id":"cand_b610bfdccb8389cabf39","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a185e39047a46a55a953","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies accumulated layers or masses and gives the boast its asserted magnitude.","root":"ل ب د","source_ref":"90:6","source_word_indices":["4"]},{"hft_ref":"hft_0c49882a40e7f8ccb64d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies piled mass and intensifies the abundance whose rhetorical size is being shrunk.","root":"ل ب د","source_ref":"90:6","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001340","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2845fd15b54a3d723e25","sup_54154efd8595ba64b78d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001457/B001","candidate_links":[{"candidate_id":"cand_9438f41b241fdc6c7539","lane":"macro"},{"candidate_id":"cand_b610bfdccb8389cabf39","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a185e39047a46a55a953","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies acquisition and abundance of wealth and provides the audit's material object.","root":"م و ل","source_ref":"90:6","source_word_indices":["3"]},{"hft_ref":"hft_0c49882a40e7f8ccb64d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies abundant acquired wealth and establishes the scale that the counterimage contests.","root":"م و ل","source_ref":"90:6","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001457","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2845fd15b54a3d723e25","sup_54154efd8595ba64b78d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001596/B009","candidate_links":[{"candidate_id":"cand_9438f41b241fdc6c7539","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a185e39047a46a55a953","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies exhaustion or consumption of effort and sharpens what the speaker alleges was spent.","root":"ه ل ك","source_ref":"90:6","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001596","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_54154efd8595ba64b78d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001683/B003","candidate_links":[{"candidate_id":"cand_5f655045bc1def917c73","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d14567cf78cde7282ade","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies the event of birth and changes the place from static boundary into a site of temporal emergence.","root":"و ل د","source_ref":"90:3","source_word_indices":["1","3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001683","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_41535c4caf8fdf90a0b4"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001683/B005","candidate_links":[{"candidate_id":"cand_5f655045bc1def917c73","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d14567cf78cde7282ade","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies something produced from something else and makes civic inheritance a generative chain rather than mere occupancy.","root":"و ل د","source_ref":"90:3","source_word_indices":["1","3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001683","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_41535c4caf8fdf90a0b4"]}],"candidate_inventory":[{"anchor_refs":["90:1","90:7","90:8"],"branch_refs":["root_000148/B003","root_000531/B006","root_001069/B016","root_001226/B001"],"candidate_id":"cand_266c5efc419fba24d8a9","commentary_obligation":"review","focus_branch_refs":["root_000148/B003","root_001226/B001"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000531/B006","root_001069/B016"],"root_ids":[],"scope":"pericope","source_local_id":"A:Brow, Facial Beauty, and Wide Eyes","source_type":"channel","support_ids":["sup_3e5d02509d23ad94c770","sup_47f713c41503ca9954ce","sup_59c023bb0995d074fe6f","sup_f2f5d9adb0e8ddb4c404","sup_f5073b77f4e8bb1e112f"],"title":"Brow, Facial Beauty, and Wide Eyes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:1","90:10","90:4","90:6"],"branch_refs":["root_000148/B011","root_001272/B008","root_001280/B004","root_001473/B003"],"candidate_id":"cand_1d09325403f9b60cb561","commentary_obligation":"review","focus_branch_refs":["root_000148/B011"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001272/B008","root_001280/B004","root_001473/B003"],"root_ids":[],"scope":"pericope","source_local_id":"B:Sword, Stick, and Close Combat","source_type":"channel","support_ids":["sup_6bc2d69f5ccc6e1de1ec","sup_ae67ec1c3ab2b02c0236","sup_b9c95f2b9d66f3d762ba","sup_ded257294b490fcdcd06","sup_ec4166c3914d21cd1e5d"],"title":"Sword, Stick, and Close Combat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:1","90:10","90:5","90:6","90:7"],"branch_refs":["root_000318/B002","root_000318/B006","root_000531/B002","root_001205/B005","root_001226/B006","root_001272/B011","root_001272/B012","root_001473/B010"],"candidate_id":"cand_d5d7cddf4f13827e1e75","commentary_obligation":"review","focus_branch_refs":["root_001226/B006"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000318/B002","root_000318/B006","root_000531/B002","root_001205/B005","root_001272/B011","root_001272/B012","root_001473/B010"],"root_ids":[],"scope":"pericope","source_local_id":"E:Planning, Opinion, and Deliberation","source_type":"channel","support_ids":["sup_484c4cdd42172ec56cbb","sup_4b7cbb824ef2374ff790","sup_a954d4d10fb2ccc6554b","sup_eccf061b44e3212c1080","sup_f85fa1b54247257f67bb"],"title":"Planning, Opinion, and Deliberation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:1","90:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:1","branch_refs":["root_000148/B001","root_000351/B001","root_000351/B002","root_000351/B003","root_000351/B005","root_001226/B004"],"candidate_id":"cand_c68d843c1c65d54b69b7","commentary_obligation":"review","hft_ref":"hft_7c5d261d246695f0cef4","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_oath_boundary_unbound","source_type":"hft","support_ids":["sup_bd1e762a3efedbfb8e99"],"title":"d_oath_boundary_unbound","trust":"legacy_unbound"},{"anchor_refs":["90:1","90:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:1","branch_refs":["root_000148/B001","root_001226/B003","root_001683/B003","root_001683/B005"],"candidate_id":"cand_5f655045bc1def917c73","commentary_obligation":"review","hft_ref":"hft_d14567cf78cde7282ade","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_generational_city_allotment","source_type":"hft","support_ids":["sup_41535c4caf8fdf90a0b4"],"title":"d_generational_city_allotment","trust":"legacy_unbound"},{"anchor_refs":["90:1","90:5","90:6","90:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:1","branch_refs":["root_000148/B001","root_000318/B001","root_000531/B001","root_001205/B001","root_001226/B003","root_001226/B004","root_001272/B001","root_001340/B002","root_001457/B001","root_001596/B009"],"candidate_id":"cand_9438f41b241fdc6c7539","commentary_obligation":"review","hft_ref":"hft_a185e39047a46a55a953","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_oath_as_public_account","source_type":"hft","support_ids":["sup_54154efd8595ba64b78d"],"title":"d_oath_as_public_account","trust":"legacy_unbound"},{"anchor_refs":["90:1","90:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:1","branch_refs":["root_000148/B001","root_001226/B003","root_001251/B001","root_001340/B002","root_001457/B001"],"candidate_id":"cand_b610bfdccb8389cabf39","commentary_obligation":"review","hft_ref":"hft_0c49882a40e7f8ccb64d","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_piled_boast_shrunk_by_split_root","source_type":"hft","support_ids":["sup_2845fd15b54a3d723e25"],"title":"o_piled_boast_shrunk_by_split_root","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_8864acfdedb2ffff42cb","connection_ref":"conn_3f31dd9518f0d0eabb31","note":"Direct continuation: the city is further specified through the addressed person; V12 positively supports f02.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_455299fa4190e0f8b97b","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"90:2","source_note":"The preceding oath repeats the city frame and directly anchors f01.","source_row_role":"ranked_review","source_target_component_ref":"90:1","source_target_components":["90:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"90:2","source_target_components":["90:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:2","target_evidence":{"arabic_uthmani":"وَأَنتَ حِلٌّۢ بِهَٰذَا ٱلْبَلَدِ","ayah_ref":"90:2"},"target_ref":"90:2"},{"connection_evidence_ref":"conn_ev_9e05cc810de30f910b8d","connection_ref":"conn_979cea83aacbbd6e110c","note":"Same-surah human faculties extend the person-and-responsibility horizon.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_1c3d0119da5fb609dbba","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"90:9","source_note":"No focused addition to tongue or lips.","source_row_role":"ranked_review","source_target_component_ref":"90:1","source_target_components":["90:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"90:9","source_target_components":["90:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:9","target_evidence":{"arabic_uthmani":"وَلِسَانًۭا وَشَفَتَيْنِ","ayah_ref":"90:9"},"target_ref":"90:9"},{"connection_evidence_ref":"conn_ev_58e3769fc9120e14ba1e","connection_ref":"conn_789e4a1822afa845e211","note":"Same-surah wealth claim adds the resource-and-responsibility side of the social reading.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_ebf6846a193de4bac01c","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"90:6","source_note":"The oath setting does not specify the speech or expenditure.","source_row_role":"ranked_review","source_target_component_ref":"90:1","source_target_components":["90:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"90:6","source_target_components":["90:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:6","target_evidence":{"arabic_uthmani":"يَقُولُ أَهْلَكْتُ مَالًۭا لُّبَدًا","ayah_ref":"90:6"},"target_ref":"90:6"},{"connection_evidence_ref":"conn_ev_f6b990d8392b354b7cd7","connection_ref":"conn_680520fea4d9ac87fd3e","note":"Same-surah challenge of human power is only indirectly related to the focal oath.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_2bb9e68d761ec1f9b586","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"90:5","source_note":"Surenin yerel çerçevesini verir; 90:5 okumasına sınırlı ek yapar.","source_row_role":"ranked_review","source_target_component_ref":"90:1","source_target_components":["90:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"90:5","source_target_components":["90:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:5","target_evidence":{"arabic_uthmani":"أَيَحْسَبُ أَن لَّن يَقْدِرَ عَلَيْهِ أَحَدٌۭ","ayah_ref":"90:5"},"target_ref":"90:5"},{"connection_evidence_ref":"conn_ev_56750fbb610c2c166ca7","connection_ref":"conn_65c396cd02cc2d1bccac","note":"Same-surah observation theme is only indirectly related to the focal oath.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_40fd8881855472857256","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"90:7","source_note":"Immediate oath setting adds no explanatory viewing relation.","source_row_role":"ranked_review","source_target_component_ref":"90:1","source_target_components":["90:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"90:7","source_target_components":["90:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:7","target_evidence":{"arabic_uthmani":"أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ","ayah_ref":"90:7"},"target_ref":"90:7"},{"connection_evidence_ref":"conn_ev_7b3b17888de65155708b","connection_ref":"conn_ab5ade185257e02efb69","note":"Same-surah paired paths extend terrain imagery into human direction and choice.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_ef46d422d3080ef2041f","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"90:10","source_note":"Surah setting is only indirect context for the focus.","source_row_role":"ranked_review","source_target_component_ref":"90:1","source_target_components":["90:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"90:10","source_target_components":["90:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:10","target_evidence":{"arabic_uthmani":"وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ","ayah_ref":"90:10"},"target_ref":"90:10"},{"connection_evidence_ref":"conn_ev_4b37469522a547fc2a3f","connection_ref":"conn_a59416db9417f7e8d726","note":"Same-surah human hardship is central to the focal readings of burden and responsibility.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_b51e8b559bdd5771f24d","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"90:4","source_note":"The oath setting does not add to understanding 90:4.","source_row_role":"ranked_review","source_target_component_ref":"90:1","source_target_components":["90:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"90:4","source_target_components":["90:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:4","target_evidence":{"arabic_uthmani":"لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِى كَبَدٍ","ayah_ref":"90:4"},"target_ref":"90:4"},{"connection_evidence_ref":"conn_ev_d53c3b8a28ca741f00e0","connection_ref":"conn_74eaeb63e92bf8fe8bf3","note":"Same-surah bodily endowment supports the human dimension of the focal readings.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_7c9fd245572d3c3b40c4","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"90:8","source_note":"Opening 90 channels supply broad setting, not an eye reading.","source_row_role":"ranked_review","source_target_component_ref":"90:1","source_target_components":["90:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"90:8","source_target_components":["90:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:8","target_evidence":{"arabic_uthmani":"أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ","ayah_ref":"90:8"},"target_ref":"90:8"},{"connection_evidence_ref":"conn_ev_9cbae84f6ea173d4231e","connection_ref":"conn_f170411b3ab15f0f7dbc","note":"Immediate continuation of the focal oath sequence; adds the generational human relation beside the city.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"90:3","source_target_components":["90:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:3","target_evidence":{"arabic_uthmani":"وَوَالِدٍۢ وَمَا وَلَدَ","ayah_ref":"90:3"},"target_ref":"90:3"}],"focus":{"arabic_uthmani":"لَآ أُقْسِمُ بِهَٰذَا ٱلْبَلَدِ","qac_morphemes":[{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"90:1:1:1","qac_word_ref":"90:1:1","root_ar":"","surface_ar":"لَآ"},{"lemma_ar":"أَقْسَمُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aqosamu|ROOT:qsm|1S","morpheme_role":"STEM","pos":"V","qac_ref":"90:1:2:1","qac_word_ref":"90:1:2","root_ar":"ق س م","surface_ar":"أُقْسِمُ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"90:1:3:1","qac_word_ref":"90:1:3","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"هَٰذَا","morph_features":"STEM|POS:DEM|LEM:ha`*aA|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"90:1:3:2","qac_word_ref":"90:1:3","root_ar":"","surface_ar":"هَٰذَا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"90:1:4:1","qac_word_ref":"90:1:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:1:4:2","qac_word_ref":"90:1:4","root_ar":"ب ل د","surface_ar":"بَلَدِ"}],"word_analysis_qac_refs":[["90:1:1:1"],["90:1:2:1"],["90:1:3:1"],["90:1:3:2"],["90:1:4:1","90:1:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["90:1:1","90:1:2","90:1:3","90:1:4","90:1:5"]},"focus_surface_evidence":{"arabic_uthmani":"لَآ أُقْسِمُ بِهَٰذَا ٱلْبَلَدِ","qac_morphemes":[{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"90:1:1:1","qac_word_ref":"90:1:1","root_ar":"","surface_ar":"لَآ"},{"lemma_ar":"أَقْسَمُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aqosamu|ROOT:qsm|1S","morpheme_role":"STEM","pos":"V","qac_ref":"90:1:2:1","qac_word_ref":"90:1:2","root_ar":"ق س م","surface_ar":"أُقْسِمُ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"90:1:3:1","qac_word_ref":"90:1:3","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"هَٰذَا","morph_features":"STEM|POS:DEM|LEM:ha`*aA|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"90:1:3:2","qac_word_ref":"90:1:3","root_ar":"","surface_ar":"هَٰذَا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"90:1:4:1","qac_word_ref":"90:1:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:1:4:2","qac_word_ref":"90:1:4","root_ar":"ب ل د","surface_ar":"بَلَدِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["90:1:1:1"],["90:1:2:1"],["90:1:3:1"],["90:1:3:2"],["90:1:4:1","90:1:4:2"]],"word_analysis_refs":["90:1:1","90:1:2","90:1:3","90:1:4","90:1:5"],"word_rows":[{"analysis_record_ref":"90:1:1","analytic_gloss_range_en":"negation-shaped oath opener; it withholds, rebuts, and heightens the oath rather than functioning as a flat denial alone","analytic_root_gloss_range_en":null,"qac_refs":["90:1:1:1"],"root":{},"surface":{"arabic":"لَآ","transliteration":"lā"}},{"analysis_record_ref":"90:1:2","analytic_gloss_range_en":"Form IV first-person imperfect oath verb performing a sworn assertion through a following bi-phrase; partition and apportionment pressure remains secondary","analytic_root_gloss_range_en":"root range includes oath-taking, dividing, apportioning, allotment, and other specialized branches; the local Form IV oath frame selects solemn assertion while preserving boundary-making pressure","qac_refs":["90:1:2:1"],"root":{"arabic":"ق س م","transliteration":"q-s-m"},"surface":{"arabic":"أُقْسِمُ","transliteration":"ʾuqsimu"}},{"analysis_record_ref":"90:1:3","analytic_gloss_range_en":"prefixed oath preposition governing the demonstrative phrase; broader attachment force survives under oath scope","analytic_root_gloss_range_en":null,"qac_refs":["90:1:3:1"],"root":{},"surface":{"arabic":"بِ","transliteration":"bi"}},{"analysis_record_ref":"90:1:4","analytic_gloss_range_en":"proximal masculine singular demonstrative governed by the oath preposition and specified by the following city noun","analytic_root_gloss_range_en":null,"qac_refs":["90:1:3:2"],"root":{},"surface":{"arabic":"هَٰذَا","transliteration":"hādhā"}},{"analysis_record_ref":"90:1:5","analytic_gloss_range_en":"the known city as a bounded inhabited place, appositional to the demonstrative and functioning as the sworn-by witness; security remains intertextual pressure, not an explicit adjective here","analytic_root_gloss_range_en":"root range includes bounded land, city, settlement, residence, exposed place, and several non-place branches such as dullness, body marks, sky-place, combat, and nesting-place; the local concrete noun selects the inhabited place branch","qac_refs":["90:1:4:1","90:1:4:2"],"root":{"arabic":"ب ل د","transliteration":"b-l-d"},"surface":{"arabic":"ٱلْبَلَدِ","transliteration":"al-balad"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":6,"missing_anchor_refs":[],"supplied_unique_anchor_count":6},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["90:1","90:2"],"branch_refs":["root_000148/B001","root_000351/B001","root_000351/B002","root_000351/B003","root_000351/B005","root_001226/B004"],"candidate_id":"cand_c68d843c1c65d54b69b7","evidence_scope":"declared_pericope","hft_ref":"hft_7c5d261d246695f0cef4","item_id":"d_oath_boundary_unbound","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_oath_boundary_unbound","support_id":"sup_bd1e762a3efedbfb8e99"},{"anchor_refs":["90:1","90:3"],"branch_refs":["root_000148/B001","root_001226/B003","root_001683/B003","root_001683/B005"],"candidate_id":"cand_5f655045bc1def917c73","evidence_scope":"declared_pericope","hft_ref":"hft_d14567cf78cde7282ade","item_id":"d_generational_city_allotment","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_generational_city_allotment","support_id":"sup_41535c4caf8fdf90a0b4"},{"anchor_refs":["90:1","90:5","90:6","90:7"],"branch_refs":["root_000148/B001","root_000318/B001","root_000531/B001","root_001205/B001","root_001226/B003","root_001226/B004","root_001272/B001","root_001340/B002","root_001457/B001","root_001596/B009"],"candidate_id":"cand_9438f41b241fdc6c7539","evidence_scope":"declared_pericope","hft_ref":"hft_a185e39047a46a55a953","item_id":"d_oath_as_public_account","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_oath_as_public_account","support_id":"sup_54154efd8595ba64b78d"},{"anchor_refs":["90:1","90:6"],"branch_refs":["root_000148/B001","root_001226/B003","root_001251/B001","root_001340/B002","root_001457/B001"],"candidate_id":"cand_b610bfdccb8389cabf39","evidence_scope":"declared_pericope","hft_ref":"hft_0c49882a40e7f8ccb64d","item_id":"o_piled_boast_shrunk_by_split_root","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_piled_boast_shrunk_by_split_root","support_id":"sup_2845fd15b54a3d723e25"}],"diagnostics":[],"lane_counts":{"global":16,"macro":4,"micro":4},"packet_summary":{"ayah_count":20,"focus_ref":"90:1","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ح ل ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000351","furuq_root_norm":"ح ل ل","furuq_source_root_norm":"ح ل ل","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000353","furuq_root_norm":"ح ل ي","furuq_source_root_norm":"ح ل ي","is_dominant":false,"target_occurrences":6,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"90:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"90:1","lane":"macro","linguistic_source_ref":"90:1","surface_ref":"90:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"90:1","target_tokens":[["Hayır",["90:1:1"]],["bu",["90:1:3"]],["şehre",["90:1:3","90:1:4"]],["yemin",["90:1:2"]],["ederim",["90:1:2"]]],"text":"Hayır, bu şehre yemin ederim."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":10,"id":"s090-p01-001-010","label":"Human toil and the two paths","number":1,"refs":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"90:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"90:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["90:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"90:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Brow, Facial Beauty, and Wide Eyes","source_type":"channel","support_id":"sup_3e5d02509d23ad94c770","text":"Beauty is read through intervals and proportions: the clear brow frames the face, the eyes widen its expression, and the mirror makes the whole arrangement available for appraisal.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Brow, Facial Beauty, and Wide Eyes","source_type":"channel","support_id":"sup_47f713c41503ca9954ce","text":"90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:1 `أُقْسِمُ` (ق س م); 90:8 `عَيْنَيْنِ` (ع ي ن); 90:7 `يَرَهُ` (ر ء ي)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"E:Planning, Opinion, and Deliberation","source_type":"channel","support_id":"sup_484c4cdd42172ec56cbb","text":"Deliberation moves from uncertainty toward commitment. Experience, perception, and inner speech supply possible courses, divided attention compares them, and planning converts judgment into a prepared intention.","trust":"trusted"},{"branch_refs":["root_000318/B002","root_000318/B006","root_000531/B002","root_001205/B005","root_001226/B006","root_001272/B011","root_001272/B012","root_001473/B010"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"E:Planning, Opinion, and Deliberation","source_type":"channel","support_id":"sup_4b7cbb824ef2374ff790","text":"uncertain supposition `ح س ب:B002/m01`; saying construed as supposition `ق و ل:B011/m01`; experience acquired through time `ن ج د:B010/m01`; reflective planning `ق د ر:B005/m01`; divided attention among alternatives `ق س م:B006/m01`; reasoned opinion `ر ء ي:B002/m01`; practical oversight `ح س ب:B006/m01`; inner unspoken thought `ق و ل:B012/m01`","trust":"trusted"},{"branch_refs":["root_000148/B003","root_000531/B006","root_001069/B016","root_001226/B001"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Brow, Facial Beauty, and Wide Eyes","source_type":"channel","support_id":"sup_59c023bb0995d074fe6f","text":"clear space between the brows `ب ل د:B003/m01`; distributed facial beauty `ق س م:B001/m01`; wide and beautiful eyes `ع ي ن:B016/m01`; pleasing mirror appearance `ر ء ي:B006/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Sword, Stick, and Close Combat","source_type":"channel","support_id":"sup_6bc2d69f5ccc6e1de1ec","text":"Conflict exposes agents to danger, organized violence, hostility, restraint, and answering punishment.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"E:Planning, Opinion, and Deliberation","source_type":"channel","support_id":"sup_a954d4d10fb2ccc6554b","text":"Action depends on counting, delimiting, possessing power, enduring constraint, and choosing after reflection.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Sword, Stick, and Close Combat","source_type":"channel","support_id":"sup_ae67ec1c3ab2b02c0236","text":"90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:10 `ٱلنَّجْدَيْنِ` (ن ج د); 90:6 `يَقُولُ` (ق و ل); 90:4 `كَبَدٍ` (ك ب د)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Sword, Stick, and Close Combat","source_type":"channel","support_id":"sup_b9c95f2b9d66f3d762ba","text":"Opponents close distance and strike with swords, sticks, or a club-like implement.","trust":"trusted"},{"branch_refs":["root_000148/B011","root_001272/B008","root_001280/B004","root_001473/B003"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"B:Sword, Stick, and Close Combat","source_type":"channel","support_id":"sup_ded257294b490fcdcd06","text":"dueling with swords and sticks `ب ل د:B011/m01`; courage and aid in combat `ن ج د:B003/m01`; striking-stick or bat `ق و ل:B008/m01`; hard central grip `ك ب د:B004/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Sword, Stick, and Close Combat","source_type":"channel","support_id":"sup_ec4166c3914d21cd1e5d","text":"The combat scene combines bodily courage, held implement, and sustained proximity. The grip mediates force from the fighter into sword, stick, or club.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"E:Planning, Opinion, and Deliberation","source_type":"channel","support_id":"sup_eccf061b44e3212c1080","text":"90:5, 90:7 `أَيَحْسَبُ` (ح س ب); 90:6 `يَقُولُ` (ق و ل); 90:10 `ٱلنَّجْدَيْنِ` (ن ج د); 90:5 `يَقْدِرَ` (ق د ر); 90:1 `أُقْسِمُ` (ق س م); 90:7 `يَرَهُ` (ر ء ي)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Brow, Facial Beauty, and Wide Eyes","source_type":"channel","support_id":"sup_f2f5d9adb0e8ddb4c404","text":"Facial openness, proportion, and eye shape produce a recognizable ideal of beauty.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Brow, Facial Beauty, and Wide Eyes","source_type":"channel","support_id":"sup_f5073b77f4e8bb1e112f","text":"Bodies and objects become socially legible through proportion, color, trace, and adornment.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"E:Planning, Opinion, and Deliberation","source_type":"channel","support_id":"sup_f85fa1b54247257f67bb","text":"A person moves from uncertain supposition through gathered experience and comparison toward a formed intention.","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"لَآ أُقْسِمُ بِهَٰذَا ٱلْبَلَدِ","ayah_ref":"90:1"},{"arabic_uthmani":"وَأَنتَ حِلٌّۢ بِهَٰذَا ٱلْبَلَدِ","ayah_ref":"90:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000148/B001","root_000351/B001","root_000351/B002","root_000351/B003","root_000351/B005","root_001226/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001226","role":"Supplies the oath as a binding performative whose force can be tested by the following release images.","root":"ق س م","source_ref":"90:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000148","role":"Supplies the original bounded tract against which occupation and loosening become spatially consequential.","root":"ب ل د","source_ref":"90:1","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000351","role":"Supplies the literal untying of a knot and recasts the oath-place relation as something that can be loosened.","root":"ح ل ل","source_ref":"90:2","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000351","role":"Supplies settling in a place and makes the addressee's presence inside the boundary operational.","root":"ح ل ل","source_ref":"90:2","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000351","role":"Supplies dissolution of a prohibition and gives the repeated city a changing legal status.","root":"ح ل ل","source_ref":"90:2","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_000351","role":"Supplies release or discharge from an oath and directly feeds back upon the opening oath mechanism.","root":"ح ل ل","source_ref":"90:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000148","role":"Repeats the same bounded tract and holds the spatial referent steady while its relation to the addressee changes.","root":"ب ل د","source_ref":"90:2","source_word_indices":["4"]}],"changed_reading":{"after":"The oath stands at a legal-spatial threshold: this city binds and is also being unbound in relation to the addressee, so the initial negation may register suspension or reversal as well as emphasis.","before":"The speaker simply swears by a stable city."},"confidence":"medium","mechanism":"The immediate repetition of the same city introduces images of untying, occupying, lifted prohibition, and release from an oath. The opening oath and the city's boundary now behave like a reversible bind: the addressee's presence can inhabit, loosen, or alter the force of the bounded jurisdiction.","model_id":"d_oath_boundary_unbound","reader_inference":"The packet supplies oath, bounded place, untying, occupancy, lifted prohibition, and oath-release; I infer that the addressee's presence makes the boundary a reversible bind. A live alternative is that the second ayah merely predicates a status and does not act back on the opening oath.","status":"revised","structural_cues":["90:2 immediately repeats the deictic city, preserving the same spatial object while inserting the addressed person's status within it.","The sequence moves from an oath by the boundary to a second-person relation inside that boundary."],"trigger_roots":["ح ل ل","ب ل د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_oath_boundary_unbound","source_type":"hft","support_id":"sup_bd1e762a3efedbfb8e99","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَآ أُقْسِمُ بِهَٰذَا ٱلْبَلَدِ","ayah_ref":"90:1"},{"arabic_uthmani":"وَوَالِدٍۢ وَمَا وَلَدَ","ayah_ref":"90:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000148/B001","root_001226/B003","root_001683/B003","root_001683/B005"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001226","role":"Supplies shares and allotment and lets generation distribute place and obligation through time.","root":"ق س م","source_ref":"90:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000148","role":"Supplies the bounded territorial container within which generational succession can be imagined.","root":"ب ل د","source_ref":"90:1","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_001683","role":"Supplies the event of birth and changes the place from static boundary into a site of temporal emergence.","root":"و ل د","source_ref":"90:3","source_word_indices":["1","3"]},{"branch_id":"B005","mapped_root_id":"root_001683","role":"Supplies something produced from something else and makes civic inheritance a generative chain rather than mere occupancy.","root":"و ل د","source_ref":"90:3","source_word_indices":["1","3"]}],"changed_reading":{"after":"The city also becomes an inherited allotment that generates and receives successive lives, making the oath temporally civic rather than only geographic.","before":"The city is a fixed location honored in the present."},"confidence":"medium","mechanism":"The move from repeated place to parent and offspring makes the bounded allotment temporally productive. The city can be read not only as inherited ground but as a generator of successive inhabitants, claims, and consequences.","model_id":"d_generational_city_allotment","reader_inference":"The packet supplies a bounded allotment and a parent-product sequence; I infer that place mediates intergenerational shares and consequences. The live alternative is simple coordination of separate oath objects with no causal role for the city.","status":"new","structural_cues":["The context moves from place in 90:1-2 to paired begetter and begotten in 90:3.","The root occurs twice in one compact relation, foregrounding succession rather than an isolated individual."],"trigger_roots":["و ل د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_generational_city_allotment","source_type":"hft","support_id":"sup_41535c4caf8fdf90a0b4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَآ أُقْسِمُ بِهَٰذَا ٱلْبَلَدِ","ayah_ref":"90:1"},{"arabic_uthmani":"أَيَحْسَبُ أَن لَّن يَقْدِرَ عَلَيْهِ أَحَدٌۭ","ayah_ref":"90:5"},{"arabic_uthmani":"يَقُولُ أَهْلَكْتُ مَالًۭا لُّبَدًا","ayah_ref":"90:6"},{"arabic_uthmani":"أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ","ayah_ref":"90:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000148/B001","root_000318/B001","root_000531/B001","root_001205/B001","root_001226/B003","root_001226/B004","root_001272/B001","root_001340/B002","root_001457/B001","root_001596/B009"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001226","role":"Supplies the oath's legal and testimonial frame and opens the later claim to adjudication.","root":"ق س م","source_ref":"90:1","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001226","role":"Supplies apportioned shares and makes the claimed wealth susceptible to distributional accounting.","root":"ق س م","source_ref":"90:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000148","role":"Supplies a bounded jurisdiction within which account, power, and witness can converge.","root":"ب ل د","source_ref":"90:1","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000318","role":"Supplies counting and reckoning and turns the interrogative thought into an audit operation.","root":"ح س ب","source_ref":"90:5","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001205","role":"Supplies a measure reaching its limit and gives the audit a scale against which claims are bounded.","root":"ق د ر","source_ref":"90:5","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001272","role":"Supplies an uttered statement and identifies the wealth expenditure as a claim rather than self-validating fact.","root":"ق و ل","source_ref":"90:6","source_word_indices":["1"]},{"branch_id":"B009","mapped_root_id":"root_001596","role":"Supplies exhaustion or consumption of effort and sharpens what the speaker alleges was spent.","root":"ه ل ك","source_ref":"90:6","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Supplies acquisition and abundance of wealth and provides the audit's material object.","root":"م و ل","source_ref":"90:6","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001340","role":"Supplies accumulated layers or masses and gives the boast its asserted magnitude.","root":"ل ب د","source_ref":"90:6","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000531","role":"Supplies sight by eye and insight and closes the account under an observing witness.","root":"ر ء ي","source_ref":"90:7","source_word_indices":["4"]}],"changed_reading":{"after":"The oath opens a civic court of account: within this boundary, asserted expenditure is counted, limited, and seen rather than accepted at the scale claimed.","before":"The city is honored before an unrelated rebuke of human arrogance."},"confidence":"strong","mechanism":"The legal oath and latent apportionment of the focus are followed by counting, limit or power, a spoken expenditure claim, wealth piled in layers, and seeing. The city becomes a jurisdiction of public account in which boasts about consumed resources are measured against power and witness.","model_id":"d_oath_as_public_account","reader_inference":"The packet supplies legal oath, apportioned shares, calculation, measure, speech, consumed effort, piled wealth, and sight; I infer a public accounting sequence located by the city. A live alternative is a universal moral interrogation with no specifically civic or forensic mechanism.","status":"revised","structural_cues":["The repeated interrogative about what the person supposes brackets the expenditure boast in 90:5-7.","The first question concerns reach or power, the middle gives a monetary claim, and the second concerns being seen."],"trigger_roots":["ح س ب","ق د ر","ق و ل","ه ل ك","م و ل","ل ب د","ر ء ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_oath_as_public_account","source_type":"hft","support_id":"sup_54154efd8595ba64b78d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَآ أُقْسِمُ بِهَٰذَا ٱلْبَلَدِ","ayah_ref":"90:1"},{"arabic_uthmani":"يَقُولُ أَهْلَكْتُ مَالًۭا لُّبَدًا","ayah_ref":"90:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000148/B001","root_001226/B003","root_001251/B001","root_001340/B002","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001226","role":"Supplies apportioned shares and gives the later boast a measure rather than accepting its scale.","root":"ق س م","source_ref":"90:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000148","role":"Supplies a bounded field and contains the boast within a finite jurisdiction.","root":"ب ل د","source_ref":"90:1","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001251","role":"Supplies smallness from the non-dominant mapped root and reverses the asserted magnitude of the spoken claim.","root":"ق و ل","source_ref":"90:6","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Supplies abundant acquired wealth and establishes the scale that the counterimage contests.","root":"م و ل","source_ref":"90:6","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001340","role":"Supplies piled mass and intensifies the abundance whose rhetorical size is being shrunk.","root":"ل ب د","source_ref":"90:6","source_word_indices":["4"]}],"changed_reading":{"after":"The oath's scale can expose a reversal: what speech piles up as vast is bounded, apportioned, and branch-wise reduced to a small claim under examination.","before":"The oath precedes a straightforward boast about a very large expenditure."},"confidence":"exploratory","containment":"This outlier deliberately uses the packet's non-dominant mapping of the speech root to an image of smallness. It is valid as a scale-reversing activation anchored to the focus's apportionment and bounded-place mechanism, but it is not a claim that the contextual verb lexically means 'to be little'; downstream prose should label the reversal as a split-root counterimage.","focus_anchor":"The opening root can apportion and measure shares within the bounded city, giving later claims a scale on which they can be enlarged or diminished.","outlier_id":"o_piled_boast_shrunk_by_split_root"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_piled_boast_shrunk_by_split_root","source_type":"hft","support_id":"sup_2845fd15b54a3d723e25","trust":"legacy_unbound"}]}
</lane_packet_json>
