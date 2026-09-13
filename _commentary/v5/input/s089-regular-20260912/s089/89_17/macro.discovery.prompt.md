# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **89:17**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_17/macro.discovery.json` and modify nothing
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
  "ayah_ref": "89:17",
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
{"branch_registry":[{"boundary":"Mumbling or speaking without clear articulation.","branch_kind":null,"branch_ref":"root_000261/B008","candidate_links":[{"candidate_id":"cand_726f3769562d8304973d","lane":"macro"}],"focus_root_occurrences":[],"gloss":"muffled unclear speech","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"جمجمة الكلام بلا بيان","image_en":"muffled unclear speech"}}],"root_ar":"ج م م","root_id":"root_000261","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"جمجمة الكلام بلا بيان","image_en":"muffled unclear speech","scope_ar":"يدخل فيه جمجم الرجل أو تجمجم إذا لم يبين كلامه.","scope_en":"Mumbling or speaking without clear articulation."},"support_links":["sup_3a8c325854a67d00b3a8"]},{"boundary":"Includes plant growth that becomes tall, thick, intertwined, flowering, or abundant, and tall palms.","branch_kind":null,"branch_ref":"root_000266/B011","candidate_links":[{"candidate_id":"cand_ecaca707605984f08a4c","lane":"macro"}],"focus_root_occurrences":[],"gloss":"thick or vigorous growth","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"التفاف النبات واندفاعه","image_en":"thick or vigorous growth"}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"التفاف النبات واندفاعه","image_en":"thick or vigorous growth","scope_ar":"يدخل فيه النبات إذا اشتد أو طال أو التف أو خرج زهره والنخل الطويل والأرض الكثيرة العشب","scope_en":"Includes plant growth that becomes tall, thick, intertwined, flowering, or abundant, and tall palms."},"support_links":["sup_64f16d37122b142060d7"]},{"boundary":"This branch covers formulaic approval, commendation, and idioms of utmost desire.","branch_kind":null,"branch_ref":"root_000286/B003","candidate_links":[{"candidate_id":"cand_21cd8c1582ef56c05f3e","lane":"macro"}],"focus_root_occurrences":[],"gloss":"formula of approval and utmost desire","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"صيغة المدح وغاية الرغبة","image_en":"formula of approval and utmost desire"}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"صيغة المدح وغاية الرغبة","image_en":"formula of approval and utmost desire","scope_ar":"يدخل فيه حبذا، وحبابك أن تفعل، ونعم وحبة وكرامة، وما جاء بصيغة مدح أو بلوغ الغاية في المحبة.","scope_en":"This branch covers formulaic approval, commendation, and idioms of utmost desire."},"support_links":["sup_f592d95e95bfe57ac9ff"]},{"boundary":"The branch covers urging, inciting, exhorting, and mutual exhortation toward good, fighting, or feeding the needy.","branch_kind":null,"branch_ref":"root_000334/B001","candidate_links":[{"candidate_id":"cand_95f55e75ff4283b2cf84","lane":"macro"},{"candidate_id":"cand_cf949783b5773986924a","lane":"macro"}],"focus_root_occurrences":[],"gloss":"urging toward a thing","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الحَضّ على الشيء","image_en":"urging toward a thing"}}],"root_ar":"ح ض ض","root_id":"root_000334","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الحَضّ على الشيء","image_en":"urging toward a thing","scope_ar":"الحث والتحريض والحض المتبادل على الخير أو القتال أو طعام المسكين","scope_en":"The branch covers urging, inciting, exhorting, and mutual exhortation toward good, fighting, or feeding the needy."},"support_links":["sup_77e721a081c56d7de638","sup_cf9234255be709a3c2a1"]},{"boundary":"Includes the idiom \"entered upon/with his wife\" as a euphemism for consummation.","branch_kind":null,"branch_ref":"root_000464/B002","candidate_links":[{"candidate_id":"cand_52fa281701419a01271b","lane":"macro"}],"focus_root_occurrences":[],"gloss":"consummating marriage","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الإفضاء الزوجي","image_en":"consummating marriage"}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الإفضاء الزوجي","image_en":"consummating marriage","scope_ar":"يدخل فيه قولهم دخل بامرأته كناية عن الإفضاء إليها.","scope_en":"Includes the idiom \"entered upon/with his wife\" as a euphemism for consummation."},"support_links":["sup_c90e2bc134658840580d"]},{"boundary":"Includes the noun for the small bird so called for entering thickets, caves, or dense trees.","branch_kind":null,"branch_ref":"root_000464/B009","candidate_links":[{"candidate_id":"cand_ecaca707605984f08a4c","lane":"macro"}],"focus_root_occurrences":[],"gloss":"a small bird of thickets","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"طائر يدخل الغيران والشجر","image_en":"a small bird of thickets"}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"طائر يدخل الغيران والشجر","image_en":"a small bird of thickets","scope_ar":"يدخل فيه الدخل اسم الطائر الصغير، وجمعه دخاخيل أو دخاليل، مع تعليل دخوله بين الأشجار الملتفة.","scope_en":"Includes the noun for the small bird so called for entering thickets, caves, or dense trees."},"support_links":["sup_64f16d37122b142060d7"]},{"boundary":"This includes verbal mention, utterance, making known, naming, and speaking of people well or badly when the wording indicates it.","branch_kind":null,"branch_ref":"root_000516/B004","candidate_links":[{"candidate_id":"cand_726f3769562d8304973d","lane":"macro"}],"focus_root_occurrences":[],"gloss":"mention on the tongue","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"جريان الذكر على اللسان","image_en":"mention on the tongue"}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"جريان الذكر على اللسان","image_en":"mention on the tongue","scope_ar":"يدخل فيه ذكر الشيء باللسان والقول والإظهار والتسمية، ومنه ذكر الناس بخير أو بسوء إذا دل السياق.","scope_en":"This includes verbal mention, utterance, making known, naming, and speaking of people well or badly when the wording indicates it."},"support_links":["sup_3a8c325854a67d00b3a8"]},{"boundary":"This includes honor, elevation, reputation, praise, and being well spoken of.","branch_kind":null,"branch_ref":"root_000516/B007","candidate_links":[{"candidate_id":"cand_21cd8c1582ef56c05f3e","lane":"macro"}],"focus_root_occurrences":[],"gloss":"honorable mention and renown","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"ذكر المرء شرف وصيت","image_en":"honorable mention and renown"}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"ذكر المرء شرف وصيت","image_en":"honorable mention and renown","scope_ar":"يدخل فيه الشرف والعلاء والصيت والثناء وحسن الذكر.","scope_en":"This includes honor, elevation, reputation, praise, and being well spoken of."},"support_links":["sup_f592d95e95bfe57ac9ff"]},{"boundary":"This covers marital reinstatement after divorce and a woman returning to her family.","branch_kind":null,"branch_ref":"root_000544/B004","candidate_links":[{"candidate_id":"cand_52fa281701419a01271b","lane":"macro"}],"focus_root_occurrences":[],"gloss":"Domestic or marital return","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"رجعة المرأة في النكاح والأهل","image_en":"Domestic or marital return"}}],"root_ar":"ر ج ع","root_id":"root_000544","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"رجعة المرأة في النكاح والأهل","image_en":"Domestic or marital return","scope_ar":"يدخل فيه مراجعة الزوج امرأته ورجعة الطلاق ورجوع المرأة إلى أهلها بعد موت زوجها أو طلاقها.","scope_en":"This covers marital reinstatement after divorce and a woman returning to her family."},"support_links":["sup_c90e2bc134658840580d"]},{"boundary":"This covers birds returning after seasonal departure or migration.","branch_kind":null,"branch_ref":"root_000544/B012","candidate_links":[{"candidate_id":"cand_ecaca707605984f08a4c","lane":"macro"}],"focus_root_occurrences":[],"gloss":"Birds returning after seasonal departure","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"رجوع الطير بعد القطاع","image_en":"Birds returning after seasonal departure"}}],"root_ar":"ر ج ع","root_id":"root_000544","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"رجوع الطير بعد القطاع","image_en":"Birds returning after seasonal departure","scope_ar":"يدخل فيه الرجاع المختص برجوع الطير بعد قطاعها من مواضع إلى مواضع.","scope_en":"This covers birds returning after seasonal departure or migration."},"support_links":["sup_64f16d37122b142060d7"]},{"boundary":"poverty, need, weakness, humility, abasement, and submission","branch_kind":null,"branch_ref":"root_000726/B006","candidate_links":[{"candidate_id":"cand_95f55e75ff4283b2cf84","lane":"macro"}],"focus_root_occurrences":[],"gloss":"poverty and humble abasement","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"ذل المسكنة","image_en":"poverty and humble abasement"}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"ذل المسكنة","image_en":"poverty and humble abasement","scope_ar":"يدخل فيه المسكين والمسكنة والفقر والذلة والضعف والخضوع والاستكانة والتمسكن","scope_en":"poverty, need, weakness, humility, abasement, and submission"},"support_links":["sup_77e721a081c56d7de638"]},{"boundary":"Includes giving food to another, asking to be fed, and feeding the needy.","branch_kind":null,"branch_ref":"root_000934/B002","candidate_links":[{"candidate_id":"cand_95f55e75ff4283b2cf84","lane":"macro"},{"candidate_id":"cand_cf949783b5773986924a","lane":"macro"}],"focus_root_occurrences":[],"gloss":"Feeding and asking for food","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"إطعام الغير وطلب الطعام","image_en":"Feeding and asking for food"}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"إطعام الغير وطلب الطعام","image_en":"Feeding and asking for food","scope_ar":"يدخل فيه أطعمته الطعام واستطعمه أي سأله أن يطعمه وإطعام المحتاج","scope_en":"Includes giving food to another, asking to be fed, and feeding the needy."},"support_links":["sup_77e721a081c56d7de638","sup_cf9234255be709a3c2a1"]},{"boundary":"Includes saying, utterance, qawl/qil, and articulated speech made of letters, whether word, sentence, poem, or sermon.","branch_kind":null,"branch_ref":"root_001272/B001","candidate_links":[{"candidate_id":"cand_726f3769562d8304973d","lane":"macro"}],"focus_root_occurrences":[],"gloss":"uttered speech","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"إخراج القول بالنطق","image_en":"uttered speech"}}],"root_ar":"ق و ل","root_id":"root_001272","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"إخراج القول بالنطق","image_en":"uttered speech","scope_ar":"يدخل فيه قال يقول قولا، والقول والقيل، والكلام المركب من الحروف إذا أبرز بالنطق، مفردا كان أو جملة أو قصيدة أو خطبة.","scope_en":"Includes saying, utterance, qawl/qil, and articulated speech made of letters, whether word, sentence, poem, or sermon."},"support_links":["sup_3a8c325854a67d00b3a8"]},{"boundary":"Includes al-maqul as the tongue.","branch_kind":null,"branch_ref":"root_001272/B002","candidate_links":[{"candidate_id":"cand_726f3769562d8304973d","lane":"macro"}],"focus_root_occurrences":[],"gloss":"tongue as the instrument of speech","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"اللسان آلة القول","image_en":"tongue as the instrument of speech"}}],"root_ar":"ق و ل","root_id":"root_001272","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"اللسان آلة القول","image_en":"tongue as the instrument of speech","scope_ar":"يدخل فيه المقول بمعنى اللسان.","scope_en":"Includes al-maqul as the tongue."},"support_links":["sup_3a8c325854a67d00b3a8"]},{"boundary":"Dal, kolye, üzüm, kap kapağı ve kalça kemiği gibi aynı kökten gelen bağımsız nesne adlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001294/B001","candidate_links":[{"candidate_id":"cand_95f55e75ff4283b2cf84","lane":"macro"},{"candidate_id":"cand_cd967dac22d4e075b109","lane":"macro"},{"candidate_id":"cand_cf949783b5773986924a","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَكْرَمَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>akorama|ROOT:krm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:17:4:1","qac_word_ref":"89:17:4","surface_ar":"تُكْرِمُ"}],"gloss":"övgüye değer soyluluk, eli açıklık ve onurlandırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, davranış veya şey kendi alanında üstün ve övgüye değer sayılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsandaki çekirdek görünüm eli açıklık, bol iyilik, bağışlayıcılık ve güzel huydur."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başkasını onurlandırmak veya ona incitmeden değerli bir yarar sağlamak bu niteliğin eylemsel uzantısıdır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişinin kendisini ayıp ve utanç verici işlerden uzak tutması, kendi değerini koruyan bir tutum olarak anlatılır."}},{"facet_id":"F005","role":"example","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Övgüye değer çocuklar dünyaya getirmek veya değerli bir bağ ya da varlık edinmek bu geniş niteliğin özel örnekleridir."}}],"root_ar":"ك ر م","root_id":"root_001294","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın nitelik, davranış ve başkasına değer verme boyutlarını birlikte anlatan genel kavram karşılığıdır.","boundary_detail":"Dal, kolye, üzüm, kap kapağı ve kalça kemiği gibi aynı kökten gelen bağımsız nesne adlarını kapsamaz.","branch_image_ar":"الشرف والجود المحمود","concept_gloss":"övgüye değer soyluluk, eli açıklık ve onurlandırma","contextual_glosses":[{"applicability":"Bir kişinin huyunu, davranışını veya toplumsal değerini anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsana ilişkin övgüye değer üstünlük ve cömert davranış çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"soyluluk ve eli açıklık","usage_role":"general"},{"applicability":"Bir kişiye saygınlık kazandırma veya onu incitmeden değerli bir yarara ulaştırma eyleminde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başkasına yönelen onurlandırma ve değerli yarar sağlama işlemini korur."},"facet_ids":["F003"],"text":"onurlandırmak ve değerli kılmak","usage_role":"contextual"},{"applicability":"Kişinin kendi değerini koruyarak utanç verici işlerden kaçınmasını anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kendini küçültücü ve ayıplanan şeylerden uzak tutma yönünü korur."},"facet_ids":["F004"],"text":"ayıptan uzak durmak","usage_role":"contextual"}],"definition":"Bir kişide, davranışta ya da şeyde kendi alanına göre bulunan övgüye değer üstünlük; insanda eli açıklık, bağışlayıcılık ve utanç verici olandan uzak durma biçiminde belirir. Başkasını onurlandırma ve ona küçültücü olmayan değerli bir yarar ulaştırma da bu anlam alanına girer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, davranış veya şey kendi alanında üstün ve övgüye değer sayılır."},{"facet_id":"F002","role":"specialization","statement":"İnsandaki çekirdek görünüm eli açıklık, bol iyilik, bağışlayıcılık ve güzel huydur."},{"facet_id":"F003","role":"extension","statement":"Başkasını onurlandırmak veya ona incitmeden değerli bir yarar sağlamak bu niteliğin eylemsel uzantısıdır."},{"facet_id":"F004","role":"associated_use","statement":"Kişinin kendisini ayıp ve utanç verici işlerden uzak tutması, kendi değerini koruyan bir tutum olarak anlatılır."},{"facet_id":"F005","role":"example","statement":"Övgüye değer çocuklar dünyaya getirmek veya değerli bir bağ ya da varlık edinmek bu geniş niteliğin özel örnekleridir."}],"identity_rationale":"Kaynak ifadesi, dalı hem kişide veya şeyde bulunan övgüye değer üstünlük hem de eli açıklık, bağışlayıcılık, ayıptan uzak durma ve başkasını onurlandırma alanı olarak kurar. Verilen dal çerçevesi bu geniş çekirdeği doğru biçimde karşılar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"soyluluk, eli açıklık ve övgüye değer huy"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"soylu, eli açık, bağışlayıcı; kendi türünde seçkin"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"soylular; seçkin ve övgüye değer olanlar"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"onurlandırdı veya değerli kıldı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onurlandırma ve incitmeden değerli yarar sağlama"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onurlandırma; saygınlık"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ayıp ve utanç verici şeylerden uzak durdu"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"soylu ve değerli çocukları oldu"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"değerli bir bağ ya da varlık edindi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yumuşak ve saygılı söz"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"kendi alanında yararlı ve övgüye değer tür"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"içerdiği yol gösterme, açıklama, bilgi ve bilgelikle övgüye değer kitap"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"içeriği güzel, saygın ya da mühürlü yazı"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"en soylu ve en erdemli"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"güzel ve saygın giriş yeri"}],"lexicalization_note":"Tanım, genel nitelik çekirdeğini ayrı tutar; belirli söz kalıpları, eylemler ve özel kullanımlar bu çekirdeğin bağımlı gerçekleşmeleri olarak gösterilir.","neighbor_coverage_note":"Tüm aday komşular karşılaştırıldı; yalnızca genel erdem ve eli açıklık sınırını belirginleştiren iki yakın ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu, güzel bir huy ya da davranış örneğine odaklanır; odak dal ise niteliği daha geniş kurar ve eli açıklık ile başkasını onurlandırma eylemini de içine alır.","focus_only":"Odak dal, genel üstünlüğün yanında eli açıklık, bağışlayıcılık, ayıptan kaçınma ve onurlandırmayı da kapsar.","gloss":"güzel huy veya övgüye değer davranış","neighbor_only":"Komşu dal, belirli bir güzel huyu veya övgüye değer davranışı ayrı bir üstünlük ve başarı olarak adlandırır.","neighbor_ref":"root_001539/B010","relation_type":"near_synonym","shared_zone":"Her iki dal da insanın övgüye değer niteliğini veya davranışını anlatır."},{"boundary_match":"partial","distinction":"Komşu, dalın yalnızca eli açıklık bölümüne yaklaşır; odak dalın övgüye değer üstünlük ve onurlandırma kapsamının tamamının yerine geçmez.","focus_only":"Odak dal, eli açıklığın yanı sıra soyluluk, bağışlayıcılık, ayıptan uzak durma ve onurlandırma anlamlarını taşır.","gloss":"eli açıklık ve cömertlik","neighbor_only":"Komşu dalın kapsamı özellikle eli açıklık ve cömert davranışla sınırlıdır.","neighbor_ref":"root_001503/B010","relation_type":"near_synonym","shared_zone":"Her iki dal da bol verme ve iyilikte bulunma niteliğinde kesişir."}],"source_phrase_ar":"شرف في الشيء في نفسه أو شرف في خلق من الأخلاق (maqayis)؛ الكريم الصفوح (maqayis;sihah)؛ الكرم شرف الرجل (ayn)؛ تكرم عن الشائنات أي تنزه (ayn;tahdhib)؛ الكرم ضد اللؤم (sihah)؛ أتى بأولاد كرام واستحدث علقا كريما (sihah)؛ الكثير الخير الجواد المنعم المفضل (tahdhib)؛ اسم جامع لكل ما يحمد (tahdhib)؛ الأخلاق والأفعال المحمودة (mufradat)؛ كل شيء شرف في بابه (mufradat)","source_summary":"Kaynaklar, övgüye değer üstünlük ile eli açıklık ve güzel huy çekirdeğinde birleşir; bağışlama, ayıptan kaçınma ve başkasını onurlandırma bu çekirdeğin başlıca görünümleridir. Övgüye değer çocuklar sahibi olmak ile değerli bir bağ ya da varlık edinmek de kaynakta verilen özel örneklerdir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه شرف الشيء في نفسه وشرف الخلق والجود والصفح والتنزه والإكرام والتكريم والكرامة وكل محمود في بابه","what_is_not_ar":"ليس القلادة ولا العنب ولا طبق القدر ولا رأس الفخذ"},"support_links":["sup_77e721a081c56d7de638","sup_cf9234255be709a3c2a1","sup_fb77551059ebd1b78c9a"]},{"boundary":"Dal, her türlü yağmuru veya verimli toprağı adlandırmaz; bulut ve toprakla kurulan belirtilmiş yapılara bağlıdır.","branch_kind":"collocation","branch_ref":"root_001294/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْرَمَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>akorama|ROOT:krm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:17:4:1","qac_word_ref":"89:17:4","surface_ar":"تُكْرِمُ"}],"gloss":"yağmur getirme ve toprağın verimli oluşu","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bulut, yağmur getirip suyunu bolca verdiğinde bu nitelikle anlatılır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toprak, bitkisi iyi ve gür olduğunda verimli bir yer olarak aynı yapıda nitelenir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Toprağın sürülmesi, taşlardan temizlenmesi veya gübrelenmesi, bitkinin gürleşmesini sağlayan hazırlık olarak belirtilir."}}],"root_ar":"ك ر م","root_id":"root_001294","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca bulut ve hazırlanmış toprakla kurulan iki belirli kullanımın ortak açıklamasıdır.","boundary_detail":"Dal, her türlü yağmuru veya verimli toprağı adlandırmaz; bulut ve toprakla kurulan belirtilmiş yapılara bağlıdır.","branch_image_ar":"جودة النبات والغيث","concept_gloss":"yağmur getirme ve toprağın verimli oluşu","contextual_glosses":[{"applicability":"Bulutun veya göğün yağmurunu bolca bırakmasını anlatan yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bulutun yağmur getirmesi olayını eksiksiz korur."},"facet_ids":["F001"],"text":"bol yağmur getirdi","usage_role":"contextual"},{"applicability":"İşlenen, temizlenen veya gübrelenen toprağın iyi ürün vermesini anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hazırlanmış toprağın bitkisel verim kazanmasını korur."},"facet_ids":["F002","F003"],"text":"toprağı verimli, bitkisi gür oldu","usage_role":"contextual"}],"definition":"Belirli kullanımlarda bulutun bol yağmur getirmesi veya toprağın işlenip taşlardan arındırılması ya da gübrelenmesi sonucunda bitkisinin iyi ve gür olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bulut, yağmur getirip suyunu bolca verdiğinde bu nitelikle anlatılır."},{"facet_id":"F002","role":"core","statement":"Toprak, bitkisi iyi ve gür olduğunda verimli bir yer olarak aynı yapıda nitelenir."},{"facet_id":"F003","role":"specialization","statement":"Toprağın sürülmesi, taşlardan temizlenmesi veya gübrelenmesi, bitkinin gürleşmesini sağlayan hazırlık olarak belirtilir."}],"identity_rationale":"Kaynak ifadesi hem bulutun yağmur getirmesini hem de toprağın işlenip temizlenmesi veya gübrelenmesi sonucunda bitkisinin gürleşmesini içerir. Verilen çerçeve kullanılabilir, ancak anlam genel bir verimlilik adı değil, yalnızca bu belirli yapılar içindeki iki kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bulut yağmur getirdi ve suyunu bolca verdi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bitkisi gür, toprağı iyi ve taşları ayıklanmış arazi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"toprağı işlenip gübrelendikten sonra bitkisi gürleşti"}],"lexicalization_note":"Tanım yalnızca bulutun yağmur getirmesi ve işlenmiş toprağın iyi ürün vermesi yapılarıyla sınırlandırılır; bunlardan bağımsız genel bir anlam kurulmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; toprağın verimliliğiyle en doğrudan kesişen iki komşu sınır açıklığı sağladığı için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal verimli toprağı daha genel anlatır; odak dal ise belirli bulut ve toprak yapılarıyla sınırlıdır ve yağmur getirme olayını da kapsar.","focus_only":"Odak dal, bulutun yağmur getirmesini ve toprağın işleme ya da gübreleme sonrasında gürleşmesini de içerir.","gloss":"yumuşak, verimli ve iyi bitki veren toprak","neighbor_only":"Komşu dal, yumuşak ve iyi bitki veren araziyi, kök salıp çoğalan bitkiyi ve bu bitkiyle beslenen hayvanı da kapsar.","neighbor_ref":"root_000025/B002","relation_type":"near_synonym","shared_zone":"İki dal, iyi bitki veren ve verim kazanmış toprak tasvirinde kesişir."},{"boundary_match":"partial","distinction":"Komşu toprağın fiziksel kolaylığını ve düzlüğünü öne çıkarır; odak dal hazırlama sonucunu ve ayrı olarak bulutun yağmur getirmesini içerir.","focus_only":"Odak dalda yağmur getiren bulut ile işlenip temizlenen veya gübrelenen toprağın verimi birlikte yer alır.","gloss":"düz, kolay ve verimli toprak","neighbor_only":"Komşu dal, toprağın kolay, düz ve bitki yetiştirmeye elverişli oluşunu özellikle belirtir.","neighbor_ref":"root_001521/B006","relation_type":"near_synonym","shared_zone":"Her ikisi de bitkiyi iyi yetiştiren verimli araziyi anlatır."}],"source_phrase_ar":"كرم السحاب أتى بالغيث (maqayis;sihah)؛ أرض مكرمة للنبات إذا كانت جيدة النبات (maqayis;sihah)؛ إذا جاد السحاب بغيثه قيل كرم (ayn)؛ أرض مثارة منقاة من الحجارة (ayn;tahdhib)؛ البقعة الطيبة التربة العذاة المنبت بقعة مكرمة (tahdhib)؛ كرمت أرض فلان إذا دملها فزكا نبتها (tahdhib)","source_summary":"Kaynaklar, bulutun yağmur getirmesi ile iyi hazırlanmış toprağın güçlü bitki vermesini aynı yapı ailesinde birleştirir; toprak için işleme, taş ayıklama ve gübreleme ayrıntıları da verilir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه كرم السحاب إذا جاء بالغيث وكرم الأرض إذا جادت تربتها ونباتها وكثر عصف الحب","what_is_not_ar":"ليس الجود الخلقي ولا اسم العنب ولا القلادة"},"support_links":[]},{"boundary":"Dal yalnızca boyunda taşınan dizili süs nesnesidir; üzüm, asma veya başka bağımsız anlamlar buraya girmez.","branch_kind":"bare","branch_ref":"root_001294/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْرَمَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>akorama|ROOT:krm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:17:4:1","qac_word_ref":"89:17:4","surface_ar":"تُكْرِمُ"}],"gloss":"boyun kolyesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, boyna takılan bir kolyedir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnci tanelerinin dizilmesiyle yapılmış güzel bir kolye örnek olarak verilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çoğul biçim birden çok kolyeyi adlandırır."}}],"root_ar":"ك ر م","root_id":"root_001294","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Boyna takılan dizili süs nesnesinin kısa ve doğal genel karşılığıdır.","boundary_detail":"Dal yalnızca boyunda taşınan dizili süs nesnesidir; üzüm, asma veya başka bağımsız anlamlar buraya girmez.","branch_image_ar":"الكَرْم المنظوم في العنق","concept_gloss":"boyun kolyesi","contextual_glosses":[{"applicability":"Dizinin inciden yapıldığı somut örnekte doğal karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kolye türünü ve inci malzemesini korur."},"facet_ids":["F001","F002"],"text":"inci kolye","usage_role":"contextual"},{"applicability":"Birden çok boyun süsünün anlatıldığı çoğul bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kolyelerin çoğul oluşunu korur."},"facet_ids":["F003"],"text":"kolyeler","usage_role":"contextual"}],"definition":"Boyna takılan, boncuk veya inci gibi parçaların dizilmesiyle yapılabilen kolyedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, boyna takılan bir kolyedir."},{"facet_id":"F002","role":"example","statement":"İnci tanelerinin dizilmesiyle yapılmış güzel bir kolye örnek olarak verilir."},{"facet_id":"F003","role":"source_variant","statement":"Çoğul biçim birden çok kolyeyi adlandırır."}],"identity_rationale":"Kaynak ifadesi tekil biçimi boyunda taşınan kolye, çoğul biçimi de kolyeler olarak açıkça tanımlar ve inci dizisi örneği verir. Verilen dal kimliği bu nesne anlamını doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"boyna takılan kolye veya dizili süs"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kolyeler"}],"lexicalization_note":"Tanım yalın nesne adını verir ve herhangi bir özel söz dizimine ya da başka dalın anlamına dayanmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel kolye ile dar boyun kolyesi sınırlarını en açık gösteren iki yakın komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İnsan boynundaki süs kullanımında anlamlar yaklaşır; komşu dalın hayvanlara takılan işaret ve ayırt etme kapsamı odak dalda bulunmaz.","focus_only":"Odak dal, özellikle insan boynunda süs olarak taşınan kolyeyi adlandırır.","gloss":"boyna takılan süs veya ayırt edici bağ","neighbor_only":"Komşu dal, insan dışındaki canlılara takılan ve süsten başka işaretleme ya da ayırt etme görevi gören boyun bağlarını da kapsar.","neighbor_ref":"root_001249/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da boyna geçirilen kolye biçimli nesneyi kapsar."},{"boundary_match":"partial","distinction":"Komşu dal sıkılık ve boynu çepeçevre sarma koşuluyla daha dardır; odak dal genel kolye adıdır.","focus_only":"Odak dalda kolyenin boynu sıkıca çevrelemesi şart değildir ve inci gibi dizili süsler örneklenir.","gloss":"boynu sıkıca saran dar kolye","neighbor_only":"Komşu dal, boynu çepeçevre saran dar kolyeyi ve köpek tasmasını özellikle belirtir.","neighbor_ref":"root_000444/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da boyun çevresinde taşınan kolye türü nesneleri anlatır."}],"source_phrase_ar":"الكَرْم وهي القلادة (maqayis)؛ الكَرْم القلادة (ayn;sihah)؛ رأيت في عنقها كَرْما حسنا من لؤلؤ (sihah)؛ الكروم القلائد واحدها كَرْم (tahdhib)","source_summary":"Kaynaklar, anlamı boyna takılan kolye olarak ortaklaştırır; inci dizisi somut bir örnek, çoğul biçim ise kolyelerin adı olarak belirtilir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الكَرْم بمعنى القلادة والكروم بمعنى القلائد وما ينظم في العنق","what_is_not_ar":"ليس العنب ولا الكرامة التي هي طبق ولا رأس الفخذ"},"support_links":[]},{"boundary":"Dal üzüm, asma ve tek sürgün kapsamındadır; kolye anlamıyla yalnızca dizili kümelenme açıklamasında benzerlik kurulur.","branch_kind":"bare","branch_ref":"root_001294/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْرَمَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>akorama|ROOT:krm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:17:4:1","qac_word_ref":"89:17:4","surface_ar":"تُكْرِمُ"}],"gloss":"üzüm ve asma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ad, üzüm meyvesini ve üzüm veren asmayı kapsar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tekil bitki parçası kullanımında bir asma sürgününü veya tek asmayı belirtir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanelerin dallanmış bir kümede dizili oluşu ve asma ile meyvesinin değerli sayılması adlandırma gerekçeleri olarak sunulur."}}],"root_ar":"ك ر م","root_id":"root_001294","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Meyveyi, onu veren bitkiyi ve bağlama göre tek asmayı karşılayan genel ifadedir.","boundary_detail":"Dal üzüm, asma ve tek sürgün kapsamındadır; kolye anlamıyla yalnızca dizili kümelenme açıklamasında benzerlik kurulur.","branch_image_ar":"العنب والكرمة","concept_gloss":"üzüm ve asma","contextual_glosses":[{"applicability":"Sözün meyveyi veya üzüm tanelerini belirttiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dalın meyve kapsamını korur."},"facet_ids":["F001"],"text":"üzüm","usage_role":"contextual"},{"applicability":"Sözün üzüm veren bitkiyi veya tek bir asmayı belirttiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dalın üzüm veren bitki kapsamını korur."},"facet_ids":["F001","F002"],"text":"asma","usage_role":"contextual"},{"applicability":"Tek bir dal veya sürgünün özellikle belirtildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tek asma parçası anlamını korur."},"facet_ids":["F002"],"text":"asma sürgünü","usage_role":"contextual"}],"definition":"Üzüm meyvesi, bu meyveyi veren asma ve tek bir asma sürgünüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ad, üzüm meyvesini ve üzüm veren asmayı kapsar."},{"facet_id":"F002","role":"specialization","statement":"Tekil bitki parçası kullanımında bir asma sürgününü veya tek asmayı belirtir."},{"facet_id":"F003","role":"source_variant","statement":"Tanelerin dallanmış bir kümede dizili oluşu ve asma ile meyvesinin değerli sayılması adlandırma gerekçeleri olarak sunulur."}],"identity_rationale":"Kaynak ifadesi anlamı üzüm, asma ve tek asma sürgünü üzerinden açıklar; tanelerin dizili kümelenmesi ve ağacın ya da meyvenin değerli görülmesi de adlandırma açıklamalarıdır. Verilen dal bu bitki ve meyve kapsamını doğru biçimde karşılar.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"üzüm, asma veya asmanın meyvesi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"tek asma sürgünü veya bir asma"}],"lexicalization_note":"Tanım yalın üzüm ve asma adını korur; özel bir söz kalıbından türetilmiş daha geniş bir anlam eklemez.","neighbor_coverage_note":"Tüm komşu adayları değerlendirildi; üzümle doğrudan örtüşen dal ve genel meyve dalı en yararlı iki sınırı sağladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Meyve ve asma alanında büyük ölçüde örtüşürler; komşunun dilbilgisel türevleri ile çok üzümü olan kişi kapsamı odak dalda yoktur.","focus_only":"Odak dal, üzümün yanında asmayı ve tek asma sürgününü açıkça kapsar.","gloss":"üzüm ve üzümle ilgili adlandırmalar","neighbor_only":"Komşu dal, üzümün tekil ve çoğul adlarını, dilsel bir değişkesini ve çok üzümü olan kişiyi de kapsar.","neighbor_ref":"root_001050/B001","relation_type":"near_synonym","shared_zone":"İki dal da üzüm meyvesini ve onu veren bitkiyi adlandırır."},{"boundary_match":"partial","distinction":"Komşu genel meyve ve gelişme sürecidir; odak dal tür bakımından üzüm ve asmayla sınırlıdır.","focus_only":"Odak dal belirli olarak üzüm meyvesini, asmayı ve tek asma sürgününü adlandırır.","gloss":"ağaç meyvesi ve meyvenin gelişmesi","neighbor_only":"Komşu dal bütün ağaç meyvelerini, meyvenin oluşmasını ve olgunlaşmasını genel olarak kapsar.","neighbor_ref":"root_000205/B001","relation_type":"near_neighbor","shared_zone":"Üzüm, genel meyve alanının bir üyesi olduğu için dallar meyve kavramında kesişir."}],"source_phrase_ar":"الكَرْم فالعنب أيضا لأنه مجتمع الشعب منظوم الحب (maqayis)؛ الكرمة طاقة من الكرم (ayn)؛ الكَرْم كرم العنب (sihah)؛ الكرمة الطاقة الواحدة من الكرم (tahdhib)؛ يسمى الكرم كرما لأنه وصف بكرم شجرته وثمرته (tahdhib)","source_summary":"Kaynaklar üzüm ve asma anlamında birleşir; tek asma sürgünü ayrıca belirtilir, kümelenmiş taneler ile bitkinin değerli görülmesi de adın açıklaması olarak verilir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الكَرْم بمعنى العنب والكرمة بمعنى الطاقة الواحدة من الكرم وشجرة العنب وثمرتها","what_is_not_ar":"ليس الشرف الخلقي ولا القلادة مع أن بعض المصادر تقارب بينهما في صورة الاجتماع والنظم"},"support_links":[]},{"boundary":"Bu dal onurlandırma veya saygınlık anlamını değil, bir kabın ağzına konan tabak biçimli nesneyi anlatır.","branch_kind":"bare","branch_ref":"root_001294/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْرَمَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>akorama|ROOT:krm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:17:4:1","qac_word_ref":"89:17:4","surface_ar":"تُكْرِمُ"}],"gloss":"kap ağzına konan tabak biçimli kapak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, bir kabın üst açıklığını örten tabak biçimli kapaktır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Testi ve tencere, bu kapağın üzerine konduğu iki kap örneğidir."}}],"root_ar":"ك ر م","root_id":"root_001294","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Testi veya tencere gibi bir kabın üstünü örten somut nesnenin tam açıklayıcı karşılığıdır.","boundary_detail":"Bu dal onurlandırma veya saygınlık anlamını değil, bir kabın ağzına konan tabak biçimli nesneyi anlatır.","branch_image_ar":"طبق على رأس الوعاء","concept_gloss":"kap ağzına konan tabak biçimli kapak","contextual_glosses":[{"applicability":"Nesnenin özellikle testinin ağzına konduğu bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Testinin üstünü kapatan nesneyi korur."},"facet_ids":["F001","F002"],"text":"testi kapağı","usage_role":"contextual"},{"applicability":"Nesnenin tencerenin üstüne yerleştirilen bir tabak olduğu bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tencere ve tabak biçimi ayrıntılarını korur."},"facet_ids":["F001","F002"],"text":"tencere üstüne konan tabak","usage_role":"explanatory"}],"definition":"Testi veya tencere gibi bir kabın ağzına konan tabak biçimli kapaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, bir kabın üst açıklığını örten tabak biçimli kapaktır."},{"facet_id":"F002","role":"example","statement":"Testi ve tencere, bu kapağın üzerine konduğu iki kap örneğidir."}],"identity_rationale":"Kaynak ifadesi, belirli biçimi testi veya tencere ağzına konan tabak olarak tanımlar. Verilen çerçeve bu somut kapatma işlevini doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"testi veya tencere ağzına konan tabak biçimli kapak"}],"lexicalization_note":"Tanım yalın nesne adını, testi ya da tencere ağzına konan tabak biçimli kapakla sınırlar.","neighbor_coverage_note":"Adayların tamamı incelendi; kabın kendisi ile bağlama yoluyla kapatmayı gösteren iki ilişki nesnenin sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komşu içerik taşıyan ana kaptır; odak dal ise o kabın ağzına sonradan konan ayrı kapatma parçasıdır.","focus_only":"Odak dal, kabın kendisini değil, onun üst açıklığını örten tabak biçimli parçayı adlandırır.","gloss":"içine bir şey konan kap","neighbor_only":"Komşu dal, içine bir şey konan kabın veya kabın genel adıdır.","neighbor_ref":"root_000063/B004","relation_type":"same_field","shared_zone":"İki dal aynı kap kullanımı ortamında yer alan nesneleri anlatır."},{"boundary_match":"thematic_only","distinction":"Odak dal üstüne konan bir kapaktır; komşu ise kabın ağzını bağlayıp sıkan esnek araç ve işlemdir.","focus_only":"Odak dal, açıklığın üzerine yerleştirilen sert ve tabak biçimli kapağı belirtir.","gloss":"kabı bağlayan ip veya kayış","neighbor_only":"Komşu dal, su kabı veya başka bir kabı bağlayarak kapatan ip, kayış ve bağlama işlemini kapsar.","neighbor_ref":"root_001678/B001","relation_type":"thematic","shared_zone":"Her iki dal da bir kabın ağzını kapalı tutma senaryosunda yer alır."}],"source_phrase_ar":"الكرامة طبق يوضع على رأس الحب (ayn;sihah)؛ لطبق القدر والحب الكرامة (tahdhib)","source_summary":"Kaynaklar, nesneyi testi veya tencerenin üstüne konan tabak biçimli kapak olarak ortak biçimde tanımlar.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه الكرامة بمعنى طبق يوضع على رأس الحب أو القدر","what_is_not_ar":"ليس الإكرام ولا الكرامة بمعنى مصدر الفضل"},"support_links":[]},{"boundary":"Dal genel övünme veya genel onurlandırma değildir; eli açıklık alanındaki karşılıklı yarışma ve üstün gelmeyle sınırlıdır.","branch_kind":"non_bare","branch_ref":"root_001294/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْرَمَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>akorama|ROOT:krm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:17:4:1","qac_word_ref":"89:17:4","surface_ar":"تُكْرِمُ"}],"gloss":"eli açıklıkta övünme yarışı ve üstün gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki kişi eli açıklıklarını öne sürerek karşılıklı bir övünme yarışına girer."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yarışın sonuç aşamasında bir kişi diğerini eli açıklık bakımından geçer."}}],"root_ar":"ك ر م","root_id":"root_001294","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca eli açıklık konusunda karşılıklı yarışma ve rakibi geçme eylemlerini birlikte açıklar.","boundary_detail":"Dal genel övünme veya genel onurlandırma değildir; eli açıklık alanındaki karşılıklı yarışma ve üstün gelmeyle sınırlıdır.","branch_image_ar":"مفاخرة الكرم والغلبة فيه","concept_gloss":"eli açıklıkta övünme yarışı ve üstün gelme","contextual_glosses":[{"applicability":"Karşılıklı yarışmanın başladığı, fakat sonucun ayrıca belirtilmediği eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı övünme yarışını ve yarışma alanını korur."},"facet_ids":["F001"],"text":"eli açıklıkta övünme yarışına girdi","usage_role":"contextual"},{"applicability":"Yarışın sonucunda bir kişinin ötekine üstün geldiği eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Rakibi belirli alanda geçme sonucunu korur."},"facet_ids":["F002"],"text":"eli açıklıkta onu geçti","usage_role":"contextual"}],"definition":"Bir kişiyle eli açıklık konusunda karşılıklı övünme yarışına girmek ve bu yarışta onu geçmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki kişi eli açıklıklarını öne sürerek karşılıklı bir övünme yarışına girer."},{"facet_id":"F002","role":"core","statement":"Yarışın sonuç aşamasında bir kişi diğerini eli açıklık bakımından geçer."}],"identity_rationale":"Kaynak ifadesi iki aşamalı olarak, biriyle eli açıklık konusunda övünme yarışına girmeyi ve ardından onu bu konuda geçmeyi anlatır. Verilen dal kimliği hem yarışmayı hem de üstün gelme sonucunu doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"onunla eli açıklık konusunda övünme yarışına girdi"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"eli açıklıkta onu geçti"}],"lexicalization_note":"Tanım yalnızca belirtilmiş eylem yapılarındaki karşılıklı övünme yarışı ve üstün gelme anlamını verir; yalın kök anlamına genişletmez.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; yarışma düzenini paylaşan ve konu sınırını açıkça gösteren iki yakın dal seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Eylem düzeni benzerdir, fakat odak dal yalnızca eli açıklık ölçütüne; komşu dal ise şan ve büyük işler ölçütüne bağlıdır.","focus_only":"Odak dalın yarışma ölçütü özellikle eli açıklıktır.","gloss":"şan konusunda övünme yarışı ve üstünlük","neighbor_only":"Komşu dalın yarışma ölçütü şan, büyük işler ve toplumsal üstünlüktür; topluluğun karşılıklı yarışması da kapsanır.","neighbor_ref":"root_001398/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da karşılıklı övünme yarışını ve rakibe üstün gelmeyi anlatır."},{"boundary_match":"partial","distinction":"Komşu genel övünme üstünlüğüdür; odak dalın ayırt edici koşulu yarışmanın eli açıklık üzerinden yürütülmesidir.","focus_only":"Odak dal, yarışma ve üstün gelmeyi yalnızca eli açıklık bakımından sınırlar.","gloss":"övünme yarışında üstün gelme","neighbor_only":"Komşu dal genel övünme alanında rakibi geçme ve ondan üstün sayılma anlamını taşır.","neighbor_ref":"root_001135/B002","relation_type":"near_synonym","shared_zone":"İki dal da övünme yarışına girme ve karşıdakini geçme sonucunda kesişir."}],"source_phrase_ar":"كارمت الرجل إذا فاخرته في الكرم فكرمته إذا غلبته فيه (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Eli açıklık konusunda karşılıklı övünme yarışına girmek ile rakibi bu konuda geçmek iki bağlı aşama olarak tanıklanır."}],"source_summary":"Bu anlam için birden çok kaynağın ortaklaştırılabileceği ayrı bir özet bulunmaz; dal tek bir sözlük tanıklığıyla sınırlıdır.","sources":["SI"],"what_is_ar":"يدخل فيه كارمت الرجل إذا فاخرته في الكرم وكرمته إذا غلبته فيه","what_is_not_ar":"ليس مطلق الإكرام ولا هدية المكافأة"},"support_links":[]},{"boundary":"Dal bütün uyluk kemiğini veya kalça eklemini değil, kalça yuvasında dönen yuvarlak kemik başını adlandırır.","branch_kind":"bare","branch_ref":"root_001294/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْرَمَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>akorama|ROOT:krm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:17:4:1","qac_word_ref":"89:17:4","surface_ar":"تُكْرِمُ"}],"gloss":"uyluk kemiğinin kalça yuvasındaki yuvarlak başı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anılan parça, uyluk kemiğinin yuvarlak başıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu baş kalça yuvasına oturur ve yuvanın içinde dönerek eklem hareketine katılır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Parçanın yuvarlak biçimi ceviz benzetmesiyle açıklanır."}}],"root_ar":"ك ر م","root_id":"root_001294","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalça eklemine oturan belirli kemik parçasını biçimi ve konumuyla tam olarak açıklar.","boundary_detail":"Dal bütün uyluk kemiğini veya kalça eklemini değil, kalça yuvasında dönen yuvarlak kemik başını adlandırır.","branch_image_ar":"رأس الفخذ المستدير","concept_gloss":"uyluk kemiğinin kalça yuvasındaki yuvarlak başı","contextual_glosses":[{"applicability":"Anatomik bağlamın kalça eklemini zaten belirgin kıldığı cümlelerde doğal kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli kemik bölümünün uyluk başı oluşunu korur."},"facet_ids":["F001","F002"],"text":"uyluk kemiği başı","usage_role":"general"},{"applicability":"Parçanın biçimini, yerini ve hareketini açıkça belirtmek gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yuvarlak biçim, kalça yuvası ve dönme ilişkisini birlikte korur."},"facet_ids":["F001","F002","F003"],"text":"kalça yuvasında dönen yuvarlak kemik başı","usage_role":"explanatory"}],"definition":"Uyluk kemiğinin kalça yuvasına oturan ve yuvanın içinde dönen ceviz biçimli yuvarlak başıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anılan parça, uyluk kemiğinin yuvarlak başıdır."},{"facet_id":"F002","role":"specialization","statement":"Bu baş kalça yuvasına oturur ve yuvanın içinde dönerek eklem hareketine katılır."},{"facet_id":"F003","role":"example","statement":"Parçanın yuvarlak biçimi ceviz benzetmesiyle açıklanır."}],"identity_rationale":"Kaynak ifadesi, uyluk kemiğinin ceviz gibi yuvarlak başını ve bu başın kalça yuvasında dönmesini açıkça belirtir. Verilen dal kimliği bu anatomik parçayı ve hareket ilişkisini doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"uyluk kemiğinin kalça yuvasındaki yuvarlak başı"}],"lexicalization_note":"Tanım, yalın anatomik nesne adını verir ve onu kalça yuvasındaki yuvarlak uyluk başıyla sınırlar.","neighbor_coverage_note":"Tüm aday komşular incelendi; eklem yuvası ile yakın anatomik yapıyı ayıran iki ilişki en açıklayıcı bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ekleme giren yuvarlak kemik başıdır; komşu dal ise birleşme yeri ya da başın oturduğu yuva tarafındadır.","focus_only":"Odak dal, kalça yuvasına oturan belirli yuvarlak uyluk kemiği başını adlandırır.","gloss":"kemiklerin birleşme yeri veya kalça yuvası","neighbor_only":"Komşu dal, iki kemiğin birleşme yerini veya kalça yuvasını ve bunlardan başka kap ya da orta nokta uzantılarını kapsar.","neighbor_ref":"root_000347/B011","relation_type":"near_neighbor","shared_zone":"İki dal kalça ekleminin birbirine oturan parçalarını anlatır."},{"boundary_match":"field_only","distinction":"Ortak anatomik bölgeye karşın odak dal tek bir kemik parçasıdır; komşu dal sinir, çift taraflı yapılar ve yaralanma durumlarını da içerir.","focus_only":"Odak dal yalnızca kalça yuvasındaki yuvarlak uyluk kemiği başını belirtir.","gloss":"kalça çevresindeki sinir veya uyluk başları","neighbor_only":"Komşu dal kalça çevresindeki siniri, iki uyluk başını ve bunların kopması ya da kalçanın çıkması durumunu kapsar.","neighbor_ref":"root_000311/B007","relation_type":"same_field","shared_zone":"Her iki dal kalça ve uyluk başı anatomisi alanındadır."}],"source_phrase_ar":"الكرمة رأس الفخذ المستدير كأنه جوزة تدور في قلت الورك (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Uyluk kemiğinin ceviz biçimli yuvarlak başı ve bu başın kalça yuvasında dönmesi birlikte tanımlanır."}],"source_summary":"Bu anatomik anlam için ortaklaştırılacak çok kaynaklı bir açıklama yoktur; tanıklık tek sözlükte yer alır.","sources":["SI"],"what_is_ar":"يدخل فيه الكرمة بمعنى رأس الفخذ المستدير الذي يدور في قلت الورك","what_is_not_ar":"ليس الكرمة التي هي طاقة من الكرم ولا القلادة"},"support_links":[]},{"boundary":"Dal genel hediye verme veya genel ödül değildir; sunulan şey ya da söylenen övgü karşılığında bir karşılık beklentisi bulunur.","branch_kind":"non_bare","branch_ref":"root_001294/B008","candidate_links":[{"candidate_id":"cand_26a441939b3b5b26da0e","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَكْرَمَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>akorama|ROOT:krm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:17:4:1","qac_word_ref":"89:17:4","surface_ar":"تُكْرِمُ"}],"gloss":"karşılık bekleyerek sunma ve övgüyü ödüllendirme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey, alıcının karşılık vermesi beklentisiyle ona sunulur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Alıcının beklenen karşılığı ödül veya denk bir yarar olarak sunması amaçlanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişi, kendisine yöneltilen övgüyü ödüllendirerek karşılayan kimse diye nitelenebilir."}}],"root_ar":"ك ر م","root_id":"root_001294","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşılık beklentili sunma eylemi ile övgüye ödülle karşılık veren kişi kullanımını birlikte açıklar.","boundary_detail":"Dal genel hediye verme veya genel ödül değildir; sunulan şey ya da söylenen övgü karşılığında bir karşılık beklentisi bulunur.","branch_image_ar":"هدية تطلب المكافأة","concept_gloss":"karşılık bekleyerek sunma ve övgüyü ödüllendirme","contextual_glosses":[{"applicability":"Bir şeyin alıcıdan karşılık alma amacıyla verildiği eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sunmayı, alıcıyı ve ödül beklentisini korur."},"facet_ids":["F001","F002"],"text":"karşılığında ödül bekleyerek sundu","usage_role":"contextual"},{"applicability":"Kişinin kendisini öveni ödüllendirmesi veya ona karşılık vermesi niteliğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Övgü ile buna verilen ödüllendirici karşılık arasındaki ilişkiyi korur."},"facet_ids":["F003"],"text":"övgüyü karşılıksız bırakmayan kişi","usage_role":"explanatory"}],"definition":"Bir şeyi alıcının ödül veya benzeri bir karşılık vermesi beklentisiyle sunmak ya da bir kişiyi kendisine yöneltilen övgüyü karşılıksız bırakmayıp ödüllendiren kimse olarak nitelemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey, alıcının karşılık vermesi beklentisiyle ona sunulur."},{"facet_id":"F002","role":"core","statement":"Alıcının beklenen karşılığı ödül veya denk bir yarar olarak sunması amaçlanır."},{"facet_id":"F003","role":"associated_use","statement":"Bir kişi, kendisine yöneltilen övgüyü ödüllendirerek karşılayan kimse diye nitelenebilir."}],"identity_rationale":"Kaynak ifadesi tek bir armağan olayından daha geniş iki bağlı yapıyı verir: karşılığında ödül almak umuduyla bir şey sunmak ve bir kişiyi övgüsüne karşılık veren kimse olarak nitelemek. Dal korunabilir, ancak tanımın hem sunma eylemini hem de övgüyü karşılıksız bırakmayan kişiyi ayrı tutması gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"karşılığında ödül almak için onu sundu"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kendisine yöneltilen övgüyü ödüllendiren kişi"}],"lexicalization_note":"Tanım, yalnızca karşılık bekleyerek sunma ve övgüyü ödüllendiren kişi yapılarıyla sınırlıdır; bunlardan yalın bir hediye anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel karşılık verme ile ödül veya armağan alanını ayıran iki komşu en yararlı karşılaştırmayı sağladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu genel ve iki yönlü karşılık verme kavramıdır; odak dal ise baştan karşılık beklentisiyle sunulan şey veya övgüye verilen ödülle sınırlıdır.","focus_only":"Odak dalda ilk eylem, ileride karşılık almak amacıyla bir şey sunmaktır; ayrıca övgüyü ödüllendiren kişi kullanımı vardır.","gloss":"bir eyleme iyi veya kötü karşılık verme","neighbor_only":"Komşu dal, yapılmış bir eylemi iyi veya kötü bir sonuçla karşılamayı ve öç alma türü karşılıkları genel olarak kapsar.","neighbor_ref":"root_000244/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal bir eylem ile ona dönen karşılık arasındaki ilişkiyi içerir."},{"boundary_match":"field_only","distinction":"Komşu verilen ödülün kendisidir; odak dal ise ödül almak için önce bir şey sunma düzenini ve övgüyü ödüllendiren kişiyi anlatır.","focus_only":"Odak dalda sunma işleminin amacı alıcıdan daha sonra bir ödül ya da karşılık almaktır.","gloss":"ödül veya armağan","neighbor_only":"Komşu dal, insanlara verilen ödül ve armağanı, önceden bir karşılık beklentisi şartı olmadan adlandırır.","neighbor_ref":"root_000276/B010","relation_type":"same_field","shared_zone":"İki dalda da bir kişiye verilen değerli şey ve ödüllendirme senaryosu bulunur."}],"source_phrase_ar":"أكارم بها يهود أي أهديها إليهم فيثيبوني عليها (tahdhib)؛ أخ مكارم أي يكافئني على مدحي إياه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Karşılık bekleyerek bir şey sunma ile kendisine yöneltilen övgüyü ödüllendiren kişi nitelemesi birlikte tanıklanır."}],"source_summary":"Bu dal için çok kaynaklı ortak bir açıklama yoktur; iki bağlı kullanım tek bir sözlük tanıklığıyla aktarılır.","sources":["TA"],"what_is_ar":"يدخل فيه أكارم بها أي أهديها طلبا للثواب والمكافأة وطلب الجائزة بوسيلة المدح","what_is_not_ar":"ليس المفاخرة في الكرم ولا الإكرام المجرد"},"support_links":["sup_8cee24f222a125b9f45c"]},{"boundary":"Dal genel saygınlık veya genel onurlandırma değildir; bir öneri ya da isteğe verilen memnuniyetli kabul ve iyi dilek kalıplarıyla sınırlıdır.","branch_kind":"collocation","branch_ref":"root_001294/B009","candidate_links":[{"candidate_id":"cand_21cd8c1582ef56c05f3e","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَكْرَمَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>akorama|ROOT:krm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:17:4:1","qac_word_ref":"89:17:4","surface_ar":"تُكْرِمُ"}],"gloss":"memnuniyetle kabul ve saygı bildiren kalıp yanıt","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Konuşan, öneriyi veya isteği olumlu biçimde kabul eder."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kabul, karşıdakine sevgi, memnuniyet ve değer verme duygusuyla güçlendirilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı işlev, karşıdakinin kendisi veya gözü için değer bildiren çeşitli kalıp biçimlerle söylenir."}}],"root_ar":"ك ر م","root_id":"root_001294","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir isteği kabul ederken karşıdakine sevgi ve değer verildiğini de bildiren sözlerin genel açıklamasıdır.","boundary_detail":"Dal genel saygınlık veya genel onurlandırma değildir; bir öneri ya da isteğe verilen memnuniyetli kabul ve iyi dilek kalıplarıyla sınırlıdır.","branch_image_ar":"جواب الرضا والكرامة","concept_gloss":"memnuniyetle kabul ve saygı bildiren kalıp yanıt","contextual_glosses":[{"applicability":"Bir öneri veya isteğin sıcak ve istekli biçimde kabul edildiği yanıtta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Olumlu kabulü ve memnuniyet duygusunu korur."},"facet_ids":["F001","F002"],"text":"evet, memnuniyetle","usage_role":"contextual"},{"applicability":"Kabulün özellikle karşıdakine duyulan sevgi ve değerle gerekçelendirildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kabulü, gönüllülüğü ve karşıdaki kişiye değer verme yönünü korur."},"facet_ids":["F001","F002","F003"],"text":"senin için seve seve","usage_role":"contextual"}],"definition":"Bir öneri veya isteği memnuniyetle kabul ederken karşıdakine sevgi, saygı ve değer verme de bildiren kalıplaşmış yanıttır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Konuşan, öneriyi veya isteği olumlu biçimde kabul eder."},{"facet_id":"F002","role":"core","statement":"Kabul, karşıdakine sevgi, memnuniyet ve değer verme duygusuyla güçlendirilir."},{"facet_id":"F003","role":"source_variant","statement":"Aynı işlev, karşıdakinin kendisi veya gözü için değer bildiren çeşitli kalıp biçimlerle söylenir."}],"identity_rationale":"Kaynak ifadesi, kabul edilen bir öneriye sevgi, memnuniyet ve karşıdakine değer verme ekleyen birkaç kalıp yanıt biçimi sunar. Verilen dal çerçevesi bunları kabul ve saygı bildiren sözler olarak doğru biçimde bir araya getirir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"evet, memnuniyetle ve seve seve"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"senin için seve seve; sana duyduğum saygıyla"}],"lexicalization_note":"Tanım yalnızca kabul, memnuniyet ve değer verme bildiren belirtilmiş yanıt kalıplarına bağlıdır; yalın bir saygınlık anlamına genişletilmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; yalın olumlu yanıt ile övgü ve istek kalıplarını ayıran iki yakın komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu yalın bir doğrulamadır; odak dal kabulü duygusal sıcaklık ve karşıdakini onurlandırma anlamıyla genişletir.","focus_only":"Odak dal, olumlu yanıtın yanında memnuniyet, sevgi ve karşıdakine değer verme de bildirir.","gloss":"yalın doğrulama ve olumlu yanıt","neighbor_only":"Komşu dal yalnızca söyleneni doğrulayan veya soruya olumlu yanıt veren sade kabul sözüdür.","neighbor_ref":"root_000016/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da konuşmada olumlu yanıt ve kabul işlevi görür."},{"boundary_match":"partial","distinction":"Komşu övgü ve güçlü istek işlevlerine de uzanır; odak dal yanıt olarak memnuniyetli kabul ve saygı bildirmeye bağlıdır.","focus_only":"Odak dalın çekirdeği, bir istek veya öneriye verilen memnuniyetli ve saygılı kabuldür.","gloss":"övgü, sıcak kabul ve güçlü istek kalıbı","neighbor_only":"Komşu dal, kabul dışında doğrudan övgü ve bir işi yapmaya duyulan en güçlü isteği bildiren kalıpları da kapsar.","neighbor_ref":"root_000286/B003","relation_type":"near_synonym","shared_zone":"İki dal, sıcak kabul ve sevgi bildiren bazı kalıp sözlerde doğrudan kesişir."}],"source_phrase_ar":"نعم وحبا وكرامة (sihah)؛ نعم وحبا وكرما وحبا وكرمة (sihah)؛ أفعل ذلك وكرمة لك وكرمى لك وكرامة لك وكرما لك وكرمة عين (tahdhib)","source_summary":"Kaynaklar, bu sözleri olumlu kabulü sevgi ve değer verme duygusuyla güçlendiren yanıtlar olarak birleştirir; birden çok kalıp biçim aynı işlevi taşır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه صيغ الجواب والدعاء مثل حبا وكرامة وكرمة لك وكرمة عين","what_is_not_ar":"ليس الكرامة التي هي طبق ولا المصدر العام للإكرام"},"support_links":["sup_f592d95e95bfe57ac9ff"]},{"boundary":"Dal yalnızca insanı anlatmaz; değer verilen bir şey de kapsama girebilir, topluluk kullanımı ise özellikle soylu ve seçkin kişiye bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001294/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْرَمَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>akorama|ROOT:krm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:17:4:1","qac_word_ref":"89:17:4","surface_ar":"تُكْرِمُ"}],"gloss":"değer verilen varlık ve topluluğun seçkin kişisi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şey, sahibi ya da ilgilisi için vazgeçilmesi zor derecede değerli olabilir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Değer verilen kimse uğruna, kişinin değerli bulduğu başka şeyleri esirgememesi beklenebilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Topluluk yapısında söz, o topluluğun soylu, saygın ve seçkin kişisini belirtir."}}],"root_ar":"ك ر م","root_id":"root_001294","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişisel olarak değer verilen kişi veya şeyi ve topluluk içindeki soylu temsilciyi birlikte açıklayan üst karşılıktır.","boundary_detail":"Dal yalnızca insanı anlatmaz; değer verilen bir şey de kapsama girebilir, topluluk kullanımı ise özellikle soylu ve seçkin kişiye bağlıdır.","branch_image_ar":"العزيز الذي يكرم عليك","concept_gloss":"değer verilen varlık ve topluluğun seçkin kişisi","contextual_glosses":[{"applicability":"Bir kişinin kendisi için çok değerli gördüğü insanı ya da nesneyi anlatan bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Değer veren kişiyi ve değer verilen kişi ya da şey kapsamını korur."},"facet_ids":["F001","F002"],"text":"çok değer verdiği kişi veya şey","usage_role":"general"},{"applicability":"Bir topluluğu temsil eden, soyu ve saygınlığıyla öne çıkan kişi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluk bağını, soyluluğu ve seçkinliği korur."},"facet_ids":["F003"],"text":"topluluğun soylu ve seçkin kişisi","usage_role":"contextual"}],"definition":"Bir kişinin gözünde çok değerli olan herhangi bir kişi veya şey ya da bir topluluğun soylu, saygın ve seçkin temsilcisidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şey, sahibi ya da ilgilisi için vazgeçilmesi zor derecede değerli olabilir."},{"facet_id":"F002","role":"associated_use","statement":"Değer verilen kimse uğruna, kişinin değerli bulduğu başka şeyleri esirgememesi beklenebilir."},{"facet_id":"F003","role":"specialization","statement":"Topluluk yapısında söz, o topluluğun soylu, saygın ve seçkin kişisini belirtir."}],"identity_rationale":"Kaynak ifadesi bir yanda kişiye çok değerli gelen herhangi bir kişi veya şeyi, öte yanda bir topluluğun soylu ve seçkin temsilcisini anlatır. Verilen değerli kişi çerçevesi kullanılabilir, ancak nesneleri de kapsayan ilk kullanımla topluluğun seçkin kişisini anlatan ikinci kullanımın ayrılması gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"senin için çok değerli olan kişi veya şey"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"topluluğun soylu, saygın ve seçkin kişisi"}],"lexicalization_note":"Tanım, kişiye değerli gelen kişi veya şey kullanımını topluluğun seçkin kişisi yapısından ayırır ve bu yapılardan bağımsız yalın bir anlam varsaymaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; kişisel değer, korunmuş seçkinlik ve grup içinden seçilme sınırlarını gösteren iki ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşuda seçilme ve korunma belirleyicidir; odak dalda kişisel değer ilişkisi veya topluluğun soylu temsilcisi olma koşulu öne çıkar.","focus_only":"Odak dal, kişisel olarak değer verilen herhangi bir kişi veya şeyi ve bir topluluğun soylu temsilcisini kapsar.","gloss":"seçilmiş, korunmuş ve en değerli varlık","neighbor_only":"Komşu dal, kadın, topluluk, hayvan veya inci gibi varlıkların seçilmiş, korunmuş ve en değerli üyesi olma yönünü özellikle taşır.","neighbor_ref":"root_001036/B008","relation_type":"near_synonym","shared_zone":"Her iki dal kişi veya şeyler arasından çok değerli ve seçkin olanı anlatabilir."},{"boundary_match":"partial","distinction":"Komşu, seçkinlerden oluşan grup veya seçilmiş bölüm kavramına uzanır; odak dal kişisel değer ilişkisine ve tek bir soylu temsilciye bağlıdır.","focus_only":"Odak dal, sahibine değerli gelen tekil kişi ya da şeyi ve topluluğun soylu temsilcisini anlatır.","gloss":"seçkinler ve grubun seçilmiş bölümü","neighbor_only":"Komşu dal, bir topluluk veya nesne grubunun seçkinleri, önde gelenleri ve geride kalan seçilmiş bölümü gibi çoğul kümeleri de kapsar.","neighbor_ref":"root_001512/B003","relation_type":"near_neighbor","shared_zone":"İki dal topluluk içinden seçkin ve üstün sayılan kişi alanında kesişir."}],"source_phrase_ar":"كل شيء يكرم عليك فهو كريمك وكريمتك (tahdhib)؛ الكريمة الرجل الحسيب (tahdhib)؛ إذا أتاكم كريمة قوم فأكرموه أي كريم قوم (tahdhib)؛ لا تدخر عنه شيئا يكرم عليك (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Kişiye çok değerli gelen kişi veya şey ile bir topluluğun soylu ve seçkin temsilcisi iki bağlı kullanım olarak verilir."}],"source_summary":"Bu dal için ortaklaştırılacak çok kaynaklı bir açıklama yoktur; değer verilen varlık ve topluluğun seçkin kişisi kullanımları tek sözlükte tanıklanır.","sources":["TA"],"what_is_ar":"يدخل فيه كل شيء يكرم عليك فهو كريمك وكريمتك والكريمة بمعنى الحسيب أو كريم القوم وما لا يدخر عنه شيء يكرم","what_is_not_ar":"ليس العنب ولا القلادة ولا طبق الوعاء"},"support_links":[]},{"boundary":"marriage contracting and the idiom of a man taking a woman in marriage","branch_kind":null,"branch_ref":"root_001444/B004","candidate_links":[{"candidate_id":"cand_52fa281701419a01271b","lane":"macro"}],"focus_root_occurrences":[],"gloss":"marriage contract","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الإملاك والتزويج","image_en":"marriage contract"}}],"root_ar":"م ل ك","root_id":"root_001444","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الإملاك والتزويج","image_en":"marriage contract","scope_ar":"عقد التزويج والإملاك؛ شهدنا إملاك فلان؛ ملك الرجل المرأة بمعنى تزوجها","scope_en":"marriage contracting and the idiom of a man taking a woman in marriage"},"support_links":["sup_c90e2bc134658840580d"]},{"boundary":"This branch covers نعم as a praise verb or formula meaning excellent, good, or praiseworthy, including forms opposed to بئس.","branch_kind":null,"branch_ref":"root_001525/B003","candidate_links":[{"candidate_id":"cand_21cd8c1582ef56c05f3e","lane":"macro"}],"focus_root_occurrences":[],"gloss":"praising as excellent","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"مدح الشيء بنعم","image_en":"praising as excellent"}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"مدح الشيء بنعم","image_en":"praising as excellent","scope_ar":"يدخل فيه نعم المقابلة لبئس، ونعم الشيء، ونعما، وفبها ونعمت، حيث تكون اللفظة فعلا أو صيغة مدح واستحسان.","scope_en":"This branch covers نعم as a praise verb or formula meaning excellent, good, or praiseworthy, including forms opposed to بئس."},"support_links":["sup_f592d95e95bfe57ac9ff"]},{"boundary":"İnsan çocuğu için baba kaybı ve ergenlik sınırı, hayvan yavrusu için anne kaybı esastır; genel yalnızlık bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B001","candidate_links":[{"candidate_id":"cand_95f55e75ff4283b2cf84","lane":"macro"},{"candidate_id":"cand_cd967dac22d4e075b109","lane":"macro"},{"candidate_id":"cand_cf949783b5773986924a","lane":"macro"},{"candidate_id":"cand_26a441939b3b5b26da0e","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:17:5:2","qac_word_ref":"89:17:5","surface_ar":"يَتِيمَ"}],"gloss":"babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu olma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanlarda durum, bir çocuğun ergenliğe ulaşmadan babasını yitirmesiyle oluşur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan dışındaki hayvanlarda karşılık gelen durum, yavrunun annesini yitirmesidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Türemiş eylemler, bir çocuğu babasız bırakmayı veya çocukları topluca bu duruma düşürmeyi anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bazı türemiş kadın adları, çocukları babasız kalmış olan anneyi niteler."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve hayvan için farklı ebeveyn koşullarını birlikte belirtmek gereken genel açıklamada kullanılır.","boundary_detail":"İnsan çocuğu için baba kaybı ve ergenlik sınırı, hayvan yavrusu için anne kaybı esastır; genel yalnızlık bu dala girmez.","branch_image_ar":"انقطاع الولد عن كافله","concept_gloss":"babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu olma","contextual_glosses":[{"applicability":"Ergenliğe ulaşmadan babası ölen bir insan çocuğundan söz edilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan çocuğunu ve belirleyici baba kaybını açık biçimde korur."},"facet_ids":["F001"],"text":"babasını yitirmiş çocuk","usage_role":"contextual"},{"applicability":"İnsan dışındaki bir hayvanın annesini yitirmiş yavrusundan söz edilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan yavrusunu ve belirleyici anne kaybını açık biçimde korur."},"facet_ids":["F002"],"text":"annesini yitirmiş hayvan yavrusu","usage_role":"contextual"}],"definition":"İnsanlarda ergenliğe ulaşmadan babasını yitirmiş çocuk olma, öteki hayvanlarda ise annesini yitirmiş yavru olma durumudur. Bir çocuğu bu duruma düşürme ve çocukları babasız kalan kadını niteleme gibi türev kullanımlar bu çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanlarda durum, bir çocuğun ergenliğe ulaşmadan babasını yitirmesiyle oluşur."},{"facet_id":"F002","role":"specialization","statement":"İnsan dışındaki hayvanlarda karşılık gelen durum, yavrunun annesini yitirmesidir."},{"facet_id":"F003","role":"extension","statement":"Türemiş eylemler, bir çocuğu babasız bırakmayı veya çocukları topluca bu duruma düşürmeyi anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Bazı türemiş kadın adları, çocukları babasız kalmış olan anneyi niteler."}],"identity_rationale":"Kaynak ifadesi genel olarak bakımı üstlenen kişiden ayrılmayı değil, insan çocuğunda ergenlikten önce babanın, öteki hayvanlarda ise annenin ölümünü belirleyici sayar. Bu nedenle dal, bu iki katılımcı ayrımı açıkça korunarak tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"insanda babasız, hayvanda annesiz kalma"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"çocuk babasını yitirip babasız kaldı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"Tanrı onu babasız bıraktı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çocukları babasız bıraktı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuklar"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuklar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çocukları babasız kalmış kadın"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"çocukları babasız kalmış kadın"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"onları babasız bıraktı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"çocukken kendisini yetiştiren kişiye nispetle, büyüdüğünde de babasını yitirmiş çocuk diye anılan kişi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuklar topluluğu"}],"lexicalization_note":"Tanım, yalın durum ve kişi adlandırmalarını temel alır; çocukları babasız kalan kadın ile büyüdükten sonra da sürdürülen adlandırma yalnız kendi kalıpları içinde tutulur.","neighbor_coverage_note":"Sunulan bütün komşu adaylar değerlendirildi; ebeveyn ölümü, bırakılma, bakım bağı ve tek kalma arasındaki sınırı en açık gösteren üç karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ölümden doğan ve türe göre baba ya da anne üzerinden tanımlanan statüdür; komşu dal ise ölüm gerektirmeyen bırakılma ve bulunma olayını anlatır.","focus_only":"Odak dalda ebeveynin ölümü, insan ve hayvan için ayrı ebeveyn rolleriyle belirleyicidir.","gloss":"ebeveynini yitirmiş yavru ile bırakılmış çocuk","neighbor_only":"Komşu dalda çocuk annesi tarafından bırakılır ve başka biri tarafından bulunur.","neighbor_ref":"root_001466/B007","relation_type":"near_neighbor","shared_zone":"Her ikisi de bir çocuğun veya yavrunun doğal ebeveyn bakımından yoksun kalabildiği durumları anlatır."},{"boundary_match":"field_only","distinction":"Bakıma muhtaçlık odak dalın tanımı değildir ve her bakmakla yükümlü olunan kişi ebeveynini yitirmiş değildir.","focus_only":"Odak dal, insan çocuğunda baba ve hayvan yavrusunda anne ölümüyle sınırlı bir durumdur.","gloss":"ebeveyn kaybı ile bakıma muhtaç olma","neighbor_only":"Komşu dal bakmakla yükümlü olunanları, yük sayılan kişileri ve çocuğu olmayanları da kapsar.","neighbor_ref":"root_001315/B002","relation_type":"same_field","shared_zone":"İki dal da başkasının bakımına veya desteğine ihtiyaç duyan kişilerin alanına değebilir."},{"boundary_match":"partial","distinction":"Odak dalın koşulları ebeveyn türü ve insanlarda ergenlik sınırıyla belirlenir; komşu dal bu koşulları taşımaz ve nadir nesnelere de uygulanır.","focus_only":"Odak dal canlılarda belirli bir ebeveynin ölümüne bağlı statüyü bildirir.","gloss":"ebeveyn kaybı ile tek kalma","neighbor_only":"Komşu dal canlı ya da cansız herhangi bir şeyin tek kalmasını veya benzerinin zor bulunmasını bildirir.","neighbor_ref":"root_001692/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da önceki bir bağdan veya eşlikten yoksun kalma düşüncesi bulunabilir."}],"source_phrase_ar":"اليتم في الناس من قبل الأب وفي سائر الحيوان من جهة الأم (maqayis)؛ يتم الصبي إذا صار يتيما وأيتمه الله (jamhara)؛ أيتمت المرأة فهي موتم (jamhara;sihah)؛ يتمهم الله تيتيما (sihah)؛ اليتيم الذي مات أبوه حتى يبلغ (tahdhib)؛ انقطاع الصبي عن أبيه قبل بلوغه وفي سائر الحيوانات من قبل أمه (mufradat)","source_summary":"Kanıt bütünü, insan çocuğunda baba kaybını, hayvan yavrusunda anne kaybını ve bu durumla ilgili türemiş biçimleri verir. Ergenlik sınırı bazı aktarımlarda açıkça belirtilir; ettirgen ve topluluk bildiren biçimler ayrı tanıklamalar olarak bu çekirdeğe bağlanır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الصبي الذي مات أبوه قبل بلوغه، والبهيمة التي ماتت أمها، وجعل الأولاد أيتاما","what_is_not_ar":"ليس مجرد الانفراد في الأشياء النفيسة ولا الإبطاء في السير ولا الغفلة والتقصير"},"support_links":["sup_77e721a081c56d7de638","sup_8cee24f222a125b9f45c","sup_cf9234255be709a3c2a1","sup_fb77551059ebd1b78c9a"]},{"boundary":"Dal, ebeveyn kaybını değil tekliği veya benzer azlığını anlatır; değerli nesne ve şiir örnekleri çekirdeğin kendisi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:17:5:2","qac_word_ref":"89:17:5","surface_ar":"يَتِيمَ"}],"gloss":"tek kalmış ya da benzeri zor bulunan şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlı ya da cansız bir varlık, başka bir eşlikçi olmadan tek başına bulunduğunda bu nitelemeyi alabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Niteleme, benzeri veya dengi zor bulunan seçkin bir varlığa da uygulanabilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tek başına duran şiir dizesi, eşi zor bulunan inci ve ayrı kumluk kaynaklarda örneklenir."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek başına bulunma ile eşine az rastlanma kapsamlarının ikisini de taşıyan genel niteleme için kullanılır.","boundary_detail":"Dal, ebeveyn kaybını değil tekliği veya benzer azlığını anlatır; değerli nesne ve şiir örnekleri çekirdeğin kendisi değildir.","branch_image_ar":"انفراد الشيء وانقطاع نظيره","concept_gloss":"tek kalmış ya da benzeri zor bulunan şey","contextual_glosses":[{"applicability":"Varlığın eşlikçisiz veya çevresindekilerden ayrı bulunmasının öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Varlığın başka bir eşlikçi olmadan tek kalması özelliğini korur."},"facet_ids":["F001"],"text":"tek başına kalmış","usage_role":"contextual"},{"applicability":"Bir nesnenin veya söz ürününün benzerinin az bulunması vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Benzer azlığını ve bundan doğan eşsizlik niteliğini korur."},"facet_ids":["F002"],"text":"eşi zor bulunan","usage_role":"contextual"}],"definition":"Bir varlığın tek başına kalması veya benzerinin zor bulunmasıdır; şiir dizesi, inci ve tek başına duran kumluk bu niteliğin özel örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlı ya da cansız bir varlık, başka bir eşlikçi olmadan tek başına bulunduğunda bu nitelemeyi alabilir."},{"facet_id":"F002","role":"extension","statement":"Niteleme, benzeri veya dengi zor bulunan seçkin bir varlığa da uygulanabilir."},{"facet_id":"F003","role":"example","statement":"Tek başına duran şiir dizesi, eşi zor bulunan inci ve ayrı kumluk kaynaklarda örneklenir."}],"identity_rationale":"Kaynak ifadesi, tek başına kalan şeyi ve benzeri zor bulunan şeyi aynı dalda açıkça toplar; şiir dizesi, inci ve tek kumluk bu çekirdeğin örnekleridir. Geçici çerçeve bu kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"tek başına veya eşi zor bulunan"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"tek başına duran veya benzeri olmayan şiir dizesi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"tek ve eşi zor bulunan inci"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"tek başına duran kumluk veya dişil varlık"}],"lexicalization_note":"Yalın niteleme tekliği veya benzer azlığını bildirir; şiir dizesi ve inci okumaları yalnız tanıklanmış ad öbeklerinin özel uygulamalarıdır.","neighbor_coverage_note":"Bütün adaylar incelendi; genel teklik, nadirlik, belirli bir nitelikte rakipsizlik ve ebeveyn kaybı ile en güçlü sınırları kuran dört aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tek kalmayı benzer azlığına kadar genişletirken komşu dal sayısal birlik ve tekleştirme işlemlerine de uzanır; bu yüzden kapsamları bütünüyle örtüşmez.","focus_only":"Odak dal, benzeri zor bulunan nesne ile şiir dizesi ve inci gibi kalıplaşmış uygulamaları özellikle kapsar.","gloss":"tek kalmış ve bir olan","neighbor_only":"Komşu dal bir olma, teklik, birer birer gelme ve tek başına gönderme gibi daha geniş işlemleri de kapsar.","neighbor_ref":"root_001141/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığın tek başına ve eşlikçisiz bulunmasını doğrudan anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği tek kalmadır; komşu dalın çekirdeği ise kıtlık ve erişim güçlüğüdür, dolayısıyla yalnızlığın kendisini gerektirmez.","focus_only":"Odak dalda tek başına bulunma yeterlidir ve erişim güçlüğü gerekli değildir.","gloss":"eşi zor bulunan ile nadir ve güç erişilen","neighbor_only":"Komşu dal az bulunmanın yanında bir şeye erişmenin veya benzerini bulmanın güçlüğünü bildirir.","neighbor_ref":"root_001008/B003","relation_type":"near_neighbor","shared_zone":"Benzeri az bulunan bir nesne iki dalın kapsamına da girebilir."},{"boundary_match":"partial","distinction":"Komşu dal belirli insani niteliklerle sınırlı bir üstünlük veya uçluk bildirirken odak dal tek başına bulunmayı da kapsayan daha genel bir nesne niteliğidir.","focus_only":"Odak dal her tür canlı veya cansız varlığın tekliğine ve benzer azlığına uygulanabilir.","gloss":"genel eşsizlik ile bir nitelikte rakipsizlik","neighbor_only":"Komşu dal cömertlik, erdem, iyilik ya da kötülük gibi belirli değerlendirme alanlarında dengi olmayan kişiyi niteler.","neighbor_ref":"root_001240/B018","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir varlığın belli bakımdan denginin bulunmamasını anlatabilir."},{"boundary_match":"partial","distinction":"Bu çağrışım iki dalı özdeş kılmaz; odak dal genel teklik ve eşsizlik, komşu dal ise canlılara özgü ve koşulları belirli bir ebeveyn kaybı statüsüdür.","focus_only":"Odak dal ebeveyn ölümü olmadan da tek kalan veya benzeri az bulunan her şeye uygulanabilir.","gloss":"tek kalma ile ebeveynini yitirme","neighbor_only":"Komşu dal insan çocuğunda baba, hayvan yavrusunda anne ölümünü ve insan için ergenlik sınırını gerektirir.","neighbor_ref":"root_001692/B001","relation_type":"near_neighbor","shared_zone":"Ebeveynini yitiren çocuk veya yavru, tek kalma düşüncesiyle ilişkilendirilebilir."}],"source_phrase_ar":"لكل منفرد يتيم وبيت من الشعر يتيم (maqayis)؛ اليتيم الفرد (jamhara)؛ كل شيء مفرد يعز نظيره فهو يتيم ودرة يتيمة (sihah)؛ الرملة المنفردة وكل منفرد ومنفردة يتيم ويتيمة (tahdhib)؛ كل منفرد يتيم ودرة يتيمة وبيت يتيم (mufradat)","source_summary":"Kaynaklar tek kalma anlamında birleşir ve bir şeyin benzerinin az bulunmasını buna bağlı bir kapsam olarak verir. Şiir dizesi, inci ve kumluk bu ortak anlamı görünür kılan örneklerdir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه كل منفرد أو منفردة، وما عز نظيره كالدرة اليتيمة وبيت الشعر اليتيم والرملة المنفردة","what_is_not_ar":"ليس خصوص موت الأب عن الصبي ولا موت الأم عن البهيمة ولا الإبطاء في السير"},"support_links":[]},{"boundary":"Buradaki anlam zihinsel dikkatsizlik ile görevde eksik bırakmayı birlikte kapsar; salt yavaşlama ayrı daldadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:17:5:2","qac_word_ref":"89:17:5","surface_ar":"يَتِيمَ"}],"gloss":"dalgınlık ve gerekeni eksik yapma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlam, dikkat göstermeme ile bir işi veya yükümlülüğü gerektiği kadar yerine getirmemeyi birlikte kapsar."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yol alış hakkında kullanılan olumsuz kalıp, gidişte dalgınlık veya eksik davranış bulunmadığını bildirir."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dikkat eksikliği ile görevde yetersiz kalmanın birlikte anlatıldığı genel bağlamlarda kullanılır.","boundary_detail":"Buradaki anlam zihinsel dikkatsizlik ile görevde eksik bırakmayı birlikte kapsar; salt yavaşlama ayrı daldadır.","branch_image_ar":"غفلة وتقصير","concept_gloss":"dalgınlık ve gerekeni eksik yapma","contextual_glosses":[{"applicability":"Bir kişinin yol alışında dikkatsizlik veya kusurlu davranış bulunmadığını söyleyen tanıklanmış kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Olumsuzluğu, yol alış bağlamını ve iki kusurun yokluğunu korur."},"facet_ids":["F002"],"text":"gidişinde dalgınlık veya eksiklik yok","usage_role":"contextual"}],"definition":"Bir şeyi yeterince gözetmeyerek dalgın davranma ve yapılması gerekeni eksik bırakmadır; yol alışa ilişkin kalıpta bu özelliklerin bulunmadığı söylenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlam, dikkat göstermeme ile bir işi veya yükümlülüğü gerektiği kadar yerine getirmemeyi birlikte kapsar."},{"facet_id":"F002","role":"associated_use","statement":"Yol alış hakkında kullanılan olumsuz kalıp, gidişte dalgınlık veya eksik davranış bulunmadığını bildirir."}],"identity_rationale":"Kaynak ifadesi dalı açıkça dalgınlık ve gerekeni eksik yapma olarak tanımlar; yol alış kalıbı da bu iki niteliğin bulunmadığını söyleyen bir uygulamadır. Geçici çerçeve kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dalgınlık ve gerekeni eksik yapma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"gidişinde dalgınlık veya eksik davranış yok"}],"lexicalization_note":"Yalın biçim dalgınlık ve eksik davranmayı anlatır; yol alışa ilişkin olumsuz okuma yalnız tanıklanmış cümle kalıbının kapsamındadır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dikkatsizlik, savsaklama, mazeretli eksiklik ve yavaşlama arasındaki ayrımları en iyi gösteren dört aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dikkatsizlik ile kusuru birleştirir; komşu dal ise bilinçli oyalanma, tembellik ve güçsüz değerlendirme gibi nedenleri de kapsar.","focus_only":"Odak dal dalgınlığı ve eksik yapmayı yalın bir anlam olarak, ayrıca yol alış kalıbındaki olumsuz uygulamayla verir.","gloss":"dalgınlık ve eksik yapma ile savsaklama","neighbor_only":"Komşu dal işi savsaklama, oyalanma, tembellikten yatma ve görüş zayıflığı gibi daha geniş davranışları kapsar.","neighbor_ref":"root_000902/B003","relation_type":"near_synonym","shared_zone":"İki dal da kişinin üstlendiği işi yeterince yerine getirmemesini anlatabilir."},{"boundary_match":"partial","distinction":"Komşu dal dikkat dışına çıkma olayında yoğunlaşır; odak dal ise bunun yanında görev veya davranıştaki yetersizliği de kurucu sayar.","focus_only":"Odak dal dikkat eksikliğinin yanında yapılması gerekeni eksik bırakmayı da doğrudan içerir.","gloss":"dalgınlık ve eksik yapma ile gözden kaçırma","neighbor_only":"Komşu dal bir şeyi uyanıklık ve koruma azlığından dolayı unutma veya gözden kaçırma yönünü öne çıkarır.","neighbor_ref":"root_001097/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak alanı, yeterli dikkat göstermemektir."},{"boundary_match":"partial","distinction":"Odak dal dikkatsizlik ve eksikliktir; komşu dal ise eksikliği mazeret gösterme tavrıyla birlikte tanımlar.","focus_only":"Odak dalda sahte mazeret gösterme veya kendini haklı çıkarma koşulu yoktur.","gloss":"eksik yapma ile mazeretli savsaklama","neighbor_only":"Komşu dal eksik davranışa gerçek olmayan bir mazeret gösterme veya özür görüntüsü verme boyutunu ekler.","neighbor_ref":"root_000995/B005","relation_type":"near_neighbor","shared_zone":"İki dal da bir işin gerektiği gibi yerine getirilmemesini kapsayabilir."},{"boundary_match":"partial","distinction":"Ortak kalıp anlam özdeşliği yaratmaz; bu dal davranış kusurunu, komşu dal ise hızın düşmesini veya gecikmeyi anlatır.","focus_only":"Odak dal dikkatsizlik ve gerekeni eksik yapma kusurlarını bildirir.","gloss":"dikkatsizlik ile yavaşlama","neighbor_only":"Komşu dal hareketin veya yol alışın ağırlaşmasını ve iyiliğin gecikmesini bildirir.","neighbor_ref":"root_001692/B004","relation_type":"near_neighbor","shared_zone":"Aynı yol alış ifadesi kaynaklarda iki ayrı yorumun bağlamı olabilir."}],"source_phrase_ar":"اليتم الغفلة والتقصير وما في سيره يتم أي ما فيه غفلة ولا تقصير (jamhara)؛ أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره (tahdhib)","source_summary":"Kaynakların ortak alanı dalgınlıktır. Eksik davranma ve yol alışta dalgınlık ya da eksiklik bulunmadığını bildiren kalıp, bunları açıkça birlikte veren aktarımın ek ayrıntılarıdır.","sources":["JA","TA"],"what_is_ar":"يدخل فيه اليتم بمعنى الغفلة والتقصير، وما نفي عن السير في قولهم ما في سيره يتم عند من فسره بذلك","what_is_not_ar":"ليس اليتم بمعنى اليتيم الذي مات أبوه ولا الانفراد النفيس ولا الإبطاء الخالص"},"support_links":[]},{"boundary":"Çekirdek hareketin ağırlaşması veya gecikmesidir; çocuğa iyiliğin geç ulaşması yalnız açıklayıcı bir bağlantıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:17:5:2","qac_word_ref":"89:17:5","surface_ar":"يَتِيمَ"}],"gloss":"yavaşlama veya gecikme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, hareketin olağan hızından daha ağır ilerlemesi veya gecikmesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tanıklanmış yol alış kalıbında, bir kimsenin gidişinde yavaşlama bulunduğu anlatılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Babasını yitirmiş çocuğa iyiliğin geç ulaşması, ebeveyn kaybı adlandırmasıyla kurulan açıklayıcı bağ olarak verilir."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hareketin ya da ilerleyişin olağan hızından daha ağır sürmesini anlatan genel bağlamlarda kullanılır.","boundary_detail":"Çekirdek hareketin ağırlaşması veya gecikmesidir; çocuğa iyiliğin geç ulaşması yalnız açıklayıcı bir bağlantıdır.","branch_image_ar":"إبطاء السير والبر","concept_gloss":"yavaşlama veya gecikme","contextual_glosses":[{"applicability":"Tanıklanmış yol alış kalıbında kişinin ilerleyişinin ağır olduğunu belirtmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yol alış bağlamını ve hareket hızının düşmesini açıkça korur."},"facet_ids":["F002"],"text":"gidişinde yavaşlama var","usage_role":"contextual"},{"applicability":"Babasını yitirmiş çocuğa gösterilen iyiliğin gecikmesini adlandırma gerekçesi olarak açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İyilik alanını, gecikmeyi ve açıklayıcı bağlantının yönünü korur."},"facet_ids":["F003"],"text":"iyiliğin geç ulaşması","usage_role":"explanatory"}],"definition":"Bir şeyin yavaşlaması veya gecikmesidir. Yol alışın ağırlaşması bunun özel uygulamasıdır; babasını yitirmiş çocuğa iyiliğin geç ulaşması ise açıklayıcı bir bağlantıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, hareketin olağan hızından daha ağır ilerlemesi veya gecikmesidir."},{"facet_id":"F002","role":"specialization","statement":"Tanıklanmış yol alış kalıbında, bir kimsenin gidişinde yavaşlama bulunduğu anlatılır."},{"facet_id":"F003","role":"associated_use","statement":"Babasını yitirmiş çocuğa iyiliğin geç ulaşması, ebeveyn kaybı adlandırmasıyla kurulan açıklayıcı bağ olarak verilir."}],"identity_rationale":"Kaynak ifadesi yavaşlama anlamını ve yol alış uygulamasını doğrudan destekler; babasını yitirmiş çocuğa iyiliğin geç ulaşması ise adlandırmayı açıklayan bağımlı bir gerekçedir. Bu açıklama çekirdekle eş düzeye çıkarılmadan dal korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"gidişinde yavaşlama var"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yavaşlama ve gecikme"}],"lexicalization_note":"Yalın biçim yavaşlama anlamını taşır; yol alış okuması kendi kalıbında tutulur ve iyiliğin geç ulaşması bağımsız bir yalın anlam sayılmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; çaba eksikliği, güçten düşme, isteksiz ağırlaşma ve dikkatsizlikten ayrımı en belirgin dört komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hız ve zaman bakımından ağırlaşmayı temel alır; komşu dal ise görevde yetersiz çaba gösterme anlamına da uzanır.","focus_only":"Odak dal yalın yavaşlamayı ve babasını yitirmiş çocuğa iyiliğin geç ulaşmasına ilişkin açıklamayı içerir.","gloss":"yavaşlama ile çabada geri kalma","neighbor_only":"Komşu dal bir işte, özellikle öğüt vermede, gereken çabayı göstermeyip geri kalmayı da içerir.","neighbor_ref":"root_000048/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir işin veya ilerleyişin beklenenden geç gerçekleşmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal gözlenen hız düşüşüdür; komşu dal ise hareketin altında yatan gevşeme ve güç azalması durumunu öne çıkarır.","focus_only":"Odak dal yavaşlamayı nedenine bakmadan bildirir ve iyiliğin gecikmesine ilişkin açıklayıcı bir bağlantı taşır.","gloss":"yavaşlama ile güçten düşme","neighbor_only":"Komşu dal işte veya yol alışta güç ve canlılığın azalmasından doğan gevşemeyi anlatır.","neighbor_ref":"root_001621/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal yol alışın veya işin daha ağır sürmesine uygulanabilir."},{"boundary_match":"partial","distinction":"Odak dal sonucun hız boyutunu adlandırır; komşu dal bedensel veya ruhsal gevşekliği kurucu unsur yapar.","focus_only":"Odak dal gecikmeyi ve ilerleyişin ağırlaşmasını bedensel bir neden gerektirmeden anlatır.","gloss":"gecikme ile gevşek ve isteksiz davranma","neighbor_only":"Komşu dal tembellik, ateşli hastalık veya beden gevşekliğiyle bağlantılı isteksizlik ve ağır davranmayı kapsar.","neighbor_ref":"root_000392/B001","relation_type":"near_neighbor","shared_zone":"Ağır yürüyen veya işini yavaş yapan kişi iki alanın görünür sonucunu paylaşabilir."},{"boundary_match":"partial","distinction":"Bu dal zamansal ve devinimsel ağırlaşmadır; komşu dal ise davranış ve dikkat kusurudur.","focus_only":"Odak dal hareket hızının düşmesini veya bir şeyin geç ulaşmasını anlatır.","gloss":"yavaşlama ile dikkatsizlik","neighbor_only":"Komşu dal dikkat göstermemeyi ve yapılması gerekeni eksik bırakmayı anlatır.","neighbor_ref":"root_001692/B003","relation_type":"near_neighbor","shared_zone":"Yol alışa ilişkin aynı kalıp iki anlam için kaynaklarda yorumlanmıştır."}],"source_phrase_ar":"في سيره يتم أي إبطاء (sihah)؛ اليتم الإبطاء ومنه أخذ اليتيم لأن البر يبطىء عنه (tahdhib)","source_summary":"Kaynakların ortak alanı genel yavaşlama ve gecikmedir. Yol alıştaki ağırlaşma bir aktarımdaki özel uygulama, iyiliğin babasını yitirmiş çocuğa geç ulaşması ise diğer aktarımdaki adlandırma açıklamasıdır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه اليتم بمعنى الإبطاء، وخاصة قولهم في سيره يتم، وتعليل تسمية اليتيم بأن البر يبطئ عنه","what_is_not_ar":"ليس الغفلة والتقصير إلا حيث جعلها المصدر تفسيرا آخر، وليس الانفراد في الشيء"},"support_links":[]},{"boundary":"Kullanım yalnız kadınlara yönelik tanıklanmış adlandırma kalıplarıyla sınırlıdır; gerçek bir eş kaybı veya genel eşsizlik anlamı çıkarılamaz.","branch_kind":"collocation","branch_ref":"root_001692/B005","candidate_links":[{"candidate_id":"cand_52fa281701419a01271b","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:17:5:2","qac_word_ref":"89:17:5","surface_ar":"يَتِيمَ"}],"gloss":"evlilikle sona erip ermediği tartışmalı kadın adlandırması","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kullanım, babasını yitirmiş çocuklara verilen adın kadın hakkında da söylenmesinden oluşur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir aktarımda kadın evlenince bu adlandırma sona erer; karşıt aktarımda ise kadın bu adı hiçbir zaman yitirmez."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadına yönelik bu özel adın evlilikten sonra sürüp sürmediğine ilişkin iki aktarımı birlikte özetlerken kullanılır.","boundary_detail":"Kullanım yalnız kadınlara yönelik tanıklanmış adlandırma kalıplarıyla sınırlıdır; gerçek bir eş kaybı veya genel eşsizlik anlamı çıkarılamaz.","branch_image_ar":"انفراد المرأة عن الزوج","concept_gloss":"evlilikle sona erip ermediği tartışmalı kadın adlandırması","contextual_glosses":[{"applicability":"Adlandırmanın kadının evlenmesiyle sona erdiğini kabul eden aktarımın bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına yönelik kullanımı ve evlilikte sona erme sınırını korur."},"facet_ids":["F001","F002"],"text":"evlenene dek bu adla anılan kadın","usage_role":"contextual"},{"applicability":"Adlandırmanın evlilikten sonra da sürdüğünü kabul eden karşıt aktarımın bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına yönelik kullanımı ve evlilikten sonra sürme bilgisini korur."},"facet_ids":["F001","F002"],"text":"evlendikten sonra da bu adla anılan kadın","usage_role":"contextual"}],"definition":"Kadına, babasını yitirmiş çocuklara verilen adla seslenilen kalıplaşmış bir kullanımdır. Bir aktarım bu adın evlilikle sona erdiğini, diğeri ise evlilikten sonra da sürdüğünü bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kullanım, babasını yitirmiş çocuklara verilen adın kadın hakkında da söylenmesinden oluşur."},{"facet_id":"F002","role":"source_variant","statement":"Bir aktarımda kadın evlenince bu adlandırma sona erer; karşıt aktarımda ise kadın bu adı hiçbir zaman yitirmez."}],"identity_rationale":"Kaynak ifadesi kocasından ayrılmış kadını tanımlamaz; kadına belirli bir adın verilmesini ve bu adın evlilikle sona erip ermediğine ilişkin iki karşıt aktarımı bildirir. Dal korunabilir, ancak tanımı eşten ayrılma yerine bu kalıplaşmış ve tartışmalı adlandırmaya bağlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"evlenene dek, başka bir aktarıma göre ise evlendikten sonra da babasını yitirmiş çocuk adıyla anılan kadın"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kadınların babasını yitirmiş çocuk adıyla anılabileceğini bildiren söz"}],"lexicalization_note":"Tanım yalnız kadın hakkında kullanılan iki tanıklanmış söz kalıbına bağlıdır; buradan yalın biçime genel bir evlenmemişlik veya eşten ayrılma anlamı aktarılamaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel kadın adlandırmasını eşsiz olma, eşten kopma, ebeveyn kaybı ve eş olma alanlarından ayıran dört aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gerçek medeni durumu tanımlamak yerine özel bir adlandırmayı aktarır; komşu dal ise kişinin eşinin bulunmamasını cinsiyet ayrımı olmadan bildirir.","focus_only":"Odak dal kadınlara verilen özel bir addır ve bir aktarımda evlilikten sonra da sürebilir.","gloss":"kadına verilen özel ad ile eşsiz olma","neighbor_only":"Komşu dal kadın veya erkeğin fiilen eşsiz olmasını ve evlenmeden kalmasını doğrudan anlatır.","neighbor_ref":"root_000073/B001","relation_type":"near_neighbor","shared_zone":"Evlenmemiş kadın, bir aktarımda iki kullanımın ortak bağlamında bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal eşten ayrılmayı gerektirmez; komşu dalın çekirdeği ise eş bağının bulunmaması veya kesilmesidir.","focus_only":"Odak dal evlilik öncesinde kullanılan ve bazı aktarımlarda evlilik sonrasında da süren bir kadın adlandırmasıdır.","gloss":"kadın adlandırması ile eşten kopma","neighbor_only":"Komşu dal eşten kopma, uzun süre eşsiz kalma ve evlenmeme durumunu anlatır.","neighbor_ref":"root_001252/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal kadın ve evlilik durumu çevresinde kullanılabilir."},{"boundary_match":"partial","distinction":"Biçim ortaklığına rağmen odak dalda ebeveyn ölümü kurucu değildir; komşu dalda ise ebeveynin ölümü ve katılımcı ayrımı anlamın temelidir.","focus_only":"Odak dal kadın hakkındaki kalıplaşmış adlandırmayı ve süresine ilişkin aktarım ayrılığını içerir.","gloss":"kadına verilen ad ile ebeveyn kaybı","neighbor_only":"Komşu dal insan çocuğunun babasını ergenlikten önce, hayvan yavrusunun ise annesini yitirmesiyle oluşan gerçek durumu bildirir.","neighbor_ref":"root_001692/B001","relation_type":"near_neighbor","shared_zone":"Kadına verilen ad, babasını yitirmiş çocuk için kullanılan adlandırmayla biçimsel olarak ortaktır."},{"boundary_match":"thematic_only","distinction":"Odak dalın içeriği adlandırmanın süresidir; komşu dalın içeriği ise eşin kendisi ve eş olma bağıdır, bu nedenle anlamsal örtüşme çok sınırlıdır.","focus_only":"Odak dal, kadına yönelik özel bir adın evlilikle sona erip ermediğini tartışır.","gloss":"kadın adlandırması ve eş olma","neighbor_only":"Komşu dal eş olan erkeği, eş olan kadını ve eş olma ilişkisini doğrudan adlandırır.","neighbor_ref":"root_000134/B001","relation_type":"thematic","shared_zone":"İki dal da evlilik ilişkisini çevreleyen söz varlığında yer alır."}],"source_phrase_ar":"المرأة تدعى يتيما ما لم تتزوج فإذا تزوجت زال عنها اسم اليتم؛ يقال للمرأة يتيمة لا يزول عنها اسم اليتم أبدا (tahdhib)","source_qualifications":[{"kind":"disagreement","summary":"Bir aktarım adlandırmayı evlenene kadar sürdürürken diğeri evliliğin bu adı sona erdirmediğini bildirir."}],"source_summary":"Kanıt, kadınlara özgü bu kalıplaşmış adlandırmanın evlilikle ilişkili olduğunu, ancak kullanım süresinin tek biçimde aktarılmadığını gösterir.","sources":["TA"],"what_is_ar":"يدخل فيه إطلاق يتيمة على المرأة عند من يجعله قبل الزواج أو لا يزيله الزواج","what_is_not_ar":"ليس اليتيم من الصبيان ولا كل منفرد من الأشياء ولا أم الأيتام"},"support_links":["sup_c90e2bc134658840580d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000043/B004","candidate_links":[{"candidate_id":"cand_26a441939b3b5b26da0e","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b49412e5d03e69d4b9ba","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Consuming or taking property supplies the inward predatory motion opposed to protective honor.","root":"ء ك ل","source_ref":"89:19","source_word_indices":["1","3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000043","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8cee24f222a125b9f45c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000153/B002","candidate_links":[{"candidate_id":"cand_cd967dac22d4e075b109","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_757c16b381d1d3bc7d78","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Testing that reveals a person's state recasts abundance as disclosure rather than a settled verdict of worth.","root":"ب ل و","source_ref":"89:15","source_word_indices":["5"]},{"hft_ref":"hft_757c16b381d1d3bc7d78","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The repeated revealing test places restriction and abundance within one diagnostic frame.","root":"ب ل و","source_ref":"89:16","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000153","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_fb77551059ebd1b78c9a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000261/B001","candidate_links":[{"candidate_id":"cand_26a441939b3b5b26da0e","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b49412e5d03e69d4b9ba","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Abundance gathered to fullness gives the accumulation mechanism its excessive endpoint.","root":"ج م م","source_ref":"89:20","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000261","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8cee24f222a125b9f45c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000286/B002","candidate_links":[{"candidate_id":"cand_26a441939b3b5b26da0e","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b49412e5d03e69d4b9ba","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Love adhering to the heart supplies the motive that keeps wealth moving toward the possessor.","root":"ح ب ب","source_ref":"89:20","source_word_indices":["1","3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000286","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8cee24f222a125b9f45c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000560/B001","candidate_links":[{"candidate_id":"cand_cd967dac22d4e075b109","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_757c16b381d1d3bc7d78","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"An apportioned gift identifies provision as an allocation whose quantity is being mistaken for personal rank.","root":"ر ز ق","source_ref":"89:16","source_word_indices":["7"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000560","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_fb77551059ebd1b78c9a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000726/B010","candidate_links":[{"candidate_id":"cand_cf949783b5773986924a","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_94c088a14d66919d7af4","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Sustenance that fixes one's place supplies the durable stabilizing outcome of provision.","root":"س ك ن","source_ref":"89:18","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000726","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_cf9234255be709a3c2a1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001205/B004","candidate_links":[{"candidate_id":"cand_cd967dac22d4e075b109","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_757c16b381d1d3bc7d78","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Constriction to a small measure supplies the opposite test condition without making it proof of worthlessness.","root":"ق د ر","source_ref":"89:16","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001205","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_fb77551059ebd1b78c9a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001378/B001","candidate_links":[{"candidate_id":"cand_26a441939b3b5b26da0e","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b49412e5d03e69d4b9ba","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Gathering scattered things into one mass supplies indiscriminate aggregation of shares.","root":"ل م م","source_ref":"89:19","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001378","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8cee24f222a125b9f45c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001457/B001","candidate_links":[{"candidate_id":"cand_26a441939b3b5b26da0e","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b49412e5d03e69d4b9ba","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Acquiring and multiplying property identifies accumulation as the object of attachment.","root":"م و ل","source_ref":"89:20","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001457","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8cee24f222a125b9f45c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001525/B001","candidate_links":[{"candidate_id":"cand_cd967dac22d4e075b109","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_757c16b381d1d3bc7d78","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Good condition and ease supply the prosperous state that the human prematurely equates with honor.","root":"ن ع م","source_ref":"89:15","source_word_indices":["8"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001525","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_fb77551059ebd1b78c9a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001608/B003","candidate_links":[{"candidate_id":"cand_cd967dac22d4e075b109","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_757c16b381d1d3bc7d78","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Humiliation through disparagement supplies the false negative status judgment paired with the false positive honor judgment.","root":"ه و ن","source_ref":"89:16","source_word_indices":["10"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001608","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_fb77551059ebd1b78c9a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001639/B001","candidate_links":[{"candidate_id":"cand_26a441939b3b5b26da0e","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b49412e5d03e69d4b9ba","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Property passing from a predecessor to an heir supplies the transfer point at which an unprotected beneficiary can be displaced.","root":"و ر ث","source_ref":"89:19","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001639","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8cee24f222a125b9f45c"]}],"candidate_inventory":[{"anchor_refs":["89:17"],"branch_refs":["root_000334/B001","root_000726/B006","root_000934/B002","root_001294/B001","root_001692/B001"],"candidate_id":"cand_95f55e75ff4283b2cf84","commentary_obligation":"review","focus_branch_refs":["root_001294/B001","root_001692/B001"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000334/B001","root_000726/B006","root_000934/B002"],"root_ids":[],"scope":"pericope","source_local_id":"B:Feeding the Vulnerable","source_type":"channel","support_ids":["sup_05ed61d0e672388bab55","sup_77e721a081c56d7de638","sup_783e0fa58a9105fff53e","sup_b3c5fc3b3d714fdda050","sup_bb8bf76101e5e3c6257b"],"title":"Feeding the Vulnerable","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:15","89:17","89:20","89:23"],"branch_refs":["root_000286/B003","root_000516/B007","root_001294/B009","root_001525/B003"],"candidate_id":"cand_21cd8c1582ef56c05f3e","commentary_obligation":"review","focus_branch_refs":["root_001294/B009"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000286/B003","root_000516/B007","root_001525/B003"],"root_ids":[],"scope":"pericope","source_local_id":"C:Honor, Reputation, and Approval","source_type":"channel","support_ids":["sup_0af8d287d958b0550415","sup_8982865fc0a86d6261fb","sup_be025e72a745053cc943","sup_f592d95e95bfe57ac9ff","sup_ffe4468f01027f920edc"],"title":"Honor, Reputation, and Approval","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:15","89:17","89:20","89:23","89:24"],"branch_refs":["root_000261/B008","root_000516/B004","root_001272/B001","root_001272/B002"],"candidate_id":"cand_726f3769562d8304973d","commentary_obligation":"review","focus_branch_refs":[],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000261/B008","root_000516/B004","root_001272/B001","root_001272/B002"],"root_ids":[],"scope":"pericope","source_local_id":"C:Utterance, Tongue, and Articulation","source_type":"channel","support_ids":["sup_0f815fdbaf91cf87cada","sup_23a6bfda254aa8d09046","sup_3a8c325854a67d00b3a8","sup_45d1eee3ee93a4268876","sup_58197ae1b9f65fe1dad5"],"title":"Utterance, Tongue, and Articulation","trust":"trusted","unresolved_branch_citations":[{"citation":"ب ل ل/B006","reason":"no registered branch match"}],"unresolved_branch_refs":[]},{"anchor_refs":["89:17","89:28","89:29","89:30"],"branch_refs":["root_000266/B011","root_000464/B009","root_000544/B012"],"candidate_id":"cand_ecaca707605984f08a4c","commentary_obligation":"review","focus_branch_refs":[],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000266/B011","root_000464/B009","root_000544/B012"],"root_ids":[],"scope":"pericope","source_local_id":"D:Bird in Thicket, Cave, and Return","source_type":"channel","support_ids":["sup_64f16d37122b142060d7","sup_b63c198da809829baaa0","sup_b85cf28e97ecf65b519d","sup_c84561bbc48683a753f1","sup_ed71a6efac4104d5326f"],"title":"Bird in Thicket, Cave, and Return","trust":"trusted","unresolved_branch_citations":[{"citation":"ب ل ل/B010","reason":"no registered branch match"}],"unresolved_branch_refs":[]},{"anchor_refs":["89:17","89:22","89:28","89:29"],"branch_refs":["root_000464/B002","root_000544/B004","root_001444/B004","root_001692/B005"],"candidate_id":"cand_52fa281701419a01271b","commentary_obligation":"review","focus_branch_refs":["root_001692/B005"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000464/B002","root_000544/B004","root_001444/B004"],"root_ids":[],"scope":"pericope","source_local_id":"D:Marriage, Consummation, and Marital Return","source_type":"channel","support_ids":["sup_7f46d061a5662674fc4a","sup_bfc5d0fe7326cb2cc286","sup_c90e2bc134658840580d","sup_cd040d17330543c47ce4","sup_d265453c53220d12ae3c"],"title":"Marriage, Consummation, and Marital Return","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:15","89:16","89:17"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:17","branch_refs":["root_000153/B002","root_000560/B001","root_001205/B004","root_001294/B001","root_001525/B001","root_001608/B003","root_001692/B001"],"candidate_id":"cand_cd967dac22d4e075b109","commentary_obligation":"review","hft_ref":"hft_757c16b381d1d3bc7d78","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_honor_metric_relocated","source_type":"hft","support_ids":["sup_fb77551059ebd1b78c9a"],"title":"delta_honor_metric_relocated","trust":"legacy_unbound"},{"anchor_refs":["89:17","89:18"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:17","branch_refs":["root_000334/B001","root_000726/B010","root_000934/B002","root_001294/B001","root_001692/B001"],"candidate_id":"cand_cf949783b5773986924a","commentary_obligation":"review","hft_ref":"hft_94c088a14d66919d7af4","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_collective_provision","source_type":"hft","support_ids":["sup_cf9234255be709a3c2a1"],"title":"delta_collective_provision","trust":"legacy_unbound"},{"anchor_refs":["89:17","89:19","89:20"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:17","branch_refs":["root_000043/B004","root_000261/B001","root_000286/B002","root_001294/B008","root_001378/B001","root_001457/B001","root_001639/B001","root_001692/B001"],"candidate_id":"cand_26a441939b3b5b26da0e","commentary_obligation":"review","hft_ref":"hft_b49412e5d03e69d4b9ba","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_fiduciary_restraint","source_type":"hft","support_ids":["sup_8cee24f222a125b9f45c"],"title":"delta_fiduciary_restraint","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_6532ed6b4b8937d58a41","connection_ref":"conn_6977ae5a8abb2b519185","note":"The next ayah broadens neglect into withholding advocacy for the needy.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_eb019b2beaa5e2c43d63","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:18","source_note":"Adjacent neglect of the orphan joins the focal public-care indictment.","source_row_role":"ranked_review","source_target_component_ref":"89:17","source_target_components":["89:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:17"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:18","source_target_components":["89:18"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:18","target_evidence":{"arabic_uthmani":"وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ","ayah_ref":"89:18"},"target_ref":"89:18"},{"connection_evidence_ref":"conn_ev_d4678aa4d1a2285802f4","connection_ref":"conn_2de24a3a3501b8a2c805","note":"Names consuming attachment to wealth in the same indictment sequence.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_f53918f7f3de5c985033","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:20","source_note":"The immediate context pairs wealth attachment with failure to honor the orphan.","source_row_role":"ranked_review","source_target_component_ref":"89:17","source_target_components":["89:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:17"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:20","source_target_components":["89:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:20","target_evidence":{"arabic_uthmani":"وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا","ayah_ref":"89:20"},"target_ref":"89:20"},{"connection_evidence_ref":"conn_ev_74caef4c9e3a5250c347","connection_ref":"conn_4f8c2c8ee6f27230f20d","note":"Later punishment supplies only a distant consequence within the surah.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_56a55cb15a7748e90c50","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:25","source_note":"Supplies the chapter's neglected-orphan charge before the focus.","source_row_role":"ranked_review","source_target_component_ref":"89:17","source_target_components":["89:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:17"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:25","source_target_components":["89:25"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:25","target_evidence":{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","ayah_ref":"89:25"},"target_ref":"89:25"},{"connection_evidence_ref":"conn_ev_97d9fe59568265c5770e","connection_ref":"conn_fa1ed702743fc550dd56","note":"Directly overturns the claim that constrained provision means humiliation.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_ba4f00b9737526ac6afb","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:16","source_note":"Immediate correction redirects the honor claim to treatment of the orphan.","source_row_role":"ranked_review","source_target_component_ref":"89:17","source_target_components":["89:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:17"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:16","source_target_components":["89:16"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:16","target_evidence":{"arabic_uthmani":"وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ","ayah_ref":"89:16"},"target_ref":"89:16"},{"connection_evidence_ref":"conn_ev_438e29370d83d30835c4","connection_ref":"conn_41a3488f7ec165459841","note":"Exposes indiscriminate inheritance consumption beside the orphan indictment.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_2e50357f6358b0233d1f","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:19","source_note":"Immediate preceding rebuke about al-yatim supplies the vulnerable-rights context.","source_row_role":"ranked_review","source_target_component_ref":"89:17","source_target_components":["89:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:17"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:19","source_target_components":["89:19"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:19","target_evidence":{"arabic_uthmani":"وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا","ayah_ref":"89:19"},"target_ref":"89:19"},{"connection_evidence_ref":"conn_ev_fbe0420117fc2ab8f051","connection_ref":"conn_359de29591ece36310a1","note":"Later belonging in the surah only faintly contrasts social exclusion.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_3538bf0a7943896e03a5","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:29","source_note":"Earlier surah social failure contrasts with the honored acceptance sequence.","source_row_role":"ranked_review","source_target_component_ref":"89:17","source_target_components":["89:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:17"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:29","source_target_components":["89:29"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:29","target_evidence":{"arabic_uthmani":"فَٱدْخُلِى فِى عِبَٰدِى","ayah_ref":"89:29"},"target_ref":"89:29"},{"connection_evidence_ref":"conn_ev_8a34ac77ed9a564db1b4","connection_ref":"conn_e049ac3e72ad0543d6b6","note":"The immediately preceding ayah identifies wealth and ease as a test, not proof of honor.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_4a262d965baa0c40343b","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:15","source_note":"Turns claimed honor into the concrete treatment of the orphan, testing the claim ethically.","source_row_role":"ranked_review","source_target_component_ref":"89:17","source_target_components":["89:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:17"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:15","source_target_components":["89:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:15","target_evidence":{"arabic_uthmani":"فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ","ayah_ref":"89:15"},"target_ref":"89:15"},{"connection_evidence_ref":"conn_ev_1157e3553c1d792dc1db","connection_ref":"conn_3cfd44e0bf77968b8200","note":"Later eschatological remembrance adds only distant consequence.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_84e0075eeb5411483cce","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"89:23","source_note":"Preceding failure toward the orphan supplies moral context for the reckoning.","source_row_role":"ranked_review","source_target_component_ref":"89:17","source_target_components":["89:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:17"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:23","source_target_components":["89:23"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:23","target_evidence":{"arabic_uthmani":"وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ","ayah_ref":"89:23"},"target_ref":"89:23"},{"connection_evidence_ref":"conn_ev_6dd85482ec9a9ec05553","connection_ref":"conn_db9ecb18a41854048d56","note":"Regret over what was sent ahead is only indirect context.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_27353cccdbae263684c5","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:24","source_note":"Failure to honor the orphan begins the local moral indictment.","source_row_role":"ranked_review","source_target_component_ref":"89:17","source_target_components":["89:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:17"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:24","source_target_components":["89:24"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:24","target_evidence":{"arabic_uthmani":"يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى","ayah_ref":"89:24"},"target_ref":"89:24"},{"connection_evidence_ref":"conn_ev_2c44420cc314dd4241d7","connection_ref":"conn_dc8c973b7a7229bd3136","note":"Later entry into the garden does not clarify the focus.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_6701bd02882fc3c21a2e","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:30","source_note":"Failure toward al-yatīm contributes moral contrast only.","source_row_role":"ranked_review","source_target_component_ref":"89:17","source_target_components":["89:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:17"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:30","source_target_components":["89:30"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:30","target_evidence":{"arabic_uthmani":"وَٱدْخُلِى جَنَّتِى","ayah_ref":"89:30"},"target_ref":"89:30"},{"connection_evidence_ref":"conn_ev_41bd9c998b7f1c44a707","connection_ref":"conn_3a0e60bb9e9fc7e0d51d","note":"No focused contribution to the orphan-honor claim.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_7878685cdcedefb2dc6a","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:28","source_note":"No direct addition; it remains in the social-ethical correction before the address.","source_row_role":"ranked_review","source_target_component_ref":"89:17","source_target_components":["89:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:17"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:28","source_target_components":["89:28"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:28","target_evidence":{"arabic_uthmani":"ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ","ayah_ref":"89:28"},"target_ref":"89:28"},{"connection_evidence_ref":"conn_ev_42626541941b11ed0ff3","connection_ref":"conn_6f2cb3ba9f918ab1361e","note":"No focused contribution to the orphan-honor claim.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_c6759c5e4eafac666ac0","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:27","source_note":"Immediate social failure belongs to the direct moral contrast in the surah.","source_row_role":"ranked_review","source_target_component_ref":"89:17","source_target_components":["89:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:17"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:27","source_target_components":["89:27"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:27","target_evidence":{"arabic_uthmani":"يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ","ayah_ref":"89:27"},"target_ref":"89:27"}],"focus":{"arabic_uthmani":"كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ","qac_morphemes":[{"lemma_ar":"كَلَّا","morph_features":"STEM|POS:AVR|LEM:kal~aA","morpheme_role":"STEM","pos":"AVR","qac_ref":"89:17:1:1","qac_word_ref":"89:17:1","root_ar":"","surface_ar":"كَلَّا"},{"lemma_ar":"بَل","morph_features":"STEM|POS:RET|LEM:bal","morpheme_role":"STEM","pos":"RET","qac_ref":"89:17:2:1","qac_word_ref":"89:17:2","root_ar":"","surface_ar":"بَل"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"89:17:3:1","qac_word_ref":"89:17:3","root_ar":"","surface_ar":"لَّا"},{"lemma_ar":"أَكْرَمَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>akorama|ROOT:krm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:17:4:1","qac_word_ref":"89:17:4","root_ar":"ك ر م","surface_ar":"تُكْرِمُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:17:4:2","qac_word_ref":"89:17:4","root_ar":"","surface_ar":"ونَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:17:5:1","qac_word_ref":"89:17:5","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:17:5:2","qac_word_ref":"89:17:5","root_ar":"ي ت م","surface_ar":"يَتِيمَ"}],"word_analysis_qac_refs":[["89:17:1:1"],["89:17:2:1"],["89:17:3:1"],["89:17:4:1","89:17:4:2"],["89:17:5:1","89:17:5:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:17:1","89:17:2","89:17:3","89:17:4","89:17:5"]},"focus_surface_evidence":{"arabic_uthmani":"كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ","qac_morphemes":[{"lemma_ar":"كَلَّا","morph_features":"STEM|POS:AVR|LEM:kal~aA","morpheme_role":"STEM","pos":"AVR","qac_ref":"89:17:1:1","qac_word_ref":"89:17:1","root_ar":"","surface_ar":"كَلَّا"},{"lemma_ar":"بَل","morph_features":"STEM|POS:RET|LEM:bal","morpheme_role":"STEM","pos":"RET","qac_ref":"89:17:2:1","qac_word_ref":"89:17:2","root_ar":"","surface_ar":"بَل"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"89:17:3:1","qac_word_ref":"89:17:3","root_ar":"","surface_ar":"لَّا"},{"lemma_ar":"أَكْرَمَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>akorama|ROOT:krm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:17:4:1","qac_word_ref":"89:17:4","root_ar":"ك ر م","surface_ar":"تُكْرِمُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:17:4:2","qac_word_ref":"89:17:4","root_ar":"","surface_ar":"ونَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:17:5:1","qac_word_ref":"89:17:5","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:17:5:2","qac_word_ref":"89:17:5","root_ar":"ي ت م","surface_ar":"يَتِيمَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:17:1:1"],["89:17:2:1"],["89:17:3:1"],["89:17:4:1","89:17:4:2"],["89:17:5:1","89:17:5:2"]],"word_analysis_refs":["89:17:1","89:17:2","89:17:3","89:17:4","89:17:5"],"word_rows":[{"analysis_record_ref":"89:17:1","analytic_gloss_range_en":"clause-level rebuttal and deterrent particle that rejects the prior evaluation before the corrective replacement clause arrives","analytic_root_gloss_range_en":null,"qac_refs":["89:17:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"كَلَّا","transliteration":"kallā"}},{"analysis_record_ref":"89:17:2","analytic_gloss_range_en":"adversative and resumptive replacement particle that overturns the rejected frame and moves into the negated conduct clause","analytic_root_gloss_range_en":null,"qac_refs":["89:17:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"بَل","transliteration":"bal"}},{"analysis_record_ref":"89:17:3","analytic_gloss_range_en":"indicative negation particle scoping over the imperfect honoring verb and its definite object, reporting an existing failure rather than issuing a prohibition","analytic_root_gloss_range_en":null,"qac_refs":["89:17:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَّا","transliteration":"lā"}},{"analysis_record_ref":"89:17:4","analytic_gloss_range_en":"second-person plural Form IV active imperfect: to confer honor, dignity, generous treatment, and public worth on an explicit recipient, here negated as a recurring communal failure","analytic_root_gloss_range_en":"broad range centered on nobility, generosity, preciousness, honored status, and conferral of honor; local Form IV with a direct object selects conferred honoring, not unrelated grapevine, adornment, vessel-cover, or bone branches","qac_refs":["89:17:4:1","89:17:4:2"],"root":{"arabic":"ك ر م","transliteration":"k-r-m"},"surface":{"arabic":"تُكْرِمُونَ","transliteration":"tukrimūna"}},{"analysis_record_ref":"89:17:5","analytic_gloss_range_en":"definite singular accusative orphan object: the socially exposed, cut-off dependent who receives the pressure of the negated honoring clause","analytic_root_gloss_range_en":"root range includes orphanhood through loss of protecting parent, cut-off isolation, solitary uniqueness, falling short, delay, and disputed marriage-related uses; this ayah selects the orphaned and unsupported person as the concrete object","qac_refs":["89:17:5:1","89:17:5:2"],"root":{"arabic":"ي ت م","transliteration":"y-t-m"},"surface":{"arabic":"ٱلْيَتِيمَ","transliteration":"al-yatīma"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":6,"missing_anchor_refs":[],"supplied_unique_anchor_count":6},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["89:15","89:16","89:17"],"branch_refs":["root_000153/B002","root_000560/B001","root_001205/B004","root_001294/B001","root_001525/B001","root_001608/B003","root_001692/B001"],"candidate_id":"cand_cd967dac22d4e075b109","evidence_scope":"declared_pericope","hft_ref":"hft_757c16b381d1d3bc7d78","item_id":"delta_honor_metric_relocated","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_honor_metric_relocated","support_id":"sup_fb77551059ebd1b78c9a"},{"anchor_refs":["89:17","89:18"],"branch_refs":["root_000334/B001","root_000726/B010","root_000934/B002","root_001294/B001","root_001692/B001"],"candidate_id":"cand_cf949783b5773986924a","evidence_scope":"declared_pericope","hft_ref":"hft_94c088a14d66919d7af4","item_id":"delta_collective_provision","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_collective_provision","support_id":"sup_cf9234255be709a3c2a1"},{"anchor_refs":["89:17","89:19","89:20"],"branch_refs":["root_000043/B004","root_000261/B001","root_000286/B002","root_001294/B008","root_001378/B001","root_001457/B001","root_001639/B001","root_001692/B001"],"candidate_id":"cand_26a441939b3b5b26da0e","evidence_scope":"declared_pericope","hft_ref":"hft_b49412e5d03e69d4b9ba","item_id":"delta_fiduciary_restraint","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_fiduciary_restraint","support_id":"sup_8cee24f222a125b9f45c"}],"diagnostics":[],"lane_counts":{"global":14,"macro":3,"micro":4},"packet_summary":{"ayah_count":30,"focus_ref":"89:17","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:17","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":12,"unstructured_record_count":0},"identity":{"ayah_ref":"89:17","lane":"macro","linguistic_source_ref":"89:17","surface_ref":"89:17","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:17","target_tokens":[["Hayır",["89:17:1"]],["Aksine",["89:17:2"]],["siz",["89:17:4"]],["yetime",["89:17:5"]],["değer",["89:17:4"]],["vermiyorsunuz",["89:17:3","89:17:4"]]],"text":"Hayır! Aksine siz yetime değer vermiyorsunuz."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":15,"ayah_to":30,"id":"s089-p02-015-030","label":"The wealth test, judgment, and tranquil soul","number":2,"refs":["89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"89:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"89:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["89:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"89:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Feeding the Vulnerable","source_type":"channel","support_id":"sup_05ed61d0e672388bab55","text":"Need, food, exhortation, and honor form a welfare scene in which dignity is enacted through provision.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Honor, Reputation, and Approval","source_type":"channel","support_id":"sup_0af8d287d958b0550415","text":"89:23 (الذكرى); 89:20 (حبا); 89:15, 89:17 (أكرم); 89:15 (نعمه)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Utterance, Tongue, and Articulation","source_type":"channel","support_id":"sup_0f815fdbaf91cf87cada","text":"Content, organ, articulation quality, and social mention form one speech-production scene.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Utterance, Tongue, and Articulation","source_type":"channel","support_id":"sup_23a6bfda254aa8d09046","text":"89:15-16, 89:24 (يقول); 89:17 (بل); 89:20 (جما); 89:23 (الذكرى)","trust":"trusted"},{"branch_refs":["root_000261/B008","root_000516/B004","root_001272/B001","root_001272/B002"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"C:Utterance, Tongue, and Articulation","source_type":"channel","support_id":"sup_3a8c325854a67d00b3a8","text":"utterance `ق و ل:B001/m01`; tongue or articulator `ق و ل:B002/m01`; clear articulation `ب ل ل:B006/m01`; unclear speech `ج م م:B008/m01`; mention `ذ ك ر:B004/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Utterance, Tongue, and Articulation","source_type":"channel","support_id":"sup_45d1eee3ee93a4268876","text":"An intended proposition is shaped by the tongue into audible speech.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Utterance, Tongue, and Articulation","source_type":"channel","support_id":"sup_58197ae1b9f65fe1dad5","text":"Language connects speaker, proposition, answer, and referent through distinct discourse operations.","trust":"trusted"},{"branch_refs":["root_000266/B011","root_000464/B009","root_000544/B012"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"D:Bird in Thicket, Cave, and Return","source_type":"channel","support_id":"sup_64f16d37122b142060d7","text":"bird habitat in cave or tree `د خ ل:B009/m01`; dense cover `ج ن ن:B011/m01`; returning birds `ر ج ع:B012/m01`; nightingale-like call `ب ل ل:B010/m01`","trust":"trusted"},{"branch_refs":["root_000334/B001","root_000726/B006","root_000934/B002","root_001294/B001","root_001692/B001"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"B:Feeding the Vulnerable","source_type":"channel","support_id":"sup_77e721a081c56d7de638","text":"mutual urging `ح ض ض:B001/m01`; feeding `ط ع م:B002/m01`; poverty and humility `س ك ن:B006/m01`; orphanhood `ي ت م:B001/m01`; generous honor `ك ر م:B001/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Feeding the Vulnerable","source_type":"channel","support_id":"sup_783e0fa58a9105fff53e","text":"Goods acquire moral and social meaning through allotment, withholding, transfer, and use.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Marriage, Consummation, and Marital Return","source_type":"channel","support_id":"sup_7f46d061a5662674fc4a","text":"89:29-30 (ادخلي); 89:22 (الملك); 89:28 (ارجعي); 89:17 (اليتيم)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Honor, Reputation, and Approval","source_type":"channel","support_id":"sup_8982865fc0a86d6261fb","text":"Praiseworthy action produces mention, reputation, and an approving response.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Feeding the Vulnerable","source_type":"channel","support_id":"sup_b3c5fc3b3d714fdda050","text":"Community members urge one another to feed a poor or dependent person.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Bird in Thicket, Cave, and Return","source_type":"channel","support_id":"sup_b63c198da809829baaa0","text":"Shelter, movement, return, and call define a habitat cycle rather than a generic wildlife grouping.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Bird in Thicket, Cave, and Return","source_type":"channel","support_id":"sup_b85cf28e97ecf65b519d","text":"Animal life is organized through habitat, herd movement, breeding, and distinctive body parts.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Feeding the Vulnerable","source_type":"channel","support_id":"sup_bb8bf76101e5e3c6257b","text":"89:17-18 (تكرمون اليتيم، تحاضون، طعام المسكين)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Honor, Reputation, and Approval","source_type":"channel","support_id":"sup_be025e72a745053cc943","text":"Conduct circulates as public mention and returns to the actor as praise or approval.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Marriage, Consummation, and Marital Return","source_type":"channel","support_id":"sup_bfc5d0fe7326cb2cc286","text":"Life is carried forward through gestation, birth, marriage, guardianship, and care for dependents.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Bird in Thicket, Cave, and Return","source_type":"channel","support_id":"sup_c84561bbc48683a753f1","text":"A bird shelters in a cave or dense tree cover, leaves, and returns by a familiar route.","trust":"trusted"},{"branch_refs":["root_000464/B002","root_000544/B004","root_001444/B004","root_001692/B005"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"D:Marriage, Consummation, and Marital Return","source_type":"channel","support_id":"sup_c90e2bc134658840580d","text":"consummation `د خ ل:B002/m01`; marriage contract `م ل ك:B004/m01`; marital return `ر ج ع:B004/m01`; woman without spouse `ي ت م:B005/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Marriage, Consummation, and Marital Return","source_type":"channel","support_id":"sup_cd040d17330543c47ce4","text":"Contract, sexual entry, separation status, and return form one legal and domestic marriage frame.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Marriage, Consummation, and Marital Return","source_type":"channel","support_id":"sup_d265453c53220d12ae3c","text":"A marriage contract permits entry and consummation, while separation may be reversed by marital return.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Bird in Thicket, Cave, and Return","source_type":"channel","support_id":"sup_ed71a6efac4104d5326f","text":"89:29-30 (ادخلي); 89:30 (جنتي); 89:28 (ارجعي); 89:17 (بل)","trust":"trusted"},{"branch_refs":["root_000286/B003","root_000516/B007","root_001294/B009","root_001525/B003"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"C:Honor, Reputation, and Approval","source_type":"channel","support_id":"sup_f592d95e95bfe57ac9ff","text":"reputation `ذ ك ر:B007/m01`; praise or desire `ح ب ب:B003/m01`; approving response `ك ر م:B009/m01`; commendation `ن ع م:B003/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Honor, Reputation, and Approval","source_type":"channel","support_id":"sup_ffe4468f01027f920edc","text":"Inner disposition becomes socially legible through conduct, generosity, reputation, imitation, or corruption.","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ","ayah_ref":"89:15"},{"arabic_uthmani":"وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ","ayah_ref":"89:16"},{"arabic_uthmani":"كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ","ayah_ref":"89:17"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000153/B002","root_000560/B001","root_001205/B004","root_001294/B001","root_001525/B001","root_001608/B003","root_001692/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001294","role":"Praiseworthy generosity anchors the corrected honor metric in the addressed group's conduct.","root":"ك ر م","source_ref":"89:17","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001692","role":"The child lacking a protector becomes the concrete recipient by whom the new metric is tested.","root":"ي ت م","source_ref":"89:17","source_word_indices":["5"]},{"branch_id":"B002","mapped_root_id":"root_000153","role":"Testing that reveals a person's state recasts abundance as disclosure rather than a settled verdict of worth.","root":"ب ل و","source_ref":"89:15","source_word_indices":["5"]},{"branch_id":"B002","mapped_root_id":"root_000153","role":"The repeated revealing test places restriction and abundance within one diagnostic frame.","root":"ب ل و","source_ref":"89:16","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001294","role":"Honor and generosity appear both as an event and as the human's self-interested report, creating the term that verse 17 corrects.","root":"ك ر م","source_ref":"89:15","source_word_indices":["7","11"]},{"branch_id":"B001","mapped_root_id":"root_001525","role":"Good condition and ease supply the prosperous state that the human prematurely equates with honor.","root":"ن ع م","source_ref":"89:15","source_word_indices":["8"]},{"branch_id":"B004","mapped_root_id":"root_001205","role":"Constriction to a small measure supplies the opposite test condition without making it proof of worthlessness.","root":"ق د ر","source_ref":"89:16","source_word_indices":["5"]},{"branch_id":"B001","mapped_root_id":"root_000560","role":"An apportioned gift identifies provision as an allocation whose quantity is being mistaken for personal rank.","root":"ر ز ق","source_ref":"89:16","source_word_indices":["7"]},{"branch_id":"B003","mapped_root_id":"root_001608","role":"Humiliation through disparagement supplies the false negative status judgment paired with the false positive honor judgment.","root":"ه و ن","source_ref":"89:16","source_word_indices":["10"]}],"changed_reading":{"after":"The proof of honor is not receiving abundance but converting whatever agency one has into dignity for the person deprived of protection.","before":"You fail at one obligation after misdescribing prosperity and scarcity."},"confidence":"strong","mechanism":"The paired tests stage abundance and restricted provision, followed by human reports of personal honor and humiliation. The correction then relocates honor from what one receives under testing to what one does with social power toward the unprotected: possession is not the metric; dignity-producing distribution is.","model_id":"delta_honor_metric_relocated","reader_inference":"The packet supplies paired tests, opposed self-reports, and the corrective transition; I infer that orphan-treatment is the criterion that overturns the reports. A live alternative is that verse 17 merely adds a separate vice rather than redefining honor.","status":"revised","structural_cues":["89:15 and 89:16 are matched test-and-report clauses, one expansive and one restrictive.","89:17 opens with both rejection and redirection before switching from what the human receives to what the plural addressees do."],"trigger_roots":["ب ل و","ك ر م","ن ع م","ق د ر","ر ز ق","ه و ن"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_honor_metric_relocated","source_type":"hft","support_id":"sup_fb77551059ebd1b78c9a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ","ayah_ref":"89:17"},{"arabic_uthmani":"وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ","ayah_ref":"89:18"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000334/B001","root_000726/B010","root_000934/B002","root_001294/B001","root_001692/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001294","role":"Generosity supplies the active social good that the plural group withholds.","root":"ك ر م","source_ref":"89:17","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001692","role":"Lost protection supplies the vulnerability that requires a network rather than a passing courtesy.","root":"ي ت م","source_ref":"89:17","source_word_indices":["5"]},{"branch_id":"B001","mapped_root_id":"root_000334","role":"Urging toward an action makes peer reinforcement part of the failed communal mechanism.","root":"ح ض ض","source_ref":"89:18","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000934","role":"Feeding another turns honor from an abstract status word into material transfer.","root":"ط ع م","source_ref":"89:18","source_word_indices":["4"]},{"branch_id":"B010","mapped_root_id":"root_000726","role":"Sustenance that fixes one's place supplies the durable stabilizing outcome of provision.","root":"س ك ن","source_ref":"89:18","source_word_indices":["5"]}],"changed_reading":{"after":"The group must produce and reinforce a provisioning norm that gives the unprotected durable material footing.","before":"Each person should privately show generosity to an orphan."},"confidence":"strong","mechanism":"The adjacent plural failures link direct honoring to mutual social pressure around feeding. Care is therefore not exhausted by a donor-recipient gesture: a community honors the exposed by making provision a reproduced norm and by supplying sustenance that stabilizes life.","model_id":"delta_collective_provision","reader_inference":"The packet supplies plural negations, urging, food, and stabilizing sustenance; I infer a causal chain from mutual encouragement to durable provision. The live alternative is that honoring and feeding remain parallel duties without an institutional link.","status":"strengthened","structural_cues":["89:17 and 89:18 are adjacent coordinated negations addressed to the same plural group.","The participatory morphology of the urging verb makes failure to mobilize one another distinct from failure to feed alone."],"trigger_roots":["ح ض ض","ط ع م","س ك ن"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_collective_provision","source_type":"hft","support_id":"sup_cf9234255be709a3c2a1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ","ayah_ref":"89:17"},{"arabic_uthmani":"وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا","ayah_ref":"89:19"},{"arabic_uthmani":"وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا","ayah_ref":"89:20"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000043/B004","root_000261/B001","root_000286/B002","root_001294/B008","root_001378/B001","root_001457/B001","root_001639/B001","root_001692/B001"],"payload":{"activation_trace":[{"branch_id":"B008","mapped_root_id":"root_001294","role":"The recompense-seeking gift exposes outward generosity that can coexist with self-serving acquisition.","root":"ك ر م","source_ref":"89:17","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001692","role":"Loss of a protecting parent supplies the legal and social exposure that makes stewardship decisive.","root":"ي ت م","source_ref":"89:17","source_word_indices":["5"]},{"branch_id":"B004","mapped_root_id":"root_000043","role":"Consuming or taking property supplies the inward predatory motion opposed to protective honor.","root":"ء ك ل","source_ref":"89:19","source_word_indices":["1","3"]},{"branch_id":"B001","mapped_root_id":"root_001639","role":"Property passing from a predecessor to an heir supplies the transfer point at which an unprotected beneficiary can be displaced.","root":"و ر ث","source_ref":"89:19","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001378","role":"Gathering scattered things into one mass supplies indiscriminate aggregation of shares.","root":"ل م م","source_ref":"89:19","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000286","role":"Love adhering to the heart supplies the motive that keeps wealth moving toward the possessor.","root":"ح ب ب","source_ref":"89:20","source_word_indices":["1","3"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Acquiring and multiplying property identifies accumulation as the object of attachment.","root":"م و ل","source_ref":"89:20","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000261","role":"Abundance gathered to fullness gives the accumulation mechanism its excessive endpoint.","root":"ج م م","source_ref":"89:20","source_word_indices":["4"]}],"changed_reading":{"after":"Honoring first means not absorbing what should remain protected for the orphan; stewardship precedes display.","before":"Honoring the orphan means adding a generous gift."},"confidence":"strong","mechanism":"The orphan's severed protector makes assets transferred after a predecessor especially vulnerable. The following sequence moves property inward by consuming transferred wealth, gathering it indiscriminately, and loving accumulated assets. Against that flow, honoring becomes fiduciary restraint: preserving the exposed person's share rather than offering ceremonial generosity after appropriation.","model_id":"delta_fiduciary_restraint","reader_inference":"The packet supplies parental severance followed by inherited wealth, consumption, aggregation, and love of property; I infer heightened fiduciary exposure and a duty to preserve the orphan's share. The live alternative is a general critique of greed with no specific estate relation.","status":"strengthened","structural_cues":["89:17-20 forms a continuous plural indictment that moves from the unprotected recipient to food, inherited property, and amassed wealth.","The orphan's loss of a parent precedes the explicit inheritance vocabulary without the packet explicitly naming the orphan's own estate."],"trigger_roots":["ء ك ل","و ر ث","ل م م","ح ب ب","م و ل","ج م م"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_fiduciary_restraint","source_type":"hft","support_id":"sup_8cee24f222a125b9f45c","trust":"legacy_unbound"}]}
</lane_packet_json>
