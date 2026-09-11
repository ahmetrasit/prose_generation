# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **87:19**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s087-regular-20260911/s087/87_19/micro.discovery.json` and modify nothing
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
  "ayah_ref": "87:19",
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
{"analysis_context":{"analysis_id":"s087-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"87:19","host_surah":87,"lane_context_refs":[],"ordered_context_refs":["87:0","87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, yazı yaprağını, bağlı yapraklar bütününü, yayvan kabı veya okuma yanlışını değil; yayılmış geniş yüzeyi ve buna bağlı özel kullanımları anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000845/B001","candidate_links":[{"candidate_id":"cand_7737c28a091844963ab6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صُحُف","morph_features":"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"87:19:1:1","qac_word_ref":"87:19:1","surface_ar":"صُحُفِ"}],"gloss":"yayılmış geniş yüzey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin yayılması ve geniş bir yüzey görünümü kazanması temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yeryüzünün görünen yüzü, yayılmış geniş yüzeyin özel bir gerçekleşmesidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsan yüzünün dış derisi, geniş ve açık yüzey düşüncesine bağlı özel bir kullanımdır."}}],"root_ar":"ص ح ف","root_id":"root_000845","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel çekirdeği ve özel yüzey kullanımlarının dayandığı ortak görünümü birlikte karşılar.","boundary_detail":"Dal, yazı yaprağını, bağlı yapraklar bütününü, yayvan kabı veya okuma yanlışını değil; yayılmış geniş yüzeyi ve buna bağlı özel kullanımları anlatır.","branch_image_ar":"انبساط وسعة","concept_gloss":"yayılmış geniş yüzey","contextual_glosses":[{"applicability":"Yalnızca yayılmış yüzeyin yeryüzünün görünen yüzünü anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":"Tek başına bütün yerküreyi de anlatabildiği için bağlamla sınırlandırılmalıdır.","fit":"narrowing","loses":"Genel yayılma çekirdeğini ve yüz derisi kullanımını dışarıda bırakır.","preserves":"Yeryüzünün görünen yüzü olan özel gerçekleşmeyi korur."},"facet_ids":["F002"],"text":"yeryüzü","usage_role":"contextual"},{"applicability":"İnsan yüzünün dış derisini belirten kalıplaşmış kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel geniş yüzey anlamını ve yeryüzü kullanımını karşılamaz.","preserves":"İnsan yüzünün dış derisine ilişkin özel kullanımı korur."},"facet_ids":["F003"],"text":"yüz derisi","usage_role":"contextual"}],"definition":"Bir şeyin yayılıp geniş bir yüzey oluşturması ya da böyle yayılmış yüzeyin kendisidir. Yeryüzünün görünen yüzü ve insan yüzünün dış derisi bu çekirdeğin özel adlandırmalarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin yayılması ve geniş bir yüzey görünümü kazanması temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Yeryüzünün görünen yüzü, yayılmış geniş yüzeyin özel bir gerçekleşmesidir."},{"facet_id":"F003","role":"specialization","statement":"İnsan yüzünün dış derisi, geniş ve açık yüzey düşüncesine bağlı özel bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi, dalın temelini bir şeydeki yayılma ve genişlik olarak kurar; yeryüzünün görünen yüzü ile insan yüzünün derisini de bu geniş yüzey düşüncesinin özel gerçekleşmeleri olarak verir. Bu nedenle sunulan dal kimliği kaynak anlatımıyla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yayılmış geniş yüzey"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yeryüzünün görünen yüzü"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yüz derisi"}],"lexicalization_note":"Tanım, genel yayılma ve geniş yüzey çekirdeğini korurken yeryüzü ve yüz derisi gibi kalıplaşmış kullanımları bu çekirdekten ayrı özel yüzey adları olarak sınırlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca yayılma, düz arazi ve geniş yüzey bakımından dal sınırını belirginleştiren üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal geniş yüzey görünümünü ve bu görünümün yeryüzü ile yüz derisindeki adlarını öne çıkarır; komşu dal ise yayma ve uzatma sürecini daha geniş bir eylem alanında anlatır.","focus_only":"Bu dal, yayılmanın ortaya çıkardığı geniş yüzeyi ve onun özel yüzey adlarını da kapsar.","gloss":"yayma ve genişletme","neighbor_only":"Komşu dal, bir şeyi yayma, uzatma ve genişletme eylemini daha genel biçimde kapsar.","neighbor_ref":"root_000928/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda bir şeyin açılarak yayılması ve genişlik kazanması ortak alandır."},{"boundary_match":"partial","distinction":"Odak dal genel yüzey genişliğini anlatır; komşu dal ise belirli düz, açık veya alçak arazi türlerini adlandırdığı için olağan bağlamda birbirlerinin yerine geçmez.","focus_only":"Odak dal her türlü yayılmış geniş yüzeyi ve yüz derisi gibi özel kullanımları kapsar.","gloss":"düz açık arazi","neighbor_only":"Komşu dal açık, düz veya çukurca belirli arazi biçimlerini ve geniş yolu adlandırır.","neighbor_ref":"root_000734/B009","relation_type":"near_neighbor","shared_zone":"Yeryüzünün geniş ve açık bir yüzey olarak görülmesi iki dalı birbirine yaklaştırır."},{"boundary_match":"partial","distinction":"Odak dal yayılma ve genişliği kurucu özellik sayar; komşu dal ise yan, kenar ve nesnenin belirli yüzü gibi konumsal bölümleri de kapsayan daha başka bir örgüye sahiptir.","focus_only":"Odak dalın çekirdeği bir şeyin yayılması ve geniş yüzey görünümüdür.","gloss":"yan ve enli yüz","neighbor_only":"Komşu dal bir nesnenin yanı, yüzü, kenarı veya özellikle enli hale getirilmiş biçimini kapsar.","neighbor_ref":"root_000867/B001","relation_type":"near_neighbor","shared_zone":"Bir nesnenin geniş görünen yüzü her iki dalın anlam alanına yaklaşabilir."}],"source_phrase_ar":"أصل صحيح يدل على انبساط في شيء وسعة (maqayis); الصحيف وجه الأرض (maqayis); صحيفة الوجه بشرة جلده (ayn); الصحيفة المبسوط من الشيء كصحيفة الوجه (mufradat)","source_summary":"Kaynakların ortak çerçevesi yayılma ve genişliği temel alır; görünen yeryüzü ile yüz derisini de bu yüzey kavrayışına bağlar.","sources":["MQ","AY","MU"],"what_is_ar":"انبساط الشيء وسعته ووجه الأرض وبشرة الوجه","what_is_not_ar":"الصحيفة المكتوبة والمصحف والصحفة والتصحيف"},"support_links":["sup_ced24621bc9f51de9f7f"]},{"boundary":"Dal, tek yazı yaprağı ile ondan oluşan kitap kullanımını kapsar; yüz derisi, yayvan kap, yaprakları kapaklar arasında toplama işlemi ve yanlış okuma bunun dışındadır.","branch_kind":"bare","branch_ref":"root_000845/B002","candidate_links":[{"candidate_id":"cand_e4935c28add11ce9520b","lane":"micro"},{"candidate_id":"cand_18576204d5386030822e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صُحُف","morph_features":"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"87:19:1:1","qac_word_ref":"87:19:1","surface_ar":"صُحُفِ"}],"gloss":"yazı yaprağı veya kitap","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, deri veya benzeri bir malzemeden olup üzerine yazı yazılan ya da yazı taşıyan tek yapraktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı ad kimi kullanımda yazılı yaprakların oluşturduğu kitap için de kullanılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaynak ifadesi tekil yazı yaprağı için birden çok çoğul biçim bildirir."}}],"root_ar":"ص ح ف","root_id":"root_000845","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek yazı yüzeyini, kitap genişlemesini ve bunların çoğul olarak anılabilmesini kapsayan genel karşılıktır.","boundary_detail":"Dal, tek yazı yaprağı ile ondan oluşan kitap kullanımını kapsar; yüz derisi, yayvan kap, yaprakları kapaklar arasında toplama işlemi ve yanlış okuma bunun dışındadır.","branch_image_ar":"صحيفة مكتوبة","concept_gloss":"yazı yaprağı veya kitap","contextual_glosses":[{"applicability":"Tek bir yazı yüzeyinin veya yazılı yaprağın söz konusu olduğu bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kitap için kullanılan genişlemiş anlamı ve çoğul biçim bilgisini karşılamaz.","preserves":"Üzerine yazılan veya yazı taşıyan tek yaprak çekirdeğini korur."},"facet_ids":["F001"],"text":"yazı yaprağı","usage_role":"general"},{"applicability":"Adın yazılı yapraklardan oluşan bir bütünü belirttiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":"Güncel kullanımda her türlü kitabı anlatabildiği için tarihsel malzeme sınırını tek başına göstermez.","fit":"narrowing","loses":"Tek yazı yaprağı çekirdeğini ve çoğul biçim bilgisini dışarıda bırakır.","preserves":"Yazılı yapraklar bütününe yönelik kitap kullanımını korur."},"facet_ids":["F002"],"text":"kitap","usage_role":"contextual"}],"definition":"Üzerine yazı yazılan veya yazı taşıyan yaprak ya da parçadır; kimi kullanımda bu tür yazılı yapraklardan oluşan kitabı da belirtir. Tekil adın çeşitli çoğul biçimleri vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, deri veya benzeri bir malzemeden olup üzerine yazı yazılan ya da yazı taşıyan tek yapraktır."},{"facet_id":"F002","role":"extension","statement":"Aynı ad kimi kullanımda yazılı yaprakların oluşturduğu kitap için de kullanılır."},{"facet_id":"F003","role":"source_variant","statement":"Kaynak ifadesi tekil yazı yaprağı için birden çok çoğul biçim bildirir."}],"identity_rationale":"Kaynak ifadesi dalı, üzerine yazı yazılan ya da yazı taşıyan tek yaprak ve kimi kullanımda kitap olarak açıkça tanımlar; ayrıca bunun çoğul biçimlerini verir. Sunulan yazılı yaprak çerçevesi bu içeriği doğru biçimde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yazı yazılan yaprak veya kitap"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yazı yaprakları"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yazı yaprakları"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yazı yaprakları için seyrek bir çoğul biçim"}],"lexicalization_note":"Tanım yalın yazı yaprağı anlamında kalır ve yalnızca kaynakta bulunan kitap genişlemesini içerir; başka dallardaki toplama işlemi tanıma taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yazı malzemesi, deri yaprak, içerikli yayın ve bağlı yaprak bütünüyle karışma olasılığını açıklayan dört karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal malzemeden bağımsız olarak yazı yaprağını ve kitap kullanımını kapsar; komşu dal ise yazı yüzeyini malzeme türü üzerinden adlandırır.","focus_only":"Odak dal yazı taşıyan yaprağı, kitap genişlemesini ve çoğul adlandırmaları kapsar.","gloss":"yazı kâğıdı","neighbor_only":"Komşu dal yazı malzemesini özellikle belirli bir bitkisel kâğıt türü veya başka malzemeler bakımından sınırlar.","neighbor_ref":"root_001218/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da üzerine yazı yazılan taşınabilir bir yüzeyi adlandırır."},{"boundary_match":"partial","distinction":"Odak dalın yazı yüzeyi farklı malzemelerden olabilir ve kitap anlamına genişleyebilir; komşu dalın çekirdeği ise belirli bir deri malzemesidir.","focus_only":"Odak dal genel yazı yaprağını, kitap kullanımını ve çoğul biçimleri kapsar.","gloss":"deri yazı yaprağı","neighbor_only":"Komşu dal özellikle işlenmiş deri yaprağını ve onun beyaz ya da açılmış durumunu belirtir.","neighbor_ref":"root_000586/B002","relation_type":"near_synonym","shared_zone":"Yazı yazmaya elverişli veya yazı taşıyan yaprak iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dalı belirleyen şey yazının taşındığı yapraktır; komşu dalda ise yayın veya bilgi içeriği daha belirleyici bir sınır oluşturur.","focus_only":"Odak dal herhangi bir yazı yaprağını veya genel olarak kitabı belirtebilir.","gloss":"bilgi yazısı veya dergi","neighbor_only":"Komşu dal bilgelik ya da bilgi içeriği taşıyan dergi, yaprak veya kitabı özellikle öne çıkarır.","neighbor_ref":"root_000255/B006","relation_type":"near_synonym","shared_zone":"Yazılı bir yaprak ya da kitap görünümü iki dalda da bulunur."},{"boundary_match":"partial","distinction":"Bu dal yaprağın kendisini adlandırır; komşu dal ise yaprakların iki kapak arasında bir araya getirilmesiyle oluşan bütünü kurucu özellik sayar.","focus_only":"Odak dal tek yazı yaprağını ve daha gevşek kitap kullanımını kapsar.","gloss":"bağlı yazı yaprakları bütünü","neighbor_only":"Komşu dal yazılı yaprakların iki kapak arasında toplanmış bütününü ve bu toplama işlemini gerektirir.","neighbor_ref":"root_000845/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalın ortak malzemesi yazılı yapraklardır."}],"source_phrase_ar":"الصحيفة وهي التي يكتب فيها والجمع صحائف والصحف (maqayis); الصحف جمع الصحيفة (ayn); الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها (jamhara); الصحيفة الكتاب والجمع صحف وصحائف (sihah); الصحيفة التي يكتب فيها وجمعها صحائف وصحف (mufradat)","source_summary":"Kaynaklar yazı yazılan yaprak veya parçayı ortak çekirdek olarak verir; kitap kullanımını ve tekil adın farklı çoğul biçimlerini de aynı dalda kaydeder.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"الصحيفة التي يكتب فيها والكتاب والصحف والصحائف","what_is_not_ar":"صحيفة الوجه والصحفة والمصحف والتصحيف"},"support_links":["sup_2993825d4d21a656ce4c","sup_bb076108e85095823972"]},{"boundary":"Kurucu sınır, yazılı yaprakların bir araya getirilip iki kapak arasında tutulmasıdır; tek yaprak, yalnız okuma eylemi veya metnin tek bir bölümü yeterli değildir.","branch_kind":"bare","branch_ref":"root_000845/B003","candidate_links":[{"candidate_id":"cand_1d0fa2a9cd13de36ef11","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صُحُف","morph_features":"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"87:19:1:1","qac_word_ref":"87:19:1","surface_ar":"صُحُفِ"}],"gloss":"iki kapak arasında toplanmış yazı yaprakları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sonuç nesnesi, yazılı yaprakların iki kapak arasında toplanmış bütünüdür."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu bütünü kuran eylem, yazılı yaprakları bir araya getirip kapaklar arasında toplamaktır."}}],"root_ar":"ص ح ف","root_id":"root_000845","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaprakların toplanmasıyla oluşan sonuç nesnesini bütün kurucu sınırlarıyla karşılar.","boundary_detail":"Kurucu sınır, yazılı yaprakların bir araya getirilip iki kapak arasında tutulmasıdır; tek yaprak, yalnız okuma eylemi veya metnin tek bir bölümü yeterli değildir.","branch_image_ar":"جمع الصحف في مصحف","concept_gloss":"iki kapak arasında toplanmış yazı yaprakları","contextual_glosses":[{"applicability":"Sonuç nesnesinden çok onu kuran toplama eyleminin anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yazılı yaprakların bir araya getirilmesi ve iki kapak arasında bütünleştirilmesi işlemini korur."},"facet_ids":["F002"],"text":"yazı yapraklarını iki kapak arasında toplamak","usage_role":"explanatory"},{"applicability":"İki kapak arasındaki sonuç nesnesinin kısa ve doğal biçimde anılması için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki kapak sınırını açıkça söylemez ve toplama eylemini karşılamaz.","preserves":"Yazılı yaprakların bağlı bir bütün oluşturması sonucunu korur."},"facet_ids":["F001"],"text":"bağlı yazı yaprakları bütünü","usage_role":"general"}],"definition":"Yazılı yaprakların bir araya getirilip iki kapak arasında tutulmasıyla oluşan bütündür. Aynı dal, yaprakları böyle bir bütün oluşturacak biçimde toplama eylemini de içerir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sonuç nesnesi, yazılı yaprakların iki kapak arasında toplanmış bütünüdür."},{"facet_id":"F002","role":"associated_use","statement":"Bu bütünü kuran eylem, yazılı yaprakları bir araya getirip kapaklar arasında toplamaktır."}],"identity_rationale":"Kaynak ifadesi hem yazılı yaprakların iki kapak arasında toplanması işlemini hem de bu işlemle ortaya çıkan toplanmış bütünü açıkça kurar. Sunulan dal kimliği bu işlem, düzenleme ve sonuç ilişkisini doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"iki kapak arasında toplanmış yazı yaprakları bütünü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yazı yapraklarını iki kapak arasında toplamak"}],"lexicalization_note":"Tanım kaynakta verilen yalın sonuç nesnesi ile onu kuran toplama eylemini korur; tek yaprak ya da genel toplama anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tek yaprak, genel toplama, okuma ve metin bölümüyle sınır farkını gösteren dört komşu yeterli bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın anlamında yaprakların toplanması ve kapaklar arasında bütünleşmesi kurucudur; komşu dalda tek yaprak başlı başına yeterlidir.","focus_only":"Odak dal, yazılı yaprakların iki kapak arasında toplanmış bir bütün oluşturmasını gerektirir.","gloss":"yazı yaprağı","neighbor_only":"Komşu dal tek yazı yaprağını ve genel kitap kullanımını, özel bir toplama işlemi gerektirmeden kapsar.","neighbor_ref":"root_000845/B002","relation_type":"near_neighbor","shared_zone":"Yazılı yaprak iki dalın ortak maddi öğesidir."},{"boundary_match":"partial","distinction":"Odak dalın katılımcıları yazılı yapraklardır ve sonuç kapaklı bir bütündür; komşu dalın toplama alanı genel olup böyle bir malzeme ve sonuç şartı taşımaz.","focus_only":"Odak dal yalnızca yazılı yaprakların kapaklar arasında düzenli biçimde toplanmasını ve sonucunu anlatır.","gloss":"toplama ve elde tutma","neighbor_only":"Komşu dal bir şeyi alma, ele geçirme, elde tutma veya genel olarak toplama eylemlerini kapsar.","neighbor_ref":"root_000018/B001","relation_type":"near_neighbor","shared_zone":"Birden çok şeyi bir araya getirme düşüncesi iki dalda ortaktır."},{"boundary_match":"field_only","distinction":"Odak dal metnin taşıyıcı yapraklarının fiziksel bütünleşmesini anlatırken komşu dal metnin okunmasını ve aktarılmasını anlatır; çekirdekleri ortak değildir.","focus_only":"Odak dal yazılı yaprakların kapaklar arasında toplanmasıyla oluşan nesneyi ve kurma işlemini anlatır.","gloss":"metni okuma","neighbor_only":"Komşu dal metni seslendirme, okuma, başkasına okutma ve birlikte çalışma eylemlerini kapsar.","neighbor_ref":"root_001211/B001","relation_type":"same_field","shared_zone":"Her iki dal yazılı metinlerin kullanıldığı bilgi alanına girer."},{"boundary_match":"field_only","distinction":"Odak dal metni taşıyan yaprakların bütününü kurar; komşu dal ise bu bütün içindeki sınırlı bir metin bölümünü adlandırabilir ve fiziksel toplama şartı taşımaz.","focus_only":"Odak dal, yazılı yaprakların tümünü taşıyan kapaklı fiziksel bütündür.","gloss":"sınırlı metin bölümü","neighbor_only":"Komşu dal metin içindeki çevrelenmiş bir bölümü ve ayrıca yüksek derece anlamını kapsar.","neighbor_ref":"root_000758/B003","relation_type":"same_field","shared_zone":"İki dal da düzenlenmiş yazılı metnin yapısal öğeleriyle ilgilidir."}],"source_phrase_ar":"سمي المصحف مصحفا لأنه أصحف أي جعل جامعا للصحف المكتوبة بين الدفتين (ayn); المصحف لأنه صحف جمعت (jamhara); مصحف مأخوذة من أصحف أي جمعت فيه الصحف (sihah); المصحف ما جعل جامعا للصحف المكتوبة (mufradat)","source_summary":"Kaynakların ortak anlatımı, yazılı yaprakların toplanarak iki kapak arasında bir bütün haline getirilmesini ve ortaya çıkan bağlı bütünü birlikte açıklar.","sources":["AY","JA","SI","MU"],"what_is_ar":"المصحف وما جمع فيه الصحف المكتوبة بين الدفتين","what_is_not_ar":"الصحيفة المفردة والصحفة والتصحيف"},"support_links":["sup_bac362581746d4dfb48c"]},{"boundary":"Çekirdek geniş, yayvan çanaktır; küçük su biriktirme çukurları ayrı bir uzantıdır ve yazı yaprağı ya da genel geniş yüzey anlamıyla karıştırılmamalıdır.","branch_kind":"bare","branch_ref":"root_000845/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صُحُف","morph_features":"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"87:19:1:1","qac_word_ref":"87:19:1","surface_ar":"صُحُفِ"}],"gloss":"yayvan çanak; küçük su biriktirme çukuru","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel nesne geniş ağızlı, basık ve yayvan bir çanaktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı ad ailesinin çoğul biçimi, su için yapılan küçük biriktirme çukurlarını da adlandırabilir."}}],"root_ar":"ص ح ف","root_id":"root_000845","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çanak çekirdeği ile aynı ad ailesindeki su biriktirme yeri uzantısını birbirine karıştırmadan birlikte gösterir.","boundary_detail":"Çekirdek geniş, yayvan çanaktır; küçük su biriktirme çukurları ayrı bir uzantıdır ve yazı yaprağı ya da genel geniş yüzey anlamıyla karıştırılmamalıdır.","branch_image_ar":"صَحفة عريضة","concept_gloss":"yayvan çanak; küçük su biriktirme çukuru","contextual_glosses":[{"applicability":"Geniş ağızlı ve basık kap çekirdeğinin söz konusu olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Küçük su biriktirme çukurlarına yönelik uzantıyı karşılamaz.","preserves":"Geniş ağızlı, basık ve yayvan kap çekirdeğini korur."},"facet_ids":["F001"],"text":"yayvan çanak","usage_role":"general"},{"applicability":"Ad ailesinin küçük su toplama yerlerini belirttiği özel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geniş ve yayvan çanak çekirdeğini karşılamaz.","preserves":"Su tutmak için yapılan küçük biriktirme yeri kullanımını korur."},"facet_ids":["F002"],"text":"küçük su biriktirme çukuru","usage_role":"contextual"}],"definition":"Geniş ağızlı, yayvan bir çanaktır. Aynı ad ailesindeki çoğul biçim ayrıca su tutmak için yapılan küçük biriktirme çukurlarını da belirtebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel nesne geniş ağızlı, basık ve yayvan bir çanaktır."},{"facet_id":"F002","role":"extension","statement":"Aynı ad ailesinin çoğul biçimi, su için yapılan küçük biriktirme çukurlarını da adlandırabilir."}],"identity_rationale":"Kaynak ifadesinin baskın gönderimi geniş ve yayvan bir çanaktır; aynı birleşik iddia ayrıca aynı ad ailesindeki çoğul biçimi küçük su biriktirme yerleri için de verir. Dal korunabilir, ancak ikinci gönderimin çanak tanımına özdeş değil, ona biçim ve işlev bakımından bağlı ayrı bir uzantı olduğu belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"geniş ve yayvan çanak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"geniş ve yayvan çanaklar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"su için yapılmış küçük biriktirme çukurları"}],"lexicalization_note":"Tanım yalın kap adını çekirdekte tutar ve kaynakta açıkça verilen küçük su biriktirme yeri kullanımını bağımlı bir uzantı olarak sınırlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kap biçimi, su tutma işlevi ve geniş yüzeyle karışabilecek sınırları gösteren dört komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kabın yayvan ve basık biçimini öne çıkarır ve su çukurlarına uzanır; komşu dal yemek sunma işlevini öne çıkarır ve küçük kuyu benzetmesine uzanır.","focus_only":"Odak dal yayvan çanağın yanında küçük su biriktirme çukurları uzantısını da kapsar.","gloss":"büyük yemek kabı","neighbor_only":"Komşu dal özellikle yemek konan büyük kabı ve ona benzetilen küçük kuyuyu kapsar.","neighbor_ref":"root_000250/B002","relation_type":"near_synonym","shared_zone":"Geniş bir yemek kabı iki dalın en yakın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dalda yayvan çanak biçimi kurucudur; komşu dalın kabı daha çok yıkama veya su tutma işleviyle belirlenen leğen ya da tekne türündedir.","focus_only":"Odak dal geniş, yayvan çanağı ve küçük su biriktirme çukurlarını adlandırır.","gloss":"leğen veya tekne","neighbor_only":"Komşu dal su veya çamaşır için kullanılan daha derin tekne ve leğen türlerini kapsar.","neighbor_ref":"root_000596/B003","relation_type":"near_synonym","shared_zone":"Su ya da başka bir içerik tutan geniş kap görünümü iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Odak dal biçimce yayvan çanakla sınırlı bir çekirdeğe sahiptir; komşu dal ise biçimden çok toplama işlevi çevresinde farklı kap ve yer türlerini birleştirir.","focus_only":"Odak dal belirli olarak yayvan çanağı ve küçük su biriktirme çukurunu kapsar.","gloss":"su veya yemek toplayan kap","neighbor_only":"Komşu dal bardak, havuz, kap, oluk ve oyulmuş toplama yeri gibi çok çeşitli su veya yemek toplayıcılarını kapsar.","neighbor_ref":"root_001222/B004","relation_type":"near_neighbor","shared_zone":"Bir sıvıyı ya da yemeği içinde toplama işlevi iki dalda kesişir."},{"boundary_match":"partial","distinction":"Odak dal somut bir kap veya su biriktirme yeridir; komşu dal ise genel yüzey genişliğini anlatır ve kap olma şartı taşımaz.","focus_only":"Odak dal genişliğin kendisini değil, geniş ve basık belirli bir kap türünü adlandırır.","gloss":"yayılmış geniş yüzey","neighbor_only":"Komşu dal bir şeydeki yayılma ve geniş yüzeyi, yeryüzü ve yüz derisi kullanımlarıyla birlikte anlatır.","neighbor_ref":"root_000845/B001","relation_type":"near_neighbor","shared_zone":"Yayvan kabın geniş ve açılmış yüzeyi, iki dal arasında biçimsel bir yakınlık kurar."}],"source_phrase_ar":"الصحفة القصعة المسلنطحة (maqayis); الصحاف مناقع صغار تتخذ للماء (maqayis); الصحفة شبه القصعة المسلنطحة العريضة (ayn); الصحفة القصعة وتجمع صحافا (jamhara); الصحفة كالقصعة والجمع صحاف (sihah); الصحفة مثل قصعة عريضة (mufradat)","source_summary":"Birleşik kaynak anlatımı geniş ve yayvan çanağı ortak çekirdek olarak verir; ayrıca aynı ad ailesinin küçük su biriktirme yerlerine yönelen ayrı kullanımını kaydeder.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"الصَّحفة القصعة العريضة المسلنطحة والصحاف مناقع صغار للماء","what_is_not_ar":"الصحيفة المكتوبة والمصحف وصحيفة الوجه والتصحيف"},"support_links":[]},{"boundary":"Dal yalnız genel yanılmayı değil, harf benzerliğinin doğurduğu yanlış okuma veya aktarımı ve buna bağlı kişi adlandırmasını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000845/B005","candidate_links":[{"candidate_id":"cand_18576204d5386030822e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صُحُف","morph_features":"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"87:19:1:1","qac_word_ref":"87:19:1","surface_ar":"صُحُفِ"}],"gloss":"harf benzerliğinden doğan yanlış okuma veya aktarım","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kurucu olay, benzer harflerin karıştırılması yüzünden yazılı metnin yanlış okunması veya yanlış aktarılmasıdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlı kişi kullanımı, yazılı metni benzer harfleri karıştırarak yanlış aktaran kimseyi belirtir."}}],"root_ar":"ص ح ف","root_id":"root_000845","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hatanın nedenini, okuma aşamasını ve yanlış aktarım sonucunu birlikte karşılayan genel açıklamadır.","boundary_detail":"Dal yalnız genel yanılmayı değil, harf benzerliğinin doğurduğu yanlış okuma veya aktarımı ve buna bağlı kişi adlandırmasını kapsar.","branch_image_ar":"تصحيف القراءة","concept_gloss":"harf benzerliğinden doğan yanlış okuma veya aktarım","contextual_glosses":[{"applicability":"Hatanın doğrudan okuma sırasında gerçekleştiği bağlamlarda doğal bir eylem karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yanlış okumanın başkasına aktarılması sonucunu ve kişi kullanımını karşılamaz.","preserves":"Benzer harflerin karıştırılmasıyla oluşan yanlış okuma olayını korur."},"facet_ids":["F001"],"text":"benzer harfleri karıştırarak yanlış okumak","usage_role":"general"},{"applicability":"Benzer harfleri karıştırdığı için okuduğu metni yanlış aktaran kişiden söz edilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":"Neden açıkça belirtilmezse başka tür aktarım yanlışlarını da çağrıştırabilir.","fit":"narrowing","loses":"Tek başına olay adı olarak yanlış okuma ve aktarım sürecini karşılamaz.","preserves":"Yanlış okumayı aktarımına taşıyan kişi kullanımını korur."},"facet_ids":["F002"],"text":"metni yanlış aktaran kişi","usage_role":"contextual"}],"definition":"Yazılı bir metni, birbirine benzeyen harfleri karıştırarak yanlış okumak veya aslından farklı aktarmaktır. Aynı dal, bu tür bir okuma hatasını aktarımında yapan kişiyi de niteleyebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kurucu olay, benzer harflerin karıştırılması yüzünden yazılı metnin yanlış okunması veya yanlış aktarılmasıdır."},{"facet_id":"F002","role":"associated_use","statement":"Bağlı kişi kullanımı, yazılı metni benzer harfleri karıştırarak yanlış aktaran kimseyi belirtir."}],"identity_rationale":"Kaynak ifadesinin ana çekirdeği, birbirine benzeyen harfler yüzünden yazılı metni yanlış okumak veya aslından farklı aktarmaktır. Sunulan çerçeve doğrudur; ancak kaynak ayrıca bu hatayı yapan aktarıcıyı belirten bağlı bir kişi kullanımını da içerdiğinden sınır buna göre genişletilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"benzer harfleri karıştırmaktan doğan yanlış okuma veya aktarım"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"benzer harfleri karıştırıp metni yanlış aktaran kişi"}],"lexicalization_note":"Tanım olay çekirdeğini, harf benzerliği koşulunu ve yanlışı aktaran kişiye özgü bağlı kullanımı ayrı tutar; genel belirsizlik anlamına genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ayırt edici işaretle karşıtlık ve genel benzerlik, belirsizleştirme ile karışıklık sınırlarını gösteren dört komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal ayırt edememenin doğurduğu hatalı sonucu, komşu dal ise harfleri işaretleyerek aynı belirsizliği ortadan kaldıran karşıt işlemi anlatır.","focus_only":"Odak dal, harf benzerliğinin giderilememesi yüzünden ortaya çıkan yanlış okuma veya aktarımı anlatır.","gloss":"harfleri ayırt edici işaretleme","neighbor_only":"Komşu dal, işaret veya noktalar ekleyerek harfler arasındaki belirsizliği giderme işlemini anlatır.","neighbor_ref":"root_000988/B002","relation_type":"polarity_pair","shared_zone":"İki dalın ortak ekseni, yazıdaki benzer harflerin ayırt edilmesi veya karıştırılmasıdır."},{"boundary_match":"partial","distinction":"Odak dal yazıdaki harflerin karışmasına ve metnin yanlış okunmasına bağlıdır; komşu dal ise yazı şartı olmadan daha genel kuşku ve benzerlik durumlarını kapsar.","focus_only":"Odak dal yazılı metinde benzer harflerden doğan belirli bir okuma ve aktarım hatasıdır.","gloss":"benzerlikten doğan kuşku","neighbor_only":"Komşu dal sanı, kuruntu, genel benzerlik, belirsizlik ve bir kişiden kuşkulanma alanlarını kapsar.","neighbor_ref":"root_000454/B005","relation_type":"near_neighbor","shared_zone":"Benzer görünen şeylerin birbirine karıştırılması iki dalda ortak bir bilişsel zemindir."},{"boundary_match":"partial","distinction":"Odak dal okuyucunun harf benzerliği yüzünden düştüğü hatadır; komşu dal ise nesne veya anlam üzerinde belirsizlik yaratan işlemi anlatır.","focus_only":"Odak dal benzer harfleri karıştıran okuyucunun yaptığı somut okuma veya aktarım hatasıdır.","gloss":"anlamı belirsizleştirme","neighbor_only":"Komşu dal bir şeyi ya da sözün anlamını başkası için bilerek veya fiilen kapalı ve karışık hale getirmeyi anlatır.","neighbor_ref":"root_001049/B004","relation_type":"near_neighbor","shared_zone":"Bir metnin anlaşılmasını zorlaştıran karışıklık iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal yazıya, harf benzerliğine ve okuma sonucuna özgüdür; komşu dal daha genel bir karıştırma ve belirsizleşme alanına sahiptir.","focus_only":"Odak dalın koşulu yazılı harflerin birbirine benzemesi, sonucu ise yanlış okuma veya aktarımdır.","gloss":"karıştırıp belirsizleştirme","neighbor_only":"Komşu dal herhangi bir işin, anlatımın veya karanlığın karışıp belirsizleşmesini genel olarak kapsar.","neighbor_ref":"root_001341/B003","relation_type":"near_neighbor","shared_zone":"Karışıklığın doğru ayrımı engellemesi her iki dalda da bulunur."}],"source_phrase_ar":"الصحفي الذي يروي الخطأ عن قراءة الصحف بأشباه الحروف (ayn); التصحيف الخطأ في الصحيفة (sihah); التصحيف قراءة المصحف وروايته على غير ما هو لاشتباه حروفه (mufradat)","source_summary":"Kaynakların birleşik anlatımı, benzer harflerin karıştırılmasıyla doğan yanlış okuma veya aktarımı temel alır ve bu yanlışı aktaran kişiyi belirten kullanımı da içerir.","sources":["AY","SI","MU"],"what_is_ar":"التصحيف والخطأ في قراءة الصحف أو المصحف لاشتباه الحروف","what_is_not_ar":"الصحيفة المكتوبة نفسها والمصحف نفسه والصحفة"},"support_links":["sup_2993825d4d21a656ce4c"]}],"candidate_inventory":[{"anchor_refs":["87:19:1"],"branch_refs":[],"candidate_id":"cand_ec1351498e6a5b2bcce9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:19:1:appositional-archive-resolution","source_type":"word_analysis","support_ids":["sup_3cf8050f7b6733b707c6","sup_4567fda16442ceddd869"],"title":"genitive apposition resolves the prior archive claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:1","qac_refs":["87:19:1:1"],"status":"accepted"}},{"anchor_refs":["87:19:1"],"branch_refs":[],"candidate_id":"cand_2630aa56bfd2c8e90b7e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:19:1:archive-field-and-cadence","source_type":"word_analysis","support_ids":["sup_20c7779ae314159317ae","sup_4567fda16442ceddd869"],"title":"rare archive term with compressed cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:1","qac_refs":["87:19:1:1"],"status":"accepted"}},{"anchor_refs":["87:19:1"],"branch_refs":[],"candidate_id":"cand_dd522dc6d6799e8b946e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:19:1:cross-boundary-narrowing-reprise","source_type":"word_analysis","support_ids":["sup_092fdb40ebb556a013e8","sup_4567fda16442ceddd869"],"title":"same archive noun narrows 87:18","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:1","qac_refs":["87:19:1:1"],"status":"accepted"}},{"anchor_refs":["87:19:1"],"branch_refs":[],"candidate_id":"cand_01be157215c0d3695513","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:19:1:plural-construct-specificity","source_type":"word_analysis","support_ids":["sup_4567fda16442ceddd869","sup_f6be9b8c2e17fdfb086d"],"title":"plural construct binds two named possessors","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:1","qac_refs":["87:19:1:1"],"status":"accepted"}},{"anchor_refs":["87:19:1"],"branch_refs":[],"candidate_id":"cand_56d228856cb64ef2655a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:19:1:written-record-materiality","source_type":"word_analysis","support_ids":["sup_4567fda16442ceddd869","sup_9f7290714cb3b5538023"],"title":"written sheets as scriptural witness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:1","qac_refs":["87:19:1:1"],"status":"accepted"}},{"anchor_refs":["87:19:2"],"branch_refs":[],"candidate_id":"cand_081ccb043f5cfbd2d80e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:19:2:diptote-genitive-provenance","source_type":"word_analysis","support_ids":["sup_1e035f545158f6114e2c","sup_43e24ae3d044261cd84c"],"title":"fatḥa-marked genitive under the archive head","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:2","qac_refs":["87:19:2:1"],"status":"accepted"}},{"anchor_refs":["87:19:2"],"branch_refs":[],"candidate_id":"cand_4c9c02c1542169a0a333","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:19:2:first-restrictor-and-lineage-shift","source_type":"word_analysis","support_ids":["sup_43e24ae3d044261cd84c","sup_cf7f1a3e860ca9bbff41"],"title":"Abrahamic witness starts the named restriction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:2","qac_refs":["87:19:2:1"],"status":"accepted"}},{"anchor_refs":["87:19:2"],"branch_refs":[],"candidate_id":"cand_af540fcff019eecae15d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:19:2:ordered-pair-continuity","source_type":"word_analysis","support_ids":["sup_43e24ae3d044261cd84c","sup_aa387fb2aa70d8c5146f"],"title":"first member of the Abraham-Moses pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:2","qac_refs":["87:19:2:1"],"status":"accepted"}},{"anchor_refs":["87:19:2"],"branch_refs":[],"candidate_id":"cand_3889c0204b50978b4b86","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:19:2:proper-name-witness-not-derivation","source_type":"word_analysis","support_ids":["sup_43e24ae3d044261cd84c","sup_95d091f2ebc475f60a22"],"title":"recognized witness, not Arabic root play","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:2","qac_refs":["87:19:2:1"],"status":"accepted"}},{"anchor_refs":["87:19:2"],"branch_refs":[],"candidate_id":"cand_f4dc844812149d8160eb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:19:2:vocalic-stability-and-cadence","source_type":"word_analysis","support_ids":["sup_43e24ae3d044261cd84c","sup_7f186053fe678e2b2680"],"title":"stable referent through vowel and cadence variation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:2","qac_refs":["87:19:2:1"],"status":"accepted"}},{"anchor_refs":["87:19:3"],"branch_refs":[],"candidate_id":"cand_731c4bcdb380a936c360","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:19:3:compact-witness-pair-binder","source_type":"word_analysis","support_ids":["sup_1632eb615975c37be1e2","sup_5c76b71b7098ff799514"],"title":"compact hinge into the second witness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:3","qac_refs":["87:19:3:1"],"status":"accepted"}},{"anchor_refs":["87:19:3"],"branch_refs":[],"candidate_id":"cand_86addae317acce84bdde","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:19:3:shared-genitive-coordination","source_type":"word_analysis","support_ids":["sup_1632eb615975c37be1e2","sup_601e031cc2872107a5da"],"title":"coordinates two genitive dependents","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:3","qac_refs":["87:19:3:1"],"status":"accepted"}},{"anchor_refs":["87:19:3"],"branch_refs":[],"candidate_id":"cand_0144995e0b8f1b166531","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:19:3:surface-fusion-and-wasl","source_type":"word_analysis","support_ids":["sup_1632eb615975c37be1e2","sup_8d091e35a8934324f8f8"],"title":"segmented particle, fused recitation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:3","qac_refs":["87:19:3:1"],"status":"accepted"}},{"anchor_refs":["87:19:4"],"branch_refs":[],"candidate_id":"cand_812985b6a1a95b55b038","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:19:4:coordinated-genitive-inheritance","source_type":"word_analysis","support_ids":["sup_572fd27908bfc471b483","sup_609fdbe0d74eea494ee3"],"title":"hidden-case name inherits genitive force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:4","qac_refs":["87:19:3:2"],"status":"accepted"}},{"anchor_refs":["87:19:4"],"branch_refs":[],"candidate_id":"cand_d004b1a1926e4dd26bda","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:19:4:final-archive-seal","source_type":"word_analysis","support_ids":["sup_609fdbe0d74eea494ee3","sup_b07b2ec383c147c708b5"],"title":"final named witness seals the surah","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:4","qac_refs":["87:19:3:2"],"status":"accepted"}},{"anchor_refs":["87:19:4"],"branch_refs":[],"candidate_id":"cand_aa64aeffaca70bf4771c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:19:4:foreign-name-mosaic-witness","source_type":"word_analysis","support_ids":["sup_609fdbe0d74eea494ee3","sup_c1a92b0a3eb4875beedf"],"title":"foreign proper name as Mosaic witness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:4","qac_refs":["87:19:3:2"],"status":"accepted"}},{"anchor_refs":["87:19:4"],"branch_refs":[],"candidate_id":"cand_85a162b21c1fad3fd9ef","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:19:4:long-a-cadence-closure","source_type":"word_analysis","support_ids":["sup_609fdbe0d74eea494ee3","sup_eb257b3bfdbc3f9f100f"],"title":"long ā landing closes the citation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:4","qac_refs":["87:19:3:2"],"status":"accepted"}},{"anchor_refs":["87:19:4"],"branch_refs":[],"candidate_id":"cand_a4b075a725d5c5bbcaab","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"87:19:4:mosaic-record-recurrence","source_type":"word_analysis","support_ids":["sup_609fdbe0d74eea494ee3","sup_d14cf12a6e98eb3f2b2d"],"title":"Mosaic records recalled in closing identification","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"87:19:4","qac_refs":["87:19:3:2"],"status":"accepted"}},{"anchor_refs":["87:19:1"],"branch_refs":[],"candidate_id":"cand_dc80ae247d365a819141","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000845"],"scope":"focus_ayah","source_local_id":"87:19:1:1","source_type":"qac_morpheme","support_ids":["sup_d2e6cd68eb6fb99b3786"],"title":"QAC root occurrence: ص ح ف","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["87:19"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:19","branch_refs":["root_000845/B002"],"candidate_id":"cand_e4935c28add11ce9520b","commentary_obligation":"review","hft_ref":"hft_0d873dfcfa4bb77a2959","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_named_written_witnesses","source_type":"hft","support_ids":["sup_bb076108e85095823972"],"title":"base_named_written_witnesses","trust":"legacy_unbound"},{"anchor_refs":["87:19"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:19","branch_refs":["root_000845/B001"],"candidate_id":"cand_7737c28a091844963ab6","commentary_obligation":"review","hft_ref":"hft_fc8d4c518b58cdf81b06","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_open_spread_surfaces","source_type":"hft","support_ids":["sup_ced24621bc9f51de9f7f"],"title":"base_open_spread_surfaces","trust":"legacy_unbound"},{"anchor_refs":["87:19"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:19","branch_refs":["root_000845/B003"],"candidate_id":"cand_1d0fa2a9cd13de36ef11","commentary_obligation":"review","hft_ref":"hft_03eb360a26bb91bb5b46","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_collectable_plural_archive","source_type":"hft","support_ids":["sup_bac362581746d4dfb48c"],"title":"base_collectable_plural_archive","trust":"legacy_unbound"},{"anchor_refs":["87:19"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"87:19","branch_refs":["root_000845/B002","root_000845/B005"],"candidate_id":"cand_18576204d5386030822e","commentary_obligation":"review","hft_ref":"hft_d255c4ed96347b36c3bc","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_preservation_with_graphic_risk","source_type":"hft","support_ids":["sup_2993825d4d21a656ce4c"],"title":"base_preservation_with_graphic_risk","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ","qac_morphemes":[{"lemma_ar":"صُحُف","morph_features":"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"87:19:1:1","qac_word_ref":"87:19:1","root_ar":"ص ح ف","surface_ar":"صُحُفِ"},{"lemma_ar":"إِبْرَاهِيم","morph_features":"STEM|POS:PN|LEM:<iboraAhiym|M|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"87:19:2:1","qac_word_ref":"87:19:2","root_ar":"","surface_ar":"إِبْرَٰهِيمَ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:19:3:1","qac_word_ref":"87:19:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مُوسَىٰ","morph_features":"STEM|POS:PN|LEM:muwsaY`|M|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"87:19:3:2","qac_word_ref":"87:19:3","root_ar":"","surface_ar":"مُوسَىٰ"}],"word_analysis_qac_refs":[["87:19:1:1"],["87:19:2:1"],["87:19:3:1"],["87:19:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["87:19:1","87:19:2","87:19:3","87:19:4"]},"focus_surface_evidence":{"arabic_uthmani":"صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ","qac_morphemes":[{"lemma_ar":"صُحُف","morph_features":"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"87:19:1:1","qac_word_ref":"87:19:1","root_ar":"ص ح ف","surface_ar":"صُحُفِ"},{"lemma_ar":"إِبْرَاهِيم","morph_features":"STEM|POS:PN|LEM:<iboraAhiym|M|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"87:19:2:1","qac_word_ref":"87:19:2","root_ar":"","surface_ar":"إِبْرَٰهِيمَ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"87:19:3:1","qac_word_ref":"87:19:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مُوسَىٰ","morph_features":"STEM|POS:PN|LEM:muwsaY`|M|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"87:19:3:2","qac_word_ref":"87:19:3","root_ar":"","surface_ar":"مُوسَىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["87:19:1:1"],["87:19:2:1"],["87:19:3:1"],["87:19:3:2"]],"word_analysis_refs":["87:19:1","87:19:2","87:19:3","87:19:4"],"word_rows":[{"analysis_record_ref":"87:19:1","analytic_gloss_range_en":"written prophetic records named as appositional specification of the earlier archive phrase; plural construct form keeps material record, scriptural content, and named provenance together","analytic_root_gloss_range_en":"root range includes flat surface, written sheet, collected written sheets or codex, broad shallow vessel, and scribal misreading from written sheets; the local phrase selects the written-record/archive branch","qac_refs":["87:19:1:1"],"root":{"arabic":"ص ح ف","transliteration":"ṣ-ḥ-f"},"surface":{"arabic":"صُحُفِ","transliteration":"ṣuḥufi"}},{"analysis_record_ref":"87:19:2","analytic_gloss_range_en":"proper name functioning as the first named archive witness and genitive complement under the record head; its authority is referential and provenance-bearing, not derived from an Arabic root sense","analytic_root_gloss_range_en":"dictionary material includes fixed gaze, plant budding, the foreign proper name Ibrahim and its variants, and Brahmins as a named community; the local word selects the proper-name branch only","qac_refs":["87:19:2:1"],"root":{"arabic":"ب ر ه م","transliteration":"b-r-h-m"},"surface":{"arabic":"إِبْرَٰهِيمَ","transliteration":"ibrāhīma"}},{"analysis_record_ref":"87:19:3","analytic_gloss_range_en":"coordinating particle that adds Moses to Abraham under the same archive head; locally it creates shared genitive governance and a compact two-name witness pair rather than a new clause","analytic_root_gloss_range_en":null,"qac_refs":["87:19:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"87:19:4","analytic_gloss_range_en":"foreign proper name functioning as the second coordinated archive witness; its final position completes the pair, inherits genitive force through coordination, and seals the surah on named Mosaic textual authority","analytic_root_gloss_range_en":null,"qac_refs":["87:19:3:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"مُوسَىٰ","transliteration":"mūsā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["87:19"],"branch_refs":["root_000845/B002"],"candidate_id":"cand_e4935c28add11ce9520b","evidence_scope":"focus_ayah","hft_ref":"hft_0d873dfcfa4bb77a2959","item_id":"base_named_written_witnesses","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_named_written_witnesses","support_id":"sup_bb076108e85095823972"},{"anchor_refs":["87:19"],"branch_refs":["root_000845/B001"],"candidate_id":"cand_7737c28a091844963ab6","evidence_scope":"focus_ayah","hft_ref":"hft_fc8d4c518b58cdf81b06","item_id":"base_open_spread_surfaces","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_open_spread_surfaces","support_id":"sup_ced24621bc9f51de9f7f"},{"anchor_refs":["87:19"],"branch_refs":["root_000845/B003"],"candidate_id":"cand_1d0fa2a9cd13de36ef11","evidence_scope":"focus_ayah","hft_ref":"hft_03eb360a26bb91bb5b46","item_id":"base_collectable_plural_archive","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_collectable_plural_archive","support_id":"sup_bac362581746d4dfb48c"},{"anchor_refs":["87:19"],"branch_refs":["root_000845/B002","root_000845/B005"],"candidate_id":"cand_18576204d5386030822e","evidence_scope":"focus_ayah","hft_ref":"hft_d255c4ed96347b36c3bc","item_id":"base_preservation_with_graphic_risk","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_preservation_with_graphic_risk","support_id":"sup_2993825d4d21a656ce4c"}],"diagnostics":[],"lane_counts":{"global":8,"macro":11,"micro":4},"packet_summary":{"ayah_count":19,"focus_ref":"87:19","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ء ث ر","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":true,"target_occurrences":9,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]}],"window":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"87:19","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"87:19","lane":"micro","linguistic_source_ref":"87:19","surface_ref":"87:19","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"87:19","target_tokens":[["İbrahim'in",["87:19:2"]],["ve",["87:19:3"]],["Musa'nın",["87:19:3"]],["sayfalarında",["87:19:1"]]],"text":"İbrahim'in ve Musa'nın sayfalarında."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s087-p01-001-019","label":"Whole surah","number":1,"refs":["87:1","87:2","87:3","87:4","87:5","87:6","87:7","87:8","87:9","87:10","87:11","87:12","87:13","87:14","87:15","87:16","87:17","87:18","87:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:1:cross-boundary-narrowing-reprise","source_type":"word_analysis","support_id":"sup_092fdb40ebb556a013e8","text":"{\"blocking_evidence\":null,\"headline\":\"same archive noun narrows 87:18\",\"reader_payoff\":\"The reader notices the repeated archive noun crossing the ayah boundary: the broad former records in 87:18 become named prophetic provenance in 87:19.\",\"reason\":\"The immediate prior ayah contains the earlier archive phrase, and the current noun repeats the same root in a dependent identifying phrase.\",\"representative_source_ids\":[\"QI-8b055a37\",\"QE-df623a8d\",\"ME-641344d6\",\"QB-b3d35bf9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:3","source_type":"word_analysis","support_id":"sup_1632eb615975c37be1e2","text":"{\"gloss_range\":\"coordinating particle that adds Moses to Abraham under the same archive head; locally it creates shared genitive governance and a compact two-name witness pair rather than a new clause\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) is small, but it carries the phrase from the first named witness to the second without repeating the archive noun. It coordinates dependents under the same {{ar:صُحُفِ}} ({{tr:ṣuḥufi}}) head, so Moses is added as co-possessor or source, not as a new sentence. Because the particle is segmented analytically while fused to the following name in recitation, it makes the join visible in grammar and audible in the surface. The result is not just \\\"and\\\" as addition; it is shared governance, compactness, and equality of attachment inside one closing archive phrase.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:2:diptote-genitive-provenance","source_type":"word_analysis","support_id":"sup_1e035f545158f6114e2c","text":"{\"blocking_evidence\":null,\"headline\":\"fatḥa-marked genitive under the archive head\",\"reader_payoff\":\"The reader notices that Abraham is grammatically dependent on the archive noun even though the case relation is not shown by the expected kasra.\",\"reason\":\"QAC identifies the proper noun as diptote genitive under {{ar:صُحُفِ}} ({{tr:ṣuḥufi}}), and attachment evidence marks it as the genitive complement.\",\"representative_source_ids\":[\"QG-8a96492a\",\"QG-ac2fa9a6\",\"MG-2810b78e\",\"QF-fd8e8be5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:1:archive-field-and-cadence","source_type":"word_analysis","support_id":"sup_20c7779ae314159317ae","text":"{\"blocking_evidence\":null,\"headline\":\"rare archive term with compressed cadence\",\"reader_payoff\":\"The reader notices that the closing phrase uses a constrained archive term also seen in record scenes, while variant compression changes pacing rather than reference.\",\"reason\":\"The source rows give concrete record-field references in 80:13 and 81:10 and an accepted recitational compression; neither changes the local construct archive sense.\",\"representative_source_ids\":[\"MI-7775f790\",\"QF-1c22f618\",\"QP-ec907291\",\"QH-c2e0bad7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:1:appositional-archive-resolution","source_type":"word_analysis","support_id":"sup_3cf8050f7b6733b707c6","text":"{\"blocking_evidence\":null,\"headline\":\"genitive apposition resolves the prior archive claim\",\"reader_payoff\":\"The reader notices that the final ayah identifies the archive named broadly in 87:18 rather than launching a separate list.\",\"reason\":\"QAC marks the noun as genitive/appositive, and translation support warns that the phrase should be read with the 87:18 window.\",\"representative_source_ids\":[\"QG-41cb015a\",\"MG-b0e1151e\",\"QT-cc5a172e\",\"QY-bde928e0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:2","source_type":"word_analysis","support_id":"sup_43e24ae3d044261cd84c","text":"{\"gloss_range\":\"proper name functioning as the first named archive witness and genitive complement under the record head; its authority is referential and provenance-bearing, not derived from an Arabic root sense\",\"prose\":\"{{ar:إِبْرَٰهِيمَ}} ({{tr:ibrāhīma}}) is the first named restrictor of the archive phrase, beginning a shared category that the second name will complete rather than standing as a separate archive title. The fatḥa ending does not free it from genitive dependence; as a diptote proper name, its relation is recovered from the construct head rather than from a visible kasra. Its payoff is not Arabic wordplay from {{ar:ب ر ه م}} ({{tr:b-r-h-m}}), but recognized prophetic provenance: the record is associated with Abraham as witness. That matters because the name often carries lineage or community discourse elsewhere, while here it shifts into textual witness (2:130; 16:123). Its long-vowel shape and accepted vocalic variants affect acoustic weight before {{ar:وَ مُوسَىٰ}} ({{tr:wa mūsā}}), but the referent and genitive role stay stable.\",\"root_display\":\"{{ar:ب ر ه م}} ({{tr:b-r-h-m}})\",\"root_gloss_range\":\"dictionary material includes fixed gaze, plant budding, the foreign proper name Ibrahim and its variants, and Brahmins as a named community; the local word selects the proper-name branch only\",\"surface_display\":\"{{ar:إِبْرَٰهِيمَ}} ({{tr:ibrāhīma}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:1","source_type":"word_analysis","support_id":"sup_4567fda16442ceddd869","text":"{\"gloss_range\":\"written prophetic records named as appositional specification of the earlier archive phrase; plural construct form keeps material record, scriptural content, and named provenance together\",\"prose\":\"{{ar:صُحُفِ}} ({{tr:ṣuḥufi}}) opens the final ayah as a dependent specification, not as a new subject. Its genitive shape sends the reader back to the archive claim in 87:18, so the broad earlier records are now identified as the records of the two named witnesses. The word stays concrete: these are written record-bearing sheets, not abstract doctrine detached from archival witness, and the constrained archive term belongs to a field of honored or opened records (80:13; 81:10). As a plural construct, it can gather more than one written record and bind both names under one archive category, while the proper-name dependents make the anarthrous noun specific. The optional compressed reading {{ar:صُحْفِ}} ({{tr:ṣuḥfi}}) tightens the onset before the first long proper name without changing the reference, case role, or written-record root.\",\"root_display\":\"{{ar:ص ح ف}} ({{tr:ṣ-ḥ-f}})\",\"root_gloss_range\":\"root range includes flat surface, written sheet, collected written sheets or codex, broad shallow vessel, and scribal misreading from written sheets; the local phrase selects the written-record/archive branch\",\"surface_display\":\"{{ar:صُحُفِ}} ({{tr:ṣuḥufi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:4:coordinated-genitive-inheritance","source_type":"word_analysis","support_id":"sup_572fd27908bfc471b483","text":"{\"blocking_evidence\":null,\"headline\":\"hidden-case name inherits genitive force\",\"reader_payoff\":\"The reader notices that Moses is grammatically dependent on the archive noun even though his ending does not show the case vowel.\",\"reason\":\"QAC notes genitive coordination with masked case, and attachment evidence makes the name a coordinated dependent of the archive head.\",\"representative_source_ids\":[\"QG-040369e3\",\"QG-e422231c\",\"MG-f8c61a54\",\"QF-3bd9e8e8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:3:compact-witness-pair-binder","source_type":"word_analysis","support_id":"sup_5c76b71b7098ff799514","text":"{\"blocking_evidence\":null,\"headline\":\"compact hinge into the second witness\",\"reader_payoff\":\"The reader notices the phrase becoming a two-member witness unit while the head noun remains unrepeated.\",\"reason\":\"The local syntax has one archive head and two coordinated names, so the conjunction preserves compactness while completing the former-record specification.\",\"representative_source_ids\":[\"QT-2df64402\",\"MT-7d77fd6b\",\"QE-33fedbd8\",\"QB-ba38912f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:3:shared-genitive-coordination","source_type":"word_analysis","support_id":"sup_601e031cc2872107a5da","text":"{\"blocking_evidence\":null,\"headline\":\"coordinates two genitive dependents\",\"reader_payoff\":\"The reader notices that the particle makes both names share the same archive relation instead of starting a separate claim.\",\"reason\":\"Attachment evidence coordinates {{ar:مُوسَىٰ}} ({{tr:mūsā}}) with {{ar:إِبْرَٰهِيمَ}} ({{tr:ibrāhīma}}) under the same head noun.\",\"representative_source_ids\":[\"QG-552587fb\",\"MG-d02129f0\",\"QS-13b5b28e\",\"QY-938c657a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:4","source_type":"word_analysis","support_id":"sup_609fdbe0d74eea494ee3","text":"{\"gloss_range\":\"foreign proper name functioning as the second coordinated archive witness; its final position completes the pair, inherits genitive force through coordination, and seals the surah on named Mosaic textual authority\",\"prose\":\"{{ar:مُوسَىٰ}} ({{tr:mūsā}}) completes the archive pair. Its final alif maqṣūra hides case, so the genitive relation must be recovered from {{ar:وَ}} ({{tr:wa}}), position, and the shared {{ar:صُحُفِ}} ({{tr:ṣuḥufi}}) head. Like the first name, it works by recognized prophetic authority rather than Arabic derivation, and its foreign-name shape helps keep that onomastic force clear. The word also carries a pointed recurrence: the Mosaic records are invoked at 53:36, and here the same archive field becomes the surah's closing identification. As the final word, its long ā landing completes the two-name cadence and lets the whole surah close by turning the preceding assertion into cited prophetic witness rather than a new command or threat.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مُوسَىٰ}} ({{tr:mūsā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:2:vocalic-stability-and-cadence","source_type":"word_analysis","support_id":"sup_7f186053fe678e2b2680","text":"{\"blocking_evidence\":null,\"headline\":\"stable referent through vowel and cadence variation\",\"reader_payoff\":\"The reader notices that qirāʾāt and long-vowel cadence can reshape the heard name while leaving its referential witness role stable.\",\"reason\":\"The variant rows concern sound-form and pacing, while the dictionary and local grammar keep the proper-name reference and genitive role unchanged.\",\"representative_source_ids\":[\"QF-3a882d5d\",\"MF-ffec9f00\",\"QP-59839f58\",\"QH-15275d5a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:3:surface-fusion-and-wasl","source_type":"word_analysis","support_id":"sup_8d091e35a8934324f8f8","text":"{\"blocking_evidence\":null,\"headline\":\"segmented particle, fused recitation\",\"reader_payoff\":\"The reader notices that the join is both analytically visible and audibly fused to the final name, making detachment less available.\",\"reason\":\"The bundle segments {{ar:وَ}} ({{tr:wa}}) as a particle while the source rows track its prefixed surface and waṣl effect before the second name.\",\"representative_source_ids\":[\"QF-80c7e590\",\"QT-590c4f13\",\"QP-e503692c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:2:proper-name-witness-not-derivation","source_type":"word_analysis","support_id":"sup_95d091f2ebc475f60a22","text":"{\"blocking_evidence\":null,\"headline\":\"recognized witness, not Arabic root play\",\"reader_payoff\":\"The reader notices that the name contributes stable prophetic authority by recognition, while non-name dictionary branches do not become local semantics.\",\"reason\":\"V4 includes a foreign proper-name branch alongside unrelated gaze, plant, and community branches; the local form and referent profile select the proper-name witness.\",\"representative_source_ids\":[\"QS-8d5fd9c0\",\"QS-d019a6b8\",\"MS-97a74404\",\"QY-13465ec3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:1:written-record-materiality","source_type":"word_analysis","support_id":"sup_9f7290714cb3b5538023","text":"{\"blocking_evidence\":null,\"headline\":\"written sheets as scriptural witness\",\"reader_payoff\":\"The reader notices that the authority is carried through written record-bearing surfaces, while the local sense remains scriptural archive rather than any broad physical surface.\",\"reason\":\"V4 supports written sheet and collected-sheet branches for {{ar:ص ح ف}} ({{tr:ṣ-ḥ-f}}); local apposition and named possessors narrow the field to scriptural records, not dish, broad surface, or misreading branches.\",\"representative_source_ids\":[\"QS-0ff09778\",\"QS-bd54a602\",\"MS-781cc2f3\",\"QE-74729781\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:2:ordered-pair-continuity","source_type":"word_analysis","support_id":"sup_aa387fb2aa70d8c5146f","text":"{\"blocking_evidence\":null,\"headline\":\"first member of the Abraham-Moses pair\",\"reader_payoff\":\"The reader notices one archive category being distributed across two recognized prophetic lineages, with Abraham beginning the pair and Moses closing it.\",\"reason\":\"Attachment evidence coordinates the two names as shared dependents of the same head, so the order is a local two-name distribution rather than separate clauses.\",\"representative_source_ids\":[\"QT-0ee97794\",\"QT-326805cf\",\"MT-8957bf81\",\"QE-2a6eb200\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:4:final-archive-seal","source_type":"word_analysis","support_id":"sup_b07b2ec383c147c708b5","text":"{\"blocking_evidence\":null,\"headline\":\"final named witness seals the surah\",\"reader_payoff\":\"The reader notices that the surah closes when the second named witness completes the archival pair, turning assertion into citation.\",\"reason\":\"The word is final in the ayah and surah, and translation support treats the two names as coordinated possessors of the same archive phrase.\",\"representative_source_ids\":[\"QT-4475e817\",\"QT-dc343c9e\",\"MT-fb52bb75\",\"QY-dc70fe97\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:4:foreign-name-mosaic-witness","source_type":"word_analysis","support_id":"sup_c1a92b0a3eb4875beedf","text":"{\"blocking_evidence\":null,\"headline\":\"foreign proper name as Mosaic witness\",\"reader_payoff\":\"The reader notices that the word contributes Mosaic textual authority by recognized name, not by root-derived Arabic semantics.\",\"reason\":\"The aligned word is a foreign proper noun with no local Arabic root; the source rows press onomastic recognition rather than derivation.\",\"representative_source_ids\":[\"QS-8b41751a\",\"QS-8e25fee2\",\"MS-b4240f05\",\"QF-836e9f64\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:2:first-restrictor-and-lineage-shift","source_type":"word_analysis","support_id":"sup_cf7f1a3e860ca9bbff41","text":"{\"blocking_evidence\":null,\"headline\":\"Abrahamic witness starts the named restriction\",\"reader_payoff\":\"The reader notices Abraham's name moving from familiar lineage discourse into the first textual witness that narrows the former records (2:130; 16:123).\",\"reason\":\"The local syntax places the name first under the archive head, and the CRITICAL rows provide concrete lineage-discourse contrasts at 2:130 and 16:123.\",\"representative_source_ids\":[\"QI-b7f0b428\",\"QI-ecb1294b\",\"MI-4a539623\",\"MT-d4a93276\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:4:mosaic-record-recurrence","source_type":"word_analysis","support_id":"sup_d14cf12a6e98eb3f2b2d","text":"{\"blocking_evidence\":null,\"headline\":\"Mosaic records recalled in closing identification\",\"reader_payoff\":\"The reader notices that the final name is not merely another prophet mention; it is attached to a narrow record-witness formula also invoked at 53:36.\",\"reason\":\"The CRITICAL rows give 53:36 as a concrete Mosaic-record reference, and the local syntax binds {{ar:مُوسَىٰ}} ({{tr:mūsā}}) to the archive noun.\",\"representative_source_ids\":[\"MI-12fc0479\",\"QE-5fc87a2c\",\"QH-b6fdfd3e\",\"ME-d72fb37d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"87:19:1:1","source_type":"qac_morpheme","support_id":"sup_d2e6cd68eb6fb99b3786","text":"{\"lemma_ar\":\"صُحُف\",\"morph_features\":\"STEM|POS:N|LEM:SuHuf|ROOT:SHf|FP|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"87:19:1:1\",\"qac_word_ref\":\"87:19:1\",\"root_ar\":\"ص ح ف\",\"surface_ar\":\"صُحُفِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:4:long-a-cadence-closure","source_type":"word_analysis","support_id":"sup_eb257b3bfdbc3f9f100f","text":"{\"blocking_evidence\":null,\"headline\":\"long ā landing closes the citation\",\"reader_payoff\":\"The reader notices the final long ā as an audible landing that balances the first long proper name and joins the citation to the surah's close.\",\"reason\":\"The final alif maqṣūra and final word position support the sound-cadence payoff without changing the grammatical witness role.\",\"representative_source_ids\":[\"QF-5dfa83ef\",\"QP-76b60168\",\"QP-d0df2331\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"87:19:1:plural-construct-specificity","source_type":"word_analysis","support_id":"sup_f6be9b8c2e17fdfb086d","text":"{\"blocking_evidence\":null,\"headline\":\"plural construct binds two named possessors\",\"reader_payoff\":\"The reader notices one plural archive category broad enough for multiple records and specific enough to be defined by the named possessors.\",\"reason\":\"Attachment evidence makes {{ar:صُحُفِ}} ({{tr:ṣuḥufi}}) the head governing both proper names; construct dependence supplies specificity despite the lack of the article.\",\"representative_source_ids\":[\"QG-588528d7\",\"QG-833f994b\",\"QF-27d5c300\",\"MF-abc0d73b\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ","ayah_ref":"87:19"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000845/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000845","role":"The written-sheet image supplies the textual medium, while the two following names organize that medium as attributed witness.","root":"ص ح ف","source_ref":"87:19","source_word_indices":["1"]}],"changed_reading":{"after":"Plural written witnesses whose authority remains indexed to two distinguishable prophetic provenances.","before":"A bare label for old books associated with two figures."},"confidence":"strong","focus_anchor":"The plural construct at focus word 1 is followed by the coordinated names Abraham and Moses.","mechanism":"The written-sheet branch makes the phrase a pair of provenance-bearing textual corpora. The proper names do more than identify a topic: they keep two lines of witness visible inside one compact attribution.","model_id":"base_named_written_witnesses"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_named_written_witnesses","source_type":"hft","support_id":"sup_bb076108e85095823972","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ","ayah_ref":"87:19"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000845/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000845","role":"Flat breadth turns the named sheets from closed containers into surfaces on which distinct testimony can be openly spread.","root":"ص ح ف","source_ref":"87:19","source_word_indices":["1"]}],"changed_reading":{"after":"Two traditions laid out as broad, inspectable surfaces of disclosure.","before":"Closed textual objects possessed by Abraham and Moses."},"confidence":"medium","focus_anchor":"The plural noun at word 1 can retain the root's image of breadth even while denoting sheets.","mechanism":"Flat spread and breadth foreground the sheet as an exposed surface. The phrase can therefore evoke teachings laid open side by side, with Abraham and Moses occupying a shared plane of disclosure without being collapsed into one source.","model_id":"base_open_spread_surfaces"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_open_spread_surfaces","source_type":"hft","support_id":"sup_ced24621bc9f51de9f7f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ","ayah_ref":"87:19"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000845/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000845","role":"Collected sheets supply an archival gathering mechanism, while the coordinated names preserve two components within the gathering.","root":"ص ح ف","source_ref":"87:19","source_word_indices":["1"]}],"changed_reading":{"after":"A gatherable constellation of leaves in which distinct Abrahamic and Mosaic provenances remain legible.","before":"Two unrelated references to earlier writings."},"confidence":"medium","focus_anchor":"The plural sheets and the coordination of two names permit collection while preserving internal plurality.","mechanism":"The codex branch pulls separate leaves toward an assembled archive, but the syntax does not require one physical volume. A live reading is a collectable cross-prophetic dossier whose unity consists in juxtaposition rather than source erasure.","model_id":"base_collectable_plural_archive"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_collectable_plural_archive","source_type":"hft","support_id":"sup_bac362581746d4dfb48c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ","ayah_ref":"87:19"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000845/B002","root_000845/B005"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000845","role":"The written-sheet image supplies durable inscription as the condition for preservation.","root":"ص ح ف","source_ref":"87:19","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_000845","role":"Misreading from similar written forms supplies the graphic failure mode carried by that same preserving medium.","root":"ص ح ف","source_ref":"87:19","source_word_indices":["1"]}],"changed_reading":{"after":"The named sheets preserve a trace while remaining exposed to specifically visual transmission error.","before":"Written attribution guarantees transparent preservation."},"confidence":"exploratory","focus_anchor":"The same focus root that denotes written sheets also carries a branch for error caused by confused written characters.","mechanism":"Writing stabilizes a trace but introduces a medium-specific vulnerability: what is preserved can be misread. The two attributions keep provenance visible, yet the focus alone does not show whether parallel provenance corrects or compounds transmission error.","model_id":"base_preservation_with_graphic_risk"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_preservation_with_graphic_risk","source_type":"hft","support_id":"sup_2993825d4d21a656ce4c","trust":"legacy_unbound"}]}
</lane_packet_json>
