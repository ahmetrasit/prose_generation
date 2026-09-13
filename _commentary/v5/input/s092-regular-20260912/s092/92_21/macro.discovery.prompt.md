# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **92:21**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s092-regular-20260912/s092/92_21/macro.discovery.json` and modify nothing
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
  "ayah_ref": "92:21",
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
{"branch_registry":[{"boundary":"Includes rababah/rabab as a covenant, pact, or protection agreement, arabah as covenanters, and rabab as tithes when explained like a covenant.","branch_kind":null,"branch_ref":"root_000532/B011","candidate_links":[{"candidate_id":"cand_18703bcf347440afcb42","lane":"macro"}],"focus_root_occurrences":[],"gloss":"covenant or pact close to a binding bundle","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"ربابة عهد وميثاق","image_en":"covenant or pact close to a binding bundle"}}],"root_ar":"ر ب ب","root_id":"root_000532","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"ربابة عهد وميثاق","image_en":"covenant or pact close to a binding bundle","scope_ar":"يدخل فيه الربابة والرباب للعهد والميثاق والجوار، والأربة للمعاهدين، والرباب للعشور إذا جعل كالعهد","scope_en":"Includes rababah/rabab as a covenant, pact, or protection agreement, arabah as covenanters, and rabab as tithes when explained like a covenant."},"support_links":["sup_ccec50095c07b4e1540f"]},{"boundary":"Temel durum, yönelinen şeyi kabul etmeyi de kapsar; karşılıklı hoşnutlaşma, başkasını hoşnut etme, yoğunluk bildiren ad ve üstün gelme kullanımı bu dalın çekirdeğine katılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000569/B001","candidate_links":[{"candidate_id":"cand_9641fb3c7d43ca2d5618","lane":"macro"},{"candidate_id":"cand_62a9229cd296274eb852","lane":"macro"},{"candidate_id":"cand_8e5fb0a604a1c43c11ba","lane":"macro"},{"candidate_id":"cand_7c46be0cb75535197987","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"رَّضِىَ","morph_features":"STEM|POS:V|IMPF|LEM:r~aDiYa|ROOT:rDw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:21:2:1","qac_word_ref":"92:21:2","surface_ar":"يَرْضَىٰ"}],"gloss":"hoşnut olma ve kabul etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hoşnutluk, öfke ve hoşnutsuzluğun karşıtı olan olumlu kabul durumudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Durum bir şeye veya kişiye yöneldiğinde onu benimseme, uygun bulma ve kabul etme anlamı taşır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanrı-kul ilişkisinde aynı çekirdek, taraflara göre hükme karşı çıkmama ve buyruğa uygun davranışı onaylama biçiminde ayrışır."}}],"root_ar":"ر ض و","root_id":"root_000569","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Öfke ve hoşnutsuzluğun karşıtı olan iç durumu ve bu durumun bir şeyi ya da kişiyi benimsemeye yönelmesini birlikte karşılar.","boundary_detail":"Temel durum, yönelinen şeyi kabul etmeyi de kapsar; karşılıklı hoşnutlaşma, başkasını hoşnut etme, yoğunluk bildiren ad ve üstün gelme kullanımı bu dalın çekirdeğine katılmaz.","branch_image_ar":"الرضا خلاف السخط","concept_gloss":"hoşnut olma ve kabul etme","contextual_glosses":[{"applicability":"Bir kişi ya da davranış hakkında öfkenin kalktığı ve olumlu değerlendirmenin oluştuğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yönelinen kişi hakkındaki olumlu değerlendirmeyi korur."},"facet_ids":["F001","F002"],"text":"ondan hoşnut oldu","usage_role":"contextual"},{"applicability":"Bir şeyin, seçimin veya kişinin benimsenip uygun görüldüğü geçişli bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Benimseme, kabul ve uygun bulma yönlerini korur."},"facet_ids":["F002"],"text":"onu kabul edip uygun buldu","usage_role":"contextual"},{"applicability":"Kulun Tanrı'nın hükmü karşısındaki hoşnutluğunu açıklayan özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kulun hüküm karşısında hoşnutsuzluk göstermemesi ölçütünü korur."},"facet_ids":["F003"],"text":"hükme içten karşı çıkmadı","usage_role":"explanatory"}],"definition":"Bir şeye ya da kimseye karşı öfke ve hoşnutsuzluk duymayı bırakıp onu benimsemek, uygun bulmak veya ondan hoşnut olmaktır. Tanrı-kul ilişkisinde bu durum, kul açısından hükme içten karşı çıkmama; Tanrı açısından ise kulun buyruğa uyup yasaktan kaçınmasını uygun bulma ölçütleriyle özelleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hoşnutluk, öfke ve hoşnutsuzluğun karşıtı olan olumlu kabul durumudur."},{"facet_id":"F002","role":"extension","statement":"Durum bir şeye veya kişiye yöneldiğinde onu benimseme, uygun bulma ve kabul etme anlamı taşır."},{"facet_id":"F003","role":"specialization","statement":"Tanrı-kul ilişkisinde aynı çekirdek, taraflara göre hükme karşı çıkmama ve buyruğa uygun davranışı onaylama biçiminde ayrışır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Belirgin bir coşku ve neşe duygusu ekler.","collision":"Hoşnutluğu geçici bir sevinç duygusuyla karıştırır.","fit":"displacement","loses":"Öfkenin karşıtı olma, uygun bulma ve kabul etme öğelerini kaybeder.","preserves":"Olumlu bir iç yöneliş bulunduğunu kısmen korur."},"text":"sevinç"}],"identity_rationale":"Yetkili ifade, anlamın merkezini hoşnutsuzluk ve öfkenin karşıtı olan hoşnutlukta kurar; bir şeyi veya kişiyi kabul etme ile kendisinden hoşnut olunan tarafı da bu merkeze bağlar. Kulun Tanrı karşısındaki ve Tanrı'nın kul karşısındaki hoşnutluğu ise katılımcıları ve ölçütleri farklı iki özel uygulama olarak verilir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"hoşnut olmak; kabul etmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"hoşnut"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kabul edilmiş; kendisinden hoşnut olunan"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kendisinden hoşnut olunan kişi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"hoşnutluk"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"onu kabul edip uygun buldu"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"onu seçip uygun buldu"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"ondan hoşnut oldu; onu kabul etti"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"hoşnutluk adı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"beğenilen bir yaşayış"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"onu arkadaş olarak kabul etti"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ondan hoşnut oldu; onu uygun buldu"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"beğenilen; kabul edilen"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"Tanrı'nın kulu buyruğa uyan ve yasaktan kaçınan biri olarak görmesi"}],"lexicalization_note":"Tanım, yalın hoşnutluk çekirdeğini korurken nesneye, kişiye ve Tanrı-kul ilişkisine bağlı kullanımları ayrı özel yüzler olarak gösterir; bu kullanımlar yalın anlamın tamamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; temel karşıtlık, kabul ve yetinme yakınlıkları ile karşılıklı ve ettirgen kardeş dallar sınırı en açık biçimde gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu dal olumlu kabul kutbunu, komşu ise aynı eksenin olumsuz ve öfkeli kutbunu gösterir; bu nedenle karşıtlık doğrudandır.","focus_only":"Hoşnut olma, benimseme ve uygun bulma yönünü taşır.","gloss":"hoşnutluk / öfke ve hoşnutsuzluk","neighbor_only":"Öfke, beğenmeme ve hoşnutsuzluk yönünü taşır.","neighbor_ref":"root_000686/B001","relation_type":"antonym","shared_zone":"İkisi de bir şey ya da kişi hakkındaki değerlendirme ve duygusal tutum eksenindedir."},{"boundary_match":"partial","distinction":"Komşu dal hoşnutluğu pay, geçim veya azla yetinme koşuluna bağlar; bu dalda böyle bir yeterlilik sınırı yoktur.","focus_only":"Her tür kişi veya şeye yönelen genel hoşnutluk ve kabulü kapsar.","gloss":"hoşnutluk / elindekine yetinme","neighbor_only":"Payına düşene yetinme ve azla geçinme sınırını özellikle taşır.","neighbor_ref":"root_001263/B001","relation_type":"near_synonym","shared_zone":"Her ikisinde de elde olana karşı hoşnutsuzluk göstermeme vardır."},{"boundary_match":"partial","distinction":"Kabul komşusunda alma veya geçerli sayma eylemi yeterli olabilir; bu dal ise buna hoşnutluk ve öfkesizlik durumunu da bağlar.","focus_only":"İç hoşnutluk durumunu ve öfkenin kalkmasını kurucu öğe sayar.","gloss":"hoşnut olup benimseme / kabul etme","neighbor_only":"Bir şeyi, özrü, armağanı veya işi alma ve kabul etme eylemini öne çıkarır.","neighbor_ref":"root_001198/B004","relation_type":"near_synonym","shared_zone":"Bir şeyi olumlu karşılayıp geri çevirmeme alanında örtüşürler."},{"boundary_match":"partial","distinction":"Bu dal tek yönlü veya yöneltilmiş olabilir; komşu dalda karşılıklılık kurucu bir koşuldur.","focus_only":"Tek bir tarafın bir şeyden veya kişiden hoşnut olmasını da kapsar.","gloss":"hoşnut olma / karşılıklı hoşnutlaşma","neighbor_only":"İki ya da daha çok tarafın birbirlerinden hoşnutluk göstermesini gerektirir.","neighbor_ref":"root_000569/B003","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak alanı olumlu kabul ve hoşnutluktur."},{"boundary_match":"partial","distinction":"Bu dal durum ve değerlendirmeyi, komşu dal ise o durumu başka bir kişide meydana getiren ya da isteyen eylemi merkez alır.","focus_only":"Bir öznenin mevcut hoşnutluk ve kabul durumunu anlatır.","gloss":"hoşnut olma / hoşnut etme","neighbor_only":"Başka bir kişide hoşnutluk oluşturma veya ondan hoşnutluk isteme işlemini anlatır.","neighbor_ref":"root_000569/B004","relation_type":"near_neighbor","shared_zone":"İki dal da hoşnutsuzluğun giderildiği aynı genel durum alanına katılır."}],"source_phrase_ar":"أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضا مقصور (ayn)؛ رضيت الشيء وارتضيته فهو مرضي ومرضو ورضيت عنه رضا (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو ورضا العبد عن الله ورضا الله عن العبد (mufradat)","source_summary":"Kaynakların ortak çizgisi hoşnutluğu öfke ve hoşnutsuzluğun karşıtı sayar; ayrıca kabul edilen tarafı ve hoşnutluğun yöneldiği nesne ya da kişiyi gösterir. Bir tanıklık ayrıca Tanrı-kul ilişkisindeki iki yönün ölçütlerini birbirinden ayırır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أصل الرضا والقبول وترك الكراهة، ورضي يرضى، والراضي، والمرضي أو المرضو عنه","what_is_not_ar":"ليس هو الرضوان الكثير خاصة، ولا المراضاة من اثنين، ولا الغلبة في قولهم راضاني فرضوته"},"support_links":["sup_4bc153124929efa0f62d","sup_51399e621030adfb6a5d","sup_68dab5d4db31f58d24f5","sup_be1a3cf49b3f7cd249fa"]},{"boundary":"Dal, hoşnutluğu adlandıran belirli biçimlerle sınırlıdır; yoğunluk bunlardan biri için kaynaklar arası bir anlam farkıdır, genel çekirdeğin zorunlu öğesi değildir.","branch_kind":"bare","branch_ref":"root_000569/B002","candidate_links":[{"candidate_id":"cand_9641fb3c7d43ca2d5618","lane":"macro"},{"candidate_id":"cand_647e3faf1f6ad542c0ec","lane":"macro"},{"candidate_id":"cand_94508efab8ab397dd9dd","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"رَّضِىَ","morph_features":"STEM|POS:V|IMPF|LEM:r~aDiYa|ROOT:rDw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:21:2:1","qac_word_ref":"92:21:2","surface_ar":"يَرْضَىٰ"}],"gloss":"hoşnutluk; yoğun hoşnutluk","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki ad biçimi de hoşnutluk durumunu adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad biçimlerinden biri, bir tanıklıkta genel anlamdan daha yoğun ve bol hoşnutluk olarak yorumlanır."}}],"root_ar":"ر ض و","root_id":"root_000569","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli ad biçimlerinin genel hoşnutluğu veya kaynak yorumuna göre onun yoğun derecesini bildirdiği yerlerde kullanılır.","boundary_detail":"Dal, hoşnutluğu adlandıran belirli biçimlerle sınırlıdır; yoğunluk bunlardan biri için kaynaklar arası bir anlam farkıdır, genel çekirdeğin zorunlu öğesi değildir.","branch_image_ar":"الرضوان والمرضاة اسم للرضا الكثير أو المطلوب","concept_gloss":"hoşnutluk; yoğun hoşnutluk","contextual_glosses":[{"applicability":"Ad biçiminin temel hoşnutluk durumuyla eşdeğer kullanıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın temel hoşnutluk anlamını eksiksiz korur."},"facet_ids":["F001"],"text":"hoşnutluk","usage_role":"general"},{"applicability":"Ad biçiminin hoşnutluğun çokluğunu veya yoğunluğunu belirttiği özel yorumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yoğun ve bol hoşnutluk yorumunu açıkça korur."},"facet_ids":["F002"],"text":"engin hoşnutluk","usage_role":"contextual"}],"definition":"Hoşnutluk durumunu adlandıran iki ad biçimidir. Bunlardan biri kimi tanıklıkta genel hoşnutlukla eşdeğerken bir tanıklıkta hoşnutluğun çokluğu veya yoğunluğu olarak açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki ad biçimi de hoşnutluk durumunu adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Ad biçimlerinden biri, bir tanıklıkta genel anlamdan daha yoğun ve bol hoşnutluk olarak yorumlanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Karşılık olarak verilen somut veya soyut bir kazanç anlamı ekler.","collision":"Hoşnutluğun kendisini hoşnutluk sonucunda verilebilecek bir karşılıkla karıştırır.","fit":"displacement","loses":"Hoşnutluk durumunu ve onun yoğunluk ayrımını bütünüyle kaybeder.","preserves":"Olumlu değerlendirmeyle ilişkilendirilebilmesini çok dolaylı biçimde korur."},"text":"ödül"}],"identity_rationale":"Yetkili ifade iki ad biçimini hoşnutlukla ilişkilendirir ve bunlardan biri için bir kaynakta yoğunluk bildirir. Hazırlanmış çerçevedeki 'istenen' ya da 'aranan' anlamı ise kaynak ifadesinde yer almadığından tanımdan çıkarılmıştır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"hoşnutluk; yoğun hoşnutluk"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"hoşnutluk"}],"lexicalization_note":"Tanım yalnızca kanıtta verilen yalın ad biçimlerinin hoşnutluk ve bir tanıklıkta yoğun hoşnutluk bildirmesiyle sınırlıdır; karşılıklı ya da ettirgen kullanımlar eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; temel hoşnutluk dalı, geniş küme adayı ve olumlu duygu alanındaki iki komşu, ad biçimi ile yoğunluk sınırını en yararlı şekilde açtığı için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli ad biçimlerine ve olası yoğunluk farkına bağlıdır; komşu dal genel durumu ve onun yönelimli kullanımlarını anlatır.","focus_only":"Hoşnutluğu adlandıran iki belirli biçimi ve bunlardan birindeki yoğunluk yorumunu kapsar.","gloss":"hoşnutluk adı / hoşnut olma","neighbor_only":"Hoşnut olma eylemini, hoşnut kişiyi ve bir şeye yönelen kabulü daha geniş biçimde kapsar.","neighbor_ref":"root_000569/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak çekirdeği öfkenin karşıtı olan hoşnutluk durumudur."},{"boundary_match":"partial","distinction":"Komşu çok daha geniş bir türetim alanıdır; bu dalın sınırı iki ad biçimi ve bunların anlam farkıdır.","focus_only":"Belirli iki ad biçimini ve bunlardan birinin yoğunluk yorumunu ayrı bir dal olarak tutar.","gloss":"yoğun hoşnutluk adı / geniş hoşnutluk kümesi","neighbor_only":"Hoşnutlukla birlikte kabul, ettirgenlik, karşılıklılık ve başka türemiş kullanımları geniş bir kümede toplar.","neighbor_ref":"root_000570/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de hoşnutluğu ve onu adlandıran biçimleri içerir."},{"boundary_match":"field_only","distinction":"Bu dal kabul edici hoşnutluk durumudur; komşu dal sevinç, iyilik görme ve onurlandırılma sonuçlarını öne çıkarır.","focus_only":"Bir değerlendirme durumu olarak hoşnutluğu ve onun yoğunluğunu bildirir.","gloss":"yoğun hoşnutluk / sevinç ve nimet","neighbor_only":"Sevinç, nimet ve onurlandırılma durumlarını bildirir.","neighbor_ref":"root_000287/B005","relation_type":"same_field","shared_zone":"İkisi de olumlu duygulanım ve iyi karşılanma alanında yer alır."},{"boundary_match":"partial","distinction":"Beğenip sevinme belirli bir tepki ve sevinç taşır; bu dalda sevinç zorunlu değildir ve asıl öğe hoşnutluktur.","focus_only":"Süreklilik gösterebilen bir hoşnutluk durumunu adlandırır.","gloss":"hoşnutluk / beğenip sevinme","neighbor_only":"Bir şey karşısında beğeni ve sevinç duymayı birlikte anlatır.","neighbor_ref":"root_000832/B004","relation_type":"near_neighbor","shared_zone":"Olumlu değerlendirme ve iyi hissetme alanında örtüşürler."}],"source_phrase_ar":"الرضوان اسم موضوع من الرضا (ayn)؛ الرضوان الرضا وكذلك الرضوان بالضم والمرضاة مثله (sihah)؛ الرضوان الرضا الكثير (mufradat)","source_summary":"Toplu tanıklık, iki ad biçimini hoşnutluk adı olarak bir araya getirir; kaynaklar arasındaki fark, bunlardan birinin genel hoşnutluk mu yoksa çok ve yoğun hoşnutluk mu bildirdiğidir.","sources":["AY","SI","MU"],"what_is_ar":"يدخل فيه الرضوان والمرضاة بوصفهما اسما أو صيغة للرضا، وخاصة الرضوان الكثير في كلام المفردات","what_is_not_ar":"ليس مطلق فعل رضي وحده، ولا المراضاة المتبادلة بين طرفين"},"support_links":["sup_51399e621030adfb6a5d","sup_6ee6121e2651b60beb8e","sup_afbcb90733bed8a1a59d"]},{"boundary":"Karşılıklılık zorunludur; tek taraflı hoşnutluk, bir başkasını hoşnut etme çabası ve çekişmede üstün gelme bu dalın dışında kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000569/B003","candidate_links":[{"candidate_id":"cand_56af131a36c2eab633b1","lane":"macro"},{"candidate_id":"cand_7c46be0cb75535197987","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"رَّضِىَ","morph_features":"STEM|POS:V|IMPF|LEM:r~aDiYa|ROOT:rDw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:21:2:1","qac_word_ref":"92:21:2","surface_ar":"يَرْضَىٰ"}],"gloss":"karşılıklı hoşnutluk ve kabul","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hoşnutluk ve kabul iki taraf arasında karşılıklı olarak kurulur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tarafların her biri ötekinden hoşnut olduğunu ve onu kabul ettiğini gösterir."}}],"root_ar":"ر ض و","root_id":"root_000569","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki ya da daha çok tarafın birbirlerini uygun bulup birbirlerinden hoşnutluk gösterdiği durumların genel karşılığıdır.","boundary_detail":"Karşılıklılık zorunludur; tek taraflı hoşnutluk, bir başkasını hoşnut etme çabası ve çekişmede üstün gelme bu dalın dışında kalır.","branch_image_ar":"المراضاة والتراضي رضا متبادل","concept_gloss":"karşılıklı hoşnutluk ve kabul","contextual_glosses":[{"applicability":"Tarafların birbirlerini olumlu karşılayıp hoşnutluklarını karşılıklı biçimde gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki tarafın birbirinden hoşnut olması koşulunu korur."},"facet_ids":["F001"],"text":"karşılıklı olarak hoşnut oldular","usage_role":"general"},{"applicability":"İç hoşnutluktan çok tarafların birbirlerini benimsediğini açık etmek gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı kabulü ve her tarafın ötekini uygun bulmasını korur."},"facet_ids":["F001","F002"],"text":"birbirlerini kabul edip uygun buldular","usage_role":"explanatory"}],"definition":"İki ya da daha çok tarafın birbirlerini kabul edip birbirlerinden hoşnut olduklarını karşılıklı olarak göstermeleridir. Her tarafın ötekini uygun bulması ve bu hoşnutluğu dışa vurması yapının kurucu koşuludur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hoşnutluk ve kabul iki taraf arasında karşılıklı olarak kurulur."},{"facet_id":"F002","role":"specialization","statement":"Tarafların her biri ötekinden hoşnut olduğunu ve onu kabul ettiğini gösterir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Görüş, karar veya koşullar üzerinde uzlaşma anlamını ekler.","collision":"Kişiler arası hoşnutluğu bir konu üzerindeki uzlaşmayla karıştırabilir.","fit":"broadening","loses":"Her tarafın ötekinden hoşnut olması ve bunu göstermesi koşulunu kaybeder.","preserves":"Tarafların aynı yönde buluşması düşüncesini kısmen korur."},"text":"anlaşma"}],"identity_rationale":"Yetkili ifade, iki tarafın birbirinden hoşnut olmasını ve her birinin ötekini kabul ettiğini göstermesini açıkça kurucu öğe yapar. Eylem adı ve tarafların bu durumu aralarında göstermesi aynı karşılıklı yapı içinde birleşir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"karşılıklı hoşnutluk"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"birbiriyle hoşnutlaşma"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"birbirlerinden hoşnut olduklarını karşılıklı gösterdiler"}],"lexicalization_note":"Tanım, karşılıklı eylem biçimleri ile tarafların birbirlerinden hoşnutluk gösterdiği yapıyı birlikte fakat açıkça karşılıklılık koşuluna bağlı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tek yönlü hoşnutluk ile uyuşma, iş üzerinde uzlaşma, uyma ve karşılıklı kararlaştırma adayları karşılıklılık koşulunu en net biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın kurulması için en az iki taraflı hoşnutluk gerekir; komşu dal tek yönlü bir tutumla da gerçekleşir.","focus_only":"Her tarafın ötekinden hoşnut olmasıyla kurulan karşılıklı ilişkiyi gerektirir.","gloss":"karşılıklı hoşnutluk / hoşnut olma","neighbor_only":"Tek bir tarafın bir şeyden veya kişiden hoşnut olmasını da kapsar.","neighbor_ref":"root_000569/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da olumlu kabul ve hoşnutsuzluğun kalkması alanındadır."},{"boundary_match":"partial","distinction":"Uyuşma komşusu duygu veya kabul gerektirmeden eşleşme bildirebilir; bu dalda karşılıklı hoşnutluk kurucudur.","focus_only":"Tarafların birbirlerinden hoşnut ve birbirlerini kabul eder olması gerekir.","gloss":"karşılıklı hoşnutluk / uyuşma","neighbor_only":"Nesnelerin birbirine uyması, sözlerin örtüşmesi veya kişilerin aynı görüşte buluşması yeterlidir.","neighbor_ref":"root_000927/B003","relation_type":"near_synonym","shared_zone":"Tarafların çatışmadan aynı yönde bulunması bakımından örtüşürler."},{"boundary_match":"partial","distinction":"Komşu dalda uzlaşmanın konusu belirli bir iştir; bu dalda ise ilişki tarafların birbirlerine yönelik hoşnutluğudur.","focus_only":"Tarafların birbirlerini kabul etmesine ve birbirlerinden hoşnut olmasına odaklanır.","gloss":"karşılıklı hoşnutluk / bir iş üzerinde uzlaşma","neighbor_only":"Topluluğun belirli bir iş üzerinde, özellikle kestirime dayalı biçimde uzlaşmasına odaklanır.","neighbor_ref":"root_001610/B003","relation_type":"near_synonym","shared_zone":"Birden çok tarafın gönüllü biçimde ortak bir noktaya gelmesi alanında örtüşürler."},{"boundary_match":"partial","distinction":"Uyma davranışsal bir izleme veya eşleşme olabilir; bu dal ise her iki tarafın birbirinden hoşnut olmasını gerektirir.","focus_only":"Karşılıklı hoşnutluk ve kabulün kendisini bildirir.","gloss":"karşılıklı hoşnutluk / uyma ve uyuşma","neighbor_only":"Birinin ötekine uyması, onu izlemesi veya onunla aynı yönde davranmasını bildirir.","neighbor_ref":"root_000956/B002","relation_type":"near_neighbor","shared_zone":"Tarafların çatışmayıp birbirine yönelmesi bakımından yakınlaşırlar."},{"boundary_match":"partial","distinction":"Karşılıklı kararlaştırma bir işlem veya konu çevresindedir; bu dal tarafların birbirlerini olumlu kabul etmesi çevresindedir.","focus_only":"Tarafların birbirlerine yönelik hoşnutluklarını kurucu sayar.","gloss":"karşılıklı hoşnutluk / karşılıklı kararlaştırma","neighbor_only":"Belirli bir işin koşullarını karşılıklı olarak kararlaştırmayı veya tartışmayı kurucu sayar.","neighbor_ref":"root_001657/B011","relation_type":"near_neighbor","shared_zone":"İki tarafın birlikte ve gönüllü biçimde hareket ettiği ilişkisel alanda buluşurlar."}],"source_phrase_ar":"المراضاة من اثنين (ayn)؛ مصدر راضيته رضاء ومراضاة (sihah;tahdhib)؛ إذا تراضوا بينهم أي أظهر كل واحد منهم الرضا بصاحبه ورضيه (mufradat)","source_summary":"Tanıklıklar, bu kullanımı iki taraflı hoşnutluk ilişkisi ve onun eylem adı olarak verir. Toplu ifade, tarafların birbirlerini kabul etmelerinin yanı sıra bu hoşnutluğu karşılıklı olarak göstermelerini de açıklar.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه المراضاة من اثنين، ومصدر راضيته، والتراضي بينهم حين يظهر كل واحد الرضا بصاحبه","what_is_not_ar":"ليس رضا طرف واحد فقط، ولا إرضاء الغير بعد جهد، ولا غلبة راضاني فرضوته"},"support_links":["sup_a7376aec448cd5a67406","sup_be1a3cf49b3f7cd249fa"]},{"boundary":"Merkez, öznenin kendi hoşnutluğu değil başka birinin hoşnut olmasını sağlama ya da istemedir; karşılıklı hoşnutluk ayrıca kurulmadıkça bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000569/B004","candidate_links":[{"candidate_id":"cand_b7c23c193d1764e69611","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"رَّضِىَ","morph_features":"STEM|POS:V|IMPF|LEM:r~aDiYa|ROOT:rDw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:21:2:1","qac_word_ref":"92:21:2","surface_ar":"يَرْضَىٰ"}],"gloss":"başkasını hoşnut etme veya hoşnutluğunu isteme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Özne, başka bir kişiyi hoşnut duruma getirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hoşnut etme sonucu kimi biçimde ancak çaba gösterildikten sonra elde edilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özne karşı taraftan hoşnutluk ister ve karşı tarafın onu hoşnut etmesiyle sonuçlanan bir ilişki kurar."}}],"root_ar":"ر ض و","root_id":"root_000569","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin hoşnutsuzluğunu giderip onu hoşnut kılmayı veya ondan olumlu kabul istemeyi anlatan kullanımları kapsar.","boundary_detail":"Merkez, öznenin kendi hoşnutluğu değil başka birinin hoşnut olmasını sağlama ya da istemedir; karşılıklı hoşnutluk ayrıca kurulmadıkça bu dala girmez.","branch_image_ar":"الإرضاء طلب رضا الغير وإزالة سخطه","concept_gloss":"başkasını hoşnut etme veya hoşnutluğunu isteme","contextual_glosses":[{"applicability":"Öznenin karşı taraftaki hoşnutsuzluğu giderip kendisine yönelik olumlu tutum oluşturduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başkasında hoşnutluk meydana getirme sonucunu korur."},"facet_ids":["F001"],"text":"onu kendisinden hoşnut etti","usage_role":"general"},{"applicability":"Hoşnut etme sonucunun emek veya çaba sonrasında elde edildiği özel biçim için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hoşnut etme sonucunu ve öncesindeki çabayı korur."},"facet_ids":["F002"],"text":"uğraşarak onu hoşnut etti","usage_role":"contextual"},{"applicability":"Öznenin karşı taraftan kendisine yönelik hoşnutluk ve kabul istediği kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karşı tarafın sonunda özneyi hoşnut etmesi sonucunu açıkça söylemez.","preserves":"Karşı taraftan hoşnutluk isteme aşamasını korur."},"facet_ids":["F003"],"text":"ondan hoşnutluk göstermesini istedi","usage_role":"explanatory"}],"definition":"Başka bir kişide kendisine veya bir duruma yönelik hoşnutluk oluşturmak ya da o kişiden hoşnutluk göstermesini istemektir. Bazı biçimler sonucun çabayla elde edildiğini, bazıları ise istemenin ardından karşı tarafın özneyi hoşnut ettiğini ayrıca bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Özne, başka bir kişiyi hoşnut duruma getirir."},{"facet_id":"F002","role":"specialization","statement":"Hoşnut etme sonucu kimi biçimde ancak çaba gösterildikten sonra elde edilir."},{"facet_id":"F003","role":"extension","statement":"Özne karşı taraftan hoşnutluk ister ve karşı tarafın onu hoşnut etmesiyle sonuçlanan bir ilişki kurar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Hoşnut etmeyi yalnızca öfkeyi geçici olarak dindirmeye indirger.","fit":"narrowing","loses":"Olumlu hoşnutluk oluşturma, bunu isteme ve sonucun çabayla elde edilmesi ayrımlarını kaybeder.","preserves":"Olumsuz bir tutumu giderme çabasını kısmen korur."},"text":"yatıştırma"}],"identity_rationale":"Yetkili ifade, başka bir kişide hoşnutluk meydana getirme, bunu çaba sonunda sağlama ve karşı taraftan hoşnutluk isteme biçimlerini aynı ettirgen ve isteme alanında toplar. Hazırlanmış çerçeve bu yön değişimini doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"onu kendimden hoşnut ettim"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"onu hoşnut ettim"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"uğraşarak onu hoşnut ettim"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ondan hoşnutluk göstermesini istedim; o da beni hoşnut etti"}],"lexicalization_note":"Tanım, başkasını hoşnut etme çekirdeği ile çaba ve isteme bildiren özel biçimleri ayrı yüzlerde tutar; bunları yalın hoşnut olma anlamına genellemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; temel durum dalı ile gönül alma, yumuşak davranma ve çatışmadan kaçınarak idare etme adayları, sonuç ile yöntem ayrımını en açık biçimde gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal ettirgen veya isteme yönlüdür; komşu dalda hoşnutluğu taşıyan öznenin kendi durumu merkezde kalır.","focus_only":"Başka bir kişide hoşnutluk oluşturma veya ondan hoşnutluk isteme işlemini bildirir.","gloss":"hoşnut etme / hoşnut olma","neighbor_only":"Öznenin kendisinin hoşnut olması ya da bir şeyi kabul etmesi durumunu bildirir.","neighbor_ref":"root_000569/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da hoşnutsuzluğun kalkması ve olumlu kabul alanındadır."},{"boundary_match":"partial","distinction":"Komşu dal yumuşatma ve gönlünü alma davranışlarını sonuçtan bağımsız kapsayabilir; bu dal hoşnutluk sonucunu veya onun açıkça istenmesini merkez alır.","focus_only":"Karşı tarafı gerçekten hoşnut etme sonucunu ve hoşnutluk istemeyi kapsar.","gloss":"hoşnut etme / gönlünü alma","neighbor_only":"İlgi uyandırma, yumuşatma ve gönlünü alma yoluyla birinden iyilik isteme gibi daha geniş kullanımları kapsar.","neighbor_ref":"root_001592/B006","relation_type":"near_synonym","shared_zone":"Bir kişinin olumlu tutumunu kazanma çabasında örtüşürler."},{"boundary_match":"partial","distinction":"Komşu dal bir davranış yöntemini ve yumuşaklığı öne çıkarır; bu dalın çekirdeği hoşnutluğun oluşmasıdır.","focus_only":"Başkasını hoşnut duruma getirme sonucunu bildirir.","gloss":"hoşnut etme / gönlünü hoş tutma","neighbor_only":"İstekte bulunurken kişiyi yumuşaklıkla gözetme ve iyi geçinme yöntemini bildirir.","neighbor_ref":"root_000751/B002","relation_type":"near_synonym","shared_zone":"Karşı tarafın olumsuz tepki vermemesini ve iyi ilişkiyi sağlama alanında örtüşürler."},{"boundary_match":"partial","distinction":"Yumuşak davranma komşusunda amaç zarar veya çatışmadan kaçınmak olabilir; bu dalda belirleyici sonuç karşı tarafın hoşnutluğudur.","focus_only":"Karşı tarafta hoşnutluk oluşturmayı amaç ve sonuç olarak taşır.","gloss":"hoşnut etme / çatışmadan kaçınarak idare etme","neighbor_only":"Çatışmadan korunmak için kişiye yumuşak davranmayı ve onu idare etmeyi taşır.","neighbor_ref":"root_000466/B008","relation_type":"near_neighbor","shared_zone":"Karşı tarafın olumsuz tepkisini azaltmaya yönelik kişiler arası davranış alanında buluşurlar."},{"boundary_match":"partial","distinction":"Yumuşak davranış hoşnutluk doğurmayabilir; bu dal ise davranışın biçiminden çok hoşnutluğu sağlama veya isteme ilişkisini tanımlar.","focus_only":"Hoşnutluk meydana getirme veya isteme sonucuna bağlıdır.","gloss":"hoşnut etme / yumuşak davranma","neighbor_only":"Bir kişiye nazik ve yumuşak davranma biçimine bağlıdır.","neighbor_ref":"root_000485/B006","relation_type":"near_neighbor","shared_zone":"İyi ilişki kurmaya yönelik kişiler arası eylemlerde yakınlaşırlar."}],"source_phrase_ar":"أرضيته عني ورضيته بالتشديد أيضا فرضي وترضيته أرضيته بعد جهد واسترضيته فأرضاني (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, doğrudan hoşnut etme, çabayla hoşnut etme ve hoşnutluk isteme ayrımlarını birlikte verir."}],"source_summary":"Tanıklık, başkasının hoşnutluğunu sağlama ve isteme çevresindeki kullanımları; doğrudan sonuç, çabayla elde edilen sonuç ve istemeye verilen karşılık ayrımlarıyla birlikte sunar.","sources":["SI"],"what_is_ar":"يدخل فيه أرضيته، ورضيته بالتشديد، وترضيته بعد جهد، واسترضيته فأرضاني","what_is_not_ar":"ليس هو رضا النفس ابتداء، ولا التراضي بين طرفين على سواء، ولا رضوان اسما للرضا"},"support_links":["sup_5ff162ef651bc90031ee"]},{"boundary":"Anlam yalnızca verilen karşılıklı eylem kalıbında bir konuda üstün gelmeyi anlatır; genel hoşnutluk, karşılıklı kabul veya her türlü yenme anlamına genişletilemez.","branch_kind":"non_bare","branch_ref":"root_000569/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَّضِىَ","morph_features":"STEM|POS:V|IMPF|LEM:r~aDiYa|ROOT:rDw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:21:2:1","qac_word_ref":"92:21:2","surface_ar":"يَرْضَىٰ"}],"gloss":"karşılıklı çekişmede üstün gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Karşılıklı bir girişim veya çekişme içinde öteki tarafa o konuda üstün gelinir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üstün gelme anlamı yalnızca tanıklanan sözlüksel ifadenin sınırı içinde geçerlidir."}}],"root_ar":"ر ض و","root_id":"root_000569","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca tanıklanan karşılıklı eylem ifadesinin, bir konuda karşı tarafı yenme sonucunu bildirdiği kullanım için uygundur.","boundary_detail":"Anlam yalnızca verilen karşılıklı eylem kalıbında bir konuda üstün gelmeyi anlatır; genel hoşnutluk, karşılıklı kabul veya her türlü yenme anlamına genişletilemez.","branch_image_ar":"راضاني فرضوته غلبة في ذلك","concept_gloss":"karşılıklı çekişmede üstün gelme","contextual_glosses":[{"applicability":"Karşı tarafın aynı alandaki girişimine cevap verilip onun yenildiği belirli ifade bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eylemin karşılıklı kalıba bağlı olduğunu açıkça söylemez.","preserves":"Belirli bir konuda karşı tarafa üstün gelme sonucunu korur."},"facet_ids":["F001","F002"],"text":"o konuda ona üstün geldim","usage_role":"contextual"}],"definition":"Belirli bir karşılıklı çekişme ifadesinde, öteki tarafın girişimine karşı aynı konuda ona üstün gelmektir. Anlam, ifadenin bütününe bağlıdır ve genel hoşnutluk alanından ayrıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Karşılıklı bir girişim veya çekişme içinde öteki tarafa o konuda üstün gelinir."},{"facet_id":"F002","role":"specialization","statement":"Üstün gelme anlamı yalnızca tanıklanan sözlüksel ifadenin sınırı içinde geçerlidir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Olumlu kabul ve iç hoşnutluk durumu ekler.","collision":"Kalıba bağlı üstün gelme anlamını kökün temel hoşnutluk anlamıyla karıştırır.","fit":"displacement","loses":"Karşılıklı çekişmeyi ve öteki tarafa üstün gelme sonucunu bütünüyle kaybeder.","preserves":"Aynı kök ailesiyle biçimsel bağı dışında kurucu anlamı korumaz."},"text":"hoşnut oldum"}],"identity_rationale":"Yetkili ifade, belirli bir karşılıklı eylem kalıbında birinin ötekine üstün gelmesini açıkça bildirir. Bu kullanım hoşnutluk çekirdeğinden değil, kalıbın bütününden doğduğu için ayrı ve sözlüksel olarak sınırlı dal kabul edilmiştir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"karşılıklı çekişmede ona üstün geldim"}],"lexicalization_note":"Tanım, üstün gelme anlamını yalnızca kanıtta verilen sözlüksel kalıba bağlar ve bunu kökün yalın anlamı ya da genel bir yenme fiili olarak sunmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı kullanımı veren tam eşdeğer önce, ardından sözlüksel kalıp, sayı, genel zafer ve güç yarışı sınırlarını gösteren en yakın üstün gelme dalları seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Anlam çekirdeği, katılımcılar ve sözlüksel sınır bakımından ayrım yoktur; iki dal aynı kullanımı temsil eder.","focus_only":null,"gloss":"karşılıklı çekişmede üstün gelme","neighbor_only":null,"neighbor_ref":"root_000570/B002","relation_type":"synonym","shared_zone":"İki kart da aynı sözlüksel ifade içinde aynı konuda karşı tarafa üstün gelmeyi bildirir."},{"boundary_match":"partial","distinction":"Sonuç aynıdır, ancak her anlam kendi tanıklanan sözlüksel ifadesine bağlıdır; bu nedenle ifadeler serbestçe birbirinin yerine geçmez.","focus_only":"Üstün gelmeyi yalnızca bu dala özgü karşılıklı eylem ifadesinde bildirir.","gloss":"çekişmede üstün gelme / karşı koyuşta üstün gelme","neighbor_only":"Üstün gelmeyi karşı koyma ve ayrışma alanına özgü başka bir karşılıklı eylem ifadesinde bildirir.","neighbor_ref":"root_000808/B003","relation_type":"near_synonym","shared_zone":"İki kullanım da karşılıklı bir eylem kalıbında öteki tarafa o konuda üstün gelmeyi anlatır."},{"boundary_match":"partial","distinction":"Komşu dalda sayı çokluğu kurucu araçtır; bu dalda sayı koşulu yoktur, fakat anlam belirli bir ifadeyle sınırlıdır.","focus_only":"Üstün gelmenin aracını veya ölçüsünü belirtmeden belirli bir çekişme kalıbına bağlıdır.","gloss":"çekişmede üstün gelme / sayıca üstün gelme","neighbor_only":"Üstün gelmeyi özellikle sayı çokluğu üzerinden kurar.","neighbor_ref":"root_001286/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da rakip tarafa üstün gelme sonucunu taşır."},{"boundary_match":"partial","distinction":"Komşu genel bir zafer ve yenme alanıdır; bu dalın anlamı tek bir sözlüksel kullanımdan dışarı taşmaz.","focus_only":"Yalnızca tanıklanan karşılıklı ifade içinde bir konuda üstün gelmeyi bildirir.","gloss":"kalıba bağlı üstün gelme / zafer kazanma","neighbor_only":"Zafer kazanma, ele geçirme ve rakibi yenme alanını daha genel biçimde kapsar.","neighbor_ref":"root_000965/B001","relation_type":"near_synonym","shared_zone":"Rakibin yenilmesi ve üstünlüğün elde edilmesi sonucunda örtüşürler."},{"boundary_match":"partial","distinction":"Komşu güç gösterisi ve büyüklük yarışını öne çıkarır; bu dalda böyle bir yöntem yoktur, yalnızca tanıklanan ifade sınırı vardır.","focus_only":"Belirli bir karşılıklı eylem ifadesinde o konuda üstün gelmeye bağlıdır.","gloss":"çekişmede üstün gelme / güç yarışında üstün gelme","neighbor_only":"Rakiple büyüklük ve güç yarışı içindeki karşılıklı üstünlük kurma davranışına bağlıdır.","neighbor_ref":"root_001281/B011","relation_type":"near_synonym","shared_zone":"Karşılıklı mücadelede rakibi aşma sonucunu paylaşırlar."}],"source_phrase_ar":"قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه لأنه من الواو (sihah)","source_summary":"Tanıklıklar aynı karşılıklı eylem ifadesini bir konuda öteki tarafa üstün gelmek diye açıklar; verilen malzeme bu anlamı tanıklanan sözlüksel kalıpla sınırlı tutar.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه قولهم راضاني فلان فرضوته أو أرضوه إذا غلبته فيه","what_is_not_ar":"ليس مطلق الرضا خلاف السخط، ولا المراضاة بمعنى رضا الطرفين"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_000569/B006","candidate_links":[{"candidate_id":"cand_18703bcf347440afcb42","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"رَّضِىَ","morph_features":"STEM|POS:V|IMPF|LEM:r~aDiYa|ROOT:rDw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:21:2:1","qac_word_ref":"92:21:2","surface_ar":"يَرْضَىٰ"}],"gloss":"söz dinleyen, seven veya güvence veren","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"associated_use","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kullanım, buyruğa uyan ve söz dinleyen kişiyi niteler."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İkinci kullanım, sevgi duyan kişiyi niteler."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Üçüncü kullanım, bir yükümlülük için güvence veren kişiyi niteler."}},{"facet_id":"F004","role":"core","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Aynı sıfat biçiminin kanıtta yalnız bu üç kişi niteliğiyle sınırlı olarak kaydedilmesidir."}}],"root_ar":"ر ض و","root_id":"root_000569","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sıfat biçiminin kanıtta buyruğa uyan, sevgi duyan veya yükümlülük için güvence veren kişi anlamlarıyla kullanıldığı yerlerde uygundur.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"الرضي صفة للمطيع أو المحب أو الضامن","concept_gloss":"söz dinleyen, seven veya güvence veren","contextual_glosses":[{"applicability":"Sıfatın buyruğa uyma ve itaat etme anlamında kullanıldığı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Buyruğa uyma ve söz dinleme anlamını korur."},"facet_ids":["F001"],"text":"söz dinleyen","usage_role":"contextual"},{"applicability":"Sıfatın birine sevgi duyan kişiyi anlattığı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin sevgi duyan taraf olmasını korur."},"facet_ids":["F002"],"text":"seven","usage_role":"contextual"},{"applicability":"Sıfatın bir borç veya yükümlülük için güvence üstlenen kişiyi anlattığı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güvence üstlenme ve sorumluluk alma yönünü korur."},"facet_ids":["F003"],"text":"güvence veren","usage_role":"contextual"}],"definition":"Aynı sıfat biçimi, kanıt sınırı içinde üç ayrı kullanım için kaydedilir: buyruğa uyan kişi, seven kişi ve bir yükümlülük için güvence veren kişi. Bu kullanımlar tek bir üretken kök çekirdeği yerine sınırlı bir kayıt alanı oluşturur.","distinctive_facets":[{"facet_id":"F001","role":"associated_use","statement":"Bir kullanım, buyruğa uyan ve söz dinleyen kişiyi niteler."},{"facet_id":"F002","role":"associated_use","statement":"İkinci kullanım, sevgi duyan kişiyi niteler."},{"facet_id":"F003","role":"associated_use","statement":"Üçüncü kullanım, bir yükümlülük için güvence veren kişiyi niteler."},{"facet_id":"F004","role":"core","statement":"Aynı sıfat biçiminin kanıtta yalnız bu üç kişi niteliğiyle sınırlı olarak kaydedilmesidir."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"söz dinleyen; seven; güvence veren"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı sıfat kullanımı ve aynı üç anlamı veren tam eşdeğer komşu seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Anlam çekirdeği, kullanım sınırı ve verilen üç anlam bakımından ayrım yoktur; iki dal aynı sınırlı sıfat kullanımını temsil eder.","focus_only":null,"gloss":"söz dinleyen, seven veya güvence veren","neighbor_only":null,"neighbor_ref":"root_000570/B004","relation_type":"synonym","shared_zone":"İki kart da aynı sıfat biçimini itaat eden, seven veya güvence veren kişi anlamlarıyla sınırlar."}],"source_phrase_ar":"الرضي المطيع والرضي المحب والرضي الضامن (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, biçimi söz dinleyen, seven ve güvence veren kişi için üç ayrı biçimde açıklar."}],"source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["TA"],"what_is_ar":"يدخل فيه الرضي بمعنى المطيع، والرضي بمعنى المحب، والرضي بمعنى الضامن كما نقل التهذيب","what_is_not_ar":"ليس الرضي هنا مجرد مرضي عنه ولا أصل الرضا العام"},"support_links":["sup_ccec50095c07b4e1540f"]},{"boundary":"Dal yalnızca dağ ve kişi adlarını kapsar; hoşnutluk, karşılıklı kabul veya başka kavramsal anlamlar bu özel ad kimliklerine aktarılmaz.","branch_kind":"bare","branch_ref":"root_000569/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَّضِىَ","morph_features":"STEM|POS:V|IMPF|LEM:r~aDiYa|ROOT:rDw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:21:2:1","qac_word_ref":"92:21:2","surface_ar":"يَرْضَىٰ"}],"gloss":"bir dağ adı ve kadın adları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir biçim belirli bir dağın özel adı olarak kullanılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı biçim ve onunla ilişkili başka bir biçim kadın adı olarak kullanılır."}}],"root_ar":"ر ض و","root_id":"root_000569","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Biçimlerin bir coğrafi varlığı veya kişiyi özel ad olarak belirlediği kullanımların toplu karşılığıdır.","boundary_detail":"Dal yalnızca dağ ve kişi adlarını kapsar; hoşnutluk, karşılıklı kabul veya başka kavramsal anlamlar bu özel ad kimliklerine aktarılmaz.","branch_image_ar":"رضوى ورضيا أعلام من المادة","concept_gloss":"bir dağ adı ve kadın adları","contextual_glosses":[{"applicability":"Biçimin belirli bir coğrafi varlığı adlandırdığı kullanım için açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir dağı adlandırma işlevini korur."},"facet_ids":["F001"],"text":"dağın özel adı","usage_role":"explanatory"},{"applicability":"Biçimin bir kişiye verilen özel ad olduğu kullanımlar için açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir kadını özel adla belirleme işlevini korur."},"facet_ids":["F002"],"text":"kadın adı","usage_role":"explanatory"}],"definition":"Aynı biçim ailesinin bir üyesi belirli bir dağın adı ve kadınlara verilen bir ad olarak, başka bir üyesi de kadın adı olarak kullanılır. Bu kullanımlar kavramsal hoşnutluk anlamı değil, adlandırma işlevi taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir biçim belirli bir dağın özel adı olarak kullanılır."},{"facet_id":"F002","role":"source_variant","statement":"Aynı biçim ve onunla ilişkili başka bir biçim kadın adı olarak kullanılır."}],"identity_rationale":"Yetkili ifade, aynı biçim ailesinde bir dağ adını ve kadınlara verilen adları açıkça kaydeder. Bunlar sözlüksel anlamdan türetilmiş açıklamalar değil, özel ad kullanımları olarak tek adlandırma dalında tutulabilir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir dağ adı; bir kadın adı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"o dağın adına bağlılık bildiren biçim"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bir kadın adı"}],"lexicalization_note":"Tanım, kanıtta yalın biçimler olarak verilen özel ad kullanımlarıyla sınırlıdır; adların sözlüksel kök anlamı taşıdığı varsayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı ad kümesini veren tam eşdeğer ile dağ, yer ve kişi adları alanındaki üç karşılaştırma, gönderim kimliği ile ortak adlandırma alanını en açık biçimde ayırdığı için seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Ad kimlikleri ve kullanım sınırları bakımından anlamlı bir fark yoktur; iki dal aynı özel ad kümesini temsil eder.","focus_only":null,"gloss":"aynı dağ ve kadın adları","neighbor_only":null,"neighbor_ref":"root_000570/B003","relation_type":"synonym","shared_zone":"İki kart da aynı dağ adını, ona bağlı biçimi ve aynı kadın adlarını kaydeder."},{"boundary_match":"field_only","distinction":"Özel adlar aynı tür varlığı adlandırsa da gönderimde bulundukları dağlar farklıdır; bu nedenle eşanlamlı değildirler.","focus_only":"Bir dağ adının yanında kadınlara verilen adları da kapsar.","gloss":"dağ ve kadın adları / başka bir dağ adı","neighbor_only":"Yalnızca başka bir belirli dağın adını kapsar.","neighbor_ref":"root_000706/B006","relation_type":"same_field","shared_zone":"Her ikisinde de bir dağın özel adla belirlenmesi söz konusudur."},{"boundary_match":"field_only","distinction":"Adlandırma işlevi ortak olsa da ad biçimleri ve gönderimde bulundukları kişi ya da yerler ayrıdır.","focus_only":"Belirli bir dağ ile kadınlara verilen adları kapsar.","gloss":"dağ ve kadın adları / başka yer ve kişi adları","neighbor_only":"Başka yer, su ve kişi adlarını kapsar.","neighbor_ref":"root_000361/B005","relation_type":"same_field","shared_zone":"Sözlük biçimlerinin kişi veya yer için özel ada dönüşmesi alanını paylaşırlar."},{"boundary_match":"field_only","distinction":"Komşu dalın gönderim alanı ve ad kümesi daha geniş ve bütünüyle başkadır; ortaklık yalnızca özel ad alanındadır.","focus_only":"Tek bir dağ adı ile belirli kadın adlarını sınırlar.","gloss":"dağ ve kadın adları / geniş özel ad kümesi","neighbor_only":"Kişi, yer, soy ve tarihsel olay adlarından oluşan daha geniş bir özel ad kümesini kapsar.","neighbor_ref":"root_000364/B007","relation_type":"same_field","shared_zone":"Her iki dal da kişi ve yerleri sözlüksel biçimlerden aktarılan özel adlarla belirler."}],"source_phrase_ar":"رضوى جبل (maqayis;ayn;sihah)؛ ومن أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)","source_summary":"Tanıklıklar dağ adını ortak biçimde kaydeder; toplu ifade ayrıca aynı biçimin ve ilgili başka bir biçimin kadınlara verilen adlar arasında bulunduğunu belirtir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه رضوى اسم جبل، ورضيا ورضوى في أسماء النساء كما ورد في التهذيب","what_is_not_ar":"ليس استعمالا معنويا للرضا أو الرضوان أو التراضي"},"support_links":[]},{"boundary":"Bu dal yarışta üstün gelme kalıbını, özel adları ve aynı biçimdeki buyruğa uyma, sevme ya da güvence verme anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000570/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَّضِىَ","morph_features":"STEM|POS:V|IMPF|LEM:r~aDiYa|ROOT:rDw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:21:2:1","qac_word_ref":"92:21:2","surface_ar":"يَرْضَىٰ"}],"gloss":"hoşnut olup uygun bulma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kimseye, şeye veya duruma karşı kızgınlık ve hoşnutsuzluk duymamak, onu gönle uygun bulmak."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyi beğenip benimsemek veya seçenekler arasından uygun bulmak."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ad biçimleri genel hoşnutluğu, kimi kayıtta ise çok güçlü hoşnutluğu bildirir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Edilgen biçimler, uygun bulunan ya da kendisinden hoşnut olunan kimseyi veya şeyi gösterir."}}],"root_ar":"ر ض و","root_id":"root_000570","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duygusal hoşnutluk ile bilinçli benimsemenin birlikte bulunduğu genel çekirdek için kullanılır.","boundary_detail":"Bu dal yarışta üstün gelme kalıbını, özel adları ve aynı biçimdeki buyruğa uyma, sevme ya da güvence verme anlamlarını kapsamaz.","branch_image_ar":"الرِّضا خلاف السخط والقبول","concept_gloss":"hoşnut olup uygun bulma","contextual_glosses":[{"applicability":"Bir kimse, durum veya sonuç karşısındaki olumlu gönül durumunun öne çıktığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gönle aykırı bulmama ve hoşnutluk çekirdeğini korur."},"facet_ids":["F001"],"text":"hoşnut olma","usage_role":"general"},{"applicability":"Bir şeyi değerlendirip beğenme, benimseme veya seçme bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Değerlendirme sonunda benimseme ve seçme yönünü korur."},"facet_ids":["F002"],"text":"uygun bulma","usage_role":"contextual"},{"applicability":"Bir kimsenin veya şeyin başkası tarafından uygun bulunmuş olduğunu anlatan edilgen bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uygun bulunan varlığın edilgen konumunu korur."},"facet_ids":["F004"],"text":"beğenilmiş olma","usage_role":"contextual"},{"applicability":"Kaydın özellikle yüksek derece bildirdiği ad biçiminin açıklanmasında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hoşnutluğun olağandan yüksek derecesini korur."},"facet_ids":["F003"],"text":"derin hoşnutluk","usage_role":"explanatory"}],"definition":"Bir kimseyi, şeyi veya durumu gönle aykırı görmeyip uygun bulma ve ondan hoşnut olma durumudur. Ad ve edilgen biçimleri genel ya da güçlü hoşnutluğu ve uygun bulunan varlığı anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kimseye, şeye veya duruma karşı kızgınlık ve hoşnutsuzluk duymamak, onu gönle uygun bulmak."},{"facet_id":"F002","role":"extension","statement":"Bir şeyi beğenip benimsemek veya seçenekler arasından uygun bulmak."},{"facet_id":"F003","role":"source_variant","statement":"Ad biçimleri genel hoşnutluğu, kimi kayıtta ise çok güçlü hoşnutluğu bildirir."},{"facet_id":"F004","role":"source_variant","statement":"Edilgen biçimler, uygun bulunan ya da kendisinden hoşnut olunan kimseyi veya şeyi gösterir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kızgınlığın karşıtı olan gönül durumunu ve benimsemenin sürekliliğini eksiltir.","preserves":"Bir şeyi olumlu değerlendirme yönünü korur."},"text":"beğenme"},{"category":"confusable","error_profile":{"adds":"Belirgin bir neşe ve coşku olayı çağrıştırır.","collision":"Sevinme olayını, daha durgun bir hoşnutluk ve benimseme durumuyla karıştırır.","fit":"displacement","loses":"Bir kimseyi veya şeyi uygun bulup benimseme değerlendirmesini yitirir.","preserves":"Olumlu bir iç yaşantı bulunmasını korur."},"text":"sevinç"},{"category":"confusable","error_profile":{"adds":"İstek dışı uyma veya güç karşısında geri çekilme anlamı ekler.","collision":"Gönüllü benimsemeyi zorunlu uyma davranışıyla karıştırır.","fit":"displacement","loses":"İçten uygun bulma ve hoşnutluk çekirdeğini yitirir.","preserves":"Bir duruma açıkça karşı çıkmama görünümünü korur."},"text":"boyun eğme"}],"identity_rationale":"Kaynakların ortak çekirdeği, kızgınlık ve hoşnutsuzluğun karşısında bir kimseyi, şeyi ya da durumu gönle uygun bulup benimsemedir. Ad biçimleri hoşnutluk durumunu, edilgen biçimler ise uygun bulunan veya kendisinden hoşnut olunan varlığı gösterir; kimi kayıtlar hoşnutluğun yoğunluğunu ayrıca belirtir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"hoşnut olmak; gönlüne uygun bulmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"hoşnut olan"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"beğenilmiş, uygun bulunmuş"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kendisinden hoşnut olunan"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"uygun bulunmuş; eski kök yapısını koruyan biçim"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kendisinden hoşnut olunan adam; eski kök yapısını koruyan söyleyiş"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"hoşnutluk; hoşnutsuzluğun karşıtı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"hoşnutluğu bildiren uzatılmış ad biçimi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"hoşnutluk; çok güçlü hoşnutluk"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"hoşnutluk bildiren ad"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"iki tarafın birbirini uygun bulması"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"birbirini uygun bulma ve karşılıklı anlaşma"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"şeyi beğenip uygun buldum"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"onu beğenip seçtim"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ondan hoşnut oldum"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"onu arkadaş olarak uygun buldum"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ondan ya da onunla olmaktan hoşnut oldum"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"beğenilen, hoşnutluk veren yaşayış"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"onu benden hoşnut ettim"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"onu hoşnut ettim"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"uğraştıktan sonra onu hoşnut ettim"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"onun gönlünü yapmaya çalıştım, sonunda benden hoşnut oldu"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"birbirlerini uygun bulup anlaştılar"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"Tanrı'nın kulunu buyruklarına uyar ve yasaklarından kaçınır görmesi"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"beğenilmiş, uygun bulunmuş"}],"lexicalization_note":"Çekirdek yalın hoşnutluk ve benimsemedir; nesne, ilgeç, karşılıklılık, ettirme veya isteme içeren birimler yalnızca kendi yapılarında tanıklanan anlamı taşır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; karşılıklı anlaşma, yüz çevirme, hayranlık ve aynı kökün yarışta üstün gelme, özel ad ve eşsesli sıfat dalları, seçilen beş ayrımın ötesinde çekirdeği daha iyi açıklamadığı veya gereksiz tekrar oluşturduğu için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdek anlam örtüşür; odak dal komşu kartta bulunmayan karşılıklılık, ettirme, hoşnutluğu isteme ve ilgeçli kalıpları da kapsadığı için sınırlar tam olarak aynı değildir.","focus_only":"Karşılıklılık, ettirme, hoşnutluğu isteme ve çeşitli ilgeçli kalıpları da kapsayan daha geniş yapı alanı.","gloss":"hoşnutluk ve benimsemenin ortak çekirdeği","neighbor_only":null,"neighbor_ref":"root_000569/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da hoşnutsuzluğun karşıtını, uygun bulmayı ve temel etkin-edilgen biçimleri kapsar."},{"boundary_match":"partial","distinction":"Odak dal içsel hoşnutluk ve uygun bulmayı çekirdek yapar; komşu dal ise hoşnutluk şartı bulunmadan bir şeyi alma veya geçerli sayma eylemini de kapsar.","focus_only":"Gönülde hoşnutsuzluk bulunmaması ve kişiye ya da duruma yönelik içsel uygunluk.","gloss":"hoşnutlukla benimseme ile bir şeyi alma","neighbor_only":"Özür, armağan, iş veya benzeri bir şeyi teslim alıp geçerli saymaya uzanan daha geniş alma alanı.","neighbor_ref":"root_001198/B004","relation_type":"near_synonym","shared_zone":"Her ikisi de bir şeyi geri çevirmeyip uygun bulma ve benimseme alanında kesişir."},{"boundary_match":"opposed","distinction":"Odak dal olumlu gönül uygunluğunu ve benimsemeyi, komşu dal ise kızgınlıkla birleşebilen olumsuz değerlendirme ve istememeyi bildirir.","focus_only":"Gönle uygun bulma, hoşnut olma ve benimseme.","gloss":"hoşnutluk ile hoşnutsuzluk karşıtlığı","neighbor_only":"Kızma, hoşnutsuz olma, bir şeyi istemeyip geri çevirme.","neighbor_ref":"root_000686/B001","relation_type":"antonym","shared_zone":"İki dal aynı kişi, şey veya durum karşısındaki değerlendirme ekseninin karşı uçlarını gösterir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeğinde bir nesne veya durumu uygun bulma vardır; komşu dal değerlendirme gerektirmeden haz, neşe veya rahatlık yaşantısını öne çıkarır.","focus_only":"Bir kimseyi, şeyi veya durumu uygun bulup benimseme değerlendirmesi.","gloss":"hoşnutluk ile haz duyma","neighbor_only":"Haz, neşe, rahatlık ve içinde bulunulan nimetlerden tat alma.","neighbor_ref":"root_001174/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de olumlu ve gönle iyi gelen bir iç durumu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal uygun bulma ve benimsemeyle sınırlı kalabilir; komşu dal ise daha kalıcı sevgi ve bağlılığı çekirdek yapar.","focus_only":"Uygun bulma ve hoşnutsuzluk taşımama, kalıcı duygusal bağ gerektirmez.","gloss":"hoşnutluk ile sevgi","neighbor_only":"Kişi veya şeye yerleşik sevgi, bağlılık ve karşılıklı yakınlık.","neighbor_ref":"root_000286/B002","relation_type":"near_neighbor","shared_zone":"İki dal bir kimseye veya şeye olumlu yöneliş bildirebilir."}],"source_phrase_ar":"أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضوان من الرضا (ayn)؛ الرضوان الرضا والمرضاة مثله ورضيت الشيء وارتضيته (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو والرضوان الرضا الكثير (mufradat)","source_summary":"Kaynaklar anlamı hoşnutsuzluğun karşıtı olan gönül uygunluğu ve benimseme çevresinde birleştirir. Aynı toplu tanıklık, ad biçimlerinin genel veya yoğun hoşnutluğu, edilgen biçimlerin de uygun bulunan varlığı gösterebildiğini aktarır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الرضا والرضوان والمرضاة ورضي عن الشيء أو به أو عليه وارتضاه وأرضاه واسترضاه وترضاه والتراضي والمراضاة إذا كان المعنى إظهار القبول أو حصوله","what_is_not_ar":"ليس غلبة راضاني فرضوته ولا رضوى علما ولا الرَّضِيّ بمعانيه المفردة عند ابن الأعرابي"},"support_links":[]},{"boundary":"Anlam yalnızca tanıklanan çekişme ve ardından üstün gelme kalıbına bağlıdır; hoşnutluk, karşılıklı anlaşma veya genel güç kullanımı değildir.","branch_kind":"non_bare","branch_ref":"root_000570/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَّضِىَ","morph_features":"STEM|POS:V|IMPF|LEM:r~aDiYa|ROOT:rDw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:21:2:1","qac_word_ref":"92:21:2","surface_ar":"يَرْضَىٰ"}],"gloss":"çekişmede alt etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Karşı tarafın giriştiği çekişmede onu yenip üstün gelmek."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yenme anlamı, iki taraflı çekişmeyi ve sonucu birlikte bildiren özel söz dizisi içinde kurulur."}}],"root_ar":"ر ض و","root_id":"root_000570","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca birinin kendisiyle çekişen kişiyi aynı işte yendiğini bildiren özel kullanım için uygundur.","boundary_detail":"Anlam yalnızca tanıklanan çekişme ve ardından üstün gelme kalıbına bağlıdır; hoşnutluk, karşılıklı anlaşma veya genel güç kullanımı değildir.","branch_image_ar":"غلبة راضاني فرضوته","concept_gloss":"çekişmede alt etme","contextual_glosses":[{"applicability":"Karşılıklı yarışma görünümünün belirgin olduğu ve taraflardan birinin kazandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki taraflı yarışmayı ve yenme sonucunu korur."},"facet_ids":["F001","F002"],"text":"yarışta yenme","usage_role":"contextual"},{"applicability":"Yarışın türü belirtilmediğinde kalıbın sonuç yönünü açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir karşılaşmada öteki tarafı geçme sonucunu korur."},"facet_ids":["F001","F002"],"text":"karşılaşmada üstün gelme","usage_role":"explanatory"}],"definition":"Belirli bir karşılaşmada kendisiyle çekişen kişiyi o işte alt etmeyi anlatan kalıplaşmış kullanımdır. Genel hoşnutluk veya genel zorlama anlamına genişletilemez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Karşı tarafın giriştiği çekişmede onu yenip üstün gelmek."},{"facet_id":"F002","role":"specialization","statement":"Yenme anlamı, iki taraflı çekişmeyi ve sonucu birlikte bildiren özel söz dizisi içinde kurulur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bir başkasının gönül durumunu olumluya çevirme anlamı ekler.","collision":"Bu özel yenme kalıbını kökün hoşnutluk dalıyla karıştırır.","fit":"displacement","loses":"Çekişme ilişkisini ve karşı tarafı yenme sonucunu bütünüyle yitirir.","preserves":"Aynı kökün başka kullanımlarını yüzeysel olarak çağrıştırır."},"text":"hoşnut etme"},{"category":"alternative","error_profile":{"adds":"Çatışmanın karşılıklı uzlaşmayla sona ermesi anlamını ekler.","collision":"Yarışta üstün gelmeyi karşılıklı anlaşmayla karıştırır.","fit":"displacement","loses":"Bir tarafın ötekini yenmesi sonucunu yitirir.","preserves":"İki tarafın aynı olayda yer almasını korur."},"text":"barışma"},{"category":"alternative","error_profile":{"adds":"Yarışma olmadan güç, tehdit veya sürekli zorlama uygulanmasını da kapsar.","collision":"Belirli çekişmede yenme ile genel zorlayıcı egemenliği karıştırabilir.","fit":"broadening","loses":null,"preserves":"Bir tarafın ötekine üstün gelmesi yönünü korur."},"text":"baskı kurma"}],"identity_rationale":"Kaynak ifadesi genel bir üstünlük kökü değil, bir kişinin belirli bir işte kendisiyle çekişen kişiyi yenmesini bildiren kalıplaşmış bir söz dizisini verir. Geçici dal çerçevesi bu yapısal sınırı ve yenme sonucunu doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"o benimle çekişti, ben de onu o işte yendim"}],"lexicalization_note":"Bu dal yalın bir kök anlamı sayılmaz; karşı tarafın yarışmaya giriştiğini ve konuşanın onu aynı işte yendiğini bildiren tanıklı söz dizisiyle sınırlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; karşılık verme yarışına, genel kişi yenmeye, genel üstünlük ve tartışmada bastırmaya ayrılan adaylar seçilen ayrımlarla yinelendi, aynı kökün hoşnutluk, özel ad ve sıfat dalları ise bu kalıbın anlam sınırını keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sunulan kartlarda yapı, katılımcılar ve sonuç bakımından hiçbir sınır farkı yoktur; dallar tam karşılık olarak değerlendirilebilir.","focus_only":null,"gloss":"aynı kalıpta çekişeni yenme","neighbor_only":null,"neighbor_ref":"root_000569/B005","relation_type":"synonym","shared_zone":"Her iki dal da aynı söz dizisini ve çekişen kişiyi o işte yenme sonucunu verir."},{"boundary_match":"partial","distinction":"Sonuç çekirdeği örtüşür, ancak her dal yenme anlamını kendi kalıplaşmış fiil yapısına bağlar; bu nedenle yalın biçimler arasında genel bir eşitlik kurulamaz.","focus_only":"Yalnızca odak köke ait tanıklı çekişme kalıbı.","gloss":"aynı işte yarışıp yenme","neighbor_only":"Karşılıklı girişme veya bir işi ele alma eylemini kendi söz kalıbıyla kurma.","neighbor_ref":"root_001028/B007","relation_type":"near_synonym","shared_zone":"İki dal da karşılıklı girişilen bir işte taraflardan birinin ötekini yenmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal çekişmenin türünü açık bırakır; komşu dal karşı çıkma ve zıtlaşma alanını kendi yapısının parçası yapar.","focus_only":"Çekişmenin türünü ayrıca adlandırmayan özel yenme kalıbı.","gloss":"çekişmede üstün gelme","neighbor_only":"Karşı çıkma ve zıtlaşma biçimindeki çekişmeye bağlı özel yenme kalıbı.","neighbor_ref":"root_000808/B003","relation_type":"near_synonym","shared_zone":"Her ikisi de iki taraflı bir çekişmede karşı tarafı yenme sonucunu bildirir."},{"boundary_match":"partial","distinction":"Odak dal iki taraflı çekişme kalıbına bağlı tekil sonucu anlatır; komşu dal güçle bastırma ve egemenlik dahil daha geniş bir üstünlük alanını kapsar.","focus_only":"Belirli bir söz dizisinde, kendisiyle çekişen kişiyi o işte yenme.","gloss":"özel yarış zaferi ile genel üstünlük","neighbor_only":"Genel güç, zorlama, egemenlik kurma ve çeşitli alanlarda üstünlük.","neighbor_ref":"root_001098/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir tarafın ötekini geçmesi veya yenmesi sonucu bulunur."},{"boundary_match":"field_only","distinction":"Odak dal sonuç olarak yenmeyi zorunlu kılar; komşu dal yarışma ve boy ölçüşme sürecini, bir kazanan bulunmasa da anlatabilir.","focus_only":"Çekişmenin kazananını ve öteki tarafın yenildiğini bildirir.","gloss":"yarışma ile yarışta kazanma","neighbor_only":"Yarışma, boy ölçüşme veya karşılaştırılma sürecini sonuç belirtmeden anlatabilir.","neighbor_ref":"root_000745/B007","relation_type":"same_field","shared_zone":"İki dal da kişilerin birbirleriyle yarıştığı veya boy ölçüştüğü alana aittir."}],"source_phrase_ar":"قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه (sihah)","source_summary":"Tanıklıklar aynı kalıplaşmış söz dizisini, bir kişinin kendisiyle çekişen ötekini o işte yenmesi anlamında birleştirir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه قولهم راضاني فلان فرضوته أو أرضوه إذا غلبته في الأمر","what_is_not_ar":"ليس المراضاة بمعنى التراضي والقبول المتبادل ولا الرضا خلاف السخط"},"support_links":[]},{"boundary":"Bu dal genel hoşnutluk veya üstün gelme anlamı taşımaz; yalnız tanıklanan dağ adı, kadın adı ve dağla ilişki bildiren biçimlerle sınırlıdır.","branch_kind":"bare","branch_ref":"root_000570/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَّضِىَ","morph_features":"STEM|POS:V|IMPF|LEM:r~aDiYa|ROOT:rDw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:21:2:1","qac_word_ref":"92:21:2","surface_ar":"يَرْضَىٰ"}],"gloss":"dağ ve kadın adı ailesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir dağın özel adı olarak kullanılan biçim."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı kökten bir biçimin kadın adı olarak kullanılması ve küçültülmemiş karşılığının da aktarılması."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dağ adından türetilen sıfatın o dağla ilişki veya köken bildirmesi."}}],"root_ar":"ر ض و","root_id":"root_000570","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tanıklanan dağ adını, kadın adını ve dağ adına bağlı ilişki biçimini yüzey adlarını üretmeden birlikte açıklamak için kullanılır.","boundary_detail":"Bu dal genel hoşnutluk veya üstün gelme anlamı taşımaz; yalnız tanıklanan dağ adı, kadın adı ve dağla ilişki bildiren biçimlerle sınırlıdır.","branch_image_ar":"رضوى ورضيا أسماء","concept_gloss":"dağ ve kadın adı ailesi","contextual_glosses":[{"applicability":"Biçim bir coğrafi yükseltinin kendine özgü adı olarak kullanıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dağ adı olma işlevini eksiksiz korur."},"facet_ids":["F001"],"text":"bir dağın özel adı","usage_role":"contextual"},{"applicability":"Aynı kökten biçim bir kadını adlandırdığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadın adı olma işlevini eksiksiz korur."},"facet_ids":["F002"],"text":"bir kadın adı","usage_role":"contextual"},{"applicability":"Dağ adına bağlı türemiş sıfatın ilişki veya köken bildirdiği bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli dağa bağlılık ve ilişki yönünü korur."},"facet_ids":["F003"],"text":"o dağla ilgili","usage_role":"explanatory"}],"definition":"Bir dağın adı olarak kullanılan biçim ile aynı kökten bir kadın adı ve bunlara bağlı adlandırma ailesidir. Dağ adından türeyen biçim, o dağla ilişkiyi bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir dağın özel adı olarak kullanılan biçim."},{"facet_id":"F002","role":"source_variant","statement":"Aynı kökten bir biçimin kadın adı olarak kullanılması ve küçültülmemiş karşılığının da aktarılması."},{"facet_id":"F003","role":"extension","statement":"Dağ adından türetilen sıfatın o dağla ilişki veya köken bildirmesi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bir gönül durumu ve değerlendirme anlamı ekler.","collision":"Adlandırma dalını kökün genel hoşnutluk dalıyla karıştırır.","fit":"displacement","loses":"Özel ad ve ada bağlı ilişki işlevlerinin tümünü yitirir.","preserves":"Yalnızca aynı kökle yüzeysel bağı korur."},"text":"hoşnutluk"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kadın adı kullanımını ve dağa bağlı türemiş ilişki biçimini eksiltir.","preserves":"Dağın özel adla anılması yönünü korur."},"text":"yer adı"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dağ adını ve o dağla ilişki bildiren türemiş biçimi eksiltir.","preserves":"Kadını adlandırma işlevini korur."},"text":"kadın adı"}],"identity_rationale":"Kaynak ifadesi bir dağ adını, o dağla ilişki bildiren türemiş biçimi ve aynı kökten kadın adlarını birlikte tanıklar. Geçici çerçeve bunları ortak bir sözlük anlamı gibi birleştirmeden, adlandırma ailesi olarak doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bir dağın ve bir kadının adı"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"söz konusu dağla ilgili veya o dağdan olan"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bir kadın adı"}],"lexicalization_note":"Mekanik sınıf yalındır; ancak tanıklıklar özel ad ve addan türeyen ilişki biçimleridir, bu yüzden bunlardan genel bir yalın kök anlamı çıkarılamaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öteki yer ve kişi adı aileleri seçilen aynı-alan örneklerini yineledi, aynı kökün hoşnutluk, yarışta üstün gelme ve eşsesli sıfat dalları ise adlandırma çekirdeğiyle anlam ilişkisi kurmadığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Adlandırma çekirdeği örtüşür; odak dal verilen kanıtta dağ adına bağlı türemiş ilişki biçimini ayrıca içerdiği için sınırı biraz daha geniştir.","focus_only":"Dağ adına bağlı ilişki veya köken bildiren türemiş sıfatın açıkça kapsanması.","gloss":"aynı dağ ve kadın adları","neighbor_only":null,"neighbor_ref":"root_000569/B007","relation_type":"near_synonym","shared_zone":"İki dal da aynı kökten gelen dağ ve kadın adlarını kapsar."},{"boundary_match":"field_only","distinction":"Ortaklık yalnızca adlandırma düzenindedir; hangi kişi ve yerleri adlandırdıkları ile türemiş biçimlerin dayandığı özel adlar bütünüyle ayrıdır.","focus_only":"Belirli bir dağ adı, kadın adı ve dağa bağlı ilişki sıfatından oluşan aile.","gloss":"kişi ve yer adları","neighbor_only":"Bir kadın adıyla birlikte ülke, köy ve başka yer adları ile bunlara bağlı ilişki biçimleri.","neighbor_ref":"root_001697/B005","relation_type":"same_field","shared_zone":"Her iki dal da aynı sözcük ailesinden kişi ve yer adları ile ada bağlı biçimler üretir."},{"boundary_match":"field_only","distinction":"Ad olma işlevi ortaktır, fakat adların taşıyıcıları ve bağlı oldukları söz ailesi ayrıdır; anlam bakımından birbirlerinin yerine geçmezler.","focus_only":"Bir dağ ve kadın adlarıyla sınırlı belirli adlandırma ailesi.","gloss":"sözden türeyen özel adlar","neighbor_only":"Çeşitli kişi ve yer adlarını başka bir söz ailesi altında toplayan daha geniş ad dizisi.","neighbor_ref":"root_000943/B007","relation_type":"same_field","shared_zone":"İki dal da bir söz biçiminin kişi veya yer adı olarak kullanılmasını kaydeder."},{"boundary_match":"field_only","distinction":"Odak dal adlandırma ailesi ve türemiş ilişki biçimi kurar; komşu dal ise başka bir biçimin yer veya erkek adı olmasını tanıklar.","focus_only":"Dağ ve kadın adı ile dağa bağlı ilişki biçiminin birlikte bulunması.","gloss":"yer ve kişi adı kullanımı","neighbor_only":"Tek bir biçimin yer veya erkek adı olarak kullanılması.","neighbor_ref":"root_001013/B004","relation_type":"same_field","shared_zone":"Her iki dalda da sözlükteki biçim bir yerin veya kişinin özel adı olur."},{"boundary_match":"field_only","distinction":"Odak dal kadın adı kullanımının yanında dağ adını ve ona bağlı ilişki biçimini taşır; komşu dalın ortaklığı yalnız kadın adı olma işlevindedir.","focus_only":"Dağ adı, kadın adı ve dağa bağlı türemiş sıfat.","gloss":"kadın adı kullanımı","neighbor_only":"Yalnızca başka bir kadın adı olarak kaydedilen biçim.","neighbor_ref":"root_000848/B009","relation_type":"same_field","shared_zone":"Her iki dal bir söz biçiminin kadın adı olarak kullanılmasını içerir."}],"source_phrase_ar":"رضوى جبل (maqayis;ayn)؛ رضوى جبل بالمدينة والنسبة إليه رضوى (sihah)؛ من أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)","source_summary":"Toplu tanıklık bir dağ adında birleşir; ayrıca dağla ilişki bildiren türemiş biçimi ve aynı kökten kadın adlarını kaydeder. Bu kullanımlar genel bir nitelik değil, adlandırma ve ada bağlı ilişki alanı oluşturur.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه رضوى علما للجبل وما يلحق به من النسبة إليه ورضيا اسما للنساء وتكبيره رضوى","what_is_not_ar":"ليس الرضا مصدرا ولا الرضوان ولا غلبة راضاني"},"support_links":[]},{"boundary":"Üç anlam birbirine karıştırılmaz: buyruğa uyma davranışı, sevgi yönelimi ve güvence üstlenme ayrı bağlamsal seçeneklerdir; beğenilmiş olma anlamı bu dala girmez.","branch_kind":"bare","branch_ref":"root_000570/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَّضِىَ","morph_features":"STEM|POS:V|IMPF|LEM:r~aDiYa|ROOT:rDw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:21:2:1","qac_word_ref":"92:21:2","surface_ar":"يَرْضَىٰ"}],"gloss":"buyruğa uyan, seven veya güvence veren","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Aynı sıfat biçiminin ortak bir anlamda birleşmeyen üç seçenekli okumaya sahip olması."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Buyruğa uyan ve kendisinden isteneni yerine getiren kişi."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kimseyi veya şeyi seven kişi."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir yükümlülük için güvence veren veya sorumluluğu üstlenen kişi."}}],"root_ar":"ر ض و","root_id":"root_000570","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Biçimin üç tanıklı okumasını birlikte listeler; gerçek bağlamda bunlardan yalnız uygun olanı seçilmelidir.","boundary_detail":"Üç anlam birbirine karıştırılmaz: buyruğa uyma davranışı, sevgi yönelimi ve güvence üstlenme ayrı bağlamsal seçeneklerdir; beğenilmiş olma anlamı bu dala girmez.","branch_image_ar":"الرَّضِيّ طاعة ومحبة وضمان","concept_gloss":"buyruğa uyan, seven veya güvence veren","contextual_glosses":[{"applicability":"Bir kişinin verilen buyruğu yerine getirmesi veya istenen davranışı göstermesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Buyruğa uyma ve isteneni yerine getirme yönünü korur."},"facet_ids":["F002"],"text":"buyruğa uyan","usage_role":"contextual"},{"applicability":"Sıfatın bir kimseye veya şeye sevgi duyan kişiyi gösterdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sevgi yönelimini doğrudan ve eksiksiz korur."},"facet_ids":["F003"],"text":"seven","usage_role":"contextual"},{"applicability":"Bir kişinin başkasının yükümlülüğü için sorumluluk üstlendiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yükümlülüğe güvence olma ve sorumluluk üstlenme yönünü korur."},"facet_ids":["F004"],"text":"güvence veren","usage_role":"contextual"}],"definition":"Tek bir sıfat biçiminin bağlama göre buyruğa uyan, seven veya bir yükümlülüğe güvence veren kişiyi göstermesidir. Bu üç okuma seçeneklidir ve aynı kullanımda birlikte varsayılmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Aynı sıfat biçiminin ortak bir anlamda birleşmeyen üç seçenekli okumaya sahip olması."},{"facet_id":"F002","role":"source_variant","statement":"Buyruğa uyan ve kendisinden isteneni yerine getiren kişi."},{"facet_id":"F003","role":"source_variant","statement":"Bir kimseyi veya şeyi seven kişi."},{"facet_id":"F004","role":"source_variant","statement":"Bir yükümlülük için güvence veren veya sorumluluğu üstlenen kişi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Başkasının olumlu değerlendirmesine uğramış olma anlamı ekler.","collision":"Bu üçlü sıfat dalını edilgen biçimde uygun bulunma dalıyla karıştırır.","fit":"displacement","loses":"Buyruğa uyma, sevme ve güvence verme okumalarının tümünü yitirir.","preserves":"Aynı yazılı biçimin başka dalda görülen yüzeyini çağrıştırır."},"text":"beğenilmiş"},{"category":"confusable","error_profile":{"adds":"Kişinin kendi gönül durumuna ilişkin hoşnutluk anlamı ekler.","collision":"Eşsesli sıfatı kökün genel hoşnutluk dalıyla karıştırır.","fit":"displacement","loses":"Tanıklanan buyruğa uyma, sevme ve güvence verme seçeneklerini yitirir.","preserves":"Olumlu bir kişi niteliği izlenimini korur."},"text":"hoşnut olan"},{"category":"alternative","error_profile":{"adds":"Genel dürüstlük, sağlamlık ve sözünde durma gibi tanıklanmayan kişilik özelliklerini ekler.","collision":"Belirli bir yükümlülüğü üstlenmeyi genel güvenilirlikle karıştırır.","fit":"broadening","loses":null,"preserves":"Güvence veren kişiye duyulan güven yönünü kısmen korur."},"text":"güvenilir"}],"identity_rationale":"Kaynak tanıklığı aynı sıfat biçimine buyruğa uyan, seven ve bir yükümlülüğe güvence veren kişi anlamlarını yükler. Geçici çerçeve ancak bunlar tek bir birleşik kişilik niteliği değil, bağlama göre seçilen üç ayrı okuma olarak tutulursa geçerlidir.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"buyruğa uyan, seven ya da güvence veren"}],"lexicalization_note":"Mekanik sınıf yalındır; sıfat, herhangi bir ek söz kalıbına bağlı olmadan üç ayrı anlamdan birini taşır, fakat bu anlamlar ortak bir çekirdekte birleştirilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sevgiye ayrılan ikinci aday, yükümlülük ve güvenceye yakın adaylar ile ihanet ve söz bozma alanları seçilen ayrımları yineledi veya yalnız dolaylı karşıtlık kurdu, aynı kökün diğer üç dalı da eşseslilik dışında anlam sınırını açıklamadı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sunulan kartlarda anlam seçenekleri ve sınırlar bütünüyle aynıdır; dallar arasında ayırıcı bir içerik bulunmaz.","focus_only":null,"gloss":"aynı üç seçenekli sıfat","neighbor_only":null,"neighbor_ref":"root_000569/B006","relation_type":"synonym","shared_zone":"Her iki dal da aynı sıfatı buyruğa uyan, seven veya güvence veren kişi anlamlarıyla verir."},{"boundary_match":"partial","distinction":"Odaktaki uyma yalnız üç seçenekten biridir ve zorunlu olarak dinsel değildir; komşu dal dinsel boyun eğme ve doğru yolda kalmayı çekirdek yapar.","focus_only":"Buyruğa uyma yanında sevme ve güvence verme seçeneklerini de taşıyan eşsesli sıfat.","gloss":"buyruğa uyma ile dinsel boyun eğme","neighbor_only":"Din yolunda boyun eğme, doğru yolda kalma ve belirli toplumsal uyma ilişkileri.","neighbor_ref":"root_001260/B001","relation_type":"near_synonym","shared_zone":"Odak sıfatın bir okuması ile komşu dal, istenen buyruğa uyma davranışında kesişir."},{"boundary_match":"partial","distinction":"Odak dal sevgiyi yalnız sıfatın seçenekli bir okuması olarak verir; komşu dal sevgi ve karşılıklı yakınlığı bağımsız, geniş bir anlam alanı olarak kurar.","focus_only":"Sevmenin yanı sıra buyruğa uyma ve güvence verme okumalarını da taşıyan tek sıfat.","gloss":"seven kişi ile sevgi alanı","neighbor_only":"Sevgi, yakınlık, karşılıklı sevme ve sevginin oluşma yollarından meydana gelen geniş alan.","neighbor_ref":"root_001634/B001","relation_type":"near_synonym","shared_zone":"Odak sıfatın bir okuması, bir kimseye veya şeye sevgi duyan kişiyi gösterir."},{"boundary_match":"partial","distinction":"Odak dal yalnız sorumluluğu üstlenen kişiyi niteleyen seçenekli bir sıfat verir; komşu dal güvence kurumunu ve üstlenilen mali ya da hukuki yükü kapsar.","focus_only":"Güvence veren kişi okumasını, iki başka eşsesli okumayla aynı sıfatta taşıması.","gloss":"güvence veren kişi ile güvence yükümlülüğü","neighbor_only":"Borç, ödeme veya başka bir hakkı üstlenmeye ilişkin güvence ve yükümlülük düzeni.","neighbor_ref":"root_000357/B004","relation_type":"near_synonym","shared_zone":"Odak sıfatın bir okuması ile komşu dal, başkasının yükümlülüğü için sorumluluk üstlenmede kesişir."}],"source_phrase_ar":"الرَّضِيّ المطيع؛ الرَّضِيّ المحب؛ الرَّضِيّ الضامن (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık sıfatı, birbirinden ayrı biçimde buyruğa uyan, seven veya bir yükümlülüğe güvence veren kişi için kullanır."}],"source_summary":"Birden çok kaynağın ortaklaştırdığı bir anlam yoktur; veri, aynı sıfat için üç ayrı okuma veren tek bir tanıklığa dayanır.","sources":["TA"],"what_is_ar":"يدخل فيه الرَّضِيّ إذا استعمل بمعنى المطيع أو المحب أو الضامن كما حكاه ابن الأعرابي","what_is_not_ar":"ليس الرَّضِيّ بمعنى المرضي ولا الرضا مصدرا عاما ولا رضوانا"},"support_links":[]},{"boundary":"This branch covers blessing, favor, bounty, good condition, pleasant living, and benefaction given to another.","branch_kind":null,"branch_ref":"root_001525/B001","candidate_links":[{"candidate_id":"cand_9641fb3c7d43ca2d5618","lane":"macro"},{"candidate_id":"cand_56af131a36c2eab633b1","lane":"macro"}],"focus_root_occurrences":[],"gloss":"pleasant well-being and bestowed favor","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"حسن الحال والنعمة","image_en":"pleasant well-being and bestowed favor"}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"حسن الحال والنعمة","image_en":"pleasant well-being and bestowed favor","scope_ar":"يدخل فيه النعمة والنعمى والنعماء والنعيم والإنعام، بمعنى حسن الحال وطيب العيش والمن والعطاء والإحسان الموصل إلى غيره.","scope_en":"This branch covers blessing, favor, bounty, good condition, pleasant living, and benefaction given to another."},"support_links":["sup_51399e621030adfb6a5d","sup_a7376aec448cd5a67406"]},{"boundary":"It includes hady for a man possessing inviolability because he seeks protection or a pledge before being granted it, and hady for a captive in some reports","branch_kind":null,"branch_ref":"root_001583/B007","candidate_links":[{"candidate_id":"cand_18703bcf347440afcb42","lane":"macro"}],"focus_root_occurrences":[],"gloss":"a protected person or captive called hady","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"هدي الحرمة والأسير","image_en":"a protected person or captive called hady"}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"هدي الحرمة والأسير","image_en":"a protected person or captive called hady","scope_ar":"يدخل فيه الهدي للرجل ذي الحرمة المستجير أو الآخذ عهدا قبل أن يجار وللأسير في بعض الأقوال","scope_en":"It includes hady for a man possessing inviolability because he seeks protection or a pledge before being granted it, and hady for a captive in some reports"},"support_links":["sup_ccec50095c07b4e1540f"]},{"boundary":"Includes mawla as patron or freed person, agnate or cousin, neighbor, in-law, legal manumission patronage, and affiliated dependents.","branch_kind":null,"branch_ref":"root_001684/B005","candidate_links":[{"candidate_id":"cand_18703bcf347440afcb42","lane":"macro"}],"focus_root_occurrences":[],"gloss":"kinship and manumission patronage","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"ولاء قرابة وعتق وجوار","image_en":"kinship and manumission patronage"}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"ولاء قرابة وعتق وجوار","image_en":"kinship and manumission patronage","scope_ar":"يدخل فيه المولى بمعاني المعتق والمعتق وابن العم والعصبة والجار والصهر والولاء القانوني للمعتق والموالي المنتسبين","scope_en":"Includes mawla as patron or freed person, agnate or cousin, neighbor, in-law, legal manumission patronage, and affiliated dependents."},"support_links":["sup_ccec50095c07b4e1540f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000009/B002","candidate_links":[{"candidate_id":"cand_647e3faf1f6ad542c0ec","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_537bbf5f96fa411c4234","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Active giving makes value leave the subject's possession and enter relation.","root":"ء ت ي","source_ref":"92:18","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000009","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6ee6121e2651b60beb8e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000017/B002","candidate_links":[{"candidate_id":"cand_56af131a36c2eab633b1","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2eef32f7400d8267a124","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Exhaustive scope under negation removes every candidate human creditor.","root":"ء ح د","source_ref":"92:19","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000017","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a7376aec448cd5a67406"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000019/B001","candidate_links":[{"candidate_id":"cand_62a9229cd296274eb852","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8c9a55aa6803c70072cd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The later or last term establishes the far temporal boundary.","root":"ء خ ر","source_ref":"92:13","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000019","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_68dab5d4db31f58d24f5"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000067/B001","candidate_links":[{"candidate_id":"cand_62a9229cd296274eb852","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8c9a55aa6803c70072cd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Beginning and precedence establish the near temporal boundary.","root":"ء و ل","source_ref":"92:13","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000067","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_68dab5d4db31f58d24f5"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000067/B002","candidate_links":[{"candidate_id":"cand_62a9229cd296274eb852","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8c9a55aa6803c70072cd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Return toward final outcome turns the temporal pair into a course with a meaningful terminus.","root":"ء و ل","source_ref":"92:13","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000067","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_68dab5d4db31f58d24f5"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000138/B001","candidate_links":[{"candidate_id":"cand_7c46be0cb75535197987","lane":"macro"},{"candidate_id":"cand_b7c23c193d1764e69611","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a7b9fd41ee5fffc61a7f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Deliberate seeking supplies the vector that precedes the promised arrival.","root":"ب غ ي","source_ref":"92:20","source_word_indices":["2"]},{"hft_ref":"hft_395ffad8cfa874b33d8b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Seeking establishes the subject as moving toward something he does not produce for himself.","root":"ب غ ي","source_ref":"92:20","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000138","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5ff162ef651bc90031ee","sup_be1a3cf49b3f7cd249fa"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000244/B001","candidate_links":[{"candidate_id":"cand_56af131a36c2eab633b1","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2eef32f7400d8267a124","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Counterbalancing an act with its return supplies the transactional loop that the negation breaks.","root":"ج ز ي","source_ref":"92:19","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000244","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a7376aec448cd5a67406"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000262/B003","candidate_links":[{"candidate_id":"cand_8e5fb0a604a1c43c11ba","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d3da5854c4101ac2fcb7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Being made separate and distant provides the positive subject's spatial reversal.","root":"ج ن ب","source_ref":"92:17","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000262","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4bc153124929efa0f62d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000532/B002","candidate_links":[{"candidate_id":"cand_7c46be0cb75535197987","lane":"macro"},{"candidate_id":"cand_b7c23c193d1764e69611","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a7b9fd41ee5fffc61a7f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Nurturing, repair, and completion provide a process by which the seeker can be brought to fullness.","root":"ر ب ب","source_ref":"92:20","source_word_indices":["4"]},{"hft_ref":"hft_395ffad8cfa874b33d8b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Nurture and completion supply a plausible contextual agency that brings the seeker to the resulting state.","root":"ر ب ب","source_ref":"92:20","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000532","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5ff162ef651bc90031ee","sup_be1a3cf49b3f7cd249fa"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000537/B005","candidate_links":[{"candidate_id":"cand_94508efab8ab397dd9dd","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_79789d4189657f67a6d6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant mapped branch of feeding and development supplies nurture across the interval before fullness.","root":"ر ب ب","source_ref":"92:20","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000537","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_afbcb90733bed8a1a59d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000637/B001","candidate_links":[{"candidate_id":"cand_647e3faf1f6ad542c0ec","lane":"macro"},{"candidate_id":"cand_94508efab8ab397dd9dd","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_537bbf5f96fa411c4234","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Growth and increase relocate gain from the stock to the giver's developing state.","root":"ز ك و","source_ref":"92:18","source_word_indices":["4"]},{"hft_ref":"hft_79789d4189657f67a6d6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Growth and increase make the giver's inner change developmental.","root":"ز ك و","source_ref":"92:18","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000637","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6ee6121e2651b60beb8e","sup_afbcb90733bed8a1a59d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000637/B002","candidate_links":[{"candidate_id":"cand_647e3faf1f6ad542c0ec","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_537bbf5f96fa411c4234","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Purification makes the gain qualitative as well as expansive.","root":"ز ك و","source_ref":"92:18","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000637","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6ee6121e2651b60beb8e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000809/B001","candidate_links":[{"candidate_id":"cand_8e5fb0a604a1c43c11ba","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d3da5854c4101ac2fcb7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Wretchedness opposed to flourishing names the condition produced by that contact.","root":"ش ق و","source_ref":"92:15","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000809","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4bc153124929efa0f62d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000880/B003","candidate_links":[{"candidate_id":"cand_8e5fb0a604a1c43c11ba","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d3da5854c4101ac2fcb7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Meeting fire and its heat defines the adverse relation as direct contact.","root":"ص ل ي","source_ref":"92:15","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000880","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4bc153124929efa0f62d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001042/B002","candidate_links":[{"candidate_id":"cand_7c46be0cb75535197987","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a7b9fd41ee5fffc61a7f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Elevation and honor place the sought relation above ordinary social exchange.","root":"ع ل و","source_ref":"92:20","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001042","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_be1a3cf49b3f7cd249fa"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001052/B004","candidate_links":[{"candidate_id":"cand_56af131a36c2eab633b1","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2eef32f7400d8267a124","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Proximity or possession locates the alleged favor in the subject's social account before it is denied.","root":"ع ن د","source_ref":"92:19","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001052","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a7376aec448cd5a67406"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001357/B001","candidate_links":[{"candidate_id":"cand_8e5fb0a604a1c43c11ba","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d3da5854c4101ac2fcb7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Pure, actively burning flame intensifies the medium into something consuming.","root":"ل ظ ي","source_ref":"92:14","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001357","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4bc153124929efa0f62d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001457/B001","candidate_links":[{"candidate_id":"cand_647e3faf1f6ad542c0ec","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_537bbf5f96fa411c4234","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Accumulated property supplies the material stock being released.","root":"م و ل","source_ref":"92:18","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001457","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6ee6121e2651b60beb8e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001564/B002","candidate_links":[{"candidate_id":"cand_8e5fb0a604a1c43c11ba","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d3da5854c4101ac2fcb7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A kindled fire supplies the dangerous medium from which the later subject is separated.","root":"ن و ر","source_ref":"92:14","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001564","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4bc153124929efa0f62d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001583/B001","candidate_links":[{"candidate_id":"cand_62a9229cd296274eb852","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8c9a55aa6803c70072cd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Gentle indication toward a path supplies orientation rather than coercive transport.","root":"ه د ي","source_ref":"92:12","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001583","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_68dab5d4db31f58d24f5"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001630/B002","candidate_links":[{"candidate_id":"cand_7c46be0cb75535197987","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a7b9fd41ee5fffc61a7f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Direction and orientation give the seeking a determinate bearing.","root":"و ج ه","source_ref":"92:20","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001630","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_be1a3cf49b3f7cd249fa"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001630/B003","candidate_links":[{"candidate_id":"cand_7c46be0cb75535197987","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a7b9fd41ee5fffc61a7f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Face-to-face encounter adds a relational endpoint alongside bare direction.","root":"و ج ه","source_ref":"92:20","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001630","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_be1a3cf49b3f7cd249fa"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001677/B001","candidate_links":[{"candidate_id":"cand_8e5fb0a604a1c43c11ba","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d3da5854c4101ac2fcb7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Warding off harm supplies the protective function of that separation.","root":"و ق ي","source_ref":"92:17","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001677","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4bc153124929efa0f62d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001684/B007","candidate_links":[{"candidate_id":"cand_8e5fb0a604a1c43c11ba","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d3da5854c4101ac2fcb7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Turning away supplies the orientation that precedes the adverse exposure.","root":"و ل ي","source_ref":"92:16","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001684","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4bc153124929efa0f62d"]}],"candidate_inventory":[{"anchor_refs":["92:19","92:21"],"branch_refs":["root_000569/B001","root_000569/B002","root_001525/B001"],"candidate_id":"cand_9641fb3c7d43ca2d5618","commentary_obligation":"review","focus_branch_refs":["root_000569/B001","root_000569/B002"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001525/B001"],"root_ids":[],"scope":"pericope","source_local_id":"A:Contentment and Abundant Satisfaction","source_type":"channel","support_ids":["sup_51399e621030adfb6a5d","sup_6a22170b39a7a657d7bb","sup_83ff16b8454a885826f4","sup_95c3f15d44a76d50ac6a","sup_cb28556b6be4fc7091a4"],"title":"Contentment and Abundant Satisfaction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:12","92:16","92:20","92:21"],"branch_refs":["root_000532/B011","root_000569/B006","root_001583/B007","root_001684/B005"],"candidate_id":"cand_18703bcf347440afcb42","commentary_obligation":"review","focus_branch_refs":["root_000569/B006"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000532/B011","root_001583/B007","root_001684/B005"],"root_ids":[],"scope":"pericope","source_local_id":"C:Pact, Surety, and Protected Alliance","source_type":"channel","support_ids":["sup_189446ae92084307064c","sup_4293019f0d0f6dcfaa9f","sup_9dde66ada772df9ad10f","sup_add03a61340a3562a8ca","sup_ccec50095c07b4e1540f"],"title":"Pact, Surety, and Protected Alliance","trust":"trusted","unresolved_branch_citations":[{"citation":"ر ض ي/B004","reason":"no registered branch match"}],"unresolved_branch_refs":[]},{"anchor_refs":["92:12","92:13","92:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:21","branch_refs":["root_000019/B001","root_000067/B001","root_000067/B002","root_000569/B001","root_001583/B001"],"candidate_id":"cand_62a9229cd296274eb852","commentary_obligation":"review","hft_ref":"hft_8c9a55aa6803c70072cd","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_guided_temporal_wholeness","source_type":"hft","support_ids":["sup_68dab5d4db31f58d24f5"],"title":"delta_guided_temporal_wholeness","trust":"legacy_unbound"},{"anchor_refs":["92:14","92:15","92:16","92:17","92:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:21","branch_refs":["root_000262/B003","root_000569/B001","root_000809/B001","root_000880/B003","root_001357/B001","root_001564/B002","root_001677/B001","root_001684/B007"],"candidate_id":"cand_8e5fb0a604a1c43c11ba","commentary_obligation":"review","hft_ref":"hft_d3da5854c4101ac2fcb7","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_separation_from_consuming_contact","source_type":"hft","support_ids":["sup_4bc153124929efa0f62d"],"title":"delta_separation_from_consuming_contact","trust":"legacy_unbound"},{"anchor_refs":["92:18","92:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:21","branch_refs":["root_000009/B002","root_000569/B002","root_000637/B001","root_000637/B002","root_001457/B001"],"candidate_id":"cand_647e3faf1f6ad542c0ec","commentary_obligation":"review","hft_ref":"hft_537bbf5f96fa411c4234","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_release_becomes_growth","source_type":"hft","support_ids":["sup_6ee6121e2651b60beb8e"],"title":"delta_release_becomes_growth","trust":"legacy_unbound"},{"anchor_refs":["92:19","92:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:21","branch_refs":["root_000017/B002","root_000244/B001","root_000569/B003","root_001052/B004","root_001525/B001"],"candidate_id":"cand_56af131a36c2eab633b1","commentary_obligation":"review","hft_ref":"hft_2eef32f7400d8267a124","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_human_reciprocity_weakened","source_type":"hft","support_ids":["sup_a7376aec448cd5a67406"],"title":"delta_human_reciprocity_weakened","trust":"legacy_unbound"},{"anchor_refs":["92:20","92:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:21","branch_refs":["root_000138/B001","root_000532/B002","root_000569/B001","root_000569/B003","root_001042/B002","root_001630/B002","root_001630/B003"],"candidate_id":"cand_7c46be0cb75535197987","commentary_obligation":"review","hft_ref":"hft_a7b9fd41ee5fffc61a7f","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_directed_nurturing_completion","source_type":"hft","support_ids":["sup_be1a3cf49b3f7cd249fa"],"title":"delta_directed_nurturing_completion","trust":"legacy_unbound"},{"anchor_refs":["92:20","92:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:21","branch_refs":["root_000138/B001","root_000532/B002","root_000569/B004"],"candidate_id":"cand_b7c23c193d1764e69611","commentary_obligation":"review","hft_ref":"hft_395ffad8cfa874b33d8b","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_implied_satisfier","source_type":"hft","support_ids":["sup_5ff162ef651bc90031ee"],"title":"outlier_implied_satisfier","trust":"legacy_unbound"},{"anchor_refs":["92:18","92:20","92:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:21","branch_refs":["root_000537/B005","root_000569/B002","root_000637/B001"],"candidate_id":"cand_94508efab8ab397dd9dd","commentary_obligation":"review","hft_ref":"hft_79789d4189657f67a6d6","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_nurtured_ripening","source_type":"hft","support_ids":["sup_afbcb90733bed8a1a59d"],"title":"outlier_nurtured_ripening","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_dda128b3993267ce2c58","connection_ref":"conn_0a5217b899f986ed64c6","note":"Immediate surah frame joins first and last domains; situates the future horizon.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_dcdc8c048ce1613335a1","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"92:13","source_note":"Local later fulfillment extends the surrounding temporal sequence.","source_row_role":"ranked_review","source_target_component_ref":"92:21","source_target_components":["92:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:21"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:13","source_target_components":["92:13"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:13","target_evidence":{"arabic_uthmani":"وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ","ayah_ref":"92:13"},"target_ref":"92:13"},{"connection_evidence_ref":"conn_ev_67e4b30a9e5fb94062f3","connection_ref":"conn_78fc24e7514ab8b1209d","note":"Immediate denial of repayable favor safeguards the non-transactional motive before the focus.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_4a6c0c01dc1e90019fd4","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:19","source_note":"Supplies the concluding satisfaction in the same giving sequence.","source_row_role":"ranked_review","source_target_component_ref":"92:21","source_target_components":["92:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:21"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:19","source_target_components":["92:19"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:19","target_evidence":{"arabic_uthmani":"وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ","ayah_ref":"92:19"},"target_ref":"92:19"},{"connection_evidence_ref":"conn_ev_775f86b8c478b5b390fb","connection_ref":"conn_26661d69b5738a5a6b39","note":"Immediate exclusive orientation to the highest Lord gives the focus its motive direction.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_ff988f616e786e7eb8d8","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:20","source_note":"Immediate outcome card: satisfaction completes the preceding exclusive seeking.","source_row_role":"ranked_review","source_target_component_ref":"92:21","source_target_components":["92:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:21"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:20","source_target_components":["92:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:20","target_evidence":{"arabic_uthmani":"إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ","ayah_ref":"92:20"},"target_ref":"92:20"},{"connection_evidence_ref":"conn_ev_0ece91e093b5e9c5d879","connection_ref":"conn_c71f27c249ed3f32da51","note":"Immediate denial-and-turning-away branch sharpens the contrast with the focused outcome.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_a86fb094fc5720d783f5","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"92:16","source_note":"Completes the contrary trajectory that begins at 92:17.","source_row_role":"ranked_review","source_target_component_ref":"92:21","source_target_components":["92:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:21"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:16","source_target_components":["92:16"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:16","target_evidence":{"arabic_uthmani":"ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ","ayah_ref":"92:16"},"target_ref":"92:16"},{"connection_evidence_ref":"conn_ev_f3ff9a32a94501947840","connection_ref":"conn_ce1cb608a19377a4bac4","note":"Immediate claim of divine guidance supports the surah’s directed positive branch.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_33af8080326266661b82","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"92:12","source_note":"Local closure shows the eventual satisfaction associated with the giving-side sequence.","source_row_role":"ranked_review","source_target_component_ref":"92:21","source_target_components":["92:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:21"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:12","source_target_components":["92:12"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:12","target_evidence":{"arabic_uthmani":"إِنَّ عَلَيْنَا لَلْهُدَىٰ","ayah_ref":"92:12"},"target_ref":"92:12"},{"connection_evidence_ref":"conn_ev_0204cf02bd185ca766cd","connection_ref":"conn_4d5edc678c1bb92f409b","note":"Immediate exclusion of the wretched from the fire completes the surah’s contrary branch.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_9a6b981d710ab7a24ba5","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"92:15","source_note":"Final satisfaction belongs to the opposite surah trajectory.","source_row_role":"ranked_review","source_target_component_ref":"92:21","source_target_components":["92:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:21"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:15","source_target_components":["92:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:15","target_evidence":{"arabic_uthmani":"لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى","ayah_ref":"92:15"},"target_ref":"92:15"},{"connection_ref":"conn_53c3adcee13fd026d19f","note":null,"origin":"derived_reciprocal_seed","prior_label":null,"qualification":{"boundary":"At least one source-direction review meaningfully linked this target back to the focus ayah. Treat its note and label only as a discovery nomination. Reassess the relation from the focus ayah using the supplied exact target Arabic; do not invent missing target morphology or inherit the source label.","derived_reciprocal_counterevidence":false,"derived_reciprocal_seed":true,"has_missing_ayah_suggestion_source_row":true,"has_ranked_review_source_row":false,"has_reciprocal_counterevidence":false,"has_reciprocal_nomination":true,"receiving_direction_requires_fresh_assessment":true,"source_direction_labels_are_not_focus_decisions":true,"source_row_roles_are_provenance_not_decisions":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_e03e7736c14d4515eb51","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"92:14","source_note":"Supplies the final satisfaction promised to the protected giver, completing the passage's contrast.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"92:21","source_target_components":["92:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:21"}],"relation_scope":"declared_pericope_reciprocal_evidence","target_evidence":{"arabic_uthmani":"فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ","ayah_ref":"92:14"},"target_ref":"92:14"},{"connection_ref":"conn_0387977881952a7b4609","note":null,"origin":"derived_reciprocal_seed","prior_label":null,"qualification":{"boundary":"At least one source-direction review meaningfully linked this target back to the focus ayah. Treat its note and label only as a discovery nomination. Reassess the relation from the focus ayah using the supplied exact target Arabic; do not invent missing target morphology or inherit the source label.","derived_reciprocal_counterevidence":false,"derived_reciprocal_seed":true,"has_missing_ayah_suggestion_source_row":true,"has_ranked_review_source_row":false,"has_reciprocal_counterevidence":false,"has_reciprocal_nomination":true,"receiving_direction_requires_fresh_assessment":true,"source_direction_labels_are_not_focus_decisions":true,"source_row_roles_are_provenance_not_decisions":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_9b473c393963dd66fc61","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:17","source_note":"Yakın bağlamda nihai rıza sonucunu verir; 92:17'nin ateşten uzaklaştırmasının sonrasını bağlar.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"92:21","source_target_components":["92:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:21"}],"relation_scope":"declared_pericope_reciprocal_evidence","target_evidence":{"arabic_uthmani":"وَسَيُجَنَّبُهَا ٱلْأَتْقَى","ayah_ref":"92:17"},"target_ref":"92:17"},{"connection_ref":"conn_1aebfa213d318e83720b","note":null,"origin":"derived_reciprocal_seed","prior_label":null,"qualification":{"boundary":"At least one source-direction review meaningfully linked this target back to the focus ayah. Treat its note and label only as a discovery nomination. Reassess the relation from the focus ayah using the supplied exact target Arabic; do not invent missing target morphology or inherit the source label.","derived_reciprocal_counterevidence":false,"derived_reciprocal_seed":true,"has_missing_ayah_suggestion_source_row":true,"has_ranked_review_source_row":false,"has_reciprocal_counterevidence":false,"has_reciprocal_nomination":true,"receiving_direction_requires_fresh_assessment":true,"source_direction_labels_are_not_focus_decisions":true,"source_row_roles_are_provenance_not_decisions":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_c14963d7cba0aba09c19","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:18","source_note":"Immediate sequel gives the positive end of the giver's unrecompensed, Godward path.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"92:21","source_target_components":["92:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:21"}],"relation_scope":"declared_pericope_reciprocal_evidence","target_evidence":{"arabic_uthmani":"ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ","ayah_ref":"92:18"},"target_ref":"92:18"}],"focus":{"arabic_uthmani":"وَلَسَوْفَ يَرْضَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:21:1:1","qac_word_ref":"92:21:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"92:21:1:2","qac_word_ref":"92:21:1","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"سَوْف","morph_features":"STEM|POS:FUT|LEM:sawof","morpheme_role":"STEM","pos":"FUT","qac_ref":"92:21:1:3","qac_word_ref":"92:21:1","root_ar":"","surface_ar":"سَوْفَ"},{"lemma_ar":"رَّضِىَ","morph_features":"STEM|POS:V|IMPF|LEM:r~aDiYa|ROOT:rDw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:21:2:1","qac_word_ref":"92:21:2","root_ar":"ر ض و","surface_ar":"يَرْضَىٰ"}],"word_analysis_qac_refs":[["92:21:1:1"],["92:21:1:2","92:21:1:3"],["92:21:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["92:21:1","92:21:2","92:21:3"]},"focus_surface_evidence":{"arabic_uthmani":"وَلَسَوْفَ يَرْضَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:21:1:1","qac_word_ref":"92:21:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"92:21:1:2","qac_word_ref":"92:21:1","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"سَوْف","morph_features":"STEM|POS:FUT|LEM:sawof","morpheme_role":"STEM","pos":"FUT","qac_ref":"92:21:1:3","qac_word_ref":"92:21:1","root_ar":"","surface_ar":"سَوْفَ"},{"lemma_ar":"رَّضِىَ","morph_features":"STEM|POS:V|IMPF|LEM:r~aDiYa|ROOT:rDw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:21:2:1","qac_word_ref":"92:21:2","root_ar":"ر ض و","surface_ar":"يَرْضَىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["92:21:1:1"],["92:21:1:2","92:21:1:3"],["92:21:2:1"]],"word_analysis_refs":["92:21:1","92:21:2","92:21:3"],"word_rows":[{"analysis_record_ref":"92:21:1","analytic_gloss_range_en":"clause-opening connector that keeps the closing promise tied to the preceding motive chain while allowing a resumptive final declaration","analytic_root_gloss_range_en":null,"qac_refs":["92:21:1:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"92:21:2","analytic_gloss_range_en":"emphatic future particle cluster placing certainty and deferred futurity over the closing verb","analytic_root_gloss_range_en":null,"qac_refs":["92:21:1:2","92:21:1:3"],"root":{"note":"— (no root)"},"surface":{"arabic":"لَسَوْفَ","transliteration":"la-sawfa"}},{"analysis_record_ref":"92:21:3","analytic_gloss_range_en":"future objectless satisfaction or contented acceptance, with the subject recovered from the prior righteous giver and the object left unspecified","analytic_root_gloss_range_en":"satisfaction, pleasure, approval, acceptance, and being pleased; local grammar selects the intransitive state while broader root-family approval remains relevant as semantic pressure","qac_refs":["92:21:2:1"],"root":{"arabic":"ر ض ي","transliteration":"r-ḍ-y"},"surface":{"arabic":"يَرْضَىٰ","transliteration":"yarḍā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":10,"missing_anchor_refs":[],"supplied_unique_anchor_count":10},"assigned_record_count":7,"assigned_records":[{"anchor_refs":["92:12","92:13","92:21"],"branch_refs":["root_000019/B001","root_000067/B001","root_000067/B002","root_000569/B001","root_001583/B001"],"candidate_id":"cand_62a9229cd296274eb852","evidence_scope":"declared_pericope","hft_ref":"hft_8c9a55aa6803c70072cd","item_id":"delta_guided_temporal_wholeness","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_guided_temporal_wholeness","support_id":"sup_68dab5d4db31f58d24f5"},{"anchor_refs":["92:14","92:15","92:16","92:17","92:21"],"branch_refs":["root_000262/B003","root_000569/B001","root_000809/B001","root_000880/B003","root_001357/B001","root_001564/B002","root_001677/B001","root_001684/B007"],"candidate_id":"cand_8e5fb0a604a1c43c11ba","evidence_scope":"declared_pericope","hft_ref":"hft_d3da5854c4101ac2fcb7","item_id":"delta_separation_from_consuming_contact","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_separation_from_consuming_contact","support_id":"sup_4bc153124929efa0f62d"},{"anchor_refs":["92:18","92:21"],"branch_refs":["root_000009/B002","root_000569/B002","root_000637/B001","root_000637/B002","root_001457/B001"],"candidate_id":"cand_647e3faf1f6ad542c0ec","evidence_scope":"declared_pericope","hft_ref":"hft_537bbf5f96fa411c4234","item_id":"delta_release_becomes_growth","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_release_becomes_growth","support_id":"sup_6ee6121e2651b60beb8e"},{"anchor_refs":["92:19","92:21"],"branch_refs":["root_000017/B002","root_000244/B001","root_000569/B003","root_001052/B004","root_001525/B001"],"candidate_id":"cand_56af131a36c2eab633b1","evidence_scope":"declared_pericope","hft_ref":"hft_2eef32f7400d8267a124","item_id":"delta_human_reciprocity_weakened","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_human_reciprocity_weakened","support_id":"sup_a7376aec448cd5a67406"},{"anchor_refs":["92:20","92:21"],"branch_refs":["root_000138/B001","root_000532/B002","root_000569/B001","root_000569/B003","root_001042/B002","root_001630/B002","root_001630/B003"],"candidate_id":"cand_7c46be0cb75535197987","evidence_scope":"declared_pericope","hft_ref":"hft_a7b9fd41ee5fffc61a7f","item_id":"delta_directed_nurturing_completion","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_directed_nurturing_completion","support_id":"sup_be1a3cf49b3f7cd249fa"},{"anchor_refs":["92:20","92:21"],"branch_refs":["root_000138/B001","root_000532/B002","root_000569/B004"],"candidate_id":"cand_b7c23c193d1764e69611","evidence_scope":"declared_pericope","hft_ref":"hft_395ffad8cfa874b33d8b","item_id":"outlier_implied_satisfier","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_implied_satisfier","support_id":"sup_5ff162ef651bc90031ee"},{"anchor_refs":["92:18","92:20","92:21"],"branch_refs":["root_000537/B005","root_000569/B002","root_000637/B001"],"candidate_id":"cand_94508efab8ab397dd9dd","evidence_scope":"declared_pericope","hft_ref":"hft_79789d4189657f67a6d6","item_id":"outlier_nurtured_ripening","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_nurtured_ripening","support_id":"sup_afbcb90733bed8a1a59d"}],"diagnostics":[],"lane_counts":{"global":17,"macro":7,"micro":4},"packet_summary":{"ayah_count":21,"focus_ref":"92:21","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ج ز ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000244","furuq_root_norm":"ج ز ي","furuq_source_root_norm":"ج ز ي","is_dominant":true,"target_occurrences":97,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000242","furuq_root_norm":"ج ز ز","furuq_source_root_norm":"ج ز ز","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11","92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"92:21","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":18,"unstructured_record_count":0},"identity":{"ayah_ref":"92:21","lane":"macro","linguistic_source_ref":"92:21","surface_ref":"92:21","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"92:21","target_tokens":[["Ve",["92:21:1"]],["elbette",["92:21:1"]],["hoşnut",["92:21:2"]],["olacaktır",["92:21:1","92:21:2"]]],"text":"Ve elbette hoşnut olacaktır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":7,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":12,"ayah_to":21,"id":"s092-p02-012-021","label":"Guidance, fire, and generous salvation","number":2,"refs":["92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"92:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"92:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["92:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"92:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Pact, Surety, and Protected Alliance","source_type":"channel","support_id":"sup_189446ae92084307064c","text":"Parties establish a durable relation through pact, guaranty, patronage, and loyal aid.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Pact, Surety, and Protected Alliance","source_type":"channel","support_id":"sup_4293019f0d0f6dcfaa9f","text":"Pact defines the bond, surety secures performance, patronage gives it standing, and loyalty sustains it.","trust":"trusted"},{"branch_refs":["root_000569/B001","root_000569/B002","root_001525/B001"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Contentment and Abundant Satisfaction","source_type":"channel","support_id":"sup_51399e621030adfb6a5d","text":"acceptance opposed to displeasure `ر ض و:B001/m01`, `ر ض ي:B001/m01`; abundant or sought satisfaction `ر ض و:B002/m01`; favorable settled condition `ن ع م:B001/m03`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Contentment and Abundant Satisfaction","source_type":"channel","support_id":"sup_6a22170b39a7a657d7bb","text":"Persons move from displeasure or need into accepted, beneficial, and mutually sustaining relations.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Contentment and Abundant Satisfaction","source_type":"channel","support_id":"sup_83ff16b8454a885826f4","text":"92:21 (`ر ض و`: `يرضى`); 92:19 (`ن ع م`: `نعمة`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Contentment and Abundant Satisfaction","source_type":"channel","support_id":"sup_95c3f15d44a76d50ac6a","text":"Acceptance removes resistance, favor makes the state positively good, and abundant satisfaction describes its stable culmination.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Pact, Surety, and Protected Alliance","source_type":"channel","support_id":"sup_9dde66ada772df9ad10f","text":"92:20 (`ر ب ب`: `ربه`); 92:21 (`ر ض و`: `يرضى`); 92:16 (`و ل ي`: `تولى`); 92:12 (`ه د ي`: `الهدى`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Pact, Surety, and Protected Alliance","source_type":"channel","support_id":"sup_add03a61340a3562a8ca","text":"A verbal or written commitment binds participants by promise, vow, record, surety, pact, or injunction.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Contentment and Abundant Satisfaction","source_type":"channel","support_id":"sup_cb28556b6be4fc7091a4","text":"Aversion ceases, an outcome is accepted, and satisfaction may expand into an abundant settled state.","trust":"trusted"},{"branch_refs":["root_000532/B011","root_000569/B006","root_001583/B007","root_001684/B005"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"C:Pact, Surety, and Protected Alliance","source_type":"channel","support_id":"sup_ccec50095c07b4e1540f","text":"pact and covenant `ر ب ب:B011/m01`; guarantor or obedient loyal party `ر ض و:B006/m01`; obedient, loving, or guaranteeing trusted person `ر ض ي:B004/m01`; legal patronage `و ل ي:B005/m01`; protected person under a pledge `ه د ي:B007/m01`","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ عَلَيْنَا لَلْهُدَىٰ","ayah_ref":"92:12"},{"arabic_uthmani":"وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ","ayah_ref":"92:13"},{"arabic_uthmani":"وَلَسَوْفَ يَرْضَىٰ","ayah_ref":"92:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000019/B001","root_000067/B001","root_000067/B002","root_000569/B001","root_001583/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000569","role":"Acceptance is recast as arrival at the end of an oriented temporal course.","root":"ر ض و","source_ref":"92:21","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001583","role":"Gentle indication toward a path supplies orientation rather than coercive transport.","root":"ه د ي","source_ref":"92:12","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000019","role":"The later or last term establishes the far temporal boundary.","root":"ء خ ر","source_ref":"92:13","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000067","role":"Beginning and precedence establish the near temporal boundary.","root":"ء و ل","source_ref":"92:13","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000067","role":"Return toward final outcome turns the temporal pair into a course with a meaningful terminus.","root":"ء و ل","source_ref":"92:13","source_word_indices":["4"]}],"changed_reading":{"after":"The delay is a guided interval whose beginning and outcome lie within one encompassing order, making رضا an assured arrival rather than a lucky turn.","before":"The delay before satisfaction is an empty interval."},"confidence":"medium","mechanism":"Gentle indication supplies direction, while the first and the last place both temporal ends within one domain and the return-to-outcome branch folds beginning toward consequence. The delayed رضا becomes arrival within an already held and guided whole.","model_id":"delta_guided_temporal_wholeness","reader_inference":"The packet supplies guidance, both temporal ends, and return to outcome; I infer that the future satisfaction is an arrival secured within that whole. The alternative is that ownership of both ends guarantees authority but does not describe the subject's experience of guidance.","status":"strengthened","structural_cues":["92:12-13 repeat emphatic إِنَّ while shifting from human striving to first-person plural responsibility and possession.","The coordinated last and first encompass both temporal boundaries before the focus says سَوْفَ."],"trigger_roots":["ه د ي","ء خ ر","ء و ل"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_guided_temporal_wholeness","source_type":"hft","support_id":"sup_68dab5d4db31f58d24f5","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ","ayah_ref":"92:14"},{"arabic_uthmani":"لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى","ayah_ref":"92:15"},{"arabic_uthmani":"ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ","ayah_ref":"92:16"},{"arabic_uthmani":"وَسَيُجَنَّبُهَا ٱلْأَتْقَى","ayah_ref":"92:17"},{"arabic_uthmani":"وَلَسَوْفَ يَرْضَىٰ","ayah_ref":"92:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":5,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":5,"target_morphology_supplied":false},"branch_refs":["root_000262/B003","root_000569/B001","root_000809/B001","root_000880/B003","root_001357/B001","root_001564/B002","root_001677/B001","root_001684/B007"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000569","role":"The affective endpoint is grounded in a preceding change of exposure and location.","root":"ر ض و","source_ref":"92:21","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001564","role":"A kindled fire supplies the dangerous medium from which the later subject is separated.","root":"ن و ر","source_ref":"92:14","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001357","role":"Pure, actively burning flame intensifies the medium into something consuming.","root":"ل ظ ي","source_ref":"92:14","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000880","role":"Meeting fire and its heat defines the adverse relation as direct contact.","root":"ص ل ي","source_ref":"92:15","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000809","role":"Wretchedness opposed to flourishing names the condition produced by that contact.","root":"ش ق و","source_ref":"92:15","source_word_indices":["4"]},{"branch_id":"B007","mapped_root_id":"root_001684","role":"Turning away supplies the orientation that precedes the adverse exposure.","root":"و ل ي","source_ref":"92:16","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000262","role":"Being made separate and distant provides the positive subject's spatial reversal.","root":"ج ن ب","source_ref":"92:17","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001677","role":"Warding off harm supplies the protective function of that separation.","root":"و ق ي","source_ref":"92:17","source_word_indices":["2"]}],"changed_reading":{"after":"Satisfaction is also embodied relief: the subject has been relocated outside a relation of consuming contact and held within protection.","before":"Satisfaction is only an inward evaluation."},"confidence":"strong","mechanism":"Kindled flame becomes pure consuming heat, and misery is defined by entering into contact with it after denial and turning away. The guarded subject is instead moved aside and warded from harm. رضا thus gains a spatial and bodily substrate: satisfaction as no longer being exposed to consumption.","model_id":"delta_separation_from_consuming_contact","reader_inference":"The packet supplies a consuming medium, direct contact, turning away, separation, and protection; I infer that removal from exposure enables the later رضا. The alternative is that the fire sequence marks fate while satisfaction remains a distinct reward with no bodily mechanism.","status":"new","structural_cues":["The feminine object pronoun threads one danger from the blaze, through contact, to being kept aside from it.","The restrictive إِلَّا construction contrasts the one exposed with the superlative guarded subject who is separated."],"trigger_roots":["ن و ر","ل ظ ي","ص ل ي","ش ق و","و ل ي","ج ن ب","و ق ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_separation_from_consuming_contact","source_type":"hft","support_id":"sup_4bc153124929efa0f62d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ","ayah_ref":"92:18"},{"arabic_uthmani":"وَلَسَوْفَ يَرْضَىٰ","ayah_ref":"92:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000009/B002","root_000569/B002","root_000637/B001","root_000637/B002","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000569","role":"Abundant satisfaction supplies the eventual surplus that possession alone could not provide.","root":"ر ض و","source_ref":"92:21","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000009","role":"Active giving makes value leave the subject's possession and enter relation.","root":"ء ت ي","source_ref":"92:18","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Accumulated property supplies the material stock being released.","root":"م و ل","source_ref":"92:18","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000637","role":"Growth and increase relocate gain from the stock to the giver's developing state.","root":"ز ك و","source_ref":"92:18","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000637","role":"Purification makes the gain qualitative as well as expansive.","root":"ز ك و","source_ref":"92:18","source_word_indices":["4"]}],"changed_reading":{"after":"Giving converts stored wealth into personal growth and purification, so satisfaction is the ripened surplus of release rather than reimbursement for depletion.","before":"Satisfaction compensates the giver for a net material loss."},"confidence":"strong","mechanism":"Wealth is actively transferred outward while the giver reflexively grows and is purified. The focus's abundant satisfaction becomes the surplus generated by release: what leaves as possession returns as enlargement of the person rather than of the store.","model_id":"delta_release_becomes_growth","reader_inference":"The packet supplies outward transfer followed by reflexive growth and purification; I infer that this transformed subject becomes capable of the later abundant رضا. The alternative is that purification is the motive of giving while satisfaction is a separate promised consequence.","status":"strengthened","structural_cues":["The same relative-clause subject gives his wealth and then appears inside the reflexive يَتَزَكَّىٰ.","The object leaves the subject while the resulting change remains in the subject."],"trigger_roots":["ء ت ي","م و ل","ز ك و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_release_becomes_growth","source_type":"hft","support_id":"sup_6ee6121e2651b60beb8e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ","ayah_ref":"92:19"},{"arabic_uthmani":"وَلَسَوْفَ يَرْضَىٰ","ayah_ref":"92:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000017/B002","root_000244/B001","root_000569/B003","root_001052/B004","root_001525/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000569","role":"The possible mutual-consent horizon is retained but narrowed by the cancellation of human debt.","root":"ر ض و","source_ref":"92:21","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000017","role":"Exhaustive scope under negation removes every candidate human creditor.","root":"ء ح د","source_ref":"92:19","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001052","role":"Proximity or possession locates the alleged favor in the subject's social account before it is denied.","root":"ع ن د","source_ref":"92:19","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001525","role":"A benefaction supplies the putative credit that could have motivated repayment.","root":"ن ع م","source_ref":"92:19","source_word_indices":["5"]},{"branch_id":"B001","mapped_root_id":"root_000244","role":"Counterbalancing an act with its return supplies the transactional loop that the negation breaks.","root":"ج ز ي","source_ref":"92:19","source_word_indices":["6"]}],"changed_reading":{"after":"Human repayment is explicitly cleared from the mechanism; if the focus remains relational, its decisive counterpart and source of satisfaction lie beyond the human favor-debt ledger.","before":"The unstated counterpart in the focus could be any human party whose consent or gratitude completes an exchange."},"confidence":"strong","mechanism":"Exhaustive negation removes any favor held with any human party that needs repayment. This weakens the baseline's unrestricted mutual-consent reading: the later satisfaction cannot be explained as balancing a human ledger or purchasing another person's approval.","model_id":"delta_human_reciprocity_weakened","reader_inference":"The packet supplies the absence of any human favor awaiting recompense; I infer that this severs human approval and repayment as causes of رضا. The alternative is narrower: the verse may negate only an antecedent motive while leaving other human relational satisfactions possible.","status":"weakened","structural_cues":["مَا, the indefinite أَحَدٍ, and مِن before an indefinite favor intensify the negation.","The passive تُجْزَىٰ suppresses a repaid agent and foregrounds the repayment structure itself."],"trigger_roots":["ء ح د","ع ن د","ن ع م","ج ز ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_human_reciprocity_weakened","source_type":"hft","support_id":"sup_a7376aec448cd5a67406","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ","ayah_ref":"92:20"},{"arabic_uthmani":"وَلَسَوْفَ يَرْضَىٰ","ayah_ref":"92:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000138/B001","root_000532/B002","root_000569/B001","root_000569/B003","root_001042/B002","root_001630/B002","root_001630/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000569","role":"Settled acceptance names the seeker's assured endpoint.","root":"ر ض و","source_ref":"92:21","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000569","role":"Mutual consent keeps a two-sided concord reading live without making it grammatically explicit.","root":"ر ض و","source_ref":"92:21","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000138","role":"Deliberate seeking supplies the vector that precedes the promised arrival.","root":"ب غ ي","source_ref":"92:20","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001630","role":"Direction and orientation give the seeking a determinate bearing.","root":"و ج ه","source_ref":"92:20","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001630","role":"Face-to-face encounter adds a relational endpoint alongside bare direction.","root":"و ج ه","source_ref":"92:20","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000532","role":"Nurturing, repair, and completion provide a process by which the seeker can be brought to fullness.","root":"ر ب ب","source_ref":"92:20","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_001042","role":"Elevation and honor place the sought relation above ordinary social exchange.","root":"ع ل و","source_ref":"92:20","source_word_indices":["5"]}],"changed_reading":{"after":"The subject reaches satisfaction as his upward-directed seeking is nurtured to completion—possibly as concord between seeker and sought, but certainly not as human repayment.","before":"The subject accepts an unspecified outcome, possibly through a human exchange."},"confidence":"medium","mechanism":"Seeking establishes an intentional vector toward a face or direction; lordship adds nurture and completion, and highest rank lifts the vector beyond the canceled human ledger. The future satisfaction becomes arrival into aligned relation. Mutual approval remains a coexisting possibility, but the grammar explicitly guarantees only the seeker's satisfaction.","model_id":"delta_directed_nurturing_completion","reader_inference":"The packet supplies seeking, orientation or encounter, nurturing completion, and elevation; I infer that the Lord brings the directed seeker to satisfaction and that concord may be two-sided. The live alternative is grammatically important: 92:21 predicates رضا only of the human subject and does not itself state reciprocal divine approval.","status":"revised","structural_cues":["The exception in 92:20 replaces the negated repayment motive with one positive motive: seeking.","Possessive رَبِّهِ binds the seeker to the sought Lord immediately before the focus promise.","The focus follows without restating an object, allowing the preceding directional relation to fill the omission."],"trigger_roots":["ب غ ي","و ج ه","ر ب ب","ع ل و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_directed_nurturing_completion","source_type":"hft","support_id":"sup_be1a3cf49b3f7cd249fa","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ","ayah_ref":"92:20"},{"arabic_uthmani":"وَلَسَوْفَ يَرْضَىٰ","ayah_ref":"92:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000138/B001","root_000532/B002","root_000569/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000569","role":"The causative and appeasing branch raises the possibility of an unexpressed satisfier behind the intransitive result.","root":"ر ض و","source_ref":"92:21","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000138","role":"Seeking establishes the subject as moving toward something he does not produce for himself.","root":"ب غ ي","source_ref":"92:20","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000532","role":"Nurture and completion supply a plausible contextual agency that brings the seeker to the resulting state.","root":"ر ب ب","source_ref":"92:20","source_word_indices":["4"]}],"changed_reading":{"after":"Exploratorily, the subject is brought to satisfaction by the nurturing completion of the one he seeks, though the verb itself states only his resulting state.","before":"The subject simply and spontaneously becomes satisfied."},"confidence":"exploratory","containment":"This is surprising because the focus is an active intransitive simple verb, whereas the activated focus branch concerns causing or seeking another's satisfaction. It remains useful because the immediately prior context supplies a nurturing Lord and a directed seeker, making an omitted causal agent conceivable; downstream prose must distinguish this inferred causation from the morphology and say that the subject is brought to satisfaction, not translate the verb as passive.","focus_anchor":"The focus names the subject's resulting state but leaves its cause unspoken.","outlier_id":"outlier_implied_satisfier"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_implied_satisfier","source_type":"hft","support_id":"sup_5ff162ef651bc90031ee","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ","ayah_ref":"92:18"},{"arabic_uthmani":"إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ","ayah_ref":"92:20"},{"arabic_uthmani":"وَلَسَوْفَ يَرْضَىٰ","ayah_ref":"92:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000537/B005","root_000569/B002","root_000637/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000569","role":"Abundant satisfaction supplies the mature fullness at the end of the analogy.","root":"ر ض و","source_ref":"92:21","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000637","role":"Growth and increase make the giver's inner change developmental.","root":"ز ك و","source_ref":"92:18","source_word_indices":["4"]},{"branch_id":"B005","mapped_root_id":"root_000537","role":"The non-dominant mapped branch of feeding and development supplies nurture across the interval before fullness.","root":"ر ب ب","source_ref":"92:20","source_word_indices":["4"]}],"changed_reading":{"after":"As a contained organic analogy, satisfaction ripens from growth that is fed and brought to fullness over time.","before":"Satisfaction appears suddenly as an external payment."},"confidence":"exploratory","containment":"This organic reading is surprising because it links a non-dominant split mapping under ر ب ب to the growth branch in the giving sequence and then materializes an affective verb as ripening. It remains anchored in the focus's abundant-satisfaction branch and in packet-backed growth and nourishment images; downstream prose should qualify it as an ecological model of how رضا develops, not as a lexical gloss.","focus_anchor":"The promised fullness can be construed as a state that matures rather than a reward delivered all at once.","outlier_id":"outlier_nurtured_ripening"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_nurtured_ripening","source_type":"hft","support_id":"sup_afbcb90733bed8a1a59d","trust":"legacy_unbound"}]}
</lane_packet_json>
