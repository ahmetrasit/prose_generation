# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **1:4**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s001-fresh-20260910/s001/1_4/micro.discovery.json` and modify nothing
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
  "ayah_ref": "1:4",
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

Make the relationship between layers intelligible in positive terms: establish
the foreground meaning and show what a resonance contributes in the background.
According to the evidence, it may reinforce, expand, or shift how the primary
meaning is understood. Preserve its source, scope, and degree of certainty
within that account. The foreground's continued presence can be demonstrated
by the explanation itself, without repeated assurances after each reading.
Use varied language; "second layer" is not a required label, and "supports the
main meaning" is not an adequate description of every interpretive contribution.

Use an explicit negative when a concrete ambiguity or live counter-evidence
requires it. Preserve substantive restrictions when rewriting denials, while
letting each explanation leave the reader with what the reading contributes.
Review paragraph endings for repeated exclusions that seem to withdraw the
interpretation just developed.

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
{"branch_registry":[{"boundary":"Genel olarak buyruğa uyma çekirdektir; kulluk ve inanç düzeni bu çekirdeğin özel alanlarıdır, hesap, borç ve zorla egemenlik bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000504/B001","candidate_links":[{"candidate_id":"cand_b6d347cb5abb89b72475","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:3:2","qac_word_ref":"1:4:3","surface_ar":"دِّينِ"}],"gloss":"boyun eğerek uyma ve buna dayalı inanç düzeni","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir üstün iradesine boyun eğme ve onun buyruğuna uyma."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tanrı söz konusu olduğunda bağlılığın kulluk etme biçimini alması."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnanç yolu ve kurallar bütününün, onlara uyma ve bağlanma ilişkisi açısından adlandırılması."}}],"root_ar":"د ي ن","root_id":"root_000504","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel bağlılık çekirdeğini ve bunun kulluk ile inanç düzenine uzanan kapsamını birlikte anlatan en kısa doğal karşılıktır.","boundary_detail":"Genel olarak buyruğa uyma çekirdektir; kulluk ve inanç düzeni bu çekirdeğin özel alanlarıdır, hesap, borç ve zorla egemenlik bu dala girmez.","branch_image_ar":"الطاعة والانقياد","concept_gloss":"boyun eğerek uyma ve buna dayalı inanç düzeni","contextual_glosses":[{"applicability":"Bir kişiye veya üstün iradeye bağlılığın doğrudan anlatıldığı genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kulluk ile inanç ve kurallar düzenine uzanan özel kapsamı söylemez.","preserves":"Boyun eğme ve buyruğa uyma ilişkisini korur."},"facet_ids":["F001"],"text":"boyun eğip buyruğuna uyma","usage_role":"general"},{"applicability":"Tanrı'ya bağlılık, kulluk ve benimsenen inanç yolunun birlikte öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tanrısal alan dışındaki genel boyun eğme ve buyruğa uyma kapsamını dışarıda bırakır.","preserves":"Kulluk ile inanç ve kurallar bütününe bağlılığı korur."},"facet_ids":["F002","F003"],"text":"inanç ve kulluk düzeni","usage_role":"contextual"}],"definition":"Bir üstün iradesine boyun eğerek buyruğuna uyma ve bağlı kalma; Tanrı'ya yöneldiğinde kulluk, bir inanç yolu ve onun kurallarına bağlılık biçimini alabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir üstün iradesine boyun eğme ve onun buyruğuna uyma."},{"facet_id":"F002","role":"specialization","statement":"Tanrı söz konusu olduğunda bağlılığın kulluk etme biçimini alması."},{"facet_id":"F003","role":"extension","statement":"İnanç yolu ve kurallar bütününün, onlara uyma ve bağlanma ilişkisi açısından adlandırılması."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":null,"collision":"Türkçede çoğunlukla yalnızca kurumsal inanç sistemini düşündürür.","fit":"drifted_loanword","loses":"Boyun eğme ve buyruğa uyma çekirdeğini kendi başına açıklamaz.","preserves":"Yerleşik bir inanç ve kulluk alanına gönderme yapar."},"text":"din"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Boyun eğme, kulluk ve inanç düzeni kapsamının tümünü vermez.","preserves":"Buyruğa uyma ve bağlılık yönünü korur."},"text":"itaat"}],"identity_rationale":"Kaynak ifadesi dalın merkezine boyun eğme, uyma ve bağlılığı koyar; Tanrı'ya yönelik kulluğu, inanç yolunu ve kurallar bütününü de bu temel ilişkinin özel görünümleri olarak açıklar. Bu nedenle verilen dal kimliği kanıtla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"boyun eğme, kulluk ve inanç düzeni"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ona boyun eğdi ve buyruğuna uydu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"gerçek inanç yolu"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"hükümdarın buyruğu ya da yargısı"}],"lexicalization_note":"Dal hem yalın biçimleri hem de belirli söz öbeklerini içerir; söz öbeklerine özgü hükümdarlık ve gerçek inanç yolu anlamları yalın biçimin bütün kullanımlarına yayılmaz.","neighbor_coverage_note":"Sunulan komşuların tümü değerlendirildi; en açıklayıcı üç sınır yayımlandı. Namaz, yemin ve karşı gelme gibi adaylar aynı sahneyi paylaşsa da doğrudan anlam karışıklığı yaratmadığından, kardeş dallar ise aşağıda ayrıca işlendiğinden eklenmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği genel boyun eğme ve uyma olup kulluk ile inanç düzenine genişler; komşu dal ise dinsel nitelikli, alçak gönüllü uyma alanını merkez alır.","focus_only":"Bu dal genel buyruğa uymayı ve bundan gelişen inanç düzenini de kapsar.","gloss":"genel bağlılık ile dinsel bağlılık","neighbor_only":"Komşu dal bağlılığı özellikle dinsel yolda doğruluk ve belirli kişiler arası uyma örnekleriyle sınırlar.","neighbor_ref":"root_001260/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da üstün bir buyruğa boyun eğerek uyma vardır."},{"boundary_match":"partial","distinction":"Odak dal kulluğu daha geniş bir uyma ve bağlılık haritasının özel biçimi sayar; komşu dalda ise kulluk ve alçalış doğrudan tanımlayıcı eylemdir.","focus_only":"Odak dal genel uyma ilişkisini ve inanç ile kurallar düzenini kapsar.","gloss":"bağlılık ile kulluk","neighbor_only":"Komşu dal kulluk eylemini ve bu eylemdeki alçalışı doğrudan çekirdek yapar.","neighbor_ref":"root_000973/B003","relation_type":"near_synonym","shared_zone":"Kulluk bağlamında boyun eğme ve üstün iradeye uyma iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği uyma ve bağlılık ilişkisidir; komşu dalın çekirdeği ise kişinin benimsediği belirli inanç yolu veya gelenektir.","focus_only":"Odak dal inanç yolunun dayandığı boyun eğme ve buyruğa uyma ilişkisini açıklar.","gloss":"uyma ilişkisi ile benimsenen inanç yolu","neighbor_only":"Komşu dal benimsenen belirli inanç topluluğu veya öğreti geleneğini adlandırır.","neighbor_ref":"root_001445/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir inanç yoluna bağlanma alanında buluşur."}],"source_phrase_ar":"أصل واحد إليه يرجع فروعه كلها وهو جنس من الانقياد والذل (maqayis)؛ فالدين الطاعة (maqayis;sihah)؛ الدين لله طاعته والتعبد له (tahdhib)؛ الدين كالملة اعتبارا بالطاعة والانقياد للشريعة (mufradat)","source_summary":"Kanıt, bütün kullanımları boyun eğme ve uyma ekseninde birleştirir; kulluk ile inanç ve kural düzenini bu ilişkinin özel ve genişlemiş görünümleri olarak sunar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الدين بمعنى الطاعة والانقياد والتعبد والملة والشريعة وما يتدين به","what_is_not_ar":"ليس الحساب والجزاء ولا الدين المالي ولا المدينة المصر"},"support_links":["sup_ec98c3825f872a39c0a9"]},{"boundary":"Bu dal, bir eylem veya kişi hakkında hesap ve karşılık sonucuna varmayı anlatır; inanç düzeni, mali borç ve zorla boyun eğdirme bunun dışında kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000504/B002","candidate_links":[{"candidate_id":"cand_b6d98f0c83a6743ebe20","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:3:2","qac_word_ref":"1:4:3","surface_ar":"دِّينِ"}],"gloss":"yargılayıp hesap görerek karşılığını verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya eylem hakkında hükme varıp hesabını görmek."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hesabın sonucuna göre yapılanın karşılığını vermek."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hüküm, hesap ve karşılığın gerçekleşeceği özel günü adlandırmak."}}],"root_ar":"د ي ن","root_id":"root_000504","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hüküm, hesap ve eylemin sonucuna göre karşılık verme aşamalarını birlikte taşıyan genel kavram karşılığıdır.","boundary_detail":"Bu dal, bir eylem veya kişi hakkında hesap ve karşılık sonucuna varmayı anlatır; inanç düzeni, mali borç ve zorla boyun eğdirme bunun dışında kalır.","branch_image_ar":"الحساب والجزاء","concept_gloss":"yargılayıp hesap görerek karşılığını verme","contextual_glosses":[{"applicability":"Hüküm ve karşılık sürecinin gerçekleşeceği özel günün adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kavramın gün adı dışındaki genel yargılama ve karşılık kullanımlarını dışarıda bırakır.","preserves":"Hesap görme ve karşılık verme olayını korur."},"facet_ids":["F001","F002","F003"],"text":"hesap ve karşılık günü","usage_role":"contextual"},{"applicability":"Bir kişinin veya eylemin değerlendirilip sonucuna göre karşılık gördüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hesap görme ile sonuca göre karşılık verme sırasını korur."},"facet_ids":["F001","F002"],"text":"hesaba çekilip karşılığının verilmesi","usage_role":"general"}],"definition":"Bir eylemi veya kişiyi hükme bağlayıp hesabını görmek ve sonucuna göre karşılığını vermek; belirli bir gün adı olarak bu sürecin gerçekleşeceği zamanı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya eylem hakkında hükme varıp hesabını görmek."},{"facet_id":"F002","role":"core","statement":"Hesabın sonucuna göre yapılanın karşılığını vermek."},{"facet_id":"F003","role":"specialization","statement":"Hüküm, hesap ve karşılığın gerçekleşeceği özel günü adlandırmak."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hükme varma ve sonuca göre karşılık verme aşamalarını açıkça taşımaz.","preserves":"Eylemlerin değerlendirilmesi ve hesabının görülmesi yönünü korur."},"text":"hesap"},{"category":"confusable","error_profile":{"adds":"Karşılığın mutlaka olumsuz ve yaptırım niteliğinde olduğu izlenimini ekler.","collision":"Genel karşılık sürecini yalnızca yaptırımla karıştırır.","fit":"narrowing","loses":"Hesap, hüküm ve olumlu ya da olumsuz her tür karşılık kapsamını kaybeder.","preserves":"Olumsuz bir eyleme verilen karşılık yönünü koruyabilir."},"text":"ceza"}],"identity_rationale":"Kaynak ifadesi hüküm verme, hesap görme, yapılanın karşılığını verme ve bunların gerçekleşeceği özel günü aynı anlam örgüsünde açıkça birleştirir. Verilen hesap ve karşılık çerçevesi bu kanıtı doğru temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"hesap, yargı ve yapılanın karşılığı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"hesap ve karşılık günü"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"hesaba çekilip karşılığı verilecek olanlar"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yargılayan ve karşılığını veren"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"hükümdarın buyruğu ya da yargısı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kendini alçalttı ya da hesaba çekti"}],"lexicalization_note":"Dal yalın biçimler, türemiş biçimler ve belirli bir gün adını içeren söz öbeğini birlikte taşır; günle sınırlı kullanım bütün dala genellenmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; karşılık verme ve hüküm alanındaki en yakın üç sınır seçildi. Salt yaptırım, pay, borç veya kardeş dal ilişkisi sunan adaylar ya daha dar kaldı ya da yayımlanan ayrımları yineledi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hesap ve hüküm aşamalarını karşılıkla birlikte kurar; komşu dal ise karşılıklı ödül, yaptırım veya ödeşme eylemini öne çıkarır.","focus_only":"Odak dal karşılıktan önce hükme varma ve hesabı görme aşamalarını da içerir.","gloss":"hesaplı yargı ile eyleme karşılık","neighbor_only":"Komşu dal bir eyleme iyilik veya kötülükle denk karşılık vermeyi doğrudan merkez alır.","neighbor_ref":"root_000244/B001","relation_type":"near_synonym","shared_zone":"Her iki dal yapılan bir eylemin sonucuna göre karşılık verilmesini kapsar."},{"boundary_match":"partial","distinction":"Odak dal kurumsal veya sonul bir hüküm ve hesap sürecini içerir; komşu dalda asıl vurgu yapılan işin sahibine dönen sonucundadır.","focus_only":"Odak dal yargılama, hesap görme ve özel gün kullanımını birlikte taşır.","gloss":"hesap ve karşılık ile işin geri dönüşü","neighbor_only":"Komşu dal karşılığı, kişinin yaptığı işin kendisine geri dönen sonucu olarak kurar.","neighbor_ref":"root_000209/B002","relation_type":"near_synonym","shared_zone":"İki dalda da kişinin yaptığı iş nedeniyle bir sonuç veya karşılık görmesi vardır."},{"boundary_match":"partial","distinction":"Odak dal kişinin veya eylemin hesabını ve karşılığını konu edinir; komşu dal iki taraf arasındaki çekişmeyi yargısal kararla sona erdirir.","focus_only":"Odak dal hesap sonucunda karşılık vermeyi ve özel gün kullanımını kapsar.","gloss":"hesap verdirme ile uyuşmazlığı hükme bağlama","neighbor_only":"Komşu dal çekişen taraflar arasında uyuşmazlığı kararla kapatan yargı eylemine odaklanır.","neighbor_ref":"root_001124/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bir değerlendirme sonunda bağlayıcı hükme varma alanındadır."}],"source_phrase_ar":"يوم الدين أي يوم الحكم والحساب والجزاء (maqayis)؛ الدين الجزاء والمكافأة (sihah)؛ الدين الحساب ومنه مالك يوم الدين ومالك يوم الجزاء (tahdhib)؛ غير مدينين أي غير مجزيين (mufradat)","source_summary":"Kanıt hüküm, hesap ve karşılık vermeyi tek bir süreçte toplar; özel gün kullanımı ile hesaba çekilip karşılığı verilen kişi biçimleri de bu sürece bağlanır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الدين بمعنى الحكم والحساب والجزاء والمكافأة والقضاء","what_is_not_ar":"ليس الطاعة والشريعة ولا القرض والمداينة"},"support_links":["sup_5e5a60a15581f02f2ebd"]},{"boundary":"Dal, malın şimdi verilip yükümlülüğün ileride yerine getirildiği mali ilişkiyle sınırlıdır; hesap günü, inanç bağlılığı ve genel alışveriş bununla özdeş değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000504/B003","candidate_links":[{"candidate_id":"cand_ceeeb8799a41d7f31756","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:3:2","qac_word_ref":"1:4:3","surface_ar":"دِّينِ"}],"gloss":"borç alıp verme ve vadeli ödeme ilişkisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Mal veya paranın borç olarak alınması ya da verilmesiyle mali yükümlülük doğması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birine ödünç vererek onu geri ödeme yükümlüsü kılmak."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başkasından ödünç alarak geri ödeme yükümlülüğü altına girmek."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Alışverişte bedelin ileri bir tarihe bırakılması."}}],"root_ar":"د ي ن","root_id":"root_000504","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Borç nesnesini, iki taraflı işlemi ve ileride ödeme yükümlülüğünü birlikte anlatan genel karşılıktır.","boundary_detail":"Dal, malın şimdi verilip yükümlülüğün ileride yerine getirildiği mali ilişkiyle sınırlıdır; hesap günü, inanç bağlılığı ve genel alışveriş bununla özdeş değildir.","branch_image_ar":"الدين المالي","concept_gloss":"borç alıp verme ve vadeli ödeme ilişkisi","contextual_glosses":[{"applicability":"Tarafların borç veren ve borç alan olarak kurduğu genel mali bağ anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Vadeli alışveriş ile alma ve verme işlemlerinin ayrı yönlerini açıkça göstermez.","preserves":"Mali yükümlülük ve iki taraflı borç bağını korur."},"facet_ids":["F001"],"text":"borç ilişkisi","usage_role":"general"},{"applicability":"Bir kişinin başkasına geri ödenmek üzere mal veya para sağladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Borç alma yönünü ve vadeli alışveriş kapsamını dışarıda bırakır.","preserves":"Borç ilişkisinin veren tarafını ve geri ödeme beklentisini korur."},"facet_ids":["F001","F002"],"text":"ödünç verme","usage_role":"contextual"},{"applicability":"Bir kişinin ödünç alarak geri ödeme yükümlülüğü altına girdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Borç verme yönünü ve vadeli satışın özel yapısını dışarıda bırakır.","preserves":"Borç alan tarafı ve üstlenilen mali yükümlülüğü korur."},"facet_ids":["F001","F003"],"text":"borçlanma","usage_role":"contextual"}],"definition":"Bir mal veya paranın borç olarak alınıp verilmesiyle, taraflardan biri için ileride ödeme ya da geri verme yükümlülüğü doğuran mali ilişki; vadeli alışveriş de bu ilişkinin özel bir biçimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Mal veya paranın borç olarak alınması ya da verilmesiyle mali yükümlülük doğması."},{"facet_id":"F002","role":"specialization","statement":"Birine ödünç vererek onu geri ödeme yükümlüsü kılmak."},{"facet_id":"F003","role":"specialization","statement":"Başkasından ödünç alarak geri ödeme yükümlülüğü altına girmek."},{"facet_id":"F004","role":"extension","statement":"Alışverişte bedelin ileri bir tarihe bırakılması."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kurumsal finansman veya banka ürünü çağrışımını gereksiz biçimde ekler.","collision":"Genel borç ilişkisini modern bir finans ürünüyle karıştırır.","fit":"narrowing","loses":"Kişiler arası ödünç verme ile her tür vadeli alışverişi kapsamaz.","preserves":"Sonradan geri ödeme yükümlülüğü doğuran mali kaynak yönünü koruyabilir."},"text":"kredi"},{"category":"alternative","error_profile":{"adds":"Peşin ve borç doğurmayan bütün alım satım işlemlerini kapsama ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Vadeli satış örneğinde taraflar arasındaki mali işlemi korur."},"text":"alışveriş"}],"identity_rationale":"Kaynak ifadesi mali borcu, vadeli alıp vermeyi, borçla alışverişi ve ödünç alma ya da verme yönlerini açıkça aynı dalda toplar. Verilen mali ilişki çerçevesi bu karşılıklı tarafları doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"borç ve vadeli ödeme yükümlülüğü"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"onunla borç alıp verme işlemi yaptı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ona ödünç verdi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ödünç aldı ve borçlandı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"borçlu veya çok borçlanmış kişi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"onu vadeli olarak sattım"}],"lexicalization_note":"Yalın borç adı, borç alma ve verme eylemleri ile vadeli satış söz öbeği ayrı ayrı korunur; vadeli satışa özgü anlam bütün yalın kullanımlara yüklenmez.","neighbor_coverage_note":"Bütün komşular değerlendirildi; avans, borç aktarımı ve genel satışla olan üç temel sınır seçildi. Borç bakiyesi, güvence, ödünç satış türü ve para adı adayları bu ayrımları dar bir örnekle yinelediği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal taraflar arasında doğan borç bağının iki yönünü anlatır; komşu dal ise işlemin başında öne sürülen para veya bedele odaklanır.","focus_only":"Odak dal ödünç alma, borçlanma ve ileride ödeme yükümlülüğünü de kapsar.","gloss":"borç ilişkisi ile önceden verilen para","neighbor_only":"Komşu dal özellikle önceden verilen para veya satış bedelini nesne olarak öne çıkarır.","neighbor_ref":"root_000733/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir mal veya para, daha sonraki karşılıkla bağlantılı olarak verilir."},{"boundary_match":"field_only","distinction":"Odak dalda borç ilişkisi kurulur veya üstlenilir; komşu dalda ise önceden var olan borcun muhatabı değiştirilir.","focus_only":"Odak dal borcu doğuran alma, verme ve vadeli işlem sürecini anlatır.","gloss":"borç kurma ile borcu aktarma","neighbor_only":"Komşu dal var olan borcun başka bir kişiye veya borçluya aktarılmasını anlatır.","neighbor_ref":"root_000373/B010","relation_type":"same_field","shared_zone":"İki dal da alacaklı ve borçlu arasındaki mali yükümlülük alanındadır."},{"boundary_match":"field_only","distinction":"Odak dalın ayırıcı özelliği borç veya vade doğurmasıdır; komşu dalın çekirdeği ise vade şartı olmaksızın satış ve satın almadır.","focus_only":"Odak dal ödemenin veya geri vermenin ileri tarihe bırakıldığı yükümlülüğü gerektirir.","gloss":"vadeli borç işlemi ile genel satış","neighbor_only":"Komşu dal peşin ya da vadeli olabilen genel mal ve bedel değişimini kapsar.","neighbor_ref":"root_000169/B001","relation_type":"same_field","shared_zone":"Her iki dal mal ile bedelin taraflar arasında değiştiği işlemleri kapsayabilir."}],"source_phrase_ar":"الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء (maqayis)؛ الدين واحد الديون وتداينوا تبايعوا بالدين (sihah)؛ دنت الرجل أقرضته وأدنت الرجل إذا أقرضته (tahdhib)؛ التداين والمداينة دفع الدين (mufradat)","source_summary":"Kanıt borcu tek taraflı bir nesne olarak değil, alma ve verme yönleri bulunan bir mali işlem olarak açıklar; ödünç verme, ödünç alma ve vadeli alışveriş bu ortak yapının görünümleridir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الدين المالي والقرض والاستقراض والمداينة والبيع إلى أجل وما يؤخذ أو يعطى دينا","what_is_not_ar":"ليس الطاعة الدينية ولا الجزاء الأخروي ولا الذل المجرد"},"support_links":["sup_9076b32659455b9ab4a1"]},{"boundary":"Zorlama, alçaltma ve sahiplik bu dalı gönüllü uyma dalından ayırır; mali borçlu olma ya da hesap verme tek başına bu anlama girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000504/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:3:2","qac_word_ref":"1:4:3","surface_ar":"دِّينِ"}],"gloss":"zorla alçaltıp egemenliği altına alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birini zor kullanarak alçaltmak ve egemenlik altına almak."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Egemenlik altına alınan kişiyi köleleştirmek veya mülk edinmek."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Egemenlik altındaki erkek veya kadını köleleştirilmiş kişi olarak adlandırmak."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir deyimde kalbi alçaltan veya kişiyi istemediği şeye zorlayan etkeni anlatmak."}}],"root_ar":"د ي ن","root_id":"root_000504","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Alçaltma, zorlama ve sahiplik sonucunu tek bir egemenlik ilişkisi içinde anlatan genel karşılıktır.","boundary_detail":"Zorlama, alçaltma ve sahiplik bu dalı gönüllü uyma dalından ayırır; mali borçlu olma ya da hesap verme tek başına bu anlama girmez.","branch_image_ar":"الإذلال والملك","concept_gloss":"zorla alçaltıp egemenliği altına alma","contextual_glosses":[{"applicability":"Bir topluluk veya kişinin zorla egemenlik altına sokulduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mülk edinme ile köleleştirilmiş kişi adlarını açıkça taşımaz.","preserves":"Zorlama, alçaltma ve egemenlik kurma yönlerini korur."},"facet_ids":["F001"],"text":"boyunduruk altına alma","usage_role":"general"},{"applicability":"Bir insanın mülk ve bağımlı kişi durumuna getirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Köleliğe varmayan genel alçaltma ve zorlama kullanımlarını dışarıda bırakır.","preserves":"Egemenlik altına alma, mülk edinme ve bağımlı kılma yönlerini korur."},"facet_ids":["F001","F002","F003"],"text":"köleleştirme","usage_role":"contextual"},{"applicability":"Fiziksel sahiplikten çok kişinin onurunu kırıp onu aşağı duruma düşürmenin öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Egemenlik, köleleştirme ve mülk edinme sonuçlarını vermez.","preserves":"Kişiyi alçaltma ve güç altında bırakma yönünü korur."},"facet_ids":["F001"],"text":"aşağılama","usage_role":"contextual"}],"definition":"Birini zorla alçaltıp egemenlik altına almak, köleleştirmek veya mülk edinmek; bu işlemin sonucunda kişi bağımlı ve başkasının buyruğu altında sayılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birini zor kullanarak alçaltmak ve egemenlik altına almak."},{"facet_id":"F002","role":"extension","statement":"Egemenlik altına alınan kişiyi köleleştirmek veya mülk edinmek."},{"facet_id":"F003","role":"associated_use","statement":"Egemenlik altındaki erkek veya kadını köleleştirilmiş kişi olarak adlandırmak."},{"facet_id":"F004","role":"example","statement":"Bir deyimde kalbi alçaltan veya kişiyi istemediği şeye zorlayan etkeni anlatmak."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Eylemi uygulayan yerine buna uyan kişinin gönüllü davranışı izlenimini ekler.","collision":"Bu kökün gönüllü uyma dalıyla karışır.","fit":"displacement","loses":"Başkasını zorla alçaltma, köleleştirme ve mülk edinme eylemlerini kaybeder.","preserves":"Güç ilişkisi içinde aşağı konumda bulunma yönünü kısmen korur."},"text":"boyun eğme"},{"category":"confusable","error_profile":{"adds":"Kanıtta bu dal için bulunmayan mali ödeme yükümlülüğünü ekler.","collision":"Ayrı mali borç dalıyla karışır.","fit":"displacement","loses":"Alçaltma, egemenlik, köleleştirme ve sahiplik çekirdeğini bütünüyle kaybeder.","preserves":"Bir kişiyi bağımlı bir yükümlülük altına sokma çağrışımını koruyabilir."},"text":"borçlandırma"}],"identity_rationale":"Kaynak ifadesi birini alçaltma, zorla egemenlik altına alma, köleleştirme ve mülk edinme eylemlerini; ayrıca bu duruma sokulmuş erkek ve kadın adlarını aynı dalda birleştirir. Verilen zorlayıcı egemenlik çerçevesi bu yapıyı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"onu alçalttı, boyunduruk altına aldı ve köleleştirdi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"topluluğu alçalttım ve köleleştirdim"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"onu mülk edindim veya buyruğum altına aldım"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"köleleştirilmiş erkek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"köleleştirilmiş kadın"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kendini alçalttı ya da hesaba çekti"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kalbini alçaltan şey; ayrıca alışkanlık, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz"}],"lexicalization_note":"Dal eylem biçimleri, köleleştirilmiş kişiyi gösteren adlar ve tartışmalı bir deyim içerir; deyimdeki yorumlar yalın eylemin tek anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; zorla yenme, doğrudan köleleştirme ve kölelik durumu arasındaki üç sınır seçildi. Öteki güç, yönetim ve vurma adayları aynı ayrımı daha dolaylı kurduğu için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal zorlayıcı üstünlüğü sahiplik ve köleleştirme sonucuna bağlar; komşu dal ise böyle bir sonuç gerektirmeden güçle yenme ve zorlama çekirdeğinde kalır.","focus_only":"Odak dal köleleştirme, mülk edinme ve köleleştirilmiş kişi adlarını da içerir.","gloss":"köleleştirici egemenlik ile zorla yenme","neighbor_only":"Komşu dal üstün konumdan güç kullanarak yenme ve istem dışı ele geçirmeyi genel biçimde kapsar.","neighbor_ref":"root_001266/B001","relation_type":"near_synonym","shared_zone":"Her iki dal birini zorla yenip aşağı ve bağımlı duruma sokmayı kapsar."},{"boundary_match":"partial","distinction":"Odak dal köleleştirmeyi daha geniş alçaltma, sahiplik ve egemenlik alanına yerleştirir; komşu dalın çekirdeği doğrudan köle edinme veya köle gibi çalıştırmadır.","focus_only":"Odak dal genel alçaltma ve egemenlik kurmayı, ayrıca köleleştirilmiş kişi adlarını kapsar.","gloss":"egemenlik altına alma ile köleleştirme","neighbor_only":"Komşu dal birini özellikle köle durumuna getirip köle işi yaptırma eylemini merkez alır.","neighbor_ref":"root_000973/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir insanı zorla bağımlı ve köle durumuna getirebilir."},{"boundary_match":"field_only","distinction":"Odak dalın çekirdeği uygulanan alçaltıcı egemenliktir; komşu dalın çekirdeği bunun kurduğu kölelik statüsü ve mülkiyet durumudur.","focus_only":"Odak dal birini alçaltıp köleleştiren eylemi ve bu sonuca yol açan gücü anlatır.","gloss":"köleleştirme eylemi ile kölelik durumu","neighbor_only":"Komşu dal kölelik durumunu, köle mülkiyetini ve köleleştirilmiş insanlar sınıfını adlandırır.","neighbor_ref":"root_000586/B003","relation_type":"same_field","shared_zone":"Her iki dal kölelik, sahiplik ve insanın bağımlı duruma sokulması alanındadır."}],"source_phrase_ar":"العبد مدين كأنهما أذلهما العمل ويا دين قلبك أي أذل (maqayis)؛ دانه دينا أي أذله واستعبده ودينته ملكته (sihah)؛ غير مدينين غير مملوكين ودنت القوم أدينهم إذا أذللتهم (tahdhib)؛ المدين والمدينة العبد والأمة (mufradat)","source_summary":"Kanıt alçaltma ve zorla egemenlik kurmayı köleleştirme ve sahiplikle birleştirir; egemenlik altındaki erkek ve kadın adları sonuç durumunu, deyimsel kullanım ise alçaltma yönünü örnekler.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الإذلال والقهر والملك والاستعباد والحمل على المكروه والعبد المدين والأمة المدينة","what_is_not_ar":"ليس الطاعة الاختيارية ولا الحساب والجزاء ولا الدين المالي نفسه"},"support_links":[]},{"boundary":"Tekrarlanarak yerleşen davranış veya alışılmış durum çekirdektir; inanç sistemi, mali borç ve zorlayıcı egemenlik bu dala ait değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000504/B005","candidate_links":[{"candidate_id":"cand_85368a4b3f75ed141a49","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:3:2","qac_word_ref":"1:4:3","surface_ar":"دِّينِ"}],"gloss":"alışılmış davranış ve öteden beri bilinen hal","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tekrarlanarak yerleşmiş alışkanlık veya sürekli yapılan iş."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi veya topluluk için öteden beri bilinen hal, tutum ve gidiş."}}],"root_ar":"د ي ن","root_id":"root_000504","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tekrarlanan davranışı ve bundan oluşan yerleşik durum veya tutumu birlikte anlatan genel karşılıktır.","boundary_detail":"Tekrarlanarak yerleşen davranış veya alışılmış durum çekirdektir; inanç sistemi, mali borç ve zorlayıcı egemenlik bu dala ait değildir.","branch_image_ar":"العادة والشأن","concept_gloss":"alışılmış davranış ve öteden beri bilinen hal","contextual_glosses":[{"applicability":"Tekrarlanan ve kişide ya da toplulukta yerleşmiş davranışın öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Davranıştan daha geniş olan bilinen hal ve genel tutum kapsamını açıkça vermez.","preserves":"Tekrarlanarak yerleşen davranış ve olağan işi korur."},"facet_ids":["F001"],"text":"alışkanlık","usage_role":"general"},{"applicability":"Bir kişinin öteden beri bilinen durumu veya olağan gidişi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tekrarlı davranış olarak alışkanlık anlamını doğrudan belirtmez.","preserves":"Bilinen durum, olağan tutum ve süreklilik yönlerini korur."},"facet_ids":["F002"],"text":"süregelen hal ve tutum","usage_role":"contextual"}],"definition":"Bir kişinin veya topluluğun tekrarla yerleşmiş alışkanlığı, süregelen işi ya da öteden beri bilinen hali ve tutumu.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tekrarlanarak yerleşmiş alışkanlık veya sürekli yapılan iş."},{"facet_id":"F002","role":"extension","statement":"Bir kişi veya topluluk için öteden beri bilinen hal, tutum ve gidiş."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Güncel Türkçede kurumsal inanç sistemi anlamını baskın biçimde ekler.","collision":"Aynı kökün inanç ve bağlılık dalıyla karışır.","fit":"drifted_loanword","loses":"Alışkanlık ve öteden beri bilinen hal anlamını güncel kullanımda göstermez.","preserves":"Tarihsel kullanımda yerleşik yol veya tutum çağrışımını kısmen koruyabilir."},"text":"din"},{"category":"alternative","error_profile":{"adds":"Fiziksel güzergah, yöntem ve araç gibi ilgisiz anlamları kapsama ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Yerleşik davranış biçimi ve olağan gidiş yönünü kısmen korur."},"text":"yol"}],"identity_rationale":"Kaynak ifadesi sözcüğü alışkanlık, süregelen iş, bilinen hal ve kişinin öteden beri tanınan durumu olarak açıklar. Verilen alışkanlık ve durum çerçevesi bu ortak anlamı eksiksiz karşılar.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"alışkanlık, olağan iş ve öteden beri bilinen hal"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kalbinin alışkanlığı; ayrıca alçaltma, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz"}],"lexicalization_note":"Dal yalın alışkanlık adını ve yorumları ayrışan bir deyimi içerir; deyimin alçaltma, zorlama veya gönül derdi yorumları yalın alışkanlık anlamına eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sürekli alışkanlık, ısrarlı uğraş ve izlenen yol ile kurulan üç sınır seçildi. Öbür adaylar huy, örnek alma veya düzgün gidiş gibi daha dar örnekler sunduğundan eklenmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yerleşik alışkanlıktan bilinen hale genişler; komşu dalın ayırıcı yönü işin kesintisiz veya düzenli biçimde aynı halde sürmesidir.","focus_only":"Odak dal alışkanlığın yanında kişinin bilinen hali ve genel tutumunu da kapsar.","gloss":"yerleşik alışkanlık ile sürekli gidiş","neighbor_only":"Komşu dal bir işin aynı durumda durmadan sürdürülmesini daha belirgin biçimde öne çıkarır.","neighbor_ref":"root_000456/B002","relation_type":"near_synonym","shared_zone":"Her iki dal tekrarlanarak olağanlaşan davranış ve süregelen işi anlatır."},{"boundary_match":"partial","distinction":"Odak dal nötr bir alışkanlık ve durum adıdır; komşu dal belirli bir söz veya uğraş üzerinde sürekli durma ve düşkünlük yönünü de taşır.","focus_only":"Odak dal genel alışkanlığı ve öteden beri bilinen hali kapsar.","gloss":"genel alışkanlık ile sürekli uğraş","neighbor_only":"Komşu dal bir şeyi sürekli anma veya ona düşkünlük gibi ısrarlı uğraşıları da içerir.","neighbor_ref":"root_001578/B009","relation_type":"near_synonym","shared_zone":"İki dalda da kişiye yerleşen ve yinelenen davranış veya uğraş vardır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği alışkanlık ve bilinen durumdur; komşu dal bu alanı kişinin izlediği yöntem veya yön olarak da kurar.","focus_only":"Odak dal kişinin yerleşik davranışını ve bilinen halini adlandırır.","gloss":"alışkanlık ile izlenen yol","neighbor_only":"Komşu dal alışılmış davranışın yanında izlenen yöntem, yön veya güzergah anlamını da taşır.","neighbor_ref":"root_000240/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal yerleşmiş davranış biçimi veya olağan gidiş için kullanılabilir."}],"source_phrase_ar":"العادة يقال لها دين (maqayis)؛ الدين بالكسر العادة والشأن (sihah)؛ الدين أيضا العادة (tahdhib)؛ الحال والأمر الذي تعهده (maqayis)","source_summary":"Kanıt alışkanlık ile süregelen işi ortak çekirdek sayar ve bu anlamı kişinin bilinen hali, olağan tutumu veya öteden beri tanınan durumu yönünde genişletir.","sources":["MQ","SI","TA"],"what_is_ar":"الدين بمعنى العادة والشأن والحال المعهود والدأب","what_is_not_ar":"ليس الشريعة والطاعة ولا الحساب ولا الدين المالي"},"support_links":["sup_247e039079f06dc5170b"]},{"boundary":"Kent temel anlamdır; yönetime uyma yalnızca kaynaklarda verilen adlandırma açıklamasıdır. Köleleştirilmiş kadın adı ve genel bağlılık anlamı bu dala aktarılmaz.","branch_kind":"bare","branch_ref":"root_000504/B006","candidate_links":[{"candidate_id":"cand_85368a4b3f75ed141a49","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:3:2","qac_word_ref":"1:4:3","surface_ar":"دِّينِ"}],"gloss":"kent","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanların toplu yaşadığı büyük ve düzenli yerleşim olan kent."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kent adının, yöneticilerin buyruklarına uyulan yer olmasıyla kökensel olarak açıklanması."}}],"root_ar":"د ي ن","root_id":"root_000504","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın doğrudan gösterdiği büyük ve düzenli yerleşim için eksiksiz doğal karşılıktır; adlandırma gerekçesi ayrıca açıklanır.","boundary_detail":"Kent temel anlamdır; yönetime uyma yalnızca kaynaklarda verilen adlandırma açıklamasıdır. Köleleştirilmiş kadın adı ve genel bağlılık anlamı bu dala aktarılmaz.","branch_image_ar":"مدينة الطاعة","concept_gloss":"kent","contextual_glosses":[{"applicability":"Kent sözcüğünün yerleşim türü olarak açıklanmasının gerektiği bağlamlarda kullanılır.","error_profile":{"adds":"Kent düzeyinde örgütlenmemiş büyük yerleşimleri de kapsayabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"İnsanların toplu yaşadığı geniş yerleşim olma yönünü korur."},"facet_ids":["F001"],"text":"büyük yerleşim","usage_role":"explanatory"}],"definition":"İnsanların toplu yaşadığı büyük ve düzenli yerleşim, yani kent. Adlandırılması, o yerde yöneticilerin buyruklarına uyulmasıyla açıklanır; bu ilişki kentin zorunlu özelliği değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanların toplu yaşadığı büyük ve düzenli yerleşim olan kent."},{"facet_id":"F002","role":"source_variant","statement":"Kent adının, yöneticilerin buyruklarına uyulan yer olmasıyla kökensel olarak açıklanması."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yalnızca belirli bir yönetim biçimine bağlı özel kent türü olduğu izlenimini ekler.","collision":"Adlandırma açıklamasını tanımlayıcı bir kent alt türüyle karıştırır.","fit":"displacement","loses":"Her tür kenti karşılayan yalın ve genel yerleşim anlamını kaybeder.","preserves":"Kent adıyla yönetime uyma arasında kurulan kökensel bağı korur."},"text":"buyruk kenti"}],"identity_rationale":"Kaynak ifadesinin doğrudan gösterdiği varlık kent veya büyük yerleşimdir. Yöneticilerin buyruğuna uyulması, bu yer adının neden aynı kök ailesinde açıklandığına ilişkin bir adlandırma gerekçesidir; her kentin tanımlayıcı koşulu değildir. Dal korunabilir, ancak tanım bu ayrımı açıkça yapmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kent; yöneticilerin buyruğuna uyulan yer olarak açıklanan büyük yerleşim"}],"lexicalization_note":"Mekanik sınıf yalındır; tanım kent biçiminin yerleşim anlamıyla sınırlı tutulur ve adlandırma açıklaması bağımsız bir anlam gibi genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel kent, köyleri toplayan bölge ve yönetici rolüyle kurulan üç sınır seçildi. Özel yer adları yalnızca örnek, karşı gelme ve kardeş dallar ise kökensel ya da tematik bağ sunduğundan yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalın kent anlamını belirli bir adlandırma açıklamasıyla verir; komşu dalın kapsamı kentten ülkeye ve surlu yapılaşmış alana kadar genişler.","focus_only":"Odak dal kent adını yöneticilerin buyruğuna uyulan yer biçimindeki kökensel açıklamayla ilişkilendirir.","gloss":"kent ile yapılaşmış ve surlu yer","neighbor_only":"Komşu dal kentle birlikte ülke, yapılaşmış toprak ve surlu yer gibi daha geniş yer türlerini kapsar.","neighbor_ref":"root_001408/B001","relation_type":"near_synonym","shared_zone":"Her iki dal insanların toplu yaşadığı yapılaşmış büyük yerleşimi adlandırır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği kentin kendisidir; komşu dalda kent, çevredeki küçük yerleşimleri kapsayan daha geniş bir bölgesel birimin merkezi olabilir.","focus_only":"Odak dal kendi başına büyük ve düzenli yerleşim olan kenti anlatır.","gloss":"kent ile köyleri toplayan bölge","neighbor_only":"Komşu dal çevresindeki köy ve mahalleleri bir araya getiren bölge veya yönetim çevresini de anlatır.","neighbor_ref":"root_001330/B005","relation_type":"near_neighbor","shared_zone":"İki dal da yerleşimlerin toplandığı büyük bir merkez için kullanılabilir."},{"boundary_match":"field_only","distinction":"Odak dal fiziksel yerleşimdir ve yönetim yalnızca adlandırma açıklamasında görünür; komşu dal ise topluluk üzerinde görev ve yetki taşıyan kişiyi anlatır.","focus_only":"Odak dal yönetimin gerçekleştiği fiziksel yerleşimi adlandırır.","gloss":"yönetilen yer ile yöneten görevli","neighbor_only":"Komşu dal bir topluluğun işini yürüten yönetici, görevli veya başkan rolünü adlandırır.","neighbor_ref":"root_000709/B003","relation_type":"same_field","shared_zone":"Her iki dal kent veya topluluk yönetimi sahnesinde yer alabilir."}],"source_phrase_ar":"المدينة كأنها مفعلة سميت بذلك لأنها تقام فيها طاعة ذوي الأمر (maqayis)؛ ومنه سمى المصر مدينة (sihah)؛ جعل بعضهم المدينة من هذا الباب (mufradat)","source_summary":"Kanıt yerleşim anlamını kent olarak verir ve bu adın yöneticilerin buyruklarına uyulan yer düşüncesiyle açıklandığını bildirir; kökensel açıklama yerleşim tanımından ayrı tutulmalıdır.","sources":["MQ","SI","MU"],"what_is_ar":"المدينة بمعنى المصر والموضع الذي تقام فيه طاعة ذوي الأمر","what_is_not_ar":"ليست المدينة الأمة المملوكة ولا العبد المدين في هذا الفرع"},"support_links":["sup_247e039079f06dc5170b"]},{"boundary":"Anlam yalnızca verilen kişi, yargı ve yemin yapılarında geçerlidir; genel inanma, yönetim yetkisi devretme, borçlandırma veya hüküm verme anlamına genişletilmez.","branch_kind":"non_bare","branch_ref":"root_000504/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:3:2","qac_word_ref":"1:4:3","surface_ar":"دِّينِ"}],"gloss":"kişiyi sözüne ve vicdani sorumluluğuna göre değerlendirme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiyi kendi vicdani yükümlülüğüyle baş başa bırakmak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yargıda veya kişiyle Tanrı arasındaki konuda onun sözünü doğru kabul etmek."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yemin edenin sözünü ve yükümlülüğünü kendi niyetine göre değerlendirmek."}}],"root_ar":"د ي ن","root_id":"root_000504","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin sözünü doğru sayma, sorumluluğu ona bırakma ve yeminini kendi niyetine göre yorumlama yönlerini birlikte anlatır.","boundary_detail":"Anlam yalnızca verilen kişi, yargı ve yemin yapılarında geçerlidir; genel inanma, yönetim yetkisi devretme, borçlandırma veya hüküm verme anlamına genişletilmez.","branch_image_ar":"التصديق والتفويض","concept_gloss":"kişiyi sözüne ve vicdani sorumluluğuna göre değerlendirme","contextual_glosses":[{"applicability":"Bir kişinin yükümlülüğünün kendisiyle Tanrı arasındaki bağına bırakıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yargıda sözünü doğru kabul etme ve yemini niyetine göre değerlendirme yönlerini dışarıda bırakır.","preserves":"Sorumluluğu kişinin kendisine bırakma yönünü korur."},"facet_ids":["F001"],"text":"vicdani sorumluluğuyla baş başa bırakma","usage_role":"contextual"},{"applicability":"Bir kişinin yargıda veya vicdani konuda doğru söylediğinin kabul edildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sorumluluğu kişiye bırakma ile yemin niyetini ölçü alma yönlerini dışarıda bırakır.","preserves":"Kişinin sözüne güvenme ve onu doğru sayma yönünü korur."},"facet_ids":["F002"],"text":"sözünü doğru kabul etme","usage_role":"contextual"},{"applicability":"Yemin sözünün kapsamı belirlenirken söyleyen kişinin niyetinin esas alındığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel vicdani sorumluluk ve yargıda söze güvenme kullanımlarını dışarıda bırakır.","preserves":"Yeminin söyleyen kişinin niyetine bağlanması yönünü korur."},"facet_ids":["F003"],"text":"yemini söyleyenin niyetine göre yorumlama","usage_role":"contextual"}],"definition":"Bir kişiyi kendi vicdani yükümlülüğü ve sözüyle baş başa bırakmak veya yargıda sözünü doğru kabul etmek; yemin edenin sözünü de onun kendi niyetine göre değerlendirmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiyi kendi vicdani yükümlülüğüyle baş başa bırakmak."},{"facet_id":"F002","role":"specialization","statement":"Yargıda veya kişiyle Tanrı arasındaki konuda onun sözünü doğru kabul etmek."},{"facet_id":"F003","role":"specialization","statement":"Yemin edenin sözünü ve yükümlülüğünü kendi niyetine göre değerlendirmek."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Karar veya yönetim yetkisinin resmen başka kişiye verildiği anlamını ekler.","collision":"Genel görevlendirme ve temsil ilişkisiyle karışır.","fit":"displacement","loses":"Kişinin sözüne güvenme ve vicdani yükümlülüğünü ölçü alma yönlerini kaybeder.","preserves":"Bir işi veya sorumluluğu başka kişiye bırakma yönünü kısmen korur."},"text":"yetki devri"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Vicdani sorumluluğu kişiye bırakma ve yemini niyetine göre değerlendirme kapsamını kaybeder.","preserves":"Bir kişinin sözünü doğru kabul etme yönünü korur."},"text":"doğrulama"},{"category":"confusable","error_profile":{"adds":"Kanıtta bulunmayan, kişiye yeni bir yemin söyletme eylemini ekler.","collision":"Yeminin yorumlanmasını yemin isteme eylemiyle karıştırır.","fit":"displacement","loses":"Söylenmiş yemini söyleyenin niyetine göre değerlendirme işlemini kaybeder.","preserves":"Yemin sahnesiyle olan bağlantıyı korur."},"text":"yemin ettirme"}],"identity_rationale":"Kaynak ifadesi genel bir yetki devrinden çok, kişiyi kendi vicdani yükümlülüğüyle baş başa bırakmayı, yargıda veya kişiyle Tanrı arasındaki konuda sözünü doğru kabul etmeyi ve yemini söyleyenin niyetine göre değerlendirmeyi anlatır. Dal korunabilir, ancak genel görevlendirme anlamından bu güven ve sorumluluk ilişkisine çekilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"onu vicdani yükümlülüğüyle baş başa bıraktı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yargıda veya Tanrı'yla arasındaki konuda sözünü doğru kabul etti"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yeminini kendi niyetine göre değerlendirdi"}],"lexicalization_note":"Dal yalnızca kanıtta verilen kişi, yargı ve yemin yapılarıyla sözlükselleşmiştir; bunlardan bağımsız bir yalın kök anlamı varsayılmaz.","neighbor_coverage_note":"Sunulan bütün adaylar değerlendirildi; genel doğrulama, işi başkasına bırakma ve karar yetkisi verme ile oluşan üç sınır seçildi. Yemin sunma, yemini bozma, suç yükleme ve benzer görevlendirme adayları bu sınırları yinelediği için eklenmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yargı, vicdani yükümlülük ve yemin yapılarıyla sınırlıdır; komşu dal ise bu yapılara bağlı olmadan genel doğrulama ve inanmayı anlatır.","focus_only":"Odak dal sorumluluğu kişiye bırakmayı ve yemin niyetini ölçü almayı da içerir.","gloss":"sınırlı bağlamda söze güvenme ile genel inanma","neighbor_only":"Komşu dal haber veya sözü doğru saymaktan dinsel inanca kadar uzanan genel inanmayı kapsar.","neighbor_ref":"root_000054/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir kişinin sözünü doğru ve güvenilir kabul etme alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dalda kişi kendi iç yükümlülüğü ve beyanıyla baş başa bırakılır; komşu dalda ise işi yapma veya kararı yürütme yetkisi başka birine aktarılır.","focus_only":"Odak dal kişiyi kendi sözüne ve vicdani sorumluluğuna bırakır.","gloss":"vicdana bırakma ile işi başkasına bırakma","neighbor_only":"Komşu dal bir işi veya kararı başka bir kişiye verip onun yürütmesine dayanmayı anlatır.","neighbor_ref":"root_001187/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da bir konunun başka bir kişinin sorumluluğuna bırakılması vardır."},{"boundary_match":"partial","distinction":"Odak dal güveni kişinin beyanı ve vicdani sorumluluğuyla sınırlar; komşu dal kişiyi karar veren makam durumuna getirir.","focus_only":"Odak dal yargıda kişinin sözünü doğru sayar, ancak ona hüküm verme yetkisi tanımaz.","gloss":"söze güvenme ile karar yetkisi verme","neighbor_only":"Komşu dal uyuşmazlıkta karar verme yetkisini seçilen kişiye bırakır ve onun hükmünü geçerli kılar.","neighbor_ref":"root_000348/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal bir yargı veya uyuşmazlık bağlamında başka bir kişiye güvenmeyi içerir."}],"source_phrase_ar":"دينت الرجل تديينا إذا وكلته إلى دينه (sihah)؛ دينت الرجل في القضاء وفيما بينه وبين الله أي صدقته (tahdhib)؛ دينت الحالف أي نويته فيما حلف وهو التديين (tahdhib)","source_summary":"Kanıt, kişiyi kendi vicdani sorumluluğuna bırakma ile belirli yargı ve yemin bağlamlarında onun sözüne güvenmeyi birleştirir; yemin kullanımında belirleyici olan söyleyenin niyetidir.","sources":["SI","TA"],"what_is_ar":"التديين بمعنى تصديق الرجل في القضاء أو الحلف أو تفويضه إلى دينه","what_is_not_ar":"ليس الطاعة العامة ولا الدين المالي ولا الحكم والجزاء"},"support_links":[]},{"boundary":"Bu alan, mala sahip olmayı veya kamusal egemenliği değil, sağlamlık ve iç tutarlılık kazanmayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001444/B001","candidate_links":[{"candidate_id":"cand_85368a4b3f75ed141a49","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَٰلِك","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ma`lik|ROOT:mlk|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:1:1","qac_word_ref":"1:4:1","surface_ar":"مَٰلِكِ"}],"gloss":"güçlü ve tutarlı biçimde bir arada durma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey, parçaları çözülmeden bir arada duracak güç ve iç tutarlılık taşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hamur sıkı ve bütünlüklü bir kıvama gelinceye kadar kuvvetle yoğrulur."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir bitki sürgünü kurutularak sert ve dayanıklı hâle getirilir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir yapı veya kişi, çökmesini ya da denetimsiz davranmasını önleyen iç tutarlılığı korur."}}],"root_ar":"م ل ك","root_id":"root_001444","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin sağlamlaşmasıyla kişinin kendini tutmasını birlikte kapsayan en genel Türkçe karşılıktır.","boundary_detail":"Bu alan, mala sahip olmayı veya kamusal egemenliği değil, sağlamlık ve iç tutarlılık kazanmayı anlatır.","branch_image_ar":"قوة الشيء وتماسكه","concept_gloss":"güçlü ve tutarlı biçimde bir arada durma","contextual_glosses":[{"applicability":"Hamurun sıkı, dayanıklı ve bütünlüklü hâle getirildiği kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yapısal sağlamlık ve kişinin kendini tutması kapsamlarını dışarıda bırakır.","preserves":"Sıkılaştırma ve bütünlüklü kıvam oluşturma işlemini korur."},"facet_ids":["F002"],"text":"sıkıca yoğurup kıvamlandırmak","usage_role":"contextual"},{"applicability":"Kişinin düşmeye veya söz söylemeye karşı özdenetimini koruduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Maddi nesnelerin sıkılaşması ve sertleşmesi kapsamlarını dışarıda bırakır.","preserves":"Kişideki iç tutarlılık ve özdenetim sonucunu korur."},"facet_ids":["F004"],"text":"kendini tutmak","usage_role":"contextual"}],"definition":"Bir şeyin parçalarının sıkıca bağlanarak güçlü, dayanıklı ve dağılmaya dirençli hâle gelmesi veya getirilmesidir. Kişide bu iç tutarlılık, düşmekten ya da düşünmeden konuşmaktan kendini alıkoyma biçiminde görünür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey, parçaları çözülmeden bir arada duracak güç ve iç tutarlılık taşır."},{"facet_id":"F002","role":"specialization","statement":"Hamur sıkı ve bütünlüklü bir kıvama gelinceye kadar kuvvetle yoğrulur."},{"facet_id":"F003","role":"specialization","statement":"Bir bitki sürgünü kurutularak sert ve dayanıklı hâle getirilir."},{"facet_id":"F004","role":"extension","statement":"Bir yapı veya kişi, çökmesini ya da denetimsiz davranmasını önleyen iç tutarlılığı korur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Mal veya hak üzerinde sahiplik ilişkisi ekler.","collision":"Aynı kökün özel sahiplik dalıyla karışır.","fit":"displacement","loses":"Sıkılık, dayanıklılık ve iç tutarlılık çekirdeğini bütünüyle kaybeder.","preserves":"Bir şey üzerinde denetim çağrışımını uzaktan korur."},"text":"mülkiyet"}],"identity_rationale":"Kaynak ifadesi, nesnenin iç sağlamlığını ve dağılmadan bir arada durmasını ortak çekirdek olarak verir; hamurun sıkıca yoğrulması, bir sürgünün sertleştirilmesi, duvarın ayakta kalması ve kişinin kendini tutması bu çekirdeğin farklı gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"hamuru sıkıca yoğurup kıvamlandırmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sürgünü kabuğuyla kurutup sertleştirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kendini tutmak; dayanmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyi ayakta tutan iç sağlamlık"}],"lexicalization_note":"Tanım, genel sağlamlık çekirdeğini korurken hamur, sürgün, duvar ve özdenetim kullanımlarını kendi kalıplarına bağlı ayrı gerçekleşmeler olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sağlamlık, yoğun güç ve dayanakla doğrudan sınır oluşturan üç aday yayımlandı, yalnız ortak kök, uzak tema veya ilgisiz nesne paylaşan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı, nesnenin ya da kişinin kendi içinde dağılmadan durmasına yönelir; komşu dal ise yapılan işin sağlam ve güvenilir biçimde pekiştirilmesine daha belirgin vurgu yapar.","focus_only":"İç tutarlılık, hamurun kıvamı ve kişinin kendini tutması da kapsama girer.","gloss":"sağlam ve tutarlı olma","neighbor_only":"Bir işi veya nesneyi güvenilir biçimde sağlamlaştırma ve sıkıca güvenceye alma öne çıkar.","neighbor_ref":"root_001623/B002","relation_type":"near_synonym","shared_zone":"Her iki alan da gevşekliğin giderilmesini, güçlenmeyi ve sağlam bir bütün oluşmasını anlatır."},{"boundary_match":"partial","distinction":"Komşu dal genel ve yoğun kuvveti geniş bir alanda anlatırken odak dalı, kuvvetin nesneyi veya kişiyi çözülmeden tutan iç bütünlük olarak işlemesini gerektirir.","focus_only":"Parçaların bir arada durması ve özdenetim biçimindeki tutarlılık belirleyicidir.","gloss":"iç tutarlılık ile sert güç","neighbor_only":"Cesaret, güçlü yürek, ağır koşul ve şiddetli eylem gibi yoğun güç alanları da bulunur.","neighbor_ref":"root_000782/B002","relation_type":"near_synonym","shared_zone":"İki dal da güç, sertlik ve dayanıklılık niteliklerinde kesişir."},{"boundary_match":"partial","distinction":"Odak dalı ayakta kalmanın niteliği olan iç tutarlılığı belirtir; komşu dal ise ayakta kalmayı sağlayan temel unsur veya dayanağı adlandırır.","focus_only":"Bir şeyin kendi parçaları arasındaki sıkılık ve dayanıklılık anlatılır.","gloss":"iç sağlamlık ve dayanak","neighbor_only":"Bir işin veya bedenin dayandığı temel unsur anlatılır.","neighbor_ref":"root_001444/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir şeyin ayakta kalmasını ve bozulmamasını sağlayan koşulla ilgilidir."}],"source_phrase_ar":"أصل صحيح يدل على قوة في الشيء وصحة (maqayis)؛ أملك عجينه قوي عجنه وشده (maqayis)؛ ملكت العجين إذا شددت عجنه (sihah)؛ ملك النبعة صلبها (sihah)؛ العجين إذا كان متماسكا متينا مملوك ومملك (tahdhib)؛ حائط ليس له ملاك أي تماسك (mufradat)","source_summary":"Kaynakların ortak çizgisi, gücün yalnız dış kuvvet değil, nesneyi veya kişiyi çözülmeden ayakta tutan sıkılık ve tutarlılık olmasıdır; verilen örnekler bu niteliğin maddi ve davranışsal görünümlerini gösterir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"شد العجين وإحكام عجنه؛ تقوية الشيء؛ صلابة النبعة؛ التماسك الذي يقوم به الجدار أو النفس","what_is_not_ar":"ليس المِلْك للمال ولا المُلك للسلطان"},"support_links":["sup_247e039079f06dc5170b"]},{"boundary":"Bu dal özel sahiplik ve tasarruf yetkisidir; halk üzerinde kamusal yönetim ve saltanat ayrı bir daldır.","branch_kind":"mixed_non_bare","branch_ref":"root_001444/B002","candidate_links":[{"candidate_id":"cand_ceeeb8799a41d7f31756","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَٰلِك","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ma`lik|ROOT:mlk|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:1:1","qac_word_ref":"1:4:1","surface_ar":"مَٰلِكِ"}],"gloss":"sahiplik ve tasarruf yetkisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi, mal veya hak üzerinde sahiplikten doğan elinde bulundurma ve tasarruf yetkisine sahiptir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sahiplik bir başkasına geçirilebilir veya belirli bir konuda karar yetkisi o kişiye bırakılabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tarihsel kullanımda sahip olunan kişi, köleleştirilmiş insanı ve ona ilişkin sahiplik durumunu belirtir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Belirli bir kalıp, sahibin köleleştirilmiş kişilere iyi davranmasını ifade eder."}}],"root_ar":"م ل ك","root_id":"root_001444","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Mal, hak ve kişi üzerinde kurulan özel sahiplik ilişkisini ve bundan doğan işlem yetkisini kapsar.","boundary_detail":"Bu dal özel sahiplik ve tasarruf yetkisidir; halk üzerinde kamusal yönetim ve saltanat ayrı bir daldır.","branch_image_ar":"المِلْك والتصرف","concept_gloss":"sahiplik ve tasarruf yetkisi","contextual_glosses":[{"applicability":"Bir mal veya hakkın kişiye ait olduğu ve onun tasarrufunda bulunduğu genel bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yetki devri ile tarihsel kölelik ve özel davranış kullanımlarını açıkça göstermez.","preserves":"Aidiyet ve kişisel denetim çekirdeğini korur."},"facet_ids":["F001"],"text":"sahip olmak","usage_role":"general"},{"applicability":"Bir malın veya belirli karar yetkisinin başka bir kişiye verildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sahipliğin durağan aidiyet ve tarihsel kişi sahipliği kapsamlarını dışarıda bırakır.","preserves":"Yetkinin bir başkasına geçirilmesini korur."},"facet_ids":["F002"],"text":"tasarrufuna bırakmak","usage_role":"contextual"}],"definition":"Bir şeyin bir kişinin elinde veya hukuki alanında bulunması ve o kişinin onun üzerinde tasarruf yetkisi taşımasıdır. Bu yetki devredilebilir; tarihsel kullanımlarda köleleştirilmiş kişileri ve onlara ilişkin davranışı, belirli bir kalıpta ise boşanma kararının eşe bırakılmasını da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi, mal veya hak üzerinde sahiplikten doğan elinde bulundurma ve tasarruf yetkisine sahiptir."},{"facet_id":"F002","role":"extension","statement":"Sahiplik bir başkasına geçirilebilir veya belirli bir konuda karar yetkisi o kişiye bırakılabilir."},{"facet_id":"F003","role":"specialization","statement":"Tarihsel kullanımda sahip olunan kişi, köleleştirilmiş insanı ve ona ilişkin sahiplik durumunu belirtir."},{"facet_id":"F004","role":"associated_use","statement":"Belirli bir kalıp, sahibin köleleştirilmiş kişilere iyi davranmasını ifade eder."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Halk veya ülke üzerinde kamusal hüküm sürme anlamı ekler.","collision":"Aynı kökün yönetim ve saltanat dalıyla karışır.","fit":"displacement","loses":"Özel aidiyet ve sahip olunan şey üzerindeki tasarruf ilişkisini kaybeder.","preserves":"Yetki ve denetim unsurunu korur."},"text":"egemenlik"}],"identity_rationale":"Kaynak ifadesi, bir şeyi elinde bulundurma ve üzerinde hükme bağlı tasarruf yetkisi taşıma çekirdeğini açıkça kurar; malın başkasına geçirilmesi, köleleştirilmiş kişi, bu kişilere davranış ve boşanma kararının eşe bırakılması bu çekirdeğe bağlı özel kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir şeye sahip olup onu tasarrufunda bulundurmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"mülkiyet; sahip olunan mal veya hak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kişinin elinin altında ve sahipliğinde bulunan şey"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"köleleştirilmiş kişi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"köleleştirilmiş kişilere iyi davranma"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"özgür doğmuşken tutsak edilip köleleştirilen kişi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"boşanma kararını eşin tasarrufuna bırakmak"}],"lexicalization_note":"Genel sahiplik çekirdeği ile el altında bulundurma, kölelik, iyi muamele ve boşanma yetkisini devretme gibi kalıba bağlı kullanımlar birbirine karıştırılmadan tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel sahipliğe en yakın el altında bulundurma ve edinme alanlarıyla kamusal egemenlik karışıklığı yayımlandı, hak, engelleme, görevlendirme ve çalışma temaları daha uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal el ve hâkimiyet imgesiyle fiilî denetime odaklanır; odak dalı hukuki aidiyeti ve bu aidiyetten doğan çeşitli tasarruf biçimlerini daha geniş işler.","focus_only":"Sahipliği devretme, köleleştirilmiş kişi ve özel karar yetkisi gibi türemiş kullanımlar da yer alır.","gloss":"sahiplik ve el altında bulundurma","neighbor_only":"El altında veya kişinin fiilî denetiminde bulunma imgesi daha belirgindir.","neighbor_ref":"root_001693/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin kişiye ait olmasını ve onun tasarruf alanında bulunmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalı sahiplik ilişkisini ve yetkisini tanımlar; komşu dal ise malın toplanması, elde edilmesi veya teslim alınması sürecini öne çıkarır.","focus_only":"Mevcut aidiyet ve sürekli tasarruf yetkisi belirleyicidir.","gloss":"sahiplik ve edinme","neighbor_only":"Malı toplama, elde etme ve teslim alana geçirme eylemleri belirleyicidir.","neighbor_ref":"root_001197/B003","relation_type":"near_neighbor","shared_zone":"Her iki alan da malın bir kişinin denetimine girmesiyle ilgilidir."},{"boundary_match":"field_only","distinction":"Odak dalı sahibi ile sahip olunan şey arasındaki özel ilişkiyi kurar; komşu dal hükümdarın halk ve ülke üzerindeki kamusal yönetim gücünü kurar.","focus_only":"Belirli mal, hak veya kişi üzerinde özel aidiyet ve tasarruf vardır.","gloss":"özel sahiplik ve kamusal egemenlik","neighbor_only":"Bir topluluk üzerinde emir, yasak, siyaset ve kamusal hüküm vardır.","neighbor_ref":"root_001444/B003","relation_type":"same_field","shared_zone":"Her iki dal da yetki, denetim ve hüküm kullanma alanına girer."}],"source_phrase_ar":"ملك الإنسان الشيء يملكه ملكا (maqayis)؛ الملك ما ملكت اليد من مال وخول (ayn;tahdhib)؛ ملكت الشيء أملكه ملكا (sihah)؛ وملكه المال والملك فهو مملك (sihah)؛ أملكت فلانة أمرها إذا جعل أمر طلاقها بيدها (tahdhib)؛ المملوك يختص في التعارف بالرقيق من الأملاك (mufradat)","source_summary":"Kaynaklar, sahipliği bir şeyin elde veya hukuki denetimde bulunması ve üzerinde hükme bağlı tasarruf kurulması olarak birleştirir; devir, kölelik ve özel karar yetkisi bu ilişkinin tarihsel ya da kalıplaşmış uzantılarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"ملك الشيء والمال وما ملكت اليد؛ جعل الشيء ملكا لغيره؛ المملوك والعبد وملك اليمين؛ حسن الملكة إلى المماليك؛ تفويض الأمر لصاحبه","what_is_not_ar":"ليس مُلك السلطان العام ولا الإملاك للتزويج"},"support_links":["sup_9076b32659455b9ab4a1"]},{"boundary":"Bu dal, belirli bir malın kişisel sahipliğinden ve ilahi haberci varlığın adından ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001444/B003","candidate_links":[{"candidate_id":"cand_b6d98f0c83a6743ebe20","lane":"micro"},{"candidate_id":"cand_b6d347cb5abb89b72475","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَٰلِك","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ma`lik|ROOT:mlk|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:1:1","qac_word_ref":"1:4:1","surface_ar":"مَٰلِكِ"}],"gloss":"hükümdarlık ve kamusal egemenlik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hükümdar, halk üzerinde emir ve yasak koyarak kamusal yönetim yetkisi kullanır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hükümranlık, yöneticinin halkı ve ülkesindeki etkili yönetim alanını kapsar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İlahi bağlamda bütün varlık üzerindeki mutlak ve kalıcı egemenlik anlatılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir topluluk bir kişiyi başına geçirerek onu hükümdar konumuna getirir."}}],"root_ar":"م ل ك","root_id":"root_001444","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yönetici kişiyi, halk üzerindeki hüküm gücünü ve bu gücün ülkesini birlikte temsil eder.","boundary_detail":"Bu dal, belirli bir malın kişisel sahipliğinden ve ilahi haberci varlığın adından ayrıdır.","branch_image_ar":"المُلك والسلطان","concept_gloss":"hükümdarlık ve kamusal egemenlik","contextual_glosses":[{"applicability":"Halk üzerinde yönetim ve siyaset yetkisi kullanan kişi kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Soyut hükümranlığı, ülkeyi ve ilahi mutlak egemenliği dışarıda bırakır.","preserves":"Kamusal yönetim yetkisini taşıyan katılımcıyı korur."},"facet_ids":["F001"],"text":"hükümdar","usage_role":"contextual"},{"applicability":"Halk ve ülke üzerindeki yönetim gücü soyut olarak anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hükümdar kişisini ve birini hükümdar yapma eylemini açıkça göstermez.","preserves":"Kamusal egemenlik ve yönetim gücünü korur."},"facet_ids":["F002","F003"],"text":"hükümranlık","usage_role":"general"}],"definition":"Bir hükümdarın halk üzerinde emir, yasak ve yönetim yetkisi kullanmasıyla kurulan kamusal hükümranlıktır. Bu alan hükümdarı, yönetim gücünü, hükmedilen ülkeyi ve ilahi bağlamda mutlak egemenliği kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hükümdar, halk üzerinde emir ve yasak koyarak kamusal yönetim yetkisi kullanır."},{"facet_id":"F002","role":"extension","statement":"Hükümranlık, yöneticinin halkı ve ülkesindeki etkili yönetim alanını kapsar."},{"facet_id":"F003","role":"specialization","statement":"İlahi bağlamda bütün varlık üzerindeki mutlak ve kalıcı egemenlik anlatılır."},{"facet_id":"F004","role":"associated_use","statement":"Bir topluluk bir kişiyi başına geçirerek onu hükümdar konumuna getirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Belirli bir mal veya hak üzerinde özel aidiyet ekler.","collision":"Aynı kökün özel sahiplik dalıyla karışır.","fit":"displacement","loses":"Halk üzerinde emir, yasak ve siyaset yoluyla kurulan kamusal yönetimi kaybeder.","preserves":"Denetim ve yetki unsurunu sınırlı biçimde korur."},"text":"mülkiyet"}],"identity_rationale":"Kaynak ifadesi, hükümdarı halk üzerinde emir ve yasak koyan yönetici olarak tanımlar; hükümranlık, ülke, halk üzerindeki siyaset ve özellikle ilahi mutlak egemenlik bu kamusal yönetim çekirdeğinde birleşir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"hükümdar"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"hükümdar; egemen yönetici"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"hükümranlık; kamusal egemenlik"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ilahi mutlak hükümranlık"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"hükümdarın yönetim alanı ve ülkesi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"birini başlarına hükümdar yapmak"}],"lexicalization_note":"Hükümdar ve hükümranlık çekirdeği korunur; ülke, mutlak ilahi egemenlik ve birini hükümdar yapma kullanımları kendi biçim ve kalıplarına bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yetki, yöneticilik ve özel sahiplikle en açıklayıcı üç sınır yayımlandı, üstünlük, azletme ve unvanla ilgili daha uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı hükümdarın halk üzerindeki genel kamusal yönetimini kurar; komşu dal yönetici kişiden bağımsız olarak belirli bir hak veya eylem alanında verilen yetkiyi de kapsar.","focus_only":"Hükümdar kişisi, ülkesi ve ilahi mutlak egemenlik de kapsama girer.","gloss":"hükümranlık ve yetkili güç","neighbor_only":"Belirli bir hak veya eylem için bir kişiye verilmiş yetki de kapsama girer.","neighbor_ref":"root_000732/B003","relation_type":"near_synonym","shared_zone":"İki dal da başkaları üzerinde geçerli yönetim ve yetki kullanmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dalı en üst kamusal hükümranlığa ve ülke ölçeğine yönelir; komşu dal ise atanabilen yöneticilik veya valilik makamını daha geniş biçimde kapsar.","focus_only":"Hükümdarlık, ülke ve mutlak egemenlik ölçeği bulunur.","gloss":"hükümdarlık ve yöneticilik","neighbor_only":"Bir kişiyi yönetici olarak görevlendirme ve belirli yöneticilik makamı öne çıkar.","neighbor_ref":"root_000051/B003","relation_type":"near_synonym","shared_zone":"Her iki alan da bir topluluğu yönetme yetkisini ve bu yetkiyi taşıyan kişiyi kapsar."},{"boundary_match":"field_only","distinction":"Odak dalının nesnesi topluluk ve ülke, yetkisi ise kamusaldır; komşu dalın nesnesi belirli mal veya hak, yetkisi ise sahibin özel tasarrufudur.","focus_only":"Halk ve ülke üzerinde kamusal yönetim ve siyaset vardır.","gloss":"kamusal egemenlik ve özel sahiplik","neighbor_only":"Belirli mal veya hak üzerinde kişisel aidiyet ve tasarruf vardır.","neighbor_ref":"root_001444/B002","relation_type":"same_field","shared_zone":"Her iki dal da denetim, yetki ve hüküm kullanma düşüncesini paylaşır."}],"source_phrase_ar":"والاسم الملك لأن يده فيه قوية صحيحة (maqayis)؛ الملك لله المالك المليك (ayn)؛ الملكوت ملك الله وملكوت الله سلطانه (ayn)؛ الملكوت من الملك (sihah)؛ المملكة سلطان الملك في رعيته (ayn;tahdhib)؛ له ملكوت العراق وعزه وسلطانه وملكه (tahdhib)؛ الملك هو المتصرف بالأمر والنهي في الجمهور (mufradat)؛ ملك القوم فلانا وأملكوه على أنفسهم أي صيروه ملكا (tahdhib)","source_summary":"Kaynaklar, bu alanı halk üzerinde emir ve yasakla işleyen yönetim gücü etrafında toplar; hükümdar, hükümranlık, ülke ve ilahi mutlak egemenlik aynı kamusal yetki ekseninin farklı görünümleridir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"المَلِك والملوك؛ المُلك والسلطان والعز؛ ملك الناس وسياسة الرعية؛ المملكة؛ الملكوت وخاصة ملك الله","what_is_not_ar":"ليس مجرد مِلْك اليد للمال؛ ولا مَلَك الملائكة"},"support_links":["sup_5e5a60a15581f02f2ebd","sup_ec98c3825f872a39c0a9"]},{"boundary":"Bu kullanım mal sahipliği veya insanı köleleştirme değil, yalnız evlilik akdi ve evlenme bağlamıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001444/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَٰلِك","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ma`lik|ROOT:mlk|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:1:1","qac_word_ref":"1:4:1","surface_ar":"مَٰلِكِ"}],"gloss":"evlilik akdi kurma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Evlilik bağı, tarafları birbirine bağlayan bir akitle kurulur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi iki tarafın evlilik akdini kurarak onları evlendirir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Evlilik akdinin yapıldığı tören veya ona tanıklık etme olayı adlandırılır."}}],"root_ar":"م ل ك","root_id":"root_001444","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Evlendirme, evlenme ve akdin gerçekleşmesi kullanımlarını ortak sözleşmesel çekirdekte toplar.","boundary_detail":"Bu kullanım mal sahipliği veya insanı köleleştirme değil, yalnız evlilik akdi ve evlenme bağlamıdır.","branch_image_ar":"الإملاك والتزويج","concept_gloss":"evlilik akdi kurma","contextual_glosses":[{"applicability":"Bir kişinin iki taraf arasında evlilik akdini kurduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tarafın kendi evlenme eylemini ve akit törenini dışarıda bırakır.","preserves":"Akdi kuran dış katılımcının evlendirme eylemini korur."},"facet_ids":["F002"],"text":"evlendirmek","usage_role":"contextual"},{"applicability":"Taraflardan birinin evlilik bağına girdiği kalıplaşmış kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Evlendiren kişinin eylemini ve akde tanıklık olayını dışarıda bırakır.","preserves":"Evlilik bağının taraf açısından kurulmasını korur."},"facet_ids":["F001"],"text":"evlenmek","usage_role":"contextual"}],"definition":"İki kişi arasında evlilik bağını sözleşmeyle kurmak veya bu akdin gerçekleşmesidir. Kullanım, birini evlendirmeyi, evlilik akdine tanıklığı ve bir erkeğin bir kadınla evlenmesini kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Evlilik bağı, tarafları birbirine bağlayan bir akitle kurulur."},{"facet_id":"F002","role":"extension","statement":"Bir kişi iki tarafın evlilik akdini kurarak onları evlendirir."},{"facet_id":"F003","role":"associated_use","statement":"Evlilik akdinin yapıldığı tören veya ona tanıklık etme olayı adlandırılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Tek yanlı sahiplik ve nesneleştirme anlamı ekler.","collision":"Özel sahiplik dalıyla yanıltıcı biçimde karışır.","fit":"displacement","loses":"Karşılıklı evlilik akdini ve evlendirme olayını kaybeder.","preserves":"Bir ilişki kurma düşüncesini çok dolaylı biçimde korur."},"text":"sahiplenmek"}],"identity_rationale":"Kaynak ifadesi bütün örnekleri evlilik akdinin kurulması çevresinde toplar: birinin evlendirilmesi, bu akde tanıklık edilmesi ve erkeğin kadınla evlenmesi aynı sözleşmesel olayın farklı katılımcı görünümleridir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"evlilik akdi; evlendirme"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kadınla evlenmek"}],"lexicalization_note":"Tanım evlilik akdiyle sınırlıdır; ad biçimindeki akit ve kadınla evlenmeyi bildiren kalıp ayrı yüzler olarak korunur, çıplak sahiplik anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşdeğer evlilik akdi, bedelin belirtilmediği özel akit ve cinsel birliktelik alanıyla sınırlar yayımlandı, akrabalık ve bekleme süresi gibi yalnız tematik adaylar elendi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen sınırlar bakımından iki dal aynı sözleşmesel evlilik olayını ifade eder ve olağan bağlamlarda birbirinin yerine kullanılabilir.","focus_only":null,"gloss":"evlilik akdi","neighbor_only":null,"neighbor_ref":"root_001548/B002","relation_type":"synonym","shared_zone":"Her iki dal da evlilik bağının akitle kurulmasını, evlenmeyi ve evlendirmeyi kapsar."},{"boundary_match":"partial","distinction":"Odak dalı yalnız akdin kurulmasına ve evlenmeye yönelir; komşu dal evlilik akdinden cinsel birleşme ve bedenle ilgili örtmeceli anlamlara uzanır.","focus_only":"Evlilik bağını kuran akit ve evlendirme işlemi merkezde yer alır.","gloss":"evlilik akdi ve cinsel birliktelik alanı","neighbor_only":"Cinsel birleşme ve beden bölgesi için örtmeceli kullanımlar da bulunur.","neighbor_ref":"root_000123/B003","relation_type":"near_neighbor","shared_zone":"İki dal evlilik ilişkisi ve bu ilişkiyi kuran akit bağlamında kesişir."},{"boundary_match":"partial","distinction":"Komşu dal yalnız evlilik bedelinin adlandırılmadığı özel akit türünü belirtir; odak dalında böyle bir kurucu sınırlama yoktur.","focus_only":"Evlilik akdinin genel biçimidir ve bedel şartına bağlı değildir.","gloss":"genel ve bedelsiz belirtilen evlilik akdi","neighbor_only":"Akdin kuruluşunda evlilik bedelinin belirtilmemesi özel koşuldur.","neighbor_ref":"root_001187/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da taraflar arasında evlilik akdi kurulmasını anlatır."}],"source_phrase_ar":"كنا في إملاك فلان أي أملكناه امرأته (maqayis)؛ الإملاك التزويج قد أملكوه وملكوه أي زوجوه (ayn)؛ ملكت المرأة تزوجتها (sihah)؛ أملكنا فلانا فلانة إذا زوجناه إياها (sihah)؛ شهدنا إملاك فلان وملاكه وملاكه (tahdhib)؛ الملاك التزويج وأملكوه زوجوه (mufradat)","source_summary":"Kaynaklar, bu dalı evlilik akdinin kurulması olarak ortaklaştırır; evlendiren kişi, evlenen kişi ve akde tanıklık edenler aynı sözleşmesel olayın farklı katılımcılarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"عقد التزويج والإملاك؛ شهدنا إملاك فلان؛ ملك الرجل المرأة بمعنى تزوجها","what_is_not_ar":"ليس ملك المال ولا استرقاق المملوك"},"support_links":[]},{"boundary":"Bu dal dayanak olan unsuru belirtir; nesnenin kendi iç sıkılığı veya sahiplik ilişkisi değildir.","branch_kind":"collocation","branch_ref":"root_001444/B005","candidate_links":[{"candidate_id":"cand_85368a4b3f75ed141a49","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَٰلِك","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ma`lik|ROOT:mlk|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:1:1","qac_word_ref":"1:4:1","surface_ar":"مَٰلِكِ"}],"gloss":"işi ayakta tutan temel dayanak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir unsur, daha büyük bir işin veya düzenin dayandığı ve onun düzgün işlemesini sağlayan temeldir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu dayanak, işin doğruluğunu, sürekliliğini ve tamamlanmasını sağlayan belirleyici koşul olur."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kalp, bedenin işleyişinin kendisine dayandığı temel unsur olarak gösterilir."}}],"root_ar":"م ل ك","root_id":"root_001444","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir düzenin varlığını ve düzgün işlemesini kendisine borçlu olduğu unsur için kullanılır.","boundary_detail":"Bu dal dayanak olan unsuru belirtir; nesnenin kendi iç sıkılığı veya sahiplik ilişkisi değildir.","branch_image_ar":"مِلاك الأمر وعِماده","concept_gloss":"işi ayakta tutan temel dayanak","contextual_glosses":[{"applicability":"Bir işin veya düzenin kendisine bağlı olduğu belirleyici unsur anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşin doğruluğu ve tamamlanması sonucunu açıkça belirtmez.","preserves":"Bağımlılık ve ayakta tutma işlevini korur."},"facet_ids":["F001"],"text":"temel dayanak","usage_role":"general"},{"applicability":"Bir işin onsuz yürümeyeceği temel unsur mecazlı ve doğal Türkçeyle anlatıldığında kullanılır.","error_profile":{"adds":"Beden parçası üzerinden güçlü bir mecaz ve örgütsel önem çağrışımı ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Temel destek ve vazgeçilmezlik ilişkisini korur."},"facet_ids":["F001","F002"],"text":"işin belkemiği","usage_role":"explanatory"}],"definition":"Bir işin, düzenin veya bedenin ayakta kalmasını, düzgün işlemesini ve tamamlanmasını sağlayan temel dayanak unsurudur. Kalbin beden için bu işlevi görmesi verilen başlıca örnektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir unsur, daha büyük bir işin veya düzenin dayandığı ve onun düzgün işlemesini sağlayan temeldir."},{"facet_id":"F002","role":"extension","statement":"Bu dayanak, işin doğruluğunu, sürekliliğini ve tamamlanmasını sağlayan belirleyici koşul olur."},{"facet_id":"F003","role":"example","statement":"Kalp, bedenin işleyişinin kendisine dayandığı temel unsur olarak gösterilir."}],"identity_rationale":"Kaynak ifadesi, bir işin ayakta kalmasını ve düzgün işlemesini sağlayan temel dayanağı açıkça tanımlar; kalbin beden için örnek verilmesi bu genel bağımlılık ilişkisinin özel bir uygulamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"işin dayandığı temel unsur"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kalp bedenin temel dayanağıdır"}],"lexicalization_note":"Anlam yalnız dayanak bildiren belirtili kalıplarda geçerlidir; kökün çıplak biçimine genel bir temel veya öz anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ayakta tutma, iç sağlamlık ve somut yapısal destekle en açıklayıcı sınırlar yayımlandı, öz, köken, yerleşme ve sınıflandırma adayları uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı belirli bir iş veya beden için kurucu dayanağı kalıplaşmış biçimde adlandırır; komşu dal ayakta tutan araçları geçim ve beden dâhil daha geniş alana yayar.","focus_only":"Anlam, dayanak bildiren belirli kalıplara bağlıdır ve bir işin doğruluğunu da içerir.","gloss":"temel dayanak ve yaşamı sürdüren unsur","neighbor_only":"Geçim, bedenin beslenmesi ve genel olarak varlığı sürdürme araçları da kapsanır.","neighbor_ref":"root_001273/B009","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin ayakta kalmasını ve işleyişini mümkün kılan temel unsuru anlatır."},{"boundary_match":"partial","distinction":"Odak dalı ayakta kalmanın bağlı olduğu unsuru gösterir; komşu dal ise ayakta kalan şeyin kendi içindeki sağlamlık niteliğini gösterir.","focus_only":"Ayakta kalmayı sağlayan belirli temel unsur adlandırılır.","gloss":"dayanak ve iç sağlamlık","neighbor_only":"Nesnenin kendi parçaları arasındaki sıkılık ve tutarlılık adlandırılır.","neighbor_ref":"root_001444/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir şeyin bozulmadan veya çökmeksizin ayakta kalmasıyla ilgilidir."},{"boundary_match":"partial","distinction":"Komşu dal somut taşıyıcı parçaları ve yerleşmeyi öne çıkarırken odak dalı bir işin doğruluğunu ve devamını sağlayan işlevsel temele uzanır.","focus_only":"Soyut işlerin veya bedenin işleyişine temel olan unsur da kapsanır.","gloss":"işlevsel dayanak ve yapısal destek","neighbor_only":"Kaburga ve yapı direği gibi somut taşıyıcı parçalar öne çıkar.","neighbor_ref":"root_000156/B009","relation_type":"near_neighbor","shared_zone":"İki dal da daha büyük bir bütünün üzerinde durduğu taşıyıcı unsuru anlatır."}],"source_phrase_ar":"ملاك الأمر ما يعتمد عليه (ayn)؛ القلب ملاك الجسد (ayn;sihah;mufradat)؛ هذا ملاك الأمر وملاكه أي صلاحه (tahdhib)","source_summary":"Kaynakların ortak açıklaması, bir işin kendisine dayandığı ve onun düzgün kalmasını sağlayan temel unsurdur; kalbin bedenle ilişkisi bu bağımlılık yapısını somutlaştırır.","sources":["AY","SI","TA","MU"],"what_is_ar":"ما يقوم به الأمر ويعتمد عليه؛ القلب ملاك الجسد","what_is_not_ar":"ليس الملك للسلطان ولا ملك اليد"},"support_links":["sup_247e039079f06dc5170b"]},{"boundary":"Tanım yol ve vadi kalıplarıyla sınırlıdır; her nesnenin genel ortası anlamına genişletilemez.","branch_kind":"mixed_non_bare","branch_ref":"root_001444/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَٰلِك","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ma`lik|ROOT:mlk|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:1:1","qac_word_ref":"1:4:1","surface_ar":"مَٰلِكِ"}],"gloss":"yolun veya yerin orta ya da ana kesimi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yolun veya vadinin orta ya da ana kesimi belirli bir kalıpla adlandırılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Vadi için orta kesimin yanında sınır, yol için ise büyük bölüm açıklaması da verilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı biçim bir yerleşimin orta veya büyük kesimi için de kullanılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bağlama göre kişi bu ana kesimi izlemeye ya da ondan uzak durmaya yönlendirilir."}}],"root_ar":"م ل ك","root_id":"root_001444","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yol, vadi ve yerleşim kalıplarındaki orta, büyük veya bağlama göre sınır kesimini kapsar.","boundary_detail":"Tanım yol ve vadi kalıplarıyla sınırlıdır; her nesnenin genel ortası anlamına genişletilemez.","branch_image_ar":"مَلَك الطريق والوادي","concept_gloss":"yolun veya yerin orta ya da ana kesimi","contextual_glosses":[{"applicability":"Yolun orta kesiminin izlenmesi veya boş bırakılması istendiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yolun ana bölümü, vadinin sınırı ve yerleşimin merkezi kapsamlarını dışarıda bırakır.","preserves":"Yol ve orta kesim ilişkisini korur."},"facet_ids":["F001","F004"],"text":"yolun ortası","usage_role":"contextual"},{"applicability":"Vadiye bağlı kullanımda kaynakların verdiği iki yer belirlemesini birlikte göstermek için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yol ve yerleşim kullanımlarını dışarıda bırakır.","preserves":"Vadi kullanımındaki orta ve sınır seçeneklerini korur."},"facet_ids":["F002"],"text":"vadinin orta veya sınır kesimi","usage_role":"explanatory"}],"definition":"Yolun, vadinin veya yerleşimin bağlama göre orta, ana ya da büyük kesimidir; vadi kullanımında sınır da bu adlandırmaya katılır. Söyleyişe göre bu kesim izlenecek bir güzergâh veya uzak durulacak bir yer olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yolun veya vadinin orta ya da ana kesimi belirli bir kalıpla adlandırılır."},{"facet_id":"F002","role":"source_variant","statement":"Vadi için orta kesimin yanında sınır, yol için ise büyük bölüm açıklaması da verilir."},{"facet_id":"F003","role":"extension","statement":"Aynı biçim bir yerleşimin orta veya büyük kesimi için de kullanılır."},{"facet_id":"F004","role":"associated_use","statement":"Bağlama göre kişi bu ana kesimi izlemeye ya da ondan uzak durmaya yönlendirilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"İdari veya işlevsel merkez anlamıyla karışabilir.","fit":"narrowing","loses":"Ana veya büyük kesim ile vadi sınırı seçeneklerini kaybeder.","preserves":"Orta yerde bulunma özelliğini korur."},"text":"merkez"}],"identity_rationale":"Kaynak ifadesi yol ve vadi için orta kısmı açıkça verir, ancak vadi kullanımında sınır, yol kullanımında ise ana veya büyük bölüm de aktarılır. Bu yüzden dal yalnız geometrik orta nokta diye daraltılmamalı, yerin ortası, ana kesimi veya bağlama göre sınırı olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yolun ortası veya ana kesimi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"vadinin sınırı veya orta kesimi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yerleşimin ortası veya büyük kesimi"}],"lexicalization_note":"Yolun ortası veya ana kesimi, vadinin ortası veya sınırı ve yerleşimin merkezi yalnız belgelenmiş biçim ve kalıplarda korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yolun ana hattı, genel orta konum ve dönemeçle sınırlar yayımlandı, yolculuk, dağ yolu ve yer çıkışı gibi yalnız aynı alanda bulunan adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı belirli yol, vadi ve yerleşim kalıplarında orta ya da ana kesimi adlandırır; komşu dal yolun güzergâh ve açıklık niteliğini daha genel işler.","focus_only":"Vadi sınırı ve yerleşimin merkezi gibi kalıba bağlı kullanımlar da vardır.","gloss":"yolun orta veya ana hattı","neighbor_only":"Yolun doğrultusu, açıklığı veya izlenmesi gereken güzergâhı daha geniş biçimde kapsanır.","neighbor_ref":"root_001371/B001","relation_type":"near_synonym","shared_zone":"İki dal da yolun ortası, ana kısmı ve izlenen doğrultusu alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal genel bir konumsal orta kavramıdır; odak dalı yalnız belirli yer kalıplarında orta, ana bölüm veya sınır olarak sözlüksel biçimde sınırlanmıştır.","focus_only":"Yol, vadi ve yerleşimle sınırlı ana kesim ve sınır kullanımları bulunur.","gloss":"yerin ana kesimi ve genel orta konum","neighbor_only":"Her tür nesne, topluluk veya sıralı yapıdaki iki uç arasındaki orta konum kapsanır.","neighbor_ref":"root_001646/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir bütünün uçları arasında bulunan orta bölgeyi gösterebilir."},{"boundary_match":"field_only","distinction":"Odak dalı bölümün bütün içindeki konumunu veya büyüklüğünü gösterir; komşu dal ise yolun biçim değiştirerek kıvrıldığı geçiş noktasını gösterir.","focus_only":"Yolun veya vadinin orta, ana ya da sınır kesimi belirtilir.","gloss":"orta kesim ve dönemeç","neighbor_only":"Dağ veya vadide yolun kıvrıldığı geçit ve dönemeç belirtilir.","neighbor_ref":"root_000208/B006","relation_type":"same_field","shared_zone":"İki dal yol ve vadi içindeki belirli bir yer bölümünü adlandırır."}],"source_phrase_ar":"ملك الطريق أيضا وسطه (sihah)؛ خل عن ملك الطريق وملك الوادي وملكه وملكه أي حده ووسطه (tahdhib)؛ الزم ملك الطريق أي وسطه (tahdhib)؛ أراد بالمملكة وسطها وملك الطريق معظمه ووسطه (tahdhib)","source_summary":"Kaynaklar yolun orta kesiminde birleşir; toplu ifade ayrıca yolun ana veya büyük bölümünü, vadinin orta ya da sınır kesimini ve yerleşimin merkezini kapsayan bağlama bağlı bir çeşitlilik gösterir.","sources":["SI","TA"],"what_is_ar":"وسط الطريق أو الوادي وحده ومعظمه؛ موضع يجتنب أو يلزم بحسب التعبير","what_is_not_ar":"ليس المَلِك الحاكم ولا المِلْك المالي"},"support_links":[]},{"boundary":"Bu anlam suyu yaşamsal ve düzen kurucu kaynak sayan kalıplara bağlıdır; her türlü soyut dayanağa genişletilemez.","branch_kind":"collocation","branch_ref":"root_001444/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَٰلِك","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ma`lik|ROOT:mlk|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:1:1","qac_word_ref":"1:4:1","surface_ar":"مَٰلِكِ"}],"gloss":"işleri ve yaşamı sürdüren su kaynağı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su, yolcunun veya topluluğun işlerini yürütebilmesini sağlayan temel kaynaktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Su kaynakları konaklama, geçim ve topluluk düzeninin sürmesini mümkün kılar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Suyun yokluğu çaresizlik, çok sayıda su kaynağı ise geniş yaşam imkânı olarak ifade edilir."}}],"root_ar":"م ل ك","root_id":"root_001444","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Suyun yolculuk, konaklama ve topluluk geçimi için belirleyici dayanak olduğu kullanımları kapsar.","boundary_detail":"Bu anlam suyu yaşamsal ve düzen kurucu kaynak sayan kalıplara bağlıdır; her türlü soyut dayanağa genişletilemez.","branch_image_ar":"الماء مَلَك الأمر","concept_gloss":"işleri ve yaşamı sürdüren su kaynağı","contextual_glosses":[{"applicability":"Yolcunun su sayesinde ihtiyaçlarını karşılayıp yolculuğunu yönetebildiği bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Topluluğun konaklama ve ortak geçim kapsamını dışarıda bırakır.","preserves":"Su ile işini yürütebilme arasındaki araç ilişkisini korur."},"facet_ids":["F001"],"text":"yolcunun işini gördüren su","usage_role":"explanatory"},{"applicability":"Bir topluluğun sularının onun yerleşme ve geçinme imkânını sağladığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek yolcunun suyla kendi işini yönetmesi kapsamını dışarıda bırakır.","preserves":"Su kaynaklarının ortak yaşamı ve geçimi sürdürme işlevini korur."},"facet_ids":["F002","F003"],"text":"geçimi ayakta tutan su kaynakları","usage_role":"contextual"}],"definition":"Su, yolcunun veya bir topluluğun işini denetim altında tutmasını, konaklamasını ve geçimini sürdürmesini sağlayan temel kaynaktır. Suyun bulunmaması bu yeterliğin yokluğu, çok sayıda su kaynağı ise güçlü yaşam imkânı olarak anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su, yolcunun veya topluluğun işlerini yürütebilmesini sağlayan temel kaynaktır."},{"facet_id":"F002","role":"extension","statement":"Su kaynakları konaklama, geçim ve topluluk düzeninin sürmesini mümkün kılar."},{"facet_id":"F003","role":"associated_use","statement":"Suyun yokluğu çaresizlik, çok sayıda su kaynağı ise geniş yaşam imkânı olarak ifade edilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yolculuk, konaklama ve topluluk işlerini yürütme işlevini kaybeder.","preserves":"Suyun doğrudan yaşamsal kullanımını korur."},"text":"içme suyu"}],"identity_rationale":"Kaynak ifadesi suyu yalnız içecek olarak değil, yolcunun veya topluluğun işini yürütebilmesini ve geçimini sürdürebilmesini sağlayan belirleyici kaynak olarak sunar. Bu nedenle dal, suyun kendisi ile suyun işleri ayakta tutan dayanak oluşunu birlikte korumalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"işini yürütmesini sağlayan su"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"hiç suyu yok"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"sularımız geçimimizi ayakta tutar"}],"lexicalization_note":"Tanım yalnız suyun yolcu veya topluluk için işleri yürütme ve yaşamı sürdürme aracı olduğunu bildiren kalıplaşmış söyleyişlere bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; canı sürdüren su, genel geçim ve genel dayanakla en yakın sınırlar yayımlandı, kuyu, su yolu ve belirli yiyecek çiftleri yalnız aynı yaşam senaryosunu paylaştığı için elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı suyun yolcu ve topluluk için işlevsel kaynak oluşunu vurgular; komşu dal suyu içecek olarak kişinin canlılığını ve suya doymasını sağlayan şey sayar.","focus_only":"Su, yolculuk ve topluluk düzenini yönetmeyi sağlayan kaynak olarak ele alınır.","gloss":"işleri sürdüren ve canı koruyan su","neighbor_only":"İçeceğin ferahlatıcı bolluğu ve kişinin canını sürdürmesi öne çıkar.","neighbor_ref":"root_001533/B008","relation_type":"near_synonym","shared_zone":"İki dal da suyun yaşamı sürdürmesi ve yeterlik sağlaması üzerinde birleşir."},{"boundary_match":"partial","distinction":"Odak dalı geçimi sağlayan unsuru suyla sınırlar ve onu işleri yönetme aracı sayar; komşu dal geçimin bütün maddi ve mekânsal araçlarını kapsar.","focus_only":"Dayanak özellikle su ve su kaynaklarıdır.","gloss":"su kaynağı ve genel geçim","neighbor_only":"Yiyecek, içecek, kazanç yolu ve yaşama yeri gibi bütün geçim araçları kapsanır.","neighbor_ref":"root_001067/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da hayatın ve geçimin sürmesini sağlayan kaynaklarla ilgilidir."},{"boundary_match":"partial","distinction":"Odak dalı genel dayanak kalıbını suya, yolculuğa ve topluluk geçimine özelleştirir; komşu dal dayanağın ne olduğuna dair böyle bir madde sınırlaması taşımaz.","focus_only":"Belirleyici dayanak su olarak ve yaşam düzeni bağlamında somutlaştırılır.","gloss":"suya bağlı geçim ve genel dayanak","neighbor_only":"Herhangi bir işin veya bedenin dayandığı temel unsur olabilir.","neighbor_ref":"root_001444/B005","relation_type":"near_neighbor","shared_zone":"İki dal da bir işin ayakta kalmasını sağlayan vazgeçilmez dayanak ilişkisini kurar."}],"source_phrase_ar":"والملك الماء يكون مع المسافر لأنه إذا كان معه ملك أمره (maqayis)؛ الماء ملك أمر أي يقوم به الأمر (sihah)؛ الماء ملك أمره (tahdhib)؛ الماء ملاك الأشياء يضرب للشيء الذي به كمال الأمر (tahdhib)؛ ماله ملك ولا نقر أي ما له ماء (tahdhib)؛ مياهنا ملوكنا ومات فلان عن ملوك كثيرة (tahdhib)","source_summary":"Kaynaklar suyu, yolcunun veya topluluğun işlerini yürütüp yaşamını sürdürebilmesinin temel şartı olarak açıklar; tekil su varlığı ile topluluğa ait çok sayıdaki kaynak aynı işlevsel çekirdeğe bağlanır.","sources":["MQ","SI","TA"],"what_is_ar":"الماء الذي به يملك المسافر أو القوم أمرهم؛ المياه التي يقوم بها النزول والمعيشة","what_is_not_ar":"ليس مطلق مِلاك الأمر المجرد ولا ملك المال"},"support_links":[]},{"boundary":"Bu alan hayvanlarla sınırlı önden gitme ve yönlendirmedir; insanlar üzerindeki siyasi yönetim değildir.","branch_kind":"collocation","branch_ref":"root_001444/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَٰلِك","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ma`lik|ROOT:mlk|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:1:1","qac_word_ref":"1:4:1","surface_ar":"مَٰلِكِ"}],"gloss":"hayvanlarda önden gidip yön veren unsur","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hayvanlar bağlamında önde bulunan unsur, geri kalanların hareketini yönlendirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Arı topluluğunda önde gelen ve topluluğu yönlendiren canlı adlandırılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Deve veya koyun sürüsünde önden gidip diğerlerinin izlediği öncü adlandırılır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Binek hayvanında ön ayaklar ve hayvanın yönlendirilmesini sağlayan ön kısım adlandırılır."}}],"root_ar":"م ل ك","root_id":"root_001444","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlı öncüyü ve bineğin yönlendirici ön bölümünü işlev ortaklığıyla kapsar.","boundary_detail":"Bu alan hayvanlarla sınırlı önden gitme ve yönlendirmedir; insanlar üzerindeki siyasi yönetim değildir.","branch_image_ar":"المتقدم القائد في الحيوان","concept_gloss":"hayvanlarda önden gidip yön veren unsur","contextual_glosses":[{"applicability":"Deve veya koyun sürüsünde önden gidip geri kalanın izlediği canlı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Arı topluluğu ile bineğin ön ayakları ve yönlendirici kısmını dışarıda bırakır.","preserves":"Canlı öncü, önden gitme ve izlenme ilişkisini korur."},"facet_ids":["F003"],"text":"sürünün öncüsü","usage_role":"contextual"},{"applicability":"Binek hayvanının ön ayakları ve hareketine yön veren ön kısmı kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Topluluk içindeki canlı önder ve izlenme ilişkisini dışarıda bırakır.","preserves":"Önden taşıma ve yön verme işlevini korur."},"facet_ids":["F004"],"text":"bineği yönelten ön bölüm","usage_role":"explanatory"}],"definition":"Bir hayvan topluluğunda önden gidip geri kalanların izlediği önder canlı veya bir binek hayvanını önden yönelten beden bölümüdür. Arı topluluğunun önderi, sürünün öncüsü ve bineğin ön ayakları ile yönlendirici kısmı bu kalıba bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hayvanlar bağlamında önde bulunan unsur, geri kalanların hareketini yönlendirir."},{"facet_id":"F002","role":"specialization","statement":"Arı topluluğunda önde gelen ve topluluğu yönlendiren canlı adlandırılır."},{"facet_id":"F003","role":"specialization","statement":"Deve veya koyun sürüsünde önden gidip diğerlerinin izlediği öncü adlandırılır."},{"facet_id":"F004","role":"source_variant","statement":"Binek hayvanında ön ayaklar ve hayvanın yönlendirilmesini sağlayan ön kısım adlandırılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İnsan toplumu üzerinde siyasi ve hukuki yönetim yetkisi ekler.","collision":"Aynı kökün kamusal egemenlik dalıyla karışır.","fit":"broadening","loses":null,"preserves":"Önde bulunma ve başkalarını yönlendirme özelliklerini korur."},"text":"hükümdar"}],"identity_rationale":"Kaynak ifadesi hayvan topluluklarında önden gidip diğerlerinin izlediği canlıyı açıkça içerir, fakat binek kullanımında önderlik canlı bir bireyden çok hayvanın ön ayakları ve yönlendirici kısmına yüklenir. Dal bu iki gerçekleşmeyi tek bir canlı önder imgesine indirgememelidir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"arı topluluğunun önderi"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bineğin ön ayakları ve yönlendirici kısmı"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"deve ve koyun sürüsünün öncüsü"}],"lexicalization_note":"Anlam yalnız arı topluluğu, binek hayvanı, deve ve koyun sürüsüyle kurulan kalıplarda geçerlidir; genel liderlik anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel önderlik, önce gelen topluluk ve itibarlı baş kişiyle sınırlar yayımlandı, hayvan türü adları ve sürüden ayrılma gibi işlevsel örtüşmesi olmayan adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı hayvanlara bağlı sözlüksel kalıpları ve beden bölümünü içerir; komşu dal örnek alınan genel önderliği birçok insanî ve nesnel alana yayar.","focus_only":"Hayvan topluluğundaki öncü ve bineğin yönlendirici ön bölümüyle sınırlıdır.","gloss":"hayvan öncüsü ve genel önder","neighbor_only":"İnsan, ibadet, kitap, yol ve yapı gibi çok çeşitli alanlarda örnek alınan veya başa geçirilen unsur kapsanır.","neighbor_ref":"root_000053/B009","relation_type":"near_neighbor","shared_zone":"İki dal da önde bulunup geri kalana yön veren veya izlenen unsur düşüncesini taşır."},{"boundary_match":"partial","distinction":"Odak dalında öncelik yön verme ve izlenme işlevi taşır; komşu dalda ise insanların hızlı biçimde önce gelmesi yeterlidir ve liderlik gerekmez.","focus_only":"Öndeki unsur diğer hayvanların hareketini yönlendirir veya taşır.","gloss":"yön veren öncü ve önce gelenler","neighbor_only":"İnsan topluluğunun hızlı ve erken gelen ilk bölümü anlatılır.","neighbor_ref":"root_000698/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir topluluğun geri kalanından önce bulunmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dalı fiilî olarak önden gidilen ve izlenen hareket düzenini anlatır; komşu dal saygın insanın anılma sırasındaki önceliğini anlatır.","focus_only":"Hayvan alanındaki hareket ve yönlendirme ilişkisi belirleyicidir.","gloss":"hareket öncüsü ve itibarlı baş kişi","neighbor_only":"Bir insanın üstün konumu nedeniyle adının önce anılması belirleyicidir.","neighbor_ref":"root_000091/B003","relation_type":"near_neighbor","shared_zone":"İki dalda da bir grubun başında veya önünde bulunan seçkin unsur vardır."}],"source_phrase_ar":"مليك النحل يعسوبها (sihah)؛ ملك الدابة قوائمها وهاديها (sihah;tahdhib)؛ جاءنا تقوده ملكه يعني قوائمه وهاديه (tahdhib)؛ ملك الإبل والشاء ما يتقدم ويتبعه سائره (mufradat)","source_summary":"Kaynaklar hayvan alanında önde bulunma ve yön verme işlevini paylaşır; bu işlev arı veya sürüde izlenen canlıya, binek hayvanında ise hareketi önden taşıyan ayaklara ve yönlendirici kısma yüklenir.","sources":["SI","TA","MU"],"what_is_ar":"يعسوب النحل؛ هادي الدابة وقوائمها؛ ما يتقدم الإبل والشاء ويتبعه سائره","what_is_not_ar":"ليس ملك الناس ولا سلطان الرعية"},"support_links":[]},{"boundary":"Bu dal sözlükte kaydedilen varlık adını ve kaynakların etimolojik açıklamasını verir; güç, sahiplik veya egemenlik anlamı vermez.","branch_kind":"unresolved","branch_ref":"root_001444/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَٰلِك","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ma`lik|ROOT:mlk|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:1:1","qac_word_ref":"1:4:1","surface_ar":"مَٰلِكِ"}],"gloss":"ilahi haberci varlık","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ad, ilahi haber veya buyruk ileten haberci varlığı belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynaklar adın ses ve harf düzeni değişmiş daha eski biçimlerini aktarır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Türetim, güç, sahiplik veya egemenlikten değil, haber götürme ve elçilik anlamından açıklanır."}}],"root_ar":"م ل ك","root_id":"root_001444","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözlükte kaydedilen varlık adını karşılar; onu güç, sahiplik veya egemenlik alanının bir anlamı olarak sunmaz.","boundary_detail":"Bu dal sözlükte kaydedilen varlık adını ve kaynakların etimolojik açıklamasını verir; güç, sahiplik veya egemenlik anlamı vermez.","branch_image_ar":"المَلَك من الملائكة","concept_gloss":"ilahi haberci varlık","contextual_glosses":[{"applicability":"Varlığın Tanrı adına haber ve buyruk iletme işlevi açıklanırken kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İlahi görevlendirme, elçilik ve varlık niteliğini korur."},"facet_ids":["F001"],"text":"ilahi elçi varlık","usage_role":"explanatory"}],"definition":"İlahi buyruğu veya haberi ileten haberci varlığın adıdır. Dal ayrıca kaynakların bu adı, haber götürme ve elçilik anlamıyla ilişkili daha eski biçimlerden açıklayan etimolojik kaydını kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ad, ilahi haber veya buyruk ileten haberci varlığı belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Kaynaklar adın ses ve harf düzeni değişmiş daha eski biçimlerini aktarır."},{"facet_id":"F003","role":"source_variant","statement":"Türetim, güç, sahiplik veya egemenlikten değil, haber götürme ve elçilik anlamından açıklanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İnsan toplumu üzerinde siyasi yönetim yetkisi ekler.","collision":"Aynı yazım çevresindeki kamusal egemenlik dalıyla karışır.","fit":"displacement","loses":"İlahi haber götürme ve görünmez haberci varlık kimliğini kaybeder.","preserves":"Üst bir otoriteyle ilişki çağrışımını çok dolaylı biçimde korur."},"text":"hükümdar"}],"identity_rationale":"Kaynak ifadesi, ilahi haberci varlığın tekil adını ve çoğul sınıfını doğrudan tanımlar; ayrıca adı haber götürme ve elçilik anlamıyla ilişkilendirilen daha eski biçimlerden açıklar. Dal, mevcut zarf içinde bu sözlük biçimi ve etimolojik açıklama olarak tutulabilir; güç, özel sahiplik ya da kamusal egemenlik anlamı sayılmamalıdır.","lexicalization_note":"Mekanik kapsam çözümlenmemiştir; hiçbir çıplak kök anlamı varsayılmaz ve kavram yalnız kaynakta açıklanan ad ile etimolojik tartışma düzeyinde tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; haber, gönderme ve elçilik dalları yalnız kaynakların etimolojik açıklamasıyla ilişkilidir, güç ve egemenlik dalları ise kavram sınırının dışındadır; bu nedenle doğrudan bir anlam komşusu yayımlanmadı.","source_phrase_ar":"الملك واحد الملائكة إنما هو تخفيف الملأك والأصل مألك (ayn)؛ مألك من الألوك وهو الرسالة (ayn)؛ الملك من الملائكة واحد وجمع (sihah)؛ أصله مألك بتقديم الهمزة من الألوك وهي الرسالة (sihah)؛ الملك واحد الملائكة إنما هو تخفيف الملأك وهو مفعل من الألوك (tahdhib)","source_summary":"Kaynaklar ilahi haberci varlığın adını ve çoğul sınıfını tanır; aynı zamanda adın daha eski biçimlerden ses ve harf düzeni değişerek geldiğini, bu biçimlerin de haber götürme ve elçilik anlamıyla açıklandığını ortak biçimde aktarır.","sources":["AY","SI","TA"],"what_is_ar":"لفظ المَلَك والملائكة الوارد في المصادر مع بيان أصله من الملأك والألوك والرسالة","what_is_not_ar":"ليس من قوة المِلْك ولا سلطان المُلك في تعليل المصادر"},"support_links":[]},{"boundary":"Bu dal yalnızca sınırları gün doğumu ve gün batımıyla belirlenen gündüz süresini kapsar; belirsiz süre, devir ve olay anlamları ayrı dallardadır.","branch_kind":"bare","branch_ref":"root_001700/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَوْم","morph_features":"STEM|POS:N|LEM:yawom|ROOT:ywm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:2:1","qac_word_ref":"1:4:2","surface_ar":"يَوْمِ"}],"gloss":"güneşin doğuşundan batışına kadarki gün","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başlangıcı güneşin doğuşu, sonu güneşin batışıdır; aynı zamanda sayılabilen günlerden biridir."}}],"root_ar":"ي و م","root_id":"root_001700","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Günün geceyi dışarıda bırakan, doğal ışık sınırlarıyla belirlenmiş tek bir zaman birimi olarak kastedildiği kullanımlara uygundur.","boundary_detail":"Bu dal yalnızca sınırları gün doğumu ve gün batımıyla belirlenen gündüz süresini kapsar; belirsiz süre, devir ve olay anlamları ayrı dallardadır.","branch_image_ar":"وقت النهار المحدود","concept_gloss":"güneşin doğuşundan batışına kadarki gün","contextual_glosses":[{"applicability":"Karşıtlığın geceyle kurulduğu ve sayılabilir birim özelliğinin bağlamdan zaten anlaşıldığı cümlelerde doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güneşin doğuşu ile batışı arasındaki aydınlık zaman aralığını korur."},"facet_ids":["F001"],"text":"gündüz vakti","usage_role":"contextual"},{"applicability":"Hem doğal gündüz sınırının hem de bunun tek bir sayılabilir birim olduğunun açıkça belirtilmesi gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sınırlandırılmış gündüz süresini ve onun tek bir gün birimi oluşunu birlikte korur."},"facet_ids":["F001"],"text":"bir günlük gündüz süresi","usage_role":"explanatory"}],"definition":"Güneşin doğuşundan batışına kadar uzanan bilinen zaman aralığı ve bu aralıklardan oluşan dizinin tek bir birimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başlangıcı güneşin doğuşu, sonu güneşin batışıdır; aynı zamanda sayılabilen günlerden biridir."}],"identity_rationale":"Kaynak ifadesi, bilinen günü güneşin doğuşundan batışına kadar süren zaman olarak tanımlar ve onu günler dizisinin tek bir birimi sayar. Verilen dal çerçevesi bu iki kurucu özelliği de doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"güneşin doğuşundan batışına kadarki gün"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bu anlamdaki günlerin çoğulu"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"gün gün veya gündelik esasa göre yapılan işlem"}],"lexicalization_note":"Dal yalın kullanımı tanımlar; günlük işlem bildiren türemiş kullanım, temel gün anlamının yerine geçirilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca gündüz sınırı, belirsiz süre ve olay günüyle doğrudan karışabilecek üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, başlangıcı güneşin doğuşu olan sayılabilir günü tanımlar. Komşu dal ise şafaktan başlayan gündüzü ve onun ışığını öne çıkarır; bu yüzden sınırları tam örtüşmez.","focus_only":"Gün doğumunu kesin başlangıç sayar ve aralığı sayılabilir tek bir gün birimi olarak kurar.","gloss":"gün ile gündüz","neighbor_only":"Gündüz ışığını ve şafaktan gün batımına uzanan süreyi kapsar; ayrıca gündüzle ilişkili başka kullanımları da içerir.","neighbor_ref":"root_001559/B002","relation_type":"near_synonym","shared_zone":"İkisi de gecenin karşısındaki aydınlık zaman kesitini gün batımına kadar anlatır."},{"boundary_match":"partial","distinction":"Bu dal doğal göksel sınırları olan bilinen gündür; komşu dalın süresi belirlenmemiştir ve devir kadar genişleyebilir.","focus_only":"Süreyi gün doğumu ile gün batımı arasında kesin olarak sınırlar.","gloss":"sınırlı gün ile belirsiz süre","neighbor_only":"Her uzunluktaki bir zaman dilimini ve bazı bağlamlarda bir devri anlatabilir.","neighbor_ref":"root_001700/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir zaman kesitini gün sözü üzerinden kavramlaştırır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği zamansal sınırdır. Komşu dalda gün, olayın büyüklüğünü veya çetinliğini taşıyan mecazî ve bağlama bağlı bir anlatıma dönüşür.","focus_only":"Olayın niteliğinden bağımsız, gerçek bir gündüz zaman aralığını belirtir.","gloss":"zaman birimi ile olay günü","neighbor_only":"Büyük veya çetin bir olayı, onun yaşandığı kritik günü ya da çoğulda olayları belirtir.","neighbor_ref":"root_001700/B003","relation_type":"near_neighbor","shared_zone":"Olay dalındaki kullanımlar, bir gün içinde yaşananlardan hareketle bu zaman birimiyle ilişki kurar."}],"source_phrase_ar":"اليوم: الواحد من الأيام (maqayis)؛ اليوم مقداره من طلوع الشمس إلى غروبها (ayn;tahdhib)؛ اليوم معروف والجمع أيام (sihah)؛ اليوم يعبر به عن وقت طلوع الشمس إلى غروبها (mufradat)","source_summary":"Kaynaklar, bilinen günün güneşin doğuşuyla başlayıp batışıyla bittiği ve çoğulu bulunan sayılabilir bir zaman birimi olduğu konusunda birleşir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"اليوم المعروف: وقت من طلوع الشمس إلى غروبها، وهو الواحد من الأيام وجمعه أيام.","what_is_not_ar":"ليس المراد هنا مطلق الدهر، ولا الوقائع والنعم، ولا تركيب يومئذ."},"support_links":[]},{"boundary":"Bu dal, uzunluğu önceden belirlenmeyen süreyi ve bağlama bağlı devir anlamını kapsar; belirli gündüz aralığını veya olayın kendisini tanımlamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001700/B002","candidate_links":[{"candidate_id":"cand_ceeeb8799a41d7f31756","lane":"micro"},{"candidate_id":"cand_b6d347cb5abb89b72475","lane":"micro"},{"candidate_id":"cand_85368a4b3f75ed141a49","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَوْم","morph_features":"STEM|POS:N|LEM:yawom|ROOT:ywm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:2:1","qac_word_ref":"1:4:2","surface_ar":"يَوْمِ"}],"gloss":"herhangi bir zaman dilimi; bağlama göre devir","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Herhangi bir uzunluktaki zaman süresini belirtir ve bilinen gündüz sınırlarına bağlı değildir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlama göre uzun bir devir veya bir varlığın yaşadığı dönemler anlamına genişleyebilir."}}],"root_ar":"ي و م","root_id":"root_001700","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sürenin gün doğumu ve gün batımıyla sınırlandırılmadığı, kısa veya uzun bir dönem ya da bütün bir devir olarak yorumlandığı kullanımlara uygundur.","boundary_detail":"Bu dal, uzunluğu önceden belirlenmeyen süreyi ve bağlama bağlı devir anlamını kapsar; belirli gündüz aralığını veya olayın kendisini tanımlamaz.","branch_image_ar":"مدة من الزمان","concept_gloss":"herhangi bir zaman dilimi; bağlama göre devir","contextual_glosses":[{"applicability":"Sürenin sınırlarının önem taşımadığı ve yalnızca belirsiz bir zaman kesitinin anlatıldığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uzunluğu belirtilmemiş bir zaman dilimi olma özelliğini korur."},"facet_ids":["F001"],"text":"bir zaman","usage_role":"contextual"},{"applicability":"Bağlam sözün tek bir günü değil, uzun bir hayat veya tarih dönemini anlattığını gösterdiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözün uzun bir döneme genişleyen bağlamsal kullanımını korur."},"facet_ids":["F002"],"text":"devir","usage_role":"contextual"}],"definition":"Uzunluğu önceden sınırlandırılmamış bir zaman dilimidir; bazı bağlamlarda kişinin veya bir şeyin devri kadar geniş bir süreyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Herhangi bir uzunluktaki zaman süresini belirtir ve bilinen gündüz sınırlarına bağlı değildir."},{"facet_id":"F002","role":"extension","statement":"Bağlama göre uzun bir devir veya bir varlığın yaşadığı dönemler anlamına genişleyebilir."}],"identity_rationale":"Kaynak ifadesi sözü herhangi bir uzunluktaki zaman süresi için genişletir ve bazı kullanımlarda devir anlamına geldiğini açıkça belirtir. Dal çerçevesi, sınırlı gündüz anlamından bu geniş zamansal kullanıma geçişi doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"herhangi bir zaman dilimi; bağlama göre devir"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"iki devri veya bollukla sıkıntı, cömertlikle savaş gibi iki karşıt hali"}],"lexicalization_note":"Yalın biçimin belirsiz süre ve devir kullanımı, iki karşıt hayat durumunu anlatan özel söz öbeğinden ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; süre, devir, zaman parçası ve aynı kökün literal ya da olay odaklı dallarıyla sınırı açıklayan beş komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gün sözünün süre ve devir anlamındaki genişlemesidir. Komşu dal daha genel olarak vakti, anı ve dönemi kapsadığı için bütün bağlamlarda birbirinin yerine geçmez.","focus_only":"Gün sözünün herhangi bir süreye ve bağlama göre bütün bir devre genişlemesini içerir.","gloss":"zaman dilimi ile vakit","neighbor_only":"Bir şeyin vakti, yakın veya gerçekleşmiş anı ve bağlama bağlanan o sırada anlamlarını da içerir.","neighbor_ref":"root_000382/B001","relation_type":"near_synonym","shared_zone":"İki dal da uzunluğu kesin olmayan bir zamanı veya dönemi anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın uzunluk bakımından üst sınırı yoktur. Komşu dal daha sınırlı bir zaman parçasına yönelir ve yerleşme anlamı da taşır.","focus_only":"Süreyi herhangi bir uzunlukta bırakabilir ve onu devir anlamına kadar genişletebilir.","gloss":"serbest süre ile sınırlı zaman parçası","neighbor_only":"Devreden daha kısa belirli bir zaman parçasını ve bir yerde kalmayı da anlatır.","neighbor_ref":"root_000307/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de günün doğal sınırlarına bağlı olmayan bir zaman parçasını belirtebilir."},{"boundary_match":"partial","distinction":"Odak dal çok kısa süreden devre kadar geniştir; komşu dal ise parçalanmış veya birkaç gün süren daha sınırlı bir kesiti öne çıkarır.","focus_only":"Her uzunluktaki süreyi ve bir devri kapsayabilir.","gloss":"belirsiz süre ile zaman parçası","neighbor_only":"Bir parça zaman, birkaç gün süren ara dönem veya devam eden durumla sınırlıdır.","neighbor_ref":"root_000664/B005","relation_type":"near_synonym","shared_zone":"İki dal da kesin başlangıç ve bitişi verilmeyen bir süreyi anlatır."},{"boundary_match":"partial","distinction":"Bu dalın süresi bağlamca belirlenir; komşu dalın sınırları ise güneşin hareketine göre sabittir.","focus_only":"Süreyi doğal gündüz sınırlarından bağımsız bırakır ve devir anlamına genişletebilir.","gloss":"belirsiz süre ile bilinen gün","neighbor_only":"Güneşin doğuşundan batışına kadar kesin sınırlı tek bir gün birimidir.","neighbor_ref":"root_001700/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da gün sözünün bir zaman kesitini anlatan kullanımlarıdır."},{"boundary_match":"partial","distinction":"Odak dal zamansal niceliği korur. Komşu dal zamanı, olayın kendisine veya onun çetinliğine aktaran bir kullanımdır.","focus_only":"Yalnızca zamanın uzunluğunu veya bir devri belirtir.","gloss":"süre ile olay","neighbor_only":"Büyük ya da çetin olayı, olayın yaşandığı kritik günü veya çoğulda olayları anlatır.","neighbor_ref":"root_001700/B003","relation_type":"near_neighbor","shared_zone":"Her iki genişleme de literal gün anlamından hareket eder ve tek bir gündüzü aşabilir."}],"source_phrase_ar":"مدة من الزمان أي مدة كانت (mufradat)؛ اليوم ها هنا بمعنى الدهر (tahdhib)؛ شر أيام دهرها (tahdhib)","source_summary":"Kaynaklar bu kullanımda gün sözünün sabit gündüz süresinden çıkarak herhangi bir zaman dilimini, özel bağlamlarda ise bir devri anlatabildiğini gösterir.","sources":["TA","MU"],"what_is_ar":"اليوم بمعنى مدة من الزمان أي مدة كانت، أو بمعنى الدهر في بعض الاستعمال.","what_is_not_ar":"ليس محصورا في النهار من طلوع الشمس إلى غروبها، ولا هو خصوص الوقائع أو النعم."},"support_links":["sup_247e039079f06dc5170b","sup_9076b32659455b9ab4a1","sup_ec98c3825f872a39c0a9"]},{"boundary":"Dal, büyük veya çetin olayla bağlantılı mecazî ve kalıplaşmış kullanımlarla sınırlıdır; literal zaman süresi ve yalnızca Tanrı'ya bağlanan anma günleri dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_001700/B003","candidate_links":[{"candidate_id":"cand_b6d98f0c83a6743ebe20","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَوْم","morph_features":"STEM|POS:N|LEM:yawom|ROOT:ywm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:2:1","qac_word_ref":"1:4:2","surface_ar":"يَوْمِ"}],"gloss":"büyük olayın yaşandığı çetin gün veya olay","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gün sözü, büyük bir olay gerçekleştiğinde o kritik zamanı veya gerçekleşen olayı anlatmak üzere aktarılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli kalıplarda günün çok çetin, ağır ve etkisi uzun süren bir gün olduğu vurgulanır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çoğul biçim, bilinen günlerde gerçekleşmiş önemli olayları veya tarihî vakaları anlatabilir."}}],"root_ar":"ي و م","root_id":"root_001700","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözün sıradan bir zaman biriminden çok büyük olayın gerçekleşmesini, olayın kendisini ya da çetinliğini öne çıkardığı kullanımlara uygundur.","boundary_detail":"Dal, büyük veya çetin olayla bağlantılı mecazî ve kalıplaşmış kullanımlarla sınırlıdır; literal zaman süresi ve yalnızca Tanrı'ya bağlanan anma günleri dışarıda kalır.","branch_image_ar":"كائنة اليوم وشدته","concept_gloss":"büyük olayın yaşandığı çetin gün veya olay","contextual_glosses":[{"applicability":"Büyük bir olayın meydana geldiği zamanın, olayla özdeşleşmiş bir dönüm noktası olarak anlatıldığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Büyük olayın gerçekleşmesiyle belirlenen kritik zaman özelliğini korur."},"facet_ids":["F001"],"text":"kritik olay anı","usage_role":"contextual"},{"applicability":"Olayın niteliğinden çok, o günün insanlar üzerindeki ağır ve uzayan etkisinin vurgulandığı kalıplarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günün şiddetini ve etkisinin uzamasını belirten özel yüzü korur."},"facet_ids":["F002"],"text":"çok çetin gün","usage_role":"contextual"},{"applicability":"Çoğul biçimin günlerin sürelerini değil, o günlerde gerçekleşmiş bilinen olayları anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çoğul gün biçiminin olaylar toplamına aktarılmasını korur."},"facet_ids":["F003"],"text":"tarihî olaylar","usage_role":"contextual"}],"definition":"Büyük veya çetin bir olayın gerçekleştiği kritik günü ya da olayın kendisini anlatan aktarmalı kullanımdır. Bazı kalıplarda çok ağır bir gün, çoğul biçimde ise yaşanmış önemli olaylar anlamı taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gün sözü, büyük bir olay gerçekleştiğinde o kritik zamanı veya gerçekleşen olayı anlatmak üzere aktarılır."},{"facet_id":"F002","role":"specialization","statement":"Belirli kalıplarda günün çok çetin, ağır ve etkisi uzun süren bir gün olduğu vurgulanır."},{"facet_id":"F003","role":"extension","statement":"Çoğul biçim, bilinen günlerde gerçekleşmiş önemli olayları veya tarihî vakaları anlatabilir."}],"identity_rationale":"Kaynak ifadesi büyük olay, olayın gerçekleşmesi, şiddetli gün ve çoğulda yaşanmış olaylar kullanımlarını aynı dalda toplar. Bu çerçeve kullanılabilir, ancak bunların tek bir yalın anlam değil, gün ile olay arasındaki aktarmaya dayanan bağlı kullanımlar olduğu açıkça belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"büyük olay, olayın gerçekleştiği kritik gün veya çetin gün"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"çok çetin gün veya savaş günü"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bilinen günlerde gerçekleşmiş olaylar"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"çok çetin gün"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kötülüğü insanlar üzerinde uzun süren çetin gün"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kötülüğü insanlar üzerinde uzun süren çetin gün"}],"lexicalization_note":"Olayı anlatan biçimsel genişleme, şiddetli gün bildiren kalıplar ve çoğul olay anlamı ayrı yüzler olarak korunur; kalıp anlamları yalın kullanıma genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; olay, felaket ve şiddet alanındaki en yakın üç aday ile aynı kökün literal gün ve süre dalları sınırı en iyi açıkladığı için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal olayın bir günle ilişkilendirilmesine dayanır. Komşu dal ise olayı ya da felaketi doğrudan adlandırır ve günle kurulmuş bu aktarmayı gerektirmez.","focus_only":"Gün sözünün kritik zamana, çetin güne ve çoğulda olaylara aktarılmasını içerir.","gloss":"olay günü ile sonradan çıkan olay","neighbor_only":"Zaman adından bağımsız olarak sonradan ortaya çıkan olay, felaket ve devrin sıkıntısını doğrudan adlandırır.","neighbor_ref":"root_000299/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir devrin önemli, ağır veya beklenmedik olayını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalda şiddet bir güne yüklenebilir ve olay-zaman bağı kurucudur. Komşu dalın çekirdeği ise gün kavramından bağımsız felaket ve sıkıntıdır.","focus_only":"Kritik gün, büyük olay ve çoğul olaylar arasında gün temelli bir aktarım kurar.","gloss":"çetin gün ile felaket","neighbor_only":"Felaketi, sıkıntıyı ve devrin değişen darbelerini doğrudan anlatır.","neighbor_ref":"root_001378/B006","relation_type":"near_neighbor","shared_zone":"İki dal da insanları etkileyen ağır bir olay veya sıkıntı alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı yönü zaman ile olay arasındaki aktarmadır. Komşu dal olayın kapanmış ve aşırı şiddetli niteliğine odaklanır.","focus_only":"Olayı yaşandığı kritik gün üzerinden anlatır ve çoğulda olaylar anlamına geçebilir.","gloss":"çetin gün ile şiddetli felaket","neighbor_only":"Çıkış yolu bulunmayan şiddetli iş, fitne veya felaketi doğrudan niteler.","neighbor_ref":"root_000884/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da ağır, korkutucu ve insanları zorlayan olayları anlatır."},{"boundary_match":"partial","distinction":"Odak dalda gün, olayın kendisini ya da niteliğini taşır. Komşu dal yalnızca doğal sınırları bulunan zaman aralığıdır.","focus_only":"Günü olayın büyüklüğüne veya çetinliğine aktarır.","gloss":"olay günü ile literal gün","neighbor_only":"Olaydan bağımsız olarak gün doğumu ile gün batımı arasındaki zaman birimini belirtir.","neighbor_ref":"root_001700/B001","relation_type":"near_neighbor","shared_zone":"Kritik olay, literal bir gün içinde gerçekleşebildiği için iki kullanım aynı zaman zeminini paylaşır."},{"boundary_match":"partial","distinction":"Odak dalda belirleyici unsur olaydır; komşu dalda ise yalnızca zamanın uzunluğu veya dönem oluşu korunur.","focus_only":"Büyük olayın gerçekleşmesini, çetinliği veya olaylar toplamını anlatır.","gloss":"olay odaklı gün ile süre","neighbor_only":"Olay niteliği eklemeden herhangi bir zaman dilimini ya da devri belirtir.","neighbor_ref":"root_001700/B002","relation_type":"near_neighbor","shared_zone":"İki dal da literal tek gün sınırını aşan kullanımlardır."}],"source_phrase_ar":"يستعيرونه في الأمر العظيم ويقولون نعم فلان في اليوم إذا نزل (maqayis)؛ اليوم: الكون، الكائنة من الكون إذا نزلت أو حدثت (ayn;tahdhib)؛ الشدة باليوم (sihah)؛ اليوم الشديد: يوم ذو أيام (ayn;tahdhib)؛ الأيام في معنى الوقائع (tahdhib)","source_summary":"Kaynaklar gün sözünün büyük bir olayın gerçekleşmesine aktarılmasını, çetin gün anlatımında kullanılmasını ve çoğul biçimin olayları belirtmesini aynı anlamsal aile içinde verir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه استعارة اليوم للأمر العظيم، والكائنة إذا نزلت، واليوم الشديد، والأيام بمعنى الوقائع.","what_is_not_ar":"لا يدخل فيه اليوم الزمني المحض، ولا خصوص أيام الله من جهة النعم والعذاب، ولا أسماء يام."},"support_links":["sup_5e5a60a15581f02f2ebd"]},{"boundary":"Dal yalnızca Tanrı'ya bağlanarak nimet, bağışlama, ceza veya ibret verici olayla anılan günleri kapsar; her önemli ya da çetin gün buraya girmez.","branch_kind":"collocation","branch_ref":"root_001700/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَوْم","morph_features":"STEM|POS:N|LEM:yawom|ROOT:ywm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:2:1","qac_word_ref":"1:4:2","surface_ar":"يَوْمِ"}],"gloss":"Tanrı'nın nimet ve ibret verici işleriyle anılan günler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Günler, Tanrı'nın insanlara yönelik etkili ve hatırlanmaya değer işleriyle ilişkilendirilir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anılan işler nimet verme ve bağışlamanın yanı sıra bir topluluğa inen cezayı da kapsayabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Günlerin Tanrı'ya bağlanması, o günlerde verilen nimetler ve gerçekleşen işler nedeniyle onlara özel değer kazandırır."}}],"root_ar":"ي و م","root_id":"root_001700","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Günlerin Tanrı'ya bağlanarak nimet, bağışlama, ceza veya unutulmaması gereken toplumsal olayları hatırlattığı özel ifadeye uygundur.","boundary_detail":"Dal yalnızca Tanrı'ya bağlanarak nimet, bağışlama, ceza veya ibret verici olayla anılan günleri kapsar; her önemli ya da çetin gün buraya girmez.","branch_image_ar":"أيام النعم والوقائع الإلهية","concept_gloss":"Tanrı'nın nimet ve ibret verici işleriyle anılan günler","contextual_glosses":[{"applicability":"Bağlam özellikle verilen nimetleri ve bağışlamayı hatırlatıyorsa kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tanrı'ya bağlanan günlerin nimet ve bağışlama yönünü korur."},"facet_ids":["F001","F002"],"text":"Tanrı'nın nimet günleri","usage_role":"contextual"},{"applicability":"Bağlam geçmiş bir topluluğa inen ceza veya hatırlanması gereken sarsıcı olayı öne çıkarıyorsa uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tanrı'ya bağlanan günlerin ceza ve ibret verici olay yönünü korur."},"facet_ids":["F001","F002"],"text":"Tanrı'nın ibret günleri","usage_role":"contextual"}],"definition":"Tanrı'nın nimet, bağışlama veya cezalandırma gibi unutulmaması gereken etkileriyle anılan günlerdir. Bu bağlama, söz konusu günlerin önemini ve hatırlatıcı değerini yükseltir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Günler, Tanrı'nın insanlara yönelik etkili ve hatırlanmaya değer işleriyle ilişkilendirilir."},{"facet_id":"F002","role":"example","statement":"Anılan işler nimet verme ve bağışlamanın yanı sıra bir topluluğa inen cezayı da kapsayabilir."},{"facet_id":"F003","role":"associated_use","statement":"Günlerin Tanrı'ya bağlanması, o günlerde verilen nimetler ve gerçekleşen işler nedeniyle onlara özel değer kazandırır."}],"identity_rationale":"Kaynak ifadesi, Tanrı'ya bağlanan günleri insanlara hatırlatılan nimet, bağışlama, ceza ve toplumsal olaylarla açıklar; bu bağlamanın günlere özel değer kazandırdığını da belirtir. Verilen dal çerçevesi bu sınırlı ifadeyi doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"Tanrı'nın nimet, bağışlama ve cezalandırma olaylarıyla anılan günleri"}],"lexicalization_note":"Anlam yalnızca Tanrı'ya bağlanan günler ifadesine aittir; nimet, ceza ve anma içeriği yalın gün sözüne genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca olay günü, literal gün ve belirsiz süre dalları okuyucu açısından gerçek sınır karşılaştırması sunduğu için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir Tanrı'ya bağlama ifadesiyle sınırlıdır ve nimet ile cezayı anma amacı taşır. Komşu dal genel olay ve çetinlik aktarımıdır.","focus_only":"Günleri Tanrı'nın nimeti, bağışlaması veya cezasıyla ilişkilendirir ve hatırlatıcı değer taşır.","gloss":"ilahi anma günleri ile olay günleri","neighbor_only":"Herhangi bir büyük veya çetin olayı, kritik günü ya da çoğulda olayları Tanrı'ya bağlama şartı olmadan anlatır.","neighbor_ref":"root_001700/B003","relation_type":"near_neighbor","shared_zone":"İki dal da önemli veya sarsıcı olayların gerçekleştiği günleri olay üzerinden anlamlandırır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği özel bağlama ve hatırlatılan ilahi iştir; komşu dal yalnızca gündüz süresidir.","focus_only":"Günü Tanrı'nın hatırlanmaya değer işi ve verdiği özel değer üzerinden niteler.","gloss":"anma günü ile literal gün","neighbor_only":"Herhangi bir olay veya değer yüklemeden gün doğumu ile gün batımı arasındaki zaman birimini belirtir.","neighbor_ref":"root_001700/B001","relation_type":"near_neighbor","shared_zone":"Anılan olayların gerçekleştiği günler literal zaman birimlerinden oluşur."},{"boundary_match":"thematic_only","distinction":"Odak dal olay ve kutsal bağlama dayalı özel bir ifadedir; komşu dal nötr bir süre veya devir anlamıdır ve anlamsal çekirdekleri örtüşmez.","focus_only":"Tanrı'ya bağlanan, nimet veya ceza olaylarıyla anılan günleri belirtir.","gloss":"anılan günler ile süre","neighbor_only":"Herhangi bir olay veya ilahi bağ kurmadan uzunluğu belirsiz süreyi ya da devri belirtir.","neighbor_ref":"root_001700/B002","relation_type":"thematic","shared_zone":"Her iki dal da gün sözünden hareketle tek bir literal gündüzü aşan zaman anlatımlarına katılır."}],"source_phrase_ar":"وذكرهم بأيام الله: بما نزل بعاد وثمود وغيرهم من العذاب، وبالعفو عن آخرين (tahdhib)؛ جاءت الأيام بمعنى الوقائع والنعم (tahdhib)؛ أيامه: نعمه (tahdhib)؛ إضافة الأيام إلى الله تشريف لأمرها لما أفاض الله عليهم من نعمه فيها (mufradat)","source_summary":"Kaynaklar, Tanrı'ya bağlanan günlerin nimetleri ve önemli işleri hatırlattığını; bu işlerin bağışlama kadar cezayı da içerebildiğini ve bağlamanın günleri yücelttiğini gösterir.","sources":["TA","MU"],"what_is_ar":"يدخل فيه أيام الله وما في معناها من أيام النعم والوقائع التي يذكر بها، من عفو أو نعمة أو عذاب نزل بقوم.","what_is_not_ar":"ليس كل جمع أيام، ولا كل يوم شديد، ولا مجرد مدة زمانية."},"support_links":[]},{"boundary":"Bu dal bağımsız bir gün anlamı değil, bağlamda daha önce veya sonra belirlenen güne gönderme yapan birleşik yapıdır.","branch_kind":"non_bare","branch_ref":"root_001700/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَوْم","morph_features":"STEM|POS:N|LEM:yawom|ROOT:ywm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:2:1","qac_word_ref":"1:4:2","surface_ar":"يَوْمِ"}],"gloss":"bağlamda işaret edilen o gün veya o sırada","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birleşik yapı, hangi gün olduğu bağlamdan belirlenen zamana gönderme yapar."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yapı, birleşmenin dilbilgisel değerlendirilmesine göre çekimli veya değişmez biçimde gerçekleşebilir."}}],"root_ar":"ي و م","root_id":"root_001700","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Konuşma veya metin bağlamının belirli bir günü önceden ya da sonradan tanımladığı ve birleşik yapının o zamana gönderme yaptığı kullanımlara uygundur.","boundary_detail":"Bu dal bağımsız bir gün anlamı değil, bağlamda daha önce veya sonra belirlenen güne gönderme yapan birleşik yapıdır.","branch_image_ar":"يوم مضاف إلى إذ","concept_gloss":"bağlamda işaret edilen o gün veya o sırada","contextual_glosses":[{"applicability":"Bağlamın belirli bir takvim gününü veya olay gününü açıkça belirlediği cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlamda belirlenen tek bir güne geriye veya ileriye dönük gönderimi korur."},"facet_ids":["F001"],"text":"o gün","usage_role":"contextual"},{"applicability":"Gönderimin takvim gününden çok anlatılan olayın gerçekleştiği zamana yöneldiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlamda işaret edilen zamana gönderim işlevini korur."},"facet_ids":["F001"],"text":"o sırada","usage_role":"contextual"}],"definition":"Gün sözü bağlamda işaret edilen zamana gönderme yapan bir belirteçle birleşir ve o gün veya o sırada anlamını verir. Birleşik yapı, kuruluşuna göre çekimli ya da değişmez biçimde kullanılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birleşik yapı, hangi gün olduğu bağlamdan belirlenen zamana gönderme yapar."},{"facet_id":"F002","role":"associated_use","statement":"Yapı, birleşmenin dilbilgisel değerlendirilmesine göre çekimli veya değişmez biçimde gerçekleşebilir."}],"identity_rationale":"Kaynak ifadesi gün sözünün bağlamda işaret edilen zamanı gösteren bir belirteçle birleştiğini, ortaya çıkan yapının o gün anlamına geldiğini ve yapıya göre çekimli ya da değişmez olabildiğini belirtir. Dal çerçevesi bu dilbilgisel ve gönderimsel yapıyı doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"o gün; o sırada"}],"lexicalization_note":"Anlam yalnızca gün ile bağlama işaret eden belirtecin birleşik yapısına aittir; yalın gün sözüne yeni bir kök anlamı olarak aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bağlama bağlı yapıyla doğrudan karşılaştırılabilen literal gün ve belirsiz süre dalları dışında yararlı bir anlamsal komşu bulunmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bağlama bağımlı ve dilbilgisel olarak birleşik bir gösterimdir. Komşu dal ise bağlamdan bağımsız temel zaman birimidir.","focus_only":"Hangi günün kastedildiğini bağlamdan alan birleşik bir gönderim yapısıdır.","gloss":"o gün yapısı ile literal gün","neighbor_only":"Gün doğumu ile gün batımı arasındaki zaman birimini kendi başına tanımlar.","neighbor_ref":"root_001700/B001","relation_type":"near_neighbor","shared_zone":"Birleşik yapı, gönderimde bulunduğu zamanı literal gün kavramı üzerinden kurar."},{"boundary_match":"thematic_only","distinction":"Odak dalın görevi belirli bir zamana işaret etmektir; komşu dal ise zamanın süresini belirsiz bırakır ve gönderim yapısı kurmaz.","focus_only":"Bağlamın belirlediği tek bir güne veya ana gönderme yapar.","gloss":"işaret edilen gün ile belirsiz süre","neighbor_only":"Uzunluğu belirsiz herhangi bir zaman dilimini ve bağlama göre bir devri anlatır.","neighbor_ref":"root_001700/B002","relation_type":"thematic","shared_zone":"İki dal da bağlamın zaman yorumunu belirlemesine izin veren gün temelli anlatımlardır."}],"source_phrase_ar":"يركب يوم مع إذ، فيقال: يومئذ؛ وربما يعرب ويبنى، وإذا بني فللإضافة إلى إذ (mufradat)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak, gün sözünün işaret belirteciyle birleşmesini ve bu yapının çekimli ya da değişmez kullanılabilmesini birlikte kaydeder."}],"source_summary":"Dal, bağımsız bir kök anlamından çok bağlamca belirlenen güne gönderme yapan birleşik bir zaman gösterimidir.","sources":["MU"],"what_is_ar":"تركيب يوم مع إذ في يومئذ للدلالة على وقت مشار إليه في السياق، مع جواز الإعراب أو البناء بحسب الإضافة.","what_is_not_ar":"ليس أصلا دلاليا جديدا لليوم، ولا أسماء يام، ولا اليوم الشديد."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["1:4:1"],"branch_refs":[],"candidate_id":"cand_d584a6130d5e5d7473c4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001444"],"scope":"focus_ayah","source_local_id":"1:4:1:authority-time-reckoning-compression","source_type":"word_analysis","support_ids":["sup_17b1771aa0e4a29e83b1","sup_613fd4393bdcab97ac78"],"title":"head word launches a descending authority hierarchy","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:1","qac_refs":["1:4:1:1"],"status":"accepted"}},{"anchor_refs":["1:4:1"],"branch_refs":[],"candidate_id":"cand_d096bda5e280690e7233","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001444"],"scope":"focus_ayah","source_local_id":"1:4:1:construct-head-definiteness","source_type":"word_analysis","support_ids":["sup_4bd53eaa2010b4506441","sup_613fd4393bdcab97ac78"],"title":"construct head governs the Day and receives definiteness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:1","qac_refs":["1:4:1:1"],"status":"accepted"}},{"anchor_refs":["1:4:1"],"branch_refs":[],"candidate_id":"cand_10e2975e2a43470504da","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001444"],"scope":"focus_ayah","source_local_id":"1:4:1:genitive-apposition-chain","source_type":"word_analysis","support_ids":["sup_613fd4393bdcab97ac78","sup_973e971167e834110985"],"title":"genitive apposition continues the praise chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:1","qac_refs":["1:4:1:1"],"status":"accepted"}},{"anchor_refs":["1:4:1"],"branch_refs":[],"candidate_id":"cand_bc7ccb77c27d95f4e829","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001444"],"scope":"focus_ayah","source_local_id":"1:4:1:intertext-and-forward-bridge","source_type":"word_analysis","support_ids":["sup_459b2375c87d374c5011","sup_613fd4393bdcab97ac78"],"title":"ownership title bridges earlier attributes and later petition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:1","qac_refs":["1:4:1:1"],"status":"accepted"}},{"anchor_refs":["1:4:1"],"branch_refs":[],"candidate_id":"cand_1d7af88ee1616911f9ff","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001444"],"scope":"focus_ayah","source_local_id":"1:4:1:marked-divine-possessor-distribution","source_type":"word_analysis","support_ids":["sup_613fd4393bdcab97ac78","sup_64e74d3a1f4c07c93894"],"title":"rare active-possessor form is salient in divine attribute contexts","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:1","qac_refs":["1:4:1:1"],"status":"accepted"}},{"anchor_refs":["1:4:1"],"branch_refs":[],"candidate_id":"cand_e2881ce3aeac695d0ee6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001444"],"scope":"focus_ayah","source_local_id":"1:4:1:ownership-disposal-root-pressure","source_type":"word_analysis","support_ids":["sup_613fd4393bdcab97ac78","sup_819f8345fb1c0289c479"],"title":"ownership carries disposal force without importing every root branch","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:1","qac_refs":["1:4:1:1"],"status":"accepted"}},{"anchor_refs":["1:4:1"],"branch_refs":[],"candidate_id":"cand_38982be08ab072d2bed3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001444"],"scope":"focus_ayah","source_local_id":"1:4:1:qiraat-authority-range","source_type":"word_analysis","support_ids":["sup_613fd4393bdcab97ac78","sup_b4185d17d054e7ca7628"],"title":"variant readings expose owner, king, and intensified authority","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:1","qac_refs":["1:4:1:1"],"status":"accepted"}},{"anchor_refs":["1:4:1"],"branch_refs":[],"candidate_id":"cand_2c15ff8bded81f35718e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001444"],"scope":"focus_ayah","source_local_id":"1:4:1:sound-and-orthographic-pressure","source_type":"word_analysis","support_ids":["sup_613fd4393bdcab97ac78","sup_fee32f29cb2a0b8b041d"],"title":"vowel length and sound contour make the head word perceptible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:1","qac_refs":["1:4:1:1"],"status":"accepted"}},{"anchor_refs":["1:4:1"],"branch_refs":[],"candidate_id":"cand_730efd9f2f5303871ec2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001444"],"scope":"focus_ayah","source_local_id":"1:4:1:standing-possessor-not-event","source_type":"word_analysis","support_ids":["sup_613fd4393bdcab97ac78","sup_ed8e8d5c6ff316dd8d8a"],"title":"active participle presents standing ownership","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:1","qac_refs":["1:4:1:1"],"status":"accepted"}},{"anchor_refs":["1:4:2"],"branch_refs":[],"candidate_id":"cand_1f877dfa4ec3fe370653","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"1:4:2:definite-named-day","source_type":"word_analysis","support_ids":["sup_51cf6e466b7c15530bf3","sup_71e70fb8c4d8f3b6fd87"],"title":"bare construct noun becomes a definite named temporal unit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:2","qac_refs":["1:4:2:1"],"status":"accepted"}},{"anchor_refs":["1:4:2"],"branch_refs":[],"candidate_id":"cand_6d0df9f1bcd7ffaece09","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"1:4:2:elastic-event-time","source_type":"word_analysis","support_ids":["sup_14c1b20570559be207bc","sup_51cf6e466b7c15530bf3"],"title":"day carries bounded time and eschatological event scope","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:2","qac_refs":["1:4:2:1"],"status":"accepted"}},{"anchor_refs":["1:4:2"],"branch_refs":[],"candidate_id":"cand_77edb4e22927fa721fc3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"1:4:2:formulaic-day-of-reckoning","source_type":"word_analysis","support_ids":["sup_51cf6e466b7c15530bf3","sup_8c112abe26320d4b702e"],"title":"recurring reckoning formula is activated by the middle word","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:2","qac_refs":["1:4:2:1"],"status":"accepted"}},{"anchor_refs":["1:4:2"],"branch_refs":[],"candidate_id":"cand_cb477dad6b63424e0da0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"1:4:2:middle-idafa-hinge","source_type":"word_analysis","support_ids":["sup_51cf6e466b7c15530bf3","sup_6de496dddc7dfca67bc2"],"title":"middle noun is governed and governing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:2","qac_refs":["1:4:2:1"],"status":"accepted"}},{"anchor_refs":["1:4:2"],"branch_refs":[],"candidate_id":"cand_8823bb766dbdf09fc3d9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"1:4:2:morphologically-stable-time-noun","source_type":"word_analysis","support_ids":["sup_51cf6e466b7c15530bf3","sup_ff4ec64a41acd87c78f8"],"title":"frequent root remains locked to temporal noun use","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:2","qac_refs":["1:4:2:1"],"status":"accepted"}},{"anchor_refs":["1:4:2"],"branch_refs":[],"candidate_id":"cand_1db655de3c463b2220da","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"1:4:2:qiraat-adverbial-contrast","source_type":"word_analysis","support_ids":["sup_51cf6e466b7c15530bf3","sup_7b30429bf1ce383d9449"],"title":"case variants show how the canonical genitive keeps the chain intact","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:2","qac_refs":["1:4:2:1"],"status":"accepted"}},{"anchor_refs":["1:4:2"],"branch_refs":[],"candidate_id":"cand_e60580c7d8041ce6afdd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"1:4:2:scene-and-forward-pressure","source_type":"word_analysis","support_ids":["sup_51cf6e466b7c15530bf3","sup_76cc63a82aa9c81cef1e"],"title":"temporal frame turns praise toward petition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:2","qac_refs":["1:4:2:1"],"status":"accepted"}},{"anchor_refs":["1:4:2"],"branch_refs":[],"candidate_id":"cand_267db6728a85591e6977","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"1:4:2:sound-cadence-binding","source_type":"word_analysis","support_ids":["sup_4bc8ad33cd3cfb1a8928","sup_51cf6e466b7c15530bf3"],"title":"sound binds the Day to the final reckoning noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:2","qac_refs":["1:4:2:1"],"status":"accepted"}},{"anchor_refs":["1:4:3"],"branch_refs":[],"candidate_id":"cand_bed7dfd1a0af1a64ff96","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"1:4:3:closure-scene-architecture","source_type":"word_analysis","support_ids":["sup_5cc9eecb7b90639f6d3d","sup_fa7492dd0f3b6cc0fcd0"],"title":"final term supplies the scene's governing content","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:3","qac_refs":["1:4:3:1","1:4:3:2"],"status":"accepted"}},{"anchor_refs":["1:4:3"],"branch_refs":[],"candidate_id":"cand_73cc49fe9b05fcad2f67","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"1:4:3:cosmic-order-parallels","source_type":"word_analysis","support_ids":["sup_01013f3d0430275cbec1","sup_5cc9eecb7b90639f6d3d"],"title":"dīn as ordered way broadens juridical reckoning","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:3","qac_refs":["1:4:3:1","1:4:3:2"],"status":"accepted"}},{"anchor_refs":["1:4:3"],"branch_refs":[],"candidate_id":"cand_da9701c50c4e99cd327d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"1:4:3:debt-obligation-image","source_type":"word_analysis","support_ids":["sup_4589d16da66ea5b6fe31","sup_5cc9eecb7b90639f6d3d"],"title":"debt-accounting image sharpens abstract judgment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:3","qac_refs":["1:4:3:1","1:4:3:2"],"status":"accepted"}},{"anchor_refs":["1:4:3"],"branch_refs":[],"candidate_id":"cand_f60d772bab6dd2a01454","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"1:4:3:definite-chain-terminus","source_type":"word_analysis","support_ids":["sup_23d201850bbb4c6d14cb","sup_5cc9eecb7b90639f6d3d"],"title":"final definite genitive closes and defines the chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:3","qac_refs":["1:4:3:1","1:4:3:2"],"status":"accepted"}},{"anchor_refs":["1:4:3"],"branch_refs":[],"candidate_id":"cand_a72fdd098e559cf96684","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"1:4:3:formula-and-root-pair","source_type":"word_analysis","support_ids":["sup_0bc779fd208db092d121","sup_5cc9eecb7b90639f6d3d"],"title":"final word completes the recurring Day formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:3","qac_refs":["1:4:3:1","1:4:3:2"],"status":"accepted"}},{"anchor_refs":["1:4:3"],"branch_refs":[],"candidate_id":"cand_565536b084f1144440c2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"1:4:3:generative-parse-layering","source_type":"word_analysis","support_ids":["sup_5cc9eecb7b90639f6d3d","sup_c82c2ec94ed066047591"],"title":"parse and qiraat alternatives layer belonging and characterization","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:3","qac_refs":["1:4:3:1","1:4:3:2"],"status":"accepted"}},{"anchor_refs":["1:4:3"],"branch_refs":[],"candidate_id":"cand_81a543ae3500e59dd7bc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"1:4:3:marked-ownership-over-reckoning","source_type":"word_analysis","support_ids":["sup_5cc9eecb7b90639f6d3d","sup_a72e773b70cd46efe06b"],"title":"ordinary Day formula is drawn under ownership language","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:3","qac_refs":["1:4:3:1","1:4:3:2"],"status":"accepted"}},{"anchor_refs":["1:4:3"],"branch_refs":[],"candidate_id":"cand_3aaf3c5b2783c78bce5d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"1:4:3:nominal-system-not-event-verb","source_type":"word_analysis","support_ids":["sup_5cc9eecb7b90639f6d3d","sup_807fe6a67fa2a2d47348"],"title":"definite abstract noun names a system rather than narrating an action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:3","qac_refs":["1:4:3:1","1:4:3:2"],"status":"accepted"}},{"anchor_refs":["1:4:3"],"branch_refs":[],"candidate_id":"cand_31d7d133ce1a3349a29c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"1:4:3:polyvalent-reckoning-system","source_type":"word_analysis","support_ids":["sup_02c8df68324c0e51b0eb","sup_5cc9eecb7b90639f6d3d"],"title":"judgment remains selected while debt and submission pressure survive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:3","qac_refs":["1:4:3:1","1:4:3:2"],"status":"accepted"}},{"anchor_refs":["1:4:3"],"branch_refs":[],"candidate_id":"cand_d9121b28b3a0313c67ad","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"1:4:3:sound-definiteness-and-rhyme","source_type":"word_analysis","support_ids":["sup_5cc9eecb7b90639f6d3d","sup_af40b71ee4e9ff0f1d18"],"title":"assimilation, doubled onset, and nasal rhyme weight the final noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"1:4:3","qac_refs":["1:4:3:1","1:4:3:2"],"status":"accepted"}},{"anchor_refs":["1:4:1"],"branch_refs":[],"candidate_id":"cand_3ea7ead20d81d4fd76fb","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001444"],"scope":"focus_ayah","source_local_id":"1:4:1:1","source_type":"qac_morpheme","support_ids":["sup_fd8b5adbbedbb1e0027b"],"title":"QAC root occurrence: م ل ك","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["1:4:2"],"branch_refs":[],"candidate_id":"cand_1a5189fd545f17b7f6a7","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"1:4:2:1","source_type":"qac_morpheme","support_ids":["sup_9689a9db629abd007935"],"title":"QAC root occurrence: ي و م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["1:4:3"],"branch_refs":[],"candidate_id":"cand_eda2018d432ebffbb5bf","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"1:4:3:2","source_type":"qac_morpheme","support_ids":["sup_39de4f6450273056ca0c"],"title":"QAC root occurrence: د ي ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["1:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"1:4","branch_refs":["root_000504/B002","root_001444/B003","root_001700/B003"],"candidate_id":"cand_b6d98f0c83a6743ebe20","commentary_obligation":"review","hft_ref":"hft_78d184fee34bdac2b4ca","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_sovereign_reckoning_event","source_type":"hft","support_ids":["sup_5e5a60a15581f02f2ebd"],"title":"b_sovereign_reckoning_event","trust":"legacy_unbound"},{"anchor_refs":["1:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"1:4","branch_refs":["root_000504/B003","root_001444/B002","root_001700/B002"],"candidate_id":"cand_ceeeb8799a41d7f31756","commentary_obligation":"review","hft_ref":"hft_c7605eafceac319286b8","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_debt_maturity","source_type":"hft","support_ids":["sup_9076b32659455b9ab4a1"],"title":"b_debt_maturity","trust":"legacy_unbound"},{"anchor_refs":["1:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"1:4","branch_refs":["root_000504/B001","root_001444/B003","root_001700/B002"],"candidate_id":"cand_b6d347cb5abb89b72475","commentary_obligation":"review","hft_ref":"hft_0ef5c978a575388dfdb5","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_obedience_regime","source_type":"hft","support_ids":["sup_ec98c3825f872a39c0a9"],"title":"b_obedience_regime","trust":"legacy_unbound"},{"anchor_refs":["1:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"1:4","branch_refs":["root_000504/B005","root_000504/B006","root_001444/B001","root_001444/B005","root_001700/B002"],"candidate_id":"cand_85368a4b3f75ed141a49","commentary_obligation":"review","hft_ref":"hft_a90f2f2d2edb2ab0382b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_mainstay_of_customary_order","source_type":"hft","support_ids":["sup_247e039079f06dc5170b"],"title":"b_mainstay_of_customary_order","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"مَٰلِكِ يَوْمِ ٱلدِّينِ","qac_morphemes":[{"lemma_ar":"مَٰلِك","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ma`lik|ROOT:mlk|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:1:1","qac_word_ref":"1:4:1","root_ar":"م ل ك","surface_ar":"مَٰلِكِ"},{"lemma_ar":"يَوْم","morph_features":"STEM|POS:N|LEM:yawom|ROOT:ywm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:2:1","qac_word_ref":"1:4:2","root_ar":"ي و م","surface_ar":"يَوْمِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"1:4:3:1","qac_word_ref":"1:4:3","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:3:2","qac_word_ref":"1:4:3","root_ar":"د ي ن","surface_ar":"دِّينِ"}],"word_analysis_qac_refs":[["1:4:1:1"],["1:4:2:1"],["1:4:3:1","1:4:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["1:4:1","1:4:2","1:4:3"]},"focus_surface_evidence":{"arabic_uthmani":"مَٰلِكِ يَوْمِ ٱلدِّينِ","qac_morphemes":[{"lemma_ar":"مَٰلِك","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ma`lik|ROOT:mlk|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:1:1","qac_word_ref":"1:4:1","root_ar":"م ل ك","surface_ar":"مَٰلِكِ"},{"lemma_ar":"يَوْم","morph_features":"STEM|POS:N|LEM:yawom|ROOT:ywm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:2:1","qac_word_ref":"1:4:2","root_ar":"ي و م","surface_ar":"يَوْمِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"1:4:3:1","qac_word_ref":"1:4:3","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:4:3:2","qac_word_ref":"1:4:3","root_ar":"د ي ن","surface_ar":"دِّينِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["1:4:1:1"],["1:4:2:1"],["1:4:3:1","1:4:3:2"]],"word_analysis_refs":["1:4:1","1:4:2","1:4:3"],"word_rows":[{"analysis_record_ref":"1:4:1","analytic_gloss_range_en":"standing possessor and disposer over the specific Day of reckoning; qiraat keep kingly sovereignty in view, but the aligned surface foregrounds active ownership in a construct chain","analytic_root_gloss_range_en":"broad root range includes ownership, disposal, kingship, dominion, cohesion, and other construction-bound branches; the local word selects divine possessive authority over the Day","qac_refs":["1:4:1:1"],"root":{"arabic":"م ل ك","transliteration":"m-l-k"},"surface":{"arabic":"مَٰلِكِ","transliteration":"māliki"}},{"analysis_record_ref":"1:4:2","analytic_gloss_range_en":"the specific Day as a possessed temporal unit and eschatological event-horizon; broader day, span, and epoch senses are narrowed by the reckoning construct","analytic_root_gloss_range_en":"root range centers on day, time-span, event-day, and marked divine occasion; locally it is the stable temporal noun that mediates ownership and reckoning","qac_refs":["1:4:2:1"],"root":{"arabic":"ي و م","transliteration":"y-w-m"},"surface":{"arabic":"يَوْمِ","transliteration":"yawmi"}},{"analysis_record_ref":"1:4:3","analytic_gloss_range_en":"the known reckoning order that defines the Day; judgment and requital are selected while debt-settlement, obligation, obedience, and submission pressures remain locally relevant","analytic_root_gloss_range_en":"root range includes obedience, religion, judgment, recompense, debt, obligation, subjugation, and ordered way; the local formula selects reckoning as a binding moral system","qac_refs":["1:4:3:1","1:4:3:2"],"root":{"arabic":"د ي ن","transliteration":"d-y-n"},"surface":{"arabic":"ٱلدِّينِ","transliteration":"ad-dīni"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["1:4"],"branch_refs":["root_000504/B002","root_001444/B003","root_001700/B003"],"candidate_id":"cand_b6d98f0c83a6743ebe20","evidence_scope":"focus_ayah","hft_ref":"hft_78d184fee34bdac2b4ca","item_id":"b_sovereign_reckoning_event","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_sovereign_reckoning_event","support_id":"sup_5e5a60a15581f02f2ebd"},{"anchor_refs":["1:4"],"branch_refs":["root_000504/B003","root_001444/B002","root_001700/B002"],"candidate_id":"cand_ceeeb8799a41d7f31756","evidence_scope":"focus_ayah","hft_ref":"hft_c7605eafceac319286b8","item_id":"b_debt_maturity","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_debt_maturity","support_id":"sup_9076b32659455b9ab4a1"},{"anchor_refs":["1:4"],"branch_refs":["root_000504/B001","root_001444/B003","root_001700/B002"],"candidate_id":"cand_b6d347cb5abb89b72475","evidence_scope":"focus_ayah","hft_ref":"hft_0ef5c978a575388dfdb5","item_id":"b_obedience_regime","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_obedience_regime","support_id":"sup_ec98c3825f872a39c0a9"},{"anchor_refs":["1:4"],"branch_refs":["root_000504/B005","root_000504/B006","root_001444/B001","root_001444/B005","root_001700/B002"],"candidate_id":"cand_85368a4b3f75ed141a49","evidence_scope":"focus_ayah","hft_ref":"hft_a90f2f2d2edb2ab0382b","item_id":"b_mainstay_of_customary_order","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_mainstay_of_customary_order","support_id":"sup_247e039079f06dc5170b"}],"diagnostics":[],"lane_counts":{"global":9,"macro":17,"micro":4},"packet_summary":{"ayah_count":7,"focus_ref":"1:4","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001064","furuq_root_norm":"ع و ن","furuq_source_root_norm":"ع و ن","is_dominant":true,"target_occurrences":10,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001069","furuq_root_norm":"ع ي ن","furuq_source_root_norm":"ع ي ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["1:1","1:2","1:3","1:4","1:5","1:6","1:7"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"1:4","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":21,"unstructured_record_count":0},"identity":{"ayah_ref":"1:4","lane":"micro","linguistic_source_ref":"1:4","surface_ref":"1:4","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"1:4","target_tokens":[["Hesap",["1:4:3"]],["gününün",["1:4:2"]],["sahibidir",["1:4:1"]]],"text":"Hesap gününün sahibidir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":7,"id":"s001-p01-001-007","label":"Whole surah","number":1,"refs":["1:1","1:2","1:3","1:4","1:5","1:6","1:7"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:3:cosmic-order-parallels","source_type":"word_analysis","support_id":"sup_01013f3d0430275cbec1","text":"{\"blocking_evidence\":null,\"headline\":\"dīn as ordered way broadens juridical reckoning\",\"reader_payoff\":\"The reader notices that legal judgment is not isolated from a wider moral-cosmic order, while the local phrase still lands on reckoning.\",\"reason\":\"Parallel order-language references (9:36, 12:40, 30:30, 98:5) and cognate judgment pressure support the wider order field, but local grammar keeps the final noun as the Day's defining reckoning content.\",\"representative_source_ids\":[\"MS-cef1ecb7\",\"MI-5a9e2836\",\"MS-f0eff266\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:3:polyvalent-reckoning-system","source_type":"word_analysis","support_id":"sup_02c8df68324c0e51b0eb","text":"{\"blocking_evidence\":null,\"headline\":\"judgment remains selected while debt and submission pressure survive\",\"reader_payoff\":\"The reader hears reckoning as a binding moral order: judgment, requital, debt-settlement, and submission pressure remain together without reducing the word to one flat gloss.\",\"reason\":\"V4 accepts judgment, obedience, debt, and subjugation branches, while the local day-of-reckoning collocation selects reckoning as the governing sense.\",\"representative_source_ids\":[\"QS-1df59362\",\"QS-eb019d2a\",\"MS-dd4bb324\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:3:formula-and-root-pair","source_type":"word_analysis","support_id":"sup_0bc779fd208db092d121","text":"{\"blocking_evidence\":null,\"headline\":\"final word completes the recurring Day formula\",\"reader_payoff\":\"The reader recognizes the final word as what turns the temporal noun into the recurring Day-of-reckoning formula.\",\"reason\":\"The row evidence lists the formula across references (15:35, 26:82, 37:20, 38:78, 51:12, 56:56, 70:26, 74:46, 82:15, 82:17, 82:18, 83:11), and V4 includes the collocation as judgment and recompense.\",\"representative_source_ids\":[\"QI-e4c53c77\",\"QI-ffaf132c\",\"MI-7a53717c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:2:elastic-event-time","source_type":"word_analysis","support_id":"sup_14c1b20570559be207bc","text":"{\"blocking_evidence\":null,\"headline\":\"day carries bounded time and eschatological event scope\",\"reader_payoff\":\"The reader feels the Day as both a bounded temporal object and a decisive event-horizon, while the local formula prevents it from becoming vague time in general.\",\"reason\":\"V4 supports ordinary day, open span, and event-day branches; the local collocation with reckoning narrows that elasticity into an eschatological Day.\",\"representative_source_ids\":[\"QS-1c0420fb\",\"QS-5b832c9c\",\"MS-e6c6c81c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:1:authority-time-reckoning-compression","source_type":"word_analysis","support_id":"sup_17b1771aa0e4a29e83b1","text":"{\"blocking_evidence\":null,\"headline\":\"head word launches a descending authority hierarchy\",\"reader_payoff\":\"The reader sees the phrase descend from possessor to time to reckoning system, so the first word carries the whole ayah's ownership frame.\",\"reason\":\"The two forced idafa attachments make a three-term hierarchy, with the first word as the head that governs the temporal domain.\",\"representative_source_ids\":[\"QT-53c67152\",\"MT-64552c0c\",\"MT-8c4414ae\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:3:definite-chain-terminus","source_type":"word_analysis","support_id":"sup_23d201850bbb4c6d14cb","text":"{\"blocking_evidence\":null,\"headline\":\"final definite genitive closes and defines the chain\",\"reader_payoff\":\"The reader notices that the last word both closes the construct chain and sends definiteness back through the earlier words.\",\"reason\":\"The aligned word is definite, genitive, and final muḍāf ilayhi; attachment evidence makes it the terminus of the chain.\",\"representative_source_ids\":[\"QG-0b2217ed\",\"QG-a58e7e5e\",\"QG-c6bc9321\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"1:4:3:2","source_type":"qac_morpheme","support_id":"sup_39de4f6450273056ca0c","text":"{\"lemma_ar\":\"دِين\",\"morph_features\":\"STEM|POS:N|LEM:diyn|ROOT:dyn|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"1:4:3:2\",\"qac_word_ref\":\"1:4:3\",\"root_ar\":\"د ي ن\",\"surface_ar\":\"دِّينِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:3:debt-obligation-image","source_type":"word_analysis","support_id":"sup_4589d16da66ea5b6fe31","text":"{\"blocking_evidence\":null,\"headline\":\"debt-accounting image sharpens abstract judgment\",\"reader_payoff\":\"The reader feels judgment as settlement of what is owed and returned, while the local noun remains the broader reckoning system rather than a merely financial debt.\",\"reason\":\"Debt and credit are accepted root branches, but the local formula and distribution favor the abstract reckoning system over a concrete loan sense.\",\"representative_source_ids\":[\"QS-25a86017\",\"QS-9a9bec61\",\"QI-15615485\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:1:intertext-and-forward-bridge","source_type":"word_analysis","support_id":"sup_459b2375c87d374c5011","text":"{\"blocking_evidence\":null,\"headline\":\"ownership title bridges earlier attributes and later petition\",\"reader_payoff\":\"The reader notices the authority title as a hinge between mercy, the reckoning scene, and the coming direct worship request.\",\"reason\":\"The row evidence links the active possessor title to ownership of dominion (3:26), the petition for guidance (1:6), and direct worship address (1:5), so the bridge survives as inter-ayah payoff.\",\"representative_source_ids\":[\"QI-bb228acc\",\"MI-dd7c81d6\",\"QE-1b081dc4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:2:sound-cadence-binding","source_type":"word_analysis","support_id":"sup_4bc8ad33cd3cfb1a8928","text":"{\"blocking_evidence\":null,\"headline\":\"sound binds the Day to the final reckoning noun\",\"reader_payoff\":\"The reader hears the two final nouns as a bound phrase through nasal closure, glide movement, liaison, and repeated genitive cadence.\",\"reason\":\"The sound rows converge on audible binding between the middle and final terms without changing the local grammar.\",\"representative_source_ids\":[\"QE-6c5359a5\",\"QP-40e56259\",\"QP-56ea13f5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:1:construct-head-definiteness","source_type":"word_analysis","support_id":"sup_4bd53eaa2010b4506441","text":"{\"blocking_evidence\":null,\"headline\":\"construct head governs the Day and receives definiteness\",\"reader_payoff\":\"The reader sees ownership aimed at a specific Day, with definiteness traveling backward through the construct chain rather than through a visible article on the head word.\",\"reason\":\"The local idafa relation makes the first word govern the second, while the final definite term specifies the whole chain.\",\"representative_source_ids\":[\"QG-1f27dc3f\",\"QG-ebeee66f\",\"QF-2f21ba2b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:2","source_type":"word_analysis","support_id":"sup_51cf6e466b7c15530bf3","text":"{\"gloss_range\":\"the specific Day as a possessed temporal unit and eschatological event-horizon; broader day, span, and epoch senses are narrowed by the reckoning construct\",\"prose\":\"{{ar:يَوْمِ}} ({{tr:yawmi}}) is the middle hinge of the chain: governed by the Owner and governing the reckoning term. Its article-less construct form becomes definite through what follows, so the reader receives a named Day rather than an indefinite date. The root can name ordinary days, open spans, and event-days, but here the recurring reckoning formula (51:12; 70:26; 82:17; 82:18; 83:11) narrows that elasticity into the decisive eschatological time. Variant case evidence shows how much depends on the genitive: the Day remains a possessed construct term, not merely an adverbial backdrop. It turns the praise sequence toward direct worship and path outcome (1:5; 1:7), and its sound binds forward so the temporal noun and the reckoning noun land as one audible formula.\",\"root_display\":\"{{ar:ي و م}} ({{tr:y-w-m}})\",\"root_gloss_range\":\"root range centers on day, time-span, event-day, and marked divine occasion; locally it is the stable temporal noun that mediates ownership and reckoning\",\"surface_display\":\"{{ar:يَوْمِ}} ({{tr:yawmi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:3","source_type":"word_analysis","support_id":"sup_5cc9eecb7b90639f6d3d","text":"{\"gloss_range\":\"the known reckoning order that defines the Day; judgment and requital are selected while debt-settlement, obligation, obedience, and submission pressures remain locally relevant\",\"prose\":\"{{ar:ٱلدِّينِ}} ({{tr:ad-dīni}}) is the final genitive term, so it closes the chain and defines the Day that the first word owns. Its definiteness reaches backward through the construct, making the whole phrase point to the known reckoning order. The local formula selects judgment and recompense, but the root pressure keeps debt-settlement, obligation, obedience, and submission in the reader's ear; the Day is not just a verdict date but the settlement of a binding moral order. The final word completes the recurring Day formula (15:35; 26:82; 37:20; 38:78; 51:12; 56:56; 70:26; 74:46; 82:15; 82:17; 82:18; 83:11), while its wider order field can be heard beside upright-order references (9:36; 12:40; 30:30; 98:5) without displacing the local reckoning sense. Because the word is a definite abstract noun, the ayah ends on a named system rather than on a judging verb. Its assimilated article and nasal ending add audible closure to the semantic closure.\",\"root_display\":\"{{ar:د ي ن}} ({{tr:d-y-n}})\",\"root_gloss_range\":\"root range includes obedience, religion, judgment, recompense, debt, obligation, subjugation, and ordered way; the local formula selects reckoning as a binding moral system\",\"surface_display\":\"{{ar:ٱلدِّينِ}} ({{tr:ad-dīni}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:1","source_type":"word_analysis","support_id":"sup_613fd4393bdcab97ac78","text":"{\"gloss_range\":\"standing possessor and disposer over the specific Day of reckoning; qiraat keep kingly sovereignty in view, but the aligned surface foregrounds active ownership in a construct chain\",\"prose\":\"{{ar:مَٰلِكِ}} ({{tr:māliki}}) opens the ayah as a genitive continuation of the prior praise chain, not as a detached title. Its construct shape points forward to the specific Day, while definiteness travels back from the final term through the chain. As a sparse active-participle form in the root's wider field, it presents ownership as a standing divine attribute rather than a future event clause. The accepted reading field keeps kingly sovereignty and intensified possession nearby, but the aligned surface gives the reader a possessor with disposal over time and reckoning. Its rare divine-ownership field places ownership of the Day beside ownership of dominion (3:26), while inside the Fatiha it pivots the opening from mercy into accountability and prepares the direct worship and guidance requests (1:5; 1:6).\",\"root_display\":\"{{ar:م ل ك}} ({{tr:m-l-k}})\",\"root_gloss_range\":\"broad root range includes ownership, disposal, kingship, dominion, cohesion, and other construction-bound branches; the local word selects divine possessive authority over the Day\",\"surface_display\":\"{{ar:مَٰلِكِ}} ({{tr:māliki}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:1:marked-divine-possessor-distribution","source_type":"word_analysis","support_id":"sup_64e74d3a1f4c07c93894","text":"{\"blocking_evidence\":null,\"headline\":\"rare active-possessor form is salient in divine attribute contexts\",\"reader_payoff\":\"The reader notices that a common root is funneled into a sparse active-possessor profile at a liturgical hinge.\",\"reason\":\"The contextual profile marks this exact root-form as low occurrence and tied to divine referent usage, matching the CRITICAL claim of marked form choice.\",\"representative_source_ids\":[\"QI-0fdcea26\",\"QH-d3d6b189\",\"MH-4f575afe\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:2:middle-idafa-hinge","source_type":"word_analysis","support_id":"sup_6de496dddc7dfca67bc2","text":"{\"blocking_evidence\":null,\"headline\":\"middle noun is governed and governing\",\"reader_payoff\":\"The reader notices the word as the hinge that receives ownership from the head and passes definition onward to reckoning.\",\"reason\":\"Attachment evidence marks the word as genitive complement of the first word and construct head over the final word.\",\"representative_source_ids\":[\"QG-fce60c74\",\"MG-c3db2bb6\",\"QT-4f4cdfcf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:2:definite-named-day","source_type":"word_analysis","support_id":"sup_71e70fb8c4d8f3b6fd87","text":"{\"blocking_evidence\":null,\"headline\":\"bare construct noun becomes a definite named temporal unit\",\"reader_payoff\":\"The reader sees an article-less word become a specific known Day through annexation, not an indefinite date.\",\"reason\":\"The construct chain licenses definiteness through the following definite term while preserving the singular temporal unit.\",\"representative_source_ids\":[\"QG-568d467b\",\"MG-4c19c57b\",\"QF-31529026\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:2:scene-and-forward-pressure","source_type":"word_analysis","support_id":"sup_76cc63a82aa9c81cef1e","text":"{\"blocking_evidence\":null,\"headline\":\"temporal frame turns praise toward petition\",\"reader_payoff\":\"The reader sees the attribute sequence enter an accountability scene before the later worship and path language arrives.\",\"reason\":\"The topic survives because the word creates the temporal frame for reckoning before the direct worship declaration (1:5) and path outcome (1:7).\",\"representative_source_ids\":[\"QT-4323f488\",\"QE-b03c5109\",\"QB-7af795ed\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:2:qiraat-adverbial-contrast","source_type":"word_analysis","support_id":"sup_7b30429bf1ce383d9449","text":"{\"blocking_evidence\":null,\"headline\":\"case variants show how the canonical genitive keeps the chain intact\",\"reader_payoff\":\"The reader notices that genitive case makes the Day a possessed construct term, while accusative variants would turn it toward an adverbial time setting.\",\"reason\":\"Variant evidence is retained as contrast, but the aligned grammar keeps the word inside the idafa chain.\",\"representative_source_ids\":[\"QG-0da7e57a\",\"QF-4dce11f7\",\"MT-f151455a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:3:nominal-system-not-event-verb","source_type":"word_analysis","support_id":"sup_807fe6a67fa2a2d47348","text":"{\"blocking_evidence\":null,\"headline\":\"definite abstract noun names a system rather than narrating an action\",\"reader_payoff\":\"The reader notices that the ayah ends on a named order of requital, not on a narrated act of judging.\",\"reason\":\"QAC marks a definite singular abstract noun, and the contextual profile supports a strongly nominal deployment for this root-form.\",\"representative_source_ids\":[\"QF-2ce11b98\",\"QF-4b9a9dc9\",\"QH-ff141c93\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:1:ownership-disposal-root-pressure","source_type":"word_analysis","support_id":"sup_819f8345fb1c0289c479","text":"{\"blocking_evidence\":null,\"headline\":\"ownership carries disposal force without importing every root branch\",\"reader_payoff\":\"The reader feels ownership as command and disposal over the Day, not merely a thin legal title, while unrelated root branches remain outside the local sense.\",\"reason\":\"V4 supports ownership and dominion branches for the root, but local grammar selects the possessor relation over the Day rather than branches such as marriage, road-center, or angel derivation.\",\"representative_source_ids\":[\"QS-5a6654d9\",\"QS-8bad9ded\",\"MS-4cf25e2b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:2:formulaic-day-of-reckoning","source_type":"word_analysis","support_id":"sup_8c112abe26320d4b702e","text":"{\"blocking_evidence\":null,\"headline\":\"recurring reckoning formula is activated by the middle word\",\"reader_payoff\":\"The reader recognizes that the middle word is not a neutral date marker but the entry into a recurring eschatological formula.\",\"reason\":\"The row evidence gives recurring formula references (51:12, 70:26, 82:17, 82:18, 83:11), and V4 includes the day-of-reckoning collocation under the reckoning branch.\",\"representative_source_ids\":[\"QI-e44b1309\",\"QI-f9bf0193\",\"MI-27647015\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"1:4:2:1","source_type":"qac_morpheme","support_id":"sup_9689a9db629abd007935","text":"{\"lemma_ar\":\"يَوْم\",\"morph_features\":\"STEM|POS:N|LEM:yawom|ROOT:ywm|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"1:4:2:1\",\"qac_word_ref\":\"1:4:2\",\"root_ar\":\"ي و م\",\"surface_ar\":\"يَوْمِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:1:genitive-apposition-chain","source_type":"word_analysis","support_id":"sup_973e971167e834110985","text":"{\"blocking_evidence\":null,\"headline\":\"genitive apposition continues the praise chain\",\"reader_payoff\":\"The reader notices that the ayah is not syntactically isolated; the genitive head continues the divine-description chain already underway.\",\"reason\":\"QAC marks the word as genitive apposition to the earlier divine referent, and attachment support warns against detaching this ayah from the preceding attribute sequence.\",\"representative_source_ids\":[\"QG-1150182b\",\"QG-b8d8615e\",\"QG-cb711a9f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:3:marked-ownership-over-reckoning","source_type":"word_analysis","support_id":"sup_a72e773b70cd46efe06b","text":"{\"blocking_evidence\":null,\"headline\":\"ordinary Day formula is drawn under ownership language\",\"reader_payoff\":\"The reader sees the familiar reckoning formula placed under ownership, so the phrase is not just a Day formula but a sovereignty claim over that formula.\",\"reason\":\"The d-y-n and y-w-m pairing is formulaically strong, while the m-l-k pairing is marked; 1:4 draws the formula under the head noun's authority.\",\"representative_source_ids\":[\"QI-50e41ab0\",\"QI-fa2e024e\",\"QT-c578841f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:3:sound-definiteness-and-rhyme","source_type":"word_analysis","support_id":"sup_af40b71ee4e9ff0f1d18","text":"{\"blocking_evidence\":null,\"headline\":\"assimilation, doubled onset, and nasal rhyme weight the final noun\",\"reader_payoff\":\"The reader hears definiteness, pressure, and closure arrive together in the final noun's assimilated onset and nasal ending.\",\"reason\":\"The sound rows preserve a perceptual payoff around article assimilation, doubled onset, genitive cadence, and adjacent Fatiha ending rhyme.\",\"representative_source_ids\":[\"QF-a9d496ef\",\"QP-1999de86\",\"QP-0437717d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:1:qiraat-authority-range","source_type":"word_analysis","support_id":"sup_b4185d17d054e7ca7628","text":"{\"blocking_evidence\":null,\"headline\":\"variant readings expose owner, king, and intensified authority\",\"reader_payoff\":\"The reader notices that the transmitted reading field presses authority through both proprietary disposal and royal sovereignty, while the local canonical surface keeps the active-possessor form primary.\",\"reason\":\"Accepted variant evidence is useful for the authority range, but it clarifies rather than replaces the aligned active-participle surface.\",\"representative_source_ids\":[\"QS-9b482ae8\",\"QS-de8d4f90\",\"QF-3e274e60\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:3:generative-parse-layering","source_type":"word_analysis","support_id":"sup_c82c2ec94ed066047591","text":"{\"blocking_evidence\":null,\"headline\":\"parse and qiraat alternatives layer belonging and characterization\",\"reader_payoff\":\"The reader notices that the final noun can define the Day semantically even while grammar marks it as governed, creating productive layering in the chain.\",\"reason\":\"The local genitive parse is fixed by attachment evidence, but the CRITICAL rows preserve the semantic backflow by which the final term characterizes the Day.\",\"representative_source_ids\":[\"QS-feba4ec9\",\"QY-1c6ec582\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:1:standing-possessor-not-event","source_type":"word_analysis","support_id":"sup_ed8e8d5c6ff316dd8d8a","text":"{\"blocking_evidence\":null,\"headline\":\"active participle presents standing ownership\",\"reader_payoff\":\"The reader notices that ownership is presented as an already-standing attribute, not as a future event that begins on the Day.\",\"reason\":\"The aligned form is an active participle inside a verbless nominal chain, not a finite verb clause.\",\"representative_source_ids\":[\"MG-0b185676\",\"QF-7b3823b7\",\"QT-43cc534d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:3:closure-scene-architecture","source_type":"word_analysis","support_id":"sup_fa7492dd0f3b6cc0fcd0","text":"{\"blocking_evidence\":null,\"headline\":\"final term supplies the scene's governing content\",\"reader_payoff\":\"The reader sees the ayah resolve from authority and time into the system that gives the Day its content.\",\"reason\":\"The final governed term completes the hierarchy: authority, temporal frame, and the reckoning order that defines the frame.\",\"representative_source_ids\":[\"QT-39f5b896\",\"QT-aa729ec7\",\"MT-591be38d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"1:4:1:1","source_type":"qac_morpheme","support_id":"sup_fd8b5adbbedbb1e0027b","text":"{\"lemma_ar\":\"مَٰلِك\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|LEM:ma`lik|ROOT:mlk|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"1:4:1:1\",\"qac_word_ref\":\"1:4:1\",\"root_ar\":\"م ل ك\",\"surface_ar\":\"مَٰلِكِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:1:sound-and-orthographic-pressure","source_type":"word_analysis","support_id":"sup_fee32f29cb2a0b8b041d","text":"{\"blocking_evidence\":null,\"headline\":\"vowel length and sound contour make the head word perceptible\",\"reader_payoff\":\"The reader hears and sees the long-vowel ownership reading before the chain narrows into the following genitives.\",\"reason\":\"The sound and orthographic rows support a perceptual payoff around vowel length, imala and madd coloring, and the narrowing closure of the head word.\",\"representative_source_ids\":[\"QF-d08dfd86\",\"QP-9a6fc590\",\"QP-c390e310\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"1:4:2:morphologically-stable-time-noun","source_type":"word_analysis","support_id":"sup_ff4ec64a41acd87c78f8","text":"{\"blocking_evidence\":null,\"headline\":\"frequent root remains locked to temporal noun use\",\"reader_payoff\":\"The reader notices that a very frequent root contributes a stable time noun here, not an action or derived agency.\",\"reason\":\"The contextual profile shows high frequency for this exact noun form and no local verb frame, supporting the CRITICAL claim of temporal noun stability.\",\"representative_source_ids\":[\"QF-82183011\",\"QI-bad9f2ce\",\"ME-8fb9e869\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"مَٰلِكِ يَوْمِ ٱلدِّينِ","ayah_ref":"1:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000504/B002","root_001444/B003","root_001700/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001444","role":"Kingship and public dominion supply the governing authority exercised in the event.","root":"م ل ك","source_ref":"1:4","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001700","role":"A severe event-day turns time from a calendar label into the occasion on which authority becomes manifest.","root":"ي و م","source_ref":"1:4","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000504","role":"Reckoning and recompense specify what the sovereign event does.","root":"د ي ن","source_ref":"1:4","source_word_indices":["3"]}],"changed_reading":{"after":"The phrase stages a sovereign public event in which authority becomes operative as reckoning and recompense.","before":"The phrase merely assigns ownership of a future date."},"confidence":"strong","focus_anchor":"The full genitive chain, with مَٰلِكِ governing يَوْمِ and ٱلدِّينِ specifying the event.","mechanism":"Kingship becomes executable in a marked event: the severe-event branch of day concentrates sovereignty into an occasion when reckoning and recompense are carried out.","model_id":"b_sovereign_reckoning_event"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_sovereign_reckoning_event","source_type":"hft","support_id":"sup_5e5a60a15581f02f2ebd","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"مَٰلِكِ يَوْمِ ٱلدِّينِ","ayah_ref":"1:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000504/B003","root_001444/B002","root_001700/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001444","role":"Ownership and disposal make the focus figure the holder of the claim and its settlement.","root":"م ل ك","source_ref":"1:4","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001700","role":"An open span of time supplies the interval through which a deferred obligation matures.","root":"ي و م","source_ref":"1:4","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000504","role":"Debt and credit make the final relation one of liability coming due.","root":"د ي ن","source_ref":"1:4","source_word_indices":["3"]}],"changed_reading":{"after":"The focus can depict the holder of every deferred liability and of the very interval in which it comes due.","before":"Dīn is only a religious label or a judicial verdict."},"confidence":"medium","focus_anchor":"مَٰلِكِ as holder with power of disposal, joined to the temporal and financial branches of يَوْمِ ٱلدِّينِ.","mechanism":"Ownership, an open span of time, and deferred debt form a maturity mechanism: the owner controls both the liability and the interval at whose end it is settled.","model_id":"b_debt_maturity"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_debt_maturity","source_type":"hft","support_id":"sup_9076b32659455b9ab4a1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"مَٰلِكِ يَوْمِ ٱلدِّينِ","ayah_ref":"1:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000504/B001","root_001444/B003","root_001700/B002"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001444","role":"Dominion supplies the authority that orders a lived regime.","root":"م ل ك","source_ref":"1:4","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001700","role":"A span of time allows dīn to organize an age or duration, not just one daylight period.","root":"ي و م","source_ref":"1:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000504","role":"Obedience, worship, and followed law provide the regime's recurring practice.","root":"د ي ن","source_ref":"1:4","source_word_indices":["3"]}],"changed_reading":{"after":"It can also name sovereignty over every duration constituted by worship, allegiance, and followed law.","before":"The phrase concerns only authority exercised after present life."},"confidence":"medium","focus_anchor":"The sovereignty of مَٰلِكِ, the durative possibility of يَوْمِ, and the obedience branch of ٱلدِّينِ.","mechanism":"Sovereignty extends across a duration organized by obedience, worship, and law; the phrase can name an enacted regime rather than only a terminal courtroom.","model_id":"b_obedience_regime"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_obedience_regime","source_type":"hft","support_id":"sup_ec98c3825f872a39c0a9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"مَٰلِكِ يَوْمِ ٱلدِّينِ","ayah_ref":"1:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000504/B005","root_000504/B006","root_001444/B001","root_001444/B005","root_001700/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001444","role":"Strength and cohesion supply the material image of an order being held together.","root":"م ل ك","source_ref":"1:4","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_001444","role":"The mainstay of a matter turns ownership into structural support.","root":"م ل ك","source_ref":"1:4","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001700","role":"An open temporal span is the duration across which the order persists.","root":"ي و م","source_ref":"1:4","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_000504","role":"Habit and customary state make dīn the repeated order being sustained.","root":"د ي ن","source_ref":"1:4","source_word_indices":["3"]},{"branch_id":"B006","mapped_root_id":"root_000504","role":"The city of ordered authority gives the customary order a civic and institutional form.","root":"د ي ن","source_ref":"1:4","source_word_indices":["3"]}],"changed_reading":{"after":"Mālik can be the mainstay that keeps a temporal, customary, and civic order coherent.","before":"Mālik is only an external ruler over an event."},"confidence":"exploratory","focus_anchor":"مَٰلِكِ through its cohesion and mainstay branches, with يَوْمِ as duration and ٱلدِّينِ as customary or civic order.","mechanism":"The owner is read systemically as what holds an order together; time is the field, and dīn is the repeated custom or organized authority sustained within it.","model_id":"b_mainstay_of_customary_order"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_mainstay_of_customary_order","source_type":"hft","support_id":"sup_247e039079f06dc5170b","trust":"legacy_unbound"}]}
</lane_packet_json>
