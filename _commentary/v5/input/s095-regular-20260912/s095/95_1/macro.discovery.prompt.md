# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **95:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s095-regular-20260912/s095/95_1/macro.discovery.json` and modify nothing
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
  "ayah_ref": "95:1",
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
{"branch_registry":[{"boundary":"Human beings or human presence: ins, humans, people, anasi, insan as a person or group, and anis meaning anyone present in a dwelling.","branch_kind":null,"branch_ref":"root_000059/B001","candidate_links":[{"candidate_id":"cand_2b6dfb92fca330bba11a","lane":"macro"},{"candidate_id":"cand_f532461f05b2eb1eec37","lane":"macro"},{"candidate_id":"cand_fdf8a65d88b5fe260f1a","lane":"macro"}],"focus_root_occurrences":[],"gloss":"visible human presence over against hidden or wild beings","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"ظهور الإنسان المخالف للتوحش والجن","image_en":"visible human presence over against hidden or wild beings"}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"ظهور الإنسان المخالف للتوحش والجن","image_en":"visible human presence over against hidden or wild beings","scope_ar":"يدخل فيه الإنس والبشر والناس والأناسي والإنسان من حيث الجماعة أو الواحد، وما بالدار أنيس بمعنى أحد.","scope_en":"Human beings or human presence: ins, humans, people, anasi, insan as a person or group, and anis meaning anyone present in a dwelling."},"support_links":["sup_11c5980695cc480bba28","sup_1342c3eb7ecbfe914bb9","sup_181c3eec5c4b2950e49a"]},{"boundary":"Bu dal yenilebilir meyveyle sınırlıdır; yer adı veya kurt adı kullanımını kapsamaz.","branch_kind":"bare","branch_ref":"root_000190/B001","candidate_links":[{"candidate_id":"cand_48990720f3b6373c54a3","lane":"macro"},{"candidate_id":"cand_1ed8409f637f78bdb575","lane":"macro"},{"candidate_id":"cand_3ca0913747e037aad56b","lane":"macro"},{"candidate_id":"cand_7a61eae3b729c2a8c371","lane":"macro"},{"candidate_id":"cand_5b549f19ba0d0adf50ea","lane":"macro"},{"candidate_id":"cand_6b14a928608c23465e5f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"تِّين","morph_features":"STEM|POS:N|LEM:t~iyn|ROOT:tyn|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:1:1:3","qac_word_ref":"95:1:1","surface_ar":"تِّينِ"}],"gloss":"yenilebilir incir meyvesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam bilinen ve yenilebilir incir meyvesidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Meyvenin taze veya kuru yenebilir olması anlam sınırını açıklar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tekil kullanımdaki biçim bir adet incir meyvesini gösterir."}}],"root_ar":"ت ي ن","root_id":"root_000190","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Meyvenin kendisini, yenebilirliğini ve tekil meyve kullanımını birlikte temsil eden en kısa doğal karşılıktır.","boundary_detail":"Bu dal yenilebilir meyveyle sınırlıdır; yer adı veya kurt adı kullanımını kapsamaz.","branch_image_ar":"ثمرة التين المأكولة","concept_gloss":"yenilebilir incir meyvesi","contextual_glosses":[{"applicability":"Sıradan bağlamda yenilen meyve kastedildiğinde doğal Türkçe karşılıktır.","error_profile":{"adds":"Türkçede bağlama göre ağaç veya ürün adı olarak da anlaşılabilir.","collision":"Yer adı veya başka özel kullanım bağlamı açık değilse karışma oluşabilir.","fit":"broadening","loses":null,"preserves":"Meyvenin bilinen adını korur."},"facet_ids":["F001","F002"],"text":"incir","usage_role":"general"},{"applicability":"Tekil meyve sayımı veya bir adet meyvenin belirtilmesi gerektiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tekil meyve değerini ve yenilebilir incir çekirdeğini korur."},"facet_ids":["F001","F003"],"text":"bir incir meyvesi","usage_role":"contextual"}],"definition":"Bu dal, bilinen yenilebilir incir meyvesini kapsar; meyvenin taze ya da kuru yenmesi ve tek bir meyve olarak sayılması bu çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam bilinen ve yenilebilir incir meyvesidir."},{"facet_id":"F002","role":"associated_use","statement":"Meyvenin taze veya kuru yenebilir olması anlam sınırını açıklar."},{"facet_id":"F003","role":"specialization","statement":"Tekil kullanımdaki biçim bir adet incir meyvesini gösterir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Ağaç anlamını ekler.","collision":null,"fit":"displacement","loses":"Yenilebilir meyvenin kendisini merkeze almaktan çıkarır.","preserves":"İncir alanıyla bağlantıyı korur."},"text":"incir ağacı"}],"identity_rationale":"Kaynak ifadesi bu dalı bilinen yenilebilir incir meyvesi olarak kuruyor; meyvenin taze veya kuru yenmesi ve tekil meyve biçimi aynı çekirdeğin içindedir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"taze veya kuru yenilen bilinen incir meyvesi"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tek bir incir meyvesi"}],"lexicalization_note":"Mekanik kapsam bare olduğu için tanım çıplak meyve anlamını verir ve başka dala ait özel ad kullanımlarını içeri almaz.","neighbor_coverage_note":"Aday komşular içinde meyve alanındaki yakınlıklar ve aynı kök içindeki eşbiçimli karışmalar sınırı en çok keskinleştirir; diğer meyve adları aynı alanı paylaşsa da tekrarlı kalır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda çekirdek doğrudan yenilen incirdir; komşu dal ise belirli olgunluk, benzerlik veya aktarım bağlamıyla sınırlı olduğu için tam ikame edilemez.","focus_only":"Bu dal bilinen incir meyvesinin kendisini çıplak meyve anlamı olarak verir.","gloss":"incir meyvesi ile incir benzeri","neighbor_only":"Komşu dal olgunlaşmış incir meyvesi veya incire benzeyen şey gibi daha özel ya da benzetmeli bir alan taşır.","neighbor_ref":"root_000149/B006","relation_type":"near_neighbor","shared_zone":"İki dal da incir meyvesi çevresinde okuyucu karışıklığı oluşturabilir."},{"boundary_match":"field_only","distinction":"Paylaşılan alan meyve adıdır; referans nesneleri farklı meyveler olduğu için anlam çekirdeği ortak değildir.","focus_only":"Bu dal incir meyvesidir.","gloss":"incir ile başka meyve","neighbor_only":"Komşu dal başka bir bilinen meyveyi gösterir.","neighbor_ref":"root_000602/B001","relation_type":"same_field","shared_zone":"İki dal yenilebilir meyve adları alanında buluşur."},{"boundary_match":"thematic_only","distinction":"Odak dalın referenti yenilen meyvedir; komşu dal coğrafi veya mekansal adlandırmadır ve meyve anlamıyla ikame edilemez.","focus_only":"Bu dal yenilebilir meyveyi gösterir.","gloss":"meyve ile yer adı","neighbor_only":"Komşu dal aynı ifadenin yer, dağ veya yapı adı olarak anlaşılmasını kapsar.","neighbor_ref":"root_000190/B002","relation_type":"other","shared_zone":"Aynı ifade farklı dallarda geçtiği için biçimsel karışma olabilir."},{"boundary_match":"thematic_only","distinction":"Meyve adı ile hayvan adı arasında ortak semantik çekirdek yoktur; ayrım yalnızca eşbiçimli veya yakın biçimli adlandırmadan doğar.","focus_only":"Bu dal incir meyvesini adlandırır.","gloss":"meyve ile kurt adı","neighbor_only":"Komşu dal bazı konuşma biçimlerinde kurt için kullanılan ayrı bir addır.","neighbor_ref":"root_000190/B003","relation_type":"other","shared_zone":"Yakın biçimli kullanımlar aynı kök paketi içinde yer alır."}],"source_phrase_ar":"التين وهو معروف (maqayis)؛ والتين ثمر معروف (jamhara)؛ التين هذا الذي يؤكل رطبا ويابسا الواحدة تينة (sihah)؛ هو تينكم هذا وزيتونكم (tahdhib)؛ هما المأكولان (mufradat)","source_summary":"Kaynaklar bu dalda yenilen bilinen incir meyvesini ortak çekirdek olarak verir; bazı aktarım ayrıntıları meyvenin taze ve kuru yenmesine ve tekil meyve biçimine işaret eder.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه التين المعروف وثمرته التي تؤكل رطبا ويابسا والواحدة تينة","what_is_not_ar":"ليس موضعا جبليا ولا اسما للذئب"},"support_links":["sup_2ebba7b49bcbd77a091a","sup_5c78b35c82ed9c19b66d","sup_6258318b0372247b0d28","sup_6925fdadbc27aa33354d","sup_78430e46ce7bffb30fff","sup_d3fa10a303f4b206eb8c"]},{"boundary":"Bu dal meyve anlamından ayrıdır; dağ yorumu merkezidir ama tek desteklenen biçim değildir.","branch_kind":"bare","branch_ref":"root_000190/B002","candidate_links":[{"candidate_id":"cand_6c8d69e8b79051eb3910","lane":"macro"},{"candidate_id":"cand_29f737daf46242eee0af","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"تِّين","morph_features":"STEM|POS:N|LEM:t~iyn|ROOT:tyn|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:1:1:3","qac_word_ref":"95:1:1","surface_ar":"تِّينِ"}],"gloss":"yer veya dağ adı","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, ifadenin yenilen meyve yerine bir mekan adı olarak kullanılmasıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı aktarımlar bunu tek dağ, iki dağ veya dağlar olarak açıklar."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka aktarım biçimleri iki ibadet yeri veya belirli bir bölgesel mekan anlayışını içerir."}}],"root_ar":"ت ي ن","root_id":"root_000190","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Meyve dışı mekan adlandırmasını ve dağ merkezli varyantları kısa biçimde birlikte verir.","boundary_detail":"Bu dal meyve anlamından ayrıdır; dağ yorumu merkezidir ama tek desteklenen biçim değildir.","branch_image_ar":"موضع التين من الجبال","concept_gloss":"yer veya dağ adı","contextual_glosses":[{"applicability":"Kaynak bağlamında dağ veya dağlar yorumu öne çıktığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki ibadet yeri veya genel bölgesel mekan yorumu dışarıda kalır.","preserves":"Dağla ilgili mekan adlandırmasını korur."},"facet_ids":["F001","F002"],"text":"dağ adı","usage_role":"contextual"},{"applicability":"Dağ, yapı ve yer varyantlarının tamamını meyve dışı adlandırma olarak açıklamak için uygundur.","error_profile":{"adds":"Dağ veya ibadet yeri olarak sınırlanmayan daha genel yer adı alanını ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Meyve dışı yer adı çekirdeğini korur."},"facet_ids":["F001","F002","F003"],"text":"mekan adı","usage_role":"explanatory"}],"definition":"Bu dal, aynı ifadenin meyve adı değil, dağ, iki dağ, dağlar, iki ibadet yeri veya bölgesel mekan adı olarak anlaşılmasını kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, ifadenin yenilen meyve yerine bir mekan adı olarak kullanılmasıdır."},{"facet_id":"F002","role":"source_variant","statement":"Bazı aktarımlar bunu tek dağ, iki dağ veya dağlar olarak açıklar."},{"facet_id":"F003","role":"source_variant","statement":"Başka aktarım biçimleri iki ibadet yeri veya belirli bir bölgesel mekan anlayışını içerir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yenilebilir meyve anlamını ekler.","collision":"Birinci dalın meyve anlamıyla doğrudan çakışır.","fit":"displacement","loses":"Mekan veya dağ adı çekirdeğini bütünüyle kaybeder.","preserves":"Aynı ifade ailesiyle biçimsel bağı korur."},"text":"incir meyvesi"}],"identity_rationale":"Kaynak ifadesi dalı yalnızca dağ olarak değil, dağ, iki dağ, dağlar, iki ibadet yeri ve bölgesel mekan adı gibi yerle bağlantılı yorumlar halinde verir. Bu yüzden dal korunur, fakat tanım dar bir dağ anlamı yerine yer veya mekan adı çerçevesinde kurulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yer, dağ veya bölgesel mekan adı"}],"lexicalization_note":"Mekanik kapsam bare olduğu için ifade çıplak adlandırma olarak ele alınır; meyve dalından veya kurt adı dalından anlam aktarılmaz.","neighbor_coverage_note":"Yayınlanan komşular mekan adı sınırını ve aynı kök içindeki meyve ile hayvan adı karışmasını gösterir; diğer dağ veya yer adı adayları aynı alanı tekrarlar.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal yalnızca dağla sınırlı değildir ve aynı ifade etrafındaki farklı mekan yorumlarını içerir; komşu dalın çekirdeği dağ adlandırmasıdır.","focus_only":"Bu dal belirli ifade için yer, dağ, dağlar veya ibadet yeri yorumlarını taşır.","gloss":"yer adı ile dağ adı","neighbor_only":"Komşu dal dağ için genel veya belirli bir adlandırma alanını taşır.","neighbor_ref":"root_000955/B005","relation_type":"same_field","shared_zone":"İki dal da dağ veya yer adı alanında değerlendirilir."},{"boundary_match":"field_only","distinction":"Odak dalın varyantları mekan ekseninde kalır; komşu dalın kapsamı yer dışı adlandırmalara da uzanır.","focus_only":"Bu dal dağ veya mekan adı olarak aynı ifadeye bağlıdır.","gloss":"mekan adı alanı","neighbor_only":"Komşu dal yer adının yanında topluluk veya burç gibi başka adlandırmaları da içerir.","neighbor_ref":"root_000210/B006","relation_type":"same_field","shared_zone":"İki dal özel adlandırma ve yer adı alanında kesişir."},{"boundary_match":"thematic_only","distinction":"Mekan adı yorumu yenilen meyveye indirgenemez; iki dal aynı biçim çevresinde eşadlı ayrım oluşturur.","focus_only":"Bu dal meyve dışı mekan adıdır.","gloss":"yer adı ile meyve","neighbor_only":"Komşu dal yenilen incir meyvesidir.","neighbor_ref":"root_000190/B001","relation_type":"other","shared_zone":"Aynı ifade iki ayrı dalda farklı referentlerle kullanılabilir."},{"boundary_match":"thematic_only","distinction":"Yer veya mekan adı ile hayvan adı arasında semantik ikame yoktur; ayrım farklı referent alanlarından doğar.","focus_only":"Bu dal yer veya dağ adlandırmasıdır.","gloss":"yer adı ile hayvan adı","neighbor_only":"Komşu dal kurt için kullanılan ayrı addır.","neighbor_ref":"root_000190/B003","relation_type":"other","shared_zone":"Aynı kök paketi içinde farklı adlandırma alanları yer alır."}],"source_phrase_ar":"والتين جبل (maqayis;jamhara)؛ جبلان بالشأم (sihah)؛ مسجدان بالشام (tahdhib)؛ التين جبال ما بين حلوان إلى همذان (tahdhib)؛ قيل هما جبلان (mufradat)","source_summary":"Kaynakların ortak malzemesi bu dalı meyve dışı bir yer veya mekan adı olarak ele alır; ayrıntılarda tek dağ, iki dağ, dağlar ve iki ibadet yeri gibi yorumlar bulunur.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه تفسير التين بأنه جبل أو جبلان أو جبال أو موضعان بالشام","what_is_not_ar":"ليس الثمرة المأكولة ولا اسم الذئب"},"support_links":["sup_0d18cf4245f1d374233c","sup_82800c2b4f9d548de6ae"]},{"boundary":"Bu dal yalnızca kurt adı kullanımını kapsar ve meyve ile mekan dallarından ayrıdır.","branch_kind":"bare","branch_ref":"root_000190/B003","candidate_links":[{"candidate_id":"cand_2b6dfb92fca330bba11a","lane":"macro"},{"candidate_id":"cand_fdf8a65d88b5fe260f1a","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"تِّين","morph_features":"STEM|POS:N|LEM:t~iyn|ROOT:tyn|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:1:1:3","qac_word_ref":"95:1:1","surface_ar":"تِّينِ"}],"gloss":"kurt için ad","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam kurt için kullanılan bir ad olmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanım bütün dil alanına değil, bazı konuşma biçimlerine bağlanır."}}],"root_ar":"ت ي ن","root_id":"root_000190","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın türünü ve bunun sıradan niteleme değil adlandırma olduğunu birlikte verir.","boundary_detail":"Bu dal yalnızca kurt adı kullanımını kapsar ve meyve ile mekan dallarından ayrıdır.","branch_image_ar":"ذئب يسمى تِينان","concept_gloss":"kurt için ad","contextual_glosses":[{"applicability":"Okura bunun hayvan türü değil, o hayvan için kullanılan ad olduğunu göstermek gerektiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kurt referentini ve ad olma değerini korur."},"facet_ids":["F001","F002"],"text":"kurt adı","usage_role":"explanatory"}],"definition":"Bu dal, bazı konuşma biçimlerinde kurt için kullanılan bir adlandırmayı kapsar; meyve veya yer adı değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam kurt için kullanılan bir ad olmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Kullanım bütün dil alanına değil, bazı konuşma biçimlerine bağlanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yenilebilir meyve anlamını ekler.","collision":"Birinci dalın meyve anlamıyla çakışır.","fit":"displacement","loses":"Kurt adı olma çekirdeğini kaybeder.","preserves":"Aynı kök paketindeki başka bir biçimsel alanla bağı korur."},"text":"incir"}],"identity_rationale":"Kaynak ifadesi bu dalı bazı konuşma biçimlerinde kurt için kullanılan bir ad olarak açıkça verir. Bu kullanım ne yenilebilir meyveye ne de yer veya dağ adına bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bazı konuşma biçimlerinde kurt için kullanılan ad"}],"lexicalization_note":"Mekanik kapsam bare olduğu için adlandırma çıplak biçim olarak tanımlanır; başka dala ait meyve veya yer anlamı eklenmez.","neighbor_coverage_note":"Kurt alanındaki adaylardan biri yakın adlandırma, biri nitelikli kurt kullanımı, biri daha geniş yırtıcı sınıfı olarak sınırı açıklar; diğer hayvan adı adayları daha uzak ve tekrarlıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdek referent aynıdır, fakat her dal farklı ad biçimine ve ayrı kayıt koşuluna bağlı olduğu için tam eşanlamlı sayılmaz.","focus_only":"Bu dal belirli biçimin bazı konuşma biçimlerinde kurt adı olmasına dayanır.","gloss":"kurt adı","neighbor_only":"Komşu dal kurt için başka ad biçimlerini ve kendi dil kaydını taşır.","neighbor_ref":"root_001248/B013","relation_type":"near_synonym","shared_zone":"İki dal da kurt için kullanılan adlandırmalar alanında örtüşür."},{"boundary_match":"field_only","distinction":"Odak dal yalnızca adlandırma bildirir; komşu dalda ses çıkarma niteliği anlam sınırına dahil olur.","focus_only":"Bu dal kurt için bir addır.","gloss":"kurt adı ile kurt niteliği","neighbor_only":"Komşu dal çok ses çıkarma niteliğiyle bağlantılı bir kurt adı veya sıfatı verir.","neighbor_ref":"root_001270/B004","relation_type":"same_field","shared_zone":"İki dal kurtla ilgili adlandırma alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal tek bir hayvan için adlandırmadır; komşu dal daha geniş yırtıcı hayvan sınıfını ifade eder.","focus_only":"Bu dal kurt için özel bir addır.","gloss":"kurt adı ile yırtıcı sınıfı","neighbor_only":"Komşu dal aslan, kurt ve benzeri yırtıcı hayvanlar için daha geniş bir yırtıcı sınıfı taşır.","neighbor_ref":"root_000669/B002","relation_type":"near_neighbor","shared_zone":"Kurt, komşu dalın yırtıcı hayvanlar alanında yer alabilir."},{"boundary_match":"thematic_only","distinction":"Kurt adı ile meyve adı arasında ortak referent veya ikame edilebilir anlam yoktur.","focus_only":"Bu dal kurt için addır.","gloss":"hayvan adı ile meyve","neighbor_only":"Komşu dal yenilebilir incir meyvesidir.","neighbor_ref":"root_000190/B001","relation_type":"other","shared_zone":"Aynı kök paketi içinde biçimsel yakınlık bulunur."},{"boundary_match":"thematic_only","distinction":"Odak dal hayvan referentine bağlıdır; komşu dal mekan referentine bağlıdır ve anlam çekirdeği paylaşmaz.","focus_only":"Bu dal kurt için addır.","gloss":"hayvan adı ile yer adı","neighbor_only":"Komşu dal yer veya dağ adlandırmasıdır.","neighbor_ref":"root_000190/B002","relation_type":"other","shared_zone":"Aynı kök paketindeki farklı adlandırma dalları okuyucuya yakın görünebilir."}],"source_phrase_ar":"وقد سمي الذئب تِينانا في بعض اللغات (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı kayıt, bu biçimin bazı konuşma biçimlerinde kurt adı olarak kullanıldığını bildirir."}],"source_summary":"Bu dal için ortak çok kaynaklı özet yoktur; kanıt, bazı konuşma biçimlerinde kurt için kullanılan özel bir adlandırmayı bildirir.","sources":["JA"],"what_is_ar":"يدخل فيه تسمية الذئب تِينانا في بعض اللغات","what_is_not_ar":"ليس ثمر التين ولا مواضعه الجبلية"},"support_links":["sup_11c5980695cc480bba28","sup_181c3eec5c4b2950e49a"]},{"boundary":"Dal, yağı konu edinir; zeytin ağacını, meyvenin kendisini veya yağ sürme eylemini kapsamaz.","branch_kind":"bare","branch_ref":"root_000656/B001","candidate_links":[{"candidate_id":"cand_1d37b1a7789fb8cc933c","lane":"macro"},{"candidate_id":"cand_1ed8409f637f78bdb575","lane":"macro"},{"candidate_id":"cand_5b549f19ba0d0adf50ea","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"زَّيْتُون","morph_features":"STEM|POS:N|LEM:z~ayotuwn|ROOT:zyt|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:1:2:3","qac_word_ref":"95:1:2","surface_ar":"زَّيْتُونِ"}],"gloss":"zeytin meyvesinden çıkarılan yağ","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Zeytin meyvesinden sıkılarak çıkarılan yağlı maddedir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak anlatımları aynı maddeyi bilinen yağ, zeytinin yağı ve zeytinin sıkılmış özü olarak açıklar."}}],"root_ar":"ز ي ت","root_id":"root_000656","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maddenin kaynağını ve yağ niteliğini birlikte belirtmek gereken genel kullanımlarda uygundur.","boundary_detail":"Dal, yağı konu edinir; zeytin ağacını, meyvenin kendisini veya yağ sürme eylemini kapsamaz.","branch_image_ar":"الزيت وعصارة الزيتون","concept_gloss":"zeytin meyvesinden çıkarılan yağ","contextual_glosses":[{"applicability":"Sıkma yoluyla elde edilişin bağlamda özellikle öne çıktığı kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Zeytin kaynağını, sıkma işlemini ve elde edilen yağ niteliğini korur."},"facet_ids":["F001"],"text":"zeytinin sıkılmış yağı","usage_role":"contextual"}],"definition":"Zeytin meyvesinin sıkılmasıyla elde edilen, onun yağı veya sıkılmış özü sayılan yağlı maddedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Zeytin meyvesinden sıkılarak çıkarılan yağlı maddedir."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak anlatımları aynı maddeyi bilinen yağ, zeytinin yağı ve zeytinin sıkılmış özü olarak açıklar."}],"identity_rationale":"Kaynak ifadesi, bilinen yağı özellikle zeytin meyvesinden çıkarılan yağ ve sıkılmış öz olarak tanımlar. Verilen dal çerçevesi bu maddeyi ağaçtan, meyveden ve yağlama eyleminden ayırarak doğru sınırı korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"zeytin meyvesinden çıkarılan bilinen yağ ve sıkılmış öz"}],"lexicalization_note":"Yalın kapsam, zeytinden çıkarılan yağın adını tanımlar; başka dallardaki eylem ve meslek anlamları buraya taşınmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; sınırı en açık biçimde bitki ve meyve, başka bitkisel yağ ve yağlama eylemiyle karşılaştıran üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Biri sıkmayla elde edilen maddeyi, diğeri ise bu maddenin kaynağı olan ağacı ve meyveyi adlandırır; birbirinin yerine kullanılamaz.","focus_only":"Bu dal, meyveden çıkarılan yağlı maddeyi belirtir.","gloss":"çıkarılan yağ ile bitki ve meyve","neighbor_only":"Komşu dal, ağacı, meyveyi veya bunların topluluğunu belirtir.","neighbor_ref":"root_000656/B002","relation_type":"thematic","shared_zone":"İki dal aynı bitki ve onun ürünü çevresindeki üretim ilişkisine katılır."},{"boundary_match":"field_only","distinction":"Madde türleri aynı genel alanda bulunsa da kaynak bitkileri farklıdır; zeytin yağı ile susam yağı aynı kavram değildir.","focus_only":"Bu dalın yağı zeytin meyvesinden çıkarılır.","gloss":"farklı bitkilerden çıkarılan yağlar","neighbor_only":"Komşu dalın yağı susamdan çıkarılır.","neighbor_ref":"root_000351/B015","relation_type":"same_field","shared_zone":"Her iki dal da bitkisel bir hammaddeden elde edilen yağlı bir maddeyi konu edinir."},{"boundary_match":"thematic_only","distinction":"Maddenin adı, o maddeyle yapılan hazırlama veya sürme eyleminin adı değildir.","focus_only":"Bu dal, kullanılan yağlı maddenin kendisini adlandırır.","gloss":"madde ile onun kullanılması","neighbor_only":"Komşu dal, yağı yemeğe katma veya birine ya da kendine sürme eylemini adlandırır.","neighbor_ref":"root_000656/B003","relation_type":"thematic","shared_zone":"Her iki dalda da zeytinden çıkarılan yağ ortak katılımcıdır."}],"source_phrase_ar":"الزيت معروف (maqayis;jamhara)؛ الزيت دهنه (sihah)؛ الزيت عصارة الزيتون (tahdhib;mufradat)؛ الدهن الذي يستخرج منه زيت (tahdhib)","source_summary":"Kaynakların ortak çekirdeği, bu adın zeytin meyvesinden elde edilen bilinen yağlı maddeyi ve onun sıkılmış özünü belirtmesidir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الزيت المعروف ودهن الزيتون وعصارته","what_is_not_ar":"ليس شجر الزيتون ولا ثمرته ولا فعل التزييت"},"support_links":["sup_2ebba7b49bcbd77a091a","sup_391abd11076b410a0c27","sup_6258318b0372247b0d28"]},{"boundary":"Dal, ağaç, meyve ve bunların topluluğuyla sınırlıdır; meyveden çıkarılan yağ burada tanımlanmaz.","branch_kind":"bare","branch_ref":"root_000656/B002","candidate_links":[{"candidate_id":"cand_29f737daf46242eee0af","lane":"macro"},{"candidate_id":"cand_fdf8a65d88b5fe260f1a","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"زَّيْتُون","morph_features":"STEM|POS:N|LEM:z~ayotuwn|ROOT:zyt|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:1:2:3","qac_word_ref":"95:1:2","surface_ar":"زَّيْتُونِ"}],"gloss":"zeytin ağacı, meyvesi veya topluluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ad, zeytin ağacının kendisini belirtebilir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı ad, ağacın verdiği zeytin meyvesini belirtebilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tekil biçim bir ağacı veya bir meyveyi, topluluk biçimi ise bunların bütününü gösterebilir."}}],"root_ar":"ز ي ت","root_id":"root_000656","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ağaç, meyve ve sayı bakımından bütün dal kapsamını tek ifadede göstermek gerektiğinde uygundur.","boundary_detail":"Dal, ağaç, meyve ve bunların topluluğuyla sınırlıdır; meyveden çıkarılan yağ burada tanımlanmaz.","branch_image_ar":"الزيتون والزيتونة","concept_gloss":"zeytin ağacı, meyvesi veya topluluğu","contextual_glosses":[{"applicability":"Gönderimin bitkinin kendisi olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ağaç gönderimini açık ve doğal biçimde korur."},"facet_ids":["F001"],"text":"zeytin ağacı","usage_role":"contextual"},{"applicability":"Gönderimin ağacın yenilebilir meyvesi olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Meyve gönderimini ağaç gönderiminden açıkça ayırır."},"facet_ids":["F002"],"text":"zeytin meyvesi","usage_role":"contextual"},{"applicability":"Topluluk biçiminin bağlama göre ağaçlar ya da meyveler gösterdiğini açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluk kapsamını ve ağaç ile meyve arasındaki bağlamsal seçimi korur."},"facet_ids":["F003"],"text":"zeytin ağaçları veya meyveleri","usage_role":"explanatory"}],"definition":"Zeytin ağacını, bu ağacın meyvesini veya bunların topluluğunu belirten addır; tekil biçim bir ağacı da bir meyveyi de gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ad, zeytin ağacının kendisini belirtebilir."},{"facet_id":"F002","role":"core","statement":"Aynı ad, ağacın verdiği zeytin meyvesini belirtebilir."},{"facet_id":"F003","role":"specialization","statement":"Tekil biçim bir ağacı veya bir meyveyi, topluluk biçimi ise bunların bütününü gösterebilir."}],"identity_rationale":"Kaynak ifadesi hem ağacın hem meyvenin aynı adla anılabildiğini, tekil biçimin bir ağacı veya bir meyveyi gösterebildiğini ve topluluk biçiminin de bulunduğunu açıkça belirtir. Dal çerçevesi bu sayı ve gönderim ayrımlarını korur.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"zeytin ağacı, meyvesi veya bunların topluluğu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tek bir zeytin ağacı veya tek bir zeytin meyvesi"}],"lexicalization_note":"Yalın kapsam, bitkiyi, meyveyi ve tekil-topluluk ayrımını içerir; yağ maddesi veya yağlama eylemi eklenmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; yağla ürün ilişkisini ve ağaç ile meyve alanındaki tür sınırlarını gösteren üç karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Ağaç veya meyve adı, bunlardan sıkılarak çıkarılan maddenin adıyla aynı anlamsal çekirdeğe sahip değildir.","focus_only":"Bu dal, ağacı, meyveyi veya bunların topluluğunu belirtir.","gloss":"bitki ve meyve ile çıkarılan yağ","neighbor_only":"Komşu dal, meyvenin sıkılmasıyla elde edilen yağlı maddeyi belirtir.","neighbor_ref":"root_000656/B001","relation_type":"thematic","shared_zone":"Meyve, komşu daldaki yağlı maddenin doğal kaynağıdır."},{"boundary_match":"field_only","distinction":"Ortak üst alan ağaç adlarıdır; tür kimliği ve meyveye uzanan gönderim yalnızca bu dalın sınırındadır.","focus_only":"Bu dal, zeytin ağacını ve onun meyvesini birlikte kapsayabilir.","gloss":"farklı ağaç türleri","neighbor_only":"Komşu dal, başka bir tür ağacı adlandırır ve meyve gönderimini çekirdek yapmaz.","neighbor_ref":"root_000501/B005","relation_type":"same_field","shared_zone":"Her iki dal da belirli bir ağaç türünün adını içerir."},{"boundary_match":"field_only","distinction":"Meyve alanındaki yakınlık tür özdeşliği yaratmaz; ayrıca bu dalın ağaç ve topluluk gönderimleri komşuda bulunmaz.","focus_only":"Bu dal hem ağacı hem onun meyvesini adlandırabilir.","gloss":"farklı meyve türleri","neighbor_only":"Komşu dal belirli bir başka meyve türünü adlandırır.","neighbor_ref":"root_000149/B006","relation_type":"same_field","shared_zone":"Her iki dal da yenilebilir bir ağaç meyvesini konu edinir."}],"source_phrase_ar":"الزيتون معروف والواحدة زيتونة (sihah)؛ يقال للشجرة نفسها زيتونة ولثمرها زيتونة والجميع الزيتون (tahdhib)؛ زيتون وزيتونة نحو شجر وشجرة (mufradat)","source_summary":"Kaynaklar, adın ağaca ve meyveye ortak biçimde uygulanmasında ve tekil biçimin bunlardan birini gösterebilmesinde birleşir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه الزيتون والزيتونة للشجرة أو الثمرة والجمع","what_is_not_ar":"ليس الزيت المستخرج ولا دهن الشيء بالزيت"},"support_links":["sup_11c5980695cc480bba28","sup_82800c2b4f9d548de6ae"]},{"boundary":"Dal, yağın yiyeceğe katılması veya birine ya da kişinin kendisine sürülmesiyle sınırlıdır; yağ sağlama ve bağış isteme ayrı daldadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000656/B003","candidate_links":[{"candidate_id":"cand_d57d4b196caffdd3e548","lane":"macro"},{"candidate_id":"cand_6b14a928608c23465e5f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"زَّيْتُون","morph_features":"STEM|POS:N|LEM:z~ayotuwn|ROOT:zyt|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:1:2:3","qac_word_ref":"95:1:2","surface_ar":"زَّيْتُونِ"}],"gloss":"yemeğe yağ katmak ya da birine veya kendine yağ sürmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yiyeceğe zeytinden çıkarılan yağ katmak veya yiyeceği bu yağla hazırlamaktır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin başına veya bedenine zeytinden çıkarılan yağ sürmektir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dönüşlü kullanımda yağı süren kişi ile yağ sürülen kişi aynıdır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İşlemin sonucu, yağ katılmış yiyecek veya üzerine yağ sürülmüş bir şey olarak adlandırılabilir."}}],"root_ar":"ز ي ت","root_id":"root_000656","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yiyecek hazırlama, başa veya bedene sürme ve dönüşlü uygulama kapsamını birlikte göstermek için uygundur.","boundary_detail":"Dal, yağın yiyeceğe katılması veya birine ya da kişinin kendisine sürülmesiyle sınırlıdır; yağ sağlama ve bağış isteme ayrı daldadır.","branch_image_ar":"التزييت والإدهان بالزيت","concept_gloss":"yemeğe yağ katmak ya da birine veya kendine yağ sürmek","contextual_glosses":[{"applicability":"Yağın yiyeceğin içine konduğu veya yiyeceğin yağla hazırlandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yiyeceğe yağ ekleme işlemini ve ortaya çıkan yağlı hazırlığı korur."},"facet_ids":["F001","F004"],"text":"yemeğe yağ katmak","usage_role":"contextual"},{"applicability":"Yağın bir başkasının başına ya da bedenine uygulandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağı yüzeye sürme işlemini ve uygulanan kişiyi korur."},"facet_ids":["F002","F004"],"text":"başa veya bedene yağ sürmek","usage_role":"contextual"},{"applicability":"Eylemi yapan ile yağ sürülen kişinin aynı olduğu dönüşlü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağ sürme eylemini ve özne ile etkilenen kişinin özdeşliğini korur."},"facet_ids":["F003"],"text":"kendine yağ sürmek","usage_role":"contextual"}],"definition":"Bir yiyeceğe zeytinden çıkarılan yağ katmak veya bu yağı birinin başına ya da bedenine sürmektir; dönüşlü kullanımda kişi yağı kendisine sürer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yiyeceğe zeytinden çıkarılan yağ katmak veya yiyeceği bu yağla hazırlamaktır."},{"facet_id":"F002","role":"core","statement":"Bir kişinin başına veya bedenine zeytinden çıkarılan yağ sürmektir."},{"facet_id":"F003","role":"specialization","statement":"Dönüşlü kullanımda yağı süren kişi ile yağ sürülen kişi aynıdır."},{"facet_id":"F004","role":"extension","statement":"İşlemin sonucu, yağ katılmış yiyecek veya üzerine yağ sürülmüş bir şey olarak adlandırılabilir."}],"identity_rationale":"Kaynak ifadesi yemeğe yağ katmayı, başa yağ sürmeyi ve kişinin yağı kendine sürmesini ayrı gerçekleşmeler olarak verir. Dal çerçevesi hem işlem türlerini hem de dönüşlü kullanımda katılımcı değişimini doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yemeğe yağ katmak veya yemeği yağla hazırlamak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"başa yağ sürmek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yağ katılmış veya yağla hazırlanmış"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yağ katılmış ya da üzerine yağ sürülmüş"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kendine yağ sürmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kendine yağ sürmüş kimse"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kendine yağ sürmüş kimseyi küçülterek anlatan biçim"}],"lexicalization_note":"Karma ve yalın olmayan kapsamda yiyecek, baş ve dönüşlü kullanım ayrı tutulur; belirli yapılardan genel bir yağ adı türetilmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; madde-eylem ayrımını, sağlama eylemi sınırını ve bedene başka madde uygulama yakınlığını gösteren üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Bir maddeyi adlandırmak, o maddeyi yemeğe katma veya bedene sürme eylemini adlandırmakla aynı değildir.","focus_only":"Bu dal, yağla yapılan katma veya sürme işlemini belirtir.","gloss":"yağı kullanmak ile yağın kendisi","neighbor_only":"Komşu dal, işlemde kullanılan yağlı maddenin kendisini belirtir.","neighbor_ref":"root_000656/B001","relation_type":"thematic","shared_zone":"Yağlı madde, bu daldaki bütün işlemlerin ortak aracıdır."},{"boundary_match":"partial","distinction":"Doğrudan katma ya da sürme işlemi, topluluğun gereksinimi için sağlama veya bağış isteme işlemiyle yer değiştiremez.","focus_only":"Bu dalda yağ doğrudan yiyeceğe katılır veya bir yüzeye sürülür.","gloss":"yağı uygulamak ile yağı sağlamak","neighbor_only":"Komşu dalda yağ bir topluluğa katık veya azık yapılır, sağlanır ya da bağış olarak istenir.","neighbor_ref":"root_000656/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalda da yağ bir insan etkinliğinin nesnesidir ve yiyecek bağlamı bulunabilir."},{"boundary_match":"partial","distinction":"Bu dalın aracı yağdır ve yiyecek hazırlamaya da uzanır; komşu dalın çekirdeği koku veya renk veren maddeyle kaplamadır.","focus_only":"Bu dal, yiyeceğe yağ katmayı ve başa ya da bedene yağ sürmeyi kapsar.","gloss":"yağ sürmek ile kokulu maddeyle kaplamak","neighbor_only":"Komşu dal, bedeni koku verici veya renk verici maddelerle kaplamayı kapsar.","neighbor_ref":"root_001100/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir madde insan bedeninin dış yüzeyine uygulanabilir."}],"source_phrase_ar":"زته إذا دهنته بالزيت (maqayis)؛ طعام مزيت إذا كان فيه الزيت (jamhara)؛ زت الطعام إذا جعلت فيه الزيت وطعام مزيت ومزيوت (sihah)؛ زت الثريد وزت رأس فلان وازدات فلان إذا ادهن بالزيت (tahdhib)؛ زات طعامه وزات رأسه وازدات ادهن (mufradat)","source_summary":"Kaynaklar, yiyeceğe yağ katma ile başa veya bedene yağ sürme işlemlerini ve kişinin kendine yağ sürmesini aynı anlam ailesinde toplar.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه جعل الزيت في الطعام أو على الرأس أو الدهن به والادهان به","what_is_not_ar":"ليس اسم الزيت نفسه ولا الزيتون ولا تزويد القوم بالزيت ولا طلب هبته"},"support_links":["sup_555353fda551042fee86","sup_6925fdadbc27aa33354d"]},{"boundary":"Dal, topluluk için katık yapma, yağ sağlama ve bağış isteme yapılarıyla sınırlıdır; sıradan yağ sürme eylemini kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000656/B004","candidate_links":[{"candidate_id":"cand_3ca0913747e037aad56b","lane":"macro"},{"candidate_id":"cand_7a61eae3b729c2a8c371","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"زَّيْتُون","morph_features":"STEM|POS:N|LEM:z~ayotuwn|ROOT:zyt|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:1:2:3","qac_word_ref":"95:1:2","surface_ar":"زَّيْتُونِ"}],"gloss":"bir topluluğa yağı katık yapmak veya sağlamak ya da yağı bağış olarak istemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun yiyeceğine eşlik eden katığı zeytinden çıkarılan yağ yapmaktır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğa gereksinimleri için zeytinden çıkarılan yağ sağlamaktır."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Zeytinden çıkarılan yağı birinden bağış olarak istemektir."}}],"root_ar":"ز ي ت","root_id":"root_000656","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Üç katılımcı düzenini ve yağın katık, sağlanan azık veya istenen bağış olmasını birlikte göstermek için uygundur.","boundary_detail":"Dal, topluluk için katık yapma, yağ sağlama ve bağış isteme yapılarıyla sınırlıdır; sıradan yağ sürme eylemini kapsamaz.","branch_image_ar":"الزيت أدمًا وزادًا وهبة","concept_gloss":"bir topluluğa yağı katık yapmak veya sağlamak ya da yağı bağış olarak istemek","contextual_glosses":[{"applicability":"Yağın bir topluluğun yiyeceğine eşlik eden katık yapıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluk katılımcısını ve yağın katık yapılması işlemini korur."},"facet_ids":["F001"],"text":"topluluğun katığını yağ yapmak","usage_role":"contextual"},{"applicability":"Bir topluluğa gereksinimleri veya yol azığı için yağ verildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağın topluluğa sağlanması işlemini ve alıcı grubunu korur."},"facet_ids":["F002"],"text":"topluluğa yağ sağlamak","usage_role":"contextual"},{"applicability":"Birinden karşılıksız yağ verme isteğinde bulunulan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağın istenen bağış olmasını ve isteme işlemini korur."},"facet_ids":["F003"],"text":"yağı bağış olarak istemek","usage_role":"contextual"}],"definition":"Bir topluluğun katığını zeytinden çıkarılan yağ yapmak veya onlara bu yağı azık olarak sağlamak ya da aynı yağı bağış olarak istemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun yiyeceğine eşlik eden katığı zeytinden çıkarılan yağ yapmaktır."},{"facet_id":"F002","role":"core","statement":"Bir topluluğa gereksinimleri için zeytinden çıkarılan yağ sağlamaktır."},{"facet_id":"F003","role":"core","statement":"Zeytinden çıkarılan yağı birinden bağış olarak istemektir."}],"identity_rationale":"Kaynak ifadesi üç ayrı işlemi açıkça verir: bir topluluğun katığını yağ yapmak, onlara yağ sağlamak ve yağı bağış olarak istemek. Dal çerçevesi bu işlemleri doğrudan yiyeceğe yağ katma veya bedene sürme anlamıyla karıştırmadan korur.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"topluluğun katığını zeytinden çıkarılan yağ yapmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"onlara zeytinden çıkarılan yağ sağlamak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"zeytinden çıkarılan yağı bağış olarak istemek"}],"lexicalization_note":"Karma ve yalın olmayan kapsam, topluluk katılımcısını ve sağlama ya da isteme yapılarını zorunlu tutar; genel yağlama anlamına genişletilmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; benzer işlemleri başka yağla kuran dal, doğrudan yedirme dalı ve yağ uygulama dalı sınırı en iyi açıklayan komşulardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İşlem örüntüleri büyük ölçüde örtüşse de kullanılan yağ türü farklıdır ve komşu dal satışa da uzanır.","focus_only":"Bu dalın işlemleri zeytinden çıkarılan yağla yapılır.","gloss":"farklı yağlarla katık ve azık sağlama","neighbor_only":"Komşu dal aynı türden bazı işlemleri sütten elde edilen katı yağla yapar ve satış kullanımını da içerir.","neighbor_ref":"root_000744/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da yenilebilir bir yağ katık yapılabilir, topluluğa sağlanabilir veya bağış olarak istenebilir."},{"boundary_match":"field_only","distinction":"Yağı topluluğa sağlamak veya istemek, yağı doğrudan insanlara yedirme eylemiyle aynı işlem değildir.","focus_only":"Bu dal katık yapma, azık sağlama ve bağış istemeyi kapsar.","gloss":"yağ sağlamak ile yağ yedirmek","neighbor_only":"Komşu dal insanlara hayvansal yağ yedirmeyi çekirdek işlem yapar.","neighbor_ref":"root_000779/B004","relation_type":"same_field","shared_zone":"Her iki dalda da bir topluluğa yenilebilir yağ ulaştırma durumu bulunabilir."},{"boundary_match":"partial","distinction":"Topluluğa yönelik sağlama ve isteme ilişkileri, nesneye doğrudan yağ katma veya sürme işlemlerinden ayrıdır.","focus_only":"Bu dal yağın topluluğa katık veya azık yapılmasını, sağlanmasını ya da istenmesini belirtir.","gloss":"yağı sağlamak ile yağı uygulamak","neighbor_only":"Komşu dal yağı doğrudan yiyeceğe katmayı veya başa ya da bedene sürmeyi belirtir.","neighbor_ref":"root_000656/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da yağ insan kullanımına sokulur ve yiyecek bağlamına girebilir."}],"source_phrase_ar":"زت القوم جعلت أدمهم الزيت؛ زيتهم إذا زودتهم الزيت؛ جاءوا يستزيتون أي يستوهبون الزيت","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, topluluğun katığını yağ yapma, onlara yağ sağlama ve yağı bağış olarak isteme işlemlerini birlikte verir."}],"source_summary":"Kanıt tek kaynağa dayandığından ortak kaynak özeti yoktur; özgül işlemler aşağıdaki tek kaynak notunda birlikte korunur.","sources":["SI"],"what_is_ar":"يدخل فيه جعل الزيت أدمًا للقوم أو زادًا لهم أو استيهابه","what_is_not_ar":"ليس مجرد صب الزيت في الطعام ولا الادهان به"},"support_links":["sup_78430e46ce7bffb30fff","sup_d3fa10a303f4b206eb8c"]},{"boundary":"Dal, yağı satan veya sıkıp çıkaran kişiyi belirtir; yağ maddesini ya da yağlama işlemini belirtmez.","branch_kind":"bare","branch_ref":"root_000656/B005","candidate_links":[{"candidate_id":"cand_7a61eae3b729c2a8c371","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"زَّيْتُون","morph_features":"STEM|POS:N|LEM:z~ayotuwn|ROOT:zyt|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:1:2:3","qac_word_ref":"95:1:2","surface_ar":"زَّيْتُونِ"}],"gloss":"zeytin yağını satan veya sıkıp çıkaran kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Zeytin meyvesinden çıkarılan yağı satan kişidir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zeytin meyvesini sıkıp yağını çıkaran kişidir."}}],"root_ar":"ز ي ت","root_id":"root_000656","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Satıcılık ve sıkma yoluyla yağ çıkarma uğraşlarının ikisini de kapsayan kişi adı gerektiğinde uygundur.","boundary_detail":"Dal, yağı satan veya sıkıp çıkaran kişiyi belirtir; yağ maddesini ya da yağlama işlemini belirtmez.","branch_image_ar":"الزيات بائع الزيت وعاصره","concept_gloss":"zeytin yağını satan veya sıkıp çıkaran kişi","contextual_glosses":[{"applicability":"Kişinin zeytin meyvesinden çıkarılan yağı sattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Satıcı kişiyi ve satılan yağın zeytin kaynağını korur."},"facet_ids":["F001"],"text":"zeytin yağı satıcısı","usage_role":"contextual"},{"applicability":"Kişinin zeytin meyvesini sıkarak yağ elde ettiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sıkma işlemini, ortaya çıkan yağı ve işlemi yapan kişiyi korur."},"facet_ids":["F002"],"text":"zeytini sıkıp yağ çıkaran kişi","usage_role":"contextual"}],"definition":"Zeytin meyvesinden çıkarılan yağı satan veya zeytini sıkıp bu yağı çıkaran kişidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Zeytin meyvesinden çıkarılan yağı satan kişidir."},{"facet_id":"F002","role":"core","statement":"Zeytin meyvesini sıkıp yağını çıkaran kişidir."}],"identity_rationale":"Kaynak ifadesi kişiyi iki uğraşla tanımlar: zeytinden çıkarılan yağı satmak ve bu yağı sıkma yoluyla çıkarmak. Dal çerçevesi meslek veya uğraş sahibini maddenin kendisinden ve yağ sürme eyleminden doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"zeytin yağını satan veya zeytini sıkıp yağ çıkaran kişi"}],"lexicalization_note":"Yalın kapsam kişi adını satma ve sıkıp çıkarma uğraşlarıyla tanımlar; genel tüccar veya herhangi bir yağ işçisi anlamına genişletmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; genel yağ satıcısı, başka tür yağ satıcısı ve geniş kapsamlı yiyecek satıcısı kişi adının sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Satıcılık kesişiminde yakınlık vardır; ancak bu dal ürün kaynağını zeytinle sınırlar ve sıkıp yağ çıkaran kişiyi de kapsar.","focus_only":"Bu dal zeytin yağını satmanın yanında zeytini sıkıp yağ çıkarmayı da kapsar.","gloss":"zeytin yağı işçisi ile genel yağ satıcısı","neighbor_only":"Komşu dal, kaynak veya üretim işlemi bakımından daha genel bir yağ satıcısını belirtir.","neighbor_ref":"root_000497/B010","relation_type":"near_synonym","shared_zone":"Her iki dal da yağ satan bir kişiyi belirtebilir."},{"boundary_match":"partial","distinction":"Satılan ürünün kaynağı farklıdır; ayrıca sıkıp yağ çıkarma işi yalnızca bu dalın kapsamındadır.","focus_only":"Bu dal zeytin yağını satan veya zeytinden yağ çıkaran kişiyi belirtir.","gloss":"farklı tür yağların satıcıları","neighbor_only":"Komşu dal hayvansal yağ satan kişiyi belirtir.","neighbor_ref":"root_000779/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda da yenilebilir yağ satan bir kişi söz konusudur."},{"boundary_match":"partial","distinction":"Genel yiyecek satıcılığı ürün türünü sınırlamaz ve sıkma yoluyla üretimi içermez; bu dal ise belirli yağ ve üretim işiyle sınırlandırılmıştır.","focus_only":"Bu dal belirli bir yağı satan veya onu sıkıp çıkaran kişiye özgüdür.","gloss":"özel yağ satıcısı ile genel yiyecek satıcısı","neighbor_only":"Komşu dal her tür yiyeceği satabilen daha geniş kapsamlı bir satıcıyı belirtir.","neighbor_ref":"root_000095/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal gıda satışı yapan bir meslek sahibini içerebilir."}],"source_phrase_ar":"يقال للذي يبيعه ويعتصره زيات","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, aynı kişi adının yağı satan kimseyi de zeytini sıkıp yağ çıkaran kimseyi de belirtebildiğini bildirir."}],"source_summary":"Kanıt tek kaynağa dayandığından ortak kaynak özeti yoktur; iki uğraş aşağıdaki tek kaynak notunda birlikte korunur.","sources":["TA"],"what_is_ar":"يدخل فيه الزيات الذي يبيع الزيت أو يعتصره","what_is_not_ar":"ليس الزيت نفسه ولا فعل دهن الشيء به"},"support_links":["sup_78430e46ce7bffb30fff"]},{"boundary":"It includes travelers called بنو العمل when they travel on foot","branch_kind":null,"branch_ref":"root_001046/B012","candidate_links":[{"candidate_id":"cand_f532461f05b2eb1eec37","lane":"macro"}],"focus_root_occurrences":[],"gloss":"walking travelers","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"بنو العمل من المشاة","image_en":"walking travelers"}}],"root_ar":"ع م ل","root_id":"root_001046","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"بنو العمل من المشاة","image_en":"walking travelers","scope_ar":"يدخل فيه بنو العمل وهم المسافرون إذا مشوا على أرجلهم","scope_en":"It includes travelers called بنو العمل when they travel on foot"},"support_links":["sup_1342c3eb7ecbfe914bb9"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000015/B001","candidate_links":[{"candidate_id":"cand_7a61eae3b729c2a8c371","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1fc526760dd3de41a9b3","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Recompense for work or hire formalizes the return side of the labor relation.","root":"ء ج ر","source_ref":"95:6","source_word_indices":["7"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000015","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_78430e46ce7bffb30fff"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000047/B002","candidate_links":[{"candidate_id":"cand_5b549f19ba0d0adf50ea","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_48833b804a57be4e33c1","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The divine name's use in oath and invocation reinforces the formal oath frame surrounding the focus objects.","root":"ء ل ه","source_ref":"95:8","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000047","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2ebba7b49bcbd77a091a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000054/B001","candidate_links":[{"candidate_id":"cand_29f737daf46242eee0af","lane":"macro"},{"candidate_id":"cand_fdf8a65d88b5fe260f1a","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_891c83d7e1aeb5d71e7e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Calm security and trust qualify the bounded land as protected rather than merely enclosed.","root":"ء م ن","source_ref":"95:3","source_word_indices":["3"]},{"hft_ref":"hft_261ad29b2d4e9e93280c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Security and settled trust make the bounded cultivated side explicitly safe.","root":"ء م ن","source_ref":"95:3","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000054","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_11c5980695cc480bba28","sup_82800c2b4f9d548de6ae"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000148/B001","candidate_links":[{"candidate_id":"cand_29f737daf46242eee0af","lane":"macro"},{"candidate_id":"cand_fdf8a65d88b5fe260f1a","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_891c83d7e1aeb5d71e7e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The bounded tract of earth supplies a perimeter, converting loose landmarks into delimited inhabited space.","root":"ب ل د","source_ref":"95:3","source_word_indices":["2"]},{"hft_ref":"hft_261ad29b2d4e9e93280c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Bounded ground supplies the perimeter across which wild and cultivated domains can be contrasted.","root":"ب ل د","source_ref":"95:3","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000148","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_11c5980695cc480bba28","sup_82800c2b4f9d548de6ae"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000148/B006","candidate_links":[{"candidate_id":"cand_6b14a928608c23465e5f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_24dcfbf6eb7678798376","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A mark on skin or body makes the context's spatial noun touch the body's visible surface.","root":"ب ل د","source_ref":"95:3","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000148","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6925fdadbc27aa33354d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000323/B001","candidate_links":[{"candidate_id":"cand_1ed8409f637f78bdb575","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9091e1cf7b421ddf3490","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Beauty opposed to ugliness supplies a qualitative pole for the formed result.","root":"ح س ن","source_ref":"95:4","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000323","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6258318b0372247b0d28"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000348/B002","candidate_links":[{"candidate_id":"cand_5b549f19ba0d0adf50ea","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_48833b804a57be4e33c1","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Judgment between people supplies the tribunal role that converts invoked objects into evidentiary witnesses.","root":"ح ك م","source_ref":"95:8","source_word_indices":["3","4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000348","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2ebba7b49bcbd77a091a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000434/B001","candidate_links":[{"candidate_id":"cand_1ed8409f637f78bdb575","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9091e1cf7b421ddf3490","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Creation as measuring and proportioning supplies the operation by which an achieved form is set.","root":"خ ل ق","source_ref":"95:4","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000434","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6258318b0372247b0d28"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000434/B009","candidate_links":[{"candidate_id":"cand_6b14a928608c23465e5f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_24dcfbf6eb7678798376","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A garment worn until its nap disappears contributes gradual loss of an outer covering.","root":"خ ل ق","source_ref":"95:4","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000434","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6925fdadbc27aa33354d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000504/B002","candidate_links":[{"candidate_id":"cand_7a61eae3b729c2a8c371","lane":"macro"},{"candidate_id":"cand_5b549f19ba0d0adf50ea","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1fc526760dd3de41a9b3","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Accounting and recompense extend the crop-and-wage chain into a final reckoning of value.","root":"د ي ن","source_ref":"95:7","source_word_indices":["4"]},{"hft_ref":"hft_48833b804a57be4e33c1","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Accounting and recompense define what is at stake in the contested claim.","root":"د ي ن","source_ref":"95:7","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000504","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2ebba7b49bcbd77a091a","sup_78430e46ce7bffb30fff"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000555/B001","candidate_links":[{"candidate_id":"cand_1ed8409f637f78bdb575","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9091e1cf7b421ddf3490","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Returning a thing to a prior place supplies the reversal arrow that makes achieved form nonfinal.","root":"ر د د","source_ref":"95:5","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000555","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6258318b0372247b0d28"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000715/B001","candidate_links":[{"candidate_id":"cand_1ed8409f637f78bdb575","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9091e1cf7b421ddf3490","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Physical low position supplies the downward endpoint of the reversal.","root":"س ف ل","source_ref":"95:5","source_word_indices":["3","4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000715","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6258318b0372247b0d28"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000715/B004","candidate_links":[{"candidate_id":"cand_3ca0913747e037aad56b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ffb9a9f0034ac0cd696b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The act of moving downward supplies the collapse that contrasts with maintained standing.","root":"س ف ل","source_ref":"95:5","source_word_indices":["3","4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000715","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d3fa10a303f4b206eb8c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000955/B005","candidate_links":[{"candidate_id":"cand_29f737daf46242eee0af","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_891c83d7e1aeb5d71e7e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The mountain or mountain-name branch repeats the focus place scale and extends it into an explicit upland landmark.","root":"ط و ر","source_ref":"95:2","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000955","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_82800c2b4f9d548de6ae"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000955/B006","candidate_links":[{"candidate_id":"cand_fdf8a65d88b5fe260f1a","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_261ad29b2d4e9e93280c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Wildness and departure from familiar human limits give the wolf branch an environmental domain rather than leaving it isolated.","root":"ط و ر","source_ref":"95:2","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000955","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_11c5980695cc480bba28"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001046/B004","candidate_links":[{"candidate_id":"cand_7a61eae3b729c2a8c371","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1fc526760dd3de41a9b3","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The wage and provision of a worker connect intentional labor to a due material return.","root":"ع م ل","source_ref":"95:6","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001046","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_78430e46ce7bffb30fff"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001273/B008","candidate_links":[{"candidate_id":"cand_1ed8409f637f78bdb575","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9091e1cf7b421ddf3490","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Straightness, moderation, and levelness give the human form an upright equilibrium rather than a static shape alone.","root":"ق و م","source_ref":"95:4","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001273","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6258318b0372247b0d28"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001273/B009","candidate_links":[{"candidate_id":"cand_3ca0913747e037aad56b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ffb9a9f0034ac0cd696b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Qiwam as pillar, subsistence, and livelihood explicitly joins economic sustenance to structural support.","root":"ق و م","source_ref":"95:4","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001273","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d3fa10a303f4b206eb8c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001273/B010","candidate_links":[{"candidate_id":"cand_7a61eae3b729c2a8c371","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1fc526760dd3de41a9b3","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Valuation and pricing supply the operation that assigns exchange value to produced goods.","root":"ق و م","source_ref":"95:4","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001273","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_78430e46ce7bffb30fff"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001290/B001","candidate_links":[{"candidate_id":"cand_5b549f19ba0d0adf50ea","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_48833b804a57be4e33c1","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Falsehood as the contrary of truth creates the contested claim for which the oath objects can serve as evidence.","root":"ك ذ ب","source_ref":"95:7","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001290","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2ebba7b49bcbd77a091a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001390/B001","candidate_links":[{"candidate_id":"cand_5b549f19ba0d0adf50ea","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_48833b804a57be4e33c1","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Negation that denies a state supplies the closing interrogative challenge to denial.","root":"ل ي س","source_ref":"95:8","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001390","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2ebba7b49bcbd77a091a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001413/B001","candidate_links":[{"candidate_id":"cand_6b14a928608c23465e5f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_24dcfbf6eb7678798376","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant mapped branch's stripping away of what covers a thing supplies the terminal exposure in the surface sequence.","root":"ر د د","source_ref":"95:5","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001413","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6925fdadbc27aa33354d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001449/B001","candidate_links":[{"candidate_id":"cand_7a61eae3b729c2a8c371","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1fc526760dd3de41a9b3","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Cutting and diminishing until extension ceases supply the finite limit that the grammatical negation refuses.","root":"م ن ن","source_ref":"95:6","source_word_indices":["9"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001449","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_78430e46ce7bffb30fff"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001449/B002","candidate_links":[{"candidate_id":"cand_3ca0913747e037aad56b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ffb9a9f0034ac0cd696b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The force by which something stands, or the loss of that force, makes continuity of support the mechanism's hinge.","root":"م ن ن","source_ref":"95:6","source_word_indices":["9"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001449","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d3fa10a303f4b206eb8c"]}],"candidate_inventory":[{"anchor_refs":["95:1","95:2","95:4"],"branch_refs":["root_000059/B001","root_000190/B003"],"candidate_id":"cand_2b6dfb92fca330bba11a","commentary_obligation":"review","focus_branch_refs":["root_000190/B003"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000059/B001"],"root_ids":[],"scope":"pericope","source_local_id":"A:Familiar Presence Against Wild Absence","source_type":"channel","support_ids":["sup_1500a4508ad33e941986","sup_181c3eec5c4b2950e49a","sup_465a62a27b3cddebfe3f","sup_6175c0de0dbd5d2d15b6","sup_ecff66811dbe5f242371"],"title":"Familiar Presence Against Wild Absence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["95:1"],"branch_refs":["root_000190/B001"],"candidate_id":"cand_48990720f3b6373c54a3","commentary_obligation":"review","focus_branch_refs":["root_000190/B001"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":[],"root_ids":[],"scope":"pericope","source_local_id":"A:Fig and Olive Produce","source_type":"channel","support_ids":["sup_22b5079c586e4194db46","sup_5c78b35c82ed9c19b66d","sup_97191546bba009aa9770","sup_c372fe19efa187b2f191","sup_e0ef5d091445912a3ac9"],"title":"Fig and Olive Produce","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["95:1","95:2","95:3","95:4","95:6"],"branch_refs":["root_000190/B002"],"candidate_id":"cand_6c8d69e8b79051eb3910","commentary_obligation":"review","focus_branch_refs":["root_000190/B002"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":[],"root_ids":[],"scope":"pericope","source_local_id":"A:Mountain and Named Landmark","source_type":"channel","support_ids":["sup_0d18cf4245f1d374233c","sup_4abf56db290f6c94957d","sup_500ed083cb48ef5d00b2","sup_6c237407567a61958439","sup_8d8f721395d637e19635"],"title":"Mountain and Named Landmark","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["95:1","95:3","95:4","95:6"],"branch_refs":["root_000059/B001","root_001046/B012"],"candidate_id":"cand_f532461f05b2eb1eec37","commentary_obligation":"review","focus_branch_refs":[],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000059/B001","root_001046/B012"],"root_ids":[],"scope":"pericope","source_local_id":"A:Provisioned Human Group","source_type":"channel","support_ids":["sup_1342c3eb7ecbfe914bb9","sup_17962704df875a0e1dd2","sup_6b33542393d853a6f356","sup_85c90a0fc1461cecff70","sup_da386bcb2262447eb854"],"title":"Provisioned Human Group","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["95:1","95:4","95:6"],"branch_refs":["root_000656/B001"],"candidate_id":"cand_1d37b1a7789fb8cc933c","commentary_obligation":"review","focus_branch_refs":["root_000656/B001"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":[],"root_ids":[],"scope":"pericope","source_local_id":"B:Oil, Pressing, Trade, and Provision","source_type":"channel","support_ids":["sup_07ca19d59c9c0b8612da","sup_391abd11076b410a0c27","sup_b1b18e87e2dc4f0ab2d6","sup_c695fe5e6001a9c14222","sup_f8312d865510fcf5427f"],"title":"Oil, Pressing, Trade, and Provision","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["95:1","95:4","95:6","95:7"],"branch_refs":["root_000656/B003"],"candidate_id":"cand_d57d4b196caffdd3e548","commentary_obligation":"review","focus_branch_refs":["root_000656/B003"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":[],"root_ids":[],"scope":"pericope","source_local_id":"C:Oiling, Perfuming, and Recurrent Application","source_type":"channel","support_ids":["sup_2cdd3f8b8606464020b0","sup_555353fda551042fee86","sup_686276cccde88a29d142","sup_732b0adcdca6b1988b80","sup_9a59fa9c1a24c79b29e6"],"title":"Oiling, Perfuming, and Recurrent Application","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["95:1","95:2","95:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:1","branch_refs":["root_000054/B001","root_000148/B001","root_000190/B002","root_000656/B002","root_000955/B005"],"candidate_id":"cand_29f737daf46242eee0af","commentary_obligation":"review","hft_ref":"hft_891c83d7e1aeb5d71e7e","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_nested_protected_landscape","source_type":"hft","support_ids":["sup_82800c2b4f9d548de6ae"],"title":"delta_nested_protected_landscape","trust":"legacy_unbound"},{"anchor_refs":["95:1","95:4","95:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:1","branch_refs":["root_000190/B001","root_000323/B001","root_000434/B001","root_000555/B001","root_000656/B001","root_000715/B001","root_001273/B008"],"candidate_id":"cand_1ed8409f637f78bdb575","commentary_obligation":"review","hft_ref":"hft_9091e1cf7b421ddf3490","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_formed_yield_and_reversal","source_type":"hft","support_ids":["sup_6258318b0372247b0d28"],"title":"delta_formed_yield_and_reversal","trust":"legacy_unbound"},{"anchor_refs":["95:1","95:4","95:5","95:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:1","branch_refs":["root_000190/B001","root_000656/B004","root_000715/B004","root_001273/B009","root_001449/B002"],"candidate_id":"cand_3ca0913747e037aad56b","commentary_obligation":"review","hft_ref":"hft_ffb9a9f0034ac0cd696b","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_sustenance_as_qiwam","source_type":"hft","support_ids":["sup_d3fa10a303f4b206eb8c"],"title":"delta_sustenance_as_qiwam","trust":"legacy_unbound"},{"anchor_refs":["95:1","95:4","95:6","95:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:1","branch_refs":["root_000015/B001","root_000190/B001","root_000504/B002","root_000656/B004","root_000656/B005","root_001046/B004","root_001273/B010","root_001449/B001"],"candidate_id":"cand_7a61eae3b729c2a8c371","commentary_obligation":"review","hft_ref":"hft_1fc526760dd3de41a9b3","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_labor_value_and_uncut_return","source_type":"hft","support_ids":["sup_78430e46ce7bffb30fff"],"title":"delta_labor_value_and_uncut_return","trust":"legacy_unbound"},{"anchor_refs":["95:1","95:7","95:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:1","branch_refs":["root_000047/B002","root_000190/B001","root_000348/B002","root_000504/B002","root_000656/B001","root_001290/B001","root_001390/B001"],"candidate_id":"cand_5b549f19ba0d0adf50ea","commentary_obligation":"review","hft_ref":"hft_48833b804a57be4e33c1","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_oath_objects_as_evidence","source_type":"hft","support_ids":["sup_2ebba7b49bcbd77a091a"],"title":"delta_oath_objects_as_evidence","trust":"legacy_unbound"},{"anchor_refs":["95:1","95:2","95:3","95:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:1","branch_refs":["root_000054/B001","root_000059/B001","root_000148/B001","root_000190/B003","root_000656/B002","root_000955/B006"],"candidate_id":"cand_fdf8a65d88b5fe260f1a","commentary_obligation":"review","hft_ref":"hft_261ad29b2d4e9e93280c","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_wolf_to_cultivated_security","source_type":"hft","support_ids":["sup_11c5980695cc480bba28"],"title":"outlier_wolf_to_cultivated_security","trust":"legacy_unbound"},{"anchor_refs":["95:1","95:3","95:4","95:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:1","branch_refs":["root_000148/B006","root_000190/B001","root_000434/B009","root_000656/B003","root_001413/B001"],"candidate_id":"cand_6b14a928608c23465e5f","commentary_obligation":"review","hft_ref":"hft_24dcfbf6eb7678798376","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_coating_wear_and_exposure","source_type":"hft","support_ids":["sup_6925fdadbc27aa33354d"],"title":"outlier_coating_wear_and_exposure","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_6c5c17a2d75784e03d63","connection_ref":"conn_b9e275e5584329bfa149","note":"Direct next oath-member; establishes the mountain element required by the geographic sequence reading.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_a29f3f329245d464b662","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"95:2","source_note":"Immediate sequence context; ch017/ch023 preserves the landmark and outer-field reading.","source_row_role":"ranked_review","source_target_component_ref":"95:1","source_target_components":["95:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"95:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"95:2","source_target_components":["95:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"95:2","target_evidence":{"arabic_uthmani":"وَطُورِ سِينِينَ","ayah_ref":"95:2"},"target_ref":"95:2"},{"connection_evidence_ref":"conn_ev_f48e84acd4c9f3264731","connection_ref":"conn_2102238ce0a556fda889","note":"Directly supplies the surah's exception and enduring recompense, linking the oath sequence to human response.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_3eb29e2b8e8e58a741a8","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"95:6","source_note":"Local oath context, but no retained route to the focus readings.","source_row_role":"ranked_review","source_target_component_ref":"95:1","source_target_components":["95:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"95:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"95:6","source_target_components":["95:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"95:6","target_evidence":{"arabic_uthmani":"إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَلَهُمْ أَجْرٌ غَيْرُ مَمْنُونٍۢ","ayah_ref":"95:6"},"target_ref":"95:6"},{"connection_evidence_ref":"conn_ev_d53ae6ad297bbb592757","connection_ref":"conn_48e17955a9685d23caf7","note":"Direct continuation frames the ensuing issue as accountability, extending the scope of the opening oath.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_d3ecd414cc210d86380f","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"95:7","source_note":"Opens the focus surah's accumulating evidentiary sequence before its question.","source_row_role":"ranked_review","source_target_component_ref":"95:1","source_target_components":["95:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"95:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"95:7","source_target_components":["95:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"95:7","target_evidence":{"arabic_uthmani":"فَمَا يُكَذِّبُكَ بَعْدُ بِٱلدِّينِ","ayah_ref":"95:7"},"target_ref":"95:7"},{"connection_evidence_ref":"conn_ev_da18033bcc21cd0f70f0","connection_ref":"conn_eb9e27f9cf1696212fe1","note":"Directly gives the surah's affirmative statement about human formation, central to the sequence begun at 95:1.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_cb99940f69d06edf51ca","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"95:4","source_note":"Part of the oath setting, with no direct clarification of human formation.","source_row_role":"ranked_review","source_target_component_ref":"95:1","source_target_components":["95:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"95:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"95:4","source_target_components":["95:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"95:4","target_evidence":{"arabic_uthmani":"لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِىٓ أَحْسَنِ تَقْوِيمٍۢ","ayah_ref":"95:4"},"target_ref":"95:4"},{"connection_evidence_ref":"conn_ev_058a4ebcd7d4ebe86c40","connection_ref":"conn_8ff2d98817c0f65a7c40","note":"Direct next oath-member establishes the secure-city element of the geographic sequence reading.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_c48936356d9f1719efdd","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"95:3","source_note":"Immediate oath sequence establishes the parallel landmarks before the city.","source_row_role":"ranked_review","source_target_component_ref":"95:1","source_target_components":["95:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"95:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"95:3","source_target_components":["95:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"95:3","target_evidence":{"arabic_uthmani":"وَهَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ","ayah_ref":"95:3"},"target_ref":"95:3"},{"connection_evidence_ref":"conn_ev_402c93780d1722f1a602","connection_ref":"conn_53280d2c58292561dd41","note":"Directly supplies the downward reversal that qualifies the human-form statement following the oaths.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_639e655b070687a7e41d","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"95:5","source_note":"Part of the oath setting, with no distinct descent route.","source_row_role":"ranked_review","source_target_component_ref":"95:1","source_target_components":["95:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"95:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"95:5","source_target_components":["95:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"95:5","target_evidence":{"arabic_uthmani":"ثُمَّ رَدَدْنَٰهُ أَسْفَلَ سَٰفِلِينَ","ayah_ref":"95:5"},"target_ref":"95:5"},{"connection_evidence_ref":"conn_ev_5a2c71e1e716f2d3a2eb","connection_ref":"conn_97831be083436b02e2fc","note":"Direct closing question places the oath sequence within the surah's final judgment horizon.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_2bf3b0416852867bce13","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"95:8","source_note":"Begins the oath sequence whose argument closes at 95:8.","source_row_role":"ranked_review","source_target_component_ref":"95:1","source_target_components":["95:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"95:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"95:8","source_target_components":["95:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"95:8","target_evidence":{"arabic_uthmani":"أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ","ayah_ref":"95:8"},"target_ref":"95:8"}],"focus":{"arabic_uthmani":"وَٱلتِّينِ وَٱلزَّيْتُونِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"95:1:1:1","qac_word_ref":"95:1:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"95:1:1:2","qac_word_ref":"95:1:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"تِّين","morph_features":"STEM|POS:N|LEM:t~iyn|ROOT:tyn|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:1:1:3","qac_word_ref":"95:1:1","root_ar":"ت ي ن","surface_ar":"تِّينِ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"95:1:2:1","qac_word_ref":"95:1:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"95:1:2:2","qac_word_ref":"95:1:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"زَّيْتُون","morph_features":"STEM|POS:N|LEM:z~ayotuwn|ROOT:zyt|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:1:2:3","qac_word_ref":"95:1:2","root_ar":"ز ي ت","surface_ar":"زَّيْتُونِ"}],"word_analysis_qac_refs":[["95:1:1:1"],["95:1:1:2","95:1:1:3"],["95:1:2:1"],["95:1:2:2","95:1:2:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["95:1:1","95:1:2","95:1:3","95:1:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلتِّينِ وَٱلزَّيْتُونِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"95:1:1:1","qac_word_ref":"95:1:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"95:1:1:2","qac_word_ref":"95:1:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"تِّين","morph_features":"STEM|POS:N|LEM:t~iyn|ROOT:tyn|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:1:1:3","qac_word_ref":"95:1:1","root_ar":"ت ي ن","surface_ar":"تِّينِ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"95:1:2:1","qac_word_ref":"95:1:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"95:1:2:2","qac_word_ref":"95:1:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"زَّيْتُون","morph_features":"STEM|POS:N|LEM:z~ayotuwn|ROOT:zyt|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:1:2:3","qac_word_ref":"95:1:2","root_ar":"ز ي ت","surface_ar":"زَّيْتُونِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["95:1:1:1"],["95:1:1:2","95:1:1:3"],["95:1:2:1"],["95:1:2:2","95:1:2:3"]],"word_analysis_refs":["95:1:1","95:1:2","95:1:3","95:1:4"],"word_rows":[{"analysis_record_ref":"95:1:1","analytic_gloss_range_en":"surah-opening oath particle governing the following genitive fig noun, with connective force inside a repeated oath series","analytic_root_gloss_range_en":null,"qac_refs":["95:1:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"95:1:2","analytic_gloss_range_en":"definite genitive fig as a recognized sworn sign, locally botanical while allowing cautious place and sound-pressure associations","analytic_root_gloss_range_en":"accepted range includes the edible fig fruit and interpretations of the fig as a named place or mountain; unrelated dialectal wolf naming is not locally pressed by the ayah","qac_refs":["95:1:1:2","95:1:1:3"],"root":{"arabic":"ت ي ن","transliteration":"t-y-n"},"surface":{"arabic":"ٱلتِّينِ","transliteration":"al-tīni"}},{"analysis_record_ref":"95:1:3","analytic_gloss_range_en":"second oath-linking particle before the olive noun, keeping coordination and renewed oath force live inside the paired structure","analytic_root_gloss_range_en":null,"qac_refs":["95:1:2:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"95:1:4","analytic_gloss_range_en":"definite genitive olive as a collective tree or fruit sign, locally botanical with oil, provision, light, and place associations narrowed by the oath pair","analytic_root_gloss_range_en":"accepted range includes olive oil and extract, olive tree and fruit, oiling or anointing constructions, oil as provision, and oil-related occupations; the local noun selects the olive tree or fruit with product pressure","qac_refs":["95:1:2:2","95:1:2:3"],"root":{"arabic":"ز ي ت","transliteration":"z-y-t"},"surface":{"arabic":"ٱلزَّيْتُونِ","transliteration":"al-zaytūni"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":8,"missing_anchor_refs":[],"supplied_unique_anchor_count":8},"assigned_record_count":7,"assigned_records":[{"anchor_refs":["95:1","95:2","95:3"],"branch_refs":["root_000054/B001","root_000148/B001","root_000190/B002","root_000656/B002","root_000955/B005"],"candidate_id":"cand_29f737daf46242eee0af","evidence_scope":"declared_pericope","hft_ref":"hft_891c83d7e1aeb5d71e7e","item_id":"delta_nested_protected_landscape","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_nested_protected_landscape","support_id":"sup_82800c2b4f9d548de6ae"},{"anchor_refs":["95:1","95:4","95:5"],"branch_refs":["root_000190/B001","root_000323/B001","root_000434/B001","root_000555/B001","root_000656/B001","root_000715/B001","root_001273/B008"],"candidate_id":"cand_1ed8409f637f78bdb575","evidence_scope":"declared_pericope","hft_ref":"hft_9091e1cf7b421ddf3490","item_id":"delta_formed_yield_and_reversal","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_formed_yield_and_reversal","support_id":"sup_6258318b0372247b0d28"},{"anchor_refs":["95:1","95:4","95:5","95:6"],"branch_refs":["root_000190/B001","root_000656/B004","root_000715/B004","root_001273/B009","root_001449/B002"],"candidate_id":"cand_3ca0913747e037aad56b","evidence_scope":"declared_pericope","hft_ref":"hft_ffb9a9f0034ac0cd696b","item_id":"delta_sustenance_as_qiwam","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_sustenance_as_qiwam","support_id":"sup_d3fa10a303f4b206eb8c"},{"anchor_refs":["95:1","95:4","95:6","95:7"],"branch_refs":["root_000015/B001","root_000190/B001","root_000504/B002","root_000656/B004","root_000656/B005","root_001046/B004","root_001273/B010","root_001449/B001"],"candidate_id":"cand_7a61eae3b729c2a8c371","evidence_scope":"declared_pericope","hft_ref":"hft_1fc526760dd3de41a9b3","item_id":"delta_labor_value_and_uncut_return","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_labor_value_and_uncut_return","support_id":"sup_78430e46ce7bffb30fff"},{"anchor_refs":["95:1","95:7","95:8"],"branch_refs":["root_000047/B002","root_000190/B001","root_000348/B002","root_000504/B002","root_000656/B001","root_001290/B001","root_001390/B001"],"candidate_id":"cand_5b549f19ba0d0adf50ea","evidence_scope":"declared_pericope","hft_ref":"hft_48833b804a57be4e33c1","item_id":"delta_oath_objects_as_evidence","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_oath_objects_as_evidence","support_id":"sup_2ebba7b49bcbd77a091a"},{"anchor_refs":["95:1","95:2","95:3","95:4"],"branch_refs":["root_000054/B001","root_000059/B001","root_000148/B001","root_000190/B003","root_000656/B002","root_000955/B006"],"candidate_id":"cand_fdf8a65d88b5fe260f1a","evidence_scope":"declared_pericope","hft_ref":"hft_261ad29b2d4e9e93280c","item_id":"outlier_wolf_to_cultivated_security","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_wolf_to_cultivated_security","support_id":"sup_11c5980695cc480bba28"},{"anchor_refs":["95:1","95:3","95:4","95:5"],"branch_refs":["root_000148/B006","root_000190/B001","root_000434/B009","root_000656/B003","root_001413/B001"],"candidate_id":"cand_6b14a928608c23465e5f","evidence_scope":"declared_pericope","hft_ref":"hft_24dcfbf6eb7678798376","item_id":"outlier_coating_wear_and_exposure","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_coating_wear_and_exposure","support_id":"sup_6925fdadbc27aa33354d"}],"diagnostics":[],"lane_counts":{"global":9,"macro":7,"micro":3},"packet_summary":{"ayah_count":8,"focus_ref":"95:1","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر د د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000555","furuq_root_norm":"ر د د","furuq_source_root_norm":"ر د د","is_dominant":true,"target_occurrences":52,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001413","furuq_root_norm":"م ر د","furuq_source_root_norm":"م ر د","is_dominant":false,"target_occurrences":5,"target_rank":2}]}],"window":["95:1","95:2","95:3","95:4","95:5","95:6","95:7","95:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"95:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":10,"unstructured_record_count":0},"identity":{"ayah_ref":"95:1","lane":"macro","linguistic_source_ref":"95:1","surface_ref":"95:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"95:1","target_tokens":[["İncire",["95:1:1"]],["ve",["95:1:2"]],["zeytine",["95:1:2"]],["andolsun",["95:1:1","95:1:2"]]],"text":"İncire ve zeytine andolsun."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":7,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":8,"id":"s095-p01-001-008","label":"Whole surah","number":1,"refs":["95:1","95:2","95:3","95:4","95:5","95:6","95:7","95:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"95:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"95:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["95:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"95:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Oil, Pressing, Trade, and Provision","source_type":"channel","support_id":"sup_07ca19d59c9c0b8612da","text":"Extraction creates the product, specialized labor moves it into exchange, and provision carries it from seller to community. The oil is therefore simultaneously substance, commodity, and shared food.","trust":"trusted"},{"branch_refs":["root_000190/B002"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Mountain and Named Landmark","source_type":"channel","support_id":"sup_0d18cf4245f1d374233c","text":"fig-associated mountain place `ت ي ن:B002/m01`, mountain landmark `ط و ر:B005/m01`, bounded tract of land `ب ل د:B001/m01`, named places `ص ل ح:B005/m01`, mountain or elevated body-name `ح س ن:B004/m01`","trust":"trusted"},{"branch_refs":["root_000059/B001","root_001046/B012"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Provisioned Human Group","source_type":"channel","support_id":"sup_1342c3eb7ecbfe914bb9","text":"human collective `ء ن س:B001/m01`, people and men `ق و م:B001/m01`, attributed possessor or kin `ذ و و:B001/m01`, oil as group provision `ز ي ت:B004/m01`, manual workers `ع م ل:B006/m01`, travelers on foot `ع م ل:B012/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Familiar Presence Against Wild Absence","source_type":"channel","support_id":"sup_1500a4508ad33e941986","text":"Capacity appears as the ability to approach without fear, fit an intended role, bear a load, and continue rather than lag or stop.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Provisioned Human Group","source_type":"channel","support_id":"sup_17962704df875a0e1dd2","text":"95:1 `الزيتون`; 95:3 `هذا`; 95:4 `الإنسان`، `تقويم`; 95:6 `عملوا`","trust":"trusted"},{"branch_refs":["root_000059/B001","root_000190/B003"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Familiar Presence Against Wild Absence","source_type":"channel","support_id":"sup_181c3eec5c4b2950e49a","text":"human presence `ء ن س:B001/m01`, tame familiarity `ء ن س:B003/m01`, wildness beyond human familiarity `ط و ر:B006/m01`, absence of anyone in the place `ط و ر:B007/m01`, wolf named `تينان` `ت ي ن:B003/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Fig and Olive Produce","source_type":"channel","support_id":"sup_22b5079c586e4194db46","text":"Edible fig fruit and the olive tree or fruit appear as paired produce.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Oiling, Perfuming, and Recurrent Application","source_type":"channel","support_id":"sup_2cdd3f8b8606464020b0","text":"95:1 `الزيتون`; 95:4 `خلقنا`; 95:6 `عملوا`; 95:7 `بعد`","trust":"trusted"},{"branch_refs":["root_000656/B001"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"B:Oil, Pressing, Trade, and Provision","source_type":"channel","support_id":"sup_391abd11076b410a0c27","text":"olive oil and extract `ز ي ت:B001/m01`, oil seller or presser `ز ي ت:B005/m01`, oil as provision `ز ي ت:B004/m01`, commercial dealing `ع م ل:B005/m01`, recipient group `ق و م:B001/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Familiar Presence Against Wild Absence","source_type":"channel","support_id":"sup_465a62a27b3cddebfe3f","text":"Familiarity is spatial and social: a place is humanly occupied, a participant can be approached without hostility, and wildness marks movement beyond that relation. The named wolf supplies a concrete wild participant, while total absence is the limiting case in which no familiar participant remains.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Mountain and Named Landmark","source_type":"channel","support_id":"sup_4abf56db290f6c94957d","text":"95:1 `التين`; 95:2 `طور`; 95:3 `البلد`; 95:4 `أحسن`; 95:6 `الصالحات`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Mountain and Named Landmark","source_type":"channel","support_id":"sup_500ed083cb48ef5d00b2","text":"A place becomes intelligible through prominent terrain, named stations, residence, and the civic order maintained there.","trust":"trusted"},{"branch_refs":["root_000656/B003"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"C:Oiling, Perfuming, and Recurrent Application","source_type":"channel","support_id":"sup_555353fda551042fee86","text":"oiling and anointing `ز ي ت:B003/m01`, aromatic coating `خ ل ق:B010/m01`, intermittent recurrence `ب ع د:B007/m01`, trodden path `ع م ل:B011/m01`","trust":"trusted"},{"branch_refs":["root_000190/B001"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Fig and Olive Produce","source_type":"channel","support_id":"sup_5c78b35c82ed9c19b66d","text":"edible fig fruit `ت ي ن:B001/m01`, olive tree and fruit `ز ي ت:B002/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Familiar Presence Against Wild Absence","source_type":"channel","support_id":"sup_6175c0de0dbd5d2d15b6","text":"95:1 `التين`; 95:2 `طور`; 95:4 `الإنسان`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Oiling, Perfuming, and Recurrent Application","source_type":"channel","support_id":"sup_686276cccde88a29d142","text":"Oiling and perfuming share the action of laying a substance onto a surface. Intermittent recurrence renews the coating, while the trodden path extends repeated application into a surface marked and maintained by passage.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Provisioned Human Group","source_type":"channel","support_id":"sup_6b33542393d853a6f356","text":"A human group is identified by shared affiliation, manual work, travel, and provision.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Mountain and Named Landmark","source_type":"channel","support_id":"sup_6c237407567a61958439","text":"Mountain, tract, and place-name cooperate as a geography of recognition. The same naming process moves between ordinary terrain and elevated landmarks, allowing a lexical mountain sense of the fig to join the explicit mountain and city sequence.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Oiling, Perfuming, and Recurrent Application","source_type":"channel","support_id":"sup_732b0adcdca6b1988b80","text":"Fruit becomes oil and provision, then enters trade and repeated surface application as food, ointment, or fragrance.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Provisioned Human Group","source_type":"channel","support_id":"sup_85c90a0fc1461cecff70","text":"Human presence becomes a social group through affiliation and shared labor. Provision sustains the group, while hand-workers and foot-travelers show the collective in two recurrent modes: producing in place and moving together.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Mountain and Named Landmark","source_type":"channel","support_id":"sup_8d8f721395d637e19635","text":"Mountains and named places organize a landscape into recognizable sacred or inhabited landmarks.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Fig and Olive Produce","source_type":"channel","support_id":"sup_97191546bba009aa9770","text":"The two motifs form a direct food-and-cultivation pair: one names the fig as eaten fruit and the other the olive as both tree and fruit.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Oiling, Perfuming, and Recurrent Application","source_type":"channel","support_id":"sup_9a59fa9c1a24c79b29e6","text":"Oil or fragrance is spread over a surface and renewed through repeated application.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Oil, Pressing, Trade, and Provision","source_type":"channel","support_id":"sup_b1b18e87e2dc4f0ab2d6","text":"Olives yield oil, a specialist presses or sells it, and the product becomes food provision within a group.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Fig and Olive Produce","source_type":"channel","support_id":"sup_c372fe19efa187b2f191","text":"Fruit becomes oil and provision, then enters trade and repeated surface application as food, ointment, or fragrance.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Oil, Pressing, Trade, and Provision","source_type":"channel","support_id":"sup_c695fe5e6001a9c14222","text":"95:1 `الزيتون`; 95:4 `تقويم`; 95:6 `عملوا`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Provisioned Human Group","source_type":"channel","support_id":"sup_da386bcb2262447eb854","text":"Human beings form provisioned groups structured by possession, labor, rank, kinship, protection, and intimate attachment.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Fig and Olive Produce","source_type":"channel","support_id":"sup_e0ef5d091445912a3ac9","text":"95:1 `التين`، `الزيتون`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Familiar Presence Against Wild Absence","source_type":"channel","support_id":"sup_ecff66811dbe5f242371","text":"Human or tame presence occupies a place from which wildness, estrangement, or complete absence would otherwise withdraw.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Oil, Pressing, Trade, and Provision","source_type":"channel","support_id":"sup_f8312d865510fcf5427f","text":"Fruit becomes oil and provision, then enters trade and repeated surface application as food, ointment, or fragrance.","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلتِّينِ وَٱلزَّيْتُونِ","ayah_ref":"95:1"},{"arabic_uthmani":"وَطُورِ سِينِينَ","ayah_ref":"95:2"},{"arabic_uthmani":"وَهَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ","ayah_ref":"95:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000054/B001","root_000148/B001","root_000190/B002","root_000656/B002","root_000955/B005"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000190","role":"The named mountain or place carried by the fig keeps the first focus noun available as an actual coordinate.","root":"ت ي ن","source_ref":"95:1","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000656","role":"The olive tree and crop give the coordinate a cultivated ecological signature.","root":"ز ي ت","source_ref":"95:1","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_000955","role":"The mountain or mountain-name branch repeats the focus place scale and extends it into an explicit upland landmark.","root":"ط و ر","source_ref":"95:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000148","role":"The bounded tract of earth supplies a perimeter, converting loose landmarks into delimited inhabited space.","root":"ب ل د","source_ref":"95:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000054","role":"Calm security and trust qualify the bounded land as protected rather than merely enclosed.","root":"ء م ن","source_ref":"95:3","source_word_indices":["3"]}],"changed_reading":{"after":"The focus pair opens a protected-landscape itinerary in which productive terrain, mountain, bounded city, and security successively specify one spatial field.","before":"A place branch for the fig and a grove branch for the olive are only a lexical possibility."},"confidence":"strong","mechanism":"The following mountain, bounded land, and security cues turn the baseline place-and-grove possibility into a nested topography. The opening pair can mark productive terrain, the mountain extends the upland scale, and the deictically present secure city narrows the sequence to protected inhabited ground.","model_id":"delta_nested_protected_landscape","reader_inference":"The packet supplies place, mountain, bounded-earth, and security images in that order; I supply the arrow of spatial nesting and movement toward protected settlement. A live alternative is that the oath names independent referents without forming an itinerary.","status":"strengthened","structural_cues":["The first three ayat form one coordinated oath sequence: focus pair, mountain, then a deictically present city.","The sequence narrows from potentially named terrain and vegetation to bounded ground whose endpoint is explicitly secure."],"trigger_roots":["ط و ر","ب ل د","ء م ن"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_nested_protected_landscape","source_type":"hft","support_id":"sup_82800c2b4f9d548de6ae","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلتِّينِ وَٱلزَّيْتُونِ","ayah_ref":"95:1"},{"arabic_uthmani":"لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِىٓ أَحْسَنِ تَقْوِيمٍۢ","ayah_ref":"95:4"},{"arabic_uthmani":"ثُمَّ رَدَدْنَٰهُ أَسْفَلَ سَٰفِلِينَ","ayah_ref":"95:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000190/B001","root_000323/B001","root_000434/B001","root_000555/B001","root_000656/B001","root_000715/B001","root_001273/B008"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000190","role":"The fig eaten fresh or dried contributes one substance carried through a visible change of state.","root":"ت ي ن","source_ref":"95:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000656","role":"Oil as the olive's extracted yield contributes a latent content that becomes manifest through transformation.","root":"ز ي ت","source_ref":"95:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000434","role":"Creation as measuring and proportioning supplies the operation by which an achieved form is set.","root":"خ ل ق","source_ref":"95:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000323","role":"Beauty opposed to ugliness supplies a qualitative pole for the formed result.","root":"ح س ن","source_ref":"95:4","source_word_indices":["5"]},{"branch_id":"B008","mapped_root_id":"root_001273","role":"Straightness, moderation, and levelness give the human form an upright equilibrium rather than a static shape alone.","root":"ق و م","source_ref":"95:4","source_word_indices":["6"]},{"branch_id":"B001","mapped_root_id":"root_000555","role":"Returning a thing to a prior place supplies the reversal arrow that makes achieved form nonfinal.","root":"ر د د","source_ref":"95:5","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000715","role":"Physical low position supplies the downward endpoint of the reversal.","root":"س ف ل","source_ref":"95:5","source_word_indices":["3","4"]}],"changed_reading":{"after":"They also become small material demonstrations of formed yield: a good state can be achieved and disclosed, yet still be returned into another condition.","before":"Drying and extraction make the pair durable provisions."},"confidence":"medium","mechanism":"Fresh-to-dried fruit and fruit-to-oil extraction make the focus pair examples of achieved material states. Measuring creation, beauty, upright balance, return, and lowering then recast those yields as analogues for form that is produced, disclosed, and reversible rather than simply possessed.","model_id":"delta_formed_yield_and_reversal","reader_inference":"The packet supplies processed plant states and a measured-upright-to-lowered sequence; I supply the analogy that plant yield prefigures the making and unmaking of form. The live alternative is that the plants remain oath objects with no material analogy to the human sequence.","status":"revised","structural_cues":["The superlative contrast between best and lowest brackets a directional turn introduced by then.","The context moves from an act of forming to a return, so state change rather than fixed classification controls the sequence."],"trigger_roots":["خ ل ق","ح س ن","ق و م","ر د د","س ف ل"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_formed_yield_and_reversal","source_type":"hft","support_id":"sup_6258318b0372247b0d28","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلتِّينِ وَٱلزَّيْتُونِ","ayah_ref":"95:1"},{"arabic_uthmani":"لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِىٓ أَحْسَنِ تَقْوِيمٍۢ","ayah_ref":"95:4"},{"arabic_uthmani":"ثُمَّ رَدَدْنَٰهُ أَسْفَلَ سَٰفِلِينَ","ayah_ref":"95:5"},{"arabic_uthmani":"إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَلَهُمْ أَجْرٌ غَيْرُ مَمْنُونٍۢ","ayah_ref":"95:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000190/B001","root_000656/B004","root_000715/B004","root_001273/B009","root_001449/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000190","role":"The edible fig supplies immediate nourishment as one material support of life.","root":"ت ي ن","source_ref":"95:1","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000656","role":"Oil as condiment and provision supplies stored sustenance that can maintain a person or group.","root":"ز ي ت","source_ref":"95:1","source_word_indices":["2"]},{"branch_id":"B009","mapped_root_id":"root_001273","role":"Qiwam as pillar, subsistence, and livelihood explicitly joins economic sustenance to structural support.","root":"ق و م","source_ref":"95:4","source_word_indices":["6"]},{"branch_id":"B004","mapped_root_id":"root_000715","role":"The act of moving downward supplies the collapse that contrasts with maintained standing.","root":"س ف ل","source_ref":"95:5","source_word_indices":["3","4"]},{"branch_id":"B002","mapped_root_id":"root_001449","role":"The force by which something stands, or the loss of that force, makes continuity of support the mechanism's hinge.","root":"م ن ن","source_ref":"95:6","source_word_indices":["9"]}],"changed_reading":{"after":"Fig and olive become the material qiwam of the body: provision imagined as the support that keeps formed life standing against decline.","before":"Fig and olive are signs or instances of nourishment."},"confidence":"medium","mechanism":"The focus foods can be read as qiwam: livelihood that acts like a supporting pillar. Upright form, downward movement, and the force by which a thing stands or loses strength make nourishment function as material maintenance of embodied standing, not merely as abundance.","model_id":"delta_sustenance_as_qiwam","reader_inference":"The packet supplies foods, provision, livelihood-as-pillar, descent, and sustaining force; I infer that nourishment is one material condition of continued uprightness. A live alternative is that qiwam remains formal or moral and the foods do not enter its causal chain.","status":"new","structural_cues":["Best upright formation is followed by downward return, then by an exception whose reward is described through noncessation.","The repeated standing-versus-lowering axis lets concrete provisions at the opening participate in the maintenance of form."],"trigger_roots":["ق و م","س ف ل","م ن ن"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_sustenance_as_qiwam","source_type":"hft","support_id":"sup_d3fa10a303f4b206eb8c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلتِّينِ وَٱلزَّيْتُونِ","ayah_ref":"95:1"},{"arabic_uthmani":"لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِىٓ أَحْسَنِ تَقْوِيمٍۢ","ayah_ref":"95:4"},{"arabic_uthmani":"إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَلَهُمْ أَجْرٌ غَيْرُ مَمْنُونٍۢ","ayah_ref":"95:6"},{"arabic_uthmani":"فَمَا يُكَذِّبُكَ بَعْدُ بِٱلدِّينِ","ayah_ref":"95:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000015/B001","root_000190/B001","root_000504/B002","root_000656/B004","root_000656/B005","root_001046/B004","root_001273/B010","root_001449/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000190","role":"The edible fig, preserved fresh or dried, supplies a finite crop that can be stored and circulated.","root":"ت ي ن","source_ref":"95:1","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000656","role":"Oil as provision or gift supplies the distributable good around which exchange and obligation can form.","root":"ز ي ت","source_ref":"95:1","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_000656","role":"The presser and seller expose the otherwise hidden labor and market roles behind the olive product.","root":"ز ي ت","source_ref":"95:1","source_word_indices":["2"]},{"branch_id":"B010","mapped_root_id":"root_001273","role":"Valuation and pricing supply the operation that assigns exchange value to produced goods.","root":"ق و م","source_ref":"95:4","source_word_indices":["6"]},{"branch_id":"B004","mapped_root_id":"root_001046","role":"The wage and provision of a worker connect intentional labor to a due material return.","root":"ع م ل","source_ref":"95:6","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000015","role":"Recompense for work or hire formalizes the return side of the labor relation.","root":"ء ج ر","source_ref":"95:6","source_word_indices":["7"]},{"branch_id":"B001","mapped_root_id":"root_001449","role":"Cutting and diminishing until extension ceases supply the finite limit that the grammatical negation refuses.","root":"م ن ن","source_ref":"95:6","source_word_indices":["9"]},{"branch_id":"B002","mapped_root_id":"root_000504","role":"Accounting and recompense extend the crop-and-wage chain into a final reckoning of value.","root":"د ي ن","source_ref":"95:7","source_word_indices":["4"]}],"changed_reading":{"after":"It opens a miniature labor economy—crop, processing, provision, price, wage, and account—whose finite returns are exceeded by a reward that is not cut off.","before":"The opening pair shows preserved food available for human use."},"confidence":"medium","mechanism":"The oil presser and seller already place labor and exchange inside the focus. Later valuation, work-wage, recompense, possible cutting-off, and accounting unfold that seed into an economy: finite crops are processed and priced, while the promised return is emphatically not exhausted like ordinary provision.","model_id":"delta_labor_value_and_uncut_return","reader_inference":"The packet supplies crop, presser, seller, pricing, wage, recompense, cutting, and accounting branches; I compose them into an economy and infer a contrast between finite market return and uncut recompense. A live alternative is that these are independent ethical terms rather than one exchange mechanism.","status":"strengthened","structural_cues":["The sequence moves from work to a possessed recompense qualified as uncut, then immediately asks about accounting or requital.","The focus pair itself contains both raw crop and a product whose pressing, provisioning, gifting, and selling imply a chain of hands."],"trigger_roots":["ق و م","ع م ل","ء ج ر","م ن ن","د ي ن"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_labor_value_and_uncut_return","source_type":"hft","support_id":"sup_78430e46ce7bffb30fff","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلتِّينِ وَٱلزَّيْتُونِ","ayah_ref":"95:1"},{"arabic_uthmani":"فَمَا يُكَذِّبُكَ بَعْدُ بِٱلدِّينِ","ayah_ref":"95:7"},{"arabic_uthmani":"أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ","ayah_ref":"95:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000047/B002","root_000190/B001","root_000348/B002","root_000504/B002","root_000656/B001","root_001290/B001","root_001390/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000190","role":"The directly edible fig supplies a manifest yield that can function as the first material exhibit.","root":"ت ي ن","source_ref":"95:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000656","role":"Oil as extracted olive yield supplies a second exhibit whose content becomes evident only through disclosure.","root":"ز ي ت","source_ref":"95:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001290","role":"Falsehood as the contrary of truth creates the contested claim for which the oath objects can serve as evidence.","root":"ك ذ ب","source_ref":"95:7","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000504","role":"Accounting and recompense define what is at stake in the contested claim.","root":"د ي ن","source_ref":"95:7","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001390","role":"Negation that denies a state supplies the closing interrogative challenge to denial.","root":"ل ي س","source_ref":"95:8","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000047","role":"The divine name's use in oath and invocation reinforces the formal oath frame surrounding the focus objects.","root":"ء ل ه","source_ref":"95:8","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000348","role":"Judgment between people supplies the tribunal role that converts invoked objects into evidentiary witnesses.","root":"ح ك م","source_ref":"95:8","source_word_indices":["3","4"]}],"changed_reading":{"after":"Fig and olive act as paired material witnesses—one manifest, one extractable—in an argument that moves from testimony through denial to judgment.","before":"Fig and olive are objects invoked to intensify a later assertion."},"confidence":"medium","mechanism":"Denial, accounting, negation, oath-language, and judgment retrospectively juridicize the opening coordination. The fig's manifest edible fruit and the olive's extractable inner yield become two kinds of exhibit—yield immediately seen and yield disclosed by pressure—inside a case about whether formed life can be assessed and requited.","model_id":"delta_oath_objects_as_evidence","reader_inference":"The packet supplies oath-capable divine naming, truth-versus-falsehood, accounting, negation, and judging; I infer a juridical arrow that makes the opening objects exhibits rather than ornament. A live alternative is a general rhetorical emphasis with no courtroom-like mechanism.","status":"new","structural_cues":["The opening coordinated oath is answered by a claim about human formation and then by questions concerning denial, requital, and the best judge.","The final negative interrogative does not merely conclude the oath; it stages assent as the expected verdict."],"trigger_roots":["ك ذ ب","د ي ن","ل ي س","ء ل ه","ح ك م"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_oath_objects_as_evidence","source_type":"hft","support_id":"sup_2ebba7b49bcbd77a091a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلتِّينِ وَٱلزَّيْتُونِ","ayah_ref":"95:1"},{"arabic_uthmani":"وَطُورِ سِينِينَ","ayah_ref":"95:2"},{"arabic_uthmani":"وَهَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ","ayah_ref":"95:3"},{"arabic_uthmani":"لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِىٓ أَحْسَنِ تَقْوِيمٍۢ","ayah_ref":"95:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000054/B001","root_000059/B001","root_000148/B001","root_000190/B003","root_000656/B002","root_000955/B006"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000190","role":"The dialectal name for a wolf inserts a predator at the edge of the ordinary fig reading.","root":"ت ي ن","source_ref":"95:1","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000656","role":"The cultivated olive tree and crop provide the settled agricultural counterpole to the wolf.","root":"ز ي ت","source_ref":"95:1","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_000955","role":"Wildness and departure from familiar human limits give the wolf branch an environmental domain rather than leaving it isolated.","root":"ط و ر","source_ref":"95:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000148","role":"Bounded ground supplies the perimeter across which wild and cultivated domains can be contrasted.","root":"ب ل د","source_ref":"95:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000054","role":"Security and settled trust make the bounded cultivated side explicitly safe.","root":"ء م ن","source_ref":"95:3","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000059","role":"The human defined against wildness supplies the social threshold through which the predator-to-cultivation contrast passes.","root":"ء ن س","source_ref":"95:4","source_word_indices":["3"]}],"changed_reading":{"after":"At the lexical fringe, it can flicker as a crossing from wolf and wilderness toward olive cultivation, bounded settlement, security, and the human.","before":"The focus begins with two cultivated foods."},"confidence":"exploratory","containment":"This is surprising because it activates the rare dialectal wolf-name rather than the ordinary fig, yet it remains anchored in the exact focus branch and is independently stirred by later wilderness, bounded-land, security, and human-versus-wild branches. Downstream prose should present it only as a lexical flicker or punning countercurrent, never as a replacement gloss for the focus noun.","focus_anchor":"The ت ي ن noun at word 1 through its dialectal wolf-name branch, contrasted with the cultivated olive at word 2.","outlier_id":"outlier_wolf_to_cultivated_security"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_wolf_to_cultivated_security","source_type":"hft","support_id":"sup_11c5980695cc480bba28","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلتِّينِ وَٱلزَّيْتُونِ","ayah_ref":"95:1"},{"arabic_uthmani":"وَهَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ","ayah_ref":"95:3"},{"arabic_uthmani":"لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِىٓ أَحْسَنِ تَقْوِيمٍۢ","ayah_ref":"95:4"},{"arabic_uthmani":"ثُمَّ رَدَدْنَٰهُ أَسْفَلَ سَٰفِلِينَ","ayah_ref":"95:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000148/B006","root_000190/B001","root_000434/B009","root_000656/B003","root_001413/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000190","role":"The edible fig's fresh and dried states supply a visible alteration of moisture, texture, and surface.","root":"ت ي ن","source_ref":"95:1","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000656","role":"Oiling or anointing the head and body supplies an applied protective or beautifying surface layer.","root":"ز ي ت","source_ref":"95:1","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_000148","role":"A mark on skin or body makes the context's spatial noun touch the body's visible surface.","root":"ب ل د","source_ref":"95:3","source_word_indices":["2"]},{"branch_id":"B009","mapped_root_id":"root_000434","role":"A garment worn until its nap disappears contributes gradual loss of an outer covering.","root":"خ ل ق","source_ref":"95:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001413","role":"The non-dominant mapped branch's stripping away of what covers a thing supplies the terminal exposure in the surface sequence.","root":"ر د د","source_ref":"95:5","source_word_indices":["2"]}],"changed_reading":{"after":"The pair can also initiate a fragile surface sequence—drying, coating, marking, wearing away, and stripping—that makes formed embodiment vulnerable to exposure.","before":"The pair consists of foods with different uses."},"confidence":"exploratory","containment":"This cross-domain surface reading is surprising, especially because its final stripping cue comes from the non-dominant م ر د inventory mapped from ر د د. It remains valid as an activation because fresh-versus-dried fig and oiling are exact focus branches, while bodily marking, surface wear, and stripping recur in the context inventories. Downstream prose should qualify it as a material analogy about covering and exposure, not as ordinary lexical sense or a claim that the split root controls the ayah.","focus_anchor":"The fig's fresh/dried material states and the olive's oiling or anointing branch.","outlier_id":"outlier_coating_wear_and_exposure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_coating_wear_and_exposure","source_type":"hft","support_id":"sup_6925fdadbc27aa33354d","trust":"legacy_unbound"}]}
</lane_packet_json>
