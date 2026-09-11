# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **87:13**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s087-regular-20260911/s087/87_13/micro.discovery.json` and modify nothing
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
  "ayah_ref": "87:13",
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
{"analysis_context":{"analysis_id":"s087-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"87:13","host_surah":87,"lane_context_refs":[],"ordered_context_refs":["87:0","87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:14","87:15","87:16","87:17","87:18","87:19","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, yaşam durumunu ve onu başlatma ya da sürdürme işlemini kapsar; yağmur, karşılama sözü, utanma ve başka özel türevler ayrı dallarda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000383/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","surface_ar":"يَحْيَىٰ"}],"gloss":"canlı olma, sürüp gitme ve canlandırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığın ölü olmayıp canlı bulunması ve yaşamını sürdürmesi temel anlamdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Canlı kılma veya ölümden sonra yeniden canlandırma, temel durumun ettirgen ve yenileyici uzantısıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bitkisel büyüme, duyum, düşünme, dünya yaşamı, sonraki yaşam ve ölmez var oluş, canlılığın kaynakta ayrılan özel düzeyleridir."}}],"root_ar":"ح ي ي","root_id":"root_000383","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın durum, süreklilik ve canlı kılma işlemlerini birlikte anlatan en geniş doğal karşılıktır.","boundary_detail":"Dal, yaşam durumunu ve onu başlatma ya da sürdürme işlemini kapsar; yağmur, karşılama sözü, utanma ve başka özel türevler ayrı dallarda kalır.","branch_image_ar":"الحياة في مقابل الموت","concept_gloss":"canlı olma, sürüp gitme ve canlandırma","contextual_glosses":[{"applicability":"Bir varlığın ölmeden yaşamını sürdürdüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Canlandırma işlemini ve yaşamın özel düzeylerini kapsamaz.","preserves":"Canlı olma ve yaşamı sürdürme durumunu doğal bir yüklemle verir."},"facet_ids":["F001"],"text":"canlı kaldı","usage_role":"contextual"},{"applicability":"Ölmüş ya da sönmüş sayılan bir varlığın yeniden canlı duruma getirildiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kendiliğinden canlı olma ve yaşamı sürdürme durumlarını kapsamaz.","preserves":"Canlılığın yeniden kazandırılması işlemini açıkça korur."},"facet_ids":["F002"],"text":"yeniden canlandırdı","usage_role":"contextual"}],"definition":"Ölümün karşıtı olarak canlı olma ve canlı kalma durumudur; bir varlığı canlı kılma ya da yeniden canlandırma işlemini de kapsar. Bitkisel, duyusal ve düşünsel yaşam ile dünyadaki, sonraki ve ölmez var oluş bu çekirdeğin farklı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığın ölü olmayıp canlı bulunması ve yaşamını sürdürmesi temel anlamdır."},{"facet_id":"F002","role":"extension","statement":"Canlı kılma veya ölümden sonra yeniden canlandırma, temel durumun ettirgen ve yenileyici uzantısıdır."},{"facet_id":"F003","role":"specialization","statement":"Bitkisel büyüme, duyum, düşünme, dünya yaşamı, sonraki yaşam ve ölmez var oluş, canlılığın kaynakta ayrılan özel düzeyleridir."}],"identity_rationale":"Kaynak ifadesi bu dalı ölümün karşıtı olan canlılık durumu etrafında kurar; canlı kalmayı, yaşamın farklı güç ve düzeylerini, yeniden canlandırmayı ve ölümün düşünülemediği sürekli var oluşu da bu çekirdeğe bağlar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yaşam"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"canlı; ölmesi düşünülemeyen varlık"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"canlı oldu ya da canlı kaldı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"canlandırdı ya da yeniden yaşama döndürdü"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yaşam"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bitmeyen gerçek yaşam"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"ateşi üfleyerek canlandırdı"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"çocuğu yaşatan besin"}],"lexicalization_note":"Temel yaşam ve canlı olma anlamlarıyla, canlı kalma, canlandırma ve özel türevlerde beliren kullanımlar birbirinden ayrılarak tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; canlı varlık, sağ bırakma ve koruyucu yarar dalları okuyucunun en kolay karıştırabileceği üç sınırı gösterdiği için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bir durum, güç ve işlem kümesini anlatır; komşu dal ise o durumu taşıyan varlığı sınıflandırır, bu yüzden bağlam içinde birbirlerinin yerine geçmezler.","focus_only":"Yaşam durumu, bu durumun sürmesi ve bir varlığın canlandırılması bu dala özgüdür.","gloss":"yaşam ile canlı varlık","neighbor_only":"Canlılığı taşıyan duyarlı ya da ruh sahibi varlığın kendisi komşu dalın odağıdır.","neighbor_ref":"root_000383/B003","relation_type":"near_neighbor","shared_zone":"İki dal da canlı olmayı ve ölüm karşıtlığını temel alır."},{"boundary_match":"partial","distinction":"Bu dal yaşamın kendisini ve canlandırmayı kapsar; komşu dal ise belirli bir kalıpta öldürmeme kararını bildirir.","focus_only":"Genel canlılık, yaşamın sürmesi ve canlı kılma işlemi bu dalda yer alır.","gloss":"yaşamak ile sağ bırakmak","neighbor_only":"Belirli kişileri öldürmeyip sağ bırakma anlamı yalnız komşu yapıya bağlıdır.","neighbor_ref":"root_000383/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir canlının ölmemesi sonucu bulunur."},{"boundary_match":"partial","distinction":"Bu dal gerçek canlılık alanındadır; komşu dal yaşam sözünü yarar, iyilik ve koruyucu sonuç için kullanır.","focus_only":"Canlılık durumu ve onu meydana getirme bu dalın çekirdeğidir.","gloss":"yaşam ile koruyucu yarar","neighbor_only":"Yarar, caydırma ve yok olmaktan kurtarma üzerinden kurulan mecazlı değer komşu dala özgüdür.","neighbor_ref":"root_000383/B013","relation_type":"near_neighbor","shared_zone":"İki dal yaşamın korunması ve ölümden uzak kalma sonucunda kesişir."}],"source_phrase_ar":"خلاف الموت (maqayis); الحياة ضد الموت والحي ضد الميت (jamhara;sihah); يقال حيي يحيا فهو حي (ayn;tahdhib); الحياة تستعمل للقوة النامية والحساسة والعاقلة والأخروية والباري حي (mufradat)","source_summary":"Kaynaklar ölüm karşıtı canlılık çekirdeğinde birleşir; toplu tanıklık ayrıca yaşamın güçlerini, sürekliliğini ve yeniden canlandırmayı bu çekirdeğin kapsamına alır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه كون الشيء حيا، والحياة والبقاء، والإحياء بعد موت، والحياة الدنيا والآخرة، ووصف الحي الذي لا يموت.","what_is_not_ar":"لا يختص بالمطر أو التحية أو الحياء الخلقي إلا من جهة الاشتقاق العام."},"support_links":[]},{"boundary":"Dal insanın genel yaşamını değil, yağmurun toprağa, bitkiye ve geçime getirdiği canlılık ile buna bağlı kalıpları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000383/B002","candidate_links":[{"candidate_id":"cand_780eeea0b117a8fdca01","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","surface_ar":"يَحْيَىٰ"}],"gloss":"yağmurla gelen toprak canlılığı ve bolluk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yağmur, toprağa canlılık verdiği ve onu ölüm görünümünden çıkardığı için bu adla anılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Verimli toprak ile taze ve hareketli bitki, yağmurun yaşatıcı etkisinin görünür sonuçlarıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Toprağı verimli bulmak veya bir topluluğun yağmur ve bol ota kavuşması yalnız belirli yapılarda anlatılır."}}],"root_ar":"ح ي ي","root_id":"root_000383","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yağmurun kendisini, toprağı canlandıran etkisini ve verim sonucunu birlikte anlatır.","boundary_detail":"Dal insanın genel yaşamını değil, yağmurun toprağa, bitkiye ve geçime getirdiği canlılık ile buna bağlı kalıpları kapsar.","branch_image_ar":"حياة الأرض بالمطر والنبات","concept_gloss":"yağmurla gelen toprak canlılığı ve bolluk","contextual_glosses":[{"applicability":"Yağmurun yaşatıcı etkisinin açıkça anlatılması gereken bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toprağı verimli bulma ve topluluğun bol ota kavuşması gibi yapıya bağlı kullanımları kapsamaz.","preserves":"Yağmur ile toprağın canlanması arasındaki neden bağını korur."},"facet_ids":["F001","F002"],"text":"toprağı canlandıran yağmur","usage_role":"explanatory"}],"definition":"Yağmurun toprağı canlandırması, verim ve taze bitki meydana getirmesidir; yağmurun kendisi de bu yaşatıcı etkiden ötürü adlandırılır. Toprağı bu durumda bulmak ve bir topluluğun yağmurla bol ota kavuşması yapıya bağlı uzantılardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yağmur, toprağa canlılık verdiği ve onu ölüm görünümünden çıkardığı için bu adla anılır."},{"facet_id":"F002","role":"specialization","statement":"Verimli toprak ile taze ve hareketli bitki, yağmurun yaşatıcı etkisinin görünür sonuçlarıdır."},{"facet_id":"F003","role":"associated_use","statement":"Toprağı verimli bulmak veya bir topluluğun yağmur ve bol ota kavuşması yalnız belirli yapılarda anlatılır."}],"identity_rationale":"Kaynak ifadesi yağmuru toprağı yaşatan neden olarak adlandırır ve bu anlamı verimli toprak, taze bitki, yağmura kavuşan topluluk ve otlanan hayvanlarla somutlaştırır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"toprağı canlandıran yağmur ve bolluk"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"toprağı bitkili ve verimli buldum"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"topluluk yağmura ve bol ota kavuştu"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"körpe ve canlı bitki"}],"lexicalization_note":"Yağmur ve toprak canlılığına ilişkin temel adlandırma, toprağı verimli bulma ve bir topluluğun yağmurla ota kavuşması gibi yapıya bağlı kullanımlardan ayrı tutulur.","neighbor_coverage_note":"Bütün yağmur, toprak ve bitki adayları değerlendirildi; karşıt kuraklık ile bahar ve bitki çıkışı sınırları en açıklayıcı üç karşılaştırma olarak seçildi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu dal yağmurla canlanan ve ürün veren toprağı anlatırken komşu dal yağışsızlık, otsuzluk ve verimsizlik durumunu anlatır.","focus_only":"Yağmurun getirdiği toprak canlılığı, verim ve taze bitki bu dalda bulunur.","gloss":"verim ile kuraklık","neighbor_only":"Yağmurun, otun ve verimin yokluğu komşu dalın belirleyici durumudur.","neighbor_ref":"root_000258/B002","relation_type":"antonym","shared_zone":"İki dal toprağın yağmur ve bitki bakımından durumunu karşıt uçlarda ele alır."},{"boundary_match":"partial","distinction":"Bu dal etkiyi yağmurun toprağı canlandırmasına bağlar; komşu dal aynı görünümü mevsim, otlak ve dönemsel üretim çerçevesinde kurar.","focus_only":"Yağmurun yaşatıcı etkisi ve bundan doğan toprak canlılığı bu dalın çekirdeğidir.","gloss":"yaşatıcı yağmur ile bahar bolluğu","neighbor_only":"Yılın belirli mevsimi, o mevsimde otlama ve ürün verme komşu dalın kapsamındadır.","neighbor_ref":"root_000536/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal yağmur, yeşerme, ot ve bolluk görünümünde kesişir."},{"boundary_match":"partial","distinction":"Bu dal yağmuru ve verimli sonucu adlandırır; komşu dal bitkinin çıkış ve büyüme sürecini adlandırır.","focus_only":"Yağmur ve onun toprağa verdiği canlılık bu dalda belirleyicidir.","gloss":"toprağın canlanması ile bitkinin çıkması","neighbor_only":"Bitkinin topraktan çıkması ve büyüme eylemi komşu dalın çekirdeğidir.","neighbor_ref":"root_001465/B001","relation_type":"near_neighbor","shared_zone":"İki dal taze bitki ve toprağın yeşermesi sonucunda buluşur."}],"source_phrase_ar":"يسمى المطر حيا لأن به حياة الأرض (maqayis); الحيا مقصور حيا الربيع وهو ما تحيا به الأرض من الغيث (ayn); أحيا القوم أي صاروا في الحيا وهو الخصب وأتيت الأرض فأحييتها أي وجدتها خصبة (sihah); الحي من النبات ما كان طريا يهتز والحيا الغيث (tahdhib); الحيا المطر لأنه يحيي الأرض بعد موتها (mufradat)","source_summary":"Kaynaklar yağmurun toprağı canlandırdığı konusunda birleşir; verim, taze bitki ve hayvanların otla güçlenmesi bu etkinin sonuçları olarak aktarılır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الحيا بمعنى المطر، وخصب الأرض، والنبات الطري، وإحياء الأرض أو إصابة القوم بالمطر والمرعى.","what_is_not_ar":"لا يضم مطلق الحياة الآدمية أو الأخروية إلا من جهة أن المطر سبب الحياة."},"support_links":["sup_cd95784aa9d134d8bfb8"]},{"boundary":"Ana okuma canlı varlıktır; bitmeyen gerçek yaşam kaynakta bulunan ayrı bir anlam değişkesi olarak tutulur, genel yaşam durumu ise B001'e bırakılır.","branch_kind":"bare","branch_ref":"root_000383/B003","candidate_links":[{"candidate_id":"cand_c253bb91ae6112790ccf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","surface_ar":"يَحْيَىٰ"}],"gloss":"canlı varlık veya bitmeyen gerçek yaşam","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ruh, duyum veya yaşam taşıyan her canlı varlık temel kapsamı oluşturur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bitmeyen gerçek yaşam okuması, canlı varlık adından ayrılması gereken ikinci bir kaynak kullanımıdır."}}],"root_ar":"ح ي ي","root_id":"root_000383","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakta aynı biçime bağlanan iki ayrı okumayı birleştirmeden gösteren kapsayıcı karşılıktır.","boundary_detail":"Ana okuma canlı varlıktır; bitmeyen gerçek yaşam kaynakta bulunan ayrı bir anlam değişkesi olarak tutulur, genel yaşam durumu ise B001'e bırakılır.","branch_image_ar":"ذو الروح والحيوان","concept_gloss":"canlı varlık veya bitmeyen gerçek yaşam","contextual_glosses":[{"applicability":"Ruh, duyum veya canlılık taşıyan bir varlıktan söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bitmeyen gerçek yaşam biçimindeki kaynak değişkesini kapsamaz.","preserves":"Dalın baskın canlı varlık okumasını eksiksiz verir."},"facet_ids":["F001"],"text":"canlı varlık","usage_role":"general"},{"applicability":"Biçimin kalıcı ve yok olmayan yaşamı anlattığı özel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Canlı varlık sınıfını bildiren ana okumayı kapsamaz.","preserves":"Kalıcı yaşam değişkesini açıkça korur."},"facet_ids":["F002"],"text":"bitmeyen gerçek yaşam","usage_role":"contextual"}],"definition":"Ruh, duyum veya canlılık taşıyan varlığı anlatır ve ölü cansız varlığın karşısında durur. Aynı biçim kaynakta ayrıca bitmeyen gerçek yaşam için kullanıldığından bu ikinci okuma ayrı tutulmalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ruh, duyum veya yaşam taşıyan her canlı varlık temel kapsamı oluşturur."},{"facet_id":"F002","role":"source_variant","statement":"Bitmeyen gerçek yaşam okuması, canlı varlık adından ayrılması gereken ikinci bir kaynak kullanımıdır."}],"identity_rationale":"Kaynak ifadesinin baskın yönü ruh, duyum veya canlılık taşıyan varlıktır; ancak aynı ifade ayrıca bitmeyen gerçek yaşamı da ayrı bir kullanım olarak verir. Dal korunabilir, fakat varlık adı ile sonsuz yaşam okuması tek bir çekirdekmiş gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"canlı varlık, özellikle duyup hareket eden varlık"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bitmeyen gerçek yaşam"}],"lexicalization_note":"Temel biçimin canlı varlık anlamı tanımın merkezidir; aynı biçimin bitmeyen yaşam okuması bağımsız bir kaynak değişkesi olarak ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; canlıların alt sınıfı, bedeni yaşatan öz ve yılan türü üst sınıf-alt sınıf karışıklıklarını en iyi gösteren adaylardı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal canlı varlığı genel olarak adlandırır; komşu dal canlılar içinden ayırt etme yetisi bulunmayan belirli sınıfı öne çıkarır.","focus_only":"Ruh veya duyum taşıyan bütün canlı varlıklar ile bitmeyen yaşam değişkesi bu dalın geniş kapsamındadır.","gloss":"canlı varlık ile ayırt etmeyen canlı","neighbor_only":"Ayırt etme yetisi bulunmayan ve özellikle dört ayaklı canlı sınıfı komşu dalın daraltıcı özelliğidir.","neighbor_ref":"root_000160/B003","relation_type":"near_synonym","shared_zone":"İki dal da insan dışı canlıları kapsayabilen varlık adlarıdır."},{"boundary_match":"partial","distinction":"Bu dal canlı bireyi adlandırır; komşu dal o bireyin yaşam ilkesi sayılan özü adlandırır.","focus_only":"Canlılığı taşıyan bütün varlığın kendisi bu dalın odağıdır.","gloss":"canlı varlık ile yaşatan öz","neighbor_only":"Bedeni yaşattığı düşünülen öz ve onun bedenden çıkışı komşu dalın odağıdır.","neighbor_ref":"root_001533/B011","relation_type":"near_neighbor","shared_zone":"Her iki dal bedenin canlı olması ve ölümle ilişkisi çevresinde birleşir."},{"boundary_match":"partial","distinction":"Bu dal üst sınıfı anlatır; komşu dal o sınıf içindeki belirli canlı türünü adlandırır.","focus_only":"Her tür ruh veya duyum taşıyan canlı bu dalın kapsamına girebilir.","gloss":"canlı varlık ile yılan","neighbor_only":"Yılan türünün adı ve bu ada bağlı özel türevler komşu dala özgüdür.","neighbor_ref":"root_000383/B004","relation_type":"near_neighbor","shared_zone":"Yılan da canlı bir varlık olduğu için iki dalın gönderimleri kesişebilir."}],"source_phrase_ar":"الحيوان كل ذي روح (ayn); الحيوان خلاف الموتان (sihah); الحيوان اسم يقع على كل شيء حي وكل ذي روح حيوان (tahdhib); الحيوان مقر الحياة وما له الحاسة وما له البقاء الأبدي (mufradat)","source_summary":"Toplu tanıklık canlı varlık ve ölüm karşıtlığı üzerinde yoğunlaşır; aynı kaynak kümesi biçimi kalıcı gerçek yaşam için de kullandığından iki okuma bağlamla ayrılmalıdır.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الحيوان وكل ذي روح، والحية الأهلية في الحديث بمعنى كل نفس أو دابة، وما يقابل الموتان.","what_is_not_ar":"لا يضم الحية الثعبان كاسم جنس مستقل إلا إذا كان الكلام عن كونها دابة حية."},"support_links":["sup_d8c3c7ff070cd4abfbe1"]},{"boundary":"Dal yılan adlandırmasını korur; yaşamla türetme yalnız bir açıklamadır ve sarılma temelli karşı açıklama dışlanmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000383/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","surface_ar":"يَحْيَىٰ"}],"gloss":"yılan ve yılanla ilgili adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Genel yılan adı hem erkek hem dişi birey için kullanılabilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Erkek yılan için ayrı bir özel biçim kaynakta açıkça tanıklanır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yılan adının yaşamdan türetilmesi ile sarılıp kıvrılmadan türetilmesi birbirine rakip iki açıklamadır."}}],"root_ar":"ح ي ي","root_id":"root_000383","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel tür adını, erkek birey adını ve bu alandaki türevleri kapsayan doğal karşılıktır.","boundary_detail":"Dal yılan adlandırmasını korur; yaşamla türetme yalnız bir açıklamadır ve sarılma temelli karşı açıklama dışlanmaz.","branch_image_ar":"الحية من جنس الحياة","concept_gloss":"yılan ve yılanla ilgili adlandırmalar","contextual_glosses":[{"applicability":"Özel biçimin yılanın erkek bireyini gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Her iki cinsiyeti kapsayan genel tür adını ve köken tartışmasını kapsamaz.","preserves":"Cinsiyete bağlı özel adlandırmanın gönderimini korur."},"facet_ids":["F002"],"text":"erkek yılan","usage_role":"contextual"}],"definition":"Erkek veya dişi olabilen yılan için kullanılan genel addır; erkek yılan için ayrıca özel bir adlandırma bulunur. Adın yaşam düşüncesinden türediği açıklaması, sarılma düşüncesine dayanan karşı açıklamayla birlikte ve kesinleştirilmeden verilmelidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Genel yılan adı hem erkek hem dişi birey için kullanılabilir."},{"facet_id":"F002","role":"specialization","statement":"Erkek yılan için ayrı bir özel biçim kaynakta açıkça tanıklanır."},{"facet_id":"F003","role":"source_variant","statement":"Yılan adının yaşamdan türetilmesi ile sarılıp kıvrılmadan türetilmesi birbirine rakip iki açıklamadır."}],"identity_rationale":"Kaynak ifadesi erkek ve dişi için kullanılan genel yılan adını ve erkek yılan için özel biçimi açıkça destekler. Bununla birlikte adın yaşam kökünden mi yoksa sarılma düşüncesinden mi geldiği konusunda iki türetme bulunduğundan köken bağı kesinleştirilemez.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yılan"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"erkek yılan"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yılan bakıcısı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yılanlı toprak"}],"lexicalization_note":"Genel yılan adı çekirdekte tutulur; erkek yılan, yılan bakıcısı ve yılanlı yer gibi özel biçimler yalnız kendi sözcük sınırlarında yorumlanır.","neighbor_coverage_note":"Bütün yılan adları değerlendirildi; genel tür adıyla belirli yılan çeşitleri arasındaki sınırı en açık gösteren iki aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal genel tür adıdır; komşu dal yılanlar içinde belirli bir çeşide verilen addır ve genel karşılık olarak kullanılamaz.","focus_only":"Her iki cinsiyeti kapsayan genel yılan adı ve ona bağlı türevler bu dalın kapsamındadır.","gloss":"genel yılan ile özel yılan türü","neighbor_only":"Belirli bir yılan çeşidi, özellikle beyaz yılan okuması komşu dalın dar kapsamıdır.","neighbor_ref":"root_000266/B012","relation_type":"near_synonym","shared_zone":"Her iki dal doğrudan yılan türünden bir canlıyı adlandırır."},{"boundary_match":"partial","distinction":"Bu dal bütün yılanlara açık genel addır; komşu dal belirli görünüş veya nitelikteki yılanı adlandırır.","focus_only":"Boyut veya biçim sınırlaması olmadan genel yılan adı bu dala özgüdür.","gloss":"yılan ile iri özel yılan","neighbor_only":"İrilik, kötücüllük, kısalık veya yuvarlaklık gibi niteliklerle tanımlanan özel yılan komşu dala özgüdür.","neighbor_ref":"root_000038/B004","relation_type":"near_synonym","shared_zone":"Her iki dal yılanı doğrudan gönderim konusu yapar."}],"source_phrase_ar":"الحية معروف يقال حية ذكر وحية أنثى والحيوت ذكر الحيات (jamhara); الحية اشتقاقها من الحياة (ayn); الحية تكون للذكر والأنثى والحيوت ذكر الحيات (sihah); اشتقاق الحية من الحياة ومن قال حواء قال من حويت لأنها تتحوى (tahdhib)","source_summary":"Kaynaklar genel yılan adı ve erkek yılan için özel biçim üzerinde birleşir; köken açıklaması ise yaşam ile sarılıp kıvrılma arasında kesinleştirilemeyen bir ayrılık gösterir.","sources":["JA","AY","SI","TA"],"what_is_ar":"يدخل فيه الحية للذكر والأنثى، والحيوت ذكر الحيات، والنسبة والصاحب المتعامل مع الحيات عند من يشتقه من هذا الباب.","what_is_not_ar":"لا يضم تفسير الحية من حويت والالتواء إلا بوصفه اشتقاقا بديلا خارج هذا الفرع."},"support_links":[]},{"boundary":"Dal içsel utanma ve kötüden çekinmeyle sınırlıdır; öldürmeyip sağ bırakma anlamındaki benzer biçim bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000383/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","surface_ar":"يَحْيَىٰ"}],"gloss":"kötü olandan utanarak çekinme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kötü görülen şey karşısında duyulan içsel daralma ve utanma temel duygudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu duygu kişiyi kötü davranışı bırakmaya veya ondan uzak durmaya yöneltir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişiden veya onun karşısında yapılan bir şeyden utanma, duygunun katılımcısı belirtilmiş kullanım biçimidir."}}],"root_ar":"ح ي ي","root_id":"root_000383","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duyguyu ve bu duygunun davranışı durdurucu sonucunu birlikte veren temel karşılıktır.","boundary_detail":"Dal içsel utanma ve kötüden çekinmeyle sınırlıdır; öldürmeyip sağ bırakma anlamındaki benzer biçim bu dala girmez.","branch_image_ar":"الحياء وانقباض النفس","concept_gloss":"kötü olandan utanarak çekinme","contextual_glosses":[{"applicability":"Utanma duygusunun yöneldiği kişi veya neden açıkça belirtildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Duygunun kötü davranışı bırakmaya yönelten genel işlevini açıkça söylemez.","preserves":"Utanma duygusunu ve yöneldiği katılımcıyı doğal biçimde verir."},"facet_ids":["F001","F003"],"text":"ondan utandı","usage_role":"contextual"}],"definition":"Kişinin kötü, uygunsuz veya yüz kızartıcı gördüğü şey karşısında içten daralması ve bu nedenle ondan kaçınmasıdır; yüzsüzlüğün karşıtı olarak değerlendirilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kötü görülen şey karşısında duyulan içsel daralma ve utanma temel duygudur."},{"facet_id":"F002","role":"extension","statement":"Bu duygu kişiyi kötü davranışı bırakmaya veya ondan uzak durmaya yöneltir."},{"facet_id":"F003","role":"specialization","statement":"Bir kişiden veya onun karşısında yapılan bir şeyden utanma, duygunun katılımcısı belirtilmiş kullanım biçimidir."}],"identity_rationale":"Kaynak ifadesi utanmayı yüzsüzlüğün karşıtı olarak verir ve kişinin kötü görülen davranışlardan içsel bir daralma nedeniyle kaçınmasını temel anlam sayar.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"utanma ve kötü davranıştan çekinme"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ondan utandı ve çekindi"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ondan utandı ya da konuşmasına karşılık vermedi"}],"lexicalization_note":"Temel utanma adı ile bir kişiden veya davranıştan utanmayı bildiren yapılar ayrı dil bilgisel gerçekleşmeler olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dış adaylar anlam alanını kesmiyordu, benzer biçimli sağ bırakma dalı ise en güçlü yanlış anlamayı oluşturduğu için tek ayrım olarak yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal bir duygu ve davranışsal çekinme bildirir; komşu dal ise bir kişinin yaşamına son vermeme eylemini bildirir.","focus_only":"Kötü görülen şey karşısındaki içsel daralma ve davranıştan çekinme bu dala özgüdür.","gloss":"utanma ile sağ bırakma ayrımı","neighbor_only":"Birini öldürmeyip sağ bırakma kararı komşu dalın tek çekirdeğidir.","neighbor_ref":"root_000383/B006","relation_type":"other","shared_zone":"İki dal benzer sözcük yapılarıyla ifade edilir, fakat anlam çekirdekleri ortak değildir."}],"source_phrase_ar":"الاستحياء الذي هو ضد الوقاحة واستحييت منه (maqayis); حييت عن فلان إذا استحييت عنه (jamhara); حييت منه أحيا استحييت واستحياه واستحيا منه من الحياء (sihah); الحياء من الاستحياء ورجل حيي واستحيا الرجل (tahdhib); الحياء انقباض النفس عن القبائح وتركه (mufradat)","source_summary":"Kaynaklar utanmayı yüzsüzlüğün karşıtı, kötü davranış karşısındaki içsel daralma ve o davranışı bırakmaya yönelten duygu olarak birlikte tanımlar.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحياء، والاستحياء، وحييت منه أو من فعل، والانقباض عن القبائح، وترك القبيح في حق الله عند تفسير الصفة.","what_is_not_ar":"لا يضم الاستبقاء وترك القتل في مثل يستحيون نساءكم، ولا العضو المسمى حياء إلا من جهة التسمية."},"support_links":[]},{"boundary":"Tanım öldürmeyip sağ bırakma okumasını izler; karşıt yöndeki tek olumsuz aktarım kaynak içi uyuşmazlık olarak korunur.","branch_kind":"non_bare","branch_ref":"root_000383/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","surface_ar":"يَحْيَىٰ"}],"gloss":"öldürmeyip sağ bırakma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Öldürme imkânı veya tehdidi altında bulunan kişileri öldürmeyip canlı bırakmak temel işlemdir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kadınlar ve bir topluluğun gençleri kaynakta açıkça belirtilen kişi gruplarıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Toplu aktarımın bir bölümündeki karşıt olumsuzluk, baskın sağ bırakma açıklamasıyla uyuşmayan metinsel bir değişkedir."}}],"root_ar":"ح ي ي","root_id":"root_000383","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kişilerin yaşamına son verilmeyip korunması anlamındaki türemiş yapıya uygundur.","boundary_detail":"Tanım öldürmeyip sağ bırakma okumasını izler; karşıt yöndeki tek olumsuz aktarım kaynak içi uyuşmazlık olarak korunur.","branch_image_ar":"استبقاء الحياة وترك القتل","concept_gloss":"öldürmeyip sağ bırakma","contextual_glosses":[{"applicability":"Kadınların öldürülmeyip canlı bırakıldığı tarihsel veya anlatısal bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gençler veya başka kişi grupları üzerindeki daha geniş uygulamayı kapsamaz.","preserves":"Öldürmeme işlemini ve kadınların canlı kalması sonucunu açıkça verir."},"facet_ids":["F001","F002"],"text":"kadınları sağ bıraktılar","usage_role":"contextual"}],"definition":"Kadınları, gençleri veya başka belirli kişileri öldürmeyip sağ bırakmaktır. Kaynakların baskın açıklaması bu yöndedir; tek bir karşıt olumsuz aktarım tanımın parçası değil, metinsel uyuşmazlıktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Öldürme imkânı veya tehdidi altında bulunan kişileri öldürmeyip canlı bırakmak temel işlemdir."},{"facet_id":"F002","role":"specialization","statement":"Kadınlar ve bir topluluğun gençleri kaynakta açıkça belirtilen kişi gruplarıdır."},{"facet_id":"F003","role":"source_variant","statement":"Toplu aktarımın bir bölümündeki karşıt olumsuzluk, baskın sağ bırakma açıklamasıyla uyuşmayan metinsel bir değişkedir."}],"identity_rationale":"Kaynak ifadesinin çoğunluğu kadınları veya gençleri sağ bırakıp öldürmemeyi açıkça destekler. Buna karşılık toplu aktarımdaki bir parça bunun tersini söyleyen eksik ya da bozuk bir olumsuzluk içerdiğinden dal ancak bu metinsel karşıtlık belirtilerek kabul edilebilir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kadınları sağ bırakıyor ve öldürmüyorlar"}],"lexicalization_note":"Anlam yalnız belirli kişileri sağ bırakmayı bildiren türemiş yapıdadır; temel biçime genel bir utanma veya yaşam anlamı olarak taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bağışlayarak sağ bırakma ve daha genel koruma anlamları, bu yapının öldürmeme sınırını en iyi açıklayan iki yakın komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yapıya bağlı olarak öldürmeme ve canlı bırakmayı bildirir; komşu dal bağışlama, acıma ve ilişkiyi koruma gibi daha geniş gerekçeler taşıyabilir.","focus_only":"Belirli bir türemiş yapıda kadınları veya gençleri öldürmeme anlamı bu dala özgüdür.","gloss":"sağ bırakmak ile bağışlamak","neighbor_only":"Bağışlama, acıma ve sevgiyi sürdürme gerekçeleri komşu dalın daha geniş kapsamındadır.","neighbor_ref":"root_000142/B003","relation_type":"near_synonym","shared_zone":"İki dal da güç yetirilen bir kişiyi yok etmeyip koruma sonucunda birleşir."},{"boundary_match":"partial","distinction":"Bu dal doğrudan yaşamı sona erdirmemeye bağlıdır; komşu dal yaşam dışındaki koruma ve söz gözetme durumlarına da uzanır.","focus_only":"Öldürme karşısında kişiyi canlı bırakma bu dalın zorunlu sonucudur.","gloss":"sağ bırakmak ile koruyup saklamak","neighbor_only":"Nesneyi koruma, kişiye acıma ve verilen sözü gözetme komşu dalın ek kapsamıdır.","neighbor_ref":"root_000574/B006","relation_type":"near_synonym","shared_zone":"Her iki dal bir kişi veya şeyin ortadan kalkmasını önleyebilir."}],"source_phrase_ar":"ويستحيون نساءكم أي لا يستبقي (sihah); استحيوا شرخهم بمعنى استفعلوا من الحياة أي استبقوهم ولا تقتلوهم (tahdhib); ويستحيون نساءكم أي يستبقونهن (mufradat)","source_summary":"Toplu kanıtın baskın yönü belirli kişileri sağ bırakmak ve öldürmemektir; aynı toplu iddiadaki tek karşıt olumsuzluk, kaynaklara ayrı ayrı bağlanamayan bir uyuşmazlık olarak not edilmelidir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه استحياء النساء أو الصغار بمعنى استبقائهم أحياء وترك قتلهم.","what_is_not_ar":"لا يضم الحياء الخلقي أو الخجل، وإن اتحد اللفظ في استحيا."},"support_links":[]},{"boundary":"Dal karşılama, esenlik ve uzun ömür dileğine dayanır; egemenlik yorumu yalnız ayrı bir değişke olarak tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000383/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","surface_ar":"يَحْيَىٰ"}],"gloss":"esenlik, uzun ömür ve kalıcılık dileği","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye yaşam, kalıcılık ve esenlik dilemek karşılama sözünün temel işlevidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanların birbirini karşılaması ve esenlik sözünü karşılıklı iletmesi bu çekirdeğin toplumsal kullanımıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı sözün egemenlik bildirdiği yorumu, esenlik dileğinden ayrılması gereken bir kaynak değişkesidir."}}],"root_ar":"ح ي ي","root_id":"root_000383","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşılama sözünün yaşam ve esenlik dileyen ana işlevini eksiksiz anlatır.","boundary_detail":"Dal karşılama, esenlik ve uzun ömür dileğine dayanır; egemenlik yorumu yalnız ayrı bir değişke olarak tutulur.","branch_image_ar":"التحية دعاء بالحياة والسلام","concept_gloss":"esenlik, uzun ömür ve kalıcılık dileği","contextual_glosses":[{"applicability":"Bir kişinin diğerini karşılama sözüyle selamladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzun ömür dileğinin bütün ayrıntılarını ve egemenlik değişkesini kapsamaz.","preserves":"Karşılıklı söz ve esenlik dileği işlevini korur."},"facet_ids":["F001","F002"],"text":"esenlik dileğiyle karşıladı","usage_role":"contextual"}],"definition":"İnsanların birbirine esenlik, yaşam ve kalıcılık dilediği karşılama veya karşılık verme sözüdür. Bazı aktarımlarda aynı kalıp egemenlik bildirimi olarak yorumlandığından bu okuma ana anlamdan ayrı tutulur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye yaşam, kalıcılık ve esenlik dilemek karşılama sözünün temel işlevidir."},{"facet_id":"F002","role":"associated_use","statement":"İnsanların birbirini karşılaması ve esenlik sözünü karşılıklı iletmesi bu çekirdeğin toplumsal kullanımıdır."},{"facet_id":"F003","role":"source_variant","statement":"Aynı sözün egemenlik bildirdiği yorumu, esenlik dileğinden ayrılması gereken bir kaynak değişkesidir."}],"identity_rationale":"Kaynak ifadesinin ana çizgisi insanlar arasında esenlik, yaşam ve kalıcılık dileği taşıyan karşılama sözüdür. Aynı ifade içinde egemenlik yorumu da geçtiği için bu yorum çekirdeğe katılmamalı, ayrı bir kaynak değişkesi ve B008 ile kesişen okuma olarak gösterilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"Tanrı sana yaşam, kalıcılık ve esenlik versin"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"karşılama ve esenlik dileği"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yoruma göre bütün esenlik, kalıcılık ya da egemenlik Tanrı'nındır"}],"lexicalization_note":"Genel karşılama adı, yaşam ve esenlik dileyen kalıp ile bütün kalıcılığı yüce varlığa ayıran söz ayrı kullanımlar olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; esenlik sözünü iletme ve genel iyi dilek, karşılama işlevinin sınırını en açık gösteren iki komşu olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal doğrudan karşılama ve dilek bildirimidir; komşu dal önceden verilmiş esenlik sözünün aracıyla iletilmesine bağlıdır.","focus_only":"Doğrudan karşılama, uzun ömür dileği ve karşılıklı esenlik sözü bu dalın geniş kapsamındadır.","gloss":"karşılama sözü ile esenlik iletme","neighbor_only":"Bir başkasının esenlik sözünü üçüncü kişiye aynen iletme komşu dalın özel işlemidir.","neighbor_ref":"root_001211/B006","relation_type":"near_synonym","shared_zone":"Her iki dal bir kişiye esenlik bildiren sözlü davranışı kapsar."},{"boundary_match":"partial","distinction":"Bu dal kalıplaşmış karşılama ve yaşam dileğine bağlıdır; komşu dal karşılama gerektirmeyen çok çeşitli iyi dilek ve övgüleri kapsar.","focus_only":"Karşılama bağlamı ile yaşam ve kalıcılık dileği bu dala özgüdür.","gloss":"esenlik dileği ile genel iyi dilek","neighbor_only":"Övgü, bağışlanma isteği ve genel iyilik dileği komşu dalın daha geniş alanıdır.","neighbor_ref":"root_000879/B002","relation_type":"near_neighbor","shared_zone":"İki dal başkası için iyilik ve esenlik isteme eyleminde kesişir."}],"source_phrase_ar":"حياك الله أي ملكك الله والتحيات لله أي الملك لله (sihah); التحية ما يحيي به بعضهم بعضا وتحية الله السلام عليكم ورحمة الله وحياك الله أي أبقاك (tahdhib); التحية أن يقال حياك الله أي جعل لك حياة ثم يجعل دعاء (mufradat)","source_summary":"Toplu kanıt karşılama sözünü yaşam, kalıcılık ve esenlik dileği olarak açıklar; aynı toplu iddia içindeki egemenlik yorumu ise kaynaklara ayrıştırılamayan karşıt bir açıklama oluşturur.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه حياك الله، والتحية بين الناس، والرد على التحية، والتحيات لله من جهة السلام والدعاء بالبقاء والسلامة.","what_is_not_ar":"لا يضم الملك إلا في التفسير الخاص المختلف فيه للفظ التحية."},"support_links":[]},{"boundary":"Dal yalnız egemenlik yorumuna bağlıdır; esenlik bildiren olağan karşılama anlamı B007'de kalır.","branch_kind":"non_bare","branch_ref":"root_000383/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","surface_ar":"يَحْيَىٰ"}],"gloss":"egemenlik bildiren kalıplaşmış söz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Biçimin egemenlik ve yönetme gücü olarak yorumlanması bu sınırlı dalın çekirdeğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalıplaşmış söz, bütün egemenlik bildiren anlatımları yüce varlığa ayırır."}}],"root_ar":"ح ي ي","root_id":"root_000383","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız karşılama biçiminin egemenlik olarak yorumlandığı aktarımlara uygundur.","boundary_detail":"Dal yalnız egemenlik yorumuna bağlıdır; esenlik bildiren olağan karşılama anlamı B007'de kalır.","branch_image_ar":"التحية بمعنى الملك والسلطان","concept_gloss":"egemenlik bildiren kalıplaşmış söz","contextual_glosses":[{"applicability":"Kalıplaşmış sözün egemenlik yorumu açıkça amaçlandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Egemenliğin tümünü yüce varlığa bağlayan özel bildirimi korur."},"facet_ids":["F001","F002"],"text":"bütün egemenlik Tanrı'nındır","usage_role":"contextual"}],"definition":"Karşılama sözüyle aynı biçimin, belirli aktarımlarda egemenlik ve yönetme gücü olarak yorumlanmasıdır; kalıplaşmış kullanımda bütün egemenliğin yüce varlığa ait olduğu bildirilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Biçimin egemenlik ve yönetme gücü olarak yorumlanması bu sınırlı dalın çekirdeğidir."},{"facet_id":"F002","role":"specialization","statement":"Kalıplaşmış söz, bütün egemenlik bildiren anlatımları yüce varlığa ayırır."}],"identity_rationale":"Kaynak ifadesi karşılama sözüyle aynı biçimi belirli bir yorumda egemenlik ve yönetme gücü olarak açıklar; ayrıca kalıplaşmış sözde bütün egemenliği yüce varlığa ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"egemenlik ve yönetme gücü"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bütün egemenlik Tanrı'nındır"}],"lexicalization_note":"Egemenlik anlamı bağımsız bir temel kök anlamı sayılmaz; belirli sözlerin yorumuna ve aktarılan kalıplara bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dış adaylar anlamca uzak kaldı, aynı biçimin esenlik dileği olan B007 ise temel yorum ayrımını gösterdiği için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal biçimi egemenlik bildirimi olarak yorumlar; komşu dal aynı biçimin kişiye yaşam ve esenlik dileyen olağan işlevini anlatır.","focus_only":"Egemenlik ve yönetme gücü yorumu yalnız bu dalın çekirdeğidir.","gloss":"egemenlik yorumu ile esenlik dileği","neighbor_only":"İnsanlar arasında esenlik, yaşam ve kalıcılık dileme komşu dalın ana işlevidir.","neighbor_ref":"root_000383/B007","relation_type":"near_neighbor","shared_zone":"İki dal aynı karşılama biçimi ve aynı kalıplaşmış söz çevresinde ortaya çıkar."}],"source_phrase_ar":"التحية الملك وحياك الله أي ملكك الله (sihah); التحية الملك وأنشد يعني على ملكه والتحيات لله الألفاظ التي تدل على الملك (tahdhib)","source_summary":"Kaynaklar bu özel yorumda biçimi egemenlik ve yönetme gücüyle açıklar; kalıplaşmış söz de bu gücün tümünü yüce varlığa bağlar.","sources":["SI","TA"],"what_is_ar":"يدخل فيه التحية إذا فسرت بالملك، وعلى تحيته أي على ملكه، والتحيات لله عند من يفسرها بالملك.","what_is_not_ar":"لا يضم أصل السلام والتحية المتبادلة إلا بوصفها منشأ هذا التفسير."},"support_links":[]},{"boundary":"Dal yalnız bir hedefe gelme çağrısı yapan kalıba aittir; canlı kişi veya yaşam anlamıyla karıştırılmaz.","branch_kind":"non_bare","branch_ref":"root_000383/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","surface_ar":"يَحْيَىٰ"}],"gloss":"bir şeye gelmeye çağırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Muhatabı belirtilen hedefe gelmeye ve yönelmeye çağıran buyruk işlevi temel anlamdır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İbadete veya belirli bir yemeğe çağrı, yapının kaynakta verilen iki uygulama alanıdır."}}],"root_ar":"ح ي ي","root_id":"root_000383","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirtilen hedefe yönelmeyi isteyen kalıplaşmış buyruk için kullanılır.","boundary_detail":"Dal yalnız bir hedefe gelme çağrısı yapan kalıba aittir; canlı kişi veya yaşam anlamıyla karıştırılmaz.","branch_image_ar":"حي على بمعنى هلم وأقبل","concept_gloss":"bir şeye gelmeye çağırma","contextual_glosses":[{"applicability":"Hedefin bağlamdan anlaşıldığı doğrudan çağrılarda doğal Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İbadet veya yemek gibi açıkça adlandırılan hedefi belirtmez.","preserves":"Gelme ve yaklaşma çağrısını doğal bir buyrukla verir."},"facet_ids":["F001"],"text":"haydi, buraya gel","usage_role":"general"}],"definition":"Bir kişiyi belirtilen etkinliğe, ibadete veya yemeğe gelmeye ve yönelmeye çağıran, buyruk işlevli kalıplaşmış sözdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Muhatabı belirtilen hedefe gelmeye ve yönelmeye çağıran buyruk işlevi temel anlamdır."},{"facet_id":"F002","role":"example","statement":"İbadete veya belirli bir yemeğe çağrı, yapının kaynakta verilen iki uygulama alanıdır."}],"identity_rationale":"Tek kaynak ifadesi yapıyı bir eylem buyruğu gibi kullanılan, muhatabı belirli bir etkinliğe veya yemeğe gelmeye çağıran kalıplaşmış söz olarak açıkça tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"haydi ibadete gel"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"haydi et suyuna ekmek yemeğine gel"}],"lexicalization_note":"Anlam yalnız ardından yönelinen hedefin geldiği çağrı yapısında oluşur; tek başına temel biçime genellenmez.","neighbor_coverage_note":"Bütün çağrı ve ibadet adayları değerlendirildi; genel gelme çağrısı ile çekimli yaklaşma buyruğu, kalıbın hedefe bağlı sınırını en iyi gösteren iki adaydır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir yapıda hedefi kendisine bağlar; komşu dal daha genel ve bağımsız bir çağrı sözü olarak kullanılabilir.","focus_only":"Ardından yönelinen hedefi alan sabit çağrı yapısı bu dala özgüdür.","gloss":"hedefli çağrı ile genel gel çağrısı","neighbor_only":"Kişi ve sayı ayrımına girmeyen genel gelme, yaklaşma ve yönelme çağrısı komşu dalın kapsamıdır.","neighbor_ref":"root_001597/B001","relation_type":"near_synonym","shared_zone":"İki dal da muhatabı gelmeye, yaklaşmaya veya bir hedefe yönelmeye çağırır."},{"boundary_match":"partial","distinction":"Anlam çekirdeği yakındır, fakat bu dal hedef alan kalıplaşmış yapıdır; komşu dal çekimli ve daha genel bir yaklaşma buyruğudur.","focus_only":"Belirli hedefe yönelten değişmez çağrı kalıbı bu dala özgüdür.","gloss":"hedefe çağrı ile yaklaş çağrısı","neighbor_only":"Kişi, sayı ve cinsiyete göre biçimlenebilen yaklaşma çağrısı komşu dala özgüdür.","neighbor_ref":"root_001042/B006","relation_type":"near_synonym","shared_zone":"Her ikisi de muhataptan konuşana veya belirtilen yere doğru hareket etmesini ister."}],"source_phrase_ar":"قولهم حي على الصلاة معناه هلم وأقبل والعرب تقول حي على الثريد وهو اسم لفعل الأمر (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Kalıp, muhatabı belirtilen hedefe gelmeye çağırır ve eylem buyruğu gibi işler."}],"source_summary":"Bu dal tek bir tanıklıkla kuruludur; tanıklık yapının buyruk işlevli bir gelme çağrısı olduğunu ve iki ayrı hedefle kullanılabildiğini gösterir.","sources":["SI"],"what_is_ar":"يدخل فيه صيغة حي على الصلاة وحي على الثريد، أي هلم وأقبل، كاسم فعل للأمر.","what_is_not_ar":"لا يضم الحي بمعنى الحي من الناس أو الحياة."},"support_links":[]},{"boundary":"Dal kişiyi değil, ortak soyla kurulan topluluğu ve bazı kullanımlarda boyları birleştiren daha geniş topluluğu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000383/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","surface_ar":"يَحْيَىٰ"}],"gloss":"ortak soylu topluluk veya boylar birliği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ortak bir babadan gelen küçük veya büyük soy topluluğu temel kapsamdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birden çok boyu bir araya getiren daha geniş halk topluluğu kaynakta verilen kapsam uzantısıdır."}}],"root_ar":"ح ي ي","root_id":"root_000383","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem ortak babaya bağlı boyu hem de boyları birleştiren geniş topluluğu kapsar.","boundary_detail":"Dal kişiyi değil, ortak soyla kurulan topluluğu ve bazı kullanımlarda boyları birleştiren daha geniş topluluğu anlatır.","branch_image_ar":"الحي جماعة النسب والقبيلة","concept_gloss":"ortak soylu topluluk veya boylar birliği","contextual_glosses":[{"applicability":"Ortak bir ataya bağlanan belirli topluluğun anlatıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Birden çok boyu birleştiren daha geniş halk kapsamını içermez.","preserves":"Ortak soy ve topluluk çekirdeğini açıkça verir."},"facet_ids":["F001"],"text":"aynı soydan gelen boy","usage_role":"contextual"}],"definition":"Ortak bir babadan geldiği kabul edilen, sayısı az veya çok olabilen soy topluluğu ya da boydur; kullanım kimi zaman birden çok boyu bir araya getiren daha geniş halk topluluğuna uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ortak bir babadan gelen küçük veya büyük soy topluluğu temel kapsamdır."},{"facet_id":"F002","role":"extension","statement":"Birden çok boyu bir araya getiren daha geniş halk topluluğu kaynakta verilen kapsam uzantısıdır."}],"identity_rationale":"Kaynak ifadesi dalı ortak bir babadan gelen topluluk, Arap boyu veya daha geniş biçimde boyları birleştiren halk topluluğu olarak açıklar; bireysel canlı anlamı burada yer almaz.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"soy topluluğu ya da boy"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"aynı soydan gelen bir topluluk"}],"lexicalization_note":"Genel soy topluluğu adı ile belirli bir soyun çocuklarını bildiren yapı birbirinden ayrılır; kişi için canlı anlamı içeri alınmaz.","neighbor_coverage_note":"Bütün soy ve topluluk adayları değerlendirildi; genel topluluk ile boyların üst birliği, bu dalın ortak baba ve ölçek sınırlarını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeği ortak soy ve boy örgütlenmesidir; komşu dal soy dışındaki ortaklıklarla kurulan topluluklara da açıktır.","focus_only":"Ortak baba bağı ve Arap boy düzenindeki özel kullanım bu dala özgüdür.","gloss":"soy topluluğu ile genel topluluk","neighbor_only":"Tek bir iş çevresinde birleşen, soy bağı gerektirmeyen genel topluluk komşu dalın ek kapsamıdır.","neighbor_ref":"root_001016/B013","relation_type":"near_synonym","shared_zone":"İki dal boy, oymak ve birlikte hareket eden insan topluluğunu adlandırabilir."},{"boundary_match":"partial","distinction":"Bu dal tek bir soy topluluğunu da gösterebilir; komşu dal esas olarak birden çok boyu üst düzeyde birleştiren topluluğu adlandırır.","focus_only":"Tek bir ortak soydan gelen küçük veya büyük boy bu dalın çekirdeğidir.","gloss":"boy ile boylar topluluğu","neighbor_only":"Boyların üstünde yer alan ve onları birleştiren en geniş halk bölümü komşu dalın belirgin kapsamıdır.","neighbor_ref":"root_000797/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal soy ve boy düzenindeki insan topluluklarını sınıflandırır."}],"source_phrase_ar":"الحي حي من العرب وبنو حي بطن من العرب (jamhara); الحي واحد أحياء العرب (sihah); الحي الواحد من أحياء العرب يقع على بني أب كثروا أم قلوا وعلى شعب يجمع القبائل (tahdhib)","source_summary":"Kaynaklar Arap soy topluluğu ve boy anlamında birleşir; topluluğun büyüklüğü değişebilir ve kullanım boyları birleştiren daha geniş bir halka kadar uzanabilir.","sources":["JA","SI","TA"],"what_is_ar":"يدخل فيه الحي الواحد من أحياء العرب، وبنو حي أو بنو حيي، والشعب أو بنو الأب قلوا أو كثروا.","what_is_not_ar":"لا يضم الحي الفرد بمعنى غير الميت."},"support_links":[]},{"boundary":"Dal utanma duygusunu değil, dişi insan veya hayvandaki örtülü üreme organını ve kimi kullanımda döl yatağını anlatır.","branch_kind":"bare","branch_ref":"root_000383/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","surface_ar":"يَحْيَىٰ"}],"gloss":"dişi canlının üreme organı veya döl yatağı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi insan veya hayvanın dış üreme organı temel anatomik gönderimdir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Döl yatağı gönderimi, dış organla aynı ad altında tanıklanan ikinci anatomik okumadır."}}],"root_ar":"ح ي ي","root_id":"root_000383","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve hayvan kullanımlarını, ayrıca iki anatomik gönderimi birlikte kapsar.","boundary_detail":"Dal utanma duygusunu değil, dişi insan veya hayvandaki örtülü üreme organını ve kimi kullanımda döl yatağını anlatır.","branch_image_ar":"الحياء العضو المستور","concept_gloss":"dişi canlının üreme organı veya döl yatağı","contextual_glosses":[{"applicability":"Hayvan anatomisinin ve özellikle dişi devenin söz konusu olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kadın ve koyun kullanımını, ayrıca döl yatağı değişkesini kapsamaz.","preserves":"Dişi hayvandaki anatomik gönderimi açıkça korur."},"facet_ids":["F001"],"text":"dişi devenin üreme organı","usage_role":"contextual"}],"definition":"Kadın, dişi deve veya koyunda dış üreme organını, bazı kullanımlarda ise döl yatağını anlatan örtülü anatomik addır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi insan veya hayvanın dış üreme organı temel anatomik gönderimdir."},{"facet_id":"F002","role":"source_variant","statement":"Döl yatağı gönderimi, dış organla aynı ad altında tanıklanan ikinci anatomik okumadır."}],"identity_rationale":"Kaynak ifadesi dişi deve, koyun ve kadın için üreme organını açıkça bildirir; bazı tanıklıklar aynı adı döl yatağına yönelttiğinden iki anatomik gönderim tanımda korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"dişi insan ya da hayvanın üreme organı veya döl yatağı"}],"lexicalization_note":"Temel biçimin anatomik anlamı doğrudan tanımlanır; utanma duygusundan türetildiği düşünülse bile o duygu tanıma katılmaz.","neighbor_coverage_note":"Bütün anatomik ve örtülülük adayları değerlendirildi; genel özel bölge ve örtülmesi gereken yer, dişilik ile organ sınırını en yararlı biçimde açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal dişi anatomiyle ve kimi kullanımda döl yatağıyla sınırlıdır; komşu dal cinsiyet ayrımı olmadan daha geniş özel bölgeyi kapsar.","focus_only":"Dişi canlıya özgü kullanım ve döl yatağı değişkesi bu dalın kapsamındadır.","gloss":"dişi üreme organı ile özel bölge","neighbor_only":"Erkek, kadın ve hayvanda bacak arası, örtülmesi gereken yer ve genel özel bölge komşu dalın geniş kapsamıdır.","neighbor_ref":"root_001139/B003","relation_type":"near_synonym","shared_zone":"İki dal üreme organını veya örtülü beden bölgesini adlandırabilir."},{"boundary_match":"partial","distinction":"Bu dal anatomik bir organ adıdır; komşu dal örtülme gereğini ve özel alanı organın ötesine taşır.","focus_only":"Belirli bir anatomik organ bu dalın doğrudan gönderimidir.","gloss":"üreme organı ile örtülmesi gereken yer","neighbor_only":"Görünmesi utandıran her beden bölgesi ve özel kalma zamanları komşu dalın daha soyut kapsamıdır.","neighbor_ref":"root_001060/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal görünür tutulmayan özel beden bölgeleriyle ilişkilidir."}],"source_phrase_ar":"حياء الناقة وهو فرجها يمكن أن يكون من هذا (maqayis); الحياء أيضا رحم الناقة والجمع أحيية (sihah); الحي فرج المرأة وحياء الشاة والناقة والمرأة ممدود (tahdhib)","source_summary":"Kaynaklar dişi insan ve hayvanın üreme organı anlamında birleşir; toplu tanıklık dış organ ile döl yatağı arasında iki anatomik gönderim bulunduğunu gösterir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه حياء الناقة والشاة والمرأة، أي الفرج أو الرحم وما يستحيا من ذكره.","what_is_not_ar":"لا يضم الحياء الخلقي نفسه إلا باعتباره سبب التسمية."},"support_links":[]},{"boundary":"Dal yalnız yüz ve görünüş gönderimindedir; kişinin yaşamı anlamındaki eş biçim B001'de kalır.","branch_kind":"bare","branch_ref":"root_000383/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","surface_ar":"يَحْيَىٰ"}],"gloss":"yüz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan yüzü ve kişinin önden görünen çehresi tek temel gönderimdir."}}],"root_ar":"ح ي ي","root_id":"root_000383","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan yüzünün doğrudan adlandırıldığı bütün tanıklı bağlamlara uygundur.","boundary_detail":"Dal yalnız yüz ve görünüş gönderimindedir; kişinin yaşamı anlamındaki eş biçim B001'de kalır.","branch_image_ar":"المحيا وجه الإنسان","concept_gloss":"yüz","contextual_glosses":[{"applicability":"Bir kişinin yüzünden iyelik veya nesne ilişkisi içinde söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüzün doğrudan anatomik gönderimini bağlama uygun çekimle korur."},"facet_ids":["F001"],"text":"yüzü","usage_role":"contextual"}],"definition":"İnsanın başındaki yüzü ve önden görünen çehresini anlatan addır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan yüzü ve kişinin önden görünen çehresi tek temel gönderimdir."}],"identity_rationale":"Tek kaynak ifadesi biçimi doğrudan insan yüzü olarak tanımlar; yaşam anlamındaki eş biçimli kullanım için hiçbir kapsam iddiası taşımaz.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"yüz"}],"lexicalization_note":"Temel biçimin yüz anlamı doğrudan tanımlanır ve aynı biçimin yaşam anlamı bu dala aktarılmaz.","neighbor_coverage_note":"Bütün yüz ve görünüş adayları değerlendirildi; genel yüz adı ile güler yüz görünümü, doğrudan anatomik gönderimin sınırını en açık gösteren iki adaydır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İnsan yüzü bağlamında karşılıklar örtüşür; komşu dal hayvanlara ve nesnelerin ön ya da dış yüzüne de uzandığı için sınırlar tam değildir.","focus_only":"Yalnız insan yüzünü gösteren bu biçimin sözlük anlamı bu dala özgüdür.","gloss":"insan yüzü ile genel ön yüz","neighbor_only":"Hayvan yüzü, nesnenin önü ve dışa bakan yanı komşu dalın ek kapsamıdır.","neighbor_ref":"root_001630/B001","relation_type":"near_synonym","shared_zone":"İki dal insanın yüzünü doğrudan ve doğal biçimde adlandırabilir."},{"boundary_match":"partial","distinction":"Bu dal yüzün kendisini adlandırır; komşu dal yüzün taşıdığı hoş ifade ve güzelliği anlatır.","focus_only":"Yüzün anatomik varlığı bu dalın tek çekirdeğidir.","gloss":"yüz ile güler yüz","neighbor_only":"Yüzün güler, açık ve güzel görünmesi komşu dalın değerlendirme içeriğidir.","neighbor_ref":"root_000120/B006","relation_type":"near_neighbor","shared_zone":"İki dal insan yüzünü gönderim veya görünüş bakımından konu edinir."}],"source_phrase_ar":"المحيا الوجه (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Biçim, kişinin yaşamını değil doğrudan yüzünü adlandırır."}],"source_summary":"Bu dal tek bir tanıklıkla kuruludur ve tanıklık biçimi herhangi bir ek anlam vermeden doğrudan yüz olarak açıklar.","sources":["SI"],"what_is_ar":"يدخل فيه المحيا بمعنى الوجه.","what_is_not_ar":"لا يضم محياي بمعنى حياتي."},"support_links":[]},{"boundary":"Dal gerçek canlılık durumunu değil, yaşamı koruyan yarar, caydırma ve kurtarma sonucunu anlatan değer kullanımını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000383/B013","candidate_links":[{"candidate_id":"cand_7f508cf16e323ad37129","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","surface_ar":"يَحْيَىٰ"}],"gloss":"yarar, iyilik ve yok olmaktan koruma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yarar ve iyilik, yaşam sözünün bu dalda kazandığı değer çekirdeğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşılık yaptırımının öldürmeyi caydırıp insanları koruması, yararın toplumsal ve koruyucu gerçekleşmesidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birini yok olmaktan kurtarmak, yaşamı koruyan yararın doğrudan eylem uzantısıdır."}}],"root_ar":"ح ي ي","root_id":"root_000383","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Değer çekirdeğini, caydırıcı korumayı ve kurtarma sonucunu birlikte anlatır.","boundary_detail":"Dal gerçek canlılık durumunu değil, yaşamı koruyan yarar, caydırma ve kurtarma sonucunu anlatan değer kullanımını kapsar.","branch_image_ar":"الحياة بمعنى النفع والخير","concept_gloss":"yarar, iyilik ve yok olmaktan koruma","contextual_glosses":[{"applicability":"Caydırıcı bir düzenlemenin öldürmeyi azaltıp toplumu koruduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel iyilik anlamını ve tek bir kişiyi kurtarma kullanımını bütünüyle kapsamaz.","preserves":"Yararı, caydırmayı ve koruyucu toplumsal sonucu açıkça verir."},"facet_ids":["F001","F002"],"text":"insanları yok olmaktan koruyan yarar","usage_role":"explanatory"},{"applicability":"Bir kişinin veya canlının yıkımdan kurtarıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel yarar ile toplumsal caydırma boyutlarını kapsamaz.","preserves":"Yok olmaktan kurtarma eylemini ve koruyucu sonucu korur."},"facet_ids":["F003"],"text":"onu yok olmaktan kurtardı","usage_role":"contextual"}],"definition":"Yarar, iyilik veya yok olmaktan koruma sağlayan sonuçtur; özellikle karşılık yaptırımının öldürmeyi caydırarak insanları koruması ve birini yıkımdan kurtarmak bu değerin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yarar ve iyilik, yaşam sözünün bu dalda kazandığı değer çekirdeğidir."},{"facet_id":"F002","role":"specialization","statement":"Karşılık yaptırımının öldürmeyi caydırıp insanları koruması, yararın toplumsal ve koruyucu gerçekleşmesidir."},{"facet_id":"F003","role":"extension","statement":"Birini yok olmaktan kurtarmak, yaşamı koruyan yararın doğrudan eylem uzantısıdır."}],"identity_rationale":"Kaynak ifadesi yaşam sözünü yarar ve iyilik için kullanır; yaptırımın öldürmeyi caydırmasıyla toplumu korumasını ve birini yok olmaktan kurtarmayı bu değer alanının özel gerçekleşmeleri olarak açıklar.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yarar, iyilik ve yok olmaktan koruma"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"çocuğu yaşatan besin"}],"lexicalization_note":"Genel yarar ve iyilik okuması ile yaptırım, kurtarma ve çocuğu yaşatan besin gibi belirli yapılara bağlı kullanımlar birbirinden ayrılır.","neighbor_coverage_note":"Bütün yarar, iyilik, ceza ve suç adayları değerlendirildi; genel yarar, eğitici caydırma ve genel iyilik bu dalın yaşamı koruma sınırını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yararı yaşamın korunması ve kurtarma üzerinden kurar; komşu dal yaşamla ilgisi bulunmayan bütün yarar türlerine açıktır.","focus_only":"Yaşamı koruma, caydırıcı yaptırım ve yok olmaktan kurtarma bu dalın belirgin kapsamıdır.","gloss":"koruyucu yarar ile genel yarar","neighbor_only":"Zarara karşı duran her türlü genel yarar ve yararlı kişi komşu dalın daha geniş kapsamındadır.","neighbor_ref":"root_001536/B001","relation_type":"near_synonym","shared_zone":"İki dal zarar karşısında olumlu sonuç ve yarar bildirebilir."},{"boundary_match":"partial","distinction":"Bu dal öldürmenin karşılığı olan yaptırımın yaşam koruyucu sonucunu anlatır; komşu dal daha hafif ve eğitici cezayı anlatır.","focus_only":"Karşılık yaptırımının öldürmeyi önleyerek yaşamı koruması bu dala özgüdür.","gloss":"yaşamı koruyan caydırma ile eğitici ceza","neighbor_only":"Yasal üst sınıra varmayan eğitici ceza ve kötü davranışı durdurma komşu dalın kapsamıdır.","neighbor_ref":"root_001007/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal cezanın gelecekteki kötü eylemi caydırması sonucunda kesişir."},{"boundary_match":"partial","distinction":"Bu dal iyiliği yaşamı koruma ve kurtarma bağıyla sınırlar; komşu dal bütün yararlı ve erdemli sonuçları kapsar.","focus_only":"Yok olmaktan kurtarma ve yaşamı caydırma yoluyla koruma bu dalın özel içeriğidir.","gloss":"yaşamı koruyan iyilik ile genel iyilik","neighbor_only":"Kötülüğün karşıtı olan ve istenen her türlü genel iyilik komşu dalın geniş alanıdır.","neighbor_ref":"root_000452/B001","relation_type":"near_synonym","shared_zone":"İki dal olumlu, yararlı ve istenir sonucu ifade edebilir."}],"source_phrase_ar":"في القصاص حياة أي منفعة وليس بفلان حياة أي ليس عنده نفع ولا خير (tahdhib); ولكم في القصاص حياة أي يرتدع بالقصاص ومن أحياها أي من نجاها من الهلاك (mufradat)","source_summary":"Kaynaklar yaşam sözünün yarar ve iyilik değeri taşıdığını bildirir; caydırıcı yaptırımın insanları koruması ve yok olmaktan kurtarma bu değerin açıklanan uygulamalarıdır.","sources":["TA","MU"],"what_is_ar":"يدخل فيه الحياة بمعنى المنفعة والخير، وفي القصاص حياة من جهة ردع القتل وحفظ الناس، ومن أحياها أي نجاها من الهلاك.","what_is_not_ar":"لا يضم مطلق الحياة الحسية إلا إذا كان المقصود أثرها من النفع والحفظ."},"support_links":["sup_2126fdd8be499654fbb9"]},{"boundary":"Dal yalnız kişi adı olarak kullanılan biçimleri kapsar; aynı görünümlü eylem veya genel yaşam adı bu dala girmez.","branch_kind":"bare","branch_ref":"root_000383/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","surface_ar":"يَحْيَىٰ"}],"gloss":"yaşamla ilişkilendirilen erkek kişi adları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Erkek kişilere verilen ve yaşam alanıyla ilişkilendirilen özel adlar bu dalın temel kapsamıdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlardan birinin yaşamla bağı, yanlış davranışların kişiyi öldürememesi düşüncesiyle açıklanır."}}],"root_ar":"ح ي ي","root_id":"root_000383","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yüzey biçimleri kurulmadan, kaynakta kişi adı olduğu bildirilen bütün biçimleri topluca açıklar.","boundary_detail":"Dal yalnız kişi adı olarak kullanılan biçimleri kapsar; aynı görünümlü eylem veya genel yaşam adı bu dala girmez.","branch_image_ar":"أسماء الأعلام من الحياة","concept_gloss":"yaşamla ilişkilendirilen erkek kişi adları","contextual_glosses":[{"applicability":"Tek bir adın türü ve anlam bağlantısı yüzey biçimi verilmeden açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaynakta tanıklanan birden çok adı topluca kapsamaz.","preserves":"Kişi adı olma niteliğini ve yaşamla ilişkiyi korur."},"facet_ids":["F001"],"text":"yaşam anlamıyla ilişkilendirilmiş bir erkek adı","usage_role":"explanatory"}],"definition":"Yaşam düşüncesiyle ilişkilendirilen ve erkek kişiler için kullanılan özel adlar kümesidir; kaynak, adlardan birini yanlış davranışların öldüremediği kişi düşüncesiyle açıklar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Erkek kişilere verilen ve yaşam alanıyla ilişkilendirilen özel adlar bu dalın temel kapsamıdır."},{"facet_id":"F002","role":"associated_use","statement":"Adlardan birinin yaşamla bağı, yanlış davranışların kişiyi öldürememesi düşüncesiyle açıklanır."}],"identity_rationale":"Kaynak ifadesi birkaç erkek kişi adını açıkça tanıklar ve bunlardan birinin yaşamla ilişkisini yanlış davranışların onu öldürmemesi düşüncesiyle açıklar. Adların yüzey biçimi yazar tarafından kurulmadan dal topluca tanımlanabilir.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"yaşamla ilişkilendirilen erkek kişi adları"}],"lexicalization_note":"Kişi adı kullanımları temel biçim düzeyinde tanıklanır; ad olmayan eylem ve yaşam biçimleri bu özel ad dalına aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; verilen komşular bitki, sıvı veya başka nesne alanlarına aitti ve kişi adı dalının anlam sınırını yararlı biçimde kesmediği için ayrım yayımlanmadı.","source_phrase_ar":"حيي اسم رجل (jamhara); حيوة اسم رجل (sihah); حيوة اسم رجل بسكون الياء (tahdhib); اسمه يحيى نبه أنه سماه بذلك من حيث إنه لم تمته الذنوب (mufradat)","source_summary":"Toplu tanıklık birkaç erkek kişi adını bu kök ailesine bağlar; ayrıca bir ad için yaşamı yanlış davranışların söndürememesi düşüncesine dayanan açıklama verir.","sources":["JA","SI","TA","MU"],"what_is_ar":"يدخل فيه يحيى، وحيوة، وحيي إذا وردت أسماء رجال أو أعلاما، مع تعليل يحيى بالحياة عند الراغب.","what_is_not_ar":"لا يضم الفعل يحيى أو الاسم الحياة إذا لم يكن علما."},"support_links":[]},{"boundary":"Dal, yaşamın sona ermesini anlatır; dilek, yalan veya okuma anlamlarını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_001454/B001","candidate_links":[{"candidate_id":"cand_c253bb91ae6112790ccf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","surface_ar":"يَمُوتُ"}],"gloss":"yaşamın ve canlı gücünün sona ermesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlıdaki güç ve yaşam sona erer; bu durum yaşamın karşıtıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ölümün türleri, karşılık geldikleri yaşam türlerine göre ayrılabilir."}}],"root_ar":"م و ت","root_id":"root_001454","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir canlının yaşam durumunun bütünüyle sona ermesini anlatan genel çekirdek karşılıktır.","boundary_detail":"Dal, yaşamın sona ermesini anlatır; dilek, yalan veya okuma anlamlarını içermez.","branch_image_ar":"ذهاب القوة والحياة","concept_gloss":"yaşamın ve canlı gücünün sona ermesi","contextual_glosses":[{"applicability":"Belirli bir canlının yaşamdan ayrıldığını bildiren yüklem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli canlıda yaşamın sona erdiğini doğal bir yüklemle eksiksiz aktarır."},"facet_ids":["F001"],"text":"öldü","usage_role":"contextual"}],"definition":"Canlıdaki güç ve yaşamın sona ermesi, yani yaşam durumunun karşıtına geçmesidir. Ölüm türleri, söz konusu yaşam türlerine göre ayrılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlıdaki güç ve yaşam sona erer; bu durum yaşamın karşıtıdır."},{"facet_id":"F002","role":"source_variant","statement":"Ölümün türleri, karşılık geldikleri yaşam türlerine göre ayrılabilir."}],"identity_rationale":"Kaynak ifadesi, canlıdaki gücün ve yaşamın sona ermesini çekirdek anlam olarak verir; ayrıca ölümün yaşamın karşıtı olduğunu ve yaşam türlerine göre ölüm türlerinin de ayrılabildiğini belirtir. Verilen dal çerçevesi bu bileşenleri doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ölüm; yaşamın sona ermesi"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"öldü; yaşamdan ayrıldı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"öldü; yaşamdan ayrıldı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yakında ölecek kimse"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"ölmüş veya ölecek kimse"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kesin ve gerçek ölüm"}],"lexicalization_note":"Mekanik kapsam hem yalın anlamı hem de türemiş biçimlerle bir pekiştirme kalıbını içerir; kalıba özgü pekiştirme çekirdek ölüm anlamına genellenmez.","neighbor_coverage_note":"Verilen bütün komşu adayları karşılaştırıldı; yalnızca ölümle göçüp gitme ve genel yok oluş arasındaki sınırı açıklayan iki ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal doğrudan ve genel ölüm kavramıdır; komşu dal ise insan ölümü için uzaklaşma görüntüsüne dayanan özel bir anlatımdır.","focus_only":"Odak dal, yaşamın sona ermesini bütün canlılar için genel bir kavram olarak ele alır.","gloss":"ölmek ve bu dünyadan göçüp gitmek","neighbor_only":"Komşu dal, ölen bir insanı gitme hareketiyle anlatan özel bir söyleyişe bağlıdır.","neighbor_ref":"root_001430/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da bir insanın yaşamının sona ermesini anlatabilir."},{"boundary_match":"partial","distinction":"Ölüm yaşam taşıyan varlığa bağlıdır; yok oluş ise yaşam koşulu aramadan bir şeyin tükenmesini veya ortadan kaldırılmasını da anlatır.","focus_only":"Odak dalın kurucu sınırı, canlıdaki yaşamın sona ermesidir.","gloss":"ölüm ve yok oluş","neighbor_only":"Komşu dal, canlı olmayan şeylerin de tükenmesini, yok olmasını ve ortadan kaldırılmasını kapsar.","neighbor_ref":"root_001181/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da önceden var olan bir durumun kesilmesi ve sona ermesi bulunur."}],"source_phrase_ar":"أصل صحيح يدل على ذهاب القوة من الشيء (maqayis)؛ الموت خلاف الحياة (maqayis;sihah)؛ الموت معروف مات يموت موتا (jamhara)؛ الموت خلق من خلق الله (tahdhib)؛ أنواع الموت بحسب أنواع الحياة (mufradat)","source_summary":"Kaynakların ortak çekirdeği, ölümü yaşamın ve canlı gücünün sona ermesi olarak tanımlar. Toplu aktarım ayrıca bunun temel bir yaratılmış durum olduğunu ve farklı yaşam biçimlerine göre farklı ölüm türlerinden söz edilebildiğini bildirir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"الموت وضد الحياة وما يقال في المَيّت والمائت وتوكيد موت مائت وأنواع الموت بحسب الحياة","what_is_not_ar":"ليس تمني الشيء ولا الكذب ولا التلاوة"},"support_links":["sup_d8c3c7ff070cd4abfbe1"]},{"boundary":"Dal, ölümün kendisini değil, ölüm veya güç kaybı meydana getiren ettirgen işlemi anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001454/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","surface_ar":"يَمُوتُ"}],"gloss":"öldürme veya pişirerek keskinliğini giderme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ettirgen bir işlem, canlıda ölümü ya da bir şeyde güç kaybını meydana getirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Pişirme, içkinin keskinliğini ve etkisini azaltan özel gerçekleştirme yoludur."}}],"root_ar":"م و ت","root_id":"root_001454","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ettirgen ölüm anlamını ve yalnızca belirtilen pişirme bağlamındaki güç azaltmayı birlikte temsil eder.","boundary_detail":"Dal, ölümün kendisini değil, ölüm veya güç kaybı meydana getiren ettirgen işlemi anlatır.","branch_image_ar":"إذهاب القوة بالإماتة","concept_gloss":"öldürme veya pişirerek keskinliğini giderme","contextual_glosses":[{"applicability":"İçkinin pişirilip sertliğinin veya etkisinin azaltıldığı özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Pişirme işlemini ve bunun keskinliği azaltan sonucunu birlikte korur."},"facet_ids":["F002"],"text":"pişirerek keskinliğini giderdiler","usage_role":"contextual"}],"definition":"Bir canlıyı öldürmek veya bir şeyin gücünü ve keskinliğini gidermektir. Özel olarak, pişirme işlemiyle içkinin sertliğinin azaltılmasını da anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ettirgen bir işlem, canlıda ölümü ya da bir şeyde güç kaybını meydana getirir."},{"facet_id":"F002","role":"specialization","statement":"Pişirme, içkinin keskinliğini ve etkisini azaltan özel gerçekleştirme yoludur."}],"identity_rationale":"Kaynak ifadesi iki bağlı kullanımı açıkça destekler: bir canlıyı öldürmek veya bir şeyin gücünü gidermek ve pişirme yoluyla içkinin keskinliğini azaltmak. Dal çerçevesi bu ettirgen çekirdeği ve özel pişirme uygulamasını birbirine karıştırmadan korur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"öldürdü; gücünü giderdi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"pişirerek keskinliğini giderin"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"içki pişirilip keskinliği giderildi"}],"lexicalization_note":"Mekanik kapsam ettirgen biçimle pişirme kalıplarını birlikte içerir; pişirmeye bağlı keskinlik giderme anlamı her öldürme kullanımına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ettirgen ölüm ile ölüm durumu ve hayvan ölümü alanı arasındaki iki yararlı sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırt edici uzantısı pişirmeyle gücü azaltmadır; komşu dal ise hayvanın ölümü ve ölüsü çevresinde daha geniş bir alan kurar.","focus_only":"Odak dal, pişirmeyle bir şeyin keskinliğini azaltan özel kullanımı da içerir.","gloss":"öldürme ve ölü hale getirme","neighbor_only":"Komşu dal, hayvan ölümü, hayvan ölüsü ve öldürme buyruğu gibi daha geniş hayvan bağlamlarını içerir.","neighbor_ref":"root_001568/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da bir canlıda ölümü meydana getirme anlamında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal ölüme yol açan işlemdir; komşu dal ise bu işlemin nedeni belirtilsin ya da belirtilmesin ortaya çıkan ölüm durumudur.","focus_only":"Odak dal, sonucu meydana getiren bir ettirgen ve bunu yapan bir katılımcı gerektirir.","gloss":"öldürme ve ölüm","neighbor_only":"Komşu dal, yaşamın sona ermesi durumunu herhangi bir ettirgen belirtmeden anlatır.","neighbor_ref":"root_001454/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın ortak sonucu canlı yaşamının sona ermesidir."}],"source_phrase_ar":"أميتوها طبخا (maqayis)؛ أميتت الخمر طبخت (maqayis)؛ أماته الله وموته شدد للمبالغة (sihah)","source_summary":"Toplu kanıt, ettirgen kullanımı bir canlıyı öldürme veya bir şeyin gücünü giderme olarak verir. Pişirme örneği bu çekirdeğin, içkinin keskinliğini azaltmaya özgü bir uygulamasıdır.","sources":["MQ","SI","TA"],"what_is_ar":"إماتة الشيء أو تمييته وإضعاف حدته بالطبخ كإماتة الخمر والشجرة الخبيثة","what_is_not_ar":"ليس مجرد وقوع الموت ولا الميتة"},"support_links":[]},{"boundary":"Dal canlı hayvanları, köleleri veya binekleri değil, cansız şeyleri ve yararlanılmayan araziyi kapsar.","branch_kind":"bare","branch_ref":"root_001454/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","surface_ar":"يَمُوتُ"}],"gloss":"cansız şey; işlenmemiş veya sahipsiz arazi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Varlık canlı değildir ve ruh taşıyan hayvanlar sınıfına girmez."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Arazi ekim veya iyileştirme yoluyla üretken hale getirilmemiştir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Arazi sahipsiz olabilir ve kimse ondan yararlanmıyor olabilir."}}],"root_ar":"م و ت","root_id":"root_001454","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ruh taşımayan eşya ile ekilip iyileştirilmemiş ya da kimsenin yararlanmadığı araziyi kapsar.","boundary_detail":"Dal canlı hayvanları, köleleri veya binekleri değil, cansız şeyleri ve yararlanılmayan araziyi kapsar.","branch_image_ar":"أرض موات ومتاع لا روح فيه","concept_gloss":"cansız şey; işlenmemiş veya sahipsiz arazi","contextual_glosses":[{"applicability":"Ekilmemiş, iyileştirilmemiş ve kimsenin yararlanmadığı arazi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Araziye özgü işlenmemişlik, sahipsizlik ve yararlanılmama sınırlarını korur."},"facet_ids":["F002","F003"],"text":"işlenmemiş ve sahipsiz arazi","usage_role":"contextual"}],"definition":"Ruh taşımayan bir şey ya da ekim ve iyileştirmeyle canlandırılmamış arazidir. Arazi ayrıca sahipsiz ve kimsenin yararlanmadığı yer olarak da belirlenebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Varlık canlı değildir ve ruh taşıyan hayvanlar sınıfına girmez."},{"facet_id":"F002","role":"specialization","statement":"Arazi ekim veya iyileştirme yoluyla üretken hale getirilmemiştir."},{"facet_id":"F003","role":"source_variant","statement":"Arazi sahipsiz olabilir ve kimse ondan yararlanmıyor olabilir."}],"identity_rationale":"Kaynak ifadesi hem ruh taşımayan şeyleri hem de ekim ve iyileştirmeyle canlandırılmamış, sahipsiz veya kullanılmayan araziyi kapsar. Dal çerçevesi araziye özgü koşulları genel cansızlık alanından ayırarak doğru biçimde sunar.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"işlenmemiş arazi; canlı olmayan şey"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"cansız şey; sahipsiz ve kullanılmayan arazi"}],"lexicalization_note":"Mekanik kapsam yalındır; tanım yalnızca cansız şey ve işlenmemiş ya da sahipsiz arazi anlamlarını içerir, başka kalıplardan anlam almaz.","neighbor_coverage_note":"Adayların tamamı incelendi; arazi anlamını en iyi sınırlayan ekilmemiş boş arazi ve yerleşilmemiş arazi komşuları seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal cansız eşya alanına da uzanır ve sahipsizlik ölçütünü taşır; komşu dalın çekirdeği ise boşluk ve tarımsal verimsizliktir.","focus_only":"Odak dal, ruh taşımayan eşya ile sahipsiz ve kullanılmayan araziyi de kapsar.","gloss":"işlenmemiş veya boş arazi","neighbor_only":"Komşu dal, boş konutları ve tarıma elverişsiz olabilen ekilmemiş toprağı özellikle kapsar.","neighbor_ref":"root_000164/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da ekilmemiş, boş veya üretime katılmamış araziyi anlatabilir."},{"boundary_match":"partial","distinction":"Yerleşilmemiş arazi mutlaka sahipsiz veya tarımsal olarak canlandırılmamış değildir; odak dal bu daha özel ölçütleri de gerektirebilir.","focus_only":"Odak dal, sahipsizlik, yararlanılmama ve cansız eşya gibi ek sınırlar taşır.","gloss":"kullanılmayan ve yerleşilmemiş arazi","neighbor_only":"Komşu dal yalnızca arazinin yerleşim görmemiş olmasını öne çıkarır.","neighbor_ref":"root_001535/B011","relation_type":"near_neighbor","shared_zone":"Her iki dal da insan eliyle etkin biçimde kullanılmayan araziyi kapsar."}],"source_phrase_ar":"الموتان الأرض لم تحي بعد بزرع ولا إصلاح وكذلك الموات (maqayis)؛ الموات ما لا روح فيه (sihah)؛ الموات الأرض التي لا مالك لها ولا ينتفع بها أحد (sihah)؛ الموتان أن يبيع المتاع وكل شيء غير ذي روح (tahdhib)","source_summary":"Toplu kanıt, genel cansızlık ile işlenmemiş arazi anlamlarını aynı dalda birleştirir. Arazi için ekilip iyileştirilmemiş olma, sahipsizlik ve fiilen yararlanılmama ölçütleri aktarılır; cansız eşya da kapsam içindedir.","sources":["MQ","SI","TA"],"what_is_ar":"الأرض التي لم تحي بزرع ولا إصلاح أو لا مالك لها ولا ينتفع بها وما لا روح فيه من متاع ودور","what_is_not_ar":"ليس الحيوان ولا الرقيق ولا الدواب"},"support_links":[]},{"boundary":"Dal, bir topluluk veya varlık grubu içinde görülen ölümü anlatır; işlenmemiş arazi anlamını içermez.","branch_kind":"bare","branch_ref":"root_001454/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","surface_ar":"يَمُوتُ"}],"gloss":"insanlar veya hayvan varlığı içinde ölüm görülmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluk veya varlık grubu içinde ölüm meydana gelir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Etkilenen grup insanlar, hayvan sürüsü veya mal varlığı olabilir."}}],"root_ar":"م و ت","root_id":"root_001454","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir insan topluluğunda, sürüde veya mal varlığı içinde ölüm meydana geldiğini topluca anlatır.","boundary_detail":"Dal, bir topluluk veya varlık grubu içinde görülen ölümü anlatır; işlenmemiş arazi anlamını içermez.","branch_image_ar":"مُوتان واقع في الناس أو المال","concept_gloss":"insanlar veya hayvan varlığı içinde ölüm görülmesi","contextual_glosses":[{"applicability":"Bir hayvan sürüsünün üyeleri arasında ölüm meydana geldiğini bildiren bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Grup içindeki ölüm olayını ve hayvan sürüsü katılımcısını açıkça korur."},"facet_ids":["F001","F002"],"text":"sürüde ölüm görüldü","usage_role":"contextual"}],"definition":"İnsanlar ya da hayvan ve mal varlığı içinde ölüm görülmesi, yani grubun üyelerinin ölmesi durumudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluk veya varlık grubu içinde ölüm meydana gelir."},{"facet_id":"F002","role":"extension","statement":"Etkilenen grup insanlar, hayvan sürüsü veya mal varlığı olabilir."}],"identity_rationale":"Kaynak ifadesi insanlarda, hayvan varlığında veya mal içinde görülen ölüm olayını açıkça bildirir. Dal çerçevesi bunu arazi ve cansızlık bildiren benzer biçimden ayırdığı için kaynak sınırına uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"insanlarda veya hayvanlarda görülen ölüm"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"mal veya hayvan varlığı içindeki ölüm"}],"lexicalization_note":"Mekanik kapsam yalındır; tanım insanlarda veya hayvan ve mal varlığında görülen ölüm olgusuyla sınırlıdır.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; toplu ölümün art arda ölümden ve sürü kaybının sonucundan ayrımını gösteren iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal grup içindeki ölüm olgusunu genel bırakır; komşu dalda ölümlerin peş peşe gelmesi kurucu bir koşuldur.","focus_only":"Odak dal, ölümlerin birbirini izlemesini zorunlu kılmaz ve hayvan ya da mal varlığını da kapsar.","gloss":"toplulukta ölüm ve art arda ölüm","neighbor_only":"Komşu dal, insanların art arda birer birer ölmesi biçimindeki zamansal dizilişi gerektirir.","neighbor_ref":"root_000021/B009","relation_type":"near_synonym","shared_zone":"Her iki dal da bir grubun birden fazla üyesinin ölmesi durumunu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal olayın kendisidir; komşu dal ise bu olaydan etkilenen insanların sonradan kazandığı durumu anlatır.","focus_only":"Odak dal doğrudan sürüde veya mal varlığında meydana gelen ölüm olayını adlandırır.","gloss":"sürü ölümü ve sürüsünü yitirmiş topluluk","neighbor_only":"Komşu dal, sürünün yok olmasından sonra insanların içine düştüğü sonucu ve durumu adlandırır.","neighbor_ref":"root_000619/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalın ortak sahnesinde bir topluluğun hayvan varlığı ölümle kaybedilir."}],"source_phrase_ar":"وقع في الناس موتان (maqayis)؛ الموتان بالضم موت يقع في الماشية (sihah)؛ وقع في المال موتان وموات وهو الموت (tahdhib)","source_summary":"Toplu kanıt, bu kullanımı tek bir bireyin ölümünden çok insanlar, hayvanlar veya mal varlığı içinde görülen ölüm olgusu olarak sunar. Aktarımlar kapsamı insan topluluğundan sürü ve mala kadar genişletir.","sources":["MQ","SI","TA"],"what_is_ar":"المُوتان بمعنى موت يقع في الناس أو المال والماشية","what_is_not_ar":"ليس المَوَتان من الأرض ولا خلاف الحيوان"},"support_links":[]},{"boundary":"Ölüm nitelenen ebeveynin değil, onun çocuğunun başına gelir.","branch_kind":"mixed_non_bare","branch_ref":"root_001454/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","surface_ar":"يَمُوتُ"}],"gloss":"çocuğu ölmüş ebeveyn veya ana hayvan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir ebeveynin çocuğu ölür; nitelenen katılımcı ebeveyndir, ölen ise çocuktur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ebeveyn bir ana hayvan, kadın veya erkek olabilir; bir ya da birden çok çocuk kaybı söz konusu olabilir."}}],"root_ar":"م و ت","root_id":"root_001454","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çocuğunu ölümle kaybetmiş insan ebeveyni ya da ana hayvanı nitelemek için kullanılır.","boundary_detail":"Ölüm nitelenen ebeveynin değil, onun çocuğunun başına gelir.","branch_image_ar":"موت الولد للوالد أو الناقة","concept_gloss":"çocuğu ölmüş ebeveyn veya ana hayvan","contextual_glosses":[{"applicability":"Bir insanın çocuğunun öldüğünü, ebeveynin kendi ölümüyle karıştırmadan bildiren bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çocuğun ölümü ile ebeveynin hayatta kalması arasındaki katılımcı ayrımını korur."},"facet_ids":["F001","F002"],"text":"çocuğunu ölümle kaybetti","usage_role":"contextual"}],"definition":"Kendisi hayatta olduğu halde çocuğu ölen ana hayvanın, kadının veya erkeğin kazandığı durumdur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir ebeveynin çocuğu ölür; nitelenen katılımcı ebeveyndir, ölen ise çocuktur."},{"facet_id":"F002","role":"extension","statement":"Ebeveyn bir ana hayvan, kadın veya erkek olabilir; bir ya da birden çok çocuk kaybı söz konusu olabilir."}],"identity_rationale":"Kaynak ifadesi, ölen kişinin veya hayvanın kendisini değil, çocuğu ölen ana hayvanı, kadını veya erkeği nitelemektedir. Dal çerçevesi ebeveyn ile ölen çocuk arasındaki bu katılımcı ayrımını eksiksiz korur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yavrusu ölmüş ana hayvan veya çocuğu ölmüş kadın"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"oğlu veya oğulları öldü"}],"lexicalization_note":"Mekanik kapsam bir niteleme biçimi ile kişi kalıbını birlikte içerir; her ikisi de çocuğu ölen ebeveyn sınırında tutulur.","neighbor_coverage_note":"Bütün adaylar incelendi; çocuk ölümü ile genel çocuksuzluk ve hayvana özgü yavru kaybı arasındaki iki yakın sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli çocuk ölümü ilişkisine bağlıdır; komşu dal daha kalıcı çocuksuzluk ve başka yoksunluk durumlarına da açılır.","focus_only":"Odak dal ana hayvanı, kadını ve erkeği çocuğun fiilen ölmesi üzerinden niteler.","gloss":"çocuk kaybı yaşamış ebeveyn","neighbor_only":"Komşu dal, çocuklarının yaşamaması yanında çocuksuz ve kazançsız dul veya yaşlı kişilere ilişkin aktarımları da içerir.","neighbor_ref":"root_000584/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da çocuğu yaşamayan veya ölen ebeveynin durumunda örtüşür."},{"boundary_match":"partial","distinction":"Odak dalda çocuk ölümü ve insan ebeveyn kapsamı belirleyicidir; komşu dal hayvana özgüdür ve daha geniş yavru kaybı nedenlerini içerir.","focus_only":"Odak dal insan ebeveynleri de kapsar ve çocuğun ölmesini temel koşul yapar.","gloss":"yavrusunu kaybetmiş ana hayvan","neighbor_only":"Komşu dal yalnızca ana hayvana bağlıdır ve yavrunun alınması, düşürülmesi veya erken atılması gibi ölüm dışı kayıpları da kapsar.","neighbor_ref":"root_000727/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da yavrusu ölen bir ana hayvanı niteleyebilir."}],"source_phrase_ar":"ناقة مميت ومميتة للتي يموت ولدها (maqayis)؛ أماتت الناقة إذا مات ولدها فهي مميت ومميتة (sihah)؛ وكذلك المرأة (sihah)؛ أمات فلان إذا مات له ابن أو بنون (sihah)","source_summary":"Kaynakların ortak anlatımı, nitelenen varlığın kendi ölümünü değil çocuk kaybını öne çıkarır. Kapsam ana hayvandan kadın ve erkeğe uzanır; kişi kalıbında bir oğlun veya oğulların ölmesi belirtilir.","sources":["MQ","SI","TA"],"what_is_ar":"من مات ولده من ناقة أو امرأة أو رجل فيقال ناقة مميت ومميتة وأمات فلان إذا مات له ابن أو بنون","what_is_not_ar":"ليس موت صاحب الوصف نفسه"},"support_links":[]},{"boundary":"Dal bedensel ölümü değil, zekâ ve anlama gücünün bulunmamasını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001454/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","surface_ar":"يَمُوتُ"}],"gloss":"zekâ ve anlayıştan yoksunluk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişide zekâ, anlayış ve hızlı kavrayış bulunmaz."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zihinsel yetersizlik, kalbin körelmiş veya ölü olması görüntüsüyle dile getirilir."}}],"root_ar":"م و ت","root_id":"root_001454","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin kavrayış ve anlama gücünün bulunmadığını bildiren niteleyici anlamdır.","boundary_detail":"Dal bedensel ölümü değil, zekâ ve anlama gücünün bulunmamasını anlatır.","branch_image_ar":"موتان الفؤاد","concept_gloss":"zekâ ve anlayıştan yoksunluk","contextual_glosses":[{"applicability":"Bir kişinin zekâ ve kavrayış eksikliğini doğal bir niteleme olarak aktaran bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin anlayış ve kavrayış bakımından yetersiz olması anlamını korur."},"facet_ids":["F001"],"text":"anlayışı kıt","usage_role":"contextual"}],"definition":"Bir kişinin zekâ ve anlama gücünden yoksun, kavrayışı körelmiş olmasıdır; bu durum kalbin ölü oluşu görüntüsüyle anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişide zekâ, anlayış ve hızlı kavrayış bulunmaz."},{"facet_id":"F002","role":"associated_use","statement":"Zihinsel yetersizlik, kalbin körelmiş veya ölü olması görüntüsüyle dile getirilir."}],"identity_rationale":"Kaynak ifadesi beden ölümünü değil, zekâ ve anlama gücünden yoksunluğu kalbin körelmesi görüntüsüyle anlatır. Dal çerçevesi bu niteleyici ve ünlemli kullanımları aynı zihinsel yetersizlik çekirdeğinde doğru biçimde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"zekâsı ve anlayışı kıt kimse"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ne kadar anlayışsız!"}],"lexicalization_note":"Mekanik kapsam kalıplaşmış bir niteleme ve bir ünlemli birimi içerir; anlam bu belirli zihinsel yetersizlik kullanımlarında tutulur.","neighbor_coverage_note":"Tüm komşular değerlendirildi; en yakın kavrayışsızlık dalı ile karşıt kutuptaki hızlı kavrayış dalı sınırı en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekler yakın olsa da odak dal kalbe bağlı özel anlatım ve ünlem kapsamına sahiptir; komşu dal doğrudan kişi niteliğidir.","focus_only":"Odak dal, anlayışsızlığı kalbin körelmesi görüntüsüne bağlı belirli kalıp ve ünlemle anlatır.","gloss":"anlayışsız ve ağır kavrayışlı","neighbor_only":"Komşu dal, belirli bir erkek nitelemesi olarak doğrudan ağır kavrayışlılığı bildirir.","neighbor_ref":"root_001250/B019","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin anlamayan, zekâca yetersiz oluşunu anlatır."},{"boundary_match":"opposed","distinction":"Odak dal bu kapasitenin yokluğunu veya körelmesini, komşu dal ise belirgin beceri ve hızlı kavrayışı gösterir.","focus_only":"Odak dalda zekâ, anlayış ve hızlı kavrayış eksiktir.","gloss":"kavrayışsızlık ve hızlı kavrayış","neighbor_only":"Komşu dalda öğrenme, anlama ve uygulama becerisi hızlı ve gelişmiştir.","neighbor_ref":"root_000201/B002","relation_type":"polarity_pair","shared_zone":"İki dal da kişinin öğrenme ve anlama kapasitesini değerlendiren aynı bilişsel eksendedir."}],"source_phrase_ar":"رجل موتان الفؤاد وامرأة موتانة (maqayis)؛ رجل موتان الفؤاد وامرأة موتانة الفؤاد (sihah)؛ رجل موتان الفؤاد إذا كان غير ذكي ولا فهم (tahdhib)","source_summary":"Kaynaklar bu nitelemeyi zekâ ve anlayış eksikliği olarak ortaklaşa açıklar. Kalbe bağlanan ölüm görüntüsü bedensel ölüm bildirmez; kişinin kavrayışsızlığını güçlendiren bir anlatımdır.","sources":["MQ","SI","TA"],"what_is_ar":"موتان الفؤاد لمن لا ذكاء له ولا فهم أو لقلب أموت","what_is_not_ar":"ليس موت الجسد"},"support_links":[]},{"boundary":"Kapsam, eti yenebilen ve usulüne uygun kesim gerçekleşmeden ölen hayvanla sınırlıdır.","branch_kind":"bare","branch_ref":"root_001454/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","surface_ar":"يَمُوتُ"}],"gloss":"usulüne uygun kesilmeden ölen yenilebilir hayvan","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eti yenebilen bir hayvan ölmüştür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvan ölmeden önce usulüne uygun kesim gerçekleşmemiştir."}}],"root_ar":"م و ت","root_id":"root_001454","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eti yenebilen bir hayvanın geçerli kesim yapılmadan öldüğü durumda ortaya çıkan hayvan ölüsünü anlatır.","boundary_detail":"Kapsam, eti yenebilen ve usulüne uygun kesim gerçekleşmeden ölen hayvanla sınırlıdır.","branch_image_ar":"الميتة بلا ذكاة","concept_gloss":"usulüne uygun kesilmeden ölen yenilebilir hayvan","contextual_glosses":[{"applicability":"Eti yenebilen hayvanın usulüne uygun kesimden önce öldüğü gıda bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın ölümünü ve geçerli kesimin ölümden önce gerçekleşmemesini korur."},"facet_ids":["F001","F002"],"text":"kesilmeden ölmüş hayvan","usage_role":"contextual"}],"definition":"Eti yenebilen bir hayvanın usulüne uygun kesim gerçekleşmeden ölmesiyle ortaya çıkan hayvan ölüsüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eti yenebilen bir hayvan ölmüştür."},{"facet_id":"F002","role":"specialization","statement":"Hayvan ölmeden önce usulüne uygun kesim gerçekleşmemiştir."}],"identity_rationale":"Kaynak ifadesinin ortak yönü, eti yenebilen bir hayvanın ölümünü usulüne uygun kesimin gerçekleşmemesiyle ilişkilendirir. Ancak toplu aktarımın bir bölümü kesim koşulunu yüzeyde belirsiz bırakırken diğer bölümü kesimin yetişmediğini açıkça söyler; bu nedenle dal yalnızca kesim gerçekleşmeden ölen hayvanla sınırlandırılarak kabul edilebilir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"usulüne uygun kesilmeden ölmüş yenilebilir hayvan"}],"lexicalization_note":"Mekanik kapsam yalındır; tanım yalnızca eti yenebilen hayvanın geçerli kesim olmadan ölmesi anlamını taşır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel hayvan ölümü, geçerli kesim ve boynuzlanarak ölüm arasındaki üç temel sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın gıda uygunluğuna bağlı kesim koşulu kurucudur; komşu dalda yenilebilir tür ve kesimsizlik zorunlu değildir.","focus_only":"Odak dal eti yenebilen hayvanı ve geçerli kesimin gerçekleşmemesini zorunlu kılar.","gloss":"kesimsiz hayvan ölüsü ve genel hayvan ölümü","neighbor_only":"Komşu dal hayvan ölümünü, hayvan ölüsünü ve öldürme buyruğunu daha genel biçimde kapsar.","neighbor_ref":"root_001568/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da ölmüş hayvanı veya hayvanın ölüm durumunu anlatabilir."},{"boundary_match":"opposed","distinction":"Odak dal kesimin yetişmediği kutuptadır; komşu dal ise canlılık sürerken uygun kesimin tamamlandığı karşıt kutuptadır.","focus_only":"Odak dalda hayvan ölmeden önce geçerli kesim tamamlanmamıştır.","gloss":"kesimsiz ölüm ve geçerli kesim","neighbor_only":"Komşu dalda hayvan canlılık belirtisi taşırken kesim tamamlanır ve ölüm bu işlemle gerçekleşir.","neighbor_ref":"root_000517/B003","relation_type":"polarity_pair","shared_zone":"İki dal da eti yenebilen hayvanın ölümü ile kesim arasındaki ilişkiyi belirler."},{"boundary_match":"partial","distinction":"Odak dal kesim durumuna göre genel bir sonuç sınıfıdır; komşu dal ise ölümün boynuz darbesinden kaynaklanmasını zorunlu kılar.","focus_only":"Odak dal ölüm nedenini sınırlamaz ve kesimsiz ölen yenilebilir hayvanların genel sınıfını verir.","gloss":"kesimsiz hayvan ölüsü ve boynuzlanarak ölen hayvan","neighbor_only":"Komşu dal, özellikle boynuzlanma sonucu ölen koyun veya başka hayvanı adlandırır.","neighbor_ref":"root_001517/B005","relation_type":"near_neighbor","shared_zone":"Boynuzlanıp ölen ve kesilemeyen yenilebilir hayvan iki dalın kapsamına birden girebilir."}],"source_phrase_ar":"الميتة ما مات مما يؤكل لحمه إذا ذكي (maqayis)؛ الميتة ما لم تلحقه الذكاة (sihah)","source_summary":"Toplu kanıt, kavramı eti yenebilen hayvanın ölümü ve geçerli kesimin yetişmemesi çevresinde kurar. Bir aktarımın kesim ifadesindeki yüzey belirsizliği, kesimin gerçekleşmediğini açıkça bildiren sınırla birlikte okunmalıdır.","sources":["MQ","SI"],"what_is_ar":"الميتة مما يؤكل لحمه إذا مات ولم تلحقه الذكاة","what_is_not_ar":"ليست ميتة الحال الحسنة أو القبيحة"},"support_links":[]},{"boundary":"Dal, kesimsiz hayvan ölüsünü veya geçici bilinç bozukluğunu değil, ölümün tek oluşunu ya da biçimini anlatır.","branch_kind":"bare","branch_ref":"root_001454/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","surface_ar":"يَمُوتُ"}],"gloss":"bir kez ölme veya ölüm biçimi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ölüm, sayılabilir tek bir olay veya tek bir gerçekleşme olarak ele alınır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ölüm, iyi veya kötü diye değerlendirilebilen bir oluş biçimi ve durum taşır."}}],"root_ar":"م و ت","root_id":"root_001454","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölümü tek bir olay olarak sayarken ya da nasıl gerçekleştiğini nitelendirirken kullanılır.","boundary_detail":"Dal, kesimsiz hayvan ölüsünü veya geçici bilinç bozukluğunu değil, ölümün tek oluşunu ya da biçimini anlatır.","branch_image_ar":"ميتة الحال وواحدة الموت","concept_gloss":"bir kez ölme veya ölüm biçimi","contextual_glosses":[{"applicability":"Ölümün tek bir gerçekleşmesini sayılabilir olay olarak anlatan bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölümün yalnızca bir kez meydana gelen olay oluşunu korur."},"facet_ids":["F001"],"text":"bir kez ölme","usage_role":"contextual"},{"applicability":"Bir kişinin ölümünün gerçekleşme biçiminin olumlu nitelendiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölümün iyi veya kötü diye nitelenebilen oluş biçimini korur."},"facet_ids":["F002"],"text":"iyi bir biçimde öldü","usage_role":"contextual"}],"definition":"Bir kez meydana gelen ölüm olayı veya bir kişinin ölümünün iyi ya da kötü diye nitelenebilen oluş biçimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ölüm, sayılabilir tek bir olay veya tek bir gerçekleşme olarak ele alınır."},{"facet_id":"F002","role":"extension","statement":"Ölüm, iyi veya kötü diye değerlendirilebilen bir oluş biçimi ve durum taşır."}],"identity_rationale":"Kaynak ifadesi iki yakın fakat ayrı değeri açıkça verir: tek bir ölüm olayı ve ölümün iyi ya da kötü oluşla nitelenebilen biçimi. Dal çerçevesi bu değerleri birbirine indirgemeden aynı dal içinde korur.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ölüm biçimi veya hali"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir kez ölme"}],"lexicalization_note":"Mekanik kapsam yalındır; tanım tek ölüm olayı ile ölümün nitelenebilir biçimini ayrı yüzler olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ölüm çekirdeği ve hızlı ölüm biçimi, dalın olay ve niteleme sınırını en açık gösteren komşulardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal olayın tekliğini ya da nasıl gerçekleştiğini öne çıkarır; komşu dal bu ek bakışlar olmadan ölümün kendisini anlatır.","focus_only":"Odak dal ölümü tek bir olay olarak sayar veya gerçekleşme biçimi bakımından niteler.","gloss":"ölüm olayı, ölüm biçimi ve genel ölüm","neighbor_only":"Komşu dal yaşamın sona ermesi biçimindeki genel ölüm çekirdeğini verir.","neighbor_ref":"root_001454/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da yaşamın sona ermesi olayına dayanır."},{"boundary_match":"field_only","distinction":"Hız, odak dalın zorunlu özelliği değildir; komşu dalda ise ölümün çabuk ve kesin olması temel nitelemedir.","focus_only":"Odak dal her türlü iyi veya kötü ölüm biçimini ve tek ölüm olayını kapsayabilir.","gloss":"ölüm biçimi ve hızlı ölüm","neighbor_only":"Komşu dal yalnızca hızlı ve hemen sonuçlanan ölüm biçimini niteler.","neighbor_ref":"root_000270/B005","relation_type":"same_field","shared_zone":"Her iki dal ölümün nasıl gerçekleştiğine ilişkin bir niteleme taşıyabilir."}],"source_phrase_ar":"الموتة الواحدة من الموت (maqayis)؛ الميتة حال من الموت حسنة أو قبيحة (maqayis)؛ مات فلان ميتة حسنة (sihah)؛ الميتة الحال من أحوال الموت (tahdhib)","source_summary":"Toplu kanıt, bir biçimi ölümün tek gerçekleşmesini sayan ad olarak, diğerini ise ölümün nitelenebilir hali olarak açıklar. İkinci kullanım iyi veya kötü gibi değerlendirmeleri kabul eder.","sources":["MQ","SI","TA"],"what_is_ar":"الموتة الواحدة من الموت والميتة حال من أحوال الموت حسنة أو قبيحة","what_is_not_ar":"ليست الميتة التي لم تلحقها الذكاة ولا جنون الموتة"},"support_links":[]},{"boundary":"Dal gerçek ölümü değil, kişiyi geçici olarak kaplayan ve sonrasında ayılabildiği bir bilinç veya nöbet durumunu anlatır.","branch_kind":"bare","branch_ref":"root_001454/B009","candidate_links":[{"candidate_id":"cand_780eeea0b117a8fdca01","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","surface_ar":"يَمُوتُ"}],"gloss":"ardından ayılınan geçici delilik, nöbet veya baygınlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanı geçici olarak kaplayan bir bilinç veya davranış bozukluğu ortaya çıkar."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Durum deliliğe benzer hal, nöbet veya baygınlık biçiminde gerçekleşebilir."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Etkilenen kişi durumun ardından yeniden ayılır."}}],"root_ar":"م و ت","root_id":"root_001454","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir insanın geçici olarak bilincini veya davranış denetimini yitirip sonra ayıldığı durum için kullanılır.","boundary_detail":"Dal gerçek ölümü değil, kişiyi geçici olarak kaplayan ve sonrasında ayılabildiği bir bilinç veya nöbet durumunu anlatır.","branch_image_ar":"الموتة جنون وغشية","concept_gloss":"ardından ayılınan geçici delilik, nöbet veya baygınlık","contextual_glosses":[{"applicability":"Kişinin geçici bir nöbetten sonra bilincini yeniden kazandığı olay bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geçici nöbeti ve ardından ayılma aşamasını birlikte korur."},"facet_ids":["F001","F002","F003"],"text":"nöbet geçirip yeniden ayıldı","usage_role":"contextual"}],"definition":"Bir insanı geçici olarak etkileyen deliliğe benzer durum, nöbet veya baygınlıktır; kişi bu durumdan sonra yeniden ayılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanı geçici olarak kaplayan bir bilinç veya davranış bozukluğu ortaya çıkar."},{"facet_id":"F002","role":"source_variant","statement":"Durum deliliğe benzer hal, nöbet veya baygınlık biçiminde gerçekleşebilir."},{"facet_id":"F003","role":"core","statement":"Etkilenen kişi durumun ardından yeniden ayılır."}],"identity_rationale":"Kaynak ifadesi kişiyi geçici olarak etkileyen deliliğe benzer durum, nöbet veya baygınlığı ve ardından ayılmayı birlikte verir. Dal çerçevesi bu geçici oluşu ölümden ve yer adından ayırarak doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ardından ayılınan delilik benzeri hal, nöbet veya baygınlık"}],"lexicalization_note":"Mekanik kapsam yalındır; tanım geçici delilik, nöbet veya baygınlık halini ve ardından ayılmayı içerir.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; baygınlık ve nöbet hastalığı komşuları, geçicilik ve sonradan ayılma sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kapsamı delilik benzeri davranış ve nöbete uzanır ve ayılmayla kapanır; komşu dalın çekirdeği bilincin örtülmesidir.","focus_only":"Odak dal deliliğe benzer hal ve nöbeti de kapsar, ayrıca sonradan ayılmayı açıkça gerektirir.","gloss":"geçici nöbet ve baygınlık","neighbor_only":"Komşu dal bilinci örten baygınlığı ve ölüm sırasında gelen ağır bayılmayı özellikle kapsar.","neighbor_ref":"root_001088/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin bilincini geçici olarak örten baygınlık halinde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal tekil ve geçici bir durum alanıdır; komşu dal ise nöbeti süreklilik gösterebilen bir hastalık olarak adlandırır.","focus_only":"Odak dal baygınlık ve deliliğe benzer geçici hali de kapsar ve ayılma sonucunu belirtir.","gloss":"geçici nöbet hali ve nöbet hastalığı","neighbor_only":"Komşu dal nöbeti bilinen bir hastalık olarak ele alır ve nöbetli kişiye ilişkin ayrı bir niteleme içerir.","neighbor_ref":"root_000859/B002","relation_type":"near_synonym","shared_zone":"İnsanın yere düşmesine veya bilincini yitirmesine yol açan nöbet iki dalda da bulunur."}],"source_phrase_ar":"الموتة شبه الجنون يعترى الإنسان (maqayis)؛ الموتة جنس من الجنون والصرع يعتري الإنسان (sihah)؛ الموتة الجنون (tahdhib)؛ الموتة الذي يصرع من الجنون أو غيره ثم يفيق (tahdhib)؛ الموتة شبه الغشية (tahdhib)","source_summary":"Kaynaklar, kişiyi etkileyen bu durumu deliliğe benzer hal, nöbet ve baygınlık çevresinde ortaklaştırır. Toplu aktarım, durumun geçici olmasını ve etkilenen kişinin daha sonra ayılmasını sınırın önemli bir parçası yapar.","sources":["MQ","SI","TA"],"what_is_ar":"الموتة جنس من الجنون والصرع والغشية يعترى الإنسان ثم يفيق","what_is_not_ar":"ليست مؤتة اسم الأرض"},"support_links":["sup_cd95784aa9d134d8bfb8"]},{"boundary":"Dal gerçek bir kendini verme ve ölümü göze alma durumudur; yapmacık ölüm veya gösteriş içermez.","branch_kind":"collocation","branch_ref":"root_001454/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","surface_ar":"يَمُوتُ"}],"gloss":"bir işe kendini bütünüyle verme; savaşta ölümü göze alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi belirli bir işe kendini bütünüyle bırakır ve çekinmeden yönelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Savaşta kişi ölümü önemsemeden sonuna kadar dövüşür."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişi ölümü gönüllü ve hazır bir ruh haliyle karşılar."}}],"root_ar":"م و ت","root_id":"root_001454","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca verilen iş ve savaş kalıplarında, çekinmeden kendini adama veya ölümü önemsememe anlamında kullanılır.","boundary_detail":"Dal gerçek bir kendini verme ve ölümü göze alma durumudur; yapmacık ölüm veya gösteriş içermez.","branch_image_ar":"استماتة في الأمر والموت","concept_gloss":"bir işe kendini bütünüyle verme; savaşta ölümü göze alma","contextual_glosses":[{"applicability":"Kişinin savaşta ölümden çekinmeden sonuna kadar dövüştüğü bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Savaş katılımcısını, ölüm kaygısının yokluğunu ve dövüşme eylemini korur."},"facet_ids":["F002","F003"],"text":"savaşta ölümü göze alarak dövüştü","usage_role":"contextual"}],"definition":"Belirli bir işe kendini bütünüyle bırakmak ve ona çekinmeden yönelmektir. Savaş bağlamında ölümü önemsemeden dövüşmeyi ve ölümü gönüllü karşılamayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi belirli bir işe kendini bütünüyle bırakır ve çekinmeden yönelir."},{"facet_id":"F002","role":"specialization","statement":"Savaşta kişi ölümü önemsemeden sonuna kadar dövüşür."},{"facet_id":"F003","role":"extension","statement":"Kişi ölümü gönüllü ve hazır bir ruh haliyle karşılar."}],"identity_rationale":"Kaynak ifadesi bir işe kendini bütünüyle bırakmayı, savaşta ölümü önemsemeden dövüşmeyi ve ölümü gönüllü karşılamayı aynı kendini adama çizgisinde verir. Dal çerçevesi bu kullanımları sahte ölüm veya gösterişçi alçakgönüllülükten doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"işe kendini bütünüyle veren"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"savaşta ölümü göze alarak dövüşen"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"ölümü gönüllü karşıladı"}],"lexicalization_note":"Mekanik kapsam yalnızca verilen kalıplara bağlıdır; bir işe kendini bırakma ve savaşta ölümü göze alma anlamları yalın köke genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kendini ölüme atarcasına çabalama, tehlikeye girme ve kesin karar verme en yararlı üç sınırı sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal odaktaki savaş uzmanlaşmasına çok yakındır; odak dal ise savaş dışı işe bağlanma ve ölümü gönüllü kabul etme kapsamlarına da sahiptir.","focus_only":"Odak dal bir işe kendini bırakmayı ve ölümü gönüllü karşılamayı da kapsar.","gloss":"kendini adama ve kendini ölüme atarcasına çabalama","neighbor_only":"Komşu dal yalnızca kişinin kendini ölüme atarcasına çabalamasını adlandıran dar bir kullanımdır.","neighbor_ref":"root_001200/B012","relation_type":"near_synonym","shared_zone":"Her iki dal da tehlike karşısında kendini sakınmadan bütünüyle ortaya koymayı anlatır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği kendini bütünüyle verme ve ölüm kaygısını bırakmadır; komşu dalın çekirdeği tehlikenin içine atılmaktır.","focus_only":"Odak dal belirli bir işe kendini bırakmayı ve ölümü içtenlikle kabul etmeyi içerir.","gloss":"ölümü göze alma ve tehlikeye atılma","neighbor_only":"Komşu dal tehlikeye ve savaşa gözü kapalı dalmayı, sonuçlara aldırmamayı öne çıkarır.","neighbor_ref":"root_001105/B006","relation_type":"near_synonym","shared_zone":"Her iki dalda da kişi ölüm tehlikesine rağmen savaşa veya güç işe girer."},{"boundary_match":"partial","distinction":"Karar verme eylemden önceki zihinsel bağlanmadır; odak dal ise kişinin kendisini fiilen işe veya ölüm tehlikesine bırakmasını anlatır.","focus_only":"Odak dal kendini eyleme bırakmayı ve kimi bağlamlarda ölümü göze almayı gerektirir.","gloss":"kendini verme ve kesin karar","neighbor_only":"Komşu dal karar verme, kararı kesinleştirme ve tereddütsüz kalma zihinsel aşamasını anlatır.","neighbor_ref":"root_001010/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin bir işe tereddütsüz yönelmesini destekleyebilir."}],"source_phrase_ar":"المستميت للأمر المسترسل له (maqayis;sihah)؛ المستميت المستقتل الذي لا يبالي في الحرب من الموت (sihah)؛ استمات الرجل إذا طاب نفسا بالموت (tahdhib)؛ المستميت الذي يقاتل على الموت (tahdhib)","source_summary":"Kaynakların ortak çizgisi, kişinin bir işe kendini bırakması ve savaşta ölüm kaygısını geride bırakarak dövüşmesidir. Toplu aktarım bunu ölümü içtenlikle kabul etmeye kadar genişletir.","sources":["MQ","SI","TA"],"what_is_ar":"المستميت للأمر المسترسل له والمستقتل الذي لا يبالي بالموت ومن طابت نفسه بالموت","what_is_not_ar":"ليس المتماوت المرائي ولا المتجان"},"support_links":[]},{"boundary":"Dal gerçek ölüm, delilik veya içten alçakgönüllülük değil, bunların çıkar ya da gösteriş için taklit edilmesidir.","branch_kind":"bare","branch_ref":"root_001454/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","surface_ar":"يَمُوتُ"}],"gloss":"ölmüş, deli veya alçakgönüllüymüş gibi davranma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi gerçekte taşımadığı bir durumu başkalarına varmış gibi gösterir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Canlı kişi, bir darbeye karşı ölmüş gibi davranabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gösteri, sahte delilik veya yiyecek elde etmek için yapmacık alçakgönüllülük biçimini alabilir."}}],"root_ar":"م و ت","root_id":"root_001454","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gerçekte bulunmayan ölüm, delilik veya alçakgönüllülük halinin çıkar ya da gösteriş için sergilendiği durumda kullanılır.","boundary_detail":"Dal gerçek ölüm, delilik veya içten alçakgönüllülük değil, bunların çıkar ya da gösteriş için taklit edilmesidir.","branch_image_ar":"إظهار الموت والخشوع كذبا","concept_gloss":"ölmüş, deli veya alçakgönüllüymüş gibi davranma","contextual_glosses":[{"applicability":"Canlı bir kişinin darbe sonrasında ölmüş gibi göründüğü olay bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin canlı olmasını ve bilinçli biçimde ölü görünmesini birlikte korur."},"facet_ids":["F001","F002"],"text":"ölmüş numarası yaptı","usage_role":"contextual"}],"definition":"Gerçekte bulunmayan bir hali çıkar veya gösteriş için varmış gibi sergilemektir; kişi ölü, deli ya da aşırı alçakgönüllü görünmeye çalışabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi gerçekte taşımadığı bir durumu başkalarına varmış gibi gösterir."},{"facet_id":"F002","role":"example","statement":"Canlı kişi, bir darbeye karşı ölmüş gibi davranabilir."},{"facet_id":"F003","role":"extension","statement":"Gösteri, sahte delilik veya yiyecek elde etmek için yapmacık alçakgönüllülük biçimini alabilir."}],"identity_rationale":"Kaynak ifadesi gerçekte canlıyken ölü görünmeyi, gerçekte deli değilken deli gibi davranmayı ve çıkar için yapmacık alçakgönüllülük göstermeyi birlikte aktarır. Dal çerçevesi bunları gerçek savaş kararlılığından ayıran ortak sahtelik çekirdeğini doğru yakalar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"gösteriş için aşırı alçakgönüllü görünen"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"canlıyken ölmüş gibi davrandı"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"deli veya alçakgönüllüymüş gibi davranan"}],"lexicalization_note":"Mekanik kapsam yalındır; tanım sahte ölüm, sahte delilik ve gösterişçi alçakgönüllülük biçimlerini aynı davranış alanında tutar.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel gösteriş, yapmacık ağlama ve ikiyüzlülük sahtelik çekirdeğinin üç ayrı sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir halin taklididir; komşu dal ise yapılan herhangi bir işin görülme ve ün kazanma amacıyla yapılmasını anlatır.","focus_only":"Odak dal ölüm, delilik veya alçakgönüllülük gibi belirli sahte durumları sergilemeyi içerir.","gloss":"sahte hal gösterisi ve gösteriş","neighbor_only":"Komşu dal herhangi bir işi insanların görmesi veya duyması için yapma amacını genel olarak kapsar.","neighbor_ref":"root_000531/B005","relation_type":"near_synonym","shared_zone":"Her iki dalda kişi başkalarının algısını yönlendirmek amacıyla gerçek dışı veya abartılı bir görünüm sunar."},{"boundary_match":"partial","distinction":"Odak dalın görünüm türleri ölüm, delilik ve alçakgönüllülüktür; komşu dal yalnızca ağlamanın yapmacık biçimde üretilmesine bağlıdır.","focus_only":"Odak dal ölüm, delilik ve alçakgönüllülük taklitlerini kapsar.","gloss":"ölü numarası ve ağlama numarası","neighbor_only":"Komşu dal yalnızca doğal gelmeyen ağlama davranışını zorlayarak göstermeyi anlatır.","neighbor_ref":"root_000147/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalda gerçekte doğal biçimde bulunmayan bir durum davranışla taklit edilir."},{"boundary_match":"partial","distinction":"Odak dal belirli bir anlık görünümün taklididir; komşu dal ise inanç ve davranış arasındaki gizli karşıtlığı temel alan daha geniş bir tutumdur.","focus_only":"Odak dal belirli bir bedensel veya davranışsal hali doğrudan taklit eder.","gloss":"sahte durum gösterisi ve ikiyüzlülük","neighbor_only":"Komşu dal kişinin içindeki inanç veya niyetin tersini dışarıya gösterdiği süreğen ikili tutumu anlatır.","neighbor_ref":"root_001537/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalda dışarıya sunulan görünüm kişinin gerçek durumuyla uyuşmaz."}],"source_phrase_ar":"المتماوت من صفة الناسك المرائي (sihah)؛ المستميت الذي يتجان وليس بمجنون (tahdhib)؛ يتخاشع ويتواضع لهذا حتى يطعمه (tahdhib)؛ ضربته فتماوت إذا أرى أنه ميت وهو حي (tahdhib)؛ المتماوتون المراءون (tahdhib)","source_summary":"Toplu kanıtın ortak çekirdeği, gerçekte olmayan bir hali bilinçli olarak sergilemektir. Aktarımlar ölü numarası yapmayı, deli görünmeyi ve başkasından çıkar sağlamak amacıyla aşırı alçakgönüllü davranmayı bu çekirdeğin örnekleri olarak verir.","sources":["SI","TA"],"what_is_ar":"التماوت بإراءة أنه ميت وهو حي والمتماوت أو المستميت المرائي المتخاشع والمتجانس وليس بمجنون","what_is_not_ar":"ليس الاستماتة في القتال ولا الخضوع للحق"},"support_links":[]},{"boundary":"Dal gerçek yaşam kaybı değil, yalnızca verilen rüzgâr, kumaş ve uyku kalıplarındaki durgunluk veya yıpranmadır.","branch_kind":"collocation","branch_ref":"root_001454/B012","candidate_links":[{"candidate_id":"cand_7f508cf16e323ad37129","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","surface_ar":"يَمُوتُ"}],"gloss":"rüzgârın dinmesi, kumaşın eskimesi veya insanın uyuması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Rüzgâr hareketini yitirir ve diner."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kumaş kullanımla yıpranır ve eskir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsan uyur ve hareketsiz bir duruma geçer."}}],"root_ar":"م و ت","root_id":"root_001454","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca verilen rüzgâr, kumaş ve insan kalıplarında üç ayrı sonucu temsil eder.","boundary_detail":"Dal gerçek yaşam kaybı değil, yalnızca verilen rüzgâr, kumaş ve uyku kalıplarındaki durgunluk veya yıpranmadır.","branch_image_ar":"سكون وخمود كنوم أو بلى","concept_gloss":"rüzgârın dinmesi, kumaşın eskimesi veya insanın uyuması","contextual_glosses":[{"applicability":"Rüzgârın hareketini yitirip bütünüyle sakinleştiği özel kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Rüzgâr katılımcısını ve hareketin sona ermesi sonucunu korur."},"facet_ids":["F001"],"text":"rüzgâr dindi","usage_role":"contextual"},{"applicability":"Bir kumaşın kullanımla yıpranıp eski hale geldiği özel kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kumaş katılımcısını ve yıpranarak eskime sonucunu korur."},"facet_ids":["F002"],"text":"kumaş eskidi","usage_role":"contextual"},{"applicability":"Bir insanın uykuya geçip hareketsizleştiği özel kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan katılımcısını ve ölüm değil uyku olan sonucu korur."},"facet_ids":["F003"],"text":"adam uyudu","usage_role":"contextual"}],"definition":"Yalnızca belirli kalıplarda rüzgârın dinmesini, kumaşın yıpranmasını veya insanın uyuyup hareketsizleşmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Rüzgâr hareketini yitirir ve diner."},{"facet_id":"F002","role":"specialization","statement":"Kumaş kullanımla yıpranır ve eskir."},{"facet_id":"F003","role":"specialization","statement":"İnsan uyur ve hareketsiz bir duruma geçer."}],"identity_rationale":"Kaynak ifadesi ölüm sözünü üç kalıba bağlı mecazlı sonuç için kullanır: rüzgârın dinmesi, kumaşın eskimesi ve insanın uyuyup hareketsizleşmesi. Dal çerçevesi bu kullanımları gerçek canlı ölümünden ayırarak doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"rüzgâr dindi"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"kumaş eskidi ve yıprandı"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"adam uyudu ve hareketsizleşti"}],"lexicalization_note":"Mekanik kapsam yalnızca verilen üç kalıba bağlıdır; durma, eskime ve uyuma anlamları yalın ölüm anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; rüzgârın dinmesi, doğrudan uyku ve kumaş yıpranması üç kalıba özgü sınırları ayrı ayrı açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme yalnızca rüzgâr bağlamındadır; odak dalın öteki iki kalıbı komşuda yoktur, komşunun su ve ısı kapsamı da odakta yoktur.","focus_only":"Odak dal rüzgârın dinmesi yanında kumaşın eskimesi ve insanın uyuması kalıplarını da içerir.","gloss":"rüzgârın dinmesi ve hareketin yatışması","neighbor_only":"Komşu dal rüzgâra ek olarak suyun, gecenin ve ısının yatışmasını doğrudan durgunluk alanında kapsar.","neighbor_ref":"root_000725/B004","relation_type":"near_synonym","shared_zone":"Rüzgârın hareketini yitirip sakinleşmesi iki dalda da aynı sonucu verir."},{"boundary_match":"partial","distinction":"Odak dalda uyku, ölüm sözünün belirli bir kalıptaki aktarımıdır; komşu dalın bağımsız çekirdeği doğrudan uyku ve dinlenmedir.","focus_only":"Odak dal uyku dışında rüzgârın dinmesi ve kumaşın eskimesini de içerir.","gloss":"uyuma ve ölüm görüntüsüyle uyuma","neighbor_only":"Komşu dal uykuyu ve dinlenme halini doğrudan, çeşitli ad ve eylem biçimleriyle anlatır.","neighbor_ref":"root_000585/B001","relation_type":"near_synonym","shared_zone":"Bir insanın uykuya geçmesi ve hareketsiz kalması iki dalda da örtüşür."},{"boundary_match":"partial","distinction":"Odak dalda eskime yalnızca üç kalıptan biridir; komşu dal kumaş yıpranmasını bağımsız ve daha ayrıntılı bir çekirdek olarak işler.","focus_only":"Odak dal kumaş eskimesi yanında rüzgâr ve insan kalıplarına da sahiptir.","gloss":"kumaşın eskimesi ve yıpranması","neighbor_only":"Komşu dal kumaşın tüyünü yitirmesi, yırtılması ve kullanım izleriyle eskimesini ayrıntılı biçimde kapsar.","neighbor_ref":"root_000434/B009","relation_type":"near_synonym","shared_zone":"Kumaşın kullanımla eskiyip yıpranması iki dalda da örtüşür."}],"source_phrase_ar":"الموت السكون (tahdhib)؛ ماتت الريح إذا سكنت (tahdhib)؛ مات الثوب ونام إذا بلي (tahdhib)؛ مات الرجل وهمد وهوم إذا نام (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek aktarım, rüzgâr için dinmeyi, kumaş için eskimeyi ve insan için uyumayı aynı ölüm görüntüsüne bağlı özel kullanımlar olarak verir."}],"source_summary":"Ortak bir çoklu kaynak özeti yoktur; dalın üç kalıba bağlı durgunluk, yıpranma ve uyku değerleri tek bir sözlük aktarımına dayanır.","sources":["TA"],"what_is_ar":"موت الريح إذا سكنت وموت الرجل إذا نام وموت الثوب إذا بلي","what_is_not_ar":"ليس مفارقة الروح ولا موت الحيوان"},"support_links":["sup_2126fdd8be499654fbb9"]},{"boundary":"Dal yalnızca gerçeğe boyun eğme kalıbıdır; ölüm veya sahte alçakgönüllülük anlamı taşımaz.","branch_kind":"collocation","branch_ref":"root_001454/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","surface_ar":"يَمُوتُ"}],"gloss":"gerçeğe boyun eğme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi gerçeğe boyun eğer ve ona karşı direncini bırakır."}}],"root_ar":"م و ت","root_id":"root_001454","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kişinin gerçeği kabul edip direnmeyi bıraktığını bildiren verilen kalıpta kullanılır.","boundary_detail":"Dal yalnızca gerçeğe boyun eğme kalıbıdır; ölüm veya sahte alçakgönüllülük anlamı taşımaz.","branch_image_ar":"الخضوع للحق","concept_gloss":"gerçeğe boyun eğme","contextual_glosses":[{"applicability":"Kişinin gerçeği kabul ederek karşı koymayı bıraktığı cümle bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin gerçeği kabul edip ona boyun eğmesi anlamını doğal yüklemle korur."},"facet_ids":["F001"],"text":"gerçeğe boyun eğdi","usage_role":"contextual"}],"definition":"Belirli kişi kalıbında, kişinin gerçeği kabul ederek ona boyun eğmesi ve direnmeyi bırakmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi gerçeğe boyun eğer ve ona karşı direncini bırakır."}],"identity_rationale":"Kaynak ifadesi belirli kişi kalıbını doğrudan doğruya gerçeğe boyun eğmek olarak açıklar. Dal çerçevesi bu kullanımı beden ölümünden ve gösterişçi alçakgönüllülükten ayırarak eksiksiz korur.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"adam gerçeğe boyun eğdi"}],"lexicalization_note":"Mekanik kapsam tek bir kişi kalıbına bağlıdır; gerçeğe boyun eğme anlamı yalın köke veya başka kullanımlara genellenmez.","neighbor_coverage_note":"Bütün adaylar incelendi; baskı altında kabul ve genel alçakgönüllülük, gerçeğe bağlı boyun eğmenin sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalın kabul ve boyun eğmedir; komşu dal bunu baskı altında, isteksizce veya buyruğa uyma biçiminde sınırlayabilir.","focus_only":"Odak dal gerçeğe boyun eğmeyi bildirir, baskı veya isteksizlik koşulu koymaz.","gloss":"gerçeğe boyun eğme ve baskı altında kabul","neighbor_only":"Komşu dal gerçeği kabul etme yanında baskı, sertlik, isteksizlik ve buyruğa uyma koşullarını da içerebilir.","neighbor_ref":"root_000088/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin gerçeği kabul edip direnmeyi bırakması durumunda örtüşür."},{"boundary_match":"partial","distinction":"Odak dal doğruluk karşısındaki kabul ilişkisidir; komşu dalın çekirdeği ise iç veya dış alçakgönüllülük ve sakinliktir.","focus_only":"Odak dalın yöneldiği nesne gerçektir ve kişinin onu kabul etmesi gerekir.","gloss":"gerçeği kabul etme ve alçakgönüllülük","neighbor_only":"Komşu dal baş eğme, bakışı indirme, sesi kısma ve bedensel alçalma gibi dış belirtileri kapsar.","neighbor_ref":"root_000412/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da direnç azalır ve kişi kendini aşağı veya uysal bir konuma getirir."}],"source_phrase_ar":"مات الرجل إذا خضع للحق (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek aktarım, kişi kalıbını ölüm değil gerçeği kabul edip ona boyun eğme anlamında açıklar."}],"source_summary":"Ortak bir çoklu kaynak özeti yoktur; gerçeğe boyun eğme anlamı tek bir sözlük aktarımında ve tek bir kişi kalıbında verilir.","sources":["TA"],"what_is_ar":"مات الرجل إذا خضع للحق","what_is_not_ar":"ليس موت الجسد ولا التماوت المرائي"},"support_links":[]},{"boundary":"Dal vurulmuş avın ölüm durumunu sonradan belirlemeye yöneliktir; avı vurma veya öldürme eylemi değildir.","branch_kind":"collocation","branch_ref":"root_001454/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","surface_ar":"يَمُوتُ"}],"gloss":"vurulmuş avın ölüp ölmediğini inceleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Av hayvanı önceden vurulmuştur ve ölüp ölmediği belirsizdir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi avı inceleyerek ölü olup olmadığını belirler."}}],"root_ar":"م و ت","root_id":"root_001454","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca önceden vurulmuş bir av hayvanının ölüm durumu kuşkulu olduğunda yapılan denetim için kullanılır.","boundary_detail":"Dal vurulmuş avın ölüm durumunu sonradan belirlemeye yöneliktir; avı vurma veya öldürme eylemi değildir.","branch_image_ar":"استبانة موت الصيد","concept_gloss":"vurulmuş avın ölüp ölmediğini inceleme","contextual_glosses":[{"applicability":"Vurulmuş avın ölüm durumunun kuşkulu olduğu bir buyruğu doğal Türkçeyle aktarır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Av katılımcısını, ölüm kuşkusunu ve denetleme buyruğunu eksiksiz korur."},"facet_ids":["F001","F002"],"text":"avınızın ölüp ölmediğini kontrol edin","usage_role":"contextual"}],"definition":"Vurulmuş bir av hayvanının ölüp ölmediğinden kuşkulanıldığında onu inceleyerek ölüm durumunu belirlemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Av hayvanı önceden vurulmuştur ve ölüp ölmediği belirsizdir."},{"facet_id":"F002","role":"core","statement":"Kişi avı inceleyerek ölü olup olmadığını belirler."}],"identity_rationale":"Kaynak ifadesi vurulmuş bir av hayvanının ölüp ölmediğinden kuşkulanıldığında durumunu incelemeyi açıkça emreder. Dal çerçevesi bunu avı ilk kez öldürmekten ve savaşta ölümü göze almaktan doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"avınızın ölüp ölmediğine bakın"}],"lexicalization_note":"Mekanik kapsam yalnızca verilen av buyruğuna bağlıdır; ölüm durumunu denetleme anlamı yalın köke genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel kuşku, kesimi tamamlama ve atışla ilgili av kartları denetleme eyleminin sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir kuşkuyu eylemle çözmeye yöneliktir; komşu dal nesnesi ve çözüm işlemi sınırlanmamış genel kuşku durumudur.","focus_only":"Odak dal kuşkuyu vurulmuş bir avın ölüm durumuna bağlar ve inceleyerek çözmeyi gerektirir.","gloss":"avın ölümünü denetleme ve genel kuşku","neighbor_only":"Komşu dal iki olasılık arasında kesinliğin kurulamamasını genel bir zihinsel durum olarak anlatır.","neighbor_ref":"root_000812/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda iki olasılık arasında kesinlik yoktur."},{"boundary_match":"partial","distinction":"Odak dal bilgi edinme ve durum belirleme işlemidir; komşu dal ise kesim yoluyla ölümü gerçekleştiren fiziksel işlemdir.","focus_only":"Odak dal vurulmuş avın zaten ölü olup olmadığını sonradan belirler.","gloss":"ölümü denetleme ve kesimi tamamlama","neighbor_only":"Komşu dal canlılık belirtisi süren hayvanın kesimini tamamlayarak ölüm sonucunu meydana getirir.","neighbor_ref":"root_000517/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir hayvanın canlılık durumu ve ölümü değerlendirilir."},{"boundary_match":"thematic_only","distinction":"Anlamsal çekirdekler örtüşmez: odak dal ölüm denetimidir, komşu dal ise atış aracı veya atış sonucu elde edilen avdır.","focus_only":"Odak dal vurulmuş hayvanın ölüm durumunu inceleyen sonraki aşamayı anlatır.","gloss":"vurulmuş avın denetimi ve atışla ilgili av","neighbor_only":"Komşu dal atışta kullanılan araçları veya atışla yere düşürülen avı adlandırır.","neighbor_ref":"root_000603/B003","relation_type":"thematic","shared_zone":"İki dal aynı av ve atış sahnesinde art arda yer alabilir."}],"source_phrase_ar":"استميتوا صيدكم أي انظروا مات أم لا (tahdhib)؛ إذا أصيب فشك في موته (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek aktarım, vurulmuş ve ölümü kuşkulu avın incelenerek ölüp ölmediğinin belirlenmesini bildirir."}],"source_summary":"Ortak bir çoklu kaynak özeti yoktur; vurulmuş avın ölüm durumunu kuşku üzerine inceleme anlamı tek bir sözlük aktarımına dayanır.","sources":["TA"],"what_is_ar":"استميتوا صيدكم أي انظروا مات أم لا إذا أصيب وشك في موته","what_is_not_ar":"ليس قتل الصيد ابتداء ولا الاستماتة في القتال"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["87:13:1"],"branch_refs":[],"candidate_id":"cand_51a52a0da1453b0607e5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:1:boundary-and-rhythm","source_type":"word_analysis","support_ids":["sup_0f50ee95fc54e11b5d44","sup_43fda457d2a7a74aed65"],"title":"boundary into interior stasis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:1","qac_refs":["87:13:1:1"],"status":"accepted"}},{"anchor_refs":["87:13:1"],"branch_refs":[],"candidate_id":"cand_72f7a123b8da8fc1a03a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:1:scope-over-paired-negation","source_type":"word_analysis","support_ids":["sup_0f50ee95fc54e11b5d44","sup_f5e3955da6a9f8c62fb0"],"title":"scope over the full neither-nor frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:1","qac_refs":["87:13:1:1"],"status":"accepted"}},{"anchor_refs":["87:13:1"],"branch_refs":[],"candidate_id":"cand_ea1e4c5ef57d43cde31a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:1:sequenced-escalation-after-fire","source_type":"word_analysis","support_ids":["sup_0f50ee95fc54e11b5d44","sup_93164c26948c7866937e"],"title":"later stage after fire-contact","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:1","qac_refs":["87:13:1:1"],"status":"accepted"}},{"anchor_refs":["87:13:2"],"branch_refs":[],"candidate_id":"cand_2dd5482e9ed4a8b53e9f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:2:descriptive-not-prohibitive","source_type":"word_analysis","support_ids":["sup_c6a2b094a38d8f88d674","sup_ce830c840e4d20c313d8"],"title":"condition, not prohibition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:2","qac_refs":["87:13:2:1"],"status":"accepted"}},{"anchor_refs":["87:13:2"],"branch_refs":[],"candidate_id":"cand_273a62c9e10524f05c09","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:2:first-negation-denies-death","source_type":"word_analysis","support_ids":["sup_c6a2b094a38d8f88d674","sup_ffd5b6e74c0d31184c6a"],"title":"death denied as first endpoint","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:2","qac_refs":["87:13:2:1"],"status":"accepted"}},{"anchor_refs":["87:13:2"],"branch_refs":[],"candidate_id":"cand_109a31255cdbac295147","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:2:opening-neither-nor-pulse","source_type":"word_analysis","support_ids":["sup_4861cd844ca1bc14c85e","sup_c6a2b094a38d8f88d674"],"title":"first beat of double closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:2","qac_refs":["87:13:2:1"],"status":"accepted"}},{"anchor_refs":["87:13:3"],"branch_refs":[],"candidate_id":"cand_262932607f0ca8c11ed5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001454"],"scope":"focus_ayah","source_local_id":"87:13:3:death-life-anti-cycle","source_type":"word_analysis","support_ids":["sup_15edd6d9b9a627786f39","sup_9cf8ef00d999b4087897"],"title":"death-life pair becomes anti-cycle","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:3","qac_refs":["87:13:3:1"],"status":"accepted"}},{"anchor_refs":["87:13:3"],"branch_refs":[],"candidate_id":"cand_cb4c2552aaf88a140205","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001454"],"scope":"focus_ayah","source_local_id":"87:13:3:formula-and-context-expansion","source_type":"word_analysis","support_ids":["sup_9cf8ef00d999b4087897","sup_c0ea7f09363f512c4024"],"title":"known punishment formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:3","qac_refs":["87:13:3:1"],"status":"accepted"}},{"anchor_refs":["87:13:3"],"branch_refs":[],"candidate_id":"cand_23b5e68bfa2fc066f0c2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001454"],"scope":"focus_ayah","source_local_id":"87:13:3:imperfect-death-withheld","source_type":"word_analysis","support_ids":["sup_6f940f9c1c49a8ede8ca","sup_9cf8ef00d999b4087897"],"title":"death continually unrealized","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:3","qac_refs":["87:13:3:1"],"status":"accepted"}},{"anchor_refs":["87:13:3"],"branch_refs":[],"candidate_id":"cand_c2250dfc113263f23f81","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001454"],"scope":"focus_ayah","source_local_id":"87:13:3:objectless-own-death-denied","source_type":"word_analysis","support_ids":["sup_8aaa2ca21e250e4dbde5","sup_9cf8ef00d999b4087897"],"title":"subject's own death-event denied","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:3","qac_refs":["87:13:3:1"],"status":"accepted"}},{"anchor_refs":["87:13:3"],"branch_refs":[],"candidate_id":"cand_f4f1ab4a25be2996dd9e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001454"],"scope":"focus_ayah","source_local_id":"87:13:3:root-field-narrowed-to-basic-death","source_type":"word_analysis","support_ids":["sup_28c6937d1c6a0992eee7","sup_9cf8ef00d999b4087897"],"title":"death field narrowed to dying endpoint","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:3","qac_refs":["87:13:3:1"],"status":"accepted"}},{"anchor_refs":["87:13:3"],"branch_refs":[],"candidate_id":"cand_847093aeff75b9b3574c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001454"],"scope":"focus_ayah","source_local_id":"87:13:3:sound-and-sequence-pairing","source_type":"word_analysis","support_ids":["sup_0871fbecac256783f8e9","sup_9cf8ef00d999b4087897"],"title":"formal echo before semantic split","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:3","qac_refs":["87:13:3:1"],"status":"accepted"}},{"anchor_refs":["87:13:4"],"branch_refs":[],"candidate_id":"cand_9aa5a11bc58bc576e04a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:4:fire-pronoun-recall","source_type":"word_analysis","support_ids":["sup_06f37b8c3bd57242ec87","sup_bb88da866c109ea26575"],"title":"feminine suffix recalls the fire","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:4","qac_refs":["87:13:4:1","87:13:4:2"],"status":"accepted"}},{"anchor_refs":["87:13:4"],"branch_refs":[],"candidate_id":"cand_49cc3028a6ae2a50a047","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:4:fused-form-and-cadence","source_type":"word_analysis","support_ids":["sup_504ff3fd9f139cc24844","sup_bb88da866c109ea26575"],"title":"fused containment and long-ā link","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:4","qac_refs":["87:13:4:1","87:13:4:2"],"status":"accepted"}},{"anchor_refs":["87:13:4"],"branch_refs":[],"candidate_id":"cand_864f7636db72ad5c5788","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:4:greater-fire-specified","source_type":"word_analysis","support_ids":["sup_b965dfcb28c835e58b3d","sup_bb88da866c109ea26575"],"title":"greater fire specified as suspended existence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:4","qac_refs":["87:13:4:1","87:13:4:2"],"status":"accepted"}},{"anchor_refs":["87:13:4"],"branch_refs":[],"candidate_id":"cand_82b12ce7d4c2cec290e2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:4:medial-pivot-between-opposites","source_type":"word_analysis","support_ids":["sup_bb88da866c109ea26575","sup_f0ec8bcf4f726e48bbc6"],"title":"locative hinge in the antithesis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:4","qac_refs":["87:13:4:1","87:13:4:2"],"status":"accepted"}},{"anchor_refs":["87:13:4"],"branch_refs":[],"candidate_id":"cand_26c8129acf0f8ab62972","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:4:shared-containment-domain","source_type":"word_analysis","support_ids":["sup_bb88da866c109ea26575","sup_de0cbc0bb311579f06ea"],"title":"one container for both denials","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:4","qac_refs":["87:13:4:1","87:13:4:2"],"status":"accepted"}},{"anchor_refs":["87:13:5"],"branch_refs":[],"candidate_id":"cand_884591a6ffd4beb13c7c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:5:binds-opposite-predicates","source_type":"word_analysis","support_ids":["sup_289f2c7f1ecfc16fb454","sup_2f1c1974c0f43c5e86e5"],"title":"opposites bound under one frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:5","qac_refs":["87:13:5:1"],"status":"accepted"}},{"anchor_refs":["87:13:5"],"branch_refs":[],"candidate_id":"cand_1072934b63a4194da175","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:5:completion-and-cadence","source_type":"word_analysis","support_ids":["sup_09f307b99ed5a72e66ea","sup_2f1c1974c0f43c5e86e5"],"title":"linked completion of the refrain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:5","qac_refs":["87:13:5:1"],"status":"accepted"}},{"anchor_refs":["87:13:5"],"branch_refs":[],"candidate_id":"cand_e3211527a0568905117a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:5:coordinated-second-denial","source_type":"word_analysis","support_ids":["sup_2f1c1974c0f43c5e86e5","sup_db5f7513257f4cc258a6"],"title":"second denial coordinated with first","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:5","qac_refs":["87:13:5:1"],"status":"accepted"}},{"anchor_refs":["87:13:6"],"branch_refs":[],"candidate_id":"cand_87fad4a2c33cbfa248f7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:6:independent-life-negation","source_type":"word_analysis","support_ids":["sup_9fafa32970d2ba85e142","sup_c7c534448d194b9d0d7d"],"title":"life gets its own negation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:6","qac_refs":["87:13:5:2"],"status":"accepted"}},{"anchor_refs":["87:13:6"],"branch_refs":[],"candidate_id":"cand_2ce6ffb7213d20e16be2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:6:punitive-non-life-closure","source_type":"word_analysis","support_ids":["sup_5c0c9788ccc9912a1683","sup_c7c534448d194b9d0d7d"],"title":"non-death is not mercy","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:6","qac_refs":["87:13:5:2"],"status":"accepted"}},{"anchor_refs":["87:13:6"],"branch_refs":[],"candidate_id":"cand_583513f21f915fa4f4af","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:13:6:repeated-negator-rhythm","source_type":"word_analysis","support_ids":["sup_b8fa242caa2b56cb6d52","sup_c7c534448d194b9d0d7d"],"title":"balanced negation refrain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:6","qac_refs":["87:13:5:2"],"status":"accepted"}},{"anchor_refs":["87:13:7"],"branch_refs":[],"candidate_id":"cand_61ccec6b61c4b8543951","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000383"],"scope":"focus_ayah","source_local_id":"87:13:7:closing-sound-with-denied-life","source_type":"word_analysis","support_ids":["sup_8c39fab8889a5f08f4b1","sup_ec17ff33b90be2278a7c"],"title":"open closing sound, withheld life","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:7","qac_refs":["87:13:6:1"],"status":"accepted"}},{"anchor_refs":["87:13:7"],"branch_refs":[],"candidate_id":"cand_6a2ae44375b30b5f0efb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000383"],"scope":"focus_ayah","source_local_id":"87:13:7:contained-final-denial","source_type":"word_analysis","support_ids":["sup_5e7592203ab58d8df389","sup_ec17ff33b90be2278a7c"],"title":"final denial inside recalled fire","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:7","qac_refs":["87:13:6:1"],"status":"accepted"}},{"anchor_refs":["87:13:7"],"branch_refs":[],"candidate_id":"cand_2b4bc60075ca6e2b825c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000383"],"scope":"focus_ayah","source_local_id":"87:13:7:imperfect-life-withheld","source_type":"word_analysis","support_ids":["sup_3d6b482e2cc8280ffc99","sup_ec17ff33b90be2278a7c"],"title":"life continually unrealized","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:7","qac_refs":["87:13:6:1"],"status":"accepted"}},{"anchor_refs":["87:13:7"],"branch_refs":[],"candidate_id":"cand_7ae100df602069af552d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000383"],"scope":"focus_ayah","source_local_id":"87:13:7:intertextual-life-contrasts","source_type":"word_analysis","support_ids":["sup_3ab3ccdb36de7ac0454c","sup_ec17ff33b90be2278a7c"],"title":"true life and cycle contrasts","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:7","qac_refs":["87:13:6:1"],"status":"accepted"}},{"anchor_refs":["87:13:7"],"branch_refs":[],"candidate_id":"cand_81a60b3202acd18bf844","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000383"],"scope":"focus_ayah","source_local_id":"87:13:7:life-field-narrowed-to-vitality","source_type":"word_analysis","support_ids":["sup_5ff411cddcf400eddd7c","sup_ec17ff33b90be2278a7c"],"title":"life field sharpens withheld vitality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:7","qac_refs":["87:13:6:1"],"status":"accepted"}},{"anchor_refs":["87:13:7"],"branch_refs":[],"candidate_id":"cand_4db6c9ca4b2e91bf6bbd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000383"],"scope":"focus_ayah","source_local_id":"87:13:7:life-opposite-becomes-second-deprivation","source_type":"word_analysis","support_ids":["sup_0c8889d490be5f01d6cc","sup_ec17ff33b90be2278a7c"],"title":"relief opposite turned into deprivation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:7","qac_refs":["87:13:6:1"],"status":"accepted"}},{"anchor_refs":["87:13:7"],"branch_refs":[],"candidate_id":"cand_6a1e467c4935fdad939f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000383"],"scope":"focus_ayah","source_local_id":"87:13:7:objectless-life-state-denied","source_type":"word_analysis","support_ids":["sup_558246b088e8d007b8f1","sup_ec17ff33b90be2278a7c"],"title":"subject's own life-state denied","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:13:7","qac_refs":["87:13:6:1"],"status":"accepted"}},{"anchor_refs":["87:13:3"],"branch_refs":[],"candidate_id":"cand_a64d417ebbe999d90fa8","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001454"],"scope":"focus_ayah","source_local_id":"87:13:3:1","source_type":"qac_morpheme","support_ids":["sup_00be36dd431c5e7bb515"],"title":"QAC root occurrence: م و ت","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:13:6"],"branch_refs":[],"candidate_id":"cand_069bd4185ab08f1d16ee","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000383"],"scope":"focus_ayah","source_local_id":"87:13:6:1","source_type":"qac_morpheme","support_ids":["sup_abe665473c9d15a2be18"],"title":"QAC root occurrence: ح ي ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:13"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:13","branch_refs":["root_000383/B003","root_001454/B001"],"candidate_id":"cand_c253bb91ae6112790ccf","commentary_obligation":"review","hft_ref":"hft_0f2b6a743b8b4964ec2e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_suspended_endpoints","source_type":"hft","support_ids":["sup_d8c3c7ff070cd4abfbe1"],"title":"baseline_suspended_endpoints","trust":"legacy_unbound"},{"anchor_refs":["87:13"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:13","branch_refs":["root_000383/B013","root_001454/B012"],"candidate_id":"cand_7f508cf16e323ad37129","commentary_obligation":"review","hft_ref":"hft_1c5dd0604a5030afbfd1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_persistence_without_welfare","source_type":"hft","support_ids":["sup_2126fdd8be499654fbb9"],"title":"baseline_persistence_without_welfare","trust":"legacy_unbound"},{"anchor_refs":["87:13"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:13","branch_refs":["root_000383/B002","root_001454/B009"],"candidate_id":"cand_780eeea0b117a8fdca01","commentary_obligation":"review","hft_ref":"hft_ed3603dd8015e64dcb21","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_no_collapse_no_renewal","source_type":"hft","support_ids":["sup_cd95784aa9d134d8bfb8"],"title":"baseline_no_collapse_no_renewal","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ","qac_morphemes":[{"lemma_ar":"ثُمّ","morph_features":"STEM|POS:CONJ|LEM:vum~","morpheme_role":"STEM","pos":"CONJ","qac_ref":"87:13:1:1","qac_word_ref":"87:13:1","root_ar":"","surface_ar":"ثُمَّ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"87:13:2:1","qac_word_ref":"87:13:2","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","root_ar":"م و ت","surface_ar":"يَمُوتُ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"87:13:4:1","qac_word_ref":"87:13:4","root_ar":"","surface_ar":"فِي"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"87:13:4:2","qac_word_ref":"87:13:4","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:13:5:1","qac_word_ref":"87:13:5","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"87:13:5:2","qac_word_ref":"87:13:5","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","root_ar":"ح ي ي","surface_ar":"يَحْيَىٰ"}],"word_analysis_qac_refs":[["87:13:1:1"],["87:13:2:1"],["87:13:3:1"],["87:13:4:1","87:13:4:2"],["87:13:5:1"],["87:13:5:2"],["87:13:6:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["87:13:1","87:13:2","87:13:3","87:13:4","87:13:5","87:13:6","87:13:7"]},"focus_surface_evidence":{"arabic_uthmani":"ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ","qac_morphemes":[{"lemma_ar":"ثُمّ","morph_features":"STEM|POS:CONJ|LEM:vum~","morpheme_role":"STEM","pos":"CONJ","qac_ref":"87:13:1:1","qac_word_ref":"87:13:1","root_ar":"","surface_ar":"ثُمَّ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"87:13:2:1","qac_word_ref":"87:13:2","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"مَّاتَ","morph_features":"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:3:1","qac_word_ref":"87:13:3","root_ar":"م و ت","surface_ar":"يَمُوتُ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"87:13:4:1","qac_word_ref":"87:13:4","root_ar":"","surface_ar":"فِي"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"87:13:4:2","qac_word_ref":"87:13:4","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:13:5:1","qac_word_ref":"87:13:5","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"87:13:5:2","qac_word_ref":"87:13:5","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"حَىَّ","morph_features":"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:13:6:1","qac_word_ref":"87:13:6","root_ar":"ح ي ي","surface_ar":"يَحْيَىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["87:13:1:1"],["87:13:2:1"],["87:13:3:1"],["87:13:4:1","87:13:4:2"],["87:13:5:1"],["87:13:5:2"],["87:13:6:1"]],"word_analysis_refs":["87:13:1","87:13:2","87:13:3","87:13:4","87:13:5","87:13:6","87:13:7"],"word_rows":[{"analysis_record_ref":"87:13:1","analytic_gloss_range_en":"sequencing particle marking a later or escalated stage; here it carries the whole paired negation forward from the prior fire scene","analytic_root_gloss_range_en":null,"qac_refs":["87:13:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"ثُمَّ","transliteration":"thumma"}},{"analysis_record_ref":"87:13:2","analytic_gloss_range_en":"negative particle over the first imperfect verb; here it denies death as release while opening a paired neither-nor construction","analytic_root_gloss_range_en":null,"qac_refs":["87:13:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَا","transliteration":"lā"}},{"analysis_record_ref":"87:13:3","analytic_gloss_range_en":"Form I imperfect active intransitive dying; here negated as the subject's own death-event withheld inside the fire-domain","analytic_root_gloss_range_en":"broad death field includes death, deadness, causing death, lifeless land, deathlike states, and throwing oneself toward death; this local Form I imperfect selects the basic dying endpoint and negates it","qac_refs":["87:13:3:1"],"root":{"arabic":"م و ت","transliteration":"m-w-t"},"surface":{"arabic":"يَمُوتُ","transliteration":"yamūtu"}},{"analysis_record_ref":"87:13:4","analytic_gloss_range_en":"preposition plus feminine singular suffix: in it, inside it; here the pronoun resumes the prior greater fire and supplies the shared containment domain","analytic_root_gloss_range_en":null,"qac_refs":["87:13:4:1","87:13:4:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"فِيهَا","transliteration":"fīhā"}},{"analysis_record_ref":"87:13:5","analytic_gloss_range_en":"coordinating conjunction; here it binds the second negated predicate to the first without making the second denial a later event","analytic_root_gloss_range_en":null,"qac_refs":["87:13:5:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"87:13:6","analytic_gloss_range_en":"second negative particle with its own predicate scope; here it independently negates life and completes the neither-nor frame","analytic_root_gloss_range_en":null,"qac_refs":["87:13:5:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَا","transliteration":"lā"}},{"analysis_record_ref":"87:13:7","analytic_gloss_range_en":"Form I imperfect active intransitive living; here negated as the subject's own life-state and vitality withheld after death has already been denied","analytic_root_gloss_range_en":"broad life field includes living, reviving, sparing alive, true life, greeting, recognition, modesty, creatures, and names; this local Form I selects living/vitality and denies it, while some wider branches remain contrastive pressure","qac_refs":["87:13:6:1"],"root":{"arabic":"ح ي ي","transliteration":"ḥ-y-y"},"surface":{"arabic":"يَحْيَىٰ","transliteration":"yaḥyā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":7,"words_total":7,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["87:13"],"branch_refs":["root_000383/B003","root_001454/B001"],"candidate_id":"cand_c253bb91ae6112790ccf","evidence_scope":"focus_ayah","hft_ref":"hft_0f2b6a743b8b4964ec2e","item_id":"baseline_suspended_endpoints","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_suspended_endpoints","support_id":"sup_d8c3c7ff070cd4abfbe1"},{"anchor_refs":["87:13"],"branch_refs":["root_000383/B013","root_001454/B012"],"candidate_id":"cand_7f508cf16e323ad37129","evidence_scope":"focus_ayah","hft_ref":"hft_1c5dd0604a5030afbfd1","item_id":"baseline_persistence_without_welfare","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_persistence_without_welfare","support_id":"sup_2126fdd8be499654fbb9"},{"anchor_refs":["87:13"],"branch_refs":["root_000383/B002","root_001454/B009"],"candidate_id":"cand_780eeea0b117a8fdca01","evidence_scope":"focus_ayah","hft_ref":"hft_ed3603dd8015e64dcb21","item_id":"baseline_no_collapse_no_renewal","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_no_collapse_no_renewal","support_id":"sup_cd95784aa9d134d8bfb8"}],"diagnostics":[],"lane_counts":{"global":8,"macro":9,"micro":3},"packet_summary":{"ayah_count":19,"focus_ref":"87:13","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ء ث ر","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":true,"target_occurrences":9,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]}],"window":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"87:13","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":12,"unstructured_record_count":0},"identity":{"ayah_ref":"87:13","lane":"micro","linguistic_source_ref":"87:13","surface_ref":"87:13","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"87:13","target_tokens":[["Sonra",["87:13:1"]],["orada",["87:13:4"]],["ne",["87:13:2"]],["ölecek",["87:13:2","87:13:3"]],["ne",["87:13:5"]],["de",["87:13:5"]],["yaşayacaktır",["87:13:5","87:13:6"]]],"text":"Sonra orada ne ölecek ne de yaşayacaktır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s087-p01-001-019","label":"Whole surah","number":1,"refs":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:13:3:1","source_type":"qac_morpheme","support_id":"sup_00be36dd431c5e7bb515","text":"{\"lemma_ar\":\"مَّاتَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:m~aAta|ROOT:mwt|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"87:13:3:1\",\"qac_word_ref\":\"87:13:3\",\"root_ar\":\"م و ت\",\"surface_ar\":\"يَمُوتُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:4:fire-pronoun-recall","source_type":"word_analysis","support_id":"sup_06f37b8c3bd57242ec87","text":"{\"blocking_evidence\":null,\"headline\":\"feminine suffix recalls the fire\",\"reader_payoff\":\"The reader notices that the greater fire from 87:12 remains active by pronoun agreement rather than by repetition.\",\"reason\":\"Attachment cross-reference evidence strongly licenses the feminine suffix as resuming the prior fire and warns against adding an explanatory noun.\",\"representative_source_ids\":[\"QG-daad45c9\",\"MG-50b5dd50\",\"QE-b25460f7\",\"QB-034359f6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:3:sound-and-sequence-pairing","source_type":"word_analysis","support_id":"sup_0871fbecac256783f8e9","text":"{\"blocking_evidence\":null,\"headline\":\"formal echo before semantic split\",\"reader_payoff\":\"The reader notices that the death verb is first blocked, then echoed by the life verb in matched imperfect sound while death's terminal force is semantically refused.\",\"reason\":\"The two verbs are visible as paired imperfects in coordinated predicates; the sound observation is secondary but grounded in the local surfaces.\",\"representative_source_ids\":[\"QT-12fa4f7a\",\"MT-e8510045\",\"QE-b78eb2e8\",\"QP-ae94ecd5\",\"QP-d5ce28e3\",\"QY-9bea6922\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:5:completion-and-cadence","source_type":"word_analysis","support_id":"sup_09f307b99ed5a72e66ea","text":"{\"blocking_evidence\":null,\"headline\":\"linked completion of the refrain\",\"reader_payoff\":\"The reader notices the second half as both linked to the first negation and audibly launched as its own closing beat.\",\"reason\":\"The surface conjunction appears as the onset of the second negated unit, making the formal completion claim local and bounded.\",\"representative_source_ids\":[\"QE-c3688cf7\",\"QP-cf431cd9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:7:life-opposite-becomes-second-deprivation","source_type":"word_analysis","support_id":"sup_0c8889d490be5f01d6cc","text":"{\"blocking_evidence\":null,\"headline\":\"relief opposite turned into deprivation\",\"reader_payoff\":\"The reader notices that life arrives as the expected opposite of death, but the second negation turns that expected relief into the final denied possibility.\",\"reason\":\"The local life verb is coordinated with the death verb, and contextual collocation shows these roots forming a strong death-life pair in this form class.\",\"representative_source_ids\":[\"QS-26bf9f68\",\"MS-4de8fdac\",\"QT-3cac20bd\",\"ME-b5290a2a\",\"QH-33f1df08\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:1","source_type":"word_analysis","support_id":"sup_0f50ee95fc54e11b5d44","text":"{\"gloss_range\":\"sequencing particle marking a later or escalated stage; here it carries the whole paired negation forward from the prior fire scene\",\"prose\":\"{{ar:ثُمَّ}} ({{tr:thumma}}) does not merely open a new sentence; it moves the prior fire-contact of 87:12 into a further stage. Because it stands before the whole paired negation, the later stage is not just failure to die but the full condition in which both death and life are denied. The particle therefore makes the punishment feel sequenced and intensified: first the greater fire is entered, then its interior condition is disclosed. Its short opening beat also launches the first negation quickly, so release through death is blocked before the clause finishes naming the whole trap.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ثُمَّ}} ({{tr:thumma}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:3:death-life-anti-cycle","source_type":"word_analysis","support_id":"sup_15edd6d9b9a627786f39","text":"{\"blocking_evidence\":null,\"headline\":\"death-life pair becomes anti-cycle\",\"reader_payoff\":\"The reader notices that death and life are grammatically paired as opposites, but both poles are denied so the normal cycle becomes suspended deprivation.\",\"reason\":\"Attachment evidence coordinates the life verb with the death verb, and contextual collocation shows these exact root-forms strongly partner with one another.\",\"representative_source_ids\":[\"QS-fdffdc86\",\"QF-6aa325c2\",\"QT-c33a6b90\",\"ME-a59efc36\",\"QI-2b4c506e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:5:binds-opposite-predicates","source_type":"word_analysis","support_id":"sup_289f2c7f1ecfc16fb454","text":"{\"blocking_evidence\":null,\"headline\":\"opposites bound under one frame\",\"reader_payoff\":\"The reader notices that death and life are processed as opposite alternatives, and coordination helps exclude both together.\",\"reason\":\"The coordinated verbs are the death-life pair, and contextual collocation identifies the two roots as frequent partners in this form class.\",\"representative_source_ids\":[\"QS-1a019b45\",\"QS-a166d5e2\",\"QI-073b7dbf\",\"MT-299bbc26\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:3:root-field-narrowed-to-basic-death","source_type":"word_analysis","support_id":"sup_28c6937d1c6a0992eee7","text":"{\"blocking_evidence\":null,\"headline\":\"death field narrowed to dying endpoint\",\"reader_payoff\":\"The reader notices the wider death-family pressure around escape, deadness, and deathlike states, while the local Form I still denies the basic dying endpoint.\",\"reason\":\"V4 lists broader death and deadness branches, but the aligned local word is Form I intransitive, so derivative mechanisms such as seeking death or deathlike becoming remain background pressure rather than the selected local sense.\",\"representative_source_ids\":[\"QS-3a85810c\",\"QS-71f9ff1b\",\"QS-7b5f622c\",\"QS-c31b9e30\",\"QS-e855760c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:5","source_type":"word_analysis","support_id":"sup_2f1c1974c0f43c5e86e5","text":"{\"gloss_range\":\"coordinating conjunction; here it binds the second negated predicate to the first without making the second denial a later event\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) is small, but it decides how the second denial is read. It coordinates {{ar:لَا يَحْيَىٰ}} ({{tr:lā yaḥyā}}) with the first negated predicate, so life is not a new topic after death but the paired counter-exit within the same suspended state. The conjunction adds the expected opposite and at the same time sharpens the contrast: after death is refused, life is not left as an available residue. Its entry before the second {{ar:لَا}} ({{tr:lā}}) gives the final denial its own audible start while keeping it bound to the first.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:7:intertextual-life-contrasts","source_type":"word_analysis","support_id":"sup_3ab3ccdb36de7ac0454c","text":"{\"blocking_evidence\":null,\"headline\":\"true life and cycle contrasts\",\"reader_payoff\":\"The reader notices that the denied life here contrasts with true life in 29:64, the death-life sequence in 2:28, the same punishment formula in 20:74, and the later worldly-life mention in 87:16.\",\"reason\":\"The CRITICAL rows supply concrete references, and none conflicts with the local grammar; they function as formulaic and thematic contrasts rather than governing the local parse.\",\"representative_source_ids\":[\"QI-1f782caa\",\"QI-406b091c\",\"QI-4621baf0\",\"MI-3526d0f5\",\"MI-50a171e0\",\"QE-6c6c0d20\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:7:imperfect-life-withheld","source_type":"word_analysis","support_id":"sup_3d6b482e2cc8280ffc99","text":"{\"blocking_evidence\":null,\"headline\":\"life continually unrealized\",\"reader_payoff\":\"The reader notices that life is not merely absent at one instant; vitality remains unavailable as the ongoing condition is described.\",\"reason\":\"The local word is a Form I imperfect active verb under a repeated negative particle, not a perfect, imperative, or causative reviving form.\",\"representative_source_ids\":[\"QG-308f73c3\",\"QG-be3efd75\",\"QF-a69f8745\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:1:boundary-and-rhythm","source_type":"word_analysis","support_id":"sup_43fda457d2a7a74aed65","text":"{\"blocking_evidence\":null,\"headline\":\"boundary into interior stasis\",\"reader_payoff\":\"The reader notices the ayah boundary as a turn from entering the fire to being held inside its unresolved condition.\",\"reason\":\"The particle opens 87:13 while attachment evidence links the following clause to the locative fire-domain, supporting a boundary shift rather than an independent maxim.\",\"representative_source_ids\":[\"QT-47782833\",\"QP-8d44a197\",\"QB-a1cdc44b\",\"QB-e7c055b3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:2:opening-neither-nor-pulse","source_type":"word_analysis","support_id":"sup_4861cd844ca1bc14c85e","text":"{\"blocking_evidence\":null,\"headline\":\"first beat of double closure\",\"reader_payoff\":\"The reader notices the first negator as the opening beat of a staged deprivation whose full force arrives with the later repeated negator.\",\"reason\":\"Attachment evidence marks the two negated predicates as coordinated, so the first negator legitimately functions as the first member of a paired neither-nor frame.\",\"representative_source_ids\":[\"QT-dce4740c\",\"MT-cd676fec\",\"QE-56fc7de1\",\"QP-f10c4b34\",\"QY-c5217bd9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:4:fused-form-and-cadence","source_type":"word_analysis","support_id":"sup_504ff3fd9f139cc24844","text":"{\"blocking_evidence\":null,\"headline\":\"fused containment and long-ā link\",\"reader_payoff\":\"The reader notices that the compact word binds containment to pronoun recall, while its long ending audibly links the enclosure to the final denied life.\",\"reason\":\"The local surface visibly combines preposition and suffix and ends in a long vowel before the closing life verb; the claim is formal and phonetic, not a new semantic branch.\",\"representative_source_ids\":[\"QF-48a15ad2\",\"QF-bb24fd13\",\"QF-fff1208e\",\"QP-63a751ac\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:7:objectless-life-state-denied","source_type":"word_analysis","support_id":"sup_558246b088e8d007b8f1","text":"{\"blocking_evidence\":null,\"headline\":\"subject's own life-state denied\",\"reader_payoff\":\"The reader notices that the same sufferer is denied his own life-state inside the fire, not granted revived agency or shifted to another subject.\",\"reason\":\"Attachment evidence marks the verb as objectless and coordinated with the first verb, with a syntactically controlled shared 3ms subject.\",\"representative_source_ids\":[\"QG-0bc4d9e9\",\"QG-44329edc\",\"MG-b092a2ec\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:6:punitive-non-life-closure","source_type":"word_analysis","support_id":"sup_5c0c9788ccc9912a1683","text":"{\"blocking_evidence\":null,\"headline\":\"non-death is not mercy\",\"reader_payoff\":\"The reader notices that the repeated negation converts the first denial from possible survival into a fully sealed neither-nor deprivation.\",\"reason\":\"The attachment layer treats the two negated predicates as coordinated, making the second negation the closure of the same punishment frame.\",\"representative_source_ids\":[\"QS-4a13c0b0\",\"QT-32675de5\",\"MT-6489f6e3\",\"QY-cbe94400\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:7:contained-final-denial","source_type":"word_analysis","support_id":"sup_5e7592203ab58d8df389","text":"{\"blocking_evidence\":null,\"headline\":\"final denial inside recalled fire\",\"reader_payoff\":\"The reader notices the final life-denial as the closure of the whole contained punishment: the recalled fire holds both failed endpoints and becomes the foil for the next ayah's success in 87:14.\",\"reason\":\"Attachment evidence links the locative pronoun to the prior fire and coordinates the life verb with the death verb; the boundary rows extend that local containment into the next ayah contrast.\",\"representative_source_ids\":[\"QE-8b4643d2\",\"QP-4ff357f7\",\"QP-a9972c0f\",\"QP-c1d0f985\",\"QB-261d3578\",\"QB-8c1fa217\",\"QB-fa71cebf\",\"QY-b37eba9e\",\"QY-edacd1ce\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:7:life-field-narrowed-to-vitality","source_type":"word_analysis","support_id":"sup_5ff411cddcf400eddd7c","text":"{\"blocking_evidence\":null,\"headline\":\"life field sharpens withheld vitality\",\"reader_payoff\":\"The reader notices that the wider life-family makes the denial feel like withheld vitality, restoration, sparing, and recognition, while the local verb still means living itself.\",\"reason\":\"V4 supports many accepted life-family branches, but the local intransitive Form I imperfect selects living/vitality; greeting, sparing-alive, true-life, and derivational dispute rows are preserved as narrowed semantic pressure.\",\"representative_source_ids\":[\"QS-09e8679f\",\"QS-2d0a754f\",\"QS-2e666b1b\",\"QS-5a3a50f4\",\"QS-c379b9e9\",\"QS-cf67e17a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:3:imperfect-death-withheld","source_type":"word_analysis","support_id":"sup_6f940f9c1c49a8ede8ca","text":"{\"blocking_evidence\":null,\"headline\":\"death continually unrealized\",\"reader_payoff\":\"The reader notices death not as a one-time non-event but as an endpoint kept unavailable throughout the punishment scene.\",\"reason\":\"The local form is an imperfect active verb under negation; contextual polarity also shows this root-form often occurs under negation or scope, supporting the durative withholding reading.\",\"representative_source_ids\":[\"QG-571730c5\",\"QG-7bc03596\",\"MF-ef75bc2d\",\"MS-6362ff1f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:3:objectless-own-death-denied","source_type":"word_analysis","support_id":"sup_8aaa2ca21e250e4dbde5","text":"{\"blocking_evidence\":null,\"headline\":\"subject's own death-event denied\",\"reader_payoff\":\"The reader notices that the clause denies the sufferer's own dying inside the fire, not an action done to another or a newly named agent.\",\"reason\":\"Attachment evidence marks the verb as objectless and intransitive with an implicit 3ms subject continued from the prior discourse.\",\"representative_source_ids\":[\"QG-88ae80c5\",\"MG-82a71930\",\"QG-06f1129a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:7:closing-sound-with-denied-life","source_type":"word_analysis","support_id":"sup_8c39fab8889a5f08f4b1","text":"{\"blocking_evidence\":null,\"headline\":\"open closing sound, withheld life\",\"reader_payoff\":\"The reader notices that the ayah lands on an open long ending associated with the life verb while the semantics deny life, so formal closure carries unresolved meaning.\",\"reason\":\"The final alif maqṣūrah and closing position are visible in the local word; the sound claim is formal and does not create a separate lexical sense.\",\"representative_source_ids\":[\"QF-0ffde603\",\"QF-9b14763a\",\"MF-482b9b5f\",\"QT-4ec56b04\",\"QY-60f36882\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:1:sequenced-escalation-after-fire","source_type":"word_analysis","support_id":"sup_93164c26948c7866937e","text":"{\"blocking_evidence\":null,\"headline\":\"later stage after fire-contact\",\"reader_payoff\":\"The reader notices that the neither-death-nor-life condition is presented as the developed stage after entry into the greater fire, not as a detached description.\",\"reason\":\"QAC identifies the word as a sequencer, and attachment evidence places it before the first negated verbal predicate continuing the punishment scene from 87:12.\",\"representative_source_ids\":[\"QG-acedd206\",\"MG-7f62c64e\",\"QS-52a17efd\",\"QT-4001cfd1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:3","source_type":"word_analysis","support_id":"sup_9cf8ef00d999b4087897","text":"{\"gloss_range\":\"Form I imperfect active intransitive dying; here negated as the subject's own death-event withheld inside the fire-domain\",\"prose\":\"{{ar:يَمُوتُ}} ({{tr:yamūtu}}) names the first withheld endpoint. The verb is objectless and intransitive, so the clause denies the subject's own dying rather than making him an agent or an object of killing. Its imperfect form under {{ar:لَا}} ({{tr:lā}}) keeps death continually unrealized inside the fire-domain, not merely absent at one past moment. The broader {{ar:م و ت}} ({{tr:m-w-t}}) field can include deadness, caused death, deathlike posture, and even seeking death, but the local Form I narrows the payoff to basic death as completion: what would normally terminate exposure is refused. The paired verb {{ar:يَحْيَىٰ}} ({{tr:yaḥyā}}) shares the ya- imperfect onset with it, while this word's terminal t sound gives death a hard closure that the semantics refuse. Read after the greater fire of 87:12 and beside the exact formula in 20:74, the familiar death-life polarity has become a punitive anti-cycle rather than a normal passage through death and life such as 2:28.\",\"root_display\":\"{{ar:م و ت}} ({{tr:m-w-t}})\",\"root_gloss_range\":\"broad death field includes death, deadness, causing death, lifeless land, deathlike states, and throwing oneself toward death; this local Form I imperfect selects the basic dying endpoint and negates it\",\"surface_display\":\"{{ar:يَمُوتُ}} ({{tr:yamūtu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:6:independent-life-negation","source_type":"word_analysis","support_id":"sup_9fafa32970d2ba85e142","text":"{\"blocking_evidence\":null,\"headline\":\"life gets its own negation\",\"reader_payoff\":\"The reader notices that life is independently denied, so non-death cannot be mistaken for survival or mercy.\",\"reason\":\"QAC and attachment evidence identify this particle as negating the second imperfect predicate within the paired negative frame.\",\"representative_source_ids\":[\"QG-63c90516\",\"QG-7bdb181f\",\"MG-75629a86\",\"QS-ca94b23c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:13:6:1","source_type":"qac_morpheme","support_id":"sup_abe665473c9d15a2be18","text":"{\"lemma_ar\":\"حَىَّ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:HaY~a|ROOT:Hyy|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"87:13:6:1\",\"qac_word_ref\":\"87:13:6\",\"root_ar\":\"ح ي ي\",\"surface_ar\":\"يَحْيَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:6:repeated-negator-rhythm","source_type":"word_analysis","support_id":"sup_b8fa242caa2b56cb6d52","text":"{\"blocking_evidence\":null,\"headline\":\"balanced negation refrain\",\"reader_payoff\":\"The reader notices the exact particle repetition as an audible frame over both opposed verbs.\",\"reason\":\"The repeated particles are visible in the local surface, and the phonetic claim remains secondary to their syntactic scope.\",\"representative_source_ids\":[\"QE-a1f226da\",\"QP-4f7debd6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:4:greater-fire-specified","source_type":"word_analysis","support_id":"sup_b965dfcb28c835e58b3d","text":"{\"blocking_evidence\":null,\"headline\":\"greater fire specified as suspended existence\",\"reader_payoff\":\"The reader notices that the greatness of the fire is being specified by its interior condition: neither death nor life.\",\"reason\":\"The fire antecedent from 87:12 is strongly licensed for the pronoun, and the locative phrase governs the local punishment condition.\",\"representative_source_ids\":[\"MS-c55b0797\",\"QB-4078c8f2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:4","source_type":"word_analysis","support_id":"sup_bb88da866c109ea26575","text":"{\"gloss_range\":\"preposition plus feminine singular suffix: in it, inside it; here the pronoun resumes the prior greater fire and supplies the shared containment domain\",\"prose\":\"{{ar:فِيهَا}} ({{tr:fīhā}}) makes the prior {{ar:ٱلنَّارَ ٱلْكُبْرَىٰ}} ({{tr:al-nāra al-kubrā}}) from 87:12 remain grammatically present without being renamed. The feminine suffix points back to that fire, while {{ar:فِي}} ({{tr:fī}}) puts the subject inside it as the shared domain of the two denied predicates. Placed between {{ar:يَمُوتُ}} ({{tr:yamūtu}}) and {{ar:يَحْيَىٰ}} ({{tr:yaḥyā}}), the word turns enclosure into the hinge of the antithesis: death and life both fail in the same recalled container. That same containment specifies the greatness of the fire named in 87:12: its interior condition is neither death nor life. The compact fusion of preposition and pronoun makes containment and antecedent recall inseparable on the surface, and the long final sound also helps tie the enclosure to the final life-word.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِيهَا}} ({{tr:fīhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:3:formula-and-context-expansion","source_type":"word_analysis","support_id":"sup_c0ea7f09363f512c4024","text":"{\"blocking_evidence\":null,\"headline\":\"known punishment formula\",\"reader_payoff\":\"The reader notices that 87:13 compresses the greater fire of 87:12 into a known punishment expression also found in 20:74.\",\"reason\":\"The CRITICAL rows supply concrete references to 87:12 and 20:74, and the local grammar matches the same death-life negation formula.\",\"representative_source_ids\":[\"QI-9d81c6aa\",\"MI-9d5ade65\",\"QH-ae3cc0ec\",\"MT-dc1fe05b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:2","source_type":"word_analysis","support_id":"sup_c6a2b094a38d8f88d674","text":"{\"gloss_range\":\"negative particle over the first imperfect verb; here it denies death as release while opening a paired neither-nor construction\",\"prose\":\"The first {{ar:لَا}} ({{tr:lā}}) directly targets {{ar:يَمُوتُ}} ({{tr:yamūtu}}), so death itself is the first endpoint closed. Because the verb remains an indicative imperfect, the line states an ongoing punishment condition rather than commanding someone not to die. This matters for the reader: non-death is not mercy here, since the syntax first blocks death as release and then waits for the second negation to remove life as an alternative. The repeated negative sound makes the two exits distinct in recitation instead of letting one broad negation blur them together.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَا}} ({{tr:lā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:6","source_type":"word_analysis","support_id":"sup_c7c534448d194b9d0d7d","text":"{\"gloss_range\":\"second negative particle with its own predicate scope; here it independently negates life and completes the neither-nor frame\",\"prose\":\"The second {{ar:لَا}} ({{tr:lā}}) prevents a false inference: if the subject does not die, that still does not mean he lives. By repeating the particle before {{ar:يَحْيَىٰ}} ({{tr:yaḥyā}}), the ayah gives life its own predicate-level negation rather than letting it be a weak implication from the first clause. This turns non-death into punitive non-life, completing the syntactic trap in which the first exit is death and the second is meaningful life. The repeated open sound also balances the two denials before the final long ending of the life verb.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَا}} ({{tr:lā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:2:descriptive-not-prohibitive","source_type":"word_analysis","support_id":"sup_ce830c840e4d20c313d8","text":"{\"blocking_evidence\":null,\"headline\":\"condition, not prohibition\",\"reader_payoff\":\"The reader notices that the line describes deprivation inside punishment; it is not an instruction forbidding the subject to die.\",\"reason\":\"The verb is an imperfect indicative under negative particle scope, and the local syntax reports the fire-domain condition rather than an imperative frame.\",\"representative_source_ids\":[\"QG-b22756e8\",\"QS-8e10daaa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:5:coordinated-second-denial","source_type":"word_analysis","support_id":"sup_db5f7513257f4cc258a6","text":"{\"blocking_evidence\":null,\"headline\":\"second denial coordinated with first\",\"reader_payoff\":\"The reader notices that the life-denial belongs to the same suspended condition as the death-denial, not to a later separate scene.\",\"reason\":\"Attachment evidence marks the second predicate as coordinated with the first through the conjunction.\",\"representative_source_ids\":[\"QG-9d74f696\",\"QG-a8379ec1\",\"MG-2f497e02\",\"QT-323e7465\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:4:shared-containment-domain","source_type":"word_analysis","support_id":"sup_de0cbc0bb311579f06ea","text":"{\"blocking_evidence\":null,\"headline\":\"one container for both denials\",\"reader_payoff\":\"The reader notices that the fire is not just a location; it is the enclosing condition in which both death and life fail.\",\"reason\":\"The attachment layer makes the prepositional phrase the locative complement of the first verb, while the coordinated second predicate shares the same punishment frame.\",\"representative_source_ids\":[\"QG-0d4f10dc\",\"QG-be2f8813\",\"QG-cf8461b0\",\"QS-15267c33\",\"QS-706d50ca\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:7","source_type":"word_analysis","support_id":"sup_ec17ff33b90be2278a7c","text":"{\"gloss_range\":\"Form I imperfect active intransitive living; here negated as the subject's own life-state and vitality withheld after death has already been denied\",\"prose\":\"{{ar:يَحْيَىٰ}} ({{tr:yaḥyā}}) closes the ayah on the word that should have been the relief opposite of death. Instead, under the second {{ar:لَا}} ({{tr:lā}}), life is continually unrealized for the same unspoken subject who was denied death. The objectless Form I verb denies the subject's own life-state, not an act of reviving someone else. The wider {{ar:ح ي ي}} ({{tr:ḥ-y-y}}) field includes vitality, reviving, sparing alive, recognition through greeting, and true life, but local grammar narrows the selected sense to living itself while letting those branches sharpen what is withheld. The contrasts with the same punishment formula in 20:74, true life in 29:64, the death-life sequence in 2:28, and later worldly life in 87:16 make the end sharper: the afterlife condition here is excluded from true vitality and freezes the normal death-life movement. Within the surah, the contained final denial also becomes the negative foil for the next ayah's success in 87:14. The final long sound gives formal closure while the meaning refuses the consolation that closure might suggest.\",\"root_display\":\"{{ar:ح ي ي}} ({{tr:ḥ-y-y}})\",\"root_gloss_range\":\"broad life field includes living, reviving, sparing alive, true life, greeting, recognition, modesty, creatures, and names; this local Form I selects living/vitality and denies it, while some wider branches remain contrastive pressure\",\"surface_display\":\"{{ar:يَحْيَىٰ}} ({{tr:yaḥyā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:4:medial-pivot-between-opposites","source_type":"word_analysis","support_id":"sup_f0ec8bcf4f726e48bbc6","text":"{\"blocking_evidence\":null,\"headline\":\"locative hinge in the antithesis\",\"reader_payoff\":\"The reader notices the locative in the middle of the two opposite verbs, making enclosure the pivot rather than an afterthought.\",\"reason\":\"The surface order places the locative after the first negated verb and before the coordinated second predicate, matching the CRITICAL structural claim.\",\"representative_source_ids\":[\"QT-6d9dab8a\",\"QT-ba0551a2\",\"MT-be3d4e56\",\"QY-e352e3a7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:1:scope-over-paired-negation","source_type":"word_analysis","support_id":"sup_f5e3955da6a9f8c62fb0","text":"{\"blocking_evidence\":null,\"headline\":\"scope over the full neither-nor frame\",\"reader_payoff\":\"The reader notices that the sequence particle governs the whole paired denial, so the subsequent stage is both denied death and denied life.\",\"reason\":\"The attachment layer marks the first and second negated predicates as coordinated, with the opening sequencer preceding that coordinated frame.\",\"representative_source_ids\":[\"QG-1078c3ac\",\"QI-a2db77c2\",\"MT-39ac2f60\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:13:2:first-negation-denies-death","source_type":"word_analysis","support_id":"sup_ffd5b6e74c0d31184c6a","text":"{\"blocking_evidence\":null,\"headline\":\"death denied as first endpoint\",\"reader_payoff\":\"The reader notices that death is blocked first, so the most obvious endpoint or release is removed before life is separately addressed.\",\"reason\":\"QAC and attachment evidence identify the particle as negating the first imperfect predicate, with the paired negation preserved across both predicates.\",\"representative_source_ids\":[\"QG-8e1ac569\",\"MG-dbf6c7b3\",\"QS-36db2897\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ","ayah_ref":"87:13"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000383/B003","root_001454/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001454","role":"Loss of vitality supplies the terminal endpoint that the first negation refuses to let complete.","root":"م و ت","source_ref":"87:13","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000383","role":"Animate existence supplies the positive endpoint that the second negation withholds.","root":"ح ي ي","source_ref":"87:13","source_word_indices":["6"]}],"changed_reading":{"after":"The line specifies an imposed interval in which death never finishes and life never becomes functioning animation.","before":"The line is a bare paradox: he does not die and is not alive."},"confidence":"strong","focus_anchor":"The balanced construction la yamutu fiha wa-la yahya coordinates two present-tense negations inside one location, with thumma presenting the condition as a result.","mechanism":"The first negation prevents the loss of vitality from reaching death, while the second prevents persistence from becoming animate life. The subject is therefore held between terminal cessation and functioning animation rather than alternating normally between them.","model_id":"baseline_suspended_endpoints"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_suspended_endpoints","source_type":"hft","support_id":"sup_d8c3c7ff070cd4abfbe1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ","ayah_ref":"87:13"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000383/B013","root_001454/B012"],"payload":{"activation_trace":[{"branch_id":"B012","mapped_root_id":"root_001454","role":"Death-like stillness, sleep, or wearing out supplies a possible shutdown that la yamutu denies.","root":"م و ت","source_ref":"87:13","source_word_indices":["3"]},{"branch_id":"B013","mapped_root_id":"root_000383","role":"Life as benefit, good, and rescue supplies the qualitative life that wa-la yahya denies.","root":"ح ي ي","source_ref":"87:13","source_word_indices":["6"]}],"changed_reading":{"after":"Mere continuation is severed from life: the subject cannot shut down, yet receives none of life's benefit or rescue.","before":"Not dying appears equivalent to continuing to live."},"confidence":"medium","focus_anchor":"The same double negation can distinguish continued exposure from the qualities that make continuation count as life.","mechanism":"Negated death removes quiescent shutdown, while negated life removes benefit and saving good. What remains is duration without rest, welfare, rescue, or flourishing.","model_id":"baseline_persistence_without_welfare"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_persistence_without_welfare","source_type":"hft","support_id":"sup_2126fdd8be499654fbb9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ","ayah_ref":"87:13"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000383/B002","root_001454/B009"],"payload":{"activation_trace":[{"branch_id":"B009","mapped_root_id":"root_001454","role":"A recoverable faint or seizure supplies an episodic collapse whose interruption is denied.","root":"م و ت","source_ref":"87:13","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000383","role":"Rain-driven renewal and fresh growth supply the restorative phase that is also denied.","root":"ح ي ي","source_ref":"87:13","source_word_indices":["6"]}],"changed_reading":{"after":"The verse can also deny both phases of a restorative rhythm: no merciful lapse and no return to freshness.","before":"The verse denies two static states, death and life."},"confidence":"exploratory","focus_anchor":"The paired imperfect verbs permit a process reading in which neither a collapse nor a renewal ever occurs.","mechanism":"A death-word branch names a swoon or seizure from which one later recovers, while a life-word branch names earth renewed through rain and growth. Negating both yields an anti-cycle: no temporary collapse that grants interruption and no regenerative return.","model_id":"baseline_no_collapse_no_renewal"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_no_collapse_no_renewal","source_type":"hft","support_id":"sup_cd95784aa9d134d8bfb8","trust":"legacy_unbound"}]}
</lane_packet_json>
