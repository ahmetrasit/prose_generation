# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **87:11**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s087-regular-20260911/s087/87_11/micro.discovery.json` and modify nothing
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
  "ayah_ref": "87:11",
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
{"analysis_context":{"analysis_id":"s087-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"87:11","host_surah":87,"lane_context_refs":[],"ordered_context_refs":["87:0","87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Anlam yalnızca uzak durmayı değil, somut bir yanı, yan bölgeyi veya ona bitişik çevreyi bildirir.","branch_kind":"bare","branch_ref":"root_000262/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتَجَنَّبُ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:11:1:2","qac_word_ref":"87:11:1","surface_ar":"يَتَجَنَّبُ"}],"gloss":"bedenin veya şeyin yanı ve bitişik çevresi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan veya hayvan bedeninin böğrünü ve bir şeyin yanını ya da tarafını belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir evin veya topluluğun yerleşimine bitişik yakın çevreyi belirtebilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Vadi, ordu veya ırmak gibi bir bütünün iki yanından her birini belirtir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Devenin böğründen alınan ve kap yapımında kullanılabilen deri parçasını belirtir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedenin böğrü, bir nesnenin tarafı ve o tarafa bitişik yakın alan birlikte kastedildiğinde en uygun karşılıktır.","boundary_detail":"Anlam yalnızca uzak durmayı değil, somut bir yanı, yan bölgeyi veya ona bitişik çevreyi bildirir.","branch_image_ar":"الجنب جانب الجسد وناحية الشيء","concept_gloss":"bedenin veya şeyin yanı ve bitişik çevresi","contextual_glosses":[{"applicability":"Vadi, ordu veya ırmak gibi iki taraflı düşünülen yapıların karşılıklı yanları için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki taraflı bir bütünün karşılıklı yanlarını eksiksiz belirtir."},"facet_ids":["F003"],"text":"iki yan","usage_role":"contextual"}],"definition":"İnsan ya da hayvan gövdesinin böğrü veya herhangi bir şeyin yanı ve bu yana bitişik yakın çevredir. İki yandan oluşan düzenlerde her bir yanı, ayrıca böğürden alınan deri parçasını da adlandırabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan veya hayvan bedeninin böğrünü ve bir şeyin yanını ya da tarafını belirtir."},{"facet_id":"F002","role":"extension","statement":"Bir evin veya topluluğun yerleşimine bitişik yakın çevreyi belirtebilir."},{"facet_id":"F003","role":"specialization","statement":"Vadi, ordu veya ırmak gibi bir bütünün iki yanından her birini belirtir."},{"facet_id":"F004","role":"specialization","statement":"Devenin böğründen alınan ve kap yapımında kullanılabilen deri parçasını belirtir."}],"identity_rationale":"Kaynak ifadesi insanın veya hayvanın böğrünü, bir şeyin yanını ve bu temel anlamdan gelişen bitişik çevreyi birlikte doğrular. Vadi ve ordu gibi yapıların iki yanı ile böğürden alınan deri parçası, aynı yan bölge çekirdeğinin belirli uygulamalarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"insanın veya hayvanın böğrü"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yan, taraf"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"evin önü veya topluluğun yerleşimine bitişik çevre"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"vadinin, ordunun veya ırmağın iki yanı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"devenin böğür derisinden alınan parça"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"ordunun sağ ve sol kanadı"}],"lexicalization_note":"Dal yalın kullanıma dayanır; tanım, özel bir söz öbeğine bağlı anlamları çekirdeğe katmadan yan ve bitişik çevre alanını kapsar.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi; yan ve taraf alanındaki en güçlü sınır karşılaştırması yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel yön ve çevresel uçlar üzerinden tarafı anlatırken bu dal beden böğrünü temel alır ve bitişik çevre ile deri parçasına uzanır.","focus_only":"Bedenin böğrünü, yerleşime bitişik çevreyi ve böğürden alınan deri parçasını da kapsar.","gloss":"yan ve taraf","neighbor_only":"Dağ veya at gibi varlıkların yüksek ve dışa uzanan uçlarını da kapsar.","neighbor_ref":"root_001238/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin yanını veya tarafını adlandırabilir."}],"source_phrase_ar":"أصل الجنب الجارحة وجمعه جنوب (mufradat)؛ الجنب للإنسان وغيره (maqayis)؛ الجانب والجوانب معروفة والجنبتان ناحيتا كل شيء (ayn)؛ الجنب معروف والجانب الناحية (sihah)؛ جنبتا الوادي ناحيتاه وجناب القوم ما حولهم (tahdhib)؛ جنب الإنسان والدابة معروف وأعطني جنبة جلد جنب بعير (jamhara)","source_summary":"Anlamın ortak çekirdeği bedenin veya bir nesnenin yanıdır. Yakın çevre, iki yandan biri ve böğür derisinden alınan parça bu mekansal çekirdeğin belirli uzantılarıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه جنب الإنسان والدابة، والجانب والناحية، وجنبتا الوادي أو العسكر أو النهر، وجناب الدار والقوم وما قرب من محلتهم، وما يؤخذ من جلد الجنب.","what_is_not_ar":"لا يدخل فيه مجرد البعد والاجتناب ولا الجنوب الريح ولا الأعلام كجنب الحي وجناب الموضع."},"support_links":[]},{"boundary":"Yakınlık çekirdeği ile belirli söz öbeklerinin buyruk, yol veya bir kimse hakkındaki anlamları ayrı tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000262/B002","candidate_links":[{"candidate_id":"cand_c91955913c19c6a61c96","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَتَجَنَّبُ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:11:1:2","qac_word_ref":"87:11:1","surface_ar":"يَتَجَنَّبُ"}],"gloss":"yanında yakın bulunma ve eşlik etme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kimseye yakın olmayı, yanında bulunmayı veya kolayca yaklaşılabilir olmayı belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yolculukta bir kimsenin yanında bulunan eşlikçiyi belirtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli dinsel yapılarda yakınlık yanında buyruk, iş veya izlenen yol anlamını taşır."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaklaşılabilirlik, yan yana bulunma ve eşlik etme çekirdeğinin birlikte anlatılması gerektiğinde kullanılır.","boundary_detail":"Yakınlık çekirdeği ile belirli söz öbeklerinin buyruk, yol veya bir kimse hakkındaki anlamları ayrı tutulmalıdır.","branch_image_ar":"الجنب قرب ومجاورة على الجانب","concept_gloss":"yanında yakın bulunma ve eşlik etme","contextual_glosses":[{"applicability":"Yolculuk sırasında kişinin yanında bulunan ve ona eşlik eden kimse için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yolculuk bağlamındaki yakın eşlik ilişkisini tam olarak korur."},"facet_ids":["F002"],"text":"yol arkadaşı","usage_role":"contextual"}],"definition":"Bir kimseye yanından yakın olma, kolayca yaklaşabilme veya ona eşlik etme ilişkisidir. Belirli yapılarda bu mekansal yakınlık, bir buyruğa ya da yola bağlılık anlamına kayar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kimseye yakın olmayı, yanında bulunmayı veya kolayca yaklaşılabilir olmayı belirtir."},{"facet_id":"F002","role":"specialization","statement":"Yolculukta bir kimsenin yanında bulunan eşlikçiyi belirtir."},{"facet_id":"F003","role":"associated_use","statement":"Belirli dinsel yapılarda yakınlık yanında buyruk, iş veya izlenen yol anlamını taşır."}],"identity_rationale":"Kaynak ifadesi yumuşak yaklaşılabilirliği ve yolda eşliği gerçekten yakınlık çekirdeğine bağlar; ancak Tanrı ile ilgili yapılarda yakınlık yanında buyruk, iş ve yol yorumları da vardır. Bu nedenle dal korunur, fakat her yapının yalnızca fiziksel komşuluk diye genellenmemesi gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yaklaşması ve ilişki kurması kolay"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yol arkadaşı veya yakın eşlikçi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"Tanrı'ya yakınlıkta veya Tanrı'nın buyruğu ve yolu üzerinde"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kardeşin hakkında, özellikle onu çekiştirme konusunda"}],"lexicalization_note":"Dal hem yan üzerinden kurulan yakınlık çekirdeğini hem de belirli yapılara bağlı anlamları içerir; bu yapılar yalın anlama genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel komşulukla örtüşme ve aynı kökteki karşıt uzaklaşma yönü en açıklayıcı iki sınırdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel komşuluk düzenini anlatır; bu dal ise yan yana bulunma imgesinden gelişen kişisel yaklaşılabilirlik ve eşlik ilişkisine odaklanır.","focus_only":"Yaklaşılabilir kişiliği, yol arkadaşlığını ve belirli yapılardaki buyruk ya da yol anlamını içerir.","gloss":"yakınlık ve komşuluk","neighbor_only":"Yerleşimlerin, toprak parçalarının ve eşlerin komşuluğunu genel biçimde kapsar.","neighbor_ref":"root_000275/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da yakın bulunma ve komşu olma ilişkisini anlatır."},{"boundary_match":"opposed","distinction":"Bu dal yakınlık ve eşlik kutbunu, komşu dal ise mesafe koyma ve ayrı kalma kutbunu gerçekleştirir.","focus_only":"Yakınlaşma, yanında bulunma ve eşlik etme yönünü taşır.","gloss":"yakın durma ve uzak durma","neighbor_only":"Uzaklaşma, kaçınma, ayırma ve yabancılık yönünü taşır.","neighbor_ref":"root_000262/B003","relation_type":"polarity_pair","shared_zone":"İki dal da kişiler veya şeyler arasındaki göreli mesafe ve ilişki eksenindedir."}],"source_phrase_ar":"رجل لين الجانب والجنب أي سهل القرب (ayn;tahdhib)؛ الصاحب بالجنب صاحبك في السفر (sihah)؛ الجنب القرب وفي قرب الله وجواره (tahdhib)؛ في أمره وحده الذي حده لنا (mufradat)","source_summary":"Yakınlık ve yanında bulunma, kolay yaklaşılabilen kişi ile yol arkadaşını açıklayan ortak çekirdektir. Belirli dinsel söyleyişlerde aynı yapı mekansal yakınlığın ötesine geçerek buyruk, iş veya yol ilişkisini anlatır.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه القرب والجوار والمصاحبة من جهة الجنب، مثل الصاحب بالجنب، لين الجانب أو الجنب، وما فسرته المصادر في جنب الله بالقرب أو الجوار أو الأمر أو الطريق.","what_is_not_ar":"لا يدخل فيه الغريب الأجنبي والجار الجنب إذا أريد به البعيد من غير قومك، ولا الجنابة الشرعية."},"support_links":["sup_0793f3c648ae91665955"]},{"boundary":"Dal yakın komşuluğu değil, kişinin uzak durmasını, başkasını uzaklaştırmasını veya uzaklık sonucu yabancı kalmasını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000262/B003","candidate_links":[{"candidate_id":"cand_e1e0a6115ea9277889eb","lane":"micro"},{"candidate_id":"cand_b4902bc5400ed6c2d9d6","lane":"micro"},{"candidate_id":"cand_c91955913c19c6a61c96","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَتَجَنَّبُ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:11:1:2","qac_word_ref":"87:11:1","surface_ar":"يَتَجَنَّبُ"}],"gloss":"uzak durma veya uzaklaştırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin bir şeyden uzaklaşmasını, ona yaklaşmamasını veya onu bırakmasını belirtir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kimseyi bir şeyden uzaklaştırmayı veya kötülüğü ondan savmayı belirtir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsanlardan ayrı bir yerde durma ve yalnız kalma durumuna uzanır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Akrabalık, soy veya yerleşim bakımından uzak olan yabancı kişiyi belirtir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem kişinin kendisinin mesafe koymasını hem de bir başkasını bir şeyden uzak tutmayı kapsayan genel karşılıktır.","boundary_detail":"Dal yakın komşuluğu değil, kişinin uzak durmasını, başkasını uzaklaştırmasını veya uzaklık sonucu yabancı kalmasını anlatır.","branch_image_ar":"المجانبة إبعاد واعتزال وغربة","concept_gloss":"uzak durma veya uzaklaştırma","contextual_glosses":[{"applicability":"Bir kişinin topluluktan çekilip ayrı bir yerde kalması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluktan ayrılma ve ayrı yerde kalma anlamını korur."},"facet_ids":["F003"],"text":"insanlardan ayrı durma","usage_role":"contextual"},{"applicability":"Soy veya yerleşim yakınlığı bulunmayan bir kişinin nitelenmesinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soy veya yer bakımından uzak ve yabancı olma sonucunu korur."},"facet_ids":["F004"],"text":"akrabalığı bulunmayan yabancı","usage_role":"contextual"}],"definition":"Bir kişi veya şeyle araya mesafe koymak, ondan uzak durmak ya da birini ondan uzaklaştırmaktır. Bu ayrılma kötülükten korunma, insanlardan ayrı yaşama veya soy ve yer bakımından yabancı olma sonucunu da doğurabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin bir şeyden uzaklaşmasını, ona yaklaşmamasını veya onu bırakmasını belirtir."},{"facet_id":"F002","role":"core","statement":"Bir kimseyi bir şeyden uzaklaştırmayı veya kötülüğü ondan savmayı belirtir."},{"facet_id":"F003","role":"extension","statement":"İnsanlardan ayrı bir yerde durma ve yalnız kalma durumuna uzanır."},{"facet_id":"F004","role":"extension","statement":"Akrabalık, soy veya yerleşim bakımından uzak olan yabancı kişiyi belirtir."}],"identity_rationale":"Kaynak ifadesi bir şeyden uzaklaşmayı, onu bırakmayı, birini ondan uzaklaştırmayı, kötülüğü savmayı, insanlardan ayrı durmayı ve akrabalık ya da yerleşim bakımından yabancı olmayı açıkça aynı uzaklık alanında toplar. Etken ve edilgen katılımcı yönleri tanımda ayrı tutulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"uzak durmak, sakınmak veya bırakmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"birini bir şeyden uzaklaştırmak veya kötülükten korumak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"beni ve çocuklarımı putlara tapmaktan uzak tut"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"insanlardan ayrı bir yerde durma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"akrabalıkta, soyda veya yerleşimde uzak olan yabancı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"başka bir topluluktan gelip akrabalığı bulunmayan komşu"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"uzaktan ve yabancı olarak"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"birini iyilikten yoksun bırakmak"}],"lexicalization_note":"Yalın uzaklık alanı ile belirli yapılardaki kaçınma, koruma ve yabancılık kullanımları ayrıştırılır; yapı anlamları bütüne yayılmaz.","neighbor_coverage_note":"Bütün komşular incelendi; genel uzaklık ve tek başına kalma dalları çekirdeğin sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel ve özellikle yurt merkezli uzaklığa yayılır; bu dal ise bilinçli kaçınma, uzaklaştırma ve yakınlık bağının kesilmesini çekirdek alır.","focus_only":"Kaçınmayı, birini kötülükten uzak tutmayı ve soyca yabancı olmayı da kapsar.","gloss":"uzaklaşma ve yabancılık","neighbor_only":"Yurttan uzak kalmayı, sürgünü, uzaktan gelen haberi ve av köpeklerinin uzun takibini de kapsar.","neighbor_ref":"root_001077/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da uzaklık, ayrılma ve yabancı kalma durumlarını kapsar."},{"boundary_match":"partial","distinction":"Komşu dal tek başına bulunma durumuna odaklanır; bu dalın çekirdeği ise bir hedefe karşı mesafe koyma veya koydurmadır.","focus_only":"Bir şeyden sakınmayı, başkasını uzaklaştırmayı ve yabancılığı kapsar.","gloss":"ayrı durma","neighbor_only":"Bir topluluktan sapıp tek başına bir yerde veya gök cisminde bulunmayı kapsar.","neighbor_ref":"root_000305/B004","relation_type":"near_neighbor","shared_zone":"İki dal da topluluktan çekilme ve ayrı kalma durumunda buluşur."}],"source_phrase_ar":"الأصل الآخر البعد والجنابة (maqayis)؛ جنبته عن كذا فاجتنب أي تجنبه وجنبته أي دفعت عنه مكروها (ayn)؛ الجناب مصدر جانبته مجانبة وهو من المباعدة (jamhara)؛ جانبه وتجانبه وتجنبه واجتنبه كله بمعنى وجنبته الشيء أي نحيته عنه (sihah)؛ أجنب تباعد والجنابة ضد القرابة (tahdhib)؛ جنبته عن كذا أي أبعدته واجتنبوا عبارة عن تركهم إياه (mufradat)","source_summary":"Ortak anlam mesafe koyma ve yakınlığı kesmedir. Kişinin kendisinin uzak durması, başka birini uzaklaştırması, kötülüğü savması, ayrı kalması ve yabancı sayılması bu çekirdeğin katılımcı ve sonuç çeşitleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه جانبته وتجنبته واجتنبته، جنبته أو أجنبته عن الشيء أي أبعدته ونحيته، النجاة أو الدفع عن المكروه، الجنبة بمعنى الاعتزال، والأجنب أو الجنب بمعنى الغريب أو غير القريب في النسب والدار.","what_is_not_ar":"لا يدخل فيه القرب والمصاحبة إذا كان المراد جوارا وملازمة، ولا حالة الجنابة الشرعية إلا من جهة تعليلها بالبعد."},"support_links":["sup_0793f3c648ae91665955","sup_24be94ddce34b7dac6ce","sup_c001808549ecea3473b5"]},{"boundary":"Dal genel uzaklık veya bedensel yan anlamını değil, cinsel ilişki sonrası arınmaya dek süren dinsel kısıtlılığı belirtir.","branch_kind":"bare","branch_ref":"root_000262/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتَجَنَّبُ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:11:1:2","qac_word_ref":"87:11:1","surface_ar":"يَتَجَنَّبُ"}],"gloss":"cinsel ilişki sonrası arınma gerektiren dinsel durum","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Cinsel ilişki sonrasında arınma gerektiren ve kişiyi namazdan ve mescitten uzak tutan durumu belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu durumda bulunan kadın, erkek veya birden çok kişiyi niteleyebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adlandırma, kişinin arınana kadar namazdan ve mescitten uzak durmasıyla açıklanır."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Durumun sebebi, geçici dinsel kısıtı ve arınmayla sona ermesi birlikte anlatılmak istendiğinde kullanılır.","boundary_detail":"Dal genel uzaklık veya bedensel yan anlamını değil, cinsel ilişki sonrası arınmaya dek süren dinsel kısıtlılığı belirtir.","branch_image_ar":"الجنابة حالة تجنب مواضع الصلاة","concept_gloss":"cinsel ilişki sonrası arınma gerektiren dinsel durum","contextual_glosses":[{"applicability":"Cinsel ilişki sonrası geçici dinsel kısıt altında bulunan kişinin nitelenmesinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin arınma gerektiren geçici durumunu bağlam içinde korur."},"facet_ids":["F002"],"text":"arınması gereken kişi","usage_role":"contextual"}],"definition":"Cinsel ilişki sonrasında arınma yapılıncaya kadar kişinin namazdan ve mescitten uzak durduğu dinsel durumdur. Bu durumda bulunan kadın, erkek veya topluluk da aynı adlandırmayla nitelenebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Cinsel ilişki sonrasında arınma gerektiren ve kişiyi namazdan ve mescitten uzak tutan durumu belirtir."},{"facet_id":"F002","role":"extension","statement":"Bu durumda bulunan kadın, erkek veya birden çok kişiyi niteleyebilir."},{"facet_id":"F003","role":"associated_use","statement":"Adlandırma, kişinin arınana kadar namazdan ve mescitten uzak durmasıyla açıklanır."}],"identity_rationale":"Kaynak ifadesi cinsel ilişki sonrasında oluşan dinsel durumu, bu durumdaki kişi ve toplulukları ve adlandırmanın arınmaya kadar belirli ibadetlerden ve yerlerden uzak durma gerekçesini açıkça destekler. Bu uzak durma genel kaçınma değil, belirli bir dinsel hükmün sonucudur.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"cinsel ilişkiden sonra arınana dek dinsel kısıt altında bulunan kişi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"cinsel ilişki sonrası arınma gerektiren duruma girmek"}],"lexicalization_note":"Dal yalın bir dinsel durum ve bu durumdaki kişi anlamındadır; genel uzak durma anlamı tanıma taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; cinsel ilişkiden sürekli uzak durma dalı, bu geçici durumla karışma olasılığı en yüksek komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal ilişkiye girmemeyi seçme veya sürdürme halidir; bu dal ise ilişki gerçekleştikten sonra arınmaya kadar doğan geçici dinsel durumdur.","focus_only":"Gerçekleşmiş cinsel ilişkiden sonra arınmaya kadar süren dinsel kısıtlılığı belirtir.","gloss":"cinsel ilişkiden uzak kalma","neighbor_only":"Evlilikten ve cinsel ilişkiden sürekli ya da iradi biçimde uzak durmayı belirtir.","neighbor_ref":"root_000082/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da cinsel ilişkiyle bağlantılı bir uzak durma durumuna değinir."}],"source_phrase_ar":"الجنب الذي يجامع أهله مشتق من هذا لأنه يبعد عن الصلاة والمسجد (maqayis)؛ أجنب الرجل إذا أصابته الجنابة (ayn;jamhara;sihah;tahdhib)؛ رجل جنب وامرأة جنب وقوم جنب (jamhara;sihah;tahdhib)؛ سميت الجنابة بذلك لكونها سببا لتجنب الصلاة في حكم الشرع (mufradat)","source_summary":"Ortak tanım, cinsel ilişki sonrasında başlayan ve arınmaya kadar kişiyi namazdan ve mescitten uzak tutan durumdur. Durumun adı, bu uzak durmayla ilişkilendirilir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه رجل أو امرأة أو قوم جنب، أصابته الجنابة، أجنب أو جنب أو اجتنب أو تجنب، وسبب التسمية بتجنب الصلاة أو مواضعها حتى الطهر.","what_is_not_ar":"لا يدخل فيه مطلق البعد أو الغربة، ولا الجنب الجارحة."},"support_links":[]},{"boundary":"Çekirdek, bir varlığı kişinin yanında bağlı veya yönlendirilmiş biçimde götürmektir; genel eşlikçilik değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000262/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتَجَنَّبُ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:11:1:2","qac_word_ref":"87:11:1","surface_ar":"يَتَجَنَّبُ"}],"gloss":"yanında yönlendirerek götürme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hayvanı veya tutsağı kişinin kendi yanında yönlendirerek götürmesini belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yanda çekilerek götürülen hayvanı veya hayvana bağlı götürülen tutsağı belirtir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir hayvan veya tutsağın kişinin yanında bağlı ya da yönlendirilmiş biçimde götürülmesini anlatır.","boundary_detail":"Çekirdek, bir varlığı kişinin yanında bağlı veya yönlendirilmiş biçimde götürmektir; genel eşlikçilik değildir.","branch_image_ar":"التجنيب قيادة شيء إلى الجنب","concept_gloss":"yanında yönlendirerek götürme","contextual_glosses":[{"applicability":"Binek olarak kullanılmadan bir kişinin yanında çekilerek götürülen hayvan için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın yanda ve bir yönlendiricinin denetiminde götürülmesini korur."},"facet_ids":["F002"],"text":"yanda çekilerek götürülen hayvan","usage_role":"contextual"}],"definition":"Bir hayvanı veya tutsağı kişinin kendi yanında, bağlı ya da yönlendirilmiş biçimde götürmesidir. Bu biçimde yanda götürülen hayvan veya bağlı tutsak da aynı anlam alanında adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hayvanı veya tutsağı kişinin kendi yanında yönlendirerek götürmesini belirtir."},{"facet_id":"F002","role":"extension","statement":"Yanda çekilerek götürülen hayvanı veya hayvana bağlı götürülen tutsağı belirtir."}],"identity_rationale":"Yetkili dal ifadesi hayvanı veya tutsağı kişinin yanında götürmesini ve yanda götürülen varlığı destekler. Yarışta yedek at bulundurma yasağı yalnız ayrı bir sözcük biriminde tanıklanmıştır; bu nedenle dal tanımına kurucu anlam olarak alınmamış, yalnız o birimin karşılığında korunmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"hayvanı veya atı yanında yürütmek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"tutsağı yürütmek veya hayvanın yanına bağlamak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yanda çekilerek götürülen hayvan"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yarış atının yanında yedek bir at koşturma yasağı"}],"lexicalization_note":"Yalın götürme çekirdeği ile hayvan, tutsak ve yarış bağlamındaki belirli birimler ayrı tutulur; yarış yasağı bütüne genellenmez.","neighbor_coverage_note":"Bütün komşular değerlendirildi; atı yanda götürme ile bağ kullanarak çekme, işlemin sınırını en iyi gösteren iki karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yalnız atın yanda götürülmesine odaklanır; bu dal hayvanları ve tutsakları kapsayan daha geniş bir götürme düzenidir.","focus_only":"Hayvan yanında tutsak götürmeyi ve yanda götürülen varlığın adını da kapsar.","gloss":"atı yanda götürme","neighbor_only":"Özellikle bir atı binmeden yanda götürme biçimiyle sınırlıdır.","neighbor_ref":"root_001519/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir atı kişinin yanında, ona binmeden yönlendirerek götürmeyi kapsar."},{"boundary_match":"partial","distinction":"Komşu dal çekme aracına ve bağlı hayvana odaklanırken bu dal götürülen varlığın yönlendiricinin yanında bulunmasına odaklanır.","focus_only":"Yönlendirilen varlığın kişinin yanında götürülmesi konumunu kurucu sayar.","gloss":"bağla çekip götürme","neighbor_only":"Boyun ipini, yuları ve bu bağlarla çekilen hayvanı araç merkezli olarak kapsar.","neighbor_ref":"root_000235/B003","relation_type":"near_neighbor","shared_zone":"İki dal da hayvanın bir bağ veya yönlendirme yoluyla götürülmesi sahnesini paylaşır."}],"source_phrase_ar":"جنبت الدابة إذا قدتها إلى جنبك وكذلك جنبت الأسير (maqayis;jamhara)؛ الجنيبة كل دابة تقاد والجنيب الأسير مشدود إلى جنب الدابة (ayn)؛ جنبت الدابة إذا قدتها إلى جنبك ومنه خيل مجنبة (sihah)؛ جنبت الفرس أجنبه جنبا إذا قدته والجنيبة الدابة تقاد (tahdhib)؛ من جنبت الفرس كأنما سأله أن يقوده عن جانب الشرك (mufradat)","source_summary":"Anlam çekirdeği, bir hayvanı ya da tutsağı kişinin yanında yönlendirerek götürmesidir. Eylem, yanda çekilen hayvanı ve hayvana bağlı tutsağı adlandıran sonuç biçimlerine de uzanır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه جنبت الدابة أو الفرس أو الأسير إذا قدته إلى جنبك، الجنيبة الدابة المقادة، والجنب المنهي عنه في الرهان بإحضار فرس إلى جنب فرس السباق.","what_is_not_ar":"لا يدخل فيه مجرد كون الشيء ناحية، ولا الرفيق المصاحب بلا معنى القيادة."},"support_links":[]},{"boundary":"Dal genel olarak her yeli değil, belirli güney yönünden esen yeli belirtir; ona bağlı olaylar ayrı kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000262/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتَجَنَّبُ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:11:1:2","qac_word_ref":"87:11:1","surface_ar":"يَتَجَنَّبُ"}],"gloss":"güneyden esen yel","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli güney yönünden esen ve kuzeyden esen yelin karşıtı olan yeli belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yelin yönü sağ taraf, iki başka yelin yönleri arasındaki bölge veya kutsal yapının bir yanı üzerinden tarif edilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu yel sıcak oluşuyla da nitelenebilir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yelin ayırt edici yönünün güney olduğu ve kuzeyden esen yele karşı konumlandığı bağlamlarda kullanılır.","boundary_detail":"Dal genel olarak her yeli değil, belirli güney yönünden esen yeli belirtir; ona bağlı olaylar ayrı kullanımlardır.","branch_image_ar":"الجنوب ريح من جهة مخصوصة","concept_gloss":"güneyden esen yel","contextual_glosses":[{"applicability":"Yönün yanı sıra yelin sıcak niteliğinin de öne çıktığı anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güney yönünü ve kaynakta belirtilen sıcaklık niteliğini birlikte korur."},"facet_ids":["F001","F003"],"text":"sıcak güney yeli","usage_role":"contextual"}],"definition":"Belirli güney yönünden esen, kuzeyden esen yelin karşısında konumlanan ve sıcaklığıyla da nitelenebilen yeldir. Yön tarifi geleneksel yön işaretlerine göre daha ayrıntılı biçimde belirtilebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli güney yönünden esen ve kuzeyden esen yelin karşıtı olan yeli belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Yelin yönü sağ taraf, iki başka yelin yönleri arasındaki bölge veya kutsal yapının bir yanı üzerinden tarif edilir."},{"facet_id":"F003","role":"specialization","statement":"Bu yel sıcak oluşuyla da nitelenebilir."}],"identity_rationale":"Yetkili dal ifadesi belirli bir yönden esen, kuzey yeline karşıt ve çoğu kez sıcak sayılan yeli açıkça tanımlar. Bu yelin esmesi, insanların ona girmesi veya bir bulutu sürüklemesi ayrı sözcük birimlerinde tanıklanır; bunlar dalın yönsel yel çekirdeğini değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"güney yeli"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yelin güneyden esmesi veya topluluğun bu yele girip ona tutulması"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"güney yelinin sürüklediği bulut"}],"lexicalization_note":"Belirli yelin yalın adı ile esme, ona tutulma ve bulut sürükleme yapıları ayrıdır; yapıların olay anlamı yalın ada yüklenmez.","neighbor_coverage_note":"Bütün komşular değerlendirildi; genel yel alanı ve farklı yönlü belirli bir yel, dalın yönsel sınırını en açık gösteren adaylardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel yel ve esinti alanıdır; bu dal yalnız belirli güney yönünden gelen yeldir.","focus_only":"Yeli güney yönü ve kuzeyden esen yele karşıtlığıyla sınırlar.","gloss":"yel","neighbor_only":"Yelin yönünden bağımsız olarak hafif veya sert esintileri ve havalandırma araçlarını da kapsar.","neighbor_ref":"root_000609/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da hareket eden havayı ve onun esmesini adlandırır."},{"boundary_match":"field_only","distinction":"Aynı yel sınıflandırmasına katılsalar da esiş yönleri farklıdır ve birbirlerinin yerine kullanılamazlar.","focus_only":"Güney yönünden esen ve kuzey yeline karşı konumlanan yeli belirtir.","gloss":"yönlü yeller","neighbor_only":"Kutsal yapının arkasından veya batı yönünden geldiği tarif edilen başka bir yeli belirtir.","neighbor_ref":"root_000458/B012","relation_type":"same_field","shared_zone":"İki dal da geleneksel yön noktalarıyla ayırt edilen belirli bir yeli adlandırır."}],"source_phrase_ar":"مما شذ عن الباب ريح الجنوب (maqayis)؛ الجنوب ريح تجيء عن يمين القبلة وقد جنبت الريح (ayn)؛ الجنوب ريح معروفة (jamhara)؛ الجنوب الريح التي تقابل الشمال (sihah)؛ الجنوب من الرياح حارة ومهبها ما بين مهبي الصبا والدبور (tahdhib)؛ الجنوب يصح أن يعتبر فيها معنى المجيء من جانب الكعبة (mufradat)","source_summary":"Ortak çekirdek, kuzeyden esen yelin karşısındaki güney yönlü yeldir. Kaynak ifadesinde yön, geleneksel yön noktalarıyla farklı biçimlerde açıklanır ve yelin sıcak olduğu da belirtilir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الجنوب الريح، هبوبها، الدخول في الجنوب، وإصابة القوم بها، والسحابة المجنوبة.","what_is_not_ar":"لا يدخل فيه الجنب الجارحة ولا الاجتناب والبعد."},"support_links":[]},{"boundary":"Dal sağlam böğrü değil, insan veya hayvanda böğür bölgesini tutan hastalık ve ağrı durumunu belirtir.","branch_kind":"bare","branch_ref":"root_000262/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتَجَنَّبُ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:11:1:2","qac_word_ref":"87:11:1","surface_ar":"يَتَجَنَّبُ"}],"gloss":"böğür bölgesini tutan ağrı veya hastalık","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın böğründe ağrı bulunmasını veya akciğer zarını tutan hastalığa yakalanmasını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Devenin aşırı susuzluk yüzünden akciğerinin böğrüne yapıştığı hastalık durumunu belirtir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve devedeki farklı gerçekleşmeleri ortak böğür bölgesi ve bedensel bozukluk çekirdeğinde birleştirmek için kullanılır.","boundary_detail":"Dal sağlam böğrü değil, insan veya hayvanda böğür bölgesini tutan hastalık ve ağrı durumunu belirtir.","branch_image_ar":"داء الجنب وأثره في البدن","concept_gloss":"böğür bölgesini tutan ağrı veya hastalık","contextual_glosses":[{"applicability":"İnsanın böğür ağrısıyla beliren akciğer zarı hastalığına yakalanması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsandaki belirli hastalık ve böğür ağrısı bağlantısını korur."},"facet_ids":["F001"],"text":"akciğer zarı hastalığına tutulma","usage_role":"contextual"}],"definition":"İnsanda böğür ağrısı veya akciğer zarını tutan ağır hastalık, devede ise aşırı susuzluğun akciğeri böğre yapıştırdığı hastalık durumudur. Ortak nokta, böğür bölgesinin ağrı ya da iç bozuklukla etkilenmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın böğründe ağrı bulunmasını veya akciğer zarını tutan hastalığa yakalanmasını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Devenin aşırı susuzluk yüzünden akciğerinin böğrüne yapıştığı hastalık durumunu belirtir."}],"identity_rationale":"Yetkili dal ifadesi insanın böğür ağrısını veya akciğer zarı hastalığını ve devenin aşırı susuzluk sonucu akciğerinin böğrüne yapışmasını destekler. Vurularak böğrün incitilmesi yalnız ayrı sözcük biriminde tanıklıdır; bu nedenle dalın hastalık çekirdeğine katılmamıştır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"böğrü ağrımak veya akciğer zarı hastalığına tutulmak"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"vurarak böğrünü incitmek veya kırmak"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"devenin aşırı susuzluktan akciğeri böğrüne yapışacak ölçüde hastalanması"}],"lexicalization_note":"Dal yalın hastalık ve ağrı anlamında tanımlanır; ayrı bir birimdeki vurma sonucu yaralanma çekirdeğe eklenmez.","neighbor_coverage_note":"Bütün komşular değerlendirildi; genel kırık olmayan ağrı ile başka bir bölgeye özgü ağrı en yararlı sınırları sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal organ ve neden bakımından geneldir; bu dal böğür bölgesine ve belirli insan ya da deve hastalıklarına bağlıdır.","focus_only":"Böğür bölgesine özgüdür ve belirli iç hastalıklarla deve susuzluğu durumunu kapsar.","gloss":"kırık olmayan ağrı","neighbor_only":"Herhangi bir organda kırığa varmayan genel bir ağrıyı belirtir.","neighbor_ref":"root_000417/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da bedende kırık olmak zorunda olmayan bir ağrı veya incinme durumunu anlatır."},{"boundary_match":"field_only","distinction":"Ağrı alanları farklıdır: bu dal böğür ve akciğer çevresine, komşu dal boyna özgüdür.","focus_only":"Böğür ve akciğer çevresindeki ağrıyı veya hastalığı belirtir.","gloss":"bölgesel beden ağrısı","neighbor_only":"Yalnız boyun ağrısını ve bunun sağaltılmasını belirtir.","neighbor_ref":"root_000016/B006","relation_type":"same_field","shared_zone":"İki dal da belirli bir beden bölgesindeki ağrıyı adlandırır."}],"source_phrase_ar":"الجنب أن يشتد عطش البعير حتى تلتصق رئته بجنبه (maqayis)؛ أجنب فلان إذا أخذته ذات الجنب والجنيب الذي يشتكي جنبه (ayn)؛ جنب الرجل إذا اشتكى جنبه (jamhara)؛ المجنوب الذي به ذات الجنب وجنب البعير من شدة العطش (sihah)؛ ذات الجنب علة صعبة وجنب جنبا إذا اشتكى جنبه (tahdhib)؛ جنب شكا جنبه (mufradat)","source_summary":"Ortak alan böğür bölgesini tutan ağrı veya hastalıktır. İnsan için böğür ağrısı ve akciğer zarı hastalığı, deve içinse aşırı susuzluğun akciğeri böğre yapıştırdığı özel durum belirtilir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه اشتكى جنبه، ذات الجنب، المجنوب، ضربه فجنبه، وجنب البعير من شدة العطش حتى تلتصق رئته بجنبه أو يلتوي.","what_is_not_ar":"لا يدخل فيه الجنب الجارحة بلا علة، ولا الجنوب الريح."},"support_links":[]},{"boundary":"Dal hayvan sayısının azlığını veya genel güçsüzlüğü değil, özellikle develerde süt veriminin azalmasını belirtir.","branch_kind":"mixed_non_bare","branch_ref":"root_000262/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتَجَنَّبُ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:11:1:2","qac_word_ref":"87:11:1","surface_ar":"يَتَجَنَّبُ"}],"gloss":"develerde sütün azalması veya tükenmesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun develerindeki sütün azalmasını veya hiç kalmamasını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sütü azalan develerin sahibi olan kişi veya topluluk, bu eksiklik üzerinden nitelenir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi ya da topluluğun deve sürüsündeki süt verimi eksikliğini genel olarak anlatmak için kullanılır.","boundary_detail":"Dal hayvan sayısının azlığını veya genel güçsüzlüğü değil, özellikle develerde süt veriminin azalmasını belirtir.","branch_image_ar":"التجنيب قلة لبن الإبل","concept_gloss":"develerde sütün azalması veya tükenmesi","contextual_glosses":[{"applicability":"Bir topluluğa ait develerde hiç süt kalmadığının özellikle belirtildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Deve sürüsündeki tam süt yokluğunu bağlama uygun biçimde korur."},"facet_ids":["F001"],"text":"sütü tükenen deve sürüsü","usage_role":"contextual"}],"definition":"Bir kişinin veya topluluğun develerinde sütün azalması ya da bütünüyle tükenmesidir. Değişen katılımcı, sütü azalan hayvanların sahibi veya içinde bulundukları topluluktur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun develerindeki sütün azalmasını veya hiç kalmamasını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Sütü azalan develerin sahibi olan kişi veya topluluk, bu eksiklik üzerinden nitelenir."}],"identity_rationale":"Yetkili dal ifadesi bir topluluğun develerindeki sütün azalması veya tükenmesini ortak ve açık biçimde destekler. Sütün kaybolduğu yıl anlamı ayrı söz öbeğinde tanıklanmıştır; dalın kurucu tanımı sürüdeki süt yokluğuyla sınırlandırılmıştır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"topluluğun develerinde sütün azalması veya tükenmesi"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"süt kıtlığı yaşanan yıl"}],"lexicalization_note":"Sürüde süt azalması çekirdeği ile süt kıtlığı yılına bağlı söz öbeği ayrı tutulur; yıl anlamı yalın dala yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tek devenin az sütü ile sütün geri dönmesi umudu, dalın sürü ve sonuç sınırlarını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal tek hayvanın niteliğine ve genel güçsüzlüğe uzanır; bu dal sahip veya topluluk düzeyindeki sürüsel süt eksikliğine odaklanır.","focus_only":"Bir kişi veya topluluğun bütün deve varlığındaki süt azalmasını ya da yokluğunu belirtir.","gloss":"az süt verme","neighbor_only":"Tek bir dişi devenin az süt vermesini ve insan ya da iş için genel güçsüzlüğü de kapsar.","neighbor_ref":"root_000497/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da develerde süt miktarının düşük olmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal mevcut süt eksikliğini bildirir; komşu dal ise bu eksikliğe ek olarak sütün geri gelmesi beklentisini taşır.","focus_only":"Sütün azalması veya yokluğu durumunu, geri dönüş beklentisi olmadan bildirir.","gloss":"sütün kesilmesi","neighbor_only":"Kesilmiş ya da kuşkulu sütün yeniden gelmesinin umulmasını kurucu olarak içerir.","neighbor_ref":"root_001015/B006","relation_type":"near_neighbor","shared_zone":"İki dal da develerde sütün bulunmaması veya azalması durumuyla ilgilidir."}],"source_phrase_ar":"جنب القوم إذا قلت ألبانهم (maqayis;sihah)؛ جنب بنو فلان إذا لم يكن في إبلهم لبن (ayn;tahdhib)؛ جنب الرجل إذا قلت ألبان إبله (jamhara)؛ جنب بنو فلان إذا لم يكن في إبلهم اللبن (mufradat)","source_summary":"Ortak anlam, bir kişi ya da topluluğa ait develerde sütün azalması veya kalmamasıdır. Söyleyiş hayvanı doğrudan değil, bu süt eksikliğinden etkilenen sahibi ya da topluluğu özne yapar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه جنب القوم أو بنو فلان إذا قلت ألبان إبلهم أو لم يكن في إبلهم لبن، وعام تجنيب.","what_is_not_ar":"لا يدخل فيه الجنب الجارحة ولا المجنوب المريض."},"support_links":[]},{"boundary":"Dal bağımsız ve genel çokluk anlamı değildir; çokluk yalnız belirtilen iyi veya kötü yapısı içinde gerçekleşir.","branch_kind":"collocation","branch_ref":"root_000262/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتَجَنَّبُ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:11:1:2","qac_word_ref":"87:11:1","surface_ar":"يَتَجَنَّبُ"}],"gloss":"çok miktarda iyilik veya kötülük","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli söz öbeğinde iyilik veya kötülüğün çok miktarda olmasını belirtir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İyiliğin çokluğu, onun kişinin yanında hazır bulunması düşüncesiyle açıklanabilir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız belirtilen iyi veya kötü adlarıyla kurulan yapının çokluk anlamını karşılamak için kullanılır.","boundary_detail":"Dal bağımsız ve genel çokluk anlamı değildir; çokluk yalnız belirtilen iyi veya kötü yapısı içinde gerçekleşir.","branch_image_ar":"المجنب خير أو شر كثير","concept_gloss":"çok miktarda iyilik veya kötülük","contextual_glosses":[{"applicability":"Söz öbeğinin olumlu kutbunda çok miktarda iyilik bulunduğunu anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Olumlu bağlamdaki iyilik ve çokluk anlamlarını birlikte korur."},"facet_ids":["F001"],"text":"bolca iyilik","usage_role":"contextual"}],"definition":"Yalnız belirli bir söz öbeği içinde, iyiliğin veya kötülüğün çok miktarda bulunmasını belirtir. İyiliğin kişiye yakın bulunması, çokluğu açıklayan ikincil bir tasarım olarak verilebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli söz öbeğinde iyilik veya kötülüğün çok miktarda olmasını belirtir."},{"facet_id":"F002","role":"associated_use","statement":"İyiliğin çokluğu, onun kişinin yanında hazır bulunması düşüncesiyle açıklanabilir."}],"identity_rationale":"Kaynak ifadesi yalnız belirli iyi ve kötü adlarıyla kurulan yapıda çokluk anlamını doğrular. İyilik için verilen kişinin yanında bulunma açıklaması olası bir anlamlandırmadır; çekirdek, söz konusu iyi veya kötünün çok miktarda olmasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"pek çok iyilik veya kötülük"}],"lexicalization_note":"Tanım yalnız çok miktarda iyilik veya kötülük bildiren belirli söz öbeğine bağlıdır; yalın köke genel çokluk anlamı verilmez.","neighbor_coverage_note":"Bütün komşular değerlendirildi; genel çoklukla kapsam farkı ve azlıkla karşıtlık, yapıya bağlı anlamın sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel çokluk anlamıdır; bu dal yalnız iyilik veya kötülükle kurulan belirli yapıda çokluk bildirir.","focus_only":"Çokluk anlamı yalnız belirli iyi veya kötü adlarıyla kurulan söz öbeğinde geçerlidir.","gloss":"çokluk","neighbor_only":"Her türlü şeyin, sayının veya malın çokluğunu ve bir şeyi çoğaltmayı genel olarak kapsar.","neighbor_ref":"root_001286/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin yüksek miktarda bulunmasını bildirir."},{"boundary_match":"opposed","distinction":"Bu dal yüksek miktar kutbunda, komşu dal ise azlık ve küçüklük kutbundadır.","focus_only":"Belirli bir iyilik veya kötülüğün yüksek miktarını bildirir.","gloss":"çok ve az","neighbor_only":"Bir şeyin az, küçük, önemsiz veya değersiz oluşunu bildirir.","neighbor_ref":"root_000053/B013","relation_type":"antonym","shared_zone":"İki dal miktarın yüksek ya da düşük olması ekseninde karşı karşıya gelir."}],"source_phrase_ar":"المجنب الخير الكثير كأنه إلى جنب الإنسان (maqayis)؛ شرا مجنبا وخيرا مجنبا أي كثيرا (ayn)؛ خيرا مجنبة ومجنبا وشرا مجنبا أي كثيرا (jamhara)؛ المجنب بالفتح الشيء الكثير وخيرا مجنبا وشرا مجنبا (sihah)؛ المجنب الخير الكثير والمجنب يقال في الشر إذا كثر (tahdhib)؛ جنب فلان خيرا وجنب شرا (mufradat)","source_summary":"Ortak anlam, belirli iyi ve kötü adlarıyla birlikte kullanıldığında çok miktar bildirmesidir. Kişinin yanında bulunan iyilik açıklaması, çokluk çekirdeğinin kaynakta sunulan ikincil yorumudur.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه خير مجنب أو شر مجنب بمعنى كثير، وما جعلته بعض المصادر كأنه إلى جنب الإنسان.","what_is_not_ar":"لا يدخل فيه القيادة إلى الجنب ولا الترس المجنب."},"support_links":[]},{"boundary":"Dal genel olarak her otu değil, yaz döneminde kalan veya gelişen köklü küçük bitki ve çalı kümesini belirtir.","branch_kind":"bare","branch_ref":"root_000262/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتَجَنَّبُ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:11:1:2","qac_word_ref":"87:11:1","surface_ar":"يَتَجَنَّبُ"}],"gloss":"yazın kalan köklü küçük bitkiler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yazın kalan veya yaz döneminde yeniden gelişen köklü küçük bitki ve çalıların genel adıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birçok ayrı bitkiyi, kalıcı kök ve yaz döneminde varlığını sürdürme ortaklığıyla tek kümede toplar."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli bir tür yerine yaz döneminde varlığını sürdüren çeşitli köklü küçük bitkilerin ortak adı gerektiğinde kullanılır.","boundary_detail":"Dal genel olarak her otu değil, yaz döneminde kalan veya gelişen köklü küçük bitki ve çalı kümesini belirtir.","branch_image_ar":"الجنبة نبت متوسط مستقل","concept_gloss":"yazın kalan köklü küçük bitkiler","contextual_glosses":[{"applicability":"Yaz döneminde kalan veya yeniden gelişen bitki kümesini açıklayıcı biçimde anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaz dönemindeki küçük çalı ve ot kümesini anlaşılır biçimde korur."},"facet_ids":["F001","F002"],"text":"yazın kalan veya yeniden gelişen bitkiler","usage_role":"explanatory"}],"definition":"Yaz döneminde kalan ya da yeniden gelişen, kökü bulunan çeşitli küçük bitki ve çalıların ortak adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yazın kalan veya yaz döneminde yeniden gelişen köklü küçük bitki ve çalıların genel adıdır."},{"facet_id":"F002","role":"extension","statement":"Birçok ayrı bitkiyi, kalıcı kök ve yaz döneminde varlığını sürdürme ortaklığıyla tek kümede toplar."}],"identity_rationale":"Kaynak ifadesi tek bir türden çok, yaz boyunca kalan veya yazın yeniden gelişen çeşitli köklü küçük bitkiler için ortak bir ad verir. Bu nedenle tanım belirli bir bitki türü değil, mevsimsel özellikleri ortak bir bitki kümesidir.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"yazın kalan, köklü küçük bitki veya çalı"}],"lexicalization_note":"Dal yalın bir bitki kümesi adıdır; belirli bir tür veya yalnız tek bir otla sınırlandırılmaz.","neighbor_coverage_note":"Bütün komşular değerlendirildi; yaz bitkisi ve hasat sonrası otlak karşılaştırmaları bu genel bitki kümesinin mevsim ve tür sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal mevsimsel olarak ortaya çıkan belirli yaz otunu anlatır; bu dal yazın kalan köklü çeşitli bitkilerin daha geniş ortak adıdır.","focus_only":"Yazın kalan ya da yazın gelişen köklü birçok küçük bitki ve çalıyı ortak ad altında toplar.","gloss":"yaz bitkisi","neighbor_only":"İlkbahar geçtikten sonra küçük ağaçların yeşermesiyle oluşan belirli yaz otlağını anlatır.","neighbor_ref":"root_000993/B011","relation_type":"near_synonym","shared_zone":"Her iki dal da ilkbahar sonrasındaki yaz döneminde görülen bitkileri kapsar."},{"boundary_match":"partial","distinction":"Komşu dal hasat sonrası tarla kalıntısına bağlıdır; bu dalın çekirdeği ise köklü küçük bitkilerin yazın varlığını sürdürmesidir.","focus_only":"Bitkileri köklü oluşları ve yaz boyunca kalmaları temelinde sınıflandırır.","gloss":"mevsim sonrasında kalan bitki örtüsü","neighbor_only":"Hasattan sonra tarlada kalan ekin artığını ve altından çıkan yeşil otu birlikte kapsar.","neighbor_ref":"root_000324/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal da asıl mevsim veya hasat sonrasında kalan bitki örtüsüne değinir."}],"source_phrase_ar":"الجنبة اسم يقع على عامة الشجر يترك في الصيف (ayn)؛ الجنبة ضرب من النبت (jamhara)؛ الجنبة اسم لكل نبت يتربل في الصيف (sihah)؛ الجنبة اسم واحد لنبوت كثيرة هي كلها عروة (tahdhib)","source_summary":"Anlam tek bir türe değil, yaz boyunca kalan veya yazın yeniden yeşeren çeşitli küçük bitkilere yönelir. Ortak özellikleri köklü olmaları ve yaz döneminde varlığını sürdürmeleri ya da yeniden gelişmeleridir.","sources":["AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الجنبة اسم عام لنبات يترك في الصيف أو يتربل فيه، مما له أرومة ويبقى في المحل ويعصم المال.","what_is_not_ar":"لا يدخل فيه الجنبة بمعنى الاعتزال ولا الجنب الجارحة."},"support_links":[]},{"boundary":"Dal genel olarak her örtüyü değil, kişinin yanında bulunan ve yanını koruyan kalkanı veya benzer koruyucu örtüyü belirtir.","branch_kind":"bare","branch_ref":"root_000262/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتَجَنَّبُ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:11:1:2","qac_word_ref":"87:11:1","surface_ar":"يَتَجَنَّبُ"}],"gloss":"yanı koruyan kalkan veya örtü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin yanında taşıdığı ve bedenini koruyan kalkanı belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalkan dışında koruyucu bir örtü için de kullanılabilir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalkan çekirdeğini ve kaynakta verilen daha geniş koruyucu örtü yorumunu birlikte yansıtmak için kullanılır.","boundary_detail":"Dal genel olarak her örtüyü değil, kişinin yanında bulunan ve yanını koruyan kalkanı veya benzer koruyucu örtüyü belirtir.","branch_image_ar":"المجنب وقاء إلى الجنب","concept_gloss":"yanı koruyan kalkan veya örtü","contextual_glosses":[{"applicability":"Savaşta veya savunmada kişinin yanında tuttuğu koruyucu kalkan özellikle kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalkanın koruyucu işlevini ve kişinin yanındaki konumunu korur."},"facet_ids":["F001"],"text":"kişinin yanında taşıdığı kalkan","usage_role":"contextual"}],"definition":"Kişinin yanında taşıdığı ve özellikle yanını koruduğu düşünülen kalkandır. Daha geniş bir kaynak yorumunda, aynı koruma işlevindeki bir örtüyü de belirtebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin yanında taşıdığı ve bedenini koruyan kalkanı belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Kalkan dışında koruyucu bir örtü için de kullanılabilir."}],"identity_rationale":"Kaynak ifadesi kişinin yanında bulunan kalkanı ortak anlam olarak verir ve bir kaynakta koruyucu örtü yorumunu da ekler. Yanında bulunma açıklaması nesnenin konumunu, kalkan ve örtü ise koruyucu işlevini birlikte destekler.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"kişinin yanında taşıdığı kalkan veya koruyucu örtü"}],"lexicalization_note":"Dal yalın bir koruyucu nesne adıdır; çokluk bildiren benzer biçimli söz öbeği veya atın beden yapısı bu tanıma katılmaz.","neighbor_coverage_note":"Bütün komşular değerlendirildi; genel kalkan ve genel koruyucu örtü dalları bu nesnenin konum ve işlev sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel koruyucu araç alanına yayılır; bu dal kalkanı kişinin yanındaki konumuyla sınırlar ve yalnız ikincil olarak örtüye uzanır.","focus_only":"Kalkanı kişinin yanındaki konumu ve yanını koruması üzerinden adlandırır; örtü yorumunu da taşır.","gloss":"koruyucu kalkan","neighbor_only":"Korunmak için kullanılan kalkanı, silahı veya herhangi bir koruyucu aracı genel olarak kapsar.","neighbor_ref":"root_000266/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin kendini korumak için kullandığı kalkanı kapsar."},{"boundary_match":"partial","distinction":"Komşu dal genel örtme ve saklama alanıdır; bu dal kişinin yanında taşıdığı savunma nesnesiyle sınırlıdır.","focus_only":"Kişinin yanında taşınan kalkanı temel alır.","gloss":"koruyucu örtü","neighbor_only":"Baş, eşya, tel veya gök gibi çok farklı şeyleri örten ve koruyan genel örtme eylemi ile nesnelerini kapsar.","neighbor_ref":"root_001096/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir şeyi örterek veya araya girerek koruyan nesne alanında buluşur."}],"source_phrase_ar":"سمي الترس مجنبا لأنه إلى جنب الإنسان (maqayis)؛ المجنب الترس (ayn;sihah;tahdhib)؛ المجنب الترس ويقال المجنب والمجنب الستر أيضا (jamhara)","source_summary":"Ortak karşılık kişinin yanında taşıdığı kalkandır; adlandırma nesnenin yandaki konumuyla açıklanır. Daha geniş tekil yorum, koruyucu örtüyü de aynı işlev alanına alır.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه المجنب بمعنى الترس، وما روي بمعنى الستر، باعتباره شيئا إلى جنب الإنسان أو يحمي جانبه.","what_is_not_ar":"لا يدخل فيه المجنب بمعنى الكثير ولا الفرس المجنب في الخلقة."},"support_links":[]},{"boundary":"Dal hareket sırasında bacağı yana atmayı değil, özellikle atın bacaklarında doğuştan bulunan ölçülü açıklık ve biçim özelliğini belirtir.","branch_kind":"bare","branch_ref":"root_000262/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتَجَنَّبُ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:11:1:2","qac_word_ref":"87:11:1","surface_ar":"يَتَجَنَّبُ"}],"gloss":"atın bacaklarında doğuştan ölçülü açıklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Atın iki bacağının doğuştan birbirinden uzak ve açık durmasını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bacakta eğrilik veya gerginlik görünümü bulunabilir, fakat açıklık aşırı ayrık bacaklılık değildir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Atın bacakları arasındaki yapısal uzaklığın doğuştan olduğu ve aşırı ayrıklığa varmadığı bağlamlarda kullanılır.","boundary_detail":"Dal hareket sırasında bacağı yana atmayı değil, özellikle atın bacaklarında doğuştan bulunan ölçülü açıklık ve biçim özelliğini belirtir.","branch_image_ar":"التجنيب تباعد في هيئة القوائم","concept_gloss":"atın bacaklarında doğuştan ölçülü açıklık","contextual_glosses":[{"applicability":"Bu doğuştan beden yapısını taşıyan atın doğrudan nitelenmesi gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Atın bacak açıklığını ve bunun aşırı olmadığı sınırını korur."},"facet_ids":["F001","F002"],"text":"bacakları ölçülü biçimde ayrık at","usage_role":"contextual"}],"definition":"Özellikle atın iki bacağının doğuştan birbirinden ölçülü biçimde uzak durduğu beden yapısıdır. Bacakta eğrilik veya gerginlik görünümü oluşturabilir, ancak aşırı ayrık bacaklılık düzeyine ulaşmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Atın iki bacağının doğuştan birbirinden uzak ve açık durmasını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Bacakta eğrilik veya gerginlik görünümü bulunabilir, fakat açıklık aşırı ayrık bacaklılık değildir."}],"identity_rationale":"Kaynak ifadesi atın bacağında eğrilik veya gerginlik görünümünü ve iki bacağın doğuştan birbirinden uzak durmasını destekler. Ayrıca bu açıklığın aşırı ayrık bacaklılık olmadığı açıkça sınırlandırılır.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"atın bacaklarının doğuştan birbirinden ayrı durması, fakat aşırı ayrık olmaması"}],"lexicalization_note":"Dal yalın bir beden yapısı niteliğidir; hayvanı yanda götürme eylemi veya ayrı bir yürüyüş biçimi tanıma katılmaz.","neighbor_coverage_note":"Bütün komşular değerlendirildi; genel ayrık bacak yapısı ile devenin bacak genişliği, at türü ve derece sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal beden bölgesi ve derece bakımından daha geniştir; bu dal ata özgüdür ve aşırı ayrıklığı özellikle dışlar.","focus_only":"Özellikle atın bacaklarındaki doğuştan ve aşırı olmayan açıklığı belirtir.","gloss":"bacak açıklığı","neighbor_only":"İnsan veya hayvanda aşık kemikleri, uyluklar ya da dizler arasındaki açıklığı ve bunun ağır derecesini kapsar.","neighbor_ref":"root_001133/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bacakların veya eklemlerin birbirinden uzak durduğu beden yapısını anlatır."},{"boundary_match":"partial","distinction":"Komşu dal deveye ve sırt yapısına uzanır; bu dal atın bacakları arasındaki doğuştan uzaklıkla sınırlıdır.","focus_only":"Atın iki bacağının birbirinden uzak durmasını ve eğrilik görünümünü belirtir.","gloss":"hayvan bacağında açıklık","neighbor_only":"Devenin bacağındaki hafif genişlik yanında sırtın yayvanlığını ve hörgüçsüzlüğü de kapsar.","neighbor_ref":"root_001143/B015","relation_type":"near_neighbor","shared_zone":"İki dal da bir hayvanın bacak yapısındaki açıklık veya yayvanlık niteliğine değinir."}],"source_phrase_ar":"التجنيب انحناء وتوتير في رجل الفرس (sihah)؛ المجنب من الخيل البعيد ما بين الرجلين من غير فجج والتجنيب بالجيم في الرجلين (tahdhib)؛ التجنيب الروح في الرجلين وذلك إبعاد إحدى الرجلين عن الأخرى خلقة (mufradat)","source_summary":"Ortak anlam, atın bacaklarının doğuştan birbirinden uzak durduğu bir beden yapısıdır. Görünüm eğrilik veya gerginlik olarak tarif edilir ve aşırı ayrıklıkla arasına açık bir sınır konur.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه التجنيب في رجل الفرس أو قوائمه، والمجنب من الخيل البعيد ما بين الرجلين من غير فجج، وما وصف بأنه إبعاد إحدى الرجلين عن الأخرى خلقة.","what_is_not_ar":"لا يدخل فيه قيادة الدابة إلى الجنب ولا الجنيبة المقادة."},"support_links":[]},{"boundary":"Dal, her türlü yorgunluğu değil, mutluluğun karşıtı sayılan mutsuzluk durumunu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000808/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:11:2:2","qac_word_ref":"87:11:2","surface_ar":"أَشْقَى"}],"gloss":"mutluluğun karşıtı olan mutsuzluk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, mutluluğun karşıtı olan mutsuzluk ve bahtsızlık durumudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu durum hem bu dünyadaki yaşam hem de ölümden sonraki yaşam bakımından değerlendirilebilir."}}],"root_ar":"ش ق و","root_id":"root_000808","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın temel durum anlamını, sıradan yorgunlukla karıştırmadan genel olarak karşılar.","boundary_detail":"Dal, her türlü yorgunluğu değil, mutluluğun karşıtı sayılan mutsuzluk durumunu anlatır.","branch_image_ar":"الشقاء ضد السعادة","concept_gloss":"mutluluğun karşıtı olan mutsuzluk","contextual_glosses":[{"applicability":"Mutsuzluk durumunun bu dünyadaki yaşam ve yaşantılar bakımından ele alındığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ölümden sonraki yaşama ilişkin kapsamı dışarıda bırakır.","preserves":"Mutluluğun karşıtı olan olumsuz yaşam durumu korunur."},"facet_ids":["F001","F002"],"text":"bu dünyadaki bahtsızlık","usage_role":"contextual"},{"applicability":"Mutsuzluk durumunun ölümden sonraki yaşam bakımından değerlendirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu dünyadaki yaşama ilişkin kapsamı dışarıda bırakır.","preserves":"Mutluluğun karşıtı olma ve ölüm sonrası kapsam birlikte korunur."},"facet_ids":["F001","F002"],"text":"ölümden sonraki yaşamda mutsuzluk","usage_role":"contextual"}],"definition":"Mutluluğun karşıtı olan mutsuzluk ya da bahtsızlık durumudur. Bu durum kişinin bu dünyadaki yaşamına da ölümden sonraki yaşamına da ilişkin olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, mutluluğun karşıtı olan mutsuzluk ve bahtsızlık durumudur."},{"facet_id":"F002","role":"extension","statement":"Bu durum hem bu dünyadaki yaşam hem de ölümden sonraki yaşam bakımından değerlendirilebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Mutluluğun karşıtı olmayan sıradan bedensel ya da zihinsel yorulmayı da kapsar.","collision":"Güçlük ve yorucu uğraş dalıyla anlam karışmasına yol açar.","fit":"broadening","loses":null,"preserves":"Olumsuz ve güçlük içeren bir yaşantı çağrışımını korur."},"text":"yorgunluk"}],"identity_rationale":"Yetkili kaynak ifadesi bu dalı doğrudan mutluluğun karşıtı olan durum diye belirler ve bu durumun hem bu dünyadaki yaşamda hem de ölümden sonraki yaşamda söz konusu olabileceğini bildirir. Bu nedenle verilen dal kimliği kaynak ifadesinin çekirdeğini ve kapsam ayrımını doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"mutsuzluk, bahtsızlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"mutsuz, bahtsız kimse"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"Tanrı onu mutsuzluğa düşürdü"}],"lexicalization_note":"Tanım, durum bildiren biçimlerin ortak anlamını temel alır; birini bu duruma sokma anlamı ise yalnızca ilgili ettirgen söyleyişe bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca güçlük dalı okur açısından doğrudan ve anlamlı bir sınır karşılaştırması sağladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın ölçütü mutluluğun karşıtı bir durumda bulunmaktır; komşu dalın ölçütü ise bir zorlukla uğraşmak, yorulmak ya da ona dayanmaktır. Bu yüzden her güçlük mutsuzluk sayılmaz.","focus_only":"Mutluluğun karşıtı olan genel yaşam durumunu ve iki yaşam alanındaki kapsamını belirtir.","gloss":"mutsuzluk ile güçlük çekme","neighbor_only":"Güçlük, yorulma, dayanma ve zorlu bir işle ya da kişiyle uğraşma anlamlarını kapsar.","neighbor_ref":"root_000808/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da olumsuz, yorucu ve kişiyi zorlayan bir yaşantı alanında buluşur."}],"source_phrase_ar":"الشقوة خلاف السعادة (maqayis)؛ الشقاء والشقاوة بالفتح: نقيض السعادة (sihah)؛ الشقاوة: خلاف السعادة، والشقاوة الأخروية والدنيوية (mufradat)","source_summary":"Kaynakların ortak çizgisi, anlamı mutluluğun karşıtı olan bir durum olarak kurar; kapsam, bu dünyadaki ve ölümden sonraki yaşamda görülen mutsuzluğu içerir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه الشقاء والشقوة والشقاوة بمعنى نقيض السعادة، وما يذكر في الشقاوة الأخروية والدنيوية.","what_is_not_ar":"لا يدخل مجرد التعب من حيث هو تعب أعم من الشقاوة، ولا المعنى المهموز شقأ ناب البعير."},"support_links":[]},{"boundary":"Dal, güçlük çekme çekirdeğiyle karşılıklı uğraşma kullanımlarını ayırır; her yorgunluğu ya da sonradan gelen yenme sonucunu kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000808/B002","candidate_links":[{"candidate_id":"cand_b4902bc5400ed6c2d9d6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:11:2:2","qac_word_ref":"87:11:2","surface_ar":"أَشْقَى"}],"gloss":"güçlük çekme ve zorluğa dayanma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, kolaylığın karşıtı olan güçlüğü çekmek ve zorluğa katlanmaktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlam yorgunluk yerine kullanılabilir; ancak her yorgunluk bu ölçüde bir güçlük çekme değildir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişiyle sabırla uğraşma, bir işi göğüsleme veya savaşta boğuşma yapıya bağlı kullanımlardır."}}],"root_ar":"ش ق و","root_id":"root_000808","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kolaylığın karşıtı olan uğraşma çekirdeğini, yapıya bağlı özel kullanımları genelleştirmeden karşılar.","boundary_detail":"Dal, güçlük çekme çekirdeğiyle karşılıklı uğraşma kullanımlarını ayırır; her yorgunluğu ya da sonradan gelen yenme sonucunu kapsamaz.","branch_image_ar":"مشقة العسر والمعاناة","concept_gloss":"güçlük çekme ve zorluğa dayanma","contextual_glosses":[{"applicability":"Güçlüğün kişide belirgin bir yorgunluk ve sıkıntı doğurduğu bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiyle ya da işle sabırla uğraşma ve savaşta boğuşma kapsamını vermez.","preserves":"Güçlük çekmenin yorucu ve sıkıntılı yönünü korur."},"facet_ids":["F001","F002"],"text":"sıkıntı çekip yorulma","usage_role":"contextual"},{"applicability":"Bir kişiyle veya zorlu bir işle sürdürülmüş uğraşı ve sabrı öne çıkaran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel güçlük durumu ile sırf yorulma kullanımını geri plana iter.","preserves":"Süreğen uğraşma ve zorluğa dayanma yönlerini korur."},"facet_ids":["F001","F003"],"text":"uğraşıp dayanma","usage_role":"contextual"},{"applicability":"Karşılıklı zorlu uğraşın savaş alanında gerçekleştiği özel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Savaş dışındaki güçlük, yorulma ve dayanma kullanımlarını dışarıda bırakır.","preserves":"Karşılıklı uğraşma ve güçlüğü göğüsleme yönlerini korur."},"facet_ids":["F003"],"text":"savaşta boğuşma","usage_role":"contextual"}],"definition":"Kolaylığın karşıtı olan güçlükle uğraşma, bunun sıkıntısını çekme ve ona dayanma durumudur. Kişiyle, işle ya da savaş gibi zorlu bir süreçle karşılıklı ve sürekli uğraşma bu çekirdeğin yapıya bağlı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, kolaylığın karşıtı olan güçlüğü çekmek ve zorluğa katlanmaktır."},{"facet_id":"F002","role":"specialization","statement":"Anlam yorgunluk yerine kullanılabilir; ancak her yorgunluk bu ölçüde bir güçlük çekme değildir."},{"facet_id":"F003","role":"associated_use","statement":"Bir kişiyle sabırla uğraşma, bir işi göğüsleme veya savaşta boğuşma yapıya bağlı kullanımlardır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Güçlükle bağlı olmayan sıradan bedensel ya da zihinsel yorulmayı da kapsar.","collision":"Dalın kolaylığın karşıtı olan uğraşma ve dayanma ölçütünü belirsizleştirir.","fit":"broadening","loses":null,"preserves":"Güçlüğün kişide bıraktığı yorucu etkiyi korur."},"text":"yalnızca yorgunluk"},{"category":"confusable","error_profile":{"adds":"Sürecin ardından gelen üstün gelme sonucunu temel anlam yapar.","collision":"Aynı kökün üstün gelme dalıyla karışır.","fit":"displacement","loses":"Güçlük çekme, uğraşma ve dayanma sürecini ortadan kaldırır.","preserves":"Karşılıklı bir uğraş veya çekişme ortamını dolaylı olarak çağrıştırır."},"text":"yenme"}],"identity_rationale":"Yetkili kaynak ifadesi anlam çekirdeğini uğraşma ve kolaylığın karşıtı olarak verir; ayrıca şiddetli güçlük, yorulma, dayanma, bir işi göğüsleme ve savaşta boğuşma kullanımlarını açıkça sıralar. Verilen dal kimliği bu öğeleri korur ve sıradan yorgunluk ile daha dar kapsamlı mutsuzluk arasındaki sınırı belirtmeye elverişlidir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"güçlük, sıkıntı ve yorucu uğraş"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bu işte yoruldum ve güçlük çektim"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"zorluğa katlanma, uğraşıp dayanma ve savaşta boğuşma"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"onunla uğraştım ve güçlüğüne katlandım"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"o işle uğraşıp güçlüğünü çektim"}],"lexicalization_note":"Genel güçlük ve yorulma anlamı biçim düzeyinde korunur; kişiyle çekişme, bir işe katlanma ve savaşta boğuşma anlamları yalnızca ilgili yapılı söyleyişlere bağlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; eş anlamlı olan dal ile süreç, kapsam veya sonuç sınırını aydınlatan üç aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda çekirdek, katılımcılar ve kapsam bakımından ayırıcı bir sınır görünmez; bu nedenle iki dal eş anlamlı değerlendirilir.","focus_only":null,"gloss":"güçlük, sıkıntı ve uğraşma","neighbor_only":null,"neighbor_ref":"root_000809/B002","relation_type":"synonym","shared_zone":"İki dal da şiddetli güçlük, yorulma ve bir işi uğraşarak göğüsleme alanını aynı sınırlarla kapsar."},{"boundary_match":"partial","distinction":"Bu dal güçlüğe katlanmayı ve kimi yapılarda karşılıklı uğraşmayı kapsar; komşu dal ise bir işin ya da yolun kişiye ağır gelmesini ve yoğun çabayla aşılmasını öne çıkarır.","focus_only":"Kişiyle karşılıklı uğraşma, sabırla dayanma ve savaşta boğuşma gibi yapıya bağlı kullanımları da kapsar.","gloss":"güçlük çekme ile ağır çaba","neighbor_only":"Yolda, işte veya bir amaca ulaşmada kişinin iç dünyasına ağır gelen yük ve çabayı öne çıkarır.","neighbor_ref":"root_000807/B003","relation_type":"near_synonym","shared_zone":"Her iki dalda da işin kolay olmayışı, çaba ve kişiye yük olan güçlük bulunur."},{"boundary_match":"partial","distinction":"Bu dal kolaylığın karşıtı olan daha geniş güçlük alanını ve karşılıklı uğraşı da içerir; komşu dalın odağı ise özellikle çetin bir işi göğüslemektir.","focus_only":"Genel güçlük ve yorulma durumuyla kişiyle karşılıklı uğraşma kapsamını içerir.","gloss":"zorluğa dayanma ile çetin işi göğüsleme","neighbor_only":"Özellikle şiddetli bir işi göğüsleyip onun eziyetine dayanmayı merkez alır.","neighbor_ref":"root_001227/B003","relation_type":"near_synonym","shared_zone":"İki dal da zor bir işi yaşayarak sürdürme ve onun yüküne katlanma anlamında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal sürecin güçlüğünü ve dayanmayı, komşu dal ise o süreçte üstün gelme sonucunu kodlar; süreç sonucu zorunlu olarak içermez.","focus_only":"Zorlu uğraşın sürmesi, çekilmesi ve ona dayanılması sürecini anlatır.","gloss":"uğraşma süreci ile yenme sonucu","neighbor_only":"Karşılıklı uğraşın sonunda öteki kişiyi yenme sonucunu anlatır.","neighbor_ref":"root_000808/B003","relation_type":"near_neighbor","shared_zone":"İki dal aynı karşılıklı ve zorlu uğraş senaryosunun farklı aşamalarına bağlanır."}],"source_phrase_ar":"أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (maqayis;sihah)؛ الشقاء: الشدة والعسر، وشاقيته أي صابرته، وشاقيت ذلك الأمر بمعنى عانيته، والمشاقاة: المعالجة في الحرب وغيرها (tahdhib)؛ يوضع الشقاء موضع التعب، وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)","source_summary":"Kaynakların birleşen anlatımı, kolaylığın karşısındaki güçlük ve uğraşma çekirdeğini; yorulma, dayanma, işi göğüsleme ve savaşta boğuşma gibi bağlı gerçekleşmelerle birlikte verir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الشقاء بمعنى الشدة والعسر والتعب، والمشاقاة بمعنى المعاناة والممارسة والصبر والمعالجة في الحرب وغيرها، وعشرة المرء غيره في هذا الباب.","what_is_not_ar":"لا يدخل نقيض السعادة إذا كان المقصود حكما وجوديا أو أخرويا خالصا، ولا الغلبة بعد المشاقاة."},"support_links":["sup_24be94ddce34b7dac6ce"]},{"boundary":"Anlam, herhangi bir yenmeye değil, belirtilen karşılıklı uğraş yapısında ötekine üstün gelmeye bağlıdır.","branch_kind":"collocation","branch_ref":"root_000808/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:11:2:2","qac_word_ref":"87:11:2","surface_ar":"أَشْقَى"}],"gloss":"karşılıklı uğraşta ötekini yenme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Karşılıklı uğraşın sonunda konuşan, öteki kişiye aynı uğraş alanında üstün gelir."}}],"root_ar":"ش ق و","root_id":"root_000808","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kaynakta verilen ardışık karşılıklı uğraş ve üstün gelme yapısını tam olarak karşılar.","boundary_detail":"Anlam, herhangi bir yenmeye değil, belirtilen karşılıklı uğraş yapısında ötekine üstün gelmeye bağlıdır.","branch_image_ar":"الغلبة في المشاقاة","concept_gloss":"karşılıklı uğraşta ötekini yenme","contextual_glosses":[{"applicability":"Yapının iki katılımcısını ve uğraştan üstün gelmeye uzanan sırasını açıkça göstermek gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki katılımcı, karşılıklı çekişme ve konuşanın yenmesi tam olarak korunur."},"facet_ids":["F001"],"text":"benimle çekişti, ben de onu yendim","usage_role":"explanatory"}],"definition":"Bir kişinin konuşanla belirli bir uğraş alanında çekişmesinin ardından konuşanın onu aynı alanda yenmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Karşılıklı uğraşın sonunda konuşan, öteki kişiye aynı uğraş alanında üstün gelir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Aynı kökün güçlük ve uğraşma dalıyla karışır.","fit":"narrowing","loses":"Konuşanın öteki kişiyi aynı alanda yenmesi sonucunu vermez.","preserves":"Karşılıklı sürecin uğraş ve çekişme yönünü korur."},"text":"uğraşma"}],"identity_rationale":"Yetkili kaynak ifadesi, bir kişinin konuşana aynı uğraş alanında karşılık vermesini ve konuşanın onu o alanda yenmesini açıkça ardışık bir yapı içinde verir. Verilen dal kimliği bu sonucu doğru biçimde yakalar ve onu yalnızca uğraşma sürecinden ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"benimle çekişti, ben de o işte onu yendim"}],"lexicalization_note":"Tanım yalnızca birinin konuşanla belirli bir alanda uğraşması ve konuşanın onu aynı alanda yenmesi biçimindeki yapıya bağlıdır; yalın kök anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; süreç dalı, tam eş anlamlı yapı ve daha genel üstün gelme dalı sınırı açıklayan adaylar olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal uğraşın üstün gelmeyle biten sonucudur; komşu dal ise uğraşın ve dayanmanın kendisidir, dolayısıyla yenmeyi gerektirmez.","focus_only":"Karşılıklı uğraşta konuşanın öteki kişiyi yenmesi sonucunu kodlar.","gloss":"yenme sonucu ile uğraşma süreci","neighbor_only":"Güçlük çekme, karşılıklı uğraşma ve zorluğa dayanma sürecini sonuçtan bağımsız anlatır.","neighbor_ref":"root_000808/B002","relation_type":"near_neighbor","shared_zone":"İki dal da aynı zorlu ve karşılıklı uğraş senaryosuna katılır."},{"boundary_match":"exact","distinction":"Verilen kartlara göre işlem sırası, katılımcılar ve sonuç bakımından ayırıcı bir sınır yoktur; iki yapı aynı kavramsal içeriği taşır.","focus_only":null,"gloss":"karşılıklı uğraşta yenme","neighbor_only":null,"neighbor_ref":"root_000569/B005","relation_type":"synonym","shared_zone":"İki dal da belirli bir alandaki karşılıklı uğraşın konuşanın ötekini yenmesiyle sonuçlanmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal yalnızca belirtilen karşılıklı uğraş yapısında işler; komşu dal ise üstün gelmeyi ve kazanmayı böyle bir ön koşul olmadan daha genel biçimde kapsar.","focus_only":"Yenme anlamını belirli bir karşılıklı uğraşı önceleyen ve konuşanı galip yapan yapıya bağlar.","gloss":"yapıya bağlı yenme ile genel zafer","neighbor_only":"Zafer, ele geçirme ve rakibi alt etme sonucunu daha genel bir kapsamda anlatır.","neighbor_ref":"root_000965/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir rakibe üstün gelme ve onu yenme sonucu vardır."}],"source_phrase_ar":"شاقاني فلان فشقوته أشقوه، أي غلبته فيه (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak tanıklığı, birinin konuşanla uğraşmasını ve konuşanın onu aynı alanda yenmesini ardışık olarak verir."}],"source_summary":"Dal, karşılıklı uğraşın kendisini değil, bu uğraşın konuşanın üstün gelmesiyle sonuçlanan aşamasını anlatır.","sources":["SI"],"what_is_ar":"يدخل فيه قولهم شاقاني فلان فشقوته، أي غلبته في ذلك الباب.","what_is_not_ar":"لا يدخل أصل المعاناة والممارسة بلا معنى الغلبة."},"support_links":[]},{"boundary":"Dal genel olarak her yüksek dağı değil, uzun, kolay çıkılan ve oturmaya elverişli belirli bir dağ sırtını anlatır.","branch_kind":"bare","branch_ref":"root_000808/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:11:2:2","qac_word_ref":"87:11:2","surface_ar":"أَشْقَى"}],"gloss":"uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, dağın yükselen ve uzun bir sırtıdır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uzunluğuna karşın bu sırtın çıkışı görece kolaydır."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sırt, insanın oturmasına daha elverişli bir yer sağlar."}}],"root_ar":"ش ق و","root_id":"root_000808","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yer biçimini, uzunluğunu, çıkılabilirliğini ve oturma elverişliliğini birlikte karşılar.","boundary_detail":"Dal genel olarak her yüksek dağı değil, uzun, kolay çıkılan ve oturmaya elverişli belirli bir dağ sırtını anlatır.","branch_image_ar":"شاقي الجبل الطالع الطويل","concept_gloss":"uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı","contextual_glosses":[{"applicability":"Yol alma ve tırmanma kolaylığının öne çıktığı bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanın oturmasına elverişli olma niteliğini belirtmez.","preserves":"Dağ sırtı olma, uzunluk ve kolay çıkış niteliklerini korur."},"facet_ids":["F001","F002"],"text":"çıkması kolay uzun dağ sırtı","usage_role":"contextual"},{"applicability":"Bir insanın durup oturabileceği yer niteliğinin öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sırtın uzunluğunu ve çıkışının görece kolay oluşunu tam belirtmez.","preserves":"Dağ sırtı olma, yükselme ve oturmaya elverişlilik niteliklerini korur."},"facet_ids":["F001","F003"],"text":"oturmaya elverişli yüksek dağ sırtı","usage_role":"contextual"}],"definition":"Dağın yükselen ve uzun bir sırtıdır; uzun olmasına karşın çıkılması görece kolaydır ve insana oturmak için elverişli bir yer sağlar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, dağın yükselen ve uzun bir sırtıdır."},{"facet_id":"F002","role":"core","statement":"Uzunluğuna karşın bu sırtın çıkışı görece kolaydır."},{"facet_id":"F003","role":"core","statement":"Sırt, insanın oturmasına daha elverişli bir yer sağlar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Sırt olmayan ve çıkışı ya da oturma elverişliliği belirtilmeyen her yüksek dağı kapsar.","collision":"Genel yükseklik bildiren dağ dallarıyla karışır.","fit":"broadening","loses":null,"preserves":"Dağlık yer ve yükselti özelliklerini genel olarak korur."},"text":"yüksek dağ"}],"identity_rationale":"Yetkili kaynak ifadesi dağ sırtının yükselen ve uzun olduğunu, uzunluğuna karşın çıkışının daha kolay ve insanın oturmasına daha elverişli bulunduğunu açıkça belirtir. Verilen dal kimliği bu dört kurucu niteliği ve yer biçimini doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı; bu tür dağ sırtları"}],"lexicalization_note":"Tanım, tek başına kullanılan dağ sırtı adının niteliklerini verir; başka bir yapıya bağlı anlam veya öteki dalların soyut anlamları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eş anlamlı dal, genel yükseklik ve dağın bütünü ya da orta kesimi en açıklayıcı karşılaştırmaları sağladı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda gönderge, nitelikler ve kapsam bakımından ayırıcı bir sınır bulunmadığından iki dal eş anlamlıdır.","focus_only":null,"gloss":"uzun ve kolay çıkılan dağ sırtı","neighbor_only":null,"neighbor_ref":"root_000809/B004","relation_type":"synonym","shared_zone":"İki dal da uzun, yükselen, çıkışı kolay ve insanın oturmasına elverişli aynı dağ sırtı türünü anlatır."},{"boundary_match":"partial","distinction":"Bu dal somut bir dağ sırtı türüdür ve erişim ile oturma niteliklerini gerektirir; komşu dal ise nesne türünü ve bu ek nitelikleri sınırlamayan genel yüksekliktir.","focus_only":"Belirli bir dağ sırtını uzunluk, kolay çıkış ve oturma elverişliliğiyle birlikte tanımlar.","gloss":"özel dağ sırtı ile genel yükseklik","neighbor_only":"Dağ veya başka bir varlıktaki yükselme ve uzunluğu genel olarak belirtir.","neighbor_ref":"root_000824/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da yükselme ve uzunluk niteliği bulunur."},{"boundary_match":"field_only","distinction":"Bu dal biçimi ve kullanım elverişliliği belirlenmiş bir sırtı anlatır; komşu dal ise bütün dağı ya da dağın orta kesimini gösterir.","focus_only":"Uzun, çıkışı kolay ve oturmaya elverişli bir dağ sırtı türünü gösterir.","gloss":"dağ sırtı ile dağ ve orta kesimi","neighbor_only":"Dağın kendisini veya dağların orta kesimini adlandırır.","neighbor_ref":"root_000840/B017","relation_type":"same_field","shared_zone":"İki dal da dağlık araziyi ve dağın bölümlerini adlandıran aynı kavram alanındadır."}],"source_phrase_ar":"الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak tanıklığı bu sırtı yükselen ve uzun, fakat çıkışı kolay ve insanın oturmasına elverişli olarak niteler."}],"source_summary":"Dal, biçimsel ve kullanımsal nitelikleri birlikte verilen özel bir dağ sırtı türünü anlatır.","sources":["AY"],"what_is_ar":"يدخل فيه الشاقي من حيود الجبال: الطالع الطويل الذي، مع طوله، يكون أيسر صعودا وأقدر مقعدا للإنسان، وجمعه شاقيات وشواقي.","what_is_not_ar":"لا يدخل الشقاء بمعنى ضد السعادة، ولا المشاقاة والمعاناة."},"support_links":[]},{"boundary":"Dal, her türlü yorgunluğu veya güçlüğü değil, mutluluğun karşıtı olan durumu ve bu duruma düşürmeyi anlatır.","branch_kind":"bare","branch_ref":"root_000809/B001","candidate_links":[{"candidate_id":"cand_e1e0a6115ea9277889eb","lane":"micro"},{"candidate_id":"cand_c91955913c19c6a61c96","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:11:2:2","qac_word_ref":"87:11:2","surface_ar":"أَشْقَى"}],"gloss":"bedbahtlık ve bedbaht duruma düşürme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kimsenin mutluluğun karşıtı olan bedbaht bir durumda bulunmasıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgen kullanımda bir kimseyi bedbaht duruma düşürmeyi anlatır."}}],"root_ar":"ش ق و","root_id":"root_000809","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem durum bildiren çekirdeğini hem de aynı anlam alanındaki ettirgen uzantısını birlikte karşılar.","boundary_detail":"Dal, her türlü yorgunluğu veya güçlüğü değil, mutluluğun karşıtı olan durumu ve bu duruma düşürmeyi anlatır.","branch_image_ar":"الشقاوة وخلاف السعادة","concept_gloss":"bedbahtlık ve bedbaht duruma düşürme","contextual_glosses":[{"applicability":"Bir kişinin mutluluğun karşıtı olan durumunu adlandıran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin mutluluğun karşıtı olan durumunu tam olarak korur."},"facet_ids":["F001"],"text":"bedbahtlık","usage_role":"general"},{"applicability":"Birinin başka birini bu olumsuz duruma soktuğu ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir kimseyi bedbaht duruma sokma işlemini açıkça korur."},"facet_ids":["F002"],"text":"bedbaht duruma düşürmek","usage_role":"contextual"}],"definition":"Mutluluğun karşıtı olan bedbahtlık durumu ve bir kimseyi bu duruma düşürmedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kimsenin mutluluğun karşıtı olan bedbaht bir durumda bulunmasıdır."},{"facet_id":"F002","role":"extension","statement":"Ettirgen kullanımda bir kimseyi bedbaht duruma düşürmeyi anlatır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bedensel veya zihinsel yorulmanın genel anlamını ekler.","collision":"Güçlük ve yorulma dalıyla karışır.","fit":"displacement","loses":"Mutluluğun karşıtı olan kalıcı durum ile ettirgen uzantıyı kaybeder.","preserves":"Olumsuz bir insan deneyimini adlandırma özelliğini korur."},"text":"yorgunluk"}],"identity_rationale":"Kaynak ifadesi bu dalı mutluluğun karşıtı olan bedbahtlık durumu etrafında kurar; kişinin bu durumda bulunmasını ve bir başkasının onu bu duruma düşürmesini de aynı anlam alanına bağlar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bedbaht olmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bedbahtlık"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bedbahtlık"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bu dünyada veya ölümden sonraki yaşamda bedbahtlık"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onu bedbaht duruma düşürmek"}],"lexicalization_note":"Yalın dal, bedbaht olma durumunu ve aynı kökten gelen ettirgen biçimi kapsar; güçlük ve yorulma dalındaki kullanımlar buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca bedbahtlıkla anlam, neden veya sonuç bakımından gerçek karışma ihtimali taşıyan üç karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal mutluluğun karşıtı olan bedbahtlık durumudur; komşu dal ise özellikle üzüntüye, hoşnutsuzluğa ve istenmeyen bir sonuca yönelir.","focus_only":"Bedbahtlığı mutluluğun karşıtı olan genel bir durum olarak ve ettirgen uzantısıyla kapsar.","gloss":"üzüntü ve bedbahtlık","neighbor_only":"Üzüntü, hoşnutsuzluk ve istenmeyen bir durumun başa gelmesi üzerinde durur.","neighbor_ref":"root_000079/B003","relation_type":"near_synonym","shared_zone":"İkisi de kişinin ağır ve olumsuz ruhsal ya da yaşamsal durumunu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal bir kişinin mutluluk karşısındaki durumunu belirtir; komşu dal ise yaşanan işin zorluğunu ve harcanan çabayı öne çıkarır.","focus_only":"Mutluluğun karşıtı olan bedbahtlık durumunu ve birini bu duruma düşürmeyi anlatır.","gloss":"bedbahtlık ile güçlük","neighbor_only":"Güçlük, zorluk, yorulma ve bir işle uğraşıp ona katlanmayı anlatır.","neighbor_ref":"root_000809/B002","relation_type":"near_neighbor","shared_zone":"Ağır güçlükler bedbahtlıkla birlikte görülebilir ve iki dal bazı bağlamlarda birbirini çağrıştırır."},{"boundary_match":"field_only","distinction":"Bedbahtlık umut bulunup bulunmamasına bağlı değildir; komşu dalın çekirdeği ise beklentinin ve umudun sona ermesidir.","focus_only":"Mutluluğun karşıtı olan genel bedbahtlık durumunu kapsar.","gloss":"bedbahtlık ve umutsuzluk","neighbor_only":"Bir şeyden, iyilikten veya merhametten umut kesmeyi bildirir.","neighbor_ref":"root_001261/B001","relation_type":"same_field","shared_zone":"Her ikisi de kişinin olumsuz bir yaşamsal ya da ruhsal durumda bulunmasıyla ilgilidir."}],"source_phrase_ar":"الشقوة خلاف السعادة (maqayis)؛ شقي شقاء وشقوة وأصل الشقاء والشقوة (ayn)؛ الشقاء والشقاوة نقيض السعادة وأشقاه الله (sihah)؛ شقي شقاء وشقاوة وشقوة (tahdhib)؛ الشقاوة خلاف السعادة (mufradat)","source_summary":"Kaynakların ortak çekirdeği, mutluluğun karşıtı olan bedbahtlık ve bu durumda bulunan kişidir; ettirgen biçim de birini bu duruma düşürür.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الشقاء والشقوة والشقاوة وحال الشقي وإشقاؤه","what_is_not_ar":"ليس مطلق التعب الأعم ولا المعنى المهموز في شقأ ناب البعير"},"support_links":["sup_0793f3c648ae91665955","sup_c001808549ecea3473b5"]},{"boundary":"Yalın güçlük anlamı ile belirli bir işte yorulma veya o işle uğraşma biçimleri ayrı tutulmalı; dal genel yorgunlukla özdeşleştirilmemelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000809/B002","candidate_links":[{"candidate_id":"cand_b4902bc5400ed6c2d9d6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:11:2:2","qac_word_ref":"87:11:2","surface_ar":"أَشْقَى"}],"gloss":"zorluk ve yorucu uğraş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kolaylığın karşıtı olan güçlük, zorluk ve sıkıntıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yorgunluk anlamında da kullanılabilir, ancak genel olarak her yorgunluğu kapsamaz."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yalın olmayan biçimlerde belirli bir işi yaşayarak sürdürme, onunla uğraşma ve ona katlanmadır."}}],"root_ar":"ش ق و","root_id":"root_000809","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın güçlük çekirdeğini ve belirli bir işe bağlanan uğraşma ile katlanma biçimlerini birlikte özetler.","boundary_detail":"Yalın güçlük anlamı ile belirli bir işte yorulma veya o işle uğraşma biçimleri ayrı tutulmalı; dal genel yorgunlukla özdeşleştirilmemelidir.","branch_image_ar":"الشدة والعسر والعناء","concept_gloss":"zorluk ve yorucu uğraş","contextual_glosses":[{"applicability":"Yalın biçimin kolaylığın karşıtı olan durum veya deneyimi anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kolaylığın karşıtı olan zorlu ve sıkıntılı durumu korur."},"facet_ids":["F001"],"text":"güçlük ve sıkıntı","usage_role":"general"},{"applicability":"Belirli bir iş yüzünden yorulmayı veya o işte güçlük çekmeyi anlatan kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yorgunluğu belirli bir işte yaşanan güçlüğe bağlı olarak korur."},"facet_ids":["F002"],"text":"bir işte yorulmak","usage_role":"contextual"},{"applicability":"Yalın olmayan biçimin bir işi yaşayarak sürdürme ve onun güçlüğünü çekme anlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir işle uğraşma, onu sürdürme ve güçlüğüne katlanma öğelerini korur."},"facet_ids":["F003"],"text":"bir işle uğraşıp ona katlanmak","usage_role":"explanatory"}],"definition":"Kolaylığın karşıtı olan güçlük, zorluk ve bunların doğurduğu yorucu yaşantıdır. Yalın olmayan kullanımlarda belirli bir işle uğraşmayı, onu yaşayarak sürdürmeyi ve ona katlanmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kolaylığın karşıtı olan güçlük, zorluk ve sıkıntıdır."},{"facet_id":"F002","role":"source_variant","statement":"Yorgunluk anlamında da kullanılabilir, ancak genel olarak her yorgunluğu kapsamaz."},{"facet_id":"F003","role":"specialization","statement":"Yalın olmayan biçimlerde belirli bir işi yaşayarak sürdürme, onunla uğraşma ve ona katlanmadır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Her türlü yorgunluğun bu dala girdiği izlenimini verebilir.","fit":"narrowing","loses":"Kolaylık karşıtı güçlüğü ve belirli bir işle uğraşıp ona katlanma kapsamını kaybeder.","preserves":"Zorlu yaşantının yorucu yönünü korur."},"text":"yorgunluk"}],"identity_rationale":"Kaynak ifadesi güçlük, zorluk ve kolaylığın karşıtı olan yaşantıyı doğrular; ayrıca bir işle uğraşma ve ona katlanma biçimlerini verir. Bununla birlikte yorgunluk kullanımı sınırlıdır: bu kapsamdaki her durum yorucu olabilir, fakat her yorgunluk bu dala girmez.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"güçlük, zorluk ve yorucu sıkıntı"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir işte yorulmak veya güçlük çekmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"uğraşma, yaşayarak sürdürme ve katlanma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bir işle uğraşmak ve ona katlanmak"}],"lexicalization_note":"Dal, yalın biçimde güçlük ve zorluğu; yalın olmayan biçimlerde ise belirli bir işte yorulmayı, o işi yaşayarak sürdürmeyi ve ona katlanmayı ayrı yüzler olarak kapsar.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlanan üç yakın anlamlı dal, genel zorluk, kişiye ağır gelme ve ağır işe katlanma sınırlarını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel güçlükten belirli bir işle uğraşmaya uzanır; komşu dalın belirleyici yanı ise işin kişiye ağır gelmesi ve büyük güçlükle yapılmasıdır.","focus_only":"Güçlüğün yanı sıra belirli bir işle uğraşma, onu sürdürme ve ona katlanma biçimlerini kapsar.","gloss":"zorluk ve ağır gelme","neighbor_only":"Yürüyüşte veya işte insanın iç dünyasına ağır gelen yükü ve işi büyük güçlükle başarmayı vurgular.","neighbor_ref":"root_000807/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da çaba gerektiren, yorucu ve kolay olmayan bir deneyimi anlatır."},{"boundary_match":"partial","distinction":"Odak dal daha genel bir kolaylık karşıtlığına sahiptir; komşu dal ise ağır işin bizzat çekilmesini ve ona dayanmayı merkezleştirir.","focus_only":"Kolaylığın karşıtı olan genel güçlüğü ve bazı biçimlerde yorgunluğu kapsar.","gloss":"güçlük ve çetin işe katlanma","neighbor_only":"Ağır bir işi çekip katlanma ve onunla boğuşma yönünü daha belirgin taşır.","neighbor_ref":"root_001280/B002","relation_type":"near_synonym","shared_zone":"İki dal da zorluk, sıkıntı ve bir işi yaşayarak sürdürme alanında geniş ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal genel zorluğu doğrudan niteler; odak dal ise bu zorluğun yaşanmasını, yorgunluğu ve işle uğraşmayı da kapsayan karma bir yapıya sahiptir.","focus_only":"Yorucu yaşantı ile belirli bir işle uğraşma ve ona katlanma uzantılarını içerir.","gloss":"güçlük ve zorluk","neighbor_only":"Zor bir işi veya zor bir günü, yaşanan çaba ve katlanma sürecini gerektirmeden niteleyebilir.","neighbor_ref":"root_001012/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde kolaylığın karşıtı olan güçlük ve zorluk bulunur."}],"source_phrase_ar":"أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (sihah)؛ الشقاء الشدة والعسر وشاقيت ذلك الأمر بمعنى عانيته (tahdhib)؛ يوضع الشقاء موضع التعب وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)","source_summary":"Kaynakların ortak çerçevesi kolaylığın karşıtı olan güçlük ve zorluktur; buna yorucu yaşantı ile belirli bir işle uğraşma, onu sürdürme ve ona katlanma kullanımları eklenir. Yorgunlukla bağ kurulsa da her yorgunluk bu anlamı taşımaz.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الشدة والعسر والتعب الذي يسمى شقاء ومعاناة الأمر وممارسته","what_is_not_ar":"ليس التعب الأعم كله شقاوة ولا المعنى المهموز في شقأ ناب البعير"},"support_links":["sup_24be94ddce34b7dac6ce"]},{"boundary":"Dal yalnızca bir kişinin bedbahtlığı veya genel yorgunluk değildir; mutlaka başka bir kişiyle kurulan ilişki, dayanışma ya da karşılaşma yapısına bağlıdır.","branch_kind":"non_bare","branch_ref":"root_000809/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:11:2:2","qac_word_ref":"87:11:2","surface_ar":"أَشْقَى"}],"gloss":"biriyle karşılıklı uğraşıp mücadele etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başka bir kişiyle karşılıklı ilişki ve uğraş içinde olmaktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşı tarafa dayanma, onunla mücadele etme ve özellikle savaşta onunla uğraşmadır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Rekabetli kullanımda karşı tarafla çekişip onu söz konusu işte alt etmeye uzanır."}}],"root_ar":"ش ق و","root_id":"root_000809","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişiye bağlı biçimlerin karşılıklı ilişki, dayanma ve mücadele çekirdeğini karşılar; yenme sonucu bunun rekabetli uzantısıdır.","boundary_detail":"Dal yalnızca bir kişinin bedbahtlığı veya genel yorgunluk değildir; mutlaka başka bir kişiyle kurulan ilişki, dayanışma ya da karşılaşma yapısına bağlıdır.","branch_image_ar":"المشاقاة مصابرة ومعالجة","concept_gloss":"biriyle karşılıklı uğraşıp mücadele etme","contextual_glosses":[{"applicability":"İki kişinin ilişki veya işlem içinde birbirleriyle uğraştığı genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başka bir kişiyle kurulan karşılıklı ilişki ve uğraş yapısını korur."},"facet_ids":["F001"],"text":"biriyle karşılıklı uğraşmak","usage_role":"general"},{"applicability":"Karşı tarafa dayanma ve özellikle çatışmada onunla mücadele etme bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşı tarafa dayanma ve onunla mücadele etme yönlerini korur."},"facet_ids":["F002"],"text":"birine karşı direnip mücadele etmek","usage_role":"contextual"},{"applicability":"Karşılıklı çekişmenin odak kişisinin üstün gelmesiyle sonuçlandığı kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşı tarafla çekişme ve onu söz konusu işte alt etme sonucunu korur."},"facet_ids":["F003"],"text":"çekişmede onu yenmek","usage_role":"contextual"}],"definition":"Bir kişiyle karşılıklı ilişki içinde olma, ona karşı dayanma ve özellikle savaş gibi ortamlarda onunla uğraşıp mücadele etmedir. Rekabetli kullanımda bu süreç karşı tarafı bir işte alt etme sonucuna ulaşabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başka bir kişiyle karşılıklı ilişki ve uğraş içinde olmaktır."},{"facet_id":"F002","role":"specialization","statement":"Karşı tarafa dayanma, onunla mücadele etme ve özellikle savaşta onunla uğraşmadır."},{"facet_id":"F003","role":"extension","statement":"Rekabetli kullanımda karşı tarafla çekişip onu söz konusu işte alt etmeye uzanır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Her türlü galibiyetin bu dala girdiği izlenimini verebilir.","fit":"narrowing","loses":"Karşılıklı ilişkiyi, uğraşmayı, dayanmayı ve mücadele sürecini kaybeder.","preserves":"Rekabetli kullanımın üstün gelme sonucunu korur."},"text":"yenmek"}],"identity_rationale":"Kaynak ifadesi bir kişiyle karşılıklı ilişki ve uğraş içinde olmayı, ona karşı sabretmeyi ve özellikle çatışma ortamında onunla mücadele etmeyi birlikte verir; rekabetli kullanımda karşı tarafı yenme sonucu da açıkça tanıklanır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"biriyle ilişki kurup ona karşı direnmek veya onunla uğraşmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"benimle çekişti, ben de onu o işte yendim"}],"lexicalization_note":"Anlam, kişi alan biçimlere bağlıdır: biriyle karşılıklı ilişki kurma, ona karşı dayanma veya mücadele etme ve çekişmede onu yenme kullanımları yalın kök anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma, dalın genel uğraşmadan, çetin işe katlanmadan ve düzenli yarışmadan ayrılan kişiler arası yapısını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişiyle kurulan karşılıklı ilişki ve direnme yapısına bağlıdır; komşu dal ise daha genel biçimde bir şeyi işlemeyi, denemeyi veya başkasıyla çekişmeyi kapsar.","focus_only":"Başka bir kişiyle karşılıklı ilişki kurmayı ve ona karşı dayanmayı açıkça içerir.","gloss":"karşılıklı uğraşma ve bir şeyi işleme","neighbor_only":"Bir şeyi deneme ve onunla uğraşma, karşılıklı bir kişi ilişkisi bulunmadan da gerçekleşebilir.","neighbor_ref":"root_000655/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi veya işle uğraşmayı, onu sürdürmeyi ve kimi bağlamlarda karşı tarafı aşmayı anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal kişiler arası karşılıklılığı merkez alır; komşu dalın çekirdeği ise ağır işin kendisini çekmek ve onun güçlüğüne katlanmaktır.","focus_only":"Başka bir kişiyle karşılıklı ilişki, direnme ve çekişme yapısını gerektirir.","gloss":"kişiye karşı mücadele ve çetin işle uğraşma","neighbor_only":"Çetin bir işi çekip onunla uğraşmayı, başka bir kişi bulunmadan da anlatabilir.","neighbor_ref":"root_001227/B003","relation_type":"near_neighbor","shared_zone":"İki dalda da zorlu bir süreçle uğraşma, dayanma ve işi sürdürme düşüncesi vardır."},{"boundary_match":"partial","distinction":"Odak dal genel karşılıklı ilişki ve mücadeleden bir tarafın üstün gelmesine uzanır; komşu dal ise gidip gelen üstünlükle kurulan yarışmayı belirginleştirir.","focus_only":"İlişki kurma ve karşı tarafa dayanma gibi rekabet dışı kullanımlara da sahiptir.","gloss":"karşılıklı mücadele ve yarışma","neighbor_only":"Tarafların sırayla üstün geldiği düzenli yarışma ve karşılıklı övünme görünümlerini kapsar.","neighbor_ref":"root_000677/B002","relation_type":"near_neighbor","shared_zone":"Her ikisi de iki tarafın birbirine karşı çaba gösterdiği mücadele veya yarışma ortamında kullanılabilir."}],"source_phrase_ar":"المشاقاة المعاناة والممارسة (maqayis;sihah)؛ شاقاني فلان فشقوته أي غلبته فيه (sihah)؛ شاقيت فلانا مشاقاة إذا عاشرته وعاشرك (tahdhib)؛ شاقيته أي صابرته والمشاقاة المعالجة في الحرب وغيرها (tahdhib)","source_summary":"Kaynaklar karşılıklı uğraşma ve işi birlikte ya da karşı karşıya yaşayarak sürdürme çekirdeğinde birleşir. Kişiyle ilişki kurma, ona karşı dayanma, savaşta mücadele etme ve çekişmenin sonunda onu alt etme bu çekirdeğin bağlama bağlı görünümleridir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه مشاقاة الإنسان معاشرة ومصابرة ومعالجة في الحرب وغيرها ومغالبة الآخر في الأمر","what_is_not_ar":"ليس مجرد الشقاء خلاف السعادة ولا الشقاء بمعنى التعب العام"},"support_links":[]},{"boundary":"Dal genel olarak dağı, yükseltiyi veya geçidi değil, belirtilen çıkış ve oturma özelliklerine sahip uzun bir dağ sırtını adlandırır.","branch_kind":"bare","branch_ref":"root_000809/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:11:2:2","qac_word_ref":"87:11:2","surface_ar":"أَشْقَى"}],"gloss":"kolay çıkılan, oturmaya elverişli uzun dağ sırtı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dağın yükselen ve uzun bir sırtıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uzunluğuna rağmen çıkılması daha kolay ve insanın oturmasına daha elverişlidir."}}],"root_ar":"ش ق و","root_id":"root_000809","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yeryüzü biçimini uzunluk, yükseliş, çıkış kolaylığı ve oturmaya elverişlilik özellikleriyle birlikte karşılar.","boundary_detail":"Dal genel olarak dağı, yükseltiyi veya geçidi değil, belirtilen çıkış ve oturma özelliklerine sahip uzun bir dağ sırtını adlandırır.","branch_image_ar":"الشاقي من حيود الجبال","concept_gloss":"kolay çıkılan, oturmaya elverişli uzun dağ sırtı","contextual_glosses":[{"applicability":"Bir dağ üzerindeki belirli yeryüzü biçiminin özelliklerini açıklayan coğrafi bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uzun sırt biçimini, tırmanma kolaylığını ve oturmaya uygunluğu korur."},"facet_ids":["F001","F002"],"text":"kolay tırmanılan ve oturmaya uygun uzun sırt","usage_role":"explanatory"}],"definition":"Dağın yükselen ve uzun, fakat uzunluğuna rağmen çıkılması daha kolay ve insanın oturmasına daha elverişli sırtıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dağın yükselen ve uzun bir sırtıdır."},{"facet_id":"F002","role":"specialization","statement":"Uzunluğuna rağmen çıkılması daha kolay ve insanın oturmasına daha elverişlidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Bu özellikleri taşımayan bütün dağları kapsama katar.","collision":"Genel dağ adıyla karışır.","fit":"broadening","loses":"Uzun sırt biçimini, çıkış kolaylığını ve oturmaya elverişliliği kaybeder.","preserves":"Yükseltili bir yeryüzü biçimi olma özelliğini korur."},"text":"dağ"}],"identity_rationale":"Tek kaynaklı ifade, dağın yükselen ve uzun bir sırtını; uzunluğuna rağmen çıkılması daha kolay ve insanın oturmasına daha elverişli oluşuyla birlikte açıkça tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kolay çıkılan ve oturmaya elverişli uzun dağ sırtı"}],"lexicalization_note":"Yalın dal doğrudan belirli bir dağ sırtı türünü adlandırır; bedbahtlık, güçlük veya karşılıklı uğraşma dallarından anlam aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşleşen dağ sırtı dalı ile biçimsel çıkıntı ve çıkış yeri bakımından en yakın iki coğrafi komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Odak dal ile komşu dalın çekirdeği, kapsamı ve ayırt edici koşulları aynıdır; olağan bağlamlarda birbirinin yerine kullanılabilir.","focus_only":null,"gloss":"kolay çıkılan, oturmaya elverişli uzun dağ sırtı","neighbor_only":null,"neighbor_ref":"root_000808/B004","relation_type":"synonym","shared_zone":"Her iki dal da aynı uzun dağ sırtını çıkış kolaylığı ve oturmaya elverişliliğiyle tanımlar."},{"boundary_match":"partial","distinction":"Odak dalın çıkış kolaylığı ve oturma elverişliliği zorunlu sınırdır; komşu dal biçimsel çıkıntıyı veya büyük dağı daha geniş biçimde kapsar.","focus_only":"Çıkılması daha kolay ve oturmaya daha elverişli olan uzun bir dağ sırtını belirtir.","gloss":"uzun dağ sırtı ve çıkıntılı dağ parçası","neighbor_only":"Büyük dağın kendisini veya dağdan uzunlamasına çıkan bir parçayı, çıkış ve oturma koşulları olmadan belirtebilir.","neighbor_ref":"root_001179/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da dağın uzunlamasına uzanan ya da dışarı çıkan bir bölümünü adlandırabilir."},{"boundary_match":"field_only","distinction":"Odak dal somut bir sırt türüdür; komşu dal ise çıkma eylemine, çıkış güzergahına veya yüksekten bakılan yere odaklanır.","focus_only":"Belirli özelliklere sahip uzun bir dağ sırtını adlandırır.","gloss":"dağ sırtı ve çıkış yeri","neighbor_only":"Dağa çıkma eylemini, çıkış yerini veya yüksekten bakılan bir konumu anlatır.","neighbor_ref":"root_000945/B006","relation_type":"same_field","shared_zone":"İki dal da dağlık bir yerde yükselme, çıkma ve yüksek konumla ilişkilidir."}],"source_phrase_ar":"الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Dalın tek tanıklığı, uzun dağ sırtını hem kolay çıkılır hem de oturmaya elverişli oluşuyla sınırlar."}],"source_summary":"Bu coğrafi ad, yükselen uzun bir dağ sırtını çıkış kolaylığı ve oturmaya elverişliliğiyle birlikte tanımlar.","sources":["AY"],"what_is_ar":"يدخل فيه الحيد الطالع الطويل من الجبل إذا كان أيسر صعودا وأقدر مقعدا للإنسان وجمعه شاقيات وشواقي","what_is_not_ar":"ليس الشقاء ولا المشاقاة"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["87:11:1"],"branch_refs":[],"candidate_id":"cand_71349aa29ccdf2b8b9bf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:11:1:paired-response-connector","source_type":"word_analysis","support_ids":["sup_214fc011c8d7894c77a4","sup_ca69f4f1039a287fa85c"],"title":"connector pairs receptive fear with avoidance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:1","qac_refs":["87:11:1:1"],"status":"accepted"}},{"anchor_refs":["87:11:1"],"branch_refs":[],"candidate_id":"cand_484357f0b12d6131de6b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:11:1:surface-pivot","source_type":"word_analysis","support_ids":["sup_214fc011c8d7894c77a4","sup_4cc7350346d06e1abd34"],"title":"short attached hinge into the avoidance verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:1","qac_refs":["87:11:1:1"],"status":"accepted"}},{"anchor_refs":["87:11:2"],"branch_refs":[],"candidate_id":"cand_fe907ea05860e41bd5f5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"87:11:2:active-ongoing-self-distancing","source_type":"word_analysis","support_ids":["sup_585d3efab0f9f900d957","sup_7310fd5c39c6ec05bd85"],"title":"active imperfect self-positioning","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:2","qac_refs":["87:11:1:2","87:11:1:3"],"status":"accepted"}},{"anchor_refs":["87:11:2"],"branch_refs":[],"candidate_id":"cand_eba68f2150ae12fc4624","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"87:11:2:commanded-shunning-contrast","source_type":"word_analysis","support_ids":["sup_7310fd5c39c6ec05bd85","sup_f04333cc9ca41795e7d5"],"title":"pious avoidance elsewhere reversed here","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:2","qac_refs":["87:11:1:2","87:11:1:3"],"status":"accepted"}},{"anchor_refs":["87:11:2"],"branch_refs":[],"candidate_id":"cand_616e62f46dc09aa33342","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"87:11:2:form-contrast-agency","source_type":"word_analysis","support_ids":["sup_7310fd5c39c6ec05bd85","sup_9828e189e90107d795f9"],"title":"selected stem keeps distancing internally owned","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:2","qac_refs":["87:11:1:2","87:11:1:3"],"status":"accepted"}},{"anchor_refs":["87:11:2"],"branch_refs":[],"candidate_id":"cand_aabac533104736021cbf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"87:11:2:remembered-object-suffix","source_type":"word_analysis","support_ids":["sup_7310fd5c39c6ec05bd85","sup_eefadc02613bc37f404c"],"title":"suffix keeps the refused reminder present","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:2","qac_refs":["87:11:1:2","87:11:1:3"],"status":"accepted"}},{"anchor_refs":["87:11:2"],"branch_refs":[],"candidate_id":"cand_5896712093bc36245aea","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"87:11:2:side-distance-moral-refusal","source_type":"word_analysis","support_ids":["sup_1654530d531481504045","sup_7310fd5c39c6ec05bd85"],"title":"side-distance image under moral refusal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:2","qac_refs":["87:11:1:2","87:11:1:3"],"status":"accepted"}},{"anchor_refs":["87:11:2"],"branch_refs":[],"candidate_id":"cand_395721f192dcbdf91bb7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"87:11:2:sound-thickened-distance","source_type":"word_analysis","support_ids":["sup_2e94ac0e50934c7fc4dd","sup_7310fd5c39c6ec05bd85"],"title":"sound texture slows the avoidance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:2","qac_refs":["87:11:1:2","87:11:1:3"],"status":"accepted"}},{"anchor_refs":["87:11:2"],"branch_refs":[],"candidate_id":"cand_0c9d19d5a1e49c31d554","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"87:11:2:verb-before-subject-diagnosis","source_type":"word_analysis","support_ids":["sup_4e9a62eadc2f574a7289","sup_7310fd5c39c6ec05bd85"],"title":"conduct shown before the actor is labeled","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:2","qac_refs":["87:11:1:2","87:11:1:3"],"status":"accepted"}},{"anchor_refs":["87:11:3"],"branch_refs":[],"candidate_id":"cand_1d834d89a32d7ca2b990","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"87:11:3:audible-response-contrast","source_type":"word_analysis","support_ids":["sup_62245042a731bbdc9ae2","sup_853abf82234ad68438f2"],"title":"shared final cadence with opposite orientation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:3","qac_refs":["87:11:2:1","87:11:2:2"],"status":"accepted"}},{"anchor_refs":["87:11:3"],"branch_refs":[],"candidate_id":"cand_a0f429e90a76ff802710","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"87:11:3:extreme-wretched-verdict","source_type":"word_analysis","support_ids":["sup_3e7aa64ea7a084288b4d","sup_853abf82234ad68438f2"],"title":"extreme wretchedness as final verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:3","qac_refs":["87:11:2:1","87:11:2:2"],"status":"accepted"}},{"anchor_refs":["87:11:3"],"branch_refs":[],"candidate_id":"cand_a300ca7c79b99f8bf3a2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"87:11:3:inter-ayah-outcome-links","source_type":"word_analysis","support_ids":["sup_1675c0121a6e27c28cbf","sup_853abf82234ad68438f2"],"title":"same label points toward outcome scenes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:3","qac_refs":["87:11:2:1","87:11:2:2"],"status":"accepted"}},{"anchor_refs":["87:11:3"],"branch_refs":[],"candidate_id":"cand_9ee65e85941da00d0fb1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"87:11:3:postponed-elative-subject","source_type":"word_analysis","support_ids":["sup_853abf82234ad68438f2","sup_ec29945e5077f0ce7030"],"title":"definite elative names the exposed subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:3","qac_refs":["87:11:2:1","87:11:2:2"],"status":"accepted"}},{"anchor_refs":["87:11:3"],"branch_refs":[],"candidate_id":"cand_b167c27f88f82eea7a92","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"87:11:3:recitational-final-arrival","source_type":"word_analysis","support_ids":["sup_853abf82234ad68438f2","sup_afe0b4a01b3c7c08c071"],"title":"recitation sharpens the final diagnosis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:3","qac_refs":["87:11:2:1","87:11:2:2"],"status":"accepted"}},{"anchor_refs":["87:11:3"],"branch_refs":[],"candidate_id":"cand_e15fb7eec33ff135e1b4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"87:11:3:root-family-ruin-pressure","source_type":"word_analysis","support_ids":["sup_7ebc9955cd75a919c692","sup_853abf82234ad68438f2"],"title":"judgment and self-involved ruin as pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:11:3","qac_refs":["87:11:2:1","87:11:2:2"],"status":"accepted"}},{"anchor_refs":["87:11:1"],"branch_refs":[],"candidate_id":"cand_42db2348dc21fbc4c645","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"87:11:1:2","source_type":"qac_morpheme","support_ids":["sup_8edbfb660b8b71170ae3"],"title":"QAC root occurrence: ج ن ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:11:2"],"branch_refs":[],"candidate_id":"cand_6bc8e7842f059c06d535","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"87:11:2:2","source_type":"qac_morpheme","support_ids":["sup_4a476f7f44721257f0e6"],"title":"QAC root occurrence: ش ق و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:11","branch_refs":["root_000262/B003","root_000809/B001"],"candidate_id":"cand_e1e0a6115ea9277889eb","commentary_obligation":"review","hft_ref":"hft_2aa0cddb441acee93923","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_enacted_estrangement","source_type":"hft","support_ids":["sup_c001808549ecea3473b5"],"title":"baseline_enacted_estrangement","trust":"legacy_unbound"},{"anchor_refs":["87:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:11","branch_refs":["root_000262/B003","root_000808/B002","root_000809/B002"],"candidate_id":"cand_b4902bc5400ed6c2d9d6","commentary_obligation":"review","hft_ref":"hft_18e2aa107f6d6ea05e22","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_avoidance_as_toil","source_type":"hft","support_ids":["sup_24be94ddce34b7dac6ce"],"title":"baseline_avoidance_as_toil","trust":"legacy_unbound"},{"anchor_refs":["87:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:11","branch_refs":["root_000262/B002","root_000262/B003","root_000809/B001"],"candidate_id":"cand_c91955913c19c6a61c96","commentary_obligation":"review","hft_ref":"hft_a8c8fb0ad847023e0c87","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_contested_proximity","source_type":"hft","support_ids":["sup_0793f3c648ae91665955"],"title":"baseline_contested_proximity","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَيَتَجَنَّبُهَا ٱلْأَشْقَى","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:11:1:1","qac_word_ref":"87:11:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"يَتَجَنَّبُ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:11:1:2","qac_word_ref":"87:11:1","root_ar":"ج ن ب","surface_ar":"يَتَجَنَّبُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"87:11:1:3","qac_word_ref":"87:11:1","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"87:11:2:1","qac_word_ref":"87:11:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:11:2:2","qac_word_ref":"87:11:2","root_ar":"ش ق و","surface_ar":"أَشْقَى"}],"word_analysis_qac_refs":[["87:11:1:1"],["87:11:1:2","87:11:1:3"],["87:11:2:1","87:11:2:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["87:11:1","87:11:2","87:11:3"]},"focus_surface_evidence":{"arabic_uthmani":"وَيَتَجَنَّبُهَا ٱلْأَشْقَى","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:11:1:1","qac_word_ref":"87:11:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"يَتَجَنَّبُ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:11:1:2","qac_word_ref":"87:11:1","root_ar":"ج ن ب","surface_ar":"يَتَجَنَّبُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"87:11:1:3","qac_word_ref":"87:11:1","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"87:11:2:1","qac_word_ref":"87:11:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"87:11:2:2","qac_word_ref":"87:11:2","root_ar":"ش ق و","surface_ar":"أَشْقَى"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["87:11:1:1"],["87:11:1:2","87:11:1:3"],["87:11:2:1","87:11:2:2"]],"word_analysis_refs":["87:11:1","87:11:2","87:11:3"],"word_rows":[{"analysis_record_ref":"87:11:1","analytic_gloss_range_en":"clause-opening connector that links the avoidant response to the prior receptive response; locally contrastive by pairing, not by an explicit adversative particle","analytic_root_gloss_range_en":null,"qac_refs":["87:11:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"87:11:2","analytic_gloss_range_en":"active ongoing self-distancing from a definite remembered object; the local sense is deliberate avoidance of the prior reminder, with side-distance imagery retained but ritual, wind, ailment, and other remote branches unactivated","analytic_root_gloss_range_en":"broad range around side, flank, nearness, keeping aside, avoidance, foreignness, ritual separation, leading alongside, and other specialized branches; the local frame selects the keeping-aside/avoidance branch","qac_refs":["87:11:1:2","87:11:1:3"],"root":{"arabic":"ج ن ب","transliteration":"j-n-b"},"surface":{"arabic":"يَتَجَنَّبُهَا","transliteration":"yatajannabuhā"}},{"analysis_record_ref":"87:11:3","analytic_gloss_range_en":"definite singular elative class-label for the avoider: the most wretched or ruinously failed one, functioning as the postponed subject and final verdict rather than a mere emotional description","analytic_root_gloss_range_en":"broad range around wretchedness, misery opposite happiness, hardship, strenuous suffering, and specialized mountain-flank terminology; the local elative selects extreme wretchedness and ruinous outcome","qac_refs":["87:11:2:1","87:11:2:2"],"root":{"arabic":"ش ق و","transliteration":"sh-q-w"},"surface":{"arabic":"ٱلْأَشْقَى","transliteration":"al-ashqā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["87:11"],"branch_refs":["root_000262/B003","root_000809/B001"],"candidate_id":"cand_e1e0a6115ea9277889eb","evidence_scope":"focus_ayah","hft_ref":"hft_2aa0cddb441acee93923","item_id":"baseline_enacted_estrangement","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_enacted_estrangement","support_id":"sup_c001808549ecea3473b5"},{"anchor_refs":["87:11"],"branch_refs":["root_000262/B003","root_000808/B002","root_000809/B002"],"candidate_id":"cand_b4902bc5400ed6c2d9d6","evidence_scope":"focus_ayah","hft_ref":"hft_18e2aa107f6d6ea05e22","item_id":"baseline_avoidance_as_toil","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_avoidance_as_toil","support_id":"sup_24be94ddce34b7dac6ce"},{"anchor_refs":["87:11"],"branch_refs":["root_000262/B002","root_000262/B003","root_000809/B001"],"candidate_id":"cand_c91955913c19c6a61c96","evidence_scope":"focus_ayah","hft_ref":"hft_a8c8fb0ad847023e0c87","item_id":"baseline_contested_proximity","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_contested_proximity","support_id":"sup_0793f3c648ae91665955"}],"diagnostics":[],"lane_counts":{"global":10,"macro":11,"micro":3},"packet_summary":{"ayah_count":19,"focus_ref":"87:11","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ء ث ر","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":true,"target_occurrences":9,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]}],"window":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"87:11","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"87:11","lane":"micro","linguistic_source_ref":"87:11","surface_ref":"87:11","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"87:11","target_tokens":[["En",["87:11:2"]],["bahtsız",["87:11:2"]],["olan",["87:11:2"]],["ise",["87:11:1"]],["ondan",["87:11:1"]],["kaçınacaktır",["87:11:1"]]],"text":"En bahtsız olan ise ondan kaçınacaktır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s087-p01-001-019","label":"Whole surah","number":1,"refs":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:2:side-distance-moral-refusal","source_type":"word_analysis","support_id":"sup_1654530d531481504045","text":"{\"blocking_evidence\":null,\"headline\":\"side-distance image under moral refusal\",\"reader_payoff\":\"The reader notices refusal as managed distance: the avoider places himself to the side of an available reminder rather than simply holding an opinion.\",\"reason\":\"V4 supports side, keeping-aside, and avoidance branches for {{ar:ج ن ب}} ({{tr:j-n-b}}); local grammar narrows the pressure to avoidance of the reminder and does not activate ritual separation, wind, ailment, milk-scarcity, or other specialized branches.\",\"representative_source_ids\":[\"QS-030158e4\",\"MS-c4c98795\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:3:inter-ayah-outcome-links","source_type":"word_analysis","support_id":"sup_1675c0121a6e27c28cbf","text":"{\"blocking_evidence\":null,\"headline\":\"same label points toward outcome scenes\",\"reader_payoff\":\"The reader notices that the rare elative class-label here is tied to outcome language elsewhere, especially the burning figure in 92:15, while 20:2 contrasts misery with the Quran's purpose.\",\"reason\":\"The cited references provide concrete echo and contrast evidence; they clarify the local verdict's horizon without replacing the grammar of the local subject.\",\"representative_source_ids\":[\"QI-e2d9914e\",\"MI-e4704ba0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:1","source_type":"word_analysis","support_id":"sup_214fc011c8d7894c77a4","text":"{\"gloss_range\":\"clause-opening connector that links the avoidant response to the prior receptive response; locally contrastive by pairing, not by an explicit adversative particle\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) opens the ayah by making the avoider an answering countertype to the one who heeds under fear in the prior clause (87:10). The particle does not need to say \\\"but\\\"; it lets the two responses stand side by side, so receptivity and avoidance interpret each other. Its visible attachment to the following verb and its short sound also make the turn quick: the clause begins from relation before the avoider is named.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:2:sound-thickened-distance","source_type":"word_analysis","support_id":"sup_2e94ac0e50934c7fc4dd","text":"{\"blocking_evidence\":null,\"headline\":\"sound texture slows the avoidance\",\"reader_payoff\":\"The reader notices that the doubled middle sound and final long vowel make the held distance audible before the clause lands on the closing label.\",\"reason\":\"The phonetic rows do not create grammar, but they add a distinct audible payoff to the retained avoidance and suffix topics.\",\"representative_source_ids\":[\"QP-54bcf707\",\"MP-9152bc10\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:3:extreme-wretched-verdict","source_type":"word_analysis","support_id":"sup_3e7aa64ea7a084288b4d","text":"{\"blocking_evidence\":null,\"headline\":\"extreme wretchedness as final verdict\",\"reader_payoff\":\"The reader notices that the word does not mean ordinary sadness; it closes the ayah with an extreme moral and outcome verdict on avoidance.\",\"reason\":\"V4 supports misery opposite happiness and hardship branches for {{ar:ش ق و}} ({{tr:sh-q-w}}), while the local ADJ_COMP form selects the extreme wretchedness label as the clause's final landing.\",\"representative_source_ids\":[\"QS-55c8847f\",\"QT-b1ee9a9d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:11:2:2","source_type":"qac_morpheme","support_id":"sup_4a476f7f44721257f0e6","text":"{\"lemma_ar\":\"أَشْقَى\",\"morph_features\":\"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|MS|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"87:11:2:2\",\"qac_word_ref\":\"87:11:2\",\"root_ar\":\"ش ق و\",\"surface_ar\":\"أَشْقَى\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:1:surface-pivot","source_type":"word_analysis","support_id":"sup_4cc7350346d06e1abd34","text":"{\"blocking_evidence\":null,\"headline\":\"short attached hinge into the avoidance verb\",\"reader_payoff\":\"The reader notices a quick surface pivot: the connector is segmented as a particle but graphically and audibly launches the heavier avoidance verb.\",\"reason\":\"The bundle isolates the connector from the following verb while preserving its prefixed surface position; the sound observation adds a distinct pacing payoff.\",\"representative_source_ids\":[\"QF-323c7919\",\"QP-f8072eab\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:2:verb-before-subject-diagnosis","source_type":"word_analysis","support_id":"sup_4e9a62eadc2f574a7289","text":"{\"blocking_evidence\":null,\"headline\":\"conduct shown before the actor is labeled\",\"reader_payoff\":\"The reader notices the action before the agent's label arrives, so identity is diagnosed from exposed conduct.\",\"reason\":\"Attachment evidence identifies {{ar:ٱلْأَشْقَى}} ({{tr:al-ashqā}}) as the postponed subject of the verb, matching the CRITICAL word-order observation.\",\"representative_source_ids\":[\"QT-a2dd445d\",\"MT-bef74017\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:2:active-ongoing-self-distancing","source_type":"word_analysis","support_id":"sup_585d3efab0f9f900d957","text":"{\"blocking_evidence\":null,\"headline\":\"active imperfect self-positioning\",\"reader_payoff\":\"The reader notices avoidance as an ongoing, self-involving posture rather than a completed incident or accidental non-contact.\",\"reason\":\"The aligned grammar identifies an imperfect active verb, and attachment evidence makes the avoider the active subject rather than a hidden or passive patient.\",\"representative_source_ids\":[\"QG-c9d2a0d2\",\"QF-746652d1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:3:audible-response-contrast","source_type":"word_analysis","support_id":"sup_62245042a731bbdc9ae2","text":"{\"blocking_evidence\":null,\"headline\":\"shared final cadence with opposite orientation\",\"reader_payoff\":\"The reader notices that the receptive and avoidant figures are paired by sound across 87:10-11 even as their responses move in opposite directions.\",\"reason\":\"The sound rows add a distinct cadence payoff: the long final endings connect the adjacent response-types without changing their semantic opposition.\",\"representative_source_ids\":[\"QE-9350e8b9\",\"QY-be621e76\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:2","source_type":"word_analysis","support_id":"sup_7310fd5c39c6ec05bd85","text":"{\"gloss_range\":\"active ongoing self-distancing from a definite remembered object; the local sense is deliberate avoidance of the prior reminder, with side-distance imagery retained but ritual, wind, ailment, and other remote branches unactivated\",\"prose\":\"{{ar:يَتَجَنَّبُهَا}} ({{tr:yatajannabuhā}}) makes refusal grammatical before the actor is named. The imperfect active form shows avoidance as an ongoing posture, and the self-positioning stem makes the subject move himself aside rather than merely miss the message. The attached feminine suffix keeps the earlier reminder (87:9) inside the verb, so the object of refusal is definite and already known. The root's side-distance field lets the moral refusal feel spatial: the avoider places himself to the side of the reminder. That image is narrowed locally to avoidance of the reminder; ritual separation, wind, side-ailment, and other dictionary branches do not govern this clause. The same distancing logic can mark commanded shunning elsewhere (22:30; 49:12), but here it is reversed because the target is the saving reminder. The doubled middle sound and final long suffix make the held distance audible before the verb lands on {{ar:ٱلْأَشْقَى}} ({{tr:al-ashqā}}), so the conduct is displayed before the closing label diagnoses the agent.\",\"root_display\":\"{{ar:ج ن ب}} ({{tr:j-n-b}})\",\"root_gloss_range\":\"broad range around side, flank, nearness, keeping aside, avoidance, foreignness, ritual separation, leading alongside, and other specialized branches; the local frame selects the keeping-aside/avoidance branch\",\"surface_display\":\"{{ar:يَتَجَنَّبُهَا}} ({{tr:yatajannabuhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:3:root-family-ruin-pressure","source_type":"word_analysis","support_id":"sup_7ebc9955cd75a919c692","text":"{\"blocking_evidence\":null,\"headline\":\"judgment and self-involved ruin as pressure\",\"reader_payoff\":\"The reader notices that the label carries ruin and judgment pressure around the avoider, while the local word remains the elative class-label.\",\"reason\":\"Derivative-family rows legitimately sharpen the force of wretchedness, but local grammar does not turn the word into a passive judgment verb, a causative verb, or a Form V suffering verb.\",\"representative_source_ids\":[\"QS-6d25e8d1\",\"QS-8d57a827\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:3","source_type":"word_analysis","support_id":"sup_853abf82234ad68438f2","text":"{\"gloss_range\":\"definite singular elative class-label for the avoider: the most wretched or ruinously failed one, functioning as the postponed subject and final verdict rather than a mere emotional description\",\"prose\":\"{{ar:ٱلْأَشْقَى}} ({{tr:al-ashqā}}) arrives after the verb, so the ayah lets avoidance expose the actor before it gives him a name. The definite singular elative turns an adjective of extreme wretchedness into a recognizable class-label: not merely someone sad, but the one at the outer edge of failed response. Root-family pressures of misery, judgment, and self-involved ruin survive as the verdict's force, while the local form keeps the sense on the elative label. The exact label also links this avoider to the one who burns under the same label (92:15), while 20:2 marks misery as what the Quran is not sent to impose on the Prophet. Sound helps the contrast close: the fear-response in 87:10 and {{ar:ٱلْأَشْقَى}} ({{tr:al-ashqā}}) share a long final cadence while naming opposite orientations toward the reminder. Recitationally, liaison keeps the final label continuous with the avoidance verb, while the hamza sharpens its arrival as the verdict.\",\"root_display\":\"{{ar:ش ق و}} ({{tr:sh-q-w}})\",\"root_gloss_range\":\"broad range around wretchedness, misery opposite happiness, hardship, strenuous suffering, and specialized mountain-flank terminology; the local elative selects extreme wretchedness and ruinous outcome\",\"surface_display\":\"{{ar:ٱلْأَشْقَى}} ({{tr:al-ashqā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:11:1:2","source_type":"qac_morpheme","support_id":"sup_8edbfb660b8b71170ae3","text":"{\"lemma_ar\":\"يَتَجَنَّبُ\",\"morph_features\":\"STEM|POS:V|IMPF|(V)|LEM:yatajan~abu|ROOT:jnb|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"87:11:1:2\",\"qac_word_ref\":\"87:11:1\",\"root_ar\":\"ج ن ب\",\"surface_ar\":\"يَتَجَنَّبُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:2:form-contrast-agency","source_type":"word_analysis","support_id":"sup_9828e189e90107d795f9","text":"{\"blocking_evidence\":null,\"headline\":\"selected stem keeps distancing internally owned\",\"reader_payoff\":\"The reader notices that the ayah does not make an outside force avert the avoider; the selected surface makes him perform the distancing himself.\",\"reason\":\"The local verb carries the self-positioning avoidance reading; other derived forms in the CRITICAL rows are useful contrasts but do not replace the local surface.\",\"representative_source_ids\":[\"QF-4d670e79\",\"QF-c783422a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:3:recitational-final-arrival","source_type":"word_analysis","support_id":"sup_afe0b4a01b3c7c08c071","text":"{\"blocking_evidence\":null,\"headline\":\"recitation sharpens the final diagnosis\",\"reader_payoff\":\"The reader notices that liaison and hamza make the final label sound continuous with the avoidance while sharpening its arrival as a verdict.\",\"reason\":\"The phonetic rows preserve an audible boundary effect that is distinct from both the grammar of the postponed subject and the rhyme contrast with 87:10.\",\"representative_source_ids\":[\"QP-05b988ff\",\"QP-654fa5b0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:1:paired-response-connector","source_type":"word_analysis","support_id":"sup_ca69f4f1039a287fa85c","text":"{\"blocking_evidence\":null,\"headline\":\"connector pairs receptive fear with avoidance\",\"reader_payoff\":\"The reader notices that the ayah begins as the answering half of a paired response, so avoidance is read against the prior receptive fear (87:10).\",\"reason\":\"QAC identifies {{ar:وَ}} ({{tr:wa}}) as a prefixed conjunction, and the local clause evidence supports a verbal clause coordinated with the prior heed-taking response.\",\"representative_source_ids\":[\"QG-35e33db0\",\"QE-534524d2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:3:postponed-elative-subject","source_type":"word_analysis","support_id":"sup_ec29945e5077f0ce7030","text":"{\"blocking_evidence\":null,\"headline\":\"definite elative names the exposed subject\",\"reader_payoff\":\"The reader notices that the final label is a grammatical subject revealed after the avoidance, turning behavior into an identified class.\",\"reason\":\"QAC and attachment evidence identify {{ar:ٱلْأَشْقَى}} ({{tr:al-ashqā}}) as a definite masculine singular elative functioning as the postponed subject of the verb.\",\"representative_source_ids\":[\"QG-17f16640\",\"MG-53a0a70f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:2:remembered-object-suffix","source_type":"word_analysis","support_id":"sup_eefadc02613bc37f404c","text":"{\"blocking_evidence\":null,\"headline\":\"suffix keeps the refused reminder present\",\"reader_payoff\":\"The reader notices that the refused object is not vague; the attached feminine suffix carries the prior reminder into the avoidance verb.\",\"reason\":\"Attachment evidence marks the suffix as the direct object and links it to the feminine reminder in the preceding discourse.\",\"representative_source_ids\":[\"QG-40f650aa\",\"QE-c177f2b4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:11:2:commanded-shunning-contrast","source_type":"word_analysis","support_id":"sup_f04333cc9ca41795e7d5","text":"{\"blocking_evidence\":null,\"headline\":\"pious avoidance elsewhere reversed here\",\"reader_payoff\":\"The reader notices that avoidance can be commanded as piety elsewhere, but here the same distancing logic is reversed because the target is the saving reminder (22:30; 49:12).\",\"reason\":\"The cited parallels show a real contrast in the root-family logic of avoidance; they are kept as contrastive evidence and do not govern the local form or target.\",\"representative_source_ids\":[\"QI-d6c643b0\",\"MI-30858a0a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَيَتَجَنَّبُهَا ٱلْأَشْقَى","ayah_ref":"87:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000262/B003","root_000809/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000262","role":"Keeping aside, avoidance, and estrangement supply the verb's literal motion and make self-exile the model's operative relation.","root":"ج ن ب","source_ref":"87:11","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000809","role":"Wretchedness opposite happiness supplies the agent's superlative condition and lets the distancing action diagnose that condition.","root":"ش ق و","source_ref":"87:11","source_word_indices":["2"]}],"changed_reading":{"after":"The maximally wretched person makes wretchedness visible by continually relocating himself to the far side of the feminine referent.","before":"A maximally wretched person simply avoids an unspecified feminine object."},"confidence":"strong","focus_anchor":"The imperfect middle-form verb يَتَجَنَّبُهَا makes ٱلْأَشْقَى the agent of an ongoing self-positioning away from a feminine referent.","mechanism":"The side-root becomes a relation deliberately broken: the agent moves himself out of adjacency with the referent. Read with the wretchedness branch of the split ش ق و inventory, the superlative is not only a prior label but a condition enacted and exposed by this withdrawal.","model_id":"baseline_enacted_estrangement"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_enacted_estrangement","source_type":"hft","support_id":"sup_c001808549ecea3473b5","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَيَتَجَنَّبُهَا ٱلْأَشْقَى","ayah_ref":"87:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000262/B003","root_000808/B002","root_000809/B002"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000262","role":"Withdrawal and active removal to a side supply the distance that must be maintained.","root":"ج ن ب","source_ref":"87:11","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000808","role":"Strenuous suffering and endurance supply the energetic cost of keeping the referent away.","root":"ش ق و","source_ref":"87:11","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000809","role":"Hardship, difficulty, and toil preserve the labor reading in the second mapped inventory rather than reducing ش ق و to a moral label.","root":"ش ق و","source_ref":"87:11","source_word_indices":["2"]}],"changed_reading":{"after":"The one deepest in hardship labors to hold the referent at a distance; evasion is itself a toil-producing practice.","before":"The predicate reports a bad recipient's easy refusal."},"confidence":"medium","focus_anchor":"ٱلْأَشْقَى can activate both mapped ش ق و inventories, where hardship and labor coexist with wretchedness, while يَتَجَنَّبُهَا supplies maintained distance.","mechanism":"Avoidance is not effortless nonattendance. The split root makes it an exertion: the agent keeps working to preserve separation, so the attempted escape becomes part of the hardship named by the superlative.","model_id":"baseline_avoidance_as_toil"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_avoidance_as_toil","source_type":"hft","support_id":"sup_24be94ddce34b7dac6ce","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَيَتَجَنَّبُهَا ٱلْأَشْقَى","ayah_ref":"87:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000262/B002","root_000262/B003","root_000809/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000262","role":"Nearness and companionship at one's side supply the latent proximity against which avoidance operates.","root":"ج ن ب","source_ref":"87:11","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000262","role":"Removal and estrangement reverse that adjacency and turn a stable side into an actively defended boundary.","root":"ج ن ب","source_ref":"87:11","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000809","role":"Wretchedness names the person whose identity remains relationally bound to the object he excludes.","root":"ش ق و","source_ref":"87:11","source_word_indices":["2"]}],"changed_reading":{"after":"He sustains a side-boundary against something still close enough to press upon him; avoidance discloses contested nearness, not freedom from relation.","before":"He leaves the referent behind in a clean, completed departure."},"confidence":"medium","focus_anchor":"The same ج ن ب inventory places adjacency at one's side beside the derived verb's avoidance, and the imperfect يَتَجَنَّبُ presents the boundary as active rather than settled.","mechanism":"The referent is not simply absent. Avoidance reverses a live side-by-side relation, implying something close enough to require recurrent lateral repositioning. The verse can therefore stage contested proximity: the agent remains defined by what he tries to put aside.","model_id":"baseline_contested_proximity"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_contested_proximity","source_type":"hft","support_id":"sup_0793f3c648ae91665955","trust":"legacy_unbound"}]}
</lane_packet_json>
