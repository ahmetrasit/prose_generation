# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **31:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s031-regular-20260919/s031/31_2/macro.discovery.json` and modify nothing
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
  "ayah_ref": "31:2",
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
{"branch_registry":[{"boundary":"Bu dal hedefe yonelme, isaret adi veya soru edati degil; bekleme ve kalma alanidir.","branch_kind":"bare","branch_ref":"root_000074/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ءَايَة","morph_features":"STEM|POS:N|LEM:'aAyap|ROOT:Ayy|FP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:2:1","qac_word_ref":"31:2:2","surface_ar":"ءَايَٰتُ"}],"gloss":"bekleyerek oyalanma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kisi veya sey hareketi erteleyip durur, oyalanir ya da bekler."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir isin gerceklesme imkanini bekleme anlami da ayni durup bekleme cekirdegine baglidir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kalinan veya beklenilen yer icin konaklama ve tutulma yeri anlaminda adlasmis kullanim vardir."}}],"root_ar":"ء ي ي","root_id":"root_000074","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Durma, oyalanma, bekleme ve kalinan yer baglantisini en kisa bicimde tasir.","boundary_detail":"Bu dal hedefe yonelme, isaret adi veya soru edati degil; bekleme ve kalma alanidir.","branch_image_ar":"تمهل وانتظار","concept_gloss":"bekleyerek oyalanma","contextual_glosses":[{"applicability":"Fiil olarak kisinin hareket etmeyip bekledigi baglamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Durma ve bekleme eylemini korur."},"facet_ids":["F001"],"text":"durup bekledi","usage_role":"contextual"},{"applicability":"Bir isin olabilirligini bekleme baglaminda kullanilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Isin imkanini bekleme yonunu korur."},"facet_ids":["F002"],"text":"imkanini bekledi","usage_role":"contextual"},{"applicability":"Yer adi olarak konaklama veya tutulma yeri anlaminda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mekan ve kalma sonucunu korur."},"facet_ids":["F003"],"text":"kalinacak yer","usage_role":"contextual"}],"definition":"Bir yerde veya bir isin basinda oyalanarak durmak, beklemek ya da kalinacak yer olarak tutulmak.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kisi veya sey hareketi erteleyip durur, oyalanir ya da bekler."},{"facet_id":"F002","role":"extension","statement":"Bir isin gerceklesme imkanini bekleme anlami da ayni durup bekleme cekirdegine baglidir."},{"facet_id":"F003","role":"associated_use","statement":"Kalinan veya beklenilen yer icin konaklama ve tutulma yeri anlaminda adlasmis kullanim vardir."}],"identity_rationale":"Kaynak ifadesi oyalanma, durup bekleme, bir isin imkanini bekleme ve kalinan yer anlamlarini birlikte verir. Verilen dal cercevesi bu bekleme ve kalma cekirdegini sadik bicimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"durup oyalanmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"isin imkanini beklemek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kalinacak veya oyalanilacak yer"}],"lexicalization_note":"Bare kapsam, anlami kokten gelen bekleme ve kalma cekirdegiyle sinirlar; baska edat veya ad kullanimlari buraya alinmaz.","neighbor_coverage_note":"Adaylar icinden bekleme ve kalma sinirini aciklastiranlar secildi; diger ic dallar ve uzak adaylar daha cok ses, edat veya genel alan benzerligi tasir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bekleyerek oyalanmayi ve imkan kollamayi kapsar; komsu dal beklemeyle birlikte sabit durus ve yerlesme tarafini daha guclu kurar.","focus_only":"Bu dalda oyalanma ve isin imkanini bekleme de vardir.","gloss":"bekleme ve durma","neighbor_only":"Komsu dalda bekleyisle birlikte daha belirgin sabitlik ve yerlesme vurgusu vardir.","neighbor_ref":"root_001437/B001","relation_type":"near_synonym","shared_zone":"Ikisi de hareketin ertelenmesi ve bir yerde kalma alanina girer."},{"boundary_match":"partial","distinction":"Bu dalin cekirdegi bekleyerek durma iken komsu dalin cekirdegi bir yerde ikamet veya uzun sureli yerlesik kalmadir.","focus_only":"Bu dal bekleme, oyalanma ve kisa sureli kalma durumuna aciktir.","gloss":"kalma ve ikamet","neighbor_only":"Komsu dalda bir yerde yerlesme, uzun kalma veya ikamet etme cekirdegi vardir.","neighbor_ref":"root_000211/B001","relation_type":"near_neighbor","shared_zone":"Ikisi de bir yerde bulunma ve kalma durumunu anlatabilir."},{"boundary_match":"field_only","distinction":"Anlam cekirdekleri ayridir: burada eylem durup beklemek, komsuda ise bir kisiyi hedef alarak kastetmektir.","focus_only":"Bu dal bekleme ve oyalanmadir.","gloss":"bekleme ile kastetme","neighbor_only":"Komsu dal bir kisinin belirtisine veya kendisine yonelerek onu kastetmedir.","neighbor_ref":"root_000074/B002","relation_type":"same_field","shared_zone":"Ikisi ayni kok ailesindeki sesce yakin formlardir."}],"source_phrase_ar":"تأيا يتأيا تأييا أي تمكث؛ تأييت الأمر انتظرت إمكانه؛ ليست هذه بدار تئية أي مقام (maqayis)؛ تأيا أي توقف وتمكث؛ منزل تئية أي منزل تلبث وتحبس (sihah)","source_summary":"Kaynaklar dalin temelini durma, oyalanma ve bekleme olarak verir; ayrica bir isin imkanini bekleme ve kalinacak yer kullanimi ayni anlam alaninda yer alir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه تأيا بمعنى تمكث وتوقف، وتأيي الأمر بمعنى انتظار إمكانه، والتئية بمعنى مقام أو منزل تلبث.","what_is_not_ar":"ليس هو التعمد إلى الشخص أو العلامة، ولا اسم أي في الاستفهام."},"support_links":[]},{"boundary":"Bu dal beklemek veya yalniz bir isaret bildirmek degil, kisiyi belirtisiyle hedef almaktir.","branch_kind":"bare","branch_ref":"root_000074/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ءَايَة","morph_features":"STEM|POS:N|LEM:'aAyap|ROOT:Ayy|FP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:2:1","qac_word_ref":"31:2:2","surface_ar":"ءَايَٰتُ"}],"gloss":"kisiyi bilerek hedefleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eylemde belirli bir kisi secilir ve ona kasitli olarak yonelinir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kisiyi hedefleme, onun gorunen belirtisi veya sahsi uzerinden kurulur."}}],"root_ar":"ء ي ي","root_id":"root_000074","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kisinin kendisini veya ayirt edici belirtisini esas alan kastetme eylemini karsilar.","boundary_detail":"Bu dal beklemek veya yalniz bir isaret bildirmek degil, kisiyi belirtisiyle hedef almaktir.","branch_image_ar":"تعمد آية الشخص","concept_gloss":"kisiyi bilerek hedefleme","contextual_glosses":[{"applicability":"Belirli kisinin hedef alindigi fiil baglaminda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli kisiyi kasitli hedefleme anlamini korur."},"facet_ids":["F001","F002"],"text":"onu bilerek kastetti","usage_role":"contextual"}],"definition":"Bir kisinin belirtisini ve sahsini esas alarak onu bilerek hedeflemek ve kastetmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eylemde belirli bir kisi secilir ve ona kasitli olarak yonelinir."},{"facet_id":"F002","role":"specialization","statement":"Kisiyi hedefleme, onun gorunen belirtisi veya sahsi uzerinden kurulur."}],"identity_rationale":"Kaynak ifadesi bir kisinin belirtisini ve sahsini amaclayarak ona yonelmeyi ve onu bilerek kastetmeyi bildirir. Dal cercevesi bu hedeflenmis kisiyi kastetme anlamini dogru ayirir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"onu belirtisiyle bilerek kastetmek"}],"lexicalization_note":"Bare kapsam, anlamin edat veya sabit kalipla degil fiilsel kastetme cekirdegiyle verilmesini gerektirir.","neighbor_coverage_note":"Kastetme alanini ayiran en yakin genel yonelme adaylari ve ic isaret dali secildi; diger adaylar uzak veya yalniz bicimsel benzerliklidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kisiye ve onun belirtisine bagli ozel bir kastetmedir; komsu dal hedef nesnesi bakimindan daha genis bir yonelme anlamidir.","focus_only":"Bu dal kisinin belirtisi ve sahsi uzerinden hedeflemeyi belirtir.","gloss":"kastetme","neighbor_only":"Komsu dal daha genel olarak herhangi bir seye yonelme ve onda ciddi olma anlamina aciktir.","neighbor_ref":"root_000305/B001","relation_type":"near_synonym","shared_zone":"Ikisi de bilerek yonelme ve hedef edinme alanini paylasir."},{"boundary_match":"partial","distinction":"Bu dalin siniri belirli kisiyi kastetmeye dardir; komsu dal genel hedefe gitme veya arama niyetini de tasir.","focus_only":"Bu dal kisi sahsini ve belirtisini hedef alir.","gloss":"yonelerek kastetme","neighbor_only":"Komsu dal yonelme, arama ve niyet etme gibi daha genis alanlari kapsar.","neighbor_ref":"root_000053/B012","relation_type":"near_synonym","shared_zone":"Ikisi de amacli yonelme anlaminda kesisir."},{"boundary_match":"field_only","distinction":"Bu dalda belirti hedefleme araci olur; komsu dalda belirti veya isaret bizzat adlasmis anlamdir.","focus_only":"Bu dal bir kisiyi hedeflemeyi anlatir.","gloss":"kastetme ile belirti","neighbor_only":"Komsu dal isaret, belirti, topluluk veya metin birimi gibi adlasmis anlamlari anlatir.","neighbor_ref":"root_000074/B003","relation_type":"same_field","shared_zone":"Kisinin belirtisi fikri iki dal arasinda bag kurar."}],"source_phrase_ar":"تآييت وأصله تعمدت آيته وشخصه (maqayis)؛ تآييته وتأييته إذا قصدت آيته وتعمدته (sihah)","source_summary":"Kaynaklar bu dali bir kisinin belirtisini ve sahsini hedefleyerek onu kastetme seklinde toplar; anlamda bilincli yonelme esastir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه تآييت أو تأييت الشخص إذا قصدت آيته وشخصه وتعمدته.","what_is_not_ar":"ليس هو التمكث والانتظار، ولا الآية بمعنى العلامة المجردة إلا من جهة كونها مقصودة."},"support_links":[]},{"boundary":"Isaret cekirdegi korunur; kisi, topluluk, metin parcasi ve gunes isigi kullanimlari buna bagli uzantilardir.","branch_kind":"mixed_non_bare","branch_ref":"root_000074/B003","candidate_links":[{"candidate_id":"cand_578b04313f4833efdfe8","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ءَايَة","morph_features":"STEM|POS:N|LEM:'aAyap|ROOT:Ayy|FP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:2:1","qac_word_ref":"31:2:2","surface_ar":"ءَايَٰتُ"}],"gloss":"gorunen belirti","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, bir seyi tanitan veya ona delalet eden gorunen belirtidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kisinin sahsi, onun taninmasini saglayan belirti gibi dusunulerek ifade edilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir toplulugun eksiksiz butunu icin de kullanilir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kitapta harf toplulugundan olusan belirli parca anlamina gelir."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Gunes isigi, gunesin ayirt ettirici belirtisi gibi goruldugu icin bu alana baglanir."}}],"root_ar":"ء ي ي","root_id":"root_000074","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ciplak isaret anlamini iyi karsilar, fakat kalipli uzantilari tek basina tam tasimaz.","boundary_detail":"Isaret cekirdegi korunur; kisi, topluluk, metin parcasi ve gunes isigi kullanimlari buna bagli uzantilardir.","branch_image_ar":"علامة ظاهرة","concept_gloss":"gorunen belirti","contextual_glosses":[{"applicability":"Belirti veya delalet eden alamet anlaminda kullanilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Cekirdek belirti anlamini korur."},"facet_ids":["F001"],"text":"isaret","usage_role":"general"},{"applicability":"Bir kisinin kendisi anlamindaki kalipli kullanim icindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kisiye bagli ozel uzantiyi korur."},"facet_ids":["F002"],"text":"sahsi","usage_role":"contextual"},{"applicability":"Toplulugun geride kimse birakmadan butun olarak cikmasi baglaminda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Butun topluluk anlamini korur."},"facet_ids":["F003"],"text":"topluca","usage_role":"contextual"},{"applicability":"Harflerden olusan belirli metin bolumu icin aciklayici karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Metin parcasi ve harf toplulugu anlamini korur."},"facet_ids":["F004"],"text":"kitap parcasi","usage_role":"contextual"}],"definition":"Gorunen bir belirti veya isaret; bazi kalipli kullanimlarda kisinin sahsi, toplulugun butunu, kitapta harflerden olusan parca ya da gunesin isigi icin de kullanilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, bir seyi tanitan veya ona delalet eden gorunen belirtidir."},{"facet_id":"F002","role":"extension","statement":"Kisinin sahsi, onun taninmasini saglayan belirti gibi dusunulerek ifade edilir."},{"facet_id":"F003","role":"extension","statement":"Bir toplulugun eksiksiz butunu icin de kullanilir."},{"facet_id":"F004","role":"specialization","statement":"Kitapta harf toplulugundan olusan belirli parca anlamina gelir."},{"facet_id":"F005","role":"associated_use","statement":"Gunes isigi, gunesin ayirt ettirici belirtisi gibi goruldugu icin bu alana baglanir."}],"identity_rationale":"Kaynak ifadesi yalniz soyut isaret degil, kisinin sahsi, topluca cikma, kitap parcasini olusturan harf toplulugu ve gunes isigini de ayni ailede verir. Dal adi kullanilabilir, fakat tanim isaret cekirdegini bu adlasmis ve kalipli uzantilardan ayirmalidir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"gorunen isaret"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"belirlenmis isaret"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kisinin sahsi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"topluca cikmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kitaptaki harf toplulugu parcasi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"gunesin isigi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"gunesin isigi"}],"lexicalization_note":"Mixed non-bare kapsam, yalniz ciplak isaret anlamini degil, kalipli kisi, topluluk, metin parcasi ve gunes isigi kullanimlarini ayri facetlerde tutar.","neighbor_coverage_note":"Isaret cekirdegini aciklastiran alamet ve delil adaylari secildi; ayni kokteki diger dallar ise edat, bekleme veya yemin alanlarina ayrilir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal gorunen belirtiyi cesitli adlasmis kaliplarla genisletir; komsu dal isaret anlamini yol ve randevu gibi baska alanlara baglar.","focus_only":"Bu dal kitap parcasi, kisi sahsi, topluluk ve gunes isigi uzantilarini da tasir.","gloss":"belirti","neighbor_only":"Komsu dalda belirtiyle birlikte yol isareti ve belirlenmis zaman anlamlari vardir.","neighbor_ref":"root_000051/B005","relation_type":"near_synonym","shared_zone":"Ikisi de bir seyi tanitan isaret veya belirti anlaminda kesisir."},{"boundary_match":"partial","distinction":"Bu dal isaret cekirdeginden metin ve topluluk anlamlarina acilir; komsu dal ise bir seyi tanittiran alamet olma sinirinda kalir.","focus_only":"Bu dalda metin parcasi ve topluluk butunu gibi kalipli uzantilar vardir.","gloss":"tanitici isaret","neighbor_only":"Komsu dal taninma icin konan veya gorulen alametler alaninda yogunlasir.","neighbor_ref":"root_000764/B004","relation_type":"near_synonym","shared_zone":"Ikisi de tanimaya yarayan belirti anlamini paylasir."},{"boundary_match":"partial","distinction":"Bu dal isaretin varligini adlandirir; komsu dal isaretin anlam gosteren delil olma islevini daha guclu tasir.","focus_only":"Bu dalda gorunen belirti veya isaretin kendisi one cikar.","gloss":"belirti ve delil","neighbor_only":"Komsu dalda belirti konusan delil gibi anlam aciga cikaran kanit niteligindedir.","neighbor_ref":"root_001519/B002","relation_type":"near_neighbor","shared_zone":"Ikisi de gorulenden anlam cikarma alanina yakindir."},{"boundary_match":"field_only","distinction":"Burada belirti adlasmis cekirdektir; komsuda belirti, kisiyi kastetmenin aracidir.","focus_only":"Bu dal isaret veya belirtinin kendisini anlatir.","gloss":"belirti ile hedefleme","neighbor_only":"Komsu dal belirti uzerinden bir kisiyi hedeflemeyi anlatir.","neighbor_ref":"root_000074/B002","relation_type":"same_field","shared_zone":"Belirti fikri iki dal arasinda ortak temas noktasi olusturur."}],"source_phrase_ar":"الآية العلامة؛ آية الرجل شخصه؛ خرج القوم بآيتهم أي بجماعتهم؛ آية القرآن لأنها جماعة حروف؛ إياة الشمس ضوءها لأنه كالعلامة لها (maqayis)؛ الآية العلامة والآية من آيات الله والجميع الآي (ayn)؛ الآية العلامة؛ آية الرجل شخصه؛ خرج القوم بآيتهم أي بجماعتهم؛ الآية من كتاب الله جماعة حروف؛ أياة الشمس ضوؤها (sihah)","source_summary":"Kaynaklar isaret ve belirti cekirdeginde bulusur; ayni iddia kisinin sahsi, toplulugun butunu, kitap parcasi ve gunes isigi gibi uzantilari da birlikte aktarir.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه الآية بمعنى العلامة، وآية الرجل بمعنى شخصه، وخروج القوم بآيتهم أي بجماعتهم، وآية القرآن لأنها جماعة حروف، وإياة الشمس بمعنى ضوئها كالعلامة لها.","what_is_not_ar":"ليس هو أي الاستفهامية ولا إي في اليمين ولا التمكث والتأني."},"support_links":["sup_71229f315fee594210df"]},{"boundary":"Bu dal isaret veya yemin degil; belirleme, sorma, sart ve ilgi islevli gramer birimidir.","branch_kind":"non_bare","branch_ref":"root_000074/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ءَايَة","morph_features":"STEM|POS:N|LEM:'aAyap|ROOT:Ayy|FP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:2:1","qac_word_ref":"31:2:2","surface_ar":"ءَايَٰتُ"}],"gloss":"hangi belirleyicisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel islev, soru veya belirleme yoluyla hangi kisi ya da seyin kastedildigini ayirt etmektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sart-cevap ve ilgi yapilarinda da benzer belirleme isleviyle kullanilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Niteleme, belirsiz ad anlatimi ve hayret bildirme kullanislari bu gramer islevine baglidir."}}],"root_ar":"ء ي ي","root_id":"root_000074","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Soru ve secme cekirdegini dogal Turkceyle verir; ilgi ve sart islevleri aciklama ister.","boundary_detail":"Bu dal isaret veya yemin degil; belirleme, sorma, sart ve ilgi islevli gramer birimidir.","branch_image_ar":"أي للسؤال والتعيين","concept_gloss":"hangi belirleyicisi","contextual_glosses":[{"applicability":"Soru ve secme baglamlarinda en dogal karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soru ve belirleme islevini korur."},"facet_ids":["F001"],"text":"hangi","usage_role":"general"},{"applicability":"Sart-cevap veya bagimli belirleme kullanimlarinda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirlenen unsura bagli sart veya ilgi islevini korur."},"facet_ids":["F002"],"text":"hangisi ise","usage_role":"contextual"},{"applicability":"Hayret veya niteleme etkisi olan baglamlarda aciklayici karsiliktir.","error_profile":{"adds":"Miktar veya derece yorumu ekleyebilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Hayret ve derece etkisini Turkce anlatir."},"facet_ids":["F003"],"text":"ne kadar","usage_role":"contextual"}],"definition":"Soru, sart-cevap, ilgi, niteleme, secme veya hayret isleviyle istenen kisiyi ya da seyi belirleyen gramer birimi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel islev, soru veya belirleme yoluyla hangi kisi ya da seyin kastedildigini ayirt etmektir."},{"facet_id":"F002","role":"extension","statement":"Sart-cevap ve ilgi yapilarinda da benzer belirleme isleviyle kullanilir."},{"facet_id":"F003","role":"associated_use","statement":"Niteleme, belirsiz ad anlatimi ve hayret bildirme kullanislari bu gramer islevine baglidir."}],"identity_rationale":"Kaynak ifadesi soru, sart-cevap, ilgi, niteleme, secme ve hayret islevlerini ayni ad-edat ailesinde toplar. Dal cercevesi bu non-bare gramer birimini genel kok anlamina cevirmeden dogru sinirlar.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"soru, sart veya ilgiyle belirleyen ad"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"hangi olursa veya herhangi bir"}],"lexicalization_note":"Non-bare kapsam, tanimi yalniz bu gramer biriminin kullanimlariyla sinirlar ve kokten genel bir anlam uretmez.","neighbor_coverage_note":"Soru ve belirleme sinirini gosteren gramer komsulari secildi; isaret, nidalik ve yemin dallari yalniz bicimsel yakinlik tasir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal hangi unsurun kastedildigini gramer yoluyla belirler; komsu dal bir kisiyi veya seyi secip tercih etme eylemidir.","focus_only":"Bu dal soru ve secme islevli gramer belirleyicisidir.","gloss":"secme ile secilme","neighbor_only":"Komsu dal secip yakina alma veya ustun tutma eylemini anlatir.","neighbor_ref":"root_000220/B004","relation_type":"near_neighbor","shared_zone":"Ikisi de birden fazla ihtimal arasindan ayirma fikrine yakindir."},{"boundary_match":"field_only","distinction":"Bu dal secim veya soru sorar; komsu dal belirli cogul kisileri baglayan ilgi zamiridir.","focus_only":"Bu dal tekil veya genel belirleme, soru ve sart islevleri tasir.","gloss":"belirleyici ile ilgi zamiri","neighbor_only":"Komsu dal cogul ilgi zamiri olarak kimler anlamindadir.","neighbor_ref":"root_000076/B004","relation_type":"same_field","shared_zone":"Ikisi de gramerde ilgi ve belirleme alanina girer."},{"boundary_match":"field_only","distinction":"Bu dal kastedileni secer veya sorar; komsu dal ogeleri ayirip belirginlestiren yapisal bir unsurdur.","focus_only":"Bu dal soru, secme ve sart gibi anlam islevleri tasir.","gloss":"gramer belirleyicisi","neighbor_only":"Komsu dal cumlede ayirma veya vurgu yapan gramer ogesi niteligindedir.","neighbor_ref":"root_001159/B015","relation_type":"same_field","shared_zone":"Ikisi de cumle yapisinda islevsel gramer birimleri olarak kullanilir."},{"boundary_match":"field_only","distinction":"Bu dal kastedileni belirler veya sorar; komsu dal sorumaz, ardindan gelen aciklamayi baslatir.","focus_only":"Bu dal soru, secme, sart ve ilgi islevlerini tasir.","gloss":"soru ile aciklama","neighbor_only":"Komsu dal onceki ifadeyi aciklayan yorumlayici birimdir.","neighbor_ref":"root_000074/B009","relation_type":"same_field","shared_zone":"Ikisi de ayni bicim ailesinde gramer islevi tasir."}],"source_phrase_ar":"لم يجىء إلا في قولهم أي في الاستفهام (jamhara)؛ أي مثقلة بمنزلة من وما؛ أيهم أخوك؛ أيما الأخوين؛ أيا ما تحب؛ أي لا تنون لأن أي مضاف (ayn)؛ أي اسم معرب يستفهم به ويجازى؛ وقد يكون بمنزلة الذي؛ وقد يكون نعتا للنكرة؛ وأي قد يتعجب بها (sihah)","source_summary":"Kaynaklar bu birimi soru ve belirleme temelinde verir; sart-cevap, ilgi, niteleme ve hayret islevleri ayni gramer alani icinde aktarilir.","sources":["JA","AY","SI"],"what_is_ar":"يدخل فيه أي في الاستفهام والجزاء والصلة والنعت والتعجب وحكاية النكرات، وما يتصل بها من أيهم وأيما وأية.","what_is_not_ar":"ليس هو أي المفسرة، ولا إي في القسم، ولا الآية بمعنى العلامة."},"support_links":[]},{"boundary":"Bu dal soru, nida veya isaret degil; nesne konumundaki zamir yapisina destek olan gramer unsurudur.","branch_kind":"non_bare","branch_ref":"root_000074/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ءَايَة","morph_features":"STEM|POS:N|LEM:'aAyap|ROOT:Ayy|FP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:2:1","qac_word_ref":"31:2:2","surface_ar":"ءَايَٰتُ"}],"gloss":"nesne zamiri dayanagi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birime baglanan zamir eki nesne konumunu belirtir ve birim bu eki tasiyan dayanak olur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak siniri, bu kullanimin yukleme konumunda oldugunu ve baska durum konumlarina tasinmadigini belirtir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Uyarma veya sakindirma yapisi bu dayanak islevinin tipik kullanimidir."}}],"root_ar":"ء ي ي","root_id":"root_000074","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zamir ekini tasiyan gramer unsurunu aciklayici bicimde karsilar.","boundary_detail":"Bu dal soru, nida veya isaret degil; nesne konumundaki zamir yapisina destek olan gramer unsurudur.","branch_image_ar":"إيا عماد للضمير","concept_gloss":"nesne zamiri dayanagi","contextual_glosses":[{"applicability":"Ikinci tekil kisi nesne zamiri olarak ceviri baglaminda uygundur.","error_profile":{"adds":"Belirli kisi ve sayi ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Nesne zamiri etkisini Turkceye tasir."},"facet_ids":["F001"],"text":"seni","usage_role":"contextual"},{"applicability":"Uyarma ve sakindirma kalibinda dogal Turkce karsilik olarak kullanilir.","error_profile":{"adds":"Uyari edasi degeri ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Uyarma kullanimini korur."},"facet_ids":["F003"],"text":"sakin ha","usage_role":"contextual"}],"definition":"Nesne konumundaki zamir ekleriyle birlikte kullanilip zamiri tasiyan ve ozellikle uyarma yapilarinda gorulen gramer dayanak birimi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birime baglanan zamir eki nesne konumunu belirtir ve birim bu eki tasiyan dayanak olur."},{"facet_id":"F002","role":"specialization","statement":"Kaynak siniri, bu kullanimin yukleme konumunda oldugunu ve baska durum konumlarina tasinmadigini belirtir."},{"facet_id":"F003","role":"example","statement":"Uyarma veya sakindirma yapisi bu dayanak islevinin tipik kullanimidir."}],"identity_rationale":"Kaynak ifadesi bu birimi yalniz belirli eklerle birlikte nesne konumunda zamir destegi olarak verir ve ozellikle uyari yapisinda ornekler. Dal cercevesi yalin kok anlami degil, bu sinirli gramer islevini anlatir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"nesne zamiri icin dayanak unsur"}],"lexicalization_note":"Non-bare kapsam, tanimi belirli zamir ekleriyle kurulan nesne konumlu gramer isleviyle sinirlar.","neighbor_coverage_note":"Yapisal gramer islevini aciklastiran zamir ve ayirma adaylari secildi; nida, yemin ve isaret dallari anlamca ayri kalir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal zamir ekinin nesne konumunu tasir; komsu dal ogeleri ayirip belirginlestiren farkli bir yapisal islevdir.","focus_only":"Bu dal nesne zamiri ekini tasiyan dayanak birimidir.","gloss":"gramer dayanagi","neighbor_only":"Komsu dal cumlede ayrim ve vurgu saglayan gramer ogesidir.","neighbor_ref":"root_001159/B015","relation_type":"same_field","shared_zone":"Ikisi de cumlede anlamdan cok yapisal islev tasiyan unsurlardir."},{"boundary_match":"field_only","distinction":"Bu dal kendi basina ilgi zamiri degil, zamir ekini tasiyan destektir; komsu dal bir ismi niteleyen ilgi zamiri gibi calisir.","focus_only":"Bu dal nesne zamiriyle sinirli bir dayanak unsurudur.","gloss":"zamir islevi","neighbor_only":"Komsu dal ilgi zamiri gibi kullanilan ayri bir gramer kelimesidir.","neighbor_ref":"root_000527/B002","relation_type":"same_field","shared_zone":"Ikisi de zamir ve ilgi alaninda gramer islevi gorur."},{"boundary_match":"field_only","distinction":"Bu dal nesne zamiri yapisini kurar; komsu dal hangi unsurun kastedildigini sorar veya belirler.","focus_only":"Bu dal nesne zamirini tasima islevindedir.","gloss":"zamir dayanagi ile belirleyici","neighbor_only":"Komsu dal soru, secme ve sart belirleyicisidir.","neighbor_ref":"root_000074/B004","relation_type":"same_field","shared_zone":"Ikisi de islevsel gramer birimleri olarak ayni kok ailesinde yer alir."}],"source_phrase_ar":"إياك ضربت فتكون إيا عمادا للكاف؛ ولا تكون إيا مع كاف ولا هاء ولا ياء في موضع الرفع والجر؛ إياك وزيدا (ayn)","source_summary":"Tek kaynakli iddia, bu gramer unsurunu nesne konumundaki zamir ekleri icin dayanak olarak sinirlar ve uyarma yapisini ornekler.","sources":["AY"],"what_is_ar":"يدخل فيه إيا مع الكاف والهاء والياء في موضع الاسم المنصوب، كإياك، وذكرها عمادا للضمير في التحذير وغيره.","what_is_not_ar":"ليس هو أي الاستفهامية ولا أيا حرف النداء ولا الآية العلامة."},"support_links":[]},{"boundary":"Bu dal sayi sorusu veya genel hangi belirleyicisi degil; zaman sorusuna ozgu gramer birimidir.","branch_kind":"non_bare","branch_ref":"root_000074/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ءَايَة","morph_features":"STEM|POS:N|LEM:'aAyap|ROOT:Ayy|FP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:2:1","qac_word_ref":"31:2:2","surface_ar":"ءَايَٰتُ"}],"gloss":"zaman sorusu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir olayin veya durumun zamanini sorma islevi tasir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Son sesinin asil mi ek mi oldugu hakkinda kaynakta bicimsel tartisma aktarilir."}}],"root_ar":"ء ي ي","root_id":"root_000074","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zaman sorusu islevini dogrudan karsilar.","boundary_detail":"Bu dal sayi sorusu veya genel hangi belirleyicisi degil; zaman sorusuna ozgu gramer birimidir.","branch_image_ar":"أيان للزمان","concept_gloss":"zaman sorusu","contextual_glosses":[{"applicability":"Zaman sorusu sorulan butun baglamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Zaman sorma islevini korur."},"facet_ids":["F001"],"text":"ne zaman","usage_role":"general"}],"definition":"Zaman hakkinda soru sormak icin kullanilan, ne zaman islevindeki gramer birimi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir olayin veya durumun zamanini sorma islevi tasir."},{"facet_id":"F002","role":"source_variant","statement":"Son sesinin asil mi ek mi oldugu hakkinda kaynakta bicimsel tartisma aktarilir."}],"identity_rationale":"Kaynak ifadesi bu birimi zaman sorusu icin ne zaman anlaminda verir ve son sesinin kokeni hakkindaki tartismayi ekler. Dal cercevesi bu sinirli zaman-soru islevini dogru aktarir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ne zaman anlaminda zaman sorusu"}],"lexicalization_note":"Non-bare kapsam, tanimi yalniz zaman soran gramer birimiyle sinirlar; sayi ve genel soru anlamlari alinmaz.","neighbor_coverage_note":"Zaman alanini ve soru islevini ayiran adaylar secildi; gun adlari ve genel zaman adlari daha uzak alan komsularidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal soru islevi tasir; komsu dal zamanin kendisini veya uygun vaktini adlandirir.","focus_only":"Bu dal zaman hakkinda soru soran gramer birimidir.","gloss":"zaman sorusu","neighbor_only":"Komsu dal bir seyin vakti veya zamani anlaminda isimsel zaman degeridir.","neighbor_ref":"root_000039/B003","relation_type":"near_neighbor","shared_zone":"Ikisi de zaman ve vakit alanina girer."},{"boundary_match":"field_only","distinction":"Bu dal zaman sorusu edatidir; komsu dal ise zaman olcusunun veya belirli vaktin adidir.","focus_only":"Bu dal zamanin sorulmasini saglar.","gloss":"sorulan zaman","neighbor_only":"Komsu dal belirli zaman, saat veya sure sonu anlamindadir.","neighbor_ref":"root_001671/B001","relation_type":"same_field","shared_zone":"Ikisi de zaman kavramina baglidir."},{"boundary_match":"partial","distinction":"Bu dal ne zaman sorusuna ozgudur; komsu dal daha genis bicimde nereden, nasil veya hangi yonden gibi alanlara yayilir.","focus_only":"Bu dal yalniz zaman sorusuyla sinirlidir.","gloss":"soru edati","neighbor_only":"Komsu dal yer, yon, durum ve kimi aktarmalarda zaman sorusuna aciktir.","neighbor_ref":"root_000063/B005","relation_type":"near_neighbor","shared_zone":"Ikisi de soru yoluyla bilinmeyeni ister."},{"boundary_match":"field_only","distinction":"Bu dal zaman eksenini ister; komsu dal nicelik ve cokluk eksenindedir.","focus_only":"Bu dal zamani sorar.","gloss":"zaman ile sayi sorusu","neighbor_only":"Komsu dal sayi veya cokluk anlamini sorar ya da bildirir.","neighbor_ref":"root_000074/B007","relation_type":"same_field","shared_zone":"Ikisi de soru veya belirsiz miktar alaninda gramer birimleridir."}],"source_phrase_ar":"أيان بمنزلة متى؛ يختلف في نونها فيقال هي أصلية ويقال هي زائدة (ayn)","source_summary":"Kaynak bu birimi ne zaman islevinde zaman sorusu olarak verir; bicimsel olarak son sesin kokeni konusunda iki ihtimal aktarir.","sources":["AY"],"what_is_ar":"يدخل فيه أيان إذا جعلت بمنزلة متى للسؤال عن الزمان، مع الخلاف في نونها أهي أصلية أم زائدة.","what_is_not_ar":"ليس هو كأين بمعنى كم، ولا أي في الاستفهام العام."},"support_links":[]},{"boundary":"Bu dal zaman sormaz; sayi, miktar ve cokluk alaninda non-bare gramer birimidir.","branch_kind":"non_bare","branch_ref":"root_000074/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ءَايَة","morph_features":"STEM|POS:N|LEM:'aAyap|ROOT:Ayy|FP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:2:1","qac_word_ref":"31:2:2","surface_ar":"ءَايَٰتُ"}],"gloss":"nice cok","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir sayi veya miktarin coklugunu bildirir ya da o niceligi sorar."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bicimsel aciklama, eklenen unsur ve son sesin yapisi hakkinda aktarilir."}}],"root_ar":"ء ي ي","root_id":"root_000074","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Cokluk ve miktar sorusu alanini kisa bicimde verir.","boundary_detail":"Bu dal zaman sormaz; sayi, miktar ve cokluk alaninda non-bare gramer birimidir.","branch_image_ar":"كأين لعدد كثير","concept_gloss":"nice cok","contextual_glosses":[{"applicability":"Sayi veya miktar hakkinda cokluk sorusu ya da bildirimi icin uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Cokluk ve nicelik islevini korur."},"facet_ids":["F001"],"text":"ne kadar cok","usage_role":"general"},{"applicability":"Edebi veya sayisal cokluk bildirimi icin kisa karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirsiz cokluk anlamini korur."},"facet_ids":["F001"],"text":"nice","usage_role":"contextual"}],"definition":"Sayi veya miktar hakkinda cokluk bildiren ya da soru soran, ne kadar veya nice islevindeki gramer birimi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir sayi veya miktarin coklugunu bildirir ya da o niceligi sorar."},{"facet_id":"F002","role":"source_variant","statement":"Bicimsel aciklama, eklenen unsur ve son sesin yapisi hakkinda aktarilir."}],"identity_rationale":"Kaynak ifadesi bu birimi sayi ve cokluk anlaminda ne kadar veya nice islevine baglar, ayrica bicimsel olusumunu aktarir. Dal cercevesi zaman sorusundan ve genel belirleyiciden ayri olarak nicelik islevini dogru verir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ne kadar cok anlaminda nicelik birimi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ne kadar cok anlaminda varyant"}],"lexicalization_note":"Non-bare kapsam, tanimi yalniz bu nicelik bildiren gramer birimiyle sinirlar ve genel kok anlami olarak genisletmez.","neighbor_coverage_note":"Ayni bicim ve nicelik cekirdegi tasiyan komsu ile cokluk alanindaki adaylar secildi; salt sayi adlari daha uzak sinir bilgisi verir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Aday komsu ayni bicim ailesini ve ayni sayi-cokluk islevini verir; kullanimsal sinir aynidir.","focus_only":null,"gloss":"ne kadar cok","neighbor_only":null,"neighbor_ref":"root_001336/B002","relation_type":"synonym","shared_zone":"Ikisi de ayni nicelik ve cokluk bildiren gramer birimini anlatir."},{"boundary_match":"partial","distinction":"Bu dal gramer birimiyle miktari sorar veya vurgular; komsu dal coklugun kendisini sozluksel anlam olarak anlatir.","focus_only":"Bu dal niceligi soran veya bildiren gramer birimidir.","gloss":"cokluk","neighbor_only":"Komsu dal cokluk ve artma anlamini sozluksel sifat veya fiil alaninda verir.","neighbor_ref":"root_001286/B001","relation_type":"near_neighbor","shared_zone":"Ikisi de cok olma ve sayica fazlalik alanina girer."},{"boundary_match":"field_only","distinction":"Bu dal nicelik eksenindedir; komsu dal zaman eksenindedir.","focus_only":"Bu dal sayi veya miktar coklugunu bildirir.","gloss":"nicelik ile zaman","neighbor_only":"Komsu dal olay zamanini sorar.","neighbor_ref":"root_000074/B006","relation_type":"same_field","shared_zone":"Ikisi de soru ve belirsiz bilgi isteyen gramer birimleridir."}],"source_phrase_ar":"كأين في معنى كم؛ أصل بنائها أي (ayn)؛ تدخل على أي الكاف فينقل إلى تكثير العدد بمعنى كم؛ كائن وكأين (sihah)","source_summary":"Kaynaklar bu birimi ne kadar veya nice anlaminda sayi ve cokluk islevine baglar; bicimsel koken ve varyantlar ayni iddia icinde verilir.","sources":["AY","SI"],"what_is_ar":"يدخل فيه كأين أو كائن في معنى كم، مع الكاف الزائدة والنون التي تشبه التنوين أو تكون مع أي أصلا.","what_is_not_ar":"ليس هو أيان للزمان، ولا أي وحدها للاستفهام والتعيين."},"support_links":[]},{"boundary":"Bu dal soru, aciklama veya yemin degil; muhataba seslenme islevindeki nida birimleridir.","branch_kind":"non_bare","branch_ref":"root_000074/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ءَايَة","morph_features":"STEM|POS:N|LEM:'aAyap|ROOT:Ayy|FP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:2:1","qac_word_ref":"31:2:2","surface_ar":"ءَايَٰتُ"}],"gloss":"ey seslenmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel islev, bir muhatabi seslenme yoluyla cagirmaktir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir bicim yakin muhataba, digeri hem yakin hem uzak muhataba seslenebilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Uzatilmis seslenme bicimi de ayni nida alaninda aktarilir."}}],"root_ar":"ء ي ي","root_id":"root_000074","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nida ve muhataba cagri islevini dogal Turkceyle karsilar.","boundary_detail":"Bu dal soru, aciklama veya yemin degil; muhataba seslenme islevindeki nida birimleridir.","branch_image_ar":"أي وأيا للنداء","concept_gloss":"ey seslenmesi","contextual_glosses":[{"applicability":"Seslenme basinda dogal ve kisa Turkce karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nida islevini korur."},"facet_ids":["F001"],"text":"ey","usage_role":"general"},{"applicability":"Seslenmenin daha konusma dili veya uzaktan cagri etkisi tasidigi baglamlarda uygundur.","error_profile":{"adds":"Konusma dili ve dikkat cekme tonu ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Muhataba seslenme islevini korur."},"facet_ids":["F001","F002"],"text":"hey","usage_role":"contextual"}],"definition":"Yakin ya da uzak muhataba seslenmek icin kullanilan nida birimi ve bunun uzatilmis seslenme bicimi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel islev, bir muhatabi seslenme yoluyla cagirmaktir."},{"facet_id":"F002","role":"specialization","statement":"Bir bicim yakin muhataba, digeri hem yakin hem uzak muhataba seslenebilir."},{"facet_id":"F003","role":"source_variant","statement":"Uzatilmis seslenme bicimi de ayni nida alaninda aktarilir."}],"identity_rationale":"Kaynak ifadesi yakin veya uzak muhataba seslenme icin kullanilan nida birimlerini verir ve uzatilmis bicimi de ekler. Dal cercevesi bunu soru veya aciklama islevlerinden ayri olarak dogru sinirlar.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yakin muhataba seslenme birimi"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yakin veya uzak muhataba seslenme birimi"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"uzatilmis seslenme bicimi"}],"lexicalization_note":"Non-bare kapsam, tanimi yalniz nida islevli gramer birimleriyle sinirlar ve genel kok anlamina yaymaz.","neighbor_coverage_note":"Seslenme eylemi ve ic gramer dallari siniri en iyi gosterir; soru, yemin ve isaret dallari ayrik islevlerdir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal seslenme edatidir; komsu dal seslenme veya cagirma eyleminin kendisini anlatir.","focus_only":"Bu dal seslenmeyi kuran gramer birimidir.","gloss":"seslenme","neighbor_only":"Komsu dal ses cikarma, cagirma ve yukseltme eylemini daha genis anlatir.","neighbor_ref":"root_001487/B001","relation_type":"near_neighbor","shared_zone":"Ikisi de cagirma ve muhataba yoneltilen ses alanini paylasir."},{"boundary_match":"partial","distinction":"Bu dal yakin ve uzak muhatap icin genel seslenme birimini verir; komsu dal belirli kisaltilmis hitap kaliplarina aittir.","focus_only":"Bu dal genel nida birimleridir.","gloss":"nida kalibi","neighbor_only":"Komsu dal kisaltilmis belirli seslenme kaliplariyla sinirlidir.","neighbor_ref":"root_001178/B003","relation_type":"near_neighbor","shared_zone":"Ikisi de muhataba seslenme yapilaridir."},{"boundary_match":"field_only","distinction":"Bu dal seslenme baslatir; komsu dal soru veya secme isleviyle belirsizi belirler.","focus_only":"Bu dal muhatabi cagirmaya yarar.","gloss":"nida ile soru","neighbor_only":"Komsu dal hangi kisi veya seyin kastedildigini sorar ya da belirler.","neighbor_ref":"root_000074/B004","relation_type":"same_field","shared_zone":"Ikisi de islevsel gramer birimleridir."},{"boundary_match":"field_only","distinction":"Bu dal muhataba donuktur; komsu dal onceki sozun anlamini aciklayan sonraki ifadeye donuktur.","focus_only":"Bu dal seslenme islevindedir.","gloss":"nida ile aciklama","neighbor_only":"Komsu dal aciklama veya yorum baslatir.","neighbor_ref":"root_000074/B009","relation_type":"same_field","shared_zone":"Ikisi de cumlede islevsel parca olarak gorulur."}],"source_phrase_ar":"في النداء أي فلان وقد يمد آي فلان (ayn)؛ أيا من حروف النداء ينادى بها القريب والبعيد؛ أي حرف ينادى به القريب (sihah)","source_summary":"Kaynaklar bu dali seslenme birimleri olarak verir; yakin muhatap, yakin-uzak muhatap ayrimi ve uzatilmis seslenme bicimi ayni iddiada yer alir.","sources":["AY","SI"],"what_is_ar":"يدخل فيه أي في نداء القريب، وأيا في نداء القريب والبعيد، وآي الممدودة في النداء.","what_is_not_ar":"ليس هو أيها الداخلة على الاسم بالألف واللام، ولا أي المفسرة، ولا أي الاستفهامية."},"support_links":[]},{"boundary":"Bu dal soru sormaz ve seslenmez; onceki ifadeyi aciklayan yorumlayici gramer birimidir.","branch_kind":"non_bare","branch_ref":"root_000074/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ءَايَة","morph_features":"STEM|POS:N|LEM:'aAyap|ROOT:Ayy|FP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:2:1","qac_word_ref":"31:2:2","surface_ar":"ءَايَٰتُ"}],"gloss":"yani aciklayicisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir aciklama veya yorumun basina gelerek onceki anlamin neye yoneldigini belirtir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ardindan gelen ifade, anlatilmak istenen anlamin aciklayici karsiligidir."}}],"root_ar":"ء ي ي","root_id":"root_000074","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Onceki ifadeyi aciklayan gramer islevini Turkcede dogal bicimde karsilar.","boundary_detail":"Bu dal soru sormaz ve seslenmez; onceki ifadeyi aciklayan yorumlayici gramer birimidir.","branch_image_ar":"أي مفسرة","concept_gloss":"yani aciklayicisi","contextual_glosses":[{"applicability":"Onceki sozun aciklamasini veren baglamlarda en dogal karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aciklama baslatma islevini korur."},"facet_ids":["F001"],"text":"yani","usage_role":"general"},{"applicability":"Aciklamanin yorumlayici sonuc gibi verildigi baglamlarda kullanilabilir.","error_profile":{"adds":"Sonuc cikarma tonu ekleyebilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Yorumlayici aciklama etkisini korur."},"facet_ids":["F002"],"text":"demek ki","usage_role":"contextual"}],"definition":"Onceki sozun veya anlamin ne demek oldugunu gostermek icin aciklama ifadesinden once gelen yorumlayici gramer birimi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir aciklama veya yorumun basina gelerek onceki anlamin neye yoneldigini belirtir."},{"facet_id":"F002","role":"associated_use","statement":"Ardindan gelen ifade, anlatilmak istenen anlamin aciklayici karsiligidir."}],"identity_rationale":"Kaynak ifadesi bu birimi onceki anlamin aciklamasini baslatan ve ardindan gelen sozle neyin kastedildigini gosteren unsur olarak verir. Dal cercevesi soru veya nida isleviyle karistirmadan dogru ayrim yapar.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"anlami aciklayan yani birimi"}],"lexicalization_note":"Non-bare kapsam, tanimi yalniz aciklama baslatan gramer birimiyle sinirlar; genel isaret veya soru anlami yuklenmez.","neighbor_coverage_note":"Aciklama ve yorum alanini ayiran komsular secildi; nida, yemin ve zamir dayanagi islevleri ayrik kalir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal aciklayici ifadeyi baglayan birimdir; komsu dal aciklama ve yorumlama eyleminin kendisini anlatir.","focus_only":"Bu dal aciklamayi baslatan kisa gramer birimidir.","gloss":"aciklama","neighbor_only":"Komsu dal bir seyi aciklama, yorumlama veya kapali anlami ortaya cikarma eylemidir.","neighbor_ref":"root_001155/B001","relation_type":"near_neighbor","shared_zone":"Ikisi de anlamin aciga cikarilmasi alanina girer."},{"boundary_match":"partial","distinction":"Bu dal aciklama oncesi baglayici unsur olarak kalir; komsu dal aciklama isinin kendisini sozluksel cekirdek yapar.","focus_only":"Bu dal onceki ifadeye aciklama getiren gramer unsurudur.","gloss":"anlami acma","neighbor_only":"Komsu dal kapali veya zor seyi acma ve anlamlandirma eylemidir.","neighbor_ref":"root_000784/B001","relation_type":"near_neighbor","shared_zone":"Ikisi de kapali anlamin belirginlestirilmesiyle ilgilidir."},{"boundary_match":"partial","distinction":"Bu dal kastedilen anlami aciklayan ifadeyi baslatir; komsu dal kastin veya talebin kendisini anlatir.","focus_only":"Bu dal aciklamayi gosteren gramer birimidir.","gloss":"kastedilen anlam","neighbor_only":"Komsu dal sozun maksadi, istenen sey veya amac alanina girer.","neighbor_ref":"root_001085/B005","relation_type":"near_neighbor","shared_zone":"Ikisi de bir sozle neyin istenip kastedildigini anlama alanina yakindir."},{"boundary_match":"field_only","distinction":"Bu dal sorulani istemez; onceki sozu aciklayan sonraki ifadeyi tanitir.","focus_only":"Bu dal aciklama baslatir.","gloss":"aciklama ile soru","neighbor_only":"Komsu dal soru, secme ve sart belirlemesi yapar.","neighbor_ref":"root_000074/B004","relation_type":"same_field","shared_zone":"Ikisi de islevsel gramer birimleridir."}],"source_phrase_ar":"أي تفسيرا للمعاني أي كذا وكذا (ayn)؛ أي كلمة تتقدم التفسير تقول أي كذا بمعنى تريد كذا (sihah)","source_summary":"Kaynaklar bu birimi anlamlari aciklamak icin aciklama sozunun onune gelen unsur olarak verir; islevi soru degil, yorum ve aciklamadir.","sources":["AY","SI"],"what_is_ar":"يدخل فيه أي التي تتقدم تفسير المعنى، كقولهم أي كذا وكذا أو أي بمعنى تريد كذا.","what_is_not_ar":"ليس هو أي الاستفهامية ولا إي في القسم ولا أيا في النداء."},"support_links":[]},{"boundary":"Bu dal soru veya aciklama degil; yemin oncesinde gelen onaylayici acilis sozudur.","branch_kind":"non_bare","branch_ref":"root_000074/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ءَايَة","morph_features":"STEM|POS:N|LEM:'aAyap|ROOT:Ayy|FP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:2:1","qac_word_ref":"31:2:2","surface_ar":"ءَايَٰتُ"}],"gloss":"yemin oncesi evet","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yemin ifadesini baslatir ve ona onaylayici bir giris saglar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlam degeri evet ya da bilakis gibi tasdik edici cevap sozune yakindir."}}],"root_ar":"ء ي ي","root_id":"root_000074","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yeminle bagli onaylayici acilis islevini acik ve kisa bicimde karsilar.","boundary_detail":"Bu dal soru veya aciklama degil; yemin oncesinde gelen onaylayici acilis sozudur.","branch_image_ar":"إي افتتاح للقسم","concept_gloss":"yemin oncesi evet","contextual_glosses":[{"applicability":"Yemin ifadesiyle birlikte gelen tasdikli baglamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tasdik ve yemin acilisini korur."},"facet_ids":["F001","F002"],"text":"evet, andolsun","usage_role":"contextual"},{"applicability":"Cevap degerinin bilakis veya evet tonu aldigi yemin baglaminda kullanilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tasdik edici cevap ve yemin girisini korur."},"facet_ids":["F001","F002"],"text":"bilakis, andolsun","usage_role":"contextual"}],"definition":"Bir yemin ifadesinden once gelip sozu onaylayan veya pekistiren, evet ya da bilakis degeri tasiyan acilis birimi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yemin ifadesini baslatir ve ona onaylayici bir giris saglar."},{"facet_id":"F002","role":"specialization","statement":"Anlam degeri evet ya da bilakis gibi tasdik edici cevap sozune yakindir."}],"identity_rationale":"Kaynak ifadesi bu birimi yemin veya ant oncesinde gelen, evet ya da bilakis onay degeri tasiyan acilis sozu olarak verir. Dal cercevesi bunu soru, aciklama ve zamir islevlerinden ayirir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yemin oncesi evet veya bilakis sozu"}],"lexicalization_note":"Non-bare kapsam, tanimi yalniz yeminle birlikte kullanilan onaylayici gramer sozune baglar.","neighbor_coverage_note":"Yemin ve tasdik alanindaki adaylar siniri en iyi gosterir; soru, nida ve zamir dayanak dallari farkli gramer islevleri tasir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yemin fiili degil, yeminin onune gelen tasdik sozudur; komsu dal yemin etme veya yemin adinin kendisini anlatir.","focus_only":"Bu dal yeminden once gelen onaylayici acilis sozudur.","gloss":"yemin girisi","neighbor_only":"Komsu dal yemin etme eylemi ve yemin adlari alanindadir.","neighbor_ref":"root_000048/B003","relation_type":"near_neighbor","shared_zone":"Ikisi de ant ve yemin soylemiyle ilgilidir."},{"boundary_match":"partial","distinction":"Bu dal yemin ifadesini baslatan onaylayici sozdur; komsu dal yeminin kendisine verilen addir.","focus_only":"Bu dal yemin oncesi tasdik birimidir.","gloss":"yemin ve tasdik","neighbor_only":"Komsu dal yemin veya ant anlamini sozluksel cekirdek olarak verir.","neighbor_ref":"root_000076/B007","relation_type":"near_neighbor","shared_zone":"Ikisi de yemin soyleminin parcalaridir."},{"boundary_match":"partial","distinction":"Bu dal yeminle sinirli bir acilis sozudur; komsu dal yemin baglantisi olmadan genel evet cevabidir.","focus_only":"Bu dal tasdiki yemin oncesinde kullanir.","gloss":"evet tasdiki","neighbor_only":"Komsu dal genel cevap ve tasdik sozu olarak kullanilir.","neighbor_ref":"root_000016/B003","relation_type":"near_synonym","shared_zone":"Ikisi de kabul veya tasdik bildiren cevap degeri tasir."},{"boundary_match":"field_only","distinction":"Bu dal antli tasdike baglidir; komsu dal onceki ifadenin anlamini aciklayan sozu tanitir.","focus_only":"Bu dal yemin oncesi tasdik verir.","gloss":"tasdik ile aciklama","neighbor_only":"Komsu dal aciklama baslatir.","neighbor_ref":"root_000074/B009","relation_type":"same_field","shared_zone":"Ikisi de kisa gramer birimleri olarak soz akisini yonlendirir."}],"source_phrase_ar":"إي تدخل في اليمين كالصلة والافتتاح؛ إي وربي؛ المعنى نعم والله (ayn)؛ إى بالكسر كلمة تتقدم القسم معناها بلى؛ إى ربى وإى والله (sihah)","source_summary":"Kaynaklar bu birimi yemin oncesinde gelen acilis veya baglayici soz olarak verir; anlam degeri tasdik ve pekistirme yonundedir.","sources":["AY","SI"],"what_is_ar":"يدخل فيه إي المكسورة التي تدخل في اليمين أو تتقدم القسم بمعنى نعم أو بلى.","what_is_not_ar":"ليس هو أي المفسرة، ولا أي للاستفهام، ولا إيا عماد الضمير."},"support_links":[]},{"boundary":"Alan, yargıda bulunmayı veya bir şeyi sağlamlaştırmayı değil, engelleyip geri çevirmeyi kapsar; düzeltme bu işlemin belirgin bir amacıdır ama her kullanımı sınırlandırmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000348/B001","candidate_links":[{"candidate_id":"cand_76ec2154e9f8f4d07002","lane":"macro"},{"candidate_id":"cand_bd3c2ccee142e3a0015f","lane":"macro"},{"candidate_id":"cand_a9bfcbc21a3b506f08ec","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"حَكِيم","morph_features":"STEM|POS:ADJ|LEM:Hakiym|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"31:2:4:2","qac_word_ref":"31:2:4","surface_ar":"حَكِيمِ"}],"gloss":"alıkoyup geri çevirmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel işlem, birini istediği veya yöneldiği şeyden ya da bir şeyi bozulmadan alıkoyup geri çevirmektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Savurgan ya da sorumsuz kişinin elini tutmak, onun zarar verici girişimini durdurmanın özel bir örneğidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Koruma altındaki birini bozulmadan uzak tutmak, yalnız engellemeyi değil onun durumunu düzeltme amacını da içerir."}}],"root_ar":"ح ك م","root_id":"root_000348","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel engelleme ve geri çevirme işlemini kısa biçimde karşılar; düzeltici kullanımlar kavram haritasındaki özelleşmelerle açıklanır.","boundary_detail":"Alan, yargıda bulunmayı veya bir şeyi sağlamlaştırmayı değil, engelleyip geri çevirmeyi kapsar; düzeltme bu işlemin belirgin bir amacıdır ama her kullanımı sınırlandırmaz.","branch_image_ar":"المنع والرد للإصلاح","concept_gloss":"alıkoyup geri çevirmek","contextual_glosses":[{"applicability":"Bir kişinin zararlı veya sorumsuz bir davranışa girişmesini fiilen önleme bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan dışındaki şeylerin bozulmasını önleme kapsamını dışarıda bırakır.","preserves":"Kişiyi zararlı davranıştan engelleme yönünü korur."},"facet_ids":["F001","F002"],"text":"elini tutup yanlışından alıkoymak","usage_role":"contextual"},{"applicability":"Koruma altındaki bir kişiyi bozulmadan uzak tutma ve durumunu düzeltme bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel engelleme ve geri çevirme işleminin bütün kullanım alanlarını kapsamaz.","preserves":"Koruma ve düzeltme amacını açık biçimde korur."},"facet_ids":["F001","F003"],"text":"koruyup doğru yola yöneltmek","usage_role":"contextual"}],"definition":"Birini istediği veya yöneldiği şeyden, bir şeyi de bozulmadan alıkoyup geri çevirmektir; bu işlem özellikle haksızlığı ya da bozulmayı önleme ve düzeltme amacıyla kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel işlem, birini istediği veya yöneldiği şeyden ya da bir şeyi bozulmadan alıkoyup geri çevirmektir."},{"facet_id":"F002","role":"specialization","statement":"Savurgan ya da sorumsuz kişinin elini tutmak, onun zarar verici girişimini durdurmanın özel bir örneğidir."},{"facet_id":"F003","role":"specialization","statement":"Koruma altındaki birini bozulmadan uzak tutmak, yalnız engellemeyi değil onun durumunu düzeltme amacını da içerir."}],"identity_rationale":"Kaynak anlatımlarının ortak işlemi, birini ya da bir şeyi yöneldiği veya istediği şeyden alıkoyup geri çevirmektir. Haksızlığı ve bozulmayı önleme ile düzeltme amacı bu işlemin güçlü bir gerekçesidir, ancak bütün tanıklıklarda zorunlu koşul olarak belirtilmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"haksızlıktan veya bozulmadan alıkoyup geri çevirmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sorumsuz kişinin elini tutup zarar vermesini önlemek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yetimi bozulmadan koruyup durumunu düzeltmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"birini yapmak istediği şeyden alıkoymak"}],"lexicalization_note":"Tanım ortak engelleme çekirdeğini korur; kişi, savurgan ve yetimle kurulan özel yapılar bu çekirdeğin ayrı gerçekleşmeleridir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlanan üç ilişki, düzeltici engellemenin genel önleme, tutma ve yargılama karşısındaki sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda haksızlığı veya bozulmayı önleme ve kişiyi istediği şeyden alıkoyma kullanımları öne çıkar; komşu dal kişinin kendini tutmasına ve gözyaşını bastırmaya da uzanır.","focus_only":"Engellemenin öne çıkan kullanımları haksızlığı veya bozulmayı önlemeye yönelir; dal ayrıca kişiyi istediği şeyden alıkoymayı da kapsar.","gloss":"alıkoyma ve önleme","neighbor_only":"Komşu dal kişinin kendini tutmasını ve gözyaşını bastırma gibi daha geniş kullanımları da kapsar.","neighbor_ref":"root_001308/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir eylemin sürmesini önleme ve bir şeyi geri tutma vardır."},{"boundary_match":"partial","distinction":"Komşu dal fiziksel tutma ve yoksun bırakma sonucuna daha geniş yer verir; odak dalda haksızlığı ya da bozulmayı önleme ve kişiyi istediğinden alıkoyma kullanımları öne çıkar.","focus_only":"Durdurma işleminin öne çıkan kullanımları haksızlığı ve bozulmayı önlemeye yönelir; dal ayrıca kişiyi istediği şeyden alıkoymayı da kapsar.","gloss":"tutup geri çevirmek","neighbor_only":"Komşu dal tutma, hapsetme, geri çevirme ve iyilikten yoksun bırakılma sonuçlarını birlikte kapsar.","neighbor_ref":"root_000193/B003","relation_type":"near_synonym","shared_zone":"İki dal da birini veya bir şeyi ilerlemekten ya da bir işe girişmekten alıkoyabilir."},{"boundary_match":"field_only","distinction":"Birincisi engelleme eylemini, ikincisi ise uyuşmazlığı karara bağlama eylemini temel alır; aynı bağlamda görülebilseler de birbirinin yerine geçmezler.","focus_only":"Odak dal birini ya da bir şeyi engelleyip geri çevirir; haksızlığı veya bozulmayı önleme bunun belirgin kullanımlarındandır.","gloss":"engelleme ile yargılama","neighbor_only":"Komşu dal taraflar veya bir önerme hakkında bağlayıcı karar verir.","neighbor_ref":"root_000348/B002","relation_type":"same_field","shared_zone":"İki dal haksızlığı önleme düşüncesinde ve insanlar arasındaki düzen alanında buluşur."}],"source_phrase_ar":"الحكم وهو المنع من الظلم (maqayis)؛ كل شيء منعته من الفساد فقد حكمته وحكمته وأحكمته (ayn)؛ حكمت السفيه وأحكمته إذا أخذت على يده (sihah)؛ كل من منعته من شيء فقد حكمته وأحكمته (tahdhib)؛ حكم أصله منع منعا لإصلاح (mufradat)","source_summary":"Kaynak anlatımları alıkoyma ve geri çevirme işleminde birleşir; haksızlığı veya bozulmayı önleme ile düzeltme amacı bu anlatımlardaki belirgin vurgulardır, ancak her tanıklığın zorunlu sınırı değildir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"منع الظلم والفساد؛ رد السفيه أو منعه؛ كف المرء عما يريد","what_is_not_ar":"القضاء بمجرده؛ الحكمة العلمية؛ إحكام الشيء وإتقانه؛ حكمة اللجام اسما للآلة"},"support_links":["sup_5712b0b2d10fda67a9c5","sup_627bc33a8346c850ddd6","sup_c05798d40f82a678d48a"]},{"boundary":"Dalın çekirdeği uyuşmazlığı veya bir savı karara bağlamaktır; özel bedel hesapları ve salt yetki devri çekirdeğe katılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000348/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَكِيم","morph_features":"STEM|POS:ADJ|LEM:Hakiym|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"31:2:4:2","qac_word_ref":"31:2:4","surface_ar":"حَكِيمِ"}],"gloss":"uyuşmazlığı bağlayıcı kararla sonuçlandırmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel işlem, insanlar arasındaki uyuşmazlığı bağlayıcı bir kararla sona erdirmektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karar verme, bir durumun belirli biçimde olduğunu ya da olmadığını saptamaya da uzanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tarafların yetkili bir karar merciine başvurması, kararın kendisi değil bu sürece giriş eylemidir."}}],"root_ar":"ح ك م","root_id":"root_000348","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanlar arasındaki karar verme çekirdeğini doğal biçimde karşılar ve salt engellemeden ayrılır.","boundary_detail":"Dalın çekirdeği uyuşmazlığı veya bir savı karara bağlamaktır; özel bedel hesapları ve salt yetki devri çekirdeğe katılmaz.","branch_image_ar":"الحكم والقضاء بين الناس","concept_gloss":"uyuşmazlığı bağlayıcı kararla sonuçlandırmak","contextual_glosses":[{"applicability":"İki ya da daha çok taraf arasındaki çekişmenin karara bağlandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir savın doğru olup olmadığını belirleme uzantısını kapsamaz.","preserves":"Taraflar arasında karar verme işlemini korur."},"facet_ids":["F001"],"text":"taraflar arasında karar vermek","usage_role":"general"},{"applicability":"Bir nesne, olay veya sav hakkında olumlu ya da olumsuz belirleme yapıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanlar arasındaki uyuşmazlığı sonuçlandırma çekirdeğini dışarıda bırakır.","preserves":"Bir durumun öyle olup olmadığını karara bağlama yönünü korur."},"facet_ids":["F002"],"text":"öyle olduğuna karar vermek","usage_role":"contextual"}],"definition":"İnsanlar arasındaki bir uyuşmazlığı doğru ölçüye göre bağlayıcı bir kararla sonuçlandırmak veya bir şeyin öyle olup olmadığına karar vermektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel işlem, insanlar arasındaki uyuşmazlığı bağlayıcı bir kararla sona erdirmektir."},{"facet_id":"F002","role":"extension","statement":"Karar verme, bir durumun belirli biçimde olduğunu ya da olmadığını saptamaya da uzanır."},{"facet_id":"F003","role":"associated_use","statement":"Tarafların yetkili bir karar merciine başvurması, kararın kendisi değil bu sürece giriş eylemidir."}],"identity_rationale":"Kaynak anlatımı, insanlar arasında karar vermeyi ve bir şeyin öyle olup olmadığına karar bağlamayı açıkça destekler. Yaralanma bedelini hesaplama gibi özel uygulamalar ayrı sözcük birimlerinde görülür; bunlar dalın genel çekirdeği değil, yargısal karar vermenin özel kullanımlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"insanlar arasında doğru ölçüyle karar vermek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"biri lehine veya aleyhine karar vermek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"karar verme veya işi karara bağlama"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"insanlar arasında karar veren kişi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"karar verme işiyle özellikle görevli kişi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"çekişmede verilen karar veya yaralanma karşılığını belirleme"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"çekişmeyi karar verecek bir mercie götürmek"}],"lexicalization_note":"Tanım karar verme çekirdeğini verir; kişiler arasında karar verme, biri lehine karar verme ve bir karar merciine başvurma yapıları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen ilişkiler karar verme çekirdeğini yakın karar dallarından ve yetki devrinden ayıran en yararlı karşılaştırmalardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekler büyük ölçüde örtüşür; odak dal belirleme anlamına uzanırken komşu dal ayırıp sonuca bağlama yönünü daha belirgin taşır.","focus_only":"Odak dal, bir durumun öyle olup olmadığını belirleme kullanımını da taşır.","gloss":"uyuşmazlığı karara bağlamak","neighbor_only":"Komşu dal, doğru ile yanlışı keskin biçimde ayırma ve son sözü söyleme görüntüsünü öne çıkarır.","neighbor_ref":"root_001159/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da çekişen taraflar arasında ayırıcı ve sonuçlandırıcı karar vermeyi kapsar."},{"boundary_match":"partial","distinction":"Odak dalın önerme hakkında karar verme uzantısı daha geniştir; komşu dal ise açıp ayırarak çözme görüntüsüne ve karar vericiye bağlıdır.","focus_only":"Odak dal kararın içeriğini ve bir sav hakkında belirleme yapmayı birlikte kapsar.","gloss":"taraflar arasında karar vermek","neighbor_only":"Komşu dal, uyuşmazlığı açıp çözerek kapatan karar verici kişiyi de adlandırır.","neighbor_ref":"root_001124/B003","relation_type":"near_synonym","shared_zone":"İki dalın merkezinde çekişen taraflar arasında karar vererek uyuşmazlığı bitirmek bulunur."},{"boundary_match":"field_only","distinction":"Karar verme eylemi ile o eylemi yapma yetkisinin başkasına bırakılması farklı aşamalardır; biri diğerini gerektirebilir ama tanımlamaz.","focus_only":"Odak dal bağlayıcı kararın verilmesini anlatır.","gloss":"karar ile yetki devri","neighbor_only":"Komşu dal karar verme yetkisinin bir kişiye bırakılmasını anlatır.","neighbor_ref":"root_000348/B005","relation_type":"same_field","shared_zone":"Her iki dalda da bir kişi karar verme görevini üstlenebilir ve taraflar bu karara bağlanabilir."}],"source_phrase_ar":"الحكم وهو المنع من الظلم (maqayis)؛ حاكمناه إلى الله دعوناه إلى حكم الله (ayn)؛ الحكم مصدر قولك حكم بينهم أي قضى (sihah)؛ الحكم أيضا القضاء بالعدل (tahdhib)؛ الحكم بالشيء أن تقضي بأنه كذا أو ليس بكذا (mufradat)","source_summary":"Kaynaklar, insanlar arasında karar vermeyi, haksızlığı önleyen bir sonuç üretmeyi ve bir durumun öyle olup olmadığını karara bağlamayı ortaklaştırır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"القضاء بالعدل؛ الحكم بين الناس؛ الحكومة والتحاكم والمحاكمة؛ تقدير الأرش في الجراحات","what_is_not_ar":"المنع العام؛ الحكمة بمعنى العلم؛ تفويض التصرف في المال بلا خصومة"},"support_links":[]},{"boundary":"Dal, bilgi ve usla doğruyu bulma yetkinliğidir; yargısal karar, salt öğrenilmiş bilgi veya yalnızca işçilik ustalığı değildir.","branch_kind":"bare","branch_ref":"root_000348/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَكِيم","morph_features":"STEM|POS:ADJ|LEM:Hakiym|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"31:2:4:2","qac_word_ref":"31:2:4","surface_ar":"حَكِيمِ"}],"gloss":"bilgi ve usla doğruyu bulma yetkinliği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bilgi ve us, kişinin doğruyu yanlıştan ayırıp doğru olana ulaşmasını sağlar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu yetkinlikte bilgiye ölçülülük ve ağırbaşlılık eşlik eder."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu yetkinliğe sahip kişi bilgili, deneyimli ve yerinde davranan biri olarak nitelenir."}}],"root_ar":"ح ك م","root_id":"root_000348","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bilgi, us, ölçülülük ve doğruya ulaşma bileşenlerini tek bir doğal açıklamada birleştirir.","boundary_detail":"Dal, bilgi ve usla doğruyu bulma yetkinliğidir; yargısal karar, salt öğrenilmiş bilgi veya yalnızca işçilik ustalığı değildir.","branch_image_ar":"الحكمة والعلم المصيب","concept_gloss":"bilgi ve usla doğruyu bulma yetkinliği","contextual_glosses":[{"applicability":"Bilgi, deneyim, ölçülülük ve doğru davranışı birlikte düşündüren genel bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgi, deneyim, ölçülülük ve doğruyu bulma yetkinliğini birlikte korur."},"facet_ids":["F001","F002","F003"],"text":"bilgelik","usage_role":"general"},{"applicability":"Bu yetkinliği taşıyan kişinin bilgisi ve yerinde kavrayışı vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ölçülülük ve iyi davranış boyutunu açıkça taşımaz.","preserves":"Kişinin bilgili oluşunu ve doğruya ulaşma yetisini korur."},"facet_ids":["F001","F003"],"text":"doğruyu gören bilgili kişi","usage_role":"contextual"}],"definition":"Bilgi, us ve ağırbaşlılık sayesinde doğruyu yerinde bulma yetkinliğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bilgi ve us, kişinin doğruyu yanlıştan ayırıp doğru olana ulaşmasını sağlar."},{"facet_id":"F002","role":"core","statement":"Bu yetkinlikte bilgiye ölçülülük ve ağırbaşlılık eşlik eder."},{"facet_id":"F003","role":"associated_use","statement":"Bu yetkinliğe sahip kişi bilgili, deneyimli ve yerinde davranan biri olarak nitelenir."}],"identity_rationale":"Kaynak anlatımı bilgiyi, anlayışı, ağırbaşlılığı ve doğruyu bilgi ile us yoluyla bulmayı tek bir yetkinlik alanında birleştirir. Bu alan salt bilgi sahibi olmaktan daha güçlü, yargılama ya da teknik ustalıktan ise farklıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bilgi ve kavrayış ya da doğru bir önerme"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bilgi ve usla doğruyu bulma yetkinliği"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bilgili, deneyimli ve doğruyu bulan kişi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"deneyimle olgunlaşmış bilge yaşlı"}],"lexicalization_note":"Tanım çıplak dalın bilgi, anlayış, ölçülülük ve doğruya erişme çekirdeğiyle sınırlıdır; başka dalların özel yapılarını içeri almaz.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; yayımlanan ilişkiler bu dalı salt bilgiden, hızlı kavrayıştan ve yalnız ağırbaşlılıktan ayıran temel sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal bilişsel kavrayışa odaklanır; odak dal ise bu kavrayışın doğruyu bulma, ölçülülük ve iyi davranışla bütünleşmesini gerektirir.","focus_only":"Odak dal, bilgiyi ölçülü ve doğru davranışa dönüştürme yetkinliğini içerir.","gloss":"bilme ve doğruyu bulma","neighbor_only":"Komşu dal hızlı kavrama ve bir şeyin anlamlarını doğrulama süreçlerini daha geniş biçimde kapsar.","neighbor_ref":"root_001182/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bilgi edinme, anlama ve bir şeyin anlamını usla kavrama alanında örtüşür."},{"boundary_match":"partial","distinction":"Ağırbaşlılık odak dalın bir bileşenidir ama bilgiyle doğruyu bulma çekirdeğinin yerini tutmaz; komşu dal bu bilişsel koşulu gerektirmez.","focus_only":"Bilgi ve us yoluyla doğruya erişme yetkinliği belirleyicidir.","gloss":"bilgelik ve ağırbaşlılık","neighbor_only":"Komşu dal zihinsel sağlamlık, ağırbaşlılık ve cömertlik niteliklerini öne çıkarır.","neighbor_ref":"root_000591/B006","relation_type":"near_neighbor","shared_zone":"İki dal da ölçülü, dengeli ve yerinde davranan kişinin niteliğini anlatabilir."},{"boundary_match":"partial","distinction":"Bilgi odak dalın gerekli öğesidir, fakat odak dal onu us, ölçü ve doğru davranışla birleştirir; komşu dal salt bilgi süreçlerini de kapsar.","focus_only":"Doğruya ulaşan ölçülü uygulama ve davranış sonucu bulunur.","gloss":"bilgi ve bilgelik","neighbor_only":"Komşu dal öğrenme, öğretme, bildirme ve haber edinme süreçlerine kadar uzanır.","neighbor_ref":"root_001040/B001","relation_type":"near_neighbor","shared_zone":"Bilgi edinme ve bir şeyi bilinir duruma getirme iki alanın ortak zeminidir."}],"source_phrase_ar":"الحكمة تمنع من الجهل (maqayis)؛ الحكمة مرجعها إلى العدل والعلم والحلم (ayn)؛ الحكمة من العلم والحكيم العالم وصاحب الحكمة (sihah)؛ الحكم العلم والفقه (tahdhib)؛ الحكمة إصابة الحق بالعلم والعقل (mufradat)","source_summary":"Kaynakların ortak özeti, bilgisizliği uzaklaştıran bilgi ve anlayışın ölçülü davranışla birleşerek kişiyi doğru sonuca ulaştırmasıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"العلم والفقه؛ الحلم؛ إصابة الحق بالعلم والعقل؛ وصف الحكيم والعالم وصاحب الحكمة","what_is_not_ar":"القضاء بين الخصوم؛ إتقان الصنعة فقط؛ مجرد المنع الحسي"},"support_links":[]},{"boundary":"Çekirdek sağlamlaştırma ve kusursuzlaştırmadır; bilgi sahibi olma, yargılama ve düzeltici engelleme bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000348/B004","candidate_links":[{"candidate_id":"cand_76ec2154e9f8f4d07002","lane":"macro"},{"candidate_id":"cand_584680d8279eb2f9be35","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"حَكِيم","morph_features":"STEM|POS:ADJ|LEM:Hakiym|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"31:2:4:2","qac_word_ref":"31:2:4","surface_ar":"حَكِيمِ"}],"gloss":"sağlam ve kusursuz duruma getirmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin yapısı veya düzeni sağlamlaştırılır ve kusur barındırmayacak biçimde tamamlanır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Süreç sonunda şey, sağlamlığı yerleşmiş ve bozulmaya karşı dirençli bir duruma gelir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir söz veya metin, kuşkuya ve karışıklığa yer bırakmayacak açıklıkta düzenlenmiş olabilir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kişinin övgüye değer niteliğinde en ileri düzeye varması, sağlamlaşmanın kişiye uygulanmış özel bir anlatımıdır."}}],"root_ar":"ح ك م","root_id":"root_000348","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yapılan işlemi ve amaçlanan sağlam, eksiksiz sonuç durumunu birlikte taşıyan genel karşılıktır.","boundary_detail":"Çekirdek sağlamlaştırma ve kusursuzlaştırmadır; bilgi sahibi olma, yargılama ve düzeltici engelleme bu dala girmez.","branch_image_ar":"الإحكام والإتقان والوثاقة","concept_gloss":"sağlam ve kusursuz duruma getirmek","contextual_glosses":[{"applicability":"Bir işin, yapının veya düzenin gevşeklik bırakmadan güçlendirildiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kusursuzluk ve kuşkusuz açıklık yönlerini açıkça belirtmez.","preserves":"Sağlamlaştırma işlemini ve yerleşmiş sonucu korur."},"facet_ids":["F001","F002"],"text":"iyice sağlamlaştırmak","usage_role":"general"},{"applicability":"Bir sözün veya metnin açıklık ve tutarlılık bakımından eksiksiz kılındığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Fiziksel ya da genel sağlamlaştırma kapsamını dışarıda bırakır.","preserves":"Kuşku ve karışıklığı gideren düzenleme yönünü korur."},"facet_ids":["F003"],"text":"kuşkuya yer bırakmayacak biçimde düzenlemek","usage_role":"contextual"}],"definition":"Bir şeyi gevşeklik, eksik veya kuşku taşımayacak ölçüde sağlam ve kusursuz duruma getirmek ya da onun böyle bir duruma yerleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin yapısı veya düzeni sağlamlaştırılır ve kusur barındırmayacak biçimde tamamlanır."},{"facet_id":"F002","role":"core","statement":"Süreç sonunda şey, sağlamlığı yerleşmiş ve bozulmaya karşı dirençli bir duruma gelir."},{"facet_id":"F003","role":"extension","statement":"Bir söz veya metin, kuşkuya ve karışıklığa yer bırakmayacak açıklıkta düzenlenmiş olabilir."},{"facet_id":"F004","role":"source_variant","statement":"Bir kişinin övgüye değer niteliğinde en ileri düzeye varması, sağlamlaşmanın kişiye uygulanmış özel bir anlatımıdır."}],"identity_rationale":"Kaynak anlatımı bir şeyi sağlam, kusursuz ve kuşkuya yer bırakmayacak duruma getirme ile bu durumun yerleşmesini ortak çekirdek olarak destekler. Bir kişinin kendi niteliğinde en ileri düzeye varması ise aynı sağlamlaşma görüntüsünün özel uzantısıdır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir şeyi sağlamlaştırmak veya sağlam duruma gelmek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kusur ve kuşkuya yer bırakmayacak biçimde sağlamlaştırılmış"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"işleri sağlam ve kusursuz yapan"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"övgüye değer niteliğinde doruğa varmak"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kendisine zarar verecek şeylerden bütünüyle uzaklaşmak"}],"lexicalization_note":"Tanım yapma ve sonuç durumunu ayırır; metnin açıklığı ile kişinin kendi niteliğinde doruğa varması özel, yapıya bağlı uzantılar olarak kalır.","neighbor_coverage_note":"Bütün adaylar incelendi; seçilen üç yakın ilişki genel sağlamlaştırmayı işçilik, yapısal güç ve söz ya da dokuma alanındaki sıkılıktan ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Sağlamlaştırma çekirdekleri yakındır; odak dal kusursuzluk ve kuşkusuz açıklığı, komşu dal ise yapısal güç ile güvenilir seçimi ayrıca kapsar.","focus_only":"Odak dal kuşkuyu gideren açıklık ve bir niteliğin doruğuna ulaşma uzantılarını taşır.","gloss":"sağlamlaştırma ve güvenilirlik","neighbor_only":"Komşu dal canlıların yapısal sağlamlığına ve bir işte en güvenilir olanı seçmeye kadar uzanır.","neighbor_ref":"root_001623/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi güçlü, dayanıklı ve güvenilir duruma getirmeyi anlatır."},{"boundary_match":"partial","distinction":"Komşu dal yapım becerisi ve güzel işçiliğe daha yakındır; odak dal sağlam, eksiksiz ve kuşkusuz sonuç durumunu temel alır.","focus_only":"Odak dal kuşkuya yer bırakmayan açıklık ve yerleşmiş sağlamlık sonucunu içerir.","gloss":"kusursuz yapma","neighbor_only":"Komşu dal işçilik becerisini, güzel yapmayı ve canlıdaki güçlü yaratılışı öne çıkarır.","neighbor_ref":"root_000290/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir işi iyi yapıp ürünü sağlam ve düzgün bir sonuca ulaştırabilir."},{"boundary_match":"partial","distinction":"Komşu dalın dokuma ve söz alanı belirgindir; odak dal ise genel sağlamlaştırmayı, sonuç durumunu ve kuşkunun giderilmesini kapsar.","focus_only":"Odak dal her tür şeyin sağlamlaştırılmasını ve sağlamlığın yerleşmesini kapsar.","gloss":"sağlam ve düzgün kurmak","neighbor_only":"Komşu dal özellikle dokuma ile sözün sıkı, doğru ve düzgün kurulmasına bağlıdır.","neighbor_ref":"root_000347/B010","relation_type":"near_synonym","shared_zone":"İki dal da bir ürünü gevşeklik ve kusur bırakmadan sağlam, tutarlı biçimde kurmayı anlatır."}],"source_phrase_ar":"استحكم الأمر وثق (ayn)؛ أحكمت الشيء فاستحكم أي صار محكما (sihah)؛ آياته أحكمت وفصلت (tahdhib)؛ المحكم ما لا يعرض فيه شبهة (mufradat)؛ حكم الرجل إذا بلغ النهاية في معناه (tahdhib)","source_summary":"Kaynaklar bir şeyi sağlamlaştırma, onun bu durumda yerleşmesi ve kuşku ya da eksik barındırmayan bir bütünlük kazanması çevresinde birleşir.","sources":["AY","SI","TA","MU"],"what_is_ar":"إحكام الشيء حتى يستحكم؛ كون الأمر وثيقا أو محكما؛ الآيات المحكمات؛ بلوغ الشيء نهايته في المدح أو السلامة","what_is_not_ar":"القضاء بين الناس؛ الحكمة بمعنى العلم فقط؛ منع السفيه أو الدابة"},"support_links":["sup_5712b0b2d10fda67a9c5","sup_8d457ca41ac0b90c1e02"]},{"boundary":"Dal, kararın kendisini değil karar verme veya davranma yetkisinin birine bırakılmasını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000348/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَكِيم","morph_features":"STEM|POS:ADJ|LEM:Hakiym|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"31:2:4:2","qac_word_ref":"31:2:4","surface_ar":"حَكِيمِ"}],"gloss":"karar verme yetkisini başkasına bırakmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işin yürütülmesi veya karara bağlanması başka bir kişinin yetkisine bırakılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çekişen taraflar, aralarındaki konuda seçtikleri kişinin vereceği kararı geçerli sayar."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yetki verilen kişi, belirlenen iş veya mal üzerinde uygun gördüğü biçimde davranabilir."}}],"root_ar":"ح ك م","root_id":"root_000348","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İş, mal ve uyuşmazlık bağlamlarında ortak olan yetki devri çekirdeğini en kısa doğal biçimde karşılar.","boundary_detail":"Dal, kararın kendisini değil karar verme veya davranma yetkisinin birine bırakılmasını kapsar.","branch_image_ar":"التفويض والتحكيم","concept_gloss":"karar verme yetkisini başkasına bırakmak","contextual_glosses":[{"applicability":"Bir işin sonucunu başka bir kişinin seçimine ve kararına bağlama bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşi devretme, karar yetkisi verme ve sonucu o seçime bağlama yönlerini korur."},"facet_ids":["F001","F002","F003"],"text":"işi onun kararına bırakmak","usage_role":"general"},{"applicability":"Kişiye bir mal veya iş üzerinde uygun gördüğü gibi davranma izni verildiğinde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Taraflar arasında karar verme görevinin devrini kapsamaz.","preserves":"Kişiye serbest davranma yetkisi verilmesini korur."},"facet_ids":["F003"],"text":"eli serbest bırakılmak","usage_role":"contextual"}],"definition":"Bir iş, mal veya uyuşmazlık hakkında karar verme ve uygun gördüğü biçimde davranma yetkisini başka bir kişiye bırakmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işin yürütülmesi veya karara bağlanması başka bir kişinin yetkisine bırakılır."},{"facet_id":"F002","role":"specialization","statement":"Çekişen taraflar, aralarındaki konuda seçtikleri kişinin vereceği kararı geçerli sayar."},{"facet_id":"F003","role":"extension","statement":"Yetki verilen kişi, belirlenen iş veya mal üzerinde uygun gördüğü biçimde davranabilir."}],"identity_rationale":"Kaynak anlatımı bir işin veya karar verme yetkisinin başka bir kişiye bırakılmasını, tarafların o kişinin kararını geçerli saymasını ve kişiye belirli alanda serbest davranma gücü verilmesini ortaklaştırır. Verilen kararın içeriği değil, yetkinin devri çekirdektir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir işte karar verme yetkisini ona bırakmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"malı üzerinde uygun gördüğü gibi davranabilmek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yetim malını yönetmeye elverişli duruma geldiğinde malı üzerinde tasarruf etmesine izin vermek"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"birinin elini istediğini yapmakta serbest bırakmak"}],"lexicalization_note":"Tanım yetki devri çekirdeğini korur; mal üzerinde serbest davranma, taraflar arasında karar verme ve elini serbest bırakma yapıları ayrı uygulamalardır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan ilişkiler özel karar yetkisi devrini genel iş devrinden, vekillikten ve kararın verilmesinden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın belirleyici yönü karar veya davranma yetkisidir; komşu dalda işi geri çevirip başkasına dayanma ilişkisi daha geniştir.","focus_only":"Odak dal, tarafların bir kişiye karar verme gücü tanımasını ve onun kararını geçerli saymasını kapsar.","gloss":"işi başkasına bırakmak","neighbor_only":"Komşu dal işi başkasına bırakırken ona dayanma ve sonucu ona emanet etme tutumunu öne çıkarır.","neighbor_ref":"root_001187/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda bir işin yönetimi veya sonucu başka bir kişinin eline verilir."},{"boundary_match":"partial","distinction":"Genel iş devri komşu dalda yeterlidir; odak dal özellikle karar verme serbestisini ve verilen kararın kabulünü öne çıkarır.","focus_only":"Uyuşmazlıktaki tarafların seçilen kişinin kararını önceden geçerli sayması odak dala özgüdür.","gloss":"yetkiyi başkasına vermek","neighbor_only":"Komşu dal vekil kılmayı ve genel olarak bir işi başkasına gördürmeyi daha geniş kapsar.","neighbor_ref":"root_001681/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir işin yürütülmesi veya karara bağlanması için başkasına yetki vermeyi içerir."},{"boundary_match":"field_only","distinction":"Yetkinin verilmesi ile bu yetkiye dayanılarak karar verilmesi ayrı işlemlerdir; odak dal sonuçtan önceki yetkilendirme aşamasıdır.","focus_only":"Odak dal karar verme yetkisinin kurulmasını anlatır.","gloss":"yetkilendirme ve karar","neighbor_only":"Komşu dal yetki kullanılarak bağlayıcı karar verilmesini anlatır.","neighbor_ref":"root_000348/B002","relation_type":"same_field","shared_zone":"İki dal aynı uyuşmazlıkta ardışık aşamalar olarak bulunabilir ve karar veren bir kişiyi gerektirebilir."}],"source_phrase_ar":"حكم فلان في كذا إذا جعل أمره إليه (maqayis)؛ احتكم في ماله إذا جاز فيه حكمه (ayn)؛ حكمته في مالي إذا جعلت إليه الحكم فيه (sihah)؛ حكمنا فلانا بيننا أي أجزنا حكمه بيننا (tahdhib)؛ الحكمين أن يتوليا الحكم عليهم ولهم حسب ما يستصوبانه (mufradat)","source_summary":"Kaynaklar, bir işin veya karar verme gücünün başka bir kişiye bırakılması ve o kişinin belirlenen alandaki seçiminin geçerli sayılması üzerinde birleşir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"جعل الحكم أو الأمر إلى شخص؛ إجازة حكمه بين المتخاصمين؛ الاحتكام إلى من يحكم؛ إطلاق يد المرء فيما شاء","what_is_not_ar":"القضاء الصادر نفسه؛ المنع والرد؛ الحكمة العلمية"},"support_links":[]},{"boundary":"Çekirdek, gemin çene çevresini kuşatan kısıtlayıcı parçasıdır; her halka, bağ veya hayvan çenesi genel olarak bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000348/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَكِيم","morph_features":"STEM|POS:ADJ|LEM:Hakiym|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"31:2:4:2","qac_word_ref":"31:2:4","surface_ar":"حَكِيمِ"}],"gloss":"gemin çene çevresini kuşatan kısıtlayıcı parçası","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Parça, hayvanın iki çene yanını veya ağız çevresini kuşatan bir gem bölümüdür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu kuşatma hayvanın koşmasını ve denetimsiz ilerlemesini sınırlar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adlandırma, aracın hayvanı engelleme işleviyle açıklanır; salt genel engelleme anlamı değildir."}}],"root_ar":"ح ك م","root_id":"root_000348","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Aracın yerini ve hayvanın hareketini sınırlayan temel işlevini birlikte açıklar.","boundary_detail":"Çekirdek, gemin çene çevresini kuşatan kısıtlayıcı parçasıdır; her halka, bağ veya hayvan çenesi genel olarak bu dala girmez.","branch_image_ar":"حكمة اللجام","concept_gloss":"gemin çene çevresini kuşatan kısıtlayıcı parçası","contextual_glosses":[{"applicability":"Parçanın hayvanın başındaki konumu anlatılırken kullanılan kısa ve doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanın koşmasını sınırlayan işlevi açıkça söylemez.","preserves":"Gem bölümünü ve çene çevresindeki konumunu korur."},"facet_ids":["F001"],"text":"gemin çeneyi saran bölümü","usage_role":"general"},{"applicability":"Parçanın koşmayı ve ileri atılmayı sınırlayan işlevi öne çıkarıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Parçanın çene veya ağız çevresini kuşatan konumunu açıkça vermez.","preserves":"Gemin hayvanı kısıtlayan işlevini korur."},"facet_ids":["F002","F003"],"text":"hayvanı tutan gem parçası","usage_role":"contextual"}],"definition":"Gemin, hayvanın çene çevresini veya ağzını kuşatarak onun koşmasını ve ileri atılmasını sınırlayan parçasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Parça, hayvanın iki çene yanını veya ağız çevresini kuşatan bir gem bölümüdür."},{"facet_id":"F002","role":"core","statement":"Bu kuşatma hayvanın koşmasını ve denetimsiz ilerlemesini sınırlar."},{"facet_id":"F003","role":"associated_use","statement":"Adlandırma, aracın hayvanı engelleme işleviyle açıklanır; salt genel engelleme anlamı değildir."}],"identity_rationale":"Kaynak anlatımı dalı, gemin hayvanın çene çevresini kuşatan ve koşmasını sınırlayan parçası olarak destekler. Geçici çerçevedeki halka veya çenenin kendisi ifadesi genel tanıma katılmamalıdır; çene anlamı yalnız ayrı bir sözcük biriminde özel olarak bulunur.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"gemin hayvanın çene çevresini kuşatıp koşmasını sınırlayan parçası"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"hayvana gem takmak veya onu gemle durdurmak"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"koyunun çenesi"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"başında gemin kısıtlayıcı parçası bulunan at"}],"lexicalization_note":"Tanım gem ve hayvanla sınırlı araç anlamını korur; gem takma eylemi, koyun çenesi ve bu parçayı taşıyan at ayrı kullanımlardır.","neighbor_coverage_note":"Tüm adaylar incelendi; seçilen ilişkiler bu parçayı gem halkalarından, genel kısıtlama araçlarından ve çene kemiğinin kendisinden ayırır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komşu dal belirli iki halkaya, odak dal ise çene çevresini kuşatıp hareketi sınırlayan daha işlevsel gem bölümüne karşılık gelir.","focus_only":"Odak dal çene çevresini kuşatan ve hayvanı kısıtlayan gem bölümünün bütününü anlatır.","gloss":"gem bölümü ve uç halkaları","neighbor_only":"Komşu dal yalnız ağız demirinin iki ucundaki iki halkayı adlandırır.","neighbor_ref":"root_000684/B008","relation_type":"same_field","shared_zone":"İki dal da gem takımının hayvanın ağzı çevresinde bulunan parçalarını anlatır."},{"boundary_match":"partial","distinction":"Odak dalın araç türü ve hayvan başındaki konumu belirgindir; komşu dal her türlü kısıtlayıcı bağ ve araca uzanan daha geniş bir alandır.","focus_only":"Odak dal hayvanın çene çevresindeki belirli gem parçasıyla sınırlıdır.","gloss":"kısıtlayıcı gem parçası","neighbor_only":"Komşu dal insanı veya şeyi hareketten alıkoyan zincir, demir ve başka araçları da kapsar.","neighbor_ref":"root_001554/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir araç veya gem bölümü hareketi engelleme işlevi görür."},{"boundary_match":"field_only","distinction":"Biri çene çevresine yerleştirilen işlevsel bir araç parçası, diğeri ise bedenin doğal kemik bölümüdür.","focus_only":"Odak dal çene çevresine takılan ve kısıtlama işlevi gören bir araç parçasıdır.","gloss":"gem parçası ve çene kemiği","neighbor_only":"Komşu dal çene kemiğinin kendisini ve diş ya da sakal köklerinin bulunduğu bölgeyi anlatır.","neighbor_ref":"root_001350/B001","relation_type":"same_field","shared_zone":"İki dal aynı çene bölgesine gönderme yapar ve hayvan betimlemelerinde birlikte görülebilir."}],"source_phrase_ar":"حكمة الدابة لأنها تمنعها (maqayis)؛ حكمة اللجام ما أحاط بحنكيه (ayn)؛ حكمة اللجام ما أحاط بالحنك (sihah)؛ حكمة اللجام ما أحاط بحنكيه (tahdhib)؛ سميت اللجام حكمة الدابة (mufradat)","source_summary":"Kaynaklar terimi hayvanın gemiyle ilişkisi çevresinde birleştirir; tanıklıklar çene çevresini kuşatan bölüm, hayvanı kısıtlama işlevi ve gemin bu adla anılması yönlerini farklı biçimlerde öne çıkarır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"حكمة الدابة؛ ما يحيط بحنكي الدابة؛ الحلقة أو الذقن وما يمنع الفرس من الجري","what_is_not_ar":"الحكمة بمعنى العلم؛ الحكم القضائي؛ المنع المجرد من غير آلة"},"support_links":[]},{"boundary":"Alan yalnız belirtilen yapıdaki kendiliğinden geri dönme ve ettirgen geri döndürme anlamlarını kapsar.","branch_kind":"non_bare","branch_ref":"root_000348/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَكِيم","morph_features":"STEM|POS:ADJ|LEM:Hakiym|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"31:2:4:2","qac_word_ref":"31:2:4","surface_ar":"حَكِيمِ"}],"gloss":"bir şeyden geri dönmek veya birini döndürmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi yöneldiği veya giriştiği bir şeyden kendi hareketiyle geri döner."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgen kullanımda başka biri kişiyi yöneldiği şeyden geri döndürür."}}],"root_ar":"ح ك م","root_id":"root_000348","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kanıtlanan özel yapılarda hem kendiliğinden hem ettirgen katılımcı düzenini karşılar.","boundary_detail":"Alan yalnız belirtilen yapıdaki kendiliğinden geri dönme ve ettirgen geri döndürme anlamlarını kapsar.","branch_image_ar":"الرجوع والإرجاع عن الشيء","concept_gloss":"bir şeyden geri dönmek veya birini döndürmek","contextual_glosses":[{"applicability":"Kişinin yöneldiği veya giriştiği bir şeyden kendi isteği ya da hareketiyle dönmesi bağlamındadır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka bir kişinin onu geri döndürdüğü ettirgen düzeni kapsamaz.","preserves":"Kişinin bir şeyden kendi hareketiyle geri dönmesini korur."},"facet_ids":["F001"],"text":"o işten geri dönmek","usage_role":"contextual"},{"applicability":"Bir kişinin başka birini yöneldiği veya giriştiği şeyden çevirmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendi hareketiyle geri dönmesi kullanımını kapsamaz.","preserves":"Başkasını belirli bir şeyden geri döndürme işlemini korur."},"facet_ids":["F002"],"text":"onu o işten geri döndürmek","usage_role":"contextual"}],"definition":"Belirli yapı içinde bir kişinin yöneldiği bir şeyden geri dönmesi veya başka birinin onu o şeyden geri döndürmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi yöneldiği veya giriştiği bir şeyden kendi hareketiyle geri döner."},{"facet_id":"F002","role":"core","statement":"Ettirgen kullanımda başka biri kişiyi yöneldiği şeyden geri döndürür."}],"identity_rationale":"Tek kaynak anlatımı, belirli bir yapı içinde kişinin bir şeyden geri dönmesi ile başka birinin onu o şeyden geri döndürmesini açıkça ayırır. Dal, genel geri dönüş anlamına değil bu iki yapıya bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bir şeyden geri dönmek"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"birini bir şeyden geri döndürmek"}],"lexicalization_note":"Tanım çıplak köke genellenmez; bir şeyden geri dönme ve birini o şeyden geri döndürme yapılarıyla sınırlı tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; seçilen ilişkiler yapıya bağlı bu kullanımı genel dönüşten, önceki duruma getirmeden ve uzamsal geri çekilmeden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Katılımcı düzenleri yakındır; odak dal yapısal olarak sınırlı ve tek tanıklı bir kullanımdır, komşu dal ise genel dönüş ve yön değiştirme alanına yayılır.","focus_only":"Odak dal yalnız kanıtlanan özel yapılarda geri dönme ve geri döndürme çiftini taşır.","gloss":"geri dönmek ve döndürmek","neighbor_only":"Komşu dal ayrılıktan sonra dönüşü, başka bir işe yönelmeyi ve geri döndürmeyi daha genel biçimde kapsar.","neighbor_ref":"root_001191/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda kişi önceki yönelişinden ayrılır veya başka biri onu bu yönelişten çevirir."},{"boundary_match":"partial","distinction":"Komşu dal başlangıç yönüne veya önceki duruma dönüşü gerektirir; odak dalda belirleyici olan yönelinen şeyden uzaklaşmadır.","focus_only":"Odak dal bir şeyden vazgeçer gibi geri dönmeyi ve birini ondan çevirmeyi anlatır.","gloss":"geri dönme ve geri getirme","neighbor_only":"Komşu dal bir nesne veya kişiyi başladığı yere ya da önceki durumuna geri getirmeyi kapsar.","neighbor_ref":"root_000544/B001","relation_type":"near_synonym","shared_zone":"İki dal da öznenin geri hareketini ve başka bir katılımcının bu dönüşü sağlamasını kapsayabilir."},{"boundary_match":"partial","distinction":"Komşu dalın uzamsal geri adım görüntüsü güçlüdür; odak dal ise bir işten veya yönelişten dönmeye bağlıdır ve ettirgen biçimi de içerir.","focus_only":"Odak dal geri dönülen şeyden uzaklaşmayı ve ettirgen geri döndürmeyi kapsar.","gloss":"geri dönme ve geri çekilme","neighbor_only":"Komşu dal geri adım atma, arkaya dönme ve ilerledikten sonra gerileme görüntüsünü öne çıkarır.","neighbor_ref":"root_001033/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal önceki ileri yönelişin tersine çevrilmesini veya bırakılmasını anlatabilir."}],"source_phrase_ar":"حكم فلان عن الشيء أي رجع؛ وأحكمته أنا أي رجعته (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu özel kullanım tek kaynakta, geri dönme ve geri döndürme biçimleri birlikte verilerek tanıklanır."}],"source_summary":"Kanıt, aynı özel yapı alanında kendiliğinden geri dönme ile başkasını geri döndürme arasında açık bir katılımcı ayrımı kurar.","sources":["TA"],"what_is_ar":"حكم عن الشيء بمعنى رجع؛ أحكمته بمعنى رجعته","what_is_not_ar":"المنع العام المتعدي؛ القضاء؛ الحكمة العلمية"},"support_links":[]},{"boundary":"Dal, yazı yazma ya da hüküm verme anlamını değil, fiziksel veya toplu birleştirme işlemini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001283/B001","candidate_links":[{"candidate_id":"cand_76ec2154e9f8f4d07002","lane":"macro"},{"candidate_id":"cand_584680d8279eb2f9be35","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"كِتَٰب","morph_features":"STEM|POS:N|LEM:kita`b|ROOT:ktb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:3:2","qac_word_ref":"31:2:3","surface_ar":"كِتَٰبِ"}],"gloss":"bir şeyi başka bir şeye katıp birleştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel işlem, bir şeyi başka bir şeye katarak ikisini bir bütün veya bağlı bir düzen içinde birleştirmektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Deri parçalarını ya da bir su tulumunu dikişle birleştirmek, çekirdeğin el işi alanındaki özel gerçekleşmesidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir hayvanın belirli uzuvlarını halka, kayış veya iple birbirine bağlamak ve bir kabın ağzını sıkıca kapatmak yapıya bağlı kullanımlardır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Atların veya askerlerin toplanıp ayrı ve düzenli bir birlik oluşturması, fiziksel birleştirmeden topluluk düzenine uzanan anlamdır."}},{"facet_id":"F005","role":"example","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Kayışın iki yüzünü bir arada tutan boncuk, ortaya çıkan bağın somut bir örneğidir."}}],"root_ar":"ك ت ب","root_id":"root_001283","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın bütün özel kullanımlarının dayandığı genel birleştirme işlemi için uygundur.","boundary_detail":"Dal, yazı yazma ya da hüküm verme anlamını değil, fiziksel veya toplu birleştirme işlemini kapsar.","branch_image_ar":"ضم شيء إلى شيء","concept_gloss":"bir şeyi başka bir şeye katıp birleştirme","contextual_glosses":[{"applicability":"Deri parçalarının veya su tulumunun dikişle bir araya getirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikiş aracılığıyla gerçekleştirilen birleştirme işlemini tam olarak korur."},"facet_ids":["F002"],"text":"dikerek birleştirmek","usage_role":"contextual"},{"applicability":"Atların veya askerlerin ayrı ve düzenli topluluklar hâlinde toplandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Toplama sonucunda düzenli bir birlik oluşturma anlamını korur."},"facet_ids":["F004"],"text":"birlikler hâlinde düzenlemek","usage_role":"contextual"}],"definition":"Bir şeyi başka bir şeye katıp aralarında fiziksel ya da topluluk oluşturan bir bağ kurmaktır. Derileri dikme, açıklıkları bağlama veya kapatma ve insan ya da atları düzenli bir birlik hâline getirme bunun yapıya bağlı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel işlem, bir şeyi başka bir şeye katarak ikisini bir bütün veya bağlı bir düzen içinde birleştirmektir."},{"facet_id":"F002","role":"specialization","statement":"Deri parçalarını ya da bir su tulumunu dikişle birleştirmek, çekirdeğin el işi alanındaki özel gerçekleşmesidir."},{"facet_id":"F003","role":"specialization","statement":"Bir hayvanın belirli uzuvlarını halka, kayış veya iple birbirine bağlamak ve bir kabın ağzını sıkıca kapatmak yapıya bağlı kullanımlardır."},{"facet_id":"F004","role":"extension","statement":"Atların veya askerlerin toplanıp ayrı ve düzenli bir birlik oluşturması, fiziksel birleştirmeden topluluk düzenine uzanan anlamdır."},{"facet_id":"F005","role":"example","statement":"Kayışın iki yüzünü bir arada tutan boncuk, ortaya çıkan bağın somut bir örneğidir."}],"identity_rationale":"Kaynak ifadesi, anlam çekirdeğini bir şeyi başka bir şeye katıp birleştirmek olarak açıkça kurar; deri dikme, hayvanın bazı uzuvlarını bağlama, boncukla tutturma ve birlik oluşturma kullanımları da bu çekirdeğin özelleşmiş gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi başka bir şeye katıp birleştirme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"su tulumunu dikerek birleştirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"katırın üreme organının dudaklarını halka veya kayışla birleştirmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"dişi devenin burun deliklerini iplikle dikmek veya bağlamak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"dişi devenin memelerini bağlamak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"su tulumunun ağzını bağıyla sıkıca kapatmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kayışın iki yüzünü birleştiren boncuk"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir arada duran atlı veya askerî birlik"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"atların toplanması"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"askerleri birlik birlik düzenlemek"}],"lexicalization_note":"Tanım ortak birleştirme çekirdeğini korur; dikme, bağlama, kapatma ve birlik düzenleme anlamlarını yalnızca tanıklanmış biçim ve yapılara bağlı özelleşmeler olarak verir.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; yayımlanan iki karşılaştırma genel birleştirme ve bağlama sınırındaki en güçlü karışma noktalarını gösterirken diğerleri yalnızca uzak alan veya dal içi çağrışım sundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği yakın olsa da tanıklanmış sınırı belirli dikme, bağlama ve topluluk oluşturma kullanımlarıyla şekillenir; komşu dalın kapsama ve eşlik etme uzantıları odak dalın sınırına girmez.","focus_only":"Odak dalda dikiş, uzuv bağlama, kapatma ve askerî birlik oluşturma gibi kalıplaşmış özel gerçekleşmeler bulunur.","gloss":"katıp birleştirme","neighbor_only":"Komşu dal, eşlik etme ve bir şeyin başka bir şeyi içine alması gibi daha geniş kapsama uzanır.","neighbor_ref":"root_000915/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da ayrı unsurları bir araya getirip bağlı bir bütün oluşturma alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal için bağlama yalnızca birleştirmenin yollarından biridir; komşu dalda ise düğüm ve sıkı bağ kurma işlemin kendisini tanımlar.","focus_only":"Odak dal, katma ve birleştirmenin yanı sıra dikişle birleştirme ve topluluk oluşturmayı kapsar.","gloss":"bağlayarak birleştirme","neighbor_only":"Komşu dalın çekirdeği uçları sıkıca bağlama, düğümleme ve düğüm oluşumudur.","neighbor_ref":"root_001034/B001","relation_type":"near_neighbor","shared_zone":"İki dal, parçaların bir bağ aracılığıyla bir arada tutulduğu fiziksel işlemlerde yaklaşır."}],"source_phrase_ar":"أصل صحيح واحد يدل على جمع شيء إلى شيء (maqayis)؛ أصل الكتب ضمك الشيء إلى الشيء (jamhara)؛ ضم أديم إلى أديم بالخياطة (mufradat)؛ كتبت السقاء إذا خرزته (tahdhib)؛ كتبت البغلة إذا جمعت بين شفريها بحلقة (sihah;mufradat)؛ الكتيبة جماعة مستحيزة (sihah;tahdhib)","source_summary":"Kaynakların ortak çizgisi, katma ve birleştirme çekirdeğinin dikiş, bağlama, sıkıca kapatma ve düzenli topluluk oluşturma gibi somut uygulamalarda korunmasıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه أصل الجمع والضم، وخرز الأديم والسقاء، وضم شفري الدابة أو صر أخلافها، والخرزة المضمومة، واجتماع الخيل أو الكتيبة.","what_is_not_ar":"ليس المراد هنا الكتاب المكتوب، ولا الفرض والحكم، ولا عقد المكاتبة إلا من جهة أصل الجمع."},"support_links":["sup_5712b0b2d10fda67a9c5","sup_8d457ca41ac0b90c1e02"]},{"boundary":"Dal, yazı üretimi ve yazılı ürünle sınırlıdır; yazının bağlayıcı hüküm için mecazlaşması ayrı dalda tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_001283/B002","candidate_links":[{"candidate_id":"cand_76ec2154e9f8f4d07002","lane":"macro"},{"candidate_id":"cand_578b04313f4833efdfe8","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"كِتَٰب","morph_features":"STEM|POS:N|LEM:kita`b|ROOT:ktb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:3:2","qac_word_ref":"31:2:3","surface_ar":"كِتَٰبِ"}],"gloss":"yazma ve yazılı metin","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel işlem, harfleri yazıyla düzenleyip bir metin oluşturmak veya var olan metni kopyalamaktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlemin ürünü, yazılmış metin veya üzerinde bu metnin bulunduğu sayfa ya da kitaptır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir metni başkasına söyleyerek yazdırmak ve birinden kendisi için yazmasını istemek yapıya bağlı ettirgen ve isteme kullanımlarıdır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yazmayı öğretmek, yazı öğretmeni ve öğretim yeri anlamları yazı edinimi alanındaki bağlı kullanımlardır."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Öğretim yerindeki çocuklar veya onların topluluğu için kullanılan biçim, yeri değil öğrencileri gösterir."}}],"root_ar":"ك ت ب","root_id":"root_001283","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem harflerden metin oluşturma işlemini hem de ortaya çıkan yazılı ürünü birlikte temsil eder.","boundary_detail":"Dal, yazı üretimi ve yazılı ürünle sınırlıdır; yazının bağlayıcı hüküm için mecazlaşması ayrı dalda tutulur.","branch_image_ar":"نظم الحروف واسم المكتوب","concept_gloss":"yazma ve yazılı metin","contextual_glosses":[{"applicability":"Bir metnin harflerle oluşturulduğu veya mevcut bir metnin yeniden yazıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yazılı metni üretme veya yeniden oluşturma işlemini eksiksiz korur."},"facet_ids":["F001"],"text":"yazmak veya kopyalamak","usage_role":"contextual"},{"applicability":"Metnin başkasına söylenerek yazıya geçirilmesinin sağlandığı yapıya bağlı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yazı eyleminin başka bir kişiye yaptırılması anlamını korur."},"facet_ids":["F003"],"text":"yazdırmak","usage_role":"contextual"}],"definition":"Harfleri çizgiyle düzenleyerek yazılı bir metin oluşturmak ve bu işlemin ürünü olan metin ya da yazılı sayfadır. Birine yazdırma, ondan yazmasını isteme ve yazmayı öğretme ise belirli yapılara bağlı uzantılardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel işlem, harfleri yazıyla düzenleyip bir metin oluşturmak veya var olan metni kopyalamaktır."},{"facet_id":"F002","role":"extension","statement":"İşlemin ürünü, yazılmış metin veya üzerinde bu metnin bulunduğu sayfa ya da kitaptır."},{"facet_id":"F003","role":"associated_use","statement":"Bir metni başkasına söyleyerek yazdırmak ve birinden kendisi için yazmasını istemek yapıya bağlı ettirgen ve isteme kullanımlarıdır."},{"facet_id":"F004","role":"associated_use","statement":"Yazmayı öğretmek, yazı öğretmeni ve öğretim yeri anlamları yazı edinimi alanındaki bağlı kullanımlardır."},{"facet_id":"F005","role":"source_variant","statement":"Öğretim yerindeki çocuklar veya onların topluluğu için kullanılan biçim, yeri değil öğrencileri gösterir."}],"identity_rationale":"Kaynak ifadesi harfleri çizgiyle düzenleyerek yazma işlemini, bunun ürünü olan yazılı metin veya sayfayı ve yazdırma, isteme ya da öğretme gibi yapıya bağlı kullanımları birlikte tanıklar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kitabı yazmak veya kopyalamak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yazılı metin veya üzerinde yazı bulunan sayfa"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yazma işi ve yazıcılık"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kitabı yazmak veya kopyalamak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ona şiiri söyleyerek yazdırmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birinden kendisi için bir şey yazmasını istemek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"çocuğa yazmayı öğretmek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yazı öğretmeni veya yazı öğretilen yer"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"öğretim yerindeki çocuklar veya onların topluluğu"}],"lexicalization_note":"Yazma işlemi ve yazılı ürün dalın merkezindedir; dikte ettirme, başkasından yazmasını isteme ve yazmayı öğretme anlamları yalnızca ilgili yapılara bağlı olarak korunur.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; seçilen üçü yazı, yazılı nesne ve söyleyerek yazdırma sınırlarını doğrudan aydınlatır, kalanlar ise daha dar nesne türleri veya uzak dal içi ilişkiler sunar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yazma çekirdeğinde güçlü biçimde örtüşürler; odak dal öğretim ve yazdırma yapılarına uzanırken komşu dal kazıma ve taş üzerine işleme alanına uzanır.","focus_only":"Odak dal, kopyalama, yazdırma, yazma isteği ve yazı öğretimiyle ilgili bağlı kullanımları da kapsar.","gloss":"yazı oluşturma","neighbor_only":"Komşu dal, sözün taşa kazınması ve yazıya ek olarak oyma işlemini açıkça kapsar.","neighbor_ref":"root_001633/B003","relation_type":"near_synonym","shared_zone":"İki dal da sözün görünür işaretlerle kayda geçirilmesini ve ortaya çıkan yazılı ürünü kapsar."},{"boundary_match":"field_only","distinction":"Komşu dal nesne türünü tanımlar; odak dal ise nesnenin yanı sıra yazı oluşturma işlemini de kurucu anlam olarak içerir.","focus_only":"Odak dal hem yazma işlemini hem yazılı ürünü ve yazıyla ilgili bağlı eylemleri kapsar.","gloss":"yazılı sayfa","neighbor_only":"Komşu dalın çekirdeği, üzerine yazı yazılan veya yazı taşıyan sayfanın kendisidir.","neighbor_ref":"root_000845/B002","relation_type":"same_field","shared_zone":"Her iki dal yazı taşıyan sayfa veya yazılı ürün alanında buluşur."},{"boundary_match":"partial","distinction":"Söyleme işlemi komşu dalın merkezidir; odak dalda ise yalnızca yazdırmayı sağlayan yapıya bağlı bir kullanım olup yazma eyleminin yerini almaz.","focus_only":"Odak dalın çekirdeği yazıyı fiilen oluşturma ve ortaya çıkan yazılı üründür.","gloss":"söyleyerek yazdırma","neighbor_only":"Komşu dalın çekirdeği, yazılacak sözleri yazara söyleme işlemidir.","neighbor_ref":"root_001447/B003","relation_type":"near_neighbor","shared_zone":"İki dal, bir metnin sözlü aktarım yoluyla yazıya geçirilmesi sürecinde kesişir."}],"source_phrase_ar":"الكتاب والكتابة يقال كتبت الكتاب أكتبه كتبا (maqayis)؛ وقد كتب الكتاب يكتبه كتبا إذا جمع حروفه (jamhara)؛ الكتاب معروف وقد كتبت كتبا وكتابا وكتابة (sihah)؛ كتبت الكتاب كتبا وكتابا فالكتاب اسم لما كتب مجموعا (tahdhib)؛ في التعارف ضم الحروف بعضها إلى بعض بالخط (mufradat)؛ أكتبني هذه القصيدة أي أملها علي (sihah)؛ استكتبه الشيء أي سأله أن يكتبه له (sihah;tahdhib)","source_summary":"Kaynaklar yazmayı harfleri çizgiyle bir araya getiren işlem olarak sunar; yazılı ürün, kopyalama, dikte ettirme, yazma isteği ve öğretimle ilgili kullanımlar bu merkeze bağlanır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه كتب الكتاب وكتابته ونسخه، والكتاب اسما للمكتوب أو الصحيفة ذات الكتابة، والتعليم والإملاء والاستكتاب المتعلق بالكتابة.","what_is_not_ar":"ليس المراد هنا الفرض والحكم والقدر إلا إذا صارت الكتابة كناية عن الإيجاب أو الإثبات، ولا يدخل فيه سهم الصبيان الصغير."},"support_links":["sup_5712b0b2d10fda67a9c5","sup_71229f315fee594210df"]},{"boundary":"Salt yazı yazmak bu dala girmez; belirleme işleminin yükümlülük, hüküm veya yazgı sonucu doğurması gerekir.","branch_kind":"mixed_non_bare","branch_ref":"root_001283/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كِتَٰب","morph_features":"STEM|POS:N|LEM:kita`b|ROOT:ktb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:3:2","qac_word_ref":"31:2:3","surface_ar":"كِتَٰبِ"}],"gloss":"bağlayıcı olarak hükme bağlama ve belirleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işi yapılması gereken bağlayıcı bir yükümlülük olarak belirlemek temel değerlerden biridir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir konuda geçerli ve kesinleşmiş hüküm vermek aynı belirleme çekirdeğinin yargısal yönüdür."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir olayın payını, ölçüsünü veya gelecekte gerçekleşecek sonucunu önceden belirlemek yazgı yönünü oluşturur."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yazma anlatımı, belirlenen hükmün saptanmış, yürürlüğe konmuş ve kesinleşmiş olmasını ifade eder."}}],"root_ar":"ك ت ب","root_id":"root_001283","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yükümlülük, hüküm ve yazgı yönlerini tek bir kesin ve geçerli belirleme çekirdeğinde toplar.","boundary_detail":"Salt yazı yazmak bu dala girmez; belirleme işleminin yükümlülük, hüküm veya yazgı sonucu doğurması gerekir.","branch_image_ar":"إثبات يوجب حكما أو قدرا","concept_gloss":"bağlayıcı olarak hükme bağlama ve belirleme","contextual_glosses":[{"applicability":"Bir eylemin kişilere bağlayıcı yükümlülük olarak yüklendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapılması gereken işi bağlayıcı yükümlülük hâline getirme anlamını korur."},"facet_ids":["F001","F004"],"text":"zorunlu kılmak","usage_role":"contextual"},{"applicability":"Bir olayın gerçekleşmesini veya kişiye düşecek payı önceden belirleme bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gelecekteki olay veya payın önceden karara bağlanması anlamını korur."},"facet_ids":["F003","F004"],"text":"yazgı olarak belirlemek","usage_role":"contextual"}],"definition":"Bir şeyi bağlayıcı bir yükümlülük, hüküm veya gerçekleşmesi belirlenmiş pay ve yazgı olarak karara bağlamaktır. Yazma çağrışımı burada harf çizmekten çok kararın kesinleştirilip geçerli kılınmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işi yapılması gereken bağlayıcı bir yükümlülük olarak belirlemek temel değerlerden biridir."},{"facet_id":"F002","role":"core","statement":"Bir konuda geçerli ve kesinleşmiş hüküm vermek aynı belirleme çekirdeğinin yargısal yönüdür."},{"facet_id":"F003","role":"core","statement":"Bir olayın payını, ölçüsünü veya gelecekte gerçekleşecek sonucunu önceden belirlemek yazgı yönünü oluşturur."},{"facet_id":"F004","role":"associated_use","statement":"Yazma anlatımı, belirlenen hükmün saptanmış, yürürlüğe konmuş ve kesinleşmiş olmasını ifade eder."}],"identity_rationale":"Kaynak ifadesi, bir şeyi yükümlülük, hüküm, paylaştırılmış yazgı veya kesinleşmiş karar olarak belirleme alanını açıkça toplar; burada yazı, harf çizme eylemi değil bağlayıcı biçimde belirlemenin anlatım yoludur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yükümlülük, hüküm veya yazgı"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"size zorunlu kılındı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"Tanrı belirledi, karara bağladı veya zorunlu kıldı"}],"lexicalization_note":"Yükümlülük, hüküm ve yazgı değerleri birlikte korunur; birine zorunluluk yükleme ve Tanrı'nın belirlemesi anlamları yalnızca tanıklanmış yapılara bağlanır.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; seçilenler zorunluluk, kesin hüküm ve karar verme sınırlarındaki gerçek örtüşmeleri gösterir, diğerleri yalnızca kanıt, izin veya konu ortaklığı düzeyinde kalır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kaçınılmaz kesin hükmü merkez alır; odak dal ise aynı ekseni yükümlülük ve yazgı belirleme yönlerine de açar.","focus_only":"Odak dal, zorunluluk ve kesin hükmün yanında pay veya yazgıyı önceden belirlemeyi de kapsar.","gloss":"kesin hükme bağlama","neighbor_only":"Komşu dal, kararın kaçınılmazlığına, sıkıca kesinleştirilmesine ve kişiye yüklenmesine özellikle yoğunlaşır.","neighbor_ref":"root_000292/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir kararın kesin, geçerli ve bağlayıcı hâle getirilmesi alanında güçlü biçimde örtüşür."},{"boundary_match":"partial","distinction":"Yükümlülük bağlamında yaklaşırlar; ancak odak dalın hüküm ve yazgı kapsamı komşuda yoktur, komşunun ödev ve hak odağı da daha dardır.","focus_only":"Odak dal, yükümlülüğe ek olarak hüküm ve önceden belirlenmiş yazgı anlamlarını taşır.","gloss":"zorunlu yükümlülük","neighbor_only":"Komşu dal, özellikle yerine getirilmesi gereken ödev ve vazgeçilmez hak türlerini öne çıkarır.","neighbor_ref":"root_001010/B005","relation_type":"near_synonym","shared_zone":"Her iki dal yapılması gereken işi bağlayıcı bir yükümlülük olarak gösterir."},{"boundary_match":"partial","distinction":"Komşu dal yargılama ve uyuşmazlığı ayırma eylemine dayanır; odak dalda ise bağlayıcı belirleme daha geniş olup bir uyuşmazlık gerektirmez.","focus_only":"Odak dal, hükmün yanında yükümlülük koyma ve olayları önceden belirleme yönlerini içerir.","gloss":"kesin karar verme","neighbor_only":"Komşu dal, taraflar arasında karar verme ve uyuşmazlığı kesin biçimde sonuçlandırma işlemini kapsar.","neighbor_ref":"root_001237/B001","relation_type":"near_neighbor","shared_zone":"İki dal, bir meseleyi geçerli ve kesin bir kararla sonuçlandırma alanında buluşur."}],"source_phrase_ar":"الكتاب وهو الفرض (maqayis)؛ يقال للحكم الكتاب (maqayis)؛ يقال للقدر الكتاب (maqayis)؛ الكتاب الفرض والحكم والقدر (sihah)؛ الكتاب يوضع موضع الفرض (tahdhib)؛ يعبر عن الإثبات والتقدير والإيجاب والفرض والعزم بالكتابة (mufradat)؛ يعبر بالكتابة عن القضاء الممضى (mufradat)","source_summary":"Kaynaklar yükümlülük, hüküm, yazgı, belirleme ve kesinleşmiş karar değerlerini aynı bağlayıcı saptama alanında birleştirir; yazma sözü bu saptamanın anlatım aracıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الكتاب بمعنى الفرض والحكم والقدر، والكتابة بمعنى الإثبات والتقدير والإيجاب والعزم والقضاء الممضى.","what_is_not_ar":"لا يدخل فيه مجرد خط الحروف إلا إذا كان المعنى المنقول هو الإيجاب أو الحكم أو التقدير."},"support_links":[]},{"boundary":"Dal, genel yazma eylemini değil, adı kayda geçirerek kişiyi bir listeye veya belirli topluluğa dâhil etmeyi anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001283/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كِتَٰب","morph_features":"STEM|POS:N|LEM:kita`b|ROOT:ktb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:3:2","qac_word_ref":"31:2:3","surface_ar":"كِتَٰبِ"}],"gloss":"adını sicile yazma veya bir gruba dâhil etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin adını bir kayıt veya listeye geçirerek ona kayıtlı kişi konumu vermek dalın çekirdeğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adı pay, geçim tahsisatı veya yönetim siciline yazdırmak resmî kayıt alanındaki özel gerçekleşmedir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişiyi tanıklar gibi belirli bir topluluğun içinde saymak, sicile almadan üyelik vermeye uzanan kullanımdır."}}],"root_ar":"ك ت ب","root_id":"root_001283","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem resmî sicile alma hem de kişiyi belirli bir topluluğun üyesi sayma anlamlarını kapsar.","boundary_detail":"Dal, genel yazma eylemini değil, adı kayda geçirerek kişiyi bir listeye veya belirli topluluğa dâhil etmeyi anlatır.","branch_image_ar":"إدخال الاسم في سجل أو زمرة","concept_gloss":"adını sicile yazma veya bir gruba dâhil etme","contextual_glosses":[{"applicability":"Kişinin pay, geçim tahsisatı veya yönetim kaydına kendi adını geçirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin adını resmî kayda geçirerek kayıtlı konum kazanması anlamını korur."},"facet_ids":["F001","F002"],"text":"adını sicile yazdırmak","usage_role":"contextual"},{"applicability":"Bir kişinin tanıklar gibi adı belirli bir topluluğun üyesi sayıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye belirli topluluk içinde üyelik ve yer verilmesi anlamını korur."},"facet_ids":["F003"],"text":"aralarına katmak","usage_role":"contextual"}],"definition":"Bir kişinin adını resmî bir pay, geçim veya yönetim kaydına geçirerek onu kayıtlılar arasına almak ya da kişiyi belirli bir topluluğun üyesi saymaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin adını bir kayıt veya listeye geçirerek ona kayıtlı kişi konumu vermek dalın çekirdeğidir."},{"facet_id":"F002","role":"specialization","statement":"Adı pay, geçim tahsisatı veya yönetim siciline yazdırmak resmî kayıt alanındaki özel gerçekleşmedir."},{"facet_id":"F003","role":"extension","statement":"Bir kişiyi tanıklar gibi belirli bir topluluğun içinde saymak, sicile almadan üyelik vermeye uzanan kullanımdır."}],"identity_rationale":"Kaynak ifadesi, bir kişinin adını pay veya geçim kaydına ya da yönetim siciline geçirmek ile kişiyi tanıklar topluluğuna dâhil etmek arasında ortak bir kayıt ve üyelik çekirdeği kurar.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"pay veya geçim tahsisatı için kaydolma"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"adını pay kaydına veya yönetim siciline yazdırmak"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bizi tanıklar topluluğuna kat"}],"lexicalization_note":"Sicile alma ve topluluğa katma çekirdeği korunur; pay kaydı, yönetim sicili ve tanıklar arasına katılma anlamları kendi tanıklanmış yapılarıyla sınırlıdır.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; yayımlanan karşılaştırmalar kayıtla üyelik ile genel katma ve özel aidiyet arasındaki sınırı gösterir, kalan adaylar yalnızca grup veya yazı alanını uzaktan paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırıcı özelliği adın kayda geçirilmesi veya üyelik verilmesidir; komşu dalda kayıt koşulu bulunmaz ve birleştirme kendi başına çekirdektir.","focus_only":"Odak dalda kişinin adı kayda geçirilir ve bunun sonucunda ona resmî veya toplumsal üyelik verilir.","gloss":"bir topluluğa katma","neighbor_only":"Komşu dal, ad kaydı olmadan nesneleri fiziksel olarak veya insanları düzenli topluluk olarak birleştirir.","neighbor_ref":"root_001283/B001","relation_type":"near_neighbor","shared_zone":"İki dal, ayrı bir kişiyi veya unsuru daha büyük bir bütünün içine katma düşüncesinde buluşur."},{"boundary_match":"field_only","distinction":"Odak dal katılma ve kayıt işlemini, komşu dal ise başkalarına kapalı özel aidiyet ve ayrışma durumunu merkez alır.","focus_only":"Odak dal, kişiyi adını kaydederek bir sicile veya topluluğa dâhil etme işlemini anlatır.","gloss":"gruba ait kılma","neighbor_only":"Komşu dal, bir şeyin belirli kişi veya topluluğa özel olmasını ve başkalarından ayrılmasını anlatır.","neighbor_ref":"root_000430/B004","relation_type":"same_field","shared_zone":"Her iki dal kişi veya şeyin belirli bir toplulukla ilişkili konum kazanması alanındadır."}],"source_phrase_ar":"الكتبة الاكتتاب في الفرض والرزق (ayn;tahdhib)؛ اكتتب فلان أي كتب اسمه في الفرض (ayn;tahdhib)؛ اكتتب الرجل إذا كتب نفسه في ديوان السلطان (sihah)؛ فاكتبنا مع الشاهدين أي اجعلنا في زمرتهم (mufradat)","source_summary":"Kaynakların ortak içeriği, adı kayda geçirmenin kişiyi pay alanlar, yönetim sicilindekiler veya belirli bir topluluğun üyeleri arasına sokmasıdır.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الاكتتاب في الفرض والرزق، وكتابة الاسم في ديوان السلطان، ومعنى اجعلنا في زمرة الشاهدين.","what_is_not_ar":"ليس هو مجرد تأليف كتاب، ولا حكم الفرض نفسه، بل إدخال اسم أو شخص في سجل أو جماعة."},"support_links":[]},{"boundary":"Dal, her türlü yazılı sözleşmeyi değil, bedelin ödenmesiyle özgürlüğe götüren bu özel sözleşme türünü kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001283/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كِتَٰب","morph_features":"STEM|POS:N|LEM:kita`b|ROOT:ktb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:3:2","qac_word_ref":"31:2:3","surface_ar":"كِتَٰبِ"}],"gloss":"özgürlük bedelini ödemeye dayalı özgürleşme sözleşmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sahip ile köleleştirilmiş kişi arasında, kişinin kendi özgürlük bedelini ödemesini konu alan özel bir sözleşme kurulur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bedel belirlenmiş ödeme dilimlerine bağlanır ve köleleştirilmiş kişi bunu kendi kazancından karşılar."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kararlaştırılan bedelin tamamlanması sözleşmenin sonucu olarak köleleştirilmiş kişinin özgür olmasını sağlar."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İlgili biçimler sözleşmenin kendisini, sözleşmeye bağlı köleleştirilmiş kişiyi ve bağlama göre sözleşmenin öteki tarafını gösterebilir."}}],"root_ar":"ك ت ب","root_id":"root_001283","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözleşmenin taraflarını, ödeme düzenini ve bedelin tamamlanmasıyla doğan özgürleşme sonucunu birlikte kapsar.","boundary_detail":"Dal, her türlü yazılı sözleşmeyi değil, bedelin ödenmesiyle özgürlüğe götüren bu özel sözleşme türünü kapsar.","branch_image_ar":"مكاتبة العبد على عتقه","concept_gloss":"özgürlük bedelini ödemeye dayalı özgürleşme sözleşmesi","contextual_glosses":[{"applicability":"Köleleştirilmiş kişinin kendi bedelini aşamalı ödeyerek özgürleşmesini açıklayan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin bedeli ödemesi, ödemelerin aşamalı oluşu ve özgürleşme sonucunu korur."},"facet_ids":["F001","F002","F003"],"text":"özgürlüğünü taksitle satın alma sözleşmesi","usage_role":"explanatory"},{"applicability":"Sahibin köleleştirilmiş kişiyle bu özel ödeme ve özgürleşme sözleşmesini kurduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tarafların özgürlük bedelini konu alan özel sözleşmeyi kurması anlamını korur."},"facet_ids":["F001","F004"],"text":"özgürlük bedeli sözleşmesi yapmak","usage_role":"contextual"}],"definition":"Köleleştirilmiş kişinin, belirlenen bedeli kazancından ve kararlaştırılmış ödemelerle sahibine vererek özgürlüğünü kazanması için taraflar arasında yapılan özel sözleşmedir. Bedel tamamlandığında kişi özgür olur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sahip ile köleleştirilmiş kişi arasında, kişinin kendi özgürlük bedelini ödemesini konu alan özel bir sözleşme kurulur."},{"facet_id":"F002","role":"core","statement":"Bedel belirlenmiş ödeme dilimlerine bağlanır ve köleleştirilmiş kişi bunu kendi kazancından karşılar."},{"facet_id":"F003","role":"core","statement":"Kararlaştırılan bedelin tamamlanması sözleşmenin sonucu olarak köleleştirilmiş kişinin özgür olmasını sağlar."},{"facet_id":"F004","role":"associated_use","statement":"İlgili biçimler sözleşmenin kendisini, sözleşmeye bağlı köleleştirilmiş kişiyi ve bağlama göre sözleşmenin öteki tarafını gösterebilir."}],"identity_rationale":"Kaynak ifadesi, köleleştirilmiş kişinin kendi özgürlük bedelini kazancından ve belirlenmiş ödemelerle karşılaması için sahibiyle yaptığı özel sözleşmeyi, taraflarını ve özgürleşme sonucunu açıkça tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kölenin bedelini ödeyerek özgürlüğünü kazanma sözleşmesi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"özgürlük bedeli sözleşmesinin tarafı olan köle; bağlama göre sahibi"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"köleyle özgürlük bedeli ödemesine dayalı sözleşme yapmak"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"kölenin özgürlüğünü satın almak için yaptığı sözleşme"}],"lexicalization_note":"Tanım özel sözleşme türüne bağlı kalır; sözleşmenin adı, tarafı ve sözleşme yapma eylemi ayrı tanıklanmış biçimler olarak korunur ve genel sözleşme anlamına genişletilmez.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; seçilenler sözleşme, bedeli kazanma, özgürleşme sonucu ve ölüm sonrası özgür bırakma arasındaki temel sınırları gösterir, kalanlar yalnızca aynı hukuk alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hukuki ilişkiyi ve ödeme yükümlülüğünü kurar; komşu dal ise bu yükümlülüğü yerine getirmek için gösterilen çalışma ve kazanç sürecidir.","focus_only":"Odak dal, ödeme koşullarını ve özgürleşme sonucunu kuran sözleşmenin kendisini tanımlar.","gloss":"özgürlük bedelini kazanma","neighbor_only":"Komşu dal, köleleştirilmiş kişinin bedeli kazanmak için çalışmasını ve kalan payı tamamlama çabasını tanımlar.","neighbor_ref":"root_000709/B005","relation_type":"near_neighbor","shared_zone":"İki dal aynı özgürlük bedelinin ödenmesi ve kölelikten çıkma sürecinde yer alır."},{"boundary_match":"partial","distinction":"Özgürlük komşu dalın doğrudan çekirdeğidir; odak dalda ise özel bir sözleşme ve bedelin ödenmesiyle ulaşılan sonuçtur.","focus_only":"Odak dal, özgürlüğün ancak kararlaştırılan bedelin sözleşmeye göre ödenmesiyle kazanılmasını içerir.","gloss":"özgürleşme","neighbor_only":"Komşu dal, sözleşme veya bedel koşulu aramadan özgür olma ve kölelikten çıkarılma durumunu kapsar.","neighbor_ref":"root_000306/B002","relation_type":"near_neighbor","shared_zone":"İki dal kölelik durumunun sona ermesi ve kişinin özgürlüğe kavuşması sonucunda buluşur."},{"boundary_match":"field_only","distinction":"Odak dalın koşulu bedelin sözleşmeye göre ödenmesidir; komşu dalın koşulu ise sahibin ölümü olup ödeme sözleşmesi bulunmaz.","focus_only":"Odak dalda özgürleşme, kişinin kazancından yaptığı kararlaştırılmış ödemeleri tamamlamasına bağlıdır.","gloss":"koşula bağlı özgürleşme","neighbor_only":"Komşu dalda özgürleşme, sahibin ölümünden sonra gerçekleşmek üzere önceden verilmiş karara bağlıdır.","neighbor_ref":"root_000458/B007","relation_type":"same_field","shared_zone":"Her iki dal özgürlüğün gelecekteki bir koşul gerçekleşince doğmasını düzenler."}],"source_phrase_ar":"المكاتب العبد يكاتبه سيده على نفسه (maqayis)؛ المكاتب الذي يشتري نفسه ويكاتب عليها (jamhara)؛ المكاتب العبد يكاتب على نفسه بثمنه فإذا سعى وأداه عتق (sihah)؛ معنى الكتاب والمكاتبة أن يكاتب الرجل عبده أو أمته على مال ينجمه عليه (tahdhib)؛ كتابة العبد ابتياع نفسه من سيده بما يؤديه من كسبه (mufradat)","source_summary":"Kaynaklar, özgürlük bedelinin kararlaştırılıp ödemelere bölündüğü, köleleştirilmiş kişinin bunu kazancıyla ödediği ve tamamlandığında özgürleştiği özel sözleşmede birleşir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه عقد المكاتبة بين السيد والعبد أو الأمة على مال منجم، وكتابة الشرط والنجوم المؤدية إلى العتق.","what_is_not_ar":"لا يدخل فيه مطلق الكتابة ولا كل عقد مكتوب، بل هذا الباب الفقهي الخاص بالمكاتب والمكاتبة."},"support_links":[]},{"boundary":"It includes huda and hidayah as right guidance, indication, clarification, showing the road, truth, or religion, becoming guided, divine enabling, and accepting guidance","branch_kind":null,"branch_ref":"root_001583/B001","candidate_links":[{"candidate_id":"cand_76ec2154e9f8f4d07002","lane":"macro"},{"candidate_id":"cand_bd3c2ccee142e3a0015f","lane":"macro"},{"candidate_id":"cand_a9bfcbc21a3b506f08ec","lane":"macro"}],"focus_root_occurrences":[],"gloss":"gentle guidance toward a way or truth","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"دلالة بلطف إلى الطريق والحق","image_en":"gentle guidance toward a way or truth"}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"دلالة بلطف إلى الطريق والحق","image_en":"gentle guidance toward a way or truth","scope_ar":"يدخل فيه الهدى والهداية بمعنى الرشاد والدلالة والبيان وتعريف الطريق أو الحق والدين والاهتداء والتوفيق الإلهي وقبول الهدى","scope_en":"It includes huda and hidayah as right guidance, indication, clarification, showing the road, truth, or religion, becoming guided, divine enabling, and accepting guidance"},"support_links":["sup_5712b0b2d10fda67a9c5","sup_627bc33a8346c850ddd6","sup_c05798d40f82a678d48a"]},{"boundary":"It includes hadi or hadiyah as the first or leading part of something, such as horses' necks or first troop, the first of wild animals, the sheep's neck, an arrowhead, or a staff or guide when they go ahead","branch_kind":null,"branch_ref":"root_001583/B003","candidate_links":[{"candidate_id":"cand_76ec2154e9f8f4d07002","lane":"macro"}],"focus_root_occurrences":[],"gloss":"the leading front part","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"المتقدم الهادي وأوائل الشيء","image_en":"the leading front part"}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"المتقدم الهادي وأوائل الشيء","image_en":"the leading front part","scope_ar":"يدخل فيه الهادي أو الهادية بمعنى أول الشيء وما تقدم منه كأعناق الخيل وأول رعيلها وأوائل الوحش ورقبة الشاة ونصل السهم والعصا أو الدليل حين يتقدمان","scope_en":"It includes hadi or hadiyah as the first or leading part of something, such as horses' necks or first troop, the first of wild animals, the sheep's neck, an arrowhead, or a staff or guide when they go ahead"},"support_links":["sup_5712b0b2d10fda67a9c5"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000083/B001","candidate_links":[{"candidate_id":"cand_584680d8279eb2f9be35","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ed0ab0cc0a0db497bfdd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Dispersion supplies distributed population of the system.","root":"ب ث ث","source_ref":"31:10","source_word_indices":["13"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000083","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8d457ca41ac0b90c1e02"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000186/B001","candidate_links":[{"candidate_id":"cand_578b04313f4833efdfe8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_160a2d5c757e54b05213","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"One item following another supplies temporal delivery of the book's signs.","root":"ت ل و","source_ref":"31:7","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000186","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_71229f315fee594210df"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000299/B003","candidate_links":[{"candidate_id":"cand_578b04313f4833efdfe8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_160a2d5c757e54b05213","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Freshly renewed talk supplies the rival channel's recurrent novelty.","root":"ح د ث","source_ref":"31:6","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000299","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_71229f315fee594210df"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000434/B001","candidate_links":[{"candidate_id":"cand_584680d8279eb2f9be35","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ed0ab0cc0a0db497bfdd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Measurement and proportion supply the specification step.","root":"خ ل ق","source_ref":"31:10","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000434","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8d457ca41ac0b90c1e02"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000552/B001","candidate_links":[{"candidate_id":"cand_bd3c2ccee142e3a0015f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_5c9de4d9121554d3f328","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Tender concern supplies the beneficial aim of the correction.","root":"ر ح م","source_ref":"31:3","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000552","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_627bc33a8346c850ddd6"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000564/B001","candidate_links":[{"candidate_id":"cand_584680d8279eb2f9be35","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ed0ab0cc0a0db497bfdd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Fixing something in place supplies stabilization.","root":"ر س و","source_ref":"31:10","source_word_indices":["9"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000564","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8d457ca41ac0b90c1e02"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000741/B003","candidate_links":[{"candidate_id":"cand_578b04313f4833efdfe8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_160a2d5c757e54b05213","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Hearing as understanding and compliance identifies the blocked downstream function.","root":"س م ع","source_ref":"31:7","source_word_indices":["9"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000741","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_71229f315fee594210df"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001043/B002","candidate_links":[{"candidate_id":"cand_584680d8279eb2f9be35","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ed0ab0cc0a0db497bfdd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Load-bearing support supplies the otherwise unseen structural problem.","root":"ع م د","source_ref":"31:10","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001043","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8d457ca41ac0b90c1e02"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001273/B008","candidate_links":[{"candidate_id":"cand_bd3c2ccee142e3a0015f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_5c9de4d9121554d3f328","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Restoring balance and uprightness supplies the practiced adjustment.","root":"ق و م","source_ref":"31:4","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001273","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_627bc33a8346c850ddd6"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001382/B001","candidate_links":[{"candidate_id":"cand_578b04313f4833efdfe8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_160a2d5c757e54b05213","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Being occupied by a substitute supplies the rival attention channel.","root":"ل ه و","source_ref":"31:6","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001382","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_71229f315fee594210df"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001459/B001","candidate_links":[{"candidate_id":"cand_584680d8279eb2f9be35","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ed0ab0cc0a0db497bfdd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Swaying and instability specify what the stabilizer prevents.","root":"م ي د","source_ref":"31:10","source_word_indices":["11"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001459","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8d457ca41ac0b90c1e02"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001465/B001","candidate_links":[{"candidate_id":"cand_584680d8279eb2f9be35","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ed0ab0cc0a0db497bfdd","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Emergence from the ground supplies productive output after delivery of water.","root":"ن ب ت","source_ref":"31:10","source_word_indices":["22"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001465","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_8d457ca41ac0b90c1e02"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001580/B001","candidate_links":[{"candidate_id":"cand_a9bfcbc21a3b506f08ec","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_be13de2c048164ba3713","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Forceful breaking supplies an alternative mode that disrupts a resistant structure.","root":"ه د ي","source_ref":"31:3","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001580","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_c05798d40f82a678d48a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001580/B006","candidate_links":[{"candidate_id":"cand_a9bfcbc21a3b506f08ec","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_be13de2c048164ba3713","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Rhythmic calming of a child supplies the opposite mode, lowering resistance to reception.","root":"ه د ي","source_ref":"31:3","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001580","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_c05798d40f82a678d48a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001674/B001","candidate_links":[{"candidate_id":"cand_578b04313f4833efdfe8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_160a2d5c757e54b05213","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Imagined auditory weight materializes the self-imposed blockage.","root":"و ق ر","source_ref":"31:7","source_word_indices":["13"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001674","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_71229f315fee594210df"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001684/B007","candidate_links":[{"candidate_id":"cand_578b04313f4833efdfe8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_160a2d5c757e54b05213","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Deliberate turning away supplies an active break in reception.","root":"و ل ي","source_ref":"31:7","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001684","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_71229f315fee594210df"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001696/B001","candidate_links":[{"candidate_id":"cand_bd3c2ccee142e3a0015f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_5c9de4d9121554d3f328","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Knowledge becoming stable and doubt receding supplies the feedback outcome.","root":"ي ق ن","source_ref":"31:4","source_word_indices":["9"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001696","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_627bc33a8346c850ddd6"]}],"candidate_inventory":[{"anchor_refs":["31:2","31:3","31:5"],"branch_refs":["root_000348/B001","root_000348/B004","root_001283/B001","root_001283/B002","root_001583/B001","root_001583/B003"],"candidate_id":"cand_76ec2154e9f8f4d07002","commentary_obligation":"review","focus_branch_refs":["root_000348/B001","root_000348/B004","root_001283/B001","root_001283/B002"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001583/B001","root_001583/B003"],"root_ids":[],"scope":"pericope","source_local_id":"A:Braced Text Leads the Route","source_type":"channel","support_ids":["sup_138d5130154740384625","sup_2b0b3dd40c13db61efcf","sup_2e665a4464d1c156b75d","sup_559dbcaa45e7d3612d6d","sup_5712b0b2d10fda67a9c5"],"title":"Braced Text Leads the Route","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["31:2","31:3","31:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"31:2","branch_refs":["root_000348/B001","root_000552/B001","root_001273/B008","root_001583/B001","root_001696/B001"],"candidate_id":"cand_bd3c2ccee142e3a0015f","commentary_obligation":"review","hft_ref":"hft_5c9de4d9121554d3f328","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_guidance_feedback","source_type":"hft","support_ids":["sup_627bc33a8346c850ddd6"],"title":"d_guidance_feedback","trust":"legacy_unbound"},{"anchor_refs":["31:2","31:6","31:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"31:2","branch_refs":["root_000074/B003","root_000186/B001","root_000299/B003","root_000741/B003","root_001283/B002","root_001382/B001","root_001674/B001","root_001684/B007"],"candidate_id":"cand_578b04313f4833efdfe8","commentary_obligation":"review","hft_ref":"hft_160a2d5c757e54b05213","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_competing_transmission","source_type":"hft","support_ids":["sup_71229f315fee594210df"],"title":"d_competing_transmission","trust":"legacy_unbound"},{"anchor_refs":["31:10","31:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"31:2","branch_refs":["root_000083/B001","root_000348/B004","root_000434/B001","root_000564/B001","root_001043/B002","root_001283/B001","root_001459/B001","root_001465/B001"],"candidate_id":"cand_584680d8279eb2f9be35","commentary_obligation":"review","hft_ref":"hft_ed0ab0cc0a0db497bfdd","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_cosmic_control_spec","source_type":"hft","support_ids":["sup_8d457ca41ac0b90c1e02"],"title":"d_cosmic_control_spec","trust":"legacy_unbound"},{"anchor_refs":["31:2","31:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"31:2","branch_refs":["root_000348/B001","root_001580/B001","root_001580/B006","root_001583/B001"],"candidate_id":"cand_a9bfcbc21a3b506f08ec","commentary_obligation":"review","hft_ref":"hft_be13de2c048164ba3713","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_split_guidance_modulation","source_type":"hft","support_ids":["sup_c05798d40f82a678d48a"],"title":"o_split_guidance_modulation","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_2d2ffb6fe22add050584","connection_ref":"conn_17391fbdf764dae42758","note":"The immediate continuation gives the wise Book's signs their function as guidance and mercy for those who do good.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_4761669de561f6a95a46","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"31:3","source_note":"The immediately preceding verse identifies the source of this guidance and mercy as the wise Book.","source_row_role":"ranked_review","source_target_component_ref":"31:2","source_target_components":["31:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"31:2"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"31:3","source_target_components":["31:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"31:3","target_evidence":{"arabic_uthmani":"هُدًۭى وَرَحْمَةًۭ لِّلْمُحْسِنِينَ","ayah_ref":"31:3"},"target_ref":"31:3"},{"connection_evidence_ref":"conn_ev_9b1cd3d489156a991a2d","connection_ref":"conn_bcd07fd7598932820ba3","note":"It supplies the local outcome of the preceding guidance: firm direction and success.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_6903ee378b939f6fd965","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"31:5","source_note":"The immediately preceding ayah introduces the wise Book whose guidance the focus states.","source_row_role":"ranked_review","source_target_component_ref":"31:2","source_target_components":["31:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"31:2"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"31:5","source_target_components":["31:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"31:5","target_evidence":{"arabic_uthmani":"أُو۟لَٰٓئِكَ عَلَىٰ هُدًۭى مِّن رَّبِّهِمْ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ","ayah_ref":"31:5"},"target_ref":"31:5"},{"connection_evidence_ref":"conn_ev_05a7fbcf796e98e3d0be","connection_ref":"conn_b7452df5b07c1f38645c","note":"The immediate description of prayer, almsgiving, and certainty identifies the conduct of those guided by the Book.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_85430481a515b5659271","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"31:4","source_note":"The nearby description of the wise Book frames the qualities unfolded in the following verses.","source_row_role":"ranked_review","source_target_component_ref":"31:2","source_target_components":["31:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"31:2"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"31:4","source_target_components":["31:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"31:4","target_evidence":{"arabic_uthmani":"ٱلَّذِينَ يُقِيمُونَ ٱلصَّلَوٰةَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَهُم بِٱلْءَاخِرَةِ هُمْ يُوقِنُونَ","ayah_ref":"31:4"},"target_ref":"31:4"},{"connection_evidence_ref":"conn_ev_9df052223856157f0481","connection_ref":"conn_a2e7ae62fda949dc2677","note":"The local promise to believers who act rightly follows the passage but does not itself elucidate the wise Book.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_da3e1eed2fb39aac672e","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"31:8","source_note":"The wise Book is local framing but does not itself clarify the promise in the focus.","source_row_role":"ranked_review","source_target_component_ref":"31:2","source_target_components":["31:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"31:2"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"31:8","source_target_components":["31:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"31:8","target_evidence":{"arabic_uthmani":"إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُمْ جَنَّٰتُ ٱلنَّعِيمِ","ayah_ref":"31:8"},"target_ref":"31:8"},{"connection_evidence_ref":"conn_ev_4282d2ed5540bfe3872f","connection_ref":"conn_3f871a8dcfcac1850c86","note":"The local true promise is sealed by the Mighty, Wise attributes, extending the authority introduced in the focus.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_9a38037a339460dc704d","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"31:9","source_note":"The local description of the Book as wise gives only a broad backdrop for the focus's wisdom.","source_row_role":"ranked_review","source_target_component_ref":"31:2","source_target_components":["31:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"31:2"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"31:9","source_target_components":["31:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"31:9","target_evidence":{"arabic_uthmani":"خَٰلِدِينَ فِيهَا ۖ وَعْدَ ٱللَّهِ حَقًّۭا ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ","ayah_ref":"31:9"},"target_ref":"31:9"},{"connection_evidence_ref":"conn_ev_4bc46eb5346873a51474","connection_ref":"conn_49b8521d4c5fc58210e2","note":"The immediate warning against turning away from recited signs directly supplies the focus's rejected-reception counterpart.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_788f318e1ca5cdb6918d","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"31:7","source_note":"The nearby designation of the Book as wise provides only minimal context for the signs recited in the focus.","source_row_role":"ranked_review","source_target_component_ref":"31:2","source_target_components":["31:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"31:2"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"31:7","source_target_components":["31:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"31:7","target_evidence":{"arabic_uthmani":"وَإِذَا تُتْلَىٰ عَلَيْهِ ءَايَٰتُنَا وَلَّىٰ مُسْتَكْبِرًۭا كَأَن لَّمْ يَسْمَعْهَا كَأَنَّ فِىٓ أُذُنَيْهِ وَقْرًۭا ۖ فَبَشِّرْهُ بِعَذَابٍ أَلِيمٍ","ayah_ref":"31:7"},"target_ref":"31:7"},{"connection_evidence_ref":"conn_ev_1d7c011fd3b1271f4b79","connection_ref":"conn_bc3ae0334a095c3a6eca","note":"The immediate contrast between distracting speech that misleads without knowledge and the preceding wise Book directly clarifies its guiding authority.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"31:6","source_target_components":["31:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"31:6","target_evidence":{"arabic_uthmani":"وَمِنَ ٱلنَّاسِ مَن يَشْتَرِى لَهْوَ ٱلْحَدِيثِ لِيُضِلَّ عَن سَبِيلِ ٱللَّهِ بِغَيْرِ عِلْمٍۢ وَيَتَّخِذَهَا هُزُوًا ۚ أُو۟لَٰٓئِكَ لَهُمْ عَذَابٌۭ مُّهِينٌۭ","ayah_ref":"31:6"},"target_ref":"31:6"}],"focus":{"arabic_uthmani":"تِلْكَ ءَايَٰتُ ٱلْكِتَٰبِ ٱلْحَكِيمِ","qac_morphemes":[{"lemma_ar":"ذَٰلِك","morph_features":"STEM|POS:DEM|LEM:*a`lik|FS","morpheme_role":"STEM","pos":"DEM","qac_ref":"31:2:1:1","qac_word_ref":"31:2:1","root_ar":"","surface_ar":"تِلْكَ"},{"lemma_ar":"ءَايَة","morph_features":"STEM|POS:N|LEM:'aAyap|ROOT:Ayy|FP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:2:1","qac_word_ref":"31:2:2","root_ar":"ء ي ي","surface_ar":"ءَايَٰتُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"31:2:3:1","qac_word_ref":"31:2:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"كِتَٰب","morph_features":"STEM|POS:N|LEM:kita`b|ROOT:ktb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:3:2","qac_word_ref":"31:2:3","root_ar":"ك ت ب","surface_ar":"كِتَٰبِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"31:2:4:1","qac_word_ref":"31:2:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"حَكِيم","morph_features":"STEM|POS:ADJ|LEM:Hakiym|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"31:2:4:2","qac_word_ref":"31:2:4","root_ar":"ح ك م","surface_ar":"حَكِيمِ"}],"word_analysis_qac_refs":[["31:2:1:1"],["31:2:2:1"],["31:2:3:1","31:2:3:2"],["31:2:4:1","31:2:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["31:2:1","31:2:2","31:2:3","31:2:4"]},"focus_surface_evidence":{"arabic_uthmani":"تِلْكَ ءَايَٰتُ ٱلْكِتَٰبِ ٱلْحَكِيمِ","qac_morphemes":[{"lemma_ar":"ذَٰلِك","morph_features":"STEM|POS:DEM|LEM:*a`lik|FS","morpheme_role":"STEM","pos":"DEM","qac_ref":"31:2:1:1","qac_word_ref":"31:2:1","root_ar":"","surface_ar":"تِلْكَ"},{"lemma_ar":"ءَايَة","morph_features":"STEM|POS:N|LEM:'aAyap|ROOT:Ayy|FP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:2:1","qac_word_ref":"31:2:2","root_ar":"ء ي ي","surface_ar":"ءَايَٰتُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"31:2:3:1","qac_word_ref":"31:2:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"كِتَٰب","morph_features":"STEM|POS:N|LEM:kita`b|ROOT:ktb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"31:2:3:2","qac_word_ref":"31:2:3","root_ar":"ك ت ب","surface_ar":"كِتَٰبِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"31:2:4:1","qac_word_ref":"31:2:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"حَكِيم","morph_features":"STEM|POS:ADJ|LEM:Hakiym|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"31:2:4:2","qac_word_ref":"31:2:4","root_ar":"ح ك م","surface_ar":"حَكِيمِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["31:2:1:1"],["31:2:2:1"],["31:2:3:1","31:2:3:2"],["31:2:4:1","31:2:4:2"]],"word_analysis_refs":["31:2:1","31:2:2","31:2:3","31:2:4"],"word_rows":[{"analysis_record_ref":"31:2:1","analytic_gloss_range_en":"distal feminine singular demonstrative resolved by the following nonhuman plural predicate and also usable as a boundary pointer","analytic_root_gloss_range_en":null,"qac_refs":["31:2:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"تِلْكَ","transliteration":"tilka"}},{"analysis_record_ref":"31:2:2","analytic_gloss_range_en":"textual signs or verses in construct with the book; sign, proof, and orientation pressures remain active under the local book frame","analytic_root_gloss_range_en":"QAC supplies the sign root, while V4 has no guardrail rows for this root; CRITICAL derivational disputes are therefore kept where locally coherent","qac_refs":["31:2:2:1"],"root":{"arabic":"أ ي ي","transliteration":"ʾ-y-y"},"surface":{"arabic":"ءَايَٰتُ","transliteration":"āyātu"}},{"analysis_record_ref":"31:2:3","analytic_gloss_range_en":"the definite book as genitive complement of the signs and as the textual whole qualified by wise","analytic_root_gloss_range_en":"joining and writing branches are locally relevant to bookhood; decree and binding pressure can color the noun, while contract/register side branches remain secondary unless tied to the book frame","qac_refs":["31:2:3:1","31:2:3:2"],"root":{"arabic":"ك ت ب","transliteration":"k-t-b"},"surface":{"arabic":"ٱلْكِتَٰبِ","transliteration":"al-kitābi"}},{"analysis_record_ref":"31:2:4","analytic_gloss_range_en":"wise, governing, firmly composed, and restraining as a definite adjective of the book","analytic_root_gloss_range_en":"accepted branches include restraining, adjudication, wisdom, firmness, and bridle imagery; local adjective attachment selects wise/governing book-quality and narrows side branches into metaphorical ordering","qac_refs":["31:2:4:1","31:2:4:2"],"root":{"arabic":"ح ك م","transliteration":"ḥ-k-m"},"surface":{"arabic":"ٱلْحَكِيمِ","transliteration":"al-ḥakīmi"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":6,"missing_anchor_refs":[],"supplied_unique_anchor_count":6},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["31:2","31:3","31:4"],"branch_refs":["root_000348/B001","root_000552/B001","root_001273/B008","root_001583/B001","root_001696/B001"],"candidate_id":"cand_bd3c2ccee142e3a0015f","evidence_scope":"declared_pericope","hft_ref":"hft_5c9de4d9121554d3f328","item_id":"d_guidance_feedback","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_guidance_feedback","support_id":"sup_627bc33a8346c850ddd6"},{"anchor_refs":["31:2","31:6","31:7"],"branch_refs":["root_000074/B003","root_000186/B001","root_000299/B003","root_000741/B003","root_001283/B002","root_001382/B001","root_001674/B001","root_001684/B007"],"candidate_id":"cand_578b04313f4833efdfe8","evidence_scope":"declared_pericope","hft_ref":"hft_160a2d5c757e54b05213","item_id":"d_competing_transmission","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_competing_transmission","support_id":"sup_71229f315fee594210df"},{"anchor_refs":["31:10","31:2"],"branch_refs":["root_000083/B001","root_000348/B004","root_000434/B001","root_000564/B001","root_001043/B002","root_001283/B001","root_001459/B001","root_001465/B001"],"candidate_id":"cand_584680d8279eb2f9be35","evidence_scope":"declared_pericope","hft_ref":"hft_ed0ab0cc0a0db497bfdd","item_id":"d_cosmic_control_spec","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_cosmic_control_spec","support_id":"sup_8d457ca41ac0b90c1e02"},{"anchor_refs":["31:2","31:3"],"branch_refs":["root_000348/B001","root_001580/B001","root_001580/B006","root_001583/B001"],"candidate_id":"cand_a9bfcbc21a3b506f08ec","evidence_scope":"declared_pericope","hft_ref":"hft_be13de2c048164ba3713","item_id":"o_split_guidance_modulation","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_split_guidance_modulation","support_id":"sup_c05798d40f82a678d48a"}],"diagnostics":[],"lane_counts":{"global":17,"macro":4,"micro":3},"packet_summary":{"ayah_count":34,"focus_ref":"31:2","protocol":"focus-trace-pericope-lean-v1","split_root_mappings":[],"window":["31:1","31:2","31:3","31:4","31:5","31:6","31:7","31:8","31:9","31:10","31:11","31:12","31:13","31:14","31:15","31:16","31:17","31:18","31:19","31:20","31:21","31:22","31:23","31:24","31:25","31:26","31:27","31:28","31:29","31:30","31:31","31:32","31:33","31:34"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"31:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"31:2","lane":"macro","linguistic_source_ref":"31:2","surface_ref":"31:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"31:2","target_tokens":[["Bunlar",["31:2:1"]],["hikmetli",["31:2:4"]],["kitabın",["31:2:3"]],["ayetleridir",["31:2:2"]]],"text":"Bunlar hikmetli kitabın ayetleridir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":11,"id":"s031-p01-001-011","label":"Wisdom, guidance, and creation signs","number":1,"refs":["31:1","31:2","31:3","31:4","31:5","31:6","31:7","31:8","31:9","31:10","31:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"31:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"31:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["31:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"31:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Braced Text Leads the Route","source_type":"channel","support_id":"sup_138d5130154740384625","text":"Guidance becomes durable by joining, restraining, maintaining, and cultivating rather than by merely transmitting information.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Braced Text Leads the Route","source_type":"channel","support_id":"sup_2b0b3dd40c13db61efcf","text":"A written object is joined and made firm, then functions as a gentle guide and a leading edge on a route.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Braced Text Leads the Route","source_type":"channel","support_id":"sup_2e665a4464d1c156b75d","text":"31:2 كِتَٰبِ (ك ت ب) and حَكِيمِ (ح ك م); 31:3 and 31:5 هُدًى (ه د ي).","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Braced Text Leads the Route","source_type":"channel","support_id":"sup_559dbcaa45e7d3612d6d","text":"The book is not only writing: its root imagery joins separate pieces, while wisdom restrains disorder and brings the construction to firmness. Guidance then extends that fitted object into motion, both indicating the road gently and taking the forward position that lets others follow.","trust":"trusted"},{"branch_refs":["root_000348/B001","root_000348/B004","root_001283/B001","root_001283/B002","root_001583/B001","root_001583/B003"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Braced Text Leads the Route","source_type":"channel","support_id":"sup_5712b0b2d10fda67a9c5","text":"joining or stitching material `quranic:root_001283:B001/m01`; written text `quranic:root_001283:B002/m01`; restraint for correction `quranic:root_000348:B001/m01`; secure workmanship `quranic:root_000348:B004/m01`; gentle route guidance `quranic:root_001583:B001/m01`; leading vanguard `quranic:root_001583:B003/m01`.","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"تِلْكَ ءَايَٰتُ ٱلْكِتَٰبِ ٱلْحَكِيمِ","ayah_ref":"31:2"},{"arabic_uthmani":"هُدًۭى وَرَحْمَةًۭ لِّلْمُحْسِنِينَ","ayah_ref":"31:3"},{"arabic_uthmani":"ٱلَّذِينَ يُقِيمُونَ ٱلصَّلَوٰةَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَهُم بِٱلْءَاخِرَةِ هُمْ يُوقِنُونَ","ayah_ref":"31:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000348/B001","root_000552/B001","root_001273/B008","root_001583/B001","root_001696/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000348","role":"Corrective restraint supplies the regulating action at the focus.","root":"ح ك م","source_ref":"31:2","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001583","role":"Gentle wayfinding turns regulation into directed correction.","root":"ه د ي","source_ref":"31:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000552","role":"Tender concern supplies the beneficial aim of the correction.","root":"ر ح م","source_ref":"31:3","source_word_indices":["2"]},{"branch_id":"B008","mapped_root_id":"root_001273","role":"Restoring balance and uprightness supplies the practiced adjustment.","root":"ق و م","source_ref":"31:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001696","role":"Knowledge becoming stable and doubt receding supplies the feedback outcome.","root":"ي ق ن","source_ref":"31:4","source_word_indices":["9"]}],"changed_reading":{"after":"Its binding force is calibrated guidance: it repairs orientation through practice until understanding settles.","before":"The binding book mainly restrains misconduct."},"confidence":"strong","mechanism":"The book's restraint becomes a beneficent feedback process: it gently orients, sets conduct upright, and yields settled cognition.","model_id":"d_guidance_feedback","reader_inference":"The packet supplies direction, care, upright establishment, and certainty; I infer a loop from sign to practice to stable orientation. They could instead be reader-effects without describing the book's own mechanism.","status":"revised","structural_cues":["31:3 predicates guidance and mercy immediately after the focus, while 31:4-5 move through repeated practices to an announced outcome."],"trigger_roots":["ه د ي","ر ح م","ق و م","ي ق ن"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_guidance_feedback","source_type":"hft","support_id":"sup_627bc33a8346c850ddd6","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"تِلْكَ ءَايَٰتُ ٱلْكِتَٰبِ ٱلْحَكِيمِ","ayah_ref":"31:2"},{"arabic_uthmani":"وَمِنَ ٱلنَّاسِ مَن يَشْتَرِى لَهْوَ ٱلْحَدِيثِ لِيُضِلَّ عَن سَبِيلِ ٱللَّهِ بِغَيْرِ عِلْمٍۢ وَيَتَّخِذَهَا هُزُوًا ۚ أُو۟لَٰٓئِكَ لَهُمْ عَذَابٌۭ مُّهِينٌۭ","ayah_ref":"31:6"},{"arabic_uthmani":"وَإِذَا تُتْلَىٰ عَلَيْهِ ءَايَٰتُنَا وَلَّىٰ مُسْتَكْبِرًۭا كَأَن لَّمْ يَسْمَعْهَا كَأَنَّ فِىٓ أُذُنَيْهِ وَقْرًۭا ۖ فَبَشِّرْهُ بِعَذَابٍ أَلِيمٍ","ayah_ref":"31:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000074/B003","root_000186/B001","root_000299/B003","root_000741/B003","root_001283/B002","root_001382/B001","root_001674/B001","root_001684/B007"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001283","role":"Organized writing supplies the stable message that later enters recitation.","root":"ك ت ب","source_ref":"31:2","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001382","role":"Being occupied by a substitute supplies the rival attention channel.","root":"ل ه و","source_ref":"31:6","source_word_indices":["5"]},{"branch_id":"B003","mapped_root_id":"root_000299","role":"Freshly renewed talk supplies the rival channel's recurrent novelty.","root":"ح د ث","source_ref":"31:6","source_word_indices":["6"]},{"branch_id":"B001","mapped_root_id":"root_000186","role":"One item following another supplies temporal delivery of the book's signs.","root":"ت ل و","source_ref":"31:7","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000074","role":"The repeated manifest marks identify what is being delivered in sequence.","root":"ء ي ي","source_ref":"31:7","source_word_indices":["4"]},{"branch_id":"B007","mapped_root_id":"root_001684","role":"Deliberate turning away supplies an active break in reception.","root":"و ل ي","source_ref":"31:7","source_word_indices":["5"]},{"branch_id":"B003","mapped_root_id":"root_000741","role":"Hearing as understanding and compliance identifies the blocked downstream function.","root":"س م ع","source_ref":"31:7","source_word_indices":["9"]},{"branch_id":"B001","mapped_root_id":"root_001674","role":"Imagined auditory weight materializes the self-imposed blockage.","root":"و ق ر","source_ref":"31:7","source_word_indices":["13"]}],"changed_reading":{"after":"They are a live transmission whose efficacy depends on attention, sequencing, and willingness to let hearing become response.","before":"The signs are stable propositions stored in a book."},"confidence":"strong","mechanism":"The written signs enter time as sequenced recitation and compete with purchased novelty for attention; rejection occurs by interrupting the path from hearing to compliance.","model_id":"d_competing_transmission","reader_inference":"The packet supplies two transmissions, sequential delivery, turning, and obstructed understanding; I infer competition for an attention-to-action channel. The contrast could be ethical rather than a model of reception.","status":"new","structural_cues":["31:6 sets acquired distracting discourse against 31:7's recited signs; the repeated 'as if' marks simulated non-hearing rather than absent sound."],"trigger_roots":["ل ه و","ح د ث","ت ل و","ء ي ي","و ل ي","س م ع","و ق ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_competing_transmission","source_type":"hft","support_id":"sup_71229f315fee594210df","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"خَلَقَ ٱلسَّمَٰوَٰتِ بِغَيْرِ عَمَدٍۢ تَرَوْنَهَا ۖ وَأَلْقَىٰ فِى ٱلْأَرْضِ رَوَٰسِىَ أَن تَمِيدَ بِكُمْ وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ ۚ وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَنۢبَتْنَا فِيهَا مِن كُلِّ زَوْجٍۢ كَرِيمٍ","ayah_ref":"31:10"},{"arabic_uthmani":"تِلْكَ ءَايَٰتُ ٱلْكِتَٰبِ ٱلْحَكِيمِ","ayah_ref":"31:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000083/B001","root_000348/B004","root_000434/B001","root_000564/B001","root_001043/B002","root_001283/B001","root_001459/B001","root_001465/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001283","role":"Joining supplies the architecture that relates distinct operations.","root":"ك ت ب","source_ref":"31:2","source_word_indices":["3"]},{"branch_id":"B004","mapped_root_id":"root_000348","role":"Firm finishing supplies system integrity at the focus.","root":"ح ك م","source_ref":"31:2","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000434","role":"Measurement and proportion supply the specification step.","root":"خ ل ق","source_ref":"31:10","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001043","role":"Load-bearing support supplies the otherwise unseen structural problem.","root":"ع م د","source_ref":"31:10","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000564","role":"Fixing something in place supplies stabilization.","root":"ر س و","source_ref":"31:10","source_word_indices":["9"]},{"branch_id":"B001","mapped_root_id":"root_001459","role":"Swaying and instability specify what the stabilizer prevents.","root":"م ي د","source_ref":"31:10","source_word_indices":["11"]},{"branch_id":"B001","mapped_root_id":"root_000083","role":"Dispersion supplies distributed population of the system.","root":"ب ث ث","source_ref":"31:10","source_word_indices":["13"]},{"branch_id":"B001","mapped_root_id":"root_001465","role":"Emergence from the ground supplies productive output after delivery of water.","root":"ن ب ت","source_ref":"31:10","source_word_indices":["22"]}],"changed_reading":{"after":"Its coherence becomes a control diagram for reading measured creation: supports, anchors, flows, populations, and growth form one governed order.","before":"The book is coherent because its textual units are well joined."},"confidence":"strong","mechanism":"Measured formation, support, anchoring against oscillation, distribution, and growth instantiate the focus model at world-scale: many operations cohere as one stabilized specification.","model_id":"d_cosmic_control_spec","reader_inference":"The packet supplies measured parts, failure mode, stabilizer, distribution, and output; I infer a control architecture and read it back into the assembled book. The context may only offer evidence of a maker, not identify creation with a book.","status":"strengthened","structural_cues":["31:10 explicitly links the anchors to prevention of swaying, then sequences scattering, descent, and growth; 31:11 turns the result into a demonstrative challenge."],"trigger_roots":["خ ل ق","ع م د","ر س و","م ي د","ب ث ث","ن ب ت"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_cosmic_control_spec","source_type":"hft","support_id":"sup_8d457ca41ac0b90c1e02","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"تِلْكَ ءَايَٰتُ ٱلْكِتَٰبِ ٱلْحَكِيمِ","ayah_ref":"31:2"},{"arabic_uthmani":"هُدًۭى وَرَحْمَةًۭ لِّلْمُحْسِنِينَ","ayah_ref":"31:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000348/B001","root_001580/B001","root_001580/B006","root_001583/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000348","role":"Turning back damage supplies the focus-side function that guidance may perform.","root":"ح ك م","source_ref":"31:2","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001583","role":"Gentle wayfinding supplies the ordinary regulating mode.","root":"ه د ي","source_ref":"31:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001580","role":"Forceful breaking supplies an alternative mode that disrupts a resistant structure.","root":"ه د ي","source_ref":"31:3","source_word_indices":["1"]},{"branch_id":"B006","mapped_root_id":"root_001580","role":"Rhythmic calming of a child supplies the opposite mode, lowering resistance to reception.","root":"ه د ي","source_ref":"31:3","source_word_indices":["1"]}],"changed_reading":{"after":"Exploratorily, wise signs may also modulate receptivity by breaking a resistant pattern or calming the reader into attention.","before":"Guidance changes a reader only by supplying correct semantic direction."},"confidence":"exploratory","containment":"This is surprising because it activates the packet's form-distant ه د د target for 31:3's guidance root. It remains anchored through the immediate guidance predicate and 31:2's corrective adjective, but downstream prose should label breaking and soothing as experimental sound/form activations, not lexical glosses of guidance.","focus_anchor":"The corrective governing quality in 31:2, activated by the immediate guidance predicate in 31:3.","outlier_id":"o_split_guidance_modulation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_split_guidance_modulation","source_type":"hft","support_id":"sup_c05798d40f82a678d48a","trust":"legacy_unbound"}]}
</lane_packet_json>
