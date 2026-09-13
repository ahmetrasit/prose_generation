# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **92:6**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s092-regular-20260912/s092/92_6/macro.discovery.json` and modify nothing
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
  "ayah_ref": "92:6",
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
{"branch_registry":[{"boundary":"Dal bir nitelik ve durum bildirir; başkasına iyilik etme eylemini, kişiye ulaşan iyi sonucu veya kalıplaşmış özel adlandırmaları kapsamaz.","branch_kind":"bare","branch_ref":"root_000323/B001","candidate_links":[{"candidate_id":"cand_1f91fa6f782358926eb0","lane":"macro"},{"candidate_id":"cand_ba95413c78d0046d8fac","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"حُسْنَىٰ","morph_features":"STEM|POS:N|LEM:HusonaY`|ROOT:Hsn|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:6:2:3","qac_word_ref":"92:6:2","surface_ar":"حُسْنَىٰ"}],"gloss":"akla, eğilime veya duyulara göre güzel ve beğenilir olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şeyin güzel ve beğenilir olması, çirkinliğin karşıtı olan temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olumlu değerlendirme akla, kişisel eğilime veya duyulara dayanabilir; dal yalnızca görsel güzellikle sınırlı değildir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsanlar güzel diye nitelenebilir ve aynı nitelik çok yüksek derecede güzelliği belirten biçimlerle güçlendirilebilir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir insanın, işin veya başka bir şeyin güzel yerleri ve iyi nitelikleri, onun kötü yanlarının karşıtı olarak topluca anılabilir."}}],"root_ar":"ح س ن","root_id":"root_000323","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kişi, şey, görünüş ve niteliklerdeki ortak çekirdeğini, olumlu değerlendirmenin farklı dayanaklarını silmeden karşılar.","boundary_detail":"Dal bir nitelik ve durum bildirir; başkasına iyilik etme eylemini, kişiye ulaşan iyi sonucu veya kalıplaşmış özel adlandırmaları kapsamaz.","branch_image_ar":"الحسن ضد القبح","concept_gloss":"akla, eğilime veya duyulara göre güzel ve beğenilir olma","contextual_glosses":[{"applicability":"Dış görünüşün veya duyularla algılanan bir şeyin güzel oluşunun öne çıktığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Akla veya kişisel eğilime dayanan daha geniş beğenilirlik alanını tek başına açıkça göstermez.","preserves":"Duyularla algılanan güzel oluşu ve çirkinliğe karşıtlığı korur."},"facet_ids":["F001","F003"],"text":"güzellik","usage_role":"general"},{"applicability":"Bir şeyin görünüşünden çok akıl, istek veya değerlendirme bakımından olumlu bulunduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin veya bedenin somut güzelliğini ve güzelliğin çok yüksek derecesini açıkça belirtmez.","preserves":"Bir şeyin olumlu bulunması ve istenir görülmesi yönünü korur."},"facet_ids":["F001","F002"],"text":"beğenilirlik","usage_role":"explanatory"},{"applicability":"Bir kişi, iş veya şeydeki güzel yerler ile iyi niteliklerin topluca kötü yanlarla karşılaştırıldığı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çoğul güzel yerleri ve iyi nitelikleri kötü yanların karşıtı olarak eksiksiz korur."},"facet_ids":["F004"],"text":"güzel yanlar","usage_role":"contextual"}],"definition":"Bir kişinin, şeyin, görünüşün veya niteliğin; akıl, kişisel eğilim ya da duyular bakımından güzel ve beğenilir bulunması, dolayısıyla çirkinliğin ve kötü yanların karşısında yer almasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şeyin güzel ve beğenilir olması, çirkinliğin karşıtı olan temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Olumlu değerlendirme akla, kişisel eğilime veya duyulara dayanabilir; dal yalnızca görsel güzellikle sınırlı değildir."},{"facet_id":"F003","role":"specialization","statement":"İnsanlar güzel diye nitelenebilir ve aynı nitelik çok yüksek derecede güzelliği belirten biçimlerle güçlendirilebilir."},{"facet_id":"F004","role":"extension","statement":"Bir insanın, işin veya başka bir şeyin güzel yerleri ve iyi nitelikleri, onun kötü yanlarının karşıtı olarak topluca anılabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ahlaki davranış veya başkasına yarar sağlama eylemi anlamını çağrıştırır.","collision":"İyi iş yapma ve başkasına iyilik etme dalıyla karışır.","fit":"displacement","loses":"Görünüşteki güzelliği, yoğun güzelliği ve güzel yanların çirkinliğe karşıtlığını siler.","preserves":"Olumlu değerlendirme ve beğenilirlik yönünden sınırlı bir ortaklık taşır."},"text":"iyilik"}],"identity_rationale":"Dalın çirkinliğin karşıtı olan güzel ve beğenilir niteliğe ilişkin çerçevesi, kaynak söz öbeğiyle örtüşür. Bu nitelik yalnızca dış görünüşe bağlı değildir; aklın, kişisel eğilimin veya duyuların olumlu bulduğu şeyleri, kişilerdeki yoğun güzelliği ve bir kişi ya da şeydeki güzel yanları da kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"güzel ve beğenilir olma; güzellik"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"güzel olmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"güzel erkek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"güzel kadın"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"güzel kadın"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"çok güzel kadın"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"çok güzel"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"güzel yanlar ve iyi nitelikler"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bedenin güzel yeri"}],"lexicalization_note":"Dalın yalın kapsamı güzel ve beğenilir olma niteliğidir; belirli bir söz öbeğine özgü eylem veya sonuç anlamı bu kapsama taşınmamalıdır.","neighbor_coverage_note":"Bütün aday komşular karşılaştırıldı; yalnızca nitelik ile eylem ayrımını veya güzelliğin kapsam sınırını belirginleştiren üç ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeği bir varlık ya da niteliğin güzel ve beğenilir oluşudur. Komşu dalın sınırı daha geniştir; güzelleştirme ve güzel davranma gibi eylemsel kullanımları da içerdiği için her bağlamda birbirinin yerine geçmezler.","focus_only":"Bu dal, akıl, eğilim veya duyular bakımından beğenilir olmayı ve güzel yanları genel bir nitelik olarak kapsar.","gloss":"güzel oluş ve güzel davranış alanı","neighbor_only":"Komşu dal, güzel görünüş ve güzel eylemin yanında güzelleştirmeyi, güzel davranmayı ve kimi özel davranış biçimlerini de kapsar.","neighbor_ref":"root_000260/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da kişi, beden, şey veya eylemde olumlu ve güzel bulunan yönü anlatabilir."},{"boundary_match":"partial","distinction":"Niteliğin güzel olması ile bir kişinin iyi bir iş yapması aynı çekirdek değildir. İlki varlık veya nitelik değerlendirmesidir; ikincisi yapanı, yapılan işi ve kimi zaman yarar gören kişiyi içeren bir eylemdir.","focus_only":"Bu dal, kişi veya şeyde bulunan güzel ve beğenilir niteliği bildirir.","gloss":"iyi eylem ve iyilik etme","neighbor_only":"Komşu dal, bir işi iyi yapmayı, bir şeyi güzelleştirmeyi veya başkasına iyilik etmeyi bildirir.","neighbor_ref":"root_000323/B002","relation_type":"near_neighbor","shared_zone":"Güzel bir eylem olumlu değerlendirildiğinde iki dal aynı olay çevresinde buluşabilir."},{"boundary_match":"partial","distinction":"Komşu dalın kusursuzluk ve görünüş odağı, bu dalın akıl, eğilim ve duyulara yayılan genel beğenilirlik sınırından daha dardır. Görsel bağlamlarda yaklaşsalar da değerlendirme kapsamları tam örtüşmez.","focus_only":"Bu dal, görünüş dışında akla ve kişisel eğilime göre beğenilirliği de kapsar.","gloss":"kusursuz ve güzel oluş","neighbor_only":"Komşu dal, güzel oluşu özellikle kusurdan arınmışlık, süs ve yüz güzelliği çevresinde belirginleştirir.","neighbor_ref":"root_000660/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da güzel görünüşü ve bir şeyin çirkin ya da kusurlu sayılmamasını anlatır."}],"source_phrase_ar":"الحسن ضد القبح (maqayis;sihah)؛ حسن الشيء فهو حسن (ayn)؛ الحسن نعت لما حسن (tahdhib)؛ كل مبهج مرغوب فيه (mufradat)؛ مستحسن من جهة العقل ومستحسن من جهة الهوى ومستحسن من جهة الحس (mufradat)؛ رجل حسن وامرأة حسناء وحسانة (maqayis)؛ الحسان الحسن جدا (ayn)؛ المحاسن ضد المساوىء (maqayis;ayn;sihah;tahdhib)","source_summary":"Kaynaklar, temel karşıtlığı güzel ile çirkin arasında kurar; güzel olmayı kişi ve şeylere yüklenen bir nitelik olarak verir. Toplu anlatım ayrıca akla, eğilime ve duyulara göre beğenilirliği, yoğun güzelliği ve güzel yanların kötü yanlara karşıtlığını kapsar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"النعت والمصدر لما كان حسنا أو مرغوبا أو ضد القبح، ويشمل حسن الشخص والشيء والمحاسن والحسان","what_is_not_ar":"الإحسان إلى الغير، والحسنة بمعنى النعمة أو الثواب، والأعلام والمواضع المسماة بالحسن"},"support_links":["sup_1831385efe2952ea96d9","sup_cab23a87d0f55bd398de"]},{"boundary":"Dal güzel bir niteliğin kendisini değil, güzelleştiren, iyi yapan veya bir başkasına yarar sağlayan eylemi anlatır.","branch_kind":"bare","branch_ref":"root_000323/B002","candidate_links":[{"candidate_id":"cand_adb33c8ee67d98f9ab57","lane":"macro"},{"candidate_id":"cand_4ca18a4b98db24b52d22","lane":"macro"},{"candidate_id":"cand_8c19034e036d24c69fd0","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"حُسْنَىٰ","morph_features":"STEM|POS:N|LEM:HusonaY`|ROOT:Hsn|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:6:2:3","qac_word_ref":"92:6:2","surface_ar":"حُسْنَىٰ"}],"gloss":"bir şeyi güzelleştirme, işi iyi yapma veya başkasına iyilik etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kötü davranmanın karşısında yer alan iyi ve güzel eylem, dalın ortak eylemsel çekirdeğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem bir başkasına yöneldiğinde ona yarar sağlama, iyilik etme veya iyi davranma biçimini alır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eylem kişinin kendi işine yöneldiğinde işi iyi, doğru ve ustalıkla yapmayı belirtir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir şeyi daha güzel duruma getirme, iyi eylemin nesne üzerinde sonuç doğuran biçimidir."}},{"facet_id":"F005","role":"specialization","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"İyilik etme, kimi kullanımda yalnızca denk karşılığı vermekle yetinmeyip bunun üzerine çıkmayı gerektirir."}}],"root_ar":"ح س ن","root_id":"root_000323","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın nesneyi güzelleştirme, eylemi iyi yürütme ve bir başkasına yarar sağlama biçimlerini birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Dal güzel bir niteliğin kendisini değil, güzelleştiren, iyi yapan veya bir başkasına yarar sağlayan eylemi anlatır.","branch_image_ar":"الإحسان فعل حسن","concept_gloss":"bir şeyi güzelleştirme, işi iyi yapma veya başkasına iyilik etme","contextual_glosses":[{"applicability":"Eylemin başka bir kişiye yöneldiği ve ona yarar ya da karşılıksız bir fazlalık sağladığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendi işini iyi yapması ve bir nesneyi güzelleştirmesi yönlerini kapsamaz.","preserves":"Başkasına yönelme, yarar sağlama ve denk karşılığın ötesine geçme yönünü korur."},"facet_ids":["F001","F002","F005"],"text":"iyilik etmek","usage_role":"contextual"},{"applicability":"Bir kişinin yaptığı işi özenle, doğru biçimde veya ustalıkla yürüttüğü bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasına iyilik etme ve bir nesneyi daha güzel duruma getirme yönlerini dışarıda bırakır.","preserves":"Eylemin iyi ve ustalıklı biçimde yerine getirilmesi yönünü korur."},"facet_ids":["F001","F003"],"text":"işini iyi yapmak","usage_role":"contextual"},{"applicability":"Eylemin bir nesnenin görünüşünü veya niteliğini daha güzel duruma getirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşi iyi yapma ve bir başkasına yarar sağlayan iyilikte bulunma yönlerini kapsamaz.","preserves":"Bir nesnede daha güzel bir durum meydana getirme sonucunu korur."},"facet_ids":["F001","F004"],"text":"güzelleştirmek","usage_role":"contextual"}],"definition":"Bir şeyi güzelleştirmek, bir işi iyi ve özenli biçimde yapmak ya da bir başkasına yarar sağlayan bir iyilikte bulunmaktır. Başkasına yönelik biçimi, yalnızca denk bir karşılık vermenin ötesine geçen artırılmış bir iyilik içerebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kötü davranmanın karşısında yer alan iyi ve güzel eylem, dalın ortak eylemsel çekirdeğidir."},{"facet_id":"F002","role":"specialization","statement":"Eylem bir başkasına yöneldiğinde ona yarar sağlama, iyilik etme veya iyi davranma biçimini alır."},{"facet_id":"F003","role":"specialization","statement":"Eylem kişinin kendi işine yöneldiğinde işi iyi, doğru ve ustalıkla yapmayı belirtir."},{"facet_id":"F004","role":"extension","statement":"Bir şeyi daha güzel duruma getirme, iyi eylemin nesne üzerinde sonuç doğuran biçimidir."},{"facet_id":"F005","role":"specialization","statement":"İyilik etme, kimi kullanımda yalnızca denk karşılığı vermekle yetinmeyip bunun üzerine çıkmayı gerektirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Eylem yerine kişide veya şeyde bulunan durağan bir nitelik anlamını öne çıkarır.","collision":"Güzel ve beğenilir olma niteliğini anlatan dalla karışır.","fit":"displacement","loses":"Yapan kişiyi, eylemin yürütülüşünü ve iyilikten yararlanan kişiyi görünmez kılar.","preserves":"Bir nesneyi güzelleştirme sonucuyla ve iyi eylemin olumlu değerlendirilmesiyle bağlantıyı korur."},"text":"güzellik"}],"identity_rationale":"Dal çerçevesi, kaynak söz öbeğinde bulunan başkasına iyilik etme ve kişinin kendi işini iyi yapma yönlerini birlikte korur. Bir şeyi güzelleştirme, eylemi ustalıkla yürütme, kötülüğün karşısında iyi davranma ve karşılık denkliğini aşan iyilik de bu eylemsel çekirdeğin ayrı görünümleridir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir şeyi güzelleştirmek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"birine iyilik etmek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"işini iyi ve ustalıkla yapmak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"iyilik etme veya işi iyi yapma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"iyilik eden veya işini iyi yapan kimse"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sürekli iyilik eden kimse"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"güzel bulmak; beğenmek"}],"lexicalization_note":"Dal belirli bir söz öbeğine bağlı değildir; genel eylem alanı, başkasına yarar sağlama ile işi iyi ve özenli yapma yönleri ayrılarak tanımlanmalıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; iyi eylemin yardım ve güzel nitelikten ayrıldığı üç yararlı sınır karşılaştırması seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Başkasına iyilik sunma bağlamında yakın karşılık olabilirler. Ancak bu dalın işi ustalıkla yapma ve nesneyi güzelleştirme kapsamı komşuda bulunmadığından genel sınırları eş değildir.","focus_only":"Bu dal, başkasına iyilik etmenin yanında kişinin kendi işini iyi yapmasını ve bir şeyi güzelleştirmesini de kapsar.","gloss":"başkasına sunulan iyilik ve yardım","neighbor_only":"Komşu dal, özellikle başkasına sunulan yararlı iş, yardım ve iyilik üzerinde yoğunlaşır.","neighbor_ref":"root_000885/B003","relation_type":"near_synonym","shared_zone":"Bir kişinin başkasına yarar sağlayan iyi bir iş yapması iki dalın doğrudan örtüştüğü alandır."},{"boundary_match":"partial","distinction":"Ortak alanda anlamlar yaklaşır; fakat komşunun belirli çaba ve davranış örnekleri bu dalın kurucu sınırı değildir. Bu dal da nesneyi güzelleştirme ve işi ustalıkla yapma yönleriyle komşudan daha geniştir.","focus_only":"Bu dal, her tür iyi yapışı ve başkasına yarar sağlamayı, ayrıca nesneyi güzelleştirmeyi kapsar.","gloss":"güzel iş ve iyilikte bulunma","neighbor_only":"Komşu dal, güzel iş ve iyilikle birlikte cömertlikte veya savaşta çaba gösterme gibi daha belirli davranış alanlarına uzanır.","neighbor_ref":"root_000153/B003","relation_type":"near_synonym","shared_zone":"İyi bir iş yapmak ve bir başkasına yarar sunmak iki dalın ortak merkezidir."},{"boundary_match":"partial","distinction":"Bir işin yapılması ile o işin veya başka bir şeyin güzel bulunması ayrı çekirdeklerdir. Bu dal eylem ve katılımcıları, komşu dal ise nitelik ve değerlendirmeyi öne çıkarır.","focus_only":"Bu dal, yapanı ve yapılan işi içeren iyi eylemi bildirir.","gloss":"güzel ve beğenilir olma","neighbor_only":"Komşu dal, bir kişi veya şeyde bulunan güzel ve beğenilir niteliği bildirir.","neighbor_ref":"root_000323/B001","relation_type":"near_neighbor","shared_zone":"İyi yapılan bir iş, sonuçta güzel ve beğenilir diye değerlendirilebilir."}],"source_phrase_ar":"أحسنت إليه وبه (sihah)؛ وهو يحسن الشيء أي يعمله (sihah)؛ حسنت الشيء تحسينا زينته (sihah)؛ أحسن يا هذا فإنك محسان (tahdhib)؛ الإحسان ضد الإساءة (tahdhib)؛ أحسنت بفلان أي أحسنت إليه (tahdhib)؛ الإحسان يقال على وجهين الإنعام على الغير وإحسان في فعله (mufradat)؛ الإحسان فوق العدل (mufradat)","source_summary":"Toplu kaynak anlatımı eylemi iki ana yönde verir: bir başkasına yarar sağlayan iyilik ve kişinin yaptığı işi iyi yürütmesi. Bir şeyi güzelleştirme, kötülüğün karşıtı olan iyi davranış ve denk karşılığın üstüne çıkan verme de bu çerçevede yer alır.","sources":["AY","SI","TA","MU"],"what_is_ar":"الفعل الحسن والإتقان والإنعام على الغير والزيادة على العدل، وما يقابل الإساءة","what_is_not_ar":"مجرد هيئة الشيء الحسنة، والحسنة اسما للنعمة أو الثواب، والمواضع والأعلام"},"support_links":["sup_01d18329256677ad3251","sup_637938be856a819cfc5f","sup_bf1ed743df9188d14f17"]},{"boundary":"Dal, bir şeyi güzel kılan niteliği ya da iyilik etme eylemini değil, kişiye ulaşan iyi şeyi, karşılığı veya sonucu bildirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000323/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُسْنَىٰ","morph_features":"STEM|POS:N|LEM:HusonaY`|ROOT:Hsn|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:6:2:3","qac_word_ref":"92:6:2","surface_ar":"حُسْنَىٰ"}],"gloss":"kişiye ulaşan sevindirici iyilik, karşılık veya iyi sonuç","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişiye ulaşan ve onu sevindiren iyilik, iyi karşılık veya iyi sonuç, kötü şeyin ve kötü sonun karşıtıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bolluk, geniş geçim ve utkı, kişinin dünyadaki yaşamında karşılaştığı sevindirici iyi sonuçlar olarak bu dala girer."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İyi bir karşılık veya ödül, sonsuz mutluluk yurduyla örneklenen olumlu son biçimini alabilir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İki iyi sonuçtan birini bildiren kalıplaşmış kullanım, seçenekleri utkı ile kişinin inancı uğruna ölmesiyle sınırlar."}}],"root_ar":"ح س ن","root_id":"root_000323","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın dünyadaki bolluktan ödüle ve belirli iyi sonlara uzanan ortak alıcı ve sonuç yapısını birlikte karşılar.","boundary_detail":"Dal, bir şeyi güzel kılan niteliği ya da iyilik etme eylemini değil, kişiye ulaşan iyi şeyi, karşılığı veya sonucu bildirir.","branch_image_ar":"الحسنة خير يصيب","concept_gloss":"kişiye ulaşan sevindirici iyilik, karşılık veya iyi sonuç","contextual_glosses":[{"applicability":"Bir olayın sonu, utkı veya iki olumlu seçenekten biri söz konusu olduğunda doğal ve kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiye ulaşan bolluk, sevindirici iyilik ve ödül anlamlarını tek başına açıkça göstermez.","preserves":"Kötü sonun karşısındaki olumlu sonucu ve belirli iyi sonları korur."},"facet_ids":["F001","F002","F004"],"text":"iyi sonuç","usage_role":"general"},{"applicability":"İyi davranışa verilen ödülün veya olumlu sonucun vurgulandığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bolluk, geniş geçim ve utkı gibi karşılık olmak zorunda olmayan iyi şeyleri dışarıda bırakır.","preserves":"Kişiye ulaşan olumlu karşılığı ve iyi son yönünü korur."},"facet_ids":["F001","F003"],"text":"güzel karşılık","usage_role":"contextual"},{"applicability":"Kişinin yaşamında karşılaştığı geniş geçim, rahatlık ve sevindirici iyilik söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ödül, sonsuz mutluluk yurdu, utkı ve iki iyi sonuçtan biri anlamlarını kapsamaz.","preserves":"Dünyadaki sevindirici iyilik ve genişlik yönünü korur."},"facet_ids":["F001","F002"],"text":"bolluk ve esenlik","usage_role":"contextual"}],"definition":"Bir kişiyi sevindiren iyilik, bolluk, iyi karşılık veya kötü bir şeyin karşısında yer alan iyi sonuçtur. Belirli kullanımlarda sonsuz mutluluk yurdu, utkı ya da inancı uğruna ölme gibi iyi sonları gösterir; iki seçenekli kalıplaşmış kullanım ise yalnızca son iki sonucu birlikte sınırlar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişiye ulaşan ve onu sevindiren iyilik, iyi karşılık veya iyi sonuç, kötü şeyin ve kötü sonun karşıtıdır."},{"facet_id":"F002","role":"specialization","statement":"Bolluk, geniş geçim ve utkı, kişinin dünyadaki yaşamında karşılaştığı sevindirici iyi sonuçlar olarak bu dala girer."},{"facet_id":"F003","role":"specialization","statement":"İyi bir karşılık veya ödül, sonsuz mutluluk yurduyla örneklenen olumlu son biçimini alabilir."},{"facet_id":"F004","role":"source_variant","statement":"İki iyi sonuçtan birini bildiren kalıplaşmış kullanım, seçenekleri utkı ile kişinin inancı uğruna ölmesiyle sınırlar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bir kişi veya şeyde bulunan güzel niteliği öne çıkarır.","collision":"Güzel ve beğenilir olma dalıyla karışır.","fit":"displacement","loses":"Kişiye ulaşan iyiliği, karşılığı, ödülü ve olayın iyi sonucunu siler.","preserves":"Olumlu ve istenir olma yönü bakımından sınırlı bir bağlantı taşır."},"text":"güzellik"},{"category":"confusable","error_profile":{"adds":"Sonuç yerine iyiliği yapan kişinin eylemini çekirdek anlam yapar.","collision":"İyi iş yapma ve başkasına iyilik etme dalıyla karışır.","fit":"displacement","loses":"Kişinin aldığı iyiliği, ödülü ve olayın iyi sonucunu ürün olarak göstermez.","preserves":"İyilik yapan ile iyilikten yararlanan arasındaki olay bağını korur."},"text":"iyilik etme"}],"identity_rationale":"Dal çerçevesi, kaynak söz öbeğinin kişiyi sevindiren iyilik, bolluk, iyi karşılık ve iyi son anlamlarını doğru biçimde toplar. Sonsuz mutluluk yurdu, utkı ve inancı uğruna ölme belirli iyi sonuçlar olarak kalmalı; dalın tamamı yalnızca bu örneklere veya güzel bir niteliğe indirgenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kişiye ulaşan iyilik, bolluk veya ödül"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"iyi son veya en güzel karşılık; sonsuz mutluluk yurdu, utkı ya da inancı uğruna ölme"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"iki iyi sonuçtan biri: utkı ya da inancı uğruna ölme"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kötü işleri gideren iyi işler, özellikle beş günlük tapınma"}],"lexicalization_note":"Genel olarak kişiye ulaşan iyilik ve iyi sonuç bildiren tek sözcüklü biçimler ile iki iyi sonuçtan birini anlatan kalıplaşmış söz öbeği ayrı tutulmalı; bu söz öbeğinin ikili sınırı bütün dala yayılmamalıdır.","neighbor_coverage_note":"Bütün aday komşular incelendi; iyi şeyin kötülükle karşıtlığı ve nitelik ile eylemden ayrılığı en açıklayıcı üç ilişki olarak seçildi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu dal olumlu kutupta iyilik ve iyi sonucu, komşu dal olumsuz kutupta kötülük ve kötü durumu gösterir. Karşıtlık ortak değerlendirme eksenindedir; her birinin özel örnekleri bire bir eşleşmek zorunda değildir.","focus_only":"Bu dal, kişiye ulaşan sevindirici iyiliği, ödülü ve iyi sonucu bildirir.","gloss":"kötülük ve kötü sonuç","neighbor_only":"Komşu dal, kötülüğü, zararı, kötü durumu ve kötü kişiyi bildirir.","neighbor_ref":"root_000787/B001","relation_type":"antonym","shared_zone":"İki dal, bir kişinin karşılaştığı şeyin iyi ya da kötü olması ekseninde karşı karşıya gelir."},{"boundary_match":"partial","distinction":"Olumlu nitelik ile o niteliği taşıyan bir sonuç ya da kişiye ulaşan iyilik aynı değildir. Bu dal ürün ve sonuç yapısını; komşu dal ise nitelik ve değerlendirmeyi korur.","focus_only":"Bu dal, kişiye ulaşan iyi şeyi, karşılığı veya sonucu adlandırır.","gloss":"güzel ve beğenilir nitelik","neighbor_only":"Komşu dal, kişi ya da şeyde bulunan güzel ve beğenilir niteliği adlandırır.","neighbor_ref":"root_000323/B001","relation_type":"near_neighbor","shared_zone":"İyi bir sonuç veya ödül, olumlu ve beğenilir diye nitelenebilir."},{"boundary_match":"partial","distinction":"Komşu dal yapanın eylemini ve işin yapılışını, bu dal ise alıcının karşılaştığı iyiliği veya çıkan iyi sonucu merkez alır. Süreç ile ürün birbirinin yerine kullanılamaz.","focus_only":"Bu dal, iyiliğin kişiye ulaşan ürününü, karşılığını veya sonucunu bildirir.","gloss":"iyi davranma ve iyilik etme","neighbor_only":"Komşu dal, bir kişinin iyi işi yapmasını veya başkasına iyilikte bulunmasını bildirir.","neighbor_ref":"root_000323/B002","relation_type":"near_neighbor","shared_zone":"Birine yapılan iyilik, o kişinin karşılaştığı sevindirici bir iyilik doğurabilir."}],"source_phrase_ar":"للذين أحسنوا الحسنى وزيادة أي الجنة وهي ضد السوءى (ayn)؛ الحسنة خلاف السيئة (sihah)؛ الحسنى خلاف السوأى (sihah)؛ الحسنى هي الجنة وضد الحسنى السوءى (tahdhib)؛ إحدى الحسنيين يعني الظفر أو الشهادة (tahdhib)؛ حسنة أي نعمة (tahdhib)؛ أي غنيمة وخصب (tahdhib)؛ الحسنة يعبر عنها عن كل ما يسر من نعمة (mufradat)؛ خصب وسعة وظفر (mufradat)؛ من ثواب وما أصابك من سيئة أي من عقاب (mufradat)","source_summary":"Kaynakların toplu anlatımı, kötü şeyin karşısındaki sevindirici iyiliği hem dünyadaki bolluk ve utkı hem de ödül ve iyi son olarak verir. Sonsuz mutluluk yurdu ile iki iyi sonuçtan biri olan utkı veya inanç uğruna ölüm, genel çekirdeğin belirli gerçekleşmeleridir.","sources":["AY","SI","TA","MU"],"what_is_ar":"الحسنة والحسنى بوصفهما خيرا أو نعمة أو ثوابا أو عاقبة حسنة تقابل السيئة والسوءى","what_is_not_ar":"النعت الجمالي، وفعل الإحسان نفسه، وأسماء الأماكن والأشخاص"},"support_links":[]},{"boundary":"Bu kümedeki sözler geçtikleri yerde güzellik niteliğini zorunlu olarak bildirmez; belirli yer, beden bölümü, gök cismi ve eylem gönderimlerini korur.","branch_kind":"bare","branch_ref":"root_000323/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُسْنَىٰ","morph_features":"STEM|POS:N|LEM:HusonaY`|ROOT:Hsn|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:6:2:3","qac_word_ref":"92:6:2","surface_ar":"حُسْنَىٰ"}],"gloss":"yer, gök cismi ve beden bölümü adları ile kum tepesine oturma kullanımı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir dağ, kum sırtı, kumluk veya temiz yüksek kum tepesi bu söz ailesindeki biçimlerle adlandırılabilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ön kolun bileğe yakın yarısı için kalıplaşmış bir beden bölümü adlandırması bulunur."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Söz ailesindeki ayrı bir biçim ayı adlandırır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Söz ailesindeki küçültmeli bir biçim, yüksek dağ anlamında kullanılır."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bağlantılı eylem biçimi, temiz ve yüksek bir kum tepesine oturmayı bildirir."}}],"root_ar":"ح س ن","root_id":"root_000323","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek bir ortak nesne anlamı varsaymadan, dalın farklı kalıplaşmış gönderimlerini ve bağlantılı eylemini topluca tanıtmak için kullanılır.","boundary_detail":"Bu kümedeki sözler geçtikleri yerde güzellik niteliğini zorunlu olarak bildirmez; belirli yer, beden bölümü, gök cismi ve eylem gönderimlerini korur.","branch_image_ar":"أسماء الحسن للمواضع والأجسام","concept_gloss":"yer, gök cismi ve beden bölümü adları ile kum tepesine oturma kullanımı","contextual_glosses":[{"applicability":"Biçimin bir arazi oluşumunu ya da belirli bir kumluk yeri adlandırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ön kol bölümünü, ayı ve kum tepesine oturma eylemini kapsamaz.","preserves":"Dağ ve kum oluşumlarına ilişkin kalıplaşmış yer gönderimlerini korur."},"facet_ids":["F001","F004"],"text":"dağ, kum sırtı veya kum tepesi adı","usage_role":"contextual"},{"applicability":"Sözün insan bedenindeki ön kol bölümünü gösterdiği dar kullanımın tam açıklamasıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Beden bölümünü ve ön kol içindeki bileğe yakın konumunu eksiksiz korur."},"facet_ids":["F002"],"text":"ön kolun bileğe yakın yarısı","usage_role":"explanatory"},{"applicability":"Söz ailesindeki ilgili biçimin gök cismini adlandırdığı kullanımda doğrudan karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gök cismi olan ay gönderimini doğrudan ve eksiksiz korur."},"facet_ids":["F003"],"text":"ay","usage_role":"contextual"}],"definition":"Aynı söz ailesindeki biçimlerin dağ, kum sırtı, kum tepesi, ön kolun bileğe yakın yarısı, ay ve yüksek dağ için kalıplaşmış adlandırmalar olarak kullanıldığı; ayrıca temiz ve yüksek bir kum tepesine oturma eylemini bildirdiği söz varlığı kümesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir dağ, kum sırtı, kumluk veya temiz yüksek kum tepesi bu söz ailesindeki biçimlerle adlandırılabilir."},{"facet_id":"F002","role":"source_variant","statement":"Ön kolun bileğe yakın yarısı için kalıplaşmış bir beden bölümü adlandırması bulunur."},{"facet_id":"F003","role":"source_variant","statement":"Söz ailesindeki ayrı bir biçim ayı adlandırır."},{"facet_id":"F004","role":"source_variant","statement":"Söz ailesindeki küçültmeli bir biçim, yüksek dağ anlamında kullanılır."},{"facet_id":"F005","role":"associated_use","statement":"Bağlantılı eylem biçimi, temiz ve yüksek bir kum tepesine oturmayı bildirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bu gönderimlerin her birinde güzel olma niteliğinin ileri sürüldüğü izlenimini doğurur.","collision":"Güzel ve beğenilir olma niteliğini anlatan dalla karışır.","fit":"displacement","loses":"Dağ, kum oluşumu, beden bölümü, ay ve oturma eylemine ilişkin kalıplaşmış gönderimleri siler.","preserves":"Söz ailesinin öteki dalındaki olumlu değerlendirmeyle biçimsel bağlantıyı sezdirir."},"text":"güzellik"}],"identity_rationale":"Dal, kaynak söz öbeğindeki dağ, kum sırtı ve kum tepesi gibi yer adlandırmalarını doğru yakalar; ancak kaynak aynı kümede ön kolun bileğe yakın yarısını, ayı, yüksek dağı ve temiz yüksek bir kum tepesine oturma eylemini de verir. Bu nedenle dal tek bir yer veya nesne türü gibi değil, birbiriyle aynı biçim ailesini paylaşan kalıplaşmış gönderimler ve bunlara bağlı bir eylem kullanımı olarak tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir dağın, kum sırtının, kumluğun veya kum tepesinin adı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ön kolun bileğe yakın yarısı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"ay"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yüksek dağ"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"temiz ve yüksek bir kum tepesine oturmak"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"iki yerin veya iki kum sırtının birlikte anılışı"}],"lexicalization_note":"Dal belirli bir söz öbeğiyle sınırlı sayılmamalı; tek sözcüklü biçimlerde kalıplaşmış birden çok gönderimi ve kum tepesine oturmayı bildiren bağlantılı eylem kullanımını kapsamalıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; adlandırma alanındaki en yakın üç küme ile güzel nitelik dalından ayrımı gösteren dört ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortaklık, beden bölümü ve ad verme alanındadır; gönderimler aynı değildir. Bu daldaki ön kol yarısı ve kum oluşumları, komşunun yıldız, tepe, yer ve araç bölümü adlarının yerine kullanılamaz.","focus_only":"Bu dal kum oluşumları, dağ, ay ve ön kolun belirli yarısı için kendi kalıplaşmış adlandırmalarını içerir.","gloss":"ön kol adıyla anılan yerler ve bölümler","neighbor_only":"Komşu dal, ön kol adıyla anılan yıldız kümeleri, tepeler, yerler ve araç bölümleri gibi farklı adlandırmaları içerir.","neighbor_ref":"root_000512/B013","relation_type":"same_field","shared_zone":"Her iki dalda beden bölümü ile yer veya nesne adlandırmaları aynı söz varlığı alanında yan yana gelir."},{"boundary_match":"field_only","distinction":"Her iki küme ad verme alanında buluşsa da adlandırdıkları yerler ve gök cisimleri ile kullandıkları söz ailesi ayrıdır. Alan ortaklığı anlam eşdeğerliği sağlamaz.","focus_only":"Bu dal belirli kum oluşumlarını, bir beden bölümünü, ayı ve yüksek dağı adlandıran biçimleri kapsar.","gloss":"kişi, yer ve yıldız adları","neighbor_only":"Komşu dal farklı kişi, yer ve yıldız adlarını kendi söz ailesinde toplar.","neighbor_ref":"root_000333/B012","relation_type":"same_field","shared_zone":"İki dal da sözlerin kişi dışı yer ve gök gönderimleri için özel adlandırma olarak kullanılmasını içerir."},{"boundary_match":"partial","distinction":"Dağ adı olma bakımından yaklaşsalar da aynı dağı veya aynı adlandırmayı göstermezler. Ayrıca bu dalın kum, beden, ay ve eylem kapsamı komşu dalda yoktur.","focus_only":"Bu dal birden çok dağ ve kum oluşumu kullanımının yanında beden bölümü, ay ve oturma eylemini de içerir.","gloss":"belirli bir dağın adı","neighbor_only":"Komşu dal yalnızca belirli bir dağın özel adı olan tek bir gönderime odaklanır.","neighbor_ref":"root_000706/B006","relation_type":"near_neighbor","shared_zone":"Bir sözün dağa ad olması iki dalda da görülen ortak kullanım türüdür."},{"boundary_match":"partial","distinction":"Bu daldaki bir dağ, kum tepesi, beden bölümü veya ay gönderimi, o şeyin güzel olduğunu ileri sürmez. Komşu dal ise doğrudan güzel ve beğenilir niteliği taşır.","focus_only":"Bu dal, belirli yerleri, nesneleri ve bir eylemi kalıplaşmış olarak gösterir.","gloss":"güzel ve beğenilir olma","neighbor_only":"Komşu dal, kişi veya şeyin güzel ve beğenilir olmasını nitelik olarak bildirir.","neighbor_ref":"root_000323/B001","relation_type":"near_neighbor","shared_zone":"İki dal aynı söz ailesindeki biçimleri kullandığı için yüzeyde kolayca karıştırılabilir."}],"source_phrase_ar":"الحسن جبل وحبل من حبال الرمل (maqayis)؛ الحسن من الذراع النصف الذي يلي الكوع (maqayis)؛ حسن اسم رملة لنبي سعد (ayn)؛ الحاسن القمر (sihah)؛ الحسن اسم رملة لبنى سعد (sihah)؛ الحسن نقا في ديار بني تميم (tahdhib)؛ أحسن الرجل إذا جلس على الحسن وهو الكثيب النقي العالي (tahdhib)؛ الحسين الجبل العالي (tahdhib)","source_summary":"Toplu kaynak anlatımı, aynı biçim ailesine dağ ve kum oluşumu adları, ön kolun bir yarısı, ay ve yüksek dağ gibi farklı kalıplaşmış gönderimler bağlar. Temiz yüksek bir kum tepesine oturmayı bildiren eylem de bu yer adlandırmasına bağlı ayrı bir kullanımdır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"الأسماء المتفرعة من الحسن للمواضع والأجسام والأجزاء، مثل الحسن للرمل أو الجبل، والحسين للجبل العالي، والحسن من الذراع، والحاسن للقمر","what_is_not_ar":"المعنى الخلقي أو العمل الصالح، والحسنة بمعنى النعمة، وعبارة الجهد والغاية"},"support_links":[]},{"boundary":"Dal yalnızca iki kalıplaşmış ifadeye bağlıdır; genel çaba, genel amaç veya her türlü son nokta anlamına genişletilmemelidir.","branch_kind":"non_bare","branch_ref":"root_000323/B005","candidate_links":[{"candidate_id":"cand_9fb83b332639e8e6b985","lane":"macro"},{"candidate_id":"cand_8cb4c31ff4b86f2ef0fc","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"حُسْنَىٰ","morph_features":"STEM|POS:N|LEM:HusonaY`|ROOT:Hsn|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:6:2:3","qac_word_ref":"92:6:2","surface_ar":"حُسْنَىٰ"}],"gloss":"bir işteki en yüksek çabası ve erişebileceği son sınır","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir işi yapmada kişiye ait en yüksek çaba ile ulaşılabilecek son sınır birlikte anlatılır."}}],"root_ar":"ح س ن","root_id":"root_000323","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kanıtlanan iki kalıplaşmış biçimde, kişinin belirli bir işi yapma gücünün ve çabasının üst sınırı anlatılırken kullanılır.","boundary_detail":"Dal yalnızca iki kalıplaşmış ifadeye bağlıdır; genel çaba, genel amaç veya her türlü son nokta anlamına genişletilmemelidir.","branch_image_ar":"حُسَيْناء الغاية والجهد","concept_gloss":"bir işteki en yüksek çabası ve erişebileceği son sınır","contextual_glosses":[{"applicability":"Bir kişinin belirli bir işi yapmak için kullanabileceği bütün gücün vurgulandığı doğal anlatımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çabanın yanında ayrıca belirtilen erişilecek son sınırı açıkça adlandırmaz.","preserves":"Kişiye bağlı güç ve çabanın erişebildiği en yüksek dereceyi korur."},"facet_ids":["F001"],"text":"elinden gelenin en çoğu","usage_role":"contextual"},{"applicability":"Kişinin belli bir işi yaparken hem harcayabileceği çabanın hem ulaşabileceği noktanın üst sınırı açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gücü, etkin çabayı ve ulaşılabilecek son sınırı tek anlatımda korur."},"facet_ids":["F001"],"text":"gücünün ve çabasının son sınırı","usage_role":"explanatory"}],"definition":"Bir kişinin belirli bir işi yapmak için gösterebileceği en yüksek çabayı ve erişebileceği son sınırı bildiren, iki kalıplaşmış biçime özgü anlatımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir işi yapmada kişiye ait en yüksek çaba ile ulaşılabilecek son sınır birlikte anlatılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sınırın belirli bir kişiye ve onun bir işi yaparken göstereceği en yüksek çabaya bağlı olduğunu göstermez.","preserves":"Bir şeyin erişebileceği bitiş sınırı yönünü korur."},"text":"son nokta"}],"identity_rationale":"Dal çerçevesi, kaynak söz öbeğinde iki kalıplaşmış biçim için verilen bir işi yapmadaki en yüksek çaba ve erişilebilen son sınır anlamını doğru korur. Anlam genel güzellik, kişi adı veya yer adı değildir; yalnızca bu özel ifadelerin bir kişiye bağlanan güç ve son nokta değerlendirmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bir işi yaparken gösterebileceği en yüksek çaba ve erişebileceği son sınır"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bir işi yaparken gösterebileceği en yüksek çaba ve erişebileceği son sınır"}],"lexicalization_note":"Dal yalın bir kök anlamı değildir; anlam, kişinin belirli bir işi yaparken gösterebileceği en yüksek çaba ve erişebileceği son sınırı bildiren iki kalıplaşmış biçimle sınırlıdır.","neighbor_coverage_note":"Bütün aday komşular karşılaştırıldı; özel ifadenin çaba, güç yetirme ve genel son sınır alanlarından ayrılışını gösteren beş ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda sınır kişinin gücü ve çabasıyla ölçülür; komşuda ise varılan sonun övülmeye değer oluşu öne çıkar. Bu değerlendirme farkı nedeniyle yalnızca son sınır bağlamında yaklaşırlar.","focus_only":"Bu dalın kalıplaşmış biçimleri, kişinin belirli bir işi yapmadaki en yüksek çabasını ve erişebileceği sınırı bildirir.","gloss":"ulaşılması övülen son sınır","neighbor_only":"Komşu dalın kalıplaşmış biçimleri, ulaşılması övülen bir sonu ve varılacak en ileri noktayı bildirir.","neighbor_ref":"root_000355/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da kalıplaşmış bir anlatımla erişilebilecek en ileri noktayı belirtir."},{"boundary_match":"partial","distinction":"Komşu dal çaba sürecini genel olarak anlatır. Bu dal ise yalnızca özel biçimlerde, o çabanın ulaşabileceği en yüksek dereceyi ve son sınırı birlikte gösterir.","focus_only":"Bu dal iki kalıplaşmış biçimde çaba ile erişilebilen son sınırı birlikte bildirir.","gloss":"çalışıp bütün gücünü harcama","neighbor_only":"Komşu dal, belirli bir kalıba bağlı olmadan çalışıp çabalama ve güç harcamayı bildirir.","neighbor_ref":"root_000076/B010","relation_type":"near_synonym","shared_zone":"Bir işi yapmak için kişinin gücünü kullanması ve çaba göstermesi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Bu dal özel bir anlatımla en yüksek çaba ve son sınırı bildirir. Komşu dal ise genel yeterlik, alan darlığı, yetersizlik ve ölçüyü aşma gibi daha geniş durumlara uzanır.","focus_only":"Bu dal, kişinin bir işi yaparken harcadığı en yüksek çabayı sınırla birlikte öne çıkarır.","gloss":"güç yetirme ve erişim alanı","neighbor_only":"Komşu dal, genel güç yetirme alanını, yetmezliği ve ölçünün aşılmasını da kapsar.","neighbor_ref":"root_000512/B004","relation_type":"near_synonym","shared_zone":"Bir kişinin bir işi yapabilecek gücü ile erişebileceği sınır iki dalda da değerlendirilir."},{"boundary_match":"partial","distinction":"Komşu dal güçlük ve bütün gücü harcama sürecini genel alanlara yayar. Bu dalın anlamı ise iki özel biçimde kişisel çaba ile erişilen üst sınırın birlikte söylenmesine bağlıdır.","focus_only":"Bu dal iki kalıplaşmış biçimde kişinin bir işteki en yüksek çabası ile erişim sınırını birlikte verir.","gloss":"güçlük altında bütün gücünü kullanma","neighbor_only":"Komşu dal, güçlük altında bütün gücü kullanmayı ve iş, görüş veya yemin gibi daha geniş alanlarda sona varmayı kapsar.","neighbor_ref":"root_000268/B001","relation_type":"near_synonym","shared_zone":"Bir işi sonuçlandırmak için bütün gücün kullanılması ve sona kadar çabalanması iki dalda örtüşür."},{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği nesnenin ya da hareketin vardığı genel sondur. Bu dalda ise sınır, belirli bir kişinin işi yapma çabasının ve gücünün ölçüsüdür.","focus_only":"Bu dal, son sınırı bir kişinin belirli işi yapmadaki gücü ve çabasıyla ilişkilendirir.","gloss":"bir şeyin vardığı son ve bitiş","neighbor_only":"Komşu dal, bir şeyin genel bitişini, kenarını veya bir iletinin ya da okun hedefe ulaşmasını bildirir.","neighbor_ref":"root_001560/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da erişilen son noktayı veya üst sınırı anlatabilir."}],"source_phrase_ar":"حُسَيْناؤه أن يفعل كذا وحُسَيْناه مثله أي جهده وغايته (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"İki kalıplaşmış biçim de bir kişinin belirli bir işteki en yüksek çabasını ve erişebileceği son sınırı bildirir."}],"source_summary":"Ortaklaştırılacak çok kaynaklı bir anlatım yoktur; dal, aynı anlama gelen iki kalıplaşmış biçimin tek tanıklığına dayanır.","sources":["TA"],"what_is_ar":"قولهم حُسَيْناؤه أو حُسَيْناه بمعنى جهده وغايته","what_is_not_ar":"الحسن بمعنى الجمال، واسم الحسين للجبل أو الشخص، والحسنة بمعنى النعمة"},"support_links":["sup_e742769a22f6b10ad063","sup_fd04a692af9b1a277c30"]},{"boundary":"Dal, arkadaşlık, maddi verme, evlilik hakkı ve nesnelerin fiziksel sağlamlığıyla ilgili kullanımları kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000852/B001","candidate_links":[{"candidate_id":"cand_1f91fa6f782358926eb0","lane":"macro"},{"candidate_id":"cand_ba95413c78d0046d8fac","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"صَدَّقَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Sad~aqa|ROOT:Sdq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:6:1:2","qac_word_ref":"92:6:1","surface_ar":"صَدَّقَ"}],"gloss":"sözün inançla ve gerçekle uyuşması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söylenen söz yalanın karşıtıdır ve gerçeği bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tam uygunluk, sözün hem konuşanın iç inancıyla hem de bildirilen durumla uyuşmasını gerektirir."}}],"root_ar":"ص د ق","root_id":"root_000852","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Söz doğruluğunun hem içtenlik hem de gerçekliğe uygunluk koşulunu birlikte anlatan genel karşılıktır.","boundary_detail":"Dal, arkadaşlık, maddi verme, evlilik hakkı ve nesnelerin fiziksel sağlamlığıyla ilgili kullanımları kapsamaz.","branch_image_ar":"صدق القول","concept_gloss":"sözün inançla ve gerçekle uyuşması","contextual_glosses":[{"applicability":"Bağlam yalnızca yalan söylememeyi veya gerçeği bildirmeyi öne çıkardığında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sözün hem iç inançla hem de dış gerçeklikle birlikte uyuşması koşulunu açıkça taşımaz.","preserves":"Yalanın karşıtı olan doğru söyleme yönünü korur."},"facet_ids":["F001"],"text":"doğru söz söyleme","usage_role":"contextual"},{"applicability":"Konuşanın inancı ile anlattığı durum arasındaki iki yönlü uygunluğun açıklanması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İçtenlik ile dış gerçeğe uygunluğu aynı söz eyleminde birleştirir."},"facet_ids":["F001","F002"],"text":"içten ve gerçeğe uygun anlatım","usage_role":"explanatory"}],"definition":"Bir sözün yalan olmaması ve hem söyleyenin iç inancıyla hem de hakkında konuşulan gerçekle uyuşmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söylenen söz yalanın karşıtıdır ve gerçeği bildirir."},{"facet_id":"F002","role":"specialization","statement":"Tam uygunluk, sözün hem konuşanın iç inancıyla hem de bildirilen durumla uyuşmasını gerektirir."}],"identity_rationale":"Kaynak ifadesi bu dalı yalanın karşıtı olan söz doğruluğu olarak kurar ve daha özel olarak sözün hem konuşanın iç inancına hem de anlattığı gerçeğe uymasını ister. Bu nedenle dal, genel doğruluk kavramına genişletilmeden söz ve bildirim alanında tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"doğruluk; sözün inançla ve gerçekle uyuşması"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"konuşurken doğruyu söylemek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"birine doğru söz söylemek veya onun sözünü doğru saymak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"doğruluğa sürekli bağlı ve kuşkusuz onaylayan kimse"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"çok doğru sözlü kimse"}],"lexicalization_note":"Tanım, yalın biçimdeki söz doğruluğunu temel alır; konuşmada doğruyu söyleme ve bir sözün doğruluğunu kabul etme gibi yapıya bağlı kullanımları ayrıca sınırlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma genel doğrulukla kapsam farkını, doğrudan karşıtlığı ve kısmi doğrulukla karışma sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak, söz ve bildirimin iki yönlü uygunluk koşuludur; komşu ise bu sınırı aşarak doğru inanç, doğru eylem ve gerçek durum gibi daha geniş kullanımları kapsar.","focus_only":"Odak dalı özellikle sözün konuşanın iç inancı ve bildirilen gerçeklikle birlikte uyuşmasını ister.","gloss":"gerçeğe uygun söz ile genel doğruluk","neighbor_only":"Komşu dal, söz dışındaki inanç ve eylemleri de kapsayan daha genel gerçeklik, doğruluk ve kesinlik alanına uzanır.","neighbor_ref":"root_000347/B001","relation_type":"near_synonym","shared_zone":"İki dal da yanlışın karşısında gerçeğe uygun olmayı temel alır."},{"boundary_match":"opposed","distinction":"Odak sözün gerçeğe uygun kutbunu, komşu ise gerçek dışı iddia ve yalan kutbunu temsil eder.","focus_only":"Odak dalında söz, iç inanç ve bildirilen gerçekle uyumludur.","gloss":"doğru söz ve asılsız iddia","neighbor_only":"Komşu dalda kişi gerçeği olmayan bir iddia ortaya atar veya yanlış söyler.","neighbor_ref":"root_000127/B003","relation_type":"antonym","shared_zone":"Her iki dal da bir sözün gerçekle ilişkisini değerlendirir."},{"boundary_match":"partial","distinction":"Odakta eksiksiz uygunluk vardır; komşuda doğru unsur bulunsa bile yalanla karışma bu uygunluğu bozar.","focus_only":"Odak dalı sözün iç inanç ve dış gerçekle tam uygunluğunu gerektirir.","gloss":"tam doğru söz ve doğruyla karışık yalan","neighbor_only":"Komşu dal, doğru ile yalanın karıştırıldığı ve doğruluğun arı kalmadığı bir söylemi anlatır.","neighbor_ref":"root_001442/B012","relation_type":"near_neighbor","shared_zone":"İki dal da bir anlatımdaki doğru ve yanlış bileşenlerini konu edinir."}],"source_phrase_ar":"الصدق خلاف الكذب (maqayis;ayn;sihah;tahdhib)؛ الصدق والكذب أصلهما في القول (mufradat)؛ الصدق مطابقة القول الضمير والمخبر عنه معا (mufradat)","source_summary":"Kaynakların ortak çizgisi, söz doğruluğunu yalanın karşıtı sayar; ayrıntılı açıklama, söz ile iç inanç ve dış gerçeklik arasında birlikte uygunluk arar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الصدق ضد الكذب، وقول الصدق، ومطابقة القول للضمير والمخبر عنه","what_is_not_ar":"لا يدخل فيه الصداق ولا الصدقة ولا مجرد الصداقة"},"support_links":["sup_1831385efe2952ea96d9","sup_cab23a87d0f55bd398de"]},{"boundary":"Bu dal söz doğruluğunu veya ahlaki güvenilirliği değil, bir nesnenin somut sertlik ve düzgünlük niteliğini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000852/B002","candidate_links":[{"candidate_id":"cand_9fb83b332639e8e6b985","lane":"macro"},{"candidate_id":"cand_8cb4c31ff4b86f2ef0fc","lane":"macro"},{"candidate_id":"cand_8c19034e036d24c69fd0","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"صَدَّقَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Sad~aqa|ROOT:Sdq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:6:1:2","qac_word_ref":"92:6:1","surface_ar":"صَدَّقَ"}],"gloss":"nesnenin sağlamlığı veya düzgünlüğü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne fiziksel sertlik ve sağlamlık taşır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nitelik, biçim bakımından düz veya düzgün olmayı da anlatabilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sert ve güçlü bir mızrak bu fiziksel niteliğin örneğidir."}}],"root_ar":"ص د ق","root_id":"root_000852","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel sertlik ile düz ve düzgün biçim seçeneklerini tek üst karşılıkta koruyan kullanımdır.","boundary_detail":"Bu dal söz doğruluğunu veya ahlaki güvenilirliği değil, bir nesnenin somut sertlik ve düzgünlük niteliğini anlatır.","branch_image_ar":"صلابة الشيء واستواؤه","concept_gloss":"nesnenin sağlamlığı veya düzgünlüğü","contextual_glosses":[{"applicability":"Bağlam bir nesnenin direncini veya bir mızrağın fiziksel gücünü öne çıkardığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Düz veya düzgün biçimli olma seçeneğini karşılamaz.","preserves":"Fiziksel sertlik, sağlamlık ve güç yönünü korur."},"facet_ids":["F001","F003"],"text":"sağlam ve sert nesne","usage_role":"contextual"},{"applicability":"Bağlam sertlikten çok nesnenin biçimsel düzgünlüğünü belirginleştirdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesnenin sertlik ve dayanıklılık niteliğini karşılamaz.","preserves":"Biçim bakımından düz ve düzgün olma yönünü korur."},"facet_ids":["F002"],"text":"düzgün ve düz nesne","usage_role":"contextual"}],"definition":"Bir nesnenin fiziksel olarak sert ve dayanıklı ya da biçim bakımından düz ve düzgün olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne fiziksel sertlik ve sağlamlık taşır."},{"facet_id":"F002","role":"source_variant","statement":"Nitelik, biçim bakımından düz veya düzgün olmayı da anlatabilir."},{"facet_id":"F003","role":"example","statement":"Sert ve güçlü bir mızrak bu fiziksel niteliğin örneğidir."}],"identity_rationale":"Kaynak ifadesi fiziksel bir şey için sertlik ve düz ya da düzgün olma niteliklerini açıkça birlikte verir; mızrak örneği de bu somut nitelemeyi destekler. Dalın fiziksel güç ve biçim düzgünlüğü çerçevesi bu kanıtla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir nesnedeki sertlik veya düzgünlük"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"sert ve güçlü nesne ya da mızrak"}],"lexicalization_note":"Yalın nitelik sertlik ya da düzgünlük olarak tanımlanır; nesne ve mızrakla kurulan niteleme örnekleri yalnızca bu fiziksel anlamın yapıya bağlı gerçekleşmeleridir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler doğrudan sertlik örtüşmesini, soyut güce doğru kapsam genişlemesini ve yalnızca aynı fiziksel alanda kalan yarıksızlık durumunu ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta düzgünlük ayrı bir kaynak seçeneğidir; komşuda ise şiddet ve uzunluk gibi odakta bulunmayan nitelikler vardır.","focus_only":"Odak dalı sertliğin yanında düz veya düzgün biçimli olmayı da kapsar.","gloss":"sert ve düzgün nesne ile sert ve şiddetli nesne","neighbor_only":"Komşu dal sertliğe ek olarak şiddet ve bazı aktarımlarda uzunluk niteliklerini taşır.","neighbor_ref":"root_000188/B003","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı bir nesnenin fiziksel sertliğidir."},{"boundary_match":"partial","distinction":"Odak somut nesnenin sertliği veya düzgünlüğüyle sınırlıdır; komşu hem somut hem de soyut güç ve şiddet durumlarını kapsar.","focus_only":"Odak dalı nesnenin düz ve düzgün olmasını da ifade edebilir.","gloss":"nesne sağlamlığı ile genel güç ve dayanıklılık","neighbor_only":"Komşu dal fiziksel sertliği aşarak cesaret, yürek dayanıklılığı, zor durum ve güç harcama gibi soyut alanlara uzanır.","neighbor_ref":"root_000782/B002","relation_type":"near_synonym","shared_zone":"Her iki dal fiziksel güç ve sertlik niteliğinde buluşur."},{"boundary_match":"field_only","distinction":"Odak genel bir fiziksel niteliktir; komşu belirli bir nesnenin belirli kusurdan yoksun oluşunu anlatır.","focus_only":"Odak nesnenin olumlu sertlik veya düzgünlük niteliğini doğrudan belirtir.","gloss":"sağlamlık ve yarıksız yay","neighbor_only":"Komşu yalnızca yayın gövdesinde yarık bulunmaması ve yayın çatlamaması durumunu belirtir.","neighbor_ref":"root_001284/B003","relation_type":"same_field","shared_zone":"İki dal da fiziksel bir nesnenin bütünlüğü ve dayanıklılığı alanındadır."}],"source_phrase_ar":"شيء صدق أي صلب (maqayis)؛ رمح صدق (maqayis)؛ الصدق الصلب والمستوي (sihah;tahdhib)","source_summary":"Ortak kanıt, fiziksel nesneyi sert ve sağlam diye niteler; bazı aktarımlar buna düz veya düzgün olma yönünü de ekler ve mızrağı örnek verir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الشيء الصلب أو المستوي، ورمح صدق، وما يدل على قوة محسوسة في الشيء","what_is_not_ar":"لا يدخل فيه صدق القول ولا الصداقة ولا صدقة المال"},"support_links":["sup_bf1ed743df9188d14f17","sup_e742769a22f6b10ad063","sup_fd04a692af9b1a277c30"]},{"boundary":"Dal, yalnızca doğru haber vermeyi değil; bir kişi, şey veya durumdaki tamlık, iyilik, güvenilirlik ve övgüye değer sağlamlığı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000852/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صَدَّقَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Sad~aqa|ROOT:Sdq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:6:1:2","qac_word_ref":"92:6:1","surface_ar":"صَدَّقَ"}],"gloss":"tamlık, iyilik ve güvenilirlik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey kendi türü içinde tamlığa ve kusursuzluğa erişmiştir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan nitelemesinde iyilik, erdem, sağlam karakter ve güvenilirlik öne çıkar."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yer, öncelik, giriş, çıkış veya anılma gibi alanlarda durumun iyi, sağlam ve sonradan övülmeye elverişli oluşunu belirtir."}}],"root_ar":"ص د ق","root_id":"root_000852","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Şeylerdeki kusursuzluğu, kişilerdeki erdemi ve durumlarda övgüye değer sağlamlığı birlikte temsil eden üst karşılıktır.","boundary_detail":"Dal, yalnızca doğru haber vermeyi değil; bir kişi, şey veya durumdaki tamlık, iyilik, güvenilirlik ve övgüye değer sağlamlığı anlatır.","branch_image_ar":"تمام الصلاح والثبوت","concept_gloss":"tamlık, iyilik ve güvenilirlik","contextual_glosses":[{"applicability":"Bir kişi veya topluluğun erdem, sağlam karakter ve güvenilirlik bakımından övüldüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Şeylerdeki genel tamlığı ve durumlara bağlı övgü kullanımlarını kapsamaz.","preserves":"İnsan nitelemesindeki iyilik ve güvenilirlik yönünü korur."},"facet_ids":["F002"],"text":"iyi ve güvenilir kimse","usage_role":"contextual"},{"applicability":"Bir yerin, başlangıcın, girişin, çıkışın veya kalıcı anılmanın iyi ve övgüye uygun niteliği anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişi nitelemesini ve her şeydeki yalın tamlık anlamını kapsamaz.","preserves":"Durumun iyi, sağlam ve sonradan övülmeye elverişli oluşunu korur."},"facet_ids":["F003"],"text":"övülmeye değer sağlam durum","usage_role":"explanatory"}],"definition":"Bir kişi, şey veya durumun iyi, güvenilir ve övgüye değer sayılacak ölçüde tam ve sağlam olmasıdır. Kişi nitelemelerinde erdem ve güvenilirlik, belirli yapılarda ise kalıcı ve övülebilir bir durum öne çıkar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey kendi türü içinde tamlığa ve kusursuzluğa erişmiştir."},{"facet_id":"F002","role":"specialization","statement":"İnsan nitelemesinde iyilik, erdem, sağlam karakter ve güvenilirlik öne çıkar."},{"facet_id":"F003","role":"extension","statement":"Yer, öncelik, giriş, çıkış veya anılma gibi alanlarda durumun iyi, sağlam ve sonradan övülmeye elverişli oluşunu belirtir."}],"identity_rationale":"Kaynak ifadesi insan nitelemelerini, herhangi bir şeyde tamlık fikrini ve övgüye uygun sağlam durum bildiren bir dizi kullanımı aynı dalda toplar. Verilen tam iyilik ve kalıcılık çerçevesi, bu kullanımları söz doğruluğuna indirgemeden bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"iyi, güvenilir ve erdemli kişi ya da topluluk"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir şeyde tamlık ve kusursuzluk"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"övülmeye değer, iyi ve sağlam durum"}],"lexicalization_note":"Yalın biçimdeki tamlık anlamı korunur; kişi nitelemeleri ile yer, öncelik, giriş, çıkış ve anılma alanındaki yapıya bağlı övgü kullanımları ayrı yüzler olarak gösterilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen üç komşu kalite, biçimsel düzgünlük ve toplumsal ünle oluşabilecek başlıca karışmaları açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak tamlık ve güvenilirliği, komşu ise genel kaliteyi ve kaliteyi artırmaya yönelik eylemleri öne çıkarır.","focus_only":"Odak dalı tamlığın yanında kişi güvenilirliğini ve belirli övgü yapılarını kapsar.","gloss":"tam ve güvenilir olma ile nitelikli olma","neighbor_only":"Komşu dal bir şeyi iyi yapma, iyileştirme ve iyi bulma eylemlerini de kapsar.","neighbor_ref":"root_000274/B003","relation_type":"near_synonym","shared_zone":"İki dal bir şeyin iyi ve övülmeye değer niteliğinde buluşur."},{"boundary_match":"partial","distinction":"Odak değer ve güvenilirlik yüklü bir tamlıktır; komşu biçimsel düzeltme ve dengeli duruma gelme sürecini de içerir.","focus_only":"Odak dalı ahlaki iyilik, güvenilirlik ve övgüye değer kalıcılık taşır.","gloss":"tam iyilik ile düzelmiş dengelilik","neighbor_only":"Komşu dal eğriliğin düzeltilmesi, yaratılışta dengelilik ve canlıların uygun duruma gelmesi süreçlerini kapsar.","neighbor_ref":"root_000766/B002","relation_type":"near_synonym","shared_zone":"İki dal tam, düzgün ve iyi durumda olma fikrinde örtüşür."},{"boundary_match":"partial","distinction":"Odak nesnenin veya kişinin niteliğidir; komşu ise başkaları arasında dolaşan olumlu anılma ve ün sonucudur.","focus_only":"Odak, kişi veya durumun gerçekten iyi ve güvenilir niteliğini belirtir.","gloss":"övülmeye değer nitelik ve iyi ün","neighbor_only":"Komşu, bu nitelikten bağımsız olarak insanlar arasında yayılmış olumlu ünü belirtir.","neighbor_ref":"root_000890/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal olumlu değerlendirme ve övgü alanında yer alır."}],"source_phrase_ar":"رجل صدق (maqayis;ayn;sihah;tahdhib)؛ الصدق الكامل من كل شيء (ayn;tahdhib)؛ في مقعد صدق وقدم صدق ومدخل صدق ومخرج صدق ولسان صدق (mufradat)","source_summary":"Kanıt, tamlığı genel çekirdek olarak verir; insanları iyilik ve güvenilirlikle niteler, belirli durumları da doğru biçimde övülmeye elverişli sağlamlıkları bakımından değerlendirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه رجل صدق وامرأة صدق وقوم صدق، والكامل من كل شيء، ومقعد صدق وقدم صدق ومدخل صدق ومخرج صدق ولسان صدق","what_is_not_ar":"لا يدخل فيه مجرد الإخبار الصادق ولا مال الصدقة ولا مهر المرأة"},"support_links":[]},{"boundary":"Fiilî yerine getirme çekirdeğin önemli bir görünümüdür; ancak gerçekleşen tahmin ve doğrulayıcı onay da dalın sınırı içinde kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000852/B004","candidate_links":[{"candidate_id":"cand_adb33c8ee67d98f9ab57","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"صَدَّقَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Sad~aqa|ROOT:Sdq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:6:1:2","qac_word_ref":"92:6:1","surface_ar":"صَدَّقَ"}],"gloss":"sözü veya beklentiyi doğrulayıp gerçekleştirme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir söz, beklenti veya iddia gerçekleşme, eylem ya da onayla doğru çıkarılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Savaş bağlamında kişi gereğini yerine getirir, sebat eder ve eylemiyle sözünün hakkını verir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir tahminin veya beklentinin doğru çıkması da gerçekleşme yoluyla doğrulamadır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir sözün doğruluğunu kabul etmek veya önceki bir bildiriyi desteklemek onay yoluyla doğrulamadır."}}],"root_ar":"ص د ق","root_id":"root_000852","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylemle yerine getirme, beklentinin çıkması ve bir bildiriyi onaylama yollarını ortak doğrulama çekirdeğinde birleştirir.","boundary_detail":"Fiilî yerine getirme çekirdeğin önemli bir görünümüdür; ancak gerçekleşen tahmin ve doğrulayıcı onay da dalın sınırı içinde kalır.","branch_image_ar":"تحقيق الوعد والفعل","concept_gloss":"sözü veya beklentiyi doğrulayıp gerçekleştirme","contextual_glosses":[{"applicability":"Bir kimsenin vaat ettiğini veya üstlendiğini fiilen yerine getirdiği, özellikle mücadelede gereğini yaptığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tahminin kendiliğinden gerçekleşmesini ve bir bildirinin onaylanmasını kapsamaz.","preserves":"Sözün eylem ve yerine getirme yoluyla doğru çıkarılması yönünü korur."},"facet_ids":["F001","F002"],"text":"sözünü eylemiyle doğrulamak","usage_role":"contextual"},{"applicability":"Beklenen veya tahmin edilen durumun gerçekten meydana geldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sözün eylemle yerine getirilmesini ve bildirinin onaylanmasını kapsamaz.","preserves":"Beklentinin gerçekleşmeyle doğrulanması yönünü korur."},"facet_ids":["F001","F003"],"text":"tahmini doğru çıkmak","usage_role":"contextual"},{"applicability":"Yeni bir söz veya metin daha önce bildirileni destekleyip onun doğruluğunu ortaya koyduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Fiilî yerine getirme ile tahminin gerçekleşmesi yönlerini kapsamaz.","preserves":"Önceki bildiriyi destekleme ve doğru sayma yönünü korur."},"facet_ids":["F001","F004"],"text":"önceki bildiriyi doğrulamak","usage_role":"contextual"}],"definition":"Bir söz, beklenti, vaat veya iddiayı gerçekleşme, eylem ya da onay yoluyla doğru çıkarmak ve gerektiğinde söyleneni fiilen yerine getirmektir. Savaşta gereğini yapma, tahminin gerçekleşmesi ve önceki bir bildiriyi destekleme bu çekirdeğin yapıya bağlı görünümleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir söz, beklenti veya iddia gerçekleşme, eylem ya da onayla doğru çıkarılır."},{"facet_id":"F002","role":"specialization","statement":"Savaş bağlamında kişi gereğini yerine getirir, sebat eder ve eylemiyle sözünün hakkını verir."},{"facet_id":"F003","role":"extension","statement":"Bir tahminin veya beklentinin doğru çıkması da gerçekleşme yoluyla doğrulamadır."},{"facet_id":"F004","role":"extension","statement":"Bir sözün doğruluğunu kabul etmek veya önceki bir bildiriyi desteklemek onay yoluyla doğrulamadır."}],"identity_rationale":"Kaynak ifadesi yalnızca vaat veya savaşta gereğini yapmayı değil, bir tahmini gerçekleştirmeyi, bir sözü onaylamayı ve önceki bir bildiriyi destekleyip doğrulamayı da kapsar. Bu nedenle dal, salt vaat yerine getirme olarak değil; söz, beklenti veya iddiayı gerçekleşme, eylem ya da onayla doğrulama alanı olarak yeniden çerçevelenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"savaşta gereğini yerine getirip sebat etmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"atılımında veya koşusunda verdiği sözü tutan"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"tahmini gerçekleşmek veya tahminini gerçekleştirmek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bir sözün veya durumun doğruluğunu ortaya koyma ve onaylama"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"öncekini doğrulayan ve destekleyen"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"sözü doğru kabul edip onaylayan kimse"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"doğruluğa sürekli bağlı ve kuşkusuz onaylayan kimse"}],"lexicalization_note":"Tanım ortak doğrulama ve gerçekleştirme çekirdeğini verir; savaş, tahmin, önceki bildiri ve konuşmayı onaylama anlamlarını yalnızca kendi yapılarında geçerli uzmanlaşmalar olarak ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler kanıtlayarak doğrulamayı, yükümlülüğü bozma karşıtlığını ve yalnızca sözlü onay vermeyi odak çekirdeğinden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta doğruluk çoğu kez olayın gerçekleşmesi veya sözün eylemle tutulmasıyla belirir; komşuda kanıtlama ve hüküm verme daha merkezîdir.","focus_only":"Odak dalı sözün fiilen yerine getirilmesini ve bir tahminin gerçekleşmesini de kapsar.","gloss":"gerçekleştirerek doğrulama ve gerçeği kanıtlama","neighbor_only":"Komşu dal kanıt göstererek gerçeği ortaya çıkarma, doğru olduğuna hükmetme ve bir işi tamamlama alanına uzanır.","neighbor_ref":"root_000347/B005","relation_type":"near_synonym","shared_zone":"İki dal bir sözün veya durumun doğruluğunu ortaya koyma alanında örtüşür."},{"boundary_match":"opposed","distinction":"Odak yükümlülüğü gerçekleştirerek olumlu kutbu, komşu ise kurulmuş bağı bozarak karşıt kutbu temsil eder.","focus_only":"Odak dalı üstlenilen sözü eylemle yerine getirme ve doğru çıkarma yönünü taşır.","gloss":"sözü yerine getirme ve bağı bozma","neighbor_only":"Komşu dal sağlamlaştırılmış sözleşme, bağlılık veya yemini sonradan bozmayı anlatır.","neighbor_ref":"root_001547/B002","relation_type":"polarity_pair","shared_zone":"İki dal üstlenilmiş bir söz veya bağlılık karşısındaki davranışı değerlendirir."},{"boundary_match":"partial","distinction":"Odak gerçek olay veya eylemle doğrulamayı da kapsar; komşunun çekirdeği dilsel olumlu cevap ve kabuldür.","focus_only":"Odak, onayın yanında sözün eylemle yerine gelmesini veya beklentinin gerçekleşmesini ister.","gloss":"gerçekleştirerek doğrulama ve olumlu cevap","neighbor_only":"Komşu, olumlu cevap verme ve bir sözü dil yoluyla kabul etme işleviyle sınırlıdır.","neighbor_ref":"root_001525/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal bir söz veya önermeyi kabul edip doğrulama işlevinde buluşabilir."}],"source_phrase_ar":"صدقوهم القتال (maqayis;sihah;tahdhib)؛ صدق في القتال إذا وفى حقه (mufradat)؛ صدق ظني (mufradat)؛ لقد صدق عليهم إبليس ظنه أي حقق ظنه (tahdhib)؛ مصدق لما معهم (mufradat)","source_summary":"Ortak çekirdek, bir söz veya beklentinin eylemle, gerçekleşmeyle ya da onayla doğrulanmasıdır; savaşta gereğini yapma, tahminin çıkması ve önceki bildiriyi destekleme bu çekirdeğin farklı gerçekleşmeleridir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه التصديق، وتحقيق الظن أو الرؤيا أو الوعد، والوفاء بالفعل أو القتال، وصدق العهد بالفعل","what_is_not_ar":"لا يدخل فيه المهر ولا العطية المالية ولا الصداقة الاجتماعية"},"support_links":["sup_637938be856a819cfc5f"]},{"boundary":"Buradaki doğruluk, haberin gerçekliğinden çok sevgi, bağlılık ve iyi niyetin içtenliğini niteler.","branch_kind":"bare","branch_ref":"root_000852/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صَدَّقَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Sad~aqa|ROOT:Sdq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:6:1:2","qac_word_ref":"92:6:1","surface_ar":"صَدَّقَ"}],"gloss":"içten sevgiye dayalı dostluk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki kişi arasındaki yakınlık, içten ve doğru bir sevgi inancına dayanır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu bağ, arkadaş olma, karşılıklı dostluk ve içten öğüt verme davranışlarında görünür."}}],"root_ar":"ص د ق","root_id":"root_000852","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yakın arkadaşlık bağını ve bu bağın içten, doğru ve iyi niyetli sevgi temelini birlikte anlatır.","boundary_detail":"Buradaki doğruluk, haberin gerçekliğinden çok sevgi, bağlılık ve iyi niyetin içtenliğini niteler.","branch_image_ar":"صدق المودة والصحبة","concept_gloss":"içten sevgiye dayalı dostluk","contextual_glosses":[{"applicability":"Bağlam ilişkinin içtenlik temelini ayrıca açıklamadan kişiler arasındaki dostça yakınlığı öne çıkardığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sevginin doğruluğu, içtenliği ve iyi niyetli öğüt yönünü açıkça taşımaz.","preserves":"Kişiler arasındaki yakın ve dostça ilişkiyi korur."},"facet_ids":["F001"],"text":"yakın arkadaşlık","usage_role":"contextual"},{"applicability":"Bir kimsenin başka biriyle içten sevgi ve iyi niyet temelinde dostluk kurması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dostluk ilişkisini, içten sevgiyi ve etkin biçimde dost olmayı korur."},"facet_ids":["F001","F002"],"text":"içtenlikle dost olma","usage_role":"contextual"}],"definition":"İçten, doğru ve iyi niyetli sevgiye dayanan yakın arkadaşlık; bu bağlılıkla birine dost olma ve onun iyiliğini gözetmedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki kişi arasındaki yakınlık, içten ve doğru bir sevgi inancına dayanır."},{"facet_id":"F002","role":"extension","statement":"Bu bağ, arkadaş olma, karşılıklı dostluk ve içten öğüt verme davranışlarında görünür."}],"identity_rationale":"Kaynak ifadesi arkadaşlığı içten ve doğru sevgiye dayandırır, arkadaş olma ve yakın dostluk anlamlarını açıkça bir araya getirir. Verilen çerçeve, yalnızca doğru sözlü kişi anlamını dışarıda bıraktığı için dal sınırını da doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"dost veya yakın arkadaş"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"içten sevgiye dayalı arkadaşlık ve dostluk kurma"}],"lexicalization_note":"Dal yalın arkadaşlık ve dost olma alanını tanımlar; başka dallardaki söz doğruluğu, maddi verme veya özel yapılara bağlı anlamlar buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler en yakın iki sevgi ve arkadaşlık çekirdeğini, ardından ilişkinin bozulduğu karşıt kutbu gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta sevginin içten doğruluğu belirleyicidir; komşuda ruhsal yakınlık ve farklı yakın ilişki türleri daha geniş yer tutar.","focus_only":"Odak dalı sevginin doğru, içten ve iyi niyetli oluşunu kurucu koşul sayar.","gloss":"içten dostluk ve gönüle işleyen yakınlık","neighbor_only":"Komşu dal sevginin kişinin içine işlemesini ve arkadaş, sevgili ya da yoldaş ilişkisini daha geniş biçimde kapsar.","neighbor_ref":"root_000435/B003","relation_type":"near_synonym","shared_zone":"İki dal yakın sevgi, arkadaşlık ve dost olma alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak arkadaşlık bağını adlandırır; komşu sevginin arılığı ile özel yakınlar topluluğuna kadar genişler.","focus_only":"Odak dalı belirli bir dostluk ilişkisini ve dost olma davranışını kapsar.","gloss":"içten dostluk ve arı sevgi yakınlığı","neighbor_only":"Komşu dal yakın çevreyi, seçkin yakınları ve ilişkide arınmış sevgi niteliğini de kapsar.","neighbor_ref":"root_000430/B007","relation_type":"near_synonym","shared_zone":"Her iki dal içten, arı ve yakın sevgiye dayanan ilişkileri anlatır."},{"boundary_match":"opposed","distinction":"Odak yakınlık ve bağlılığın olumlu kutbudur; komşu uzaklaşma ve kötü davranışla bu bağın olumsuz kutbunu temsil eder.","focus_only":"Odak dalı yakınlık, içten sevgi ve iyi niyetli bağlılık kurar.","gloss":"içten dostluk ve ilişkide uzaklaşma","neighbor_only":"Komşu dal ilişkiyi kesme, kaba davranma ve kötü geçinmeyle yakınlığı zedeler.","neighbor_ref":"root_000251/B002","relation_type":"polarity_pair","shared_zone":"İki dal insanlar arasındaki ilişkinin niteliği ve sürdürülmesi eksenindedir."}],"source_phrase_ar":"الصداقة مشتقة من الصدق في المودة (maqayis)؛ الصداقة مصدر الصديق (ayn;tahdhib)؛ الصداقة والمصادقة المخالة (sihah)؛ الصداقة صدق الاعتقاد في المودة (mufradat)","source_summary":"Ortak açıklama, yakın arkadaşlığı içten ve doğru sevgi inancına bağlar; arkadaş olma, dostluk kurma ve iyi niyetli bağlılık bu çekirdeğin görünüşleridir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الصداقة والمصادقة والصديق بمعنى الخليل، وصدق الاعتقاد في المودة والنصيحة","what_is_not_ar":"لا يدخل فيه الصديق بمعنى كثير الصدق أو المصدق بكل أمر"},"support_links":[]},{"boundary":"Veren ve toplayan kişi adları çekirdeğin katılımcı türevleridir; evlilikte kadına verilen özel mal ve genel yoksulluk bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000852/B006","candidate_links":[{"candidate_id":"cand_adb33c8ee67d98f9ab57","lane":"macro"},{"candidate_id":"cand_4ca18a4b98db24b52d22","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"صَدَّقَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Sad~aqa|ROOT:Sdq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:6:1:2","qac_word_ref":"92:6:1","surface_ar":"صَدَّقَ"}],"gloss":"mal vererek yardım etme veya haktan vazgeçme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi kendi malından iyilik ve manevi yakınlaşma amacıyla bir pay çıkarıp verir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin kendi hakkından bağışlayarak vazgeçmesi de mali yardım gibi değerlendirilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yardımı veren kimse, verme eylemindeki katılımcı olarak ayrıca adlandırılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Hayvanlara ilişkin yardım paylarını alan veya toplayan görevli, verme eyleminden farklı bir katılımcıdır."}}],"root_ar":"ص د ق","root_id":"root_000852","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maldan iyilik amacıyla pay verme ile bir hakkı bağışlayarak bırakma biçimlerini ortak bir karşılıkta tutar.","boundary_detail":"Veren ve toplayan kişi adları çekirdeğin katılımcı türevleridir; evlilikte kadına verilen özel mal ve genel yoksulluk bu dala girmez.","branch_image_ar":"صدقة المال والحق","concept_gloss":"mal vererek yardım etme veya haktan vazgeçme","contextual_glosses":[{"applicability":"Bir kimsenin malından gönüllü veya belirlenmiş bir pay çıkarıp ihtiyaç sahibine verdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir haktan bağışlayarak vazgeçme ve katılımcı adlarını kapsamaz.","preserves":"Maldan pay çıkarıp iyilik amacıyla verme çekirdeğini korur."},"facet_ids":["F001"],"text":"iyilik amacıyla mali yardım","usage_role":"contextual"},{"applicability":"Bir kimse alacağı veya başka bir hakkı karşılık beklemeden bıraktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Maldan doğrudan yardım verme ile veren ve toplayan kişi adlarını kapsamaz.","preserves":"Kişinin kendi hakkından bağışlayarak vazgeçmesi yönünü korur."},"facet_ids":["F002"],"text":"hakkını bağışlayarak bırakma","usage_role":"contextual"}],"definition":"Bir kimsenin iyilik ve manevi yakınlaşma amacıyla malından çıkarıp verdiği yardım veya kendi hakkından bağışlayarak vazgeçmesidir. Alan ayrıca yardımı veren kişiyi ve hayvanlara ilişkin yardım paylarını toplayan görevliyi belirten türev kullanımları kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi kendi malından iyilik ve manevi yakınlaşma amacıyla bir pay çıkarıp verir."},{"facet_id":"F002","role":"extension","statement":"Kişinin kendi hakkından bağışlayarak vazgeçmesi de mali yardım gibi değerlendirilir."},{"facet_id":"F003","role":"associated_use","statement":"Yardımı veren kimse, verme eylemindeki katılımcı olarak ayrıca adlandırılır."},{"facet_id":"F004","role":"associated_use","statement":"Hayvanlara ilişkin yardım paylarını alan veya toplayan görevli, verme eyleminden farklı bir katılımcıdır."}],"identity_rationale":"Kaynak ifadesi iyilik amacıyla maldan çıkarılan yardımı, kişinin bir hakkından vazgeçmesini, yardımı vereni ve hayvanlara ilişkin payları toplayan görevliyi kapsar. Geçici çerçevenin her türlü zorunlu hakkı niyet koşuluyla bu dala katması kanıtta açık değildir; tanım, mali yardım ve haktan bağışlayarak vazgeçme çekirdeğiyle sınırlandırılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"iyilik amacıyla maldan verilen yardım veya bu adla anılan yükümlü pay"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir hakkından bağışlayarak vazgeçmek"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"mali yardım veren kimse"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"hayvanlara ilişkin yardım paylarını toplayan görevli"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"mali yardım veren erkekler ve kadınlar"}],"lexicalization_note":"Yalın mali yardım anlamı temel alınır; bir haktan vazgeçme yapısı ile veren ve toplayan kişi adları ayrı, yapıya bağlı yüzler olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlananlar genel mal vermeyi, vermeme karşıtlığını, kalıcı mal ayırmayı ve isteyene herhangi bir şey vermeyi bu dalın sınırından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak belirli bir iyilik amacı ve hak bağlamı taşır; komşu ise mal vermenin daha genel ve amaç bakımından sınırsız adıdır.","focus_only":"Odak, vermeyi iyilik ve manevi yakınlaşma amacıyla sınırlar; haktan vazgeçmeyi ve veren ile toplayan katılımcıları da kapsar.","gloss":"amaçlı mali yardım ve genel mal verme","neighbor_only":"Komşu, amaç veya hak niteliği aramadan herhangi bir malın başkasına sunulmasını anlatır.","neighbor_ref":"root_000908/B009","relation_type":"near_synonym","shared_zone":"İki dal malın bir kişiden başka birine verilmesi alanında örtüşür."},{"boundary_match":"opposed","distinction":"Odak verme ve bırakmanın olumlu kutbudur; komşu ise malı veya gerekli hakkı tutmanın karşıt kutbunu temsil eder.","focus_only":"Odak dalı maldan pay verme veya bir hakkı başkası yararına bırakma yönünü taşır.","gloss":"mali yardım ve vermekten kaçınma","neighbor_only":"Komşu dal vermekten kaçınma, iyiliği azaltma ve ödenmesi gereken hakkı tutma yönünü taşır.","neighbor_ref":"root_000258/B003","relation_type":"polarity_pair","shared_zone":"İki dal kişinin mal veya hak karşısındaki verme tutumunu değerlendirir."},{"boundary_match":"partial","distinction":"Odak doğrudan verilen pay veya bırakılan haktır; komşu malın kendisini elden çıkarmadan kullanımını kalıcı biçimde ayırır.","focus_only":"Odak maldan pay verme, haktan vazgeçme ve bu işlemdeki katılımcıları kapsar.","gloss":"mali yardım ve kalıcı taşınmaz ayırma","neighbor_only":"Komşu bir taşınmazı sürekli olarak yoksulların yararına bağlayıp kullanımını kalıcılaştırır.","neighbor_ref":"root_001676/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal malı ihtiyaç sahiplerinin yararına özgüleme alanındadır."},{"boundary_match":"partial","distinction":"Odak mali ve hak temelli bir yardım türüdür; komşu verilen şeyin niteliğini ve verme amacını belirlemez.","focus_only":"Odak iyilik amacı, maldan ayrılan pay, haktan vazgeçme ve katılımcı rolleriyle daha belirli bir alandır.","gloss":"mali yardım ve isteyene bir şey verme","neighbor_only":"Komşu yalnızca isteyen kişiye herhangi bir şey verilmesi eylemini bildirir.","neighbor_ref":"root_001417/B005","relation_type":"near_neighbor","shared_zone":"İki dal ihtiyaç belirten bir kişiye bir şey verme durumunda buluşabilir."}],"source_phrase_ar":"الصدقة ما يتصدق به المرء عن نفسه وماله (maqayis)؛ المتصدق المعطي للصدقة (ayn;sihah;tahdhib)؛ المصدق الذي يأخذ صدقات الغنم (maqayis;sihah;tahdhib)؛ الصدقة ما يخرجه الإنسان من ماله على وجه القربة (mufradat)؛ من تجافى عنه (mufradat)","source_summary":"Ortak kanıt maldan iyilik amacıyla verilen yardımı çekirdek sayar; haktan bağışlayarak vazgeçmeyi buna benzetir ve veren kişiyle hayvan paylarını toplayan görevliyi ayrı katılımcılar olarak gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الصدقة وما يتصدق به من المال، والزكاة أو الواجب إذا تحرى صاحبه الصدق، وتجافي الإنسان عن حقه، والمتصدق المعطي، والمصدق آخذ الصدقات","what_is_not_ar":"لا يدخل فيه صداق المرأة ولا قول العامة في السائل إذا أنكره أهل اللغة"},"support_links":["sup_01d18329256677ad3251","sup_637938be856a819cfc5f"]},{"boundary":"Bu mal evlilik ilişkisinde kadına ait özel bir haktır; yoksula verilen yardım, düğün armağanı veya evliliğin kendisiyle özdeş değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000852/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صَدَّقَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Sad~aqa|ROOT:Sdq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:6:1:2","qac_word_ref":"92:6:1","surface_ar":"صَدَّقَ"}],"gloss":"kadına belirlenen evlilik hakkı olan mal","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Evlilikte kadına özel hak olarak bir mal verilir veya belirlenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı evlilik malı farklı ad biçimleriyle ve kadınlara bağlanan yapılarda ifade edilebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kadın için bu evlilik malını belirlemek veya ayırmak ilgili eylem anlamıdır."}}],"root_ar":"ص د ق","root_id":"root_000852","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Evlilik kurulurken kadına ait olacak biçimde verilen veya belirlenen özel malı tam olarak anlatır.","boundary_detail":"Bu mal evlilik ilişkisinde kadına ait özel bir haktır; yoksula verilen yardım, düğün armağanı veya evliliğin kendisiyle özdeş değildir.","branch_image_ar":"صداق المرأة","concept_gloss":"kadına belirlenen evlilik hakkı olan mal","contextual_glosses":[{"applicability":"Özel terim yerine işlemin açıkça anlatıldığı ve malın gerçekten verildiği evlilik bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Malın yalnızca belirlenmiş olup henüz verilmemiş olabileceği durumu açıkça kapsamaz.","preserves":"Evlilik bağlamını, kadın katılımcıyı ve verilen malı korur."},"facet_ids":["F001"],"text":"evlenirken kadına verilen mal","usage_role":"contextual"},{"applicability":"Bir erkeğin evleneceği kadın için ona ait olacak malı adlandırması veya ayırması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Belirlenen malın ad olarak kullanılması ve biçim çeşitleri bu karşılıkta yer almaz.","preserves":"Kadın için evlilik malını belirleme eylemini korur."},"facet_ids":["F003"],"text":"kadına evlilik hakkı belirleme","usage_role":"contextual"}],"definition":"Evlilik kurulurken kadına hakkı olarak verilen veya onun için belirlenen maldır. İlgili eylem, bu malı kadın için adlandırmayı ya da ayırmayı ifade eder.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Evlilikte kadına özel hak olarak bir mal verilir veya belirlenir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı evlilik malı farklı ad biçimleriyle ve kadınlara bağlanan yapılarda ifade edilebilir."},{"facet_id":"F003","role":"associated_use","statement":"Kadın için bu evlilik malını belirlemek veya ayırmak ilgili eylem anlamıdır."}],"identity_rationale":"Kaynak ifadesinin bütün bölümleri, evlilik sırasında kadına verilen veya onun için belirlenen özel malı ve bu anlamdaki biçim çeşitlerini gösterir. Dalın evlilik hakkı çerçevesi, genel mali yardım ya da arkadaşlık anlamlarını dışarıda bırakarak kanıtı doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kadına verilen veya belirlenen evlilik hakkı olan mal"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"kadının evlilikte aldığı mal veya kadınlara ait bu tür mallar"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kadına evlilik hakkı olarak mal belirlemek"}],"lexicalization_note":"Yalın ad kadının evlilik hakkı olan malı belirtir; kadına bu malı belirleme eylemi ve kadınlarla kurulan ad yapıları kendi yapısal sınırlarında korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler malın belirlenmemesiyle karşıtlığı, düğün armağanıyla yakın karışmayı ve evlenme olayının yalnızca tematik bağını açıklar.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak malın varlığını ve belirlenmesini, komşu ise evlilik sırasında bu belirlemenin yapılmamasını temsil eder.","focus_only":"Odak dalında kadın için evlilik hakkı olan mal verilir veya belirlenir.","gloss":"evlilik malının belirlenmesi ve belirlenmemesi","neighbor_only":"Komşu dalda evlilik kurulur fakat kadın için bu mal başlangıçta belirlenmez.","neighbor_ref":"root_001187/B004","relation_type":"polarity_pair","shared_zone":"İki dal evlilik kurulurken kadına ait özel malın belirlenip belirlenmemesi eksenindedir."},{"boundary_match":"partial","distinction":"Odaktaki mal evliliğe bağlı özel haktır; komşudaki armağan ise farklı bir tören ve verme vesilesine bağlıdır.","focus_only":"Odak malı kadının evlilikten doğan özel hakkı olarak kurar.","gloss":"evlilik hakkı olan mal ve düğün armağanı","neighbor_only":"Komşu dal gelinin görünmesi veya düğün töreni sırasında verilen ayrı bir armağanı anlatır.","neighbor_ref":"root_000256/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal evlilik çevresinde kadına veya geline verilen bir malı konu edinir."},{"boundary_match":"thematic_only","distinction":"Odak süreç içindeki belirli bir mal ve haktır; komşu ise evlenme ve düğün olayının kendisidir.","focus_only":"Odak yalnızca kadına verilen veya onun için belirlenen özel evlilik malını anlatır.","gloss":"evlilik hakkı olan mal ve evlenme olayı","neighbor_only":"Komşu evlenme, düğün yapma ve eşle birlikte yeni eve girme olayının bütününü anlatır.","neighbor_ref":"root_000166/B010","relation_type":"thematic","shared_zone":"İki dal aynı evlilik sürecinin farklı unsurlarında yer alır."}],"source_phrase_ar":"الصداق صداق المرأة (maqayis)؛ الصداق والصدقة والصدقة المهر (ayn)؛ الصداق والصداق مهر المرأة (sihah)؛ صداق المرأة وصدقة المرأة (tahdhib)؛ صداق المرأة وصداقها وصدقتها ما تعطى من مهرها (mufradat)","source_summary":"Ortak kanıt, evlilikte kadına verilen veya onun için belirlenen özel malı gösterir; adın çeşitli biçimlerini ve bu malı kadın için belirleme eylemini aynı alan içinde tutar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الصداق والصداق وصدقة المرأة وصدقات النساء بمعنى المهر","what_is_not_ar":"لا يدخل فيه صدقة الفقراء ولا الصداقة بين الأصحاب"},"support_links":[]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000058/B004","candidate_links":[{"candidate_id":"cand_8c19034e036d24c69fd0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_473093bc2ce70b804a8a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Easy fertile earth supplies a receptive and generative counter-pole rather than mere softness.","root":"ء ن ث","source_ref":"92:3","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000058","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bf1ed743df9188d14f17"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000256/B001","candidate_links":[{"candidate_id":"cand_1f91fa6f782358926eb0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3fe986d1c8aa3d257e8d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Disclosure and appearance supply the phase in which the prior alignment becomes inspectable.","root":"ج ل و","source_ref":"92:2","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000256","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1831385efe2952ea96d9"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000434/B001","candidate_links":[{"candidate_id":"cand_9fb83b332639e8e6b985","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_54eccc45e9f064a8b552","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Measuring and proportioning supply an ordered field rather than undifferentiated motion.","root":"خ ل ق","source_ref":"92:3","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000434","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_fd04a692af9b1a277c30"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000516/B002","candidate_links":[{"candidate_id":"cand_8c19034e036d24c69fd0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_473093bc2ce70b804a8a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The male branch's hardness and sharpness externalize the hard pole activated near focus-level solidity.","root":"ذ ك ر","source_ref":"92:3","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000516","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bf1ed743df9188d14f17"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000558/B003","candidate_links":[{"candidate_id":"cand_4ca18a4b98db24b52d22","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_64c8d4190ac635e7e000","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Falling into destruction supplies the terminal load-test under which retained wealth cannot suffice.","root":"ر د ي","source_ref":"92:11","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000558","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_01d18329256677ad3251"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000709/B001","candidate_links":[{"candidate_id":"cand_9fb83b332639e8e6b985","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_54eccc45e9f064a8b552","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Purposeful movement toward an object supplies directed human motion within that field.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000709","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_fd04a692af9b1a277c30"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000775/B001","candidate_links":[{"candidate_id":"cand_9fb83b332639e8e6b985","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_54eccc45e9f064a8b552","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Dispersion supplies the competing possibility that purposeful movements diverge.","root":"ش ت ت","source_ref":"92:4","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000775","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_fd04a692af9b1a277c30"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001012/B001","candidate_links":[{"candidate_id":"cand_ba95413c78d0046d8fac","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e1618fcd2c03b84c6d54","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Difficulty and severity supply the constricted destination paired with denial.","root":"ع س ر","source_ref":"92:10","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001012","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_cab23a87d0f55bd398de"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001028/B002","candidate_links":[{"candidate_id":"cand_adb33c8ee67d98f9ab57","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7bb187ebc1c1228f091f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Handing something over supplies the outward transfer that realizes beneficence.","root":"ع ط و","source_ref":"92:5","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001028","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_637938be856a819cfc5f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001088/B001","candidate_links":[{"candidate_id":"cand_1f91fa6f782358926eb0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3fe986d1c8aa3d257e8d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A covering that rises over and hides supplies the low-visibility phase of the test.","root":"غ ش و","source_ref":"92:1","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001088","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1831385efe2952ea96d9"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001110/B002","candidate_links":[{"candidate_id":"cand_4ca18a4b98db24b52d22","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_64c8d4190ac635e7e000","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Sufficiency supplies the rescue-function that wealth is asked, and fails, to perform.","root":"غ ن ي","source_ref":"92:11","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001110","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_01d18329256677ad3251"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001290/B001","candidate_links":[{"candidate_id":"cand_ba95413c78d0046d8fac","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e1618fcd2c03b84c6d54","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Falsehood as the contrary of truth supplies the explicit negative pole.","root":"ك ذ ب","source_ref":"92:9","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001290","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_cab23a87d0f55bd398de"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001457/B001","candidate_links":[{"candidate_id":"cand_4ca18a4b98db24b52d22","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_64c8d4190ac635e7e000","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Acquiring and accumulating property supplies the retained mass whose adequacy is tested.","root":"م و ل","source_ref":"92:11","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001457","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_01d18329256677ad3251"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001677/B002","candidate_links":[{"candidate_id":"cand_adb33c8ee67d98f9ab57","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7bb187ebc1c1228f091f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Placing the self within protection supplies disciplined restraint alongside outward giving.","root":"و ق ي","source_ref":"92:5","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001677","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_637938be856a819cfc5f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001694/B001","candidate_links":[{"candidate_id":"cand_8cb4c31ff4b86f2ef0fc","lane":"macro"},{"candidate_id":"cand_ba95413c78d0046d8fac","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_432465a79b56b15e944c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Opening and ease after difficulty supply the route's newly traversable condition.","root":"ي س ر","source_ref":"92:7","source_word_indices":["1","2"]},{"hft_ref":"hft_e1618fcd2c03b84c6d54","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Facilitation retains the opening mechanism but now governs the opposite destination.","root":"ي س ر","source_ref":"92:10","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001694","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_cab23a87d0f55bd398de","sup_e742769a22f6b10ad063"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001694/B005","candidate_links":[{"candidate_id":"cand_8cb4c31ff4b86f2ef0fc","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_432465a79b56b15e944c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Lightness and compliance in motion supply the felt mechanics of facilitation.","root":"ي س ر","source_ref":"92:7","source_word_indices":["1","2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001694","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_e742769a22f6b10ad063"]}],"candidate_inventory":[{"anchor_refs":["92:1","92:2","92:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:6","branch_refs":["root_000256/B001","root_000323/B001","root_000852/B001","root_001088/B001"],"candidate_id":"cand_1f91fa6f782358926eb0","commentary_obligation":"review","hft_ref":"hft_3fe986d1c8aa3d257e8d","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d92_1_2_visibility_test","source_type":"hft","support_ids":["sup_1831385efe2952ea96d9"],"title":"d92_1_2_visibility_test","trust":"legacy_unbound"},{"anchor_refs":["92:3","92:4","92:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:6","branch_refs":["root_000323/B005","root_000434/B001","root_000709/B001","root_000775/B001","root_000852/B002"],"candidate_id":"cand_9fb83b332639e8e6b985","commentary_obligation":"review","hft_ref":"hft_54eccc45e9f064a8b552","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d92_3_4_measured_trajectory","source_type":"hft","support_ids":["sup_fd04a692af9b1a277c30"],"title":"d92_3_4_measured_trajectory","trust":"legacy_unbound"},{"anchor_refs":["92:5","92:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:6","branch_refs":["root_000323/B002","root_000852/B004","root_000852/B006","root_001028/B002","root_001677/B002"],"candidate_id":"cand_adb33c8ee67d98f9ab57","commentary_obligation":"review","hft_ref":"hft_7bb187ebc1c1228f091f","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d92_5_giving_verifies","source_type":"hft","support_ids":["sup_637938be856a819cfc5f"],"title":"d92_5_giving_verifies","trust":"legacy_unbound"},{"anchor_refs":["92:6","92:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:6","branch_refs":["root_000323/B005","root_000852/B002","root_001694/B001","root_001694/B005"],"candidate_id":"cand_8cb4c31ff4b86f2ef0fc","commentary_obligation":"review","hft_ref":"hft_432465a79b56b15e944c","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d92_7_path_made_pliant","source_type":"hft","support_ids":["sup_e742769a22f6b10ad063"],"title":"d92_7_path_made_pliant","trust":"legacy_unbound"},{"anchor_refs":["92:10","92:6","92:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:6","branch_refs":["root_000323/B001","root_000852/B001","root_001012/B001","root_001290/B001","root_001694/B001"],"candidate_id":"cand_ba95413c78d0046d8fac","commentary_obligation":"review","hft_ref":"hft_e1618fcd2c03b84c6d54","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d92_8_10_mirrored_feedback","source_type":"hft","support_ids":["sup_cab23a87d0f55bd398de"],"title":"d92_8_10_mirrored_feedback","trust":"legacy_unbound"},{"anchor_refs":["92:11","92:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:6","branch_refs":["root_000323/B002","root_000558/B003","root_000852/B006","root_001110/B002","root_001457/B001"],"candidate_id":"cand_4ca18a4b98db24b52d22","commentary_obligation":"review","hft_ref":"hft_64c8d4190ac635e7e000","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d92_11_wealth_as_failed_ballast","source_type":"hft","support_ids":["sup_01d18329256677ad3251"],"title":"d92_11_wealth_as_failed_ballast","trust":"legacy_unbound"},{"anchor_refs":["92:3","92:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:6","branch_refs":["root_000058/B004","root_000323/B002","root_000516/B002","root_000852/B002"],"candidate_id":"cand_8c19034e036d24c69fd0","commentary_obligation":"review","hft_ref":"hft_473093bc2ce70b804a8a","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o92_3_firmness_fertility_coupling","source_type":"hft","support_ids":["sup_bf1ed743df9188d14f17"],"title":"o92_3_firmness_fertility_coupling","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_d495c9432bd42fe28a77","connection_ref":"conn_f3613974c647106b9559","note":"Immediate counter-reading: denying the same value opposes giving-linked confirmation.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_7f5a650df60ac4dc7b64","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:9","source_note":"Direct positive counterpart: affirming al-husna within the giving sequence.","source_row_role":"ranked_review","source_target_component_ref":"92:6","source_target_components":["92:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:6"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:9","source_target_components":["92:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:9","target_evidence":{"arabic_uthmani":"وَكَذَّبَ بِٱلْحُسْنَىٰ","ayah_ref":"92:9"},"target_ref":"92:9"},{"connection_evidence_ref":"conn_ev_6ed2b4ba0d776324bd16","connection_ref":"conn_1e72100680277e6cac0f","note":"Nearby creation pair belongs to the oath sequence but adds little to 92:6 itself.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_e6d3bc89cbfc093cbcd0","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"92:3","source_note":"The nearby confirmation pole helps connect the opening distinctions to the surah's ensuing ethical paths.","source_row_role":"ranked_review","source_target_component_ref":"92:6","source_target_components":["92:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:6"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:3","source_target_components":["92:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:3","target_evidence":{"arabic_uthmani":"وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ","ayah_ref":"92:3"},"target_ref":"92:3"},{"connection_evidence_ref":"conn_ev_99501e5e188957be2890","connection_ref":"conn_9db6645833e35ac84324","note":"Immediate warning that wealth fails provides the counter-model to the giving path.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_c161ad18022e491d69d4","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"92:11","source_note":"Local affirmation belongs to the opposed, eased path.","source_row_role":"ranked_review","source_target_component_ref":"92:6","source_target_components":["92:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:6"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:11","source_target_components":["92:11"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:11","target_evidence":{"arabic_uthmani":"وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ","ayah_ref":"92:11"},"target_ref":"92:11"},{"connection_evidence_ref":"conn_ev_82fac7cbb8acaabd83c3","connection_ref":"conn_0e21507455248c108a70","note":"Immediate miserly self-sufficiency is the principal counter-pattern to 92:5-6.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_497362bb4ebdb6169290","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:8","source_note":"Affirming the husna is the immediate positive counterpart to 92:9 and its preceding stance.","source_row_role":"ranked_review","source_target_component_ref":"92:6","source_target_components":["92:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:6"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:8","source_target_components":["92:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:8","target_evidence":{"arabic_uthmani":"وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ","ayah_ref":"92:8"},"target_ref":"92:8"},{"connection_evidence_ref":"conn_ev_a166aad3a1a6df30b1f2","connection_ref":"conn_8c0f1cf9dc0dbd8b5daf","note":"Immediate antecedent: giving and taqwa frame the confirmation in 92:6.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_e687ed3c7c4237d12f93","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:5","source_note":"Immediate continuation: affirming al-husna completes the described course.","source_row_role":"ranked_review","source_target_component_ref":"92:6","source_target_components":["92:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:6"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:5","source_target_components":["92:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:5","target_evidence":{"arabic_uthmani":"فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ","ayah_ref":"92:5"},"target_ref":"92:5"},{"connection_evidence_ref":"conn_ev_a64f19929c54a8cb292c","connection_ref":"conn_cddb9070289cc939cc3d","note":"Immediate plurality of striving establishes the choice space for the following confirmation.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_40131f06ea927b44f426","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:4","source_note":"Affirming al-husna completes the positive branch's orientation.","source_row_role":"ranked_review","source_target_component_ref":"92:6","source_target_components":["92:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:6"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:4","source_target_components":["92:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:4","target_evidence":{"arabic_uthmani":"إِنَّ سَعْيَكُمْ لَشَتَّىٰ","ayah_ref":"92:4"},"target_ref":"92:4"},{"connection_evidence_ref":"conn_ev_abefa4822081e8c32a67","connection_ref":"conn_ae477ee30f94c7186e8b","note":"No material connection to confirmation or al-husna is supplied.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_57a709115d20c8d44026","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"92:2","source_note":"Confirms the good in the favorable route, but largely repeats the preceding local pattern.","source_row_role":"ranked_review","source_target_component_ref":"92:6","source_target_components":["92:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:6"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"92:2","source_target_components":["92:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:2","target_evidence":{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا تَجَلَّىٰ","ayah_ref":"92:2"},"target_ref":"92:2"},{"connection_evidence_ref":"conn_ev_45f31e942563140d707a","connection_ref":"conn_3cc02e45804b008af979","note":"The immediate consequence of giving, taqwa, and confirmation supplies the positive path's promised facilitation.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":true,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_030b31e820f850f7b777","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:7","source_note":"Tasdiq of al-husna is the missing immediate antecedent to 92:7.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"92:6","source_target_components":["92:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:6"}],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"92:7","source_target_components":["92:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:7","target_evidence":{"arabic_uthmani":"فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ","ayah_ref":"92:7"},"target_ref":"92:7"},{"connection_evidence_ref":"conn_ev_b1777f01918f3b4d56e0","connection_ref":"conn_40c588132aa215b35ad4","note":"The immediate counterpart shows that denying al-husna is followed by facilitation toward hardship.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":true,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_f5867731bb6c8fe3e620","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"92:10","source_note":"Immediate positive counterpart: affirmation of al-husna precedes preparation toward al-yusra.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"92:6","source_target_components":["92:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:6"}],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"92:10","source_target_components":["92:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:10","target_evidence":{"arabic_uthmani":"فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ","ayah_ref":"92:10"},"target_ref":"92:10"}],"focus":{"arabic_uthmani":"وَصَدَّقَ بِٱلْحُسْنَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:6:1:1","qac_word_ref":"92:6:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"صَدَّقَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Sad~aqa|ROOT:Sdq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:6:1:2","qac_word_ref":"92:6:1","root_ar":"ص د ق","surface_ar":"صَدَّقَ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"92:6:2:1","qac_word_ref":"92:6:2","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"92:6:2:2","qac_word_ref":"92:6:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"حُسْنَىٰ","morph_features":"STEM|POS:N|LEM:HusonaY`|ROOT:Hsn|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:6:2:3","qac_word_ref":"92:6:2","root_ar":"ح س ن","surface_ar":"حُسْنَىٰ"}],"word_analysis_qac_refs":[["92:6:1:1"],["92:6:1:2"],["92:6:2:1"],["92:6:2:2","92:6:2:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["92:6:1","92:6:2","92:6:3","92:6:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَصَدَّقَ بِٱلْحُسْنَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:6:1:1","qac_word_ref":"92:6:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"صَدَّقَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Sad~aqa|ROOT:Sdq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:6:1:2","qac_word_ref":"92:6:1","root_ar":"ص د ق","surface_ar":"صَدَّقَ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"92:6:2:1","qac_word_ref":"92:6:2","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"92:6:2:2","qac_word_ref":"92:6:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"حُسْنَىٰ","morph_features":"STEM|POS:N|LEM:HusonaY`|ROOT:Hsn|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:6:2:3","qac_word_ref":"92:6:2","root_ar":"ح س ن","surface_ar":"حُسْنَىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["92:6:1:1"],["92:6:1:2"],["92:6:2:1"],["92:6:2:2","92:6:2:3"]],"word_analysis_refs":["92:6:1","92:6:2","92:6:3","92:6:4"],"word_rows":[{"analysis_record_ref":"92:6:1","analytic_gloss_range_en":"coordinating conjunction that carries the positive branch from 92:5 forward instead of closing it","analytic_root_gloss_range_en":null,"qac_refs":["92:6:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"92:6:2","analytic_gloss_range_en":"Form II perfect active confirmation or validation, locally taking a bi-governed object and sharing the subject from 92:5","analytic_root_gloss_range_en":"truthfulness, confirmation, fulfillment, sincere relation, charity, and pledge-gift branches; the local verb selects active confirmation while nearby giving lets charity and pledge language remain a narrowed undertone","qac_refs":["92:6:1:2"],"root":{"arabic":"ص د ق","transliteration":"ṣ-d-q"},"surface":{"arabic":"صَدَّقَ","transliteration":"ṣaddaqa"}},{"analysis_record_ref":"92:6:3","analytic_gloss_range_en":"preposition governing the final noun as the content or object accepted as true after the confirmation verb","analytic_root_gloss_range_en":null,"qac_refs":["92:6:2:1"],"root":{},"surface":{"arabic":"بِ","transliteration":"bi"}},{"analysis_record_ref":"92:6:4","analytic_gloss_range_en":"the definite feminine superlative object of confirmation: the known best, beautiful good, or promised best outcome, with recompense strongly pressured but not flattened to one noun","analytic_root_gloss_range_en":"goodness, beauty, beneficent action, and favorable reward branches are relevant; place-name/body-part and utmost-limit branches are not locally active","qac_refs":["92:6:2:2","92:6:2:3"],"root":{"arabic":"ح س ن","transliteration":"ḥ-s-n"},"surface":{"arabic":"ٱلْحُسْنَىٰ","transliteration":"al-ḥusnā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":10,"missing_anchor_refs":[],"supplied_unique_anchor_count":10},"assigned_record_count":7,"assigned_records":[{"anchor_refs":["92:1","92:2","92:6"],"branch_refs":["root_000256/B001","root_000323/B001","root_000852/B001","root_001088/B001"],"candidate_id":"cand_1f91fa6f782358926eb0","evidence_scope":"declared_pericope","hft_ref":"hft_3fe986d1c8aa3d257e8d","item_id":"d92_1_2_visibility_test","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d92_1_2_visibility_test","support_id":"sup_1831385efe2952ea96d9"},{"anchor_refs":["92:3","92:4","92:6"],"branch_refs":["root_000323/B005","root_000434/B001","root_000709/B001","root_000775/B001","root_000852/B002"],"candidate_id":"cand_9fb83b332639e8e6b985","evidence_scope":"declared_pericope","hft_ref":"hft_54eccc45e9f064a8b552","item_id":"d92_3_4_measured_trajectory","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d92_3_4_measured_trajectory","support_id":"sup_fd04a692af9b1a277c30"},{"anchor_refs":["92:5","92:6"],"branch_refs":["root_000323/B002","root_000852/B004","root_000852/B006","root_001028/B002","root_001677/B002"],"candidate_id":"cand_adb33c8ee67d98f9ab57","evidence_scope":"declared_pericope","hft_ref":"hft_7bb187ebc1c1228f091f","item_id":"d92_5_giving_verifies","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d92_5_giving_verifies","support_id":"sup_637938be856a819cfc5f"},{"anchor_refs":["92:6","92:7"],"branch_refs":["root_000323/B005","root_000852/B002","root_001694/B001","root_001694/B005"],"candidate_id":"cand_8cb4c31ff4b86f2ef0fc","evidence_scope":"declared_pericope","hft_ref":"hft_432465a79b56b15e944c","item_id":"d92_7_path_made_pliant","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d92_7_path_made_pliant","support_id":"sup_e742769a22f6b10ad063"},{"anchor_refs":["92:10","92:6","92:9"],"branch_refs":["root_000323/B001","root_000852/B001","root_001012/B001","root_001290/B001","root_001694/B001"],"candidate_id":"cand_ba95413c78d0046d8fac","evidence_scope":"declared_pericope","hft_ref":"hft_e1618fcd2c03b84c6d54","item_id":"d92_8_10_mirrored_feedback","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d92_8_10_mirrored_feedback","support_id":"sup_cab23a87d0f55bd398de"},{"anchor_refs":["92:11","92:6"],"branch_refs":["root_000323/B002","root_000558/B003","root_000852/B006","root_001110/B002","root_001457/B001"],"candidate_id":"cand_4ca18a4b98db24b52d22","evidence_scope":"declared_pericope","hft_ref":"hft_64c8d4190ac635e7e000","item_id":"d92_11_wealth_as_failed_ballast","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d92_11_wealth_as_failed_ballast","support_id":"sup_01d18329256677ad3251"},{"anchor_refs":["92:3","92:6"],"branch_refs":["root_000058/B004","root_000323/B002","root_000516/B002","root_000852/B002"],"candidate_id":"cand_8c19034e036d24c69fd0","evidence_scope":"declared_pericope","hft_ref":"hft_473093bc2ce70b804a8a","item_id":"o92_3_firmness_fertility_coupling","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o92_3_firmness_fertility_coupling","support_id":"sup_bf1ed743df9188d14f17"}],"diagnostics":[],"lane_counts":{"global":16,"macro":7,"micro":5},"packet_summary":{"ayah_count":21,"focus_ref":"92:6","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ج ز ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000244","furuq_root_norm":"ج ز ي","furuq_source_root_norm":"ج ز ي","is_dominant":true,"target_occurrences":97,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000242","furuq_root_norm":"ج ز ز","furuq_source_root_norm":"ج ز ز","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11","92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"92:6","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":19,"unstructured_record_count":0},"identity":{"ayah_ref":"92:6","lane":"macro","linguistic_source_ref":"92:6","surface_ref":"92:6","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"92:6","target_tokens":[["ve",["92:6:1"]],["en",["92:6:2"]],["güzeli",["92:6:2"]],["doğrularsa",["92:6:1","92:6:2"]]],"text":"ve en güzeli doğrularsa,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":7,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":11,"id":"s092-p01-001-011","label":"Contrasting forms of striving","number":1,"refs":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"92:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"92:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["92:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"92:0"}],"support_registry":[{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَغْشَىٰ","ayah_ref":"92:1"},{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا تَجَلَّىٰ","ayah_ref":"92:2"},{"arabic_uthmani":"وَصَدَّقَ بِٱلْحُسْنَىٰ","ayah_ref":"92:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000256/B001","root_000323/B001","root_000852/B001","root_001088/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000852","role":"Correspondence supplies the alignment that can persist or fail when visibility changes.","root":"ص د ق","source_ref":"92:6","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000323","role":"Goodness remains the criterion being held through both phases.","root":"ح س ن","source_ref":"92:6","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001088","role":"A covering that rises over and hides supplies the low-visibility phase of the test.","root":"غ ش و","source_ref":"92:1","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000256","role":"Disclosure and appearance supply the phase in which the prior alignment becomes inspectable.","root":"ج ل و","source_ref":"92:2","source_word_indices":["3"]}],"changed_reading":{"after":"Verification is fidelity to the good across concealment and disclosure, with revelation exposing whether inward and outward alignment held.","before":"Verification is a single moment of assent to visible good."},"confidence":"medium","mechanism":"Alternating cover and disclosure turns correspondent verification into fidelity under changing visibility: concealment withholds evidence, while disclosure tests whether inner, spoken, and actual alignment endured.","model_id":"d92_1_2_visibility_test","reader_inference":"The packet supplies covering, disclosure, goodness, and correspondence; I infer that changing visibility tests rather than creates the truth of the good. A live alternative is that the pair only frames cosmic time and adds no epistemic mechanism.","status":"revised","structural_cues":["The paired oath sequence in 92:1-2 places covering and self-disclosure before the focus."],"trigger_roots":["غ ش و","ج ل و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d92_1_2_visibility_test","source_type":"hft","support_id":"sup_1831385efe2952ea96d9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ","ayah_ref":"92:3"},{"arabic_uthmani":"إِنَّ سَعْيَكُمْ لَشَتَّىٰ","ayah_ref":"92:4"},{"arabic_uthmani":"وَصَدَّقَ بِٱلْحُسْنَىٰ","ayah_ref":"92:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000323/B005","root_000434/B001","root_000709/B001","root_000775/B001","root_000852/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000852","role":"Straight solidity supplies the stabilizing geometry of the chosen trajectory.","root":"ص د ق","source_ref":"92:6","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_000323","role":"The utmost limit supplies the trajectory's bestward endpoint.","root":"ح س ن","source_ref":"92:6","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000434","role":"Measuring and proportioning supply an ordered field rather than undifferentiated motion.","root":"خ ل ق","source_ref":"92:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000709","role":"Purposeful movement toward an object supplies directed human motion within that field.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000775","role":"Dispersion supplies the competing possibility that purposeful movements diverge.","root":"ش ت ت","source_ref":"92:4","source_word_indices":["3"]}],"changed_reading":{"after":"He fixed divergent striving into a measured bestward trajectory by treating the utmost good as its orienting limit.","before":"He accepted the best as a detached object of belief."},"confidence":"medium","mechanism":"Measured formation followed by purpose-driven but divergent striving recasts focus-level firmness as selection of a trajectory: the good is the limit that prevents purposeful motion from dispersing.","model_id":"d92_3_4_measured_trajectory","reader_inference":"The packet supplies measure, goal-directed movement, divergence, straightness, and a limit; I infer that affirming the good selects and stabilizes one path through a field of possible strivings. The alternative is that creation and striving merely classify agents without making الْحُسْنَىٰ directional.","status":"new","structural_cues":["The ordered creation pair in 92:3 is followed by the declaration of divergent strivings in 92:4, then by the focus sequence."],"trigger_roots":["خ ل ق","س ع ي","ش ت ت"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d92_3_4_measured_trajectory","source_type":"hft","support_id":"sup_fd04a692af9b1a277c30","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ","ayah_ref":"92:5"},{"arabic_uthmani":"وَصَدَّقَ بِٱلْحُسْنَىٰ","ayah_ref":"92:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000323/B002","root_000852/B004","root_000852/B006","root_001028/B002","root_001677/B002"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000852","role":"Fulfillment makes confirmation answerable to completed action.","root":"ص د ق","source_ref":"92:6","source_word_indices":["1"]},{"branch_id":"B006","mapped_root_id":"root_000852","role":"Charity and relinquished right make giving a root-internal form of verification.","root":"ص د ق","source_ref":"92:6","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000323","role":"Beneficent action identifies the enacted quality of the good.","root":"ح س ن","source_ref":"92:6","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001028","role":"Handing something over supplies the outward transfer that realizes beneficence.","root":"ع ط و","source_ref":"92:5","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001677","role":"Placing the self within protection supplies disciplined restraint alongside outward giving.","root":"و ق ي","source_ref":"92:5","source_word_indices":["4"]}],"changed_reading":{"after":"His giving and restraint perform the endorsement: he makes the good credible by transferring benefit and governing exposure to harm.","before":"He mentally endorsed the good after separately giving and guarding himself."},"confidence":"strong","mechanism":"Giving and self-protective restraint immediately operationalize fulfillment and beneficence: confirmation is evidenced by what leaves the hand and by what the self refuses to expose to harm.","model_id":"d92_5_giving_verifies","reader_inference":"The packet supplies transfer, self-protection, fulfillment, charity, and beneficent action; I infer that the preceding coordinated acts are the mode and evidence of confirmation. A live alternative keeps giving, restraint, and belief as three adjacent but independent virtues.","status":"strengthened","structural_cues":["The coordinated perfect verbs of 92:5 lead directly into the coordinated perfect verb صَدَّقَ in 92:6."],"trigger_roots":["ع ط و","و ق ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d92_5_giving_verifies","source_type":"hft","support_id":"sup_637938be856a819cfc5f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَصَدَّقَ بِٱلْحُسْنَىٰ","ayah_ref":"92:6"},{"arabic_uthmani":"فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ","ayah_ref":"92:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000323/B005","root_000852/B002","root_001694/B001","root_001694/B005"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000852","role":"Straight firmness supplies a stable bearing before movement is eased.","root":"ص د ق","source_ref":"92:6","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_000323","role":"The utmost good supplies the limit toward which the route runs.","root":"ح س ن","source_ref":"92:6","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001694","role":"Opening and ease after difficulty supply the route's newly traversable condition.","root":"ي س ر","source_ref":"92:7","source_word_indices":["1","2"]},{"branch_id":"B005","mapped_root_id":"root_001694","role":"Lightness and compliance in motion supply the felt mechanics of facilitation.","root":"ي س ر","source_ref":"92:7","source_word_indices":["1","2"]}],"changed_reading":{"after":"He took a firm bestward bearing, and that alignment became the threshold at which the route opened and motion grew compliant.","before":"He affirmed a promised ease as an object."},"confidence":"medium","mechanism":"The firm bestward bearing of the focus is answered by an opening and a light, compliant motion; confirmation is not arrival but the alignment after which a route becomes traversable.","model_id":"d92_7_path_made_pliant","reader_inference":"The packet supplies firm orientation, an utmost limit, opening, and compliant movement; the result construction supports my inference that focus-level alignment enables traversability. The alternative is external reward: the path is eased after confirmation but is not mechanically shaped by it.","status":"revised","structural_cues":["The result clause فَسَنُيَسِّرُهُ immediately follows 92:6 and repeats the ي س ر root in both the facilitating verb and destination."],"trigger_roots":["ي س ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d92_7_path_made_pliant","source_type":"hft","support_id":"sup_e742769a22f6b10ad063","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ","ayah_ref":"92:10"},{"arabic_uthmani":"وَصَدَّقَ بِٱلْحُسْنَىٰ","ayah_ref":"92:6"},{"arabic_uthmani":"وَكَذَّبَ بِٱلْحُسْنَىٰ","ayah_ref":"92:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000323/B001","root_000852/B001","root_001012/B001","root_001290/B001","root_001694/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000852","role":"Truth as the contrary of lying supplies one pole of the mirrored stance.","root":"ص د ق","source_ref":"92:6","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001290","role":"Falsehood as the contrary of truth supplies the explicit negative pole.","root":"ك ذ ب","source_ref":"92:9","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000323","role":"The repeated goodness branch holds the object constant while the stance reverses.","root":"ح س ن","source_ref":"92:9","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001694","role":"Facilitation retains the opening mechanism but now governs the opposite destination.","root":"ي س ر","source_ref":"92:10","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001012","role":"Difficulty and severity supply the constricted destination paired with denial.","root":"ع س ر","source_ref":"92:10","source_word_indices":["2"]}],"changed_reading":{"after":"Confirmation and denial are rival path-making postures: each relation to the same good progressively opens one mode of movement and constricts another.","before":"Confirmation is a static belief whose opposite is simply disbelief."},"confidence":"strong","mechanism":"The exact denial mirror and the paired ease/difficulty results make confirmation a path-forming stance: acceptance and rejection of the same good feed back into opposite conditions of movement.","model_id":"d92_8_10_mirrored_feedback","reader_inference":"The packet supplies a truth/falsehood opposition, an unchanged object, and mirrored facilitation toward ease or difficulty; I infer a feedback loop in which stance toward the good shapes the path one can travel. The live alternative treats both paths as subsequent allocation rather than an intrinsic effect of stance.","status":"revised","structural_cues":["92:9 mirrors 92:6 as كَذَّبَ بِٱلْحُسْنَىٰ, and 92:10 mirrors the result syntax of 92:7 while reversing the destination."],"trigger_roots":["ك ذ ب","ح س ن","ي س ر","ع س ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d92_8_10_mirrored_feedback","source_type":"hft","support_id":"sup_cab23a87d0f55bd398de","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ","ayah_ref":"92:11"},{"arabic_uthmani":"وَصَدَّقَ بِٱلْحُسْنَىٰ","ayah_ref":"92:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000323/B002","root_000558/B003","root_000852/B006","root_001110/B002","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000852","role":"Relinquishing wealth or a right supplies the focus-anchored alternative to retention.","root":"ص د ق","source_ref":"92:6","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000323","role":"Beneficent action makes release productive rather than merely dispossessive.","root":"ح س ن","source_ref":"92:6","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001110","role":"Sufficiency supplies the rescue-function that wealth is asked, and fails, to perform.","root":"غ ن ي","source_ref":"92:11","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Acquiring and accumulating property supplies the retained mass whose adequacy is tested.","root":"م و ل","source_ref":"92:11","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_000558","role":"Falling into destruction supplies the terminal load-test under which retained wealth cannot suffice.","root":"ر د ي","source_ref":"92:11","source_word_indices":["6"]}],"changed_reading":{"after":"Confirming the good loosens wealth's claim before retained property becomes useless ballast at the moment of collapse.","before":"Confirming the good may include an abstract willingness to give."},"confidence":"medium","mechanism":"Accumulated property promises sufficiency but fails at the fall; this sharpens relinquished-right confirmation into release from a possession that cannot bear the possessor's weight.","model_id":"d92_11_wealth_as_failed_ballast","reader_inference":"The packet supplies retained wealth, expected sufficiency, destructive falling, and charitable relinquishment; I supply the ballast metaphor and infer that release before the fall reverses wealth's failed rescue-function. A live alternative is that wealth merely fails to rescue from an independently caused fall.","status":"strengthened","structural_cues":["92:11 directly asks what accumulated wealth can avail when its owner falls."],"trigger_roots":["غ ن ي","م و ل","ر د ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d92_11_wealth_as_failed_ballast","source_type":"hft","support_id":"sup_01d18329256677ad3251","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ","ayah_ref":"92:3"},{"arabic_uthmani":"وَصَدَّقَ بِٱلْحُسْنَىٰ","ayah_ref":"92:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000058/B004","root_000323/B002","root_000516/B002","root_000852/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000852","role":"Solidity and straightness supply a conventionally hard material pole inside the focus.","root":"ص د ق","source_ref":"92:6","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000323","role":"Beneficent action requires the firm orientation to become productive for another.","root":"ح س ن","source_ref":"92:6","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000516","role":"The male branch's hardness and sharpness externalize the hard pole activated near focus-level solidity.","root":"ذ ك ر","source_ref":"92:3","source_word_indices":["3"]},{"branch_id":"B004","mapped_root_id":"root_000058","role":"Easy fertile earth supplies a receptive and generative counter-pole rather than mere softness.","root":"ء ن ث","source_ref":"92:3","source_word_indices":["4"]}],"changed_reading":{"after":"The focus can image a firmness that enters fertile receptivity and thereby becomes generative beneficence rather than sterile hardness.","before":"Truth toward the good is rigid correctness."},"confidence":"exploratory","containment":"This is surprising because it transfers nearby sexed and terrain images into the feminine الْحُسْنَىٰ; it remains anchored in the focus's feminine form, its firmness branch, and its beneficent-action branch. Downstream prose must present it only as a material analogy in which firmness becomes generative, not as a lexical derivation of الْحُسْنَىٰ from femininity.","focus_anchor":"The feminine form الْحُسْنَىٰ receives صَدَّقَ's solidity without losing the focus root's capacity for beneficent action.","outlier_id":"o92_3_firmness_fertility_coupling"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o92_3_firmness_fertility_coupling","source_type":"hft","support_id":"sup_bf1ed743df9188d14f17","trust":"legacy_unbound"}]}
</lane_packet_json>
