# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **87:17**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s087-regular-20260911/s087/87_17/micro.discovery.json` and modify nothing
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
  "ayah_ref": "87:17",
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
{"analysis_context":{"analysis_id":"s087-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"87:17","host_surah":87,"lane_context_refs":[],"ordered_context_refs":["87:0","87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:18","87:19","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, erteleme eylemini, bir nesnenin arka bölümünü ve ölümden sonraki dünyaya özgü yerleşik kullanımı kendi başına kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000019/B001","candidate_links":[{"candidate_id":"cand_943aa477973aad770107","lane":"micro"},{"candidate_id":"cand_6349af299a067939a02c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"آخِر","morph_features":"STEM|POS:N|LEM:A^xir|ROOT:Axr|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:1:3","qac_word_ref":"87:17:1","surface_ar":"ءَاخِرَةُ"}],"gloss":"sonraki ya da öteki olan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir öğe, ilk olandan sonra gelmesi veya ilk ya da tek olmayıp başka olması bakımından nitelenir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı karşıtlık, uzakta bulunan ya da ortada bulunmayan bir öğeyi göstermeye genişleyebilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bağlamlarda bir topluluğun son kesimi veya ardından hiçbir şey gelmeyen nihai varlık anlatılır."}}],"root_ar":"ء خ ر","root_id":"root_000019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İlkten sonra gelme ile ilk veya tek olmayıp başka olma çekirdeğini birlikte anlatan genel karşılıktır.","boundary_detail":"Dal, erteleme eylemini, bir nesnenin arka bölümünü ve ölümden sonraki dünyaya özgü yerleşik kullanımı kendi başına kapsamaz.","branch_image_ar":"الآخرية بعد الأول أو غيره","concept_gloss":"sonraki ya da öteki olan","contextual_glosses":[{"applicability":"Bir dizinin veya topluluğun en sonundaki öğe özellikle kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalnızca başka veya ilk olmayan öğe anlamını ve uzaklık kullanımını dışarıda bırakır.","preserves":"Sıralama içindeki sonralık ve nihai konum anlamını korur."},"facet_ids":["F003"],"text":"sonuncu","usage_role":"contextual"},{"applicability":"İki ya da daha çok öğeden ilk veya anılan olmayan başka öğe kastedildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Zorunlu bir zaman veya sıra sonralığı bildirmez.","preserves":"İlk ya da tek olmayıp başka olma ayrımını korur."},"facet_ids":["F001"],"text":"öteki","usage_role":"contextual"},{"applicability":"Sözün özellikle mesafedeki veya ortamda bulunmayan kişiye yöneldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel sonraki ve öteki olma anlamlarını tek başına karşılamaz.","preserves":"Merkezden ayrılmış veya mevcut olmayan öğe uzantısını açıklar."},"facet_ids":["F002"],"text":"uzaktaki ya da bulunmayan","usage_role":"explanatory"}],"definition":"Bir dizide ilk olandan sonra gelen veya iki ya da daha çok öğe içinde ilk ya da tek olmayıp başka olandır. Bağlama göre bir topluluğun son kesimini, uzakta ya da bulunmayanı ve ardından hiçbir şey gelmeyen son varlığı da gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir öğe, ilk olandan sonra gelmesi veya ilk ya da tek olmayıp başka olması bakımından nitelenir."},{"facet_id":"F002","role":"extension","statement":"Aynı karşıtlık, uzakta bulunan ya da ortada bulunmayan bir öğeyi göstermeye genişleyebilir."},{"facet_id":"F003","role":"specialization","statement":"Belirli bağlamlarda bir topluluğun son kesimi veya ardından hiçbir şey gelmeyen nihai varlık anlatılır."}],"identity_rationale":"Kaynak ifadesi, ilk olandan sonra gelme ile ilk ya da tek olmayıp başka olma anlamlarını açıkça bir arada verir. Grup sonlarında bulunma, uzakta veya bulunmuyor olma ve ardından hiçbir şey gelmeme kullanımları bu çekirdeğin bağlama bağlı özelleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sonraki; öteki"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sonraki veya öteki olan dişil öğe"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"başkaları; ötekiler"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"insanların son kesimleri"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"zamanın sonu"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"ardından hiçbir şey gelmeyen son"}],"lexicalization_note":"Tanım ortak sonraki ya da öteki olma çekirdeğini korur; grup sonu ve zamanın sonu gibi söz öbeklerine bağlı kullanımları bütün dalın zorunlu anlamı saymaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; sıra sonralığı, gecikme ve somut arka bölümle en açıklayıcı sınırları kuran üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı, sıralama ilişkisinin yanında ilk ya da tek olmayıp başka olmayı da sözlükleştirir; komşu dal ise önce-sonra ilişkisini daha doğrudan kurar.","focus_only":"İlk olmayan öteki öğeyi, grup sonunu ve bazı bağlamlarda uzakta ya da bulunmayanı da gösterebilir.","gloss":"sonra gelen","neighbor_only":"Bir olayın veya öğenin öncekinden sonra gerçekleştiğini doğrudan kuran ilişkisel kullanımları kapsar.","neighbor_ref":"root_000131/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir öğeyi önce gelen bir öğeye göre daha sonraki konumda gösterebilir."},{"boundary_match":"partial","distinction":"Odak dalı öğenin konumunu ya da kimliğini niteler; komşu dal ise zamanlamayı değiştiren eylemi veya bunun sonucundaki gecikme durumunu anlatır.","focus_only":"Bir öğenin sıralamadaki sonraki veya ilk olmayıp başka olan kimliğini bildirir.","gloss":"sonralık ile gecikme","neighbor_only":"Bir şeyi daha sonraki zamana bırakma veya bir öznenin geç kalması sürecini bildirir.","neighbor_ref":"root_000019/B002","relation_type":"near_neighbor","shared_zone":"İki dal da daha sonra olma fikrini taşır ve zaman sıralamasında kesişebilir."},{"boundary_match":"partial","distinction":"Odak dalında temel eksen sıra ve başkalıktır; komşu dalda temel eksen nesnenin ön ve arka bölümleri arasındaki uzamsal karşıtlıktır.","focus_only":"Sıra içinde ilkten sonra gelen veya ilk olmayan başka öğeyi gösterir.","gloss":"sonraki ile arka","neighbor_only":"Bir nesnenin önüyle karşıtlanan somut arka bölümünü gösterir.","neighbor_ref":"root_000019/B003","relation_type":"near_neighbor","shared_zone":"Sıralamadaki son konum, uzamsal bir nesnenin arka konumuyla örtüşebilir."}],"source_phrase_ar":"الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)","source_summary":"Kanıtlar, ilk ile karşıtlık kuran sonraki öğeyi ve birden çok öğe arasında ilk olmayan öteki öğeyi ortak çekirdek olarak gösterir; son kesim, uzaklık ve nihailik kullanımları bu çekirdeğe bağlanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الآخر والأخرى وأخر وأواخر وأخريات الناس، وما كان بعد الأول أو غير الأول، ويدخل فيه الأبعد أو الغائب عند التصريح به.","what_is_not_ar":"لا يدخل فيه فعل التأخير والإمهال نفسه، ولا مؤخر الأجسام، ولا اصطلاح الدار الآخرة إلا بقرينة خاصة."},"support_links":["sup_1fd91e24ee29a5f37fb2","sup_494adb4b482277e4a4a1"]},{"boundary":"Dal, yalnızca sonraki veya öteki olanı adlandırmaz ve somut bir nesnenin arka tarafını zaman gecikmesi bulunmadıkça kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000019/B002","candidate_links":[{"candidate_id":"cand_d04c778a5e6e0ee28341","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"آخِر","morph_features":"STEM|POS:N|LEM:A^xir|ROOT:Axr|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:1:3","qac_word_ref":"87:17:1","surface_ar":"ءَاخِرَةُ"}],"gloss":"geciktirme veya gecikme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir olay veya öğe daha sonraki zamana bırakılır ya da bir özne zaman veya sıra bakımından geride kalır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Satış bağlamında ödeme vadesinin ileri bir tarihe bırakılması anlatılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Zaman belirten kullanımda birini ancak geç bir dönemde tanıma veya birinin geç gelmesi anlatılır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Ürünü hasat döneminin sonuna kadar üzerinde kalan bir hurma ağacı, gecikmiş kalışın somut örneğidir."}}],"root_ar":"ء خ ر","root_id":"root_000019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem bir şeyi daha sonraya bırakmayı hem de öznenin daha sonraya kalmasını kapsayan genel karşılıktır.","boundary_detail":"Dal, yalnızca sonraki veya öteki olanı adlandırmaz ve somut bir nesnenin arka tarafını zaman gecikmesi bulunmadıkça kapsamaz.","branch_image_ar":"التأخير إلى وقت لاحق","concept_gloss":"geciktirme veya gecikme","contextual_glosses":[{"applicability":"Bir işi, olayı veya vadeyi bilinçli biçimde daha sonraki zamana bırakma bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öznenin kendisinin gecikmesi ve ürünün geç zamana kalması kullanımlarını karşılamaz.","preserves":"Bir şeyi sonraki zamana bırakma işlemini korur."},"facet_ids":["F001"],"text":"ertelemek","usage_role":"contextual"},{"applicability":"Bedelin veya ödeme tarihinin ileri bırakıldığı satış söz öbeğine özgü karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Satış dışındaki genel geciktirme ve gecikme alanını dışarıda bırakır.","preserves":"Satışta vadenin ileri alınması anlamını eksiksiz korur."},"facet_ids":["F002"],"text":"vadeli satmak","usage_role":"contextual"},{"applicability":"Bir tanıma veya gelme olayının geç bir zamanda gerçekleştiğini belirten kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geciktirme eylemini ve vadeli satış anlamını karşılamaz.","preserves":"Olayın beklenen veya önceki zamandan daha geç gerçekleşmesini korur."},"facet_ids":["F003"],"text":"geç vakitte","usage_role":"contextual"}],"definition":"Bir şeyi olağan, belirlenmiş veya başka bir şeye göre daha sonraki bir zamana bırakmak ya da bir öznenin bu biçimde geride kalmasıdır. Vadeyi ileri alma ve bir ürünün hasadın sonuna kadar kalması bunun bağlama bağlı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir olay veya öğe daha sonraki zamana bırakılır ya da bir özne zaman veya sıra bakımından geride kalır."},{"facet_id":"F002","role":"specialization","statement":"Satış bağlamında ödeme vadesinin ileri bir tarihe bırakılması anlatılır."},{"facet_id":"F003","role":"associated_use","statement":"Zaman belirten kullanımda birini ancak geç bir dönemde tanıma veya birinin geç gelmesi anlatılır."},{"facet_id":"F004","role":"example","statement":"Ürünü hasat döneminin sonuna kadar üzerinde kalan bir hurma ağacı, gecikmiş kalışın somut örneğidir."}],"identity_rationale":"Kaynak ifadesi bir şeyi daha sonraya bırakma, bir öznenin geride kalması, vadeli satış ve ürününü hasadın sonuna dek taşıyan hurma örneklerini aynı zaman sonralığı çevresinde toplar. Geçişlilik ve bağlama bağlı örnekler korunarak dal kimliği tutarlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"geciktirme"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"geciktirmek; sonraya bırakmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"gecikmek; geride kalmak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"geç vakitte; sonradan"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"vadeli satmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ürünü hasadın sonuna kadar kalan hurma ağacı"}],"lexicalization_note":"Tanım geciktirme ve gecikme çekirdeğini verir; vadeli satış ile ürünü geç zamana kalan hurma anlamlarını kendi söz öbekleri ve biçimleriyle sınırlı tutar.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; erteleme, süre tanıma ve yavaşlıkla en yararlı sınırları kuran üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu, erteleme eylemine daha sıkı bağlıdır; odak dalı ise eylemin yanı sıra gecikmiş durumu, geç zaman belirtecini ve özel adlandırmaları da kapsayan daha geniş bir türeme alanına sahiptir.","focus_only":"Gecikmek, geç vakitte olmak, vadeli satış ve ürünü geç hasada kalan ağaç kullanımlarını da kapsar.","gloss":"ertelemek","neighbor_only":"Belirli bir şeyi sonraki zamana bırakmanın yanında bu işlemle bağlantılı yerleşik topluluk adlandırmasını da içerir.","neighbor_ref":"root_000548/B004","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde bir şeyi daha sonraki bir zamana bırakma işlemi bulunur."},{"boundary_match":"partial","distinction":"Odak dalı zaman sırasındaki gecikmeye dayanır; komşu dal ise bekleyen katılımcı ve ona tanınan süre ilişkisini ayrıca kurar.","focus_only":"Bir olayın ya da öznenin daha sonraya kalmasını, bekleyen bir kişi bulunmaksızın da anlatabilir.","gloss":"geciktirme ile süre tanıma","neighbor_only":"Bir talep sahibine süre tanımayı, beklemeyi ve beklenen bir iyiliği ummayı da içerir.","neighbor_ref":"root_001520/B002","relation_type":"near_neighbor","shared_zone":"Bir borcun veya işin hemen sonuçlandırılmayıp ileri zamana bırakılmasında iki dal kesişir."},{"boundary_match":"partial","distinction":"Odak dalında belirleyici ölçüt daha sonraki zaman veya sıra konumudur; komşu dalda belirleyici ölçüt hareket ya da yürütme hızının düşüklüğüdür.","focus_only":"Bir şeyi bilinçli olarak sonraya bırakmayı ve vadeyi ileri almayı kapsar.","gloss":"gecikme ile yavaşlık","neighbor_only":"Hareketin veya iş görmenin düşük hızını, sonuçta geç kalma olmasa bile anlatabilir.","neighbor_ref":"root_000124/B001","relation_type":"near_neighbor","shared_zone":"Yavaş ilerleyen bir kişi veya süreç, beklenen zamana göre gecikmiş de olabilir."}],"source_phrase_ar":"تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)","source_summary":"Kanıtlar, öne almanın karşıtı olarak daha sonraya bırakmayı ve geride kalmayı ortaklaştırır; vadeli satış, geç zamanda gerçekleşme ve ürünü hasadın sonuna kalan ağaç bu yapının özel kullanımlarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أخرته وتأخر واستأخر والمستأخر، وبيع بأخرة أو بنظرة، وما يبقى إلى آخر الشيء كالمئخار.","what_is_not_ar":"لا يدخل فيه مجرد معنى الآخر بمعنى غير الأول، ولا الجهة الخلفية من الجسم إلا إذا دل السياق على التأخير الزمني."},"support_links":["sup_4f5cd9b273d716085f0d"]},{"boundary":"Dalın ekseni uzamsal ön-arka karşıtlığıdır; zaman bakımından gecikme, genel ötekilik ve ölümden sonraki dünya anlamları dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000019/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"آخِر","morph_features":"STEM|POS:N|LEM:A^xir|ROOT:Axr|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:1:3","qac_word_ref":"87:17:1","surface_ar":"ءَاخِرَةُ"}],"gloss":"arka bölüm","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesnenin önüyle karşıtlanan arka bölümü ya da arka tarafı gösterilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gözde şakağa yakın arka köşe ve binek semerinde binicinin yaslandığı arka dayanak adlandırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir nesneyi arka tarafından yarmak, arka bölüm adının ilgeçli bir yapıda kullanılmasına dayanır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Dişi devenin öndeki iki yanıyla karşıtlanan iki arka yanı özel bir çoğul biçimle gösterilir."}}],"root_ar":"ء خ ر","root_id":"root_000019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin önüyle karşıtlanan somut arka kısmını gösteren en kısa genel karşılıktır.","boundary_detail":"Dalın ekseni uzamsal ön-arka karşıtlığıdır; zaman bakımından gecikme, genel ötekilik ve ölümden sonraki dünya anlamları dışarıda kalır.","branch_image_ar":"المؤخر والخلف","concept_gloss":"arka bölüm","contextual_glosses":[{"applicability":"Belirli bir organ veya araç parçası adı gerekmeyen genel uzamsal bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önle karşıtlanan arka yönü veya bölümü doğal biçimde karşılar."},"facet_ids":["F001"],"text":"arka taraf","usage_role":"general"},{"applicability":"Binek semerinde binicinin yaslandığı arka parça özellikle kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel arka bölüm ile göz ve hayvan anatomisine ilişkin kullanımları dışarıda bırakır.","preserves":"Semerin arka konumunu ve yaslanma işlevini korur."},"facet_ids":["F002"],"text":"arka dayanak","usage_role":"contextual"},{"applicability":"Bir nesnenin arka tarafından kesilmesi veya yarılması anlatılırken doğal akış karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Arka bölümün bağımsız ad olarak kullanılmasını ve özel parça adlarını karşılamaz.","preserves":"İşlemin nesnenin arka bölümünden başlamasını korur."},"facet_ids":["F003"],"text":"arkasından","usage_role":"contextual"}],"definition":"Bir nesnenin ön bölümüyle karşıtlanan arka bölümü veya arka tarafıdır. Gözün şakağa yakın köşesi, semerin arka dayanağı ve hayvanın arka yanları gibi belirli yapılarda özelleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesnenin önüyle karşıtlanan arka bölümü ya da arka tarafı gösterilir."},{"facet_id":"F002","role":"specialization","statement":"Gözde şakağa yakın arka köşe ve binek semerinde binicinin yaslandığı arka dayanak adlandırılır."},{"facet_id":"F003","role":"associated_use","statement":"Bir nesneyi arka tarafından yarmak, arka bölüm adının ilgeçli bir yapıda kullanılmasına dayanır."},{"facet_id":"F004","role":"specialization","statement":"Dişi devenin öndeki iki yanıyla karşıtlanan iki arka yanı özel bir çoğul biçimle gösterilir."}],"identity_rationale":"Kaynak ifadesi nesnenin önüyle karşıtlanan arka bölümünü ortak çekirdek yapar ve bunu göz, semer, kumaş ve dişi devenin arka kısımlarıyla örnekler. Zamansal gecikme veya yalnızca ilkten sonra gelme bu somut bölüm anlamının yerine geçmez.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"nesnenin arka bölümü"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"gözün şakağa yakın arka köşesi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"binek semerinin arka dayanağı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"semerin arka dayanağı için seyrek ve tartışmalı söyleyiş"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"arka tarafından; arkasından"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"dişi devenin iki arka yanı"}],"lexicalization_note":"Tanım ortak arka bölüm çekirdeğini verir; gözün köşesi, semerin dayanağı, kumaşı arkadan yarma ve devenin arka yanları gibi kullanımları kendi yapılarıyla sınırlı tutar.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; genel arkada bulunma, kuyruk ve sıra sonralığıyla temel karışma noktalarını açıklayan üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı çoğunlukla nesnenin kendi arka bölümünü adlandırır; komşu dal ise başka bir şeye göre arkada veya geride bulunma ilişkisini de kurar.","focus_only":"Göz köşesi, semer dayanağı ve devenin arka yanları gibi nesnenin yapısal parçalarını adlandırır.","gloss":"arka bölüm ile arkada","neighbor_only":"Bir şeyin arkasında bulunma yön ve konum ilişkisini, ayrı bir yapısal parça olmadan da anlatır.","neighbor_ref":"root_000433/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da önün karşısındaki uzamsal alanı ve nesnenin arka tarafını gösterebilir."},{"boundary_match":"field_only","distinction":"Odak dalı konumsal ön-arka karşıtlığıyla belirlenir; komşu dal ise kuyruk anatomisi, biçimi veya bir şeyin sonuna eklenme benzerliğiyle belirlenir.","focus_only":"Önle karşıtlanan herhangi bir arka bölümü, kuyruk biçimi veya işlevi olmadan da kapsar.","gloss":"arka bölüm ile kuyruk","neighbor_only":"Hayvan kuyruğunu ve kuyruk gibi uzayan, sarkan ya da bir şeyin sonuna eklenen bölümü kapsar.","neighbor_ref":"root_000521/B002","relation_type":"same_field","shared_zone":"Bir hayvanın kuyruğu arka bölgede bulunduğundan iki dal aynı beden ve nesne bölümleri alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dalının ekseni uzamsal nesne bölümüdür; komşu dalın ekseni sıra sonralığı veya başkalıktır.","focus_only":"Bir nesnenin somut arka kısmını ön kısmıyla karşıtlık içinde adlandırır.","gloss":"arka ile sonraki","neighbor_only":"Bir sıra içinde sonraki veya ilk olmayıp başka olan öğeyi somut bölüm gerektirmeden gösterir.","neighbor_ref":"root_000019/B001","relation_type":"near_neighbor","shared_zone":"Bir dizinin sonundaki öğe, uzamsal olarak arka tarafta da bulunabilir."}],"source_phrase_ar":"آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)","source_summary":"Kanıtlar, ön bölümün karşıtı olan arka bölümü ortaklaştırır; gözün arka köşesi, semerin arka dayanağı, arkadan yarma ve devenin arka yanları bu uzamsal çekirdeği farklı yapılarda gerçekleştirir. Semerin arka dayanağını adlandıran seyrek biçim konusunda bir aktarım biçimi reddederken diğeri kullanımı Esmaî'ye bağlar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه مؤخر الشيء ومقدمه، ومؤخر العين ومقدمها، وآخرة الرحل أو مؤخرته، وشق الشيء من أخره، وآخرا الناقة عند التصريح.","what_is_not_ar":"لا يدخل فيه التأخير الزمني، ولا الآخر بمعنى غير الأول، ولا الآخرة الدينية."},"support_links":[]},{"boundary":"Dal yalnızca ölümden sonraki ikinci yaşam düzenini ve onun dünyasını kapsar; genel sonralık ve geciktirme anlamları ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000019/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"آخِر","morph_features":"STEM|POS:N|LEM:A^xir|ROOT:Axr|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:1:3","qac_word_ref":"87:17:1","surface_ar":"ءَاخِرَةُ"}],"gloss":"ölümden sonraki yaşam ve öteki dünya","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dünya yaşamından sonra gelen ikinci varoluş düzeni anlatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu ikinci varoluş, içinde bulunulan dünyaya karşıt bir yurt olarak adlandırılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yurt adı söylenmeden kullanılan biçim, bağlam içinde ikinci yaşam yurdunu tek başına temsil eder."}}],"root_ar":"ء خ ر","root_id":"root_000019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İkinci varoluş düzenini ve onun yurdunu birlikte karşılayan açıklayıcı genel ifadedir.","boundary_detail":"Dal yalnızca ölümden sonraki ikinci yaşam düzenini ve onun dünyasını kapsar; genel sonralık ve geciktirme anlamları ayrı tutulur.","branch_image_ar":"الدار الآخرة","concept_gloss":"ölümden sonraki yaşam ve öteki dünya","contextual_glosses":[{"applicability":"Kavramın bir varoluş evresi veya yaşam düzeni olarak öne çıktığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu varoluşun ayrı bir yurt olarak kavranmasını açıkça belirtmez.","preserves":"Dünya yaşamından sonra gelen ikinci varoluş evresini korur."},"facet_ids":["F001"],"text":"ölümden sonraki yaşam","usage_role":"contextual"},{"applicability":"İçinde yaşanılan dünyaya karşıt ikinci yaşam yurdu kastedildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dünya yaşamına karşıt ikinci varoluş yurdunu doğal ve yerleşik biçimde karşılar."},"facet_ids":["F002","F003"],"text":"öteki dünya","usage_role":"contextual"}],"definition":"İçinde yaşanılan dünya düzeninden sonra başlayacağı kabul edilen ikinci varoluş ve bu varoluşun yurdudur. Tek başına kullanılan biçim, bağlamda bu yurt ifadesinin düşürülmüş biçimi olarak işleyebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dünya yaşamından sonra gelen ikinci varoluş düzeni anlatılır."},{"facet_id":"F002","role":"specialization","statement":"Bu ikinci varoluş, içinde bulunulan dünyaya karşıt bir yurt olarak adlandırılır."},{"facet_id":"F003","role":"source_variant","statement":"Yurt adı söylenmeden kullanılan biçim, bağlam içinde ikinci yaşam yurdunu tek başına temsil eder."}],"identity_rationale":"Kaynak ifadesi, dünya yaşamının karşısındaki ikinci varoluşu ve onun yurdunu açıkça tek bir yerleşik kavram olarak sunar. Bu kullanım, herhangi bir dişil sonraki biçimine veya sıradan zaman gecikmesine genellenemez.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ölümden sonraki yaşam; öteki dünya"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"öteki dünya"}],"lexicalization_note":"Tanım, tek başına kullanılan biçim ile öteki dünyayı belirten söz öbeğini ayırırken ikisini aynı ikinci varoluş kavramına bağlar.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yerleşik ikinci yaşam kavramını genel sonralık ve geciktirmeden ayıran iki iç komşu yeterli bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı belirli bir ikinci yaşam düzenine özgü yerleşik kavramdır; komşu dal ise nesne, kişi veya sıra ayrımı gözetmeden genel sonralık ve ötekilik bildirir.","focus_only":"Dünya yaşamından sonraki ikinci varoluşu ve onun yurdunu yerleşik bir inanç kavramı olarak gösterir.","gloss":"öteki dünya ile öteki öğe","neighbor_only":"Herhangi bir dizide sonraki veya ilk olmayıp başka olan öğeyi gösterebilir.","neighbor_ref":"root_000019/B001","relation_type":"near_neighbor","shared_zone":"İkinci varoluşun bu dünyadan sonra ve ona karşıt düşünülmesi genel sonralık ve başkalıkla bağ kurar."},{"boundary_match":"thematic_only","distinction":"Odak dalında sonraki yaşam yerleşik bir varoluş alanıdır; komşu dalda ise olayın zamanlamasını değiştiren süreç veya geride kalma durumu vardır.","focus_only":"Dünya yaşamından sonraki ikinci varoluş düzenini adlandırır.","gloss":"sonraki yaşam ile geciktirme","neighbor_only":"Bir olayın zamanını ileri bırakma veya bir öznenin gecikmesi sürecini anlatır.","neighbor_ref":"root_000019/B002","relation_type":"thematic","shared_zone":"Her iki dal zaman bakımından daha sonra olma düşüncesiyle aynı geniş senaryoya katılır."}],"source_phrase_ar":"يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)","source_qualifications":[{"kind":"sole_attestation","summary":"İkinci varoluşun yurdu tam söz öbeğiyle veya yurt adı düşürülerek tek başına anılabilir."}],"source_summary":"Tek kaynaklı kanıt, ikinci varoluş ile onun yurdunu aynı yerleşik kavramın iki anlatımı olarak verir ve yurt adının bağlamda söylenmeden bırakılabildiğini belirtir.","sources":["MU"],"what_is_ar":"يدخل فيه الآخرة والدار الآخرة بوصفها النشأة الثانية أو دار الحياة الآخرة المقابلة للدنيا.","what_is_not_ar":"لا يدخل فيه كل مؤنث لآخر ولا كل تأخير زمني إلا إذا صار اصطلاحا للدار أو النشأة الآخرة."},"support_links":[]},{"boundary":"Bu dal, geriye kalan parçayı, birini bağışlayarak sağ bırakmayı veya bakarak beklemeyi değil, doğrudan sürme ve yok olmama durumunu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000142/B001","candidate_links":[{"candidate_id":"cand_943aa477973aad770107","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَبْقَىٰٓ","morph_features":"STEM|POS:N|LEM:>aboqaY`^|ROOT:bqy|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:3:2","qac_word_ref":"87:17:3","surface_ar":"أَبْقَىٰٓ"}],"gloss":"varlığını sürdürme ve yok olmama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey yok olmaz; varlığı veya içinde bulunduğu durum sürer."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir insan bakımından bu süreklilik, uzun süre yaşama biçiminde gerçekleşir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İyi işlerin kendisi sona erse de bunların karşılığı veya etkisi sürebilir."}}],"root_ar":"ب ق ي","root_id":"root_000142","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın temelindeki süreklilik ve yok olmama karşıtlığını birlikte karşılayan genel açıklamadır.","boundary_detail":"Bu dal, geriye kalan parçayı, birini bağışlayarak sağ bırakmayı veya bakarak beklemeyi değil, doğrudan sürme ve yok olmama durumunu anlatır.","branch_image_ar":"دوام الشيء وبقاؤه","concept_gloss":"varlığını sürdürme ve yok olmama","contextual_glosses":[{"applicability":"Sürekliliğin bir insanın ömrü bakımından anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan dışındaki varlıkların, durumların veya sonuçların sürmesini kapsamaz.","preserves":"İnsan yaşamının uzun süre devam etmesi anlamını korur."},"facet_ids":["F002"],"text":"uzun süre yaşamak","usage_role":"contextual"},{"applicability":"İyi bir işin etkisinin veya karşılığının işi yapan kişi için sürmesi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dalın bütün varlıklara uygulanabilen genel yok olmama ve sürme anlamını dışarıda bırakır.","preserves":"Bir işin sonucunun zaman içinde devam etmesini korur."},"facet_ids":["F003"],"text":"karşılığı kalıcı olmak","usage_role":"contextual"}],"definition":"Bir şeyin yok olmayarak ilk durumunu veya varlığını sürdürmesidir. İnsan için uzun yaşamayı, iş ve etkiler içinse sonuç ya da karşılığın devam etmesini de kapsayabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey yok olmaz; varlığı veya içinde bulunduğu durum sürer."},{"facet_id":"F002","role":"extension","statement":"Bir insan bakımından bu süreklilik, uzun süre yaşama biçiminde gerçekleşir."},{"facet_id":"F003","role":"specialization","statement":"İyi işlerin kendisi sona erse de bunların karşılığı veya etkisi sürebilir."}],"identity_rationale":"Kaynak ifadesi, anlamın merkezini bir şeyin yok olmayıp durumunu sürdürmesi olarak belirler; uzun yaşama ve iyi işlerin karşılığının kalması da bu sürekliliğin özel gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"varlığını sürdürdü, yok olmadı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sürdü, kalıcı oldu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"varlığını sürdürme, yok olmama"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"varlığını sürdüren, yok olmayan"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kalmasını sağladı veya ömrünü uzattı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"daha kalıcı, daha uzun süreli"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"karşılığı kalıcı olan iyi işler veya ibadetler"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kalma, geride kalan kişi veya topluluk"}],"lexicalization_note":"Tanım genel sürme çekirdeğini verir; uzun yaşama, daha kalıcı olma ve karşılığı süren iyi işler gibi belirli kullanımlar bu çekirdeğe bağlı ayrı yüzler olarak tutulur.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; süreklilik, çok uzun zaman ve geriye kalma sınırlarını en açık gösteren dört karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği varlığın ya da durumun yok olmadan sürmesidir; komşu dal ise yerinde kalma ve çatışmada direnme gibi konumsal veya davranışsal sabitliği de kendi sınırına alır.","focus_only":"İyi işlerin karşılığının sürmesi ve bir insanın uzun yaşaması gibi özel gerçekleşmeleri de içerir.","gloss":"sürme ve sabit kalma","neighbor_only":"Bir yerde kalmayı ve savaşta ayak direyip sabit durmayı ayrıca kapsar.","neighbor_ref":"root_000192/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da yok olma veya sona ermenin karşısında süreklilik ve sabitlik bildirir."},{"boundary_match":"partial","distinction":"Odak dal için devam etme yeterlidir; komşu dal kalıcılığın olağanüstü uzunluğunu veya yok oluşun belirgin biçimde gecikmesini öne çıkarır.","focus_only":"Sıradan sürekliliği, uzun yaşamayı ve bir işin karşılığının devam etmesini özel bir aşırılık şartı olmadan kapsar.","gloss":"çok uzun süre kalıcı olma","neighbor_only":"Yok oluşun çok gecikmesi, çok uzun kalış ve ölümsüzlük tasarımı gibi güçlendirilmiş süreklilikleri öne çıkarır.","neighbor_ref":"root_000429/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin yok olmayıp zaman içinde varlığını sürdürmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal süren şeyin durumunu anlatırken komşu dal süren zamanın uzunluğunu, özellikle sonsuzluğu, kavramlaştırır.","focus_only":"Bir varlığın veya durumun fiilen sürmesini ve yok olmamasını bildirir.","gloss":"sonsuz veya çok uzun süre","neighbor_only":"Süren varlıktan çok sınırsız ya da çok uzun zaman düşüncesini ve sonsuzlaştırmayı adlandırır.","neighbor_ref":"root_000004/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın ortak alanı zaman içinde kesintisiz devam etmedir."},{"boundary_match":"partial","distinction":"Odak dal süreklilik durumudur; komşu dal ise bu süreklilik sonucunda geride bulunan somut ya da soyut kalandır.","focus_only":"Bir şeyin varlığını veya durumunu sürdürmesi sürecini ve durumunu anlatır.","gloss":"sürme ile geriye kalan","neighbor_only":"Bir bütünün ardından elde kalan parçayı, tutarı veya topluluğu adlandırır.","neighbor_ref":"root_000142/B002","relation_type":"near_neighbor","shared_zone":"Geriye kalan bir parça da sona ermeyip varlığını sürdürmüş olduğundan iki dal sonuç bakımından buluşur."}],"source_phrase_ar":"أصل واحد وهو الدوام (maqayis)؛ بقي الشيء يبقى بقاء وهو ضد الفناء (maqayis;ayn;tahdhib)؛ بقى الشيء يبقى بقاء وبقي الرجل زمانا طويلا أي عاش (sihah)؛ البقاء ثبات الشيء على حاله الأولى وهو يضاد الفناء (mufradat)؛ الباقيات الصالحات هي الصلوات الخمس وقيل الأعمال الصالحة كلها (tahdhib;mufradat)","source_summary":"Kaynakların paylaştığı çekirdek, bir şeyin ilk durumunu koruyarak sürmesi ve yok olmamasıdır. Ayrıntılar bunu uzun yaşama örneğine ve kalıcı iyi işler ifadesinin beş vakit ibadet ya da bütün iyi işler olarak yorumlanmasına genişletir. Ayrıca bir lehçe biçimi ile kalan dişil biçimin mastar, kişi, topluluk veya geride kalan eylem olarak açıklanması aktarılır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه بقاء الشيء وثباته ضد الفناء، وطول العيش، وبقاء الأثر أو الثواب.","what_is_not_ar":"ليس المراد خصوص البقية المتروكة من شيء، ولا فعل العفو والإبقاء، ولا الترقب بالبصر، إلا من جهة رجوعها إلى معنى الدوام العام."},"support_links":["sup_1fd91e24ee29a5f37fb2"]},{"boundary":"Bu dal geride bulunan sonucu adlandırır; o sonucu doğuran kasıtlı ayırma, bağışlama veya genel varlığını sürdürme durumu dalın çekirdeği değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000142/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبْقَىٰٓ","morph_features":"STEM|POS:N|LEM:>aboqaY`^|ROOT:bqy|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:3:2","qac_word_ref":"87:17:3","surface_ar":"أَبْقَىٰٓ"}],"gloss":"bir şeyden geriye kalan bölüm","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünün bir bölümü gider veya kullanılır; geride kalan bölüm sonuç olarak bulunmaya devam eder."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hesap ve gelir bağlamında tahsil edilen ya da kullanılan miktardan sonra kalan tutarı gösterebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir topluluktan geriye kalan kişiler veya o toplulukta hâlâ bulunan iyilik ve sağlamlık payı da bu anlamla anlatılabilir."}}],"root_ar":"ب ق ي","root_id":"root_000142","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bütünün ardından sonuç olarak elde bulunan somut veya soyut kalanı karşılayan genel açıklamadır.","boundary_detail":"Bu dal geride bulunan sonucu adlandırır; o sonucu doğuran kasıtlı ayırma, bağışlama veya genel varlığını sürdürme durumu dalın çekirdeği değildir.","branch_image_ar":"البقية وما يبقى من الشيء","concept_gloss":"bir şeyden geriye kalan bölüm","contextual_glosses":[{"applicability":"Gelir, vergi veya hesap sonunda elde bulunan miktar söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Topluluktan kalan kişileri ve soyut iyilik ya da sağlamlık payını kapsamaz.","preserves":"Bir miktardan geriye kalan hesaplanabilir payı korur."},"facet_ids":["F002"],"text":"kalan tutar","usage_role":"contextual"},{"applicability":"Bir kişi veya toplulukta hâlâ iyilik, inanç ya da dayanıklılık bulunduğu anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Maddi parçaları, hesap sonunda kalan tutarı ve geride kalan topluluğu dışarıda bırakır.","preserves":"Soyut bir iyi niteliğin bütünüyle kaybolmayıp kalmasını korur."},"facet_ids":["F003"],"text":"iyilikten kalan pay","usage_role":"explanatory"}],"definition":"Bir şey eksildikten, harcandıktan veya ortadan kalktıktan sonra ondan geriye kalan bölüm, tutar ya da topluluktur. Soyut olarak bir toplulukta hâlâ bulunan iyilik ve sağlamlık payını da anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünün bir bölümü gider veya kullanılır; geride kalan bölüm sonuç olarak bulunmaya devam eder."},{"facet_id":"F002","role":"specialization","statement":"Hesap ve gelir bağlamında tahsil edilen ya da kullanılan miktardan sonra kalan tutarı gösterebilir."},{"facet_id":"F003","role":"extension","statement":"Bir topluluktan geriye kalan kişiler veya o toplulukta hâlâ bulunan iyilik ve sağlamlık payı da bu anlamla anlatılabilir."}],"identity_rationale":"Kaynak ifadesi, bir şeyden geriye kalanı; gelirden kalan tutarı ve bir toplulukta kalan iyilik ya da direnç payını aynı sonuç merkezinde toplar. Bunlar, bağışlayıp sağ bırakma eyleminden veya bilinçli olarak bir parçayı ayırma işleminden ayrılabilir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bir şeyden geriye kalan, artık"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"geriye kalan bölüm"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"gelir veya vergiden kalan tutar"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kendilerinde iyilik ve sağlamlık kalmış kimseler"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"Tanrı'nın size helal olarak bıraktığı şey; ayrıca Tanrı'yı gözetme"}],"lexicalization_note":"Tanım geriye kalan sonucu merkeze alır; gelir artığı, kalan topluluk ve kişide ya da toplulukta kalan iyilik gibi belirli kullanımlar ayrı yüzler olarak korunur.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; kalıntı, fazlalık ve kasıtlı ayırma arasındaki sınırı en iyi açıklayan dört karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve sınır aynıdır; gelir, iyilik, günün sonu ve kuyu suyu gibi farklı örnek alanları eş anlamlılığı bozmaz.","focus_only":null,"gloss":"geriye kalan bölüm","neighbor_only":null,"neighbor_ref":"root_000507/B007","relation_type":"synonym","shared_zone":"Her iki dal da daha büyük bir şeyden geriye kalan bölümü veya son parçayı anlatır."},{"boundary_match":"partial","distinction":"Odak dalda yalnızca geride bulunma yeterlidir; komşu dalda kalan şey çoğu kez gereksinimi aşan bir fazlalıktır.","focus_only":"Bir topluluktan kalanları ve toplulukta süren iyilik veya sağlamlığı kapsar.","gloss":"kalan ile fazlalık","neighbor_only":"Gereksinim ya da bölüşme sonrasında fazladan kalan yiyecek, su ve malı, yani fazlalık niteliğini öne çıkarır.","neighbor_ref":"root_001163/B001","relation_type":"near_synonym","shared_zone":"İki dal da kullanım veya bölüşme sonrasında elde bulunan artakalan payı gösterebilir."},{"boundary_match":"partial","distinction":"Odak dal elde bulunan sonucu, komşu dal ise bu sonucu doğuran kasıtlı ayırma ve saklama işlemini merkeze alır.","focus_only":"İşlem tamamlandıktan sonra geride bulunan bölüm veya tutarı sonuç olarak adlandırır.","gloss":"kalan sonuç ile ayırıp tutma","neighbor_only":"Bir bölümün elde tutulması, ayrılması veya daha sonra kullanılmak üzere saklanması eylemini bildirir.","neighbor_ref":"root_000142/B004","relation_type":"near_neighbor","shared_zone":"Bir parçayı elde tutma eylemi sonunda o parça geriye kalan bölüm olabilir."},{"boundary_match":"partial","distinction":"Odak dal kalanı bir sonuç ve varlık olarak sunar; komşu dal bu sonucun yanında bırakma eylemini ve kalanın yokluğunu da kendi alanına alır.","focus_only":"Gelirden kalan tutarı ve toplulukta kalan soyut iyilik payını içerir.","gloss":"artakalan ve geride bırakma","neighbor_only":"Yeme veya başka bir eylem sonrasında bir şeyi bırakma eylemini ve hiçbir şey kalmamasını da kapsar.","neighbor_ref":"root_000830/B004","relation_type":"near_synonym","shared_zone":"Her iki dal yiyecek, mal veya topluluktan geriye kalan bölümü anlatabilir."}],"source_phrase_ar":"نشدتك الله والبقيا وهي البقية (maqayis;ayn;tahdhib)؛ بقي من الشيء بقية والباقية توضع موضع المصدر (sihah)؛ الباقي حاصل الخراج ونحوه (tahdhib)؛ بقيت الله أي ما أبقى لكم من الحلال (tahdhib)؛ أولو بقية من دين قوم لهم بقية إذا كانت بهم مسكة وفيهم خير (tahdhib)؛ فهل ترى لهم من باقية أي جماعة باقية أو فعلة لهم باقية وقيل معناه بقية (mufradat)","source_summary":"Çekirdek, daha büyük bir şeyden geriye kalan bölümdür. Ayrıntılarda bu kalan; gelirden arta kalan tutar, izin verilen şeylerden bırakılan pay, iyilik ve sağlamlık taşıyan bir topluluk, kalan topluluk ya da geride kalan eylem olarak farklı biçimlerde açıklanır. Tanrı'nın bıraktığı pay ifadesi için ayrıca Tanrı'yı gözetme yorumu verilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه البقية والباقية والباقي من مال أو خراج، وما أبقاه الله أو بقي من الخير والمسكة.","what_is_not_ar":"ليس هو فعل استبقاء الشخص بالعفو، ولا حبس بعض الشيء قصدا للادخار، ولا انتظار الشيء وترقبه."},"support_links":[]},{"boundary":"Dalın çekirdeği edilgen biçimde hayatta kalmak değil, gücü yeten tarafın merhamet veya bağışlama göstererek kişiyi ya da ilişkiyi ortadan kaldırmamasıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000142/B003","candidate_links":[{"candidate_id":"cand_6349af299a067939a02c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَبْقَىٰٓ","morph_features":"STEM|POS:N|LEM:>aboqaY`^|ROOT:bqy|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:3:2","qac_word_ref":"87:17:3","surface_ar":"أَبْقَىٰٓ"}],"gloss":"bağışlayıp sağ bırakma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Üstün veya yetkili taraf, zarar verme ya da öldürme gücü varken kişiyi bağışlar ve sağ bırakır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağışlama, kişinin kusurundan sonra aradaki sevginin ve ilişkinin sürmesini sağlayabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yenilen taraf, üstün gelen taraftan kendilerini tümüyle yok etmeyip sağ bırakmasını isteyebilir."}}],"root_ar":"ب ق ي","root_id":"root_000142","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gücü yeten tarafın merhamet göstererek kişiyi öldürmemesi veya tümüyle ortadan kaldırmaması için kullanılan genel açıklamadır.","boundary_detail":"Dalın çekirdeği edilgen biçimde hayatta kalmak değil, gücü yeten tarafın merhamet veya bağışlama göstererek kişiyi ya da ilişkiyi ortadan kaldırmamasıdır.","branch_image_ar":"الإبقاء عفوا واستحياء","concept_gloss":"bağışlayıp sağ bırakma","contextual_glosses":[{"applicability":"Bir kişinin yanılgısından sonra onu bağışlayarak ilişkiyi ve karşılıklı sevgiyi sürdürme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Canı bağışlama ve yenilmiş bir topluluğu tümüyle yok etmeme boyutunu kapsamaz.","preserves":"Bağışlamanın ilişkiyi ve sevgiyi sürdürmesi sonucunu korur."},"facet_ids":["F002"],"text":"kusurunu bağışlayıp sevgisini korumak","usage_role":"contextual"},{"applicability":"Yenilmiş bir grubun üstün gelen düşmandan acıma ve tümüyle yok edilmeme istediği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bireysel bir kusuru bağışlayarak sevgiyi koruma kullanımını kapsamaz.","preserves":"Üstün taraftan canların bağışlanmasını ve yok etmeye son vermesini istemeyi korur."},"facet_ids":["F003"],"text":"bizi yok etmeyin, sağ bırakın","usage_role":"contextual"}],"definition":"Birine zarar verme, onu öldürme veya bütünüyle ortadan kaldırma gücü varken merhamet ya da bağışlama gösterip onu sağ bırakmaktır. Bir kusurdan sonra kişiyi bağışlayarak aradaki sevgiyi korumayı da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Üstün veya yetkili taraf, zarar verme ya da öldürme gücü varken kişiyi bağışlar ve sağ bırakır."},{"facet_id":"F002","role":"extension","statement":"Bağışlama, kişinin kusurundan sonra aradaki sevginin ve ilişkinin sürmesini sağlayabilir."},{"facet_id":"F003","role":"associated_use","statement":"Yenilen taraf, üstün gelen taraftan kendilerini tümüyle yok etmeyip sağ bırakmasını isteyebilir."}],"identity_rationale":"Kaynak ifadesi, zarar verme veya öldürme gücü varken bir kişiyi bağışlayıp sağ bırakmayı, ona acımayı ve kusurundan sonra sevgiyi korumayı aynı koruyucu eylem çevresinde birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"Tanrı aşkına bize acıyın ve bizi sağ bırakın"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"acıma ve sağ bırakma"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ona acıdı ve onu sağ bıraktı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"onu bağışlayıp sağ bıraktı veya sevgisini korudu"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bizi yok etmeyin, sağ bırakın"}],"lexicalization_note":"Tanım koruyucu bağışlama çekirdeğini verir; canı bağışlama, tümüyle yok etmeme, acıma dileği ve kusurdan sonra sevgiyi sürdürme gibi yapıya bağlı kullanımları birbirine karıştırmadan kapsar.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; genel bağışlama, cezanın kaldırılması, merhamet duygusu ve edilgen sürme ile sınırı gösteren dört ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bağışlamayı kişinin, topluluğun ya da ilişkinin korunması sonucuna bağlar; komşu dalın çekirdeği ise yalnızca kusurdan dolayı hesap sormamaktır.","focus_only":"Bağışlama sonucunda kişinin sağ kalmasını, topluluğun tümüyle yok edilmemesini veya sevginin korunmasını gerektirir.","gloss":"bağışlama ile sağ bırakma","neighbor_only":"Her türlü kusur ya da suç için hesap sormaktan vazgeçmeyi, kişinin hayatı veya ilişkinin sürmesi şartı olmadan kapsar.","neighbor_ref":"root_000276/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da kusur veya suç karşısında kişiyi cezalandırmaktan vazgeçmeyi içerebilir."},{"boundary_match":"partial","distinction":"Odak dalın belirleyici sonucu sağ bırakma veya ilişkiyi sürdürmedir; komşu dalda belirleyici işlem cezanın ve suçun etkisinin kaldırılmasıdır.","focus_only":"Kişiyi öldürmeme, topluluğu tümüyle yok etmeme ve sevgiyi sürdürme gibi koruyucu sonuçları içerir.","gloss":"cezayı kaldırma ve canı bağışlama","neighbor_only":"Hak edilmiş cezayı kaldırmayı ve suçun kaydını silmeyi, canı ya da ilişkiyi koruma şartı olmadan kapsar.","neighbor_ref":"root_001032/B001","relation_type":"near_synonym","shared_zone":"İki dal da cezayı hak eden birine yaptırım uygulamaktan vazgeçme alanında örtüşür."},{"boundary_match":"field_only","distinction":"Odak dal koruyucu kararı ve sağ bırakma sonucunu anlatır; komşu dal ise bu kararı doğurabilen duygu ve iyilik yönelimini anlatır.","focus_only":"Acımanın sonucu olarak kişiye zarar vermemeyi ve onu sağ bırakmayı bildirir.","gloss":"merhamet duygusu ile sağ bırakma","neighbor_only":"İçsel yumuşaklığı, şefkati ve acınan kişiye iyilik etmeyi sonuçtan bağımsız biçimde kapsar.","neighbor_ref":"root_000552/B001","relation_type":"near_neighbor","shared_zone":"Merhamet, gücü yeten tarafı kişiyi bağışlayıp korumaya yöneltebilir."},{"boundary_match":"partial","distinction":"Odak dal sürekliliği doğuran merhametli ve geçişli eylemdir; komşu dal ise bu eylemden bağımsız olarak süren varlık veya durumdur.","focus_only":"Başka bir tarafın gücünü kullanmaktan vazgeçerek kişiyi veya ilişkiyi korumasını gerektirir.","gloss":"sağ bırakma ile varlığını sürdürme","neighbor_only":"Bir şeyin herhangi bir bağışlayan taraf olmadan kendi varlığını veya durumunu sürdürmesini anlatır.","neighbor_ref":"root_000142/B001","relation_type":"near_neighbor","shared_zone":"Sağ bırakılan kişi, bağışlama eyleminin sonucu olarak yaşamını sürdürür."}],"source_phrase_ar":"استبقيت فلانا أن تعفو عن زلله فتستبقي مودته (maqayis)؛ استبقيت فلانا إذا أوجبت عليه قتلا وعفوت عنه واستبقيت مودته (ayn;tahdhib)؛ أبقيت على فلان إذا أرعيت عليه ورحمته واستبقاه استحياه (sihah)؛ العرب تقول للعدو إذا غلب البقية أي أبقوا علينا ولا تستأصلونا (tahdhib)","source_summary":"Ortak çekirdek, üstün tarafın zarar vermekten vazgeçerek kişiyi, topluluğu veya ilişkiyi korumasıdır. Ayrıntılar kusuru bağışlayıp sevgiyi koruma, hak edilmiş ölüm cezasından vazgeçerek sağ bırakma, merhamet gösterme ve yenilmiş topluluğun tümüyle yok edilmemeyi istemesi arasında ayrışır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الإبقاء على شخص بالعفو والرحمة وترك الاستئصال، واستبقاء المودة بعد الزلل.","what_is_not_ar":"ليس هو مجرد بقاء الشيء بنفسه، ولا البقية المتروكة من مال أو شيء، ولا مراقبة الشيء وانتظاره."},"support_links":["sup_494adb4b482277e4a4a1"]},{"boundary":"Dal, kendiliğinden geriye kalmış bir parçayı değil, bir bölümün bilinçli biçimde ayrılması, elde tutulması veya yedek güç olarak saklanması eylemini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000142/B004","candidate_links":[{"candidate_id":"cand_d04c778a5e6e0ee28341","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَبْقَىٰٓ","morph_features":"STEM|POS:N|LEM:>aboqaY`^|ROOT:bqy|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:3:2","qac_word_ref":"87:17:3","surface_ar":"أَبْقَىٰٓ"}],"gloss":"bir bölümünü ayırıp elde tutma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünün tamamı verilmez veya kullanılmaz; bir bölümü bilinçli olarak ayrılır ve elde tutulur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir at, koşarken gücünün tamamını tüketmeyip bir bölümünü daha sonra kullanmak üzere saklayabilir."}}],"root_ar":"ب ق ي","root_id":"root_000142","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bütünün tamamını vermemek veya tüketmemek ve bir kısmını daha sonra için saklamak anlamını birlikte karşılar.","boundary_detail":"Dal, kendiliğinden geriye kalmış bir parçayı değil, bir bölümün bilinçli biçimde ayrılması, elde tutulması veya yedek güç olarak saklanması eylemini anlatır.","branch_image_ar":"حبس بعض الشيء وادخاره","concept_gloss":"bir bölümünü ayırıp elde tutma","contextual_glosses":[{"applicability":"Bir atın koşarken gücünün tamamını kullanmayıp bir kısmını sonraki aşama için ayırdığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mal veya başka bir nesnenin bir bölümünü verirken elde tutma kullanımını kapsamaz.","preserves":"Eldeki gücün bir bölümünü tüketmeyip sonraki kullanım için ayırmayı korur."},"facet_ids":["F002"],"text":"gücünü sonraya saklamak","usage_role":"contextual"}],"definition":"Bir şeyi verirken, harcarken veya kullanırken onun bir bölümünü ayırıp elde tutmak ve gerektiğinde kullanmak üzere saklamaktır. Bir atın koşu gücünün tamamını tüketmeyip bir kısmını sonraya ayırması da bu işlemin özel bir uygulamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünün tamamı verilmez veya kullanılmaz; bir bölümü bilinçli olarak ayrılır ve elde tutulur."},{"facet_id":"F002","role":"specialization","statement":"Bir at, koşarken gücünün tamamını tüketmeyip bir bölümünü daha sonra kullanmak üzere saklayabilir."}],"identity_rationale":"Kaynak ifadesi, bir şey verilirken veya kullanılırken onun bir bölümünü kasıtlı biçimde elde tutmayı ve bu bölümün daha sonra kullanılmak üzere ayrılmasını açıkça bildirir; atın gücünün bir kısmını saklaması da aynı işlemin uzmanlaşmış örneğidir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"bir bölümünü ayırıp elde tuttum"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"koşu gücünün bir bölümünü sonraya saklayan atlar"}],"lexicalization_note":"Tanım kasıtlı ayırıp tutma işlemini verir; bir şeyden pay saklama ile atın koşu gücünü sonraya ayırması, genel bir artık anlamına dönüştürülmeden ayrı yüzler olarak korunur.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; sonuç olarak kalma, yedek saklama, cimrice esirgeme ve doğal tutulma ile sınırı gösteren dört ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal niyetli işlemi merkeze alır; komşu dal ise niyet ve işlemden bağımsız olarak elde bulunan kalanı gösterir.","focus_only":"Bir parçanın bilinçli biçimde ayrılması, elde tutulması ve gerekirse sonraya saklanması işlemini anlatır.","gloss":"ayırıp tutma ile geriye kalan","neighbor_only":"Bir bütün eksildikten sonra sonuç olarak geride bulunan bölüm veya tutarı adlandırır.","neighbor_ref":"root_000142/B002","relation_type":"near_neighbor","shared_zone":"Kasıtlı biçimde elde tutulan parça, işlem sonunda geriye kalan bölüm olarak bulunur."},{"boundary_match":"partial","distinction":"Odak dalın ayırt edici işlemi bütünün bir kısmını tüketmemektir; komşu dalın ayırt edici işlemi ise şeyi saklı bir yedek olarak depolamaktır.","focus_only":"Bir bütünün bir kısmını verirken veya kullanırken onu tüketmeyip elde tutmayı bildirir.","gloss":"elde tutma ile yedek saklama","neighbor_only":"Bir şeyi gizli veya güvenli yerde saklanan bir yedek hâline getirmeyi öne çıkarır.","neighbor_ref":"root_000078/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir şey gelecekte kullanılmak üzere mevcut tutulabilir."},{"boundary_match":"partial","distinction":"Odak dal ihtiyat ve sonraki kullanım için ayırmadır; komşu dalda belirleyici unsur cimrilik veya vermeyi azaltma niyetidir.","focus_only":"Tutulan bölümün daha sonra kullanılmasını veya gücün korunmasını içerir ve cimrilik şartı taşımaz.","gloss":"ihtiyat için tutma ile cimrice esirgeme","neighbor_only":"Bir şeyi cimrilik ederek veya verilen miktarı azaltmak amacıyla esirgemeyi içerir.","neighbor_ref":"root_000803/B004","relation_type":"near_neighbor","shared_zone":"İki dal da elde bulunanın tamamını vermeme ve bir bölümünü tutma davranışında buluşabilir."},{"boundary_match":"field_only","distinction":"Odak dal seçilmiş bir bölümün geleceğe ayrılmasını gerektirir; komşu dal akışın veya çıkışın engellenmesini anlatır ve parça ayırma şartı taşımaz.","focus_only":"Bir kişinin veya canlının bir bölüm ya da güç payını kasıtlı biçimde elde tutmasını anlatır.","gloss":"kasıtlı elde tutma ile akışın tutulması","neighbor_only":"Yağmurun, idrarın veya rüzgârın doğal ya da bedensel olarak tutulması ve akışın durmasıdır.","neighbor_ref":"root_000345/B001","relation_type":"same_field","shared_zone":"Her iki dalda da bir şeyin bütünüyle dışarı çıkmaması veya hareketini sürdürmemesi söz konusudur."}],"source_phrase_ar":"إذا أعطيت شيئا وحبست بعضه قلت استبقيت بعضه (ayn;tahdhib)؛ استبقيت من الشيء أي تركت بعضه (sihah)؛ المبقيات من الخيل التي تبقي بعض جريها تدخره (tahdhib)","source_summary":"Ortak çekirdek, bir şeyin tamamını vermeyip ya da tüketmeyip bir bölümünü elde tutmak veya bırakmaktır. Ayrıntılardan biri, atın koşu gücünün bir bölümünü sonraya saklamasını bu işlemin özel bir örneği olarak verir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه أن يمسك المعطي بعض ما عنده، أو يترك جزءا من الشيء، أو تدخر الخيل بعض جريها.","what_is_not_ar":"ليس هو مطلق البقية بوصفها حاصلا باقيا، ولا إبقاء الشخص بالعفو، ولا دوام الشيء ضد الفناء."},"support_links":["sup_4f5cd9b273d716085f0d"]},{"boundary":"Çekirdek dikkatini bir şeye yöneltip onu gözeterek beklemektir; bakışla izleme güçlü bir gerçekleşmedir, her kullanımın zorunlu koşulu değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000142/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبْقَىٰٓ","morph_features":"STEM|POS:N|LEM:>aboqaY`^|ROOT:bqy|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:3:2","qac_word_ref":"87:17:3","surface_ar":"أَبْقَىٰٓ"}],"gloss":"gözetleyerek bekleme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi dikkatini hedefe yöneltir, onu gözetir ve görünmesini ya da gelmesini bekler."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hedef göz önündeyken ona bakmak, hareketini izlemek veya nerede belireceğini kollamak öne çıkabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişinin ya da beklenen olayın gelmesi için uzun süre gözeterek beklemek de aynı anlam alanına girer."}}],"root_ar":"ب ق ي","root_id":"root_000142","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir hedefi dikkatle izleme ile onun görünmesini, gelmesini veya gerçekleşmesini bekleme bileşenlerini birlikte karşılar.","boundary_detail":"Çekirdek dikkatini bir şeye yöneltip onu gözeterek beklemektir; bakışla izleme güçlü bir gerçekleşmedir, her kullanımın zorunlu koşulu değildir.","branch_image_ar":"ترقب الشيء وانتظاره بالبصر","concept_gloss":"gözetleyerek bekleme","contextual_glosses":[{"applicability":"Bir nesnenin görünüşünü veya hareketini gözle takip etmenin öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Görsel takip gerektirmeyen kişi veya olay bekleme kullanımlarını kapsamaz.","preserves":"Dikkatin hedefe çevrilmesini ve görsel izlemenin sürekliliğini korur."},"facet_ids":["F002"],"text":"gözünü ayırmadan izlemek","usage_role":"contextual"},{"applicability":"Şimşek gibi kısa süreli bir belirtinin hangi yönde görüneceğini gözleyerek bekleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir kişiyi uzun süre bekleme ve genel hedefi izleme kullanımlarını dışarıda bırakır.","preserves":"Bir belirtinin yerini dikkatle gözleyip görünmesini beklemeyi korur."},"facet_ids":["F002"],"text":"nerede belireceğini kollamak","usage_role":"contextual"},{"applicability":"Bir kişinin veya beklenen olayın gerçekleşmesini bir süre boyunca dikkatle bekleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Görünür bir nesneyi o anda gözle izleme kullanımını kapsamaz.","preserves":"Beklenen hedefe yönelik dikkatli ve süreli beklemeyi korur."},"facet_ids":["F003"],"text":"gelmesini gözleyerek beklemek","usage_role":"contextual"}],"definition":"Dikkati bir şeye yönelterek onu izlemek, gelişini ya da görünmesini gözetmek ve gerçekleşmesini beklemektir. Bazı kullanımlarda gözle sürekli takip belirginken, bazılarında süre boyunca bekleme öne çıkar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi dikkatini hedefe yöneltir, onu gözetir ve görünmesini ya da gelmesini bekler."},{"facet_id":"F002","role":"specialization","statement":"Hedef göz önündeyken ona bakmak, hareketini izlemek veya nerede belireceğini kollamak öne çıkabilir."},{"facet_id":"F003","role":"extension","statement":"Bir kişinin ya da beklenen olayın gelmesi için uzun süre gözeterek beklemek de aynı anlam alanına girer."}],"identity_rationale":"Kaynak ifadesinin önemli bir bölümü bakışla izleme ve gözetlemeyi bildirir; ancak kişi veya elçi bekleme örnekleri görsel takibi zorunlu kılmadan süreli beklemeyi de kapsar. Bu nedenle dal korunabilir, fakat yalnızca gözle bekleme olarak sınırlandırılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"onu gözetip bekledim"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"onu gözleriyle izleyip gözetliyor"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"geceyi şimşeğin nerede parlayacağını gözleyerek geçirdi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"ibadet çağrısını benim için gözet"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"Tanrı'nın elçisini uzun süre bekleyip gözledik"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"ona bakıp onu gözetledi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"ona bakıp onu gözetledi"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"ona bakıp onu gözetledi"}],"lexicalization_note":"Tanım gözetleme ile bekleme ortaklığını verir; bir şeyi gözle izleme, şimşeğin yerini kollama, çağrıyı gözetme ve bir kişiyi bekleme gibi yapıya bağlı kullanımlar ayrı yüzler olarak tutulur.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; genel gözetleme, zamanı kollama, nöbet tutma ve doğrudan görme ile sınırı açıklayan dört ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal görsel izleme ile süreli beklemeyi aynı çekirdekte toplar; komşu dalın alanı daha genel gözetleme ve buna bağlı korkuyu da kapsar.","focus_only":"Şimşeğin nerede belireceğini gözleme ve bir kişiyi uzun süre bekleme gibi belirli izleme-bekleme kullanımlarını kapsar.","gloss":"gözetleme ve bekleme","neighbor_only":"Beklenen söz veya gelişin yanında, gözetlemeye dayanan korkuyu da içerir.","neighbor_ref":"root_000584/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da dikkati bir hedefe yöneltip onu izlemeyi ve gelişini ya da ortaya çıkışını beklemeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dalın dikkati hedefin kendisine ve görünmesine yönelir; komşu dalın dikkati gerçekleşme anına veya uygun zamana yönelir.","focus_only":"Hedefi gözle izlemeyi veya nerede belireceğini kollamayı içerebilir.","gloss":"hedefi gözetme ile zamanını kollama","neighbor_only":"Bir şeyin uygun zamanını kollamayı, hedefi görsel olarak izleme şartı olmadan öne çıkarır.","neighbor_ref":"root_000382/B005","relation_type":"near_synonym","shared_zone":"İki dal da beklenen bir şey gerçekleşinceye kadar dikkatli biçimde beklemeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği hedefi dikkatle beklemektir; komşu dal bu gözetlemeyi koruma veya saldırı hazırlığı işlevine bağlayabilir.","focus_only":"Bir şeyin görünmesini veya gelmesini izleyerek beklemeyi bildirir ve koruma ya da saldırı amacı gerektirmez.","gloss":"bekleyerek izleme ile nöbet tutma","neighbor_only":"Nöbet tutma, koruma ve saldırmak için pusuya yatma gibi amaçlı gözetlemeleri kapsar.","neighbor_ref":"root_000566/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da hedefe sürekli dikkat yöneltme, izleme ve ortaya çıkışını bekleme vardır."},{"boundary_match":"field_only","distinction":"Odak dal süreli izleme ve beklenti içerir; komşu dalda tek başına doğrudan görme veya tanık olma yeterlidir.","focus_only":"Görsel dikkatin yanında hedefin belirmesini veya gelmesini beklemeyi gerektirir.","gloss":"gözetleyerek bekleme ile gözle görme","neighbor_only":"Bir şeyi gözle görmeyi ve doğrudan tanık olmayı, süreli bekleme ya da gözetleme şartı olmadan anlatır.","neighbor_ref":"root_001069/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da göz ve doğrudan görsel dikkat hedefe yönelir."}],"source_phrase_ar":"يبقى الشيء ببصره إذا كان ينظر إليه ويرصده (maqayis;ayn)؛ بات فلان يبقي البرق أي ينظر إليه من أين يلمع (maqayis;ayn)؛ بقيت فلانا أبقيه إذا رعيته وانتظرته (maqayis)؛ بقيته أبقيه أي نظرت إليه وترقبته وبقينا رسول الله أي انتظرناه (sihah)؛ بقينا رسول الله أي انتظرناه وترصدنا له مدة كثيرة (mufradat)","source_summary":"Ortak çekirdek, dikkati bir hedefe yönelterek onu gözetmek ve beklemektir. Ayrıntılar şimşeğin nerede görüneceğini görsel olarak kollama, bir kişiyi uzun süre bekleme, ibadet çağrısını bir başkası için gözetme ve aynı gözetleme-bekleme anlamını taşıyan biçim değişkeleri arasında ayrışır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه النظر إلى الشيء ورصده وترقبه وانتظاره، كترقب البرق أو الظعن أو انتظار شخص.","what_is_not_ar":"ليس هو مجرد دوام الشيء وبقائه، ولا البقية المتروكة، ولا العفو عن مستحق العقوبة."},"support_links":[]},{"boundary":"Bu dal genel iyilik değeridir; seçme eylemi, özel olarak mal, cömertlik veya belirli bir kullanım kalıbı bu çekirdeğin yerine geçirilmez.","branch_kind":"bare","branch_ref":"root_000452/B001","candidate_links":[{"candidate_id":"cand_943aa477973aad770107","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:2:1","qac_word_ref":"87:17:2","surface_ar":"خَيْرٌ"}],"gloss":"arzulanan iyilik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Herkesçe arzu edilen ve kötülüğün karşısında duran genel olumlu değeri bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlama göre yarar yönü belirginleşebilir ve kavram zararın karşısına da yerleştirilebilir."}}],"root_ar":"خ ي ر","root_id":"root_000452","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel olumlu değerin kötülüğe karşı konduğu ve insanların ona yöneldiği yalın kullanımlar için uygundur.","boundary_detail":"Bu dal genel iyilik değeridir; seçme eylemi, özel olarak mal, cömertlik veya belirli bir kullanım kalıbı bu çekirdeğin yerine geçirilmez.","branch_image_ar":"الميل إلى الخير النافع","concept_gloss":"arzulanan iyilik","contextual_glosses":[{"applicability":"Olumlu değerin doğrudan kötülüğün karşıtı olarak kullanıldığı genel bağlamlara uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Herkesçe arzulanma ile yarar ve üstünlük yönlerini tek başına belirtmez.","preserves":"Kötülüğün karşıtı olan olumlu değer yönünü korur."},"facet_ids":["F001"],"text":"iyilik","usage_role":"general"},{"applicability":"Olumlu değerin özellikle zararın karşısında ve fayda sağlayan yönüyle öne çıktığı bağlamlara uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kötülüğün karşıtı olan daha geniş ahlaki ve değer bildiren kapsamı dışarıda bırakır.","preserves":"Zararın karşısındaki fayda sağlayan yönü korur."},"facet_ids":["F002"],"text":"yarar","usage_role":"contextual"}],"definition":"İnsanların yöneldiği ve arzu ettiği, kötülüğün karşıtı olan genel olumlu değerdir; bağlama göre yarar yönü öne çıkabilir ve zarara da karşı konabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Herkesçe arzu edilen ve kötülüğün karşısında duran genel olumlu değeri bildirir."},{"facet_id":"F002","role":"extension","statement":"Bağlama göre yarar yönü belirginleşebilir ve kavram zararın karşısına da yerleştirilebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Birden çok seçenek arasında karar verme eylemini anlamın merkezine ekler.","collision":"Aynı kökün seçme ve seçilme dalıyla karışır.","fit":"displacement","loses":"Genel olumlu değer, kötülüğe karşıtlık ve yarar kapsamını kaybeder.","preserves":"Daha iyi olana yönelme düşüncesini dolaylı olarak çağrıştırabilir."},"text":"seçim"}],"identity_rationale":"Kaynak ifadesi, herkesin yöneldiği ve arzuladığı genel olumlu değeri kötülüğün karşıtı olarak kurar; ayrıca bağlama göre kötülüğe ya da zarara karşı konabildiğini belirtir. Verilen dal çerçevesi bu genel çekirdeği ve yarar yönünü doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"iyilik; yarar veya üstünlük taşıyan olumlu şey"}],"lexicalization_note":"Tanım yalın dalın genel değer anlamıyla sınırlıdır; seçim, mal veya armağanla ilgili özel dalların anlamları buraya taşınmaz.","neighbor_coverage_note":"Gösterilen bütün adaylar değerlendirildi. Yarar, erdemli davranış, üstün nitelik ve cömertlik sınırı en açıklayıcı karşılaştırmaları verdi; yalnızca ortak olumlu çağrışım, örnek veya uzak konu bağı taşıyan diğer adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yararı içine alabilen daha geniş bir iyilik değeridir; komşu dal ise doğrudan fayda sağlama ilişkisini anlatır.","focus_only":"Kötülüğün karşıtı olan genel olumlu değeri ve arzu edilirliği kapsar.","gloss":"genel iyilik ile yarar","neighbor_only":"Fayda sağlama ve zararın karşıtı olma ilişkisini anlamın doğrudan çekirdeği yapar.","neighbor_ref":"root_001536/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de olumlu sonuç, fayda ve zarardan uzaklık alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal genel değer kategorisidir; komşu dal bu değeri inanç ve davranıştaki düzgünlük ve bağlılıkla somutlaştırır.","focus_only":"Yarar yönü öne çıkabilen her türlü genel olumlu değeri kapsayabilir.","gloss":"genel iyilik ile erdemli davranış","neighbor_only":"Düzgünlük, sakınma ve yaratıcıya bağlılıkla ilgili davranış alanını özellikle kapsar.","neighbor_ref":"root_000104/B002","relation_type":"near_synonym","shared_zone":"İki dal da iyilik ve olumlu davranış değeri alanında kesişir."},{"boundary_match":"partial","distinction":"Odak dal soyut ve genel iyiliktir; komşu dal bu değeri taşıdığı düşünülen kişi veya şeyin niteliğidir.","focus_only":"Bir kişi veya nesneye yüklenmeden de var olan genel iyilik değerini bildirir.","gloss":"iyilik ile üstün nitelik","neighbor_only":"Belirli bir kişi veya şeyin üstün, iyi ya da seçkin oluşunu niteleme konusu yapar.","neighbor_ref":"root_000452/B002","relation_type":"near_neighbor","shared_zone":"Her ikisi de olumlu değer değerlendirmesi alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal üst kavram niteliğindeki genel iyiliktir; komşu dal bunun verme ve armağanla belirlenen özel görünümüdür.","focus_only":"Cömertlikten bağımsız olarak arzu edilen her türlü olumlu değeri kapsar.","gloss":"iyilik ile cömertlik","neighbor_only":"İyiliği verme, armağan etme ve kişide cömertlik bolluğu olarak somutlaştırır.","neighbor_ref":"root_000452/B005","relation_type":"near_neighbor","shared_zone":"Cömertlik olumlu ve arzu edilen bir iyilik türü olduğundan iki dal kesişir."}],"source_phrase_ar":"فالخير خلاف الشر لأن كل أحد يميل إليه (maqayis)؛ الخير ضد الشر (jamhara;sihah)؛ الخير ما يرغب فيه الكل وضده الشر (mufradat)؛ يقابل به الشر مرة والضر مرة (mufradat)","source_summary":"Kaynakların ortak çekirdeği, insanların yöneldiği genel olumlu değerin kötülüğün karşıtı olmasıdır. Bu değer bazı bağlamlarda yarar yönüyle belirginleşerek zararla karşıtlık da kurar.","sources":["MQ","JA","SI","MU"],"what_is_ar":"يدخل فيه الخير العام المرغوب فيه، وضد الشر، وما فيه نفع أو فضل أو صلاح، والخير المطلق والمقيد، ومقابلته للشر أو الضر.","what_is_not_ar":"لا يدخل خصوص الاختيار والاستخارة، ولا خصوص المال، ولا ألفاظ الخيار المعربة للنبات."},"support_links":["sup_1fd91e24ee29a5f37fb2"]},{"boundary":"Bu dal salt karşılaştırma derecesi değil, kişi veya şeyde bulunan iyilik ve üstünlük niteliğidir; genel iyilik ile seçme eyleminden ayrıdır.","branch_kind":"bare","branch_ref":"root_000452/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:2:1","qac_word_ref":"87:17:2","surface_ar":"خَيْرٌ"}],"gloss":"iyi ve seçkin olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi veya şeyi iyilik ve değer bakımından üstün, iyi ve seçkin olarak niteler."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanlarda düzgünlük ve erdemin yanı sıra güzellik ve hoş görünüş yönünü de belirginleştirebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir topluluk veya tür içinden düşük nitelikli olmayan üstün ve seçilmiş üyeleri gösterebilir."}}],"root_ar":"خ ي ر","root_id":"root_000452","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya şeyin değer, düzgünlük, güzellik ya da seçkinlik bakımından üstün nitelenmesini kapsayan genel karşılıktır.","boundary_detail":"Bu dal salt karşılaştırma derecesi değil, kişi veya şeyde bulunan iyilik ve üstünlük niteliğidir; genel iyilik ile seçme eyleminden ayrıdır.","branch_image_ar":"فضل الصلاح والاصطفاء","concept_gloss":"iyi ve seçkin olma","contextual_glosses":[{"applicability":"Kişi, hayvan veya nesnenin kendi türü içinde değerli ve iyi sayıldığı niteleme bağlamlarına uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Düzgünlük, güzellik ve seçilmişlik yönlerinden hangisinin öne çıktığını belirtmez.","preserves":"Değer ve nitelik bakımından üstünlük çekirdeğini korur."},"facet_ids":["F001"],"text":"üstün nitelikli","usage_role":"general"},{"applicability":"Bir topluluk içinden iyi ve düşük nitelikten uzak üyelerin çoğul olarak gösterildiği bağlamlara uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir kişi veya şeyde bulunan genel iyilik ve güzellik niteliğini kapsamaz.","preserves":"Üstün üyelerin diğerlerinden ayrılması ve seçkinlik yönünü korur."},"facet_ids":["F003"],"text":"seçkinler","usage_role":"contextual"}],"definition":"Bir kişi veya şeyin iyilik, düzgünlük, güzellik ya da başka bir değer yönünden üstün ve seçkin olmasıdır. Çoğul ve seçme bağlamlarında sıradan veya düşük sayılanlardan ayrılmış iyi üyeleri de gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi veya şeyi iyilik ve değer bakımından üstün, iyi ve seçkin olarak niteler."},{"facet_id":"F002","role":"specialization","statement":"İnsanlarda düzgünlük ve erdemin yanı sıra güzellik ve hoş görünüş yönünü de belirginleştirebilir."},{"facet_id":"F003","role":"extension","statement":"Bir topluluk veya tür içinden düşük nitelikli olmayan üstün ve seçilmiş üyeleri gösterebilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Açık bir karşılaştırma ölçüsü ve ikinci bir karşılaştırılan öğe gerektirir.","collision":"Salt karşılaştırma derecesiyle karışır.","fit":"displacement","loses":"Kişi veya şeyde yerleşik iyilik, düzgünlük ve seçkinlik niteliğini zayıflatır.","preserves":"Bir değer üstünlüğü bulunduğu düşüncesini korur."},"text":"daha iyi"}],"identity_rationale":"Kaynak ifadesi insanı, hayvanı veya başka bir şeyi iyilik, düzgünlük, güzellik ya da seçkinlik bakımından üstün niteleyen kullanımları birlikte verir. Verilen çerçeve bu niteleme çekirdeğini ve sıradanlıktan uzak seçkinlik sınırını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"iyi ve üstün nitelikli"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"üstün, güzel veya seçkin olan"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"üstün veya seçkin kimse ya da şey"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"iyi ve erdemli kişiler"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"üstün, güzel veya seçilmiş olanlar"}],"lexicalization_note":"Tanım yalın niteleme dalına bağlıdır; seçim işlemi veya yalnızca belirli bir söz kalıbında doğan anlam buraya genellenmez.","neighbor_coverage_note":"Bütün aday komşular incelendi. Seçilmiş üst kesim, yüksek nitelik, genel iyilik ve seçme süreciyle kurulan dört sınır yayımlandı; güzellik, övgü, benzersizlik veya cömertlikle yalnızca dolaylı kesişen adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal seçme işlemi bulunmadan da üstün niteliği bildirir; komşu dal ise seçilip ayrılmış üst kesimi daha belirgin biçimde öne çıkarır.","focus_only":"Seçilmiş olmanın yanı sıra iyilik, düzgünlük veya güzellik bakımından üstün niteliği de kapsar.","gloss":"üstün nitelik ile seçilmiş seçkinler","neighbor_only":"Bir topluluğun doruğundaki üyelerin özellikle seçilip ayrılması ve öncü sayılması üzerinde durur.","neighbor_ref":"root_001512/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir topluluk içindeki üstün ve seçkin üyeleri gösterebilir."},{"boundary_match":"partial","distinction":"Odak dal iyilik ve seçkinliği merkez alır; komşu dal soyluluk, incelik ve uç derece gibi daha farklı kalite ölçülerine de açılır.","focus_only":"Düzgünlük ve seçilmişlik yönünü, düşük nitelikten uzak iyi üyeleri kapsar.","gloss":"seçkinlik ile yüksek nitelik","neighbor_only":"İncelik, soyluluk ve bir niteliğin iyi ya da kötü uç noktasına varması gibi ek kapsamlar taşır.","neighbor_ref":"root_000979/B002","relation_type":"near_synonym","shared_zone":"Kişi, hayvan veya şeyin kendi türü içinde iyi ve üstün sayılmasında kesişirler."},{"boundary_match":"partial","distinction":"Odak dal nitelenen varlığın özelliğidir; komşu dal bu tür nitelemelere ölçü olabilen genel olumlu değerdir.","focus_only":"Belirli bir kişi veya şeyde bulunan üstün ve seçkin niteliği bildirir.","gloss":"üstün olan ile genel iyilik","neighbor_only":"Herhangi bir taşıyıcıya bağlı olmadan genel ve arzu edilen iyilik değerini bildirir.","neighbor_ref":"root_000452/B001","relation_type":"near_neighbor","shared_zone":"Üstün sayılan kişi veya şeyin değerlendirilmesi genel iyilik ölçüsüne dayanabilir."},{"boundary_match":"partial","distinction":"Odak dal sonuçta bulunan üstün niteliktir; komşu dal bu niteliğe göre karar verme veya seçme sürecidir.","focus_only":"Bir varlığın seçme gerçekleşmeden de iyi ve üstün olmasını kapsar.","gloss":"seçkin olma ile seçme","neighbor_only":"Daha iyi görüleni ayırıp seçme, seçim hakkı verme veya iyi sonucu isteme işlemini kapsar.","neighbor_ref":"root_000452/B003","relation_type":"near_neighbor","shared_zone":"Bir şeyin üstün görülmesi onu seçmenin ölçüsü olabilir."}],"source_phrase_ar":"رجل خير وامرأة خيرة فاضلة وقوم خيار وأخيار في صلاحها وامرأة خيرة في جمالها وميسمها (maqayis;ayn)؛ رجل خير إذا كان فيه خير ورجل خيار من قوم خيار وأخيار والأخيار خلاف الأشرار (jamhara)؛ الخيرات جمع خيرة وهي الفاضلة من كل شيء (sihah)؛ فيهن مختارات لا رذل فيهن والخير الفاضل المختص بالخير (mufradat)","source_summary":"Kaynakların ortak çerçevesi, kişi veya şeyde iyilik ve üstünlük bulunmasıdır. Bu üstünlük düzgünlük, güzellik veya seçkinlik olarak belirginleşebilir; çoğul kullanımlar iyi ve düşük nitelikten uzak üyeleri gösterebilir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه وصف الإنسان أو الشيء بأنه خير أو خيرة أو خيار أو أخيار، بمعنى الفضل والصلاح والجمال والميسم والاختيار من غير رذالة.","what_is_not_ar":"لا يدخل خير التفضيل المحض إذا كان مجرد صيغة أفعل، ولا أسماء الأعلام والقبائل إلا من جهة التسمية."},"support_links":[]},{"boundary":"Dal, daha iyi olanı belirleme ve seçme çevresinde örgütlenir; hayvanı yuvasından çıkarma anlamındaki ayrı kullanım yalnızca biçim benzerliği taşır.","branch_kind":"mixed_non_bare","branch_ref":"root_000452/B003","candidate_links":[{"candidate_id":"cand_d04c778a5e6e0ee28341","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:2:1","qac_word_ref":"87:17:2","surface_ar":"خَيْرٌ"}],"gloss":"daha iyi olanı seçme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olasılıklar arasından daha iyi görüleni arayıp ayırmayı, seçmeyi ve seçilmiş sonucu bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi için iki olasılıktan daha iyi olanı Yaratıcıdan dileme ve iyi sonucun belirlenmesini isteme anlamını taşır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Seçim hakkını bir başkasına bırakma veya birini seçim bakımından üstün gelmiş sayma gibi ilişki biçimlerini kapsar."}}],"root_ar":"خ ي ر","root_id":"root_000452","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Seçenekler arasından üstün veya daha yararlı görüleni belirleyip alma çekirdeğini anlatan genel kullanımlara uyar.","boundary_detail":"Dal, daha iyi olanı belirleme ve seçme çevresinde örgütlenir; hayvanı yuvasından çıkarma anlamındaki ayrı kullanım yalnızca biçim benzerliği taşır.","branch_image_ar":"طلب الخير بالاختيار والاستخارة","concept_gloss":"daha iyi olanı seçme","contextual_glosses":[{"applicability":"Bir kişiye iki şey arasında karar verme yetkisinin bırakıldığı veya bu yetkinin adlandırıldığı bağlamlara uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Daha iyi olanı arama, seçilmiş sonuç ve iyi sonucu dileme kullanımlarını dışarıda bırakır.","preserves":"Seçenekler arasında karar verebilme yetkisini korur."},"facet_ids":["F003"],"text":"seçim hakkı","usage_role":"contextual"},{"applicability":"İki olasılık arasından kişi için iyi olan sonucun Yaratıcı tarafından belirlenmesinin istendiği bağlama uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel seçme eylemini, seçim hakkını ve seçimde üstün gelmeyi kapsamaz.","preserves":"Kişi için daha iyi olanı isteme yönünü korur."},"facet_ids":["F002"],"text":"iyi sonucu dileme","usage_role":"explanatory"},{"applicability":"Bir kişinin seçim veya karşılaştırma bakımından diğerini geçtiğinin anlatıldığı özel bağlama uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Daha iyi olanı seçme, seçim hakkı ve iyi sonuç isteme alanlarını dışarıda bırakır.","preserves":"Seçim alanındaki üstünlük ilişkisini korur."},"facet_ids":["F003"],"text":"seçimde üstün gelme","usage_role":"contextual"}],"definition":"Birden çok olasılık arasından daha iyi görüleni arayıp ayırma, seçme veya seçim yetkisine sahip olma alanıdır. Belirli kullanımlarda iyi sonucu Yaratıcıdan dileme, seçim hakkını başkasına bırakma ya da seçimde üstün gelme anlamları bu çekirdeğe bağlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olasılıklar arasından daha iyi görüleni arayıp ayırmayı, seçmeyi ve seçilmiş sonucu bildirir."},{"facet_id":"F002","role":"specialization","statement":"Kişi için iki olasılıktan daha iyi olanı Yaratıcıdan dileme ve iyi sonucun belirlenmesini isteme anlamını taşır."},{"facet_id":"F003","role":"associated_use","statement":"Seçim hakkını bir başkasına bırakma veya birini seçim bakımından üstün gelmiş sayma gibi ilişki biçimlerini kapsar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Karar verememe ve tereddüt durumunu anlamın merkezine ekler.","collision":"İki seçenek arasında tartma bildiren komşu alanla karışır.","fit":"displacement","loses":"Daha iyi olanı belirleme, seçme ve seçim yetkisi çekirdeğini kaybeder.","preserves":"Birden çok olasılığın bulunduğunu dolaylı olarak korur."},"text":"kararsızlık"}],"identity_rationale":"Kaynak ifadesi daha iyi olanı arayıp seçme çekirdeğini; seçim hakkı, seçilmiş sonuç, iki seçenekten iyisini dileme, seçimi başkasına bırakma ve seçimde üstün gelme kullanımlarıyla birlikte verir. Dal çerçevesi bu çok parçalı fakat seçim merkezli alanı doğru tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"seçim veya seçim hakkı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"seçim, seçilmiş şey veya seçim sonucu"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"daha iyi olanı arayıp seçme"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"seçmek veya üstün tutmak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"Yaratıcıdan kişi için iyi sonucu dilemek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"Yaratıcının kişi için iyi olanı seçip vermesi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"iki şey arasında seçim hakkını ona bırakmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"seçimde üstün gelmek veya diğerini geçmek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"seçen ya da seçilmiş olan"}],"lexicalization_note":"Tanım yalın seçme çekirdeğiyle söz kalıplarına bağlı seçim hakkı, iyi sonuç dileme ve üstün gelme kullanımlarını ayrı yüzler olarak korur.","neighbor_coverage_note":"Bütün adaylar, aynı kökün diğer dalları da dahil olmak üzere değerlendirildi. Seçkin olanı ayırma, doğruyu arama, iki seçenek arasında tartma ve genel iyilik sınırları yayımlandı; geri kalanlar uzak süreç ortaklığı taşıdı veya hayvanı yuvasından çıkaran ayrı kullanımla yalnızca biçimsel olarak çakıştı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal seçim sürecinin ve yetkisinin daha geniş alanını kapsar; komşu dal seçkin bölümün ayrılıp yeğlenmesini merkez alır.","focus_only":"İyi sonucu dileme, seçim hakkını başkasına bırakma ve seçimde üstün gelme alanlarını da kapsar.","gloss":"seçme ile seçkin olanı ayırma","neighbor_only":"Bir topluluk veya nesne grubunun seçkin bölümünü ayırma ve onu özellikle yeğleme üzerinde yoğunlaşır.","neighbor_ref":"root_000873/B002","relation_type":"near_synonym","shared_zone":"İki dal da seçenekler arasından üstün görüleni ayırıp alma eyleminde buluşur."},{"boundary_match":"partial","distinction":"Odak dal seçimin yapılmasına ve sonucuna uzanır; komşu dal doğruyu araştırma ve ona yönelme aşamasında kalabilir.","focus_only":"Seçim yapmayı, seçim hakkını ve seçilmiş sonucu doğrudan kapsar.","gloss":"daha iyiyi seçme ile doğruyu arama","neighbor_only":"Doğruyu, en uygun yönü veya öncelikli olanı araştırıp ona yönelmeyi kararın önüne çıkarır.","neighbor_ref":"root_000314/B004","relation_type":"near_synonym","shared_zone":"Her ikisi de seçenekler içinde daha doğru veya daha iyi olana yönelmeyi içerir."},{"boundary_match":"partial","distinction":"Odak dal karşılaştırmayı seçimle sonuçlandırır; komşu dal seçenekleri tartmayı anlatır ve zorunlu olarak seçim bildirmez.","focus_only":"Daha iyi görüleni seçerek karara ve seçilmiş sonuca ulaşır.","gloss":"seçme ile iki seçenek arasında tartma","neighbor_only":"İki seçenek arasında hangisinin ağır bastığını tartma veya kararsız kalma sürecini bildirir.","neighbor_ref":"root_000991/B008","relation_type":"near_neighbor","shared_zone":"İki olasılığın karşılaştırılması her iki dalda da bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal iyiliğe göre yapılan eylem ve karardır; komşu dal bu karara ölçü olabilen genel değerdir.","focus_only":"İyi sayılan seçenekler arasında arama, ayırma ve karar verme işlemini bildirir.","gloss":"iyiyi seçme ile iyilik","neighbor_only":"Herhangi bir seçim yapılmadan da var olan genel ve arzu edilen olumlu değeri bildirir.","neighbor_ref":"root_000452/B001","relation_type":"near_neighbor","shared_zone":"Seçimin ölçüsü, bir seçeneğin iyi ve arzu edilir sayılması olabilir."}],"source_phrase_ar":"الخيرة الخيار والاستخارة أن تسأل خير الأمرين لك ويقال خايرت فلانا فخرته وتقول اختر (maqayis)؛ خايرت فلانا فخرته والله يخير للعبد إذا استخاره وهذا وهذه وهؤلاء خيرتي وهو ما تختاره (ayn)؛ الخيار الاسم من الاختيار والخيرة من قولك خار الله لك والاختيار الاصطفياء والاستخارة الخيرة وخيرته بين الشيئين (sihah)؛ الاختيار طلب ما هو خير وفعله واستخار الله العبد فخار له وخايرت فلانا كذا فخرته (mufradat)","source_summary":"Kaynaklar daha iyi olanı arayıp seçme çekirdeğinde birleşir. Seçim hakkı ve seçilmiş şey, iyi sonucu Yaratıcıdan dileme, iki şey arasında yetki verme ve seçimde üstün gelme bu çekirdeğin farklı dilsel gerçekleşmeleridir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الخيار والاختيار والتخير والاستخارة وخار الله لك وخيرته بين شيئين، أي طلب ما هو خير، أو الاصطفاء، أو تفويض الخيار.","what_is_not_ar":"لا يدخل الخيار المعرب بمعنى القثاء، ولا الخيري المعرب، ولا خصوص استخراج الحيوان من جحره إلا في فرعه الخاص."},"support_links":["sup_4f5cd9b273d716085f0d"]},{"boundary":"Çekirdek, sözcüğün malı adlandırmasıdır; çokluk ve övülen yoldan edinilme bazı kullanımların belirgin kısıtıdır, bütün mal kullanımlarına zorunlu şart yapılmaz.","branch_kind":"bare","branch_ref":"root_000452/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:2:1","qac_word_ref":"87:17:2","surface_ar":"خَيْرٌ"}],"gloss":"mal, özellikle çok veya övülen bir yoldan edinilmiş servet","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, kişinin sahip olduğu malı veya serveti adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı açıklamalarda kapsam, çok olan ve övülen bir yoldan edinilmiş mala daraltılır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Miras bırakma ve mala güçlü bağlılık bağlamları bu adlandırmanın örnekleridir."}}],"root_ar":"خ ي ر","root_id":"root_000452","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Malın doğrudan adlandırıldığı, özellikle çokluğu veya övülen bir yoldan edinilmiş oluşunun öne çıktığı kullanımları birlikte karşılar.","boundary_detail":"Çekirdek, sözcüğün malı adlandırmasıdır; çokluk ve övülen yoldan edinilme bazı kullanımların belirgin kısıtıdır, bütün mal kullanımlarına zorunlu şart yapılmaz.","branch_image_ar":"المال المسمى خيرا","concept_gloss":"mal, özellikle çok veya övülen bir yoldan edinilmiş servet","contextual_glosses":[{"applicability":"Sahip olunan veya miras bırakılan varlığın nicelik şartı açıkça öne çıkarılmadan adlandırıldığı bağlamlara uyar.","error_profile":{"adds":"Çokluk veya övülen edinme yolu şartı bulunan bağlamlarda bu şartları taşımayan malları da kapsayabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Sahip olunan ekonomik varlık çekirdeğini korur."},"facet_ids":["F001","F003"],"text":"mal","usage_role":"general"},{"applicability":"Malın çokluğu ve değeri özellikle vurgulandığında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nicelik vurgusu bulunmayan genel mal ve tekil miras varlığı kullanımlarını dışarıda bırakabilir.","preserves":"Çok ve değerli mal yönünü açık biçimde korur."},"facet_ids":["F002"],"text":"servet","usage_role":"contextual"}],"definition":"Malı veya serveti adlandıran kullanımdır; bazı bağlamlarda özellikle çok ya da övülen bir yoldan edinilmiş malı belirtir. Miras bırakılan veya güçlü biçimde sevilen mal da bu adlandırmayla anılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, kişinin sahip olduğu malı veya serveti adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Bazı açıklamalarda kapsam, çok olan ve övülen bir yoldan edinilmiş mala daraltılır."},{"facet_id":"F003","role":"example","statement":"Miras bırakma ve mala güçlü bağlılık bağlamları bu adlandırmanın örnekleridir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Soyut ahlaki değer anlamını merkeze taşır.","collision":"Aynı kökün genel olumlu değer dalıyla karışır.","fit":"displacement","loses":"Ekonomik varlık ve sahip olunan mal çekirdeğini ortadan kaldırır.","preserves":"Malın değerli veya övülen oluşunu çağrıştırabilir."},"text":"iyilik"}],"identity_rationale":"Kaynak ifadesi sözcüğün mal anlamında kullanılmasını açıkça destekler; ancak kapsam bir anlatımda genel malı gösterirken başka anlatımlarda çokluk ve övülen bir edinme yolu şartıyla daraltılır. Dal korunabilir, fakat bu değişken sınır tanımda açıkça belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"mal, özellikle çok veya iyi yoldan edinilmiş servet"}],"lexicalization_note":"Tanım yalın sözcüğün malı adlandıran anlamına bağlıdır; genel iyilik veya cömertlik anlamları malın kendisiyle özdeşleştirilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Genel iyilik, cömertçe verme ve mal üzerinde işlem yapma karşılaştırmaları dal sınırını en açık biçimde gösterdi; çokluk, savurganlık, gecikme veya yön değiştirme gibi daha uzak bağlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir ekonomik varlık türünü adlandırır; komşu dal ise bu varlığın yalnızca bir örneği olabildiği genel olumlu değerdir.","focus_only":"Doğrudan sahip olunan malı ve serveti adlandırır.","gloss":"mal ile genel iyilik","neighbor_only":"Mal dışında da arzu edilen her türlü olumlu değeri ve iyiliği kapsar.","neighbor_ref":"root_000452/B001","relation_type":"near_neighbor","shared_zone":"Değerli veya yararlı mal genel iyilik düşüncesiyle ilişkilendirilebilir."},{"boundary_match":"partial","distinction":"Odak dal verilen ya da elde tutulan varlıktır; komşu dal o varlığı verme niteliği veya verme sonucudur.","focus_only":"Kişinin elinde bulunan malı, verilmemiş olsa bile kapsar.","gloss":"servet ile cömertçe verme","neighbor_only":"Verme niteliğini, armağanı ve kişideki cömertlik bolluğunu bildirir.","neighbor_ref":"root_000452/B005","relation_type":"near_neighbor","shared_zone":"Mal, armağan ve cömertlik eyleminin konusu olabilir."},{"boundary_match":"field_only","distinction":"Odak dal bir varlık adıdır; komşu dal bu varlık üzerinde gerçekleştirilen tüketme, harcama veya alma eylemidir.","focus_only":"Malın kendisini ve bazı kullanımlarda onun çokluk niteliğini adlandırır.","gloss":"mal ile malı tüketme veya alma","neighbor_only":"Malı tüketme, harcama, ele geçirme veya başkasının malından yararlanma eylemlerini bildirir.","neighbor_ref":"root_000043/B004","relation_type":"same_field","shared_zone":"Her iki dalın ortak katılımcısı ekonomik varlık olan maldır."}],"source_phrase_ar":"إن ترك خيرا أي مالا (sihah;mufradat)؛ لا يقال للمال خير حتى يكون كثيرا ومن مكان طيب (mufradat)؛ وإنه لحب الخير لشديد أي المال الكثير (mufradat)؛ ما كان مجموعا من المال من وجه محمود (mufradat)","source_summary":"Kullanım malı göstermekle birlikte açıklamaların bir bölümü kapsamı çokluk ve övülen bir edinme yolu şartıyla daraltır. Miras bırakılan veya güçlü biçimde sevilen mal da ortak claim içinde örneklenir.","sources":["SI","MU"],"what_is_ar":"يدخل فيه إطلاق الخير على المال، وبخاصة المال الكثير أو المجتمع من وجه محمود، وما يوصى به أو ينفق.","what_is_not_ar":"لا يدخل كل مال مطلقا عند من قيده بالكثرة أو بالوجه المحمود، ولا يدخل الخير الأخلاقي العام إلا بوصفه أصلا أوسع."},"support_links":[]},{"boundary":"Bu dal malın kendisini değil, cömertlik niteliğini ve onun armağan ya da verme biçimindeki sonucunu bildirir.","branch_kind":"bare","branch_ref":"root_000452/B005","candidate_links":[{"candidate_id":"cand_6349af299a067939a02c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:2:1","qac_word_ref":"87:17:2","surface_ar":"خَيْرٌ"}],"gloss":"cömertlik ve armağan verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişide bulunan cömertlik ve bolca verme niteliğini bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Cömertliğin somut sonucu olan armağanı, bağışı veya verme eylemini gösterebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişide iyiliğin çok olması, onun cömert ve yararlı oluşunun göstergesi olarak kullanılır."}}],"root_ar":"خ ي ر","root_id":"root_000452","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem kişideki verme niteliğini hem de bu niteliğin armağan veya bağış olarak gerçekleşmesini kapsayan genel karşılıktır.","boundary_detail":"Bu dal malın kendisini değil, cömertlik niteliğini ve onun armağan ya da verme biçimindeki sonucunu bildirir.","branch_image_ar":"الكرم والهبة","concept_gloss":"cömertlik ve armağan verme","contextual_glosses":[{"applicability":"Bir kişinin bolca veren ve iyiliği çok olan niteliğinin öne çıktığı bağlamlara uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir armağanı veya somut verme sonucunu doğrudan adlandırmaz.","preserves":"Kişideki verme isteği ve iyilik bolluğu niteliğini korur."},"facet_ids":["F001","F003"],"text":"cömertlik","usage_role":"general"},{"applicability":"Cömertliğin somut olarak verilen bir şey biçiminde gerçekleştiği bağlamlara uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin sürekli cömertlik niteliğini ve genel iyilik bolluğunu kapsamaz.","preserves":"Verme sonucunda alıcıya ulaşan somut yararı korur."},"facet_ids":["F002"],"text":"armağan","usage_role":"contextual"}],"definition":"Cömert olma niteliği ve bunun armağan ya da verme olarak görünmesidir; kişi için kullanıldığında onda iyiliğin ve verme isteğinin bol bulunduğunu da bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişide bulunan cömertlik ve bolca verme niteliğini bildirir."},{"facet_id":"F002","role":"extension","statement":"Cömertliğin somut sonucu olan armağanı, bağışı veya verme eylemini gösterebilir."},{"facet_id":"F003","role":"associated_use","statement":"Bir kişide iyiliğin çok olması, onun cömert ve yararlı oluşunun göstergesi olarak kullanılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Elde tutulan ekonomik varlığı anlamın merkezine ekler.","collision":"Aynı kökün mal ve servet dalıyla karışır.","fit":"displacement","loses":"Cömertlik niteliğini, verme eylemini ve armağan sonucunu kaybeder.","preserves":"Verilebilecek malın bolluğunu dolaylı biçimde çağrıştırır."},"text":"servet"}],"identity_rationale":"Kaynak ifadesi cömertlik niteliğini, armağanı ve vermeyi aynı dalda birleştirir; ayrıca kişide iyiliğin çok oluşunu bu niteliğin göstergesi sayar. Verilen dal çerçevesi, sahip olunan maldan farklı olarak verme ve bolluk yönünü doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"cömertlik, armağan ve verme"}],"lexicalization_note":"Tanım yalın cömertlik ve armağan alanıyla sınırlıdır; yalnızca belirli bir nesneye sahip olma durumu veya genel iyilik bütünü buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Cömertçe verme, bol bağış, karşılıksız iyilik, esirgeme karşıtlığı ve malın kendisiyle ayrım yayımlandı; yalnızca genel değer, kişisel üstünlük veya uzak bolluk çağrışımı taşıyan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal nitelik ile armağan sonucunu birlikte kapsar; komşu dal verme davranışının sürekliliğini ve bolluğunu daha belirgin işler.","focus_only":"Armağanın kendisini ve kişide genel iyiliğin çok oluşunu da adlandırabilir.","gloss":"cömertlik ve bolca verme","neighbor_only":"El açıklığını ve arkadaş çevresine bolca verme davranışını daha eylemli biçimde öne çıkarır.","neighbor_ref":"root_001487/B008","relation_type":"near_synonym","shared_zone":"İki dal da cömertlik, armağan, yararlı davranış ve bolca verme alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal armağan ve genel iyilik bolluğuna uzanır; komşu dal çeşitli değerleri bolca bağışlama davranışını daha açık sınırlar.","focus_only":"Armağanı ve kişide iyiliğin bol oluşunu bağımsız anlamlar olarak da kapsar.","gloss":"cömertlik ile bol bağış","neighbor_only":"Malın yanı sıra bilginin de bolca verilmesini ve bağışta geniş davranmayı açıkça kapsar.","neighbor_ref":"root_000274/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de eli açıklık ve elindekini başkasına verme niteliğini anlatır."},{"boundary_match":"partial","distinction":"Odak dal genel cömertlik ve armağandır; komşu dal verilmesi zorunlu olmayan fazladan iyiliği ve karşılıksız yararı özellikle belirtir.","focus_only":"Cömertliği kişinin niteliği ve armağanı doğrudan adlandıracak biçimde kapsar.","gloss":"cömertlik ile karşılıksız iyilik","neighbor_only":"Hak edilmiş bir borç olmadan fazladan iyilikte bulunma ve lütufta bulunma koşulunu öne çıkarır.","neighbor_ref":"root_001163/B003","relation_type":"near_synonym","shared_zone":"Armağan verme ve başkasına yarar sağlama iki dalın ortak alanıdır."},{"boundary_match":"opposed","distinction":"Odak dal verme yönündeki olumlu kutuptur; komşu dal aynı eksende vermeme ve engelleme yönündeki karşıt kutuptur.","focus_only":"Elindekini verme, armağan etme ve cömert davranma yönünü taşır.","gloss":"verme ile esirgeme","neighbor_only":"Vermeyi engelleme, eli sıkı davranma ve iyiliği esirgeme yönünü taşır.","neighbor_ref":"root_001448/B001","relation_type":"antonym","shared_zone":"İki dal, kişinin elindeki yararı başkasına verip vermemesi ekseninde karşılaşır."}],"source_phrase_ar":"والخير الكرم (maqayis)؛ الخير الهبة (ayn)؛ رجل ذو خير إذا كان كثير الخير (jamhara)؛ الخير بالكسر الكرم (sihah)","source_summary":"Kaynaklar cömertlik, armağan ve verme anlamlarını ortak bir alanda toplar. Bir kişide iyiliğin çok olduğunun söylenmesi de cömertlik ve yarar bolluğunun kişiye yüklenen niteliğidir.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه الخير بمعنى الكرم، والهبة والعطاء، وكثرة الخير في الشخص.","what_is_not_ar":"لا يدخل المال المملوك بمجرده إلا إذا نظر إليه من جهة العطاء والكرم."},"support_links":["sup_494adb4b482277e4a4a1"]},{"boundary":"Bu anlam yalnızca hayvan, yuva, bir geçidin engellenmesi ve başka çıkıştan çıkma bileşenlerini taşıyan özel kullanıma aittir; iyi olanı seçme anlamına genellenmez.","branch_kind":"collocation","branch_ref":"root_000452/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:2:1","qac_word_ref":"87:17:2","surface_ar":"خَيْرٌ"}],"gloss":"bir geçidi tıkayıp hayvanı yuvasından çıkarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hayvanın yuvasındaki bir geçide engel yerleştirerek onu başka bir çıkışa yöneltme işlemini bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlemin katılımcısı sırtlan veya çöl sıçanı, aracı ise geçidi tıkayan çubuk ya da benzeri bir engeldir."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yuva geçidinin engellenmesi sonucunda hayvanın öteki geçitten çıkması işlemin kurucu sonucudur."}}],"root_ar":"خ ي ر","root_id":"root_000452","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sırtlan veya çöl sıçanının yuvasındaki bir yolun engellenip hayvanın başka çıkıştan çıkarıldığı özel işlemi tam olarak karşılar.","boundary_detail":"Bu anlam yalnızca hayvan, yuva, bir geçidin engellenmesi ve başka çıkıştan çıkma bileşenlerini taşıyan özel kullanıma aittir; iyi olanı seçme anlamına genellenmez.","branch_image_ar":"استدراج الحيوان من جحره","concept_gloss":"bir geçidi tıkayıp hayvanı yuvasından çıkarma","contextual_glosses":[{"applicability":"Yuvadaki bir geçidin kapatılmasıyla hayvanın alternatif çıkışa yöneltildiği anlatımda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çubuk veya benzeri engelin belirli bir yuva geçidine yerleştirilmesi aşamasını açıkça söylemez.","preserves":"Hayvanın başka bir çıkışa yöneltilmesi ve dışarı çıkarılması sonucunu korur."},"facet_ids":["F001","F003"],"text":"hayvanı öteki çıkışa sürme","usage_role":"explanatory"}],"definition":"Sırtlanı veya çöl sıçanını yuvasındaki bir geçide çubuk ya da başka bir engel koyarak başka bir çıkıştan dışarı çıkarmaktır. İşlem, bir yolu kapatma ile hayvanın alternatif yola yönelmesi sırasını zorunlu olarak içerir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hayvanın yuvasındaki bir geçide engel yerleştirerek onu başka bir çıkışa yöneltme işlemini bildirir."},{"facet_id":"F002","role":"specialization","statement":"İşlemin katılımcısı sırtlan veya çöl sıçanı, aracı ise geçidi tıkayan çubuk ya da benzeri bir engeldir."},{"facet_id":"F003","role":"core","statement":"Bir yuva geçidinin engellenmesi sonucunda hayvanın öteki geçitten çıkması işlemin kurucu sonucudur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İki olasılık arasından iyi olanı isteme düşüncesini ekler.","collision":"Aynı kökün seçme ve iyi sonucu isteme dalıyla karışır.","fit":"displacement","loses":"Hayvanı, yuvayı, engel koymayı ve başka çıkıştan çıkarmayı bütünüyle kaybeder.","preserves":"Aynı kökteki başka bir kullanımın çağrışımını taşır."},"text":"iyi sonucu dileme"}],"identity_rationale":"Kaynak ifadesi, sırtlan veya çöl sıçanının yuvasındaki bir geçide çubuk ya da engel yerleştirip hayvanı başka bir çıkıştan çıkarmayı açık bir işlem dizisiyle anlatır. Verilen çerçeve hem aracı hem yer değişimini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"sırtlanı, yuvasının bir geçidini tıkayarak başka çıkıştan çıkarma"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"çöl sıçanını, yuvasının bir geçidini tıkayarak başka çıkıştan çıkarma"}],"lexicalization_note":"Tanım yalnızca sırtlan veya çöl sıçanıyla kurulan özel kullanıma bağlıdır; bu işlem yalın kökün genel anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar ve aynı kökün diğer dalları değerlendirildi. Çıkış geçidi, yuva içindeki hayvan hareketi, genel avlanma ve yuvanın kendisiyle kurulan sınırlar yayımlandı; tuzak, hayvan adı veya toprağa gizlenme gibi yalnızca sahneyi paylaşan adaylar elendi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal geçit üzerinde yapılan bir işlem ve bunun sonucudur; komşu dal işlemin gerçekleştiği geçidin kendisini adlandırır.","focus_only":"Yuvanın bir geçidini engelleyerek hayvanın hareketini ve çıkışını yönlendirir.","gloss":"hayvanı çıkarmak ile çıkış geçidi","neighbor_only":"İki ucu bulunan geçidi ve çöl sıçanının kullandığı giriş çıkış yolunu adlandırır.","neighbor_ref":"root_001537/B003","relation_type":"near_neighbor","shared_zone":"İki dal da çöl sıçanının yer altı yuvası ve alternatif çıkış düzeniyle ilgilidir."},{"boundary_match":"field_only","distinction":"Odak dal dışarı çıkarma amacı taşıyan insan müdahalesidir; komşu dal hayvanın boynunu sokma veya çıkarma biçimindeki hareketidir.","focus_only":"Bir geçidi tıkayarak hayvanı başka çıkıştan bütünüyle dışarı yöneltir.","gloss":"yuvadan çıkarma ile boyun hareketi","neighbor_only":"Hayvanın boynunu çamura veya yuva toprağına sokması ya da oradan çıkarması hareketini anlatır.","neighbor_ref":"root_001053/B007","relation_type":"same_field","shared_zone":"Her iki dal hayvanın toprak veya yuva içindeki yönlendirilmiş hareketini konu alır."},{"boundary_match":"thematic_only","distinction":"Odak dal tek ve ayrıntılı bir çıkarma tekniğidir; komşu dal çok sayıda yöntem ve aracı kapsayan genel avlanma etkinliğidir.","focus_only":"Belirli yuva düzeninde bir geçidi kapatıp hayvanı başka çıkıştan çıkarma yöntemini bildirir.","gloss":"yuvadan çıkarma yöntemi ile avlanma","neighbor_only":"Sahipsiz ve yakalanması güç hayvanı arama, yakalama, araç kullanma ve avlanma alanının tamamını kapsar.","neighbor_ref":"root_000896/B001","relation_type":"thematic","shared_zone":"Hayvanı saklandığı yerden çıkarma işlemi daha geniş bir avlanma senaryosunda kullanılabilir."},{"boundary_match":"field_only","distinction":"Odak dal yuvada gerçekleştirilen yönlendirme işlemidir; komşu dal bu işlemin mekânı olan yuva yapısı veya toprağıdır.","focus_only":"Yuvaya engel koyup içindeki hayvanı alternatif çıkışa sevk eden eylemi anlatır.","gloss":"yuva üzerinde işlem ile yuvanın kendisi","neighbor_only":"Çöl sıçanının yuvasını veya yuva ağzına yığdığı toprağı adlandırır.","neighbor_ref":"root_000605/B003","relation_type":"same_field","shared_zone":"İki dal da çöl sıçanının yuvasını ve yuva ağzını ortak sahne olarak paylaşır."}],"source_phrase_ar":"استخاره الضبع وهو أن تجعل خشبة في ثقبة بيتها حتى تخرج من مكان إلى آخر (maqayis)؛ يستخير الضبع واليربوع إذا جعل في موضع النافقاء فخرج من القاصعاء (ayn)","source_summary":"Kaynakların ortak anlatımı, sırtlan veya çöl sıçanının yuvasındaki bir geçidin çubuk ya da engelle kapatılması ve hayvanın bunun sonucunda başka bir çıkıştan dışarı çıkmasıdır.","sources":["MQ","AY"],"what_is_ar":"يدخل فيه استخارة الضبع أو اليربوع بجعل خشبة أو نحوها في موضع من جحره حتى يخرج من موضع آخر.","what_is_not_ar":"لا يدخل طلب الخير في الأمرين إلا من جهة اللفظ المشترك والاستخارة العامة."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["87:17:1"],"branch_refs":[],"candidate_id":"cand_97caf1deec17aa46ef32","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:17:1:bound-subject-entry","source_type":"word_analysis","support_ids":["sup_032cdaa9ea6ad38f46fb","sup_e1989ea2262371cc3d62"],"title":"bound entry into the subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:1","qac_refs":["87:17:1:1"],"status":"accepted"}},{"anchor_refs":["87:17:1"],"branch_refs":[],"candidate_id":"cand_ec74c5baf99b91c54900","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:17:1:corrective-boundary-bridge","source_type":"word_analysis","support_ids":["sup_032cdaa9ea6ad38f46fb","sup_178bc90b02a5c51bb7fc"],"title":"boundary bridge to the verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:1","qac_refs":["87:17:1:1"],"status":"accepted"}},{"anchor_refs":["87:17:1"],"branch_refs":[],"candidate_id":"cand_1febb7cefa91dd5c24a4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:17:1:verbal-action-to-nominal-scale","source_type":"word_analysis","support_ids":["sup_032cdaa9ea6ad38f46fb","sup_a4d550b5aec4a719a2cc"],"title":"from action to stable scale","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:1","qac_refs":["87:17:1:1"],"status":"accepted"}},{"anchor_refs":["87:17:2"],"branch_refs":[],"candidate_id":"cand_911d10496443270e0878","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:17:2:boundary-counter-scale","source_type":"word_analysis","support_ids":["sup_70ee3535458b4ac1cd0e","sup_bd74d7d067a2444c06f8"],"title":"boundary hinge into counter-scale","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:2","qac_refs":["87:17:1:2","87:17:1:3"],"status":"accepted"}},{"anchor_refs":["87:17:2"],"branch_refs":[],"candidate_id":"cand_daa62fa1cc28d28eaea0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:17:2:definite-counterpart-to-near-life","source_type":"word_analysis","support_ids":["sup_53d2d7d47b74005c88c4","sup_bd74d7d067a2444c06f8"],"title":"overt counterpart to the near life","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:2","qac_refs":["87:17:1:2","87:17:1:3"],"status":"accepted"}},{"anchor_refs":["87:17:2"],"branch_refs":[],"candidate_id":"cand_749a6208c90a4bfe3a26","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:17:2:formula-and-horizon-links","source_type":"word_analysis","support_ids":["sup_98d5fda169c64071524a","sup_bd74d7d067a2444c06f8"],"title":"finality linked with lasting value","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:2","qac_refs":["87:17:1:2","87:17:1:3"],"status":"accepted"}},{"anchor_refs":["87:17:2"],"branch_refs":[],"candidate_id":"cand_ed880747695cec5411e7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:17:2:posteriority-as-value-horizon","source_type":"word_analysis","support_ids":["sup_0cf46e6c9e905ec87e9e","sup_bd74d7d067a2444c06f8"],"title":"posteriority becomes value horizon","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:2","qac_refs":["87:17:1:2","87:17:1:3"],"status":"accepted"}},{"anchor_refs":["87:17:2"],"branch_refs":[],"candidate_id":"cand_5a44ce34d34fa849dfb2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:17:2:realm-form-totality","source_type":"word_analysis","support_ids":["sup_7a7c5e1497b0e48e544f","sup_bd74d7d067a2444c06f8"],"title":"singular realm-form totality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:2","qac_refs":["87:17:1:2","87:17:1:3"],"status":"accepted"}},{"anchor_refs":["87:17:2"],"branch_refs":[],"candidate_id":"cand_a60489ca74f76fe9e0f1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:17:2:subject-with-two-predicates","source_type":"word_analysis","support_ids":["sup_bd74d7d067a2444c06f8","sup_ca0fd3e4b914a16a5de6"],"title":"known subject carrying two predicates","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:2","qac_refs":["87:17:1:2","87:17:1:3"],"status":"accepted"}},{"anchor_refs":["87:17:3"],"branch_refs":[],"candidate_id":"cand_f220f6bf613ef425c660","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"87:17:3:choice-correction","source_type":"word_analysis","support_ids":["sup_1c309b1d5695c3588628","sup_530f8eeded7986c410ce"],"title":"goodness as corrected choice","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:3","qac_refs":["87:17:2:1"],"status":"accepted"}},{"anchor_refs":["87:17:3"],"branch_refs":[],"candidate_id":"cand_5cde25f14d14e754e2bd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"87:17:3:corrective-value-node","source_type":"word_analysis","support_ids":["sup_1c309b1d5695c3588628","sup_d393d7dd4326d1c9baca"],"title":"main reversal node","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:3","qac_refs":["87:17:2:1"],"status":"accepted"}},{"anchor_refs":["87:17:3"],"branch_refs":[],"candidate_id":"cand_96934cd178e333c6ed68","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"87:17:3:qualitative-value-predicate","source_type":"word_analysis","support_ids":["sup_1c309b1d5695c3588628","sup_6cf40be3a5313f0b5cc6"],"title":"qualitative value predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:3","qac_refs":["87:17:2:1"],"status":"accepted"}},{"anchor_refs":["87:17:3"],"branch_refs":[],"candidate_id":"cand_c1130df629b05193dbc9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"87:17:3:valuation-formula-and-echoes","source_type":"word_analysis","support_ids":["sup_1c309b1d5695c3588628","sup_8a88e891b855fe1272d0"],"title":"valuation formula echoes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:3","qac_refs":["87:17:2:1"],"status":"accepted"}},{"anchor_refs":["87:17:3"],"branch_refs":[],"candidate_id":"cand_b49ce50a659e84e75d78","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"87:17:3:value-before-endurance","source_type":"word_analysis","support_ids":["sup_1c309b1d5695c3588628","sup_5011ea0a7ad0c103bcaa"],"title":"value before endurance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:3","qac_refs":["87:17:2:1"],"status":"accepted"}},{"anchor_refs":["87:17:3"],"branch_refs":[],"candidate_id":"cand_425777531dcc1a9a0e16","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"87:17:3:value-not-material-good","source_type":"word_analysis","support_ids":["sup_1c309b1d5695c3588628","sup_b8b677e492ca115c87bb"],"title":"worth, not material wealth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:3","qac_refs":["87:17:2:1"],"status":"accepted"}},{"anchor_refs":["87:17:4"],"branch_refs":[],"candidate_id":"cand_6e7917820fcd7a5d95ac","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:17:4:bound-continuation-sound","source_type":"word_analysis","support_ids":["sup_7704a59508a1c0327b2f","sup_e66625e93c36cf8026ff"],"title":"bound continuation into endurance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:4","qac_refs":["87:17:3:1"],"status":"accepted"}},{"anchor_refs":["87:17:4"],"branch_refs":[],"candidate_id":"cand_74f9f6ba179b9c5cc5f1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:17:4:coordinated-predicate-link","source_type":"word_analysis","support_ids":["sup_3b3877bc248e31128eb7","sup_e66625e93c36cf8026ff"],"title":"same-subject predicate link","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:4","qac_refs":["87:17:3:1"],"status":"accepted"}},{"anchor_refs":["87:17:4"],"branch_refs":[],"candidate_id":"cand_fe0acc0ab1410acea5c7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:17:4:double-connector-frame","source_type":"word_analysis","support_ids":["sup_279d8ec33dcc88249877","sup_e66625e93c36cf8026ff"],"title":"second connector in the verse frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:4","qac_refs":["87:17:3:1"],"status":"accepted"}},{"anchor_refs":["87:17:5"],"branch_refs":[],"candidate_id":"cand_3e74b28a1d84f118b404","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000142"],"scope":"focus_ayah","source_local_id":"87:17:5:adjective-not-preserving-verb","source_type":"word_analysis","support_ids":["sup_4615b2a162ab5247d4d4","sup_debd5dafca526ba95bba"],"title":"comparative adjective, not preserving verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:5","qac_refs":["87:17:3:2"],"status":"accepted"}},{"anchor_refs":["87:17:5"],"branch_refs":[],"candidate_id":"cand_41125213320c114779d5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000142"],"scope":"focus_ayah","source_local_id":"87:17:5:coequal-second-predicate","source_type":"word_analysis","support_ids":["sup_5e885edbaf0199f7e0bc","sup_debd5dafca526ba95bba"],"title":"coequal second predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:5","qac_refs":["87:17:3:2"],"status":"accepted"}},{"anchor_refs":["87:17:5"],"branch_refs":[],"candidate_id":"cand_353316e1052d5801215a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000142"],"scope":"focus_ayah","source_local_id":"87:17:5:comparative-endurance-against-near-life","source_type":"word_analysis","support_ids":["sup_5b5aef825aec97736bd6","sup_debd5dafca526ba95bba"],"title":"comparative endurance against the near life","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:5","qac_refs":["87:17:3:2"],"status":"accepted"}},{"anchor_refs":["87:17:5"],"branch_refs":[],"candidate_id":"cand_b35ca2b6a7b37f930943","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000142"],"scope":"focus_ayah","source_local_id":"87:17:5:compressed-comparator","source_type":"word_analysis","support_ids":["sup_debd5dafca526ba95bba","sup_e99e2bedfe79dc5c448b"],"title":"omitted comparator kept active","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:5","qac_refs":["87:17:3:2"],"status":"accepted"}},{"anchor_refs":["87:17:5"],"branch_refs":[],"candidate_id":"cand_0cc0a917fadaebe7f3d2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000142"],"scope":"focus_ayah","source_local_id":"87:17:5:first-last-and-scroll-horizon","source_type":"word_analysis","support_ids":["sup_95cb198a79b2343746c5","sup_debd5dafca526ba95bba"],"title":"first-last and scroll horizon","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:5","qac_refs":["87:17:3:2"],"status":"accepted"}},{"anchor_refs":["87:17:5"],"branch_refs":[],"candidate_id":"cand_10f7ce4107d4b1c70268","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000142"],"scope":"focus_ayah","source_local_id":"87:17:5:maxim-formula-and-intertexts","source_type":"word_analysis","support_ids":["sup_387749964fa22e65b43a","sup_debd5dafca526ba95bba"],"title":"formulaic enduring verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:5","qac_refs":["87:17:3:2"],"status":"accepted"}},{"anchor_refs":["87:17:5"],"branch_refs":[],"candidate_id":"cand_c74a90e2e6fea0a30a52","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000142"],"scope":"focus_ayah","source_local_id":"87:17:5:rare-finality-endurance-pair","source_type":"word_analysis","support_ids":["sup_debd5dafca526ba95bba","sup_ecde79e8228fb598daa7"],"title":"weighted finality-endurance pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:5","qac_refs":["87:17:3:2"],"status":"accepted"}},{"anchor_refs":["87:17:5"],"branch_refs":[],"candidate_id":"cand_557d7252c3869c3b3902","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000142"],"scope":"focus_ayah","source_local_id":"87:17:5:remaining-after-loss-pressure","source_type":"word_analysis","support_ids":["sup_7d1a5c0478bb6bea7f45","sup_debd5dafca526ba95bba"],"title":"remaining after loss","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:5","qac_refs":["87:17:3:2"],"status":"accepted"}},{"anchor_refs":["87:17:5"],"branch_refs":[],"candidate_id":"cand_3cd70a0a86b93155e5a8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000142"],"scope":"focus_ayah","source_local_id":"87:17:5:sound-and-closure","source_type":"word_analysis","support_ids":["sup_7c6f836bcf5e37e02934","sup_debd5dafca526ba95bba"],"title":"audible landing on lastingness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:17:5","qac_refs":["87:17:3:2"],"status":"accepted"}},{"anchor_refs":["87:17:1"],"branch_refs":[],"candidate_id":"cand_55d954bcd48f318e30ad","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000019"],"scope":"focus_ayah","source_local_id":"87:17:1:3","source_type":"qac_morpheme","support_ids":["sup_9d6003c390642606e781"],"title":"QAC root occurrence: ء خ ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:17:2"],"branch_refs":[],"candidate_id":"cand_4c3d4ea3b0a526268584","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"87:17:2:1","source_type":"qac_morpheme","support_ids":["sup_9026778350e07a7deec3"],"title":"QAC root occurrence: خ ي ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:17:3"],"branch_refs":[],"candidate_id":"cand_7affe1ca0dab9307e5a6","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000142"],"scope":"focus_ayah","source_local_id":"87:17:3:2","source_type":"qac_morpheme","support_ids":["sup_c991ece7bcf5a9687426"],"title":"QAC root occurrence: ب ق ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:17"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:17","branch_refs":["root_000019/B001","root_000142/B001","root_000452/B001"],"candidate_id":"cand_943aa477973aad770107","commentary_obligation":"review","hft_ref":"hft_22e459b00a659e633b3a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b-qualified-endurance","source_type":"hft","support_ids":["sup_1fd91e24ee29a5f37fb2"],"title":"b-qualified-endurance","trust":"legacy_unbound"},{"anchor_refs":["87:17"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:17","branch_refs":["root_000019/B002","root_000142/B004","root_000452/B003"],"candidate_id":"cand_d04c778a5e6e0ee28341","commentary_obligation":"review","hft_ref":"hft_4860c5b9de2b58d233d4","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b-deferred-reserve","source_type":"hft","support_ids":["sup_4f5cd9b273d716085f0d"],"title":"b-deferred-reserve","trust":"legacy_unbound"},{"anchor_refs":["87:17"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:17","branch_refs":["root_000019/B001","root_000142/B003","root_000452/B005"],"candidate_id":"cand_6349af299a067939a02c","commentary_obligation":"review","hft_ref":"hft_eb564036a0042adf0975","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b-preserving-beneficence","source_type":"hft","support_ids":["sup_494adb4b482277e4a4a1"],"title":"b-preserving-beneficence","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:17:1:1","qac_word_ref":"87:17:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"87:17:1:2","qac_word_ref":"87:17:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"آخِر","morph_features":"STEM|POS:N|LEM:A^xir|ROOT:Axr|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:1:3","qac_word_ref":"87:17:1","root_ar":"ء خ ر","surface_ar":"ءَاخِرَةُ"},{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:2:1","qac_word_ref":"87:17:2","root_ar":"خ ي ر","surface_ar":"خَيْرٌ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:17:3:1","qac_word_ref":"87:17:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَبْقَىٰٓ","morph_features":"STEM|POS:N|LEM:>aboqaY`^|ROOT:bqy|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:3:2","qac_word_ref":"87:17:3","root_ar":"ب ق ي","surface_ar":"أَبْقَىٰٓ"}],"word_analysis_qac_refs":[["87:17:1:1"],["87:17:1:2","87:17:1:3"],["87:17:2:1"],["87:17:3:1"],["87:17:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["87:17:1","87:17:2","87:17:3","87:17:4","87:17:5"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:17:1:1","qac_word_ref":"87:17:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"87:17:1:2","qac_word_ref":"87:17:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"آخِر","morph_features":"STEM|POS:N|LEM:A^xir|ROOT:Axr|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:1:3","qac_word_ref":"87:17:1","root_ar":"ء خ ر","surface_ar":"ءَاخِرَةُ"},{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:2:1","qac_word_ref":"87:17:2","root_ar":"خ ي ر","surface_ar":"خَيْرٌ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:17:3:1","qac_word_ref":"87:17:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَبْقَىٰٓ","morph_features":"STEM|POS:N|LEM:>aboqaY`^|ROOT:bqy|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:17:3:2","qac_word_ref":"87:17:3","root_ar":"ب ق ي","surface_ar":"أَبْقَىٰٓ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["87:17:1:1"],["87:17:1:2","87:17:1:3"],["87:17:2:1"],["87:17:3:1"],["87:17:3:2"]],"word_analysis_refs":["87:17:1","87:17:2","87:17:3","87:17:4","87:17:5"],"word_rows":[{"analysis_record_ref":"87:17:1","analytic_gloss_range_en":"initial conjunctive bridge that carries the prior preference statement into a nominal counter-verdict rather than opening an isolated maxim","analytic_root_gloss_range_en":null,"qac_refs":["87:17:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"87:17:2","analytic_gloss_range_en":"the definite final realm as a known, whole counterpart to the near life of 87:16, carrying posteriority into an evaluative horizon","analytic_root_gloss_range_en":"coming after, delay, posteriority, lastness, and finality; local grammar selects the eschatological final-realm noun while preserving the pressure that what comes later becomes the judging horizon","qac_refs":["87:17:1:2","87:17:1:3"],"root":{"arabic":"أ خ ر","transliteration":"ʾ-kh-r"},"surface":{"arabic":"ٱلْءَاخِرَةُ","transliteration":"al-ākhiratu"}},{"analysis_record_ref":"87:17:3","analytic_gloss_range_en":"qualitative comparative predicate of superior worth and preferability, selected against the prior near-life preference and not the material-wealth branch","analytic_root_gloss_range_en":"goodness, excellence, choice-worthiness, choosing the better, benefit, beneficence, and a wealth-as-good branch; local predicate grammar selects superior value and true preferability","qac_refs":["87:17:2:1"],"root":{"arabic":"خ ي ر","transliteration":"kh-y-r"},"surface":{"arabic":"خَيْرٌۭ","transliteration":"khayrun"}},{"analysis_record_ref":"87:17:4","analytic_gloss_range_en":"coordinating connector between the two predicates, making endurance an attached continuation of the same evaluative act rather than a separate clause","analytic_root_gloss_range_en":null,"qac_refs":["87:17:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"87:17:5","analytic_gloss_range_en":"comparative predicate meaning more enduring or more able to remain, coordinated with superior worth and measured against the near life supplied by 87:16","analytic_root_gloss_range_en":"remaining, persisting, surviving after loss, residue, sparing, reserve, and watching/waiting branches; local form selects comparative endurance while the survival-after-loss pressure remains relevant","qac_refs":["87:17:3:2"],"root":{"arabic":"ب ق ي","transliteration":"b-q-y"},"surface":{"arabic":"أَبْقَىٰٓ","transliteration":"abqā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["87:17"],"branch_refs":["root_000019/B001","root_000142/B001","root_000452/B001"],"candidate_id":"cand_943aa477973aad770107","evidence_scope":"focus_ayah","hft_ref":"hft_22e459b00a659e633b3a","item_id":"b-qualified-endurance","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b-qualified-endurance","support_id":"sup_1fd91e24ee29a5f37fb2"},{"anchor_refs":["87:17"],"branch_refs":["root_000019/B002","root_000142/B004","root_000452/B003"],"candidate_id":"cand_d04c778a5e6e0ee28341","evidence_scope":"focus_ayah","hft_ref":"hft_4860c5b9de2b58d233d4","item_id":"b-deferred-reserve","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b-deferred-reserve","support_id":"sup_4f5cd9b273d716085f0d"},{"anchor_refs":["87:17"],"branch_refs":["root_000019/B001","root_000142/B003","root_000452/B005"],"candidate_id":"cand_6349af299a067939a02c","evidence_scope":"focus_ayah","hft_ref":"hft_eb564036a0042adf0975","item_id":"b-preserving-beneficence","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b-preserving-beneficence","support_id":"sup_494adb4b482277e4a4a1"}],"diagnostics":[],"lane_counts":{"global":9,"macro":9,"micro":3},"packet_summary":{"ayah_count":19,"focus_ref":"87:17","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ء ث ر","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":true,"target_occurrences":9,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]}],"window":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"87:17","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":12,"unstructured_record_count":0},"identity":{"ayah_ref":"87:17","lane":"micro","linguistic_source_ref":"87:17","surface_ref":"87:17","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"87:17","target_tokens":[["Oysa",["87:17:1"]],["ahiret",["87:17:1"]],["daha",["87:17:2"]],["iyi",["87:17:2"]],["ve",["87:17:3"]],["daha",["87:17:3"]],["kalıcıdır",["87:17:3"]]],"text":"Oysa ahiret daha iyi ve daha kalıcıdır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s087-p01-001-019","label":"Whole surah","number":1,"refs":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:1","source_type":"word_analysis","support_id":"sup_032cdaa9ea6ad38f46fb","text":"{\"gloss_range\":\"initial conjunctive bridge that carries the prior preference statement into a nominal counter-verdict rather than opening an isolated maxim\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) keeps 87:16 active as the new clause begins. The reader does not meet a detached maxim, but a corrective continuation: the preference for the nearer life is still in force when the final realm is declared better and more enduring. Because the particle is bound directly to {{ar:ٱلْءَاخِرَةُ}} ({{tr:al-ākhiratu}}), the bridge and the counter-subject arrive as one surface movement. The ayah also turns from ongoing human choosing into a stable nominal verdict, so the connector marks the pivot from behavior to the scale that judges it.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:2:posteriority-as-value-horizon","source_type":"word_analysis","support_id":"sup_0cf46e6c9e905ec87e9e","text":"{\"blocking_evidence\":null,\"headline\":\"posteriority becomes value horizon\",\"reader_payoff\":\"The reader notices the irony that what humans defer becomes the horizon by which their immediate preference is corrected.\",\"reason\":\"The local noun selects the final-realm sense; V4 has no root rows for this root, so the valid root-pressure claim is preserved cautiously rather than expanded into unrelated delay branches.\",\"representative_source_ids\":[\"QS-2155027c\",\"QS-29bbe333\",\"QS-9e3683f1\",\"MS-8363a6a5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:1:corrective-boundary-bridge","source_type":"word_analysis","support_id":"sup_178bc90b02a5c51bb7fc","text":"{\"blocking_evidence\":null,\"headline\":\"boundary bridge to the verdict\",\"reader_payoff\":\"The reader notices that 87:17 answers the preference named in 87:16 instead of starting a separate saying.\",\"reason\":\"The local clause begins with a conjunction and attachment evidence identifies one nominal clause that follows the prior preference statement.\",\"representative_source_ids\":[\"QG-54b982a8\",\"QT-a03725a1\",\"MT-84765b2b\",\"QB-c170b96b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:3","source_type":"word_analysis","support_id":"sup_1c309b1d5695c3588628","text":"{\"gloss_range\":\"qualitative comparative predicate of superior worth and preferability, selected against the prior near-life preference and not the material-wealth branch\",\"prose\":\"{{ar:خَيْرٌۭ}} ({{tr:khayrun}}) gives the first predicate of the verdict. As an indefinite comparative predicate, it characterizes the final realm by superior worth without turning that worth into a named object. The root family keeps goodness tied to choosability, so the word answers the preference of 87:16 by naming what should truly be preferred. Local grammar narrows the broad root range: the point is not a detachable material good or wealth item, but evaluative benefit and worth. Since {{ar:خَيْرٌۭ}} ({{tr:khayrun}}) comes before {{ar:أَبْقَىٰٓ}} ({{tr:abqā}}), the ayah argues value before duration; endurance strengthens a good already judged superior. The clipped close of {{ar:خَيْرٌۭ}} ({{tr:khayrun}}) followed by the longer landing of {{ar:أَبْقَىٰٓ}} ({{tr:abqā}}) lets that order be heard as well as parsed. That pairing joins a recognizable Quranic valuation pattern, including worldly-life versus Hereafter comparison at 4:77, consolation through a similar afterlife-better formula at 93:4, and value-plus-endurance echoes at 28:60 and 42:36.\",\"root_display\":\"{{ar:خ ي ر}} ({{tr:kh-y-r}})\",\"root_gloss_range\":\"goodness, excellence, choice-worthiness, choosing the better, benefit, beneficence, and a wealth-as-good branch; local predicate grammar selects superior value and true preferability\",\"surface_display\":\"{{ar:خَيْرٌۭ}} ({{tr:khayrun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:4:double-connector-frame","source_type":"word_analysis","support_id":"sup_279d8ec33dcc88249877","text":"{\"blocking_evidence\":null,\"headline\":\"second connector in the verse frame\",\"reader_payoff\":\"The reader notices that the two connectors do different work: one bridges from 87:16, and this one expands the verdict inside 87:17.\",\"reason\":\"The ayah contains an initial conjunction and a second predicate-level conjunction; attachment evidence distinguishes the clause bridge from the internal coordination.\",\"representative_source_ids\":[\"QE-b54b38b3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:5:maxim-formula-and-intertexts","source_type":"word_analysis","support_id":"sup_387749964fa22e65b43a","text":"{\"blocking_evidence\":null,\"headline\":\"formulaic enduring verdict\",\"reader_payoff\":\"The reader notices that the word completes a known value-plus-endurance verdict rather than adding a random second praise.\",\"reason\":\"The CRITICAL rows cite the value-plus-endurance formula at 20:73, and local attachment shows the same two-predicate pairing in 87:17.\",\"representative_source_ids\":[\"MI-b17f6b4b\",\"QT-510111c8\",\"QE-95648bf0\",\"ME-9a00ef31\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:4:coordinated-predicate-link","source_type":"word_analysis","support_id":"sup_3b3877bc248e31128eb7","text":"{\"blocking_evidence\":null,\"headline\":\"same-subject predicate link\",\"reader_payoff\":\"The reader notices that endurance is coordinated with value under one subject, not appended as a weaker afterthought.\",\"reason\":\"Attachment evidence marks the second comparative as conjoined with the first predicate and predicated of the same final-realm subject.\",\"representative_source_ids\":[\"QG-34e8c08c\",\"MG-5c5df857\",\"QT-74613474\",\"QY-4ed91709\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:5:adjective-not-preserving-verb","source_type":"word_analysis","support_id":"sup_4615b2a162ab5247d4d4","text":"{\"blocking_evidence\":null,\"headline\":\"comparative adjective, not preserving verb\",\"reader_payoff\":\"The reader notices that the word asserts an enduring quality of the Hereafter rather than introducing a new agent who preserves something.\",\"reason\":\"The same surface can be associated with causative preservation elsewhere, but the local coordinated predicate slot selects an adjectival comparative quality.\",\"representative_source_ids\":[\"QG-e50675e6\",\"QF-12ae382f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:3:value-before-endurance","source_type":"word_analysis","support_id":"sup_5011ea0a7ad0c103bcaa","text":"{\"blocking_evidence\":null,\"headline\":\"value before endurance\",\"reader_payoff\":\"The reader notices that permanence is not the only argument; the final realm is first better and then more lasting.\",\"reason\":\"The local order places the value predicate before the coordinated endurance predicate, and attachment evidence keeps them under one subject.\",\"representative_source_ids\":[\"QT-22982920\",\"MT-ab4d8ce8\",\"QP-e122742b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:3:choice-correction","source_type":"word_analysis","support_id":"sup_530f8eeded7986c410ce","text":"{\"blocking_evidence\":null,\"headline\":\"goodness as corrected choice\",\"reader_payoff\":\"The reader notices that the word does not merely praise the Hereafter; it corrects the act of choosing by naming the truly preferable object.\",\"reason\":\"V4 supports branches of goodness, excellence, and choosing the better, while local comparison to 87:16 selects the preference-correcting comparative sense.\",\"representative_source_ids\":[\"QS-397c345b\",\"QS-5dccef04\",\"QS-9e08f57f\",\"MS-64fc5a66\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:2:definite-counterpart-to-near-life","source_type":"word_analysis","support_id":"sup_53d2d7d47b74005c88c4","text":"{\"blocking_evidence\":null,\"headline\":\"overt counterpart to the near life\",\"reader_payoff\":\"The reader notices that the ayah names the neglected opposite of the near life, so the rebuke becomes a direct contrast rather than an abstract preference lesson.\",\"reason\":\"The article and nominative subject role are local, while the comparison standard for the following predicates is recoverable from the near-life object in 87:16.\",\"representative_source_ids\":[\"QG-928b1e28\",\"QG-d3355fd3\",\"QS-1a05dbe0\",\"QT-c83d8a75\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:5:comparative-endurance-against-near-life","source_type":"word_analysis","support_id":"sup_5b5aef825aec97736bd6","text":"{\"blocking_evidence\":null,\"headline\":\"comparative endurance against the near life\",\"reader_payoff\":\"The reader notices that the near life is real enough to be compared but too transient to win the comparison.\",\"reason\":\"Attachment evidence marks an omitted comparison standard recoverable from 87:16, and the local form is an adjectival comparative predicate.\",\"representative_source_ids\":[\"QS-38aa3c87\",\"QS-4c51de11\",\"QF-5a9e879f\",\"QI-f1262f72\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:5:coequal-second-predicate","source_type":"word_analysis","support_id":"sup_5e885edbaf0199f7e0bc","text":"{\"blocking_evidence\":null,\"headline\":\"coequal second predicate\",\"reader_payoff\":\"The reader notices that duration is not secondary to worth; it is a coordinated predicate in the same counter-scale.\",\"reason\":\"Attachment evidence marks the word as coordinated with the first predicate and also predicated of the final-realm subject.\",\"representative_source_ids\":[\"QG-885c0901\",\"MG-ea1700a5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:3:qualitative-value-predicate","source_type":"word_analysis","support_id":"sup_6cf40be3a5313f0b5cc6","text":"{\"blocking_evidence\":null,\"headline\":\"qualitative value predicate\",\"reader_payoff\":\"The reader notices that the word asserts superior worth as a stable predicate, not as a new event or a label.\",\"reason\":\"QAC marks an indefinite nominative comparative/superlative adjective, and attachment evidence makes it the first predicate of the final-realm subject.\",\"representative_source_ids\":[\"QG-ca23be9f\",\"MG-df6708b8\",\"QF-bb74139e\",\"MT-58d6ebe3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:2:boundary-counter-scale","source_type":"word_analysis","support_id":"sup_70ee3535458b4ac1cd0e","text":"{\"blocking_evidence\":null,\"headline\":\"boundary hinge into counter-scale\",\"reader_payoff\":\"The reader notices that the word is the hinge where the previous preference becomes measurable against a named counter-scale.\",\"reason\":\"The preceding ayah supplies the contrastive comparison standard, and the local word explicitly names the counterpart before the two predicates.\",\"representative_source_ids\":[\"MI-a85526c7\",\"MI-bb5e42d7\",\"QB-4e693d82\",\"QY-66fb2d65\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:4:bound-continuation-sound","source_type":"word_analysis","support_id":"sup_7704a59508a1c0327b2f","text":"{\"blocking_evidence\":null,\"headline\":\"bound continuation into endurance\",\"reader_payoff\":\"The reader notices the audible continuity from the value predicate into the endurance predicate.\",\"reason\":\"The conjunction is a bound clitic directly attached to the second predicate; the payoff is local sound and surface linkage.\",\"representative_source_ids\":[\"QF-e6a9a9a6\",\"QP-11679086\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:2:realm-form-totality","source_type":"word_analysis","support_id":"sup_7a7c5e1497b0e48e544f","text":"{\"blocking_evidence\":null,\"headline\":\"singular realm-form totality\",\"reader_payoff\":\"The reader notices that the word gathers the final life as one evaluable realm or state, able to receive both predicates together.\",\"reason\":\"QAC and noun-instance evidence support a definite feminine abstract noun in nominative subject position.\",\"representative_source_ids\":[\"QF-6711d755\",\"QF-b53605fa\",\"QF-f16227bc\",\"MF-54d17e6a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:5:sound-and-closure","source_type":"word_analysis","support_id":"sup_7c6f836bcf5e37e02934","text":"{\"blocking_evidence\":null,\"headline\":\"audible landing on lastingness\",\"reader_payoff\":\"The reader notices that the word of endurance also gives the ayah its stretched final landing.\",\"reason\":\"The written final long vowel and surrounding closure pattern are visible in the local surface; this is an acoustic payoff, not an added semantic branch.\",\"representative_source_ids\":[\"QF-f92ce272\",\"QP-4140187e\",\"QP-a54d9bc3\",\"QY-eaa7437c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:5:remaining-after-loss-pressure","source_type":"word_analysis","support_id":"sup_7d1a5c0478bb6bea7f45","text":"{\"blocking_evidence\":null,\"headline\":\"remaining after loss\",\"reader_payoff\":\"The reader notices that endurance is felt as survival after other goods disappear, not just as abstract length of time.\",\"reason\":\"V4 supports remaining, persistence, and remainder branches; local grammar keeps the selected sense comparative endurance while allowing the survival-after-loss image to color it.\",\"representative_source_ids\":[\"QS-6c3ad2b7\",\"QS-8bc7b9df\",\"MS-cf32a916\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:3:valuation-formula-and-echoes","source_type":"word_analysis","support_id":"sup_8a88e891b855fe1272d0","text":"{\"blocking_evidence\":null,\"headline\":\"valuation formula echoes\",\"reader_payoff\":\"The reader notices that this compact predicate belongs to a wider Quranic pattern where afterlife value outranks worldly immediacy.\",\"reason\":\"The CRITICAL evidence gives concrete parallels at 4:77, 93:4, 28:60, and 42:36, while local grammar supports the same comparative valuation pattern.\",\"representative_source_ids\":[\"QI-9aed0bb6\",\"MI-7474527a\",\"QE-08a314b6\",\"ME-78e93027\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:17:2:1","source_type":"qac_morpheme","support_id":"sup_9026778350e07a7deec3","text":"{\"lemma_ar\":\"خَيْر\",\"morph_features\":\"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"87:17:2:1\",\"qac_word_ref\":\"87:17:2\",\"root_ar\":\"خ ي ر\",\"surface_ar\":\"خَيْرٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:5:first-last-and-scroll-horizon","source_type":"word_analysis","support_id":"sup_95cb198a79b2343746c5","text":"{\"blocking_evidence\":null,\"headline\":\"first-last and scroll horizon\",\"reader_payoff\":\"The reader notices that the endurance claim is immediately framed by a wider horizon: lastness versus firstness across 87:17-18 and the older scroll witness in 87:18.\",\"reason\":\"The CRITICAL rows provide concrete neighboring references, so the topic survives as a local boundary observation without controlling the lexical parse.\",\"representative_source_ids\":[\"MT-2a8581a7\",\"QB-c4998102\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:2:formula-and-horizon-links","source_type":"word_analysis","support_id":"sup_98d5fda169c64071524a","text":"{\"blocking_evidence\":null,\"headline\":\"finality linked with lasting value\",\"reader_payoff\":\"The reader notices that the final realm is not merely later; it is tied to superior and enduring value within this ayah and nearby scriptural patterns.\",\"reason\":\"The CRITICAL rows give concrete links to the afterlife-and-endurance relation at 20:127 and the first/last axis across 87:17-18; local attachment supports the paired predicates.\",\"representative_source_ids\":[\"QI-064dee60\",\"QE-78d2f2c3\",\"QH-498f72f3\",\"QB-3790d908\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:17:1:3","source_type":"qac_morpheme","support_id":"sup_9d6003c390642606e781","text":"{\"lemma_ar\":\"آخِر\",\"morph_features\":\"STEM|POS:N|LEM:A^xir|ROOT:Axr|FS|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"87:17:1:3\",\"qac_word_ref\":\"87:17:1\",\"root_ar\":\"ء خ ر\",\"surface_ar\":\"ءَاخِرَةُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:1:verbal-action-to-nominal-scale","source_type":"word_analysis","support_id":"sup_a4d550b5aec4a719a2cc","text":"{\"blocking_evidence\":null,\"headline\":\"from action to stable scale\",\"reader_payoff\":\"The reader notices the shift from human preference as an ongoing act to a standing evaluative truth.\",\"reason\":\"Attachment evidence supports a nominal clause in 87:17, allowing the boundary topic to contrast that stable predication with the preceding preference statement.\",\"representative_source_ids\":[\"QB-1ad839f4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:3:value-not-material-good","source_type":"word_analysis","support_id":"sup_b8b677e492ca115c87bb","text":"{\"blocking_evidence\":null,\"headline\":\"worth, not material wealth\",\"reader_payoff\":\"The reader notices that the predicate ranks moral and practical worth, not a piece of wealth or a detachable good.\",\"reason\":\"V4 records a wealth-as-good branch for the root, but the local adjectival predicate and near-life contrast select evaluative worth rather than a material-good noun.\",\"representative_source_ids\":[\"QS-dd803390\",\"QS-decb707a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:2","source_type":"word_analysis","support_id":"sup_bd74d7d067a2444c06f8","text":"{\"gloss_range\":\"the definite final realm as a known, whole counterpart to the near life of 87:16, carrying posteriority into an evaluative horizon\",\"prose\":\"{{ar:ٱلْءَاخِرَةُ}} ({{tr:al-ākhiratu}}) stands first as the known subject that receives both predicates. Its definiteness and singular feminine realm-form make the Hereafter one recognizable destiny, not a vague later item or scattered events. The root pressure of coming after becomes evaluative here: the reality treated as deferred is the one by which the nearer life of 87:16 is weighed. By naming the counterpart overtly, the ayah turns misdirected preference into a direct trial between the near life and the final realm. The word also belongs to a wider pattern in which finality is judged by remaining value, visible in the afterlife-and-endurance relation at 20:127 and in the first/last movement across 87:17-18. Because this final-realm-and-endurance bond is not routine, the compact wording carries concentrated weight rather than formulaic blandness.\",\"root_display\":\"{{ar:أ خ ر}} ({{tr:ʾ-kh-r}})\",\"root_gloss_range\":\"coming after, delay, posteriority, lastness, and finality; local grammar selects the eschatological final-realm noun while preserving the pressure that what comes later becomes the judging horizon\",\"surface_display\":\"{{ar:ٱلْءَاخِرَةُ}} ({{tr:al-ākhiratu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:17:3:2","source_type":"qac_morpheme","support_id":"sup_c991ece7bcf5a9687426","text":"{\"lemma_ar\":\"أَبْقَىٰٓ\",\"morph_features\":\"STEM|POS:N|LEM:>aboqaY`^|ROOT:bqy|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"87:17:3:2\",\"qac_word_ref\":\"87:17:3\",\"root_ar\":\"ب ق ي\",\"surface_ar\":\"أَبْقَىٰٓ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:2:subject-with-two-predicates","source_type":"word_analysis","support_id":"sup_ca0fd3e4b914a16a5de6","text":"{\"blocking_evidence\":null,\"headline\":\"known subject carrying two predicates\",\"reader_payoff\":\"The reader notices that the final realm itself is the evaluated subject, carrying both worth and endurance as stable predicates.\",\"reason\":\"QAC marks the word as nominative, and attachment evidence makes both comparative predicates depend on this subject.\",\"representative_source_ids\":[\"QG-159a894b\",\"QG-7c849380\",\"MT-16f7aa98\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:3:corrective-value-node","source_type":"word_analysis","support_id":"sup_d393d7dd4326d1c9baca","text":"{\"blocking_evidence\":null,\"headline\":\"main reversal node\",\"reader_payoff\":\"The reader notices that this word carries the ayah's reversal from enacted preference to correct comparative value.\",\"reason\":\"The local comparative predicate answers the prior preference statement, and contextual role profiles show this form commonly functioning in predication.\",\"representative_source_ids\":[\"QE-429135bf\",\"QB-344e6120\",\"QY-6472d1fe\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:5","source_type":"word_analysis","support_id":"sup_debd5dafca526ba95bba","text":"{\"gloss_range\":\"comparative predicate meaning more enduring or more able to remain, coordinated with superior worth and measured against the near life supplied by 87:16\",\"prose\":\"{{ar:أَبْقَىٰٓ}} ({{tr:abqā}}) gives the second predicate and lands the ayah on endurance. It shares the predicate slot with {{ar:خَيْرٌۭ}} ({{tr:khayrun}}), so duration is grammatically coequal with worth. Local grammar narrows the form to a comparative adjective, not a finite act of preserving; the clause ranks the final realm as more enduring than the near life supplied by 87:16. The root's remaining-and-surviving pressure makes the contrast sharper: the preferred near life looks fragile beside what remains after other goods pass. The word completes the value-plus-endurance formula seen at 20:73, turning the specific rebuke of worldly preference into a maxim-like verdict where the better thing is also the remaining horizon. The compact bond between final realm and endurance is not routine, so the pairing has concentrated weight rather than merely repeating a stock praise. The following turn to earlier scrolls in 87:18 then gives the verdict a textual horizon beyond the immediate rebuke. Its final long sound also lets the word for lastingness become the audible landing of the ayah.\",\"root_display\":\"{{ar:ب ق ي}} ({{tr:b-q-y}})\",\"root_gloss_range\":\"remaining, persisting, surviving after loss, residue, sparing, reserve, and watching/waiting branches; local form selects comparative endurance while the survival-after-loss pressure remains relevant\",\"surface_display\":\"{{ar:أَبْقَىٰٓ}} ({{tr:abqā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:1:bound-subject-entry","source_type":"word_analysis","support_id":"sup_e1989ea2262371cc3d62","text":"{\"blocking_evidence\":null,\"headline\":\"bound entry into the subject\",\"reader_payoff\":\"The reader notices that the connector is not pause-like; it carries the ear and eye straight into the named final realm.\",\"reason\":\"The source surface is a clitic conjunction immediately followed by the definite subject, so the payoff is morphological and acoustic rather than a new lexical sense.\",\"representative_source_ids\":[\"QF-2c5fea2f\",\"QP-8cee9f99\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:4","source_type":"word_analysis","support_id":"sup_e66625e93c36cf8026ff","text":"{\"gloss_range\":\"coordinating connector between the two predicates, making endurance an attached continuation of the same evaluative act rather than a separate clause\",\"prose\":\"The second {{ar:وَ}} ({{tr:wa}}) keeps {{ar:أَبْقَىٰٓ}} ({{tr:abqā}}) under the same subject and alongside {{ar:خَيْرٌۭ}} ({{tr:khayrun}}). Duration is therefore not a new clause or an afterthought; it is added as part of the same verdict. The clitic sound carries the listener from the first predicate into the second, so the ayah's two criteria accumulate without breaking the line. Together with the initial connector, this small particle frames the verse: first linking backward to the prior preference, then expanding the judgment internally.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:5:compressed-comparator","source_type":"word_analysis","support_id":"sup_e99e2bedfe79dc5c448b","text":"{\"blocking_evidence\":null,\"headline\":\"omitted comparator kept active\",\"reader_payoff\":\"The reader notices that the comparison stays compact because 87:16 has already supplied the worldly rival.\",\"reason\":\"Attachment and translation-support evidence explicitly mark the comparison standard as omitted and recoverable from the preceding near-life contrast.\",\"representative_source_ids\":[\"QT-e7924e93\",\"MF-f3ae05c9\",\"QB-f1c72713\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:17:5:rare-finality-endurance-pair","source_type":"word_analysis","support_id":"sup_ecde79e8228fb598daa7","text":"{\"blocking_evidence\":null,\"headline\":\"weighted finality-endurance pair\",\"reader_payoff\":\"The reader notices that the compact pairing of final realm and endurance has concentrated weight rather than routine collocational blandness.\",\"reason\":\"Contextual collocation evidence shows the exact form as relatively constrained, while local grammar supplies the final-realm subject.\",\"representative_source_ids\":[\"QH-b77ef1e3\",\"QH-e0601635\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ","ayah_ref":"87:17"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000019/B001","root_000142/B001","root_000452/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000019","role":"The later-or-other-than-first branch establishes the relational horizon being compared.","root":"ء خ ر","source_ref":"87:17","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000452","role":"The desired and beneficial good branch supplies qualitative superiority, not just temporal succession.","root":"خ ي ر","source_ref":"87:17","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000142","role":"The persistence-against-perishing branch supplies the durability dimension of the comparison.","root":"ب ق ي","source_ref":"87:17","source_word_indices":["3"]}],"changed_reading":{"after":"The latter horizon is preferred because its benefit and its resistance to extinction coincide, while remaining analytically distinct.","before":"The latter is simply better and lasts longer."},"confidence":"strong","focus_anchor":"The three-part construction joins the later/other horizon, beneficial goodness, and persistence without collapsing them into one property.","mechanism":"Laterness supplies the compared horizon, goodness supplies the reason for preference, and persistence supplies resistance to loss. Keeping the last two predicates distinct prevents mere longevity from counting automatically as good.","model_id":"b-qualified-endurance"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b-qualified-endurance","source_type":"hft","support_id":"sup_1fd91e24ee29a5f37fb2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ","ayah_ref":"87:17"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000019/B002","root_000142/B004","root_000452/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000019","role":"The deferral-to-a-later-time branch supplies postponed realization rather than simple absence.","root":"ء خ ر","source_ref":"87:17","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000452","role":"The choosing-the-better-option branch turns the comparison into a decision between alternatives.","root":"خ ي ر","source_ref":"87:17","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000142","role":"The held-back reserve branch makes durability function as conserved, unspent capacity.","root":"ب ق ي","source_ref":"87:17","source_word_indices":["3"]}],"changed_reading":{"after":"The verse can also stage a choice between immediate expenditure and a better deferred reserve.","before":"The verse only reports fixed attributes of two worlds."},"confidence":"medium","focus_anchor":"The focus roots themselves permit a deferred-time branch, a better-option branch, and a held-reserve branch.","mechanism":"The focus can stage an allocation decision: value not exhausted in the first horizon is deferred, selected as the better option, and conserved as reserve. Delay is therefore not emptiness but protected capacity.","model_id":"b-deferred-reserve"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b-deferred-reserve","source_type":"hft","support_id":"sup_4f5cd9b273d716085f0d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ","ayah_ref":"87:17"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000019/B001","root_000142/B003","root_000452/B005"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000019","role":"The latter-or-other branch locates the proposed preserving order beyond the first one.","root":"ء خ ر","source_ref":"87:17","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_000452","role":"The beneficence-and-gift branch renders goodness as something given to a recipient.","root":"خ ي ر","source_ref":"87:17","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000142","role":"The sparing-and-keeping-alive branch supplies active preservation instead of duration alone.","root":"ب ق ي","source_ref":"87:17","source_word_indices":["3"]}],"changed_reading":{"after":"As a live secondary reading, the latter realm may also be more preserving: its goodness consists partly in what it spares from loss.","before":"More lasting describes only the duration of the latter realm."},"confidence":"exploratory","focus_anchor":"The branch inventory of the focus permits beneficent giving beside sparing and keeping alive.","mechanism":"Alongside passive endurance, the final predicate can echo an agentive relation: the latter order gives more good by sparing, preserving, or refusing total loss. This remains a secondary activation rather than a replacement gloss.","model_id":"b-preserving-beneficence"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b-preserving-beneficence","source_type":"hft","support_id":"sup_494adb4b482277e4a4a1","trust":"legacy_unbound"}]}
</lane_packet_json>
