# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **87:18**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s087-regular-20260911/s087/87_18/micro.discovery.json` and modify nothing
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
  "ayah_ref": "87:18",
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
{"analysis_context":{"analysis_id":"s087-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"87:18","host_surah":87,"lane_context_refs":[],"ordered_context_refs":["87:0","87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:19","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal yalnız başlangıç ve önde gelme alanındadır; sonuca dönme, aile, yönetme ve araç anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000067/B001","candidate_links":[{"candidate_id":"cand_49e8bc88876e0bab25ea","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"başlangıç ve öncelik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin başlangıç noktasını veya ilk bölümünü belirtir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir varlığın zaman, sıra, derece ya da ilerleyişte önde bulunmasını belirtir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sürüde önden giden deve, bu önceliğin hareket alanındaki özel bir örneğidir."}}],"root_ar":"ء و ل","root_id":"root_000067","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin ilk noktasını ve zaman, sıra, derece ya da ilerleyiş bakımından önde olmayı birlikte anlatan genel karşılıktır.","boundary_detail":"Bu dal yalnız başlangıç ve önde gelme alanındadır; sonuca dönme, aile, yönetme ve araç anlamlarını kapsamaz.","branch_image_ar":"ابتداء الشيء وتقدمه","concept_gloss":"başlangıç ve öncelik","contextual_glosses":[{"applicability":"Bir zamanın, sıranın ya da şeyin başlangıçtaki öğesi doğal Türkçede nitelenirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlam içinde başlangıçta veya sıranın önünde bulunmayı korur."},"facet_ids":["F001","F002"],"text":"ilk","usage_role":"contextual"}],"definition":"Bir şeyin başladığı nokta veya zaman ile bir varlığın zaman, sıra, derece ya da ilerleyiş bakımından başkalarından önce bulunmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin başlangıç noktasını veya ilk bölümünü belirtir."},{"facet_id":"F002","role":"core","statement":"Bir varlığın zaman, sıra, derece ya da ilerleyişte önde bulunmasını belirtir."},{"facet_id":"F003","role":"example","statement":"Sürüde önden giden deve, bu önceliğin hareket alanındaki özel bir örneğidir."}],"identity_rationale":"Kaynak ifadesi, bir şeyin başlangıcını ve zaman, sıra ya da ilerleyiş bakımından başkalarının önünde bulunmasını birlikte gösterir. Verilen dal çerçevesi bu çekirdeği doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ilk; önde gelen"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ilk olan kadın ya da dişil şey"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ilkler; öncekiler"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"topluluğun önünde bulunma"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"sürünün önünde giden dişi ya da erkek deve"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"önceki yıl"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"her şeyden önce"}],"lexicalization_note":"Tanım genel başlangıç ve öncelik çekirdeğini korur; deve sürüsü, önceki yıl ve her şeyden önce olma kullanımları kendi kalıplarıyla sınırlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın sınır karşılaştırması yayımlandı, kalanlar sonuç, aile, yönetim, durum, araç ve başka uzak alanlara aittir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel başlangıç ve öncelik kavramıdır; komşu dal ise bu önceliği egemenlik, anılma, eylem veya önce başlama hakkı gibi daha belirli alanlara bağlar.","focus_only":"Odak dal, egemenlik ya da söz hakkı bulunmadan yalnız zamansal, sırasal veya devinimsel önceliği de kapsar.","gloss":"öncelik ve başlama üstünlüğü","neighbor_only":"Komşu dal, egemenlikte, anılmada veya eylemde önce gelme ve önce başlama hakkını özellikle içerir.","neighbor_ref":"root_000090/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da başlangıçta veya başkalarından önce bulunmayı anlatır."}],"source_phrase_ar":"الأول وهو مبتدأ الشيء؛ ناقة أولة وجمل أول إذا تقدما الإبل (maqayis)؛ أول في اللغة على الحقيقة ابتداء الشيء؛ جاء فلان في أولية الناس إذا جاء في أولهم (tahdhib)","source_summary":"Kaynaklar başlangıç ile önde gelmeyi ortak çekirdek sayar; önde gidiş, topluluğun başında bulunma ve zamansal öncelik bu çekirdeğin bağlama göre gerçekleşmeleridir.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه الأول والأولى والأوائل والأولية وما يدل على ابتداء الشيء أو تقدمه في الزمن أو الرتبة أو السير.","what_is_not_ar":"ليس من رجوع الشيء إلى مآله، ولا من آل الأهل، ولا من السياسة أو الخثور أو الآلة."},"support_links":["sup_0ba9419ab25b6e5b671e"]},{"boundary":"Bu dal sırf başlangıç, aile, yönetim ya da fiziksel koyulaşma değildir; bir varışa, sonuca veya anlama yönelme bağı zorunludur.","branch_kind":"mixed_non_bare","branch_ref":"root_000067/B002","candidate_links":[{"candidate_id":"cand_54c429f748c97833f5b7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"sonuca dönme ve varma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin geri dönmesi veya sonunda belirli bir duruma varmasıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir sözün sonucunu ya da varacağı anlamı açıklamak, geri döndürme çekirdeğinin yorum alanındaki uzantısıdır."}}],"root_ar":"ء و ل","root_id":"root_000067","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Geri dönüşü, son duruma ulaşmayı ve sözün varacağı anlama bağlanmasını ortak çekirdekte anlatır.","boundary_detail":"Bu dal sırf başlangıç, aile, yönetim ya da fiziksel koyulaşma değildir; bir varışa, sonuca veya anlama yönelme bağı zorunludur.","branch_image_ar":"رجوع الشيء إلى مآله وعاقبته","concept_gloss":"sonuca dönme ve varma","contextual_glosses":[{"applicability":"Bir varlığın süreç sonunda ulaştığı durum yüklemle belirtildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geri dönme ve sözü anlamına döndürerek açıklama yönlerini dışarıda bırakır.","preserves":"Bir son duruma varma yönünü korur."},"facet_ids":["F001"],"text":"sonunda ... olmak","usage_role":"contextual"},{"applicability":"Bir sözün neye vardığı veya ne demek olduğu ortaya konurken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel geri dönüş ve bir son duruma varma yönlerini dışarıda bırakır.","preserves":"Sözü varacağı anlama döndürme yönünü korur."},"facet_ids":["F002"],"text":"anlamını açıklamak","usage_role":"contextual"}],"definition":"Bir şeyin geri dönerek ya da değişerek varacağı son duruma, yere veya sonuca ulaşmasıdır; söz alanında, anlatımı varacağı anlama döndürerek açıklamayı da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin geri dönmesi veya sonunda belirli bir duruma varmasıdır."},{"facet_id":"F002","role":"extension","statement":"Bir sözün sonucunu ya da varacağı anlamı açıklamak, geri döndürme çekirdeğinin yorum alanındaki uzantısıdır."}],"identity_rationale":"Kaynak ifadesi hem geri dönme veya bir son duruma varmayı hem de sözün varacağı anlamı ortaya çıkarma işlemini açıkça içerir. Dal çerçevesi süreç, sonuç ve yorumlama bağlantısını korur.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"geri dönmek; sonunda bir duruma varmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"hükmü sahiplerine geri vermek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bedeni zayıflamak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"sözün sonucu veya anlamının açıklanması"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"açıklamak; anlamına döndürmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"onunla ilgili ödülü gözetmek ve aramak"}],"lexicalization_note":"Genel geri dönme ve sonuca varma çekirdeği ile sözü anlamına döndürme, hükmü sahibine verme ve ödül arama kalıpları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan komşu son duruma varma bakımından en yakın olandır, diğerleri dönüş, sonuç veya olay alanının daha dar parçalarını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel olarak olma ve bir şeyi oldurma alanına uzanır; odak dalda geri dönüş bağı ve sözün sonucunu ya da anlamını açıklama özel olarak belirgindir.","focus_only":"Odak dal geri dönüşü ve sözün varacağı anlama döndürülerek açıklanmasını içerir.","gloss":"bir son duruma dönüşme","neighbor_only":"Komşu dal bir şeyi belirli bir duruma sokma ve kararın ya da sağlam tutumun varacağı sonucu da içerir.","neighbor_ref":"root_000897/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir süreç sonunda ulaşılan durumu, varışı veya sonucu anlatır."}],"source_phrase_ar":"آل يؤول أى رجع؛ تأويل الكلام وهو عاقبته وما يؤول إليه (maqayis)؛ التأويل تفسير ما يؤول إليه الشئ؛ آل أي رجع (sihah)؛ آل يؤول أي رجع وعاد؛ التأويل المرجع والمصير (tahdhib)","source_summary":"Kaynaklar geri dönüş, son varış ve sonuç anlamlarında birleşir; sözün açıklanması da onu ulaşacağı anlama veya sonuca bağlayan özel bir kullanımdır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه آل يؤول بمعنى رجع أو صار، والمآل والمرجع والمصير، وتأويل الكلام بمعنى ما يؤول إليه أو تفسيره برده إلى معناه.","what_is_not_ar":"ليس مجرد الأولية والابتداء، ولا أهل الرجل، ولا السياسة، ولا الخثور الحسي."},"support_links":["sup_7643f4841419c3065d94"]},{"boundary":"Buradaki topluluk kişinin ailesi ve ona bağlı çevresidir; görünen siluet, yorumlama veya genel bir insan topluluğu değildir.","branch_kind":"bare","branch_ref":"root_000067/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"aile ve bağlı çevre","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin ev halkını, ailesini, yakınlarını ve bakmakla yükümlü olduğu kimseleri kapsar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin izleyicileri ve onun tarafında bulunan bağlı kimseler de bu aidiyet çevresine katılabilir."}}],"root_ar":"ء و ل","root_id":"root_000067","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ev halkını, yakınları, bakmakla yükümlü olunanları ve kişiye bağlı kimseleri birlikte kapsayan genel karşılıktır.","boundary_detail":"Buradaki topluluk kişinin ailesi ve ona bağlı çevresidir; görünen siluet, yorumlama veya genel bir insan topluluğu değildir.","branch_image_ar":"آل الرجل من يرجع إليهم ويرجعون إليه","concept_gloss":"aile ve bağlı çevre","contextual_glosses":[{"applicability":"Kapsam kişinin aynı eve ve yakın aile çevresine bağlı kimseleriyle sınırlı olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ev dışındaki izleyicileri ve daha geniş bağlı çevreyi dışarıda bırakabilir.","preserves":"Kişiye bağlı aile ve ev çevresi çekirdeğini korur."},"facet_ids":["F001"],"text":"ev halkı","usage_role":"contextual"}],"definition":"Bir kişinin ev halkı, ailesi, yakınları, bakmakla yükümlü oldukları ve ona bağlı olanlardan oluşan; karşılıklı aidiyetle kişiye bağlanan topluluktur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin ev halkını, ailesini, yakınlarını ve bakmakla yükümlü olduğu kimseleri kapsar."},{"facet_id":"F002","role":"extension","statement":"Kişinin izleyicileri ve onun tarafında bulunan bağlı kimseler de bu aidiyet çevresine katılabilir."}],"identity_rationale":"Kaynak ifadesi kişinin ev halkını, yakınlarını, bakmakla yükümlü olduklarını ve bağlılarını, kişinin onlara ve onların kişiye dönük aidiyetiyle tanımlar. Dal çerçevesi bu topluluk çekirdeğini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kişinin ailesi, ev halkı ve yakınları"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"onun izleyicileri ve bağlıları"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kişinin sığındığı ev halkı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kişinin kökü ve bağlı olduğu aile"}],"lexicalization_note":"Tanım dalın yalın aile ve bağlı çevre anlamıyla sınırlıdır; başka dallardaki kalıplaşmış kullanımlar içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ev halkı komşusu en yakın sınırı verir, öteki adaylar soy, aşiret, evlilik veya genel topluluk yönlerinden daha özeldir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal karşılıklı aidiyet ve kişiye bağlı çevre üzerinden genişleyebilir; komşu dalın sınırı ev ve ev halkı merkezlidir ve ev benzetmeli adlandırmaları da içerir.","focus_only":"Odak dal yakınların yanında izleyicileri ve kişiye bağlı daha geniş çevreyi de kapsayabilir.","gloss":"ev halkı ve bakmakla yükümlü olunanlar","neighbor_only":"Komşu dal ev benzetmesiyle bir kadın ya da topluluğun ev diye adlandırılmasına uzanır.","neighbor_ref":"root_000166/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin ev halkını, ailesini ve bakmakla yükümlü olduğu kimseleri kapsar."}],"source_phrase_ar":"آل الرجل أهل بيته؛ لأنه إليه مآلهم وإليهم مآله (maqayis)؛ آل الرجل أهله وقرابته (jamhara)؛ آل الرجل أهله وعياله؛ وآله أيضا أتباعه (sihah)؛ إلة الرجل أهل بيته؛ إيلة الرجل فهم أصله الذين يؤول إليهم (tahdhib)","source_summary":"Kaynaklar kişinin ailesi ve ev halkında birleşir; yakınlar, bakmakla yükümlü olunanlar ve bağlı kimseler bu çekirdeğin kapsam genişlikleridir.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه آل الرجل: أهل بيته وعياله وقرابته وأتباعه ومن إليه مآل الرجل أو مآلهم إليه، مع استعمال آل فلان في الرجل نفسه على جهة التعبير عنه بآله.","what_is_not_ar":"ليس الآل بمعنى الشخص المرئي أو السراب، ولا السياسة، ولا التأويل."},"support_links":[]},{"boundary":"Bu dal salt sonuca varma ya da genel iyilik durumu değildir; sorumluluk üstlenerek yönetme, toplama veya düzeltme işlemi gerekir.","branch_kind":"mixed_non_bare","branch_ref":"root_000067/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"iyi yönetip düzene koyma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğu veya işi iyi yönetip gözetmeyi ifade eder."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Malı ya da dağınık bir işi düzeltip toparlayarak işler duruma getirmeyi ifade eder."}}],"root_ar":"ء و ل","root_id":"root_000067","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Topluluk, mal veya iş üzerinde yönetme, gözetme, toplama ve düzeltme işlemlerini birlikte anlatır.","boundary_detail":"Bu dal salt sonuca varma ya da genel iyilik durumu değildir; sorumluluk üstlenerek yönetme, toplama veya düzeltme işlemi gerekir.","branch_image_ar":"إيالة الأمر بإصلاحه وسياسته","concept_gloss":"iyi yönetip düzene koyma","contextual_glosses":[{"applicability":"Bir topluluk, mal veya iş etkin biçimde yönetilip düzene konurken doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yönetme, gözetme ve işleri düzene koyma yönlerini bağlam içinde korur."},"facet_ids":["F001","F002"],"text":"çekip çevirmek","usage_role":"contextual"}],"definition":"Bir topluluğu, malı veya işi sorumluluk alarak iyi yönetmek, gözetmek, dağınıklığını toplamak ve işler duruma getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğu veya işi iyi yönetip gözetmeyi ifade eder."},{"facet_id":"F002","role":"core","statement":"Malı ya da dağınık bir işi düzeltip toparlayarak işler duruma getirmeyi ifade eder."}],"identity_rationale":"Kaynak ifadesi bir topluluğu veya malı iyi yönetme, gözetme, düzene koyma ve onarma işlemlerini birlikte verir. Dal çerçevesi yönetim ile iyileştirme arasındaki kurucu bağı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"iyi yönetme ve gözetme"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yöneticinin halkını iyi yönetip gözetmesi"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"malını düzeltip iyi yönetmek"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"düzeltme ve iyi yönetme"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"Tanrı işini toparlayıp düzeltsin"}],"lexicalization_note":"Genel yönetme ve düzeltme çekirdeği korunur; halkı yönetme, malı düzeltme ve işi toparlama anlamları kendi söz dizimsel yapılarıyla belirtilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; görev ve yöneticilik komşusu en açıklayıcı karşılaştırmadır, diğerleri yalnız düzeltme, engelleme veya bakım yanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sorumluluk alanını iyi yönetip düzeltme eylemidir; komşu dal ise topluluk üzerindeki görevli veya yönetici konumunu ve bu konumun türlerini öne çıkarır.","focus_only":"Odak dal malı veya herhangi bir işi düzeltip toparlamaya da uygulanır.","gloss":"topluluk üzerinde yöneticilik","neighbor_only":"Komşu dal belirli bir topluluk üzerinde görev, vergi toplama işi, başkanlık veya yöneticilik makamını içerir.","neighbor_ref":"root_000709/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir topluluğun işlerini üstlenme ve onu yönetme alanında buluşur."}],"source_phrase_ar":"الإيالة السياسة؛ آل الرجل رعيته يؤولها إذا أحسن سياستها (maqayis)؛ الايالة السياسة؛ آل الأمير رعيته يؤولها أولا وإيالا؛ آل ما له أي أصلحه وساسه (sihah)؛ ألت الشيء جمعته وأصلحته؛ أول الله عليك أمرك أي جمعه (tahdhib)","source_summary":"Kaynaklar iyi yönetme ve gözetme üzerinde birleşir; malı düzeltme, dağınık işi toplama ve düzene koyma aynı etkin çekirdeğin uygulamalarıdır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الإيالة والسياسة، وآل الأمير رعيته إذا ساسها، وآل ماله إذا أصلحه، والائتيال والإصلاح وجمع الأمر أو رد الضالة في الدعاء.","what_is_not_ar":"ليس مجرد المآل والتفسير، ولا آل الأهل، ولا الأداة."},"support_links":[]},{"boundary":"Bu dal soyut bir sonuca varma değildir; akışkanın fiziksel olarak koyulaşması veya pıhtılaşması gerekir.","branch_kind":"bare","branch_ref":"root_000067/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"koyulaşıp pıhtılaşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir akışkanın yoğunlaşıp koyulaşması veya pıhtılaşmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bal veya katranın ateşle koyulaştırılması, sürecin ısıyla gerçekleştirilen özel biçimidir."}}],"root_ar":"ء و ل","root_id":"root_000067","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Akışkanın yoğunlaşarak koyulaşmasını veya pıhtılaşmasını süreç ve sonuç bağıyla anlatır.","boundary_detail":"Bu dal soyut bir sonuca varma değildir; akışkanın fiziksel olarak koyulaşması veya pıhtılaşması gerekir.","branch_image_ar":"خثور السائل وانعقاده في آخر أمره","concept_gloss":"koyulaşıp pıhtılaşma","contextual_glosses":[{"applicability":"Süt, katran veya bal gibi bir maddenin akışkanlığını yitirmesi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Maddenin yoğunlaşıp daha az akışkan duruma gelmesini korur."},"facet_ids":["F001"],"text":"koyulaşmak","usage_role":"contextual"}],"definition":"Süt, katran veya bal gibi bir akışkanın süreç sonunda yoğunlaşarak koyulaşması, pıhtılaşması ya da katılaşmaya yaklaşmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir akışkanın yoğunlaşıp koyulaşması veya pıhtılaşmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Bal veya katranın ateşle koyulaştırılması, sürecin ısıyla gerçekleştirilen özel biçimidir."}],"identity_rationale":"Kaynak ifadesi süt, katran veya bal gibi akışkanların koyulaşıp pıhtılaşmasını açıkça bildirir; bazı örneklerde bunun kendiliğinden, bazılarında ısıyla gerçekleştiği görülür. Dal çerçevesi fiziksel değişimi doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"sütün koyulaşıp pıhtılaşması"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"katranın veya balın koyulaşıp katılaşması"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"pıhtılaşmış süt"}],"lexicalization_note":"Tanım yalın fiziksel koyulaşma dalına bağlıdır ve başka dallardaki soyut dönüş, yönetim veya araç anlamlarını içermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; içeceğin pıhtılaşması en yakın sınırı verir, kalanlar karıştırma, ufalama, yağ oluşumu veya yalnız ısıyla yoğunlaşma gibi ayrı süreçlerdir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal içeceklerle ve belirgin bir pıhtı kıvamıyla sınırlıdır; odak dalın madde kapsamı katran ve bala kadar genişler ve ısıyla koyulaştırmayı da içerebilir.","focus_only":"Odak dal süt dışında katran ve balı, ayrıca ateşle koyulaştırma örneğini kapsar.","gloss":"içeceğin koyulaşıp pıhtılaşması","neighbor_only":"Komşu dal içeceğin karaciğere benzer ölçüde özel bir yoğunluğa ulaşmasını belirtir.","neighbor_ref":"root_001280/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da sütün veya başka bir içeceğin yoğunlaşıp pıhtılaşmasını anlatır."}],"source_phrase_ar":"آل اللبن أي خثر؛ لا يخثر إلا آخر أمره؛ آل القطران إذا خثر (maqayis)؛ آل القطران أو العسل إذا أعقد بالنار (jamhara)؛ آل القطران والعسل أي خثر؛ الآيل اللبن الخاثر (sihah)","source_summary":"Kaynaklar süt, katran ve bal gibi maddelerin koyulaşıp pıhtılaşmasında birleşir; aktarım, sürecin kendiliğinden son aşamada veya ateşle gerçekleşebildiğini gösterir.","sources":["MQ","JA","SI"],"what_is_ar":"يدخل فيه آل اللبن أو النبات أو القطران أو العسل إذا خثر أو انعقد، والآيل اللبن الخاثر.","what_is_not_ar":"ليس رجوعا معنويا ولا سياسة ولا أداة، وإن علله بعض المصدر بآخر الأمر."},"support_links":[]},{"boundary":"Görünen siluet, uzaktan beliren görüntü ve nesnenin uçları aynı aktarımda buluşur; görüntünün doğrudan serap sayılması kesinleştirilemez.","branch_kind":"bare","branch_ref":"root_000067/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"görünür siluet ve dış uçlar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya nesnenin uzaktan seçilen görünür siluetidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir dağ gibi nesnenin dış uçları ve yanları, görünür dış çizgi anlamının uzantısıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sabah ve akşam görülen yükselmiş görüntü bir aktarımda serap sayılırken başka bir aktarımda seraptan ayrılır."}}],"root_ar":"ء و ل","root_id":"root_000067","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Uzaktan seçilen kişi veya nesne görüntüsü ile nesnenin görünür uç ve yanlarını birlikte temsil eder.","boundary_detail":"Görünen siluet, uzaktan beliren görüntü ve nesnenin uçları aynı aktarımda buluşur; görüntünün doğrudan serap sayılması kesinleştirilemez.","branch_image_ar":"الشخص المترائي والطرف الظاهر","concept_gloss":"görünür siluet ve dış uçlar","contextual_glosses":[{"applicability":"Bir kişi ya da nesne uzaktan yalnız dış çizgileriyle seçildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesnenin uçları ve yanları anlamını dışarıda bırakır.","preserves":"Uzaktan seçilen görünür kişi veya nesne biçimini korur."},"facet_ids":["F001"],"text":"siluet","usage_role":"contextual"}],"definition":"Bir kişi ya da nesnenin uzaktan seçilen görünür silueti veya bir nesnenin dışa uzanan uçları ve yanlarıdır. Sabah ya da akşam cisimleri yükselmiş gibi gösteren görüntü de buraya aktarılır, ancak bunun serap sayılıp sayılmadığı kesin değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya nesnenin uzaktan seçilen görünür siluetidir."},{"facet_id":"F002","role":"extension","statement":"Bir dağ gibi nesnenin dış uçları ve yanları, görünür dış çizgi anlamının uzantısıdır."},{"facet_id":"F003","role":"source_variant","statement":"Sabah ve akşam görülen yükselmiş görüntü bir aktarımda serap sayılırken başka bir aktarımda seraptan ayrılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Görüntünün kesinlikle ışık kırılmasına dayalı yanılsama olduğu anlamını ekler.","collision":"Kaynak aktarımının bir bölümü bu görüntüyü açıkça seraptan ayırır.","fit":"displacement","loses":"Kişi ya da nesnenin gerçek silueti ile nesnenin uçları ve yanlarını dışarıda bırakır.","preserves":"Sabah veya akşam görülen uzaktan görüntü olma yönünü kısmen korur."},"text":"serap"}],"identity_rationale":"Kaynak ifadesi görünen kişi ya da nesne siluetini ve bir şeyin uçlarıyla yanlarını aynı dalda verir. Ayrıca sabah ve akşam görülen yükselmiş görüntünün serap olup olmadığı konusunda kaynak içi karşıt anlatım bulunduğundan dal ancak bu ayrım açıkça korunarak kullanılabilir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"görünür siluet; uzaktan beliren görüntü"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"adamın görünen silueti"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"dağın uçları ve yanları"}],"lexicalization_note":"Tanım yalın görünür siluet ve uç anlamlarını korur; aile veya başka kalıplaşmış anlamlar bu dala taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kenar ve yan komşusu uç anlamını en iyi sınırlar, diğer adaylar yükselti, yüzey veya beden yanı gibi daha dar alanlardadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal somut kenar ve yan kavramına dayanır; odak dal bu alanı kapsamakla birlikte görünür siluet ve uzaktan beliren görüntü çekirdeğine de sahiptir.","focus_only":"Odak dal kişi veya nesnenin uzaktan görünen siluetini ve günün belli saatlerinde beliren görüntüyü de içerir.","gloss":"nesnenin kenarı ve yanı","neighbor_only":"Komşu dal kuyu ve gök gibi alanların kenar ve yönlerine, ayrıca bu adın çekimli sayı biçimlerine uzanır.","neighbor_ref":"root_000548/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir nesnenin dış tarafını, yanını veya sınır bölgesini anlatabilir."}],"source_phrase_ar":"آل الرجل شخصه؛ آل كل شيء؛ آل الجبل أطرافه ونواحيه (maqayis)؛ الآل السراب؛ آل كل شيء شخصه (jamhara)؛ الآل الشخص؛ الآل الذي تراه في أول النهار وآخره كأنه يرفع الشخوص وليس هو السراب (sihah)","source_summary":"Aktarımlar görünür kişi veya nesne silueti ile dış uçları bildirir; sabah ve akşam cisimleri yükselmiş gibi gösteren görüntünün serapla özdeş olup olmadığı konusunda ise ayrışır.","sources":["MQ","JA","SI"],"what_is_ar":"يدخل فيه الآل بمعنى الشخص أو ما يتراءى في أول النهار وآخره ويرفع الشخوص، وأطراف الشيء ونواحيه كآل الجبل والبعير والخيمة.","what_is_not_ar":"الجمهرة تسمي الآل السراب، والصحاح يقول ليس هو السراب؛ ولا يدخل فيه آل الأهل."},"support_links":[]},{"boundary":"Bu dal içinde bulunulan durumdur; kullanılan araç, taşıyıcı yapı veya nesnenin ilk bölümü değildir.","branch_kind":"bare","branch_ref":"root_000067/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"içinde bulunulan durum","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şeyin içinde bulunduğu mevcut durumu belirtir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kötü durumda bulunma, bu genel durum anlamının açık örneğidir."}}],"root_ar":"ء و ل","root_id":"root_000067","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin veya şeyin belirli andaki iyi, kötü ya da başka türlü durumunu genel olarak anlatır.","boundary_detail":"Bu dal içinde bulunulan durumdur; kullanılan araç, taşıyıcı yapı veya nesnenin ilk bölümü değildir.","branch_image_ar":"آلة الحال التي يكون عليها الشيء","concept_gloss":"içinde bulunulan durum","contextual_glosses":[{"applicability":"Bir kişinin ya da şeyin o sıradaki durumu kısa ve doğal biçimde belirtilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İçinde bulunulan durumu bağlam içinde korur."},"facet_ids":["F001"],"text":"hal","usage_role":"contextual"}],"definition":"Bir kişinin ya da şeyin belirli bir anda içinde bulunduğu iyi, kötü veya başka türlü durumdur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şeyin içinde bulunduğu mevcut durumu belirtir."},{"facet_id":"F002","role":"example","statement":"Kötü durumda bulunma, bu genel durum anlamının açık örneğidir."}],"identity_rationale":"Kaynak ifadesi ilgili sözcüğü doğrudan bir kişi ya da şeyin içinde bulunduğu durum olarak tanımlar ve kötü durum örneği verir. Dal çerçevesi bu soyut durum anlamını doğru biçimde araç anlamından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"içinde bulunulan durum"}],"lexicalization_note":"Tanım yalnız yalın durum anlamını verir ve aynı biçimin araç ya da taşıyıcı nesne anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eş anlamlı durum dalı yayımlandı, diğerleri aşama, ortam, eksiklik, kötülük veya durum değişikliği gibi ek sınırlar taşır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kanıtlarda kapsam, koşul veya katılımcı ayrımı görünmediğinden iki dal aynı durum çekirdeğini ve aynı sınırı paylaşır.","focus_only":null,"gloss":"mevcut durum","neighbor_only":null,"neighbor_ref":"root_001180/B005","relation_type":"synonym","shared_zone":"Her iki dal da bir kişi ya da şeyin içinde bulunduğu mevcut durumu belirtir."}],"source_phrase_ar":"الآلة الحالة (maqayis)؛ والآلة الحالة (jamhara)؛ والآلة الحالة يقال هو بآلة سوء (sihah)","source_summary":"Kaynaklar bu kullanımı bir kişi ya da şeyin içinde bulunduğu durum olarak ortak biçimde tanımlar ve kötü durum anlatımını örnekler.","sources":["MQ","JA","SI"],"what_is_ar":"يدخل فيه الآلة أو الألة بمعنى الحالة، كقولهم هو بآلة سوء.","what_is_not_ar":"ليس الآلة بمعنى الأداة أو الخشبات أو الجنازة، ولا آل الأهل."},"support_links":[]},{"boundary":"Bu dal iş görmeye veya taşımaya yarayan somut nesnedir; soyut durum anlamını kapsamaz.","branch_kind":"bare","branch_ref":"root_000067/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"araç ve taşıyıcı düzen","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işi yapmaya veya bir amacı gerçekleştirmeye yarayan somut araçtır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çadırı ayakta tutan direkler, destekleyici araç türüdür."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ölüyü taşımaya yarayan sedye, taşıyıcı araç türüdür."}}],"root_ar":"ء و ل","root_id":"root_000067","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İş görmeye, desteklemeye veya taşımaya yarayan somut nesneleri ortak işlevleriyle kapsar.","boundary_detail":"Bu dal iş görmeye veya taşımaya yarayan somut nesnedir; soyut durum anlamını kapsamaz.","branch_image_ar":"الآلة الحاملة أو الأداة","concept_gloss":"araç ve taşıyıcı düzen","contextual_glosses":[{"applicability":"Belirli bir işi yapmaya yarayan somut nesne genel olarak adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir amaca hizmet eden somut nesne çekirdeğini korur."},"facet_ids":["F001"],"text":"araç","usage_role":"general"}],"definition":"Bir işin yapılmasına, bir yapının ayakta tutulmasına veya bir yükün taşınmasına yarayan somut araç ya da taşıyıcı düzendir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işi yapmaya veya bir amacı gerçekleştirmeye yarayan somut araçtır."},{"facet_id":"F002","role":"specialization","statement":"Çadırı ayakta tutan direkler, destekleyici araç türüdür."},{"facet_id":"F003","role":"specialization","statement":"Ölüyü taşımaya yarayan sedye, taşıyıcı araç türüdür."}],"identity_rationale":"Kaynak ifadesi genel aracı, çadırı taşıyan direkleri ve ölüyü taşıyan sedyeyi aynı taşıma ya da işe yarama alanında verir. Dal çerçevesi araç çekirdeği ile özel taşıyıcı örnekleri doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"araç"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"çadır direkleri ve taşıyıcı ağaçları"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"cenaze veya ölüyü taşıyan sedye"}],"lexicalization_note":"Tanım yalın araç ve taşıyıcı nesne anlamını korur; çadır direkleri ile cenaze sedyesi bu çekirdeğin özel gerçekleşmeleridir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel araç dalı en yakın karşılaştırmadır, diğerleri belirli bir iğne, taşıt, destek, anahtar, eksen veya yapı parçasıyla sınırlıdır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kanıtlarda çekirdek kapsamı değiştiren bir koşul, katılımcı veya kullanım sınırı görünmez; özel nesne türleri bağımlı örneklerdir.","focus_only":null,"gloss":"araç ve gereç","neighbor_only":null,"neighbor_ref":"root_000021/B004","relation_type":"synonym","shared_zone":"Her iki dal da bir işin yapılmasına veya bir amacın gerçekleştirilmesine yarayan araç ve gereçleri anlatır."}],"source_phrase_ar":"آل الخيمة العمد (maqayis)؛ الآلة الأداة؛ خشبات تبنى عليها الخيمة؛ الآلة الجنازة (sihah)","source_summary":"Kaynaklar somut araç ve taşıyıcı yapı alanını verir; çadır direkleri destekleme, cenaze sedyesi ise taşıma işlevinin özel örnekleridir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه الآلة بمعنى الأداة، وخشبات الخيمة، والجنازة أو الحامل الذي يحمل عليه.","what_is_not_ar":"ليس الحالة، ولا التأويل، ولا آل الأهل."},"support_links":[]},{"boundary":"Dal belirli bir erkek dağ keçisini adlandırır; genel olarak dağa sığınma eylemini ya da bütün dağ hayvanlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_000067/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"erkek yabani dağ keçisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dağlık yerde yaşayan yabani keçilerin erkek bireyini adlandırır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanın dağa sığınıp korunması, adlandırmayı açıklayan ilişkili bir özelliktir."}}],"root_ar":"ء و ل","root_id":"root_000067","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dağlık yerde yaşayan yabani keçinin erkek bireyini eksiksiz ve doğal biçimde belirtir.","boundary_detail":"Dal belirli bir erkek dağ keçisini adlandırır; genel olarak dağa sığınma eylemini ya da bütün dağ hayvanlarını kapsamaz.","branch_image_ar":"الأيل الذي يأوي إلى الجبل","concept_gloss":"erkek yabani dağ keçisi","contextual_glosses":[{"applicability":"Yabanilik bağlamdan açık olduğunda hayvanı doğal Türkçeyle adlandırmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dağ keçisi türünü ve erkek birey ayrımını korur."},"facet_ids":["F001"],"text":"erkek dağ keçisi","usage_role":"contextual"}],"definition":"Dağlık yerde yaşayan yabani keçilerin erkek bireyidir; dağa sığınıp korunması, adın açıklaması olarak aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dağlık yerde yaşayan yabani keçilerin erkek bireyini adlandırır."},{"facet_id":"F002","role":"associated_use","statement":"Hayvanın dağa sığınıp korunması, adlandırmayı açıklayan ilişkili bir özelliktir."}],"identity_rationale":"Kaynak ifadesi bu adı dağ keçilerinin erkeği için açıkça verir; dağa sığınıp korunması adlandırmaya ilişkin bir açıklamadır, hayvan türünün kurucu tanımının yerine geçmez.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"erkek yabani dağ keçisi"}],"lexicalization_note":"Tanım yalın hayvan adını verir; dağa sığınma açıklaması bağımlı bir gerekçe olarak kalır ve genel fiil anlamına dönüştürülmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yabani dağ keçisi komşusu tür ve cinsiyet sınırını en iyi açıklar, diğer adaylar hastalık, farklı hayvan, barınak veya davranış alanındadır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalın cinsiyet sınırı erkektir; komşu dalın temel kullanımı dişi bireydir ve bazı aktarımlarda cinsiyet kapsamı genişleyebilir.","focus_only":"Odak dal yalnız erkek yabani dağ keçisini adlandırır.","gloss":"dişi ya da genel yabani dağ keçisi","neighbor_only":"Komşu dal dişi yabani dağ keçisini, bazı aktarımlarda ise her iki cinsi ve çoğul topluluğu adlandırabilir.","neighbor_ref":"root_000615/B011","relation_type":"same_field","shared_zone":"Her iki dal da dağlık yerde yaşayan yabani keçileri adlandırır."}],"source_phrase_ar":"الأيل الذكر من الوعول؛ لأنه يؤول إلى الجبل يتحصن (maqayis)؛ الايل أيضا الذكر من الاوعال (sihah)","source_summary":"Kaynaklar adın erkek yabani dağ keçisini gösterdiğinde birleşir; dağa sığınıp korunma davranışı adlandırmanın açıklaması olarak eklenir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه الأيل: ذكر الوعول، مع تعليل تسميته بأنه يؤول إلى الجبل يتحصن.","what_is_not_ar":"ليس آل يؤول الفعل العام، ولا آل الأهل، ولا الآلة."},"support_links":[]},{"boundary":"Bu dal herhangi bir kap değil, içeceği birkaç gün bekletip olgunlaştırmaya ayrılmış kaptır; koyulaşma sürecinin kendisi değildir.","branch_kind":"bare","branch_ref":"root_000067/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"içecek olgunlaştırma kabı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İçeceği birkaç gün toplu halde bekletmeye yarayan özel bir kaptır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kabın işlevsel sonucu, içeceğin bekleme süresinde olgunlaşmasıdır."}}],"root_ar":"ء و ل","root_id":"root_000067","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İçeceğin birkaç gün bekletilerek olgunlaştırılmasına ayrılmış özel kabı kısa ve eksiksiz biçimde adlandırır.","boundary_detail":"Bu dal herhangi bir kap değil, içeceği birkaç gün bekletip olgunlaştırmaya ayrılmış kaptır; koyulaşma sürecinin kendisi değildir.","branch_image_ar":"الإيال وعاء الشراب حتى يجود","concept_gloss":"içecek olgunlaştırma kabı","contextual_glosses":[{"applicability":"İçeceğin bekletilerek olgunlaşması bağlamında kısa bir işlev adı gerektiğinde kullanılır.","error_profile":{"adds":"Kaynakta açıkça belirtilmeyen belirli bir mayalanma sürecini çağrıştırabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"İçeceği bir süre bekleterek değiştirme ve olgunlaştırma işlevini korur."},"facet_ids":["F001","F002"],"text":"mayalama kabı","usage_role":"contextual"}],"definition":"İçeceğin birkaç gün boyunca içinde toplanıp bekletildiği ve böylece olgunlaşmasının sağlandığı özel kaptır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İçeceği birkaç gün toplu halde bekletmeye yarayan özel bir kaptır."},{"facet_id":"F002","role":"core","statement":"Kabın işlevsel sonucu, içeceğin bekleme süresinde olgunlaşmasıdır."}],"identity_rationale":"Tek kaynak ifadesi, içeceğin birkaç gün boyunca içinde toplanıp olgunlaştığı özel kabı doğrudan tanımlar. Dal çerçevesi kabın işlevini ve bekletme süresini eksiksiz korur.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"içecek olgunlaştırma kabı"}],"lexicalization_note":"Tanım yalın özel kap adını korur; genel araç, genel içecek kabı veya içeceğin fiziksel değişimi anlamlarına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel büyük kap en yakın karşılaştırmadır, diğerleri bardak, deri tekne, tulum veya oyulmuş ağaç gibi farklı kap türleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal biçimsel olarak büyük bir küp veya genel kaptır; odak dalın ayırt edici sınırı içeceği birkaç gün bekletip olgunlaştırma işlevidir.","focus_only":"Odak dal içeceği birkaç gün bekletip olgunlaştırma işleviyle tanımlanır.","gloss":"büyük küp veya kap","neighbor_only":"Komşu dal büyük küp ya da genel kap türüdür ve içeceği olgunlaştırma işlevi zorunlu değildir.","neighbor_ref":"root_000384/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da sıvı veya içecek koyulabilen bir kap türünü anlatır."}],"source_phrase_ar":"الإيال على فعال وعاء يجمع فيه الشراب اياما حتى يجود (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu özel kap, içeceği birkaç gün bir arada bekleterek olgunlaştırmak için kullanılır."}],"source_summary":"Tek aktarım, kabı içeceğin birkaç gün bekletilip olgunlaştırıldığı özel bir kap olarak tanımlar.","sources":["MQ"],"what_is_ar":"يدخل فيه الإيال: وعاء يجمع فيه الشراب أياما حتى يجود.","what_is_not_ar":"ليس الخثور نفسه، ولا الأداة العامة، ولا التأويل."},"support_links":[]},{"boundary":"Bu dal yalnız belirli bir yem bitkisinin adıdır; söz açıklama, sonuç veya genel otlak anlamlarını kapsamaz.","branch_kind":"non_bare","branch_ref":"root_000067/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"kumda yetişen yem bitkisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kumlu yerde yetişen belirli bir ot ya da bitkiyi adlandırır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eşekler ve yabani sığırlar tarafından yenmesi, bitkinin ilişkili yem özelliğidir."}}],"root_ar":"ء و ل","root_id":"root_000067","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kumlu yerde yetişme ve hayvanlarca yenme özellikleriyle kanıtlanan özel bitki adını açıklayıcı biçimde verir.","boundary_detail":"Bu dal yalnız belirli bir yem bitkisinin adıdır; söz açıklama, sonuç veya genel otlak anlamlarını kapsamaz.","branch_image_ar":"التأويل اسم بقلة معزول","concept_gloss":"kumda yetişen yem bitkisi","contextual_glosses":[{"applicability":"Özel bitki adının Türkçede yerleşik karşılığı bulunmadığında türünü açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kumda yetişme ve özellikle eşeklerle yabani sığırların yeme ayrıntılarını dışarıda bırakır.","preserves":"Hayvanların yediği bir bitki olma özelliğini korur."},"facet_ids":["F001","F002"],"text":"bir yem otu","usage_role":"explanatory"}],"definition":"Kumlu yerde yetişen, eşeklerin ve özellikle yabani sığırların severek yediği belirli bir yem bitkisinin adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kumlu yerde yetişen belirli bir ot ya da bitkiyi adlandırır."},{"facet_id":"F002","role":"associated_use","statement":"Eşekler ve yabani sığırlar tarafından yenmesi, bitkinin ilişkili yem özelliğidir."}],"identity_rationale":"Tek kaynak ifadesi bu sözcüğü kumda yetişen ve eşeklerle yabani sığırların yediği belirli bir bitki adı olarak verir. Dalın, aynı biçimdeki söz açıklama anlamından ayrı tutulması kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"kumda yetişen bir yem bitkisi"}],"lexicalization_note":"Tanım yalnız kanıtlanan özel bitki adına bağlıdır ve biçim benzerliğinden genel bir kök ya da söz açıklama anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hayvanların otladığı belirli bitki komşusu en açıklayıcıdır, diğer adaylar farklı bitki türleri, otlak veya otlama eylemidir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal kumlu yer, eşek ve yabani sığır bağlantısıyla tanınır; komşu dal koyunların sevdiği başka bir bitkiyi ve onun bol yetiştiği araziyi kapsar.","focus_only":"Odak dal kumlu yerde yetişen ve eşeklerle yabani sığırların yediği özel bir bitkidir.","gloss":"koyunların otladığı yeşil yem bitkisi","neighbor_only":"Komşu dal koyunların sevdiği, yeşil kaldığı sürece otlanan başka bir bitkiyi ve bu bitkinin bolca yetiştiği araziyi de adlandırır.","neighbor_ref":"root_000160/B007","relation_type":"same_field","shared_zone":"Her iki dal da otlayan hayvanların yediği belirli bir yem bitkisini adlandırır."}],"source_phrase_ar":"التأويل نبت يعتلفه الحمار؛ التأويل اسم بقلة يولع بها بقر الوحش تنبت في الرمل (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Ad, kumlu yerde yetişen ve eşeklerle yabani sığırların yediği özel bir yem bitkisini gösterir."}],"source_summary":"Tek aktarım, adı kumda yetişen ve eşeklerle yabani sığırlar tarafından yenen belirli bir bitkiye verir.","sources":["TA"],"what_is_ar":"يدخل فيه التأويل اسما لنبت أو بقلة ترعاها البهائم، كما ورد في تهذيب اللغة.","what_is_not_ar":"ليس تأويل الكلام ولا المرجع والمصير."},"support_links":[]},{"boundary":"Dal, yazı yaprağını, bağlı yapraklar bütününü, yayvan kabı veya okuma yanlışını değil; yayılmış geniş yüzeyi ve buna bağlı özel kullanımları anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000845/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صُحُف","morph_features":"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"87:18:4:2","qac_word_ref":"87:18:4","surface_ar":"صُّحُفِ"}],"gloss":"yayılmış geniş yüzey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin yayılması ve geniş bir yüzey görünümü kazanması temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yeryüzünün görünen yüzü, yayılmış geniş yüzeyin özel bir gerçekleşmesidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsan yüzünün dış derisi, geniş ve açık yüzey düşüncesine bağlı özel bir kullanımdır."}}],"root_ar":"ص ح ف","root_id":"root_000845","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel çekirdeği ve özel yüzey kullanımlarının dayandığı ortak görünümü birlikte karşılar.","boundary_detail":"Dal, yazı yaprağını, bağlı yapraklar bütününü, yayvan kabı veya okuma yanlışını değil; yayılmış geniş yüzeyi ve buna bağlı özel kullanımları anlatır.","branch_image_ar":"انبساط وسعة","concept_gloss":"yayılmış geniş yüzey","contextual_glosses":[{"applicability":"Yalnızca yayılmış yüzeyin yeryüzünün görünen yüzünü anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":"Tek başına bütün yerküreyi de anlatabildiği için bağlamla sınırlandırılmalıdır.","fit":"narrowing","loses":"Genel yayılma çekirdeğini ve yüz derisi kullanımını dışarıda bırakır.","preserves":"Yeryüzünün görünen yüzü olan özel gerçekleşmeyi korur."},"facet_ids":["F002"],"text":"yeryüzü","usage_role":"contextual"},{"applicability":"İnsan yüzünün dış derisini belirten kalıplaşmış kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel geniş yüzey anlamını ve yeryüzü kullanımını karşılamaz.","preserves":"İnsan yüzünün dış derisine ilişkin özel kullanımı korur."},"facet_ids":["F003"],"text":"yüz derisi","usage_role":"contextual"}],"definition":"Bir şeyin yayılıp geniş bir yüzey oluşturması ya da böyle yayılmış yüzeyin kendisidir. Yeryüzünün görünen yüzü ve insan yüzünün dış derisi bu çekirdeğin özel adlandırmalarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin yayılması ve geniş bir yüzey görünümü kazanması temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Yeryüzünün görünen yüzü, yayılmış geniş yüzeyin özel bir gerçekleşmesidir."},{"facet_id":"F003","role":"specialization","statement":"İnsan yüzünün dış derisi, geniş ve açık yüzey düşüncesine bağlı özel bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi, dalın temelini bir şeydeki yayılma ve genişlik olarak kurar; yeryüzünün görünen yüzü ile insan yüzünün derisini de bu geniş yüzey düşüncesinin özel gerçekleşmeleri olarak verir. Bu nedenle sunulan dal kimliği kaynak anlatımıyla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yayılmış geniş yüzey"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yeryüzünün görünen yüzü"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yüz derisi"}],"lexicalization_note":"Tanım, genel yayılma ve geniş yüzey çekirdeğini korurken yeryüzü ve yüz derisi gibi kalıplaşmış kullanımları bu çekirdekten ayrı özel yüzey adları olarak sınırlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca yayılma, düz arazi ve geniş yüzey bakımından dal sınırını belirginleştiren üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal geniş yüzey görünümünü ve bu görünümün yeryüzü ile yüz derisindeki adlarını öne çıkarır; komşu dal ise yayma ve uzatma sürecini daha geniş bir eylem alanında anlatır.","focus_only":"Bu dal, yayılmanın ortaya çıkardığı geniş yüzeyi ve onun özel yüzey adlarını da kapsar.","gloss":"yayma ve genişletme","neighbor_only":"Komşu dal, bir şeyi yayma, uzatma ve genişletme eylemini daha genel biçimde kapsar.","neighbor_ref":"root_000928/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda bir şeyin açılarak yayılması ve genişlik kazanması ortak alandır."},{"boundary_match":"partial","distinction":"Odak dal genel yüzey genişliğini anlatır; komşu dal ise belirli düz, açık veya alçak arazi türlerini adlandırdığı için olağan bağlamda birbirlerinin yerine geçmez.","focus_only":"Odak dal her türlü yayılmış geniş yüzeyi ve yüz derisi gibi özel kullanımları kapsar.","gloss":"düz açık arazi","neighbor_only":"Komşu dal açık, düz veya çukurca belirli arazi biçimlerini ve geniş yolu adlandırır.","neighbor_ref":"root_000734/B009","relation_type":"near_neighbor","shared_zone":"Yeryüzünün geniş ve açık bir yüzey olarak görülmesi iki dalı birbirine yaklaştırır."},{"boundary_match":"partial","distinction":"Odak dal yayılma ve genişliği kurucu özellik sayar; komşu dal ise yan, kenar ve nesnenin belirli yüzü gibi konumsal bölümleri de kapsayan daha başka bir örgüye sahiptir.","focus_only":"Odak dalın çekirdeği bir şeyin yayılması ve geniş yüzey görünümüdür.","gloss":"yan ve enli yüz","neighbor_only":"Komşu dal bir nesnenin yanı, yüzü, kenarı veya özellikle enli hale getirilmiş biçimini kapsar.","neighbor_ref":"root_000867/B001","relation_type":"near_neighbor","shared_zone":"Bir nesnenin geniş görünen yüzü her iki dalın anlam alanına yaklaşabilir."}],"source_phrase_ar":"أصل صحيح يدل على انبساط في شيء وسعة (maqayis); الصحيف وجه الأرض (maqayis); صحيفة الوجه بشرة جلده (ayn); الصحيفة المبسوط من الشيء كصحيفة الوجه (mufradat)","source_summary":"Kaynakların ortak çerçevesi yayılma ve genişliği temel alır; görünen yeryüzü ile yüz derisini de bu yüzey kavrayışına bağlar.","sources":["MQ","AY","MU"],"what_is_ar":"انبساط الشيء وسعته ووجه الأرض وبشرة الوجه","what_is_not_ar":"الصحيفة المكتوبة والمصحف والصحفة والتصحيف"},"support_links":[]},{"boundary":"Dal, tek yazı yaprağı ile ondan oluşan kitap kullanımını kapsar; yüz derisi, yayvan kap, yaprakları kapaklar arasında toplama işlemi ve yanlış okuma bunun dışındadır.","branch_kind":"bare","branch_ref":"root_000845/B002","candidate_links":[{"candidate_id":"cand_49e8bc88876e0bab25ea","lane":"micro"},{"candidate_id":"cand_54c429f748c97833f5b7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صُحُف","morph_features":"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"87:18:4:2","qac_word_ref":"87:18:4","surface_ar":"صُّحُفِ"}],"gloss":"yazı yaprağı veya kitap","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, deri veya benzeri bir malzemeden olup üzerine yazı yazılan ya da yazı taşıyan tek yapraktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı ad kimi kullanımda yazılı yaprakların oluşturduğu kitap için de kullanılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaynak ifadesi tekil yazı yaprağı için birden çok çoğul biçim bildirir."}}],"root_ar":"ص ح ف","root_id":"root_000845","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek yazı yüzeyini, kitap genişlemesini ve bunların çoğul olarak anılabilmesini kapsayan genel karşılıktır.","boundary_detail":"Dal, tek yazı yaprağı ile ondan oluşan kitap kullanımını kapsar; yüz derisi, yayvan kap, yaprakları kapaklar arasında toplama işlemi ve yanlış okuma bunun dışındadır.","branch_image_ar":"صحيفة مكتوبة","concept_gloss":"yazı yaprağı veya kitap","contextual_glosses":[{"applicability":"Tek bir yazı yüzeyinin veya yazılı yaprağın söz konusu olduğu bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kitap için kullanılan genişlemiş anlamı ve çoğul biçim bilgisini karşılamaz.","preserves":"Üzerine yazılan veya yazı taşıyan tek yaprak çekirdeğini korur."},"facet_ids":["F001"],"text":"yazı yaprağı","usage_role":"general"},{"applicability":"Adın yazılı yapraklardan oluşan bir bütünü belirttiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":"Güncel kullanımda her türlü kitabı anlatabildiği için tarihsel malzeme sınırını tek başına göstermez.","fit":"narrowing","loses":"Tek yazı yaprağı çekirdeğini ve çoğul biçim bilgisini dışarıda bırakır.","preserves":"Yazılı yapraklar bütününe yönelik kitap kullanımını korur."},"facet_ids":["F002"],"text":"kitap","usage_role":"contextual"}],"definition":"Üzerine yazı yazılan veya yazı taşıyan yaprak ya da parçadır; kimi kullanımda bu tür yazılı yapraklardan oluşan kitabı da belirtir. Tekil adın çeşitli çoğul biçimleri vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, deri veya benzeri bir malzemeden olup üzerine yazı yazılan ya da yazı taşıyan tek yapraktır."},{"facet_id":"F002","role":"extension","statement":"Aynı ad kimi kullanımda yazılı yaprakların oluşturduğu kitap için de kullanılır."},{"facet_id":"F003","role":"source_variant","statement":"Kaynak ifadesi tekil yazı yaprağı için birden çok çoğul biçim bildirir."}],"identity_rationale":"Kaynak ifadesi dalı, üzerine yazı yazılan ya da yazı taşıyan tek yaprak ve kimi kullanımda kitap olarak açıkça tanımlar; ayrıca bunun çoğul biçimlerini verir. Sunulan yazılı yaprak çerçevesi bu içeriği doğru biçimde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yazı yazılan yaprak veya kitap"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yazı yaprakları"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yazı yaprakları"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yazı yaprakları için seyrek bir çoğul biçim"}],"lexicalization_note":"Tanım yalın yazı yaprağı anlamında kalır ve yalnızca kaynakta bulunan kitap genişlemesini içerir; başka dallardaki toplama işlemi tanıma taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yazı malzemesi, deri yaprak, içerikli yayın ve bağlı yaprak bütünüyle karışma olasılığını açıklayan dört karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal malzemeden bağımsız olarak yazı yaprağını ve kitap kullanımını kapsar; komşu dal ise yazı yüzeyini malzeme türü üzerinden adlandırır.","focus_only":"Odak dal yazı taşıyan yaprağı, kitap genişlemesini ve çoğul adlandırmaları kapsar.","gloss":"yazı kâğıdı","neighbor_only":"Komşu dal yazı malzemesini özellikle belirli bir bitkisel kâğıt türü veya başka malzemeler bakımından sınırlar.","neighbor_ref":"root_001218/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da üzerine yazı yazılan taşınabilir bir yüzeyi adlandırır."},{"boundary_match":"partial","distinction":"Odak dalın yazı yüzeyi farklı malzemelerden olabilir ve kitap anlamına genişleyebilir; komşu dalın çekirdeği ise belirli bir deri malzemesidir.","focus_only":"Odak dal genel yazı yaprağını, kitap kullanımını ve çoğul biçimleri kapsar.","gloss":"deri yazı yaprağı","neighbor_only":"Komşu dal özellikle işlenmiş deri yaprağını ve onun beyaz ya da açılmış durumunu belirtir.","neighbor_ref":"root_000586/B002","relation_type":"near_synonym","shared_zone":"Yazı yazmaya elverişli veya yazı taşıyan yaprak iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dalı belirleyen şey yazının taşındığı yapraktır; komşu dalda ise yayın veya bilgi içeriği daha belirleyici bir sınır oluşturur.","focus_only":"Odak dal herhangi bir yazı yaprağını veya genel olarak kitabı belirtebilir.","gloss":"bilgi yazısı veya dergi","neighbor_only":"Komşu dal bilgelik ya da bilgi içeriği taşıyan dergi, yaprak veya kitabı özellikle öne çıkarır.","neighbor_ref":"root_000255/B006","relation_type":"near_synonym","shared_zone":"Yazılı bir yaprak ya da kitap görünümü iki dalda da bulunur."},{"boundary_match":"partial","distinction":"Bu dal yaprağın kendisini adlandırır; komşu dal ise yaprakların iki kapak arasında bir araya getirilmesiyle oluşan bütünü kurucu özellik sayar.","focus_only":"Odak dal tek yazı yaprağını ve daha gevşek kitap kullanımını kapsar.","gloss":"bağlı yazı yaprakları bütünü","neighbor_only":"Komşu dal yazılı yaprakların iki kapak arasında toplanmış bütününü ve bu toplama işlemini gerektirir.","neighbor_ref":"root_000845/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalın ortak malzemesi yazılı yapraklardır."}],"source_phrase_ar":"الصحيفة وهي التي يكتب فيها والجمع صحائف والصحف (maqayis); الصحف جمع الصحيفة (ayn); الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها (jamhara); الصحيفة الكتاب والجمع صحف وصحائف (sihah); الصحيفة التي يكتب فيها وجمعها صحائف وصحف (mufradat)","source_summary":"Kaynaklar yazı yazılan yaprak veya parçayı ortak çekirdek olarak verir; kitap kullanımını ve tekil adın farklı çoğul biçimlerini de aynı dalda kaydeder.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"الصحيفة التي يكتب فيها والكتاب والصحف والصحائف","what_is_not_ar":"صحيفة الوجه والصحفة والمصحف والتصحيف"},"support_links":["sup_0ba9419ab25b6e5b671e","sup_7643f4841419c3065d94"]},{"boundary":"Kurucu sınır, yazılı yaprakların bir araya getirilip iki kapak arasında tutulmasıdır; tek yaprak, yalnız okuma eylemi veya metnin tek bir bölümü yeterli değildir.","branch_kind":"bare","branch_ref":"root_000845/B003","candidate_links":[{"candidate_id":"cand_b2f3d9a718de8ab9aa34","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صُحُف","morph_features":"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"87:18:4:2","qac_word_ref":"87:18:4","surface_ar":"صُّحُفِ"}],"gloss":"iki kapak arasında toplanmış yazı yaprakları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sonuç nesnesi, yazılı yaprakların iki kapak arasında toplanmış bütünüdür."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu bütünü kuran eylem, yazılı yaprakları bir araya getirip kapaklar arasında toplamaktır."}}],"root_ar":"ص ح ف","root_id":"root_000845","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaprakların toplanmasıyla oluşan sonuç nesnesini bütün kurucu sınırlarıyla karşılar.","boundary_detail":"Kurucu sınır, yazılı yaprakların bir araya getirilip iki kapak arasında tutulmasıdır; tek yaprak, yalnız okuma eylemi veya metnin tek bir bölümü yeterli değildir.","branch_image_ar":"جمع الصحف في مصحف","concept_gloss":"iki kapak arasında toplanmış yazı yaprakları","contextual_glosses":[{"applicability":"Sonuç nesnesinden çok onu kuran toplama eyleminin anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yazılı yaprakların bir araya getirilmesi ve iki kapak arasında bütünleştirilmesi işlemini korur."},"facet_ids":["F002"],"text":"yazı yapraklarını iki kapak arasında toplamak","usage_role":"explanatory"},{"applicability":"İki kapak arasındaki sonuç nesnesinin kısa ve doğal biçimde anılması için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki kapak sınırını açıkça söylemez ve toplama eylemini karşılamaz.","preserves":"Yazılı yaprakların bağlı bir bütün oluşturması sonucunu korur."},"facet_ids":["F001"],"text":"bağlı yazı yaprakları bütünü","usage_role":"general"}],"definition":"Yazılı yaprakların bir araya getirilip iki kapak arasında tutulmasıyla oluşan bütündür. Aynı dal, yaprakları böyle bir bütün oluşturacak biçimde toplama eylemini de içerir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sonuç nesnesi, yazılı yaprakların iki kapak arasında toplanmış bütünüdür."},{"facet_id":"F002","role":"associated_use","statement":"Bu bütünü kuran eylem, yazılı yaprakları bir araya getirip kapaklar arasında toplamaktır."}],"identity_rationale":"Kaynak ifadesi hem yazılı yaprakların iki kapak arasında toplanması işlemini hem de bu işlemle ortaya çıkan toplanmış bütünü açıkça kurar. Sunulan dal kimliği bu işlem, düzenleme ve sonuç ilişkisini doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"iki kapak arasında toplanmış yazı yaprakları bütünü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yazı yapraklarını iki kapak arasında toplamak"}],"lexicalization_note":"Tanım kaynakta verilen yalın sonuç nesnesi ile onu kuran toplama eylemini korur; tek yaprak ya da genel toplama anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tek yaprak, genel toplama, okuma ve metin bölümüyle sınır farkını gösteren dört komşu yeterli bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın anlamında yaprakların toplanması ve kapaklar arasında bütünleşmesi kurucudur; komşu dalda tek yaprak başlı başına yeterlidir.","focus_only":"Odak dal, yazılı yaprakların iki kapak arasında toplanmış bir bütün oluşturmasını gerektirir.","gloss":"yazı yaprağı","neighbor_only":"Komşu dal tek yazı yaprağını ve genel kitap kullanımını, özel bir toplama işlemi gerektirmeden kapsar.","neighbor_ref":"root_000845/B002","relation_type":"near_neighbor","shared_zone":"Yazılı yaprak iki dalın ortak maddi öğesidir."},{"boundary_match":"partial","distinction":"Odak dalın katılımcıları yazılı yapraklardır ve sonuç kapaklı bir bütündür; komşu dalın toplama alanı genel olup böyle bir malzeme ve sonuç şartı taşımaz.","focus_only":"Odak dal yalnızca yazılı yaprakların kapaklar arasında düzenli biçimde toplanmasını ve sonucunu anlatır.","gloss":"toplama ve elde tutma","neighbor_only":"Komşu dal bir şeyi alma, ele geçirme, elde tutma veya genel olarak toplama eylemlerini kapsar.","neighbor_ref":"root_000018/B001","relation_type":"near_neighbor","shared_zone":"Birden çok şeyi bir araya getirme düşüncesi iki dalda ortaktır."},{"boundary_match":"field_only","distinction":"Odak dal metnin taşıyıcı yapraklarının fiziksel bütünleşmesini anlatırken komşu dal metnin okunmasını ve aktarılmasını anlatır; çekirdekleri ortak değildir.","focus_only":"Odak dal yazılı yaprakların kapaklar arasında toplanmasıyla oluşan nesneyi ve kurma işlemini anlatır.","gloss":"metni okuma","neighbor_only":"Komşu dal metni seslendirme, okuma, başkasına okutma ve birlikte çalışma eylemlerini kapsar.","neighbor_ref":"root_001211/B001","relation_type":"same_field","shared_zone":"Her iki dal yazılı metinlerin kullanıldığı bilgi alanına girer."},{"boundary_match":"field_only","distinction":"Odak dal metni taşıyan yaprakların bütününü kurar; komşu dal ise bu bütün içindeki sınırlı bir metin bölümünü adlandırabilir ve fiziksel toplama şartı taşımaz.","focus_only":"Odak dal, yazılı yaprakların tümünü taşıyan kapaklı fiziksel bütündür.","gloss":"sınırlı metin bölümü","neighbor_only":"Komşu dal metin içindeki çevrelenmiş bir bölümü ve ayrıca yüksek derece anlamını kapsar.","neighbor_ref":"root_000758/B003","relation_type":"same_field","shared_zone":"İki dal da düzenlenmiş yazılı metnin yapısal öğeleriyle ilgilidir."}],"source_phrase_ar":"سمي المصحف مصحفا لأنه أصحف أي جعل جامعا للصحف المكتوبة بين الدفتين (ayn); المصحف لأنه صحف جمعت (jamhara); مصحف مأخوذة من أصحف أي جمعت فيه الصحف (sihah); المصحف ما جعل جامعا للصحف المكتوبة (mufradat)","source_summary":"Kaynakların ortak anlatımı, yazılı yaprakların toplanarak iki kapak arasında bir bütün haline getirilmesini ve ortaya çıkan bağlı bütünü birlikte açıklar.","sources":["AY","JA","SI","MU"],"what_is_ar":"المصحف وما جمع فيه الصحف المكتوبة بين الدفتين","what_is_not_ar":"الصحيفة المفردة والصحفة والتصحيف"},"support_links":["sup_6940b6d1eba667610fc7"]},{"boundary":"Çekirdek geniş, yayvan çanaktır; küçük su biriktirme çukurları ayrı bir uzantıdır ve yazı yaprağı ya da genel geniş yüzey anlamıyla karıştırılmamalıdır.","branch_kind":"bare","branch_ref":"root_000845/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صُحُف","morph_features":"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"87:18:4:2","qac_word_ref":"87:18:4","surface_ar":"صُّحُفِ"}],"gloss":"yayvan çanak; küçük su biriktirme çukuru","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel nesne geniş ağızlı, basık ve yayvan bir çanaktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı ad ailesinin çoğul biçimi, su için yapılan küçük biriktirme çukurlarını da adlandırabilir."}}],"root_ar":"ص ح ف","root_id":"root_000845","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çanak çekirdeği ile aynı ad ailesindeki su biriktirme yeri uzantısını birbirine karıştırmadan birlikte gösterir.","boundary_detail":"Çekirdek geniş, yayvan çanaktır; küçük su biriktirme çukurları ayrı bir uzantıdır ve yazı yaprağı ya da genel geniş yüzey anlamıyla karıştırılmamalıdır.","branch_image_ar":"صَحفة عريضة","concept_gloss":"yayvan çanak; küçük su biriktirme çukuru","contextual_glosses":[{"applicability":"Geniş ağızlı ve basık kap çekirdeğinin söz konusu olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Küçük su biriktirme çukurlarına yönelik uzantıyı karşılamaz.","preserves":"Geniş ağızlı, basık ve yayvan kap çekirdeğini korur."},"facet_ids":["F001"],"text":"yayvan çanak","usage_role":"general"},{"applicability":"Ad ailesinin küçük su toplama yerlerini belirttiği özel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geniş ve yayvan çanak çekirdeğini karşılamaz.","preserves":"Su tutmak için yapılan küçük biriktirme yeri kullanımını korur."},"facet_ids":["F002"],"text":"küçük su biriktirme çukuru","usage_role":"contextual"}],"definition":"Geniş ağızlı, yayvan bir çanaktır. Aynı ad ailesindeki çoğul biçim ayrıca su tutmak için yapılan küçük biriktirme çukurlarını da belirtebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel nesne geniş ağızlı, basık ve yayvan bir çanaktır."},{"facet_id":"F002","role":"extension","statement":"Aynı ad ailesinin çoğul biçimi, su için yapılan küçük biriktirme çukurlarını da adlandırabilir."}],"identity_rationale":"Kaynak ifadesinin baskın gönderimi geniş ve yayvan bir çanaktır; aynı birleşik iddia ayrıca aynı ad ailesindeki çoğul biçimi küçük su biriktirme yerleri için de verir. Dal korunabilir, ancak ikinci gönderimin çanak tanımına özdeş değil, ona biçim ve işlev bakımından bağlı ayrı bir uzantı olduğu belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"geniş ve yayvan çanak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"geniş ve yayvan çanaklar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"su için yapılmış küçük biriktirme çukurları"}],"lexicalization_note":"Tanım yalın kap adını çekirdekte tutar ve kaynakta açıkça verilen küçük su biriktirme yeri kullanımını bağımlı bir uzantı olarak sınırlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kap biçimi, su tutma işlevi ve geniş yüzeyle karışabilecek sınırları gösteren dört komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kabın yayvan ve basık biçimini öne çıkarır ve su çukurlarına uzanır; komşu dal yemek sunma işlevini öne çıkarır ve küçük kuyu benzetmesine uzanır.","focus_only":"Odak dal yayvan çanağın yanında küçük su biriktirme çukurları uzantısını da kapsar.","gloss":"büyük yemek kabı","neighbor_only":"Komşu dal özellikle yemek konan büyük kabı ve ona benzetilen küçük kuyuyu kapsar.","neighbor_ref":"root_000250/B002","relation_type":"near_synonym","shared_zone":"Geniş bir yemek kabı iki dalın en yakın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dalda yayvan çanak biçimi kurucudur; komşu dalın kabı daha çok yıkama veya su tutma işleviyle belirlenen leğen ya da tekne türündedir.","focus_only":"Odak dal geniş, yayvan çanağı ve küçük su biriktirme çukurlarını adlandırır.","gloss":"leğen veya tekne","neighbor_only":"Komşu dal su veya çamaşır için kullanılan daha derin tekne ve leğen türlerini kapsar.","neighbor_ref":"root_000596/B003","relation_type":"near_synonym","shared_zone":"Su ya da başka bir içerik tutan geniş kap görünümü iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Odak dal biçimce yayvan çanakla sınırlı bir çekirdeğe sahiptir; komşu dal ise biçimden çok toplama işlevi çevresinde farklı kap ve yer türlerini birleştirir.","focus_only":"Odak dal belirli olarak yayvan çanağı ve küçük su biriktirme çukurunu kapsar.","gloss":"su veya yemek toplayan kap","neighbor_only":"Komşu dal bardak, havuz, kap, oluk ve oyulmuş toplama yeri gibi çok çeşitli su veya yemek toplayıcılarını kapsar.","neighbor_ref":"root_001222/B004","relation_type":"near_neighbor","shared_zone":"Bir sıvıyı ya da yemeği içinde toplama işlevi iki dalda kesişir."},{"boundary_match":"partial","distinction":"Odak dal somut bir kap veya su biriktirme yeridir; komşu dal ise genel yüzey genişliğini anlatır ve kap olma şartı taşımaz.","focus_only":"Odak dal genişliğin kendisini değil, geniş ve basık belirli bir kap türünü adlandırır.","gloss":"yayılmış geniş yüzey","neighbor_only":"Komşu dal bir şeydeki yayılma ve geniş yüzeyi, yeryüzü ve yüz derisi kullanımlarıyla birlikte anlatır.","neighbor_ref":"root_000845/B001","relation_type":"near_neighbor","shared_zone":"Yayvan kabın geniş ve açılmış yüzeyi, iki dal arasında biçimsel bir yakınlık kurar."}],"source_phrase_ar":"الصحفة القصعة المسلنطحة (maqayis); الصحاف مناقع صغار تتخذ للماء (maqayis); الصحفة شبه القصعة المسلنطحة العريضة (ayn); الصحفة القصعة وتجمع صحافا (jamhara); الصحفة كالقصعة والجمع صحاف (sihah); الصحفة مثل قصعة عريضة (mufradat)","source_summary":"Birleşik kaynak anlatımı geniş ve yayvan çanağı ortak çekirdek olarak verir; ayrıca aynı ad ailesinin küçük su biriktirme yerlerine yönelen ayrı kullanımını kaydeder.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"الصَّحفة القصعة العريضة المسلنطحة والصحاف مناقع صغار للماء","what_is_not_ar":"الصحيفة المكتوبة والمصحف وصحيفة الوجه والتصحيف"},"support_links":[]},{"boundary":"Dal yalnız genel yanılmayı değil, harf benzerliğinin doğurduğu yanlış okuma veya aktarımı ve buna bağlı kişi adlandırmasını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000845/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صُحُف","morph_features":"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"87:18:4:2","qac_word_ref":"87:18:4","surface_ar":"صُّحُفِ"}],"gloss":"harf benzerliğinden doğan yanlış okuma veya aktarım","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kurucu olay, benzer harflerin karıştırılması yüzünden yazılı metnin yanlış okunması veya yanlış aktarılmasıdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlı kişi kullanımı, yazılı metni benzer harfleri karıştırarak yanlış aktaran kimseyi belirtir."}}],"root_ar":"ص ح ف","root_id":"root_000845","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hatanın nedenini, okuma aşamasını ve yanlış aktarım sonucunu birlikte karşılayan genel açıklamadır.","boundary_detail":"Dal yalnız genel yanılmayı değil, harf benzerliğinin doğurduğu yanlış okuma veya aktarımı ve buna bağlı kişi adlandırmasını kapsar.","branch_image_ar":"تصحيف القراءة","concept_gloss":"harf benzerliğinden doğan yanlış okuma veya aktarım","contextual_glosses":[{"applicability":"Hatanın doğrudan okuma sırasında gerçekleştiği bağlamlarda doğal bir eylem karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yanlış okumanın başkasına aktarılması sonucunu ve kişi kullanımını karşılamaz.","preserves":"Benzer harflerin karıştırılmasıyla oluşan yanlış okuma olayını korur."},"facet_ids":["F001"],"text":"benzer harfleri karıştırarak yanlış okumak","usage_role":"general"},{"applicability":"Benzer harfleri karıştırdığı için okuduğu metni yanlış aktaran kişiden söz edilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":"Neden açıkça belirtilmezse başka tür aktarım yanlışlarını da çağrıştırabilir.","fit":"narrowing","loses":"Tek başına olay adı olarak yanlış okuma ve aktarım sürecini karşılamaz.","preserves":"Yanlış okumayı aktarımına taşıyan kişi kullanımını korur."},"facet_ids":["F002"],"text":"metni yanlış aktaran kişi","usage_role":"contextual"}],"definition":"Yazılı bir metni, birbirine benzeyen harfleri karıştırarak yanlış okumak veya aslından farklı aktarmaktır. Aynı dal, bu tür bir okuma hatasını aktarımında yapan kişiyi de niteleyebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kurucu olay, benzer harflerin karıştırılması yüzünden yazılı metnin yanlış okunması veya yanlış aktarılmasıdır."},{"facet_id":"F002","role":"associated_use","statement":"Bağlı kişi kullanımı, yazılı metni benzer harfleri karıştırarak yanlış aktaran kimseyi belirtir."}],"identity_rationale":"Kaynak ifadesinin ana çekirdeği, birbirine benzeyen harfler yüzünden yazılı metni yanlış okumak veya aslından farklı aktarmaktır. Sunulan çerçeve doğrudur; ancak kaynak ayrıca bu hatayı yapan aktarıcıyı belirten bağlı bir kişi kullanımını da içerdiğinden sınır buna göre genişletilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"benzer harfleri karıştırmaktan doğan yanlış okuma veya aktarım"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"benzer harfleri karıştırıp metni yanlış aktaran kişi"}],"lexicalization_note":"Tanım olay çekirdeğini, harf benzerliği koşulunu ve yanlışı aktaran kişiye özgü bağlı kullanımı ayrı tutar; genel belirsizlik anlamına genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ayırt edici işaretle karşıtlık ve genel benzerlik, belirsizleştirme ile karışıklık sınırlarını gösteren dört komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal ayırt edememenin doğurduğu hatalı sonucu, komşu dal ise harfleri işaretleyerek aynı belirsizliği ortadan kaldıran karşıt işlemi anlatır.","focus_only":"Odak dal, harf benzerliğinin giderilememesi yüzünden ortaya çıkan yanlış okuma veya aktarımı anlatır.","gloss":"harfleri ayırt edici işaretleme","neighbor_only":"Komşu dal, işaret veya noktalar ekleyerek harfler arasındaki belirsizliği giderme işlemini anlatır.","neighbor_ref":"root_000988/B002","relation_type":"polarity_pair","shared_zone":"İki dalın ortak ekseni, yazıdaki benzer harflerin ayırt edilmesi veya karıştırılmasıdır."},{"boundary_match":"partial","distinction":"Odak dal yazıdaki harflerin karışmasına ve metnin yanlış okunmasına bağlıdır; komşu dal ise yazı şartı olmadan daha genel kuşku ve benzerlik durumlarını kapsar.","focus_only":"Odak dal yazılı metinde benzer harflerden doğan belirli bir okuma ve aktarım hatasıdır.","gloss":"benzerlikten doğan kuşku","neighbor_only":"Komşu dal sanı, kuruntu, genel benzerlik, belirsizlik ve bir kişiden kuşkulanma alanlarını kapsar.","neighbor_ref":"root_000454/B005","relation_type":"near_neighbor","shared_zone":"Benzer görünen şeylerin birbirine karıştırılması iki dalda ortak bir bilişsel zemindir."},{"boundary_match":"partial","distinction":"Odak dal okuyucunun harf benzerliği yüzünden düştüğü hatadır; komşu dal ise nesne veya anlam üzerinde belirsizlik yaratan işlemi anlatır.","focus_only":"Odak dal benzer harfleri karıştıran okuyucunun yaptığı somut okuma veya aktarım hatasıdır.","gloss":"anlamı belirsizleştirme","neighbor_only":"Komşu dal bir şeyi ya da sözün anlamını başkası için bilerek veya fiilen kapalı ve karışık hale getirmeyi anlatır.","neighbor_ref":"root_001049/B004","relation_type":"near_neighbor","shared_zone":"Bir metnin anlaşılmasını zorlaştıran karışıklık iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal yazıya, harf benzerliğine ve okuma sonucuna özgüdür; komşu dal daha genel bir karıştırma ve belirsizleşme alanına sahiptir.","focus_only":"Odak dalın koşulu yazılı harflerin birbirine benzemesi, sonucu ise yanlış okuma veya aktarımdır.","gloss":"karıştırıp belirsizleştirme","neighbor_only":"Komşu dal herhangi bir işin, anlatımın veya karanlığın karışıp belirsizleşmesini genel olarak kapsar.","neighbor_ref":"root_001341/B003","relation_type":"near_neighbor","shared_zone":"Karışıklığın doğru ayrımı engellemesi her iki dalda da bulunur."}],"source_phrase_ar":"الصحفي الذي يروي الخطأ عن قراءة الصحف بأشباه الحروف (ayn); التصحيف الخطأ في الصحيفة (sihah); التصحيف قراءة المصحف وروايته على غير ما هو لاشتباه حروفه (mufradat)","source_summary":"Kaynakların birleşik anlatımı, benzer harflerin karıştırılmasıyla doğan yanlış okuma veya aktarımı temel alır ve bu yanlışı aktaran kişiyi belirten kullanımı da içerir.","sources":["AY","SI","MU"],"what_is_ar":"التصحيف والخطأ في قراءة الصحف أو المصحف لاشتباه الحروف","what_is_not_ar":"الصحيفة المكتوبة نفسها والمصحف نفسه والصحفة"},"support_links":[]},{"boundary":"Dal, zamansal sıralanma veya yönetim anlamını değil, yakınlık ve bitişiklik sınırını taşır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"aralıksız yakınlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Arada ayırıcı unsur olmadan yakın, bitişik veya yanında olma."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin başka bir şeye bitişik ya da hemen yakın olduğunu anlatan genel çekirdek için uygundur.","boundary_detail":"Dal, zamansal sıralanma veya yönetim anlamını değil, yakınlık ve bitişiklik sınırını taşır.","concept_gloss":"aralıksız yakınlık","contextual_glosses":[{"applicability":"Bir kişinin hemen yanında veya yakınında bulunan şeyi doğal Türkçe bağlamda karşılar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yanındalık ve yakın bulunma değerini korur."},"facet_ids":["F001"],"text":"yanında bulunan","usage_role":"contextual"},{"applicability":"Ev veya yer örneklerinde arada mesafe bırakmayan komşuluğu verir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bitişiklik ve yakın komşuluk sınırını korur."},"facet_ids":["F001"],"text":"bitişik komşu","usage_role":"contextual"}],"definition":"Bir şeyin başka bir şeye araya yabancı bir unsur girmeden yakın, bitişik veya yanında olmasıdır. Bu yakınlık yer bakımından olabileceği gibi ilişki bakımından da kurulabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Arada ayırıcı unsur olmadan yakın, bitişik veya yanında olma."}],"identity_rationale":"Kaynak ifadesi, dalın temelini arada yabancı bir unsur bulunmadan yakın olma, bitişik durma veya yanında bulunma olarak verir. Yer, ilişki ve bir evin başka bir eve bitişik olması gibi kullanımlar bu aynı yakınlık çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yakınlık ve bitişiklik"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sana yakın veya yanında olan şey"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir eve bitişik olan ev"}],"lexicalization_note":"Çıplak yakınlık değeri ile kalıp içindeki ev veya yanındalık kullanımları ayrılarak korunur.","neighbor_coverage_note":"Tüm aday komşular yakınlık, yanındalık veya aynı kökün diğer dalları bakımından değerlendirildi; yalnız sınırı gerçekten keskinleştirenler yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda yakınlık çoğu kez şeyin hemen yanında veya onu izleyen konumda bulunmasıyla sınırlanır; komşu dal daha genel yakınlaşma ve yaklaştırma eylemlerine de açıktır.","focus_only":"Arada yabancı bir unsur bulunmaması ve bitişik yanındalık daha belirgindir.","gloss":"yakınlık","neighbor_only":"Genel yaklaşma, yakınlaştırma ve iki şey arasında yakınlık kurma alanı daha geniştir.","neighbor_ref":"root_000493/B001","relation_type":"near_synonym","shared_zone":"İki dal da yakın olma ve mesafenin azlığı alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği bitişik yakınlıktır; B002 aynı kesintisizlik fikrini zamansal veya eylemsel sıra halinde gerçekleşen öğelere uygular.","focus_only":"Yakınlık yer veya ilişki bakımından yan yana durma olarak kurulur.","gloss":"yakınlık ile ardışıklık","neighbor_only":"Ardışıklıkta bir şeyin başka bir şeyden sonra gelmesi ve sıra düzeni öne çıkar.","neighbor_ref":"root_001684/B002","relation_type":"near_neighbor","shared_zone":"İkisinde de araya yabancı bir unsur girmemesi önemlidir."}],"source_summary":"Kaynakların ortak anlatımı, bu dalı yakınlık ve bitişiklik çekirdeği etrafında toplar; kişinin yanındaki şey ve birbirine komşu ev örnekleri bu çekirdeğin uygulamalarıdır."},"support_links":[]},{"boundary":"Dal, mekansal yakınlık veya dostça destek anlamına genişletilmeden ardışık gerçekleşme ile sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B002","candidate_links":[{"candidate_id":"cand_b2f3d9a718de8ab9aa34","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"kesintisiz ardışıklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Şeylerin veya eylemlerin kesintisiz biçimde peş peşe gerçekleşmesi."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Peş peşe gelen şeyler, eylemler veya dönemler için dalın bütün çekirdeğini verir.","boundary_detail":"Dal, mekansal yakınlık veya dostça destek anlamına genişletilmeden ardışık gerçekleşme ile sınırlıdır.","concept_gloss":"kesintisiz ardışıklık","contextual_glosses":[{"applicability":"Atış, iş veya haberlerin ardı ardına geldiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sıra ve kesintisiz takip anlamını korur."},"facet_ids":["F001"],"text":"peş peşe","usage_role":"contextual"},{"applicability":"İki iş veya iki nesne arasında ardışık düzen kuran eylem bağlamına uyar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemler arasında sıra kurma değerini korur."},"facet_ids":["F001"],"text":"art arda yapmak","usage_role":"contextual"}],"definition":"İki veya daha çok şeyin ya da eylemin araya ilgisiz bir kesinti girmeden peş peşe gerçekleşmesidir. Düzen, art arda geliş ve süreklilik çekirdeği birlikte korunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Şeylerin veya eylemlerin kesintisiz biçimde peş peşe gerçekleşmesi."}],"identity_rationale":"Kaynak ifadesi, iki veya daha çok şeyin araya başka bir şey girmeden biri diğerinin ardından gelmesini anlatır. Atış, iş, ay ve yazıların peş peşe gelişi örnekleri bu sıra ve kesintisizlik çekirdeğini doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kesintisiz sıra"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"araya kesinti girmeden peş peşe oluş"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"şeyleri veya işleri peş peşe getirme"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"iki şeyi peş peşe getirmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"peş peşe isabet eden üç ok"}],"lexicalization_note":"Çıplak sıralanma değeri ile iki şey arasında kurulan veya örneklerdeki kalıplı kullanım ayrı tutulur.","neighbor_coverage_note":"Adaylar ardışıklık, takip ve aynı kökün yakın dalları açısından denetlendi; örnek tekrarı yapan adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal, aynı kökün yakınlık fikrinden gelen aralıksız sıra değerini taşır; komşu dal daha genel takip ve düzenli akış alanını kapsar.","focus_only":"Araya aynı diziden olmayan bir unsur girmemesi özellikle vurgulanır.","gloss":"kesintisiz takip","neighbor_only":"Okuma, konuşma veya ayların akışı gibi süreklilik örnekleri daha geniştir.","neighbor_ref":"root_000695/B001","relation_type":"near_synonym","shared_zone":"İki dal da şeylerin biri diğerinin ardından gelmesine dayanır."},{"boundary_match":"field_only","distinction":"B002 nesne ya da eylemlerin sıra halinde gelişiyle ilgilidir; B004 kişiler veya topluluklar arasında destekleyici bağlılık kurar.","focus_only":"Peş peşe gerçekleşme ve düzen anlamı vardır.","gloss":"sıra ile destek","neighbor_only":"Dostça yakınlık, sevgi, destek ve karşıtlığa karşı taraf tutma anlamı vardır.","neighbor_ref":"root_001684/B004","relation_type":"same_field","shared_zone":"İkisi de yakınlık veya bağ kurma alanında aynı kökten ayrılır."}],"source_summary":"Kaynakların ortak anlatımı, dalı şeyin şeyden sonra gelmesi, işlerin düzenli biçimde sıralanması ve araya yabancı bir kesinti girmemesi etrafında birleştirir."},"support_links":["sup_6940b6d1eba667610fc7"]},{"boundary":"Dal, yalnız sevgi ve yardım anlamı değil, bir işin başına geçip onu yürütme anlamıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"bir işi üstlenip yönetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işi veya başkasının durumunu üstlenip yönetme ve yürütme."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yönetim, görev alma ve başkasının işini yürütme bağlamlarının hepsine uygulanabilir.","boundary_detail":"Dal, yalnız sevgi ve yardım anlamı değil, bir işin başına geçip onu yürütme anlamıdır.","concept_gloss":"bir işi üstlenip yönetme","contextual_glosses":[{"applicability":"Bir yer, iş veya görevin başına geçme bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başına geçme ve yürütme değerini korur."},"facet_ids":["F001"],"text":"yönetimini üstlenmek","usage_role":"contextual"},{"applicability":"Yetim, kadın veya başka bir kişinin işini gözetme bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sorumluluk ve gözetim değerini korur."},"facet_ids":["F001"],"text":"işlerine bakmak","usage_role":"contextual"}],"definition":"Bir işin, yerin veya başkasına ait durumun sorumluluğunu üstlenip onu yönetmek ve yürütmektir. Bu, resmi yönetimden bakım ve gözetim sorumluluğuna kadar uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işi veya başkasının durumunu üstlenip yönetme ve yürütme."}],"identity_rationale":"Kaynak ifadesi, bir işin, yerin veya kişinin işlerinin sorumluluğunu üstlenip yürütmeyi açıkça verir. Yönetim, yetki, görev üstlenme ve yetim ya da kadınla ilgili sorumluluk örnekleri aynı idare etme çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yönetim ve yetki alanı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir yeri veya işi yöneten kişi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"başkasının işlerinden sorumlu kişi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bir işi üstlenmek"}],"lexicalization_note":"Yönetim adı, görevli kişi ve işi üstlenme kalıbı aynı dalda ama kapsamları ayrılarak tutulur.","neighbor_coverage_note":"Yönetim, yetki, yardım ve aynı kökün ilişki dalları karşılaştırıldı; yalnız gerçek kapsam ayrımı veren komşular seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal görev üstlenme ve gözetimi birlikte içerir; komşu dal daha çok emir ve resmi yönetici konumunu öne çıkarır.","focus_only":"Gözetim ve başkasının işlerini yürütme gibi resmi olmayan sorumlulukları da kapsar.","gloss":"yönetim yetkisi","neighbor_only":"Buyruk sahibi yönetici ve resmen yönetici kılma alanı daha baskındır.","neighbor_ref":"root_000051/B003","relation_type":"near_synonym","shared_zone":"İki dal da yönetim ve işlerin başında bulunma alanında örtüşür."},{"boundary_match":"field_only","distinction":"B003 sorumluluk ve idare çekirdeğindedir; B004 birini sevmek, desteklemek veya onun yanında yer almakla sınırlıdır.","focus_only":"İşin başına geçme ve onu yürütme vardır.","gloss":"yönetim ile destek","neighbor_only":"Sevgi, dostluk ve yardım ederek taraf olma vardır.","neighbor_ref":"root_001684/B004","relation_type":"same_field","shared_zone":"İkisi de insanlar arası bağlılık ve yakın ilişki alanına dokunur."}],"source_summary":"Kaynakların ortak anlatımı, bu dalı yönetme, sorumluluk alma, bir yerin veya işin başına geçme ve korunmaya muhtaç kişinin işini yürütme alanında toplar."},"support_links":[]},{"boundary":"Dal, resmi yönetim veya özgür bırakmaya bağlı hukuki bağ anlamına indirgenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"yakın durup destek olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sevgi, dostluk, inanç veya yardım bağıyla birinin yanında yer alma."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sevgi, dostluk, inanç veya yardım bağıyla bir tarafı tutma bağlamlarında uygundur.","boundary_detail":"Dal, resmi yönetim veya özgür bırakmaya bağlı hukuki bağ anlamına indirgenmez.","concept_gloss":"yakın durup destek olma","contextual_glosses":[{"applicability":"Kişi veya topluluk için düşmanın karşıtı olan yakın destekçi bağlamına uyar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dostluk ve destek değerini korur."},"facet_ids":["F001"],"text":"dost ve destekçi","usage_role":"contextual"},{"applicability":"Birini sevme, kayırma veya yardım ederek destekleme eyleminde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taraf olma ve destekleme anlamını korur."},"facet_ids":["F001"],"text":"yanında yer almak","usage_role":"contextual"}],"definition":"Bir kişi veya topluluğa sevgi, dostluk, inanç ya da yardım bağıyla yakın durup onun yanında yer almaktır. Karşıtlık ekseninde düşmanın değil desteklenen tarafın yanında olma anlamı taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sevgi, dostluk, inanç veya yardım bağıyla birinin yanında yer alma."}],"identity_rationale":"Kaynak ifadesi, düşmanın karşıtı olan yakın tarafı, sevgi, destek, dostluk, inanç veya anlaşma bağıyla yanında olmayı birlikte verir. Bu dalda yakınlık, yönetim değil, taraf tutan ve yardım eden ilişki olarak işler.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"dost, seven veya destekleyen kişi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"destekçi, anlaşmalı dost veya yakın yoldaş"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"birini sevip destekleme veya kayırma"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birini sevmek, desteklemek veya kayırmak"}],"lexicalization_note":"Kişi adı, destek ilişkisi ve birini destekleme kalıbı karıştırılmadan aynı ilişki alanında açıklanır.","neighbor_coverage_note":"Sevgi, dostluk, destek ve akrabalık adayları karşılaştırıldı; yalnız okuyucunun karıştırabileceği sınırlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal sevgi bağını destek ve taraf olma ile birlikte kurar; komşu dal daha çok dostluğun içtenlik yönünü anlatır.","focus_only":"Sevgiyle birlikte yardım, taraf tutma ve düşmanın karşıtı olma vardır.","gloss":"dostluk ve destek","neighbor_only":"İçten dostluk ve sevgi bağı daha baskındır; yardım veya taraf tutma zorunlu değildir.","neighbor_ref":"root_000435/B003","relation_type":"near_neighbor","shared_zone":"İki dal da yakın dostluk ve sevgi ilişkisine dokunur."},{"boundary_match":"partial","distinction":"B004 yardım eden dost tarafı anlatır; B005 hukuki, soyla ilgili veya toplumsal statüden doğan özel bağı anlatır.","focus_only":"Destek, sevgi ve taraf olma ilişkisi öne çıkar.","gloss":"destek bağı ile statü bağı","neighbor_only":"Soy, özgür bırakma, komşuluk veya miras bağlantısı gibi statü bağı öne çıkar.","neighbor_ref":"root_001684/B005","relation_type":"near_neighbor","shared_zone":"İki dal da insanlar arasında yakın bağ ve karşılıklı yükümlülük alanına girer."}],"source_summary":"Kaynakların ortak anlatımı, dalı düşmana karşı yakın taraf olmak, sevmek, desteklemek, dost veya anlaşmalı yardımcı olmak ve inanç yahut arkadaşlık bakımından yakınlaşmak etrafında toplar."},"support_links":[]},{"boundary":"Dal, dostça destekten ayrılır; soy, özgür bırakma, komşuluk veya özel bağlılık ilişkisi ister.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"özel yakınlık ve bağlılık bağı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Soy, özgür bırakma, komşuluk veya hısımlıktan doğan özel bağlılık."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Soy, özgür bırakma, komşuluk veya hısımlıkla kurulan toplumsal ve hukuki bağlar için uygundur.","boundary_detail":"Dal, dostça destekten ayrılır; soy, özgür bırakma, komşuluk veya özel bağlılık ilişkisi ister.","concept_gloss":"özel yakınlık ve bağlılık bağı","contextual_glosses":[{"applicability":"Akrabalık ve özgür bırakmadan doğan özel ilişkiyi açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soy ve özgür bırakma kaynaklı bağı korur."},"facet_ids":["F001"],"text":"soy veya özgür bırakma bağı","usage_role":"explanatory"},{"applicability":"Soydan, anlaşmadan veya özel statüden bağlı kişiler topluluğu için doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlı kişiler ve yakınlık değerini korur."},"facet_ids":["F001"],"text":"yakın bağlılar","usage_role":"contextual"}],"definition":"Soy, özgür bırakma, komşuluk, hısımlık veya özel bağlılık sebebiyle kişileri birbirine bağlayan toplumsal ve hukuki yakınlık ilişkisidir. Bağ, miras, destek veya mensubiyet sonucunu doğurabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Soy, özgür bırakma, komşuluk veya hısımlıktan doğan özel bağlılık."}],"identity_rationale":"Kaynak ifadesi, özgür bırakan ve özgür bırakılan kişi, soy yakınları, destek veren anlaşmalı kişi, komşu, hısım ve bunlardan doğan özel bağları birlikte sayar. Bu dalda anlam genel yardım değil, belirli sosyal veya hukuki yakınlık statüsüdür.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"özgür bırakan, özgür bırakılan, soy yakını veya komşu gibi bağlı kişi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"özgür bırakma ilişkisine bağlı özel hak ve mensubiyet"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"soy yakınları veya özgür bırakma bağıyla bağlı kişiler"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"nimet veya özgür bırakma bağı kuran kişi"}],"lexicalization_note":"Çeşitli kişi adları ve özel bağ adı aynı statü alanında tutulur, genel destek anlamına yayılmaz.","neighbor_coverage_note":"Soy, hısımlık, özgür bırakma ve aynı kökün destek dalları denetlendi; genel destek adayları ayrı tutuldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal, belirli sözlük birimleriyle özgür bırakma ve statü adlarını da içerir; komşu dal daha genel soy ve bağlılık dokusunu anlatır.","focus_only":"Özgür bırakan ve özgür bırakılan kişi, komşu ve çeşitli bağlı kişi adları da sayılır.","gloss":"bağlılık bağı","neighbor_only":"Soy ve bağlılığın dokusu daha genel bir ilişki alanı olarak verilir.","neighbor_ref":"root_001348/B007","relation_type":"near_synonym","shared_zone":"İki dal da soy veya benzeri bağlılık ilişkisinin insanları birbirine bağlamasına dayanır."},{"boundary_match":"field_only","distinction":"B005 soy yakınlığını aşarak özgür bırakma ve komşuluk gibi statü bağlarını da içerir; komşu dal kan ve rahim yakınlığına odaklanır.","focus_only":"Özgür bırakma, komşuluk ve özel mensubiyet bağları da kapsamdadır.","gloss":"özel bağ ile akrabalık","neighbor_only":"Rahim ve kan bağına dayalı akrabalık çekirdeği öne çıkar.","neighbor_ref":"root_000552/B002","relation_type":"same_field","shared_zone":"İki dal da kişiler arasındaki yakın bağ alanındadır."}],"source_summary":"Kaynaklar bu dalı, soy yakınlığı, özgür bırakma ilişkisi, komşuluk, hısımlık, anlaşmalı bağlılık ve bunlara eşlik eden destek veya miras yükümlülüğü etrafında toplar."},"support_links":[]},{"boundary":"Dal, iş üstlenme veya yüz çevirme anlamına değil, bir şeye yönelme ve ona dönme anlamına bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"yüzünü veya dikkatini yöneltme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüz, duyu veya dikkati bir şeye doğru çevirip ona yönelme."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel yöneliş, dinleme veya dikkat verme bağlamlarını birlikte karşılar.","boundary_detail":"Dal, iş üstlenme veya yüz çevirme anlamına değil, bir şeye yönelme ve ona dönme anlamına bağlıdır.","concept_gloss":"yüzünü veya dikkatini yöneltme","contextual_glosses":[{"applicability":"Yüzün belirli bir yöne çevrildiği bağlamda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüzle yönelme değerini korur."},"facet_ids":["F001"],"text":"yüzünü çevirmek","usage_role":"contextual"},{"applicability":"İşitme, görme veya ilginin bir şeye yöneldiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duyu ve dikkat yönelişini korur."},"facet_ids":["F001"],"text":"dikkatini vermek","usage_role":"contextual"}],"definition":"Yüzü, gözü, kulağı veya dikkati bir şeye çevirip ona yönelmektir. Bazı kullanımlarda bu yönelme takip etme ya da razı olma tutumunu da taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüz, duyu veya dikkati bir şeye doğru çevirip ona yönelme."}],"identity_rationale":"Kaynak ifadesi, yüzü, kulağı veya gözü bir şeye yöneltmeyi ve ona dönük kabul, takip veya razı oluşu verir. Bu dal açıkça uzaklaşma değil, bedensel ya da dikkat yönünden yönelmedir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yüzünü bir şeye çevirmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yüzünü o yöne dönmüş veya ona uyan kişi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kulağını veya dikkatini bir şeye vermek"}],"lexicalization_note":"Yüz, işitme ve dikkat kalıpları yönelme çekirdeğinde tutulur; çıplak yönetim anlamı içeri alınmaz.","neighbor_coverage_note":"Yönelme, işitme, karşıya dönme ve yüz çevirme adayları değerlendirildi; ters kutup özellikle yayımlandı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"B006 yönelişi ve karşıya dönmeyi anlatır; B007 aynı eksenin tersinde, dönüp gitme veya ilgiyi kesme anlamını taşır.","focus_only":"Bir şeye doğru dönme, kabul veya dikkat verme vardır.","gloss":"yönelme ile yüz çevirme","neighbor_only":"Bir şeyden dönüp uzaklaşma, yüz çevirme veya dinlemeyi bırakma vardır.","neighbor_ref":"root_001684/B007","relation_type":"polarity_pair","shared_zone":"İki dal da yön değiştirme ve tutum alma ekseninde durur."},{"boundary_match":"partial","distinction":"Bu dal duyu ve dikkat yönelişini de içerir; komşu dal daha genel karşı karşıya oluş ve cephe yönünü anlatır.","focus_only":"Yüzün yanında işitme, göz ve razı oluş gibi tutum yönelişleri de kapsamdadır.","gloss":"yönelme","neighbor_only":"Karşı karşıya gelme ve genel cephe oluşturma alanı daha geniştir.","neighbor_ref":"root_001198/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeye yüzünü veya yönünü çevirme alanında örtüşür."}],"source_summary":"Kaynakların ortak anlatımı, dalı yüze, işitmeye veya göze yön verme, bir şeyi karşıya alıp ona dönme ve bu yönelişten doğan takip ya da razı oluş ile açıklar."},"support_links":[]},{"boundary":"Dal yalnız bedensel dönüp gitme değildir; bedensel uzaklaşma ile tutum olarak yüz çevirme birlikte bulunur.","branch_kind":"collocation","branch_ref":"root_001684/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"dönüp yüz çevirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dönüp uzaklaşma, yüz çevirme veya dinleme ve uyma bağını kesme."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel uzaklaşma ve tutum olarak ilgiyi kesme bağlamlarını birlikte karşılar.","boundary_detail":"Dal yalnız bedensel dönüp gitme değildir; bedensel uzaklaşma ile tutum olarak yüz çevirme birlikte bulunur.","concept_gloss":"dönüp yüz çevirme","contextual_glosses":[{"applicability":"Kaçış veya bedensel uzaklaşma bağlamlarında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dönüp gitme ve uzaklaşma değerini korur."},"facet_ids":["F001"],"text":"arkasını dönüp kaçmak","usage_role":"contextual"},{"applicability":"Birinden, bir işten veya buyruktan ilgiyi kesme bağlamına uyar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İlgiyi kesme ve reddedici uzaklaşmayı korur."},"facet_ids":["F001"],"text":"yüz çevirmek","usage_role":"contextual"}],"definition":"Bir şeyden bedenen dönüp uzaklaşmak veya ona kulak vermeyi ve uymayı bırakarak yüz çevirmektir. Kaçış, ayrılma ve ilgiyi kesme aynı sınır içinde kalır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dönüp uzaklaşma, yüz çevirme veya dinleme ve uyma bağını kesme."}],"identity_rationale":"Kaynak ifadesi, kişinin dönüp gitmesini, kaçarken arkasını dönmesini, birinden yüz çevirmesini ve dinleme ya da buyruğa uymayı bırakmasını verir. Bu nedenle dal, yönelmenin karşıtı olan uzaklaşma ve ilgiyi kesme anlamındadır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"arkasını dönüp kaçarak uzaklaşmak"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"birinden yüz çevirmek ve ilgiyi kesmek"}],"lexicalization_note":"Anlam kalıplı kullanımlara bağlıdır; çıplak köke yönetim veya destek anlamı yüklenmez.","neighbor_coverage_note":"Kaçış, reddetme, ilgiyi kesme ve aynı kökün yönelme dalı denetlendi; en keskin karşıtlıklar yayımlandı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"B007 uzaklaşma ve reddedici yön değişimini anlatır; B006 kabul edici veya dikkat veren yönelişi anlatır.","focus_only":"Bir şeyden dönüp uzaklaşma ve ilgiyi kesme vardır.","gloss":"yüz çevirme ile yönelme","neighbor_only":"Bir şeye doğru dönme, dikkat verme veya razı oluş vardır.","neighbor_ref":"root_001684/B006","relation_type":"polarity_pair","shared_zone":"İki dal da bedenin veya tutumun yön değiştirmesiyle ilgilidir."},{"boundary_match":"partial","distinction":"Bu dal bedensel uzaklaşmayı tutum olarak ilgiyi kesmeyle birleştirir; komşu dal arka taraf ve bozgun görüntüsünü daha açık taşır.","focus_only":"Dinlemeyi ve buyruğa uymayı bırakma gibi iç tutum boyutu da vardır.","gloss":"dönüp uzaklaşma","neighbor_only":"Savaşta arkayı dönme, bozgun ve arka yön vurgusu daha belirgindir.","neighbor_ref":"root_000458/B003","relation_type":"near_synonym","shared_zone":"İki dal da arkasını dönme, uzaklaşma ve yüz çevirme alanında örtüşür."}],"source_summary":"Kaynakların ortak anlatımı, dalı kaçışla dönüp gitme, birinden yüz çevirme ve dinleme ya da buyruğa uyma bağını kesme biçimlerinde açıklar."},"support_links":[]},{"boundary":"Dal, kötü sonuç tehdidi taşıyan kalıptan ayrılır; burada uygunluk ve haklı öncelik vardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"daha uygun ve hak sahibi olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeye daha uygun, daha layık veya daha hak sahibi olma."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işe, şeye veya konuma en layık olanı belirtme bağlamlarında uygundur.","boundary_detail":"Dal, kötü sonuç tehdidi taşıyan kalıptan ayrılır; burada uygunluk ve haklı öncelik vardır.","concept_gloss":"daha uygun ve hak sahibi olma","contextual_glosses":[{"applicability":"Kişinin bir iş veya konuma başkasından daha uygun olduğu bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Layık olma ve öncelik değerini korur."},"facet_ids":["F001"],"text":"daha layık","usage_role":"contextual"},{"applicability":"Bir şey üzerinde haklı öncelik veya sahiplik önceliği belirtilirken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Haklı öncelik ve uygunluk anlamını korur."},"facet_ids":["F001"],"text":"daha hak sahibi","usage_role":"contextual"}],"definition":"Bir kişinin veya tarafın bir şeye başkasından daha uygun, daha layık ya da daha hak sahibi olmasıdır. Anlam bir tehdit değil, uygunluk ve öncelik yargısıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeye daha uygun, daha layık veya daha hak sahibi olma."}],"identity_rationale":"Kaynak ifadesi, bir kişinin bir şeye daha uygun, daha layık veya daha hak sahibi olmasını anlatır. Dal, tehdit kalıbıyla değil, öncelik ve yerindelik karşılaştırmasıyla tanımlanır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bir şeye daha uygun, daha layık veya daha hak sahibi olmak"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"iki daha haklı veya daha uygun kişi"}],"lexicalization_note":"Karşılaştırmalı uygunluk kalıbı ile iki kişinin daha haklı olması biçimi aynı öncelik sınırında tutulur.","neighbor_coverage_note":"Hak, uygunluk, öncelik ve aynı yüzey kalıbı adayları denetlendi; tehdit anlamı ayrı dalda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bir şeye en layık veya daha hak sahibi olmayı karşılaştırmalı verir; komşu dal hakkın kendisini ve ona sahip olmayı daha özel anlatır.","focus_only":"Karşılaştırmalı olarak daha layık veya daha uygun olma vurgusu vardır.","gloss":"haklı öncelik","neighbor_only":"Belirli bir hakkın mülk veya talep olarak sabit olması daha baskındır.","neighbor_ref":"root_000347/B003","relation_type":"near_synonym","shared_zone":"İki dal da hak, uygunluk ve öncelik alanında örtüşür."},{"boundary_match":"partial","distinction":"B008 uygunluğu öncelik ve haklılık karşılaştırmasıyla kurar; komşu dal genel ehillik ve yaraşırlık alanında kalabilir.","focus_only":"Hak sahibi olma ve öncelik karşılaştırması açıkça bulunur.","gloss":"uygun olma","neighbor_only":"Bir kişi veya şeyin uygun, ehil ya da yaraşır olması daha genel verilir.","neighbor_ref":"root_000064/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir şeye yaraşma ve uygunluk alanında buluşur."}],"source_summary":"Kaynakların ortak anlatımı, dalı bir işe veya nesneye daha layık, daha uygun ve daha hak sahibi olma karşılaştırması olarak verir; iki kişinin en haklı olması da bu kapsamdadır."},"support_links":[]},{"boundary":"Dal yalnız belirli tehdit ve uyarı kalıbında geçerlidir; uygunluk karşılaştırması değildir.","branch_kind":"non_bare","branch_ref":"root_001684/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"yaklaşan kötü sonuç tehdidi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yaklaşan kötü sonuçla tehdit etme, uyarma veya kaçırılana hayıflandırma."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Muhataba kötü akıbetin yaklaştığını bildiren uyarı ve tehdit sözü için uygundur.","boundary_detail":"Dal yalnız belirli tehdit ve uyarı kalıbında geçerlidir; uygunluk karşılaştırması değildir.","concept_gloss":"yaklaşan kötü sonuç tehdidi","contextual_glosses":[{"applicability":"Kötü sonucun yaklaştığını sezdiren tehditli hitap bağlamlarında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tehdit ve yaklaşan kötü sonuç değerini korur."},"facet_ids":["F001"],"text":"yazık sana, başına gelecek var","usage_role":"contextual"},{"applicability":"Kaçırılan şey üzerine acı hatırlatma anlamı öne çıktığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayıflandırma ve uyarı değerini korur."},"facet_ids":["F001"],"text":"kaçırdığına hayıflanma","usage_role":"explanatory"}],"definition":"Muhataba kötü bir sonucun yaklaştığını bildiren tehdit ya da uyarı kalıbıdır. Bazı kullanımlarda kaçırılan şey için acı bir hatırlatma veya hayıflanma da taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yaklaşan kötü sonuçla tehdit etme, uyarma veya kaçırılana hayıflandırma."}],"identity_rationale":"Kaynak ifadesi, kalıbın tehdit, uyarı, yaklaşan kötü sonuç veya kaçırılan şey için acı hatırlatma değeri taşıdığını söyler. Bu nedenle dal, B008'deki uygunluk ve hak sahibi olma anlamından ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"tehdit ve uyarı sözü; sana kötü şey yaklaştı"}],"lexicalization_note":"Anlam belirli sözlü kalıba bağlıdır; çıplak öncelik veya yakınlık anlamı olarak genellenmez.","neighbor_coverage_note":"Tehdit, yıkım ve aynı kalıptan doğan uygunluk adayı denetlendi; söz kalıbı dışındaki zarar dalları ayrı tutuldu.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"B009 kalıplaşmış bir uyarı ve tehdit sözüdür; B008 uygunluk ve haklı öncelik yargısıdır.","focus_only":"Tehdit, kötü sonuç ve hayıflanma kalıbı vardır.","gloss":"tehdit ile öncelik","neighbor_only":"Bir şeye daha layık, daha uygun veya daha hak sahibi olma vardır.","neighbor_ref":"root_001684/B008","relation_type":"other","shared_zone":"Aynı yüzey kalıbı okuyucuda karışıklık yaratabilir."},{"boundary_match":"partial","distinction":"Bu dal zararın kendisini değil, muhataba yaklaşan zararı bildiren kalıbı anlatır; komşu dal yıkım veya yok oluşun kendisidir.","focus_only":"Kötü sonucun yaklaştığını söyleyen sözlü tehdit vardır.","gloss":"tehdit ve yıkım","neighbor_only":"Gerçek yıkım, yok etme veya bozma eylemi anlatılır.","neighbor_ref":"root_000174/B001","relation_type":"near_neighbor","shared_zone":"İki dal da kötü sonuç ve zarar alanına dokunur."}],"source_summary":"Kaynakların ortak anlatımı, dalı muhataba kötü ya da yıkıcı bir şeyin yaklaştığını sezdiren tehdit ve uyarı sözü olarak verir; ayrıca kaçırılan şey üzerine acı hatırlatma değeri bulunur."},"support_links":[]},{"boundary":"Dal genel yağmur adı değildir; önceki yağmuru izleyen özel yağmurla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"önceki yağmuru izleyen yağmur","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Önceki veya erken mevsim yağmurunu izleyen yağmur."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yağmurun özel ad olarak bir önceki yağmurdan sonra gelişini anlatan bağlamlarda uygundur.","boundary_detail":"Dal genel yağmur adı değildir; önceki yağmuru izleyen özel yağmurla sınırlıdır.","concept_gloss":"önceki yağmuru izleyen yağmur","contextual_glosses":[{"applicability":"Önceki mevsim yağmurunu izleyen yağmur bağlamında doğal ve kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İzleyen yağmur anlamını korur."},"facet_ids":["F001"],"text":"sonraki yağmur","usage_role":"contextual"},{"applicability":"Toprağın özel izleyen yağmurla ıslanması bağlamında açıklayıcıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Toprağın izleyen yağmuru alması değerini korur."},"facet_ids":["F001"],"text":"toprak bu yağmuru aldı","usage_role":"explanatory"}],"definition":"İlk mevsim yağmurundan ya da önceki yağmurdan sonra gelen yağmurdur. Toprağın bu yağmuru alması ve iyiliğin iyilik ardınca gelmesi gibi özel kullanımlar bu izleme fikrine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Önceki veya erken mevsim yağmurunu izleyen yağmur."}],"identity_rationale":"Kaynak ifadesi, bu dalı erken mevsim yağmurundan veya önceki yağmurdan sonra gelen yağmur adı olarak verir. Toprağın bu yağmuru alması ve dua kalıbındaki ardışık iyilik ifadesi de aynı izleme ilişkisine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"önceki yağmurdan sonra gelen yağmur"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"erken mevsim yağmurunu izleyen yağmur adı"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"toprağa izleyen yağmurun yağması"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"iyilik ardından gelen yağmur veya iyilik"}],"lexicalization_note":"Yağmur adı, toprağın bu yağmuru alması ve dua kalıbındaki özel kullanım ayrı ayrı korunur.","neighbor_coverage_note":"Yağmur adayları sıralanma, miktar ve toprakla ilişki bakımından değerlendirildi; genel yağmur adları yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal adlandırmayı önceki yağmurun ardından gelmeye bağlar; komşu dal toprağın tekrar yağmur alması veya erken mevsim zamanı yönünden daha geniştir.","focus_only":"Özellikle erken mevsim yağmurunu veya önceki yağmuru izleyen yağmur adı olarak verilir.","gloss":"izleyen yağmur","neighbor_only":"Daha önce ıslanmış toprağı tekrar yoklayan yağmur veya erken mevsim yağmuru alanı daha geniştir.","neighbor_ref":"root_001055/B007","relation_type":"near_synonym","shared_zone":"İki dal da önceki yağmurla ilişkili sonraki yağmur alanında örtüşür."},{"boundary_match":"field_only","distinction":"B010 yağmurun sırasını ve önceki yağmurla ilişkisini tanımlar; komşu dal yağmurun miktarı ve bolluğunu tanımlar.","focus_only":"Yağmurun önceki yağmuru izlemesi belirleyicidir.","gloss":"sonraki yağmur ile bol yağmur","neighbor_only":"Yağmurun çokluğu ve bereketli oluşu belirleyicidir.","neighbor_ref":"root_000274/B002","relation_type":"same_field","shared_zone":"İki dal da yağmur adlandırması alanındadır."}],"source_summary":"Kaynakların ortak anlatımı, dalı önceki yağmuru veya erken mevsim yağmurunu izleyen yağmur olarak açıklar; toprağın bu yağmuru alması da aynı adlandırmaya bağlanır."},"support_links":[]},{"boundary":"Dal çıplak somut addır; yönetim, yağmur veya başka aynı sesli kullanımlar buna taşınmaz.","branch_kind":"bare","branch_ref":"root_001684/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"deve sırtı alt örtüsü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Deve sırtında semer veya yük takımı altında kullanılan örtü ya da altlık."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Devenin sırtında semer veya yük takımı altında kullanılan örtü için uygundur.","boundary_detail":"Dal çıplak somut addır; yönetim, yağmur veya başka aynı sesli kullanımlar buna taşınmaz.","concept_gloss":"deve sırtı alt örtüsü","contextual_glosses":[{"applicability":"Deve veya yük hayvanı takımının altında kullanılan örtü bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alt örtü ve semerle ilişkiyi korur."},"facet_ids":["F001"],"text":"semer altı örtüsü","usage_role":"contextual"}],"definition":"Devenin sırtına, semer ya da yük takımı altına konan örtü, keçe veya benzeri altlıktır. Tekil ve çoğul biçimler aynı eşya sınıfına bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Deve sırtında semer veya yük takımı altında kullanılan örtü ya da altlık."}],"identity_rationale":"Kaynak ifadesi, dalı devenin sırtına konan, semer veya yük altındaki örtü ya da benzeri parça olarak verir. Bu somut eşya anlamı yönetim, yağmur veya yakınlık dallarından ayrı tutulur.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"deve sırtında semer altında kullanılan örtü"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"semer altı örtüleri"}],"lexicalization_note":"Çıplak eşya adı tanımlanır; kalıp dışı soyut anlamlar bu dala alınmaz.","neighbor_coverage_note":"Deve takımı, örtü, yastık ve taşıma araçları adayları denetlendi; nesnenin altlık işlevini ayıranlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal altlık olarak kullanılan örtüyü tanımlar; komşu dal deve sırtındaki daha genel binek veya örtü takımını kapsar.","focus_only":"Örtünün semer veya takım altında yer alması belirleyicidir.","gloss":"semer altı örtüsü","neighbor_only":"Deve sırtındaki daha genel örtü, küçük semer veya takım parçası alanı vardır.","neighbor_ref":"root_000766/B010","relation_type":"near_neighbor","shared_zone":"İki dal da deve sırtında kullanılan örtü veya takım parçası alanındadır."},{"boundary_match":"field_only","distinction":"B011 asıl takımın altında kalan örtüyü belirtir; komşu dal semer veya binek takımının kendisini anlatır.","focus_only":"Semerin altında kalan örtü veya altlık nesnedir.","gloss":"alt örtü ile semer","neighbor_only":"Devenin asıl binek takımı veya semeri anlatılır.","neighbor_ref":"root_000551/B002","relation_type":"same_field","shared_zone":"İki dal da deve üzerinde kullanılan binek takımı alanındadır."}],"source_summary":"Kaynakların ortak anlatımı, dalı devenin sırtında semer veya benzeri takım altında kullanılan örtü, keçe ya da altlık olarak verir; çoğul biçim aynı nesnenin çoğuludur."},"support_links":[]},{"boundary":"Dal, görev üstlenme değil, kalıplı olarak bir şeyi ele geçirme veya hedefe varmadır.","branch_kind":"collocation","branch_ref":"root_001684/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"ele geçirip hedefe ulaşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi ele geçirip ona üstün gelme veya yarış hedefine ulaşma."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyi kontrol altına alma veya yarışta son noktaya varma bağlamlarında uygundur.","boundary_detail":"Dal, görev üstlenme değil, kalıplı olarak bir şeyi ele geçirme veya hedefe varmadır.","concept_gloss":"ele geçirip hedefe ulaşma","contextual_glosses":[{"applicability":"Mal veya nesne üzerinde üstünlük kurma bağlamlarında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ele geçirme ve kontrol değerini korur."},"facet_ids":["F001"],"text":"eline geçirmek","usage_role":"contextual"},{"applicability":"Yarış veya mesafe sonuna ulaşma bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hedefe ulaşma değerini korur."},"facet_ids":["F001"],"text":"hedefe varmak","usage_role":"contextual"}],"definition":"Bir şeyin kişinin eline geçmesi, onun üzerinde üstünlük kurması veya yarışta hedefe varıp onu elde etmesidir. Sahip olma, galip gelme ve hedefe ulaşma sonuçları birlikte korunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi ele geçirip ona üstün gelme veya yarış hedefine ulaşma."}],"identity_rationale":"Kaynak ifadesi, bir şeyin kişinin eline geçmesini veya onun üzerinde üstün gelmesini ve yarış bağlamında son noktaya varıp onu geçerek elde etmesini verir. Dalda ele geçirme ile hedefe varma aynı üstün gelme sonucuna bağlanır.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"bir şeyi ele geçirmek veya ona üstün gelmek"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"hedefe varmak veya ona önce ulaşmak"}],"lexicalization_note":"Anlam belirli kalıplara bağlıdır; çıplak yönetim veya yakınlık anlamına genellenmez.","neighbor_coverage_note":"Ele geçirme, üstünlük, hedefe varma ve yönetim adayları denetlendi; görev üstlenme dalları ayrı tutuldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B012 ele geçirmeyi hedefe varma kullanımıyla birlikte verir; komşu dal daha genel üstünlük, kuşatma ve toplama alanını kapsar.","focus_only":"Yarış hedefine varma ve hedefi önde alma kullanımı da vardır.","gloss":"ele geçirme","neighbor_only":"Toplama, kuşatma ve geniş anlamda kontrol altına alma alanı daha geniştir.","neighbor_ref":"root_000368/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir şey üzerinde üstünlük ve kontrol kurma alanında örtüşür."},{"boundary_match":"field_only","distinction":"B012 sonuç olarak elde etme veya hedefe ulaşmayı ister; komşu dal üstünlük ve galiplik alanında daha geniştir.","focus_only":"Bir şeyin elde edilmesi veya hedefe varılması belirleyicidir.","gloss":"ele geçirme ile üstünlük","neighbor_only":"Üstünlük, yükseklik veya galiplik niteliği daha genel anlatılır.","neighbor_ref":"root_000104/B008","relation_type":"same_field","shared_zone":"İki dal da galip gelme ve üstün konuma geçme alanına dokunur."}],"source_summary":"Kaynakların ortak anlatımı, dalı bir şeyin ele geçmesi, mal üzerinde üstünlük kurulması ve yarış ya da mesafe bağlamında hedefe varılıp orada üstün gelinmesi olarak açıklar."},"support_links":[]},{"boundary":"Dal kalıplı verme ve yöneltme anlamındadır; yönetim veya öncelik anlamına genellenmez.","branch_kind":"collocation","branch_ref":"root_001684/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"birine iyi ya da kötü şey yöneltme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birine iyi veya kötü bir şeyi yöneltip ulaştırma ya da payına kılma."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye yarar, iyilik, zarar veya başka bir şeyi ulaştırma bağlamlarında uygundur.","boundary_detail":"Dal kalıplı verme ve yöneltme anlamındadır; yönetim veya öncelik anlamına genellenmez.","concept_gloss":"birine iyi ya da kötü şey yöneltme","contextual_glosses":[{"applicability":"Birine iyilik ulaştırma bağlamında doğal Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İyiliği kişiye ulaştırma değerini korur."},"facet_ids":["F001"],"text":"iyilikte bulunmak","usage_role":"contextual"},{"applicability":"Birine kötü bir şey yöneltme bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kötü şeyi kişiye yöneltme değerini korur."},"facet_ids":["F001"],"text":"zarar yöneltmek","usage_role":"contextual"}],"definition":"Bir şeyi, iyiliği, yararı veya kötülüğü bir kişiye yöneltip ona ulaştırmak ya da onun payına kılmaktır. Verilen şeyin iyi veya kötü olması dalın kapsamını değiştirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birine iyi veya kötü bir şeyi yöneltip ulaştırma ya da payına kılma."}],"identity_rationale":"Kaynak ifadesi, birine bir şey, iyilik, kötülük veya yarar yöneltmeyi ve onu o kişiye ulaştırmayı verir. Dal, görevi üstlenmek veya daha haklı olmak değil, bir şeyi birine tahsis edip ulaştırmaktır.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"birine iyilik yapmak veya bir şeyi ona ulaştırmak"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"birine iyilik veya kötülük yöneltmek"}],"lexicalization_note":"Anlam birine bir şey, iyilik veya kötülük yöneltme kalıbına bağlı tutulur.","neighbor_coverage_note":"Verme, ulaştırma, kazandırma ve satış adayları değerlendirildi; yalnız yöneltme çekirdeğini aydınlatanlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B013 verilen şeyin kişiye yöneltilmesini ve iyilik ya da kötülük olabilmesini vurgular; komşu dal genel verme ve getirme anlamındadır.","focus_only":"İyi ya da kötü bir şeyin belirli kişiye yöneltilmesi vurgulanır.","gloss":"birine verme","neighbor_only":"Genel verme, getirme veya bir şeyi birine sunma alanı daha geniştir.","neighbor_ref":"root_000009/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi bir kişiye ulaştırma alanında örtüşür."},{"boundary_match":"partial","distinction":"B013 iyi ve kötü yöneltmeyi birlikte kapsar; komşu dal başkasına yarar veya mal kazandırmaya odaklanır.","focus_only":"Kötülük veya zarar yöneltme de kapsam içindedir.","gloss":"yarar ulaştırma","neighbor_only":"Başkasına mal veya yarar kazandırma daha özel ve olumlu yöndedir.","neighbor_ref":"root_001296/B002","relation_type":"near_neighbor","shared_zone":"İki dal da kişiye bir yarar veya şey kazandırma alanına yaklaşır."}],"source_summary":"Kaynakların ortak anlatımı, dalı bir kişiye iyilik, yarar, kötülük veya herhangi bir şeyi ulaştırma ve onun üzerine yöneltme olarak açıklar."},"support_links":[]},{"boundary":"Dal yalnız satıştaki özel devir işlemidir; genel alım satım veya bağış anlamına genişletilmez.","branch_kind":"non_bare","branch_ref":"root_001684/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"aldığı fiyatla devretme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Satın alınan malı bilinen aynı fiyatla başka birine devretme."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Alım satımda malın satın alındığı bilinen fiyat üzerinden devredildiği özel işlem için uygundur.","boundary_detail":"Dal yalnız satıştaki özel devir işlemidir; genel alım satım veya bağış anlamına genişletilmez.","concept_gloss":"aldığı fiyatla devretme","contextual_glosses":[{"applicability":"Ticari işlem bağlamında malın alındığı fiyatla başkasına geçirilmesini doğal biçimde verir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aynı fiyatla devir şartını korur."},"facet_ids":["F001"],"text":"maliyet fiyatına devretmek","usage_role":"contextual"}],"definition":"Bir malı bilinen bir fiyatla satın aldıktan sonra aynı fiyatla başka birine devretme işlemidir. Anlam, satış içindeki özel fiyat ve devir şartına bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Satın alınan malı bilinen aynı fiyatla başka birine devretme."}],"identity_rationale":"Kaynak ifadesi, bir malı bilinen bir fiyatla satın aldıktan sonra aynı fiyatla başka birine devretme işlemini açıkça verir. Bu tekil ticaret terimi, yönetim veya genel verme anlamlarından ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"satın alınan malı bilinen aynı fiyatla başkasına devretme"}],"lexicalization_note":"Anlam satış alanındaki belirli terime bağlıdır; çıplak kök anlamına taşınmaz.","neighbor_coverage_note":"Satış, fiyat, devir ve genel verme adayları denetlendi; yalnız ticari işlem sınırını gösterenler yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"B014 genel satış değil, alınmış malı alış fiyatıyla devretme terimidir; komşu dal satış ve satın alma işlemini genel olarak anlatır.","focus_only":"Malın önce alınması ve aynı bilinen fiyatla devredilmesi şarttır.","gloss":"özel devir ile alım satım","neighbor_only":"Alım ve satımın genel karşılıklı işlem alanı vardır.","neighbor_ref":"root_000169/B001","relation_type":"same_field","shared_zone":"İki dal da ticari alım satım alanındadır."},{"boundary_match":"field_only","distinction":"B014 fiyatı şart olarak kullanan bir işlem adıdır; komşu dal bedel veya fiyat kavramının kendisini verir.","focus_only":"Aynı fiyatla başka kişiye devir işlemi anlatılır.","gloss":"devir işlemi ile fiyat","neighbor_only":"Fiyatın, bedelin veya değerin kendisi anlatılır.","neighbor_ref":"root_000206/B001","relation_type":"same_field","shared_zone":"İki dal da satışta bedel ve fiyat alanına dokunur."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanık, bu kullanımı bilinen fiyatla alınan malın aynı fiyatla başka kişiye devri olarak verir."}],"source_summary":"Bu dal, satış alanında belirli bir işlem adı olarak sunulur; malın önce bilinen fiyatla alınması ve sonra aynı fiyatla başka kişiye devredilmesi şartı belirleyicidir."},"support_links":[]},{"boundary":"Dal hayvan sürüsündeki ayırma ve sütten kesme uygulamasına bağlıdır; genel ardışıklık değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"küçük sürü hayvanlarını ayırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Küçük sürü hayvanlarını büyüklerinden veya yavruları analarından ayırma."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Küçük hayvanları büyüklerinden veya yavruları analarından ayırma bağlamlarında uygundur.","boundary_detail":"Dal hayvan sürüsündeki ayırma ve sütten kesme uygulamasına bağlıdır; genel ardışıklık değildir.","concept_gloss":"küçük sürü hayvanlarını ayırma","contextual_glosses":[{"applicability":"Yavru develerin analarından kesilmesi ve alıştırılması bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Anadan ayırma ve alıştırma değerini korur."},"facet_ids":["F001"],"text":"yavruları anadan ayırmak","usage_role":"contextual"},{"applicability":"Sürü içindeki küçük hayvanların büyüklerden ayrıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sürü içinde ayırma değerini korur."},"facet_ids":["F001"],"text":"küçükleri büyüklerden ayırmak","usage_role":"contextual"}],"definition":"Küçük sürü hayvanlarını büyüklerinden veya yavruları analarından ayırarak bağımsızlaşmaya ve yola gelmeye alıştırmaktır. Anlam, hayvancılıktaki ayırma ve sütten kesme uygulamasına bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Küçük sürü hayvanlarını büyüklerinden veya yavruları analarından ayırma."}],"identity_rationale":"Kaynak ifadesi, küçük sürü hayvanlarını büyüklerinden ayırmayı ve yavru develeri analarından keserek alıştırmayı verir. Bu dal, peş peşe geliş veya dostça destek anlamından farklı, hayvancılıkta ayırma ve alıştırma işlemidir.","lexical_glosses":[{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"küçük sürü hayvanlarını büyüklerinden ayırmak"},{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"yavru develeri analarından ayırıp alıştırma"}],"lexicalization_note":"Kalıplı sürü ayırma ve yavruyu anadan kesme kullanımları birlikte ama hayvancılık alanıyla sınırlı tutulur.","neighbor_coverage_note":"Küçük hayvan adları, buzağı ve deve yavrusu adayları ile aynı kökün ardışıklık dalı denetlendi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"B015 hayvancılık uygulaması olarak ayırmayı anlatır; komşu dal küçük hayvanların kendisini adlandırır.","focus_only":"Küçüklerin büyüklerden ayrılması veya yavruların anadan kesilmesi eylemi vardır.","gloss":"ayırma ile küçük hayvan adı","neighbor_only":"Küçük hayvanların adlandırılması ve sınıflanması öne çıkar.","neighbor_ref":"root_000160/B004","relation_type":"same_field","shared_zone":"İki dal da küçük sürü hayvanları alanındadır."},{"boundary_match":"field_only","distinction":"B015 sürüde ayırma işlemidir; B002 herhangi bir hayvancılık işlemi gerektirmeyen ardışık sıra anlamıdır.","focus_only":"Hayvanları ayırma ve alıştırma uygulamasıdır.","gloss":"ayırma ile ardışıklık","neighbor_only":"Şeylerin peş peşe gelişi ve kesintisiz sıra anlamıdır.","neighbor_ref":"root_001684/B002","relation_type":"other","shared_zone":"Aynı kökteki benzer yüzey biçimi karışıklık yaratabilir."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanık, kullanımı küçük hayvanları büyüklerden ve yavruları analarından ayırma uygulaması olarak verir."}],"source_summary":"Bu dal, sürü hayvanlarında küçükleri büyüklerden ayırma ve yavru develeri analarından kesip alışmalarını sağlama biçimindeki özel uygulamayı özetler."},"support_links":[]},{"boundary":"Dal bitki ve meyve olgunlaşma evresine bağlıdır; insana ait uzaklaşma anlamı buraya taşınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","surface_ar":"أُولَىٰ"}],"gloss":"taze hurmanın kurumaya dönmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taze hurmanın solup açık renge dönerek kurumaya başlaması."}}],"root_ar":"ء و ل","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Taze hurmanın solgunlaşıp kurumaya yöneldiği olgunluk sonrası evre için uygundur.","boundary_detail":"Dal bitki ve meyve olgunlaşma evresine bağlıdır; insana ait uzaklaşma anlamı buraya taşınmaz.","concept_gloss":"taze hurmanın kurumaya dönmesi","contextual_glosses":[{"applicability":"Taze hurmanın açık renkli kuruma evresine girmesi bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Solma ve kurumaya başlama değerini korur."},"facet_ids":["F001"],"text":"solup kurumaya başlamak","usage_role":"contextual"},{"applicability":"Evrenin rengini veya solgunluğunu açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Renk değişimi ve solgunluk değerini korur."},"facet_ids":["F001"],"text":"solgun kuruma rengi","usage_role":"explanatory"}],"definition":"Taze hurmanın olgunluk sonrası solup açık renge dönerek kurumaya yönelen evreye girmesidir. Bu evrenin belirgin rengi veya solgunluğu da adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taze hurmanın solup açık renge dönerek kurumaya başlaması."}],"identity_rationale":"Kaynak ifadesi, taze hurmanın solma, sararma veya kurumaya dönme evresine girmesini ve bu evrenin açık rengini verir. Dal, yüz çevirme değil, meyvenin olgunluk sonrası değişim aşamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"taze hurmanın solup kurumaya başlaması"},{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"taze hurmadaki solgun kuruma rengi"}],"lexicalization_note":"Meyvenin evreye girmesi ve bu evrenin adı birlikte korunur; soyut yüz çevirme anlamına yayılmaz.","neighbor_coverage_note":"Hurma, meyve olgunlaşması, sararma ve kuruma adayları değerlendirildi; uzaklaşma anlamlı dallar ayrı tutuldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B016 taze hurmanın özel geçiş evresini anlatır; komşu dal bitki ve sapların daha genel sararıp kuruma durumunu verir.","focus_only":"Taze hurmanın belirli solgun kuruma evresine bağlıdır.","gloss":"sararıp kurumaya dönme","neighbor_only":"Bitkinin veya sapın sararıp kuruması daha genel bir bitki evresidir.","neighbor_ref":"root_001033/B015","relation_type":"near_synonym","shared_zone":"İki dal da bitkisel ürünün sararma veya kuruma evresine girmesi alanında örtüşür."},{"boundary_match":"partial","distinction":"B016 geçiş evresidir; komşu dal kurumuş olma durumunu daha doğrudan anlatır.","focus_only":"Kurumaya başlama ve solgun renk evresi vurgulanır.","gloss":"kurumaya başlama ile kurumuşluk","neighbor_only":"Hurmanın kurumuş olması veya kuruluk durumu öne çıkar.","neighbor_ref":"root_000242/B005","relation_type":"near_neighbor","shared_zone":"İki dal da hurma veya meyve kuruması alanına yaklaşır."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanık, kullanımı taze hurmanın kurumaya dönerken aldığı solgun ve açık renkli evre olarak verir."}],"source_summary":"Bu dal, taze hurmanın solma ve açık renge dönme yoluyla kurumaya başladığı evreyi ve bu evrenin rengini özetler."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["87:18:1"],"branch_refs":[],"candidate_id":"cand_bc0879a2adc00e09a207","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:1:attestation-turn-at-surah-close","source_type":"word_analysis","support_ids":["sup_0e3a0b3223bae8229d1f","sup_fdf7c832367a3b348a04"],"title":"valuation turns into attestation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:1","qac_refs":["87:18:1:1"],"status":"accepted"}},{"anchor_refs":["87:18:1"],"branch_refs":[],"candidate_id":"cand_2dd7cdd5f37948755a79","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:1:compact-certification-sound","source_type":"word_analysis","support_ids":["sup_4e87fbd2ca27535aa2ec","sup_fdf7c832367a3b348a04"],"title":"compact audible opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:1","qac_refs":["87:18:1:1"],"status":"accepted"}},{"anchor_refs":["87:18:1"],"branch_refs":[],"candidate_id":"cand_f510d7d45d7acaacb4e8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:1:double-assertion-with-predicate-lam","source_type":"word_analysis","support_ids":["sup_0478b960eb41e8364cb1","sup_fdf7c832367a3b348a04"],"title":"opening assertion renewed at the predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:1","qac_refs":["87:18:1:1"],"status":"accepted"}},{"anchor_refs":["87:18:1"],"branch_refs":[],"candidate_id":"cand_e4e2d2ce357940f134e9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:1:opening-certification","source_type":"word_analysis","support_ids":["sup_0547044f4c9919bf853e","sup_fdf7c832367a3b348a04"],"title":"certifying particle opens the claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:1","qac_refs":["87:18:1:1"],"status":"accepted"}},{"anchor_refs":["87:18:2"],"branch_refs":[],"candidate_id":"cand_c1ab3bb1afe94064a7e9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:2:demonstrative-subject-under-inna","source_type":"word_analysis","support_ids":["sup_45433f6ce48ac3bcad44","sup_ef249701c63b45d7b368"],"title":"deictic subject under assertion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:2","qac_refs":["87:18:2:1"],"status":"accepted"}},{"anchor_refs":["87:18:2"],"branch_refs":[],"candidate_id":"cand_516657a1d8bf79130c84","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:2:discourse-content-compression","source_type":"word_analysis","support_ids":["sup_679aded12ce04fa57b29","sup_ef249701c63b45d7b368"],"title":"near demonstrative gathers prior teaching","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:2","qac_refs":["87:18:2:1"],"status":"accepted"}},{"anchor_refs":["87:18:2"],"branch_refs":[],"candidate_id":"cand_1f793af319e3f7362ebe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:2:immediacy-against-prior-records","source_type":"word_analysis","support_ids":["sup_bd0e4b45619a287c484e","sup_ef249701c63b45d7b368"],"title":"present pointing meets former records","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:2","qac_refs":["87:18:2:1"],"status":"accepted"}},{"anchor_refs":["87:18:2"],"branch_refs":[],"candidate_id":"cand_2c477002033aee1113a7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:2:scope-of-archive-claim","source_type":"word_analysis","support_ids":["sup_948a2723e972f74e2e4a","sup_ef249701c63b45d7b368"],"title":"pointer sets what is attested","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:2","qac_refs":["87:18:2:1"],"status":"accepted"}},{"anchor_refs":["87:18:2"],"branch_refs":[],"candidate_id":"cand_2c023deb2fd44c2e0078","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:2:stable-deictic-surface","source_type":"word_analysis","support_ids":["sup_d82d7402de667c00efcb","sup_ef249701c63b45d7b368"],"title":"long-vowel pointing surface","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:2","qac_refs":["87:18:2:1"],"status":"accepted"}},{"anchor_refs":["87:18:3"],"branch_refs":[],"candidate_id":"cand_821d36746d0881907852","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:3:compact-particle-pulse","source_type":"word_analysis","support_ids":["sup_41a1a927c12b7c424180","sup_9edcf31695a0eb8502d4"],"title":"brief pulse before the archive noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:3","qac_refs":["87:18:3:1"],"status":"accepted"}},{"anchor_refs":["87:18:3"],"branch_refs":[],"candidate_id":"cand_f747f504fa834cdc5e95","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:3:double-assertion-center","source_type":"word_analysis","support_ids":["sup_41a1a927c12b7c424180","sup_d82984ac6137f636f35b"],"title":"short clause with doubled certainty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:3","qac_refs":["87:18:3:1"],"status":"accepted"}},{"anchor_refs":["87:18:3"],"branch_refs":[],"candidate_id":"cand_a98aea1eb0a7dc8777dc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:3:predicate-side-emphasis","source_type":"word_analysis","support_ids":["sup_41a1a927c12b7c424180","sup_4228afde56ba9a938900"],"title":"emphasis lands on the predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:3","qac_refs":["87:18:3:1"],"status":"accepted"}},{"anchor_refs":["87:18:4"],"branch_refs":[],"candidate_id":"cand_6f43cb7a9e414919b7b2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:4:emphasis-location-surface-bundle","source_type":"word_analysis","support_ids":["sup_822f1ebfef6f4e8fa94f","sup_e0c048df5d891f868b0f"],"title":"emphasis fused to location in delivery","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:4","qac_refs":["87:18:3:2"],"status":"accepted"}},{"anchor_refs":["87:18:4"],"branch_refs":[],"candidate_id":"cand_0bc0bd7b3785da9a5147","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:4:pp-predicate-location","source_type":"word_analysis","support_ids":["sup_822f1ebfef6f4e8fa94f","sup_ebcaa199599b6ea30443"],"title":"preposition carries the predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:4","qac_refs":["87:18:3:2"],"status":"accepted"}},{"anchor_refs":["87:18:4"],"branch_refs":[],"candidate_id":"cand_308e6652ffb79c59f13b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:4:predicate-type-boundary-shift","source_type":"word_analysis","support_ids":["sup_822f1ebfef6f4e8fa94f","sup_ca5bb0509f01e5ddbfe7"],"title":"from qualities to archive location","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:4","qac_refs":["87:18:3:2"],"status":"accepted"}},{"anchor_refs":["87:18:4"],"branch_refs":[],"candidate_id":"cand_5ba6476763bbc04becda","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:4:textual-containment-not-source","source_type":"word_analysis","support_ids":["sup_3ed2aa8826b00ba18233","sup_822f1ebfef6f4e8fa94f"],"title":"records as container, not source-from","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:4","qac_refs":["87:18:3:2"],"status":"accepted"}},{"anchor_refs":["87:18:5"],"branch_refs":[],"candidate_id":"cand_eaa0c340dcd7e5440ec9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:18:5:boundary-to-archival-durability","source_type":"word_analysis","support_ids":["sup_3a8f3091d73b0aab7abd","sup_b361dc223c53cedfe926"],"title":"from value scene to preserved witness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:5","qac_refs":["87:18:4:1","87:18:4:2"],"status":"accepted"}},{"anchor_refs":["87:18:5"],"branch_refs":[],"candidate_id":"cand_8d4acabb5ec73af5f6db","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:18:5:definite-governed-archive","source_type":"word_analysis","support_ids":["sup_259a43526569b3b62428","sup_3a8f3091d73b0aab7abd"],"title":"known records governed by the preposition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:5","qac_refs":["87:18:4:1","87:18:4:2"],"status":"accepted"}},{"anchor_refs":["87:18:5"],"branch_refs":[],"candidate_id":"cand_202ef1279040f9670fd9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:18:5:next-ayah-specification","source_type":"word_analysis","support_ids":["sup_3a8f3091d73b0aab7abd","sup_f0e57f7494e1fadd4037"],"title":"general archive becomes named records","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:5","qac_refs":["87:18:4:1","87:18:4:2"],"status":"accepted"}},{"anchor_refs":["87:18:5"],"branch_refs":[],"candidate_id":"cand_e85f0e736bff548b67d0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:18:5:phrase-internal-qualification","source_type":"word_analysis","support_ids":["sup_3a8f3091d73b0aab7abd","sup_fd0421da8851a641c466"],"title":"archive waits for its qualifier","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:5","qac_refs":["87:18:4:1","87:18:4:2"],"status":"accepted"}},{"anchor_refs":["87:18:5"],"branch_refs":[],"candidate_id":"cand_f66a6b0e84712e6e740a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:18:5:plural-record-set","source_type":"word_analysis","support_ids":["sup_3a8f3091d73b0aab7abd","sup_b5c58564eae262bc7a86"],"title":"plural witness across records","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:5","qac_refs":["87:18:4:1","87:18:4:2"],"status":"accepted"}},{"anchor_refs":["87:18:5"],"branch_refs":[],"candidate_id":"cand_9c96c36d0380c31c8a29","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:18:5:recitational-variant-and-weight","source_type":"word_analysis","support_ids":["sup_3a8f3091d73b0aab7abd","sup_805b21397212758bf19c"],"title":"cadence shifts without sense shift","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:5","qac_refs":["87:18:4:1","87:18:4:2"],"status":"accepted"}},{"anchor_refs":["87:18:5"],"branch_refs":[],"candidate_id":"cand_02ccfd569b6c04d486dc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:18:5:wider-archive-continuity","source_type":"word_analysis","support_ids":["sup_3a8f3091d73b0aab7abd","sup_bae75017ca8274c77d17"],"title":"scriptural archive continuity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:5","qac_refs":["87:18:4:1","87:18:4:2"],"status":"accepted"}},{"anchor_refs":["87:18:5"],"branch_refs":[],"candidate_id":"cand_eaa642fba91e1eea7b31","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:18:5:written-surface-media","source_type":"word_analysis","support_ids":["sup_3a8f3091d73b0aab7abd","sup_6b7f9e91f147cc554eff"],"title":"material written-surface attestation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:5","qac_refs":["87:18:4:1","87:18:4:2"],"status":"accepted"}},{"anchor_refs":["87:18:6"],"branch_refs":[],"candidate_id":"cand_a7e250c5fd648b4a487c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:6:adjective-inside-pp","source_type":"word_analysis","support_ids":["sup_9f35c685c3bae56c5855","sup_c9863cca499e0ade7fdc"],"title":"final adjective qualifies the archive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:6","qac_refs":["87:18:5:1","87:18:5:2"],"status":"accepted"}},{"anchor_refs":["87:18:6"],"branch_refs":[],"candidate_id":"cand_ee0cd79a346ff458e37f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:6:archive-formula-and-lineage","source_type":"word_analysis","support_ids":["sup_c9863cca499e0ade7fdc","sup_dbb1293421dea543b1b8"],"title":"former records as lineage formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:6","qac_refs":["87:18:5:1","87:18:5:2"],"status":"accepted"}},{"anchor_refs":["87:18:6"],"branch_refs":[],"candidate_id":"cand_d60e69b664ef22e26f39","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:6:delayed-qualifier-resolution","source_type":"word_analysis","support_ids":["sup_a4be34a20e5a0cbc63c6","sup_c9863cca499e0ade7fdc"],"title":"final word resolves the archive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:6","qac_refs":["87:18:5:1","87:18:5:2"],"status":"accepted"}},{"anchor_refs":["87:18:6"],"branch_refs":[],"candidate_id":"cand_fdc3f47b59a286693467","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:6:final-long-vowel-closure","source_type":"word_analysis","support_ids":["sup_6d3d75322db987c234e0","sup_c9863cca499e0ade7fdc"],"title":"priority becomes the audible landing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:6","qac_refs":["87:18:5:1","87:18:5:2"],"status":"accepted"}},{"anchor_refs":["87:18:6"],"branch_refs":[],"candidate_id":"cand_5ff8298081f2536faa1a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:6:first-last-temporal-bracket","source_type":"word_analysis","support_ids":["sup_3cae0c6bc6c115cc94e8","sup_c9863cca499e0ade7fdc"],"title":"last realm answered by first records","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:6","qac_refs":["87:18:5:1","87:18:5:2"],"status":"accepted"}},{"anchor_refs":["87:18:6"],"branch_refs":[],"candidate_id":"cand_58daffa77e6076429de7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:6:one-qualified-record-set","source_type":"word_analysis","support_ids":["sup_0ee31e10ffad3b79dd2f","sup_c9863cca499e0ade7fdc"],"title":"broken plural treated as one set","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:6","qac_refs":["87:18:5:1","87:18:5:2"],"status":"accepted"}},{"anchor_refs":["87:18:6"],"branch_refs":[],"candidate_id":"cand_0169a0f7a38d7cab7dce","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:18:6:priority-source-status","source_type":"word_analysis","support_ids":["sup_7467518a382ff5aedabe","sup_c9863cca499e0ade7fdc"],"title":"broad root narrowed to anterior authority","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:18:6","qac_refs":["87:18:5:1","87:18:5:2"],"status":"accepted"}},{"anchor_refs":["87:18:4"],"branch_refs":[],"candidate_id":"cand_bd3fade9430623dba671","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:18:4:2","source_type":"qac_morpheme","support_ids":["sup_ad73b310903aa636d753"],"title":"QAC root occurrence: ص ح ف","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:18:5"],"branch_refs":[],"candidate_id":"cand_6082a50aa4ed7989f164","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000067","root_001684"],"scope":"focus_ayah","source_local_id":"87:18:5:2","source_type":"qac_morpheme","support_ids":["sup_e58e25721baaf0ac4784"],"title":"QAC root occurrence: ء و ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:18"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:18","branch_refs":["root_000067/B001","root_000845/B002"],"candidate_id":"cand_49e8bc88876e0bab25ea","commentary_obligation":"review","hft_ref":"hft_967599bba15e39c46875","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_prior_textual_attestation","source_type":"hft","support_ids":["sup_0ba9419ab25b6e5b671e"],"title":"baseline_prior_textual_attestation","trust":"legacy_unbound"},{"anchor_refs":["87:18"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:18","branch_refs":["root_000845/B003","root_001684/B002"],"candidate_id":"cand_b2f3d9a718de8ab9aa34","commentary_obligation":"review","hft_ref":"hft_0e8552e213a1f29c419a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_successive_archive","source_type":"hft","support_ids":["sup_6940b6d1eba667610fc7"],"title":"baseline_successive_archive","trust":"legacy_unbound"},{"anchor_refs":["87:18"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:18","branch_refs":["root_000067/B002","root_000845/B002"],"candidate_id":"cand_54c429f748c97833f5b7","commentary_obligation":"review","hft_ref":"hft_b889fd7444aef6a79957","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_origin_bearing_outcome","source_type":"hft","support_ids":["sup_7643f4841419c3065d94"],"title":"baseline_origin_bearing_outcome","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"87:18:1:1","qac_word_ref":"87:18:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"هَٰذَا","morph_features":"STEM|POS:DEM|LEM:ha`*aA|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"87:18:2:1","qac_word_ref":"87:18:2","root_ar":"","surface_ar":"هَٰذَا"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"87:18:3:1","qac_word_ref":"87:18:3","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"87:18:3:2","qac_word_ref":"87:18:3","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"87:18:4:1","qac_word_ref":"87:18:4","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"صُحُف","morph_features":"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"87:18:4:2","qac_word_ref":"87:18:4","root_ar":"ص ح ف","surface_ar":"صُّحُفِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"87:18:5:1","qac_word_ref":"87:18:5","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","root_ar":"ء و ل","surface_ar":"أُولَىٰ"}],"word_analysis_qac_refs":[["87:18:1:1"],["87:18:2:1"],["87:18:3:1"],["87:18:3:2"],["87:18:4:1","87:18:4:2"],["87:18:5:1","87:18:5:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["87:18:1","87:18:2","87:18:3","87:18:4","87:18:5","87:18:6"]},"focus_surface_evidence":{"arabic_uthmani":"إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"87:18:1:1","qac_word_ref":"87:18:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"هَٰذَا","morph_features":"STEM|POS:DEM|LEM:ha`*aA|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"87:18:2:1","qac_word_ref":"87:18:2","root_ar":"","surface_ar":"هَٰذَا"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"87:18:3:1","qac_word_ref":"87:18:3","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"87:18:3:2","qac_word_ref":"87:18:3","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"87:18:4:1","qac_word_ref":"87:18:4","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"صُحُف","morph_features":"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"87:18:4:2","qac_word_ref":"87:18:4","root_ar":"ص ح ف","surface_ar":"صُّحُفِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"87:18:5:1","qac_word_ref":"87:18:5","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَوَّل","morph_features":"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:18:5:2","qac_word_ref":"87:18:5","root_ar":"ء و ل","surface_ar":"أُولَىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["87:18:1:1"],["87:18:2:1"],["87:18:3:1"],["87:18:3:2"],["87:18:4:1","87:18:4:2"],["87:18:5:1","87:18:5:2"]],"word_analysis_refs":["87:18:1","87:18:2","87:18:3","87:18:4","87:18:5","87:18:6"],"word_rows":[{"analysis_record_ref":"87:18:1","analytic_gloss_range_en":"emphatic annulling particle that opens and certifies the whole nominal claim","analytic_root_gloss_range_en":null,"qac_refs":["87:18:1:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"إِنَّ","transliteration":"inna"}},{"analysis_record_ref":"87:18:2","analytic_gloss_range_en":"near masculine singular demonstrative pointing to discourse content rather than naming a new lexical object","analytic_root_gloss_range_en":null,"qac_refs":["87:18:2:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"هَٰذَا","transliteration":"hādhā"}},{"analysis_record_ref":"87:18:3","analytic_gloss_range_en":"predicate-side emphatic lām reinforcing the following prepositional claim","analytic_root_gloss_range_en":null,"qac_refs":["87:18:3:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"لَ","transliteration":"la"}},{"analysis_record_ref":"87:18:4","analytic_gloss_range_en":"preposition heading the predicate and framing the records as the space of textual containment","analytic_root_gloss_range_en":null,"qac_refs":["87:18:3:2"],"root":{"note":"— (no root)"},"surface":{"arabic":"فِى","transliteration":"fī"}},{"analysis_record_ref":"87:18:5","analytic_gloss_range_en":"definite plural written records or scriptures governed by the preposition and qualified by the following adjective","analytic_root_gloss_range_en":"root field includes broad surfaces, written sheets, collected codex material, dish/basin senses, and misreading from written sheets; the local plural selects written-record scripture while surface and collection imagery remain relevant","qac_refs":["87:18:4:1","87:18:4:2"],"root":{"arabic":"ص ح ف","transliteration":"ṣ-ḥ-f"},"surface":{"arabic":"ٱلصُّحُفِ","transliteration":"aṣ-ṣuḥufi"}},{"analysis_record_ref":"87:18:6","analytic_gloss_range_en":"definite feminine singular adjective qualifying the records as former, first, or earlier-source records","analytic_root_gloss_range_en":"broad root field of nearness, succession, charge, alliance, turning, priority, warning formulae, and other specialized branches; the local adjective selects anterior priority and source-status","qac_refs":["87:18:5:1","87:18:5:2"],"root":{"arabic":"و ل ي","transliteration":"w-l-y"},"surface":{"arabic":"ٱلْأُولَىٰ","transliteration":"al-ūlā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["87:18"],"branch_refs":["root_000067/B001","root_000845/B002"],"candidate_id":"cand_49e8bc88876e0bab25ea","evidence_scope":"focus_ayah","hft_ref":"hft_967599bba15e39c46875","item_id":"baseline_prior_textual_attestation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_prior_textual_attestation","support_id":"sup_0ba9419ab25b6e5b671e"},{"anchor_refs":["87:18"],"branch_refs":["root_000845/B003","root_001684/B002"],"candidate_id":"cand_b2f3d9a718de8ab9aa34","evidence_scope":"focus_ayah","hft_ref":"hft_0e8552e213a1f29c419a","item_id":"baseline_successive_archive","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_successive_archive","support_id":"sup_6940b6d1eba667610fc7"},{"anchor_refs":["87:18"],"branch_refs":["root_000067/B002","root_000845/B002"],"candidate_id":"cand_54c429f748c97833f5b7","evidence_scope":"focus_ayah","hft_ref":"hft_b889fd7444aef6a79957","item_id":"baseline_origin_bearing_outcome","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_origin_bearing_outcome","support_id":"sup_7643f4841419c3065d94"}],"diagnostics":[],"lane_counts":{"global":8,"macro":10,"micro":3},"packet_summary":{"ayah_count":19,"focus_ref":"87:18","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ء ث ر","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":true,"target_occurrences":9,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"87:18","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"87:18","lane":"micro","linguistic_source_ref":"87:18","surface_ref":"87:18","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"87:18","target_tokens":[["Kuşkusuz",["87:18:1"]],["bu",["87:18:2"]],["önceki",["87:18:5"]],["sayfalarda",["87:18:4"]],["yer",["87:18:3"]],["alır",["87:18:3"]]],"text":"Kuşkusuz bu, önceki sayfalarda yer alır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s087-p01-001-019","label":"Whole surah","number":1,"refs":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:1:double-assertion-with-predicate-lam","source_type":"word_analysis","support_id":"sup_0478b960eb41e8364cb1","text":"{\"blocking_evidence\":null,\"headline\":\"opening assertion renewed at the predicate\",\"reader_payoff\":\"The reader notices that emphasis is not diffuse; it begins at the clause opening and returns at the predicate that locates the teaching in the records.\",\"reason\":\"The bundle separates {{ar:لَ}} ({{tr:la}}) from {{ar:فِى}} ({{tr:fī}}), confirming that the second assertion marker belongs to the predicate side.\",\"representative_source_ids\":[\"QI-eb8ac08f\",\"MT-19825c8d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:1:opening-certification","source_type":"word_analysis","support_id":"sup_0547044f4c9919bf853e","text":"{\"blocking_evidence\":null,\"headline\":\"certifying particle opens the claim\",\"reader_payoff\":\"The reader notices that the ayah begins by certifying the archive claim before any lexical noun or verb supplies new content.\",\"reason\":\"QAC and attachment evidence support an {{ar:إِنَّ}} ({{tr:inna}}) clause whose name is {{ar:هَٰذَا}} ({{tr:hādhā}}) and whose predicate is the archive-location phrase.\",\"representative_source_ids\":[\"QG-6297cffc\",\"MG-c7082549\",\"QS-d95a2ce5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:1:attestation-turn-at-surah-close","source_type":"word_analysis","support_id":"sup_0e3a0b3223bae8229d1f","text":"{\"blocking_evidence\":null,\"headline\":\"valuation turns into attestation\",\"reader_payoff\":\"The reader sees the close of the surah change mode: after the value ranking in 87:17, the teaching is certified in prior records.\",\"reason\":\"The local clause is syntactically complete, and the next ayah (87:19) supplies the named-record continuation.\",\"representative_source_ids\":[\"QT-dc0be6b3\",\"QT-e4ad5b57\",\"QB-741f3584\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:6:one-qualified-record-set","source_type":"word_analysis","support_id":"sup_0ee31e10ffad3b79dd2f","text":"{\"blocking_evidence\":null,\"headline\":\"broken plural treated as one set\",\"reader_payoff\":\"The reader sees multiple records gathered into one known former archive rather than scattered earlier writings.\",\"reason\":\"The agreement pattern and definite article both bind the adjective into the same definite archive phrase.\",\"representative_source_ids\":[\"QG-8ac73e61\",\"QF-d1624dff\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:5:definite-governed-archive","source_type":"word_analysis","support_id":"sup_259a43526569b3b62428","text":"{\"blocking_evidence\":null,\"headline\":\"known records governed by the preposition\",\"reader_payoff\":\"The reader notices that the ayah invokes an identifiable archive as the object of containment, not an independent subject or generic writings.\",\"reason\":\"QAC and attachment evidence mark {{ar:ٱلصُّحُفِ}} ({{tr:aṣ-ṣuḥufi}}) as definite plural genitive after {{ar:فِى}} ({{tr:fī}}), modified by the final adjective.\",\"representative_source_ids\":[\"QG-4d37334e\",\"QG-64caca4b\",\"MG-c3bf906a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:5","source_type":"word_analysis","support_id":"sup_3a8f3091d73b0aab7abd","text":"{\"gloss_range\":\"definite plural written records or scriptures governed by the preposition and qualified by the following adjective\",\"prose\":\"{{ar:ٱلصُّحُفِ}} ({{tr:aṣ-ṣuḥufi}}) is the governed genitive object of {{ar:فِى}} ({{tr:fī}}), and its definiteness makes the records identifiable rather than generic writings. The root's written-surface branch makes the attestation materially textual: the teaching is placed in preservable sheets or records, not only in memory. Its plural form spreads that witness across a record-set, while the following adjective keeps the archive and anteriority in one predicate phrase. The word also waits for 87:19, where the general archive is resumed and specified through the records of Abraham and Moses, turning archive category into prophetic exemplars and making the present recitation continuous with earlier records rather than novel. Accepted recitational compression sharpens the noun's cadence after the light particles without changing the plural written-record sense.\",\"root_display\":\"{{ar:ص ح ف}} ({{tr:ṣ-ḥ-f}})\",\"root_gloss_range\":\"root field includes broad surfaces, written sheets, collected codex material, dish/basin senses, and misreading from written sheets; the local plural selects written-record scripture while surface and collection imagery remain relevant\",\"surface_display\":\"{{ar:ٱلصُّحُفِ}} ({{tr:aṣ-ṣuḥufi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:6:first-last-temporal-bracket","source_type":"word_analysis","support_id":"sup_3cae0c6bc6c115cc94e8","text":"{\"blocking_evidence\":null,\"headline\":\"last realm answered by first records\",\"reader_payoff\":\"The reader notices the time-axis: the later realm of 87:17 is certified by earlier records in 87:18.\",\"reason\":\"The boundary rows explicitly connect 87:17 and 87:18, and the local adjective occupies the closing position of 87:18.\",\"representative_source_ids\":[\"QT-536bd664\",\"MT-3f2cf955\",\"QE-1cf7ce38\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:4:textual-containment-not-source","source_type":"word_analysis","support_id":"sup_3ed2aa8826b00ba18233","text":"{\"blocking_evidence\":null,\"headline\":\"records as container, not source-from\",\"reader_payoff\":\"The reader sees written scripture as the container of attestation rather than a vague association or source label.\",\"reason\":\"The governed object is the definite record noun, and no local evidence selects a source-from or report-about preposition.\",\"representative_source_ids\":[\"QS-ca830160\",\"MS-f6a01644\",\"QI-e3347636\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:3","source_type":"word_analysis","support_id":"sup_41a1a927c12b7c424180","text":"{\"gloss_range\":\"predicate-side emphatic lām reinforcing the following prepositional claim\",\"prose\":\"{{ar:لَ}} ({{tr:la}}) is small, but it is placed exactly on the predicate side. It does not add a new referent; it raises certainty on the claim that the gathered teaching is in the written records. Together with the opening {{ar:إِنَّ}} ({{tr:inna}}), it makes the archive-location phrase the reinforced center of the ayah, and its short pulse before {{ar:فِى}} ({{tr:fī}}) lets the heavier record noun arrive as the audible landing.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَ}} ({{tr:la}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:3:predicate-side-emphasis","source_type":"word_analysis","support_id":"sup_4228afde56ba9a938900","text":"{\"blocking_evidence\":null,\"headline\":\"emphasis lands on the predicate\",\"reader_payoff\":\"The reader notices that the emphasis targets archive location, not merely the existence of the demonstrative content.\",\"reason\":\"The bundle splits {{ar:لَ}} ({{tr:la}}) as an emphatic particle before the prepositional predicate.\",\"representative_source_ids\":[\"QG-eb1459de\",\"MG-320a10fe\",\"QS-a2f8b3d8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:2:demonstrative-subject-under-inna","source_type":"word_analysis","support_id":"sup_45433f6ce48ac3bcad44","text":"{\"blocking_evidence\":null,\"headline\":\"deictic subject under assertion\",\"reader_payoff\":\"The reader notices that the demonstrative is not floating; it is the grammatical subject whose content will be located in the records.\",\"reason\":\"Attachment evidence marks {{ar:هَٰذَا}} ({{tr:hādhā}}) as the governed name of {{ar:إِنَّ}} ({{tr:inna}}), with the prepositional phrase as predicate.\",\"representative_source_ids\":[\"QG-8e4aff59\",\"QG-cd56440f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:1:compact-certification-sound","source_type":"word_analysis","support_id":"sup_4e87fbd2ca27535aa2ec","text":"{\"blocking_evidence\":null,\"headline\":\"compact audible opening\",\"reader_payoff\":\"The reader hears a compressed certification formula whose weight falls quickly on the document-location claim.\",\"reason\":\"The nominal claim has no overt copula, and the opening particle gives the short formula assertive force.\",\"representative_source_ids\":[\"QT-1a9c3342\",\"QP-27b7dfff\",\"QB-de63865a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:2:discourse-content-compression","source_type":"word_analysis","support_id":"sup_679aded12ce04fa57b29","text":"{\"blocking_evidence\":null,\"headline\":\"near demonstrative gathers prior teaching\",\"reader_payoff\":\"The reader has to gather the preceding teaching as one object rather than treat the ayah as naming a fresh topic.\",\"reason\":\"The attachment layer marks the demonstrative reference as ambiguous between nearby discourse scopes, so the topic survives as discourse compression without forcing one narrow antecedent.\",\"representative_source_ids\":[\"QG-980ebaaf\",\"MG-27279367\",\"QS-a6ee174c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:5:written-surface-media","source_type":"word_analysis","support_id":"sup_6b7f9e91f147cc554eff","text":"{\"blocking_evidence\":null,\"headline\":\"material written-surface attestation\",\"reader_payoff\":\"The reader sees the proof as textual and preservable, not merely remembered, oral, or abstract.\",\"reason\":\"V4 accepts written-sheet and collected-sheet branches for {{ar:ص ح ف}} ({{tr:ṣ-ḥ-f}}); local QAC form and predicate context select the written-record scripture branch rather than every accepted root branch.\",\"representative_source_ids\":[\"QS-020b6af7\",\"QS-39e0c217\",\"MS-e5fbb2af\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:6:final-long-vowel-closure","source_type":"word_analysis","support_id":"sup_6d3d75322db987c234e0","text":"{\"blocking_evidence\":null,\"headline\":\"priority becomes the audible landing\",\"reader_payoff\":\"The reader hears firstness or formerness as the final acoustic landing of the ayah.\",\"reason\":\"The orthographic and phonetic rows are local to the final adjective and do not require a different lexical sense.\",\"representative_source_ids\":[\"QF-2635c12c\",\"QF-502b8c9d\",\"QP-1b5b96a8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:6:priority-source-status","source_type":"word_analysis","support_id":"sup_7467518a382ff5aedabe","text":"{\"blocking_evidence\":null,\"headline\":\"broad root narrowed to anterior authority\",\"reader_payoff\":\"The reader notices that formerness carries source-priority and continuity, not merely chronological age.\",\"reason\":\"V4 shows many accepted {{ar:و ل ي}} ({{tr:w-l-y}}) branches, but local QAC and attachment evidence select the adjective of former or first priority.\",\"representative_source_ids\":[\"QS-0db49745\",\"QS-7046d554\",\"MS-5a2fad53\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:5:recitational-variant-and-weight","source_type":"word_analysis","support_id":"sup_805b21397212758bf19c","text":"{\"blocking_evidence\":null,\"headline\":\"cadence shifts without sense shift\",\"reader_payoff\":\"The reader hears the archive noun carry weight after the particles, while the variant confirms that the written-record meaning is stable.\",\"reason\":\"The variant and phonetic observations are useful for cadence, but they do not alter the local plural written-record analysis.\",\"representative_source_ids\":[\"QS-d81b4b36\",\"QF-997dc861\",\"MP-4d1f4e7c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:4","source_type":"word_analysis","support_id":"sup_822f1ebfef6f4e8fa94f","text":"{\"gloss_range\":\"preposition heading the predicate and framing the records as the space of textual containment\",\"prose\":\"{{ar:فِى}} ({{tr:fī}}) heads the predicate, so the ayah's claim is not origin from, ownership by, or a new action, but located attestation. After the value comparison in 87:17, the predicate type changes: the close no longer assigns qualities to the Hereafter but locates the teaching in an archive. With {{ar:ٱلصُّحُفِ}} ({{tr:aṣ-ṣuḥufi}}) as its object, ordinary containment becomes textual inclusion: the teaching is found within written material. Because the written-recited surface joins {{ar:لَ}} ({{tr:la}}) and {{ar:فِى}} ({{tr:fī}}) tightly, emphasis and location are heard together even though the two functions remain distinct.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِى}} ({{tr:fī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:2:scope-of-archive-claim","source_type":"word_analysis","support_id":"sup_948a2723e972f74e2e4a","text":"{\"blocking_evidence\":null,\"headline\":\"pointer sets what is attested\",\"reader_payoff\":\"The reader notices that the ayah first turns recited teaching into a documentable object, then supplies its archive.\",\"reason\":\"The demonstrative precedes the predicate, so the listener collects the discourse object before hearing its location in the records.\",\"representative_source_ids\":[\"QI-9296373f\",\"QT-e715f012\",\"QB-a92f9ba8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:3:compact-particle-pulse","source_type":"word_analysis","support_id":"sup_9edcf31695a0eb8502d4","text":"{\"blocking_evidence\":null,\"headline\":\"brief pulse before the archive noun\",\"reader_payoff\":\"The reader hears certainty enter right at the threshold of the archive phrase before the substantive record word arrives.\",\"reason\":\"The sound observation is anchored by the adjacent particle-preposition sequence and the following heavier noun.\",\"representative_source_ids\":[\"QT-8b0d8ca5\",\"QP-a36593a0\",\"QY-71bd8e59\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:6:adjective-inside-pp","source_type":"word_analysis","support_id":"sup_9f35c685c3bae56c5855","text":"{\"blocking_evidence\":null,\"headline\":\"final adjective qualifies the archive\",\"reader_payoff\":\"The reader notices that the location claim is narrowed from within: the records are specifically the former records.\",\"reason\":\"Attachment evidence strongly licenses {{ar:ٱلْأُولَىٰ}} ({{tr:al-ūlā}}) as the adjective of {{ar:ٱلصُّحُفِ}} ({{tr:aṣ-ṣuḥufi}}).\",\"representative_source_ids\":[\"QG-02e977de\",\"QG-d07ed793\",\"MG-2c3fb71d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:6:delayed-qualifier-resolution","source_type":"word_analysis","support_id":"sup_a4be34a20e5a0cbc63c6","text":"{\"blocking_evidence\":null,\"headline\":\"final word resolves the archive\",\"reader_payoff\":\"The reader feels the phrase tighten at the final word: written records become earlier-source testimony that 87:19 will name.\",\"reason\":\"The final adjective is syntactically attached to the archive noun, and the next ayah (87:19) turns the priority into named exemplars.\",\"representative_source_ids\":[\"QT-b549d5ca\",\"MT-a30cda55\",\"QB-1d942a8b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:18:4:2","source_type":"qac_morpheme","support_id":"sup_ad73b310903aa636d753","text":"{\"lemma_ar\":\"صُحُف\",\"morph_features\":\"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"87:18:4:2\",\"qac_word_ref\":\"87:18:4\",\"root_ar\":\"ص ح ف\",\"surface_ar\":\"صُّحُفِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:5:boundary-to-archival-durability","source_type":"word_analysis","support_id":"sup_b361dc223c53cedfe926","text":"{\"blocking_evidence\":null,\"headline\":\"from value scene to preserved witness\",\"reader_payoff\":\"The reader notices that permanence is no longer only a value claim; it is supported by preserved documentation.\",\"reason\":\"The boundary rows are coherent with the local shift from the comparative statement of 87:17 to the archive predicate of 87:18.\",\"representative_source_ids\":[\"QB-40039b80\",\"QB-ea539907\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:5:plural-record-set","source_type":"word_analysis","support_id":"sup_b5c58564eae262bc7a86","text":"{\"blocking_evidence\":null,\"headline\":\"plural witness across records\",\"reader_payoff\":\"The reader notices that continuity is spread across records rather than resting on one isolated document.\",\"reason\":\"The local noun is plural and definite, and contextual profiles show the exact root/form as an archive noun with adjective and prepositional attachments.\",\"representative_source_ids\":[\"QF-40355178\",\"QF-534ed48c\",\"MF-ee4560e2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:5:wider-archive-continuity","source_type":"word_analysis","support_id":"sup_bae75017ca8274c77d17","text":"{\"blocking_evidence\":null,\"headline\":\"scriptural archive continuity\",\"reader_payoff\":\"The reader notices that the word is a hinge between present recitation and earlier prophetic records, not a novelty claim.\",\"reason\":\"The CRITICAL rows tie the word to a record-lineage field, while the local predicate keeps the claim focused on textual containment.\",\"representative_source_ids\":[\"QI-968b87a9\",\"QE-12196ee4\",\"QY-53089896\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:2:immediacy-against-prior-records","source_type":"word_analysis","support_id":"sup_bd0e4b45619a287c484e","text":"{\"blocking_evidence\":null,\"headline\":\"present pointing meets former records\",\"reader_payoff\":\"The reader sees immediacy and anteriority meet: the present teaching is the very thing being traced to earlier records.\",\"reason\":\"The local sequence places the near demonstrative before the archive phrase that ends with the formerness adjective.\",\"representative_source_ids\":[\"QE-9c8643e2\",\"QB-a6bbfb8c\",\"QY-865b9253\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:6","source_type":"word_analysis","support_id":"sup_c9863cca499e0ade7fdc","text":"{\"gloss_range\":\"definite feminine singular adjective qualifying the records as former, first, or earlier-source records\",\"prose\":\"{{ar:ٱلْأُولَىٰ}} ({{tr:al-ūlā}}) closes the phrase as the adjective of {{ar:ٱلصُّحُفِ}} ({{tr:aṣ-ṣuḥufi}}), not as a separate predicate. Its feminine singular agreement treats the nonhuman plural records as one qualified set. From the broad {{ar:و ل ي}} ({{tr:w-l-y}}) field, the local form selects anterior priority: these are earlier, source-worthy records, not merely old documents. With the record-lineage echo of 53:36-37 and the specification that follows in 87:19, the former-record phrase works as lineage certification rather than a loose temporal label. Coming after 87:17's last-realm term, it creates a first-last bracket, and its final long vowel lets source-priority become the audible close while 87:19 turns formerness into named prophetic records.\",\"root_display\":\"{{ar:و ل ي}} ({{tr:w-l-y}})\",\"root_gloss_range\":\"broad root field of nearness, succession, charge, alliance, turning, priority, warning formulae, and other specialized branches; the local adjective selects anterior priority and source-status\",\"surface_display\":\"{{ar:ٱلْأُولَىٰ}} ({{tr:al-ūlā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:4:predicate-type-boundary-shift","source_type":"word_analysis","support_id":"sup_ca5bb0509f01e5ddbfe7","text":"{\"blocking_evidence\":null,\"headline\":\"from qualities to archive location\",\"reader_payoff\":\"The reader notices a change in predicate type after 87:17: the close no longer compares values but gives documentary location.\",\"reason\":\"The local predicate is prepositional, and the previous ayah (87:17) supplies the immediate value-judgment boundary.\",\"representative_source_ids\":[\"QB-192d8fb7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:3:double-assertion-center","source_type":"word_analysis","support_id":"sup_d82984ac6137f636f35b","text":"{\"blocking_evidence\":null,\"headline\":\"short clause with doubled certainty\",\"reader_payoff\":\"The reader hears brevity as intensified certainty: the clause is short because the archive claim is sharply asserted.\",\"reason\":\"Attachment evidence identifies a single {{ar:إِنَّ}} ({{tr:inna}}) clause with an emphatic lām before its predicate.\",\"representative_source_ids\":[\"QI-65f46412\",\"MT-539e3fb2\",\"QE-636cd9e5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:2:stable-deictic-surface","source_type":"word_analysis","support_id":"sup_d82d7402de667c00efcb","text":"{\"blocking_evidence\":null,\"headline\":\"long-vowel pointing surface\",\"reader_payoff\":\"The reader hears the pointer as a stable near-deictic form before the clause shifts into archive location.\",\"reason\":\"The orthographic observation supports the same deictic function already licensed by QAC and attachment evidence.\",\"representative_source_ids\":[\"QF-533e2e34\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:6:archive-formula-and-lineage","source_type":"word_analysis","support_id":"sup_dbb1293421dea543b1b8","text":"{\"blocking_evidence\":null,\"headline\":\"former records as lineage formula\",\"reader_payoff\":\"The reader sees the former-record phrase as lineage certification, with the record tradition echoed at 53:36-37 and specified next in 87:19.\",\"reason\":\"The CRITICAL row gives the concrete 53:36-37 parallel, while the immediate context gives 87:19 as the local specification.\",\"representative_source_ids\":[\"QI-ece62769\",\"MI-7f2378f3\",\"QE-635aa6b0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:4:emphasis-location-surface-bundle","source_type":"word_analysis","support_id":"sup_e0c048df5d891f868b0f","text":"{\"blocking_evidence\":null,\"headline\":\"emphasis fused to location in delivery\",\"reader_payoff\":\"The reader hears the reinforced claim enter the archive phrase as one compact movement before the heavier noun.\",\"reason\":\"The bundle analytically separates {{ar:لَ}} ({{tr:la}}) and {{ar:فِى}} ({{tr:fī}}), but their adjacency explains the compressed delivery.\",\"representative_source_ids\":[\"QF-a2af3c4e\",\"QP-9e181982\",\"QY-0b263770\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:18:5:2","source_type":"qac_morpheme","support_id":"sup_e58e25721baaf0ac4784","text":"{\"lemma_ar\":\"أَوَّل\",\"morph_features\":\"STEM|POS:ADJ|LEM:>aw~al|ROOT:Awl|F|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"87:18:5:2\",\"qac_word_ref\":\"87:18:5\",\"root_ar\":\"ء و ل\",\"surface_ar\":\"أُولَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:4:pp-predicate-location","source_type":"word_analysis","support_id":"sup_ebcaa199599b6ea30443","text":"{\"blocking_evidence\":null,\"headline\":\"preposition carries the predicate\",\"reader_payoff\":\"The reader notices that the ayah does not narrate an action; it predicates located attestation.\",\"reason\":\"Attachment evidence marks the phrase headed by {{ar:فِى}} ({{tr:fī}}) as the predicate of the {{ar:إِنَّ}} ({{tr:inna}}) clause.\",\"representative_source_ids\":[\"QG-9e6c4f2b\",\"MG-684e8b56\",\"QT-b1d0e9b8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:2","source_type":"word_analysis","support_id":"sup_ef249701c63b45d7b368","text":"{\"gloss_range\":\"near masculine singular demonstrative pointing to discourse content rather than naming a new lexical object\",\"prose\":\"{{ar:هَٰذَا}} ({{tr:hādhā}}) is the governed subject of {{ar:إِنَّ}} ({{tr:inna}}), but it does not name the content directly. Its near, stable pointing form gathers the preceding teaching into a single discourse object rather than a list of separate items, and then lets the predicate locate that object in the earlier records. The demonstrative therefore controls the scope of the archive claim: what is being certified is the content carried forward from the preceding discourse, especially the movement through 87:14-17, while the present pointer stands opposite the formerness that will close the phrase.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:هَٰذَا}} ({{tr:hādhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:5:next-ayah-specification","source_type":"word_analysis","support_id":"sup_f0e57f7494e1fadd4037","text":"{\"blocking_evidence\":null,\"headline\":\"general archive becomes named records\",\"reader_payoff\":\"The reader sees the final couplet tighten from archive category to named exemplars in the next ayah (87:19).\",\"reason\":\"The next ayah (87:19) repeats the record noun and specifies the prophetic lineage, so the inter-ayah topic is directly anchored.\",\"representative_source_ids\":[\"QI-816334b6\",\"MI-0c7e4615\",\"MT-f04fbe6d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:5:phrase-internal-qualification","source_type":"word_analysis","support_id":"sup_fd0421da8851a641c466","text":"{\"blocking_evidence\":null,\"headline\":\"archive waits for its qualifier\",\"reader_payoff\":\"The reader notices that the archive is not merely written; it is written-record anteriority delivered as one phrase.\",\"reason\":\"Attachment evidence strongly licenses the final adjective as qualifying {{ar:ٱلصُّحُفِ}} ({{tr:aṣ-ṣuḥufi}}).\",\"representative_source_ids\":[\"QG-1262cc55\",\"QT-f2c5c866\",\"QH-d895c083\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:18:1","source_type":"word_analysis","support_id":"sup_fdf7c832367a3b348a04","text":"{\"gloss_range\":\"emphatic annulling particle that opens and certifies the whole nominal claim\",\"prose\":\"{{ar:إِنَّ}} ({{tr:inna}}) opens the ayah as certification rather than tentative report: the archive-location claim is asserted before the listener reaches the demonstrative or the written-record phrase. Its force is renewed by the later predicate lām, so the short clause surrounds the claim of being in prior records with double assertion. At the close of the surah, this shifts the discourse from the value verdict of 87:17 into formal attestation, with a compact, copula-less formula that prepares 87:19 to name the records.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِنَّ}} ({{tr:inna}})\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ","ayah_ref":"87:18"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000067/B001","root_000845/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000845","role":"The written-sheet image supplies the concrete textual container asserted by في.","root":"ص ح ف","source_ref":"87:18","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000067","role":"Beginning and precedence place those written witnesses before the present utterance in time or rank.","root":"ء و ل","source_ref":"87:18","source_word_indices":["5"]}],"changed_reading":{"after":"This teaching is emphatically attested as content within written predecessors.","before":"This teaching has some vague ancient precedent."},"confidence":"strong","focus_anchor":"The emphatic construction إن هذا لفي locates the deictic content inside the plural الصحف, while الأولى qualifies those sheets as prior.","mechanism":"A salient but internally unspecified 'this' is not merely old wisdom; it is presented as recoverable textual content already borne by earlier written witnesses.","model_id":"baseline_prior_textual_attestation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_prior_textual_attestation","source_type":"hft","support_id":"sup_0ba9419ab25b6e5b671e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ","ayah_ref":"87:18"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000845/B003","root_001684/B002"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000845","role":"The collected-sheets image turns the plural into an archive assembled from multiple textual units.","root":"ص ح ف","source_ref":"87:18","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_001684","role":"Continuous succession supplies the ordering relation that links the prior sheets into a relay.","root":"ء و ل","source_ref":"87:18","source_word_indices":["5"]}],"changed_reading":{"after":"The first sheets form a successive, internally plural archive of witness.","before":"The first scriptures are an undifferentiated ancient source."},"confidence":"medium","focus_anchor":"The plural الصحف and the split inventory attached to الأولى allow plurality to be read as an ordered archive rather than a single old book.","mechanism":"Collected sheets and uninterrupted succession form a relay: priorness belongs to a sequence of textual witnesses whose continuity matters as much as their age.","model_id":"baseline_successive_archive"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_successive_archive","source_type":"hft","support_id":"sup_6940b6d1eba667610fc7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ","ayah_ref":"87:18"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000067/B002","root_000845/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000845","role":"Written sheets anchor the reading in actual textual predecessors rather than free temporal symbolism.","root":"ص ح ف","source_ref":"87:18","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000067","role":"Return to outcome or final meaning makes the earliest textual point capable of carrying its later interpretive destination.","root":"ء و ل","source_ref":"87:18","source_word_indices":["5"]}],"changed_reading":{"after":"The textual beginning is also a source to which the teaching's eventual meaning returns.","before":"First means only chronologically old."},"confidence":"exploratory","focus_anchor":"الأولى directly denotes firstness, yet its dominant mapped inventory also contains return to outcome and interpretive result.","mechanism":"The first sheets can function as an origin that already bears a later meaning: textual precedence and eventual interpretation coexist rather than pointing in opposite directions.","model_id":"baseline_origin_bearing_outcome"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_origin_bearing_outcome","source_type":"hft","support_id":"sup_7643f4841419c3065d94","trust":"legacy_unbound"}]}
</lane_packet_json>
