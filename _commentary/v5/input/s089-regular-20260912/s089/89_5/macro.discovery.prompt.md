# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **89:5**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_5/macro.discovery.json` and modify nothing
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
  "ayah_ref": "89:5",
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
{"branch_registry":[{"boundary":"It covers cutting or piercing a thing, opening a garment neck, carving rock, excavating, and a horn breaking through skin","branch_kind":null,"branch_ref":"root_000273/B001","candidate_links":[{"candidate_id":"cand_82e52fdf8e233a79c4c9","lane":"macro"},{"candidate_id":"cand_4c926d5a4f75fdabdf2f","lane":"macro"}],"focus_root_occurrences":[],"gloss":"piercing or cutting through","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الخَرْق والقطع النافذ","image_en":"piercing or cutting through"}}],"root_ar":"ج و ب","root_id":"root_000273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الخَرْق والقطع النافذ","image_en":"piercing or cutting through","scope_ar":"يدخل فيه قطع الشيء وخرقه وتقوير الجيب ونقر الصخر واحتفار الموضع وخروج القرن بخرق الجلد","scope_en":"It covers cutting or piercing a thing, opening a garment neck, carving rock, excavating, and a horn breaking through skin"},"support_links":["sup_81901d9a83302d38f27b","sup_f4c672d2b411e02865d1"]},{"boundary":"Dal, katı nesne ya da çevrili mekan anlamını değil, erişimi veya işlem yapmayı önleyen sınırlandırmayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","surface_ar":"حِجْرٍ"}],"gloss":"engelleme ve erişimi sınırlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığa erişmeyi, ondan yararlanmayı veya onun üzerinde işlem yapmayı engelleyen sınırlandırmadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyi dokunulması ya da yapılması yasak saymak, genel engellemenin kurallı bir uygulamasıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişinin malı üzerinde işlem yapma yetkisini yargı kararıyla kısıtlamak, çekirdeğin hukuki uygulamasıdır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeye ulaşmanın, ondan yararlanmanın veya onun üzerinde işlem yapmanın önlenmesini anlatan genel karşılıktır.","boundary_detail":"Dal, katı nesne ya da çevrili mekan anlamını değil, erişimi veya işlem yapmayı önleyen sınırlandırmayı anlatır.","branch_image_ar":"المنع والإحاطة","concept_gloss":"engelleme ve erişimi sınırlama","contextual_glosses":[{"applicability":"Bir nesnenin, eylemin veya erişimin kuralla izin dışına çıkarıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kurallı biçimde izin vermeme ve erişimi önleme anlamını eksiksiz korur."},"facet_ids":["F002"],"text":"yasaklama","usage_role":"contextual"},{"applicability":"Bir kişinin malı üzerinde hukuken işlem yapmasının önlendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mal üzerindeki işlem yetkisinin yargısal olarak sınırlandırılmasını açıkça korur."},"facet_ids":["F003"],"text":"tasarruf yetkisini kısıtlama","usage_role":"explanatory"}],"definition":"Bir şeye ulaşmayı, ondan yararlanmayı ya da onun üzerinde işlem yapmayı engelleyen bir sınır koymadır. Bu çekirdek, bir şeyi yasak saymayı ve kişinin malı üzerindeki işlem yetkisini yargı kararıyla kısıtlamayı da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığa erişmeyi, ondan yararlanmayı veya onun üzerinde işlem yapmayı engelleyen sınırlandırmadır."},{"facet_id":"F002","role":"specialization","statement":"Bir şeyi dokunulması ya da yapılması yasak saymak, genel engellemenin kurallı bir uygulamasıdır."},{"facet_id":"F003","role":"specialization","statement":"Bir kişinin malı üzerinde işlem yapma yetkisini yargı kararıyla kısıtlamak, çekirdeğin hukuki uygulamasıdır."}],"identity_rationale":"Kaynak ifadesi dalı tutarlı biçimde engelleme ve çevreleme ilkesiyle tanımlar; genel erişim engeli, yasaklama ve mal üzerinde işlem yapmanın yargı kararıyla kısıtlanması bu ilkenin açık uygulamalarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"erişimi veya işlem yapmayı engelleme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yasaklanmış, dokunulması önlenmiş şey"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"benden uzak dur; bana zarar vermen yasaktır"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sığınak ya da koruyucu dayanak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"geniş tutulmuş bir imkanı yasaklayıp daraltmak"}],"lexicalization_note":"Tanım genel engelleme çekirdeğini korur; belirli söz kalıplarındaki yasak, sığınma ve daraltma kullanımları yalnızca kendi sözcüksel karşılıklarında ele alınır.","neighbor_coverage_note":"Tüm adaylar incelendi; en güçlü iki sınır karşılaştırması yayımlandı, yalnızca koruma, aynı konu alanı veya uzak çağrışım paylaşan adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal doğrudan izin vermemenin ve engellemenin alan örneklerini öne çıkarır; odak dal ise çevreleyici sınır fikrini ve kişinin mal üzerindeki işlem yetkisinin kaldırılmasını da kendi çekirdeğine bağlar.","focus_only":"Mal üzerinde işlem yetkisinin yargısal olarak kısıtlanmasını ve genel çevreleme ilkesini de kapsar.","gloss":"yasaklama ve engelleme","neighbor_only":"Ekin veya otlak kullanımını engelleme gibi belirli arazi kullanımlarına ayrıca uzanır.","neighbor_ref":"root_000338/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir eylemi, erişimi veya yararlanmayı izin alanının dışında bırakır."},{"boundary_match":"partial","distinction":"Odak dal engeli çevreleme ve hukuki işlem kısıtıyla kurar; komşu dal ise geçişi tutan kişilerden cezai sınıra kadar daha geniş bir alıkoyma düzeni taşır.","focus_only":"Çevreleme ilkesi ile mal üzerinde işlem yapma yetkisinin hukuken sınırlandırılmasını içerir.","gloss":"alıkoyma ve yasak koyma","neighbor_only":"Kapı görevlisi, tutuklu kişi ve yeniden suç işlemeyi önleyen ceza sınırı gibi rolleri içerir.","neighbor_ref":"root_000002/B002","relation_type":"near_synonym","shared_zone":"İki dal da giriş, çıkış veya eylem imkanını bir sınırla önleme alanında buluşur."}],"source_phrase_ar":"أصل واحد مطرد وهو المنع والإحاطة (maqayis)؛ الحجر والحجر لغتان وهو الحرام (ayn;tahdhib)؛ كل شيء حجرت عليه فقد منعت عنه (jamhara)؛ حجر عليه القاضي إذا منعه من التصرف في ماله (sihah)؛ وأصل الحجر في اللغة ما حجرت عليه أي منعته (tahdhib)؛ الحجر الممنوع منه بتحريمه (mufradat)","source_summary":"Kaynakların ortak anlatımı, temel anlamı engelleme ve çevreleme olarak verir; yasaklanmış şey ile mal üzerinde işlem yapması önlenen kişi bu ortak çekirdeğin belirgin uygulamalarıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه المنع والحظر والتحريم والاعتصام والذمام والمنعة ومنع التصرف في المال","what_is_not_ar":"ليس الحجر الصلب ولا الحجرة المبنية ولا دارة القمر"},"support_links":[]},{"boundary":"Buradaki engel dışarıdan konan bir yasak değil, kişinin davranışını içeriden denetleyen anlama ve yargılama yetisidir.","branch_kind":"bare","branch_ref":"root_000296/B002","candidate_links":[{"candidate_id":"cand_4c926d5a4f75fdabdf2f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","surface_ar":"حِجْرٍ"}],"gloss":"yanlıştan alıkoyan akıl","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlama ve yargılama gücü, kişiyi yapılmaması gereken davranışlardan alıkoyan içsel bir engel gibi işler."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zihinsel yetinin düşünme ile davranışı dizginleme işlevlerinin birlikte anlatılması gereken bağlamlarda kullanılır.","boundary_detail":"Buradaki engel dışarıdan konan bir yasak değil, kişinin davranışını içeriden denetleyen anlama ve yargılama yetisidir.","branch_image_ar":"العقل الحاجز","concept_gloss":"yanlıştan alıkoyan akıl","contextual_glosses":[{"applicability":"Engelleyici işlevin bağlamdan anlaşıldığı doğal ve kısa kullanımlarda uygun karşılıktır.","error_profile":{"adds":null,"collision":"Genel zihinsel kapasite anlamıyla bağlam dışında karışabilir.","fit":"narrowing","loses":"Uygun olmayan davranıştan alıkoyma işlevini açıkça söylemez.","preserves":"Düşünme ve yargılama yetisi anlamını doğal biçimde korur."},"facet_ids":["F001"],"text":"akıl","usage_role":"general"}],"definition":"İnsanın düşünüp yargılamasını ve uygun olmayan davranışlardan kendini alıkoymasını sağlayan zihinsel yetidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlama ve yargılama gücü, kişiyi yapılmaması gereken davranışlardan alıkoyan içsel bir engel gibi işler."}],"identity_rationale":"Kaynak ifadesi, zihinsel yetiyi insanı uygun olmayan davranışlardan alıkoyma işlevi üzerinden tanımlar; dalın engelleyici akıl çerçevesi bu ilişkiyi doğru ve eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kişiyi yanlıştan alıkoyan akıl ve sağduyu"}],"lexicalization_note":"Dal yalın sözcükteki zihinsel yeti anlamını tanımlar ve başka yapılara özgü yasaklama ya da maddi çevreleme anlamlarını içeri almaz.","neighbor_coverage_note":"Tüm adaylar incelendi; zihinsel yetiyle doğrudan karışabilecek iki dal ve aynı kökün genel engelleme dalı seçildi, yalnızca sonuç veya konu yakınlığı taşıyanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekler çok yakındır; odak dal uygun olmayan davranış ölçüsünü daha genel kurarken komşu dal engeli özellikle çirkin davranış ekseninde belirginleştirir.","focus_only":"Yapılması uygun olmayan davranışların bütününe karşı işleyen genel zihinsel yetiyi anlatır.","gloss":"kötü davranıştan alıkoyan akıl","neighbor_only":"Özellikle çirkin davranışı durduran zihinsel uyarı yönünü öne çıkarır.","neighbor_ref":"root_001560/B003","relation_type":"near_synonym","shared_zone":"Her iki dalda da akıl, kişiyi yanlış veya çirkin davranıştan geri tutan içsel güçtür."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı çekirdeği davranışı engelleme işlevidir; komşu dal aynı yetinin bilgi edinme, anlama ve sağlam karar verme boyutlarını da bağımsız bileşenler olarak taşır.","focus_only":"Zihinsel yetinin davranış üzerinde engelleyici bir sınır kurmasını merkez alır.","gloss":"anlama ve kendini dizginleme gücü","neighbor_only":"Bilgi, ayırt etme, anlama ve sağlam karar verme gibi bilişsel işlevleri daha geniş biçimde kapsar.","neighbor_ref":"root_001036/B001","relation_type":"near_synonym","shared_zone":"İki dal da anlayan, ayırt eden ve kişiyi yanlış davranıştan geri tutan zihinsel yetiyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal bir zihinsel yetiyi adlandırır; komşu dal ise nesnelere, eylemlere veya mal üzerindeki işlemlere getirilen engelleme eylemini ve durumunu adlandırır.","focus_only":"Engeli kuran şey kişinin kendi anlama ve yargılama yetisidir.","gloss":"içsel davranış engeli","neighbor_only":"Engel dışarıdan konan yasak, erişim sınırı veya yargısal işlem kısıtı olabilir.","neighbor_ref":"root_000296/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir eylemi yapılmaması gereken sınırın gerisinde tutma düşüncesini paylaşır."}],"source_phrase_ar":"العقل يسمى حجرا لأنه يمنع من إتيان ما لا ينبغي (maqayis)؛ والحجر العقل (jamhara)؛ والحجر العقل (sihah)؛ والحجر اللب والعقل (tahdhib)؛ فقيل للعقل حجر لكون الإنسان في منع منه مما تدعو إليه نفسه (mufradat)","source_summary":"Kaynaklar zihinsel yetiyi yalnızca düşünme gücü olarak değil, kişinin isteklerini denetleyip onu uygun olmayan eylemden geri tutan bir iç sınır olarak açıklar.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحجر بمعنى العقل واللب الذي يمنع صاحبه مما لا ينبغي","what_is_not_ar":"ليس التحريم ولا الحجر على المال ولا الحجارة"},"support_links":["sup_f4c672d2b411e02865d1"]},{"boundary":"Dalın çekirdeği sert taş nesnesidir; türemiş eylemler, deyimsel felaket anlatımı ve altın-gümüş ikilisi yalnızca kendi birimleriyle sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B003","candidate_links":[{"candidate_id":"cand_82e52fdf8e233a79c4c9","lane":"macro"},{"candidate_id":"cand_4c926d5a4f75fdabdf2f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","surface_ar":"حِجْرٍ"}],"gloss":"taş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bilinen sert ve katı taş nesnesini, tek bir parçayı ve aynı türden taşların çoğulunu anlatır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sert ve katı doğal nesnenin tekil ya da tür adı olarak karşılandığı genel bağlamlarda kullanılır.","boundary_detail":"Dalın çekirdeği sert taş nesnesidir; türemiş eylemler, deyimsel felaket anlatımı ve altın-gümüş ikilisi yalnızca kendi birimleriyle sınırlıdır.","branch_image_ar":"الحَجَر الصلب","concept_gloss":"taş","contextual_glosses":[{"applicability":"Nesnenin katılığı ile tek bir parça oluşunun açıkça belirtilmesi gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşın sert ve katı bir nesne oluşunu, tek parça görünümüyle birlikte korur."},"facet_ids":["F001"],"text":"sert taş parçası","usage_role":"explanatory"}],"definition":"Doğada bulunan, sert ve katı yapılı bilinen taş nesnesi ile bu nesnenin tekil ve çoğul örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bilinen sert ve katı taş nesnesini, tek bir parçayı ve aynı türden taşların çoğulunu anlatır."}],"identity_rationale":"Kaynak ifadesi dal düzeyinde bilinen sert taşı ve onun çoğul biçimlerini açıkça destekler. Geçici çerçevedeki taşlaşma, deyim ve özel adlandırmalar ise ayrı sözcüksel birimlerde bulunur ve yalın taş çekirdeğinin kurucu parçaları sayılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"taş; taşlar"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"taşlaşmak ve sertleşmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"başına çok çetin bir kişi ya da ağır bir iş gelmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"altın ve gümüş"}],"lexicalization_note":"Tanım yalın taş anlamını temel alır; taşlaşma, deyimsel kullanım ve özel ikili adlandırma ayrı sözcüksel karşılıklarda tutulur.","neighbor_coverage_note":"Tüm adaylar incelendi; genel taşla en kolay karışan iri kaya ve çakıl dalları ile aynı kökün çevrili mekan dalı yayımlandı, uzak deyim ve nitelik benzerlikleri elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sıradan boyuttaki taşı da kapsayan genel addır; komşu dal ise aynı nesne alanını büyüklük ve kaya kütlesi niteliğiyle daraltır.","focus_only":"Boyut bakımından büyük olma şartı taşımayan genel taş türünü ve çoğulunu kapsar.","gloss":"iri ve sert kaya","neighbor_only":"Özellikle büyük ve kütleli kaya ya da iri taş olma sınırını taşır.","neighbor_ref":"root_000847/B001","relation_type":"near_synonym","shared_zone":"İki dal da sert, katı ve doğal taş maddesinden oluşan nesneleri adlandırır."},{"boundary_match":"partial","distinction":"Odak dal boyut ve zemin türü bakımından sınırsız genel taş adıdır; komşu dal küçük çakıl boyutuna ve çakıllı yüzeye özgüdür.","focus_only":"Küçük ya da büyük her türlü sıradan taş parçasını kapsayabilir.","gloss":"çakıl ve küçük taş","neighbor_only":"Küçük, yuvarlanmış çakıl parçalarını ve bunlarla kaplı zemini özellikle adlandırır.","neighbor_ref":"root_000332/B001","relation_type":"near_synonym","shared_zone":"Her iki dal taş maddesinden oluşan ayrık parçaları anlatır."},{"boundary_match":"partial","distinction":"Odak dal sınırı oluşturan malzeme ya da nesnedir; komşu dal ise bu veya başka bir sınırın içinde kalan mekandır.","focus_only":"Sınır kurup kurmamasından bağımsız olarak taş maddesini ve taş parçasını adlandırır.","gloss":"taş ile çevrili yer ayrımı","neighbor_only":"Taş veya duvarla çevrilmiş alanı, odayı, ağılı ya da yerleşim bölümünü adlandırır.","neighbor_ref":"root_000296/B004","relation_type":"near_neighbor","shared_zone":"Çevrili mekanın sınırı taşla kurulabildiği için iki dal aynı somut sahnede buluşabilir."}],"source_phrase_ar":"والحجر معروف (maqayis)؛ الأحجار جمع الحجر والحجارة جمع الحجر أيضا (ayn)؛ الحجر معروف ويجمع أحجارا وحجارة (jamhara)؛ الحجر جمعه في القلة أحجار وفي الكثرة حجار وحجارة (sihah)؛ الحجر وجمعه الحجارة (tahdhib)؛ الحجر الجوهر الصلب المعروف وجمعه أحجار وحجارة (mufradat)","source_summary":"Kaynaklar ortak biçimde bilinen sert taş nesnesini tanır ve bu nesne için birden çok çoğul biçimin kullanıldığını belirtir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحجر المعروف والحجارة والصلابة والتحجر وما يلحق بذلك من أمثال وأسماء مبنية على الحجارة","what_is_not_ar":"ليس الحرام ولا العقل ولا الحجرة المحوطة"},"support_links":["sup_81901d9a83302d38f27b","sup_f4c672d2b411e02865d1"]},{"boundary":"Dal sınırın yapıldığı taşı veya duvarı değil, sınırın içinde kalan yeri ve bu modele göre adlandırılmış mekanları anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","surface_ar":"حِجْرٍ"}],"gloss":"çevrili yer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir sınır, duvar veya taş çevre içinde kalan ve dışarıdan ayrılan mekandır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yapının içindeki oda ya da ayrılmış bölüm, çevrili mekanın yapı içindeki uygulamasıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvanları bir arada tutan çevrili ağıl, çekirdeğin barınak uygulamasıdır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir topluluğun evinin veya yerleşiminin yanı ve korunan çevresi, mekan çekirdeğinin alan uzantısıdır."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Kaynaklarda kutsal bir yapının çevrili yanı ile eski bir topluluğun yurdu da bu çevreleme modeline göre adlandırılır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duvar, taş veya başka bir sınır içinde kalan mekanın genel ve türden bağımsız karşılığıdır.","boundary_detail":"Dal sınırın yapıldığı taşı veya duvarı değil, sınırın içinde kalan yeri ve bu modele göre adlandırılmış mekanları anlatır.","branch_image_ar":"المكان المحوط","concept_gloss":"çevrili yer","contextual_glosses":[{"applicability":"Bir yapının içinde duvarlarla ayrılmış yaşama veya kullanma bölümü anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapı içinde sınırlarla ayrılmış kapalı bölüm anlamını eksiksiz korur."},"facet_ids":["F002"],"text":"oda","usage_role":"contextual"},{"applicability":"Hayvanların çevrili bir alanda tutulduğu barınak bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanları sınır içinde bir arada tutan çevrili barınak anlamını korur."},"facet_ids":["F003"],"text":"ağıl","usage_role":"contextual"},{"applicability":"Bir evin ya da yerleşimin yakınındaki ayrılmış ve korunan alan anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerleşimin yakınında sınırlandırılmış ve korunan alan anlamını tam olarak korur."},"facet_ids":["F004"],"text":"korunan çevre","usage_role":"explanatory"}],"definition":"Duvar, taş dizisi ya da başka bir sınırla çevrilmiş ve dışarıdan ayrılmış yerdir. Oda, hayvan ağılı, bir yerleşimin yanı ve bu çevreleme modeline göre adlandırılmış belirli mekanlar bu çekirdeğin uygulamalarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir sınır, duvar veya taş çevre içinde kalan ve dışarıdan ayrılan mekandır."},{"facet_id":"F002","role":"specialization","statement":"Bir yapının içindeki oda ya da ayrılmış bölüm, çevrili mekanın yapı içindeki uygulamasıdır."},{"facet_id":"F003","role":"specialization","statement":"Hayvanları bir arada tutan çevrili ağıl, çekirdeğin barınak uygulamasıdır."},{"facet_id":"F004","role":"extension","statement":"Bir topluluğun evinin veya yerleşiminin yanı ve korunan çevresi, mekan çekirdeğinin alan uzantısıdır."},{"facet_id":"F005","role":"source_variant","statement":"Kaynaklarda kutsal bir yapının çevrili yanı ile eski bir topluluğun yurdu da bu çevreleme modeline göre adlandırılır."}],"identity_rationale":"Kaynak ifadesi oda, duvarla çevrili yer, hayvan ağılı, evin yanı ve belirli kutsal ya da eski yer adlarını çevrilmiş alan ilişkisiyle birlikte verir; mekan merkezli dal çerçevesi bu ortak yapıyı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kutsal yapının çevrili yan bölümü"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"eski bir topluluğun yurt edindiği bölge"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"oda, çevrili yer veya ağıl"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"topluluğun evinin yanı ya da korunan çevresi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"vadide veya çukur yerde suyu tutan setli alan"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bahçe, koruluk veya köy çevresindeki korunan alan"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"çevrili bir yer edinmek"}],"lexicalization_note":"Genel çevrili mekan çekirdeği ile oda ve ağıl uygulamaları tanımda ayrılır; belirli yapı, yer, su tutma alanı ve köy çevresi kullanımları kendi birimlerine bağlı kalır.","neighbor_coverage_note":"Tüm adaylar incelendi; ağıl, duvar ve ayrılmış yapı bölümüyle kurulan en açıklayıcı üç sınır yayımlandı, yalnızca aynı sahneyi paylaşan uzak mekan adayları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal hayvan ağılına ve kapsama işlevine özgüdür; odak dal aynı çevreleme düzenini odadan yerleşim çevresine kadar daha geniş mekanlara taşır.","focus_only":"Oda, ev yanı, kutsal yapı bölümü ve geniş yerleşim alanı gibi farklı mekan türlerini kapsar.","gloss":"çevrili ağıl","neighbor_only":"İçindekileri bir arada tutan ağıl olma işlevini adlandırmanın açık merkezi yapar.","neighbor_ref":"root_000036/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir sınırın içindekileri dışarıdan ayırdığı çevrili mekanı anlatır."},{"boundary_match":"partial","distinction":"Odak dal çevrelenen iç mekandır; komşu dal ise bu mekanı oluşturan dik sınır yapısıdır ve iç alanın kendisi yerine duvarı öne çıkarır.","focus_only":"Duvarın veya sınırın içinde kalan oda, ağıl ya da bölgeyi adlandırır.","gloss":"çevrili alan ile duvar ayrımı","neighbor_only":"Alanı çevreleyen yükseltilmiş duvarı, seti veya suyu tutan yapı unsurunu adlandırır.","neighbor_ref":"root_000228/B001","relation_type":"near_neighbor","shared_zone":"Bir duvarın çevrelediği mekan sahnesinde iki dal doğrudan yan yana bulunur."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği yalnızca çevrilmiş olmaktır; komşu dal ise büyük yapı ya da yapı içindeki özel ayrılmış kesim türlerini kendi adlandırma alanına alır.","focus_only":"Basit oda, hayvan ağılı ve yerleşim çevresi gibi büyük yapı niteliği gerektirmeyen mekanları kapsar.","gloss":"ayrılmış yapı bölümü","neighbor_only":"Büyük yapı olarak sarayı ve ev ya da ibadet yapısı içindeki özel ayrılmış bölümü kapsar.","neighbor_ref":"root_001231/B005","relation_type":"near_neighbor","shared_zone":"İki dal da duvarlarla belirlenmiş bir yapı veya yapı içi bölüm alanında buluşur."}],"source_phrase_ar":"حجرة القوم ناحية دارهم والحجرة من الأبنية معروفة (maqayis)؛ الحجر حطيم مكة وحجر موضع كان لثمود والحجرة ناحية كل موضع (ayn)؛ الحجر حجر الكعبة والحجر بلاد ثمود والحجرة الحائط يحجر على دار (jamhara)؛ الحجرة حظيرة الإبل ومنه حجرة الدار والحجر حجر الكعبة والحجر منازل ثمود (sihah)؛ الحجرة التي ينزلها الناس وهو ما حوطوا عليه (tahdhib)؛ سمي ما أحيط به الحجارة حجرا وبه سمي حجر الكعبة وديار ثمود (mufradat)","source_summary":"Kaynaklar çevrelenerek ayrılmış yer çekirdeğinde birleşir; oda, duvarlı bölüm, hayvan ağılı, evin yakını, kutsal bir yapının yanı ve eski bir yerleşim alanı bu mekan düzeninin farklı gerçekleşmeleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحجرة والحائط والحظيرة وحجر الكعبة وديار ثمود والحديقة والحاجر ومحجر القرية","what_is_not_ar":"ليس الحِجر بمعنى الحضن ولا دارة القمر ولا الفرس الأنثى"},"support_links":[]},{"boundary":"Dal genel yasaklamayı ya da yapı içindeki odayı değil, kucak alanını ve bir kişinin yakın koruması altında bulunma durumunu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","surface_ar":"حِجْرٍ"}],"gloss":"kucak ve yakın koruma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın gövdesi ile bacakları arasında, birini veya bir şeyi yakında tutmaya yarayan kucak alanıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birinin kucağında ya da kanadı altında olmak, onun yakın koruması ve denetimi altında bulunmayı anlatır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel kucak alanı ile bundan gelişen koruma ilişkisini birlikte karşılamanın gerektiği genel açıklamalarda kullanılır.","boundary_detail":"Dal genel yasaklamayı ya da yapı içindeki odayı değil, kucak alanını ve bir kişinin yakın koruması altında bulunma durumunu anlatır.","branch_image_ar":"الحِجر والحضن","concept_gloss":"kucak ve yakın koruma","contextual_glosses":[{"applicability":"Bir insanın otururken gövdesi ile bacakları arasındaki yakın tutma alanı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel yakınlık ve birini ya da bir şeyi sararak tutma alanını korur."},"facet_ids":["F001"],"text":"kucak","usage_role":"general"},{"applicability":"Bir kişinin başka birinin yakın koruması ve denetimi altında bulunduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Birinin yakın koruması ve gözetimi altında bulunma ilişkisini doğal biçimde korur."},"facet_ids":["F002"],"text":"kanadı altında","usage_role":"contextual"}],"definition":"İnsanın otururken gövdesi ile bacakları arasında oluşan, birini ya da bir şeyi yakınında tutup sardığı kucak alanıdır. Bu bedensel yakınlık, birinin koruması ve denetimi altında bulunma ilişkisine de uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın gövdesi ile bacakları arasında, birini veya bir şeyi yakında tutmaya yarayan kucak alanıdır."},{"facet_id":"F002","role":"extension","statement":"Birinin kucağında ya da kanadı altında olmak, onun yakın koruması ve denetimi altında bulunmayı anlatır."}],"identity_rationale":"Kaynak ifadesi insanın, özellikle kadının, kucağını ve birinin kucağında ya da kanadı altında bulunmayı birlikte verir; yakın bedensel alan ile bu alandan gelişen koruma ilişkisi dal çerçevesinde doğru biçimde ayrılabilir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kucak, yakın sığınak ve koruma"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"birinin kanadı ve denetimi altında"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"gömleğin içinde bir şeyi tutan kıvrım"}],"lexicalization_note":"Kucak anlamı ile yakın koruma uzantısı tanımda ayrılır; birinin kanadı altında bulunma ve gömlek kıvrımı kullanımları kendi sözcüksel birimleriyle sınırlıdır.","neighbor_coverage_note":"Tüm adaylar incelendi; sığınak, sarılma ve genel engelleme ile kurulabilecek başlıca karışıklıklar yayımlandı, yalnızca aile veya koruma sahnesini uzaktan paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal korumayı kucak ve kişisel yakınlık üzerinden kurar; komşu dal ise kişiden bağımsız fiziksel siperleri ve doğa koşullarından saklanmayı da kapsar.","focus_only":"İnsanın bedensel kucak alanını ve bu alana dayalı yakın denetimi içerir.","gloss":"sığınak ve kanat altı","neighbor_only":"Rüzgar, soğuk veya güneşten koruyan ağaç ve benzeri siperleri de kapsar.","neighbor_ref":"root_000513/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi ya da nesnenin yakınına girerek korunma durumunu anlatır."},{"boundary_match":"partial","distinction":"Odak dal bir yer ve koruma ilişkisi olarak kucağı anlatır; komşu dal ise bedenlerin birbirine sarılması eylemini anlatır.","focus_only":"Kucak olarak kullanılan bedensel alanı ve orada korunma durumunu adlandırır.","gloss":"kucak ile sarılma ayrımı","neighbor_only":"İki bedenin birbirine sarılması ve bu temasın sürdürülmesi eylemini adlandırır.","neighbor_ref":"root_001354/B005","relation_type":"near_neighbor","shared_zone":"İki dal bedensel yakınlık, sarma ve temas sahnesini paylaşır."},{"boundary_match":"partial","distinction":"Odak dal korumayı kucak ve kişisel yakınlık ilişkisiyle somutlaştırır; komşu dalın çekirdeği ise herhangi bir erişim ya da işlemi engellemektir.","focus_only":"Yakın bedensel alanı ve bir kişinin koruması altında bulunmayı içerir.","gloss":"yakın koruma ile engelleme ayrımı","neighbor_only":"Genel erişim yasağını ve mal üzerinde işlem yapma yetkisinin hukuken kısıtlanmasını içerir.","neighbor_ref":"root_000296/B001","relation_type":"near_neighbor","shared_zone":"Korunan kişiye dışarıdan müdahaleyi önleme düşüncesi iki dalı birbirine bağlar."}],"source_phrase_ar":"الحجر حجر الإنسان وقد تكسر حاؤه (maqayis)؛ حجر المرأة وحجرها لغتان للحضنين (ayn)؛ حجر المرأة وقالوا حجرها (jamhara)؛ حجر الإنسان وحجره والجمع حجور (sihah)؛ حجر المرأة وحجرها حضنها وفلان حجر فلان أي في كنفه ومنعته (tahdhib)؛ فلان في حجر فلان أي في منع منه وجمعه حجور (mufradat)","source_summary":"Kaynaklar kucak alanını ortak çekirdek olarak verir; bir kişinin yakınında, korumasında ve denetimi altında bulunma ilişkisi bu bedensel alandan gelişen uzantıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه حجر الإنسان وحجر المرأة والحضن والكنف والمنعة القريبة","what_is_not_ar":"ليس حجر القاضي على المال ولا حجر الكعبة ولا الحجر الصلب"},"support_links":[]},{"boundary":"Dal her türlü daireselliği kapsamaz; bir nesnenin, özellikle ayın ya da gözün, çevresini belirleyen halka, iz ve bölgeyle sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B006","candidate_links":[{"candidate_id":"cand_b1c0b25598981381b1f9","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","surface_ar":"حِجْرٍ"}],"gloss":"çevreleyen halka veya sınır","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesnenin çevresini halka, çizgi veya belirgin bölge halinde kuşatan çevre sınırıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayın çevresinde beliren ince halka, çevre sınırının gökyüzündeki görünümüdür."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir hayvanın göz çevresine yuvarlak damga vurmak, halka biçimli sınırı kasıtlı olarak oluşturma eylemidir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Göz çukuru çevresi ile yüz örtüsünün göz çevresine oturduğu bölüm, çekirdeğin bedensel alan uzantısıdır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin çevresini halka, çizgi ya da belirgin bölge olarak kuşatan biçimin genel karşılığıdır.","boundary_detail":"Dal her türlü daireselliği kapsamaz; bir nesnenin, özellikle ayın ya da gözün, çevresini belirleyen halka, iz ve bölgeyle sınırlıdır.","branch_image_ar":"الدائرة حول الشيء","concept_gloss":"çevreleyen halka veya sınır","contextual_glosses":[{"applicability":"Ayın çevresinde ince ve yuvarlak bir ışık kuşağı görüldüğü gökyüzü bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayın çevresinde beliren ince ve yuvarlak halka görünümünü açıkça korur."},"facet_ids":["F002"],"text":"ayın çevresindeki ışık halkası","usage_role":"contextual"},{"applicability":"Bir hayvanın gözünün çevresinin yuvarlak bir damgayla işaretlendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın göz çevresinde damgayla yuvarlak bir iz oluşturma eylemini tam korur."},"facet_ids":["F003"],"text":"göz çevresine yuvarlak damga vurmak","usage_role":"explanatory"},{"applicability":"Gözün çevresindeki anatomik bölge veya yüz örtüsünün göz yanında durduğu kesim anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözün çevresindeki belirgin yüz bölgesini ve sınır niteliğini korur."},"facet_ids":["F004"],"text":"göz çukuru çevresi","usage_role":"contextual"}],"definition":"Bir şeyin, özellikle ayın ya da gözün, çevresini halka, ince çizgi veya belirgin bir bölge halinde kuşatan çevredir. Hayvan gözünün çevresine yuvarlak damga vurma eylemi bu biçimi kasıtlı olarak oluşturur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesnenin çevresini halka, çizgi veya belirgin bölge halinde kuşatan çevre sınırıdır."},{"facet_id":"F002","role":"specialization","statement":"Ayın çevresinde beliren ince halka, çevre sınırının gökyüzündeki görünümüdür."},{"facet_id":"F003","role":"associated_use","statement":"Bir hayvanın göz çevresine yuvarlak damga vurmak, halka biçimli sınırı kasıtlı olarak oluşturma eylemidir."},{"facet_id":"F004","role":"extension","statement":"Göz çukuru çevresi ile yüz örtüsünün göz çevresine oturduğu bölüm, çekirdeğin bedensel alan uzantısıdır."}],"identity_rationale":"Kaynak ifadesi ayın çevresindeki halka, hayvan gözünün çevresine vurulan yuvarlak damga ve göz çevresi bölgesini ortak bir çevre çizgisi ilişkisiyle birleştirir. Dal korunabilir, ancak çekirdek dönme eylemi değil bir şeyi kuşatan halka, iz veya çevre bölgesidir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ayın çevresinde ince bir halka belirmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"hayvanın göz çevresine yuvarlak damga vurmak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"göz çukuru çevresi veya yüz örtüsünün gözü açıkta bırakan bölümü"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"çocukların çizilmiş bir çember çevresinde oynadığı oyun"}],"lexicalization_note":"Genel çevre halkası çekirdeği korunur; ay halkası, göz çevresine damga vurma, göz çevresi bölgesi ve çocuk oyunu yalnızca kendi yapılardaki kullanımlarıyla ayrılır.","neighbor_coverage_note":"Tüm adaylar incelendi; ay halkası, genel dairesellik ve çevresini kuşatma ile kurulan üç temel sınır yayımlandı, yalnızca biçim ya da aynı sahne çağrışımı taşıyanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ay bağlamında karşılıklar çok yakındır; odak dal aynı çevre biçimini göz çevresi ve yuvarlak damga alanına da taşırken komşu dal yalnızca ay halkasına özgüdür.","focus_only":"Göz çevresi, yüz bölgesi ve göz çevresine vurulan yuvarlak damga kullanımlarını da kapsar.","gloss":"ayın çevresindeki halka","neighbor_only":"Ay çevresindeki ışık görünümünü bağımsız ve yalnızca gökyüzüne özgü bir anlam olarak adlandırır.","neighbor_ref":"root_001613/B003","relation_type":"near_synonym","shared_zone":"İki dal da ayın çevresinde görülen yuvarlak kuşağı doğrudan anlatır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği çevreleyen sınırın kendisidir; komşu dal ise hem daire biçimini hem de dönme ve döndürme hareketini kapsayan daha geniş bir süreç alanına sahiptir.","focus_only":"Bir nesnenin çevresini kuşatan sabit halka, iz veya anatomik bölgeyi merkez alır.","gloss":"çevre halkası ile dönme ayrımı","neighbor_only":"Dönme eylemini, dönüş döngüsünü ve döndürülen araç ya da nesneleri geniş biçimde kapsar.","neighbor_ref":"root_000499/B001","relation_type":"near_neighbor","shared_zone":"Daire biçimi ve bir merkez çevresinde düzenlenme iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal çevrede oluşan biçim veya bölgedir; komşu dal ise katılımcıların bir nesnenin etrafını çevirmesi eylemidir.","focus_only":"Halka, ince çizgi, damga izi veya göz çevresi gibi kalıcı ya da görünür sınırı adlandırır.","gloss":"çevre çizgisi ile kuşatma ayrımı","neighbor_only":"İnsanların veya başka ögelerin bir şeyin çevresinde toplanıp onu kuşatması eylemini adlandırır.","neighbor_ref":"root_000300/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal bir merkezin bütün çevresinin sarılması ilişkisini taşır."}],"source_phrase_ar":"حجر القمر إذا صارت حوله دارة وحجرت عين البعير إذا وسمت حولها بميسم مستدير ومحجر العين ما يدور بها (maqayis)؛ المحجر حيث يقع عليه النقاب من الوجه (ayn)؛ حجر القمر إذا صارت حوله دارة وحجرت عين البعير إذا وسمت حولها بميسم مستدير ومحجر العين معروف (jamhara)؛ حجر القمر إذا استدار بخط دقيق والتحجير أن تسم حول عين البعير بميسم مستدير (sihah)؛ المحجر من الوجه حيث يقع عليه النقاب والمحجر العين (tahdhib)؛ حجرت عين الفرس إذا وسمت حولها بميسم وحجر القمر صار حوله دائرة ومحجر العين منه (mufradat)","source_summary":"Kaynak anlatımı ay çevresindeki ince halkayı, hayvan gözünün çevresine vurulan yuvarlak damgayı ve göz ya da yüz çevresindeki bölgeyi aynı çevreleme biçiminin farklı uygulamaları olarak bir araya getirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه دارة القمر والوسم المستدير حول عين الدابة ومحجر العين وما يشبه الخط المستدير","what_is_not_ar":"ليس الحائط والحجرة ولا الحجر بمعنى الحرام"},"support_links":["sup_b20e502901c704330196"]},{"boundary":"Dal genel olarak dişi hayvanı değil dişi atı anlatır; koruma ve damızlık için ayırma bu referentin belirgin fakat kaynaklarda farklı vurgulanan nitelikleridir.","branch_kind":"bare","branch_ref":"root_000296/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","surface_ar":"حِجْرٍ"}],"gloss":"dişi at, özellikle damızlık kısrak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Referent, genel hayvan türü içinde özellikle dişi attır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi atın üreme için ayrılması, özenle korunması ve yalnızca seçilmiş bir erkekle çiftleştirilmesi belirgin yetiştirme uygulamasıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adlandırma, dişi atın karnında yavru taşıyıp onu içinde barındırmasıyla da açıklanır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi at çekirdeği ile üreme için ayrılıp korunma niteliğinin birlikte gösterilmesi gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal genel olarak dişi hayvanı değil dişi atı anlatır; koruma ve damızlık için ayırma bu referentin belirgin fakat kaynaklarda farklı vurgulanan nitelikleridir.","branch_image_ar":"الفرس الأنثى المصونة","concept_gloss":"dişi at, özellikle damızlık kısrak","contextual_glosses":[{"applicability":"Yalnızca hayvanın cinsiyeti ve türünün gerekli olduğu doğal metin bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişi at referentini kısa ve doğal biçimde eksiksiz korur."},"facet_ids":["F001"],"text":"kısrak","usage_role":"general"},{"applicability":"Dişi atın üreme için ayrılıp özenle korunduğu yetiştiricilik bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalnızca seçilmiş bir erkekle çiftleştirilme koşulunu açıkça belirtmez.","preserves":"Dişi atın üreme amacıyla ayrılması ve korunması anlamını korur."},"facet_ids":["F002"],"text":"damızlık kısrak","usage_role":"contextual"}],"definition":"Dişi at, özellikle üreme için ayrılıp korunan ve yalnızca seçilmiş bir erkekle çiftleştirilen kısraktır. Adlandırma kaynaklarda ayrıca karnında yavru taşımasına bağlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Referent, genel hayvan türü içinde özellikle dişi attır."},{"facet_id":"F002","role":"specialization","statement":"Dişi atın üreme için ayrılması, özenle korunması ve yalnızca seçilmiş bir erkekle çiftleştirilmesi belirgin yetiştirme uygulamasıdır."},{"facet_id":"F003","role":"source_variant","statement":"Adlandırma, dişi atın karnında yavru taşıyıp onu içinde barındırmasıyla da açıklanır."}],"identity_rationale":"Kaynak ifadesi dişi atı temel referent olarak verir ve onu korunan, üreme için ayrılan, seçilmiş erkek dışında çiftleştirilmeyen ya da yavru taşıyan hayvan olarak açıklar; geçici dal çerçevesi bu ortak alanı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"korunan ya da damızlık olarak ayrılan kısrak"}],"lexicalization_note":"Dal yalın sözcükteki dişi at anlamını tanımlar; koruma, damızlık için ayırma ve yavru taşıma açıklamaları aynı referentin sınırları içinde tutulur.","neighbor_coverage_note":"Tüm adaylar incelendi; üreyen dişi hayvan, korunan seçkin hayvan ve yavru-soy alanlarıyla kurulan üç açıklayıcı karşılaştırma yayımlandı, yalnızca erkek hayvan ya da çiftleşme olayı odaklı adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tür bakımından dişi atla sınırlıdır ve seçici çiftleştirmeyi vurgular; komşu dal üreme değeri taşıyan dişi hayvanları daha geniş bir tür alanında toplar.","focus_only":"Yalnızca at türündeki dişiyi ve seçilmiş erkekle çiftleştirme kısıtını kapsar.","gloss":"yavru vermesi beklenen dişi hayvan","neighbor_only":"At dışındaki mal ve çiftlik hayvanlarının yavru vermesi beklenen dişilerini de kapsar.","neighbor_ref":"root_000233/B006","relation_type":"near_synonym","shared_zone":"İki dal da yavru üretmesi beklenen ve bu amaçla değer verilen dişi hayvanı anlatır."},{"boundary_match":"partial","distinction":"Odak dal dişi atı damızlık olarak korur; komşu dal ise seçkin deveyi güvenilir yedek olarak saklar ve aynı çiftleştirme sınırını taşımaz.","focus_only":"Korunan hayvan dişi attır ve üreme amacı ile eş seçimi açıkça belirleyicidir.","gloss":"özenle saklanan seçkin hayvan","neighbor_only":"Korunan hayvan devedir; seçim cinsiyetten çok yormadan saklama, güvenilir yedek ve sürü niteliğine dayanır.","neighbor_ref":"root_001235/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da değerli bir hayvanın yıpratılmadan korunup gelecekteki yarar için ayrılmasını anlatır."},{"boundary_match":"field_only","distinction":"Odak dal üremeye katılan korunan dişi hayvandır; komşu dal ise üremenin sonucu olan yavruyu ve kuşaklar boyunca çoğalan soyu anlatır.","focus_only":"Üreme için ayrılan ana hayvanı, yani dişi atı adlandırır.","gloss":"damızlık ana ile yavru-soy ayrımı","neighbor_only":"Doğan yavruyu, soyu ve canlıların birbirinden çoğalmasını adlandırır.","neighbor_ref":"root_001499/B001","relation_type":"same_field","shared_zone":"İki dal hayvan yetiştiriciliği, çiftleşme ve neslin sürdürülmesi alanını paylaşır."}],"source_phrase_ar":"والحجر الفرس الأنثى وهي تصان ويضن بها (maqayis)؛ أحجار الخيل ما اتخذ منها للنسل (ayn)؛ سميت الأنثى من الخيل حجرا لأنها حجرت عن الذكور إلا عن فحل كريم (jamhara)؛ والحجر أيضا الأنثى من الخيل (sihah)؛ الحجر الفرس الأنثى وما اتخذ منها للنسل (tahdhib)؛ يقال للأنثى من الفرس حجر لكونها مشتملة على ما في بطنها من الولد (mufradat)","source_summary":"Kaynaklar referentin dişi at olduğu konusunda birleşir; korunan ve üreme için ayrılan hayvan oluşu, seçilmiş erkek dışında çiftleştirilmemesi ve karnında yavru taşıması adlandırmayı açıklayan tamamlayıcı vurgulardır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحجر من الخيل وهي الأنثى المصونة أو المعدة للنسل","what_is_not_ar":"ليس حجر المرأة ولا الحجر الصلب ولا الحرام"},"support_links":[]},{"boundary":"Includes a hollow in rock holding rainwater, underground water cavities, and newly dug wells.","branch_kind":null,"branch_ref":"root_000434/B011","candidate_links":[{"candidate_id":"cand_82e52fdf8e233a79c4c9","lane":"macro"}],"focus_root_occurrences":[],"gloss":"water-holding hollow or new well","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"نقرة أو بئر تمسك الماء","image_en":"water-holding hollow or new well"}}],"root_ar":"خ ل ق","root_id":"root_000434","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"نقرة أو بئر تمسك الماء","image_en":"water-holding hollow or new well","scope_ar":"يدخل فيه الخليقة بمعنى النقرة في الصفا أو الصخرة يجتمع فيها ماء السماء، والدحلان والآبار الحديثة الحفر.","scope_en":"Includes a hollow in rock holding rainwater, underground water cavities, and newly dug wells."},"support_links":["sup_81901d9a83302d38f27b"]},{"boundary":"large hard stone, rock, boulder, and rocks","branch_kind":null,"branch_ref":"root_000847/B001","candidate_links":[{"candidate_id":"cand_82e52fdf8e233a79c4c9","lane":"macro"},{"candidate_id":"cand_4c926d5a4f75fdabdf2f","lane":"macro"}],"focus_root_occurrences":[],"gloss":"hard massive rock","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الصخر الصلب العظيم","image_en":"hard massive rock"}}],"root_ar":"ص خ ر","root_id":"root_000847","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الصخر الصلب العظيم","image_en":"hard massive rock","scope_ar":"الحجر الصلب العظيم والصخرة والصخور والحجارة العظام","scope_en":"large hard stone, rock, boulder, and rocks"},"support_links":["sup_81901d9a83302d38f27b","sup_f4c672d2b411e02865d1"]},{"boundary":"Dal, malı bölme, yemin etme, öğle sıcağı ve öteki eşsesli anlamları kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001226/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"yüz güzelliği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüzde veya insan görünüşünde algılanan güzellik niteliğini bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güzel yüzün kendisini ya da güzel yüzlü kişiyi niteleyen kullanımları kapsar."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın soyut güzellik çekirdeğini ve güzelliğin özellikle yüzde görünmesini birlikte karşılar.","boundary_detail":"Dal, malı bölme, yemin etme, öğle sıcağı ve öteki eşsesli anlamları kapsamaz.","branch_image_ar":"حسن موزع في الوجه","concept_gloss":"yüz güzelliği","contextual_glosses":[{"applicability":"Bir kişiyi yüzünün güzelliğiyle niteleyen kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Soyut güzellik adı olarak kullanılabilme yönünü dışarıda bırakır.","preserves":"Kişinin yüz güzelliğini ve olumlu görünüşünü korur."},"facet_ids":["F002"],"text":"güzel yüzlü","usage_role":"contextual"},{"applicability":"Doğrudan yüzün kendisinin güzel diye nitelendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin bütünü için kullanılan niteleme ve soyut nitelik adı kapsamını kaybeder.","preserves":"Güzelliğin yüzde gerçekleşmesi yönünü korur."},"facet_ids":["F001","F002"],"text":"güzel yüz","usage_role":"contextual"}],"definition":"Yüzde ya da kişinin görünüşünde beliren güzellik ve yüz güzelliği niteliğidir. Bazı kullanımlar doğrudan güzel yüzü, bazıları da böyle bir yüze sahip kişiyi niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüzde veya insan görünüşünde algılanan güzellik niteliğini bildirir."},{"facet_id":"F002","role":"specialization","statement":"Güzel yüzün kendisini ya da güzel yüzlü kişiyi niteleyen kullanımları kapsar."}],"identity_rationale":"Kaynak ifadesi, güzelliği özellikle yüzde görülen bir nitelik olarak verir; hem soyut güzellik adlarını hem de güzel yüzlü kişi ve yüz betimlemelerini kapsar. Bu nedenle dalın yüz güzelliği ekseni kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"güzellik, güzel görünüş"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"eksiksiz güzellik"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yüz, özellikle yüzün güzel bölümü"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yakışıklı ya da güzel yaradılışlı erkek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"güzel yüzlü"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yüzü güzel ve uyumlu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"güzel yüz"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"güzel yüzlü kadın"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"güzel"}],"lexicalization_note":"Tanım, yalın güzellik adlarıyla yüzü niteleyen kalıpları ayırır; kalıba bağlı kişi nitelemelerini bütün dalın tek biçimi saymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca genel güzellik ve yüz uyumu dalları, yüz merkezli sınırı açıklayan yararlı karşılaştırmalar sundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yüz merkezli ve kişi nitelemelerine açıkken komşu dal nesnelere de uzanan genel güzellik ile kusursuzluğu bir araya getirir.","focus_only":"Güzelliği özellikle insan yüzünde ve güzel yüzlü kişi nitelemelerinde toplar.","gloss":"güzellik ve kusursuzluk","neighbor_only":"Her türlü şeyin güzelliğini ve kusurdan arınmışlığını daha geniş biçimde kapsar.","neighbor_ref":"root_000660/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin ya da yüzün güzel oluşunu bildirir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği güzelliktir; komşu dalın çekirdeği ise güzelliği doğuran yüz oranlarının karşılıklı dengelenmesidir.","focus_only":"Yüz güzelliğini uyumun nasıl kurulduğunu şart koşmadan bildirir.","gloss":"yüz güzelliğindeki uyum","neighbor_only":"Yüz parçalarının birbirine denk ve dengeli oluşunu güzelliğin belirleyici koşulu yapar.","neighbor_ref":"root_001511/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal yüzün güzel görünmesi alanında buluşur."}],"source_phrase_ar":"القسام وهو الحسن والجمال (maqayis)؛ القسيم من الرجال الحسن الخلق والقسمة الوجه (ayn)؛ القسام: الحسن وفلان قسيم الوجه ومقسم الوجه (sihah)؛ القسامة: الحسن التام ووجه مقسم أي حسن (tahdhib)؛ فلان مقسم الوجه وقسيم الوجه والقسامة الحسن (mufradat)","source_summary":"Kaynaklar, bu anlam alanında güzelliği ve yüz güzelliğini ortak çekirdek olarak verir; ad ve niteleme biçimleri güzel yüzü veya güzel yüzlü kişiyi anlatır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه حسن الوجه والقسمة والقسامة بمعنى الحسن، ووصف الرجل أو الوجه بأنه قسيم أو مقسم.","what_is_not_ar":"ليس هو تقسيم المال أو الحظوظ، ولا اليمين، ولا الاستقسام بالأزلام."},"support_links":[]},{"boundary":"Anlam, genel sıcaklığa değil özellikle gün ortasındaki şiddetli sıcağa veya onun vaktine bağlıdır.","branch_kind":"bare","branch_ref":"root_001226/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"şiddetli öğle sıcağı veya vakti","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gün ortasında hissedilen şiddetli sıcağı bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı söz, şiddetli öğle sıcağının yaşandığı vakti de adlandırır."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynaklardaki sıcaklık yoğunluğu ile gün ortası zamanı okumalarının ikisini de açıkça taşır.","boundary_detail":"Anlam, genel sıcaklığa değil özellikle gün ortasındaki şiddetli sıcağa veya onun vaktine bağlıdır.","branch_image_ar":"حر الهاجرة","concept_gloss":"şiddetli öğle sıcağı veya vakti","contextual_glosses":[{"applicability":"Sözün sıcaklığın şiddetini anlattığı metinlerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sözcüğün doğrudan bir vakti adlandırabildiği okumasını kaybeder.","preserves":"Gün ortasındaki sıcaklığın yüksek şiddetini korur."},"facet_ids":["F001"],"text":"kavurucu öğle sıcağı","usage_role":"contextual"},{"applicability":"Sözün günün sıcak bir zaman dilimini adlandırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıcağın şiddetini başlı başına adlandıran okumayı geri plana iter.","preserves":"Gün ortasıyla sıcaklığın birlikte belirlediği vakti korur."},"facet_ids":["F002"],"text":"öğle sıcağı vakti","usage_role":"contextual"}],"definition":"Gün ortasında bastıran şiddetli sıcak ya da bu sıcağın yaşandığı vakittir. Kaynak anlatımı yoğunluk ile zaman adlandırmasını yan yana bırakır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gün ortasında hissedilen şiddetli sıcağı bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı söz, şiddetli öğle sıcağının yaşandığı vakti de adlandırır."}],"identity_rationale":"Kaynak ifadesi tek bir noktada birleşmez: bir aktarım sözcüğü öğle sıcağının şiddeti, diğeri ise bu sıcağın görüldüğü vakit olarak açıklar. Dal korunabilir, ancak hem yoğunluk hem zaman okuması açıkça belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"şiddetli öğle sıcağı veya öğle sıcağı vakti"}],"lexicalization_note":"Tanım yalın dalı kapsar ve başka dallardaki güzellik, bölüştürme ya da yemin anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gün ortası sıcağı dalı tam örtüşme, yaz sıcağı dalı ise zaman sınırını gösteren yakın karşılaştırma sağladı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek anlam ve sınırlar aynıdır; komşu karttaki hareket ve yemek bağlantıları bu ortak çekirdeğin bağımlı kullanımlarıdır.","focus_only":null,"gloss":"öğle sıcağı ve vakti","neighbor_only":null,"neighbor_ref":"root_001578/B005","relation_type":"synonym","shared_zone":"Her iki dal da gün ortasındaki şiddetli sıcağı ve bu sıcağın vaktini çekirdek anlam yapar."},{"boundary_match":"partial","distinction":"Odak dal gün ortasıyla sınırlıyken komşu dal yaz mevsimi ve sıcak dönemin süresi üzerinden daha geniş bir zaman çerçevesi kurar.","focus_only":"Sıcağı özellikle gün ortasına bağlar ve vakit adı olarak da kullanır.","gloss":"şiddetli yaz sıcağı","neighbor_only":"Şiddetli yaz sıcağını veya bunun sürdüğü dönemi gün ortası şartı olmadan anlatır.","neighbor_ref":"root_001672/B004","relation_type":"near_synonym","shared_zone":"İki dal da ağır ve bunaltıcı sıcaklık alanını paylaşır."}],"source_phrase_ar":"والقسام في شعر النابغة شدة الحر (maqayis)؛ القسام: وقت الهاجرة (tahdhib)","source_summary":"Toplu kaynak anlatımı, sözü bir yandan şiddetli öğle sıcağına, öte yandan bu sıcağın vaktine bağlar; bu iki okuma tek bir yoğun gün ortası sahnesinde birleşir.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه القسام بمعنى شدة الحر أو وقت الهاجرة كما في الشواهد.","what_is_not_ar":"ليس هو القسام بمعنى الحسن، ولا القسام الذي يقسم بين الناس."},"support_links":[]},{"boundary":"Dal, yemin etmeyi ve payın ok çekerek aranmasını değil gerçek bölme, dağıtma ve belirlenmiş payı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001226/B003","candidate_links":[{"candidate_id":"cand_b1c0b25598981381b1f9","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"paylara ayırma ve ayrılmış pay","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünü parçalara, kişilere veya belirlenmiş paylara ayırma ve dağıtma işlemini bildirir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayırma işlemi sonunda bir kimseye düşen belirli payı veya hakkı bildirir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birlikte paylaşan kişiyi ve miras ya da savaş kazancının hak sahiplerine dağıtılmasını kapsar."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İşlem olarak bölüştürmeyi ve sonuç olarak belirlenen payı aynı kısa karşılıkta korur.","boundary_detail":"Dal, yemin etmeyi ve payın ok çekerek aranmasını değil gerçek bölme, dağıtma ve belirlenmiş payı kapsar.","branch_image_ar":"إفراز النصيب وتقسيم الشيء","concept_gloss":"paylara ayırma ve ayrılmış pay","contextual_glosses":[{"applicability":"Bir şeyin kişiler veya paylar arasında dağıtıldığı işlem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşlem sonunda ortaya çıkan belirli payı ad olarak karşılamaz.","preserves":"Bütünü paylara ayırma ve dağıtma işlemini korur."},"facet_ids":["F001","F003"],"text":"bölüştürme","usage_role":"general"},{"applicability":"Bir bölüştürme sonucunda kişiye düşen bölümün anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bütünü ayırma ve payları dağıtma işlemini karşılamaz.","preserves":"Bir kimseye ayrılan belirli bölüm veya hak sonucunu korur."},"facet_ids":["F002"],"text":"pay","usage_role":"contextual"}],"definition":"Bir şeyi parçalara ya da hak sahiplerinin paylarına ayırma ve dağıtma işlemidir; ayrıca bu işlem sonunda ayrılan payı bildirir. Paylaşmaya katılan kişi ve miras ya da ganimetin sahiplerine dağıtılması bu çekirdeğin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünü parçalara, kişilere veya belirlenmiş paylara ayırma ve dağıtma işlemini bildirir."},{"facet_id":"F002","role":"core","statement":"Ayırma işlemi sonunda bir kimseye düşen belirli payı veya hakkı bildirir."},{"facet_id":"F003","role":"specialization","statement":"Birlikte paylaşan kişiyi ve miras ya da savaş kazancının hak sahiplerine dağıtılmasını kapsar."}],"identity_rationale":"Kaynak ifadesi bir bütünü parçalara veya hak sahiplerine ayırma işlemini, bu işlemle belirlenen payı ve paylaşmaya katılan kişiyi birlikte verir. Dalın işlem ve sonuç ayrımı bu içeriği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir şeyi parçalara veya paylara ayırmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"paylara ayırma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"pay, kişiye düşen bölüm"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bölüştürme, paylaşma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"arazi veya evleri paylaştıran kimse"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"birlikte paylaşan ortak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"öteki araziden ayrılmış arazi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"az suyu eşit paylaştırmaya yarayan taş"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kişilere ayrılmış paylar"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ayırma ve dağıtma"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"zaman onları ayırıp dağıttı"}],"lexicalization_note":"Tanım yalın bölme ve pay anlamlarını korurken belirli nesne, kişi ve araç kalıplarını bağımlı özel kullanımlar olarak ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel dağıtma, belirli hisse ve ortaklık dalları işlem, sonuç ve ortak sahiplik sınırlarını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirlenmiş pay ve hak sahibi yapısını korurken komşu dalın çekirdeği daha genel ayırma ve dağıtmadır.","focus_only":"Bölme işleminin yanında ayrılmış payı ve paylaşmaya katılan kişiyi de kapsar.","gloss":"bölme ve dağıtma","neighbor_only":"Dağılma ve genel dağıtma yönünü, belirli bir pay sonucu gerektirmeden öne çıkarır.","neighbor_ref":"root_001644/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir bütünü parçalara ayırma ve parçaları dağıtma işlemini bildirir."},{"boundary_match":"partial","distinction":"Odak dal işlem ile sonucu dengeler; komşu dalda belirli parça veya hisse, işlemin kendisinden daha merkezîdir.","focus_only":"Bütünün bölünme işlemini ve bölüştüren ya da birlikte paylaşan kişileri de kapsar.","gloss":"hisse ve pay","neighbor_only":"Bütünden kopan parçayı ve o parçanın birine verilmesini daha doğrudan öne çıkarır.","neighbor_ref":"root_000329/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir bütünden kişiye ayrılan payı ve payların bölüşülmesini kapsar."},{"boundary_match":"field_only","distinction":"Odak dalın çekirdeği ayırma ve pay belirlemedir; komşu dalın çekirdeği ise henüz ayrılmamış ortak sahiplik veya katılımdır.","focus_only":"Ortak veya tekil bir bütünü fiilen paylara ayırır ve her payı belirler.","gloss":"ortaklık ve katılma","neighbor_only":"Bir şeyin birden çok kişi arasında ortak olmasını ve ortakların ilişki kurmasını bildirir.","neighbor_ref":"root_000791/B001","relation_type":"same_field","shared_zone":"Her iki dal pay, ortaklar ve birden çok kişinin aynı mal üzerindeki ilişkisi alanında bulunur."}],"source_phrase_ar":"تجزئة شيء والنصيب قسم (maqayis)؛ القسم مصدر قسم والقسم الحظ من الخير والقسيم الذي يقاسمك أرضا أو مالا (ayn)؛ القسم مصدر قسمت الشئ والقسم الحظ والنصيب والتقسيم التفريق (sihah)؛ قسمت الشيء بينهم قسما وقسمة والقسم الحظ والنصيب (tahdhib)؛ القسم: إفراز النصيب وقسمة الميراث والغنيمة تفريقهما على أربابهما (mufradat)","source_summary":"Kaynaklar bölme, paylara ayırma ve dağıtma işlemiyle bu işlemden doğan pay üzerinde birleşir; ortaklaşa paylaşan kişi ile miras ve savaş kazancının sahiplerine verilmesi de bu çekirdeğe bağlanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه قسم الشيء وقسمته، وإفراز النصيب، والحظ والنصيب المقسوم، والقاسم والقسام، والقسيم الذي يقاسمك، وعزل أرض عن أرض، وتفريق الشيء أو الناس، وحصاة القسم في تسوية الماء.","what_is_not_ar":"ليس هو اليمين، ولا جمال الوجه، ولا طي القسامي، ولا حر الهاجرة."},"support_links":["sup_b20e502901c704330196"]},{"boundary":"Buradaki dağıtma, mal paylaştırma anlamı değil; öldürme davasında yeminlerin ilgililere bölüştürülmesidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001226/B004","candidate_links":[{"candidate_id":"cand_4c926d5a4f75fdabdf2f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"yemin etme ve öldürme davasında paylaştırılan yeminler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iddia veya söz için yemin etmeyi ve karşılıklı yeminleşmeyi bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Öldürme iddiasında yeminlerin öldürülen kişinin yakınlarına bölüştürüldüğü hukuk uygulamasını kapsar."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel yemin eylemiyle özel hukuk uygulamasındaki dağıtılmış yeminleri birlikte temsil eder.","boundary_detail":"Buradaki dağıtma, mal paylaştırma anlamı değil; öldürme davasında yeminlerin ilgililere bölüştürülmesidir.","branch_image_ar":"يمين مقسومة على أهلها","concept_gloss":"yemin etme ve öldürme davasında paylaştırılan yeminler","contextual_glosses":[{"applicability":"Genel olarak yemin etme veya verilen güçlü sözün adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öldürme davasında yeminlerin yakınlara paylaştırılması düzenini göstermez.","preserves":"Sözü yeminle güvenceye bağlama çekirdeğini korur."},"facet_ids":["F001"],"text":"yemin","usage_role":"general"},{"applicability":"Öldürme iddiasına özgü toplu yemin uygulamasının açıklanması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Her türlü yemin için geçerli olan genel eylem anlamını dışarıda bırakır.","preserves":"Yeminlerin öldürülen kişinin yakınları arasında dağıtılması özelliğini korur."},"facet_ids":["F002"],"text":"öldürme davasındaki paylaştırılmış yeminler","usage_role":"explanatory"}],"definition":"Bir sözün doğruluğunu güçlü bir tanıklık çağrısıyla güvenceye bağlayarak yemin etmedir. Özel hukuk kullanımında, öldürme iddiasında yeminlerin öldürülen kişinin yakınları arasında paylaştırılmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iddia veya söz için yemin etmeyi ve karşılıklı yeminleşmeyi bildirir."},{"facet_id":"F002","role":"specialization","statement":"Öldürme iddiasında yeminlerin öldürülen kişinin yakınlarına bölüştürüldüğü hukuk uygulamasını kapsar."}],"identity_rationale":"Kaynak ifadesi genel olarak yemin etmeyi ve bunun özel bir kökeni sayılan, öldürme davasında maktulün yakınlarına dağıtılan yeminleri birlikte açıklar. Dalın genel yemin ile özel hukuk uygulaması ayrımı bu yapıya uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yemin"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yemin etti"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"ona yemin etti veya onunla antlaştı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"Tanrı adına karşılıklı yemin ettiler"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"öldürme davasında yakınlara paylaştırılan yeminler"}],"lexicalization_note":"Tanım yalın yemin anlamıyla belirli yeminleşme ve öldürme davası kalıplarını ayırır; özel uygulamayı her yeminin zorunlu içeriği yapmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yemin dalı anlam yakınlığını, öldürme bedeli dalı ise özel hukuk alanındaki araç farkını görünür kıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Genel yemin alanında yakın olsalar da odak dalın belirleyici ek sınırı öldürme davasındaki dağıtılmış yeminlerdir.","focus_only":"Öldürme davasında yakınlara paylaştırılan yeminlerden oluşan özel uygulamayı da kapsar.","gloss":"yemin ve yemin etme","neighbor_only":"Çok yemin etme, birine yemin ettirme ve üzerine yemin edilen şeyi daha geniş biçimde kapsar.","neighbor_ref":"root_000349/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir sözü yemin yoluyla güçlü biçimde doğrulamayı bildirir."},{"boundary_match":"field_only","distinction":"Odak dal kanıtlama veya iddiayı destekleme aracı olarak yeminleri, komşu dal ise ceza yerine ödenen maddi bedeli merkez alır.","focus_only":"Öldürme iddiasını yeminlerin yakınlar arasında paylaştırılması yoluyla ele alır.","gloss":"öldürme bedeli","neighbor_only":"Öldürme karşılığında ödenen bedeli, bu bedeli ödeyen topluluğu ve bedel yoluyla çözümü bildirir.","neighbor_ref":"root_001036/B004","relation_type":"same_field","shared_zone":"İki dal da öldürme olayının hukukî sonuçları ve yakınların hak iddiası alanında yer alır."}],"source_phrase_ar":"اليمين فالقسم وأصل ذلك من القسامة وهي الأيمان تقسم على أولياء المقتول (maqayis)؛ القسم اليمين والفعل أقسم (ayn)؛ أقسمت حلفت وأصله من القسامة (sihah)؛ القسم اليمين وأقسمت إقساما وقسما والقسامة في الدم (tahdhib)؛ وأقسم: حلف وأصله من القسامة ثم صار اسما لكل حلف (mufradat)","source_summary":"Kaynaklar genel yemin anlamında birleşir ve bu anlamı, öldürme davasında yeminlerin yakınlara paylaştırıldığı özel uygulamayla ilişkilendirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه القسم بمعنى اليمين، وأقسم وحلف، وقاسمه حلف له، وتقاسموا بالله، والقسامة في الدم بوصفها أيمانا تقسم على أولياء المقتول.","what_is_not_ar":"ليس هو قسمة المال أو النصيب إلا من جهة الأصل الذي ترده المصادر إلى القسامة."},"support_links":["sup_f4c672d2b411e02865d1"]},{"boundary":"Dal yalnızca işaretli oklarla karar veya ayrılmış sonuç arama uygulamasına bağlıdır; genel bölüştürme ya da oyun oku anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001226/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"işaretli ok çekerek karar arama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İşaretli oklar çekerek ayrılmış sonucu ya da bir işi yapma veya bırakma kararını aramayı bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı türetim ayrıca birinden bir şeyi paylaştırmasını isteme anlamında aktarılır."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca işaretli oklarla yapılacak işi veya kişiye ayrılan sonucu belirleme uygulamasını karşılar.","boundary_detail":"Dal yalnızca işaretli oklarla karar veya ayrılmış sonuç arama uygulamasına bağlıdır; genel bölüştürme ya da oyun oku anlamı değildir.","branch_image_ar":"طلب القسم بالأزلام","concept_gloss":"işaretli ok çekerek karar arama","contextual_glosses":[{"applicability":"Bir eyleme girişme ya da ondan vazgeçme kararının ok çekmeyle arandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiye önceden ayrılmış sonucu öğrenme yönünü açıkça karşılamaz.","preserves":"Ok çekme aracını ve yapma ya da bırakma kararını korur."},"facet_ids":["F001"],"text":"işaretli oklarla yapıp yapmamaya karar vermek","usage_role":"explanatory"}],"definition":"Üzerinde yönlendirme işaretleri bulunan okları çekerek kişiye ayrılmış sonucu veya bir işi yapıp yapmamayı belirlemeye çalışma uygulamasıdır. Aynı türetimin birinden paylaştırmasını isteme kullanımı, çekirdeğin dışında bir kaynak çeşitlemesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İşaretli oklar çekerek ayrılmış sonucu ya da bir işi yapma veya bırakma kararını aramayı bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı türetim ayrıca birinden bir şeyi paylaştırmasını isteme anlamında aktarılır."}],"identity_rationale":"Kaynak ifadesinin ana bölümü, üzerinde yönlendirme işaretleri bulunan okları çekerek kişiye ayrılan sonucu veya yapılacak işi aramayı anlatır. Aynı toplu iddia daha geniş biçimde birinden paylaştırmasını istemeyi de anar; bu ikinci kullanım, oklarla yapılan uygulamanın çekirdeğine genellenemez.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"işaretli ok çekerek ayrılmış sonucu veya yapılacak işi belirleme"}],"lexicalization_note":"Tanım açıkça işaretli oklarla kurulan yapıya bağlıdır; aynı türetimin genel olarak paylaştırma isteme kullanımı yalın dal anlamına çevrilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; fiziksel ok ve araç adları anlam sınırını keskinleştirmedi, yalnızca gerçek paylaştırma dalı yararlı bir karşıtlık sundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal işaretli oklarla bilgi ya da karar arayan bir uygulamadır; komşu dal ise gerçek bir nesneyi veya hakkı paylaştırma işlemidir.","focus_only":"İşaretli oklar çekerek gelecekte yapılacak işi veya kişiye ayrıldığı düşünülen sonucu arar.","gloss":"paylara ayırma","neighbor_only":"Bir bütünü fiilen parçalara ve hak sahiplerinin paylarına ayırır.","neighbor_ref":"root_001226/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişiye düşen bölüm veya sonuç düşüncesi çevresinde ilişki kurar."}],"source_phrase_ar":"الاستقسام أنهم كانوا يجيلون السهام أي الأزلام (ayn)؛ واستقسم: طلب القسم بالازلام (sihah)؛ تستقسموا بالأزلام معناه تطلبوا من جهة الأزلام وما كتب عليها ما قسم لكم (tahdhib)؛ واستقسمته: سألته أن يقسم ثم قد يستعمل في معنى قسم (mufradat)","source_summary":"Toplu kaynak anlatımı, işaretli okları çevirip çekerek kişiye ayrılmış sonucu veya yapılacak işi arama uygulamasında birleşir; ayrıca aynı türetimin genel paylaştırma isteme kullanımı bulunduğunu belirtir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الاستقسام بالأزلام والقداح، أي طلب ما قسم أو تعيين المضي والترك بضرب السهام.","what_is_not_ar":"ليس هو مطلق القسمة بين الشركاء، ولا اليمين، ولا قداح الميسر حين تفرقها المصادر عن أزلام الأمر والنهي."},"support_links":[]},{"boundary":"Bu dal maddi bir şeyi paylaştırmayı değil, kararın seçeneklere ayrılmasını veya zihnin kaygılarla dağılmasını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001226/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"işi ölçüp biçme; kaygıyla zihnin dağılması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işin nasıl yapılacağını ölçüp biçme ve seçenekleri değerlendirme sürecini bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaygıların zihni veya kalbi farklı yönlere çekerek düşünceyi dağıtmasını bildirir."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın karar değerlendirmesi ile kaygı kaynaklı zihinsel dağılma kullanımlarını ayrı bölümler halinde korur.","boundary_detail":"Bu dal maddi bir şeyi paylaştırmayı değil, kararın seçeneklere ayrılmasını veya zihnin kaygılarla dağılmasını anlatır.","branch_image_ar":"بال مقسم بين وجوه الأمر","concept_gloss":"işi ölçüp biçme; kaygıyla zihnin dağılması","contextual_glosses":[{"applicability":"Bir kişinin nasıl davranacağını düşünüp seçenekleri değerlendirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaygıların zihni farklı yönlere dağıtması anlamını dışarıda bırakır.","preserves":"Bir işin uygulanışını düşünme ve seçenekleri değerlendirme sürecini korur."},"facet_ids":["F001"],"text":"işi ölçüp biçmek","usage_role":"contextual"},{"applicability":"Kaygıların kişinin düşüncesini birçok yöne çektiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işi planlayarak nasıl yapacağını değerlendirme anlamını karşılamaz.","preserves":"Kaygı nedeniyle düşüncenin bölünüp dağılması sonucunu korur."},"facet_ids":["F002"],"text":"kaygıdan zihni dağılmak","usage_role":"contextual"}],"definition":"Bir işi nasıl yürüteceğini ölçüp biçerek seçenekleri değerlendirmeyi anlatır. Başka bir kullanımda, kaygıların kişinin düşüncesini farklı yönlere çekip dağıtmasını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işin nasıl yapılacağını ölçüp biçme ve seçenekleri değerlendirme sürecini bildirir."},{"facet_id":"F002","role":"extension","statement":"Kaygıların zihni veya kalbi farklı yönlere çekerek düşünceyi dağıtmasını bildirir."}],"identity_rationale":"Kaynak ifadesi bölme düşüncesini zihinsel alana iki ayrı biçimde taşır: kişi bir işi nasıl yapacağını ölçüp biçer veya kaygılar düşüncesini farklı yönlere dağıtır. Dal, bu iki kullanımı birbirine karıştırmadan ayırdığı sürece kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"işini ölçüp biçiyor ve nasıl yapacağını düşünüyor"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"kaygının dağıttığı zihin"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"kaygılar yüzünden düşüncesi dağılmış"}],"lexicalization_note":"Tanım, işi ölçüp biçme yapısıyla kaygılı zihin nitelemelerini ayrı tutar ve bunlardan genel bir yalın bölme anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; görüş karışıklığı ve tek olmayan görüş dalları zihinsel bölünmenin nedenini ve katılımcı yapısını ayırt etmeye yaradı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal değerlendirme sürecini de içerebilir ve dağılmayı kaygıya bağlar; komşu dalda belirleyici olan kuşku ve görüş karışıklığıdır.","focus_only":"Ya bilinçli seçenek değerlendirmesini ya da kaygının düşünceyi yönlere ayırmasını bildirir.","gloss":"kararsız ve karışık görüş","neighbor_only":"Kişinin görüşünde kuşkuya düşmesini ve ne yapacağını bilemeyecek ölçüde karışmasını bildirir.","neighbor_ref":"root_000576/B005","relation_type":"near_neighbor","shared_zone":"İki dal da düşüncenin tek bir kararlı yönde ilerleyemediği zihinsel durumu kapsar."},{"boundary_match":"partial","distinction":"Odak dal içsel değerlendirme ya da kaygı kaynaklı dağılmadır; komşu dalın ayrılığı ise görüşün ortaklaşa taşınması veya kişinin kendine seslenmesidir.","focus_only":"Tek kişinin zihninin seçenekler veya kaygılar arasında bölünmesini anlatır.","gloss":"ortak veya tek olmayan görüş","neighbor_only":"Bir görüşün birden çok kişi arasında ortak olmasını veya kişinin kendi kendine konuşmasını anlatır.","neighbor_ref":"root_000791/B008","relation_type":"near_neighbor","shared_zone":"İki dal da düşüncenin tek ve yalın bir yön taşımaması noktasında buluşur."}],"source_phrase_ar":"أمسى فلان متقسما أي كأن خواطر الهموم تقسمته (maqayis)؛ هو يقسم أمره قسما أي يقدره وينظر فيه كيف يفعل (sihah)؛ يقسم أمره قسما أي يقدره ينظر كيف يعمل فيه (tahdhib)؛ رجل منقسم القلب أي اقتسمه الهم (mufradat)","source_summary":"Kaynaklar bölünme tasarımını zihinsel alana taşır: bir kullanım işi nasıl yapacağını düşünüp tartmayı, öteki kullanım ise kaygıların zihni bölüp dağıtmasını anlatır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه تقسيم الأمر بمعنى تقديره والنظر كيف يفعل، وتوزع القلب أو الخاطر بالهموم.","what_is_not_ar":"ليس هو التقسيم الحسي للمال أو الأرض، ولا الاستقسام بالأزلام."},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_001226/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"yalıtık adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Giysileri ilk kez katlayıp kumaşta ilk kat izlerini oluşturan kişiyi bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin iki durum arasında bulunmasını, özellikle bir atın iki gelişim evresi arasında kalmasını bildirir."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"طي القسامي أول الثوب","concept_gloss":"yalıtık adlandırmalar","contextual_glosses":[{"applicability":"Kumaşın ilk kez katlanıp kat izlerinin oluşturulduğu meslek veya iş bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki durum arasında bulunan şey veya hayvan anlamını dışarıda bırakır.","preserves":"Giysiyi ilk kez katlayan kişiyi ve ilk kat oluşturma işini korur."},"facet_ids":["F001"],"text":"giysinin ilk katını yapan kimse","usage_role":"explanatory"},{"applicability":"Bir varlığın iki gelişim durumu arasında kaldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Giysiyi ilk kez katlayan kişi anlamını dışarıda bırakır.","preserves":"Bir varlığın iki ayrı durum arasında bulunması özelliğini korur."},"facet_ids":["F002"],"text":"iki durum arasında bulunan","usage_role":"explanatory"}],"definition":"Kayıt, bir yanda giysileri ilk kez katlayarak kat yerlerini oluşturan kişiyi, öte yanda iki durum arasında bulunan şeyi anlatır. Bu iki anlam tek bir kavram değildir ve ayrı dallar gerektirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Giysileri ilk kez katlayıp kumaşta ilk kat izlerini oluşturan kişiyi bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Bir şeyin iki durum arasında bulunmasını, özellikle bir atın iki gelişim evresi arasında kalmasını bildirir."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"giysiyi ilk kez katlayıp kat izlerini oluşturan kimse"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"iki durum arasında bulunan, özellikle iki gelişim evresi arasındaki at"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"القسامى وهو الذي يطوى الثياب أول طيها (maqayis)؛ القسامى الذى يطوى الثياب أول طيها حتى تتكسر على طيه (sihah)؛ القسامي الذي يطوي الثياب أول طيها والقسامي الذي يكون بين شيئين (tahdhib)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه القسامي الذي يطوي الثياب أول طيها، وما ألحق به من كونه بين شيئين في وصف الفرس.","what_is_not_ar":"ليس هو القاسم الذي يقسم المال، ولا القسام بمعنى الحسن أو الحر."},"support_links":[]},{"boundary":"Bu dal genel barışın bütün türlerini, yüz güzelliğini veya öldürme davasındaki yeminleri kapsamaz.","branch_kind":"bare","branch_ref":"root_001226/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"düşman ile Müslümanlar arasındaki ateşkes","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Düşman ile Müslümanlar arasında çatışmayı durduran ateşkesi bildirir."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakta belirtilen iki taraf arasında çatışmanın durdurulduğu özel ateşkes anlamını karşılar.","boundary_detail":"Bu dal genel barışın bütün türlerini, yüz güzelliğini veya öldürme davasındaki yeminleri kapsamaz.","branch_image_ar":"هدنة قسامة","concept_gloss":"düşman ile Müslümanlar arasındaki ateşkes","contextual_glosses":[{"applicability":"Tarafların metinde zaten açık olduğu ve çatışmaya ara verilmesinin anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":"Kaynakta belirtilen taraflar dışındaki her türlü ateşkese uygulanabilen daha geniş bir kapsam ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Çatışmanın anlaşmayla durdurulması çekirdeğini korur."},"facet_ids":["F001"],"text":"ateşkes","usage_role":"contextual"}],"definition":"Düşman ile Müslümanlar arasında çatışmaya ara veren ateşkestir. Kaynak, tarafları ve savaşın geçici olarak durmasını anlamın sınırı olarak verir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Düşman ile Müslümanlar arasında çatışmayı durduran ateşkesi bildirir."}],"identity_rationale":"Kaynak ifadesi anlamı doğrudan düşman ile Müslümanlar arasındaki çatışmasızlık anlaşması olarak verir. Dalın ateşkes çerçevesi bu tekil aktarımı eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"düşman ile Müslümanlar arasındaki ateşkes"}],"lexicalization_note":"Tanım yalın dalı kaynakta belirtilen taraflar arasındaki ateşkesle sınırlar ve başka barış türlerine kendiliğinden genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; karşılıklı çatışmayı bırakma ve genel barış dalları ateşkesin taraf ve süre bakımından daha dar sınırını gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli taraflar arasındaki ateşkestir; komşu dal tarafları sınırlamayan ve uzlaşma ile saldırmama sözünü de kapsayan daha geniş bir bırakışmadır.","focus_only":"Tarafları özellikle düşman ile Müslümanlar olarak sınırlar.","gloss":"karşılıklı çatışmayı bırakma","neighbor_only":"Karşılıklı saldırmama, uzlaşma, savaşı bırakma ve savaş açmama sözü gibi daha geniş anlaşma türlerini kapsar.","neighbor_ref":"root_001635/B004","relation_type":"near_synonym","shared_zone":"İki dal da karşıt tarafların çatışmayı bırakması ve bir süre saldırmaması alanında buluşur."},{"boundary_match":"partial","distinction":"Ateşkes geçici ve tarafları belirli bir çatışma düzenlemesidir; komşu dal daha genel ve kalıcı olabilen barış durumunu anlatır.","focus_only":"Belirli taraflar arasında çatışmaya ara veren sınırlı ateşkesi bildirir.","gloss":"barış ve uzlaşma","neighbor_only":"Savaşın karşıtı olarak genel barış, uzlaşma ve barış içinde olma durumunu kapsar.","neighbor_ref":"root_000737/B004","relation_type":"near_synonym","shared_zone":"Her iki dal silahlı çatışmanın durması ve tarafların savaşmaması durumunu içerir."}],"source_phrase_ar":"القسامة: الهدنة بين العدو وبين المسلمين (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu anlam yalnızca bir kaynakta, düşman ile Müslümanlar arasındaki ateşkes olarak aktarılır."}],"source_summary":"Tek kaynaklı aktarım, sözü düşman ile Müslümanlar arasındaki ateşkes olarak tanımlar ve başka bir barış ya da yemin anlamı eklemez.","sources":["TA"],"what_is_ar":"يدخل فيه القسامة بمعنى الهدنة بين العدو وبين المسلمين.","what_is_not_ar":"ليس هو القسامة بمعنى الحسن، ولا القسامة في الدم والأيمان."},"support_links":[]},{"boundary":"The known valley: an opening among mountains, hills, or mounds that serves as a path or outlet for floodwater; plural الأودية.","branch_kind":null,"branch_ref":"root_001637/B005","candidate_links":[{"candidate_id":"cand_82e52fdf8e233a79c4c9","lane":"macro"}],"focus_root_occurrences":[],"gloss":"valley as a flood channel","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الوادي مسلك السيل","image_en":"valley as a flood channel"}}],"root_ar":"و د ي","root_id":"root_001637","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الوادي مسلك السيل","image_en":"valley as a flood channel","scope_ar":"الوادي المعروف؛ مفرج بين جبال وآكام وتلال؛ مسلك للسيل أو منفذ؛ جمعه الأودية","scope_en":"The known valley: an opening among mountains, hills, or mounds that serves as a path or outlet for floodwater; plural الأودية."},"support_links":["sup_81901d9a83302d38f27b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000434/B001","candidate_links":[{"candidate_id":"cand_4c926d5a4f75fdabdf2f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_72506be5c3bcc624172f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Measuring and proportioning a thing supplies designed scale rather than accidental bulk.","root":"خ ل ق","source_ref":"89:8","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000434","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_f4c672d2b411e02865d1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000566/B001","candidate_links":[{"candidate_id":"cand_4c926d5a4f75fdabdf2f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_72506be5c3bcc624172f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Watchful guarding supplies a final boundary that observes those who would not guard themselves.","root":"ر ص د","source_ref":"89:14","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000566","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_f4c672d2b411e02865d1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000702/B001","candidate_links":[{"candidate_id":"cand_b1c0b25598981381b1f9","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_98b716b9e90978045d95","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Night travel supplies ordered passage across the boundaries just established.","root":"س ر ي","source_ref":"89:4","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000702","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b20e502901c704330196"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000802/B001","candidate_links":[{"candidate_id":"cand_b1c0b25598981381b1f9","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_98b716b9e90978045d95","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Joining a thing to its like supplies the paired class within the partition.","root":"ش ف ع","source_ref":"89:3","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000802","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b20e502901c704330196"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000937/B001","candidate_links":[{"candidate_id":"cand_4c926d5a4f75fdabdf2f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_72506be5c3bcc624172f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Crossing the limit supplies the failure of inward boundary despite external mastery.","root":"ط غ ي","source_ref":"89:11","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000937","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_f4c672d2b411e02865d1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001016/B002","candidate_links":[{"candidate_id":"cand_b1c0b25598981381b1f9","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_98b716b9e90978045d95","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Completion of nine by a tenth supplies a closed counted span.","root":"ع ش ر","source_ref":"89:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001016","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b20e502901c704330196"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001043/B003","candidate_links":[{"candidate_id":"cand_4c926d5a4f75fdabdf2f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_72506be5c3bcc624172f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Columns and supports supply conspicuous external structure.","root":"ع م د","source_ref":"89:7","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001043","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_f4c672d2b411e02865d1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001132/B002","candidate_links":[{"candidate_id":"cand_b1c0b25598981381b1f9","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_98b716b9e90978045d95","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Dawn emerging from night supplies the first temporal cut.","root":"ف ج ر","source_ref":"89:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001132","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b20e502901c704330196"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001154/B001","candidate_links":[{"candidate_id":"cand_4c926d5a4f75fdabdf2f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_72506be5c3bcc624172f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Departure from soundness and equilibrium supplies the consequence of failed restraint.","root":"ف س د","source_ref":"89:12","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001154","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_f4c672d2b411e02865d1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001392/B001","candidate_links":[{"candidate_id":"cand_b1c0b25598981381b1f9","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_98b716b9e90978045d95","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Night as darkness supplies the bounded medium being counted and traversed.","root":"ل ي ل","source_ref":"89:2","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001392","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b20e502901c704330196"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001620/B001","candidate_links":[{"candidate_id":"cand_4c926d5a4f75fdabdf2f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_72506be5c3bcc624172f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Driven stakes supply fixation and imposed stability.","root":"و ت د","source_ref":"89:10","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001620","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_f4c672d2b411e02865d1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001621/B001","candidate_links":[{"candidate_id":"cand_b1c0b25598981381b1f9","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_98b716b9e90978045d95","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The singular without a pair supplies the complementary remainder.","root":"و ت ر","source_ref":"89:3","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001621","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b20e502901c704330196"]}],"candidate_inventory":[{"anchor_refs":["89:5","89:8","89:9"],"branch_refs":["root_000273/B001","root_000296/B003","root_000434/B011","root_000847/B001","root_001637/B005"],"candidate_id":"cand_82e52fdf8e233a79c4c9","commentary_obligation":"review","focus_branch_refs":["root_000296/B003"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000273/B001","root_000434/B011","root_000847/B001","root_001637/B005"],"root_ids":[],"scope":"pericope","source_local_id":"A:Cutting Rock Into a Valley Place","source_type":"channel","support_ids":["sup_4fc43ad56c262d861088","sup_601c13e4247efecd740a","sup_75b38b9f40f147abec64","sup_81901d9a83302d38f27b","sup_b941cb84e4c22613efb2"],"title":"Cutting Rock Into a Valley Place","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:1","89:2","89:3","89:4","89:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:5","branch_refs":["root_000296/B006","root_000702/B001","root_000802/B001","root_001016/B002","root_001132/B002","root_001226/B003","root_001392/B001","root_001621/B001"],"candidate_id":"cand_b1c0b25598981381b1f9","commentary_obligation":"review","hft_ref":"hft_98b716b9e90978045d95","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_counted_temporal_partition","source_type":"hft","support_ids":["sup_b20e502901c704330196"],"title":"delta_counted_temporal_partition","trust":"legacy_unbound"},{"anchor_refs":["89:10","89:11","89:12","89:14","89:5","89:7","89:8","89:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:5","branch_refs":["root_000273/B001","root_000296/B002","root_000296/B003","root_000434/B001","root_000566/B001","root_000847/B001","root_000937/B001","root_001043/B003","root_001154/B001","root_001226/B004","root_001620/B001"],"candidate_id":"cand_4c926d5a4f75fdabdf2f","commentary_obligation":"review","hft_ref":"hft_72506be5c3bcc624172f","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_monumental_hardness_vs_inner_limit","source_type":"hft","support_ids":["sup_f4c672d2b411e02865d1"],"title":"delta_monumental_hardness_vs_inner_limit","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_ffe63d5fcc242337a5d0","connection_ref":"conn_9cced10867569d693183","note":"Its fixed-constraint imagery sharpens the difference between power and disciplined restraint.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_a86959c43544cb83ae3d","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"89:10","source_note":"No focused connection beyond remote formal associations.","source_row_role":"ranked_review","source_target_component_ref":"89:5","source_target_components":["89:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:10","source_target_components":["89:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:10","target_evidence":{"arabic_uthmani":"وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ","ayah_ref":"89:10"},"target_ref":"89:10"},{"connection_evidence_ref":"conn_ev_e9da9fc6715d44a39eb5","connection_ref":"conn_c558d57f0be448243348","note":"It completes the immediately preceding oath series to which ذَٰلِكَ points.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_8399dd244cf5b37f1fab","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:4","source_note":"The immediate oath-frame channel supplies limited context rather than a reading of the verb.","source_row_role":"ranked_review","source_target_component_ref":"89:5","source_target_components":["89:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:4","source_target_components":["89:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:4","target_evidence":{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَسْرِ","ayah_ref":"89:4"},"target_ref":"89:4"},{"connection_evidence_ref":"conn_ev_b1386fbca406d8dab034","connection_ref":"conn_2499ea5186739f91e827","note":"The immediate historical example extends the sequence after the oath.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_86778d67b7dee57ad663","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"89:9","source_note":"No specific addition to the Thamud rock-valley scene.","source_row_role":"ranked_review","source_target_component_ref":"89:5","source_target_components":["89:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:9","source_target_components":["89:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:9","target_evidence":{"arabic_uthmani":"وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ","ayah_ref":"89:9"},"target_ref":"89:9"},{"connection_evidence_ref":"conn_ev_d61f25973a95aca12bce","connection_ref":"conn_02b0b8feb9df0f0778c3","note":"It opens the immediate oath series that 89:5 gathers under ذَٰلِكَ.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_e1133c3753c13f71e748","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"89:1","source_note":"The local oath's restraint frame supports measured thresholds indirectly.","source_row_role":"ranked_review","source_target_component_ref":"89:5","source_target_components":["89:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:1","source_target_components":["89:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:1","target_evidence":{"arabic_uthmani":"وَٱلْفَجْرِ","ayah_ref":"89:1"},"target_ref":"89:1"},{"connection_evidence_ref":"conn_ev_b1f554fd640e301dbd49","connection_ref":"conn_f6513f93e2d232d5f470","note":"Watchfulness fits the surrounding accountability, but adds no direct oath or حِجْر route.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_5262615cb12eff252d5b","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:14","source_note":"Provides an oath-context marker, not a reading of the watchpoint.","source_row_role":"ranked_review","source_target_component_ref":"89:5","source_target_components":["89:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:14","source_target_components":["89:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:14","target_evidence":{"arabic_uthmani":"إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ","ayah_ref":"89:14"},"target_ref":"89:14"},{"connection_evidence_ref":"conn_ev_bb66928a24ea3c3a28d6","connection_ref":"conn_32241bb7f3dfb7589006","note":"Its paired terms are a central element of the immediate oath series.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_8187d168b1de746d04dd","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"89:3","source_note":"Yemînlerin akıl sahibine hitabını tamamlar; anlam katkısı bağlamsaldır.","source_row_role":"ranked_review","source_target_component_ref":"89:5","source_target_components":["89:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:3","source_target_components":["89:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:3","target_evidence":{"arabic_uthmani":"وَٱلشَّفْعِ وَٱلْوَتْرِ","ayah_ref":"89:3"},"target_ref":"89:3"},{"connection_evidence_ref":"conn_ev_24157b020563aba5eeb1","connection_ref":"conn_992c2eeef275339a87c1","note":"It is another indispensable item in the immediate oath series.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_adfc9ab22aa0e1610a8c","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:2","source_note":"Immediate oath conclusion adds only broad rhetorical framing.","source_row_role":"ranked_review","source_target_component_ref":"89:5","source_target_components":["89:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:2","source_target_components":["89:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:2","target_evidence":{"arabic_uthmani":"وَلَيَالٍ عَشْرٍۢ","ayah_ref":"89:2"},"target_ref":"89:2"},{"connection_evidence_ref":"conn_ev_2661ebad4b0348b0bad5","connection_ref":"conn_5a6c0d99fc9c4795cf8b","note":"The immediate exemplum contributes scale and uniqueness to the oath's ensuing evidence.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_e4d0d183958cb63237bb","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:8","source_note":"Nearby language and channels are too indirect to specify the unmatched construction.","source_row_role":"ranked_review","source_target_component_ref":"89:5","source_target_components":["89:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:8","source_target_components":["89:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:8","target_evidence":{"arabic_uthmani":"ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ","ayah_ref":"89:8"},"target_ref":"89:8"},{"connection_evidence_ref":"conn_ev_a888087186dc69dba897","connection_ref":"conn_1b10f8b4719f830cd44d","note":"The immediate charge of excess supplies context but not a distinct reading of 89:5.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_46fddd16cb95e0507bf9","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"89:11","source_note":"The oath's appeal to restraint is too remote from the clause.","source_row_role":"ranked_review","source_target_component_ref":"89:5","source_target_components":["89:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:11","source_target_components":["89:11"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:11","target_evidence":{"arabic_uthmani":"ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ","ayah_ref":"89:11"},"target_ref":"89:11"},{"connection_evidence_ref":"conn_ev_3fc250e59029b0787e31","connection_ref":"conn_2a9294a0f6cb241cb2f0","note":"It begins the immediate historical proof sequence introduced after 89:5.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_2f1b69cc4df4ef2c0833","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:6","source_note":"Nearby oath closure; no material expansion of the focus.","source_row_role":"ranked_review","source_target_component_ref":"89:5","source_target_components":["89:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:6","source_target_components":["89:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:6","target_evidence":{"arabic_uthmani":"أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ","ayah_ref":"89:6"},"target_ref":"89:6"}],"focus":{"arabic_uthmani":"هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ","qac_morphemes":[{"lemma_ar":"هَل","morph_features":"STEM|POS:INTG|LEM:hal","morpheme_role":"STEM","pos":"INTG","qac_ref":"89:5:1:1","qac_word_ref":"89:5:1","root_ar":"","surface_ar":"هَلْ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"89:5:2:1","qac_word_ref":"89:5:2","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"ذَٰلِك","morph_features":"STEM|POS:DEM|LEM:*a`lik|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"89:5:3:1","qac_word_ref":"89:5:3","root_ar":"","surface_ar":"ذَٰلِكَ"},{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","root_ar":"ق س م","surface_ar":"قَسَمٌ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"89:5:5:1","qac_word_ref":"89:5:5","root_ar":"","surface_ar":"لِّ"},{"lemma_ar":"ذُو","morph_features":"STEM|POS:N|LEM:*uw|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:5:2","qac_word_ref":"89:5:5","root_ar":"","surface_ar":"ذِى"},{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","root_ar":"ح ج ر","surface_ar":"حِجْرٍ"}],"word_analysis_qac_refs":[["89:5:1:1"],["89:5:2:1"],["89:5:3:1"],["89:5:4:1"],["89:5:5:1"],["89:5:5:2"],["89:5:6:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:5:1","89:5:2","89:5:3","89:5:4","89:5:5","89:5:6","89:5:7"]},"focus_surface_evidence":{"arabic_uthmani":"هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ","qac_morphemes":[{"lemma_ar":"هَل","morph_features":"STEM|POS:INTG|LEM:hal","morpheme_role":"STEM","pos":"INTG","qac_ref":"89:5:1:1","qac_word_ref":"89:5:1","root_ar":"","surface_ar":"هَلْ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"89:5:2:1","qac_word_ref":"89:5:2","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"ذَٰلِك","morph_features":"STEM|POS:DEM|LEM:*a`lik|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"89:5:3:1","qac_word_ref":"89:5:3","root_ar":"","surface_ar":"ذَٰلِكَ"},{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","root_ar":"ق س م","surface_ar":"قَسَمٌ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"89:5:5:1","qac_word_ref":"89:5:5","root_ar":"","surface_ar":"لِّ"},{"lemma_ar":"ذُو","morph_features":"STEM|POS:N|LEM:*uw|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:5:2","qac_word_ref":"89:5:5","root_ar":"","surface_ar":"ذِى"},{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","root_ar":"ح ج ر","surface_ar":"حِجْرٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:5:1:1"],["89:5:2:1"],["89:5:3:1"],["89:5:4:1"],["89:5:5:1"],["89:5:5:2"],["89:5:6:1"]],"word_analysis_refs":["89:5:1","89:5:2","89:5:3","89:5:4","89:5:5","89:5:6","89:5:7"],"word_rows":[{"analysis_record_ref":"89:5:1","analytic_gloss_range_en":"yes-no interrogative particle whose local force is rhetorical recognition of the whole oath proposition","analytic_root_gloss_range_en":null,"qac_refs":["89:5:1:1"],"root":{"note":"—"},"surface":{"arabic":"هَلْ","transliteration":"hal"}},{"analysis_record_ref":"89:5:2","analytic_gloss_range_en":"preposition of containment and conceptual domain, fronting the prior oath sequence as the place where oath-force is tested","analytic_root_gloss_range_en":null,"qac_refs":["89:5:2:1"],"root":{"note":"—"},"surface":{"arabic":"فِى","transliteration":"fī"}},{"analysis_record_ref":"89:5:3","analytic_gloss_range_en":"distal demonstrative that packages the preceding oath sequence as one definite, reviewable discourse object","analytic_root_gloss_range_en":null,"qac_refs":["89:5:3:1"],"root":{"note":"—"},"surface":{"arabic":"ذَٰلِكَ","transliteration":"dhālika"}},{"analysis_record_ref":"89:5:4","analytic_gloss_range_en":"indefinite oath-value or binding attestation discovered inside the prior sequence and directed toward a qualified receiver","analytic_root_gloss_range_en":"root range includes oath-taking, apportioning, division, shares, and other peripheral branches; local grammar selects oath while division/allotment remains image-pressure","qac_refs":["89:5:4:1"],"root":{"arabic":"ق س م","transliteration":"q-s-m"},"surface":{"arabic":"قَسَمٌۭ","transliteration":"qasamun"}},{"analysis_record_ref":"89:5:5","analytic_gloss_range_en":"prefixed preposition of specialization, suitability, and audience, making the oath operative for the possessor of restraint","analytic_root_gloss_range_en":null,"qac_refs":["89:5:5:1"],"root":{"note":"—"},"surface":{"arabic":"لِّ","transliteration":"li"}},{"analysis_record_ref":"89:5:6","analytic_gloss_range_en":"genitive five-noun construct head meaning possessor or bearer, forming a generic receiver class defined by restraint","analytic_root_gloss_range_en":"root range centers on possessor, bearer, or one characterized by a construct complement, with other demonstrative or relative-pronoun branches not active locally","qac_refs":["89:5:5:2"],"root":{"arabic":"ذ و و","transliteration":"dh-w-w"},"surface":{"arabic":"ذِى","transliteration":"dhī"}},{"analysis_record_ref":"89:5:7","analytic_gloss_range_en":"possessed restraint or disciplined intellect, qualitative rather than titular, functioning as the faculty that can recognize the oath","analytic_root_gloss_range_en":"root range includes restraint, prohibition, enclosure, hard stone, protected places, and reason as restraining faculty; local construct selects cognitive restraint while boundary and enclosure pressure remains active","qac_refs":["89:5:6:1"],"root":{"arabic":"ح ج ر","transliteration":"ḥ-j-r"},"surface":{"arabic":"حِجْرٍ","transliteration":"ḥijr"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":7,"words_total":7,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":12,"missing_anchor_refs":[],"supplied_unique_anchor_count":12},"assigned_record_count":2,"assigned_records":[{"anchor_refs":["89:1","89:2","89:3","89:4","89:5"],"branch_refs":["root_000296/B006","root_000702/B001","root_000802/B001","root_001016/B002","root_001132/B002","root_001226/B003","root_001392/B001","root_001621/B001"],"candidate_id":"cand_b1c0b25598981381b1f9","evidence_scope":"declared_pericope","hft_ref":"hft_98b716b9e90978045d95","item_id":"delta_counted_temporal_partition","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_counted_temporal_partition","support_id":"sup_b20e502901c704330196"},{"anchor_refs":["89:10","89:11","89:12","89:14","89:5","89:7","89:8","89:9"],"branch_refs":["root_000273/B001","root_000296/B002","root_000296/B003","root_000434/B001","root_000566/B001","root_000847/B001","root_000937/B001","root_001043/B003","root_001154/B001","root_001226/B004","root_001620/B001"],"candidate_id":"cand_4c926d5a4f75fdabdf2f","evidence_scope":"declared_pericope","hft_ref":"hft_72506be5c3bcc624172f","item_id":"delta_monumental_hardness_vs_inner_limit","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_monumental_hardness_vs_inner_limit","support_id":"sup_f4c672d2b411e02865d1"}],"diagnostics":[],"lane_counts":{"global":15,"macro":2,"micro":3},"packet_summary":{"ayah_count":30,"focus_ref":"89:5","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:5","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":12,"unstructured_record_count":0},"identity":{"ayah_ref":"89:5","lane":"macro","linguistic_source_ref":"89:5","surface_ref":"89:5","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:5","target_tokens":[["Bunlarda",["89:5:2","89:5:3"]],["akıl",["89:5:6"]],["sahibi",["89:5:5","89:5:6"]],["için",["89:5:5"]],["bir",["89:5:4"]],["yemin",["89:5:4"]],["yok",["89:5:1"]],["mu",["89:5:1"]]],"text":"Bunlarda akıl sahibi için bir yemin yok mu?"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":2,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":14,"id":"s089-p01-001-014","label":"Oaths and the downfall of tyrants","number":1,"refs":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"89:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"89:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["89:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"89:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Cutting Rock Into a Valley Place","source_type":"channel","support_id":"sup_4fc43ad56c262d861088","text":"Hard stone is pierced or excavated within a valley to create usable space.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Cutting Rock Into a Valley Place","source_type":"channel","support_id":"sup_601c13e4247efecd740a","text":"89:9 (جابوا، الصخر، الواد); 89:5 (حجر); 89:8 (يخلق)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Cutting Rock Into a Valley Place","source_type":"channel","support_id":"sup_75b38b9f40f147abec64","text":"Stable places are made by cutting, leveling, bounding, supporting, and directing material.","trust":"trusted"},{"branch_refs":["root_000273/B001","root_000296/B003","root_000434/B011","root_000847/B001","root_001637/B005"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Cutting Rock Into a Valley Place","source_type":"channel","support_id":"sup_81901d9a83302d38f27b","text":"piercing or excavation `ج و ب:B001/m01`; hard stone `ح ج ر:B003/m01`; boulder `ص خ ر:B001/m01`; valley `و د ي:B005/m01`; water-holding rock hollow `خ ل ق:B011/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Cutting Rock Into a Valley Place","source_type":"channel","support_id":"sup_b941cb84e4c22613efb2","text":"Tool-like cutting acts on resistant material in a valley setting, producing a hollow that can become chamber or reservoir.","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْفَجْرِ","ayah_ref":"89:1"},{"arabic_uthmani":"وَلَيَالٍ عَشْرٍۢ","ayah_ref":"89:2"},{"arabic_uthmani":"وَٱلشَّفْعِ وَٱلْوَتْرِ","ayah_ref":"89:3"},{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَسْرِ","ayah_ref":"89:4"},{"arabic_uthmani":"هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ","ayah_ref":"89:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":5,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":5,"target_morphology_supplied":false},"branch_refs":["root_000296/B006","root_000702/B001","root_000802/B001","root_001016/B002","root_001132/B002","root_001226/B003","root_001392/B001","root_001621/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001226","role":"Apportionment supplies the focus mechanism by which one temporal whole becomes distinguishable shares.","root":"ق س م","source_ref":"89:5","source_word_indices":["4"]},{"branch_id":"B006","mapped_root_id":"root_000296","role":"A circling boundary supplies the perceptual frame that keeps each temporal share distinct.","root":"ح ج ر","source_ref":"89:5","source_word_indices":["6"]},{"branch_id":"B002","mapped_root_id":"root_001132","role":"Dawn emerging from night supplies the first temporal cut.","root":"ف ج ر","source_ref":"89:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001392","role":"Night as darkness supplies the bounded medium being counted and traversed.","root":"ل ي ل","source_ref":"89:2","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001016","role":"Completion of nine by a tenth supplies a closed counted span.","root":"ع ش ر","source_ref":"89:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000802","role":"Joining a thing to its like supplies the paired class within the partition.","root":"ش ف ع","source_ref":"89:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001621","role":"The singular without a pair supplies the complementary remainder.","root":"و ت ر","source_ref":"89:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000702","role":"Night travel supplies ordered passage across the boundaries just established.","root":"س ر ي","source_ref":"89:4","source_word_indices":["3"]}],"changed_reading":{"after":"The opening performs the very qasam it names by apportioning time, while the possessor of hijr is the reader who can perceive its limits and relations.","before":"The opening names several sacred times and then asks whether their oath is sufficient."},"confidence":"strong","mechanism":"The opening does not only provide objects to swear by. It repeatedly cuts, counts, pairs, leaves a remainder, and moves a bounded darkness onward. That sequence activates qasam as temporal apportionment and hijr as the boundary faculty that recognizes the architecture.","model_id":"delta_counted_temporal_partition","reader_inference":"The packet supplies dawn's emergence, a completed count, paired and unpaired units, and night passage; I infer that their ordered recurrence makes the oath a temporal partitioning apparatus. They may alternatively remain separate oath objects without one mathematical mechanism.","status":"strengthened","structural_cues":["89:1-4 form a coordinated chain of oath phrases gathered by the singular deictic 'that' in 89:5.","The sequence moves from a cut to a counted span, then paired and unpaired classes, then passage."],"trigger_roots":["ف ج ر","ل ي ل","ع ش ر","ش ف ع","و ت ر","س ر ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_counted_temporal_partition","source_type":"hft","support_id":"sup_b20e502901c704330196","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ","ayah_ref":"89:10"},{"arabic_uthmani":"ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ","ayah_ref":"89:11"},{"arabic_uthmani":"فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ","ayah_ref":"89:12"},{"arabic_uthmani":"إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ","ayah_ref":"89:14"},{"arabic_uthmani":"هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ","ayah_ref":"89:5"},{"arabic_uthmani":"إِرَمَ ذَاتِ ٱلْعِمَادِ","ayah_ref":"89:7"},{"arabic_uthmani":"ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ","ayah_ref":"89:8"},{"arabic_uthmani":"وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ","ayah_ref":"89:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":8,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":8,"target_morphology_supplied":false},"branch_refs":["root_000273/B001","root_000296/B002","root_000296/B003","root_000434/B001","root_000566/B001","root_000847/B001","root_000937/B001","root_001043/B003","root_001154/B001","root_001226/B004","root_001620/B001"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001226","role":"The oath supplies the evidentiary summons under which monumental achievement is tested.","root":"ق س م","source_ref":"89:5","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_000296","role":"Hard stone supplies the context-facing material sense of hijr.","root":"ح ج ر","source_ref":"89:5","source_word_indices":["6"]},{"branch_id":"B002","mapped_root_id":"root_000296","role":"Reason as restraint supplies the inward counterpart that monumental hardness cannot guarantee.","root":"ح ج ر","source_ref":"89:5","source_word_indices":["6"]},{"branch_id":"B003","mapped_root_id":"root_001043","role":"Columns and supports supply conspicuous external structure.","root":"ع م د","source_ref":"89:7","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000434","role":"Measuring and proportioning a thing supplies designed scale rather than accidental bulk.","root":"خ ل ق","source_ref":"89:8","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000273","role":"Penetrating cutting supplies the human ability to open and shape hard material.","root":"ج و ب","source_ref":"89:9","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000847","role":"Massive hard rock makes the material echo with the focus root explicit.","root":"ص خ ر","source_ref":"89:9","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001620","role":"Driven stakes supply fixation and imposed stability.","root":"و ت د","source_ref":"89:10","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000937","role":"Crossing the limit supplies the failure of inward boundary despite external mastery.","root":"ط غ ي","source_ref":"89:11","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001154","role":"Departure from soundness and equilibrium supplies the consequence of failed restraint.","root":"ف س د","source_ref":"89:12","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000566","role":"Watchful guarding supplies a final boundary that observes those who would not guard themselves.","root":"ر ص د","source_ref":"89:14","source_word_indices":["3"]}],"changed_reading":{"after":"Possessing hijr means having an inward limit: the context exposes the irony that people may command stone, columns, and stakes while lacking the restraint named by the same focus root.","before":"Possessing hijr means simply being intelligent enough to understand the oath."},"confidence":"strong","mechanism":"The context constructs an external architecture of columns, measured making, cut rock, and stakes, then shows its makers crossing the limit and leaving sound order. This splits hijr into hard material and inward restraint: those with monumental stone can still lack the inner barrier that makes one truly 'possessed of hijr.'","model_id":"delta_monumental_hardness_vs_inner_limit","reader_inference":"The packet supplies supports, measured formation, rock-cutting, stakes, limit-crossing, disorder, and watchfulness; I infer an antithesis between mastered matter and unmastered desire. Alternatively, the building vocabulary may identify powers and their punishment without deliberately redefining hijr.","status":"revised","structural_cues":["The branchless ك ي ف at 89:6 is used only as an interrogative cue: it echoes 89:5's question and opens the historical demonstration.","89:7-10 accumulate built fixtures before 89:11-12 reverse from external order to transgression and corruption."],"trigger_roots":["ع م د","خ ل ق","ج و ب","ص خ ر","و ت د","ط غ ي","ف س د","ر ص د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_monumental_hardness_vs_inner_limit","source_type":"hft","support_id":"sup_f4c672d2b411e02865d1","trust":"legacy_unbound"}]}
</lane_packet_json>
