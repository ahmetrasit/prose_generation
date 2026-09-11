# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **87:14**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s087-regular-20260911/s087/87_14/micro.discovery.json` and modify nothing
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
  "ayah_ref": "87:14",
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
{"analysis_context":{"analysis_id":"s087-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"87:14","host_surah":87,"lane_context_refs":[],"ordered_context_refs":["87:0","87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:15","87:16","87:17","87:18","87:19","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal, büyüme ve artmayı kapsar; ahlaki arınma, mali yükümlülük, uygunluk ve tek-çift karşıtlığı ayrı dallarda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000637/B001","candidate_links":[{"candidate_id":"cand_5c2dab6f77af8d8e7755","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَزَكَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:4:1","qac_word_ref":"87:14:4","surface_ar":"تَزَكَّىٰ"}],"gloss":"büyüyüp artma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, bir şeyin önceki durumuna göre büyümesi ve artmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ekinin gelişmesi, herhangi bir şeyin çoğalması ve bir canlının dolgunlaşması bu artışın somut gerçekleşmeleridir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bazı açıklamalarda büyüme, ilahi iyiliğin sağladığı verim ve bollukla ilişkilendirilir."}}],"root_ar":"ز ك و","root_id":"root_000637","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin gelişme, miktar veya dolgunluk bakımından önceki durumunu aşmasını anlatan genel karşılıktır.","boundary_detail":"Bu dal, büyüme ve artmayı kapsar; ahlaki arınma, mali yükümlülük, uygunluk ve tek-çift karşıtlığı ayrı dallarda kalır.","branch_image_ar":"النماء والزيادة","concept_gloss":"büyüyüp artma","contextual_glosses":[{"applicability":"Ekinin veya başka bir varlığın zaman içinde büyüyerek miktarca artması anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Süreç içindeki gelişmeyi ve bunun sonucundaki artışı birlikte korur."},"facet_ids":["F001","F002"],"text":"gelişip çoğalmak","usage_role":"contextual"},{"applicability":"Artışın verim ve iyilikle gelen bolluk yönü özellikle öne çıkarıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bolluk niteliği taşımayan yalın büyüme ve dolgunlaşma kullanımlarını kapsamaz.","preserves":"Verim ve bollukla sonuçlanan artış yönünü korur."},"facet_ids":["F003"],"text":"bolluk kazanmak","usage_role":"contextual"}],"definition":"Bir varlığın gelişerek büyümesi, miktarının artması veya daha dolgun ve verimli duruma gelmesidir. Bu gelişme kimi anlatımlarda ilahi iyiliğin doğurduğu bolluk olarak açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, bir şeyin önceki durumuna göre büyümesi ve artmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Ekinin gelişmesi, herhangi bir şeyin çoğalması ve bir canlının dolgunlaşması bu artışın somut gerçekleşmeleridir."},{"facet_id":"F003","role":"source_variant","statement":"Bazı açıklamalarda büyüme, ilahi iyiliğin sağladığı verim ve bollukla ilişkilendirilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gelişme, dolgunlaşma ve verim kazanma yönlerini dışarıda bırakır.","preserves":"Miktarca artma yönünü korur."},"text":"yalnızca çoğalma"}],"identity_rationale":"Kaynak ifadesi, ortak çekirdeği bir şeyin büyümesi, miktarca artması veya dolgunlaşması olarak açıkça kurar; ekin, genel varlıklar ve bollukla gelişme bu çekirdeğin farklı gerçekleşmeleridir. İlahi iyilikle elde edilen gelişme, çekirdeği değiştiren ayrı bir anlam değil, artışın kaynağını belirten bir açıklamadır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"büyümek, artmak ve verim kazanmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"büyüme ve artış"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"gelişmiş ve artışı belirgin"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"Tanrı onu büyütüp artırdı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"ekin büyüyüp arttı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kişi bolluğa kavuşup rahat yaşadı"}],"lexicalization_note":"Yalın biçimlerdeki büyüme çekirdeği ile ekin, kişi ve ettirgenlik bildiren sınırlı kullanımlar ayrı tutulur; bu kullanımlar bütün dalı tek bir bağlama daraltmaz.","neighbor_coverage_note":"Sunulan on bir adayın tamamı değerlendirildi; büyüme sınırını en açık gösteren beş karşılaştırma seçildi, yağmur, verimli arazi, su bolluğu, uygunluk ve tek-çift alanındaki daha uzak adaylar yayıma alınmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal değişimin kendisini, yani büyüyüp artmayı bildirir; komşu dal ise ortaya çıkan çokluk ve bolluk durumunu, daha geniş alanlarla birlikte öne çıkarır.","focus_only":"Odak dal, herhangi bir şeyin büyüme ve dolgunlaşma sürecini doğrudan adlandırır.","gloss":"büyüme ile bolluk","neighbor_only":"Komşu dal, malda, toplulukta veya soyda çokluğu ve uğurlu bolluğu daha geniş biçimde kapsar.","neighbor_ref":"root_000051/B004","relation_type":"near_synonym","shared_zone":"İki dal da artış, verim ve bolluk fikrinde kesişir."},{"boundary_match":"partial","distinction":"Odak dal süreç ve gelişme merkezlidir; komşu dal ise asla eklenen fazlalık ile ürün, yiyecek ve hayvan gibi alanlardaki verim ölçüsünü belirginleştirir.","focus_only":"Odak dal, genel büyümeyi ve ilahi iyilikle gelen gelişmeyi de kapsar.","gloss":"artma ile fazlalık","neighbor_only":"Komşu dal, özellikle asıl miktarın üzerindeki fazlayı ve belirli üretim alanlarındaki verim artışını öne çıkarır.","neighbor_ref":"root_000618/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de bir başlangıç durumunu aşan büyüme ve artışı anlatır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği nicel ya da gelişimsel artıştır; komşu dalın çekirdeği ise kişinin geçim durumunu düzeltmek veya güçlendirmektir.","focus_only":"Odak dal, varlığın kendisinde gerçekleşen büyüme ve miktar artışını bildirir.","gloss":"artış ile durumun düzelmesi","neighbor_only":"Komşu dal, bir kişinin geçim ve varlık durumunun yardım ya da güçlendirmeyle düzelmesini kapsar.","neighbor_ref":"root_000617/B004","relation_type":"near_neighbor","shared_zone":"İki dal da daha iyi ve daha varlıklı bir duruma geçişi çağrıştırabilir."},{"boundary_match":"opposed","distinction":"Odak dal olumlu büyüme kutbunu, komşu dal ise bitki üretmeyen toprağın olumsuz kutbunu gösterir; kapsamları tam karşıt sözcükler olacak kadar eşit değildir.","focus_only":"Odak dal, ekin dahil olmak üzere varlıkların gelişip artmasını geniş biçimde kapsar.","gloss":"gelişme ile verimsizlik","neighbor_only":"Komşu dal, özellikle hiçbir şey bitirmeyen verimsiz toprağı adlandırır.","neighbor_ref":"root_001321/B003","relation_type":"polarity_pair","shared_zone":"İki dal, toprağın veya ürünün gelişme ve verim ekseninde karşılaştırılabilir."},{"boundary_match":"partial","distinction":"Büyüme dalında belirleyici unsur artıştır; arınma dalında ise kusurdan uzaklaşıp temiz ve doğru duruma gelmektir.","focus_only":"Odak dal, fiziksel veya nicel büyümeyi, çoğalmayı ve dolgunlaşmayı içerir.","gloss":"gelişme ile arınma","neighbor_only":"Komşu dal, ahlaki temizlik, doğruluk ve birini bu duruma getirme anlamlarını içerir.","neighbor_ref":"root_000637/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal daha iyi bir duruma geçiş düşüncesinde yaklaşabilir."}],"source_phrase_ar":"أصل يدل على نماء وزيادة (maqayis)؛ زكا الزرع يزكو زكاء ازداد ونما وكل شيء ازداد ونما فهو يزكو زكاء (ayn)؛ زكا الزرع يزكو زكاء ممدود أي نما (sihah)؛ كل شيء يزداد ويسمن فهو يزكو زكاء (tahdhib)؛ أصل الزكاة النمو الحاصل عن بركة الله تعالى (mufradat)","source_summary":"Kaynakların ortak anlatımı büyüme ve artmayı merkeze alır; ekin gelişmesi, genel çoğalma, dolgunlaşma ve iyilikle gelen verim bu ortak anlamın kapsamındadır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه نماء الزرع وزيادة الشيء وسمنه وبركته وخصب الرجل وتنعمه.","what_is_not_ar":"لا يدخل فيه معنى الزكاة المالية إلا من جهة كونها سببا للنماء أو البركة، ولا معنى الزوج والشفع."},"support_links":["sup_3b224864180081dd711e"]},{"boundary":"Bu dal ahlaki ve manevi temizlik ile düzgünlüğü kapsar; yalın büyüme ve maldan ödenen zorunlu pay kendi dallarına aittir.","branch_kind":"mixed_non_bare","branch_ref":"root_000637/B002","candidate_links":[{"candidate_id":"cand_da740048d4da35cf4392","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَزَكَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:4:1","qac_word_ref":"87:14:4","surface_ar":"تَزَكَّىٰ"}],"gloss":"ahlaken arınıp düzgünleşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, ahlaki veya manevi bakımdan temiz ve düzgün durumda olmaktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin bu niteliği taşıması, doğru davranan ve kötülükten sakınan biri olmasıyla belirginleşir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Anlam, bir kişiyi veya iç dünyayı arındırıp düzeltme ve iyiliklerle geliştirme eylemine uzanır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yiyecek için kullanıldığında dinen izin verilen, iyi ve sonradan zarar doğurmayan seçeneği belirtir."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Maldan verilen zorunlu payın temizleyici sayılması, bu ahlaki temizlik alanıyla kurulan açıklayıcı bir bağlantıdır."}}],"root_ar":"ز ك و","root_id":"root_000637","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin veya iç durumun kusurdan uzaklaşıp temiz, doğru ve sakınan bir niteliğe kavuşmasını anlatan temel karşılıktır.","boundary_detail":"Bu dal ahlaki ve manevi temizlik ile düzgünlüğü kapsar; yalın büyüme ve maldan ödenen zorunlu pay kendi dallarına aittir.","branch_image_ar":"الطهارة والصلاح","concept_gloss":"ahlaken arınıp düzgünleşme","contextual_glosses":[{"applicability":"Bir kişiyi veya onun iç dünyasını temizleyip ahlaken daha iyi duruma getirme eyleminde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Arındırma ile doğru duruma getirme eylemlerini birlikte korur."},"facet_ids":["F003"],"text":"arındırıp düzeltmek","usage_role":"contextual"},{"applicability":"Yiyecek seçiminin izin verilir ve sonradan zarar vermeyecek nitelikte olduğunu anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yiyeceğin izin verilir oluşunu ve iyi sonucunu birlikte korur."},"facet_ids":["F004"],"text":"dinen uygun ve sonu iyi","usage_role":"contextual"}],"definition":"Bir kişinin veya iç durumun kusurdan arınıp ahlaken temiz, doğru ve sakınan bir niteliğe kavuşması ya da bir başkasının onu bu duruma getirmesidir. Yiyecek bağlamında dinen izin verilen ve sonu zarar getirmeyen olmayı da anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, ahlaki veya manevi bakımdan temiz ve düzgün durumda olmaktır."},{"facet_id":"F002","role":"specialization","statement":"Bir kişinin bu niteliği taşıması, doğru davranan ve kötülükten sakınan biri olmasıyla belirginleşir."},{"facet_id":"F003","role":"extension","statement":"Anlam, bir kişiyi veya iç dünyayı arındırıp düzeltme ve iyiliklerle geliştirme eylemine uzanır."},{"facet_id":"F004","role":"specialization","statement":"Yiyecek için kullanıldığında dinen izin verilen, iyi ve sonradan zarar doğurmayan seçeneği belirtir."},{"facet_id":"F005","role":"associated_use","statement":"Maldan verilen zorunlu payın temizleyici sayılması, bu ahlaki temizlik alanıyla kurulan açıklayıcı bir bağlantıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ahlaki düzgünlük, sakınma ve birini daha iyi duruma getirme yönlerini eksiltir.","preserves":"Kusurdan uzak olma yönünü korur."},"text":"yalnızca temizlik"}],"identity_rationale":"Kaynak ifadesi temizlik, düzgünlük ve sakınmayı aynı ahlaki çekirdekte birleştirir; birini düzeltip arındırma, iç temizliği ve dinen uygun olup kötü sonuç doğurmayan yiyecek bu çekirdeğin bağlama bağlı açılımlarıdır. Mali payın temizleyici sayılması burada yalnız anlam ilişkisini açıklar; mali uygulamanın kendisi ayrı dalda tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"arınmak ve düzgünleşmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"temiz, doğru ve kötülükten sakınan"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"arındırıp düzeltmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"arındırma, düzeltme ve iyiliklerle geliştirme"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"iç temizliği ve ahlaki düzgünlük"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kendini övmek veya sözle temiz saymak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"dinen uygun ve sonu zarar vermeyen yiyecek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"temizlik ve düzgünlük"}],"lexicalization_note":"Yalın temizlik ve düzgünlük anlamı; kişiyi düzeltme, iç dünya, kendini övme ve yiyeceğin uygunluğu gibi yapıya bağlı kullanımlarla karıştırılmadan sunulur.","neighbor_coverage_note":"Sunulan on bir adayın tamamı değerlendirildi; ahlaki temizlik ve düzgünlük sınırını en iyi açıklayan beş aday seçildi, doğruluk, sakınma, kir, büyüme, uygunluk ve tek-çift alanındaki daha uzak adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sınırı ahlaki doğruluk ve bağlama bağlı uygunluktur; komşu dalın sınırı ise daha genel arıtma, uzak tutma ve kutsama alanına yayılır.","focus_only":"Odak dal, ahlaki düzgünlüğü, sakınan kişiyi ve yiyeceğin dinen uygun sonucunu da kapsar.","gloss":"ahlaki arınma ile genel arıtma","neighbor_only":"Komşu dal, arıtma yanında yüceltme, kutsama ve bunlara bağlı iyiliği daha geniş biçimde kapsar.","neighbor_ref":"root_001206/B001","relation_type":"near_synonym","shared_zone":"İki dal da kirden veya kusurdan uzaklaştırıp temiz duruma getirme fikrinde birleşir."},{"boundary_match":"partial","distinction":"Odak dal kişilik ve davranış değerini belirler; komşu dal ise bir karışımı, kiri veya bulanıklığı gidererek saflaştırma sürecini öne çıkarır.","focus_only":"Odak dal, ahlaki düzgünlük ve kötülükten sakınma niteliğini içerir.","gloss":"ahlaki arınma ile arıtma","neighbor_only":"Komşu dal, karışmış veya kirlenmiş bir şeyi süzüp arı ve duru hale getirme işlemini içerir.","neighbor_ref":"root_000430/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal, istenmeyen bir unsurdan kurtulup temiz hale gelmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal ahlaki arınma ve düzgünlüğe bağlıdır; komşu dal ise duyu, gönül ve din ölçülerindeki her türlü iyi ve hoş niteliğe uzanır.","focus_only":"Odak dal, arınıp ahlaken düzgünleşme sürecini ve bu niteliği özellikle öne çıkarır.","gloss":"arınmışlık ile iyi ve temiz olma","neighbor_only":"Komşu dal, duyusal hoşluk, temiz oluş, yararlılık ve dinen izin verilirlik gibi çok daha geniş bir iyi olma alanını kapsar.","neighbor_ref":"root_000961/B001","relation_type":"near_synonym","shared_zone":"İki dal, temiz, doğru ve dinen uygun sayılan şeylerde örtüşür."},{"boundary_match":"opposed","distinction":"Odak olumlu arınma ve doğruluk kutbunu, komşu ise bozulma ve kötülük kutbunu gösterir; odaktaki arındırma süreci komşuda bulunmaz.","focus_only":"Odak dal, arınmış, doğru ve sakınan olmayı veya bu duruma gelmeyi bildirir.","gloss":"düzgünlük ile bozukluk","neighbor_only":"Komşu dal, bozulmuş, kötü ve düzgünlüğün karşıtı olan durumu bildirir.","neighbor_ref":"root_000944/B005","relation_type":"polarity_pair","shared_zone":"İki dal ahlaki veya niteliksel düzgünlük ekseninin karşı kutuplarında yer alır."},{"boundary_match":"partial","distinction":"Odak dal kişinin temiz ve düzgün niteliğine veya arındırılmasına yönelir; komşu dal ise yapılan iyi işlerin ve bağlılığın geniş kapsamına yönelir.","focus_only":"Odak dal, iç temizliği ve kusurdan arınarak düzgün duruma gelmeyi öne çıkarır.","gloss":"arınmışlık ile iyilik","neighbor_only":"Komşu dal, inanç ve davranış alanındaki iyilik ve görevleri geniş bir eylem alanı olarak kapsar.","neighbor_ref":"root_000104/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal doğru davranış, sakınma ve ahlaki iyilik alanında buluşur."}],"source_phrase_ar":"الطهارة زكاة المال؛ زكاة لأنها طهارة (maqayis)؛ والزكاة الصلاح؛ رجل زكي تقي (ayn)؛ معناه صلاحا؛ ما صلح؛ أي يصلح (tahdhib)؛ بزكاء النفس وطهارتها؛ حلالا لا يستوخم عقباه (mufradat)","source_summary":"Ortak anlatım temizlik ve düzgünlüğü, kişinin sakınan niteliğini, birini düzeltip arındırmayı ve iç temizliğini birleştirir; yiyeceğin dinen uygun ve sonucu iyi olması da bağlama bağlı bir açılımdır.","sources":["MQ","AY","TA","MU"],"what_is_ar":"يدخل فيه التطهير والتزكية والصلاح والتقوى وزكاء النفس أو الشخص، ومنه الطعام الأزكى بمعنى الحلال الطيب العاقبة.","what_is_not_ar":"لا يدخل فيه مجرد الزيادة الحسية في الزرع والمال إلا إذا جعلتها المصادر وجها للتزكية، ولا يدخل فيه الشفع والزوج."},"support_links":["sup_c79ffcf871a54dc34c28"]},{"boundary":"Bu dal maldan çıkarılan payı ve verme eylemini kapsar; genel arınma, büyüme veya başka tür bir yükümlülük bu sınırı tek başına karşılamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000637/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَزَكَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:4:1","qac_word_ref":"87:14:4","surface_ar":"تَزَكَّىٰ"}],"gloss":"yoksula verilmesi gereken mal payı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, maldan yoksullara ayrılan ve dinen onların hakkı sayılan paydır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlam, mal için gereken payı çıkarıp hak sahiplerine ödeme eylemini de kapsar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Maldan karşılıksız yardımda bulunmak, zorunlu payla aynı verme alanında yer alan daha genel bir kullanımdır."}}],"root_ar":"ز ك و","root_id":"root_000637","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maldan dinen hak sahibi yoksullara ayrılan payın kendisini ve bu paya dayalı mali yükümlülüğü anlatır.","boundary_detail":"Bu dal maldan çıkarılan payı ve verme eylemini kapsar; genel arınma, büyüme veya başka tür bir yükümlülük bu sınırı tek başına karşılamaz.","branch_image_ar":"زكاة المال والصدقة","concept_gloss":"yoksula verilmesi gereken mal payı","contextual_glosses":[{"applicability":"Bir kişinin malı için ayrılması gereken payı hak sahiplerine ödediği eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gerekli payı maldan çıkarma ve hak sahibine verme eylemini korur."},"facet_ids":["F002"],"text":"gereken mal payını vermek","usage_role":"contextual"},{"applicability":"Zorunlu payın özel sınırı belirtilmeden, kişinin malıyla karşılıksız yardım etmesi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Maldan başkasına karşılıksız verme eylemini korur."},"facet_ids":["F003"],"text":"malından karşılıksız vermek","usage_role":"contextual"}],"definition":"Bir kişinin malından, dinen hak sahibi sayılan yoksullara vermesi gereken pay ve bu payı mal adına çıkarıp ödeme eylemidir. Aynı alan, maldan karşılıksız yardımda bulunma eylemini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, maldan yoksullara ayrılan ve dinen onların hakkı sayılan paydır."},{"facet_id":"F002","role":"extension","statement":"Anlam, mal için gereken payı çıkarıp hak sahiplerine ödeme eylemini de kapsar."},{"facet_id":"F003","role":"associated_use","statement":"Maldan karşılıksız yardımda bulunmak, zorunlu payla aynı verme alanında yer alan daha genel bir kullanımdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Dinen belirlenmiş payın dışında kalan her türlü isteğe bağlı yardımı ana anlama katar.","collision":"Zorunlu mal payı ile isteğe bağlı yardım arasındaki sınırı belirsizleştirir.","fit":"broadening","loses":null,"preserves":"Karşılıksız mal verme yönünü korur."},"text":"genel bağış"}],"identity_rationale":"Kaynak ifadesi, maldan yoksullara verilmesi dinen hak sayılan payı, bu payı ödeme eylemini ve karşılıksız mal vermeyi aynı mali yardım alanında toplar. Dal bu nedenle salt ahlaki temizlik olarak değil, malın belirli bir bölümünü hak sahibine çıkarma ve verme uygulaması olarak tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yoksullara verilmesi gereken mal payı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"malının gereken payını ödemek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"malından karşılıksız vermek"}],"lexicalization_note":"Mali payı adlandıran biçim, payı ödeme yapısı ve karşılıksız verme eylemi ayrı gerçekleşmeler olarak korunur; anlam genel yardım veya genel arınma diye genişletilmez.","neighbor_coverage_note":"Sunulan on adayın tamamı değerlendirildi; mali payın yardım, arınma, bedel ve yükümlülük alanlarından ayrımını gösteren dört aday seçildi, akıl eksikliği, sapma, iç körlük, büyüme, uygunluk ve tek-çift adayları anlamsal sınırı keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirlenmiş pay ve onun ödenmesiyle sınırlıdır; komşu dal isteğe bağlı yardım, haktan vazgeçme ve tahsil görevi gibi ek katılımcı ve işlemlere uzanır.","focus_only":"Odak dal, yoksullara verilmesi gereken belirli mal payını ve bu payı ödeme eylemini öne çıkarır.","gloss":"zorunlu pay ile mali yardım","neighbor_only":"Komşu dal, karşılıksız verilen malı, bir haktan vazgeçmeyi ve yardım payını alan görevliyi daha geniş biçimde kapsar.","neighbor_ref":"root_000852/B006","relation_type":"near_synonym","shared_zone":"İki dal da maldan hak sahibine karşılıksız aktarım ve belirli mali hak alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal somut bir mali hak ve aktarım uygulamasıdır; komşu dal ise ahlaki veya manevi bir nitelik ve dönüşümdür.","focus_only":"Odak dal, maldan yoksullara aktarılan payı ve ödeme eylemini bildirir.","gloss":"mali pay ile arınma","neighbor_only":"Komşu dal, kişinin ahlaken arınmış ve düzgün niteliğini veya bu duruma getirilmesini bildirir.","neighbor_ref":"root_000637/B002","relation_type":"near_neighbor","shared_zone":"Mali payın temizleyici sayılması iki dal arasında açıklayıcı bir bağ kurar."},{"boundary_match":"field_only","distinction":"Odakta alıcı yoksul ve verilen şey onun hakkı olan mal payıdır; komşuda verilen şey bir kişi veya yükümlülük yerine geçen kurtarma ya da karşılama bedelidir.","focus_only":"Odak dal, yoksulların hakkı sayılan mal payını düzenli bir mali yükümlülük olarak verir.","gloss":"hak payı ile kurtarma bedeli","neighbor_only":"Komşu dal, bir kişiyi kurtarmak, bir zararı gidermek veya bir ibadet borcunu karşılamak için mal ya da canı bedel kılar.","neighbor_ref":"root_001136/B001","relation_type":"same_field","shared_zone":"İki dal da dini veya ahlaki bir gerekçeyle değerli bir şeyi elden çıkarma alanındadır."},{"boundary_match":"thematic_only","distinction":"Odak, yükümlülüğün konusu olan mal payının verilmesini tanımlar; komşu ise yükümlülüğü kişinin üzerine koyma işlemini, ödeme şartı olmadan tanımlar.","focus_only":"Odak dal, belirli bir mal payını hak sahibine fiilen aktarmayı içerir.","gloss":"mali yükümlülük ile görevlendirme","neighbor_only":"Komşu dal, herhangi bir işi, görevi veya inancı bir kişinin sorumluluğuna yüklemeyi içerir.","neighbor_ref":"root_001249/B004","relation_type":"thematic","shared_zone":"Her iki dal kişiye bağlanan bir yükümlülük düşüncesinde aynı senaryoya katılır."}],"source_phrase_ar":"زكاة المال (maqayis;ayn;sihah;tahdhib)؛ زكى ماله تزكية أي أدى عنه زكاته؛ وتزكى أي تصدق (sihah)؛ ما يخرج الإنسان من حق الله تعالى إلى الفقراء (mufradat)","source_summary":"Kaynaklar maldan ayrılan bilinen payı ortak biçimde tanır; payın mal adına ödenmesi, yoksullara aktarılması ve karşılıksız mal verme eylemi aynı anlatımda bir araya gelir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه زكاة المال المعروفة وأداء الزكاة والتصدق وما يخرج من حق الله تعالى إلى الفقراء، مع تعليلها بالتطهير أو النماء أو البركة.","what_is_not_ar":"لا يدخل فيه كل صلاح أو طهارة مجردة إلا إذا كان الكلام على الزكاة المالية أو عملها."},"support_links":[]},{"boundary":"Anlam, bir işin kişiye yakışmadığını veya durumuna uygun düşmediğini bildiren yapıyla sınırlıdır; genel uyum alanına taşınmaz.","branch_kind":"collocation","branch_ref":"root_000637/B004","candidate_links":[{"candidate_id":"cand_c7e2315d1d3d5821759d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَزَكَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:4:1","qac_word_ref":"87:14:4","surface_ar":"تَزَكَّىٰ"}],"gloss":"yakışmamak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş veya durum, değerlendirilen kişiye yakışmaz ve onun haliyle bağdaşmaz."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Değerlendirme kaynakta olumsuz yapı içinde verilir ve genel uygunluk bildiren bağımsız bir anlama genişletilmez."}}],"root_ar":"ز ك و","root_id":"root_000637","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin veya durumun belirli bir kişiye uygun olmadığını ve onun konumuyla bağdaşmadığını anlatan yapı için kullanılır.","boundary_detail":"Anlam, bir işin kişiye yakışmadığını veya durumuna uygun düşmediğini bildiren yapıyla sınırlıdır; genel uyum alanına taşınmaz.","branch_image_ar":"الملاءمة واللياقة","concept_gloss":"yakışmamak","contextual_glosses":[{"applicability":"Bir davranışın veya işin kişinin hali, konumu ya da niteliğiyle bağdaşmadığı söylenirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli kişiye göre kurulan uygunsuzluk ve bağdaşmazlık yargısını korur."},"facet_ids":["F001","F002"],"text":"ona uygun düşmemek","usage_role":"contextual"}],"definition":"Belirli bir işin, davranışın veya durumun bir kişiye yakışmadığını ve onun konumuna ya da haline uygun düşmediğini bildiren kalıplaşmış bir değerlendirmedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş veya durum, değerlendirilen kişiye yakışmaz ve onun haliyle bağdaşmaz."},{"facet_id":"F002","role":"specialization","statement":"Değerlendirme kaynakta olumsuz yapı içinde verilir ve genel uygunluk bildiren bağımsız bir anlama genişletilmez."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İki tarafın zaman içinde birbirine ayak uydurması anlamını ekler.","collision":"Karşılıklı uyum süreciyle karışır.","fit":"displacement","loses":"Belirli bir işin kişiye yakışmadığını bildiren olumsuz değerlendirmeyi ortadan kaldırır.","preserves":"Uygunluk alanıyla olan genel ilişkiyi korur."},"text":"uyum sağlamak"}],"identity_rationale":"Kaynak ifadesi uygunluk alanını doğrular, ancak tanıklıklar bunu özellikle bir işin veya durumun kişiye uygun düşmediğini söyleyen olumsuz yapıda verir. Bu nedenle dal korunabilir, fakat genel ve bağımsız bir uygunluk anlamına genişletilmeden söz konusu yapı içinde tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ona yakışmamak veya durumuna uygun düşmemek"}],"lexicalization_note":"Tanım yalnız kaynakta verilen olumsuz uygunluk yapısına bağlıdır; kökün tek başına her türlü uygunluk veya uyum bildirdiği varsayılmaz.","neighbor_coverage_note":"Sunulan on bir adayın tamamı değerlendirildi; uygunluk sınırını doğrudan aydınlatan dört aday seçildi, kınama, kusuru görmezden gelme, ayıplama, kötüleme, büyüme, arınma ve tek-çift alanları yalnız uzak çağrışım taşıdığı için yayıma alınmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal olumsuz ve yapıya bağlı bir yargıdır; komşu dal olumlu ya da olumsuz değerlendirilebilen daha genel yakışma alanına sahiptir.","focus_only":"Odak dal, kaynakta yalnız bir işin kişiye yakışmadığını bildiren belirli olumsuz yapıyla sınırlıdır.","gloss":"yakışmamak ile yakışmak","neighbor_only":"Komşu dal, bir şeyin kişiye uygun veya güzel düşmesi alanını daha genel biçimde kapsar.","neighbor_ref":"root_001391/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir iş veya şey ile kişi arasındaki yakışma ve uygunluk yargısını anlatır."},{"boundary_match":"partial","distinction":"Odak dal yalnız uygunsuzluk hükmü verir; komşu dal ise kişinin ihtiyacına veya durumuna uygunluğu genel bir ilişki olarak kurar.","focus_only":"Odak dal, bir işin kişiye yakışmadığını belirten olumsuz değerlendirmeyi taşır.","gloss":"yakışmama ile uygun olma","neighbor_only":"Komşu dal, bir şeyin kişi için işe yarar ve uygun olmasını olumlu yönden de bildirebilir.","neighbor_ref":"root_000876/B003","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyin kişiye uygun düşüp düşmediğini değerlendirir."},{"boundary_match":"partial","distinction":"Odakta ilişki bir iş ile kişi arasında ve değerlendirme yönlüdür; komşuda iki tarafın karşılıklı uygunluğu veya görüş birliği belirleyicidir.","focus_only":"Odak dal, bir işin kişinin haline yakışıp yakışmadığına ilişkin değer yargısı taşır.","gloss":"yakışma ile karşılıklı uyum","neighbor_only":"Komşu dal, iki şeyin veya görüşün aynı yönde buluşmasını ve karşılıklı uyuşmasını anlatır.","neighbor_ref":"root_001668/B001","relation_type":"near_neighbor","shared_zone":"İki dal, iki unsur arasında bağdaşma bulunup bulunmadığını sorgular."},{"boundary_match":"partial","distinction":"Odak kişiye yakışma ölçütüne bağlıdır; komşu ise yapılması doğru olanı veya ulaşılabilir sonucu değerlendiren daha geniş bir alan taşır.","focus_only":"Odak dal, bir davranışın kişiye yakışmaması ve haliyle bağdaşmaması yargısını verir.","gloss":"yakışmama ile doğru bulma","neighbor_only":"Komşu dal, bir işi yapmanın doğru veya beklenebilir olup olmadığını ve istenen sonuca erişmeyi kapsar.","neighbor_ref":"root_001572/B003","relation_type":"near_neighbor","shared_zone":"İki dal, bir davranışın kişi bakımından yerinde olup olmadığını değerlendirebilir."}],"source_phrase_ar":"أمر لا يزكو بفلان أي لا يليق به (maqayis;sihah)؛ وهذا الأمر لا يزكو أي لا يليق (ayn)؛ هذا الأمر لا يزكو بفلان أي لا يليق به (tahdhib)","source_summary":"Kaynakların ortak anlatımı, bir işin veya durumun belirli bir kişiye yakışmadığını ve onun haline uygun düşmediğini bildiren olumsuz değerlendirmede birleşir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه قولهم لا يزكو بفلان أي لا يليق به أو لا يناسب حاله.","what_is_not_ar":"لا يدخل فيه زكاء المال أو النفس ولا معنى الزوج والشفع."},"support_links":["sup_57360a114f6de622f5da"]},{"boundary":"Bu dal çift ve tek karşıtlığıyla sınırlıdır; büyüme, arınma, mali pay ve uygunluk anlamlarıyla birleştirilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000637/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَزَكَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:4:1","qac_word_ref":"87:14:4","surface_ar":"تَزَكَّىٰ"}],"gloss":"çift olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, tek olanın karşıtı olarak çift veya iki öğeli olma durumudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sabit karşılaştırma sözünde tek ve çift seçenekleri birbirine karşı konur."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Avuçta saklanan bir şeyin tek mi çift mi olduğunu sorma ve tahmin etme, karşıtlığın oyun içindeki kullanımıdır."}}],"root_ar":"ز ك و","root_id":"root_000637","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin tek değil, iki öğeli veya çift sayıda olduğunu bildiren genel karşılıktır.","boundary_detail":"Bu dal çift ve tek karşıtlığıyla sınırlıdır; büyüme, arınma, mali pay ve uygunluk anlamlarıyla birleştirilmez.","branch_image_ar":"الزوج والشفع","concept_gloss":"çift olma","contextual_glosses":[{"applicability":"İki seçeneği karşılaştıran sözde veya avuçta saklanan şeyin sayısını tahmin etme oyununda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tek ile çift arasındaki karşıtlığı ve soru işlevini korur."},"facet_ids":["F002","F003"],"text":"tek mi çift mi","usage_role":"contextual"}],"definition":"Bir şeyin tek değil, iki öğeli veya çift sayıda olduğunu bildiren anlamdır. Tek-çift karşıtlığını kuran sözlerde ve avuçta saklanan bir şeyin tek mi çift mi olduğunu tahmin etme oyununda özel olarak kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, tek olanın karşıtı olarak çift veya iki öğeli olma durumudur."},{"facet_id":"F002","role":"specialization","statement":"Sabit karşılaştırma sözünde tek ve çift seçenekleri birbirine karşı konur."},{"facet_id":"F003","role":"associated_use","statement":"Avuçta saklanan bir şeyin tek mi çift mi olduğunu sorma ve tahmin etme, karşıtlığın oyun içindeki kullanımıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Birbirine denk olma, benzerlik veya evlilikteki taraf anlamlarını gereksiz yere ekler.","collision":"Sayısal çiftlik ile denk veya evli taraf anlamları birbirine karışır.","fit":"broadening","loses":null,"preserves":"İki öğenin birlikte düşünülmesi yönünü kısmen korur."},"text":"eş"}],"identity_rationale":"Kaynak ifadesi sözcüğü çift veya iki öğeden oluşan taraf için açıkça tanımlar ve onu tek olanın karşısına koyar. Avuçta saklanan şey üzerine sorulan tek-çift sorusu ile buna eşlik eden söyleyiş, aynı karşıtlığın oyun ve tahmin bağlamındaki özel kullanımlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"çift veya iki öğeli"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"tek veya çift"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"avuçtaki çift mi tek mi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"avuçtaki şey için tek-çift söylemek"}],"lexicalization_note":"Çift olmayı adlandıran biçim ile tek-çift karşıtlığını kuran sözler ve avuçtaki şey üzerine söylenen oyun yapıları ayrı kapsamlarıyla korunur.","neighbor_coverage_note":"Sunulan on bir adayın tamamı değerlendirildi; çiftlik sınırını iki oluşturma, eşleşmiş ikili, iki öğeyi kapsama ve özel ikili adlarından ayıran dört aday seçildi, çift organlar, varsayım, on sayısına tamamlama, tahmin, büyüme, arınma ve uygunluk alanları dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sayısal tek-çift karşıtlığına açıktır; komşu dal ise benzer, karşıt veya tamamlayıcı iki öğenin birbirine eşlik etmesini öne çıkarır.","focus_only":"Odak dal, tek sayının karşıtı olan çiftliği ve tek-çift tahmin sözünü kapsar.","gloss":"çift sayı ile eşleşmiş ikili","neighbor_only":"Komşu dal, birbirine bağlanan iki öğenin her birini veya birlikte oluşturdukları karşılıklı çifti kapsar.","neighbor_ref":"root_000652/B001","relation_type":"near_synonym","shared_zone":"İki dal da tek olmayan, iki öğeli bir bütün veya çift fikrinde örtüşür."},{"boundary_match":"partial","distinction":"Odak bir sınıflandırma ve durumdur; komşu ise bir öğeye ikincisini katıp iki oluşturma sürecidir.","focus_only":"Odak dal, ortaya çıkmış çiftlik durumunu ve bunun tek olanla karşıtlığını adlandırır.","gloss":"çift olma ile ikiye çıkarma","neighbor_only":"Komşu dal, bire bir ekleyerek iki oluşturma, ikinci olma veya bir şeyi ikileme işlemini anlatır.","neighbor_ref":"root_000208/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal iki öğe ve iki sayısı çevresinde buluşur."},{"boundary_match":"field_only","distinction":"Odak dal çift olma niteliğini verir; komşu dal ise adı anılan iki öğeyi eksiksiz kapsayan dil bilgisel araçları konu edinir.","focus_only":"Odak dal, tek olanın karşıtı olarak çiftliği ve tahmin oyunundaki seçeneği bildirir.","gloss":"çiftlik ile ikisini birden kapsama","neighbor_only":"Komşu dal, iki varlığın ikisini birden kapsayan dil bilgisel ifadeleri ve onların kullanım kurallarını bildirir.","neighbor_ref":"root_001317/B007","relation_type":"same_field","shared_zone":"İki dal da tam olarak iki öğenin birlikte düşünülmesi alanındadır."},{"boundary_match":"field_only","distinction":"Odak genel ve sayısal bir sınıftır; komşu ise su ile yiyecek veya iki zaman dilimi gibi önceden belirlenmiş ikililerin özel adlandırılmasıdır.","focus_only":"Odak dal, herhangi bir şeyin çift veya çift sayıda olmasını genel biçimde bildirir.","gloss":"genel çiftlik ile adlandırılmış ikililer","neighbor_only":"Komşu dal, kültürel kullanımda birlikte anılan belirli ikililere verilen ortak bir adı kapsar.","neighbor_ref":"root_000168/B008","relation_type":"same_field","shared_zone":"Her iki dal iki öğenin tek bir ikili olarak anılması alanına girer."}],"source_phrase_ar":"الزكا الزوج وهو الشفع (maqayis)؛ وزكا الشفع يقال خسا أو زكا (sihah)؛ العرب تقول للفرد خسا وللزوجين اثنين زكا؛ هو يخسي ويزكي إذا قبض على شيء في كفه وقال أزكا أم خسا (tahdhib)","source_summary":"Kaynakların ortak anlatımı çift veya iki öğeli olmayı tek olanın karşısına koyar; tek-çift sözü ve avuçtaki şey üzerine yapılan tahmin bu karşıtlığın özel kullanımlarıdır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه زكا بمعنى الزوج أو الشفع، في مقابلة خسا للفرد، وألفاظ اللعب أو القبض على الشيء في الكف: أزكا أم خسا.","what_is_not_ar":"لا يدخل فيه النمو والطهارة والزكاة المالية."},"support_links":[]},{"boundary":"Dal genel yarma ve kesme işlemini kapsar; toprağı işleme ve demiri demirle kesme bunun bağlama bağlı gerçekleşimleridir.","branch_kind":"mixed_non_bare","branch_ref":"root_001175/B001","candidate_links":[{"candidate_id":"cand_c7e2315d1d3d5821759d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَفْلَحَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>afolaHa|ROOT:flH|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:2:1","qac_word_ref":"87:14:2","surface_ar":"أَفْلَحَ"}],"gloss":"yarmak veya kesip ayırmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi yararak açıklık oluşturmak veya keserek parçalarını ayırmak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toprağı ekim amacıyla yarıp işlenebilir hale getirmek."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir demir parçasını başka bir demirle yarmak veya kesmek."}}],"root_ar":"ف ل ح","root_id":"root_001175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnede yarık açma ya da onu keserek ayırma işleminin genel ve bağlamdan bağımsız karşılığıdır.","boundary_detail":"Dal genel yarma ve kesme işlemini kapsar; toprağı işleme ve demiri demirle kesme bunun bağlama bağlı gerçekleşimleridir.","branch_image_ar":"شق الشيء وقطعه","concept_gloss":"yarmak veya kesip ayırmak","contextual_glosses":[{"applicability":"İşlemin tarla veya toprak üzerinde ekime hazırlık amacıyla yapıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Toprağı yarma işlemini ve ekim amacını birlikte korur."},"facet_ids":["F002"],"text":"toprağı ekim için yarmak","usage_role":"contextual"},{"applicability":"Bir demir aracın ya da parçanın başka bir demiri yardığı veya kestiği bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Malzemeyi, aracı ve yarma ya da kesme sonucunu korur."},"facet_ids":["F003"],"text":"demiri demirle yarmak veya kesmek","usage_role":"contextual"}],"definition":"Bir şeyi yararak açıklık oluşturmak veya keserek parçalarını birbirinden ayırmak; bu işlem toprağın ekim için ya da demirin başka bir demirle yarılmasında gerçekleşebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi yararak açıklık oluşturmak veya keserek parçalarını ayırmak."},{"facet_id":"F002","role":"specialization","statement":"Toprağı ekim amacıyla yarıp işlenebilir hale getirmek."},{"facet_id":"F003","role":"specialization","statement":"Bir demir parçasını başka bir demirle yarmak veya kesmek."}],"identity_rationale":"Kaynak ifadesi, anlamın merkezine bir şeyi yarmayı veya keserek ayırmayı koyuyor; toprağın ve demirin yarılması bu işlemin belirgin uygulamalarıdır. Bu nedenle dal kimliği kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi yarmak veya kesmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"toprağı sürmek üzere yarmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"toprağı sürmek üzere yarmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"demiri başka bir demirle yarmak veya kesmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir uzuvdaki yarıklar"}],"lexicalization_note":"Tanım genel yarma ve kesme çekirdeğini korur; toprak ve demirle ilgili kullanımları yalnız kendi yapıları içinde ayrıca belirtir.","neighbor_coverage_note":"Verilen bütün komşular incelendi; yayımlanan üç karşılaştırma, yarma çekirdeğinin en yakın işlem ve sonuç sınırlarını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal açma ve genişletme sonucuna yönelirken bu dal yarma ile keserek ayırmayı aynı çekirdekte tutar ve toprak ile demir uygulamalarını içerir.","focus_only":"Keserek ayırmayı ve toprağın ya da demirin yarılmasını da kapsar.","gloss":"bir şeyi yarmak ve açmak","neighbor_only":"Açmayı ve genişletmeyi, ayrıca karın yarılması gibi özel olayları kapsar.","neighbor_ref":"root_000139/B002","relation_type":"near_synonym","shared_zone":"Her iki dalın merkezinde somut bir nesneyi yararak açma işlemi vardır."},{"boundary_match":"partial","distinction":"Komşu dalın eğme yönü bu dalda yoktur; bu dalın çekirdeği yarma ve keserek ayırma ile sınırlıdır.","focus_only":"Toprağı ekim için yarma gibi belirgin uygulamaları vardır.","gloss":"yarmak, kesmek veya eğmek","neighbor_only":"Bir şeyi eğme ve boyunları bükme anlamlarını da taşır.","neighbor_ref":"root_000897/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi yarma veya kesme işlemini ifade edebilir."},{"boundary_match":"partial","distinction":"Bu dal yarığı meydana getiren genel işlemdir; komşu dal ise belirli bir vücut bölümündeki kalıcı yarık durumudur.","focus_only":"Bir nesne üzerinde gerçekleştirilen yarma veya kesme eylemini bildirir.","gloss":"dudaktaki yarık","neighbor_only":"Dudakta, özellikle alt dudakta bulunan yarığı ve bu özelliği taşıyan kişiyi bildirir.","neighbor_ref":"root_001175/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da somut bir yarık kavramı bulunur."}],"source_phrase_ar":"أصل يدل على شق (maqayis)؛ فلحت الأرض شققتها (maqayis;sihah;tahdhib)؛ فلحت الشيء إذا شققته أو قطعته (jamhara)؛ الحديد بالحديد يفلح أي يشق أو يقطع (maqayis;ayn;jamhara;sihah;tahdhib;mufradat)","source_summary":"Kaynaklar, temel işlemi yarma ve kesme olarak ortaklaştırır; toprağın ekim için yarılması ile demirin demirle kesilmesi bu çekirdeğin uygulamalarıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"شق الأرض أو الشيء أو الحديد وقطعه أو فتحه من مضيق","what_is_not_ar":"ليس شق الشفة اسما للصفة؛ وليس الفوز والبقاء؛ وليس السحور"},"support_links":["sup_57360a114f6de622f5da"]},{"boundary":"Anlam herhangi bir yarık değil, dudakta bulunan ve niteleyici biçimlerde özellikle alt dudakla ilişkilendirilen yarıktır.","branch_kind":"bare","branch_ref":"root_001175/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَفْلَحَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>afolaHa|ROOT:flH|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:2:1","qac_word_ref":"87:14:2","surface_ar":"أَفْلَحَ"}],"gloss":"dudakta, özellikle alt dudakta yarık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dudakta bulunan belirgin bir yarık."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özellikle alt dudağı yarık olan kişiyi bu özelliğiyle nitelemek."}}],"root_ar":"ف ل ح","root_id":"root_001175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yarığın kendisini ve alt dudağı yarık olma durumunu birlikte temsil eden genel karşılıktır.","boundary_detail":"Anlam herhangi bir yarık değil, dudakta bulunan ve niteleyici biçimlerde özellikle alt dudakla ilişkilendirilen yarıktır.","branch_image_ar":"فلحة الشفة","concept_gloss":"dudakta, özellikle alt dudakta yarık","contextual_glosses":[{"applicability":"Bir kişiyi dudak yapısındaki yarıkla niteleyen sıfat görevli kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişideki özelliği ve alt dudak konumunu açıkça korur."},"facet_ids":["F002"],"text":"alt dudağı yarık","usage_role":"contextual"}],"definition":"Dudakta bulunan yarık ve bu yarığı taşıma durumu; kişiyi niteleyen kullanımlarda yarık özellikle alt dudaktadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dudakta bulunan belirgin bir yarık."},{"facet_id":"F002","role":"specialization","statement":"Özellikle alt dudağı yarık olan kişiyi bu özelliğiyle nitelemek."}],"identity_rationale":"Kaynak ifadesi hem dudaktaki yarığı hem de özellikle alt dudağı yarık olan kişiye ilişkin nitelemeleri açıkça verir. Dalın dudak yarığı olarak kurulması bu kanıtı doğrudan karşılar.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"dudaktaki yarık"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"alt dudağı yarık olan erkek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dudağında yarık bulunan kadın"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"dudaktaki yarığın kendisi"}],"lexicalization_note":"Tanım, bağımsız dudak yarığı anlamıyla sınırlıdır ve genel yarma eylemini ya da başka vücut bölümlerindeki yarıkları içine almaz.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi; üst dudak yarığı, genel yarma eylemi ve ağız çevresi eğriliği en açıklayıcı sınırları sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Temel ayrım konumdur: bu dalın niteleyici kullanımı alt dudağa ağırlık verirken komşu dal üst dudakla sınırlıdır.","focus_only":"Dudak yarığını genel olarak, nitelemelerde ise özellikle alt dudakta gösterir.","gloss":"üst dudaktaki belirgin yarık","neighbor_only":"Yarığı yalnız üst dudakta konumlandırır ve aynı sözü başka üst işaretler için de kullanır.","neighbor_ref":"root_001040/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişiyi dudaktaki belirgin yarık üzerinden niteler."},{"boundary_match":"partial","distinction":"Bu dal dudaktaki durumun adıdır; komşu dal ise nesne ve malzeme ayrımı yapmadan yarma eylemini anlatır.","focus_only":"Belirli bir vücut bölümündeki yarığı ve bu bedensel özelliği bildirir.","gloss":"yarmak veya kesip ayırmak","neighbor_only":"Bir şeyi yarmaya veya kesmeye yönelik genel eylemi bildirir.","neighbor_ref":"root_001175/B001","relation_type":"near_neighbor","shared_zone":"Yarık sonucu iki dalın ortak kavramsal alanıdır."},{"boundary_match":"field_only","distinction":"Bu dalın ayırıcı özelliği yarıktır; komşu dalda doku yarığı değil, yapının eğrilmesi veya yana kayması esastır.","focus_only":"Dudak dokusundaki gerçek bir yarığa dayanır.","gloss":"ağız veya göz yapısında eğrilik","neighbor_only":"Ağız, dudak veya gözdeki eğrilik ve yana kayma durumunu bildirir.","neighbor_ref":"root_000866/B003","relation_type":"same_field","shared_zone":"İki dal da yüz ve ağız çevresindeki doğuştan ya da kalıcı biçim özelliklerini anlatır."}],"source_phrase_ar":"الفلح الشق في الشفة (ayn;tahdhib)؛ الأفلح المشقوق الشفة السفلى (maqayis;jamhara;sihah;tahdhib)؛ امرأة فلحاء وعنترة الفلحاء لفلحة كانت به (maqayis;jamhara;sihah;tahdhib)","source_summary":"Kaynaklar dudaktaki yarık anlamında birleşir ve kişiyi niteleyen biçimlerde yerin özellikle alt dudak olduğunu belirtir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"الأفلح والفلحاء والفلحة لشق في الشفة ولا سيما السفلى","what_is_not_ar":"ليس شق الأرض والحديد؛ وليس الفلاح بمعنى الفوز أو السحور"},"support_links":[]},{"boundary":"Dal gerçek anlamdaki tarım çalışanı ile onun toprağı işleme uğraşını kapsar; benzetmeyle aynı adın verildiği taşıma çalışanını kapsamaz.","branch_kind":"bare","branch_ref":"root_001175/B003","candidate_links":[{"candidate_id":"cand_5c2dab6f77af8d8e7755","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَفْلَحَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>afolaHa|ROOT:flH|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:2:1","qac_word_ref":"87:14:2","surface_ar":"أَفْلَحَ"}],"gloss":"çiftçi ve toprağı işleme işi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Toprağı yarıp işleyerek ürün yetiştiren çiftçi."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toprağı sürme ve çiftçinin yürüttüğü tarım işi."}}],"root_ar":"ف ل ح","root_id":"root_001175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem toprağı yarıp işleyen kişiyi hem de bu kişinin tarımsal uğraşını kapsayan karşılıktır.","boundary_detail":"Dal gerçek anlamdaki tarım çalışanı ile onun toprağı işleme uğraşını kapsar; benzetmeyle aynı adın verildiği taşıma çalışanını kapsamaz.","branch_image_ar":"الأكار الشاق للأرض","concept_gloss":"çiftçi ve toprağı işleme işi","contextual_glosses":[{"applicability":"Sözün tarım işini yapan kişiyi adlandırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tarım çalışanını ve toprağı işleme niteliğini korur."},"facet_ids":["F001"],"text":"toprağı işleyen çiftçi","usage_role":"contextual"},{"applicability":"Sözün kişiyi değil, onun yaptığı tarımsal işi adlandırdığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Toprağı sürme işlemini ve mesleki uğraşı birlikte korur."},"facet_ids":["F002"],"text":"toprağı sürme ve çiftçilik","usage_role":"contextual"}],"definition":"Toprağı ekim için yarıp işleyen çiftçi ve bu kişinin yaptığı sürme, tarım ve çiftçilik işi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Toprağı yarıp işleyerek ürün yetiştiren çiftçi."},{"facet_id":"F002","role":"extension","statement":"Toprağı sürme ve çiftçinin yürüttüğü tarım işi."}],"identity_rationale":"Kaynak ifadesi, toprağı yaran tarım çalışanını ve onun yaptığı toprak işleme işini birlikte tanımlar. Dalın çiftçi ve çiftçilik çevresinde kurulması bu iki açık unsuru korur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"çiftçi, toprağı işleyen kimse"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"toprağı sürme ve çiftçilik işi"}],"lexicalization_note":"Tanım, bağımsız çiftçi ve çiftçilik anlamlarını verir; belirli bir söz dizimine ya da benzetmeli taşıma kullanımına bağlanmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; genel çiftçi, bahçe çiftçisi, tohum ekme ve yarma eylemiyle kurulan dört karşılaştırma dalın sınırlarını yeterince açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kişi anlamında büyük ölçüde örtüşseler de bu dal çiftçilik işini de kapsar; komşu dal ise topluluk adlandırmasıyla sınırlıdır.","focus_only":"Çiftçinin yaptığı toprağı sürme ve çiftçilik işini de adlandırır.","gloss":"çiftçiler topluluğu","neighbor_only":"Yalnız çiftçilerin topluluk veya çoğul adını verir.","neighbor_ref":"root_001003/B012","relation_type":"near_synonym","shared_zone":"Her iki dal toprağı işleyen çiftçileri adlandırır."},{"boundary_match":"partial","distinction":"Komşu dal çalışma yerini bağ veya bahçeyle daraltır; bu dal tarım çalışanını ve uğraşını daha genel bir kapsamda verir.","focus_only":"Tarla ve tarım alanlarında çalışan çiftçiyi ve çiftçilik işini genel olarak kapsar.","gloss":"bağ veya bahçe çiftçisi","neighbor_only":"Özellikle bağ veya bahçede çalışan tarım işçisini adlandırır.","neighbor_ref":"root_000275/B005","relation_type":"near_synonym","shared_zone":"İki dal da toprağı işleyerek ürün yetiştiren kişiyi bildirir."},{"boundary_match":"field_only","distinction":"Bu dal işi yapan kişi ile toprağı işlemeyi merkez alır; komşu dal sürecin tohum atma aşamasını merkez alır.","focus_only":"Çiftçiyi ve toprağı sürme uğraşını adlandırır.","gloss":"tohum ekmek ve ekine hazırlamak","neighbor_only":"Tohuma ve tohumu toprağa atma işlemine odaklanır.","neighbor_ref":"root_000303/B002","relation_type":"same_field","shared_zone":"Her iki dal ekim ve ürün yetiştirme sürecinin içindedir."},{"boundary_match":"partial","distinction":"Komşu dal işlemin kendisidir; bu dal o işlemin tarımdaki uygulamasından hareketle kişiyi ve mesleği adlandırır.","focus_only":"Toprağı yaran kişiyi ve bu kişinin mesleki uğraşını adlandırır.","gloss":"yarmak veya kesip ayırmak","neighbor_only":"Herhangi bir nesneyi yarma veya kesme eylemini genel olarak bildirir.","neighbor_ref":"root_001175/B001","relation_type":"near_neighbor","shared_zone":"Çiftçinin toprağı yarması iki dal arasında açık bir bağlantı kurar."}],"source_phrase_ar":"سمي الأكار فلاحا لأنه يشق الأرض (maqayis;jamhara;sihah;tahdhib;mufradat)؛ الفلاحون الزراعون (ayn)؛ الفلاحة الحراثة أو صناعة الفلاح (jamhara;sihah;tahdhib)","source_summary":"Kaynaklar çiftçiyi toprağı yarmasıyla açıklar ve aynı anlam çevresinde toprağı sürme ile çiftçilik uğraşını birlikte kaydeder.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الفلاح بمعنى الأكار أو الزارع وصناعة الفلاحة والحراثة لأنها شق الأرض للزرع","what_is_not_ar":"ليس المكاري إلا إذا سمي فلاحا تشبيها بالأكار؛ وليس مطلق الفوز"},"support_links":["sup_3b224864180081dd711e"]},{"boundary":"Buradaki kişi gerçek çiftçi değildir; adlandırma, ücretli taşıma işi yapan kişinin çalışmasının çiftçinin çalışmasına benzetilmesine dayanır.","branch_kind":"bare","branch_ref":"root_001175/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَفْلَحَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>afolaHa|ROOT:flH|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:2:1","qac_word_ref":"87:14:2","surface_ar":"أَفْلَحَ"}],"gloss":"çiftçiye benzetilen ücretli taşıyıcı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ücretli taşıma işi yapan kimsenin çiftçiye benzetilerek adlandırılması."}}],"root_ar":"ف ل ح","root_id":"root_001175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ücretle taşıma yapan kişinin çiftçi adıyla benzetmeli biçimde anıldığı kullanımı tam olarak açıklar.","boundary_detail":"Buradaki kişi gerçek çiftçi değildir; adlandırma, ücretli taşıma işi yapan kişinin çalışmasının çiftçinin çalışmasına benzetilmesine dayanır.","branch_image_ar":"المكاري المشبه بالأكار","concept_gloss":"çiftçiye benzetilen ücretli taşıyıcı","contextual_glosses":[{"applicability":"Benzetmeli adın hedefindeki gerçek mesleğin okura açıklanması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çiftçiye benzetilerek adlandırılma ilişkisini dışarıda bırakır.","preserves":"Kişinin ücret karşılığı taşıma yapan biri olduğunu korur."},"facet_ids":["F001"],"text":"ücretle yük ve yolcu taşıyan kimse","usage_role":"explanatory"}],"definition":"Ücret karşılığında taşıma işi yapan kişinin, çalışma biçimi toprağı işleyen çiftçiye benzetilerek çiftçi adıyla anılması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ücretli taşıma işi yapan kimsenin çiftçiye benzetilerek adlandırılması."}],"identity_rationale":"Kaynak ifadesi ücretle taşıma işi yapan kişiye, toprağı işleyen çiftçiye benzetildiği için çiftçi adının verildiğini açıkça belirtir. Dal bu benzetmeli adlandırmayı doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çiftçiye benzetilerek adlandırılan ücretli taşıyıcı"}],"lexicalization_note":"Tanım bağımsız bir kişi adlandırmasını karşılar, ancak bu adın gerçek tarım çalışanına değil benzetmeyle taşıma çalışanına yöneldiğini açık tutar.","neighbor_coverage_note":"Tüm adaylar incelendi; gerçek çiftçi, genel mesleki kazanç ve taşıma hayvanıyla yapılan karşılaştırmalar kişi adının benzetmeli sınırını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İki dal aynı kişi adında buluşsa da meslekleri ayrıdır: burada taşıma çalışanı, komşu dalda tarım çalışanı söz konusudur.","focus_only":"Ücretli taşıma işi yapan ve yalnız benzetme yoluyla çiftçi adı verilen kişidir.","gloss":"toprağı işleyen çiftçi","neighbor_only":"Gerçekten toprağı işleyen çiftçiyi ve çiftçilik uğraşını bildirir.","neighbor_ref":"root_001175/B003","relation_type":"near_neighbor","shared_zone":"Bu dalın adlandırması komşu daldaki gerçek çiftçi kavramından aktarılmıştır."},{"boundary_match":"field_only","distinction":"Komşu dal her türlü mesleki kazancı kapsar; bu dal yalnız taşıma çalışanına yönelen benzetmeli kişi adıdır.","focus_only":"Belirli bir taşıma çalışanını çiftçiye benzeten özel bir adlandırmadır.","gloss":"meslek yoluyla kazanç sağlamak","neighbor_only":"Geçim sağlama, meslek, ticaret ve kazanç elde etme alanını genel olarak kapsar.","neighbor_ref":"root_000310/B006","relation_type":"same_field","shared_zone":"Ücretli taşıma da geçim sağlayan bir meslek ve kazanç biçimidir."},{"boundary_match":"field_only","distinction":"Bu dal taşıma hizmetini sunan kişidir; komşu dal ise taşıma için kullanılan hayvandır.","focus_only":"Taşıma işini yapan insanı ve ona verilen benzetmeli adı bildirir.","gloss":"yolculuk için hazırlanmış yük devesi","neighbor_only":"Yolculukta binmek ve yük taşımak için hazırlanan deveyi bildirir.","neighbor_ref":"root_000964/B004","relation_type":"same_field","shared_zone":"İnsan ve hayvan farklı rollerle aynı yolculuk ve yük taşıma alanında yer alır."}],"source_phrase_ar":"الفلاح المكاري وإنما قيل له فلاح تشبيها بالأكار (ayn;tahdhib)؛ وجعله ابن أحمر المكاري (jamhara)","source_summary":"Kaynaklar, ücretle taşıma işi yapan kişiye gerçek mesleği tarım olmadığı halde çiftçiye benzetilerek aynı adın verildiğinde birleşir.","sources":["AY","JA","TA"],"what_is_ar":"المكاري إذا سمي فلاحا تشبيها بالأكار","what_is_not_ar":"ليس الأكار والزارع على الحقيقة؛ وليس الفلاح بمعنى الفوز والبقاء"},"support_links":[]},{"boundary":"Anlam yalnız anlık bir kazanma değildir; iyilik içinde kalıcılık, zarardan kurtulma ve amaçlanan sonuca erişme boyutlarını birlikte taşır.","branch_kind":"mixed_non_bare","branch_ref":"root_001175/B005","candidate_links":[{"candidate_id":"cand_da740048d4da35cf4392","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَفْلَحَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>afolaHa|ROOT:flH|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:2:1","qac_word_ref":"87:14:2","surface_ar":"أَفْلَحَ"}],"gloss":"iyilik içinde kalma, amaca ulaşma ve kurtuluş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İyilik içinde kalmak ve bu iyi durumu sürdürmek."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İstenen sonuca ulaşıp başarı, kurtuluş veya üstünlük elde etmek."}}],"root_ar":"ف ل ح","root_id":"root_001175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıcılık ile olumlu sonuca erişme boyutlarının ikisini de taşıyan genel kavram karşılığıdır.","boundary_detail":"Anlam yalnız anlık bir kazanma değildir; iyilik içinde kalıcılık, zarardan kurtulma ve amaçlanan sonuca erişme boyutlarını birlikte taşır.","branch_image_ar":"فوز وبقاء","concept_gloss":"iyilik içinde kalma, amaca ulaşma ve kurtuluş","contextual_glosses":[{"applicability":"Bir kişinin istediği sonuca ulaştığı veya zarardan kurtulduğu eylem bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Amaca ulaşma, başarı ve kurtuluş bileşenlerini korur."},"facet_ids":["F002"],"text":"başarıya ve kurtuluşa erişmek","usage_role":"contextual"},{"applicability":"Olumlu bir durumun sürmesi ve kişinin o durum içinde kalması vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İyilik içinde bulunma ve kalıcılık boyutlarını korur."},"facet_ids":["F001"],"text":"iyilik içinde kalıcı olmak","usage_role":"contextual"}],"definition":"İyilik içinde kalıcı olmak ve istenen sonuca ulaşarak başarı, kurtuluş ya da üstünlük elde etmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İyilik içinde kalmak ve bu iyi durumu sürdürmek."},{"facet_id":"F002","role":"core","statement":"İstenen sonuca ulaşıp başarı, kurtuluş veya üstünlük elde etmek."}],"identity_rationale":"Kaynak ifadesi iyilik içinde kalmayı, başarıyı, kurtuluşu, üstün gelmeyi ve istenen sonuca ulaşmayı aynı anlam alanında açıkça toplar. Dal başlığı bu birleşik çekirdeği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"iyilik içinde kalma, başarı ve kurtuluş"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"iyilik içinde kalma ve başarı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"başarmak, amacına ulaşmak veya iyilik elde etmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"dilediğin biçimde yaşa"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"işinde başarı kazan ve onu kendi başına yürüt"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kurtuluşa ve kalıcı iyiliğe yönel"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"iyilik elde eden başarılı kişi"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"dünya hayatında kalıcılık, varlık ve saygınlık elde etme"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"son bulmayan yaşam, yoksulluksuz varlık, aşağılanmayan saygınlık ve bilgisizlikten uzak bilgi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"şafak öncesi öğünü ya da gece ibadetinin kazancını kaçırmaktan korkmak"}],"lexicalization_note":"Tanım genel başarı ve kalıcı iyilik çekirdeğini verir; yaşama, bir işi bağımsız yürütme ve çağrı sözleri gibi yapıya bağlı kullanımları bu çekirdekten ayrı tutar.","neighbor_coverage_note":"Verilen tüm komşular değerlendirildi; başarı ve kurtuluşun en yakın iki karşılığı, bereket alanı ve özel öğün kullanımı en yararlı sınırları verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kazanma ve kurtulma olayına odaklanır; bu dal bunlara iyilik içinde kalıcı olma boyutunu da ekler.","focus_only":"İyilik içinde kalıcılığı açık bir kurucu boyut olarak içerir.","gloss":"kötülükten kurtulup iyiliği kazanmak","neighbor_only":"Bir şeyi ele geçirme ve payın sahibine çıkması gibi somut kazanım örneklerini içerir.","neighbor_ref":"root_001186/B001","relation_type":"near_synonym","shared_zone":"Her iki dal iyiliğe erişme, başarı ve zarardan kurtulma anlamlarında geniş ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal hedefe ulaşma ve ulaştırma ile sınırlıyken bu dal başarıya kurtuluş ve kalıcı iyilik boyutlarını ekler.","focus_only":"Kurtuluşu ve iyilik içinde kalıcılığı da kapsar.","gloss":"istenen şeyi elde etmek veya ettirmek","neighbor_only":"Bir başkasının istenen şeyi elde etmesini sağlama anlamını da kapsar.","neighbor_ref":"root_000941/B002","relation_type":"near_synonym","shared_zone":"İki dal da kişinin istediği sonuca ulaşmasını ve başarı kazanmasını ifade eder."},{"boundary_match":"partial","distinction":"Bu dal kişinin başarıya ve kurtuluşa erişmesine odaklanır; komşu dal olumlu uğur ve bereket niteliğine odaklanır.","focus_only":"Bir amaca ulaşma, üstün gelme ve kurtulma sonucunu içerir.","gloss":"uğur, mutluluk ve bereket","neighbor_only":"Uğur, bereket ve bir şeyden hayır umma anlamlarını içerir.","neighbor_ref":"root_001698/B001","relation_type":"near_neighbor","shared_zone":"İki dal olumlu sonuç, iyilik ve esenlik alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal soyut olumlu sonucu bildirir; komşu dal bu sonuçla gerekçelendirilen belirli bir öğünü adlandırır.","focus_only":"Genel başarı, kurtuluş ve iyilik içinde kalıcılık anlamıdır.","gloss":"orucu destekleyen şafak öncesi öğün","neighbor_only":"Orucu sürdürmeye güç veren şafak öncesi öğünün özel adıdır.","neighbor_ref":"root_001175/B006","relation_type":"near_neighbor","shared_zone":"Özel öğün adının gerekçesi, gücün ve orucun sürmesi düşüncesi üzerinden kalıcılık anlamına bağlanır."}],"source_phrase_ar":"الأصل الثاني الفلاح البقاء والفوز (maqayis)؛ الفلاح والفلح البقاء في الخير (ayn;tahdhib)؛ الفلح والفلاح البقاء (jamhara)؛ الفلاح الفوز والنجاة والبقاء (sihah)؛ أفلح وأنجح إذا أدرك مطلوبه (jamhara)؛ استفلحي بأمرك أي فوزي أو اظفري بأمرك (maqayis;sihah;tahdhib)؛ الفلاح الظفر وإدراك بغية (mufradat)","source_summary":"Kaynaklar iyilik içinde kalıcılık ile amaca ulaşma, başarı, kurtuluş ve üstün gelme anlamlarını ortak bir olumlu sonuç alanında birleştirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الفلاح والفلح بمعنى البقاء في الخير والفوز والنجاة والظفر وإدراك المطلوب؛ وأفلح إذا ظفر أو أصاب خيرا","what_is_not_ar":"ليس الشق الحسي؛ وليس الفلاحة؛ وليس السحور المخصوص"},"support_links":["sup_c79ffcf871a54dc34c28"]},{"boundary":"Anlam genel başarı veya kalıcılık değildir; oruç öncesindeki belirli öğünün, sürdürme gücü sağladığı için aldığı özel addır.","branch_kind":"mixed_non_bare","branch_ref":"root_001175/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَفْلَحَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>afolaHa|ROOT:flH|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:2:1","qac_word_ref":"87:14:2","surface_ar":"أَفْلَحَ"}],"gloss":"orucu sürdürmeye güç veren şafak öncesi öğün","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Oruçtan önce şafak vaktinde yenilen öğünün özel adı."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırmanın, öğünün oruç tutma gücünü ve orucun sürmesini desteklemesine bağlanması."}}],"root_ar":"ف ل ح","root_id":"root_001175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli öğünü ve bu öğüne verilen adın sürdürme gücüyle ilişkili gerekçesini birlikte temsil eder.","boundary_detail":"Anlam genel başarı veya kalıcılık değildir; oruç öncesindeki belirli öğünün, sürdürme gücü sağladığı için aldığı özel addır.","branch_image_ar":"السحور المسمى فلاحا","concept_gloss":"orucu sürdürmeye güç veren şafak öncesi öğün","contextual_glosses":[{"applicability":"Sözün doğrudan oruç öncesinde yenilen belirli öğünü adlandırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli öğünü ve onun şafak öncesindeki zamanını korur."},"facet_ids":["F001"],"text":"şafak öncesi öğün","usage_role":"contextual"}],"definition":"Oruç tutanın gücünü ve orucu sürdürmesine yardımcı olduğu düşünülen şafak öncesi öğün için kullanılan özel ad.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Oruçtan önce şafak vaktinde yenilen öğünün özel adı."},{"facet_id":"F002","role":"associated_use","statement":"Adlandırmanın, öğünün oruç tutma gücünü ve orucun sürmesini desteklemesine bağlanması."}],"identity_rationale":"Kaynak ifadesi şafak öncesi yenilen öğünü doğrudan bu adla tanımlar ve adlandırmayı oruç tutanın gücünün ya da orucun sürmesiyle açıklar. Dal bu özel göndermeyi ve gerekçesini korur.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"şafak öncesi öğün"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"şafak öncesi öğünü ya da gece ibadetinin kazancını kaçırmaktan korkmak"}],"lexicalization_note":"Tanım öğünün bağımsız adlandırmasını, bağlama göre değişen söz yorumundan ayırır; genel başarı anlamını dalın çekirdeğine katmaz.","neighbor_coverage_note":"Tüm aday komşular incelendi; öğünün olağan adı, genel besin kavramı ve başarı-kalıcılık dalı özel adlandırmanın sınırını yeterince belirler.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal öğünün olağan adını ve yenmesini bildirir; bu dal aynı öğüne sürdürme gücü düşüncesiyle verilmiş özel addır.","focus_only":"Öğünün adını, gücü ve orucu sürdürmesiyle gerekçelendiren özel bir kullanımdır.","gloss":"şafak vaktinde yenilen oruç öğünü","neighbor_only":"Şafak vaktindeki yiyecek ve içeceği, ayrıca bunları tüketme eylemini doğrudan kapsar.","neighbor_ref":"root_000682/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da oruçtan önce şafak vaktinde yenilen aynı öğüne gönderme yapar."},{"boundary_match":"partial","distinction":"Komşu dal besini genel olarak adlandırır; bu dal zamanı, oruç bağlamı ve sürdürme işlevi belirlenmiş tek bir öğündür.","focus_only":"Oruç öncesindeki belirli zamanda yenilen öğüne ve orucu destekleme işlevine bağlıdır.","gloss":"besin ve geçimlik yiyecek","neighbor_only":"Vücuda giren her türlü yiyecek ve besini genel olarak kapsar.","neighbor_ref":"root_000560/B002","relation_type":"near_neighbor","shared_zone":"Şafak öncesi öğün de insanı besleyen yiyeceklerden oluşur."},{"boundary_match":"partial","distinction":"Bu dal somut bir öğüne gönderme yapar; komşu dal ise olumlu ve kalıcı sonucun soyut anlamını taşır.","focus_only":"Şafak öncesi öğünün özel adıdır.","gloss":"iyilik içinde kalma ve başarı","neighbor_only":"Başarıyı, kurtuluşu, amaca ulaşmayı ve iyilik içinde kalmayı genel olarak ifade eder.","neighbor_ref":"root_001175/B005","relation_type":"near_neighbor","shared_zone":"Öğünün özel adı, gücün ve orucun sürmesi yoluyla kalıcılık düşüncesiyle ilişkilendirilir."}],"source_phrase_ar":"الفلاح السحور (maqayis;ayn;sihah;tahdhib)؛ سمي فلاحا لأن الإنسان تبقى معه قوته على الصوم (maqayis)؛ لأن به بقاء الصوم (sihah;tahdhib)؛ سمي السحور الفلاح (mufradat)","source_summary":"Kaynaklar adı şafak öncesi öğüne verir; çoğu açıklama, öğünün oruç tutanın gücünü veya orucun sürmesini desteklemesini adlandırmanın gerekçesi sayar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الفلاح بمعنى السحور وما علل ببقاء قوة الصائم أو بقاء الصوم","what_is_not_ar":"ليس مطلق الفوز والبقاء؛ وليس شق الأرض والحديد"},"support_links":[]},{"boundary":"Alışverişi çekici gösterme ayrı bir kullanım yüzüdür; yalan, yanıltıcı fiyat artırımı ve alaya alma ise açıkça aldatıcı yüzü oluşturur.","branch_kind":"mixed_non_bare","branch_ref":"root_001175/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَفْلَحَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>afolaHa|ROOT:flH|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:2:1","qac_word_ref":"87:14:2","surface_ar":"أَفْلَحَ"}],"gloss":"alışverişi çekici gösterme; yalanla kandırma ve alaya alma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Satış ve alışverişi satıcıya veya alıcıya çekici göstermek."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğu kandırmak ve onlara gerçeğe aykırı söz söylemek."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kiracının başkasını daha yüksek bedel vermeye kandırmak için bedeli artırması."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Başkalarını kandırma ve alaya alma davranışı."}}],"root_ar":"ف ل ح","root_id":"root_001175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın çekici gösterme yüzüyle açıkça aldatıcı ve alaycı yüzlerini birbirine karıştırmadan birlikte gösteren üst karşılıktır.","boundary_detail":"Alışverişi çekici gösterme ayrı bir kullanım yüzüdür; yalan, yanıltıcı fiyat artırımı ve alaya alma ise açıkça aldatıcı yüzü oluşturur.","branch_image_ar":"تزيين البيع والمكر","concept_gloss":"alışverişi çekici gösterme; yalanla kandırma ve alaya alma","contextual_glosses":[{"applicability":"Sözün satıcı veya alıcı yararına alışverişi cazip gösterme yapısında kullanıldığı bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alışveriş alanını, tarafları ve çekici gösterme işlemini korur."},"facet_ids":["F001"],"text":"satış ve alışverişi taraflara çekici göstermek","usage_role":"contextual"},{"applicability":"Gerçeğe aykırı söz, kandırma veya alaya alma bildiren yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yalan söyleme, kandırma ve alaya alma davranışlarını korur."},"facet_ids":["F002","F004"],"text":"yalanla kandırmak ve alaya almak","usage_role":"contextual"},{"applicability":"Bir kiracının başka birini daha yüksek bedel vermeye yöneltmek için görünürde bedel artırdığı özel kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedel artırma işlemini, yanıltma amacını ve hedef kişiyi korur."},"facet_ids":["F003"],"text":"başkasını yanıltmak için bedeli artırmak","usage_role":"explanatory"}],"definition":"Satış ve alışverişi satıcıya ya da alıcıya çekici göstermek. Ayrı yapılarda ise yalan söyleyerek kandırmak, başkasını daha yüksek bedel vermeye çekmek için bedeli artırmak veya alaya almak.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Satış ve alışverişi satıcıya veya alıcıya çekici göstermek."},{"facet_id":"F002","role":"associated_use","statement":"Bir topluluğu kandırmak ve onlara gerçeğe aykırı söz söylemek."},{"facet_id":"F003","role":"specialization","statement":"Bir kiracının başkasını daha yüksek bedel vermeye kandırmak için bedeli artırması."},{"facet_id":"F004","role":"associated_use","statement":"Başkalarını kandırma ve alaya alma davranışı."}],"identity_rationale":"Kaynak ifadesi alışverişi taraflara çekici göstermeyi, yalanla kandırmayı, sahte artırımla başkasını yanıltmayı ve alaya almayı aynı dalda sıralar. Ancak ilk kullanım açıkça kandırma şartı taşımaz; bu nedenle dal korunmalı, fakat çekici gösterme ile aldatıcı kullanımlar tek bir eylemmiş gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"satış ve alışverişi satıcıya ve alıcıya çekici göstermek"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"satış ve alışverişi satıcıya ve alıcıya çekici göstermek"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"onları kandırıp gerçeğe aykırı söz söylemek"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"başkasını daha yüksek bedel vermeye kandırmak için kiracının bedeli artırması"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"kandırma ve alaya alma"}],"lexicalization_note":"Tanım, taraflara bağlı alışveriş yapılarını ve kandırma yapılarını ayrı yüzler olarak gösterir; bunlardan genel ve sınırsız bir yalın anlam üretmez.","neighbor_coverage_note":"Bütün komşular değerlendirildi; süslü yalan, yumuşak sözlü aldatma, baş başa kandırma ve pazar alanı dalın farklı kullanım yüzlerini açıkça sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal aldatıcı biçimde süslenmiş söze odaklanır; bu dal alışveriş davranışlarını, doğrudan kandırmayı ve alayı da kapsar.","focus_only":"Alışverişi çekici gösterme, yanıltıcı bedel artırımı ve alaya alma kullanımlarını da içerir.","gloss":"yalanla süslenmiş çekici söz","neighbor_only":"Özellikle güzel görünen fakat yalanla süslenmiş sözü bildirir.","neighbor_ref":"root_000628/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal çekici gösterme ile aldatmayı aynı olay içinde buluşturabilir."},{"boundary_match":"partial","distinction":"Komşu dal söz ve toplumsal yakınlıktaki yapmacıklığı merkez alır; bu dal ticari yönlendirme ile daha açık yalan ve alayı da içerir.","focus_only":"Ticari çekici gösterme, sahte bedel artırımı ve alaya alma gibi özel kullanımları vardır.","gloss":"yumuşak sözle aldatıcı davranmak","neighbor_only":"Yumuşak ve güzel sözle yaklaşma ile içtenliksiz toplumsal ilişkiye odaklanır.","neighbor_ref":"root_001420/B016","relation_type":"near_neighbor","shared_zone":"İki dal da dışarıdan olumlu görünen bir davranışın kandırma amacı taşımasını anlatabilir."},{"boundary_match":"partial","distinction":"Komşu dal ortamı özel görüşmeyle sınırlar; bu dalda böyle bir ortam koşulu yoktur ve ticari kullanımlar ayrıca bulunur.","focus_only":"Alışverişi çekici gösterme ve yanıltıcı fiyat artırımı gibi ticari uygulamaları vardır.","gloss":"baş başayken kandırmak veya alay etmek","neighbor_only":"Kandırma veya alayın baş başa kalınan durumda yapılmasını şart koşar.","neighbor_ref":"root_000436/B015","relation_type":"near_synonym","shared_zone":"Her iki dal başkasını kandırma ve alaya alma davranışlarını ifade eder."},{"boundary_match":"field_only","distinction":"Komşu dal ticaretin yerini ve genel etkinliğini adlandırır; bu dal o alandaki belirli yönlendirme ve aldatma davranışlarını anlatır.","focus_only":"Satış ve alışverişi çekici gösteren ya da ticari işlemde başkasını yanıltan davranıştır.","gloss":"pazar ve alışveriş yeri","neighbor_only":"Malın getirildiği, satıldığı ve alındığı pazar yerini ve alışveriş alanını bildirir.","neighbor_ref":"root_000762/B005","relation_type":"same_field","shared_zone":"Satış, alış ve bedel artırma olayları pazar ve alışveriş alanında gerçekleşebilir."}],"source_phrase_ar":"فلحت للقوم وبالقوم أفلح فلاحة وهو أن يزين البيع والشراء للبائع والمشتري (tahdhib)؛ فلحت بهم تفليحا إذا مكر بهم وقال لهم غير الحق (tahdhib)؛ الفلح النجس وهو زيادة المكتري ليزيد غيره فيغر به (tahdhib)؛ التفليح المكر والاستهزاء (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Alışverişi çekici gösterme ile kandırma, yanıltıcı bedel artırımı ve alaya alma kullanımlarının tamamı bu tek tanıklıkta yer alır."}],"source_summary":"Tek kaynak, alışverişi taraflara çekici gösterme kullanımının yanında yalanla kandırma, yanıltıcı bedel artırımı ve alaya alma kullanımlarını da kaydeder.","sources":["TA"],"what_is_ar":"فلح للقوم أو بالقوم في تزيين البيع والشراء؛ وفلح بهم تفليحا في المكر وقول غير الحق؛ والفلح في زيادة المكتري ليغر غيره؛ والتفليح في المكر والاستهزاء","what_is_not_ar":"ليس الفوز والبقاء؛ وليس شق الأرض؛ وليس الفلاحة"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["87:14:1"],"branch_refs":[],"candidate_id":"cand_25add50f034d4babf15a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:14:1:boundary-counter-verdict","source_type":"word_analysis","support_ids":["sup_89966617f47cca9727eb","sup_c7f307ce745c11e6947d"],"title":"counter-verdict after punishment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:1","qac_refs":["87:14:1:1"],"status":"accepted"}},{"anchor_refs":["87:14:1"],"branch_refs":[],"candidate_id":"cand_3f2a685c6e8975cc9d4b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:14:1:certified-before-identity","source_type":"word_analysis","support_ids":["sup_1f44b5468a7e05d9bda7","sup_89966617f47cca9727eb"],"title":"certainty before identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:1","qac_refs":["87:14:1:1"],"status":"accepted"}},{"anchor_refs":["87:14:1"],"branch_refs":[],"candidate_id":"cand_75c4de3a4cec691f76bb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:14:1:certified-perfect-verdict","source_type":"word_analysis","support_ids":["sup_89966617f47cca9727eb","sup_ac0f74d956de9a2b30f7"],"title":"certified realized verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:1","qac_refs":["87:14:1:1"],"status":"accepted"}},{"anchor_refs":["87:14:1"],"branch_refs":[],"candidate_id":"cand_14c63e0cfb6fafca40ab","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:14:1:clipped-acoustic-launch","source_type":"word_analysis","support_ids":["sup_0e992c763285cb8a6dc3","sup_89966617f47cca9727eb"],"title":"clipped opening beat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:1","qac_refs":["87:14:1:1"],"status":"accepted"}},{"anchor_refs":["87:14:1"],"branch_refs":[],"candidate_id":"cand_b1d567f7bb82f6454a77","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:14:1:formulaic-success-opening","source_type":"word_analysis","support_ids":["sup_7515477116aa2c2d1ffe","sup_89966617f47cca9727eb"],"title":"success formula reprise","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:1","qac_refs":["87:14:1:1"],"status":"accepted"}},{"anchor_refs":["87:14:1"],"branch_refs":[],"candidate_id":"cand_1795d934346a56851916","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:14:1:predicate-not-purification-scope","source_type":"word_analysis","support_ids":["sup_89966617f47cca9727eb","sup_938f6f9e9728c5f277b5"],"title":"scope on success","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:1","qac_refs":["87:14:1:1"],"status":"accepted"}},{"anchor_refs":["87:14:2"],"branch_refs":[],"candidate_id":"cand_74f70e55944baee06a90","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001175"],"scope":"focus_ayah","source_local_id":"87:14:2:absolute-intransitive-success","source_type":"word_analysis","support_ids":["sup_683cf487f2ce765c160e","sup_f07e724937c7caef1e36"],"title":"absolute success","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:2","qac_refs":["87:14:2:1"],"status":"accepted"}},{"anchor_refs":["87:14:2"],"branch_refs":[],"candidate_id":"cand_61d8d9850895d5b62ec9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001175"],"scope":"focus_ayah","source_local_id":"87:14:2:achieved-success-verdict","source_type":"word_analysis","support_ids":["sup_b786452c57f1edbb8541","sup_f07e724937c7caef1e36"],"title":"achieved success verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:2","qac_refs":["87:14:2:1"],"status":"accepted"}},{"anchor_refs":["87:14:2"],"branch_refs":[],"candidate_id":"cand_037281d973645a4ec351","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001175"],"scope":"focus_ayah","source_local_id":"87:14:2:acoustic-landing","source_type":"word_analysis","support_ids":["sup_db1c59dec947dce9c41b","sup_f07e724937c7caef1e36"],"title":"breath-marked landing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:2","qac_refs":["87:14:2:1"],"status":"accepted"}},{"anchor_refs":["87:14:2"],"branch_refs":[],"candidate_id":"cand_ff23e581ee44ba120fbe","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001175"],"scope":"focus_ayah","source_local_id":"87:14:2:counterclass-after-punishment","source_type":"word_analysis","support_ids":["sup_d2ca0f13cd5816b8cdbc","sup_f07e724937c7caef1e36"],"title":"successful counterclass","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:2","qac_refs":["87:14:2:1"],"status":"accepted"}},{"anchor_refs":["87:14:2"],"branch_refs":[],"candidate_id":"cand_9a1a885aaae007f5f740","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001175"],"scope":"focus_ayah","source_local_id":"87:14:2:cultivated-flourishing","source_type":"word_analysis","support_ids":["sup_141044c3aad861a2e00e","sup_f07e724937c7caef1e36"],"title":"cultivated flourishing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:2","qac_refs":["87:14:2:1"],"status":"accepted"}},{"anchor_refs":["87:14:2"],"branch_refs":[],"candidate_id":"cand_aa70b0cbee0501f505f7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001175"],"scope":"focus_ayah","source_local_id":"87:14:2:form-iv-surface","source_type":"word_analysis","support_ids":["sup_ac41fa399fcb32a40f6d","sup_f07e724937c7caef1e36"],"title":"marked derived form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:2","qac_refs":["87:14:2:1"],"status":"accepted"}},{"anchor_refs":["87:14:2"],"branch_refs":[],"candidate_id":"cand_5b7cdab2e5e7830c3ddd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001175"],"scope":"focus_ayah","source_local_id":"87:14:2:formulaic-recurrence","source_type":"word_analysis","support_ids":["sup_707df89ccfc3cd23c7f3","sup_f07e724937c7caef1e36"],"title":"formulaic recurrence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:2","qac_refs":["87:14:2:1"],"status":"accepted"}},{"anchor_refs":["87:14:2"],"branch_refs":[],"candidate_id":"cand_3c04f80f53255c5f5e24","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001175"],"scope":"focus_ayah","source_local_id":"87:14:2:launch-unit","source_type":"word_analysis","support_ids":["sup_7628ad8c17022ec78344","sup_f07e724937c7caef1e36"],"title":"compact launch unit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:2","qac_refs":["87:14:2:1"],"status":"accepted"}},{"anchor_refs":["87:14:2"],"branch_refs":[],"candidate_id":"cand_15e7edd3458da06ba75c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001175"],"scope":"focus_ayah","source_local_id":"87:14:2:paired-perfect-outcome-and-condition","source_type":"word_analysis","support_ids":["sup_0d429532de52c303802b","sup_f07e724937c7caef1e36"],"title":"paired perfect verbs","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:2","qac_refs":["87:14:2:1"],"status":"accepted"}},{"anchor_refs":["87:14:2"],"branch_refs":[],"candidate_id":"cand_26c7a42306ae0eb8b164","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001175"],"scope":"focus_ayah","source_local_id":"87:14:2:purification-defined-subject","source_type":"word_analysis","support_ids":["sup_b9af847a20dc1343c5a1","sup_f07e724937c7caef1e36"],"title":"subject disclosed by criterion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:2","qac_refs":["87:14:2:1"],"status":"accepted"}},{"anchor_refs":["87:14:3"],"branch_refs":[],"candidate_id":"cand_b3648df1cd4142b5d49b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:14:3:accountable-same-person","source_type":"word_analysis","support_ids":["sup_6590532d7d554d879579","sup_f5df0bd1e430ba7abaae"],"title":"same accountable person","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:3","qac_refs":["87:14:3:1"],"status":"accepted"}},{"anchor_refs":["87:14:3"],"branch_refs":[],"candidate_id":"cand_81c52674b07c24b933f2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:14:3:boundary-to-general-rule","source_type":"word_analysis","support_ids":["sup_6590532d7d554d879579","sup_c790d1dd603534823d5b"],"title":"turn to general rule","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:3","qac_refs":["87:14:3:1"],"status":"accepted"}},{"anchor_refs":["87:14:3"],"branch_refs":[],"candidate_id":"cand_288c2df3a1f30d6c3fef","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:14:3:delayed-relative-subject","source_type":"word_analysis","support_ids":["sup_6590532d7d554d879579","sup_b28ad32b95c76b59c43f"],"title":"delayed relative subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:3","qac_refs":["87:14:3:1"],"status":"accepted"}},{"anchor_refs":["87:14:3"],"branch_refs":[],"candidate_id":"cand_861540a4ac19e4c7e8a3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:14:3:open-class-by-action","source_type":"word_analysis","support_ids":["sup_6590532d7d554d879579","sup_f22439e61e3c548655f0"],"title":"open class by action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:3","qac_refs":["87:14:3:1"],"status":"accepted"}},{"anchor_refs":["87:14:3"],"branch_refs":[],"candidate_id":"cand_dddc65b5d57c85680832","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:14:3:relative-and-conditional-coloring","source_type":"word_analysis","support_ids":["sup_6590532d7d554d879579","sup_7490a97ddae0c81b5394"],"title":"whoever and the one who","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:3","qac_refs":["87:14:3:1"],"status":"accepted"}},{"anchor_refs":["87:14:3"],"branch_refs":[],"candidate_id":"cand_e8a739a5729d5b51fd0d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:14:3:semantic-load-forward","source_type":"word_analysis","support_ids":["sup_6590532d7d554d879579","sup_8332ebad9c32d23095e4"],"title":"meaning carried forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:3","qac_refs":["87:14:3:1"],"status":"accepted"}},{"anchor_refs":["87:14:4"],"branch_refs":[],"candidate_id":"cand_3e026da4769b0f7ca978","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"87:14:4:boundary-reversal","source_type":"word_analysis","support_ids":["sup_0f73d1ca3ee5e821759d","sup_a894c451773e9c575033"],"title":"answer to denied vitality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:4","qac_refs":["87:14:4:1"],"status":"accepted"}},{"anchor_refs":["87:14:4"],"branch_refs":[],"candidate_id":"cand_28e116c5c92be08db410","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"87:14:4:criterion-not-single-biography","source_type":"word_analysis","support_ids":["sup_4250b291d0b2bcabf89a","sup_a894c451773e9c575033"],"title":"criterion for whoever","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:4","qac_refs":["87:14:4:1"],"status":"accepted"}},{"anchor_refs":["87:14:4"],"branch_refs":[],"candidate_id":"cand_e4b0d704746c3898f60e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"87:14:4:due-extraction-as-growth","source_type":"word_analysis","support_ids":["sup_a894c451773e9c575033","sup_f2ec9963f3d36a4211d5"],"title":"subtraction as growth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:4","qac_refs":["87:14:4:1"],"status":"accepted"}},{"anchor_refs":["87:14:4"],"branch_refs":[],"candidate_id":"cand_64d99d163ad48efc9de1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"87:14:4:final-purification-criterion","source_type":"word_analysis","support_ids":["sup_7b5a435ee472fffe67f4","sup_a894c451773e9c575033"],"title":"final purification criterion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:4","qac_refs":["87:14:4:1"],"status":"accepted"}},{"anchor_refs":["87:14:4"],"branch_refs":[],"candidate_id":"cand_e45d73386455fc99b032","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"87:14:4:form-v-self-involving","source_type":"word_analysis","support_ids":["sup_9acbd7990fe66b1b950f","sup_a894c451773e9c575033"],"title":"self-involving Form V","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:4","qac_refs":["87:14:4:1"],"status":"accepted"}},{"anchor_refs":["87:14:4"],"branch_refs":[],"candidate_id":"cand_cff1213bde9ac36a55e3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"87:14:4:forward-into-remembrance-and-prayer","source_type":"word_analysis","support_ids":["sup_a894c451773e9c575033","sup_c36f5b2394163639d08a"],"title":"unfolds into later acts","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:4","qac_refs":["87:14:4:1"],"status":"accepted"}},{"anchor_refs":["87:14:4"],"branch_refs":[],"candidate_id":"cand_c7fd95412ee52e70a210","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"87:14:4:growth-purity-fusion","source_type":"word_analysis","support_ids":["sup_3a0ed23188c21ca707cd","sup_a894c451773e9c575033"],"title":"growth through cleansing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:4","qac_refs":["87:14:4:1"],"status":"accepted"}},{"anchor_refs":["87:14:4"],"branch_refs":[],"candidate_id":"cand_9f17bc11fa173d1336dc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"87:14:4:not-self-commendation","source_type":"word_analysis","support_ids":["sup_a894c451773e9c575033","sup_eda45e8d048853c0ea7c"],"title":"not self-commendation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:4","qac_refs":["87:14:4:1"],"status":"accepted"}},{"anchor_refs":["87:14:4"],"branch_refs":[],"candidate_id":"cand_149ba2872ea7c355fb93","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"87:14:4:objectless-comprehensive-purification","source_type":"word_analysis","support_ids":["sup_a894c451773e9c575033","sup_cc865a30d8a636ab429d"],"title":"objectless comprehensive purification","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:4","qac_refs":["87:14:4:1"],"status":"accepted"}},{"anchor_refs":["87:14:4"],"branch_refs":[],"candidate_id":"cand_2e4db786f23730b64ae1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"87:14:4:recitational-closure","source_type":"word_analysis","support_ids":["sup_a894c451773e9c575033","sup_fc5d1d6dfe81cde6cbba"],"title":"long-vowel closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:4","qac_refs":["87:14:4:1"],"status":"accepted"}},{"anchor_refs":["87:14:4"],"branch_refs":[],"candidate_id":"cand_b6c60be757b29cf479fe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"87:14:4:sound-links-forward","source_type":"word_analysis","support_ids":["sup_a894c451773e9c575033","sup_f1ffe62962a80d98df86"],"title":"sound links forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:4","qac_refs":["87:14:4:1"],"status":"accepted"}},{"anchor_refs":["87:14:4"],"branch_refs":[],"candidate_id":"cand_051cd191b55cce5368b1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"87:14:4:success-purification-pair","source_type":"word_analysis","support_ids":["sup_0ff56d58a7355a27cf9f","sup_a894c451773e9c575033"],"title":"success-purification pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:14:4","qac_refs":["87:14:4:1"],"status":"accepted"}},{"anchor_refs":["87:14:2"],"branch_refs":[],"candidate_id":"cand_14610abb83b37f6237f3","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001175"],"scope":"focus_ayah","source_local_id":"87:14:2:1","source_type":"qac_morpheme","support_ids":["sup_d61bd5b68e905806718a"],"title":"QAC root occurrence: ف ل ح","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:14:4"],"branch_refs":[],"candidate_id":"cand_cfd3f00fb1f84a3c3d3c","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"87:14:4:1","source_type":"qac_morpheme","support_ids":["sup_7f88eb7bd30ba549ef54"],"title":"QAC root occurrence: ز ك و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:14"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:14","branch_refs":["root_000637/B002","root_001175/B005"],"candidate_id":"cand_da740048d4da35cf4392","commentary_obligation":"review","hft_ref":"hft_e794d5449a515c64c327","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_durable_rectitude","source_type":"hft","support_ids":["sup_c79ffcf871a54dc34c28"],"title":"baseline_durable_rectitude","trust":"legacy_unbound"},{"anchor_refs":["87:14"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:14","branch_refs":["root_000637/B001","root_001175/B003"],"candidate_id":"cand_5c2dab6f77af8d8e7755","commentary_obligation":"review","hft_ref":"hft_b07bdaa0cac324be0251","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_cultivated_increase","source_type":"hft","support_ids":["sup_3b224864180081dd711e"],"title":"baseline_cultivated_increase","trust":"legacy_unbound"},{"anchor_refs":["87:14"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:14","branch_refs":["root_000637/B004","root_001175/B001"],"candidate_id":"cand_c7e2315d1d3d5821759d","commentary_obligation":"review","hft_ref":"hft_84d98c3c52eecc30162e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_opening_into_fitness","source_type":"hft","support_ids":["sup_57360a114f6de622f5da"],"title":"baseline_opening_into_fitness","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"قَدْ أَفْلَحَ مَن تَزَكَّىٰ","qac_morphemes":[{"lemma_ar":"قَد","morph_features":"STEM|POS:CERT|LEM:qad","morpheme_role":"STEM","pos":"CERT","qac_ref":"87:14:1:1","qac_word_ref":"87:14:1","root_ar":"","surface_ar":"قَدْ"},{"lemma_ar":"أَفْلَحَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>afolaHa|ROOT:flH|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:2:1","qac_word_ref":"87:14:2","root_ar":"ف ل ح","surface_ar":"أَفْلَحَ"},{"lemma_ar":"مَن","morph_features":"STEM|POS:REL|LEM:man","morpheme_role":"STEM","pos":"REL","qac_ref":"87:14:3:1","qac_word_ref":"87:14:3","root_ar":"","surface_ar":"مَن"},{"lemma_ar":"تَزَكَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:4:1","qac_word_ref":"87:14:4","root_ar":"ز ك و","surface_ar":"تَزَكَّىٰ"}],"word_analysis_qac_refs":[["87:14:1:1"],["87:14:2:1"],["87:14:3:1"],["87:14:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["87:14:1","87:14:2","87:14:3","87:14:4"]},"focus_surface_evidence":{"arabic_uthmani":"قَدْ أَفْلَحَ مَن تَزَكَّىٰ","qac_morphemes":[{"lemma_ar":"قَد","morph_features":"STEM|POS:CERT|LEM:qad","morpheme_role":"STEM","pos":"CERT","qac_ref":"87:14:1:1","qac_word_ref":"87:14:1","root_ar":"","surface_ar":"قَدْ"},{"lemma_ar":"أَفْلَحَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>afolaHa|ROOT:flH|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:2:1","qac_word_ref":"87:14:2","root_ar":"ف ل ح","surface_ar":"أَفْلَحَ"},{"lemma_ar":"مَن","morph_features":"STEM|POS:REL|LEM:man","morpheme_role":"STEM","pos":"REL","qac_ref":"87:14:3:1","qac_word_ref":"87:14:3","root_ar":"","surface_ar":"مَن"},{"lemma_ar":"تَزَكَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:14:4:1","qac_word_ref":"87:14:4","root_ar":"ز ك و","surface_ar":"تَزَكَّىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["87:14:1:1"],["87:14:2:1"],["87:14:3:1"],["87:14:4:1"]],"word_analysis_refs":["87:14:1","87:14:2","87:14:3","87:14:4"],"word_rows":[{"analysis_record_ref":"87:14:1","analytic_gloss_range_en":"certifying particle before a perfect verb; locally it confirms the realized success verdict before the qualifying subject is named","analytic_root_gloss_range_en":null,"qac_refs":["87:14:1:1"],"root":{"note":"-"},"surface":{"arabic":"قَدْ","transliteration":"qad"}},{"analysis_record_ref":"87:14:2","analytic_gloss_range_en":"Form IV perfect intransitive success verdict; locally absolute achieved flourishing, with cultivation pressure retained without activating unrelated root branches","analytic_root_gloss_range_en":"broad range including cleaving and tilling, the tiller, success with lasting good, and remote branches such as pre-dawn meal or deceptive sales speech; this ayah selects the lasting-success branch with a cultivated-flourishing undertone","qac_refs":["87:14:2:1"],"root":{"arabic":"ف ل ح","transliteration":"f-l-ḥ"},"surface":{"arabic":"أَفْلَحَ","transliteration":"aflaḥa"}},{"analysis_record_ref":"87:14:3","analytic_gloss_range_en":"headless relative pronoun functioning as delayed subject; locally open as whoever or the one who, then restricted by the following purification clause","analytic_root_gloss_range_en":null,"qac_refs":["87:14:3:1"],"root":{"note":"-"},"surface":{"arabic":"مَن","transliteration":"man"}},{"analysis_record_ref":"87:14:4","analytic_gloss_range_en":"Form V perfect active/reflexive-middle purification verb with no explicit object; locally self-involving purification that remains comprehensive and closes the ayah's criterion","analytic_root_gloss_range_en":"broad range including growth and increase, purity and rectitude, charitable due, fittingness, and remote even-number usage; this ayah selects self-involving purification, with growth-through-cleansing pressure retained and institutional or remote branches not selected as the local sense","qac_refs":["87:14:4:1"],"root":{"arabic":"ز ك و","transliteration":"z-k-w"},"surface":{"arabic":"تَزَكَّىٰ","transliteration":"tazakkā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["87:14"],"branch_refs":["root_000637/B002","root_001175/B005"],"candidate_id":"cand_da740048d4da35cf4392","evidence_scope":"focus_ayah","hft_ref":"hft_e794d5449a515c64c327","item_id":"baseline_durable_rectitude","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_durable_rectitude","support_id":"sup_c79ffcf871a54dc34c28"},{"anchor_refs":["87:14"],"branch_refs":["root_000637/B001","root_001175/B003"],"candidate_id":"cand_5c2dab6f77af8d8e7755","evidence_scope":"focus_ayah","hft_ref":"hft_b07bdaa0cac324be0251","item_id":"baseline_cultivated_increase","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_cultivated_increase","support_id":"sup_3b224864180081dd711e"},{"anchor_refs":["87:14"],"branch_refs":["root_000637/B004","root_001175/B001"],"candidate_id":"cand_c7e2315d1d3d5821759d","evidence_scope":"focus_ayah","hft_ref":"hft_84d98c3c52eecc30162e","item_id":"baseline_opening_into_fitness","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_opening_into_fitness","support_id":"sup_57360a114f6de622f5da"}],"diagnostics":[],"lane_counts":{"global":9,"macro":12,"micro":3},"packet_summary":{"ayah_count":19,"focus_ref":"87:14","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ء ث ر","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":true,"target_occurrences":9,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]}],"window":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"87:14","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"87:14","lane":"micro","linguistic_source_ref":"87:14","surface_ref":"87:14","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"87:14","target_tokens":[["Arınan",["87:14:4"]],["kişi",["87:14:3"]],["gerçekten",["87:14:1"]],["kurtuluşa",["87:14:2"]],["ermiştir",["87:14:2"]]],"text":"Arınan kişi gerçekten kurtuluşa ermiştir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s087-p01-001-019","label":"Whole surah","number":1,"refs":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:2:paired-perfect-outcome-and-condition","source_type":"word_analysis","support_id":"sup_0d429532de52c303802b","text":"{\"blocking_evidence\":null,\"headline\":\"paired perfect verbs\",\"reader_payoff\":\"The reader sees success and purification as matched formal counterparts: outcome and condition answer each other.\",\"reason\":\"Both local verbs are perfect active verbs, while their distinct roots keep success and purification related but not identical.\",\"representative_source_ids\":[\"QF-b3bb941b\",\"QE-13026cbf\",\"QE-42e9144f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:1:clipped-acoustic-launch","source_type":"word_analysis","support_id":"sup_0e992c763285cb8a6dc3","text":"{\"blocking_evidence\":null,\"headline\":\"clipped opening beat\",\"reader_payoff\":\"The reader hears the verdict begin with a compact certifying beat before the fuller success verb expands it.\",\"reason\":\"The phonetic row adds a pacing payoff that fits the particle's first-position certifying role.\",\"representative_source_ids\":[\"QP-8b8fa7b6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:4:boundary-reversal","source_type":"word_analysis","support_id":"sup_0f73d1ca3ee5e821759d","text":"{\"blocking_evidence\":null,\"headline\":\"answer to denied vitality\",\"reader_payoff\":\"The reader sees the move from denied vitality in 87:13 to purifying growth in 87:14.\",\"reason\":\"The boundary rows link the prior punishment scene with the growth-purity root field named at the ayah's close.\",\"representative_source_ids\":[\"QB-00935ae2\",\"QB-79e0724e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:4:success-purification-pair","source_type":"word_analysis","support_id":"sup_0ff56d58a7355a27cf9f","text":"{\"blocking_evidence\":null,\"headline\":\"success-purification pair\",\"reader_payoff\":\"The reader hears this ayah as a condensed success criterion, not a loose thematic statement about purity.\",\"reason\":\"The CRITICAL rows preserve the paired-context recurrence, and the local line contains both {{ar:أَفْلَحَ}} ({{tr:aflaḥa}}) and {{ar:تَزَكَّىٰ}} ({{tr:tazakkā}}).\",\"representative_source_ids\":[\"QE-fe0b9540\",\"QH-6785fa86\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:2:cultivated-flourishing","source_type":"word_analysis","support_id":"sup_141044c3aad861a2e00e","text":"{\"blocking_evidence\":null,\"headline\":\"cultivated flourishing\",\"reader_payoff\":\"The reader senses success as cultivated flourishing rather than arbitrary status, while still keeping the local sense as achieved felicity.\",\"reason\":\"V4 preserves cleaving, tilling, and lasting-success branches for {{ar:ف ل ح}} ({{tr:f-l-ḥ}}), but the local Form IV success predicate selects the lasting-good branch and only allows cultivation as semantic pressure.\",\"representative_source_ids\":[\"QS-2de4101a\",\"QS-6783a2e0\",\"QF-0cd3967f\",\"MS-d3b1a489\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:1:certified-before-identity","source_type":"word_analysis","support_id":"sup_1f44b5468a7e05d9bda7","text":"{\"blocking_evidence\":null,\"headline\":\"certainty before identity\",\"reader_payoff\":\"The reader feels the outcome outrun social identity; the ayah announces success before saying who qualifies.\",\"reason\":\"Attachment evidence identifies {{ar:مَن}} ({{tr:man}}) as the subject after {{ar:أَفْلَحَ}} ({{tr:aflaḥa}}), so the initial particle and predicate precede the named criterion.\",\"representative_source_ids\":[\"QT-e1c07624\",\"MT-6f94d4fb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:4:growth-purity-fusion","source_type":"word_analysis","support_id":"sup_3a0ed23188c21ca707cd","text":"{\"blocking_evidence\":null,\"headline\":\"growth through cleansing\",\"reader_payoff\":\"The reader senses purification as growth by removing corruption, while the local sense remains self-involving purification.\",\"reason\":\"V4 accepts growth, purity, charitable-due, fittingness, and even-number branches for {{ar:ز ك و}} ({{tr:z-k-w}}), but local Form V syntax licenses the purification branch with growth pressure, not the remote branches as local meanings.\",\"representative_source_ids\":[\"QS-1fa182b7\",\"QS-d364a376\",\"MS-214923bc\",\"ME-683b2e1f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:4:criterion-not-single-biography","source_type":"word_analysis","support_id":"sup_4250b291d0b2bcabf89a","text":"{\"blocking_evidence\":null,\"headline\":\"criterion for whoever\",\"reader_payoff\":\"The reader hears the completed act as an open rule of success, not only a report about one past person.\",\"reason\":\"The perfect verb is governed by the headless relative {{ar:مَن}} ({{tr:man}}), which creates an open subject class defined by the following act.\",\"representative_source_ids\":[\"QG-bc70230c\",\"QT-c0f2334e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:3","source_type":"word_analysis","support_id":"sup_6590532d7d554d879579","text":"{\"gloss_range\":\"headless relative pronoun functioning as delayed subject; locally open as whoever or the one who, then restricted by the following purification clause\",\"prose\":\"{{ar:مَن}} ({{tr:man}}) is the delayed subject of {{ar:أَفْلَحَ}} ({{tr:aflaḥa}}) and the head of the relative clause {{ar:تَزَكَّىٰ}} ({{tr:tazakkā}}). It does not inherit a named group, tribe, rank, or prior noun; it opens a person-slot and lets the following verb define it. That makes the successful class open as whoever, yet restricted by purification rather than identity claims. The 3ms agreement of {{ar:تَزَكَّىٰ}} ({{tr:tazakkā}}) locks the purifying action to the same accountable person who receives the success verdict. Its brief sound also hands the line forward to the longer purification verb; after the fixed negative figure of 87:13, 87:15 shows that this open subject can carry onward into remembrance and prayer.\",\"root_display\":\"-\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَن}} ({{tr:man}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:2:absolute-intransitive-success","source_type":"word_analysis","support_id":"sup_683cf487f2ce765c160e","text":"{\"blocking_evidence\":null,\"headline\":\"absolute success\",\"reader_payoff\":\"The reader avoids reducing the verdict to success in wealth, status, survival, or recognition.\",\"reason\":\"Attachment evidence gives an intransitive frame with no object, and the valency profile confirms the exact form is consistently objectless in the sampled profile.\",\"representative_source_ids\":[\"QG-4531c47f\",\"QG-d6fde967\",\"MG-c3789e0b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:2:formulaic-recurrence","source_type":"word_analysis","support_id":"sup_707df89ccfc3cd23c7f3","text":"{\"blocking_evidence\":null,\"headline\":\"formulaic recurrence\",\"reader_payoff\":\"The reader notices that 87:14 compresses a familiar success declaration into an open purification criterion.\",\"reason\":\"The CRITICAL rows cite 23:1 and 91:9, and the contextual profile reports the exact Form IV perfect as low occurrence.\",\"representative_source_ids\":[\"QI-d24c3d13\",\"QI-ee62d900\",\"QI-f074aa66\",\"MI-aa23399a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:3:relative-and-conditional-coloring","source_type":"word_analysis","support_id":"sup_7490a97ddae0c81b5394","text":"{\"blocking_evidence\":null,\"headline\":\"whoever and the one who\",\"reader_payoff\":\"The reader hears both definition and invitation: the class is restricted, but the access point is open.\",\"reason\":\"The headless relative construction lets {{ar:مَن}} ({{tr:man}}) define the successful class through the following act without naming a closed group.\",\"representative_source_ids\":[\"QS-f4542a99\",\"QI-a6408282\",\"QB-fc684317\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:1:formulaic-success-opening","source_type":"word_analysis","support_id":"sup_7515477116aa2c2d1ffe","text":"{\"blocking_evidence\":null,\"headline\":\"success formula reprise\",\"reader_payoff\":\"The reader notices that 87:14 is not using generic success vocabulary but entering a familiar verdict formula with its own criterion.\",\"reason\":\"The CRITICAL rows give concrete parallels at 23:1 and 91:9, and the contextual profile marks the exact success form as low occurrence.\",\"representative_source_ids\":[\"QI-d5469031\",\"QE-03a20f87\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:2:launch-unit","source_type":"word_analysis","support_id":"sup_7628ad8c17022ec78344","text":"{\"blocking_evidence\":null,\"headline\":\"compact launch unit\",\"reader_payoff\":\"The reader hears the first two words as a complete verdict unit that the rest of the ayah explains.\",\"reason\":\"The local syntax begins with {{ar:قَدْ أَفْلَحَ}} ({{tr:qad aflaḥa}}), then supplies the relative subject and its defining clause.\",\"representative_source_ids\":[\"QT-4a300e16\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:4:final-purification-criterion","source_type":"word_analysis","support_id":"sup_7b5a435ee472fffe67f4","text":"{\"blocking_evidence\":null,\"headline\":\"final purification criterion\",\"reader_payoff\":\"The reader is left with purification as the explanation of success, not as an optional virtue appended afterward.\",\"reason\":\"QAC places {{ar:تَزَكَّىٰ}} ({{tr:tazakkā}}) as the Form V perfect verb in the relative clause after {{ar:مَن}} ({{tr:man}}), and the word is the ayah's final lexical item.\",\"representative_source_ids\":[\"QG-2c171eb3\",\"QT-3733a6a4\",\"QT-c0e5fe12\",\"QY-7e2498c9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:14:4:1","source_type":"qac_morpheme","support_id":"sup_7f88eb7bd30ba549ef54","text":"{\"lemma_ar\":\"تَزَكَّىٰ\",\"morph_features\":\"STEM|POS:V|PERF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"87:14:4:1\",\"qac_word_ref\":\"87:14:4\",\"root_ar\":\"ز ك و\",\"surface_ar\":\"تَزَكَّىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:3:semantic-load-forward","source_type":"word_analysis","support_id":"sup_8332ebad9c32d23095e4","text":"{\"blocking_evidence\":null,\"headline\":\"meaning carried forward\",\"reader_payoff\":\"The reader feels the pronoun depend on the act that follows; the subject is built as a criterion, not a name.\",\"reason\":\"The pronoun has no lexical root field in QAC, and the local relative clause supplies the defining predicate immediately after it.\",\"representative_source_ids\":[\"QS-f6a3a006\",\"QT-8f561594\",\"QP-12e5f83f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:1","source_type":"word_analysis","support_id":"sup_89966617f47cca9727eb","text":"{\"gloss_range\":\"certifying particle before a perfect verb; locally it confirms the realized success verdict before the qualifying subject is named\",\"prose\":\"{{ar:قَدْ}} ({{tr:qad}}) makes the ayah begin as a certified verdict. Because it stands directly before the perfect verb {{ar:أَفْلَحَ}} ({{tr:aflaḥa}}), the success is heard as realized and confirmed, not as a hope, command, future possibility, or merely occasional outcome. The particle certifies the success predicate itself; {{ar:مَن تَزَكَّىٰ}} ({{tr:man tazakkā}}) then identifies who bears that already announced result, so purification is the criterion rather than a separate socially visible claim. The opening also participates in the recognizable perfected-success formula of 23:1 and 91:9, while 87:14 delays identity into a purification-defined relative clause. After the preceding punishment scene of 87:13, this clipped first word turns the discourse into a counter-verdict of established flourishing.\",\"root_display\":\"-\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:قَدْ}} ({{tr:qad}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:1:predicate-not-purification-scope","source_type":"word_analysis","support_id":"sup_938f6f9e9728c5f277b5","text":"{\"blocking_evidence\":null,\"headline\":\"scope on success\",\"reader_payoff\":\"The reader distinguishes the certified outcome from the later criterion that identifies the successful person.\",\"reason\":\"The local clause has {{ar:قَدْ}} ({{tr:qad}}) immediately before {{ar:أَفْلَحَ}} ({{tr:aflaḥa}}), while {{ar:مَن تَزَكَّىٰ}} ({{tr:man tazakkā}}) functions as the delayed subject and relative content.\",\"representative_source_ids\":[\"QG-2ebbf5c8\",\"QS-7f53ae4c\",\"QT-bc7f5263\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:4:form-v-self-involving","source_type":"word_analysis","support_id":"sup_9acbd7990fe66b1b950f","text":"{\"blocking_evidence\":null,\"headline\":\"self-involving Form V\",\"reader_payoff\":\"The reader sees success assigned to one who enters purification, not to someone passively cleansed while uninvolved or merely praised as pure.\",\"reason\":\"QAC marks the local verb as Form V active/reflexive-middle, and attachment evidence notes the reflexive-middle use with the subject controlled by {{ar:مَن}} ({{tr:man}}).\",\"representative_source_ids\":[\"QG-3dc0f506\",\"QF-1fffe557\",\"QF-ac5040ea\",\"QF-c479cf20\",\"MF-eb0db6d7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:4","source_type":"word_analysis","support_id":"sup_a894c451773e9c575033","text":"{\"gloss_range\":\"Form V perfect active/reflexive-middle purification verb with no explicit object; locally self-involving purification that remains comprehensive and closes the ayah's criterion\",\"prose\":\"{{ar:تَزَكَّىٰ}} ({{tr:tazakkā}}) is the word that finally explains the success verdict. As a Form V perfect in the relative clause after {{ar:مَن}} ({{tr:man}}), it defines the successful person by a completed, self-involving entry into purification, not by passive cleansing or self-commendation; the contrast with 53:32 keeps this away from boasting and toward actual purification. Its objectless frame matters: unlike the soul-object named in 91:9, 87:14 does not confine purification to one explicit domain, so self, conduct, intention, wealth, and relation to God are not artificially separated. The root {{ar:ز ك و}} ({{tr:z-k-w}}) joins purity with growth and increase; the charitable-due branch such as {{ar:زَكَاة}} ({{tr:zakāh}}) narrows here into the idea that removal can cleanse and increase, not into a local legal-payment sense. The doubled middle gives the word audible intensity, and the final long vowel leaves purification as the ayah's landing; its cadence carries into 87:15, where the purified subject unfolds into remembrance of the Lord's name and prayer.\",\"root_display\":\"{{ar:ز ك و}} ({{tr:z-k-w}})\",\"root_gloss_range\":\"broad range including growth and increase, purity and rectitude, charitable due, fittingness, and remote even-number usage; this ayah selects self-involving purification, with growth-through-cleansing pressure retained and institutional or remote branches not selected as the local sense\",\"surface_display\":\"{{ar:تَزَكَّىٰ}} ({{tr:tazakkā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:1:certified-perfect-verdict","source_type":"word_analysis","support_id":"sup_ac0f74d956de9a2b30f7","text":"{\"blocking_evidence\":null,\"headline\":\"certified realized verdict\",\"reader_payoff\":\"The reader hears success as an accomplished verdict rather than an aspiration or uncertain possibility.\",\"reason\":\"QAC marks {{ar:قَدْ}} ({{tr:qad}}) as a certifying particle before the perfect verb {{ar:أَفْلَحَ}} ({{tr:aflaḥa}}), and attachment evidence says it strengthens the realization of that predicate.\",\"representative_source_ids\":[\"QG-2dd068f6\",\"QG-95334565\",\"MG-fbd5ff74\",\"QS-b270559d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:2:form-iv-surface","source_type":"word_analysis","support_id":"sup_ac41fa399fcb32a40f6d","text":"{\"blocking_evidence\":null,\"headline\":\"marked derived form\",\"reader_payoff\":\"The reader notices that the word's own surface carries the move from root texture into achieved success.\",\"reason\":\"The local morphology is Form IV, and V4's success branch supports reading the derived verb as attainment of lasting good.\",\"representative_source_ids\":[\"QF-44616192\",\"MF-5f5753a0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:3:delayed-relative-subject","source_type":"word_analysis","support_id":"sup_b28ad32b95c76b59c43f","text":"{\"blocking_evidence\":null,\"headline\":\"delayed relative subject\",\"reader_payoff\":\"The reader experiences identity as delayed until the purification clause can disclose it.\",\"reason\":\"QAC marks {{ar:مَن}} ({{tr:man}}) as a relative pronoun, and attachment evidence makes it the subject of {{ar:أَفْلَحَ}} ({{tr:aflaḥa}}) with {{ar:تَزَكَّىٰ}} ({{tr:tazakkā}}) completing the relative content.\",\"representative_source_ids\":[\"QG-377fed65\",\"QG-8957dda7\",\"QT-f82de47f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:2:achieved-success-verdict","source_type":"word_analysis","support_id":"sup_b786452c57f1edbb8541","text":"{\"blocking_evidence\":null,\"headline\":\"achieved success verdict\",\"reader_payoff\":\"The reader hears success as already reached and judicially announced before the qualifying subject appears.\",\"reason\":\"QAC and attachment evidence identify {{ar:أَفْلَحَ}} ({{tr:aflaḥa}}) as a Form IV perfect active verb, and the contextual profile marks the exact form as limited and formulaic.\",\"representative_source_ids\":[\"QG-02568348\",\"QF-e1cc1ec1\",\"QH-9377bf4c\",\"QY-009a3e6a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:2:purification-defined-subject","source_type":"word_analysis","support_id":"sup_b9af847a20dc1343c5a1","text":"{\"blocking_evidence\":null,\"headline\":\"subject disclosed by criterion\",\"reader_payoff\":\"The reader waits with the syntax: success is announced first, and purification then reveals the successful person.\",\"reason\":\"Attachment evidence makes {{ar:مَن}} ({{tr:man}}) the subject of {{ar:أَفْلَحَ}} ({{tr:aflaḥa}}), completed by the relative predicate {{ar:تَزَكَّىٰ}} ({{tr:tazakkā}}).\",\"representative_source_ids\":[\"QG-0b16c17f\",\"QT-91bb97d2\",\"MT-57ba9f7b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:4:forward-into-remembrance-and-prayer","source_type":"word_analysis","support_id":"sup_c36f5b2394163639d08a","text":"{\"blocking_evidence\":null,\"headline\":\"unfolds into later acts\",\"reader_payoff\":\"The reader sees purification become concrete in 87:15 instead of remaining an abstract inward label.\",\"reason\":\"Attachment evidence controls the implicit subject through {{ar:مَن}} ({{tr:man}}), and CRITICAL rows explicitly connect 87:14 with remembrance and prayer in 87:15.\",\"representative_source_ids\":[\"QG-ae9b196c\",\"MI-8ba20ac6\",\"QB-09958fbc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:3:boundary-to-general-rule","source_type":"word_analysis","support_id":"sup_c790d1dd603534823d5b","text":"{\"blocking_evidence\":null,\"headline\":\"turn to general rule\",\"reader_payoff\":\"The reader notices the ayah move from a fixed negative type to an open successful subject carried into later acts.\",\"reason\":\"The boundary rows connect the open subject with the transition from the prior punishment scene and with the continuation of the subject into 87:15.\",\"representative_source_ids\":[\"QB-084648c5\",\"QB-488e5caa\",\"QY-63d8318d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:1:boundary-counter-verdict","source_type":"word_analysis","support_id":"sup_c7f307ce745c11e6947d","text":"{\"blocking_evidence\":null,\"headline\":\"counter-verdict after punishment\",\"reader_payoff\":\"The reader notices the discourse pivot from denied life in 87:13 into certified flourishing in 87:14.\",\"reason\":\"The boundary rows explicitly connect the initial certifier with the move from the prior deprivation scene into the positive success verdict.\",\"representative_source_ids\":[\"QB-5d29d775\",\"QB-cc87b87f\",\"QY-6d4fc159\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:4:objectless-comprehensive-purification","source_type":"word_analysis","support_id":"sup_cc865a30d8a636ab429d","text":"{\"blocking_evidence\":null,\"headline\":\"objectless comprehensive purification\",\"reader_payoff\":\"The reader keeps the purified field broad instead of narrowing it prematurely to soul, wealth, intention, or conduct alone.\",\"reason\":\"Attachment evidence gives no object for {{ar:تَزَكَّىٰ}} ({{tr:tazakkā}}), and the CRITICAL comparison with 91:9 highlights the absence of an explicit object like {{ar:زَكَّاهَا}} ({{tr:zakkāhā}}).\",\"representative_source_ids\":[\"QG-38f03263\",\"MG-fd508798\",\"QF-117171c6\",\"QI-1eaa50c7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:2:counterclass-after-punishment","source_type":"word_analysis","support_id":"sup_d2ca0f13cd5816b8cdbc","text":"{\"blocking_evidence\":null,\"headline\":\"successful counterclass\",\"reader_payoff\":\"The reader feels 87:14 answer the denied vitality of 87:13 with a verdict of flourishing.\",\"reason\":\"The boundary rows explicitly frame the verb as the positive turn from the preceding punishment description into lasting success.\",\"representative_source_ids\":[\"QB-a7326751\",\"QB-e4654d49\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:14:2:1","source_type":"qac_morpheme","support_id":"sup_d61bd5b68e905806718a","text":"{\"lemma_ar\":\"أَفْلَحَ\",\"morph_features\":\"STEM|POS:V|PERF|(IV)|LEM:>afolaHa|ROOT:flH|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"87:14:2:1\",\"qac_word_ref\":\"87:14:2\",\"root_ar\":\"ف ل ح\",\"surface_ar\":\"أَفْلَحَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:2:acoustic-landing","source_type":"word_analysis","support_id":"sup_db1c59dec947dce9c41b","text":"{\"blocking_evidence\":null,\"headline\":\"breath-marked landing\",\"reader_payoff\":\"The reader hears the success word stand out acoustically before the criterion phrase follows.\",\"reason\":\"The phonetic row gives a distinct sound payoff tied to the local surface form.\",\"representative_source_ids\":[\"QP-b2949407\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:4:not-self-commendation","source_type":"word_analysis","support_id":"sup_eda45e8d048853c0ea7c","text":"{\"blocking_evidence\":null,\"headline\":\"not self-commendation\",\"reader_payoff\":\"The reader avoids mistaking the successful person's purification for self-praise or a static clean label.\",\"reason\":\"The CRITICAL contrast cites 53:32, while local morphology selects Form V {{ar:تَزَكَّىٰ}} ({{tr:tazakkā}}) rather than Form II {{ar:زَكَّى}} ({{tr:zakkā}}).\",\"representative_source_ids\":[\"QI-18b468d0\",\"QI-03c94bd3\",\"QH-78b76194\",\"QS-e7339ba6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:2","source_type":"word_analysis","support_id":"sup_f07e724937c7caef1e36","text":"{\"gloss_range\":\"Form IV perfect intransitive success verdict; locally absolute achieved flourishing, with cultivation pressure retained without activating unrelated root branches\",\"prose\":\"{{ar:أَفْلَحَ}} ({{tr:aflaḥa}}) is a perfect Form IV verdict: success has been reached before the ayah discloses the subject. The verb is intransitive and objectless here, so the success is not narrowed to a named prize such as wealth, rank, survival, or public recognition; it is an absolute state of lasting good. Its root {{ar:ف ل ح}} ({{tr:f-l-ḥ}}) carries a broader field of cleaving, tilling, and cultivated prosperity, but local form and syntax select the success branch, letting the cultivation image pressure the line without turning the verb into physical farming. The predicate waits for {{ar:مَن تَزَكَّىٰ}} ({{tr:man tazakkā}}), so the person of success is defined by purification rather than prior group identity; because both verbs are perfects, outcome and condition answer each other without collapsing into one idea. The formula recalls 23:1 and 91:9, yet 87:14 compresses the success-purification pairing into a short counter-verdict after 87:13, with a breath-marked landing before the criterion phrase follows.\",\"root_display\":\"{{ar:ف ل ح}} ({{tr:f-l-ḥ}})\",\"root_gloss_range\":\"broad range including cleaving and tilling, the tiller, success with lasting good, and remote branches such as pre-dawn meal or deceptive sales speech; this ayah selects the lasting-success branch with a cultivated-flourishing undertone\",\"surface_display\":\"{{ar:أَفْلَحَ}} ({{tr:aflaḥa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:4:sound-links-forward","source_type":"word_analysis","support_id":"sup_f1ffe62962a80d98df86","text":"{\"blocking_evidence\":null,\"headline\":\"sound links forward\",\"reader_payoff\":\"The reader hears purification move naturally toward the devotional cadence of the next ayah.\",\"reason\":\"The CRITICAL rows explicitly connect the final sound of {{ar:تَزَكَّىٰ}} ({{tr:tazakkā}}) with the closure of prayer in 87:15.\",\"representative_source_ids\":[\"QE-653521f3\",\"QP-d6b1bd57\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:3:open-class-by-action","source_type":"word_analysis","support_id":"sup_f22439e61e3c548655f0","text":"{\"blocking_evidence\":null,\"headline\":\"open class by action\",\"reader_payoff\":\"The reader sees success opened to whoever meets the purification criterion, not to a pre-named social identity.\",\"reason\":\"The local pronoun has no antecedent noun and is defined by the following relative predicate; contextual profiles also show generic human referents for the purification form.\",\"representative_source_ids\":[\"QG-380404d5\",\"QG-c373dd82\",\"MG-d829f51b\",\"MT-cb336414\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:4:due-extraction-as-growth","source_type":"word_analysis","support_id":"sup_f2ec9963f3d36a4211d5","text":"{\"blocking_evidence\":null,\"headline\":\"subtraction as growth\",\"reader_payoff\":\"The reader can feel the paradox of increase through removal without turning the verb into a narrow payment term.\",\"reason\":\"V4 records the charitable-due branch and the purity-growth branches, while the local word is a Form V verb without a financial object.\",\"representative_source_ids\":[\"QS-9783c61b\",\"QS-aba05907\",\"QS-bcea01e5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:3:accountable-same-person","source_type":"word_analysis","support_id":"sup_f5df0bd1e430ba7abaae","text":"{\"blocking_evidence\":null,\"headline\":\"same accountable person\",\"reader_payoff\":\"The reader does not treat purification as an abstract state detached from the person who receives success.\",\"reason\":\"Attachment evidence says the implicit 3ms subject of {{ar:تَزَكَّىٰ}} ({{tr:tazakkā}}) is syntactically controlled by {{ar:مَن}} ({{tr:man}}).\",\"representative_source_ids\":[\"QG-4aa1459d\",\"QG-f5fe6285\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:14:4:recitational-closure","source_type":"word_analysis","support_id":"sup_fc5d1d6dfe81cde6cbba","text":"{\"blocking_evidence\":null,\"headline\":\"long-vowel closure\",\"reader_payoff\":\"The reader hears the ayah land on purification with both intensity in the middle and openness at the end.\",\"reason\":\"The phonetic and form rows identify the doubled middle consonant and final long-vowel closure as local sound payoffs.\",\"representative_source_ids\":[\"QF-80264570\",\"QF-d0162c2e\",\"QP-ccaca355\",\"QP-f02614e7\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"قَدْ أَفْلَحَ مَن تَزَكَّىٰ","ayah_ref":"87:14"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000637/B002","root_001175/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001175","role":"The durable-success branch supplies an achieved outcome that exceeds a momentary win.","root":"ف ل ح","source_ref":"87:14","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000637","role":"The purity-and-rectitude branch supplies the reflexive transformation that characterizes the subject.","root":"ز ك و","source_ref":"87:14","source_word_indices":["4"]}],"changed_reading":{"after":"The ayah announces lasting good as already realized in the kind of person who actively brings the self into purity and rectitude.","before":"A person succeeds by becoming morally clean."},"confidence":"strong","focus_anchor":"The achieved predicate at word 2 is joined through man to the reflexive purification verb at word 4.","mechanism":"Success with lasting good and self-purification form an outcome-process relation: the successful subject is identified by actively bringing the self into purity and rectitude.","model_id":"baseline_durable_rectitude"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_durable_rectitude","source_type":"hft","support_id":"sup_c79ffcf871a54dc34c28","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قَدْ أَفْلَحَ مَن تَزَكَّىٰ","ayah_ref":"87:14"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000637/B001","root_001175/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001175","role":"The ground-splitting tiller supplies productive labor and prepared soil as the success mechanism.","root":"ف ل ح","source_ref":"87:14","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000637","role":"The increase branch supplies the growth that answers cultivation rather than a merely subtractive cleansing.","root":"ز ك و","source_ref":"87:14","source_word_indices":["4"]}],"changed_reading":{"after":"Purification is self-cultivation: worked openness produces living increase, and falah names the resulting yield.","before":"Purification removes an impurity and is then rewarded with success."},"confidence":"medium","focus_anchor":"The two finite verbs connect the tilling image latent in word 2 with growth latent in word 4.","mechanism":"A tiller opens worked ground so that increase can occur; read together, the branches make self-purification a cultivation process and success its viable yield.","model_id":"baseline_cultivated_increase"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_cultivated_increase","source_type":"hft","support_id":"sup_3b224864180081dd711e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قَدْ أَفْلَحَ مَن تَزَكَّىٰ","ayah_ref":"87:14"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000637/B004","root_001175/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001175","role":"The cleaving branch supplies an opened way through material that had enclosed or narrowed it.","root":"ف ل ح","source_ref":"87:14","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000637","role":"The fittingness branch makes the reflexive act an acquisition of aptitude for that passage.","root":"ز ك و","source_ref":"87:14","source_word_indices":["4"]}],"changed_reading":{"after":"Success is an emergence: self-fitting and the opening of a viable passage are two sides of the same event.","before":"Success is a possession awarded after purification."},"confidence":"exploratory","focus_anchor":"Word 2 can image an opening cut through constriction, while word 4 can image becoming suitable or fitting.","mechanism":"Fitness and opening make a threshold model: as the subject makes the self apt for passage, a constricted route opens into successful emergence.","model_id":"baseline_opening_into_fitness"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_opening_into_fitness","source_type":"hft","support_id":"sup_57360a114f6de622f5da","trust":"legacy_unbound"}]}
</lane_packet_json>
