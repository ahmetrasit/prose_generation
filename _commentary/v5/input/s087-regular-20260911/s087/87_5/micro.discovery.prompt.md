# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **87:5**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s087-regular-20260911/s087/87_5/micro.discovery.json` and modify nothing
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
  "ayah_ref": "87:5",
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
{"analysis_context":{"analysis_id":"s087-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"87:5","host_surah":87,"lane_context_refs":[],"ordered_context_refs":["87:0","87:1","87:2","87:3","87:4","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal, var olan bir şeyi başka bir duruma sokmayı, adlandırmayı ya da bir eyleme başlamayı kapsamaz.","branch_kind":"bare","branch_ref":"root_000248/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:5:1:2","qac_word_ref":"87:5:1","surface_ar":"جَعَلَ"}],"gloss":"bir şeyi yapıp var etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığın yapılmasını, üretilmesini veya varlığa çıkarılmasını bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin üretilmesi, yaratılması veya yokken ortaya çıkarılması anlatıldığında dalın bütün çekirdeğini karşılar.","boundary_detail":"Bu dal, var olan bir şeyi başka bir duruma sokmayı, adlandırmayı ya da bir eyleme başlamayı kapsamaz.","branch_image_ar":"إحداث الشيء وصنعه","concept_gloss":"bir şeyi yapıp var etme","contextual_glosses":[{"applicability":"Bir nesnenin veya varlığın ortaya çıkarılışını bildiren tamamlanmış eylem bağlamlarında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapma ile var etme arasındaki çekirdek anlam genişliğini korur."},"facet_ids":["F001"],"text":"onu yaptı ya da var etti","usage_role":"contextual"}],"definition":"Bir şeyi yapmak, üretmek, yaratmak ya da daha önce yokken var etmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığın yapılmasını, üretilmesini veya varlığa çıkarılmasını bildirir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi yapma, üretme, yaratma veya yokken var etme anlamlarını açıkça aynı çekirdekte toplar. Geçici dal çerçevesi bu üretici ve var edici işlemi doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi yapmak, yaratmak veya var etmek"}],"lexicalization_note":"Dal yalın kullanıma dayanır; tanım herhangi bir özel söz öbeğine bağlı değildir.","neighbor_coverage_note":"Bütün adaylar incelendi; en güçlü karışma noktaları durum değiştirme dalı ile daha geniş yapma ve iş görme dalıdır, öteki adaylar aynı sınırı daha az açıklayıcı biçimde yineler.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sonucu bir şeyin yapılması ya da var edilmesidir; komşu dalda ise var olan katılımcı korunur ve yalnızca onun durumu veya niteliği değiştirilir.","focus_only":"Yeni bir şeyi üretme veya yokken varlığa çıkarma işlemini anlatır.","gloss":"bir duruma sokma","neighbor_only":"Var olan bir kişi ya da şeyi belirli bir duruma, niteliğe veya konuma getirir.","neighbor_ref":"root_000248/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir etkenin yol açtığı sonuç ve değişiklik bulunur."},{"boundary_match":"partial","distinction":"Odak dal nesnenin yapılması veya var edilmesinde yoğunlaşırken komşu dal, ortaya bir nesne çıkarmayan genel eylem ve davranışları da içine alır.","focus_only":"Bir şeyi üretme, yaratma veya varlığa çıkarma yönü belirgindir.","gloss":"yapma ve iş görme","neighbor_only":"İyi ya da kötü her türlü işi ve davranışı da kapsayan daha geniş bir eylem alanına sahiptir.","neighbor_ref":"root_000885/B001","relation_type":"near_synonym","shared_zone":"Bir şeyi yapma ve ortaya çıkarma anlamlarında iki dal geniş ölçüde örtüşür."}],"source_phrase_ar":"جعلت الشيء صنعته (maqayis)؛ جعل جعلا صنع صنعا (ayn)؛ جعل خلق؛ خلقنا (tahdhib)؛ يجري مجرى أوجد (mufradat)","source_summary":"Kaynaklar, bir şeyi yapma ile onu yaratıp var etme yönlerini ortak bir üretici eylem altında birleştirir.","sources":["MQ","AY","TA","MU"],"what_is_ar":"يدخل فيه جعل الشيء بمعنى صنعه أو خلقه أو أوجده.","what_is_not_ar":"لا يدخل فيه التصيير إلى حال، ولا التسمية والقول، ولا الشروع في الفعل."},"support_links":[]},{"boundary":"Burada katılımcı varlığını sürdürür ve durumu değişir; onu yoktan üretme, adlandırma veya eyleme başlatma anlamı yoktur.","branch_kind":"bare","branch_ref":"root_000248/B002","candidate_links":[{"candidate_id":"cand_69fcf9534f45539b2909","lane":"micro"},{"candidate_id":"cand_8b3cceff415da6700cec","lane":"micro"},{"candidate_id":"cand_5fdeb0d46f7fbdc0b8d9","lane":"micro"},{"candidate_id":"cand_5850328ea1db625cb7d4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:5:1:2","qac_word_ref":"87:5:1","surface_ar":"جَعَلَ"}],"gloss":"birini veya şeyi belirli bir duruma getirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Var olan bir katılımcının durumunu, niteliğini veya konumunu değiştiren ettirici işlemi bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Katılımcının varlığı korunurken niteliği, görevi, konumu veya durumu değiştirildiğinde eksiksiz karşılık verir.","boundary_detail":"Burada katılımcı varlığını sürdürür ve durumu değişir; onu yoktan üretme, adlandırma veya eyleme başlatma anlamı yoktur.","branch_image_ar":"تصيير الشيء على حال","concept_gloss":"birini veya şeyi belirli bir duruma getirme","contextual_glosses":[{"applicability":"Bir kişinin veya şeyin yeni bir nitelik, görev ya da duruma geçirilmesini anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Var olan katılımcının ettirici bir işlemle yeni duruma geçmesini korur."},"facet_ids":["F001"],"text":"onu bu duruma getirdi","usage_role":"contextual"}],"definition":"Bir kişi veya şeyi belirli bir duruma, niteliğe ya da konuma getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Var olan bir katılımcının durumunu, niteliğini veya konumunu değiştiren ettirici işlemi bildirir."}],"identity_rationale":"Kaynak ifadesi, bir kişi veya şeyi belirli bir duruma, niteliğe ya da konuma getirme işlemini doğrudan bildirir. Verilen örnekler hem görev ve konum kazandırmayı hem de üstün bir niteliğe ulaştırmayı destekler.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi belirli bir duruma, niteliğe veya konuma getirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyi belirli bir duruma getirmek"}],"lexicalization_note":"Dal yalın kullanıma dayanır; özel bir söz öbeğinin anlamı genel tanıma taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; üretme ile ettirici olmayan duruma gelme, bu dalın katılımcı yapısını en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda sonuç, aynı katılımcının yeni durumudur; komşu dalda ise sonuç yapılan veya var edilen şeyin kendisidir.","focus_only":"Var olan katılımcıyı koruyup onun durumunu veya niteliğini değiştirir.","gloss":"bir şeyi var etme","neighbor_only":"Bir şeyi yapma, üretme ya da yokken varlığa çıkarma işlemini anlatır.","neighbor_ref":"root_000248/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de bir etkenin ortaya çıkardığı yeni sonucu ifade eder."},{"boundary_match":"partial","distinction":"Odak dal ettirici ve etkilenen olmak üzere iki katılımcılıdır; komşu dalda durum değişimi öznenin başına gelir ve ayrı bir ettirici zorunlu değildir.","focus_only":"Bir etkenin başka bir katılımcıyı yeni duruma soktuğu geçişli yapıyı gerektirir.","gloss":"bir duruma gelme","neighbor_only":"Öznenin bir dış ettirici belirtilmeden kendisinin yeni bir duruma gelmesini bildirir.","neighbor_ref":"root_000839/B010","relation_type":"near_neighbor","shared_zone":"İki dal da önceki durumdan farklı bir sonuç durumuna geçişi anlatır."}],"source_phrase_ar":"جعله الله نبيا أي صيره (sihah)؛ جعل صير؛ جعلته أحذق الناس؛ صيرهم؛ صيرته (tahdhib)","source_summary":"Kaynaklar, birini bir göreve veya üstün bir niteliğe getirmenin aynı durum değiştirme çekirdeğine bağlı olduğunu gösterir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه جعل الشيء أو الشخص على صفة أو منزلة، كتصييره نبيا أو جعله أحذق الناس.","what_is_not_ar":"لا يدخل فيه الخلق والإيجاد المجرد، ولا التسمية، ولا جعل بمعنى أخذ يفعل."},"support_links":["sup_1b557f13d09d6802a6ae","sup_33053778a4e67dd75312","sup_3f4b01b22ddbd600757d","sup_ea7f41da09281fecc31c"]},{"boundary":"Çekirdek adlandırma ve söylemedir; aynı söz dizimine ilişkin durum değiştirme yorumu ayrı bir kaynak değişkesi olarak tutulur.","branch_kind":"unresolved","branch_ref":"root_000248/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:5:1:2","qac_word_ref":"87:5:1","surface_ar":"جَعَلَ"}],"gloss":"öyle adlandırma ya da öyle olduğunu söyleme; başka yorumda öyle kılma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığı belli bir adla veya nitelikle anmayı ve onun öyle olduğunu söylemeyi bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı tanıklık için, varlığı söylenen duruma gerçekten getirme biçiminde rakip bir yorum da aktarılır."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem baskın adlandırma ve söyleme çözümünü hem de aynı tanıklığa ilişkin durum değiştirme yorumunu birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Çekirdek adlandırma ve söylemedir; aynı söz dizimine ilişkin durum değiştirme yorumu ayrı bir kaynak değişkesi olarak tutulur.","branch_image_ar":"قول الشيء أو تسميته","concept_gloss":"öyle adlandırma ya da öyle olduğunu söyleme; başka yorumda öyle kılma","contextual_glosses":[{"applicability":"Sözün bir varlığa ad veya nitelik yükleyen anlatım olarak çözüldüğü bağlamda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı ifadenin varlığı gerçekten o duruma getirme biçimindeki rakip yorumunu dışarıda bırakır.","preserves":"Adlandırma ve sözle niteleme çözümünü açık biçimde korur."},"facet_ids":["F001"],"text":"onları öyle adlandırdılar","usage_role":"contextual"},{"applicability":"Tanıklığın gerçek bir durum değişikliği olarak yorumlandığı bağlamda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Baskın adlandırma ve söyleme çözümünü dışarıda bırakır.","preserves":"Rakip durum değiştirme yorumunu doğrudan korur."},"facet_ids":["F002"],"text":"onları öyle yaptılar","usage_role":"contextual"}],"definition":"Bir varlığı belirli bir ad veya nitelikle anmak ya da onun öyle olduğunu söylemektir; aynı ifadenin bir yorumunda ise varlığı gerçekten o duruma getirme anlamı vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığı belli bir adla veya nitelikle anmayı ve onun öyle olduğunu söylemeyi bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı tanıklık için, varlığı söylenen duruma gerçekten getirme biçiminde rakip bir yorum da aktarılır."}],"identity_rationale":"Kaynak ifadesinin baskın açıklaması bir varlığı belirli bir ad veya nitelikle anma ve onun öyle olduğunu söylemedir. Bununla birlikte aynı ifadenin bir başka yorumda o varlığı gerçekten söz konusu duruma getirme diye açıklandığı da kaydedilir; bu yüzden dal ancak bu yorum ayrılığı belirtilerek korunabilir.","lexicalization_note":"Kullanımın yalın olup olmadığı mekanik olarak çözümlenmemiştir; tanım bağımsız bir yalın anlam varsaymaz.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; en yararlı ayrımlar geniş sözlü anma alanı ile aynı tanıklığa rakip olan gerçek durum değişikliğidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir yüklemeyi adlandırma veya söyleme olarak çözer; komşu dal ise sözlü anmayı ve hakkında konuşmayı daha geniş biçimde kapsar.","focus_only":"Belirli bir nesneyi veya varlığı belli bir ad ya da nitelikle anma yapısına bağlıdır.","gloss":"dilde anma ve adlandırma","neighbor_only":"Bir şeyi dilde anma, açığa vurma ve insanlar hakkında iyi ya da kötü söz söyleme alanlarına da uzanır.","neighbor_ref":"root_000516/B004","relation_type":"near_synonym","shared_zone":"Bir şeyi sözle belirtme ve adlandırma bölgesinde iki dal örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın baskın okuması dilsel bir yüklemedir; komşu dal gerçek dünyadaki durum değişikliğini anlatır ve odak dalda yalnızca rakip yorum olarak görünür.","focus_only":"Çekirdeğinde sözle adlandırma veya bir niteliği söyleme vardır.","gloss":"bir duruma sokma","neighbor_only":"Var olan katılımcının durumunu gerçekten değiştiren ettirici işlemdir.","neighbor_ref":"root_000248/B002","relation_type":"near_neighbor","shared_zone":"Aynı yüzey yapısı, aktarılan yorum ayrılığı nedeniyle iki anlam alanına yaklaşabilir."}],"source_phrase_ar":"جعلوا الملائكة إناثا أي سموهم (sihah)؛ جعل قال؛ أي قلناه؛ وقال غيره صيرناه (tahdhib)","source_summary":"Toplu tanıklık adlandırma ve söyleme açıklamasını verirken, aynı ifadenin durum değiştirme diye yorumlandığını da kaynak adı yüklemeden kaydeder.","sources":["SI","TA"],"what_is_ar":"يدخل فيه جعل بمعنى قال أو سمى بحسب النصوص التي صرحت بذلك.","what_is_not_ar":"لا يدخل فيه التصيير إلا حيث اختلف المصدر في العبارة نفسها."},"support_links":[]},{"boundary":"Anlam yalnızca ardından bir eylem gelen yapıya bağlıdır ve genel yapma, üretme ya da kesintisiz sürdürme anlamına genişletilemez.","branch_kind":"non_bare","branch_ref":"root_000248/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:5:1:2","qac_word_ref":"87:5:1","surface_ar":"جَعَلَ"}],"gloss":"bir eylemi yapmaya başlama","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Öznenin belirtilen eyleme başlamasını veya girişmesini anlatan yapı bağımlı bir kullanımdır."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca öznenin hemen ardından belirtilen eyleme giriştiğini bildiren yapı bağımlı kullanımı karşılar.","boundary_detail":"Anlam yalnızca ardından bir eylem gelen yapıya bağlıdır ve genel yapma, üretme ya da kesintisiz sürdürme anlamına genişletilemez.","branch_image_ar":"الشروع في الفعل أو ملازمته","concept_gloss":"bir eylemi yapmaya başlama","contextual_glosses":[{"applicability":"Ardından gelen eylemin özne tarafından başlatıldığını bildiren geçmiş zamanlı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öznenin belirtilen eyleme giriştiği başlangıç aşamasını korur."},"facet_ids":["F001"],"text":"yapmaya başladı","usage_role":"contextual"}],"definition":"Yalnızca ardından çekimli bir eylem gelen yapıda, öznenin o eylemi yapmaya başlamasını veya ona girişmesini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Öznenin belirtilen eyleme başlamasını veya girişmesini anlatan yapı bağımlı bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi, çekimli bir eylemden önce gelen yapının o eyleme girişme veya başlamayı bildirdiğini gösterir. Geçici çerçevedeki genel bağlı kalma ve sürdürme yönü kaynak cümlesinde kurucu bir koşul değildir; tanım bu nedenle başlangıç anlamına göre yeniden kurulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyi yapmaya başlamak"}],"lexicalization_note":"Dal yalnızca ardından çekimli bir eylem gelen özel yapıda geçerlidir; yalın kök anlamı olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; başlangıçla sürdürmeyi birlikte taşıyan yakın yapı ile yalnız devam bildiren yapı, sınırı en iyi görünür kılar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın güvenli çekirdeği başlangıçtır; komşu dalda ise başlangıçla birlikte sürdürme veya bağlı kalma yönü de açıkça yer alır.","focus_only":"Kaynak tanıklığı çekirdek olarak bir eyleme girişmeyi bildirir.","gloss":"bir eyleme başlayıp sürdürme","neighbor_only":"Başlangıcın yanında eyleme bağlı kalma ve onu sürdürme yönünü de taşıyabilir.","neighbor_ref":"root_000941/B001","relation_type":"near_synonym","shared_zone":"Ardından eylem gelen yapılarda başlangıç bildirme bakımından güçlü bir örtüşme vardır."},{"boundary_match":"partial","distinction":"Odak dal başlangıç aşamasını seçer; komşu dal başlangıcı değil, önceden süren durumun devamını ve özel bir olumsuz kuruluşu gerektirir.","focus_only":"Eylemin başlangıç sınırını ve ona girişmeyi bildirir.","gloss":"eylemi sürdürme","neighbor_only":"Olumsuz kuruluşta eylemin ya da haberin kesintisiz sürmesini bildirir.","neighbor_ref":"root_000659/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bir öznenin bir eylemle zaman içinde ilişkisini kurar."}],"source_phrase_ar":"تقول جعل يقول ولا تقول صنع يقول (maqayis)؛ جعل يأكل وجعل يصنع كذا (ayn)؛ جعل فلان يصنع كذا كقولك طفق وعلق يفعل (tahdhib)؛ يجري مجرى صار وطفق فلا يتعدى نحو جعل زيد يقول (mufradat)","source_summary":"Kaynaklar, bu yapıyı ardından gelen eyleme başlama veya girişme anlamında ve nesne almayan bir kuruluş olarak ortaklaştırır.","sources":["MQ","AY","TA","MU"],"what_is_ar":"يدخل فيه جعل يفعل كذا، أي أخذ أو طفق أو علق بالفعل.","what_is_not_ar":"لا يدخل فيه صنع الشيء ولا تصييره ولا جعله أجرا."},"support_links":[]},{"boundary":"Bu dal iş veya görev karşılığında belirlenen ödemedir; genel armağanı, yapılan işi, durum değiştirmeyi ve tencere bezini kapsamaz.","branch_kind":"bare","branch_ref":"root_000248/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:5:1:2","qac_word_ref":"87:5:1","surface_ar":"جَعَلَ"}],"gloss":"iş karşılığı belirlenen ücret veya ortaklaşa kararlaştırılan ödeme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir iş veya görevin yapılması karşılığında bir kişiye ayrılan ücret, ödeme ya da armağandır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğun sefer veya önemli bir iş sırasında kendi arasında kararlaştırdığı ortak ödemeleri de kapsar."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem bir kişiye iş için ayrılan karşılığı hem de bir topluluğun önemli iş için kararlaştırdığı ödeme biçimini kapsar.","boundary_detail":"Bu dal iş veya görev karşılığında belirlenen ödemedir; genel armağanı, yapılan işi, durum değiştirmeyi ve tencere bezini kapsamaz.","branch_image_ar":"أجر مجعول على عمل","concept_gloss":"iş karşılığı belirlenen ücret veya ortaklaşa kararlaştırılan ödeme","contextual_glosses":[{"applicability":"Belirli bir işi üstlenecek kişiye vaat edilen ücret veya ödülün anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir topluluğun kendi arasında kararlaştırdığı ortak ödeme özel durumunu dışarıda bırakır.","preserves":"Bir işin yapılmasına bağlanan bireysel ücret veya ödül çekirdeğini korur."},"facet_ids":["F001"],"text":"bu işi yapana verilecek ücret","usage_role":"contextual"},{"applicability":"Bir sefer veya önemli iş için insanların aralarında ödeme belirlediği topluluk bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir kişiye belirli bir işi yapması için ayrılan bireysel ücret biçimini dışarıda bırakır.","preserves":"Topluluğun karşılıklı olarak ödeme kararlaştırması yönünü korur."},"facet_ids":["F002"],"text":"ortaklaşa kararlaştırılan ödeme","usage_role":"contextual"}],"definition":"Bir kişinin yapacağı iş veya görev karşılığında ona verilmek üzere belirlenen ücret, ödeme ya da armağandır. Bir topluluğun sefer veya önemli bir iş için aralarında kararlaştırdığı ödemeler de bu çekirdeğin özel bir gerçekleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir iş veya görevin yapılması karşılığında bir kişiye ayrılan ücret, ödeme ya da armağandır."},{"facet_id":"F002","role":"specialization","statement":"Bir topluluğun sefer veya önemli bir iş sırasında kendi arasında kararlaştırdığı ortak ödemeleri de kapsar."}],"identity_rationale":"Kaynak ifadesi, bir kişiye yapacağı iş veya yerine getireceği görev karşılığında ayrılan ücret, ödeme ya da armağanı açıkça tanımlar. İnsanların bir sefer veya önemli iş için aralarında kararlaştırdıkları ortak ödemeler de aynı karşılık belirleme çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir iş karşılığında belirlenen ücret, ödeme veya ödül"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"önemli bir iş için ortaklaşa kararlaştırılan ödemeler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ona bir ödeme veya armağan ayırmak"}],"lexicalization_note":"Dal yalın ad alanına dayanır; özel bir söz öbeğiyle sınırlı değildir.","neighbor_coverage_note":"Bütün adaylar incelendi; genel emek karşılığı ile düzenli çalışan ücreti, bu dalın önceden belirlenen görev karşılığı sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir işi yaptırmak için konan veya kararlaştırılan karşılıktır; komşu dalın karşılık alanı daha geniştir ve önceden konma koşulu taşımaz.","focus_only":"Belirli bir iş yapılmadan önce veya onun için konan karşılığı öne çıkarır.","gloss":"emek karşılığı ve kira","neighbor_only":"Yapılmış işin karşılığını, kirayı, manevi ödülü ve evlilikte verilen bedeli de kapsar.","neighbor_ref":"root_000015/B001","relation_type":"near_synonym","shared_zone":"Bir iş ya da hizmet karşılığında verilen maddi bedel alanında örtüşürler."},{"boundary_match":"partial","distinction":"Odak dal görev koşuluna bağlı vaat veya belirlemedir; komşu dal düzenli çalışma karşılığındaki ücret ve geçim payı alanında daha özeldir.","focus_only":"Tek bir görev için vaat edilen ödülü ve topluca kararlaştırılan ödemeyi de kapsar.","gloss":"çalışanın ücreti","neighbor_only":"Bir çalışanın düzenli iş ücreti veya geçim payı olmasına odaklanır.","neighbor_ref":"root_001046/B004","relation_type":"near_synonym","shared_zone":"Yapılan emek karşılığında bir kişiye verilen maddi ödemede örtüşürler."}],"source_phrase_ar":"الجعل والجعالة والجعلية ما يجعل للإنسان على الأمر يفعله (maqayis)؛ الجعل ما جعلت لإنسان أجرا له على عمل يعمله؛ الجعالات ما يتجاعل الناس بينهم (ayn)؛ الجعل ما جعل للانسان من شئ على الشئ يفعله؛ الجعالة؛ الجعيلة مثله (sihah)؛ الجعل في العطية؛ الجعالة بالفتح من الشيء تجعله للإنسان؛ ما جعلته للإنسان أجرا على عمله (tahdhib)","source_summary":"Kaynaklar iş karşılığında önceden ayrılan ücret veya armağanda birleşir; topluca kararlaştırılan ödemeler bu çekirdeğin özel biçimi olarak aktarılır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الجعل والجعلية والجعالة والجعيلة وما يتجاعله الناس أجرا أو عطية على عمل أو أمر.","what_is_not_ar":"لا يدخل فيه فعل جعل بمعنى صنع أو صير، ولا الجعال خرقة القدر."},"support_links":[]},{"boundary":"Dal yalnızca kısa veya küçük hurma ağaçlarına ilişkindir; yer adı, böcek ve genel bitki kısalığı anlamlarına uzanmaz.","branch_kind":"bare","branch_ref":"root_000248/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:5:1:2","qac_word_ref":"87:5:1","surface_ar":"جَعَلَ"}],"gloss":"kısa veya küçük hurma ağaçları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kısa veya küçük hurma ağaçlarını topluluk olarak, tekil biçimiyle de bunlardan birini adlandırır."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hurma ağaçlarının boyca kısa ya da küçük oluşuna göre topluca adlandırıldığı kullanımların bütün çekirdeğini karşılar.","boundary_detail":"Dal yalnızca kısa veya küçük hurma ağaçlarına ilişkindir; yer adı, böcek ve genel bitki kısalığı anlamlarına uzanmaz.","branch_image_ar":"النخل الصغار أو القصار","concept_gloss":"kısa veya küçük hurma ağaçları","contextual_glosses":[{"applicability":"Birden çok kısa veya küçük hurma ağacının topluca anıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kısa hurma ağaçlarını topluluk olarak adlandırma yönünü korur."},"facet_ids":["F001"],"text":"kısa hurma ağaçları topluluğu","usage_role":"contextual"}],"definition":"Kısa veya küçük hurma ağaçlarının topluluk adı ve bu topluluktaki tek bir ağacın adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kısa veya küçük hurma ağaçlarını topluluk olarak, tekil biçimiyle de bunlardan birini adlandırır."}],"identity_rationale":"Kaynak ifadesi, kısa veya küçük hurma ağaçlarını topluluk olarak ve bunlardan birini tekil biçimde tanımlar. Geçici çerçeve hem boy hem küçüklük yönünü ve tekil ayrımını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kısa veya küçük hurma ağaçları; tekili bu ağaçlardan biri"}],"lexicalization_note":"Dal yalın ad kullanımına dayanır; özel bir söz öbeğinden türetilmiş değildir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı küçük hurma alanındaki yakın ad ile özellikle genç sürgünü anlatan ad, sınırı açıklamak için yeterlidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hem küçük hem kısa ağaçlara uzanır; komşu dalın verilen sınırı yalnız küçüklüktür, bu nedenle tam ikame her bağlamda güvenli değildir.","focus_only":"Küçüklüğün yanında boyca kısalığı da açıkça kapsar.","gloss":"küçük hurma ağaçları","neighbor_only":"Yalnız küçük hurma ağaçlarını bildirir ve ayrı bir söz ailesine dayanır.","neighbor_ref":"root_000832/B006","relation_type":"near_synonym","shared_zone":"Küçük hurma ağaçlarını topluca adlandırmada iki dal doğrudan örtüşür."},{"boundary_match":"partial","distinction":"Odak dal boy veya genel küçüklük ölçütüne dayanır; komşu dal ise bitkinin sürgün ve dikim evresini seçer.","focus_only":"Kısa veya küçük hurma ağaçlarının kendisini topluluk olarak adlandırır.","gloss":"genç hurma sürgünleri","neighbor_only":"Özellikle yeni dikilmiş küçük sürgünleri ve bunların tekil ile çoğul biçimlerini adlandırır.","neighbor_ref":"root_001637/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal hurmanın küçük ve henüz gelişmemiş örnekleriyle ilişkilidir."}],"source_phrase_ar":"الجعل النخل يفوت اليد والواحدة جعلة (maqayis)؛ الجعل واحدها جعلة وهي النخل الصغار (ayn)؛ الجعل النخل القصار الواحدة جعلة (sihah)؛ الجعل قصار النخل (tahdhib)","source_summary":"Kaynaklar kısa veya küçük hurma ağaçları anlamında ve topluluk ile tek ağaç arasındaki biçim ayrımında birleşir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الجعل للنخل الصغار أو القصار، والواحدة جعلة.","what_is_not_ar":"لا يدخل فيه جعلة اسم المكان ولا الجعل الدويبة."},"support_links":[]},{"boundary":"Dal tencereyi indirmeye yarayan ısı koruyucu bez ve onunla yapılan eylemle sınırlıdır; ücret anlamındaki benzer biçim buna girmez.","branch_kind":"bare","branch_ref":"root_000248/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:5:1:2","qac_word_ref":"87:5:1","surface_ar":"جَعَلَ"}],"gloss":"sıcak tencereyi indirme bezi ve onunla indirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sıcak tencereyi ocaktan indirirken tutmaya yarayan ve eli sıcaktan koruyan bezdir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tencereyi bu bez aracılığıyla ateşten indirme eylemini de bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem ısıdan koruyan araç adı hem de tencereyi bu araçla ocaktan indirme eylemi birlikte gösterileceğinde kullanılır.","boundary_detail":"Dal tencereyi indirmeye yarayan ısı koruyucu bez ve onunla yapılan eylemle sınırlıdır; ücret anlamındaki benzer biçim buna girmez.","branch_image_ar":"خرقة إنزال القدر","concept_gloss":"sıcak tencereyi indirme bezi ve onunla indirme","contextual_glosses":[{"applicability":"Sıcak tencereyi tutup ocaktan indirmeye yarayan bez nesne olarak anıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı bezle tencereyi indirmeyi bildiren eylem kullanımını dışarıda bırakır.","preserves":"Aracın tencereyi indirme ve eli ısıdan koruma işlevini korur."},"facet_ids":["F001"],"text":"tencereyi ateşten indirme bezi","usage_role":"contextual"},{"applicability":"Tencerenin özel bez kullanılarak ocaktan indirilmesi eylem olarak anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bezin bağımsız araç adı olarak kullanılmasını dışarıda bırakır.","preserves":"Tencereyi koruyucu bez aracılığıyla indirme işlemini korur."},"facet_ids":["F002"],"text":"tencereyi bezle ateşten indirmek","usage_role":"contextual"}],"definition":"Sıcak tencereyi ateşten veya dayandığı taşlardan indirirken kullanılan ve eli sıcaktan koruyan bezdir; bu bezle tencereyi indirme eylemi de aynı dala bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sıcak tencereyi ocaktan indirirken tutmaya yarayan ve eli sıcaktan koruyan bezdir."},{"facet_id":"F002","role":"associated_use","statement":"Tencereyi bu bez aracılığıyla ateşten indirme eylemini de bildirir."}],"identity_rationale":"Kaynak ifadesi, sıcak tencereyi ateşten veya onu taşıyan taşlardan indirirken kullanılan ve eli sıcaktan koruyan bezi açıkça tanımlar. Aynı tanıklık, tencereyi bu bezle indirme eylemini de ayrı bir türemiş kullanım olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sıcak tencereyi ateşten indirmeye yarayan koruyucu bez"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"tencereyi koruyucu bezle ateşten indirmek"}],"lexicalization_note":"Dal yalın ad ve ona bağlı eylem biçimlerini kapsar; başka dallardaki benzer sesli adlar tanıma alınmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; tencereyi yönetmeye yarayan çubuk ile onu ateşte taşıyan taş, aracın özgül işlevini en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak araç tencerenin dışından tutulmasını ve ocaktan indirilmesini sağlar; komşu araç tencerenin içine sokularak kaynamayı yatıştırır.","focus_only":"Tencereyi ocaktan indirirken kullanılan ve eli sıcaktan koruyan bir bezdir.","gloss":"tencere karıştırma çubuğu","neighbor_only":"Tencerenin içini karıştırıp kaynamasını yatıştırmak için kullanılan bir çubuktur.","neighbor_ref":"root_001676/B011","relation_type":"same_field","shared_zone":"İki araç da sıcak tencereyi güvenli biçimde yönetmeye yarayan ev gereçleridir."},{"boundary_match":"thematic_only","distinction":"Odak dal kaldırma sırasında kullanılan koruyucu aracı, komşu dal ise pişirme sırasında tencereyi taşıyan yapısal desteği adlandırır.","focus_only":"Eli koruyarak tencereyi ateşten indirmeye yarayan taşınabilir bir bezdir.","gloss":"tencereyi taşıyan üçüncü taş","neighbor_only":"Tencereyi ateş üzerinde taşımak için iki taşa eklenen üçüncü sabit destektir.","neighbor_ref":"root_000203/B007","relation_type":"thematic","shared_zone":"Her ikisi de ateş üzerindeki tencerenin kurulması ve kaldırılması senaryosunda yer alır."}],"source_phrase_ar":"الجعال الخرقة التي تنزل بها القدر عن الأثافي (maqayis)؛ الجعال والجعالة خرقة تنزل بها القدر عن رأس النار يتقى بها من الحر (ayn)؛ الجعال الخرقة التي تنزل بها القدر عن النار؛ أجعلت القدر (sihah)؛ الجعال الخرقة التي تنزل بها القدور؛ أجعلت القدر إجعالا إذا أنزلتها بالجعال (tahdhib)","source_summary":"Kaynaklar bezin tencereyi ateşten indirirken ısıdan koruma işlevinde birleşir ve aynı araçla yapılan indirme eylemini de aktarır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الجعال أو الجعالة، وهي خرقة تنزل بها القدر عن النار أو الأثافي ويتقى بها الحر.","what_is_not_ar":"لا يدخل فيه الجعالة بمعنى الأجر."},"support_links":[]},{"boundary":"Hayvanın kendisi yalın çekirdektir; suya ilişkin anlam yalnız bu hayvanların suda çok bulunmasını bildiren özel kuruluşta geçerlidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000248/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:5:1:2","qac_word_ref":"87:5:1","surface_ar":"جَعَلَ"}],"gloss":"kara küçük yer hayvanı ve bunlarla dolu su","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kara renkli küçük bir yer hayvanını adlandırır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yalnız suyla kurulan kullanımda, bu hayvanların suyun içinde çokça bulunmasını bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın hayvan adı ile yalnız bu hayvanların çokça bulunduğu suyu anlatan bağlı kullanım birlikte gösterileceğinde uygundur.","boundary_detail":"Hayvanın kendisi yalın çekirdektir; suya ilişkin anlam yalnız bu hayvanların suda çok bulunmasını bildiren özel kuruluşta geçerlidir.","branch_image_ar":"دويبة الجعلان","concept_gloss":"kara küçük yer hayvanı ve bunlarla dolu su","contextual_glosses":[{"applicability":"Canlının kendisi yalın bir ad olarak anıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu hayvanların çok bulunduğu suyu anlatan bağlı kullanımı dışarıda bırakır.","preserves":"Kara renkli küçük yer hayvanı çekirdeğini korur."},"facet_ids":["F001"],"text":"kara renkli küçük yer hayvanı","usage_role":"contextual"},{"applicability":"Suyun içinde söz konusu hayvanların çokça bulunduğu özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanın bağımsız yalın ad olarak kullanılmasını dışarıda bırakır.","preserves":"Suya bağlı hayvan çokluğu ve doluluk yönünü korur."},"facet_ids":["F002"],"text":"bu hayvanlarla dolu su","usage_role":"contextual"}],"definition":"Kara renkli küçük bir yer hayvanıdır. Buna bağlı söz öbeği, bu hayvanların içine çokça düştüğü veya içinde çoğaldığı suyu niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kara renkli küçük bir yer hayvanını adlandırır."},{"facet_id":"F002","role":"associated_use","statement":"Yalnız suyla kurulan kullanımda, bu hayvanların suyun içinde çokça bulunmasını bildirir."}],"identity_rationale":"Kaynak ifadesi, küçük bir yer hayvanını ve onun kara renkli oluşunu bildirir; ayrıca bu hayvanların çokça bulunduğu suyu niteleyen bağlı kullanımı verir. Geçici çerçeve bu iki kapsamı doğru ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kara renkli küçük bir yer hayvanı"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bu hayvanların çokça bulunduğu su"}],"lexicalization_note":"Yalın hayvan adı ile yalnız bu hayvanların çokça bulunduğu suyu niteleyen söz öbeği ayrı facetlerde tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel küçük yer hayvanları sınıfı, odak canlının belirli bir ad oluşunu açıklayan en yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir hayvan adıdır ve suya özgü türemiş kullanımı vardır; komşu dal ise birçok farklı küçük hayvanı içine alan üst sınıftır.","focus_only":"Kara renkli belirli bir küçük yer hayvanını ve ona bağlı su niteliğini adlandırır.","gloss":"küçük yer hayvanları","neighbor_only":"Küçük yer hayvanlarının pek çok türünü topluca kapsayan genel bir sınıf adıdır.","neighbor_ref":"root_000324/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal küçük ve yerde yaşayan hayvanlar alanında buluşur."}],"source_phrase_ar":"الجعل دابة من هوام الأرض (ayn)؛ الجعل دويبة؛ جعل الماء بالكسر أي كثر فيه الجعلان (sihah)؛ الجعل دابة سوداء من دواب الأرض تجمع جعلانا؛ ماء مجعل وجعل إذا تهافتت فيه الجعلان (tahdhib)","source_summary":"Kaynaklar küçük yer hayvanı anlamında birleşir; kara renk niteliğini ve hayvanların çok bulunduğu suya özgü kullanımı da topluca destekler.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه الجعل دابة أو دويبة من هوام الأرض، وجمعها جعلان، وما وصف به الماء إذا كثرت فيه الجعلان.","what_is_not_ar":"لا يدخل فيه الجعل بمعنى الأجر أو النخل."},"support_links":[]},{"boundary":"Dal dişi köpek ve benzeri yırtıcı dişilerin çiftleşme isteğiyle sınırlıdır; erkeğin isteğini veya çiftleşmenin gerçekleşmesini bildirmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000248/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:5:1:2","qac_word_ref":"87:5:1","surface_ar":"جَعَلَ"}],"gloss":"dişinin çiftleşmek için erkeği istemesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"specialization","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi köpeği, çiftleşmek için erkeği isteyen durumda niteleyen söz öbeğidir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi köpek ve diğer yırtıcı dişilerin erkeği istemesi durumunu çekimli biçimlerle bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi köpek veya benzeri yırtıcı dişinin çiftleşme isteğini bildiren hem niteleme hem eylem biçimlerini karşılar.","boundary_detail":"Dal dişi köpek ve benzeri yırtıcı dişilerin çiftleşme isteğiyle sınırlıdır; erkeğin isteğini veya çiftleşmenin gerçekleşmesini bildirmez.","branch_image_ar":"اشتهاء الأنثى للفحل","concept_gloss":"dişinin çiftleşmek için erkeği istemesi","contextual_glosses":[{"applicability":"Dişi köpek veya benzeri bir yırtıcı dişinin erkeği istediği durum niteleme olarak verildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişi hayvanın çiftleşmeye yönelik erkek isteğini korur."},"facet_ids":["F001","F002"],"text":"çiftleşmek isteyen dişi","usage_role":"contextual"}],"definition":"Dişi köpeğin veya benzeri yırtıcı bir dişinin çiftleşmek için erkeği istemesidir; hem belirli bir söz öbeği hem de çekimli biçimler bu durumu anlatır.","distinctive_facets":[{"facet_id":"F001","role":"specialization","statement":"Dişi köpeği, çiftleşmek için erkeği isteyen durumda niteleyen söz öbeğidir."},{"facet_id":"F002","role":"core","statement":"Dişi köpek ve diğer yırtıcı dişilerin erkeği istemesi durumunu çekimli biçimlerle bildirir."}],"identity_rationale":"Kaynak ifadesi, dişi köpeğin ve diğer yırtıcı dişilerin çiftleşmek üzere erkeği istemesini açıkça bildirir. Hem dişi köpekle kurulan söz öbeği hem de çekimli biçimler aynı üreme isteği durumuna bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"çiftleşmek isteyen dişi köpek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"dişinin çiftleşmek için erkeği istemesi"}],"lexicalization_note":"Dişi köpekle kurulan söz öbeği ile dişinin isteğini bildiren çekimli biçimler ayrı tutulur; kapsam genel bir yalın kök anlamına çevrilmez.","neighbor_coverage_note":"Bütün adaylar incelendi; daha geniş hayvan kapsamlı yakın ad ile dişi deveye özgü ad, tür sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın tür sınırı köpek ve benzeri yırtıcılardır; komşu dal aynı durumu daha geniş bir hayvan listesinde adlandırır.","focus_only":"Dişi köpek ve benzeri yırtıcı dişiler için belirli niteleme ve eylem biçimlerine dayanır.","gloss":"dişi hayvanın erkeği istemesi","neighbor_only":"Koyun, sığır ve keçi gibi daha geniş evcil hayvan sınıflarına da uzanır.","neighbor_ref":"root_000860/B010","relation_type":"near_synonym","shared_zone":"Dişi köpek ve yırtıcı dişilerin çiftleşme isteğinde iki dal doğrudan örtüşür."},{"boundary_match":"partial","distinction":"Çekirdek durum aynıdır, ancak tür kapsamları ayrıdır: odak dal köpek ve yırtıcı dişilere, komşu dal dişi deveye bağlıdır.","focus_only":"Dişi köpek ve diğer yırtıcı dişilerin çiftleşme isteğine özgüdür.","gloss":"dişi devenin erkeği istemesi","neighbor_only":"Aynı isteği yalnız dişi deve için adlandırır.","neighbor_ref":"root_000009/B012","relation_type":"near_synonym","shared_zone":"Her iki dal dişi hayvanın çiftleşmek üzere erkeği istemesini anlatır."}],"source_phrase_ar":"كلبة مجعل إذا أرادت السفاد (maqayis)؛ أجعلت الكبة واستجعلت فهي مجعل إذا أرادت السفاد وكذلك سائر السباع (sihah)؛ أجعلت الكلبة والسباع كلها إذا اشتهت الفحل؛ استجعلت أيضا بمعناه (tahdhib)","source_summary":"Kaynaklar dişi köpeğin ve diğer yırtıcı dişilerin çiftleşme isteğinde birleşir ve söz öbeği ile çekimli biçimleri aynı duruma bağlar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه مجعل وأجعلت واستجعلت للكلبة والسباع إذا أرادت السفاد أو اشتهت الفحل.","what_is_not_ar":"لا يدخل فيه الجعل الدويبة ولا الفعل العام جعل."},"support_links":[]},{"boundary":"Dal yalnız deve kuşunun yavrusunu adlandırır; genel yavru, başka kuş yavrusu veya deve yavrusu anlamına genişlemez.","branch_kind":"bare","branch_ref":"root_000248/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:5:1:2","qac_word_ref":"87:5:1","surface_ar":"جَعَلَ"}],"gloss":"deve kuşu yavrusu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Türü deve kuşu olan genç yavruyu bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız deve kuşunun genç yavrusu adlandırıldığında eksiksiz ve doğal karşılıktır.","boundary_detail":"Dal yalnız deve kuşunun yavrusunu adlandırır; genel yavru, başka kuş yavrusu veya deve yavrusu anlamına genişlemez.","branch_image_ar":"فرخ النعام","concept_gloss":"deve kuşu yavrusu","contextual_glosses":[{"applicability":"Canlı bir cümlede deve kuşunun yavrusundan söz edilirken doğal sözcük sırasını sağlar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Deve kuşu türünü ve yavruluk durumunu eksiksiz korur."},"facet_ids":["F001"],"text":"yavru deve kuşu","usage_role":"contextual"}],"definition":"Deve kuşunun yavrusunu adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Türü deve kuşu olan genç yavruyu bildirir."}],"identity_rationale":"Kaynak ifadesi söz konusu biçimi doğrudan deve kuşunun yavrusu olarak açıklar. Geçici çerçeve bu hayvan türü ve yaşam evresi ayrımını eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"deve kuşu yavrusu"}],"lexicalization_note":"Dal yalın ad kullanımına dayanır ve herhangi bir özel söz öbeğiyle sınırlı değildir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çok anlamlı yakın ad ile genel yavru adı, tür ve kapsam sınırlarını en yararlı biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bütünüyle deve kuşu yavrusuna bağlıdır; komşu dal aynı karşılığın yanında tür ve insan bakımından başka anlamlara da uzanır.","focus_only":"Yalnız deve kuşu yavrusunu adlandıran tek anlamlı kullanım burada esastır.","gloss":"deve kuşu yavruları ve başka topluluklar","neighbor_only":"Deve kuşu yavrusunun yanında küçük develeri ve hizmetçileri de kapsayan daha geniş bir anlam kümesi vardır.","neighbor_ref":"root_000343/B008","relation_type":"near_synonym","shared_zone":"Deve kuşunun yavrusunu adlandırma alanında iki dal örtüşür."},{"boundary_match":"partial","distinction":"Odak dal tür bakımından özeldir; komşu dal pek çok canlı türünün yavrusunu içine alan genel sınıf adıdır.","focus_only":"Yavruluğu özellikle deve kuşu türüne bağlayan özel bir addır.","gloss":"küçük yavru","neighbor_only":"İnsan, evcil hayvan ve yabanıl hayvan yavrularını genel olarak kapsar.","neighbor_ref":"root_000942/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal doğumdan sonraki genç ve küçük yaşam evresini anlatır."}],"source_phrase_ar":"الجعول ولد النعام (maqayis)؛ الجعول الرأل ولد النعام (tahdhib)","source_summary":"Kaynaklar bu adın deve kuşunun yavrusunu bildirdiği konusunda birleşir.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه الجعول بمعنى الرأل، ولد النعام.","what_is_not_ar":"لا يدخل فيه الجعل الدويبة ولا الجعل النخل."},"support_links":[]},{"boundary":"Adın gösterdiği belirli yer açıklanmadığı için tanım bir yer kimliği uydurmaz ve sözü genel yer anlamına dönüştürmez.","branch_kind":"non_bare","branch_ref":"root_000248/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:5:1:2","qac_word_ref":"87:5:1","surface_ar":"جَعَلَ"}],"gloss":"belirtilmemiş bir yer adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kimliği belirtilmeyen bir yer için kullanılan özel addır."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynağın belirli yer kimliğini açıklamadan yalnızca yer adı diye sınıflandırdığı bu özel kullanım için uygundur.","boundary_detail":"Adın gösterdiği belirli yer açıklanmadığı için tanım bir yer kimliği uydurmaz ve sözü genel yer anlamına dönüştürmez.","branch_image_ar":"الجَعْلة اسم مكان","concept_gloss":"belirtilmemiş bir yer adı","contextual_glosses":[{"applicability":"Sözün genel yer anlamı taşımadığı, yalnız özel ad olarak kullanıldığı açıklanırken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözü kimliği belirtilmemiş özel bir yer adı olarak korur."},"facet_ids":["F001"],"text":"bir yerin adı","usage_role":"explanatory"}],"definition":"Kaynağın yalnızca bir yer adı olduğunu bildirdiği, gösterdiği yer açıklanmayan özel kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kimliği belirtilmeyen bir yer için kullanılan özel addır."}],"identity_rationale":"Tek kaynak ifadesi, sözün bir yer adı olduğunu açıkça bildirir ve bundan başka bir yer kimliği veya genel anlam vermez. Geçici çerçeve bu sınırlı tanıklığı doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kimliği belirtilmemiş bir yer adı"}],"lexicalization_note":"Dal yalnız belirli ad biçimine bağlıdır; genel veya yalın bir yer anlamı olarak genişletilemez.","neighbor_coverage_note":"Bütün adaylar incelendi; adayların her biri başka ve belirli bir yer adını veya genel yer alanını gösterir, ancak odak adın hangi yerle özdeş olduğunu kanıtlamaz; bu yüzden yayımlanabilir bir karşıtlık seçilmedi.","source_phrase_ar":"الجَعْلة اسم مكان (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık sözü bir yer adı olarak sınıflandırır, fakat hangi yeri gösterdiğini açıklamaz."}],"source_summary":"Bu kullanım tek bir tanıklıkla sınırlıdır ve yerin kimliğine ilişkin ek bir ortak açıklama bulunmaz.","sources":["MQ"],"what_is_ar":"يدخل فيه الجعلة حين يصرح المصدر بأنها اسم مكان.","what_is_not_ar":"لا يدخل فيه الجعلة الواحدة من النخل الصغار."},"support_links":[]},{"boundary":"Üç nitelik birlikte kurucudur; yalnız kısa, yalnız şişman veya yalnız inatçı olan biri bu dalın tam kapsamına girmez.","branch_kind":"bare","branch_ref":"root_000248/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:5:1:2","qac_word_ref":"87:5:1","surface_ar":"جَعَلَ"}],"gloss":"kısa, şişman ve inatçı olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kısa, şişman ve tartışmada inatla direnen kişiyi üç niteliği birlikte taşıyarak betimler."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişide beden kısalığı, şişmanlık ve inatçı çekişkenlik birlikte anlatıldığında tam karşılık verir.","boundary_detail":"Üç nitelik birlikte kurucudur; yalnız kısa, yalnız şişman veya yalnız inatçı olan biri bu dalın tam kapsamına girmez.","branch_image_ar":"قصر مع سمن ولجاج","concept_gloss":"kısa, şişman ve inatçı olma","contextual_glosses":[{"applicability":"Üç niteliği birlikte taşıyan bir kişiyi doğal cümle içinde nitelemek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiyi belirleyen üç kurucu niteliğin tümünü birlikte korur."},"facet_ids":["F001"],"text":"kısa, şişman ve inatçı biri","usage_role":"contextual"}],"definition":"Bir kişide kısalık, şişmanlık ve inatçı çekişkenliğin birlikte bulunmasını anlatan nitelemedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kısa, şişman ve tartışmada inatla direnen kişiyi üç niteliği birlikte taşıyarak betimler."}],"identity_rationale":"Tek kaynak ifadesi, bir kişide kısalık, şişmanlık ve inatçı çekişkenliğin birlikte bulunmasını tek bir betimleyici anlam olarak verir. Geçici çerçeve bu üç kurucu niteliği doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kısa, şişman ve inatçı kişi"}],"lexicalization_note":"Dal yalın betimleyici kullanıma dayanır ve özel bir söz öbeğiyle sınırlı değildir.","neighbor_coverage_note":"Bütün adaylar incelendi; kısa ve toplu kişi betimi ile genel beden dolgunluğu, üç niteliğin birlikte bulunması koşulunu en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bedensel kısalık ve şişmanlığa davranışsal inatçılığı ekler; komşu dal ise bedensel kalınlık ve gücü öne çıkarır.","focus_only":"Şişmanlık ile tartışmada inatla direnme niteliklerini kısalıkla birlikte gerektirir.","gloss":"kısa, kalın ve güçlü kişi","neighbor_only":"Kalın, güçlü ve toplu beden yapısını bildirir, fakat inatçılığı gerektirmez.","neighbor_ref":"root_001315/B008","relation_type":"near_synonym","shared_zone":"Kısa ve toplu beden yapısına sahip kişiyi betimlemede iki dal örtüşür."},{"boundary_match":"partial","distinction":"Odak dal üçlü bir kişi niteliğidir; komşu dal yalnız bedensel dolgunluğu seçer ve farklı canlı türlerine de uygulanabilir.","focus_only":"Kısalık ve inatçı çekişkenliği şişmanlıkla birlikte zorunlu kılar.","gloss":"bedenin dolgun ve şişman olması","neighbor_only":"İnsan veya hayvanda bedenin dolgunlaşıp yağlanmasını anlatır, boy ve huy koşulu taşımaz.","neighbor_ref":"root_000352/B006","relation_type":"near_neighbor","shared_zone":"Şişmanlık ve beden dolgunluğu anlam alanında iki dal buluşur."}],"source_phrase_ar":"الجعل القصر مع السمن واللجاج (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık üç niteliği ayırmadan kısa, şişman ve inatçı kişi betimlemesinde birleştirir."}],"source_summary":"Bu birleşik kişi betimlemesi tek bir tanıklığa dayanır; kısalık, şişmanlık ve inatçı çekişkenlik birlikte verilir.","sources":["TA"],"what_is_ar":"يدخل فيه الجعل بمعنى اجتماع القصر والسمن واللجاج في وصف الشخص.","what_is_not_ar":"لا يدخل فيه قصر النخل ولا الدويبة المسماة جعلا."},"support_links":[]},{"boundary":"Dalın eylem çekirdeği toplama, güvenceye alma ve denetim kurmadır; hak kazanma sonrasında sahip olma ise ayrı kişi adı uzantısıdır.","branch_kind":"bare","branch_ref":"root_000374/B001","candidate_links":[{"candidate_id":"cand_8b3cceff415da6700cec","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْوَىٰ","morph_features":"STEM|POS:ADJ|LEM:>aHowaY`|ROOT:Hwy|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:5:3:1","qac_word_ref":"87:5:3","surface_ar":"أَحْوَىٰ"}],"gloss":"toplayıp güvenceye veya denetim altına alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dağınık ya da dışarıdaki bir şeyi toplama ve güvenceye alma işlemi vardır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toplanan şey kişinin kendi denetimine veya tasarrufuna geçirilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hak kazanmanın ardından sahip olma durumu da aynı anlam alanına girer."}}],"root_ar":"ح و ي","root_id":"root_000374","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin toplanarak güvenceye alındığı veya kişinin denetimine geçirildiği genel eylem kullanımlarında uygundur.","boundary_detail":"Dalın eylem çekirdeği toplama, güvenceye alma ve denetim kurmadır; hak kazanma sonrasında sahip olma ise ayrı kişi adı uzantısıdır.","branch_image_ar":"الجمع والإحراز والاحتواء","concept_gloss":"toplayıp güvenceye veya denetim altına alma","contextual_glosses":[{"applicability":"Nesne veya malın bir araya getirilmesi ve korunması öne çıktığında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Denetimi ele geçirme ile hak kazanıldıktan sonraki sahiplik sonucunu belirtmez.","preserves":"Toplama ve güvenceye alma işlemlerini açık biçimde korur."},"facet_ids":["F001"],"text":"toplayıp güvenceye almak","usage_role":"contextual"},{"applicability":"Bir şeyin kişinin tasarrufuna veya egemenliğine geçmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Önceki toplama işlemini ve hak kazanma sonrasındaki sahiplik niteliğini dışarıda bırakır.","preserves":"Bir şeyi kişinin kendi denetimine geçirme yönünü korur."},"facet_ids":["F002"],"text":"üzerinde denetim kurmak","usage_role":"contextual"}],"definition":"Bir şeyi ya da malı bir araya getirip güvenceye almak veya onu kendi denetimine geçirmektir; aynı anlam alanındaki kişi adı, hak kazandıktan sonra sahip olanı belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dağınık ya da dışarıdaki bir şeyi toplama ve güvenceye alma işlemi vardır."},{"facet_id":"F002","role":"extension","statement":"Toplanan şey kişinin kendi denetimine veya tasarrufuna geçirilir."},{"facet_id":"F003","role":"extension","statement":"Hak kazanmanın ardından sahip olma durumu da aynı anlam alanına girer."}],"identity_rationale":"Kaynak ifadesi, bir şeyi ya da malı toplama ve güvenceye alma çekirdeğini, onu kendi denetimine geçirme uzantısını ve ayrı bir kişi adında hak kazanıldıktan sonra sahip olmayı açıkça destekler. Geçici dal çerçevesi bu ilişkili kullanımları doğru biçimde bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi toplamak ve güvenceye almak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"üzerinde denetim kurup kendi tasarrufuna almak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"hak kazandıktan sonra sahip olan kimse"}],"lexicalization_note":"Tanım yalın dalı kapsar; başka dallardaki renk, bitki, bağırsak, binek ve su yapısı anlamları buraya taşınmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; renk, bitki, organ, binek ve su yapısı dalları yalnızca kök ilişkisi taşıdığı için yayımlanmadı, en yakın üç sınır karşılaştırması seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal toplama ile haklı sahipliğe uzanan çizgiyi izler; komşu dal ise üstün gelme ve yönlendirme gibi güç kullanımını da kapsayan daha geniş bir denetim alanına sahiptir.","focus_only":"Hak kazanma sonrasındaki sahiplik, odak dalda açık bir sonuçtur.","gloss":"toplayıp ele geçirme","neighbor_only":"Üstün gelme, kuşatma ve bir şeyi belirlenen yöne sürme gibi daha geniş eylemler komşuda bulunur.","neighbor_ref":"root_000368/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da toplama, bir araya getirme ve bir şey üzerinde denetim kurma alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal korunan alan ve çevrelenmiş yer düşüncesini de taşır; odak dalın sınırı ise toplama, denetim ve haklı sahiplik sürecidir.","focus_only":"Odak dal hak kazanıldıktan sonra sahip olmayı ayrıca belirtir.","gloss":"kendi alanına katma","neighbor_only":"Korunan alan, çevrili bölge ve kişiye ait doğal alan gibi mekansal kullanımlar komşuya özgüdür.","neighbor_ref":"root_000370/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi toplayıp kişinin kendi denetim alanına katmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dal toplama ve denetime alma sürecine dayanır; komşu dal edinilen şeyi kullanım veya birikim amacıyla elde tutma niyetini sınır olarak koyar.","focus_only":"Bir şeyi toplama ve üzerinde denetim kurma işlemi odak dalın çekirdeğidir.","gloss":"edinip elde tutma","neighbor_only":"Bir şeyi satmak veya ticaretini yapmak için değil, elde tutmak üzere edinme koşulu komşuya özgüdür.","neighbor_ref":"root_001264/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir şeyin kişinin malı veya tasarrufu haline gelmesiyle ilgilidir."}],"source_phrase_ar":"حويت الشيء أحويه حيا إذا جمعته (maqayis)؛ حوى فلان مالا حيا وحواية أي جمعه وأحرزه واحتوى عليه (ayn;tahdhib)؛ احتوى فلان على كذا إذا استولى عليه (jamhara)؛ حواه يحويه حيا أي جمعه واحتواه مثله (sihah)؛ الحوي المالك بعد استحقاق (tahdhib)","source_summary":"Kaynakların ortak çizgisi toplama, güvenceye alma ve kişinin denetimine geçirmedir; toplu kanıttaki ayrı kişi adı ise hak kazanıldıktan sonra sahip olanı belirtir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه حوى الشيء أو المال بمعنى جمعه وأحرزه، واحتوى عليه أو استولى عليه، والملك بعد استحقاق.","what_is_not_ar":"لا يدخل فيه لون الأحوى، ولا الحواء النبات، ولا الأمعاء أو مراكب الحوية إلا من جهة الاشتقاق أو التشبيه."},"support_links":["sup_ea7f41da09281fecc31c"]},{"boundary":"Toplanma ancak dairesel bir biçime veya kıvrılmaya dönüştüğü ölçüde bu dala girer; sıradan toplama yeterli değildir.","branch_kind":"bare","branch_ref":"root_000374/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْوَىٰ","morph_features":"STEM|POS:ADJ|LEM:>aHowaY`|ROOT:Hwy|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:5:3:1","qac_word_ref":"87:5:3","surface_ar":"أَحْوَىٰ"}],"gloss":"toplanıp dairesel biçimde kıvrılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Toplanma ile dairesel biçim alma veya kendi üzerine kıvrılma birlikte gerçekleşir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yılanın kıvrılması ve bazı yıldızların yuvarlak bir düzende sıralanması bu biçimin örnekleridir."}}],"root_ar":"ح و ي","root_id":"root_000374","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir varlığın kendi üzerine toplanıp yuvarlak veya halka benzeri biçim aldığı genel durumları karşılar.","boundary_detail":"Toplanma ancak dairesel bir biçime veya kıvrılmaya dönüştüğü ölçüde bu dala girer; sıradan toplama yeterli değildir.","branch_image_ar":"استدارة الشيء والتفافه","concept_gloss":"toplanıp dairesel biçimde kıvrılma","contextual_glosses":[{"applicability":"Yılan gibi uzamış bir varlığın kendi üzerine kıvrıldığı hareketli bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hareketsiz öğelerin dairesel bir düzende sıralanması kullanımını kapsamaz.","preserves":"Kendi üzerine kıvrılma ve halka biçimi kazanma yönünü korur."},"facet_ids":["F001","F002"],"text":"kıvrılıp halka olmak","usage_role":"contextual"},{"applicability":"Yıldızlar gibi ayrı öğelerin yuvarlak bir sıra oluşturduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir varlığın kendi üzerine kıvrılarak toplanması hareketini belirtmez.","preserves":"Öğelerin dairesel biçimde düzenlenmesi sonucunu korur."},"facet_ids":["F002"],"text":"dairesel düzene girmek","usage_role":"contextual"}],"definition":"Bir şeyin kendi üzerine toplanarak dairesel biçim alması veya kıvrılıp halka benzeri bir düzen oluşturmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Toplanma ile dairesel biçim alma veya kendi üzerine kıvrılma birlikte gerçekleşir."},{"facet_id":"F002","role":"example","statement":"Yılanın kıvrılması ve bazı yıldızların yuvarlak bir düzende sıralanması bu biçimin örnekleridir."}],"identity_rationale":"Kaynak ifadesi her tür şeyin dairesel biçim almasını, özellikle yılanın kendi üzerine kıvrılmasını ve yıldızların yuvarlak bir düzende toplanmasını aynı çekirdekte birleştirir. Geçici çerçeve bu biçimsel hareketi doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"dairesel biçimde kıvrılma"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"toplanıp kıvrılarak halka olmak"}],"lexicalization_note":"Tanım yalın biçimde dairesel kıvrılma ve düzenlenmeyi kapsar; belirli bir nesneye veya kalıba bağlı değildir.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; halka, çember ve bükülme alanındaki üç aday sınırı keskinleştirdi, nesne adı veya yalnızca kök ortaklığı taşıyan adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal toplanıp kıvrılarak biçim almayı gerektirir; komşu dal ise bir nesnenin yalnızca dönmesini de kapsayan daha genel bir hareket çekirdeğine sahiptir.","focus_only":"Kendi üzerine toplanma, odak dalın dairesel biçimi kuran belirgin bileşenidir.","gloss":"dairesel kıvrılma","neighbor_only":"Genel dönme hareketi, dairesel biçim oluşmasa da komşu dalın kapsamındadır.","neighbor_ref":"root_001177/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da yuvarlaklık, dairesel hareket veya dairesel biçim alanında güçlü biçimde örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal dönme, döndürme ve dairesel nesnelerin genel alanını kapsar; odak dal yalnızca toplanarak kıvrılma veya yuvarlak düzene girme biçimine odaklanır.","focus_only":"Toplanma ve kendi üzerine kıvrılma odak dalda kurucu niteliktedir.","gloss":"dönme ve daireselleşme","neighbor_only":"Döndürme, yörünge, daire ve çevreleme araçları komşunun daha geniş kapsamındadır.","neighbor_ref":"root_000499/B001","relation_type":"near_synonym","shared_zone":"İki dal da dairesel biçim ve çevresel hareket düşüncesini paylaşır."},{"boundary_match":"partial","distinction":"Odak dalın sonucu dairesel toplanmadır; komşu dalın çekirdeği ise bir şeyi eğip bükerek yönünü veya biçimini değiştirmektir.","focus_only":"Kıvrılmanın dairesel bir düzen veya halka benzeri sonuç vermesi odak dala özgüdür.","gloss":"bükülme ve kıvrılma","neighbor_only":"Bükme, eğme ve yönünden saptırma, dairesellik olmadan da komşu dalda gerçekleşebilir.","neighbor_ref":"root_001388/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da düz biçimin bozulup kıvrımlı hale gelmesini içerebilir."}],"source_phrase_ar":"الحوي استدارة كل شيء كحوي الحية وكحوي بعض النجوم (ayn;tahdhib)؛ تحوى أي تجمع واستدار يقال تحوت الحية (sihah)","source_summary":"Kaynaklar dairesel biçim alma çekirdeğinde birleşir; yılanın kıvrılması hareketli, yıldızların yuvarlak düzeni ise konumsal bir örnek verir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه الحوي بمعنى استدارة كل شيء، كحوي الحية وتحويها، وانتظام النجوم على نسق مستدير.","what_is_not_ar":"لا يدخل فيه مجرد جمع المال أو الاستيلاء عليه، ولا أسماء الأمعاء والحوية إلا حيث يصرح المصدر بالتشبيه بالالتفاف."},"support_links":[]},{"boundary":"Dal yalnızca karın içindeki bağırsak ve kıvrımlı iç bölüm adlarını kapsar; aynı biçimdeki binek veya su yapısı adları dışarıdadır.","branch_kind":"bare","branch_ref":"root_000374/B003","candidate_links":[{"candidate_id":"cand_5850328ea1db625cb7d4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْوَىٰ","morph_features":"STEM|POS:ADJ|LEM:>aHowaY`|ROOT:Hwy|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:5:3:1","qac_word_ref":"87:5:3","surface_ar":"أَحْوَىٰ"}],"gloss":"bağırsaklar ve karındaki kıvrımlı bölümleri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Karın içindeki bağırsaklar ve onların tekil bölümleri temel gönderimi oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koyunun karnındaki halka biçimli bölüm ve geleneksel olarak süt kızları diye adlandırılan iç kısımlar özel kullanımlardır."}}],"root_ar":"ح و ي","root_id":"root_000374","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bağırsakların bütünüyle tek tek kıvrımlı iç bölümlerini birlikte temsil eden genel anatomik karşılıktır.","boundary_detail":"Dal yalnızca karın içindeki bağırsak ve kıvrımlı iç bölüm adlarını kapsar; aynı biçimdeki binek veya su yapısı adları dışarıdadır.","branch_image_ar":"الحوايا: الأمعاء والدوارات الباطنة","concept_gloss":"bağırsaklar ve karındaki kıvrımlı bölümleri","contextual_glosses":[{"applicability":"Organların topluca anıldığı sıradan anatomik bağlamlarda en doğal kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Koyunun karnındaki özel halka biçimli bölüm ve geleneksel alt adlandırmalar görünmez olur.","preserves":"Temel anatomik bağırsak gönderimini eksiksiz biçimde korur."},"facet_ids":["F001"],"text":"bağırsaklar","usage_role":"general"},{"applicability":"Tek bir iç bölümün biçimi ve karındaki konumu açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bağırsakların çoğul ve genel adı olarak kullanılma kapsamını dışarıda bırakır.","preserves":"Tekil, kıvrımlı ve karın içinde bulunan bağırsak bölümü yönünü korur."},"facet_ids":["F002"],"text":"kıvrımlı bağırsak bölümü","usage_role":"explanatory"}],"definition":"Karın içindeki bağırsakların ve özellikle kendi üzerine dönen kıvrımlı bağırsak bölümlerinin adıdır; koyunun karnındaki halka biçimli iç bölüm de bu kapsamdadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Karın içindeki bağırsaklar ve onların tekil bölümleri temel gönderimi oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Koyunun karnındaki halka biçimli bölüm ve geleneksel olarak süt kızları diye adlandırılan iç kısımlar özel kullanımlardır."}],"identity_rationale":"Kaynak ifadesi farklı tekil ve çoğul biçimleri bağırsaklar, karın içindeki kıvrımlı bölümler ve özellikle koyunun karnındaki halka biçimli iç bölüm için birlikte verir. Geçici dal tanımı bu anatomik kümeyi doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bağırsak veya bağırsakların bir bölümü"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bağırsağın kıvrımlı bir bölümü"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bağırsakların tek bir kıvrımlı bölümü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bağırsaklar ve karındaki kıvrımlı iç bölümler"}],"lexicalization_note":"Tanım yalın anatomik dalı kapsar ve benzer sözcük biçimleriyle adlandırılan binek ya da su tutma yapılarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğrudan bağırsak gönderimi taşıyan üçü yayımlandı, yağ, sırt eti, açlık sözü ve öteki kök dalları yalnızca aynı anatomi alanında kaldı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek gönderim ve anatomik sınır aynıdır; farklı adlandırma biçimleri bu tam örtüşmeyi bozmaz.","focus_only":null,"gloss":"bağırsak","neighbor_only":null,"neighbor_ref":"root_001435/B001","relation_type":"synonym","shared_zone":"Her iki dal da karın içinde uzanıp kıvrılan bağırsakları ve bunların bölümlerini gösterir."},{"boundary_match":"partial","distinction":"Anatomik çekirdek yakındır, ancak komşu dal bağırsak adından türeyen niteliksiz hurma kullanımını da içerdiği için sınırlar tam değildir.","focus_only":"Odak dal bağırsakları çoğul bütün ve kıvrımlı iç bölümler olarak adlandırır.","gloss":"bağırsak ve bağırsak bölümü","neighbor_only":"Niteliksiz hurma için kullanılan benzetmeli ad komşu dalın ek kapsamıdır.","neighbor_ref":"root_001428/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da karın içindeki bağırsak veya tek bir bağırsak bölümünü gösterebilir."},{"boundary_match":"partial","distinction":"Odak dal genel anatomik adlandırmadır; komşu dal bağırsakları içeriğin toplandığı belirli bölümler olarak sınırlar.","focus_only":"Odak dal bağırsakların genelini ve farklı kıvrımlı bölümlerini kapsar.","gloss":"içeriğin toplandığı bağırsaklar","neighbor_only":"Dışkının toplandığı bağırsak bölümlerine yönelik daha dar işlevsel belirleme komşuya özgüdür.","neighbor_ref":"root_001414/B008","relation_type":"near_synonym","shared_zone":"İki dal da karın içindeki bağırsak bölümlerine gönderimde bulunur."}],"source_phrase_ar":"الحوية والواحدة من الحوايا وهي الأمعاء (maqayis)؛ الحوية والحاوية والجميع الحوايا الأمعاء (ayn)؛ الحاوية والحاوياء الأمعاء التي تسمى بنات اللبن (jamhara)؛ حوية البطن وحاوية البطن وحاوياء البطن كله بمعنى وجمع الحوية حوايا وهي الأمعاء (sihah)؛ هي المباعر وبنات اللبن وهي الحواية والحاوية وهي الدوارة التي في بطن الشاة (tahdhib)","source_summary":"Kaynaklar temel olarak bağırsak gönderiminde birleşir; tekil biçimler bağırsakların bir bölümünü, çoğul biçim ise kıvrımlı iç bölümlerin bütününü gösterebilir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الحوية والحاوية والحاوياء والحوايا بمعنى الأمعاء، وبنات اللبن، والدوارة التي في بطن الشاة، وحوية البطن.","what_is_not_ar":"لا يدخل فيه الحوية التي على ظهر البعير أو مركب المرأة، ولا الحوايا المساطح وحفائر الماء."},"support_links":["sup_33053778a4e67dd75312"]},{"boundary":"Kadın bineği ile hörgüç çevresindeki binme örtüsü iki ayrı gerçekleşmedir; tanım bunları tek bir melez nesne saymaz.","branch_kind":"bare","branch_ref":"root_000374/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْوَىٰ","morph_features":"STEM|POS:ADJ|LEM:>aHowaY`|ROOT:Hwy|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:5:3:1","qac_word_ref":"87:5:3","surface_ar":"أَحْوَىٰ"}],"gloss":"kadın bineği veya hörgüç çevresine sarılan binme minderi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadının binmesi için hazırlanan, mahfeye benzeyen bir taşıma düzeneği olabilir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Deve hörgücünün çevresine sarılan ve binme yüzeyi oluşturan dolgulu bir örtü olabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çoğul biçim, kişinin bineği üzerindeyken ölümle karşılaşabileceğini anlatan kalıplaşmış bir sözde binekleri gösterir."}}],"root_ar":"ح و ي","root_id":"root_000374","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Adın hem kadın taşıma düzeneğini hem de deve üzerindeki dolgulu binme örtüsünü kapsaması gerektiğinde kullanılır.","boundary_detail":"Kadın bineği ile hörgüç çevresindeki binme örtüsü iki ayrı gerçekleşmedir; tanım bunları tek bir melez nesne saymaz.","branch_image_ar":"الحوية: مركب أو كساء يحوي الراكب والسنام","concept_gloss":"kadın bineği veya hörgüç çevresine sarılan binme minderi","contextual_glosses":[{"applicability":"Kadının taşıma düzeneğine bindiği bağlamlarda doğal ve açıklayıcıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deve hörgücünü çevreleyen dolgulu örtü kullanımını kapsamaz.","preserves":"Kadın için hazırlanmış taşıma ve binme düzeneği kullanımını korur."},"facet_ids":["F001"],"text":"kadınlar için kapalı binek","usage_role":"contextual"},{"applicability":"Devenin hörgücü çevresine sarılan örtünün yapısı ve işlevi anlatılırken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kadınlar için hazırlanan ayrı taşıma düzeneği kullanımını dışarıda bırakır.","preserves":"Hörgücü çevreleme, dolgu ve üzerine binme işlevlerini korur."},"facet_ids":["F002"],"text":"hörgüç çevresi binme minderi","usage_role":"explanatory"}],"definition":"Kadınlar için hazırlanmış mahfe benzeri bir binek ya da deve hörgücünün çevresine sarılıp üzerine binilen dolgulu örtüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadının binmesi için hazırlanan, mahfeye benzeyen bir taşıma düzeneği olabilir."},{"facet_id":"F002","role":"core","statement":"Deve hörgücünün çevresine sarılan ve binme yüzeyi oluşturan dolgulu bir örtü olabilir."},{"facet_id":"F003","role":"associated_use","statement":"Çoğul biçim, kişinin bineği üzerindeyken ölümle karşılaşabileceğini anlatan kalıplaşmış bir sözde binekleri gösterir."}],"identity_rationale":"Kaynak ifadesi aynı ad altında iki açık gerçekleşme verir: kadın için hazırlanan mahfe benzeri bir binek ve deve hörgücünün çevresine sarılıp üzerine binilen dolgulu örtü. Dal çerçevesi bu iki yerleşik kullanımı birbirine karıştırmadan koruyabilir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kadın bineği veya hörgüç çevresine sarılan binme minderi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"üzerine binilen taşıma düzenekleri"}],"lexicalization_note":"Tanım, yalın adın iki binek kullanımını kapsar; bağırsak veya su çukuru anlamı bu biçim benzerliğinden çıkarılmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; kadın bineği ve deve sırtı örtüsüyle doğrudan örtüşen üç aday seçildi, yalnızca aynı taşıma alanında kalan araçlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtü kullanımında güçlü örtüşme vardır; odak dal ayrıca kadın bineğini adlandırırken komşu dal sırt örtüsü ve semer türlerinde daha geneldir.","focus_only":"Kadınlar için hazırlanan mahfe benzeri ayrı binek odak dalın ek kapsamıdır.","gloss":"deve sırtı binme örtüsü","neighbor_only":"Genel eyer örtüsü ve yük semeri türleri komşu dalda daha geniş yer tutar.","neighbor_ref":"root_000766/B010","relation_type":"near_synonym","shared_zone":"Her iki dal da deve sırtına veya hörgüç çevresine yerleştirilen binme örtüsünü kapsar."},{"boundary_match":"partial","distinction":"Odak dal örtü yanında bir kadın bineğini de kapsar; komşu dal ise arkadaki yolcunun bindiği örtüden kap parçalarına uzanan benzetmeli kullanımlara sahiptir.","focus_only":"Kadın taşıma düzeneği odak dalda bulunur.","gloss":"hörgüç çevresi binme örtüsü","neighbor_only":"Kabın kulpu veya çentiği için yapılan benzetmeli kullanımlar komşuya özgüdür.","neighbor_ref":"root_001309/B003","relation_type":"near_synonym","shared_zone":"İki dal da deve hörgücüne veya sağrısına sarılan ve binmeyi sağlayan örtüyü gösterebilir."},{"boundary_match":"partial","distinction":"Kadın bineği kullanımında yakınlık vardır, fakat komşu dal örtülme biçimiyle tanımlanan özel bir taşıttır; odak dal ayrıca deve üzerindeki binme minderini kapsar.","focus_only":"Hörgüç çevresindeki dolgulu binme örtüsü odak dala özgüdür.","gloss":"örtülü kadın bineği","neighbor_only":"Kumaşla örtülme ve kubbeli olmama ayrımı komşu bineğin belirleyici sınırıdır.","neighbor_ref":"root_000343/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da kadınların bindiği, örtülü ve mahfe benzeri bir taşıma düzeneğini anlatır."}],"source_phrase_ar":"الحوية كساء يحوي حول سنام البعير ثم يركب (maqayis;tahdhib)؛ الحوية مركب يهيأ للمرأة (ayn;tahdhib)؛ الحوية مركب من مراكب النساء ليس بحدج ولا هودج (jamhara)؛ الحوية كساء محشو يدار حول سنام البعير (sihah)؛ الحوية شبيهة بالمحفة تركبها النساء (jamhara)","source_summary":"Kaynaklar kadın bineği ile hörgüç çevresindeki dolgulu binme örtüsünü aynı adın iki kullanımı olarak verir; ikisinin ortak noktası binme ve taşıma işlevidir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الحوية مركبا يهيأ للمرأة، وشبيهة المحفة، والكساء المحشو أو الذي يحوي حول سنام البعير ثم يركب.","what_is_not_ar":"لا يدخل فيه الحوايا الأمعاء، ولا الحوايا حفائر الماء، ولا عموم الجمع والإحراز."},"support_links":[]},{"boundary":"Dalın odağı barınakların yakın birlikteliğidir; sırf komşuluk ilişkisi veya açık yerleşim alanı tek başına yeterli değildir.","branch_kind":"bare","branch_ref":"root_000374/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْوَىٰ","morph_features":"STEM|POS:ADJ|LEM:>aHowaY`|ROOT:Hwy|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:5:3:1","qac_word_ref":"87:5:3","surface_ar":"أَحْوَىٰ"}],"gloss":"tek barınak veya yakın barınaklardan oluşan yerleşim kümesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tek bir çadır veya ev, adın en küçük yerleşim gönderimi olabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birbirine yakın kurulmuş çadır ve evlerden oluşan toplu konaklama alanını gösterir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı konaklama kümesinde yaşayan insan topluluğu da yerleşim üzerinden adlandırılabilir."}}],"root_ar":"ح و ي","root_id":"root_000374","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek bir çadırdan aynı yerde toplanmış ev ve çadırların bütününe uzanan genel yerleşim kullanımlarını kapsar.","boundary_detail":"Dalın odağı barınakların yakın birlikteliğidir; sırf komşuluk ilişkisi veya açık yerleşim alanı tek başına yeterli değildir.","branch_image_ar":"الحواء والمحوى: اجتماع البيوت والأخبية","concept_gloss":"tek barınak veya yakın barınaklardan oluşan yerleşim kümesi","contextual_glosses":[{"applicability":"Birbirine yakın kurulmuş birden çok çadırın oluşturduğu konaklama alanı anlatılırken doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir ev kullanımını ve yerleşimde yaşayan insan topluluğu uzantısını kapsamaz.","preserves":"Yakın barınakların oluşturduğu toplu konaklama yapısını korur."},"facet_ids":["F002"],"text":"çadır kümesi","usage_role":"contextual"},{"applicability":"Aynı çadır veya ev kümesinde yaşayan insanların birlikte anıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Barınakların kendisini ve tek bir ev ya da çadır gönderimini belirtmez.","preserves":"Ortak bir konaklama kümesine bağlı insan topluluğu yönünü korur."},"facet_ids":["F003"],"text":"konaklama topluluğu","usage_role":"contextual"}],"definition":"Tek bir çadır veya evden, birbirine yakın kurulmuş çadır ve evlerin oluşturduğu konaklama kümesine ve bu kümede yaşayan topluluğa uzanan yerleşim birimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tek bir çadır veya ev, adın en küçük yerleşim gönderimi olabilir."},{"facet_id":"F002","role":"extension","statement":"Birbirine yakın kurulmuş çadır ve evlerden oluşan toplu konaklama alanını gösterir."},{"facet_id":"F003","role":"extension","statement":"Aynı konaklama kümesinde yaşayan insan topluluğu da yerleşim üzerinden adlandırılabilir."}],"identity_rationale":"Kaynak ifadesi tek bir barınağı, birbirine yakın kurulmuş çadır ve ev topluluğunu ve bu yerleşimin halkını aynı yerleşim örgüsü içinde sunar. Geçici çerçeve, tek yapıdan kümeye uzanan bu kapsamı doğru taşır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"tek çadır veya yakın çadırlardan oluşan konaklama kümesi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"konaklama kümeleri"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"topluluğun evlerinin bir araya geldiği yer"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"toplu konaklama yeri"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"aynı konaklama kümesinde yaşayan topluluk"}],"lexicalization_note":"Tanım yalın yerleşim ve barınak dalını kapsar; bitki ve renk anlamlarıyla ya da özel topluluk adlarıyla genişletilmez.","neighbor_coverage_note":"Tüm adaylar incelendi; barınak kümesi, tek çadır ve yakınlık ilişkisi sınırını en iyi gösteren üçü seçildi, avlu ve açık alan adayları farklı çekirdek taşıdığı için elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tek barınaktan yakın barınaklar yerleşimine uzanır; komşu dal ise özellikle evler ve insanlardan oluşan bir parçayı adlandırır.","focus_only":"Tek bir ev veya çadır da odak dalın gönderimi olabilir.","gloss":"evler ve insanlar kümesi","neighbor_only":"İnsan topluluğunun bir parçası olma vurgusu komşuda daha doğrudandır.","neighbor_ref":"root_000389/B011","relation_type":"near_synonym","shared_zone":"Her iki dal da bir arada bulunan evler ile o evlere bağlı insan topluluğunu gösterebilir."},{"boundary_match":"partial","distinction":"Komşu dal yapım malzemesi ve çadır türüyle sınırlıdır; odak dal tek çadırın yanı sıra birbirine yakın barınaklardan oluşan yerleşimi de kapsar.","focus_only":"Birden çok yakın barınağın oluşturduğu yerleşim kümesi odak dalda kurucu bir kapsamdır.","gloss":"göçebe çadırı","neighbor_only":"Belirli göçebe çadırının kıl, yün veya hayvan lifinden yapılması komşuya özgüdür.","neighbor_ref":"root_000384/B004","relation_type":"near_synonym","shared_zone":"Odak dalın tek barınak kullanımı ile komşunun göçebe çadırı gönderimi örtüşebilir."},{"boundary_match":"partial","distinction":"Odak dal yakınlıktan doğan yerleşim birimini adlandırır; komşu dal ise yerleşimin kendisini değil, öğeler arasındaki komşuluk ve yakınlık ilişkisini anlatır.","focus_only":"Somut barınak veya barınaklar kümesi odak dalın gönderimidir.","gloss":"yakın komşuluk","neighbor_only":"Nesneler veya topluluklar arasındaki soyut yakınlık ilişkisi komşuda da bulunabilir.","neighbor_ref":"root_000037/B006","relation_type":"near_neighbor","shared_zone":"İki dal da evlerin ve toplulukların birbirine yakın bulunması durumuyla ilgilidir."}],"source_phrase_ar":"الحي من أحياء العرب والحواء البيت الواحد (maqayis)؛ الحواء جماعة بيوت من الناس مجتمعة والجمع الأحوية وهي من الوبر (sihah)؛ الحواء أخبية تدانى بعضها من بعض وهم أهل حواء واحد وجمع الحواء أحوية (tahdhib)؛ لمجتمع بيوت الحي محوى وحواء ومحتوى والجميع أحوية ومحاء (tahdhib)","source_summary":"Kaynaklar barınak ile toplu yerleşim arasında kapsam farkı gösterir: ad kimi yerde tek evi, kimi yerde bitişik çadır ve evlerin tümünü ve oradaki topluluğu belirtir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الحواء بيتا واحدا أو جماعة بيوت وأخبية متدانية، ومجتمع بيوت الحي، ومحوى ومحتوى بهذا المعنى.","what_is_not_ar":"لا يدخل فيه بنو حاء اسما لقبيلة، ولا الحواء النبات، ولا الحوة اللون."},"support_links":[]},{"boundary":"Dal doğrudan siyahı ve siyaha yaklaşan veya siyahla karışan koyu renkleri; bunların hayvan, dudak ya da bitki görünümündeki gerçekleşmelerini kapsar.","branch_kind":"bare","branch_ref":"root_000374/B006","candidate_links":[{"candidate_id":"cand_69fcf9534f45539b2909","lane":"micro"},{"candidate_id":"cand_5fdeb0d46f7fbdc0b8d9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْوَىٰ","morph_features":"STEM|POS:ADJ|LEM:>aHowaY`|ROOT:Hwy|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:5:3:1","qac_word_ref":"87:5:3","surface_ar":"أَحْوَىٰ"}],"gloss":"siyah veya siyaha çalan koyu kızıl, esmer ya da yeşil renk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Renk doğrudan siyah olabilir ya da siyaha yaklaşan veya siyahla karışan koyu bir ton olabilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atlarda koyu siyah ile koyu kızıl arasında bir don veya sırtı kızıl koyu görünüm olabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dudaktaki koyu esmerlik ile siyah ve sarının karıştığı koyu yeşil görünüm de kapsama girer."}}],"root_ar":"ح و ي","root_id":"root_000374","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvan donu, dudak veya bitki görünümünde doğrudan siyahı ya da siyahla karışmış koyu tonu genel olarak anlatır.","boundary_detail":"Dal doğrudan siyahı ve siyaha yaklaşan veya siyahla karışan koyu renkleri; bunların hayvan, dudak ya da bitki görünümündeki gerçekleşmelerini kapsar.","branch_image_ar":"الحوة والأحوى: سواد أو حمرة تميل إلى السواد","concept_gloss":"siyah veya siyaha çalan koyu kızıl, esmer ya da yeşil renk","contextual_glosses":[{"applicability":"Özellikle at donunun koyu siyah ile koyu kızıl arasında bulunduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğrudan siyahı, dudaktaki esmerliği ve siyah karışmış koyu yeşil görünümü kapsamaz.","preserves":"At donundaki kızıl-siyah aralığını ve siyaha yaklaşma niteliğini korur."},"facet_ids":["F001","F002"],"text":"siyaha çalan koyu kızıl","usage_role":"contextual"},{"applicability":"Yeşil görünümün siyah ve yer yer sarı karışımıyla koyulaştığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğrudan siyahı, kızıl-siyah at donunu ve dudaktaki koyu esmerlik kullanımını dışarıda bırakır.","preserves":"Yeşilin siyahla karışarak koyulaşması yönünü açıkça korur."},"facet_ids":["F001","F003"],"text":"siyah karışmış koyu yeşil","usage_role":"contextual"}],"definition":"Doğrudan siyah ya da siyaha yaklaşan veya siyahla karışan koyu kızıl, koyu esmer veya koyu yeşil renk niteliğidir; at ve devede don, dudakta koyuluk ve bitkide kararmış yeşillik olarak görülebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Renk doğrudan siyah olabilir ya da siyaha yaklaşan veya siyahla karışan koyu bir ton olabilir."},{"facet_id":"F002","role":"specialization","statement":"Atlarda koyu siyah ile koyu kızıl arasında bir don veya sırtı kızıl koyu görünüm olabilir."},{"facet_id":"F003","role":"extension","statement":"Dudaktaki koyu esmerlik ile siyah ve sarının karıştığı koyu yeşil görünüm de kapsama girer."}],"identity_rationale":"Kaynak ifadesi doğrudan siyahı, atlarda koyu siyah ile koyu kızıl arasındaki donu, siyaha çalan kızıllığı, dudaktaki koyu esmerliği ve siyahla karışmış yeşil-sarı görünümü aynı renk alanında toplar. Geçici renk çerçevesi bu çeşitliliği doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"siyaha çalan koyu kızıl veya koyu esmer renk"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"siyah ya da siyah karışmış koyu yeşil renkli"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"siyah veya siyaha çalan koyu renkli dişi"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"atın siyah veya siyaha çalan koyu renge dönüşmesi"}],"lexicalization_note":"Tanım yalın renk niteliğini kapsar; aynı biçimdeki bitki adı yalnızca bitkinin rengi açıkça anlatıldığında bu dala yaklaşır.","neighbor_coverage_note":"Bütün renk adayları incelendi; siyah-kızıl karışımı, esmer üstü koyuluk ve genel siyahlıkla en yakın üç karşılaştırma yayımlandı, beyazlık ve beneklilik adayları uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kızılla karışmış siyahı farklı yüzey ve durumlara yayar; odak dal hayvan donu, dudak ve koyu yeşil görünüm çevresinde daha belirli bir karışık renk kümesi kurar.","focus_only":"Siyah karışmış koyu yeşil ve hayvan donuna özgü kullanımlar odak dalda bulunur.","gloss":"kızıla çalan siyah","neighbor_only":"Yüz, boyun, tüy, ev izi ve öfke belirtisi gibi daha geniş yüzey ve durum kullanımları komşuya özgüdür.","neighbor_ref":"root_000713/B002","relation_type":"near_synonym","shared_zone":"İki dal da siyah ile kızılın karıştığı koyu bir renk alanını paylaşır."},{"boundary_match":"partial","distinction":"Komşu dal esmer zemin üzerindeki siyaha çalan renkle sınırlıdır; odak dal kızıl, esmer ve yeşil zeminlerdeki koyulaşmayı kapsar.","focus_only":"At donu, dudak koyuluğu ve siyah karışmış yeşil odak dalın geniş gerçekleşmeleridir.","gloss":"esmer üzerinde siyaha çalan ton","neighbor_only":"Koyuluğun özellikle esmer tenin üzerinde belirmesi komşunun daha dar koşuludur.","neighbor_ref":"root_000708/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da temel rengin üzerinde siyaha yaklaşan koyu bir ton oluşmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal siyahı ve siyaha çalan karışık tonları hayvan donu, dudak ve koyu yeşil görünüm çevresinde toplar; komşu dal genel karanlık ve kararma kullanımlarına da uzanır.","focus_only":"Kızıl ile siyah arasındaki karışık ton ve dudak esmerliği odak dalda belirgindir.","gloss":"koyu siyah ve kararma","neighbor_only":"Gecenin karanlığı ve genel kararma komşu dalın daha geniş kapsamıdır.","neighbor_ref":"root_000496/B001","relation_type":"near_synonym","shared_zone":"İki dal da doğrudan siyah ve siyaha yaklaşan yoğun koyu renk alanında örtüşür."}],"source_phrase_ar":"الحوة شية من شيات الخيل وهي بين الدهمة والكمتة وكل أسود أحوى وامرأة حواء (jamhara)؛ الحوة لون يخالط الكمتة وحمرة تضرب إلى السواد والحوة سمرة الشفة وبعير أحوى إذا خالط خضرته سواد وصفرة (sihah)؛ الأحوى من الخيل هو الأحمر السراة والحوة في الشفاه شبيه باللمى والأحوى الأسود من الخضرة (tahdhib)","source_summary":"Kaynakların ortak noktası siyah veya siyaha yaklaşan karışık koyu renktir; ayrıntılar at donunda kızıl-siyah aralığından dudak koyuluğuna ve siyah karışmış yeşile kadar değişir.","sources":["JA","SI","TA"],"what_is_ar":"يدخل فيه الحوة شية الخيل بين الدهمة والكمتة أو حمرة تضرب إلى السواد، وسمرة الشفة، والأحوى الأسود من الخضرة أو لون الفرس والبعير، وحواء مؤنث أحوى.","what_is_not_ar":"لا يدخل فيه الحواء النبات إلا إذا سمي للون، ولا الحواء البيوت، ولا حوى بمعنى جمع."},"support_links":["sup_1b557f13d09d6802a6ae","sup_3f4b01b22ddbd600757d"]},{"boundary":"Dal genel olarak bütün otları değil, yaprak veya renk özellikleriyle tanıtılan belirli bitkiyi ve onun adlandırılmış türlerini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000374/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْوَىٰ","morph_features":"STEM|POS:ADJ|LEM:>aHowaY`|ROOT:Hwy|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:5:3:1","qac_word_ref":"87:5:3","surface_ar":"أَحْوَىٰ"}],"gloss":"ok uçlu yapraklı veya kurt renkli belirli bir ot","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim genel ot sınıfına değil, adı yerleşmiş belirli bir ot veya otsu bitkiye yöneliktir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir betimlemede yaprakları ok uçlarına benzer biçimde tanıtılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir betimlemede bitkinin rengi kurdun rengine benzetilir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Genişletilmiş adlar, hayvanla ilişkilendirilen bir türü ve tuzcul çalılar arasında yetişen kaba bir türü ayırır."}}],"root_ar":"ح و ي","root_id":"root_000374","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitkinin genel adı ile kaynaklardaki iki ayırt edici görünüş betimini birlikte vermek gerektiğinde uygundur.","boundary_detail":"Dal genel olarak bütün otları değil, yaprak veya renk özellikleriyle tanıtılan belirli bitkiyi ve onun adlandırılmış türlerini kapsar.","branch_image_ar":"الحواء: نبت معروف","concept_gloss":"ok uçlu yapraklı veya kurt renkli belirli bir ot","contextual_glosses":[{"applicability":"Bitkinin yaprak biçimi üzerinden tanıtıldığı botanik betimlemelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kurt rengini andıran görünümü ve adlandırılmış alt türleri belirtmez.","preserves":"Belirli ot gönderimini ve ok ucuna benzeyen yaprak özelliğini korur."},"facet_ids":["F001","F002"],"text":"ok ucu biçimli yaprakları olan ot","usage_role":"explanatory"},{"applicability":"Bitkinin genişletilmiş adla belirtilen kaba alt türü anlatılırken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bitkinin yalın genel adını, yaprak biçimini ve öteki adlandırılmış türünü kapsamaz.","preserves":"Kaba yapılı alt türü ve yetiştiği tuzcul çalı çevresini korur."},"facet_ids":["F004"],"text":"tuzcul çalılıkta yetişen kaba tür","usage_role":"contextual"}],"definition":"Ok ucu biçimli yaprakları veya kurdu andıran rengiyle betimlenen belirli bir ot türüdür; yalın ad bitkiyi, genişletilmiş adlandırmalar ise onun belirli kaba ya da hayvanla ilişkilendirilen türlerini gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim genel ot sınıfına değil, adı yerleşmiş belirli bir ot veya otsu bitkiye yöneliktir."},{"facet_id":"F002","role":"source_variant","statement":"Bir betimlemede yaprakları ok uçlarına benzer biçimde tanıtılır."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir betimlemede bitkinin rengi kurdun rengine benzetilir."},{"facet_id":"F004","role":"specialization","statement":"Genişletilmiş adlar, hayvanla ilişkilendirilen bir türü ve tuzcul çalılar arasında yetişen kaba bir türü ayırır."}],"identity_rationale":"Kaynak ifadesi belirli bir ot türünü, tekil bitkiyi ve adlandırılmış iki alt türü açıkça destekler; yaprakların ok ucu biçimine benzemesi ile rengin kurdu andırması kaynaklar arasındaki betimleyici çeşitliliktir. Geçici bitki çerçevesi bu ayrıntıları korur.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"belirli bir ot veya otsu bitki"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bu bitkinin tek bir örneği"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"aynı bitkinin sığırla ilişkilendirilen türü"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"tuzcul çalılar arasında yetişen kaba türü"}],"lexicalization_note":"Yalın biçimler bitkinin kendisini ve tek örneğini gösterir; ad tamlaması biçimindeki iki birim yalnızca belirli bitki türlerini adlandırır ve genel anlama yayılmaz.","neighbor_coverage_note":"Bitki adaylarının ve aynı kökün öteki dallarının tümü değerlendirildi; genel üst sınıf ile iki ayrı bitki karşılaştırması yayımlandı, yalnızca biçimsel çağrışım taşıyan adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel bir bitki sınıfıdır; odak dal ise görünüş özellikleri ve özel tür adları bulunan belirli bir bitkidir.","focus_only":"Ok ucu biçimli yaprak veya kurdu andıran renk ve adlandırılmış türler odak dala özgüdür.","gloss":"yeşil otsu bitki","neighbor_only":"Ağaç olmayan bütün taze yeşil otları kapsayan genel sınıf komşuya özgüdür.","neighbor_ref":"root_000141/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da ağaç olmayan yeşil ve otsu bitkileri gösterebilir."},{"boundary_match":"field_only","distinction":"Gönderimleri farklı bitki türleridir; ortak botanik alan, bağlam içinde birbirlerinin yerine kullanılmalarına izin vermez.","focus_only":"Odak bitki ok ucu yaprak veya kurt rengiyle tanıtılır.","gloss":"başka bir otsu bitki","neighbor_only":"Komşu dal semizotu, kereviz ve başka yerleşik bitki gönderimlerini kapsar.","neighbor_ref":"root_000546/B007","relation_type":"same_field","shared_zone":"İki dal da belirli otların ve yenebilir yeşil bitkilerin adlandırıldığı alandadır."},{"boundary_match":"field_only","distinction":"Odak dal ile komşu dal iki ayrı bitkiyi adlandırır; yalnızca aynı bitki alanında ve hayvanla ilişkilendirilme bakımından buluşurlar.","focus_only":"Odak dalın bitkisi yaprak biçimi ve kurt benzeri rengiyle ayırt edilir.","gloss":"develerin yediği başaklı ot","neighbor_only":"Komşu bitki büyük bir başak veya uzun sap taşır ve develerin yemi olarak tanıtılır.","neighbor_ref":"root_000879/B009","relation_type":"same_field","shared_zone":"Her iki dal da ot türlerini ve hayvanlarla ilişkili bitki adlarını içerir."}],"source_phrase_ar":"الحواء ضرب من البقل يشبه ورقه بنصال السهام (jamhara)؛ الحواء نبت يشبه لون الذئب الواحدة حواءة (sihah)؛ الحواء نبت معروف الواحدة حوءة وحواء الذعاليق وحواء البقر وحواء الكلاب (tahdhib)","source_summary":"Ortak çekirdek belirli bir ot türüdür; toplu kanıtta yaprak biçimi ok uçlarına, renk ise kurda benzetilir ve iki genişletilmiş ad belirli alt türleri ayırır.","sources":["JA","SI","TA"],"what_is_ar":"يدخل فيه الحواء أو الحواءة نباتا أو بقلا معروفا، ومنه حواء الذعاليق أو البقر وحواء الكلاب، والنبت الذي يشبه ورقه نصال السهام أو يشبه لون الذئب.","what_is_not_ar":"لا يدخل فيه حواء مؤنث أحوى، ولا الحواء بمعنى البيوت، ولا الحوة اللون إلا من جهة الوصف اللوني في بعض المصادر."},"support_links":[]},{"boundary":"Dal suyun tutulduğu küçük yapı veya yerleri kapsar; bağırsak ve binek adları yalnızca biçim benzerliği nedeniyle bu dala alınmaz.","branch_kind":"bare","branch_ref":"root_000374/B008","candidate_links":[{"candidate_id":"cand_8b3cceff415da6700cec","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْوَىٰ","morph_features":"STEM|POS:ADJ|LEM:>aHowaY`|ROOT:Hwy|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:5:3:1","qac_word_ref":"87:5:3","surface_ar":"أَحْوَىٰ"}],"gloss":"suyu tutan küçük yalak, kıvrımlı çukur veya çevrili yüzey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"specialization","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin devesini sulamak için hazırladığı küçük yalak bu dalın tekil türüdür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Düzlük ve çayırlarda sel suyunu toplayan kıvrımlı çukurlar doğal yer türünü oluşturur."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Toprak ve taş yığılarak çevrilen düz yüzeyler suyu tutmak için yapılmış türdür."}}],"root_ar":"ح و ي","root_id":"root_000374","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Küçük yalak, doğal sel çukuru ve yapılmış toplama yüzeyinin ortak su tutma işlevini birlikte kapsar.","boundary_detail":"Dal suyun tutulduğu küçük yapı veya yerleri kapsar; bağırsak ve binek adları yalnızca biçim benzerliği nedeniyle bu dala alınmaz.","branch_image_ar":"الحوية والحوايا: حفائر ومساطح تحبس الماء","concept_gloss":"suyu tutan küçük yalak, kıvrımlı çukur veya çevrili yüzey","contextual_glosses":[{"applicability":"Bir kişinin devesi için hazırladığı küçük su kabı veya yalak anlatılırken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sel suyuyla dolan doğal çukurları ve toprak-taş çevrili yüzeyleri kapsamaz.","preserves":"Hayvan sulamak için yapılan küçük yalak kullanımını korur."},"facet_ids":["F001"],"text":"küçük hayvan sulama yalağı","usage_role":"contextual"},{"applicability":"Düzlük veya çayırlarda sel suyuyla dolan doğal oyuklar anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Küçük sulama yalağını ve yapay toprak-taş çevrili yüzeyi dışarıda bırakır.","preserves":"Kıvrımlı çukur biçimini ve sel suyunu toplama işlevini korur."},"facet_ids":["F002"],"text":"sel suyunu tutan kıvrımlı çukur","usage_role":"explanatory"}],"definition":"Suyu kaçmadan bir arada tutan küçük bir yalak, sel suyuyla dolan kıvrımlı bir çukur ya da toprak ve taşla çevrilmiş düz bir toplama yüzeyidir.","distinctive_facets":[{"facet_id":"F001","role":"specialization","statement":"Bir kişinin devesini sulamak için hazırladığı küçük yalak bu dalın tekil türüdür."},{"facet_id":"F002","role":"core","statement":"Düzlük ve çayırlarda sel suyunu toplayan kıvrımlı çukurlar doğal yer türünü oluşturur."},{"facet_id":"F003","role":"specialization","statement":"Toprak ve taş yığılarak çevrilen düz yüzeyler suyu tutmak için yapılmış türdür."}],"identity_rationale":"Kaynak ifadesi suyu tutma işlevinde birleşen üç somut gerçekleşmeyi açıkça verir: deve sulamak için küçük yalak, düzlüklerde sel suyuyla dolan kıvrımlı çukurlar ve toprakla taşın çevrilmesiyle yapılan su tutucu yüzeyler. Geçici çerçeve bu ortak işlevi doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"deve sulamak için yapılmış küçük yalak"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"sel suyunu tutan kıvrımlı çukurlar veya çevrili yüzeyler"}],"lexicalization_note":"Tanım yalın su tutma dalını ve kaynakta verilen üç fiziksel türü kapsar; başka dalların benzer biçimli adları eklenmez.","neighbor_coverage_note":"Bütün su ve arazi adayları değerlendirildi; genel havuz, tarımsal depo ve suyun toplandığı yer en yararlı üç sınırı verdi, topoğrafyası farklı adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel su birikintisi ve havuz alanına yakındır; odak dal küçük hayvan yalağı, kıvrımlı sel çukuru ve çevrili yüzey türlerini özellikle birleştirir.","focus_only":"Deve için küçük yalak ve toprak-taşla çevrilen düz yüzey odak dalın belirli türleridir.","gloss":"suyu tutan havuz veya çukur","neighbor_only":"Suyu günlerce tutma ve küçük gölete benzeme komşu dalın belirgin kapsamıdır.","neighbor_ref":"root_000018/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da suyu bir yerde toplayıp bir süre tutan havuz veya çukur türlerini kapsar."},{"boundary_match":"partial","distinction":"Komşu dal geniş ve tarımsal amaçlı bir su deposudur; odak dal daha küçük veya doğal su tutma biçimlerini de kapsar.","focus_only":"Küçük deve yalağı ve doğal kıvrımlı sel çukurları odak dalda bulunur.","gloss":"tarımsal su toplama havuzu","neighbor_only":"Geniş depoya suyun kuyu, kanal veya yağmurdan getirilip tarıma salınması komşuya özgüdür.","neighbor_ref":"root_000016/B007","relation_type":"near_synonym","shared_zone":"İki dal da suyu sınırlı bir yapıda toplama ve gerektiğinde kullanma işlevini paylaşır."},{"boundary_match":"partial","distinction":"Komşu dal biçimi belirsiz genel bir toplanma yeridir; odak dal suyu tutan üç somut yapı ve yer türüyle sınırlıdır.","focus_only":"Yalak, kıvrımlı çukur ve çevrili yüzey biçimleri odak dalda açıkça belirlenir.","gloss":"suyun toplandığı yer","neighbor_only":"Suyun toplandığı herhangi bir yer olma genelliği komşu dala özgüdür.","neighbor_ref":"root_000593/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da suyun akıştan sonra bir yerde toplanıp durmasını anlatır."}],"source_phrase_ar":"الحوي الحويض الصغير يسويه الرجل لبعيره يسقيه فيه (tahdhib)؛ الحوايا التي تكون في القيعان والرياض حفائر ملتوية يملؤها ماء السيل (tahdhib)؛ الحوايا المساطح وهو أن يعمدوا إلى الصفا فيحوون له ترابا وحجارة ليحبس عليهم الماء (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak küçük deve yalağını, sel suyuyla dolan kıvrımlı çukurları ve toprak-taş çevrili toplama yüzeylerini birlikte kaydeder."}],"source_summary":"Dalın bütün kullanımları, suyu küçük ve sınırlanmış bir yerde toplama ve akıp gitmesini önleme işlevinde birleşir.","sources":["TA"],"what_is_ar":"يدخل فيه الحوي الحويض الصغير للبعير، والحوايا حفائر ملتوية في القيعان والرياض تمسك ماء السيل، والمساطح التي يحوى لها التراب والحجارة لحبس الماء.","what_is_not_ar":"لا يدخل فيه الحوايا الأمعاء إلا من جهة التشبيه المصرح به، ولا الحوية مركب المرأة أو كساء البعير."},"support_links":["sup_ea7f41da09281fecc31c"]},{"boundary":"Dal hastalık durumundaki kişiyi niteler; akılsızlık, genel zayıflık veya belirli bir hastalık türü anlamın parçası değildir.","branch_kind":"bare","branch_ref":"root_000374/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْوَىٰ","morph_features":"STEM|POS:ADJ|LEM:>aHowaY`|ROOT:Hwy|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:5:3:1","qac_word_ref":"87:5:3","surface_ar":"أَحْوَىٰ"}],"gloss":"hasta veya rahatsız kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim, bedensel olarak hasta veya rahatsız durumda bulunan kişidir."}}],"root_ar":"ح و ي","root_id":"root_000374","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hastalığın türü belirtilmeden bir kişinin bedensel rahatsızlık durumunun anlatıldığı kullanımlarda uygundur.","boundary_detail":"Dal hastalık durumundaki kişiyi niteler; akılsızlık, genel zayıflık veya belirli bir hastalık türü anlamın parçası değildir.","branch_image_ar":"الحوي: العليل","concept_gloss":"hasta veya rahatsız kimse","contextual_glosses":[{"applicability":"Kişinin hastalığının türü veya ağırlığı belirtilmeden yapılan genel nitelemede doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiyi genel olarak hasta sayan çekirdek anlamı bütünüyle korur."},"facet_ids":["F001"],"text":"hasta kimse","usage_role":"general"}],"definition":"Bedensel bir rahatsızlığı veya hastalığı bulunan kişi için kullanılan yalın bir nitelemedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim, bedensel olarak hasta veya rahatsız durumda bulunan kişidir."}],"identity_rationale":"Tek kaynak ifadesi sözcüğü doğrudan hasta veya rahatsız kimse anlamında açıklar ve aynı cümledeki başka bir sözcüğün akılsız anlamını ayrı tutar. Geçici çerçeve bu yalın kişi niteliğini doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"hasta veya rahatsız kimse"}],"lexicalization_note":"Tanım tek başına kullanılan hasta kişi niteliğiyle sınırlıdır; belirli hastalık, ateş veya güçsüzlük türleri eklenmez.","neighbor_coverage_note":"Bütün hastalık ve kök içi adaylar değerlendirildi; genel bedensel hastalık, geniş sağlık kaybı ve hastalığa bağlı güçsüzlük sınırları yayımlandı, özel ateş ve organ kusuru adayları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kişi nitelemesinde yakın karşılık vardır; komşu dal ayrıca hastalık durumunu ve hastalandırma eylemini kapsadığı için sınırı daha geniştir.","focus_only":"Odak dal yalnızca hasta kişiyi adlandıran yalın ve tek kaynaklı bir nitelemedir.","gloss":"bedensel olarak hasta","neighbor_only":"Hastalık durumunun adı, sürekli hasta olma ve bir hastalığın kişiyi hasta etmesi komşuda bulunur.","neighbor_ref":"root_000721/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bedensel hastalık içindeki kişiyi niteleyebilir."},{"boundary_match":"partial","distinction":"Odak dal yalnızca hasta kişiyi gösterir; komşu dal hastalık durumunu, davranışı ve beden dışındaki eksilmeleri de kapsar.","focus_only":"Odak dalın kanıtı doğrudan hasta kişiye yönelik tek bir nitelemedir.","gloss":"sağlıktan çıkmış olma","neighbor_only":"Hastalık, sakatlık, eksilme, hasta görünme ve maldaki bozulma komşunun geniş kapsamındadır.","neighbor_ref":"root_001415/B001","relation_type":"near_synonym","shared_zone":"İki dal da kişinin sağlıklı durumdan çıkıp hasta olması alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal hasta kişiyi niteler; komşu dal hastalık ya da açlığın yol açtığı güç azalmasını anlatır ve hastalık olmadan da gerçekleşebilir.","focus_only":"Hastalığın kendisi odak dalda yeterlidir; ayrıca güç kaybı şart değildir.","gloss":"hastalık veya açlıktan güçsüz düşme","neighbor_only":"Açlık veya hastalık yüzünden gücün azalması komşu dalın zorunlu sonucudur.","neighbor_ref":"root_000425/B003","relation_type":"near_neighbor","shared_zone":"Hastalık bir kişide güçsüzlük doğurduğunda iki dal aynı durumda buluşabilir."}],"source_phrase_ar":"الحوي العليل والدوي الأحمق مشددات كلها (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak bu biçimi hasta kişi anlamında verir ve yanındaki akılsızlık bildiren ayrı sözcükten açıkça ayırır."}],"source_summary":"Kanıtın çekirdeği herhangi bir hastalık türünü belirtmeden kişiyi hasta veya rahatsız olarak nitelemektir.","sources":["TA"],"what_is_ar":"يدخل فيه قول ابن الأعرابي الحوي العليل، على أنه لفظ مفرد مشدد ذكره تهذيب اللغة.","what_is_not_ar":"لا يدخل فيه الدوي الأحمق، ولا حوى بمعنى جمع، ولا الحوة اللون."},"support_links":[]},{"boundary":"Dal, bulantıyı, bitkinin kurutulmasını ve insanlar için kullanılan küçültücü benzetmeyi değil, sıvıda taşınan ya da yüzeye çıkan maddi döküntüyü anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001073/B001","candidate_links":[{"candidate_id":"cand_8b3cceff415da6700cec","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"غُثَآء","morph_features":"STEM|POS:N|LEM:guvaA^'|ROOT:gvw|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:5:2:1","qac_word_ref":"87:5:2","surface_ar":"غُثَآءً"}],"gloss":"akışla taşınan veya sıvı yüzeyine çıkan döküntü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Selin taşıdığı veya su yüzünde yüzen kuru bitki, kumaş parçası ve benzeri değersiz maddelerden oluşan döküntüdür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tencerenin ya da başka bir sıvının yüzüne çıkan köpük ve kuru bitki parçaları da bu adlandırmanın kapsamına girer."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Suyun hayvan pisliği, yaprak, kamış ve benzeri döküntülerle dolması, aynı maddi görüntüyü kuran yapıya bağlı bir kullanımdır."}}],"root_ar":"غ ث و","root_id":"root_001073","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maddi çekirdeğin tamamını, hem selin taşıdığı karışık parçaları hem de sıvı yüzeyine çıkan düşük değerli artıkları birlikte belirtmek için uygundur.","boundary_detail":"Dal, bulantıyı, bitkinin kurutulmasını ve insanlar için kullanılan küçültücü benzetmeyi değil, sıvıda taşınan ya da yüzeye çıkan maddi döküntüyü anlatır.","branch_image_ar":"غثاء يطفو ويحمله السيل","concept_gloss":"akışla taşınan veya sıvı yüzeyine çıkan döküntü","contextual_glosses":[{"applicability":"Selin kuru bitki, kumaş parçası ve benzeri maddeleri sürükleyip su yüzünde topladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Selin taşıyıcılığını, su yüzündeki konumu ve döküntünün karışık maddi yapısını korur."},"facet_ids":["F001"],"text":"selin taşıdığı yüzey döküntüsü","usage_role":"contextual"},{"applicability":"Köpük ve kuru bitki parçalarının suyun ya da tenceredeki sıvının yüzüne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüzeye çıkma hareketini ve sıvıda beliren düşük değerli madde niteliğini korur."},"facet_ids":["F002"],"text":"sıvının yüzüne çıkan artık","usage_role":"contextual"},{"applicability":"Suyun yaprak, kamış, hayvan pisliği ve benzeri parçalar bakımından çoğalıp kirlenmesini anlatan yapıya bağlı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Döküntünün suda çoğalmasını ve suyu dolduran karışık madde niteliğini korur."},"facet_ids":["F003"],"text":"döküntüyle dolmak","usage_role":"explanatory"}],"definition":"Selin taşıdığı ya da bir sıvının yüzüne çıkıp dağılan, kuru bitki, köpük, kumaş parçası ve benzeri düşük değerli maddelerden oluşan döküntüdür. Buna, suyun yaprak, kamış ve hayvan pisliği gibi maddelerle dolması da bağlı bir kullanım olarak katılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Selin taşıdığı veya su yüzünde yüzen kuru bitki, kumaş parçası ve benzeri değersiz maddelerden oluşan döküntüdür."},{"facet_id":"F002","role":"extension","statement":"Tencerenin ya da başka bir sıvının yüzüne çıkan köpük ve kuru bitki parçaları da bu adlandırmanın kapsamına girer."},{"facet_id":"F003","role":"associated_use","statement":"Suyun hayvan pisliği, yaprak, kamış ve benzeri döküntülerle dolması, aynı maddi görüntüyü kuran yapıya bağlı bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi, selin taşıdığı veya suyun ve tencerenin yüzüne çıkardığı kuru bitki, köpük, kumaş parçası ve benzeri değersiz döküntüleri aynı maddi çekirdekte toplar. Verilen dal çerçevesi bu çekirdeği ve suyun yaprak, kamış ya da hayvan pisliğiyle dolması gibi bağlı kullanımları doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"selin taşıdığı ya da suyun ve tencerenin yüzüne çıkan kuru bitki, köpük ve döküntü"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"vadi yüzeyde toplanan değersiz döküntüler getirdi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yüzeyde toplanan döküntü getirdi veya bunlarla doldu"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"selin taşıdığı kumaş parçası ve benzeri yüzey döküntüsü"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"selin taşıdığı yüzey döküntüleri"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"suda hayvan pisliği, yaprak, kamış ve benzeri döküntüler çoğaldı"}],"lexicalization_note":"Tanım, bağımsız olarak adlandırılan yüzey döküntüsünü temel alır; vadi ve suyla kurulan ifadeler ise bu maddenin gelmesini veya suda çoğalmasını anlatan yapıya bağlı kullanımlar olarak ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma sırasıyla en yakın maddi komşuyu, köpükle olan kapsam ilişkisini ve aynı sahnedeki eylem-nesne ayrımını gösterir. Kalan adaylar bu sınırları yinelediği veya yalnızca daha uzak bir ortak alan sunduğu için eklenmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal maddenin taşınan ya da yüzen döküntü oluşunu adlandırır; komşu dal ise bu maddenin akış veya kaynama tarafından yana atılmış, ayrılmış artık oluşunu belirginleştirir.","focus_only":"Odak dal, yüzeyde kalan veya akışla taşınan döküntüyü, kenara atılmış olmasını gerektirmeden kapsar.","gloss":"yüzey döküntüsü ile yana atılan artık","neighbor_only":"Komşu dal, selin ya da tencerenin köpük ve döküntüyü yana atması veya dışarı ayırması sonucunu öne çıkarır.","neighbor_ref":"root_000251/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da selde veya tencere yüzeyinde beliren köpük ve düşük değerli parçaları kapsayabilir."},{"boundary_match":"partial","distinction":"Odak dal köpüğü daha geniş ve karışık bir döküntü sınıfının bir parçası olarak kapsar; komşu dalın çekirdeği ise doğrudan köpük maddesidir.","focus_only":"Odak dal kuru bitki, kumaş parçası, yaprak ve kamış gibi köpük olmayan maddeleri de içerir.","gloss":"karışık yüzey döküntüsü ile köpük","neighbor_only":"Komşu dal, su, süt, içecek ve ağız yüzeyinde oluşabilen beyaz köpüğün kendisini adlandırır.","neighbor_ref":"root_000620/B001","relation_type":"near_neighbor","shared_zone":"Köpük, sıvı yüzeyinde belirdiğinde odak dalın karışık yüzey maddeleri arasında yer alabilir."},{"boundary_match":"field_only","distinction":"Biri taşınan ya da biriken maddenin adıdır; diğeri bu maddeyi bir araya getirip götüren sel eylemidir, bu nedenle birbirlerinin yerine kullanılamazlar.","focus_only":"Odak dal, selin taşıdığı veya yüzeyde biriken döküntü maddesinin kendisini gösterir.","gloss":"taşınan döküntü ile selin taşıması","neighbor_only":"Komşu dal, selin döküntüyü toplaması ve taşıması olayını gösterir.","neighbor_ref":"root_000529/B003","relation_type":"same_field","shared_zone":"İki dal aynı sel ve döküntü sahnesini, aynı madde ile taşıyıcı akış ilişkisini paylaşır."}],"source_phrase_ar":"الغثاء غثاء السيل (maqayis)؛ الغثاء ما جاء به السيل من نبات قد يبس (ayn)؛ ما يحمله السيل من القماش (sihah)؛ غثا الماء إذا كثر فيه البعر والورق والقصب (tahdhib)؛ الغثاء غثاء السيل والقدر، ما يطفح ويتفرق من النبات اليابس وزبد القدر (mufradat)","source_summary":"Kaynakların ortak çekirdeği, selin getirdiği veya sıvı yüzeyine çıkan kuru bitki ve çeşitli değersiz parçaların oluşturduğu döküntüdür. Toplu anlatım, sel suyunu, su yüzeyini ve tencere yüzeyini kapsar; suyun yaprak, kamış ve hayvan pisliğiyle dolmasını da aynı görüntüye bağlı olarak verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الغثاء الذي يحمله السيل أو يطفح على الماء والقدر من نبات يابس وزبد وقماش وبعر وورق وقصب، وما يجتمع بعضه فوق بعض من دنيء المادة.","what_is_not_ar":"لا يدخل خبث النفس والغثيان، ولا الاستعمال المجازي لسفلة الناس إلا من جهة التشبيه."},"support_links":["sup_ea7f41da09281fecc31c"]},{"boundary":"Dal, kuru bitki maddesinin genel adı değil, otlağın selce yığılması ve niteliğini yitirmesi ya da bitkinin yeşillikten kuru ufalanmış hale getirilmesi sürecidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001073/B002","candidate_links":[{"candidate_id":"cand_69fcf9534f45539b2909","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"غُثَآء","morph_features":"STEM|POS:N|LEM:guvaA^'|ROOT:gvw|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:5:2:1","qac_word_ref":"87:5:2","surface_ar":"غُثَآءً"}],"gloss":"bitkiyi kuru ve ufalanmış hale getirmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Otlak sel tarafından yığılıp tadını yitirir ya da bitki yeşillikten sonra kuru ve ufalanmış hale getirilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sel, otlağı parça parça bir araya yığar ve onun tadını ya da otlak değerini giderir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dönüşümün sonucu, yeşillikten sonra kurumuş ve ufalanmış bitki olarak da açıklanır."}}],"root_ar":"غ ث و","root_id":"root_001073","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitkinin yeşil ve yararlı durumdan çıkarılıp kuru, parçalanmış ve niteliğini yitirmiş hale dönüştürülmesini anlatan ortak sonuç için uygundur.","boundary_detail":"Dal, kuru bitki maddesinin genel adı değil, otlağın selce yığılması ve niteliğini yitirmesi ya da bitkinin yeşillikten kuru ufalanmış hale getirilmesi sürecidir.","branch_image_ar":"مرعى صار هشيما غثاء","concept_gloss":"bitkiyi kuru ve ufalanmış hale getirmek","contextual_glosses":[{"applicability":"Selin otlak parçalarını bir araya topladığı ve otlağın yenilebilir niteliğini ortadan kaldırdığı yapıya bağlı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Selin yapan taraf oluşunu, yığma işlemini ve otlağın tadını yitirmesi sonucunu birlikte korur."},"facet_ids":["F002"],"text":"selin otlağı yığıp tadını gidermesi","usage_role":"contextual"},{"applicability":"Bitkinin önceki yeşil halinden kurutulup ufalanmış ot haline getirildiğinin özellikle belirtildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yeşillikten kuruluğa geçişi, ettirgen dönüşümü ve ortaya çıkan kuru bitki sonucunu korur."},"facet_ids":["F001","F003"],"text":"yeşil bitkiyi kuru ota çevirmek","usage_role":"explanatory"}],"definition":"Selin otlağı bir araya yığıp tadını gidermesi veya bitkinin yeşil halinden kuru, ufalanmış ota dönüştürülmesidir. İlk kullanım selin otlak üzerindeki işlemini, ikincisi ise kurutma sonucunu öne çıkarır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Otlak sel tarafından yığılıp tadını yitirir ya da bitki yeşillikten sonra kuru ve ufalanmış hale getirilir."},{"facet_id":"F002","role":"specialization","statement":"Sel, otlağı parça parça bir araya yığar ve onun tadını ya da otlak değerini giderir."},{"facet_id":"F003","role":"source_variant","statement":"Dönüşümün sonucu, yeşillikten sonra kurumuş ve ufalanmış bitki olarak da açıklanır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Selin otlağı yığması, tadını gidermesi ve bir etkenin bitkiyi bu sonuca dönüştürmesi kaybolur.","preserves":"Bitkinin canlı ve yeşil durumunu yitirerek kuru hale gelmesini korur."},"text":"kurumak"}],"identity_rationale":"Kaynak ifadesi iki bağlı gerçekleşmeyi açıkça bir araya getirir: selin otlağı yığıp tadını gidermesi ve yeşil bitkinin kurutularak kuru, ufalanmış ota çevrilmesi. Verilen dal çerçevesi bu işlem, önceki durum ve ortaya çıkan sonuç ayrımlarını korur.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"sel otlağı bir araya yığıp tadını giderdi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"otlağı bir araya yığıp tadını giderdi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"onu yeşillikten sonra kuru ve ufalanmış ota çevirdi"}],"lexicalization_note":"Tanım, sel ile otlak arasındaki yapıya bağlı yığma ve tadı giderme kullanımını, bitkiyi kuru ufalanmış hale getiren ettirgen kullanımdan ayırır; bunlardan bağımsız genel bir kuruma anlamı çıkarmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; en yararlı ayrımlar genel sararıp kuruma ile geniş cansızlık alanına karşı kurutma, yığma ve niteliği giderme sınırlarını gösteren iki komşuda bulundu. Diğerleri yalnız kuru bitki alanını yineledi veya daha uzak örnekler sundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sınırı, yığma ve tadı giderme işlemiyle ya da kuru ufalanmış sonuçla belirlenir; komşu dalın çekirdeği ise daha genel sararma ve kuruma durumudur.","focus_only":"Odak dal, selin otlağı yığması ve tadını gidermesi ile bitkinin kuru ufalanmış hale getirilmesini içerir.","gloss":"kurutup ufalamak ile sararıp kurumak","neighbor_only":"Komşu dal, bitki ve toprağın sararıp kurumasını veya bu duruma sokulmasını, sel ve yığılma gerektirmeden kapsar.","neighbor_ref":"root_001612/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda bitki canlılığını ve yeşilliğini yitirerek kuru bir duruma geçebilir."},{"boundary_match":"partial","distinction":"Odak dal süreç ve sonucu birlikte sınırlar; komşu dal ise farklı varlıklarda görülen ölü ya da kurumuş durumu adlandırır ve yığma veya dönüştürme işlemini gerektirmez.","focus_only":"Odak dal bir dönüşüm işlemini, özellikle otlağın yığılması veya bitkinin kurutulup ufalanmasını anlatır.","gloss":"kurutma dönüşümü ile kurumuş cansız şey","neighbor_only":"Komşu dal bitkisiz toprağı, kuru bitkiyi, bozulmuş meyveyi ve ölü hayvanı kapsayan daha geniş bir cansızlık alanıdır.","neighbor_ref":"root_001598/B002","relation_type":"near_neighbor","shared_zone":"Kuru bitki, odak dalın işleminin sonucu ve komşu dalın adlandırdığı durumlardan biri olabilir."}],"source_phrase_ar":"غثا السيل المرتع إذا جمع بعضه إلى بعض وأذهب حلاوته (sihah;tahdhib)؛ جففه حتى صيره هشيما جافا كالغثاء (tahdhib)؛ يابسا بعد خضرته (tahdhib)؛ ما يطفح ويتفرق من النبات اليابس (mufradat)","source_summary":"Toplu kaynak anlatımı, selin otlağı yığarak tadını gidermesini ve bitkinin yeşil durumdan kuru, ufalanmış hale çevrilmesini aynı sonuç çizgisinde buluşturur. Böylece yalnız kuruluk değil, önceki canlılık ve yararlılığın bir işlem sonucunda yitirilmesi de korunur.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه جعل المرعى أو النبات يابسا هشيما بعد خضرته، أو جمع السيل المرعى بعضه إلى بعض وإذهاب حلاوته حتى يصير كالغثاء.","what_is_not_ar":"لا يدخل الغثيان، ولا غثاء القدر، ولا مجرد المثل في الشيء الذي لا يعتد به إلا إذا كان مبنيا على صورة اليبس والذهاب."},"support_links":["sup_3f4b01b22ddbd600757d"]},{"boundary":"Dal, sel döküntüsünü, kuru otu veya değersiz insan benzetmesini değil, kişinin içinde duyduğu bulantı ve rahatsız edici kabarma durumunu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001073/B003","candidate_links":[{"candidate_id":"cand_5850328ea1db625cb7d4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"غُثَآء","morph_features":"STEM|POS:N|LEM:guvaA^'|ROOT:gvw|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:5:2:1","qac_word_ref":"87:5:2","surface_ar":"غُثَآءً"}],"gloss":"iç bulanması","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin içi bozulur ve rahatsız edici bir şeyle kabarıp dalgalanıyormuş gibi bir bulantı duyulur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı durum, iç bulanması adıyla veya kişinin içinin bulanmasını bildiren farklı fiil biçimleriyle anlatılır."}}],"root_ar":"غ ث و","root_id":"root_001073","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin içinde rahatsız edici bir kabarma ve bozulma olarak duyulan, kusmayı zorunlu kılmayan genel bulantı durumu için uygundur.","boundary_detail":"Dal, sel döküntüsünü, kuru otu veya değersiz insan benzetmesini değil, kişinin içinde duyduğu bulantı ve rahatsız edici kabarma durumunu anlatır.","branch_image_ar":"نفس تخبث وتغثي","concept_gloss":"iç bulanması","contextual_glosses":[{"applicability":"Bir kişinin içinde rahatsız edici bir kabarma ve kusma eğilimi hissettiğini bildiren fiil bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Durumu yaşayan kişiyi, içteki bulanmayı ve rahatsız edici kabarma duyumunu korur."},"facet_ids":["F001"],"text":"içi bulanmak","usage_role":"contextual"},{"applicability":"İç bulanmasının kısa ve doğal bir adla belirtildiği, kusma eyleminin gerçekleşip gerçekleşmediğinin açık bırakıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Rahatsız edici iç bozulmasını ve kusmadan ayrı bir duyum olarak bulantıyı korur."},"facet_ids":["F001","F002"],"text":"bulantı","usage_role":"general"}],"definition":"Kişinin içinde rahatsız edici bir şey yükseliyormuş gibi oluşan bulanma ve kabarma durumudur. Bu durum bir duyum olarak kalabilir ve kusmanın gerçekleşmesini zorunlu kılmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin içi bozulur ve rahatsız edici bir şeyle kabarıp dalgalanıyormuş gibi bir bulantı duyulur."},{"facet_id":"F002","role":"source_variant","statement":"Aynı durum, iç bulanması adıyla veya kişinin içinin bulanmasını bildiren farklı fiil biçimleriyle anlatılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Mide içeriğinin dışarı çıkarılması biçimindeki gerçekleşmiş eylemi ekler.","collision":"Duyumu, onun olası fakat zorunlu olmayan sonucu olan kusma eylemiyle karıştırır.","fit":"displacement","loses":"Kusma gerçekleşmeden de var olabilen iç bulanması ve kabarma duyumu kaybolur.","preserves":"Bulantının ilerleyebileceği aynı bedensel olay alanıyla bağlantıyı korur."},"text":"kusmak"}],"identity_rationale":"Kaynak ifadesi, kişinin içinin bozulup rahatsız edici bir şeyle kabarması biçimindeki bulantı durumunu ortak çekirdek olarak verir. Bulantı çekirdeği kabul edilmekle birlikte ikinci fiil biçimi kaynaklar arasında tartışmalıdır: ayn bunu aktarır, tahdhib ise al-Layth rivayetini sonraki dönem kullanımına bağlar.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"içi bulandı ve rahatsız edici bir şeyle kabardı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bulantı ve iç bulanması"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"içi bozulup bulandı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"iç bulanması ve bulantı"}],"lexicalization_note":"Bulantı adı ile kişinin içinin bulanmasını bildiren yapıya bağlı fiil kullanımları ayrı tutulur; tanım bunları kusma eylemine ya da genel hastalığa genişletmez.","neighbor_coverage_note":"Bütün adaylar incelendi; yayımlanan ilişkiler tam eşdeğer bulantı dalını, gebeliğe özgü dar alanı ve sık karıştırılan kusma sonucunu ayırır. Kalan adaylar genel hastalık, ağrı, ateş veya bedensel değişim alanında daha uzak kaldığı için eklenmedi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sunulan kartlara göre kapsam, katılımcı ve sonuç sınırı bakımından anlamlı bir ayrım yoktur; farklı anlatım aynı bulantı durumunu gösterir.","focus_only":null,"gloss":"bulantı ve iç bulanması","neighbor_only":null,"neighbor_ref":"root_000619/B004","relation_type":"synonym","shared_zone":"İki dal da kişinin içinin bozulması ve bulantı duyması biçimindeki aynı çekirdeği anlatır."},{"boundary_match":"partial","distinction":"Odak dal genel bulantı durumudur; komşu dal aynı durumu gebeliğin başlangıcı ve eşlik eden belirtilerle sınırlar.","focus_only":"Odak dal bulantıyı herhangi bir kişide ve belirli bir neden şartı olmadan kapsar.","gloss":"genel bulantı ile gebelik bulantısı","neighbor_only":"Komşu dal, gebeliğin ilk dönemindeki kadının bulantısına ve buna eşlik eden sık tükürmeye özgüdür.","neighbor_ref":"root_001138/B005","relation_type":"near_synonym","shared_zone":"Her iki dalda da kişinin içi bulanır ve rahatsız edici bir kusma eğilimi duyulur."},{"boundary_match":"partial","distinction":"Odak dal bir duyum ve durumdur; komşu dal ise bu duyumun ardından gelebilen, ancak onun için zorunlu olmayan dışarı çıkarma eylemidir.","focus_only":"Odak dal, kusma olmadan da yaşanabilen iç bulanması ve kabarma duyumudur.","gloss":"bulantı ile kusma","neighbor_only":"Komşu dal, mide içeriğinin dışarı çıkarıldığı gerçekleşmiş kusma olayını adlandırır.","neighbor_ref":"root_001334/B007","relation_type":"near_neighbor","shared_zone":"Bulantı kusmadan önce gelebilir ve iki durum aynı bedensel rahatsızlık sahnesinde bulunabilir."}],"source_phrase_ar":"غثت نفسه تغثي كأنها جاشت بشيء مؤذ (maqayis)؛ الغثيان خبث النفس وغثيت نفسه تغثى (ayn)؛ الغثيان خبث النفس وقد غثت نفسه تغثي غثيا وغثيانا (sihah)؛ غثت نفسه تغثى غثيا وغثيانا (tahdhib)؛ غثت نفسه تغثي غثيانا خبثت (mufradat)","source_summary":"Kaynaklar, kişinin içinde rahatsız edici bir kabarma ve bozulma olarak duyulan bulantıda birleşir. Toplu ifade durumun adını ve kişinin içinin bulanmasını bildiren biçimleri kapsar, fakat kusmayı kurucu sonuç yapmaz; ikinci fiil biçiminin geçerliliği kaynaklar arasında tartışmalıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه خبث النفس وغثيانها وجيشانها بما يؤذي، وصيغ غثت أو غثيت النفس تغثي غثيا وغثيانا.","what_is_not_ar":"لا يدخل غثاء السيل أو القدر، ولا سفلة الناس، ولا جفاف المرعى."},"support_links":["sup_33053778a4e67dd75312"]},{"boundary":"Dal, gerçek sel döküntüsünü veya bulantıyı değil, değersiz görülüp önemsenmeyen insanları ve boşa gidip kaybolan şeyleri benzetme yoluyla anlatır.","branch_kind":"bare","branch_ref":"root_001073/B004","candidate_links":[{"candidate_id":"cand_5fdeb0d46f7fbdc0b8d9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"غُثَآء","morph_features":"STEM|POS:N|LEM:guvaA^'|ROOT:gvw|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:5:2:1","qac_word_ref":"87:5:2","surface_ar":"غُثَآءً"}],"gloss":"değersiz görülüp önemsenmeyen kimse veya şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan topluluğu aşağı ve değersiz görülmesi bakımından, şey ise önemsenmeden boşa gidip kaybolması bakımından sel döküntüsüne benzetilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toplumun aşağı, önemsiz ve değer verilmeyen kesimi bu küçültücü benzetmeyle adlandırılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Önemsenmeden boşa giden ve kalıcı bir değer bırakmadan kaybolan şeyler için de aynı benzetme kullanılır."}}],"root_ar":"غ ث و","root_id":"root_001073","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem toplumun aşağı görülen kesimini hem de değer verilmeyerek boşa giden şeyi ortak küçültücü benzetme altında anlatmak için uygundur.","boundary_detail":"Dal, gerçek sel döküntüsünü veya bulantıyı değil, değersiz görülüp önemsenmeyen insanları ve boşa gidip kaybolan şeyleri benzetme yoluyla anlatır.","branch_image_ar":"غثاء لا يعتد به","concept_gloss":"değersiz görülüp önemsenmeyen kimse veya şey","contextual_glosses":[{"applicability":"Bir insan topluluğunun küçültücü biçimde değersiz, önemsiz ve dikkate alınmaz sayıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan topluluğu kapsamını, aşağı görülmeyi ve toplumsal değersizleştirme yargısını korur."},"facet_ids":["F002"],"text":"toplumun aşağı görülen kesimi","usage_role":"contextual"},{"applicability":"Bir şeyin değer görmeden, önemsenmeden ve kalıcı sonuç bırakmadan ortadan gittiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Değer verilmeme, boşa gitme ve iz bırakmadan kaybolma özelliklerini korur."},"facet_ids":["F003"],"text":"boşa gidip kaybolan şey","usage_role":"contextual"}],"definition":"Selin sürüklediği değersiz döküntüye benzetilerek, toplumun aşağı ve önemsiz görülen kesimi ya da değer verilmeyip boşa giden şey için kullanılan adlandırmadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan topluluğu aşağı ve değersiz görülmesi bakımından, şey ise önemsenmeden boşa gidip kaybolması bakımından sel döküntüsüne benzetilir."},{"facet_id":"F002","role":"specialization","statement":"Toplumun aşağı, önemsiz ve değer verilmeyen kesimi bu küçültücü benzetmeyle adlandırılır."},{"facet_id":"F003","role":"extension","statement":"Önemsenmeden boşa giden ve kalıcı bir değer bırakmadan kaybolan şeyler için de aynı benzetme kullanılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Topluluk kapsamını ve önemsenmeden boşa gidip kaybolan şeylere uzanan kullanımı dışarıda bırakır.","preserves":"İnsanlara yöneltilen küçültücü değersizlik yargısını korur."},"text":"değersiz insan"}],"identity_rationale":"Kaynak ifadesi, sel döküntüsünün değersiz ve kolayca sürüklenip gitme görüntüsünden hareketle toplumun aşağı görülen kesimine ve önemsenmeden boşa giden şeye yapılan benzetmeyi açıkça kurar. Dal çerçevesi, maddi kökeni yalnız benzetmenin dayanağı olarak tutup mecazi değersizlik çekirdeğini doğru verir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"toplumun aşağı ve değersiz görülen kesimi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"değer verilmeyip boşa giden şey"}],"lexicalization_note":"Tanım, bağımsız biçimin mecazi değersizlik anlamıyla sınırlıdır; başka dallardaki su, otlak veya bulantı yapıları bu yalın dalın anlamına taşınmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; seçilen üç komşu değersiz kişi veya şey, yalnız aşağı görülen insanlar ve soyut değersizlik niteliği arasındaki temel sınırları gösterir. Kalan adaylar aynı toplumsal küçültme alanını tekrarladığı ya da dalın çekirdeğiyle yeterli örtüşme kurmadığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın değersizlik yargısı sürüklenip giden döküntü benzetmesine bağlıdır; komşu dal ise düşmüş, kötü veya düşük değerli kişi ve malları bu benzetme şartı olmadan kapsar.","focus_only":"Odak dal, değersiz sel döküntüsüne dayanan benzetmeyi ve boşa gidip kaybolma yönünü taşır.","gloss":"önemsenmeyen döküntü benzetmesi ile değersiz düşüntü","neighbor_only":"Komşu dal kötü malı ve yemeği, gruptan düşen kişileri ve doğrudan aşağı sayılan kimseleri daha geniş biçimde kapsar.","neighbor_ref":"root_000719/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da dikkate alınmayan insanları veya düşük değerli şeyleri küçültücü biçimde adlandırabilir."},{"boundary_match":"partial","distinction":"İnsanlara uygulandığında anlamlar yaklaşır; ancak odak dal benzetmelidir ve cansız şeylere uzanır, komşu dal ise doğrudan insan topluluğuyla sınırlıdır.","focus_only":"Odak dal, insanlar yanında değer verilmeyip boşa giden şeyleri de kapsar ve sel döküntüsü benzetmesini taşır.","gloss":"döküntü benzetmesi ile aşağı görülen insanlar","neighbor_only":"Komşu dal yalnız aşağı, alt tabakadan ve önemsenmeyen insanlar için doğrudan bir toplumsal adlandırmadır.","neighbor_ref":"root_000177/B002","relation_type":"near_synonym","shared_zone":"İki dal da toplumun aşağı ve dikkate alınmaz görülen kesimini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal bu yargının yöneldiği kimseyi veya şeyi benzetmeyle adlandırır; komşu dal ise değersiz ve aşağı olma niteliğinin kendisine odaklanır.","focus_only":"Odak dal değersiz sayılan insan veya şeyi bir varlık olarak adlandırır ve boşa gitme görüntüsünü kapsar.","gloss":"önemsenmeyen varlık ile değersizlik niteliği","neighbor_only":"Komşu dal küçüklük, bayağılık ve önemsizlik niteliğini soyut ya da genel bir değer yargısı olarak anlatır.","neighbor_ref":"root_000502/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalın ortak alanı, bir kimseyi veya şeyi düşük değerli ve önemsiz sayma yargısıdır."}],"source_phrase_ar":"يقال لسفلة الناس الغثاء تشبيها بالذي ذكرناه (maqayis)؛ يضرب به المثل فيما يضيع ويذهب غير معتد به (mufradat)","source_summary":"Toplu kaynak anlatımı, değersiz sel döküntüsünü bir benzetme dayanağına dönüştürür. Bu benzetme bir yandan toplumun aşağı görülen kesimini, öte yandan önemsenmeden boşa gidip kaybolan şeyi anlatır.","sources":["MQ","MU"],"what_is_ar":"يدخل فيه إطلاق الغثاء على سفلة الناس أو على ما يضيع ويذهب غير معتد به، تشبيها بغثاء السيل.","what_is_not_ar":"لا يدخل المعنى الحسي للغثاء نفسه إلا أصلا للتشبيه، ولا يدخل الغثيان."},"support_links":["sup_1b557f13d09d6802a6ae"]}],"candidate_inventory":[{"anchor_refs":["87:5:1"],"branch_refs":[],"candidate_id":"cand_09df29ca9042b5257ade","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:5:1:attached-proclitic-form","source_type":"word_analysis","support_ids":["sup_1f0562eec16eee1514b6","sup_7fca4e8f6edd6cc222cd"],"title":"small particle fused to the conversion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:1","qac_refs":["87:5:1:1"],"status":"accepted"}},{"anchor_refs":["87:5:1"],"branch_refs":[],"candidate_id":"cand_f5d46812e1c5c80d0dc6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:5:1:lifecycle-hinge","source_type":"word_analysis","support_ids":["sup_7fca4e8f6edd6cc222cd","sup_a562d4776bceacdc85b6"],"title":"growth and exhaustion read together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:1","qac_refs":["87:5:1:1"],"status":"accepted"}},{"anchor_refs":["87:5:1"],"branch_refs":[],"candidate_id":"cand_6755789968f55da23856","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:5:1:relative-chain-coordination","source_type":"word_analysis","support_ids":["sup_7fca4e8f6edd6cc222cd","sup_e5a72f1a2d50a98b0673"],"title":"same subject and chain continue","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:1","qac_refs":["87:5:1:1"],"status":"accepted"}},{"anchor_refs":["87:5:1"],"branch_refs":[],"candidate_id":"cand_ccbc2e76d7f26955f8f5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:5:1:resultive-sequel","source_type":"word_analysis","support_ids":["sup_7fca4e8f6edd6cc222cd","sup_f6a8902fb5ce1cce2e6f"],"title":"resultive sequel to the prior pasture","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:1","qac_refs":["87:5:1:1"],"status":"accepted"}},{"anchor_refs":["87:5:2"],"branch_refs":[],"candidate_id":"cand_d7b060e0b3cc59360cdd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"87:5:2:boundary-arguments","source_type":"word_analysis","support_ids":["sup_3a9a9177329bb0effbf9","sup_721b8f996de376b102d5"],"title":"agent and object cross the boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:2","qac_refs":["87:5:1:2","87:5:1:3"],"status":"accepted"}},{"anchor_refs":["87:5:2"],"branch_refs":[],"candidate_id":"cand_0a837e4e73219dde967d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"87:5:2:boundary-lifecycle-reversal","source_type":"word_analysis","support_ids":["sup_3a9a9177329bb0effbf9","sup_ffd08b7040b55152d67f"],"title":"same object enters the afterstate scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:2","qac_refs":["87:5:1:2","87:5:1:3"],"status":"accepted"}},{"anchor_refs":["87:5:2"],"branch_refs":[],"candidate_id":"cand_6459582845198815d3ef","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"87:5:2:completed-rendering","source_type":"word_analysis","support_ids":["sup_3a9a9177329bb0effbf9","sup_f15794cda4f214918e0c"],"title":"completed act of conversion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:2","qac_refs":["87:5:1:2","87:5:1:3"],"status":"accepted"}},{"anchor_refs":["87:5:2"],"branch_refs":[],"candidate_id":"cand_24610f3c47715c8971c2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"87:5:2:conversion-frame-engine","source_type":"word_analysis","support_ids":["sup_3a9a9177329bb0effbf9","sup_d5335a15a712122f5d4b"],"title":"verb organizes the three-step frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:2","qac_refs":["87:5:1:2","87:5:1:3"],"status":"accepted"}},{"anchor_refs":["87:5:2"],"branch_refs":[],"candidate_id":"cand_908649c3243f565c0fce","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"87:5:2:form-i-directness","source_type":"word_analysis","support_ids":["sup_3a9a9177329bb0effbf9","sup_8a581d393c0a492086ba"],"title":"Form I directness over marked extensions","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:2","qac_refs":["87:5:1:2","87:5:1:3"],"status":"accepted"}},{"anchor_refs":["87:5:2"],"branch_refs":[],"candidate_id":"cand_3123ca89ffc2114dcb1f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"87:5:2:intertextual-life-refuse-contrast","source_type":"word_analysis","support_ids":["sup_3a9a9177329bb0effbf9","sup_c3eafc19fb6dfdd0ccec"],"title":"same root links life elsewhere and residue here","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:2","qac_refs":["87:5:1:2","87:5:1:3"],"status":"accepted"}},{"anchor_refs":["87:5:2"],"branch_refs":[],"candidate_id":"cand_42be52fa1918d8158bc4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"87:5:2:made-refuse-pairing","source_type":"word_analysis","support_ids":["sup_3a9a9177329bb0effbf9","sup_f3b369b7753e4ad942de"],"title":"making-refuse pairing echoes 23:41","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:2","qac_refs":["87:5:1:2","87:5:1:3"],"status":"accepted"}},{"anchor_refs":["87:5:2"],"branch_refs":[],"candidate_id":"cand_2ca4927152ad04c16fdd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"87:5:2:pronoun-continuity","source_type":"word_analysis","support_ids":["sup_3a9a9177329bb0effbf9","sup_3bb8c9c5965c11c2e99d"],"title":"known pasture carried by the suffix","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:2","qac_refs":["87:5:1:2","87:5:1:3"],"status":"accepted"}},{"anchor_refs":["87:5:2"],"branch_refs":[],"candidate_id":"cand_c586d05df3b736d5b809","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"87:5:2:result-valency","source_type":"word_analysis","support_ids":["sup_3a9a9177329bb0effbf9","sup_f3622865cd1330a98269"],"title":"object plus result complement enact transformation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:2","qac_refs":["87:5:1:2","87:5:1:3"],"status":"accepted"}},{"anchor_refs":["87:5:2"],"branch_refs":[],"candidate_id":"cand_6201ee13bfaedd33987a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"87:5:2:sound-pressure","source_type":"word_analysis","support_ids":["sup_3a9a9177329bb0effbf9","sup_404352b457c1c7a852cd"],"title":"compact consonantal pressure before residue","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:2","qac_refs":["87:5:1:2","87:5:1:3"],"status":"accepted"}},{"anchor_refs":["87:5:2"],"branch_refs":[],"candidate_id":"cand_d4aef58d182e8f078ef3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"87:5:2:state-setting-root-pressure","source_type":"word_analysis","support_ids":["sup_3a9a9177329bb0effbf9","sup_86dcf0b756e53f6320f8"],"title":"making and assignment pressure narrows to rendering","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:2","qac_refs":["87:5:1:2","87:5:1:3"],"status":"accepted"}},{"anchor_refs":["87:5:3"],"branch_refs":[],"candidate_id":"cand_7f7066489ccac72a722a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001073"],"scope":"focus_ayah","source_local_id":"87:5:3:abrasive-sound-shape","source_type":"word_analysis","support_ids":["sup_2bbc744696899bfb5bee","sup_46b66af23f9936ca6585"],"title":"rough sound shape suits debris","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:3","qac_refs":["87:5:2:1"],"status":"accepted"}},{"anchor_refs":["87:5:3"],"branch_refs":[],"candidate_id":"cand_f88695dd96e2fec85151","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001073"],"scope":"focus_ayah","source_local_id":"87:5:3:adjective-binding","source_type":"word_analysis","support_ids":["sup_2bbc744696899bfb5bee","sup_577aa20f4af5c32c1bfc"],"title":"residue noun receives the final color","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:3","qac_refs":["87:5:2:1"],"status":"accepted"}},{"anchor_refs":["87:5:3"],"branch_refs":[],"candidate_id":"cand_86494bb164e1be52ca94","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001073"],"scope":"focus_ayah","source_local_id":"87:5:3:indefinite-result-complement","source_type":"word_analysis","support_ids":["sup_2bbc744696899bfb5bee","sup_7ee61b0e925e1e6c9cb7"],"title":"indefinite accusative result state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:3","qac_refs":["87:5:2:1"],"status":"accepted"}},{"anchor_refs":["87:5:3"],"branch_refs":[],"candidate_id":"cand_ba13fa86f679aaeb3583","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001073"],"scope":"focus_ayah","source_local_id":"87:5:3:marked-rare-choice","source_type":"word_analysis","support_ids":["sup_2bbc744696899bfb5bee","sup_beaad6b8bc8a51f1d549"],"title":"rare noun sharper than ordinary plant death","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:3","qac_refs":["87:5:2:1"],"status":"accepted"}},{"anchor_refs":["87:5:3"],"branch_refs":[],"candidate_id":"cand_7d258b60fd19ecc19609","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001073"],"scope":"focus_ayah","source_local_id":"87:5:3:mass-concrete-substance","source_type":"word_analysis","support_ids":["sup_2bbc744696899bfb5bee","sup_6e63ad84486d7453e50a"],"title":"mass substance rather than process","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:3","qac_refs":["87:5:2:1"],"status":"accepted"}},{"anchor_refs":["87:5:3"],"branch_refs":[],"candidate_id":"cand_8d00cb338bcfb44c8b3f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001073"],"scope":"focus_ayah","source_local_id":"87:5:3:material-endpoint-structure","source_type":"word_analysis","support_ids":["sup_2bbc744696899bfb5bee","sup_b86de70dc5827990fd1a"],"title":"middle beat turns action into tableau","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:3","qac_refs":["87:5:2:1"],"status":"accepted"}},{"anchor_refs":["87:5:3"],"branch_refs":[],"candidate_id":"cand_3f8687301c6eecdb910a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001073"],"scope":"focus_ayah","source_local_id":"87:5:3:pasture-boundary-reversal","source_type":"word_analysis","support_ids":["sup_191d3c1ed5c517bcb409","sup_2bbc744696899bfb5bee"],"title":"provided pasture becomes uncared-for refuse","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:3","qac_refs":["87:5:2:1"],"status":"accepted"}},{"anchor_refs":["87:5:3"],"branch_refs":[],"candidate_id":"cand_c666136e4c002a485e3e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001073"],"scope":"focus_ayah","source_local_id":"87:5:3:phrase-cadence-to-color","source_type":"word_analysis","support_ids":["sup_2bbc744696899bfb5bee","sup_839f4d43251ad00df574"],"title":"residue resolves into final color cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:3","qac_refs":["87:5:2:1"],"status":"accepted"}},{"anchor_refs":["87:5:3"],"branch_refs":[],"candidate_id":"cand_52ae50cf2d7b904680f4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001073"],"scope":"focus_ayah","source_local_id":"87:5:3:rare-made-refuse-echo","source_type":"word_analysis","support_ids":["sup_109bcd2e6ab2081abc32","sup_2bbc744696899bfb5bee"],"title":"rare residue word echoes 23:41","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:3","qac_refs":["87:5:2:1"],"status":"accepted"}},{"anchor_refs":["87:5:3"],"branch_refs":[],"candidate_id":"cand_6c12d5c6bd115be8466b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001073"],"scope":"focus_ayah","source_local_id":"87:5:3:residue-scum-range","source_type":"word_analysis","support_ids":["sup_0d31c5460382752fd16f","sup_2bbc744696899bfb5bee"],"title":"stubble and flood-scum imagery","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:3","qac_refs":["87:5:2:1"],"status":"accepted"}},{"anchor_refs":["87:5:3"],"branch_refs":[],"candidate_id":"cand_f25e9718d480b622371a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001073"],"scope":"focus_ayah","source_local_id":"87:5:3:value-collapse","source_type":"word_analysis","support_ids":["sup_2bbc744696899bfb5bee","sup_45b98c135f3cf0a64f66"],"title":"provision becomes waste matter","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:3","qac_refs":["87:5:2:1"],"status":"accepted"}},{"anchor_refs":["87:5:3"],"branch_refs":[],"candidate_id":"cand_c03e39d6e1be9c8e7ff4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001073"],"scope":"focus_ayah","source_local_id":"87:5:3:verb-result-formula","source_type":"word_analysis","support_ids":["sup_2bbc744696899bfb5bee","sup_910eb0802d3a245970ce"],"title":"compact making-refuse formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:3","qac_refs":["87:5:2:1"],"status":"accepted"}},{"anchor_refs":["87:5:4"],"branch_refs":[],"candidate_id":"cand_30d844d61013b0d9d2a8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000374"],"scope":"focus_ayah","source_local_id":"87:5:4:adjective-attachment","source_type":"word_analysis","support_ids":["sup_e211cbc8d26dd93a74bc","sup_e964a413e2c861dbf77a"],"title":"final adjective colors the residue","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:4","qac_refs":["87:5:3:1"],"status":"accepted"}},{"anchor_refs":["87:5:4"],"branch_refs":[],"candidate_id":"cand_69ef9fd7cb919149ef7b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000374"],"scope":"focus_ayah","source_local_id":"87:5:4:black-green-color-range","source_type":"word_analysis","support_ids":["sup_8ce162793284494ccb82","sup_e964a413e2c861dbf77a"],"title":"dark color holds greenness and decay","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:4","qac_refs":["87:5:3:1"],"status":"accepted"}},{"anchor_refs":["87:5:4"],"branch_refs":[],"candidate_id":"cand_941838035365af9f1abd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000374"],"scope":"focus_ayah","source_local_id":"87:5:4:containment-resonance","source_type":"word_analysis","support_ids":["sup_0365a99e0f5dd548a3d4","sup_e964a413e2c861dbf77a"],"title":"gathering pressure fits compacted residue","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:4","qac_refs":["87:5:3:1"],"status":"accepted"}},{"anchor_refs":["87:5:4"],"branch_refs":[],"candidate_id":"cand_cd58cae1a28fccfb705e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000374"],"scope":"focus_ayah","source_local_id":"87:5:4:darkening-process-pressure","source_type":"word_analysis","support_ids":["sup_457c505a52ea8348f438","sup_e964a413e2c861dbf77a"],"title":"visible darkening as completed trace","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:4","qac_refs":["87:5:3:1"],"status":"accepted"}},{"anchor_refs":["87:5:4"],"branch_refs":[],"candidate_id":"cand_feea1db0336fa3a59fb1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000374"],"scope":"focus_ayah","source_local_id":"87:5:4:form-color-state","source_type":"word_analysis","support_ids":["sup_d6f83305f894de56baa0","sup_e964a413e2c861dbf77a"],"title":"color-state form closes the clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:4","qac_refs":["87:5:3:1"],"status":"accepted"}},{"anchor_refs":["87:5:4"],"branch_refs":[],"candidate_id":"cand_05fd5ed8e2cdf4cb68c4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000374"],"scope":"focus_ayah","source_local_id":"87:5:4:lifecycle-sensory-boundary","source_type":"word_analysis","support_ids":["sup_2b455089da5dbe36b516","sup_e964a413e2c861dbf77a"],"title":"green provision shifts to dark afterstate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:4","qac_refs":["87:5:3:1"],"status":"accepted"}},{"anchor_refs":["87:5:4"],"branch_refs":[],"candidate_id":"cand_898e5d41215465f082dd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000374"],"scope":"focus_ayah","source_local_id":"87:5:4:next-ayah-cadence","source_type":"word_analysis","support_ids":["sup_72112d61bb7d5ad66599","sup_e964a413e2c861dbf77a"],"title":"final cadence carries into the next assurance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:4","qac_refs":["87:5:3:1"],"status":"accepted"}},{"anchor_refs":["87:5:4"],"branch_refs":[],"candidate_id":"cand_7a42ee5a21c1df64c1d0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000374"],"scope":"focus_ayah","source_local_id":"87:5:4:open-final-cadence","source_type":"word_analysis","support_ids":["sup_dee4d75cce99a84b683c","sup_e964a413e2c861dbf77a"],"title":"open final sound lets the color linger","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:4","qac_refs":["87:5:3:1"],"status":"accepted"}},{"anchor_refs":["87:5:4"],"branch_refs":[],"candidate_id":"cand_b531225c7ff168c11d28","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000374"],"scope":"focus_ayah","source_local_id":"87:5:4:other-root-occurrence-contrast","source_type":"word_analysis","support_ids":["sup_406372b6948bd317b89c","sup_e964a413e2c861dbf77a"],"title":"other root material contrasts with this color use","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:4","qac_refs":["87:5:3:1"],"status":"accepted"}},{"anchor_refs":["87:5:4"],"branch_refs":[],"candidate_id":"cand_4668fdfd95e7a23725a1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000374"],"scope":"focus_ayah","source_local_id":"87:5:4:rare-final-color-choice","source_type":"word_analysis","support_ids":["sup_cfa66aa76754415671ce","sup_e964a413e2c861dbf77a"],"title":"rare exact color adjective","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:4","qac_refs":["87:5:3:1"],"status":"accepted"}},{"anchor_refs":["87:5:4"],"branch_refs":[],"candidate_id":"cand_b03e60584dea1cae95b2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000374"],"scope":"focus_ayah","source_local_id":"87:5:4:sifa-hal-tension","source_type":"word_analysis","support_ids":["sup_5bea12eccafb5bf1ed2a","sup_e964a413e2c861dbf77a"],"title":"color can also press toward the transformed object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:4","qac_refs":["87:5:3:1"],"status":"accepted"}},{"anchor_refs":["87:5:4"],"branch_refs":[],"candidate_id":"cand_37391a352f908774a5d4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000374"],"scope":"focus_ayah","source_local_id":"87:5:4:substance-quality-sound-link","source_type":"word_analysis","support_ids":["sup_703663f534644444ce8b","sup_e964a413e2c861dbf77a"],"title":"open sound links residue and color","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:4","qac_refs":["87:5:3:1"],"status":"accepted"}},{"anchor_refs":["87:5:4"],"branch_refs":[],"candidate_id":"cand_7838fbc91dcd3cbb445e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000374"],"scope":"focus_ayah","source_local_id":"87:5:4:visual-endpoint","source_type":"word_analysis","support_ids":["sup_8dd2d744b237d189d3ba","sup_e964a413e2c861dbf77a"],"title":"conversion sequence ends in visible color","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:5:4","qac_refs":["87:5:3:1"],"status":"accepted"}},{"anchor_refs":["87:5:1"],"branch_refs":[],"candidate_id":"cand_927bddf2771617bff910","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"87:5:1:2","source_type":"qac_morpheme","support_ids":["sup_4b5229419172394199b7"],"title":"QAC root occurrence: ج ع ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:5:2"],"branch_refs":[],"candidate_id":"cand_0581694e67efab34d55d","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001073"],"scope":"focus_ayah","source_local_id":"87:5:2:1","source_type":"qac_morpheme","support_ids":["sup_58700b2606492a1dc176"],"title":"QAC root occurrence: غ ث و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:5:3"],"branch_refs":[],"candidate_id":"cand_d633b9e652bbb3394879","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000374"],"scope":"focus_ayah","source_local_id":"87:5:3:1","source_type":"qac_morpheme","support_ids":["sup_4187b45eec24b84f2fb9"],"title":"QAC root occurrence: ح و ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:5","branch_refs":["root_000248/B002","root_000374/B006","root_001073/B002"],"candidate_id":"cand_69fcf9534f45539b2909","commentary_obligation":"review","hft_ref":"hft_f51cce417fc48518366f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_resultative_decay","source_type":"hft","support_ids":["sup_3f4b01b22ddbd600757d"],"title":"base_resultative_decay","trust":"legacy_unbound"},{"anchor_refs":["87:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:5","branch_refs":["root_000248/B002","root_000374/B001","root_000374/B008","root_001073/B001"],"candidate_id":"cand_8b3cceff415da6700cec","commentary_obligation":"review","hft_ref":"hft_17146e8c5ac85d1f3211","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_fluvial_aggregation","source_type":"hft","support_ids":["sup_ea7f41da09281fecc31c"],"title":"base_fluvial_aggregation","trust":"legacy_unbound"},{"anchor_refs":["87:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:5","branch_refs":["root_000248/B002","root_000374/B006","root_001073/B004"],"candidate_id":"cand_5fdeb0d46f7fbdc0b8d9","commentary_obligation":"review","hft_ref":"hft_725a1ff25a4b8981f15f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_value_collapse","source_type":"hft","support_ids":["sup_1b557f13d09d6802a6ae"],"title":"base_value_collapse","trust":"legacy_unbound"},{"anchor_refs":["87:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:5","branch_refs":["root_000248/B002","root_000374/B003","root_001073/B003"],"candidate_id":"cand_5850328ea1db625cb7d4","commentary_obligation":"review","hft_ref":"hft_5df4da3c31bd0add90e8","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier_visceral_ecology","source_type":"hft","support_ids":["sup_33053778a4e67dd75312"],"title":"outlier_visceral_ecology","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:5:1:1","qac_word_ref":"87:5:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:5:1:2","qac_word_ref":"87:5:1","root_ar":"ج ع ل","surface_ar":"جَعَلَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"87:5:1:3","qac_word_ref":"87:5:1","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"غُثَآء","morph_features":"STEM|POS:N|LEM:guvaA^'|ROOT:gvw|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:5:2:1","qac_word_ref":"87:5:2","root_ar":"غ ث و","surface_ar":"غُثَآءً"},{"lemma_ar":"أَحْوَىٰ","morph_features":"STEM|POS:ADJ|LEM:>aHowaY`|ROOT:Hwy|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:5:3:1","qac_word_ref":"87:5:3","root_ar":"ح و ي","surface_ar":"أَحْوَىٰ"}],"word_analysis_qac_refs":[["87:5:1:1"],["87:5:1:2","87:5:1:3"],["87:5:2:1"],["87:5:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["87:5:1","87:5:2","87:5:3","87:5:4"]},"focus_surface_evidence":{"arabic_uthmani":"فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:5:1:1","qac_word_ref":"87:5:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:5:1:2","qac_word_ref":"87:5:1","root_ar":"ج ع ل","surface_ar":"جَعَلَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"87:5:1:3","qac_word_ref":"87:5:1","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"غُثَآء","morph_features":"STEM|POS:N|LEM:guvaA^'|ROOT:gvw|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:5:2:1","qac_word_ref":"87:5:2","root_ar":"غ ث و","surface_ar":"غُثَآءً"},{"lemma_ar":"أَحْوَىٰ","morph_features":"STEM|POS:ADJ|LEM:>aHowaY`|ROOT:Hwy|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"87:5:3:1","qac_word_ref":"87:5:3","root_ar":"ح و ي","surface_ar":"أَحْوَىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["87:5:1:1"],["87:5:1:2","87:5:1:3"],["87:5:2:1"],["87:5:3:1"]],"word_analysis_refs":["87:5:1","87:5:2","87:5:3","87:5:4"],"word_rows":[{"analysis_record_ref":"87:5:1","analytic_gloss_range_en":"resultive and sequential connector binding the new clause to the prior pasture-emergence","analytic_root_gloss_range_en":null,"qac_refs":["87:5:1:1"],"root":{"note":"no root"},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"87:5:2","analytic_gloss_range_en":"perfect Form I rendering of the prior pasture into a new result-state, with attached object continuity","analytic_root_gloss_range_en":"making, rendering, placing, assigning, and other nominal side-branches; the local pronoun plus result complement selects state-rendering rather than all root branches","qac_refs":["87:5:1:2","87:5:1:3"],"root":{"arabic":"ج ع ل","transliteration":"j-ʿ-l"},"surface":{"arabic":"جَعَلَهُۥ","transliteration":"jaʿalahū"}},{"analysis_record_ref":"87:5:3","analytic_gloss_range_en":"indefinite accusative result noun naming the pasture's reduced matter as refuse, stubble, chaff, or flood-scum residue","analytic_root_gloss_range_en":"floating flood refuse, spoiled pasture chaff, nausea, and metaphorical waste; the local noun selects residue/refuse while allowing stubble and flood-scum imagery","qac_refs":["87:5:2:1"],"root":{"arabic":"غ ث و","transliteration":"gh-th-w"},"surface":{"arabic":"غُثَآءً","transliteration":"ghuthāʾan"}},{"analysis_record_ref":"87:5:4","analytic_gloss_range_en":"final accusative color adjective qualifying the residue as dark, dusky, black-green, or visibly withered","analytic_root_gloss_range_en":"gathering and containing, coiling, inward folds, dwellings, water catchments, plants, sickness, and dark reddish or black-green coloring; the local adjective selects the color branch while containment pressure survives only as compacted-residue resonance","qac_refs":["87:5:3:1"],"root":{"arabic":"ح و ي","transliteration":"ḥ-w-y"},"surface":{"arabic":"أَحْوَىٰ","transliteration":"aḥwā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["87:5"],"branch_refs":["root_000248/B002","root_000374/B006","root_001073/B002"],"candidate_id":"cand_69fcf9534f45539b2909","evidence_scope":"focus_ayah","hft_ref":"hft_f51cce417fc48518366f","item_id":"base_resultative_decay","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_resultative_decay","support_id":"sup_3f4b01b22ddbd600757d"},{"anchor_refs":["87:5"],"branch_refs":["root_000248/B002","root_000374/B001","root_000374/B008","root_001073/B001"],"candidate_id":"cand_8b3cceff415da6700cec","evidence_scope":"focus_ayah","hft_ref":"hft_17146e8c5ac85d1f3211","item_id":"base_fluvial_aggregation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_fluvial_aggregation","support_id":"sup_ea7f41da09281fecc31c"},{"anchor_refs":["87:5"],"branch_refs":["root_000248/B002","root_000374/B006","root_001073/B004"],"candidate_id":"cand_5fdeb0d46f7fbdc0b8d9","evidence_scope":"focus_ayah","hft_ref":"hft_725a1ff25a4b8981f15f","item_id":"base_value_collapse","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_value_collapse","support_id":"sup_1b557f13d09d6802a6ae"},{"anchor_refs":["87:5"],"branch_refs":["root_000248/B002","root_000374/B003","root_001073/B003"],"candidate_id":"cand_5850328ea1db625cb7d4","evidence_scope":"focus_ayah","hft_ref":"hft_5df4da3c31bd0add90e8","item_id":"outlier_visceral_ecology","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_visceral_ecology","support_id":"sup_33053778a4e67dd75312"}],"diagnostics":[],"lane_counts":{"global":9,"macro":11,"micro":4},"packet_summary":{"ayah_count":19,"focus_ref":"87:5","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ء ث ر","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":true,"target_occurrences":9,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]}],"window":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"87:5","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"87:5","lane":"micro","linguistic_source_ref":"87:5","surface_ref":"87:5","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"87:5","target_tokens":[["Sonra",["87:5:1"]],["onu",["87:5:1"]],["kapkara",["87:5:3"]],["bir",["87:5:2"]],["çerçöpe",["87:5:2"]],["çevirdi",["87:5:1"]]],"text":"Sonra onu kapkara bir çerçöpe çevirdi."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s087-p01-001-019","label":"Whole surah","number":1,"refs":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:4:containment-resonance","source_type":"word_analysis","support_id":"sup_0365a99e0f5dd548a3d4","text":"{\"blocking_evidence\":null,\"headline\":\"gathering pressure fits compacted residue\",\"reader_payoff\":\"The reader may hear compacted or gathered residue behind the dark color, while the active local sense remains color.\",\"reason\":\"V4 separates gathering/containment from the color branch; the local adjective selects color, with containment retained only as resonance suited to compacted refuse.\",\"representative_source_ids\":[\"QS-283995da\",\"QE-b7f04541\",\"QI-b97139b1\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:3:residue-scum-range","source_type":"word_analysis","support_id":"sup_0d31c5460382752fd16f","text":"{\"blocking_evidence\":null,\"headline\":\"stubble and flood-scum imagery\",\"reader_payoff\":\"The reader pictures more than dry vegetation: the endpoint can feel like stubble, chaff, swept debris, and flood-borne scum.\",\"reason\":\"V4 supports both flood-borne refuse and dried pasture chaff branches for the local noun, while nausea and unrelated metaphor branches are not selected here.\",\"representative_source_ids\":[\"QS-12c8eb27\",\"QS-4e0ae781\",\"MS-4d87ee20\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:3:rare-made-refuse-echo","source_type":"word_analysis","support_id":"sup_109bcd2e6ab2081abc32","text":"{\"blocking_evidence\":null,\"headline\":\"rare residue word echoes 23:41\",\"reader_payoff\":\"The reader hears the rare residue noun as marked and mutually illuminated by its made-refuse occurrence in 23:41.\",\"reason\":\"The root and noun are low-occurrence, and the supplied 23:41 evidence gives a concrete echo of being made into refuse without controlling the local vegetation scene.\",\"representative_source_ids\":[\"QI-aa300ede\",\"MI-12ca52cb\",\"QH-2f38831c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:3:pasture-boundary-reversal","source_type":"word_analysis","support_id":"sup_191d3c1ed5c517bcb409","text":"{\"blocking_evidence\":null,\"headline\":\"provided pasture becomes uncared-for refuse\",\"reader_payoff\":\"The reader sees the prior care-field reversed into the afterlife of what remains after value is gone.\",\"reason\":\"The noun's residue range and the cross-boundary object continuity make the provision-to-refuse reversal locally coherent.\",\"representative_source_ids\":[\"QS-c1695ea5\",\"QB-2db29ee2\",\"QH-2f38831c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:1:attached-proclitic-form","source_type":"word_analysis","support_id":"sup_1f0562eec16eee1514b6","text":"{\"blocking_evidence\":null,\"headline\":\"small particle fused to the conversion\",\"reader_payoff\":\"The reader notices that the connector is separable for analysis but fused in recitation and writing to the conversion act it introduces.\",\"reason\":\"The bundle segmentation splits {{ar:فَ}} ({{tr:fa}}) as a particle while the surface keeps it attached to {{ar:جَعَلَهُۥ}} ({{tr:jaʿalahū}}).\",\"representative_source_ids\":[\"QF-dc464ac1\",\"QP-84152a3b\",\"MT-1e91aa77\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:4:lifecycle-sensory-boundary","source_type":"word_analysis","support_id":"sup_2b455089da5dbe36b516","text":"{\"blocking_evidence\":null,\"headline\":\"green provision shifts to dark afterstate\",\"reader_payoff\":\"The reader sees the same ecological object at the far side of its lifecycle, where vitality and decay meet in one color word.\",\"reason\":\"The adjective's color range and final position converge with the boundary continuity of the transformed pasture.\",\"representative_source_ids\":[\"QS-f886b294\",\"QB-6154ec89\",\"QY-16145abc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:3","source_type":"word_analysis","support_id":"sup_2bbc744696899bfb5bee","text":"{\"gloss_range\":\"indefinite accusative result noun naming the pasture's reduced matter as refuse, stubble, chaff, or flood-scum residue\",\"prose\":\"{{ar:غُثَآءً}} ({{tr:ghuthāʾan}}) names the material endpoint of the making. Its accusative indefiniteness makes the known pasture become a class of low-value residue, not a named remnant, and its position after {{ar:جَعَلَهُۥ}} ({{tr:jaʿalahū}}) makes it the result complement rather than an incidental description. As a concrete mass noun, it freezes the process into collective matter rather than counted stalks or an ongoing action. Lexically, the word is sharper than generic dryness: stubble, chaff, swept plant matter, and flood-scum can all inform the image, so usefulness, rootedness, and stable form collapse into refuse, and the prior care-field of pasture becomes legible by contrast. The rare noun also echoes the made-refuse use in 23:41 without importing that scene's actors. In the clause's middle beat, the rough consonants and internal hamza turn the action into visible, audible debris before {{ar:أَحْوَىٰ}} ({{tr:aḥwā}}) seals it with color; that final color primarily qualifies the refuse-state, while the possible circumstantial hearing keeps the transformed pasture itself in view.\",\"root_display\":\"{{ar:غ ث و}} ({{tr:gh-th-w}})\",\"root_gloss_range\":\"floating flood refuse, spoiled pasture chaff, nausea, and metaphorical waste; the local noun selects residue/refuse while allowing stubble and flood-scum imagery\",\"surface_display\":\"{{ar:غُثَآءً}} ({{tr:ghuthāʾan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:2","source_type":"word_analysis","support_id":"sup_3a9a9177329bb0effbf9","text":"{\"gloss_range\":\"perfect Form I rendering of the prior pasture into a new result-state, with attached object continuity\",\"prose\":\"{{ar:جَعَلَهُۥ}} ({{tr:jaʿalahū}}) is the engine of the ayah's conversion. The perfect Form I verb presents the rendering as an accomplished act, not an intensified or marked causative extension, while the attached {{ar:هُۥ}} ({{tr:hū}}) carries the known pasture from 87:4 into a new predicate. Grammar is doing the transformation: the verb requires the object and the result complement {{ar:غُثَآءً}} ({{tr:ghuthāʾan}}), so the pasture is not replaced offstage but made to become residue onstage. The agent and object both depend on the prior boundary, yet their slots stay distinct: the implicit subject continues the divine descriptor chain while the suffix carries the transformed pasture. The root's making, placing, and assigning range survives as state-setting pressure, but local valency narrows it to direct rendering, not the auxiliary, reward, naming, or other side branches. The pairing with {{ar:غُثَآءً}} ({{tr:ghuthāʾan}}) also resonates with the made-refuse scene in 23:41, while 21:30 provides a contrast where a same-root form links water to life; before the rougher residue noun arrives, the compact consonantal texture gives the conversion a firm audible push.\",\"root_display\":\"{{ar:ج ع ل}} ({{tr:j-ʿ-l}})\",\"root_gloss_range\":\"making, rendering, placing, assigning, and other nominal side-branches; the local pronoun plus result complement selects state-rendering rather than all root branches\",\"surface_display\":\"{{ar:جَعَلَهُۥ}} ({{tr:jaʿalahū}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:2:pronoun-continuity","source_type":"word_analysis","support_id":"sup_3bb8c9c5965c11c2e99d","text":"{\"blocking_evidence\":null,\"headline\":\"known pasture carried by the suffix\",\"reader_payoff\":\"The reader notices continuity before degradation: the same known pasture is carried forward before it is renamed as residue.\",\"reason\":\"Attachment evidence identifies the {{ar:هُۥ}} ({{tr:hū}}) suffix as the direct object and as resuming the nearby pasture object from 87:4.\",\"representative_source_ids\":[\"QG-c877c681\",\"QG-ceffc100\",\"MT-5d78d8af\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:2:sound-pressure","source_type":"word_analysis","support_id":"sup_404352b457c1c7a852cd","text":"{\"blocking_evidence\":null,\"headline\":\"compact consonantal pressure before residue\",\"reader_payoff\":\"The reader hears a compact verbal pressure before the rougher residue noun arrives.\",\"reason\":\"The phonetic observation is modest but tied to the attested surface of {{ar:جَعَلَهُۥ}} ({{tr:jaʿalahū}}) before {{ar:غُثَآءً}} ({{tr:ghuthāʾan}}).\",\"representative_source_ids\":[\"QP-513a0ba8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:4:other-root-occurrence-contrast","source_type":"word_analysis","support_id":"sup_406372b6948bd317b89c","text":"{\"blocking_evidence\":null,\"headline\":\"other root material contrasts with this color use\",\"reader_payoff\":\"The reader sees 87:5 foregrounding a rare color deployment against other concrete root material, including the containment context in 6:146.\",\"reason\":\"The supplied 6:146 contrast is useful for root-range contrast, but it does not activate non-color branches as the local sense.\",\"representative_source_ids\":[\"QI-acbb58d1\",\"QI-b97139b1\",\"QH-d85eda9e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:5:3:1","source_type":"qac_morpheme","support_id":"sup_4187b45eec24b84f2fb9","text":"{\"lemma_ar\":\"أَحْوَىٰ\",\"morph_features\":\"STEM|POS:ADJ|LEM:>aHowaY`|ROOT:Hwy|MS|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"87:5:3:1\",\"qac_word_ref\":\"87:5:3\",\"root_ar\":\"ح و ي\",\"surface_ar\":\"أَحْوَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:4:darkening-process-pressure","source_type":"word_analysis","support_id":"sup_457c505a52ea8348f438","text":"{\"blocking_evidence\":null,\"headline\":\"visible darkening as completed trace\",\"reader_payoff\":\"The reader notices the final color as the visible trace of spentness, not merely a static label.\",\"reason\":\"The local surface is an adjective, so process language is kept as color-change pressure rather than a separate verbal action.\",\"representative_source_ids\":[\"QS-354ce7b7\",\"QS-d4fcf8c6\",\"QS-fa8b7734\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:3:value-collapse","source_type":"word_analysis","support_id":"sup_45b98c135f3cf0a64f66","text":"{\"blocking_evidence\":null,\"headline\":\"provision becomes waste matter\",\"reader_payoff\":\"The reader notices the reversal from usable provision to low-value leftover matter.\",\"reason\":\"The same prior pasture is the object transformed into residue, so the negative evaluative force of refuse is locally attached to the provision object.\",\"representative_source_ids\":[\"QS-17e59b72\",\"QS-823dcd71\",\"QB-fdc03a55\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:3:abrasive-sound-shape","source_type":"word_analysis","support_id":"sup_46b66af23f9936ca6585","text":"{\"blocking_evidence\":null,\"headline\":\"rough sound shape suits debris\",\"reader_payoff\":\"The reader hears the residue word as marked by elongation, guttural and interdental pressure, and a hamza catch before the phrase resolves.\",\"reason\":\"The sound claims are tied to the actual surface of {{ar:غُثَآءً}} ({{tr:ghuthāʾan}}) and remain modest support for the debris image.\",\"representative_source_ids\":[\"QF-b51969b9\",\"QP-81b243da\",\"MP-4df8fcaf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:5:1:2","source_type":"qac_morpheme","support_id":"sup_4b5229419172394199b7","text":"{\"lemma_ar\":\"جَعَلَ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:jaEala|ROOT:jEl|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"87:5:1:2\",\"qac_word_ref\":\"87:5:1\",\"root_ar\":\"ج ع ل\",\"surface_ar\":\"جَعَلَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:3:adjective-binding","source_type":"word_analysis","support_id":"sup_577aa20f4af5c32c1bfc","text":"{\"blocking_evidence\":null,\"headline\":\"residue noun receives the final color\",\"reader_payoff\":\"The reader sees the color as attached to the refuse-state, while the possible circumstantial hearing keeps the transformed object in view.\",\"reason\":\"Attachment evidence strongly licenses {{ar:أَحْوَىٰ}} ({{tr:aḥwā}}) as an adjective qualifying {{ar:غُثَآءً}} ({{tr:ghuthāʾan}}); the circumstantial possibility is retained only as secondary pressure.\",\"representative_source_ids\":[\"QG-6f5d7fe3\",\"QG-dac09332\",\"QT-c69bec4f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:5:2:1","source_type":"qac_morpheme","support_id":"sup_58700b2606492a1dc176","text":"{\"lemma_ar\":\"غُثَآء\",\"morph_features\":\"STEM|POS:N|LEM:guvaA^'|ROOT:gvw|M|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"87:5:2:1\",\"qac_word_ref\":\"87:5:2\",\"root_ar\":\"غ ث و\",\"surface_ar\":\"غُثَآءً\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:4:sifa-hal-tension","source_type":"word_analysis","support_id":"sup_5bea12eccafb5bf1ed2a","text":"{\"blocking_evidence\":null,\"headline\":\"color can also press toward the transformed object\",\"reader_payoff\":\"The reader can feel the color attached to both the named refuse and the pasture at the moment of transformation, while the adjective attachment remains primary.\",\"reason\":\"The local attachment favors adjective-to-noun agreement, so the circumstantial reading is preserved as secondary pressure rather than the governing parse.\",\"representative_source_ids\":[\"QG-5bf85d46\",\"QG-b8e00c10\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:3:mass-concrete-substance","source_type":"word_analysis","support_id":"sup_6e63ad84486d7453e50a","text":"{\"blocking_evidence\":null,\"headline\":\"mass substance rather than process\",\"reader_payoff\":\"The reader sees the process frozen as a collective matter-state, not counted plants or an ongoing verbal action.\",\"reason\":\"The local form is a concrete singular indefinite noun in the result slot, supporting the mass-category reading.\",\"representative_source_ids\":[\"QF-166408fb\",\"QF-38f097f5\",\"QF-3ae00fd2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:4:substance-quality-sound-link","source_type":"word_analysis","support_id":"sup_703663f534644444ce8b","text":"{\"blocking_evidence\":null,\"headline\":\"open sound links residue and color\",\"reader_payoff\":\"The reader hears the residue noun and color adjective bound into one closing image by their broad open sound.\",\"reason\":\"The sound link follows the actual phrase sequence from {{ar:غُثَآءً}} ({{tr:ghuthāʾan}}) to {{ar:أَحْوَىٰ}} ({{tr:aḥwā}}).\",\"representative_source_ids\":[\"QE-5e6c7cee\",\"QP-df7ef3d3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:4:next-ayah-cadence","source_type":"word_analysis","support_id":"sup_72112d61bb7d5ad66599","text":"{\"blocking_evidence\":null,\"headline\":\"final cadence carries into the next assurance\",\"reader_payoff\":\"The reader notices that the dark visual endpoint does not fully close the surah's motion; its final cadence carries into the next fa-linked assurance.\",\"reason\":\"The row gives a boundary-cadence observation tied to the final sound of 87:5 and the following fa-linked movement; it is preserved as sound continuity, not as a syntactic claim.\",\"representative_source_ids\":[\"QB-833e3a0e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:2:boundary-arguments","source_type":"word_analysis","support_id":"sup_721b8f996de376b102d5","text":"{\"blocking_evidence\":null,\"headline\":\"agent and object cross the boundary\",\"reader_payoff\":\"The reader sees that 87:5 depends on the previous descriptive chain for both the acting subject and the transformed object.\",\"reason\":\"The verb has an implicit third-person masculine subject from the prior relative chain and a distinct attached object suffix, so the two masculine singular slots are not conflated.\",\"representative_source_ids\":[\"QG-9d4f6470\",\"QG-ade6380a\",\"QG-e424f148\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:3:indefinite-result-complement","source_type":"word_analysis","support_id":"sup_7ee61b0e925e1e6c9cb7","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite accusative result state\",\"reader_payoff\":\"The reader notices that the known pasture is grammatically rendered into an indefinite class of residue.\",\"reason\":\"QAC and attachment evidence mark {{ar:غُثَآءً}} ({{tr:ghuthāʾan}}) as an indefinite accusative result complement governed by {{ar:جَعَلَهُۥ}} ({{tr:jaʿalahū}}).\",\"representative_source_ids\":[\"QG-42c42955\",\"QG-b8b556e4\",\"MG-f0eb8f43\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:1","source_type":"word_analysis","support_id":"sup_7fca4e8f6edd6cc222cd","text":"{\"gloss_range\":\"resultive and sequential connector binding the new clause to the prior pasture-emergence\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) makes 87:5 arrive as the immediate consequence of the pasture brought forth in 87:4, not as a detached note about decay. The particle is analytically small but functionally wide: it scopes over the conversion clause, keeps the new perfect act inside the same implicit divine subject-chain, and turns the first sound of the ayah into the hinge from provision to reduction. Because it is attached in the written-recited bundle with {{ar:جَعَلَهُۥ}} ({{tr:jaʿalahū}}), the linkage is heard inside the act of making itself: the same pasture is crossed from emergence into residue without a narrative gap.\",\"root_display\":\"no root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:3:phrase-cadence-to-color","source_type":"word_analysis","support_id":"sup_839f4d43251ad00df574","text":"{\"blocking_evidence\":null,\"headline\":\"residue resolves into final color cadence\",\"reader_payoff\":\"The reader hears the rough residue noun move into the open final color, binding debris and appearance into one closing phrase.\",\"reason\":\"The observation follows the local sequence from {{ar:غُثَآءً}} ({{tr:ghuthāʾan}}) into {{ar:أَحْوَىٰ}} ({{tr:aḥwā}}).\",\"representative_source_ids\":[\"QP-85ed55ea\",\"QP-f00d034d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:2:state-setting-root-pressure","source_type":"word_analysis","support_id":"sup_86dcf0b756e53f6320f8","text":"{\"blocking_evidence\":null,\"headline\":\"making and assignment pressure narrows to rendering\",\"reader_payoff\":\"The reader feels the pasture being assigned a degraded state, while local grammar keeps the selected sense to direct rendering.\",\"reason\":\"V4 supports making and state-rendering branches, but auxiliary beginning, naming, reward, and nominal side branches are not licensed by the local pronoun-plus-result frame.\",\"representative_source_ids\":[\"QS-13c0d1e6\",\"QS-af7992c8\",\"MS-d8f4dc6e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:2:form-i-directness","source_type":"word_analysis","support_id":"sup_8a581d393c0a492086ba","text":"{\"blocking_evidence\":null,\"headline\":\"Form I directness over marked extensions\",\"reader_payoff\":\"The reader notices that the surface form gives a single direct rendering, not a marked causative or intensified repetition.\",\"reason\":\"The aligned form is perfect Form I; the contrast with other possible derived forms is useful only as form pressure, not as alternate local morphology.\",\"representative_source_ids\":[\"QF-eeda793f\",\"QF-ef306dc6\",\"QF-9751abd8\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:4:black-green-color-range","source_type":"word_analysis","support_id":"sup_8ce162793284494ccb82","text":"{\"blocking_evidence\":null,\"headline\":\"dark color holds greenness and decay\",\"reader_payoff\":\"The reader sees a precise liminal color where intense greenness and withered darkness can overlap.\",\"reason\":\"V4 supports the dark, black-green, and reddish-brown color branch for this root, and the local form is a color adjective.\",\"representative_source_ids\":[\"QS-46c33ff6\",\"QS-ac96cccd\",\"MS-d13a3477\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:4:visual-endpoint","source_type":"word_analysis","support_id":"sup_8dd2d744b237d189d3ba","text":"{\"blocking_evidence\":null,\"headline\":\"conversion sequence ends in visible color\",\"reader_payoff\":\"The reader experiences the clause moving from conversion to matter to visible darkening.\",\"reason\":\"The clause's local order places the adjective after the result noun as the last perceptible sign.\",\"representative_source_ids\":[\"QT-1ee7d4aa\",\"QT-2ab43d06\",\"MT-d434d145\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:3:verb-result-formula","source_type":"word_analysis","support_id":"sup_910eb0802d3a245970ce","text":"{\"blocking_evidence\":null,\"headline\":\"compact making-refuse formula\",\"reader_payoff\":\"The reader notices that the verb-result combination has echo-pressure as a compact making-refuse formula, especially through 23:41.\",\"reason\":\"The local pairing with {{ar:جَعَلَهُۥ}} ({{tr:jaʿalahū}}) is syntactically forced, and the supplied echo evidence supports formula pressure without importing the other scene's details.\",\"representative_source_ids\":[\"QE-62292395\",\"QE-e4313f8d\",\"QI-f7b5dd48\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:1:lifecycle-hinge","source_type":"word_analysis","support_id":"sup_a562d4776bceacdc85b6","text":"{\"blocking_evidence\":null,\"headline\":\"growth and exhaustion read together\",\"reader_payoff\":\"The reader feels the particle turn emergence and exhaustion into paired stages of one governed lifecycle.\",\"reason\":\"The sequence and result values are locally coherent because the object resumed from 87:4 is the same object transformed in 87:5.\",\"representative_source_ids\":[\"QS-db7a7d6a\",\"QS-f8b81924\",\"QT-06610efd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:3:material-endpoint-structure","source_type":"word_analysis","support_id":"sup_b86de70dc5827990fd1a","text":"{\"blocking_evidence\":null,\"headline\":\"middle beat turns action into tableau\",\"reader_payoff\":\"The reader sees the noun as the clause's material center between conversion verb and final color.\",\"reason\":\"The clause architecture places {{ar:غُثَآءً}} ({{tr:ghuthāʾan}}) after the conversion verb and before the adjective, making it the material endpoint that the color specifies.\",\"representative_source_ids\":[\"QT-36761fe9\",\"MT-b012c648\",\"QY-b9e8d69f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:3:marked-rare-choice","source_type":"word_analysis","support_id":"sup_beaad6b8bc8a51f1d549","text":"{\"blocking_evidence\":null,\"headline\":\"rare noun sharper than ordinary plant death\",\"reader_payoff\":\"The reader notices that the ayah chooses a marked residue word rather than ordinary withering vocabulary.\",\"reason\":\"The low-occurrence profile supports the CRITICAL rarity claim as marked diction, not as a new independent meaning.\",\"representative_source_ids\":[\"QI-3f700abf\",\"MH-e50725f4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:2:intertextual-life-refuse-contrast","source_type":"word_analysis","support_id":"sup_c3eafc19fb6dfdd0ccec","text":"{\"blocking_evidence\":null,\"headline\":\"same root links life elsewhere and residue here\",\"reader_payoff\":\"The reader notices that the common rendering root can link water to life in 21:30 but here links pasture to refuse, sharpening the reversal.\",\"reason\":\"The concrete references are valid as contrast and echo, but they do not change the local result-complement parse of {{ar:جَعَلَهُۥ}} ({{tr:jaʿalahū}}).\",\"representative_source_ids\":[\"QI-a93ed4de\",\"MI-a1830ebc\",\"QI-7ccdfefc\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:4:rare-final-color-choice","source_type":"word_analysis","support_id":"sup_cfa66aa76754415671ce","text":"{\"blocking_evidence\":null,\"headline\":\"rare exact color adjective\",\"reader_payoff\":\"The reader notices that the final color choice is marked and more precise than generic darkness or dryness.\",\"reason\":\"The contextual profile marks the exact adjective deployment as low-occurrence, supporting the CRITICAL claim of marked final precision.\",\"representative_source_ids\":[\"QI-25cface5\",\"QH-1e1fde0e\",\"MH-f6778be2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:2:conversion-frame-engine","source_type":"word_analysis","support_id":"sup_d5335a15a712122f5d4b","text":"{\"blocking_evidence\":null,\"headline\":\"verb organizes the three-step frame\",\"reader_payoff\":\"The reader sees the verb as the hinge that carries the clause from connector to substance to color.\",\"reason\":\"The local clause runs from {{ar:فَ}} ({{tr:fa}}) to the conversion verb, then to the result noun and color adjective, so the verb governs the conversion architecture.\",\"representative_source_ids\":[\"QT-2314e2e0\",\"QT-7710a7c3\",\"QY-da1ce72f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:4:form-color-state","source_type":"word_analysis","support_id":"sup_d6f83305f894de56baa0","text":"{\"blocking_evidence\":null,\"headline\":\"color-state form closes the clause\",\"reader_payoff\":\"The reader sees the ayah stop at a visible quality rather than introducing another action.\",\"reason\":\"The aligned word is an accusative qualitative adjective; the final long spelling masks audible case, so parsing comes from agreement, sequence, and attachment.\",\"representative_source_ids\":[\"QF-f407f9ea\",\"MF-10ed880d\",\"QF-f816fa4c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:4:open-final-cadence","source_type":"word_analysis","support_id":"sup_dee4d75cce99a84b683c","text":"{\"blocking_evidence\":null,\"headline\":\"open final sound lets the color linger\",\"reader_payoff\":\"The reader hears the dark afterstate linger through the open final cadence after the rough residue noun.\",\"reason\":\"The cadence observation is grounded in the final long sound of {{ar:أَحْوَىٰ}} ({{tr:aḥwā}}) and its position after {{ar:غُثَآءً}} ({{tr:ghuthāʾan}}).\",\"representative_source_ids\":[\"QF-60a2f210\",\"QP-09475e8e\",\"MP-c21f48b5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:4:adjective-attachment","source_type":"word_analysis","support_id":"sup_e211cbc8d26dd93a74bc","text":"{\"blocking_evidence\":null,\"headline\":\"final adjective colors the residue\",\"reader_payoff\":\"The reader notices that the final word qualifies the refuse-state itself, so the clause ends on appearance after material reduction.\",\"reason\":\"Attachment evidence strongly licenses {{ar:أَحْوَىٰ}} ({{tr:aḥwā}}) as the adjective qualifying {{ar:غُثَآءً}} ({{tr:ghuthāʾan}}).\",\"representative_source_ids\":[\"QG-af8f9ed1\",\"MG-cd9fed8d\",\"QT-c065c355\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:1:relative-chain-coordination","source_type":"word_analysis","support_id":"sup_e5a72f1a2d50a98b0673","text":"{\"blocking_evidence\":null,\"headline\":\"same subject and chain continue\",\"reader_payoff\":\"The reader notices that the ayah remains inside the same descriptive chain of divine action across the verse boundary.\",\"reason\":\"The verb's implicit third-person subject continues the prior relative chain, so the connector coordinates another act under the same recoverable agent.\",\"representative_source_ids\":[\"QG-5ce9a265\",\"QT-b4046b0c\",\"QB-4e3691ad\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:4","source_type":"word_analysis","support_id":"sup_e964a413e2c861dbf77a","text":"{\"gloss_range\":\"final accusative color adjective qualifying the residue as dark, dusky, black-green, or visibly withered\",\"prose\":\"{{ar:أَحْوَىٰ}} ({{tr:aḥwā}}) closes the clause by making the refuse visible. Agreement binds it to {{ar:غُثَآءً}} ({{tr:ghuthāʾan}}), so the ayah does not stop at residue in the abstract; it ends on a dark, dusky, black-green afterstate, while the secondary circumstantial pressure lets that color touch the pasture at the moment of transformation too. The color range lets greenness and blackening overlap, compressing vitality and decay into one final perception, and the darkening feels like a completed visible trace rather than a static label alone. The broader {{ar:ح و ي}} ({{tr:ḥ-w-y}}) field of gathering or containing does not replace the color sense, but it can resonate with compacted organic matter; the containment context in 6:146 sharpens this as contrast, because 87:5 turns the root-field toward surface color. Form and position matter too: the color adjective comes after the result noun, has a rare exact deployment here, and ends with an open long final sound that links back to the residue phrase, lets the darkened afterstate linger, and carries cadence into the following fa-linked assurance.\",\"root_display\":\"{{ar:ح و ي}} ({{tr:ḥ-w-y}})\",\"root_gloss_range\":\"gathering and containing, coiling, inward folds, dwellings, water catchments, plants, sickness, and dark reddish or black-green coloring; the local adjective selects the color branch while containment pressure survives only as compacted-residue resonance\",\"surface_display\":\"{{ar:أَحْوَىٰ}} ({{tr:aḥwā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:2:completed-rendering","source_type":"word_analysis","support_id":"sup_f15794cda4f214918e0c","text":"{\"blocking_evidence\":null,\"headline\":\"completed act of conversion\",\"reader_payoff\":\"The reader notices that the transformation is presented as decisive divine rendering rather than slow natural drift.\",\"reason\":\"QAC and verb-instance evidence mark a perfect Form I verb governing an object pronoun and result complement, matching the CRITICAL completed-rendering claim.\",\"representative_source_ids\":[\"QG-6c3a4420\",\"QF-ef306dc6\",\"MF-04a5f333\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:2:result-valency","source_type":"word_analysis","support_id":"sup_f3622865cd1330a98269","text":"{\"blocking_evidence\":null,\"headline\":\"object plus result complement enact transformation\",\"reader_payoff\":\"The reader notices that the clause's grammar itself requires a new state for the known object.\",\"reason\":\"Attachment evidence marks {{ar:غُثَآءً}} ({{tr:ghuthāʾan}}) as the accusative result complement or second object governed by {{ar:جَعَلَهُۥ}} ({{tr:jaʿalahū}}).\",\"representative_source_ids\":[\"QG-a47410e0\",\"QG-c3ab2502\",\"MG-e64331cf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:2:made-refuse-pairing","source_type":"word_analysis","support_id":"sup_f3b369b7753e4ad942de","text":"{\"blocking_evidence\":null,\"headline\":\"making-refuse pairing echoes 23:41\",\"reader_payoff\":\"The reader hears the verb answered immediately by the residue noun and resonating with another made-refuse context (23:41).\",\"reason\":\"The local verb-result pairing is syntactically forced, and the supplied 23:41 evidence supports an echo without importing that narrative into the local parse.\",\"representative_source_ids\":[\"QE-3058e7c0\",\"QE-ee947e6d\",\"QI-7ccdfefc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:1:resultive-sequel","source_type":"word_analysis","support_id":"sup_f6a8902fb5ce1cce2e6f","text":"{\"blocking_evidence\":null,\"headline\":\"resultive sequel to the prior pasture\",\"reader_payoff\":\"The reader notices that the reduction clause follows as a tight consequence of the pasture's emergence, not as an independent ecological observation.\",\"reason\":\"QAC identifies the segmented connector, and the clause evidence supports a single verbal predicate whose object continues from the prior pasture scene.\",\"representative_source_ids\":[\"QG-371c4459\",\"QG-f55632f6\",\"MG-c353a4eb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:5:2:boundary-lifecycle-reversal","source_type":"word_analysis","support_id":"sup_ffd08b7040b55152d67f","text":"{\"blocking_evidence\":null,\"headline\":\"same object enters the afterstate scene\",\"reader_payoff\":\"The reader sees lifecycle reversal as one continuous operation on the same object, not a switch to a new scene-object.\",\"reason\":\"The object suffix resolves across the ayah boundary, so the pasture's semantic role shifts from produced provision to patient of conversion.\",\"representative_source_ids\":[\"QS-e2572c68\",\"QB-13974002\",\"QB-6834c01a\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ","ayah_ref":"87:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000248/B002","root_000374/B006","root_001073/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000248","role":"Turning something into a state makes the verb the causal hinge of the transformation.","root":"ج ع ل","source_ref":"87:5","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001073","role":"Pasture dried into chaff-like refuse supplies both the prior vegetal state and its spoiled result.","root":"غ ث و","source_ref":"87:5","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_000374","role":"Blackish or dark-greenish coloring makes darkness the visible finish of the reduction.","root":"ح و ي","source_ref":"87:5","source_word_indices":["3"]}],"changed_reading":{"after":"He caused it to pass from growth into dry, spoiled refuse whose darkened color exposes the completed change.","before":"He made it dark chaff."},"confidence":"strong","focus_anchor":"The resultative construction joins جَعَلَ to غُثَاءً أَحْوَىٰ as a caused state.","mechanism":"A referent is made to cross into the state of pasture reduced to dry refuse, with dark coloration registering the completed material change.","model_id":"base_resultative_decay"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_resultative_decay","source_type":"hft","support_id":"sup_3f4b01b22ddbd600757d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ","ayah_ref":"87:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000248/B002","root_000374/B001","root_000374/B008","root_001073/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000248","role":"Caused state-change links the original referent to a newly aggregated material condition.","root":"ج ع ل","source_ref":"87:5","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001073","role":"Floating refuse carried by floodwater supplies mobility, surface position, and heterogeneous accumulation.","root":"غ ث و","source_ref":"87:5","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000374","role":"Gathering and holding turns the color word's root into an exploratory image of debris collected into one mass.","root":"ح و ي","source_ref":"87:5","source_word_indices":["3"]},{"branch_id":"B008","mapped_root_id":"root_000374","role":"Enclosed catchments that retain floodwater provide a possible spatial endpoint for the floating debris.","root":"ح و ي","source_ref":"87:5","source_word_indices":["3"]}],"changed_reading":{"after":"The referent becomes flood-mobile refuse that gathers, darkens, and lodges as a contained surface mass.","before":"The referent simply dries into dark chaff."},"confidence":"exploratory","focus_anchor":"غُثَاءً can be flood-borne surface refuse, while the root of أَحْوَىٰ also carries gathering, holding, and water-catchment images.","mechanism":"The product is not merely scattered dry matter: it can be imagined as mobile debris gathered by water and arrested in a dark mass or holding place.","model_id":"base_fluvial_aggregation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_fluvial_aggregation","source_type":"hft","support_id":"sup_ea7f41da09281fecc31c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ","ayah_ref":"87:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000248/B002","root_000374/B006","root_001073/B004"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000248","role":"Turning something into a state supports a change of status as well as substance.","root":"ج ع ل","source_ref":"87:5","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_001073","role":"Unregarded refuse supplies the endpoint of devaluation: material present but no longer taken into account.","root":"غ ث و","source_ref":"87:5","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_000374","role":"Dark coloration gives the loss of standing a concrete visible surface.","root":"ح و ي","source_ref":"87:5","source_word_indices":["3"]}],"changed_reading":{"after":"The line enacts a collapse of standing: the transformed material remains visible but is recategorized as something not worth counting.","before":"The line reports physical decay."},"confidence":"medium","focus_anchor":"The result noun غُثَاءً includes refuse that is not counted or valued.","mechanism":"The caused change is simultaneously material and classificatory: what had a prior identity is reassigned to the category of negligible remainder.","model_id":"base_value_collapse"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_value_collapse","source_type":"hft","support_id":"sup_1b557f13d09d6802a6ae","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ","ayah_ref":"87:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000248/B002","root_000374/B003","root_001073/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000248","role":"Caused state-change gives the cross-domain image a single transformation frame.","root":"ج ع ل","source_ref":"87:5","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001073","role":"A stomach or soul churning with nausea supplies visceral recoil from the product.","root":"غ ث و","source_ref":"87:5","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000374","role":"Inward intestinal coils locate the churning inside a containing body.","root":"ح و ي","source_ref":"87:5","source_word_indices":["3"]}],"changed_reading":{"after":"The same refuse can be felt from inside as a nauseating, gut-coiling encounter with corruption.","before":"The transformation is viewed from outside as a dark landscape."},"confidence":"exploratory","containment":"This is surprising because it crosses from landscape waste into bodily nausea and intestinal coils. It remains anchored in the two adjacent focus roots and their packet branches, but downstream prose should present it only as a somatic echo of revulsion and inward churning, not as a claim that the syntax literally denotes intestines.","focus_anchor":"The adjacent words غُثَاءً أَحْوَىٰ activate nausea in the first root inventory and inward coils in the second.","outlier_id":"outlier_visceral_ecology"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier_visceral_ecology","source_type":"hft","support_id":"sup_33053778a4e67dd75312","trust":"legacy_unbound"}]}
</lane_packet_json>
