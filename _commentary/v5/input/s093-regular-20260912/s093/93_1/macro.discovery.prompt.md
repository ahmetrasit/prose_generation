# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **93:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s093-regular-20260912/s093/93_1/macro.discovery.json` and modify nothing
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
  "ayah_ref": "93:1",
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
{"branch_registry":[{"boundary":"Includes rabab/rabab as abundant water, also said of sweet water, with Maqayis explaining it through gathering.","branch_kind":null,"branch_ref":"root_000532/B013","candidate_links":[{"candidate_id":"cand_f74d9c49655ec0033d3e","lane":"macro"}],"focus_root_occurrences":[],"gloss":"abundant collected water","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"ماء رَبَب كثير","image_en":"abundant collected water"}}],"root_ar":"ر ب ب","root_id":"root_000532","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"ماء رَبَب كثير","image_en":"abundant collected water","scope_ar":"يدخل فيه الربب للماء الكثير، ويقال للعذب، من جهة اجتماع الماء","scope_en":"Includes rabab/rabab as abundant water, also said of sweet water, with Maqayis explaining it through gathering."},"support_links":["sup_645641411e9d6ab59351"]},{"boundary":"Includes rab-rab as a herd, especially wild cattle, and in one report cattle or camels together.","branch_kind":null,"branch_ref":"root_000532/B014","candidate_links":[{"candidate_id":"cand_2f1774b551cc0019f472","lane":"macro"}],"focus_root_occurrences":[],"gloss":"herd or gathered wild cattle","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"رَبْرَب قطيع","image_en":"herd or gathered wild cattle"}}],"root_ar":"ر ب ب","root_id":"root_000532","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"رَبْرَب قطيع","image_en":"herd or gathered wild cattle","scope_ar":"يدخل فيه الربرب لقطيع بقر الوحش، وقيل لجماعة البقر أو الإبل","scope_en":"Includes rab-rab as a herd, especially wild cattle, and in one report cattle or camels together."},"support_links":["sup_2a30b6a52dd9e12a63f4"]},{"boundary":"Includes the settling or stilling of night, sea or waves, wind, and the quiet or languid gaze.","branch_kind":null,"branch_ref":"root_000679/B001","candidate_links":[{"candidate_id":"cand_2271495035bc343d417f","lane":"macro"},{"candidate_id":"cand_63364e129fe9629ecfa7","lane":"macro"},{"candidate_id":"cand_41d6d0fa51c3464365a2","lane":"macro"}],"focus_root_occurrences":[],"gloss":"still settling and closing-in","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"السكون والركود مع إطباق الليل أو البحر أو الطرف","image_en":"still settling and closing-in"}}],"root_ar":"س ج و","root_id":"root_000679","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"السكون والركود مع إطباق الليل أو البحر أو الطرف","image_en":"still settling and closing-in","scope_ar":"يدخل فيه سكون الليل وركوده أو إظلامه ودوامه، وسكون البحر وأمواجه، وسكون الريح، وفتور الطرف وسكونه.","scope_en":"Includes the settling or stilling of night, sea or waves, wind, and the quiet or languid gaze."},"support_links":["sup_505eb59f90dcf7b91ffd","sup_6de832772998fb3b589c","sup_d1851db359b0882caaa9"]},{"boundary":"Bu dal güneşe çıkmayı, görünür olmayı, yemek yemeyi ya da hayvan kesmeyi değil, bunlara ad verebilen gündüz vaktini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B001","candidate_links":[{"candidate_id":"cand_2271495035bc343d417f","lane":"macro"},{"candidate_id":"cand_f74d9c49655ec0033d3e","lane":"macro"},{"candidate_id":"cand_63364e129fe9629ecfa7","lane":"macro"},{"candidate_id":"cand_88e57ac020c8cec56f94","lane":"macro"},{"candidate_id":"cand_715c89701200b5aaa9bd","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","surface_ar":"ضُّحَىٰ"}],"gloss":"güneş yükseldikten sonraki kuşluk vakti","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güneş doğduktan sonra gün yükselir ve erken aydınlık zaman dilimi başlar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu zaman, doğuşun hemen sonrasından başlayıp günün uzadığı ve öğleye yaklaştığı daha ileri aşamalara ayrılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yerde bu vakte kadar kalmak veya bir eylemi vaktin yükselmesine kadar geciktirmek zaman anlamına bağlı kullanımlardır."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın doğuş sonrası başlayıp öğleye yaklaşan temel zaman alanını doğal ve kısa biçimde karşılar.","boundary_detail":"Bu dal güneşe çıkmayı, görünür olmayı, yemek yemeyi ya da hayvan kesmeyi değil, bunlara ad verebilen gündüz vaktini anlatır.","branch_image_ar":"امتداد الضحى في النهار","concept_gloss":"güneş yükseldikten sonraki kuşluk vakti","contextual_glosses":[{"applicability":"Zaman dizisinin ilk aşamasını özellikle belirtmek gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öğleye yaklaşan daha ileri kuşluk aşamalarını dışarıda bırakır.","preserves":"Doğuş sonrasındaki erken gündüz zamanını korur."},"facet_ids":["F001"],"text":"güneş doğduktan hemen sonraki vakit","usage_role":"contextual"},{"applicability":"Bir eylemin erken gündüzün daha ileri bir aşamasına bırakıldığını anlatan cümlelere uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Zaman alanının doğuşa yakın ilk aşamasını karşılamaz.","preserves":"Günün yükselmesini ve eylemin o zamana bağlanmasını korur."},"facet_ids":["F002","F003"],"text":"gün iyice yükselince","usage_role":"contextual"}],"definition":"Güneş doğduktan sonra günün yükselip yayılmasıyla başlayan, aşamalar halinde ilerleyerek öğleye yaklaşan erken aydınlık zaman dilimidir. Bir yerde bu vakte kadar kalma veya bir işi bu vaktin daha ileri aşamasına bırakma kullanımları bu zaman çekirdeğine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güneş doğduktan sonra gün yükselir ve erken aydınlık zaman dilimi başlar."},{"facet_id":"F002","role":"specialization","statement":"Bu zaman, doğuşun hemen sonrasından başlayıp günün uzadığı ve öğleye yaklaştığı daha ileri aşamalara ayrılır."},{"facet_id":"F003","role":"associated_use","statement":"Bir yerde bu vakte kadar kalmak veya bir eylemi vaktin yükselmesine kadar geciktirmek zaman anlamına bağlı kullanımlardır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Güneş doğmadan önceki ve dalın kapsamadığı daha geniş zaman aralığını da ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Günün erken bölümünde bulunma özelliğini korur."},"text":"sabah"}],"identity_rationale":"Kaynak ifadesi, güneş doğduktan sonra başlayan ve gün yükseldikçe ilerleyen bir zaman dizisini açıkça verir. Çerçevedeki günün yükselmesi ve uzaması bu diziyi doğru karşılar; eylemi bu zamana bırakma ise zaman anlamına bağlı bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"günün yükseldiği erken vakit"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kuşluk vakti"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"günün uzayıp öğleye yaklaştığı kuşluk vakti"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"güneş doğduktan sonraki ilk kuşluk vakti"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kuşluk vaktine girmek veya o vakte kadar kalmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kuşluk namazını vakit iyice yükselene kadar geciktirmek"}],"lexicalization_note":"Tanım, günün erken aydınlık bölümünü temel alır; bu vakte girme ve bir işi vaktin ilerisine bırakma yalnızca ilgili biçim ve söz öbeklerine bağlıdır.","neighbor_coverage_note":"Verilen bütün komşu kartları değerlendirildi; zaman sınırını en açık gösteren üç karşılaştırma seçildi, yalnızca aynı gün içindeki olayları anan daha uzak adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir erken gündüz zaman alanını ve onun aşamalarını adlandırır; komşu dal ise günün yükselmesini bir oluş olarak anlatır ve kaynak kartında daha geç bir güneş konumuna da uzanır.","focus_only":"Doğuş sonrasından öğleye yaklaşmaya kadar uzanan adlandırılmış zaman aşamalarını ve eylemi o vakte bırakmayı kapsar.","gloss":"günün yükselmesi","neighbor_only":"Günün yükselmesi yanında bazı kullanımlarda güneşin duvarlardan çekilmeye başlamasını da kapsar.","neighbor_ref":"root_000546/B012","relation_type":"near_synonym","shared_zone":"İki dal da gündüzün yükselip yayılmasını zaman belirleyici bir özellik olarak kullanır."},{"boundary_match":"partial","distinction":"Odak dalın gönderimi zamandır; komşunun çekirdeği ise dikleşme ve yükselme hareketidir. Bu nedenle olağan bağlamlarda birbirlerinin yerine geçmezler.","focus_only":"Güneş doğduktan sonra ilerleyen zaman dilimini adlandırır.","gloss":"yükselen gündüz","neighbor_only":"Bir şeyin dikilmesini ve doğrulmasını temel alıp günün yükselmesini bu çekirdeğin bir uygulaması olarak verir.","neighbor_ref":"root_000642/B012","relation_type":"near_neighbor","shared_zone":"Her ikisinde de gündüzün yükselmesi ortak bir görüntüdür."},{"boundary_match":"field_only","distinction":"Birinci dal zamansal bir bölümdür; ikinci dal ise maruz kalma veya görünürlük durumudur. Aynı güneşli sahneyi paylaşmaları anlamlarını birleştirmez.","focus_only":"Güneşin yükselmesine göre belirlenen bir gündüz vaktini anlatır.","gloss":"vakit ile güneşe açıklık","neighbor_only":"Güneşe açık kalmayı, görünür olmayı ve dışta bulunan belirgin yanı anlatır.","neighbor_ref":"root_000904/B002","relation_type":"same_field","shared_zone":"Her iki dal da güneş ve açık gündüz çevresinde örgütlenir."}],"source_phrase_ar":"الضحاء امتداد النهار (maqayis); الضحو ارتفاع النهار والضحى فويق ذلك والضحاء ممدود إذا امتد النهار (ayn); الضحو لغة في الضحى (jamhara); ضحوة النهار بعد طلوع الشمس ثم بعده الضحى ثم بعده الضحاء (sihah); الضحى انبساط الشمس وامتداد النهار وسمي الوقت به (mufradat)","source_summary":"Kaynakların ortak çizgisi, güneş doğduktan sonra günün yükselmesiyle açılan ve öğleye doğru ilerleyen bir zaman alanıdır. Adlandırmalar bu alanın birbirini izleyen erken ve ileri aşamalarını, ayrıca eylemin o vakte ulaşmasını anlatır.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الضحو والضحى والضحاء ووقت ارتفاع النهار وتأخير الفعل إلى ذلك الوقت","what_is_not_ar":"لا يدخل فيه مجرد البروز للشمس ولا الذبيحة ولا الطعام إلا من جهة التسمية بالوقت"},"support_links":["sup_289cdad6e176c1e5f988","sup_505eb59f90dcf7b91ffd","sup_645641411e9d6ab59351","sup_6de832772998fb3b589c","sup_a866c9b415f3ebb29fad"]},{"boundary":"Dal, gündüz vaktinin kendisini değil, güneşe veya bakışa açık olma ve böylece belirginleşme durumunu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B002","candidate_links":[{"candidate_id":"cand_63364e129fe9629ecfa7","lane":"macro"},{"candidate_id":"cand_c78647c4b0d26dfb83dc","lane":"macro"},{"candidate_id":"cand_54a85c000f3ccb10e233","lane":"macro"},{"candidate_id":"cand_96ba0348ec5d77399a50","lane":"macro"},{"candidate_id":"cand_e1333bfc096aa9d84ce7","lane":"macro"},{"candidate_id":"cand_6d937e7faf936862aea0","lane":"macro"},{"candidate_id":"cand_0ea93d667e05b71df20e","lane":"macro"},{"candidate_id":"cand_d89fb0da4706ffd68a79","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","surface_ar":"ضُّحَىٰ"}],"gloss":"güneşe veya bakışa açık olup görünürleşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şey güneşe ya da bakışa açık hale gelir ve görünür olur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yerin dışta kalan belirgin yanı, açık kenarı veya sürekli güneş alan bölümü aynı görünürlük çekirdeğiyle adlandırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir işi açıkça ve herkesin görebileceği biçimde yapmak, görünür olmanın eylem alanındaki kullanımıdır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Güneş ısısına maruz kalma ve bununla bağlantılı terleme, güneşe açıklığın bedensel sonucudur."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın güneşe maruz kalma ile dışta ve görünür olma arasındaki ortak çekirdeğini birlikte karşılar.","boundary_detail":"Dal, gündüz vaktinin kendisini değil, güneşe veya bakışa açık olma ve böylece belirginleşme durumunu anlatır.","branch_image_ar":"البروز للشمس والظهور","concept_gloss":"güneşe veya bakışa açık olup görünürleşme","contextual_glosses":[{"applicability":"Bir kişinin ya da şeyin güneşe maruz kalmasını anlatan bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bakışa görünür olma, dış kenar ve alenen yapma kullanımlarını karşılamaz.","preserves":"Güneşe açık hale gelme ve ısıya maruz kalma yönünü korur."},"facet_ids":["F001","F004"],"text":"güneşe çıkmak","usage_role":"contextual"},{"applicability":"Yolun, yerin veya başka bir şeyin belirgin biçimde görünmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneş ısısına maruz kalma ve terleme yönünü dışarıda bırakır.","preserves":"Bakışa açık ve belirgin olma yönünü korur."},"facet_ids":["F001","F002"],"text":"açıkça görünmek","usage_role":"contextual"},{"applicability":"Bir eylemin gizlenmeden ve herkesin görebileceği biçimde yapılmasına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yer, güneş ve bedensel maruz kalma kullanımlarını karşılamaz.","preserves":"Eylemin bakışa açık ve belirgin biçimde yapılmasını korur."},"facet_ids":["F003"],"text":"alenen yapmak","usage_role":"contextual"}],"definition":"Bir kişinin, yerin ya da şeyin güneşe veya bakışa açık duruma gelmesi ve böylece dışta, belirgin ya da görünür olmasıdır. Güneş ısısına maruz kalma ve terleme ile bir işi açıkça yapma, bu çekirdeğin bağlama bağlı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şey güneşe ya da bakışa açık hale gelir ve görünür olur."},{"facet_id":"F002","role":"extension","statement":"Bir yerin dışta kalan belirgin yanı, açık kenarı veya sürekli güneş alan bölümü aynı görünürlük çekirdeğiyle adlandırılır."},{"facet_id":"F003","role":"associated_use","statement":"Bir işi açıkça ve herkesin görebileceği biçimde yapmak, görünür olmanın eylem alanındaki kullanımıdır."},{"facet_id":"F004","role":"associated_use","statement":"Güneş ısısına maruz kalma ve bununla bağlantılı terleme, güneşe açıklığın bedensel sonucudur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneşe maruz kalmayı, dışta kalan yanı ve alenen yapma kapsamını tam olarak taşımaz.","preserves":"Görünür ve belirgin hale gelme yönünü korur."},"text":"ortaya çıkma"}],"identity_rationale":"Kaynak ifadesi güneşe çıkma, güneş ısısına maruz kalma, görünür hale gelme, dışta ve açıkta bulunan yan ile bir işi herkesin görebileceği biçimde yapma kullanımlarını birlikte destekler. Terleme, bu alanın bağımsız çekirdeği değil, güneş ısısına maruz kalmayla bağlantılı bir sonuçtur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"güneşe çıkmak veya güneşin ısısına maruz kalmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"güneşe çık"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yol görünür hale geldi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yerleşimin dışta ve açıkta kalan yanı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"dışta kalan açık bölgeler veya kenarlar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bunu açıkça ve herkesin gözü önünde yaptı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"açıkta ve görünür yer"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"güneşin neredeyse hiç eksik olmadığı yer"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"atın bacakları arasındaki bölüm görünür olur"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"terledim"}],"lexicalization_note":"Güneşe çıkma ve görünür olma ortak çekirdektir; yolun görünmesi, açık yer, dış kenar, alenen yapma ve terleme ilgili biçim ve söz öbeklerinin ayrı gerçekleşmeleridir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel görünürlük dalları ile aynı kökün zaman dalı sınırı en çok keskinleştirdiği için yayımlandı, yalnızca dolaylı güneş veya açıklık çağrışımı taşıyanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu genel görünme ve açığa çıkma alanındadır; odak dal ise bu alanı güneşe açıklık, dış kenar ve açıkça yapılan eylemle özel olarak birleştirir.","focus_only":"Güneşe çıkmayı, güneş ısısına maruz kalmayı, dışta kalan yanı ve terlemeyi kapsar.","gloss":"açığa çıkıp görünür olma","neighbor_only":"Gizli veya içte olanın genel olarak açığa çıkıp anlaşılır hale gelmesini kapsar.","neighbor_ref":"root_000970/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin dışta, açık ve görünür olmasını anlatır."},{"boundary_match":"partial","distinction":"Odak için önceden gizli olma şart değildir ve güneş altında bulunma belirgindir; komşu ise gizlilikten görünürlüğe geçişi temel alır.","focus_only":"Güneşe maruz kalma ile öteden beri dışta ve açıkta bulunan yeri de kapsar.","gloss":"görünür hale gelme","neighbor_only":"Önceden gizli ya da örtülü olanın sonradan açılması ve bir metnin yayımlanması yönünü kapsar.","neighbor_ref":"root_000105/B001","relation_type":"near_synonym","shared_zone":"İki dalın kesişimi, bir şeyin saklı olmayıp görünür duruma gelmesidir."},{"boundary_match":"partial","distinction":"Komşu dar bir açık karşılaşma kalıbına bağlıdır; odak dal ise kişi, yol, yer ve eylem üzerinde daha geniş fakat güneşle güçlü biçimde ilişkili bir açıklık alanıdır.","focus_only":"Güneş altında kalma, dış kenar, alenen eylem ve terleme gibi daha geniş gerçekleşmeleri vardır.","gloss":"örtüsüz ve açıkta olma","neighbor_only":"Özellikle hiçbir şeyin örtmediği açık bir karşılaşma durumuna bağlıdır.","neighbor_ref":"root_000086/B005","relation_type":"near_synonym","shared_zone":"Her ikisi de örtüsüz, dışta ve bakışa açık bulunmayı anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dal bir açıklık ve görünürlük durumudur; komşu dal zamandır. Bir kişinin o vakitte bulunması onun zorunlu olarak güneşe açık olduğu anlamına gelmez.","focus_only":"Güneşe veya bakışa maruz kalıp görünür olmayı anlatır.","gloss":"güneşe açıklık ile kuşluk vakti","neighbor_only":"Güneşin yükselişine göre belirlenen erken gündüz zamanını anlatır.","neighbor_ref":"root_000904/B001","relation_type":"same_field","shared_zone":"İki dal güneşli erken gündüz sahnesini paylaşır."}],"source_phrase_ar":"ضحى الرجل يضحى إذا تعرض للشمس (maqayis); اضح أي ابرز للشمس (maqayis;ayn); ضحا الطريق إذا بدا وظهر (maqayis;sihah); ضاحية كل بلدة ناحيتها البارزة (maqayis;ayn;sihah;mufradat); فعل ذلك ضاحية أي ظاهرا بينا (maqayis;ayn;sihah); ضحيت عرقت وضحيت للشمس إذا برزت لها (sihah)","source_summary":"Kaynaklar, güneşe çıkma ile görünür ve dışta olmayı aynı anlam alanında birleştirir. Yolun görünmesi, yerin açık kenarı, işin alenen yapılması ve güneş altında terleme bu ortak açıklık durumunun farklı bağlamlarıdır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه التعرض للشمس وحرها والتعرق والبروز والظهور والناحية البارزة والعلانية","what_is_not_ar":"لا يدخل فيه وقت الضحى من حيث هو وقت ولا الأضحية ولا الغداء"},"support_links":["sup_232a2e81d217f7f05b9b","sup_3ab9701ea9b2b3dae50f","sup_505eb59f90dcf7b91ffd","sup_5eb68340db0beb49c3f6","sup_6609efaa09c9be1016db","sup_9281d059a5c59ce7cf82","sup_b41af86a4082058c74b8","sup_b51f71c5749d3deb6888"]},{"boundary":"Dal yalnızca günün erken aydınlık vaktine bağlanan öğün ve otlatmayı kapsar; genel yemek, genel otlatma veya vaktin kendisi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B003","candidate_links":[{"candidate_id":"cand_2f1774b551cc0019f472","lane":"macro"},{"candidate_id":"cand_636f80ea79f1756dd885","lane":"macro"},{"candidate_id":"cand_715c89701200b5aaa9bd","lane":"macro"},{"candidate_id":"cand_0e3baa73ac0f9682ac80","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","surface_ar":"ضُّحَىٰ"}],"gloss":"erken gündüz öğünü ve o vakitte otlatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Günün erken aydınlık bölümünde yenen öğün ve bu öğünü yeme eylemi adlandırılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Develerin günün başında otlamaya koyulması, aynı vakte bağlı hayvan yetiştiriciliği kullanımıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Koyunları erken aydınlık vakitte otlatmak, belirli bir söz öbeğine bağlı diğer hayvan yetiştiriciliği kullanımıdır."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın öğün ile hayvan otlatma kullanımlarını ortak zaman sınırı altında birlikte gösterir.","boundary_detail":"Dal yalnızca günün erken aydınlık vaktine bağlanan öğün ve otlatmayı kapsar; genel yemek, genel otlatma veya vaktin kendisi değildir.","branch_image_ar":"طعام الضحاء ورعي أوله","concept_gloss":"erken gündüz öğünü ve o vakitte otlatma","contextual_glosses":[{"applicability":"İnsanların günün erken aydınlık bölümündeki öğünü yemesini anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deve ve koyunların otlatılması kullanımlarını dışarıda bırakır.","preserves":"Öğünü ve onun erken gündüz zamanını korur."},"facet_ids":["F001"],"text":"kuşluk öğünü yemek","usage_role":"contextual"},{"applicability":"Deve veya koyunların erken aydınlık vakitte otlaması ya da otlatılması bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanların yediği öğün ve yeme eylemi anlamını karşılamaz.","preserves":"Otlatma eylemini ve erken gündüz zaman sınırını korur."},"facet_ids":["F002","F003"],"text":"günün başında otlatmak","usage_role":"contextual"}],"definition":"Günün erken aydınlık bölümünde yenen öğünü ve o sırada yemek yemeyi; ayrıca deve ya da koyunların günün başında otlamaya koyulmasını anlatan zaman bağlı kullanımlar alanıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Günün erken aydınlık bölümünde yenen öğün ve bu öğünü yeme eylemi adlandırılır."},{"facet_id":"F002","role":"associated_use","statement":"Develerin günün başında otlamaya koyulması, aynı vakte bağlı hayvan yetiştiriciliği kullanımıdır."},{"facet_id":"F003","role":"associated_use","statement":"Koyunları erken aydınlık vakitte otlatmak, belirli bir söz öbeğine bağlı diğer hayvan yetiştiriciliği kullanımıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Günün ilk öğünü olma yönündeki çağdaş ve daha dar bir öğün düzenini çağrıştırır.","collision":"Çağdaş kahvaltı kavramıyla karışarak tarihsel zaman sınırını belirsizleştirir.","fit":"displacement","loses":"Kuşluk vaktine özgü zaman bağını ve hayvan otlatma kullanımlarını kaybeder.","preserves":"Günün erken bölümünde yenen bir öğün olma özelliğini korur."},"text":"kahvaltı"}],"identity_rationale":"Kaynak ifadesi iki zaman bağlı kullanımı açıkça bir araya getirir: günün erken aydınlık bölümünde yenen öğün ve evcil hayvanların o sırada otlamaya başlaması. Bunlar zamanın kendisi değildir; yeme ve otlatma eylemlerinin o vakitle sınırlandırılmış adlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kuşluk öğünü"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kuşluk öğününü yemek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"develer günün başında otlamaya koyuldu"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"koyunlarını kuşluk vaktinde otlatmak"}],"lexicalization_note":"Öğün adı ve yemek yeme biçimleri ile deve ya da koyun otlatma söz öbekleri ayrı tutulur; zaman bağlantısı bu kullanımlardan bağımsız bir yalın anlam sayılmaz.","neighbor_coverage_note":"Bütün komşu adayları gözden geçirildi; erken gündüzü akşamdan, genel otlatmadan ve zamanın kendisinden ayıran dört kart yayımlandı, yem ve sürü çevresindeki daha dolaylı ilişkiler elendi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Eylem türleri paraleldir, fakat zaman ekseninin karşıt uçlarına yerleşirler: odak erken aydınlık vakte, komşu akşam ve geceye bağlıdır.","focus_only":"Erken aydınlık vakitteki öğün ve otlatmayı anlatır.","gloss":"gündüz başı ile akşam yeme ve otlatması","neighbor_only":"Akşam ya da geceye bağlı yemek ve otlatmayı anlatır.","neighbor_ref":"root_001017/B005","relation_type":"polarity_pair","shared_zone":"İki dal da bir öğünü ve hayvanların otlatılmasını günün belirli bölümüne bağlar."},{"boundary_match":"partial","distinction":"Odak dal zamana bağlı özel bir otlatma kullanımıdır; komşu dal otlatmanın genel alanını, otlağı ve yeneni de kapsar.","focus_only":"Otlatmayı günün erken aydınlık bölümüyle sınırlar ve ayrıca insan öğününü kapsar.","gloss":"erken vakitte otlatma","neighbor_only":"Hayvanın otlamasını, yemi ve otlak yerini zaman sınırı olmadan genel olarak kapsar.","neighbor_ref":"root_000574/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın ortak alanı evcil hayvanların otlamasıdır."},{"boundary_match":"field_only","distinction":"Odak dal zamanın adını eylem ve öğüne aktarır; komşu dal ise zaman diliminin kendisidir. Her iki yön tek bir yalın anlam olarak birleştirilmemelidir.","focus_only":"O vakitte yapılan yeme ve otlatma eylemlerini adlandırır.","gloss":"kuşluk vakti ile kuşluk etkinliği","neighbor_only":"Eylemlerden bağımsız olarak vaktin kendisini ve aşamalarını adlandırır.","neighbor_ref":"root_000904/B001","relation_type":"same_field","shared_zone":"Yeme ve otlatma kullanımları komşu dalın belirlediği erken gündüz zamanında gerçekleşir."},{"boundary_match":"partial","distinction":"Odak için belirleyici olan günün vaktidir; komşu için belirleyici olan otlağın bolluğu ve hayvanın genişçe beslenmesidir.","focus_only":"Günün başındaki otlatma zamanını ve insan öğününü içerir.","gloss":"zamanlı otlatma ile bol otlak","neighbor_only":"Bolluk içinde dilediğince otlama, geniş otlak ve doygun beslenme koşulunu içerir.","neighbor_ref":"root_000538/B001","relation_type":"near_neighbor","shared_zone":"İki dal da sürülerin otlamasını konu edinir."}],"source_phrase_ar":"للطعام الذي يؤكل في ذلك الوقت ضحاء (maqayis); هم يتضحون أي يتغدون والغداء الضحاء (maqayis); نتضحى أي نتغدى (ayn); تضحت الإبل أخذت في الرعي من أول النهار (ayn); الضحاء أيضا الغداء وهم يتضحون أي يتغدون (sihah); ضحى فلان غنمه أي رعاها بالضحا (sihah); تضحى أكل ضحى والضحاء والغداء لطعامهما (mufradat)","source_summary":"Kaynaklar erken aydınlık vakitte yenen öğünü ve o öğünü yeme eylemini ortak biçimde verir; aynı zaman bağı, develerin otlamaya başlamasına ve koyunların o vakitte otlatılmasına da uygulanır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الغداء المسمى ضحاء ويتضحون بمعنى يتغدون ورعي الإبل أو الغنم في أول النهار","what_is_not_ar":"لا يدخل فيه الذبح ولا مطلق وقت الضحى بلا أكل أو رعي"},"support_links":["sup_00c44fa8fcb832001a3a","sup_2a30b6a52dd9e12a63f4","sup_2d49dc2784a0f03037eb","sup_a866c9b415f3ebb29fad"]},{"boundary":"Herhangi bir kesilmiş hayvanı değil, belirli bayram günündeki dinsel kesime ayrılan ve o gün kesilen hayvanı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B004","candidate_links":[{"candidate_id":"cand_eff28988437e9928f8b4","lane":"macro"},{"candidate_id":"cand_f9456626e31fd63aa56f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","surface_ar":"ضُّحَىٰ"}],"gloss":"bayram gününde dinsel amaçla kesilen hayvan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bayram gününde dinsel amaçla kesilmek üzere ayrılan veya kesilen hayvan adlandırılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı hayvan için birden çok tekil ve çoğul biçim aktarılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu amaçla ayrılmış bir koyunu belirli bayram gününde kesmek, ilgili söz öbeğinin eylem anlamıdır."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın nesne, belirli gün ve dinsel kesim koşullarını birlikte taşıyan en kısa doğal karşılığıdır.","boundary_detail":"Herhangi bir kesilmiş hayvanı değil, belirli bayram günündeki dinsel kesime ayrılan ve o gün kesilen hayvanı kapsar.","branch_image_ar":"ذبيحة يوم الأضحى","concept_gloss":"bayram gününde dinsel amaçla kesilen hayvan","contextual_glosses":[{"applicability":"Hayvanın ilgili bayram gününde kesilmek üzere ayrılmış olmasını öne çıkaran kullanımlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kesilmiş olabilme durumunu açıkça söylemez.","preserves":"Hayvanın belirli bayram gününde kesilmek üzere ayrılmasını korur."},"facet_ids":["F001"],"text":"bayram günü kesilmek üzere ayrılan hayvan","usage_role":"contextual"},{"applicability":"Koyunun ilgili günde kesilmesini bildiren söz öbeği için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanı adlandıran genel biçimleri ve koyun dışındaki olası hayvanları kapsamaz.","preserves":"Koyunu, kesme eylemini, özel amacı ve günü korur."},"facet_ids":["F003"],"text":"bayram günü adaklık koyun kesmek","usage_role":"contextual"}],"definition":"Belirli bayram gününde dinsel amaçla kesilmek üzere ayrılan veya kesilen koyun ya da başka hayvandır. Böyle bir koyunu o gün kesme eylemi, nesne merkezli bu anlamın söz öbeğine bağlı gerçekleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bayram gününde dinsel amaçla kesilmek üzere ayrılan veya kesilen hayvan adlandırılır."},{"facet_id":"F002","role":"source_variant","statement":"Aynı hayvan için birden çok tekil ve çoğul biçim aktarılır."},{"facet_id":"F003","role":"associated_use","statement":"Bu amaçla ayrılmış bir koyunu belirli bayram gününde kesmek, ilgili söz öbeğinin eylem anlamıdır."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Belirli bayram gününe bağlı olmayan daha genel sunu ve özveri anlamlarını da ekler.","collision":"Günlük dilde mecazi olarak zarar gören kişi anlamıyla da karışabilir.","fit":"broadening","loses":null,"preserves":"Dinsel amaçla sunulan veya kesilen şey yönünü korur."},"text":"kurban"}],"identity_rationale":"Kaynak ifadesi, belirli bayram gününde kesilen koyun ya da başka hayvanı, bu hayvan için kullanılan biçimleri ve koyun kesme eylemini açıkça verir. Dalın kimliği genel hayvan kesimi değil, gün ve dinsel uygulamayla sınırlandırılmış kesim nesnesidir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bayram gününde dinsel amaçla kesilen koyun veya başka hayvan"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bayram gününde dinsel amaçla kesilen hayvan"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"aynı hayvan için kullanılan başka bir ad"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"dinsel hayvan kesiminin yapıldığı bayram günü veya o gün kesilen hayvanlar"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bayram gününde dinsel amaçla bir koyun kesmek"}],"lexicalization_note":"Hayvanı adlandıran biçimler dalın merkezindedir; koyun kesme eylemi yalnızca verilen söz öbeğinde ve belirli bayram günü koşuluyla tanımlanır.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel dinsel kesim hayvanı, genel kesme işlemi, belirli hayvan türü ve kesim sonrası işlemle kurulan dört sınır yayımlandı, yalnızca aynı tören alanını paylaşan uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sınırı belirli bayram günü ve o güne özgü adlandırmadır; komşu dal daha genel dinsel sunu alanına uzanır.","focus_only":"Belirli bayram gününü ve o gün kesilen hayvana ait ad biçimlerini şart koşar.","gloss":"bayramlık kesim hayvanı","neighbor_only":"Yaklaşma amacıyla sunulan kesim hayvanını ve dökülen kanı gün şartı olmadan daha genel biçimde kapsar.","neighbor_ref":"root_001498/B002","relation_type":"near_synonym","shared_zone":"İki dal da dinsel yakınlaşma amacıyla kesilen hayvanı anlatabilir."},{"boundary_match":"partial","distinction":"Odak nesne ve törensel zaman merkezlidir; komşu ise kesme işleminin tamamlanması merkezlidir. Her genel kesim bu dalın kapsamına girmez.","focus_only":"Belirli gün ve dinsel amaçla tanımlanan hayvanı merkez alır.","gloss":"kesim hayvanı ile kesme işlemi","neighbor_only":"Hayvanın yaşamını sona erdiren kesim işlemini, gün ve dinsel amaç koşulu olmadan merkez alır.","neighbor_ref":"root_000517/B003","relation_type":"near_neighbor","shared_zone":"Odak daldaki hayvanın gerçekleştirilmiş kullanımında bir kesme işlemi bulunur."},{"boundary_match":"partial","distinction":"Odak dal işlev ve günle, komşu dal ise hayvan türü ve sunulma durumuyla sınırlıdır; kapsamları kesişse de özdeş değildir.","focus_only":"Bayram günündeki dinsel kesime ayrılan hayvanı türden bağımsız bir işlevle adlandırır.","gloss":"bayramlık hayvan ile iri sunu hayvanı","neighbor_only":"Özellikle deve veya sığır türünden sunulan iri hayvanı adlandırır.","neighbor_ref":"root_000096/B003","relation_type":"near_neighbor","shared_zone":"Bazı iri hayvanlar her iki dalın gönderimine birden girebilir."},{"boundary_match":"thematic_only","distinction":"Odak hayvan ile kesim anına, komşu ise sonradan etin işlenmesine ve izleyen günlere aittir; anlamsal çekirdekleri ortak değildir.","focus_only":"Belirli günde kesilen hayvanı ve kesme eylemini anlatır.","gloss":"kesim ve sonrasındaki et kurutma","neighbor_only":"Kesimden sonra etin güneşte kurutulmasını ve bunu izleyen günlerin adlandırılmasını anlatır.","neighbor_ref":"root_000790/B002","relation_type":"thematic","shared_zone":"İki dal aynı bayram çevrimindeki hayvan kesimi ve et hazırlama sahnesinde yer alır."}],"source_phrase_ar":"الضحية معروفة وهي الأضحية (maqayis); أربع لغات أضحية وإضحية وضحية وأضحاة (maqayis;sihah); الضحية الأضحية والجميع الضحايا والأضاحي وهي الشاة يضحي بها يوم الأضحى (ayn); ضحى بشاة من الأضحية وهي شاة تذبح يوم الأضحى (sihah); الأضحية جمعها أضاحي وقيل ضحية وضحايا وأضحاة وأضحى (mufradat)","source_summary":"Kaynakların ortak çekirdeği, belirli bayram gününde dinsel amaçla kesilen hayvandır. Çeşitli tekil ve çoğul adlandırmalar aynı gönderime bağlanır; koyun kesme eylemi de bu gün ve amaç koşuluyla verilir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الأضحية والضحية والضحايا والأضاحي والأضحاة وما يذبح يوم الأضحى","what_is_not_ar":"لا يدخل فيه مطلق الطعام ولا الرعي ولا البروز للشمس"},"support_links":["sup_65dadf9a50ab46d5d1ad","sup_700c0a735717486bd851"]},{"boundary":"Dal vaktin kendisini değil, o vaktin aydınlığına benzetilen parlaklık, bulutsuz açıklık ve açık at rengini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B005","candidate_links":[{"candidate_id":"cand_2271495035bc343d417f","lane":"macro"},{"candidate_id":"cand_54a85c000f3ccb10e233","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","surface_ar":"ضُّحَىٰ"}],"gloss":"kuşluk aydınlığını andıran parlak açıklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kuşluk aydınlığını andıran parlak ve açık görünüm temel niteliktir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güneş, verdiği güçlü aydınlık nedeniyle bu nitelikle adlandırılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bulutsuz ve aydınlık gece ile gün, açıklık ve ışık niteliğini birlikte taşır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Atlarda erkek ve dişi için kullanılan açık kır-boz renk adları, parlak açıklığın renk alanına aktarımıdır."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Güneş, açık gökyüzü ve at rengi uzantılarını birleştiren temel görsel niteliği karşılar.","boundary_detail":"Dal vaktin kendisini değil, o vaktin aydınlığına benzetilen parlaklık, bulutsuz açıklık ve açık at rengini anlatır.","branch_image_ar":"ضياء الضحى وصفاؤه","concept_gloss":"kuşluk aydınlığını andıran parlak açıklık","contextual_glosses":[{"applicability":"Gece veya günün gökyüzü açıklığıyla birlikte aydınlık olduğu bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneşin adı ve atların açık kır-boz rengi kullanımlarını karşılamaz.","preserves":"Aydınlık ile bulutsuz açıklığı birlikte korur."},"facet_ids":["F001","F003"],"text":"bulutsuz ve aydınlık","usage_role":"contextual"},{"applicability":"Atın açık, beyaza çalan kır-boz rengini anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneş, gün ve gece aydınlığı kullanımlarını dışarıda bırakır.","preserves":"Parlak açıklığın at rengine aktarılmış yönünü korur."},"facet_ids":["F004"],"text":"açık kır-boz renkli","usage_role":"contextual"}],"definition":"Kuşluk aydınlığını andıran parlaklık ve bulutsuz açıklıktır. Bu nitelik güneşin adlandırılmasına, aydınlık gece ve güne ilişkin söz öbeklerine, ayrıca atların açık kır-boz rengine aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kuşluk aydınlığını andıran parlak ve açık görünüm temel niteliktir."},{"facet_id":"F002","role":"extension","statement":"Güneş, verdiği güçlü aydınlık nedeniyle bu nitelikle adlandırılır."},{"facet_id":"F003","role":"specialization","statement":"Bulutsuz ve aydınlık gece ile gün, açıklık ve ışık niteliğini birlikte taşır."},{"facet_id":"F004","role":"extension","statement":"Atlarda erkek ve dişi için kullanılan açık kır-boz renk adları, parlak açıklığın renk alanına aktarımıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kaynağı ve niteliği sınırsız olan her türlü ışığı kapsama ekler.","collision":"At rengindeki açık kır-boz görünümü doğrudan karşılayamaz.","fit":"broadening","loses":null,"preserves":"Aydınlık ve parlaklık yönünü korur."},"text":"ışık"}],"identity_rationale":"Kaynak ifadesi güneşin bu adla anılmasını, bulutsuz ve aydınlık gece ile günü, ayrıca atlarda açık kır-boz rengi birlikte aktarır. Çerçevedeki kuşluk aydınlığı ve açıklık bunları birleştiren niteliktir; at rengi doğrudan ışık değil, bu açık parlak niteliğin renk alanına aktarımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"güneş"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bulutsuz ve aydınlık gece"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bulutsuz, berrak ve aydınlık gece"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bulutsuz ve aydınlık gün"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"açık kır-boz renkli at"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"açık kır-boz renkli kısrak"}],"lexicalization_note":"Aydınlık ve açıklık ortak niteliktir; güneş adı, bulutsuz gece ve gün söz öbekleri ile at rengi biçimleri kendi özel kapsamlarında tutulur.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi; açık gökyüzü, aydınlanma, genel ışık ve aynı kökün zaman dalı temel sınırları gösterdiği için seçildi, yalnızca belirli ışık kaynaklarını anlatan uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal niteliği geceye, güneş adına ve at rengine taşır; komşu dal gündüz beyazlığı ve karanlığın açılması çevresinde kalır.","focus_only":"Güneş adı, aydınlık gece ve atların açık kır-boz rengi uzantılarını kapsar.","gloss":"aydınlık ve açık gökyüzü","neighbor_only":"Gündüzün beyazlığı ile gökyüzü açıklığının karanlığı giderip günü yaymasını merkez alır.","neighbor_ref":"root_000256/B007","relation_type":"near_synonym","shared_zone":"İki dal da gün ışığının parlaklığı ile gökyüzünün açıklığını birleştirir."},{"boundary_match":"partial","distinction":"Odak kuşluk benzeri parlak açıklığa ve renk uzantısına dayanır; komşu karanlıktan aydınlığa çıkışı ve yüz parıltısını da kapsayan başka bir gelişim çizgisidir.","focus_only":"Bulutsuz geceyi ve atların açık kır-boz rengini içerir.","gloss":"aydınlanıp belirginleşme","neighbor_only":"Şafak aydınlığını, yüzün parlamasını ve karanlıktan sonra belirginleşen zamanı içerir.","neighbor_ref":"root_000712/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de aydınlık, beyazlık ve açık görünüm alanında buluşur."},{"boundary_match":"partial","distinction":"Odak belirli bir parlak-açık görünüm niteliğidir; komşu ise kaynağı ne olursa olsun ışığın yayılması ve bir şeyi aydınlatmasıdır.","focus_only":"Bulutsuz açıklığı ve atların açık kır-boz rengini kuşluk ışığı benzerliğiyle birleştirir.","gloss":"parlak açıklık ile yayılan ışık","neighbor_only":"Ateş, kandil, şimşek ve tan gibi çok çeşitli kaynaklardan yayılan ışığı ve aydınlatma eylemini kapsar.","neighbor_ref":"root_000919/B001","relation_type":"near_neighbor","shared_zone":"İki dalın ortak alanı ışık veren veya aydınlık görünen şeylerdir."},{"boundary_match":"field_only","distinction":"Bir dal görsel nitelik, diğeri zamansal bölümdür. Aydınlık başka zamanlara ve at rengine taşınabilirken zaman anlamı taşınmaz.","focus_only":"Kuşluk ışığına benzer parlaklık ve açıklık niteliğini anlatır.","gloss":"kuşluk aydınlığı ile kuşluk vakti","neighbor_only":"Kuşluk zamanını ve onun gündüz içindeki aşamalarını anlatır.","neighbor_ref":"root_000904/B001","relation_type":"same_field","shared_zone":"Odak niteliğin benzetme kaynağı, komşu dalın adlandırdığı zamanın ışığıdır."}],"source_phrase_ar":"تسمى الشمس الضحاء (ayn); ليلة إضحيانة وضحياء أي مضيئة لا غيم فيها (maqayis); ليلة ضحياء مضيئة لا غيم فيها وليلة إضحيانة (sihah); يوم إضحيان مضيء لا غيم فيه (ayn); الأضحى من الخيل الأشهب والأنثى ضحياء (sihah); ليلة إضحيانة وضحياء مضيئة إضاءة الضحى (mufradat)","source_summary":"Kaynakların toplu verisi kuşluk ışığına benzeyen parlak ve bulutsuz açıklığı gösterir. Güneş adı ile aydınlık gece ve gün bu niteliği doğrudan taşırken, atların açık kır-boz rengi görsel bir uzantı oluşturur.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الشمس المسماة الضحاء والليلة المضيئة الصافية والبياض الأشهب في الخيل","what_is_not_ar":"لا يدخل فيه مجرد وقت الضحى ولا البروز المكاني"},"support_links":["sup_6de832772998fb3b589c","sup_b51f71c5749d3deb6888"]},{"boundary":"Bu dal genel görünürlük veya gündüz anlamını taşımaz; yalnızca yumuşak davranma ve acele etmeme bildiren kayıtlı kullanımları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B006","candidate_links":[{"candidate_id":"cand_cee7d167f096d93a41ad","lane":"macro"},{"candidate_id":"cand_88e57ac020c8cec56f94","lane":"macro"},{"candidate_id":"cand_41d6d0fa51c3464365a2","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","surface_ar":"ضُّحَىٰ"}],"gloss":"yumuşak davranıp acele etmemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş karşısında yumuşak davranmak ve onu aceleye getirmemek temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işi yumuşaklıkla ve ağırdan alarak yürütme, belirli bir söz öbeğine bağlı kullanımdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Acele etmeme ve yavaşlama buyruğu, diğer kayıtlı yapının doğrudan işlevini oluşturur."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki kayıtlı yapının ortak çekirdeği olan davranış yumuşaklığını ve hızın düşürülmesini birlikte karşılar.","boundary_detail":"Bu dal genel görünürlük veya gündüz anlamını taşımaz; yalnızca yumuşak davranma ve acele etmeme bildiren kayıtlı kullanımları kapsar.","branch_image_ar":"الرفق والإمهال","concept_gloss":"yumuşak davranıp acele etmemek","contextual_glosses":[{"applicability":"Bir işin sertlik ve acele olmadan ele alınmasını anlatan bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğrudan bir yavaşlama buyruğu olma işlevini karşılamaz.","preserves":"İşin yumuşak ve acele edilmeden yürütülmesini korur."},"facet_ids":["F001","F002"],"text":"işi ağırdan ve yumuşaklıkla yürütmek","usage_role":"contextual"},{"applicability":"Karşıdakinden hızını düşürmesini isteyen doğrudan buyruk bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işi yumuşak davranarak yürütme anlamını tek başına taşımaz.","preserves":"Acele etmeme ve yavaşlama buyruğunu korur."},"facet_ids":["F003"],"text":"acele etme, yavaş ol","usage_role":"contextual"}],"definition":"Bir işi sertlik göstermeden, yumuşak davranarak ve acele etmeden yürütmektir. Bir kullanım eylem biçimini, diğeri ise doğrudan yavaşlama ve acele etmeme buyruğunu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş karşısında yumuşak davranmak ve onu aceleye getirmemek temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Bir işi yumuşaklıkla ve ağırdan alarak yürütme, belirli bir söz öbeğine bağlı kullanımdır."},{"facet_id":"F003","role":"specialization","statement":"Acele etmeme ve yavaşlama buyruğu, diğer kayıtlı yapının doğrudan işlevini oluşturur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Eylemi tümüyle durdurup zaman geçmesini bekleme anlamını ekler.","collision":null,"fit":"displacement","loses":"Yumuşak davranarak işi sürdürme ve doğrudan yavaşlama buyruğunu kaybeder.","preserves":"Hızı düşürme ve acele etmeme yönünü kısmen korur."},"text":"beklemek"}],"identity_rationale":"Kaynak ifadesi bir iş karşısında yumuşak davranmayı ve acele etmeme buyruğunu doğrudan verir. Çerçevedeki yumuşaklık ve ağırdan alma bu iki kullanımı doğru bir ortak alanda tutar; ancak anlam yalın köke değil, verilen söz öbeklerine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bir işi yumuşak davranarak ve ağırdan alarak yürütmek"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"acele etme, yavaş ol"}],"lexicalization_note":"Yumuşak davranma ve acele etmeme iki kayıtlı yapı içinde tanımlanır; bunlardan sınırsız bir yalın kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün komşu kartları değerlendirildi; bekleme, genel yumuşaklık, geniş acele etmeme alanı ve başka bir yapıdaki yumuşak davranma en yararlı sınırları verdi, daha uzak ağırbaşlılık ve özdenetim adayları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda bekleme zorunlu değildir; iş yumuşakça sürdürülebilir. Komşu dal ise bekleme ve oyalanma yönünü açıkça içerir.","focus_only":"Yumuşak davranma ile acele etmeme buyruğunu iki kayıtlı yapı içinde birleştirir.","gloss":"yavaş davranıp beklemek","neighbor_only":"Bekleme eylemini doğrudan anlam alanına alır.","neighbor_ref":"root_000583/B008","relation_type":"near_synonym","shared_zone":"İki dal da hızın düşürülmesini ve bir işte zaman tanınmasını anlatır."},{"boundary_match":"partial","distinction":"Odak zamanlama ve acele etmeme yönünü de taşır ve belirli yapılara bağlıdır; komşu ise genel davranış yumuşaklığında daha geniştir.","focus_only":"Acele etmeme ve yavaşlama buyruğunu özellikle içerir.","gloss":"yumuşak ve ölçülü davranma","neighbor_only":"Sertliğin karşıtı olan genel davranış yumuşaklığını, kişilik niteliğini ve özenli uygulamayı daha geniş biçimde kapsar.","neighbor_ref":"root_000583/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da sertlikten kaçınarak yumuşak davranmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dalın yumuşak davranma bileşeni ve yapı bağı önemlidir; komşu dal ise hız, bekleme ve kendini tutma yönlerinde daha geniştir.","focus_only":"Bir iş karşısındaki yumuşak davranışı kayıtlı söz öbekleriyle sınırlar.","gloss":"ağırdan alma ve acele etmeme","neighbor_only":"Gecikme, bekleme, ağırbaşlılık ve öfkeyi dizginleme gibi daha geniş acele etmeme alanını kapsar.","neighbor_ref":"root_000063/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir işi aceleye getirmemeyi içerir."},{"boundary_match":"partial","distinction":"Odak dal yumuşaklığın yanında hızın düşürülmesini açıkça içerir; komşu kart yalnızca yönelinen şeye yumuşak davranmayı bildirir.","focus_only":"Acele etmeme buyruğunu ve işi ağırdan almayı da kapsar.","gloss":"bir şeye yumuşak davranma","neighbor_only":"Yumuşak davranmayı tek bir başka söz öbeği içinde, yönelinen kişi veya şeyle ilişkilendirir.","neighbor_ref":"root_001017/B008","relation_type":"near_synonym","shared_zone":"İki dal belirli bir yapı içinde bir işe veya şeye yumuşak davranmayı anlatır."}],"source_phrase_ar":"ضحيت عن الأمر إذا رفقت (maqayis;sihah); ضح رويدا أي لا تعجل (sihah)","source_summary":"Kaynakların ortak verisi, bir işte yumuşak davranma ile acele etmeyip ağırdan alma yönlerini birleştirir. Biri işin yürütülüşünü, diğeri doğrudan yavaşlama buyruğunu anlatan iki sınırlı kullanım vardır.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه ضحيت عن الأمر بمعنى رفقت وضح رويدا بمعنى لا تعجل","what_is_not_ar":"لا يدخل فيه أصل البروز ولا الضحى ولا الأضحية"},"support_links":["sup_289cdad6e176c1e5f988","sup_a1de4e211be14988a059","sup_d1851db359b0882caaa9"]},{"boundary":"A stray domestic animal, especially a camel, left in a place of loss with no known owner.","branch_kind":null,"branch_ref":"root_000913/B005","candidate_links":[{"candidate_id":"cand_2f1774b551cc0019f472","lane":"macro"}],"focus_root_occurrences":[],"gloss":"stray animal in a wasteland","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الضالّة في المضيعة","image_en":"stray animal in a wasteland"}}],"root_ar":"ض ل ل","root_id":"root_000913","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الضالّة في المضيعة","image_en":"stray animal in a wasteland","scope_ar":"البهيمة ولا سيما الإبل إذا بقيت في مضيعة لا يعرف ربها والذكر والأنثى فيها سواء","scope_en":"A stray domestic animal, especially a camel, left in a place of loss with no known owner."},"support_links":["sup_2a30b6a52dd9e12a63f4"]},{"boundary":"Includes giving, handing over, reciprocal handing, the gift, and names for what is given.","branch_kind":null,"branch_ref":"root_001028/B002","candidate_links":[{"candidate_id":"cand_eff28988437e9928f8b4","lane":"macro"},{"candidate_id":"cand_715c89701200b5aaa9bd","lane":"macro"},{"candidate_id":"cand_f9456626e31fd63aa56f","lane":"macro"}],"focus_root_occurrences":[],"gloss":"handing over and giving","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"المناولة والإعطاء","image_en":"handing over and giving"}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"المناولة والإعطاء","image_en":"handing over and giving","scope_ar":"يدخل فيه الإعطاء والمناولة والمعاطاة والعطاء والعطية والشيء المعطى وجمعه","scope_en":"Includes giving, handing over, reciprocal handing, the gift, and names for what is given."},"support_links":["sup_65dadf9a50ab46d5d1ad","sup_700c0a735717486bd851","sup_a866c9b415f3ebb29fad"]},{"boundary":"A stray animal not knowing which direction to seek.","branch_kind":null,"branch_ref":"root_001068/B008","candidate_links":[{"candidate_id":"cand_2f1774b551cc0019f472","lane":"macro"}],"focus_root_occurrences":[],"gloss":"stray animal losing its direction","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"حيرة الضالة عن وجهتها","image_en":"stray animal losing its direction"}}],"root_ar":"ع ي ل","root_id":"root_001068","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"حيرة الضالة عن وجهتها","image_en":"stray animal losing its direction","scope_ar":"الضالة التي لا تدري أي وجهة تبغيها","scope_en":"A stray animal not knowing which direction to seek."},"support_links":["sup_2a30b6a52dd9e12a63f4"]},{"boundary":"Includes roasting or frying grain, meat, dates, or other food on a pan, the pan/place/seller, and qaliyya food","branch_kind":null,"branch_ref":"root_001253/B004","candidate_links":[{"candidate_id":"cand_636f80ea79f1756dd885","lane":"macro"},{"candidate_id":"cand_0ea93d667e05b71df20e","lane":"macro"}],"focus_root_occurrences":[],"gloss":"roasting or frying on a pan","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"إلقاء الطعام على المقلى حتى ينضج","image_en":"roasting or frying on a pan"}}],"root_ar":"ق ل ي","root_id":"root_001253","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"إلقاء الطعام على المقلى حتى ينضج","image_en":"roasting or frying on a pan","scope_ar":"يدخل فيه قلي الشيء والسويق واللحم والحب والبسر على المقلى، والمقلاة والمقلى، والقلاء الذي يقلي البر، وموضع القلاءة، والقلية من الطعام","scope_en":"Includes roasting or frying grain, meat, dates, or other food on a pan, the pan/place/seller, and qaliyya food"},"support_links":["sup_2d49dc2784a0f03037eb","sup_9281d059a5c59ce7cf82"]},{"boundary":"This branch covers qahara of meat: cooking or fire acting on it until its moisture runs and it changes.","branch_kind":null,"branch_ref":"root_001266/B002","candidate_links":[{"candidate_id":"cand_636f80ea79f1756dd885","lane":"macro"},{"candidate_id":"cand_0ea93d667e05b71df20e","lane":"macro"}],"focus_root_occurrences":[],"gloss":"meat seized by fire until its juices run","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"لحم تأخذه النار فيسيل ماؤه ويتغير","image_en":"meat seized by fire until its juices run"}}],"root_ar":"ق ه ر","root_id":"root_001266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"لحم تأخذه النار فيسيل ماؤه ويتغير","image_en":"meat seized by fire until its juices run","scope_ar":"يدخل فيه قهر اللحم إذا طبخ أو أخذته النار حتى يسيل ماؤه ويتغير.","scope_en":"This branch covers qahara of meat: cooking or fire acting on it until its moisture runs and it changes."},"support_links":["sup_2d49dc2784a0f03037eb","sup_9281d059a5c59ce7cf82"]},{"boundary":"This branch covers the single attested food preparation called al-qahira.","branch_kind":null,"branch_ref":"root_001266/B003","candidate_links":[{"candidate_id":"cand_636f80ea79f1756dd885","lane":"macro"}],"focus_root_occurrences":[],"gloss":"a milk food heated with hot stones and flour","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"قهيرة من محض تسخنه الرضف ويذر عليه الدقيق","image_en":"a milk food heated with hot stones and flour"}}],"root_ar":"ق ه ر","root_id":"root_001266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"قهيرة من محض تسخنه الرضف ويذر عليه الدقيق","image_en":"a milk food heated with hot stones and flour","scope_ar":"يدخل فيه القهيرة: محض تلقى فيه الرضف فإذا غلى ذر عليه الدقيق وسيط به ثم أكل.","scope_en":"This branch covers the single attested food preparation called al-qahira."},"support_links":["sup_2d49dc2784a0f03037eb"]},{"boundary":"The night period, its single night and plurals, as opposite of day, including its darkness and intensified or long forms.","branch_kind":null,"branch_ref":"root_001392/B001","candidate_links":[{"candidate_id":"cand_2271495035bc343d417f","lane":"macro"},{"candidate_id":"cand_63364e129fe9629ecfa7","lane":"macro"}],"focus_root_occurrences":[],"gloss":"night as the opposite of day and its darkness","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الليل خلاف النهار وظلمته","image_en":"night as the opposite of day and its darkness"}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الليل خلاف النهار وظلمته","image_en":"night as the opposite of day and its darkness","scope_ar":"يدخل فيه الليل والليلة والليالي، وضده النهار، وظلام الليل وشدته وطوله في نحو ليلة ليلاء وليل أليل وليل لائل وليلة ليلى","scope_en":"The night period, its single night and plurals, as opposite of day, including its darkness and intensified or long forms."},"support_links":["sup_505eb59f90dcf7b91ffd","sup_6de832772998fb3b589c"]},{"boundary":"This branch covers نعم and أنعام as grazing livestock, especially camels and by extension camels, cattle, and sheep.","branch_kind":null,"branch_ref":"root_001525/B005","candidate_links":[{"candidate_id":"cand_2f1774b551cc0019f472","lane":"macro"},{"candidate_id":"cand_eff28988437e9928f8b4","lane":"macro"}],"focus_root_occurrences":[],"gloss":"grazing livestock, especially camels","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"مال الأنعام والإبل","image_en":"grazing livestock, especially camels"}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"مال الأنعام والإبل","image_en":"grazing livestock, especially camels","scope_ar":"يدخل فيه النعم والأنعام، خصوصا الإبل، وبالتوسيع الإبل والبقر والغنم والبهائم الراعية حيث نصت المصادر على ذلك.","scope_en":"This branch covers نعم and أنعام as grazing livestock, especially camels and by extension camels, cattle, and sheep."},"support_links":["sup_2a30b6a52dd9e12a63f4","sup_65dadf9a50ab46d5d1ad"]},{"boundary":"A flooded watercourse, river and rivers, the channel cutting through ground, abundant flowing water, a stream taking its course, and reaching water while digging.","branch_kind":null,"branch_ref":"root_001559/B001","candidate_links":[{"candidate_id":"cand_f74d9c49655ec0033d3e","lane":"macro"}],"focus_root_occurrences":[],"gloss":"river cutting the ground with flowing water","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"نهر يشق الأرض بماء جار","image_en":"river cutting the ground with flowing water"}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"نهر يشق الأرض بماء جار","image_en":"river cutting the ground with flowing water","scope_ar":"مجرى الماء الفائض؛ النهر والأنهار وجمع نهر؛ شق الأرض بالمجرى؛ جريان الماء الكثير؛ أخذ المجرى موضعا؛ بلوغ الماء في الحفر","scope_en":"A flooded watercourse, river and rivers, the channel cutting through ground, abundant flowing water, a stream taking its course, and reaching water while digging."},"support_links":["sup_645641411e9d6ab59351"]},{"boundary":"The day or daylight period from dawn to sunset, opposite night, sometimes a day, pluralized as نهر, and a man of daytime activity.","branch_kind":null,"branch_ref":"root_001559/B002","candidate_links":[{"candidate_id":"cand_2271495035bc343d417f","lane":"macro"},{"candidate_id":"cand_e1333bfc096aa9d84ce7","lane":"macro"}],"focus_root_occurrences":[],"gloss":"day opening with light","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"انفتاح النهار بالضياء","image_en":"day opening with light"}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"انفتاح النهار بالضياء","image_en":"day opening with light","scope_ar":"النهار وضوء ما بين طلوع الفجر وغروب الشمس؛ ضد الليل؛ اليوم في بعض الاستعمال؛ جمع النهار على نهر؛ رجل نهر صاحب نهار","scope_en":"The day or daylight period from dawn to sunset, opposite night, sometimes a day, pluralized as نهر, and a man of daytime activity."},"support_links":["sup_5eb68340db0beb49c3f6","sup_6de832772998fb3b589c"]},{"boundary":"Opening or widening something, making blood flow, widening a wound or split, an open space between courtyards, belly discharge like a river, and نهر as spaciousness or brightness with spaciousness.","branch_kind":null,"branch_ref":"root_001559/B003","candidate_links":[{"candidate_id":"cand_f74d9c49655ec0033d3e","lane":"macro"},{"candidate_id":"cand_e1333bfc096aa9d84ce7","lane":"macro"}],"focus_root_occurrences":[],"gloss":"opening or widening until something flows or opens out","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"فتح الشيء وتوسيعه حتى يسيل أو ينفسح","image_en":"opening or widening until something flows or opens out"}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"فتح الشيء وتوسيعه حتى يسيل أو ينفسح","image_en":"opening or widening until something flows or opens out","scope_ar":"فتح الشيء وتوسيعه؛ إسالة الدم؛ اتساع الطعنة والفتق؛ الفضاء بين الأفنية؛ مجيء البطن كمجيء النهر؛ تفسير النهر بالسعة أو الضياء والسعة","scope_en":"Opening or widening something, making blood flow, widening a wound or split, an open space between courtyards, belly discharge like a river, and نهر as spaciousness or brightness with spaciousness."},"support_links":["sup_5eb68340db0beb49c3f6","sup_645641411e9d6ab59351"]},{"boundary":"It includes hady as what is sent to Mecca, the sanctuary, or the House, especially livestock but also wealth or goods offered in devotion, with extensions to sacrificial camels or camels generally","branch_kind":null,"branch_ref":"root_001583/B005","candidate_links":[{"candidate_id":"cand_eff28988437e9928f8b4","lane":"macro"},{"candidate_id":"cand_f9456626e31fd63aa56f","lane":"macro"}],"focus_root_occurrences":[],"gloss":"the offering sent to the sanctuary","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الهدي المهدى إلى الحرم","image_en":"the offering sent to the sanctuary"}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الهدي المهدى إلى الحرم","image_en":"the offering sent to the sanctuary","scope_ar":"يدخل فيه الهدي أو الهدي المشدد والمخفف بمعنى ما يهدى إلى مكة أو الحرم أو بيت الله من النعم أو المال أو المتاع قربة وما توسع منه إلى البدنة والإبل","scope_en":"It includes hady as what is sent to Mecca, the sanctuary, or the House, especially livestock but also wealth or goods offered in devotion, with extensions to sacrificial camels or camels generally"},"support_links":["sup_65dadf9a50ab46d5d1ad","sup_700c0a735717486bd851"]},{"boundary":"Includes the expression توديع الفحل meaning keeping a male animal for breeding.","branch_kind":null,"branch_ref":"root_001635/B008","candidate_links":[{"candidate_id":"cand_2f1774b551cc0019f472","lane":"macro"}],"focus_root_occurrences":[],"gloss":"keeping a stud male for breeding","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"اقتناء الفحل للفحلة","image_en":"keeping a stud male for breeding"}}],"root_ar":"و د ع","root_id":"root_001635","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"اقتناء الفحل للفحلة","image_en":"keeping a stud male for breeding","scope_ar":"يدخل فيه توديع الفحل بمعنى اقتنائه للفحلة.","scope_en":"Includes the expression توديع الفحل meaning keeping a male animal for breeding."},"support_links":["sup_2a30b6a52dd9e12a63f4"]},{"boundary":"Includes a human child whose father has died before maturity, an animal whose mother has died, and making children orphans","branch_kind":null,"branch_ref":"root_001692/B001","candidate_links":[{"candidate_id":"cand_2f1774b551cc0019f472","lane":"macro"},{"candidate_id":"cand_c78647c4b0d26dfb83dc","lane":"macro"},{"candidate_id":"cand_96ba0348ec5d77399a50","lane":"macro"}],"focus_root_occurrences":[],"gloss":"orphaned offspring cut off from its protecting parent","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"انقطاع الولد عن كافله","image_en":"orphaned offspring cut off from its protecting parent"}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"انقطاع الولد عن كافله","image_en":"orphaned offspring cut off from its protecting parent","scope_ar":"يدخل فيه الصبي الذي مات أبوه قبل بلوغه، والبهيمة التي ماتت أمها، وجعل الأولاد أيتاما","scope_en":"Includes a human child whose father has died before maturity, an animal whose mother has died, and making children orphans"},"support_links":["sup_2a30b6a52dd9e12a63f4","sup_3ab9701ea9b2b3dae50f","sup_6609efaa09c9be1016db"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000019/B002","candidate_links":[{"candidate_id":"cand_88e57ac020c8cec56f94","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_86608eb9b38981b4df61","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Deferral to a later time supplies the temporal displacement beyond the present phase.","root":"ء خ ر","source_ref":"93:4","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000019","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_289cdad6e176c1e5f988"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000067/B001","candidate_links":[{"candidate_id":"cand_88e57ac020c8cec56f94","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_86608eb9b38981b4df61","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Beginning and precedence establish the initial phase from which the comparison departs.","root":"ء و ل","source_ref":"93:4","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000067","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_289cdad6e176c1e5f988"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000067/B002","candidate_links":[{"candidate_id":"cand_88e57ac020c8cec56f94","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_86608eb9b38981b4df61","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Return to an outcome or consequence gives the temporal extension a telos.","root":"ء و ل","source_ref":"93:4","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000067","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_289cdad6e176c1e5f988"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000070/B001","candidate_links":[{"candidate_id":"cand_c78647c4b0d26dfb83dc","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3f38da5051ae6b48af6f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Joining a gathering refuge supplies the spatial reversal from exposed isolation to shelter.","root":"ء و ي","source_ref":"93:6","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000070","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3ab9701ea9b2b3dae50f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000070/B002","candidate_links":[{"candidate_id":"cand_c78647c4b0d26dfb83dc","lane":"macro"},{"candidate_id":"cand_41d6d0fa51c3464365a2","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3f38da5051ae6b48af6f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Tender mercy supplies the affective quality that makes shelter more than containment.","root":"ء و ي","source_ref":"93:6","source_word_indices":["4"]},{"hft_ref":"hft_f377ac95a8a24832bfa4","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Tender compassion supplies the relational quality that prevents slowing from becoming neglect.","root":"ء و ي","source_ref":"93:6","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000070","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3ab9701ea9b2b3dae50f","sup_d1851db359b0882caaa9"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000299/B003","candidate_links":[{"candidate_id":"cand_6d937e7faf936862aea0","lane":"macro"},{"candidate_id":"cand_d89fb0da4706ffd68a79","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_5d2a95d3b9038ccd761e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Speech continually renewed as news turns received benefit into an ongoing verbal event.","root":"ح د ث","source_ref":"93:11","source_word_indices":["4"]},{"hft_ref":"hft_b082876e6ff897cfbe1e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Renewed speech and news give the audible manifestation recurrence rather than a single utterance.","root":"ح د ث","source_ref":"93:11","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000299","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_232a2e81d217f7f05b9b","sup_b41af86a4082058c74b8"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000299/B006","candidate_links":[{"candidate_id":"cand_6d937e7faf936862aea0","lane":"macro"},{"candidate_id":"cand_d89fb0da4706ffd68a79","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_5d2a95d3b9038ccd761e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Bringing something out and making it appear mirrors the focus's visible disclosure in speech.","root":"ح د ث","source_ref":"93:11","source_word_indices":["4"]},{"hft_ref":"hft_b082876e6ff897cfbe1e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Making something appear links verbal disclosure back to the focus's visual disclosure.","root":"ح د ث","source_ref":"93:11","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000299","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_232a2e81d217f7f05b9b","sup_b41af86a4082058c74b8"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000452/B001","candidate_links":[{"candidate_id":"cand_88e57ac020c8cec56f94","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_86608eb9b38981b4df61","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Beneficial good assigns positive direction rather than mere lateness to the movement.","root":"خ ي ر","source_ref":"93:4","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000452","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_289cdad6e176c1e5f988"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000532/B002","candidate_links":[{"candidate_id":"cand_cee7d167f096d93a41ad","lane":"macro"},{"candidate_id":"cand_715c89701200b5aaa9bd","lane":"macro"},{"candidate_id":"cand_6d937e7faf936862aea0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_068b2b330cb63bd2bfeb","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Nurturing, repair, and completion make the continuing relation developmental rather than merely possessive.","root":"ر ب ب","source_ref":"93:3","source_word_indices":["3"]},{"hft_ref":"hft_b431632dcac05eb679bb","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Nurturing and bringing to completion turn transfer into sustained development.","root":"ر ب ب","source_ref":"93:5","source_word_indices":["3"]},{"hft_ref":"hft_5d2a95d3b9038ccd761e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Nurturing and completion identify care, rather than self-display, as the source of the visible good.","root":"ر ب ب","source_ref":"93:11","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000532","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_232a2e81d217f7f05b9b","sup_a1de4e211be14988a059","sup_a866c9b415f3ebb29fad"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000532/B007","candidate_links":[{"candidate_id":"cand_cee7d167f096d93a41ad","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_068b2b330cb63bd2bfeb","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Remaining, dwelling, and duration supply continuity beneath the apparent interval.","root":"ر ب ب","source_ref":"93:3","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000532","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a1de4e211be14988a059"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000537/B005","candidate_links":[{"candidate_id":"cand_715c89701200b5aaa9bd","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b431632dcac05eb679bb","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant split image of feeding and growth intensifies the maturation mechanism.","root":"ر ب ب","source_ref":"93:5","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000537","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a866c9b415f3ebb29fad"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000569/B002","candidate_links":[{"candidate_id":"cand_715c89701200b5aaa9bd","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b431632dcac05eb679bb","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Abundant or sought satisfaction supplies the experienced completion toward which the gift develops.","root":"ر ض و","source_ref":"93:5","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000569","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a866c9b415f3ebb29fad"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000661/B001","candidate_links":[{"candidate_id":"cand_e1333bfc096aa9d84ce7","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_facac0c2dcc9bd2925df","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Asking and requesting supply the explicit movement of need toward a listener.","root":"س ء ل","source_ref":"93:10","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000661","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5eb68340db0beb49c3f6"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000679/B002","candidate_links":[{"candidate_id":"cand_63364e129fe9629ecfa7","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ab57a0ff14e88e549dda","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Covering with a cloth sharpens the image of light being veiled without being destroyed.","root":"س ج و","source_ref":"93:2","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000679","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_505eb59f90dcf7b91ffd"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000736/B001","candidate_links":[{"candidate_id":"cand_e1333bfc096aa9d84ce7","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_facac0c2dcc9bd2925df","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant split image of gentle, hidden drawing suggests that some requests emerge indirectly and must be noticed without force.","root":"س ء ل","source_ref":"93:10","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000736","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5eb68340db0beb49c3f6"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000913/B002","candidate_links":[{"candidate_id":"cand_54a85c000f3ccb10e233","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_464e8dd4462a8f4941ed","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Hiddenness and disappearance supply an optical-spatial account of being unlocated.","root":"ض ل ل","source_ref":"93:7","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000913","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b51f71c5749d3deb6888"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000913/B003","candidate_links":[{"candidate_id":"cand_54a85c000f3ccb10e233","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_464e8dd4462a8f4941ed","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Loss supplies the condition that finding and direction reverse.","root":"ض ل ل","source_ref":"93:7","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000913","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b51f71c5749d3deb6888"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001068/B001","candidate_links":[{"candidate_id":"cand_0e3baa73ac0f9682ac80","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2f4d871fbc11117ab1fa","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Poverty and need supply the deficit from which the provisioning sequence begins.","root":"ع ي ل","source_ref":"93:8","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001068","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_00c44fa8fcb832001a3a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001068/B004","candidate_links":[{"candidate_id":"cand_0e3baa73ac0f9682ac80","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2f4d871fbc11117ab1fa","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Poor nourishment makes the deficit bodily and connects it directly to the focus's feeding branch.","root":"ع ي ل","source_ref":"93:8","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001068","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_00c44fa8fcb832001a3a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001110/B002","candidate_links":[{"candidate_id":"cand_0e3baa73ac0f9682ac80","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2f4d871fbc11117ab1fa","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Sufficiency and adequacy define the endpoint as enoughness rather than excess.","root":"غ ن ي","source_ref":"93:8","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001110","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_00c44fa8fcb832001a3a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001110/B003","candidate_links":[{"candidate_id":"cand_d89fb0da4706ffd68a79","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b082876e6ff897cfbe1e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Song and voice convert sufficiency from a silent state into an audible expression.","root":"غ ن ي","source_ref":"93:8","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001110","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b41af86a4082058c74b8"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001253/B003","candidate_links":[{"candidate_id":"cand_cee7d167f096d93a41ad","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_068b2b330cb63bd2bfeb","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Aversion that distances the heart supplies the rejected affective explanation for obscurity.","root":"ق ل ي","source_ref":"93:3","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001253","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a1de4e211be14988a059"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001266/B001","candidate_links":[{"candidate_id":"cand_96ba0348ec5d77399a50","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fba36a745b281ef92354","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Dominance descending from above and humiliating its object supplies the abusive use of superior standing.","root":"ق ه ر","source_ref":"93:9","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001266","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6609efaa09c9be1016db"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001525/B001","candidate_links":[{"candidate_id":"cand_6d937e7faf936862aea0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_5d2a95d3b9038ccd761e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A good, benefited condition supplies the content that has become manifest and can be recounted.","root":"ن ع م","source_ref":"93:11","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001525","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_232a2e81d217f7f05b9b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001525/B003","candidate_links":[{"candidate_id":"cand_6d937e7faf936862aea0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_5d2a95d3b9038ccd761e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Praising something with نعم gives narration an affirmative evaluative register.","root":"ن ع م","source_ref":"93:11","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001525","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_232a2e81d217f7f05b9b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001559/B004","candidate_links":[{"candidate_id":"cand_e1333bfc096aa9d84ce7","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_facac0c2dcc9bd2925df","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Harsh verbal rebuke supplies the closing force that the prohibition removes from the channel.","root":"ن ه ر","source_ref":"93:10","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001559","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5eb68340db0beb49c3f6"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001580/B006","candidate_links":[{"candidate_id":"cand_41d6d0fa51c3464365a2","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_f377ac95a8a24832bfa4","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant split image of rocking a child to sleep supplies a rhythmic, soothing mode of guidance.","root":"ه د ي","source_ref":"93:7","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001580","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d1851db359b0882caaa9"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001583/B001","candidate_links":[{"candidate_id":"cand_54a85c000f3ccb10e233","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_464e8dd4462a8f4941ed","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Gentle indication toward a path supplies non-coercive direction after discovery.","root":"ه د ي","source_ref":"93:7","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001583","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b51f71c5749d3deb6888"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001583/B003","candidate_links":[{"candidate_id":"cand_54a85c000f3ccb10e233","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_464e8dd4462a8f4941ed","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A guide moving at the front gives the visible field a leading edge and destination.","root":"ه د ي","source_ref":"93:7","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001583","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b51f71c5749d3deb6888"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001626/B001","candidate_links":[{"candidate_id":"cand_c78647c4b0d26dfb83dc","lane":"macro"},{"candidate_id":"cand_54a85c000f3ccb10e233","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3f38da5051ae6b48af6f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Encountering and locating something turns visibility into an act of finding.","root":"و ج د","source_ref":"93:6","source_word_indices":["2"]},{"hft_ref":"hft_464e8dd4462a8f4941ed","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Finding what was not securely located initiates the recovery mechanism.","root":"و ج د","source_ref":"93:7","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001626","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3ab9701ea9b2b3dae50f","sup_b51f71c5749d3deb6888"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001626/B003","candidate_links":[{"candidate_id":"cand_0e3baa73ac0f9682ac80","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2f4d871fbc11117ab1fa","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Capacity, means, and wealth supply the resource state discovered or produced in the reversal.","root":"و ج د","source_ref":"93:8","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001626","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_00c44fa8fcb832001a3a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001635/B001","candidate_links":[{"candidate_id":"cand_cee7d167f096d93a41ad","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_068b2b330cb63bd2bfeb","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Leaving and relinquishing supply the rupture that the verse explicitly negates.","root":"و د ع","source_ref":"93:3","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001635","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a1de4e211be14988a059"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001635/B002","candidate_links":[{"candidate_id":"cand_cee7d167f096d93a41ad","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_068b2b330cb63bd2bfeb","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Ease and stillness preserve a non-hostile sense of pause once abandonment is denied.","root":"و د ع","source_ref":"93:3","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001635","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a1de4e211be14988a059"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001684/B002","candidate_links":[{"candidate_id":"cand_88e57ac020c8cec56f94","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_86608eb9b38981b4df61","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant split image of one thing following another supplies continuity between phases without a vacant gap.","root":"ء و ل","source_ref":"93:4","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001684","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_289cdad6e176c1e5f988"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001692/B002","candidate_links":[{"candidate_id":"cand_c78647c4b0d26dfb83dc","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3f38da5051ae6b48af6f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Singularity and separation widen orphanhood into a structural image of isolation.","root":"ي ت م","source_ref":"93:6","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001692","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3ab9701ea9b2b3dae50f"]}],"candidate_inventory":[{"anchor_refs":["93:1","93:10","93:2"],"branch_refs":["root_000679/B001","root_000904/B001","root_000904/B005","root_001392/B001","root_001559/B002"],"candidate_id":"cand_2271495035bc343d417f","commentary_obligation":"review","focus_branch_refs":["root_000904/B001","root_000904/B005"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000679/B001","root_001392/B001","root_001559/B002"],"root_ids":[],"scope":"pericope","source_local_id":"A:Daylight, Night, and Stilling","source_type":"channel","support_ids":["sup_0a4d742a14d6d2461050","sup_284ab30aa31ce7d1948b","sup_2d978237f198c0c9b4c5","sup_5a5ddba1ab7267c5b86b","sup_6de832772998fb3b589c"],"title":"Daylight, Night, and Stilling","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["93:1","93:11","93:3","93:5","93:6","93:7","93:8","93:9"],"branch_refs":["root_000532/B014","root_000904/B003","root_000913/B005","root_001068/B008","root_001525/B005","root_001635/B008","root_001692/B001"],"candidate_id":"cand_2f1774b551cc0019f472","commentary_obligation":"review","focus_branch_refs":["root_000904/B003"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000532/B014","root_000913/B005","root_001068/B008","root_001525/B005","root_001635/B008","root_001692/B001"],"root_ids":[],"scope":"pericope","source_local_id":"A:Herd, Grazing, and the Stray","source_type":"channel","support_ids":["sup_2a30b6a52dd9e12a63f4","sup_329dc30c1dd53ce07636","sup_37697cd9e95e933be08b","sup_b174b5fb40a75adb4292","sup_e88f761376ec049a96c8"],"title":"Herd, Grazing, and the Stray","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["93:1","93:3","93:9"],"branch_refs":["root_000904/B003","root_001253/B004","root_001266/B002","root_001266/B003"],"candidate_id":"cand_636f80ea79f1756dd885","commentary_obligation":"review","focus_branch_refs":["root_000904/B003"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001253/B004","root_001266/B002","root_001266/B003"],"root_ids":[],"scope":"pericope","source_local_id":"B:Frying, Boiling, and the Prepared Meal","source_type":"channel","support_ids":["sup_20230814417f61a7bcda","sup_2d49dc2784a0f03037eb","sup_4571260657fc5bf2063a","sup_cdec8991b9bb84ac9175","sup_d780bfc649de54f55596"],"title":"Frying, Boiling, and the Prepared Meal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["93:1","93:11","93:5","93:7"],"branch_refs":["root_000904/B004","root_001028/B002","root_001525/B005","root_001583/B005"],"candidate_id":"cand_eff28988437e9928f8b4","commentary_obligation":"review","focus_branch_refs":["root_000904/B004"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001028/B002","root_001525/B005","root_001583/B005"],"root_ids":[],"scope":"pericope","source_local_id":"B:Offering and Sacrifice","source_type":"channel","support_ids":["sup_0f1565815a1d45812cc2","sup_2ddcdb6084243ea1535d","sup_4ebc471e274e62602fad","sup_5a6e091450560c29da23","sup_65dadf9a50ab46d5d1ad"],"title":"Offering and Sacrifice","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["93:1","93:10","93:11","93:3","93:5"],"branch_refs":["root_000532/B013","root_000904/B001","root_001559/B001","root_001559/B003"],"candidate_id":"cand_f74d9c49655ec0033d3e","commentary_obligation":"review","focus_branch_refs":["root_000904/B001"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000532/B013","root_001559/B001","root_001559/B003"],"root_ids":[],"scope":"pericope","source_local_id":"B:River, Current, and Opened Ground","source_type":"channel","support_ids":["sup_046ea8f1780d0d276e65","sup_417ccf7c6a49970f9b1d","sup_45de3d65ac0f43d3cd67","sup_645641411e9d6ab59351","sup_d864e20578135b5eb359"],"title":"River, Current, and Opened Ground","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["93:1","93:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000679/B001","root_000679/B002","root_000904/B001","root_000904/B002","root_001392/B001"],"candidate_id":"cand_63364e129fe9629ecfa7","commentary_obligation":"review","hft_ref":"hft_ab57a0ff14e88e549dda","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_cycle_visibility_and_cover","source_type":"hft","support_ids":["sup_505eb59f90dcf7b91ffd"],"title":"d_cycle_visibility_and_cover","trust":"legacy_unbound"},{"anchor_refs":["93:1","93:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000532/B002","root_000532/B007","root_000904/B006","root_001253/B003","root_001635/B001","root_001635/B002"],"candidate_id":"cand_cee7d167f096d93a41ad","commentary_obligation":"review","hft_ref":"hft_068b2b330cb63bd2bfeb","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_pause_not_relational_exit","source_type":"hft","support_ids":["sup_a1de4e211be14988a059"],"title":"d_pause_not_relational_exit","trust":"legacy_unbound"},{"anchor_refs":["93:1","93:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000019/B002","root_000067/B001","root_000067/B002","root_000452/B001","root_000904/B001","root_000904/B006","root_001684/B002"],"candidate_id":"cand_88e57ac020c8cec56f94","commentary_obligation":"review","hft_ref":"hft_86608eb9b38981b4df61","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_delayed_brightness_as_better_later","source_type":"hft","support_ids":["sup_289cdad6e176c1e5f988"],"title":"d_delayed_brightness_as_better_later","trust":"legacy_unbound"},{"anchor_refs":["93:1","93:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000532/B002","root_000537/B005","root_000569/B002","root_000904/B001","root_000904/B003","root_001028/B002"],"candidate_id":"cand_715c89701200b5aaa9bd","commentary_obligation":"review","hft_ref":"hft_b431632dcac05eb679bb","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_forenoon_as_gift_maturation","source_type":"hft","support_ids":["sup_a866c9b415f3ebb29fad"],"title":"d_forenoon_as_gift_maturation","trust":"legacy_unbound"},{"anchor_refs":["93:1","93:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000070/B001","root_000070/B002","root_000904/B002","root_001626/B001","root_001692/B001","root_001692/B002"],"candidate_id":"cand_c78647c4b0d26dfb83dc","commentary_obligation":"review","hft_ref":"hft_3f38da5051ae6b48af6f","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_visibility_finds_and_shelters","source_type":"hft","support_ids":["sup_3ab9701ea9b2b3dae50f"],"title":"d_visibility_finds_and_shelters","trust":"legacy_unbound"},{"anchor_refs":["93:1","93:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000904/B002","root_000904/B005","root_000913/B002","root_000913/B003","root_001583/B001","root_001583/B003","root_001626/B001"],"candidate_id":"cand_54a85c000f3ccb10e233","commentary_obligation":"review","hft_ref":"hft_464e8dd4462a8f4941ed","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_brightness_as_wayfinding","source_type":"hft","support_ids":["sup_b51f71c5749d3deb6888"],"title":"d_brightness_as_wayfinding","trust":"legacy_unbound"},{"anchor_refs":["93:1","93:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000904/B003","root_001068/B001","root_001068/B004","root_001110/B002","root_001626/B003"],"candidate_id":"cand_0e3baa73ac0f9682ac80","commentary_obligation":"review","hft_ref":"hft_2f4d871fbc11117ab1fa","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_forenoon_sufficiency_ecology","source_type":"hft","support_ids":["sup_00c44fa8fcb832001a3a"],"title":"d_forenoon_sufficiency_ecology","trust":"legacy_unbound"},{"anchor_refs":["93:1","93:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000904/B002","root_001266/B001","root_001692/B001"],"candidate_id":"cand_96ba0348ec5d77399a50","commentary_obligation":"review","hft_ref":"hft_fba36a745b281ef92354","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_public_light_morally_ambivalent","source_type":"hft","support_ids":["sup_6609efaa09c9be1016db"],"title":"d_public_light_morally_ambivalent","trust":"legacy_unbound"},{"anchor_refs":["93:1","93:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000661/B001","root_000736/B001","root_000904/B002","root_001559/B002","root_001559/B003","root_001559/B004"],"candidate_id":"cand_e1333bfc096aa9d84ce7","commentary_obligation":"review","hft_ref":"hft_facac0c2dcc9bd2925df","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_daylight_as_open_request_channel","source_type":"hft","support_ids":["sup_5eb68340db0beb49c3f6"],"title":"d_daylight_as_open_request_channel","trust":"legacy_unbound"},{"anchor_refs":["93:1","93:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000299/B003","root_000299/B006","root_000532/B002","root_000904/B002","root_001525/B001","root_001525/B003"],"candidate_id":"cand_6d937e7faf936862aea0","commentary_obligation":"review","hft_ref":"hft_5d2a95d3b9038ccd761e","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_brightness_must_become_testimony","source_type":"hft","support_ids":["sup_232a2e81d217f7f05b9b"],"title":"d_brightness_must_become_testimony","trust":"legacy_unbound"},{"anchor_refs":["93:1","93:5","93:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000904/B004","root_001028/B002","root_001583/B005"],"candidate_id":"cand_f9456626e31fd63aa56f","commentary_obligation":"review","hft_ref":"hft_2abf1b231655de69e463","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_sacrificial_gift_horizon","source_type":"hft","support_ids":["sup_700c0a735717486bd851"],"title":"o_sacrificial_gift_horizon","trust":"legacy_unbound"},{"anchor_refs":["93:1","93:3","93:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000904/B002","root_001253/B004","root_001266/B002"],"candidate_id":"cand_0ea93d667e05b71df20e","commentary_obligation":"review","hft_ref":"hft_e4df746bdc4c0d111056","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_thermal_transformation","source_type":"hft","support_ids":["sup_9281d059a5c59ce7cf82"],"title":"o_thermal_transformation","trust":"legacy_unbound"},{"anchor_refs":["93:1","93:2","93:6","93:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000070/B002","root_000679/B001","root_000904/B006","root_001580/B006"],"candidate_id":"cand_41d6d0fa51c3464365a2","commentary_obligation":"review","hft_ref":"hft_f377ac95a8a24832bfa4","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_lullaby_care_rhythm","source_type":"hft","support_ids":["sup_d1851db359b0882caaa9"],"title":"o_lullaby_care_rhythm","trust":"legacy_unbound"},{"anchor_refs":["93:1","93:11","93:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000299/B003","root_000299/B006","root_000904/B002","root_001110/B003"],"candidate_id":"cand_d89fb0da4706ffd68a79","commentary_obligation":"review","hft_ref":"hft_b082876e6ff897cfbe1e","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_voiced_daylight","source_type":"hft","support_ids":["sup_b41af86a4082058c74b8"],"title":"o_voiced_daylight","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_4b6a9eb3727b5657b645","connection_ref":"conn_fd682add75cfd2f16f07","note":"Immediate paired oath: the focus channel's night-and-stilling counterpart defines the local contrast.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_db58ecee3b76e1692ea6","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"93:2","source_note":"Immediate counterpart establishes the daylight side of the local sequence.","source_row_role":"ranked_review","source_target_component_ref":"93:1","source_target_components":["93:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"93:2","source_target_components":["93:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:2","target_evidence":{"arabic_uthmani":"وَٱلَّيْلِ إِذَا سَجَىٰ","ayah_ref":"93:2"},"target_ref":"93:2"},{"connection_evidence_ref":"conn_ev_80b6c8da19e318f67c4e","connection_ref":"conn_ce711c7eaaec396ae1f4","note":"Same-surah ethical sequel; it can extend the focus's care trajectory, though it does not explain ضحى directly.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_32b9e3ba5b4d2685ea53","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"93:10","source_note":"Surah daylight node supports f04 only indirectly.","source_row_role":"ranked_review","source_target_component_ref":"93:1","source_target_components":["93:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"93:10","source_target_components":["93:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:10","target_evidence":{"arabic_uthmani":"وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ","ayah_ref":"93:10"},"target_ref":"93:10"},{"connection_evidence_ref":"conn_ev_817312802242e7de1811","connection_ref":"conn_20daf1646c661d506c2a","note":"Same-surah future-over-earlier movement supports the focus's developing temporal frame without defining its image.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_00052233206bf532aac2","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"93:4","source_note":"Immediate temporal setting supports the surah's movement from an earlier state onward.","source_row_role":"ranked_review","source_target_component_ref":"93:1","source_target_components":["93:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"93:4","source_target_components":["93:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:4","target_evidence":{"arabic_uthmani":"وَلَلْءَاخِرَةُ خَيْرٌۭ لَّكَ مِنَ ٱلْأُولَىٰ","ayah_ref":"93:4"},"target_ref":"93:4"},{"connection_evidence_ref":"conn_ev_a5cb1896b4fa2ff5c80a","connection_ref":"conn_219ce94ee6f28a33f8ea","note":"Same-surah care instruction contributes the downstream ethical context, not a direct reading of the oath.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_7f978a5b291a5223900b","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"93:9","source_note":"Intra-surah opening context only; it adds no orphan or coercion specification.","source_row_role":"ranked_review","source_target_component_ref":"93:1","source_target_components":["93:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"93:9","source_target_components":["93:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:9","target_evidence":{"arabic_uthmani":"فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ","ayah_ref":"93:9"},"target_ref":"93:9"},{"connection_evidence_ref":"conn_ev_d1875157ca1d04af89bf","connection_ref":"conn_9263694f865292f135fd","note":"Same-surah guidance clause supports a developing-care context; indirect for the focus image.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_0b6c0f90384a2c330d2a","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"93:7","source_note":"Surah-opening frame only; no direct lexical or exact-route clarification.","source_row_role":"ranked_review","source_target_component_ref":"93:1","source_target_components":["93:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"93:7","source_target_components":["93:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:7","target_evidence":{"arabic_uthmani":"وَوَجَدَكَ ضَآلًّۭا فَهَدَىٰ","ayah_ref":"93:7"},"target_ref":"93:7"},{"connection_evidence_ref":"conn_ev_bba499a3b15dd5f35628","connection_ref":"conn_ae28788b9c7ba991b673","note":"Immediate response to the paired oaths; essential local context for reading the focus against perceived departure.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_648e64086ce808154c1d","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"93:3","source_note":"The opening daylight oath frames the passage but adds no direct denial.","source_row_role":"ranked_review","source_target_component_ref":"93:1","source_target_components":["93:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"93:3","source_target_components":["93:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:3","target_evidence":{"arabic_uthmani":"مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ","ayah_ref":"93:3"},"target_ref":"93:3"},{"connection_evidence_ref":"conn_ev_4691ec2e1e0ab08a5168","connection_ref":"conn_75ba48921798ae6e6502","note":"Same-surah closing instruction can support the f03 disclosure trajectory, but remains indirect.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_6c328f231c16284e786f","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"93:11","source_note":"The surah opening supplies atmosphere but no distinct reading of the final command.","source_row_role":"ranked_review","source_target_component_ref":"93:1","source_target_components":["93:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"93:11","source_target_components":["93:11"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:11","target_evidence":{"arabic_uthmani":"وَأَمَّا بِنِعْمَةِ رَبِّكَ فَحَدِّثْ","ayah_ref":"93:11"},"target_ref":"93:11"},{"connection_evidence_ref":"conn_ev_b5291d283af94184e16b","connection_ref":"conn_adf51efeb5703a836de1","note":"Same-surah promised giving develops the response following the oaths, without defining ضحى.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_7cadfe961475735026eb","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"93:5","source_note":"Opening oath supplies the local temporal frame for the surah's forward assurance.","source_row_role":"ranked_review","source_target_component_ref":"93:1","source_target_components":["93:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"93:5","source_target_components":["93:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:5","target_evidence":{"arabic_uthmani":"وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ","ayah_ref":"93:5"},"target_ref":"93:5"},{"connection_evidence_ref":"conn_ev_92b6b5c950d1e313201a","connection_ref":"conn_86259beffab6591b7368","note":"Same-surah recollection of care gives context for the assurance framed by the opening oaths.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_f402ebac5da4b461cac5","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"93:6","source_note":"The opening oath gives only distant local context.","source_row_role":"ranked_review","source_target_component_ref":"93:1","source_target_components":["93:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"93:6","source_target_components":["93:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:6","target_evidence":{"arabic_uthmani":"أَلَمْ يَجِدْكَ يَتِيمًۭا فَـَٔاوَىٰ","ayah_ref":"93:6"},"target_ref":"93:6"},{"connection_evidence_ref":"conn_ev_60c8263bc240eb3ae9d6","connection_ref":"conn_e3920b25927ad154d12d","note":"Same-surah movement from need to sufficiency supports the care trajectory, indirectly.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_08fa43539815f454d51c","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"93:8","source_note":"Opening oath context is too general after the stronger nearby cards.","source_row_role":"ranked_review","source_target_component_ref":"93:1","source_target_components":["93:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:1"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"93:8","source_target_components":["93:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"93:8","target_evidence":{"arabic_uthmani":"وَوَجَدَكَ عَآئِلًۭا فَأَغْنَىٰ","ayah_ref":"93:8"},"target_ref":"93:8"}],"focus":{"arabic_uthmani":"وَٱلضُّحَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"93:1:1:1","qac_word_ref":"93:1:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"93:1:1:2","qac_word_ref":"93:1:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","root_ar":"ض ح و","surface_ar":"ضُّحَىٰ"}],"word_analysis_qac_refs":[["93:1:1:1"],["93:1:1:2","93:1:1:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["93:1:1","93:1:2"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلضُّحَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"93:1:1:1","qac_word_ref":"93:1:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"93:1:1:2","qac_word_ref":"93:1:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","root_ar":"ض ح و","surface_ar":"ضُّحَىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["93:1:1:1"],["93:1:1:2","93:1:1:3"]],"word_analysis_refs":["93:1:1","93:1:2"],"word_rows":[{"analysis_record_ref":"93:1:1","analytic_gloss_range_en":"surah-opening oath particle that governs the following definite noun, launches fresh discourse, and keeps the oath answer beyond this ayah","analytic_root_gloss_range_en":null,"qac_refs":["93:1:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"93:1:2","analytic_gloss_range_en":"the definite forenoon brightness as a sworn witness: a recognized, self-standing light/time phenomenon with exposure and disclosure pressure, not a local sacrifice sense or mere clock point","analytic_root_gloss_range_en":"forenoon daylight, visible exposure, early-day activity, Adha sacrifice terms, brightness, and reviewed slow/gentle expressions; locally the forenoon daylight and exposure-brightness branches are relevant, while sacrifice and meal branches remain derivative background","qac_refs":["93:1:1:2","93:1:1:3"],"root":{"arabic":"ض ح و","transliteration":"ḍ-ḥ-w"},"surface":{"arabic":"ٱلضُّحَىٰ","transliteration":"aḍ-ḍuḥā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":2,"words_total":2,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":11,"missing_anchor_refs":[],"supplied_unique_anchor_count":11},"assigned_record_count":14,"assigned_records":[{"anchor_refs":["93:1","93:2"],"branch_refs":["root_000679/B001","root_000679/B002","root_000904/B001","root_000904/B002","root_001392/B001"],"candidate_id":"cand_63364e129fe9629ecfa7","evidence_scope":"declared_pericope","hft_ref":"hft_ab57a0ff14e88e549dda","item_id":"d_cycle_visibility_and_cover","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_cycle_visibility_and_cover","support_id":"sup_505eb59f90dcf7b91ffd"},{"anchor_refs":["93:1","93:3"],"branch_refs":["root_000532/B002","root_000532/B007","root_000904/B006","root_001253/B003","root_001635/B001","root_001635/B002"],"candidate_id":"cand_cee7d167f096d93a41ad","evidence_scope":"declared_pericope","hft_ref":"hft_068b2b330cb63bd2bfeb","item_id":"d_pause_not_relational_exit","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_pause_not_relational_exit","support_id":"sup_a1de4e211be14988a059"},{"anchor_refs":["93:1","93:4"],"branch_refs":["root_000019/B002","root_000067/B001","root_000067/B002","root_000452/B001","root_000904/B001","root_000904/B006","root_001684/B002"],"candidate_id":"cand_88e57ac020c8cec56f94","evidence_scope":"declared_pericope","hft_ref":"hft_86608eb9b38981b4df61","item_id":"d_delayed_brightness_as_better_later","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_delayed_brightness_as_better_later","support_id":"sup_289cdad6e176c1e5f988"},{"anchor_refs":["93:1","93:5"],"branch_refs":["root_000532/B002","root_000537/B005","root_000569/B002","root_000904/B001","root_000904/B003","root_001028/B002"],"candidate_id":"cand_715c89701200b5aaa9bd","evidence_scope":"declared_pericope","hft_ref":"hft_b431632dcac05eb679bb","item_id":"d_forenoon_as_gift_maturation","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_forenoon_as_gift_maturation","support_id":"sup_a866c9b415f3ebb29fad"},{"anchor_refs":["93:1","93:6"],"branch_refs":["root_000070/B001","root_000070/B002","root_000904/B002","root_001626/B001","root_001692/B001","root_001692/B002"],"candidate_id":"cand_c78647c4b0d26dfb83dc","evidence_scope":"declared_pericope","hft_ref":"hft_3f38da5051ae6b48af6f","item_id":"d_visibility_finds_and_shelters","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_visibility_finds_and_shelters","support_id":"sup_3ab9701ea9b2b3dae50f"},{"anchor_refs":["93:1","93:7"],"branch_refs":["root_000904/B002","root_000904/B005","root_000913/B002","root_000913/B003","root_001583/B001","root_001583/B003","root_001626/B001"],"candidate_id":"cand_54a85c000f3ccb10e233","evidence_scope":"declared_pericope","hft_ref":"hft_464e8dd4462a8f4941ed","item_id":"d_brightness_as_wayfinding","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_brightness_as_wayfinding","support_id":"sup_b51f71c5749d3deb6888"},{"anchor_refs":["93:1","93:8"],"branch_refs":["root_000904/B003","root_001068/B001","root_001068/B004","root_001110/B002","root_001626/B003"],"candidate_id":"cand_0e3baa73ac0f9682ac80","evidence_scope":"declared_pericope","hft_ref":"hft_2f4d871fbc11117ab1fa","item_id":"d_forenoon_sufficiency_ecology","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_forenoon_sufficiency_ecology","support_id":"sup_00c44fa8fcb832001a3a"},{"anchor_refs":["93:1","93:9"],"branch_refs":["root_000904/B002","root_001266/B001","root_001692/B001"],"candidate_id":"cand_96ba0348ec5d77399a50","evidence_scope":"declared_pericope","hft_ref":"hft_fba36a745b281ef92354","item_id":"d_public_light_morally_ambivalent","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_public_light_morally_ambivalent","support_id":"sup_6609efaa09c9be1016db"},{"anchor_refs":["93:1","93:10"],"branch_refs":["root_000661/B001","root_000736/B001","root_000904/B002","root_001559/B002","root_001559/B003","root_001559/B004"],"candidate_id":"cand_e1333bfc096aa9d84ce7","evidence_scope":"declared_pericope","hft_ref":"hft_facac0c2dcc9bd2925df","item_id":"d_daylight_as_open_request_channel","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_daylight_as_open_request_channel","support_id":"sup_5eb68340db0beb49c3f6"},{"anchor_refs":["93:1","93:11"],"branch_refs":["root_000299/B003","root_000299/B006","root_000532/B002","root_000904/B002","root_001525/B001","root_001525/B003"],"candidate_id":"cand_6d937e7faf936862aea0","evidence_scope":"declared_pericope","hft_ref":"hft_5d2a95d3b9038ccd761e","item_id":"d_brightness_must_become_testimony","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_brightness_must_become_testimony","support_id":"sup_232a2e81d217f7f05b9b"},{"anchor_refs":["93:1","93:5","93:7"],"branch_refs":["root_000904/B004","root_001028/B002","root_001583/B005"],"candidate_id":"cand_f9456626e31fd63aa56f","evidence_scope":"declared_pericope","hft_ref":"hft_2abf1b231655de69e463","item_id":"o_sacrificial_gift_horizon","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_sacrificial_gift_horizon","support_id":"sup_700c0a735717486bd851"},{"anchor_refs":["93:1","93:3","93:9"],"branch_refs":["root_000904/B002","root_001253/B004","root_001266/B002"],"candidate_id":"cand_0ea93d667e05b71df20e","evidence_scope":"declared_pericope","hft_ref":"hft_e4df746bdc4c0d111056","item_id":"o_thermal_transformation","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_thermal_transformation","support_id":"sup_9281d059a5c59ce7cf82"},{"anchor_refs":["93:1","93:2","93:6","93:7"],"branch_refs":["root_000070/B002","root_000679/B001","root_000904/B006","root_001580/B006"],"candidate_id":"cand_41d6d0fa51c3464365a2","evidence_scope":"declared_pericope","hft_ref":"hft_f377ac95a8a24832bfa4","item_id":"o_lullaby_care_rhythm","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_lullaby_care_rhythm","support_id":"sup_d1851db359b0882caaa9"},{"anchor_refs":["93:1","93:11","93:8"],"branch_refs":["root_000299/B003","root_000299/B006","root_000904/B002","root_001110/B003"],"candidate_id":"cand_d89fb0da4706ffd68a79","evidence_scope":"declared_pericope","hft_ref":"hft_b082876e6ff897cfbe1e","item_id":"o_voiced_daylight","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_voiced_daylight","support_id":"sup_b41af86a4082058c74b8"}],"diagnostics":[],"lane_counts":{"global":11,"macro":14,"micro":5},"packet_summary":{"ayah_count":11,"focus_ref":"93:1","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"و ج د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001626","furuq_root_norm":"و ج د","furuq_source_root_norm":"و ج د","is_dominant":true,"target_occurrences":61,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000227","furuq_root_norm":"ج د د","furuq_source_root_norm":"ج د د","is_dominant":false,"target_occurrences":10,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ء ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000661","furuq_root_norm":"س ء ل","furuq_source_root_norm":"س أ ل","is_dominant":true,"target_occurrences":118,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000736","furuq_root_norm":"س ل ل","furuq_source_root_norm":"س ل ل","is_dominant":false,"target_occurrences":2,"target_rank":2}]}],"window":["93:1","93:2","93:3","93:4","93:5","93:6","93:7","93:8","93:9","93:10","93:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"93:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":19,"unstructured_record_count":0},"identity":{"ayah_ref":"93:1","lane":"macro","linguistic_source_ref":"93:1","surface_ref":"93:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"93:1","target_tokens":[["Kuşluk",["93:1:1"]],["vaktine",["93:1:1"]],["andolsun",["93:1:1"]]],"text":"Kuşluk vaktine andolsun."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":14,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":11,"id":"s093-p01-001-011","label":"Whole surah","number":1,"refs":["93:1","93:2","93:3","93:4","93:5","93:6","93:7","93:8","93:9","93:10","93:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"93:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"93:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["93:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"93:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:River, Current, and Opened Ground","source_type":"channel","support_id":"sup_046ea8f1780d0d276e65","text":"Abundant water cuts through land, opens a channel, and continues as a broad current.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Daylight, Night, and Stilling","source_type":"channel","support_id":"sup_0a4d742a14d6d2461050","text":"Bright daytime opens and extends, then night covers the scene and settles into stillness.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Offering and Sacrifice","source_type":"channel","support_id":"sup_0f1565815a1d45812cc2","text":"Livestock supplies the object, selection as a sacrificial animal gives it ritual status, transfer directs it to the sanctuary, and giving explains the offering relation.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Frying, Boiling, and the Prepared Meal","source_type":"channel","support_id":"sup_20230814417f61a7bcda","text":"Materials change through thickening, heat, abrasion, washing, and polishing.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Daylight, Night, and Stilling","source_type":"channel","support_id":"sup_284ab30aa31ce7d1948b","text":"Forenoon supplies both duration and radiance, while night supplies darkness and `سَجَىٰ` supplies the act of becoming still. The lexical opening of daylight completes a cycle in which illumination expands, darkness arrives, and motion subsides.","trust":"trusted"},{"branch_refs":["root_000532/B014","root_000904/B003","root_000913/B005","root_001068/B008","root_001525/B005","root_001635/B008","root_001692/B001"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Herd, Grazing, and the Stray","source_type":"channel","support_id":"sup_2a30b6a52dd9e12a63f4","text":"gathered herd `ر ب ب:B014/m01`; livestock `ن ع م:B005/m01`; early grazing `ض ح و:B003/m02`; stray animal `ض ل ل:B005/m01`; directionless stray `ع ي ل:B008/m01`; breeding male retained for the herd `و د ع:B008/m01`; motherless animal `ي ت م:B001/m02`","trust":"trusted"},{"branch_refs":["root_000904/B003","root_001253/B004","root_001266/B002","root_001266/B003"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"B:Frying, Boiling, and the Prepared Meal","source_type":"channel","support_id":"sup_2d49dc2784a0f03037eb","text":"frying on a pan `ق ل ي:B004/m01`; meat altered by heat `ق ه ر:B002/m01`; hot-stone dairy and flour dish `ق ه ر:B003/m01`; morning meal `ض ح و:B003/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Daylight, Night, and Stilling","source_type":"channel","support_id":"sup_2d978237f198c0c9b4c5","text":"Things occupy phases, move through ordered succession, and become manifest after absence.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Offering and Sacrifice","source_type":"channel","support_id":"sup_2ddcdb6084243ea1535d","text":"93:1 `ٱلضُّحَىٰ`; 93:5 `يُعْطِيكَ`; 93:7 `فَهَدَىٰ`; 93:11 `بِنِعْمَةِ`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Herd, Grazing, and the Stray","source_type":"channel","support_id":"sup_329dc30c1dd53ce07636","text":"Animals are gathered, grazed, lost, sheltered, bred, hunted, or transferred as offerings.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Herd, Grazing, and the Stray","source_type":"channel","support_id":"sup_37697cd9e95e933be08b","text":"93:1 `ٱلضُّحَىٰ`; 93:3, 93:5, 93:11 `رَبُّكَ` and `رَبِّكَ`; 93:3 `وَدَّعَكَ`; 93:6 and 93:9 `يَتِيمًا`, `ٱلْيَتِيمَ`; 93:7 `ضَآلًّا`; 93:8 `عَآئِلًا`; 93:11 `بِنِعْمَةِ`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:River, Current, and Opened Ground","source_type":"channel","support_id":"sup_417ccf7c6a49970f9b1d","text":"93:1 `ٱلضُّحَىٰ`; 93:3, 93:5, 93:11 `رَبُّكَ` and `رَبِّكَ`; 93:10 `تَنْهَرْ`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Frying, Boiling, and the Prepared Meal","source_type":"channel","support_id":"sup_4571260657fc5bf2063a","text":"Frying provides direct pan heat, heated meat shows moisture leaving under fire, and the hot-stone mixture shows boiling and stirring into a finished preparation. The morning meal gives the transformed food its serving context.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:River, Current, and Opened Ground","source_type":"channel","support_id":"sup_45de3d65ac0f43d3cd67","text":"Air, cloud, light, and flowing water form an environment through which land, vegetation, and travelers are sustained or directed.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Offering and Sacrifice","source_type":"channel","support_id":"sup_4ebc471e274e62602fad","text":"Animals are gathered, grazed, lost, sheltered, bred, hunted, or transferred as offerings.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Daylight, Night, and Stilling","source_type":"channel","support_id":"sup_5a5ddba1ab7267c5b86b","text":"93:1 `ٱلضُّحَىٰ`; 93:2 `ٱلَّيْلِ`, `سَجَىٰ`; 93:10 `تَنْهَرْ`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Offering and Sacrifice","source_type":"channel","support_id":"sup_5a6e091450560c29da23","text":"Livestock is selected, transferred toward a sacred destination, and slaughtered as an offering.","trust":"trusted"},{"branch_refs":["root_000532/B013","root_000904/B001","root_001559/B001","root_001559/B003"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"B:River, Current, and Opened Ground","source_type":"channel","support_id":"sup_645641411e9d6ab59351","text":"flowing river `ن ه ر:B001/m01`; opening and widening a channel `ن ه ر:B003/m01`; abundant gathered water `ر ب ب:B013/m01`; exposed daylight `ض ح و:B001/m01`","trust":"trusted"},{"branch_refs":["root_000904/B004","root_001028/B002","root_001525/B005","root_001583/B005"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"B:Offering and Sacrifice","source_type":"channel","support_id":"sup_65dadf9a50ab46d5d1ad","text":"ritual offering sent to the sanctuary `ه د ي:B005/m01`; sacrificial animal `ض ح و:B004/m01`; livestock fit for offering `ن ع م:B005/m01`; transfer as gift `ع ط و:B002/m01`","trust":"trusted"},{"branch_refs":["root_000679/B001","root_000904/B001","root_000904/B005","root_001392/B001","root_001559/B002"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Daylight, Night, and Stilling","source_type":"channel","support_id":"sup_6de832772998fb3b589c","text":"extended forenoon `ض ح و:B001/m01`; clear forenoon brightness `ض ح و:B005/m01`; night and darkness `ل ي ل:B001/m01`; night settling into stillness `س ج و:B001/m01`; daylight opening `ن ه ر:B002/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Herd, Grazing, and the Stray","source_type":"channel","support_id":"sup_b174b5fb40a75adb4292","text":"Herd and livestock establish collective ownership, early grazing establishes routine, and the retained male sustains reproduction. Straying breaks the owner-animal relation, while motherlessness creates the animal form of lost care.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Frying, Boiling, and the Prepared Meal","source_type":"channel","support_id":"sup_cdec8991b9bb84ac9175","text":"Food is exposed to heat, releases or absorbs liquid, thickens into a dish, and is served as a meal.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Frying, Boiling, and the Prepared Meal","source_type":"channel","support_id":"sup_d780bfc649de54f55596","text":"93:1 `ٱلضُّحَىٰ`; 93:3 `قَلَىٰ`; 93:9 `تَقْهَرْ`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:River, Current, and Opened Ground","source_type":"channel","support_id":"sup_d864e20578135b5eb359","text":"Abundant water supplies the material, opening and widening supply the geomorphic action, and the river is the stable path produced by that action. Daylight exposes the channel as an open feature of the land.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Herd, Grazing, and the Stray","source_type":"channel","support_id":"sup_e88f761376ec049a96c8","text":"A herd grazes early, depends on an owner, produces breeding stock, and risks losing animals to the open waste.","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"},{"arabic_uthmani":"وَٱلَّيْلِ إِذَا سَجَىٰ","ayah_ref":"93:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000679/B001","root_000679/B002","root_000904/B001","root_000904/B002","root_001392/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000904","role":"Extended risen daylight supplies the visible phase that can recur after a settled interval.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000904","role":"Open prominence supplies the exposed pole whose temporary withdrawal needs interpretation.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001392","role":"Night as the darkness contrary to day supplies the alternating, non-visible pole.","root":"ل ي ل","source_ref":"93:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000679","role":"Settled stillness under the enclosing night makes concealment a repose rather than a rupture.","root":"س ج و","source_ref":"93:2","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000679","role":"Covering with a cloth sharpens the image of light being veiled without being destroyed.","root":"س ج و","source_ref":"93:2","source_word_indices":["3"]}],"changed_reading":{"after":"Duha is the returning visible phase of a rhythm that also contains stillness and covering; its force does not require continuous exposure.","before":"Duha signifies uninterrupted visibility and disclosure."},"confidence":"strong","mechanism":"The oath-pair places exposed, extending forenoon beside night in its settling and covering phase. Visibility and concealment become alternating modes in one rhythm; the cessation of exposure is not the cessation of the cycle.","model_id":"d_cycle_visibility_and_cover","reader_inference":"The packet supplies extending public daylight and night as darkness, stillness, and covering; I infer a recurrent alternation in which concealment pauses exposure without negating it. A live alternative is a simple rhetorical contrast with no causal cycle.","status":"revised","structural_cues":["93:1–2 coordinate two oath objects, while إذا marks night in its settling phase rather than naming abstract darkness alone."],"trigger_roots":["ل ي ل","س ج و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_cycle_visibility_and_cover","source_type":"hft","support_id":"sup_505eb59f90dcf7b91ffd","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"},{"arabic_uthmani":"مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ","ayah_ref":"93:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000532/B002","root_000532/B007","root_000904/B006","root_001253/B003","root_001635/B001","root_001635/B002"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000904","role":"Gentle delay supplies a positive account of temporal pause before later denials exclude harsher accounts.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001635","role":"Leaving and relinquishing supply the rupture that the verse explicitly negates.","root":"و د ع","source_ref":"93:3","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001635","role":"Ease and stillness preserve a non-hostile sense of pause once abandonment is denied.","root":"و د ع","source_ref":"93:3","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000532","role":"Nurturing, repair, and completion make the continuing relation developmental rather than merely possessive.","root":"ر ب ب","source_ref":"93:3","source_word_indices":["3"]},{"branch_id":"B007","mapped_root_id":"root_000532","role":"Remaining, dwelling, and duration supply continuity beneath the apparent interval.","root":"ر ب ب","source_ref":"93:3","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001253","role":"Aversion that distances the heart supplies the rejected affective explanation for obscurity.","root":"ق ل ي","source_ref":"93:3","source_word_indices":["5"]}],"changed_reading":{"after":"The delayed or veiled light becomes a test case for pause without rejection: obscurity does not entail that care has exited.","before":"Gentle delay remains a lexical possibility with no relational consequence."},"confidence":"strong","mechanism":"The denial of leaving and aversion, framed by enduring nurture, converts the gentle-delay baseline into a relational diagnostic. A quiet interval can be repose, but it is not abandonment, expulsion, or the heart's withdrawal.","model_id":"d_pause_not_relational_exit","reader_inference":"The packet supplies leaving, repose, nurturing endurance, and heart-distancing aversion; I infer that the denied rupture recodes darkness or delay as an interval within continued care. A live alternative is that the oath only reassures externally and does not alter the semantics of ضحى.","status":"strengthened","structural_cues":["The parallel negations ما ... وما bracket the possessive relation ربك and address the addressee directly."],"trigger_roots":["و د ع","ر ب ب","ق ل ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_pause_not_relational_exit","source_type":"hft","support_id":"sup_a1de4e211be14988a059","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"},{"arabic_uthmani":"وَلَلْءَاخِرَةُ خَيْرٌۭ لَّكَ مِنَ ٱلْأُولَىٰ","ayah_ref":"93:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000019/B002","root_000067/B001","root_000067/B002","root_000452/B001","root_000904/B001","root_000904/B006","root_001684/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000904","role":"Daylight rising and extending supplies a natural process with distinguishable earlier and later phases.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B006","mapped_root_id":"root_000904","role":"Gentle postponement makes the superior later phase compatible with present waiting.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000019","role":"Deferral to a later time supplies the temporal displacement beyond the present phase.","root":"ء خ ر","source_ref":"93:4","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000452","role":"Beneficial good assigns positive direction rather than mere lateness to the movement.","root":"خ ي ر","source_ref":"93:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000067","role":"Beginning and precedence establish the initial phase from which the comparison departs.","root":"ء و ل","source_ref":"93:4","source_word_indices":["5"]},{"branch_id":"B002","mapped_root_id":"root_000067","role":"Return to an outcome or consequence gives the temporal extension a telos.","root":"ء و ل","source_ref":"93:4","source_word_indices":["5"]},{"branch_id":"B002","mapped_root_id":"root_001684","role":"The non-dominant split image of one thing following another supplies continuity between phases without a vacant gap.","root":"ء و ل","source_ref":"93:4","source_word_indices":["5"]}],"changed_reading":{"after":"Duha's extension is directional: a first condition can pass continuously into a later condition that carries greater good.","before":"Duha's extension is neutral duration."},"confidence":"strong","mechanism":"Later, beneficial good, beginning, outcome, and unbroken succession turn extended duha into directed maturation. Its rise is not neutral duration but a trajectory in which an initial state gives way to a more beneficial later disclosure.","model_id":"d_delayed_brightness_as_better_later","reader_inference":"The packet supplies laterness, beneficial good, beginning, consequence, and close succession; I infer that the rising course of duha analogizes a better-later trajectory. A live alternative is that the contrast is wholly eschatological and the daylight image remains only an oath witness.","status":"strengthened","structural_cues":["The comparative خير with من explicitly orders the later and the first, turning temporal contrast into valuation."],"trigger_roots":["ء خ ر","خ ي ر","ء و ل"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_delayed_brightness_as_better_later","source_type":"hft","support_id":"sup_289cdad6e176c1e5f988","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"},{"arabic_uthmani":"وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ","ayah_ref":"93:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000532/B002","root_000537/B005","root_000569/B002","root_000904/B001","root_000904/B003","root_001028/B002"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000904","role":"Forenoon feeding and grazing supply the material scene in which a gift becomes sustaining provision.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000904","role":"The extending daytime interval gives provision time to arrive and have an effect.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001028","role":"Passing something to another supplies the concrete transfer at the start of the provisioning chain.","root":"ع ط و","source_ref":"93:5","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000532","role":"Nurturing and bringing to completion turn transfer into sustained development.","root":"ر ب ب","source_ref":"93:5","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_000537","role":"The non-dominant split image of feeding and growth intensifies the maturation mechanism.","root":"ر ب ب","source_ref":"93:5","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000569","role":"Abundant or sought satisfaction supplies the experienced completion toward which the gift develops.","root":"ر ض و","source_ref":"93:5","source_word_indices":["4"]}],"changed_reading":{"after":"Duha becomes a promise-shaped provisioning interval in which what is given is nurtured until it becomes satisfying.","before":"Duha merely marks the daily time when feeding occurs."},"confidence":"medium","mechanism":"The meal-and-grazing branch joins hand-to-hand giving, nurturing growth, and eventual satisfaction. Future giving fits the extended interval: provision arrives, is taken in, and matures into enough rather than appearing as an inert object.","model_id":"d_forenoon_as_gift_maturation","reader_inference":"The packet supplies forenoon feeding, transfer, nurture, growth, and satisfaction; I infer a gift-to-growth-to-contentment chain. A live alternative is that satisfaction concerns an unspecified gift with no nourishment or daylight mechanism.","status":"strengthened","structural_cues":["سوف opens a future interval, and the فاء in فترضى presents satisfaction as the result of giving."],"trigger_roots":["ع ط و","ر ب ب","ر ض و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_forenoon_as_gift_maturation","source_type":"hft","support_id":"sup_a866c9b415f3ebb29fad","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"},{"arabic_uthmani":"أَلَمْ يَجِدْكَ يَتِيمًۭا فَـَٔاوَىٰ","ayah_ref":"93:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000070/B001","root_000070/B002","root_000904/B002","root_001626/B001","root_001692/B001","root_001692/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000904","role":"Open visibility supplies the condition in which an otherwise isolated person can be noticed.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001626","role":"Encountering and locating something turns visibility into an act of finding.","root":"و ج د","source_ref":"93:6","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001692","role":"A child cut off from a guardian supplies the vulnerable state that visibility discovers.","root":"ي ت م","source_ref":"93:6","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001692","role":"Singularity and separation widen orphanhood into a structural image of isolation.","root":"ي ت م","source_ref":"93:6","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000070","role":"Joining a gathering refuge supplies the spatial reversal from exposed isolation to shelter.","root":"ء و ي","source_ref":"93:6","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000070","role":"Tender mercy supplies the affective quality that makes shelter more than containment.","root":"ء و ي","source_ref":"93:6","source_word_indices":["4"]}],"changed_reading":{"after":"Daylight finds isolated vulnerability so that exposure can terminate in refuge and belonging.","before":"Daylight exposes what was hidden."},"confidence":"strong","mechanism":"Public visibility becomes ethically productive when finding an isolated, unguarded person leads to gathering shelter and compassion. Light is a search field whose proper endpoint is enclosure and belonging, not exposure for its own sake.","model_id":"d_visibility_finds_and_shelters","reader_inference":"The packet supplies visibility, finding, severed isolation, gathering refuge, and compassion; I infer that illumination enables recognition and that recognition calls for shelter. A live alternative is a biographical rescue sequence with no instrumental link to daylight.","status":"new","structural_cues":["The rhetorical question ألم recalls a prior state, and the result فآوى binds finding to an answering act of shelter."],"trigger_roots":["و ج د","ي ت م","ء و ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_visibility_finds_and_shelters","source_type":"hft","support_id":"sup_3ab9701ea9b2b3dae50f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"},{"arabic_uthmani":"وَوَجَدَكَ ضَآلًّۭا فَهَدَىٰ","ayah_ref":"93:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000904/B002","root_000904/B005","root_000913/B002","root_000913/B003","root_001583/B001","root_001583/B003","root_001626/B001"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000904","role":"Clear brightness supplies enough distinction for orientation rather than mere visibility.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000904","role":"Emergence into visible prominence supplies the transition out of hiddenness.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001626","role":"Finding what was not securely located initiates the recovery mechanism.","root":"و ج د","source_ref":"93:7","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000913","role":"Hiddenness and disappearance supply an optical-spatial account of being unlocated.","root":"ض ل ل","source_ref":"93:7","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000913","role":"Loss supplies the condition that finding and direction reverse.","root":"ض ل ل","source_ref":"93:7","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001583","role":"Gentle indication toward a path supplies non-coercive direction after discovery.","root":"ه د ي","source_ref":"93:7","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001583","role":"A guide moving at the front gives the visible field a leading edge and destination.","root":"ه د ي","source_ref":"93:7","source_word_indices":["3"]}],"changed_reading":{"after":"Duha is operative wayfinding: it brings the unlocated into view and gives that visibility a direction.","before":"Clear brightness makes the scene legible."},"confidence":"strong","mechanism":"Clear prominence becomes navigational: a hidden or lost state is found and then gently directed. Daylight does not merely display objects; it yields a path, a leading edge, and an orientation.","model_id":"d_brightness_as_wayfinding","reader_inference":"The packet supplies clarity, hidden loss, finding, and gentle path-indication; I infer that visibility enables orientation. A live alternative is that ضال marks uncertainty resolved by guidance without any optical mechanism.","status":"strengthened","structural_cues":["The result فهدى makes guidance follow the recalled unlocated state, preserving a directional sequence."],"trigger_roots":["و ج د","ض ل ل","ه د ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_brightness_as_wayfinding","source_type":"hft","support_id":"sup_b51f71c5749d3deb6888","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"},{"arabic_uthmani":"وَوَجَدَكَ عَآئِلًۭا فَأَغْنَىٰ","ayah_ref":"93:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000904/B003","root_001068/B001","root_001068/B004","root_001110/B002","root_001626/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000904","role":"Early feeding and grazing supply the daily material operation through which lack can be answered.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001626","role":"Capacity, means, and wealth supply the resource state discovered or produced in the reversal.","root":"و ج د","source_ref":"93:8","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001068","role":"Poverty and need supply the deficit from which the provisioning sequence begins.","root":"ع ي ل","source_ref":"93:8","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001068","role":"Poor nourishment makes the deficit bodily and connects it directly to the focus's feeding branch.","root":"ع ي ل","source_ref":"93:8","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001110","role":"Sufficiency and adequacy define the endpoint as enoughness rather than excess.","root":"غ ن ي","source_ref":"93:8","source_word_indices":["3"]}],"changed_reading":{"after":"The oath bears a recurring anti-scarcity pattern: embodied lack is met until there is enough to sustain life.","before":"Forenoon is merely when feeding happens."},"confidence":"strong","mechanism":"The forenoon meal and grazing image joins poverty and poor nourishment to capacity and sufficiency. Duha becomes a recurrent conversion of lack into enough, an ecology of support rather than a display of accumulated wealth.","model_id":"d_forenoon_sufficiency_ecology","reader_inference":"The packet supplies poverty, poor nourishment, capacity, sufficiency, and the focus's feeding time; I infer a recurrent provision-through-activity mechanism. A live alternative is nonmaterial sufficiency, which weakens the meal connection but preserves the lack-to-enough movement.","status":"strengthened","structural_cues":["The repeated وجدك ... فأغنى pattern presents an encountered deficit followed by a causally marked reversal."],"trigger_roots":["و ج د","ع ي ل","غ ن ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_forenoon_sufficiency_ecology","source_type":"hft","support_id":"sup_00c44fa8fcb832001a3a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"},{"arabic_uthmani":"فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ","ayah_ref":"93:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000904/B002","root_001266/B001","root_001692/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000904","role":"Exposure and public prominence supply the morally ambivalent field in which power becomes visible and actionable.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001692","role":"Severance from a guardian supplies the asymmetrically exposed person lacking protective backing.","root":"ي ت م","source_ref":"93:9","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001266","role":"Dominance descending from above and humiliating its object supplies the abusive use of superior standing.","root":"ق ه ر","source_ref":"93:9","source_word_indices":["4"]}],"changed_reading":{"after":"Prominence is morally ambivalent: full visibility can enable care or vertical crushing, so the daylight oath places publicity under non-domination.","before":"Open prominence is inherently beneficial because it makes things visible."},"confidence":"strong","mechanism":"Exposure is dangerous under hierarchy. An unguarded, isolated person under an overpowering force from above turns public visibility into an ethical test: prominence can notice and protect, or it can make vulnerability easier to crush.","model_id":"d_public_light_morally_ambivalent","reader_inference":"The packet supplies public exposure, severed guardianship, and subjugation from above; I infer that one who received shelter must not weaponize superior visibility or status. A live alternative is an ethical sequel with no semantic revision of the oath.","status":"revised","structural_cues":["فأما shifts from remembered rescue to addressed conduct, and فلا reverses the addressee from former recipient of care into a possible agent of domination."],"trigger_roots":["ي ت م","ق ه ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_public_light_morally_ambivalent","source_type":"hft","support_id":"sup_6609efaa09c9be1016db","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"},{"arabic_uthmani":"وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ","ayah_ref":"93:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000661/B001","root_000736/B001","root_000904/B002","root_001559/B002","root_001559/B003","root_001559/B004"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000904","role":"Open public appearance supplies the interpersonal space in which a need can become present to another.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000661","role":"Asking and requesting supply the explicit movement of need toward a listener.","root":"س ء ل","source_ref":"93:10","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000736","role":"The non-dominant split image of gentle, hidden drawing suggests that some requests emerge indirectly and must be noticed without force.","root":"س ء ل","source_ref":"93:10","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001559","role":"Day opening in brightness directly links the response-space back to the focus's daylight.","root":"ن ه ر","source_ref":"93:10","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_001559","role":"Opening and widening until something flows supply the channel mechanics of social receptivity.","root":"ن ه ر","source_ref":"93:10","source_word_indices":["4"]},{"branch_id":"B004","mapped_root_id":"root_001559","role":"Harsh verbal rebuke supplies the closing force that the prohibition removes from the channel.","root":"ن ه ر","source_ref":"93:10","source_word_indices":["4"]}],"changed_reading":{"after":"Duha's opening becomes interpersonal permeability: make room for requests, including quietly emerging ones, and do not dam them with harsh speech.","before":"Duha's openness is visual and public."},"confidence":"medium","mechanism":"The نهر inventory creates an internal reversal among day opening, widening until flow, and harsh rebuke. Alongside overt request and the split image of gentle hidden extraction, duha becomes an open channel through which even indirect need can enter; scolding blocks that flow.","model_id":"d_daylight_as_open_request_channel","reader_inference":"The packet supplies request, gentle hidden drawing, day-opening, widening flow, and harsh rebuke; I infer social access as a channel and scolding as anti-flow. A live alternative is the direct command 'do not scold,' with the day and flow images remaining only branch resonance.","status":"new","structural_cues":["وأما ... فلا parallels the orphan case, placing the seeker before the negated response; the one surface تنهر resolves to both opening and rebuke branches."],"trigger_roots":["س ء ل","ن ه ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_daylight_as_open_request_channel","source_type":"hft","support_id":"sup_5eb68340db0beb49c3f6","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"},{"arabic_uthmani":"وَأَمَّا بِنِعْمَةِ رَبِّكَ فَحَدِّثْ","ayah_ref":"93:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000299/B003","root_000299/B006","root_000532/B002","root_000904/B002","root_001525/B001","root_001525/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000904","role":"Visible prominence supplies the focus-side movement from hidden condition into public manifestation.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001525","role":"A good, benefited condition supplies the content that has become manifest and can be recounted.","root":"ن ع م","source_ref":"93:11","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001525","role":"Praising something with نعم gives narration an affirmative evaluative register.","root":"ن ع م","source_ref":"93:11","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000532","role":"Nurturing and completion identify care, rather than self-display, as the source of the visible good.","root":"ر ب ب","source_ref":"93:11","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000299","role":"Speech continually renewed as news turns received benefit into an ongoing verbal event.","root":"ح د ث","source_ref":"93:11","source_word_indices":["4"]},{"branch_id":"B006","mapped_root_id":"root_000299","role":"Bringing something out and making it appear mirrors the focus's visible disclosure in speech.","root":"ح د ث","source_ref":"93:11","source_word_indices":["4"]}],"changed_reading":{"after":"Duha is a disclosure cycle: care becomes visible, and visible benefit becomes renewed testimony rather than remaining mute.","before":"Public brightness is an object that is seen."},"confidence":"strong","mechanism":"Good condition and nurturing completion culminate in renewed speech and disclosure. Public daylight is not self-contained display: what care has brought into manifest form is to be manifested again as narration.","model_id":"d_brightness_must_become_testimony","reader_inference":"The packet supplies good condition, nurturing completion, renewed speech, and disclosure; I infer that received manifestation should cause verbal manifestation. A live alternative is simply reporting benefits, without importing any daylight mechanics.","status":"revised","structural_cues":["وأما ... فحدث turns remembered benefit into a positive command, while ربك recurs and the فاء marks narration as an output."],"trigger_roots":["ن ع م","ر ب ب","ح د ث"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_brightness_must_become_testimony","source_type":"hft","support_id":"sup_232a2e81d217f7f05b9b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"},{"arabic_uthmani":"وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ","ayah_ref":"93:5"},{"arabic_uthmani":"وَوَجَدَكَ ضَآلًّۭا فَهَدَىٰ","ayah_ref":"93:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000904/B004","root_001028/B002","root_001583/B005"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000904","role":"The Adha sacrifice supplies a root-internal horizon of something offered up at a marked time.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001028","role":"Concrete giving supplies the transfer that lets sacrifice be modeled as offering rather than loss alone.","root":"ع ط و","source_ref":"93:5","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_001583","role":"The sacrificial animal conveyed to the sanctuary supplies a context-side image of directed gift and destination.","root":"ه د ي","source_ref":"93:7","source_word_indices":["3"]}],"changed_reading":{"after":"At the root-image margin, the marked time also opens an offering economy in which a gift is directed toward a sacred end.","before":"The oath marks only a luminous time."},"confidence":"exploratory","containment":"This is surprising because the ordinary focus sense is a time of day and the sacrificial image is a derivationally distant branch. It remains valid as a packet-attested ضحى branch directly anchored in 93:1 and is reinforced by giving and sacrificial-guidance branches in context. Render only as a latent offering resonance, never as a replacement translation of والضحى.","focus_anchor":"The focus root itself includes the Adha sacrificial animal as B004.","outlier_id":"o_sacrificial_gift_horizon"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_sacrificial_gift_horizon","source_type":"hft","support_id":"sup_700c0a735717486bd851","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"},{"arabic_uthmani":"مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ","ayah_ref":"93:3"},{"arabic_uthmani":"فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ","ayah_ref":"93:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000904/B002","root_001253/B004","root_001266/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000904","role":"Sun exposure and heat supply the thermal field in which prominence can become ordeal.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_001253","role":"Food placed on a hot pan until it changes supplies controlled heat as a material transformation.","root":"ق ل ي","source_ref":"93:3","source_word_indices":["5"]},{"branch_id":"B002","mapped_root_id":"root_001266","role":"Meat seized and altered by fire supplies destructive heat as an analogue for overpowering exposed vulnerability.","root":"ق ه ر","source_ref":"93:9","source_word_indices":["4"]}],"changed_reading":{"after":"Exploratorily, exposure also subjects what appears to transforming pressure, making the ban on domination a refusal to turn public light into consuming heat.","before":"Exposure in duha simply reveals."},"confidence":"exploratory","containment":"This cross-material reading is surprising because frying and meat altered by fire are remote from the direct verbal senses in context. It remains anchored in the focus branch's explicit sun exposure and heat, and the two context branches jointly model exposed matter being transformed. Render as a contained analogy for pressure on the exposed, not as a claim that the verses literally describe cooking.","focus_anchor":"Focus B002 includes exposure to the sun and its heat as well as public emergence.","outlier_id":"o_thermal_transformation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_thermal_transformation","source_type":"hft","support_id":"sup_9281d059a5c59ce7cf82","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"},{"arabic_uthmani":"وَٱلَّيْلِ إِذَا سَجَىٰ","ayah_ref":"93:2"},{"arabic_uthmani":"أَلَمْ يَجِدْكَ يَتِيمًۭا فَـَٔاوَىٰ","ayah_ref":"93:6"},{"arabic_uthmani":"وَوَجَدَكَ ضَآلًّۭا فَهَدَىٰ","ayah_ref":"93:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000070/B002","root_000679/B001","root_000904/B006","root_001580/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000904","role":"Gentle slowing supplies the unhurried tempo to which the care images attach.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000679","role":"Settling stillness supplies the quiet phase of an alternation between waking visibility and rest.","root":"س ج و","source_ref":"93:2","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000070","role":"Tender compassion supplies the relational quality that prevents slowing from becoming neglect.","root":"ء و ي","source_ref":"93:6","source_word_indices":["4"]},{"branch_id":"B006","mapped_root_id":"root_001580","role":"The non-dominant split image of rocking a child to sleep supplies a rhythmic, soothing mode of guidance.","root":"ه د ي","source_ref":"93:7","source_word_indices":["3"]}],"changed_reading":{"after":"At the exploratory edge, duha participates in a care rhythm that alternates awakening, settling, sheltering, and soothing rather than forcing immediate motion.","before":"Gentle delay is only patient waiting for daylight."},"confidence":"exploratory","containment":"This is surprising because the lullaby image comes through a non-dominant split mapping of هدى and is formally distant from route-guidance. It remains worth carrying because focus B006 already anchors gentleness and slowing, while settling night and compassionate shelter form a coherent care rhythm. Render as a sonic-affective analogy, explicitly qualified as split-branch activation.","focus_anchor":"Focus B006 gives ضحى a gentle, unhurried tempo.","outlier_id":"o_lullaby_care_rhythm"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_lullaby_care_rhythm","source_type":"hft","support_id":"sup_d1851db359b0882caaa9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"},{"arabic_uthmani":"وَأَمَّا بِنِعْمَةِ رَبِّكَ فَحَدِّثْ","ayah_ref":"93:11"},{"arabic_uthmani":"وَوَجَدَكَ عَآئِلًۭا فَأَغْنَىٰ","ayah_ref":"93:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000299/B003","root_000299/B006","root_000904/B002","root_001110/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000904","role":"Public emergence supplies the shared arena in which visible benefit can acquire a voice.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001110","role":"Song and voice convert sufficiency from a silent state into an audible expression.","root":"غ ن ي","source_ref":"93:8","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000299","role":"Renewed speech and news give the audible manifestation recurrence rather than a single utterance.","root":"ح د ث","source_ref":"93:11","source_word_indices":["4"]},{"branch_id":"B006","mapped_root_id":"root_000299","role":"Making something appear links verbal disclosure back to the focus's visual disclosure.","root":"ح د ث","source_ref":"93:11","source_word_indices":["4"]}],"changed_reading":{"after":"A live cross-sensory reading lets public brightness become voiced: what is made visible is repeatedly articulated as news.","before":"Duha manifests silently through sight."},"confidence":"medium","containment":"This is cross-sensory because daylight is visual while song and renewed report are audible. It remains anchored in the focus's public-emergence branch and gains a coherent context sequence from voice to recurrent disclosure. Render as synesthetic public manifestation—brightness becoming voiced testimony—not as a lexical meaning of ضحى.","focus_anchor":"Focus B002 makes duha an event of coming visibly and publicly forth.","outlier_id":"o_voiced_daylight"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_voiced_daylight","source_type":"hft","support_id":"sup_b41af86a4082058c74b8","trust":"legacy_unbound"}]}
</lane_packet_json>
