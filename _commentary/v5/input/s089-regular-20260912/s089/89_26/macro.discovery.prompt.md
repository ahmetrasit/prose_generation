# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **89:26**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_26/macro.discovery.json` and modify nothing
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
  "ayah_ref": "89:26",
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
{"branch_registry":[{"boundary":"Bu dal tekliği ve eşsizliği anlatır; olumsuzlukta kişi kapsamını, onlu sayı kuruluşlarını, gün adını ve dağ adını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:26:4:1","qac_word_ref":"89:26:4","surface_ar":"أَحَدٌ"}],"gloss":"tek ve eşi olmayan olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığı bir tane, tek veya eşi bulunmayan olarak gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Mutlak niteleme olarak kullanıldığında Tanrı'nın ortağı ve benzeri bulunmadığını bildirir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı sözün art arda yinelenmesi tek olma bildirimini pekiştirir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kaynak ifadesi sözcüğü saymanın başlangıcındaki bir sayısıyla da ilişkilendirir; düzenli sayı kuruluşları ayrı dalda ele alınır."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek olma çekirdeğini, mutlak eşsizliği ve yinelemeli pekiştirmeyi birlikte temsil eden dal düzeyi karşılıktır.","boundary_detail":"Bu dal tekliği ve eşsizliği anlatır; olumsuzlukta kişi kapsamını, onlu sayı kuruluşlarını, gün adını ve dağ adını kapsamaz.","branch_image_ar":"الأَحَدِيَّة والوَحْدَة","concept_gloss":"tek ve eşi olmayan olma","contextual_glosses":[{"applicability":"Sayılabilir bir varlığın tek örnek olduğunu bildiren genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mutlak eşsizlik ile yinelemeli pekiştirme yüzlerini taşımaz.","preserves":"Bir tane olma çekirdeğini korur."},"facet_ids":["F001","F004"],"text":"bir tane","usage_role":"contextual"},{"applicability":"Tanrı'nın ortağı ve benzeri olmadığını bildiren mutlak niteleme bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel sayısal birliği ve yinelemeli söyleyiş biçimini kapsamaz.","preserves":"Mutlak tekliği ve eşsizliği korur."},"facet_ids":["F002"],"text":"tek ve eşsiz","usage_role":"contextual"},{"applicability":"Teklik bildiren sözün yinelenerek güçlü biçimde vurgulandığı söyleyiş için açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yinelenmeyen genel kullanımın bütün kapsamını taşımaz.","preserves":"Yineleme yoluyla yapılan tek olma vurgusunu korur."},"facet_ids":["F003"],"text":"yalnız bir, yalnız bir","usage_role":"explanatory"}],"definition":"Bir varlığın bir tane, tek ya da eşi olmayan olmasıdır; mutlak kullanımda Tanrı'nın ortağı ve benzeri bulunmadığını bildirir. Sözcüğün yinelenmesi bu tekliği güçlü biçimde vurgular.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığı bir tane, tek veya eşi bulunmayan olarak gösterir."},{"facet_id":"F002","role":"specialization","statement":"Mutlak niteleme olarak kullanıldığında Tanrı'nın ortağı ve benzeri bulunmadığını bildirir."},{"facet_id":"F003","role":"associated_use","statement":"Aynı sözün art arda yinelenmesi tek olma bildirimini pekiştirir."},{"facet_id":"F004","role":"source_variant","statement":"Kaynak ifadesi sözcüğü saymanın başlangıcındaki bir sayısıyla da ilişkilendirir; düzenli sayı kuruluşları ayrı dalda ele alınır."}],"identity_rationale":"Kaynak ifadesi tek olma, mutlak biçimde eşsiz sayılma ve yinelemeyle bu niteliği pekiştirme çekirdeğini destekler. Aynı ifade saymanın ilk basamağına da değindiği için dal korunabilir, ancak düzenli sayı kurma kullanımları ayrı sayı dalına bırakılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir tane; tek ve eşsiz"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yalnız bir, yalnız bir"}],"lexicalization_note":"Tanım yalın biçimdeki tek olma anlamını ve yinelemeli pekiştirmeyi ayrı yüzler olarak tutar; yinelemeyi yalın biçimin zorunlu anlamı yapmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en güçlü sınırlar mutlak birlik, alana bağlı eşsizlik, sayısal bir ve tek başına kalma dallarıyla kuruldu, kalanlar yalnız uzak konu ortaklığı taşıdığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yalnız Tanrı'nın birliği çevresinde kuruludur; odak dal ise genel tek olmayı ve yinelemeli vurguyu da taşıdığı için bütünüyle onun yerine geçmez.","focus_only":"Odak dal genel tekliği, sayı başlangıcına değen kullanımı ve yinelemeli pekiştirmeyi de içerir.","gloss":"Tanrı'nın ortak ve benzerden uzak tekliği","neighbor_only":"Komşu dal Tanrı'nın birliği inancını, ortak bulunmamasını ve bölünmezliği daha geniş bir inanç alanı olarak işler.","neighbor_ref":"root_001631/B004","relation_type":"near_synonym","shared_zone":"İki dal da Tanrı için mutlak tekliği ve ortak bulunmamasını bildirir."},{"boundary_match":"partial","distinction":"Odak dalın tekliği varlığın bir tane veya mutlak eşsiz olmasıdır; komşu dalın eşsizliği ise belirli bir nitelik alanındaki karşılaştırmaya bağlıdır.","focus_only":"Odak dal sayısal birlik ve mutlak tek olma bildirebilir.","gloss":"belirli bir alanda benzeri bulunmayan","neighbor_only":"Komşu dal belirli bir üstünlük ya da kötülük alanında benzeri bulunmayan kişiyi anlatır.","neighbor_ref":"root_001240/B018","relation_type":"near_synonym","shared_zone":"İki dal da eş ya da benzer bulunmaması düşüncesinde buluşur."},{"boundary_match":"partial","distinction":"Odak dal nitelik olarak tekliği merkez alır; komşu dal ise birin sayı dizisindeki ve birleşik sayılardaki görevini merkez alır.","focus_only":"Odak dal varlığın tek ve eşi olmayan oluşunu, ayrıca bu niteliğin vurgulanmasını anlatır.","gloss":"bir sayısı ve onlu sayı kuruluşları","neighbor_only":"Komşu dal sayma dizisini, onlu sayı kuruluşlarını ve bir kümeyi on bire çıkarma işlemini kapsar.","neighbor_ref":"root_000017/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir tane olma düşüncesi ve sayının ilk basamağıyla bağ vardır."},{"boundary_match":"partial","distinction":"Odak dal bir nitelik bildirirken komşu dal tek başına kalma ya da ayrı ayrı hareket etme sürecini ve sonucunu bildirir.","focus_only":"Odak dal bir varlığın tek ya da eşsiz olma niteliğini bildirir.","gloss":"tek başına kalma ve birer birer dağılma","neighbor_only":"Komşu dal kişinin tek başına kalması veya bir topluluğun birer birer gelmesi gibi değişme ve dağılım olaylarını bildirir.","neighbor_ref":"root_000017/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da birlikten veya topluluktan ayrı tek olma görünümüne dokunur."}],"source_phrase_ar":"أحد فرع والأصل الواو وحد (maqayis); أحد بمعنى الواحد وهو أول العدد (sihah); قل هو الله أحد (sihah;mufradat); يستعمل مطلقا وصفا في وصف الله تعالى وأصله وحد (mufradat); أحد أحد (sihah)","source_summary":"Kaynakların ortak çizgisi tek olma düşüncesidir. Bu çizgi genel olarak bir tane olmayı, Tanrı için mutlak eşsizliği ve yineleme yoluyla yapılan güçlü vurguyu bir araya getirir; sayı başlangıcına ilişkin kayıt ise komşu sayı dalıyla sınır oluşturur.","sources":["MQ","SI","MU"],"what_is_ar":"أحد بمعنى الواحد، والوصف المطلق بأحد، وتكرار أحد أحد للتأكيد","what_is_not_ar":"ليس نفي الجنس ولا أحد عشر ولا يوم الأحد ولا جبل أُحُد"},"support_links":[]},{"boundary":"Bu dal yalnız olumsuz bağlamdaki kişi kapsamıdır; olumlu tekliği, sayı kuruluşlarını, gün adını ve dağ adını içermez.","branch_kind":"bare","branch_ref":"root_000017/B002","candidate_links":[{"candidate_id":"cand_00b2bfe089da4b527c3f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:26:4:1","qac_word_ref":"89:26:4","surface_ar":"أَحَدٌ"}],"gloss":"hiç kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olumsuzluk altında konuşmaya konu olabilecek kişiler türünün tamamını kapsar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin yanı sıra iki veya daha çok kişinin varlığını ya da katılımını da dışlar."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yerde hiç kimsenin bulunmadığını veya bir eylemi hiç kimsenin yapmadığını söyleyen cümlelerde gerçekleşir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Olumsuzluk altında kişi türünün tamamını, sayı ayrımı yapmadan dışlayan doğal dal karşılığıdır.","boundary_detail":"Bu dal yalnız olumsuz bağlamdaki kişi kapsamıdır; olumlu tekliği, sayı kuruluşlarını, gün adını ve dağ adını içermez.","branch_image_ar":"استغراق النفي","concept_gloss":"hiç kimse","contextual_glosses":[{"applicability":"Bir yerde kişi bulunmadığını bildiren varlık cümlelerinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir eyleme katılmama gibi yer bildirmeyen olumsuz bağlamları kapsamaz.","preserves":"Kişilerin tümünü olumsuzluk altında dışlama kapsamını korur."},"facet_ids":["F001","F002","F003"],"text":"hiç kimse yok","usage_role":"contextual"},{"applicability":"Belirli bir insan topluluğunun hiçbir üyesinin eyleme katılmadığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Belirsiz bir yerde insan bulunmaması gibi topluluğu belirtilmeyen bağlamları kapsamaz.","preserves":"Belirli bir topluluğun bütün üyelerini olumsuzluk kapsamına alır."},"facet_ids":["F001","F002"],"text":"aranızdan hiç kimse","usage_role":"contextual"}],"definition":"Olumsuz bir cümlede, söz konusu olabilecek kişilerden bir tekinin bile bulunmadığını ya da eyleme katılmadığını bildirir. Kapsam yalnız bir kişiyi değil, iki ve daha çok kişiyi de dışarıda bırakır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olumsuzluk altında konuşmaya konu olabilecek kişiler türünün tamamını kapsar."},{"facet_id":"F002","role":"specialization","statement":"Bir kişinin yanı sıra iki veya daha çok kişinin varlığını ya da katılımını da dışlar."},{"facet_id":"F003","role":"example","statement":"Bir yerde hiç kimsenin bulunmadığını veya bir eylemi hiç kimsenin yapmadığını söyleyen cümlelerde gerçekleşir."}],"identity_rationale":"Kaynak ifadesi, sözcüğün olumsuzluk içinde konuşmaya konu olabilecek kişilerin bütün türünü kapsadığını ve yalnız tek kişiyi değil iki ya da daha çok kişiyi de dışladığını açıkça belirtir. Hazırlanan dal çerçevesi bu kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"olumsuzlukta hiç kimse"}],"lexicalization_note":"Tanım yalın birimin olumsuz cümledeki kapsamına bağlıdır ve başka bir söz öbeğine özgü anlamı bu dala taşımaz.","neighbor_coverage_note":"Adayların tümü gözden geçirildi; yer boşluğunu bildiren kalıplar, daha geniş yokluk kalıbı ve olumlu teklik dalı okur açısından en yararlı karşıtlıkları verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişi türünü olumsuzlukla kapsayan genel birimdir; komşu dal ise belirli kalıplaşmış sözlerle yerin boşluğunu, bazen de iz yokluğunu anlatır.","focus_only":"Odak dal olumsuzluk altında kişi türünün tamamını düzenli bir dil bilgisel kapsamla dışlar.","gloss":"bir yerde kimse ya da iz bulunmaması","neighbor_only":"Komşu dal, bir yerde insanın ya da kimi kullanımlarda herhangi bir izin bulunmadığını bildiren kalıplaşmış sözleri kapsar.","neighbor_ref":"root_000075/B008","relation_type":"near_neighbor","shared_zone":"İki dal da bir yerde kişinin bulunmadığını söyleyebilir."},{"boundary_match":"partial","distinction":"Odak dalın alanı kişilerdir; komşu dalın kalıplaşmış kullanımı kişi dışındaki şeylere ve suya kadar genişleyebilir.","focus_only":"Odak dal yalnız konuşmaya konu olabilecek kişilerin tümünü dışlar.","gloss":"en küçük kişi ya da şeyin bile yokluğu","neighbor_only":"Komşu dal kalıplaşmış bir sözle kişi, herhangi bir şey veya su gibi farklı varlıkların en küçüğünü bile dışlayabilir.","neighbor_ref":"root_000187/B005","relation_type":"near_neighbor","shared_zone":"İki dal da olumsuzlukta en küçük bir örneğin bile bulunmadığını bildirebilir."},{"boundary_match":"partial","distinction":"Odak dalın anlamı olumsuzluk ve bütün kişileri kapsama koşuluna bağlıdır; komşu dal olumlu tekliği veya eşsizliği anlatır.","focus_only":"Odak dal olumsuzluk altında herhangi bir kişinin varlığını ya da katılımını dışlar.","gloss":"bir tane, tek ve eşsiz","neighbor_only":"Komşu dal olumlu biçimde bir tane, tek veya eşi olmayan olmayı bildirir.","neighbor_ref":"root_000017/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın biçiminde bir kişiye ya da varlığa ilişkin birlik düşüncesi bulunur."}],"source_phrase_ar":"لا أحد في الدار؛ ما في الدار أحد (sihah); أحد في النفي لاستغراق جنس الناطقين ولا واحد ولا اثنان فصاعدا (mufradat); فما منكم من أحد عنه حاجزين (sihah;mufradat)","source_summary":"Kaynaklar olumsuzluk içindeki kullanımın kişi türünü bütünüyle kapsadığı konusunda birleşir. Böylece söz yalnız tek bir kişinin yokluğunu değil, o türe giren herhangi bir sayıda kişinin bulunmamasını da bildirir.","sources":["SI","MU"],"what_is_ar":"أحد في سياق النفي لاستغراق جنس من يصلح أن يخاطب، فيشمل الواحد وما فوقه","what_is_not_ar":"ليس إثبات الواحد ولا العدد المركب ولا علم الجبل"},"support_links":["sup_fbcbd48c4bdefe125457"]},{"boundary":"Bu dal sayı ve sayı kurma alanındadır; olumsuz kişi kapsamını, mutlak eşsizliği, gün adını ve özel dağ adını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:26:4:1","qac_word_ref":"89:26:4","surface_ar":"أَحَدٌ"}],"gloss":"bir sayısı, onlu kuruluşları ve on bire çıkarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sayma dizisinin başlangıcındaki bir sayısını bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir sayısı on veya yirmi gibi onluklarla birleşerek on bir ve yirmi bir türü sayıları kurar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eylem biçimi, bir topluluğun sayısını on bire çıkarma işlemini bildirir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın sayıyı, onluklarla kurulan sayı biçimlerini ve on bire çıkarma eylemini birlikte temsil eder.","boundary_detail":"Bu dal sayı ve sayı kurma alanındadır; olumsuz kişi kapsamını, mutlak eşsizliği, gün adını ve özel dağ adını içermez.","branch_image_ar":"الواحد في العد والتركيب","concept_gloss":"bir sayısı, onlu kuruluşları ve on bire çıkarma","contextual_glosses":[{"applicability":"Sayma dizisinin ilk sayısını yalın olarak bildiren bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Onluklarla kurulan sayıları ve on bire çıkarma eylemini kapsamaz.","preserves":"Bir sayısının sayma başlangıcındaki değerini korur."},"facet_ids":["F001"],"text":"bir","usage_role":"contextual"},{"applicability":"Bir sayısının on veya yirmiyle kurduğu birleşik ya da bağlı sayı örneklerinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın bir sayısını ve bir topluluğu on bire çıkarma eylemini kapsamaz.","preserves":"Bir sayısının onluklarla birleşerek sayı kurmasını korur."},"facet_ids":["F002"],"text":"on bir ya da yirmi bir","usage_role":"contextual"},{"applicability":"Bir topluluğun sayısını on bire ulaştıran eylem biçiminin doğal karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın sayıyı ve onluklarla kurulan sayı adlarını kapsamaz.","preserves":"Bir topluluğu on bire ulaştırma işlemini ve sonucunu korur."},"facet_ids":["F003"],"text":"on bire çıkarmak","usage_role":"contextual"}],"definition":"Saymanın başlangıcındaki bir sayısını, bu sayının on ve yirmi gibi onluklarla birleşerek kurduğu sayıları ve bir topluluğu on bire çıkarma işlemini kapsar. Yalın sayı, birleşik sayı ve yapma eylemi birbirinden ayrı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sayma dizisinin başlangıcındaki bir sayısını bildirir."},{"facet_id":"F002","role":"extension","statement":"Bir sayısı on veya yirmi gibi onluklarla birleşerek on bir ve yirmi bir türü sayıları kurar."},{"facet_id":"F003","role":"associated_use","statement":"Eylem biçimi, bir topluluğun sayısını on bire çıkarma işlemini bildirir."}],"identity_rationale":"Kaynak ifadesi bir sayısını saymanın başlangıcı olarak, on ve yirmi gibi onluklarla kurulan sayılarda bir bileşen olarak ve bir kümeyi on bire çıkaran eylem biçiminde açıkça sunar. Dal çerçevesi bu üç kullanımı doğru biçimde ayırarak bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"saymanın başlangıcındaki bir"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"on bir, on bir dişil biçimi ve yirmi bir"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onları on bire çıkarmak"}],"lexicalization_note":"Tanım yalın bir sayısını, onluklarla kurulan söz öbeklerini ve on bire çıkarma biçimini ayrı yüzler olarak gösterir; söz öbeği anlamını yalın biçime yaymaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; onluklar, üç sayısı, teklik dalı ve üçe tamamlama dalı sayı alanının en açıklayıcı sınırlarını verdi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal kuruluş içindeki bir bileşenini ve on bire çıkarma eylemini izler; komşu dal ise onluk sayıların kendisini ve çevresindeki biçimleri izler.","focus_only":"Odak dal bir sayısını, onluklara eklenmesini ve on bire çıkarma işlemini merkez alır.","gloss":"on ve onluk sayılar","neighbor_only":"Komşu dal on, yirmi ve bunlara komşu onluk sayı sözlerini merkez alır.","neighbor_ref":"root_001016/B001","relation_type":"same_field","shared_zone":"İki dal on bir ve yirmi bir gibi sayı kuruluşlarında birlikte görünür."},{"boundary_match":"field_only","distinction":"Ortak alan sayı sistemidir, ancak merkez sayılar ve bunlardan kurulan biçimler farklıdır; birbirlerinin yerine kullanılamazlar.","focus_only":"Odak dal bir sayısını ve onun onluklarla kurduğu biçimleri kapsar.","gloss":"üç sayısı ve bağlı biçimleri","neighbor_only":"Komşu dal üç sayısını, onun sıra, dağıtma, yüzlük ve binlik gibi geniş türevlerini kapsar.","neighbor_ref":"root_000203/B001","relation_type":"same_field","shared_zone":"İki dal sayı adlarını ve bu adların düzenli kuruluşlarını işler."},{"boundary_match":"partial","distinction":"Odak dal sayı dizisi ve sayı kuruluşuyla sınırlıdır; komşu dal nitelik olarak tekliği ve eşsizliği merkez alır.","focus_only":"Odak dal sayma, onluklarla sayı kurma ve bir kümeyi on bire çıkarma görevlerini kapsar.","gloss":"tek ve eşi olmayan olma","neighbor_only":"Komşu dal tek ve eşi olmayan olmayı, mutlak nitelemeyi ve yinelemeli pekiştirmeyi kapsar.","neighbor_ref":"root_000017/B001","relation_type":"near_neighbor","shared_zone":"İki dal bir tane olma ve saymanın ilk basamağı çevresinde temas eder."},{"boundary_match":"partial","distinction":"Odak dalın merkez sayısı bir ve onlu kuruluşlarıdır; komşu dalın merkez sayısı beş, sıra değeri beşinci ve tamamlama sonucu beştir.","focus_only":"Odak dal bir sayısını, onun onluklarla kurduğu sayıları ve bir topluluğu on bire çıkarma işlemini bildirir.","gloss":"beş, beşinci ve beşe tamamlama","neighbor_only":"Komşu dal beş sayısını, beşinci olmayı, beş kişiden birini ve bir topluluğu beşe tamamlamayı bildirir.","neighbor_ref":"root_000439/B001","relation_type":"near_neighbor","shared_zone":"İki dal sayı adı, sıra içindeki yer ve bir topluluğu belirli sayıya ulaştırma alanlarında temas eder."}],"source_phrase_ar":"أحد واثنان وأحد عشر وإحدى عشرة (sihah); الواحد المضموم إلى العشرات نحو أحد عشر وأحد وعشرين (mufradat); فأحدهن أي صيرهن أحد عشر (sihah)","source_summary":"Kaynakların ortak kaydı bir sayısının hem sayma dizisindeki yalın yerini hem de onluklarla kurduğu sayıları gösterir. Aynı kanıt, ayrı bir eylem biçiminde bir kümeyi on bire çıkarma sonucunu da korur.","sources":["SI","MU"],"what_is_ar":"أحد في العد، وتركيبه مع العشرات، وتصْيير المعدود أحد عشر","what_is_not_ar":"ليس نفي الجنس ولا الأحدية المطلقة ولا يوم الأحد"},"support_links":[]},{"boundary":"Ad öbeğindeki seçme veya ilk olma kullanımı ile haftanın gün adı ayrı yüzlerdir; sayı kuruluşları ve dağ adı bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:26:4:1","qac_word_ref":"89:26:4","surface_ar":"أَحَدٌ"}],"gloss":"iki kişiden biri, ilk olan ve haftanın ilk günü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir ad öbeği içinde iki kişiden birini ayırır veya bağlama göre ilk olanı gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gün sözüyle kurulan söz öbeği haftanın ilk gününü ve o günün özel adını bildirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaynak ifadesi haftanın bu gününe verilen adın çoğul biçimini de kaydeder."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ad öbeğindeki seçme ya da ilk olma işlevini ve gün adıyla sınırlı takvim kullanımını birlikte temsil eder.","boundary_detail":"Ad öbeğindeki seçme veya ilk olma kullanımı ile haftanın gün adı ayrı yüzlerdir; sayı kuruluşları ve dağ adı bu dala girmez.","branch_image_ar":"الأول والإضافة","concept_gloss":"iki kişiden biri, ilk olan ve haftanın ilk günü","contextual_glosses":[{"applicability":"İki kişilik bir topluluktan herhangi bir üyeyi ad öbeği içinde ayıran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıra bakımından ilk olmayı, gün adını ve gün adının çoğulunu kapsamaz.","preserves":"İki kişiden birini seçme işlevini korur."},"facet_ids":["F001"],"text":"ikinizden biri","usage_role":"contextual"},{"applicability":"Haftanın ilk gününün Türkçedeki yerleşik adını gerektiren takvim bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki kişiden birini ayırma işlevini ve çoğul gün adı biçimini kapsamaz.","preserves":"Haftanın ilk gününün özel gün adı olma işlevini korur."},"facet_ids":["F002"],"text":"Pazar günü","usage_role":"contextual"},{"applicability":"Gün adının çoğul ya da yinelenen günler anlamındaki kullanımını karşılar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir günü ve iki kişiden birini ayırma işlevini kapsamaz.","preserves":"Gün adının çoğul kullanımını korur."},"facet_ids":["F003"],"text":"Pazar günleri","usage_role":"contextual"}],"definition":"Bir ad öbeğinin parçası olduğunda iki kişiden birini seçer veya bağlama göre ilk olanı bildirir. Gün adıyla kurulan kullanımda haftanın ilk gününü ve bu günün özel adını, ayrıca gün adının çoğul biçimini kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir ad öbeği içinde iki kişiden birini ayırır veya bağlama göre ilk olanı gösterir."},{"facet_id":"F002","role":"specialization","statement":"Gün sözüyle kurulan söz öbeği haftanın ilk gününü ve o günün özel adını bildirir."},{"facet_id":"F003","role":"source_variant","statement":"Kaynak ifadesi haftanın bu gününe verilen adın çoğul biçimini de kaydeder."}],"identity_rationale":"Kaynak ifadesi bir ad öbeği içinde bir kişiyi ayıran ya da ilk olanı bildiren kullanımla haftanın ilk gününün adını birlikte verir ve gün adının çoğulunu da kaydeder. Hazırlanan çerçeve kullanılabilir, ancak iki kişiden birini seçme anlamı her bağlamda sıra bakımından ilk olmayı zorunlu kılmaz.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ikinizden biri"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"Pazar günü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"Pazar günleri"}],"lexicalization_note":"Tanım ad öbeğine bağlı seçme kullanımını, gün adı söz öbeğini ve gün adının çoğul biçimini ayırır; bunları yalın kökün tek bir genel anlamına dönüştürmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ilk olma alanındaki komşu ile üç farklı gün adı ve sayı dalı, dalın hem sıra hem takvim sınırlarını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ilk olma yüzü belirli ad öbeklerine ve gün adına bağlıdır; komşu dal ise nesnelerin ön, üst ve başlangıç bölümlerine uzanan daha geniş bir öncelik alanıdır.","focus_only":"Odak dal ad öbeğinde iki kişiden birini ayırmayı ve haftanın ilk gününün adını da kapsar.","gloss":"ön, üst ve ilk bölüm","neighbor_only":"Komşu dal bir nesnenin önü, üstü ya da başlangıcı gibi uzamsal ve sıralı öncelikleri geniş biçimde kapsar.","neighbor_ref":"root_000849/B002","relation_type":"near_neighbor","shared_zone":"İki dal sıra bakımından ilk veya önde olanı gösterebilir."},{"boundary_match":"field_only","distinction":"Ortak alan haftanın günleridir, ancak gösterdikleri günler farklıdır ve gün adları birbirinin yerine geçmez.","focus_only":"Odak dal haftanın ilk gününün adını ve bu adın çoğulunu kapsar.","gloss":"Salı günü","neighbor_only":"Komşu dal Salı gününün adını ve onun tekil ile çoğul biçimlerini kapsar.","neighbor_ref":"root_000203/B006","relation_type":"same_field","shared_zone":"İki dal haftanın belirli bir gününe verilen adı ve adın sayı biçimlerini işler."},{"boundary_match":"field_only","distinction":"Odak dal ilk güne, komşu dal beşinci güne işaret eder; ortak takvim alanına karşın gösterdikleri gün ayrıdır.","focus_only":"Odak dal haftanın ilk gününü ve adını bildirir.","gloss":"Perşembe günü","neighbor_only":"Komşu dal haftanın beşinci gününün yerleşik adını bildirir.","neighbor_ref":"root_000439/B004","relation_type":"same_field","shared_zone":"İki dal haftanın gün adları dizgesine aittir."},{"boundary_match":"field_only","distinction":"Aynı takvim alanındadırlar, fakat haftanın farklı günlerini gösterirler ve odak dal ayrıca ad öbeğinde birini ayırma işlevi taşır.","focus_only":"Odak dal haftanın ilk gününü, adını ve çoğul biçimini kapsar.","gloss":"Çarşamba günü","neighbor_only":"Komşu dal Çarşamba gününün adını, söyleniş ayrıntısını ve çoğulunu kapsar.","neighbor_ref":"root_000536/B010","relation_type":"same_field","shared_zone":"İki dal bir hafta gününün adı ve çoğul kullanımı çevresinde buluşur."},{"boundary_match":"partial","distinction":"Odak dal seçme, sıra ve gün adı yapılarıyla sınırlıdır; komşu dal sayma ve sayı oluşturma işlemleriyle sınırlıdır.","focus_only":"Odak dal ad öbeğinde bir kişiyi ayırma ve haftanın ilk gününü adlandırma işlevlerini taşır.","gloss":"bir sayısı ve onlu sayı kuruluşları","neighbor_only":"Komşu dal bir sayısını, onluklarla sayı kurmayı ve bir topluluğu on bire çıkarmayı taşır.","neighbor_ref":"root_000017/B003","relation_type":"near_neighbor","shared_zone":"İki dal bir ve ilk düşüncelerinde temas eder."}],"source_phrase_ar":"أن يستعمل مضافا أو مضافا إليه بمعنى الأول (mufradat); أما أحدكما (mufradat); يوم الأحد أي يوم الأول (mufradat); يوم الأحد يجمع على آحاد (sihah)","source_summary":"Kaynakların birleşik kaydı, ad öbeği içindeki birini ayırma veya ilk sayma işlevini haftanın ilk gününün adıyla ilişkilendirir. Gün adının çoğul biçimi de aynı kanıt içinde korunur.","sources":["SI","MU"],"what_is_ar":"أحد مضافا أو مضافا إليه بمعنى الأول، واسم يوم الأحد","what_is_not_ar":"ليس أحد عشر ولا لا أحد ولا جبل أُحُد"},"support_links":[]},{"boundary":"Bu dal tek başına kalma ve ayrı ayrı hareket etme olaylarıdır; sayısal biri, olumsuz kişi kapsamını ve özel adları içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:26:4:1","qac_word_ref":"89:26:4","surface_ar":"أَحَدٌ"}],"gloss":"tek başına kalma ve birer birer gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin bir işi başkalarından ayrı olarak üstlenmesini veya tek başına kalmasını bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğun üyelerinin toplu halde değil, ayrı ayrı ve birer birer gelmesini bildirir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bireyin yalnızlaşmasını veya işi yalnız üstlenmesini ve topluluğun ayrı ayrı gelişini birlikte temsil eder.","boundary_detail":"Bu dal tek başına kalma ve ayrı ayrı hareket etme olaylarıdır; sayısal biri, olumsuz kişi kapsamını ve özel adları içermez.","branch_image_ar":"الانفراد والتفرق آحادا","concept_gloss":"tek başına kalma ve birer birer gelme","contextual_glosses":[{"applicability":"Bir kişinin başkalarından ayrılarak yalnız kalmasını bildiren bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işi yalnız üstlenme ayrıntısını ve topluluğun birer birer gelişini kapsamaz.","preserves":"Bireyin başkalarından ayrı ve yalnız duruma gelmesini korur."},"facet_ids":["F001"],"text":"tek başına kalmak","usage_role":"contextual"},{"applicability":"Bir kişinin belirli bir işi başkalarının katılımı olmadan üstlendiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel tek başına kalmayı ve topluluğun ayrı ayrı gelişini kapsamaz.","preserves":"Bir işi başkalarından ayrı olarak üstlenme ilişkisini korur."},"facet_ids":["F001"],"text":"işi yalnız üstlenmek","usage_role":"contextual"},{"applicability":"Bir topluluğun üyelerinin toplu halde değil, ayrı ayrı geldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bireyin bir işi yalnız üstlenmesini veya tek başına kalmasını kapsamaz.","preserves":"Ayrı ayrı ve birer birer geliş biçimini korur."},"facet_ids":["F002"],"text":"birer birer gelmek","usage_role":"contextual"}],"definition":"Bir kişinin bir işi başkalarından ayrı olarak yalnız üstlenmesi ya da tek başına kalmasıdır. Topluluk için kullanıldığında kişilerin toplu değil, ayrı ayrı ve birer birer gelmesini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin bir işi başkalarından ayrı olarak üstlenmesini veya tek başına kalmasını bildirir."},{"facet_id":"F002","role":"extension","statement":"Bir topluluğun üyelerinin toplu halde değil, ayrı ayrı ve birer birer gelmesini bildirir."}],"identity_rationale":"Kaynak ifadesi kişinin bir işi yalnız üstlenmesi ya da tek başına kalması ile insanların ayrı ayrı, birer birer gelmesini açıkça birbirine bağlı iki kullanım olarak verir. Hazırlanan dal bu eylem ve dağılım ayrımını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tek başına kalmak; işi yalnız üstlenmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"birer birer, ayrı ayrı"}],"lexicalization_note":"Tanım türemiş eylem biçimindeki yalnızlaşmayı ve yinelemeli dağılım sözündeki birer birer gelişi ayrı yüzler olarak tutar; ikisini yalın kök anlamı saymaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; yana çekilme, dağınık bulunma, yönlere dağılma ve benzeri az tek örnek dalları süreç ile nitelik sınırlarını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız üstlenme ile birer birer gelişe uzanır; komşu dal ise yana çekilme ve konumsal ayrılmayı daha belirgin biçimde taşır.","focus_only":"Odak dal bir işi yalnız üstlenmeyi ve topluluğun birer birer gelişini de kapsar.","gloss":"yana çekilme ve topluluktan ayrılma","neighbor_only":"Komşu dal topluluktan yana çekilmeyi, yer değiştirmeyi ve ayrı bir konumda bulunmayı kapsar.","neighbor_ref":"root_000305/B004","relation_type":"near_synonym","shared_zone":"İki dal bir kişinin topluluktan ayrılıp tek başına bulunmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal birer birer geliş biçimini ve bireysel yalnızlaşmayı belirtir; komşu dal yalnız topluluğun dağılmış durumunu kalıplaşmış biçimde bildirir.","focus_only":"Odak dal bireyin yalnızlaşmasını ve kişilerin birer birer gelişini kapsar.","gloss":"insanların dağılıp darmadağın olması","neighbor_only":"Komşu dal insanların genel olarak dağılmış ve darmadağın durumda bulunmasını anlatan kalıplaşmış bir sözdür.","neighbor_ref":"root_000154/B008","relation_type":"near_synonym","shared_zone":"İki dal bir topluluğun üyelerinin birlikte değil, dağınık durumda bulunmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal gelişin birer birer oluşunu ve bireysel yalnızlaşmayı da içerir; komşu dal yönlere dağılıp gitme olayına bağlıdır.","focus_only":"Odak dal tek başına kalmayı ve ayrı ayrı gelmeyi bildirir.","gloss":"farklı yönlere dağılıp gitmek","neighbor_only":"Komşu dal topluluğun farklı yönlere giderek dağılmasını bildiren kalıplaşmış bir anlatımdır.","neighbor_ref":"root_001331/B008","relation_type":"near_synonym","shared_zone":"İki dal bir topluluğun üyelerinin birbirinden ayrılarak dağılmasını kapsar."},{"boundary_match":"partial","distinction":"Odak dal insanların yalnızlaşma ya da ayrı ayrı hareket etme sürecini bildirir; komşu dal ise belirli bir hayvanın tek başına oluşunu adlandıran türle sınırlı bir kullanımdır.","focus_only":"Odak dal yalnızlaşma sürecini veya kişilerin ayrı ayrı hareket etmesini anlatır.","gloss":"topluluktan ayrı duran tek hayvan","neighbor_only":"Komşu dal belirli yaban hayvanlarının topluluktan ayrı duran tek üyesini adlandırır.","neighbor_ref":"root_000877/B009","relation_type":"near_neighbor","shared_zone":"İki dal bir canlının başkalarından ayrı ve tek başına bulunması düşüncesinde buluşur."}],"source_phrase_ar":"ما استأحدت بهذا الأمر أي ما انفردت به (maqayis); استأحد الرجل انفرد (sihah); جاءوا آحاد أحاد (sihah)","source_summary":"Kaynaklar tek başına kalma veya bir işi yalnız üstlenme anlamını birlikte destekler. Aynı kayıt, topluluğun üyelerinin ayrı ayrı ve birer birer gelişiyle bu çekirdeğin dağılımsal uzantısını da gösterir.","sources":["MQ","SI"],"what_is_ar":"الانفراد بالفعل، والمجيء آحادا أفرادا","what_is_not_ar":"ليس الواحد في العدد ولا نفي الجنس ولا علم الجبل"},"support_links":[]},{"boundary":"Bu dal yalnız belirli bir dağın özel adıdır; tek olma, olumsuz kişi kapsamı, sayı, gün adı ve yalnızlaşma anlamlarını taşımaz.","branch_kind":"non_bare","branch_ref":"root_000017/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:26:4:1","qac_word_ref":"89:26:4","surface_ar":"أَحَدٌ"}],"gloss":"Medine'deki belirli bir dağın özel adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir dağın özel adı olarak tek bir coğrafi varlığı gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dağın yeri kaynakta Medine ile ilişkilendirilmiştir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel dağ anlamı yüklemeden, kaynakta Medine'de bulunduğu belirtilen tek coğrafi varlığın özel ad işlevini açıklar.","boundary_detail":"Bu dal yalnız belirli bir dağın özel adıdır; tek olma, olumsuz kişi kapsamı, sayı, gün adı ve yalnızlaşma anlamlarını taşımaz.","branch_image_ar":"جبل أُحُد","concept_gloss":"Medine'deki belirli bir dağın özel adı","contextual_glosses":[{"applicability":"Dağın kimliği bağlamdan zaten biliniyorsa, adı yeniden üretmeden özel ad işlevini açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaynakta belirtilen kentle kurulan yer bağını açıkça taşımaz.","preserves":"Belirli bir dağın özel adı olma işlevini korur."},"facet_ids":["F001"],"text":"o dağın özel adı","usage_role":"explanatory"}],"definition":"Medine'de bulunan belirli bir dağa verilen özel addır. Genel olarak dağ türünü ya da dağın bir niteliğini değil, tek bir coğrafi varlığın kimliğini gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir dağın özel adı olarak tek bir coğrafi varlığı gösterir."},{"facet_id":"F002","role":"specialization","statement":"Dağın yeri kaynakta Medine ile ilişkilendirilmiştir."}],"identity_rationale":"Kaynak ifadesi bu birimi genel bir dağ türü olarak değil, belirli bir kentteki tek bir dağın özel adı olarak tanımlar. Hazırlanan dalın özel yer adı çerçevesi bu kanıtla doğrudan uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"Medine'deki dağın özel adı"}],"lexicalization_note":"Tanım yalnız kaynakta belirlenen özel dağ adına bağlıdır ve bu yer adı kullanımından genel bir dağ ya da yalın kök anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; başka dağ ve yer adları yalnız alan ortaklığı düzeyinde karşılaştırıldı, anlamdaşlık kurulmadı ve en açıklayıcı üç özel ad adayı yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Özel ad işlevleri aynı olsa da gösterdikleri coğrafi varlıklar ayrıdır; adlar birbirinin yerine kullanılamaz.","focus_only":"Odak dal kaynakta belirtilen kentteki belirli bir dağı adlandırır.","gloss":"başka bir dağın özel adı","neighbor_only":"Komşu dal başka bir belirli dağa verilen ayrı özel adı kapsar.","neighbor_ref":"root_000706/B006","relation_type":"same_field","shared_zone":"İki dal da genel dağ türünü değil, belirli bir dağın özel adını bildirir."},{"boundary_match":"field_only","distinction":"Aynı özel ad türüne girseler de farklı kentlerdeki farklı dağları gösterirler; kimlikleri ortak değildir.","focus_only":"Odak dal kaynakta belirtilen kentteki belirli dağı gösterir.","gloss":"başka bir kentteki tanınmış dağın adı","neighbor_only":"Komşu dal başka bir kentteki tanınmış dağı gösteren ayrı bir özel addır.","neighbor_ref":"root_000314/B006","relation_type":"same_field","shared_zone":"İki dal da bir kentle ilişkilendirilen tanınmış dağın özel adıdır."},{"boundary_match":"field_only","distinction":"Odak dal tek bir dağa bağlıdır; komşu dalın adı birden çok yer biçimine ve birden çok coğrafi varlığa uygulanabilir.","focus_only":"Odak dal yalnız tek bir belirli dağın özel adıdır.","gloss":"dağ ve tepeler için kullanılan başka bir yer adı","neighbor_only":"Komşu dal aynı adla anılan birden çok yer, dağ veya tepeyi kapsayabilir.","neighbor_ref":"root_000602/B002","relation_type":"same_field","shared_zone":"İki dal coğrafi varlıkları gösteren özel yer adları alanındadır."}],"source_phrase_ar":"أحد جبل بالمدينة (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak tanıklığı, birimi Medine'deki belirli dağın özel adı olarak kaydeder."}],"source_summary":"Bu dal genel bir sözlük anlamından çok, tek bir coğrafi varlığı gösteren özel ad kullanımını kapsar. Kaynak kaydı, gösterilen varlığın Medine'de bulunan dağ olduğunu bildirir.","sources":["SI"],"what_is_ar":"اسم جبل بالمدينة","what_is_not_ar":"ليس معنى الواحد ولا النفي ولا الاستئحاد"},"support_links":[]},{"boundary":"It includes causing someone to be driven, constrained, or forced toward something.","branch_kind":null,"branch_ref":"root_000281/B005","candidate_links":[{"candidate_id":"cand_fb9181681c8a792269f1","lane":"macro"}],"focus_root_occurrences":[],"gloss":"driving or compelling","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الإلجاء والاضطرار","image_en":"driving or compelling"}}],"root_ar":"ج ي ء","root_id":"root_000281","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الإلجاء والاضطرار","image_en":"driving or compelling","scope_ar":"يدخل فيه أجاءه إلى كذا بمعنى ألجأه واضطره إليه، وجعله العرب إلجاء مع كونه معدى عن جاء.","scope_en":"It includes causing someone to be driven, constrained, or forced toward something."},"support_links":["sup_e735f60954e26a6d1f49"]},{"boundary":"Includes the idiom \"entered upon/with his wife\" as a euphemism for consummation.","branch_kind":null,"branch_ref":"root_000464/B002","candidate_links":[{"candidate_id":"cand_91ffbab76826cb46a989","lane":"macro"}],"focus_root_occurrences":[],"gloss":"consummating marriage","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الإفضاء الزوجي","image_en":"consummating marriage"}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الإفضاء الزوجي","image_en":"consummating marriage","scope_ar":"يدخل فيه قولهم دخل بامرأته كناية عن الإفضاء إليها.","scope_en":"Includes the idiom \"entered upon/with his wife\" as a euphemism for consummation."},"support_links":["sup_a322f69eb4f5ec97f50a"]},{"boundary":"This covers marital reinstatement after divorce and a woman returning to her family.","branch_kind":null,"branch_ref":"root_000544/B004","candidate_links":[{"candidate_id":"cand_91ffbab76826cb46a989","lane":"macro"}],"focus_root_occurrences":[],"gloss":"Domestic or marital return","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"رجعة المرأة في النكاح والأهل","image_en":"Domestic or marital return"}}],"root_ar":"ر ج ع","root_id":"root_000544","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"رجعة المرأة في النكاح والأهل","image_en":"Domestic or marital return","scope_ar":"يدخل فيه مراجعة الزوج امرأته ورجعة الطلاق ورجوع المرأة إلى أهلها بعد موت زوجها أو طلاقها.","scope_en":"This covers marital reinstatement after divorce and a woman returning to her family."},"support_links":["sup_a322f69eb4f5ec97f50a"]},{"boundary":"cessation of movement, settling, stillness, silence, and calming after agitation","branch_kind":null,"branch_ref":"root_000726/B001","candidate_links":[{"candidate_id":"cand_7c69e717657cbe5f5791","lane":"macro"}],"focus_root_occurrences":[],"gloss":"cessation of motion","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"ذهاب الحركة","image_en":"cessation of motion"}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"ذهاب الحركة","image_en":"cessation of motion","scope_ar":"يدخل فيه السكون بعد الحركة والاستقرار والثبوت والهدوء والسكوت وسكون الريح والمطر والغضب","scope_en":"cessation of movement, settling, stillness, silence, and calming after agitation"},"support_links":["sup_22731a5850a177d357e0"]},{"boundary":"anything one rests in or finds comfort in, including a beloved object, house, night, prayer, or fire as a source of familiar rest","branch_kind":null,"branch_ref":"root_000726/B004","candidate_links":[{"candidate_id":"cand_7c69e717657cbe5f5791","lane":"macro"}],"focus_root_occurrences":[],"gloss":"object of rest and comfort","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"مأنس السكون","image_en":"object of rest and comfort"}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"مأنس السكون","image_en":"object of rest and comfort","scope_ar":"يدخل فيه كل ما تسكن إليه النفس من محبوب أو بيت أو ليل أو صلاة أو نار سميت بذلك للأنس والسكون إليها","scope_en":"anything one rests in or finds comfort in, including a beloved object, house, night, prayer, or fire as a source of familiar rest"},"support_links":["sup_22731a5850a177d357e0"]},{"boundary":"ship rudder or stern part by which a vessel is steadied and corrected","branch_kind":null,"branch_ref":"root_000726/B008","candidate_links":[{"candidate_id":"cand_fb9181681c8a792269f1","lane":"macro"}],"focus_root_occurrences":[],"gloss":"rudder steadying a ship","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"تسكين السفينة بالسكان","image_en":"rudder steadying a ship"}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"تسكين السفينة بالسكان","image_en":"rudder steadying a ship","scope_ar":"يدخل فيه سكان السفينة وذنبها أو كوثلها الذي تعدل به وتسكن عن الاضطراب","scope_en":"ship rudder or stern part by which a vessel is steadied and corrected"},"support_links":["sup_e735f60954e26a6d1f49"]},{"boundary":"marriage contracting and the idiom of a man taking a woman in marriage","branch_kind":null,"branch_ref":"root_001444/B004","candidate_links":[{"candidate_id":"cand_91ffbab76826cb46a989","lane":"macro"}],"focus_root_occurrences":[],"gloss":"marriage contract","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الإملاك والتزويج","image_en":"marriage contract"}}],"root_ar":"م ل ك","root_id":"root_001444","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الإملاك والتزويج","image_en":"marriage contract","scope_ar":"عقد التزويج والإملاك؛ شهدنا إملاك فلان؛ ملك الرجل المرأة بمعنى تزوجها","scope_en":"marriage contracting and the idiom of a man taking a woman in marriage"},"support_links":["sup_a322f69eb4f5ec97f50a"]},{"boundary":"Bu kol, fiziksel bağlama, sağlamlaştırma veya bağlayıcı anlaşma kurmayı değil, güvenip dayanmayı ve güvenilir sayılmayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001623/B001","candidate_links":[{"candidate_id":"cand_7c69e717657cbe5f5791","lane":"macro"},{"candidate_id":"cand_fb9181681c8a792269f1","lane":"macro"},{"candidate_id":"cand_11e5939c0c158e0e5dc0","lane":"macro"},{"candidate_id":"cand_fc0f7d806678b91d369b","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"يُوثِقُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yuwviqu|ROOT:wvq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:26:2:1","qac_word_ref":"89:26:2","surface_ar":"يُوثِقُ"},{"lemma_ar":"وَثَاق","morph_features":"STEM|POS:N|LEM:wavaAq|ROOT:wvq|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:26:3:1","qac_word_ref":"89:26:3","surface_ar":"وَثَاقَ"}],"gloss":"güvenmek ve güvenilir olmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da şeyi güvenilir bulmak, ona inanmak ve ona dayanmak."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi, topluluk veya şeyi güvenilebilir ve dayanılabilir diye nitelemek."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir arazi söz öbeğinde, bol otu sayesinde kendisine güvenilen yeri anlatmak."}}],"root_ar":"و ث ق","root_id":"root_001623","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kolun güvenip dayanma eylemini ve güvenilen kişi ya da şeyin niteliğini birlikte karşılayan genel anlatımdır.","boundary_detail":"Bu kol, fiziksel bağlama, sağlamlaştırma veya bağlayıcı anlaşma kurmayı değil, güvenip dayanmayı ve güvenilir sayılmayı anlatır.","branch_image_ar":"الثقة والسكون إلى المعتمد","concept_gloss":"güvenmek ve güvenilir olmak","contextual_glosses":[{"applicability":"Bir kişinin başka bir kişiyi güvenilir bulup ona dayandığı eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güvenilir bulma, iç rahatlığı ve dayanma yönlerini korur."},"facet_ids":["F001"],"text":"ona güvendi","usage_role":"contextual"},{"applicability":"Bir kişi, topluluk veya şeyin kendisine güvenilebildiğini belirten niteleme bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güvenilen ve dayanılabilen olma niteliğini doğrudan korur."},"facet_ids":["F002"],"text":"güvenilir","usage_role":"general"},{"applicability":"Yalnız bol ot sağladığı için güvenilir sayılan araziyi anlatan özel söz öbeği bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Araziye duyulan güveni ve bunun bol ot gerekçesini korur."},"facet_ids":["F003"],"text":"bol otuna güvenilen arazi","usage_role":"explanatory"}],"definition":"Bir kişi ya da şeyi güvenilir bulup ona iç rahatlığıyla dayanmak; ayrıca güvenilir olma niteliğini veya böyle nitelenen kişi, topluluk ya da şeyi anlatır. Belirli bir arazi söz öbeğinde, bol ot verdiği için güvenilen yeri belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da şeyi güvenilir bulmak, ona inanmak ve ona dayanmak."},{"facet_id":"F002","role":"core","statement":"Bir kişi, topluluk veya şeyi güvenilebilir ve dayanılabilir diye nitelemek."},{"facet_id":"F003","role":"specialization","statement":"Belirli bir arazi söz öbeğinde, bol otu sayesinde kendisine güvenilen yeri anlatmak."}],"identity_rationale":"Kaynak ifadesi, bir kişi ya da şeyi güvenilir bulup ona iç rahatlığıyla dayanmayı; ayrıca güvenilen kişi, topluluk veya şeyi nitelemeyi açıkça bir arada verir. Bol otlu arazi kullanımı da bu çekirdeğin belirli bir söz öbeğindeki uygulamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ona güvendi ve dayandı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"güvenme ve dayanma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"güvenilir kişi veya topluluk"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ona güvenen ve dayanan"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kendisine güvenilen"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bol otuna güvenilen arazi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"onu güvenilir ilan etti"}],"lexicalization_note":"Tanım, yalın güven ve güvenilirlik çekirdeğini belirli kişi ve şey kullanımlarından ayırır; bol otlu arazi anlamını yalnız kendi söz öbeğine bağlı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın güven, dayanma ve sakinleşme komşuları ile aynı kökün sağlamlık kolu sınırı açıklayıcı bulundu. Öteki adaylar ya yalnız ortak bir senaryoya katılıyor ya da seçilen ayrımları yineliyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kolunda güvenilir bulma ve bu yüzden dayanma esastır; komşu kolda ise güvenin yanı sıra yakınlık, alışma ve iç huzuru öne çıkar. Bu nedenle her bağlamda birbirlerinin yerine geçmezler.","focus_only":"Güvenilen kişi, topluluk veya şeyin güvenilir diye nitelenmesini de kapsar.","gloss":"güvenme ile iç huzuru bulma","neighbor_only":"Yakınlık duyma, alışma ve birinin yanında iç huzuru bulma yönünü daha belirgin taşır.","neighbor_ref":"root_001568/B005","relation_type":"near_synonym","shared_zone":"Her iki kol da bir kişi ya da şey karşısında kuşkunun yatışmasını ve ona güven duymayı anlatır."},{"boundary_match":"partial","distinction":"Odak kolu, dayanılan kişi ya da şeyin güvenilir bulunmasına dayanır. Komşu kolun çekirdeği ise işi veya sonucu başkasına dayandırmaktır; güvenilirlik değerlendirmesi zorunlu çekirdek değildir.","focus_only":"Dayanılan kişi ya da şeyin güvenilir olduğu yönünde bir değerlendirme içerir.","gloss":"güvenme ile bel bağlama","neighbor_only":"Bir işi başka birine bırakma ve sonucu onun gücüne veya yönetimine dayandırma yönünü kapsar.","neighbor_ref":"root_001681/B002","relation_type":"near_neighbor","shared_zone":"İki kol da kişinin kendi başına davranmayıp başka birine veya şeye dayanmasını içerir."},{"boundary_match":"partial","distinction":"Odak kolunda yatışmanın temeli güvenilirlik ve dayanmadır. Komşu kol ise yönelme ve sakinleşmeyi anlatır; bu yönelim mutlaka güvenme ya da güvenilir sayma anlamına gelmez.","focus_only":"Bir kişi ya da şeyi güvenilir bulup ona dayanma ve onu güvenilir diye niteleme yönü vardır.","gloss":"güvenme ile yönelip sakinleşme","neighbor_only":"Bir şeye yönelme, ona yakınlık duyma ve onun yanında durulma yönü güven olmadan da gerçekleşebilir.","neighbor_ref":"root_000596/B002","relation_type":"near_neighbor","shared_zone":"Her ikisinde de kişinin bir şey karşısında yatışması ve ona doğru kalıcı bir yönelim göstermesi mümkündür."},{"boundary_match":"field_only","distinction":"Odak kolu değerlendiren kişinin güvenini ve dayanmasını konu eder. Komşu kol ise nesnenin, yapının veya işin kendi sağlamlığını ve sağlamlaştırılmasını konu eder.","focus_only":"Bir kişi ya da şey hakkında güvenilirlik yargısı kurup ona dayanmayı anlatır.","gloss":"güvenilirlik ile sağlamlık","neighbor_only":"Bir nesne veya işin sıkı, güçlü ve bozulmaya dirençli olması ya da bu duruma getirilmesini anlatır.","neighbor_ref":"root_001623/B002","relation_type":"same_field","shared_zone":"Her iki kol da dayanmaya elverişlilik ve beklenen durumda kalma düşüncesi çevresinde buluşur."}],"source_phrase_ar":"وثقت بفلان أثق به ثقة وأنا واثق به وهو موثوق به (ayn;tahdhib)؛ وثقت بفلان إذا ائمنته (sihah)؛ وثقت به أثق ثقة: سكنت إليه واعتمدت عليه (mufradat)؛ وهو ثقة وقد وثقت به (maqayis)؛ استعمل منه الثقة وهي راجعة إلى الوثيقة (jamhara)؛ أرض وثيقة: كثيرة العشب موثوق بها (tahdhib)","source_summary":"Kaynaklar, güvenmenin iç rahatlığı ve dayanma içerdiğinde; güvenilen kişi ya da şeyin de güvenilir diye nitelenebildiğinde birleşir. Arazi örneği, bu güvenilirlik düşüncesini bol ot sağlama beklentisine uygular.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه وثقت به أو بالشيء، والائتمان، والاعتماد، ووصف الشخص أو الجماعة أو الشيء بأنه ثقة أو موثوق به، ومنه التعبير عن أرض وثيقة موثوق بها لكثرة عشبها.","what_is_not_ar":"ليس المراد مجرد شد الحبل أو عقد الميثاق إلا إذا صار الكلام عن الاعتماد والائتمان."},"support_links":["sup_22731a5850a177d357e0","sup_5e75750b5c5a308713dc","sup_e735f60954e26a6d1f49","sup_fefe8979b20d01fde650"]},{"boundary":"Bu kol genel sağlamlık ve sağlamlaştırmayla sınırlıdır; güvenme, fiziksel bağ aracı veya bağlayıcı anlaşma anlamları kendi başlarına buraya girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001623/B002","candidate_links":[{"candidate_id":"cand_7de2443661e049279fb8","lane":"macro"},{"candidate_id":"cand_df7cb0e9b7256a09cebd","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"يُوثِقُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yuwviqu|ROOT:wvq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:26:2:1","qac_word_ref":"89:26:2","surface_ar":"يُوثِقُ"},{"lemma_ar":"وَثَاق","morph_features":"STEM|POS:N|LEM:wavaAq|ROOT:wvq|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:26:3:1","qac_word_ref":"89:26:3","surface_ar":"وَثَاقَ"}],"gloss":"sağlamlaştırma ve sağlamlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi sıkılaştırmak, güçlendirmek ve bozulmaya dirençli duruma getirmek."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin sıkı, güçlü, sağlam ve dayanıklı olması."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dişi veya erkek devenin yaratılış ve beden yapısı bakımından güçlü ve sağlam olması."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir işi sıkı tutmak ve seçenekler arasından en sağlam, en güvenli olanı seçmek."}}],"root_ar":"و ث ق","root_id":"root_001623","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kolun bir şeyi sıkı ve dirençli kılma eylemiyle bu eylemin sonucundaki güçlü durumu birlikte anlatan genel karşılıktır.","boundary_detail":"Bu kol genel sağlamlık ve sağlamlaştırmayla sınırlıdır; güvenme, fiziksel bağ aracı veya bağlayıcı anlaşma anlamları kendi başlarına buraya girmez.","branch_image_ar":"الإحكام والوثاقة","concept_gloss":"sağlamlaştırma ve sağlamlık","contextual_glosses":[{"applicability":"Bir nesne veya yapının daha sıkı, güçlü ve bozulmaya dirençli duruma getirildiği eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyi sıkı ve dayanıklı duruma getirme işlemini korur."},"facet_ids":["F001"],"text":"onu sağlamlaştırdı","usage_role":"contextual"},{"applicability":"Bir şeyin güçlü, sıkı ve bozulmaya dirençli durumunu niteleyen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güçlü, sıkı ve dayanıklı olma niteliğini doğrudan korur."},"facet_ids":["F002"],"text":"sağlam ve sıkı","usage_role":"general"},{"applicability":"Dişi veya erkek devenin beden yapısının güçlü ve sağlam olduğunu belirten özel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın yaratılıştan gelen güçlü ve sağlam yapısını korur."},"facet_ids":["F003"],"text":"yapısı sağlam deve","usage_role":"contextual"},{"applicability":"Bir işte seçenekler arasından en sıkı, güvenli ve dayanılır yolu seçme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşi sıkı tutma ve en güvenli seçeneği benimseme yönünü korur."},"facet_ids":["F004"],"text":"en sağlam yolu tuttu","usage_role":"explanatory"}],"definition":"Bir şeyi sıkı, güçlü ve bozulmaya dirençli duruma getirmek veya böyle bir sağlamlık niteliğine sahip olmak. Belirli kullanımlarda güçlü yapılı hayvanı ve bir işte en sağlam, en güvenli yolu seçmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi sıkılaştırmak, güçlendirmek ve bozulmaya dirençli duruma getirmek."},{"facet_id":"F002","role":"core","statement":"Bir şeyin sıkı, güçlü, sağlam ve dayanıklı olması."},{"facet_id":"F003","role":"specialization","statement":"Dişi veya erkek devenin yaratılış ve beden yapısı bakımından güçlü ve sağlam olması."},{"facet_id":"F004","role":"extension","statement":"Bir işi sıkı tutmak ve seçenekler arasından en sağlam, en güvenli olanı seçmek."}],"identity_rationale":"Kaynak ifadesi hem bir şeyi sıkı ve sağlam duruma getirme eylemini hem de ortaya çıkan sağlamlık niteliğini verir. Hayvanın güçlü yapısı ve bir işte en sağlam yolu tutma kullanımları bu çekirdeğin açık uzmanlaşmalarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"sağlam ve sıkı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"sağlam ve sıkı oldu"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"onu sağlamlaştırdı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yapısı sağlam dişi deve"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yapısı sağlam dişi veya erkek deve"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"işi sıkı tutma ve en sağlam yolu seçme"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"en sağlam ve en sıkı olan"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"en sağlam olan"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"işte en sağlam yolu tuttu"}],"lexicalization_note":"Tanım, genel sağlamlık çekirdeğini korurken hayvan yapısı ve işi sıkı tutma gibi kullanımları yalnız kendi söz öbeklerine bağlı uzmanlaşmalar olarak ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; maddi sertlik, genel güçlendirme, gevşekliğin yokluğu ve aynı kökün bağlama kolu en öğretici sınırları verdi. Diğer adaylar daha uzak güç görünümleri sunduğu veya bu ayrımları yinelediği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kolunda parçaları tutan, bozulmaya dirençli bir sağlamlık ve bunu oluşturma işlemi esastır. Komşu kol sertlik ve şiddeti çok daha geniş alanlara yayar; sağlam kurulmuş olma zorunlu değildir.","focus_only":"Bir şeyi sağlamlaştırma işlemini ve bir işi en sağlam yoldan yürütme uzantısını kapsar.","gloss":"sağlamlık ile sertlik","neighbor_only":"Sertlik, şiddet, kuruma, hızlı koşma ve yüksek ses gibi çok daha geniş güç ve katılık görünümlerini kapsar.","neighbor_ref":"root_000875/B001","relation_type":"near_synonym","shared_zone":"Her iki kol da gevşekliğin ve yumuşaklığın karşısında güçlü, sıkı bir durumu anlatabilir."},{"boundary_match":"partial","distinction":"Odak kolu sıkı kurulmuşluk ve dayanıklılıktan hareketle soyut işlere de uzanır. Komşu kolun çekirdeği ise maddi sertlik ve düzgünlüktür; sağlamlaştırma işlemini taşımaz.","focus_only":"Soyut işlerde sağlam yolu seçmeyi ve bir şeyi sağlamlaştırmayı da kapsar.","gloss":"sağlamlık ile maddi sertlik","neighbor_only":"Maddi sertlik ve düzgünlük, özellikle sert ve doğru duran nesne görünümünü öne çıkarır.","neighbor_ref":"root_000852/B002","relation_type":"near_synonym","shared_zone":"İki kol da maddi bir şeyin güçlü, kolay eğilmeyen veya bozulmayan durumunu karşılayabilir."},{"boundary_match":"partial","distinction":"Odak kolu parçaları sıkı tutan ve bozulmayı önleyen sağlamlığa yönelir. Komşu kol genel güç artışına ve birini başkasıyla desteklemeye yönelir; sıkı kurulmuşluk şart değildir.","focus_only":"Sıkı ve bozulmaya dirençli olma durumunu, hayvan yapısını ve sağlam seçim yapmayı içerir.","gloss":"sağlamlaştırma ile güçlendirme","neighbor_only":"Bir kişi veya şeyi başka bir güçle destekleyip gücünü artırma ilişkisini öne çıkarır.","neighbor_ref":"root_001008/B004","relation_type":"near_neighbor","shared_zone":"Her iki kol da bir kişi ya da şeyi öncekinden daha güçlü duruma getiren bir işlemi anlatabilir."},{"boundary_match":"partial","distinction":"Odak kolu güçlü ve sıkı yapıyı olumlu bir nitelik olarak kurar ve sağlamlaştırma eylemini de içerir. Komşu kol yalnız gevşeklik ya da güçsüzlüğün yokluğunu bildirir.","focus_only":"Olumlu bir sağlamlık niteliğini ve bu niteliği oluşturma eylemini adlandırır.","gloss":"sağlamlık ile gevşek olmama","neighbor_only":"Gevşeklik, güçsüzlük, kusur veya yumuşaklık bulunmadığını olumsuz yoldan belirtir.","neighbor_ref":"root_000049/B002","relation_type":"near_neighbor","shared_zone":"Sağlam bir şeyde gevşeklik ve güçsüzlük bulunmaması iki kolun ortak alanını oluşturur."},{"boundary_match":"partial","distinction":"Odak kolunun çekirdeği genel sağlamlık ve sağlamlaştırmadır; belirli bir bağlama işlemi gerekmez. Komşu kol ise somut bağlama eylemini veya bağ aracını zorunlu kılar.","focus_only":"Bağ kullanılmadan da bir nesnenin veya işin sağlam ve sıkı olması ya da sağlamlaştırılmasını kapsar.","gloss":"sağlamlaştırma ile sıkıca bağlama","neighbor_only":"Bir canlı veya nesneyi iple ya da başka bir araçla bağlamayı ve kullanılan bağ aracını adlandırır.","neighbor_ref":"root_001623/B003","relation_type":"near_neighbor","shared_zone":"Sıkıca bağlama bir şeyi yerinde tutup sağlamlaştırabildiği için iki kol aynı sonuç çevresinde kesişebilir."}],"source_phrase_ar":"كلمة تدل على عقد وإحكام؛ وثقت الشيء: أحكمته؛ ناقة موثقة الخلق (maqayis)؛ الوثيق المحكم؛ الوثيقة في الأمر إحكامه؛ ناقة وثيقة وجمل وثيق (ayn;tahdhib)؛ أخذت الأمر بالأوثق أي الشديد المحكم (jamhara)؛ الوثيق: الشيء المحكم؛ وثقت الشيء توثيقا فهو موثق؛ ناقة موثقة الخلق (sihah)؛ الوثقى تأنيث الأوثق؛ ناقة موثقة الخلق: محكمته (mufradat)","source_summary":"Kaynakların ortak çekirdeği, bir şeyi sağlamlaştırmak ile bir şeyin sıkı ve güçlü olmasıdır. Güçlü yapılı deve örnekleri bu niteliği bedene, bir işte en sağlam olanı seçme kullanımları ise karar ve önleme alanına taşır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه إحكام الشيء وتقويته، والشيء الوثيق المحكم، والأوثق والشديد المحكم، ووثاقة الخلق في الناقة أو الجمل، والوثيقة في الأمر بمعنى إحكامه والأخذ بالأثبت.","what_is_not_ar":"لا يدخل فيه الائتمان المحض، ولا العهد بوصفه ميثاقا، ولا أداة الربط إلا من جهة الإحكام العام."},"support_links":["sup_77981ca9c5a7a11a0cf9","sup_df7bc0986b1725eab3ec"]},{"boundary":"Bu kol somut bağlama ve bağ aracına bağlıdır; genel sağlamlık, birine güvenme veya bağlayıcı sözleşme anlamını tek başına taşımaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001623/B003","candidate_links":[{"candidate_id":"cand_7de2443661e049279fb8","lane":"macro"},{"candidate_id":"cand_00b2bfe089da4b527c3f","lane":"macro"},{"candidate_id":"cand_11e5939c0c158e0e5dc0","lane":"macro"},{"candidate_id":"cand_80d710337ef76db09173","lane":"macro"},{"candidate_id":"cand_fc0f7d806678b91d369b","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"يُوثِقُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yuwviqu|ROOT:wvq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:26:2:1","qac_word_ref":"89:26:2","surface_ar":"يُوثِقُ"},{"lemma_ar":"وَثَاق","morph_features":"STEM|POS:N|LEM:wavaAq|ROOT:wvq|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:26:3:1","qac_word_ref":"89:26:3","surface_ar":"وَثَاقَ"}],"gloss":"sıkıca bağlama ve bağ aracı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir canlı veya nesneyi sıkıca bağlayarak bulunduğu yerde tutmak ve hareketini sınırlamak."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sıkıca bağlama ve bağlı duruma getirme eyleminin adı olmak."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şeyi bağlı tutmak için kullanılan ipi veya başka bağ aracını adlandırmak."}}],"root_ar":"و ث ق","root_id":"root_001623","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kolun bağlı duruma getirme eylemiyle bu iş için kullanılan ip veya başka aracı birlikte karşılayan genel anlatımdır.","boundary_detail":"Bu kol somut bağlama ve bağ aracına bağlıdır; genel sağlamlık, birine güvenme veya bağlayıcı sözleşme anlamını tek başına taşımaz.","branch_image_ar":"الإيثاق والوثاق الذي يشد به","concept_gloss":"sıkıca bağlama ve bağ aracı","contextual_glosses":[{"applicability":"Bir canlı veya nesnenin hareketi sınırlanacak biçimde bağlı duruma getirildiği eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sıkıca bağlayıp hareketi sınırlama işlemini doğrudan korur."},"facet_ids":["F001"],"text":"onu sıkıca bağladı","usage_role":"contextual"},{"applicability":"Bir şeyi bağlı duruma getirme işinin eylem adı olarak kullanıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlama işlemini bir eylem adı olarak eksiksiz korur."},"facet_ids":["F002"],"text":"sıkıca bağlama","usage_role":"general"},{"applicability":"Bir nesne veya canlıyı bağlı tutmak için kullanılan ip ya da başka aracın adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlama amacıyla kullanılan ip veya araç anlamını korur."},"facet_ids":["F003"],"text":"bağlama ipi veya aracı","usage_role":"explanatory"}],"definition":"Bir canlıyı ya da nesneyi sıkıca bağlayıp hareketini sınırlamak; ayrıca bu bağlama eylemini ve bağlamada kullanılan ipi ya da başka aracı adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir canlı veya nesneyi sıkıca bağlayarak bulunduğu yerde tutmak ve hareketini sınırlamak."},{"facet_id":"F002","role":"extension","statement":"Sıkıca bağlama ve bağlı duruma getirme eyleminin adı olmak."},{"facet_id":"F003","role":"extension","statement":"Bir şeyi bağlı tutmak için kullanılan ipi veya başka bağ aracını adlandırmak."}],"identity_rationale":"Kaynak ifadesi, bir canlı ya da nesneyi sıkıca bağlama eylemini ve bu işte kullanılan ip veya başka bağ aracını birlikte gösterir. Eylem adı ile araç adı aynı kol içinde açıkça ayrılabildiğinden yapısal bir sorun yoktur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"onu sıkıca bağladı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"sıkıca bağlama"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bağlama eylemi"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"bağlama ipi veya aracı"}],"lexicalization_note":"Tanım, sıkıca bağlama eylemi ile bu eylemin adını ve kullanılan aracı ayrı yüzler olarak gösterir; bunları genel sağlamlık anlamına yaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel bağlama, tutsak etme, köstekleme, deveye özgü bağ ve aynı kökün sağlamlık kolu en yararlı sınırları sundu. Kalan adaylar daha dar araç adları veya seçilen karşılaştırmaların yinelemeleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kolunda sıkıca bağlama ve bağlı tutma sonucu belirleyicidir. Komşu kol daha genel bağlama alanını, bağlama yerini ve tuzak gibi ek adlandırmaları da kapsadığından sınırları tam örtüşmez.","focus_only":"Bağlamanın sıkı oluşunu ve bağlı nesnenin hareketini sınırlama sonucunu belirgin biçimde taşır.","gloss":"sıkıca bağlama ile genel bağlama","neighbor_only":"Bağlama yeri, genel bağ, ip ve kesilmiş tuzak gibi daha geniş adlandırmaları içerir.","neighbor_ref":"root_000535/B001","relation_type":"near_synonym","shared_zone":"Her iki kol da bir nesneyi ip veya benzeri bir araçla bağlayıp yerinde tutma eylemini ve aracı kapsar."},{"boundary_match":"partial","distinction":"Odak kolu sıkıca bağlama işlemi ile bağ aracına odaklanır. Komşu kol bağlamadan tutsaklık ve alıkoyma durumuna geçer, hatta gerçek bir bağ bulunmayan ve aktarmalı tutsaklık kullanımlarını da içerir.","focus_only":"Bağlama eyleminin yanı sıra kullanılan ip veya başka bağ aracını genel olarak adlandırır.","gloss":"bağlama ile tutsak etme","neighbor_only":"Tutsak etme, alıkoyma ve gerçekten bağlanmamış tutsak ile iyiliğin tutsağı gibi aktarmalı kullanımları kapsar.","neighbor_ref":"root_000030/B001","relation_type":"near_synonym","shared_zone":"Bir kişiyi veya şeyi bağlayarak hareketini sınırlama iki kolun doğrudan kesiştiği alandır."},{"boundary_match":"partial","distinction":"Odak kolu genel sıkı bağlama eylemi ve aracıdır. Komşu kol belirli bir köstek türüne yönelir ve ayrıca yazıya işaret koyma alanına uzanır; bu nedenle olağan ikame mümkün değildir.","focus_only":"Her türlü canlı veya nesneyi sıkıca bağlama eylemini ve genel bağ aracını kapsar.","gloss":"bağlama ile köstekleme","neighbor_only":"Hayvanın ayağına vurulan belirli engeli ve yazıya işaret koyarak onu sınırlama kullanımını kapsar.","neighbor_ref":"root_000813/B003","relation_type":"near_neighbor","shared_zone":"Her iki kol da bir canlıyı bağ aracıyla hareket edemez veya daha sınırlı hareket eder duruma getirebilir."},{"boundary_match":"partial","distinction":"Odak kolu hedef ve bağlama biçimi bakımından geneldir. Komşu kol yalnız devenin belirli uzuvlarını birbirine bağlayan, yürüyüşü yavaşlatmaya yönelik özel bir bağlama biçimidir.","focus_only":"Canlı veya cansız her türlü hedefin sıkıca bağlanmasını ve kullanılan aracı kapsar.","gloss":"genel bağlama ile deve bağı","neighbor_only":"Devenin dirsek ya da üst bacağını alt bacağına bağlayarak yürüyüşünü yavaşlatan özel düzeni anlatır.","neighbor_ref":"root_000583/B005","relation_type":"near_neighbor","shared_zone":"Her iki kol da bir hayvanın uzuvlarını bağlayarak hareketini azaltma durumunda örtüşür."},{"boundary_match":"partial","distinction":"Odak kolunda somut bağlama veya bağ aracı anlamın çekirdeğidir. Komşu kol genel sağlamlığı ve sağlamlaştırmayı anlatır; bağlama bunun yalnız olası yollarından biridir.","focus_only":"Somut bir bağlama işlemini, bağlı durumu ve bu işte kullanılan aracı zorunlu kılar.","gloss":"sıkıca bağlama ile sağlamlaştırma","neighbor_only":"Herhangi bir bağ aracı olmaksızın genel sağlamlık, güç ve bozulmaya dirençli olma durumunu kapsar.","neighbor_ref":"root_001623/B002","relation_type":"near_neighbor","shared_zone":"Bir şeyi sıkıca bağlamak onu yerinde tutup daha sağlam duruma getirebilir."}],"source_phrase_ar":"أوثقته إيثاقا ووثاقا؛ الوثاق الحبل (ayn)؛ أوثقت الدابة وغيرها إيثاقا؛ الوثاق: كل ما أوثقت به شيئا (jamhara)؛ أوثقه في الوثاق، أي شده؛ فشدوا الوثاق (sihah)؛ الوثاق: اسم الإيثاق؛ الحبل أو الشيء الذي يوثق به وثاق (tahdhib)؛ أوثقته: شددته؛ الوثاق والوثاق: اسمان لما يوثق به الشيء (mufradat)","source_summary":"Kaynaklar, canlı veya nesneyi sıkıca bağlama eyleminde ve bu eylemde kullanılan ipin ya da başka aracın adlandırılmasında birleşir. Aynı biçim ailesi hem yapılan işi hem de bağlama aracını karşılayabilir.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه أوثقته وإيثاقا ووثاقا، وشد الشيء أو الأسير، والوثاق بوصفه حبلا أو كل ما يوثق به الشيء.","what_is_not_ar":"ليس المراد العهد والميثاق، ولا الثقة القلبية، ولا مطلق إحكام الشيء بلا آلة أو شد."},"support_links":["sup_5e75750b5c5a308713dc","sup_6869fd2160b498124919","sup_77981ca9c5a7a11a0cf9","sup_fbcbd48c4bdefe125457","sup_fefe8979b20d01fde650"]},{"boundary":"Bu kol bağlayıcı ve pekiştirilmiş söz ya da anlaşmayla sınırlıdır; fiziksel bağ, genel sağlamlık ve kişisel güvenilirlik tek başına yeterli değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001623/B004","candidate_links":[{"candidate_id":"cand_91ffbab76826cb46a989","lane":"macro"},{"candidate_id":"cand_f4d3abf145cff1b2a3f4","lane":"macro"},{"candidate_id":"cand_407a0de6483bcc2a1afd","lane":"macro"},{"candidate_id":"cand_80d710337ef76db09173","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"يُوثِقُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yuwviqu|ROOT:wvq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:26:2:1","qac_word_ref":"89:26:2","surface_ar":"يُوثِقُ"},{"lemma_ar":"وَثَاق","morph_features":"STEM|POS:N|LEM:wavaAq|ROOT:wvq|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:26:3:1","qac_word_ref":"89:26:3","surface_ar":"وَثَاقَ"}],"gloss":"bağlayıcı ve pekiştirilmiş anlaşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tarafları bağlayan ve tutulması güçlü biçimde güvence altına alınmış söz veya anlaşma."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlaşmayı ant içme veya ek bir sözle pekiştirerek bağlayıcılığını güçlendirmek."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İki tarafın karşılıklı söz vererek bağlayıcı bir anlaşma kurması."}}],"root_ar":"و ث ق","root_id":"root_001623","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kolun güçlü bir sözle veya antla güvenceye alınmış, tarafları yükümlü kılan anlaşma çekirdeğini karşılar.","boundary_detail":"Bu kol bağlayıcı ve pekiştirilmiş söz ya da anlaşmayla sınırlıdır; fiziksel bağ, genel sağlamlık ve kişisel güvenilirlik tek başına yeterli değildir.","branch_image_ar":"الميثاق والعهد المؤكد","concept_gloss":"bağlayıcı ve pekiştirilmiş anlaşma","contextual_glosses":[{"applicability":"Tarafların uymakla yükümlü olduğu, tutulması güvenceye bağlanmış söz veya anlaşma bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tarafları yükümlü kılan güçlü söz ve anlaşma çekirdeğini korur."},"facet_ids":["F001"],"text":"bağlayıcı anlaşma","usage_role":"general"},{"applicability":"Anlaşmanın ant içme veya ek bir sözle güçlendirildiği özel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlayıcı anlaşmanın ant veya ek sözle güçlendirilmesini korur."},"facet_ids":["F002"],"text":"antla pekiştirilmiş sözleşme","usage_role":"contextual"},{"applicability":"İki tarafın birbirine söz vererek bağlayıcı bir anlaşma kurduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki tarafın karşılıklı söz verip bağ kurması yönünü korur."},"facet_ids":["F003"],"text":"karşılıklı sözleşme","usage_role":"contextual"}],"definition":"Tarafları bağlayan, tutulacağı güçlü biçimde güvence altına alınmış söz veya anlaşmadır; özellikle karşılıklı söz verme ya da ant içmeyle pekiştirilen sözleşmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tarafları bağlayan ve tutulması güçlü biçimde güvence altına alınmış söz veya anlaşma."},{"facet_id":"F002","role":"specialization","statement":"Anlaşmayı ant içme veya ek bir sözle pekiştirerek bağlayıcılığını güçlendirmek."},{"facet_id":"F003","role":"associated_use","statement":"İki tarafın karşılıklı söz vererek bağlayıcı bir anlaşma kurması."}],"identity_rationale":"Kaynak ifadesi, tutulması güçlü biçimde güvence altına alınmış söz veya anlaşmayı; bunun karşılıklı söz verme, ant içme ve anlaşma yapma biçimlerini açıkça bir araya getirir. Geçici ya da sıradan söz verme bu güçlendirilmiş bağlayıcılığı taşımadıkça kolun dışında kalır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bağlayıcı ve pekiştirilmiş anlaşma"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"güvenceye bağlanmış anlaşma"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"karşılıklı sözleşme"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"Tanrı'yı tanık tutup yapacağına söz verdi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"ondan bağlayıcı güvence aldı"}],"lexicalization_note":"Tanım, bağlayıcı anlaşma çekirdeğini ad, karşılıklı sözleşme ve antla pekiştirilmiş söz verme biçimlerinde ayırır; bunları sıradan söz vermeye genellemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; korunan söz, genel yükümlülük kurma, karşılıklı söz verme, güvence bağı ve aynı kökün somut bağlama kolu en açıklayıcı karşılaştırmaları sağladı. Diğerleri daha uzak işlem türleri veya bu sınırların yinelemeleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kolunda anlaşmanın sağlamlaştırılması, karşılıklı kurulması ve antla pekiştirilmesi öne çıkar. Komşu kol ise anlaşmanın yanında koruma ve dokunulmazlık durumlarını, bunlara bağlı kişileri de kapsar.","focus_only":"Karşılıklı sözleşme yapma ve belirli bir işi antla üstlenme eylemlerini açıkça içerir.","gloss":"pekiştirilmiş anlaşma ile korunan söz","neighbor_only":"Koruma, dokunulmazlık, güvence ilişkisi ve bu ilişkiye bağlı kişi veya topluluk durumlarını da kapsar.","neighbor_ref":"root_001055/B003","relation_type":"near_synonym","shared_zone":"Her iki kol da tarafları bağlayan, tutulması beklenen güçlü bir anlaşma veya sözü anlatır."},{"boundary_match":"partial","distinction":"Odak kolunun ayırıcı yönü anlaşmanın güçlü bir söz veya antla güvenceye alınmasıdır. Komşu kol ise yükümlülük kuran işlemleri daha geniş biçimde kapsar; bu tür pekiştirme her zaman gerekli değildir.","focus_only":"Anlaşmanın güçlü bir söz veya antla pekiştirilmiş ve güvenceye alınmış olmasını gerektirir.","gloss":"pekiştirilmiş anlaşma ile yükümlülük kurma","neighbor_only":"Alım satım, evlenme ve her türlü hukuki yükümlülük kurma gibi daha geniş işlem türlerini kapsar.","neighbor_ref":"root_001034/B002","relation_type":"near_synonym","shared_zone":"İki kol da tarafları bağlayan ve onlara uyma yükümlülüğü getiren anlaşmalar alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak kolu ortaya çıkan güçlü ve bağlayıcı anlaşmayı merkez alır. Komşu kol ise yalnız iki taraflı söz verme olayını merkez alır; sözlerin ayrıca güvenceye bağlanması zorunlu değildir.","focus_only":"Kurulan anlaşmanın bağlayıcı ve güçlü biçimde güvenceye alınmış olmasını anlatır.","gloss":"bağlayıcı anlaşma ile karşılıklı söz verme","neighbor_only":"İki tarafın birbirine söz vermesi eylemini anlatır; sözlerin bağlayıcı bir anlaşmaya dönüşmesi gerekmez.","neighbor_ref":"root_001662/B004","relation_type":"near_neighbor","shared_zone":"Karşılıklı söz verme, taraflar arasında bağlayıcı bir anlaşma kurulmasının bir yolu olabilir."},{"boundary_match":"partial","distinction":"Odak kolunda güçlü sözleşme ve yükümlülük çekirdektir. Komşu kol anlaşmanın yanında koruma, güvenlik ve genel bağlantı araçlarını da kapsar; bu yüzden anlam alanı daha geniştir.","focus_only":"Pekiştirilmiş söz veya anlaşmanın tarafları yükümlü kılan yönünü öne çıkarır.","gloss":"bağlayıcı anlaşma ile güvence bağı","neighbor_only":"Koruma, güvenlik, komşuluk ve kişiler ya da şeyler arasında bağlantı kurma gibi daha geniş ilişkileri kapsar.","neighbor_ref":"root_000291/B002","relation_type":"near_neighbor","shared_zone":"Güvence ve korunma sağlayan bir anlaşma, iki kolun ortak kullanım alanını oluşturabilir."},{"boundary_match":"thematic_only","distinction":"Odak kolundaki bağ, kişilerin uyması gereken söz ve anlaşma üzerinden kurulur. Komşu koldaki bağ ise somut bir araçla fiziksel olarak kurulur; aralarında olağan anlam ikamesi yoktur.","focus_only":"Kişileri verdikleri söze bağlayan soyut ve toplumsal bir yükümlülük kurar.","gloss":"sözle bağlama ile iple bağlama","neighbor_only":"Canlı veya nesneyi iple ya da başka bir araçla somut olarak bağlayıp hareketini sınırlar.","neighbor_ref":"root_001623/B003","relation_type":"thematic","shared_zone":"Her iki kol da bir şeyi serbest bırakmayan, onu belirli bir durumda tutan bağ düşüncesiyle ilişkilidir."}],"source_phrase_ar":"الميثاق: العهد المحكم (maqayis)؛ الميثاق من المواثقة والمعاهدة ومنه الموثق؛ واثقته بالله لأفعلن (ayn;tahdhib)؛ الميثاق: العهد؛ والجمع مواثيق (jamhara)؛ الميثاق: العهد؛ الموثق: الميثاق؛ المواثقة: المعاهدة (sihah)؛ الميثاق: عقد مؤكد بيمين وعهد؛ والموثق الاسم منه (mufradat)","source_summary":"Kaynaklar, tutulması güvenceye bağlanmış güçlü söz veya anlaşma çekirdeğinde birleşir. Karşılıklı sözleşme, ant içerek belirli bir işi yapmayı üstlenme ve böyle bir güvenceyi karşı taraftan alma bu çekirdeğin başlıca gerçekleşmeleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الميثاق والموثق والمواثقة والمعاهدة، والعهد المحكم أو العقد المؤكد بيمين وعهد.","what_is_not_ar":"لا يدخل فيه مجرد الوثاق الحسي، ولا وصف الشخص بأنه ثقة، ولا إحكام الشيء إلا إذا صار عهدا موثقا."},"support_links":["sup_54465687a6e135567fc3","sup_559fab728286458e241c","sup_6869fd2160b498124919","sup_a322f69eb4f5ec97f50a"]},{"boundary":"It includes a person, heart, or soul becoming still, and confidence or rest toward something after unrest.","branch_kind":null,"branch_ref":"root_003669/B001","candidate_links":[{"candidate_id":"cand_7c69e717657cbe5f5791","lane":"macro"},{"candidate_id":"cand_fb9181681c8a792269f1","lane":"macro"}],"focus_root_occurrences":[],"gloss":"settling into calm","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"السكون بعد الانزعاج","image_en":"settling into calm"}}],"root_ar":"ط م ن","root_id":"root_003669","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"السكون بعد الانزعاج","image_en":"settling into calm","scope_ar":"يدخل فيه سكون الرجل والقلب والنفس والطمأنينة والاطمئنان إلى الشيء بعد اضطراب أو انزعاج","scope_en":"It includes a person, heart, or soul becoming still, and confidence or rest toward something after unrest."},"support_links":["sup_22731a5850a177d357e0","sup_e735f60954e26a6d1f49"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000025/B006","candidate_links":[{"candidate_id":"cand_df7cb0e9b7256a09cebd","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2113a5b8a350428bc898","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Clinging and weighting oneself to earth supplies the foothold that leveling makes unavailable.","root":"ء ر ض","source_ref":"89:21","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000025","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_df7bc0986b1725eab3ec"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000043/B004","candidate_links":[{"candidate_id":"cand_f4d3abf145cff1b2a3f4","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e30c351b4ffdbe17a27a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Consumption and taking of property turn neglected obligation into active appropriation.","root":"ء ك ل","source_ref":"89:19","source_word_indices":["1","3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000043","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_559fab728286458e241c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000261/B001","candidate_links":[{"candidate_id":"cand_f4d3abf145cff1b2a3f4","lane":"macro"},{"candidate_id":"cand_7de2443661e049279fb8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e30c351b4ffdbe17a27a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Accumulation toward fullness supplies the concentrating endpoint of withheld and consumed goods.","root":"ج م م","source_ref":"89:20","source_word_indices":["4"]},{"hft_ref":"hft_6e528545be6cc1bf043d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Gathering until full supplies the cumulative pressure that turns preference into fixation.","root":"ج م م","source_ref":"89:20","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000261","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_559fab728286458e241c","sup_77981ca9c5a7a11a0cf9"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000266/B008","candidate_links":[{"candidate_id":"cand_80d710337ef76db09173","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fd5ca51fa1fc3fb28dec","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Protective covering supplies enclosure as shelter, a functional reversal of punitive confinement.","root":"ج ن ن","source_ref":"89:30","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000266","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6869fd2160b498124919"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000286/B002","candidate_links":[{"candidate_id":"cand_f4d3abf145cff1b2a3f4","lane":"macro"},{"candidate_id":"cand_7de2443661e049279fb8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e30c351b4ffdbe17a27a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Love that stays attached to the heart supplies the inward adhesion sustaining appropriation.","root":"ح ب ب","source_ref":"89:20","source_word_indices":["1","3"]},{"hft_ref":"hft_6e528545be6cc1bf043d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Love adhering to the heart supplies the inward bond that precedes imposed restraint.","root":"ح ب ب","source_ref":"89:20","source_word_indices":["1","3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000286","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_559fab728286458e241c","sup_77981ca9c5a7a11a0cf9"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000286/B005","candidate_links":[{"candidate_id":"cand_7de2443661e049279fb8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6e528545be6cc1bf043d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Remaining fixed in place through incapacity supplies the surprising immobilization latent inside the love root.","root":"ح ب ب","source_ref":"89:20","source_word_indices":["1","3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000286","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_77981ca9c5a7a11a0cf9"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000464/B001","candidate_links":[{"candidate_id":"cand_80d710337ef76db09173","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fd5ca51fa1fc3fb28dec","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Entry into an interior supplies voluntary admission as the spatial opposite of being held from escape.","root":"د خ ل","source_ref":"89:29","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000464","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6869fd2160b498124919"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000482/B001","candidate_links":[{"candidate_id":"cand_df7cb0e9b7256a09cebd","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2113a5b8a350428bc898","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Pounding and demolition to levelness remove the old material structures and hiding places.","root":"د ك ك","source_ref":"89:21","source_word_indices":["3","5","6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000482","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_df7bc0986b1725eab3ec"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000516/B008","candidate_links":[{"candidate_id":"cand_407a0de6483bcc2a1afd","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_22fffcc8209be5356364","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A remembered right as deed or documentary proof supplies evidence that can make the focus compact operative.","root":"ذ ك ر","source_ref":"89:23","source_word_indices":["5","9"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000516","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_54465687a6e135567fc3"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000544/B001","candidate_links":[{"candidate_id":"cand_11e5939c0c158e0e5dc0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_4ab46ef198e93368a4d7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Return to a prior place supplies directed movement completed by belonging rather than blocked by a bond.","root":"ر ج ع","source_ref":"89:28","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000544","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5e75750b5c5a308713dc"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000569/B003","candidate_links":[{"candidate_id":"cand_11e5939c0c158e0e5dc0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_4ab46ef198e93368a4d7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Mutual satisfaction supplies reciprocal acceptance, the relational condition under which trust can settle.","root":"ر ض و","source_ref":"89:28","source_word_indices":["4","5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000569","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5e75750b5c5a308713dc"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000871/B001","candidate_links":[{"candidate_id":"cand_df7cb0e9b7256a09cebd","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2113a5b8a350428bc898","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Alignment on a level line supplies gapless order across the transformed field.","root":"ص ف ف","source_ref":"89:22","source_word_indices":["4","5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000871","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_df7bc0986b1725eab3ec"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000948/B001","candidate_links":[{"candidate_id":"cand_11e5939c0c158e0e5dc0","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_4ab46ef198e93368a4d7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Tranquility and stillness supply a willing mode of settledness adjacent to the imposed stillness of restraint.","root":"ط م ن","source_ref":"89:27","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000948","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5e75750b5c5a308713dc"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000973/B001","candidate_links":[{"candidate_id":"cand_80d710337ef76db09173","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fd5ca51fa1fc3fb28dec","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Servitude as ownership supplies the custody relation shared, uneasily, by bondage and belonging.","root":"ع ب د","source_ref":"89:29","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000973","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6869fd2160b498124919"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000973/B003","candidate_links":[{"candidate_id":"cand_80d710337ef76db09173","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fd5ca51fa1fc3fb28dec","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Submissive obedience supplies accepted service, differentiating incorporated belonging from forced restraint.","root":"ع ب د","source_ref":"89:29","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000973","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6869fd2160b498124919"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000994/B005","candidate_links":[{"candidate_id":"cand_00b2bfe089da4b527c3f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_f0624974b05763234cf4","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Painful punishment supplies the first sanction, against which binding distinguishes loss of agency from inflicted pain.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000994","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_fbcbd48c4bdefe125457"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001207/B004","candidate_links":[{"candidate_id":"cand_407a0de6483bcc2a1afd","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_22fffcc8209be5356364","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Advancing something forward supplies the prior conduct now presented into the evidentiary moment.","root":"ق د م","source_ref":"89:24","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001207","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_54465687a6e135567fc3"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001444/B001","candidate_links":[{"candidate_id":"cand_df7cb0e9b7256a09cebd","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2113a5b8a350428bc898","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Strength and cohesion activate the host as a unified securing presence rather than a loose crowd.","root":"م ل ك","source_ref":"89:22","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001444","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_df7bc0986b1725eab3ec"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001444/B009","candidate_links":[{"candidate_id":"cand_df7cb0e9b7256a09cebd","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2113a5b8a350428bc898","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The angel branch identifies the ordered host occupying the newly leveled scene.","root":"م ل ك","source_ref":"89:22","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001444","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_df7bc0986b1725eab3ec"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001457/B001","candidate_links":[{"candidate_id":"cand_7de2443661e049279fb8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6e528545be6cc1bf043d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Acquiring and multiplying wealth supplies the object around which attachment tightens.","root":"م و ل","source_ref":"89:20","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001457","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_77981ca9c5a7a11a0cf9"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001639/B001","candidate_links":[{"candidate_id":"cand_f4d3abf145cff1b2a3f4","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e30c351b4ffdbe17a27a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Transfer from predecessor to heir supplies the relational property whose passage has been devoured rather than honored.","root":"و ر ث","source_ref":"89:19","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001639","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_559fab728286458e241c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001692/B001","candidate_links":[{"candidate_id":"cand_f4d3abf145cff1b2a3f4","lane":"macro"},{"candidate_id":"cand_fc0f7d806678b91d369b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e30c351b4ffdbe17a27a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A child cut off from a guardian supplies the broken protective relation at the start of the social mechanism.","root":"ي ت م","source_ref":"89:17","source_word_indices":["5"]},{"hft_ref":"hft_12239825e77dc83d2fdc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Severance of a child from a guardian supplies the concrete withdrawal of reliable support.","root":"ي ت م","source_ref":"89:17","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001692","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_559fab728286458e241c","sup_fefe8979b20d01fde650"]}],"candidate_inventory":[{"anchor_refs":["89:18","89:26","89:27"],"branch_refs":["root_000726/B001","root_000726/B004","root_001623/B001","root_003669/B001"],"candidate_id":"cand_7c69e717657cbe5f5791","commentary_obligation":"review","focus_branch_refs":["root_001623/B001"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000726/B001","root_000726/B004","root_003669/B001"],"root_ids":[],"scope":"pericope","source_local_id":"C:Stillness, Comfort, and Trust","source_type":"channel","support_ids":["sup_22731a5850a177d357e0","sup_3412cbb84d8c8f1c371a","sup_3782e6e5868cfd419d59","sup_a0b095941a5812b81663","sup_dbd533f53cc08694df7a"],"title":"Stillness, Comfort, and Trust","trust":"trusted","unresolved_branch_citations":[{"citation":"ط م ء ن/B001","reason":"no registered branch match"}],"unresolved_branch_refs":[]},{"anchor_refs":["89:18","89:22","89:26","89:27"],"branch_refs":["root_000281/B005","root_000726/B008","root_001623/B001","root_003669/B001"],"candidate_id":"cand_fb9181681c8a792269f1","commentary_obligation":"review","focus_branch_refs":["root_001623/B001"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000281/B005","root_000726/B008","root_003669/B001"],"root_ids":[],"scope":"pericope","source_local_id":"E:Rudder and Stabilized Vessel","source_type":"channel","support_ids":["sup_04e48a6911d391f9390e","sup_ba96cb1c1b549be2c68c","sup_d6352d66637b9312b2eb","sup_e735f60954e26a6d1f49","sup_ec78846382fa750c520d"],"title":"Rudder and Stabilized Vessel","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:22","89:26","89:28","89:29"],"branch_refs":["root_000464/B002","root_000544/B004","root_001444/B004","root_001623/B004"],"candidate_id":"cand_91ffbab76826cb46a989","commentary_obligation":"review","focus_branch_refs":["root_001623/B004"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000464/B002","root_000544/B004","root_001444/B004"],"root_ids":[],"scope":"pericope","source_local_id":"F:Marriage as Binding Contract","source_type":"channel","support_ids":["sup_4b5b95241de1b5112498","sup_5997fc8b9765a6ad1474","sup_9233876e5056040af093","sup_a322f69eb4f5ec97f50a","sup_e6841fd48f20a0c63dac"],"title":"Marriage as Binding Contract","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:17","89:19","89:20","89:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:26","branch_refs":["root_000043/B004","root_000261/B001","root_000286/B002","root_001623/B004","root_001639/B001","root_001692/B001"],"candidate_id":"cand_f4d3abf145cff1b2a3f4","commentary_obligation":"review","hft_ref":"hft_e30c351b4ffdbe17a27a","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:social_obligation_returns","source_type":"hft","support_ids":["sup_559fab728286458e241c"],"title":"social_obligation_returns","trust":"legacy_unbound"},{"anchor_refs":["89:20","89:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:26","branch_refs":["root_000261/B001","root_000286/B002","root_000286/B005","root_001457/B001","root_001623/B002","root_001623/B003"],"candidate_id":"cand_7de2443661e049279fb8","commentary_obligation":"review","hft_ref":"hft_6e528545be6cc1bf043d","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:desire_becomes_restraint","source_type":"hft","support_ids":["sup_77981ca9c5a7a11a0cf9"],"title":"desire_becomes_restraint","trust":"legacy_unbound"},{"anchor_refs":["89:21","89:22","89:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:26","branch_refs":["root_000025/B006","root_000482/B001","root_000871/B001","root_001444/B001","root_001444/B009","root_001623/B002"],"candidate_id":"cand_df7cb0e9b7256a09cebd","commentary_obligation":"review","hft_ref":"hft_2113a5b8a350428bc898","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:leveled_world_systemic_closure","source_type":"hft","support_ids":["sup_df7bc0986b1725eab3ec"],"title":"leveled_world_systemic_closure","trust":"legacy_unbound"},{"anchor_refs":["89:23","89:24","89:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:26","branch_refs":["root_000516/B008","root_001207/B004","root_001623/B004"],"candidate_id":"cand_407a0de6483bcc2a1afd","commentary_obligation":"review","hft_ref":"hft_22fffcc8209be5356364","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:remembered_record_binds","source_type":"hft","support_ids":["sup_54465687a6e135567fc3"],"title":"remembered_record_binds","trust":"legacy_unbound"},{"anchor_refs":["89:25","89:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:26","branch_refs":["root_000017/B002","root_000994/B005","root_001623/B003"],"candidate_id":"cand_00b2bfe089da4b527c3f","commentary_obligation":"review","hft_ref":"hft_f0624974b05763234cf4","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:paired_unmatched_sanctions","source_type":"hft","support_ids":["sup_fbcbd48c4bdefe125457"],"title":"paired_unmatched_sanctions","trust":"legacy_unbound"},{"anchor_refs":["89:26","89:27","89:28"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:26","branch_refs":["root_000544/B001","root_000569/B003","root_000948/B001","root_001623/B001","root_001623/B003"],"candidate_id":"cand_11e5939c0c158e0e5dc0","commentary_obligation":"review","hft_ref":"hft_4ab46ef198e93368a4d7","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:coerced_vs_tranquil_settlement","source_type":"hft","support_ids":["sup_5e75750b5c5a308713dc"],"title":"coerced_vs_tranquil_settlement","trust":"legacy_unbound"},{"anchor_refs":["89:26","89:29","89:30"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:26","branch_refs":["root_000266/B008","root_000464/B001","root_000973/B001","root_000973/B003","root_001623/B003","root_001623/B004"],"candidate_id":"cand_80d710337ef76db09173","commentary_obligation":"review","hft_ref":"hft_fd5ca51fa1fc3fb28dec","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:custody_vs_belonging_enclosure","source_type":"hft","support_ids":["sup_6869fd2160b498124919"],"title":"custody_vs_belonging_enclosure","trust":"legacy_unbound"},{"anchor_refs":["89:17","89:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:26","branch_refs":["root_001623/B001","root_001623/B003","root_001692/B001"],"candidate_id":"cand_fc0f7d806678b91d369b","commentary_obligation":"review","hft_ref":"hft_12239825e77dc83d2fdc","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_withdrawn_reliance_as_restraint","source_type":"hft","support_ids":["sup_fefe8979b20d01fde650"],"title":"outlier_withdrawn_reliance_as_restraint","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_c5bc8f2abb43c8417639","connection_ref":"conn_5ae816547e7e89aa74a3","note":"Immediate parallel: unmatched punishment supplies the paired punitive frame.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_5ded756ce70d4bc218a0","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:25","source_note":"Adjacent parallel: unmatched binding reinforces unmatched punishment.","source_row_role":"ranked_review","source_target_component_ref":"89:26","source_target_components":["89:26"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:26"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:25","source_target_components":["89:25"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:25","target_evidence":{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","ayah_ref":"89:25"},"target_ref":"89:25"},{"connection_evidence_ref":"conn_ev_3a09ec4a0aeb4c997805","connection_ref":"conn_ece3773f7f7f8f2b5911","note":"Adjacent contrast begins the calm-soul sequence after punitive binding.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_122e224682434f3ab30a","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"89:27","source_note":"Immediate judgment sequence sharpens the contrast with the addressed soul.","source_row_role":"ranked_review","source_target_component_ref":"89:26","source_target_components":["89:26"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:26"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:27","source_target_components":["89:27"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:27","target_evidence":{"arabic_uthmani":"يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ","ayah_ref":"89:27"},"target_ref":"89:27"},{"connection_evidence_ref":"conn_ev_54457f8c80347b32dd59","connection_ref":"conn_e45a370385c5fe5c1703","note":"Immediate context of neglected care, but no distinct binding route.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_cc5dab58aa0588cb5009","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"89:18","source_note":"No discernible contribution to the focal care or provision question.","source_row_role":"ranked_review","source_target_component_ref":"89:26","source_target_components":["89:26"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:26"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:18","source_target_components":["89:18"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:18","target_evidence":{"arabic_uthmani":"وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ","ayah_ref":"89:18"},"target_ref":"89:18"},{"connection_evidence_ref":"conn_ev_614c959aa91c5f76b47e","connection_ref":"conn_20728b58f7907fb2f2de","note":"Immediate judgment-arrival context prepares the unmatched punitive binding.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_1904cb5de6abac1a4191","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"89:22","source_note":"The immediate, incomparable punishment develops the scene's judicial aftermath.","source_row_role":"ranked_review","source_target_component_ref":"89:26","source_target_components":["89:26"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:26"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:22","source_target_components":["89:22"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:22","target_evidence":{"arabic_uthmani":"وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا","ayah_ref":"89:22"},"target_ref":"89:22"},{"connection_evidence_ref":"conn_ev_a4507394b8c2732d573a","connection_ref":"conn_be72e692e3af80c279cc","note":"Adjacent destination after the calm-soul contrast; secondary counterframe.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_b3b66ace34d100cc68f3","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"89:30","source_note":"Completes the immediate punitive contrast through binding before 89:27-30.","source_row_role":"ranked_review","source_target_component_ref":"89:26","source_target_components":["89:26"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:26"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:30","source_target_components":["89:30"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:30","target_evidence":{"arabic_uthmani":"وَٱدْخُلِى جَنَّتِى","ayah_ref":"89:30"},"target_ref":"89:30"},{"connection_evidence_ref":"conn_ev_c434be2d9f0f3356ea04","connection_ref":"conn_9cf53582a74e6a0156ff","note":"Adjacent incorporation into servants supplies the opposite communal destination.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_e09e064b1b6e833632d6","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:29","source_note":"Earlier binding/punishment context has no focused route.","source_row_role":"ranked_review","source_target_component_ref":"89:26","source_target_components":["89:26"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:26"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:29","source_target_components":["89:29"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:29","target_evidence":{"arabic_uthmani":"فَٱدْخُلِى فِى عِبَٰدِى","ayah_ref":"89:29"},"target_ref":"89:29"},{"connection_evidence_ref":"conn_ev_bc5a6c1dcd8ebd463444","connection_ref":"conn_0e7af2e85769a259d5c0","note":"Immediate judgment/remembrance context underlies the punitive sequence.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_c3d41347e081e9022a90","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:23","source_note":"Immediate continuation: no binding matches the punishment of that Day.","source_row_role":"ranked_review","source_target_component_ref":"89:26","source_target_components":["89:26"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:26"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:23","source_target_components":["89:23"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:23","target_evidence":{"arabic_uthmani":"وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ","ayah_ref":"89:23"},"target_ref":"89:23"},{"connection_evidence_ref":"conn_ev_5ca91e6dfd0066f26c4d","connection_ref":"conn_a46777fb52ca63ae73fd","note":"Immediate contrast: contented, accepted return opposes coercive fixing.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_dacaf27842567717a634","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:28","source_note":"No clear addition; it completes the punishment description.","source_row_role":"ranked_review","source_target_component_ref":"89:26","source_target_components":["89:26"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:26"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:28","source_target_components":["89:28"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:28","target_evidence":{"arabic_uthmani":"ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ","ayah_ref":"89:28"},"target_ref":"89:28"},{"connection_ref":"conn_e67cc1a3cd7345c674da","note":null,"origin":"derived_reciprocal_seed","prior_label":null,"qualification":{"boundary":"At least one source-direction review meaningfully linked this target back to the focus ayah. Treat its note and label only as a discovery nomination. Reassess the relation from the focus ayah using the supplied exact target Arabic; do not invent missing target morphology or inherit the source label.","derived_reciprocal_counterevidence":false,"derived_reciprocal_seed":true,"has_missing_ayah_suggestion_source_row":true,"has_ranked_review_source_row":false,"has_reciprocal_counterevidence":false,"has_reciprocal_nomination":true,"receiving_direction_requires_fresh_assessment":true,"source_direction_labels_are_not_focus_decisions":true,"source_row_roles_are_provenance_not_decisions":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_613447302e67bd4aaf74","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:19","source_note":"The unmatched binding follows the focus's judgment sequence, indirectly.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"89:26","source_target_components":["89:26"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:26"}],"relation_scope":"declared_pericope_reciprocal_evidence","target_evidence":{"arabic_uthmani":"وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا","ayah_ref":"89:19"},"target_ref":"89:19"}],"focus":{"arabic_uthmani":"وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:26:1:1","qac_word_ref":"89:26:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"89:26:1:2","qac_word_ref":"89:26:1","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"يُوثِقُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yuwviqu|ROOT:wvq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:26:2:1","qac_word_ref":"89:26:2","root_ar":"و ث ق","surface_ar":"يُوثِقُ"},{"lemma_ar":"وَثَاق","morph_features":"STEM|POS:N|LEM:wavaAq|ROOT:wvq|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:26:3:1","qac_word_ref":"89:26:3","root_ar":"و ث ق","surface_ar":"وَثَاقَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:26:3:2","qac_word_ref":"89:26:3","root_ar":"","surface_ar":"هُۥٓ"},{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:26:4:1","qac_word_ref":"89:26:4","root_ar":"ء ح د","surface_ar":"أَحَدٌ"}],"word_analysis_qac_refs":[["89:26:1:1"],["89:26:1:2"],["89:26:2:1"],["89:26:3:1","89:26:3:2"],["89:26:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:26:1","89:26:2","89:26:3","89:26:4","89:26:5"]},"focus_surface_evidence":{"arabic_uthmani":"وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:26:1:1","qac_word_ref":"89:26:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"89:26:1:2","qac_word_ref":"89:26:1","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"يُوثِقُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yuwviqu|ROOT:wvq|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:26:2:1","qac_word_ref":"89:26:2","root_ar":"و ث ق","surface_ar":"يُوثِقُ"},{"lemma_ar":"وَثَاق","morph_features":"STEM|POS:N|LEM:wavaAq|ROOT:wvq|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:26:3:1","qac_word_ref":"89:26:3","root_ar":"و ث ق","surface_ar":"وَثَاقَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:26:3:2","qac_word_ref":"89:26:3","root_ar":"","surface_ar":"هُۥٓ"},{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:26:4:1","qac_word_ref":"89:26:4","root_ar":"ء ح د","surface_ar":"أَحَدٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:26:1:1"],["89:26:1:2"],["89:26:2:1"],["89:26:3:1","89:26:3:2"],["89:26:4:1"]],"word_analysis_refs":["89:26:1","89:26:2","89:26:3","89:26:4","89:26:5"],"word_rows":[{"analysis_record_ref":"89:26:1","analytic_gloss_range_en":"coordinating continuation; locally attaches the binding denial to the prior punishment denial","analytic_root_gloss_range_en":null,"qac_refs":["89:26:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"89:26:2","analytic_gloss_range_en":"declarative negation over the binding predicate, its cognate measure, and the delayed indefinite subject","analytic_root_gloss_range_en":null,"qac_refs":["89:26:1:2"],"root":{},"surface":{"arabic":"لَا","transliteration":"lā"}},{"analysis_record_ref":"89:26:3","analytic_gloss_range_en":"to bind or fasten firmly in a negated Form IV judgment predicate; locally objectless except for the same-root measure","analytic_root_gloss_range_en":"root range includes trust, firmness, fastening, and covenant; local Form IV selects imposed binding, with firmness and covenant certainty as bounded color","qac_refs":["89:26:2:1"],"root":{"arabic":"و ث ق","transliteration":"w-th-q"},"surface":{"arabic":"يُوثِقُ","transliteration":"yūthiqu"}},{"analysis_record_ref":"89:26:4","analytic_gloss_range_en":"his binding, binding-measure, or mode of restraint; locally same-root accusative measure with an attached 3ms suffix","analytic_root_gloss_range_en":"root range includes trust, firmness, fastening, and covenant; local noun selects binding measure, with firmness and covenant certainty as bounded color","qac_refs":["89:26:3:1","89:26:3:2"],"root":{"arabic":"و ث ق","transliteration":"w-th-q"},"surface":{"arabic":"وَثَاقَهُۥٓ","transliteration":"wathāqahu"}},{"analysis_record_ref":"89:26:5","analytic_gloss_range_en":"any one, no single one under negation; locally the delayed indefinite nominative subject universalized by {{ar:لَا}} ({{tr:lā}})","analytic_root_gloss_range_en":"one-ness, singleness, and individual unit force; local negation turns the singular into universal exclusion","qac_refs":["89:26:4:1"],"root":{"arabic":"أ ح د","transliteration":"ʾ-ḥ-d"},"surface":{"arabic":"أَحَدٌۭ","transliteration":"aḥadun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":13,"missing_anchor_refs":[],"supplied_unique_anchor_count":13},"assigned_record_count":8,"assigned_records":[{"anchor_refs":["89:17","89:19","89:20","89:26"],"branch_refs":["root_000043/B004","root_000261/B001","root_000286/B002","root_001623/B004","root_001639/B001","root_001692/B001"],"candidate_id":"cand_f4d3abf145cff1b2a3f4","evidence_scope":"declared_pericope","hft_ref":"hft_e30c351b4ffdbe17a27a","item_id":"social_obligation_returns","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:social_obligation_returns","support_id":"sup_559fab728286458e241c"},{"anchor_refs":["89:20","89:26"],"branch_refs":["root_000261/B001","root_000286/B002","root_000286/B005","root_001457/B001","root_001623/B002","root_001623/B003"],"candidate_id":"cand_7de2443661e049279fb8","evidence_scope":"declared_pericope","hft_ref":"hft_6e528545be6cc1bf043d","item_id":"desire_becomes_restraint","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:desire_becomes_restraint","support_id":"sup_77981ca9c5a7a11a0cf9"},{"anchor_refs":["89:21","89:22","89:26"],"branch_refs":["root_000025/B006","root_000482/B001","root_000871/B001","root_001444/B001","root_001444/B009","root_001623/B002"],"candidate_id":"cand_df7cb0e9b7256a09cebd","evidence_scope":"declared_pericope","hft_ref":"hft_2113a5b8a350428bc898","item_id":"leveled_world_systemic_closure","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:leveled_world_systemic_closure","support_id":"sup_df7bc0986b1725eab3ec"},{"anchor_refs":["89:23","89:24","89:26"],"branch_refs":["root_000516/B008","root_001207/B004","root_001623/B004"],"candidate_id":"cand_407a0de6483bcc2a1afd","evidence_scope":"declared_pericope","hft_ref":"hft_22fffcc8209be5356364","item_id":"remembered_record_binds","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:remembered_record_binds","support_id":"sup_54465687a6e135567fc3"},{"anchor_refs":["89:25","89:26"],"branch_refs":["root_000017/B002","root_000994/B005","root_001623/B003"],"candidate_id":"cand_00b2bfe089da4b527c3f","evidence_scope":"declared_pericope","hft_ref":"hft_f0624974b05763234cf4","item_id":"paired_unmatched_sanctions","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:paired_unmatched_sanctions","support_id":"sup_fbcbd48c4bdefe125457"},{"anchor_refs":["89:26","89:27","89:28"],"branch_refs":["root_000544/B001","root_000569/B003","root_000948/B001","root_001623/B001","root_001623/B003"],"candidate_id":"cand_11e5939c0c158e0e5dc0","evidence_scope":"declared_pericope","hft_ref":"hft_4ab46ef198e93368a4d7","item_id":"coerced_vs_tranquil_settlement","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:coerced_vs_tranquil_settlement","support_id":"sup_5e75750b5c5a308713dc"},{"anchor_refs":["89:26","89:29","89:30"],"branch_refs":["root_000266/B008","root_000464/B001","root_000973/B001","root_000973/B003","root_001623/B003","root_001623/B004"],"candidate_id":"cand_80d710337ef76db09173","evidence_scope":"declared_pericope","hft_ref":"hft_fd5ca51fa1fc3fb28dec","item_id":"custody_vs_belonging_enclosure","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:custody_vs_belonging_enclosure","support_id":"sup_6869fd2160b498124919"},{"anchor_refs":["89:17","89:26"],"branch_refs":["root_001623/B001","root_001623/B003","root_001692/B001"],"candidate_id":"cand_fc0f7d806678b91d369b","evidence_scope":"declared_pericope","hft_ref":"hft_12239825e77dc83d2fdc","item_id":"outlier_withdrawn_reliance_as_restraint","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_withdrawn_reliance_as_restraint","support_id":"sup_fefe8979b20d01fde650"}],"diagnostics":[],"lane_counts":{"global":15,"macro":8,"micro":4},"packet_summary":{"ayah_count":30,"focus_ref":"89:26","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:26","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":19,"unstructured_record_count":0},"identity":{"ayah_ref":"89:26","lane":"macro","linguistic_source_ref":"89:26","surface_ref":"89:26","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:26","target_tokens":[["Hiç",["89:26:4"]],["kimse",["89:26:4"]],["de",["89:26:1"]],["onun",["89:26:3"]],["bağlayışı",["89:26:3"]],["gibi",["89:26:3"]],["bağlayamaz",["89:26:1","89:26:2"]]],"text":"Hiç kimse de onun bağlayışı gibi bağlayamaz."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":8,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":15,"ayah_to":30,"id":"s089-p02-015-030","label":"The wealth test, judgment, and tranquil soul","number":2,"refs":["89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"89:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"89:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["89:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"89:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"E:Rudder and Stabilized Vessel","source_type":"channel","support_id":"sup_04e48a6911d391f9390e","text":"Raw material is shaped, joined, tensioned, or folded into a tool with a specific function.","trust":"trusted"},{"branch_refs":["root_000726/B001","root_000726/B004","root_001623/B001","root_003669/B001"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"C:Stillness, Comfort, and Trust","source_type":"channel","support_id":"sup_22731a5850a177d357e0","text":"stillness `س ك ن:B001/m01`; comfort `س ك ن:B004/m01`; tranquility `ط م ء ن:B001/m01`; calm `ط م ن:B001/m01`; trust `و ث ق:B001/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Stillness, Comfort, and Trust","source_type":"channel","support_id":"sup_3412cbb84d8c8f1c371a","text":"89:18 (المسكين); 89:27 (المطمئنة); 89:26 (وثاقه)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Stillness, Comfort, and Trust","source_type":"channel","support_id":"sup_3782e6e5868cfd419d59","text":"The scene traces an embodied transition from motion to repose and then to relational assurance.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"F:Marriage as Binding Contract","source_type":"channel","support_id":"sup_4b5b95241de1b5112498","text":"89:22 (الملك); 89:28 (ارجعي); 89:26 (وثاقه); 89:29-30 (ادخلي)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"F:Marriage as Binding Contract","source_type":"channel","support_id":"sup_5997fc8b9765a6ad1474","text":"Contract, entry, continuity, and return give marriage the same durable relational structure as other covenants.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"F:Marriage as Binding Contract","source_type":"channel","support_id":"sup_9233876e5056040af093","text":"A relation becomes durable when it is sworn, trusted, physically secured, or repaired after breach.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Stillness, Comfort, and Trust","source_type":"channel","support_id":"sup_a0b095941a5812b81663","text":"A place becomes home when it affords stable entry, concealment, nourishment, and calm.","trust":"trusted"},{"branch_refs":["root_000464/B002","root_000544/B004","root_001444/B004","root_001623/B004"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"F:Marriage as Binding Contract","source_type":"channel","support_id":"sup_a322f69eb4f5ec97f50a","text":"marriage contract `م ل ك:B004/m01`; marital return `ر ج ع:B004/m01`; covenant `و ث ق:B004/m01`; consummation `د خ ل:B002/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"E:Rudder and Stabilized Vessel","source_type":"channel","support_id":"sup_ba96cb1c1b549be2c68c","text":"A rudder at the stern controls a vessel and dampens its oscillation.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"E:Rudder and Stabilized Vessel","source_type":"channel","support_id":"sup_d6352d66637b9312b2eb","text":"89:18 (المسكين); 89:27 (المطمئنة); 89:22-23 (جاء، جيء); 89:26 (وثاقه)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Stillness, Comfort, and Trust","source_type":"channel","support_id":"sup_dbd533f53cc08694df7a","text":"Movement ceases as the resident becomes calm, comfortable, and assured.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"F:Marriage as Binding Contract","source_type":"channel","support_id":"sup_e6841fd48f20a0c63dac","text":"A marriage relation is secured by contract and may be maintained or restored through accepted obligation.","trust":"trusted"},{"branch_refs":["root_000281/B005","root_000726/B008","root_001623/B001","root_003669/B001"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"E:Rudder and Stabilized Vessel","source_type":"channel","support_id":"sup_e735f60954e26a6d1f49","text":"ship rudder `س ك ن:B008/m01`; calming control `ط م ن:B001/m01`; compelled direction `ج ي ء:B005/m01`; firm reliance `و ث ق:B001/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"E:Rudder and Stabilized Vessel","source_type":"channel","support_id":"sup_ec78846382fa750c520d","text":"Vessel, steering component, controlling action, and stabilized outcome form a complete navigational mechanism.","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ","ayah_ref":"89:17"},{"arabic_uthmani":"وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا","ayah_ref":"89:19"},{"arabic_uthmani":"وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا","ayah_ref":"89:20"},{"arabic_uthmani":"وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ","ayah_ref":"89:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000043/B004","root_000261/B001","root_000286/B002","root_001623/B004","root_001639/B001","root_001692/B001"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001623","role":"The assured compact supplies the focus anchor for reading social duties as obligations with binding force.","root":"و ث ق","source_ref":"89:26","source_word_indices":["2","3"]},{"branch_id":"B001","mapped_root_id":"root_001692","role":"A child cut off from a guardian supplies the broken protective relation at the start of the social mechanism.","root":"ي ت م","source_ref":"89:17","source_word_indices":["5"]},{"branch_id":"B004","mapped_root_id":"root_000043","role":"Consumption and taking of property turn neglected obligation into active appropriation.","root":"ء ك ل","source_ref":"89:19","source_word_indices":["1","3"]},{"branch_id":"B001","mapped_root_id":"root_001639","role":"Transfer from predecessor to heir supplies the relational property whose passage has been devoured rather than honored.","root":"و ر ث","source_ref":"89:19","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000286","role":"Love that stays attached to the heart supplies the inward adhesion sustaining appropriation.","root":"ح ب ب","source_ref":"89:20","source_word_indices":["1","3"]},{"branch_id":"B001","mapped_root_id":"root_000261","role":"Accumulation toward fullness supplies the concentrating endpoint of withheld and consumed goods.","root":"ج م م","source_ref":"89:20","source_word_indices":["4"]}],"changed_reading":{"after":"The binding can be the returning force of obligations that were severed, consumed, and converted into accumulated wealth.","before":"The focus binds a body without stating what relation is being enforced."},"confidence":"medium","mechanism":"Severed guardianship, consumed inheritance, heart-fast attachment, and accumulation describe obligations displaced by appropriation. The covenant branch of the focus root lets those abandoned relations return as an enforceable bond.","model_id":"social_obligation_returns","reader_inference":"The packet supplies broken care, property transfer, consumption, attachment, and accumulation; I infer that violated social relations become the enforceable compact carried by the focus root. The alternative is that these cues identify offenders but leave وَثَاق wholly physical.","status":"strengthened","structural_cues":["89:17-20 moves from failure of care to failure of mutual urging, then to appropriation and accumulated attachment."],"trigger_roots":["ي ت م","ء ك ل","و ر ث","ح ب ب","ج م م"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:social_obligation_returns","source_type":"hft","support_id":"sup_559fab728286458e241c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا","ayah_ref":"89:20"},{"arabic_uthmani":"وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ","ayah_ref":"89:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000261/B001","root_000286/B002","root_000286/B005","root_001457/B001","root_001623/B002","root_001623/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001623","role":"Firm securing gives inward attachment a focus-anchored endpoint in completed fixity.","root":"و ث ق","source_ref":"89:26","source_word_indices":["2","3"]},{"branch_id":"B003","mapped_root_id":"root_001623","role":"Material restraint externalizes the attachment mechanism as an actual loss of movement.","root":"و ث ق","source_ref":"89:26","source_word_indices":["2","3"]},{"branch_id":"B002","mapped_root_id":"root_000286","role":"Love adhering to the heart supplies the inward bond that precedes imposed restraint.","root":"ح ب ب","source_ref":"89:20","source_word_indices":["1","3"]},{"branch_id":"B005","mapped_root_id":"root_000286","role":"Remaining fixed in place through incapacity supplies the surprising immobilization latent inside the love root.","root":"ح ب ب","source_ref":"89:20","source_word_indices":["1","3"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Acquiring and multiplying wealth supplies the object around which attachment tightens.","root":"م و ل","source_ref":"89:20","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000261","role":"Gathering until full supplies the cumulative pressure that turns preference into fixation.","root":"ج م م","source_ref":"89:20","source_word_indices":["4"]}],"changed_reading":{"after":"The final restraint can complete and expose an inward fastening already formed by adhesive, accumulating desire.","before":"The restraint arrives wholly from outside."},"confidence":"exploratory","mechanism":"Heart-fast love, wealth acquisition, and filling accumulation form an inward fastening. A branch in the love inventory adds an image of remaining in place through incapacity, allowing the final restraint to appear as the perfected exterior form of an attachment already immobilizing its subject.","model_id":"desire_becomes_restraint","reader_inference":"The packet supplies heart-attachment, immobilization, wealth-making, and accumulation; I infer a progression from self-fastening desire to imposed restraint. The live alternative is that desire explains culpability only and has no material continuity with وَثَاق.","status":"new","structural_cues":["The doubled love construction and abundance modifier immediately precede the collapse and judgment sequence."],"trigger_roots":["ح ب ب","م و ل","ج م م"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:desire_becomes_restraint","source_type":"hft","support_id":"sup_77981ca9c5a7a11a0cf9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا","ayah_ref":"89:21"},{"arabic_uthmani":"وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا","ayah_ref":"89:22"},{"arabic_uthmani":"وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ","ayah_ref":"89:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000025/B006","root_000482/B001","root_000871/B001","root_001444/B001","root_001444/B009","root_001623/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001623","role":"Firm securing anchors the changed reading in closure that can scale beyond a single implement.","root":"و ث ق","source_ref":"89:26","source_word_indices":["2","3"]},{"branch_id":"B001","mapped_root_id":"root_000482","role":"Pounding and demolition to levelness remove the old material structures and hiding places.","root":"د ك ك","source_ref":"89:21","source_word_indices":["3","5","6"]},{"branch_id":"B006","mapped_root_id":"root_000025","role":"Clinging and weighting oneself to earth supplies the foothold that leveling makes unavailable.","root":"ء ر ض","source_ref":"89:21","source_word_indices":["4"]},{"branch_id":"B009","mapped_root_id":"root_001444","role":"The angel branch identifies the ordered host occupying the newly leveled scene.","root":"م ل ك","source_ref":"89:22","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001444","role":"Strength and cohesion activate the host as a unified securing presence rather than a loose crowd.","root":"م ل ك","source_ref":"89:22","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000871","role":"Alignment on a level line supplies gapless order across the transformed field.","root":"ص ف ف","source_ref":"89:22","source_word_indices":["4","5"]}],"changed_reading":{"after":"Binding becomes systemic closure: old anchors vanish and the newly ordered field itself offers no gap or counter-position.","before":"A localized bond prevents one body from moving."},"confidence":"medium","mechanism":"The ground and its anchors are flattened, then a strong, coherent angelic presence is aligned in rows. Binding no longer depends on one rope or terrestrial fixture; the reordered field itself leaves no foothold, gap, or counter-position.","model_id":"leveled_world_systemic_closure","reader_inference":"The packet supplies leveling, earth-clinging, angelic cohesion, and straight rows; I infer that the whole reordered scene performs confinement. The alternative is that the rows are ceremonial witnesses and the focus still denotes a discrete restraint.","status":"revised","structural_cues":["Repeated cognate forms in the leveling and row clauses precede the focus's own repeated-root construction."],"trigger_roots":["د ك ك","ء ر ض","م ل ك","ص ف ف"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:leveled_world_systemic_closure","source_type":"hft","support_id":"sup_df7bc0986b1725eab3ec","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ","ayah_ref":"89:23"},{"arabic_uthmani":"يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى","ayah_ref":"89:24"},{"arabic_uthmani":"وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ","ayah_ref":"89:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000516/B008","root_001207/B004","root_001623/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001623","role":"The assured compact supplies the legal-relational bond that a record can evidence and enforce.","root":"و ث ق","source_ref":"89:26","source_word_indices":["2","3"]},{"branch_id":"B008","mapped_root_id":"root_000516","role":"A remembered right as deed or documentary proof supplies evidence that can make the focus compact operative.","root":"ذ ك ر","source_ref":"89:23","source_word_indices":["5","9"]},{"branch_id":"B004","mapped_root_id":"root_001207","role":"Advancing something forward supplies the prior conduct now presented into the evidentiary moment.","root":"ق د م","source_ref":"89:24","source_word_indices":["3"]}],"changed_reading":{"after":"The binding can be the execution of a covenantal claim whose remembered record and prior acts have become present.","before":"The restraint is imposed without an expressed evidentiary medium."},"confidence":"medium","mechanism":"Recollection activates a branch of remembered right as deed or document, while prior action is brought forward. The focus covenant is thus not abstract: its evidentiary record becomes present and acquires binding force.","model_id":"remembered_record_binds","reader_inference":"The packet supplies recollection, documentary right, and prior action brought forward; I infer the arrow from evidence to enforcement in the focus covenant. The alternative is that memory motivates regret but does not itself function as a binding record.","status":"strengthened","structural_cues":["Remembering in 89:23 immediately produces retrospective speech about what was sent ahead in 89:24, just before punishment and binding."],"trigger_roots":["ذ ك ر","ق د م"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:remembered_record_binds","source_type":"hft","support_id":"sup_54465687a6e135567fc3","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","ayah_ref":"89:25"},{"arabic_uthmani":"وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ","ayah_ref":"89:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000017/B002","root_000994/B005","root_001623/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001623","role":"The binding restraint supplies the second concrete modality in the paired sanction.","root":"و ث ق","source_ref":"89:26","source_word_indices":["2","3"]},{"branch_id":"B002","mapped_root_id":"root_000017","role":"Exhaustive negative anyone makes the focus modality incomparable across all agents.","root":"ء ح د","source_ref":"89:26","source_word_indices":["4"]},{"branch_id":"B005","mapped_root_id":"root_000994","role":"Painful punishment supplies the first sanction, against which binding distinguishes loss of agency from inflicted pain.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B002","mapped_root_id":"root_000017","role":"The identical exhaustive subject frame locks the two clauses into an explicit comparison pair.","root":"ء ح د","source_ref":"89:25","source_word_indices":["5"]}],"changed_reading":{"after":"Binding is the second arm of an unmatched dyad: punishment causes pain, while restraint cancels escape and agency.","before":"Binding is a free-standing image of unmatched force."},"confidence":"strong","mechanism":"The immediately preceding clause repeats the same negative subject frame and its own verb-cognate noun. This makes binding the second coordinated sanction: pain is paired with the removal of movement and agency.","model_id":"paired_unmatched_sanctions","reader_inference":"The packet supplies exact parallel form plus pain and restraint branches; I infer a two-part sanction of suffering and arrested agency. The live alternative is simple rhetorical intensification in which the two nouns overlap rather than divide functions.","status":"strengthened","structural_cues":["89:25 and 89:26 are syntactic twins: negation, imperfect verb, cognate possessed noun, and final أَحَدٌ."],"trigger_roots":["ع ذ ب","ء ح د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:paired_unmatched_sanctions","source_type":"hft","support_id":"sup_fbcbd48c4bdefe125457","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ","ayah_ref":"89:26"},{"arabic_uthmani":"يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ","ayah_ref":"89:27"},{"arabic_uthmani":"ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ","ayah_ref":"89:28"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000544/B001","root_000569/B003","root_000948/B001","root_001623/B001","root_001623/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001623","role":"Trust as settled reliance supplies the relational security that the post-focus tranquility makes audible.","root":"و ث ق","source_ref":"89:26","source_word_indices":["2","3"]},{"branch_id":"B003","mapped_root_id":"root_001623","role":"Literal restraint preserves the coercive pole, preventing the relational activation from erasing the focus's punitive force.","root":"و ث ق","source_ref":"89:26","source_word_indices":["2","3"]},{"branch_id":"B001","mapped_root_id":"root_000948","role":"Tranquility and stillness supply a willing mode of settledness adjacent to the imposed stillness of restraint.","root":"ط م ن","source_ref":"89:27","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000544","role":"Return to a prior place supplies directed movement completed by belonging rather than blocked by a bond.","root":"ر ج ع","source_ref":"89:28","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000569","role":"Mutual satisfaction supplies reciprocal acceptance, the relational condition under which trust can settle.","root":"ر ض و","source_ref":"89:28","source_word_indices":["4","5"]}],"changed_reading":{"after":"The focus becomes the dark pole of a twofold security: one subject is fixed by force, while another settles through trust, return, and mutual acceptance.","before":"The focus root offers only imposed immobility."},"confidence":"medium","mechanism":"Tranquil settling, return, and reciprocal satisfaction awaken the focus root's reliance branch. Two forms of being made secure coexist across the boundary: coerced fixation by restraint and willing settlement through trusted return.","model_id":"coerced_vs_tranquil_settlement","reader_inference":"The packet supplies stillness, return, mutual acceptance, trust, and restraint; I infer a contrast between willing and coerced settledness. The alternative is a sharp change of addressee with no semantic echo from وَثَاق into tranquility.","status":"strengthened","structural_cues":["The address to the tranquil self follows the unmatched binding without transition, then moves through return and reciprocal satisfaction."],"trigger_roots":["ط م ن","ر ج ع","ر ض و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:coerced_vs_tranquil_settlement","source_type":"hft","support_id":"sup_5e75750b5c5a308713dc","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ","ayah_ref":"89:26"},{"arabic_uthmani":"فَٱدْخُلِى فِى عِبَٰدِى","ayah_ref":"89:29"},{"arabic_uthmani":"وَٱدْخُلِى جَنَّتِى","ayah_ref":"89:30"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000266/B008","root_000464/B001","root_000973/B001","root_000973/B003","root_001623/B003","root_001623/B004"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001623","role":"The physical bond supplies coercive custody as the negative pole of enclosure.","root":"و ث ق","source_ref":"89:26","source_word_indices":["2","3"]},{"branch_id":"B004","mapped_root_id":"root_001623","role":"The assured compact supplies belonging by relation rather than by mere spatial confinement.","root":"و ث ق","source_ref":"89:26","source_word_indices":["2","3"]},{"branch_id":"B001","mapped_root_id":"root_000464","role":"Entry into an interior supplies voluntary admission as the spatial opposite of being held from escape.","root":"د خ ل","source_ref":"89:29","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000973","role":"Servitude as ownership supplies the custody relation shared, uneasily, by bondage and belonging.","root":"ع ب د","source_ref":"89:29","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000973","role":"Submissive obedience supplies accepted service, differentiating incorporated belonging from forced restraint.","root":"ع ب د","source_ref":"89:29","source_word_indices":["3"]},{"branch_id":"B008","mapped_root_id":"root_000266","role":"Protective covering supplies enclosure as shelter, a functional reversal of punitive confinement.","root":"ج ن ن","source_ref":"89:30","source_word_indices":["2"]}],"changed_reading":{"after":"The focus is one pole in a custody spectrum: forced possession confines, while accepted service and protected entry form a non-coercive belonging.","before":"All enclosure implied by binding is punitive confinement."},"confidence":"exploratory","mechanism":"Entry, owned service, obedient service, and protective enclosure recast binding along an axis of custody and belonging. The same possessive order can confine coercively or incorporate protectively, without making those outcomes equivalent.","model_id":"custody_vs_belonging_enclosure","reader_inference":"The packet supplies restraint, compact, entry, ownership, obedience, and protection; I infer a fork between coercive custody and accepted belonging. The live alternative is that the post-focus possessives merely identify reward and should not reactivate the semantic range of binding.","status":"new","structural_cues":["Possessive forms move from وَثَاقَهُ to رَبِّكِ, عِبَادِي, and جَنَّتِي, placing restraint and belonging within competing relations of possession."],"trigger_roots":["د خ ل","ع ب د","ج ن ن"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:custody_vs_belonging_enclosure","source_type":"hft","support_id":"sup_6869fd2160b498124919","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ","ayah_ref":"89:17"},{"arabic_uthmani":"وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ","ayah_ref":"89:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_001623/B001","root_001623/B003","root_001692/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001623","role":"Dependable reliance supplies the support relation whose withdrawal can produce social immobility.","root":"و ث ق","source_ref":"89:26","source_word_indices":["2","3"]},{"branch_id":"B003","mapped_root_id":"root_001623","role":"Physical restraint supplies the focus endpoint that makes unsupported dependence legible as binding.","root":"و ث ق","source_ref":"89:26","source_word_indices":["2","3"]},{"branch_id":"B001","mapped_root_id":"root_001692","role":"Severance of a child from a guardian supplies the concrete withdrawal of reliable support.","root":"ي ت م","source_ref":"89:17","source_word_indices":["5"]}],"changed_reading":{"after":"A person may also be bound by the removal of the dependable relation that would have enabled movement and agency.","before":"Binding requires an added cord or external fastener."},"confidence":"medium","containment":"This is surprising because it treats failed support as a binding mechanism rather than merely as a moral offense. It remains anchored through the focus root's reliance and restraint branches plus the orphan's severance from a guardian; downstream prose should retain it as a social-material analogy, not claim that وَثَاق directly means abandonment.","focus_anchor":"The two focus branches of dependable reliance and physical restraint permit a reversal in which loss of dependable support itself immobilizes.","outlier_id":"outlier_withdrawn_reliance_as_restraint"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_withdrawn_reliance_as_restraint","source_type":"hft","support_id":"sup_fefe8979b20d01fde650","trust":"legacy_unbound"}]}
</lane_packet_json>
