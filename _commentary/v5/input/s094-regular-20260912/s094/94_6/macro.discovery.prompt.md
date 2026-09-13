# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **94:6**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s094-regular-20260912/s094/94_6/macro.discovery.json` and modify nothing
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
  "ayah_ref": "94:6",
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
{"branch_registry":[{"boundary":"Bu genel anlam, para darlığına, sol yana veya hayvanlara özgü kullanımlarla sınırlandırılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001012/B001","candidate_links":[{"candidate_id":"cand_41d8b7037f657ffdd2c4","lane":"macro"},{"candidate_id":"cand_732520c40bb078782bbb","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","surface_ar":"عُسْرِ"}],"gloss":"güçlük ve çetinlik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kolaylığın karşıtı olan genel güçlük ve çetinlik durumudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işin veya günün zor ve ağır geçmesi bu genel niteliğin özel bir gerçekleşmesidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kolayca gerçekleşmeyen işler topluca bu güçlük alanında adlandırılabilir."}}],"root_ar":"ع س ر","root_id":"root_001012","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel olarak kolay olmayan iş, durum veya zamanın temel niteliğini karşılar.","boundary_detail":"Bu genel anlam, para darlığına, sol yana veya hayvanlara özgü kullanımlarla sınırlandırılmaz.","branch_image_ar":"الصعوبة والشدة","concept_gloss":"güçlük ve çetinlik","contextual_glosses":[{"applicability":"Bir işin, durumun veya günün kolay olmadığını niteleyen akıcı çevirilerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlam içinde güçlük ve çetinlik niteliğini doğal biçimde korur."},"facet_ids":["F001","F002"],"text":"zor","usage_role":"contextual"}],"definition":"Bir işin, durumun ya da zamanın kolay olmaması; kişiyi zorlayan, aşılması veya gerçekleşmesi güç bir nitelik taşımasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kolaylığın karşıtı olan genel güçlük ve çetinlik durumudur."},{"facet_id":"F002","role":"specialization","statement":"Bir işin veya günün zor ve ağır geçmesi bu genel niteliğin özel bir gerçekleşmesidir."},{"facet_id":"F003","role":"extension","statement":"Kolayca gerçekleşmeyen işler topluca bu güçlük alanında adlandırılabilir."}],"identity_rationale":"Kaynak ifadesi bu dalı kolaylığın karşıtı olan genel güçlük ve çetinlik olarak kurar; zor iş, çetin gün ve gerçekleşmesi güç işler bunun doğal görünümleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"güçlük, çetinlik; kolaylığın karşıtı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"zorlaşmak, çetin hale gelmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"zor, çetin"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"zor ve çetin gün"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kolaylaşmayan zor işler"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"zor olan veya kolay olanın karşıtı"}],"lexicalization_note":"Tanım genel güçlük anlamını temel alır; çetin gün gibi kalıba bağlı kullanımları bu çekirdeğin özel görünümleri olarak ayrı tutar.","neighbor_coverage_note":"Verilen bütün komşular incelendi; yalnızca genel güçlüğün ağır etki ve para darlığından ayrımını keskinleştiren iki karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel ve tarafsız güçlük niteliğidir; komşu dal ise güçlüğün kişi üzerindeki ağır etkisini belirginleştirir.","focus_only":"Bu dal, belirli bir duygusal etki gerektirmeden her türlü genel güçlüğü kapsar.","gloss":"ağır gelen zorluk","neighbor_only":"Komşu dal, özellikle insanın üzerinde ağır ve büyük bir etki bırakan olayları öne çıkarır.","neighbor_ref":"root_001008/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin zor, ağır veya katlanılması güç oluşunu bildirir."},{"boundary_match":"partial","distinction":"Bu dal her tür güçlüğü kapsarken komşu dal yalnızca maddi yetersizlik alanında özelleşmiştir.","focus_only":"Para veya geçim şartı aramayan genel zorluk anlamını taşır.","gloss":"para darlığı","neighbor_only":"Özellikle para bulunmaması ve geçim darlığı durumunu bildirir.","neighbor_ref":"root_001012/B002","relation_type":"near_neighbor","shared_zone":"Para darlığı da kişiyi zorlayan bir durum olduğundan genel güçlük alanıyla ilişkilidir."}],"source_phrase_ar":"أصل صحيح واحد يدل على صعوبة وشدة (maqayis); العسر نقيض اليسر (maqayis;ayn;sihah;tahdhib;mufradat); أمر عسير ويوم عسير (maqayis;ayn;sihah;tahdhib;mufradat); العسرى الأمور التي تعسر ولا تتيسر (tahdhib)","source_summary":"Kaynaklar anlamı ortak biçimde kolaylığın karşıtı olan güçlükte birleştirir ve bunu zor işlerle çetin günlere uygular.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العسر نقيض اليسر والأمر العسير واليوم العسير والعسرى من الأمور الصعبة","what_is_not_ar":"لا يختص بقلة المال ولا باليد الشمال ولا بأحوال النوق الخاصة"},"support_links":["sup_5e5357ab92cddc5e2bf8","sup_662e2b62efd288c9e8cd"]},{"boundary":"Genel bir iş güçlüğü, maddi yetersizlik bulunmadıkça bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001012/B002","candidate_links":[{"candidate_id":"cand_3ad3cf6ee2a8ca8e0907","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","surface_ar":"عُسْرِ"}],"gloss":"para darlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Elde yeterli para bulunmamasından doğan maddi darlık halidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Varlıklı durumdan para darlığına geçişi ve bu durumda bulunan kişiyi de kapsar."}}],"root_ar":"ع س ر","root_id":"root_001012","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin yeterli paraya erişemediği maddi yetersizlik durumunun genel karşılığıdır.","boundary_detail":"Genel bir iş güçlüğü, maddi yetersizlik bulunmadıkça bu dala girmez.","branch_image_ar":"ضيق ذات اليد","concept_gloss":"para darlığı","contextual_glosses":[{"applicability":"Kişinin para darlığına düşmesini veya bu durumda bulunmasını anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin maddi imkan yoksunluğunu ve içinde bulunduğu hali korur."},"facet_ids":["F001","F002"],"text":"maddi sıkıntı içinde olmak","usage_role":"contextual"}],"definition":"Bir kişinin para bulmakta zorlanacak ölçüde maddi imkandan yoksun olması veya önceki varlıklı durumundan böyle bir darlığa düşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Elde yeterli para bulunmamasından doğan maddi darlık halidir."},{"facet_id":"F002","role":"extension","statement":"Varlıklı durumdan para darlığına geçişi ve bu durumda bulunan kişiyi de kapsar."}],"identity_rationale":"Kaynak ifadesi dalı açıkça para azlığı, elde para bulunmaması ve varlıktan darlığa düşme haliyle sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"para darlığı, maddi sıkıntı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"maddi darlık, parasızlık"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"maddi sıkıntı içinde olan kimse"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"varlıktan maddi darlığa düşmek"}],"lexicalization_note":"Tanım para darlığı çekirdeğini korur; kişiyi bu duruma giren veya bu durumda bulunan diye niteleyen biçimleri ayrı gerçekleşmeler sayar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yoksulluk alanı ile sınırsız güçlük anlamı, bu dalın maddi sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal para darlığı ve bu duruma düşüş üzerinde durur; komşu dal daha geniş bir ihtiyaç ve yoksulluk alanına sahiptir.","focus_only":"Para bulmanın güçleşmesini ve varlıktan darlığa geçişi özellikle içerir.","gloss":"yoksulluk ve ihtiyaç","neighbor_only":"Genel ihtiyaç ve yoksulluk durumunu, yalnız para bulma güçlüğüne bağlanmadan kapsar.","neighbor_ref":"root_001169/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin mal ve para bakımından yetersiz durumda olmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal maddi yetersizliktir; komşu dal ise sebebi ve alanı sınırlanmamış genel zorluktur.","focus_only":"Yalnızca maddi imkanın ve paranın yetersiz olduğu durumu bildirir.","gloss":"genel güçlük","neighbor_only":"Para şartı olmadan herhangi bir işin veya durumun güçlüğünü bildirir.","neighbor_ref":"root_001012/B001","relation_type":"near_neighbor","shared_zone":"Maddi darlık, kişinin karşılaştığı güçlüklerden biridir."}],"source_phrase_ar":"الإقلال أيضا عسرة (maqayis); العسر قلة ذات اليد (ayn); العسرة قلة ذات اليد وكذلك الإعسار (tahdhib); العسرة تعسر وجود المال (mufradat); أعسر الرجل إذا صار من ميسرة إلى عسرة (maqayis)","source_summary":"Kaynaklar para azlığı ile elde para bulunmamasını ortak çekirdek sayar; ayrıca varlıktan darlığa düşen kişiyi bu alan içinde gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العسرة وقلة ذات اليد والإعسار والمعسر ومن صار من ميسرة إلى عسرة","what_is_not_ar":"لا يدخل فيه مجرد صعوبة الأمر إذا لم يكن ضيق مال"},"support_links":["sup_1873718b8c21ce9368fe"]},{"boundary":"Borçlunun yoksulluğu tek başına yetmez; darlık sırasında ısrarlı ve katı bir isteme bulunmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001012/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","surface_ar":"عُسْرِ"}],"gloss":"darlıktaki borçluyu sıkıştırmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Alacaklının maddi darlık içindeki borçludan borcunu istemesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İstemenin ayırt edici yönü, borçluya süre tanımamak ve yumuşak davranmamaktır."}}],"root_ar":"ع س ر","root_id":"root_001012","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Borçlunun ödeme güçlüğüne rağmen alacağın katı biçimde istendiği durumu karşılar.","boundary_detail":"Borçlunun yoksulluğu tek başına yetmez; darlık sırasında ısrarlı ve katı bir isteme bulunmalıdır.","branch_image_ar":"مطالبة المعسر","concept_gloss":"darlıktaki borçluyu sıkıştırmak","contextual_glosses":[{"applicability":"Darlıktaki bir borçludan ödeme istenirken yumuşak davranılmadığını anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Borç isteme eylemini ve borçlu üzerindeki katı baskıyı korur."},"facet_ids":["F001","F002"],"text":"borcunu ödesin diye sıkıştırdı","usage_role":"contextual"}],"definition":"Maddi darlık içindeki borçludan alacağı, ona rahatlama süresi tanımadan ve yumuşak davranmadan istemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Alacaklının maddi darlık içindeki borçludan borcunu istemesidir."},{"facet_id":"F002","role":"specialization","statement":"İstemenin ayırt edici yönü, borçluya süre tanımamak ve yumuşak davranmamaktır."}],"identity_rationale":"Kaynak ifadesi yalnız alacak istemeyi değil, borçlunun darlığını bilerek ona süre tanımadan ve yumuşak davranmadan istemeyi kurucu şart olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"darlıktaki borçludan borcu katılıkla istemek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"darlık zamanında benden bir şey istemek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"alacak istemede ve işte katı davrananlar"}],"lexicalization_note":"Tanım alacaklı, borçlu ve darlık şartını birlikte korur; kişi ve eylem bildiren bağlı biçimleri genel çekirdekle karıştırmaz.","neighbor_coverage_note":"Bütün komşular karşılaştırıldı; borcu yumuşaklıkla alma karşıtlığı ile genel hak isteme yakınlığı, dalın özel şartlarını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Aynı borç isteme ekseninde odak dal katı ve hoşgörüsüz, komşu dal ise yumuşak davranışı kurucu özellik yapar.","focus_only":"Borçlunun darlığına rağmen onu sıkıştıran ve süre tanımayan katı isteme biçimidir.","gloss":"borcu yumuşaklıkla almak","neighbor_only":"Borcu borçludan yumuşak ve ölçülü davranarak alma biçimidir.","neighbor_ref":"root_000491/B004","relation_type":"polarity_pair","shared_zone":"Her iki dalda da alacaklının borçludan borcunu elde etmeye çalışması vardır."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı sınırı darlıktaki borçluya karşı katılıktır; komşu dal daha genel ve süreklilik odaklı bir hak istemedir.","focus_only":"Borçlunun maddi darlığı ve ona yumuşak davranmama şartlarını birlikte taşır.","gloss":"hakkını ısrarla istemek","neighbor_only":"Bir hakkı veya alacağı sürekli istemeyi, borçlunun darlığına bağlı olmadan kapsar.","neighbor_ref":"root_000943/B002","relation_type":"near_synonym","shared_zone":"İki dalda da bir hak veya alacak sahibinin karşı taraftan ödeme istemesi vardır."}],"source_phrase_ar":"عسرته أنا أعسره إذا طالبته بدينك وهو معسر ولم تنظره إلى ميسرته (maqayis); عسرت الغريم أعسره إذا طلبت منه الدين على عسرته (sihah); عسرت الغريم أعسره عسرا إذا أخذته على عسرة ولم ترفق به (tahdhib); عسرني الرجل طالبني بشيء حين العسرة (mufradat)","source_summary":"Kaynaklar darlık sırasında talepte bulunma alanında birleşir; borç isteme çoğu aktarımın özel çerçevesidir, süre tanımama ve yumuşak davranmama ise bunları açıkça bildiren aktarımlara özgü ayrıntılardır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه عسر الغريم وطلب الدين أو الشيء عند العسرة والأخذ على عسرة بلا رفق","what_is_not_ar":"لا يدخل فيه نفس الفقر بلا مطالبة ولا مجرد الخصومة العامة"},"support_links":[]},{"boundary":"Bu dal, yalnız nesnel zorluğu değil, karşı çıkma veya işi güçleştirme yönünü de içerir.","branch_kind":"mixed_non_bare","branch_ref":"root_001012/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","surface_ar":"عُسْرِ"}],"gloss":"karşı çıkıp işi güçleştirmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Karşı çıkma, düz ilerlemeyi bozma ve işi dolambaçlı hale getirme çekirdeğidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işi başkasına güçleştirmek veya tarafların karşılıklı güçlük çıkarması bu çekirdeğin eylem görünümüdür."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişiden onun elde edilmesi güç olan şeyini istemek de bu alana bağlı özel bir kullanımdır."}}],"root_ar":"ع س ر","root_id":"root_001012","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşı çıkmanın veya dolambaçlı davranmanın bir işi zorlaştırdığı genel durumlarda kullanılır.","boundary_detail":"Bu dal, yalnız nesnel zorluğu değil, karşı çıkma veya işi güçleştirme yönünü de içerir.","branch_image_ar":"الخلاف والالتواء والتعسير","concept_gloss":"karşı çıkıp işi güçleştirmek","contextual_glosses":[{"applicability":"Bir kişinin karşı çıkarak veya uzatarak işi başkası için güçleştirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşin kendiliğinden dolambaçlı hale gelmesini ve güç elde edileni isteme kullanımını kapsamaz.","preserves":"İşi bilerek güçleştirme ve düz ilerleyişi engelleme yönünü korur."},"facet_ids":["F001","F002"],"text":"işi yokuşa sürmek","usage_role":"contextual"}],"definition":"Bir işin dolambaçlı ve güç hale gelmesi ya da bir kişinin karşı çıkarak işi başkası için zorlaştırmasıdır; karşılıklı kullanımda tarafların işi kolaylaştırmak yerine güçleştirmesini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Karşı çıkma, düz ilerlemeyi bozma ve işi dolambaçlı hale getirme çekirdeğidir."},{"facet_id":"F002","role":"extension","statement":"Bir işi başkasına güçleştirmek veya tarafların karşılıklı güçlük çıkarması bu çekirdeğin eylem görünümüdür."},{"facet_id":"F003","role":"associated_use","statement":"Bir kişiden onun elde edilmesi güç olan şeyini istemek de bu alana bağlı özel bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi karşı çıkma ve dolambaçlı hale gelme çekirdeğini, işi güçleştirme, karşılıklı güçlük çıkarma ve elde edilmesi güç olanı isteme eylemleriyle açıkça birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"karşı çıkma ve dolambaçlılık"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"iş ona dolambaçlı ve güç gelmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ona karşı çıkmak veya işi ona güçleştirmek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"iş dolambaçlı ve güç hale gelmek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"birbirlerine işi güçleştirmek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"birinden elde edilmesi güç olan şeyi istemek"}],"lexicalization_note":"Tanım karşı çıkma ve dolambaçlılık çekirdeğini korur; işi güçleştiren bağlı eylemleri bunun özel gerçekleşmeleri olarak gösterir.","neighbor_coverage_note":"Tüm adaylar incelendi; dolambaçlı güçlük ve karşılıklı engelleşme karşılaştırmaları dalın karşı çıkma ile zorlaştırmayı birleştiren sınırını belirginleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dolambaçlılığı etkin karşı çıkma ve zorlaştırmaya genişletir; komşu dal niteliğin kendisinde daha dardır.","focus_only":"Karşı çıkma, işi başkasına güçleştirme ve karşılıklı güçlük çıkarma eylemlerini de kapsar.","gloss":"dolambaçlılık ve güçlük","neighbor_only":"Dolambaçlılık ve güçlük niteliğini belirli bir adlandırma içinde verir, üretken eylem alanını taşımaz.","neighbor_ref":"root_000993/B012","relation_type":"near_synonym","shared_zone":"Her iki dalda da düz ilerlemeyi bozan dolambaçlılık ve bundan doğan güçlük bulunur."},{"boundary_match":"partial","distinction":"Odak dalın merkezi işin güçleşmesidir; komşu dalın merkezi iki taraflı engelleşmedir.","focus_only":"İşin dolambaçlı hale gelmesini ve tek taraflı ya da karşılıklı zorlaştırmayı kapsar.","gloss":"karşılıklı engelleşme","neighbor_only":"Belirli bir şey üzerinde iki tarafın karşılıklı itme ve engellemesini gerektirir.","neighbor_ref":"root_001448/B006","relation_type":"near_neighbor","shared_zone":"Karşı tarafın istediği ilerleyişi engelleme her iki dalda da görülebilir."}],"source_phrase_ar":"العسر الخلاف والالتواء (maqayis;ayn); عسرت عليه تعسيرا إذا خالفته (maqayis); عسر عليه الأمر أي التاث (sihah); عسرت على فلان الأمر تعسيرا (tahdhib); استعسرت فلانا إذا طلبت معسوره (tahdhib); تعاسر القوم طلبوا تعسير الأمر (mufradat)","source_summary":"Kaynaklar karşı çıkma ve dolambaçlılık ile bir işi zorlaştırma arasında bağ kurar; karşılıklı zorlaştırma ve güç elde edileni isteme de aynı alanda verilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الخلاف والالتواء وتعسير الأمر والمعاسرة والتعاسر واستعسار المعسور","what_is_not_ar":"لا يدخل فيه تغسر الغزل بالغين ولا تجعل عقدة الغزل شاهدا صريحا للعين"},"support_links":[]},{"boundary":"Kuşlardaki tüy veya renk özelliği ancak sol yanda bulunduğunda bu dala girer.","branch_kind":"mixed_non_bare","branch_ref":"root_001012/B005","candidate_links":[{"candidate_id":"cand_721defe88f0aea4818cf","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","surface_ar":"عُسْرِ"}],"gloss":"sol taraf ve sola özgü olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sağın karşısındaki sol taraf ve bir kişinin solunda bulunma ilişkisidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlerini sol eliyle yapan kişi bu yön ilişkisiyle nitelenir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kuşun sol yanında tüy fazlalığı veya beyazlık bulunması bu alana bağlı özel bir nitelemedir."}}],"root_ar":"ع س ر","root_id":"root_001012","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sol yönü, sol eli kullanmayı veya sol yandaki ayırt edici özelliği birlikte temsil eder.","boundary_detail":"Kuşlardaki tüy veya renk özelliği ancak sol yanda bulunduğunda bu dala girer.","branch_image_ar":"الشمال والأعسر","concept_gloss":"sol taraf ve sola özgü olma","contextual_glosses":[{"applicability":"İşlerini esas olarak sol eliyle yapan bir kişiyi niteleyen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel sol yönü ve kuşların sol yanındaki tüy ya da renk özelliğini kapsamaz.","preserves":"Sol taraf ile el kullanımı arasındaki kişisel özellik bağını korur."},"facet_ids":["F002"],"text":"solak","usage_role":"contextual"}],"definition":"Sol tarafı temel alan yön ve özellik alanıdır; sol elle çalışan kişiyi, iki eli de kullanabilen kişiye ilişkin özel kalıbı ve kuşun sol yanında bulunan fazla tüy veya beyazlığı kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sağın karşısındaki sol taraf ve bir kişinin solunda bulunma ilişkisidir."},{"facet_id":"F002","role":"specialization","statement":"İşlerini sol eliyle yapan kişi bu yön ilişkisiyle nitelenir."},{"facet_id":"F003","role":"associated_use","statement":"Kuşun sol yanında tüy fazlalığı veya beyazlık bulunması bu alana bağlı özel bir nitelemedir."}],"identity_rationale":"Kaynak ifadesi sol tarafı çekirdek alır; sol eliyle çalışan kişiyi ve kuşun sol yanında fazla tüy ya da beyazlık bulunmasını bu yön temeline bağlar.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"sol taraf"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"solak, sol eliyle çalışan"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"iki elini de kullanabilen"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"soluma gelmek"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"sol yanında fazla tüy veya beyazlık bulunan kartal"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"sol kanadında beyazlık bulunan güvercin"}],"lexicalization_note":"Tanım sol taraf çekirdeğini öne alır; iki eli kullanma ve kuşun sol yanındaki işaret gibi kalıba bağlı özellikleri ayrı tutar.","neighbor_coverage_note":"Bütün komşular değerlendirildi; sol yönle kısmi örtüşme ve sağ tarafla karşıtlık, dalın yönsel temelini en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sol yana bağlı bedensel ve hayvansal özelliklere açılır; komşu dal yönelme ve taraf bildiriminde genişler.","focus_only":"Solak kişiyi ve kuşun sol yanındaki tüy ya da renk özelliğini de kapsar.","gloss":"sol yan ve sol yön","neighbor_only":"Sol yöne gitme, sola bakma ve sol taraf topluluğu gibi yönsel kullanımları daha geniş işler.","neighbor_ref":"root_000772/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak çekirdeği sağın karşısındaki sol taraf ve sol yöndür."},{"boundary_match":"opposed","distinction":"Aynı sağ-sol ekseninde odak dal sol kutbu, komşu dal sağ kutbu temsil eder.","focus_only":"Sol tarafı, sol eli kullanmayı ve sol yandaki özellikleri bildirir.","gloss":"sağ taraf","neighbor_only":"Sağ tarafı, sağ eli ve sağ yöne yönelmeyi bildirir.","neighbor_ref":"root_001698/B002","relation_type":"antonym","shared_zone":"İki dal da bedenin veya uzamın karşılıklı iki yanından birini gösterir."}],"source_phrase_ar":"العسرى خلاف اليسرى (maqayis;sihah); الذي يعمل بشماله أعسر (maqayis); رجل أعسر بين العسر وامرأة عسراء (sihah;tahdhib); عقاب عسراء ريشها من الجانب الأيسر أكثر من الأيمن (sihah); حمام أعسر وعقاب عسراء بجناحه من يساره بياض (sihah;tahdhib)","source_summary":"Kaynaklar sol tarafı, sol eli kullanan kişiyi ve bazı kuşların sol yanındaki tüy ya da renk özelliğini aynı yön temelli alanda toplar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العسرى خلاف اليسرى والأعسر الذي يعمل بشماله وما في الطير من زيادة أو بياض في الجانب الأيسر","what_is_not_ar":"لا يدخل فيه اليسر التفاؤلي ولا كل بياض في الطير بلا جهة اليسار"},"support_links":["sup_d0330e40fa27788e3b3a"]},{"boundary":"Genel zorluk veya para darlığı değil, özellikle güç doğum söz konusudur.","branch_kind":"mixed_non_bare","branch_ref":"root_001012/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","surface_ar":"عُسْرِ"}],"gloss":"güç doğum yapmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadının doğum sırasında güçlük çekmesi ve doğumunun zor ilerlemesidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güç doğum ile kız çocuk doğmasını birlikte dileyen söz, bu çekirdeğe bağlı özel kullanımdır."}}],"root_ar":"ع س ر","root_id":"root_001012","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Doğumun kadın için zor ilerlediği veya tamamlandığı durumu karşılar.","boundary_detail":"Genel zorluk veya para darlığı değil, özellikle güç doğum söz konusudur.","branch_image_ar":"تعسر الولادة","concept_gloss":"güç doğum yapmak","contextual_glosses":[{"applicability":"Bir kadının doğum sırasında belirgin güçlük çektiğini anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğuma ilişkin özel dilek veya beddua kalıbını kapsamaz.","preserves":"Doğumun güç ve zor ilerlemesi anlamını doğal biçimde korur."},"facet_ids":["F001"],"text":"doğumu zor geçti","usage_role":"contextual"}],"definition":"Bir kadının doğumunun güçleşmesi veya güç doğum yapmasıdır; buna ilişkin özel söz kalıbı, doğumun güç olmasını ve kız çocuk doğmasını birlikte diler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadının doğum sırasında güçlük çekmesi ve doğumunun zor ilerlemesidir."},{"facet_id":"F002","role":"associated_use","statement":"Güç doğum ile kız çocuk doğmasını birlikte dileyen söz, bu çekirdeğe bağlı özel kullanımdır."}],"identity_rationale":"Kaynak ifadesi dalı doğumun kadın için güçleşmesiyle sınırlar ve bu duruma ilişkin beddua kalıbını bağlı bir kullanım olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kadının doğumu güçleşmek"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"doğumu güç olsun ve kız doğursun diye beddua etmek"}],"lexicalization_note":"Tanım güç doğum durumunu temel alır; doğum ve çocuğun cinsiyetini birlikte anan dilek kalıbını yalnız bağlı kullanım olarak tutar.","neighbor_coverage_note":"Bütün adaylar incelendi; sıradan doğum ile doğum sancısı, güç doğumun olay ve belirti sınırlarını en yararlı biçimde açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal doğum olayının güçlüğünü anlatır; komşu dal doğumun gerçekleşmesini tarafsız biçimde anlatır.","focus_only":"Doğumun güç ilerlemesini kurucu şart yapar.","gloss":"doğum yapmak","neighbor_only":"Güçlük şartı olmadan doğumun gerçekleşmesini ve çocuğun dünyaya gelmesini bildirir.","neighbor_ref":"root_001683/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kadının çocuğu dünyaya getirmesi olayı bulunur."},{"boundary_match":"partial","distinction":"Odak dal doğumun güçlüğüdür; komşu dal ise bu süreçteki sancının kendisidir.","focus_only":"Doğumun bütün olarak güç gerçekleşmesi durumunu bildirir.","gloss":"doğum sancısı","neighbor_only":"Doğuma eşlik eden sancı ve ağrıyı olayın bir evresi olarak bildirir.","neighbor_ref":"root_000946/B008","relation_type":"near_neighbor","shared_zone":"İki dal da zorlayıcı bir doğum sürecinin içinde yer alabilir."}],"source_phrase_ar":"أعسرت المرأة إذا عسر عليها ولادها (maqayis;sihah;tahdhib); أعسرت وآنثت (maqayis;tahdhib); أيسرت وأذكرت (maqayis;tahdhib)","source_summary":"Kaynaklar kadının doğumunun güçleşmesi anlamında birleşir ve güç doğumla kız çocuk doğmasını birlikte anan geleneksel söz kullanımını da kaydeder.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه أعسرت المرأة إذا عسر عليها ولادها والدعاء عليها أو لها في الولادة","what_is_not_ar":"لا يدخل فيه العسر المالي ولا صعوبة الأمر العامة"},"support_links":[]},{"boundary":"Anlam, o yıl gebe kalmama haliyle sınırlıdır ve bütün kaynakların ortak kabulü gibi sunulmamalıdır.","branch_kind":"bare","branch_ref":"root_001012/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","surface_ar":"عُسْرِ"}],"gloss":"o yıl gebe kalmayan deve","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"O yıl çiftleşmesine rağmen gebe kalmayan dişi deveye ilişkin bir adlandırmadır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu adlandırma bazı aktarımlarca kabul edilirken bir başka aktarımca yanlış sayılır."}}],"root_ar":"ع س ر","root_id":"root_001012","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız bu hayvan adlandırmasını kabul eden aktarım çizgisinde ve görüş ayrılığı saklı tutularak kullanılır.","boundary_detail":"Anlam, o yıl gebe kalmama haliyle sınırlıdır ve bütün kaynakların ortak kabulü gibi sunulmamalıdır.","branch_image_ar":"الناقة التي لا تحمل عامها","concept_gloss":"o yıl gebe kalmayan deve","contextual_glosses":[{"applicability":"Eski hayvancılık söz varlığındaki tartışmalı adlandırmayı açıklamak gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan türünü, ilgili yılı ve gebe kalmama halini açıkça korur."},"facet_ids":["F001","F002"],"text":"bu yıl gebe kalmamış deve","usage_role":"explanatory"}],"definition":"Bazı aktarımlarda, çiftleşme döneminden geçmesine rağmen o yıl gebe kalmayan deve için kullanılan addır; bu açıklamanın doğruluğu başka bir aktarımda reddedilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"O yıl çiftleşmesine rağmen gebe kalmayan dişi deveye ilişkin bir adlandırmadır."},{"facet_id":"F002","role":"source_variant","statement":"Bu adlandırma bazı aktarımlarca kabul edilirken bir başka aktarımca yanlış sayılır."}],"identity_rationale":"Kaynak ifadesi bir kısım aktarımda bu adı o yıl gebe kalmayan deve için verirken başka bir aktarım bu açıklamayı açıkça yanlış sayar; dal ancak bu görüş ayrılığı belirtilerek korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"o yıl çiftleştiği halde gebe kalmayan deve"}],"lexicalization_note":"Tanım yalnız çıplak biçime verilen, o yıl gebe kalmayan deve anlamını ve bu anlam üzerindeki kaynak ayrılığını yansıtır.","neighbor_coverage_note":"Tüm komşular değerlendirildi; gebe kalmayan deveyle kısmi örtüşme ve belli olmuş gebelikle karşıtlık, tartışmalı dalın sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yıllık ve tartışmalı bir adlandırmadır; komşu dal daha kalıcı bir gebe kalmama özelliğini ek nitelikle birlikte anlatır.","focus_only":"Gebe kalmama durumunu belirli bir yılla sınırlar ve adlandırmanın kendisi tartışmalıdır.","gloss":"gebe kalmayan güçlü deve","neighbor_only":"Gebe kalmamayı süreklileşmiş bir özellik ve hayvanın gücünü korumasıyla birlikte verir.","neighbor_ref":"root_000980/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da dişi devenin gebe kalmaması durumunu adlandırır."},{"boundary_match":"opposed","distinction":"Aynı gebelik ekseninde odak dal gebeliğin oluşmamasını, komşu dal ise gebeliğin belirginleşmesini gösterir.","focus_only":"Devenin ilgili yıl gebe kalmamasını bildirir.","gloss":"gebeliği belli olan deve","neighbor_only":"Devenin gebe olduğunun belli hale gelmesini bildirir.","neighbor_ref":"root_001213/B006","relation_type":"polarity_pair","shared_zone":"İki dal da dişi devenin gebelik durumunu değerlendiren hayvancılık söz varlığına aittir."}],"source_phrase_ar":"العسير الناقة التي اعتاطت واعتاصت فلم تحمل عامها (maqayis); العسير الناقة إذا اعتاطت عامها فلم تحمل (sihah); تفسير الليث للعسير أنها الناقة التي اعتاطت غير صحيح (tahdhib)","source_summary":"Aktarımlar aynı deve açıklamasını kaydeder, ancak bunun doğru bir kullanım olup olmadığı konusunda uyuşmaz: bir görüş kabul ederken diğeri reddeder.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه تفسير العسير بالناقة التي اعتاطت أو اعتاصت فلم تحمل عامها عند من قبله","what_is_not_ar":"لا يدخل فيه الناقة التي ركبت قبل أن تراض عند من فرق بينهما"},"support_links":[]},{"boundary":"Devenin gebe kalmaması değil; hazırlık, alıştırma veya rıza öncesinde zorlama belirleyicidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001012/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","surface_ar":"عُسْرِ"}],"gloss":"hazır olmadan zorlayıp kullanmak veya almak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hazırlık, alıştırma veya rıza tamamlanmadan bir şeyi zorlayarak kullanma ya da alma işlemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Henüz eğitilip uysallaştırılmamış deveye binmek hayvancılık alanındaki gerçekleşmesidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişinin malını istememesine rağmen almak, rıza beklemeyen zorlama yönünü sürdürür."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Sözü düşünüp düzenlemeden doğaçlama söylemek, hazırlık beklememe yönünün konuşmaya uzanmasıdır."}}],"root_ar":"ع س ر","root_id":"root_001012","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Alıştırma, hazırlık ya da rıza beklenmeden gerçekleşen bütün dal kullanımlarını temsil eder.","boundary_detail":"Devenin gebe kalmaması değil; hazırlık, alıştırma veya rıza öncesinde zorlama belirleyicidir.","branch_image_ar":"الركوب والأخذ قبل التهيئة","concept_gloss":"hazır olmadan zorlayıp kullanmak veya almak","contextual_glosses":[{"applicability":"Bir kişinin malı, o istemediği halde elinden alındığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eğitilmemiş hayvana binme ve sözü hazırlamadan söyleme kullanımlarını kapsamaz.","preserves":"Sahibinin rızasını beklemeden zorlama yoluyla alma yönünü korur."},"facet_ids":["F001","F003"],"text":"zorla almak","usage_role":"contextual"},{"applicability":"Bir söz önceden düşünülüp düzenlenmeden doğrudan söylendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvana binme ve bir malı sahibinden zorla alma kullanımlarını kapsamaz.","preserves":"Hazırlık tamamlanmadan eyleme geçme yönünü konuşma bağlamında korur."},"facet_ids":["F001","F004"],"text":"hazırlıksız söylemek","usage_role":"contextual"}],"definition":"Bir şeyi alışması, hazırlanması veya sahibinin razı olması beklenmeden zorlayarak kullanmak ya da almaktır; eğitilmemiş deveye binme, isteksiz sahibinden mal alma ve sözü hazırlamadan söyleme bunun ayrı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hazırlık, alıştırma veya rıza tamamlanmadan bir şeyi zorlayarak kullanma ya da alma işlemidir."},{"facet_id":"F002","role":"specialization","statement":"Henüz eğitilip uysallaştırılmamış deveye binmek hayvancılık alanındaki gerçekleşmesidir."},{"facet_id":"F003","role":"extension","statement":"Bir kişinin malını istememesine rağmen almak, rıza beklemeyen zorlama yönünü sürdürür."},{"facet_id":"F004","role":"extension","statement":"Sözü düşünüp düzenlemeden doğaçlama söylemek, hazırlık beklememe yönünün konuşmaya uzanmasıdır."}],"identity_rationale":"Kaynak ifadesindeki farklı kullanımlar, bir şeyi eğitilmesini, hazırlanmasını veya sahibinin isteğini beklemeden zorlayarak kullanma ya da alma ortak işlemi altında birleşir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"eğitilmeden binilen deve"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"eğitilmeden önce binilen deve"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"zorla almak"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"oğlu istemediği halde malından almak"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"sözü hazırlamadan doğaçlama söylemek"}],"lexicalization_note":"Tanım hazır olmadan zorlama çekirdeğini korur; hayvana binme, mal alma ve hazırlıksız konuşma kullanımlarını ayrı alanlar olarak gösterir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; zorla alma ve sertçe sürükleme karşılaştırmaları, bu dalın hazırlık ve rıza beklemeyen kullanım sınırını keskinleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hazır oluşu veya rızayı beklememeyi ortak çekirdek yapar ve başka alanlara genişler; komşu dal haksız zorla almada yoğunlaşır.","focus_only":"Eğitilmemiş hayvanı kullanma ve sözü hazırlamadan söyleme alanlarına da uzanır.","gloss":"haksızlıkla zorla almak","neighbor_only":"Bir şeyi sahibinden haksızlık ve üstün güç yoluyla alma eylemini merkez alır.","neighbor_ref":"root_001090/B001","relation_type":"near_synonym","shared_zone":"İki dal da sahibinin isteğine karşı bir şeyi zor kullanarak alma anlamında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın sonucu kullanma ya da elde etmedir; komşu dalın çekirdeği canlıyı şiddetle sürme ve çekmedir.","focus_only":"Bir şeyi hazırlanmadan kullanma veya rıza olmadan alma işlemini bildirir.","gloss":"sertçe sürükleyip götürmek","neighbor_only":"İnsan ya da hayvanı tutup sertçe sürükleme, itme veya götürme hareketini bildirir.","neighbor_ref":"root_000980/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da karşı koymaya rağmen uygulanan fiziksel zorlama bulunabilir."}],"source_phrase_ar":"الناقة التي تركب قبل أن تراض عوسرانية (maqayis); العسير الناقة التي لم ترض وقد اعتسرتها إذا ركبتها قبل أن تراض (sihah); اعتسره مثل اقتسره (sihah); العسير الناقة التي ركبت قبل تذليلها (tahdhib); يعتسر الرجل من مال ولده معناه يأخذ من ماله وهو كاره (tahdhib); اعتسرت الكلام إذا اقتضبته قبل أن تزوره وتهيئه (tahdhib)","source_summary":"Kaynaklar eğitilmemiş deveye binme ile zorla alma arasında bağ kurar; bir aktarım aynı hazırlıksızlık yönünü sözü önceden düzenlemeden söylemeye genişletir. Eğitilmeden binilen deveye ilişkin adlandırma bir kaynakta verilirken başka bir kaynakta açıkça reddedilir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الناقة أو الجمل الذي يركب قبل الرياضة والاعتسار بمعنى الاقتسار وأخذ المال أو الكلام قبل رضى أو تهيئة","what_is_not_ar":"لا يدخل فيه امتناع الحمل في الناقة عند من رده"},"support_links":[]},{"boundary":"Genel koşu hızı değil, koşarken kuyruğun aldığı yukarı kalkık veya bükük durum belirleyicidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001012/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","surface_ar":"عُسْرِ"}],"gloss":"koşarken kuyruğunu kaldırmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hayvanın koşu sırasında kuyruğunu yukarı kaldırması veya bükmesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Davranış özellikle develer ve koşan kurtlar için adlandırılır."}}],"root_ar":"ع س ر","root_id":"root_001012","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Deve veya kurdun koşu sırasında kuyruğunu yukarı kaldırdığı ya da büktüğü davranışı karşılar.","boundary_detail":"Genel koşu hızı değil, koşarken kuyruğun aldığı yukarı kalkık veya bükük durum belirleyicidir.","branch_image_ar":"رفع الذنب في العدو","concept_gloss":"koşarken kuyruğunu kaldırmak","contextual_glosses":[{"applicability":"Hayvanın koşarken kuyruğunu yukarı kaldırdığını betimleyen cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuyruğun koşu sırasında yukarı kaldırılıp taşınması davranışını korur."},"facet_ids":["F001","F002"],"text":"kuyruğunu dikerek koşmak","usage_role":"contextual"}],"definition":"Devenin veya kurdun koşarken kuyruğunu kaldırması, dikleştirmesi ya da bükerek taşımasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hayvanın koşu sırasında kuyruğunu yukarı kaldırması veya bükmesidir."},{"facet_id":"F002","role":"specialization","statement":"Davranış özellikle develer ve koşan kurtlar için adlandırılır."}],"identity_rationale":"Kaynak ifadesi koşu sırasında devenin ya da kurdun kuyruğunu yukarı kaldırmasını veya bükmesini açık ve tutarlı biçimde dalın merkezi yapar.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"koşarken kuyruğunu kaldırıp büken deve"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"koşarken kuyruğunu kaldıran deve"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"koşarken kuyruklarını kaldıran veya büken develer ya da kurtlar"}],"lexicalization_note":"Tanım koşu sırasındaki kuyruk hareketini temel alır; deve ve kurtla kurulan biçimleri bu davranışın türlere bağlı gerçekleşmeleri sayar.","neighbor_coverage_note":"Verilen bütün komşular incelendi; koşu biçimi ve kuyruğun yana kayması, hareketin kuyruk ve koşu şartına bağlı sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal kuyruğun duruşuna, komşu dal ise bacaklar ve bütün gövdeyle yapılan hızlı ilerleyişe yöneliktir.","focus_only":"Koşu sırasında kuyruğun kaldırılması veya bükülmesini anlatır.","gloss":"hayvanın hızlı koşusu","neighbor_only":"Hayvanın koşusunun şiddetini, hızlanmasını ve yürüyüşe yüklenmesini anlatır.","neighbor_ref":"root_000336/B003","relation_type":"same_field","shared_zone":"İki dal da devenin veya binek hayvanının koşu sırasındaki davranışını betimler."},{"boundary_match":"partial","distinction":"Odak dal koşu sırasında yapılan kuyruk hareketidir; komşu dal ise arka gövde ve kuyruk kökünün anatomik adıdır.","focus_only":"Kuyruğun koşu sırasında etkin biçimde kaldırılması veya bükülmesi şartını taşır.","gloss":"arka gövde ve kuyruk kökü","neighbor_only":"Hayvanın arka gövdesindeki geniş bölgeyi ve kuyruk kökünü anatomik bir yer olarak bildirir.","neighbor_ref":"root_001243/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da hayvanın kuyruk bölgesiyle ilgili bir görünümü anlatır."}],"source_phrase_ar":"العاسر من النوق إذا عدت رفعت ذنبها (maqayis); عسرت الناقة بذنبها إذا شالت به (sihah); العاسرة من النوق فهي التي إذا عدت رفعت ذنبها (tahdhib); عواسر الذئاب التي تعسل في عدوها وتكسر أذنابها (tahdhib); ناقة عوسرانية إذا كان من دأبها تكسير ذنبها ورفعه إذا عدت (tahdhib)","source_summary":"Kaynaklar koşan devenin kuyruğunu kaldırmasında birleşir; kapsam ayrıca koşarken kuyruklarını büken kurtlara ve bu davranışı alışkanlık edinmiş deveye uzanır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العاسرة من النوق أو الذئاب إذا عدت فرفعت أو كسرت ذنبها وناقة عوسرانية بهذا الدأب","what_is_not_ar":"لا يدخل فيه العوسرانية بمعنى المركوبة قبل الرياضة حيث فرق المصدر"},"support_links":[]},{"boundary":"Anlam yalnız belirtilen gün kalıbına bağlıdır ve genel zorluk anlamına genişletilemez.","branch_kind":"collocation","branch_ref":"root_001012/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","surface_ar":"عُسْرِ"}],"gloss":"uğursuz gün","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli kalıp içinde bir günün uğursuz sayıldığını bildirir."}}],"root_ar":"ع س ر","root_id":"root_001012","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız bir günün uğursuz sayıldığını bildiren kayıtlı kalıbın karşılığıdır.","boundary_detail":"Anlam yalnız belirtilen gün kalıbına bağlıdır ve genel zorluk anlamına genişletilemez.","branch_image_ar":"اليوم المشؤوم","concept_gloss":"uğursuz gün","contextual_glosses":[{"applicability":"Günün yalnız zor değil, kötü sonuç getireceğine inanılan bir gün olduğunu açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uğursuzluk inancını ve bunun güne yüklenen bir nitelik oluşunu korur."},"facet_ids":["F001"],"text":"uğursuz sayılan gün","usage_role":"explanatory"}],"definition":"Uğursuz veya kötü sonuç getireceğine inanılan günü niteleyen kalıba bağlı bir anlamdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli kalıp içinde bir günün uğursuz sayıldığını bildirir."}],"identity_rationale":"Tek kaynak ifadesi bu kalıbı güç bir gün olarak değil, uğursuz sayılan bir gün olarak açıkça tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"uğursuz gün"}],"lexicalization_note":"Tanım yalnız uğursuz gün bildiren kalıba bağlıdır; kökün tek başına genel bir uğursuzluk anlamı taşıdığı sonucu çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; genel uğursuzluk ile zor gün anlamı, kalıbın uğursuzluk ve gün sınırını en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal günle sınırlı kalıplaşmış nitelemedir; komşu dal uğursuzluk alanının genel adlandırmasıdır.","focus_only":"Uğursuzluğu yalnız gün bildiren belirli bir kalıp içinde anlatır.","gloss":"uğursuzluk","neighbor_only":"Uğursuzluğu, uğursuz kişiyi ve topluluğa uğursuzluk getirdiğine inanılan şeyi genişçe kapsar.","neighbor_ref":"root_000772/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da kötü sonuç getireceğine inanılan uğursuzluk niteliğini taşır."},{"boundary_match":"partial","distinction":"Odak dal inanç temelli uğursuzluktur; komşu dal yaşanan güçlük ve çetinliktir.","focus_only":"Günün kötü sonuç getireceğine ilişkin uğursuzluk yargısını bildirir.","gloss":"zor gün","neighbor_only":"Günün güç ve çetin geçmesini, uğursuzluk inancı olmadan bildirir.","neighbor_ref":"root_001012/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da olumsuz değerlendirilen bir günü niteleyebilir."}],"source_phrase_ar":"يوم أعسر أي مشئوم (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu kalıp yalnız bir kaynakta uğursuz gün anlamıyla kaydedilmiştir."}],"source_summary":"Tek kaynaklı kayıt, kalıbın bir günü uğursuz diye nitelediğini açıkça belirtir.","sources":["TA"],"what_is_ar":"يدخل فيه يوم أعسر بمعنى مشؤوم","what_is_not_ar":"لا يدخل فيه كل يوم عسير بمعنى صعب شديد"},"support_links":[]},{"boundary":"Dağınık ilerleme ile ardışık ilerleme alternatif kullanımlardır; biri ötekinin zorunlu sonucu değildir.","branch_kind":"bare","branch_ref":"root_001012/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","surface_ar":"عُسْرِ"}],"gloss":"dağınık veya art arda ilerleme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Develerin yayılıp birbirinden ayrı halde gitmesini bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğun üyelerinin birbirinin ardından gelmesini bildirir."}}],"root_ar":"ع س ر","root_id":"root_001012","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bağlama göre ya birbirinden ayrılmış halde gitmeyi ya da birbiri ardınca gelmeyi karşılar.","boundary_detail":"Dağınık ilerleme ile ardışık ilerleme alternatif kullanımlardır; biri ötekinin zorunlu sonucu değildir.","branch_image_ar":"التفرق والتتابع","concept_gloss":"dağınık veya art arda ilerleme","contextual_glosses":[{"applicability":"Develerin yayılıp birbirinden ayrı biçimde ilerlediği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanların birbiri ardınca gelmesi kullanımını kapsamaz.","preserves":"Topluluğun yayılıp ayrı halde ilerlemesi görünümünü korur."},"facet_ids":["F001"],"text":"dağılarak gitmek","usage_role":"contextual"},{"applicability":"Bir topluluğun üyeleri art arda geldiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Develerin yayılıp birbirinden ayrı gitmesi kullanımını kapsamaz.","preserves":"Bireylerin birbirini izleyerek gelmesi düzenini korur."},"facet_ids":["F002"],"text":"birbiri ardınca gelmek","usage_role":"contextual"}],"definition":"Develerin dağılıp birbirinden ayrı gitmesini veya insanların birbirinin ardından gelmesini anlatan iki yönlü bir hareket düzenidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Develerin yayılıp birbirinden ayrı halde gitmesini bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Bir topluluğun üyelerinin birbirinin ardından gelmesini bildirir."}],"identity_rationale":"Tek kaynak ifadesi aynı biçimleri hem dağılma ve birbirinden ayrılma hem de birbiri ardınca gelme için verir; dal bu iki düzeni tek bir sonuç gibi birleştirmeden sunulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"dağınık halde veya birbiri ardınca"}],"lexicalization_note":"Tanım çıplak biçimlerin iki kayıtlı kullanımını korur ve bunlara yapı veya grup büyüklüğü gibi ek şartlar yüklemez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; iz üzerinde ardışıklık ve develerin dağılması, dalın iki alternatif kullanımını ayrı ayrı belirginleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ardışıklığı daha gevşek verir ve dağılma anlamına da sahiptir; komşu dal aynı iz ve yol üzerindeki takibi belirginleştirir.","focus_only":"Art arda gelişin yanında dağılıp ayrı gitme seçeneğini de taşır.","gloss":"birbirinin izinden ilerlemek","neighbor_only":"Aynı yol üzerinde birinin izinden giden düzenli ardışıklığı özellikle gerektirir.","neighbor_ref":"root_000932/B009","relation_type":"near_synonym","shared_zone":"Her iki dalda da topluluk üyelerinin birbiri ardınca hareket etmesi bulunur."},{"boundary_match":"partial","distinction":"Odak dal iki farklı hareket düzenine sahiptir; komşu dal yalnız dağılma olayıyla sınırlıdır.","focus_only":"Dağılma yanında insanların birbiri ardınca gelmesi anlamını da kapsar.","gloss":"develerin dağılması","neighbor_only":"Yalnız develerin birbirinden ayrılıp dağılması olayını bildirir.","neighbor_ref":"root_000863/B007","relation_type":"near_synonym","shared_zone":"İki dal da develerin toplu düzeni bozarak birbirinden ayrılmasını anlatır."}],"source_phrase_ar":"ذهبت الإبل عساريات وعشاريات إذا انتشرت وتفرقت (tahdhib); جاءوا عساريات وعسارى أي بعضهم في إثر بعض (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Dağılma ve art arda gelme anlamlarının ikisi de yalnız bu kayıtta birlikte verilmiştir."}],"source_summary":"Tek kaynaklı kayıt, biçimi develerin dağılıp gitmesi ve insanların birbiri ardınca gelmesi şeklinde iki ayrı hareket düzeniyle açıklar.","sources":["TA"],"what_is_ar":"يدخل فيه ذهاب الإبل عساريات أو مجيء القوم عساريات وعسارى أي متفرقين أو بعضهم في إثر بعض","what_is_not_ar":"لا يدخل فيه العسرى خلاف اليسرى"},"support_links":[]},{"boundary":"Bu ad kullanımları güçlük bildiren sıradan niteleme gibi yorumlanmamalıdır.","branch_kind":"bare","branch_ref":"root_001012/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","surface_ar":"عُسْرِ"}],"gloss":"cin topluluğu veya yer adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir cin topluluğuna verilen özel ad işlevi vardır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Cinlerin yaşadığı kabul edilen araziyi veya genel olarak bir yeri adlandırma işlevi de vardır."}}],"root_ar":"ع س ر","root_id":"root_001012","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kayıtlı özel ad işlevlerini betimlemek için kullanılır; biçimin kendisini yeniden üretmez.","boundary_detail":"Bu ad kullanımları güçlük bildiren sıradan niteleme gibi yorumlanmamalıdır.","branch_image_ar":"أعلام الجن والمواضع","concept_gloss":"cin topluluğu veya yer adı","contextual_glosses":[{"applicability":"Adın bir topluluğa mı yoksa bir yere mi yöneldiği bağlamdan anlaşılmadığında üst açıklama olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ad işlevini ve cinlerle kurulan topluluk ya da yer ilişkisini korur."},"facet_ids":["F001","F002"],"text":"cinlerle ilişkilendirilen özel ad","usage_role":"explanatory"}],"definition":"Bir cin topluluğunu, cinlerin yaşadığı kabul edilen bir araziyi veya başka bir yeri adlandırmak için kullanılan özel ad alanıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir cin topluluğuna verilen özel ad işlevi vardır."},{"facet_id":"F002","role":"source_variant","statement":"Cinlerin yaşadığı kabul edilen araziyi veya genel olarak bir yeri adlandırma işlevi de vardır."}],"identity_rationale":"Kaynak ifadesi bu dalda betimleyici güçlük anlamı değil, bir cin topluluğu ile cinlerin yaşadığı arazi veya başka bir yer için kullanılan özel ad işlevlerini sıralar.","lexical_glosses":[{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"bir cin topluluğunun adı"},{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"cin topluluğu, cinlerin yaşadığı arazi veya yer adı"}],"lexicalization_note":"Tanım çıplak biçimlere yüklenen topluluk ve yer adı işlevleriyle sınırlıdır; betimleyici anlam eklemez.","neighbor_coverage_note":"Bütün adaylar incelendi; başka özel ad kümeleri yalnız alan ortaklığı taşır, bu yüzden cin topluluğu ve yer sınırını gösteren tek karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalın adları cin topluluğu ve onunla ilişkili yerlerle sınırlıdır; komşu dal farklı adların genel bir listesidir.","focus_only":"Cin topluluğu ile cinlerin yaşadığı kabul edilen arazi veya yer adlarını kapsar.","gloss":"çeşitli özel adlar ve yer adları","neighbor_only":"Başka kökten gelen çeşitli kişi, topluluk ve yer adlarını topluca kapsar.","neighbor_ref":"root_000302/B009","relation_type":"same_field","shared_zone":"Her iki dal da betimleyici anlamdan ayrılmış kişi, topluluk veya yer adları alanına girer."}],"source_phrase_ar":"العسرة قبيلة من قبائل الجن (tahdhib); عسر قبيلة من الجن (tahdhib); عسر أرض يسكنها الجن (tahdhib); عسر موضع (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Topluluk ve yer adı işlevlerinin tamamı yalnız bir kaynakta kaydedilmiştir."}],"source_summary":"Tek kaynaklı kayıt, biçimleri bir cin topluluğunun adı ile cinlerle ilişkilendirilen arazi veya başka bir yerin adı olarak verir.","sources":["TA"],"what_is_ar":"يدخل فيه العسرة قبيلة من الجن وعسر أرض أو موضع","what_is_not_ar":"لا يدخل فيه المعنى الوصفي للصعوبة"},"support_links":[]},{"boundary":"Her çubuk oyunu değil, belirtilen kurulum ve yerinden çıkarma işlemi bu dala girer.","branch_kind":"bare","branch_ref":"root_001012/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","surface_ar":"عُسْرِ"}],"gloss":"çubuk atıp dikili çubuğu çıkarma oyunu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Oyunda hedef olarak bir çubuk dikilir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başka bir çubuk hedefe atılır ve dikili çubuğun yerinden çıkarılması amaçlanır."}}],"root_ar":"ع س ر","root_id":"root_001012","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dikili hedef çubuğun başka bir çubuk atılarak yerinden çıkarıldığı özel oyunu karşılar.","boundary_detail":"Her çubuk oyunu değil, belirtilen kurulum ve yerinden çıkarma işlemi bu dala girer.","branch_image_ar":"لعبة العسر","concept_gloss":"çubuk atıp dikili çubuğu çıkarma oyunu","contextual_glosses":[{"applicability":"Oyunun adından çok oynanışını açıklamak gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikili hedefi başka bir çubukla vurup yerinden çıkarma işlemini korur."},"facet_ids":["F001","F002"],"text":"dikili çubuğu vurup çıkarma oyunu","usage_role":"explanatory"}],"definition":"Bir çubuğun dikildiği, ardından başka bir çubuğun ona atılarak dikili çubuğun yerinden çıkarıldığı oyundur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Oyunda hedef olarak bir çubuk dikilir."},{"facet_id":"F002","role":"core","statement":"Başka bir çubuk hedefe atılır ve dikili çubuğun yerinden çıkarılması amaçlanır."}],"identity_rationale":"Kaynak ifadesi oyunun araçlarını ve temel işlemini açıkça verir: bir çubuk dikilir, başka bir çubuk ona atılır ve dikilen çubuk yerinden çıkarılır.","lexical_glosses":[{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"dikili çubuğa başka çubuk atıp onu yerinden çıkarma oyunu"}],"lexicalization_note":"Tanım çıplak biçimin adlandırdığı özel oyunla sınırlıdır ve bunu genel oyun ya da genel çubuk anlamına yaymaz.","neighbor_coverage_note":"Bütün komşular değerlendirildi; benzer çubuk oyunu ve oyundaki vurma aracı, bu dalın tam oyun düzenini en yararlı biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hedef çubuğun yerinden çıkarılmasıyla tanımlanır; komşu dal hedef ve vurma çubuğunun adlarını ve vurma eylemini daha geniş verir.","focus_only":"Atılan çubukla dikili hedef çubuğun yerinden çıkarılması sonucunu özellikle gerektirir.","gloss":"küçük hedefe çubukla vurma oyunu","neighbor_only":"Küçük hedef parçası ile ona vurmakta kullanılan çubuğu ayrı oyun araçları olarak adlandırır.","neighbor_ref":"root_001253/B005","relation_type":"near_synonym","shared_zone":"İki dalda da yere konan küçük bir hedefe başka bir çubukla vurulan geleneksel oyun düzeni vardır."},{"boundary_match":"thematic_only","distinction":"Odak dal bir oyun ve işlemler dizisidir; komşu dal ise bu sahnedeki araçlardan yalnız biridir.","focus_only":"Bütün oyunu, hedefin dikilmesini ve atışla çıkarılmasını birlikte bildirir.","gloss":"oyunda kullanılan vurma çubuğu","neighbor_only":"Benzer oyunda küçük hedefe vurmak için kullanılan çubuğun kendisini bildirir.","neighbor_ref":"root_001272/B008","relation_type":"thematic","shared_zone":"Her ikisi de küçük hedefe çubukla vurulan aynı tür geleneksel oyun sahnesine aittir."}],"source_phrase_ar":"العسر لعبة لهم ينصبون خشبة ثم ترمى بخشبة أخرى وتقلع (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Oyunun adı ve temel oynanış biçimi yalnız bir kaynakta kaydedilmiştir."}],"source_summary":"Tek kaynaklı kayıt, dikili bir çubuğun başka bir çubuk atılarak yerinden çıkarıldığı oyunu tanımlar.","sources":["TA"],"what_is_ar":"يدخل فيه لعبة العسر التي تنصب فيها خشبة ثم ترمى بخشبة أخرى وتقلع","what_is_not_ar":"لا يدخل فيه مطلق اللعب ولا الخشب بلا هذه التسمية"},"support_links":[]},{"boundary":"Azlık, varlıklılık, sol yön ve talih oyunu anlamları bu dalın dışında tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_001694/B001","candidate_links":[{"candidate_id":"cand_88daf543d5245fdd9fbb","lane":"macro"},{"candidate_id":"cand_fff4c49aac17b6bd9a86","lane":"macro"},{"candidate_id":"cand_732520c40bb078782bbb","lane":"macro"},{"candidate_id":"cand_1698ea31025eaddfffc0","lane":"macro"},{"candidate_id":"cand_e3a605033c69259b9c39","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"يُسْر","morph_features":"STEM|POS:N|LEM:yusor|ROOT:ysr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:4:1","qac_word_ref":"94:6:4","surface_ar":"يُسْرًا"}],"gloss":"kolaylık; kolay ve hazır duruma gelme ya da getirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, güç ve çetin olanın karşıtı biçimindeki kolaylıktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin kolaylaşıp hazır duruma gelmesi veya birinin onu kolaylaştırıp hazırlaması süreç anlamını oluşturur."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kimseye zorluk çıkarmamak ve ona anlayış göstermek, kolaylık çekirdeğinin kişiler arası kullanımıdır."}}],"root_ar":"ي س ر","root_id":"root_001694","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yalın durumunu ve ondan türeyen oluş ile oldurma süreçlerini birlikte karşılayan genel açıklamadır.","boundary_detail":"Azlık, varlıklılık, sol yön ve talih oyunu anlamları bu dalın dışında tutulur.","branch_image_ar":"انفتاح وسهولة بعد عسر","concept_gloss":"kolaylık; kolay ve hazır duruma gelme ya da getirme","contextual_glosses":[{"applicability":"Bir işin veya olanağın kendiliğinden ya da koşullar sayesinde yapılabilir duruma geldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın kolaylık, başkasına kolaylık sağlama ve anlayış gösterme kullanımlarını kapsamaz.","preserves":"Kolaylaşma ve hazır duruma gelme sürecini doğal bir eylem olarak korur."},"facet_ids":["F002"],"text":"kolaylaşıp hazır duruma gelmek","usage_role":"contextual"},{"applicability":"İki kişi arasındaki davranışın sertlikten uzak ve işi kolaylaştırıcı olduğunu anlatan bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesnenin kolay olması veya hazır duruma gelmesi anlamlarını dışarıda bırakır.","preserves":"Kişiler arası anlayış ve zorluk çıkarmama yönünü korur."},"facet_ids":["F003"],"text":"anlayış gösterip kolaylık sağlamak","usage_role":"contextual"}],"definition":"Güçlüğün karşıtı olan kolaylık ile bir şeyin kolay ve hazır duruma gelmesi ya da getirilmesidir. Birine zorluk çıkarmayıp anlayış gösterme kullanımı da bu çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, güç ve çetin olanın karşıtı biçimindeki kolaylıktır."},{"facet_id":"F002","role":"extension","statement":"Bir şeyin kolaylaşıp hazır duruma gelmesi veya birinin onu kolaylaştırıp hazırlaması süreç anlamını oluşturur."},{"facet_id":"F003","role":"associated_use","statement":"Bir kimseye zorluk çıkarmamak ve ona anlayış göstermek, kolaylık çekirdeğinin kişiler arası kullanımıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Miktarın düşük olduğu anlamını getirir.","collision":"Aynı kökün miktar azlığını bildiren ayrı dalıyla karışır.","fit":"displacement","loses":"Kolaylık, hazır duruma gelme ve kolaylaştırma işlemlerinin tümünü yitirir.","preserves":"Bazı bağlamlarda yükün veya sürenin sınırlı algılanmasını çağrıştırabilir."},"text":"az"}],"identity_rationale":"Kaynak ifadesi, güçlüğün karşıtı olan kolaylığı; bir şeyin kolaylaşıp hazır duruma gelmesini, onu kolaylaştırıp hazırlamayı ve karşılıklı anlayış göstermeyi birlikte bildirir. Dal çerçevesi bu çekirdeği ve ona bağlı eylem biçimlerini doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kolaylık, güçlüğün karşıtı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kolay olan, güç olmayan"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kolaylaşıp hazır duruma gelmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kolaylaştırıp hazırlamak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"birine anlayış gösterip kolaylık sağlamak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kolay olan"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kolay, güç olmayan"}],"lexicalization_note":"Tanım, yalın kolaylık anlamını bir şeyin kolaylaşması, hazırlanması veya kolaylaştırılması gibi türemiş kullanımlardan ayırarak kapsar.","neighbor_coverage_note":"Bütün komşu adayları karşılaştırıldı; en yakın sınır karışıklığını kolay ve hafif olma ile işi etkin biçimde kolaylaştırma dalları oluşturduğu için yalnızca bunlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kolaylık durumundan oluş ve oldurma süreçlerine uzanır; komşu dal ise işin hafif ve kişiye güç gelmeyen niteliğini öne çıkarır.","focus_only":"Hazır duruma gelme, hazırlama ve kişiler arası kolaylık gösterme kapsamları bulunur.","gloss":"kolay ve hafif olma","neighbor_only":"Bir işin kişiye hafif gelmesi ve yükünün azalması daha belirgindir.","neighbor_ref":"root_001608/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir işte güçlük bulunmamasını ve işin rahatça yapılabilmesini anlatır."},{"boundary_match":"partial","distinction":"Bu dal durum, oluş ve oldurma anlamlarını birlikte taşır; komşu dal özellikle bir işin yolunu açan etkin kolaylaştırmayı anlatır.","focus_only":"Yalın kolaylık ve bir şeyin kendiliğinden hazır duruma gelmesi de kapsanır.","gloss":"önünü açıp kolaylaştırma","neighbor_only":"Bir işin önünü açma ve yapılmasını sağlayacak yolu belirginleştirme öne çıkar.","neighbor_ref":"root_000751/B006","relation_type":"near_synonym","shared_zone":"İki dal da bir işteki engeli azaltma ve onun yapılmasını kolaylaştırma alanında buluşur."}],"source_phrase_ar":"اليسر: ضد العسر (maqayis;mufradat)؛ الميسور: ضد المعسور، وتيسر واستيسر بمعنى تهيأ (sihah)؛ تيسر واستيسر أي تسهل وتهيأ، وأيسرت المرأة وتيسرت في كذا أي سهلته وهيأته (mufradat)؛ ياسره أي ساهله (sihah)","source_summary":"Kaynaklar kolaylığın güçlüğe karşıt oluşunda, kolay ve hazır duruma gelme ile kolaylaştırma eylemlerinde birleşir; kişiler arası anlayış gösterme de aynı anlam alanında verilir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه اليسر ضد العسر، والميسور ضد المعسور، وتيسر الشيء واستيسر إذا تسهل وتهيأ، وتيسير الشيء وتهيئته، والمساهلة.","what_is_not_ar":"ليس المراد هنا اليسار جهة اليد، ولا الغنى، ولا القمار، ولا القلة المحضة."},"support_links":["sup_5e5357ab92cddc5e2bf8","sup_72e6bfb86acfe010819b","sup_7e541fc59ed5ee13f640","sup_896a8d3e750e18d50778","sup_92f5662c2e206751599f"]},{"boundary":"Tanım yalnızca miktar veya süre azlığını merkez alır; bağımsız kolaylık anlamını kapsamaz.","branch_kind":"bare","branch_ref":"root_001694/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُسْر","morph_features":"STEM|POS:N|LEM:yusor|ROOT:ysr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:4:1","qac_word_ref":"94:6:4","surface_ar":"يُسْرًا"}],"gloss":"az miktar veya kısa süre","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, bir şeyin miktar veya süre bakımından az olmasıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak ifadesindeki kolay veya hafif olma yönü, miktar azlığı çekirdeğinden ayrı tutulması gereken ikincil bir kullanımdır."}}],"root_ar":"ي س ر","root_id":"root_001694","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin miktarını ya da bir zaman aralığının sınırlılığını anlatan yalın kullanım için uygundur.","boundary_detail":"Tanım yalnızca miktar veya süre azlığını merkez alır; bağımsız kolaylık anlamını kapsamaz.","branch_image_ar":"قلة يسيرة","concept_gloss":"az miktar veya kısa süre","contextual_glosses":[{"applicability":"Sayılmayan bir şeyin küçük miktarını doğal akış içinde belirtmek için kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kısa süre kullanımını ve adla birlikte kurulan niteleme biçimini karşılamaz.","preserves":"Küçük miktar anlamını kısa ve doğal biçimde korur."},"facet_ids":["F001"],"text":"biraz","usage_role":"contextual"}],"definition":"Bir şeyin miktarının ya da bir sürenin az ve sınırlı olmasıdır. Kaynaktaki hafiflik çağrışımı, bu dalda ancak azlıkla bağlantılı olduğu ölçüde geçerlidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, bir şeyin miktar veya süre bakımından az olmasıdır."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak ifadesindeki kolay veya hafif olma yönü, miktar azlığı çekirdeğinden ayrı tutulması gereken ikincil bir kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bir işte güçlük bulunmadığı anlamını öne çıkarır.","collision":"Kolaylık dalıyla doğrudan karışır.","fit":"displacement","loses":"Dalın ayırt edici miktar ve süre azlığı çekirdeğini yitirir.","preserves":"Kaynak ifadesindeki ikincil hafiflik çağrışımını korur."},"text":"kolay"}],"identity_rationale":"Kaynak ifadesi sözcüğü hem az miktar hem de kolay ya da hafif olma yönüyle anar. Dal, miktar azlığını merkez almak koşuluyla kullanılabilir; kolaylık yönü ancak azlık algısına bağlı bir çağrışım olarak kalmalı ve birinci dalın çekirdeğinin yerine geçmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"az miktar veya kısa süre"}],"lexicalization_note":"Tanım yalın biçimin miktar ve süre bakımından azlık anlamıyla sınırlıdır; başka yapılara özgü anlamlar buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel azlık dalı en doğrudan karşılaştırmayı sağladı, öteki adaylar ya yalnızca özel örnekler ya da başka nicelik kutuplarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal az miktar ve kısa süreyi dar bir sözcük anlamı olarak verir; komşu dal genel azlığı ve kimi kullanımlarda değersiz görmeyi de kapsar.","focus_only":"Sürenin kısa oluşunu ve azlığın belirli bir niteleme biçimindeki kullanımını kapsar.","gloss":"azlık","neighbor_only":"Mal, yiyecek ve veriş azlığı gibi daha geniş alanlarla değersiz görme çağrışımına uzanır.","neighbor_ref":"root_000649/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin miktarının beklenenden veya bütünden az olmasını anlatır."}],"source_phrase_ar":"اليسير: القليل، وشيء يسير أي هين (sihah)؛ واليسير يقال في الشيء القليل (mufradat)","source_summary":"Kaynaklar azlık anlamında birleşir; aynı ifade içindeki kolay veya hafif olma yönü ise miktar dalının sınırını aşmaması gereken ayrı bir kullanımı gösterir.","sources":["SI","MU"],"what_is_ar":"يدخل فيه اليسير بمعنى القليل، والمدة أو الشيء اليسير من جهة قلته.","what_is_not_ar":"ليس هو سهولة الشيء ولا هوانه إلا إذا كان القصد إلى القلة نفسها."},"support_links":[]},{"boundary":"Sol yön ve genel kolaylık bu dala girmez; genişlik burada maddi olanak bolluğudur.","branch_kind":"mixed_non_bare","branch_ref":"root_001694/B003","candidate_links":[{"candidate_id":"cand_91760c6e0245cb1a5c7b","lane":"macro"},{"candidate_id":"cand_c35a42b66179a9a0fe49","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"يُسْر","morph_features":"STEM|POS:N|LEM:yusor|ROOT:ysr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:4:1","qac_word_ref":"94:6:4","surface_ar":"يُسْرًا"}],"gloss":"maddi bolluk ve varlıklı olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, maddi olanak bolluğu ve varlıklı olma durumudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin varlıklı duruma gelmesi, durum çekirdeğinin oluş bildiren uzantısıdır."}}],"root_ar":"ي س ر","root_id":"root_001694","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin veya durumun yeterli ve bol maddi olanağa sahip oluşunu anlatan genel karşılıktır.","boundary_detail":"Sol yön ve genel kolaylık bu dala girmez; genişlik burada maddi olanak bolluğudur.","branch_image_ar":"سعة وغنى","concept_gloss":"maddi bolluk ve varlıklı olma","contextual_glosses":[{"applicability":"Bir kişinin önceki durumundan çıkarak yeterli veya bol maddi olanağa eriştiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Süregelen maddi bolluk durumunu ad olarak karşılamaz.","preserves":"Varlıklılığa geçiş sürecini açıkça korur."},"facet_ids":["F002"],"text":"varlıklı duruma gelmek","usage_role":"contextual"}],"definition":"Maddi olanakların bol olması ve kişinin varlıklı bulunmasıdır. Türemiş kullanım, kişinin sonradan bu duruma erişmesini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, maddi olanak bolluğu ve varlıklı olma durumudur."},{"facet_id":"F002","role":"extension","statement":"Bir kişinin varlıklı duruma gelmesi, durum çekirdeğinin oluş bildiren uzantısıdır."}],"identity_rationale":"Kaynak ifadesi maddi genişlik ve varlıklılığı, ayrıca bir kimsenin varlıklı duruma gelmesini açıkça bildirir. Dal çerçevesi durum ile bu duruma geçişi birbirine karıştırmadan birlikte taşıyabilir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"maddi bolluk ve varlıklılık"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"varlıklılık ve maddi güç"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"varlıklılık"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"varlıklı duruma gelmek"}],"lexicalization_note":"Tanım, varlıklı olma durumunu bu duruma geçmeyi bildiren türemiş kullanımdan ayırır ve ikisini maddi olanakla sınırlar.","neighbor_coverage_note":"Tüm adaylar incelendi; genel varlıklılık ile yoksulluktan sonra varlıklı olma dalları, durum ve geçiş sınırlarını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal maddi varlıklılık durumuna ve ona erişmeye odaklanır; komşu dal maddi alanın ötesinde yapabilme gücü ve yeterliliğe de uzanır.","focus_only":"Varlıklı duruma gelmeyi bildiren belirli oluş kullanımı bulunur.","gloss":"varlıklılık ve maddi genişlik","neighbor_only":"Maddi gücün yanında yapabilme gücü ve genel yeterlilik kapsamı da vardır.","neighbor_ref":"root_001626/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin maddi bakımdan geniş olanaklara sahip olmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal geçiş için önceki bir yoksulluk koşulu koymaz; komşu dalın ayırt edici sınırı varlığın yoksulluktan sonra kazanılmasıdır.","focus_only":"Varlıklılığın süregelen durumunu ve maddi genişliği de adlandırır.","gloss":"yoksulluktan sonra varlıklı olma","neighbor_only":"Önceden yoksul olma koşulunu özellikle gerektirir.","neighbor_ref":"root_000406/B006","relation_type":"near_synonym","shared_zone":"İki dal da bir kişinin varlıklı duruma geçmesini bildirebilir."}],"source_phrase_ar":"الميسرة والميسرة: السعة والغنى؛ واليسار واليسارة: الغنى، وقد أيسر الرجل أي استغنى (sihah)؛ الميسرة واليسار عبارة عن الغنى (mufradat)","source_summary":"Kaynaklar maddi genişlik ile varlıklılık anlamlarında birleşir; bir kişinin varlıklı duruma gelmesini bildiren eylem de bu durumun oluş uzantısıdır.","sources":["SI","MU"],"what_is_ar":"يدخل فيه الميسرة واليسار واليسارة بمعنى السعة والغنى، وأيسر الرجل إذا استغنى.","what_is_not_ar":"ليس هو جهة اليسار، ولا اليسر ضد العسر إلا من حيث السعة المالية."},"support_links":["sup_0d9efaf938fb2d05a9df","sup_6c212d76b34d20643073"]},{"boundary":"Kolaylık, maddi bolluk ve talih oyunu anlamları yön bildiren bu dalın dışında kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_001694/B004","candidate_links":[{"candidate_id":"cand_721defe88f0aea4818cf","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"يُسْر","morph_features":"STEM|POS:N|LEM:yusor|ROOT:ysr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:4:1","qac_word_ref":"94:6:4","surface_ar":"يُسْرًا"}],"gloss":"sol el veya sol yön","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, sağın karşıtı olan sol el ve sol yöndür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birini sola götürmek veya sol yönde ilerlemek, yön çekirdeğinin hareket uzantısıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İki elini de kullanabilen kişi nitelemesi yalnızca kaynakta verilen özel söz öbeğine bağlıdır."}}],"root_ar":"ي س ر","root_id":"root_001694","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sağın karşısındaki bedensel tarafı veya uzamsal yönü belirtmek için kullanılan temel karşılıktır.","boundary_detail":"Kolaylık, maddi bolluk ve talih oyunu anlamları yön bildiren bu dalın dışında kalır.","branch_image_ar":"الجهة اليسرى واليد اليسرى","concept_gloss":"sol el veya sol yön","contextual_glosses":[{"applicability":"Bir kişinin veya topluluğun ilerleyişini sol tarafa çevirdiği hareket bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sol el adını ve iki eli kullanabilen kişi nitelemesini kapsamaz.","preserves":"Sol yönü seçme ve o yöne ilerleme eylemini korur."},"facet_ids":["F002"],"text":"sola yönelmek","usage_role":"contextual"}],"definition":"Sağın karşıtı olan sol el veya sol yöndür. Bu çekirdeğe bağlı biçimler sola yönelmeyi, özel bir söz öbeği ise iki eli de kullanabilen kişiyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, sağın karşıtı olan sol el ve sol yöndür."},{"facet_id":"F002","role":"extension","statement":"Birini sola götürmek veya sol yönde ilerlemek, yön çekirdeğinin hareket uzantısıdır."},{"facet_id":"F003","role":"specialization","statement":"İki elini de kullanabilen kişi nitelemesi yalnızca kaynakta verilen özel söz öbeğine bağlıdır."}],"identity_rationale":"Kaynak ifadesi sol eli ve sağın karşıtı olan sol yönü, sola yönelmeyi ve iki eli de kullanabilen kişi için kurulan özel ifadeyi açıkça kapsar. Dal çerçevesi bu yön çekirdeği ile ona bağlı hareket ve kişi nitelemesini doğru biçimde bir araya getirir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"sol el veya sol yön"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"soldaki, sağın karşıtı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sol taraf"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"sola yönelip ilerlemek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"iki elini de kullanabilen kişi"}],"lexicalization_note":"Tanım, yalın sol el ve sol yön anlamını sola yönelme eyleminden ve iki ellilik bildiren özel söz öbeğinden ayrı tutar.","neighbor_coverage_note":"Bütün yön ve beden bölgesi adayları karşılaştırıldı; en yararlı sınırlar örtüşen sol yön dalı ile karşıt kutuptaki sağ yön dalında bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Temel yön alanında büyük ölçüde örtüşürler; bu dal sola yönelme ile iki ellilik yapısını, komşu dal ise kendi benzetmeli el ve tutma uzantılarını taşır.","focus_only":"Sola yönelme eylemini ve iki ellilik bildiren özel kişi nitelemesini içerir.","gloss":"sol el ve sol taraf","neighbor_only":"Yön anlamından el ve tutma alanına uzanan benzetmeli kullanımları da kapsar.","neighbor_ref":"root_000819/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da sağın karşıtı olan sol eli ve sol yönü adlandırır."},{"boundary_match":"opposed","distinction":"Bu dal eksenin sol kutbunu, komşu dal ise sağ kutbunu anlatır; bu nedenle birbirlerinin yerine kullanılamazlar.","focus_only":"Sol el, sol taraf ve sola yönelme bulunur.","gloss":"sağ yön","neighbor_only":"Sağ el, sağ taraf ve sağa yönelme bulunur.","neighbor_ref":"root_001698/B002","relation_type":"polarity_pair","shared_zone":"İki dal bedenin ve uzamın karşılıklı iki yanını aynı yön ekseni üzerinde belirtir."}],"source_phrase_ar":"اليسار لليد، تياسروا إذ أخذوا ذات اليسار، وياسروا (maqayis)؛ الأيسر: نقيض الأيمن، والميسرة خلاف الميمنة، واليسار خلاف اليمين، والياسر نقيض اليامن، ورجل أعسر يسر للذي يعمل بكلتا يديه (sihah)","source_summary":"Kaynaklar sol el ve sol yön çekirdeğinde, sola yönelme eyleminde ve iki eli de kullanmayı bildiren özel kişi nitelemesinde birleşir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه اليسار لليد أو خلاف اليمين، والأيسر خلاف الأيمن، والميسرة خلاف الميمنة، والتياسر أو المياسرة بمعنى الأخذ ذات اليسار، ومن يعمل بكلتا يديه.","what_is_not_ar":"ليس هو اليسر ضد العسر، ولا الغنى المسمى يسارا، ولا القمار."},"support_links":["sup_d0330e40fa27788e3b3a"]},{"boundary":"Genel soyut kolaylık değil, canlıdaki uyumlu, hafif ve akıcı hareket niteliği söz konusudur.","branch_kind":"mixed_non_bare","branch_ref":"root_001694/B005","candidate_links":[{"candidate_id":"cand_41d8b7037f657ffdd2c4","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"يُسْر","morph_features":"STEM|POS:N|LEM:yusor|ROOT:ysr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:4:1","qac_word_ref":"94:6:4","surface_ar":"يُسْرًا"}],"gloss":"yumuşak başlı ve harekette uyumlu olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel nitelik, yumuşak başlılık ve yönlendirmeye hızlı uyum göstermedir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanda hafif bacaklar ve bacakların iyi aktarılması, uyumlu hareketin bedensel gerçekleşmeleridir."}}],"root_ar":"ي س ر","root_id":"root_001694","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya atın yönlendirmeye rahatça uymasını ve hareketinin akıcı olmasını birlikte anlatır.","boundary_detail":"Genel soyut kolaylık değil, canlıdaki uyumlu, hafif ve akıcı hareket niteliği söz konusudur.","branch_image_ar":"خفة وانقياد في الحركة","concept_gloss":"yumuşak başlı ve harekette uyumlu olma","contextual_glosses":[{"applicability":"Bir atın veya başka bir binek hayvanının bacaklarını rahat ve düzenli aktardığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan veya hayvanın genel yumuşak başlılık niteliğini kapsamaz.","preserves":"Bacak hafifliği ile iyi adım aktarımını doğal bir hareket anlatımıyla korur."},"facet_ids":["F002"],"text":"hafif ve düzgün adım atmak","usage_role":"contextual"}],"definition":"İnsan veya atın yumuşak başlı olup yönlendirmeye hızla uymasıdır. Hayvanda bu nitelik, bacakların hafifliği ve adımların iyi aktarılmasıyla özel olarak gerçekleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel nitelik, yumuşak başlılık ve yönlendirmeye hızlı uyum göstermedir."},{"facet_id":"F002","role":"specialization","statement":"Hayvanda hafif bacaklar ve bacakların iyi aktarılması, uyumlu hareketin bedensel gerçekleşmeleridir."}],"identity_rationale":"Kaynak ifadesi insan veya at için yumuşak başlı ve hızlı uyum gösteren olmayı, hafif bacakları ve hayvanın bacaklarını iyi aktarmasını birlikte bildirir. Dal çerçevesi davranış niteliği ile hareket gerçekleşmelerini aynı hareket kolaylığı alanında doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yumuşak başlı ve çabuk uyum gösteren"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"hafif bacaklar"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"hayvanın bacaklarını iyi aktarması"}],"lexicalization_note":"Tanım, canlıya ilişkin yalın uyumluluk niteliğini hafif bacak ve iyi adım aktarımı bildiren özel yapılardan ayırır.","neighbor_coverage_note":"Tüm hareket ve uyum adayları incelendi; genel yumuşaklık ile hafif bacak hareketi dalları çekirdek ve gerçekleşme ayrımını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal insan ve atta hızlı uyumu hareket hafifliğiyle birleştirir; komşu dal daha genel yumuşaklık, bükülme ve boyun eğme alanına yayılır.","focus_only":"Hızlı uyumun yanında hafif bacak ve iyi adım aktarımı özellikle bulunur.","gloss":"yumuşaklık ve uyum gösterme","neighbor_only":"Deve, yay ve binek için bükülme ve sahibine uyma gibi daha geniş yumuşaklık gerçekleşmeleri vardır.","neighbor_ref":"root_001028/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da canlı veya nesnenin yönlendirmeye direnmeden uyum göstermesini anlatır."},{"boundary_match":"partial","distinction":"Bu dal hafifliği uyumlu ve düzgün hareketle bağlar; komşu dal ise bacakların durmaksızın oynamasını ve kararsız hareketini öne çıkarır.","focus_only":"Yumuşak başlılık ve düzenli adım aktarımı olumlu hareket niteliğidir.","gloss":"hafif ve sürekli hareketli bacaklar","neighbor_only":"Bacakların çok hareketli ve yerinde durmaz olması özellikle belirtilir.","neighbor_ref":"root_001556/B004","relation_type":"near_neighbor","shared_zone":"İki dal da atın bacaklarındaki hafifliği ve hareket canlılığını konu edinir."}],"source_phrase_ar":"اليسرات: القوائم الخفاف؛ فرس حسن التيسور أي حسن نقل القوائم؛ رجل يسر ويسر أي حسن الانقياد (maqayis)؛ ليسر خفيف ويسر أي لين الانقياد سريع المتابعة يوصف به الإنسان والفرس (ayn)؛ اليسرات: القوائم الخفاف، ودابة حسن التيسور أي حسن نقل القوائم (sihah)","source_summary":"Kaynaklar yumuşak başlılık ve hızlı uyum niteliğinde, ayrıca hayvanın hafif bacakları ile adımlarını iyi aktarmasında birleşir.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه وصف الإنسان أو الفرس باللين وسرعة المتابعة، والقوائم الخفاف، وحسن نقل القوائم في الدابة.","what_is_not_ar":"ليس هو مجرد السهولة المعنوية، ولا اليسار جهة اليد، ولا الغنى."},"support_links":["sup_662e2b62efd288c9e8cd"]},{"boundary":"Anlam koyun sürüsüyle ve süt ile yavru artışının birlikte bildirildiği yapıyla sınırlıdır.","branch_kind":"collocation","branch_ref":"root_001694/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُسْر","morph_features":"STEM|POS:N|LEM:yusor|ROOT:ysr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:4:1","qac_word_ref":"94:6:4","surface_ar":"يُسْرًا"}],"gloss":"koyunların süt ve yavru bakımından çoğalması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Koyun sürüsünde süt veriminin çoğalması yapının ilk kurucu sonucudur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı sürüde yavru sayısının artması yapının ikinci kurucu sonucudur."}}],"root_ar":"ي س ر","root_id":"root_001694","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca koyun sürüsünde süt verimi ile yavru sayısının arttığını birlikte anlatan özel yapıya uygundur.","boundary_detail":"Anlam koyun sürüsüyle ve süt ile yavru artışının birlikte bildirildiği yapıyla sınırlıdır.","branch_image_ar":"إدرار ونماء في الغنم","concept_gloss":"koyunların süt ve yavru bakımından çoğalması","definition":"Koyun sürüsünün sütünün çoğalması ve yavru sayısının artmasıdır; anlam yalnızca bu hayvancılık yapısına bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Koyun sürüsünde süt veriminin çoğalması yapının ilk kurucu sonucudur."},{"facet_id":"F002","role":"core","statement":"Aynı sürüde yavru sayısının artması yapının ikinci kurucu sonucudur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Her türlü varlığın veya miktarın artabileceği sınırsız bir kapsam getirir.","collision":"Koyun, süt ve yavru koşullarını belirtmeyen genel artış anlamıyla karışır.","fit":"broadening","loses":null,"preserves":"Artış ve çoğalma yönünü genel düzeyde korur."},"text":"çoğalmak"}],"identity_rationale":"Kaynak ifadesi yalnızca koyun sürüsünün sütünün ve yavrusunun çoğalmasını bildiren belirli yapıyı verir. Dal çerçevesi bu iki artışı koruduğu ve genel bolluk anlamına yaymadığı sürece bütünüyle uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"koyunların sütü ve yavrusu çoğalmak"}],"lexicalization_note":"Tanım yalnızca koyun sürüsünü konu alan yerleşik yapıya bağlıdır; buradan yalın ve genel bir çoğalma anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel hayvan çoğalması ve uzun süreli süt bolluğu, yapının tür ile sonuç sınırlarını en açık gösteren iki komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir koyun yapısında süt ve yavru artışını birlikte ister; komşu dal çeşitli büyüme ve çoğalma türlerini daha genel biçimde kapsar.","focus_only":"Koyunlarda süt verimi ile yavru sayısının birlikte artmasını gerektirir.","gloss":"hayvanda büyüme ve çoğalma","neighbor_only":"Genel büyüme, ürün ve hayvan sayısı artışı ile sürü varlığını genişçe kapsar.","neighbor_ref":"root_001427/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da hayvan varlığında veya hayvandan elde edilen üründe artışı konu edinir."},{"boundary_match":"field_only","distinction":"Bu dal koyun sürüsünde süt ve yavru artışını birlikte anlatır; komşu dal devenin uzun süren süt bolluğuna odaklanır.","focus_only":"Süt veriminin yanında yavru sayısının artması da kurucu anlamdır.","gloss":"uzun süre bol sütlü olma","neighbor_only":"Devenin uzun süre süt biriktirmesi ve bol sütlü oluşu anlatılır.","neighbor_ref":"root_000752/B006","relation_type":"same_field","shared_zone":"İki dal da evcil hayvanın süt bolluğuyla ilgilidir."}],"source_phrase_ar":"يسرت الغنم إذا كثر لبنها ونسلها (maqayis;sihah)","source_summary":"Kaynaklar, koyun sürüsüne bağlı bu özel kullanımın hem süt verimindeki çoğalmayı hem de yavru artışını birlikte bildirdiğinde birleşir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه قولهم يسرت الغنم إذا كثر لبنها ونسلها.","what_is_not_ar":"ليس هو الغنى العام، ولا سهولة الأمر، إلا من جهة نماء خاص في الغنم."},"support_links":[]},{"boundary":"Kolaylık, sol yön ve maddi bolluk bu tarihsel oyun ve paylaştırma alanına girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001694/B007","candidate_links":[{"candidate_id":"cand_3ad3cf6ee2a8ca8e0907","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"يُسْر","morph_features":"STEM|POS:N|LEM:yusor|ROOT:ysr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:4:1","qac_word_ref":"94:6:4","surface_ar":"يُسْرًا"}],"gloss":"fal oklarıyla oynanan paylaştırmalı talih oyunu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel kurum, fal oklarıyla oynanan geleneksel talih oyunudur."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Oyunu oynayan kişi ve oyuna katılmak üzere toplanan topluluk ayrı adlandırmalara konu olur."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Katılımcıların deveyi kesip parçalarını oklarla belirlenen paylara göre bölüşmesi düzenin kurucu işlemidir."}}],"root_ar":"ي س ر","root_id":"root_001694","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Oyunu, katılımcıları ve kesilen devenin oklarla belirlenen paylara bölünmesini birlikte temsil eden tarihsel açıklamadır.","boundary_detail":"Kolaylık, sol yön ve maddi bolluk bu tarihsel oyun ve paylaştırma alanına girmez.","branch_image_ar":"قداح وقمار وتقسيم جزور","concept_gloss":"fal oklarıyla oynanan paylaştırmalı talih oyunu","contextual_glosses":[{"applicability":"Katılımcıların oyun için bir deveyi kesmesi ve et parçalarını çekilen oklara göre bölüşmesi bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Oyunun genel adını ve oyuncu adlarını kapsamaz.","preserves":"Kesme ve oklarla belirlenen paylara göre bölüşme işlemlerini korur."},"facet_ids":["F003"],"text":"deveyi kesip parçalarını oklarla paylaştırmak","usage_role":"explanatory"}],"definition":"Fal oklarıyla oynanan geleneksel bir talih oyunu ve bu oyunun çevresindeki paylaştırma düzenidir. Katılımcılar bir deveyi keser, parçalarını okların belirlediği paylara göre bölüşür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel kurum, fal oklarıyla oynanan geleneksel talih oyunudur."},{"facet_id":"F002","role":"associated_use","statement":"Oyunu oynayan kişi ve oyuna katılmak üzere toplanan topluluk ayrı adlandırmalara konu olur."},{"facet_id":"F003","role":"core","statement":"Katılımcıların deveyi kesip parçalarını oklarla belirlenen paylara göre bölüşmesi düzenin kurucu işlemidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Fal okları veya deve paylaştırması içermeyen bütün para ve şans oyunlarını kapsar.","collision":"Tarihsel araç ve paylaştırma düzenini belirtmeyen genel oyun adıyla karışır.","fit":"broadening","loses":null,"preserves":"Sonucu şansa bağlı oyun yönünü korur."},"text":"kumar"}],"identity_rationale":"Kaynak ifadesi fal oklarıyla oynanan geleneksel talih oyununu, bu oyuna katılanları ve kesilen devenin parçalarını oklarla paylaştırma işlemini birlikte verir. Dal çerçevesi oyun, katılımcı ve paylaştırma aşamalarını koruyarak kaynağı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"fal oklarıyla oynanan geleneksel talih oyunu"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"fal okları oyununa katılmak için toplananlar"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"fal oklarıyla oynayan kişi"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"fal oklarıyla oynayan kişi"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"topluluğun deveyi kesip parçalarını paylaştırması"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"deveyi kesip oyun düzenine göre paylaştırmak"}],"lexicalization_note":"Tanım, oyunun adını katılımcı adlarından ve devenin kesilip parçalarının oklarla paylaştırılmasını bildiren eylem biçimlerinden ayırır.","neighbor_coverage_note":"Bütün oyun aracı, oyuncu ve pay adayları incelendi; oyuncu veya ok adı ile genel pay kavramı, bütün oyun düzeninin sınırını en açık gösteren karşılaştırmalardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal oyun düzenini ve paylaştırma işlemini bütünüyle anlatır; komşu dal yalnızca bir oyuncu türünü veya belirli bir oyun okunu adlandırır.","focus_only":"Oyunun bütünü, oyuncu topluluğu ve devenin oklarla paylaştırılması kapsanır.","gloss":"talih oyunu oyuncusu veya oku","neighbor_only":"Belirli bir oyuncu veya oyunda kullanılan belirli bir ok adı öne çıkar.","neighbor_ref":"root_000432/B013","relation_type":"near_neighbor","shared_zone":"İki dal da aynı tarihsel talih oyununun katılımcı ve araç çevresinde yer alır."},{"boundary_match":"partial","distinction":"Bu dal payı belirli bir oyun, kesim ve ok çekme düzenine bağlar; komşu dal payı bu tarihsel koşullar olmadan genel olarak adlandırır.","focus_only":"Payın fal oklarıyla oynanan oyunda ve kesilen deve üzerinden belirlenmesi gerekir.","gloss":"belirlenmiş pay","neighbor_only":"Herhangi bir bağlamdaki belirli pay veya hak genel olarak kapsanır.","neighbor_ref":"root_001507/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir bütünden kişiye ayrılan pay düşüncesini içerir."}],"source_phrase_ar":"الأيسار: القوم يجتمعون على الميسر، واحدهم يسر؛ والميسر: القمار (maqayis)؛ الميسر: قمار العرب بالأزلام؛ الياسر: اللاعب بالقداح؛ اليسر والياسر بمعنى والجمع أيسار؛ يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها (sihah)","source_summary":"Kaynaklar fal oklarına dayalı talih oyunu, oyuna katılan kişiler ve kesilen devenin parçalarını oklarla belirlenen paylara göre bölüşme işlemlerinde birleşir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه الميسر قمار العرب بالأزلام، والأيسار أو الياسرون اللاعبون بالقداح، ويسر القوم الجزور إذا اجتزروها واقتسموا أعضاءها بالسهام.","what_is_not_ar":"ليس هو اليسر ضد العسر، ولا اليسار جهة اليد، ولا الغنى."},"support_links":["sup_1873718b8c21ce9368fe"]},{"boundary":"Avuç çizgileri ile uyluk damgası iki ayrı gerçekleşmedir; ortaklıkları bedensel çizgi veya iz olmalarıdır.","branch_kind":"bare","branch_ref":"root_001694/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُسْر","morph_features":"STEM|POS:N|LEM:yusor|ROOT:ysr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:4:1","qac_word_ref":"94:6:4","surface_ar":"يُسْرًا"}],"gloss":"ayrı avuç çizgileri veya uyluk damgası","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Avuç içindeki birbirine bitişmeyen çizgiler ilk beden izi anlamıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uyluklarda bulunan ayırt edici damga aynı biçimin ikinci beden izi anlamıdır."}}],"root_ar":"ي س ر","root_id":"root_001694","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Aynı yalın biçimin iki farklı beden izi kullanımını birbirine karıştırmadan birlikte gösteren açıklamadır.","boundary_detail":"Avuç çizgileri ile uyluk damgası iki ayrı gerçekleşmedir; ortaklıkları bedensel çizgi veya iz olmalarıdır.","branch_image_ar":"خطوط منفصلة وعلامات في البدن","concept_gloss":"ayrı avuç çizgileri veya uyluk damgası","definition":"Bedende görülen iki ayrı çizgi veya iz türünü adlandırır: avuç içinde birbirine bitişmeyen çizgiler ve uyluklarda bulunan bir damga.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Avuç içindeki birbirine bitişmeyen çizgiler ilk beden izi anlamıdır."},{"facet_id":"F002","role":"source_variant","statement":"Uyluklarda bulunan ayırt edici damga aynı biçimin ikinci beden izi anlamıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Yara, ben ve başka her türlü bedensel izi kapsayan geniş bir alan getirir.","collision":"Avuç çizgileri ile uyluk damgasına özgü sınırlar belirsizleşir.","fit":"broadening","loses":null,"preserves":"Her iki kullanımın bedende bulunan bir iz oluşunu korur."},"text":"beden izi"}],"identity_rationale":"Kaynak ifadesi aynı biçim altında avuç içindeki birbirine bitişmeyen çizgileri ve uyluklardaki damgayı verir. Bunlar bedendeki ayırt edici çizgi veya iz ortaklığında tutulabilir, ancak tek bir beden bölgesi ya da tek bir iz türüymüş gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"avuç içindeki birbirine bitişmeyen çizgiler"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"uyluklardaki damga"}],"lexicalization_note":"Tanım yalın biçimin iki beden izi anlamını ayrı ayrı korur; başka yapılardan yön veya oyun anlamı alınmaz.","neighbor_coverage_note":"Bütün beden izi adayları incelendi; genel iz ve damga dalı ile dövme deseni dalı, doğal çizgi ve işaret türü sınırlarını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal iki belirli beden iziyle sınırlıdır; komşu dal yaranın bıraktığı izden hayvan damgasına kadar daha geniş bir iz alanı taşır.","focus_only":"Birbirine bitişmeyen avuç çizgileri ve uyluklardaki özel damga bulunur.","gloss":"yara izi veya ayırt edici damga","neighbor_only":"Yara izi, genel damga ve hayvanı ayırt eden çizgi gibi daha geniş iz türleri bulunur.","neighbor_ref":"root_000995/B017","relation_type":"near_neighbor","shared_zone":"İki dal da bedende görülen çizgi, iz veya damgaları adlandırır."},{"boundary_match":"field_only","distinction":"Bu dal avuç çizgileri ve uyluk damgasını adlandırır; komşu dal özellikle dövme içindeki daire biçimli desenleri belirtir.","focus_only":"Doğal avuç çizgileri ile uyluktaki tekil damga söz konusudur.","gloss":"dövmedeki dairesel desenler","neighbor_only":"Dövme içinde oluşturulan dairesel desenler söz konusudur.","neighbor_ref":"root_001308/B014","relation_type":"same_field","shared_zone":"Her iki dal da beden üzerinde çizgi veya biçim oluşturan görsel işaretlerle ilgilidir."}],"source_phrase_ar":"اليسرة: أسرار الكف إذا كانت غير ملزقة (maqayis;sihah)؛ اليسرة أيضا: سمة في الفخذين (sihah)","source_summary":"Kaynaklar avuç içindeki birbirine bitişmeyen çizgileri bildirir; toplu ifade ayrıca aynı biçimin uyluklardaki bir damgayı da adlandırdığını gösterir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه اليسرة لأسرار الكف إذا كانت غير ملزقة، واليسرة سمة في الفخذين.","what_is_not_ar":"ليس هو جهة اليسار، ولا القمار، ولا السعة المالية."},"support_links":[]},{"boundary":"Aşağı doğru burma ile yüz hizasına saplama birbirinden ayrı iki teknik kullanımdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001694/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُسْر","morph_features":"STEM|POS:N|LEM:yusor|ROOT:ysr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:4:1","qac_word_ref":"94:6:4","surface_ar":"يُسْرًا"}],"gloss":"aşağı doğru burma veya yüz hizasına saplama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sağ eli gövdeye doğru çekerek bir şeyi aşağı yönlü büküp burmak yalın biçimin teknik anlamıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Saplamanın yüz hizasına yönelmesi yalnızca kaynakta verilen özel söz öbeğine bağlıdır."}}],"root_ar":"ي س ر","root_id":"root_001694","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın teknik hareket ile özel saplama söz öbeğini seçenekli ve birbirinden ayrı biçimde temsil eder.","boundary_detail":"Aşağı doğru burma ile yüz hizasına saplama birbirinden ayrı iki teknik kullanımdır.","branch_image_ar":"فتل إلى أسفل وطعن حذاء الوجه","concept_gloss":"aşağı doğru burma veya yüz hizasına saplama","contextual_glosses":[{"applicability":"Burmanın yönünü ve elin gövdeye doğru hareketini açıkça belirtmek gereken teknik bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yüz hizasına yöneltilen saplama kullanımını kapsamaz.","preserves":"El hareketini, gövdeye doğru çekişi ve aşağı yönlü burmayı korur."},"facet_ids":["F001"],"text":"sağ eli gövdeye çekerek aşağı doğru burmak","usage_role":"explanatory"}],"definition":"İki ayrı yönelimli işlemi bildirir: sağ eli gövdeye doğru çekerek aşağı yönlü burma ve bir saplamayı yüz hizasına yöneltme.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sağ eli gövdeye doğru çekerek bir şeyi aşağı yönlü büküp burmak yalın biçimin teknik anlamıdır."},{"facet_id":"F002","role":"specialization","statement":"Saplamanın yüz hizasına yönelmesi yalnızca kaynakta verilen özel söz öbeğine bağlıdır."}],"identity_rationale":"Kaynak ifadesi aşağı doğru büküp burmayı ve yüz hizasına yöneltilen saplamayı aynı dalda verir. Bunlar yönelimli iki teknik kullanımdır; ortak bir eylemin aşamaları sayılmamalı, ayrı gerçekleşmeler olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"sağ eli gövdeye çekerek aşağı doğru burma"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"yüz hizasına yöneltilen saplama"}],"lexicalization_note":"Tanım yalın biçimdeki aşağı doğru burmayı, yalnızca özel söz öbeğinde bulunan yüz hizasına saplama anlamından ayırır.","neighbor_coverage_note":"Bütün yöneltme ve saplama adayları değerlendirildi; aşağı yöneltme ile yüz hizasına düz saplama, iki teknik kullanımın sınırlarını en doğrudan gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal aşağı yönü belirli bir el hareketi ve burma işlemiyle sınırlar; komşu dal aşağı yöneltme ile aşağı inmeyi işlem türünden bağımsız anlatır.","focus_only":"Aşağı yön, elin gövdeye çekilmesiyle yapılan belirli bir burma işlemine bağlıdır.","gloss":"aşağı yöneltme veya inme","neighbor_only":"Herhangi bir şeyi aşağı yöneltme veya onun aşağı inmesi genel olarak kapsanır.","neighbor_ref":"root_000715/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir hareketin aşağıya yönelmesini bildirir."},{"boundary_match":"partial","distinction":"Bu dal yüz hizasını belirtir fakat düzlüğü kurucu koşul yapmaz; komşu dal yüz hizasıyla birlikte saplamanın dosdoğru oluşunu da gerektirir.","focus_only":"Yüz hizasına yönelme bulunur; ayrıca ayrı bir aşağı doğru burma anlamı taşır.","gloss":"yüz hizasına düz saplama","neighbor_only":"Saplamanın düz ve dosdoğru oluşu özellikle belirtilir.","neighbor_ref":"root_000735/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir saplamanın hedefin yüz hizasına yönelmesini anlatır."}],"source_phrase_ar":"اليسر: الفتل إلى أسفل، وهو أن تمد يمينك نحو جسدك؛ والطعن اليسر: حذاء وجهك (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, sağ eli gövdeye çekerek aşağı doğru burmayı ve yüz hizasına yöneltilen saplamayı ayrı kullanımlar olarak verir."}],"source_summary":"Dalın iki teknik yönelim kullanımı tek kaynak tanıklığına dayanır; aşağı doğru burma ile yüz hizasına saplama birbirinin yerine geçmez.","sources":["SI"],"what_is_ar":"يدخل فيه اليسر في الفتل إلى أسفل، والطعن اليسر حذاء الوجه.","what_is_not_ar":"ليس هو التياسر إلى جهة اليسار، ولا السهولة، ولا القمار."},"support_links":[]},{"boundary":"Bu dal bir kolaylık, yön veya varlıklılık anlamı değil, yer ve kişi adlarının toplu kaydıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001694/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُسْر","morph_features":"STEM|POS:N|LEM:yusor|ROOT:ysr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:4:1","qac_word_ref":"94:6:4","surface_ar":"يُسْرًا"}],"gloss":"yer ve kişi adı kullanımları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tek sözcüklü iki kullanım belirli yerleri adlandırır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özel söz öbeği, anlatıda geçen bir kişiyi adlandırır ve yer adı kullanımlarından ayrıdır."}}],"root_ar":"ي س ر","root_id":"root_001694","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Söz biçiminin türemiş anlamlarını değil, kaynaklarda doğrudan ad olarak kaydedilen kullanımlarını topluca gösterir.","boundary_detail":"Bu dal bir kolaylık, yön veya varlıklılık anlamı değil, yer ve kişi adlarının toplu kaydıdır.","branch_image_ar":"موضع أو علم باسم يسر ويسار","concept_gloss":"yer ve kişi adı kullanımları","definition":"Aynı söz biçiminin yer adı olarak kullanılan iki kaydını ve bir anlatıda kişi adı olarak geçen özel bir söz öbeğini kapsayan adlandırma dalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tek sözcüklü iki kullanım belirli yerleri adlandırır."},{"facet_id":"F002","role":"specialization","statement":"Özel söz öbeği, anlatıda geçen bir kişiyi adlandırır ve yer adı kullanımlarından ayrıdır."}],"identity_rationale":"Kaynak ifadesi iki yer adı kullanımı ile bir kişinin adı olarak geçen söz öbeğini açıkça sıralar. Dal, bunları türemiş bir ortak anlam gibi açıklamadan adlandırma kullanımları olarak tuttuğu sürece kaynağa uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bir yerin adı"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"çöl bölgesindeki bir geçidin adı"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"anlatıda geçen bir kişinin adı"}],"lexicalization_note":"Tanım, tek sözcüklü yer adlarını kişi adı içeren özel söz öbeğinden ayırır ve hiçbirinden genel bir yalın anlam türetmez.","neighbor_coverage_note":"Bütün adlandırma dalları değerlendirildi; yalnız yer adı içeren dal ile yer ve kişi adlarını birlikte içeren dal, bu kaydın kapsamını en iyi karşılaştırır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal yer adlarını bir kişi adı kullanımıyla birlikte toplar; komşu dal ise kendi biçimlerinin yalnızca yer adı oluşlarını kaydeder.","focus_only":"İki yer adının yanında özel bir söz öbeğinde kişi adı kullanımı da vardır.","gloss":"söz biçiminden aktarılan yer adları","neighbor_only":"Yalnızca kendi söz biçimlerinden aktarılan yer adlarını kapsar.","neighbor_ref":"root_000399/B006","relation_type":"same_field","shared_zone":"Her iki dal da sözlükte türemiş anlam olarak değil, doğrudan ad olarak kaydedilmiş yerleri içerir."},{"boundary_match":"field_only","distinction":"Anlam türleri benzer olsa da adlandırılan varlıklar ve onları taşıyan söz biçimleri ayrıdır; bu nedenle sözlüksel yerine geçme yoktur.","focus_only":"Aynı söz biçimine bağlı iki yer ve bir kişi adı kaydı vardır.","gloss":"yer, su kaynağı ve kişi adları","neighbor_only":"Kendi söz biçiminden aktarılan yer, su kaynağı ve kişi adı kayıtları bulunur.","neighbor_ref":"root_000361/B005","relation_type":"same_field","shared_zone":"İki dal da sıradan söz biçimlerinin özel ad olarak kullanılmasını kaydeder."}],"source_phrase_ar":"يسر: مكان (maqayis)؛ اليسر أيضا: دخل لنبى يربوع بالدهناء (sihah)؛ يسار الكواعب هو اسم عبد (sihah)","source_summary":"Toplu kaynak ifadesi, aynı söz biçiminin iki ayrı yer adı kullanımını ve özel bir söz öbeğinin kişi adı kullanımını herhangi bir türetme bağı kurmadan bir araya getirir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه يسر أو اليسر اسما لمكان، ويسار علما لشخص في شاهد شعري.","what_is_not_ar":"ليس هذا معنى اشتقاقيا كالسهولة أو اليسار أو الميسر."},"support_links":[]},{"boundary":"Anlam genç erkekle sınırlıdır; varlıklılık, sol yön ve kişi adı kullanımları bu dala girmez.","branch_kind":"bare","branch_ref":"root_001694/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُسْر","morph_features":"STEM|POS:N|LEM:yusor|ROOT:ysr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:4:1","qac_word_ref":"94:6:4","surface_ar":"يُسْرًا"}],"gloss":"genç erkek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yalın biçim genç yaştaki bir erkeği adlandırır."}}],"root_ar":"ي س ر","root_id":"root_001694","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaşı genç olan erkek kişiyi adlandıran yalın kullanım için doğrudan ve eksiksiz karşılıktır.","boundary_detail":"Anlam genç erkekle sınırlıdır; varlıklılık, sol yön ve kişi adı kullanımları bu dala girmez.","branch_image_ar":"فتى يسمى يسارا","concept_gloss":"genç erkek","contextual_glosses":[{"applicability":"Genç erkekten doğal ve tek sözcüklü biçimde söz edilen genel bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Genç erkek anlamını doğal bir kişi adıyla eksiksiz korur."},"facet_ids":["F001"],"text":"delikanlı","usage_role":"general"}],"definition":"Genç yaştaki erkek, başka bir deyişle delikanlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yalın biçim genç yaştaki bir erkeği adlandırır."}],"identity_rationale":"Kaynak ifadesi yalın biçimi doğrudan genç erkek anlamında verir. Dal çerçevesi bu tek tanıklığı varlıklılık veya sol yön anlamlarına taşımadan bağımsız bir insan nitelemesi olarak doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"genç erkek, delikanlı"}],"lexicalization_note":"Tanım yalnızca yalın biçimin genç erkek anlamını verir ve başka yapılara ya da eş biçimli dallara genişletilmez.","neighbor_coverage_note":"Bütün gençlik ve kişi nitelemesi adayları incelendi; genel gençlik dalı ile ek canlılık ve beceri taşıyan genç erkek dalı en yararlı sınırları sağladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yalnızca genç erkeği adlandırır; komşu dal gençliği insan dışındaki yenilik, tazelik ve yakın zaman anlamlarına da genişletir.","focus_only":"Doğrudan genç bir erkek kişiyi adlandırır.","gloss":"genç ve yeni olma","neighbor_only":"Gençlik yanında yenilik, tazelik ve yakın zamanda ortaya çıkma niteliklerini de kapsar.","neighbor_ref":"root_000299/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir erkeğin genç yaşta bulunmasını anlatabilir."},{"boundary_match":"partial","distinction":"Bu dal yaş ve cinsiyetle sınırlıdır; komşu dal genç erkeğe canlılık, kavrayış ve beceri gibi ayırt edici özellikler ekler.","focus_only":"Genç erkek olmak dışında bir davranış veya beceri koşulu taşımaz.","gloss":"canlı ve becerikli genç erkek","neighbor_only":"Canlı, kavrayışlı, becerikli ve neşeli olma gibi ek nitelikler gerektirir.","neighbor_ref":"root_001007/B013","relation_type":"near_synonym","shared_zone":"İki dal da genç yaştaki erkek kişiyi adlandırır."}],"source_phrase_ar":"اليسار: الفتى (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, yalın söz biçimini doğrudan genç yaştaki erkek anlamında kaydeder."}],"source_summary":"Genç erkek anlamı tek kaynak tanıklığıyla verilir ve başka bir yaş, yön veya varlıklılık anlamıyla desteklenmez.","sources":["MQ"],"what_is_ar":"يدخل فيه اليسار بمعنى الفتى كما أفرده ابن فارس.","what_is_not_ar":"ليس هو اليسار بمعنى الغنى ولا اليسار خلاف اليمين."},"support_links":[]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000516/B004","candidate_links":[{"candidate_id":"cand_91760c6e0245cb1a5c7b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_03ddeb72df9217afd5db","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Mention running on tongues supplies the network through which recognition circulates.","root":"ذ ك ر","source_ref":"94:4","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000516","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_0d9efaf938fb2d05a9df"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000516/B007","candidate_links":[{"candidate_id":"cand_91760c6e0245cb1a5c7b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_03ddeb72df9217afd5db","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Repute and honor supply the social capital created by that circulation.","root":"ذ ك ر","source_ref":"94:4","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000516","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_0d9efaf938fb2d05a9df"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000532/B002","candidate_links":[{"candidate_id":"cand_c35a42b66179a9a0fe49","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1fb5c1669c976fb6a6fa","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Repair, nurture, and completion supply the process by which capacity is cultivated.","root":"ر ب ب","source_ref":"94:8","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000532","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6c212d76b34d20643073"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000532/B010","candidate_links":[{"candidate_id":"cand_3ad3cf6ee2a8ca8e0907","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_5e65c70f5a5abe634867","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The container that gathers lots supplies coordination of the distributive process.","root":"ر ب ب","source_ref":"94:8","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000532","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1873718b8c21ce9368fe"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000537/B005","candidate_links":[{"candidate_id":"cand_c35a42b66179a9a0fe49","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1fb5c1669c976fb6a6fa","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant mapped branch of feeding and growth keeps literal increase live within the split inventory.","root":"ر ب ب","source_ref":"94:8","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000537","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6c212d76b34d20643073"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000575/B001","candidate_links":[{"candidate_id":"cand_c35a42b66179a9a0fe49","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1fb5c1669c976fb6a6fa","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Desire directed toward or away supplies the vector that channels available capacity.","root":"ر غ ب","source_ref":"94:8","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000575","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6c212d76b34d20643073"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000575/B002","candidate_links":[{"candidate_id":"cand_c35a42b66179a9a0fe49","lane":"macro"},{"candidate_id":"cand_e3a605033c69259b9c39","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1fb5c1669c976fb6a6fa","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Breadth and spatial extension supply room for that directed growth.","root":"ر غ ب","source_ref":"94:8","source_word_indices":["3"]},{"hft_ref":"hft_ed98aec2b799ad797ade","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A wide cavity or spatial extension supplies the resulting breadth.","root":"ر غ ب","source_ref":"94:8","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000575","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6c212d76b34d20643073","sup_72e6bfb86acfe010819b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000582/B005","candidate_links":[{"candidate_id":"cand_91760c6e0245cb1a5c7b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_03ddeb72df9217afd5db","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Broadcasting news supplies outward propagation rather than merely vertical elevation.","root":"ر ف ع","source_ref":"94:4","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000582","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_0d9efaf938fb2d05a9df"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000654/B001","candidate_links":[{"candidate_id":"cand_721defe88f0aea4818cf","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2ebcc1fb80bced30b438","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant split branch of inclination and turning supplies reorientation as a way of changing the load relation.","root":"و ز ر","source_ref":"94:2","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000654","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d0330e40fa27788e3b3a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000784/B001","candidate_links":[{"candidate_id":"cand_88daf543d5245fdd9fbb","lane":"macro"},{"candidate_id":"cand_fff4c49aac17b6bd9a86","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d709789143444cbc32cd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Opening and clarification supply an expansion operation rather than a later replacement event.","root":"ش ر ح","source_ref":"94:1","source_word_indices":["2"]},{"hft_ref":"hft_dbf3c140ce6570bbebb8","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Opening and clarification supply the first expansion in the sequence.","root":"ش ر ح","source_ref":"94:1","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000784","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7e541fc59ed5ee13f640","sup_896a8d3e750e18d50778"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000784/B002","candidate_links":[{"candidate_id":"cand_e3a605033c69259b9c39","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ed98aec2b799ad797ade","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Spreading and cutting flesh supply a deliberately material image of making internal room.","root":"ش ر ح","source_ref":"94:1","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000784","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_72e6bfb86acfe010819b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000849/B001","candidate_links":[{"candidate_id":"cand_e3a605033c69259b9c39","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ed98aec2b799ad797ade","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The bodily chest supplies the bounded container in which expansion is imagined.","root":"ص د ر","source_ref":"94:1","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000849","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_72e6bfb86acfe010819b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000849/B004","candidate_links":[{"candidate_id":"cand_88daf543d5245fdd9fbb","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d709789143444cbc32cd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The source from which actions issue locates that expansion at the point where agency begins.","root":"ص د ر","source_ref":"94:1","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000849","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_896a8d3e750e18d50778"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000970/B002","candidate_links":[{"candidate_id":"cand_41d8b7037f657ffdd2c4","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6a1f99b9bffc2d9b457d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The back supplies the load-bearing surface on which strain and relief can coexist.","root":"ظ ه ر","source_ref":"94:3","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000970","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_662e2b62efd288c9e8cd"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000970/B018","candidate_links":[{"candidate_id":"cand_721defe88f0aea4818cf","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2ebcc1fb80bced30b438","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Turning a matter back-to-belly supplies a full change of aspect without changing the underlying matter.","root":"ظ ه ر","source_ref":"94:3","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000970","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d0330e40fa27788e3b3a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001147/B001","candidate_links":[{"candidate_id":"cand_1698ea31025eaddfffc0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fe28b4fa0238f15dfae6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Vacancy after occupation supplies the release of capacity.","root":"ف ر غ","source_ref":"94:7","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001147","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_92f5662c2e206751599f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001147/B002","candidate_links":[{"candidate_id":"cand_e3a605033c69259b9c39","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ed98aec2b799ad797ade","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Pouring out and emptying a vessel supplies vacant volume after prior occupation.","root":"ف ر غ","source_ref":"94:7","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001147","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_72e6bfb86acfe010819b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001507/B001","candidate_links":[{"candidate_id":"cand_1698ea31025eaddfffc0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fe28b4fa0238f15dfae6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Setting something upright and conspicuous supplies renewed directed engagement.","root":"ن ص ب","source_ref":"94:7","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001507","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_92f5662c2e206751599f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001507/B004","candidate_links":[{"candidate_id":"cand_1698ea31025eaddfffc0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fe28b4fa0238f15dfae6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Exhausting toil keeps effort inside the semantic field that follows ease.","root":"ن ص ب","source_ref":"94:7","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001507","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_92f5662c2e206751599f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001543/B004","candidate_links":[{"candidate_id":"cand_fff4c49aac17b6bd9a86","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_dbf3c140ce6570bbebb8","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Reopening after closure supplies recurrence and reversibility rather than a one-time transition.","root":"ن ق ض","source_ref":"94:3","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001543","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7e541fc59ed5ee13f640"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001543/B005","candidate_links":[{"candidate_id":"cand_41d8b7037f657ffdd2c4","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6a1f99b9bffc2d9b457d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Creaking joints or back under weight supplies the observable failure signal of excessive loading.","root":"ن ق ض","source_ref":"94:3","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001543","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_662e2b62efd288c9e8cd"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001643/B002","candidate_links":[{"candidate_id":"cand_41d8b7037f657ffdd2c4","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6a1f99b9bffc2d9b457d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The heavy burden supplies the force whose placement matters.","root":"و ز ر","source_ref":"94:2","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001643","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_662e2b62efd288c9e8cd"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001657/B001","candidate_links":[{"candidate_id":"cand_41d8b7037f657ffdd2c4","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6a1f99b9bffc2d9b457d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Putting something into a lower or settled position supplies the load-transfer operation.","root":"و ض ع","source_ref":"94:2","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001657","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_662e2b62efd288c9e8cd"]}],"candidate_inventory":[{"anchor_refs":["94:1","94:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:6","branch_refs":["root_000784/B001","root_000849/B004","root_001694/B001"],"candidate_id":"cand_88daf543d5245fdd9fbb","commentary_obligation":"review","hft_ref":"hft_d709789143444cbc32cd","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_opened_inner_capacity","source_type":"hft","support_ids":["sup_896a8d3e750e18d50778"],"title":"delta_opened_inner_capacity","trust":"legacy_unbound"},{"anchor_refs":["94:2","94:3","94:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:6","branch_refs":["root_000970/B002","root_001012/B001","root_001543/B005","root_001643/B002","root_001657/B001","root_001694/B005"],"candidate_id":"cand_41d8b7037f657ffdd2c4","commentary_obligation":"review","hft_ref":"hft_6a1f99b9bffc2d9b457d","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_load_reconfiguration","source_type":"hft","support_ids":["sup_662e2b62efd288c9e8cd"],"title":"delta_load_reconfiguration","trust":"legacy_unbound"},{"anchor_refs":["94:1","94:3","94:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:6","branch_refs":["root_000784/B001","root_001543/B004","root_001694/B001"],"candidate_id":"cand_fff4c49aac17b6bd9a86","commentary_obligation":"review","hft_ref":"hft_dbf3c140ce6570bbebb8","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_recurrent_reopening","source_type":"hft","support_ids":["sup_7e541fc59ed5ee13f640"],"title":"delta_recurrent_reopening","trust":"legacy_unbound"},{"anchor_refs":["94:4","94:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:6","branch_refs":["root_000516/B004","root_000516/B007","root_000582/B005","root_001694/B003"],"candidate_id":"cand_91760c6e0245cb1a5c7b","commentary_obligation":"review","hft_ref":"hft_03ddeb72df9217afd5db","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_socially_distributed_ease","source_type":"hft","support_ids":["sup_0d9efaf938fb2d05a9df"],"title":"delta_socially_distributed_ease","trust":"legacy_unbound"},{"anchor_refs":["94:5","94:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:6","branch_refs":["root_001012/B001","root_001694/B001"],"candidate_id":"cand_732520c40bb078782bbb","commentary_obligation":"review","hft_ref":"hft_b760334474ddd2067597","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_iterated_openings","source_type":"hft","support_ids":["sup_5e5357ab92cddc5e2bf8"],"title":"delta_iterated_openings","trust":"legacy_unbound"},{"anchor_refs":["94:6","94:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:6","branch_refs":["root_001147/B001","root_001507/B001","root_001507/B004","root_001694/B001"],"candidate_id":"cand_1698ea31025eaddfffc0","commentary_obligation":"review","hft_ref":"hft_fe28b4fa0238f15dfae6","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_released_capacity_for_exertion","source_type":"hft","support_ids":["sup_92f5662c2e206751599f"],"title":"delta_released_capacity_for_exertion","trust":"legacy_unbound"},{"anchor_refs":["94:6","94:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:6","branch_refs":["root_000532/B002","root_000537/B005","root_000575/B001","root_000575/B002","root_001694/B003"],"candidate_id":"cand_c35a42b66179a9a0fe49","commentary_obligation":"review","hft_ref":"hft_1fb5c1669c976fb6a6fa","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_oriented_cultivable_growth","source_type":"hft","support_ids":["sup_6c212d76b34d20643073"],"title":"delta_oriented_cultivable_growth","trust":"legacy_unbound"},{"anchor_refs":["94:1","94:6","94:7","94:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:6","branch_refs":["root_000575/B002","root_000784/B002","root_000849/B001","root_001147/B002","root_001694/B001"],"candidate_id":"cand_e3a605033c69259b9c39","commentary_obligation":"review","hft_ref":"hft_ed98aec2b799ad797ade","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_free_volume","source_type":"hft","support_ids":["sup_72e6bfb86acfe010819b"],"title":"outlier_free_volume","trust":"legacy_unbound"},{"anchor_refs":["94:2","94:3","94:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:6","branch_refs":["root_000654/B001","root_000970/B018","root_001012/B005","root_001694/B004"],"candidate_id":"cand_721defe88f0aea4818cf","commentary_obligation":"review","hft_ref":"hft_2ebcc1fb80bced30b438","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_lateral_reorientation","source_type":"hft","support_ids":["sup_d0330e40fa27788e3b3a"],"title":"outlier_lateral_reorientation","trust":"legacy_unbound"},{"anchor_refs":["94:6","94:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:6","branch_refs":["root_000532/B010","root_001012/B002","root_001694/B007"],"candidate_id":"cand_3ad3cf6ee2a8ca8e0907","commentary_obligation":"review","hft_ref":"hft_5e65c70f5a5abe634867","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_apportioned_ease","source_type":"hft","support_ids":["sup_1873718b8c21ce9368fe"],"title":"outlier_apportioned_ease","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_80e6e08c460286a34ece","connection_ref":"conn_0c52cc4f89cbe52d5761","note":"The immediate first occurrence makes the second declaration a deliberate repetition within the same release sequence.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_b8633d088794e359de00","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"94:5","source_note":"Exact repetition makes the relation a continuing pattern beyond the prior sequence.","source_row_role":"ranked_review","source_target_component_ref":"94:6","source_target_components":["94:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"94:6"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"94:5","source_target_components":["94:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"94:5","target_evidence":{"arabic_uthmani":"فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا","ayah_ref":"94:5"},"target_ref":"94:5"},{"connection_evidence_ref":"conn_ev_9cca7b2d38804bd1ca1b","connection_ref":"conn_27d1765f8be45e151416","note":"The following command fixes the focus's ease as readiness for renewed exertion, not final rest.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_9a7d6fd18359e9390f7e","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"94:7","source_note":"Repetition of ease with hardship immediately precedes the command.","source_row_role":"ranked_review","source_target_component_ref":"94:6","source_target_components":["94:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"94:6"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"94:7","source_target_components":["94:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"94:7","target_evidence":{"arabic_uthmani":"فَإِذَا فَرَغْتَ فَٱنصَبْ","ayah_ref":"94:7"},"target_ref":"94:7"},{"connection_evidence_ref":"conn_ev_29c0b06f41c7e853b184","connection_ref":"conn_fb9bdf8968071e8dac67","note":"The removal in the preceding sequence grounds the focus in a concrete release from burden.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_7e808b6a73a6fd765c8d","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"94:2","source_note":"Repetition of hardship and ease confirms the immediate relief frame.","source_row_role":"ranked_review","source_target_component_ref":"94:6","source_target_components":["94:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"94:6"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"94:2","source_target_components":["94:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"94:2","target_evidence":{"arabic_uthmani":"وَوَضَعْنَا عَنكَ وِزْرَكَ","ayah_ref":"94:2"},"target_ref":"94:2"},{"connection_evidence_ref":"conn_ev_3e137465e5f7e7201e2c","connection_ref":"conn_515f8543e1f536b4e059","note":"The preceding elevation completes the local sequence that the repeated declaration generalizes.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_55b6847f121552803d2d","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"94:4","source_note":"يعيد اقتران العسر باليسر للتثبيت، لكنه مكرر بعد 94:5.","source_row_role":"ranked_review","source_target_component_ref":"94:6","source_target_components":["94:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"94:6"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"94:4","source_target_components":["94:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"94:4","target_evidence":{"arabic_uthmani":"وَرَفَعْنَا لَكَ ذِكْرَكَ","ayah_ref":"94:4"},"target_ref":"94:4"},{"connection_evidence_ref":"conn_ev_bfdc1e017ef593ad21d1","connection_ref":"conn_11ff746096dc5972a493","note":"Names the burden immediately before the focus and therefore anchors its local pressure-and-release arc.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_13078f88e8593c29e1a8","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"94:3","source_note":"Repeats the hardship-and-relief continuation already supplied by 94:5.","source_row_role":"ranked_review","source_target_component_ref":"94:6","source_target_components":["94:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"94:6"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"94:3","source_target_components":["94:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"94:3","target_evidence":{"arabic_uthmani":"ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ","ayah_ref":"94:3"},"target_ref":"94:3"},{"connection_evidence_ref":"conn_ev_1e19e12f72740bb2841c","connection_ref":"conn_1c39149796efbe32439a","note":"The opening expansion supplies the first local movement that culminates in the repeated declaration.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_363bdf47e051f9928179","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"94:1","source_note":"Reiterates the immediate ease frame; redundant but integral surah context.","source_row_role":"ranked_review","source_target_component_ref":"94:6","source_target_components":["94:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"94:6"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"94:1","source_target_components":["94:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"94:1","target_evidence":{"arabic_uthmani":"أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ","ayah_ref":"94:1"},"target_ref":"94:1"},{"connection_evidence_ref":"conn_ev_d8635720bb9a6dd21d74","connection_ref":"conn_d85c0f0fa1c49025b6c3","note":"The final orientation confirms that the local sequence leads into continued directed action.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_43178d17d23e6bf71162","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"94:8","source_note":"Repeats the immediate hardship-ease premise and adds little beyond 94:5.","source_row_role":"ranked_review","source_target_component_ref":"94:6","source_target_components":["94:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"94:6"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"94:8","source_target_components":["94:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"94:8","target_evidence":{"arabic_uthmani":"وَإِلَىٰ رَبِّكَ فَٱرْغَب","ayah_ref":"94:8"},"target_ref":"94:8"}],"focus":{"arabic_uthmani":"إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"94:6:1:1","qac_word_ref":"94:6:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"مَع2","morph_features":"STEM|POS:P|LEM:maE2","morpheme_role":"STEM","pos":"P","qac_ref":"94:6:2:1","qac_word_ref":"94:6:2","root_ar":"","surface_ar":"مَعَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"94:6:3:1","qac_word_ref":"94:6:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","root_ar":"ع س ر","surface_ar":"عُسْرِ"},{"lemma_ar":"يُسْر","morph_features":"STEM|POS:N|LEM:yusor|ROOT:ysr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:4:1","qac_word_ref":"94:6:4","root_ar":"ي س ر","surface_ar":"يُسْرًا"}],"word_analysis_qac_refs":[["94:6:1:1"],["94:6:2:1"],["94:6:3:1","94:6:3:2"],["94:6:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["94:6:1","94:6:2","94:6:3","94:6:4"]},"focus_surface_evidence":{"arabic_uthmani":"إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"94:6:1:1","qac_word_ref":"94:6:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"مَع2","morph_features":"STEM|POS:P|LEM:maE2","morpheme_role":"STEM","pos":"P","qac_ref":"94:6:2:1","qac_word_ref":"94:6:2","root_ar":"","surface_ar":"مَعَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"94:6:3:1","qac_word_ref":"94:6:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"عُسْر","morph_features":"STEM|POS:N|LEM:Eusor|ROOT:Esr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:3:2","qac_word_ref":"94:6:3","root_ar":"ع س ر","surface_ar":"عُسْرِ"},{"lemma_ar":"يُسْر","morph_features":"STEM|POS:N|LEM:yusor|ROOT:ysr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:6:4:1","qac_word_ref":"94:6:4","root_ar":"ي س ر","surface_ar":"يُسْرًا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["94:6:1:1"],["94:6:2:1"],["94:6:3:1","94:6:3:2"],["94:6:4:1"]],"word_analysis_refs":["94:6:1","94:6:2","94:6:3","94:6:4"],"word_rows":[{"analysis_record_ref":"94:6:1","analytic_gloss_range_en":"emphatic particle governing a nominal assertion; here it restarts the repeated hardship-ease clause without the prior connective","analytic_root_gloss_range_en":null,"qac_refs":["94:6:1:1"],"root":{},"surface":{"arabic":"إِنَّ","transliteration":"inna"}},{"analysis_record_ref":"94:6:2","analytic_gloss_range_en":"with, alongside, or in company with; locally a fronted circumstantial predicate of accompaniment and simultaneity","analytic_root_gloss_range_en":"the tagged root has unrelated lexical branches such as roar, heat, haste, and unstable affiliation, but the local common word is grammaticalized as an accompaniment operator rather than activating those branches","qac_refs":["94:6:2:1"],"root":{"arabic":"م ع ع","transliteration":"m-ʿ-ʿ"},"surface":{"arabic":"مَعَ","transliteration":"maʿa"}},{"analysis_record_ref":"94:6:3","analytic_gloss_range_en":"the definite, known hardship or constricted condition, governed inside the accompaniment frame rather than asserted as the subject","analytic_root_gloss_range_en":"difficulty, severity, straitness, insolvency, difficult birth, eschatological severity, and other remote branches; locally the abstract hardship/constriction branch is selected","qac_refs":["94:6:3:1","94:6:3:2"],"root":{"arabic":"ع س ر","transliteration":"ʿ-s-r"},"surface":{"arabic":"ٱلْعُسْرِ","transliteration":"al-ʿusri"}},{"analysis_record_ref":"94:6:4","analytic_gloss_range_en":"indefinite ease, facility, relief, or workable capacity; locally the delayed subject asserted with hardship","analytic_root_gloss_range_en":"ease, ready opening, facilitation, prosperity, affordability, slightness, left-side meanings, pliant movement, livestock increase, gambling lots, and remote proper-name or mark branches; locally the legitimate ease/facility branch is selected","qac_refs":["94:6:4:1"],"root":{"arabic":"ي س ر","transliteration":"y-s-r"},"surface":{"arabic":"يُسْرًۭا","transliteration":"yusran"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":8,"missing_anchor_refs":[],"supplied_unique_anchor_count":8},"assigned_record_count":10,"assigned_records":[{"anchor_refs":["94:1","94:6"],"branch_refs":["root_000784/B001","root_000849/B004","root_001694/B001"],"candidate_id":"cand_88daf543d5245fdd9fbb","evidence_scope":"declared_pericope","hft_ref":"hft_d709789143444cbc32cd","item_id":"delta_opened_inner_capacity","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_opened_inner_capacity","support_id":"sup_896a8d3e750e18d50778"},{"anchor_refs":["94:2","94:3","94:6"],"branch_refs":["root_000970/B002","root_001012/B001","root_001543/B005","root_001643/B002","root_001657/B001","root_001694/B005"],"candidate_id":"cand_41d8b7037f657ffdd2c4","evidence_scope":"declared_pericope","hft_ref":"hft_6a1f99b9bffc2d9b457d","item_id":"delta_load_reconfiguration","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_load_reconfiguration","support_id":"sup_662e2b62efd288c9e8cd"},{"anchor_refs":["94:1","94:3","94:6"],"branch_refs":["root_000784/B001","root_001543/B004","root_001694/B001"],"candidate_id":"cand_fff4c49aac17b6bd9a86","evidence_scope":"declared_pericope","hft_ref":"hft_dbf3c140ce6570bbebb8","item_id":"delta_recurrent_reopening","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_recurrent_reopening","support_id":"sup_7e541fc59ed5ee13f640"},{"anchor_refs":["94:4","94:6"],"branch_refs":["root_000516/B004","root_000516/B007","root_000582/B005","root_001694/B003"],"candidate_id":"cand_91760c6e0245cb1a5c7b","evidence_scope":"declared_pericope","hft_ref":"hft_03ddeb72df9217afd5db","item_id":"delta_socially_distributed_ease","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_socially_distributed_ease","support_id":"sup_0d9efaf938fb2d05a9df"},{"anchor_refs":["94:5","94:6"],"branch_refs":["root_001012/B001","root_001694/B001"],"candidate_id":"cand_732520c40bb078782bbb","evidence_scope":"declared_pericope","hft_ref":"hft_b760334474ddd2067597","item_id":"delta_iterated_openings","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_iterated_openings","support_id":"sup_5e5357ab92cddc5e2bf8"},{"anchor_refs":["94:6","94:7"],"branch_refs":["root_001147/B001","root_001507/B001","root_001507/B004","root_001694/B001"],"candidate_id":"cand_1698ea31025eaddfffc0","evidence_scope":"declared_pericope","hft_ref":"hft_fe28b4fa0238f15dfae6","item_id":"delta_released_capacity_for_exertion","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_released_capacity_for_exertion","support_id":"sup_92f5662c2e206751599f"},{"anchor_refs":["94:6","94:8"],"branch_refs":["root_000532/B002","root_000537/B005","root_000575/B001","root_000575/B002","root_001694/B003"],"candidate_id":"cand_c35a42b66179a9a0fe49","evidence_scope":"declared_pericope","hft_ref":"hft_1fb5c1669c976fb6a6fa","item_id":"delta_oriented_cultivable_growth","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_oriented_cultivable_growth","support_id":"sup_6c212d76b34d20643073"},{"anchor_refs":["94:1","94:6","94:7","94:8"],"branch_refs":["root_000575/B002","root_000784/B002","root_000849/B001","root_001147/B002","root_001694/B001"],"candidate_id":"cand_e3a605033c69259b9c39","evidence_scope":"declared_pericope","hft_ref":"hft_ed98aec2b799ad797ade","item_id":"outlier_free_volume","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_free_volume","support_id":"sup_72e6bfb86acfe010819b"},{"anchor_refs":["94:2","94:3","94:6"],"branch_refs":["root_000654/B001","root_000970/B018","root_001012/B005","root_001694/B004"],"candidate_id":"cand_721defe88f0aea4818cf","evidence_scope":"declared_pericope","hft_ref":"hft_2ebcc1fb80bced30b438","item_id":"outlier_lateral_reorientation","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_lateral_reorientation","support_id":"sup_d0330e40fa27788e3b3a"},{"anchor_refs":["94:6","94:8"],"branch_refs":["root_000532/B010","root_001012/B002","root_001694/B007"],"candidate_id":"cand_3ad3cf6ee2a8ca8e0907","evidence_scope":"declared_pericope","hft_ref":"hft_5e65c70f5a5abe634867","item_id":"outlier_apportioned_ease","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_apportioned_ease","support_id":"sup_1873718b8c21ce9368fe"}],"diagnostics":[],"lane_counts":{"global":9,"macro":10,"micro":4},"packet_summary":{"ayah_count":8,"focus_ref":"94:6","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"و ز ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001643","furuq_root_norm":"و ز ر","furuq_source_root_norm":"و ز ر","is_dominant":true,"target_occurrences":24,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000654","furuq_root_norm":"ز و ر","furuq_source_root_norm":"ز و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["94:1","94:2","94:3","94:4","94:5","94:6","94:7","94:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"94:6","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"94:6","lane":"macro","linguistic_source_ref":"94:6","surface_ref":"94:6","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"94:6","target_tokens":[["Gerçekten",["94:6:1"]],["zorluğun",["94:6:3"]],["yanında",["94:6:2","94:6:3"]],["bir",["94:6:4"]],["kolaylık",["94:6:4"]],["vardır",["94:6:1","94:6:4"]]],"text":"Gerçekten zorluğun yanında bir kolaylık vardır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":10,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":8,"id":"s094-p01-001-008","label":"Whole surah","number":1,"refs":["94:1","94:2","94:3","94:4","94:5","94:6","94:7","94:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"94:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"94:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["94:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"94:0"}],"support_registry":[{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ","ayah_ref":"94:1"},{"arabic_uthmani":"إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا","ayah_ref":"94:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000784/B001","root_000849/B004","root_001694/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001694","role":"Ready opening anchors the changed reading in the focus word for ease.","root":"ي س ر","source_ref":"94:6","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000784","role":"Opening and clarification supply an expansion operation rather than a later replacement event.","root":"ش ر ح","source_ref":"94:1","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000849","role":"The source from which actions issue locates that expansion at the point where agency begins.","root":"ص د ر","source_ref":"94:1","source_word_indices":["4"]}],"changed_reading":{"after":"Ease can be an internally opened capacity for action that accompanies an externally hard circumstance.","before":"Ease is an external circumstance that arrives alongside hardship."},"confidence":"strong","mechanism":"Opening at the bodily and agentive source turns abstract ease into expanded working capacity inside the person who still occupies hardship.","model_id":"delta_opened_inner_capacity","reader_inference":"The packet supplies opening and an origin of action; I infer that opening creates room to act within hardship. A live alternative is that the opening is explanatory or affective without being the mechanism of ease.","status":"strengthened","structural_cues":["94:1 places an opening at the addressee's chest before 94:6 predicates ease with hardship."],"trigger_roots":["ش ر ح","ص د ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_opened_inner_capacity","source_type":"hft","support_id":"sup_896a8d3e750e18d50778","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَوَضَعْنَا عَنكَ وِزْرَكَ","ayah_ref":"94:2"},{"arabic_uthmani":"ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ","ayah_ref":"94:3"},{"arabic_uthmani":"إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا","ayah_ref":"94:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000970/B002","root_001012/B001","root_001543/B005","root_001643/B002","root_001657/B001","root_001694/B005"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001012","role":"Difficulty and severity anchor the still-demanding condition after the load relation changes.","root":"ع س ر","source_ref":"94:6","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_001694","role":"Pliant movement supplies the regained mobility produced by better load distribution.","root":"ي س ر","source_ref":"94:6","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001657","role":"Putting something into a lower or settled position supplies the load-transfer operation.","root":"و ض ع","source_ref":"94:2","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001643","role":"The heavy burden supplies the force whose placement matters.","root":"و ز ر","source_ref":"94:2","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_001543","role":"Creaking joints or back under weight supplies the observable failure signal of excessive loading.","root":"ن ق ض","source_ref":"94:3","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000970","role":"The back supplies the load-bearing surface on which strain and relief can coexist.","root":"ظ ه ر","source_ref":"94:3","source_word_indices":["3"]}],"changed_reading":{"after":"Ease is a changed load-bearing relation—lowering, support, and mobility—that can operate while the hard task remains.","before":"Ease means that the burden or hard task disappears."},"confidence":"strong","mechanism":"The context supplies a mechanical chain of lowering a heavy load from a back that audibly strains; ease becomes altered load placement and recovered compliance while the demanding terrain can remain.","model_id":"delta_load_reconfiguration","reader_inference":"The packet supplies lowering, weight, a back, and its creak; I infer the causal arrow from redistributed force to renewed pliancy. The live alternative is a purely moral metaphor in which no mechanical model is intended.","status":"new","structural_cues":["94:2-3 sequences lowering, burden, creaking, and back as a compact load-bearing scene."],"trigger_roots":["و ض ع","و ز ر","ن ق ض","ظ ه ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_load_reconfiguration","source_type":"hft","support_id":"sup_662e2b62efd288c9e8cd","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ","ayah_ref":"94:1"},{"arabic_uthmani":"ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ","ayah_ref":"94:3"},{"arabic_uthmani":"إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا","ayah_ref":"94:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000784/B001","root_001543/B004","root_001694/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001694","role":"Ready opening anchors the recurrent process in the focus word.","root":"ي س ر","source_ref":"94:6","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000784","role":"Opening and clarification supply the first expansion in the sequence.","root":"ش ر ح","source_ref":"94:1","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001543","role":"Reopening after closure supplies recurrence and reversibility rather than a one-time transition.","root":"ن ق ض","source_ref":"94:3","source_word_indices":["2"]}],"changed_reading":{"after":"Ease is the repeated recoverability of an opening within a condition that can tighten again.","before":"Ease is one decisive transition out of hardship."},"confidence":"medium","mechanism":"Two distinct opening images make ease dynamic: an initial expansion can be followed by closure or strain and then by reopening, so ease is recoverable rather than a single irreversible switch.","model_id":"delta_recurrent_reopening","reader_inference":"The packet supplies opening and reopening after closure; I infer a cycle in which access can close and be recovered. The alternative is that the two branches describe unrelated actions and only jointly reinforce a broad opening motif.","status":"revised","structural_cues":["The opening cue in 94:1 and reopening cue in 94:3 precede the doubled hardship-ease statement."],"trigger_roots":["ش ر ح","ن ق ض"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_recurrent_reopening","source_type":"hft","support_id":"sup_7e541fc59ed5ee13f640","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَرَفَعْنَا لَكَ ذِكْرَكَ","ayah_ref":"94:4"},{"arabic_uthmani":"إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا","ayah_ref":"94:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000516/B004","root_000516/B007","root_000582/B005","root_001694/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001694","role":"Expanded means anchor social standing as a possible form of usable ease.","root":"ي س ر","source_ref":"94:6","source_word_indices":["4"]},{"branch_id":"B005","mapped_root_id":"root_000582","role":"Broadcasting news supplies outward propagation rather than merely vertical elevation.","root":"ر ف ع","source_ref":"94:4","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000516","role":"Mention running on tongues supplies the network through which recognition circulates.","root":"ذ ك ر","source_ref":"94:4","source_word_indices":["3"]},{"branch_id":"B007","mapped_root_id":"root_000516","role":"Repute and honor supply the social capital created by that circulation.","root":"ذ ك ر","source_ref":"94:4","source_word_indices":["3"]}],"changed_reading":{"after":"Ease may also be socially distributed capacity: a name carried, heard, and supported while personal hardship remains.","before":"Ease is only an inward feeling or a reduction of personal pain."},"confidence":"medium","mechanism":"Raising and circulating mention activate a social channel of ease: recognition, audibility, and standing can increase the range of action even when private difficulty persists.","model_id":"delta_socially_distributed_ease","reader_inference":"The packet supplies broadcast, circulating mention, and repute; I infer that these create social means that coexist with private strain. The alternative is that elevated mention is a separate benefit rather than an instance of the ease in 94:6.","status":"new","structural_cues":["94:4 places raised mention immediately before the repeated hardship-ease pair in 94:5-6."],"trigger_roots":["ر ف ع","ذ ك ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_socially_distributed_ease","source_type":"hft","support_id":"sup_0d9efaf938fb2d05a9df","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا","ayah_ref":"94:5"},{"arabic_uthmani":"إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا","ayah_ref":"94:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_001012/B001","root_001694/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001012","role":"The first occurrence supplies the recurring field of difficulty.","root":"ع س ر","source_ref":"94:5","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001694","role":"The first ease occurrence supplies one ready opening within that field.","root":"ي س ر","source_ref":"94:5","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001012","role":"The repeated hardship keeps the difficult field present rather than narrating its disappearance.","root":"ع س ر","source_ref":"94:6","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001694","role":"The repeated ease renews the opening and makes recurrence visible.","root":"ي س ر","source_ref":"94:6","source_word_indices":["4"]}],"changed_reading":{"after":"The hard field can be met by repeatedly renewed openings; ease behaves as a pattern of access, not a one-use event.","before":"The verse states one static companionship between one hardship and one ease."},"confidence":"strong","mechanism":"The adjacent re-predication turns co-presence into an iterative pattern: the same named hardship is met by a freshly asserted, indefinite opening rather than exhausted by one occurrence.","model_id":"delta_iterated_openings","reader_inference":"The packet supplies exact adjacent repetition; I infer renewed or multiple access to ease rather than a single spent instance. The materially live alternative is emphatic restatement of one proposition with no multiplicative force.","status":"strengthened","structural_cues":["94:5 and 94:6 repeat the same root pair and relational construction in adjacent ayat."],"trigger_roots":["ع س ر","ي س ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_iterated_openings","source_type":"hft","support_id":"sup_5e5357ab92cddc5e2bf8","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا","ayah_ref":"94:6"},{"arabic_uthmani":"فَإِذَا فَرَغْتَ فَٱنصَبْ","ayah_ref":"94:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_001147/B001","root_001507/B001","root_001507/B004","root_001694/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001694","role":"Readiness and opening anchor ease as newly available capacity.","root":"ي س ر","source_ref":"94:6","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001147","role":"Vacancy after occupation supplies the release of capacity.","root":"ف ر غ","source_ref":"94:7","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001507","role":"Setting something upright and conspicuous supplies renewed directed engagement.","root":"ن ص ب","source_ref":"94:7","source_word_indices":["3"]},{"branch_id":"B004","mapped_root_id":"root_001507","role":"Exhausting toil keeps effort inside the semantic field that follows ease.","root":"ن ص ب","source_ref":"94:7","source_word_indices":["3"]}],"changed_reading":{"after":"Ease is freed capacity: enough openness to stand up, choose a new task, and exert oneself again.","before":"Ease is passive rest and the endpoint of exertion."},"confidence":"strong","mechanism":"Vacancy after occupation feeds directly into standing up and exerting oneself, revising ease from terminal rest into released capacity that can be committed to another demanding act.","model_id":"delta_released_capacity_for_exertion","reader_inference":"The packet supplies post-occupation vacancy, upright setting, and toil; I infer that the opening of 94:6 enables renewed effort. The alternative is that 94:7 gives an ethical response after ease without redefining ease itself.","status":"revised","structural_cues":["94:7 follows the repeated promise with a conditional transition from becoming free to renewed exertion."],"trigger_roots":["ف ر غ","ن ص ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_released_capacity_for_exertion","source_type":"hft","support_id":"sup_92f5662c2e206751599f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا","ayah_ref":"94:6"},{"arabic_uthmani":"وَإِلَىٰ رَبِّكَ فَٱرْغَب","ayah_ref":"94:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000532/B002","root_000537/B005","root_000575/B001","root_000575/B002","root_001694/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001694","role":"Prosperity and means anchor the changed reading in an increase of usable capacity.","root":"ي س ر","source_ref":"94:6","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000532","role":"Repair, nurture, and completion supply the process by which capacity is cultivated.","root":"ر ب ب","source_ref":"94:8","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_000537","role":"The non-dominant mapped branch of feeding and growth keeps literal increase live within the split inventory.","root":"ر ب ب","source_ref":"94:8","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000575","role":"Desire directed toward or away supplies the vector that channels available capacity.","root":"ر غ ب","source_ref":"94:8","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000575","role":"Breadth and spatial extension supply room for that directed growth.","root":"ر غ ب","source_ref":"94:8","source_word_indices":["3"]}],"changed_reading":{"after":"Ease is capacity that can be nurtured, enlarged, and given direction toward its sustaining source.","before":"Ease is an undirected pleasant state granted amid hardship."},"confidence":"medium","mechanism":"Nurture, growth, spatial breadth, and directed desire turn ease into a cultivable vector: capacity increases by being oriented toward a sustaining source rather than remaining undirected comfort.","model_id":"delta_oriented_cultivable_growth","reader_inference":"The packet supplies nurture, a split-mapped growth image, breadth, and directed desire; I infer a growth vector from orientation toward a sustaining source. The alternative is that these cues prescribe devotion after relief without describing the mechanics of ease.","status":"new","structural_cues":["94:8 follows renewed exertion by specifying a destination for desire."],"trigger_roots":["ر ب ب","ر غ ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_oriented_cultivable_growth","source_type":"hft","support_id":"sup_6c212d76b34d20643073","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ","ayah_ref":"94:1"},{"arabic_uthmani":"إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا","ayah_ref":"94:6"},{"arabic_uthmani":"فَإِذَا فَرَغْتَ فَٱنصَبْ","ayah_ref":"94:7"},{"arabic_uthmani":"وَإِلَىٰ رَبِّكَ فَٱرْغَب","ayah_ref":"94:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000575/B002","root_000784/B002","root_000849/B001","root_001147/B002","root_001694/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001694","role":"Ready opening anchors free capacity in the focus word for ease.","root":"ي س ر","source_ref":"94:6","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000784","role":"Spreading and cutting flesh supply a deliberately material image of making internal room.","root":"ش ر ح","source_ref":"94:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000849","role":"The bodily chest supplies the bounded container in which expansion is imagined.","root":"ص د ر","source_ref":"94:1","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_001147","role":"Pouring out and emptying a vessel supplies vacant volume after prior occupation.","root":"ف ر غ","source_ref":"94:7","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000575","role":"A wide cavity or spatial extension supplies the resulting breadth.","root":"ر غ ب","source_ref":"94:8","source_word_indices":["3"]}],"changed_reading":{"after":"Ease can be imagined as free volume opened inside the same loaded system, permitting breath, movement, and renewed work.","before":"Ease is a separate positive event added to hardship."},"confidence":"exploratory","containment":"This is surprising because it links bodily opening, material spreading, vessel-emptying, and spatial breadth into one capacity model. It remains anchored in the focus word's ready-opening branch and the construction of coexistence, but downstream prose should present it only as a material analogy, not as a claim that the ayah denotes a literal vessel.","focus_anchor":"The yusr branch of ready opening, placed with hardship by مع, can support the image of free volume inside a still-bounded system.","outlier_id":"outlier_free_volume"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_free_volume","source_type":"hft","support_id":"sup_72e6bfb86acfe010819b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَوَضَعْنَا عَنكَ وِزْرَكَ","ayah_ref":"94:2"},{"arabic_uthmani":"ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ","ayah_ref":"94:3"},{"arabic_uthmani":"إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا","ayah_ref":"94:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000654/B001","root_000970/B018","root_001012/B005","root_001694/B004"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001012","role":"The left side and left-handedness turn hardship's root into one lateral orientation.","root":"ع س ر","source_ref":"94:6","source_word_indices":["3"]},{"branch_id":"B004","mapped_root_id":"root_001694","role":"The left side, left hand, and turning left make ease's root converge on the same lateral field.","root":"ي س ر","source_ref":"94:6","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000654","role":"The non-dominant split branch of inclination and turning supplies reorientation as a way of changing the load relation.","root":"و ز ر","source_ref":"94:2","source_word_indices":["3"]},{"branch_id":"B018","mapped_root_id":"root_000970","role":"Turning a matter back-to-belly supplies a full change of aspect without changing the underlying matter.","root":"ظ ه ر","source_ref":"94:3","source_word_indices":["3"]}],"changed_reading":{"after":"A branch-distant spatial echo lets ease appear as turning or changing aspect within the same terrain, not merely reducing its quantity.","before":"Hardship and ease are only opposite quantities on one scale."},"confidence":"exploratory","containment":"This reading is branch-distant because both focus roots unexpectedly carry left-side images and the context cue uses the non-dominant mapping of و ز ر. It remains anchored in exact supplied branches and yields a coherent orientation mechanism, but it should be rendered as a spatial echo rather than a lexical replacement for hardship and ease.","focus_anchor":"The paired focus roots both admit lateral images, allowing مع to be tested as adjacency and reorientation rather than only scalar opposition.","outlier_id":"outlier_lateral_reorientation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_lateral_reorientation","source_type":"hft","support_id":"sup_d0330e40fa27788e3b3a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا","ayah_ref":"94:6"},{"arabic_uthmani":"وَإِلَىٰ رَبِّكَ فَٱرْغَب","ayah_ref":"94:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000532/B010","root_001012/B002","root_001694/B007"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001012","role":"Straitness of means supplies the scarcity problem that requires allocation.","root":"ع س ر","source_ref":"94:6","source_word_indices":["3"]},{"branch_id":"B007","mapped_root_id":"root_001694","role":"Lots and division into shares supply allocation as a way to produce usable portions from one constrained whole.","root":"ي س ر","source_ref":"94:6","source_word_indices":["4"]},{"branch_id":"B010","mapped_root_id":"root_000532","role":"The container that gathers lots supplies coordination of the distributive process.","root":"ر ب ب","source_ref":"94:8","source_word_indices":["2"]}],"changed_reading":{"after":"Ease may arise by apportioning a constrained whole into usable shares, so better distribution accompanies scarcity without first abolishing it.","before":"Ease must mean that more total resource appears."},"confidence":"exploratory","containment":"This is surprising because it activates the lots-and-shares branch of ي س ر together with a context image that gathers lots. It remains anchored in the focus contrast between straitened and available means and offers a functional distribution mechanism, but downstream prose should qualify it as an allocative analogy, not as a gambling sense asserted for يسرا.","focus_anchor":"The material-means reading of the focus pair can be crossed with the branch in which ي س ر apportions a scarce whole into shares.","outlier_id":"outlier_apportioned_ease"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_apportioned_ease","source_type":"hft","support_id":"sup_1873718b8c21ce9368fe","trust":"legacy_unbound"}]}
</lane_packet_json>
