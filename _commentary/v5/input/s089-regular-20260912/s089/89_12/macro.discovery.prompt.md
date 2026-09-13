# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **89:12**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_12/macro.discovery.json` and modify nothing
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
  "ayah_ref": "89:12",
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
{"branch_registry":[{"boundary":"Olumlu durum, yarar ve düzeltme bu dalın parçaları değil, karşıt kutuplarıdır; mahvetme ise bütün kullanımlara yayılmayan daha güçlü bir sonuçtur.","branch_kind":"mixed_non_bare","branch_ref":"root_001154/B001","candidate_links":[{"candidate_id":"cand_9df2cf292fca9d715efd","lane":"macro"},{"candidate_id":"cand_6bb86eeffee062c5542d","lane":"macro"},{"candidate_id":"cand_cd8e56ea9766bdcc6d30","lane":"macro"},{"candidate_id":"cand_29f01f38cc4379d53eb4","lane":"macro"},{"candidate_id":"cand_a3c00f48868034b44775","lane":"macro"},{"candidate_id":"cand_cc1cb52ce87311dd69dd","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"فَسَاد","morph_features":"STEM|POS:N|LEM:fasaAd|ROOT:fsd|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:12:3:2","qac_word_ref":"89:12:3","surface_ar":"فَسَادَ"}],"gloss":"bozulma ve bozma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey düzgün, elverişli veya dengeli durumunu yitirerek bozuk hâle gelir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi ya da başka bir etken, bir şeyi bozarak onu elverişli ve düzgün durumundan çıkarır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bozma eylemi, belirli bağlamlarda bir malı veya başka bir şeyi mahvetme ve işe yaramaz kılma sonucuna ulaşır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Soyut türevlerde anlam, düzeltme ve yararın karşıtı yönde bozulmayı isteme ya da zarar doğuran şey olma biçiminde belirir."}}],"root_ar":"ف س د","root_id":"root_001154","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kendiliğinden kötüleşme ile bir şeyi kötü duruma düşürme biçimindeki iki temel yönünü birlikte karşılar.","boundary_detail":"Olumlu durum, yarar ve düzeltme bu dalın parçaları değil, karşıt kutuplarıdır; mahvetme ise bütün kullanımlara yayılmayan daha güçlü bir sonuçtur.","branch_image_ar":"خروج الشيء عن الصلاح والاعتدال","concept_gloss":"bozulma ve bozma","contextual_glosses":[{"applicability":"Özne düzgünlüğünü, dengesini veya işe yararlığını kendi durum değişimiyle yitirdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öznenin iyi ve dengeli durumdan çıkıp kötü duruma geçmesini korur."},"facet_ids":["F001"],"text":"bozulmak","usage_role":"general"},{"applicability":"Bir kişi veya etken başka bir şeyi düzgün ve elverişli durumundan çıkardığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dış bir etkenin nesneyi bozuk duruma düşürmesi işlemini korur."},"facet_ids":["F002"],"text":"bozmak","usage_role":"general"},{"applicability":"Bağlam, bozmanın bir malı ya da nesneyi tümüyle işe yaramaz kılan güçlü sonucunu özellikle belirttiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bozmanın ağır ve yıkıcı sonuca ulaşan özel kullanımını korur."},"facet_ids":["F003"],"text":"mahvetmek","usage_role":"contextual"},{"applicability":"Düzeltmenin ve yararın karşıtı yöndeki türemiş, soyut anlamların açıklanmasında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bozulmaya yönelme ile yararın karşısında zarar doğurma yönlerini korur."},"facet_ids":["F004"],"text":"bozulmayı istemek ya da zarar kaynağı olmak","usage_role":"explanatory"}],"definition":"Bir şeyin düzgünlük, elverişlilik ya da dengeli durumdan çıkıp bozuk hâle gelmesi ve bir şeyin bu duruma düşürülmesidir. Türemiş ve belirli kullanımlarda bu çekirdek, düzeltme ile yararın karşıtı yönde zarar doğurmaya veya bir şeyi mahvetmeye kadar genişler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey düzgün, elverişli veya dengeli durumunu yitirerek bozuk hâle gelir."},{"facet_id":"F002","role":"core","statement":"Bir kişi ya da başka bir etken, bir şeyi bozarak onu elverişli ve düzgün durumundan çıkarır."},{"facet_id":"F003","role":"specialization","statement":"Bozma eylemi, belirli bağlamlarda bir malı veya başka bir şeyi mahvetme ve işe yaramaz kılma sonucuna ulaşır."},{"facet_id":"F004","role":"associated_use","statement":"Soyut türevlerde anlam, düzeltme ve yararın karşıtı yönde bozulmayı isteme ya da zarar doğuran şey olma biçiminde belirir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Fiziksel olmayan bozulmaları, dengeden sapmayı ve dış etkenle bozma yönünü dışarıda bırakır.","preserves":"Bir şeyin iyi durumunu yitirerek kötüleşmesi yönünü korur."},"text":"çürüme"},{"category":"common_loanword","error_profile":{"adds":"Toplumsal karışıklık, kötü niyet veya kışkırtma çağrışımını gereğinden fazla öne çıkarır.","collision":"Güncel dilde çoğunlukla ahlaki ve toplumsal kötülük alanıyla karışır.","fit":"drifted_loanword","loses":"Her tür nesne ve durum için geçerli nötr bozulma ile doğrudan bozma işlemini yeterince taşımaz.","preserves":"Bozukluk ve zarar yönünü güncel kullanımda kısmen korur."},"text":"fesat"}],"identity_rationale":"Dalın bir şeyin düzgün, elverişli ve dengeli durumundan çıkıp bozulması biçimindeki çekirdeği, yetkili kaynak ifadesiyle uyumludur. Bir şeyi bozma, zarar yönelimi ve mahvetmeye varan kullanım da aynı ifadenin açıkça desteklediği bağımlı açılımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bozulmak; düzgün ve elverişli durumdan çıkmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bozulma; düzgünlüğün ve dengenin yitmesi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bozulma, bozuk duruma gelme"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bozuk, düzgünlüğünü yitirmiş"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bozulmuş, bozuk"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bozuk kimseler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bozmak, bozuk hâle getirmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bozma, bozuk hâle getirme"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bozan veya bozulmaya yol açan kimse"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bozulmayı isteme; düzeltmenin karşıtı yönde davranma"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"zarar doğuran şey; yararın karşıtı"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bir şeyi mahvetmek veya yok etmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"saldırdığı topluluğun gerisini kesip dağıtan askerî birlik"}],"lexicalization_note":"Tanım, yalın bozulma çekirdeğini türemiş bozma ve zarar anlamlarından ayırır; belirli yapılardaki mahvetme sonucunu yalın anlamın zorunlu parçası yapmaz.","neighbor_coverage_note":"Sekiz adayın tümü değerlendirildi; sınırı en açık biçimde gösteren beş karşılaştırma yayımlandı. Özel bir eylem kullanımı, malı tüketme ve ölüm çevresi ile genel iyi durum alanındaki üç aday, seçilen ayrımlara göre daha dar, daha dolaylı veya yinelenen karşılaştırmalar sunduğu için dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, durum değişimi ile bu değişime yol açan işlemi merkez alır; komşu dal ise daha çok niteliğin düşüklüğünü ve eylemin kötü sayılmasını belirtir. Bu nedenle yalnızca bozuk nitelik bağlamlarında birbirlerine yaklaşırlar.","focus_only":"İyi ve dengeli durumdan çıkma sürecini, dış etkenle bozmayı ve zarar yönelimini birlikte kapsar.","gloss":"kötü nitelik ve bozukluk","neighbor_only":"Düşük nitelik ile kötü ve kınanan eylem değerlendirmesini özellikle öne çıkarır.","neighbor_ref":"root_000554/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin iyi, düzgün veya kabul edilir durumda olmamasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal için bozuk duruma geçmek yeterlidir ve süreç geri döndürülebilir olabilir. Komşu dalın merkezi ise daha ileri bir son aşama olan yok oluş, geçersizleşme veya mahvolmadır.","focus_only":"Tam yok oluşa varmayan bozulmayı, dengeden sapmayı ve bir şeyi bozma işlemini de kapsar.","gloss":"yok oluş ve geçersiz kalma","neighbor_only":"Yok olma, geçersiz kalma, tükenme ve kişinin sapmış ya da mahvolmuş sayılması yönlerini öne çıkarır.","neighbor_ref":"root_000164/B001","relation_type":"near_synonym","shared_zone":"İki dal, ağır bozulmanın bir şeyi işe yaramaz veya geçersiz duruma getirdiği alanda kesişir."},{"boundary_match":"partial","distinction":"Odak dal genel bir bozuk duruma geçişi anlatırken komşu dal kötülük, eksiklik ve güçsüzleşmeyi birlikte taşır. Ortak bağlamları olsa da katılımcı ve sonuç yapıları olağan karşılıklı kullanım için yeterince aynı değildir.","focus_only":"Bir nesnenin düzgün durumdan çıkmasını ve başka bir etken tarafından bozulmasını temel alır.","gloss":"kötülük, eksilme ve zayıflama","neighbor_only":"Kötülük, eksilme, güçsüzlük ve özellikle bir topluluğu zayıflatan karışıklık yönlerini bir araya getirir.","neighbor_ref":"root_000390/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da düzenin bozulması, güç kaybı ve yıkıma yaklaşan kötüleşme alanına girebilir."},{"boundary_match":"opposed","distinction":"Odak dal düzgünlüğün yitmesi ve yitirilmesine yol açma yönündedir; komşu dal düzgünlüğün bulunması veya yeniden kurulması yönündedir. Zarar ile yarar da bu karşıtlığı türemiş anlamlarda sürdürür.","focus_only":"Düzgün ve yararlı durumdan çıkmayı, bozmayı ve zarar doğuran yönelimi bildirir.","gloss":"düzelme, düzeltme ve yarar","neighbor_only":"Düzgün ve yararlı durumda olmayı, bir şeyi düzeltmeyi ve iyilikle davranmayı bildirir.","neighbor_ref":"root_000876/B001","relation_type":"antonym","shared_zone":"İki dal aynı nesne veya eylemin düzgünlüğü ve yararlılığı ekseninin karşı kutuplarını kurar."},{"boundary_match":"opposed","distinction":"Odak dal bu durumun kaybını anlatır; komşu dal ise düzgünlük, denge ve tamamlığın kurulmuş olmasını öne çıkarır. Komşunun düzleştirme ve yapısal tamamlama işlemleri odak dalın bütün kullanım alanlarının doğrudan karşıtı değildir.","focus_only":"Dengeli durumdan çıkma ile bozuk hâle gelme veya getirilme sürecini taşır.","gloss":"düzgünlük ve tamamlık","neighbor_only":"Eğriliğin giderilmesini, düzgünleşmeyi, yapısal tamamlığı ve canlıların iyi durumda olmasını kapsar.","neighbor_ref":"root_000766/B002","relation_type":"polarity_pair","shared_zone":"Her iki dal bir varlığın dengeli, düzgün ve işlevini yerine getirebilir durumda olup olmamasıyla ilgilidir."}],"source_phrase_ar":"فسد الشيء يفسد فسادا وفسودا وهو فاسد وفسيد (maqayis;sihah;tahdhib)؛ الفساد نقيض الصلاح (ayn;tahdhib)؛ الفساد خروج الشيء عن الاعتدال (mufradat)؛ أفسدته وأفسده غيره (ayn;sihah;mufradat)؛ أفسد فلان المال وفسد الشيء إذا أباره (tahdhib)؛ الاستفساد خلاف الاستصلاح والمفسدة خلاف المصلحة (sihah)","source_summary":"Kaynakların ortak çekirdeği, bir şeyin düzgün ve elverişli durumdan çıkması ile başka bir etkenin onu bozmasıdır. Toplu ifade ayrıca bozulmayı dengeden sapma olarak açıklar; türemiş kullanımları düzeltme ve yararın karşıtına yerleştirir, güçlü bir kullanımda ise bozmayı mahvetme sonucuna kadar götürür.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه فساد الشيء وفسوده وكونه فاسدا أو فسيدا؛ وإفساد الغير له؛ والمفسدة والاستفساد في جهة خلاف المصلحة والاستصلاح؛ وإبارة الشيء وإهلاكه","what_is_not_ar":"الصلاح والمصلحة والاستصلاح أضداد لا أفراد؛ واستسفد في عبارة استسفد السلطان قائده ليس من هذا الأصل"},"support_links":["sup_28914d4edf4347ed5a28","sup_3b82aeb9a78904e1b2cd","sup_80f5226e49c84d776366","sup_a6e7ef9ce1e78d7824b1","sup_af9f4368ca231d4046a8","sup_bd6cdec99fc43409809f"]},{"boundary":"Çekirdek anlam yalın çokluktur; yarışma, övünme ve kalıplaşmış özel adlandırmalar bu sınırın dışında tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B001","candidate_links":[{"candidate_id":"cand_9df2cf292fca9d715efd","lane":"macro"},{"candidate_id":"cand_6bb86eeffee062c5542d","lane":"macro"},{"candidate_id":"cand_cd8e56ea9766bdcc6d30","lane":"macro"},{"candidate_id":"cand_29f01f38cc4379d53eb4","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَكْثَرُ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>akovaru|ROOT:kvr|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:12:1:2","qac_word_ref":"89:12:1","surface_ar":"أَكْثَرُ"}],"gloss":"çokluk ve sayıca artma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çokluk, azlığın karşıtıdır ve özellikle sayılabilen varlıklarda sayının yüksekliğini ya da artışını bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şey çok duruma gelebilir, bir başkası onu çok duruma getirebilir veya kişi ondan çokça edinebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Az ve çok, malın ya da içinde bulunulan durumun iki karşıt ölçüsünü birlikte anan kalıpta kullanılabilir."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin çok bulunmasını ve sayısının artmasını birlikte anlatan genel çekirdek için uygundur.","boundary_detail":"Çekirdek anlam yalın çokluktur; yarışma, övünme ve kalıplaşmış özel adlandırmalar bu sınırın dışında tutulur.","branch_image_ar":"الكثرة ونماء العدد","concept_gloss":"çokluk ve sayıca artma","contextual_glosses":[{"applicability":"Bir şeyin kendiliğinden ya da süreç içinde sayıca çok duruma gelmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyin çok duruma gelme sürecini korur."},"facet_ids":["F002"],"text":"çoğalmak","usage_role":"contextual"},{"applicability":"Bir kişinin ya da etkenin bir şeyi çok duruma getirdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dışarıdan yapılan çoklaştırma işlemini korur."},"facet_ids":["F002"],"text":"çoğaltmak","usage_role":"contextual"},{"applicability":"Malın veya bir durumun az ve çok miktarlarını birlikte karşılayan kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşıt iki miktarın birlikte anılmasını korur."},"facet_ids":["F003"],"text":"azı ve çoğu","usage_role":"contextual"}],"definition":"Bir şeyin ya da ayrık bir niceliğin az olmayacak ölçüde bulunması veya sayıca artmasıdır. Buna bir şeyi çok duruma getirme ve ondan çokça edinme gibi bu çekirdekten türeyen işlemler de bağlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çokluk, azlığın karşıtıdır ve özellikle sayılabilen varlıklarda sayının yüksekliğini ya da artışını bildirir."},{"facet_id":"F002","role":"extension","statement":"Bir şey çok duruma gelebilir, bir başkası onu çok duruma getirebilir veya kişi ondan çokça edinebilir."},{"facet_id":"F003","role":"associated_use","statement":"Az ve çok, malın ya da içinde bulunulan durumun iki karşıt ölçüsünü birlikte anan kalıpta kullanılabilir."}],"identity_rationale":"Kaynak ifadesi, çokluğu azlığın karşıtı ve sayının artması olarak kurar; ayrıca bir şeyin çok duruma gelmesini, çok duruma getirilmesini ve ondan çokça edinilmesini de açıkça kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"çokluk; sayının artması ve azlığın karşıtı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şey çoğaldı, sayısı arttı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"çok, sayıca fazla"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyi çoğaltmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir şeyden çokça edinmek veya onu çok saymak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"malın ya da durumun azı ve çoğu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"pek çok, çok büyük sayıda"}],"lexicalization_note":"Tanım yalın çokluk çekirdeğini öne alır; artırma, çokça edinme ve azıyla çoğunu birlikte anan kalıp ayrı bağımlı kullanımlar olarak korunur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel artış, çokluk yarışı ve koyuna özgü çoğalma, çekirdek sınırı en açık biçimde gösterdikleri için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Artış bir miktara eklenme işlemini öne çıkarırken odak dal, herhangi bir karşılaştırmalı ekleme gerektirmeden çok olma durumunu da anlatır.","focus_only":"Odak dal, bir şeyin çok bulunmasını ve azlığın karşıtı olan durumu da kapsar.","gloss":"artış ve çokluk","neighbor_only":"Komşu dal, var olan ölçünün üzerine belirli bir ekleme yapılmasını çekirdek edinir.","neighbor_ref":"root_000558/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da sayının veya miktarın başlangıçtakinden daha yüksek olabildiği durumlarda buluşur."},{"boundary_match":"partial","distinction":"Odak dal yalın çokluk ve çoğalmadır; komşu dal ise çokluğu taraflar arasındaki yarışın ve üstün gelmenin ölçüsü yapar.","focus_only":"Odak dalda başka bir tarafı geçme ya da övünme koşulu bulunmaz.","gloss":"çokluk ve çokluk yarışı","neighbor_only":"Komşu dal iki tarafın çokluk bakımından yarışmasını, övünmesini veya birinin ötekini geçmesini gerektirir.","neighbor_ref":"root_001286/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da sayının, malın veya başka bir varlığın çokluğu belirleyici olabilir."},{"boundary_match":"partial","distinction":"Komşu dalın kapsamı koyunla sınırlıyken odak dal nesne türüne bağlı olmayan genel çokluk çekirdeğidir.","focus_only":"Odak dal her tür sayılabilir varlıkta ve nicelikte genel çokluğu kapsar.","gloss":"genel çokluk ve koyun çokluğu","neighbor_only":"Komşu dal yalnız koyun sürüsünün çoğalmasına bağlı özel bir kullanımdır.","neighbor_ref":"root_000900/B002","relation_type":"near_neighbor","shared_zone":"İki dal da sayılabilir varlıkların sayıca çok olmasını anlatabilir."}],"source_phrase_ar":"الكثرة نماء العدد (ayn;tahdhib)؛ الكثير ضد القليل (jamhara)؛ الكثرة نقيض القلة (sihah)؛ أصل صحيح يدل خلاف القلة (maqayis)؛ الكثرة والقلة يستعملان في الكمية المنفصلة كالأعداد (mufradat)؛ كثر الشيء كثرة فهو كثير (ayn;sihah;tahdhib)؛ أكثرت الشيء وكثرته جعلته كثيرا (ayn;tahdhib)؛ استكثرت من الشيء أي أكثرت منه (sihah)؛ عدد كثار وكثير وكاثر (jamhara;sihah;mufradat;maqayis)","source_summary":"Kaynaklar çokluğu azlığın karşıtı, sayının artması ve bir şeyin çok olması diye ortaklaştırır; ayrıca çoklaştırma, çokça edinme ve çokluk bildiren niteleme biçimlerini aynı anlam alanına bağlar.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه كثرة الشيء والعدد والمال، وضد القلة، والوصف بكثير وكثار وكاثر، وجعل الشيء كثيرا أو الاستكثار منه.","what_is_not_ar":"ليس هو التفاخر أو الغلبة بالكثرة من حيث هي منافسة، ولا كوثر النهر أو الخير الكثير بوصفه اسما مخصوصا، ولا جمار النخل."},"support_links":["sup_28914d4edf4347ed5a28","sup_a6e7ef9ce1e78d7824b1","sup_af9f4368ca231d4046a8","sup_bd6cdec99fc43409809f"]},{"boundary":"Yalın biçimde çok olma bu dala yetmez; karşılaştırma, yarışma, övünme veya çoklukla üstün gelme gerekir.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْثَرُ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>akovaru|ROOT:kvr|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:12:1:2","qac_word_ref":"89:12:1","surface_ar":"أَكْثَرُ"}],"gloss":"çokluk yarışı ve çoklukla üstün gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taraflar çokluğu bir karşılaştırma ve yarışma ölçüsü yapar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yarışın sonucu, bir tarafın sayıca daha çok olup öteki tarafa üstün gelmesi olabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yarışma ve övünme yalnız kişi sayısında değil, malda ve saygınlık sağlayan güçte de gerçekleşebilir."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tarafların çokluğu yarıştırdığı, bununla övündüğü veya birinin daha çok olarak ötekini geçtiği bağlamlar için uygundur.","boundary_detail":"Yalın biçimde çok olma bu dala yetmez; karşılaştırma, yarışma, övünme veya çoklukla üstün gelme gerekir.","branch_image_ar":"المكاثرة والغلبة بالعدد","concept_gloss":"çokluk yarışı ve çoklukla üstün gelme","contextual_glosses":[{"applicability":"Bir topluluğun öteki topluluktan daha çok olduğu ve onu bu bakımdan geçtiği durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sayı karşılaştırmasını ve üstün gelen tarafı korur."},"facet_ids":["F002"],"text":"sayıca geçmek","usage_role":"contextual"},{"applicability":"Mal, sayı veya saygınlık gücü üzerinden karşılıklı övünme ve yarışma bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yarışma alanlarını ve övünme yönünü korur."},"facet_ids":["F001","F003"],"text":"çoklukla övünme yarışı","usage_role":"contextual"}],"definition":"İki tarafın sayı, mal veya saygınlık sağlayan güç bakımından çokluk yarıştırması, bununla övünmesi ya da bir tarafın daha çok olarak ötekini geçmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taraflar çokluğu bir karşılaştırma ve yarışma ölçüsü yapar."},{"facet_id":"F002","role":"specialization","statement":"Yarışın sonucu, bir tarafın sayıca daha çok olup öteki tarafa üstün gelmesi olabilir."},{"facet_id":"F003","role":"extension","statement":"Yarışma ve övünme yalnız kişi sayısında değil, malda ve saygınlık sağlayan güçte de gerçekleşebilir."}],"identity_rationale":"Kaynak ifadesi iki tarafın sayı, mal veya güç sayılan bir üstünlük alanında yarışmasını ve bir tarafın çoklukla ötekini geçmesini açıkça bildirir; yenilen tarafı adlandıran biçim de aynı karşıt ilişkiyi doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"onlarla çokluk yarışına girdik ve onları sayıca geçtik"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"mal, sayı veya güç bakımından çokluk yarışı ve övünme"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"çokluk yarışında yenilmiş"}],"lexicalization_note":"Tanım, yarışma ve üstün gelme bildiren yapılara bağlıdır; yalın çokluk anlamı bu yapılardan bağımsız biçimde dala aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalın çokluk, cömertlik yarışı ve genel övünme, bu dalın çokluk ölçüsüne bağlı yarış sınırını en iyi gösteren karşılaştırmalardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda çokluk karşılaştırmalı bir yarışın aracıdır; komşu dalda ise kendi başına bir nicelik durumu veya artma sürecidir.","focus_only":"Odak dal, taraflar arasında yarışma veya üstün gelme ilişkisini zorunlu kılar.","gloss":"çokluk yarışı ve yalın çokluk","neighbor_only":"Komşu dal, başka bir taraf bulunmadan yalın çokluğu ve çoğalmayı da kapsar.","neighbor_ref":"root_001286/B001","relation_type":"near_neighbor","shared_zone":"İki dal da sayının, malın veya başka bir ölçünün çok olmasına dayanır."},{"boundary_match":"partial","distinction":"İlişki düzeni benzese de üstünlüğün ölçüsü ayrıdır: odak dal çokluğu, komşu dal cömertliği temel alır.","focus_only":"Odak dalın yarış ölçüsü sayı, mal veya toplumsal güç gibi çokluk alanlarıdır.","gloss":"çoklukta ve cömertlikte yarış","neighbor_only":"Komşu dalın yarış ölçüsü cömertlik ve eli açıklıktır.","neighbor_ref":"root_001294/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal karşılıklı övünme ve bir tarafın belirli bir ölçütte ötekini geçmesi düzenini taşır."},{"boundary_match":"partial","distinction":"Odak dal, üstünlük iddiasını sayı veya mal gibi çoğaltılabilir değerlere bağlarken komşu dal daha genel bir övünme üstünlüğüdür.","focus_only":"Odak dal övünmeyi özellikle çokluk ölçüsüne bağlar.","gloss":"çoklukla övünmek ve genel övünme","neighbor_only":"Komşu dal övünme alanını belirli bir çokluk ölçüsüyle sınırlamaz.","neighbor_ref":"root_001135/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da karşılıklı övünme ve bir tarafın üstün sayılması bulunabilir."}],"source_phrase_ar":"كاثرناهم فكثرناهم (ayn;sihah;tahdhib)؛ كاثر بنو فلان بني فلان فكثروهم إذا زادوا على عددهم (jamhara)؛ كاثر بنو فلان بني فلان فكثروهم أي كانوا أكثر منهم (maqayis)؛ كاثرناهم فكثرناهم أي غلبناهم بالكثرة (sihah)؛ التكاثر المكاثرة (sihah)؛ التفاخر بكثرة العدد والمال (tahdhib)؛ المكاثرة والتكاثر التباري في كثرة المال والعز (mufradat)؛ فلان مكثور أي مغلوب في الكثرة (mufradat)","source_summary":"Kaynaklar, çokluk bakımından karşılıklı yarışmayı sayıca geçme ve üstün gelme sonucuyla birlikte verir; yarışın mal ve toplumsal güç üzerinden övünmeye uzanabildiğini de belirtir.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه كاثرناهم فكثرناهم، ومكاثرة القوم إذا غلبوا غيرهم بالعدد، والتكاثر والتفاخر أو التباري بكثرة العدد والمال والعز.","what_is_not_ar":"ليس هو مجرد كون الشيء كثيرا بلا مقابلة أو مفاخرة، ولا المكثر بمعنى كثير المال وحده."},"support_links":[]},{"boundary":"Her anlam kendi kalıbına bağlıdır; mal çokluğu, çok konuşma, çok sayıda istemle karşılaşma ve başkasının malıyla çok görünme birbirinin yerine geçmez.","branch_kind":"collocation","branch_ref":"root_001286/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْثَرُ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>akovaru|ROOT:kvr|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:12:1:2","qac_word_ref":"89:12:1","surface_ar":"أَكْثَرُ"}],"gloss":"kişiye bağlı çokluk nitelemeleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli kişi ve durum kalıpları, malın, sözün, isteklerin veya hakların bir kişiye bağlı çokluğunu bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başka bir kişi kalıbı, kadın veya erkeğin çok konuştuğunu bildirir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Edilgen yapı, kişiden iyilik isteyenlerin veya onun üzerindeki hakların çokluğunu bildirir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir başka kalıp, kişinin başkasının malına dayanarak kendini çok malı varmış gibi göstermesini anlatır."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız mal, konuşma, istem veya hak çokluğunu belirli kişi kalıplarında toplayan üst açıklama olarak uygundur.","boundary_detail":"Her anlam kendi kalıbına bağlıdır; mal çokluğu, çok konuşma, çok sayıda istemle karşılaşma ve başkasının malıyla çok görünme birbirinin yerine geçmez.","branch_image_ar":"كثرة في صاحب أو كلام أو مطالب","concept_gloss":"kişiye bağlı çokluk nitelemeleri","contextual_glosses":[{"applicability":"Bir kişinin varlığının ve malının çok olduğunu bildiren kişi kalıbında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye yüklenen mal çokluğunu korur."},"facet_ids":["F001"],"text":"malı çok kişi","usage_role":"contextual"},{"applicability":"Kadın veya erkek için sözün çokluğunu bildiren niteleme kalıbında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşmanın çokluğu ve kişi niteliğini korur."},"facet_ids":["F002"],"text":"çok konuşan kişi","usage_role":"contextual"},{"applicability":"Kendisinden iyilik isteyenlerin veya üzerindeki hakların çok olduğu kişi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çok sayıda isteyen veya hak sahibinin kişiye yönelmesini korur."},"facet_ids":["F003"],"text":"istek ve hak yükü altında","usage_role":"explanatory"},{"applicability":"Kişinin kendisine ait olmayan mala dayanarak çok malı varmış gibi görünmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Malın başkasına ait oluşunu ve görünüş yaratmayı korur."},"facet_ids":["F004"],"text":"başkasının malıyla varlıklı görünmek","usage_role":"contextual"}],"definition":"Belirli kalıplarda bir kişinin malının ya da sözünün çok olması, kendisinden iyilik isteyenlerin veya üzerindeki hakların çoğalması yahut başkasının malıyla kendini varlıklı göstermesidir. Bu kullanımlar yalnız bağlı oldukları kalıp içinde geçerlidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli kişi ve durum kalıpları, malın, sözün, isteklerin veya hakların bir kişiye bağlı çokluğunu bildirir."},{"facet_id":"F002","role":"specialization","statement":"Başka bir kişi kalıbı, kadın veya erkeğin çok konuştuğunu bildirir."},{"facet_id":"F003","role":"specialization","statement":"Edilgen yapı, kişiden iyilik isteyenlerin veya onun üzerindeki hakların çokluğunu bildirir."},{"facet_id":"F004","role":"associated_use","statement":"Bir başka kalıp, kişinin başkasının malına dayanarak kendini çok malı varmış gibi göstermesini anlatır."}],"identity_rationale":"Kaynak ifadesi tek bir yalın anlamdan çok, belirli kişi ve durum kalıplarında malı veya sözü çok olma, üzerinde çok sayıda istek ya da hak bulunma ve başkasının malıyla çok görünme kullanımlarını toplar. Dal korunabilir, ancak bu kullanımlar ortak bir yalın kök anlamı gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"malı çok kişi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çok konuşan kadın veya erkek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"iyilik isteyenleri veya üzerindeki haklar çoğalmış kişi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"başkasının malıyla kendini varlıklı göstermek"}],"lexicalization_note":"Tanım yalnız verilen kişi ve durum kalıplarının anlam alanını düzenler; bunlardan bağımsız bir yalın çokluk anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; genel çokluk, hak isteme ve çokluk yarışı, kalıba bağlı kişi nitelemelerinin sınırını en belirgin biçimde açığa çıkarır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal, çokluk öğesini farklı kalıpların kişi nitelemelerine dağıtır; komşu dal ise çokluğu kendi başına tanımlar.","focus_only":"Odak dalda her anlam belirli bir kişi veya durum kalıbına bağlıdır.","gloss":"kalıba bağlı ve genel çokluk","neighbor_only":"Komşu dal, kalıptan bağımsız yalın çokluğu ve sayıca artmayı kapsar.","neighbor_ref":"root_001286/B001","relation_type":"same_field","shared_zone":"Her iki dalın kullanımlarında da bir varlığın, sözün, malın veya istemin çokluğu bulunur."},{"boundary_match":"partial","distinction":"Odak dalda belirleyici olan isteyenlerin ya da hakların çokluğudur; komşu dalda ise tek bir istem bile olsa hakkın peşine düşme ilişkisidir.","focus_only":"Odak dal, istem veya hak sahiplerinin çokluğunu ve bunların bir kişinin üzerinde birikmesini bildirir.","gloss":"çok sayıda istem ve hak isteme","neighbor_only":"Komşu dal, istemin sayısından bağımsız olarak bir hakkı veya alacağı isteme eylemini çekirdek edinir.","neighbor_ref":"root_000175/B005","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişiye yönelen hak veya iyilik istemleri bağlamında buluşabilir."},{"boundary_match":"field_only","distinction":"Odak dalın kişi nitelemeleri karşılıklı yarışma gerektirmez; komşu dalın çekirdeği karşılaştırma ve üstün gelmedir.","focus_only":"Odak dal kişide bulunan mal, söz veya yük çokluğunu kalıplaşmış biçimde niteler.","gloss":"çokluk niteliği ve çokluk yarışı","neighbor_only":"Komşu dal iki tarafın çokluğu yarıştırmasını ve birinin üstün gelmesini anlatır.","neighbor_ref":"root_001286/B002","relation_type":"same_field","shared_zone":"Her iki dalda mal veya sayı gibi çokluk ölçüleri kişilere bağlanabilir."}],"source_phrase_ar":"رجل مكثر كثير المال (ayn;tahdhib)؛ أكثر الرجل أي كثر ماله (sihah)؛ رجل كاثر إذا كان كثير المال (mufradat)؛ رجل مكثار وامرأة مكثار وهما الكثيرا الكلام (ayn)؛ رجل مكثار وامرأة مكثار إذا كانا كثيري الكلام (tahdhib)؛ المكثار متعارف في كثرة الكلام (mufradat)؛ رجل مكثور عليه أي كثر من يطلب إليه معروفه (ayn;tahdhib)؛ مكثور عليه إذا نفد ما عنده وكثرت عليه الحقوق (sihah)؛ فلان يتكثر بمال غيره (sihah)","source_summary":"Kaynaklar, kalıba göre mal çokluğu, çok konuşma, iyilik isteyenlerin veya hak sahiplerinin çoğalması ve başkasının malıyla varlıklı görünme anlamlarını verir; bunlar ortak çokluk öğesine rağmen ayrı kullanımlardır. Bir açıklamada hakların çoğalmasına kişinin elindekinin tükenmesi eşlik eder.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه مكثر أو كاثر بمعنى كثير المال، ومكثار في كثرة الكلام، ومكثور عليه لكثرة طالبي المعروف أو الحقوق عليه، ويتكثر بمال غيره.","what_is_not_ar":"ليس هو المكاثرة بين جماعتين، ولا كوثر بمعنى السيد الكثير الخير أو النهر."},"support_links":[]},{"boundary":"Irmak, bol iyilik ve cömert kişi ayrı sözlüksel gerçekleşmelerdir; ortak bağları olağanüstü bolluk düşüncesidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْثَرُ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>akovaru|ROOT:kvr|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:12:1:2","qac_word_ref":"89:12:1","surface_ar":"أَكْثَرُ"}],"gloss":"özel ırmak veya bol iyilik","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"specialization","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözlük birimi cennette bulunan ve başka ırmakların kendisinden ayrıldığı özel bir ırmağı adlandırır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözlük biriminin ortak çekirdeği, ırmak, iyilik ve kişi kullanımlarını olağanüstü bolluk düşüncesine bağlar."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişi kalıbında iyiliği ve bağışı çok, cömert ve önder bir erkek nitelenir."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözlük biriminin iki temel açıklamasını birlikte gösterir; kişi nitelemesi ayrıca bağlama bağlıdır.","boundary_detail":"Irmak, bol iyilik ve cömert kişi ayrı sözlüksel gerçekleşmelerdir; ortak bağları olağanüstü bolluk düşüncesidir.","branch_image_ar":"الكوثر: خير كثير وفيض مخصوص","concept_gloss":"özel ırmak veya bol iyilik","contextual_glosses":[{"applicability":"Başka ırmakların kendisinden ayrıldığı bildirilen cennet ırmağı anlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Irmak oluşunu ve cennete özgü gönderimi korur."},"facet_ids":["F001"],"text":"cennetteki özel ırmak","usage_role":"contextual"},{"applicability":"Birine verilmiş çok geniş ve büyük iyiliği anlatan açıklamada kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İyiliğin hem bolluğunu hem büyüklüğünü korur."},"facet_ids":["F002"],"text":"bol ve büyük iyilik","usage_role":"contextual"},{"applicability":"Cömertliği, iyiliği ve çok bağışta bulunmasıyla öne çıkan erkek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin cömertliğini, önderliğini ve bağış bolluğunu korur."},"facet_ids":["F003"],"text":"iyiliği ve bağışı bol önder","usage_role":"contextual"}],"definition":"Olağanüstü bolluk bildiren özel bir sözlük birimi, cennetteki bir ırmağı veya bol ve büyük iyiliği adlandırır; kişi kalıbında ise iyiliği ve bağışı bol, cömert bir önderi niteler.","distinctive_facets":[{"facet_id":"F001","role":"specialization","statement":"Sözlük birimi cennette bulunan ve başka ırmakların kendisinden ayrıldığı özel bir ırmağı adlandırır."},{"facet_id":"F002","role":"core","statement":"Sözlük biriminin ortak çekirdeği, ırmak, iyilik ve kişi kullanımlarını olağanüstü bolluk düşüncesine bağlar."},{"facet_id":"F003","role":"extension","statement":"Kişi kalıbında iyiliği ve bağışı çok, cömert ve önder bir erkek nitelenir."}],"identity_rationale":"Kaynak ifadesi aynı sözlük birimini cennetteki özel ırmak, bol ve büyük iyilik, ayrıca iyiliği ve bağışı bol cömert önder için kullanır. Dal bu sözlüksel çokanlamlılık olarak korunabilir; bu üç gönderim tek bir varlık tanımıymış gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"cennetteki özel ırmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bol veya büyük iyilik"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"iyiliği ve bağışı bol, cömert önder"}],"lexicalization_note":"Tanım, yalın bir çokluk anlamı kurmak yerine verilen sözcük ve kişi kalıbına bağlı üç özel kullanımı ayrı tutar.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel çokluk, aynı kökteki yoğun toz kullanımı ve bastıran çokluk, özel bolluk anlamlarının sınırını en yararlı biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bolluğu belirli bir ırmak, iyilik veya cömert kişi adı ve nitelemesi içinde özelleştirir; komşu dal genel nicelik çekirdeğidir.","focus_only":"Odak dal belirli bir sözlük biriminin ırmak, bol iyilik ve cömert kişi kullanımlarına bağlıdır.","gloss":"özel bolluk kullanımı ve genel çokluk","neighbor_only":"Komşu dal varlık türünden bağımsız yalın çokluğu ve sayıca artmayı anlatır.","neighbor_ref":"root_001286/B001","relation_type":"near_neighbor","shared_zone":"İki dal da azlığın karşıtı olan bolluk düşüncesini taşıyabilir."},{"boundary_match":"field_only","distinction":"Ortak bolluk bağına karşın gönderimler ayrıdır: odak dal iyilik, ırmak ve kişiyi; komşu dal tozu ve aşırı çoğalmayı anlatır.","focus_only":"Odak dal ırmak, iyilik ve cömert kişiyle ilgili özel kullanımları kapsar.","gloss":"bol iyilik ve yoğun toz","neighbor_only":"Komşu dal kabarıp yükselen yoğun tozu ve bir şeyin aşırı derecede çoğalmasını kapsar.","neighbor_ref":"root_001286/B005","relation_type":"same_field","shared_zone":"İki dalın sözlük birimleri olağanüstü çokluk ve bolluk düşüncesiyle açıklanır."},{"boundary_match":"partial","distinction":"Odak dalda baskın gelme koşulu yoktur; komşu dalda çokluğun yükselerek başka şeyleri örtmesi veya yenmesi belirleyicidir.","focus_only":"Odak dalda bolluk özel olarak iyilik, bağış, kişi veya ırmakla sözlükselleşir.","gloss":"bolluk ve bastıran çokluk","neighbor_only":"Komşu dal çokluğun yükselip çevresindekileri bastırmasını çekirdek edinir.","neighbor_ref":"root_000952/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal olağan ölçüyü aşan bir çokluğu anlatabilir."}],"source_phrase_ar":"الكوثر نهر في الجنة يتشعب منه أكثر أنهار الجنة (ayn)؛ الكوثر الخير الكثير الذي أعطاه النبي (ayn)؛ الكوثر من الرجال السيد الكثير الخير (sihah)؛ الكوثر نهر في الجنة وأراد الخير الكثير (maqayis)؛ الكوثر هو الخير الكثير (tahdhib)؛ الكوثر فوعل من الكثرة ومعناه الخير الكثير (tahdhib)؛ الكوثر الرجل الكثير العطاء والخير والسيد (tahdhib)؛ قيل هو نهر في الجنة وقيل الخير العظيم (mufradat)؛ يقال للرجل السخي كوثر (mufradat)","source_summary":"Kaynaklar özel sözlük birimini cennetteki bir ırmak ve bol ya da büyük iyilik olarak açıklar; kişi için kullanıldığında cömertliği, önderliği, iyilik ve bağış bolluğunu bildirir. Bir açıklamada cennet ırmaklarının çoğunun ondan ayrıldığı, bir diğerinde ise bol iyiliğin Peygamber'e verildiği belirtilir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الكوثر بوصفه نهر الجنة، أو الخير الكثير العظيم، أو الرجل السيد السخي الكثير الخير والعطاء، وكل ذلك من فوعل الكثرة.","what_is_not_ar":"ليس هو مطلق الكثرة العددية، ولا جمار النخل، ولا غبار الكوثر إلا من جهة صيغة المبالغة في الكثرة."},"support_links":[]},{"boundary":"Toz kullanımı yükselme veya kabarma görüntüsüne bağlıdır; genel biçim ise yalnız aşırı derecede çoğalmayı bildirir.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B005","candidate_links":[{"candidate_id":"cand_cc1cb52ce87311dd69dd","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَكْثَرُ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>akovaru|ROOT:kvr|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:12:1:2","qac_word_ref":"89:12:1","surface_ar":"أَكْثَرُ"}],"gloss":"kabarıp yükselen yoğun toz","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek olağanüstü çokluktur; toz kalıbında bu çokluk kabarıp havada yükselen yoğun bir görünüm alır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toz dışındaki bir şey için kullanılan biçim, onun aşırı ve son sınıra varan ölçüde çoğalmasını bildirir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ölüm sahnesindeki tozun kabarıp çoklaşması, yoğun toz kullanımına örnek oluşturur."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın görüntü bakımından belirgin toz çekirdeğini karşılar; genel aşırı çoğalma ayrıca bağlama göre çevrilir.","boundary_detail":"Toz kullanımı yükselme veya kabarma görüntüsüne bağlıdır; genel biçim ise yalnız aşırı derecede çoğalmayı bildirir.","branch_image_ar":"كوثر الغبار وتكوثره","concept_gloss":"kabarıp yükselen yoğun toz","contextual_glosses":[{"applicability":"Çok miktarda tozun kabarıp havada görünür duruma geldiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tozun çokluğunu ve havada toplanmış görünümünü korur."},"facet_ids":["F001","F003"],"text":"yoğun toz bulutu","usage_role":"contextual"},{"applicability":"Tozla sınırlı olmayan biçimde bir şeyin aşırı ölçüde çok duruma gelmesi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çoğalmanın aşırı dereceye varmasını korur."},"facet_ids":["F002"],"text":"son derece çoğalmak","usage_role":"contextual"}],"definition":"Toz kalıbında, çok olup kabaran veya havada belirgin biçimde yükselen yoğun tozu anlatır. Ayrı bir biçimde ise herhangi bir şeyin son derece çoğalmasını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek olağanüstü çokluktur; toz kalıbında bu çokluk kabarıp havada yükselen yoğun bir görünüm alır."},{"facet_id":"F002","role":"extension","statement":"Toz dışındaki bir şey için kullanılan biçim, onun aşırı ve son sınıra varan ölçüde çoğalmasını bildirir."},{"facet_id":"F003","role":"example","statement":"Ölüm sahnesindeki tozun kabarıp çoklaşması, yoğun toz kullanımına örnek oluşturur."}],"identity_rationale":"Kaynak ifadesi yoğunlaşıp yükselen tozu adlandıran özel kullanımla bir şeyin son derece çoğalmasını bildiren biçimi birlikte verir. Ortak aşırı çokluk bağı dalı korur, ancak toz görüntüsü genel çoğalma anlamının zorunlu parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kabarıp yükselen yoğun toz"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"son derece çoğalmak"}],"lexicalization_note":"Tanım, toza bağlı kalıbı ve genel aşırı çoğalma biçimini ayrı yüzler olarak tutar; toz özelliğini yalın çoğalma anlamına taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yükselmiş toz, havadaki görünür toz ve genel çokluk, dalın yoğunluk, kabarma ve aşırılık sınırlarını en açık biçimde karşılaştırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Toz bağlamında anlamlar büyük ölçüde örtüşür; odak dal çokluk ve kabarmayı belirginleştirir ve ayrıca toz dışı aşırı çoğalma kullanımına sahiptir.","focus_only":"Odak dal, yoğun toz yanında bir şeyin aşırı çoğalmasını bildiren ayrı bir biçimi de kapsar.","gloss":"yoğun kabaran toz ve yükselmiş toz","neighbor_only":"Komşu dal tozu genel olarak, özellikle kaldırılmış veya yükselmiş toz olarak adlandırır.","neighbor_ref":"root_001544/B004","relation_type":"near_synonym","shared_zone":"İki dal da havaya kalkmış, görünür ve yoğun tozu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeğinde yoğunluk ve çokluk vardır; komşu dal görünürlük ve havada uçuşan toz görüntüsüne daha geniş yer verir.","focus_only":"Odak dal tozun çokluğunu ve kabarmasını, ayrıca genel aşırı çoğalmayı bildirir.","gloss":"kabarık yoğun toz ve havadaki toz","neighbor_only":"Komşu dal havada parlayan veya ışıkta belirginleşen ince toz parçalarını da kapsar.","neighbor_ref":"root_001576/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da tozun havaya yükselip görünür olması bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal çokluğun son dereceye ulaşmasını veya yoğun toz olarak görünmesini gerektirirken komşu dal derece bakımından nötrdür.","focus_only":"Odak dal aşırı çoğalmayı ve toza özgü kabarıp yükselme görüntüsünü taşır.","gloss":"aşırı çoğalma ve genel çokluk","neighbor_only":"Komşu dal herhangi bir aşırılık ya da toz görüntüsü gerektirmeyen genel çokluktur.","neighbor_ref":"root_001286/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir şeyin çok olması veya çoğalması durumunu anlatabilir."}],"source_phrase_ar":"الكوثر من الغبار الكثير وقد تكوثر (sihah)؛ يقال للغبار إذا سطع وكثر كوثر (tahdhib)؛ الكوثر الغبار سمي بذلك لكثرته وثورانه (maqayis)؛ تكوثر الشيء كثر كثرة متناهية (mufradat)؛ ثار نقع الموت حتى تكوثرا (sihah;mufradat)","source_summary":"Kaynaklar, çokluğu yüzünden kabarıp yükselen yoğun tozu ve bir şeyin son derece çoğalmasını aynı aşırılık alanında birleştirir; kabaran ölüm tozu bu kullanıma örnek verilir.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الكوثر من الغبار إذا كثر وثار أو سطع، وتكوثر الشيء إذا كثر كثرة متناهية.","what_is_not_ar":"ليس هو الكوثر بمعنى نهر الجنة أو الخير العظيم، ولا مطلق كثير بلا صورة ثوران أو إفراط."},"support_links":["sup_80f5226e49c84d776366"]},{"boundary":"Temel gönderim hurma ağacının iç göbeğidir; çiçek salkımının ilk oluşumu kaynaklarda verilen daha geniş bir açıklamadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْثَرُ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>akovaru|ROOT:kvr|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:12:1:2","qac_word_ref":"89:12:1","surface_ar":"أَكْثَرُ"}],"gloss":"hurma ağacının iç göbeği","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, hurma ağacının tepesindeki yumuşak ve yenilebilir iç göbektir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı açıklamalar aynı adı hurmanın çiçek salkımının ilk oluşumuna da verir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir ceza sözünde bu hurma ürünü, meyveyle birlikte el kesme cezasının uygulanmadığı şeyler arasında anılır."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakların ortak temel gönderimini, hurma ağacının yumuşak iç bölümü olarak karşılar.","boundary_detail":"Temel gönderim hurma ağacının iç göbeğidir; çiçek salkımının ilk oluşumu kaynaklarda verilen daha geniş bir açıklamadır.","branch_image_ar":"الكثر جمار النخل","concept_gloss":"hurma ağacının iç göbeği","contextual_glosses":[{"applicability":"Ağacın tepe kısmından çıkarılan yumuşak iç göbek yiyecek olarak söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hurmaya ait oluşu, iç konumu ve yenilebilirliği korur."},"facet_ids":["F001"],"text":"hurmanın yenilebilir iç bölümü","usage_role":"explanatory"},{"applicability":"Adın hurma ağacındaki çiçek salkımının ilk oluşumu için kullanıldığı açıklamaya uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hurma ağacını ve çiçeklenmenin ilk oluşumunu korur."},"facet_ids":["F002"],"text":"hurmanın ilk çiçek sürgünü","usage_role":"contextual"}],"definition":"Hurma ağacının tepe bölümündeki yumuşak ve yenilebilir iç göbeğini adlandırır; bazı açıklamalarda çiçek salkımının ilk oluşumuna da uzanır. Aynı birim belirli bir ceza sözünde meyveyle birlikte anılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, hurma ağacının tepesindeki yumuşak ve yenilebilir iç göbektir."},{"facet_id":"F002","role":"source_variant","statement":"Bazı açıklamalar aynı adı hurmanın çiçek salkımının ilk oluşumuna da verir."},{"facet_id":"F003","role":"associated_use","statement":"Bir ceza sözünde bu hurma ürünü, meyveyle birlikte el kesme cezasının uygulanmadığı şeyler arasında anılır."}],"identity_rationale":"Kaynak ifadesinin ortak ağırlığı hurma ağacının yenilebilir iç göbeğindedir; bazı açıklamalar bunu ağacın çekilen öz bölümü veya çiçek salkımının ilk oluşumu olarak genişletir. Dal korunabilir, fakat bu ikinci açıklama kesin eşdeğer gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"hurma ağacının iç göbeği; bazı açıklamalarda ilk çiçek sürgünü"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"meyve veya hurma göbeği için el kesme cezası yoktur"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"hurma ağacı çiçek sürgünü verdi"}],"lexicalization_note":"Tanım, bitki adını çekirdek alır; söz içindeki kullanım ve ağacın çiçeklenmesini bildiren biçim ayrı bağlı kullanımlar olarak korunur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel ağaç göbeği, hurma salkımı ve zararlı sert sürgün, bitkinin aynı bölgesindeki karışabilecek gönderimleri en iyi ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Hurma göbeği bağlamında büyük ölçüde örtüşürler; odak dalın bitki kapsamı daha dar, çiçek sürgünü açıklaması ise ona özgüdür.","focus_only":"Odak dal hurma ağacına özgüdür ve bazı açıklamalarda ilk çiçek sürgününe uzanır.","gloss":"hurma göbeği ve ağaç göbeği","neighbor_only":"Komşu dal hurma yanında başka ağaçların yumuşak iç göbeklerini de kapsar.","neighbor_ref":"root_001248/B003","relation_type":"near_synonym","shared_zone":"İki dal da hurma ağacının tepesindeki yumuşak iç bölümü adlandırır."},{"boundary_match":"field_only","distinction":"Odak dal yumuşak iç dokuya veya ilk sürgüne, komşu dal ise gelişmiş meyveleri taşıyan salkıma gönderir.","focus_only":"Odak dal ağacın iç göbeğini ve bazı açıklamalarda ilk çiçek oluşumunu anlatır.","gloss":"hurma göbeği ve meyve salkımı","neighbor_only":"Komşu dal hurmanın üzerinde meyveler bulunan bütün salkımını adlandırır.","neighbor_ref":"root_001264/B004","relation_type":"same_field","shared_zone":"İki dal da hurma ağacının tepe ve ürün oluşumu alanıyla ilgilidir."},{"boundary_match":"field_only","distinction":"Odak dal yumuşak ve yenilebilir iç bölümü öne çıkarır; komşu dal sertliği ve ağaca zarar verme sonucuyla ayrılır.","focus_only":"Odak dal yenilebilir iç göbeği veya ilk çiçek sürgününü adlandırır.","gloss":"yumuşak göbek ve zararlı sert sürgün","neighbor_only":"Komşu dal bırakıldığında ağaca zarar veren uzun ve sert bir sürgünü anlatır.","neighbor_ref":"root_000489/B003","relation_type":"same_field","shared_zone":"Her iki dal hurma ağacının kalbinden veya tepesinden çıkan bir oluşumla ilgilidir."}],"source_phrase_ar":"الكثر والكثر جمار النخل ويقال الكثر الجذب وهو الجمار أيضا (ayn)؛ الكثر الجمار وقال قوم هو الكثر بفتح الثاء (jamhara)؛ لا قطع في ثمر ولا كثر (jamhara;sihah;tahdhib;mufradat)؛ الكثر جمار النخل ويقال طلعها (sihah)؛ الكثر جمار النخل في كلام الأنصار وهو الجذب أيضا (tahdhib)؛ الكثر الجمار الكثير وحكي بتسكين الثاء (mufradat)","source_summary":"Kaynaklar adı çoğunlukla hurma ağacının iç göbeği ve çekilen öz bölümü için verir; bir açıklama çiçek salkımının ilk oluşumunu da kapsar ve yaygın bir sözde meyveyle birlikte anılır. Ad için kaynaklarda birden fazla harekeleme ve okunuş biçimi de aktarılır.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الكثر أو الكثر بمعنى جمار النخل، والجذب، وطلع النخل عند بعض المصادر، وما ورد في لا قطع في ثمر ولا كثر.","what_is_not_ar":"ليس هو الكثرة العددية، ولا الكوثر، ولا المال الكثير."},"support_links":[]},{"boundary":"Dal yalnız bir şeyin bir araya gelmesi anlamındadır; genel çokluk, hurma bölümü veya özel bolluk adlandırmaları buna katılmaz.","branch_kind":"bare","branch_ref":"root_001286/B007","candidate_links":[{"candidate_id":"cand_a3c00f48868034b44775","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَكْثَرُ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>akovaru|ROOT:kvr|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:12:1:2","qac_word_ref":"89:12:1","surface_ar":"أَكْثَرُ"}],"gloss":"bir araya toplanma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin öğeleri bir araya gelir ve toplu duruma geçer."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözcük yapısındaki ek ses, birimin çokluk anlam ailesine bağlı oluşunu açıklamak için belirtilir."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin öğelerinin birleşerek toplu duruma gelmesini anlatan yalın anlam için uygundur.","boundary_detail":"Dal yalnız bir şeyin bir araya gelmesi anlamındadır; genel çokluk, hurma bölümü veya özel bolluk adlandırmaları buna katılmaz.","branch_image_ar":"الكمثرة اجتماع الشيء","concept_gloss":"bir araya toplanma","contextual_glosses":[{"applicability":"Bir şeyin ayrı öğelerinin aynı yerde veya bütün içinde birleşmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayrı öğelerin birleşme sürecini korur."},"facet_ids":["F001"],"text":"toplanıp bir araya gelmek","usage_role":"contextual"}],"definition":"Bir şeyin parçalarının veya öğelerinin bir araya gelerek toplanmasıdır; sözlük biriminin yapısındaki ek ses, bu anlamın çokluk ailesiyle bağlantısı olarak açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin öğeleri bir araya gelir ve toplu duruma geçer."},{"facet_id":"F002","role":"associated_use","statement":"Sözcük yapısındaki ek ses, birimin çokluk anlam ailesine bağlı oluşunu açıklamak için belirtilir."}],"identity_rationale":"Tek kaynak ifadesi, bir şeyin bir araya toplanması anlamını doğrudan verir ve sözcük yapısındaki ek sesin çokluk ailesiyle bağlantısını ayrıca belirtir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"bir şeyin bir araya toplanması; yapısına m sesi eklenmiştir"}],"lexicalization_note":"Tanım, kanıtta verilen yalın sözlük biriminin bir araya toplanma anlamıyla sınırlıdır ve herhangi bir kalıp anlamı eklemez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel toplama, yönlerden bir araya getirme ve doluluk yaratan birikme, bu yalın toplanma anlamının kapsamını en iyi sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak çekirdek güçlüdür; komşu dalın eylem, katılımcı ve kullanım kapsamı odak daldan daha geniştir.","focus_only":"Odak dal yalnız bir şeyin öğelerinin bir araya toplanmasını bildirir.","gloss":"bir araya toplanma ve genel toplama","neighbor_only":"Komşu dal hem toplama eylemini hem insanların, suyun, yemeğin ve başka varlıkların çeşitli birleşme biçimlerini kapsar.","neighbor_ref":"root_001210/B001","relation_type":"near_synonym","shared_zone":"İki dal da ayrı öğelerin birleşerek toplu duruma gelmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal sonuçlanan bir araya gelişi bildirirken komşu dal toplama işlemini, yön çeşitliliğini ve türemiş kullanımları daha geniş biçimde taşır.","focus_only":"Odak dal yalın biçimde bir şeyin bir araya toplanmasını anlatır.","gloss":"toplanma ve yönlerden toplama","neighbor_only":"Komşu dal farklı yönlerden toplama, birbirine katma ve bundan türetilen adlandırmaları da kapsar.","neighbor_ref":"root_001216/B001","relation_type":"near_synonym","shared_zone":"İki dalda da dağınık öğelerin bir araya gelmesi temel görüntüdür."},{"boundary_match":"partial","distinction":"Odak dal nicelik derecesi belirtmez; komşu dal birikimin çok ve doluluk yaratacak ölçüde olmasını çekirdek edinir.","focus_only":"Odak dal için öğelerin bir araya gelmesi yeterlidir; çokluk veya doluluk zorunlu değildir.","gloss":"toplanma ve dolacak kadar birikme","neighbor_only":"Komşu dal toplanmanın yanında çokluğu ve dolacak ölçüde birikmeyi gerektirir.","neighbor_ref":"root_000261/B001","relation_type":"near_neighbor","shared_zone":"İki dal da öğelerin aynı yerde birikmesi veya birleşmesi durumunda buluşur."}],"source_phrase_ar":"الكمثرة اجتماع الشيء؛ زيدت فيه الميم وهو من الكثرة (maqayis)","source_summary":"Tek kaynak, sözlük birimini bir şeyin bir araya toplanması diye açıklar ve yapısına eklenen m sesiyle birlikte onu çokluk anlam ailesine bağlar.","sources":["MQ"],"what_is_ar":"يدخل فيه الكمثرة بمعنى اجتماع الشيء، مع تصريح Maqāyīs بأن الميم زائدة وأنه من الكثرة.","what_is_not_ar":"ليس هو استعمالا عاديا للثلاثي كثر، ولا الجمار أو الكوثر."},"support_links":["sup_3b82aeb9a78904e1b2cd"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000148/B001","candidate_links":[{"candidate_id":"cand_6bb86eeffee062c5542d","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_cef5460be871f75a6c41","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies a delimited tract of earth; it makes the pronoun's place a civic-territorial container.","root":"ب ل د","source_ref":"89:11","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000148","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a6e7ef9ce1e78d7824b1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000273/B001","candidate_links":[{"candidate_id":"cand_cd8e56ea9766bdcc6d30","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_876364f6e29c818ac224","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies a penetrating cut; it turns hard landscape into material worked by organized force.","root":"ج و ب","source_ref":"89:9","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000273","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_28914d4edf4347ed5a28"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000296/B001","candidate_links":[{"candidate_id":"cand_6bb86eeffee062c5542d","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_cef5460be871f75a6c41","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies prevention and enclosure; it functions as the limit that should contain action.","root":"ح ج ر","source_ref":"89:5","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000296","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a6e7ef9ce1e78d7824b1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000434/B001","candidate_links":[{"candidate_id":"cand_cd8e56ea9766bdcc6d30","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_876364f6e29c818ac224","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies measuring and proportioning; it frames exceptional construction as designed capacity.","root":"خ ل ق","source_ref":"89:8","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000434","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_28914d4edf4347ed5a28"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000532/B002","candidate_links":[{"candidate_id":"cand_29f01f38cc4379d53eb4","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6d3836c5a606e0195a3e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies repair, nurture, and completion; it provides the immediate contrast to multiplied فساد.","root":"ر ب ب","source_ref":"89:13","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000532","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_af9f4368ca231d4046a8"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000697/B001","candidate_links":[{"candidate_id":"cand_9df2cf292fca9d715efd","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b1ca01f484cbf7b83147","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant split supplies concealment in an interior; it makes the movement difficult to detect.","root":"س ر ي","source_ref":"89:4","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000697","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bd6cdec99fc43409809f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000702/B002","candidate_links":[{"candidate_id":"cand_9df2cf292fca9d715efd","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b1ca01f484cbf7b83147","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies coursing or flowing movement; it makes corruption mobile within the domain.","root":"س ر ي","source_ref":"89:4","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000702","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bd6cdec99fc43409809f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000759/B001","candidate_links":[{"candidate_id":"cand_a3c00f48868034b44775","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3ebac85abf0750ef75bc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies mixing one thing with another; it mirrors corruption as an accumulated composite.","root":"س و ط","source_ref":"89:13","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000759","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3b82aeb9a78904e1b2cd"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000838/B001","candidate_links":[{"candidate_id":"cand_a3c00f48868034b44775","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3ebac85abf0750ef75bc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies pouring or discharge; it gives the response a continuous delivered form.","root":"ص ب ب","source_ref":"89:13","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000838","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3b82aeb9a78904e1b2cd"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000847/B001","candidate_links":[{"candidate_id":"cand_cd8e56ea9766bdcc6d30","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_876364f6e29c818ac224","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies massive hardness; it marks the resistant substrate overcome by that force.","root":"ص خ ر","source_ref":"89:9","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000847","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_28914d4edf4347ed5a28"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000937/B002","candidate_links":[{"candidate_id":"cand_6bb86eeffee062c5542d","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_cef5460be871f75a6c41","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies rising water and sweeping force; it gives transgression a physical overflow mechanism.","root":"ط غ ي","source_ref":"89:11","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000937","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a6e7ef9ce1e78d7824b1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000994/B005","candidate_links":[{"candidate_id":"cand_a3c00f48868034b44775","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3ebac85abf0750ef75bc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies painful penalty; it fixes the mixed discharge as punitive rather than neutral.","root":"ع ذ ب","source_ref":"89:13","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000994","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3b82aeb9a78904e1b2cd"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001043/B002","candidate_links":[{"candidate_id":"cand_cd8e56ea9766bdcc6d30","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_876364f6e29c818ac224","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies load-bearing support; it introduces built structures that can carry and reproduce power.","root":"ع م د","source_ref":"89:7","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001043","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_28914d4edf4347ed5a28"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001132/B003","candidate_links":[{"candidate_id":"cand_cc1cb52ce87311dd69dd","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e996573794b33fedd9f8","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies a sudden surge of much; it gives the roiling increase a rupture-like onset.","root":"ف ج ر","source_ref":"89:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001132","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_80f5226e49c84d776366"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001620/B003","candidate_links":[{"candidate_id":"cand_cd8e56ea9766bdcc6d30","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_876364f6e29c818ac224","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supplies stake-like fixity; it lets coercive power appear anchored and durable.","root":"و ت د","source_ref":"89:10","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001620","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_28914d4edf4347ed5a28"]}],"candidate_inventory":[{"anchor_refs":["89:12","89:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:12","branch_refs":["root_000697/B001","root_000702/B002","root_001154/B001","root_001286/B001"],"candidate_id":"cand_9df2cf292fca9d715efd","commentary_obligation":"review","hft_ref":"hft_b1ca01f484cbf7b83147","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_covert_circulation","source_type":"hft","support_ids":["sup_bd6cdec99fc43409809f"],"title":"delta_covert_circulation","trust":"legacy_unbound"},{"anchor_refs":["89:11","89:12","89:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:12","branch_refs":["root_000148/B001","root_000296/B001","root_000937/B002","root_001154/B001","root_001286/B001"],"candidate_id":"cand_6bb86eeffee062c5542d","commentary_obligation":"review","hft_ref":"hft_cef5460be871f75a6c41","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_bounded_overflow","source_type":"hft","support_ids":["sup_a6e7ef9ce1e78d7824b1"],"title":"delta_bounded_overflow","trust":"legacy_unbound"},{"anchor_refs":["89:10","89:12","89:7","89:8","89:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:12","branch_refs":["root_000273/B001","root_000434/B001","root_000847/B001","root_001043/B002","root_001154/B001","root_001286/B001","root_001620/B003"],"candidate_id":"cand_cd8e56ea9766bdcc6d30","commentary_obligation":"review","hft_ref":"hft_876364f6e29c818ac224","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_infrastructural_multiplier","source_type":"hft","support_ids":["sup_28914d4edf4347ed5a28"],"title":"delta_infrastructural_multiplier","trust":"legacy_unbound"},{"anchor_refs":["89:12","89:13"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:12","branch_refs":["root_000532/B002","root_001154/B001","root_001286/B001"],"candidate_id":"cand_29f01f38cc4379d53eb4","commentary_obligation":"review","hft_ref":"hft_6d3836c5a606e0195a3e","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_counter_cultivation","source_type":"hft","support_ids":["sup_af9f4368ca231d4046a8"],"title":"delta_counter_cultivation","trust":"legacy_unbound"},{"anchor_refs":["89:12","89:13"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:12","branch_refs":["root_000759/B001","root_000838/B001","root_000994/B005","root_001154/B001","root_001286/B007"],"candidate_id":"cand_a3c00f48868034b44775","commentary_obligation":"review","hft_ref":"hft_3ebac85abf0750ef75bc","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_mixed_recoil","source_type":"hft","support_ids":["sup_3b82aeb9a78904e1b2cd"],"title":"outlier_mixed_recoil","trust":"legacy_unbound"},{"anchor_refs":["89:1","89:12"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:12","branch_refs":["root_001132/B003","root_001154/B001","root_001286/B005"],"candidate_id":"cand_cc1cb52ce87311dd69dd","commentary_obligation":"review","hft_ref":"hft_e996573794b33fedd9f8","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_roiling_corruption","source_type":"hft","support_ids":["sup_80f5226e49c84d776366"],"title":"outlier_roiling_corruption","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_419b29f9e0054fc6b746","connection_ref":"conn_5b3b77d9f217c5903167","note":"Immediate antecedent: transgression in lands supplies the agent-and-setting frame for 89:12.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_ba98355464947c5e067a","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:11","source_note":"Directly supplies the passage's consequence: corruption multiplied there.","source_row_role":"ranked_review","source_target_component_ref":"89:12","source_target_components":["89:12"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:12"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:11","source_target_components":["89:11"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:11","target_evidence":{"arabic_uthmani":"ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ","ayah_ref":"89:11"},"target_ref":"89:11"},{"connection_evidence_ref":"conn_ev_dea4d943f8474f4b1726","connection_ref":"conn_205407cdae473af398ed","note":"Immediate sequel supplies the punishment consequence that follows 89:12, especially f03.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_89b986926e07b2732da1","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:13","source_note":"States the excess corruption that immediately precedes the scourge.","source_row_role":"ranked_review","source_target_component_ref":"89:12","source_target_components":["89:12"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:12"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:13","source_target_components":["89:13"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:13","target_evidence":{"arabic_uthmani":"فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ","ayah_ref":"89:13"},"target_ref":"89:13"},{"connection_evidence_ref":"conn_ev_ae3f62836f9de961cdc9","connection_ref":"conn_4d3eedea3bd7dc4607ea","note":"Local opening contributes only a broad frame; the reviewed hidden-corruption channel remains indirect.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_7c94c3cf8cd31c372cac","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:1","source_note":"Local corruption gives the ethical boundary-breaking side of f02.","source_row_role":"ranked_review","source_target_component_ref":"89:12","source_target_components":["89:12"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:12"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:1","source_target_components":["89:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:1","target_evidence":{"arabic_uthmani":"وَٱلْفَجْرِ","ayah_ref":"89:1"},"target_ref":"89:1"},{"connection_evidence_ref":"conn_ev_da74f6b8e5fc53dfbb8b","connection_ref":"conn_074bde658e24f6b4f6b8","note":"Immediate local surveillance statement frames the accountability that follows the corrupting exemplars.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_e7a393f589c18bef7ce4","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:14","source_note":"Names the corruption in the local account that explains the ensuing response.","source_row_role":"ranked_review","source_target_component_ref":"89:12","source_target_components":["89:12"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:12"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:14","source_target_components":["89:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:14","target_evidence":{"arabic_uthmani":"إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ","ayah_ref":"89:14"},"target_ref":"89:14"},{"connection_evidence_ref":"conn_ev_a6cbe82a7a16de32693b","connection_ref":"conn_2680ed51ec6dc4823618","note":"Immediate identification of Iram helps locate the exemplary land in the 89:6-14 sequence.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_854d0d1a0d992c9d036c","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:7","source_note":"Completes the accusation against the groups introduced around 89:7.","source_row_role":"ranked_review","source_target_component_ref":"89:12","source_target_components":["89:12"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:12"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:7","source_target_components":["89:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:7","target_evidence":{"arabic_uthmani":"إِرَمَ ذَاتِ ٱلْعِمَادِ","ayah_ref":"89:7"},"target_ref":"89:7"},{"connection_evidence_ref":"conn_ev_4fed44f25c68702b7503","connection_ref":"conn_04159e67fc6c7b373a7d","note":"Local uniqueness statement adds little to the meaning of فساد.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_7a44a31108b62b2e5890","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:8","source_note":"Immediate consequence supplies the corruption that gives the Iram account its warning force.","source_row_role":"ranked_review","source_target_component_ref":"89:12","source_target_components":["89:12"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:12"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:8","source_target_components":["89:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:8","target_evidence":{"arabic_uthmani":"ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ","ayah_ref":"89:8"},"target_ref":"89:8"},{"connection_evidence_ref":"conn_ev_8362fd457b26c38dd5c0","connection_ref":"conn_d300fb9ede63095da5f2","note":"Immediate Pharaoh exemplar supplies a named power frame for the corruption in 89:12.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_7c442a7b14955db0123d","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:10","source_note":"Immediate continuation specifies the corruption associated with the rulers.","source_row_role":"ranked_review","source_target_component_ref":"89:12","source_target_components":["89:12"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:12"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:10","source_target_components":["89:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:10","target_evidence":{"arabic_uthmani":"وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ","ayah_ref":"89:10"},"target_ref":"89:10"},{"connection_evidence_ref":"conn_ev_40b0b8300b8aaf8cf720","connection_ref":"conn_dd8d3b8699298e14940e","note":"Immediate mention of 'Ad begins the historical exemplars whose actions culminate in 89:12.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_53bf3438dee395930878","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"89:6","source_note":"Completes the local diagnosis: the named peoples multiplied corruption in the lands.","source_row_role":"ranked_review","source_target_component_ref":"89:12","source_target_components":["89:12"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:12"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:6","source_target_components":["89:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:6","target_evidence":{"arabic_uthmani":"أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ","ayah_ref":"89:6"},"target_ref":"89:6"},{"connection_ref":"conn_964723404077bcab4b5f","note":null,"origin":"derived_reciprocal_seed","prior_label":null,"qualification":{"boundary":"At least one source-direction review meaningfully linked this target back to the focus ayah. Treat its note and label only as a discovery nomination. Reassess the relation from the focus ayah using the supplied exact target Arabic; do not invent missing target morphology or inherit the source label.","derived_reciprocal_counterevidence":false,"derived_reciprocal_seed":true,"has_missing_ayah_suggestion_source_row":true,"has_ranked_review_source_row":false,"has_reciprocal_counterevidence":false,"has_reciprocal_nomination":true,"receiving_direction_requires_fresh_assessment":true,"source_direction_labels_are_not_focus_decisions":true,"source_row_roles_are_provenance_not_decisions":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_c40de8933e5e7ede8519","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:9","source_note":"Immediate continuation identifies the resulting corruption in lands.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"89:12","source_target_components":["89:12"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:12"}],"relation_scope":"declared_pericope_reciprocal_evidence","target_evidence":{"arabic_uthmani":"وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ","ayah_ref":"89:9"},"target_ref":"89:9"}],"focus":{"arabic_uthmani":"فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:12:1:1","qac_word_ref":"89:12:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أَكْثَرُ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>akovaru|ROOT:kvr|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:12:1:2","qac_word_ref":"89:12:1","root_ar":"ك ث ر","surface_ar":"أَكْثَرُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:12:1:3","qac_word_ref":"89:12:1","root_ar":"","surface_ar":"وا۟"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"89:12:2:1","qac_word_ref":"89:12:2","root_ar":"","surface_ar":"فِي"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:12:2:2","qac_word_ref":"89:12:2","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:12:3:1","qac_word_ref":"89:12:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"فَسَاد","morph_features":"STEM|POS:N|LEM:fasaAd|ROOT:fsd|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:12:3:2","qac_word_ref":"89:12:3","root_ar":"ف س د","surface_ar":"فَسَادَ"}],"word_analysis_qac_refs":[["89:12:1:1"],["89:12:1:2","89:12:1:3"],["89:12:2:1","89:12:2:2"],["89:12:3:1","89:12:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:12:1","89:12:2","89:12:3","89:12:4"]},"focus_surface_evidence":{"arabic_uthmani":"فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:12:1:1","qac_word_ref":"89:12:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أَكْثَرُ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>akovaru|ROOT:kvr|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:12:1:2","qac_word_ref":"89:12:1","root_ar":"ك ث ر","surface_ar":"أَكْثَرُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:12:1:3","qac_word_ref":"89:12:1","root_ar":"","surface_ar":"وا۟"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"89:12:2:1","qac_word_ref":"89:12:2","root_ar":"","surface_ar":"فِي"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:12:2:2","qac_word_ref":"89:12:2","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:12:3:1","qac_word_ref":"89:12:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"فَسَاد","morph_features":"STEM|POS:N|LEM:fasaAd|ROOT:fsd|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:12:3:2","qac_word_ref":"89:12:3","root_ar":"ف س د","surface_ar":"فَسَادَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:12:1:1"],["89:12:1:2","89:12:1:3"],["89:12:2:1","89:12:2:2"],["89:12:3:1","89:12:3:2"]],"word_analysis_refs":["89:12:1","89:12:2","89:12:3","89:12:4"],"word_rows":[{"analysis_record_ref":"89:12:1","analytic_gloss_range_en":"resultive and sequential conjunction that launches the clause as consequence of the prior transgression","analytic_root_gloss_range_en":null,"qac_refs":["89:12:1:1"],"root":{},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"89:12:2","analytic_gloss_range_en":"Form IV completed plural action of making much, doing much, or causing abundance, locally aimed at the explicit object of corruption","analytic_root_gloss_range_en":"abundance, manyness, increase, rivalry in plenty, and special plenitude; the local Form IV verb selects caused or repeated increase rather than every root branch","qac_refs":["89:12:1:2","89:12:1:3"],"root":{"arabic":"ك ث ر","transliteration":"k-th-r"},"surface":{"arabic":"أَكْثَرُوا۟","transliteration":"aktharū"}},{"analysis_record_ref":"89:12:3","analytic_gloss_range_en":"preposition plus third feminine singular suffix, resuming the prior lands as the interior domain of multiplied corruption","analytic_root_gloss_range_en":null,"qac_refs":["89:12:2:1","89:12:2:2"],"root":{},"surface":{"arabic":"فِيهَا","transliteration":"fīhā"}},{"analysis_record_ref":"89:12:4","analytic_gloss_range_en":"definite accusative verbal noun naming the known category and accumulated product of corruption as the object made abundant","analytic_root_gloss_range_en":"corruption as loss of soundness, spoilage, disorder, ruin, and opposition to repair; local noun form gathers these registers as the product, while derivative verbs remain background family pressure","qac_refs":["89:12:3:1","89:12:3:2"],"root":{"arabic":"ف س د","transliteration":"f-s-d"},"surface":{"arabic":"ٱلْفَسَادَ","transliteration":"al-fasāda"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":10,"missing_anchor_refs":[],"supplied_unique_anchor_count":10},"assigned_record_count":6,"assigned_records":[{"anchor_refs":["89:12","89:4"],"branch_refs":["root_000697/B001","root_000702/B002","root_001154/B001","root_001286/B001"],"candidate_id":"cand_9df2cf292fca9d715efd","evidence_scope":"declared_pericope","hft_ref":"hft_b1ca01f484cbf7b83147","item_id":"delta_covert_circulation","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_covert_circulation","support_id":"sup_bd6cdec99fc43409809f"},{"anchor_refs":["89:11","89:12","89:5"],"branch_refs":["root_000148/B001","root_000296/B001","root_000937/B002","root_001154/B001","root_001286/B001"],"candidate_id":"cand_6bb86eeffee062c5542d","evidence_scope":"declared_pericope","hft_ref":"hft_cef5460be871f75a6c41","item_id":"delta_bounded_overflow","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_bounded_overflow","support_id":"sup_a6e7ef9ce1e78d7824b1"},{"anchor_refs":["89:10","89:12","89:7","89:8","89:9"],"branch_refs":["root_000273/B001","root_000434/B001","root_000847/B001","root_001043/B002","root_001154/B001","root_001286/B001","root_001620/B003"],"candidate_id":"cand_cd8e56ea9766bdcc6d30","evidence_scope":"declared_pericope","hft_ref":"hft_876364f6e29c818ac224","item_id":"delta_infrastructural_multiplier","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_infrastructural_multiplier","support_id":"sup_28914d4edf4347ed5a28"},{"anchor_refs":["89:12","89:13"],"branch_refs":["root_000532/B002","root_001154/B001","root_001286/B001"],"candidate_id":"cand_29f01f38cc4379d53eb4","evidence_scope":"declared_pericope","hft_ref":"hft_6d3836c5a606e0195a3e","item_id":"delta_counter_cultivation","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_counter_cultivation","support_id":"sup_af9f4368ca231d4046a8"},{"anchor_refs":["89:12","89:13"],"branch_refs":["root_000759/B001","root_000838/B001","root_000994/B005","root_001154/B001","root_001286/B007"],"candidate_id":"cand_a3c00f48868034b44775","evidence_scope":"declared_pericope","hft_ref":"hft_3ebac85abf0750ef75bc","item_id":"outlier_mixed_recoil","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_mixed_recoil","support_id":"sup_3b82aeb9a78904e1b2cd"},{"anchor_refs":["89:1","89:12"],"branch_refs":["root_001132/B003","root_001154/B001","root_001286/B005"],"candidate_id":"cand_cc1cb52ce87311dd69dd","evidence_scope":"declared_pericope","hft_ref":"hft_e996573794b33fedd9f8","item_id":"outlier_roiling_corruption","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_roiling_corruption","support_id":"sup_80f5226e49c84d776366"}],"diagnostics":[],"lane_counts":{"global":13,"macro":6,"micro":3},"packet_summary":{"ayah_count":30,"focus_ref":"89:12","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:12","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"89:12","lane":"macro","linguistic_source_ref":"89:12","surface_ref":"89:12","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:12","target_tokens":[["Böylece",["89:12:1"]],["oralarda",["89:12:2"]],["bozgunculuğu",["89:12:3"]],["artırdılar",["89:12:1"]]],"text":"Böylece oralarda bozgunculuğu artırdılar."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":6,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":14,"id":"s089-p01-001-014","label":"Oaths and the downfall of tyrants","number":1,"refs":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"89:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"89:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["89:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"89:0"}],"support_registry":[{"anchor_evidence":[{"arabic_uthmani":"فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ","ayah_ref":"89:12"},{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَسْرِ","ayah_ref":"89:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000697/B001","root_000702/B002","root_001154/B001","root_001286/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001286","role":"Supplies proliferation; it gives the concealed current repeated reach.","root":"ك ث ر","source_ref":"89:12","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001154","role":"Supplies the spreading loss of soundness to which the current leads.","root":"ف س د","source_ref":"89:12","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000702","role":"Supplies coursing or flowing movement; it makes corruption mobile within the domain.","root":"س ر ي","source_ref":"89:4","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000697","role":"The non-dominant split supplies concealment in an interior; it makes the movement difficult to detect.","root":"س ر ي","source_ref":"89:4","source_word_indices":["3"]}],"changed_reading":{"after":"Corruption multiplied by circulating through the place's hidden interiors, spreading before it became publicly legible.","before":"Corruption became numerous in a place."},"confidence":"exploratory","mechanism":"The split inventory permits night-motion or coursing and hidden interiority to cooperate: multiplied فساد becomes a concealed current moving through the domain rather than a static pile of acts.","model_id":"delta_covert_circulation","reader_inference":"The packet supplies nocturnal motion or current and, through the non-dominant split mapping, hidden interiority; I infer covert circulation of the increased فساد. A live alternative keeps يَسْرِ as temporal passage only, with no clandestine social mechanism.","status":"revised","structural_cues":["89:4 places movement inside night, and 89:2 has already pluralized nights, giving concealment both motion and recurrence."],"trigger_roots":["س ر ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_covert_circulation","source_type":"hft","support_id":"sup_bd6cdec99fc43409809f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ","ayah_ref":"89:11"},{"arabic_uthmani":"فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ","ayah_ref":"89:12"},{"arabic_uthmani":"هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ","ayah_ref":"89:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000148/B001","root_000296/B001","root_000937/B002","root_001154/B001","root_001286/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001286","role":"Supplies quantitative growth; it turns a breach into sustained saturation.","root":"ك ث ر","source_ref":"89:12","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001154","role":"Supplies departure from balance; it names the condition left inside the breached domain.","root":"ف س د","source_ref":"89:12","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000296","role":"Supplies prevention and enclosure; it functions as the limit that should contain action.","root":"ح ج ر","source_ref":"89:5","source_word_indices":["6"]},{"branch_id":"B001","mapped_root_id":"root_000148","role":"Supplies a delimited tract of earth; it makes the pronoun's place a civic-territorial container.","root":"ب ل د","source_ref":"89:11","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000937","role":"Supplies rising water and sweeping force; it gives transgression a physical overflow mechanism.","root":"ط غ ي","source_ref":"89:11","source_word_indices":["2"]}],"changed_reading":{"after":"They drove a bounded social-land system past its containing limits, making imbalance overflow and occupy its interior.","before":"They did many bad things in the lands."},"confidence":"strong","mechanism":"A bounded land with a restraining barrier is subjected to limit-crossing force figured as overflowing water; فِيهَا then marks the container whose internal balance is saturated and breached.","model_id":"delta_bounded_overflow","reader_inference":"The packet supplies enclosure, bounded land, and sweeping overflow; I infer that repeated limit-crossing saturates a civic ecology until it loses balance. The live alternative is a purely juridical sequence of transgression and sin without a spatial-pressure model.","status":"strengthened","structural_cues":["The shared locative pattern فِى ٱلْبِلَادِ in 89:11 and فِيهَا in 89:12 makes the land the receiving interior.","The sequence moves from restraint in 89:5 to overflow in 89:11 and multiplied imbalance in 89:12."],"trigger_roots":["ح ج ر","ب ل د","ط غ ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_bounded_overflow","source_type":"hft","support_id":"sup_a6e7ef9ce1e78d7824b1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ","ayah_ref":"89:10"},{"arabic_uthmani":"فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ","ayah_ref":"89:12"},{"arabic_uthmani":"إِرَمَ ذَاتِ ٱلْعِمَادِ","ayah_ref":"89:7"},{"arabic_uthmani":"ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ","ayah_ref":"89:8"},{"arabic_uthmani":"وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ","ayah_ref":"89:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":5,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":5,"target_morphology_supplied":false},"branch_refs":["root_000273/B001","root_000434/B001","root_000847/B001","root_001043/B002","root_001154/B001","root_001286/B001","root_001620/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001286","role":"Supplies scaling; it makes technical capacity a multiplier rather than a neutral possession.","root":"ك ث ر","source_ref":"89:12","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001154","role":"Supplies structural loss of soundness as the outcome of scaled power.","root":"ف س د","source_ref":"89:12","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001043","role":"Supplies load-bearing support; it introduces built structures that can carry and reproduce power.","root":"ع م د","source_ref":"89:7","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000434","role":"Supplies measuring and proportioning; it frames exceptional construction as designed capacity.","root":"خ ل ق","source_ref":"89:8","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000273","role":"Supplies a penetrating cut; it turns hard landscape into material worked by organized force.","root":"ج و ب","source_ref":"89:9","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000847","role":"Supplies massive hardness; it marks the resistant substrate overcome by that force.","root":"ص خ ر","source_ref":"89:9","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_001620","role":"Supplies stake-like fixity; it lets coercive power appear anchored and durable.","root":"و ت د","source_ref":"89:10","source_word_indices":["3"]}],"changed_reading":{"after":"Their organized material capacity let corruption become infrastructural, durable, and reproducible across the land.","before":"Powerful peoples happened to commit many corrupt acts."},"confidence":"medium","mechanism":"Supports, measured making, penetrative rock-cutting, resistant substrate, and fixed stakes form a chain of engineered capacity. Such capacity can multiply فساد by embedding domination in durable structures rather than leaving it at the level of individual acts.","model_id":"delta_infrastructural_multiplier","reader_inference":"The packet supplies a sequence of support, design, cutting, hardness, and fixation; I infer that technical achievements become channels that scale domination. A live alternative treats the structures only as emblems of might, with no claim that building or excavation is itself corrupt.","status":"new","structural_cues":["89:7-10 moves through pillars, unprecedented making, rock-cutting, and stakes before naming overflow and multiplied corruption.","The branchless ك ي ف at 89:6 is used only as a structural manner-question that invites attention to how the power operated."],"trigger_roots":["ع م د","خ ل ق","ج و ب","ص خ ر","و ت د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_infrastructural_multiplier","source_type":"hft","support_id":"sup_28914d4edf4347ed5a28","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ","ayah_ref":"89:12"},{"arabic_uthmani":"فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ","ayah_ref":"89:13"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000532/B002","root_001154/B001","root_001286/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001286","role":"Supplies deliberate increase; it gives anti-repair a productive, scaling action.","root":"ك ث ر","source_ref":"89:12","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001154","role":"Supplies the opposite of soundness and repair; it is the damaged trajectory being cultivated.","root":"ف س د","source_ref":"89:12","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000532","role":"Supplies repair, nurture, and completion; it provides the immediate contrast to multiplied فساد.","root":"ر ب ب","source_ref":"89:13","source_word_indices":["3"]}],"changed_reading":{"after":"They practiced a counter-cultivation, scaling the forces that keep a society from becoming sound or complete.","before":"They increased damage under a sovereign's watch."},"confidence":"medium","mechanism":"The repair, nurture, and completion branch surrounding the focus makes multiplied فساد readable as organized anti-repair: the agents increase whatever prevents the domain from reaching sound completion.","model_id":"delta_counter_cultivation","reader_inference":"The packet supplies فساد as unsoundness and ر ب ب as repair or completion; I infer a reversal in which the agents systematically cultivate non-repair. The live alternative activates only sovereignty in ر ب ب and leaves the focus as an ordinary report of corruption.","status":"revised","structural_cues":["The ر ب ب cue recurs before and after the focus at 89:6, 89:13, and 89:14, enclosing the agents' multiplication within a contrasting governance frame."],"trigger_roots":["ر ب ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_counter_cultivation","source_type":"hft","support_id":"sup_af9f4368ca231d4046a8","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ","ayah_ref":"89:12"},{"arabic_uthmani":"فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ","ayah_ref":"89:13"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000759/B001","root_000838/B001","root_000994/B005","root_001154/B001","root_001286/B007"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_001286","role":"Supplies gathering into a cluster; it permits corruption to be composite rather than homogeneous.","root":"ك ث ر","source_ref":"89:12","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001154","role":"Supplies the unsound result shared by the heterogeneous components.","root":"ف س د","source_ref":"89:12","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000838","role":"Supplies pouring or discharge; it gives the response a continuous delivered form.","root":"ص ب ب","source_ref":"89:13","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000759","role":"Supplies mixing one thing with another; it mirrors corruption as an accumulated composite.","root":"س و ط","source_ref":"89:13","source_word_indices":["4"]},{"branch_id":"B005","mapped_root_id":"root_000994","role":"Supplies painful penalty; it fixes the mixed discharge as punitive rather than neutral.","root":"ع ذ ب","source_ref":"89:13","source_word_indices":["5"]}],"changed_reading":{"after":"They gathered heterogeneous corruptions into one failed system, and the next ayah imagistically answers that composite with a poured mixture of penalty.","before":"Corruption is one undifferentiated excess answered by punishment."},"confidence":"exploratory","containment":"This is surprising because it reads 89:13 backward through the non-obvious mixing branch of س و ط; it remains anchored in the focus's clustering and فساد, but downstream prose should present it as a compositional analogy, not a lexical gloss of either corruption or punishment.","focus_anchor":"The clustered increase of أَكْثَرُوا ٱلْفَسَادَ can be tested against the immediately following poured, mixed punitive image.","outlier_id":"outlier_mixed_recoil"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_mixed_recoil","source_type":"hft","support_id":"sup_3b82aeb9a78904e1b2cd","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْفَجْرِ","ayah_ref":"89:1"},{"arabic_uthmani":"فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ","ayah_ref":"89:12"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_001132/B003","root_001154/B001","root_001286/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001286","role":"Supplies abundant dust rising and roiling; it models multiplication as turbulent spread that also obscures.","root":"ك ث ر","source_ref":"89:12","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001154","role":"Supplies departure from balance; it makes the turbulence damaging rather than merely atmospheric.","root":"ف س د","source_ref":"89:12","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001132","role":"Supplies a sudden surge of much; it gives the roiling increase a rupture-like onset.","root":"ف ج ر","source_ref":"89:1","source_word_indices":["1"]}],"changed_reading":{"after":"Corruption surged like a roiling cloud, filling the domain, spreading through motion, and obscuring the conditions needed for correction.","before":"Corruption increased as countable acts."},"confidence":"exploratory","containment":"The dust image is materially distant from the surface syntax, but it is a supplied branch of the focus verb and remains joined to فساد as loss of balance; prose should qualify this as a sensory model of spread and obscuration, never as the word's direct translation.","focus_anchor":"The focus root ك ث ر itself supplies a roiling-dust branch, while فِيهَا gives that disturbed material a place to fill.","outlier_id":"outlier_roiling_corruption"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_roiling_corruption","source_type":"hft","support_id":"sup_80f5226e49c84d776366","trust":"legacy_unbound"}]}
</lane_packet_json>
