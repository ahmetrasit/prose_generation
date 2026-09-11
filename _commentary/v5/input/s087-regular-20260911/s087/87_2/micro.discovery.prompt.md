# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **87:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s087-regular-20260911/s087/87_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "87:2",
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
{"analysis_context":{"analysis_id":"s087-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"87:2","host_surah":87,"lane_context_refs":[],"ordered_context_refs":["87:0","87:1","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, eylemden önceki ölçme ve sınır belirleme aşamasıyla sınırlıdır.","branch_kind":"bare","branch_ref":"root_000434/B001","candidate_links":[{"candidate_id":"cand_ba6b65e230f7a10a2d73","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَلَقَ","morph_features":"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:2:1","qac_word_ref":"87:2:2","surface_ar":"خَلَقَ"}],"gloss":"ölçüp sınırlarını belirleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesnenin ölçüsü ve sınırları yapılacak işten önce belirlenir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir deri parçasını kesmeden önce tuluma göre ölçmek bu işlemin örneğidir."}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin yapılacak işe göre önceden ölçülüp biçildiği genel bağlamlarda kullanılır.","boundary_detail":"Dal, eylemden önceki ölçme ve sınır belirleme aşamasıyla sınırlıdır.","branch_image_ar":"تقدير الشيء وقياسه","concept_gloss":"ölçüp sınırlarını belirleme","contextual_glosses":[{"applicability":"Deri, kumaş veya benzeri bir nesnenin kesime hazırlanmasını anlatan bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölçmenin eylemden önce geldiğini ve kesime yöneldiğini korur."},"facet_ids":["F001","F002"],"text":"kesmeden önce ölçüp biçmek","usage_role":"contextual"}],"definition":"Bir nesneyi kesme ya da uygulama öncesinde ölçüp sınırlarını uygun ve düzgün biçimde belirlemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesnenin ölçüsü ve sınırları yapılacak işten önce belirlenir."},{"facet_id":"F002","role":"example","statement":"Bir deri parçasını kesmeden önce tuluma göre ölçmek bu işlemin örneğidir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Belirsiz bir kestirimle ölçüye dayalı hazırlığı birbirine karıştırır.","fit":"narrowing","loses":"Nesneyi ölçme ve uygulama sınırlarını belirleme işlemlerini kaybeder.","preserves":"Önceden bir değer belirleme düşüncesini kısmen korur."},"text":"tahmin"}],"identity_rationale":"Kaynak anlatımı, nesnenin kesilmesi ya da işlenmesi öncesinde ölçülmesini ve sınırlarının uygun biçimde belirlenmesini ortak çekirdek olarak verir. Deri örneği bu işlemi somutlaştırır; yoktan var etme ve yalan uydurma anlamları bu dalın parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ölçüp sınırlarını belirlemek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ölçüp biçme"}],"lexicalization_note":"Tanım yalın ölçme ve biçme anlamını karşılar; başka dallardaki kalıplaşmış kullanımlar buraya taşınmaz.","neighbor_coverage_note":"Sunulan bütün adaylar değerlendirildi; yalnızca ölçmeye dayalı en yakın karşılaştırma ile aynı kökün var etme dalı sınırı belirginleştirdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda başka bir örneğe dayanmak zorunlu değildir; komşu dalda ise ölçme, bir örnekle karşılaştırma üzerine kuruludur.","focus_only":"Ölçüyü kesme ya da yapma öncesinde nesnenin kendi sınırları için belirler.","gloss":"ön ölçme ile örneğe göre ölçme","neighbor_only":"Bir şeyi başka bir örneğe göre karşılaştırarak ölçme ilişkisini öne çıkarır.","neighbor_ref":"root_001269/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin ölçüsünü ve uygun büyüklüğünü belirleme alanındadır."},{"boundary_match":"partial","distinction":"Bu dal hazırlık ve ölçülendirmede kalır; komşu dal sonucunda bir varlık ya da yapılmış şey ortaya çıkar.","focus_only":"Yapılacak nesnenin ölçü ve sınırlarını eylemden önce belirler.","gloss":"tasarlayıp ölçme ile var etme","neighbor_only":"Nesneyi gerçekten ortaya çıkarma ve var etme eylemini anlatır.","neighbor_ref":"root_000434/B002","relation_type":"near_neighbor","shared_zone":"Ölçülü hazırlık ile ortaya çıkarma aynı üretim sürecinin bağlantılı aşamaları olabilir."}],"source_phrase_ar":"أحدهما تقدير الشيء؛ خلقت الأديم للسقاء إذا قدرته (maqayis)؛ خلقت الأديم قدرته (ayn)؛ خلقت الشيء إذا قدرته (jamhara)؛ الخلق: التقدير؛ خلقت الأديم إذا قدرته قبل القطع (sihah)؛ الخلق في كلام العرب على ضربين... والآخر التقدير؛ خلقت الأديم إذا قدرته وقسته (tahdhib)؛ الخلق أصله: التقدير المستقيم (mufradat)","source_summary":"Kaynaklar, anlamı ölçme, oranlama ve kesmeden önce sınır koyma çevresinde birleştirir; düzgün ve uygun ölçü vurgusu da bu çekirdeği tamamlar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه التقدير والقياس قبل القطع أو الفعل، ومنه خلق الأديم وخلق الأمر بمعنى قدره.","what_is_not_ar":"لا يدخل فيه إبداع الله للخلق من غير أصل، ولا اختلاق الكذب إلا من جهة أنه قدر في النفس."},"support_links":["sup_ddc77dc0f5d17d05d359"]},{"boundary":"Tanım, var etmenin iki kapsamını korur; üreticiyi ve yaratılanları adlandıran kullanımları çekirdekle birleştirmez.","branch_kind":"bare","branch_ref":"root_000434/B002","candidate_links":[{"candidate_id":"cand_ba6b65e230f7a10a2d73","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَلَقَ","morph_features":"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:2:1","qac_word_ref":"87:2:2","surface_ar":"خَلَقَ"}],"gloss":"var etme ve ortaya çıkarma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey ortaya çıkarılır ve varlık kazanır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ortaya çıkarma, öncesiz bir örnek olmadan veya mevcut bir şeyden gerçekleştirilebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eylemi yapan üretici ile ortaya çıkan varlıklar eylem adından türeyen biçimlerle adlandırılır."}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin meydana getirilmesini, özellikle de başlangıç verilmeyen veya köklü bir var etme eylemini anlatır.","boundary_detail":"Tanım, var etmenin iki kapsamını korur; üreticiyi ve yaratılanları adlandıran kullanımları çekirdekle birleştirmez.","branch_image_ar":"إبداع الخلق وإيجاده","concept_gloss":"var etme ve ortaya çıkarma","contextual_glosses":[{"applicability":"Bir şeyi varlığa getiren üstün ve köklü meydana getirme eylemi için doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyi ortaya çıkarma ve varlık kazandırma anlamını korur."},"facet_ids":["F001","F002"],"text":"yaratmak","usage_role":"general"},{"applicability":"Eylemin sonucunda var olanların topluca adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemin sonucunu oluşturan varlıklar topluluğunu korur."},"facet_ids":["F003"],"text":"yaratılanlar","usage_role":"contextual"}],"definition":"Bir şeyi daha önce örneği olmadan ortaya koymak ya da başka bir şeyden yeni bir varlık meydana getirmektir. Eylem, onu yapanı ve sonuçta ortaya çıkan varlıkları adlandıran kullanımlara da uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey ortaya çıkarılır ve varlık kazanır."},{"facet_id":"F002","role":"source_variant","statement":"Ortaya çıkarma, öncesiz bir örnek olmadan veya mevcut bir şeyden gerçekleştirilebilir."},{"facet_id":"F003","role":"extension","statement":"Eylemi yapan üretici ile ortaya çıkan varlıklar eylem adından türeyen biçimlerle adlandırılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Gündelik yapım ve çoğaltma işleriyle köklü var etme eylemini karıştırabilir.","fit":"narrowing","loses":"Örneksiz var etme kapsamını ve bütün varlıkları ortaya çıkarma gücünü kaybeder.","preserves":"Bir sonuç meydana getirme düşüncesini kısmen korur."},"text":"üretme"}],"identity_rationale":"Kaynak anlatımı bir şeyi ortaya çıkarma ve var etme çekirdeğinde birleşir, fakat bunu hem öncesiz bir örnek olmadan meydana getirme hem de bir şeyden başka bir şey oluşturma biçiminde kullanır. Üretici adı ile yaratılanlar topluluğu da eylemden türeyen ayrı uzantılardır.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yaratmak, var etmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yaratan, var eden"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yaratan, var eden; özellikle Tanrı için kullanılan ad"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yaratılanlar, insanlar"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yaratılmış varlık ya da varlıklar topluluğu"}],"lexicalization_note":"Yalın dal, ortaya çıkarma eylemini tanımlar; adlaşmış üretici ve yaratılanlar anlamları bağımlı uzantılar olarak tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; örneksiz başlatma, oluşturup geliştirme ve aynı kökün ön ölçme dalı gerçek sınır farkları verdi, kalanlar daha uzak alan bağlantıları olarak elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dalın ayırıcı koşulu önceki örneğin bulunmamasıdır; bu dal ise mevcut bir şeyden yeni bir şey oluşturmayı da kapsar.","focus_only":"Var etmeyi hem örneksiz başlangıç hem de bir şeyden başka bir şey oluşturma olarak kapsar.","gloss":"var etme ile örneksiz başlatma","neighbor_only":"Örneksiz başlatmayı, yeniliği ve kendi alanında ilk olmayı özellikle öne çıkarır.","neighbor_ref":"root_000094/B001","relation_type":"near_synonym","shared_zone":"İki dal da daha önce bulunmayan bir şeyi ortaya çıkarma alanında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal yaratma eylemine odaklanır; komşu dal bazı kullanımlarda meydana getirmeyi gelişim ve yetiştirmeyle birlikte düşünür.","focus_only":"Var etmenin yanında üreticiyi ve yaratılanlar topluluğunu adlandıran uzantılar taşır.","gloss":"var etme ile oluşturup geliştirme","neighbor_only":"Ortaya çıkarmaya ek olarak büyütme ve gelişimi sürdürme boyutunu içerebilir.","neighbor_ref":"root_001502/B006","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde bir şeyi ortaya çıkarıp varlık kazandırma vardır."},{"boundary_match":"partial","distinction":"Bu dal sonuç doğuran var etmedir; komşu dal yalnızca ölçü ve tasarı sınırlarını kurar.","focus_only":"Eylemin sonunda gerçek bir varlık ya da yapılmış şey ortaya çıkar.","gloss":"var etme ile önceden ölçme","neighbor_only":"Nesnenin ölçüsünü ve sınırlarını eylem öncesinde belirlemekle yetinir.","neighbor_ref":"root_000434/B001","relation_type":"near_neighbor","shared_zone":"Ölçülü tasarım, bir şeyi meydana getirme sürecinden önce gelebilir."}],"source_phrase_ar":"الخالق الصانع (ayn)؛ الخلق مصدر خلق الله الخلق يخلقهم خلقا (jamhara)؛ هم خليقة الله (sihah)؛ الخالق والخلاق؛ الخلق ابتداع الشيء على مثال لم يسبق إليه (tahdhib)؛ يستعمل في إبداع الشيء من غير أصل ولا احتذاء؛ ويستعمل في إيجاد الشيء من الشيء (mufradat)","source_summary":"Kaynakların ortak noktası ortaya çıkarma ve var etmedir; anlatım örneksiz başlangıcı, bir şeyden başka bir şey oluşturmayı, üreticiyi ve yaratılanlar topluluğunu birlikte kapsar.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه خلق الله الخلق، والخالق الصانع، وإبداع الشيء أو إيجاده من شيء.","what_is_not_ar":"لا يدخل فيه مجرد التقدير الحرفي، ولا الخلق بمعنى السجية أو الكذب."},"support_links":["sup_ddc77dc0f5d17d05d359"]},{"boundary":"Dal görünür beden ve biçimle sınırlıdır; iç huyu veya yalnızca güzel görünmeyi tanımlamaz.","branch_kind":"bare","branch_ref":"root_000434/B003","candidate_links":[{"candidate_id":"cand_ef36520a40b54bf324ad","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَلَقَ","morph_features":"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:2:1","qac_word_ref":"87:2:2","surface_ar":"خَلَقَ"}],"gloss":"tam ve dengeli dış biçim","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dış biçim tamamlanmış ve gözle seçilebilir durumdadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan bedeninde tamamlık ve ölçülü görünüş özellikle vurgulanır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gelişmekte olan beden taslağının biçiminin belirmesi de bu tamamlanma ekseninde anlatılır."}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bedenin veya nesnenin görünür yapısının tamamlanmış ve ölçülü olduğu bağlamlarda kullanılır.","boundary_detail":"Dal görünür beden ve biçimle sınırlıdır; iç huyu veya yalnızca güzel görünmeyi tanımlamaz.","branch_image_ar":"تمام الخلقة واعتدال الصورة","concept_gloss":"tam ve dengeli dış biçim","contextual_glosses":[{"applicability":"Oluşum sürecindeki bir bedenin ya da parçanın görünür yapısının belirdiği bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dengeli ve ölçülü görünüş vurgusunu açıkça söylemez.","preserves":"Biçimin oluşmasını ve tamamlanmasını açıkça korur."},"facet_ids":["F001","F003"],"text":"biçimi tamamlanmış","usage_role":"contextual"}],"definition":"Bir varlığın dıştan görülebilen biçiminin tamamlanmış, dengeli ve belirgin hale gelmiş olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dış biçim tamamlanmış ve gözle seçilebilir durumdadır."},{"facet_id":"F002","role":"specialization","statement":"İnsan bedeninde tamamlık ve ölçülü görünüş özellikle vurgulanır."},{"facet_id":"F003","role":"example","statement":"Gelişmekte olan beden taslağının biçiminin belirmesi de bu tamamlanma ekseninde anlatılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Olumlu beğeni ve çekicilik yargısı ekler.","collision":"Tam oluşmuş bir biçimi beğenilen bir görünüşle karıştırır.","fit":"displacement","loses":"Biçimin tamamlanması ve parçaların dengeli oluşu koşullarını kaybeder.","preserves":"Dış görünüşe ilişkin bir değerlendirme alanını korur."},"text":"güzellik"}],"identity_rationale":"Kaynak anlatımı dıştan görülen biçimin tamamlanması, dengeli oluşu ve görünür duruma gelmesi üzerinde birleşir. Genel bir güzellik yargısı zorunlu değildir; asıl ölçüt oluşumun tamamlanması ve biçimin gözle seçilebilmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dış görünüş ve beden yapısı"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"beden yapısı tam ve dengeli"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yapısı tamamlanmış ve ölçülü"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"biçimi belirmiş ve oluşumu tamamlanmış"}],"lexicalization_note":"Yalın dal dış görünüşün oluşmuş ve dengeli olmasını anlatır; iç karakter veya başka kalıpların anlamları eklenmez.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; görünür yapı ile genel görünüş arasındaki fark ve aynı kökün iç karakter dalıyla karşıt alan sınırı okuyucu için en yararlı iki ayrım oldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal oluşumun tamamlığına hükmeder; komşu dal görünür yapıyı veya boyu yalnızca betimler.","focus_only":"Dış biçimin oluşumca tamamlanmış ve ölçülü olmasını gerektirir.","gloss":"tam dış biçim ile görünüş","neighbor_only":"Boy, beden, yüz veya genel görünüşü tamamlanma koşulu aramadan adlandırabilir.","neighbor_ref":"root_000053/B006","relation_type":"near_neighbor","shared_zone":"İki dal da insanın gözle algılanan bedeni ve görünüşüyle ilgilidir."},{"boundary_match":"field_only","distinction":"Burada yapı bedensel ve görünürdür; komşu dalda ise davranışta beliren iç eğilimdir.","focus_only":"Gözle algılanan dış biçim ve beden yapısını anlatır.","gloss":"dış yapı ile iç karakter","neighbor_only":"İçten taşınan huyu ve insanlarla davranış biçimini anlatır.","neighbor_ref":"root_000434/B004","relation_type":"near_neighbor","shared_zone":"İki dal insanın nasıl bir yapıya sahip olduğunu farklı yönlerden anlatır."}],"source_phrase_ar":"رجل مختلق تام الخلق؛ المختلق من كل شيء ما اعتدل (maqayis)؛ رجل خليق أي تم خلقه؛ المختلق من كل شيء ما اعتدل (ayn)؛ رجل خليق ومختلق أي تام الخلق معتدل؛ مضغة مخلقة أي تامة الخلق (sihah)؛ رجل خليق إذا تم خلقه؛ مخلقة قد بدا خلقها وغير مخلقة لم تصور (tahdhib)؛ خص الخلق بالهيئات والأشكال والصور المدركة بالبصر (mufradat)","source_summary":"Kaynaklar görünür şekil, beden yapısının tamamlanması ve parçaların dengeli biçimde belirmesi üzerinde birleşir; oluşumu henüz görünür olmayan durum bunun karşısında yer alır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه تمام الخلق، اعتدال الصورة، ظهور التصوير، والهيئات والأشكال المدركة بالبصر.","what_is_not_ar":"لا يدخل فيه السجية الباطنة ولا النصيب ولا البلى."},"support_links":["sup_4b626362257e695f0b1a"]},{"boundary":"İç eğilim çekirdektir; iyi geçinme ve edinilmiş tutumlar bağımlı kullanımlar olarak ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000434/B004","candidate_links":[{"candidate_id":"cand_ef36520a40b54bf324ad","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَلَقَ","morph_features":"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:2:1","qac_word_ref":"87:2:2","surface_ar":"خَلَقَ"}],"gloss":"huy ve iç karakter","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin iç dünyasında yerleşmiş bir huy ve davranış eğilimi bulunur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu iç eğilim erdemli yaşayış, insanlarla iyi geçinme ve benimsenen yaşam yolu olarak görünür."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişi kendisinde olmayan bir huyu çabayla edinmeye veya öyle görünmeye çalışabilir."}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin davranışlarını yönlendiren yerleşik iç eğilimi genel olarak anlatmak için kullanılır.","boundary_detail":"İç eğilim çekirdektir; iyi geçinme ve edinilmiş tutumlar bağımlı kullanımlar olarak ayrı tutulur.","branch_image_ar":"السجية والطبيعة الباطنة","concept_gloss":"huy ve iç karakter","contextual_glosses":[{"applicability":"Kişinin insanlarla olumlu, ölçülü ve iyi bir biçimde ilişki kurmasını anlatan yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Olumsuz veya değerce yansız huyları ve genel iç yapı kapsamını dışarıda bırakır.","preserves":"İç huyun insan ilişkilerindeki olumlu görünümünü korur."},"facet_ids":["F001","F002"],"text":"iyi huyluluk ve iyi geçim","usage_role":"contextual"},{"applicability":"Doğal olmayan bir davranış biçiminin çabayla benimsenmesini veya öyle görünmeye çalışılmasını anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sonradan huy edinme çabasını ve doğal huydan ayrımını korur."},"facet_ids":["F003"],"text":"bir huyu edinmeye çalışmak","usage_role":"explanatory"}],"definition":"Kişinin içten taşıdığı ve davranışlarında dışa vurduğu kalıcı eğilim ve huydur. İyi geçinme, erdemli tutum, yaşam yolu ve bir huyu edinmeye çalışma bu çekirdeğe bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin iç dünyasında yerleşmiş bir huy ve davranış eğilimi bulunur."},{"facet_id":"F002","role":"extension","statement":"Bu iç eğilim erdemli yaşayış, insanlarla iyi geçinme ve benimsenen yaşam yolu olarak görünür."},{"facet_id":"F003","role":"associated_use","statement":"Kişi kendisinde olmayan bir huyu çabayla edinmeye veya öyle görünmeye çalışabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Benlik, bireysel özellikler ve toplumsal kimlik gibi daha geniş alanlar ekler.","collision":"Huy alanını kişinin bütün ruhsal ve toplumsal özellikleriyle karıştırabilir.","fit":"broadening","loses":"Huyun davranış ve geçinme biçiminde dışa vurulmasını açıkça göstermez.","preserves":"Kişinin kalıcı iç özellikleri düşüncesini korur."},"text":"kişilik"}],"identity_rationale":"Kaynak anlatımının çekirdeği kişinin içten taşıdığı huy ve kalıcı eğilimdir. İyi geçinme, erdemli davranış, yaşam yolu ve bir huyu sonradan edinmeye çalışma aynı çekirdeğin davranışsal veya kazanılmış uzantılarıdır; bunlar doğuştan yapıyla özdeş değildir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"huy, iç karakter"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"doğal huy ve yaradılıştan eğilim"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"iyi huyluluk ve iyi geçim"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"insanlarla huyuna göre geçinmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir huyu edinmeye veya öyle görünmeye çalışmak"}],"lexicalization_note":"Yalın biçimler iç huyu anlatır; iyi huyluluk, insanlarla geçinme ve bir huy edinme gibi yapıya bağlı kullanımlar ayrıca sınırlandırılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sabit doğal eğilim, doğuştan yapı ve aynı kökün dış biçim dalı bu geniş iç-huy alanının sınırlarını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal daha çok değişmez ve yerleşik doğaya yönelir; bu dal huyun ilişkilerdeki görünümünü ve edinilme çabasını da taşır.","focus_only":"İç huyun insanlarla geçinme, erdemli yaşayış ve sonradan edinilme uzantılarını da kapsar.","gloss":"davranışta beliren huy ile sabit eğilim","neighbor_only":"Kişiye yerleşmiş ve onu sürekli izleyen doğal eğilimi özellikle öne çıkarır.","neighbor_ref":"root_000455/B002","relation_type":"near_synonym","shared_zone":"İki dal da kişide süreklilik gösteren iç huy ve eğilimi anlatır."},{"boundary_match":"partial","distinction":"Bu dal yerleşik veya kazanılmış huyu kapsar; komşu dalın ayırıcı yönü doğuştan verilmiş yapıdır.","focus_only":"İyi geçinme ve sonradan bir huy edinme gibi davranışsal uzantılara açıktır.","gloss":"huy ile doğuştan yapı","neighbor_only":"İnsanın ya da canlının başlangıçtan beri taşıdığı doğuştan yapıyı vurgular.","neighbor_ref":"root_000217/B004","relation_type":"near_synonym","shared_zone":"Her iki dal insanın içten gelen ve davranışını etkileyen yapısını anlatabilir."},{"boundary_match":"field_only","distinction":"Bu dal davranıştan anlaşılan iç yapıdır; komşu dal gözle görülen dış yapıdır.","focus_only":"İç eğilim ve davranış biçimini anlatır.","gloss":"iç huy ile dış biçim","neighbor_only":"Gözle görülen beden biçiminin tamamlık ve dengesini anlatır.","neighbor_ref":"root_000434/B003","relation_type":"near_neighbor","shared_zone":"İki dal kişide bulunan bir yapıyı farklı algı yollarıyla ele alır."}],"source_phrase_ar":"الخلق وهي السجية (maqayis)؛ الخليقة الخلق والخليقة الطبيعة (ayn)؛ الخلق: خلق الإنسان الذي طبع عليه؛ حسن الخلق؛ كريم الخليقة (jamhara)؛ الخليقة: الطبيعة؛ الخلقة: الفطرة؛ الخلق والخلق: السجية (sihah)؛ الطبيعة والخليقة والسليقة بمعنى واحد؛ خالق الناس بخلق حسن أي عاشرهم؛ الخلق الدين؛ الخلق المروءة (tahdhib)؛ خص الخلق بالقوى والسجايا المدركة بالبصيرة (mufradat)","source_summary":"Kaynaklar iç huy, doğuştan ya da yerleşik eğilim ve bunun insan ilişkilerindeki görünümü çevresinde birleşir; erdemli yaşayış ile sonradan huy edinme bu alanın uzantılarıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الخلق والخليقة والطبيعة والسليقة والفطرة والمروءة والدين من جهة الصفة الباطنة والمعاشرة بها.","what_is_not_ar":"لا يدخل فيه الخلقة والصورة المرئية ولا الخلاق بمعنى النصيب."},"support_links":["sup_4b626362257e695f0b1a"]},{"boundary":"Dal, yaraşırlık ve güçlü uygunluk bildirir; gerçekleşmiş eylemi veya yalnızca hazırlanmayı bildirmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000434/B005","candidate_links":[{"candidate_id":"cand_2e9347d6053a69cd5f71","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَلَقَ","morph_features":"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:2:1","qac_word_ref":"87:2:2","surface_ar":"خَلَقَ"}],"gloss":"bir şeye yaraşır ve uygun olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi ile ona bağlanan iş veya nitelik arasında güçlü bir uygunluk vardır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu uygunluk, kişinin söz konusu iş için hazırlanmış gibi görülmesiyle açıklanır."}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya durumun belirli bir eylem ya da iyilik için güçlü biçimde uygun görüldüğü bağlamlarda kullanılır.","boundary_detail":"Dal, yaraşırlık ve güçlü uygunluk bildirir; gerçekleşmiş eylemi veya yalnızca hazırlanmayı bildirmez.","branch_image_ar":"الجدارة والتهيؤ للشيء","concept_gloss":"bir şeye yaraşır ve uygun olma","contextual_glosses":[{"applicability":"Bir kişinin belirli bir işi yapmaya güçlü biçimde yatkın veya uygun görüldüğü cümlelerde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir niteliğe ya da iyiliğe yaraşır olma kapsamını daraltır.","preserves":"Eylemin kişiden güçlü biçimde beklenmesi anlamını korur."},"facet_ids":["F001"],"text":"bunu yapması çok beklenir","usage_role":"contextual"}],"definition":"Bir kişinin bir işi yapmaya veya bir niteliği taşımaya yaraşır, uygun ve bunu yapması beklenebilir durumda olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi ile ona bağlanan iş veya nitelik arasında güçlü bir uygunluk vardır."},{"facet_id":"F002","role":"associated_use","statement":"Bu uygunluk, kişinin söz konusu iş için hazırlanmış gibi görülmesiyle açıklanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gerçek bir hazırlık sürecinin tamamlandığı anlamını ekler.","collision":"Değer ve uygunluk yargısını uygulamalı hazırlıkla karıştırır.","fit":"displacement","loses":"Yaraşırlık ve eylemin kişiden beklenmesi yargılarını kaybeder.","preserves":"Bir işe uygun durumda bulunma düşüncesini kısmen korur."},"text":"hazır olma"}],"identity_rationale":"Kaynak anlatımı, bir kişinin bir iş veya sonuç için uygun, yaraşır ve bunu yapması beklenebilir durumda olmasını ortak anlam olarak verir. Hazırlanmış olmak bu uygunluğu açıklayan bir benzetmedir; gerçek bir hazırlık işlemi zorunlu değildir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yaraşır, uygun"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bunu yapması ne kadar beklenir"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"iyiliğe veya o işe çok uygun"}],"lexicalization_note":"Anlam, kişi ile beklenen iş arasındaki yapıya bağlı uygunlukta gerçekleşir; yalın bir hazırlık anlamına genellenmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; tam eşdeğer yaraşırlık dalı, eyleme özgü beklenti ve gerçek hazırlanma arasındaki üçlü ayrım yayıma değer bulundu.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sunulan kanıtta çekirdek ve kullanım sınırı aynıdır; iki dal birbirinin yerine geçebilir.","focus_only":null,"gloss":"bir işe yaraşır olma","neighbor_only":null,"neighbor_ref":"root_000228/B002","relation_type":"synonym","shared_zone":"İki dal da bir kişi veya şeyin belirli bir işe güçlü biçimde uygun ve yaraşır olmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dalın kapsamı nitelik ve iyiliğe de açılır; komşu dal belirli bir eylemin gerçekleşme yakınlığına daha sıkı bağlıdır.","focus_only":"İyiliğe, niteliğe veya işe genel yaraşırlığı kapsar.","gloss":"genel yaraşırlık ile beklenen eylem","neighbor_only":"Belirli bir eylemin kişiden yakın ve güçlü biçimde beklenmesini öne çıkarır.","neighbor_ref":"root_001220/B008","relation_type":"near_synonym","shared_zone":"Her iki dal bir eylemi yapmanın kişiye uygun ve ondan beklenebilir olduğunu bildirir."},{"boundary_match":"partial","distinction":"Bu dal bir değerlendirme ve beklentidir; komşu dal hazırlama veya hazırlanma sürecini gerektirir.","focus_only":"Kişinin işe yaraşır ve onu yapması beklenir olduğunu bildirir.","gloss":"yaraşırlık ile hazırlanma","neighbor_only":"Kişi veya nesnenin eylem için gerçekten hazırlanıp uygun hale getirilmesini anlatır.","neighbor_ref":"root_001610/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir iş için uygun durumda bulunma düşüncesine yaklaşır."}],"source_phrase_ar":"فلان خليق بكذا وأخلق به؛ هو ممن يقدر فيه ذلك (maqayis)؛ مخلقة للخير أي جدير به؛ خليق له أي جدير به؛ ما أخلقه أي ما أشبهه (ayn)؛ فلان خليق بكذا أي جدير به؛ مخلقة لذلك أي مجدرة له (sihah)؛ خليق بذاك أي حري؛ أخلق به أن يفعل؛ مخلقة للخير (tahdhib)؛ فلان خليق بكذا أي كأنه مخلوق فيه ذلك (mufradat)","source_summary":"Kaynaklar yaraşırlık, uygunluk ve bir eylemin kişiden güçlü biçimde beklenmesi üzerinde birleşir; hazırlanmış veya o özellik için yaratılmış olma benzetmesi bu yargıyı açıklar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه خليق بكذا، أخلق به، مخلقة للخير، وما يكون الشخص كأنه مهيأ أو مقدر لذلك.","what_is_not_ar":"لا يدخل فيه النصيب نفسه ولا تمام الخلقة الجسدية."},"support_links":["sup_1083d930d3d7d799b1d1"]},{"boundary":"Pay çekirdeği korunur; iyiliğin kendisi, inanç yolu veya kazanılmış erdem onunla doğrudan özdeşleştirilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000434/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَلَقَ","morph_features":"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:2:1","qac_word_ref":"87:2:2","surface_ar":"خَلَقَ"}],"gloss":"iyilikten düşen pay","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye ayrılmış ve onun payına düşmüş bir bölüm vardır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Pay özellikle iyilik ve öte dünyadaki karşılık bakımından değerlendirilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İyiliğe istek, düzgün yaşayış veya huyla kazanılmış erdem de pay kavramını açıklayan değerler olarak verilir."}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin iyilikten veya öte dünyadaki karşılıktan sahip olduğu ya da olmadığı payı anlatır.","boundary_detail":"Pay çekirdeği korunur; iyiliğin kendisi, inanç yolu veya kazanılmış erdem onunla doğrudan özdeşleştirilmez.","branch_image_ar":"الخلاق نصيب الخير","concept_gloss":"iyilikten düşen pay","contextual_glosses":[{"applicability":"Bir kişinin iyilik veya öte dünyadaki karşılık bakımından hiçbir pay taşımadığını söyleyen yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Payın yokluğunu ve payın iyilik alanıyla ilişkisini korur."},"facet_ids":["F001","F002"],"text":"iyilikten payı yok","usage_role":"contextual"}],"definition":"Kişiye ayrılmış paydır; özellikle iyilikten veya öte dünyadaki karşılıktan ona düşen bölümü anlatır. İyiliğe yöneliş, düzgün yaşayış ve huyla kazanılmış erdem kimi açıklamalarda bu payın niteliği olarak öne çıkar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye ayrılmış ve onun payına düşmüş bir bölüm vardır."},{"facet_id":"F002","role":"specialization","statement":"Pay özellikle iyilik ve öte dünyadaki karşılık bakımından değerlendirilir."},{"facet_id":"F003","role":"source_variant","statement":"İyiliğe istek, düzgün yaşayış veya huyla kazanılmış erdem de pay kavramını açıklayan değerler olarak verilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Payın konusu olan iyilikle payın kendisini birbirine karıştırır.","fit":"narrowing","loses":"Bir kişiye ayrılmış bölüm ve o bölümün kişiye düşmesi ilişkisini kaybeder.","preserves":"Payın değerlendirildiği olumlu değer alanını korur."},"text":"iyilik"}],"identity_rationale":"Kaynak anlatımının baskın çekirdeği kişiye ayrılan pay, özellikle iyilik ve öte dünya bakımından düşen paydır. İyiliğe istek, düzgün yaşayış ve kişinin huyuyla kazandığı erdem açıklamaları pay düşüncesini yorumlayan veya genişleten kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"pay, özellikle iyilikten düşen pay"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"iyilikten veya öte dünyadaki karşılıktan payı yok"}],"lexicalization_note":"Yalın ad payı bildirir; payın bulunmadığını söyleyen yapı ve iyilik alanındaki yorumlar kendi kullanım sınırlarında tutulur.","neighbor_coverage_note":"Sunulan bütün adaylar değerlendirildi; iyiliğin kendisi ile izlenen inanç yolu, pay çekirdeğinin en kolay karışabileceği iki alan olduğu için seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal iyiliği bir kişiye düşen pay olarak kurar; komşu dal iyilik eylem ve tutumlarını doğrudan adlandırır.","focus_only":"Kişiye iyilikten düşen payı ve bu payın bulunup bulunmadığını anlatır.","gloss":"iyilik payı ile iyiliğin kendisi","neighbor_only":"İyi davranış, doğru yaşayış ve geniş iyilik alanının kendisini anlatır.","neighbor_ref":"root_000104/B002","relation_type":"same_field","shared_zone":"İki dal iyilik, doğru yaşayış ve olumlu karşılık alanında buluşur."},{"boundary_match":"field_only","distinction":"Bu dal kişinin payını ölçer; komşu dal kişinin bağlı olduğu inanç ve yaşayış yolunu gösterir.","focus_only":"İnanç ve iyilik alanında kişiye düşen payı bildirir.","gloss":"inançtan pay ile izlenen yol","neighbor_only":"İzlenen inanç yolunu ve kurallar bütününü doğrudan adlandırır.","neighbor_ref":"root_001445/B003","relation_type":"same_field","shared_zone":"Bazı açıklamalar iki dalı doğru yaşayış ve inanç alanında yan yana getirir."}],"source_phrase_ar":"الخلاق النصيب لأنه قد قدر لكل أحد نصيبه (maqayis)؛ الخلاق النصيب من الحظ الصالح؛ ليس له خلاق أي ليس له رغبة في الخير ولا في الآخرة (ayn)؛ لا خلاق له أي لا نصيب له في الخير؛ الخلاق النصيب (jamhara)؛ الخلاق: النصيب؛ لا خلاق له في الآخرة (sihah)؛ الخلاق النصيب من الحظ الصالح؛ النصيب من الخير؛ الخلاق الدين (tahdhib)؛ الخلاق ما اكتسبه الإنسان من الفضيلة بخلقه (mufradat)","source_summary":"Kaynakların çoğu ayrılmış pay ve özellikle iyilikten düşen bölüm üzerinde birleşir; iyiliğe yönelme, düzgün yaşayış ve kazanılmış erdem bu çekirdeğin farklı açıklamalarıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الخلاق بمعنى النصيب والحظ، ولا سيما النصيب من الخير أو الآخرة أو الدين.","what_is_not_ar":"لا يدخل فيه الخلق بمعنى السجية إلا عند من يفسر الفضيلة المكتسبة بالخلق."},"support_links":[]},{"boundary":"Dal gerçek bir şeyi meydana getirmeyi değil, gerçeği olmayan söz veya anlatı üretmeyi bildirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000434/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَلَقَ","morph_features":"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:2:1","qac_word_ref":"87:2:2","surface_ar":"خَلَقَ"}],"gloss":"uydurup yalan üretme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gerçeği olmayan bir söz veya anlatı tasarlanıp üretilir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uydurma, sözün önce zihinde kurulup biçimlendirilmesiyle ilişkilendirilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yanlış kişiye bağlanan şiir ve asılsız anlatı, üretilmiş yalanın ürünü olarak adlandırılır."}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gerçeğe dayanmayan bir söz, haber veya anlatının bilinçli biçimde kurulmasını anlatır.","boundary_detail":"Dal gerçek bir şeyi meydana getirmeyi değil, gerçeği olmayan söz veya anlatı üretmeyi bildirir.","branch_image_ar":"اختلاق الكذب والكلام","concept_gloss":"uydurup yalan üretme","contextual_glosses":[{"applicability":"Gerçek olmayan bir sözün veya haberin bilinçli biçimde üretildiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yanlış kişiye bağlama ve uydurma anlatı ürünlerini kapsam dışında bırakır.","preserves":"Gerçeğe dayanmayan sözü kurma eylemini korur."},"facet_ids":["F001","F002"],"text":"bir söz uydurmak","usage_role":"contextual"},{"applicability":"Asılsız öykü ve haberlerin ürün olarak topluca adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uydurma eyleminin asılsız anlatı ürününü korur."},"facet_ids":["F003"],"text":"uydurma anlatılar","usage_role":"contextual"}],"definition":"Gerçeklik temeli olmadan zihinde bir söz veya anlatı kurup onu doğruymuş gibi ortaya atmaktır. Yanlış kişiye bağlanan şiirler ve uydurma anlatılar bu eylemin ürünleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gerçeği olmayan bir söz veya anlatı tasarlanıp üretilir."},{"facet_id":"F002","role":"associated_use","statement":"Uydurma, sözün önce zihinde kurulup biçimlendirilmesiyle ilişkilendirilir."},{"facet_id":"F003","role":"extension","statement":"Yanlış kişiye bağlanan şiir ve asılsız anlatı, üretilmiş yalanın ürünü olarak adlandırılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Hazır bir yanlış bildirimle bilinçli uydurma sürecini ayırt etmez.","fit":"narrowing","loses":"Yalanı zihinde kurma, üretme ve yanlış kişiye bağlama işlemlerini kaybeder.","preserves":"Ortaya çıkan içeriğin gerçeğe aykırı olduğunu korur."},"text":"yalan"}],"identity_rationale":"Kaynak anlatımı gerçeğe dayanmayan sözü zihinde kurma, uydurma ve doğruymuş gibi ortaya atma üzerinde birleşir. Yanlış kişiye bağlanan şiir ve asılsız anlatılar, yalan üretme eyleminin sonuç ve ürünleridir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"söz uydurmak ve çarpıtmak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"zihninde yalan kurup ortaya atmak"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yanlış kişiye bağlanmış, uydurma"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"uydurma öyküler ve asılsız anlatılar"}],"lexicalization_note":"Yalan uydurma çekirdeği korunur; söz, asılsız anlatı ve yanlış bağlama ilişkin yapılar yalnız kendi kalıplarında uygulanır.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yakın uydurma dalı, uydurma anlatı ürünü ve aynı kökün gerçek ölçme dalı anlamın eylem, ürün ve doğruluk sınırlarını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal söz ve anlatı üretme sürecine odaklanır; komşu dal uydurmanın suçlama ve ağır yanlışlık alanındaki kullanımlarını da içerir.","focus_only":"Uydurma sözün zihinde kurulmasını, asılsız anlatıları ve yanlış kişiye bağlamayı kapsar.","gloss":"uydurma söz ile suçlayıcı yalan","neighbor_only":"Yalanı suçlama, ortak koşma ve haksızlık gibi belirli alanlara genişletir.","neighbor_ref":"root_001150/B003","relation_type":"near_synonym","shared_zone":"İki dal da gerçeğe aykırı sözün bilinçli biçimde uydurulmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal üretme eylemini de içerir; komşu dal daha çok ortaya çıkmış asılsız anlatı türüne odaklanır.","focus_only":"Asılsız içeriği üretme ve doğruymuş gibi ortaya atma eylemini anlatır.","gloss":"uydurma eylemi ile asılsız anlatı","neighbor_only":"Aslı veya düzeni bulunmayan anlatıların kendisini ürün olarak adlandırır.","neighbor_ref":"root_000704/B002","relation_type":"near_neighbor","shared_zone":"Uydurulan asılsız anlatılar iki dalın ortak alanını oluşturur."},{"boundary_match":"partial","distinction":"Bu dalda kurulan şey gerçeğe aykırı sözdür; komşu dalda gerçek nesneye uygulanacak ölçü ve sınırdır.","focus_only":"Zihinde kurulan içeriğin gerçeğe aykırı bir söz olması gerekir.","gloss":"yalan tasarlama ile gerçek ölçme","neighbor_only":"Gerçek bir nesnenin ölçüsünü ve uygulama sınırlarını belirler.","neighbor_ref":"root_000434/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da eylemden önce zihinde bir düzen kurma düşüncesi bulunabilir."}],"source_phrase_ar":"الخلق خلق الكذب وهو اختلاقه واختراعه وتقديره في النفس؛ وتخلقون إفكا (maqayis)؛ الخلق الكذب (ayn)؛ اختلق فلان كلاما إذا زوره؛ وتخلقون إفكا (jamhara)؛ خلق الإفك واختلقه وتخلقه أي افتراه؛ قصيدة مخلوقة أي منحولة (sihah)؛ تقدرون كذبا؛ أحاديث الخلق وهي الخرافات من الأحاديث المفتعلة؛ اختلاق (tahdhib)؛ كل موضع استعمل الخلق في وصف الكلام فالمراد به الكذب؛ إن هذا إلا اختلاق (mufradat)","source_summary":"Kaynaklar yalan sözü uydurma, zihinde kurma ve ortaya atma çekirdeğinde birleşir; yanlış bağlama ve asılsız anlatılar bu üretimin belirgin sonuçlarıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه خلق الكذب واختلاقه وتخلقه، الكلام المزور أو المفتعل، والخرافات المنسوبة أو المنحولة.","what_is_not_ar":"لا يدخل فيه الإبداع الحقيقي ولا التقدير العملي إلا بوصفه تقديرا في النفس."},"support_links":[]},{"boundary":"Dal yüzey niteliği ve düzleştirmeyle sınırlıdır; aşınma yalnız bu niteliğe yol açtığında bağlantılıdır.","branch_kind":"bare","branch_ref":"root_000434/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَلَقَ","morph_features":"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:2:1","qac_word_ref":"87:2:2","surface_ar":"خَلَقَ"}],"gloss":"engebesiz ve düz olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüzey engebesiz, düzgün ve kesintisizdir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İp, yay kirişi, ok veya benzeri bir nesne düzeltilerek bu yüzey niteliğine kavuşturulur."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Düz kaya, yayılmış bulut, yere karışmış iz ve bedenin düz bölgesi bu niteliğin örnekleridir."}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir yüzeyin doğal olarak ya da düzeltme sonucunda çıkıntısız ve düzgün olduğu bağlamlarda kullanılır.","boundary_detail":"Dal yüzey niteliği ve düzleştirmeyle sınırlıdır; aşınma yalnız bu niteliğe yol açtığında bağlantılıdır.","branch_image_ar":"ملاسة السطح واستواؤه","concept_gloss":"engebesiz ve düz olma","contextual_glosses":[{"applicability":"İp, ok, tahta veya benzeri bir nesnenin yüzeyini işleyerek düzgün hale getirme bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğal düz yüzeyleri ve bulut ya da izin kendiliğinden düzleşmesini dışarıda bırakır.","preserves":"Yüzeyi işleyerek engebesiz hale getirme eylemini korur."},"facet_ids":["F001","F002"],"text":"yüzeyini düzeltip pürüzsüzleştirmek","usage_role":"contextual"}],"definition":"Bir yüzeyin engebesiz, düz ve kimi nesnelerde yoğun olması ya da sürtme ve düzeltmeyle bu duruma getirilmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüzey engebesiz, düzgün ve kesintisizdir."},{"facet_id":"F002","role":"extension","statement":"İp, yay kirişi, ok veya benzeri bir nesne düzeltilerek bu yüzey niteliğine kavuşturulur."},{"facet_id":"F003","role":"example","statement":"Düz kaya, yayılmış bulut, yere karışmış iz ve bedenin düz bölgesi bu niteliğin örnekleridir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Işığı güçlü biçimde yansıtma özelliği ekler.","collision":"Düz bir yüzeyle ışıldayan bir yüzeyi birbirine karıştırır.","fit":"displacement","loses":"Engebesizlik, düzlük ve yüzeyin kesintisiz olması özelliklerini kaybeder.","preserves":"İşlenmiş bir yüzeyin gözle algılanan niteliğini kısmen korur."},"text":"parlaklık"}],"identity_rationale":"Kaynak anlatımı yüzeyin engebesiz, düz ve kimi örneklerde yoğun olmasını ortak çekirdek yapar. Düzleştirme eylemi, taş ve araçların pürüzsüzlüğü, bulutun yayılıp düzleşmesi ve izin yere karışması bu çekirdeğin farklı gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"yüzeyini düzeltmek ve pürüzsüzleştirmek"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"engebesiz, düz ve yoğun"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"düz ve engebesiz kaya"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"alnın veya gözler arasının düz bölümü"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"yayılıp düzleşmek"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"düzeltilmiş ve yüzeyi engebesiz"}],"lexicalization_note":"Tanım yalın yüzey düzgünlüğünü karşılar; eskime, koku veya özel kalıp anlamları bu dala alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel izsiz yüzey, yapıya özgü perdahlama ve aynı kökün aşınma dalı düzlük çekirdeğinin üç önemli sınırını gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal genel düzlük ve düzleştirmeyi öne çıkarır; komşu dal iz, tüy veya yüzey kalıntısının yokluğuna daha fazla uzanır.","focus_only":"Düzlüğü bulut, iz, ok, ip ve belirli beden bölümleri gibi geniş örneklere uygular.","gloss":"düz yüzey ile izsiz yüzey","neighbor_only":"Yüzeyde iz bulunmaması, tüy yokluğu ve sürtünmeyle aşınma gibi özel sonuçları kapsar.","neighbor_ref":"root_001443/B003","relation_type":"near_synonym","shared_zone":"İki dalın ortak çekirdeği engebesiz ve düzgün yüzeydir."},{"boundary_match":"partial","distinction":"Bu dal nesne türüne bağlı olmayan yüzey niteliğidir; komşu dal özellikle yapı ve sıva işlemine yönelir.","focus_only":"Doğal yüzey niteliğini ve küçük nesnelerin düzeltilmesini de kapsar.","gloss":"genel düzlük ile yapı perdahı","neighbor_only":"Yapı yüzeyinin sıvanıp perdahlanması ve uzun düzgün yapı görünümüne bağlanır.","neighbor_ref":"root_001413/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal bir yüzeyi işleyip düzgün ve engebesiz hale getirebilir."},{"boundary_match":"partial","distinction":"Bu dal yüzey niteliğini anlatır; komşu dal bu niteliğe yol açabilen kullanım ve yıpranma sürecini anlatır.","focus_only":"Yüzey baştan düz olabilir veya bilinçli düzeltmeyle bu hale getirilebilir.","gloss":"düz yüzey ile aşınmış kumaş","neighbor_only":"Kumaşın kullanım yüzünden yıpranıp tüyünü kaybetmesini gerektirir.","neighbor_ref":"root_000434/B009","relation_type":"near_neighbor","shared_zone":"Yıpranmış kumaşın tüyünü kaybedip düzleşmesi iki dalı sonuç bakımından yaklaştırır."}],"source_phrase_ar":"الأصل الثاني ملاسة الشيء؛ صخرة خلقاء أي ملساء؛ اخلولق السحاب استوى؛ رسم مخلولق إذا استوى بالأرض؛ السهم المصلح مخلق لأنه يصير أملس (maqayis)؛ الأخلق الأملس؛ صخرة خلقاء أي مصمتة؛ خليقاء الجبهة مستواها؛ خليقاء الغار الأعلى باطنه؛ اخلولق السحاب أي استوى (ayn)؛ خلقت الحبل والوتر وغيرهما تخليقا إذا ملسته؛ صخرة خلقاء ملساء؛ جبل أخلق؛ ضربه على خلقاء متنه (jamhara)؛ الأخلق الأملس المصمت؛ المخلق القدح إذا لين؛ صخرة خلقاء؛ اخلولق السحاب؛ اخلولق الرسم أي استوى بالأرض (sihah)؛ الأخلق الأملس من كل شيء؛ خليقاء الجبهة مستواها؛ خلقاء الغار الأعلى؛ سهم مخلق أملس مستو؛ الخلقة السحابة المستوية (tahdhib)","source_summary":"Kaynaklar düz ve engebesiz yüzey çekirdeğinde birleşir; taş, ok, ip, beden bölgesi, bulut ve yere karışan iz bu niteliğin nesne ve durumlara göre çeşitlenen örnekleridir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الأملس المصمت، الصخرة الخلقاء، استواء السحاب أو الرسم، السهم أو القدح أو الحبل المملس، ومواضع الجبهة والوجه والظهر والغار المسماة خلقاء أو خليقاء.","what_is_not_ar":"لا يدخل فيه البلى إلا من جهة ذهاب الزئبر حتى يصير أملس، ولا يدخل فيه الخلوق الطيب."},"support_links":[]},{"boundary":"Dal kullanımın doğurduğu yıpranmayı anlatır; baştan düz olan yüzeyi veya yalnızca yaşlı olmayı kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000434/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَلَقَ","morph_features":"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:2:1","qac_word_ref":"87:2:2","surface_ar":"خَلَقَ"}],"gloss":"kullanımdan yıpranıp eskime","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kumaş veya giysi kullanım sonucunda eskiyip yıpranır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yıpranma yüzey tüyünün gitmesi, kumaşın düzleşmesi veya kenarlardan parçalanmasıyla görünür."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birine eski ve yıpranmış bir giysi vermek sonuç durumuna bağlı ettirgen kullanımdır."}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özellikle kumaş ve giysinin kullanım sonucu tüyünü, düzgünlüğünü veya bütünlüğünü yitirmesini anlatır.","boundary_detail":"Dal kullanımın doğurduğu yıpranmayı anlatır; baştan düz olan yüzeyi veya yalnızca yaşlı olmayı kapsamaz.","branch_image_ar":"بلى الثوب وذهاب وبره","concept_gloss":"kullanımdan yıpranıp eskime","contextual_glosses":[{"applicability":"Kullanımdan dolayı tüyünü yitirmiş, incelmiş veya parçalanmış giysiyi niteleyen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Giysinin kullanım sonucu eski ve maddi olarak yıpranmış olmasını korur."},"facet_ids":["F001","F002"],"text":"eski ve yıpranmış giysi","usage_role":"contextual"}],"definition":"Özellikle bir kumaş veya giysinin kullanım yüzünden yıpranması, yüzey tüyünü yitirip düzleşmesi ve yer yer parçalanmasıdır. Eski bir giysiyi birine verme de bu sonuç durumuna bağlı bir kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kumaş veya giysi kullanım sonucunda eskiyip yıpranır."},{"facet_id":"F002","role":"specialization","statement":"Yıpranma yüzey tüyünün gitmesi, kumaşın düzleşmesi veya kenarlardan parçalanmasıyla görünür."},{"facet_id":"F003","role":"associated_use","statement":"Birine eski ve yıpranmış bir giysi vermek sonuç durumuna bağlı ettirgen kullanımdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kullanılmadan yalnızca yaşı ilerlemiş her nesneyi kapsama ekler.","collision":"Yaşlılıkla kullanım sonucu oluşan maddi yıpranmayı ayırt etmez.","fit":"broadening","loses":null,"preserves":"Yeni olmama ve zamanla değişmiş olma düşüncesini korur."},"text":"eski"}],"identity_rationale":"Kaynak anlatımı özellikle kumaşın kullanım sonucu yıpranması, tüyünü yitirmesi, düzleşmesi ve yer yer parçalanması üzerinde birleşir. Eski giysi verme yapısı, yıpranmış sonucu başka bir kişiye aktaran ayrı bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"kullanımdan yıpranıp tüyünü yitirmek"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"eski ve yıpranmış giysi"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"her yanı yıpranmış veya parçalanmış giysi"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"birine eski ve yıpranmış bir giysi vermek"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"istemekten yüzünü eskitmek"}],"lexicalization_note":"Yalın biçim yıpranma sürecini, giysi yapıları eskimiş sonucu, ettirgen yapı ise eski giysi vermeyi anlatır; bu kapsamlar karıştırılmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; genel aşınma, tüyü gitmiş kumaş, giyerek yıpratma ve aynı kökün düz yüzey dalı süreç ile sonuç sınırlarını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal giysinin somut yüzey sonuçlarını ve verme yapısını taşır; komşu dal daha genel aşınma çekirdeğinde kalır.","focus_only":"Kumaşın tüyünü yitirmesi, düzleşmesi, parçalanması ve eski giysi verme yapısını ayrıntılandırır.","gloss":"giysinin yıpranması ile genel aşınma","neighbor_only":"Yıpranmayı kumaş dışındaki nesnelere de açık, daha genel bir süreç olarak verir.","neighbor_ref":"root_000683/B004","relation_type":"near_synonym","shared_zone":"Her iki dal eşya ve özellikle kumaşın kullanımla eskiyip yıpranmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal süreç ve birden çok sonucu kapsar; komşu dal daha çok tüyü gitmiş kumaşın sonuç niteliğine odaklanır.","focus_only":"Yıpranma sürecini, parçalanmayı ve eski giysinin birine verilmesini de kapsar.","gloss":"yıpranma süreci ile tüyü gitmiş kumaş","neighbor_only":"Giysinin tüyden arınmış, incelmiş ve yumuşamış sonuç durumunu özellikle öne çıkarır.","neighbor_ref":"root_000234/B006","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı eskiyip yüzey tüyünü kaybeden kumaş ve giysidir."},{"boundary_match":"partial","distinction":"Bu dal nesnenin geçirdiği değişimi ve sonucunu verir; komşu dal sonucu doğuran giyme eylemini öne çıkarır.","focus_only":"Giysinin yıpranmış durumunu ve bu durumun niteliklerini anlatır.","gloss":"yıpranmış sonuç ile giyerek yıpratma","neighbor_only":"Giysiyi uzun süre giyerek yıpranmasına yol açan eylemi özellikle anlatır.","neighbor_ref":"root_001403/B006","relation_type":"near_neighbor","shared_zone":"Uzun süre giyme, bu dalın anlattığı yıpranmış sonucu doğurur."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği yıpranmadır; komşu dalın çekirdeği yüzeyin engebesiz niteliğidir.","focus_only":"Düzleşmenin kullanım ve yıpranma sonucunda oluşmasını gerektirir.","gloss":"aşınarak düzleşme ile düz yüzey","neighbor_only":"Bir yüzeyin baştan düz olmasını veya bilinçli biçimde düzeltilmesini kapsar.","neighbor_ref":"root_000434/B008","relation_type":"near_neighbor","shared_zone":"Tüyünü yitiren kumaşın düzleşmesi iki dal arasında sonuç bakımından bağ kurar."}],"source_phrase_ar":"أخلق الشيء وخلق إذا بلي؛ إذا أخلق املاس وذهب زئبره؛ ثوب خلق (maqayis)؛ خلق الثوب يخلق خلوقة أي بلي؛ أخلقني فلان ثوبه؛ ثوب أخلاق ممزق من جوانبه (ayn)؛ أخلق الثوب إخلاقا وخلق خلوقة وخلوقا فهو خلق؛ ثوب أخلاق (jamhara)؛ ملحفة خلق وثوب خلق أي بال؛ خلق الثوب أي بلى؛ أخلقته ثوبا إذا كسوته ثوبا خلقا؛ ثوب أخلاق (sihah)؛ خلق الثوب يخلق خلوقة وأخلق إخلاقا؛ أخلق فلان فلانا أي أعطاه ثوبا خلقا؛ ثوب أخلاق؛ جبة خلق (tahdhib)","source_summary":"Kaynaklar kumaş ve giysinin eskimesi, tüyünü yitirmesi ve parçalanması çevresinde birleşir; eski giysiyi birine giydirme veya verme bu yıpranmış sonuçtan türeyen kullanımdır.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه خلق الثوب وأخلق، الثوب الخلق والأخلاق، التمزق والبلى وذهاب الزئبر أو أثر الاستعمال.","what_is_not_ar":"لا يدخل فيه كل أملس ابتداء، ولا الخلوق الطيب."},"support_links":[]},{"boundary":"Dal herhangi bir hoş kokuyu değil, sürülen koku karışımını ve onunla yapılan uygulamayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000434/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَلَقَ","morph_features":"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:2:1","qac_word_ref":"87:2:2","surface_ar":"خَلَقَ"}],"gloss":"sürülen hoş koku karışımı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sürülerek kullanılan belirli bir hoş koku maddesi veya karışımı vardır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi bu karışımı kendine sürer veya başka bir kişiyi ya da yeri onunla kaplar."}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir yüzeye veya bedene sürülerek kullanılan özel bir koku maddesini anlatır.","boundary_detail":"Dal herhangi bir hoş kokuyu değil, sürülen koku karışımını ve onunla yapılan uygulamayı anlatır.","branch_image_ar":"الخلوق والتخليق بالطيب","concept_gloss":"sürülen hoş koku karışımı","contextual_glosses":[{"applicability":"Kişinin kendisine, başka birine veya bir yere bu koku maddesini uyguladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli koku maddesini yüzeye sürme eylemini korur."},"facet_ids":["F001","F002"],"text":"hoş koku karışımı sürmek","usage_role":"contextual"}],"definition":"Bedene, kişiye veya bir yere sürülerek kullanılan belirli bir hoş koku karışımıdır. Bu karışımı sürme ve onunla kokulanma eylemleri de aynı dala bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sürülerek kullanılan belirli bir hoş koku maddesi veya karışımı vardır."},{"facet_id":"F002","role":"associated_use","statement":"Kişi bu karışımı kendine sürer veya başka bir kişiyi ya da yeri onunla kaplar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kaynağı ne olursa olsun bütün hoş kokuları kapsama ekler.","collision":"Koku yayan nesne veya havadaki kokuyla sürülen maddeyi karıştırır.","fit":"broadening","loses":"Belirli bir karışım olmasını ve sürülerek uygulanmasını açıkça söylemez.","preserves":"Kokunun hoş ve beğenilen niteliğini korur."},"text":"güzel koku"}],"identity_rationale":"Kaynak anlatımı sürülerek kullanılan belirli bir hoş koku karışımını ve bunun bedene, kişiye ya da bir yere uygulanmasını birlikte verir. Koku maddesi çekirdektir; sürme ve onunla kokulanma bu maddeye bağlı eylemlerdir.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"sürülen hoş koku karışımı"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"hoş koku karışımı sürmek veya sürünmek"}],"lexicalization_note":"Yalın biçim koku karışımını, yapıya bağlı biçim ise bu karışımı sürme veya onunla kokulanma eylemini karşılar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel kadın kokusu, renk verici kokulu karışım ve kokunun yayılması madde, kullanım ve algı sınırlarını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal uygulama eylemiyle birlikte genel bir karışımı kapsar; komşu dal cinsiyet ve giysiyi boyama özelliğiyle daha dardır.","focus_only":"Koku karışımını kişiye, başkasına veya bir yere sürme eylemlerini kapsar.","gloss":"sürülen koku karışımı ile kadın kokusu","neighbor_only":"Kadınlara özgü sayılan ve giysiye renk verebilen koku türünü öne çıkarır.","neighbor_ref":"root_000058/B007","relation_type":"near_synonym","shared_zone":"İki dal da bedene veya giysiye uygulanabilen hoş koku maddelerini anlatır."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği kokulandırmadır; komşu dal yüz rengini güzelleştirme işlevini de ekler.","focus_only":"Koku karışımının kendisini ve onunla kokulanmayı anlatır.","gloss":"koku sürme ile kokulu yüz boyası","neighbor_only":"Kokuya ek olarak yüze sürülen renk verici süs karışımını kapsar.","neighbor_ref":"root_000438/B006","relation_type":"near_neighbor","shared_zone":"İki dal hoş kokulu bir maddenin bedene sürülmesi alanında kesişir."},{"boundary_match":"field_only","distinction":"Bu dal kokunun taşıyıcı maddesine yönelir; komşu dal kokunun havaya yayılmasını olay olarak anlatır.","focus_only":"Sürülebilen koku maddesi ve onu uygulama eylemini anlatır.","gloss":"koku maddesi ile kokunun yayılması","neighbor_only":"Kokunun havada güçlü biçimde yayılması ve duyulur hale gelmesini anlatır.","neighbor_ref":"root_001686/B003","relation_type":"same_field","shared_zone":"İki dal hoş kokunun algılanması ve kullanılması alanında bulunur."}],"source_phrase_ar":"الخلوق معروف وهو الخلاق أيضا (maqayis)؛ الخلوق من الطيب؛ فعله التخليق والتخلق (ayn)؛ الخلوق ضرب من الطيب؛ خلقته أي طليته بالخلوق فتخلق به (sihah)؛ الخلوق من الطيب معروف؛ تخلقت المرأة بالخلوق وخلقت غيرها؛ خلق المسجد بالخلوق (tahdhib)","source_summary":"Kaynaklar sürülen hoş koku karışımı ve onunla kokulanma üzerinde birleşir; kişiye, başka birine veya bir yapıya sürme eylemleri kullanım alanını gösterir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الخلوق المعروف من الطيب، التخليق والتخلق به، وطلاء غيره بالخلوق.","what_is_not_ar":"لا يدخل فيه الخلق بمعنى الخلقة أو السجية ولا البلى."},"support_links":[]},{"boundary":"Dal kaya oyuğu ve yeni kuyu alt türlerini kapsar; her örnekte yağmur suyu birikmesini zorunlu saymaz.","branch_kind":"bare","branch_ref":"root_000434/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَلَقَ","morph_features":"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:2:1","qac_word_ref":"87:2:2","surface_ar":"خَلَقَ"}],"gloss":"su tutan kaya oyuğu veya yeni kuyu","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yer veya kaya içinde çukurlaşmış, suyu tutabilen bir boşluk bulunur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaya üzerindeki doğal oyuk yağmur suyunun biriktiği küçük bir hazne gibi işler."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yeni kazılmış kuyu ve yer altındaki yeni boşluklar da aynı adla anılır."}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kayadaki su biriktiren oyukları ve yeni açılmış kuyu ya da yer altı boşluklarını adlandırmak için kullanılır.","boundary_detail":"Dal kaya oyuğu ve yeni kuyu alt türlerini kapsar; her örnekte yağmur suyu birikmesini zorunlu saymaz.","branch_image_ar":"نقرة أو بئر تمسك الماء","concept_gloss":"su tutan kaya oyuğu veya yeni kuyu","contextual_glosses":[{"applicability":"Kaya yüzeyindeki küçük doğal çukurun yağmur suyunu tuttuğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yeni kazılmış kuyu ve yer altı boşluğu türlerini dışarıda bırakır.","preserves":"Doğal kaya oyuğu ile yağmur suyunu tutma ilişkisini korur."},"facet_ids":["F001","F002"],"text":"kayada yağmur suyu biriken oyuk","usage_role":"contextual"}],"definition":"Kayada yağmur suyunu tutan oyuk veya yer içinde yeni oluşmuş ya da yeni kazılmış kuyu ve boşluktur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yer veya kaya içinde çukurlaşmış, suyu tutabilen bir boşluk bulunur."},{"facet_id":"F002","role":"specialization","statement":"Kaya üzerindeki doğal oyuk yağmur suyunun biriktiği küçük bir hazne gibi işler."},{"facet_id":"F003","role":"source_variant","statement":"Yeni kazılmış kuyu ve yer altındaki yeni boşluklar da aynı adla anılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Geniş ve açık bir su yüzeyi anlamını ekler.","collision":"Suyu tutan küçük çukuru, biriken suyun oluşturduğu geniş alanla karıştırır.","fit":"displacement","loses":"Kaya içindeki küçük oyuk ve yeni kazılmış kuyu biçimlerini kaybeder.","preserves":"Suyun bir yerde toplanması ve tutulması düşüncesini korur."},"text":"gölet"}],"identity_rationale":"Kaynak anlatımı kayadaki doğal oyuk ile yeni kazılmış kuyu türünü aynı ad altında toplar. Su tutma, özellikle kaya oyuklarında belirgindir; yeni kazılmış kuyu için ayırıcı nitelik su tutmaktan çok kazının yeni oluşudur.","lexical_glosses":[{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"su tutan kaya oyuğu veya yeni kuyu"},{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"yeni kazılmış kuyular"}],"lexicalization_note":"Yalın ad kaya oyuğu veya yeni kazılmış kuyuya uygulanır; iç karakter ya da yaratılmışlar anlamı buraya taşınmaz.","neighbor_coverage_note":"Sunulan bütün adaylar değerlendirildi; kaya içindeki küçük su gözü, genel çukur ve işlevsel su havuzu bu dalın kaya, kazı ve su tutma sınırlarını belirginleştirdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kaya içindeki küçük su gözüyle sınırlıdır; bu dal yeni açılmış kuyu türüne de uzanır.","focus_only":"Doğal kaya oyuğuna ek olarak yeni kazılmış kuyu ve yer altı boşluğunu kapsar.","gloss":"kaya oyuğu ve yeni kuyu ile küçük kaya gözü","neighbor_only":"Özellikle kaya veya dağdaki küçük yağmur suyu birikintisine sıkı biçimde bağlıdır.","neighbor_ref":"root_001685/B003","relation_type":"near_synonym","shared_zone":"İki dal da kayada yağmur suyunu tutan küçük bir oyuk veya hazneyi anlatır."},{"boundary_match":"partial","distinction":"Bu dalın kapsamı su tutan oyuk ve yeni kuyudur; komşu dal beden çukuru ve hayvan izine kadar daha geniştir.","focus_only":"Su tutan kaya oyuğu ve yeni kuyu türlerini öne çıkarır.","gloss":"su oyuğu ile genel çukur","neighbor_only":"Toprak veya bedendeki çok çeşitli küçük çukurları, derin kuyuları ve izleri kapsar.","neighbor_ref":"root_001541/B004","relation_type":"near_synonym","shared_zone":"Her iki dal yer veya kaya içinde açılmış küçük çukur ve su tutan boşluk alanında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal kaya yapısı ve yeni kazı türüne bağlıdır; komşu dal su tutma işlevine bağlı daha genel bir kaptır.","focus_only":"Kaya oyuğunu ve yeni kazılmış kuyuyu adlandırır.","gloss":"kaya oyuğu ile su tutan havuz","neighbor_only":"Suyu günlerce tutan havuz, çukur veya küçük su birikme yerini işleviyle adlandırır.","neighbor_ref":"root_000018/B006","relation_type":"near_neighbor","shared_zone":"İki dal da suyun biriktiği ve bir süre tutulduğu çukur yerleri anlatır."}],"source_phrase_ar":"الخلائق نقر في الصفا (ayn)؛ الخليقة نقر في صخرة يجتمع فيه ماء السماء (jamhara)؛ قلاتا تمسك ماء السحاب في صفاة خلقها الله فيها تسميها العرب الخلائق؛ دحلان خلقها الله في بطون الأرض؛ الخليقة البئر ساعة تحفر؛ الخلق الآبار الحديثات الحفر (tahdhib)","source_summary":"Kaynaklar kaya veya yer içindeki oyukta birleşir; yağmur suyunu tutan doğal kaya çukuru ile yeni kazılmış kuyu, bu yer biçiminin iki belirgin türüdür.","sources":["AY","JA","TA"],"what_is_ar":"يدخل فيه الخليقة بمعنى النقرة في الصفا أو الصخرة يجتمع فيها ماء السماء، والدحلان والآبار الحديثة الحفر.","what_is_not_ar":"لا يدخل فيه الخليقة بمعنى الطبيعة أو الخلق المخلوق."},"support_links":[]},{"boundary":"Dal kadın bedenindeki kapanma durumuyla sınırlıdır; genel tıkanma veya yüzey düzgünlüğü değildir.","branch_kind":"bare","branch_ref":"root_000434/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَلَقَ","morph_features":"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:2:1","qac_word_ref":"87:2:2","surface_ar":"خَلَقَ"}],"gloss":"kapalı üreme yolu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın bedenindeki üreme yolu açıklığı kapalı ve geçitsizdir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapanma, yoğun ve aralıksız bir kayanın geçitsizliğine benzetilir."}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadında üreme yolu açıklığının kapalı ve geçitsiz olduğu bedensel durumu adlandırır.","boundary_detail":"Dal kadın bedenindeki kapanma durumuyla sınırlıdır; genel tıkanma veya yüzey düzgünlüğü değildir.","branch_image_ar":"انسداد مصمت كالصخرة","concept_gloss":"kapalı üreme yolu","contextual_glosses":[{"applicability":"Bu bedensel özelliği taşıyan kadını açık ve doğrudan nitelemek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiyi, bedensel yeri ve kapanma durumunu birlikte korur."},"facet_ids":["F001"],"text":"üreme yolu kapalı kadın","usage_role":"explanatory"}],"definition":"Kadının üreme yolu açıklığının kapalı, bitişik ve geçitsiz olmasıdır; durum yoğun ve geçitsiz bir kayaya benzetilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın bedenindeki üreme yolu açıklığı kapalı ve geçitsizdir."},{"facet_id":"F002","role":"associated_use","statement":"Kapanma, yoğun ve aralıksız bir kayanın geçitsizliğine benzetilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sonradan oluşan, geçici veya herhangi bir organdaki bütün tıkanmaları kapsama ekler.","collision":"Doğuştan yapısal kapanmayla sonradan gelişen engellenmeyi karıştırır.","fit":"broadening","loses":"Kadın bedenindeki belirli açıklığı ve durumun doğuştan olmasını açıkça göstermez.","preserves":"Bir geçidin kapalı ve akışa elverişsiz olmasını korur."},"text":"tıkanıklık"}],"identity_rationale":"Kaynak anlatımı kadının üreme yolu açıklığının kapalı ve geçitsiz olmasını verir; yoğun ve geçitsiz kaya benzetmesi bu bedensel durumu açıklar. Genel yüzey düzgünlüğü burada ancak benzetmenin kaynağıdır.","lexical_glosses":[{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"üreme yolu kapalı kadın"}],"lexicalization_note":"Yalın niteleme belirli bedensel kapanmayı anlatır; kapatma eylemlerine veya genel yüzey niteliğine genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; nesne ağzını kapatma, açıklığı genişletme ve başka bir bedensel yarık bu özel doğuştan kapanmanın işlem, karşıtlık ve beden bölgesi sınırlarını gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bedensel bir durumdur; komşu dal nesneye uygulanan kapatma veya örtme eylemidir.","focus_only":"Kadın bedenindeki açıklığın kapalı olmasını bildirir.","gloss":"bedensel kapanma ile ağzı kapatma","neighbor_only":"Şişe ağzı, giysi veya başka bir açıklığın kapatılması ve sıkıca bağlanmasını anlatır.","neighbor_ref":"root_000884/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da bir açıklığın ortadan kalkması ve geçişin engellenmesi vardır."},{"boundary_match":"opposed","distinction":"Bu dalda açıklık yoktur veya kapalıdır; komşu dalda açıklık oluşturulur ya da genişletilir.","focus_only":"Belirli bir beden açıklığının kapalı ve geçitsiz olmasını anlatır.","gloss":"kapalı açıklık ile açıp genişletme","neighbor_only":"Bir açıklığı genişletip akışa veya geçişe elverişli hale getirmeyi anlatır.","neighbor_ref":"root_001559/B003","relation_type":"polarity_pair","shared_zone":"İki dal aynı açıklık ve geçiş ekseninin karşıt uçlarında yer alır."},{"boundary_match":"field_only","distinction":"Bu dal kapanmış bir geçidi, komşu dal ise açık bir yarığı anlatır; beden bölgeleri de aynı değildir.","focus_only":"Üreme yolu açıklığının kapanmasını ve geçitsizliğini anlatır.","gloss":"bedensel kapanma ile bedensel yarık","neighbor_only":"Bedenin başka bir bölgesindeki yarık veya ayrımı adlandırır.","neighbor_ref":"root_001346/B006","relation_type":"same_field","shared_zone":"İki dal beden açıklıkları ve yüzey ayrımları alanında bulunur."}],"source_phrase_ar":"امرأة خلقاء رتقاء لأنها مصمتة كالصفاة الخلقاء (ayn)؛ الخلق: المرأة الرتقاء (jamhara)؛ قيل للمرأة الرتقاء: خلقاء (sihah)؛ يقال للمرأة الرتقاء: خلقاء لأنها مصمتة كالصفاة الخلقاء (tahdhib)","source_summary":"Kaynaklar belirli bir bedensel kapanma üzerinde birleşir ve bu durumu aralıksız, yoğun bir kayanın geçitsizliğiyle açıklar.","sources":["AY","JA","SI","TA"],"what_is_ar":"يدخل فيه وصف المرأة الرتقاء أو الخلقاء من جهة الانسداد والإصمات المشبه بالصفاة الخلقاء.","what_is_not_ar":"لا يدخل فيه السطح الأملس العام ولا خلق الإنسان بمعنى صورته."},"support_links":[]},{"boundary":"Bu dal başkalık, orta konum ya da bir nesnenin kendi içinde düzgün olması anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000766/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","surface_ar":"سَوَّىٰ"}],"gloss":"iki şeyi birbirine denk kılma veya denk sayma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki şey aynı ölçüye ya da değere eriştiğinde birbirini karşılar ve eş sayılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir malın belirli bir değeri karşılaması, denkliğin fiyat ve ölçü alanındaki görünümüdür."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eşlik bildiren kalıplar iki kişi ya da şey arasında ayrım bulunmadığını anlatır."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölçü, değer, nicelik, nitelik ve durum bakımından karşılıklı denkliği anlatan çekirdek kullanımlar için uygundur.","boundary_detail":"Bu dal başkalık, orta konum ya da bir nesnenin kendi içinde düzgün olması anlamlarını kapsamaz.","branch_image_ar":"مساواة ومعادلة بين شيئين","concept_gloss":"iki şeyi birbirine denk kılma veya denk sayma","contextual_glosses":[{"applicability":"İki tarafın aynı düzeyde bulunduğunu söyleyen kısa ve doğal bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılaştırılan iki tarafın aynı düzeyde bulunması anlamını korur."},"facet_ids":["F001"],"text":"eşit olmak","usage_role":"contextual"},{"applicability":"Bir malın fiyatının ya da ölçülebilir değerinin başka bir miktarı karşılaması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Değer karşılaştırmasını ve iki miktarın birbirini karşılamasını korur."},"facet_ids":["F002"],"text":"değeri buna denk olmak","usage_role":"contextual"}],"definition":"İki şeyi ölçü, değer, nicelik, nitelik ya da durum bakımından birbirine denk kılma veya denk sayma; bu denkliği eşlik bildiren belirli söz kalıplarında dile getirme.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki şey aynı ölçüye ya da değere eriştiğinde birbirini karşılar ve eş sayılır."},{"facet_id":"F002","role":"specialization","statement":"Bir malın belirli bir değeri karşılaması, denkliğin fiyat ve ölçü alanındaki görünümüdür."},{"facet_id":"F003","role":"associated_use","statement":"Eşlik bildiren kalıplar iki kişi ya da şey arasında ayrım bulunmadığını anlatır."}],"identity_rationale":"Kaynak anlatımı, iki şeyin değer, ölçü ya da durum bakımından birbirini karşılamasını çekirdek anlam olarak verir; eş olma bildiren kalıplaşmış kullanımlar da bu çekirdeğe bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi ötekinin ölçüsüne ulaştırarak eşitlemek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"iki şeyi ölçü, ağırlık, nicelik ya da nitelik bakımından eşitleme"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir işte aynı düzeyde ve eşit durumda"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"eş, benzer"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"ikisi de bir, ikisi eşit"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"özellikle, hele"}],"lexicalization_note":"Tanım eşitlik çekirdeğini korur; belirli söz kalıplarının özel işlevlerini yalın biçimin bütün anlamına yaymaz.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; genel eşitlik dalı, kapsam farkını en açık gösteren ve okur karışıklığını en iyi gideren komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sınırı belirli değer karşılaştırmalarını ve kalıplaşmış eşlik sözlerini içerirken komşu dal genel eşitleme, benzetme ve dengeleme alanında kalır.","focus_only":"Odak dal, değer ve fiyat denkliğini ve eşlik bildiren özel söz kalıplarını da içerir.","gloss":"genel eşitlik ve benzerlik","neighbor_only":"Komşu dal, iki şeyi benzetme ve dengeleme işlemini daha genel bir alanda anlatır.","neighbor_ref":"root_000991/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da iki şeyin birbirini karşılaması ve eş sayılması alanında buluşur."}],"source_phrase_ar":"أصل يدل على استقامة واعتدال بين شيئين (maqayis)؛ لا يساوي كذا أي لا يعادله (maqayis;sihah;tahdhib)؛ المساواة والاستواء واحد (ayn)؛ السِيّ المثل من قولهم سِيّان أي مثلان (jamhara;maqayis;mufradat)؛ لا سِيّما أي لا مثل ما (maqayis)؛ هذا الثوب يساوي كذا (mufradat)","source_summary":"Kaynakların ortak çizgisi, iki tarafın birbirinin ölçüsüne ulaşması ve bu nedenle eş ya da birbirini karşılar durumda bulunmasıdır; değer bildirme ve eşlik kalıpları bu çizginin özel kullanımlarıdır.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه ساوى ويساوي وتساوى واستوى بمعنى تعادل، والسواء والسَّويّة في الأمر، والسِيّ وسِيّان ولا سِيّما، وما يوازي الشيء في قدر أو ثمن.","what_is_not_ar":"ليس هو سوى بمعنى غير، ولا وسط الشيء، ولا كساء السَّويّة."},"support_links":[]},{"boundary":"Buradaki düzgünlük iki ayrı şeyi eşitlemek değil, tek bir varlığın kendi yapısındaki doğruluk ve iyiliktir.","branch_kind":"mixed_non_bare","branch_ref":"root_000766/B002","candidate_links":[{"candidate_id":"cand_ba6b65e230f7a10a2d73","lane":"micro"},{"candidate_id":"cand_ef36520a40b54bf324ad","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","surface_ar":"سَوَّىٰ"}],"gloss":"kendi içinde düzgün ve tam duruma gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin kendi yapısı içinde eğrilikten kurtulması ve düzgün duruma gelmesi çekirdektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan yaratılışında düzgünlük, görünür bozukluk ve hastalık bulunmayan tam bir yapıyı anlatır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çocukların ve hayvanların iyi durumda olması, belirli bir söz kalıbına bağlı değerlendirmedir."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir varlığın eğrilikten, eksiklikten ya da yapısal bozukluktan kurtulmasını anlatan genel kullanımlar için uygundur.","boundary_detail":"Buradaki düzgünlük iki ayrı şeyi eşitlemek değil, tek bir varlığın kendi yapısındaki doğruluk ve iyiliktir.","branch_image_ar":"استقامة وتمام في الذات","concept_gloss":"kendi içinde düzgün ve tam duruma gelme","contextual_glosses":[{"applicability":"Önceden eğri olan bir nesnenin düz ve doğru duruma gelmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başlangıçtaki eğriliğin giderilmesini ve düzgünleşme sonucunu korur."},"facet_ids":["F001"],"text":"eğrilikten kurtulup doğrulmak","usage_role":"contextual"},{"applicability":"İnsanın görünüş ve sağlık bakımından kusursuz sayılan yapısını anlatırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapısal düzgünlüğü, görünür bozukluk bulunmamasını ve sağlığı korur."},"facet_ids":["F002"],"text":"yapısı düzgün ve sağlıklı olmak","usage_role":"contextual"}],"definition":"Bir şeyi eğrilik, eksiklik ya da yapısal bozukluktan arındırarak kendi içinde düzgün ve tam duruma getirme; varlığın bu düzgün, sağlıklı ya da iyi durumda bulunması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin kendi yapısı içinde eğrilikten kurtulması ve düzgün duruma gelmesi çekirdektir."},{"facet_id":"F002","role":"specialization","statement":"İnsan yaratılışında düzgünlük, görünür bozukluk ve hastalık bulunmayan tam bir yapıyı anlatır."},{"facet_id":"F003","role":"associated_use","statement":"Çocukların ve hayvanların iyi durumda olması, belirli bir söz kalıbına bağlı değerlendirmedir."}],"identity_rationale":"Kaynak anlatımı bir şeyin eğrilikten kurtulup kendi yapısı içinde düzgünleşmesini, eksiksiz ve sağlıklı duruma gelmesini açıkça aynı dalda toplar.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir şeyi düzeltip düzgün ya da eksiksiz duruma getirmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"eğrilikten kurtulup doğrulmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yapısı düzgün, eksiksiz ve sağlıklı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"çocuklarımız ve hayvanlarımız iyi durumda"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"düz arazi"}],"lexicalization_note":"Tanım yalın düzgünleşme anlamını korur; arazi, çocuklar ve hayvanlarla kurulan özel sözlerin kapsamını ayrıca belirtir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğrultma ve dengeli olma dalı, yapısal düzgünlükle en güçlü anlam örtüşmesini gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tek varlığın yapısal tamlığına ve sağlığına uzanır; komşu dal ise doğrultma eylemi ile beden veya sıcaklık dengesini daha belirgin biçimde öne çıkarır.","focus_only":"Odak dal, sağlıklı ve eksiksiz yaratılış ile çocukların ve hayvanların iyi durumunu da kapsar.","gloss":"doğrultma ve dengeli olma","neighbor_only":"Komşu dal, bir şeyi doğrultma eylemini ve organlar ile sıcaklık arasındaki dengeyi ayrıca kapsar.","neighbor_ref":"root_000991/B005","relation_type":"near_synonym","shared_zone":"İki dal da eğrilik ya da dengesizlikten uzak, düzgün bir durumu anlatır."}],"source_phrase_ar":"سويت الشيء فاستوى (ayn;sihah)؛ استوى من اعوجاج (sihah;tahdhib)؛ السوي الذي سوى الله خلقه لا دمامة فيه ولا داء (ayn)؛ السوي فعيل في معنى مفتعل أي مستو (tahdhib)؛ السوي يقال فيما يصان عن الإفراط والتفريط (mufradat)؛ أولادنا وماشيتنا سوية صالحة (maqayis;tahdhib)","source_summary":"Kaynaklar düzgünleştirme ile düzgün duruma gelmeyi birbirine bağlı verir; insan yapısındaki sağlık ve tamlık ile ev halkı ve hayvanların iyi durumu bu çekirdeğin özel görünümleridir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه تسوية الشيء حتى يستوي، والاعتدال بعد اعوجاج، والسوي في الخلق أو الخلق، وصلاح الأولاد والماشية.","what_is_not_ar":"ليس هو المعادلة بين شيئين، ولا العلو على شيء، ولا سوى بمعنى غير."},"support_links":["sup_4b626362257e695f0b1a","sup_ddc77dc0f5d17d05d359"]},{"boundary":"Anlam yalnız üzerine gelme yapısına bağlıdır; bir yöne yönelme ya da iki şeyin eşitliği bu dala girmez.","branch_kind":"collocation","branch_ref":"root_000766/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","surface_ar":"سَوَّىٰ"}],"gloss":"üzerine çıkıp yerleşmek veya egemen olmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bineğin ya da başka bir şeyin üstüne çıkmak ve onun üzerinde yerleşmek temel somut kullanımdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı yapı üstün gelip denetimi ele alma ve egemen olma anlamına genişleyebilir."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Üzerine gelme bildiren yapı içindeki somut yükselme ve bağlamsal egemenlik kullanımlarına özgüdür.","boundary_detail":"Anlam yalnız üzerine gelme yapısına bağlıdır; bir yöne yönelme ya da iki şeyin eşitliği bu dala girmez.","branch_image_ar":"علو واستقرار على شيء","concept_gloss":"üzerine çıkıp yerleşmek veya egemen olmak","contextual_glosses":[{"applicability":"Bir kişinin bineğin sırtına çıkarak üzerinde oturması ya da durması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yukarı çıkma hedefini ve çıkıştan sonra üzerinde yerleşme sonucunu korur."},"facet_ids":["F001"],"text":"bineğin sırtına çıkıp yerleşmek","usage_role":"contextual"},{"applicability":"Bedensel çıkıştan çok güç ve denetim üstünlüğünün anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Üstünlük kurma ve denetimi ele geçirme genişlemesini korur."},"facet_ids":["F002"],"text":"üstün gelip egemen olmak","usage_role":"contextual"}],"definition":"Üzerine gelme bildiren yapı içinde bir şeyin üstüne çıkıp orada yerleşme; bağlama göre üstünlük kurup egemen duruma gelme.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bineğin ya da başka bir şeyin üstüne çıkmak ve onun üzerinde yerleşmek temel somut kullanımdır."},{"facet_id":"F002","role":"extension","statement":"Aynı yapı üstün gelip denetimi ele alma ve egemen olma anlamına genişleyebilir."}],"identity_rationale":"Kaynak anlatımı, üzerine gelme bildiren yapı içinde hem bir bineğin üstüne çıkıp yerleşmeyi hem de üstün gelip egemen olmayı verir; bu nedenle dal yalnız bedensel yükselişle sınırlandırılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bineğinin sırtına çıkıp yerleşmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"üzerine çıkmak ya da egemen olmak"}],"lexicalization_note":"Tanım yalnız üzerine gelme bildiren yapıya bağlanır ve bu yapının yükselme, yerleşme ve egemen olma kapsamını korur.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; seçilen komşu somut binme kesişimini gösterirken dalın yerleşme ve egemenlik sınırını da belirginleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal belirli binme ve çiftleşme eylemlerine odaklanır; odak dal ise üzerine gelme yapısında yerleşmeyi ve egemenlik genişlemesini de taşır.","focus_only":"Odak dal, çıkıştan sonra üstte yerleşmeyi ve bağlama göre egemenlik kurmayı içerir.","gloss":"bir canlının üstüne çıkma","neighbor_only":"Komşu dal, kişinin ata sıçrayarak binmesini ve erkek hayvanın dişinin üstüne çıkmasını anlatır.","neighbor_ref":"root_000459/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir canlının başka bir canlının sırtına ya da üstüne çıkması bulunur."}],"source_phrase_ar":"استوى على ظهر دابته أي علا واستقر (sihah)؛ استويت فوق الدابة وعلى ظهر الدابة أي علوته (tahdhib)؛ استوى أي استولى وظهر (sihah)؛ متى عدي بعلى اقتضى معنى الاستيلاء (mufradat)","source_summary":"Kaynak anlatımı, üzerine çıkıp yerleşme ile üstünlük kurma arasında yapıya bağlı bir anlam alanı kurar; somut binme örneği çekirdeği, egemenlik ise bağlamsal genişlemeyi gösterir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه استوى على الدابة أو فوقها بمعنى علا واستقر، واستوى على بمعنى علا أو استولى وظهر في الشواهد التي تذكرها المصادر.","what_is_not_ar":"ليس هو استوى إلى بمعنى قصد، ولا تساوى بمعنى تعادل، ولا استواء الخلقة."},"support_links":[]},{"boundary":"Bu anlam yönelme bildiren yapıya bağlıdır; üzerine çıkma, kendi içinde düzgünleşme ve eşitlik anlamlarından ayrıdır.","branch_kind":"collocation","branch_ref":"root_000766/B004","candidate_links":[{"candidate_id":"cand_2e9347d6053a69cd5f71","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","surface_ar":"سَوَّىٰ"}],"gloss":"bir hedefe yönelip onu amaç edinmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir hedefe yönelmek ve onu amaç edinmek yapının temel anlamıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yöneliş bazı açıklamalarda hedefe erişme, bazılarında hedefle ilgili işi düzenleme olarak belirginleşir."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yönelme bildiren yapı içinde hedefe dönme, onu amaçlama ve ona yönelik işe koyulma bağlamlarında kullanılır.","boundary_detail":"Bu anlam yönelme bildiren yapıya bağlıdır; üzerine çıkma, kendi içinde düzgünleşme ve eşitlik anlamlarından ayrıdır.","branch_image_ar":"إقبال وقصد إلى جهة","concept_gloss":"bir hedefe yönelip onu amaç edinmek","contextual_glosses":[{"applicability":"Göğün hedef olarak gösterildiği ve hareket ya da yönelişin öne çıktığı bağlam için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli hedefe doğru yönelme ve onu amaç edinme özelliklerini korur."},"facet_ids":["F001"],"text":"göğe yönelmek","usage_role":"contextual"},{"applicability":"Bedensel hareket yerine hedefle ilgili işi yönetme yorumunun gerektiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hedefe yönelişi ve onunla ilgili işi amaçlı biçimde yürütmeyi korur."},"facet_ids":["F002"],"text":"ona yönelik işi düzenlemeye koyulmak","usage_role":"explanatory"}],"definition":"Bir hedefe doğru yönelmek ve onu amaç edinmek; bağlama göre hedefe varmaya ya da onunla ilgili işi düzenlemeye koyulmak.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir hedefe yönelmek ve onu amaç edinmek yapının temel anlamıdır."},{"facet_id":"F002","role":"source_variant","statement":"Yöneliş bazı açıklamalarda hedefe erişme, bazılarında hedefle ilgili işi düzenleme olarak belirginleşir."}],"identity_rationale":"Kaynak anlatımı bir hedefe yönelme ve onu amaçlama yanında hedefe erişme ya da ona yönelik işi düzenleme yorumlarını da içerir; dal yalnız devinim başlangıcına indirgenemez.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"göğe yönelmek, ona varmak ya da ona yönelik işi düzenlemek"}],"lexicalization_note":"Tanım yalnız bir hedefe doğru yönelme bildiren yapıyı açıklar; bunu yalın kökün genel anlamı gibi sunmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yönelme dalı çekirdek örtüşmeyi ve odak dalın yapıya bağlı özel sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel amaçlama ve yaklaşma alanındadır; odak dal ise belirli bir dil yapısına bağlı olup hedefe erişme veya hedefle ilgili işi düzenleme yorumunu da taşır.","focus_only":"Odak dal belirli bir yönelme yapısına bağlıdır ve hedefe erişme ya da işi düzenleme yorumuna açılır.","gloss":"bir şeye yönelmek","neighbor_only":"Komşu dal, bir şeyi düşünceye alma, ona gelme ve onu amaçlama eylemlerini daha geniş biçimde kapsar.","neighbor_ref":"root_001230/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da belirli bir şeyi hedef seçip ona doğru yönelmeyi anlatır."}],"source_phrase_ar":"استوى إلى السماء أي قصد (sihah)؛ استوى علي وإلي يشاتمني على معنى أقبل إلي وعلي (tahdhib)؛ ثم استوى إلى بلد معناه قصد بالاستواء إليه (tahdhib)؛ إذا عدي بإلى اقتضى معنى الانتهاء إليه إما بالذات أو بالتدبير (mufradat)","source_summary":"Ortak çekirdek bir hedefe dönme ve onu amaç edinmedir; toplu kaynak anlatımı bu yönelişin hedefe varma veya hedefle ilgili işi yürütme biçiminde yorumlanabildiğini gösterir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه استوى إلى الشيء بمعنى قصد أو أقبل أو انتهى إليه، وما قارب ذلك من صعود أو تدبير بحسب عبارة المصدر.","what_is_not_ar":"ليس هو العلو على شيء بحرف على، ولا سوى بمعنى غير، ولا مجرد مساواة."},"support_links":["sup_1083d930d3d7d799b1d1"]},{"boundary":"Dal insanın gençlik olgunluğuna erişmesiyle sınırlıdır; doğuştan düzgün yapı ya da hayvanın yaş basamağı değildir.","branch_kind":"bare","branch_ref":"root_000766/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","surface_ar":"سَوَّىٰ"}],"gloss":"gençlik olgunluğuna erişmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın gençlik dönemindeki gelişiminin tamamlanması temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu tamamlanma güç, beden yapısı ve kavrayışın olgunlaşmasıyla açıklanır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kırk yaş, olgunluğun kendisi değil, kaynak anlatımında verilen olası bir yaş sınırıdır."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir insanın gençlik gelişimini tamamlayıp güç ve kavrayış bakımından olgunlaşmasını anlatır.","boundary_detail":"Dal insanın gençlik olgunluğuna erişmesiyle sınırlıdır; doğuştan düzgün yapı ya da hayvanın yaş basamağı değildir.","branch_image_ar":"بلوغ وتمام الشباب","concept_gloss":"gençlik olgunluğuna erişmek","contextual_glosses":[{"applicability":"Yaştan çok gençlik döneminin sona erip gelişimin tamamlanmasının vurgulandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gençlik döneminin sonuna erişme ve gelişimin tamamlanması anlamını korur."},"facet_ids":["F001"],"text":"gençliği tamamlanmak","usage_role":"contextual"},{"applicability":"Olgunluğun bedensel güç ve kavrayış bakımından açılması gereken bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel güç ile kavrayışın birlikte olgunlaşması anlamını korur."},"facet_ids":["F002"],"text":"gücü ve kavrayışı olgunlaşmak","usage_role":"explanatory"}],"definition":"Bir insanın gençliğinin sonuna erişerek bedensel gücünün, yapısının ve kavrayışının olgunlaşıp tamamlanması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın gençlik dönemindeki gelişiminin tamamlanması temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Bu tamamlanma güç, beden yapısı ve kavrayışın olgunlaşmasıyla açıklanır."},{"facet_id":"F003","role":"source_variant","statement":"Kırk yaş, olgunluğun kendisi değil, kaynak anlatımında verilen olası bir yaş sınırıdır."}],"identity_rationale":"Kaynak anlatımı insanın gençliğinin tamamlanmasını, gücünün ve kavrayışının olgunlaşmasını bu dalda toplar; belirli bir yaş yalnız olası bir sınır açıklamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"gençliğinin sonuna erişip gücü ve kavrayışı olgunlaşmak"}],"lexicalization_note":"Tanım yalın dalın insan gençliğinin tamamlanması anlamını verir ve başka dallardaki özel yapılardan anlam aktarmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; seçilen komşu olgunlaşma alanını paylaşır, ancak insan ile hayvan ve gelişim ölçüsü ayrımını açık tutar.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal insan gençliğinin bedensel ve kavrayışsal tamamlanmasıdır; komşu dal ise hayvanlara özgü yaş sınıflarını ve yetişkinlik ölçülerini anlatır.","focus_only":"Odak dal insanın gençliğinin, gücünün ve kavrayışının tamamlanmasını anlatır.","gloss":"yaşça olgunlaşma","neighbor_only":"Komşu dal hayvanın belirli yaş basamaklarına erişmesini ve özellikle atın yaşça olgunlaşmasını anlatır.","neighbor_ref":"root_000517/B004","relation_type":"same_field","shared_zone":"İki dal da canlı bir varlığın gelişim sürecinde olgunluk sınırına erişmesiyle ilgilidir."}],"source_phrase_ar":"استوى الرجل إذا انتهى شبابه (sihah)؛ بلغ أشده واستوى قيل بلغ الأربعين (tahdhib)؛ المستوي هو الذي تم شبابه (tahdhib)؛ فإذا استويت أنت (mufradat)","source_summary":"Kaynak anlatımının ortak yönü insanın gençliğinin ve gücünün tamamlanmasıdır; kırk yaş açıklaması çekirdeği değiştiren zorunlu bir koşul değil, olgunluğun sınırına ilişkin bir yorumdur.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه استوى الرجل إذا انتهى شبابه أو تمت قوته وخلقه وعقله، وما قيل في بلوغ الأشد أو الأربعين.","what_is_not_ar":"ليس هو صحة الخلقة ابتداء، ولا استواء الدابة، ولا التسوية بين شيئين."},"support_links":[]},{"boundary":"Dal yer ve tutum bakımından ortalık ile yansızlığı kapsar; iki nesnenin yalnız ölçü bakımından eşit olması değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000766/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","surface_ar":"سَوَّىٰ"}],"gloss":"iki yanın ortasında ve ikisine karşı yansız olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünün ya da yerin iki uç arasında kalan orta bölümü somut çekirdektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ortalık ilişkisi, taraflara eşit davranan yansız ve hak gözetir tutuma genişler."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli yer kullanımında iki yana denk, ortada ve herkesçe bilinen buluşma yeri anlatılır."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Somut orta konumu ve bu konumdan gelişen iki tarafa eşit, hak gözetir tutumu birlikte anlatır.","boundary_detail":"Dal yer ve tutum bakımından ortalık ile yansızlığı kapsar; iki nesnenin yalnız ölçü bakımından eşit olması değildir.","branch_image_ar":"وسط وعدل ومكان منصف","concept_gloss":"iki yanın ortasında ve ikisine karşı yansız olma","contextual_glosses":[{"applicability":"Bir yerin ya da bütünün iki uç arasında kalan orta bölümünü gösteren bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütünün iki ucu arasında kalan somut orta konumu korur."},"facet_ids":["F001"],"text":"tam ortasında","usage_role":"contextual"},{"applicability":"Taraflar arasında hak gözeten bir yer, söz ya da tutumun anlatıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taraflara denk uzaklığı, yansızlığı ve hak gözetme niteliğini korur."},"facet_ids":["F002","F003"],"text":"iki tarafa da eşit ve yansız","usage_role":"contextual"}],"definition":"Bir şeyin iki uç ya da yan arasında ortada bulunması; yer veya tutumun taraflara eşit uzaklıkta, yansız ve hak gözetir olması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünün ya da yerin iki uç arasında kalan orta bölümü somut çekirdektir."},{"facet_id":"F002","role":"extension","statement":"Ortalık ilişkisi, taraflara eşit davranan yansız ve hak gözetir tutuma genişler."},{"facet_id":"F003","role":"specialization","statement":"Belirli yer kullanımında iki yana denk, ortada ve herkesçe bilinen buluşma yeri anlatılır."}],"identity_rationale":"Kaynak anlatımı somut orta konumu, iki yana eşit ve herkesçe bilinen yeri, ayrıca hak gözeten ortak tutumu aynı dalda verir; bunlar tek bir belirsiz orta sözüne indirgenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"orta; iki yana eşit ve yansız durum"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"iki yana eşit, ortada ve herkesçe bilinen yer"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"iki tarafın da hakkını gözeten ortak söz"}],"lexicalization_note":"Tanım yalın orta ve yansızlık anlamlarını ayırır; yer ve söz bildiren özel yapıların koşullarını bütün dala yaymaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; seçilen komşu orta ile hak gözetme bağını paylaşırken somut yer ve ölçülü davranış kapsamlarını ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal somut orta ve iki tarafa denk yer anlamını korur; komşu dal ise ölçülülük ve seçkinlik değerlendirmesine daha geniş biçimde uzanır.","focus_only":"Odak dal somut bir yerin ortasını ve taraflara eşit uzaklıktaki belirli yeri de anlatır.","gloss":"ölçülü ve hak gözetir orta","neighbor_only":"Komşu dal ölçülülüğü, aşırılıklardan kaçınmayı ve bir topluluğun en seçkin üyelerini de anlatır.","neighbor_ref":"root_001646/B001","relation_type":"near_synonym","shared_zone":"İki dal da uçlardan uzak orta konumu hak gözetme ve yansızlıkla ilişkilendirir."}],"source_phrase_ar":"السواء ممدود وسط كل شيء (ayn)؛ مكانا سوى أي معلما قد علم القوم به (ayn;maqayis)؛ مكان سوى أي عدل ووسط (sihah)؛ السواء وسط الدار وغيرها (maqayis)؛ سواء بمعنى العدل والنصفة (tahdhib)؛ كلمة سواء أي عدل (tahdhib;mufradat)؛ في سواء الجحيم (maqayis;mufradat)","source_summary":"Kaynaklar somut ortayı temel alır ve bu ilişkiyi iki taraf arasında yansız, hak gözetir konuma taşır; yer ve ortak söz kullanımları bu iki yönün belirli bağlamlardaki biçimleridir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه السواء وسط الشيء أو الدار، وسواء السبيل، وكلمة سواء، وعلى سواء، ومكان سوى بمعنى وسط أو عدل أو منصف أو مستو معلوم.","what_is_not_ar":"ليس هو المثلية بين شيئين من جهة المقدار فقط، ولا سوى بمعنى غير، ولا الفضاء الواسع المسمى السي."},"support_links":[]},{"boundary":"Dal başkalık ve ayrılık bildirir; orta konum, eşitlik ya da aynı şeyin kendisi olma anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_000766/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","surface_ar":"سَوَّىٰ"}],"gloss":"başka ve ayrı olan","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığın söz konusu varlıkla aynı olmayıp ondan başka olması temel anlamdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başkalık, bazı bağlamlarda birinin yerinde bulunan ya da onun yerine geçen ötekiyi gösterir."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi ya da şeyin söz konusu olandan farklı olduğunu veya onun yerine geçen öteki olduğunu anlatır.","boundary_detail":"Dal başkalık ve ayrılık bildirir; orta konum, eşitlik ya da aynı şeyin kendisi olma anlamlarını kapsamaz.","branch_image_ar":"مباينة وكون الشيء غيره","concept_gloss":"başka ve ayrı olan","contextual_glosses":[{"applicability":"Bir varlığı belirtilen kişi ya da şeyin dışında tutan kısa kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirtilen varlıkla aynı olmama ve onun dışında kalma anlamını korur."},"facet_ids":["F001"],"text":"ondan başka","usage_role":"contextual"},{"applicability":"Bir kişinin yerinde bulunan ya da onun yerine düşünülen başka kişiyi anlatırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başkalığı ve belirtilen kişinin yerini tutma ilişkisini korur."},"facet_ids":["F002"],"text":"onun yerine bir başkası","usage_role":"contextual"}],"definition":"Bir kişi ya da şeyin söz konusu olandan başka, ayrı veya onun yerini tutan bir öteki olması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığın söz konusu varlıkla aynı olmayıp ondan başka olması temel anlamdır."},{"facet_id":"F002","role":"extension","statement":"Başkalık, bazı bağlamlarda birinin yerinde bulunan ya da onun yerine geçen ötekiyi gösterir."}],"identity_rationale":"Kaynak anlatımı temel olarak bir şeyin ötekinden başka ve ayrı olmasını verir; birinin yerinde ya da onun yerine bulunma açıklaması bu başkalığın bağlamsal görünümüdür.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"başka, öteki"}],"lexicalization_note":"Tanım yalın başkalık anlamıyla sınırlıdır ve örneklerdeki yerine geçme yorumunu zorunlu çekirdek yapmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; seçilen komşu yalın başkalıkla en güçlü örtüşmeyi gösterir ve dilbilgisel genişlemeleriyle ayrılır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalın başkalık ve yerine bulunma ilişkisine bağlıdır; komşu dal ise başkalığı karşıtlık, dışarıda bırakma ve olumsuzlama görevlerine kadar genişletir.","focus_only":"Odak dal bir başkasının yerinde ya da yerine bulunan öteki yorumunu da taşır.","gloss":"başkalık ve dışarıda bırakma","neighbor_only":"Komşu dal başkalık yanında karşıtlık, dışarıda bırakma, olumsuzlama ve dilbilgisel görevleri de kapsar.","neighbor_ref":"root_001119/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi ya da şeyin söz konusu olandan başka olduğunu bildirir."}],"source_phrase_ar":"سوى مقصور إذا كان في موضع غير (ayn)؛ سواء الشيء غيره (sihah;tahdhib)؛ مررت برجل سواك أي غيرك (sihah)؛ هذا سوى ذلك أي غيره (maqayis)؛ يستعمل سوى وسواء بمعنى غير (mufradat)؛ عندي رجل سواك أي مكانك وبدلك (mufradat)","source_summary":"Kaynakların ortak çekirdeği aynılık dışındaki başkalık ve ayrılıktır; yer veya yerini tutma açıklaması bu başkalığın belirli bir kişiyle kurulan ilişkide aldığı biçimdir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه سوى وسواء بمعنى غير، والبدل أو المكان المنفصل عن المخاطب في نحو عندي رجل سواك.","what_is_not_ar":"ليس هو السواء بمعنى الوسط أو العدل، ولا سوى بمعنى نفس الشيء في النقل المختلف."},"support_links":[]},{"boundary":"Dal yalnız verilen söz yapısında yön ve hedef bildirir; genel başkalık ya da bağımsız amaçlama anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000766/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","surface_ar":"سَوَّىٰ"}],"gloss":"birinin yöneldiği hedefe yönelmek","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin kendisini değil, onun tuttuğu yönü veya amaçladığı hedefi izlemek temel ilişkidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözün ya da övgünün belirli bir kişiye çevrilmesi, yönelme ilişkisinin söylem alanındaki kullanımıdır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Atışın iki hedefin bulunduğu yönü tutturamaması, doğrultunun hedefle ilişkisini gösterir."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız belirli söz yapısı içinde bir kişinin yönünü ya da hedefini izlemeyi anlatan kullanımlara uygundur.","boundary_detail":"Dal yalnız verilen söz yapısında yön ve hedef bildirir; genel başkalık ya da bağımsız amaçlama anlamı değildir.","branch_image_ar":"قصد نحو شخص أو جهة","concept_gloss":"birinin yöneldiği hedefe yönelmek","contextual_glosses":[{"applicability":"Bir kişinin seçtiği doğrultunun izlenmesi veya onun hedefinin hedeflenmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin tuttuğu doğrultuyu ve aynı yöne dönme eylemini korur."},"facet_ids":["F001"],"text":"onun tuttuğu yöne yönelmek","usage_role":"contextual"},{"applicability":"Bir sözün ya da övgünün belirli bir kişiye çevrilmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Söylemin yönünü belirli kişiye çevirme ilişkisini korur."},"facet_ids":["F002"],"text":"övgüyü ona yöneltmek","usage_role":"contextual"}],"definition":"Belirli söz yapısı içinde bir kişinin yöneldiği hedefe ya da doğrultuya yönelmek; sözü veya övgüyü o doğrultudaki kişiye çevirmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin kendisini değil, onun tuttuğu yönü veya amaçladığı hedefi izlemek temel ilişkidir."},{"facet_id":"F002","role":"associated_use","statement":"Sözün ya da övgünün belirli bir kişiye çevrilmesi, yönelme ilişkisinin söylem alanındaki kullanımıdır."},{"facet_id":"F003","role":"example","statement":"Atışın iki hedefin bulunduğu yönü tutturamaması, doğrultunun hedefle ilişkisini gösterir."}],"identity_rationale":"Kaynak deyim belirli bir kişiyi doğrudan hedeflemekten çok onun yöneldiği yöne ya da hedefe yönelmeyi anlatır; övgünün birine çevrilmesi ve hedefi ıskalama örneği de yön doğrultusunu öne çıkarır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"birinin tuttuğu yöne ya da hedefe yönelmek"}],"lexicalization_note":"Tanım belirli söz yapısına bağlı yönelme anlamını korur ve bunu yalın biçime ait genel bir anlam olarak sunmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen komşu hedefe yönelme çekirdeğini paylaşır ve odak dalın kişi üzerinden kurulan yapısal sınırını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel ve doğrudan amaçlamayı anlatır; odak dal ise başka birinin yönünü izleyen, belirli söz yapısına bağlı dolaylı yöneliştir.","focus_only":"Odak dal yalnız belirli bir söz yapısında başka bir kişinin tuttuğu yönü ya da hedefi izler.","gloss":"amaçlayıp hedefe yönelmek","neighbor_only":"Komşu dal genel amaçlama, bilinçli yönelme ve ok ya da mızrağı doğrudan hedefe çevirme eylemlerini kapsar.","neighbor_ref":"root_000053/B012","relation_type":"near_synonym","shared_zone":"İki dal da bir hedef seçme ve hareketi ya da dikkati o hedefe çevirme alanında buluşur."}],"source_phrase_ar":"يقال قصدت سوى فلان كما يقال قصدت قصده (maqayis)؛ قصدت سوى فلان أي قصدت قصده (sihah)؛ فلأصرفن سوى حذيفة مدحتى (maqayis;sihah)؛ وقع المزار على سواهما أخطأهما (tahdhib)","source_summary":"Kaynak anlatımı birinin tuttuğu yönü hedef alma çekirdeğinde birleşir; övgünün o yana çevrilmesi ve atışın hedefleri ıskalaması bu yön ilişkisinin farklı bağlamlarıdır.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه قصدت سوى فلان بمعنى قصدت قصده، وصرف الكلام أو المدح نحو شخص.","what_is_not_ar":"ليس هو سوى بمعنى غير، ولا استوى إلى السماء بالتركيب الفعلي، ولا المساواة."},"support_links":[]},{"boundary":"Dal açık ve geniş yer ile buna bağlı bolluğu anlatır; eş, orta ya da deve sırtlığı anlamlarından ayrıdır.","branch_kind":"bare","branch_ref":"root_000766/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","surface_ar":"سَوَّىٰ"}],"gloss":"geniş ve açık arazi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ufku açık, geniş bir arazi parçası dalın temel yer anlamıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir anlatım bu geniş yeri özellikle bozkırdaki pürüzsüz bir alan olarak sınırlar."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Arazinin genişliği, otlağın veya suyun çok ve yaygın oluşunu anlatmaya genişler."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Geniş, açık ve kimi bağlamlarda pürüzsüz bir bozkır yerini anlatan yalın yer adı için uygundur.","boundary_detail":"Dal açık ve geniş yer ile buna bağlı bolluğu anlatır; eş, orta ya da deve sırtlığı anlamlarından ayrıdır.","branch_image_ar":"السِيّ واسع أملس من الأرض","concept_gloss":"geniş ve açık arazi","contextual_glosses":[{"applicability":"Arazinin hem genişliği hem de bozkır içindeki pürüzsüz yüzeyi öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Genişliği, açıklığı, bozkır bağlamını ve pürüzsüz yüzey niteliğini korur."},"facet_ids":["F001","F002"],"text":"geniş, düz ve açık bozkır yeri","usage_role":"contextual"},{"applicability":"Otlak ya da suyun geniş alana yayılan çokluğunu anlatan uzantı kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mekânsal genişliğin ot veya su bolluğuna taşınan uzantısını korur."},"facet_ids":["F003"],"text":"bol ve yaygın","usage_role":"contextual"}],"definition":"Geniş, açık ve yer yer pürüzsüz bir arazi ya da bozkır yeri; buradaki mekânsal genişlikten hareketle ot veya suyun bol ve yaygın oluşu.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ufku açık, geniş bir arazi parçası dalın temel yer anlamıdır."},{"facet_id":"F002","role":"source_variant","statement":"Bir anlatım bu geniş yeri özellikle bozkırdaki pürüzsüz bir alan olarak sınırlar."},{"facet_id":"F003","role":"extension","statement":"Arazinin genişliği, otlağın veya suyun çok ve yaygın oluşunu anlatmaya genişler."}],"identity_rationale":"Kaynak anlatımı geniş açık araziyi temel alır, fakat bir aktarımda bozkırdaki pürüzsüz yer öne çıkar; otlak ve su için kullanılan bolluk anlatımı ise bu mekânsal genişliğin uzantısıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"geniş, açık ya da pürüzsüz arazi"}],"lexicalization_note":"Tanım yalın arazi adını temel alır ve otlak ile suya ilişkin bolluk kullanımını ona bağlı bir genişleme olarak tutar.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; seçilen komşu açık arazi çekirdeğini paylaşır ve bozkır, pürüzsüzlük ile bolluk sınırlarını görünür kılar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal geniş bozkır ve pürüzsüz arazi çevresinde toplanıp bolluğa uzanır; komşu dal ise farklı türden çıplak ve açık yerleri daha geniş bir adlandırma alanında toplar.","focus_only":"Odak dal pürüzsüz bozkır yerini ve ot ile suyun bol oluşuna uzanan kullanımı içerir.","gloss":"örtüsüz açık alan","neighbor_only":"Komşu dal boş yer, avlu, yüzey, yan ve örtüsüz alan gibi daha çeşitli açık yer türlerini kapsar.","neighbor_ref":"root_001005/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da üstü örtülü olmayan, açık ve geniş bir kara parçasını anlatabilir."}],"source_phrase_ar":"السِيّ الفضاء من الأرض الواسع (jamhara)؛ ومن الباب السِيّ الفضاء من الأرض (maqayis)؛ السِيّ موضع بالبادية أملس (ayn)؛ نزلنا في كلاء سِيّ وأنبط ماء سِيًّا أي كثيرا واسعا (tahdhib)","source_summary":"Kaynak anlatımında geniş açık arazi ortak çekirdektir; pürüzsüz bozkır yeri bunun daha dar betimlemesi, ot ve su bolluğu ise genişlik düşüncesinin nitelik alanına taşınmasıdır.","sources":["AY","JA","TA","MQ"],"what_is_ar":"يدخل فيه السِيّ بمعنى الفضاء الواسع من الأرض أو الموضع الأملس، وما وصف من كلأ أو ماء بالسعة والكثرة.","what_is_not_ar":"ليس هو السِيّ بمعنى المثل، ولا السَّويّة التي تلقى على البعير، ولا السواء وسط الشيء."},"support_links":[]},{"boundary":"Dal deve sırtında binmek için kullanılan nesneye özgüdür; eşitleme, açık arazi ya da yay parçası anlamı değildir.","branch_kind":"bare","branch_ref":"root_000766/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","surface_ar":"سَوَّىٰ"}],"gloss":"devenin sırtına konan dolgulu binme örtüsü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne devenin sırtına yerleştirilir ve binicinin oturmasına ya da binmesine yarar."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak anlatımları nesneyi sırtlık, sarılı örtü veya bitki sapı ve lifle doldurulmuş örtü biçimlerinde betimler."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Örtü biçimi devenin hörgücünün çevresini sararak binici için oturma yeri oluşturur."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Devenin sırtı ya da hörgücü çevresinde binicinin oturmasını sağlayan örtü veya sırtlık türü araç için kullanılır.","boundary_detail":"Dal deve sırtında binmek için kullanılan nesneye özgüdür; eşitleme, açık arazi ya da yay parçası anlamı değildir.","branch_image_ar":"السَّويّة على ظهر البعير","concept_gloss":"devenin sırtına konan dolgulu binme örtüsü","contextual_glosses":[{"applicability":"Nesnenin örtü yapısından çok deve üzerinde binmeye yarayan sırtlık oluşu öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sarılı veya içi bitki sapı ve lifle doldurulmuş örtü biçimi belirtilmez.","preserves":"Deve sırtındaki konumu ve biniciyi taşıyan araç olma işlevini korur."},"facet_ids":["F001"],"text":"deve sırtlığı","usage_role":"contextual"},{"applicability":"Aracın hörgüç çevresine sarılan ve biniciye oturma yeri sağlayan örtü biçimi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hörgüç çevresindeki yerleşimi, örtü yapısını ve binme işlevini korur."},"facet_ids":["F001","F003"],"text":"hörgüç çevresine sarılan binme örtüsü","usage_role":"explanatory"}],"definition":"Devenin sırtına ya da hörgücünün çevresine konup binmeye yarayan, kimi biçimi sarılı veya dolgulu örtüye, kimi biçimi sırtlığa benzeyen araç.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne devenin sırtına yerleştirilir ve binicinin oturmasına ya da binmesine yarar."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak anlatımları nesneyi sırtlık, sarılı örtü veya bitki sapı ve lifle doldurulmuş örtü biçimlerinde betimler."},{"facet_id":"F003","role":"specialization","statement":"Örtü biçimi devenin hörgücünün çevresini sararak binici için oturma yeri oluşturur."}],"identity_rationale":"Kaynak anlatımları aynı nesneyi kimi yerde deve için bir sırtlık, kimi yerde hörgüç çevresine sarılan ya da doldurulan örtü olarak açıklar; tanım bu yapım ve biçim çeşitliliğini korumalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"devenin sırtına ya da hörgücü çevresine konan binme örtüsü"}],"lexicalization_note":"Tanım yalın nesne adını verir ve kaynaklardaki sırtlık, dolgulu örtü ve hörgüç çevresi biçimlerini aynı araç altında toplar.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; seçilen komşu nesne ve işlev bakımından en yakın eşleşmedir, ancak daha büyük taşıma düzeneği kapsamıyla ayrılır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal deve sırtlığı ve dolgulu örtü biçiminde sınırlıdır; komşu dal buna ek olarak kapalı ya da sedye benzeri taşıma düzeneklerini de kapsar.","focus_only":"Odak dal deveye özgü sırtlık ya da dolgulu örtüyü ve hörgüç çevresindeki yerleşimini anlatır.","gloss":"biniciyi saran deve örtüsü","neighbor_only":"Komşu dal kadın için hazırlanan taşıma düzeneğini ve sedye benzeri daha büyük bir binme aracını da kapsar.","neighbor_ref":"root_000374/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da deve sırtında veya hörgüç çevresinde biniciyi taşıyan örtülü bir düzenek anlatabilir."}],"source_phrase_ar":"السَّويّة قتب أعجمي للبعير والجميع السوايا (ayn;tahdhib)؛ السَّويّة كساء يلف ويجعل شبيها بالحوية يلقى على سنام البعير (jamhara)؛ السَّويّة كساء محشو بثمام ونحوه كالبرذعة (sihah)؛ كساء محشو بثمام أو ليف يجعل على ظهر البعير (tahdhib)","source_summary":"Ortak işlev devenin sırtında binmeye yarayan bir araç olmaktır; toplu anlatım aracın sırtlık, sarılı örtü veya içi doldurulmuş örtü biçimlerinde tasarlanabildiğini gösterir.","sources":["AY","JA","SI","TA"],"what_is_ar":"يدخل فيه السَّويّة وهي كساء أو قتب أو برذعة تجعل على ظهر البعير أو حول سنامه للركوب.","what_is_not_ar":"ليس هو التسوية بمعنى التعديل، ولا السِيّ الفضاء، ولا سِيَة القوس أو الأسد."},"support_links":[]},{"boundary":"Bu dal bir öğeyi işlem dışında bırakmayı anlatır; düzeltme, eşitleme ya da orta konum bildirmez.","branch_kind":"bare","branch_ref":"root_000766/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","surface_ar":"سَوَّىٰ"}],"gloss":"atlayıp dışarıda bırakmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir öğeyi izlenen işlem ya da sıra içine almadan atlamak temel eylemdir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atlanan öğeyi bırakmak ve ona gereken ilgiyi göstermemek eylemin sonuç yönüdür."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yazı bölümünü veya geçilen bir yeri atlamak, çekirdeğin belirli nesneler üzerindeki örneğidir."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir öğenin sıra, işlem veya anlatım içine alınmayarak bırakılması ve göz ardı edilmesi için uygundur.","boundary_detail":"Bu dal bir öğeyi işlem dışında bırakmayı anlatır; düzeltme, eşitleme ya da orta konum bildirmez.","branch_image_ar":"إسقاط وإغفال","concept_gloss":"atlayıp dışarıda bırakmak","contextual_glosses":[{"applicability":"Bir yazı ya da anlatımdaki parçanın okunmadan veya aktarılmadan geçilmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir bölümün sıra içinde işlenmeden geçilmesi anlamını korur."},"facet_ids":["F001","F003"],"text":"bir bölümü atlamak","usage_role":"contextual"},{"applicability":"Bir şeyin bilinçli ya da sonuç bakımından işlem dışında bırakıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öğeyi bırakma ve ona gereken ilgiyi göstermeme sonucunu korur."},"facet_ids":["F002"],"text":"bırakıp göz ardı etmek","usage_role":"contextual"}],"definition":"Bir şeyi izlenen sıra, işlem ya da anlatım içinde atlayarak dışarıda bırakma ve ona gereken ilgiyi göstermeme.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir öğeyi izlenen işlem ya da sıra içine almadan atlamak temel eylemdir."},{"facet_id":"F002","role":"extension","statement":"Atlanan öğeyi bırakmak ve ona gereken ilgiyi göstermemek eylemin sonuç yönüdür."},{"facet_id":"F003","role":"example","statement":"Bir yazı bölümünü veya geçilen bir yeri atlamak, çekirdeğin belirli nesneler üzerindeki örneğidir."}],"identity_rationale":"Kaynak anlatımı bir şeyi, yazıdaki bir bölümü ya da geçilen bir yeri atlama, bırakma ve göz ardı etme işlemini açıkça aynı çekirdekte birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"atlamak, dışarıda bırakmak ve göz ardı etmek"}],"lexicalization_note":"Tanım yalın bırakma ve atlama eylemini verir; örneklerdeki yazı parçasını bütün dal için zorunlu nesne saymaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; seçilen komşu bırakma alanını paylaşır ve odak dalın sıradan bir öğeyi atlama özelliğini en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal seçili bir öğeyi atlama ve göz ardı etme işlemidir; komşu dal ise yetersizlikten doğan savsaklama, unutma ve yitirme sonuçlarına daha geniş biçimde uzanır.","focus_only":"Odak dal bir öğeyi sıra, işlem veya anlatım içinde atlayıp dışarıda bırakmayı öne çıkarır.","gloss":"savsaklayıp yitirme","neighbor_only":"Komşu dal yetersiz kalma, savsaklama, unutma, geride bırakma ve bütünüyle yitirme sonuçlarını da kapsar.","neighbor_ref":"root_001145/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeye gereken işlemi veya ilgiyi göstermeyerek onu bırakma alanında buluşur."}],"source_phrase_ar":"أسوى فلان حرفا من كتاب الله أي أسقط وأغفل (ayn)؛ أسويت الشيء أي تركته وأغفلته (sihah)؛ أسوى برزخا ثم رجع إليه (tahdhib)؛ أسوى يعني أسقط وأغفل (tahdhib)","source_summary":"Kaynaklar bir öğeyi sıradan düşürme, üzerinden geçme ve ilgisiz bırakma çekirdeğinde birleşir; yazı bölümü ile geçilen yer bu işlemin ayrı örnekleridir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه أسوى الشيء أو الحرف إذا أسقطه أو تركه وأغفله.","what_is_not_ar":"ليس هو التسوية ولا الاستواء ولا السواء بمعنى العدل."},"support_links":[]},{"boundary":"Dal yalnız ayın on üçüncü gecesinin adıdır; yer ortası, yansızlık ya da genel ay ışığı anlamı değildir.","branch_kind":"bare","branch_ref":"root_000766/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","surface_ar":"سَوَّىٰ"}],"gloss":"ayın on üçüncü gecesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan zaman ayın on üçüncü gecesidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gece adı, ayın o sırada dengeli bir görünüme erişmesi açıklamasıyla ilişkilendirilir."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ayın dengeli göründüğü kabul edilen belirli geceyi takvim içindeki sırasıyla adlandırmak için kullanılır.","boundary_detail":"Dal yalnız ayın on üçüncü gecesinin adıdır; yer ortası, yansızlık ya da genel ay ışığı anlamı değildir.","branch_image_ar":"ليلة استواء القمر","concept_gloss":"ayın on üçüncü gecesi","contextual_glosses":[{"applicability":"Gece adının hem takvimdeki sırası hem de ayın görünümüyle bağı açıklanmak istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"On üçüncü geceyi ve adlandırmanın ayın dengeli görünümüyle kurulan bağını korur."},"facet_ids":["F001","F002"],"text":"ayın dengelendiği on üçüncü gece","usage_role":"explanatory"}],"definition":"Ayın görünümünün dengelendiği kabul edilen, ayın on üçüncü gecesine verilen ad.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan zaman ayın on üçüncü gecesidir."},{"facet_id":"F002","role":"associated_use","statement":"Gece adı, ayın o sırada dengeli bir görünüme erişmesi açıklamasıyla ilişkilendirilir."}],"identity_rationale":"Kaynak anlatımı bu gece adını ayın on üçüncü gecesi olarak belirler ve adlandırmayı ayın o sıradaki dengeli görünümüne bağlar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"ayın dengeli göründüğü on üçüncü gece"}],"lexicalization_note":"Tanım gece adını kendi başına verir ve başka dallardaki orta, eşitlik veya düzgünlük anlamlarını ona taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen komşu aynı gök ve gece alanını paylaşır, ancak belirli gece adıyla genel ay ve ışık anlamını açıkça ayırır.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Odak dal yalnız takvimde belirli bir geceyi adlandırır; komşu dal ise ayın kendisini, ışığını ve aydınlattığı geceleri tarih sırasından bağımsız biçimde kapsar.","focus_only":"Odak dal ay içindeki belirli bir sıraya, on üçüncü geceye verilen addır.","gloss":"ay ve ay ışığı","neighbor_only":"Komşu dal gökteki ayı, onun ışığını ve ay ışığıyla aydınlanan geceleri genel olarak anlatır.","neighbor_ref":"root_001255/B001","relation_type":"thematic","shared_zone":"Her iki dal ayın gece göğündeki görünümü ve aydınlığı çevresindeki aynı zaman alanına bağlıdır."}],"source_phrase_ar":"ليلة السواء ليلة ثلاث عشرة (sihah)؛ السواء ممدود ليلة ثلاث عشرة وفيها يستوي القمر (tahdhib)","source_summary":"Kaynaklar ayın on üçüncü gecesini aynı adla belirler; bunlardan biri adın ayın o gecedeki dengeli görünümüne dayandığını ayrıca açıklar.","sources":["SI","TA"],"what_is_ar":"يدخل فيه ليلة السواء، وهي ليلة ثلاث عشرة عند استواء القمر في النقلين.","what_is_not_ar":"ليس هو السواء بمعنى العدل أو الوسط في المكان."},"support_links":[]},{"boundary":"Dal yalnız baş ölçüsü çevresinde kurulan söz kalıbına bağlıdır; genel eşitlik, para adı ya da herhangi bir mal miktarı değildir.","branch_kind":"collocation","branch_ref":"root_000766/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","surface_ar":"سَوَّىٰ"}],"gloss":"başına denk mal ve bolluk","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Mal miktarı kişinin başına denk sayılan bir ölçüyle anlatılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Baş ölçüsüne denk mal düşüncesi, kişinin bolluk ve iyi yaşam içinde bulunmasını anlatmaya genişler."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız baş ölçüsü çevresinde kurulan kalıp içinde mal miktarını veya kişinin bolluk içindeki durumunu anlatır.","boundary_detail":"Dal yalnız baş ölçüsü çevresinde kurulan söz kalıbına bağlıdır; genel eşitlik, para adı ya da herhangi bir mal miktarı değildir.","branch_image_ar":"سِيّ الرأس وقدر يوازي الرأس من مال أو نعمة","concept_gloss":"başına denk mal ve bolluk","contextual_glosses":[{"applicability":"Kalıbın bir kişinin başına denk sayılan mal miktarını bildirdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin başını ölçü alan denkliği ve bunun mal miktarı oluşunu korur."},"facet_ids":["F001"],"text":"başı ölçüsünde mal","usage_role":"explanatory"},{"applicability":"Aynı söz kalıbının mal ölçüsünden çok kişinin iyi ve bol durumunu anlattığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalıbın kişiye bağlanan bolluk ve iyi yaşam durumunu korur."},"facet_ids":["F002"],"text":"bolluk içinde olmak","usage_role":"contextual"}],"definition":"Belirli söz kalıbında bir kişinin başına denk ya da onu karşılar sayılan mal miktarı; aynı kalıpta kişinin içinde bulunduğu bolluk ve iyi yaşam durumu.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Mal miktarı kişinin başına denk sayılan bir ölçüyle anlatılır."},{"facet_id":"F002","role":"extension","statement":"Baş ölçüsüne denk mal düşüncesi, kişinin bolluk ve iyi yaşam içinde bulunmasını anlatmaya genişler."}],"identity_rationale":"Kaynak anlatımı sabit söz içinde bir kişinin başına denk sayılan mal miktarını verir, fakat aynı kalıp bolluk veya iyi yaşam durumu için de kullanılır; tanım iki görünümü ayırmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"başına denk sayılan mal miktarı ya da bolluk"}],"lexicalization_note":"Tanım yalnız baş ölçüsünü kullanan kalıba bağlanır ve buradaki mal ile bolluk anlamını yalın biçime genellemez.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; kökün genel denklik dalı ölçü ilişkisini açıklar ve bu dalın yalnız belirli söz kalıbına bağlı olduğunu gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel ve üretken denklik alanıdır; odak dal ise yalnız başı ölçü alan kalıpla mal ve bolluk anlatan özel bir kullanımdır.","focus_only":"Odak dal baş ölçüsüne bağlı sabit söz içinde mal miktarını ve bolluk durumunu anlatır.","gloss":"iki şey arasında denklik","neighbor_only":"Komşu dal iki şey arasındaki genel ölçü, değer, nicelik veya nitelik denkliğini ve eşlik kalıplarını kapsar.","neighbor_ref":"root_000766/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir miktarın seçilen ölçüyü karşılaması ve ona denk sayılması ilişkisi vardır."}],"source_phrase_ar":"جاء فلان بسِيّ رأسه من المال أي ما يوازي رأسه (jamhara)؛ وقع فلان في سواء رأسه أي فيما ساوى رأسه من النعمة (tahdhib)؛ هو في سِيّ رأسه وسواء رأسه وهي النعمة (tahdhib)","source_summary":"Kaynak anlatımı başa denk sayılan mal ölçüsü ile bu ölçünün bolluk ve iyi yaşam durumu bildiren kullanımını aynı söz kalıbında birleştirir.","sources":["JA","TA"],"what_is_ar":"يدخل فيه قولهم بسِيّ رأسه أو في سواء رأسه لما يوازي رأسه من مال أو نعمة.","what_is_not_ar":"ليس هو السِيّ بمعنى الفضاء، ولا السِيّ بمعنى المثل المطلق، ولا سواء الشيء بمعنى وسطه."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["87:2:1"],"branch_refs":[],"candidate_id":"cand_5dc2bfeb952895734adb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:2:1:command-to-evidence-register","source_type":"word_analysis","support_ids":["sup_9c02030b6584d274b297","sup_ef2a86fc6759a042b047"],"title":"command register turns into narrated evidence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:1","qac_refs":["87:2:1:1"],"status":"accepted"}},{"anchor_refs":["87:2:1"],"branch_refs":[],"candidate_id":"cand_5dc19dcdc761718bdf73","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:2:1:cross-ayah-relative","source_type":"word_analysis","support_ids":["sup_bf9f3dd0c1cfa4846726","sup_ef2a86fc6759a042b047"],"title":"relative pronoun pulls the prior title forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:1","qac_refs":["87:2:1:1"],"status":"accepted"}},{"anchor_refs":["87:2:1"],"branch_refs":[],"candidate_id":"cand_4cecb9146b8c08270f02","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:2:1:sila-evidentiary-scope","source_type":"word_analysis","support_ids":["sup_d5a84c9edb1361d69d6e","sup_ef2a86fc6759a042b047"],"title":"both verbs become one evidentiary relative clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:1","qac_refs":["87:2:1:1"],"status":"accepted"}},{"anchor_refs":["87:2:2"],"branch_refs":[],"candidate_id":"cand_1040d3b4bb35a2d4912c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000434"],"scope":"focus_ayah","source_local_id":"87:2:2:active-completed-agency","source_type":"word_analysis","support_ids":["sup_74179a7592f2ac0e97a8","sup_df0b049882aa41f98fd0"],"title":"active perfect grounds praise in accomplished agency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:2","qac_refs":["87:2:2:1"],"status":"accepted"}},{"anchor_refs":["87:2:2"],"branch_refs":[],"candidate_id":"cand_ba2f39ffee56204896b3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000434"],"scope":"focus_ayah","source_local_id":"87:2:2:creation-proportion-formula","source_type":"word_analysis","support_ids":["sup_58cba8dd0c974932d7d8","sup_74179a7592f2ac0e97a8"],"title":"first half of a recognized creation-proportion sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:2","qac_refs":["87:2:2:1"],"status":"accepted"}},{"anchor_refs":["87:2:2"],"branch_refs":[],"candidate_id":"cand_a2c39f7f57f40ce52c78","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000434"],"scope":"focus_ayah","source_local_id":"87:2:2:form-i-before-form-ii","source_type":"word_analysis","support_ids":["sup_268eb17f2111df1bfc93","sup_74179a7592f2ac0e97a8"],"title":"Form I begins before derived adjustment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:2","qac_refs":["87:2:2:1"],"status":"accepted"}},{"anchor_refs":["87:2:2"],"branch_refs":[],"candidate_id":"cand_b070c990e6da3718cdfa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000434"],"scope":"focus_ayah","source_local_id":"87:2:2:measured-origination","source_type":"word_analysis","support_ids":["sup_08b2d9c9c208006ae7a1","sup_74179a7592f2ac0e97a8"],"title":"making and measuring survive inside creation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:2","qac_refs":["87:2:2:1"],"status":"accepted"}},{"anchor_refs":["87:2:2"],"branch_refs":[],"candidate_id":"cand_20c0006ccc5fa5a09942","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000434"],"scope":"focus_ayah","source_local_id":"87:2:2:objectless-creation-scope","source_type":"word_analysis","support_ids":["sup_74179a7592f2ac0e97a8","sup_8ee6b4cc821c3ca37676"],"title":"omitted object keeps creation unrestricted","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:2","qac_refs":["87:2:2:1"],"status":"accepted"}},{"anchor_refs":["87:2:2"],"branch_refs":[],"candidate_id":"cand_40081851694c2a4e4d3b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000434"],"scope":"focus_ayah","source_local_id":"87:2:2:sound-transition","source_type":"word_analysis","support_ids":["sup_1c6e390ca8bce8be2690","sup_74179a7592f2ac0e97a8"],"title":"opening articulation supports the move toward smoothing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:2","qac_refs":["87:2:2:1"],"status":"accepted"}},{"anchor_refs":["87:2:3"],"branch_refs":[],"candidate_id":"cand_26336fb95a448502a0b6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:2:3:bound-hinge-form","source_type":"word_analysis","support_ids":["sup_164364f5be3cd7c4beab","sup_2f3fbe0fd3c17f308e07"],"title":"proclitic shape makes dependency audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:3","qac_refs":["87:2:3:1"],"status":"accepted"}},{"anchor_refs":["87:2:3"],"branch_refs":[],"candidate_id":"cand_5344a414a0eea97147ab","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:2:3:close-consequential-sequel","source_type":"word_analysis","support_ids":["sup_2f3fbe0fd3c17f308e07","sup_ba18836b49ec42e8e6d2"],"title":"close sequence becomes consequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:3","qac_refs":["87:2:3:1"],"status":"accepted"}},{"anchor_refs":["87:2:3"],"branch_refs":[],"candidate_id":"cand_9b505c653f4c4184a3c1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:2:3:same-subject-coordination","source_type":"word_analysis","support_ids":["sup_2f3fbe0fd3c17f308e07","sup_684fe90ec2fe5ca9ace3"],"title":"the particle changes the action, not the agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:3","qac_refs":["87:2:3:1"],"status":"accepted"}},{"anchor_refs":["87:2:3"],"branch_refs":[],"candidate_id":"cand_c199530e350afaf911a9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:2:3:same-surah-fa-pattern","source_type":"word_analysis","support_ids":["sup_2f3fbe0fd3c17f308e07","sup_4659930f2fa1cec086a3"],"title":"first fa-link anticipates the next pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:3","qac_refs":["87:2:3:1"],"status":"accepted"}},{"anchor_refs":["87:2:4"],"branch_refs":[],"candidate_id":"cand_a0a54053b528ae102a63","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"87:2:4:active-form-ii-calibration","source_type":"word_analysis","support_ids":["sup_2852bff23c90ec2404f4","sup_92d211f34cc7e77dc23b"],"title":"Form II makes balance an effected act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:4","qac_refs":["87:2:3:2"],"status":"accepted"}},{"anchor_refs":["87:2:4"],"branch_refs":[],"candidate_id":"cand_2f6790b3f644f14e16ed","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"87:2:4:creation-proportion-closure","source_type":"word_analysis","support_ids":["sup_2852bff23c90ec2404f4","sup_de0ea3fa31d54fbab382"],"title":"closing verb completes the creation-proportion sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:4","qac_refs":["87:2:3:2"],"status":"accepted"}},{"anchor_refs":["87:2:4"],"branch_refs":[],"candidate_id":"cand_4b44f5a3ede55dd933d6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"87:2:4:fit-completion-root-pressure","source_type":"word_analysis","support_ids":["sup_2852bff23c90ec2404f4","sup_89f11ea7e6ebe718ee01"],"title":"equality and soundness become fitted completion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:4","qac_refs":["87:2:3:2"],"status":"accepted"}},{"anchor_refs":["87:2:4"],"branch_refs":[],"candidate_id":"cand_4539b63196f3e295d151","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"87:2:4:objectless-recoverable-patient","source_type":"word_analysis","support_ids":["sup_2852bff23c90ec2404f4","sup_af2b82120e410c792cb1"],"title":"omitted object lets the created domain carry the patient role","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:4","qac_refs":["87:2:3:2"],"status":"accepted"}},{"anchor_refs":["87:2:4"],"branch_refs":[],"candidate_id":"cand_7480498523a60f26f470","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"87:2:4:pronoun-parallel-contrast","source_type":"word_analysis","support_ids":["sup_2852bff23c90ec2404f4","sup_ce910d484bf15cd274b5"],"title":"pronoun-explicit parallel sharpens local breadth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:4","qac_refs":["87:2:3:2"],"status":"accepted"}},{"anchor_refs":["87:2:4"],"branch_refs":[],"candidate_id":"cand_12158104fa9189822229","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"87:2:4:sound-and-recitation-closure","source_type":"word_analysis","support_ids":["sup_2852bff23c90ec2404f4","sup_fd0c09273d023c094116"],"title":"gemination and long close support active calibration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:2:4","qac_refs":["87:2:3:2"],"status":"accepted"}},{"anchor_refs":["87:2:2"],"branch_refs":[],"candidate_id":"cand_09068ddea149d95ff4f2","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000434"],"scope":"focus_ayah","source_local_id":"87:2:2:1","source_type":"qac_morpheme","support_ids":["sup_e484cb001ba3b269ef15"],"title":"QAC root occurrence: خ ل ق","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:2:3"],"branch_refs":[],"candidate_id":"cand_90ac86c9fc4eeb59a072","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"87:2:3:2","source_type":"qac_morpheme","support_ids":["sup_d6c948009392a93b6a9d"],"title":"QAC root occurrence: س و ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:2","branch_refs":["root_000434/B001","root_000434/B002","root_000766/B002"],"candidate_id":"cand_ba6b65e230f7a10a2d73","commentary_obligation":"review","hft_ref":"hft_c7436a5a03874669890b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_measured_origination_then_rectification","source_type":"hft","support_ids":["sup_ddc77dc0f5d17d05d359"],"title":"b_measured_origination_then_rectification","trust":"legacy_unbound"},{"anchor_refs":["87:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:2","branch_refs":["root_000434/B003","root_000434/B004","root_000766/B002"],"candidate_id":"cand_ef36520a40b54bf324ad","commentary_obligation":"review","hft_ref":"hft_b0cd218ead7b14ebd90c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_outer_inner_coherence","source_type":"hft","support_ids":["sup_4b626362257e695f0b1a"],"title":"b_outer_inner_coherence","trust":"legacy_unbound"},{"anchor_refs":["87:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:2","branch_refs":["root_000434/B005","root_000766/B004"],"candidate_id":"cand_2e9347d6053a69cd5f71","commentary_obligation":"review","hft_ref":"hft_335ff738ef0cd48a9154","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_aptitude_then_orientation","source_type":"hft","support_ids":["sup_1083d930d3d7d799b1d1"],"title":"b_aptitude_then_orientation","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"ٱلَّذِى خَلَقَ فَسَوَّىٰ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"87:2:1:1","qac_word_ref":"87:2:1","root_ar":"","surface_ar":"ٱلَّذِى"},{"lemma_ar":"خَلَقَ","morph_features":"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:2:1","qac_word_ref":"87:2:2","root_ar":"خ ل ق","surface_ar":"خَلَقَ"},{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:2:3:1","qac_word_ref":"87:2:3","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","root_ar":"س و ي","surface_ar":"سَوَّىٰ"}],"word_analysis_qac_refs":[["87:2:1:1"],["87:2:2:1"],["87:2:3:1"],["87:2:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["87:2:1","87:2:2","87:2:3","87:2:4"]},"focus_surface_evidence":{"arabic_uthmani":"ٱلَّذِى خَلَقَ فَسَوَّىٰ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"87:2:1:1","qac_word_ref":"87:2:1","root_ar":"","surface_ar":"ٱلَّذِى"},{"lemma_ar":"خَلَقَ","morph_features":"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:2:1","qac_word_ref":"87:2:2","root_ar":"خ ل ق","surface_ar":"خَلَقَ"},{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:2:3:1","qac_word_ref":"87:2:3","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:2:3:2","qac_word_ref":"87:2:3","root_ar":"س و ي","surface_ar":"سَوَّىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["87:2:1:1"],["87:2:2:1"],["87:2:3:1"],["87:2:3:2"]],"word_analysis_refs":["87:2:1","87:2:2","87:2:3","87:2:4"],"word_rows":[{"analysis_record_ref":"87:2:1","analytic_gloss_range_en":"masculine singular definite relative pronoun continuing the prior divine description; it subordinates the following verbs rather than starting an independent report","analytic_root_gloss_range_en":null,"qac_refs":["87:2:1:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"ٱلَّذِى","transliteration":"alladhī"}},{"analysis_record_ref":"87:2:2","analytic_gloss_range_en":"completed active creating or originating with the object deliberately unspoken; the local pair keeps measure and formation pressure inside the act without activating unrelated root branches","analytic_root_gloss_range_en":"root range includes measuring and proportioning, originating and bringing into being, formed constitution, disposition, worthiness, allotted share, and several specialized branches; this ayah selects measured origination under an objectless perfect verb","qac_refs":["87:2:2:1"],"root":{"arabic":"خ ل ق","transliteration":"kh-l-q"},"surface":{"arabic":"خَلَقَ","transliteration":"khalaqa"}},{"analysis_record_ref":"87:2:3","analytic_gloss_range_en":"coordinating particle with close sequential and consequential force; it binds the second perfect verb to the first while preserving their distinction","analytic_root_gloss_range_en":null,"qac_refs":["87:2:3:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"87:2:4","analytic_gloss_range_en":"active Form II proportioning, making even, making fit, and completing after creation; the object is omitted so the created domain remains recoverable rather than individually named","analytic_root_gloss_range_en":"root range includes equality, equivalence, straightness, sound completion, settling or rising in other constructions, direction toward, maturity, middle fairness, otherness, and specialized idioms; this ayah selects transitive factitive proportioning and completion","qac_refs":["87:2:3:2"],"root":{"arabic":"س و ي","transliteration":"s-w-y"},"surface":{"arabic":"سَوَّىٰ","transliteration":"sawwā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["87:2"],"branch_refs":["root_000434/B001","root_000434/B002","root_000766/B002"],"candidate_id":"cand_ba6b65e230f7a10a2d73","evidence_scope":"focus_ayah","hft_ref":"hft_c7436a5a03874669890b","item_id":"b_measured_origination_then_rectification","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_measured_origination_then_rectification","support_id":"sup_ddc77dc0f5d17d05d359"},{"anchor_refs":["87:2"],"branch_refs":["root_000434/B003","root_000434/B004","root_000766/B002"],"candidate_id":"cand_ef36520a40b54bf324ad","evidence_scope":"focus_ayah","hft_ref":"hft_b0cd218ead7b14ebd90c","item_id":"b_outer_inner_coherence","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_outer_inner_coherence","support_id":"sup_4b626362257e695f0b1a"},{"anchor_refs":["87:2"],"branch_refs":["root_000434/B005","root_000766/B004"],"candidate_id":"cand_2e9347d6053a69cd5f71","evidence_scope":"focus_ayah","hft_ref":"hft_335ff738ef0cd48a9154","item_id":"b_aptitude_then_orientation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_aptitude_then_orientation","support_id":"sup_1083d930d3d7d799b1d1"}],"diagnostics":[],"lane_counts":{"global":8,"macro":15,"micro":3},"packet_summary":{"ayah_count":19,"focus_ref":"87:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ء ث ر","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":true,"target_occurrences":9,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]}],"window":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"87:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":18,"unstructured_record_count":0},"identity":{"ayah_ref":"87:2","lane":"micro","linguistic_source_ref":"87:2","surface_ref":"87:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"87:2","target_tokens":[["O",["87:2:1"]],["yarattı",["87:2:2"]],["ve",["87:2:3"]],["düzene",["87:2:3"]],["koydu",["87:2:3"]]],"text":"O yarattı ve düzene koydu."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s087-p01-001-019","label":"Whole surah","number":1,"refs":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:2:measured-origination","source_type":"word_analysis","support_id":"sup_08b2d9c9c208006ae7a1","text":"{\"blocking_evidence\":null,\"headline\":\"making and measuring survive inside creation\",\"reader_payoff\":\"The reader notices that creation is not pictured as raw production; the root pressure and sequel make it measured origination open to proportion.\",\"reason\":\"V4 supports measuring and originating branches for the root, but local grammar and the paired sequel select measured creation rather than unrelated branches such as false fabrication, perfume, or worn fabric.\",\"representative_source_ids\":[\"QS-5f587324\",\"QS-ab73d2da\",\"QY-2b8e6669\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:3:bound-hinge-form","source_type":"word_analysis","support_id":"sup_164364f5be3cd7c4beab","text":"{\"blocking_evidence\":null,\"headline\":\"proclitic shape makes dependency audible\",\"reader_payoff\":\"The reader notices that the short bound particle makes the transition compact in sound as well as syntax.\",\"reason\":\"The particle is prefixed orthographically and phonetically to the following verb, supporting the hinge effect without replacing the syntactic evidence.\",\"representative_source_ids\":[\"QF-93a8a1b5\",\"QP-d28d07ef\",\"QP-dea851b4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:2:sound-transition","source_type":"word_analysis","support_id":"sup_1c6e390ca8bce8be2690","text":"{\"blocking_evidence\":null,\"headline\":\"opening articulation supports the move toward smoothing\",\"reader_payoff\":\"The reader notices an audible transition from the textured first verb toward the smoother following act, while grammar remains the main evidence.\",\"reason\":\"The sound observation coheres with the local semantic movement, but it is treated as supporting texture rather than independent proof.\",\"representative_source_ids\":[\"QP-5b53fadc\",\"QP-c3d31228\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:2:form-i-before-form-ii","source_type":"word_analysis","support_id":"sup_268eb17f2111df1bfc93","text":"{\"blocking_evidence\":null,\"headline\":\"Form I begins before derived adjustment\",\"reader_payoff\":\"The reader notices how the morphology distributes the work: direct creation comes first, then explicit causative proportioning follows.\",\"reason\":\"The first verb is unaugmented Form I, while the second verb is Form II; the contrast is local and does not require importing every other root form.\",\"representative_source_ids\":[\"QF-60dae73d\",\"QF-9d53a003\",\"MF-2741b752\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:4","source_type":"word_analysis","support_id":"sup_2852bff23c90ec2404f4","text":"{\"gloss_range\":\"active Form II proportioning, making even, making fit, and completing after creation; the object is omitted so the created domain remains recoverable rather than individually named\",\"prose\":\"{{ar:سَوَّىٰ}} ({{tr:sawwā}}) is the ayah's landing word: an active Form II perfect that makes proportioning an effected act by the same subject who created. Its object is again unspoken, so the patient is recovered from the created domain rather than narrowed to a single named thing; the pronoun-explicit parallel in 82:7 sharpens that canonical breadth. The root field of {{ar:س و ي}} ({{tr:s-w-y}}) gives equality, straightness, and sound completion, but local grammar selects transitive making fit: the created form is arranged into fitting relation as a sound whole, not merely smoothed on the surface and not made into intransitive self-settlement. As the second verb, it resolves the fa-hinge, completes the creation-proportion formula attested in 82:7, and looks ahead to the next ordered pair in 87:3. Its doubled sound and long close add audible pressure to active calibration, while the main payoff remains ordered fitness at the end of the ayah.\",\"root_display\":\"{{ar:س و ي}} ({{tr:s-w-y}})\",\"root_gloss_range\":\"root range includes equality, equivalence, straightness, sound completion, settling or rising in other constructions, direction toward, maturity, middle fairness, otherness, and specialized idioms; this ayah selects transitive factitive proportioning and completion\",\"surface_display\":\"{{ar:سَوَّىٰ}} ({{tr:sawwā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:3","source_type":"word_analysis","support_id":"sup_2f3fbe0fd3c17f308e07","text":"{\"gloss_range\":\"coordinating particle with close sequential and consequential force; it binds the second perfect verb to the first while preserving their distinction\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) is the hinge between the two perfect verbs. It does more than add a second predicate: it makes the next act follow closely from creation, so sequence and consequence remain live together. The chosen connector keeps the acts linked but distinct, neither collapsing them into an asyndetic stack nor treating proportioning as a loose extra beside creation. The particle also keeps the same subject across the change of action, preserving one continuous agency. Because it is bound to the following verb in speech and writing, the sequel is heard as attached rather than isolated, and the same fa-linked shape prepares the reader for the matching pattern in 87:3.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:3:same-surah-fa-pattern","source_type":"word_analysis","support_id":"sup_4659930f2fa1cec086a3","text":"{\"blocking_evidence\":null,\"headline\":\"first fa-link anticipates the next pair\",\"reader_payoff\":\"The reader notices that this local hinge also starts a same-surah pattern of first act plus fa-linked sequel that continues in 87:3.\",\"reason\":\"The same-surah echo is concrete in 87:3, while the local particle still governs only the second verb of 87:2.\",\"representative_source_ids\":[\"QE-fc64072a\",\"QB-0745b8a8\",\"QY-c8964f36\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:2:creation-proportion-formula","source_type":"word_analysis","support_id":"sup_58cba8dd0c974932d7d8","text":"{\"blocking_evidence\":null,\"headline\":\"first half of a recognized creation-proportion sequence\",\"reader_payoff\":\"The reader notices the common creation verb becoming locally marked because it begins a concentrated creation-to-proportion sequence, with concrete parallels such as 75:38 and the next pair in 87:3.\",\"reason\":\"The contextual profile shows the root pair concentrated with the following verb, and the CRITICAL rows provide concrete formula references including 75:38 and 87:3.\",\"representative_source_ids\":[\"QI-75527ef9\",\"QI-cb30b693\",\"MI-fabc2e05\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:3:same-subject-coordination","source_type":"word_analysis","support_id":"sup_684fe90ec2fe5ca9ace3","text":"{\"blocking_evidence\":null,\"headline\":\"the particle changes the action, not the agent\",\"reader_payoff\":\"The reader notices one continuous divine agency carrying creation into ordering.\",\"reason\":\"Both verbs share third-person masculine singular agreement under the same relative antecedent.\",\"representative_source_ids\":[\"QG-c6b6c81d\",\"MT-b2da2d6c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:2","source_type":"word_analysis","support_id":"sup_74179a7592f2ac0e97a8","text":"{\"gloss_range\":\"completed active creating or originating with the object deliberately unspoken; the local pair keeps measure and formation pressure inside the act without activating unrelated root branches\",\"prose\":\"{{ar:خَلَقَ}} ({{tr:khalaqa}}) is an active perfect verb under the relative frame, so creation is presented as an accomplished ground for praise and the acting subject remains the prior divine referent. Its expected object is not named; that compression lets createdness stay broad rather than narrowing the clause to one patient, especially against pronoun-explicit parallels such as 82:7. The root pressure is not bare production: {{ar:خ ل ق}} ({{tr:kh-l-q}}) carries measure, fashioning, and determinate make, and the following sequel makes that measured origination visible as ordered fitness. The Form I verb begins with direct creation rather than reflexive self-formation or a static agent-title, while the paired sequence and formulaic parallels such as 75:38, 82:7, and 87:3 show a common creation verb becoming locally marked as the first half of a creation-to-proportion pattern. Even the rougher opening sound can help the listener feel the movement from origination into later smoothing, though the grammar and pairing carry the main force.\",\"root_display\":\"{{ar:خ ل ق}} ({{tr:kh-l-q}})\",\"root_gloss_range\":\"root range includes measuring and proportioning, originating and bringing into being, formed constitution, disposition, worthiness, allotted share, and several specialized branches; this ayah selects measured origination under an objectless perfect verb\",\"surface_display\":\"{{ar:خَلَقَ}} ({{tr:khalaqa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:4:fit-completion-root-pressure","source_type":"word_analysis","support_id":"sup_89f11ea7e6ebe718ee01","text":"{\"blocking_evidence\":null,\"headline\":\"equality and soundness become fitted completion\",\"reader_payoff\":\"The reader notices that proportioning means bringing created form into fitting relation and sound completion, not merely smoothing a surface.\",\"reason\":\"V4 supports equality and sound completion branches, while the post-creation active Form II frame narrows them to transitive proportioning and excludes unrelated branches as local meanings.\",\"representative_source_ids\":[\"QS-0684e13b\",\"QS-321523bd\",\"QS-a4e3c07d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:2:objectless-creation-scope","source_type":"word_analysis","support_id":"sup_8ee6b4cc821c3ca37676","text":"{\"blocking_evidence\":null,\"headline\":\"omitted object keeps creation unrestricted\",\"reader_payoff\":\"The reader notices that the verse refuses to name a single created patient, letting the act range over the created domain.\",\"reason\":\"The local frame marks the transitive verb with no expressed object, while variants or parallels with explicit pronouns serve as contrast rather than replacing the canonical compression.\",\"representative_source_ids\":[\"QG-cd1b6030\",\"QG-f105273a\",\"MG-43db0d03\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:4:active-form-ii-calibration","source_type":"word_analysis","support_id":"sup_92d211f34cc7e77dc23b","text":"{\"blocking_evidence\":null,\"headline\":\"Form II makes balance an effected act\",\"reader_payoff\":\"The reader notices that proportion is made by the same acting subject, not merely discovered as a state already present.\",\"reason\":\"The local word is an active Form II perfect with the same third-person masculine singular subject as the first verb.\",\"representative_source_ids\":[\"QG-011980d1\",\"QF-8c8ca389\",\"MF-88f250e0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:1:command-to-evidence-register","source_type":"word_analysis","support_id":"sup_9c02030b6584d274b297","text":"{\"blocking_evidence\":null,\"headline\":\"command register turns into narrated evidence\",\"reader_payoff\":\"The reader notices the discourse turn from direct address in 87:1 to reported divine action in 87:2.\",\"reason\":\"The relative pronoun introduces third-person perfect verbs under the prior command frame.\",\"representative_source_ids\":[\"QI-453a1c73\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:4:objectless-recoverable-patient","source_type":"word_analysis","support_id":"sup_af2b82120e410c792cb1","text":"{\"blocking_evidence\":null,\"headline\":\"omitted object lets the created domain carry the patient role\",\"reader_payoff\":\"The reader notices that the final verb does not name one proportioned object; it lets whatever was created supply the recoverable patient.\",\"reason\":\"The frame marks the verb as transitive in sense with no overt object, matching the first verb's compressed argument structure.\",\"representative_source_ids\":[\"QG-22dfec2f\",\"QG-c701a71c\",\"QT-37019364\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:3:close-consequential-sequel","source_type":"word_analysis","support_id":"sup_ba18836b49ec42e8e6d2","text":"{\"blocking_evidence\":null,\"headline\":\"close sequence becomes consequence\",\"reader_payoff\":\"The reader notices that proportioning is not merely another action after creation; it follows from creation as its close fulfillment.\",\"reason\":\"The local attachment marks the second verb as sequenced after the first, and the CRITICAL rows correctly preserve both sequential and consequential force.\",\"representative_source_ids\":[\"QG-d4e27b41\",\"QS-549915b4\",\"QS-8716bdef\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:1:cross-ayah-relative","source_type":"word_analysis","support_id":"sup_bf9f3dd0c1cfa4846726","text":"{\"blocking_evidence\":null,\"headline\":\"relative pronoun pulls the prior title forward\",\"reader_payoff\":\"The reader notices that 87:2 is syntactically dependent on 87:1, not a fresh sentence detached from the prior Lord-title.\",\"reason\":\"The attachment evidence marks the relative clause as continuing the prior divine description and warns against adding a new explanatory noun.\",\"representative_source_ids\":[\"QG-143296ef\",\"QG-4ceb7deb\",\"QB-8d8b1929\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:4:pronoun-parallel-contrast","source_type":"word_analysis","support_id":"sup_ce910d484bf15cd274b5","text":"{\"blocking_evidence\":null,\"headline\":\"pronoun-explicit parallel sharpens local breadth\",\"reader_payoff\":\"The reader notices that 82:7 individualizes the patient with a pronoun, while 87:2 leaves proportioning broader by omitting it.\",\"reason\":\"The parallel in 82:7 is concrete and useful as contrast, but it does not replace the canonical object omission in 87:2.\",\"representative_source_ids\":[\"QI-ae2a1e4f\",\"MI-89d18349\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:1:sila-evidentiary-scope","source_type":"word_analysis","support_id":"sup_d5a84c9edb1361d69d6e","text":"{\"blocking_evidence\":null,\"headline\":\"both verbs become one evidentiary relative clause\",\"reader_payoff\":\"The reader notices that the following two acts define the known referent together, rather than appearing as two loose predicates.\",\"reason\":\"The local syntax makes the first verb the predicate of the relative clause and coordinates the second verb inside the same clause.\",\"representative_source_ids\":[\"QG-4e904b7e\",\"QS-6275bfc0\",\"QT-e5cb1527\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:2:3:2","source_type":"qac_morpheme","support_id":"sup_d6c948009392a93b6a9d","text":"{\"lemma_ar\":\"سَوَّىٰ\",\"morph_features\":\"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"87:2:3:2\",\"qac_word_ref\":\"87:2:3\",\"root_ar\":\"س و ي\",\"surface_ar\":\"سَوَّىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:4:creation-proportion-closure","source_type":"word_analysis","support_id":"sup_de0ea3fa31d54fbab382","text":"{\"blocking_evidence\":null,\"headline\":\"closing verb completes the creation-proportion sequence\",\"reader_payoff\":\"The reader notices that the ayah does not stop at creation; it lands on ordered fitness and then anticipates the matching ordered pair in 87:3.\",\"reason\":\"The word is coordinated as the second verb after creation, and CRITICAL gives concrete parallels including 82:7 and the next pair in 87:3.\",\"representative_source_ids\":[\"QI-39830dcb\",\"QI-56389ff1\",\"QT-68a8f6a3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:2:active-completed-agency","source_type":"word_analysis","support_id":"sup_df0b049882aa41f98fd0","text":"{\"blocking_evidence\":null,\"headline\":\"active perfect grounds praise in accomplished agency\",\"reader_payoff\":\"The reader notices that creation is presented as a completed act of the same relative antecedent, not as a process or passive event.\",\"reason\":\"The word is a Form I active perfect with a third-person masculine singular subject controlled by the relative pronoun.\",\"representative_source_ids\":[\"QG-23b09c3c\",\"QG-96644a8e\",\"QG-c66d6756\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:2:2:1","source_type":"qac_morpheme","support_id":"sup_e484cb001ba3b269ef15","text":"{\"lemma_ar\":\"خَلَقَ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:xalaqa|ROOT:xlq|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"87:2:2:1\",\"qac_word_ref\":\"87:2:2\",\"root_ar\":\"خ ل ق\",\"surface_ar\":\"خَلَقَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:1","source_type":"word_analysis","support_id":"sup_ef2a86fc6759a042b047","text":"{\"gloss_range\":\"masculine singular definite relative pronoun continuing the prior divine description; it subordinates the following verbs rather than starting an independent report\",\"prose\":\"{{ar:ٱلَّذِى}} ({{tr:alladhī}}) makes the ayah lean back across the boundary: its antecedent is already supplied by the prior Lord-title, so the new line does not begin as a detached report. Because the referent is already identified, the relative does not introduce an indefinite \\\"one who\\\"; it specifies the known Lord through the acts that follow. The relative frame gathers both following perfect verbs into one descriptive clause, turning creation and proportioning into evidence attached to that referent. It also shifts the discourse from the direct command of 87:1 into third-person evidence for why that command has its object.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ٱلَّذِى}} ({{tr:alladhī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:2:4:sound-and-recitation-closure","source_type":"word_analysis","support_id":"sup_fd0c09273d023c094116","text":"{\"blocking_evidence\":null,\"headline\":\"gemination and long close support active calibration\",\"reader_payoff\":\"The reader notices that the doubled sound and lingering close reinforce the felt pressure of making even at the ayah's end.\",\"reason\":\"The prosodic rows cohere with the Form II and closure position, but they remain supporting texture rather than a separate semantic proof.\",\"representative_source_ids\":[\"QP-43cd1808\",\"QP-9d1019d0\",\"QY-d0b18edc\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى خَلَقَ فَسَوَّىٰ","ayah_ref":"87:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000434/B001","root_000434/B002","root_000766/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000434","role":"Measuring before cutting or acting supplies the designed specification of the creature.","root":"خ ل ق","source_ref":"87:2","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000434","role":"Originating and bringing into being supplies realization of the measured design.","root":"خ ل ق","source_ref":"87:2","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000766","role":"Straightness and intrinsic completeness supply the subsequent rectifying finish.","root":"س و ي","source_ref":"87:2","source_word_indices":["3"]}],"changed_reading":{"after":"He measured a form, originated it, then rectified and completed it into soundness.","before":"He created and proportioned."},"confidence":"strong","focus_anchor":"خَلَقَ at word 2 followed by fa and سَوَّىٰ at word 3.","mechanism":"The first root supplies both prior measurement and origination, while the second supplies straightening and completion. The fa moves from apportioned design through realized existence into sound form.","model_id":"b_measured_origination_then_rectification"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_measured_origination_then_rectification","source_type":"hft","support_id":"sup_ddc77dc0f5d17d05d359","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى خَلَقَ فَسَوَّىٰ","ayah_ref":"87:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000434/B003","root_000434/B004","root_000766/B002"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000434","role":"Complete, balanced, visibly formed features supply the exterior dimension.","root":"خ ل ق","source_ref":"87:2","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000434","role":"Inner disposition and character supply a second, non-visible dimension of created form.","root":"خ ل ق","source_ref":"87:2","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000766","role":"Sound form or character makes leveling the coherence of both exterior and interior.","root":"س و ي","source_ref":"87:2","source_word_indices":["3"]}],"changed_reading":{"after":"The creature's visible form and inward disposition were brought into a coherent soundness.","before":"The creature was given a balanced physical shape."},"confidence":"medium","focus_anchor":"The paired focus verbs permit خَلَقَ to name both visible formation and inward disposition, with سَوَّىٰ completing either domain.","mechanism":"Creation is not only an exterior outline. Visible form and inward character are co-formed, and the following leveling makes them coherent rather than merely geometrically symmetric.","model_id":"b_outer_inner_coherence"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_outer_inner_coherence","source_type":"hft","support_id":"sup_4b626362257e695f0b1a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى خَلَقَ فَسَوَّىٰ","ayah_ref":"87:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000434/B005","root_000766/B004"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000434","role":"Worthiness and aptitude supply a created capacity fitted to an end.","root":"خ ل ق","source_ref":"87:2","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000766","role":"Turning and intending toward a direction supplies orientation of that capacity.","root":"س و ي","source_ref":"87:2","source_word_indices":["3"]}],"changed_reading":{"after":"Creation confers aptitude, then directs that aptitude toward a fitting end.","before":"Creation is followed by a finishing adjustment."},"confidence":"exploratory","focus_anchor":"خَلَقَ can mark fitness for something, while a branch of سَوَّىٰ turns or intends toward a direction.","mechanism":"The sequence can be functional rather than cosmetic: first an entity is made apt for an end, then its capacity is aimed toward a direction in which it can operate.","model_id":"b_aptitude_then_orientation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_aptitude_then_orientation","source_type":"hft","support_id":"sup_1083d930d3d7d799b1d1","trust":"legacy_unbound"}]}
</lane_packet_json>
