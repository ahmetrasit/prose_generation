# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **87:6**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s087-regular-20260911/s087/87_6/micro.discovery.json` and modify nothing
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
  "ayah_ref": "87:6",
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
{"analysis_context":{"analysis_id":"s087-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"87:6","host_surah":87,"lane_context_refs":[],"ordered_context_refs":["87:0","87:1","87:2","87:3","87:4","87:5","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"This covers the root image of collecting, joining, and gathering: things gathered together, water or food gathered in a vessel, people gathered in a settlement, guests gathered around a dish, and the back as gathered bones.","branch_kind":null,"branch_ref":"root_001210/B001","candidate_links":[{"candidate_id":"cand_f5954b487310c3a162ba","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نُقْرِئُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:nuqori}u|ROOT:qrA|1P","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:1:2","qac_word_ref":"87:6:1","surface_ar":"نُقْرِئُ"}],"gloss":"collecting and gathering","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"جمع واجتماع","image_en":"collecting and gathering"}}],"root_ar":"ق ر ء","root_id":"root_001210","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"جمع واجتماع","image_en":"collecting and gathering","scope_ar":"يدخل فيه أصل الجمع والاجتماع، وضم الشيء بعضه إلى بعض، وجمع الماء والطعام والناس والضيف، واجتماع عظام الظهر، وما ألحقته المقاييس بقرية من جهة الجمع.","scope_en":"This covers the root image of collecting, joining, and gathering: things gathered together, water or food gathered in a vessel, people gathered in a settlement, guests gathered around a dish, and the back as gathered bones."},"support_links":["sup_b6518febf92a70fbe9e8"]},{"boundary":"This covers reading or reciting Qur'an, a book, poetry, or report; Qur'an as a name or verbal noun; reading to another; teaching another to recite; and mutual study.","branch_kind":null,"branch_ref":"root_001210/B002","candidate_links":[{"candidate_id":"cand_2b7db860171b31b46b4b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نُقْرِئُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:nuqori}u|ROOT:qrA|1P","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:1:2","qac_word_ref":"87:6:1","surface_ar":"نُقْرِئُ"}],"gloss":"reading, reciting, and teaching recitation","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"قراءة وتلاوة وإقراء","image_en":"reading, reciting, and teaching recitation"}}],"root_ar":"ق ر ء","root_id":"root_001210","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"قراءة وتلاوة وإقراء","image_en":"reading, reciting, and teaching recitation","scope_ar":"يدخل فيه قراءة القرآن والكتاب والشعر والحديث، والقرآن اسما ومصدرا، وقراءة الشيء على غيره، وإقراء غيره، والمقارأة والمدارسة والاستقراء.","scope_en":"This covers reading or reciting Qur'an, a book, poetry, or report; Qur'an as a name or verbal noun; reading to another; teaching another to recite; and mutual study."},"support_links":["sup_bd293e59b781f5cdb243"]},{"boundary":"This covers qari' as a devotee or ascetic, qurra' as devout readers, and taqarra'a as becoming devout, learned, or understanding.","branch_kind":null,"branch_ref":"root_001210/B006","candidate_links":[{"candidate_id":"cand_1d23a7a51c07dc805bb2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نُقْرِئُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:nuqori}u|ROOT:qrA|1P","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:1:2","qac_word_ref":"87:6:1","surface_ar":"نُقْرِئُ"}],"gloss":"devout or learned reader","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"قارئ ناسك متفقه","image_en":"devout or learned reader"}}],"root_ar":"ق ر ء","root_id":"root_001210","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"قارئ ناسك متفقه","image_en":"devout or learned reader","scope_ar":"يدخل فيه القارئ بمعنى العابد الناسك، والقراء المتنسك، والتقرأ بمعنى التنسك أو التفقه أو التفهم.","scope_en":"This covers qari' as a devotee or ascetic, qurra' as devout readers, and taqarra'a as becoming devout, learned, or understanding."},"support_links":["sup_5bc2650d97db231b4003"]},{"boundary":"This covers a common manner or pattern, a course or directed path, and poetry modeled on another poem's way or example.","branch_kind":null,"branch_ref":"root_001210/B011","candidate_links":[{"candidate_id":"cand_9f18df84224d99c52b7f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نُقْرِئُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:nuqori}u|ROOT:qrA|1P","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:1:2","qac_word_ref":"87:6:1","surface_ar":"نُقْرِئُ"}],"gloss":"manner, pattern, and directed course","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"طريقة ومثال وقصد","image_en":"manner, pattern, and directed course"}}],"root_ar":"ق ر ء","root_id":"root_001210","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"طريقة ومثال وقصد","image_en":"manner, pattern, and directed course","scope_ar":"يدخل فيه القرو أو القرء بمعنى الطريقة الواحدة، والقصد أو السلوك، وأن يكون الشعر على قرء شعر آخر أي على طريقته ومثاله.","scope_en":"This covers a common manner or pattern, a course or directed path, and poetry modeled on another poem's way or example."},"support_links":["sup_b6f48b85c5b6c28ae31c"]},{"boundary":"Bu dal bellek ve hatırda tutma alanındadır; bir işi fiilen terk etme, atılmış nesne ve zaman bakımından erteleme anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001501/B001","candidate_links":[{"candidate_id":"cand_2b7db860171b31b46b4b","lane":"micro"},{"candidate_id":"cand_f5954b487310c3a162ba","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَسِىَ","morph_features":"STEM|POS:V|IMPF|LEM:nasiYa|ROOT:nsy|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:3:1","qac_word_ref":"87:6:3","surface_ar":"تَنسَىٰٓ"}],"gloss":"hatırdan çıkma veya akılda tutmayı bırakma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Daha önce hatırda bulunan şey zihinde hazır olmaktan çıkar ve kişi onu anamaz."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Korunması için verilen bilgiyi akılda tutmama, gönül zayıflığına, dalgınlığa veya bilinçli bir tutuma bağlanabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Unutma sık yinelendiğinde kişinin yerleşik bir özelliği olarak anlatılabilir."}}],"root_ar":"ن س ي","root_id":"root_001501","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Önceden bilinen bir şeyin artık hatırlanmaması ile korunması istenen bilginin akılda tutulmaması çekirdeğini birlikte karşılar.","boundary_detail":"Bu dal bellek ve hatırda tutma alanındadır; bir işi fiilen terk etme, atılmış nesne ve zaman bakımından erteleme anlamlarını kapsamaz.","branch_image_ar":"غفلة الذكر وزواله","concept_gloss":"hatırdan çıkma veya akılda tutmayı bırakma","contextual_glosses":[{"applicability":"Önceden hatırda bulunan bir şeyin artık anılamadığı doğal bellek bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyin hatırdan çıkması anlamını doğal biçimde korur."},"facet_ids":["F001"],"text":"unutmak","usage_role":"general"},{"applicability":"Korunması veya hatırda tutulması istenen bir bilginin artık tutulmadığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Verilen bilgiyi akılda tutmama ayrımını açıkça korur."},"facet_ids":["F002"],"text":"akılda tutmayı bırakmak","usage_role":"contextual"},{"applicability":"Unutmanın tek bir olay değil, kişide sık yinelenen bir özellik olarak anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sık ve yerleşik unutma özelliğini doğal biçimde korur."},"facet_ids":["F003"],"text":"çok unutkan olmak","usage_role":"contextual"}],"definition":"Daha önce hatırda bulunan bir şeyin zihinden çıkması veya insana koruması için verilen bilginin artık akılda tutulmamasıdır. Bu durum gönül zayıflığından, dalgınlıktan ya da bilinçli bir tutumdan doğabilir ve kişide sık yinelenen bir özellik olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Daha önce hatırda bulunan şey zihinde hazır olmaktan çıkar ve kişi onu anamaz."},{"facet_id":"F002","role":"source_variant","statement":"Korunması için verilen bilgiyi akılda tutmama, gönül zayıflığına, dalgınlığa veya bilinçli bir tutuma bağlanabilir."},{"facet_id":"F003","role":"specialization","statement":"Unutma sık yinelendiğinde kişinin yerleşik bir özelliği olarak anlatılabilir."}],"identity_rationale":"Kaynak sözü, önceden hatırda bulunan bir şeyin unutulmasını temel alır; ancak emanet edilen bilgiyi gönül zayıflığı, dalgınlık veya bilinçli bir tutum yüzünden akılda tutmamayı da aynı alan içinde sayar. Bu yüzden dalgınlığa dayalı çerçeve kullanılabilir, fakat bilinçli olarak akılda tutmayı bırakma olasılığı dışarıda bırakılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"önceden bilinen bir şeyi unutmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"unutma; hatırda tutmanın karşıtı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"çok unutkan"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"çok unutkan adam"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"birine bir şeyi unutturmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"unutmuş gibi davranmak"}],"lexicalization_note":"Tanım temel unutma sürecini verir; çok unutkan kişi, unutturma ve unutmuş görünme gibi biçim ya da söz öbeğine bağlı kullanımlar bu çekirdeğin ayrı gerçekleşimleridir.","neighbor_coverage_note":"Verilen bütün komşular bellek nedeni, dikkat durumu, karşıtlık ve kökün öteki dalları bakımından değerlendirildi; sınırı en açık gösteren üç karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bellek durumunu ve hatırda tutmayı konu eder; komşu dal ise davranış düzeyinde bırakmayı ve yerine getirmemeyi anlatır.","focus_only":"Bilginin zihinde hazır olmaktan çıkması veya artık akılda tutulmaması bu dala özgüdür.","gloss":"unutma ile terk etme","neighbor_only":"Bir işi, sözü ya da yükümlülüğü fiilen ve bilerek bırakma öteki dala özgüdür.","neighbor_ref":"root_001501/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir şey insanın etkin yöneliminden çıkar ve korunmaz."},{"boundary_match":"partial","distinction":"Komşu anlam dikkat dağıtan belirli bir nedeni öne çıkarır; bu dalın bellek kaybı daha genel olup böyle bir neden gerektirmez.","focus_only":"Bu dal, neden belirtilmeden unutmayı ve bilinçli olarak akılda tutmamayı da kapsayabilir.","gloss":"unutmak ve dalıp unutmak","neighbor_only":"Komşu dalda unutma, özellikle uğraş, korku veya üzüntünün yol açtığı dalgınlığa bağlanır.","neighbor_ref":"root_000523/B001","relation_type":"near_synonym","shared_zone":"İkisinde de bir şey hatırda bulunmaz ve kişi onu anamaz."},{"boundary_match":"opposed","distinction":"Bu dal hatırlamanın yitmesini, komşu dal ise bilginin korunmasını ya da yeniden hatırlanmasını anlatır.","focus_only":"Bu dalda daha önce bilinen şey zihinde hazır olmaktan çıkar.","gloss":"unutma ve hatırlama","neighbor_only":"Komşu dalda şey korunur veya unutulduktan sonra yeniden zihinde hazır edilir.","neighbor_ref":"root_000516/B003","relation_type":"antonym","shared_zone":"İki dal da bir şeyin zihinde hazır bulunup bulunmaması eksenindedir."}],"source_phrase_ar":"نسي فلان شيئا كان يذكره وإنه لنسي أي كثير النسيان (ayn;tahdhib)؛ النسيان خلاف الذكر والحفظ ورجل نسيان كثير النسيان (sihah)؛ ترك الإنسان ضبط ما استودع إما لضعف قلبه وإما عن غفلة وإما عن قصد (mufradat)؛ نسيت الشيء إذا لم تذكره نسيانا (maqayis)","source_summary":"Kaynakların ortak çekirdeği, hatırlamanın ve akılda tutmanın karşıtı olan unutmadır. Derlenmiş açıklama, daha önce zihinde bulunan şeyin kaybolmasını, korunması istenen bilginin tutulmamasını ve sık unutma özelliğini birlikte gösterir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه نسيان الشيء بعد ذكره، وعزوب الشيء عن النفس، وترك ضبط ما استودع الإنسان، وكثرة النسيان، والتنسية بمعنى جعل غيره ينسى.","what_is_not_ar":"ليس الترك العملي المقصود وحده، ولا الشيء المطروح القليل الاعتداد به، ولا التأخير المهموز."},"support_links":["sup_b6518febf92a70fbe9e8","sup_bd293e59b781f5cdb243"]},{"boundary":"Bu dal davranış düzeyindeki bilinçli bırakmayı kapsar; kendiliğinden hatırlayamama, atılmış nesne ve erteleme anlamlarından ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001501/B002","candidate_links":[{"candidate_id":"cand_9f18df84224d99c52b7f","lane":"micro"},{"candidate_id":"cand_1d23a7a51c07dc805bb2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَسِىَ","morph_features":"STEM|POS:V|IMPF|LEM:nasiYa|ROOT:nsy|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:3:1","qac_word_ref":"87:6:3","surface_ar":"تَنسَىٰٓ"}],"gloss":"bilerek bırakma ve yerine getirmeme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey unutma sözüyle anlatılsa da asıl işlem onu bilerek bırakmak ve sürdürmemektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bırakılan şey bir söz, buyruk, yükümlülük veya yapılması gereken iş olabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanrı'ya bağlanan kullanım, insanların bırakmasına karşılık onları değersiz görerek yardımsız bırakmayı bildirir."}}],"root_ar":"ن س ي","root_id":"root_001501","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin, sözün, buyruğun veya yapılması gereken işin davranış düzeyinde terk edildiği anlamı karşılar.","boundary_detail":"Bu dal davranış düzeyindeki bilinçli bırakmayı kapsar; kendiliğinden hatırlayamama, atılmış nesne ve erteleme anlamlarından ayrıdır.","branch_image_ar":"ترك الشيء وإهماله","concept_gloss":"bilerek bırakma ve yerine getirmeme","contextual_glosses":[{"applicability":"Bir şeyin bilerek bırakıldığı ve artık sürdürülmediği genel davranış bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilerek bırakma işlemini kısa ve doğal biçimde korur."},"facet_ids":["F001"],"text":"terk etmek","usage_role":"general"},{"applicability":"Verilen söz, buyruk veya yapılması gereken iş bırakıldığında kullanılabilecek doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Söz veya yükümlülüğü bırakma sonucunu açıkça korur."},"facet_ids":["F002"],"text":"yerine getirmemek","usage_role":"contextual"},{"applicability":"Tanrı'nın, kendisini bırakan insanları yaptıklarına karşılık yardımsız bırakmasının anlatıldığı bağlama özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklılık ile yardımsız ve değersiz bırakma ayrımını korur."},"facet_ids":["F003"],"text":"karşılık olarak yüzüstü bırakmak","usage_role":"explanatory"}],"definition":"Bir şeyi, verilen sözü, buyruğu ya da yapılması gereken işi bilerek bırakmak ve yerine getirmemektir. Eylem Tanrı'ya bağlandığında, insanların O'nu bırakmasına karşılık onların yardımsız ve değersiz bırakılmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey unutma sözüyle anlatılsa da asıl işlem onu bilerek bırakmak ve sürdürmemektir."},{"facet_id":"F002","role":"specialization","statement":"Bırakılan şey bir söz, buyruk, yükümlülük veya yapılması gereken iş olabilir."},{"facet_id":"F003","role":"associated_use","statement":"Tanrı'ya bağlanan kullanım, insanların bırakmasına karşılık onları değersiz görerek yardımsız bırakmayı bildirir."}],"identity_rationale":"Kaynak sözü unutma biçiminin burada açıkça bırakma anlamında kullanıldığını, özellikle verilen sözün veya buyruğun terkini anlattığını belirtir. Tanrı'ya bağlanan kullanım da gerçek unutma değil, insanların bırakmasına karşılık onların bırakılması ve değersiz görülmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir şeyi bırakmak veya savsaklamak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"Tanrı'yı bıraktılar, O da karşılık olarak onları bıraktı"}],"lexicalization_note":"Tanım bırakma çekirdeğini korur; verilen söz, buyruk ve karşılıklı bırakma söz öbeği bu çekirdeğin bağlama bağlı gerçekleşimleridir.","neighbor_coverage_note":"Bütün adaylar genel bırakma, yükümlülük, niyet, yardımsız bırakma ve kök içi anlam ayrımları bakımından karşılaştırıldı; en yararlı üç sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bilinçli bırakmayı ve davranışsal sonucu, komşu dal ise bellek durumunu ve hatırlayamamayı merkeze alır.","focus_only":"Bu dalda bırakma davranışa dönüşür ve sözün ya da işin yerine getirilmemesiyle görünür.","gloss":"terk etme ile unutma","neighbor_only":"Komşu dalda bilgi zihinden çıkar veya kişi onu akılda tutamaz.","neighbor_ref":"root_001501/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da daha önce yönelinen bir şey korunmaz veya sürdürülmez."},{"boundary_match":"partial","distinction":"Komşu dal genel bırakma eylemidir; bu dal unutma sözüyle kurulan, özellikle söz ve yükümlülüklerin terkine yönelen kullanımdır.","focus_only":"Bu dal verilen söz ve buyruk gibi yükümlülükleri bırakmayı ve karşılıklı bırakma kullanımını içerir.","gloss":"bırakmak ve terk etmek","neighbor_only":"Komşu dal bir şeyi isteyerek veya zorunluluktan bırakmayı daha genel biçimde kapsar.","neighbor_ref":"root_000180/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde bir şeyi almamak, sürdürmemek veya ondan vazgeçmek vardır."},{"boundary_match":"partial","distinction":"Bu dal doğrudan yerine getirmemeyi anlatırken komşu dal bunu arkaya koyma görüntüsüne bağlı bir yüz çevirme olarak kurar.","focus_only":"Bu dalda bir işin veya sözün bırakılması doğrudan temel anlamdır.","gloss":"bırakma ve arkaya atma","neighbor_only":"Komşu dal bırakmayı, şeyi arkaya koyma ve küçümseyerek yüz çevirme görüntüsüyle anlatır.","neighbor_ref":"root_000970/B012","relation_type":"near_neighbor","shared_zone":"İkisinde de bir şey önem ve etkin yönelim alanının dışına çıkarılır."}],"source_phrase_ar":"النسيان الترك، نسوا الله فنسيهم (sihah)؛ النسيان على الترك نتركها فلا ننسخها، وبناسيها بتاركها (tahdhib)؛ إذا نسب ذلك إلى الله فهو تركه إياهم استهانة بهم ومجازاة لما تركوه (mufradat)؛ الثاني ترك شيء، فترك العهد (maqayis)","source_summary":"Kaynaklar bu dalda unutma sözünü davranışsal bir bırakma olarak açıklar. Verilen sözün ve buyruğun yerine getirilmemesi temel örneklerdir; Tanrı'ya bağlandığında ise insanların davranışına karşılık onların bırakılması kastedilir.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه النسيان بمعنى الترك، وترك العهد أو الأمر أو العمل، وما نسب إلى الله بمعنى تركهم مجازاة أو إهانة.","what_is_not_ar":"ليس غياب الذكر غير المقصود وحده، ولا التأخير المهموز، ولا النساء جمع المرأة."},"support_links":["sup_5bc2650d97db231b4003","sup_b6f48b85c5b6c28ae31c"]},{"boundary":"Bu dal unutma eylemini değil, unutulmuş veya atılmış sayıldığı için önemsenmeyen şeyi adlandırır.","branch_kind":"mixed_non_bare","branch_ref":"root_001501/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَسِىَ","morph_features":"STEM|POS:V|IMPF|LEM:nasiYa|ROOT:nsy|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:3:1","qac_word_ref":"87:6:3","surface_ar":"تَنسَىٰٓ"}],"gloss":"unutulup atılmış değersiz şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan şey unutulmuş, atılmış ya da geride kalmış ve bu nedenle önemsenmez durumdadır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atılmış aybaşı bezi, unutulup önemsenmeyen nesnenin özel bir örneği olarak verilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Göç edenlerin konak yerinde bıraktığı değersiz ve ufak eşyalar bu adla anılabilir."}}],"root_ar":"ن س ي","root_id":"root_001501","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Unutulmuş, geride bırakılmış veya atılmış olduğu için önemsenmeyen nesnelerin ortak çekirdeğini karşılar.","boundary_detail":"Bu dal unutma eylemini değil, unutulmuş veya atılmış sayıldığı için önemsenmeyen şeyi adlandırır.","branch_image_ar":"الشيء المنسي المطروح","concept_gloss":"unutulup atılmış değersiz şey","contextual_glosses":[{"applicability":"Nesnenin atılmış veya geride bırakılmış olması öne çıktığında doğal bir karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Atılma, unutulma ve önemsenmeme özelliklerini korur."},"facet_ids":["F001"],"text":"atılıp unutulmuş şey","usage_role":"general"},{"applicability":"Göç edenlerin konak yerinde bıraktığı küçük ve değersiz eşyaların anlatıldığı bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geride kalmış değersiz eşya örneğini eksiksiz korur."},"facet_ids":["F003"],"text":"geride kalan değersiz eşya","usage_role":"contextual"}],"definition":"Unutulmuş, atılmış veya geride bırakılmış olduğu için önemsenmeyen ve değeri az görülen şeydir. Atılmış aybaşı bezleri ile göç sırasında geride kalan değersiz ufak eşyalar bunun belirli örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan şey unutulmuş, atılmış ya da geride kalmış ve bu nedenle önemsenmez durumdadır."},{"facet_id":"F002","role":"example","statement":"Atılmış aybaşı bezi, unutulup önemsenmeyen nesnenin özel bir örneği olarak verilir."},{"facet_id":"F003","role":"example","statement":"Göç edenlerin konak yerinde bıraktığı değersiz ve ufak eşyalar bu adla anılabilir."}],"identity_rationale":"Kaynak sözü, unutulan, atılan veya önemsenmeyen şeyi doğrudan bir nesne adı olarak verir. Atılmış aybaşı bezleri ile göç edenlerin geride bıraktığı değersiz eşyalar bu nesne çekirdeğinin örnekleridir; dolayısıyla dalın unutulmuş ve değersiz nesne çerçevesi kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"unutulmuş veya atılmış, önemsenmeyen şey"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"unutulup atılmış, yok sayılan şey"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"göç edenlerin geride bıraktığı değersiz ufak tefek eşya"}],"lexicalization_note":"Tanım nesne çekirdeğini verir; aybaşı bezi, geride kalmış ufak eşya ve pekiştirmeli söz öbeği yalnızca bu çekirdeğin belirli gerçekleşimleridir.","neighbor_coverage_note":"Bütün adaylar atılmışlık, geride kalmışlık, düşük değer, artık olma ve unutma süreci bakımından değerlendirildi; nesne sınırını en iyi açıklayan üçü seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal unutulmuş nesnenin adı, komşu dal ise zihinsel sürecin adıdır; biri diğerinin yerine kullanılamaz.","focus_only":"Bu dal, unutmanın sonucunda geride kalmış ve önemsenmeyen bir nesneyi adlandırır.","gloss":"unutulan şey ve unutma","neighbor_only":"Komşu dal bir kişinin hatırlayamama durumunu veya akılda tutmayı bırakmasını anlatır.","neighbor_ref":"root_001501/B001","relation_type":"same_field","shared_zone":"İki dal unutulma ilişkisini paylaşır ve aynı kök içindeki yakın çağrışım alanındadır."},{"boundary_match":"partial","distinction":"Komşu anlam düşüklüğü ve azlığı doğrudan anlatır; bu dalın ayırıcı yanı nesnenin unutulup atılmış ya da geride kalmış olmasıdır.","focus_only":"Bu dalda düşük değer, nesnenin unutulmuş, atılmış veya geride bırakılmış olmasıyla bağlantılıdır.","gloss":"değersiz artık ve az şey","neighbor_only":"Komşu dal yerdeki döküntüyü, az ve değersiz şeyi, ayrıca bir hakkı azaltmayı da kapsar.","neighbor_ref":"root_001366/B005","relation_type":"near_synonym","shared_zone":"İkisinde de az değer verilen küçük veya önemsiz bir şey söz konusudur."},{"boundary_match":"partial","distinction":"Bu dal unutulma ve önemsenmeme ilişkisini, komşu dal ise bir ayırma işleminden sonra kalan bölümü öne çıkarır.","focus_only":"Bu dalda nesnenin önemsenmemesi unutulmuş veya atılmış olmasından doğar.","gloss":"atılmış şey ve artık","neighbor_only":"Komşu dalda nesne kaldırma veya ayırma işleminden sonra kalan artık ve tortudur.","neighbor_ref":"root_000330/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da ana bütünden ayrılmış, geride kalmış düşük değerli nesneleri anlatabilir."}],"source_phrase_ar":"النسي الشيء المنسي الذي لا يذكر ويقال هو خرقة الحائض (ayn)؛ النسي والنسي ما تلقيه المرأة من خرق اعتلالها والنسي أيضا ما نسي وما سقط من رذال أمتعتهم (sihah)؛ الشيء المطروح لا يؤبه له، انظروا أنساءكم أي الشيء اليسير (tahdhib)؛ النسي ما يقل الاعتداد به وما من شأنه أن ينسى (mufradat)؛ النسي ما سقط من منازل المرتحلين من رذال أمتعتهم (maqayis)","source_summary":"Kaynakların ortak anlatımı, unutulan veya atıldığı için önemsenmeyen nesneyi temel alır. Atılmış aybaşı bezi ve göç yerinde bırakılan değersiz eşya, aynı düşük değer ve geride kalmışlık çekirdeğini somutlaştırır.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه النَّسْي والنِّسْي لما ينسى أو يطرح أو لا يؤبه له، ورذال أمتعة المرتحلين، وخرق الحيض الملقاة، وكل حقير جار مجرى المنسي.","what_is_not_ar":"ليس فعل النسيان في النفس، ولا ترك العهد والعمل، ولا النَّسَا العرق."},"support_links":[]},{"boundary":"Bu dal belirli bir anatomik damar ve onun ağrısıyla sınırlıdır; genel unutma, bırakma veya başka beden ağrıları değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001501/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَسِىَ","morph_features":"STEM|POS:V|IMPF|LEM:nasiYa|ROOT:nsy|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:3:1","qac_word_ref":"87:6:3","surface_ar":"تَنسَىٰٓ"}],"gloss":"kalçadan bacağa uzanan damar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ad, kalçadan ya da uylukların ayrıldığı bölgeden bacağa uzanan belirli bir damarı gösterir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu damarın ağrıması, kişide hastalanması veya damara vurulması aynı söz çevresinde anlatılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Damarın iki tanesi ve çoğulu için ayrı çekimli biçimler kullanılır."}}],"root_ar":"ن س ي","root_id":"root_001501","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalça veya uyluk ayrımından bacağa uzanan ve ağrısıyla da anılan belirli anatomik yapıyı karşılar.","boundary_detail":"Bu dal belirli bir anatomik damar ve onun ağrısıyla sınırlıdır; genel unutma, bırakma veya başka beden ağrıları değildir.","branch_image_ar":"النَّسَا عرق ووجعه","concept_gloss":"kalçadan bacağa uzanan damar","contextual_glosses":[{"applicability":"Damarın kendisinin anatomik bir ad olarak geçtiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Damarın yeri ile uzanışını açık ve doğal biçimde korur."},"facet_ids":["F001"],"text":"kalça ile bacak arasındaki özel damar","usage_role":"general"},{"applicability":"Kişinin söz konusu kalça ve bacak damarında ağrı çektiğinin anlatıldığı eylem bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli damarda ağrı çekme anlamını korur."},"facet_ids":["F002"],"text":"bu damarı ağrımak","usage_role":"contextual"}],"definition":"Kalçadan veya iki uyluğun ayrıldığı bölgeden bacağa doğru uzanan belirli bir damardır. Aynı ad çevresindeki kullanımlar bu damarın ağrımasını, kişide hastalanmasını veya damara vurulmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ad, kalçadan ya da uylukların ayrıldığı bölgeden bacağa uzanan belirli bir damarı gösterir."},{"facet_id":"F002","role":"associated_use","statement":"Bu damarın ağrıması, kişide hastalanması veya damara vurulması aynı söz çevresinde anlatılır."},{"facet_id":"F003","role":"specialization","statement":"Damarın iki tanesi ve çoğulu için ayrı çekimli biçimler kullanılır."}],"identity_rationale":"Kaynak sözü kalça veya iki uyluğun ayrıldığı bölgeden uzanan belirli bir damarı adlandırır; ikilini, çoğulunu, bu damarı ağrıyan kişiyi ve damara vurmayı da verir. Dalın anatomik yapı ile ona bağlı ağrı ve etkilenme çerçevesi bu kanıtı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kalçadan veya uyluk ayrımından bacağa uzanan damar"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bu damarın iki tanesi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bu damarın çoğulu"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kalçadan bacağa uzanan damarı ağrımak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birinin bu damarına vurmak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bu damarı ağrıyan"}],"lexicalization_note":"Tanım anatomik yapıyı temel alır; ikil ve çoğul biçimler ile damarı ağrıma veya damara vurma kullanımları bu yapıya bağlı ayrı türetimlerdir.","neighbor_coverage_note":"Bütün komşular anatomik yer, yapı türü, ağrı ve hastalık bakımından incelendi; yalnızca aynı beden bölgesinde en kolay karışabilecek üç yapı yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Yakın beden bölgesinde bulunmaları dışında aynı yapı oldukları gösterilmez; bu dal uzanışı belirli damar, komşu dal ise başka bir doku veya damardır.","focus_only":"Bu dal kalçadan veya uyluk ayrımından bacağa uzanan belirli damarı adlandırır.","gloss":"bacak damarı ve kalça dokusu","neighbor_only":"Komşu dal kalça yuvası üzerindeki bir et parçasını veya uyluktaki başka bir damarı adlandırır.","neighbor_ref":"root_001193/B002","relation_type":"same_field","shared_zone":"İki dal kalça ve uyluk çevresindeki anatomik yapıları konu eder."},{"boundary_match":"field_only","distinction":"Bu dal uzanan belirli damara bağlıdır; komşu dal kalça başları veya başka bir sinirsel yapı ile kopma ve çıkma durumunu anlatır.","focus_only":"Bu dal kalçadan bacağa uzanan damarı ve bu damarın ağrısını kapsar.","gloss":"bacak damarı ve kalça başı","neighbor_only":"Komşu dal kalça başları veya kalça siniri diye açıklanan başka bir yapıyı ve onun kopması ya da çıkmasını kapsar.","neighbor_ref":"root_000311/B007","relation_type":"same_field","shared_zone":"İki dal kalça çevresindeki anatomik yapı ve yaralanma alanını paylaşır."},{"boundary_match":"field_only","distinction":"Bu dalın sınırı kalça ile bacak arasındaki belirli yapıdır; komşu dal yapının kimliğinden çok atma ve ağrı olayını öne çıkarır.","focus_only":"Bu dal ağrıdan önce belirli bir anatomik damarı adlandırır.","gloss":"belirli damar ve damar atması","neighbor_only":"Komşu dal herhangi bir damarın atmasını veya çıbandaki ağrıyı anlatır.","neighbor_ref":"root_000028/B005","relation_type":"same_field","shared_zone":"Her iki dal damar ve bedensel ağrı alanında kullanılabilir."}],"source_phrase_ar":"النسا عرق يأخذ من منشق ما بين الفخذين وهما نسيان وجمعه أنساء (ayn)؛ النسا عرق يخرج من الورك والجمع أنساء ويقال نسي الرجل إذا اشتكى نساه (sihah)؛ الذي يشتكي نساه نس ورجل أنسى وامرأة نسيا إذا اشتكيا عرق النسا (tahdhib)؛ النسا عرق وتثنيته نسيان وجمعه أنساء (mufradat)؛ ومما شذ عن الأصلين النسا عرق والجمع أنساء والاثنان نسيان (maqayis)","source_summary":"Kaynaklar kalça ve uyluk bölgesinden bacağa uzanan belirli damarı ortak biçimde tanımlar. Toplu kanıt, damarın ikil ve çoğul biçimlerini, damarı ağrıyan kişiyi ve o damara vurma eylemini de aynı anatomik ad çevresinde verir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه النَّسَا اسما للعرق الممتد من الورك أو منشق الفخذ، وتثنيته نسيان وجمعه أنساء، والاشتكاء منه أو إصابته.","what_is_not_ar":"ليس النسيان ولا الترك، ولا النساء جمع المرأة، ولا المنسأة العصا."},"support_links":[]},{"boundary":"Bu dal zaman bakımından erteleme ve süre uzatmadır; hatırlayamama, davranışsal terk ve sopayla itme anlamları bu sınırın dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001501/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَسِىَ","morph_features":"STEM|POS:V|IMPF|LEM:nasiYa|ROOT:nsy|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:3:1","qac_word_ref":"87:6:3","surface_ar":"تَنسَىٰٓ"}],"gloss":"sonraya bırakma ve süreyi uzatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir olay veya işlem beklenen zamanından sonraya bırakılır ya da ona ayrılan süre uzatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ödeme, satış ve dokunulmaz ayın yerini kaydırma, genel ertelemenin kurallı uygulamalarıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aybaşının gecikmesi, susuz kalma süresine gün eklenmesi ve tüyün geç çıkması aynı zaman ilişkisine uzanır."}}],"root_ar":"ن س ي","root_id":"root_001501","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin zamanını ileri alma, gerçekleşmesini geciktirme veya mevcut süreye ekleme işlemlerinin ortak çekirdeğini karşılar.","boundary_detail":"Bu dal zaman bakımından erteleme ve süre uzatmadır; hatırlayamama, davranışsal terk ve sopayla itme anlamları bu sınırın dışındadır.","branch_image_ar":"التأخير والإمهال بالهمز","concept_gloss":"sonraya bırakma ve süreyi uzatma","contextual_glosses":[{"applicability":"Bir şeyin, ödemenin veya belirlenmiş zamanın daha sonraya bırakıldığı genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyi daha sonraki zamana bırakma işlemini korur."},"facet_ids":["F001"],"text":"ertelemek","usage_role":"general"},{"applicability":"Aybaşı gibi beklenen bir olayın olağan zamanında gerçekleşmediği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Beklenen zamanın sonrasına kalma anlamını korur."},"facet_ids":["F003"],"text":"gecikmek","usage_role":"contextual"},{"applicability":"Satış karşılığının hemen değil, daha sonraki bir zamanda ödeneceği işlem bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Satışta ödeme zamanını sonraya bırakma ayrımını korur."},"facet_ids":["F002"],"text":"ödemesini sonraya bırakmak","usage_role":"contextual"},{"applicability":"Hayvanların susuz bırakıldığı süreye bir veya iki gün eklendiği özel bağlamı açıklar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mevcut süreyi belirli sayıda gün uzatma işlemini korur."},"facet_ids":["F003"],"text":"süreye gün eklemek","usage_role":"explanatory"}],"definition":"Bir şeyi beklenen zamanından sonraya bırakmak, gerçekleşmesini geciktirmek veya ayrılan süreyi uzatmaktır. Bu çekirdek ödeme, aybaşı, ayların dokunulmazlık düzeni, hayvanların susuz kalma süresi ve döküldükten sonra geç çıkan tüy için özelleşebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir olay veya işlem beklenen zamanından sonraya bırakılır ya da ona ayrılan süre uzatılır."},{"facet_id":"F002","role":"specialization","statement":"Ödeme, satış ve dokunulmaz ayın yerini kaydırma, genel ertelemenin kurallı uygulamalarıdır."},{"facet_id":"F003","role":"extension","statement":"Aybaşının gecikmesi, susuz kalma süresine gün eklenmesi ve tüyün geç çıkması aynı zaman ilişkisine uzanır."}],"identity_rationale":"Kaynak sözü, ses yapısı değişen bu dalın temelini bir şeyi ertelemek ve zamanını uzatmak olarak açıkça kurar. Aybaşının gecikmesi, ödemesi sonraya bırakılan satış, dokunulmaz ayın yerini kaydırma, süreye gün ekleme ve geç çıkan tüy bu zaman çekirdeğine bağlı uygulamalardır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bir şeyi ertelemek veya uzak bir zamana bırakmak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kadının aybaşı gecikmek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"ödemesi sonraya bırakılan satış"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"dokunulmaz ayın yerini sonraya kaydırma"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"develerin susuz kalacağı süreye bir iki gün eklemek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"dökülmeden sonra geç çıkan deve tüyü"}],"lexicalization_note":"Tanım genel erteleme çekirdeğini verir; aybaşı, satış, ay düzeni, hayvanların susuz kalma süresi ve tüy büyümesi kullanımları kendi yapılarına bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar genel erteleme, süre verme, borç, ay düzeni, gebelik ve hayvanlara ilişkin zaman uzatmaları bakımından değerlendirildi; bir eş anlamlı ve iki açıklayıcı daralma seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek işlem ve zaman sınırı aynıdır; farklı örneklerin anılması iki dal arasında anlam ayrılığı oluşturmaz.","focus_only":null,"gloss":"ertelemek ve süre vermek","neighbor_only":null,"neighbor_ref":"root_001493/B001","relation_type":"synonym","shared_zone":"İki dal da bir şeyi beklenen zamanından sonraya bırakmayı ve süresini uzatmayı anlatır."},{"boundary_match":"partial","distinction":"Komşu anlam bir kişiye tanınan zamanı öne çıkarır; bu dal kişi gerektirmeyen gecikmeleri ve nesneye bağlı özel kullanımları da kapsar.","focus_only":"Bu dal olay gecikmesi, satış, ay düzeni, susuzluk süresi ve geç çıkan tüy gibi geniş uygulamalara uzanır.","gloss":"ertelemek ve zaman tanımak","neighbor_only":"Komşu dal özellikle birine zaman tanıma ve onun süresini uzatma eylemine odaklanır.","neighbor_ref":"root_001447/B002","relation_type":"near_synonym","shared_zone":"İki dalda da gerçekleşme zamanı ileri alınır veya bir süre uzatılır."},{"boundary_match":"partial","distinction":"Komşu anlam borç bağlamıyla sınırlı bir ertelemedir; bu dalın zaman çekirdeği çok daha geniş alanlarda gerçekleşir.","focus_only":"Bu dal borç dışında doğal olayları, ay düzenini ve hayvanlara ilişkin süre uzatmalarını da kapsar.","gloss":"erteleme ve borcu erteleme","neighbor_only":"Komşu dal yalnızca borç parasının ödenmesi için borçluya zaman tanımayı anlatır.","neighbor_ref":"root_001085/B006","relation_type":"near_synonym","shared_zone":"Her iki dalda da ödeme veya yükümlülük için belirlenen zaman ileri alınabilir."}],"source_phrase_ar":"معنى أنسيت أخرت (ayn)؛ ولا منسيها أي ولا مؤخرها من أنسأت الدين أي أخرته (tahdhib)؛ إذا همز تغير المعنى إلى تأخير الشيء، ونسئت المرأة تأخر حيضها، والنسيئة بيعك الشيء نساء، ونسأ الله في أجلك، والنسيء في كتاب الله التأخير، ونسأت الإبل في ظمئها، والنسء ما نبت من وبر الناقة بعد تساقط وبرها (maqayis)","source_summary":"Toplu kaynak kanıtı erteleme ve süreyi uzatma çekirdeğini verir. Bu çekirdek borcun veya satış karşılığının sonraya bırakılmasında, aybaşının gecikmesinde, ay düzeninin kaydırılmasında, hayvanların susuzluk süresine gün eklenmesinde ve geç çıkan tüyün adlandırılmasında gerçekleşir.","sources":["AY","TA","MQ"],"what_is_ar":"يدخل فيه معنى أنسأ ونسأ إذا أخر، وتأخر الحيض، وبيع النسيئة، وإطالة الأجل، وتأخر القوم وتباعدهم، وتأخير حرمة الشهر، وزيادة ظمء الإبل، وما جعلته المصادر من نبت الوبر بعد سقوطه لتأخره.","what_is_not_ar":"ليس النسيان بلا همز، ولا الترك بمعنى الإهمال، ولا النَّسَا العرق إلا بتعليل بعيد عند بعضهم."},"support_links":[]},{"boundary":"Bu dal herhangi bir sopa veya genel sürme değildir; itme ve uzaklaştırma işlevli sopa ile onunla yapılan eyleme bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001501/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَسِىَ","morph_features":"STEM|POS:V|IMPF|LEM:nasiYa|ROOT:nsy|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:3:1","qac_word_ref":"87:6:3","surface_ar":"تَنسَىٰٓ"}],"gloss":"sopayla vurup itme veya sürme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Araç, bir şeyi itip uzaklaştırmaya yarayan belirli işlevli bir sopadır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem, özellikle deveyi bu sopayla vurarak itmek, uzaklaştırmak veya sürmektir."}}],"root_ar":"ن س ي","root_id":"root_001501","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İtme işlevli sopayı araç olarak kullanan vurma, uzaklaştırma ve hayvan sürme işlemlerinin ortak çekirdeğini karşılar.","boundary_detail":"Bu dal herhangi bir sopa veya genel sürme değildir; itme ve uzaklaştırma işlevli sopa ile onunla yapılan eyleme bağlıdır.","branch_image_ar":"المنسأة عصا الدفع","concept_gloss":"sopayla vurup itme veya sürme","contextual_glosses":[{"applicability":"Sopanın kendisi, bir şeyi uzaklaştırma veya hayvanı sürme aracı olarak adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aracın sopa oluşunu ve itme ile sürme işlevini korur."},"facet_ids":["F001"],"text":"itme ve sürme sopası","usage_role":"contextual"},{"applicability":"Özellikle devenin belirli sopayla vurularak itilmesi veya sürülmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sopayla vurma ve hayvanı sürme işlemlerini korur."},"facet_ids":["F002"],"text":"sopayla vurup sürmek","usage_role":"contextual"}],"definition":"Bir şeyi itmek veya uzaklaştırmak için kullanılan sopa ile özellikle bir deveyi bu sopayla vurarak itme ya da sürme işlemidir. Araç adı ve eylem aynı işlev çevresinde birbirine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Araç, bir şeyi itip uzaklaştırmaya yarayan belirli işlevli bir sopadır."},{"facet_id":"F002","role":"associated_use","statement":"Eylem, özellikle deveyi bu sopayla vurarak itmek, uzaklaştırmak veya sürmektir."}],"identity_rationale":"Kaynak sözü hem bir şeyi itip uzaklaştırmaya yarayan sopayı hem de özellikle deveyi bu sopayla vurarak sürme eylemini açıkça verir. Dalın araç ile o araçla yapılan itme ve sürme işlemini birlikte tutması kaynak kanıtına uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bir şeyi itip uzaklaştırmaya yarayan sopa"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"deveyi itme sopasıyla vurup sürmek"}],"lexicalization_note":"Tanım araç ile eylemi ayırır; sopanın adı biçime, deveyi bu sopayla vurup sürmek ise söz öbeğine bağlıdır ve genel sürme anlamına yayılmaz.","neighbor_coverage_note":"Bütün adaylar sopa türü, vurma, itme, sürme ve hayvana yönelik kullanım bakımından değerlendirildi; tam örtüşen aday ile iki temel sınır karşılaştırması seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Araç, işlem ve kullanım sınırı aynıdır; ifadelerdeki ayrıntılar yeni bir anlam ayrımı doğurmaz.","focus_only":null,"gloss":"sopayla itip sürme","neighbor_only":null,"neighbor_ref":"root_001493/B002","relation_type":"synonym","shared_zone":"İki dal da itme sopasını ve hayvanı bu sopayla vurarak itip sürme eylemini kapsar."},{"boundary_match":"partial","distinction":"Komşu anlam genel sürme ve kovmadır; bu dalın ayırıcı koşulu belirli sopanın araç olması ve vurma yoluyla itmedir.","focus_only":"Bu dal belirli bir itme sopasını ve o sopayla vurma işlemini gerektirir.","gloss":"sopayla sürme ve genel sürme","neighbor_only":"Komşu dal araç gerektirmeden hayvan, sürü, bulut veya başka şeyleri sürme ve kovmayı genişçe kapsar.","neighbor_ref":"root_000762/B001","relation_type":"near_synonym","shared_zone":"İki dalda da bir canlı veya şey hareket ettirilir, sürülür ya da uzaklaştırılır."},{"boundary_match":"partial","distinction":"Bu dal araç ve uzaklaştırma işleviyle sınırlıdır; komşu dal vurma biçimlerini ve sert sürmeyi daha geniş bir olay alanında toplar.","focus_only":"Bu dal belirli sopayla vurmayı itme ve hayvanı sürme amacına bağlar.","gloss":"sopayla itme ve sert vurma","neighbor_only":"Komşu dal elle vurmayı, hayvanın yere vurmasını ve sert sürmeyi araçtan bağımsız kapsar.","neighbor_ref":"root_000388/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda vurma ile hayvanı hareket ettirme veya sürme bir arada bulunabilir."}],"source_phrase_ar":"ونسأتها ضربتها بالمنسأة العصا لأن العصا كأنه يبعد بها الشيء ويدفع (maqayis)؛ المنساة العصا وأصله الهمز (sihah)","source_summary":"Kaynakların ortak anlatımı, itme ve uzaklaştırma işlevli sopayı verir ve sopa adını bu işleve bağlar. Aynı kanıt, deveyi bu araçla vurup sürme eylemini de araçla birlikte açıklar.","sources":["SI","MQ"],"what_is_ar":"يدخل فيه المنسأة اسما للعصا، وفعل نسأ الناقة بمعنى ضربها بالمنسأة ودفعها أو إبعادها بها.","what_is_not_ar":"ليس كل عصا، ولا مجرد التأخير الزمني، ولا النسيان."},"support_links":[]},{"boundary":"Dal yalnızca üzerine su dökülmüş süt adıdır; genel karışım, her türlü süt içeceği veya unutma süreci değildir.","branch_kind":"non_bare","branch_ref":"root_001501/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَسِىَ","morph_features":"STEM|POS:V|IMPF|LEM:nasiYa|ROOT:nsy|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:3:1","qac_word_ref":"87:6:3","surface_ar":"تَنسَىٰٓ"}],"gloss":"üzerine su dökülmüş süt","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan içecek, sütün üzerine su dökülmesiyle oluşan süt ve su karışımıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir aktarım, içeceği zihne unutturan bir şey olarak ayrıca niteler."}}],"root_ar":"ن س ي","root_id":"root_001501","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sütün üzerine su eklenerek oluşturulan belirli içeceğin adını, etki nitelemesini tanıma katmadan karşılar.","boundary_detail":"Dal yalnızca üzerine su dökülmüş süt adıdır; genel karışım, her türlü süt içeceği veya unutma süreci değildir.","branch_image_ar":"اللَّبن المصبوب عليه الماء","concept_gloss":"üzerine su dökülmüş süt","contextual_glosses":[{"applicability":"İçeceğin süt ile su karışımı olarak doğal akış içinde çevrildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sütün suyla karıştırılmış olması anlamını doğal biçimde korur."},"facet_ids":["F001"],"text":"su katılmış süt","usage_role":"general"},{"applicability":"Kaynak aktarımındaki etki nitelemesinin de okuyucuya açıkça gösterilmesi gereken bağlama özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Süt ve su karışımını ve aktarılan unutma nitelemesini korur."},"facet_ids":["F001","F002"],"text":"zihni unutturduğu söylenen sulu süt","usage_role":"explanatory"}],"definition":"Sütün üzerine su dökülerek elde edilen içeceğin adıdır. Kaynak aktarımındaki ek bir niteleme, bu içeceği zihne unutturan şey olarak açıklar; bu özellik karışımın temel tanımından ayrı tutulur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan içecek, sütün üzerine su dökülmesiyle oluşan süt ve su karışımıdır."},{"facet_id":"F002","role":"source_variant","statement":"Bir aktarım, içeceği zihne unutturan bir şey olarak ayrıca niteler."}],"identity_rationale":"Kaynak sözünün iki parçası da sütün üzerine su dökülerek elde edilen içeceği adlandırır. Bir parça ayrıca onu zihne unutturan şey diye niteler; bu niteleme karışımın kurucu işlemi değildir ve çekirdeğe eşitlenmeden kaynak çeşitlemesi olarak korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"üzerine su dökülmüş süt"}],"lexicalization_note":"Tanım yalnızca kanıtlanan içecek adına bağlıdır; süt ile suyu karıştırmanın genel fiiline veya unutmanın bağımsız anlamına genişletilemez.","neighbor_coverage_note":"Bütün adaylar karışım maddeleri, su oranı, kıvam, karıştırma işlemi ve içecek etkisi bakımından değerlendirildi; tam örtüşen aday ile iki yakın sınır seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Karışımın maddeleri ve temel sınırı aynıdır; bu daldaki ek etki nitelemesi çekirdeğe bağlı olmayan bir kaynak çeşitlemesidir.","focus_only":null,"gloss":"su katılmış süt","neighbor_only":null,"neighbor_ref":"root_000821/B006","relation_type":"synonym","shared_zone":"İki dal da su eklenerek inceltilmiş süt içeceğini adlandırır."},{"boundary_match":"partial","distinction":"Komşu anlam yüksek su oranı ve belirgin görünüş sonucuyla daha dardır; bu dal için su eklenmiş olması yeterlidir.","focus_only":"Bu dal sütün üzerine su dökülmesini bildirir, fakat suyun miktarı veya ortaya çıkan renk için koşul koymaz.","gloss":"sulu süt ve çok sulanmış süt","neighbor_only":"Komşu dal suyun çok olmasını ve sütün suyun rengine yaklaşacak ölçüde incelmesini gerektirir.","neighbor_ref":"root_000418/B008","relation_type":"near_synonym","shared_zone":"Her iki dal su katılmasıyla incelmiş bir süt içeceğini anlatır."},{"boundary_match":"partial","distinction":"Bu dalın karışımı süt ile su arasında ve inceltici yöndedir; komşu dalın maddeleri ve koyu kıvamı farklıdır.","focus_only":"Bu dal özellikle sütün üzerine su dökülmesiyle oluşan içecektir.","gloss":"sulu süt ve koyu karışım","neighbor_only":"Komşu dal koyu balı, peteği veya süt parçalarının birbirine karıştığı koyu karışımı da kapsar.","neighbor_ref":"root_000906/B015","relation_type":"near_neighbor","shared_zone":"İki dal süt içeren karışımları adlandırabilir."}],"source_phrase_ar":"النسيء الحليب يصب عليه الماء وهو النسء أيضا (maqayis)؛ النسي بغير همز وهو كل ما نسى العقل وهو اللبن الحليب يصب عليه ماء (tahdhib)","source_summary":"Derlenmiş kaynak kanıtının ortak nesnesi, üzerine su dökülmüş süttür. Aktarım içindeki ek açıklama, bu içeceğe zihni unutturan bir etki yükler; bu niteleme süt ve su karışımı çekirdeğinden ayrı bir kaynak çeşitlemesidir.","sources":["TA","MQ"],"what_is_ar":"يدخل فيه النَّسِي أو النَّسء أو النَّسِيء اسما للحليب الذي يصب عليه الماء، وما وصف بأنه ينسى العقل في هذا النقل.","what_is_not_ar":"ليس النسيان العام، ولا النسيئة بمعنى البيع المؤجل، ولا بدء السمن في الدواب."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["87:6:1"],"branch_refs":[],"candidate_id":"cand_6f8978346f5e02d48a0e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001210"],"scope":"focus_ayah","source_local_id":"87:6:1:articulated-sound-texture","source_type":"word_analysis","support_ids":["sup_18be7e8e0ca36032112e","sup_cfb7c520b8d847e52a82"],"title":"controlled articulation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:1","qac_refs":["87:6:1:1","87:6:1:2","87:6:1:3"],"status":"accepted"}},{"anchor_refs":["87:6:1"],"branch_refs":[],"candidate_id":"cand_8850ebee9b071f282fcf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001210"],"scope":"focus_ayah","source_local_id":"87:6:1:bounded-promise-context","source_type":"word_analysis","support_ids":["sup_c460514a052c561113ad","sup_cfb7c520b8d847e52a82"],"title":"promise before divine reservation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:1","qac_refs":["87:6:1:1","87:6:1:2","87:6:1:3"],"status":"accepted"}},{"anchor_refs":["87:6:1"],"branch_refs":[],"candidate_id":"cand_9af05d1f691d6454b588","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001210"],"scope":"focus_ayah","source_local_id":"87:6:1:direct-address-and-echoes","source_type":"word_analysis","support_ids":["sup_5e7498f1d796de314bd0","sup_cfb7c520b8d847e52a82"],"title":"direct promise after cosmic acts","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:1","qac_refs":["87:6:1:1","87:6:1:2","87:6:1:3"],"status":"accepted"}},{"anchor_refs":["87:6:1"],"branch_refs":[],"candidate_id":"cand_decd01f5454cb2c16d12","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001210"],"scope":"focus_ayah","source_local_id":"87:6:1:form-iv-role-contrast","source_type":"word_analysis","support_ids":["sup_6308f9f069f86adcc9d7","sup_cfb7c520b8d847e52a82"],"title":"enabler role, not drilling or testing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:1","qac_refs":["87:6:1:1","87:6:1:2","87:6:1:3"],"status":"accepted"}},{"anchor_refs":["87:6:1"],"branch_refs":[],"candidate_id":"cand_50e84d6bf899e4afcbf0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001210"],"scope":"focus_ayah","source_local_id":"87:6:1:future-causative-promise","source_type":"word_analysis","support_ids":["sup_bf990fc465774ae0448b","sup_cfb7c520b8d847e52a82"],"title":"future causative promise","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:1","qac_refs":["87:6:1:1","87:6:1:2","87:6:1:3"],"status":"accepted"}},{"anchor_refs":["87:6:1"],"branch_refs":[],"candidate_id":"cand_f701668400d09a2c9306","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001210"],"scope":"focus_ayah","source_local_id":"87:6:1:ordered-gathered-recitation","source_type":"word_analysis","support_ids":["sup_8fec112df744e52ea906","sup_cfb7c520b8d847e52a82"],"title":"ordered gathered recitation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:1","qac_refs":["87:6:1:1","87:6:1:2","87:6:1:3"],"status":"accepted"}},{"anchor_refs":["87:6:1"],"branch_refs":[],"candidate_id":"cand_58f019adf5782aad2c91","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001210"],"scope":"focus_ayah","source_local_id":"87:6:1:shared-content-ellipsis","source_type":"word_analysis","support_ids":["sup_27145784e850ace07ced","sup_cfb7c520b8d847e52a82"],"title":"one unspoken content domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:1","qac_refs":["87:6:1:1","87:6:1:2","87:6:1:3"],"status":"accepted"}},{"anchor_refs":["87:6:1"],"branch_refs":[],"candidate_id":"cand_64a628f5c23112c205d0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001210"],"scope":"focus_ayah","source_local_id":"87:6:1:subject-object-recipient","source_type":"word_analysis","support_ids":["sup_083c678ce6bdf38abee1","sup_cfb7c520b8d847e52a82"],"title":"agency and reception in one word","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:1","qac_refs":["87:6:1:1","87:6:1:2","87:6:1:3"],"status":"accepted"}},{"anchor_refs":["87:6:2"],"branch_refs":[],"candidate_id":"cand_6336b52a6b22f4a570c6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:6:2:quick-fa-la-cadence","source_type":"word_analysis","support_ids":["sup_75ad6624d30bdb0f4e88","sup_9e3f83eacb64fed141eb"],"title":"quick onset into negation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:2","qac_refs":["87:6:2:1"],"status":"accepted"}},{"anchor_refs":["87:6:2"],"branch_refs":[],"candidate_id":"cand_aed3ce462d75a49a2267","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:6:2:resultive-hinge","source_type":"word_analysis","support_ids":["sup_31e0eadeed339b602bf0","sup_9e3f83eacb64fed141eb"],"title":"resultive hinge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:2","qac_refs":["87:6:2:1"],"status":"accepted"}},{"anchor_refs":["87:6:2"],"branch_refs":[],"candidate_id":"cand_bdcb02e1481839209c4a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:6:2:sequence-causation-compactness","source_type":"word_analysis","support_ids":["sup_4c53bae7431d675f0617","sup_9e3f83eacb64fed141eb"],"title":"sequence and causation together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:2","qac_refs":["87:6:2:1"],"status":"accepted"}},{"anchor_refs":["87:6:2"],"branch_refs":[],"candidate_id":"cand_9dd169abed80b65ceabd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:6:2:whole-negative-clause-scope","source_type":"word_analysis","support_ids":["sup_9e3f83eacb64fed141eb","sup_d6bbf783da5a91e7c371"],"title":"scope over the negative clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:2","qac_refs":["87:6:2:1"],"status":"accepted"}},{"anchor_refs":["87:6:3"],"branch_refs":[],"candidate_id":"cand_cbab974cdfc56da62847","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:6:3:bounded-by-exception","source_type":"word_analysis","support_ids":["sup_871dfd9c0173e30071fd","sup_b3970c3d546b0a3592be"],"title":"bounded assurance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:3","qac_refs":["87:6:2:2"],"status":"accepted"}},{"anchor_refs":["87:6:3"],"branch_refs":[],"candidate_id":"cand_5826295e58bd5cb5c1a1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:6:3:broad-denial-of-vulnerability","source_type":"word_analysis","support_ids":["sup_3aa7b013d1e1e0c31c27","sup_871dfd9c0173e30071fd"],"title":"broad denial of lapse","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:3","qac_refs":["87:6:2:2"],"status":"accepted"}},{"anchor_refs":["87:6:3"],"branch_refs":[],"candidate_id":"cand_a99a901f79b95b54874f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:6:3:lan-variant-pressure","source_type":"word_analysis","support_ids":["sup_144970ff42aab07620e7","sup_871dfd9c0173e30071fd"],"title":"future denial variant pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:3","qac_refs":["87:6:2:2"],"status":"accepted"}},{"anchor_refs":["87:6:3"],"branch_refs":[],"candidate_id":"cand_8a81b4b81689f45c5ec0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:6:3:local-promissory-negation","source_type":"word_analysis","support_ids":["sup_0c0de7e28accdd8e3830","sup_871dfd9c0173e30071fd"],"title":"promissory negation, not command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:3","qac_refs":["87:6:2:2"],"status":"accepted"}},{"anchor_refs":["87:6:3"],"branch_refs":[],"candidate_id":"cand_dd9655c662d4171bc192","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:6:3:negation-slot-after-fa","source_type":"word_analysis","support_ids":["sup_1d1b5801d98b8fe63c20","sup_871dfd9c0173e30071fd"],"title":"separable negation slot","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:3","qac_refs":["87:6:2:2"],"status":"accepted"}},{"anchor_refs":["87:6:3"],"branch_refs":[],"candidate_id":"cand_0a8c37fb007964c268f3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:6:3:negative-cadence","source_type":"word_analysis","support_ids":["sup_3daa62ab196d9b4a8084","sup_871dfd9c0173e30071fd"],"title":"negative cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:3","qac_refs":["87:6:2:2"],"status":"accepted"}},{"anchor_refs":["87:6:4"],"branch_refs":[],"candidate_id":"cand_e2a7582b5e5e3c5d2e27","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001501"],"scope":"focus_ayah","source_local_id":"87:6:4:addressee-continuity","source_type":"word_analysis","support_ids":["sup_5421d0f7d267c8ae46f3","sup_eef8406c66ffc7bd0196"],"title":"recipient becomes rememberer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:4","qac_refs":["87:6:3:1"],"status":"accepted"}},{"anchor_refs":["87:6:4"],"branch_refs":[],"candidate_id":"cand_5e1a5f7b145e071e2d8f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001501"],"scope":"focus_ayah","source_local_id":"87:6:4:deficiency-and-human-contrast","source_type":"word_analysis","support_ids":["sup_db3b98010d6546828484","sup_eef8406c66ffc7bd0196"],"title":"human weakness suspended","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:4","qac_refs":["87:6:3:1"],"status":"accepted"}},{"anchor_refs":["87:6:4"],"branch_refs":[],"candidate_id":"cand_3d4e55844a9676ea278e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001501"],"scope":"focus_ayah","source_local_id":"87:6:4:exception-bound-closure","source_type":"word_analysis","support_ids":["sup_c5a76b6e3495d578e703","sup_eef8406c66ffc7bd0196"],"title":"closure opens to exception","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:4","qac_refs":["87:6:3:1"],"status":"accepted"}},{"anchor_refs":["87:6:4"],"branch_refs":[],"candidate_id":"cand_c509775bc0700215498c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001501"],"scope":"focus_ayah","source_local_id":"87:6:4:forgetting-neglect-range","source_type":"word_analysis","support_ids":["sup_2d9b8b0fb91fc94baf74","sup_eef8406c66ffc7bd0196"],"title":"forgetting and neglect range","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:4","qac_refs":["87:6:3:1"],"status":"accepted"}},{"anchor_refs":["87:6:4"],"branch_refs":[],"candidate_id":"cand_5b93c61205336f93dc50","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001501"],"scope":"focus_ayah","source_local_id":"87:6:4:long-final-sound","source_type":"word_analysis","support_ids":["sup_eef8406c66ffc7bd0196","sup_fee6b7cb4df41b18beb6"],"title":"long final suspended loss","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:4","qac_refs":["87:6:3:1"],"status":"accepted"}},{"anchor_refs":["87:6:4"],"branch_refs":[],"candidate_id":"cand_841b1b1028804698e722","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001501"],"scope":"focus_ayah","source_local_id":"87:6:4:negated-imperfect-lapse","source_type":"word_analysis","support_ids":["sup_936a6805f21edb228494","sup_eef8406c66ffc7bd0196"],"title":"future lapse prevented","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:4","qac_refs":["87:6:3:1"],"status":"accepted"}},{"anchor_refs":["87:6:4"],"branch_refs":[],"candidate_id":"cand_509c42b24a7c077248e7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001501"],"scope":"focus_ayah","source_local_id":"87:6:4:objectless-forgetting","source_type":"word_analysis","support_ids":["sup_bf519fec246dcaf6994a","sup_eef8406c66ffc7bd0196"],"title":"objectless verb carries content backward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:4","qac_refs":["87:6:3:1"],"status":"accepted"}},{"anchor_refs":["87:6:4"],"branch_refs":[],"candidate_id":"cand_665cccf190b93456229f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001501"],"scope":"focus_ayah","source_local_id":"87:6:4:ordinary-human-vulnerability","source_type":"word_analysis","support_ids":["sup_eef8406c66ffc7bd0196","sup_fb55dfafcc223dceaa4f"],"title":"ordinary lapse, not caused or feigned","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:6:4","qac_refs":["87:6:3:1"],"status":"accepted"}},{"anchor_refs":["87:6:1"],"branch_refs":[],"candidate_id":"cand_71ece00f5adf6b14a492","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001210"],"scope":"focus_ayah","source_local_id":"87:6:1:2","source_type":"qac_morpheme","support_ids":["sup_b184ed0fabdd29163f9f"],"title":"QAC root occurrence: ق ر ء","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:6:3"],"branch_refs":[],"candidate_id":"cand_0a4963ccbe11af965015","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001501"],"scope":"focus_ayah","source_local_id":"87:6:3:1","source_type":"qac_morpheme","support_ids":["sup_d7ce78f6ab309a35bba6"],"title":"QAC root occurrence: ن س ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:6","branch_refs":["root_001210/B002","root_001501/B001"],"candidate_id":"cand_2b7db860171b31b46b4b","commentary_obligation":"review","hft_ref":"hft_0727afe65a8739b15f5c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_causative_retention","source_type":"hft","support_ids":["sup_bd293e59b781f5cdb243"],"title":"baseline_causative_retention","trust":"legacy_unbound"},{"anchor_refs":["87:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:6","branch_refs":["root_001210/B001","root_001501/B001"],"candidate_id":"cand_f5954b487310c3a162ba","commentary_obligation":"review","hft_ref":"hft_091b886a01de686dafee","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_gathered_sequence","source_type":"hft","support_ids":["sup_b6518febf92a70fbe9e8"],"title":"baseline_gathered_sequence","trust":"legacy_unbound"},{"anchor_refs":["87:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:6","branch_refs":["root_001210/B011","root_001501/B002"],"candidate_id":"cand_9f18df84224d99c52b7f","commentary_obligation":"review","hft_ref":"hft_1d1d43c64f566f2ec5ac","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_nonabandonment","source_type":"hft","support_ids":["sup_b6f48b85c5b6c28ae31c"],"title":"baseline_nonabandonment","trust":"legacy_unbound"},{"anchor_refs":["87:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:6","branch_refs":["root_001210/B006","root_001501/B002"],"candidate_id":"cand_1d23a7a51c07dc805bb2","commentary_obligation":"review","hft_ref":"hft_b2af7713f8962399b57d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_formed_reciter","source_type":"hft","support_ids":["sup_5bc2650d97db231b4003"],"title":"baseline_formed_reciter","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"سَنُقْرِئُكَ فَلَا تَنسَىٰٓ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|sa+","morpheme_role":"PREFIX","pos":"FUT","qac_ref":"87:6:1:1","qac_word_ref":"87:6:1","root_ar":"","surface_ar":"سَ"},{"lemma_ar":"نُقْرِئُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:nuqori}u|ROOT:qrA|1P","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:1:2","qac_word_ref":"87:6:1","root_ar":"ق ر ء","surface_ar":"نُقْرِئُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"87:6:1:3","qac_word_ref":"87:6:1","root_ar":"","surface_ar":"كَ"},{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"87:6:2:1","qac_word_ref":"87:6:2","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"87:6:2:2","qac_word_ref":"87:6:2","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"نَسِىَ","morph_features":"STEM|POS:V|IMPF|LEM:nasiYa|ROOT:nsy|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:3:1","qac_word_ref":"87:6:3","root_ar":"ن س ي","surface_ar":"تَنسَىٰٓ"}],"word_analysis_qac_refs":[["87:6:1:1","87:6:1:2","87:6:1:3"],["87:6:2:1"],["87:6:2:2"],["87:6:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["87:6:1","87:6:2","87:6:3","87:6:4"]},"focus_surface_evidence":{"arabic_uthmani":"سَنُقْرِئُكَ فَلَا تَنسَىٰٓ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|sa+","morpheme_role":"PREFIX","pos":"FUT","qac_ref":"87:6:1:1","qac_word_ref":"87:6:1","root_ar":"","surface_ar":"سَ"},{"lemma_ar":"نُقْرِئُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:nuqori}u|ROOT:qrA|1P","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:1:2","qac_word_ref":"87:6:1","root_ar":"ق ر ء","surface_ar":"نُقْرِئُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"87:6:1:3","qac_word_ref":"87:6:1","root_ar":"","surface_ar":"كَ"},{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"87:6:2:1","qac_word_ref":"87:6:2","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"87:6:2:2","qac_word_ref":"87:6:2","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"نَسِىَ","morph_features":"STEM|POS:V|IMPF|LEM:nasiYa|ROOT:nsy|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:6:3:1","qac_word_ref":"87:6:3","root_ar":"ن س ي","surface_ar":"تَنسَىٰٓ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["87:6:1:1","87:6:1:2","87:6:1:3"],["87:6:2:1"],["87:6:2:2"],["87:6:3:1"]],"word_analysis_refs":["87:6:1","87:6:2","87:6:3","87:6:4"],"word_rows":[{"analysis_record_ref":"87:6:1","analytic_gloss_range_en":"future Form IV causative recitation addressed to a 2ms recipient; locally, divine enabling of recitation with the recited content left unexpressed","analytic_root_gloss_range_en":"reading, reciting, making another recite, gathering speech into ordered recitation, and broader nonlocal branches such as cycles or appointed times; the local form selects causative recitation","qac_refs":["87:6:1:1","87:6:1:2","87:6:1:3"],"root":{"arabic":"ق ر ء","transliteration":"q-r-ʾ"},"surface":{"arabic":"سَنُقْرِئُكَ","transliteration":"sanuqriʾuka"}},{"analysis_record_ref":"87:6:2","analytic_gloss_range_en":"conjunctive/resultive particle; locally links the recitation promise to the whole following negated outcome","analytic_root_gloss_range_en":null,"qac_refs":["87:6:2:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"87:6:3","analytic_gloss_range_en":"negative particle over the following imperfect; locally promissory non-occurrence rather than prohibition","analytic_root_gloss_range_en":null,"qac_refs":["87:6:2:2"],"root":{"note":"— (no root)"},"surface":{"arabic":"لَا","transliteration":"lā"}},{"analysis_record_ref":"87:6:4","analytic_gloss_range_en":"Form I imperfect 2ms under negation: you forget, neglect, or let slip; locally objectless because the recited content is supplied by the prior promise","analytic_root_gloss_range_en":"forgetting, loss of recall, neglect, leaving aside, abandoned forgotten things, and nonlocal branches such as sciatic-vein or postponement terms; the local clause selects negated loss or neglect of the caused recitation","qac_refs":["87:6:3:1"],"root":{"arabic":"ن س ي","transliteration":"n-s-y"},"surface":{"arabic":"تَنسَىٰٓ","transliteration":"tansā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["87:6"],"branch_refs":["root_001210/B002","root_001501/B001"],"candidate_id":"cand_2b7db860171b31b46b4b","evidence_scope":"focus_ayah","hft_ref":"hft_0727afe65a8739b15f5c","item_id":"baseline_causative_retention","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_causative_retention","support_id":"sup_bd293e59b781f5cdb243"},{"anchor_refs":["87:6"],"branch_refs":["root_001210/B001","root_001501/B001"],"candidate_id":"cand_f5954b487310c3a162ba","evidence_scope":"focus_ayah","hft_ref":"hft_091b886a01de686dafee","item_id":"baseline_gathered_sequence","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_gathered_sequence","support_id":"sup_b6518febf92a70fbe9e8"},{"anchor_refs":["87:6"],"branch_refs":["root_001210/B011","root_001501/B002"],"candidate_id":"cand_9f18df84224d99c52b7f","evidence_scope":"focus_ayah","hft_ref":"hft_1d1d43c64f566f2ec5ac","item_id":"baseline_nonabandonment","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_nonabandonment","support_id":"sup_b6f48b85c5b6c28ae31c"},{"anchor_refs":["87:6"],"branch_refs":["root_001210/B006","root_001501/B002"],"candidate_id":"cand_1d23a7a51c07dc805bb2","evidence_scope":"focus_ayah","hft_ref":"hft_b2af7713f8962399b57d","item_id":"baseline_formed_reciter","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_formed_reciter","support_id":"sup_5bc2650d97db231b4003"}],"diagnostics":[],"lane_counts":{"global":9,"macro":11,"micro":4},"packet_summary":{"ayah_count":19,"focus_ref":"87:6","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ء ث ر","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":true,"target_occurrences":9,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]}],"window":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"87:6","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"87:6","lane":"micro","linguistic_source_ref":"87:6","surface_ref":"87:6","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"87:6","target_tokens":[["Sana",["87:6:1"]],["okutacağız",["87:6:1"]],["böylece",["87:6:2"]],["unutmayacaksın",["87:6:2","87:6:3"]]],"text":"Sana okutacağız; böylece unutmayacaksın."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s087-p01-001-019","label":"Whole surah","number":1,"refs":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:1:subject-object-recipient","source_type":"word_analysis","support_id":"sup_083c678ce6bdf38abee1","text":"{\"blocking_evidence\":null,\"headline\":\"agency and reception in one word\",\"reader_payoff\":\"The reader sees divine agency and prophetic reception occupying the same compact verbal form before any result is stated.\",\"reason\":\"The clitic object is syntactically forced, and the exact form occurs as a low-occurrence causative verb with a clitic object in the contextual profile.\",\"representative_source_ids\":[\"QG-adc43bbe\",\"MG-51d27b58\",\"QT-3c9f30eb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:3:local-promissory-negation","source_type":"word_analysis","support_id":"sup_0c0de7e28accdd8e3830","text":"{\"blocking_evidence\":null,\"headline\":\"promissory negation, not command\",\"reader_payoff\":\"The reader notices that the wording promises non-forgetting instead of issuing a command not to forget.\",\"reason\":\"QAC marks {{ar:لَا}} ({{tr:lā}}) as a negative particle, and attachment evidence scopes it over {{ar:تَنسَىٰٓ}} ({{tr:tansā}}) inside the result clause.\",\"representative_source_ids\":[\"QG-3fccbbb6\",\"QG-e8233370\",\"QT-252fbe27\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:3:lan-variant-pressure","source_type":"word_analysis","support_id":"sup_144970ff42aab07620e7","text":"{\"blocking_evidence\":null,\"headline\":\"future denial variant pressure\",\"reader_payoff\":\"The reader notices that accepted variant pressure makes the future force explicit, while the local source reading keeps {{ar:لَا}} ({{tr:lā}}) as the governing surface.\",\"reason\":\"The reported {{ar:فَلَنْ}} ({{tr:fa-lan}}) reading can sharpen prospective denial and mood pressure, but it does not replace the aligned source particle {{ar:لَا}} ({{tr:lā}}).\",\"representative_source_ids\":[\"QG-24e43e03\",\"QF-dc9069cf\",\"MI-ad5a2513\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:1:articulated-sound-texture","source_type":"word_analysis","support_id":"sup_18be7e8e0ca36032112e","text":"{\"blocking_evidence\":null,\"headline\":\"controlled articulation\",\"reader_payoff\":\"The reader can hear the compact stop-and-hamza texture matching controlled articulated delivery before the clause turns to non-forgetting.\",\"reason\":\"The sound claim is tied to the actual {{ar:ق ر ء}} ({{tr:q-r-ʾ}}) surface in {{ar:سَنُقْرِئُكَ}} ({{tr:sanuqriʾuka}}) and does not alter grammar or lexical selection.\",\"representative_source_ids\":[\"QF-cb17fa52\",\"QP-2eb39e93\",\"MP-a50a2cab\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:3:negation-slot-after-fa","source_type":"word_analysis","support_id":"sup_1d1b5801d98b8fe63c20","text":"{\"blocking_evidence\":null,\"headline\":\"separable negation slot\",\"reader_payoff\":\"The reader sees that the negator is a real morphemic position after the resultive particle, not just an inseparable spelling bundle.\",\"reason\":\"The bundle analyzes {{ar:فَ}} ({{tr:fa}}) and {{ar:لَا}} ({{tr:lā}}) separately, and the reported replacement with {{ar:لَنْ}} ({{tr:lan}}) confirms that the negation position is structurally active.\",\"representative_source_ids\":[\"QF-e87e6017\",\"QF-fb39aeaa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:1:shared-content-ellipsis","source_type":"word_analysis","support_id":"sup_27145784e850ace07ced","text":"{\"blocking_evidence\":null,\"headline\":\"one unspoken content domain\",\"reader_payoff\":\"The reader notices that what is caused to be recited and what will not be forgotten are the same unspoken content-domain.\",\"reason\":\"The first verb has only the addressee object expressed, and the later forgetting verb has no expressed object; the result-clause relation licenses carrying the recited content forward.\",\"representative_source_ids\":[\"QG-4aed57fa\",\"QG-511b382c\",\"QT-0a9c159f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:4:forgetting-neglect-range","source_type":"word_analysis","support_id":"sup_2d9b8b0fb91fc94baf74","text":"{\"blocking_evidence\":null,\"headline\":\"forgetting and neglect range\",\"reader_payoff\":\"The reader notices that the promise protects both recall and faithful attention to the recited content, while the local object-domain limits the broad root range.\",\"reason\":\"V4 supports forgetting, neglect, and abandoned-thing branches for {{ar:ن س ي}} ({{tr:n-s-y}}), but local syntax selects loss or neglect of the prior recited content rather than remote branches.\",\"representative_source_ids\":[\"QS-3de83515\",\"QS-aa9cc836\",\"MS-4bee0257\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:2:resultive-hinge","source_type":"word_analysis","support_id":"sup_31e0eadeed339b602bf0","text":"{\"blocking_evidence\":null,\"headline\":\"resultive hinge\",\"reader_payoff\":\"The reader notices that non-forgetting follows from divine causation rather than standing beside it as a separate favor.\",\"reason\":\"Attachment evidence marks 87:6:2-4 as a result clause after {{ar:سَنُقْرِئُكَ}} ({{tr:sanuqriʾuka}}), and QAC describes {{ar:فَ}} ({{tr:fa}}) as close sequence or result.\",\"representative_source_ids\":[\"QG-2343be28\",\"MG-d1760a4c\",\"QT-90fd90e4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:3:broad-denial-of-vulnerability","source_type":"word_analysis","support_id":"sup_3aa7b013d1e1e0c31c27","text":"{\"blocking_evidence\":null,\"headline\":\"broad denial of lapse\",\"reader_payoff\":\"The reader sees the vulnerability of forgetting blocked as an operative future possibility, not merely one isolated episode.\",\"reason\":\"The local imperfect is negated in a result clause after a future causative promise, supporting broad promised non-occurrence without turning the clause into prohibition.\",\"representative_source_ids\":[\"MG-345c11da\",\"QS-23d9c699\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:3:negative-cadence","source_type":"word_analysis","support_id":"sup_3daa62ab196d9b4a8084","text":"{\"blocking_evidence\":null,\"headline\":\"negative cadence\",\"reader_payoff\":\"The reader can hear the open negation carried into the verb it negates.\",\"reason\":\"The sound claim is local to the open vowel of {{ar:لَا}} ({{tr:lā}}) before the long final vowel of {{ar:تَنسَىٰٓ}} ({{tr:tansā}}).\",\"representative_source_ids\":[\"QP-50518cd0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:2:sequence-causation-compactness","source_type":"word_analysis","support_id":"sup_4c53bae7431d675f0617","text":"{\"blocking_evidence\":null,\"headline\":\"sequence and causation together\",\"reader_payoff\":\"The reader feels the ayah's logic compressed: being made to recite is immediately the ground from which not forgetting follows.\",\"reason\":\"The close particle sequence and the result-clause analysis support both immediacy and consequence without reducing {{ar:فَ}} ({{tr:fa}}) to loose coordination.\",\"representative_source_ids\":[\"QS-cb309c8e\",\"QF-1f6eb8e6\",\"QY-3bc5c5a2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:4:addressee-continuity","source_type":"word_analysis","support_id":"sup_5421d0f7d267c8ae46f3","text":"{\"blocking_evidence\":null,\"headline\":\"recipient becomes rememberer\",\"reader_payoff\":\"The reader notices that the same addressed person moves from recipient of recitation to subject of protected non-forgetting.\",\"reason\":\"Attachment evidence marks {{ar:تَنسَىٰٓ}} ({{tr:tansā}}) as having an unexpressed 2ms subject matching the addressed object in {{ar:سَنُقْرِئُكَ}} ({{tr:sanuqriʾuka}}).\",\"representative_source_ids\":[\"QG-3b40c54c\",\"QG-e2f97713\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:1:direct-address-and-echoes","source_type":"word_analysis","support_id":"sup_5e7498f1d796de314bd0","text":"{\"blocking_evidence\":null,\"headline\":\"direct promise after cosmic acts\",\"reader_payoff\":\"The reader hears the surah pivot from described divine acts into direct address, with older recitation scenes personalized as promise.\",\"reason\":\"The CRITICAL rows give concrete echoes to gathering and recitation in 75:17-18 and the command {{ar:ٱقْرَأْ}} ({{tr:iqraʾ}}) in 96:1; local morphology confirms direct second-person address.\",\"representative_source_ids\":[\"QI-ce423b78\",\"MI-eee661f3\",\"QE-2b9ede39\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:1:form-iv-role-contrast","source_type":"word_analysis","support_id":"sup_6308f9f069f86adcc9d7","text":"{\"blocking_evidence\":null,\"headline\":\"enabler role, not drilling or testing\",\"reader_payoff\":\"The reader notices a split between the one who enables recitation and the one who performs it, while non-surface stems stay only as contrast.\",\"reason\":\"The surface is Form IV causative {{ar:أَقْرَأَ}} ({{tr:aqraʾa}}) patterning, so repeated training, seeking, or examination stems do not govern the local parse.\",\"representative_source_ids\":[\"QS-1dc0d0c6\",\"QF-875afc87\",\"QF-f4b132ff\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:2:quick-fa-la-cadence","source_type":"word_analysis","support_id":"sup_75ad6624d30bdb0f4e88","text":"{\"blocking_evidence\":null,\"headline\":\"quick onset into negation\",\"reader_payoff\":\"The reader can hear the result arrive with little delay as the short particle runs into the negator.\",\"reason\":\"The phonetic point is modest and surface-bound: {{ar:فَ}} ({{tr:fa}}) directly precedes {{ar:لَا}} ({{tr:lā}}) in the recited sequence.\",\"representative_source_ids\":[\"QP-5cbd3abe\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:3","source_type":"word_analysis","support_id":"sup_871dfd9c0173e30071fd","text":"{\"gloss_range\":\"negative particle over the following imperfect; locally promissory non-occurrence rather than prohibition\",\"prose\":\"{{ar:لَا}} ({{tr:lā}}) negates {{ar:تَنسَىٰٓ}} ({{tr:tansā}}), not the promise that precedes it. The clause is therefore promissory, not an imperative command to remember: the expected lapse is denied as the result of being made to recite. The reported {{ar:لَنْ}} ({{tr:lan}}) reading sharpens future denial and shows that the negation slot after {{ar:فَ}} ({{tr:fa}}) is structurally real, but the source surface remains broad {{ar:لَا}} ({{tr:lā}}) with the imperfect. That broad denial blocks not just one remembered episode but the operative vulnerability of future forgetting, yet it is bounded because 87:7 immediately qualifies it with a divine-will exception. The open vowel of {{ar:لَا}} ({{tr:lā}}) also carries into the long close of {{ar:تَنسَىٰٓ}} ({{tr:tansā}}), making the negation and the denied verb sound joined.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَا}} ({{tr:lā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:1:ordered-gathered-recitation","source_type":"word_analysis","support_id":"sup_8fec112df744e52ea906","text":"{\"blocking_evidence\":null,\"headline\":\"ordered gathered recitation\",\"reader_payoff\":\"The reader notices that the protected recitation is an ordered gathered articulation, not bare sound or isolated remembered meaning.\",\"reason\":\"V4 supports reading, recitation, and gathering-speech branches for {{ar:ق ر ء}} ({{tr:q-r-ʾ}}), but the local Form IV grammar selects causing recitation rather than unrelated cycle, pregnancy, greeting, or holding branches.\",\"representative_source_ids\":[\"QS-274b88c3\",\"QS-dc47ea0f\",\"MS-71ea1e01\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:4:negated-imperfect-lapse","source_type":"word_analysis","support_id":"sup_936a6805f21edb228494","text":"{\"blocking_evidence\":null,\"headline\":\"future lapse prevented\",\"reader_payoff\":\"The reader sees the root shifted from reported forgetting into a prevented future or ongoing lapse at the ayah's close.\",\"reason\":\"QAC marks a 2ms imperfect negated by {{ar:لَا}} ({{tr:lā}}); the profile notes frequent negated/scoped uses for this exact root-form group.\",\"representative_source_ids\":[\"QG-c43a067f\",\"QI-729f8b93\",\"QT-23713bd8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:2","source_type":"word_analysis","support_id":"sup_9e3f83eacb64fed141eb","text":"{\"gloss_range\":\"conjunctive/resultive particle; locally links the recitation promise to the whole following negated outcome\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) is the hinge where caused recitation becomes protected memory. It does not merely attach to the following negator as spelling; it links the whole {{ar:لَا تَنسَىٰٓ}} ({{tr:lā tansā}}) outcome to {{ar:سَنُقْرِئُكَ}} ({{tr:sanuqriʾuka}}). That makes non-forgetting consequential rather than a loosely coordinated second favor, while the particle's close-sequence value keeps the result immediate. Even though the written surface fuses into {{ar:فَلَا}} ({{tr:fa-lā}}), the analytic split preserves the particle's independent scope over the clause transition. Its short sound runs directly into the negation, so the listener meets denial of forgetting already attached to the promise.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:6:1:2","source_type":"qac_morpheme","support_id":"sup_b184ed0fabdd29163f9f","text":"{\"lemma_ar\":\"نُقْرِئُ\",\"morph_features\":\"STEM|POS:V|IMPF|(IV)|LEM:nuqori}u|ROOT:qrA|1P\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"87:6:1:2\",\"qac_word_ref\":\"87:6:1\",\"root_ar\":\"ق ر ء\",\"surface_ar\":\"نُقْرِئُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:3:bounded-by-exception","source_type":"word_analysis","support_id":"sup_b3970c3d546b0a3592be","text":"{\"blocking_evidence\":null,\"headline\":\"bounded assurance\",\"reader_payoff\":\"The reader notices that the assurance is strong but not autonomous, because 87:7 places it under explicit divine will.\",\"reason\":\"The following exception in 87:7 narrows the negated promise opened by {{ar:لَا}} ({{tr:lā}}) rather than replacing it.\",\"representative_source_ids\":[\"QI-7d325d4d\",\"QB-8161a0cb\",\"QY-e716cb1a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:4:objectless-forgetting","source_type":"word_analysis","support_id":"sup_bf519fec246dcaf6994a","text":"{\"blocking_evidence\":null,\"headline\":\"objectless verb carries content backward\",\"reader_payoff\":\"The reader notices that the missing object forces the recitation promise to supply the content protected from loss.\",\"reason\":\"The verb instance is marked obj=none_absolute with a transfer warning that Arabic does not express an object; the prior recitation clause supplies the recoverable domain.\",\"representative_source_ids\":[\"QG-88fd6b58\",\"QG-a57a4a9e\",\"QT-ddbb80cf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:1:future-causative-promise","source_type":"word_analysis","support_id":"sup_bf990fc465774ae0448b","text":"{\"blocking_evidence\":null,\"headline\":\"future causative promise\",\"reader_payoff\":\"The reader notices that recitation begins as promised divine enablement, not as a command or an already completed memory state.\",\"reason\":\"QAC and attachment evidence identify {{ar:سَنُقْرِئُكَ}} ({{tr:sanuqriʾuka}}) as a Form IV imperfect with future {{ar:سَ}} ({{tr:sa}}), first common plural subject agreement, and a 2ms object suffix.\",\"representative_source_ids\":[\"QG-6a9c63e5\",\"QG-93c5ce8f\",\"QF-a7935834\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:1:bounded-promise-context","source_type":"word_analysis","support_id":"sup_c460514a052c561113ad","text":"{\"blocking_evidence\":null,\"headline\":\"promise before divine reservation\",\"reader_payoff\":\"The reader notices the scene-boundary: completed ecological acts give way to projected verbal preservation, which 87:7 immediately keeps under divine will.\",\"reason\":\"The future promise follows the prior made-and-reduced pasture scene and is followed by the divine-will qualification in 87:7.\",\"representative_source_ids\":[\"QB-57a0aae5\",\"QB-d7c4cce2\",\"QB-c790b2de\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:4:exception-bound-closure","source_type":"word_analysis","support_id":"sup_c5a76b6e3495d578e703","text":"{\"blocking_evidence\":null,\"headline\":\"closure opens to exception\",\"reader_payoff\":\"The reader notices that the final word is exactly the domain qualified by 87:7, so the assurance stays under divine will.\",\"reason\":\"The next ayah's exception in 87:7 qualifies the non-forgetting claim anchored in the final verb of 87:6.\",\"representative_source_ids\":[\"QI-29b66ab6\",\"QI-ff53141c\",\"QB-50046846\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:1","source_type":"word_analysis","support_id":"sup_cfb7c520b8d847e52a82","text":"{\"gloss_range\":\"future Form IV causative recitation addressed to a 2ms recipient; locally, divine enabling of recitation with the recited content left unexpressed\",\"prose\":\"{{ar:سَنُقْرِئُكَ}} ({{tr:sanuqriʾuka}}) opens the ayah as a complete one-word promise: future prefix, first-person plural divine subject, Form IV causation, and second-person object are all compressed before the result clause arrives. The addressee is not commanded to produce recitation from himself; he is made the recipient and performer of a recitation enabled by the speaker. The unspoken content after the verb is the same domain later protected from forgetting, so reception and retention are bound by shared ellipsis rather than by repeated nouns. The {{ar:ق ر ء}} ({{tr:q-r-ʾ}}) range keeps recitation as ordered, gathered articulation, while local grammar selects causative recitation and not unrelated cycle or womb branches. After the third-person divine acts and pasture-to-residue scene (87:1-5), this direct address turns ecological completion into projected verbal preservation, personalizing the gathering-and-recitation responsibility of 75:17-18 and shifting the familiar command {{ar:ٱقْرَأْ}} ({{tr:iqraʾ}}) (96:1) into enabled reception before 87:7 keeps the promise under divine will. The dense {{ar:ق ر ء}} ({{tr:q-r-ʾ}}) articulation makes the promised delivery feel controlled before the ayah opens into the denied loss.\",\"root_display\":\"{{ar:ق ر ء}} ({{tr:q-r-ʾ}})\",\"root_gloss_range\":\"reading, reciting, making another recite, gathering speech into ordered recitation, and broader nonlocal branches such as cycles or appointed times; the local form selects causative recitation\",\"surface_display\":\"{{ar:سَنُقْرِئُكَ}} ({{tr:sanuqriʾuka}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:2:whole-negative-clause-scope","source_type":"word_analysis","support_id":"sup_d6bbf783da5a91e7c371","text":"{\"blocking_evidence\":null,\"headline\":\"scope over the negative clause\",\"reader_payoff\":\"The reader sees that the particle governs the transition into the whole negated clause, not only the written onset before the negator.\",\"reason\":\"The bundle splits {{ar:فَ}} ({{tr:fa}}) and {{ar:لَا}} ({{tr:lā}}) while still treating {{ar:فَلَا تَنسَىٰٓ}} ({{tr:fa-lā tansā}}) as the resulting negated outcome.\",\"representative_source_ids\":[\"QG-d81dbdd1\",\"QF-297a7144\",\"QT-46e40389\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:6:3:1","source_type":"qac_morpheme","support_id":"sup_d7ce78f6ab309a35bba6","text":"{\"lemma_ar\":\"نَسِىَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:nasiYa|ROOT:nsy|2MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"87:6:3:1\",\"qac_word_ref\":\"87:6:3\",\"root_ar\":\"ن س ي\",\"surface_ar\":\"تَنسَىٰٓ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:4:deficiency-and-human-contrast","source_type":"word_analysis","support_id":"sup_db3b98010d6546828484","text":"{\"blocking_evidence\":null,\"headline\":\"human weakness suspended\",\"reader_payoff\":\"The reader notices protection from a paradigmatic human weakness, without importing a different root or making the addressee's retention autonomous.\",\"reason\":\"Rows cite divine non-forgetfulness in 19:64 and Adam's forgetting in 20:115; the local root remains {{ar:ن س ي}} ({{tr:n-s-y}}), so the human-forgetfulness dispute is retained as pressure, not as a replacement root.\",\"representative_source_ids\":[\"QS-a52ec372\",\"QS-f1741f03\",\"MI-30ab2ca0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:4","source_type":"word_analysis","support_id":"sup_eef8406c66ffc7bd0196","text":"{\"gloss_range\":\"Form I imperfect 2ms under negation: you forget, neglect, or let slip; locally objectless because the recited content is supplied by the prior promise\",\"prose\":\"{{ar:تَنسَىٰٓ}} ({{tr:tansā}}) names the vulnerability at the ayah's close and places it under negation. Its hidden 2ms subject is the same addressee marked by the {{ar:كَ}} ({{tr:ka}}) suffix in {{ar:سَنُقْرِئُكَ}} ({{tr:sanuqriʾuka}}): the recipient of caused recitation becomes the protected rememberer. The verb remains semantically transitive but objectless, so the listener must carry the recited content forward as what will not be forgotten or neglected. The {{ar:ن س ي}} ({{tr:n-s-y}}) range includes mental lapse, neglect, and abandoned cast-off things; local context narrows that range to loss or neglect of the caused recitation, not sciatic, postponement, or other remote branches. The simple Form I names ordinary human lapse rather than caused or feigned forgetting, and {{ar:لَا}} ({{tr:lā}}) suspends that process without changing the stem. Ending on this denied verb makes the promise land on the exact threat it cancels, while 87:7 immediately keeps any exception under divine will; set beside 19:64's denial of divine forgetfulness and Adam's forgetting in 20:115, this recitation is protected from paradigmatic human lapse without making the addressee's retention autonomous. The long final {{ar:ىٰٓ}} ({{tr:ā}}) lets the threatened loss linger audibly as suspended non-loss.\",\"root_display\":\"{{ar:ن س ي}} ({{tr:n-s-y}})\",\"root_gloss_range\":\"forgetting, loss of recall, neglect, leaving aside, abandoned forgotten things, and nonlocal branches such as sciatic-vein or postponement terms; the local clause selects negated loss or neglect of the caused recitation\",\"surface_display\":\"{{ar:تَنسَىٰٓ}} ({{tr:tansā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:4:ordinary-human-vulnerability","source_type":"word_analysis","support_id":"sup_fb55dfafcc223dceaa4f","text":"{\"blocking_evidence\":null,\"headline\":\"ordinary lapse, not caused or feigned\",\"reader_payoff\":\"The reader sees ordinary human forgetting named directly, while causative or feigned-forgetting forms remain only contrastive background.\",\"reason\":\"The surface is simple Form I {{ar:تَنسَىٰٓ}} ({{tr:tansā}}), so causative {{ar:نَسَّى}} ({{tr:nassā}}), {{ar:أَنْسَى}} ({{tr:ansā}}), and feigned {{ar:تَنَاسَى}} ({{tr:tanāsā}}) are valid contrasts but not the local stem.\",\"representative_source_ids\":[\"QS-d278a221\",\"QF-20e4483a\",\"QF-e628cde7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:6:4:long-final-sound","source_type":"word_analysis","support_id":"sup_fee6b7cb4df41b18beb6","text":"{\"blocking_evidence\":null,\"headline\":\"long final suspended loss\",\"reader_payoff\":\"The reader can hear the denied loss linger in the long final vowel while remaining grammatically cancelled.\",\"reason\":\"The phonetic rows concern the actual final shape of {{ar:تَنسَىٰٓ}} ({{tr:tansā}}) and its relation to the preceding negation and earlier recitation articulation.\",\"representative_source_ids\":[\"QF-f02d9564\",\"MP-634b4521\",\"QP-a77f8cbf\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"سَنُقْرِئُكَ فَلَا تَنسَىٰٓ","ayah_ref":"87:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001210/B002","root_001501/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001210","role":"Reading, reciting, and teaching another to recite supplies the externally caused vocal transmission.","root":"ق ر ء","source_ref":"87:6","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001501","role":"Loss of recall supplies the failure that the caused recitation is presented as blocking.","root":"ن س ي","source_ref":"87:6","source_word_indices":["3"]}],"changed_reading":{"after":"The speaker will actively make the addressee recite, and that caused transfer establishes protected recall.","before":"The addressee will recite and happen not to forget."},"confidence":"strong","focus_anchor":"The future-marked causative recitation verb addresses a second-person recipient, and fa-la links it directly to the negated forgetting verb.","mechanism":"The speaker does not merely predict the recipient's reading; the causative act installs recitation in the recipient, and the linked negation presents protected recall as its result.","model_id":"baseline_causative_retention"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_causative_retention","source_type":"hft","support_id":"sup_bd293e59b781f5cdb243","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"سَنُقْرِئُكَ فَلَا تَنسَىٰٓ","ayah_ref":"87:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001210/B001","root_001501/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001210","role":"Collecting and gathering recasts recitation as assembly of dispersed units into one repeatable sequence.","root":"ق ر ء","source_ref":"87:6","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001501","role":"Loss of recall threatens the gathered sequence with dispersal and supplies the prevented breakdown.","root":"ن س ي","source_ref":"87:6","source_word_indices":["3"]}],"changed_reading":{"after":"Making recite gathers units into a coherent whole whose internal order is kept from dispersing.","before":"Recitation is a sequence already present in memory."},"confidence":"medium","focus_anchor":"The recitation verb can activate the root's collecting image while the coordinated negation remains anchored in loss of recall.","mechanism":"Recitation gathers discrete sounds or units into an ordered whole; non-forgetting preserves not only items but their joins and recoverable sequence.","model_id":"baseline_gathered_sequence"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_gathered_sequence","source_type":"hft","support_id":"sup_b6518febf92a70fbe9e8","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"سَنُقْرِئُكَ فَلَا تَنسَىٰٓ","ayah_ref":"87:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001210/B011","root_001501/B002"],"payload":{"activation_trace":[{"branch_id":"B011","mapped_root_id":"root_001210","role":"A manner, pattern, and directed course supplies recitation with an ongoing path rather than a single performance.","root":"ق ر ء","source_ref":"87:6","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001501","role":"Leaving or abandoning supplies a volitional and practical dimension to what the negation prevents.","root":"ن س ي","source_ref":"87:6","source_word_indices":["3"]}],"changed_reading":{"after":"The bestowed recitative pattern is also a course that will not be left or neglected.","before":"Forgetting names an accidental cognitive lapse."},"confidence":"medium","focus_anchor":"The focus construction pairs a caused recitative action with n-s-y, whose inventory includes both forgetting and practical abandonment.","mechanism":"The causative recitation establishes a patterned course; the negation can therefore resist leaving or neglecting that course as well as involuntary memory loss.","model_id":"baseline_nonabandonment"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_nonabandonment","source_type":"hft","support_id":"sup_b6f48b85c5b6c28ae31c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"سَنُقْرِئُكَ فَلَا تَنسَىٰٓ","ayah_ref":"87:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001210/B006","root_001501/B002"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001210","role":"The devout or learned reader image supplies an identity and practice that can be formed through caused recitation.","root":"ق ر ء","source_ref":"87:6","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001501","role":"Leaving or neglecting supplies the discontinuity that an enduring reciter identity resists.","root":"ن س ي","source_ref":"87:6","source_word_indices":["3"]}],"changed_reading":{"after":"The promise begins forming a learned devotional reciter whose continuing practice resists neglect.","before":"The promise concerns reliable storage of verbal material."},"confidence":"exploratory","focus_anchor":"The causative q-r-hamza verb acts on the addressee, while one focus-root branch associates the reader with devotion and understanding.","mechanism":"Being made to recite can form a learned, devotional agent; non-abandonment then describes continuity of a reciter's practice rather than storage of words alone.","model_id":"baseline_formed_reciter"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_formed_reciter","source_type":"hft","support_id":"sup_5bc2650d97db231b4003","trust":"legacy_unbound"}]}
</lane_packet_json>
