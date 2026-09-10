# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **1:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s001-full-20260910/s001/1_3/micro.discovery.json` and modify nothing
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

- No additional lane-specific procedure.

## Response Schema

Return exactly these top-level fields:

```json
{
  "schema_version": "commentary-v5-scope-discovery-v1",
  "ayah_ref": "1:3",
  "lane": "micro",
  "coverage_complete": true,
  "candidate_decisions": [
    {
      "candidate_id": "exact packet candidate ID",
      "decision": "accept | narrow | represented | reject",
      "reason": "specific evidentiary reason",
      "finding_refs": ["micro:stable-key"],
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
      "finding_ref": "micro:stable-key",
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
`micro:`. Accepted/narrowed candidates own dedicated findings. A represented
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

Governs ayah-level (layer 2) and surah-level (layer 3) commentary. Both consume
the same input bundle and obey the same evidence rules; they differ in what
question they answer and in whether they are allowed to select.

[`PRINCIPLES.md`](PRINCIPLES.md) governs this file. Sources and formats are in
[`docs/SOURCES.md`](docs/SOURCES.md); channel rules in
[`docs/CHANNELS.md`](docs/CHANNELS.md).

The active Layer 3 production contract is
[`_channel/layer3/ORCHESTRATION.md`](_channel/layer3/ORCHESTRATION.md). The
former combined Layer 3 + 2.5 overlay workflow is retired.

Status: active draft, updated 2026-09-02. Layer 2 V5 and Layer 3 v3 workflow
contracts are implemented and locally validated; production Layer 3 semantic
passes have not yet been run.

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
The isolated Layer-2 writer cannot know that. Layer 3 consumes the unchanged
Layer-2 v2 artifacts alongside the typed Layer-1 primary floor and available
network/V11 evidence. It reads the complete Layer-2 findings index, local
`surprise:<id>` resonance rows, and preserved boundaries. It hashes Layer-2
prose and friction for lineage, but does not use their prose as the primary
floor or as semantic input. It writes a separate surah reading and does not
rewrite or overlay the ayah prose.

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

- **discovery hypotheses** — blind cross-ayah possibilities opened from the
  typed primary floor and activation cards, not reader prose;
- **channel briefs** — reviewed operations, stable hinges, safe claim forms,
  prohibited rejected predications, and explicit before/after reader shifts;
- **composition envelope** — the publishable prose plus an evidence map proving
  that every admitted channel and hinge landed visibly, with complete evidence
  refs and distinct reader-visible spans;
- **surah reading** — continuous reader prose emitted by the deterministic
  finalizer, not a summary or ayah catalogue;
- **publication evidence** — separate mapping from prose spans to packet
  evidence;
- **friction** — missing evidence and production limitations.

Contracts and schemas are under `_channel/layer3/`.

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

Layer 3 builds a separate hermetic source packet from Quran text, the typed
primary floor, the completed four-file Layer-2 v2 artifact set for every
numbered ayah, and whatever network-v3/V11 sources are available. Missing
optional source families are warnings, not build failures. Missing Quran text,
typed primary floor, or complete Layer-2 artifacts aborts. See
[`_channel/layer3/ORCHESTRATION.md`](_channel/layer3/ORCHESTRATION.md).

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

Status: active specification, updated 2026-08-18. The Layer 3 v3 workflow is
implemented and locally validated; a production semantic surah run has not yet
been completed.

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
discover or name a surah channel. In the active workflow, Layer 3 consumes those
local surprise rows later and writes a separate surah reading; it does not patch
channel disclosure back into the Layer-2 prose.

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

Layer 2 remains cold and states local surprise readings. Layer 3 v3 consumes the
unchanged Layer-2 v2 artifact set, especially the findings index and
`surprise:<id>` local resonance rows, alongside the typed primary floor and
available network/V11 evidence.

Layer 3 then performs three separate semantic passes:

- blind discovery of possible cross-ayah recognitions;
- review into channel briefs, with stable hinges, claim policies, and complete
  accounting for every discovery hypothesis and local resonance;
- composition into a prose envelope whose evidence map mechanically maps every
  admitted channel and hinge to reader-visible language.

This is not disambiguation. Review decides whether something qualifies as a
surah-wide channel, but admitted channels are not ranked and incompatible
channels may coexist.

| | layer 2 | layer 3 v3 |
| --- | --- | --- |
| states local surprise readings | yes | consumes them as local resonances |
| establishes cross-ayah systems | no | yes |
| uses Layer-2 prose as semantic input | no | no; prose is hashed for lineage |
| writes the completed channel reading | no | yes |
| writes ayah overlays | no | no |

### Layer 3 (per surah)

Receives channels at the surah level. States the whole: the operations they
form, their relation to the primary-grounded surah argument, and how each
admitted hinge changes the reader's understanding.

Layer 3 v3 writes the complete channel reading and a publication evidence map.
It does not rewrite Layer 2 and does not add Layer-2.5 increments. The evidence
map checks that every admitted channel and hinge appears in the prose exactly
enough to be visible to a regular reader.

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
`_channel/layer3/ORCHESTRATION.md`.

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
while designing additions to Layer 2. The active Layer 3 v3 workflow does not
write those additions; it records channel hinges and reader-visible prose
landings instead.

## 6. Recording

Per surah, active Layer 3 v3 records:

- `discovery-hypotheses-v3` for blind concrete image-system candidates and exact
  activation-card coverage;
- `channel-briefs-v3` for admitted channels, member landings, hinges, claim
  policies, and non-channel dispositions, with exact accounting for every
  discovery hypothesis and local resonance;
- `surah-composition-v2` for draft/editorial prelude and postlude surfaces plus
  span-level evidence maps;
- `surah-reading-evidence-v2` for the finalized publication evidence.

The schemas live under `_channel/layer3/schemas/`. For active v3 runs use only
the schema versions listed here; older schema files are archival. The runbook is
`_channel/layer3/ORCHESTRATION.md`.

---

## 7. Open

- **Maturity remains archived.** The four-step scale and `emerging`-hint rule
  belong to the retired Layer 2.5 overlay experiment. They may be revisited
  later, but the active Layer 3 v3 workflow does not depend on them.
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
{"branch_registry":[{"boundary":"Dalın çekirdeği yalnızca bir duygu değil, acımanın yönelttiği esirgeme ve iyiliktir; karşılıklı ve kalıplaşmış kullanımlar bu çekirdeğin bağımsız anlamları değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000552/B001","candidate_links":[{"candidate_id":"cand_cd0ae7737ec400621108","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَّحْمَٰن","morph_features":"STEM|POS:ADJ|LEM:r~aHoma`n|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:3:1:2","qac_word_ref":"1:3:1","surface_ar":"رَّحْمَٰنِ"},{"lemma_ar":"رَّحِيم","morph_features":"STEM|POS:ADJ|LEM:r~aHiym|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:3:2:2","qac_word_ref":"1:3:2","surface_ar":"رَّحِيمِ"}],"gloss":"acıma duygusuyla esirgeyip iyilik etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir başkasının durumu karşısında yüreğin yumuşaması, ona acıma ve içten yakınlık duyma çekirdeği oluşturur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu iç yöneliş, acınan kişiyi esirgemeyi ve ona iyilikte bulunmayı gerektiren etkin bir sonuç taşır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Topluluğun bireylerinin birbirine acıyıp birbirini esirgemesi, çekirdeğin karşılıklı bir kuruluşta gerçekleşmesidir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kimsenin Tanrı'nın esirgemesine erişmesini dilemek, çekirdek anlamdan doğan kalıplaşmış bir söz eylemidir."}},{"facet_id":"F005","role":"specialization","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Tanrı hakkında kullanıldığında esirgemenin genişliği ve yaratılmışlara iyilik olarak ulaşması belirginleşir."}}],"root_ar":"ر ح م","root_id":"root_000552","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yürek yumuşaklığı ile bunun doğurduğu esirgeme ve iyiliğin birlikte bulunduğu dal çekirdeği için uygundur.","boundary_detail":"Dalın çekirdeği yalnızca bir duygu değil, acımanın yönelttiği esirgeme ve iyiliktir; karşılıklı ve kalıplaşmış kullanımlar bu çekirdeğin bağımsız anlamları değildir.","branch_image_ar":"الرَّحْمَة والرقة","concept_gloss":"acıma duygusuyla esirgeyip iyilik etme","contextual_glosses":[{"applicability":"Bir kişiye acıma ve onu koruyup gözetme yönünün öne çıktığı genel eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İyiliğin somut olarak ulaştırılması sonucunu açıkça söylemez.","preserves":"Acıma ile esirgeme arasındaki yönelimi açıkça korur."},"facet_ids":["F001","F002"],"text":"acıyarak esirgemek","usage_role":"general"},{"applicability":"Bir topluluğun üyelerinin karşılıklı olarak acıma, esirgeme ve gözetme göstermesini anlatan bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı acıma ve gözetme kuruluşunun bütün belirleyici yönlerini korur."},"facet_ids":["F003"],"text":"birbirine acıyıp gözetmek","usage_role":"contextual"},{"applicability":"Tanrı'ya ilişkin kullanımda insana özgü duygulanma yerine kuşatıcı esirgeme ve iyilik sonucunu açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tanrısal kullanımın kuşatıcılığını, esirgeme ve iyilik sonucunu birlikte korur."},"facet_ids":["F005"],"text":"iyiliği ve esirgemesi her şeyi kuşatan","usage_role":"explanatory"}],"definition":"Bir başkasına karşı yüreğin yumuşaması, ona acıma ve bu yönelişin onu esirgeyip ona iyilik etmeyi gerektirmesidir. Tanrı'ya uygulandığında insandaki duygulanmadan çok, kuşatıcı esirgeme ve iyilik sonucu öne çıkar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir başkasının durumu karşısında yüreğin yumuşaması, ona acıma ve içten yakınlık duyma çekirdeği oluşturur."},{"facet_id":"F002","role":"core","statement":"Bu iç yöneliş, acınan kişiyi esirgemeyi ve ona iyilikte bulunmayı gerektiren etkin bir sonuç taşır."},{"facet_id":"F003","role":"associated_use","statement":"Topluluğun bireylerinin birbirine acıyıp birbirini esirgemesi, çekirdeğin karşılıklı bir kuruluşta gerçekleşmesidir."},{"facet_id":"F004","role":"associated_use","statement":"Bir kimsenin Tanrı'nın esirgemesine erişmesini dilemek, çekirdek anlamdan doğan kalıplaşmış bir söz eylemidir."},{"facet_id":"F005","role":"specialization","statement":"Tanrı hakkında kullanıldığında esirgemenin genişliği ve yaratılmışlara iyilik olarak ulaşması belirginleşir."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":null,"collision":"Kaynak dildeki aynı anlam ailesinden doğrudan alınmış bir sözcük olduğu için açıklama yerine yalnızca etiketi yineler.","fit":"drifted_loanword","loses":"İç yönelişin iyilik eylemini gerektirdiğini tek başına göstermeyebilir.","preserves":"Acıma, yumuşaklık ve esirgeme alanını genel olarak çağrıştırır."},"text":"merhamet"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Esirgeme ve somut iyilikte bulunma sonucunu dışarıda bırakır.","preserves":"Başkasının sıkıntısı karşısındaki iç yumuşamayı korur."},"text":"acıma"},{"category":"confusable","error_profile":{"adds":"Bir suçu ya da borcu kaldırma anlamını gereksiz yere ekler.","collision":"Suçtan vazgeçme eylemiyle karışarak dalın yöneldiği kişiyi ve nedeni değiştirir.","fit":"displacement","loses":"Yürek yumuşaklığı, acıma ve güçsüzü esirgeme çekirdeğini kaybeder.","preserves":"Bir başkasına iyi yönde davranma çağrışımını kısmen korur."},"text":"bağışlama"}],"identity_rationale":"Yetkili kaynak anlatımı, başkasına karşı duyulan yürek yumuşaklığını ve acımayı, bunların doğurduğu esirgeme ve iyilikle birlikte verir. Hazırlanan dal çerçevesi bu duygusal yönü, eylem sonucunu, karşılıklı kullanımları ve Tanrı'ya ilişkin genişletmeyi aynı ana bağ içinde doğru biçimde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ona acıyıp onu esirgemek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"acıma duygusu ve bu duygunun yönelttiği iyilik"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"özellikle güçsüze acıyıp onu esirgeme"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"acıma, iyilik ve gözetme"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"birbirine acıyıp birbirini esirgemek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onun Tanrı'nın esirgemesine erişmesini dilemek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"esirgemesi her şeyi kuşatan Tanrı adı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"çok esirgeyen ve bol bol iyilik eden"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"acınıp esirgenen kimse"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"acıma ve esirgeme görmüş kimse"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"acıyan ve esirgeyenlerin en üstünü"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ana babasına daha iyi davranan ve daha yakınlık gösteren"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"acıma ve esirgeme ya da başkasının acımasına konu olma durumu"}],"lexicalization_note":"Yalın biçimler acıma, esirgeme ve iyilik çekirdeğini taşır; karşılıklı davranışı ve biri için esenlik dilemeyi anlatan kalıplar ise yalnızca kendi kuruluşları içinde geçerlidir.","neighbor_coverage_note":"Sunulan bütün adaylar değerlendirildi. En yakın üç duygu dalı ile yumuşak davranış ve iyi eylem dalları sınırı gerçekten aydınlattığı için seçildi; cimrilik, iyilik yapma coşkusu, eşlik ederek koruma ve aynı kökün öteki üç dalı ya yalnızca uzak bir karşıtlık ya da ayrı bir anlam alanı sunduğundan yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu, acıma ve iç yumuşama durumunu merkezde tutar; odak ise bu yönelişin acınan kişiye iyilik olarak ulaşmasını daha kurucu bir sınır sayar. Bu yüzden genel alanları çok yakın olsa da her bağlamda birbirlerinin yerini tutmazlar.","focus_only":"Odak dal, acımanın iyilik ve esirgeme olarak kişiye ulaşmasını açık bir sonuç sayar ve Tanrısal genişletmeyi de içerir.","gloss":"acıma ile etkin esirgeme","neighbor_only":"Komşu dal, bir kişiye üzülüp yumuşama ve onun durumuna içten acıma yönünü daha doğrudan öne çıkarır.","neighbor_ref":"root_000070/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da başkasının durumu karşısında yüreğin yumuşaması, acıma ve esirgeme alanında buluşur."},{"boundary_match":"partial","distinction":"Odakta iç duygunun iyilik ve esirgeme davranışına dönüşmesi belirleyicidir. Komşuda içten yakınlık ve esirgeme isteme daha görünür olduğundan kapsamlar büyük ölçüde örtüşür, fakat kullanım sınırları tam eşit değildir.","focus_only":"Odak dal, yürek yumuşaklığından doğan esirgeme ve iyilik sonucunu çekirdeğin parçası yapar.","gloss":"esirgeyen acıma ile içten yakınlık","neighbor_only":"Komşu dal, içten yakınlık ve üst üste esirgeme dileme gibi sesleniş biçimlerini ayrıca öne çıkarır.","neighbor_ref":"root_000364/B001","relation_type":"near_synonym","shared_zone":"İki dal da yumuşaklık, acıma, içten yöneliş ve esirgeme düşüncelerini paylaşır."},{"boundary_match":"partial","distinction":"Komşunun acıma hali belirli nedenlerle açıklanabilirken odak dal daha genel bir yönelişi ve onun iyilik sonucunu kapsar. Bu neden ve sonuç farkı, yakın anlamlı iki dalı tam eşdeğer olmaktan çıkarır.","focus_only":"Odak, acımanın nedenini belirli bir yakınlık türüyle sınırlamaz ve iyilik sonucunu açıkça içerir.","gloss":"genel esirgeme ile nedenli acıma","neighbor_only":"Komşu, yumuşaklık ve acımayı özellikle kaygı duyma ya da soy yakınlığı gibi nedenlerle ilişkilendirir.","neighbor_ref":"root_000321/B006","relation_type":"near_synonym","shared_zone":"Her iki anlamda da başkasına karşı yumuşama, acıma ve onu gözetme yönelimi vardır."},{"boundary_match":"partial","distinction":"Odak dalın çıkış noktası başkasına acıyan iç yöneliştir; komşu ise acıma bulunmadan da yumuşak yöntem ve iyi davranış bildirebilir. Dolayısıyla ortak sonuçlar üretseler de çekirdekleri farklıdır.","focus_only":"Odak, bir başkasına acıma ve bu acımanın doğurduğu esirgemeyle sınırlanır.","gloss":"acıyan esirgeme ile yumuşak davranış","neighbor_only":"Komşu, işte yumuşak davranma, geçimli olma, iyi davranış, koruma ve uygunlaştırma gibi daha geniş alanlara uzanır.","neighbor_ref":"root_001356/B001","relation_type":"near_neighbor","shared_zone":"İki dal da sertlikten uzak davranma, başkasını gözetme ve ona iyilik ulaştırma alanında kesişir."},{"boundary_match":"partial","distinction":"İyi eylem çok çeşitli nedenlerle ve hatta bir nesneyi düzgün yapma biçiminde gerçekleşebilir. Odak anlam ise kişiye yönelen acıma ve esirgeme temeline bağlıdır; bu yüzden sonuç ortaklığı çekirdek eşitliği oluşturmaz.","focus_only":"Odak dalda iyilik, başkasına acıma ve yürek yumuşaklığının gerektirdiği bir sonuçtur.","gloss":"acımanın doğurduğu iyilik ile iyi eylem","neighbor_only":"Komşu dal, yapılan işin iyi ve düzgün olmasını ya da adaletin ötesinde yarar sağlamayı, acıma şartı olmadan kapsar.","neighbor_ref":"root_000323/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal başkasına yarar ulaştırma ve iyi davranma sonucunda buluşabilir."}],"source_phrase_ar":"أصل واحد يدل على الرقة والعطف والرأفة (maqayis)؛ المرحمة الرحمة ورحمته أرحمه رحمة ومرحمة وترحمت عليه (ayn)؛ رحمته رحمة ورحما ومرحمة والرحمن الرحيم مشتقان من الرحمة (jamhara)؛ الرحمة الرقة والتعطف والمرحمة مثله وتراحم القوم (sihah)؛ ذو الرحمة والرحيم العاطف ورحمة الضعيف والتعطف عليه (tahdhib)؛ الرحمة رقة تقتضي الإحسان إلى المرحوم والرحمن والرحيم (mufradat)","source_summary":"Ortak anlatım, yürek yumuşaklığı ile acıma ve yakınlığı temel alır; bu yönelişin acınan kişiye iyilik ve esirgeme olarak ulaşmasını da anlamın ayrılmaz sonucu sayar. Karşılıklı davranış, biri için esenlik dileme ve Tanrı'nın kuşatıcı esirgemesini bildiren kullanımlar aynı çekirdekten geliştirilir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الرقة والعطف والرأفة والإحسان إلى المرحوم والمرحمة والتراحم والترحم وأسماء الرحمن والرحيم من جهة الاشتقاق من الرحمة.","what_is_not_ar":"ليس المراد هنا الرَّحِم الجارحة ولا القرابة إلا من جهة اتصالها بالمعنى في بعض المصادر."},"support_links":["sup_20bee313d3d1fd1fd1a1"]},{"boundary":"Dal, bedensel organı değil ortak soydan doğan yakın ilişkiyi anlatır; bağı sürdürme ya da koparma eylemleri ancak ilgili kalıplarda bu çekirdeğe eklenir.","branch_kind":"mixed_non_bare","branch_ref":"root_000552/B002","candidate_links":[{"candidate_id":"cand_fe32ac952ea4fa4a9c2d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَّحْمَٰن","morph_features":"STEM|POS:ADJ|LEM:r~aHoma`n|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:3:1:2","qac_word_ref":"1:3:1","surface_ar":"رَّحْمَٰنِ"},{"lemma_ar":"رَّحِيم","morph_features":"STEM|POS:ADJ|LEM:r~aHiym|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:3:2:2","qac_word_ref":"1:3:2","surface_ar":"رَّحِيمِ"}],"gloss":"yakın soy bağı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ortak soydan gelme, kişiler arasında yakın ve kalıcı bir soy ilişkisi kurar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bedensel organın adı, aynı doğum kaynağından çıkmış olma düşüncesi üzerinden soy ilişkisine aktarılmıştır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Soy bağını sürdürmek veya koparmak, ilişkinin kendisini değil ona karşı takınılan eylemli tutumu anlatır."}}],"root_ar":"ر ح م","root_id":"root_000552","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ortak soydan gelmeye dayanan yakın ve kalıcı ilişkiyi kısa biçimde adlandırmak için uygundur.","boundary_detail":"Dal, bedensel organı değil ortak soydan doğan yakın ilişkiyi anlatır; bağı sürdürme ya da koparma eylemleri ancak ilgili kalıplarda bu çekirdeğe eklenir.","branch_image_ar":"الرَّحِم والقرابة","concept_gloss":"yakın soy bağı","contextual_glosses":[{"applicability":"İlişkinin ortak soy temelini açıkça belirtmenin tek sözcüklü karşılıktan daha önemli olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ortak soy temelini, tarafları ve ilişkinin yakınlık niteliğini açıkça korur."},"facet_ids":["F001"],"text":"aynı soydan gelenler arasındaki yakınlık","usage_role":"explanatory"},{"applicability":"Yakın soy ilişkisine karşı gösterilen bağlılık veya ilişkiyi kesme eylemi açıkça söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağın varlığını ve ona yönelik sürdürme ya da koparma eylemini birlikte korur."},"facet_ids":["F003"],"text":"soy bağını sürdürmek ya da koparmak","usage_role":"contextual"}],"definition":"İnsanları ortak bir soydan gelmeleri yoluyla birbirine bağlayan yakın ilişkidir. Organ adı, birden çok kişinin aynı doğum kaynağından çıkması düşüncesiyle bu toplumsal bağa aktarılmıştır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ortak soydan gelme, kişiler arasında yakın ve kalıcı bir soy ilişkisi kurar."},{"facet_id":"F002","role":"extension","statement":"Bedensel organın adı, aynı doğum kaynağından çıkmış olma düşüncesi üzerinden soy ilişkisine aktarılmıştır."},{"facet_id":"F003","role":"associated_use","statement":"Soy bağını sürdürmek veya koparmak, ilişkinin kendisini değil ona karşı takınılan eylemli tutumu anlatır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Evlilik, aynı evde yaşama ve soy bağı bulunmayan ev halkını da kapsama ekler.","collision":"Soy ilişkisi ile evlilik veya ortak yaşam temelindeki aile birimini birbirine karıştırır.","fit":"broadening","loses":null,"preserves":"Yakın kişilerden oluşan toplumsal çevre çağrışımını korur."},"text":"aile"},{"category":"alternative","error_profile":{"adds":"Duygusal, uzamsal ve düşünsel yakınlığı da soy bağı aranmadan kapsar.","collision":"Soydan gelen ilişkiyi başka yakınlık türlerinden ayıramaz.","fit":"broadening","loses":null,"preserves":"İki kişi arasındaki bağın sıkı oluşunu korur."},"text":"yakınlık"}],"identity_rationale":"Yetkili kaynak anlatımı, ortak soydan gelmeye dayanan yakın ilişkiyi dalın çekirdeği olarak verir ve organ adının ortak doğum kaynağı düşüncesiyle bu ilişkiye aktarıldığını açıklar. Hazırlanan çerçeve, bedensel organı bu daldan ayırırken soy bağını, çoğul bağları ve bu bağın sürdürülüp koparılmasını doğru yerde tutar.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yakın soy bağı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"soy ve yakınlık bağları"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"soy bağını sürdürmek ya da koparmak"}],"lexicalization_note":"Yalın biçimler yakın soy bağını adlandırır; bu bağı sürdürme veya koparma anlamı ise yalnızca eylem kalıbına bağlıdır ve yalın dal tanımına katılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Genel soy yakınlığı, bağı sürdürme, bağı kesme, evlenilmesi yasak yakınlar ve yakın kişi ayrımları yayımlandı; özel soy derecesi, soyun doğruluğu, daha seyrek bir yakınlık adı ve aynı kökün duygu, organ ve hastalık dalları sınırı daha az aydınlattığı veya seçilenlerle yinelendiği için dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal soyca yakın olmayı ve yakın kişileri genel biçimde adlandırabilir. Odak ise ortak doğum kaynağı imgesine bağlanan belirli ilişki adını öne çıkarır; bu nedenle çekirdekleri çok yakın olsa da kapsamları tam olarak eşit değildir.","focus_only":"Odak dal, yakın soy ilişkisini organ adından ortak doğum kaynağı düşüncesiyle kurulmuş özel bir bağ olarak adlandırır.","gloss":"özel soy bağı ile genel soy yakınlığı","neighbor_only":"Komşu dal, genel olarak soy yakınlığını, yakın kişileri ve yakınlık derecelerini daha geniş bir adlandırma alanında kapsar.","neighbor_ref":"root_001212/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da ortak soydan gelen kişiler arasındaki yakın ilişkiyi ve bu kişilerin birbirine bağlılığını anlatır."},{"boundary_match":"partial","distinction":"Odak dal taraflar arasındaki soy bağının adıdır, komşu ise bu veya başka bir bağı sürdürme eylemidir. İlişki ile ilişkiye yönelik davranış ayrımı, birbirlerinin yerine kullanılmalarını engeller.","focus_only":"Odak, soy ilişkisinin kendisini adlandırır; bağ sürdürülmese bile ilişki türü varlığını korur.","gloss":"soy bağı ile bağı sürdürme","neighbor_only":"Komşu, bir ilişkiyi etkin biçimde sürdürmeyi ve kopukluktan kaçınmayı anlatır; soy dışındaki bağlara da uygulanabilir.","neighbor_ref":"root_001655/B004","relation_type":"near_neighbor","shared_zone":"İki dal, soyca yakın kişiler arasındaki ilişkinin korunması bağlamında birlikte görülebilir."},{"boundary_match":"partial","distinction":"Odak anlam tarafları bağlayan ilişkinin adıdır; koparma bunun yalnızca bir olası durumudur. Komşu ise ilişkinin kendisini değil, onu kesen kişinin belirleyici davranışını adlandırır.","focus_only":"Odak, yakın soy ilişkisinin kendisini ve hem sürdürülme hem de koparılma olasılığını kapsar.","gloss":"soy bağı ile onu kesme","neighbor_only":"Komşu, yalnızca soy bağını kesen kişiyi ve bağın koparılması davranışını öne çıkarır.","neighbor_ref":"root_000080/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da yakın soy ilişkisini ve bu ilişkinin koparılması durumunu konu edinir."},{"boundary_match":"field_only","distinction":"Odak, kişiler arasında bulunan soy bağını adlandırır. Komşu ise bu bağdan doğabilen belirli bir hukukî ve toplumsal kişi sınıfını öne çıkarır; aynı alanı paylaşsalar da çekirdekleri farklıdır.","focus_only":"Odak dal, evlenme yasağı veya cinsiyet ayrımı olmadan yakın soy ilişkisini genel biçimde anlatır.","gloss":"soy ilişkisi ile yasaklı yakın sınıfı","neighbor_only":"Komşu dal, aile içindeki kadınları ve özellikle evlenilmesi yasak olan yakınları sınıflandırır.","neighbor_ref":"root_000313/B011","relation_type":"same_field","shared_zone":"İki dal da aile ve soy çevresindeki yakın kişileri konu edinir."},{"boundary_match":"partial","distinction":"Odak anlam ilişkinin kendisidir; komşu ise bu ilişkinin tarafı olan yakın ve sevilen kişiyi adlandırır. Kişi ile kişiler arasındaki bağ birbirinin yerine geçmez.","focus_only":"Odak, kişiler arasındaki ortak soy ilişkisini soyut bir bağ olarak adlandırır.","gloss":"soy bağı ile yakın kişi","neighbor_only":"Komşu, sevilen yakın kişiyi veya kişinin kendi ailesinden özel çevresini somut kişiler olarak öne çıkarır.","neighbor_ref":"root_000001/B011","relation_type":"near_neighbor","shared_zone":"Her iki dal yakın soy çevresini ve bu çevredeki kişiler arasındaki bağı kapsayan bağlamlarda kesişir."}],"source_phrase_ar":"الرَّحِم علاقة القرابة (maqayis)؛ بينهما رَحِم أي قرابة قريبة والرحم القرابة تجمع بني أب (ayn)؛ صارت أسباب القرابة أرحاما (jamhara)؛ الرحم أيضا القرابة والرحم بالكسر مثله ووصال رحم (sihah)؛ الرحم القرابة تجمع بني أب وبينهما رحم أي قرابة قريبة (tahdhib)؛ استعير الرحم للقرابة لكونهم خارجين من رحم واحدة (mufradat)","source_summary":"Ortak anlatım, aynı atadan ya da yakın bir soy çizgisinden gelen kişileri birbirine bağlayan ilişkiyi öne çıkarır. Çoğul kullanım bu bağların ve soy yollarının bütününü, eylemli kullanım ise bağın sürdürülmesini veya kesilmesini bildirir; organla bağlantı ortak doğum kaynağına dayanan bir aktarımdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الرَّحِم بمعنى القرابة القريبة وأسباب النسب وصلة الرحم وقطعها والأرحام.","what_is_not_ar":"ليس المراد هنا رَحِم الأنثى نفسه ولا الرحمة العامة إلا إذا صرح المصدر بانتقال أو استعارة."},"support_links":["sup_7599367ac31807367809"]},{"boundary":"Bu dal sağlıklı bedensel organın kendisidir; içindeki yavruyu, soy bağını veya organın ağrı ve hastalık durumlarını adlandırmaz.","branch_kind":"bare","branch_ref":"root_000552/B003","candidate_links":[{"candidate_id":"cand_c5e46909163d28966a09","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَّحْمَٰن","morph_features":"STEM|POS:ADJ|LEM:r~aHoma`n|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:3:1:2","qac_word_ref":"1:3:1","surface_ar":"رَّحْمَٰنِ"},{"lemma_ar":"رَّحِيم","morph_features":"STEM|POS:ADJ|LEM:r~aHiym|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:3:2:2","qac_word_ref":"1:3:2","surface_ar":"رَّحِيمِ"}],"gloss":"döl yatağı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi bedenindeki bu iç organ, yavrunun oluşup geliştiği yer ve onu karın içinde taşıyan kap işlevindedir."}}],"root_ar":"ر ح م","root_id":"root_000552","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi bedeninde yavrunun tutunup geliştiği belirli iç organı doğal ve kısa bir Türkçe karşılıkla anlatır.","boundary_detail":"Bu dal sağlıklı bedensel organın kendisidir; içindeki yavruyu, soy bağını veya organın ağrı ve hastalık durumlarını adlandırmaz.","branch_image_ar":"رَحِم الأنثى","concept_gloss":"döl yatağı","contextual_glosses":[{"applicability":"Teknik organ adının bilinmediği veya organın işlevinin açıkça belirtilmesi gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel organ niteliğini ve yavrunun gelişme yeri olma işlevini korur."},"facet_ids":["F001"],"text":"yavrunun geliştiği iç organ","usage_role":"explanatory"}],"definition":"Dişinin karnında yavrunun tutunup geliştiği, onu doğuma kadar içinde taşıyan iç organdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi bedenindeki bu iç organ, yavrunun oluşup geliştiği yer ve onu karın içinde taşıyan kap işlevindedir."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":null,"collision":"Kaynak dildeki organ adını doğrudan yinelediği ve aynı ses dizisi başka adlandırmalarda da bulunduğu için açıklayıcı karşılık görevini yerine getirmez.","fit":"drifted_loanword","loses":null,"preserves":"Türkçedeki yerleşik kullanımında aynı bedensel organı doğru olarak gösterebilir."},"text":"rahim"},{"category":"confusable","error_profile":{"adds":"Döl yatağı dışındaki bütün karın boşluğunu ve başka organları kapsama ekler.","collision":"Belirli iç organı onun bulunduğu daha geniş beden bölgesiyle karıştırır.","fit":"broadening","loses":null,"preserves":"Organın bulunduğu genel beden bölgesini korur."},"text":"karın"},{"category":"alternative","error_profile":{"adds":"Belirli organın dışındaki bütün karın bölgesini ve yalnızca gebelik durumunu kapsama ekler.","collision":"Organın kendisiyle annenin genel karın bölgesini birbirine karıştırır.","fit":"broadening","loses":null,"preserves":"Yavrunun anne bedeninde taşındığı yer düşüncesini korur."},"text":"ana karnı"}],"identity_rationale":"Yetkili kaynak anlatımı, dişi bedenindeki bu organı yavrunun başladığı, karın içinde taşındığı ve geliştiği yer ve kap olarak tanımlar. Hazırlanan dal çerçevesi organı soy ilişkisinden, acıma anlamından ve organın hastalık durumundan doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"dişinin döl yatağı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"döl yatakları"}],"lexicalization_note":"Dal bağımsız organ adını ve onun çoğulunu kapsar; herhangi bir kalıba bağlı yan anlam bu yalın tanıma eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Soy bağıyla ad aktarımı, organın içindeki yavru, gebeliğin yerleşmesi, dönemsel kanama ve organdaki damarlar en açıklayıcı sınırları verdi; gebelik ürünleri, karın içi, şişmanlık ve aynı kökün acıma ile hastalık dalları ya seçilen ayrımları yineledi ya da yalnızca uzak bir beden bağlamı sundu.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak bedensel bir organdır; komşu ise o organın ortak köken imgesi üzerinden adlandırılan kişiler arası bağdır. Tarihsel kavram bağlantısı, somut organ ile soyut ilişkiyi eş anlamlı yapmaz.","focus_only":"Odak dal, dişi bedeninde yavrunun geliştiği somut iç organı adlandırır.","gloss":"döl yatağı ile soy bağı","neighbor_only":"Komşu dal, ortak soydan gelen kişiler arasındaki toplumsal ilişkiyi ve yakınlığı adlandırır.","neighbor_ref":"root_000552/B002","relation_type":"same_field","shared_zone":"Soy ilişkisi, aynı doğum kaynağından çıkma düşüncesiyle organ adından geliştirilmiştir."},{"boundary_match":"partial","distinction":"Odak yavrunun bulunduğu ve geliştiği organdır, komşu ise bu organın içinde gelişen canlıdır. Taşıyan yapı ile taşınan yavru aynı bağlamda görünse de birbirinin yerine kullanılamaz.","focus_only":"Odak, yavruyu içinde taşıyan anneye ait organın kendisidir.","gloss":"taşıyan organ ile taşınan yavru","neighbor_only":"Komşu, henüz doğmamış ve anne karnında gizli bulunan yavrunun kendisidir.","neighbor_ref":"root_000266/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal doğumdan önce anne bedenindeki gelişme sürecinin aynı yer ve katılımcılarını konu edinir."},{"boundary_match":"partial","distinction":"Odak kalıcı beden yapısıdır; komşu o yapının içinde gerçekleşen belirli bir başlangıç olayıdır. Organın varlığı gebeliğin yerleşmiş olmasını gerektirmez.","focus_only":"Odak, gebelik olsun ya da olmasın bedende bulunan organı adlandırır.","gloss":"organ ile gebeliğin yerleşmesi","neighbor_only":"Komşu, döllenmiş yavrunun bu organda yerleşmesi olayını ve yerleşmiş gebelik durumunu anlatır.","neighbor_ref":"root_000042/B002","relation_type":"near_neighbor","shared_zone":"İki dal, yavrunun döl yatağında yerleşip gelişmeye başlaması bağlamında doğrudan buluşur."},{"boundary_match":"field_only","distinction":"Odak bir organın adıdır; komşu ise o organla ilişkili kan ve dönemsel bedensel olaydır. Aynı anatomik alanı paylaşmaları çekirdeklerini birleştirmez.","focus_only":"Odak, yavrunun gelişme yeri olan iç organın anatomik kimliğini bildirir.","gloss":"döl yatağı ile dönemsel kanama","neighbor_only":"Komşu, belirli zamanda bu organdan gelen kanı, kanama olayını, zamanı ve ilgili durumu bildirir.","neighbor_ref":"root_000379/B001","relation_type":"same_field","shared_zone":"Her iki dal dişi üreme bedenini ve aynı organla bağlantılı olayları konu edinir."},{"boundary_match":"field_only","distinction":"Odak bütün organdır; komşu ise o organ içinde bulunan belirli damar veya bölgedir. Bütün ile onun küçük anatomik parçası birbirinin yerine geçmez.","focus_only":"Odak, dişinin yavruyu taşıyan organının bütününü adlandırır.","gloss":"döl yatağı ile içindeki damarlar","neighbor_only":"Komşu, özellikle dişi devenin bu organındaki damarları ya da dar bir bölgeyi adlandırır.","neighbor_ref":"root_001056/B005","relation_type":"same_field","shared_zone":"İki dal aynı organın anatomik alanında ve özellikle dişi hayvan bedeninde buluşur."}],"source_phrase_ar":"سميت رحم الأنثى رحما (maqayis)؛ الرحم بيت منبت الولد ووعاؤه في البطن (ayn)؛ الرحم رحم المرأة (jamhara)؛ الرحم رحم الأنثى وهي مؤنثة (sihah)؛ الرحم بيت منبت الولد ووعاؤه في البطن (tahdhib)؛ الرحم رحم المرأة (mufradat)","source_summary":"Ortak anlatım, dişi ya da kadın bedenindeki organı yavrunun başladığı yer ve karın içindeki taşıyıcı kap olarak tanımlar. Tekil biçim organı, çoğul biçim ise aynı tür organları adlandırır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه رَحِم المرأة أو الأنثى بوصفه بيت منبت الولد ووعاءه في البطن.","what_is_not_ar":"ليس المراد هنا القرابة المسماة رحما ولا الرحمة والرقة."},"support_links":["sup_bc9f3e0dd94d781c05aa"]},{"boundary":"Dal sağlıklı organı veya genel beden ağrısını değil, döl yatağına özgü ağrı, hastalık, şişme ve doğum sonrası yavru zarını atamama durumlarını kapsar.","branch_kind":"bare","branch_ref":"root_000552/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَّحْمَٰن","morph_features":"STEM|POS:ADJ|LEM:r~aHoma`n|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:3:1:2","qac_word_ref":"1:3:1","surface_ar":"رَّحْمَٰنِ"},{"lemma_ar":"رَّحِيم","morph_features":"STEM|POS:ADJ|LEM:r~aHiym|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:3:2:2","qac_word_ref":"1:3:2","surface_ar":"رَّحِيمِ"}],"gloss":"döl yatağı hastalığı ve doğum sonrası bozukluk","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi hayvan veya kadında döl yatağının ağrıması ya da hastalanması temel durumdur; özellikle bazı kullanımlarda bu durum doğum sonrasında görülür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koyunun doğum yaptıktan sonra yavru zarını dışarı atamaması, dala bağlı özel bir doğum sonrası bozukluktur."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Koyun veya koyun sürüsünde döl yatağının şişmesi, hastalık durumunun özel bir gerçekleşmesidir."}}],"root_ar":"ر ح م","root_id":"root_000552","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Organ ağrısı veya hastalığı ile şişme ve yavru zarını atamama gibi özel doğum sonrası durumları birlikte kapsayan üst karşılıktır.","boundary_detail":"Dal sağlıklı organı veya genel beden ağrısını değil, döl yatağına özgü ağrı, hastalık, şişme ve doğum sonrası yavru zarını atamama durumlarını kapsar.","branch_image_ar":"وجع الرَّحِم بعد الولادة","concept_gloss":"döl yatağı hastalığı ve doğum sonrası bozukluk","contextual_glosses":[{"applicability":"Kadın veya dişi hayvanda doğumun ardından organ ağrısının açıkça söz konusu olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğumla sınırlı olmayan hastalığı, şişmeyi ve yavru zarının atılamamasını dışarıda bırakır.","preserves":"Doğum sonrasındaki organ ağrısını ve etkilenen beden bölümünü korur."},"facet_ids":["F001"],"text":"doğum sonrası döl yatağı ağrısı","usage_role":"contextual"},{"applicability":"Koyunun doğumdan sonra yavruyu saran dokuyu dışarı atamadığı özel hayvancılık bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğum sonrasını, etkilenen koyunu ve zarın dışarı atılamaması olayını korur."},"facet_ids":["F002"],"text":"doğumdan sonra yavru zarını atamama","usage_role":"explanatory"},{"applicability":"Koyun veya koyun sürüsünde organ şişmesinin özellikle bildirildiği bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Etkilenen organı ve hastalığın şişme biçimindeki gerçekleşmesini korur."},"facet_ids":["F003"],"text":"döl yatağında şişme","usage_role":"contextual"}],"definition":"Dişi deve, koyun veya kadında döl yatağının ağrıması ya da hastalanmasıyla; koyunda ise ayrıca şişmesiyle belirlenen durumdur. Bazı kullanımlar bunu doğum sonrasına bağlar. Koyunun doğumdan sonra yavru zarını atamaması da bu organ çevresindeki özel bir bozukluk olarak dala dahildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi hayvan veya kadında döl yatağının ağrıması ya da hastalanması temel durumdur; özellikle bazı kullanımlarda bu durum doğum sonrasında görülür."},{"facet_id":"F002","role":"specialization","statement":"Koyunun doğum yaptıktan sonra yavru zarını dışarı atamaması, dala bağlı özel bir doğum sonrası bozukluktur."},{"facet_id":"F003","role":"specialization","statement":"Koyun veya koyun sürüsünde döl yatağının şişmesi, hastalık durumunun özel bir gerçekleşmesidir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Döl yatağı hastalığı bulunmayan olağan doğum sonrası dönemi ve bütün bedensel değişimleri kapsama ekler.","collision":"Organ hastalığını doğum yapan kişinin genel iyileşme dönemiyle karıştırır.","fit":"broadening","loses":null,"preserves":"Doğumdan sonraki zaman ve iyileşme dönemi bağlantısını korur."},"text":"lohusalık"},{"category":"confusable","error_profile":{"adds":"Doğum sırasında yavrunun çıkışına eşlik eden olağan kasılma ağrılarını ekler.","collision":"Doğum sırasındaki olağan sancıyı doğum sonrasındaki organ hastalığıyla karıştırır.","fit":"displacement","loses":"Döl yatağına özgü hastalığı, şişmeyi ve doğum sonrası bozuklukları kaybeder.","preserves":"Doğum ile ağrı arasındaki genel bağlantıyı korur."},"text":"doğum sancısı"},{"category":"alternative","error_profile":{"adds":"Döl yatağı dışındaki sindirim ve başka iç organlardan doğan ağrıları kapsama ekler.","collision":"Belirli üreme organı hastalığını kaynağı belirsiz genel karın ağrısıyla karıştırır.","fit":"broadening","loses":null,"preserves":"Ağrının gövdenin iç bölümünde bulunması yönünü kısmen korur."},"text":"karın ağrısı"}],"identity_rationale":"Hazırlanan başlık doğumdan sonraki ağrıyı doğru bir merkez olarak gösterse de yetkili kaynak anlatımı bundan daha geniştir: dişi deve, koyun veya kadında döl yatağının ağrıması ya da hastalanması yanında şişme ve koyunun doğumdan sonra yavru zarını atamaması da aynı dalda yer alır. Dal bölünmeden korunabilir, fakat tanım yalnızca doğum sonrası ağrıyla sınırlandırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"doğumdan sonra döl yatağı ağrıyan ya da döl yatağı hastalanan dişi"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"döl yatağı ağrımak ya da hastalanmak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"koyunun doğumdan sonra yavru zarını atamaması"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"döl yatağı şişmiş koyun ya da koyun sürüsü"}],"lexicalization_note":"Verilen biçimler döl yatağına özgü hastalık ve doğum sonrası bozuklukları bağımsız olarak adlandırır; tanım başka bir kalıptan yalın anlama aktarım yapmaz.","neighbor_coverage_note":"Sunulan bütün adaylar değerlendirildi. Sağlıklı organla ayrım ilk sıraya alındı; hayvanlarda şişme ve üç farklı yerel hastalık dalı alan sınırını gösterdi. Öteki boğaz, boyun, omuz ve üreme organı dışı hastalık adayları seçilen alan karşılaştırmalarını yineledi; acıma ve soy bağı dalları ise yalnızca biçim ortaklığı taşıdı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal anatomik yapının adıdır; odak ise o yapıda ortaya çıkan belirli patolojik ve doğum sonrası durumların adıdır. Organın varlığı hastalık bulunduğunu göstermez.","focus_only":"Odak dal, döl yatağının ağrı, hastalık, şişme veya doğum sonrası bozukluk içindeki durumunu adlandırır.","gloss":"organ hastalığı ile organın kendisi","neighbor_only":"Komşu dal, herhangi bir hastalık şartı olmadan yavruyu taşıyan sağlıklı organın kendisini adlandırır.","neighbor_ref":"root_000552/B003","relation_type":"near_neighbor","shared_zone":"İki dal aynı bedensel organa dayanır ve biri ötekinin hastalık durumunu anlatır."},{"boundary_match":"field_only","distinction":"Odakta etkilenen yer döl yatağıdır ve durum hastalık olarak ele alınır. Komşu farklı beden bölgelerindeki şişmeyi ve olağan süt verme değişimini de kapsadığı için yalnızca aynı hayvancılık ve beden alanını paylaşır.","focus_only":"Odak, döl yatağı ağrısı, hastalığı, şişmesi ve doğum sonrası bozukluklarla sınırlıdır.","gloss":"döl yatağı bozukluğu ile başka şişmeler","neighbor_only":"Komşu, meme, boğaz veya sırttaki şişkinliği ve doğum sırasında memenin sütle dolup sarkmasını kapsar.","neighbor_ref":"root_000467/B005","relation_type":"same_field","shared_zone":"Her iki dal dişi hayvanlarda doğum çevresinde görülebilen şişme ve bedensel değişiklikleri konu edinir."},{"boundary_match":"field_only","distinction":"Ortak alan hayvan hastalığıdır; etkilenen organ, belirtiler ve doğumla bağlantı bütünüyle farklıdır. Bu nedenle alan ortaklığı dışında anlam örtüşmesi yoktur.","focus_only":"Odak, dişi üreme organına ve çoğunlukla doğum sonrasına bağlı bir hastalık kümesidir.","gloss":"üreme organı hastalığı ile başka hayvan hastalığı","neighbor_only":"Komşu, koyun ve keçinin bel, böğür, kalça veya bacak bölgelerini etkileyip yürüyüşü bozan başka bir hastalıktır.","neighbor_ref":"root_001541/B014","relation_type":"same_field","shared_zone":"İki dal koyunlarda görülen, ağrı veya belirgin beden bozukluğu yapan hayvan hastalıklarını adlandırır."},{"boundary_match":"field_only","distinction":"Etkilenen beden bölgesi ve hastalığın oluşma bağlamı farklıdır. Odak doğum ve dişi üreme organıyla sınırlıyken komşu yan bölgesine ve başka nedenlere bağlıdır.","focus_only":"Odak, yalnızca dişi üreme organındaki hastalık ve doğum sonrası bozuklukları kapsar.","gloss":"döl yatağı ağrısı ile yan ağrısı","neighbor_only":"Komşu, insan veya hayvanda böğür ve yan bölgesindeki hastalık, susuzluk etkisi veya darbe sonucunu kapsar.","neighbor_ref":"root_000262/B007","relation_type":"same_field","shared_zone":"İki dal bedendeki belirli bir bölgeye yerleşen ağrı veya hastalığı adlandırma alanında buluşur."},{"boundary_match":"field_only","distinction":"Benzerlik yalnızca beden bölgesine bağlı hastalık adı olmalarıdır. Organ, hasta grubu ve doğumla ilişki farklı olduğundan anlamları birbirinin yerine geçmez.","focus_only":"Odak, döl yatağına özgü ağrı ve doğum sonrası bozuklukları bildirir.","gloss":"üreme organı ağrısı ile boğaz ağrısı","neighbor_only":"Komşu, boğazda veya küçük dil yakınında ortaya çıkan ağrılı hastalığı bildirir.","neighbor_ref":"root_000995/B013","relation_type":"same_field","shared_zone":"Her iki dal, etkilenen beden bölümüne göre adlandırılmış yerel bir ağrı veya hastalık durumudur."}],"source_phrase_ar":"شاة رحوم إذا اشتكت رحمها بعد النتاج (maqayis)؛ ناقة رحوم أصابها داء في رحمها وقد رحمت المرأة إذا اشتكت رحمها (ayn)؛ ناقة رحوم إذا اشتكت رحمها في عقب الولادة وامرأة رحوم (jamhara)؛ الرحوم الناقة التي تشتكي رحمها بعد النتاج (sihah)؛ ناقة رحوم أصابها داء في رحمها والرحام أن تلد الشاة ثم لا تلقي سلاها وشاة راحم وغنم رواحم إذا ورم رحمها (tahdhib)؛ امرأة رحوم تشتكي رحمها (mufradat)","source_summary":"Ortak anlatım, dişi deve, koyun veya kadının döl yatağında ağrı ya da hastalık bulunmasını temel alır. Kaynakların bir bölümü bunu özellikle doğum sonrasına bağlar. Toplu anlatım ayrıca koyunda organın şişmesini ve doğumdan sonra yavru zarının atılamamasını aynı organ çevresindeki özel durumlar olarak kaydeder.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الرحوم والراحم والرواحم وما قيل في الناقة أو الشاة أو المرأة إذا اشتكت رحمها أو أصابه داء أو ورم أو لم تلق السلا بعد الولادة.","what_is_not_ar":"ليس المراد مجرد رَحِم الأنثى السليم ولا القرابة ولا الرحمة."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["1:3:1"],"branch_refs":[],"candidate_id":"cand_2fb12f95b6f9a1077b6e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000552"],"scope":"focus_ayah","source_local_id":"1:3:1:basmala-reprise-ring","source_type":"word_analysis","support_ids":["sup_272c858fee96121a92cf","sup_d9badd7741765a383942"],"title":"the opening formula returns as a mercy ring","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:3:1","qac_refs":["1:3:1:1","1:3:1:2"],"status":"accepted"}},{"anchor_refs":["1:3:1"],"branch_refs":[],"candidate_id":"cand_18d73edde943787b4080","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000552"],"scope":"focus_ayah","source_local_id":"1:3:1:compact-pair-and-sound","source_type":"word_analysis","support_ids":["sup_272c858fee96121a92cf","sup_75eb074a3ef5fea3ca41"],"title":"first half of a compact mercy-pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:3:1","qac_refs":["1:3:1:1","1:3:1:2"],"status":"accepted"}},{"anchor_refs":["1:3:1"],"branch_refs":[],"candidate_id":"cand_52d721bf55fbc6055858","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000552"],"scope":"focus_ayah","source_local_id":"1:3:1:familiar-definite-divine-title","source_type":"word_analysis","support_ids":["sup_272c858fee96121a92cf","sup_c8e3357a8bd067782315"],"title":"definite proper-name register","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:3:1","qac_refs":["1:3:1:1","1:3:1:2"],"status":"accepted"}},{"anchor_refs":["1:3:1"],"branch_refs":[],"candidate_id":"cand_acb38a75be04ec0aa63a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000552"],"scope":"focus_ayah","source_local_id":"1:3:1:genitive-apposition-boundary","source_type":"word_analysis","support_ids":["sup_272c858fee96121a92cf","sup_724702948b5a584f3539"],"title":"genitive apposition carries the prior ayah forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:3:1","qac_refs":["1:3:1:1","1:3:1:2"],"status":"accepted"}},{"anchor_refs":["1:3:1"],"branch_refs":[],"candidate_id":"cand_985bed732d2b34730bfb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000552"],"scope":"focus_ayah","source_local_id":"1:3:1:overflowing-mercy-lordship","source_type":"word_analysis","support_ids":["sup_272c858fee96121a92cf","sup_fbeb59f860e5554e459c"],"title":"overflowing mercy specifies lordship as care","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:3:1","qac_refs":["1:3:1:1","1:3:1:2"],"status":"accepted"}},{"anchor_refs":["1:3:1"],"branch_refs":[],"candidate_id":"cand_90e67649f941ab2b06ef","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000552"],"scope":"focus_ayah","source_local_id":"1:3:1:root-image-pressure","source_type":"word_analysis","support_ids":["sup_272c858fee96121a92cf","sup_5cd2ebcd0e3899a1084e"],"title":"womb and kinship pressure under the mercy-name","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:3:1","qac_refs":["1:3:1:1","1:3:1:2"],"status":"accepted"}},{"anchor_refs":["1:3:1"],"branch_refs":[],"candidate_id":"cand_635c2435c34747828997","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000552"],"scope":"focus_ayah","source_local_id":"1:3:1:surah-opening-title-55-1","source_type":"word_analysis","support_ids":["sup_0ed1d956d711789d667e","sup_272c858fee96121a92cf"],"title":"surah-opening title resonance at 55:1","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:3:1","qac_refs":["1:3:1:1","1:3:1:2"],"status":"accepted"}},{"anchor_refs":["1:3:2"],"branch_refs":[],"candidate_id":"cand_5515309fc1e575afa1d7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000552"],"scope":"focus_ayah","source_local_id":"1:3:2:closure-epithet-localized","source_type":"word_analysis","support_ids":["sup_02816da6adce33fc2739","sup_61326fbf176c211565b2"],"title":"closure epithet paired with the same root","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:3:2","qac_refs":["1:3:2:1","1:3:2:2"],"status":"accepted"}},{"anchor_refs":["1:3:2"],"branch_refs":[],"candidate_id":"cand_025e40150412f75173b9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000552"],"scope":"focus_ayah","source_local_id":"1:3:2:definite-genitive-apposition","source_type":"word_analysis","support_ids":["sup_02816da6adce33fc2739","sup_4fa5e3e0018a25417f1f"],"title":"second definite genitive in the same chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:3:2","qac_refs":["1:3:2:1","1:3:2:2"],"status":"accepted"}},{"anchor_refs":["1:3:2"],"branch_refs":[],"candidate_id":"cand_e0a7f8e4a3ea54e06ebb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000552"],"scope":"focus_ayah","source_local_id":"1:3:2:root-reprise-semantic-hinge","source_type":"word_analysis","support_ids":["sup_02816da6adce33fc2739","sup_c232b085604e158cfceb"],"title":"repeated root makes pattern difference decisive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:3:2","qac_refs":["1:3:2:1","1:3:2:2"],"status":"accepted"}},{"anchor_refs":["1:3:2"],"branch_refs":[],"candidate_id":"cand_fab3dcd67cb9c46e7fbe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000552"],"scope":"focus_ayah","source_local_id":"1:3:2:shareable-adjective-domain","source_type":"word_analysis","support_ids":["sup_02816da6adce33fc2739","sup_4dd33d41bdd71e1ff6cd"],"title":"shareable adjective field under a divine name","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:3:2","qac_refs":["1:3:2:1","1:3:2:2"],"status":"accepted"}},{"anchor_refs":["1:3:2"],"branch_refs":[],"candidate_id":"cand_2658d4ef92298f73e244","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000552"],"scope":"focus_ayah","source_local_id":"1:3:2:sound-cadence-pairing","source_type":"word_analysis","support_ids":["sup_02816da6adce33fc2739","sup_d834754f4a5016ec8ba2"],"title":"matched onset and cadence close the pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:3:2","qac_refs":["1:3:2:1","1:3:2:2"],"status":"accepted"}},{"anchor_refs":["1:3:2"],"branch_refs":[],"candidate_id":"cand_c2784c118726435c48fa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000552"],"scope":"focus_ayah","source_local_id":"1:3:2:stable-depth-after-breadth","source_type":"word_analysis","support_ids":["sup_02816da6adce33fc2739","sup_2fafa89b7c69dfe85821"],"title":"stable mercy lands after breadth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:3:2","qac_refs":["1:3:2:1","1:3:2:2"],"status":"accepted"}},{"anchor_refs":["1:3:1"],"branch_refs":[],"candidate_id":"cand_a8883dc9a7a282d88748","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000552"],"scope":"focus_ayah","source_local_id":"1:3:1:2","source_type":"qac_morpheme","support_ids":["sup_8680094eccf25d2dee9a"],"title":"QAC root occurrence: ر ح م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["1:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"1:3","branch_refs":["root_000552/B001"],"candidate_id":"cand_cd0ae7737ec400621108","commentary_obligation":"review","hft_ref":"hft_f5fb5603ed43ce7e724b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b-mercy-double-register","source_type":"hft","support_ids":["sup_20bee313d3d1fd1fd1a1"],"title":"b-mercy-double-register","trust":"legacy_unbound"},{"anchor_refs":["1:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"1:3","branch_refs":["root_000552/B002"],"candidate_id":"cand_fe32ac952ea4fa4a9c2d","commentary_obligation":"review","hft_ref":"hft_b0bffc2a1b10649a1f07","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b-mercy-as-kinship","source_type":"hft","support_ids":["sup_7599367ac31807367809"],"title":"b-mercy-as-kinship","trust":"legacy_unbound"},{"anchor_refs":["1:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"1:3","branch_refs":["root_000552/B003"],"candidate_id":"cand_c5e46909163d28966a09","commentary_obligation":"review","hft_ref":"hft_d816e8ca79a89a061d34","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b-mercy-as-womb","source_type":"hft","support_ids":["sup_bc9f3e0dd94d781c05aa"],"title":"b-mercy-as-womb","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"1:3:1:1","qac_word_ref":"1:3:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"رَّحْمَٰن","morph_features":"STEM|POS:ADJ|LEM:r~aHoma`n|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:3:1:2","qac_word_ref":"1:3:1","root_ar":"ر ح م","surface_ar":"رَّحْمَٰنِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"1:3:2:1","qac_word_ref":"1:3:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"رَّحِيم","morph_features":"STEM|POS:ADJ|LEM:r~aHiym|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:3:2:2","qac_word_ref":"1:3:2","root_ar":"ر ح م","surface_ar":"رَّحِيمِ"}],"word_analysis_qac_refs":[["1:3:1:1","1:3:1:2"],["1:3:2:1","1:3:2:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["1:3:1","1:3:2"]},"focus_surface_evidence":{"arabic_uthmani":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"1:3:1:1","qac_word_ref":"1:3:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"رَّحْمَٰن","morph_features":"STEM|POS:ADJ|LEM:r~aHoma`n|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:3:1:2","qac_word_ref":"1:3:1","root_ar":"ر ح م","surface_ar":"رَّحْمَٰنِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"1:3:2:1","qac_word_ref":"1:3:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"رَّحِيم","morph_features":"STEM|POS:ADJ|LEM:r~aHiym|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:3:2:2","qac_word_ref":"1:3:2","root_ar":"ر ح م","surface_ar":"رَّحِيمِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["1:3:1:1","1:3:1:2"],["1:3:2:1","1:3:2:2"]],"word_analysis_refs":["1:3:1","1:3:2"],"word_rows":[{"analysis_record_ref":"1:3:1","analytic_gloss_range_en":"definite divine mercy-name in genitive apposition, carrying broad overflowing mercy and continuing the praise-lordship chain from 1:2","analytic_root_gloss_range_en":"root range centered on mercy, tenderness, and compassion, with related kinship and womb branches; the local divine name selects mercy while allowing generative-care image pressure","qac_refs":["1:3:1:1","1:3:1:2"],"root":{"arabic":"ر ح م","transliteration":"r-ḥ-m"},"surface":{"arabic":"ٱلرَّحْمَٰنِ","transliteration":"ar-raḥmāni"}},{"analysis_record_ref":"1:3:2","analytic_gloss_range_en":"definite divine mercy-name in the same genitive pair, carrying enduring and directed mercy as the closing counterpart to the prior breadth","analytic_root_gloss_range_en":"root range centered on mercy, tenderness, and compassion, with related kinship and womb branches; the local second epithet selects sustained mercy within the paired divine-name frame","qac_refs":["1:3:2:1","1:3:2:2"],"root":{"arabic":"ر ح م","transliteration":"r-ḥ-m"},"surface":{"arabic":"ٱلرَّحِيمِ","transliteration":"ar-raḥīmi"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":2,"words_total":2,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["1:3"],"branch_refs":["root_000552/B001"],"candidate_id":"cand_cd0ae7737ec400621108","evidence_scope":"focus_ayah","hft_ref":"hft_f5fb5603ed43ce7e724b","item_id":"b-mercy-double-register","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b-mercy-double-register","support_id":"sup_20bee313d3d1fd1fd1a1"},{"anchor_refs":["1:3"],"branch_refs":["root_000552/B002"],"candidate_id":"cand_fe32ac952ea4fa4a9c2d","evidence_scope":"focus_ayah","hft_ref":"hft_b0bffc2a1b10649a1f07","item_id":"b-mercy-as-kinship","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b-mercy-as-kinship","support_id":"sup_7599367ac31807367809"},{"anchor_refs":["1:3"],"branch_refs":["root_000552/B003"],"candidate_id":"cand_c5e46909163d28966a09","evidence_scope":"focus_ayah","hft_ref":"hft_d816e8ca79a89a061d34","item_id":"b-mercy-as-womb","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b-mercy-as-womb","support_id":"sup_bc9f3e0dd94d781c05aa"}],"diagnostics":[],"lane_counts":{"global":10,"macro":10,"micro":3},"packet_summary":{"ayah_count":7,"focus_ref":"1:3","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001064","furuq_root_norm":"ع و ن","furuq_source_root_norm":"ع و ن","is_dominant":true,"target_occurrences":10,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001069","furuq_root_norm":"ع ي ن","furuq_source_root_norm":"ع ي ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["1:1","1:2","1:3","1:4","1:5","1:6","1:7"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"1:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"1:3","lane":"micro","linguistic_source_ref":"1:3","surface_ref":"1:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"1:3","target_tokens":[["Merhameti",["1:3:1"]],["sınırsızdır",["1:3:1"]],["merhamet",["1:3:2"]],["edendir",["1:3:2"]]],"text":"Merhameti sınırsızdır, merhamet edendir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":7,"id":"s001-p01-001-007","label":"Whole surah","number":1,"refs":["1:1","1:2","1:3","1:4","1:5","1:6","1:7"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:2","source_type":"word_analysis","support_id":"sup_02816da6adce33fc2739","text":"{\"gloss_range\":\"definite divine mercy-name in the same genitive pair, carrying enduring and directed mercy as the closing counterpart to the prior breadth\",\"prose\":\"The second word is not an afterthought; its own definiteness and genitive case keep it inside the same name-chain that reaches back to 1:2. It can complete the first name as a close appositive pair or stand as another direct attribute of the divine referent, so the grammar lets the second name both answer the first and remain independently attached. Its fa'il pattern changes the mode of mercy from broad overflow to durable, directed care, and the final position makes that sustained mercy the landing point of the ayah. Because this form can also function as a shareable adjective and a frequent closing epithet, the local use bridges divine naming with relational mercy while still staying a definite divine name here. The repeated root, matched onset, long-vowel contrast, and final kasra make the two words sound like one balanced mercy utterance, with the small pattern shift carrying the semantic hinge.\",\"root_display\":\"{{ar:ر ح م}} ({{tr:r-ḥ-m}})\",\"root_gloss_range\":\"root range centered on mercy, tenderness, and compassion, with related kinship and womb branches; the local second epithet selects sustained mercy within the paired divine-name frame\",\"surface_display\":\"{{ar:ٱلرَّحِيمِ}} ({{tr:ar-raḥīmi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:1:surah-opening-title-55-1","source_type":"word_analysis","support_id":"sup_0ed1d956d711789d667e","text":"{\"blocking_evidence\":null,\"headline\":\"surah-opening title resonance at 55:1\",\"reader_payoff\":\"The reader can hear a broader Quranic threshold use of the title at 55:1, while the local word remains an appositive epithet in 1:3.\",\"reason\":\"The 55:1 reference supports title resonance and opening placement, but local genitive grammar keeps the 1:3 function subordinate to the 1:2 chain.\",\"representative_source_ids\":[\"QI-6c335e12\",\"MI-ea1fcad4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:1","source_type":"word_analysis","support_id":"sup_272c858fee96121a92cf","text":"{\"gloss_range\":\"definite divine mercy-name in genitive apposition, carrying broad overflowing mercy and continuing the praise-lordship chain from 1:2\",\"prose\":\"The first word does not restart the discourse; its genitive form keeps 1:3 attached to 1:2, where it can qualify the divine referent as both attribute and name-equivalent. Its definiteness and proper-name register make the mercy-name familiar from 1:1, not an indefinite adjective or ordinary human description. The fa'lan pattern makes mercy feel broad and overflowing, while the local setting ties that overflow to lordship as care rather than bare rule; the womb and kinship branches remain image-pressure, adding generative shelter without replacing the selected divine name. Because the exact mercy pair from 1:1 returns at 1:3, praise and lordship are ringed by mercy; the same title also has a surah-opening role at 55:1, where its threshold force is visible without controlling the local grammar. The lack of conjunction and shared r-h-m sound make this first word the opening half of one compact pair, and the doubled onset makes definiteness audible.\",\"root_display\":\"{{ar:ر ح م}} ({{tr:r-ḥ-m}})\",\"root_gloss_range\":\"root range centered on mercy, tenderness, and compassion, with related kinship and womb branches; the local divine name selects mercy while allowing generative-care image pressure\",\"surface_display\":\"{{ar:ٱلرَّحْمَٰنِ}} ({{tr:ar-raḥmāni}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:2:stable-depth-after-breadth","source_type":"word_analysis","support_id":"sup_2fafa89b7c69dfe85821","text":"{\"blocking_evidence\":null,\"headline\":\"stable mercy lands after breadth\",\"reader_payoff\":\"The reader notices that the second name does not merely repeat the first; it turns broad mercy into enduring and directed care.\",\"reason\":\"The adjacency to the first word and the fa'il pattern support a contrast between breadth and durability within the same mercy root.\",\"representative_source_ids\":[\"QS-4e3130ca\",\"QF-795b5ef5\",\"QY-f48f6d7c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:2:shareable-adjective-domain","source_type":"word_analysis","support_id":"sup_4dd33d41bdd71e1ff6cd","text":"{\"blocking_evidence\":null,\"headline\":\"shareable adjective field under a divine name\",\"reader_payoff\":\"The reader senses that this epithet names divine mercy in a form intelligible as relational mercy, while the local definiteness keeps it from becoming an ordinary adjective.\",\"reason\":\"The local QAC tag is proper noun and definite, so the broader adjective-domain claim survives only as lexical pressure, not as a shift away from divine-name function.\",\"representative_source_ids\":[\"QS-0dc1ebfd\",\"MS-a5358097\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:2:definite-genitive-apposition","source_type":"word_analysis","support_id":"sup_4fa5e3e0018a25417f1f","text":"{\"blocking_evidence\":null,\"headline\":\"second definite genitive in the same chain\",\"reader_payoff\":\"The reader sees the second word as grammatically attached to the same continuing divine-name chain, not as a loose adjective after the first.\",\"reason\":\"The local form is definite and genitive, and attachment evidence licenses the paired appositional sequence.\",\"representative_source_ids\":[\"QG-a3bfe629\",\"QG-a5454f63\",\"MT-6d8b9182\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:1:root-image-pressure","source_type":"word_analysis","support_id":"sup_5cd2ebcd0e3899a1084e","text":"{\"blocking_evidence\":null,\"headline\":\"womb and kinship pressure under the mercy-name\",\"reader_payoff\":\"The reader can sense generative shelter and relational nearness beneath the mercy-name while keeping mercy as the selected local sense.\",\"reason\":\"V4 separates mercy, kinship, and womb branches, so the local word should not be made to mean womb or kinship directly; those branches survive as image-pressure tied to the root family.\",\"representative_source_ids\":[\"QS-c021295c\",\"MS-21c9d264\",\"MS-3dd58aa8\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:2:closure-epithet-localized","source_type":"word_analysis","support_id":"sup_61326fbf176c211565b2","text":"{\"blocking_evidence\":null,\"headline\":\"closure epithet paired with the same root\",\"reader_payoff\":\"The reader hears a familiar closing-epithet force, but here the closure comes by doubling the same mercy root rather than by pairing mercy with a different attribute.\",\"reason\":\"The word is final in the two-word ayah and the critical rows press its recurrent closure profile without requiring a nonlocal sense.\",\"representative_source_ids\":[\"QI-9c1de0d0\",\"MI-762bfb1f\",\"QT-cd066429\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:1:genitive-apposition-boundary","source_type":"word_analysis","support_id":"sup_724702948b5a584f3539","text":"{\"blocking_evidence\":null,\"headline\":\"genitive apposition carries the prior ayah forward\",\"reader_payoff\":\"The reader notices that 1:3 begins inside the grammatical chain of 1:2 rather than as a fresh independent sentence.\",\"reason\":\"The local word is genitive and the bundle identifies no internal governor in 1:3, so the appositional reading back to 1:2 is locally licensed.\",\"representative_source_ids\":[\"QG-5e838d06\",\"MT-d87efb7a\",\"QB-98e6ef3b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:1:compact-pair-and-sound","source_type":"word_analysis","support_id":"sup_75eb074a3ef5fea3ca41","text":"{\"blocking_evidence\":null,\"headline\":\"first half of a compact mercy-pair\",\"reader_payoff\":\"The reader hears the first name as the opening half of a tightly joined mercy pair whose sound and pattern difference matter.\",\"reason\":\"The two local words are adjacent without conjunction, share the same root, and repeat a definite onset, so the sound and structure claims are locally anchored.\",\"representative_source_ids\":[\"QT-02dbe12f\",\"QE-65bdbec4\",\"QP-63209c82\",\"QY-7cd56f60\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"1:3:1:2","source_type":"qac_morpheme","support_id":"sup_8680094eccf25d2dee9a","text":"{\"lemma_ar\":\"رَّحْمَٰن\",\"morph_features\":\"STEM|POS:ADJ|LEM:r~aHoma`n|ROOT:rHm|MS|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"1:3:1:2\",\"qac_word_ref\":\"1:3:1\",\"root_ar\":\"ر ح م\",\"surface_ar\":\"رَّحْمَٰنِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:2:root-reprise-semantic-hinge","source_type":"word_analysis","support_id":"sup_c232b085604e158cfceb","text":"{\"blocking_evidence\":null,\"headline\":\"repeated root makes pattern difference decisive\",\"reader_payoff\":\"The reader notices that the ayah refines one mercy root through a second pattern rather than listing unrelated attributes.\",\"reason\":\"Both local words share the same root and adjacent sound frame, so the formal difference carries the semantic contrast.\",\"representative_source_ids\":[\"QE-a8e61bfa\",\"QE-cd63546a\",\"ME-e3bd8f83\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:1:familiar-definite-divine-title","source_type":"word_analysis","support_id":"sup_c8e3357a8bd067782315","text":"{\"blocking_evidence\":null,\"headline\":\"definite proper-name register\",\"reader_payoff\":\"The reader hears a recognized divine title already active from 1:1, not a newly introduced indefinite descriptor.\",\"reason\":\"The local form is definite and tagged as a proper noun, with the contextual profile dominated by divine reference.\",\"representative_source_ids\":[\"QG-e0cfccdc\",\"QF-518f682d\",\"QS-e260aeb2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:2:sound-cadence-pairing","source_type":"word_analysis","support_id":"sup_d834754f4a5016ec8ba2","text":"{\"blocking_evidence\":null,\"headline\":\"matched onset and cadence close the pair\",\"reader_payoff\":\"The reader hears the closing name as the balanced second half of one mercy utterance, with repeated onset pressure and cadence binding the pair.\",\"reason\":\"The local pair shares the definite onset, r-h-m consonant frame, and final genitive vowel while contrasting the long vowels.\",\"representative_source_ids\":[\"QP-8a313077\",\"QP-b1ecb57c\",\"MP-d5a4cade\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:1:basmala-reprise-ring","source_type":"word_analysis","support_id":"sup_d9badd7741765a383942","text":"{\"blocking_evidence\":null,\"headline\":\"the opening formula returns as a mercy ring\",\"reader_payoff\":\"The reader notices that the phrase from 1:1 returns in 1:3, placing the praise and lordship statement of 1:2 inside a mercy frame.\",\"reason\":\"The critical rows give the concrete 1:1 to 1:3 reprise, and nothing in the local evidence blocks the formulaic ring reading.\",\"representative_source_ids\":[\"QI-5f0d2c7c\",\"QE-938953bd\",\"QY-8b07f33d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:3:1:overflowing-mercy-lordship","source_type":"word_analysis","support_id":"sup_fbeb59f860e5554e459c","text":"{\"blocking_evidence\":null,\"headline\":\"overflowing mercy specifies lordship as care\",\"reader_payoff\":\"The reader feels lordship after 1:2 being interpreted through overflowing mercy and care, not through bare possession or rule alone.\",\"reason\":\"The canonical local name is a definite divine epithet in the continuing chain, and the critical rows coherently press the fa'lan breadth and mercy frame without contradicting local grammar.\",\"representative_source_ids\":[\"QF-31dfe31e\",\"QS-462f9088\",\"QB-0bc655e2\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ","ayah_ref":"1:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000552/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000552","role":"Tenderness and beneficent mercy supply the shared substance, while the doubled morphology distributes it across expansive reach and durable action.","root":"ر ح م","source_ref":"1:3","source_word_indices":["1","2"]}],"changed_reading":{"after":"The pair stages one mercy in two temporal registers: overflowing in scope and remaining available in action.","before":"Two near-synonymous titles both say that God is merciful."},"confidence":"strong","focus_anchor":"The two adjacent adjectives at words 1-2 repeat one root in two forms.","mechanism":"The pair does more than duplicate a quality: the first form can present mercy at full reach, while the second presents it as settled and repeatedly operative. The sequence moves from amplitude to continuance.","model_id":"b-mercy-double-register"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b-mercy-double-register","source_type":"hft","support_id":"sup_20bee313d3d1fd1fd1a1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ","ayah_ref":"1:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000552/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000552","role":"The kinship bond supplies durable attachment, functioning as the relational architecture beneath the two mercy epithets.","root":"ر ح م","source_ref":"1:3","source_word_indices":["1","2"]}],"changed_reading":{"after":"Mercy creates and maintains a near bond, making the recipient one whose connection is actively kept.","before":"Mercy is a favorable disposition toward an otherwise separate recipient."},"confidence":"medium","focus_anchor":"Both focus words carry the root whose inventory includes binding near relations.","mechanism":"Repeated mercy can be heard relationally: not only an emotion directed at a remote recipient, but a bond that establishes nearness and carries an obligation not to sever connection.","model_id":"b-mercy-as-kinship"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b-mercy-as-kinship","source_type":"hft","support_id":"sup_7599367ac31807367809","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ","ayah_ref":"1:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000552/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000552","role":"The womb supplies an enclosing, life-forming vessel, functioning as a material analogy for mercy's encompassing and sustaining aspects.","root":"ر ح م","source_ref":"1:3","source_word_indices":["1","2"]}],"changed_reading":{"after":"Mercy is the enclosing and nourishing condition within which the recipient can become and endure.","before":"Mercy arrives as a discrete gift to an already formed recipient."},"confidence":"exploratory","focus_anchor":"The repeated focus root directly shares the inventory that names the womb.","mechanism":"The two forms can carry a spatial-material model: encompassing protection together with ongoing nourishment. Mercy is then an environment in which dependent life is formed, not merely an intervention from outside.","model_id":"b-mercy-as-womb"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b-mercy-as-womb","source_type":"hft","support_id":"sup_bc9f3e0dd94d781c05aa","trust":"legacy_unbound"}]}
</lane_packet_json>
