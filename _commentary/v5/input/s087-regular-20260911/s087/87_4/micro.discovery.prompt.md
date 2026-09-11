# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **87:4**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s087-regular-20260911/s087/87_4/micro.discovery.json` and modify nothing
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
  "ayah_ref": "87:4",
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
{"analysis_context":{"analysis_id":"s087-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"87:4","host_surah":87,"lane_context_refs":[],"ordered_context_refs":["87:0","87:1","87:2","87:3","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, mali ödeme, renk örüntüsü, yara ve öteki özelleşmiş kullanımları kapsamaz.","branch_kind":"bare","branch_ref":"root_000400/B001","candidate_links":[{"candidate_id":"cand_b1792cbc9527ff8f5eee","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","surface_ar":"أَخْرَجَ"}],"gloss":"bir yerden ya da durumdan dışarı çıkma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yerden, kapsayıcıdan veya durumdan dışarıya geçme hareketi gerçekleşir."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın hareket veya durum değişikliği anlamının tamamı için kullanılır.","boundary_detail":"Dal, mali ödeme, renk örüntüsü, yara ve öteki özelleşmiş kullanımları kapsamaz.","branch_image_ar":"النفاذ إلى خارج الشيء","concept_gloss":"bir yerden ya da durumdan dışarı çıkma","contextual_glosses":[{"applicability":"Bir kişinin veya nesnenin bulunduğu yerden ayrıldığı doğal cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yer veya durum dışına geçme hareketini doğal biçimde korur."},"facet_ids":["F001"],"text":"dışarı çıkmak","usage_role":"general"}],"definition":"Bir varlığın bulunduğu yerden, içinde olduğu şeyden veya sürmekte olan bir durumdan dışarıya geçmesidir; içeri girmenin karşıtıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yerden, kapsayıcıdan veya durumdan dışarıya geçme hareketi gerçekleşir."}],"identity_rationale":"Kaynak ifadesi, bir yerden veya durumdan dışarı çıkmayı ve bunun içeri girmenin karşıtı oluşunu açıkça kurar. Geçici dal çerçevesi bu çekirdeği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"dışarı çıktı; bir yerden veya durumdan ayrıldı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"dışarı çıkma; bir durumdan ayrılma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"dışarı çıkan veya ayrılan"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"çıkış yeri veya çıkış yönü"}],"lexicalization_note":"Tanım yalın çıkma anlamıyla sınırlıdır; başka dallardaki kalıplaşmış kullanımlar buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sınırı en iyi açıklayan yakın anlamlı karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu kullanım çıkma eyleminin belirli bir söyleyişine bağlıdır; odak dal ise yer, kapsayıcı ve durum değişikliğini kapsayan yalın ve daha genel çekirdektir.","focus_only":"Odak dal, yerden çıkmanın yanında bir durumdan ayrılmayı ve içeri girme karşıtlığını da kapsar.","gloss":"bir şeyden çıkma","neighbor_only":"Komşu dal, belirli bir kişi öznesiyle bir şeyden çıkmayı anlatan daha dar bir kullanımdır.","neighbor_ref":"root_001158/B004","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir sınırın veya kapsayıcının dışına geçiş vardır."}],"source_phrase_ar":"النفاذ عن الشيء (maqayis)؛ الخروج نقيض الدخول (ayn;jamhara;tahdhib)؛ خرج خروجا برز من مقره أو حاله (mufradat)","source_summary":"Kaynaklar, dışarıya geçme ve içeri girmenin karşıtı olma çekirdeğinde birleşir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"كل بروز أو انفصال عن مقر أو حال، والدخول نقيضه","what_is_not_ar":"الخراج المالي؛ الخرج اللوني؛ الخراج الجسدي"},"support_links":["sup_3ea9a34b16fb0c95f507"]},{"boundary":"Yalın çıkma bu dalın çekirdeği değildir; burada bir etken başka bir şeyi çıkarır, elde eder veya yetiştirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000400/B002","candidate_links":[{"candidate_id":"cand_c3495edd9c461a37178b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","surface_ar":"أَخْرَجَ"}],"gloss":"bir şeyi çıkarma, elde etme veya yetiştirme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir etken, başka bir varlığı bulunduğu yerden çıkarır veya görünür duruma getirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlem, saklı ya da örtük bir şeyi çıkarıp elde etme biçiminde gerçekleşebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eğitimde kişi bilgisizlikten çıkarılarak yetişmiş bir duruma geçirilir."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ettirgen çekirdeği ve kanıtlanan işlem ile eğitim uzantılarını birlikte temsil eder.","boundary_detail":"Yalın çıkma bu dalın çekirdeği değildir; burada bir etken başka bir şeyi çıkarır, elde eder veya yetiştirir.","branch_image_ar":"إخراج الشيء من خفائه","concept_gloss":"bir şeyi çıkarma, elde etme veya yetiştirme","contextual_glosses":[{"applicability":"Bir nesnenin dışarı çıkarıldığı veya görünür kılındığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başka bir varlığı görünür duruma getiren ettirgen işlemi korur."},"facet_ids":["F001"],"text":"ortaya çıkarmak","usage_role":"contextual"},{"applicability":"Saklı veya örtük bir sonucun işlem yoluyla elde edildiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çıkarma yoluyla bir sonuca ulaşma işlemini bütünüyle korur."},"facet_ids":["F002"],"text":"çıkarıp elde etmek","usage_role":"contextual"},{"applicability":"Bir kişinin eğitimle bilgisizlikten çıkarıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eğitim veren etkeni ve öğrenende oluşan durum değişikliğini korur."},"facet_ids":["F003"],"text":"eğitip yetiştirmek","usage_role":"contextual"}],"definition":"Bir etkenin bir şeyi bulunduğu yerden dışarı çıkarması, görünür kılması veya işleyerek elde etmesidir. Eğitim bağlamında kişiyi bilgisizlik sınırından çıkarıp yetiştirmeyi de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir etken, başka bir varlığı bulunduğu yerden çıkarır veya görünür duruma getirir."},{"facet_id":"F002","role":"specialization","statement":"İşlem, saklı ya da örtük bir şeyi çıkarıp elde etme biçiminde gerçekleşebilir."},{"facet_id":"F003","role":"extension","statement":"Eğitimde kişi bilgisizlikten çıkarılarak yetişmiş bir duruma geçirilir."}],"identity_rationale":"Kaynak ifadesi yalnızca gizlenmiş bir şeyi görünür kılmayı değil, bir şeyi dışarı çıkarmayı, çıkarıp elde etmeyi ve eğitimle bilgisizlik sınırından geçirmeyi de içerir. Bu nedenle dal, gizlilikle sınırlı olmayan ettirgen ve elde edici bir süreç olarak yeniden çerçevelenmiştir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"dışarı çıkardı veya ortaya koydu"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"nesneleri dışarı çıkarma veya görünür kılma"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"çıkarıp elde etti"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"işleyip ortaya çıkarma veya çeşitlere ayırma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"eğitim görüp yetişti"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"birinin elinde yetişmiş öğrenci"}],"lexicalization_note":"Tanım, ettirgen çıkarma ile kalıba bağlı elde etme ve eğitim kullanımlarını ayırır; bunları yalın çıkma anlamında birleştirmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; görünür kılma ile çıkarıp elde etme arasındaki sınır en yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşunun merkezi görünürlüktür; odak dalda ise yerden çıkarma, işlemle elde etme ve kişiyi bilgisizlikten çıkarma gibi görünürlükten daha geniş ettirgen geçişler bulunur.","focus_only":"Odak dal çıkarıp elde etmeyi ve eğitimle yetiştirmeyi de kapsar.","gloss":"gizlilikten sonra belirme veya gösterme","neighbor_only":"Komşu dal, bir şeyin gizlilikten sonra görünür olması ile görünür kılınmasına odaklanır.","neighbor_ref":"root_000097/B001","relation_type":"near_synonym","shared_zone":"İki dal da görünür olmayan bir şeyin ortaya gelmesini veya getirilmesini içerebilir."}],"source_phrase_ar":"اخترجت الرجل واستخرجته سواء (ayn)؛ الاستخراج كالاستنباط (sihah)؛ الإخراج أكثر ما يقال في الأعيان (mufradat)؛ خريج فلان كأنه أخرجه من حد الجهل (maqayis)","source_summary":"Ortak çerçeve, bir şeyi dışarı çıkarma veya elde etme işlemidir; insan eğitimindeki kullanım bu geçişi bilgisizlikten yetişmişliğe taşır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"إخراج الشيء أو استخراجه أو تخريجه، ومنه إظهار الأعيان وإخراج المتعلم من الجهل","what_is_not_ar":"الخروج اللازم؛ الخراج المالي؛ الخرج اللوني"},"support_links":["sup_1f012d8ae1609f960d2a"]},{"boundary":"Dal, fiziksel çıkışı değil; ödeme, yükümlülük, getiri ve gider olarak hesaplanan mali değeri anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000400/B003","candidate_links":[{"candidate_id":"cand_88ed936fcdded8d3cf72","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","surface_ar":"أَخْرَجَ"}],"gloss":"düzenli mali yükümlülük, getiri veya gider","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yükümlü tarafından belirli ölçü veya döneme göre çıkarılan mali değer söz konusudur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Mali değer bazı kullanımlarda ürün getirisi, bazı kullanımlarda gelirin karşıtı olan giderdir."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın ödeme, ürün getirisi ve gelir karşıtı gider kapsamını birlikte temsil eder.","boundary_detail":"Dal, fiziksel çıkışı değil; ödeme, yükümlülük, getiri ve gider olarak hesaplanan mali değeri anlatır.","branch_image_ar":"مال يخرج على جهة معلومة","concept_gloss":"düzenli mali yükümlülük, getiri veya gider","contextual_glosses":[{"applicability":"Belirli miktarda ve dönemde ödenen mali yükümlülük bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ödeme niteliğini, yükümlüyü ve düzenli ölçüyü korur."},"facet_ids":["F001"],"text":"vergi veya düzenli ödeme","usage_role":"contextual"},{"applicability":"Mali değerin getiri ya da gelirin karşı kalemi olarak geçtiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Getiri ile gider arasındaki bağlama bağlı yön değişimini korur."},"facet_ids":["F002"],"text":"ürün getirisi veya gider","usage_role":"contextual"}],"definition":"Belirli bir dönem veya ölçüye göre ödenen para, ürün ya da mali yükümlülüktür. Bağlama göre elde edilen ürün getirisi veya gelirin karşısındaki gideri de gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yükümlü tarafından belirli ölçü veya döneme göre çıkarılan mali değer söz konusudur."},{"facet_id":"F002","role":"source_variant","statement":"Mali değer bazı kullanımlarda ürün getirisi, bazı kullanımlarda gelirin karşıtı olan giderdir."}],"identity_rationale":"Kaynak ifadesi, verenin çıkardığı para, belirli dönem ve miktara bağlı mali yük, ürün getirisi ve gelirin karşısındaki gider anlamlarını birlikte destekler. Geçici çerçeve bu mali alanı doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"mali ödeme, vergi veya ürün getirisi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ürün getirisi, vergi veya zorunlu ödeme"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"hizmetindeki kişiyle aylık ödeme üzerinde anlaştı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"efendisine düzenli ödeme yapmakla yükümlü köle"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sorumluluk karşılığında elde edilen ürün getirisi"}],"lexicalization_note":"Mali çekirdek korunur; yalın ödeme ve gelir kullanımları, sözleşmeye bağlı özel ödeme kalıplarından ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel vergi ile genel mali yük ve getiri alanı arasındaki karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu kavram ödeyen topluluğu ve hukuki nedeni bakımından özeldir; odak dal ise ödeme, getiri ve gider yönleri bulunan daha geniş bir mali söz varlığı alanıdır.","focus_only":"Odak dal ürün getirisini, genel mali gideri ve farklı türde düzenli ödemeleri kapsar.","gloss":"belirli bir topluluğa yüklenen vergi","neighbor_only":"Komşu dal, belirli bir topluluktan hukuki statüsü nedeniyle alınan özel mali yükümlülüktür.","neighbor_ref":"root_000244/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalda da yükümlüden alınan ve hukukça ya da düzenle belirlenen mali ödeme bulunur."}],"source_phrase_ar":"الخراج والخرج الإتاوة لأنه مال يخرجه المعطي (maqayis)؛ الخرج والخراج ما يخرج من المال في السنة بقدر معلوم (ayn;tahdhib)؛ الخراج الغلة (tahdhib)؛ الخرج بإزاء الدخل (mufradat)","source_summary":"Kaynakların ortak mali alanı, ölçülü bir ödeme veya yükümlülük ile ürün getirisi ve gider yönlerini bir arada içerir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"ما يخرجه المرء من مال أو غلة أو ضريبة أو وظيفة معلومة","what_is_not_ar":"الخروج المكاني؛ الخراج الجسدي؛ الخرج الوعاء"},"support_links":["sup_acb68e249e6d79d8b78f"]},{"boundary":"Dal yalnızca bedensel oluşumu kapsar; mali ödeme ve yerden çıkma anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000400/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","surface_ar":"أَخْرَجَ"}],"gloss":"bedende çıkan irinli şişlik veya yara","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Beden yüzeyinde şişlik, çıban veya yara biçiminde dışa vuran bir oluşum bulunur."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ya da hayvanda dışa vuran çıban, şişlik ve yara türlerinin ortak adı olarak uygundur.","boundary_detail":"Dal yalnızca bedensel oluşumu kapsar; mali ödeme ve yerden çıkma anlamları dışarıda kalır.","branch_image_ar":"قُرْح يخرج في الجسد","concept_gloss":"bedende çıkan irinli şişlik veya yara","contextual_glosses":[{"applicability":"Oluşumun şiş ve irinli bir beden lezyonu olduğu bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Şişlik biçimini, bedensel yeri ve irinli oluşum niteliğini korur."},"facet_ids":["F001"],"text":"irinli şişlik","usage_role":"contextual"}],"definition":"İnsan veya hayvan bedeninde kendiliğinden beliren, şişlik, çıban ya da irinli yara niteliğindeki oluşumdur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Beden yüzeyinde şişlik, çıban veya yara biçiminde dışa vuran bir oluşum bulunur."}],"identity_rationale":"Kaynak ifadesi, insan veya hayvan bedeninde kendiliğinden beliren şişlik, irinli yara ve benzeri oluşumları açıkça tanımlar. Geçici dal kimliği bu bedensel çekirdekle uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bedende çıkan şişlik, çıban veya irinli yara"}],"lexicalization_note":"Tanım yalın bedensel lezyon anlamıyla sınırlıdır ve başka dallardaki mecazi çıkışları içermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; belirli kabarcık ile geniş lezyon sınıfı arasındaki sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu, görünüşü ve hastalık türü belirlenmiş dar bir kabarcıktır; odak dal ise şişlikten irinli yaraya uzanan daha geniş bir bedensel oluşumdur.","focus_only":"Odak dal farklı büyüklük ve biçimlerdeki şişlik, çıban ve yaraları kapsar.","gloss":"mercimek tanesi biçiminde hastalık kabarcığı","neighbor_only":"Komşu dal mercimek tanesine benzeyen ve salgın hastalık türü sayılan belirli bir kabarcıktır.","neighbor_ref":"root_000990/B002","relation_type":"near_neighbor","shared_zone":"Her ikisi de bedende dışa vuran kabarık bir lezyonu gösterebilir."}],"source_phrase_ar":"الخراج بالجسد (maqayis)؛ الخراج ورم وقرح يخرج من ذاته (ayn)؛ ما خرج على الجسد من دمل ونحوه (jamhara)؛ ما يخرج في البدن من القروح (sihah)؛ ورم وقرح يخرج بدابة أو غيرها من الحيوان (tahdhib)","source_summary":"Kaynaklar, insan ve hayvan bedeninde beliren şişlik veya irinli yara anlamında birleşir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"الدمل والورم والقرح الخارج في الجسد أو الحيوان","what_is_not_ar":"الخراج المالي؛ الخروج من مكان؛ الخرج اللوني"},"support_links":[]},{"boundary":"Dal bulutun belirmesine bağlıdır; göğün açılması yalnızca ilgili sözcük biriminin ayrı karşılığında gösterilir.","branch_kind":"collocation","branch_ref":"root_000400/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","surface_ar":"أَخْرَجَ"}],"gloss":"bulutun ilk kez oluşup belirmesi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bulut, oluşumunun başlangıç evresinde görünür hale gelir."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bulutun doğuş ve ilk görünme evresini anlatan kalıba bağlı kullanım için geçerlidir.","boundary_detail":"Dal bulutun belirmesine bağlıdır; göğün açılması yalnızca ilgili sözcük biriminin ayrı karşılığında gösterilir.","branch_image_ar":"ظهور السحاب وانكشاف السماء","concept_gloss":"bulutun ilk kez oluşup belirmesi","contextual_glosses":[{"applicability":"Gökyüzünde yeni bulutların oluşmaya başladığını anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bulutun ilk oluşumunu ve görünür hale gelişini korur."},"facet_ids":["F001"],"text":"bulut belirmeye başladı","usage_role":"contextual"}],"definition":"Bulutun ilk kez oluşmaya başlaması ve gökyüzünde belirmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bulut, oluşumunun başlangıç evresinde görünür hale gelir."}],"identity_rationale":"Yetkili dal iddiası, bulutun ilk kez oluşup görünmeye başlamasını destekler; göğün buluttan arınması bu iddianın parçası değildir. Bu ikinci anlam yalnızca ayrı bir sözcük biriminde bulunduğundan dal tanımına taşınmamıştır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bulut oluşmaya veya belirmeye başladı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"gökyüzü bulutlandıktan sonra açıldı"}],"lexicalization_note":"Tanım yalnızca bulut öznesiyle kurulan belirme kalıbını kapsar ve bunu genel bir yalın çıkma anlamına genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bulutun belirmesi ile dağılması arasındaki karşıt süreç en açıklayıcı sınırdır.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal bulutluluğun başlangıç yönünü, komşu ise bulutluluğun ve yağışın sona erme yönünü işaretler; aynı hava durumu ekseninde karşıt aşamalardır.","focus_only":"Odak dal bulutun oluşup görünmeye başlamasını anlatır.","gloss":"bulutun dağılması ve yağışın kesilmesi","neighbor_only":"Komşu dal bulutun dağılmasını, yıldızların görünmesini veya yağışın kesilmesini anlatır.","neighbor_ref":"root_001475/B007","relation_type":"polarity_pair","shared_zone":"İki dal da gökyüzündeki bulutluluk durumunun değişmesini konu alır."}],"source_phrase_ar":"الخروج خروج السحابة (maqayis)؛ الخروج السحاب أول ما يبدأ (ayn)؛ السحاب أول ما ينشأ (sihah)؛ أول ما ينشأ السحاب فهو نشء وقد خرج له خروج حسن (tahdhib)؛ الخرج أيضا من السحاب (mufradat)","source_summary":"Kaynaklar, bulutun oluşumunun ilk aşamasında belirmesi anlamında birleşir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"نشوء السحاب وخروجه، وصحو السماء بعد الإغام","what_is_not_ar":"الخروج من بيت أو بلد؛ الخراج المالي؛ الخرج اللوني"},"support_links":[]},{"boundary":"Dal fiziksel çıkışı anlatmaz; öz kazanımla öne çıkma ve siyasal itaatten ayrılma yüzleri ayrı tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000400/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","surface_ar":"أَخْرَجَ"}],"gloss":"yerleşik konumdan ayrılarak öne çıkma veya itaatten kopma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, atalarından gelen bir üstünlük olmadan kendi değeriyle seçkinleşir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"At, seçkin bir soydan gelmediği halde üstün koşu niteliği gösterir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Topluluk, yöneticinin buyruğuna bağlı kalmayıp itaat düzeninin dışına çıkar."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıtsal ölçüyü aşan seçkinleşme ile siyasal bağlılıktan ayrılma yüzlerini birlikte temsil eder.","boundary_detail":"Dal fiziksel çıkışı anlatmaz; öz kazanımla öne çıkma ve siyasal itaatten ayrılma yüzleri ayrı tutulmalıdır.","branch_image_ar":"خروج عن الأصل أو الطاعة","concept_gloss":"yerleşik konumdan ayrılarak öne çıkma veya itaatten kopma","contextual_glosses":[{"applicability":"Kalıtsal bir üstünlüğü olmadan kendi yeteneğiyle öne çıkan kişi için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalıtsal dayanak yokluğunu ve kişinin kendi niteliğiyle yükselmesini korur."},"facet_ids":["F001"],"text":"kendi değeriyle seçkinleşen","usage_role":"contextual"},{"applicability":"Bir topluluğun yöneticinin buyruğunu terk ettiği siyasal bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluk katılımcısını ve yönetsel itaatten ayrılma ilişkisini korur."},"facet_ids":["F003"],"text":"itaatten ayrılan topluluk","usage_role":"contextual"}],"definition":"Kalıtsal bir üstünlüğe dayanmadan kendi niteliğiyle benzerlerinden ayrılıp öne çıkmayı anlatır. Başka bir kullanımda, bir topluluğun yöneticinin itaatinden ayrılmasını belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, atalarından gelen bir üstünlük olmadan kendi değeriyle seçkinleşir."},{"facet_id":"F002","role":"example","statement":"At, seçkin bir soydan gelmediği halde üstün koşu niteliği gösterir."},{"facet_id":"F003","role":"extension","statement":"Topluluk, yöneticinin buyruğuna bağlı kalmayıp itaat düzeninin dışına çıkar."}],"identity_rationale":"Kaynak ifadesi, kalıtsal üstünlüğü olmadan kendi değeriyle öne çıkan kişi ve at ile yöneticinin itaatinden ayrılan topluluğu aynı dalda toplar. Bunlar ortak bir yerleşik sınırdan ayrılma görüntüsünü paylaşsa da övgü ve itaatsizlik anlamları birbirine indirgenemez.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kendi değeriyle seçkinleşen kimse"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"soyu seçkin olmadığı halde üstün çıkan at"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yöneticinin itaatinden ayrılan topluluk"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"birinin yeteneğinin ve iş bilirliğinin ortaya çıkması"}],"lexicalization_note":"Kişi, at ve toplulukla kurulan özel kullanımlar ayrı yüzlerdir; bunlardan genel bir yalın çıkma anlamı türetilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; itaatten ayrılma yüzünü taşkın başkaldırıdan ayıran karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal itaatsizliğin kibirli ve taşkın tutumuna odaklanır; odak dalın siyasal yüzü ayrılma ilişkisini adlandırır ve ayrıca övgü bildiren seçkinleşme yüzleri vardır.","focus_only":"Odak dal, itaatten ayrılmanın yanında kalıtsal dayanak olmadan seçkinleşmeyi de kapsar.","gloss":"büyüklük taslayarak itaatten çıkma","neighbor_only":"Komşu dalda itaatsizlik, büyüklük taslama ve sınırı aşan başkaldırı niteliği taşır.","neighbor_ref":"root_000981/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kabul edilen bir otoriteye bağlılığın terk edilmesi bulunabilir."}],"source_phrase_ar":"الخارجي الرجل المسود بنفسه من غير أن يكون له قديم (maqayis)؛ الخارجي الذي لم يكن له شرف في آبائه فيخرج ويشرف بنفسه (ayn)؛ فرس خارجي إذا خرج جوادا بين مقرفين (jamhara)؛ الخارجية من الخيل التي ليس لها عرق في الجودة فتخرج سوابق (tahdhib)؛ الخوارج خارجين عن طاعة الإمام (mufradat)","source_summary":"Toplu kanıt, kalıtsal ölçüyü kendi niteliğiyle aşma ile siyasal itaatten ayrılmayı ortak bir sınır dışına çıkma görüntüsü altında birleştirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"من يخرج عن مرتبة أصله أو جماعته، مدحا بالشرف الذاتي أو السبق، أو ذما بالخروج على الطاعة","what_is_not_ar":"مجرد الخروج المكاني؛ الخرج اللوني؛ الخراج المالي"},"support_links":[]},{"boundary":"Renk karşıtlığı çekirdektir; bitki ve yazı örnekleri aynı yer yer değişme örüntüsünün kalıba bağlı uzantılarıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000400/B007","candidate_links":[{"candidate_id":"cand_fbae4d8cbb4b413143af","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","surface_ar":"أَخْرَجَ"}],"gloss":"iki renkli ya da yer yer kesintili görünüm","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tek bir yüzeyde iki farklı renk, özellikle siyah ve beyaz, birlikte görünür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bitkili ve çıplak ya da yazılı ve boş alanlar yüzey üzerinde kesintili biçimde dağılır."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Renk karşıtlığını ve farklı dolulukta alanların düzensiz dağılımını birlikte karşılar.","boundary_detail":"Renk karşıtlığı çekirdektir; bitki ve yazı örnekleri aynı yer yer değişme örüntüsünün kalıba bağlı uzantılarıdır.","branch_image_ar":"اختلاف لونين في الشيء","concept_gloss":"iki renkli ya da yer yer kesintili görünüm","contextual_glosses":[{"applicability":"Hayvan veya nesne yüzeyinde iki belirgin rengin birlikte bulunduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aynı varlıkta iki ayrı rengin birlikte bulunmasını korur."},"facet_ids":["F001"],"text":"iki renkli","usage_role":"contextual"},{"applicability":"Bitki, yazı veya benzeri bir kaplamanın bazı yerlerde bulunup bazılarında bulunmadığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dolu ve boş alanların kesintili biçimde dağılmasını korur."},"facet_ids":["F002"],"text":"yer yer boşluklu","usage_role":"contextual"}],"definition":"Bir şeyde iki rengin veya birbirinden farklı görünüşteki alanların yer yer bulunmasıdır. Arazi ve yazı gibi bağlamlarda, dolu ile boş bölümlerin kesintili dağılımı olarak gerçekleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tek bir yüzeyde iki farklı renk, özellikle siyah ve beyaz, birlikte görünür."},{"facet_id":"F002","role":"extension","statement":"Bitkili ve çıplak ya da yazılı ve boş alanlar yüzey üzerinde kesintili biçimde dağılır."}],"identity_rationale":"Kaynak ifadesi iki rengin bir aradalığını, siyahın beyaza baskınlığını, bitkinin yer yer çıkmasını ve yazıda boş bırakılan bölümleri destekler. Dalın çekirdeği yalnızca iki renk değil, dolu ile boş veya farklı görünüşlü alanların kesintili dağılımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir işi çeşitlendirme veya yer yer farklılaştırma"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"iki renkli veya kesintili görünüm"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"siyahı beyazından çok olan iki renkli"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"iki renkli dişi hayvan veya iki renkli yer"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bitkisi yer yer çıkan arazi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"otlağın bir bölümünü yiyip bir bölümünü bıraktı"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"yazı yüzeyinde bazı yerleri boş bıraktı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"verimli ve verimsiz yerleri bir arada bulunan yıl"}],"lexicalization_note":"Yalın iki renkli görünüm ile arazi, otlak, yazı ve yıl kalıplarındaki kesintili dağılım açıkça ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; iki renk çekirdeğindeki en yakın sınır karşılaştırması yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Renkli varlıklar bakımından yakın anlamlıdırlar; odak dal yüzeydeki kesintili doluluk örüntüsüne uzanırken komşu dal karma hayvan topluluklarına uzanır.","focus_only":"Odak dal, renklerin yanında bitkili ve çıplak ya da yazılı ve boş alanların kesintili dağılımını da kapsar.","gloss":"siyah beyaz veya iki renkli olma","neighbor_only":"Komşu dal iki renkli hayvan ve nesnelerin yanında iki farklı hayvan türünden oluşan karma sürüyü de kapsar.","neighbor_ref":"root_001003/B004","relation_type":"near_synonym","shared_zone":"Her iki dalın merkezinde aynı varlıkta siyah ile beyazın ya da iki rengin birlikte bulunması vardır."}],"source_phrase_ar":"الخرج لونان بين سواد وبياض (maqayis)؛ الأخرج لون سواده أكثر من بياضه (ayn;tahdhib)؛ أرض مخرجة نبتها في مكان دون مكان (ayn;sihah;tahdhib;mufradat)؛ خرج الغلام لوحه إذا ترك فيه مواضع لم يكتبها (tahdhib)","source_summary":"Kaynaklar iki renkli görünümü, baskın siyahı ve arazi ile yazıdaki yer yer dolu veya boş örüntüyü birlikte destekler.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"اختلاف لونين أو تقطع المواضع بين بياض وخضرة أو سواد وبياض، وما شبه به من كتابة وعمل وعام","what_is_not_ar":"الخروج من مكان؛ الخراج المالي؛ الخراج الجسدي"},"support_links":["sup_ea2ac7faee43e4ff417d"]},{"boundary":"Dal yalnızca dişi devenin doğuştan erkek deve yapısı göstermesidir; üreme isteği veya genel cinsiyet ayrımı değildir.","branch_kind":"collocation","branch_ref":"root_000400/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","surface_ar":"أَخْرَجَ"}],"gloss":"erkek deve yapısında doğmuş dişi deve","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi deve, yaratılışı bakımından erkek devenin beden biçimini gösterir."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca dişi devenin doğuştan gelen beden biçimini niteleyen özel kullanım için geçerlidir.","boundary_detail":"Dal yalnızca dişi devenin doğuştan erkek deve yapısı göstermesidir; üreme isteği veya genel cinsiyet ayrımı değildir.","branch_image_ar":"خروج الخلقة عن نوعها","concept_gloss":"erkek deve yapısında doğmuş dişi deve","contextual_glosses":[{"applicability":"Bir dişi devenin beden kuruluşunun erkek deveye benzediği anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişi özneyi ve erkek deveye benzeyen beden yapısını korur."},"facet_ids":["F001"],"text":"erkek yapılı dişi deve","usage_role":"contextual"}],"definition":"Dişi bir devenin doğuştan erkek devenin beden yapısına sahip olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi deve, yaratılışı bakımından erkek devenin beden biçimini gösterir."}],"identity_rationale":"Kaynak ifadesi, dişi devenin erkek devenin beden yapısında doğmuş olmasını doğrudan belirtir. Geçici dal kimliği bu dar hayvan niteliğini eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"erkek deve yapısında doğmuş dişi deve"}],"lexicalization_note":"Tanım dişi deveyle kurulan özel niteleme kalıbına bağlıdır ve genel bir biçim değişikliğine genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; anatomik yapı ile üreme durumu arasındaki alan ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortaklık yalnızca hayvan ve cinsiyet alanındadır; odak anatomik yapı, komşu ise geçici üreme isteğidir.","focus_only":"Odak dal dişi devenin doğuştan gelen beden yapısını niteler.","gloss":"dişi devenin erkeği istemesi","neighbor_only":"Komşu dal dişi devenin çiftleşme isteğini ve erkeğe yönelmesini anlatır.","neighbor_ref":"root_000009/B012","relation_type":"same_field","shared_zone":"İki dal da dişi deveye özgü bir durumu anlatır."}],"source_phrase_ar":"ناقة مخترجة إذا خرجت على خلقة الجمل (maqayis;ayn;sihah)؛ المخترجة أنها جبلت على خلقة الجمل (tahdhib)","source_summary":"Kaynaklar, dişi devenin erkek deve yapısında doğması biçimindeki dar nitelemede birleşir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"الناقة المخلوقة على خلقة الجمل","what_is_not_ar":"الخروج المكاني؛ الخرج اللوني؛ الخارجي في الشرف أو الطاعة"},"support_links":[]},{"boundary":"Dal bir taşıma kabını anlatır; mali yük, yara ve iki renkli görünüm anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000400/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","surface_ar":"أَخْرَجَ"}],"gloss":"iki gözlü taşıma torbası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kap, taşımaya yarayan torba biçimindedir ve iki ayrı bölmesi bulunur."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki bölmeli torba biçimindeki somut taşıma kabının genel karşılığıdır.","boundary_detail":"Dal bir taşıma kabını anlatır; mali yük, yara ve iki renkli görünüm anlamları dışarıda kalır.","branch_image_ar":"خرج الوعاء ذو الأونين","concept_gloss":"iki gözlü taşıma torbası","contextual_glosses":[{"applicability":"Yük hayvanında veya elde eşya taşımaya yarayan iki bölmeli torba için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşıma işlevini ve torbanın iki ayrı gözünü korur."},"facet_ids":["F001"],"text":"iki gözlü yük torbası","usage_role":"general"}],"definition":"Yük veya eşya taşımak için kullanılan, iki ayrı gözü bulunan torba biçiminde bir kaptır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kap, taşımaya yarayan torba biçimindedir ve iki ayrı bölmesi bulunur."}],"identity_rationale":"Kaynak ifadesi, iki bölmeli bir taşıma torbasını ve onun sayı biçimini açıkça tanımlar. Geçici dal kimliği bu somut kap anlamıyla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"iki gözlü taşıma torbası"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"iki gözlü taşıma torbaları"}],"lexicalization_note":"Tanım yalın kap adına bağlıdır ve başka dallardaki eylem ya da nitelik anlamlarını içermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel torba ile iki bölmeli taşıma kabı arasındaki sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu genel bir torbayı anlatır; odak dal ise yapısal olarak iki bölmeli olan belirli taşıma torbasıdır.","focus_only":"Odak dalın ayırt edici özelliği iki ayrı göze sahip olmasıdır.","gloss":"eşya konan torba","neighbor_only":"Komşu dal, içine istenen şeyin konduğu genel bir torba veya kılıftır.","neighbor_ref":"root_000403/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da içine eşya konup taşınabilen esnek bir kaptır."}],"source_phrase_ar":"الخرج والخرجة جمعه جوالق ذو أونين (ayn)؛ الخرج من الأوعية معروف والجمع خرجة (sihah)؛ الخرج هذا الوعاء ثلاثة خرجة وهو جوالق ذو أونين (tahdhib)","source_summary":"Kaynaklar, iki gözlü torba biçimindeki taşıma kabı ve onun çoğul kullanımı üzerinde birleşir.","sources":["AY","SI","TA"],"what_is_ar":"الوعاء الجوالق ذو الأونين","what_is_not_ar":"الإتاوة؛ الدمل؛ اختلاف اللونين"},"support_links":[]},{"boundary":"Dal geleneksel oyunun kimliğini taşır; ayrıntılı oyun düzeni dal tanımının kurucu parçası sayılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000400/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","surface_ar":"أَخْرَجَ"}],"gloss":"özel çağrılı geleneksel çocuk oyunu","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Oyun, erkek çocuklar arasında oynanır ve kendine özgü yinelenen bir çağrıyla tanınır."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kuralları ayrıntılandırılmayan, erkek çocuklara özgü geleneksel oyunun kısa karşılığıdır.","boundary_detail":"Dal geleneksel oyunun kimliğini taşır; ayrıntılı oyun düzeni dal tanımının kurucu parçası sayılmaz.","branch_image_ar":"لعبة إخراج ما في اليد","concept_gloss":"özel çağrılı geleneksel çocuk oyunu","contextual_glosses":[{"applicability":"Oyunun özgün adı yerine kaynakça desteklenen genel açıklama gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çocuk oyunu oluşunu ve ayırt edici çağrı unsurunu korur."},"facet_ids":["F001"],"text":"çağrıyla oynanan çocuk oyunu","usage_role":"explanatory"}],"definition":"Erkek çocukların oynadığı ve oyun sırasında yinelenen özel bir çağrıyla tanınan geleneksel bir oyundur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Oyun, erkek çocuklar arasında oynanır ve kendine özgü yinelenen bir çağrıyla tanınır."}],"identity_rationale":"Dal iddiası, erkek çocukların oynadığı ve belirli bir çağrıyla anılan geleneksel bir oyunu doğrular; ancak oyunun kuralları dal düzeyindeki kaynak ifadesinde açıklanmaz. Eldekini çıkartma açıklaması bu nedenle yalnızca ilgili sözcük biriminin karşılığında korunmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"erkek çocukların oynadığı geleneksel oyun"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"çocukların oynadığı geleneksel oyun"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"oyunda eldekini çıkarmayı isteyen çağrı"}],"lexicalization_note":"Oyun adları ile oyun içi çağrı ayrı sözcük birimleridir; bunlardan yalın çıkma anlamı üretilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; komşu oyun kartları kuralları açıklamadığından güvenilir bir anlam sınırı yayımlanmadı.","source_phrase_ar":"الخريج لعبة لفتيان العرب يقال فيها خراج خراج (maqayis;sihah)؛ الخراج والخريج مخارجة لعبة لفتيان العرب (ayn)؛ الخراج لعبة يلعب بها الصبيان (jamhara)؛ خراج اسم لعبة لهم معروفة (tahdhib)","source_summary":"Kaynaklar, erkek çocukların oynadığı ve özel bir oyun çağrısıyla anılan geleneksel oyun kimliğinde birleşir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"لعبة الخراج والخريج التي يطلب فيها إخراج ما في اليد","what_is_not_ar":"الخراج المالي؛ الخراج الجسدي؛ الخروج المكاني"},"support_links":[]},{"boundary":"Dal yalnızca uyak yapısındaki belirli son sesi anlatır; genel çıkma eylemiyle ilişkili değildir.","branch_kind":"bare","branch_ref":"root_000400/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","surface_ar":"أَخْرَجَ"}],"gloss":"uyakta bağlantı sesinden sonraki elif harfi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Elif harfi, uyak dizisinde bağlantı sesinin hemen ardından yer alır."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Şiir ölçüsü ve uyak çözümlemesinde bağlantı sesini izleyen elif için kullanılır.","boundary_detail":"Dal yalnızca uyak yapısındaki belirli son sesi anlatır; genel çıkma eylemiyle ilişkili değildir.","branch_image_ar":"ألف الخروج بعد الصلة","concept_gloss":"uyakta bağlantı sesinden sonraki elif harfi","contextual_glosses":[{"applicability":"Teknik terimin elif harfi oluşu ve uyaktaki yeri kısa biçimde açıklanırken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uyak alanını, elif harfini ve bağlantı sesinin ardından gelme koşulunu korur."},"facet_ids":["F001"],"text":"uyak sonunda bağlantı sesini izleyen elif","usage_role":"explanatory"}],"definition":"Şiir uyağında bağlantı sesinden sonra gelen elif harfidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Elif harfi, uyak dizisinde bağlantı sesinin hemen ardından yer alır."}],"identity_rationale":"Kaynak ifadesi, uyakta bağlantı sesinden sonra gelen elif harfini açık ve tek bir teknik görevle tanımlar. Geçici dal çerçevesi bu konumu doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"uyakta bağlantı sesinden sonra gelen elif harfi"}],"lexicalization_note":"Tanım yalın bir şiir ve uyak terimine bağlıdır; başka teknik ses konumları buraya katılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; uyak içindeki konumu farklı olan en yakın teknik ses öğesiyle karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak öğe elif harfidir ve bağlantı sesinden sonra gelir; komşu öğe ise uyak harfinden önce bulunur. Ses dizisindeki konumları ve görevleri farklıdır.","focus_only":"Odak dal, bağlantı sesinden sonra gelen elif harfidir.","gloss":"uyak harfinden önceki uzun veya kayıcı ses","neighbor_only":"Komşu dal, uyak harfinden önce bulunan hareketsiz bir uzun veya kayıcı sestir.","neighbor_ref":"root_000556/B006","relation_type":"same_field","shared_zone":"İki dal da şiir uyağında belirli konumu olan ses öğeleridir."}],"source_phrase_ar":"الخروج الألف التي بعد الصلة في القافية (ayn;tahdhib)","source_summary":"Kaynaklar, uyakta bağlantı sesinden sonra gelen elif harfinin teknik adı üzerinde birleşir.","sources":["AY","TA"],"what_is_ar":"ألف الخروج في القافية بعد الصلة","what_is_not_ar":"الخروج المكاني؛ الإخراج؛ الخرج المالي"},"support_links":[]},{"boundary":"Dal tek yanlı vergi veya ödeme değildir; ortak hak sahipleri arasında karşılıklı bölüşme ve tasfiye gerektirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000400/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","surface_ar":"أَخْرَجَ"}],"gloss":"ortak payları karşılıklı bölüşüp tasfiye etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taraflar ortak değer üzerinde karşılıklı katkıda bulunur, bölüşür veya hesaplaşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ortaklar veya mirasçılar malı, alacağı ve payları denkleştirerek ortak ilişkiden ayrılır."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşılıklı katkıdan ortaklık veya miras paylarının anlaşmalı tasfiyesine uzanan çekirdeği karşılar.","boundary_detail":"Dal tek yanlı vergi veya ödeme değildir; ortak hak sahipleri arasında karşılıklı bölüşme ve tasfiye gerektirir.","branch_image_ar":"تخارج الشركاء في النصيب","concept_gloss":"ortak payları karşılıklı bölüşüp tasfiye etme","contextual_glosses":[{"applicability":"Ortakların veya mirasçıların paylarını anlaşmayla ayırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı anlaşmayı, pay ayrımını ve ortak ilişkinin sona ermesini korur."},"facet_ids":["F002"],"text":"paylaşıp ortaklıktan ayrılmak","usage_role":"contextual"},{"applicability":"Tarafların ortak değere katkı verip bunu aralarında paylaştığı genel bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Birden çok tarafı, karşılıklı katkıyı ve bölüşme işlemini korur."},"facet_ids":["F001"],"text":"karşılıklı katkı ve bölüşme","usage_role":"explanatory"}],"definition":"Birden çok hak sahibinin ortak değerleri karşılıklı katkı ve bölüşmeyle düzenlemesidir. Ortaklar veya mirasçılar bakımından pay, mal ve alacakları anlaşarak denkleştirip ortak ilişkiden ayrılmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taraflar ortak değer üzerinde karşılıklı katkıda bulunur, bölüşür veya hesaplaşır."},{"facet_id":"F002","role":"specialization","statement":"Ortaklar veya mirasçılar malı, alacağı ve payları denkleştirerek ortak ilişkiden ayrılır."}],"identity_rationale":"Kaynak ifadesi, karşılıklı katkı ve bölüşme ile ortakların veya mirasçıların mal, alacak ve paylar üzerinde anlaşarak ayrılmasını destekler. Geçici çerçeve bu karşılıklı hesaplaşma alanını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"karşılıklı katkı ve bölüşme"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"ortakların veya mirasçıların paylarını tasfiye etmesi"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"iki ortağın mal ve alacak üzerinde karşılıklı hesaplaşması"}],"lexicalization_note":"Genel karşılıklı katkı ve bölüşme, ortaklık ile miras tasfiyesine bağlı özel kalıplardan ayrı gösterilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ortak ayrışması ile payların karşılıklı tasfiyesi arasındaki sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu daha genel bir ortak ayrışmasıdır; odak dal karşılıklı katkı, miras payı, mal ve alacak gibi belirli tasfiye ilişkilerini birlikte taşır.","focus_only":"Odak dal karşılıklı katkıyı ve ortaklar ya da mirasçılar arasında mal ile alacağın tasfiyesini açıkça kapsar.","gloss":"ortakla ayrışma veya bölüşme","neighbor_only":"Komşu dal, ortak bir işteki ortağın genel olarak ayrılması, paylaştırılması veya eşitlenmesidir.","neighbor_ref":"root_001159/B014","relation_type":"near_synonym","shared_zone":"Her iki dal da ortak bir değer veya ilişki üzerinde tarafların ayrışmasını ve hesaplaşmasını anlatır."}],"source_phrase_ar":"المخارجة المناهدة بالأصابع والتخارج التناهد (sihah)؛ يتخارج الشريكان وأهل الميراث (tahdhib)؛ لا بأس أن يتخارجا يعني العين والدين (tahdhib)","source_summary":"Kaynaklar karşılıklı katkı ve bölüşme çekirdeğini, ortaklar ile mirasçıların mal ve alacak üzerindeki uzlaşmalı tasfiyesine bağlar.","sources":["SI","TA"],"what_is_ar":"تخارج الشركاء أو الورثة، والمخارجة بمعنى المناهدة والمقاسمة","what_is_not_ar":"الخراج المالي المفروض؛ الخروج المكاني؛ لعبة الخراج"},"support_links":[]},{"boundary":"Dal yalnızca atın uzun boyunlu oluşuna bağlı nitelemedir; genel uzunluk veya fiziksel çıkış anlamı değildir.","branch_kind":"non_bare","branch_ref":"root_000400/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","surface_ar":"أَخْرَجَ"}],"gloss":"uzun boyunlu at niteliği","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"At, belirgin biçimde uzun bir boyna sahiptir."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca atın belirgin boyun uzunluğunu anlatan özel nitelemede kullanılır.","boundary_detail":"Dal yalnızca atın uzun boyunlu oluşuna bağlı nitelemedir; genel uzunluk veya fiziksel çıkış anlamı değildir.","branch_image_ar":"عنق خارج يغتال العنان","concept_gloss":"uzun boyunlu at niteliği","contextual_glosses":[{"applicability":"Atın belirgin boyun uzunluğunu açıklayan betimleyici bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Atı ve belirgin boyun uzunluğunu korur."},"facet_ids":["F001"],"text":"uzun boyunlu at","usage_role":"explanatory"}],"definition":"Atın uzun boyunlu oluşunu belirten özel bir niteliktir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"At, belirgin biçimde uzun bir boyna sahiptir."}],"identity_rationale":"Kaynak ifadesi, atın boynunun uzun oluşunu belirli bir at niteliği olarak doğrular; dizginin erişimini aşma ayrıntısı ise yalnızca ilgili sözcük biriminin karşılığında korunur.","lexical_glosses":[{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"uzun boynuyla dizginin erişimini aşan at"}],"lexicalization_note":"Tanım at niteliği olarak sözlükselleşmiş özel kullanıma bağlıdır ve yalın kök anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel at niteliği ile genel uzunluk alanı arasındaki karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak yalnızca atın uzun boyunlu oluşuna bağlı bir niteliktir; komşu ise farklı nesne ve beden ölçülerine yayılan genel uzunluk alanıdır.","focus_only":"Odak dal yalnızca atın belirgin boyun uzunluğunu anlatır.","gloss":"uzunluk, uzaklık ve el erişimi","neighbor_only":"Komşu dal genel uzaklık, boy uzunluğu ve kol uzatılarak ölçülen erişim mesafesini kapsar.","neighbor_ref":"root_000116/B011","relation_type":"same_field","shared_zone":"Her iki dal da belirgin bir uzunluk niteliğini konu alır."}],"source_phrase_ar":"الخروج من صفات الخيل وهو الذي يطول عنقه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tekil tanıklık, uzun boyunlu at niteliğini tanımlar."}],"source_summary":"Dal, at anatomisine bağlı dar bir uzun boyun nitelemesi olarak anlaşılır.","sources":["TA"],"what_is_ar":"الخيل الطويلة الأعناق التي تغتال كل عنان","what_is_not_ar":"الخارجي في الشرف؛ الخرج اللوني؛ الخروج المكاني"},"support_links":[]},{"boundary":"Bu dal, sürüyü koruyup gözetmeyi değil, otlama eylemini, yenilen otu ve otlama yerini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000574/B001","candidate_links":[{"candidate_id":"cand_c3495edd9c461a37178b","lane":"micro"},{"candidate_id":"cand_fbae4d8cbb4b413143af","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَرْعَىٰ","morph_features":"STEM|POS:N|LEM:maroEaY`|ROOT:rEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:4:3:2","qac_word_ref":"87:4:3","surface_ar":"مَرْعَىٰ"}],"gloss":"otlama, ot ve otlak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, hayvanın bitkileri yiyerek otlamasıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemden hareketle hayvanın yediği ot da adlandırılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Otlama yapılan yer ve otlama eyleminin adı da kapsam içindedir."}}],"root_ar":"ر ع ي","root_id":"root_000574","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın eylem, yenilen bitki ve yer katmanlarını birlikte belirtmek gereken genel açıklamalarda kullanılır.","boundary_detail":"Bu dal, sürüyü koruyup gözetmeyi değil, otlama eylemini, yenilen otu ve otlama yerini kapsar.","branch_image_ar":"رعي الكلإ والمرعى","concept_gloss":"otlama, ot ve otlak","contextual_glosses":[{"applicability":"Hayvanın bitki yiyerek beslenmesi eyleminin anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın bitki yiyerek otlaması eylemini tam olarak korur."},"facet_ids":["F001"],"text":"otlamak","usage_role":"general"},{"applicability":"Hayvanın otladığı ve yediği bitkinin adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Otlama sırasında yenilen bitki anlamını korur."},"facet_ids":["F002"],"text":"ot","usage_role":"contextual"},{"applicability":"Hayvanların otladığı yerin adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Otlama yapılan yer anlamını korur."},"facet_ids":["F003"],"text":"otlak","usage_role":"contextual"}],"definition":"Hayvanın bitkileri yiyerek otlamasıdır; ayrıca yenilen otu, otlama yerini ve eylemin adını da belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, hayvanın bitkileri yiyerek otlamasıdır."},{"facet_id":"F002","role":"extension","statement":"Eylemden hareketle hayvanın yediği ot da adlandırılır."},{"facet_id":"F003","role":"extension","statement":"Otlama yapılan yer ve otlama eyleminin adı da kapsam içindedir."}],"identity_rationale":"Kaynak ifadesi otlama eylemini, hayvanın yediği otu ve otlama yerini birlikte gösterir. Geçici çerçeve bu çok katmanlı anlamı doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ot, otlak ve otlama"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"hayvanın otlaması"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"hayvanlar için ot bitirmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"başka hayvanlarla birlikte otlamak"}],"lexicalization_note":"Tanım, otlama eylemini temel alırken adlaşmış ot ve otlak anlamlarını ayrı uzantılar olarak gösterir.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; bitki, bollukta otlama ve sürüyü gözetme ile sınırı en açık gösteren üç karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal eylem, bitki ve yer arasında uzanırken komşu dalın çekirdeği yenilen bitki ve bitki örtüsüdür.","focus_only":"Otlama eylemini ve otlama yerini de kapsar.","gloss":"yenilen ot","neighbor_only":"Yeryüzünde hayvanların yediği bitkiyi adlandırmaya ağırlık verir.","neighbor_ref":"root_000003/B001","relation_type":"near_synonym","shared_zone":"İki dal da hayvanların otlayarak yediği bitki alanında buluşur."},{"boundary_match":"partial","distinction":"Komşu dal rahatlık ve bollukla nitelenmiş özel bir otlamayı anlatır; bu dal ise otlamanın kendisini ve ondan türeyen ot ile yer anlamlarını kapsar.","focus_only":"Otlama eylemini bolluk ya da serbestlik koşulu aramadan belirtir.","gloss":"bollukta otlama","neighbor_only":"Bolluk içinde dilediğince yeme ve geniş otlak koşulunu öne çıkarır.","neighbor_ref":"root_000538/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da hayvanın otlakta beslenmesi vardır."},{"boundary_match":"field_only","distinction":"Bu dal beslenme ve otlak çevresinde kurulur; komşu dal ise bakım, koruma ve yönetme eylemini merkez alır.","focus_only":"Hayvanın yemesi, yediği bitki ve otlama yeri bu dala özgüdür.","gloss":"otlama ve gözetme","neighbor_only":"Hayvanı ya da halkı gözetip koruma sorumluluğu komşu dala özgüdür.","neighbor_ref":"root_000574/B002","relation_type":"same_field","shared_zone":"İki dal da sürü ve çobanlık alanıyla bağlantılıdır."}],"source_phrase_ar":"الرَّعي الكلأ؛ المرعى الرعي والموضع والمصدر (sihah)؛ الرعي مصدر رعى يرعى رعيا الكلأ ونحوه (tahdhib)؛ الرعي ما يرعاه والمرعى موضع الرعي (mufradat)","source_summary":"Kaynakların ortak çerçevesinde anlam, otlama eylemi çevresinde toplanır ve bu eylemden yenilen ota, otlama yerine ve eylem adına uzanır.","sources":["SI","TA","MU"],"what_is_ar":"رعي الماشية والبعير؛ الكلأ الذي يرعى؛ المرعى موضع الرعي وما يرعى","what_is_not_ar":"ليس ولاية الناس ولا مراقبة النجوم ولا إرعاء السمع ولا الارعواء"},"support_links":["sup_1f012d8ae1609f960d2a","sup_ea2ac7faee43e4ff417d"]},{"boundary":"Dal, hayvanın ot yemesini değil, sorumluluk üstlenerek hayvanı veya halkı gözetme, koruma ve yönetmeyi anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000574/B002","candidate_links":[{"candidate_id":"cand_88ed936fcdded8d3cf72","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَرْعَىٰ","morph_features":"STEM|POS:N|LEM:maroEaY`|ROOT:rEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:4:3:2","qac_word_ref":"87:4:3","surface_ar":"مَرْعَىٰ"}],"gloss":"gözetip koruma ve yönetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, sorumluluğu altındaki hayvanları gözetip korumaktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı koruyucu gözetim, yöneticinin halkı yönetmesine genişler."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yönetim uzantısında halk, yöneticinin sorumluluğundaki topluluktur."}}],"root_ar":"ر ع ي","root_id":"root_000574","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem hayvanların korunmasını hem de halkın sorumlulukla yönetilmesini kapsayan genel anlatımlarda kullanılır.","boundary_detail":"Dal, hayvanın ot yemesini değil, sorumluluk üstlenerek hayvanı veya halkı gözetme, koruma ve yönetmeyi anlatır.","branch_image_ar":"حفظ الراعي والرعية","concept_gloss":"gözetip koruma ve yönetme","contextual_glosses":[{"applicability":"Çobanın hayvanların bakım ve güvenliğinden sorumlu olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanları sorumlulukla gözetip koruma çekirdeğini korur."},"facet_ids":["F001"],"text":"sürüyü gözetip korumak","usage_role":"contextual"},{"applicability":"Bir yöneticinin sorumluluğundaki topluluğu yönetmesi ve koruması anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yönetme, koruma ve sorumlu olunan topluluk ilişkisini korur."},"facet_ids":["F002","F003"],"text":"halkı yönetip korumak","usage_role":"contextual"}],"definition":"Bir çobanın hayvanları gözetip koruması; kapsam genişlemesiyle bir yöneticinin halkı yönetip korumasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, sorumluluğu altındaki hayvanları gözetip korumaktır."},{"facet_id":"F002","role":"extension","statement":"Aynı koruyucu gözetim, yöneticinin halkı yönetmesine genişler."},{"facet_id":"F003","role":"specialization","statement":"Yönetim uzantısında halk, yöneticinin sorumluluğundaki topluluktur."}],"identity_rationale":"Kaynak ifadesi çobanın hayvanı çevreleyip korumasını ve yöneticinin halkını yönetip korumasını aynı gözetme çekirdeğinde birleştirir. Geçici çerçeve hem hayvan hem insan topluluğu yönünü doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"hayvanı gözetip korumak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"çoban veya yönetici"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yönetilen halk veya topluluk"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yöneticinin halkını yönetip koruması"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"gözetme ve koruma; çobanlık veya yönetim"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"sürü veya mal yönetiminde becerikli kimse"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bir şeyi birinin gözetimine vermek"}],"lexicalization_note":"Tanım, hayvanı gözetme çekirdeği ile yönetici ve halk yapısına bağlı siyasal uzantıyı birbirine karıştırmadan gösterir.","neighbor_coverage_note":"Bütün adaylar incelendi; genel koruma, koruyucu bekleme ve otlama ile temel karışma noktalarını gösteren üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeği çobanlık ve bunun yönetime uzanan örüntüsüdür; komşu dal ise nesnesi bakımından daha genel bir koruma ve üstlenme alanıdır.","focus_only":"Çoban-hayvan ve yönetici-halk ilişkilerini aynı sorumluluk örüntüsünde birleştirir.","gloss":"sorumlu gözetim","neighbor_only":"Her türlü şeyi koruma, gözetme, üstlenme ve emanet alma alanına yayılır.","neighbor_ref":"root_000342/B001","relation_type":"near_synonym","shared_zone":"İki dalda da bir şeyi koruyarak gözetme ve onunla ilgilenme vardır."},{"boundary_match":"partial","distinction":"Bu dal sürekli bakım ve yönetim sorumluluğuna dayanır; komşu dalın odağı tehlikeye karşı koruyucu bekleyiştir.","focus_only":"Bakım sorumluluğunu ve halkı yönetme uzantısını içerir.","gloss":"koruyucu gözetme","neighbor_only":"Tehlikeye karşı nöbet, sakınma ve koruyucu bekleme yönünü öne çıkarır.","neighbor_ref":"root_001311/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da koruma amacıyla dikkat ve gözetim gerektirir."},{"boundary_match":"field_only","distinction":"Bu dal koruyucu sorumluluğu, komşu dal ise hayvanın beslenme eylemini ve otlakla ilgili adları anlatır.","focus_only":"Sürüyü koruma ve halkı yönetme sorumluluğu bu dala özgüdür.","gloss":"gözetme ve otlama","neighbor_only":"Hayvanın ot yemesi, yenilen ot ve otlama yeri komşu dala özgüdür.","neighbor_ref":"root_000574/B001","relation_type":"same_field","shared_zone":"İki dal da sürü ve çobanlık alanında kullanılabilir."}],"source_phrase_ar":"الراعي الوالي (maqayis)؛ الراعي جمعه رعاة والراعي الوالي والرعية العامة (sihah)؛ الراعي يرعى الماشية أي يحوطها ويحفظها والوالي يرعى رعيته (tahdhib)؛ جعل الرعي والرعاء للحفظ والسياسة (mufradat)","source_summary":"Ortak anlatım, hayvanı koruyan çoban ile halkı yönetip koruyan yönetici arasında sorumluluk temelli bir gözetme bağı kurar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"حفظ الراعي للماشية؛ سياسة الوالي للرعية؛ الرعاية والحفظ العام","what_is_not_ar":"ليس أكل الكلإ نفسه ولا المرعى الموضع ولا الرجوع عن القبيح"},"support_links":["sup_acb68e249e6d79d8b78f"]},{"boundary":"Bu dal işitmeye kulak vermeyi veya hayvan gözetmeyi değil, bir şeyi ve gelişimini dikkatle izlemeyi anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000574/B003","candidate_links":[{"candidate_id":"cand_b1792cbc9527ff8f5eee","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَرْعَىٰ","morph_features":"STEM|POS:N|LEM:maroEaY`|ROOT:rEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:4:3:2","qac_word_ref":"87:4:3","surface_ar":"مَرْعَىٰ"}],"gloss":"dikkatle izleme ve gidişatı gözetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, bir şeyi dikkatle gözleyip izlemektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işin nereye varacağını ve nasıl sonuçlanacağını izlemek özel bir kullanımdır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yıldızları gözleyip izlemek bu çekirdeğin belirtilen bir örneğidir."}}],"root_ar":"ر ع ي","root_id":"root_000574","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel gözlemi ve bir işin varacağı sonucu takip etmeyi birlikte anlatmak gereken bağlamlarda kullanılır.","boundary_detail":"Bu dal işitmeye kulak vermeyi veya hayvan gözetmeyi değil, bir şeyi ve gelişimini dikkatle izlemeyi anlatır.","branch_image_ar":"مراعاة الأمر ومراقبته","concept_gloss":"dikkatle izleme ve gidişatı gözetme","contextual_glosses":[{"applicability":"Bir kişi, nesne veya olayın dikkatle gözlendiği genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikkatli gözlem ve izleme çekirdeğini korur."},"facet_ids":["F001"],"text":"dikkatle izlemek","usage_role":"general"},{"applicability":"Bir işin nasıl gelişeceğinin ve nereye varacağının izlendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir işin gidişini sonuç noktasına kadar takip etme yönünü korur."},"facet_ids":["F002"],"text":"sonucunu gözetmek","usage_role":"contextual"},{"applicability":"Gökyüzündeki yıldızların izlenmesi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yıldızları dikkatle gözleme örneğini korur."},"facet_ids":["F003"],"text":"yıldızları gözlemek","usage_role":"contextual"}],"definition":"Bir şeyi dikkatle gözleyip izlemek; özellikle bir işin nasıl sonuçlanacağını takip etmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, bir şeyi dikkatle gözleyip izlemektir."},{"facet_id":"F002","role":"specialization","statement":"Bir işin nereye varacağını ve nasıl sonuçlanacağını izlemek özel bir kullanımdır."},{"facet_id":"F003","role":"example","statement":"Yıldızları gözleyip izlemek bu çekirdeğin belirtilen bir örneğidir."}],"identity_rationale":"Kaynak ifadesi bir şeyi gözleyip izlemeyi, bir işin nereye varacağını takip etmeyi ve yıldızları gözlemeyi açıkça bir araya getirir. Geçici kimlik bu izleme çekirdeğini doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"dikkatle gözleyip izlemek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"işin nereye varacağını izlemek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yıldızları gözlemek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kimsenin sözüne kulak asmamak"}],"lexicalization_note":"Genel gözleme çekirdeği, bir işin sonucunu gözetme ve yıldızları izleme kullanımlarından ayrılarak tanımlanır.","neighbor_coverage_note":"Adayların tümü değerlendirildi; dikkatli inceleme, uzun bakış ve dinleme ile temel sınırları gösteren üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal süreğen takip ve sonucu gözetmeye dayanır; komşu dal ise bakış sırasında sağlam inceleme yapmayı merkez alır.","focus_only":"Bir olayın gidişini ve nereye varacağını zaman içinde takip eder.","gloss":"izleme ve inceleme","neighbor_only":"Bir şeyi açıkça anlamak için bakışta ağır ve sağlam davranmayı öne çıkarır.","neighbor_ref":"root_000052/B002","relation_type":"near_neighbor","shared_zone":"İki dal da dikkatli bakış ve zihinsel odaklanma gerektirir."},{"boundary_match":"partial","distinction":"Komşu dal uzun süren görsel bakışla sınırlıdır; bu dal ise izlenen işin gidişatını ve sonucunu da kapsayan daha işlevsel bir gözlemdir.","focus_only":"Nesnenin yanı sıra bir işin gelişimini ve sonucunu da kapsar.","gloss":"uzun bakış","neighbor_only":"Gözün bir şeye uzun süre bakmasını bedensel bakış olarak öne çıkarır.","neighbor_ref":"root_001288/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bakışı bir hedef üzerinde sürdürme vardır."},{"boundary_match":"field_only","distinction":"Bu dal gözlem ve gidişat takibidir; komşu dal ise işitmeye dayalı dikkat ve dinlemedir.","focus_only":"Görsel veya zihinsel gözlemle gelişimi takip eder.","gloss":"izlemek ve dinlemek","neighbor_only":"Bir söze işitme yoluyla dikkat verip dinlemeyi anlatır.","neighbor_ref":"root_000574/B004","relation_type":"same_field","shared_zone":"İki dal da bir hedefe bilinçli dikkat yöneltir."}],"source_phrase_ar":"رعيت الشيء رقبته ورعيته إذا لاحظته؛ راعيت الأمر نظرت إلام يصير؛ رعيت النجوم رقبتها (maqayis)؛ راعيته لاحظته؛ رعيت النجوم رقبتها (sihah)؛ المراعاة المناظرة والمراقبة (tahdhib)؛ مراعاة الإنسان للأمر مراقبته إلى ماذا يصير (mufradat)","source_summary":"Ortak anlam dikkatli gözlem ve izlemedir; bu izleme bir işin gidişatına ve sonucuna yöneltilebildiği gibi yıldızlara da yöneltilebilir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"مراقبة الشيء وملاحظته؛ النظر في مآل الأمر؛ رعي النجوم بمعنى مراقبتها","what_is_not_ar":"ليس رعي الماشية ولا الرعية السياسية ولا إصغاء السمع وحده"},"support_links":["sup_3ea9a34b16fb0c95f507"]},{"boundary":"Bu dal genel gözlem değil, söze işitme dikkatini verme veya karşıdakinden bunu isteme yapısıyla sınırlıdır.","branch_kind":"non_bare","branch_ref":"root_000574/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَرْعَىٰ","morph_features":"STEM|POS:N|LEM:maroEaY`|ROOT:rEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:4:3:2","qac_word_ref":"87:4:3","surface_ar":"مَرْعَىٰ"}],"gloss":"kulak verip dinleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, birinin sözüne kulak verip onu dinlemektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Buyruk biçiminde karşıdakinden söze kulak vermesi istenir."}}],"root_ar":"ر ع ي","root_id":"root_000574","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir söze işitme dikkatini verme ve bunun istenmesi anlamlarını kapsayan açıklamalarda kullanılır.","boundary_detail":"Bu dal genel gözlem değil, söze işitme dikkatini verme veya karşıdakinden bunu isteme yapısıyla sınırlıdır.","branch_image_ar":"إرعاء السمع","concept_gloss":"kulak verip dinleme","contextual_glosses":[{"applicability":"Birinin söylediklerini dikkatle dinleme eylemi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Söze işitme dikkatini yöneltme anlamını korur."},"facet_ids":["F001"],"text":"kulak vermek","usage_role":"general"},{"applicability":"Konuşanın karşıdakinden sözüne kulak vermesini istediği buyruk bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dinleyiciden söze kulak vermesini isteme anlamını korur."},"facet_ids":["F002"],"text":"bizi dinle","usage_role":"contextual"}],"definition":"Birinin sözüne işitme dikkatini verip dinlemek veya karşıdakinden kendi sözünü böyle dinlemesini istemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, birinin sözüne kulak verip onu dinlemektir."},{"facet_id":"F002","role":"specialization","statement":"Buyruk biçiminde karşıdakinden söze kulak vermesi istenir."}],"identity_rationale":"Kaynak ifadesi birine işitme dikkatini vermeyi ve karşıdakinden sözünü dinlemesini istemeyi aynı özel yapıda açıkça gösterir. Geçici çerçeve bu işitme yönünü doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ona kulak vermek; bana kulak ver"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bizi dinle, sözümüze kulak ver"}],"lexicalization_note":"Tanım yalnızca işitme dikkatini verme ve bunu isteme biçimlerine bağlıdır; genel bir dikkat veya gözetme anlamına genişletilmez.","neighbor_coverage_note":"Tüm adaylar gözden geçirildi; genel kulak verme, söze yönelme ve gizlice dinleme ile sınırı belirginleştiren üçü yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli verme ve isteme yapılarıyla sınırlıdır; komşu dal ise işitmenin konuşana yönelmesini daha doğrudan adlandırır.","focus_only":"İşitme dikkatini verme yanında bunu dinleyiciden isteyen buyruk biçimini de içerir.","gloss":"kulak verme","neighbor_only":"Kulağın veya işitmenin konuşana doğru yönelmesini bağımsız bir dinleme eylemi olarak öne çıkarır.","neighbor_ref":"root_000866/B002","relation_type":"near_synonym","shared_zone":"İki dalın çekirdeğinde konuşana işitme dikkatini yöneltip dinlemek vardır."},{"boundary_match":"partial","distinction":"Ortak çekirdek dinlemedir, ancak bu dal özel söz kalıplarına bağlı bir verme ve isteme ilişkisi taşır.","focus_only":"Karşıdakinden dinlemesini isteyen özel buyruk kullanımını da kapsar.","gloss":"söze kulak verme","neighbor_only":"İşitmeyi konuşana yöneltme eylemini daha genel biçimde anlatır.","neighbor_ref":"root_000021/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da sözü dikkatle işitip dinleme alanındadır."},{"boundary_match":"partial","distinction":"Bu dalda gizlilik koşulu yoktur ve dinleme açıkça istenebilir; komşu dalın ayırıcı koşulu gizlice işitmektir.","focus_only":"Açıkça söze kulak vermeyi veya dinleyiciden bunu istemeyi anlatır.","gloss":"gizlice dinleme","neighbor_only":"Başkalarının işittiğini fark ettirmeden gizlice dinlemeyi gerektirir.","neighbor_ref":"root_000700/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da konuşma veya sese işitme dikkati yöneltilir."}],"source_phrase_ar":"أرعيته سمعي أصغيت إليه؛ أرعني سمعك (maqayis)؛ أرعيته سمعي أي أصغيت إليه؛ راعنا من المراعاة على معنى أرعنا سمعك (sihah)؛ راعنا سمعك أي اسمع منا؛ أرعنا سمعك وراعنا سمعك بمعنى واحد (tahdhib)؛ أرعيته سمعي؛ أرعني سمعك (mufradat)","source_summary":"Ortak çerçeve, işitme dikkatini bir söze yöneltme ile konuşanın dinleyiciden bu dikkati istemesini aynı özel kullanım alanında birleştirir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"إصغاء السمع وإعارته للقول؛ صيغة راعنا بمعنى راعنا سمعك أو أرعنا سمعك","what_is_not_ar":"ليس الرعونة ولا طلب الرعي للماشية ولا مجرد المراقبة العامة"},"support_links":[]},{"boundary":"Dal yalnızca durmayı değil, yanlış veya bilgisizce bir tutumdan dönüp vazgeçmeyi; ayrıca genel el çekme kullanımını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000574/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَرْعَىٰ","morph_features":"STEM|POS:N|LEM:maroEaY`|ROOT:rEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:4:3:2","qac_word_ref":"87:4:3","surface_ar":"مَرْعَىٰ"}],"gloss":"yanlıştan dönüp vazgeçme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, çirkin veya bilgisizce bir tutumdan geri dönmektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Geri dönüş, yanlış davranıştan vazgeçip onu bırakmayı içerir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Daha genel kullanımda çeşitli işlerden el çekmek anlamına gelir."}}],"root_ar":"ر ع ي","root_id":"root_000574","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yanlış ya da bilgisizce bir davranıştan geri dönme ve onu bırakma çekirdeğini anlatan genel bağlamlarda kullanılır.","boundary_detail":"Dal yalnızca durmayı değil, yanlış veya bilgisizce bir tutumdan dönüp vazgeçmeyi; ayrıca genel el çekme kullanımını kapsar.","branch_image_ar":"الارعواء عن القبيح","concept_gloss":"yanlıştan dönüp vazgeçme","contextual_glosses":[{"applicability":"Bir kimsenin çirkin veya bilgisizce tutumunu bırakıp geri döndüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yanlış tutumdan geri dönme çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"yanlışından dönmek","usage_role":"general"},{"applicability":"Belirli bir yanlışlık vurgusu olmadan çeşitli işlerden vazgeçme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşlerden kendini çekip vazgeçme uzantısını korur."},"facet_ids":["F003"],"text":"el çekmek","usage_role":"contextual"}],"definition":"Çirkin veya bilgisizce bir tutumdan geri dönüp vazgeçmek; daha geniş kullanımda işlerden el çekmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, çirkin veya bilgisizce bir tutumdan geri dönmektir."},{"facet_id":"F002","role":"specialization","statement":"Geri dönüş, yanlış davranıştan vazgeçip onu bırakmayı içerir."},{"facet_id":"F003","role":"extension","statement":"Daha genel kullanımda çeşitli işlerden el çekmek anlamına gelir."}],"identity_rationale":"Kaynak ifadesi çirkin veya bilgisizce davranıştan geri dönmeyi, ondan vazgeçmeyi ve daha genel olarak işlerden el çekmeyi bildirir. Geçici çerçeve bu dönüş ve kendini tutma yapısını korur.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"çirkinlikten veya bilgisizlikten dönüp vazgeçmek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"işlerden el çekmek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yanlışından güzelce dönme ve vazgeçme"}],"lexicalization_note":"Yanlıştan dönme yapısı çekirdekte tutulur; genel işlerden el çekme kullanımı ayrı bir kapsam uzantısı olarak gösterilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bağlılıktan vazgeçme, genel geri durma ve doğruya dönüş ile sınırı açıklayan üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yanlış sayılan tutumdan düzgünce dönmeyi öne çıkarır; komşu dalın ayırıcı yönü daha önceki bağın veya uğraşın kesilmesidir.","focus_only":"Çirkinlik veya bilgisizlikten iyi bir dönüş yapma değerlendirmesini taşır.","gloss":"bağını kesip vazgeçme","neighbor_only":"Daha önce bağlanılmış bir işten, hevesten veya dönemden kopmayı özellikle belirtir.","neighbor_ref":"root_001489/B003","relation_type":"near_synonym","shared_zone":"İki dalda da sürmekte olan bir yönelişi bırakıp ondan geri çekilme vardır."},{"boundary_match":"partial","distinction":"Komşu dal genel durma ve yüz çevirmeyi kapsar; bu dalın çekirdeği yanlış davranıştan geri dönüp vazgeçmektir.","focus_only":"Yanlış veya bilgisizce tutumdan geri dönüşü ve bunun olumlu niteliğini içerir.","gloss":"geri durma","neighbor_only":"Herhangi bir işi engelleme, ondan yüz çevirme veya onu bırakma alanına daha geniş yayılır.","neighbor_ref":"root_000906/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da bir işten kendini çekme ve onu sürdürmeme anlamını paylaşır."},{"boundary_match":"partial","distinction":"Bu dal davranışı bırakma ve kendini tutma çekirdeğindedir; komşu dal doğruya dönüşü belirli bir pişmanlık ve yöneliş çerçevesine bağlar.","focus_only":"Çirkinlikten veya bilgisizlikten vazgeçmeyi, belirli bir inançsal çerçeve gerektirmeden anlatır.","gloss":"doğruya dönüş","neighbor_only":"Doğru kabul edilen yola dönme ve pişmanlıkla bağışlanma arama yönünü içerir.","neighbor_ref":"root_001605/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da yanlış görülen bir yoldan geri dönme vardır."}],"source_phrase_ar":"الأصل الآخر ارعوى عن القبيح إذا رجع (maqayis)؛ رعا يرعو أي كف عن الأمور؛ ارعوى عن القبيح (sihah)؛ ارعوى فلان عن الجهل وهو نزوعه وحسن رجوعه (tahdhib)","source_summary":"Ortak anlam yanlış veya bilgisizce bir tutumdan dönüp vazgeçmedir; anlatım ayrıca genel olarak işlerden el çekmeye uzanır.","sources":["MQ","SI","TA"],"what_is_ar":"الارعواء عن القبيح والجهل؛ الكف عن الأمور؛ حسن الرجوع والنزوع","what_is_not_ar":"ليس رعي الكلإ ولا الرعاية والحفظ ولا إرعاء السمع"},"support_links":[]},{"boundary":"Dal, genel bakım sorumluluğundan çok birini veya bir şeyi esirgeyip bırakmayı ve haklarla verilen sözü korumayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000574/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَرْعَىٰ","morph_features":"STEM|POS:N|LEM:maroEaY`|ROOT:rEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:4:3:2","qac_word_ref":"87:4:3","surface_ar":"مَرْعَىٰ"}],"gloss":"esirgeyip koruma ve sözü gözetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, bir kişi veya şeyi yok etmeyip esirgeyerek korumaktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiye yönelik kullanım acıma ve ona zarar vermeden bırakma yönü taşır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Koruyup sürdürme ilişkisi hakları ve verilen sözü gözetmeye uzanır."}}],"root_ar":"ر ع ي","root_id":"root_000574","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem kişi veya şeyi esirgeme çekirdeğini hem de haklarla verilen sözü koruma uzantısını birlikte anlatırken kullanılır.","boundary_detail":"Dal, genel bakım sorumluluğundan çok birini veya bir şeyi esirgeyip bırakmayı ve haklarla verilen sözü korumayı anlatır.","branch_image_ar":"الإبقاء ورعاية العهد","concept_gloss":"esirgeyip koruma ve sözü gözetme","contextual_glosses":[{"applicability":"Bir kişi veya şeyin yok edilmeden, zarar verilmeden bırakılıp korunduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Esirgeyerek koruma ve zarar vermeden bırakma çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"esirgeyip korumak","usage_role":"general"},{"applicability":"Hakların korunması ve verilmiş bir sözün sürdürülmesi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hakları ve verilen sözü koruyup sürdürme uzantısını korur."},"facet_ids":["F003"],"text":"hakları ve verilen sözü gözetmek","usage_role":"contextual"}],"definition":"Birini veya bir şeyi esirgeyip koruyarak bırakmak; ayrıca hakları ve verilen sözü gözetip sürdürmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, bir kişi veya şeyi yok etmeyip esirgeyerek korumaktır."},{"facet_id":"F002","role":"specialization","statement":"Bir kişiye yönelik kullanım acıma ve ona zarar vermeden bırakma yönü taşır."},{"facet_id":"F003","role":"extension","statement":"Koruyup sürdürme ilişkisi hakları ve verilen sözü gözetmeye uzanır."}],"identity_rationale":"Kaynak ifadesi bir şeyi veya kişiyi esirgeyip korumayı, kişiye acımayı ve verilen söz ile hakları gözetmeyi aynı koruyup sürdürme alanında toplar. Geçici kimlik bu katmanları doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"onu esirgemek veya ona acımak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"esirgeme ve koruyup bırakma"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"esirgeme; verilen sözü gözetme"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"hakları ve verilen sözü gözetme"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bana karşı daha gözetici ve koruyucu"}],"lexicalization_note":"Esirgeyip koruma çekirdeği ile hakları ve verilen sözü gözetme uzantısı ayrı tutulur; özel söz kalıbı bütün dala yayılmaz.","neighbor_coverage_note":"Adayların tamamı incelendi; bağışlayıp sağ bırakma, genel koruyucu bakım ve acıma duygusu ile sınırı gösteren üç karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal bağışlama sonucu kişiyi sağ bırakmaya odaklanır; bu dal daha genel korumayı ve söz ile hakların sürdürülmesini de kapsar.","focus_only":"Nesneleri korumaya ve haklarla verilen sözü gözetmeye de uzanır.","gloss":"bağışlayıp sağ bırakma","neighbor_only":"Bir kişiyi bağışlayıp yok etmemeyi ve sevgiyi bir kusurdan sonra sürdürmeyi özellikle anlatır.","neighbor_ref":"root_000142/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir kişiyi yok etmeyip acıyarak esirgeme alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal esirgeyip bırakma ve sözü koruma çevresindedir; komşu dal sürekli bakım, gözetim ve üstlenme sorumluluğunu öne çıkarır.","focus_only":"Esirgeme, acıma ve verilen sözü sürdürme yönlerini taşır.","gloss":"koruyup gözetme","neighbor_only":"Bir şeyi emanet alıp sürekli gözetme, koruma ve bakımını üstlenme alanına yayılır.","neighbor_ref":"root_000342/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir kişi veya şeyi zarar görmekten koruma vardır."},{"boundary_match":"partial","distinction":"Komşu dal duygunun kendisini anlatır; bu dal ise esirgeyip koruma eylemini ve bunun söz ile haklara uzanan kullanımını anlatır.","focus_only":"Acımanın sonucunda kişiyi esirgeyip korumayı ve başka nesneleri sürdürmeyi içerir.","gloss":"acıma duygusu","neighbor_only":"Duygusal incelik ve güçlü acıma duygusunun kendisini merkez alır.","neighbor_ref":"root_000530/B001","relation_type":"near_neighbor","shared_zone":"Bir kişiye zarar vermemeye yönelten acıma iki dalda da bulunabilir."}],"source_phrase_ar":"الإرعاء الإبقاء (maqayis)؛ أرعيت عليه إذا أبقيت عليه وترحمته (sihah)؛ الإرعاء الإبقاء على أخيك؛ الرعوى رعاية الحفاظ للعهد (tahdhib)؛ أرع على كذا أي أبق عليه (mufradat)","source_summary":"Ortak çerçeve bir kişi veya şeyi esirgeyip korumayı, kişiye acımayı ve bu koruyucu tutumu haklarla verilen sözün sürdürülmesine genişletmeyi içerir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الإبقاء على الشيء أو الشخص؛ الترحم عليه؛ رعاية الحفاظ والعهد","what_is_not_ar":"ليس الرعي بالكسر ولا مراقبة النجوم ولا الارعواء"},"support_links":[]},{"boundary":"Dal genel olarak develeri veya otlayan hayvanları değil, iş gördürülen ve çevrede otlayan özel deve topluluğunu adlandırır.","branch_kind":"bare","branch_ref":"root_000574/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَرْعَىٰ","morph_features":"STEM|POS:N|LEM:maroEaY`|ROOT:rEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:4:3:2","qac_word_ref":"87:4:3","surface_ar":"مَرْعَىٰ"}],"gloss":"iş develeri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Terim, iş gördürmek için kullanılan deve topluluğunu adlandırır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu develerin insanların ve yerleşimlerinin çevresinde otladığı belirtilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adın iki söyleyiş biçimi aktarılır ve biçimlerden birinin bu anlamdaki kullanımı seyrek sayılır."}}],"root_ar":"ر ع ي","root_id":"root_000574","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İş gördürmek için kullanılan ve yerleşim çevresinde otlayan deve topluluğunun kısa adı olarak kullanılır.","boundary_detail":"Dal genel olarak develeri veya otlayan hayvanları değil, iş gördürülen ve çevrede otlayan özel deve topluluğunu adlandırır.","branch_image_ar":"الرعاوى من الإبل","concept_gloss":"iş develeri","contextual_glosses":[{"applicability":"Terimin iş gördürülen deve topluluğunu açıkladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İş gördürülen deve topluluğu anlamını korur."},"facet_ids":["F001"],"text":"işte kullanılan develer","usage_role":"explanatory"},{"applicability":"Develerin insanların yaşadığı yerlerin yakınında otlaması da belirtilmek istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İş gördürülme ile yerleşim çevresinde otlama özelliklerini birlikte korur."},"facet_ids":["F001","F002"],"text":"çevrede otlayan iş develeri","usage_role":"contextual"}],"definition":"İş gördürmek için kullanılan develere verilen topluluk adıdır; bu develerin insanların ve yerleşimlerin çevresinde otladığı da belirtilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Terim, iş gördürmek için kullanılan deve topluluğunu adlandırır."},{"facet_id":"F002","role":"associated_use","statement":"Bu develerin insanların ve yerleşimlerinin çevresinde otladığı belirtilir."},{"facet_id":"F003","role":"source_variant","statement":"Adın iki söyleyiş biçimi aktarılır ve biçimlerden birinin bu anlamdaki kullanımı seyrek sayılır."}],"identity_rationale":"Kaynak ifadesi terimi iş gördürülen develer için açıklar ve bu develerin insanların çevresinde otlamasını ek bir belirti olarak verir. Geçici kimlik bu özel deve topluluğunu doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"işte kullanılan veya yerleşim çevresinde otlayan develer"}],"lexicalization_note":"Tanım, bağımsız adın iş gördürülen deve topluluğu anlamını verir ve başka dallardaki otlama ya da bakım eylemlerini içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel deve alanı, otlamaya salınma durumu ve serbest otlatma ile sınırı en iyi gösteren üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal yalnızca belirli iş develerinin adıdır; komşu dal ise deve varlığı ve bakımına ilişkin çok daha geniş bir alandır.","focus_only":"İş gördürülen ve yerleşim çevresinde otlayan özel bir deve topluluğunu adlandırır.","gloss":"özel deve topluluğu","neighbor_only":"Develeri, sürülerini, çokluklarını, sahipliğini ve bakımlarındaki beceriyi genel olarak kapsar.","neighbor_ref":"root_000006/B001","relation_type":"same_field","shared_zone":"İki dalın ortak alanı develer ve onların insan eliyle kullanılmasıdır."},{"boundary_match":"field_only","distinction":"Bu dal bir deve topluluğunun adıdır; komşu dal ise devenin salınma, suya gitme ve sağılmama durumlarını anlatır.","focus_only":"Develerin iş gördürülmesi ve yerleşim yakınında otlaması belirleyicidir.","gloss":"otlamaya salınan deve","neighbor_only":"Devenin otlarken suya gönderilmesi ve özel olarak sağılmadan bırakılması gibi durumları içerir.","neighbor_ref":"root_000946/B006","relation_type":"same_field","shared_zone":"Her iki dal da kullanılan develerin otlama düzeniyle ilişkilidir."},{"boundary_match":"partial","distinction":"Komşu dal serbest bırakma ve otlatma düzenini anlatır; bu dal ise işte kullanılan özel deve topluluğunun adıdır.","focus_only":"İş gördürülen belirli bir deve topluluğunu ad olarak gösterir.","gloss":"otlamaya bırakılan sürü","neighbor_only":"Hayvanları serbestçe otlamaya bırakma eylemini ve bu durumdaki sürüyü genel olarak kapsar.","neighbor_ref":"root_000764/B003","relation_type":"near_neighbor","shared_zone":"İki dalda da develerin veya başka sürü hayvanlarının otlaması bulunabilir."}],"source_phrase_ar":"الرعاوى والرعاوى وهي الإبل التي يعتمل عليها (maqayis)؛ الرعاوى والرعاوى الإبل التي ترعى حوالي القوم وديارهم لأنها الإبل التي يعتمل عليها (sihah)؛ الرعاوى والرعاوى جميعا الإبل التي يعتمل عليها؛ لم أسمع الرعاوي بهذا المعنى إلا ها هنا (tahdhib)","source_summary":"Ortak tanım iş gördürülen develeri gösterir; çevrede otlama bu topluluğa eşlik eden bir özellik, ikinci söyleyiş biçiminin seyrekliği ise aktarılan bir kullanım notudur.","sources":["MQ","SI","TA"],"what_is_ar":"الرعاوى والرعاوى من الإبل التي يعتمل عليها أو ترعى حوالي القوم","what_is_not_ar":"ليس المرعى ولا الرعية ولا الرعوى بمعنى الرجوع"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["87:4:1"],"branch_refs":[],"candidate_id":"cand_98bc95556851372c20a3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:4:1:coordinated-relative-continuation","source_type":"word_analysis","support_ids":["sup_c8a4c3caf900de844cf0","sup_fb7ce32902ffcde59710"],"title":"opening connector extends the divine-description chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:1","qac_refs":["87:4:1:1"],"status":"accepted"}},{"anchor_refs":["87:4:1"],"branch_refs":[],"candidate_id":"cand_97c395f7670066b77aa7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:4:1:non-resultive-scope","source_type":"word_analysis","support_ids":["sup_54c5e6ef8ec9700cb874","sup_fb7ce32902ffcde59710"],"title":"coordination without resultive sequencing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:1","qac_refs":["87:4:1:1"],"status":"accepted"}},{"anchor_refs":["87:4:1"],"branch_refs":[],"candidate_id":"cand_6e040adaf80a580e17fe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:4:1:segmented-fused-boundary","source_type":"word_analysis","support_ids":["sup_7a71630eb55cb29fa4e3","sup_fb7ce32902ffcde59710"],"title":"separate particle heard in a joined boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:1","qac_refs":["87:4:1:1"],"status":"accepted"}},{"anchor_refs":["87:4:2"],"branch_refs":[],"candidate_id":"cand_68c9204641cdb961496f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:4:2:carried-antecedent","source_type":"word_analysis","support_ids":["sup_8ef1f3d78c3e585ce178","sup_e807e895fcb324f8c120"],"title":"masculine singular reference recovers the earlier antecedent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:2","qac_refs":["87:4:1:2"],"status":"accepted"}},{"anchor_refs":["87:4:2"],"branch_refs":[],"candidate_id":"cand_6d7aec67629f8d02c29d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:4:2:descriptive-title-chain","source_type":"word_analysis","support_ids":["sup_8ef1f3d78c3e585ce178","sup_93fbb28f290b9fe6a520"],"title":"relative architecture accumulates descriptors","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:2","qac_refs":["87:4:1:2"],"status":"accepted"}},{"anchor_refs":["87:4:2"],"branch_refs":[],"candidate_id":"cand_7ff960ab9a43a6f050c9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:4:2:joined-entry","source_type":"word_analysis","support_ids":["sup_8ef1f3d78c3e585ce178","sup_aaf0f544ea7881f14261"],"title":"joined entry prevents a hard restart","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:2","qac_refs":["87:4:1:2"],"status":"accepted"}},{"anchor_refs":["87:4:2"],"branch_refs":[],"candidate_id":"cand_7f291752dc1ce2637531","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:4:2:sila-dependence","source_type":"word_analysis","support_ids":["sup_0f77bc6fc6bc46793281","sup_8ef1f3d78c3e585ce178"],"title":"relative pronoun requires the following action clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:2","qac_refs":["87:4:1:2"],"status":"accepted"}},{"anchor_refs":["87:4:3"],"branch_refs":[],"candidate_id":"cand_4b44516d786306eff8f2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"87:4:3:form-contrast","source_type":"word_analysis","support_ids":["sup_5ad2678b1ec5f40de62b","sup_609d4b33f022a2ae5a7d"],"title":"surface form avoids intensive, sought, and result-state framing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:3","qac_refs":["87:4:2:1"],"status":"accepted"}},{"anchor_refs":["87:4:3"],"branch_refs":[],"candidate_id":"cand_427bffce3392abe5fe62","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"87:4:3:outward-sound-pressure","source_type":"word_analysis","support_ids":["sup_609d4b33f022a2ae5a7d","sup_69d47d22e8a3f212577d"],"title":"compact articulation presses toward the open object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:3","qac_refs":["87:4:2:1"],"status":"accepted"}},{"anchor_refs":["87:4:3"],"branch_refs":[],"candidate_id":"cand_e908512ed7b38061d2fa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"87:4:3:perfect-active-causation","source_type":"word_analysis","support_ids":["sup_609d4b33f022a2ae5a7d","sup_ae0bcb87ff29a87aa885"],"title":"perfect active Form IV assigns accomplished causation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:3","qac_refs":["87:4:2:1"],"status":"accepted"}},{"anchor_refs":["87:4:3"],"branch_refs":[],"candidate_id":"cand_36ed386ebd0abb529166","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"87:4:3:productive-emergence","source_type":"word_analysis","support_ids":["sup_5169c387b207b74dfd7d","sup_609d4b33f022a2ae5a7d"],"title":"root pressure narrows to hidden-to-visible production","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:3","qac_refs":["87:4:2:1"],"status":"accepted"}},{"anchor_refs":["87:4:3"],"branch_refs":[],"candidate_id":"cand_34186cf2d68112650a2a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"87:4:3:source-suppressed-recurrence","source_type":"word_analysis","support_ids":["sup_609d4b33f022a2ae5a7d","sup_7e5b4f884170ed8f366c"],"title":"exact pasture formula recurs while the source is omitted","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:3","qac_refs":["87:4:2:1"],"status":"accepted"}},{"anchor_refs":["87:4:3"],"branch_refs":[],"candidate_id":"cand_93e72daf33bf75c201b9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"87:4:3:surah-movement-and-reversal","source_type":"word_analysis","support_ids":["sup_609d4b33f022a2ae5a7d","sup_913a0b5f56f461a06284"],"title":"visible provision pivots toward immediate transformation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:3","qac_refs":["87:4:2:1"],"status":"accepted"}},{"anchor_refs":["87:4:4"],"branch_refs":[],"candidate_id":"cand_13eb0b2a0161f8ff4c50","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000574"],"scope":"focus_ayah","source_local_id":"87:4:4:care-pressure","source_type":"word_analysis","support_ids":["sup_580e82e0031a8ae75761","sup_7a0637abee374e9bce69"],"title":"grazing root carries care without making an agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:4","qac_refs":["87:4:3:1","87:4:3:2"],"status":"accepted"}},{"anchor_refs":["87:4:4"],"branch_refs":[],"candidate_id":"cand_4012de2865b66c1fea10","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000574"],"scope":"focus_ayah","source_local_id":"87:4:4:closing-scene-cadence","source_type":"word_analysis","support_ids":["sup_547f080162e75f47ca63","sup_580e82e0031a8ae75761"],"title":"final object shifts action into perceivable landscape","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:4","qac_refs":["87:4:3:1","87:4:3:2"],"status":"accepted"}},{"anchor_refs":["87:4:4"],"branch_refs":[],"candidate_id":"cand_e2df9774761da570b61a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000574"],"scope":"focus_ayah","source_local_id":"87:4:4:definite-object-forward-reference","source_type":"word_analysis","support_ids":["sup_580e82e0031a8ae75761","sup_80a3769d62a98963a5f2"],"title":"definite direct object becomes the next pronoun's antecedent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:4","qac_refs":["87:4:3:1","87:4:3:2"],"status":"accepted"}},{"anchor_refs":["87:4:4"],"branch_refs":[],"candidate_id":"cand_947138cb0a23eeb01c08","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000574"],"scope":"focus_ayah","source_local_id":"87:4:4:place-resource-habitat","source_type":"word_analysis","support_ids":["sup_580e82e0031a8ae75761","sup_c18d147217f8a6560993"],"title":"place-resource noun fuses ground and yield","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:4","qac_refs":["87:4:3:1","87:4:3:2"],"status":"accepted"}},{"anchor_refs":["87:4:4"],"branch_refs":[],"candidate_id":"cand_9bf3f936e12f69b267c3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000574"],"scope":"focus_ayah","source_local_id":"87:4:4:rare-ecological-recurrence","source_type":"word_analysis","support_ids":["sup_4365be6eee41405ec6ae","sup_580e82e0031a8ae75761"],"title":"rare pasture noun anchors recurrence and prior-use contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:4:4","qac_refs":["87:4:3:1","87:4:3:2"],"status":"accepted"}},{"anchor_refs":["87:4:2"],"branch_refs":[],"candidate_id":"cand_5115e399acb336f4fdee","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"87:4:2:1","source_type":"qac_morpheme","support_ids":["sup_74943c2f12024e548945"],"title":"QAC root occurrence: خ ر ج","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:4:3"],"branch_refs":[],"candidate_id":"cand_81c18e5315669bc12149","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000574"],"scope":"focus_ayah","source_local_id":"87:4:3:2","source_type":"qac_morpheme","support_ids":["sup_761b105f55471dea400c"],"title":"QAC root occurrence: ر ع ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:4","branch_refs":["root_000400/B002","root_000574/B001"],"candidate_id":"cand_c3495edd9c461a37178b","commentary_obligation":"review","hft_ref":"hft_1d23bd41de7324d21165","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_emergent_provision","source_type":"hft","support_ids":["sup_1f012d8ae1609f960d2a"],"title":"b_emergent_provision","trust":"legacy_unbound"},{"anchor_refs":["87:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:4","branch_refs":["root_000400/B003","root_000574/B002"],"candidate_id":"cand_88ed936fcdded8d3cf72","commentary_obligation":"review","hft_ref":"hft_78276b895b8837cad00e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_custodial_yield","source_type":"hft","support_ids":["sup_acb68e249e6d79d8b78f"],"title":"b_custodial_yield","trust":"legacy_unbound"},{"anchor_refs":["87:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:4","branch_refs":["root_000400/B001","root_000574/B003"],"candidate_id":"cand_b1792cbc9527ff8f5eee","commentary_obligation":"review","hft_ref":"hft_92503372d5b7fa639ea8","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_watched_trajectory","source_type":"hft","support_ids":["sup_3ea9a34b16fb0c95f507"],"title":"b_watched_trajectory","trust":"legacy_unbound"},{"anchor_refs":["87:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:4","branch_refs":["root_000400/B007","root_000574/B001"],"candidate_id":"cand_fbae4d8cbb4b413143af","commentary_obligation":"review","hft_ref":"hft_9f8e91ae486ff65148fc","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_variegated_field","source_type":"hft","support_ids":["sup_ea2ac7faee43e4ff417d"],"title":"b_variegated_field","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:4:1:1","qac_word_ref":"87:4:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"87:4:1:2","qac_word_ref":"87:4:1","root_ar":"","surface_ar":"ٱلَّذِىٓ"},{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","root_ar":"خ ر ج","surface_ar":"أَخْرَجَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"87:4:3:1","qac_word_ref":"87:4:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مَرْعَىٰ","morph_features":"STEM|POS:N|LEM:maroEaY`|ROOT:rEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:4:3:2","qac_word_ref":"87:4:3","root_ar":"ر ع ي","surface_ar":"مَرْعَىٰ"}],"word_analysis_qac_refs":[["87:4:1:1"],["87:4:1:2"],["87:4:2:1"],["87:4:3:1","87:4:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["87:4:1","87:4:2","87:4:3","87:4:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:4:1:1","qac_word_ref":"87:4:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"87:4:1:2","qac_word_ref":"87:4:1","root_ar":"","surface_ar":"ٱلَّذِىٓ"},{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"87:4:2:1","qac_word_ref":"87:4:2","root_ar":"خ ر ج","surface_ar":"أَخْرَجَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"87:4:3:1","qac_word_ref":"87:4:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مَرْعَىٰ","morph_features":"STEM|POS:N|LEM:maroEaY`|ROOT:rEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"87:4:3:2","qac_word_ref":"87:4:3","root_ar":"ر ع ي","surface_ar":"مَرْعَىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["87:4:1:1"],["87:4:1:2"],["87:4:2:1"],["87:4:3:1","87:4:3:2"]],"word_analysis_refs":["87:4:1","87:4:2","87:4:3","87:4:4"],"word_rows":[{"analysis_record_ref":"87:4:1","analytic_gloss_range_en":"clause-opening conjunction that coordinates the new relative clause with the preceding descriptive chain while avoiding a resultive sequence reading","analytic_root_gloss_range_en":null,"qac_refs":["87:4:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"87:4:2","analytic_gloss_range_en":"masculine singular relative pronoun that depends on an earlier divine antecedent and turns the following action clause into characterization","analytic_root_gloss_range_en":null,"qac_refs":["87:4:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"ٱلَّذِىٓ","transliteration":"alladhī"}},{"analysis_record_ref":"87:4:3","analytic_gloss_range_en":"perfect active Form IV caused emergence of the pasture as an explicit object; locally productive bringing-forth, not expulsion, sought retrieval, or passive result-state naming","analytic_root_gloss_range_en":"broad emergence and output root range including going out, causing out, yield, and other specialized branches; here grammar selects caused hidden-to-visible production with a concrete ecological object","qac_refs":["87:4:2:1"],"root":{"arabic":"خ ر ج","transliteration":"kh-r-j"},"surface":{"arabic":"أَخْرَجَ","transliteration":"akhraja"}},{"analysis_record_ref":"87:4:4","analytic_gloss_range_en":"definite pasture as a whole place-resource and grazed provision-field, the object brought forth here and the antecedent transformed in the next ayah","analytic_root_gloss_range_en":"grazing, pasture, shepherding, custodial care, attentive regard, and preservation; here narrowed to pasture as a provision-field with care and grazing pressure, not to an active shepherding agent","qac_refs":["87:4:3:1","87:4:3:2"],"root":{"arabic":"ر ع ي","transliteration":"r-ʿ-y"},"surface":{"arabic":"ٱلْمَرْعَىٰ","transliteration":"al-marʿā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["87:4"],"branch_refs":["root_000400/B002","root_000574/B001"],"candidate_id":"cand_c3495edd9c461a37178b","evidence_scope":"focus_ayah","hft_ref":"hft_1d23bd41de7324d21165","item_id":"b_emergent_provision","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_emergent_provision","support_id":"sup_1f012d8ae1609f960d2a"},{"anchor_refs":["87:4"],"branch_refs":["root_000400/B003","root_000574/B002"],"candidate_id":"cand_88ed936fcdded8d3cf72","evidence_scope":"focus_ayah","hft_ref":"hft_78276b895b8837cad00e","item_id":"b_custodial_yield","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_custodial_yield","support_id":"sup_acb68e249e6d79d8b78f"},{"anchor_refs":["87:4"],"branch_refs":["root_000400/B001","root_000574/B003"],"candidate_id":"cand_b1792cbc9527ff8f5eee","evidence_scope":"focus_ayah","hft_ref":"hft_92503372d5b7fa639ea8","item_id":"b_watched_trajectory","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_watched_trajectory","support_id":"sup_3ea9a34b16fb0c95f507"},{"anchor_refs":["87:4"],"branch_refs":["root_000400/B007","root_000574/B001"],"candidate_id":"cand_fbae4d8cbb4b413143af","evidence_scope":"focus_ayah","hft_ref":"hft_9f8e91ae486ff65148fc","item_id":"b_variegated_field","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_variegated_field","support_id":"sup_ea2ac7faee43e4ff417d"}],"diagnostics":[],"lane_counts":{"global":8,"macro":11,"micro":4},"packet_summary":{"ayah_count":19,"focus_ref":"87:4","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ء ث ر","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":true,"target_occurrences":9,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]}],"window":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"87:4","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"87:4","lane":"micro","linguistic_source_ref":"87:4","surface_ref":"87:4","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"87:4","target_tokens":[["O",["87:4:1"]],["otlağı",["87:4:3"]],["ortaya",["87:4:2"]],["çıkardı",["87:4:2"]]],"text":"O, otlağı ortaya çıkardı."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s087-p01-001-019","label":"Whole surah","number":1,"refs":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:2:sila-dependence","source_type":"word_analysis","support_id":"sup_0f77bc6fc6bc46793281","text":"{\"blocking_evidence\":null,\"headline\":\"relative pronoun requires the following action clause\",\"reader_payoff\":\"The reader notices that the verb-object action is grammatically subordinated as characterization, not left as a free-standing report.\",\"reason\":\"QAC and attachment evidence identify the word as a masculine singular relative pronoun whose completing clause is the local verb-object sequence.\",\"representative_source_ids\":[\"QG-0ee9100e\",\"MG-a24dd6b0\",\"QT-8328bb9e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:4:rare-ecological-recurrence","source_type":"word_analysis","support_id":"sup_4365be6eee41405ec6ae","text":"{\"blocking_evidence\":null,\"headline\":\"rare pasture noun anchors recurrence and prior-use contrast\",\"reader_payoff\":\"The reader notices that this is not a generic vegetation word: the rare pasture noun participates in the 79:31 emergence formula and precedes creaturely grazing use seen in 20:54.\",\"reason\":\"The contextual evidence marks this exact form as low-occurrence and tightly paired with the emergence verb, while the CRITICAL rows give concrete references at 79:31 and 20:54.\",\"representative_source_ids\":[\"QI-cf70fee6\",\"MI-471babdf\",\"QI-b2e7587e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:3:productive-emergence","source_type":"word_analysis","support_id":"sup_5169c387b207b74dfd7d","text":"{\"blocking_evidence\":null,\"headline\":\"root pressure narrows to hidden-to-visible production\",\"reader_payoff\":\"The reader notices that the act is generative exposure of pasture from hidden potential, while expulsion and unrelated output branches are not selected locally.\",\"reason\":\"The broad root includes emergence, departure, and output branches, but Form IV with the pasture object selects caused productive emergence and blocks expulsion as the local sense.\",\"representative_source_ids\":[\"QS-05fd6f99\",\"QS-1d73dba7\",\"MS-b144a247\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:4:closing-scene-cadence","source_type":"word_analysis","support_id":"sup_547f080162e75f47ca63","text":"{\"blocking_evidence\":null,\"headline\":\"final object shifts action into perceivable landscape\",\"reader_payoff\":\"The reader notices the ayah closing on a concrete visible provision-field, with an open cadence that lets the landscape linger before reversal.\",\"reason\":\"The word is the final direct object of the clause, so the structural and sound rows coherently describe the movement from verbal action to visible scene.\",\"representative_source_ids\":[\"QT-16beac8c\",\"QT-ed687c9d\",\"QP-56b49a76\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:1:non-resultive-scope","source_type":"word_analysis","support_id":"sup_54c5e6ef8ec9700cb874","text":"{\"blocking_evidence\":null,\"headline\":\"coordination without resultive sequencing\",\"reader_payoff\":\"The reader notices that the connector keeps pasture-production cumulative, not narrowly framed as the immediate result of the previous clause alone.\",\"reason\":\"The local conjunction licenses additive coordination and does not force the resultive relation that the CRITICAL rows contrast with.\",\"representative_source_ids\":[\"QG-85a4d98e\",\"QS-c70048eb\",\"QT-5b651d91\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:4","source_type":"word_analysis","support_id":"sup_580e82e0031a8ae75761","text":"{\"gloss_range\":\"definite pasture as a whole place-resource and grazed provision-field, the object brought forth here and the antecedent transformed in the next ayah\",\"prose\":\"{{ar:ٱلْمَرْعَىٰ}} ({{tr:al-marʿā}}) is the named object where the action lands. Its definiteness makes pasture a recognizable provision-category, and its direct-object role stages it as what is brought forth, not as scenery merely mentioned. The noun's singular place-resource pattern lets the word hold both grazing-ground and grazed growth together: a whole usable habitat of nourishment rather than an indefinite meadow or countable plants alone. The root's grazing and care range adds pressure without changing the local noun into an agent; pasture is felt as a tended, watched-over provision-field and as access for feeding, not simply raw fodder. Its rarity and exact pairing with caused emergence link it to the same pasture-yield frame in 79:31, while 20:54 shows eating and grazing after provision has been made available, so 87:4 places the resource before its users appear. Locally, the final word also does forward work: it becomes the referent of {{ar:فَجَعَلَهُۥ}} ({{tr:fa-jaʿalahu}}) in 87:5, so the visible provision-field is immediately available for transformation into dark stubble. The open final cadence lets the ayah close on a perceivable landscape before that reversal.\",\"root_display\":\"{{ar:ر ع ي}} ({{tr:r-ʿ-y}})\",\"root_gloss_range\":\"grazing, pasture, shepherding, custodial care, attentive regard, and preservation; here narrowed to pasture as a provision-field with care and grazing pressure, not to an active shepherding agent\",\"surface_display\":\"{{ar:ٱلْمَرْعَىٰ}} ({{tr:al-marʿā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:3:form-contrast","source_type":"word_analysis","support_id":"sup_5ad2678b1ec5f40de62b","text":"{\"blocking_evidence\":null,\"headline\":\"surface form avoids intensive, sought, and result-state framing\",\"reader_payoff\":\"The reader notices the exact form as compact causation: neither repeated processing, nor deliberate sought retrieval, nor a mere named result-state.\",\"reason\":\"The local surface is Form IV finite active; the CRITICAL contrasts with other derivational frames clarify what this form contributes without replacing the selected sense.\",\"representative_source_ids\":[\"QF-1921ad03\",\"QF-33833462\",\"QF-a3136b1b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:3","source_type":"word_analysis","support_id":"sup_609d4b33f022a2ae5a7d","text":"{\"gloss_range\":\"perfect active Form IV caused emergence of the pasture as an explicit object; locally productive bringing-forth, not expulsion, sought retrieval, or passive result-state naming\",\"prose\":\"{{ar:أَخْرَجَ}} ({{tr:akhraja}}) is a perfect active Form IV verb, so the pasture appears as an accomplished caused emergence, not as autonomous growth. Its implicit subject is fixed by the relative pronoun, and {{ar:ٱلْمَرْعَىٰ}} ({{tr:al-marʿā}}) is the explicit patient-object receiving the act. The root pressure is hidden-to-visible production: pasture is drawn from hidden potential into exposure, like an output made available, while the object blocks an expulsion sense and the unnamed source lets extraction and production remain joined. The form also matters by contrast; the wording presents one compact causative act, not intensive repeated production, deliberate sought retrieval, or a passive-result label that would merely name the pasture as produced. The same verb-object pasture formula is recalled at 79:31, where the earth-source is named, while 87:4 suppresses that source and foregrounds the act itself. In the surah's movement, the verb turns measured guidance from 87:3 into visible provision and prepares the immediate reversal of {{ar:فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ}} ({{tr:fa-jaʿalahu ghuthāʾan aḥwā}}) (87:5). Even the compact guttural-to-open cadence makes the emergence feel pressed outward before the pasture noun lands.\",\"root_display\":\"{{ar:خ ر ج}} ({{tr:kh-r-j}})\",\"root_gloss_range\":\"broad emergence and output root range including going out, causing out, yield, and other specialized branches; here grammar selects caused hidden-to-visible production with a concrete ecological object\",\"surface_display\":\"{{ar:أَخْرَجَ}} ({{tr:akhraja}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:3:outward-sound-pressure","source_type":"word_analysis","support_id":"sup_69d47d22e8a3f212577d","text":"{\"blocking_evidence\":null,\"headline\":\"compact articulation presses toward the open object\",\"reader_payoff\":\"The reader notices a small sound-shape payoff: the verb's compact articulation pushes outward before the open pasture noun resolves it.\",\"reason\":\"The phonetic rows make a modest observation tied to the local verb-object phrase and do not conflict with grammar or lexical evidence.\",\"representative_source_ids\":[\"QP-6d4ee40a\",\"QP-c172150d\",\"MP-a01b3bf6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:4:2:1","source_type":"qac_morpheme","support_id":"sup_74943c2f12024e548945","text":"{\"lemma_ar\":\"أَخْرَجَ\",\"morph_features\":\"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"87:4:2:1\",\"qac_word_ref\":\"87:4:2\",\"root_ar\":\"خ ر ج\",\"surface_ar\":\"أَخْرَجَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:4:3:2","source_type":"qac_morpheme","support_id":"sup_761b105f55471dea400c","text":"{\"lemma_ar\":\"مَرْعَىٰ\",\"morph_features\":\"STEM|POS:N|LEM:maroEaY`|ROOT:rEy|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"87:4:3:2\",\"qac_word_ref\":\"87:4:3\",\"root_ar\":\"ر ع ي\",\"surface_ar\":\"مَرْعَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:4:care-pressure","source_type":"word_analysis","support_id":"sup_7a0637abee374e9bce69","text":"{\"blocking_evidence\":null,\"headline\":\"grazing root carries care without making an agent\",\"reader_payoff\":\"The reader notices that the pasture field carries tending and custodial care pressure, while local morphology keeps it a provision place-resource rather than a shepherding agent.\",\"reason\":\"The root range includes grazing and custodial care, but the local noun pattern selects the pasture resource, so care survives as lexical pressure rather than a change of referent.\",\"representative_source_ids\":[\"QS-0422444c\",\"QS-0f5ef3c7\",\"MS-8c4e7253\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:1:segmented-fused-boundary","source_type":"word_analysis","support_id":"sup_7a71630eb55cb29fa4e3","text":"{\"blocking_evidence\":null,\"headline\":\"separate particle heard in a joined boundary\",\"reader_payoff\":\"The reader notices that the particle remains syntactically visible while its recited joining makes the ayah boundary feel continuous.\",\"reason\":\"The bundle separates the conjunction from the relative pronoun, while the CRITICAL sound and form rows coherently note that the written-recited surface still joins them.\",\"representative_source_ids\":[\"QF-020f6032\",\"QF-854c6550\",\"QP-4c3af086\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:3:source-suppressed-recurrence","source_type":"word_analysis","support_id":"sup_7e5b4f884170ed8f366c","text":"{\"blocking_evidence\":null,\"headline\":\"exact pasture formula recurs while the source is omitted\",\"reader_payoff\":\"The reader notices the exact pasture-emergence formula in 79:31, and also notices that 87:4 leaves the source unnamed to foreground the causing act.\",\"reason\":\"The CRITICAL rows provide a concrete recurrence at 79:31; the local grammar has no source phrase, so the echo survives as formulaic contrast rather than as an added local complement.\",\"representative_source_ids\":[\"QI-a1e04077\",\"QI-decefdfd\",\"MI-4bfdfa41\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:4:definite-object-forward-reference","source_type":"word_analysis","support_id":"sup_80a3769d62a98963a5f2","text":"{\"blocking_evidence\":null,\"headline\":\"definite direct object becomes the next pronoun's antecedent\",\"reader_payoff\":\"The reader notices that the pasture is a recognized object brought into view and then grammatically carried forward into 87:5.\",\"reason\":\"QAC and attachment evidence identify the word as the definite direct object of the verb, and the bundle flags the next ayah's pronoun as resuming this object.\",\"representative_source_ids\":[\"QG-aa320d7e\",\"QG-f20e50ef\",\"QB-b567c060\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:2","source_type":"word_analysis","support_id":"sup_8ef1f3d78c3e585ce178","text":"{\"gloss_range\":\"masculine singular relative pronoun that depends on an earlier divine antecedent and turns the following action clause into characterization\",\"prose\":\"{{ar:ٱلَّذِىٓ}} ({{tr:alladhī}}) is not a new independent subject inside this ayah. It needs the following {{ar:أَخْرَجَ ٱلْمَرْعَىٰ}} ({{tr:akhraja al-marʿā}}) as its completing clause, and it points back to the earlier masculine singular divine antecedent rather than letting the pasture scene supply a fresh actor. That makes the pasture action descriptive: the ayah characterizes the same referent through another act instead of narrating an unrelated event. The repeated relative architecture also keeps the praise chain cumulative, so creation, measuring-guidance, and pasture-emergence become parallel identifiers; the form both qualifies the earlier lord-title and gives the referent a title-like description through action. After {{ar:وَ}} ({{tr:wa}}), the joined entry prevents a hard restart; dependence is heard as well as parsed.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ٱلَّذِىٓ}} ({{tr:alladhī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:3:surah-movement-and-reversal","source_type":"word_analysis","support_id":"sup_913a0b5f56f461a06284","text":"{\"blocking_evidence\":null,\"headline\":\"visible provision pivots toward immediate transformation\",\"reader_payoff\":\"The reader notices that the verb converts prior measured guidance into visible provision and sets up the pasture's transformation in 87:5.\",\"reason\":\"The local clause belongs to the preceding relative chain and the bundle flags the following ayah as resuming the pasture, so the discourse pivot and forward reversal are licensed.\",\"representative_source_ids\":[\"QT-1625b251\",\"QE-36b4a923\",\"QB-4f355a04\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:2:descriptive-title-chain","source_type":"word_analysis","support_id":"sup_93fbb28f290b9fe6a520","text":"{\"blocking_evidence\":null,\"headline\":\"relative architecture accumulates descriptors\",\"reader_payoff\":\"The reader notices that repeated relative phrasing builds identity through acts before abstract doctrine is named.\",\"reason\":\"The local relative continues the same descriptive pattern, so the CRITICAL claim that it functions as both qualification and title-like descriptor is locally coherent.\",\"representative_source_ids\":[\"QG-fb06e2da\",\"QS-7dbc27e9\",\"MT-e19b5667\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:2:joined-entry","source_type":"word_analysis","support_id":"sup_aaf0f544ea7881f14261","text":"{\"blocking_evidence\":null,\"headline\":\"joined entry prevents a hard restart\",\"reader_payoff\":\"The reader notices that the relative pronoun arrives through the preceding connector, so a repeated form is heard as continuation rather than a fresh break.\",\"reason\":\"The CRITICAL phonetic and form observations fit the segmented conjunction plus relative pronoun and add a distinct surface-boundary payoff.\",\"representative_source_ids\":[\"QF-f838d63e\",\"QP-984d1c89\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:3:perfect-active-causation","source_type":"word_analysis","support_id":"sup_ae0bcb87ff29a87aa885","text":"{\"blocking_evidence\":null,\"headline\":\"perfect active Form IV assigns accomplished causation\",\"reader_payoff\":\"The reader notices pasture as something actively caused and accomplished by the carried subject, not as a neutral natural process.\",\"reason\":\"QAC identifies a perfect Form IV active verb, and attachment evidence fixes the implicit subject through the relative pronoun with an explicit direct object.\",\"representative_source_ids\":[\"QG-058820e6\",\"QG-11431b04\",\"MG-6dc6b8f6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:4:place-resource-habitat","source_type":"word_analysis","support_id":"sup_c18d147217f8a6560993","text":"{\"blocking_evidence\":null,\"headline\":\"place-resource noun fuses ground and yield\",\"reader_payoff\":\"The reader notices pasture as a whole habitat of nourishment, both where grazing happens and what is grazed.\",\"reason\":\"The local form is a definite noun of place or time pattern, and the V4 grazing branch supports pasture as place or thing grazed without forcing a choice between the two.\",\"representative_source_ids\":[\"QS-09473fae\",\"QF-5c383094\",\"MH-5b6d05cb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:1:coordinated-relative-continuation","source_type":"word_analysis","support_id":"sup_c8a4c3caf900de844cf0","text":"{\"blocking_evidence\":null,\"headline\":\"opening connector extends the divine-description chain\",\"reader_payoff\":\"The reader notices that pasture-emergence is added to the same divine profile rather than introduced as a detached ecological report.\",\"reason\":\"QAC identifies the word as a conjunction, and the attachment evidence treats the whole ayah as the local relative clause continuing the preceding descriptive chain.\",\"representative_source_ids\":[\"QG-24a19db6\",\"QG-4ad9e842\",\"MT-d3e3cf96\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:2:carried-antecedent","source_type":"word_analysis","support_id":"sup_e807e895fcb324f8c120","text":"{\"blocking_evidence\":null,\"headline\":\"masculine singular reference recovers the earlier antecedent\",\"reader_payoff\":\"The reader notices that the actor is not newly supplied by the pasture scene; reference is locked to the already carried divine antecedent.\",\"reason\":\"The relative pronoun is masculine singular and the verb's implicit subject is syntactically controlled by it, so the antecedent must be recovered from the preceding chain.\",\"representative_source_ids\":[\"QG-3f7e016c\",\"QG-a309f72c\",\"QG-cbc4c95e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:4:1","source_type":"word_analysis","support_id":"sup_fb7ce32902ffcde59710","text":"{\"gloss_range\":\"clause-opening conjunction that coordinates the new relative clause with the preceding descriptive chain while avoiding a resultive sequence reading\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) makes the pasture clause additive before any new action is heard. It coordinates {{ar:أَخْرَجَ ٱلْمَرْعَىٰ}} ({{tr:akhraja al-marʿā}}) with the preceding divine-description chain, so ecology enters as another descriptor of the same antecedent rather than as a detached sentence. Because the connector is not a result-marker, the pasture is not presented as the immediate consequence of only the prior clause; it joins the wider sequence of creation, measuring, guidance, and provision. Its separate segmentation also matters: even though it fuses in recitation with {{ar:ٱلَّذِىٓ}} ({{tr:alladhī}}), the particle keeps clause-wide scope and makes the boundary sound continuous.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ","ayah_ref":"87:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000400/B002","root_000574/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000400","role":"Causing a hidden thing to emerge supplies the transition from latent growth to visible availability.","root":"خ ر ج","source_ref":"87:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000574","role":"Grazing-place and fodder identify the emerged object as usable sustenance rather than vegetation in the abstract.","root":"ر ع ي","source_ref":"87:4","source_word_indices":["3"]}],"changed_reading":{"after":"The agent draws a grazing resource out of concealment and makes it available to consumers.","before":"The agent simply makes pasture exist."},"confidence":"strong","focus_anchor":"The causative verb at word 2 governs the pasture noun at word 3.","mechanism":"Causative extraction converts vegetation that was latent or enclosed into an accessible field of grazing.","model_id":"b_emergent_provision"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_emergent_provision","source_type":"hft","support_id":"sup_1f012d8ae1609f960d2a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ","ayah_ref":"87:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000400/B003","root_000574/B002"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000400","role":"A due output or yield supplies the image of provision issued in a determinate form.","root":"خ ر ج","source_ref":"87:4","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000574","role":"Shepherding and custodial preservation turn the yield into maintenance of beings under care.","root":"ر ع ي","source_ref":"87:4","source_word_indices":["3"]}],"changed_reading":{"after":"Pasture is a provisioned yield issued within a custodial economy.","before":"Pasture is a piece of natural scenery."},"confidence":"medium","focus_anchor":"The output verb and the semantic range of the pasture noun meet in the direct-object construction.","mechanism":"The pasture can be carried as an issued yield inside a relation of care: something is brought out because dependents must be maintained.","model_id":"b_custodial_yield"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_custodial_yield","source_type":"hft","support_id":"sup_acb68e249e6d79d8b78f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ","ayah_ref":"87:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000400/B001","root_000574/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000400","role":"Passing out from within supplies the initial phase of a trajectory.","root":"خ ر ج","source_ref":"87:4","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000574","role":"Watching an affair and considering its outcome makes the pasture's later condition part of how its emergence is read.","root":"ر ع ي","source_ref":"87:4","source_word_indices":["3"]}],"changed_reading":{"after":"The verse opens an observed pasture-trajectory whose end belongs to the meaning of its beginning.","before":"The verse records one moment of botanical appearance."},"confidence":"medium","focus_anchor":"The eventive emergence at word 2 is qualified by the outcome-aware range of the noun's root at word 3.","mechanism":"Emergence is not isolated from what follows it; the pasture is a process whose condition and outcome invite observation.","model_id":"b_watched_trajectory"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_watched_trajectory","source_type":"hft","support_id":"sup_3ea9a34b16fb0c95f507","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ","ayah_ref":"87:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000400/B007","root_000574/B001"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_000400","role":"Two-color patchiness supplies a mottled spatial pattern for the act of bringing forth.","root":"خ ر ج","source_ref":"87:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000574","role":"Literal pasture keeps the color-pattern activation anchored in an actual grazing landscape.","root":"ر ع ي","source_ref":"87:4","source_word_indices":["3"]}],"changed_reading":{"after":"Pasture emerges as a differentiated, patch-like surface whose contrasts are already perceptible.","before":"Pasture appears as a homogeneous green mass."},"confidence":"exploratory","focus_anchor":"A color-patch branch of the verb's root remains attached to the literal grazing field.","mechanism":"What is brought forth may be imagined not as a uniform carpet but as a visibly differentiated land surface, alternating growth with exposed or differently colored ground.","model_id":"b_variegated_field"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_variegated_field","source_type":"hft","support_id":"sup_ea2ac7faee43e4ff417d","trust":"legacy_unbound"}]}
</lane_packet_json>
