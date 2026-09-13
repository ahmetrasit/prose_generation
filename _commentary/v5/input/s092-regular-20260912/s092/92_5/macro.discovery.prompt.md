# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **92:5**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s092-regular-20260912/s092/92_5/macro.discovery.json` and modify nothing
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

- Macro has no explicitly added external ayat. Assess the declared pericope or host-surah context, including any automatic host basmala, as ordinary non-focus context.

## Response Schema

Return exactly these top-level fields:

```json
{
  "schema_version": "commentary-v5-scope-discovery-v1",
  "ayah_ref": "92:5",
  "lane": "macro",
  "coverage_complete": true,
  "candidate_decisions": [
    {
      "candidate_id": "exact packet candidate ID",
      "decision": "accept | narrow | represented | reject",
      "reason": "specific evidentiary reason",
      "finding_refs": ["macro:stable-key"],
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
      "finding_ref": "macro:stable-key",
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
`macro:`. Accepted/narrowed candidates own dedicated findings. A represented
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

Governs ayah-level (layer 2) and surah-level (layer 3) commentary. Layer 2 uses
its evidence bundle; the active surah workflow uses only completed final ayah
editorials. They differ in source boundary and in what they synthesize.

[`PRINCIPLES.md`](PRINCIPLES.md) governs this file. Sources and formats are in
[`docs/SOURCES.md`](docs/SOURCES.md); channel rules in
[`docs/CHANNELS.md`](docs/CHANNELS.md).

The active Layer 3 production contract is
[`_surah_commentary/v2/ORCHESTRATION.md`](_surah_commentary/v2/ORCHESTRATION.md). The
former combined Layer 3 + 2.5 overlay workflow is retired.

Status: active draft, updated 2026-09-11. The editorial-only surah contract
supersedes the legacy channel-first workflow. Mechanical validation and
semantic acceptance are separate; consult its implementation status.

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
The isolated Layer-2 writer cannot know that. The active surah workflow reads
only the completed final ayah editorials from one selected v5 analysis. It
synthesizes the readings present there, preserving their attribution, uncertainty,
and boundaries. Discovery artifacts, scope ledgers, invitations, separate
primary-floor data, and network/V11 sources do not enter this workflow. It writes
a separate surah reading and does not rewrite or overlay the ayah prose.

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

- **editorial snapshot** - the complete final editorial texts for one surah;
- **source-anchored outline** - the main cross-ayah movements supported by those
  texts, with each image's contribution and qualifications;
- **composition envelope** - prelude/postlude prose with exact anchors for
  each selected movement and member; semantic support requires review;
- **surah reading** — continuous reader prose emitted by the deterministic
  finalizer, not a summary or ayah catalogue;
- **publication evidence** — separate mapping from prose spans to packet
  evidence;
- **friction** — missing evidence and production limitations.

Contracts and schemas are under `_surah_commentary/v2/`.

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

Layer 3 freezes only the completed final editorial prose for every numbered
ayah in one selected v5 analysis. The surah number and complete ayah count are
operator-supplied scope metadata. Missing or malformed editorial prose aborts;
no other semantic source is required or permitted. See
[`_surah_commentary/v2/ORCHESTRATION.md`](_surah_commentary/v2/ORCHESTRATION.md).

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

Status: updated 2026-09-11. New surah runs use only completed final ayah
editorials. The former channel-first source contract is historical; the active
runbook is `_surah_commentary/v2/ORCHESTRATION.md`.

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
discover or name a surah channel. The active surah workflow reads the final
editorial prose containing those local readings and writes a separate surah
reading; it does not patch channel disclosure back into the Layer-2 prose.

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

Layer 2 remains cold and states local surprise readings. The active surah
workflow freezes only the completed final editorial prose for every numbered
ayah in one selected v5 analysis. It derives an anchored outline, composes the
prelude/postlude, and edits the prose in the same composition-agent session.
Discovery artifacts, scope ledgers, invitations, separate primary-floor data,
and network/V11 sources are not inputs.

The outline selects the main cross-ayah movements supported by these editorials,
not an inventory compressing every finding. Significant distinct systems remain
separate; selection is not disambiguation. Each member image must have a clear
contribution, source anchor, and preserved qualification. Every ayah is accounted
for, including ayahs serving only as primary context.

### Layer 3 (per surah)

The prelude prepares concrete expectations; the postlude develops their
whole-surah payoff. All selected movements and members must land visibly, with
exact source and prose anchors. Mechanical validation checks coverage and
lineage; a semantic reviewer checks support, scope, and coherence. The workflow
does not rewrite Layer 2 or add overlays.

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
`_surah_commentary/v2/ORCHESTRATION.md`.

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
while designing additions to Layer 2. The active editorial-only workflow does
not write those additions; it records source-anchored movements and prose landings.

## 6. Recording

Per surah, the active workflow records:

- `surah-editorial-source-v1`: frozen final editorial texts and source hashes;
- `surah-editorial-outline-v1`: primary progression, main movements, member
  contributions and qualifications, and exact editorial anchors;
- `surah-editorial-composition-v1`: draft/editorial prelude and postlude with
  exact movement/member prose anchors;
- `surah-editorial-publication-v1`: approved publication lineage and evidence.

The active output schemas are `editorial-outline-v1.schema.json` and
`editorial-composition-v1.schema.json` under `_surah_commentary/v2/schemas/`.
Old channel/discovery schemas are historical. Follow
`_surah_commentary/v2/ORCHESTRATION.md`.

---

## 7. Open

- **Maturity remains archived.** The four-step scale and `emerging`-hint rule
  belong to the retired Layer 2.5 overlay experiment. They may be revisited
later, but the active editorial-only workflow does not depend on them.
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
{"branch_registry":[{"boundary":"Includes measuring, apportioning, or planning something before cutting or carrying it out.","branch_kind":null,"branch_ref":"root_000434/B001","candidate_links":[{"candidate_id":"cand_565e5686d7eb6b5dd777","lane":"macro"}],"focus_root_occurrences":[],"gloss":"measuring and proportioning a thing","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"تقدير الشيء وقياسه","image_en":"measuring and proportioning a thing"}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"تقدير الشيء وقياسه","image_en":"measuring and proportioning a thing","scope_ar":"يدخل فيه التقدير والقياس قبل القطع أو الفعل، ومنه خلق الأديم وخلق الأمر بمعنى قدره.","scope_en":"Includes measuring, apportioning, or planning something before cutting or carrying it out."},"support_links":["sup_bb94f114e44ba5035266"]},{"boundary":"Includes smooth, solid, leveled, or even surfaces, including rocks, tools, clouds or traces that have leveled, and named flat body or cave surfaces.","branch_kind":null,"branch_ref":"root_000434/B008","candidate_links":[{"candidate_id":"cand_565e5686d7eb6b5dd777","lane":"macro"}],"focus_root_occurrences":[],"gloss":"smooth and level surface","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"ملاسة السطح واستواؤه","image_en":"smooth and level surface"}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"ملاسة السطح واستواؤه","image_en":"smooth and level surface","scope_ar":"يدخل فيه الأملس المصمت، الصخرة الخلقاء، استواء السحاب أو الرسم، السهم أو القدح أو الحبل المملس، ومواضع الجبهة والوجه والظهر والغار المسماة خلقاء أو خليقاء.","scope_en":"Includes smooth, solid, leveled, or even surfaces, including rocks, tools, clouds or traces that have leveled, and named flat body or cave surfaces."},"support_links":["sup_bb94f114e44ba5035266"]},{"boundary":"Bu dal verme, birinden isteme veya birinin işini görme anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001028/B001","candidate_links":[{"candidate_id":"cand_81ab5e5bb3ef8ad1f2ca","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:3:1","qac_word_ref":"92:5:3","surface_ar":"أَعْطَىٰ"}],"gloss":"elle uzanıp alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneye elle uzanıp onu alma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ceylanın yapraklara erişmek için ön ayaklarını kaldırıp ağaca uzanmasını anlatır."}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin el ile erişilip alındığı temel kullanım için uygundur.","boundary_detail":"Bu dal verme, birinden isteme veya birinin işini görme anlamlarını kapsamaz.","branch_image_ar":"الأخذ والتناول باليد","concept_gloss":"elle uzanıp alma","contextual_glosses":[{"applicability":"Ceylanın ön ayaklarını kaldırarak ağaç yapraklarına uzandığı betimleme için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın yükselme amacını ve yaprağa doğru uzanmasını korur."},"facet_ids":["F002"],"text":"yapraklara erişmek için uzanma","usage_role":"contextual"}],"definition":"Temel anlam, bir nesneye elle uzanıp onu almaktır. Hayvanı anlatan özel kullanımda ceylan, ağacın yapraklarına erişmek için ön ayaklarını kaldırıp uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneye elle uzanıp onu alma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Ceylanın yapraklara erişmek için ön ayaklarını kaldırıp ağaca uzanmasını anlatır."}],"identity_rationale":"Kaynak anlatımı, temel olarak bir şeyi elle almayı; özel hayvan betimlemesinde ise ceylanın ağacın yapraklarına erişmek için ön ayaklarını kaldırmasını bildirir. Bu iki kullanım, alma ve erişmek için uzanma odağında tutarlı biçimde birleşir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"elle alma"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi elle alma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yapraklara erişmek için ön ayaklarını kaldıran ceylan"}],"lexicalization_note":"Tanım, elle alma çekirdeğini hayvanı anlatan özel kalıptan ayırır; ceylan betimlemesi bütün dala yayılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlanan dört ilişki elle alma sınırını en açık biçimde gösterir, öteki adaylar yalnızca uzak konu ortaklığı taşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda erişip alma belirleyiciyken komşu dalda avucu kapatıp nesneyi bütünüyle kavrama belirleyicidir.","focus_only":"Erişmek için elle uzanmayı ve ceylanın yaprağa uzanmasını da kapsar.","gloss":"elle uzanma ile avuçlayarak alma","neighbor_only":"Nesneyi bütün avuçla kavrama ve avuçta tutma biçimini öne çıkarır.","neighbor_ref":"root_001197/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir nesneyi el kullanarak almayı anlatır."},{"boundary_match":"partial","distinction":"Odak dal elle uzanıp almaya bağlıdır; komşu dal ise elde bulundurma, toplama ve daha geniş alma kullanımlarını içerir.","focus_only":"Elle uzanma biçimini ve yaprağa uzanan ceylan betimlemesini taşır.","gloss":"elle alma ile genel alıp edinme","neighbor_only":"Alınanı elde bulundurma, toplama ve söz gibi soyut nesneleri alma alanına da uzanır.","neighbor_ref":"root_000018/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi alma ve ona erişme alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dalın sınırı elle alma üzerindedir; komşu dal uzaklıktan erişme, güçlü tutma ve soyut kullanımlara kadar genişler.","focus_only":"Elle alma çekirdeği yanında ceylanın ön ayaklarını kaldırdığı özel betimlemeyi içerir.","gloss":"elle alma ile uzaktan erişip tutma","neighbor_only":"Uzak bir şeye erişmeyi, soyut uzanımları ve baştan ya da sakaldan tutmayı da kapsar.","neighbor_ref":"root_001565/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da uzanarak bir şeye erişme ve onu alma vardır."},{"boundary_match":"partial","distinction":"Odak dal hareketi alan kişinin yönünden kurar; komşu dal veren kişinin nesneyi başkasına geçirmesini ve ortaya çıkan verilmiş şeyi anlatır.","focus_only":"Nesneyi alan kişinin elle erişip kendine doğru almasını anlatır.","gloss":"alma ile verme yönleri","neighbor_only":"Nesneyi başkasına verme, elden uzatma ve verilen şeyi adlandırma yönünü taşır.","neighbor_ref":"root_001028/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir nesnenin el aracılığıyla yer değiştirmesine ilişkindir."}],"source_phrase_ar":"العطو التناول باليد (maqayis;ayn;tahdhib)؛ عطوت الشيء تناولته باليد (sihah)؛ الظبي العاطي الرافع يديه إلى الشجرة ليتناول من الورق (ayn)؛ الظباء تتطالل إذا رفعت أيديها لتتناول ورق الشجر (tahdhib)","source_summary":"Kaynaklar elle alma çekirdeğinde birleşir ve ceylanın yaprağa erişmek için ön ayaklarını kaldırmasını bu çekirdeğin özel bir görünümü olarak verir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه التناول باليد ورفع اليدين إلى الورق وتناول الشيء","what_is_not_ar":"ليس الإعطاء ولا اسم العطية ولا طلبها ولا خدمة الإنسان لغيره"},"support_links":["sup_a16f26c6a1af947827bc"]},{"boundary":"Dal, alma yönünü veya verme isteğini değil, veren yönündeki aktarımı ve verilen şeyi kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001028/B002","candidate_links":[{"candidate_id":"cand_3f15dc539a13a94bd6aa","lane":"macro"},{"candidate_id":"cand_1460758e2c938f24657f","lane":"macro"},{"candidate_id":"cand_acf054d8c135ca9e0851","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:3:1","qac_word_ref":"92:5:3","surface_ar":"أَعْطَىٰ"}],"gloss":"verme, karşılıklı elden geçirme ve verilen şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi başkasına verme veya elden uzatma eylemidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir nesnenin iki kişi arasında karşılıklı olarak el değiştirmesini anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Verilen nesnenin kendisini ve bunun tekil ya da çoğul adlandırılışını gösterir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İki kişinin bir kılıcı birbirine verip bir süre sırayla tutması veya sallaması karşılıklı el değiştirmeye örnektir."}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın eylem, karşılıklı aktarım ve aktarılmış nesne katmanlarını birlikte göstermek için uygundur.","boundary_detail":"Dal, alma yönünü veya verme isteğini değil, veren yönündeki aktarımı ve verilen şeyi kapsar.","branch_image_ar":"المناولة والإعطاء","concept_gloss":"verme, karşılıklı elden geçirme ve verilen şey","contextual_glosses":[{"applicability":"Bir nesnenin veren kişiden başka bir kişiye geçirildiği düz kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Vereni, verilen nesneyi ve alıcıya doğru aktarımı korur."},"facet_ids":["F001"],"text":"bir şeyi başkasına vermek","usage_role":"general"},{"applicability":"Aynı nesnenin iki kişi arasında el değiştirerek sırayla kullanıldığı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı vermeyi ve nesnenin sırayla kullanılmasını korur."},"facet_ids":["F002","F004"],"text":"sırayla birbirine vermek","usage_role":"contextual"},{"applicability":"Eylemin kendisi değil, birine verilmiş nesne adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Verme sonunda alıcıya geçen nesne sonucunu açıkça korur."},"facet_ids":["F003"],"text":"verilen şey","usage_role":"contextual"}],"definition":"Bir şeyi başkasına verme veya elden uzatma; karşılıklı kullanımda aynı şeyi iki kişinin birbirine vermesi veya elden geçirmesidir. Adlaşmış kullanım ise verilen şeyi ve onun birden çok oluşunu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi başkasına verme veya elden uzatma eylemidir."},{"facet_id":"F002","role":"extension","statement":"Bir nesnenin iki kişi arasında karşılıklı olarak el değiştirmesini anlatır."},{"facet_id":"F003","role":"extension","statement":"Verilen nesnenin kendisini ve bunun tekil ya da çoğul adlandırılışını gösterir."},{"facet_id":"F004","role":"example","statement":"İki kişinin bir kılıcı birbirine verip bir süre sırayla tutması veya sallaması karşılıklı el değiştirmeye örnektir."}],"identity_rationale":"Kaynak anlatımı bir şeyi başkasına verme ve elden uzatma eylemini, iki kişi arasındaki karşılıklı el değiştirmeyi ve verilen şeyin adını birlikte bildirir. Kılıcın sırayla elde tutulması, karşılıklı el değiştirme yönünü açıklayan özel bir örnektir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"verme, elden uzatma"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"karşılıklı elden verme veya el değiştirme"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kılıcı sırayla birbirine verip elde tutma veya sallama"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"verilen şey"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"birine verilen şey"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"birine verilen şeyler"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"verilen şeylerin çoğul adı"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çok veren kimse"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"malı ne çok veriyor!"}],"lexicalization_note":"Tanım, verme çekirdeğini karşılıklı el değiştirme, verilen şeyin adı ve özel söyleyişlerden ayrı katmanlar halinde tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen beş karşılaştırma verme dalını alma, isteme, getirme, iyeliğe geçirme ve isteyene karşılık verme sınırlarında açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal aktarımı veren kişinin yönünden kurar; komşu dal nesneye erişip onu alan kişinin yönünden kurar.","focus_only":"Nesneyi veren kişiden alıcıya geçirme ve verilen şeyi adlandırma yönünü taşır.","gloss":"verme ile alma yönleri","neighbor_only":"Nesneye elle erişip onu alan kişinin yönünü ve ceylanın uzanışını taşır.","neighbor_ref":"root_001028/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir nesnenin el aracılığıyla yer değiştirmesini anlatır."},{"boundary_match":"field_only","distinction":"Odak dalda nesne verenden alıcıya geçer; komşu dalda isteyen kişi böyle bir geçişin yapılmasını başkalarından ister.","focus_only":"Bir şeyi gerçekten verme, elden uzatma ve verilen nesneyi adlandırma vardır.","gloss":"verme ile verilmesini isteme","neighbor_only":"Henüz verilmemiş bir şeyi başkalarından isteme eylemi vardır.","neighbor_ref":"root_001028/B005","relation_type":"same_field","shared_zone":"İki dal aynı olası aktarımın veren ve isteyen taraflarıyla ilgilidir."},{"boundary_match":"partial","distinction":"Odak dal karşılıklı elden geçirme ve verilen nesneye kadar genişler; komşu dal ise verme yanında getirip hazır etme yönünü taşır.","focus_only":"Karşılıklı el değiştirmeyi ve verilen nesnenin adını ayrıca kapsar.","gloss":"verme ile getirip verme","neighbor_only":"Bir şeyi başka bir şeyle birlikte getirme veya hazır etme yönüne de uzanır.","neighbor_ref":"root_000009/B002","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak çekirdeği bir şeyi başkasına vermektir."},{"boundary_match":"partial","distinction":"Odak dalda elden uzatma yeterli olabilir; komşu dalda verme, alıcının o varlık üzerinde iyelik kazanmasıyla sınırlandırılır.","focus_only":"Elden uzatma, karşılıklı geçirme ve yalnızca verilen şeyi adlandırma kullanımlarını kapsar.","gloss":"verme ile iyeliğe geçirme","neighbor_only":"Verilen malın alıcının iyeliğine geçirilmesini belirgin bir koşul olarak taşır.","neighbor_ref":"root_000448/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir varlığın başkasına verilmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal alıcının önceden istemesini gerektirmez; komşu dal ise vermeyi açıkça bir isteyen kişiye yöneltir.","focus_only":"İstek bulunmadan yapılan vermeyi, karşılıklı geçirmeyi ve verilen nesneyi de kapsar.","gloss":"genel verme ile isteyene verme","neighbor_only":"Verme eylemini, kendisinden bir şey isteyen kişiye karşılık verme durumuna bağlar.","neighbor_ref":"root_001403/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir kişiye bir nesne vermeyi anlatır."}],"source_phrase_ar":"منه اشتق الإعطاء والمعاطاة المناولة والعطاء اسم لما يعطى وهي العطية (maqayis)؛ العطاء اسم لما يعطى وأعطية وأعطيات (ayn)؛ أعطاه مالا يعطيه إعطاء والاسم العطاء والعطية الشيء المعطى (sihah)؛ الإعطاء مأخوذ من هذا والمعاطاة المناولة والعطاء اسم لما يعطى (tahdhib)؛ المعاطاة أن يستقبل رجل رجلا ومعه سيف فيقول أرني سيفك فيعطيه فيهزه هذا ساعة وهذا ساعة (tahdhib)","source_summary":"Kaynaklar verme, elden uzatma ve verilen şey anlamlarını birlikte destekler; karşılıklı verme, bir kılıcın iki kişi arasında sırayla kullanılmasıyla örneklenir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الإعطاء والمناولة والمعاطاة والعطاء والعطية والشيء المعطى وجمعه","what_is_not_ar":"ليس مجرد تناول الشيء لنفسه ولا طلب العطاء من الناس"},"support_links":["sup_7dfd247afe878c202c27","sup_a6dfe3d3a07f8aaa114e","sup_ce7c7fe0943cf7b23fd5"]},{"boundary":"Dal genel vermeyi değil, belirli bir kişinin işini görme ve ona bakma ilişkisini anlatır.","branch_kind":"non_bare","branch_ref":"root_001028/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:3:1","qac_word_ref":"92:5:3","surface_ar":"أَعْطَىٰ"}],"gloss":"birinin işini görüp istediğini uzatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir başkasının işini görme ve bakımını üstlenme eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bakılan kişinin istediği nesneleri ona uzatmak, işini görmenin bir parçasıdır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir çocuğun yakınları için çalışıp onların istediklerini uzatması bu kullanımı örnekler."}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye bakma ile onun istediği nesneleri uzatmanın birlikte anlatıldığı kullanım için uygundur.","boundary_detail":"Dal genel vermeyi değil, belirli bir kişinin işini görme ve ona bakma ilişkisini anlatır.","branch_image_ar":"الخدمة والمناولة للأهل","concept_gloss":"birinin işini görüp istediğini uzatma","contextual_glosses":[{"applicability":"Bir çocuğun kendi yakınları için çalışıp onların gereksinimlerini karşıladığı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çocuğun yakınları adına çalışmasını ve işlerini görmesini korur."},"facet_ids":["F001","F003"],"text":"yakınlarının işini görmek","usage_role":"contextual"}],"definition":"Bir kişinin işini görmek, bakımını üstlenmek ve istediği şeyleri ona uzatmaktır; çocukla ilgili özel kullanımda bu işler kendi yakınları için yapılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir başkasının işini görme ve bakımını üstlenme eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Bakılan kişinin istediği nesneleri ona uzatmak, işini görmenin bir parçasıdır."},{"facet_id":"F003","role":"example","statement":"Bir çocuğun yakınları için çalışıp onların istediklerini uzatması bu kullanımı örnekler."}],"identity_rationale":"Kaynak anlatımı bir kişinin, özellikle bir çocuğun, yakınlarının işini görmesini, istediklerini onlara uzatmasını ve genel olarak bir başkasının bakımını üstlenmesini bildirir. Verme bu dalda bağımsız amaç değil, birinin işini görmenin parçasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"çocuğun yakınlarının işini görüp istediklerini uzatması"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"onun işini görüp bakımını üstlenme"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"işimi görüyor"}],"lexicalization_note":"Anlam yalnızca belirtilen kişi ve yapı bağı içinde verilir; kökün yalın anlamına ya da bütün verme kullanımlarına yayılmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; seçilen dört ilişki iş görme çekirdeğini verme, iş gören kişi, hasta bakımı ve yol yardımı alanlarından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda uzatma, kişinin işini görme ilişkisinin bir parçasıdır; komşu dalda nesnenin verilmesi başlı başına çekirdektir.","focus_only":"Bir kişinin işini sürekli görme ve istediğini ona uzatma ilişkisini taşır.","gloss":"işini görme ile nesne verme","neighbor_only":"Bir nesneyi başkasına aktarma ve verilmiş nesneyi adlandırma çekirdeğini taşır.","neighbor_ref":"root_001028/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir kişiye istediği bir nesnenin uzatılması bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal yapılan işi anlatır; komşu dal ise bu işi yapan yardımcıları ve kimi yakınlık kümelerini adlandırır.","focus_only":"Birinin işini görme eylemini ve istediği nesneyi ona uzatmayı bildirir.","gloss":"iş görme ile iş gören kişiler","neighbor_only":"Yardımcı ya da iş gören kişileri, yakınlık bağlarıyla birlikte bir insan kümesi olarak adlandırır.","neighbor_ref":"root_000340/B002","relation_type":"near_neighbor","shared_zone":"İki dal da başkası için çalışma ve onun gereksinimini karşılama alanındadır."},{"boundary_match":"partial","distinction":"Odak dal genel bir iş görme ilişkisidir; komşu dal hastanın bakımına ve iyileşmesine yönelik daha dar bir alandır.","focus_only":"Sağlık koşulu aramadan bir kişinin işini görmeyi ve istediğini uzatmayı kapsar.","gloss":"genel iş görme ile hasta bakımı","neighbor_only":"Bakımı yalnızca hastalık durumuna ve hastayı iyileştirmeye yönelik gözetmeye bağlar.","neighbor_ref":"root_001415/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da başka bir kişinin gereksinimleriyle ilgilenme vardır."},{"boundary_match":"field_only","distinction":"Odak dal kişiye yönelik genel iş görmedir; komşu dal yalnızca yolculuk ve binek gereksinimi çevresinde kurulur.","focus_only":"Bir kişinin gündelik işini görme ve istediği nesneyi ona uzatma ilişkisini anlatır.","gloss":"iş görme ile yol yardımı","neighbor_only":"Yolculuğa yardım etme, binek sağlama veya yol yardımı isteme durumuna bağlıdır.","neighbor_ref":"root_000551/B008","relation_type":"same_field","shared_zone":"İki dal da bir başkasının gereksinimini karşılayarak ona destek olmayı içerir."}],"source_phrase_ar":"عاطى الصبي أهله إذا عمل وناول ما أرادوا (maqayis)؛ هو يعطيني ويعاطيني إذا كان يخدمك (sihah)؛ عطيته وعاطيته أي خدمته وقمت بأمره ومن يعطيك أي من يتولى خدمتك (tahdhib)","source_summary":"Kaynaklar birinin işini görme ve bakımını üstlenme çekirdeğinde birleşir; çocuğun yakınları için çalışıp istediklerini uzatması bu çekirdeği somutlaştırır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه خدمة الإنسان والقيام بأمره ومناولته ما يريد","what_is_not_ar":"ليس العطاء العام ولا طلب العطاء ولا مجرد تناول الشيء باليد"},"support_links":[]},{"boundary":"Dal olağan nesne verme veya alma değil, sınırı aşan ya da gözü pek bir işe el atma üzerindedir.","branch_kind":"mixed_non_bare","branch_ref":"root_001028/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:3:1","qac_word_ref":"92:5:3","surface_ar":"أَعْطَىٰ"}],"gloss":"hakkı olmadan el uzatma ve gözü pekçe işe girişme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hakkı olmayan veya alınması uygun görülmeyen bir şeye el uzatmayı anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işe girip onunla uğraşmayı, özellikle yüksek ya da çirkin görülen işlere yönelmeyi anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gözü pekçe eyleme geçip amaçlanan işi sonuna vardırmayı bildirir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yeterli aracı, dayanağı veya erişme olanağı olmadan gücünü aşan bir işe kalkışmayı anlatır."}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Uygunsuz alma ile sınırı aşan bir işe gözü pekçe kalkışma yönlerini birlikte anlatmak için uygundur.","boundary_detail":"Dal olağan nesne verme veya alma değil, sınırı aşan ya da gözü pek bir işe el atma üzerindedir.","branch_image_ar":"التعاطي والخوض فيما يبلغه","concept_gloss":"hakkı olmadan el uzatma ve gözü pekçe işe girişme","contextual_glosses":[{"applicability":"Bir kişinin belirli bir işe yönelip onu yapmaya başladığı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşe yönelmeyi, başlamayı ve onunla etkin biçimde uğraşmayı korur."},"facet_ids":["F002"],"text":"bir işe girip onunla uğraşmak","usage_role":"general"},{"applicability":"Yeterli araç, dayanak veya bilgi olmadan erişilmez görülen bir işe yönelme için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Araçsızlığı, dayanaksızlığı ve erişilmez işe kalkışmayı korur."},"facet_ids":["F004"],"text":"dayanaksızca gücünü aşan işe kalkışmak","usage_role":"explanatory"}],"definition":"Bir kimsenin hakkı olmayan ya da el atması uygun görülmeyen bir şeye uzanması ve bir işe gözü pek biçimde girişmesidir. Kimi kullanımlarda yeterli araç veya dayanak olmadan yüksek ya da erişilmez bir işe kalkışmayı ve girişilen eylemi sonuna vardırmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hakkı olmayan veya alınması uygun görülmeyen bir şeye el uzatmayı anlatır."},{"facet_id":"F002","role":"extension","statement":"Bir işe girip onunla uğraşmayı, özellikle yüksek ya da çirkin görülen işlere yönelmeyi anlatır."},{"facet_id":"F003","role":"specialization","statement":"Gözü pekçe eyleme geçip amaçlanan işi sonuna vardırmayı bildirir."},{"facet_id":"F004","role":"specialization","statement":"Yeterli aracı, dayanağı veya erişme olanağı olmadan gücünü aşan bir işe kalkışmayı anlatır."}],"identity_rationale":"Kaynak anlatımı, hakkı olmayan veya yapılması uygun görülmeyen bir şeye el uzatmayı; bir işe girip onunla uğraşmayı; yüksek, çirkin ya da erişilmez bir işe gözü pek biçimde kalkışmayı birlikte verir. Eylemi sonuna vardırma ve araçsız kalkışma, bu girişme çekirdeğinin ayrı görünümleridir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"hakkı olmayan veya alınması uygun görülmeyen şeye el uzatma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bir işe girip onunla uğraşma"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"gözü pekçe eyleme girişip deveyi yaralama"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"aracı, dayanağı veya yeterliği olmadan erişilmez işe kalkışma"}],"lexicalization_note":"Tanım, genel el atma yönünü belirli yapılardaki uygunsuz alma, gözü pek girişme ve araçsız kalkışma görünümlerinden ayırır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; seçilen beş ilişki dalı gerçek alma, nötr işe girme, düşünmeden atılma, yaklaşma ve çekişmede yenme alanlarından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bu görüntüyü uygunsuz veya gözü pek bir girişime taşır; komşu dal ise gerçek bir nesnenin elle alınmasını anlatır.","focus_only":"Hakkı aşma, uygunsuzluk veya gözü pek biçimde bir işe girişme yönünü taşır.","gloss":"işe el atma ile elle alma","neighbor_only":"Bir nesneye elle erişip onu alma ve ceylanın yaprağa uzanmasıyla sınırlıdır.","neighbor_ref":"root_001028/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da bir şeye uzanıp onu ele alma görüntüsü bulunur."},{"boundary_match":"partial","distinction":"Odak dal çoğunlukla uygunsuzluk, hak aşımı veya gözü peklik bildirir; komşu dal nötr biçimde işe girmeyi anlatır.","focus_only":"Haksız veya uygunsuz şeye uzanma, gözü peklik ve araçsız kalkışma sınırlarını taşır.","gloss":"sınır aşan girişme ile işe başlama","neighbor_only":"Bir işe girme ve onunla uğraşmayı değer yargısı ya da gözü peklik koşulu olmadan anlatır.","neighbor_ref":"root_000789/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir işe girme ve onunla uğraşmaya başlama alanındadır."},{"boundary_match":"partial","distinction":"Odak dal hak aşımı ve yetersiz araçla kalkışmayı öne çıkarır; komşu dal korkutucu duruma düşünmeden atılmayı öne çıkarır.","focus_only":"Hakkı olmayan şeye uzanmayı, yüksek işe araçsız kalkışmayı ve sonuca varmayı da kapsar.","gloss":"gözü pek girişme ile düşünmeden atılma","neighbor_only":"Korkutucu veya çetin bir duruma düşünmeden atılmayı ve başkasını da oraya sokmayı kapsar.","neighbor_ref":"root_001202/B001","relation_type":"near_synonym","shared_zone":"İki dal da güç veya tehlike taşıyan bir işe çekinmeden girme yönünü paylaşır."},{"boundary_match":"partial","distinction":"Odak dal etkin bir girişim ve uğraş gerektirir; komşu dal yalnız yaklaşma veya sınırda bulunmayla gerçekleşebilir.","focus_only":"Bir işi üstlenip etkin biçimde girişmeyi ve kimi zaman onu sonuna vardırmayı anlatır.","gloss":"işe girişme ile sınırına yaklaşma","neighbor_only":"Bir şeye yaklaşma, onun sınırına gelme ve yasaklanan şeye yakın durma alanını taşır.","neighbor_ref":"root_001212/B007","relation_type":"near_neighbor","shared_zone":"İki dal da kişinin bir şeyle yakın ilişkiye girmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal girişimin kendisini ve sınırlarını anlatır; komşu dal karşılıklı uğraşın yalnızca üstün gelme sonucunu anlatır.","focus_only":"Uygunsuz şeye el uzatma ve tek başına bir işe gözü pekçe girişme yönünü taşır.","gloss":"işe girişme ile çekişmede yenme","neighbor_only":"Karşılıklı çekişmenin sonunda öteki kişiyi yenme sonucuna bağlıdır.","neighbor_ref":"root_001028/B007","relation_type":"near_neighbor","shared_zone":"İki dal da kişinin etkin bir uğraşa girmesini gerektiren bir olay alanındadır."}],"source_phrase_ar":"التعاطي تناول ما ليس له بحق ويتعاطى ظلم فلان وفتعاطى فعقر وعاط بغير أنواط (maqayis)؛ تعاطاه تناوله وفلان يتعاطى كذا أي يخوض فيه وفتعاطى فعقر (sihah)؛ التعاطي تناول ما لا يجوز تناوله وفتعاطى الشقي عقر الناقة فبلغ ما أراد وتعاطيه جرأته ويتعاطى معالي الأمور ورفيعها ويتعاطى أمرا قبيحا (tahdhib)","source_summary":"Kaynaklar uygunsuz bir şeye el uzatma ile bir işe girip uğraşma yönlerini bir arada verir; gözü pekçe sonuca gitme ve araçsız biçimde erişilmez işe kalkışma bu alanın özel görünümleridir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه تعاطي ما لا حق له به أو ما لا يجوز والخوض في الأمر والتطلع إلى الرفيع بلا آلة وبلوغ الفعل بجرأة","what_is_not_ar":"ليس المناولة المشروعة ولا العطاء ولا طلب العطاء"},"support_links":[]},{"boundary":"Dal veren kişiyi değil, başkalarından kendisine bir şey verilmesini isteyen kişiyi odaklar.","branch_kind":"bare","branch_ref":"root_001028/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:3:1","qac_word_ref":"92:5:3","surface_ar":"أَعْطَىٰ"}],"gloss":"insanlardan bir şey isteme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başkalarından kendisine bir şey vermelerini isteme eylemidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İsteyen kişinin avucunu insanlara doğru uzatması bu isteğe eşlik edebilir."}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin başkalarından kendisine bir şey vermelerini istediği temel kullanım için uygundur.","boundary_detail":"Dal veren kişiyi değil, başkalarından kendisine bir şey verilmesini isteyen kişiyi odaklar.","branch_image_ar":"استعطاء الناس","concept_gloss":"insanlardan bir şey isteme","contextual_glosses":[{"applicability":"İsteğin avuç uzatma hareketiyle birlikte açıkça gösterildiği bağlam için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şey istemeyi ve buna eşlik eden avuç uzatma hareketini korur."},"facet_ids":["F001","F002"],"text":"el açıp istemek","usage_role":"contextual"}],"definition":"İnsanlardan kendisine bir şey verilmesini istemektir. Bu istek, avuç uzatma hareketiyle açıkça gösterilebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başkalarından kendisine bir şey vermelerini isteme eylemidir."},{"facet_id":"F002","role":"associated_use","statement":"İsteyen kişinin avucunu insanlara doğru uzatması bu isteğe eşlik edebilir."}],"identity_rationale":"Kaynak anlatımı, insanlardan bir şey verilmesini istemeyi açıkça bildirir ve bu isteğin avuç uzatılarak gösterilebildiğini ekler. Eylemin çekirdeği istemektir; verme eylemi veya verilen nesne bu dalın kendisi değildir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bir şey verilmesini isteme"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bir şey verilmesini isteme"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"insanlardan bir şey isteme"}],"lexicalization_note":"Tanım yalnızca başkalarından bir şey isteme çekirdeğini verir ve bunu el uzatma örneğine ya da başka bir yapıya bağımlı kılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen beş ilişki yalın istemeyi el hareketi, boyun bükme, bağış, diretme ve gerçekleşmiş verme sınırlarında açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği istemektir ve el hareketi zorunlu değildir; komşu dal doğrudan avucu uzatma görünümüne bağlıdır.","focus_only":"İsteğin el hareketi olmadan sözle veya başka yolla bildirilmesini de kapsar.","gloss":"genel isteme ile avuç uzatma","neighbor_only":"Avucun insanlara doğru uzatılmasını eylemin belirleyici görünümü yapar.","neighbor_ref":"root_001308/B009","relation_type":"near_synonym","shared_zone":"İki dal da insanlardan bir şey isterken el açma durumunu kapsar."},{"boundary_match":"partial","distinction":"Odak dal yalın istemedir; komşu dal bu isteğe boyun bükme, başkasının fazlasını arama ve verileni kabul etme yönlerini ekler.","focus_only":"Başkasından verilmesini istemeyi boyun bükme veya verilenle yetinme koşulu olmadan anlatır.","gloss":"isteme ile boyun bükerek isteme","neighbor_only":"İsterken boyun bükmeyi, başkasının fazlasını aramayı ve verileni kabul etmeyi de kapsar.","neighbor_ref":"root_001263/B002","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak çekirdeği başkasından bir şey istemektir."},{"boundary_match":"partial","distinction":"Odak dal isteme eylemiyle sınırlıdır; komşu dal bağışın kabul edilmesini ve karşılıklı verilmesini de aynı alana katar.","focus_only":"İstenen şeyin bağış niteliğinde olmasını zorunlu kılmadan insanlardan verilmesini istemeyi anlatır.","gloss":"genel isteme ile bağış isteme","neighbor_only":"Bağış istemenin yanında bağışı kabul etmeyi ve kişilerin birbirine bağış vermesini de kapsar.","neighbor_ref":"root_001685/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir kişiden karşılıksız bir şey verilmesini istemeyi kapsayabilir."},{"boundary_match":"partial","distinction":"Odak dal ısrar gerektirmez; komşu dal isteğin yinelenmesini ve istenen kişiyi bunaltacak ölçüde sürdürülmesini gerektirir.","focus_only":"İsteğin bir kez ve ısrar göstermeden yapılabildiği nötr alanı kapsar.","gloss":"isteme ile diretici isteme","neighbor_only":"İsteği yineleyip karşı tarafı bunaltacak ölçüde diretme koşulunu taşır.","neighbor_ref":"root_001346/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişiden bir şey isteme eylemini anlatır."},{"boundary_match":"field_only","distinction":"Odak dalda aktarım istenir ama gerçekleşmiş olmak zorunda değildir; komşu dalda verme veya elden geçirme gerçekleşir.","focus_only":"İsteyen kişinin henüz gerçekleşmemiş bir verme eylemini başkasından beklemesini anlatır.","gloss":"isteme ile verme","neighbor_only":"Veren kişinin nesneyi gerçekten aktarmasını ve aktarılmış nesnenin kendisini anlatır.","neighbor_ref":"root_001028/B002","relation_type":"same_field","shared_zone":"İki dal aynı olası aktarımın isteyen ve veren yönleriyle ilgilidir."}],"source_phrase_ar":"استعطى وتعطى سأل العطاء (sihah)؛ يستعطي الناس بكفه وفي كفه استعطاء إذا سألهم وطلب إليهم (tahdhib)","source_summary":"Kaynaklar başkalarından bir şey verilmesini isteme çekirdeğinde birleşir; avuç uzatma, bu isteği dışa vuran eşlikçi hareket olarak belirtilir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه سؤال العطاء وطلبه من الناس","what_is_not_ar":"ليس نفس الإعطاء ولا العطية المعطاة ولا خدمة المعطي"},"support_links":[]},{"boundary":"Dal verme anlamına değil, canlıdaki dirençsizlik ile nesnedeki kolay bükülme ortaklığına dayanır.","branch_kind":"mixed_non_bare","branch_ref":"root_001028/B006","candidate_links":[{"candidate_id":"cand_565e5686d7eb6b5dd777","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:3:1","qac_word_ref":"92:5:3","surface_ar":"أَعْطَىٰ"}],"gloss":"direnmeden uyma ve kolay bükülme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Devenin direnmeyip kendisini yönlendiren kişiye uymasını anlatır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yayın sert ve direngen olmayıp kolayca bükülmesini ve gerilmesini anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bineğin yönlendirmeye uyarak başını biniciye doğru çevirmesini bildirir."}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlıdaki yönlendirmeye uyma ile nesnedeki kolay bükülme katmanlarını birlikte göstermek için uygundur.","boundary_detail":"Dal verme anlamına değil, canlıdaki dirençsizlik ile nesnedeki kolay bükülme ortaklığına dayanır.","branch_image_ar":"اللين والانقياد والمطاوعة","concept_gloss":"direnmeden uyma ve kolay bükülme","contextual_glosses":[{"applicability":"Deve veya bineğin kendisini yönlendiren kişiye karşı koymadığı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlının direnmemesini ve yönlendiren kişiye uymasını korur."},"facet_ids":["F001","F003"],"text":"direnmeyip yönlendirmeye uyma","usage_role":"contextual"},{"applicability":"Yayın sertçe karşı koymadan kolayca bükülüp gerildiği kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yayın yumuşaklığını, kolay bükülmesini ve gerilmeye karşı koymamasını korur."},"facet_ids":["F002"],"text":"kolay bükülen yay","usage_role":"contextual"}],"definition":"Canlı varlıkta direnmeyip yönlendirmeye uymayı, nesnede ise sertçe karşı koymadan kolayca bükülmeyi anlatır. Deve veya binek başını biniciye çevirir; yay da kolay gerilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Devenin direnmeyip kendisini yönlendiren kişiye uymasını anlatır."},{"facet_id":"F002","role":"core","statement":"Yayın sert ve direngen olmayıp kolayca bükülmesini ve gerilmesini anlatır."},{"facet_id":"F003","role":"specialization","statement":"Bineğin yönlendirmeye uyarak başını biniciye doğru çevirmesini bildirir."}],"identity_rationale":"Kaynak anlatımı canlı varlıkta direnmeyip yönlendirmeye uymayı, yayda ise sertçe karşı koymadan kolay bükülmeyi bildirir. Bineğin başını biniciye çevirmesi, canlıdaki uyma yönünün somut sonucudur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"devenin direnmeyip yönlendirmeye uyması"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kolay bükülen yumuşak yay"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"gerilirken direnmeyen yumuşak yay"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"boyun eğip başını biniciye çevir"}],"lexicalization_note":"Tanım, deve ve binek için yönlendirmeye uymayı yay için kolay bükülmeden ayırır; bu özel kullanımlar yalın verme anlamına taşınmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; seçilen beş ilişki canlıdaki uyma ile nesnedeki bükülmeyi genel boyun eğme, çeviklik, yumuşaklık, eğme ve yumuşak davranıştan ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal deve ve binekteki uyumu nesnedeki bükülmeyle bağlar; komşu dal insanı da kapsayan daha genel bir boyun eğme alanına yayılır.","focus_only":"Yayın kolay bükülmesini ve bineğin başını biniciye çevirmesini de kapsar.","gloss":"direnmeden uyma ile boyun eğme","neighbor_only":"İnsanların boyun eğmesini, alçak gönüllü uyumu ve buyruğa hızlı karşılık vermeyi de kapsar.","neighbor_ref":"root_000514/B001","relation_type":"near_synonym","shared_zone":"İki dal da canlı varlığın direnmeyip yönlendirmeye uymasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal direnç göstermeme ve bükülme üzerindedir; komşu dal buna hareket hafifliği ve adımların çevik aktarımını ekler.","focus_only":"Yayın bükülmesini ve bineğin başını sürücüye çevirmesini kapsar.","gloss":"uyma ile çevikçe izleme","neighbor_only":"İnsan veya atta hızlı izlemeyi, hafif bacakları ve düzgün adım aktarımını kapsar.","neighbor_ref":"root_001694/B005","relation_type":"near_synonym","shared_zone":"Her iki dal canlıda yumuşaklık ve yönlendirmeyi kolayca izleme yönünü paylaşır."},{"boundary_match":"partial","distinction":"Odak dal yumuşaklığı yaydaki bükülme ve canlıdaki uyma üzerinden belirler; komşu dal her türlü şeydeki genel yumuşaklıktır.","focus_only":"Canlının yönlendirmeye uymasını ve yayın gerilirken karşı koymamasını birlikte kapsar.","gloss":"kolay bükülme ile genel yumuşaklık","neighbor_only":"Yumuşaklığı belirli bir canlıya, nesneye veya yönlendirme ilişkisine bağlamadan geneller.","neighbor_ref":"root_001403/B008","relation_type":"near_neighbor","shared_zone":"İki dal da nesnede sertliğin karşıtı olan yumuşaklık yönünü taşır."},{"boundary_match":"partial","distinction":"Odak dal kolay bükülmeyi nesnenin niteliği olarak verir; komşu dal o şeyi koparmadan eğme eylemini öne çıkarır.","focus_only":"Canlıdaki yönlendirmeye uymayı ve yayın gerilmeye elverişli olmasını kapsar.","gloss":"bükülgenlik ile koparmadan eğme","neighbor_only":"Yumuşak bir dalı ya da deve boynunu koparmadan eğme eylemini anlatır.","neighbor_ref":"root_000417/B001","relation_type":"near_neighbor","shared_zone":"İki dal da yumuşak bir şeyin kırılmadan eğilebilmesini içerir."},{"boundary_match":"partial","distinction":"Odak dal hayvanın yönlendirilmesi ve yayın bükülmesiyle sınırlıdır; komşu dal insanın özenli ve yumuşak davranış niteliğidir.","focus_only":"Deve ve binekte dirençsiz uyumu, yayda ise somut bükülgenliği anlatır.","gloss":"dirençsiz uyma ile yumuşak davranma","neighbor_only":"İnsanın başkalarına karşı yumuşak, ölçülü ve aşağılanmadan uyumlu davranmasını anlatır.","neighbor_ref":"root_000519/B002","relation_type":"near_neighbor","shared_zone":"İki dal da sertçe karşı koymama ve yumuşak uyum gösterme alanındadır."}],"source_phrase_ar":"أعطى البعير إذا انقاد ولم يستعصب (sihah)؛ قوس عطوى مواتية سهلة (sihah)؛ قوس معطية لينة ليست بكزة ولا ممتنعة (tahdhib)؛ أعط فيعوج رأسه إلى راكبه (tahdhib)","source_summary":"Kaynaklar direnmeden uyma ve kolay bükülme ortaklığını deve, binek ve yay üzerinden verir; başın biniciye çevrilmesi, yönlendirmeye uymanın görünür sonucudur.","sources":["SI","TA"],"what_is_ar":"يدخل فيه انقياد البعير ولين القوس ومطاوعتها وانعطاف الراحلة لصاحبها","what_is_not_ar":"ليس الإعطاء المالي ولا التناول باليد ولا طلب العطاء"},"support_links":["sup_bb94f114e44ba5035266"]},{"boundary":"Dal genel uğraşmayı değil, karşılıklı çekişmede öteki kişiye üstün gelme sonucunu anlatır.","branch_kind":"non_bare","branch_ref":"root_001028/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:3:1","qac_word_ref":"92:5:3","surface_ar":"أَعْطَىٰ"}],"gloss":"karşılıklı çekişmede yenme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Karşılıklı çekişmenin sonunda öteki kişiye üstün gelip onu yenmeyi anlatır."}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki kişinin aynı uğraşta karşı karşıya geldiği ve birinin ötekini yendiği yapı için uygundur.","boundary_detail":"Dal genel uğraşmayı değil, karşılıklı çekişmede öteki kişiye üstün gelme sonucunu anlatır.","branch_image_ar":"الغلبة في التعاطي","concept_gloss":"karşılıklı çekişmede yenme","contextual_glosses":[{"applicability":"Konuşanın karşılıklı uğraşı ve kendi üstün gelme sonucunu birlikte aktardığı cümle için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı çekişmeyi, konuşanı ve onun yenme sonucunu korur."},"facet_ids":["F001"],"text":"çekiştik ve onu yendim","usage_role":"contextual"}],"definition":"İki kişinin karşılıklı bir çekişmeye girmesi ve birinin bu çekişmede ötekini yenmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Karşılıklı çekişmenin sonunda öteki kişiye üstün gelip onu yenmeyi anlatır."}],"identity_rationale":"Tek kaynak anlatımı, iki kişinin karşılıklı bir uğraşa girmesinden sonra konuşanın ötekini yenmesini bildirir. Bu nedenle dal genel üstünlükten çok, karşılıklı çekişme içindeki yenme sonucuna bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"karşılıklı çekişmede onu yenme"}],"lexicalization_note":"Anlam yalnızca karşılıklı çekişme ve ardından yenme bildiren yapıya bağlı tutulur; yalın köke genel yenme anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; seçilen beş ilişki bir tam eşdeğeri ve çekişme türü ya da sonuç genişliği bakımından en açıklayıcı dört yakın dalı gösterir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Anlam çekirdeği ve yapı sınırı örtüşür; iki dal bu kullanımda birbirinin yerine geçebilecek eşdeğer açıklamalar sunar.","focus_only":null,"gloss":"karşılıklı çekişmede üstün gelme","neighbor_only":null,"neighbor_ref":"root_000569/B005","relation_type":"synonym","shared_zone":"İki dal da karşılıklı çekişmeye girip öteki kişiyi yenmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal çekişmenin türünü açık bırakır; komşu dal üstün gelmeyi özellikle karşı çıkma ve uyuşmazlık alanına sınırlar.","focus_only":"Karşılıklı uğraşın türünü belirlemeden öteki kişiyi yenme sonucuna bağlanır.","gloss":"genel çekişmede yenme ile karşı çıkışta yenme","neighbor_only":"Yenmeyi özellikle karşı çıkma ve çekişmeli uyuşmazlık alanındaki yarışmaya bağlar.","neighbor_ref":"root_000808/B003","relation_type":"near_synonym","shared_zone":"İki dal da karşılıklı çekişmede rakibe üstün gelmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal genel bir karşılıklı uğraşa bağlıdır; komşu dal yarışmayı özellikle gelişlerin çokluğu üzerinden kurar.","focus_only":"Yarışın veya çekişmenin türünü sık gelme koşuluna bağlamadan yenmeyi anlatır.","gloss":"çekişmede yenme ile geliş sayısında yenme","neighbor_only":"Karşılıklı yarışmayı çok kez gelme ve bu sıklıkta ötekini geçme durumuna bağlar.","neighbor_ref":"root_000281/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da iki kişinin aynı davranışta yarışması ve birinin üstün gelmesi vardır."},{"boundary_match":"partial","distinction":"Odak dal yarışın niteliğini belirlemez; komşu dal onu böbürlenme ve büyüklük taslayarak karşı koyma biçimine bağlar.","focus_only":"Çekişmenin böbürlenme veya büyüklük taslama niteliği taşımasını gerektirmez.","gloss":"çekişmede yenme ile böbürlenme yarışında yenme","neighbor_only":"Yarışmayı böbürlenerek karşı koyma ve büyüklük taslama biçiminde kurar.","neighbor_ref":"root_001281/B011","relation_type":"near_synonym","shared_zone":"İki dal da bir rakiple karşılıklı yarışıp ona üstün gelmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal karşılıklı çekişme yapısına bağlıdır; komşu dal ise genel zafer, baskınlık ve bir şeyi kazanma alanına yayılır.","focus_only":"Yenmeyi belirli bir karşılıklı çekişme yapısının sonucu olarak bildirir.","gloss":"çekişmede yenme ile genel üstün gelme","neighbor_only":"Genel zaferi, baskıyla boyun eğdirmeyi, bir şeyi kazanmayı ve üstün kılmayı da kapsar.","neighbor_ref":"root_000965/B001","relation_type":"near_synonym","shared_zone":"İki dal da rakibe üstün gelme ve onu yenme sonucunda buluşur."}],"source_phrase_ar":"تعاطينا فعطوته أي غلبته (sihah)","source_summary":"Tek tanıklık, karşılıklı çekişmenin sonunda konuşanın öteki kişiye üstün gelerek onu yenmesini bildirir.","sources":["SI"],"what_is_ar":"يدخل فيه قولهم تعاطينا فعطوته أي غلبته","what_is_not_ar":"ليس العطاء ولا الاستعطاء ولا الانقياد ولا مطلق الخوض في الأمر"},"support_links":[]},{"boundary":"Dal genel koruma işlemini ve koruyucu aracı kapsar; kişinin kendini sakınması, ağırlık ölçüsü, hayvanın aksaması ve kuş adı bu sınıra girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B001","candidate_links":[{"candidate_id":"cand_3f15dc539a13a94bd6aa","lane":"macro"},{"candidate_id":"cand_acf054d8c135ca9e0851","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ٱتَّقَىٰ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{t~aqaY`|ROOT:wqy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:4:2","qac_word_ref":"92:5:4","surface_ar":"ٱتَّقَىٰ"}],"gloss":"araya engel koyarak zarardan koruma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Korunan şeyden zarar verici etkiyi uzak tutma ve onu incinmekten ya da bozulmaktan saklama işlemidir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koruma, zarar ile korunacak şey arasına başka bir araç, katman veya engel koyularak gerçekleştirilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kadının saçı ile dış örtüsü arasına koyduğu bez, bu koruyucu ara katmanın özel bir örneğidir."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel eylem ile koruyucu aracın ortak çekirdeğini, herhangi bir özel kullanım alanına bağlamadan karşılar.","boundary_detail":"Dal genel koruma işlemini ve koruyucu aracı kapsar; kişinin kendini sakınması, ağırlık ölçüsü, hayvanın aksaması ve kuş adı bu sınıra girmez.","branch_image_ar":"دفع الضرر بوقاية","concept_gloss":"araya engel koyarak zarardan koruma","contextual_glosses":[{"applicability":"Eylemden çok, zarar ile korunacak şey arasına koyulan araç veya katman kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Araya koyulan unsurun koruyucu işlevini ve zararı kesen konumunu korur."},"facet_ids":["F002"],"text":"koruyucu engel","usage_role":"contextual"},{"applicability":"Kadına ait özel bez kullanımını açıkça anlatan bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bezin yerini, maddi niteliğini ve koruyucu ara katman işlevini korur."},"facet_ids":["F003"],"text":"saç ile dış örtü arasındaki koruyucu bez","usage_role":"explanatory"}],"definition":"Bir şeyi ona zarar verecek başka bir şeyden korumak için araya bir araç ya da engel koyma ve böylece zararı ondan uzak tutma. Bu işlevi gören araç veya engel de aynı kavram alanında adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Korunan şeyden zarar verici etkiyi uzak tutma ve onu incinmekten ya da bozulmaktan saklama işlemidir."},{"facet_id":"F002","role":"core","statement":"Koruma, zarar ile korunacak şey arasına başka bir araç, katman veya engel koyularak gerçekleştirilir."},{"facet_id":"F003","role":"example","statement":"Kadının saçı ile dış örtüsü arasına koyduğu bez, bu koruyucu ara katmanın özel bir örneğidir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi ona zarar verecek başka bir şeyden korumayı ve bunun için araya koruyucu bir unsur koymayı ortak çekirdek olarak verir. Koruyucu bez örneği bu genel işlemin özel bir gerçekleşmesidir ve dalın kimliğini değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi koruyucu bir engelle zarardan saklamak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"koruma; zararı önleyen araç veya engel"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyi korumaya yarayan araç ya da engel"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"zarardan koruyan şey"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"zararı savan koruyucu"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kadının saçı ile dış örtüsü arasına koyduğu koruyucu bez"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"koruyucu şeyler"}],"lexicalization_note":"Tanım, genel koruma çekirdeğini özel ad ve kalıplardan ayırır; kadına ait koruyucu bez yalnızca yapıya bağlı bir örnek olarak tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlanan beş ilişki koruma çekirdeğine en yakın sınırları gösterir. Kale, bekçilik, tutunarak korunma, üstü açıklık ve öteki kök içi dallar ya daha uzak alan ortaklığı kurar ya da ayrı adlandırmalardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda ayırt edici unsur, başka bir şeyi koruyucu engel olarak araya koymaktır; komşu dalın çekirdeği ise etkiyi bulunduğu yerden itmek veya doğrudan savmaktır.","focus_only":"Koruma, zarar ile hedef arasına başka bir unsur koyma mekanizmasıyla tanımlanır.","gloss":"koruma ile itip uzaklaştırma","neighbor_only":"Öteki dal yer değiştirtmeyi, karşılıklı itişmeyi ve kötülüğü doğrudan savmayı da kapsar.","neighbor_ref":"root_000480/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da zararlı veya istenmeyen bir etkinin hedefe ulaşmasını engeller."},{"boundary_match":"partial","distinction":"Bu dal koruyucu engel üzerinden zararı savmaya odaklanır; komşu dal ise engel gerektirmeyen bakım, gözetim ve süreklilik taşıyan kollamayı da içerir.","focus_only":"Zararı kesen bir araç ya da engelin araya girmesi açıkça kurucu unsurdur.","gloss":"koruma ile gözetip kollama","neighbor_only":"Sürekli gözetme, bakım, kollama ve bir şeyi iyi durumda tutma süreçlerini de kapsar.","neighbor_ref":"root_000372/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi zarar ve bozulmadan uzak tutma alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal genel koruma işlemi ile onun aracını birlikte kapsar; komşu dal belirli bir koruyucu engel veya dayanak kavramında yoğunlaşır.","focus_only":"Koruma eylemi her tür araç veya katmanla gerçekleştirilebilir ve araç da adlandırılabilir.","gloss":"koruyucu araç ile koruyan engel","neighbor_only":"Koruyan ve çevreleyen belirli bir engel ya da dayanak adı merkezde yer alır.","neighbor_ref":"root_000071/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda bir engel, dış etkiden koruma ve çevreleyerek güvence sağlama işlevi görür."},{"boundary_match":"partial","distinction":"Komşu dal giysilerin birbirini koruduğu özel uygulamayı adlandırır; bu dal ise aynı araya koyma mekanizmasını her tür korunacak şeye açar.","focus_only":"Korunacak varlık ve zarar türü bakımından genel bir koruma şeması sunar.","gloss":"genel koruma ile giysiyi örtüyle koruma","neighbor_only":"Bir giysiyi başka bir giysiyle örtüp yıpranmaktan koruyan özel uygulamaya bağlıdır.","neighbor_ref":"root_001635/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir katman, başka bir şeyi yıpranma veya zarardan korur."},{"boundary_match":"partial","distinction":"Bu dal genel ve çoğu kez maddi koruma ilişkisini anlatır; komşu dal aynı şemayı kişinin kendi davranışını ve güvenliğini gözetmesine özgüler.","focus_only":"Korunan katılımcı herhangi bir nesne veya canlı olabilir ve maddi bir engel kullanılabilir.","gloss":"bir şeyi koruma ile kendini sakınma","neighbor_only":"Korunan katılımcı kişinin kendisidir; korkulan şeyden ve yanlış davranıştan sakınma öne çıkar.","neighbor_ref":"root_001677/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da zarar ile korunacak taraf arasına koruyucu bir mesafe veya önlem koyar."}],"source_phrase_ar":"دفع شيء عن شيء بغيره (maqayis)؛ كل ما وقى شيئا فهو وقاء له ووقاية (ayn;jamhara;tahdhib)؛ حفظ الشيء مما يؤذيه ويضره (mufradat)؛ وقاية المرأة وهي الخرقة التي بين جلبابها وشعرها (jamhara)","source_summary":"Kaynakların ortak anlatımı, korumayı zararlı etkiyi başka bir şey aracılığıyla savma olarak kurar; hem koruma eylemini hem de bu işte kullanılan engeli kapsar. Kadının saçını dış örtüden ayıran bez, bu mekanizmanın özel bir örneğidir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه وقى الشيء وحفظه مما يؤذيه، والوقاء والوقاية والواقية وما يجعل حاجزا بين الشيء والضرر، ووقاية المرأة","what_is_not_ar":"لا يدخل فيه اسم الوزن أوقية ولا اسم الصرد ولا الظلع اليسير إلا من جهة الصورة العامة للاتقاء"},"support_links":["sup_a6dfe3d3a07f8aaa114e","sup_ce7c7fe0943cf7b23fd5"]},{"boundary":"Dal kişinin kendisini koruması ve sakınmasıyla sınırlıdır; herhangi bir nesneyi koruma, yalnız başına iyi iş yapma veya işlenmiş yanlıştan dönme anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B002","candidate_links":[{"candidate_id":"cand_1460758e2c938f24657f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ٱتَّقَىٰ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{t~aqaY`|ROOT:wqy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:4:2","qac_word_ref":"92:5:4","surface_ar":"ٱتَّقَىٰ"}],"gloss":"korkulan şeyden ya da yanlış davranıştan kendini koruma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, korkulan ya da zarar verecek şey ile kendi arasına koruyucu bir önlem koyar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Öz-koruma, kişiyi suç doğuran ve yanlış sayılan davranışlardan uzak tutma biçimini alabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanrı'ya karşı gelmekten sakınma, kişi ile sakınılan sonuç arasına koruyucu bir tutum koymak olarak düşünülür."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem genel öz-koruma çekirdeğini hem de kişiyi yanlış davranıştan uzak tutan yönünü birlikte verir.","boundary_detail":"Dal kişinin kendisini koruması ve sakınmasıyla sınırlıdır; herhangi bir nesneyi koruma, yalnız başına iyi iş yapma veya işlenmiş yanlıştan dönme anlamına genişletilmez.","branch_image_ar":"جعل النفس في وقاية","concept_gloss":"korkulan şeyden ya da yanlış davranıştan kendini koruma","contextual_glosses":[{"applicability":"Korunulan tehlike veya yanlış davranış bağlamdan açıkça anlaşıldığında doğal ve kısa bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Korkulan şeyin veya yanlış davranışın türünü ve araya önlem koyma şemasını açıkça söylemez.","preserves":"Kişinin kendi güvenliğini ve davranışını gözeten öz-koruma yönünü korur."},"facet_ids":["F001","F002"],"text":"kendini sakınma","usage_role":"general"},{"applicability":"İnanç ve sorumluluk bağlamında, kişinin davranışını yasak olandan uzak tutması kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnanç bağlamındaki muhatabı, sakınma tutumunu ve yanlış davranıştan uzak durmayı korur."},"facet_ids":["F003"],"text":"Tanrı'ya karşı gelmekten sakınma","usage_role":"contextual"}],"definition":"Kişinin kendisini korktuğu veya zarar beklediği şeyden koruyacak bir önlem altına alması ve yanlış davranıştan uzak tutması. Tanrı'ya karşı gelmekten sakınma, bu öz-koruma tutumunun inanç alanındaki özel biçimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, korkulan ya da zarar verecek şey ile kendi arasına koruyucu bir önlem koyar."},{"facet_id":"F002","role":"specialization","statement":"Öz-koruma, kişiyi suç doğuran ve yanlış sayılan davranışlardan uzak tutma biçimini alabilir."},{"facet_id":"F003","role":"specialization","statement":"Tanrı'ya karşı gelmekten sakınma, kişi ile sakınılan sonuç arasına koruyucu bir tutum koymak olarak düşünülür."}],"identity_rationale":"Kaynak ifadesi, kişinin kendisini korktuğu şeyden koruma altına almasını ve yanlış davranıştan uzak tutmasını aynı öz-koruma şemasında birleştirir. Tanrı'ya karşı gelmekten sakınma bu çekirdeğin inanç alanındaki belirgin gerçekleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kendini korkulan ya da zarar verecek şeyden korumak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyi kendine koruyucu yapmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"Tanrı'ya karşı gelmekten sakınmak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kişinin kendini korktuğu şeyden ve yanlış davranıştan koruması"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"sakınma ve kendini koruma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sakınan ve kendini yanlış davranıştan koruyan kimse"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"sakınma; kendini kötülükten koruma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"sakınıp kendini koruma"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kendini yanlış davranışlardan koruyan kimse"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"sakınan ve kendini yanlış davranıştan koruyan kimse"}],"lexicalization_note":"Genel öz-koruma anlamı ile bir aracı kendine koruyucu yapma ve Tanrı'ya karşı gelmekten sakınma kalıpları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler genel koruma, yanlıştan uzak durma, iyi davranış, suç korkusu ve tapınma sınırlarını en açık biçimde gösterir. Bağışlanma, tövbeye çağırma, benlik ve örtü adayları daha dolaylıdır; öteki kök içi dallar ayrı anlamlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal genel koruma şemasını kişinin kendi güvenliğine ve davranışına taşır; komşu dal katılımcıyı ve zarar türünü sınırlandırmayan genel korumadır.","focus_only":"Korunan taraf zorunlu olarak kişinin kendisidir ve davranışsal sakınma da kapsama girer.","gloss":"kendini sakınma ile genel koruma","neighbor_only":"Herhangi bir nesne veya canlı, maddi bir araç ya da engel kullanılarak korunabilir.","neighbor_ref":"root_001677/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da zarar ile korunacak taraf arasına koruyucu bir önlem koyma şeması vardır."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği önleyici öz-korumadır; komşu dal ise yanlış karşısında çekinmenin yanında işlenmiş bir yanlıştan çıkma sonucunu da kapsar.","focus_only":"Henüz gerçekleşmemiş tehlikeden ve yanlış davranıştan önleyici biçimde korunmayı da kapsar.","gloss":"yanlıştan sakınma ile yanlışın yükünden çıkma","neighbor_only":"İşlenmiş bir yanlışın yükünden çıkma ve ondan dönmüş olma anlamına kadar uzanabilir.","neighbor_ref":"root_000013/B002","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin yanlış davranıştan uzak durmasını ve suç doğuran eylemi işlememesini anlatabilir."},{"boundary_match":"partial","distinction":"Bu dal koruyucu ve kaçınmacı tutumu tanımlar; komşu dal ise sakınmanın ötesinde olumlu iyilik ve itaat eylemlerini geniş biçimde kapsar.","focus_only":"Korkulan sonuç ile kişi arasına koruyucu bir sakınma tutumu koymak merkezde yer alır.","gloss":"sakınma ile iyilik ve itaat","neighbor_only":"İyi olma, itaat ve çok çeşitli yararlı işleri yapma yönünde olumlu bir eylem alanı sunar.","neighbor_ref":"root_000104/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal doğru davranışa yönelmeyi ve yanlış olandan uzak kalmayı destekler."},{"boundary_match":"partial","distinction":"Bu dal koruyucu davranış ve uzak durma eylemidir; komşu dal ise suç durumunu ve ona düşme korkusunu merkeze alır.","focus_only":"Kişinin korkulan veya suç doğuran durumdan kendini etkin biçimde korumasını anlatır.","gloss":"suçtan korunma ile suç korkusu","neighbor_only":"Suçun kendisini, suç kazanmayı ve kötü davranışa düşme korkusunu adlandırır.","neighbor_ref":"root_001051/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da yanlış davranış, onun doğuracağı yük ve bundan duyulan korku bulunur."},{"boundary_match":"field_only","distinction":"Ortak alan inanç ve sorumluluktur; bu dal sakınma yoluyla öz-korumayı, komşu dal ise tapınma ve yakınlık arama eylemini tanımlar.","focus_only":"Yanlış davranıştan uzak durarak kişinin kendisini koruması öne çıkar.","gloss":"sakınma ile tapınma","neighbor_only":"Tapınma, yakınlık arama ve kulluk eylemlerini olumlu uygulamalar olarak adlandırır.","neighbor_ref":"root_001498/B001","relation_type":"same_field","shared_zone":"İki dal inanç alanında kişinin Tanrı karşısındaki davranışını konu edinir."}],"source_phrase_ar":"اتق الله توقه أي اجعل بينك وبينه كالوقاية (maqayis)؛ التقوى في الأصل وقوى فعلى من وقيت (ayn;tahdhib)؛ التقوى جعل النفس في وقاية مما يخاف (mufradat)؛ حفظ النفس عما يؤثم (mufradat)؛ اتقى تقية وتقاة (sihah)","source_summary":"Kaynaklar bu dalı, kişinin kendisini korkulan şey karşısında koruma altına alması ve yanlış davranıştan uzak tutması olarak açıklar. İnanç bağlamındaki kullanım, Tanrı'ya karşı gelmekten sakınmayı kişi ile kötü sonuç arasındaki koruyucu tutum şeklinde somutlaştırır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اتقى واتقاء وتقوى وتقى وتقاة وتقية وتقي، أي توقي الله أو النار أو المعاصي أو ما يخاف","what_is_not_ar":"لا يدخل فيه مطلق الوقاية المادية إلا إذا صار اتقاء للنفس"},"support_links":["sup_7dfd247afe878c202c27"]},{"boundary":"Çekirdek hafif topallama ve ağrılı ya da hassas toynak yüzünden sakınarak yürümedir; eyer, emir ve sert zemin kullanımları bağımlı yan kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B003","candidate_links":[{"candidate_id":"cand_81ab5e5bb3ef8ad1f2ca","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ٱتَّقَىٰ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{t~aqaY`|ROOT:wqy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:4:2","qac_word_ref":"92:5:4","surface_ar":"ٱتَّقَىٰ"}],"gloss":"hafif topallama ve toynak ağrısıyla yürümekten çekinme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tek sözcüklü temel anlam, hayvanın yürüyüşündeki hafif topallamadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"At, topalladığı veya toynağındaki ağrı yüzünden yürümekten çekindiği ve sert zeminde ayağını sakındığı için bu nitelemeyi alır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvana yönelik emir kalıbı, onun aksayışını gözeterek yürümeyi sürdürme ve kendini zorlamama anlamı taşır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Eyer için kullanıldığında hayvanın sırtını yaralamayan veya berelenmesine yol açmayan eyer anlatılır."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Sert ve engebeli zeminle kurulan olumsuz emir, arazinin güçlüğünden yakınmama anlamına gelir."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın tek sözcüklü çekirdeğini ve atın ağrılı ya da hassas toynak nedeniyle gösterdiği sakınan yürüyüşü birlikte karşılar.","boundary_detail":"Çekirdek hafif topallama ve ağrılı ya da hassas toynak yüzünden sakınarak yürümedir; eyer, emir ve sert zemin kullanımları bağımlı yan kullanımlardır.","branch_image_ar":"توقي الدابة من وجع الحافر","concept_gloss":"hafif topallama ve toynak ağrısıyla yürümekten çekinme","contextual_glosses":[{"applicability":"Tek sözcüklü durum adı, neden veya hayvanın türü ayrıca belirtilmeden kullanıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aksamanın hafif derecesini ve yürüyüş bozukluğu olmasını doğrudan korur."},"facet_ids":["F001"],"text":"hafif topallama","usage_role":"general"},{"applicability":"Atın topallaması veya toynak acısı yüzünden adım atmaktan çekinmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan türünü, toynaktaki ağrıyı ve bunun yol açtığı çekingen yürüyüşü korur."},"facet_ids":["F002"],"text":"toynak ağrısıyla yürümekten çekinen at","usage_role":"explanatory"},{"applicability":"Topallayan hayvana ya da biniciye, mevcut aksamayı gözeterek yürümeyi sürdürmesi söylendiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aksamayı sürdürme, onu hesaba katma ve hareketi zorlamama yönündeki emri korur."},"facet_ids":["F003"],"text":"aksayışını gözet ve ağırdan al","usage_role":"contextual"},{"applicability":"Eyerin hayvanın sırtında yara veya bere oluşturmadığı belirtilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eyerin türünü ve hayvanın sırtını yaralamama sonucunu açıkça korur."},"facet_ids":["F004"],"text":"yara açmayan eyer","usage_role":"contextual"}],"definition":"Hafif topallama ile, özellikle toynak ağrısı veya hassasiyeti yüzünden yürümekten çekinen ya da sert zeminde ayağını sakınan atın durumu. Aynı kullanım kümesi, hayvanın aksamasına göre davranmayı, sert zeminden yakınmamayı ve hayvanda yara açmayan eyeri de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tek sözcüklü temel anlam, hayvanın yürüyüşündeki hafif topallamadır."},{"facet_id":"F002","role":"specialization","statement":"At, topalladığı veya toynağındaki ağrı yüzünden yürümekten çekindiği ve sert zeminde ayağını sakındığı için bu nitelemeyi alır."},{"facet_id":"F003","role":"associated_use","statement":"Hayvana yönelik emir kalıbı, onun aksayışını gözeterek yürümeyi sürdürme ve kendini zorlamama anlamı taşır."},{"facet_id":"F004","role":"associated_use","statement":"Eyer için kullanıldığında hayvanın sırtını yaralamayan veya berelenmesine yol açmayan eyer anlatılır."},{"facet_id":"F005","role":"associated_use","statement":"Sert ve engebeli zeminle kurulan olumsuz emir, arazinin güçlüğünden yakınmama anlamına gelir."}],"identity_rationale":"Kaynak ifadesi yalnızca toynak ağrısından kaçınmayı değil, hafif topallamayı, topallayan atın davranışını, hayvanda yara açmayan eyeri ve aksayışa göre davranma sözünü birlikte verir. Bu nedenle dal korunabilir, fakat geçici hayvanın kendini koruması çerçevesi bütün malzemeyi taşıyacak biçimde aksama ve ona bağlı kullanımlar olarak yeniden kurulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"hafif topallama"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"topallayan, toynak ağrısıyla yürümekten çekinen veya ayağını sert zeminden sakınan at"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"hayvanın sırtında yara açmayan eyer"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"aksayışını gözet ve ağırdan al"}],"lexicalization_note":"Tek sözcüklü hafif topallama anlamı, atın yürüyüşü ile eyer ve emir kalıplarına bağlı anlamlardan açıkça ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan ilişkiler genel aksama, uzuv hastalığı, toynak anatomisi ve koruma bağlantısını ayırır. Keçi hastalıkları, düzensiz yürüyüş, binme ve öteki kök içi dallar daha uzak alan ortaklıklarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal hafif dereceyi ve toynak ağrısına bağlı çekingen yürüyüşü belirginleştirir; komşu dal daha genel aksama durumunda kalır.","focus_only":"Toynak ağrısıyla yürümekten çekinme ile yara açmayan eyer ve emir gibi bağımlı kullanımları da kapsar.","gloss":"hafif topallama ile hayvandaki genel aksama","neighbor_only":"Hayvandaki aksama veya eziklik daha genel bir durum adı olarak verilir ve koruyucu yan kullanımlar taşımaz.","neighbor_ref":"root_000448/B009","relation_type":"near_synonym","shared_zone":"Her iki dal hayvanın, özellikle atın, aksayan veya topallayan yürüyüşünü anlatır."},{"boundary_match":"partial","distinction":"Bu dal ağrının yürüyüşteki belirtisini ve sakınma davranışını anlatır; komşu dal ise ağrıyı doğuran hastalık veya yaralanmanın kendisini adlandırır.","focus_only":"Ağrıya verilen topallama ve yürümekten çekinme tepkisi ile ona bağlı kullanımlar merkezde yer alır.","gloss":"ağrılı yürüyüş ile uzuvdaki hastalık","neighbor_only":"Omuz veya toynağı etkileyen hastalığı ve taşın tırnak ya da toynağı çizmesini doğrudan adlandırır.","neighbor_ref":"root_001546/B006","relation_type":"near_neighbor","shared_zone":"İki dal toynak veya başka bir uzuvdaki ağrı ve bunun hayvan üzerindeki etkisiyle ilgilidir."},{"boundary_match":"field_only","distinction":"Ortak alan toynaktır; bu dal toynağa bağlı ağrı ve yürüyüş davranışını, komşu dal ise anatomik uzvun kendisini tanımlar.","focus_only":"Toynak ağrısının yol açtığı topallama ve sakınan yürüyüşü anlatır.","gloss":"toynak ağrısıyla yürüme ile toynak","neighbor_only":"Toynağın kendisini, biçimini ve zeminde iz açan uzuv olmasını adlandırır.","neighbor_ref":"root_000341/B002","relation_type":"same_field","shared_zone":"Her iki dal atın veya başka bir hayvanın toynağını ortak katılımcı olarak içerir."},{"boundary_match":"field_only","distinction":"Bu dal bir yürüyüş durumu ve ağrı tepkisidir; komşu dal ise toynağın sağ ve sol yanlarını gösteren anatomik addır.","focus_only":"Hayvanın ağrı nedeniyle aksaması ve sert zeminde ayağını sakınması bulunur.","gloss":"toynak ağrısı ile toynağın yanları","neighbor_only":"Toynağın iki yanındaki belirli anatomik bölümleri adlandırır.","neighbor_ref":"root_000358/B010","relation_type":"same_field","shared_zone":"Her iki dal toynak yapısı ve hayvanın ayağı çevresindeki aynı somut alana bağlıdır."},{"boundary_match":"thematic_only","distinction":"Koruma bu dalda yalnızca bazı at ve eyer kullanımlarının bağımlı yönüdür; komşu dalda ise bütün kavramın genel çekirdeğidir.","focus_only":"Hafif topallama ve ağrı yüzünden sakınarak yürüme, dalın temel kimliğini oluşturur.","gloss":"aksayarak sakınma ile genel koruma","neighbor_only":"Her tür varlığı zarardan korumak için araya araç veya engel koyan genel işlemi tanımlar.","neighbor_ref":"root_001677/B001","relation_type":"thematic","shared_zone":"Atın ayağını sert zeminden sakınması ve eyerin yara açmaması koruma düşüncesiyle ilişki kurar."}],"source_phrase_ar":"الوقى هو الظلع اليسير (maqayis)؛ فرس واق إذا كان ظالعا (ayn)؛ ق على ظلعك أي الزمه (sihah)؛ فرس واق إذا كان يهاب المشي من وجع يجده في حافره (sihah)؛ سرج واق إذا لم يكن معقرا (sihah;tahdhib)؛ لا تقي بالجدجد أي لا تشتكي حزونة الأرض (tahdhib)","source_summary":"Toplu kaynak ifadesi hafif topallamayı çekirdek yapar ve bunu topallayan, toynak ağrısı yüzünden yürümekten çekinen ya da sert zeminde ayağını sakınan atla açımlar. Aksamaya göre davranma, sert zeminden yakınmama ve yara açmayan eyer kullanımları aynı kümede yer alan fakat çekirdeğe bağımlı yan kullanımlardır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الوَقَى بمعنى الظلع اليسير، والفرس الواقي إذا يهاب المشي أو يقي حافره الموضع الغليظ، والسرج الواقي غير المعقر","what_is_not_ar":"لا يدخل فيه الوقاية العامة ولا التقوى ولا اسم الصرد"},"support_links":["sup_a16f26c6a1af947827bc"]},{"boundary":"Dal yalnızca bu adlandırılmış ağırlık ölçüsü ve onun biçimleriyle sınırlıdır; genel tartma eylemine, her türlü miktara veya modern bir ölçü adına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱتَّقَىٰ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{t~aqaY`|ROOT:wqy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:4:2","qac_word_ref":"92:5:4","surface_ar":"ٱتَّقَىٰ"}],"gloss":"kırk gümüş para ağırlığındaki, yağda yedi birimlik biçimi bulunan ölçü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel biçim, belirli bir ağırlık ölçüsüdür ve para hesabında kırk gümüş paranın ağırlığına eşitlenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başındaki ses düşmüş biçim, yağ ölçümünde kullanılan ve yedi temel ağırlık birimine eşit sayılan ayrı bir değeri bildirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başlangıç sesini koruyan biçim daha düzgün kabul edilir ve ölçü adının iki çoğul söylenişi kaydedilir."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölçü ailesinin iki bağlama göre değişen değerini tek açıklayıcı karşılıkta birlikte göstermenin gerektiği yerlerde kullanılır.","boundary_detail":"Dal yalnızca bu adlandırılmış ağırlık ölçüsü ve onun biçimleriyle sınırlıdır; genel tartma eylemine, her türlü miktara veya modern bir ölçü adına genişletilmez.","branch_image_ar":"الأوقية وزن معلوم","concept_gloss":"kırk gümüş para ağırlığındaki, yağda yedi birimlik biçimi bulunan ölçü","contextual_glosses":[{"applicability":"Para ağırlığının esas alındığı ilk biçim ve kullanım kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölçünün ağırlık niteliğini ve kırk gümüş para ağırlığına eşit değerini korur."},"facet_ids":["F001"],"text":"kırk gümüş para ağırlığına denk ölçü","usage_role":"contextual"},{"applicability":"Başındaki ses düşmüş biçimin yağ ölçümündeki özel değeri açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağ bağlamını, ağırlık ölçüsü olmasını ve yedi temel birime eşit değeri korur."},"facet_ids":["F002"],"text":"yağ için yedi temel birimlik ağırlık ölçüsü","usage_role":"explanatory"},{"applicability":"Ölçü adının birden fazla çoğul söylenişi bulunduğu açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Söz konusu biçimlerin aynı ağırlık ölçüsü adının çoğulları olmasını korur."},"facet_ids":["F003"],"text":"bu ağırlık ölçüsünün çoğul biçimleri","usage_role":"explanatory"}],"definition":"Bir kullanımda kırk gümüş paranın ağırlığına, başındaki ses düşmüş başka bir biçim ve kullanımda ise yağ için yedi temel ağırlık birimine eşit kabul edilen ölçü. İlk biçim daha düzgün sayılır ve birden çok çoğul biçimi vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel biçim, belirli bir ağırlık ölçüsüdür ve para hesabında kırk gümüş paranın ağırlığına eşitlenir."},{"facet_id":"F002","role":"source_variant","statement":"Başındaki ses düşmüş biçim, yağ ölçümünde kullanılan ve yedi temel ağırlık birimine eşit sayılan ayrı bir değeri bildirir."},{"facet_id":"F003","role":"source_variant","statement":"Başlangıç sesini koruyan biçim daha düzgün kabul edilir ve ölçü adının iki çoğul söylenişi kaydedilir."}],"identity_rationale":"Kaynak ifadesi dalı bilinen bir ağırlık ölçüsü olarak doğrular, ancak tek ve değişmez bir nicelik vermez. Bir kullanım kırk gümüş para ağırlığını, başındaki ses düşmüş başka bir biçim ise yağ için yedi temel ağırlık birimini gösterir; tanım bu bağlam farkını açıkça korumalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kırk gümüş para ağırlığına eşit bilinen ölçü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yağ için yedi temel ağırlık birimine eşit ölçü"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bu ağırlık ölçüsü adının çoğul biçimleri"}],"lexicalization_note":"Tanım, iki sözcük biçimine bağlı farklı ölçü değerlerini ve çoğul biçimleri ayırır; bunlardan genel bir kök anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlananlar genel ağırlık, küçük para ölçüsü, başka geleneksel birim, hacim-miktar ölçüsü ve ayar standardı sınırlarını gösterir. Artış ve çok büyük tahıl ölçüsü daha uzaktır; öteki kök içi dallar anlamsal olarak ayrıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal değerleri ve sözcük biçimleri belirlenmiş tek bir geleneksel ölçüyü adlandırır; komşu dal ağırlık ve tartma alanının genel kavramıdır.","focus_only":"Bağlama göre kırk gümüş para veya yedi temel birim değerini taşıyan belirli bir ölçü adıdır.","gloss":"özel ağırlık ölçüsü ile genel tartma","neighbor_only":"Ağırlık, tartı aracı ve bir şeye ağırlığını verme gibi genel ölçme alanını kapsar.","neighbor_ref":"root_000202/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal belirlenmiş ağırlık ve ölçme düşüncesinde buluşur."},{"boundary_match":"partial","distinction":"Ölçülerin adları ve değerleri ayrıdır: bu dal kırk paralık değeri ve yağdaki değişkeyi taşırken komşu dal çoğunlukla beş paralık küçük miktarı bildirir.","focus_only":"Para hesabında kırk gümüş para ağırlığına veya yağda yedi birime bağlanan ölçüdür.","gloss":"kırk paralık ölçü ile beş paralık ölçü","neighbor_only":"Altın veya gümüş için kullanılan, çoğunlukla beş gümüş para ağırlığıyla açıklanan daha küçük ölçüdür.","neighbor_ref":"root_001570/B004","relation_type":"near_neighbor","shared_zone":"İki dal da değerli maden veya para üzerinden açıklanan geleneksel ağırlık ölçüleridir."},{"boundary_match":"partial","distinction":"Bu dalın ölçü adı ve verilen değerleri kendine özgüdür; komşu dal başka birim adını ve ağırlığın yanında hacim kullanımını kapsar.","focus_only":"İki sözcük biçimi ve iki bağlamsal değeri bulunan belirli bir ağırlık ölçüsüdür.","gloss":"iki ayrı geleneksel ölçü adı","neighbor_only":"Başka bir adla anılan, hem ağırlık hem hacim ölçüsü olabilen ayrı bir geleneksel birimdir.","neighbor_ref":"root_001449/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli adları, tekil ve çoğul biçimleri bulunan geleneksel ölçü birimleridir."},{"boundary_match":"partial","distinction":"Bu dal ağırlığa ve belirli değerlere bağlıdır; komşu dal hacim ile para miktarı arasında daha geniş bir ölçüm alanına yayılır.","focus_only":"Öncelikle ağırlık ölçüsüdür ve iki özel sayısal değere bağlanır.","gloss":"ağırlık ölçüsü ile hacim ve miktar ölçüsü","neighbor_only":"Hacim ölçüsünü, yarım başka bir hacim ölçüsünü ve para miktarını birlikte kapsayabilir.","neighbor_ref":"root_001224/B007","relation_type":"near_neighbor","shared_zone":"İki dal da sayılabilir veya ölçülebilir bir miktarı geleneksel birimle belirtir."},{"boundary_match":"field_only","distinction":"Bu dal ölçülen miktarı bildiren birimdir; komşu dal ise ölçü araçlarının ve paraların doğruluğunu belirleyen ayar standardıdır.","focus_only":"Kendi adı, biçimleri ve geleneksel değerleri bulunan ölçü birimini tanımlar.","gloss":"ölçü birimi ile ölçü ayarı","neighbor_only":"Ölçekleri ve paraları denetlemeye yarayan ayarı veya ölçünleme işlemini tanımlar.","neighbor_ref":"root_001066/B013","relation_type":"same_field","shared_zone":"Her iki dal doğru ağırlık ve ölçü değerinin belirlenmesi alanındadır."}],"source_phrase_ar":"الأوقية في الحديث أربعون درهما (sihah;tahdhib)؛ الوقية وزن من أوزان الدهن وهي سبعة مثاقيل (tahdhib)؛ اللغة الجيدة أوقية وجمعها أواقي وأواق (tahdhib)","source_summary":"Toplu kaynak anlatımı, aynı ölçü ailesinde bağlama ve sözcük biçimine göre iki değer aktarır: para hesabında kırk gümüş para ağırlığı ve yağ hesabında yedi temel ağırlık birimi. Başlangıç sesini taşıyan biçim daha düzgün kabul edilir; ölçü adının iki çoğul biçimi de verilir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الأوقية والأواقي بوصفها وزنا معلوما للدراهم أو الدهن","what_is_not_ar":"لا يدخل فيه الوقاية ولا التقوى ولا الواقي بمعنى الصرد"},"support_links":[]},{"boundary":"Dal yalnızca örümcek kuşunun bu iki adına ve adlandırma açıklamasına aittir; koruyan kişi, topallayan at veya yara açmayan eyer anlamlarına geçmez.","branch_kind":"non_bare","branch_ref":"root_001677/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱتَّقَىٰ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{t~aqaY`|ROOT:wqy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:4:2","qac_word_ref":"92:5:4","surface_ar":"ٱتَّقَىٰ"}],"gloss":"örümcek kuşu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, örümcek kuşunu adlandıran özel bir kuş adıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuş adı, son sesi bulunan daha uzun ve bu sesin düştüğü daha kısa iki biçimde kullanılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adın kuşa verilmesi, yürürken adımlarını fazla açmayan kısa adımlı yürüyüşüyle açıklanır."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kuş türünün Türkçedeki doğal adı olarak dalın adlandırma çekirdeğini doğrudan karşılar.","boundary_detail":"Dal yalnızca örümcek kuşunun bu iki adına ve adlandırma açıklamasına aittir; koruyan kişi, topallayan at veya yara açmayan eyer anlamlarına geçmez.","branch_image_ar":"الواقي اسم للصرد","concept_gloss":"örümcek kuşu","contextual_glosses":[{"applicability":"Kuş adının yürüyüş biçimiyle ilişkilendirilen açıklaması da bağlamda görünür kılınmak istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuş türünü ve adlandırmaya gerekçe gösterilen kısa adımlı yürüyüş özelliğini birlikte korur."},"facet_ids":["F001","F003"],"text":"kısa adımlarla yürüyen örümcek kuşu","usage_role":"explanatory"}],"definition":"Örümcek kuşunun, biri son sesi koruyan diğeri bu sesi düşüren iki biçimde söylenen adı. Adlandırma, kuşun yürürken adımlarını fazla açmamasıyla açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, örümcek kuşunu adlandıran özel bir kuş adıdır."},{"facet_id":"F002","role":"source_variant","statement":"Kuş adı, son sesi bulunan daha uzun ve bu sesin düştüğü daha kısa iki biçimde kullanılır."},{"facet_id":"F003","role":"associated_use","statement":"Adın kuşa verilmesi, yürürken adımlarını fazla açmayan kısa adımlı yürüyüşüyle açıklanır."}],"identity_rationale":"Kaynak ifadesi dalı doğrudan örümcek kuşunun adı olarak verir, adın son sesi bulunan ve düşmüş iki biçimini kaydeder ve adlandırmayı kuşun yürürken adımlarını fazla açmamasına bağlar. Geçici çerçeve bu sınırı doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"örümcek kuşu; aynı kuş adının uzun ve kısalmış biçimleri"}],"lexicalization_note":"Tanım, kuşa verilmiş iki özel ad biçimiyle sınırlı tutulur ve bunlardan genel bir koruma ya da yürüme anlamı türetilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan dört karşılaştırma kuş adları arasındaki tür ayrımını yeterince gösterir. Öteki kuş adayları da yalnızca aynı alanı paylaşır; kurt adı ile koruma, ağırlık ve hayvan yürüyüşü dalları farklı kimliklerdir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortaklık yalnızca kuş adı olmalarıdır; bu dal örümcek kuşunu, komşu dal ise ibibiği adlandırır ve türler birbirinin yerine geçmez.","focus_only":"Örümcek kuşunu ve onun kısa adımlı yürüyüşüne bağlanan adını belirtir.","gloss":"örümcek kuşu ile ibibik","neighbor_only":"İbibik kuşunu ve o kuşa ait ad biçimlerini belirtir.","neighbor_ref":"root_001580/B005","relation_type":"same_field","shared_zone":"Her iki dal belirli bir kuş türünü doğrudan adlandıran sözleri içerir."},{"boundary_match":"field_only","distinction":"Bu dal örümcek kuşunun adıdır; komşu dal tarla kuşunun adıdır. Aynı üst alanda bulunsalar da tür kimlikleri ayrıdır.","focus_only":"Kısa adımlı yürüyüşüyle açıklanan örümcek kuşu adı merkezde yer alır.","gloss":"örümcek kuşu ile tarla kuşu","neighbor_only":"Tarla kuşunu ve ona ait farklı ad biçimlerini belirtir.","neighbor_ref":"root_001195/B003","relation_type":"same_field","shared_zone":"İki dal da küçük kuş türlerine verilmiş adları ve bu adların biçimlerini ele alır."},{"boundary_match":"field_only","distinction":"Anlamsal ortaklık kuş kategorisiyle sınırlıdır; dallar büyüklük, yapı ve tür bakımından bütünüyle farklı kuşları adlandırır.","focus_only":"Örümcek kuşunun özel adını bildirir.","gloss":"örümcek kuşu ile deve kuşu","neighbor_only":"Çok daha büyük ve uçamayan deve kuşunun tür adını bildirir.","neighbor_ref":"root_001525/B006","relation_type":"same_field","shared_zone":"Her iki dal bir kuş türünün doğrudan adı olarak kullanılır."},{"boundary_match":"field_only","distinction":"Bu dalın göndergesi örümcek kuşudur; komşu dal başka bir küçük kuş türünü adlandırır ve ortak kuş alanı tür özdeşliği oluşturmaz.","focus_only":"Örümcek kuşunu adlandırır ve adını kuşun yürüyüşüyle ilişkilendirir.","gloss":"örümcek kuşu ile bir serçe türü","neighbor_only":"Serçelere benzeyen başka bir küçük kuş türünün adını bildirir.","neighbor_ref":"root_000465/B008","relation_type":"same_field","shared_zone":"İki dal da küçük kuşlardan birine verilmiş sözlü adları taşır."}],"source_phrase_ar":"الواقي الصرد (sihah;tahdhib)؛ الواق بكسر القاف بلا ياء (sihah)؛ قيل للصرد واق لأنه لا ينبسط في مشيه (tahdhib)","source_summary":"Kaynakların ortak anlatımı bu sözcüğü örümcek kuşunun adı olarak tanımlar ve son sesi bulunan biçimin yanında o sesin düştüğü kısa biçimi de kaydeder. Adın nedeni, kuşun yürürken adımlarını fazla açmaması olarak açıklanır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الواقي والواق اسما للصرد","what_is_not_ar":"لا يدخل فيه الواقي بمعنى الدافع ولا الفرس الواقي ولا السرج الواقي"},"support_links":[]},{"boundary":"Includes a downward twist or spin and a thrust directed level with the face.","branch_kind":null,"branch_ref":"root_001694/B009","candidate_links":[{"candidate_id":"cand_565e5686d7eb6b5dd777","lane":"macro"}],"focus_root_occurrences":[],"gloss":"downward twist or face-level thrust","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"فتل إلى أسفل وطعن حذاء الوجه","image_en":"downward twist or face-level thrust"}}],"root_ar":"ي س ر","root_id":"root_001694","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"فتل إلى أسفل وطعن حذاء الوجه","image_en":"downward twist or face-level thrust","scope_ar":"يدخل فيه اليسر في الفتل إلى أسفل، والطعن اليسر حذاء الوجه.","scope_en":"Includes a downward twist or spin and a thrust directed level with the face."},"support_links":["sup_bb94f114e44ba5035266"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000089/B001","candidate_links":[{"candidate_id":"cand_acf054d8c135ca9e0851","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ea1a38f6938f6a6a3963","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Miserly withholding supplies the closed-hand counteraction and functions as attempted preservation by retention.","root":"ب خ ل","source_ref":"92:8","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000089","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_ce7c7fe0943cf7b23fd5"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000256/B001","candidate_links":[{"candidate_id":"cand_3f15dc539a13a94bd6aa","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2dbba4c333005d586504","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Disclosure and appearance supply the open pole and make release a movement into visibility.","root":"ج ل و","source_ref":"92:2","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000256","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a6dfe3d3a07f8aaa114e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000323/B002","candidate_links":[{"candidate_id":"cand_1460758e2c938f24657f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_51230b6dd95f31d1dc8c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Doing a beautiful or good act supplies the valued object and functions as the quality made operational.","root":"ح س ن","source_ref":"92:6","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000323","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7dfd247afe878c202c27"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000558/B003","candidate_links":[{"candidate_id":"cand_acf054d8c135ca9e0851","lane":"macro"},{"candidate_id":"cand_81ab5e5bb3ef8ad1f2ca","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ea1a38f6938f6a6a3963","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Falling into destruction supplies terminal exposure and functions as the event wealth fails to prevent.","root":"ر د ي","source_ref":"92:11","source_word_indices":["6"]},{"hft_ref":"hft_be4fa76e338c3605acaf","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Falling toward destruction supplies failed footing and functions as the embodied counter-outcome.","root":"ر د ي","source_ref":"92:11","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000558","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a16f26c6a1af947827bc","sup_ce7c7fe0943cf7b23fd5"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000709/B001","candidate_links":[{"candidate_id":"cand_3f15dc539a13a94bd6aa","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2dbba4c333005d586504","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Purposeful motion toward an object supplies directed agency and functions as the motion passing through the regulated boundary.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000709","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a6dfe3d3a07f8aaa114e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000775/B001","candidate_links":[{"candidate_id":"cand_3f15dc539a13a94bd6aa","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2dbba4c333005d586504","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Dispersion supplies divergent outcomes and functions as the reason boundary choices matter.","root":"ش ت ت","source_ref":"92:4","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000775","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a6dfe3d3a07f8aaa114e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000852/B004","candidate_links":[{"candidate_id":"cand_1460758e2c938f24657f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_51230b6dd95f31d1dc8c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Making a promise true in action supplies performative verification and functions as the bridge from belief to gift.","root":"ص د ق","source_ref":"92:6","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000852","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7dfd247afe878c202c27"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001012/B001","candidate_links":[{"candidate_id":"cand_acf054d8c135ca9e0851","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ea1a38f6938f6a6a3963","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Difficulty and severity supply the counter-path's resistance and function as the consequence toward which retention is eased.","root":"ع س ر","source_ref":"92:10","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001012","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_ce7c7fe0943cf7b23fd5"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001088/B001","candidate_links":[{"candidate_id":"cand_3f15dc539a13a94bd6aa","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2dbba4c333005d586504","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A covering that rises over and conceals supplies the closed pole and makes guarded enclosure spatially visible.","root":"غ ش و","source_ref":"92:1","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001088","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a6dfe3d3a07f8aaa114e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001110/B002","candidate_links":[{"candidate_id":"cand_acf054d8c135ca9e0851","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ea1a38f6938f6a6a3963","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Sufficiency supplies the claim of needing no support and functions as the false security premise.","root":"غ ن ي","source_ref":"92:8","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001110","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_ce7c7fe0943cf7b23fd5"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001457/B001","candidate_links":[{"candidate_id":"cand_acf054d8c135ca9e0851","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ea1a38f6938f6a6a3963","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Accumulated wealth supplies the retained reserve and functions as the tested but ineffective shield.","root":"م و ل","source_ref":"92:11","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001457","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_ce7c7fe0943cf7b23fd5"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001694/B001","candidate_links":[{"candidate_id":"cand_1460758e2c938f24657f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_51230b6dd95f31d1dc8c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Opening into ease after difficulty supplies reduced resistance and functions as path feedback after enacted commitment.","root":"ي س ر","source_ref":"92:7","source_word_indices":["1","2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001694","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7dfd247afe878c202c27"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001694/B005","candidate_links":[{"candidate_id":"cand_81ab5e5bb3ef8ad1f2ca","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_be4fa76e338c3605acaf","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Light compliant movement supplies low-friction advance and functions as the gait produced when reach and caution align.","root":"ي س ر","source_ref":"92:7","source_word_indices":["1","2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001694","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a16f26c6a1af947827bc"]}],"candidate_inventory":[{"anchor_refs":["92:10","92:3","92:5","92:7"],"branch_refs":["root_000434/B001","root_000434/B008","root_001028/B006","root_001694/B009"],"candidate_id":"cand_565e5686d7eb6b5dd777","commentary_obligation":"review","focus_branch_refs":["root_001028/B006"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000434/B001","root_000434/B008","root_001694/B009"],"root_ids":[],"scope":"pericope","source_local_id":"I:Cord Twisting, Flexion, and Tension","source_type":"channel","support_ids":["sup_1f3459fd521e6f01db6d","sup_543bca96c4a84ab2056c","sup_8b1f18d38f37cbafaf47","sup_8d939047125f4f44c72c","sup_bb94f114e44ba5035266"],"title":"Cord Twisting, Flexion, and Tension","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:1","92:2","92:4","92:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:5","branch_refs":["root_000256/B001","root_000709/B001","root_000775/B001","root_001028/B002","root_001088/B001","root_001677/B001"],"candidate_id":"cand_3f15dc539a13a94bd6aa","commentary_obligation":"review","hft_ref":"hft_2dbba4c333005d586504","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_selective_permeability","source_type":"hft","support_ids":["sup_a6dfe3d3a07f8aaa114e"],"title":"delta_selective_permeability","trust":"legacy_unbound"},{"anchor_refs":["92:5","92:6","92:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:5","branch_refs":["root_000323/B002","root_000852/B004","root_001028/B002","root_001677/B002","root_001694/B001"],"candidate_id":"cand_1460758e2c938f24657f","commentary_obligation":"review","hft_ref":"hft_51230b6dd95f31d1dc8c","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_good_made_operational","source_type":"hft","support_ids":["sup_7dfd247afe878c202c27"],"title":"delta_good_made_operational","trust":"legacy_unbound"},{"anchor_refs":["92:10","92:11","92:5","92:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:5","branch_refs":["root_000089/B001","root_000558/B003","root_001012/B001","root_001028/B002","root_001110/B002","root_001457/B001","root_001677/B001"],"candidate_id":"cand_acf054d8c135ca9e0851","commentary_obligation":"review","hft_ref":"hft_ea1a38f6938f6a6a3963","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_security_relocated","source_type":"hft","support_ids":["sup_ce7c7fe0943cf7b23fd5"],"title":"delta_security_relocated","trust":"legacy_unbound"},{"anchor_refs":["92:11","92:5","92:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:5","branch_refs":["root_000558/B003","root_001028/B001","root_001677/B003","root_001694/B005"],"candidate_id":"cand_81ab5e5bb3ef8ad1f2ca","commentary_obligation":"review","hft_ref":"hft_be4fa76e338c3605acaf","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_reach_with_guarded_footing","source_type":"hft","support_ids":["sup_a16f26c6a1af947827bc"],"title":"outlier_reach_with_guarded_footing","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_904ca00e09418df52f82","connection_ref":"conn_058c89eef632670b8478","note":"Immediate opposite pair: stinginess and self-sufficiency define the contrary course.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_0869dc49b7687fdf809c","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:8","source_note":"Direct opposite: giving and reverence frame the alternative to miserliness.","source_row_role":"ranked_review","source_target_component_ref":"92:5","source_target_components":["92:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:8","source_target_components":["92:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:8","target_evidence":{"arabic_uthmani":"وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ","ayah_ref":"92:8"},"target_ref":"92:8"},{"connection_evidence_ref":"conn_ev_6354f89776aeda38b11b","connection_ref":"conn_c14cc4abbd5bf5525920","note":"Immediate warning: wealth cannot rescue the contrary person at collapse.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_2e730a173ba94f223ef1","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"92:11","source_note":"Earlier local opposite path of giving and reverence.","source_row_role":"ranked_review","source_target_component_ref":"92:5","source_target_components":["92:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:11","source_target_components":["92:11"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:11","target_evidence":{"arabic_uthmani":"وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ","ayah_ref":"92:11"},"target_ref":"92:11"},{"connection_evidence_ref":"conn_ev_afd9a3a5c31d241f4d6c","connection_ref":"conn_7b8d685f953042ec95e0","note":"Immediate result: this course is eased toward ease.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_c17f3648081936fb2e79","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:7","source_note":"Giving and taqwa are the immediate antecedents to preparation for al-yusra.","source_row_role":"ranked_review","source_target_component_ref":"92:5","source_target_components":["92:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:7","source_target_components":["92:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:7","target_evidence":{"arabic_uthmani":"فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ","ayah_ref":"92:7"},"target_ref":"92:7"},{"connection_evidence_ref":"conn_ev_e07336f297e29c54a596","connection_ref":"conn_43b74abfbd6c5860f925","note":"Nearby structural oath material, without clarifying the paired actions.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_afaa0e63aab4f6fcef93","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"92:3","source_note":"The initial giving-and-piety pole begins the divergent conduct that follows the opening distinctions.","source_row_role":"ranked_review","source_target_component_ref":"92:5","source_target_components":["92:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:3","source_target_components":["92:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:3","target_evidence":{"arabic_uthmani":"وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ","ayah_ref":"92:3"},"target_ref":"92:3"},{"connection_evidence_ref":"conn_ev_2431745d535e21ecd806","connection_ref":"conn_208e4b586ff443d7e576","note":"Nearby oath material does not clarify giving or taqwa.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_a91728772cfa3d3bc823","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:2","source_note":"Begins the ethical pattern whose divergent paths follow the oath sequence.","source_row_role":"ranked_review","source_target_component_ref":"92:5","source_target_components":["92:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:2","source_target_components":["92:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:2","target_evidence":{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا تَجَلَّىٰ","ayah_ref":"92:2"},"target_ref":"92:2"},{"connection_evidence_ref":"conn_ev_8d94b5f71ad672d7b0ab","connection_ref":"conn_78f4a933f3177c2d9670","note":"Immediate continuation: affirming al-husna completes the described course.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_688212a9b6188b11c375","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:6","source_note":"Immediate antecedent: giving and taqwa frame the confirmation in 92:6.","source_row_role":"ranked_review","source_target_component_ref":"92:5","source_target_components":["92:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:6","source_target_components":["92:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:6","target_evidence":{"arabic_uthmani":"وَصَدَّقَ بِٱلْحُسْنَىٰ","ayah_ref":"92:6"},"target_ref":"92:6"},{"connection_evidence_ref":"conn_ev_c79d0ee8b4846f002765","connection_ref":"conn_cfa994134adbdbda507b","note":"Immediate thesis: human endeavors are diverse, introducing the two courses.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_2d69d6fbc12fa3d2de4b","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:4","source_note":"Giving and taqwa state the actions that begin the positive branch.","source_row_role":"ranked_review","source_target_component_ref":"92:5","source_target_components":["92:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:4","source_target_components":["92:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:4","target_evidence":{"arabic_uthmani":"إِنَّ سَعْيَكُمْ لَشَتَّىٰ","ayah_ref":"92:4"},"target_ref":"92:4"},{"connection_evidence_ref":"conn_ev_fa04c61597e7ad3b0e3f","connection_ref":"conn_0fd9e4f93925923e1405","note":"Immediate opposite outcome: the contrary course is eased toward hardship.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_3f624552770e02f1b22b","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:10","source_note":"Immediate opposing action profile establishes the other branch of the surah's sequence.","source_row_role":"ranked_review","source_target_component_ref":"92:5","source_target_components":["92:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:10","source_target_components":["92:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:10","target_evidence":{"arabic_uthmani":"فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ","ayah_ref":"92:10"},"target_ref":"92:10"},{"connection_ref":"conn_f36caf81648c105ed8bf","note":null,"origin":"derived_reciprocal_seed","prior_label":null,"qualification":{"boundary":"At least one source-direction review meaningfully linked this target back to the focus ayah. Treat its note and label only as a discovery nomination. Reassess the relation from the focus ayah using the supplied exact target Arabic; do not invent missing target morphology or inherit the source label.","derived_reciprocal_counterevidence":false,"derived_reciprocal_seed":true,"has_missing_ayah_suggestion_source_row":true,"has_ranked_review_source_row":false,"has_reciprocal_counterevidence":false,"has_reciprocal_nomination":true,"receiving_direction_requires_fresh_assessment":true,"source_direction_labels_are_not_focus_decisions":true,"source_row_roles_are_provenance_not_decisions":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_1ced7450e36fab58afa5","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:9","source_note":"Immediate positive profile: giving and mindfulness prepare the affirmation in 92:6.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"92:5","source_target_components":["92:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:5"}],"relation_scope":"declared_pericope_reciprocal_evidence","target_evidence":{"arabic_uthmani":"وَكَذَّبَ بِٱلْحُسْنَىٰ","ayah_ref":"92:9"},"target_ref":"92:9"}],"focus":{"arabic_uthmani":"فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"92:5:1:1","qac_word_ref":"92:5:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أَمَّا","morph_features":"STEM|POS:EXL|LEM:>am~aA","morpheme_role":"STEM","pos":"EXL","qac_ref":"92:5:1:2","qac_word_ref":"92:5:1","root_ar":"","surface_ar":"أَمَّا"},{"lemma_ar":"مَن","morph_features":"STEM|POS:COND|LEM:man","morpheme_role":"STEM","pos":"COND","qac_ref":"92:5:2:1","qac_word_ref":"92:5:2","root_ar":"","surface_ar":"مَنْ"},{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:3:1","qac_word_ref":"92:5:3","root_ar":"ع ط و","surface_ar":"أَعْطَىٰ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:5:4:1","qac_word_ref":"92:5:4","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"ٱتَّقَىٰ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{t~aqaY`|ROOT:wqy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:4:2","qac_word_ref":"92:5:4","root_ar":"و ق ي","surface_ar":"ٱتَّقَىٰ"}],"word_analysis_qac_refs":[["92:5:1:1"],["92:5:1:2"],["92:5:2:1"],["92:5:3:1"],["92:5:4:1"],["92:5:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["92:5:1","92:5:2","92:5:3","92:5:4","92:5:5","92:5:6"]},"focus_surface_evidence":{"arabic_uthmani":"فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"92:5:1:1","qac_word_ref":"92:5:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أَمَّا","morph_features":"STEM|POS:EXL|LEM:>am~aA","morpheme_role":"STEM","pos":"EXL","qac_ref":"92:5:1:2","qac_word_ref":"92:5:1","root_ar":"","surface_ar":"أَمَّا"},{"lemma_ar":"مَن","morph_features":"STEM|POS:COND|LEM:man","morpheme_role":"STEM","pos":"COND","qac_ref":"92:5:2:1","qac_word_ref":"92:5:2","root_ar":"","surface_ar":"مَنْ"},{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:3:1","qac_word_ref":"92:5:3","root_ar":"ع ط و","surface_ar":"أَعْطَىٰ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:5:4:1","qac_word_ref":"92:5:4","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"ٱتَّقَىٰ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{t~aqaY`|ROOT:wqy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:5:4:2","qac_word_ref":"92:5:4","root_ar":"و ق ي","surface_ar":"ٱتَّقَىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["92:5:1:1"],["92:5:1:2"],["92:5:2:1"],["92:5:3:1"],["92:5:4:1"],["92:5:4:2"]],"word_analysis_refs":["92:5:1","92:5:2","92:5:3","92:5:4","92:5:5","92:5:6"],"word_rows":[{"analysis_record_ref":"92:5:1","analytic_gloss_range_en":"resumptive and consequential hinge that turns the prior thesis into detailed case division","analytic_root_gloss_range_en":null,"qac_refs":["92:5:1:1"],"root":{},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"92:5:2","analytic_gloss_range_en":"conditional-detailing topic particle that foregrounds the human case and suspends the answer until the later branch response","analytic_root_gloss_range_en":null,"qac_refs":["92:5:1:2"],"root":{},"surface":{"arabic":"أَمَّا","transliteration":"ammā"}},{"analysis_record_ref":"92:5:3","analytic_gloss_range_en":"generic conditional-relative human subject, grammatically singular while semantically open to whoever meets the predicates","analytic_root_gloss_range_en":null,"qac_refs":["92:5:2:1"],"root":{},"surface":{"arabic":"مَنْ","transliteration":"man"}},{"analysis_record_ref":"92:5:4","analytic_gloss_range_en":"completed giving as open-ended outward transfer; object and recipient are unstated, while the local branch keeps yielding pressure as relinquishment rather than selecting unrelated root branches","analytic_root_gloss_range_en":"root range includes giving, handing over, reaching, serving, asking for a gift, yielding, and overreaching; this local Form IV perfect selects caused outward transfer with a restrained yielding/relinquishing pressure","qac_refs":["92:5:3:1"],"root":{"arabic":"ع ط و","transliteration":"ʿ-ṭ-w"},"surface":{"arabic":"أَعْطَىٰ","transliteration":"aʿṭā"}},{"analysis_record_ref":"92:5:5","analytic_gloss_range_en":"coordinating hinge that binds the second perfect predicate to the same subject inside the suspended protasis","analytic_root_gloss_range_en":null,"qac_refs":["92:5:4:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"92:5:6","analytic_gloss_range_en":"completed self-guarding or God-conscious protective stance, object left open and coordinated with giving as the second predicate","analytic_root_gloss_range_en":"root range includes protecting with a barrier, self-guarding in fear or reverence, and unrelated branches such as guarded gait, a measure term, or a bird name; this local Form VIII perfect selects self-directed protective caution","qac_refs":["92:5:4:2"],"root":{"arabic":"و ق ي","transliteration":"w-q-y"},"surface":{"arabic":"ٱتَّقَىٰ","transliteration":"ittaqā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":9,"missing_anchor_refs":[],"supplied_unique_anchor_count":9},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["92:1","92:2","92:4","92:5"],"branch_refs":["root_000256/B001","root_000709/B001","root_000775/B001","root_001028/B002","root_001088/B001","root_001677/B001"],"candidate_id":"cand_3f15dc539a13a94bd6aa","evidence_scope":"declared_pericope","hft_ref":"hft_2dbba4c333005d586504","item_id":"delta_selective_permeability","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_selective_permeability","support_id":"sup_a6dfe3d3a07f8aaa114e"},{"anchor_refs":["92:5","92:6","92:7"],"branch_refs":["root_000323/B002","root_000852/B004","root_001028/B002","root_001677/B002","root_001694/B001"],"candidate_id":"cand_1460758e2c938f24657f","evidence_scope":"declared_pericope","hft_ref":"hft_51230b6dd95f31d1dc8c","item_id":"delta_good_made_operational","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_good_made_operational","support_id":"sup_7dfd247afe878c202c27"},{"anchor_refs":["92:10","92:11","92:5","92:8"],"branch_refs":["root_000089/B001","root_000558/B003","root_001012/B001","root_001028/B002","root_001110/B002","root_001457/B001","root_001677/B001"],"candidate_id":"cand_acf054d8c135ca9e0851","evidence_scope":"declared_pericope","hft_ref":"hft_ea1a38f6938f6a6a3963","item_id":"delta_security_relocated","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_security_relocated","support_id":"sup_ce7c7fe0943cf7b23fd5"},{"anchor_refs":["92:11","92:5","92:7"],"branch_refs":["root_000558/B003","root_001028/B001","root_001677/B003","root_001694/B005"],"candidate_id":"cand_81ab5e5bb3ef8ad1f2ca","evidence_scope":"declared_pericope","hft_ref":"hft_be4fa76e338c3605acaf","item_id":"outlier_reach_with_guarded_footing","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_reach_with_guarded_footing","support_id":"sup_a16f26c6a1af947827bc"}],"diagnostics":[],"lane_counts":{"global":13,"macro":4,"micro":3},"packet_summary":{"ayah_count":21,"focus_ref":"92:5","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ج ز ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000244","furuq_root_norm":"ج ز ي","furuq_source_root_norm":"ج ز ي","is_dominant":true,"target_occurrences":97,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000242","furuq_root_norm":"ج ز ز","furuq_source_root_norm":"ج ز ز","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11","92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"92:5","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"92:5","lane":"macro","linguistic_source_ref":"92:5","surface_ref":"92:5","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"92:5","target_tokens":[["Kim",["92:5:1","92:5:2"]],["verir",["92:5:3"]],["ve",["92:5:4"]],["sakınırsa",["92:5:2","92:5:4"]]],"text":"Kim verir ve sakınırsa,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":11,"id":"s092-p01-001-011","label":"Contrasting forms of striving","number":1,"refs":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"92:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"92:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["92:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"92:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"I:Cord Twisting, Flexion, and Tension","source_type":"channel","support_id":"sup_1f3459fd521e6f01db6d","text":"Raw or prepared materials are shaped, layered, contained, marked, or hardened so that they can bear, cover, divide, grind, preserve, or adorn.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"I:Cord Twisting, Flexion, and Tension","source_type":"channel","support_id":"sup_543bca96c4a84ab2056c","text":"92:7 and 92:10 (`ي س ر`: `نيسره`); 92:3 (`خ ل ق`: `خلق`); 92:5 (`ع ط و`: `أعطى`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"I:Cord Twisting, Flexion, and Tension","source_type":"channel","support_id":"sup_8b1f18d38f37cbafaf47","text":"Fibers are turned downward into a cord, then tension and controlled yielding make the line or bow usable.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"I:Cord Twisting, Flexion, and Tension","source_type":"channel","support_id":"sup_8d939047125f4f44c72c","text":"Twist binds separate fibers, smoothing gives the cord a continuous surface, and controlled flexion stores force without structural failure.","trust":"trusted"},{"branch_refs":["root_000434/B001","root_000434/B008","root_001028/B006","root_001694/B009"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"I:Cord Twisting, Flexion, and Tension","source_type":"channel","support_id":"sup_bb94f114e44ba5035266","text":"downward twisting of fibers `ي س ر:B009/m01`; smooth finished cord `خ ل ق:B008/m03`; pliant bow under force `ع ط و:B006/m04`; measured shaping before use `خ ل ق:B001/m06`","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَغْشَىٰ","ayah_ref":"92:1"},{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا تَجَلَّىٰ","ayah_ref":"92:2"},{"arabic_uthmani":"إِنَّ سَعْيَكُمْ لَشَتَّىٰ","ayah_ref":"92:4"},{"arabic_uthmani":"فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ","ayah_ref":"92:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000256/B001","root_000709/B001","root_000775/B001","root_001028/B002","root_001088/B001","root_001677/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001028","role":"Handover supplies an outward crossing and functions as deliberate opening.","root":"ع ط و","source_ref":"92:5","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001677","role":"A harm-blocking barrier supplies closure and functions as selective boundary control.","root":"و ق ي","source_ref":"92:5","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001088","role":"A covering that rises over and conceals supplies the closed pole and makes guarded enclosure spatially visible.","root":"غ ش و","source_ref":"92:1","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000256","role":"Disclosure and appearance supply the open pole and make release a movement into visibility.","root":"ج ل و","source_ref":"92:2","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000709","role":"Purposeful motion toward an object supplies directed agency and functions as the motion passing through the regulated boundary.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000775","role":"Dispersion supplies divergent outcomes and functions as the reason boundary choices matter.","root":"ش ت ت","source_ref":"92:4","source_word_indices":["3"]}],"changed_reading":{"after":"Giving and guarding are coordinated boundary operations: release what should pass outward while shielding the self from harmful capture.","before":"Giving and guarding are two separate virtues."},"confidence":"medium","mechanism":"The covering/revealing alternation and the later divergence of purposeful movement recast the two focus verbs as regulation of a boundary. Giving opens a passage outward; guarding controls what may cross or harm the self. The agent is selectively permeable, not simply open or closed.","model_id":"delta_selective_permeability","reader_inference":"The packet supplies covering, disclosure, directed striving, divergence, handover, and protection; I infer a single selective-permeability mechanism linking them. A live alternative is that the opening oaths frame contrast without assigning boundary mechanics to 92:5.","status":"revised","structural_cues":["92:1-2 alternate covering and disclosure; 92:4 then declares the strivings divergent before 92:5 selects one response."],"trigger_roots":["غ ش و","ج ل و","س ع ي","ش ت ت"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_selective_permeability","source_type":"hft","support_id":"sup_a6dfe3d3a07f8aaa114e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ","ayah_ref":"92:5"},{"arabic_uthmani":"وَصَدَّقَ بِٱلْحُسْنَىٰ","ayah_ref":"92:6"},{"arabic_uthmani":"فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ","ayah_ref":"92:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000323/B002","root_000852/B004","root_001028/B002","root_001677/B002","root_001694/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001028","role":"Concrete handover supplies the deed and functions as material verification.","root":"ع ط و","source_ref":"92:5","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001677","role":"Protective moral caution supplies maintained orientation and functions as stabilization of the deed.","root":"و ق ي","source_ref":"92:5","source_word_indices":["4"]},{"branch_id":"B004","mapped_root_id":"root_000852","role":"Making a promise true in action supplies performative verification and functions as the bridge from belief to gift.","root":"ص د ق","source_ref":"92:6","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000323","role":"Doing a beautiful or good act supplies the valued object and functions as the quality made operational.","root":"ح س ن","source_ref":"92:6","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001694","role":"Opening into ease after difficulty supplies reduced resistance and functions as path feedback after enacted commitment.","root":"ي س ر","source_ref":"92:7","source_word_indices":["1","2"]}],"changed_reading":{"after":"The gift materially verifies the good, while guarded enactment begins to make that direction easier to inhabit.","before":"The gift expresses an already settled inner goodness."},"confidence":"strong","mechanism":"The next sequence makes the gift an enactment that verifies the good rather than a detachable token. Guarding stabilizes that enacted commitment, and repeated easing describes feedback in which a chosen act becomes an increasingly traversable path.","model_id":"delta_good_made_operational","reader_inference":"The packet supplies deed, verification, goodness, and subsequent easing; I infer that enacted commitment helps form the path it enters. Alternatively, the sequence may list independent traits followed by reward without path feedback.","status":"strengthened","structural_cues":["92:5-7 is an uninterrupted sequence: give and guard, verify the good, then be eased toward ease."],"trigger_roots":["ص د ق","ح س ن","ي س ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_good_made_operational","source_type":"hft","support_id":"sup_7dfd247afe878c202c27","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ","ayah_ref":"92:10"},{"arabic_uthmani":"وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ","ayah_ref":"92:11"},{"arabic_uthmani":"فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ","ayah_ref":"92:5"},{"arabic_uthmani":"وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ","ayah_ref":"92:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000089/B001","root_000558/B003","root_001012/B001","root_001028/B002","root_001110/B002","root_001457/B001","root_001677/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001028","role":"Handover supplies release of possession and functions as withdrawal of trust from the stockpile.","root":"ع ط و","source_ref":"92:5","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001677","role":"Warding harm with a barrier supplies real protection and functions as the alternative location of security.","root":"و ق ي","source_ref":"92:5","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000089","role":"Miserly withholding supplies the closed-hand counteraction and functions as attempted preservation by retention.","root":"ب خ ل","source_ref":"92:8","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001110","role":"Sufficiency supplies the claim of needing no support and functions as the false security premise.","root":"غ ن ي","source_ref":"92:8","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001012","role":"Difficulty and severity supply the counter-path's resistance and function as the consequence toward which retention is eased.","root":"ع س ر","source_ref":"92:10","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Accumulated wealth supplies the retained reserve and functions as the tested but ineffective shield.","root":"م و ل","source_ref":"92:11","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_000558","role":"Falling into destruction supplies terminal exposure and functions as the event wealth fails to prevent.","root":"ر د ي","source_ref":"92:11","source_word_indices":["6"]}],"changed_reading":{"after":"Giving releases the reserve that only impersonates safety; guarded orientation, not retained wealth, becomes the operative protection.","before":"Giving reduces one's reserve, while guarding supplies a separate moral safeguard."},"confidence":"strong","mechanism":"The mirrored counter-sequence exposes retention as failed protection: withholding allies with claimed self-sufficiency, opens toward hardship, and accumulated wealth cannot avail at the fall. Against that chain, giving relocates security from the held asset to the guarded orientation of the agent.","model_id":"delta_security_relocated","reader_inference":"The packet supplies a formal contrast and the failure of wealth at the fall; I infer a relocation of security from possession to protected orientation. A live alternative is that giving and guarding are merit conditions while wealth's failure is a separate eschatological observation.","status":"strengthened","structural_cues":["The two أَمَّا clauses mirror giving against withholding and repeat the easing formula, while 92:11 tests wealth precisely at the moment of falling."],"trigger_roots":["ب خ ل","غ ن ي","ع س ر","م و ل","ر د ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_security_relocated","source_type":"hft","support_id":"sup_ce7c7fe0943cf7b23fd5","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ","ayah_ref":"92:11"},{"arabic_uthmani":"فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ","ayah_ref":"92:5"},{"arabic_uthmani":"فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ","ayah_ref":"92:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000558/B003","root_001028/B001","root_001677/B003","root_001694/B005"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001028","role":"Taking or reaching by hand supplies forward extension and functions as the body's initiative.","root":"ع ط و","source_ref":"92:5","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001677","role":"A guarded gait that spares a hurting hoof supplies cautious contact and functions as risk-sensitive footing.","root":"و ق ي","source_ref":"92:5","source_word_indices":["4"]},{"branch_id":"B005","mapped_root_id":"root_001694","role":"Light compliant movement supplies low-friction advance and functions as the gait produced when reach and caution align.","root":"ي س ر","source_ref":"92:7","source_word_indices":["1","2"]},{"branch_id":"B003","mapped_root_id":"root_000558","role":"Falling toward destruction supplies failed footing and functions as the embodied counter-outcome.","root":"ر د ي","source_ref":"92:11","source_word_indices":["6"]}],"changed_reading":{"after":"As a contained body-image, it depicts extending forward while testing one's footing: restraint is what lets initiative move without becoming a fall.","before":"The verse states an abstract pair of generosity and moral caution."},"confidence":"exploratory","containment":"This embodied reading is surprising because it activates reaching-by-hand and guarded-animal-gait branches rather than the ordinary senses of the two focus forms. It remains anchored in both focus roots and gains a coherent motion contrast from later ease and falling. Downstream prose should label it an image-schema for ethical action, never a replacement translation.","focus_anchor":"The paired focus roots can jointly stage an extending hand and a foot that tests harmful ground.","outlier_id":"outlier_reach_with_guarded_footing"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_reach_with_guarded_footing","source_type":"hft","support_id":"sup_a16f26c6a1af947827bc","trust":"legacy_unbound"}]}
</lane_packet_json>
