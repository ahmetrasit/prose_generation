# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **92:9**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s092-regular-20260912/s092/92_9/macro.discovery.json` and modify nothing
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
  "ayah_ref": "92:9",
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
{"branch_registry":[{"boundary":"Dal bir nitelik ve durum bildirir; başkasına iyilik etme eylemini, kişiye ulaşan iyi sonucu veya kalıplaşmış özel adlandırmaları kapsamaz.","branch_kind":"bare","branch_ref":"root_000323/B001","candidate_links":[{"candidate_id":"cand_e6a2e5a4c624472700f9","lane":"macro"},{"candidate_id":"cand_490d0e30ea938d504e61","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"حُسْنَىٰ","morph_features":"STEM|POS:N|LEM:HusonaY`|ROOT:Hsn|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:9:2:3","qac_word_ref":"92:9:2","surface_ar":"حُسْنَىٰ"}],"gloss":"akla, eğilime veya duyulara göre güzel ve beğenilir olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şeyin güzel ve beğenilir olması, çirkinliğin karşıtı olan temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olumlu değerlendirme akla, kişisel eğilime veya duyulara dayanabilir; dal yalnızca görsel güzellikle sınırlı değildir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsanlar güzel diye nitelenebilir ve aynı nitelik çok yüksek derecede güzelliği belirten biçimlerle güçlendirilebilir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir insanın, işin veya başka bir şeyin güzel yerleri ve iyi nitelikleri, onun kötü yanlarının karşıtı olarak topluca anılabilir."}}],"root_ar":"ح س ن","root_id":"root_000323","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kişi, şey, görünüş ve niteliklerdeki ortak çekirdeğini, olumlu değerlendirmenin farklı dayanaklarını silmeden karşılar.","boundary_detail":"Dal bir nitelik ve durum bildirir; başkasına iyilik etme eylemini, kişiye ulaşan iyi sonucu veya kalıplaşmış özel adlandırmaları kapsamaz.","branch_image_ar":"الحسن ضد القبح","concept_gloss":"akla, eğilime veya duyulara göre güzel ve beğenilir olma","contextual_glosses":[{"applicability":"Dış görünüşün veya duyularla algılanan bir şeyin güzel oluşunun öne çıktığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Akla veya kişisel eğilime dayanan daha geniş beğenilirlik alanını tek başına açıkça göstermez.","preserves":"Duyularla algılanan güzel oluşu ve çirkinliğe karşıtlığı korur."},"facet_ids":["F001","F003"],"text":"güzellik","usage_role":"general"},{"applicability":"Bir şeyin görünüşünden çok akıl, istek veya değerlendirme bakımından olumlu bulunduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin veya bedenin somut güzelliğini ve güzelliğin çok yüksek derecesini açıkça belirtmez.","preserves":"Bir şeyin olumlu bulunması ve istenir görülmesi yönünü korur."},"facet_ids":["F001","F002"],"text":"beğenilirlik","usage_role":"explanatory"},{"applicability":"Bir kişi, iş veya şeydeki güzel yerler ile iyi niteliklerin topluca kötü yanlarla karşılaştırıldığı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çoğul güzel yerleri ve iyi nitelikleri kötü yanların karşıtı olarak eksiksiz korur."},"facet_ids":["F004"],"text":"güzel yanlar","usage_role":"contextual"}],"definition":"Bir kişinin, şeyin, görünüşün veya niteliğin; akıl, kişisel eğilim ya da duyular bakımından güzel ve beğenilir bulunması, dolayısıyla çirkinliğin ve kötü yanların karşısında yer almasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şeyin güzel ve beğenilir olması, çirkinliğin karşıtı olan temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Olumlu değerlendirme akla, kişisel eğilime veya duyulara dayanabilir; dal yalnızca görsel güzellikle sınırlı değildir."},{"facet_id":"F003","role":"specialization","statement":"İnsanlar güzel diye nitelenebilir ve aynı nitelik çok yüksek derecede güzelliği belirten biçimlerle güçlendirilebilir."},{"facet_id":"F004","role":"extension","statement":"Bir insanın, işin veya başka bir şeyin güzel yerleri ve iyi nitelikleri, onun kötü yanlarının karşıtı olarak topluca anılabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ahlaki davranış veya başkasına yarar sağlama eylemi anlamını çağrıştırır.","collision":"İyi iş yapma ve başkasına iyilik etme dalıyla karışır.","fit":"displacement","loses":"Görünüşteki güzelliği, yoğun güzelliği ve güzel yanların çirkinliğe karşıtlığını siler.","preserves":"Olumlu değerlendirme ve beğenilirlik yönünden sınırlı bir ortaklık taşır."},"text":"iyilik"}],"identity_rationale":"Dalın çirkinliğin karşıtı olan güzel ve beğenilir niteliğe ilişkin çerçevesi, kaynak söz öbeğiyle örtüşür. Bu nitelik yalnızca dış görünüşe bağlı değildir; aklın, kişisel eğilimin veya duyuların olumlu bulduğu şeyleri, kişilerdeki yoğun güzelliği ve bir kişi ya da şeydeki güzel yanları da kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"güzel ve beğenilir olma; güzellik"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"güzel olmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"güzel erkek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"güzel kadın"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"güzel kadın"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"çok güzel kadın"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"çok güzel"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"güzel yanlar ve iyi nitelikler"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bedenin güzel yeri"}],"lexicalization_note":"Dalın yalın kapsamı güzel ve beğenilir olma niteliğidir; belirli bir söz öbeğine özgü eylem veya sonuç anlamı bu kapsama taşınmamalıdır.","neighbor_coverage_note":"Bütün aday komşular karşılaştırıldı; yalnızca nitelik ile eylem ayrımını veya güzelliğin kapsam sınırını belirginleştiren üç ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeği bir varlık ya da niteliğin güzel ve beğenilir oluşudur. Komşu dalın sınırı daha geniştir; güzelleştirme ve güzel davranma gibi eylemsel kullanımları da içerdiği için her bağlamda birbirinin yerine geçmezler.","focus_only":"Bu dal, akıl, eğilim veya duyular bakımından beğenilir olmayı ve güzel yanları genel bir nitelik olarak kapsar.","gloss":"güzel oluş ve güzel davranış alanı","neighbor_only":"Komşu dal, güzel görünüş ve güzel eylemin yanında güzelleştirmeyi, güzel davranmayı ve kimi özel davranış biçimlerini de kapsar.","neighbor_ref":"root_000260/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da kişi, beden, şey veya eylemde olumlu ve güzel bulunan yönü anlatabilir."},{"boundary_match":"partial","distinction":"Niteliğin güzel olması ile bir kişinin iyi bir iş yapması aynı çekirdek değildir. İlki varlık veya nitelik değerlendirmesidir; ikincisi yapanı, yapılan işi ve kimi zaman yarar gören kişiyi içeren bir eylemdir.","focus_only":"Bu dal, kişi veya şeyde bulunan güzel ve beğenilir niteliği bildirir.","gloss":"iyi eylem ve iyilik etme","neighbor_only":"Komşu dal, bir işi iyi yapmayı, bir şeyi güzelleştirmeyi veya başkasına iyilik etmeyi bildirir.","neighbor_ref":"root_000323/B002","relation_type":"near_neighbor","shared_zone":"Güzel bir eylem olumlu değerlendirildiğinde iki dal aynı olay çevresinde buluşabilir."},{"boundary_match":"partial","distinction":"Komşu dalın kusursuzluk ve görünüş odağı, bu dalın akıl, eğilim ve duyulara yayılan genel beğenilirlik sınırından daha dardır. Görsel bağlamlarda yaklaşsalar da değerlendirme kapsamları tam örtüşmez.","focus_only":"Bu dal, görünüş dışında akla ve kişisel eğilime göre beğenilirliği de kapsar.","gloss":"kusursuz ve güzel oluş","neighbor_only":"Komşu dal, güzel oluşu özellikle kusurdan arınmışlık, süs ve yüz güzelliği çevresinde belirginleştirir.","neighbor_ref":"root_000660/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da güzel görünüşü ve bir şeyin çirkin ya da kusurlu sayılmamasını anlatır."}],"source_phrase_ar":"الحسن ضد القبح (maqayis;sihah)؛ حسن الشيء فهو حسن (ayn)؛ الحسن نعت لما حسن (tahdhib)؛ كل مبهج مرغوب فيه (mufradat)؛ مستحسن من جهة العقل ومستحسن من جهة الهوى ومستحسن من جهة الحس (mufradat)؛ رجل حسن وامرأة حسناء وحسانة (maqayis)؛ الحسان الحسن جدا (ayn)؛ المحاسن ضد المساوىء (maqayis;ayn;sihah;tahdhib)","source_summary":"Kaynaklar, temel karşıtlığı güzel ile çirkin arasında kurar; güzel olmayı kişi ve şeylere yüklenen bir nitelik olarak verir. Toplu anlatım ayrıca akla, eğilime ve duyulara göre beğenilirliği, yoğun güzelliği ve güzel yanların kötü yanlara karşıtlığını kapsar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"النعت والمصدر لما كان حسنا أو مرغوبا أو ضد القبح، ويشمل حسن الشخص والشيء والمحاسن والحسان","what_is_not_ar":"الإحسان إلى الغير، والحسنة بمعنى النعمة أو الثواب، والأعلام والمواضع المسماة بالحسن"},"support_links":["sup_6bba7cd5b4303ef8a3d7","sup_91fec92a5b011059f45b"]},{"boundary":"Dal güzel bir niteliğin kendisini değil, güzelleştiren, iyi yapan veya bir başkasına yarar sağlayan eylemi anlatır.","branch_kind":"bare","branch_ref":"root_000323/B002","candidate_links":[{"candidate_id":"cand_371579ef487deedf8019","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"حُسْنَىٰ","morph_features":"STEM|POS:N|LEM:HusonaY`|ROOT:Hsn|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:9:2:3","qac_word_ref":"92:9:2","surface_ar":"حُسْنَىٰ"}],"gloss":"bir şeyi güzelleştirme, işi iyi yapma veya başkasına iyilik etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kötü davranmanın karşısında yer alan iyi ve güzel eylem, dalın ortak eylemsel çekirdeğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem bir başkasına yöneldiğinde ona yarar sağlama, iyilik etme veya iyi davranma biçimini alır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eylem kişinin kendi işine yöneldiğinde işi iyi, doğru ve ustalıkla yapmayı belirtir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir şeyi daha güzel duruma getirme, iyi eylemin nesne üzerinde sonuç doğuran biçimidir."}},{"facet_id":"F005","role":"specialization","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"İyilik etme, kimi kullanımda yalnızca denk karşılığı vermekle yetinmeyip bunun üzerine çıkmayı gerektirir."}}],"root_ar":"ح س ن","root_id":"root_000323","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın nesneyi güzelleştirme, eylemi iyi yürütme ve bir başkasına yarar sağlama biçimlerini birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Dal güzel bir niteliğin kendisini değil, güzelleştiren, iyi yapan veya bir başkasına yarar sağlayan eylemi anlatır.","branch_image_ar":"الإحسان فعل حسن","concept_gloss":"bir şeyi güzelleştirme, işi iyi yapma veya başkasına iyilik etme","contextual_glosses":[{"applicability":"Eylemin başka bir kişiye yöneldiği ve ona yarar ya da karşılıksız bir fazlalık sağladığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendi işini iyi yapması ve bir nesneyi güzelleştirmesi yönlerini kapsamaz.","preserves":"Başkasına yönelme, yarar sağlama ve denk karşılığın ötesine geçme yönünü korur."},"facet_ids":["F001","F002","F005"],"text":"iyilik etmek","usage_role":"contextual"},{"applicability":"Bir kişinin yaptığı işi özenle, doğru biçimde veya ustalıkla yürüttüğü bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasına iyilik etme ve bir nesneyi daha güzel duruma getirme yönlerini dışarıda bırakır.","preserves":"Eylemin iyi ve ustalıklı biçimde yerine getirilmesi yönünü korur."},"facet_ids":["F001","F003"],"text":"işini iyi yapmak","usage_role":"contextual"},{"applicability":"Eylemin bir nesnenin görünüşünü veya niteliğini daha güzel duruma getirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşi iyi yapma ve bir başkasına yarar sağlayan iyilikte bulunma yönlerini kapsamaz.","preserves":"Bir nesnede daha güzel bir durum meydana getirme sonucunu korur."},"facet_ids":["F001","F004"],"text":"güzelleştirmek","usage_role":"contextual"}],"definition":"Bir şeyi güzelleştirmek, bir işi iyi ve özenli biçimde yapmak ya da bir başkasına yarar sağlayan bir iyilikte bulunmaktır. Başkasına yönelik biçimi, yalnızca denk bir karşılık vermenin ötesine geçen artırılmış bir iyilik içerebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kötü davranmanın karşısında yer alan iyi ve güzel eylem, dalın ortak eylemsel çekirdeğidir."},{"facet_id":"F002","role":"specialization","statement":"Eylem bir başkasına yöneldiğinde ona yarar sağlama, iyilik etme veya iyi davranma biçimini alır."},{"facet_id":"F003","role":"specialization","statement":"Eylem kişinin kendi işine yöneldiğinde işi iyi, doğru ve ustalıkla yapmayı belirtir."},{"facet_id":"F004","role":"extension","statement":"Bir şeyi daha güzel duruma getirme, iyi eylemin nesne üzerinde sonuç doğuran biçimidir."},{"facet_id":"F005","role":"specialization","statement":"İyilik etme, kimi kullanımda yalnızca denk karşılığı vermekle yetinmeyip bunun üzerine çıkmayı gerektirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Eylem yerine kişide veya şeyde bulunan durağan bir nitelik anlamını öne çıkarır.","collision":"Güzel ve beğenilir olma niteliğini anlatan dalla karışır.","fit":"displacement","loses":"Yapan kişiyi, eylemin yürütülüşünü ve iyilikten yararlanan kişiyi görünmez kılar.","preserves":"Bir nesneyi güzelleştirme sonucuyla ve iyi eylemin olumlu değerlendirilmesiyle bağlantıyı korur."},"text":"güzellik"}],"identity_rationale":"Dal çerçevesi, kaynak söz öbeğinde bulunan başkasına iyilik etme ve kişinin kendi işini iyi yapma yönlerini birlikte korur. Bir şeyi güzelleştirme, eylemi ustalıkla yürütme, kötülüğün karşısında iyi davranma ve karşılık denkliğini aşan iyilik de bu eylemsel çekirdeğin ayrı görünümleridir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir şeyi güzelleştirmek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"birine iyilik etmek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"işini iyi ve ustalıkla yapmak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"iyilik etme veya işi iyi yapma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"iyilik eden veya işini iyi yapan kimse"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sürekli iyilik eden kimse"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"güzel bulmak; beğenmek"}],"lexicalization_note":"Dal belirli bir söz öbeğine bağlı değildir; genel eylem alanı, başkasına yarar sağlama ile işi iyi ve özenli yapma yönleri ayrılarak tanımlanmalıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; iyi eylemin yardım ve güzel nitelikten ayrıldığı üç yararlı sınır karşılaştırması seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Başkasına iyilik sunma bağlamında yakın karşılık olabilirler. Ancak bu dalın işi ustalıkla yapma ve nesneyi güzelleştirme kapsamı komşuda bulunmadığından genel sınırları eş değildir.","focus_only":"Bu dal, başkasına iyilik etmenin yanında kişinin kendi işini iyi yapmasını ve bir şeyi güzelleştirmesini de kapsar.","gloss":"başkasına sunulan iyilik ve yardım","neighbor_only":"Komşu dal, özellikle başkasına sunulan yararlı iş, yardım ve iyilik üzerinde yoğunlaşır.","neighbor_ref":"root_000885/B003","relation_type":"near_synonym","shared_zone":"Bir kişinin başkasına yarar sağlayan iyi bir iş yapması iki dalın doğrudan örtüştüğü alandır."},{"boundary_match":"partial","distinction":"Ortak alanda anlamlar yaklaşır; fakat komşunun belirli çaba ve davranış örnekleri bu dalın kurucu sınırı değildir. Bu dal da nesneyi güzelleştirme ve işi ustalıkla yapma yönleriyle komşudan daha geniştir.","focus_only":"Bu dal, her tür iyi yapışı ve başkasına yarar sağlamayı, ayrıca nesneyi güzelleştirmeyi kapsar.","gloss":"güzel iş ve iyilikte bulunma","neighbor_only":"Komşu dal, güzel iş ve iyilikle birlikte cömertlikte veya savaşta çaba gösterme gibi daha belirli davranış alanlarına uzanır.","neighbor_ref":"root_000153/B003","relation_type":"near_synonym","shared_zone":"İyi bir iş yapmak ve bir başkasına yarar sunmak iki dalın ortak merkezidir."},{"boundary_match":"partial","distinction":"Bir işin yapılması ile o işin veya başka bir şeyin güzel bulunması ayrı çekirdeklerdir. Bu dal eylem ve katılımcıları, komşu dal ise nitelik ve değerlendirmeyi öne çıkarır.","focus_only":"Bu dal, yapanı ve yapılan işi içeren iyi eylemi bildirir.","gloss":"güzel ve beğenilir olma","neighbor_only":"Komşu dal, bir kişi veya şeyde bulunan güzel ve beğenilir niteliği bildirir.","neighbor_ref":"root_000323/B001","relation_type":"near_neighbor","shared_zone":"İyi yapılan bir iş, sonuçta güzel ve beğenilir diye değerlendirilebilir."}],"source_phrase_ar":"أحسنت إليه وبه (sihah)؛ وهو يحسن الشيء أي يعمله (sihah)؛ حسنت الشيء تحسينا زينته (sihah)؛ أحسن يا هذا فإنك محسان (tahdhib)؛ الإحسان ضد الإساءة (tahdhib)؛ أحسنت بفلان أي أحسنت إليه (tahdhib)؛ الإحسان يقال على وجهين الإنعام على الغير وإحسان في فعله (mufradat)؛ الإحسان فوق العدل (mufradat)","source_summary":"Toplu kaynak anlatımı eylemi iki ana yönde verir: bir başkasına yarar sağlayan iyilik ve kişinin yaptığı işi iyi yürütmesi. Bir şeyi güzelleştirme, kötülüğün karşıtı olan iyi davranış ve denk karşılığın üstüne çıkan verme de bu çerçevede yer alır.","sources":["AY","SI","TA","MU"],"what_is_ar":"الفعل الحسن والإتقان والإنعام على الغير والزيادة على العدل، وما يقابل الإساءة","what_is_not_ar":"مجرد هيئة الشيء الحسنة، والحسنة اسما للنعمة أو الثواب، والمواضع والأعلام"},"support_links":["sup_7721baf86920745c6e5a"]},{"boundary":"Dal, bir şeyi güzel kılan niteliği ya da iyilik etme eylemini değil, kişiye ulaşan iyi şeyi, karşılığı veya sonucu bildirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000323/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُسْنَىٰ","morph_features":"STEM|POS:N|LEM:HusonaY`|ROOT:Hsn|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:9:2:3","qac_word_ref":"92:9:2","surface_ar":"حُسْنَىٰ"}],"gloss":"kişiye ulaşan sevindirici iyilik, karşılık veya iyi sonuç","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişiye ulaşan ve onu sevindiren iyilik, iyi karşılık veya iyi sonuç, kötü şeyin ve kötü sonun karşıtıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bolluk, geniş geçim ve utkı, kişinin dünyadaki yaşamında karşılaştığı sevindirici iyi sonuçlar olarak bu dala girer."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İyi bir karşılık veya ödül, sonsuz mutluluk yurduyla örneklenen olumlu son biçimini alabilir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İki iyi sonuçtan birini bildiren kalıplaşmış kullanım, seçenekleri utkı ile kişinin inancı uğruna ölmesiyle sınırlar."}}],"root_ar":"ح س ن","root_id":"root_000323","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın dünyadaki bolluktan ödüle ve belirli iyi sonlara uzanan ortak alıcı ve sonuç yapısını birlikte karşılar.","boundary_detail":"Dal, bir şeyi güzel kılan niteliği ya da iyilik etme eylemini değil, kişiye ulaşan iyi şeyi, karşılığı veya sonucu bildirir.","branch_image_ar":"الحسنة خير يصيب","concept_gloss":"kişiye ulaşan sevindirici iyilik, karşılık veya iyi sonuç","contextual_glosses":[{"applicability":"Bir olayın sonu, utkı veya iki olumlu seçenekten biri söz konusu olduğunda doğal ve kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiye ulaşan bolluk, sevindirici iyilik ve ödül anlamlarını tek başına açıkça göstermez.","preserves":"Kötü sonun karşısındaki olumlu sonucu ve belirli iyi sonları korur."},"facet_ids":["F001","F002","F004"],"text":"iyi sonuç","usage_role":"general"},{"applicability":"İyi davranışa verilen ödülün veya olumlu sonucun vurgulandığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bolluk, geniş geçim ve utkı gibi karşılık olmak zorunda olmayan iyi şeyleri dışarıda bırakır.","preserves":"Kişiye ulaşan olumlu karşılığı ve iyi son yönünü korur."},"facet_ids":["F001","F003"],"text":"güzel karşılık","usage_role":"contextual"},{"applicability":"Kişinin yaşamında karşılaştığı geniş geçim, rahatlık ve sevindirici iyilik söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ödül, sonsuz mutluluk yurdu, utkı ve iki iyi sonuçtan biri anlamlarını kapsamaz.","preserves":"Dünyadaki sevindirici iyilik ve genişlik yönünü korur."},"facet_ids":["F001","F002"],"text":"bolluk ve esenlik","usage_role":"contextual"}],"definition":"Bir kişiyi sevindiren iyilik, bolluk, iyi karşılık veya kötü bir şeyin karşısında yer alan iyi sonuçtur. Belirli kullanımlarda sonsuz mutluluk yurdu, utkı ya da inancı uğruna ölme gibi iyi sonları gösterir; iki seçenekli kalıplaşmış kullanım ise yalnızca son iki sonucu birlikte sınırlar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişiye ulaşan ve onu sevindiren iyilik, iyi karşılık veya iyi sonuç, kötü şeyin ve kötü sonun karşıtıdır."},{"facet_id":"F002","role":"specialization","statement":"Bolluk, geniş geçim ve utkı, kişinin dünyadaki yaşamında karşılaştığı sevindirici iyi sonuçlar olarak bu dala girer."},{"facet_id":"F003","role":"specialization","statement":"İyi bir karşılık veya ödül, sonsuz mutluluk yurduyla örneklenen olumlu son biçimini alabilir."},{"facet_id":"F004","role":"source_variant","statement":"İki iyi sonuçtan birini bildiren kalıplaşmış kullanım, seçenekleri utkı ile kişinin inancı uğruna ölmesiyle sınırlar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bir kişi veya şeyde bulunan güzel niteliği öne çıkarır.","collision":"Güzel ve beğenilir olma dalıyla karışır.","fit":"displacement","loses":"Kişiye ulaşan iyiliği, karşılığı, ödülü ve olayın iyi sonucunu siler.","preserves":"Olumlu ve istenir olma yönü bakımından sınırlı bir bağlantı taşır."},"text":"güzellik"},{"category":"confusable","error_profile":{"adds":"Sonuç yerine iyiliği yapan kişinin eylemini çekirdek anlam yapar.","collision":"İyi iş yapma ve başkasına iyilik etme dalıyla karışır.","fit":"displacement","loses":"Kişinin aldığı iyiliği, ödülü ve olayın iyi sonucunu ürün olarak göstermez.","preserves":"İyilik yapan ile iyilikten yararlanan arasındaki olay bağını korur."},"text":"iyilik etme"}],"identity_rationale":"Dal çerçevesi, kaynak söz öbeğinin kişiyi sevindiren iyilik, bolluk, iyi karşılık ve iyi son anlamlarını doğru biçimde toplar. Sonsuz mutluluk yurdu, utkı ve inancı uğruna ölme belirli iyi sonuçlar olarak kalmalı; dalın tamamı yalnızca bu örneklere veya güzel bir niteliğe indirgenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kişiye ulaşan iyilik, bolluk veya ödül"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"iyi son veya en güzel karşılık; sonsuz mutluluk yurdu, utkı ya da inancı uğruna ölme"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"iki iyi sonuçtan biri: utkı ya da inancı uğruna ölme"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kötü işleri gideren iyi işler, özellikle beş günlük tapınma"}],"lexicalization_note":"Genel olarak kişiye ulaşan iyilik ve iyi sonuç bildiren tek sözcüklü biçimler ile iki iyi sonuçtan birini anlatan kalıplaşmış söz öbeği ayrı tutulmalı; bu söz öbeğinin ikili sınırı bütün dala yayılmamalıdır.","neighbor_coverage_note":"Bütün aday komşular incelendi; iyi şeyin kötülükle karşıtlığı ve nitelik ile eylemden ayrılığı en açıklayıcı üç ilişki olarak seçildi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu dal olumlu kutupta iyilik ve iyi sonucu, komşu dal olumsuz kutupta kötülük ve kötü durumu gösterir. Karşıtlık ortak değerlendirme eksenindedir; her birinin özel örnekleri bire bir eşleşmek zorunda değildir.","focus_only":"Bu dal, kişiye ulaşan sevindirici iyiliği, ödülü ve iyi sonucu bildirir.","gloss":"kötülük ve kötü sonuç","neighbor_only":"Komşu dal, kötülüğü, zararı, kötü durumu ve kötü kişiyi bildirir.","neighbor_ref":"root_000787/B001","relation_type":"antonym","shared_zone":"İki dal, bir kişinin karşılaştığı şeyin iyi ya da kötü olması ekseninde karşı karşıya gelir."},{"boundary_match":"partial","distinction":"Olumlu nitelik ile o niteliği taşıyan bir sonuç ya da kişiye ulaşan iyilik aynı değildir. Bu dal ürün ve sonuç yapısını; komşu dal ise nitelik ve değerlendirmeyi korur.","focus_only":"Bu dal, kişiye ulaşan iyi şeyi, karşılığı veya sonucu adlandırır.","gloss":"güzel ve beğenilir nitelik","neighbor_only":"Komşu dal, kişi ya da şeyde bulunan güzel ve beğenilir niteliği adlandırır.","neighbor_ref":"root_000323/B001","relation_type":"near_neighbor","shared_zone":"İyi bir sonuç veya ödül, olumlu ve beğenilir diye nitelenebilir."},{"boundary_match":"partial","distinction":"Komşu dal yapanın eylemini ve işin yapılışını, bu dal ise alıcının karşılaştığı iyiliği veya çıkan iyi sonucu merkez alır. Süreç ile ürün birbirinin yerine kullanılamaz.","focus_only":"Bu dal, iyiliğin kişiye ulaşan ürününü, karşılığını veya sonucunu bildirir.","gloss":"iyi davranma ve iyilik etme","neighbor_only":"Komşu dal, bir kişinin iyi işi yapmasını veya başkasına iyilikte bulunmasını bildirir.","neighbor_ref":"root_000323/B002","relation_type":"near_neighbor","shared_zone":"Birine yapılan iyilik, o kişinin karşılaştığı sevindirici bir iyilik doğurabilir."}],"source_phrase_ar":"للذين أحسنوا الحسنى وزيادة أي الجنة وهي ضد السوءى (ayn)؛ الحسنة خلاف السيئة (sihah)؛ الحسنى خلاف السوأى (sihah)؛ الحسنى هي الجنة وضد الحسنى السوءى (tahdhib)؛ إحدى الحسنيين يعني الظفر أو الشهادة (tahdhib)؛ حسنة أي نعمة (tahdhib)؛ أي غنيمة وخصب (tahdhib)؛ الحسنة يعبر عنها عن كل ما يسر من نعمة (mufradat)؛ خصب وسعة وظفر (mufradat)؛ من ثواب وما أصابك من سيئة أي من عقاب (mufradat)","source_summary":"Kaynakların toplu anlatımı, kötü şeyin karşısındaki sevindirici iyiliği hem dünyadaki bolluk ve utkı hem de ödül ve iyi son olarak verir. Sonsuz mutluluk yurdu ile iki iyi sonuçtan biri olan utkı veya inanç uğruna ölüm, genel çekirdeğin belirli gerçekleşmeleridir.","sources":["AY","SI","TA","MU"],"what_is_ar":"الحسنة والحسنى بوصفهما خيرا أو نعمة أو ثوابا أو عاقبة حسنة تقابل السيئة والسوءى","what_is_not_ar":"النعت الجمالي، وفعل الإحسان نفسه، وأسماء الأماكن والأشخاص"},"support_links":[]},{"boundary":"Bu kümedeki sözler geçtikleri yerde güzellik niteliğini zorunlu olarak bildirmez; belirli yer, beden bölümü, gök cismi ve eylem gönderimlerini korur.","branch_kind":"bare","branch_ref":"root_000323/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُسْنَىٰ","morph_features":"STEM|POS:N|LEM:HusonaY`|ROOT:Hsn|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:9:2:3","qac_word_ref":"92:9:2","surface_ar":"حُسْنَىٰ"}],"gloss":"yer, gök cismi ve beden bölümü adları ile kum tepesine oturma kullanımı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir dağ, kum sırtı, kumluk veya temiz yüksek kum tepesi bu söz ailesindeki biçimlerle adlandırılabilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ön kolun bileğe yakın yarısı için kalıplaşmış bir beden bölümü adlandırması bulunur."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Söz ailesindeki ayrı bir biçim ayı adlandırır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Söz ailesindeki küçültmeli bir biçim, yüksek dağ anlamında kullanılır."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bağlantılı eylem biçimi, temiz ve yüksek bir kum tepesine oturmayı bildirir."}}],"root_ar":"ح س ن","root_id":"root_000323","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek bir ortak nesne anlamı varsaymadan, dalın farklı kalıplaşmış gönderimlerini ve bağlantılı eylemini topluca tanıtmak için kullanılır.","boundary_detail":"Bu kümedeki sözler geçtikleri yerde güzellik niteliğini zorunlu olarak bildirmez; belirli yer, beden bölümü, gök cismi ve eylem gönderimlerini korur.","branch_image_ar":"أسماء الحسن للمواضع والأجسام","concept_gloss":"yer, gök cismi ve beden bölümü adları ile kum tepesine oturma kullanımı","contextual_glosses":[{"applicability":"Biçimin bir arazi oluşumunu ya da belirli bir kumluk yeri adlandırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ön kol bölümünü, ayı ve kum tepesine oturma eylemini kapsamaz.","preserves":"Dağ ve kum oluşumlarına ilişkin kalıplaşmış yer gönderimlerini korur."},"facet_ids":["F001","F004"],"text":"dağ, kum sırtı veya kum tepesi adı","usage_role":"contextual"},{"applicability":"Sözün insan bedenindeki ön kol bölümünü gösterdiği dar kullanımın tam açıklamasıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Beden bölümünü ve ön kol içindeki bileğe yakın konumunu eksiksiz korur."},"facet_ids":["F002"],"text":"ön kolun bileğe yakın yarısı","usage_role":"explanatory"},{"applicability":"Söz ailesindeki ilgili biçimin gök cismini adlandırdığı kullanımda doğrudan karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gök cismi olan ay gönderimini doğrudan ve eksiksiz korur."},"facet_ids":["F003"],"text":"ay","usage_role":"contextual"}],"definition":"Aynı söz ailesindeki biçimlerin dağ, kum sırtı, kum tepesi, ön kolun bileğe yakın yarısı, ay ve yüksek dağ için kalıplaşmış adlandırmalar olarak kullanıldığı; ayrıca temiz ve yüksek bir kum tepesine oturma eylemini bildirdiği söz varlığı kümesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir dağ, kum sırtı, kumluk veya temiz yüksek kum tepesi bu söz ailesindeki biçimlerle adlandırılabilir."},{"facet_id":"F002","role":"source_variant","statement":"Ön kolun bileğe yakın yarısı için kalıplaşmış bir beden bölümü adlandırması bulunur."},{"facet_id":"F003","role":"source_variant","statement":"Söz ailesindeki ayrı bir biçim ayı adlandırır."},{"facet_id":"F004","role":"source_variant","statement":"Söz ailesindeki küçültmeli bir biçim, yüksek dağ anlamında kullanılır."},{"facet_id":"F005","role":"associated_use","statement":"Bağlantılı eylem biçimi, temiz ve yüksek bir kum tepesine oturmayı bildirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bu gönderimlerin her birinde güzel olma niteliğinin ileri sürüldüğü izlenimini doğurur.","collision":"Güzel ve beğenilir olma niteliğini anlatan dalla karışır.","fit":"displacement","loses":"Dağ, kum oluşumu, beden bölümü, ay ve oturma eylemine ilişkin kalıplaşmış gönderimleri siler.","preserves":"Söz ailesinin öteki dalındaki olumlu değerlendirmeyle biçimsel bağlantıyı sezdirir."},"text":"güzellik"}],"identity_rationale":"Dal, kaynak söz öbeğindeki dağ, kum sırtı ve kum tepesi gibi yer adlandırmalarını doğru yakalar; ancak kaynak aynı kümede ön kolun bileğe yakın yarısını, ayı, yüksek dağı ve temiz yüksek bir kum tepesine oturma eylemini de verir. Bu nedenle dal tek bir yer veya nesne türü gibi değil, birbiriyle aynı biçim ailesini paylaşan kalıplaşmış gönderimler ve bunlara bağlı bir eylem kullanımı olarak tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir dağın, kum sırtının, kumluğun veya kum tepesinin adı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ön kolun bileğe yakın yarısı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"ay"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yüksek dağ"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"temiz ve yüksek bir kum tepesine oturmak"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"iki yerin veya iki kum sırtının birlikte anılışı"}],"lexicalization_note":"Dal belirli bir söz öbeğiyle sınırlı sayılmamalı; tek sözcüklü biçimlerde kalıplaşmış birden çok gönderimi ve kum tepesine oturmayı bildiren bağlantılı eylem kullanımını kapsamalıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; adlandırma alanındaki en yakın üç küme ile güzel nitelik dalından ayrımı gösteren dört ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortaklık, beden bölümü ve ad verme alanındadır; gönderimler aynı değildir. Bu daldaki ön kol yarısı ve kum oluşumları, komşunun yıldız, tepe, yer ve araç bölümü adlarının yerine kullanılamaz.","focus_only":"Bu dal kum oluşumları, dağ, ay ve ön kolun belirli yarısı için kendi kalıplaşmış adlandırmalarını içerir.","gloss":"ön kol adıyla anılan yerler ve bölümler","neighbor_only":"Komşu dal, ön kol adıyla anılan yıldız kümeleri, tepeler, yerler ve araç bölümleri gibi farklı adlandırmaları içerir.","neighbor_ref":"root_000512/B013","relation_type":"same_field","shared_zone":"Her iki dalda beden bölümü ile yer veya nesne adlandırmaları aynı söz varlığı alanında yan yana gelir."},{"boundary_match":"field_only","distinction":"Her iki küme ad verme alanında buluşsa da adlandırdıkları yerler ve gök cisimleri ile kullandıkları söz ailesi ayrıdır. Alan ortaklığı anlam eşdeğerliği sağlamaz.","focus_only":"Bu dal belirli kum oluşumlarını, bir beden bölümünü, ayı ve yüksek dağı adlandıran biçimleri kapsar.","gloss":"kişi, yer ve yıldız adları","neighbor_only":"Komşu dal farklı kişi, yer ve yıldız adlarını kendi söz ailesinde toplar.","neighbor_ref":"root_000333/B012","relation_type":"same_field","shared_zone":"İki dal da sözlerin kişi dışı yer ve gök gönderimleri için özel adlandırma olarak kullanılmasını içerir."},{"boundary_match":"partial","distinction":"Dağ adı olma bakımından yaklaşsalar da aynı dağı veya aynı adlandırmayı göstermezler. Ayrıca bu dalın kum, beden, ay ve eylem kapsamı komşu dalda yoktur.","focus_only":"Bu dal birden çok dağ ve kum oluşumu kullanımının yanında beden bölümü, ay ve oturma eylemini de içerir.","gloss":"belirli bir dağın adı","neighbor_only":"Komşu dal yalnızca belirli bir dağın özel adı olan tek bir gönderime odaklanır.","neighbor_ref":"root_000706/B006","relation_type":"near_neighbor","shared_zone":"Bir sözün dağa ad olması iki dalda da görülen ortak kullanım türüdür."},{"boundary_match":"partial","distinction":"Bu daldaki bir dağ, kum tepesi, beden bölümü veya ay gönderimi, o şeyin güzel olduğunu ileri sürmez. Komşu dal ise doğrudan güzel ve beğenilir niteliği taşır.","focus_only":"Bu dal, belirli yerleri, nesneleri ve bir eylemi kalıplaşmış olarak gösterir.","gloss":"güzel ve beğenilir olma","neighbor_only":"Komşu dal, kişi veya şeyin güzel ve beğenilir olmasını nitelik olarak bildirir.","neighbor_ref":"root_000323/B001","relation_type":"near_neighbor","shared_zone":"İki dal aynı söz ailesindeki biçimleri kullandığı için yüzeyde kolayca karıştırılabilir."}],"source_phrase_ar":"الحسن جبل وحبل من حبال الرمل (maqayis)؛ الحسن من الذراع النصف الذي يلي الكوع (maqayis)؛ حسن اسم رملة لنبي سعد (ayn)؛ الحاسن القمر (sihah)؛ الحسن اسم رملة لبنى سعد (sihah)؛ الحسن نقا في ديار بني تميم (tahdhib)؛ أحسن الرجل إذا جلس على الحسن وهو الكثيب النقي العالي (tahdhib)؛ الحسين الجبل العالي (tahdhib)","source_summary":"Toplu kaynak anlatımı, aynı biçim ailesine dağ ve kum oluşumu adları, ön kolun bir yarısı, ay ve yüksek dağ gibi farklı kalıplaşmış gönderimler bağlar. Temiz yüksek bir kum tepesine oturmayı bildiren eylem de bu yer adlandırmasına bağlı ayrı bir kullanımdır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"الأسماء المتفرعة من الحسن للمواضع والأجسام والأجزاء، مثل الحسن للرمل أو الجبل، والحسين للجبل العالي، والحسن من الذراع، والحاسن للقمر","what_is_not_ar":"المعنى الخلقي أو العمل الصالح، والحسنة بمعنى النعمة، وعبارة الجهد والغاية"},"support_links":[]},{"boundary":"Dal yalnızca iki kalıplaşmış ifadeye bağlıdır; genel çaba, genel amaç veya her türlü son nokta anlamına genişletilmemelidir.","branch_kind":"non_bare","branch_ref":"root_000323/B005","candidate_links":[{"candidate_id":"cand_6a25b1fbe91c2776e086","lane":"macro"},{"candidate_id":"cand_0968a5887fd224d0d990","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"حُسْنَىٰ","morph_features":"STEM|POS:N|LEM:HusonaY`|ROOT:Hsn|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:9:2:3","qac_word_ref":"92:9:2","surface_ar":"حُسْنَىٰ"}],"gloss":"bir işteki en yüksek çabası ve erişebileceği son sınır","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir işi yapmada kişiye ait en yüksek çaba ile ulaşılabilecek son sınır birlikte anlatılır."}}],"root_ar":"ح س ن","root_id":"root_000323","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kanıtlanan iki kalıplaşmış biçimde, kişinin belirli bir işi yapma gücünün ve çabasının üst sınırı anlatılırken kullanılır.","boundary_detail":"Dal yalnızca iki kalıplaşmış ifadeye bağlıdır; genel çaba, genel amaç veya her türlü son nokta anlamına genişletilmemelidir.","branch_image_ar":"حُسَيْناء الغاية والجهد","concept_gloss":"bir işteki en yüksek çabası ve erişebileceği son sınır","contextual_glosses":[{"applicability":"Bir kişinin belirli bir işi yapmak için kullanabileceği bütün gücün vurgulandığı doğal anlatımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çabanın yanında ayrıca belirtilen erişilecek son sınırı açıkça adlandırmaz.","preserves":"Kişiye bağlı güç ve çabanın erişebildiği en yüksek dereceyi korur."},"facet_ids":["F001"],"text":"elinden gelenin en çoğu","usage_role":"contextual"},{"applicability":"Kişinin belli bir işi yaparken hem harcayabileceği çabanın hem ulaşabileceği noktanın üst sınırı açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gücü, etkin çabayı ve ulaşılabilecek son sınırı tek anlatımda korur."},"facet_ids":["F001"],"text":"gücünün ve çabasının son sınırı","usage_role":"explanatory"}],"definition":"Bir kişinin belirli bir işi yapmak için gösterebileceği en yüksek çabayı ve erişebileceği son sınırı bildiren, iki kalıplaşmış biçime özgü anlatımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir işi yapmada kişiye ait en yüksek çaba ile ulaşılabilecek son sınır birlikte anlatılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sınırın belirli bir kişiye ve onun bir işi yaparken göstereceği en yüksek çabaya bağlı olduğunu göstermez.","preserves":"Bir şeyin erişebileceği bitiş sınırı yönünü korur."},"text":"son nokta"}],"identity_rationale":"Dal çerçevesi, kaynak söz öbeğinde iki kalıplaşmış biçim için verilen bir işi yapmadaki en yüksek çaba ve erişilebilen son sınır anlamını doğru korur. Anlam genel güzellik, kişi adı veya yer adı değildir; yalnızca bu özel ifadelerin bir kişiye bağlanan güç ve son nokta değerlendirmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bir işi yaparken gösterebileceği en yüksek çaba ve erişebileceği son sınır"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bir işi yaparken gösterebileceği en yüksek çaba ve erişebileceği son sınır"}],"lexicalization_note":"Dal yalın bir kök anlamı değildir; anlam, kişinin belirli bir işi yaparken gösterebileceği en yüksek çaba ve erişebileceği son sınırı bildiren iki kalıplaşmış biçimle sınırlıdır.","neighbor_coverage_note":"Bütün aday komşular karşılaştırıldı; özel ifadenin çaba, güç yetirme ve genel son sınır alanlarından ayrılışını gösteren beş ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda sınır kişinin gücü ve çabasıyla ölçülür; komşuda ise varılan sonun övülmeye değer oluşu öne çıkar. Bu değerlendirme farkı nedeniyle yalnızca son sınır bağlamında yaklaşırlar.","focus_only":"Bu dalın kalıplaşmış biçimleri, kişinin belirli bir işi yapmadaki en yüksek çabasını ve erişebileceği sınırı bildirir.","gloss":"ulaşılması övülen son sınır","neighbor_only":"Komşu dalın kalıplaşmış biçimleri, ulaşılması övülen bir sonu ve varılacak en ileri noktayı bildirir.","neighbor_ref":"root_000355/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da kalıplaşmış bir anlatımla erişilebilecek en ileri noktayı belirtir."},{"boundary_match":"partial","distinction":"Komşu dal çaba sürecini genel olarak anlatır. Bu dal ise yalnızca özel biçimlerde, o çabanın ulaşabileceği en yüksek dereceyi ve son sınırı birlikte gösterir.","focus_only":"Bu dal iki kalıplaşmış biçimde çaba ile erişilebilen son sınırı birlikte bildirir.","gloss":"çalışıp bütün gücünü harcama","neighbor_only":"Komşu dal, belirli bir kalıba bağlı olmadan çalışıp çabalama ve güç harcamayı bildirir.","neighbor_ref":"root_000076/B010","relation_type":"near_synonym","shared_zone":"Bir işi yapmak için kişinin gücünü kullanması ve çaba göstermesi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Bu dal özel bir anlatımla en yüksek çaba ve son sınırı bildirir. Komşu dal ise genel yeterlik, alan darlığı, yetersizlik ve ölçüyü aşma gibi daha geniş durumlara uzanır.","focus_only":"Bu dal, kişinin bir işi yaparken harcadığı en yüksek çabayı sınırla birlikte öne çıkarır.","gloss":"güç yetirme ve erişim alanı","neighbor_only":"Komşu dal, genel güç yetirme alanını, yetmezliği ve ölçünün aşılmasını da kapsar.","neighbor_ref":"root_000512/B004","relation_type":"near_synonym","shared_zone":"Bir kişinin bir işi yapabilecek gücü ile erişebileceği sınır iki dalda da değerlendirilir."},{"boundary_match":"partial","distinction":"Komşu dal güçlük ve bütün gücü harcama sürecini genel alanlara yayar. Bu dalın anlamı ise iki özel biçimde kişisel çaba ile erişilen üst sınırın birlikte söylenmesine bağlıdır.","focus_only":"Bu dal iki kalıplaşmış biçimde kişinin bir işteki en yüksek çabası ile erişim sınırını birlikte verir.","gloss":"güçlük altında bütün gücünü kullanma","neighbor_only":"Komşu dal, güçlük altında bütün gücü kullanmayı ve iş, görüş veya yemin gibi daha geniş alanlarda sona varmayı kapsar.","neighbor_ref":"root_000268/B001","relation_type":"near_synonym","shared_zone":"Bir işi sonuçlandırmak için bütün gücün kullanılması ve sona kadar çabalanması iki dalda örtüşür."},{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği nesnenin ya da hareketin vardığı genel sondur. Bu dalda ise sınır, belirli bir kişinin işi yapma çabasının ve gücünün ölçüsüdür.","focus_only":"Bu dal, son sınırı bir kişinin belirli işi yapmadaki gücü ve çabasıyla ilişkilendirir.","gloss":"bir şeyin vardığı son ve bitiş","neighbor_only":"Komşu dal, bir şeyin genel bitişini, kenarını veya bir iletinin ya da okun hedefe ulaşmasını bildirir.","neighbor_ref":"root_001560/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da erişilen son noktayı veya üst sınırı anlatabilir."}],"source_phrase_ar":"حُسَيْناؤه أن يفعل كذا وحُسَيْناه مثله أي جهده وغايته (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"İki kalıplaşmış biçim de bir kişinin belirli bir işteki en yüksek çabasını ve erişebileceği son sınırı bildirir."}],"source_summary":"Ortaklaştırılacak çok kaynaklı bir anlatım yoktur; dal, aynı anlama gelen iki kalıplaşmış biçimin tek tanıklığına dayanır.","sources":["TA"],"what_is_ar":"قولهم حُسَيْناؤه أو حُسَيْناه بمعنى جهده وغايته","what_is_not_ar":"الحسن بمعنى الجمال، واسم الحسين للجبل أو الشخص، والحسنة بمعنى النعمة"},"support_links":["sup_e0eb26ca9d539070b61d","sup_f32e65bbafce1a920551"]},{"boundary":"Dal, gerçeğe aykırı söz ve davranışı kapsar; başkasını yalancılıkla niteleme eylemini ya da özel kalıpların bağımsız anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001290/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:9:1:2","qac_word_ref":"92:9:1","surface_ar":"كَذَّبَ"}],"gloss":"sözde veya davranışta doğruluğa aykırılık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğruluğa aykırılık hem söylenen bir sözde hem de yapılan bir davranışta gerçekleşebilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu niteliği taşıyan veya onu sıkça gösteren kişi, yalan söyleyen kişi olarak adlandırılır."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem söz hem davranış alanındaki bütün yalın anlam çekirdeğini karşılayan açıklayıcı üst karşılıktır.","boundary_detail":"Dal, gerçeğe aykırı söz ve davranışı kapsar; başkasını yalancılıkla niteleme eylemini ya da özel kalıpların bağımsız anlamlarını kapsamaz.","branch_image_ar":"خلاف الصدق","concept_gloss":"sözde veya davranışta doğruluğa aykırılık","contextual_glosses":[{"applicability":"Bağlamın söz veya davranıştaki doğruluğa aykırılığı zaten belirginleştirdiği doğal kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğruluğa aykırılık çekirdeğini ve kişiye yüklenebilen niteliği doğal Türkçeyle korur."},"facet_ids":["F001","F002"],"text":"yalan","usage_role":"general"}],"definition":"Bir sözün veya davranışın doğruluğa aykırı olmasıdır. Bu niteliği taşıyan kişi, yalan söyleyen ya da yalanı çokça tekrarlayan biri olarak betimlenebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğruluğa aykırılık hem söylenen bir sözde hem de yapılan bir davranışta gerçekleşebilir."},{"facet_id":"F002","role":"specialization","statement":"Bu niteliği taşıyan veya onu sıkça gösteren kişi, yalan söyleyen kişi olarak adlandırılır."}],"identity_rationale":"Kaynak ifadesi anlamı doğruluğun karşıtı olarak kurar ve bu karşıtlığın hem sözde hem davranışta gerçekleşebildiğini açıkça belirtir. Kişiyi bu nitelikle betimleyen biçimler aynı çekirdeğe bağlıdır; birini yalancı sayma eylemi ise ayrı dalın konusudur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sözde veya davranışta doğruluğa aykırılık; yalan"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yalancı; çok yalan söyleyen kişi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"uydurma söz; yalanlar"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"özürlere kaçınılmaz olarak yalan karışır"}],"lexicalization_note":"Tanım yalın anlam çekirdeğini verir; kişi betimleyen türevler ile özürlere ilişkin kalıp yalnız kendi sözcüksel karşılıklarında gösterilir ve yalın anlama eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yalanla en kolay karışan beş anlam yayımlandı, yalnızca aynı senaryoda bulunan özel kalıplar ve uzak tematik adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gerçeğe aykırı içeriğin ya da davranışın niteliğidir; komşu dal ise bir kişi veya söz hakkında bu yönde hüküm verme işlemidir.","focus_only":"Doğruluğa aykırı sözün veya davranışın kendisini bildirir.","gloss":"yalan ile yalan sayma ayrımı","neighbor_only":"Bir sözü yalan sayma, birini yalancı bulma veya ona yalancılık yükleme işlemini bildirir.","neighbor_ref":"root_001290/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da doğruluk ile gerçeğe aykırılık arasındaki değerlendirme alanındadır."},{"boundary_match":"partial","distinction":"Odak dal genel doğruluğa aykırılıktır; komşu dal bunun daha ağır, saptırılmış veya başkalarını yanlış yöne sevk eden türünü belirginleştirir.","focus_only":"Sıradan ölçekteki söz ve davranış yalanlarını da kapsar.","gloss":"yalan ile saptırıcı büyük yalan","neighbor_only":"Doğrudan sapmış, büyük veya başkalarını yanlış yöne çeken ağır bir yalan alanını da öne çıkarır.","neighbor_ref":"root_000041/B002","relation_type":"near_synonym","shared_zone":"İki dal da doğruluğa aykırı söz ve aldatıcı içerik alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal söz ve davranıştaki genel doğruluğa aykırılıktır; komşu dal özellikle bilgi yerine tahmine dayanarak asılsız söz üretmeyi de içerir.","focus_only":"Söz dışındaki davranışlarda görülen doğruluğa aykırılığı da kapsar.","gloss":"yalan ile bilgisizce söyleme","neighbor_only":"Bilgiye dayanmadan tahmin yürütme ve doğrulanmamış söz söyleme alanını da kapsar.","neighbor_ref":"root_000403/B002","relation_type":"near_synonym","shared_zone":"Gerçek dışı veya dayanaksız söz söyleme bağlamlarında iki anlam birbirine yaklaşır."},{"boundary_match":"partial","distinction":"Odak dal genel yalan niteliğidir; komşu dal yalanı özellikle haktan sapma, yalancı tanıklık ve batıllık çevresinde örgütler.","focus_only":"Her türlü sözsel veya davranışsal doğruluğa aykırılığı kapsar.","gloss":"genel yalan ile haktan sapmış söz","neighbor_only":"Yalancı tanıklık, haktan sapma ve batıl sayılan nesneler gibi özel alanlara uzanır.","neighbor_ref":"root_000654/B002","relation_type":"near_neighbor","shared_zone":"İki dal da gerçek ve hakikate aykırı söz alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal doğruluğa aykırılığı temel alır; komşu dal ise sözün kesinlik ve güven düzeyine odaklanır, bu nedenle her kuşkulu aktarım yalan değildir.","focus_only":"Sözün ya da davranışın doğruluğa aykırı olmasını doğrudan bildirir.","gloss":"yalan ile kuşkulu aktarım","neighbor_only":"Kesinlik bulunmadan aktarılan, kuşkulu veya doğruluğu güven vermeyen sözü de kapsar.","neighbor_ref":"root_000633/B001","relation_type":"near_neighbor","shared_zone":"Kuşkulu bir iddianın gerçek dışı çıkması durumunda iki alan kesişebilir."}],"source_phrase_ar":"الكذب خلاف الصدق (maqayis;jamhara); الكذاب لغة في الكذب (ayn); كذب كذبا فهو كاذب وكذاب وكذوب (sihah); يقال في المقال والفعال (mufradat)","source_summary":"Kaynaklar, doğruluğa aykırılığı ortak çekirdek sayar; kullanım alanını söz ve davranış olarak verir ve bu niteliği taşıyan kişiye yönelik adlandırmaları aynı anlam çevresinde toplar.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الكذب في القول والفعل، ووصف صاحبه بالكاذب والكذاب والكذوب، وجمع الأكاذيب والمكاذب","what_is_not_ar":"لا يدخل فيه فعل التكذيب والنسبة إلى الكذب، ولا إغراء كذب عليك، ولا الألفاظ الاصطلاحية الخاصة بالحملة واللبن والثوب"},"support_links":[]},{"boundary":"Dal yalan üretmeyi değil, kişi veya söz hakkında yalan hükmü vermeyi ve belirli türevlerde bu hükmü bulguya dayandırmayı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001290/B002","candidate_links":[{"candidate_id":"cand_e6a2e5a4c624472700f9","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:9:1:2","qac_word_ref":"92:9:1","surface_ar":"كَذَّبَ"}],"gloss":"yalan sayma veya yalancı bulma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya söz, yalan olduğu söylenerek doğruluk bakımından olumsuz değerlendirilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli türemiş biçimler, kişiyi yalancı bulmayı veya onun yalanını ortaya çıkarmayı bildirir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hüküm verme çekirdeği ile belirli türevlerdeki bulma ve açığa çıkarma ayrımını birlikte karşılar.","boundary_detail":"Dal yalan üretmeyi değil, kişi veya söz hakkında yalan hükmü vermeyi ve belirli türevlerde bu hükmü bulguya dayandırmayı kapsar.","branch_image_ar":"نسبة الشيء أو صاحبه إلى الكذب","concept_gloss":"yalan sayma veya yalancı bulma","contextual_glosses":[{"applicability":"Bir sözün veya kişinin söylediğinin yalan olduğunu bildiren bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiyi yalancı bulma ve yalanını ortaya çıkarma sonucunu tek başına göstermez.","preserves":"Kişi veya söz hakkında yalan hükmü verme işlemini korur."},"facet_ids":["F001"],"text":"yalanlamak","usage_role":"contextual"},{"applicability":"Değerlendirme sonucunda bir kişinin yalan söylediğinin anlaşıldığı türemiş biçimler için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir sözü doğrudan yalan sayma ve muhataba yalan söylediğini bildirme işlemini kapsamaz.","preserves":"Kişiyi yalancı bulma veya yalanını açığa çıkarma sonucunu korur."},"facet_ids":["F002"],"text":"yalancı bulmak","usage_role":"contextual"}],"definition":"Bir kişiyi veya sözü yalanla ilişkilendirerek yalan olduğunu söylemektir. Bazı türemiş biçimlerde işlem, kişiyi yalancı bulma ya da yalanını ortaya çıkarma sonucunu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya söz, yalan olduğu söylenerek doğruluk bakımından olumsuz değerlendirilir."},{"facet_id":"F002","role":"source_variant","statement":"Belirli türemiş biçimler, kişiyi yalancı bulmayı veya onun yalanını ortaya çıkarmayı bildirir."}],"identity_rationale":"Kaynak ifadesi tek bir işlemi değil, birbirine bağlı iki işlemi içerir: bir kişiyi veya sözü yalanla nitelemek ve bazı türemiş biçimlerde kişiyi yalancı bulmak ya da yalanını açığa çıkarmak. Dal korunabilir, ancak bu ayrım tek bir genel 'yalan yükleme' anlatımı içinde eritilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yalanlama; yalan sayma"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"birini yalancı saymak veya ona yalan söylediğini bildirmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini yalancı bulmak veya yalanını ortaya çıkarmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"seni yalancı saymıyorum"}],"lexicalization_note":"Tanım, türemiş ve nesne alan biçimlerinin farklı işlemlerini ayırır; bunlardan hiçbiri yalın biçimin genel yalan anlamı olarak sunulmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalanın kendisi, genel suçlama ve benzer isnat işlemleriyle sınırı gösteren dört aday seçildi, daha uzak söz ve özel kalıp alanları yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalan olduğuna hükmetme işlemidir; komşu dal ise bu hükmün konusu olan gerçeğe aykırı söz veya davranıştır.","focus_only":"Bir kişi veya söz hakkında yalan hükmü verme işlemini bildirir.","gloss":"yalan sayma ile yalan ayrımı","neighbor_only":"Doğruluğa aykırı sözün veya davranışın kendisini bildirir.","neighbor_ref":"root_001290/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da doğruluk değerlendirmesi ve yalan alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal yalnız doğruluk ve yalan eksenindeki hükme bağlıdır; komşu dalın suçlama ve kuşku alanı daha geniştir.","focus_only":"Yüklenen nitelik özellikle yalan söyleme veya sözün yalan olmasıdır.","gloss":"yalancılıkla niteleme ile suçlama","neighbor_only":"Kişiye herhangi bir suçlama ya da kuşku iliştirmeyi, hatta onda bulunmayan olumlu bir niteliği yakıştırmayı kapsayabilir.","neighbor_ref":"root_001607/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir kişi hakkında olumsuz bir niteleme veya iddia yöneltme işlemini içerebilir."},{"boundary_match":"field_only","distinction":"İşlemin yapısı benzerdir, ancak odak dalın hükmü yalanla, komşu dalın hükmü hırsızlıkla sınırlıdır; anlam çekirdekleri birbirinin yerine geçmez.","focus_only":"Kişiyi yalancılıkla veya sözünü yalan olmakla niteler.","gloss":"farklı fiillerle suçlayıcı niteleme","neighbor_only":"Kişiyi hırsızlık yapmakla niteler.","neighbor_ref":"root_000700/B005","relation_type":"same_field","shared_zone":"İki dal da bir kişiye belirli bir olumsuz eylemi yükleyen dilsel işlemlerdir."},{"boundary_match":"partial","distinction":"Odak dal doğruluk hakkında verilen hükümdür; komşu dal ise gerçekleşmemiş belirli bir eylemin kişiye isnat edilmesidir.","focus_only":"Bir kişiyi genel olarak yalancı sayabilir veya belirli bir sözü yalanlayabilir.","gloss":"yalan sayma ile yapılmamışı yükleme","neighbor_only":"Kişinin yapmadığı belirli bir içme eylemini ona yükleme iddiasıyla sınırlıdır.","neighbor_ref":"root_000783/B010","relation_type":"near_neighbor","shared_zone":"Bir kişiye gerçekleşmemiş bir eylem yüklenince bu iddiayı yalanlama bağlamında iki alan kesişir."}],"source_phrase_ar":"كذبت فلانا نسبته إلى الكذب وأكذبته وجدته كاذبا (maqayis); كذبته جعلته كاذبا (ayn); كذبت بالحديث كذابا وتكذيبا (jamhara); أكذبت الرجل ألفيته كاذبا وكذبته إذا قلت له كذبت (sihah); كذبته نسبته إلى الكذب (mufradat)","source_summary":"Kaynaklar, birini ya da bir sözü yalanla niteleme konusunda birleşir; aynı toplu kanıt, ayrı bir türemiş biçimde kişiyi yalancı bulma veya yalanı açığa çıkarma yorumunu da taşır.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه كذبت فلانا، وأكذبته، والتكذيب، والمكاذبة، ولا مكذبة بمعنى لا أكذبك، وقراءة لا يكذبونك في معنى لا يجدونك كاذبا أو لا ينسبونك إلى الكذب","what_is_not_ar":"لا يدخل فيه إنشاء الكذب نفسه، ولا الإغراء بقول كذب عليك، ولا كذب الحملة أو اللبن"},"support_links":["sup_6bba7cd5b4303ef8a3d7"]},{"boundary":"Dal, belirli kalıbın 'sana düşer, onu yap' anlamıyla sınırlıdır; yalın köke genel bir zorunluluk veya özendirme anlamı vermez.","branch_kind":"collocation","branch_ref":"root_001290/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:9:1:2","qac_word_ref":"92:9:1","surface_ar":"كَذَّبَ"}],"gloss":"onu üstlen; sana düşer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalıp, söz konusu işin muhataba düşen bir yükümlülük olduğunu bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı kalıp, muhatabı o işi üstlenmeye yönelten güçlü bir özendirme olarak kullanılabilir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıbın hem yükümlülük bildiren hem de eyleme yönelten iki işlevini birlikte veren karşılıktır.","boundary_detail":"Dal, belirli kalıbın 'sana düşer, onu yap' anlamıyla sınırlıdır; yalın köke genel bir zorunluluk veya özendirme anlamı vermez.","branch_image_ar":"كذب عليك بمعنى الزم وعليك به","concept_gloss":"onu üstlen; sana düşer","contextual_glosses":[{"applicability":"Kalıbın yükümlülük bildiren yönünün öne çıktığı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Buyruk ve güçlü özendirme tonunu tek başına tam olarak göstermez.","preserves":"İşin muhataba düşen bir yükümlülük oluşunu açıkça korur."},"facet_ids":["F001"],"text":"onu yapmalısın","usage_role":"contextual"},{"applicability":"Kalıbın muhatabı işe yönelten özendirme işlevinin baskın olduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşin önceden var olan bir yükümlülük olarak muhataba düştüğünü zorunlu biçimde bildirmez.","preserves":"Muhatabı söz konusu işi yapmaya yönelten güçlü çağrıyı korur."},"facet_ids":["F002"],"text":"haydi, onu üstlen","usage_role":"contextual"}],"definition":"Belirli bir kalıp içinde, bir şeyin kişiye düşen bir yükümlülük olduğunu bildirmek veya kişiyi onu yapmaya yöneltmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalıp, söz konusu işin muhataba düşen bir yükümlülük olduğunu bildirir."},{"facet_id":"F002","role":"extension","statement":"Aynı kalıp, muhatabı o işi üstlenmeye yönelten güçlü bir özendirme olarak kullanılabilir."}],"identity_rationale":"Kaynak ifadesi belirli bir kalıbı zorunluluk bildirme ve bir işi yapmaya yöneltme anlamlarıyla açıklar. Bu anlamın yalan söylemeyle doğrudan bir bileşeni yoktur ve yalnız söz konusu kalıp içinde geçerlidir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"şunu üstlen; sana düşer veya onu yapmalısın"}],"lexicalization_note":"Tanım yalnızca verilen kalıplaşmış söyleyişi açıklar; zorunluluk ve yöneltme anlamları yalın biçime taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yükümlülük, özendirme ve bağlayıcılıkla doğrudan sınır kuran üç aday seçildi, yalnızca çalışma azmi veya uzak kök dallarıyla ilişkili adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli kalıbın 'sana düşer, onu yap' değeridir; komşu dal genel emir ve buyurma sistemidir.","focus_only":"Zorunluluk ile güçlü yöneltmeyi yalnız belirli bir kalıplaşmış söyleyişte birleştirir.","gloss":"kalıplaşmış yükümlülük ile genel buyruk","neighbor_only":"Genel buyruk, yasak karşıtı emir ve buyruğa uyma alanlarını kapsar.","neighbor_ref":"root_000051/B002","relation_type":"near_synonym","shared_zone":"İki dal da muhataptan bir eylemi gerçekleştirmesini isteme veya bunu gerekli kılma alanındadır."},{"boundary_match":"partial","distinction":"Odak dal yükümlülük bildirimini de taşır ve belirli bir kalıba bağlıdır; komşu dalın çekirdeği genel teşvik ve kışkırtmadır.","focus_only":"Bir işin muhataba düşen yükümlülük olduğunu da bildirebilir.","gloss":"üstlenmeye yöneltme ile kışkırtma","neighbor_only":"Özellikle çatışmaya yönelik kışkırtma, teşvik ve harekete geçirme anlamlarını kapsar.","neighbor_ref":"root_000309/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da muhatabı bir eyleme kuvvetle yöneltme işlevinde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal kalıplaşmış bir çağrı ve yükümlülük bildirimidir; komşu dal dışsal bir hüküm veya güçle bağlayıcılık kurma işlemidir.","focus_only":"Söyleyiş yoluyla muhatabı işi üstlenmeye çağırır.","gloss":"sözel yöneltme ile bağlayıcı kılma","neighbor_only":"Bir şeyi hüküm, kanıt, yönetim veya zor kullanmayla kişiye bağlayıp kaçınılmaz kılar.","neighbor_ref":"root_001354/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir işin kişi için gerekli veya bağlayıcı hale gelmesi alanında kesişir."}],"source_phrase_ar":"كذب عليك كذا بمعنى الإغراء أي عليك به أو قد وجب عليك (maqayis); كذب عليكم الحج أي وجب عليكم ودونكم الحج (ayn); كذب عليك كذا وكذا في معنى الإغراء (jamhara); كذب عليكم الحج أي وجب (sihah); كذب عليك الحج قيل معناه وجب فعليك به (mufradat)","source_summary":"Kaynaklar bu kalıplaşmış söyleyişi, bir işin muhataba düşmesi ve muhatabın o işi yapmaya yöneltilmesi anlamlarında ortaklaşa açıklar.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه كذب عليك الحج والجهاد والعسل ونحوها إذا أريد الوجوب أو الإغراء أو دونك الشيء","what_is_not_ar":"لا يدخل فيه الإخبار بالكذب، ولا تكذيب المخاطب، ولا كذب الحملة أو اللبن"},"support_links":[]},{"boundary":"Anlam yalnız saldırı hamlesi bağlamında ve olumlu-olumsuz biçimlerin karşıtlığıyla geçerlidir; genel yalan veya genel cesaret anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001290/B004","candidate_links":[{"candidate_id":"cand_6a25b1fbe91c2776e086","lane":"macro"},{"candidate_id":"cand_371579ef487deedf8019","lane":"macro"},{"candidate_id":"cand_0968a5887fd224d0d990","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:9:1:2","qac_word_ref":"92:9:1","surface_ar":"كَذَّبَ"}],"gloss":"hamlede duraksamak; olumsuzda sonuna kadar ilerlemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olumlu kalıp, saldırıya geçtikten sonra durmayı, geri kalmayı veya korkaklık göstermeyi bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olumsuz kalıp, saldırganın durmadan ilerleyerek vuruşa kadar hamleyi sürdürdüğünü bildirir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Savaş hamlesine bağlı olumlu duraksama ile olumsuz kalıptaki kesintisiz ilerlemeyi birlikte karşılar.","boundary_detail":"Anlam yalnız saldırı hamlesi bağlamında ve olumlu-olumsuz biçimlerin karşıtlığıyla geçerlidir; genel yalan veya genel cesaret anlamı değildir.","branch_image_ar":"صدق الحملة أو كذبها","concept_gloss":"hamlede duraksamak; olumsuzda sonuna kadar ilerlemek","contextual_glosses":[{"applicability":"Saldırıya başladıktan sonra geri duran veya korkaklık gösteren kişi için olumlu kalıpta uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Olumsuz kalıbın durmaksızın ilerleyip vuruşa ulaşma anlamını kapsamaz.","preserves":"Hamleyi tamamlamadan geri durma ve cesaret yitirme yönünü korur."},"facet_ids":["F001"],"text":"hamleden caymak","usage_role":"contextual"},{"applicability":"Olumsuz kalıpta saldırganın vuruşa kadar ilerlemeyi sürdürdüğü bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Olumlu kalıptaki duraksama ve korkaklık anlamını kapsamaz.","preserves":"Hamlede durmama, korkmama ve saldırıyı vuruşa kadar sürdürme yönünü korur."},"facet_ids":["F002"],"text":"geri durmadan saldırmak","usage_role":"contextual"}],"definition":"Bir saldırı hamlesinde geri durup hamleyi tamamlamamak veya korkaklık göstermektir; olumsuz kalıpta ise durmadan ilerleyip vuruncaya kadar hamleyi sürdürmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olumlu kalıp, saldırıya geçtikten sonra durmayı, geri kalmayı veya korkaklık göstermeyi bildirir."},{"facet_id":"F002","role":"specialization","statement":"Olumsuz kalıp, saldırganın durmadan ilerleyerek vuruşa kadar hamleyi sürdürdüğünü bildirir."}],"identity_rationale":"Kaynak ifadesi savaş hamlesindeki iki karşıt kalıbı birlikte verir: olumlu biçim hamlede durma, geri çekilme veya korkaklık; olumsuz biçim ise durmadan ilerleyip vuruşa ulaşmadır. Dalın kimliği bu kutuplu kalıp düzenine uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"saldırıya geçti ama duraksadı veya korktu"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"saldırıya geçti ve vuruncaya kadar durmadı; korkmadı"}],"lexicalization_note":"Tanım savaş hamlesine bağlı iki kalıbı korur; duraksama ve kararlılıkla ilerleme anlamları yalın biçime genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hamlede durma, saldırının kendisi, cesaret ve kesintisiz hamlenin sonucu ile doğrudan sınır kuran dört aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir hamlenin seyri ve onun olumsuz karşıt kalıbıdır; komşu dal kişinin daha genel korkaklık niteliğidir.","focus_only":"Başlatılmış bir saldırı hamlesinin sürdürülüp sürdürülmediğini kalıp içinde değerlendirir.","gloss":"hamlede geri durma ile korkaklık","neighbor_only":"Kişinin genel olarak atılganlıktan kesilmiş ve korkak oluşunu betimler.","neighbor_ref":"root_001150/B008","relation_type":"near_neighbor","shared_zone":"Saldırıya devam etmeme, geri kalma ve korkaklık bağlamlarında iki alan kesişir."},{"boundary_match":"field_only","distinction":"Odak dal saldırının sürdürülme niteliğini bildirir; komşu dal saldırı ve koşu hareketinin kendisidir.","focus_only":"Hamlenin duraksama veya sonuna kadar sürme bakımından sonucunu değerlendirir.","gloss":"hamlenin seyri ile hücum eylemi","neighbor_only":"Düşmana saldırma, hücum etme ve koşma eyleminin kendisini bildirir.","neighbor_ref":"root_000782/B003","relation_type":"same_field","shared_zone":"İki dal da savaşta düşmana yönelen saldırı hamlesi alanındadır."},{"boundary_match":"partial","distinction":"Odak dal belirli saldırı kalıbında gerçekleşen davranışı değerlendirir; komşu dal daha genel bir cesaret ve atılganlık niteliğidir.","focus_only":"Olumlu ve olumsuz kalıplarla tek bir hamlede durma ya da sürdürme karşıtlığını kurar.","gloss":"hamleyi sürdürme ile cesaret","neighbor_only":"Genel cesaret, atılganlık ve düşmana doğru öne çıkma niteliğini bildirir.","neighbor_ref":"root_001207/B006","relation_type":"near_neighbor","shared_zone":"Hamleyi korkmadan sürdürme bağlamında iki anlam birbirine yaklaşır."},{"boundary_match":"partial","distinction":"Odak dal hamlenin kesintisiz sürmesini yeterli görür; komşu dal buna düşmanı yenme sonucunu da ekler.","focus_only":"Hamlede durma ile durmadan sürdürme karşıtlığını, zafer şartı aramadan bildirir.","gloss":"kesintisiz hamle ile yenilgiye uğratma","neighbor_only":"Kesintisiz bir saldırıyla karşı tarafı yenme sonucunu özellikle içerir.","neighbor_ref":"root_000003/B007","relation_type":"near_neighbor","shared_zone":"Duraksamadan yapılan saldırı hamlesi iki dalın ortak sahnesidir."}],"source_phrase_ar":"حمل فلان ثم كذب أي لم يصدق في الحملة (maqayis); حمل فلان على فلان فما كذب حتى طعن أو ضرب أي ما وقف (jamhara); حمل فلان فما كذب أي ما جبن (sihah); حمل فلان على قرنه فكذب (mufradat)","source_summary":"Kaynaklar saldırı hamlesini sürdürmeme ile korkaklık arasında bağ kurar; olumsuz kalıp ise durmayıp vuruşa kadar ilerleme anlamını verir.","sources":["MQ","JA","SI","MU"],"what_is_ar":"يدخل فيه كذب في الحملة إذا لم يصدقها أو جبن، ونفي الكذب عن الحملة إذا مضى فيها ولم يقف حتى يطعن أو يضرب","what_is_not_ar":"لا يدخل فيه الكذب في الخبر، ولا الإغراء، ولا وقوف الوحشي بعد شوط"},"support_links":["sup_7721baf86920745c6e5a","sup_e0eb26ca9d539070b61d","sup_f32e65bbafce1a920551"]},{"boundary":"Dal, 'yapmakta gecikmedi' değerindeki kalıpla sınırlıdır; genel hız, acele veya yalan anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001290/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:9:1:2","qac_word_ref":"92:9:1","surface_ar":"كَذَّبَ"}],"gloss":"gecikmeden yapmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, belirtilen işi yapmadan önce beklemez veya oyalanmaz."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Beklememenin sonucu, işin gecikmeden gerçekleştirilmesidir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıbın hem oyalanmama aşamasını hem de işi gecikmeden gerçekleştirme sonucunu özlü biçimde karşılar.","boundary_detail":"Dal, 'yapmakta gecikmedi' değerindeki kalıpla sınırlıdır; genel hız, acele veya yalan anlamı değildir.","branch_image_ar":"ما كذب أن فعل أي ما لبث","concept_gloss":"gecikmeden yapmak","contextual_glosses":[{"applicability":"Söz konusu işin beklenmeden gerçekleştiği geçmiş zaman anlatımlarında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Oyalanmama aşamasını ve işin gecikmeden gerçekleşmesini doğal kullanımda korur."},"facet_ids":["F001","F002"],"text":"hemen yaptı","usage_role":"contextual"}],"definition":"Belirli bir olumsuz kalıp içinde, bir kişinin söz konusu işi yapmakta oyalanmadığını ve gecikmeden yaptığını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, belirtilen işi yapmadan önce beklemez veya oyalanmaz."},{"facet_id":"F002","role":"extension","statement":"Beklememenin sonucu, işin gecikmeden gerçekleştirilmesidir."}],"identity_rationale":"Kaynak ifadesi yalnız belirli bir olumsuz kalıp içinde kişinin bir işi yapmakta oyalanmadığını ve gecikmediğini bildirir. Geçici dal çerçevesi bu yapıyı ve anlamı doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yapmakta gecikmedi; hemen yaptı"}],"lexicalization_note":"Tanım yalnız verilen olumsuz kalıbın gecikmeme anlamını açıklar; hız ve çabukluk yalın kökün anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gecikmeme, ilk anda yapma ve genel acele arasındaki sınırı en iyi gösteren üç aday seçildi, yalnız zaman veya tekrar alanını paylaşan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız kalıplaşmış gecikmeme anlamıdır; komşu dal benzer kalıbın yanında koşma hızına ilişkin ayrı bir alan da taşır.","focus_only":"Gecikmemeyi yalnız belirli bir 'yapmakta oyalanmadı' kalıbında bildirir.","gloss":"gecikmeme ile az bekleme","neighbor_only":"Ayrı bir kullanımda koşmanın görece hızlı oluşunu da kapsar.","neighbor_ref":"root_000973/B009","relation_type":"near_synonym","shared_zone":"Bir işi yapmakta az bekleme veya hiç oyalanmama anlamında iki dal büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal bekleme süresinin yokluğuna odaklanır; komşu dal eylemin durumun ilk anındaki oluşunu ayrıca şart koşar.","focus_only":"Bir işi yapmak öncesindeki gecikmenin bulunmadığını kalıplaşmış biçimde bildirir.","gloss":"gecikmeden yapma ile ilk anda yapma","neighbor_only":"Eylemin ilk anda, durum henüz yatışmadan veya olayın başlangıç itkisiyle yapılmasını vurgular.","neighbor_ref":"root_001185/B002","relation_type":"near_synonym","shared_zone":"Bir eylemin beklenmeden ve hemen gerçekleşmesi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal yalnız gecikmenin yokluğunu bildirir; komşu dal hızlandırma, öne alma ve vaktinden önce isteme gibi ek yönler taşır.","focus_only":"Belirli bir işin yapılmasında gecikme olmadığını bildirir.","gloss":"gecikmeme ile acele etme","neighbor_only":"Bir şeyi vaktinden önce isteme, öne alma ve genel acele ettirme alanlarını kapsar.","neighbor_ref":"root_000987/B001","relation_type":"near_neighbor","shared_zone":"İşin kısa sürede veya beklenmeden yapılması bağlamında iki anlam kesişebilir."}],"source_phrase_ar":"ما كذب فلان أن فعل كذا أي ما لبث (maqayis;sihah)","source_summary":"Kaynakların ortak açıklaması, belirli kalıbın kişinin bir işi yapmakta beklemediğini ve gecikmediğini bildirmesidir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه قولهم ما كذب فلان أن فعل كذا إذا لم يلبث ولم يتأخر","what_is_not_ar":"لا يدخل فيه الكذب في الخبر، ولا وجوب كذب عليك، ولا كذب اللبن"},"support_links":[]},{"boundary":"Anlam yalnız dişi devenin sütüne ilişkin kalıpta, sütün kaybolması veya beklenen süre boyunca devam etmemesiyle sınırlıdır.","branch_kind":"collocation","branch_ref":"root_001290/B006","candidate_links":[{"candidate_id":"cand_490d0e30ea938d504e61","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:9:1:2","qac_word_ref":"92:9:1","surface_ar":"كَذَّبَ"}],"gloss":"sütün kesilmesi veya beklenenden önce tükenmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi devenin sütü gider veya kesilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir açıklamada süt bir süre sürecek sanılır, fakat bu beklentinin tersine devam etmez."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi devenin sütüne bağlı kaybolma çekirdeğini ve devam beklentisinin boşa çıkmasını birlikte karşılar.","boundary_detail":"Anlam yalnız dişi devenin sütüne ilişkin kalıpta, sütün kaybolması veya beklenen süre boyunca devam etmemesiyle sınırlıdır.","branch_image_ar":"كذب لبن الناقة إذا ذهب ولم يدم","concept_gloss":"sütün kesilmesi veya beklenenden önce tükenmesi","contextual_glosses":[{"applicability":"Sütün artık gelmediği ve önceki üretimin sona erdiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sütün süreceği beklentisinin özellikle boşa çıkmış olduğunu tek başına bildirmez.","preserves":"Dişi devenin sütünün gitmesi veya sona ermesi çekirdeğini korur."},"facet_ids":["F001"],"text":"sütü kesildi","usage_role":"contextual"},{"applicability":"Sütün belirli bir süre devam edeceği beklentisinin gerçekleşmediği açıklayıcı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sütün devamına ilişkin beklentiyi ve beklenenden önce kesilmesini birlikte korur."},"facet_ids":["F001","F002"],"text":"sütü umulduğu kadar sürmedi","usage_role":"explanatory"}],"definition":"Dişi devenin sütünün kaybolması veya bir süre devam edeceği sanıldığı halde beklenenden önce kesilmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi devenin sütü gider veya kesilir."},{"facet_id":"F002","role":"source_variant","statement":"Bir açıklamada süt bir süre sürecek sanılır, fakat bu beklentinin tersine devam etmez."}],"identity_rationale":"Kaynak ifadesi dişi devenin sütünün gitmesini ortak çekirdek olarak verir; toplu kanıttaki ek açıklama, bir süre devam edeceği sanılan sütün beklenenden önce kesilmesini belirtir. Geçici çerçeve iki yönü de doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"dişi devenin sütü kesildi veya umulduğu kadar sürmedi"}],"lexicalization_note":"Tanım yalnız dişi devenin sütünü konu alan kalıba bağlıdır; genel tükenme veya genel beklenti boşa çıkması anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; süt kesilmesi, geri dönüş beklentisi ve süt bolluğu eksenini açıklayan üç aday seçildi, yalnız başka sıvıları veya hayvan özelliklerini paylaşan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dişi devenin sütüne ve kimi kullanımda boşa çıkan süreklilik beklentisine bağlıdır; komşu dal süt veriminin azalmasını ve yağmuru da kapsar.","focus_only":"Dişi devenin sütünün gitmesini ve beklenen süre boyunca devam etmemesini bildirir.","gloss":"sütün beklenmedik kesilmesi ile verimin azalması","neighbor_only":"Sütün azalmasını veya kesilmesini yağmurun azalması ve kesilmesiyle aynı anlam alanında kapsar.","neighbor_ref":"root_000305/B005","relation_type":"near_synonym","shared_zone":"Sütün azalması veya bütünüyle kesilmesi iki dalın doğrudan ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal gerçekleşen kaybı ve boşa çıkan devam beklentisini anlatır; komşu dal kayıptan sonraki geri dönüş umuduna odaklanır.","focus_only":"Sütün fiilen gittiğini veya beklenen süre boyunca devam etmediğini bildirir.","gloss":"sütün kesilmesi ile geri dönme umudu","neighbor_only":"Sütü kesilen ya da sütü kuşkulu olan hayvanda sütün geri dönmesi umudunu bildirir.","neighbor_ref":"root_001015/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da kesilmiş veya belirsiz hale gelmiş süt verimi durumunu konu alır."},{"boundary_match":"opposed","distinction":"Odak dal süt veriminin sona eren kutbundadır; komşu dal aynı alanın bol ve güçlü verim kutbundadır.","focus_only":"Sütün kaybolmasını, kesilmesini veya beklenenden az sürmesini bildirir.","gloss":"süt kesilmesi ile süt bolluğu","neighbor_only":"Dişi devenin süt bakımından çok verimli ve bol oluşunu bildirir.","neighbor_ref":"root_000200/B005","relation_type":"polarity_pair","shared_zone":"İki dal da dişi devenin süt veriminin durumu üzerinde ortak bir nicelik ekseni kurar."}],"source_phrase_ar":"كذب لبن الناقة ذهب وفيه نظر وقياسه صحيح (maqayis); كذب لبن الناقة أي ذهب (sihah); كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم (mufradat)","source_summary":"Toplu kanıt sütün gitmesi çekirdeğinde birleşir; bunun yanında, devam edeceği sanılan sütün beklenen süreyi tamamlamadan kesilmesi biçiminde daha ayrıntılı bir yorum da verir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه كذب لبن الناقة إذا ذهب أو ظن دوامه فلم يدم","what_is_not_ar":"لا يدخل فيه كذب الخبر، ولا كذب الحملة، ولا كذب عليك في الإغراء"},"support_links":["sup_91fec92a5b011059f45b"]},{"boundary":"Dal yalnız yaban hayvanının koşma, durma ve arkasına bakma dizisine bağlıdır; genel durma ya da genel koşu anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001290/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:9:1:2","qac_word_ref":"92:9:1","surface_ar":"كَذَّبَ"}],"gloss":"koşup arkasına bakmak için durmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yaban hayvanı önce belirli bir mesafe koşar, ardından hareketini durdurur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Durmanın amacı hayvanın arkasında kalan yere veya şeye bakmasıdır."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaban hayvanını, koşudan sonraki durmayı ve durmanın geriye bakma amacını birlikte karşılar.","boundary_detail":"Dal yalnız yaban hayvanının koşma, durma ve arkasına bakma dizisine bağlıdır; genel durma ya da genel koşu anlamı değildir.","branch_image_ar":"كذب الوحشي إذا جرى ثم وقف","concept_gloss":"koşup arkasına bakmak için durmak","contextual_glosses":[{"applicability":"Yaban hayvanının hareket dizisinin anlatı içinde doğal bir cümleyle çevrildiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önce koşmayı, sonra durup geride kalana bakmayı doğal anlatım sırasıyla korur."},"facet_ids":["F001","F002"],"text":"bir süre koştu, sonra dönüp baktı","usage_role":"contextual"}],"definition":"Bir yaban hayvanının belirli bir mesafe koştuktan sonra arkasında ne olduğunu görmek için durmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yaban hayvanı önce belirli bir mesafe koşar, ardından hareketini durdurur."},{"facet_id":"F002","role":"specialization","statement":"Durmanın amacı hayvanın arkasında kalan yere veya şeye bakmasıdır."}],"identity_rationale":"Tek kaynaklı ifade, yaban hayvanının belirli bir mesafe koşmasından sonra arkasına bakmak için durduğu aşamalı hareketi eksiksiz biçimde tanımlar. Geçici dal çerçevesi katılımcıyı, hareket sırasını ve amacı korur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yaban hayvanı bir mesafe koşup arkasına bakmak için durdu"}],"lexicalization_note":"Tanım yalnız yaban hayvanını özne alan kalıba ve belirtilen hareket dizisine bağlıdır; yalın biçime bir hareket anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hayvanda hareketin kesilmesi, ileri hareket ve bakış amacıyla doğrudan karşılaştırma sağlayan dört aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın katılımcısı yaban hayvanıdır ve amaç arkasına bakmaktır; komşu dal av köpeğinin ilgisini veya takibini kesmesine odaklanır.","focus_only":"Yaban hayvanı koşusunu geriye bakmak amacıyla durdurur.","gloss":"koşudan sonra durma ile avdan vazgeçme","neighbor_only":"Köpek avını yakaladıktan sonra gevşer, ondan döner veya başka şeyle oyalanır.","neighbor_ref":"root_001084/B005","relation_type":"near_synonym","shared_zone":"Bir hayvanın koşu veya takip hareketini bir aşamadan sonra kesmesi iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Odak dal belirli bir koşu-sonrası bakış dizisidir; komşu dal daha genel durdurma, kalma ve konaklama ilişkilerini kapsar.","focus_only":"Koşudan sonra özellikle geriye bakmak için gerçekleşen kısa durmayı bildirir.","gloss":"geriye bakmak için durma ile konaklama","neighbor_only":"Binek hayvanını tutmayı, bir yerde kalmayı, inmeyi veya bir kişiye yönelmeyi kapsar.","neighbor_ref":"root_000997/B003","relation_type":"near_neighbor","shared_zone":"Hareket halindeki bir canlının ilerlemeyi kesmesi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal koşu sonrasındaki durmayı temel alır; komşu dal kesintisiz ve güçlü ileri hareketi temel alır.","focus_only":"Koşunun ardından hareketin kesilmesini ve geriye bakmayı içerir.","gloss":"koşuyu kesme ile hızla ileri atılma","neighbor_only":"Binek hayvanının hızla ileri atılmasını ve kendini öne fırlatır gibi ilerlemesini bildirir.","neighbor_ref":"root_001209/B005","relation_type":"near_neighbor","shared_zone":"İki dal da hayvanın hızlı ilerleyişini konu alan hareket sahnesindedir."},{"boundary_match":"thematic_only","distinction":"Odak dalın çekirdeği koşu sonrasında durma dizisidir; komşu dal ise önceki bir hareket gerektirmeyen bakış eylemidir.","focus_only":"Bakışı, öncesindeki koşu ve durma dizisinin amacı olarak içerir.","gloss":"hareket dizisi ile dikkatli bakış","neighbor_only":"Baş veya gözleri kaldırarak bir şeye dikkatle bakma eylemini doğrudan bildirir.","neighbor_ref":"root_000256/B008","relation_type":"thematic","shared_zone":"Bir şeyi görmek üzere yöneltilen bakış, iki anlamın aynı sahnede bulunabilen unsurudur."}],"source_phrase_ar":"كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Yaban hayvanı bir mesafe koştuktan sonra arkasına bakmak için durur."}],"source_summary":"Bu özel kullanım tek bir kaynakta, yaban hayvanının koşu sonrasında arkasına bakmak amacıyla durduğu ardışık hareket olarak tanıklanır.","sources":["JA"],"what_is_ar":"يدخل فيه كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه","what_is_not_ar":"لا يدخل فيه كذب الحملة، ولا كذب اللبن، ولا الكذب في القول"},"support_links":[]},{"boundary":"Dal, ilgili yalın biçimin 'kişinin iç benliği' adını taşımasıyla sınırlıdır; kişinin yalan söylemesi veya benliğin aldatıcılığı anlamını içermez.","branch_kind":"bare","branch_ref":"root_001290/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:9:1:2","qac_word_ref":"92:9:1","surface_ar":"كَذَّبَ"}],"gloss":"iç benlik","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, bir yalan niteliği yüklemeden doğrudan kişinin iç benliğini adlandırır."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynak ifadesindeki doğrudan adlandırmayı, yalan söyleme niteliği eklemeden karşılar.","boundary_detail":"Dal, ilgili yalın biçimin 'kişinin iç benliği' adını taşımasıyla sınırlıdır; kişinin yalan söylemesi veya benliğin aldatıcılığı anlamını içermez.","branch_image_ar":"النفس الكذوب","concept_gloss":"iç benlik","contextual_glosses":[{"applicability":"Eski ve tek kaynaklı adlandırmanın modern Türkçede açıklanması gereken bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözcüğün kişiyi içeriden kuran benliği adlandırmasını açık biçimde korur."},"facet_ids":["F001"],"text":"kişinin kendi iç benliği","usage_role":"explanatory"}],"definition":"İlgili sözcüğün, kişideki iç benliği veya kendi olma bilincini doğrudan adlandıran bir isim olarak kullanılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, bir yalan niteliği yüklemeden doğrudan kişinin iç benliğini adlandırır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kaynak ifadesinde bulunmayan yalan söyleme veya aldatma niteliğini benliğe yükler.","collision":"Kişiyi yalan söyleyen biri olarak betimleyen başka daldaki sıfat anlamıyla karışır.","fit":"broadening","loses":null,"preserves":"Benliği konu alan bir adlandırma bulunduğu izlenimini kısmen korur."},"text":"yalancı benlik"}],"identity_rationale":"Kaynak ifadesi iç benliği 'yalancı' diye niteleyen bir söz öbeği kurmaz; ilgili sözcüğü doğrudan iç benliğin adı olarak eşitler. Dal korunabilir, ancak tanım bir ahlak niteliği değil, bağımsız bir adlandırma olarak yeniden çerçevelenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"iç benlik; kişinin kendisi"}],"lexicalization_note":"Tanım sözcüğün yalın biçimde doğrudan iç benliği adlandırmasını verir; başka dallardaki kişi sıfatları veya özel kalıplar bu anlama alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; iç benliği doğrudan adlandıran veya onun işlevini konu alan üç yararlı karşılaştırma seçildi, yalnız kişilik değişimi ve uzak tematik kullanımlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız iç benliği adlandırır; komşu dal iç benliği bedenin yaşamsal özü, kanı ve kalbiyle bir araya getiren daha geniş bir anlam kümesidir.","focus_only":"Tek bir sözcüğün doğrudan iç benlik adı olarak kullanımını bildirir.","gloss":"iç benlik ile yaşam özü","neighbor_only":"İç benliğin yanında kan, yaşam özü ve kalp gibi birbiriyle ilişkili adlandırmaları da kapsar.","neighbor_ref":"root_000187/B004","relation_type":"near_synonym","shared_zone":"Kişinin iç varlığı veya kendisi anlamında iki dal büyük ölçüde örtüşebilir."},{"boundary_match":"partial","distinction":"Odak dal bağımsız iç benlik adıdır; komşu dal bu değeri belirli bir kalıp içinde verir ve ayrıca yakın dost anlamına genişler.","focus_only":"Yalın bir sözcükle kişinin iç benliğini doğrudan adlandırır.","gloss":"iç benlik ile kişinin kendisi","neighbor_only":"Belirli bir soru kalıbında kişinin kendisini, başka kullanımda ise yakın ve seçkin dostu bildirir.","neighbor_ref":"root_000059/B006","relation_type":"near_synonym","shared_zone":"Kişinin kendisini veya iç benliğini gösteren kullanımlarda iki dal örtüşür."},{"boundary_match":"thematic_only","distinction":"Odak dal varlığın adıdır; komşu dal bu varlığa yüklenen süsleme ve yanıltıcı yönlendirme eylemidir.","focus_only":"İç benliği yalnızca bir varlık olarak adlandırır.","gloss":"iç benlik ile benliğin yönlendirmesi","neighbor_only":"İç benliğin veya kötülüğe yönelten bir gücün bir işi süsleyip kişiye çekici göstermesini bildirir.","neighbor_ref":"root_000763/B002","relation_type":"thematic","shared_zone":"İç benlik iki anlamın aynı düşünsel sahnesinde yer alır."}],"source_phrase_ar":"الكذوب النفس (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Sözcük herhangi bir ahlak niteliği eklenmeden doğrudan kişinin iç benliğini adlandırır."}],"source_summary":"Bu yalın adlandırma tek bir kaynakta, ilgili sözcüğün doğrudan kişinin iç benliğiyle eşitlenmesi biçiminde tanıklanır.","sources":["JA"],"what_is_ar":"يدخل فيه إطلاق الكذوب على النفس","what_is_not_ar":"لا يدخل فيه وصف الرجل بالكذاب أو الكذوب، ولا أكاذيب الأخبار"},"support_links":[]},{"boundary":"Dal, boyası veya deseni gerçek dokuma bezemesi sanısı veren kumaşla sınırlıdır; genel yalan, her desenli kumaş veya kişi adı değildir.","branch_kind":"bare","branch_ref":"root_001290/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:9:1:2","qac_word_ref":"92:9:1","surface_ar":"كَذَّبَ"}],"gloss":"dokuma bezemesi sanısı veren boyalı kumaş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, çeşitli boya renkleriyle renklendirilmiş veya yüzeyine desen işlenmiş bir kumaştır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Boya ve desen, kumaşın dokuma yoluyla bezenmiş olduğu izlenimini verir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin kumaş oluşunu, boya veya deseni ve gerçek dokuma bezemesi gibi görünmesini birlikte karşılar.","boundary_detail":"Dal, boyası veya deseni gerçek dokuma bezemesi sanısı veren kumaşla sınırlıdır; genel yalan, her desenli kumaş veya kişi adı değildir.","branch_image_ar":"الكذابة ثوب يكذب بحاله","concept_gloss":"dokuma bezemesi sanısı veren boyalı kumaş","contextual_glosses":[{"applicability":"Kumaş türünün üretim görünüşüyle birlikte açıkça anlatılması gereken bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Boyama veya yüzey deseniyle oluşturulan dokuma bezemesi izlenimini korur."},"facet_ids":["F001","F002"],"text":"dokuma desenli gibi görünen boyalı kumaş","usage_role":"explanatory"}],"definition":"Çeşitli renklerle boyanmış veya desenlenmiş, bu yüzden dokuma yoluyla bezenmiş gibi görünen bir kumaş ya da giysidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, çeşitli boya renkleriyle renklendirilmiş veya yüzeyine desen işlenmiş bir kumaştır."},{"facet_id":"F002","role":"specialization","statement":"Boya ve desen, kumaşın dokuma yoluyla bezenmiş olduğu izlenimini verir."}],"identity_rationale":"Kaynak ifadesi çeşitli renklerle boyanmış veya desenlenmiş bir kumaşı, dokuma yoluyla bezenmiş gibi görünmesi üzerinden tanımlar; bir açıklama bu yanıltıcı görünüşü adlandırmanın gerekçesi yapar. Geçici çerçeve nesneyi ve görünüş ilişkisini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"dokuma bezemesi sanısı veren boyalı veya desenli kumaş"}],"lexicalization_note":"Tanım yalın bir kumaş adını ve onu ayıran görünüş özelliğini verir; genel aldatıcı görünüş anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dokuma bezemesi, renk etkisi, boyama, resimli kumaş ve yüzeyle yanıltma sınırlarını gösteren beş aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal boya veya desenin dokuma bezemesi sanısı vermesine dayanır; komşu dal gerçek dokuma bezemesi ve onun üretimiyle ilgilidir.","focus_only":"Boya veya yüzey deseniyle gerçek dokuma bezemesi varmış izlenimi veren kumaşı adlandırır.","gloss":"bezemeye benzeyen boya ile gerçek dokuma bezemesi","neighbor_only":"Kumaştaki gerçek dokuma bezemesini, kenar süslemesini ve bu işi yapanları kapsar.","neighbor_ref":"root_000340/B004","relation_type":"near_neighbor","shared_zone":"Kumaş yüzeyindeki bezeme görünüşü iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal dokuma bezemesi sanısına dayanır; komşu dal kumaş renginin bakışa göre değişmesine dayanır.","focus_only":"Birden çok boya veya desenle dokunmuş gibi görünen kumaşı bildirir.","gloss":"boyalı desen yanılsaması ile değişken renk görünüşü","neighbor_only":"Bakış açısına göre renkleri değişiyormuş gibi görünen belirli bir kumaş türünü bildirir.","neighbor_ref":"root_001252/B010","relation_type":"near_neighbor","shared_zone":"Renkli bir kumaşın görünüşünün algıda özel bir etki oluşturması iki dalda ortaktır."},{"boundary_match":"field_only","distinction":"Odak dal bezeme sanısı veren tasarlanmış görünüşü adlandırır; komşu dal belirli renkleri ve boyanın düzensiz tutmasını konu alır.","focus_only":"Çok renkli boya veya desenin dokuma bezemesi izlenimi vermesini temel alır.","gloss":"yanıltıcı bezeme ile alacalı boya","neighbor_only":"Sarı boya, belirli bitkisel renkler ve boyanın alacalı ya da iyi tutmamış çıkmasını kapsar.","neighbor_ref":"root_001428/B005","relation_type":"same_field","shared_zone":"Her iki dal da boyanmış kumaşın renk ve yüzey görünüşü alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal üretim biçimini olduğundan farklı gösteren genel bezeme izlenimine dayanır; komşu dal belirli resim motifleriyle tanımlanır.","focus_only":"Boyanmış veya desenlenmiş yüzeyin dokuma bezemesi sanısı vermesini bildirir.","gloss":"bezeme sanısı veren kumaş ile resimli kumaş","neighbor_only":"Üzerinde kule biçimleri veya başka resimler bulunan belirli bir süslü kumaşı bildirir.","neighbor_ref":"root_000101/B005","relation_type":"same_field","shared_zone":"İki dal da yüzeyi resim veya desenle süslenmiş kumaşları konu alır."},{"boundary_match":"thematic_only","distinction":"Odak dal yalnız kumaş ve dokuma bezemesi görünüşüne bağlıdır; komşu dal metal kaplama işleminden genel yanıltıcı gösterime uzanır.","focus_only":"Kumaşta boya veya desenin dokuma bezemesi sanısı uyandırmasını bildirir.","gloss":"kumaş görünüşü ile kaplama yoluyla yanıltma","neighbor_only":"Bir metali altın veya gümüşle kaplamayı ve bir şeyi gerçek niteliğinden farklı göstermeyi bildirir.","neighbor_ref":"root_001458/B005","relation_type":"thematic","shared_zone":"Bir nesnenin yüzey işlemiyle üretim veya madde niteliğinden farklı görünmesi iki alanda ortaktır."}],"source_phrase_ar":"الكذابة ثوب يصبغ بألوان الصبغ كأنه موشي (ayn); الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله (mufradat)","source_summary":"Kaynaklar, çeşitli renklerle boyanıp desenlenen ve böylece dokuma bezemesi varmış gibi görünen bir kumaş üzerinde birleşir; toplu kanıt bu yanıltıcı görünüşü adlandırmanın gerekçesi olarak açıklar.","sources":["AY","MU"],"what_is_ar":"يدخل فيه الكذابة للثوب المصبوغ بألوان أو المنقوش كأنه موشى لأنه يكذب بحاله","what_is_not_ar":"لا يدخل فيه الكذب في القول، ولا التكذيب، ولا أسماء الأشخاص"},"support_links":[]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000058/B001","candidate_links":[{"candidate_id":"cand_6a25b1fbe91c2776e086","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6d0e487065706aa3feea","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The feminine side supplies the other pole without erasing distinction.","root":"ء ن ث","source_ref":"92:3","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000058","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_f32e65bbafce1a920551"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000089/B001","candidate_links":[{"candidate_id":"cand_371579ef487deedf8019","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fbb73ace0bb76cc3d881","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Stinginess supplies the withheld transfer that materially contradicts beneficence.","root":"ب خ ل","source_ref":"92:8","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000089","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7721baf86920745c6e5a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000256/B001","candidate_links":[{"candidate_id":"cand_e6a2e5a4c624472700f9","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b1c4c27ba48a20640112","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Uncovering and appearance make disclosure an event rather than a static property.","root":"ج ل و","source_ref":"92:2","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000256","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6bba7cd5b4303ef8a3d7"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000434/B001","candidate_links":[{"candidate_id":"cand_6a25b1fbe91c2776e086","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6d0e487065706aa3feea","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Measuring and proportioning supply an ordered background for differentiated existence.","root":"خ ل ق","source_ref":"92:3","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000434","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_f32e65bbafce1a920551"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000516/B001","candidate_links":[{"candidate_id":"cand_6a25b1fbe91c2776e086","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6d0e487065706aa3feea","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The masculine side supplies one pole of the explicitly paired differentiation.","root":"ذ ك ر","source_ref":"92:3","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000516","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_f32e65bbafce1a920551"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000558/B003","candidate_links":[{"candidate_id":"cand_490d0e30ea938d504e61","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_dfd4538c3567906e0d68","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Falling into destruction supplies the event at which the substitute's promise fails.","root":"ر د ي","source_ref":"92:11","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000558","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_91fec92a5b011059f45b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000709/B001","candidate_links":[{"candidate_id":"cand_6a25b1fbe91c2776e086","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6d0e487065706aa3feea","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Purposeful movement toward an object makes striving directional.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000709","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_f32e65bbafce1a920551"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000775/B001","candidate_links":[{"candidate_id":"cand_6a25b1fbe91c2776e086","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6d0e487065706aa3feea","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Scattering supplies the loss of convergence among those directed movements.","root":"ش ت ت","source_ref":"92:4","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000775","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_f32e65bbafce1a920551"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000852/B004","candidate_links":[{"candidate_id":"cand_371579ef487deedf8019","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fbb73ace0bb76cc3d881","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Realizing a promise or deed makes confirmation performative rather than merely verbal.","root":"ص د ق","source_ref":"92:6","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000852","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7721baf86920745c6e5a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001012/B004","candidate_links":[{"candidate_id":"cand_0968a5887fd224d0d990","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9032e9316b3c7ba50544","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Twisting, opposition, and obstruction supply the paradoxical destination of that facilitated motion.","root":"ع س ر","source_ref":"92:10","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001012","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_e0eb26ca9d539070b61d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001028/B002","candidate_links":[{"candidate_id":"cand_371579ef487deedf8019","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fbb73ace0bb76cc3d881","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Handing something over supplies the outward transfer that realizes the good.","root":"ع ط و","source_ref":"92:5","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001028","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7721baf86920745c6e5a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001088/B001","candidate_links":[{"candidate_id":"cand_e6a2e5a4c624472700f9","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b1c4c27ba48a20640112","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A covering that rises over and conceals something supplies the occlusive operation.","root":"غ ش و","source_ref":"92:1","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001088","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6bba7cd5b4303ef8a3d7"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001110/B001","candidate_links":[{"candidate_id":"cand_371579ef487deedf8019","lane":"macro"},{"candidate_id":"cand_490d0e30ea938d504e61","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fbb73ace0bb76cc3d881","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Claimed self-sufficiency supplies the posture that makes relation and gift seem unnecessary.","root":"غ ن ي","source_ref":"92:8","source_word_indices":["4"]},{"hft_ref":"hft_dfd4538c3567906e0d68","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Self-sufficiency supplies the initial claim that no external good is needed.","root":"غ ن ي","source_ref":"92:8","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001110","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7721baf86920745c6e5a","sup_91fec92a5b011059f45b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001110/B002","candidate_links":[{"candidate_id":"cand_490d0e30ea938d504e61","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_dfd4538c3567906e0d68","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Actual sufficiency is explicitly tested and found absent at the decisive moment.","root":"غ ن ي","source_ref":"92:11","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001110","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_91fec92a5b011059f45b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001392/B001","candidate_links":[{"candidate_id":"cand_e6a2e5a4c624472700f9","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b1c4c27ba48a20640112","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Night's darkness supplies the scene in which visibility is withdrawn.","root":"ل ي ل","source_ref":"92:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001392","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6bba7cd5b4303ef8a3d7"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001457/B001","candidate_links":[{"candidate_id":"cand_490d0e30ea938d504e61","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_dfd4538c3567906e0d68","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Accumulated wealth identifies the concrete substitute expected to provide sufficiency.","root":"م و ل","source_ref":"92:11","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001457","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_91fec92a5b011059f45b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001559/B002","candidate_links":[{"candidate_id":"cand_e6a2e5a4c624472700f9","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b1c4c27ba48a20640112","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Day opening through light supplies the contrary condition of visibility.","root":"ن ه ر","source_ref":"92:2","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001559","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6bba7cd5b4303ef8a3d7"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001677/B002","candidate_links":[{"candidate_id":"cand_371579ef487deedf8019","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fbb73ace0bb76cc3d881","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Placing oneself within protection supplies the inward discipline paired with giving.","root":"و ق ي","source_ref":"92:5","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001677","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7721baf86920745c6e5a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001694/B001","candidate_links":[{"candidate_id":"cand_0968a5887fd224d0d990","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9032e9316b3c7ba50544","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Opening into ease supplies the positive path's increasing traversability.","root":"ي س ر","source_ref":"92:7","source_word_indices":["1","2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001694","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_e0eb26ca9d539070b61d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001694/B005","candidate_links":[{"candidate_id":"cand_0968a5887fd224d0d990","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9032e9316b3c7ba50544","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Lightness and compliance in motion make even the negative path easy to enter and continue.","root":"ي س ر","source_ref":"92:10","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001694","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_e0eb26ca9d539070b61d"]}],"candidate_inventory":[{"anchor_refs":["92:1","92:2","92:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:9","branch_refs":["root_000256/B001","root_000323/B001","root_001088/B001","root_001290/B002","root_001392/B001","root_001559/B002"],"candidate_id":"cand_e6a2e5a4c624472700f9","commentary_obligation":"review","hft_ref":"hft_b1c4c27ba48a20640112","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_occlusion_of_visible_good","source_type":"hft","support_ids":["sup_6bba7cd5b4303ef8a3d7"],"title":"delta_occlusion_of_visible_good","trust":"legacy_unbound"},{"anchor_refs":["92:3","92:4","92:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:9","branch_refs":["root_000058/B001","root_000323/B005","root_000434/B001","root_000516/B001","root_000709/B001","root_000775/B001","root_001290/B004"],"candidate_id":"cand_6a25b1fbe91c2776e086","commentary_obligation":"review","hft_ref":"hft_6d0e487065706aa3feea","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_divergent_striving_without_measure","source_type":"hft","support_ids":["sup_f32e65bbafce1a920551"],"title":"delta_divergent_striving_without_measure","trust":"legacy_unbound"},{"anchor_refs":["92:5","92:6","92:8","92:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:9","branch_refs":["root_000089/B001","root_000323/B002","root_000852/B004","root_001028/B002","root_001110/B001","root_001290/B004","root_001677/B002"],"candidate_id":"cand_371579ef487deedf8019","commentary_obligation":"review","hft_ref":"hft_fbb73ace0bb76cc3d881","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_good_verified_in_transfer","source_type":"hft","support_ids":["sup_7721baf86920745c6e5a"],"title":"delta_good_verified_in_transfer","trust":"legacy_unbound"},{"anchor_refs":["92:10","92:7","92:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:9","branch_refs":["root_000323/B005","root_001012/B004","root_001290/B004","root_001694/B001","root_001694/B005"],"candidate_id":"cand_0968a5887fd224d0d990","commentary_obligation":"review","hft_ref":"hft_9032e9316b3c7ba50544","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_facilitated_path_dependence","source_type":"hft","support_ids":["sup_e0eb26ca9d539070b61d"],"title":"delta_facilitated_path_dependence","trust":"legacy_unbound"},{"anchor_refs":["92:11","92:8","92:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:9","branch_refs":["root_000323/B001","root_000558/B003","root_001110/B001","root_001110/B002","root_001290/B006","root_001457/B001"],"candidate_id":"cand_490d0e30ea938d504e61","commentary_obligation":"review","hft_ref":"hft_dfd4538c3567906e0d68","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_substitute_that_proves_false","source_type":"hft","support_ids":["sup_91fec92a5b011059f45b"],"title":"delta_substitute_that_proves_false","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_011f0688a2c61f909d70","connection_ref":"conn_0ccd523bd6aa593fb166","note":"Direct positive counterpart: affirming al-husna within the giving sequence.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_dbd503004632c72a96d8","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:6","source_note":"Immediate counter-reading: denying the same value opposes giving-linked confirmation.","source_row_role":"ranked_review","source_target_component_ref":"92:9","source_target_components":["92:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:9"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:6","source_target_components":["92:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:6","target_evidence":{"arabic_uthmani":"وَصَدَّقَ بِٱلْحُسْنَىٰ","ayah_ref":"92:6"},"target_ref":"92:6"},{"connection_evidence_ref":"conn_ev_77785d4543a3a3d07480","connection_ref":"conn_1cc0c928bb9acc2800f2","note":"Opening binary frame supports the passage's later divided courses.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_d50028a3fb17ab21dc98","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"92:3","source_note":"The nearby denial pole helps show the subsequent ethical divergence, but does not explain the sexed pair itself.","source_row_role":"ranked_review","source_target_component_ref":"92:9","source_target_components":["92:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:9"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:3","source_target_components":["92:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:3","target_evidence":{"arabic_uthmani":"وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ","ayah_ref":"92:3"},"target_ref":"92:3"},{"connection_evidence_ref":"conn_ev_df0f2779bb24fdef98f9","connection_ref":"conn_09a16ac88391cc2993bf","note":"Immediate negative profile: withholding and self-sufficiency precede the focus.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_722861d6d61a87be2cb7","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:8","source_note":"Denial of the husna completes the negative pattern introduced in 92:8.","source_row_role":"ranked_review","source_target_component_ref":"92:9","source_target_components":["92:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:9"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:8","source_target_components":["92:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:8","target_evidence":{"arabic_uthmani":"وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ","ayah_ref":"92:8"},"target_ref":"92:8"},{"connection_evidence_ref":"conn_ev_98ec22180d5d26d86d9c","connection_ref":"conn_1514df1390bb6c60a42a","note":"Provides only the opening movement of the passage.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_8a58009e20f3cc751e4a","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"92:2","source_note":"Supplies the denial element in the surah's contrary moral route.","source_row_role":"ranked_review","source_target_component_ref":"92:9","source_target_components":["92:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:9"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:2","source_target_components":["92:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:2","target_evidence":{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا تَجَلَّىٰ","ayah_ref":"92:2"},"target_ref":"92:2"},{"connection_evidence_ref":"conn_ev_0e5b7eec28961cbd2bbf","connection_ref":"conn_0a865c20a258a40b85f6","note":"States that the passage's efforts divide into divergent courses.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_fab2ab173490c4c6bbe3","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:4","source_note":"Rejecting al-husna states the conviction that marks the negative branch.","source_row_role":"ranked_review","source_target_component_ref":"92:9","source_target_components":["92:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:9"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:4","source_target_components":["92:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:4","target_evidence":{"arabic_uthmani":"إِنَّ سَعْيَكُمْ لَشَتَّىٰ","ayah_ref":"92:4"},"target_ref":"92:4"},{"connection_evidence_ref":"conn_ev_3d567104d27735c65630","connection_ref":"conn_8e5218161944b9e3b451","note":"Direct consequence: stored wealth cannot avail the negative profile.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_d210dd552ce0850a44f9","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:11","source_note":"Immediate predecessor identifies denial paired with miserliness and self-sufficiency.","source_row_role":"ranked_review","source_target_component_ref":"92:9","source_target_components":["92:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:9"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:11","source_target_components":["92:11"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:11","target_evidence":{"arabic_uthmani":"وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ","ayah_ref":"92:11"},"target_ref":"92:11"},{"connection_evidence_ref":"conn_ev_8898c6871899306b6297","connection_ref":"conn_fd1eb2fd912a317ad404","note":"Positive counterpart outcome: facilitation toward ease after the contrary course.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_0bb71e0c560ef09a1a92","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:7","source_note":"Denial of al-husna is the immediate cause of the contrary preparation.","source_row_role":"ranked_review","source_target_component_ref":"92:9","source_target_components":["92:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:9"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:7","source_target_components":["92:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:7","target_evidence":{"arabic_uthmani":"فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ","ayah_ref":"92:7"},"target_ref":"92:7"},{"connection_evidence_ref":"conn_ev_4fcf2f4f793c54c1e659","connection_ref":"conn_fce08930c67e40a0140b","note":"Immediate positive profile: giving and mindfulness prepare the affirmation in 92:6.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"92:5","source_target_components":["92:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:5","target_evidence":{"arabic_uthmani":"فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ","ayah_ref":"92:5"},"target_ref":"92:5"},{"connection_evidence_ref":"conn_ev_4981c5b67d162e9af302","connection_ref":"conn_492ba853196344e93421","note":"Immediate negative outcome: facilitation toward hardship follows the focus profile.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":true,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_4a68af1f8dfb33b846d3","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:10","source_note":"Immediate negative counterpart: denial of al-husna completes the causal profile for 92:10.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"92:9","source_target_components":["92:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:9"}],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"92:10","source_target_components":["92:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:10","target_evidence":{"arabic_uthmani":"فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ","ayah_ref":"92:10"},"target_ref":"92:10"}],"focus":{"arabic_uthmani":"وَكَذَّبَ بِٱلْحُسْنَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:9:1:1","qac_word_ref":"92:9:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:9:1:2","qac_word_ref":"92:9:1","root_ar":"ك ذ ب","surface_ar":"كَذَّبَ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"92:9:2:1","qac_word_ref":"92:9:2","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"92:9:2:2","qac_word_ref":"92:9:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"حُسْنَىٰ","morph_features":"STEM|POS:N|LEM:HusonaY`|ROOT:Hsn|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:9:2:3","qac_word_ref":"92:9:2","root_ar":"ح س ن","surface_ar":"حُسْنَىٰ"}],"word_analysis_qac_refs":[["92:9:1:1"],["92:9:1:2"],["92:9:2:1"],["92:9:2:2","92:9:2:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["92:9:1","92:9:2","92:9:3","92:9:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَكَذَّبَ بِٱلْحُسْنَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:9:1:1","qac_word_ref":"92:9:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:9:1:2","qac_word_ref":"92:9:1","root_ar":"ك ذ ب","surface_ar":"كَذَّبَ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"92:9:2:1","qac_word_ref":"92:9:2","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"92:9:2:2","qac_word_ref":"92:9:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"حُسْنَىٰ","morph_features":"STEM|POS:N|LEM:HusonaY`|ROOT:Hsn|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:9:2:3","qac_word_ref":"92:9:2","root_ar":"ح س ن","surface_ar":"حُسْنَىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["92:9:1:1"],["92:9:1:2"],["92:9:2:1"],["92:9:2:2","92:9:2:3"]],"word_analysis_refs":["92:9:1","92:9:2","92:9:3","92:9:4"],"word_rows":[{"analysis_record_ref":"92:9:1","analytic_gloss_range_en":"coordinating conjunction that keeps 92:9 inside the negative branch opened in 92:8 and adds denial as the culminating predicate","analytic_root_gloss_range_en":null,"qac_refs":["92:9:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"92:9:2","analytic_gloss_range_en":"perfect active Form II falsifying or denying, locally directed through a bi-governed content complement rather than a bare personal object","analytic_root_gloss_range_en":"falsehood, lying, declaring something false, denial, and construction-bound urging or proving branches; the local Form II verb with bi selects emphatic rejection of content","qac_refs":["92:9:1:2"],"root":{"arabic":"ك ذ ب","transliteration":"k-dh-b"},"surface":{"arabic":"كَذَّبَ","transliteration":"kadhdhaba"}},{"analysis_record_ref":"92:9:3","analytic_gloss_range_en":"preposition governing the following noun and marking it as the content denied by the verb","analytic_root_gloss_range_en":null,"qac_refs":["92:9:2:1"],"root":{},"surface":{"arabic":"بِ","transliteration":"bi"}},{"analysis_record_ref":"92:9:4","analytic_gloss_range_en":"the definite feminine elative substantive naming the known ultimate good, best outcome, reward, or truth-standard that is denied in this clause","analytic_root_gloss_range_en":"goodness, beauty, excellence, beneficent action, favorable outcome, and reward; the local elative substantive concentrates those ranges into the definite good rather than naming an agent or action","qac_refs":["92:9:2:2","92:9:2:3"],"root":{"arabic":"ح س ن","transliteration":"ḥ-s-n"},"surface":{"arabic":"ٱلْحُسْنَىٰ","transliteration":"al-ḥusnā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":11,"missing_anchor_refs":[],"supplied_unique_anchor_count":11},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["92:1","92:2","92:9"],"branch_refs":["root_000256/B001","root_000323/B001","root_001088/B001","root_001290/B002","root_001392/B001","root_001559/B002"],"candidate_id":"cand_e6a2e5a4c624472700f9","evidence_scope":"declared_pericope","hft_ref":"hft_b1c4c27ba48a20640112","item_id":"delta_occlusion_of_visible_good","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_occlusion_of_visible_good","support_id":"sup_6bba7cd5b4303ef8a3d7"},{"anchor_refs":["92:3","92:4","92:9"],"branch_refs":["root_000058/B001","root_000323/B005","root_000434/B001","root_000516/B001","root_000709/B001","root_000775/B001","root_001290/B004"],"candidate_id":"cand_6a25b1fbe91c2776e086","evidence_scope":"declared_pericope","hft_ref":"hft_6d0e487065706aa3feea","item_id":"delta_divergent_striving_without_measure","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_divergent_striving_without_measure","support_id":"sup_f32e65bbafce1a920551"},{"anchor_refs":["92:5","92:6","92:8","92:9"],"branch_refs":["root_000089/B001","root_000323/B002","root_000852/B004","root_001028/B002","root_001110/B001","root_001290/B004","root_001677/B002"],"candidate_id":"cand_371579ef487deedf8019","evidence_scope":"declared_pericope","hft_ref":"hft_fbb73ace0bb76cc3d881","item_id":"delta_good_verified_in_transfer","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_good_verified_in_transfer","support_id":"sup_7721baf86920745c6e5a"},{"anchor_refs":["92:10","92:7","92:9"],"branch_refs":["root_000323/B005","root_001012/B004","root_001290/B004","root_001694/B001","root_001694/B005"],"candidate_id":"cand_0968a5887fd224d0d990","evidence_scope":"declared_pericope","hft_ref":"hft_9032e9316b3c7ba50544","item_id":"delta_facilitated_path_dependence","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_facilitated_path_dependence","support_id":"sup_e0eb26ca9d539070b61d"},{"anchor_refs":["92:11","92:8","92:9"],"branch_refs":["root_000323/B001","root_000558/B003","root_001110/B001","root_001110/B002","root_001290/B006","root_001457/B001"],"candidate_id":"cand_490d0e30ea938d504e61","evidence_scope":"declared_pericope","hft_ref":"hft_dfd4538c3567906e0d68","item_id":"delta_substitute_that_proves_false","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_substitute_that_proves_false","support_id":"sup_91fec92a5b011059f45b"}],"diagnostics":[],"lane_counts":{"global":14,"macro":5,"micro":3},"packet_summary":{"ayah_count":21,"focus_ref":"92:9","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ج ز ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000244","furuq_root_norm":"ج ز ي","furuq_source_root_norm":"ج ز ي","is_dominant":true,"target_occurrences":97,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000242","furuq_root_norm":"ج ز ز","furuq_source_root_norm":"ج ز ز","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11","92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"92:9","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"92:9","lane":"macro","linguistic_source_ref":"92:9","surface_ref":"92:9","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"92:9","target_tokens":[["ve",["92:9:1"]],["en",["92:9:2"]],["güzeli",["92:9:2"]],["yalanlarsa",["92:9:1","92:9:2"]]],"text":"ve en güzeli yalanlarsa,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":11,"id":"s092-p01-001-011","label":"Contrasting forms of striving","number":1,"refs":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"92:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"92:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["92:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"92:0"}],"support_registry":[{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَغْشَىٰ","ayah_ref":"92:1"},{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا تَجَلَّىٰ","ayah_ref":"92:2"},{"arabic_uthmani":"وَكَذَّبَ بِٱلْحُسْنَىٰ","ayah_ref":"92:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000256/B001","root_000323/B001","root_001088/B001","root_001290/B002","root_001392/B001","root_001559/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001290","role":"The active assignment of falsehood anchors the reader's proposed re-covering.","root":"ك ذ ب","source_ref":"92:9","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000323","role":"Goodness and beauty provide the potentially perceptible object being covered.","root":"ح س ن","source_ref":"92:9","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001392","role":"Night's darkness supplies the scene in which visibility is withdrawn.","root":"ل ي ل","source_ref":"92:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001088","role":"A covering that rises over and conceals something supplies the occlusive operation.","root":"غ ش و","source_ref":"92:1","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001559","role":"Day opening through light supplies the contrary condition of visibility.","root":"ن ه ر","source_ref":"92:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000256","role":"Uncovering and appearance make disclosure an event rather than a static property.","root":"ج ل و","source_ref":"92:2","source_word_indices":["3"]}],"changed_reading":{"after":"Denial can be an active occlusion of a good that has become available to sight.","before":"Denial reports a settled negative judgment."},"confidence":"medium","mechanism":"The opening cover-and-disclosure cycle recasts denial as an overlay placed upon goodness that can become visible, not simply as absence of evidence.","model_id":"delta_occlusion_of_visible_good","reader_inference":"The packet supplies alternating cover and disclosure; I supply the arrow that denial can re-cover disclosed goodness. A live alternative is ordinary propositional rejection after disclosure.","status":"revised","structural_cues":["92:1 and 92:2 form an antithetical temporal pair: covering night and self-disclosing day.","The focus clause gives denial an active agent and a fixed object."],"trigger_roots":["ل ي ل","غ ش و","ن ه ر","ج ل و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_occlusion_of_visible_good","source_type":"hft","support_id":"sup_6bba7cd5b4303ef8a3d7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ","ayah_ref":"92:3"},{"arabic_uthmani":"إِنَّ سَعْيَكُمْ لَشَتَّىٰ","ayah_ref":"92:4"},{"arabic_uthmani":"وَكَذَّبَ بِٱلْحُسْنَىٰ","ayah_ref":"92:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000058/B001","root_000323/B005","root_000434/B001","root_000516/B001","root_000709/B001","root_000775/B001","root_001290/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001290","role":"Failure to carry a charge through lets denial appear as striving that does not fulfill its direction.","root":"ك ذ ب","source_ref":"92:9","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_000323","role":"The utmost limit supplies a possible common endpoint for otherwise divergent striving.","root":"ح س ن","source_ref":"92:9","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000434","role":"Measuring and proportioning supply an ordered background for differentiated existence.","root":"خ ل ق","source_ref":"92:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000516","role":"The masculine side supplies one pole of the explicitly paired differentiation.","root":"ذ ك ر","source_ref":"92:3","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000058","role":"The feminine side supplies the other pole without erasing distinction.","root":"ء ن ث","source_ref":"92:3","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000709","role":"Purposeful movement toward an object makes striving directional.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000775","role":"Scattering supplies the loss of convergence among those directed movements.","root":"ش ت ت","source_ref":"92:4","source_word_indices":["3"]}],"changed_reading":{"after":"He rejects the orienting limit by which scattered effort could become coherent.","before":"He rejects an abstract good."},"confidence":"medium","mechanism":"Measured creation, paired differentiation, purposeful movement, and dispersed pursuits activate حُسْنَىٰ as an orienting limit; denying it leaves effort active but without a common measure.","model_id":"delta_divergent_striving_without_measure","reader_inference":"The packet supplies measure, paired difference, purposeful motion, and scattering; I infer that the focus ideal can orient the motions. The alternative is that diversity remains neutral and حُسْنَىٰ names only one moral option among it.","status":"new","structural_cues":["92:3's paired nouns are followed immediately by 92:4's declaration that strivings are diverse.","The focus's definite حُسْنَىٰ can function as a singular attractor amid plurality."],"trigger_roots":["خ ل ق","ذ ك ر","ء ن ث","س ع ي","ش ت ت"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_divergent_striving_without_measure","source_type":"hft","support_id":"sup_f32e65bbafce1a920551","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ","ayah_ref":"92:5"},{"arabic_uthmani":"وَصَدَّقَ بِٱلْحُسْنَىٰ","ayah_ref":"92:6"},{"arabic_uthmani":"وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ","ayah_ref":"92:8"},{"arabic_uthmani":"وَكَذَّبَ بِٱلْحُسْنَىٰ","ayah_ref":"92:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000089/B001","root_000323/B002","root_000852/B004","root_001028/B002","root_001110/B001","root_001290/B004","root_001677/B002"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001290","role":"A charge made false by failure to carry it through anchors denial as counter-performance.","root":"ك ذ ب","source_ref":"92:9","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000323","role":"Benefiting another and exceeding bare justice identify the practical content at stake.","root":"ح س ن","source_ref":"92:9","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001028","role":"Handing something over supplies the outward transfer that realizes the good.","root":"ع ط و","source_ref":"92:5","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001677","role":"Placing oneself within protection supplies the inward discipline paired with giving.","root":"و ق ي","source_ref":"92:5","source_word_indices":["4"]},{"branch_id":"B004","mapped_root_id":"root_000852","role":"Realizing a promise or deed makes confirmation performative rather than merely verbal.","root":"ص د ق","source_ref":"92:6","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000323","role":"The repeated object identifies beneficent action as what the positive sequence verifies.","root":"ح س ن","source_ref":"92:6","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000089","role":"Stinginess supplies the withheld transfer that materially contradicts beneficence.","root":"ب خ ل","source_ref":"92:8","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001110","role":"Claimed self-sufficiency supplies the posture that makes relation and gift seem unnecessary.","root":"غ ن ي","source_ref":"92:8","source_word_indices":["4"]}],"changed_reading":{"after":"He falsifies the good in practice by withholding and treating himself as relationlessly sufficient.","before":"He holds a false belief about the good."},"confidence":"strong","mechanism":"The matched sequences make confirmation and denial materially testable: giving and self-protection enact confirmation of beneficent good, while withholding and claimed self-sufficiency enact its falsification.","model_id":"delta_good_verified_in_transfer","reader_inference":"The packet supplies exact parallel placement and opposed acts; I infer that those acts verify or falsify the ideal in practice. The alternative is that conduct merely evidences a prior doctrinal stance.","status":"strengthened","structural_cues":["92:5-6 and 92:8-9 are matched two-verse sequences ending in opposite verbs with the same prepositional object.","Giving contrasts with stinginess, and protective self-placement contrasts with asserted self-sufficiency."],"trigger_roots":["ع ط و","و ق ي","ص د ق","ح س ن","ب خ ل","غ ن ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_good_verified_in_transfer","source_type":"hft","support_id":"sup_7721baf86920745c6e5a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ","ayah_ref":"92:10"},{"arabic_uthmani":"فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ","ayah_ref":"92:7"},{"arabic_uthmani":"وَكَذَّبَ بِٱلْحُسْنَىٰ","ayah_ref":"92:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000323/B005","root_001012/B004","root_001290/B004","root_001694/B001","root_001694/B005"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001290","role":"A charge that fails in execution anchors the stance as a trajectory, not an isolated statement.","root":"ك ذ ب","source_ref":"92:9","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_000323","role":"The utmost limit supplies the destination from which the failing trajectory diverges.","root":"ح س ن","source_ref":"92:9","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001694","role":"Opening into ease supplies the positive path's increasing traversability.","root":"ي س ر","source_ref":"92:7","source_word_indices":["1","2"]},{"branch_id":"B005","mapped_root_id":"root_001694","role":"Lightness and compliance in motion make even the negative path easy to enter and continue.","root":"ي س ر","source_ref":"92:10","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_001012","role":"Twisting, opposition, and obstruction supply the paradoxical destination of that facilitated motion.","root":"ع س ر","source_ref":"92:10","source_word_indices":["2"]}],"changed_reading":{"after":"Denial is a hinge that makes a self-obstructing course progressively easier to travel.","before":"Denial is one completed act."},"confidence":"strong","mechanism":"The repeated facilitation formula around opposed destinations turns the focus stance into path formation: denial becomes an entry condition through which obstruction grows easy to follow.","model_id":"delta_facilitated_path_dependence","reader_inference":"The packet supplies mirrored facilitation and opposed ends; I supply the arrow of path dependence from stance to increasingly compliant motion. The alternative is an imposed consequence with no claim about habituation.","status":"new","structural_cues":["The same causative facilitation verb governs opposed destinations in 92:7 and 92:10.","92:10 follows the focus immediately, making denial a hinge between stance and route."],"trigger_roots":["ي س ر","ع س ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_facilitated_path_dependence","source_type":"hft","support_id":"sup_e0eb26ca9d539070b61d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ","ayah_ref":"92:11"},{"arabic_uthmani":"وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ","ayah_ref":"92:8"},{"arabic_uthmani":"وَكَذَّبَ بِٱلْحُسْنَىٰ","ayah_ref":"92:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000323/B001","root_000558/B003","root_001110/B001","root_001110/B002","root_001290/B006","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001290","role":"A provision that disappears instead of lasting supplies the focus's expectation-failure image.","root":"ك ذ ب","source_ref":"92:9","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000323","role":"The rejected good supplies the displaced object of reliance.","root":"ح س ن","source_ref":"92:9","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001110","role":"Self-sufficiency supplies the initial claim that no external good is needed.","root":"غ ن ي","source_ref":"92:8","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_001110","role":"Actual sufficiency is explicitly tested and found absent at the decisive moment.","root":"غ ن ي","source_ref":"92:11","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Accumulated wealth identifies the concrete substitute expected to provide sufficiency.","root":"م و ل","source_ref":"92:11","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_000558","role":"Falling into destruction supplies the event at which the substitute's promise fails.","root":"ر د ي","source_ref":"92:11","source_word_indices":["6"]}],"changed_reading":{"after":"His declaration displaces trust onto wealth, which then becomes the provision that actually fails expectation.","before":"He declares the good unreliable."},"confidence":"medium","mechanism":"Claimed self-sufficiency precedes the focus, but wealth later fails to suffice at the fall; falsehood rebounds from the rejected best onto the material substitute trusted instead.","model_id":"delta_substitute_that_proves_false","reader_inference":"The packet supplies claimed sufficiency, wealth, and its failure at the fall; I infer a reversal in which the trusted substitute proves false. The alternative is a warning about greed without deliberate lexical rebound.","status":"new","structural_cues":["Forms of غ ن ي bracket the focus: asserted independence in 92:8 and failed sufficiency in 92:11.","The focus stands between the choice of substitute and the test that exposes it."],"trigger_roots":["غ ن ي","م و ل","ر د ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_substitute_that_proves_false","source_type":"hft","support_id":"sup_91fec92a5b011059f45b","trust":"legacy_unbound"}]}
</lane_packet_json>
