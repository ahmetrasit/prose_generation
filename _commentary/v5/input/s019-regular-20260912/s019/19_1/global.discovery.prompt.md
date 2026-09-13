# Commentary v5 scope discovery

You are the fresh **global** scope discoverer for **19:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s019-regular-20260912/s019/19_1/global.discovery.json` and modify nothing
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
  "ayah_ref": "19:1",
  "lane": "global",
  "coverage_complete": true,
  "candidate_decisions": [
    {
      "candidate_id": "exact packet candidate ID",
      "decision": "accept | narrow | represented | reject",
      "reason": "specific evidentiary reason",
      "finding_refs": ["global:stable-key"],
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
      "finding_ref": "global:stable-key",
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
`global:`. Accepted/narrowed candidates own dedicated findings. A represented
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
{"analysis_context":{"analysis_id":"s019-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"19:1","host_surah":19,"lane_context_refs":[],"ordered_context_refs":["19:2","19:3","19:4","19:5","19:6","19:7","19:8","19:9","19:10","19:11","19:12","19:13","19:14","19:15","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[],"candidate_inventory":[{"anchor_refs":[],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:1","branch_refs":[],"candidate_id":"cand_596cb339dee1df318e2a","commentary_obligation":"review","hft_ref":"hft_002b99b9d6612c5673de","kind":"reader_summary_claim","lane":"global","lane_assignment_basis":"unanchored reader synthesis is assigned to the widest lane","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"scope":"wider_record","source_local_id":"reader_hft_a:reader_summary:strongest_changes/0","source_type":"hft","support_ids":["sup_2a3b3e8a1b9ce33e4f27"],"title":"reader_summary:strongest_changes/0","trust":"legacy_unbound"},{"anchor_refs":[],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:1","branch_refs":[],"candidate_id":"cand_b6bffacaa9bc0f8d8158","commentary_obligation":"review","hft_ref":"hft_ef0b02e67f31716745a9","kind":"reader_summary_claim","lane":"global","lane_assignment_basis":"unanchored reader synthesis is assigned to the widest lane","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"scope":"wider_record","source_local_id":"reader_hft_a:reader_summary:strongest_changes/1","source_type":"hft","support_ids":["sup_87ce01ae665b38ea378c"],"title":"reader_summary:strongest_changes/1","trust":"legacy_unbound"},{"anchor_refs":[],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:1","branch_refs":[],"candidate_id":"cand_c161151fcdc544a839fb","commentary_obligation":"review","hft_ref":"hft_43275845c2d77ba2b44f","kind":"reader_summary_claim","lane":"global","lane_assignment_basis":"unanchored reader synthesis is assigned to the widest lane","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"scope":"wider_record","source_local_id":"reader_hft_a:reader_summary:strongest_changes/2","source_type":"hft","support_ids":["sup_6d6f3f8ebc0f7752143f"],"title":"reader_summary:strongest_changes/2","trust":"legacy_unbound"},{"anchor_refs":[],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:1","branch_refs":[],"candidate_id":"cand_76149fc7e6f4096f033d","commentary_obligation":"review","hft_ref":"hft_18d082cde420d71e8846","kind":"reader_summary_claim","lane":"global","lane_assignment_basis":"unanchored reader synthesis is assigned to the widest lane","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"scope":"wider_record","source_local_id":"reader_hft_a:reader_summary:what_was_special","source_type":"hft","support_ids":["sup_f97da0497d3f1c71d8b5"],"title":"reader_summary:what_was_special","trust":"legacy_unbound"},{"anchor_refs":[],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:1","branch_refs":[],"candidate_id":"cand_cb1d42bfb9c6d0622c51","commentary_obligation":"review","hft_ref":"hft_1432c77a46e6a2c99418","kind":"reader_summary_claim","lane":"global","lane_assignment_basis":"unanchored reader synthesis is assigned to the widest lane","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"scope":"wider_record","source_local_id":"reader_hft_a:reader_summary:remaining_uncertainties/0","source_type":"hft","support_ids":["sup_7ce388c7db06448f5eaf"],"title":"reader_summary:remaining_uncertainties/0","trust":"legacy_unbound"},{"anchor_refs":[],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:1","branch_refs":[],"candidate_id":"cand_ded04497a879df03e442","commentary_obligation":"review","hft_ref":"hft_eb3f7946abf67edaadb6","kind":"reader_summary_claim","lane":"global","lane_assignment_basis":"unanchored reader synthesis is assigned to the widest lane","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"scope":"wider_record","source_local_id":"reader_hft_a:reader_summary:remaining_uncertainties/1","source_type":"hft","support_ids":["sup_7f6b703c655faa30af8b"],"title":"reader_summary:remaining_uncertainties/1","trust":"legacy_unbound"},{"anchor_refs":[],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:1","branch_refs":[],"candidate_id":"cand_d586619c86cc4d478db2","commentary_obligation":"review","hft_ref":"hft_893452fb452b06837c03","kind":"reader_summary_claim","lane":"global","lane_assignment_basis":"unanchored reader synthesis is assigned to the widest lane","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"scope":"wider_record","source_local_id":"reader_hft_a:reader_summary:remaining_uncertainties/2","source_type":"hft","support_ids":["sup_63524ee456db735aa768"],"title":"reader_summary:remaining_uncertainties/2","trust":"legacy_unbound"},{"anchor_refs":[],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:1","branch_refs":[],"candidate_id":"cand_22b7e9c09337241b1eac","commentary_obligation":"review","hft_ref":"hft_234011d66f21a4190e42","kind":"hft_reader_extension","lane":"global","lane_assignment_basis":"one or more HFT anchors could not be resolved, so the record is conservatively visible in the widest lane","provenance_qualification":{"anchor_scope_complete":false,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["unrecognized HFT reader field"]},"scope":"wider_or_unresolved_record","source_local_id":"reader_hft_a:reader_extension:rootless_focus","source_type":"hft","support_ids":["sup_1bdfb6c6799a5dd33899"],"title":"reader_extension:rootless_focus","trust":"legacy_unbound"},{"anchor_refs":[],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:1","branch_refs":[],"candidate_id":"cand_4c31a3fc63b76739b6a0","commentary_obligation":"review","hft_ref":"hft_4f0fbc44f971b85f0cee","kind":"baseline_model","lane":"global","lane_assignment_basis":"unanchored reader synthesis is assigned to the widest lane","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"wider_record","source_local_id":"reader_hft_a:baseline_rootless_threshold","source_type":"hft","support_ids":["sup_e903b0c35f42506de778"],"title":"baseline_rootless_threshold","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_02cfdbf3eec6716b6d0d","connection_ref":"conn_5c58785b8f72b78e34c9","note":"Another isolated-letter surah opening; the closest formal parallel.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_61131519f0428140b5ad","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"strong","source_focus_ref":"20:1","source_note":"A surah-initial disjoint-letter opening, directly parallel in form and function.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"20:1","source_target_components":["20:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"20:1","target_evidence":{"arabic_uthmani":"طه","ayah_ref":"20:1"},"target_ref":"20:1"},{"connection_evidence_ref":"conn_ev_8c37f95292625f0110ea","connection_ref":"conn_a39003d893022b54c8f9","note":"A five-letter isolated opening, with Ayn shared but a different sequence.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_1522e3b250957e9598a2","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"medium","source_focus_ref":"42:2","source_note":"Its disjoint-letter opening shares ع, one constituent of عسق.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"42:2","source_target_components":["42:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"42:2","target_evidence":{"arabic_uthmani":"عٓسٓقٓ","ayah_ref":"42:2"},"target_ref":"42:2"},{"connection_evidence_ref":"conn_ev_648b69666f7e57f3558a","connection_ref":"conn_2ed893cf3ad0a863cc6a","note":"Ha-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_03474fcbd8fb040659f1","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"weak","source_focus_ref":"40:1","source_note":"Its letter sequence only illustrates the broader class of isolated Quranic openings.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"40:1","source_target_components":["40:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"40:1","target_evidence":{"arabic_uthmani":"حمٓ","ayah_ref":"40:1"},"target_ref":"40:1"},{"connection_evidence_ref":"conn_ev_e315bc1527d0374ff05c","connection_ref":"conn_4f1719ca17b0d407b274","note":"Ha-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_3f231d8d298087441b37","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"weak","source_focus_ref":"41:1","source_note":"A different disjoint-letter opening provides only a broad formal parallel.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"41:1","source_target_components":["41:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"41:1","target_evidence":{"arabic_uthmani":"حمٓ","ayah_ref":"41:1"},"target_ref":"41:1"},{"connection_evidence_ref":"conn_ev_eb784b015d7f282aed8e","connection_ref":"conn_9897f1e1eea43976316c","note":"Ha-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_8cfdfbc86474dae00c8d","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"weak","source_focus_ref":"42:1","source_note":"A different disjoint-letter opening provides only a broad formal parallel.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"42:1","source_target_components":["42:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"42:1","target_evidence":{"arabic_uthmani":"حمٓ","ayah_ref":"42:1"},"target_ref":"42:1"},{"connection_evidence_ref":"conn_ev_417e7b5cea27b8470a0d","connection_ref":"conn_0397e095956246df7ad7","note":"Ha-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_fa3042b44b597fa4ae0a","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"weak","source_focus_ref":"43:1","source_note":"A different disjoint-letter opening provides only a broad formal parallel.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"43:1","source_target_components":["43:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"43:1","target_evidence":{"arabic_uthmani":"حمٓ","ayah_ref":"43:1"},"target_ref":"43:1"},{"connection_evidence_ref":"conn_ev_504b129fb5472f716c33","connection_ref":"conn_590ab53fff697eca6fb2","note":"Ha-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_441b10829227d3a0c226","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"weak","source_focus_ref":"44:1","source_note":"A different disjoint-letter opening provides only a broad formal parallel.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"44:1","source_target_components":["44:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"44:1","target_evidence":{"arabic_uthmani":"حمٓ","ayah_ref":"44:1"},"target_ref":"44:1"},{"connection_evidence_ref":"conn_ev_11937d9906197010487e","connection_ref":"conn_a119a3f1932c35a83124","note":"An isolated-letter opening sharing the final Sad.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_72408a9335da80f26b81","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"weak","source_focus_ref":"7:1","source_note":"Disjoint-letter opening offers a secondary, non-identical formal parallel.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"7:1","source_target_components":["7:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"7:1","target_evidence":{"arabic_uthmani":"الٓمٓصٓ","ayah_ref":"7:1"},"target_ref":"7:1"},{"connection_evidence_ref":"conn_ev_e2befc49a1a739839ea2","connection_ref":"conn_4b4c1bbc09fd408c5244","note":"Ta-Sin-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_f10589d9c1eca798cd35","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"medium","source_focus_ref":"26:1","source_note":"Another surah-opening letter formula, structurally parallel but different.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"26:1","source_target_components":["26:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"26:1","target_evidence":{"arabic_uthmani":"طسٓمٓ","ayah_ref":"26:1"},"target_ref":"26:1"},{"connection_evidence_ref":"conn_ev_a592dd1f455d152e7672","connection_ref":"conn_bdbdbff30e560f7136fd","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_3cdd885ea58635819d18","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"44:27","source_note":"The disconnected opening letters do not clarify the focus.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"44:27","source_target_components":["44:27"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"44:27","target_evidence":{"arabic_uthmani":"وَنَعْمَةٍۢ كَانُوا۟ فِيهَا فَٰكِهِينَ","ayah_ref":"44:27"},"target_ref":"44:27"},{"connection_evidence_ref":"conn_ev_722d64e2c33c13f431c3","connection_ref":"conn_b81b7bc23f8a3bca7221","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_206005cba6753d3397a6","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"80:16","source_note":"Disconnected letters provide no available route to 80:16.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"80:16","source_target_components":["80:16"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"80:16","target_evidence":{"arabic_uthmani":"كِرَامٍۭ بَرَرَةٍۢ","ayah_ref":"80:16"},"target_ref":"80:16"},{"connection_evidence_ref":"conn_ev_7d873334ea91c3d27644","connection_ref":"conn_8e54f849217f2661a0f9","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"83:31","source_target_components":["83:31"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"83:31","target_evidence":{"arabic_uthmani":"وَإِذَا ٱنقَلَبُوٓا۟ إِلَىٰٓ أَهْلِهِمُ ٱنقَلَبُوا۟ فَكِهِينَ","ayah_ref":"83:31"},"target_ref":"83:31"},{"connection_evidence_ref":"conn_ev_e0fd956f65936ca49de7","connection_ref":"conn_95cffb916ab24e4cac2a","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"12:49","source_target_components":["12:49"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"12:49","target_evidence":{"arabic_uthmani":"ثُمَّ يَأْتِى مِنۢ بَعْدِ ذَٰلِكَ عَامٌۭ فِيهِ يُغَاثُ ٱلنَّاسُ وَفِيهِ يَعْصِرُونَ","ayah_ref":"12:49"},"target_ref":"12:49"},{"connection_evidence_ref":"conn_ev_ee41668b2ef5760ae2dd","connection_ref":"conn_d2cd650a87938d53586e","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"52:18","source_target_components":["52:18"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"52:18","target_evidence":{"arabic_uthmani":"فَٰكِهِينَ بِمَآ ءَاتَىٰهُمْ رَبُّهُمْ وَوَقَىٰهُمْ رَبُّهُمْ عَذَابَ ٱلْجَحِيمِ","ayah_ref":"52:18"},"target_ref":"52:18"},{"connection_evidence_ref":"conn_ev_4b99140e76829daef347","connection_ref":"conn_497762cdd346e3606687","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"72:23","source_target_components":["72:23"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"72:23","target_evidence":{"arabic_uthmani":"إِلَّا بَلَٰغًۭا مِّنَ ٱللَّهِ وَرِسَٰلَٰتِهِۦ ۚ وَمَن يَعْصِ ٱللَّهَ وَرَسُولَهُۥ فَإِنَّ لَهُۥ نَارَ جَهَنَّمَ خَٰلِدِينَ فِيهَآ أَبَدًا","ayah_ref":"72:23"},"target_ref":"72:23"},{"connection_evidence_ref":"conn_ev_38b03a8c6f65ef736df2","connection_ref":"conn_390ec94760b49fee00b1","note":"No direct connection to the isolated-letter opening.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"3:49","source_target_components":["3:49"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"3:49","target_evidence":{"arabic_uthmani":"وَرَسُولًا إِلَىٰ بَنِىٓ إِسْرَٰٓءِيلَ أَنِّى قَدْ جِئْتُكُم بِـَٔايَةٍۢ مِّن رَّبِّكُمْ ۖ أَنِّىٓ أَخْلُقُ لَكُم مِّنَ ٱلطِّينِ كَهَيْـَٔةِ ٱلطَّيْرِ فَأَنفُخُ فِيهِ فَيَكُونُ طَيْرًۢا بِإِذْنِ ٱللَّهِ ۖ وَأُبْرِئُ ٱلْأَكْمَهَ وَٱلْأَبْرَصَ وَأُحْىِ ٱلْمَوْتَىٰ بِإِذْنِ ٱللَّهِ ۖ وَأُنَبِّئُكُم بِمَا تَأْكُلُونَ وَمَا تَدَّخِرُونَ فِى بُيُوتِكُمْ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لَّكُمْ إِن كُنتُم مُّؤْمِنِينَ","ayah_ref":"3:49"},"target_ref":"3:49"},{"connection_evidence_ref":"conn_ev_4a92a700185f3f49f20e","connection_ref":"conn_c9cc52cce4dbeaca7f9b","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"22:5","source_target_components":["22:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"22:5","target_evidence":{"arabic_uthmani":"يَٰٓأَيُّهَا ٱلنَّاسُ إِن كُنتُمْ فِى رَيْبٍۢ مِّنَ ٱلْبَعْثِ فَإِنَّا خَلَقْنَٰكُم مِّن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ مِنْ عَلَقَةٍۢ ثُمَّ مِن مُّضْغَةٍۢ مُّخَلَّقَةٍۢ وَغَيْرِ مُخَلَّقَةٍۢ لِّنُبَيِّنَ لَكُمْ ۚ وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى ثُمَّ نُخْرِجُكُمْ طِفْلًۭا ثُمَّ لِتَبْلُغُوٓا۟ أَشُدَّكُمْ ۖ وَمِنكُم مَّن يُتَوَفَّىٰ وَمِنكُم مَّن يُرَدُّ إِلَىٰٓ أَرْذَلِ ٱلْعُمُرِ لِكَيْلَا يَعْلَمَ مِنۢ بَعْدِ عِلْمٍۢ شَيْـًۭٔا ۚ وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ وَأَنۢبَتَتْ مِن كُلِّ زَوْجٍۭ بَهِيجٍۢ","ayah_ref":"22:5"},"target_ref":"22:5"},{"connection_evidence_ref":"conn_ev_52c27c480467aa00fab6","connection_ref":"conn_ab114da725694be1fff7","note":"A non-identical isolated-letter surah opening.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_92c3dc85cc2f8bff394a","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"strong","source_focus_ref":"36:1","source_note":"Its distinctive multi-letter prefatory sequence is a close comparative counterpart to 36:1.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"36:1","source_target_components":["36:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"36:1","target_evidence":{"arabic_uthmani":"يسٓ","ayah_ref":"36:1"},"target_ref":"36:1"},{"connection_evidence_ref":"conn_ev_59f2d80f6c013365de14","connection_ref":"conn_e7394f0bb8321b78ae08","note":"Ha-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_3f61ea1548d731d36367","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"weak","source_focus_ref":"45:1","source_note":"فاتحة حروف متعددة مغايرة تدعم الجنس لا «حم».","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"45:1","source_target_components":["45:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"45:1","target_evidence":{"arabic_uthmani":"حمٓ","ayah_ref":"45:1"},"target_ref":"45:1"},{"connection_evidence_ref":"conn_ev_db0f747ca6e5b2245658","connection_ref":"conn_872079bb6937234d93d3","note":"Ha-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_2b47bade39774a97b627","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"medium","source_focus_ref":"46:1","source_note":"Another isolated-letter opening; preserves a distinct extended sequence without resolving the focus.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"46:1","source_target_components":["46:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"46:1","target_evidence":{"arabic_uthmani":"حمٓ","ayah_ref":"46:1"},"target_ref":"46:1"},{"connection_evidence_ref":"conn_ev_ffdf1fb8ce6718adf2d2","connection_ref":"conn_e412b6546928a039c452","note":"Ta-Sin-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_42ec24ed632b9b7caf86","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"medium","source_focus_ref":"28:1","source_note":"Another surah-opening letter formula, structurally parallel but different.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"28:1","source_target_components":["28:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"28:1","target_evidence":{"arabic_uthmani":"طسٓمٓ","ayah_ref":"28:1"},"target_ref":"28:1"},{"connection_evidence_ref":"conn_ev_aa845eed7c05dec1108d","connection_ref":"conn_965db12658124d2c6ab4","note":"Alif-Lam-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_e2b7546d982f44f43c42","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"weak","source_focus_ref":"29:1","source_note":"A distinct detached-letter opening supports the broader pattern only.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"29:1","source_target_components":["29:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"29:1","target_evidence":{"arabic_uthmani":"الٓمٓ","ayah_ref":"29:1"},"target_ref":"29:1"},{"connection_evidence_ref":"conn_ev_8104ba399099106f4cc2","connection_ref":"conn_b2d6d72214ebc427f1f2","note":"Alif-Lam-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_744947d5f1c69492302a","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"medium","source_focus_ref":"2:1","source_note":"A distinct extended detached-letter opening provides a parallel form.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"2:1","source_target_components":["2:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"2:1","target_evidence":{"arabic_uthmani":"الٓمٓ","ayah_ref":"2:1"},"target_ref":"2:1"},{"connection_evidence_ref":"conn_ev_227422e8b061adbe9268","connection_ref":"conn_b4dbe4d5c8384a62f276","note":"Alif-Lam-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":true,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_630db7a24e5f7114c42c","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"weak","source_focus_ref":"30:1","source_note":"A distinct detached-letter opening supports the broader pattern only.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"30:1","source_target_components":["30:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"30:1","target_evidence":{"arabic_uthmani":"الٓمٓ","ayah_ref":"30:1"},"target_ref":"30:1"},{"connection_evidence_ref":"conn_ev_62ce529857119f1b7444","connection_ref":"conn_64f9e13cd978c9646085","note":"Alif-Lam-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_243518a4a1f98d835fa5","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"weak","source_focus_ref":"31:1","source_note":"A distinct detached-letter opening supports the broader pattern only.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"31:1","source_target_components":["31:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"31:1","target_evidence":{"arabic_uthmani":"الٓمٓ","ayah_ref":"31:1"},"target_ref":"31:1"},{"connection_evidence_ref":"conn_ev_56bc14f5206089c91514","connection_ref":"conn_b646e6fd088040714f5e","note":"Alif-Lam-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_eb2944ecd91c9b991eaa","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"weak","source_focus_ref":"32:1","source_note":"A different disjoint-letter opening provides only a broad formal parallel.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"32:1","source_target_components":["32:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"32:1","target_evidence":{"arabic_uthmani":"الٓمٓ","ayah_ref":"32:1"},"target_ref":"32:1"},{"connection_evidence_ref":"conn_ev_08433b5ad8114f6ffdf8","connection_ref":"conn_dcc07b4793cbd7d8f525","note":"Alif-Lam-Mim is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_fdadc1b06ab4fe3b5d4f","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"cross_surah","source_direction_label":"weak","source_focus_ref":"3:1","source_note":"A different disconnected-letter opening; supports the broader opening pattern only.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"3:1","source_target_components":["3:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"3:1","target_evidence":{"arabic_uthmani":"الٓمٓ","ayah_ref":"3:1"},"target_ref":"3:1"},{"connection_evidence_ref":"conn_ev_4eab408954cf0f664e55","connection_ref":"conn_0a1086aec4f4bfa909d3","note":"No direct connection to the isolated-letter opening.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_f5eeaf22aef4be945d26","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"20:28","source_note":"The isolated opening letters add no usable relation here.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"20:28","source_target_components":["20:28"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"20:28","target_evidence":{"arabic_uthmani":"يَفْقَهُوا۟ قَوْلِى","ayah_ref":"20:28"},"target_ref":"20:28"},{"connection_evidence_ref":"conn_ev_cdbf520b02d87e5d4e18","connection_ref":"conn_d06d46eb95ad9b9d0c82","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_28124936a9af555b6689","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"90:13","source_note":"90:13 için ayırt edici katkı yok.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"90:13","source_target_components":["90:13"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"90:13","target_evidence":{"arabic_uthmani":"فَكُّ رَقَبَةٍ","ayah_ref":"90:13"},"target_ref":"90:13"},{"connection_evidence_ref":"conn_ev_9aa22a51c4692a6e5d20","connection_ref":"conn_c02df4c16fac66eddff3","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_136c3de296c643ebedc4","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"37:155","source_note":"The disjointed opening letters do not clarify the focus verse.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"37:155","source_target_components":["37:155"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"37:155","target_evidence":{"arabic_uthmani":"أَفَلَا تَذَكَّرُونَ","ayah_ref":"37:155"},"target_ref":"37:155"},{"connection_evidence_ref":"conn_ev_c67613ebf0b5db0b58cd","connection_ref":"conn_c5835e74459b1c283b62","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_a902c45520e31334b2fc","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"56:37","source_note":"Tail semantic retrieval supplies no retained connection to the focus readings.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"56:37","source_target_components":["56:37"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"56:37","target_evidence":{"arabic_uthmani":"عُرُبًا أَتْرَابًۭا","ayah_ref":"56:37"},"target_ref":"56:37"},{"connection_evidence_ref":"conn_ev_28f8eb72faa60cef4749","connection_ref":"conn_160210273aacb6093dc1","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_94db04cc1faa943adf5a","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"89:2","source_note":"Adds no clear evidence about the ten nights.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"89:2","source_target_components":["89:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:2","target_evidence":{"arabic_uthmani":"وَلَيَالٍ عَشْرٍۢ","ayah_ref":"89:2"},"target_ref":"89:2"},{"connection_evidence_ref":"conn_ev_573c2661733fb93d540f","connection_ref":"conn_341493c544d7e6bb8af8","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_865f0c6a531858c38117","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"92:21","source_note":"No interpretable route to the focus is supplied.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"92:21","source_target_components":["92:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"92:21","target_evidence":{"arabic_uthmani":"وَلَسَوْفَ يَرْضَىٰ","ayah_ref":"92:21"},"target_ref":"92:21"},{"connection_evidence_ref":"conn_ev_47f7bd6dd5b440f02838","connection_ref":"conn_676e268291ddae05e30d","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"81:21","source_target_components":["81:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"81:21","target_evidence":{"arabic_uthmani":"مُّطَاعٍۢ ثَمَّ أَمِينٍۢ","ayah_ref":"81:21"},"target_ref":"81:21"},{"connection_evidence_ref":"conn_ev_197d83bd562e79347ec5","connection_ref":"conn_22a234f673b22ea5baba","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"101:11","source_target_components":["101:11"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"101:11","target_evidence":{"arabic_uthmani":"نَارٌ حَامِيَةٌۢ","ayah_ref":"101:11"},"target_ref":"101:11"},{"connection_evidence_ref":"conn_ev_aaf64a8ab7ac93b672de","connection_ref":"conn_332a9f8d66a18f351aee","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_25d21b091a43de3b7a2a","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"101:1","source_note":"No usable connection beyond isolated letters.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"101:1","source_target_components":["101:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"101:1","target_evidence":{"arabic_uthmani":"ٱلْقَارِعَةُ","ayah_ref":"101:1"},"target_ref":"101:1"},{"connection_evidence_ref":"conn_ev_728208b7c17ba8afb2bb","connection_ref":"conn_973bb4afe7b4a75e0811","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"83:20","source_target_components":["83:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"83:20","target_evidence":{"arabic_uthmani":"كِتَٰبٌۭ مَّرْقُومٌۭ","ayah_ref":"83:20"},"target_ref":"83:20"},{"connection_evidence_ref":"conn_ev_b12fb35446f7b8fb34db","connection_ref":"conn_4b72d18971dc4bdaa5f4","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"83:9","source_target_components":["83:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"83:9","target_evidence":{"arabic_uthmani":"كِتَٰبٌۭ مَّرْقُومٌۭ","ayah_ref":"83:9"},"target_ref":"83:9"},{"connection_evidence_ref":"conn_ev_57c14e8430943e3e682c","connection_ref":"conn_3d27d9c59fb1af79ea86","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"69:1","source_target_components":["69:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"69:1","target_evidence":{"arabic_uthmani":"ٱلْحَآقَّةُ","ayah_ref":"69:1"},"target_ref":"69:1"},{"connection_evidence_ref":"conn_ev_585ca0e3ade86eb51442","connection_ref":"conn_f27f9fa14999907a6140","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"100:1","source_target_components":["100:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"100:1","target_evidence":{"arabic_uthmani":"وَٱلْعَٰدِيَٰتِ ضَبْحًۭا","ayah_ref":"100:1"},"target_ref":"100:1"},{"connection_evidence_ref":"conn_ev_a3213499ab10f28869a9","connection_ref":"conn_bbb60944a45e35aa8003","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"78:1","source_target_components":["78:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"78:1","target_evidence":{"arabic_uthmani":"عَمَّ يَتَسَآءَلُونَ","ayah_ref":"78:1"},"target_ref":"78:1"},{"connection_evidence_ref":"conn_ev_f471a4feac806fddc5ef","connection_ref":"conn_3802d2267cb5ef673057","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"37:130","source_target_components":["37:130"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"37:130","target_evidence":{"arabic_uthmani":"سَلَٰمٌ عَلَىٰٓ إِلْ يَاسِينَ","ayah_ref":"37:130"},"target_ref":"37:130"},{"connection_evidence_ref":"conn_ev_e9e240f50e194db9c057","connection_ref":"conn_59c528f49c28d4811e3f","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"74:21","source_target_components":["74:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"74:21","target_evidence":{"arabic_uthmani":"ثُمَّ نَظَرَ","ayah_ref":"74:21"},"target_ref":"74:21"},{"connection_evidence_ref":"conn_ev_09c705a1ef36174e0ccb","connection_ref":"conn_5a995601f3f6c582d1e7","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_96c9a68ef7653b0e3a17","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"55:64","source_note":"No discernible addition to the garden or vegetal-density reading.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"55:64","source_target_components":["55:64"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"55:64","target_evidence":{"arabic_uthmani":"مُدْهَآمَّتَانِ","ayah_ref":"55:64"},"target_ref":"55:64"},{"connection_evidence_ref":"conn_ev_604bc56278ce12ad37cc","connection_ref":"conn_0acfd3f6ba48dbb95b33","note":"No direct connection to the isolated-letter opening.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"20:30","source_target_components":["20:30"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"20:30","target_evidence":{"arabic_uthmani":"هَٰرُونَ أَخِى","ayah_ref":"20:30"},"target_ref":"20:30"},{"connection_evidence_ref":"conn_ev_435cc672265e8ca53cce","connection_ref":"conn_9869fc66e538dc75970c","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_c15a90c2f651c024fb74","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"56:3","source_note":"Does not add a clear interpretive route to the focus.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"56:3","source_target_components":["56:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"56:3","target_evidence":{"arabic_uthmani":"خَافِضَةٌۭ رَّافِعَةٌ","ayah_ref":"56:3"},"target_ref":"56:3"},{"connection_evidence_ref":"conn_ev_a1106b1c1bac574929de","connection_ref":"conn_5eff5aba6a84af1ec8e0","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"80:14","source_target_components":["80:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"80:14","target_evidence":{"arabic_uthmani":"مَّرْفُوعَةٍۢ مُّطَهَّرَةٍۭ","ayah_ref":"80:14"},"target_ref":"80:14"},{"connection_evidence_ref":"conn_ev_3b7f5081138271680b6e","connection_ref":"conn_9ef5960676ee2e2d7545","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"85:22","source_target_components":["85:22"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"85:22","target_evidence":{"arabic_uthmani":"فِى لَوْحٍۢ مَّحْفُوظٍۭ","ayah_ref":"85:22"},"target_ref":"85:22"},{"connection_evidence_ref":"conn_ev_8093ca9a046d967fcf0b","connection_ref":"conn_e194b91a9fd314541f2a","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"96:10","source_target_components":["96:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"96:10","target_evidence":{"arabic_uthmani":"عَبْدًا إِذَا صَلَّىٰٓ","ayah_ref":"96:10"},"target_ref":"96:10"},{"connection_evidence_ref":"conn_ev_b01d02e53cc5a3f26fd8","connection_ref":"conn_831c91e2157ea0b07398","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_f5989314f20e15734af3","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"80:28","source_note":"No material contribution to the food or cultivation sequence.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"80:28","source_target_components":["80:28"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"80:28","target_evidence":{"arabic_uthmani":"وَعِنَبًۭا وَقَضْبًۭا","ayah_ref":"80:28"},"target_ref":"80:28"},{"connection_evidence_ref":"conn_ev_30ea18ba24adb0ccc0c2","connection_ref":"conn_89eca6b259818868e17c","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"37:109","source_target_components":["37:109"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"37:109","target_evidence":{"arabic_uthmani":"سَلَٰمٌ عَلَىٰٓ إِبْرَٰهِيمَ","ayah_ref":"37:109"},"target_ref":"37:109"},{"connection_evidence_ref":"conn_ev_17183d2eb35637744f1c","connection_ref":"conn_6141434b042b85d925c1","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"74:51","source_target_components":["74:51"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"74:51","target_evidence":{"arabic_uthmani":"فَرَّتْ مِن قَسْوَرَةٍۭ","ayah_ref":"74:51"},"target_ref":"74:51"},{"connection_evidence_ref":"conn_ev_eb019c708dbbba1ddcc1","connection_ref":"conn_ed7fd8ec93ad8003ba55","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"85:18","source_target_components":["85:18"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"85:18","target_evidence":{"arabic_uthmani":"فِرْعَوْنَ وَثَمُودَ","ayah_ref":"85:18"},"target_ref":"85:18"},{"connection_evidence_ref":"conn_ev_7133443ba6825197e7ef","connection_ref":"conn_098cc86502bc11b24be8","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"69:23","source_target_components":["69:23"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"69:23","target_evidence":{"arabic_uthmani":"قُطُوفُهَا دَانِيَةٌۭ","ayah_ref":"69:23"},"target_ref":"69:23"},{"connection_evidence_ref":"conn_ev_ffca73b9c46c22dedc1b","connection_ref":"conn_0bb97c2a84e2c623e784","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"96:4","source_target_components":["96:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"96:4","target_evidence":{"arabic_uthmani":"ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ","ayah_ref":"96:4"},"target_ref":"96:4"},{"connection_evidence_ref":"conn_ev_83060124e8f899e1868a","connection_ref":"conn_489c0f75d0d0b088a02c","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_11855f3c5123ac1d0934","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"83:1","source_note":"No clear addition to the focus.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"83:1","source_target_components":["83:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"83:1","target_evidence":{"arabic_uthmani":"وَيْلٌۭ لِّلْمُطَفِّفِينَ","ayah_ref":"83:1"},"target_ref":"83:1"},{"connection_evidence_ref":"conn_ev_44304ac6b4ad445c103b","connection_ref":"conn_b2385de434bd90b324c6","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"74:15","source_target_components":["74:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"74:15","target_evidence":{"arabic_uthmani":"ثُمَّ يَطْمَعُ أَنْ أَزِيدَ","ayah_ref":"74:15"},"target_ref":"74:15"},{"connection_evidence_ref":"conn_ev_7bae87ec64ca16b03c62","connection_ref":"conn_727eb55e9ceb4ce1a674","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"69:2","source_target_components":["69:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"69:2","target_evidence":{"arabic_uthmani":"مَا ٱلْحَآقَّةُ","ayah_ref":"69:2"},"target_ref":"69:2"},{"connection_evidence_ref":"conn_ev_d83ad960482dac7960d7","connection_ref":"conn_60336f735e6c2cc3bde0","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"77:22","source_target_components":["77:22"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"77:22","target_evidence":{"arabic_uthmani":"إِلَىٰ قَدَرٍۢ مَّعْلُومٍۢ","ayah_ref":"77:22"},"target_ref":"77:22"},{"connection_evidence_ref":"conn_ev_429f9ac902dc6b9bfe02","connection_ref":"conn_128f90722dfa73f9678b","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"52:3","source_target_components":["52:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"52:3","target_evidence":{"arabic_uthmani":"فِى رَقٍّۢ مَّنشُورٍۢ","ayah_ref":"52:3"},"target_ref":"52:3"},{"connection_evidence_ref":"conn_ev_833d6b6438a6ebc89c55","connection_ref":"conn_ac7e447fcf0bdb01898e","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"4:14","source_target_components":["4:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"4:14","target_evidence":{"arabic_uthmani":"وَمَن يَعْصِ ٱللَّهَ وَرَسُولَهُۥ وَيَتَعَدَّ حُدُودَهُۥ يُدْخِلْهُ نَارًا خَٰلِدًۭا فِيهَا وَلَهُۥ عَذَابٌۭ مُّهِينٌۭ","ayah_ref":"4:14"},"target_ref":"4:14"},{"connection_evidence_ref":"conn_ev_d7add7c4273df5e213ef","connection_ref":"conn_3a7ee42ee709ebe916a9","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"51:10","source_target_components":["51:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"51:10","target_evidence":{"arabic_uthmani":"قُتِلَ ٱلْخَرَّٰصُونَ","ayah_ref":"51:10"},"target_ref":"51:10"},{"connection_evidence_ref":"conn_ev_5d51c82fbc78685d81ce","connection_ref":"conn_d993babd5415173eac04","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"56:34","source_target_components":["56:34"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"56:34","target_evidence":{"arabic_uthmani":"وَفُرُشٍۢ مَّرْفُوعَةٍ","ayah_ref":"56:34"},"target_ref":"56:34"},{"connection_evidence_ref":"conn_ev_ae41f0545d2c14a996a2","connection_ref":"conn_bc90d8d384160b232ea2","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"85:21","source_target_components":["85:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"85:21","target_evidence":{"arabic_uthmani":"بَلْ هُوَ قُرْءَانٌۭ مَّجِيدٌۭ","ayah_ref":"85:21"},"target_ref":"85:21"},{"connection_evidence_ref":"conn_ev_723380f1b70904efa976","connection_ref":"conn_a4dc00176b999ad04fa0","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"74:29","source_target_components":["74:29"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"74:29","target_evidence":{"arabic_uthmani":"لَوَّاحَةٌۭ لِّلْبَشَرِ","ayah_ref":"74:29"},"target_ref":"74:29"},{"connection_evidence_ref":"conn_ev_5cc95eaf2a6c29a195d7","connection_ref":"conn_c326ba534159cf568f70","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"55:48","source_target_components":["55:48"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"55:48","target_evidence":{"arabic_uthmani":"ذَوَاتَآ أَفْنَانٍۢ","ayah_ref":"55:48"},"target_ref":"55:48"},{"connection_evidence_ref":"conn_ev_3f621d0823ba5f13c5f9","connection_ref":"conn_904d231e740da2106df6","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"5:67","source_target_components":["5:67"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"5:67","target_evidence":{"arabic_uthmani":"۞ يَٰٓأَيُّهَا ٱلرَّسُولُ بَلِّغْ مَآ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ ۖ وَإِن لَّمْ تَفْعَلْ فَمَا بَلَّغْتَ رِسَالَتَهُۥ ۚ وَٱللَّهُ يَعْصِمُكَ مِنَ ٱلنَّاسِ ۗ إِنَّ ٱللَّهَ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ","ayah_ref":"5:67"},"target_ref":"5:67"},{"connection_evidence_ref":"conn_ev_af55444a5df24e62245f","connection_ref":"conn_3d794fa004ebefaec676","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"100:2","source_target_components":["100:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"100:2","target_evidence":{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"},"target_ref":"100:2"},{"connection_evidence_ref":"conn_ev_abca3b94da6bcfde09e8","connection_ref":"conn_22422329d3296ecc7e2a","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"78:32","source_target_components":["78:32"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"78:32","target_evidence":{"arabic_uthmani":"حَدَآئِقَ وَأَعْنَٰبًۭا","ayah_ref":"78:32"},"target_ref":"78:32"},{"connection_evidence_ref":"conn_ev_c4e16a71bbe3087c29ed","connection_ref":"conn_9fd60c7fedf3127b6a62","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"88:16","source_target_components":["88:16"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:16","target_evidence":{"arabic_uthmani":"وَزَرَابِىُّ مَبْثُوثَةٌ","ayah_ref":"88:16"},"target_ref":"88:16"},{"connection_evidence_ref":"conn_ev_7c39c473c9b9bb8ee67e","connection_ref":"conn_a008b620c1889596ae85","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"56:22","source_target_components":["56:22"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"56:22","target_evidence":{"arabic_uthmani":"وَحُورٌ عِينٌۭ","ayah_ref":"56:22"},"target_ref":"56:22"},{"connection_evidence_ref":"conn_ev_2e1c75624fb9fb0fe6e4","connection_ref":"conn_5fd691b17db3fd1ca508","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"11:43","source_target_components":["11:43"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"11:43","target_evidence":{"arabic_uthmani":"قَالَ سَـَٔاوِىٓ إِلَىٰ جَبَلٍۢ يَعْصِمُنِى مِنَ ٱلْمَآءِ ۚ قَالَ لَا عَاصِمَ ٱلْيَوْمَ مِنْ أَمْرِ ٱللَّهِ إِلَّا مَن رَّحِمَ ۚ وَحَالَ بَيْنَهُمَا ٱلْمَوْجُ فَكَانَ مِنَ ٱلْمُغْرَقِينَ","ayah_ref":"11:43"},"target_ref":"11:43"},{"connection_evidence_ref":"conn_ev_086fdd2cd285e9e90fe9","connection_ref":"conn_0eb07c94dca1beb13504","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_4f20ce64af04ea46cb4c","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"80:31","source_note":"No material addition to the focus or retained readings.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"80:31","source_target_components":["80:31"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"80:31","target_evidence":{"arabic_uthmani":"وَفَٰكِهَةًۭ وَأَبًّۭا","ayah_ref":"80:31"},"target_ref":"80:31"},{"connection_evidence_ref":"conn_ev_45dd070e1645c3742ecf","connection_ref":"conn_2ab63a381310faaae554","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"33:17","source_target_components":["33:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"33:17","target_evidence":{"arabic_uthmani":"قُلْ مَن ذَا ٱلَّذِى يَعْصِمُكُم مِّنَ ٱللَّهِ إِنْ أَرَادَ بِكُمْ سُوٓءًا أَوْ أَرَادَ بِكُمْ رَحْمَةًۭ ۚ وَلَا يَجِدُونَ لَهُم مِّن دُونِ ٱللَّهِ وَلِيًّۭا وَلَا نَصِيرًۭا","ayah_ref":"33:17"},"target_ref":"33:17"},{"connection_evidence_ref":"conn_ev_a6f4fade2952b988f256","connection_ref":"conn_6583c863c126631b91bb","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"33:36","source_target_components":["33:36"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"33:36","target_evidence":{"arabic_uthmani":"وَمَا كَانَ لِمُؤْمِنٍۢ وَلَا مُؤْمِنَةٍ إِذَا قَضَى ٱللَّهُ وَرَسُولُهُۥٓ أَمْرًا أَن يَكُونَ لَهُمُ ٱلْخِيَرَةُ مِنْ أَمْرِهِمْ ۗ وَمَن يَعْصِ ٱللَّهَ وَرَسُولَهُۥ فَقَدْ ضَلَّ ضَلَٰلًۭا مُّبِينًۭا","ayah_ref":"33:36"},"target_ref":"33:36"},{"connection_evidence_ref":"conn_ev_791943eabfbbe90e2b67","connection_ref":"conn_188c0e7e573624b9a902","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"70:16","source_target_components":["70:16"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"70:16","target_evidence":{"arabic_uthmani":"نَزَّاعَةًۭ لِّلشَّوَىٰ","ayah_ref":"70:16"},"target_ref":"70:16"},{"connection_evidence_ref":"conn_ev_cafaa6d09d52929c6d60","connection_ref":"conn_810a96193f8aefacaa74","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"66:6","source_target_components":["66:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"66:6","target_evidence":{"arabic_uthmani":"يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ عَلَيْهَا مَلَٰٓئِكَةٌ غِلَاظٌۭ شِدَادٌۭ لَّا يَعْصُونَ ٱللَّهَ مَآ أَمَرَهُمْ وَيَفْعَلُونَ مَا يُؤْمَرُونَ","ayah_ref":"66:6"},"target_ref":"66:6"},{"connection_evidence_ref":"conn_ev_1bc2ddad39d8c025d05b","connection_ref":"conn_5b58749e65487c83545e","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"53:57","source_target_components":["53:57"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"53:57","target_evidence":{"arabic_uthmani":"أَزِفَتِ ٱلْءَازِفَةُ","ayah_ref":"53:57"},"target_ref":"53:57"},{"connection_evidence_ref":"conn_ev_d75202e4661295a38a2a","connection_ref":"conn_f43352a81d93e724ec20","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"77:2","source_target_components":["77:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"77:2","target_evidence":{"arabic_uthmani":"فَٱلْعَٰصِفَٰتِ عَصْفًۭا","ayah_ref":"77:2"},"target_ref":"77:2"},{"connection_evidence_ref":"conn_ev_8fbc66490d623042b302","connection_ref":"conn_832428b01de5f634cc6f","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"100:3","source_target_components":["100:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"100:3","target_evidence":{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","ayah_ref":"100:3"},"target_ref":"100:3"},{"connection_evidence_ref":"conn_ev_1d3ec7939e89b2105252","connection_ref":"conn_c1cab7ca617b1ee1083d","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"100:10","source_target_components":["100:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"100:10","target_evidence":{"arabic_uthmani":"وَحُصِّلَ مَا فِى ٱلصُّدُورِ","ayah_ref":"100:10"},"target_ref":"100:10"},{"connection_evidence_ref":"conn_ev_0920941835a882c14d06","connection_ref":"conn_1f86dd84d69df0513b99","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"60:12","source_target_components":["60:12"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"60:12","target_evidence":{"arabic_uthmani":"يَٰٓأَيُّهَا ٱلنَّبِىُّ إِذَا جَآءَكَ ٱلْمُؤْمِنَٰتُ يُبَايِعْنَكَ عَلَىٰٓ أَن لَّا يُشْرِكْنَ بِٱللَّهِ شَيْـًۭٔا وَلَا يَسْرِقْنَ وَلَا يَزْنِينَ وَلَا يَقْتُلْنَ أَوْلَٰدَهُنَّ وَلَا يَأْتِينَ بِبُهْتَٰنٍۢ يَفْتَرِينَهُۥ بَيْنَ أَيْدِيهِنَّ وَأَرْجُلِهِنَّ وَلَا يَعْصِينَكَ فِى مَعْرُوفٍۢ ۙ فَبَايِعْهُنَّ وَٱسْتَغْفِرْ لَهُنَّ ٱللَّهَ ۖ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ","ayah_ref":"60:12"},"target_ref":"60:12"},{"connection_evidence_ref":"conn_ev_16ef107a74bdecf1b024","connection_ref":"conn_d3069dbb6ccaa96947ea","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3","target_evidence":{"arabic_uthmani":"عَامِلَةٌۭ نَّاصِبَةٌۭ","ayah_ref":"88:3"},"target_ref":"88:3"},{"connection_evidence_ref":"conn_ev_383e9a101637299f5f29","connection_ref":"conn_3e62b271c260273eb622","note":"No direct connection to the isolated-letter opening.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"5:110","source_target_components":["5:110"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"5:110","target_evidence":{"arabic_uthmani":"إِذْ قَالَ ٱللَّهُ يَٰعِيسَى ٱبْنَ مَرْيَمَ ٱذْكُرْ نِعْمَتِى عَلَيْكَ وَعَلَىٰ وَٰلِدَتِكَ إِذْ أَيَّدتُّكَ بِرُوحِ ٱلْقُدُسِ تُكَلِّمُ ٱلنَّاسَ فِى ٱلْمَهْدِ وَكَهْلًۭا ۖ وَإِذْ عَلَّمْتُكَ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَٱلتَّوْرَىٰةَ وَٱلْإِنجِيلَ ۖ وَإِذْ تَخْلُقُ مِنَ ٱلطِّينِ كَهَيْـَٔةِ ٱلطَّيْرِ بِإِذْنِى فَتَنفُخُ فِيهَا فَتَكُونُ طَيْرًۢا بِإِذْنِى ۖ وَتُبْرِئُ ٱلْأَكْمَهَ وَٱلْأَبْرَصَ بِإِذْنِى ۖ وَإِذْ تُخْرِجُ ٱلْمَوْتَىٰ بِإِذْنِى ۖ وَإِذْ كَفَفْتُ بَنِىٓ إِسْرَٰٓءِيلَ عَنكَ إِذْ جِئْتَهُم بِٱلْبَيِّنَٰتِ فَقَالَ ٱلَّذِينَ كَفَرُوا۟ مِنْهُمْ إِنْ هَٰذَآ إِلَّا سِحْرٌۭ مُّبِينٌۭ","ayah_ref":"5:110"},"target_ref":"5:110"},{"connection_evidence_ref":"conn_ev_85e1d2e93ebb31246c96","connection_ref":"conn_6277cf242a59d876256f","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"100:11","source_target_components":["100:11"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"100:11","target_evidence":{"arabic_uthmani":"إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ","ayah_ref":"100:11"},"target_ref":"100:11"},{"connection_evidence_ref":"conn_ev_a72231738b3b3bec8642","connection_ref":"conn_7344f581281deb852da7","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"100:5","source_target_components":["100:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"100:5","target_evidence":{"arabic_uthmani":"فَوَسَطْنَ بِهِۦ جَمْعًا","ayah_ref":"100:5"},"target_ref":"100:5"},{"connection_evidence_ref":"conn_ev_807101887e2e27c20a57","connection_ref":"conn_3d1594de5278f4953a66","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"100:4","source_target_components":["100:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"100:4","target_evidence":{"arabic_uthmani":"فَأَثَرْنَ بِهِۦ نَقْعًۭا","ayah_ref":"100:4"},"target_ref":"100:4"},{"connection_evidence_ref":"conn_ev_27c44d7d21e3e825e79a","connection_ref":"conn_bc1a0c9a246098ed1d2c","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"100:7","source_target_components":["100:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"100:7","target_evidence":{"arabic_uthmani":"وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ","ayah_ref":"100:7"},"target_ref":"100:7"},{"connection_evidence_ref":"conn_ev_5a0ba437215ed2a5207a","connection_ref":"conn_72d44b61d1cc30391c43","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"100:8","source_target_components":["100:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"100:8","target_evidence":{"arabic_uthmani":"وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ","ayah_ref":"100:8"},"target_ref":"100:8"},{"connection_evidence_ref":"conn_ev_ef615a64c3b9cdacaa61","connection_ref":"conn_df63691269a6bba00fa6","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"100:6","source_target_components":["100:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"100:6","target_evidence":{"arabic_uthmani":"إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌۭ","ayah_ref":"100:6"},"target_ref":"100:6"},{"connection_evidence_ref":"conn_ev_01a2e8549353eacc5dc3","connection_ref":"conn_1baf48a71308537d1983","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"77:4","source_target_components":["77:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"77:4","target_evidence":{"arabic_uthmani":"فَٱلْفَٰرِقَٰتِ فَرْقًۭا","ayah_ref":"77:4"},"target_ref":"77:4"},{"connection_evidence_ref":"conn_ev_9d3e630fe9908701fccb","connection_ref":"conn_60a9650edb802496a7d2","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"17:64","source_target_components":["17:64"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"17:64","target_evidence":{"arabic_uthmani":"وَٱسْتَفْزِزْ مَنِ ٱسْتَطَعْتَ مِنْهُم بِصَوْتِكَ وَأَجْلِبْ عَلَيْهِم بِخَيْلِكَ وَرَجِلِكَ وَشَارِكْهُمْ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ وَعِدْهُمْ ۚ وَمَا يَعِدُهُمُ ٱلشَّيْطَٰنُ إِلَّا غُرُورًا","ayah_ref":"17:64"},"target_ref":"17:64"},{"connection_evidence_ref":"conn_ev_73231fae6d2ef2169a74","connection_ref":"conn_cafd4f4962af6d2cda95","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"24:52","source_target_components":["24:52"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"24:52","target_evidence":{"arabic_uthmani":"وَمَن يُطِعِ ٱللَّهَ وَرَسُولَهُۥ وَيَخْشَ ٱللَّهَ وَيَتَّقْهِ فَأُو۟لَٰٓئِكَ هُمُ ٱلْفَآئِزُونَ","ayah_ref":"24:52"},"target_ref":"24:52"},{"connection_evidence_ref":"conn_ev_e403a9939f90ce09f7f2","connection_ref":"conn_4a91fb559f19b1373fee","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"26:7","source_target_components":["26:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"26:7","target_evidence":{"arabic_uthmani":"أَوَلَمْ يَرَوْا۟ إِلَى ٱلْأَرْضِ كَمْ أَنۢبَتْنَا فِيهَا مِن كُلِّ زَوْجٍۢ كَرِيمٍ","ayah_ref":"26:7"},"target_ref":"26:7"},{"connection_evidence_ref":"conn_ev_071bf62aefce5741476b","connection_ref":"conn_b5e542c4bf439ea00a42","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"46:26","source_target_components":["46:26"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"46:26","target_evidence":{"arabic_uthmani":"وَلَقَدْ مَكَّنَّٰهُمْ فِيمَآ إِن مَّكَّنَّٰكُمْ فِيهِ وَجَعَلْنَا لَهُمْ سَمْعًۭا وَأَبْصَٰرًۭا وَأَفْـِٔدَةًۭ فَمَآ أَغْنَىٰ عَنْهُمْ سَمْعُهُمْ وَلَآ أَبْصَٰرُهُمْ وَلَآ أَفْـِٔدَتُهُم مِّن شَىْءٍ إِذْ كَانُوا۟ يَجْحَدُونَ بِـَٔايَٰتِ ٱللَّهِ وَحَاقَ بِهِم مَّا كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ","ayah_ref":"46:26"},"target_ref":"46:26"},{"connection_evidence_ref":"conn_ev_fc49a3eadf1a1fdf15bd","connection_ref":"conn_9ced79fd88cb9ee46827","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"2:187","source_target_components":["2:187"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"2:187","target_evidence":{"arabic_uthmani":"أُحِلَّ لَكُمْ لَيْلَةَ ٱلصِّيَامِ ٱلرَّفَثُ إِلَىٰ نِسَآئِكُمْ ۚ هُنَّ لِبَاسٌۭ لَّكُمْ وَأَنتُمْ لِبَاسٌۭ لَّهُنَّ ۗ عَلِمَ ٱللَّهُ أَنَّكُمْ كُنتُمْ تَخْتَانُونَ أَنفُسَكُمْ فَتَابَ عَلَيْكُمْ وَعَفَا عَنكُمْ ۖ فَٱلْـَٰٔنَ بَٰشِرُوهُنَّ وَٱبْتَغُوا۟ مَا كَتَبَ ٱللَّهُ لَكُمْ ۚ وَكُلُوا۟ وَٱشْرَبُوا۟ حَتَّىٰ يَتَبَيَّنَ لَكُمُ ٱلْخَيْطُ ٱلْأَبْيَضُ مِنَ ٱلْخَيْطِ ٱلْأَسْوَدِ مِنَ ٱلْفَجْرِ ۖ ثُمَّ أَتِمُّوا۟ ٱلصِّيَامَ إِلَى ٱلَّيْلِ ۚ وَلَا تُبَٰشِرُوهُنَّ وَأَنتُمْ عَٰكِفُونَ فِى ٱلْمَسَٰجِدِ ۗ تِلْكَ حُدُودُ ٱللَّهِ فَلَا تَقْرَبُوهَا ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ ءَايَٰتِهِۦ لِلنَّاسِ لَعَلَّهُمْ يَتَّقُونَ","ayah_ref":"2:187"},"target_ref":"2:187"},{"connection_evidence_ref":"conn_ev_d12ab1a4fabe033f68cf","connection_ref":"conn_17b2c9bfe0951737ff8c","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"33:53","source_target_components":["33:53"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"33:53","target_evidence":{"arabic_uthmani":"يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَدْخُلُوا۟ بُيُوتَ ٱلنَّبِىِّ إِلَّآ أَن يُؤْذَنَ لَكُمْ إِلَىٰ طَعَامٍ غَيْرَ نَٰظِرِينَ إِنَىٰهُ وَلَٰكِنْ إِذَا دُعِيتُمْ فَٱدْخُلُوا۟ فَإِذَا طَعِمْتُمْ فَٱنتَشِرُوا۟ وَلَا مُسْتَـْٔنِسِينَ لِحَدِيثٍ ۚ إِنَّ ذَٰلِكُمْ كَانَ يُؤْذِى ٱلنَّبِىَّ فَيَسْتَحْىِۦ مِنكُمْ ۖ وَٱللَّهُ لَا يَسْتَحْىِۦ مِنَ ٱلْحَقِّ ۚ وَإِذَا سَأَلْتُمُوهُنَّ مَتَٰعًۭا فَسْـَٔلُوهُنَّ مِن وَرَآءِ حِجَابٍۢ ۚ ذَٰلِكُمْ أَطْهَرُ لِقُلُوبِكُمْ وَقُلُوبِهِنَّ ۚ وَمَا كَانَ لَكُمْ أَن تُؤْذُوا۟ رَسُولَ ٱللَّهِ وَلَآ أَن تَنكِحُوٓا۟ أَزْوَٰجَهُۥ مِنۢ بَعْدِهِۦٓ أَبَدًا ۚ إِنَّ ذَٰلِكُمْ كَانَ عِندَ ٱللَّهِ عَظِيمًا","ayah_ref":"33:53"},"target_ref":"33:53"},{"connection_evidence_ref":"conn_ev_e14821048c32252b24a1","connection_ref":"conn_85b1ed18a96467f29fd5","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"5:41","source_target_components":["5:41"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"5:41","target_evidence":{"arabic_uthmani":"۞ يَٰٓأَيُّهَا ٱلرَّسُولُ لَا يَحْزُنكَ ٱلَّذِينَ يُسَٰرِعُونَ فِى ٱلْكُفْرِ مِنَ ٱلَّذِينَ قَالُوٓا۟ ءَامَنَّا بِأَفْوَٰهِهِمْ وَلَمْ تُؤْمِن قُلُوبُهُمْ ۛ وَمِنَ ٱلَّذِينَ هَادُوا۟ ۛ سَمَّٰعُونَ لِلْكَذِبِ سَمَّٰعُونَ لِقَوْمٍ ءَاخَرِينَ لَمْ يَأْتُوكَ ۖ يُحَرِّفُونَ ٱلْكَلِمَ مِنۢ بَعْدِ مَوَاضِعِهِۦ ۖ يَقُولُونَ إِنْ أُوتِيتُمْ هَٰذَا فَخُذُوهُ وَإِن لَّمْ تُؤْتَوْهُ فَٱحْذَرُوا۟ ۚ وَمَن يُرِدِ ٱللَّهُ فِتْنَتَهُۥ فَلَن تَمْلِكَ لَهُۥ مِنَ ٱللَّهِ شَيْـًٔا ۚ أُو۟لَٰٓئِكَ ٱلَّذِينَ لَمْ يُرِدِ ٱللَّهُ أَن يُطَهِّرَ قُلُوبَهُمْ ۚ لَهُمْ فِى ٱلدُّنْيَا خِزْىٌۭ ۖ وَلَهُمْ فِى ٱلْءَاخِرَةِ عَذَابٌ عَظِيمٌۭ","ayah_ref":"5:41"},"target_ref":"5:41"},{"connection_evidence_ref":"conn_ev_78205a601946a7f98f95","connection_ref":"conn_02fd9c66d47b33fb9f39","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"4:91","source_target_components":["4:91"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"4:91","target_evidence":{"arabic_uthmani":"سَتَجِدُونَ ءَاخَرِينَ يُرِيدُونَ أَن يَأْمَنُوكُمْ وَيَأْمَنُوا۟ قَوْمَهُمْ كُلَّ مَا رُدُّوٓا۟ إِلَى ٱلْفِتْنَةِ أُرْكِسُوا۟ فِيهَا ۚ فَإِن لَّمْ يَعْتَزِلُوكُمْ وَيُلْقُوٓا۟ إِلَيْكُمُ ٱلسَّلَمَ وَيَكُفُّوٓا۟ أَيْدِيَهُمْ فَخُذُوهُمْ وَٱقْتُلُوهُمْ حَيْثُ ثَقِفْتُمُوهُمْ ۚ وَأُو۟لَٰٓئِكُمْ جَعَلْنَا لَكُمْ عَلَيْهِمْ سُلْطَٰنًۭا مُّبِينًۭا","ayah_ref":"4:91"},"target_ref":"4:91"},{"connection_evidence_ref":"conn_ev_aa367d7faecf2b4ffb44","connection_ref":"conn_4fcd4c2ad30f02a3c8c0","note":"No clear formal or supplied-route connection to 19:1.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"ranked_review","source_target_component_ref":"73:20","source_target_components":["73:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"73:20","target_evidence":{"arabic_uthmani":"۞ إِنَّ رَبَّكَ يَعْلَمُ أَنَّكَ تَقُومُ أَدْنَىٰ مِن ثُلُثَىِ ٱلَّيْلِ وَنِصْفَهُۥ وَثُلُثَهُۥ وَطَآئِفَةٌۭ مِّنَ ٱلَّذِينَ مَعَكَ ۚ وَٱللَّهُ يُقَدِّرُ ٱلَّيْلَ وَٱلنَّهَارَ ۚ عَلِمَ أَن لَّن تُحْصُوهُ فَتَابَ عَلَيْكُمْ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنَ ٱلْقُرْءَانِ ۚ عَلِمَ أَن سَيَكُونُ مِنكُم مَّرْضَىٰ ۙ وَءَاخَرُونَ يَضْرِبُونَ فِى ٱلْأَرْضِ يَبْتَغُونَ مِن فَضْلِ ٱللَّهِ ۙ وَءَاخَرُونَ يُقَٰتِلُونَ فِى سَبِيلِ ٱللَّهِ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنْهُ ۚ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَأَقْرِضُوا۟ ٱللَّهَ قَرْضًا حَسَنًۭا ۚ وَمَا تُقَدِّمُوا۟ لِأَنفُسِكُم مِّنْ خَيْرٍۢ تَجِدُوهُ عِندَ ٱللَّهِ هُوَ خَيْرًۭا وَأَعْظَمَ أَجْرًۭا ۚ وَٱسْتَغْفِرُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۢ","ayah_ref":"73:20"},"target_ref":"73:20"},{"connection_evidence_ref":"conn_ev_770fdc7271a84f5c91c9","connection_ref":"conn_9f813cac774a5d9869a2","note":"Alif-Lam-Ra is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"10:1","source_target_components":["10:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"10:1","target_evidence":{"arabic_uthmani":"الٓر ۚ تِلْكَ ءَايَٰتُ ٱلْكِتَٰبِ ٱلْحَكِيمِ","ayah_ref":"10:1"},"target_ref":"10:1"},{"connection_evidence_ref":"conn_ev_dfc65e20236f28686e96","connection_ref":"conn_53c5572ad6736dca6b98","note":"Alif-Lam-Ra is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"11:1","source_target_components":["11:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"11:1","target_evidence":{"arabic_uthmani":"الٓر ۚ كِتَٰبٌ أُحْكِمَتْ ءَايَٰتُهُۥ ثُمَّ فُصِّلَتْ مِن لَّدُنْ حَكِيمٍ خَبِيرٍ","ayah_ref":"11:1"},"target_ref":"11:1"},{"connection_evidence_ref":"conn_ev_ffb4bf32c91a10279fbc","connection_ref":"conn_131e3107c1934355e0fe","note":"Alif-Lam-Ra is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"12:1","source_target_components":["12:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"12:1","target_evidence":{"arabic_uthmani":"الٓر ۚ تِلْكَ ءَايَٰتُ ٱلْكِتَٰبِ ٱلْمُبِينِ","ayah_ref":"12:1"},"target_ref":"12:1"},{"connection_evidence_ref":"conn_ev_b7ac86d7707738be7318","connection_ref":"conn_4c8a27a3f49b4b288409","note":"Alif-Lam-Mim-Ra is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"13:1","source_target_components":["13:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"13:1","target_evidence":{"arabic_uthmani":"الٓمٓر ۚ تِلْكَ ءَايَٰتُ ٱلْكِتَٰبِ ۗ وَٱلَّذِىٓ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ ٱلْحَقُّ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يُؤْمِنُونَ","ayah_ref":"13:1"},"target_ref":"13:1"},{"connection_evidence_ref":"conn_ev_d725140151f04b248fe4","connection_ref":"conn_6929ece0dba1a7fbfa48","note":"Alif-Lam-Ra is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"14:1","source_target_components":["14:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"14:1","target_evidence":{"arabic_uthmani":"الٓر ۚ كِتَٰبٌ أَنزَلْنَٰهُ إِلَيْكَ لِتُخْرِجَ ٱلنَّاسَ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ بِإِذْنِ رَبِّهِمْ إِلَىٰ صِرَٰطِ ٱلْعَزِيزِ ٱلْحَمِيدِ","ayah_ref":"14:1"},"target_ref":"14:1"},{"connection_evidence_ref":"conn_ev_09bbfa41389fc47a6e21","connection_ref":"conn_9a858567490f5814d21f","note":"Alif-Lam-Ra is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"15:1","source_target_components":["15:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"15:1","target_evidence":{"arabic_uthmani":"الٓر ۚ تِلْكَ ءَايَٰتُ ٱلْكِتَٰبِ وَقُرْءَانٍۢ مُّبِينٍۢ","ayah_ref":"15:1"},"target_ref":"15:1"},{"connection_evidence_ref":"conn_ev_5d3bf3f48a4fb39f9790","connection_ref":"conn_d80af8778a09d0f3ffec","note":"Ta-Sin is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"27:1","source_target_components":["27:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"27:1","target_evidence":{"arabic_uthmani":"طسٓ ۚ تِلْكَ ءَايَٰتُ ٱلْقُرْءَانِ وَكِتَابٍۢ مُّبِينٍ","ayah_ref":"27:1"},"target_ref":"27:1"},{"connection_evidence_ref":"conn_ev_7df61e0f27d2b4b14c4b","connection_ref":"conn_4848cf5482b54ca630f2","note":"The isolated Sad opening shares one letter with 19:1.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"38:1","source_target_components":["38:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"38:1","target_evidence":{"arabic_uthmani":"صٓ ۚ وَٱلْقُرْءَانِ ذِى ٱلذِّكْرِ","ayah_ref":"38:1"},"target_ref":"38:1"},{"connection_evidence_ref":"conn_ev_18f339aea18b0cd99116","connection_ref":"conn_6b6fd82a3bfbb8408d70","note":"Qaf is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"50:1","source_target_components":["50:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"50:1","target_evidence":{"arabic_uthmani":"قٓ ۚ وَٱلْقُرْءَانِ ٱلْمَجِيدِ","ayah_ref":"50:1"},"target_ref":"50:1"},{"connection_evidence_ref":"conn_ev_748512a71c2606a36ef1","connection_ref":"conn_de5dd1c3e249b548e04f","note":"Nun is a non-identical isolated-letter opening.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"inter_surah","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"68:1","source_target_components":["68:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"68:1","target_evidence":{"arabic_uthmani":"نٓ ۚ وَٱلْقَلَمِ وَمَا يَسْطُرُونَ","ayah_ref":"68:1"},"target_ref":"68:1"},{"connection_ref":"conn_dbc3e9aca5c2fdb0f139","note":null,"origin":"derived_reciprocal_counterevidence","prior_label":null,"qualification":{"boundary":"The target's source-direction review recorded only `no value` or `reject` links back to the focus ayah. Keep that negative evidence visible as possible asymmetry or a failed edge, but do not let it veto a focus-direction reading without fresh assessment from the supplied exact target Arabic.","derived_reciprocal_counterevidence":true,"derived_reciprocal_seed":false,"has_missing_ayah_suggestion_source_row":false,"has_ranked_review_source_row":true,"has_reciprocal_counterevidence":true,"has_reciprocal_nomination":false,"receiving_direction_requires_fresh_assessment":true,"source_direction_labels_are_not_focus_decisions":true,"source_row_roles_are_provenance_not_decisions":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_edb8319778b31cc37adb","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"44:36","source_note":"The isolated letters provide no usable link to the focus.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah_reciprocal_evidence","target_evidence":{"arabic_uthmani":"فَأْتُوا۟ بِـَٔابَآئِنَآ إِن كُنتُمْ صَٰدِقِينَ","ayah_ref":"44:36"},"target_ref":"44:36"},{"connection_ref":"conn_c36aee1b6881de341cb4","note":null,"origin":"derived_reciprocal_counterevidence","prior_label":null,"qualification":{"boundary":"The target's source-direction review recorded only `no value` or `reject` links back to the focus ayah. Keep that negative evidence visible as possible asymmetry or a failed edge, but do not let it veto a focus-direction reading without fresh assessment from the supplied exact target Arabic.","derived_reciprocal_counterevidence":true,"derived_reciprocal_seed":false,"has_missing_ayah_suggestion_source_row":false,"has_ranked_review_source_row":true,"has_reciprocal_counterevidence":true,"has_reciprocal_nomination":false,"receiving_direction_requires_fresh_assessment":true,"source_direction_labels_are_not_focus_decisions":true,"source_row_roles_are_provenance_not_decisions":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_4837bf0ab5630a482ce7","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"cross_surah","source_direction_label":"no value","source_focus_ref":"106:1","source_note":"No stated lexical or auxiliary route to 106:1.","source_row_role":"ranked_review","source_target_component_ref":"19:1","source_target_components":["19:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:1"}],"relation_scope":"inter_surah_reciprocal_evidence","target_evidence":{"arabic_uthmani":"لِإِيلَٰفِ قُرَيْشٍ","ayah_ref":"106:1"},"target_ref":"106:1"}],"focus":{"arabic_uthmani":"كٓهيعٓصٓ","qac_morphemes":[{"lemma_ar":"","morph_features":"STEM|POS:INL","morpheme_role":"STEM","pos":"INL","qac_ref":"19:1:1:1","qac_word_ref":"19:1:1","root_ar":"","surface_ar":"كٓهيعٓصٓ"}],"word_analysis_qac_refs":[["19:1:1:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["19:1:1"]},"focus_surface_evidence":{"arabic_uthmani":"كٓهيعٓصٓ","qac_morphemes":[{"lemma_ar":"","morph_features":"STEM|POS:INL","morpheme_role":"STEM","pos":"INL","qac_ref":"19:1:1:1","qac_word_ref":"19:1:1","root_ar":"","surface_ar":"كٓهيعٓصٓ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["19:1:1:1"]],"word_analysis_refs":["19:1:1"],"word_rows":[{"analysis_record_ref":"19:1:1","analytic_gloss_range_en":"five recited letter-names fused into one rootless muqattaʿāt opener; its force comes through predicate-like placement, recitation, sound, distributional uniqueness, and a forward bridge into the dhikr frame rather than through an ordinary lexical gloss","analytic_root_gloss_range_en":null,"qac_refs":["19:1:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"كٓهيعٓصٓ","transliteration":"kāf hāʾ yāʾ ʿayn ṣād"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":1,"words_total":1,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":0,"missing_anchor_refs":[],"supplied_unique_anchor_count":0},"assigned_record_count":9,"assigned_records":[{"anchor_refs":[],"branch_refs":[],"candidate_id":"cand_596cb339dee1df318e2a","evidence_scope":"wider_record","hft_ref":"hft_002b99b9d6612c5673de","item_id":"reader_summary:strongest_changes/0","kind":"reader_summary_claim","lane_basis":"unanchored reader synthesis is assigned to the widest lane","owning_lane":"global","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:reader_summary:strongest_changes/0","support_id":"sup_2a3b3e8a1b9ce33e4f27"},{"anchor_refs":[],"branch_refs":[],"candidate_id":"cand_b6bffacaa9bc0f8d8158","evidence_scope":"wider_record","hft_ref":"hft_ef0b02e67f31716745a9","item_id":"reader_summary:strongest_changes/1","kind":"reader_summary_claim","lane_basis":"unanchored reader synthesis is assigned to the widest lane","owning_lane":"global","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:reader_summary:strongest_changes/1","support_id":"sup_87ce01ae665b38ea378c"},{"anchor_refs":[],"branch_refs":[],"candidate_id":"cand_c161151fcdc544a839fb","evidence_scope":"wider_record","hft_ref":"hft_43275845c2d77ba2b44f","item_id":"reader_summary:strongest_changes/2","kind":"reader_summary_claim","lane_basis":"unanchored reader synthesis is assigned to the widest lane","owning_lane":"global","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:reader_summary:strongest_changes/2","support_id":"sup_6d6f3f8ebc0f7752143f"},{"anchor_refs":[],"branch_refs":[],"candidate_id":"cand_76149fc7e6f4096f033d","evidence_scope":"wider_record","hft_ref":"hft_18d082cde420d71e8846","item_id":"reader_summary:what_was_special","kind":"reader_summary_claim","lane_basis":"unanchored reader synthesis is assigned to the widest lane","owning_lane":"global","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:reader_summary:what_was_special","support_id":"sup_f97da0497d3f1c71d8b5"},{"anchor_refs":[],"branch_refs":[],"candidate_id":"cand_cb1d42bfb9c6d0622c51","evidence_scope":"wider_record","hft_ref":"hft_1432c77a46e6a2c99418","item_id":"reader_summary:remaining_uncertainties/0","kind":"reader_summary_claim","lane_basis":"unanchored reader synthesis is assigned to the widest lane","owning_lane":"global","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:reader_summary:remaining_uncertainties/0","support_id":"sup_7ce388c7db06448f5eaf"},{"anchor_refs":[],"branch_refs":[],"candidate_id":"cand_ded04497a879df03e442","evidence_scope":"wider_record","hft_ref":"hft_eb3f7946abf67edaadb6","item_id":"reader_summary:remaining_uncertainties/1","kind":"reader_summary_claim","lane_basis":"unanchored reader synthesis is assigned to the widest lane","owning_lane":"global","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:reader_summary:remaining_uncertainties/1","support_id":"sup_7f6b703c655faa30af8b"},{"anchor_refs":[],"branch_refs":[],"candidate_id":"cand_d586619c86cc4d478db2","evidence_scope":"wider_record","hft_ref":"hft_893452fb452b06837c03","item_id":"reader_summary:remaining_uncertainties/2","kind":"reader_summary_claim","lane_basis":"unanchored reader synthesis is assigned to the widest lane","owning_lane":"global","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:reader_summary:remaining_uncertainties/2","support_id":"sup_63524ee456db735aa768"},{"anchor_refs":[],"branch_refs":[],"candidate_id":"cand_22b7e9c09337241b1eac","evidence_scope":"wider_or_unresolved_record","hft_ref":"hft_234011d66f21a4190e42","item_id":"reader_extension:rootless_focus","kind":"hft_reader_extension","lane_basis":"one or more HFT anchors could not be resolved, so the record is conservatively visible in the widest lane","owning_lane":"global","qualification":{"anchor_scope_complete":false,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["unrecognized HFT reader field"]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:reader_extension:rootless_focus","support_id":"sup_1bdfb6c6799a5dd33899"},{"anchor_refs":[],"branch_refs":[],"candidate_id":"cand_4c31a3fc63b76739b6a0","evidence_scope":"wider_record","hft_ref":"hft_4f0fbc44f971b85f0cee","item_id":"baseline_rootless_threshold","kind":"baseline_model","lane_basis":"unanchored reader synthesis is assigned to the widest lane","owning_lane":"global","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_rootless_threshold","support_id":"sup_e903b0c35f42506de778"}],"diagnostics":[{"warning":"Unrecognized HFT reader field is preserved as a global review record"}],"lane_counts":{"global":9,"macro":5,"micro":0},"packet_summary":{"ayah_count":15,"focus_ref":"19:1","protocol":"focus-trace-pericope-lean-v1","split_root_mappings":[],"window":["19:1","19:2","19:3","19:4","19:5","19:6","19:7","19:8","19:9","19:10","19:11","19:12","19:13","19:14","19:15"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"valid_pericope_packet_unbound_response"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"19:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":6,"unstructured_record_count":1},"identity":{"ayah_ref":"19:1","lane":"global","linguistic_source_ref":"19:1","surface_ref":"19:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"19:1","target_tokens":[["Kâf",["19:1:1"]],["Hâ",["19:1:1"]],["Yâ",["19:1:1"]],["Ayn",["19:1:1"]],["Sâd",["19:1:1"]]],"text":"Kâf Hâ Yâ Ayn Sâd."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":9,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"reader walks and cross-run publications with explicit trust labels","pericope":{"ayah_from":1,"ayah_to":15,"id":"s019-p01-001-015","label":"Zechariah and John","number":1,"refs":["19:1","19:2","19:3","19:4","19:5","19:6","19:7","19:8","19:9","19:10","19:11","19:12","19:13","19:14","19:15"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"anchor_evidence":[],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":0,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":0,"target_morphology_supplied":false},"branch_refs":[],"payload":"The sign-speech-gesture-book sequence makes the opener legible as communication outside ordinary sentence speech.","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"role":"hft_nomination_evidence","scope":"global","source_local_id":"reader_hft_a:reader_summary:strongest_changes/0","source_type":"hft","support_id":"sup_2a3b3e8a1b9ce33e4f27","trust":"legacy_unbound"},{"anchor_evidence":[],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":0,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":0,"target_morphology_supplied":false},"branch_refs":[],"payload":"The repeated naming language makes letter-names and visible marks a distinct formal reading of the sequence.","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"role":"hft_nomination_evidence","scope":"global","source_local_id":"reader_hft_a:reader_summary:strongest_changes/1","source_type":"hft","support_id":"sup_87ce01ae665b38ea378c","trust":"legacy_unbound"},{"anchor_evidence":[],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":0,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":0,"target_morphology_supplied":false},"branch_refs":[],"payload":"Immediate remembrance and the hidden call preserve oral-mnemonic and veiled-address readings alongside the graphic one.","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"role":"hft_nomination_evidence","scope":"global","source_local_id":"reader_hft_a:reader_summary:strongest_changes/2","source_type":"hft","support_id":"sup_6d6f3f8ebc0f7752143f","trust":"legacy_unbound"},{"anchor_evidence":[],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":0,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":0,"target_morphology_supplied":false},"branch_refs":[],"payload":"Because 19:1 is rootless, the productive evidence was formal rather than lexical: segmentation, pronounceability, visible marking, and adjacency could be activated without inventing a root or choosing a single decoding.","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"role":"hft_nomination_evidence","scope":"global","source_local_id":"reader_hft_a:reader_summary:what_was_special","source_type":"hft","support_id":"sup_f97da0497d3f1c71d8b5","trust":"legacy_unbound"},{"anchor_evidence":[],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":0,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":0,"target_morphology_supplied":false},"branch_refs":[],"payload":"No packet evidence determines a lexical expansion or referent for the five letters.","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"role":"hft_nomination_evidence","scope":"global","source_local_id":"reader_hft_a:reader_summary:remaining_uncertainties/0","source_type":"hft","support_id":"sup_7ce388c7db06448f5eaf","trust":"legacy_unbound"},{"anchor_evidence":[],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":0,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":0,"target_morphology_supplied":false},"branch_refs":[],"payload":"The mnemonic, concealed-call, naming, and sign-channel models may describe complementary functions or independent contextual projections.","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"role":"hft_nomination_evidence","scope":"global","source_local_id":"reader_hft_a:reader_summary:remaining_uncertainties/1","source_type":"hft","support_id":"sup_7f6b703c655faa30af8b","trust":"legacy_unbound"},{"anchor_evidence":[],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":0,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":0,"target_morphology_supplied":false},"branch_refs":[],"payload":"The textual-germination model is deliberately contained as analogy because its causal direction is reader-supplied.","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["Unanchored reader synthesis must be assessed as one inventory item, not accepted as a surah thesis."]},"role":"hft_nomination_evidence","scope":"global","source_local_id":"reader_hft_a:reader_summary:remaining_uncertainties/2","source_type":"hft","support_id":"sup_63524ee456db735aa768","trust":"legacy_unbound"},{"anchor_evidence":[],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":0,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":0,"target_morphology_supplied":false},"branch_refs":[],"payload":true,"qualification":{"anchor_scope_complete":false,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":["unrecognized HFT reader field"]},"role":"hft_nomination_evidence","scope":"global","source_local_id":"reader_hft_a:reader_extension:rootless_focus","source_type":"hft","support_id":"sup_1bdfb6c6799a5dd33899","trust":"legacy_unbound"},{"anchor_evidence":[],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":0,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":0,"target_morphology_supplied":false},"branch_refs":[],"payload":{"activation_trace":[],"changed_reading":{"after":"A deliberate formal threshold that suspends lexical reading and presents articulated units before discourse, without yet decoding them.","before":"An unreadable or semantically empty opener."},"confidence":"strong","focus_anchor":"The ayah consists only of كٓهيعٓصٓ, five isolated letter forms with no rooted morphemes in the packet.","mechanism":"Rootlessness blocks lexical and root-derived semantics, while the segmented form interrupts ordinary sentence processing and foregrounds the units from which discourse is made.","model_id":"baseline_rootless_threshold"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"global","source_local_id":"reader_hft_a:baseline_rootless_threshold","source_type":"hft","support_id":"sup_e903b0c35f42506de778","trust":"legacy_unbound"}]}
</lane_packet_json>
