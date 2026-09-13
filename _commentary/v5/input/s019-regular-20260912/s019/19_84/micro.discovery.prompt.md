# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **19:84**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s019-regular-20260912/s019/19_84/micro.discovery.json` and modify nothing
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
  "ayah_ref": "19:84",
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
{"analysis_context":{"analysis_id":"s019-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"19:84","host_surah":19,"lane_context_refs":[],"ordered_context_refs":["19:77","19:78","19:79","19:80","19:81","19:82","19:83","19:85","19:86","19:87","19:88","19:89","19:90","19:91","19:92","19:93","19:94","19:95","19:96","19:97","19:98","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal yalnız hız bildirmez; öne alma, geciktirmeme ve başkasını çabuklaştırma ilişkilerini de içerir.","branch_kind":"bare","branch_ref":"root_000987/B001","candidate_links":[{"candidate_id":"cand_e8951a749458e7274089","lane":"micro"},{"candidate_id":"cand_9a4bdfe69dab05fb7c63","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَجِلَ","morph_features":"STEM|POS:V|IMPF|LEM:Eajila|ROOT:Ejl|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:2:1","qac_word_ref":"19:84:2","surface_ar":"تَعْجَلْ"}],"gloss":"tez davranma, çabuklaştırma ve öne alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işte yavaş davranmanın karşıtı olarak hızla ve beklemeden davranmadır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir başkasını hızlandırma, bir işi erkene çekme veya bir şeyi vaktinden önce isteme ilişkisini kapsar."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Geciktirilmiş olana karşı elde bulunanı ve bir şeyin önüne geçmeyi de anlatır."}}],"root_ar":"ع ج ل","root_id":"root_000987","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın davranış, başkasını hızlandırma, vaktinden önce isteme ve geciktirmeme yönlerini birlikte temsil eder.","boundary_detail":"Bu dal yalnız hız bildirmez; öne alma, geciktirmeme ve başkasını çabuklaştırma ilişkilerini de içerir.","branch_image_ar":"الإسراع والتقديم","concept_gloss":"tez davranma, çabuklaştırma ve öne alma","contextual_glosses":[{"applicability":"Kişinin bir işi beklemeden ve hızlı yapmasını anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin hız ve beklememe yönünü eksiksiz korur."},"facet_ids":["F001"],"text":"tez davranmak","usage_role":"general"},{"applicability":"Bir kişinin başka bir kişiyi ya da işi hızlandırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başkasını hızlandıran ettirgen ilişkiyi korur."},"facet_ids":["F002"],"text":"çabuk davranmaya yöneltmek","usage_role":"contextual"},{"applicability":"Bir ödeme, iş veya isteğin zamanını erkene çekme bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Erkene çekme ve geciktirmeme ilişkisini korur."},"facet_ids":["F002","F003"],"text":"geciktirmeden öne almak","usage_role":"contextual"}],"definition":"Bir işte tez davranmak, bir şeyi ya da kişiyi çabuklaştırmak, isteneni vaktinden önce aramak veya vermek, başkasının önüne geçmek ve geciktirilmiş olmayana yönelmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işte yavaş davranmanın karşıtı olarak hızla ve beklemeden davranmadır."},{"facet_id":"F002","role":"extension","statement":"Bir başkasını hızlandırma, bir işi erkene çekme veya bir şeyi vaktinden önce isteme ilişkisini kapsar."},{"facet_id":"F003","role":"extension","statement":"Geciktirilmiş olana karşı elde bulunanı ve bir şeyin önüne geçmeyi de anlatır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öne alma, başkasını çabuklaştırma ve geciktirmeme ilişkilerini dışarıda bırakır.","preserves":"Tez davranma bileşenini genel olarak korur."},"text":"yalnızca hız"}],"identity_rationale":"Kaynak ifadesi, tez davranmayı, birini çabuk davranmaya yöneltmeyi, bir şeyi zamanından önce istemeyi, öne geçmeyi ve geciktirilmiş olanın karşısındaki eldeki durumu birlikte kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir işte tez davranma ve onu vaktinden önce isteme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tez davranan, ağırdan almayan"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"çok tez davranan"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"çabuk davranmaya yöneltmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çabuklaştırmak veya bir işten uzaklaştırmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"önüne geçmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"geciktirilmemiş, elde bulunan"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bu dünya ve eldeki dünya nimetleri"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bir şeyi vaktinden önce vermek"}],"lexicalization_note":"Tanım yalın dalın bütün kapsamını verir ve başka dallardaki araç, hayvan, kap ya da yiyecek adlarını buraya katmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yavaşlık karşıtı ile ilk davranma komşusu dal sınırını en açık biçimde gösterdiği için yayımlandı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal işi hızlandırıp öne çekerken komşu dal işi durdurur, bekletir veya yavaşlatır.","focus_only":"Tez davranma, hızlandırma ve erkene çekme yönü bulunur.","gloss":"tezlik ile yavaşlık","neighbor_only":"Bekleme, oyalanma ve yavaş davranma yönü bulunur.","neighbor_ref":"root_001339/B002","relation_type":"antonym","shared_zone":"İki dal da bir işin gerçekleşme hızını ve bekleme derecesini düzenleyen aynı eksendedir."},{"boundary_match":"partial","distinction":"Komşu dal girişimde ve yarışta önceliği öne çıkarır; odak dal ise hızlandırmayı, erkene almayı ve geciktirmemeyi de kapsar.","focus_only":"Başkasını hızlandırma ve geciktirilmiş olanın karşıtını belirtme kapsamı vardır.","gloss":"tez davranma ile ilk atılma","neighbor_only":"Bir işe ilk yönelen olma ve başkalarını geçerek girişimde bulunma vurgusu vardır.","neighbor_ref":"root_000093/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de beklemeden harekete geçme ve başkasından önce davranma alanında örtüşür."}],"source_phrase_ar":"العَجَلة في الأمر (maqayis)؛ العجل خلاف البطء (jamhara;sihah)؛ العجلة طلب الشيء وتحريه قبل أوانه (mufradat)؛ استعجلته أي حثثته (ayn;sihah;tahdhib)؛ أعجلتم أمر ربكم أي سبقتم (maqayis;sihah;tahdhib)؛ العاجل ضد الآجل (maqayis;sihah;tahdhib)","source_summary":"Kaynakların ortak çerçevesi tez davranma ile yavaşlığın karşıtlığını temel alır; buna hızlandırma, vaktinden önce isteme, öne geçme ve geciktirilmemiş olma anlamları eklenir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الإسراع والاستحثاث وطلب الشيء قبل أوانه وتقديمه على التأخير والعاجل المقابل للآجل","what_is_not_ar":"ليس ولد البقرة ولا آلة السقي ولا الإداوة ولا الطعام المتعجل"},"support_links":["sup_67b0aea7184f667db74d","sup_a25935cdfd85ffb5f624"]},{"boundary":"Yaban sığırı yavrusu kapsam dışındadır; yavrulu inek anlamı yalnız kendi söz öbeğine bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000987/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَجِلَ","morph_features":"STEM|POS:V|IMPF|LEM:Eajila|ROOT:Ejl|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:2:1","qac_word_ref":"19:84:2","surface_ar":"تَعْجَلْ"}],"gloss":"evcil sığır yavrusu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Evcil sığırın yavrusudur ve yaban sığırı yavrusunu kapsamaz."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi sığır yavrusu ayrı bir dişil biçimle adlandırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir söz öbeği, yanında yavrusu bulunan ineği anlatır."}}],"root_ar":"ع ج ل","root_id":"root_000987","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın temel ve yalın hayvan yavrusu anlamını, yaban türünü dışarıda bırakarak karşılar.","boundary_detail":"Yaban sığırı yavrusu kapsam dışındadır; yavrulu inek anlamı yalnız kendi söz öbeğine bağlıdır.","branch_image_ar":"ولد البقرة","concept_gloss":"evcil sığır yavrusu","contextual_glosses":[{"applicability":"Yavrunun dişi olduğunun açıkça belirtildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Evcil sığır yavruluğunu ve dişi cinsiyeti korur."},"facet_ids":["F001","F002"],"text":"dişi buzağı","usage_role":"contextual"},{"applicability":"Yalnız kaynakta verilen, yanında yavrusu bulunan inek söz öbeğini karşılar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ana hayvan ile yanındaki yavru arasındaki bağı korur."},"facet_ids":["F003"],"text":"yavrulu inek","usage_role":"contextual"}],"definition":"Evcil sığırın yavrusu; dişi yavru için özel bir biçim, ayrıca yalnız belirli bir söz öbeğinde yavrusu bulunan inek anlatımı vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Evcil sığırın yavrusudur ve yaban sığırı yavrusunu kapsamaz."},{"facet_id":"F002","role":"specialization","statement":"Dişi sığır yavrusu ayrı bir dişil biçimle adlandırılır."},{"facet_id":"F003","role":"associated_use","statement":"Belirli bir söz öbeği, yanında yavrusu bulunan ineği anlatır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Evcil sığır dışındaki hayvan yavrularını da yanlış biçimde kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Bir hayvanın yavrusu olma ilişkisini korur."},"text":"her hayvan yavrusu"}],"identity_rationale":"Kaynak ifadesi temel anlamı evcil sığır yavrusu olarak belirler, dişi yavruyu ayrıca gösterir ve yalnız belirli bir söz öbeğinde yavrusu bulunan ineği anlatır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"evcil sığır yavrusu, buzağı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"dişi buzağı"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"buzağı için kullanılan başka bir ad"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yavrulu inek"}],"lexicalization_note":"Yalın yavru adları ile yalnız yavrusu bulunan inek söz öbeğine bağlı kullanım birbirinden ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; geniş hayvan yavrusu adı ile sığır türü dalı, tür ve yaş sınırını en yararlı biçimde açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal evcil sığırla sınırlıdır; komşu dal çok sayıda hayvan türünün yavrusunu kapsayan daha geniş bir adlandırmadır.","focus_only":"Yalnız evcil sığır yavrusunu ve onun dişi biçimini belirtir.","gloss":"buzağı ile genel hayvan yavrusu","neighbor_only":"Yaban sığırı, eşek, keçi, koyun ve başka hayvanların yavrularına uzanır.","neighbor_ref":"root_001142/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da genç hayvanları adlandırır ve sığır yavrusu alanında yaklaşır."},{"boundary_match":"field_only","distinction":"Odak dal yaş evresine bağlı bir yavru adıdır; komşu dal türün kendisini ve topluluk adlarını belirtir.","focus_only":"Sığırın yalnız yavruluk evresini adlandırır.","gloss":"sığır yavrusu ile sığır","neighbor_only":"Sığır türünü, yetişkin hayvanı ve sürü bildiren adları kapsar.","neighbor_ref":"root_000139/B001","relation_type":"same_field","shared_zone":"İki dal da evcil sığır alanına ve aynı hayvan türüne ilişkindir."}],"source_phrase_ar":"العجل ولد البقرة (maqayis;jamhara;sihah;tahdhib;mufradat)؛ العجل عجل الثيران (ayn)؛ الأنثى عجلة والعجول مثله والجمع عجاجيل (maqayis;jamhara;sihah;tahdhib)؛ لا يقال لولد الوحشية عجل (jamhara)","source_summary":"Kaynaklar evcil sığır yavrusu anlamında birleşir; dişi yavru için ayrı biçimi, başka bir eşdeğer yavru adını ve yavrulu inek söz öbeğini de bildirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"ولد البقرة الأهلي والأنثى عجلة والعجول مثله والجمع عجاجيل","what_is_not_ar":"ليس العجلة في الأمر ولا العاجل ضد الآجل ولا آلة السقي؛ ولا يقال لولد الوحشية عجل"},"support_links":[]},{"boundary":"Dal, küçük su kabından ayrıdır ve yalnız bir kuyu çarkına indirgenemez.","branch_kind":"bare","branch_ref":"root_000987/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَجِلَ","morph_features":"STEM|POS:V|IMPF|LEM:Eajila|ROOT:Ejl|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:2:1","qac_word_ref":"19:84:2","surface_ar":"تَعْجَلْ"}],"gloss":"su çekme ve yük taşıma düzeneği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su çekmekte kullanılan çark veya döner düzenek olabilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuyunun iki dik desteği üzerine konan yatay kiriş olarak da tanımlanır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Öküzlerin çektiği veya üzerine ağır yüklerin konduğu birleşik tahta araçları da kapsar."}}],"root_ar":"ع ج ل","root_id":"root_000987","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çark, kuyu kirişi ve hayvanla çekilen yük tablası biçimlerini işlevleri üzerinden birlikte karşılar.","boundary_detail":"Dal, küçük su kabından ayrıdır ve yalnız bir kuyu çarkına indirgenemez.","branch_image_ar":"العَجَلة للسقي والحمل","concept_gloss":"su çekme ve yük taşıma düzeneği","contextual_glosses":[{"applicability":"Döner su çekme aracının anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Döner araç ile su çekme işlevini korur."},"facet_ids":["F001"],"text":"su çekme çarkı","usage_role":"contextual"},{"applicability":"Kuyunun iki dik desteği arasındaki tahta parçayı anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Parçanın yatay konumunu ve kuyu donanımındaki yerini korur."},"facet_ids":["F002"],"text":"kuyu üstü yatay kirişi","usage_role":"contextual"},{"applicability":"Ağır yüklerin konduğu veya öküzlerin çektiği tahta araç için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yük taşıma, tahta yapı ve hayvanla çekme özelliklerini korur."},"facet_ids":["F003"],"text":"hayvanla çekilen yük tablası","usage_role":"contextual"}],"definition":"Su çekme, yük taşıma veya çekme işinde kullanılan çark, kuyu üzerinde yatay kiriş ya da ağır yük konan tabla türündeki düzenek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su çekmekte kullanılan çark veya döner düzenek olabilir."},{"facet_id":"F002","role":"source_variant","statement":"Kuyunun iki dik desteği üzerine konan yatay kiriş olarak da tanımlanır."},{"facet_id":"F003","role":"extension","statement":"Öküzlerin çektiği veya üzerine ağır yüklerin konduğu birleşik tahta araçları da kapsar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kuyu kirişi ile yük taşıma ve hayvanla çekme biçimlerini dışarıda bırakır.","preserves":"Su çekmeye yarayan döner araç biçimini korur."},"text":"yalnız su çekme çarkı"}],"identity_rationale":"Kaynak ifadesi tek bir dar araç biçiminden çok, su çekme, yük taşıma veya çekme işlerinde kullanılan çark, kuyu kirişi ve yük tablası türündeki araçları topluca verir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"su çekme, yük taşıma veya çekme düzeneği"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"su çekme veya yük taşıma düzenekleri"}],"lexicalization_note":"Tanım yalın araç adının su çekme, yük taşıma ve çekme kapsamını korur; başka bir söz öbeğinden anlam aktarmaz.","neighbor_coverage_note":"Bütün aday araç dalları karşılaştırıldı; büyük su çıkrığı ve taşıma kulpu, bu dalın bütün araç ile parça sınırını en açık gösterenlerdir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal büyük su çıkrığıyla sınırlıyken odak dal kuyu kirişi ve yük taşıma aracına da uzanan daha geniş bir araç adıdır.","focus_only":"Kuyu kirişi ve ağır yük taşıyan tahta tabla biçimlerini de kapsar.","gloss":"geniş düzenek adı ile büyük su çıkrığı","neighbor_only":"Özellikle büyük su çekme çıkrığına ve hayvanlara su verme işine odaklanır.","neighbor_ref":"root_001402/B008","relation_type":"near_synonym","shared_zone":"İki dal su çekmekte kullanılan döner düzenek alanında doğrudan örtüşür."},{"boundary_match":"partial","distinction":"Odak dal bütün bir araç ya da ana kuyu parçasıdır; komşu dal kabın yükünü dengeleyen ikincil parçadır.","focus_only":"Bütün su çekme veya yük taşıma düzeneğini adlandırabilir.","gloss":"düzenek ile taşıma kulpu","neighbor_only":"Kova, tulum ya da sepetin yükü dengeleyen kulp ve yan parçalarını adlandırır.","neighbor_ref":"root_000741/B008","relation_type":"near_neighbor","shared_zone":"Her ikisi de su veya yük taşımaya yarayan araçların tahta ve tutucu parçalarıyla ilgilidir."}],"source_phrase_ar":"العجلة عجلة الثيران (maqayis;ayn;sihah)؛ العجلة المنجنون يستقى عليها (maqayis;ayn;sihah;tahdhib)؛ خشبة معترضة على نعامتي البئر (maqayis;sihah;tahdhib;mufradat)؛ خشب يؤلف شبيه بالمحفة تجعل عليه الأثقال (jamhara)؛ الدولاب (tahdhib)؛ ما يحمل على الثيران (mufradat)","source_summary":"Kaynaklar adı su çekme, kuyu donanımı, hayvanla çekme ve ağır yük taşıma işlevleri çevresinde toplar; biçim çarktan yatay kirişe ve tahta yük tablasına kadar değişir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"العَجَلة آلة أو خشب للسقي أو الحمل أو الجر ومنه المنجنون والدولاب وخشبة البئر وما تحمله الثيران أو الأثقال","what_is_not_ar":"ليست الإداوة الصغيرة ولا ولد البقرة ولا العجلة في الأمر"},"support_links":[]},{"boundary":"Küçüklük güçlü bir kullanımdır fakat bütün tanıklara zorla uygulanmaz; temel sınır taşınabilir su kabıdır.","branch_kind":"bare","branch_ref":"root_000987/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَجِلَ","morph_features":"STEM|POS:V|IMPF|LEM:Eajila|ROOT:Ejl|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:2:1","qac_word_ref":"19:84:2","surface_ar":"تَعْجَلْ"}],"gloss":"hafif, taşınabilir su kabı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su taşımak için kullanılan tulum, kırba veya benzeri kaptır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı tanımlarda küçük bir su kabı olarak sınırlandırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adın, taşıyan kişinin kolayca hızlanmasını sağlayan hafiflikle ilişkili olduğu açıklanır."}}],"root_ar":"ع ج ل","root_id":"root_000987","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Küçük kap ile daha genel tulum veya kırba kullanımlarını ortak taşıma işlevi ve hafiflik üzerinden karşılar.","boundary_detail":"Küçüklük güçlü bir kullanımdır fakat bütün tanıklara zorla uygulanmaz; temel sınır taşınabilir su kabıdır.","branch_image_ar":"الإداوة الخفيفة","concept_gloss":"hafif, taşınabilir su kabı","contextual_glosses":[{"applicability":"Kaynağın kabın küçüklüğünü açıkça belirttiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Küçük boyut ile su taşıma işlevini korur."},"facet_ids":["F001","F002"],"text":"küçük su kabı","usage_role":"contextual"},{"applicability":"Kabın tulum biçimi ve kolay taşınması öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tulum biçimi, su taşıma ve hafiflik özelliklerini korur."},"facet_ids":["F001","F003"],"text":"hafif su tulumu","usage_role":"contextual"}],"definition":"Suyu taşımaya yarayan tulum, kırba veya küçük kap; özellikle hafifliği sayesinde kolay ve hızlı taşınan biçimi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su taşımak için kullanılan tulum, kırba veya benzeri kaptır."},{"facet_id":"F002","role":"specialization","statement":"Bazı tanımlarda küçük bir su kabı olarak sınırlandırılır."},{"facet_id":"F003","role":"associated_use","statement":"Adın, taşıyan kişinin kolayca hızlanmasını sağlayan hafiflikle ilişkili olduğu açıklanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Suyu kuyudan çekmeye yarayan sabit araç anlamını ekler.","collision":"Aynı kökün ayrı su çekme aracı dalıyla karışır.","fit":"displacement","loses":"Taşınabilir kap olma ve hafiflik özelliklerini bütünüyle kaybeder.","preserves":"Su ile bağlantılı bir araç olma yönünü korur."},"text":"kuyu düzeneği"}],"identity_rationale":"Kaynak ifadesi küçük su kabını açıkça destekler, ancak bazı kaynaklarda daha genel olarak su tulumu veya kırba anlamı da vardır; hafiflik adlandırmanın gerekçesi olarak verilir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"hafif su tulumu, kırba veya küçük su kabı"}],"lexicalization_note":"Tanım yalın kap adını verir ve kuyu düzeneği anlamını ya da yiyecek dalını içine almaz.","neighbor_coverage_note":"Bütün kap ve taşıma adayları değerlendirildi; küçük kap ile genel kırba dalları, boyut ve hafiflik sınırını en iyi gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yalnız küçük kap türünü adlandırır; odak dal daha genel tulum veya kırba biçimlerini de kapsayabilir.","focus_only":"Genel tulum ve kırba kullanımı ile hafiflik gerekçesini de kapsar.","gloss":"hafif su kabı ile küçük su kabı","neighbor_only":"Küçük boyutlu belirli bir su kabı türüyle sınırlıdır.","neighbor_ref":"root_001138/B006","relation_type":"near_synonym","shared_zone":"İki dal küçük ve taşınabilir su kabı anlamında doğrudan örtüşür."},{"boundary_match":"partial","distinction":"Odak dal kolay taşınan, çoğu kez küçük veya hafif kabı öne çıkarır; komşu dal boyut ve ağırlık bakımından genel kalır.","focus_only":"Hafiflik ve bazı tanıklarda küçüklük belirleyicidir.","gloss":"hafif su kabı ile genel kırba","neighbor_only":"Su taşımaya yarayan kabın genel adı olup hafiflik veya küçüklük gerektirmez.","neighbor_ref":"root_001212/B009","relation_type":"near_neighbor","shared_zone":"Her ikisi de suyun taşındığı deri kapları adlandırır."}],"source_phrase_ar":"العجلة الإداوة الصغيرة (maqayis;ayn;mufradat)؛ العجلة المزادة أو السقاء أو القربة (jamhara;sihah;tahdhib)؛ سميت بذلك لأنها خفيفة يعجل بها حاملها (maqayis)","source_summary":"Kaynaklar taşınabilir bir su kabında birleşir; kimi ifadeler küçük kabı öne çıkarırken kimileri tulum veya kırbayı daha genel verir, ayrıca hafiflik adlandırma gerekçesi sayılır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"العَجَلة للمزادة أو الإداوة أو السقاء أو القربة الصغيرة التي يعجل بها","what_is_not_ar":"ليست آلة البئر ولا ولد البقرة ولا الطعام المتعجل"},"support_links":[]},{"boundary":"Dal genel tezlik anlamı değildir; yiyecek ve azıkla sınırlı adlar ile bir yolcu söz öbeğini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000987/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَجِلَ","morph_features":"STEM|POS:V|IMPF|LEM:Eajila|ROOT:Ejl|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:2:1","qac_word_ref":"19:84:2","surface_ar":"تَعْجَلْ"}],"gloss":"çabuk sunulan veya kolay yenilen azık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hazırlanması, sunulması veya yenmesi hızlandırılmış yiyecek ya da azıktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yolcunun kolayca yediği hurma ve kavrulmuş tahıl gibi yol yiyeceğini belirtir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çobanın ailesine hızla götürdüğü sütü veya konuklara hazırlık tamamlanmadan sunulan yemeği anlatır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kurutulmuş süt ürünü, hurma veya bunların karışımından yapılmış küçük uzun parçalar da bu adla anılır."}}],"root_ar":"ع ج ل","root_id":"root_000987","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yol yiyeceği, hızla getirilen süt, önceden sunulan yemek ve küçük yiyecek parçalarını ortak işlevle kapsar.","boundary_detail":"Dal genel tezlik anlamı değildir; yiyecek ve azıkla sınırlı adlar ile bir yolcu söz öbeğini kapsar.","branch_image_ar":"الزاد المعجل","concept_gloss":"çabuk sunulan veya kolay yenilen azık","contextual_glosses":[{"applicability":"Yolcunun yanında taşıdığı hurma veya kavrulmuş tahıl gibi yiyecekler için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yolculuk, azık olma ve kolay yenme özelliklerini korur."},"facet_ids":["F002"],"text":"kolay yenilen yol azığı","usage_role":"contextual"},{"applicability":"Konuklara asıl hazırlık tamamlanmadan önce getirilen yemek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yemeğin erkenden ve hazırlık tamamlanmadan sunulmasını korur."},"facet_ids":["F003"],"text":"hazırlık bitmeden sunulan yemek","usage_role":"contextual"}],"definition":"Çabuk hazırlanıp sunulan, kolay yenilen veya hızla eve götürülen yiyecek ve azık; yolcunun hurma benzeri yiyeceği, çobanın sütü ve konuklara hazırlık bitmeden sunulan yemek bunun özel biçimleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hazırlanması, sunulması veya yenmesi hızlandırılmış yiyecek ya da azıktır."},{"facet_id":"F002","role":"specialization","statement":"Yolcunun kolayca yediği hurma ve kavrulmuş tahıl gibi yol yiyeceğini belirtir."},{"facet_id":"F003","role":"specialization","statement":"Çobanın ailesine hızla götürdüğü sütü veya konuklara hazırlık tamamlanmadan sunulan yemeği anlatır."},{"facet_id":"F004","role":"example","statement":"Kurutulmuş süt ürünü, hurma veya bunların karışımından yapılmış küçük uzun parçalar da bu adla anılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Çabuk hazırlanma, sunulma veya kolay yenme koşulu bulunmayan bütün yiyecekleri kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Yiyecek ve yol gereksinimi yönünü korur."},"text":"her türlü azık"}],"identity_rationale":"Kaynak ifadesi ortak çekirdeği çabuk hazırlanıp sunulan, kolay yenilen veya hızla götürülen yiyecekte kurar; yol azığı, çobanın getirdiği süt, konuklara önceden sunulan yemek ve küçük yiyecek parçaları bunun türleridir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"çabuk elde edilen veya kolay yenilen azık"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yolcunun hurma ve kavrulmuş tahıl türü kolay azığı"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"çobanın ailesine hızla götürdüğü süt kabı veya süt"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"konuklara hazırlık tamamlanmadan sunulan yemek"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kurutulmuş süt ürünü, hurma veya karışımından küçük parçalar"}],"lexicalization_note":"Yalın yiyecek adları ile yalnız yolcunun kolay yiyeceği azığı anlatan söz öbeği ayrı tutulur.","neighbor_coverage_note":"Bütün yiyecek adayları değerlendirildi; belirli karışım yemeği ve bir gecelik azık, bu dalın hız koşulunu en iyi ayıran komşulardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yiyeceğin hızlı sunulması veya kolay yenmesiyle tanımlanır; komşu dal belirli bir karışım yemeğinin adıdır.","focus_only":"Çabuk hazırlanma, sunulma veya kolay yenme niteliği kurucudur.","gloss":"hızlı azık ile belirli karışım yemeği","neighbor_only":"Hurma ile süt, yağ veya kurutulmuş süt ürününden yapılan belirli bir yiyeceği ve ayrıca bir çuval adını kapsar.","neighbor_ref":"root_001659/B007","relation_type":"near_neighbor","shared_zone":"İki dal hurma ve süt ürünlerinden hazırlanan taşınabilir yiyecek alanında örtüşür."},{"boundary_match":"field_only","distinction":"Odak dal hız ve kolaylıkla, komşu dal ise yiyeceğin bir geceye yeten miktarıyla belirlenir.","focus_only":"Hazırlama, sunma veya yeme hızını ve çeşitli yiyecek biçimlerini kapsar.","gloss":"hızlı azık ile bir gecelik azık","neighbor_only":"Bir gecelik yeterlilik ölçüsüyle sınırlı yiyecek miktarını belirtir.","neighbor_ref":"root_000166/B005","relation_type":"same_field","shared_zone":"Her iki dal kısa süreli gereksinim için ayrılan yiyecek veya azık alanındadır."}],"source_phrase_ar":"العجالة ما تعجل من شيء (maqayis;sihah;tahdhib)؛ التمر عجالة الراكب (maqayis;jamhara;sihah;tahdhib)؛ العجل ما استعجل به طعام (maqayis;tahdhib)؛ العجالة ما يعجل أكله (mufradat)؛ الإعجالة اللبن الذي يعجله الراعي (jamhara;tahdhib;sihah)؛ العجيلاء طعام يقرب إلى القوم (jamhara)؛ العجاجيل هنات من الأقط والتمر (tahdhib)","source_summary":"Kaynaklar çabuk elde edilen veya kolay yenilen yiyecek çekirdeğinde birleşir; yol azığı, eve götürülen süt, hazırlıksız konuğa sunulan yemek ve hurma ya da kurutulmuş süt ürünü parçaları bu kapsamı örnekler.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"الطعام أو الزاد أو اللبن الذي يقدم أو يؤخذ بعجلة ومنه العجالة والإعجالة والعجيلاء والعجاجيل من الأقط والتمر","what_is_not_ar":"ليست العجلة في الأمر مجردا ولا الإداوة ولا آلة السقي"},"support_links":[]},{"boundary":"Belirleyici özellik erken doğum değil, yavru kaybı sonrasındaki yoğun özlem ve yas durumudur.","branch_kind":"bare","branch_ref":"root_000987/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَجِلَ","morph_features":"STEM|POS:V|IMPF|LEM:Eajila|ROOT:Ejl|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:2:1","qac_word_ref":"19:84:2","surface_ar":"تَعْجَلْ"}],"gloss":"yavrusunu yitirip özlem duyan dişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yavrusunu ölüm veya kesim yüzünden yitiren ve onun ardından özlem duyan dişi devedir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çocuğunu yitirmiş kadın için de aynı yas ve kayıp niteliğiyle kullanılır."}}],"root_ar":"ع ج ل","root_id":"root_000987","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi deve çekirdeğini ve çocuğunu yitirmiş kadına uzanan ortak kayıp durumunu birlikte karşılar.","boundary_detail":"Belirleyici özellik erken doğum değil, yavru kaybı sonrasındaki yoğun özlem ve yas durumudur.","branch_image_ar":"وله الفاقدة ولدها","concept_gloss":"yavrusunu yitirip özlem duyan dişi","contextual_glosses":[{"applicability":"Yavrusunu yitiren dişi devenin davranış ve duygu durumunu anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan türünü, yavru kaybını ve yoğun özlemi korur."},"facet_ids":["F001"],"text":"yavrusunu yitirmiş özlemli dişi deve","usage_role":"general"},{"applicability":"Adın insan için genişletilerek kullanıldığı bağlamları karşılar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Anne ile yitirilen çocuk arasındaki kayıp ilişkisini korur."},"facet_ids":["F002"],"text":"çocuğunu yitirmiş kadın","usage_role":"contextual"}],"definition":"Yavrusunu yitirdiği için onun ardından yoğun özlem duyan dişi deve; kapsam genişlemesiyle çocuğunu yitirmiş kadın.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yavrusunu ölüm veya kesim yüzünden yitiren ve onun ardından özlem duyan dişi devedir."},{"facet_id":"F002","role":"extension","statement":"Çocuğunu yitirmiş kadın için de aynı yas ve kayıp niteliğiyle kullanılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Yavru kaybı bulunmayan her türlü üzüntüyü de kapsar.","collision":"Genel üzüntü ve yas bildiren komşu dallarla karışır.","fit":"broadening","loses":null,"preserves":"Kayıp sonrasındaki olumsuz duygu durumunu kısmen korur."},"text":"yalnız üzgün"}],"identity_rationale":"Kaynak ifadesi yavrusunu ölüm veya kesim yüzünden yitirmiş, onun ardından yoğun özlem duyan dişi deveyi temel alır ve aynı adı çocuğunu yitirmiş kadın için de verir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yavrusunu yitirip özlem duyan dişi deve veya çocuğunu yitirmiş kadın"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yavrularını yitirmiş dişi develer"}],"lexicalization_note":"Tanım yalın niteleme adını hem dişi deve hem de çocuğunu yitirmiş kadın için, ortak kayıp durumu üzerinden verir.","neighbor_coverage_note":"Bütün kayıp, yas ve deve davranışı adayları incelendi; yavrusunu yitirmiş dişi deve ile genel iç yanması dalları temel sınırları yeterince gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kayıp sonrasındaki yoğun özlemi ve insan annesine uzanmayı öne çıkarır; komşu dal kaybın meydana geliş biçimlerini genişçe sıralar.","focus_only":"Yavru ardından yoğun özlem duymayı ve kadınlara uzanan kullanımı açıkça içerir.","gloss":"yavrusunu yitiren özlemli dişi deve","neighbor_only":"Yavrunun düşürülmesi, tamamlanmadan atılması veya anneden ölüm ya da kesimle alınması biçimlerini daha geniş kapsar.","neighbor_ref":"root_000727/B002","relation_type":"near_synonym","shared_zone":"İki dal yavrusunu ölüm veya başka bir kayıp yoluyla yitirmiş dişi deve alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal katılımcıları ve yavru ilişkisi bakımından özeldir; komşu dal kaybın nesnesi ve yaşayanı bakımından geneldir.","focus_only":"Belirli olarak yavrusunu yitiren dişi deveyi ve çocuğunu yitiren kadını niteler.","gloss":"yavru kaybı ile genel iç yanması","neighbor_only":"Kaçırılmış veya yitirilmiş herhangi bir şey karşısındaki pişmanlık, keder ve iç yanmasını anlatır.","neighbor_ref":"root_000320/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal bir kaybın ardından duyulan güçlü keder ve özlem alanında buluşur."}],"source_phrase_ar":"العجول من الإبل الواله التي فقدت ولدها (maqayis;sihah;tahdhib)؛ المعاجيل من الإبل اللاتي فقدت أولادها (jamhara)؛ المرأة الثكلى عجول (maqayis;tahdhib)","source_summary":"Kaynaklar yavrusunu yitirmiş ve onun ardından özlem duyan dişi devede birleşir; kullanım çocuğunu yitirmiş kadına da genişletilir.","sources":["MQ","JA","SI","TA"],"what_is_ar":"العجول من الإبل الوالهة التي فقدت ولدها ويقال للمرأة الثكلى عجول","what_is_not_ar":"ليست ولد البقرة ولا الناقة التي تلد قبل أوانها"},"support_links":[]},{"boundary":"Bu dal yavru kaybından değil, doğumun olağan vaktinden önce gerçekleşmesinden oluşur.","branch_kind":"bare","branch_ref":"root_000987/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَجِلَ","morph_features":"STEM|POS:V|IMPF|LEM:Eajila|ROOT:Ejl|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:2:1","qac_word_ref":"19:84:2","surface_ar":"تَعْجَلْ"}],"gloss":"yavrusunu vaktinden önce doğuran dişi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gebe dişinin yavrusunu olağan doğum vaktinden önce dünyaya getirmesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi deveye ilişkin biçimde erken doğan yavrunun yaşaması özellikle belirtilir."}}],"root_ar":"ع ج ل","root_id":"root_000987","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel gebe dişi kapsamını ve dişi deveye özgü yaşayan yavru koşulunu temel erken doğum ilişkisiyle karşılar.","boundary_detail":"Bu dal yavru kaybından değil, doğumun olağan vaktinden önce gerçekleşmesinden oluşur.","branch_image_ar":"الوضع قبل الإناء","concept_gloss":"yavrusunu vaktinden önce doğuran dişi","contextual_glosses":[{"applicability":"Dişi deve ve erken doğan yavrunun yaşaması birlikte belirtildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan türünü, erken doğumu ve yavrunun yaşamasını korur."},"facet_ids":["F001","F002"],"text":"erken doğurup yavrusu yaşayan dişi deve","usage_role":"contextual"},{"applicability":"Hayvan türü belirtilmeden erken doğuran gebe dişiyi anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gebelik, dişilik ve doğumun erkenliği bileşenlerini korur."},"facet_ids":["F001"],"text":"vaktinden önce doğuran gebe dişi","usage_role":"general"}],"definition":"Yavrusunu olağan gebelik süresi tamamlanmadan doğuran dişi; dişi deveye ilişkin özel kullanımda erken doğan yavru yaşar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gebe dişinin yavrusunu olağan doğum vaktinden önce dünyaya getirmesidir."},{"facet_id":"F002","role":"specialization","statement":"Dişi deveye ilişkin biçimde erken doğan yavrunun yaşaması özellikle belirtilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yavrunun ölüm veya başka yolla yitirilmesi anlamını ekler.","collision":"Aynı kökün yavru kaybı ve özlem dalıyla karışır.","fit":"displacement","loses":"Doğumun vaktinden önce gerçekleşmesi ve yavrunun yaşaması koşullarını kaybeder.","preserves":"Dişi deve ile yavrusu arasındaki doğum ilişkisini korur."},"text":"yavrusunu yitirmiş dişi deve"}],"identity_rationale":"Kaynak ifadesi, dişi devenin veya başka bir gebe dişinin yavrusunu gebelik süresi dolmadan doğurmasını anlatır; dişi deve örneğinde yavrunun yaşaması ayrıca kurucu bir sonuçtur.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"erken doğurup yavrusu yaşayan dişi deve"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yavrusunu vaktinden önce doğuran gebe dişi"}],"lexicalization_note":"Tanım yalın niteleme biçimlerinin erken doğum sınırını korur ve süt ya da yasla ilgili ayrı anlamları dışarıda bırakır.","neighbor_coverage_note":"Bütün gebelik ve doğum adayları karşılaştırıldı; yavru kaybı ile gebeliğin tamamlanması, erken doğum sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal sürenin eksik kalmasını, komşu dal ise gebeliğin olgunluğa ve tamamlanmaya kadar sürmesini anlatır.","focus_only":"Gebeliğin olağan süresi dolmadan doğum gerçekleşir.","gloss":"erken doğum ile süresini tamamlama","neighbor_only":"Gebelik yavru olgunlaşıncaya ve süre tamamlanıncaya kadar uzar.","neighbor_ref":"root_001432/B007","relation_type":"polarity_pair","shared_zone":"İki dal gebeliğin olağan tamamlanma süresine göre doğum zamanını karşıt yönlerden belirler."}],"source_phrase_ar":"المعجل والمعجل من النوق التي تنتج قبل أن تستكمل الوقت فيعيش ولدها (maqayis)؛ المعجال من الحوامل التي تضع ولدها قبل إناه (tahdhib)","source_summary":"Kaynaklar gebelik süresi dolmadan doğuran dişiyi bildirir; dişi deve tanımında yavrunun erken doğuma karşın yaşadığı ayrıca belirtilir.","sources":["MQ","TA"],"what_is_ar":"المعجل أو المعجال من النوق أو الحوامل التي تضع ولدها قبل تمام الوقت فيعيش ولدها","what_is_not_ar":"ليس الإعجالة من اللبن ولا العجول الفاقدة ولدها"},"support_links":[]},{"boundary":"Bu kullanımlar yolculuk ve gidiş bağlamına bağlıdır; kökün genel tez davranma anlamıyla birleştirilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000987/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَجِلَ","morph_features":"STEM|POS:V|IMPF|LEM:Eajila|ROOT:Ejl|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:2:1","qac_word_ref":"19:84:2","surface_ar":"تَعْجَلْ"}],"gloss":"hızlı gidiş, kestirme yol ve erken sıçrama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yolculukta hızlı gerçekleşen belirli bir gidiş biçimidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Varış uzaklığını azaltan yakın veya kestirme yolları belirtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yalnız binicilik söz öbeğinde, binici yerleşmeden devenin sıçramasını anlatır."}}],"root_ar":"ع ج ل","root_id":"root_000987","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın gidiş, yol ve binicilik söz öbeğine bağlı üç kullanımını birbirine karıştırmadan topluca gösterir.","boundary_detail":"Bu kullanımlar yolculuk ve gidiş bağlamına bağlıdır; kökün genel tez davranma anlamıyla birleştirilmez.","branch_image_ar":"السير والطريق المعجل","concept_gloss":"hızlı gidiş, kestirme yol ve erken sıçrama","contextual_glosses":[{"applicability":"Yolculuğun veya binek gidişinin hızını anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gidiş biçimini ve onun hızlı oluşunu korur."},"facet_ids":["F001"],"text":"hızlı gidiş biçimi","usage_role":"contextual"},{"applicability":"Uzaklığı azaltıp varışı hızlandıran yol seçenekleri için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yolların yakınlığını ve kestirme işlevini korur."},"facet_ids":["F002"],"text":"yakın ve kestirme yollar","usage_role":"contextual"},{"applicability":"Yalnız kaynakta verilen binicilik söz öbeğinin açıklayıcı karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Devenin sıçramasını ve binicinin henüz yerleşmemiş olmasını korur."},"facet_ids":["F003"],"text":"binici yerleşmeden devenin sıçraması","usage_role":"explanatory"}],"definition":"Yolculukta hızlı bir gidiş biçimi veya varışı kısaltan yakın yollar; ayrıca belirli bir binicilik söz öbeğinde, binici yerine tam yerleşmeden devenin sıçraması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yolculukta hızlı gerçekleşen belirli bir gidiş biçimidir."},{"facet_id":"F002","role":"extension","statement":"Varış uzaklığını azaltan yakın veya kestirme yolları belirtir."},{"facet_id":"F003","role":"associated_use","statement":"Yalnız binicilik söz öbeğinde, binici yerleşmeden devenin sıçramasını anlatır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yolculuk, yol ve binicilik dışındaki bütün tez davranma olaylarını kapsar.","collision":"Aynı kökün genel hızlandırma ve öne alma dalıyla karışır.","fit":"broadening","loses":null,"preserves":"Hız ve beklememe düşüncesini genel olarak korur."},"text":"genel olarak tez davranma"}],"identity_rationale":"Kaynak ifadesi üç ayrı ama tezlik ortaklı kullanımı açıkça verir: hızlı bir gidiş biçimi, yakın veya kestirme yollar ve binici yerleşmeden devenin sıçraması.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"hızlı bir gidiş biçimi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yakın veya kestirme yollar"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"binici yerleşmeden devenin sıçraması"}],"lexicalization_note":"Yalınlaşmış gidiş ve yol adları ile yalnız binicilik söz öbeğine bağlı sıçrama kullanımı ayrı facetlerde tutulur.","neighbor_coverage_note":"Bütün gidiş, yol ve binek adayları değerlendirildi; hızlı koşu ile kestirme seçme dalları, üçlü kapsamın temel sınırlarını yeterince açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal koşma ve genel ilerleme hızına odaklanır; odak dal belirli gidiş biçiminin yanında kestirme yol ve erken sıçrama kullanımlarına sahiptir.","focus_only":"Kestirme yol ve binici yerleşmeden devenin sıçraması kullanımlarını da içerir.","gloss":"hızlı gidiş ile hızlı koşu","neighbor_only":"Koşma şiddetini ve yeryüzünde hızla ilerlemeyi genel biçimde kapsar.","neighbor_ref":"root_000329/B005","relation_type":"near_synonym","shared_zone":"İki dal hızlı yol alma ve süratli gidiş anlamında doğrudan örtüşür."},{"boundary_match":"partial","distinction":"Odak dal kısa yolların kendisini adlandırır; komşu dal bu yollar arasından en kısasını seçme eylemini anlatır.","focus_only":"Hızlı gidiş biçimi ve binicilikte erken sıçrama kullanımını da kapsar.","gloss":"kestirme yollar ile kestirmeyi seçme","neighbor_only":"Bir yolun seçenekleri arasından en yakın ve kısa olanı seçme eylemini belirtir.","neighbor_ref":"root_000406/B005","relation_type":"near_synonym","shared_zone":"İki dal varışı hızlandıran yakın veya kısa yol kullanımı alanında örtüşür."}],"source_phrase_ar":"العجيلي ضرب من السير سريع (tahdhib)؛ معاجيل الطرق أقرب (tahdhib)؛ الإعجال في السير أن يثب البعير قبل استواء الراكب عليه (tahdhib)","source_summary":"Tek kaynak hızlı gidişi, yakın veya kestirme yolları ve binicinin yerleşmesini beklemeden devenin sıçramasını yolculuk çevresindeki ayrı kullanımlar olarak verir.","sources":["TA"],"what_is_ar":"السير السريع والطريق القريب أو المختصر ووثوب البعير قبل استواء الراكب عليه","what_is_not_ar":"ليس العجلة في الأمر عامة ولا العجالة من الطعام"},"support_links":[]},{"boundary":"Dal yalnız özel bir bitki adıdır; hangi tür olduğu kanıtsız biçimde belirlenmez.","branch_kind":"bare","branch_ref":"root_000987/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَجِلَ","morph_features":"STEM|POS:V|IMPF|LEM:Eajila|ROOT:Ejl|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:2:1","qac_word_ref":"19:84:2","surface_ar":"تَعْجَلْ"}],"gloss":"belirli bir bitki veya ağaç adı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir bitki türünün özel adıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kaynak varyantı bu bitkiyi ağaç olarak sınıflandırır."}}],"root_ar":"ع ج ل","root_id":"root_000987","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Türü bilinmeyen bitki adını ve ağaç olarak verilen kaynak varyantını kanıt sınırları içinde karşılar.","boundary_detail":"Dal yalnız özel bir bitki adıdır; hangi tür olduğu kanıtsız biçimde belirlenmez.","branch_image_ar":"النبت المسمى عجلة","concept_gloss":"belirli bir bitki veya ağaç adı","contextual_glosses":[{"applicability":"Türün özellikleri bilinmeden yalnız bitki adı oluşunun aktarılması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli fakat tanımlanmamış bir bitki adı olma sınırını korur."},"facet_ids":["F001"],"text":"adı belirtilen bir bitki türü","usage_role":"explanatory"}],"definition":"Türü ve ayırt edici özellikleri açıklanmayan belirli bir bitkinin adı; bir kaynak varyantında ağaç olarak nitelenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir bitki türünün özel adıdır."},{"facet_id":"F002","role":"source_variant","statement":"Bir kaynak varyantı bu bitkiyi ağaç olarak sınıflandırır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Bütün bitki türlerini kapsayarak özel ad olma sınırını ortadan kaldırır.","collision":"Genel bitki ve ağaç adlarını bildiren komşu dallarla karışır.","fit":"broadening","loses":null,"preserves":"Bitki alanına ait olma bilgisini korur."},"text":"genel olarak bitki"}],"identity_rationale":"Kaynak ifadesi sözcüğü belirli bir bitkinin adı olarak verir; bir tanık bunu ağaç diye niteler. Türü belirleyecek başka özellik bulunmadığından daha dar bir bitki eşlemesi yapılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"belirli bir bitki veya ağaç türünün adı"}],"lexicalization_note":"Tanım yalın bitki adını kaynakta verilen bitki veya ağaç sınırıyla korur ve başka dalların anlamlarını buraya taşımaz.","neighbor_coverage_note":"Bütün bitki adayları değerlendirildi; genel ağaç dalı ile özellikleri verilen özel bitki dalı, bu adın belirsiz tür sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tek bir türün açıklanmamış özel adıdır; komşu dal gövdeli bitkilerin genel sınıfını anlatır.","focus_only":"Tür özellikleri açıklanmayan tek bir özel bitki adını belirtir.","gloss":"özel bitki adı ile genel ağaç","neighbor_only":"Gövdeli bitkileri genel olarak, onların çoğalmasını ve hayvanların bunlarla beslenmesini kapsar.","neighbor_ref":"root_000777/B001","relation_type":"near_neighbor","shared_zone":"İki dal ağaç olarak nitelenebilen bitkiler alanında buluşur."},{"boundary_match":"field_only","distinction":"Ortak yönleri yalnız bitki adı olmalarıdır; komşu dalın tür ve durum özellikleri odak dal için kanıtlanmamıştır.","focus_only":"Kimliği ve özellikleri kaynakta açıklanmayan bir bitkiyi adlandırır.","gloss":"iki ayrı özel bitki adı","neighbor_only":"Belirli bir çalımsı bitkiyi ve onun yaş ya da kuru durumunu bildirir.","neighbor_ref":"root_001250/B017","relation_type":"same_field","shared_zone":"İki dal da sözlükte belirli bir bitki türüne verilmiş özel adlardır."}],"source_phrase_ar":"العجلة ضرب من النبت (jamhara;sihah;tahdhib)؛ العجلة شجرة (tahdhib)","source_summary":"Kaynaklar sözcüğü belirli bir bitkinin adı sayar; bunlardan biri bitkiyi ayrıca ağaç diye niteler, fakat türü tanıtacak ayrıntı vermez.","sources":["JA","SI","TA"],"what_is_ar":"العجلة اسم لنبت أو شجرة","what_is_not_ar":"ليست الإداوة ولا آلة البئر ولا العجلة في الأمر"},"support_links":[]},{"boundary":"Çekirdek sayma ve sayıyla belirlemedir; hazırlama, zaman bekleme, kalıcı su ve dönemsel yineleme bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B001","candidate_links":[{"candidate_id":"cand_e8951a749458e7274089","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|IMPF|LEM:Ead~a|ROOT:Edd|1P","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:5:1","qac_word_ref":"19:84:5","surface_ar":"نَعُدُّ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:84:7:1","qac_word_ref":"19:84:7","surface_ar":"عَدًّا"}],"gloss":"sayma, sayı ve sayıya göre bir topluluğa katma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin birimlerini sayıp toplam miktarını belirleme işlemi."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sayma sonucundaki miktar, sayı ve sayılmış ya da sınırlandırılmış varlık."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sayıca çokluğu belirtme veya birini belirli bir topluluğun üyeleri arasında sayma."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sayma işlemiyle onun doğrudan sonuçlarını ve sayıya dayalı topluluk üyeliğini birlikte anlatan kapsayıcı karşılıktır.","boundary_detail":"Çekirdek sayma ve sayıyla belirlemedir; hazırlama, zaman bekleme, kalıcı su ve dönemsel yineleme bu dala girmez.","branch_image_ar":"إحصاء المعدود","concept_gloss":"sayma, sayı ve sayıya göre bir topluluğa katma","contextual_glosses":[{"applicability":"Bir nesne topluluğunun kaç birimden oluştuğunun belirlenmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sayma eylemini ve miktarı belirleme sonucunu birlikte korur."},"facet_ids":["F001"],"text":"sayıp miktarını belirlemek","usage_role":"general"},{"applicability":"Eylemden çok sayma sonucunu veya sayıyla sınırlandırılmış varlığı anlatan bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sayma sonucundaki sayı ve miktar değerini korur."},"facet_ids":["F002"],"text":"sayı ve sayılan miktar","usage_role":"contextual"},{"applicability":"Bir kişinin belirli bir topluluğa dahil kabul edildiği kalıplaşmış bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir topluluğun üyeleri içinde sayılma ilişkisini korur."},"facet_ids":["F003"],"text":"arasında sayılmak","usage_role":"contextual"}],"definition":"Bir şeyi tek tek sayarak miktarını belirleme; bu işlemin sonucu olan sayı, sayılan varlıkların sayıca niteliği ve bir kimseyi ya da şeyi belirli bir topluluk içinde sayma alanıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin birimlerini sayıp toplam miktarını belirleme işlemi."},{"facet_id":"F002","role":"extension","statement":"Sayma sonucundaki miktar, sayı ve sayılmış ya da sınırlandırılmış varlık."},{"facet_id":"F003","role":"associated_use","statement":"Sayıca çokluğu belirtme veya birini belirli bir topluluğun üyeleri arasında sayma."}],"identity_rationale":"Kaynak ifadesi, bir şeyi tek tek sayıp miktarını belirleme çekirdeğini; sayı, sayılan şey, sayıca çokluk ve bir topluluk içinde sayılma kullanımlarıyla birlikte açıkça destekler. Geçici çerçeve bu kapsamı başka dallardaki hazırlama, bekleme süresi, su ve zaman anlamlarından doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi sayıp miktarını belirlemek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sayı; sayılanın miktarı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"sayıca çokluk"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sayılmış veya sayıyla sınırlandırılmış"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"iyiler arasında sayılmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"az ya da çok sayıda topluluk"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"sayıları on bini aşmak"}],"lexicalization_note":"Tanım sayma çekirdeğini temel alır; topluluk içinde sayılma ve belli bir sayıyı aşma yalnızca kendi kalıplarıyla sınırlı tutulur.","neighbor_coverage_note":"Verilen komşu adaylarının tümü incelendi; sayma ile hesap, bütünleme ve karşılıklı sayılma arasındaki en açıklayıcı üç sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı saymanın kendisiyle sayı ve üyelik sonuçlarını birlikte taşır; komşu dal ise hesabı, hesaplaşmayı ve tahmini de içerdiği için bütünüyle birbirinin yerine geçmez.","focus_only":"Sayı, sayılan varlık, sayıca çokluk ve bir topluluğun içinde sayılma kullanımlarını da kapsar.","gloss":"sayma ve hesaplama","neighbor_only":"Hesaplaşma, tahmin ve gök cisimlerinin hesabı gibi daha geniş hesap alanlarına uzanır.","neighbor_ref":"root_000318/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da nesneleri sayma ve sayısal bir sonuç elde etme alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalında birimleri sayma belirleyicidir; komşuda ise sayma gerekmeksizin parçaları topluca ve ayrıntısız biçimde kapsama esastır.","focus_only":"Tek tek sayma, sayısal miktar ve sayıya göre topluluğa katma işlemlerini bildirir.","gloss":"toplam ve bütün","neighbor_only":"Dağınık parçaları ayrıntılandırmadan tek bir bütün veya genel toplam halinde birleştirir.","neighbor_ref":"root_000260/B003","relation_type":"near_neighbor","shared_zone":"Sayılmış parçaların bir sonuçta toplanması iki alan arasında sınırlı bir temas kurar."},{"boundary_match":"partial","distinction":"Odak dalının çekirdeği sayısal belirlemedir; komşu dalın çekirdeği ise paydaşlar veya denkler arasında kurulan karşılıklı ilişkidir.","focus_only":"Varlıkları sayıp miktar belirlemeyi ve bir topluluk içinde saymayı kapsar.","gloss":"sayma ile karşılıklı sayılma","neighbor_only":"Karşılıklı paydaşlık, pay veya iki kişinin birbirine denk sayılması ilişkisini kapsar.","neighbor_ref":"root_000989/B006","relation_type":"near_neighbor","shared_zone":"İki dalda da bir kişi ya da şey başkalarıyla birlikte değerlendirilip sayılabilir."}],"source_phrase_ar":"عددت الشيء عدا أي أحصيته (maqayis;ayn;sihah;tahdhib)؛ العدد مقدار ما يعد (maqayis)؛ العديد الكثرة (maqayis;ayn;sihah;tahdhib)؛ فلان في عداد الصالحين (maqayis;ayn;sihah)؛ العدد آحاد مركبة (mufradat)","source_summary":"Toplu tanıklık, sayma işlemini temel alır ve bundan sayı, sayılan şey, sayıca çokluk ve bir topluluğa dahil sayılma kullanımlarını geliştirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الإحصاء وضم الأعداد واسم العدد والمعدود والكثرة أو القلة من جهة كون الشيء يحصى أو يعد في جماعة","what_is_not_ar":"ليس إعداد الشيء وتهيئته ولا عدة المرأة ولا الماء العد ولا العداد الزماني"},"support_links":["sup_67b0aea7184f667db74d"]},{"boundary":"Bu dal gelecekteki ihtiyaç için hazırlamadır; sayısal sayma, hukuki bekleme süresi veya yalnızca mevcut bulunma anlamı değildir.","branch_kind":"bare","branch_ref":"root_000989/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|IMPF|LEM:Ead~a|ROOT:Edd|1P","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:5:1","qac_word_ref":"19:84:5","surface_ar":"نَعُدُّ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:84:7:1","qac_word_ref":"19:84:7","surface_ar":"عَدًّا"}],"gloss":"gelecekteki bir iş için hazırlama ve hazır bulundurma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi gelecekteki belirli bir iş veya olay için önceden hazırlamak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İhtiyaç anı için mal, silah veya başka bir gereci ayırıp hazır tutmak."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hazırlanan şeyi gerektiğinde erişilip alınabilecek bir durumda bulundurmak."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel hazırlama eylemini, ihtiyaç için kaynak ayırmayı ve kullanılabilir durumda tutmayı birlikte karşılar.","boundary_detail":"Bu dal gelecekteki ihtiyaç için hazırlamadır; sayısal sayma, hukuki bekleme süresi veya yalnızca mevcut bulunma anlamı değildir.","branch_image_ar":"تهيئة العدة","concept_gloss":"gelecekteki bir iş için hazırlama ve hazır bulundurma","contextual_glosses":[{"applicability":"Bir şeyin ilerideki belirli bir iş için uygun duruma getirilmesini anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gelecekteki işe yönelik ön hazırlama işlemini korur."},"facet_ids":["F001"],"text":"önceden hazırlamak","usage_role":"general"},{"applicability":"Hazırlanan şeyin ihtiyaç anında erişilebilir ve kullanılabilir tutulduğu bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hazırlanan şeyin erişilebilir ve kullanıma hazır tutulmasını korur."},"facet_ids":["F003"],"text":"gerektiğinde kullanmak üzere hazır tutmak","usage_role":"contextual"},{"applicability":"İlerideki olaylar için mal, silah veya başka araçların önceden ayrılması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İhtiyaca yönelik somut araç ve kaynak ayırma işlemini korur."},"facet_ids":["F002"],"text":"gereç ve kaynak ayırmak","usage_role":"contextual"}],"definition":"Bir şeyi ileride doğacak bir iş veya ihtiyaç için önceden hazırlamak, gerektiğinde kullanılabilecek biçimde hazır tutmak ve bu amaçla mal, silah ya da başka gereç ayırmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi gelecekteki belirli bir iş veya olay için önceden hazırlamak."},{"facet_id":"F002","role":"specialization","statement":"İhtiyaç anı için mal, silah veya başka bir gereci ayırıp hazır tutmak."},{"facet_id":"F003","role":"extension","statement":"Hazırlanan şeyi gerektiğinde erişilip alınabilecek bir durumda bulundurmak."}],"identity_rationale":"Kaynak ifadesi bir şeyi gelecekteki bir iş veya olay için hazırlamayı, hazır ve erişilebilir duruma getirmeyi, ayrıca ihtiyaç anı için mal, silah ve gereç ayırmayı ortak bir çekirdekte birleştirir. Geçici dal kimliği bu işlemi sayma ve öteki dallardan doğru biçimde ayırmaktadır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyi ilerideki iş için hazırlamak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ilerideki ihtiyaç için hazırlanmış mal, silah veya gereç"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir işe hazırlanmak ve donanmak"}],"lexicalization_note":"Tanım çıplak hazırlama anlamını verir; belirli bir kalıba özgü kapsam eklemez ve hazırlanan araçları yalnızca desteklenen örnekler olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel hazırlama, amaç için ayırma, hazır bulunma ve ek güvence arasındaki en yararlı üç karşıtlık seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı genel hazırlama ve donanım alanıdır; komşu dalda hazırlanan şeyin belirli bir alıcıya, borca veya karşılığa bağlanması daha belirleyicidir.","focus_only":"Her türlü gelecek iş için hazırlama ile araç ve kaynakları hazır tutmayı genel olarak kapsar.","gloss":"hazırlama ve belirli amaç için ayırma","neighbor_only":"Bir şeyi belirli bir kişi, borç veya karşılık için özellikle ayırıp gözetme anlamını taşır.","neighbor_ref":"root_000566/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi ilerideki kullanım için önceden hazır hale getirmeyi içerir."},{"boundary_match":"partial","distinction":"Odak dalında amaçlı hazırlama işlemi merkezdeyken komşuda hazır bulunma durumu ve el altındaki donanım daha geniş bir yer tutar.","focus_only":"Hazırlama eylemini ve gelecekteki olay için kaynak ayırmayı öne çıkarır.","gloss":"hazırlamak ve hazır bulunmak","neighbor_only":"Hazır, yakın ve elde bulunan durum ile sürekli el altında tutulan donanımı da adlandırır.","neighbor_ref":"root_000978/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin ihtiyaç anında kullanılmaya hazır olmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalı nötr hazırlamayı anlatır; komşu dal ise belirsizlik veya tehlikeye karşı fazladan güvence sağlama amacını gerektirir.","focus_only":"Beklenen iş için gerekli şeyi hazırlayıp kullanıma hazır hale getirir.","gloss":"hazırlık ve güvence önlemi","neighbor_only":"Güvenceyi artırmak için gereğinden fazla önlem veya yedek edinmeyi içerir.","neighbor_ref":"root_000970/B021","relation_type":"near_neighbor","shared_zone":"Gelecekteki bir gereksinime karşı önceden araç edinme iki dalın ortak alanıdır."}],"source_phrase_ar":"أعددت الشيء إعدادا (maqayis)؛ أعددت الشيء هيأته (ayn)؛ العدة من السلاح ما اعتددته (jamhara)؛ أعده لأمر كذا هيأه له (sihah)؛ العدة ما أعد لأمر يحدث مثل الأهبة (tahdhib)؛ أعددت هذا لك أي جعلته بحيث تعده وتتناوله (mufradat)","source_summary":"Toplu tanıklık, önceden hazırlama ve hazır tutma çekirdeğinde birleşir; ayrılan mal, silah ve gereçler yaklaşan ihtiyaçlara yönelik somut uygulamalardır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"تهيئة الشيء لأمر حادث واتخاذ العدة والأهبة والذخيرة والسلاح والمال لما يحتاج إليه","what_is_not_ar":"ليست الإحصاء نفسه ولا عدة المرأة ولا الماء العد"},"support_links":[]},{"boundary":"Ortak sınır sayıyla belirlenmiş zaman dilimidir; bekleme, sonradan yerine getirme ve belirli günler birbirinden ayrı bağlamsal gerçekleşmelerdir.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B003","candidate_links":[{"candidate_id":"cand_9a4bdfe69dab05fb7c63","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|IMPF|LEM:Ead~a|ROOT:Edd|1P","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:5:1","qac_word_ref":"19:84:5","surface_ar":"نَعُدُّ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:84:7:1","qac_word_ref":"19:84:7","surface_ar":"عَدًّا"}],"gloss":"sayılı zaman dilimi ve bağlama bağlı bekleme ya da tamamlama süresi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gün, ay, dönemsel çevrim veya olay sonuyla ölçülüp sınırlandırılmış zaman dilimi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kadının belirli çevrimler, aylar veya gebeliğin sona ermesiyle ölçülen bekleme süresi."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaçırılmış günlerin sayısına eşit sayıda günü daha sonra yerine getirme yükümlülüğü."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Belirli ve az sayıdaki günlerin adlandırılması."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sayılı süre çekirdeğini ve bu sürenin farklı bağlamlarda bekleme veya eksik günleri tamamlama işlevini birlikte açıklar.","boundary_detail":"Ortak sınır sayıyla belirlenmiş zaman dilimidir; bekleme, sonradan yerine getirme ve belirli günler birbirinden ayrı bağlamsal gerçekleşmelerdir.","branch_image_ar":"مدة العدة المعدودة","concept_gloss":"sayılı zaman dilimi ve bağlama bağlı bekleme ya da tamamlama süresi","contextual_glosses":[{"applicability":"Kadın için çevrim, ay veya doğumla ölçülen hukuki bekleme bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölçülmüş süreyi ve yeniden evlenmeden önce bekleme koşulunu korur."},"facet_ids":["F001","F002"],"text":"yeniden evlenmeden önceki bekleme süresi","usage_role":"contextual"},{"applicability":"Yerine getirilemeyen günlerin aynı sayıda başka günle tamamlanması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaçırılan ve sonradan tamamlanan günler arasındaki sayı eşitliğini korur."},"facet_ids":["F001","F003"],"text":"kaçırılan günler kadar sonradan tamamlama","usage_role":"contextual"},{"applicability":"Özel olarak belirlenmiş, sınırlı sayıdaki günlerden söz edilen bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günlerin belirli ve sayıca sınırlı oluşunu korur."},"facet_ids":["F001","F004"],"text":"sayılı ve belirli günler","usage_role":"contextual"}],"definition":"Sayısı veya bitiş ölçütü belirlenmiş bir zaman dilimidir. Bağlama göre bu dilim kadın için bekleme süresi, kaçırılan günler kadar sonradan yerine getirme süresi ya da özellikle belirlenmiş sınırlı günler olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gün, ay, dönemsel çevrim veya olay sonuyla ölçülüp sınırlandırılmış zaman dilimi."},{"facet_id":"F002","role":"specialization","statement":"Bir kadının belirli çevrimler, aylar veya gebeliğin sona ermesiyle ölçülen bekleme süresi."},{"facet_id":"F003","role":"specialization","statement":"Kaçırılmış günlerin sayısına eşit sayıda günü daha sonra yerine getirme yükümlülüğü."},{"facet_id":"F004","role":"example","statement":"Belirli ve az sayıdaki günlerin adlandırılması."}],"identity_rationale":"Kaynak ifadesi yalnızca zorunlu bir bekleme süresini değil, kadın için ölçülen bekleme dönemini, kaçırılan günler kadar sonradan yerine getirme süresini ve belirli sayıda günleri birlikte içerir. Dal korunabilir, ancak bütün örnekleri tek bir bekleme yükümlülüğü gibi sunmak yerine sayıyla sınırlandırılmış zaman dilimleri ve bağlama göre üstlendikleri görevler üzerinden tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kadının yeniden evlenmeden önce beklemesi gereken süre"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kaçırılan günler kadar başka günlerde yerine getirmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"sayılı ve belirli günler"}],"lexicalization_note":"Tanım, sayılı süre çekirdeğini korurken kadınla ilgili bekleme, kaçırılan günleri tamamlama ve belirli günler kalıplarını ayrı tutar.","neighbor_coverage_note":"Bütün adaylar incelendi; ölçülmüş bekleme süresini dönemsel çevrimden, genel saymadan ve sıradan ertelemeden ayıran üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı ölçülen toplam süre ve yükümlülükle ilgilidir; komşu dal ise bu sürenin ölçütü olabilen bedensel çevrimin evrelerini adlandırır.","focus_only":"Kadının toplam bekleme süresini, eksik günlerin tamamlanmasını ve başka sayılı günleri kapsar.","gloss":"bekleme süresi ve dönemsel çevrim","neighbor_only":"Kadın bedenindeki kanama ve temizlik evrelerinin kendisini, geçişlerini ve aralarındaki çevrimi adlandırır.","neighbor_ref":"root_001210/B003","relation_type":"near_neighbor","shared_zone":"Kadının bekleme süresi dönemsel bedensel çevrimlerle ölçülebildiği için alanlar kesişir."},{"boundary_match":"partial","distinction":"Odak dalında sayma zaman dilimini ve bağlamsal görevi sınırlar; komşu dalda ise nesnesi zaman olmak zorunda olmayan genel sayma çekirdektir.","focus_only":"Sayının belirlediği zaman dilimini ve bu dilime bağlı bekleme veya tamamlama görevini kapsar.","gloss":"sayılı süre ve genel sayma","neighbor_only":"Her tür varlığı sayma, sayıyı adlandırma ve bir topluluk içinde sayma işlemlerini kapsar.","neighbor_ref":"root_000989/B001","relation_type":"near_neighbor","shared_zone":"Bir sürenin kaç gün veya dönemden oluştuğunu belirleme, genel sayma işlemine dayanır."},{"boundary_match":"partial","distinction":"Odak dalında sayıyla veya bitiş ölçütüyle sınırlandırılmış süre esastır; komşu dalda belirleyici olan yalnızca sonraya bırakmadır.","focus_only":"Ölçüsü belirli bir bekleme veya sonradan tamamlama süresini gerektirir.","gloss":"ölçülü bekleme ve erteleme","neighbor_only":"Bir işi ya da ödemeyi daha sonraki bir zamana bırakma eylemini genel olarak bildirir.","neighbor_ref":"root_000019/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir işlemin daha sonraki bir zamanda gerçekleşmesini içerebilir."}],"source_phrase_ar":"عدة المرأة أيام قروئها (ayn)؛ عدة المرأة معروفة (jamhara)؛ عدة المرأة أيام أقرائها (sihah)؛ العدة عدة المرأة شهورا كانت أو أقراء أو وضع حمل (tahdhib)؛ فعدة من أيام أخر أي عليه أيام بعدد ما فاته (mufradat)؛ الأيام المعدودات أيام التشريق (sihah;tahdhib;mufradat)","source_summary":"Toplu tanıklık, sayıyla veya belirli bir bitiş ölçütüyle sınırlandırılmış zaman dilimlerini; bekleme, eksik günleri tamamlama ve belirli günleri adlandırma bağlamlarında gösterir.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"المدة المعدودة الواجبة انتظارا أو قضاء كعدة المرأة وعدة الأيام الفائتة والأيام المعدودات","what_is_not_ar":"ليست الأهبة والسلاح ولا مجرد كثرة العدد"},"support_links":["sup_a25935cdfd85ffb5f624"]},{"boundary":"Dalın ayırıcı niteliği suyun kalıcı veya sürekli beslenen oluşudur; geçici yağmur suyu ve kısa ömürlü birikintiler kapsam dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|IMPF|LEM:Ead~a|ROOT:Edd|1P","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:5:1","qac_word_ref":"19:84:5","surface_ar":"نَعُدُّ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:84:7:1","qac_word_ref":"19:84:7","surface_ar":"عَدًّا"}],"gloss":"kaynağı kesilmeyen kalıcı su ve su yeri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğal olarak bir yerde toplanmış su veya bu suyun bulunduğu yer."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eskiden beri var olan ve su çekildikçe tükenmeyen kalıcı su."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Besleyici kaynağı kesilmediği için akışı veya varlığı sürekli kalan su."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem sürekli suyu hem de onun doğal olarak toplandığı veya çıkarıldığı kalıcı yeri karşılar.","boundary_detail":"Dalın ayırıcı niteliği suyun kalıcı veya sürekli beslenen oluşudur; geçici yağmur suyu ve kısa ömürlü birikintiler kapsam dışındadır.","branch_image_ar":"الماء العد","concept_gloss":"kaynağı kesilmeyen kalıcı su ve su yeri","contextual_glosses":[{"applicability":"Çekilmesine rağmen besleyici kaynağı sürdüğü için tükenmeyen suyu anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suyun sürekliliğini ve çekmekle tükenmemesini korur."},"facet_ids":["F002","F003"],"text":"tükenmeyen sürekli su","usage_role":"general"},{"applicability":"Suyun kendisinden çok onu sürekli sağlayan yer veya kaynak kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suyun bulunduğu yeri ve kaynağın sürekliliğini korur."},"facet_ids":["F001","F003"],"text":"kalıcı su kaynağı","usage_role":"contextual"}],"definition":"Doğal olarak birikmiş, eski veya besleyici kaynağı kesilmediği için çekmekle tükenmeyen sürekli su ve bu suyun bulunduğu kalıcı su yeridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğal olarak bir yerde toplanmış su veya bu suyun bulunduğu yer."},{"facet_id":"F002","role":"specialization","statement":"Eskiden beri var olan ve su çekildikçe tükenmeyen kalıcı su."},{"facet_id":"F003","role":"source_variant","statement":"Besleyici kaynağı kesilmediği için akışı veya varlığı sürekli kalan su."}],"identity_rationale":"Kaynak ifadesi doğal su birikimini ve özellikle eski, besleyici kaynağı kesilmeyen, çekmekle tükenmeyen sürekli suyu aynı dalda açıkça tanımlar. Geçici çerçeve hem suyu hem de onun bulunduğu kalıcı su yerini kapsayarak tanıklığa uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"eskiden beri var olan, tükenmeyen sürekli su"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sürekli sular veya kalıcı su yerleri"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"köklü ve eski saygınlık"}],"lexicalization_note":"Tanım kalıcı su çekirdeğini verir; su yerleri ve eski, köklü olma benzetmesi yalnızca tanıklanan biçim ve kalıpların sınırında tutulur.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; kalıcı suyu yapılmış havuz suyundan, doğal göletten ve geçici su çukurundan ayıran üç sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında kalıcılık suyun kesilmeyen beslenmesine bağlıdır; komşuda ise suyun bir yapı içinde tutulması esastır ve yenilenmesi gerekmez.","focus_only":"Doğal, eski veya sürekli beslenen ve çekmekle tükenmeyen suyu gerektirir.","gloss":"sürekli kaynak suyu ve havuz suyu","neighbor_only":"Suyun yapılmış bir havuz, sarnıç veya düzeltilmiş su kabında sabit durmasını kapsar.","neighbor_ref":"root_000109/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da belirli bir yerde duran veya toplanan suyu anlatır."},{"boundary_match":"partial","distinction":"Odak dalını belirleyen kesintisiz kaynak ve tükenmezliktir; komşu dalı belirleyen ise birikintinin biçimi ve bol su içermesidir.","focus_only":"Suyun eskiliğini, sürekliliğini ve çekmekle tükenmemesini öne çıkarır.","gloss":"kalıcı su ve gölet","neighbor_only":"Vadi içindeki bol su birikintisini, göleti veya bataklık benzeri su alanını adlandırır.","neighbor_ref":"root_001292/B003","relation_type":"near_neighbor","shared_zone":"Doğal bir çukurda veya arazide toplanan su iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dalı süreklilik ve tükenmezlik gerektirir; komşu dal geçici olarak su tutan yerle sınırlıdır.","focus_only":"Sürekli beslenen veya eskiden beri tükenmeyen suyu ve yerini bildirir.","gloss":"tükenmeyen su ve geçici su çukuru","neighbor_only":"Suyu yalnızca birkaç gün tutabilen çukur, havuz veya gölet benzeri yeri bildirir.","neighbor_ref":"root_000018/B006","relation_type":"near_neighbor","shared_zone":"İki dalda da suyun bir yerde toplanması ve tutulması söz konusudur."}],"source_phrase_ar":"العد مجتمع الماء وجمعه أعداد (maqayis;ayn)؛ العد من الماء القديم الذي لا ينتزح (jamhara)؛ العد بالكسر الماء الذي له مادة لا تنقطع (sihah)؛ الماء العد الدائم الذي لا انقطاع له (tahdhib)؛ ماء عد (mufradat)","source_summary":"Toplu tanıklık, birikmiş su anlamını eski, tükenmeyen ve sürekli beslenen su özellikleriyle açıklar; süreklilik dalın geçici su birikintilerinden ayrılan temel sınırıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الماء العد ومجتمع الماء والركية القديمة أو الدائمة التي لا ينقطع ماؤها","what_is_not_ar":"ليس ماء السماء ولا ماء الغدران المنقطع ولا العداد الزماني"},"support_links":[]},{"boundary":"Çekirdek belirli zaman ve düzenli geri geliştir; yay ve özel gün kullanımları yalnızca kendi kalıplarında ilişkili anlamlar olarak tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B005","candidate_links":[{"candidate_id":"cand_9a4bdfe69dab05fb7c63","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|IMPF|LEM:Ead~a|ROOT:Edd|1P","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:5:1","qac_word_ref":"19:84:5","surface_ar":"نَعُدُّ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:84:7:1","qac_word_ref":"19:84:7","surface_ar":"عَدًّا"}],"gloss":"belirli zaman ve bilinen aralıklarla geri gelme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin belirlenmiş zamanı, dönemi veya en güçlü evresi."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir olayın bilinen veya sayılı zaman aralıklarında yeniden ortaya çıkması."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Zehirlenme veya sokulma ağrısının belirli aralıklarla yeniden alevlenmesi."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yayın aralıklı titreşimini veya bu titreşimden çıkan sesi adlandırma."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Dağıtım, yoklama veya geçici toplanma için belirlenmiş günü adlandırma."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın zaman ve yineleme çekirdeğini verir; kalıba bağlı yay ve özel gün kullanımlarını genel anlama katmaz.","boundary_detail":"Çekirdek belirli zaman ve düzenli geri geliştir; yay ve özel gün kullanımları yalnızca kendi kalıplarında ilişkili anlamlar olarak tutulmalıdır.","branch_image_ar":"عداد الوقت ومعاودته","concept_gloss":"belirli zaman ve bilinen aralıklarla geri gelme","contextual_glosses":[{"applicability":"Bir olayın veya ağrının bilinen zaman aralıklarında tekrar belirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Zaman aralıklarını ve olayın yeniden ortaya çıkmasını korur."},"facet_ids":["F002","F003"],"text":"belirli aralıklarla yeniden ortaya çıkmak","usage_role":"general"},{"applicability":"Bir kişinin, yönetimin veya başka bir şeyin belirli zamanı ya da en güçlü evresi kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli dönemi ve o dönemin en güçlü evresini korur."},"facet_ids":["F001"],"text":"dönem veya en parlak çağ","usage_role":"contextual"},{"applicability":"Yayın belli aralıklarla titreştirilmesi ya da çıkardığı ses için kullanılan kalıba özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaya özgü tekrarlı titreşim ile ses seçeneklerini korur."},"facet_ids":["F004"],"text":"yayın aralıklı titreşimi veya sesi","usage_role":"contextual"},{"applicability":"Dağıtım, yoklama ya da geçici toplantı için ayrılmış günü anlatan kalıba özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirlenmiş gün ile dağıtım veya toplanma işlevini korur."},"facet_ids":["F005"],"text":"dağıtım veya toplanma günü","usage_role":"contextual"}],"definition":"Bir şeyin belirli zamanı veya dönemi ile belli aralıklarda yeniden ortaya çıkmasıdır. Zehir ağrısının alevlenmesi bunun özel gerçekleşmesiyken yayın sesi ve titreşimi ile dağıtım ya da toplanma günü kalıba bağlı ilişkili kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin belirlenmiş zamanı, dönemi veya en güçlü evresi."},{"facet_id":"F002","role":"core","statement":"Bir olayın bilinen veya sayılı zaman aralıklarında yeniden ortaya çıkması."},{"facet_id":"F003","role":"specialization","statement":"Zehirlenme veya sokulma ağrısının belirli aralıklarla yeniden alevlenmesi."},{"facet_id":"F004","role":"associated_use","statement":"Yayın aralıklı titreşimini veya bu titreşimden çıkan sesi adlandırma."},{"facet_id":"F005","role":"associated_use","statement":"Dağıtım, yoklama veya geçici toplanma için belirlenmiş günü adlandırma."}],"identity_rationale":"Kaynak ifadesi belirli zaman veya dönem ile bilinen aralıklarda geri gelme anlamlarını destekler; zehir ağrısının yeniden alevlenmesi bu çekirdeğin belirgin gerçekleşmesidir. Bununla birlikte yayın sesi veya aralıklı titreşimi ve dağıtım ya da toplanma günü, genel zaman çekirdeğiyle eşitlenmemesi gereken kalıba bağlı ilişkili kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"sokulma ağrısının belirli aralıklarla alevlenmesi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bana belirli zamanlarda yeniden baş göstermek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"zaman, dönem veya en parlak çağ"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yayın tekrarlanan titreşimi veya sesi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ayda bir gerçekleşen buluşma"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"dağıtım, yoklama veya geçici toplanma günü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"belirli aralıklarla gelen akıl bulanıklığı"}],"lexicalization_note":"Tanım zaman ve aralıklı geri geliş çekirdeğini ayırır; yay sesi, aylık buluşma ve özel gün anlamlarını kendi kalıplarının dışına genellemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel aralıklı geri gelişi kısa buluşma aralığından, özel dördüncü dönüşten ve yalnızca uygun zamandan ayıran ilişkiler seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı belirli zamanı ve yeniden ortaya çıkmayı genel olarak kapsar; komşu dal iki buluşmayı ayıran kısa süreye özgüdür.","focus_only":"Belirli dönemi, yinelenen ağrıyı ve kalıba bağlı yay veya özel gün kullanımlarını da kapsar.","gloss":"yinelenme zamanı ve buluşmalar arası süre","neighbor_only":"Özellikle iki buluşma arasında kalan kısa ve tekrarlanan zaman aralığını bildirir.","neighbor_ref":"root_001145/B007","relation_type":"near_synonym","shared_zone":"İki dal da olayların belli aralıklarla gerçekleşmesi ve aradaki zamanın sınırlı olması alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalında aralık bağlama göre değişebilir; komşu dalda ise dördüncü zamana bağlı özel dönüş düzeni belirleyicidir.","focus_only":"Yinelemenin aralığını genel bırakabilir ve dönem, yay sesi veya özel gün kullanımlarına uzanabilir.","gloss":"aralıklı geri geliş ve dördüncü zaman dönüşü","neighbor_only":"Hayvanların sulanması veya ateşli hastalık için her dördüncü zamandaki belirli dönüş düzenini gerektirir.","neighbor_ref":"root_000536/B004","relation_type":"near_neighbor","shared_zone":"Hastalık belirtisinin veya başka bir olayın düzenli zaman aralıklarında geri gelmesi ortak alandır."},{"boundary_match":"partial","distinction":"Odak dalında yineleme önemli bir çekirdektir; komşu dalda olayın zamanı vardır fakat düzenli geri geliş koşulu yoktur.","focus_only":"Belirli aralıklarla yeniden ortaya çıkma ve buna bağlı özel kalıpları kapsar.","gloss":"yinelenen zaman ve uygun an","neighbor_only":"Bir şeyin yalnızca uygun zamanı veya gerçekleşme anını bildirir.","neighbor_ref":"root_000039/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir olayın belirli zamanı veya dönemini gösterebilir."}],"source_phrase_ar":"العداد اهتياج وجع اللديغ (maqayis;ayn;sihah)؛ العداد الشيء الذي يأتيك لوقت (tahdhib)؛ عدان الشيء عهده وزمانه (mufradat)؛ كان ذلك في عدان شبابه (ayn;sihah;tahdhib)؛ عداد القوس أن تنبض بها ساعة بعد ساعة (maqayis)؛ عداد القوس صوتها (sihah;tahdhib)؛ يوم العداد يوم العطاء (maqayis;tahdhib)","source_summary":"Toplu tanıklık, belirli zaman ve belli aralıklarla geri gelme çekirdeğini; ağrının yeniden alevlenmesi, dönemin en güçlü evresi, yayın tekrarlı hareketi veya sesi ve özel bir gün gibi kullanımlarla gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الوقت المعدود المحدد ومعاودة الشيء في أوقات معلومة وما يلحق به من العداد والعدان","what_is_not_ar":"ليس العدد الحسابي وحده ولا العدة الشرعية ولا الماء العد"},"support_links":["sup_a25935cdfd85ffb5f624"]},{"boundary":"Dal sayısal miktardan çok kişiler arasındaki karşılıklı paydaşlık, pay veya denklik ilişkisini bildirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|IMPF|LEM:Ead~a|ROOT:Edd|1P","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:5:1","qac_word_ref":"19:84:5","surface_ar":"نَعُدُّ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:84:7:1","qac_word_ref":"19:84:7","surface_ar":"عَدًّا"}],"gloss":"karşılıklı paydaşlık, pay ve denk sayılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişilerin sayılabilir bir mal, değer veya üstünlükte karşılıklı paydaş olması."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ortaklıktan doğan payları veya özellikle mirasta karşılıklı paydaşları adlandırma."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişiyi başka bir kişinin karşılığı, eşi veya dengi sayma."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Paylaşılan değer üzerindeki ortaklığı, ortaya çıkan payı ve kişiler arasında kurulan denkliği birlikte karşılar.","boundary_detail":"Dal sayısal miktardan çok kişiler arasındaki karşılıklı paydaşlık, pay veya denklik ilişkisini bildirir.","branch_image_ar":"نظير يعد مع غيره","concept_gloss":"karşılıklı paydaşlık, pay ve denk sayılma","contextual_glosses":[{"applicability":"Kişilerin mal, değer veya üstünlük bakımından birbirine karşı pay sahibi olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Katılımcılar arasındaki karşılıklı ortaklık ve pay ilişkisini korur."},"facet_ids":["F001"],"text":"karşılıklı paydaş olmak","usage_role":"general"},{"applicability":"Ortaklıktaki bölüşüm payları ya da özellikle mirasta birbirine karşı pay sahibi kişiler kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bölüşülen payı ve pay sahipleri arasındaki karşılıklılığı korur."},"facet_ids":["F002"],"text":"paylar veya karşılıklı paydaşlar","usage_role":"contextual"},{"applicability":"Bir kişinin başka biriyle eş düzeyde veya ona karşılık sayıldığı kalıba özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki kişi arasında kurulan denklik ve karşılıklılık ilişkisini korur."},"facet_ids":["F003"],"text":"onun dengi ve karşılığı","usage_role":"contextual"}],"definition":"Birden çok kişinin sayılabilir bir mal, değer veya üstünlük bakımından karşılıklı paydaş olması; bundan doğan payların ya da birbirine karşılık ve denk sayılan kişilerin adlandırılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişilerin sayılabilir bir mal, değer veya üstünlükte karşılıklı paydaş olması."},{"facet_id":"F002","role":"extension","statement":"Ortaklıktan doğan payları veya özellikle mirasta karşılıklı paydaşları adlandırma."},{"facet_id":"F003","role":"extension","statement":"Bir kişiyi başka bir kişinin karşılığı, eşi veya dengi sayma."}],"identity_rationale":"Kaynak ifadesi karşılıklı olarak sayılabilen mal veya değerlerde ortaklığı, bundan doğan payları ve bir kişinin başka biriyle denk ya da karşılık sayılmasını birlikte verir. Geçici çerçeve, sayma fikrinin bu dalda yalın miktar belirleme değil katılımcılar arasındaki pay ve karşılıklılık ilişkisini kurduğunu doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"mal veya değer bakımından karşılıklı paydaş olmak"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"paylar, denkler veya mirastaki karşılıklı paydaşlar"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"onun dengi ve karşılığı"}],"lexicalization_note":"Tanım paydaşlık, pay ve denk sayılma yüzlerini ayırır; belirli kişi karşılaştırmasını veya miras bağlamını çıplak bir genel sayma anlamına dönüştürmez.","neighbor_coverage_note":"Tüm komşu adayları değerlendirildi; genel paydaşlık ve denkliği salt benzerlikten, genel saymadan ve güç bakımından denk rakipten ayıran üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında denklik, daha geniş karşılıklı pay ve katılım alanının bir yüzüdür; komşu dalın çekirdeği doğrudan benzerlik ve eşdeğerliktir.","focus_only":"Paylaşılan mal veya değerde ortaklığı, payları ve mirastaki karşılıklı paydaşları da kapsar.","gloss":"paydaş ve denk","neighbor_only":"İki şeyi benzerlik bakımından birbirinin tam eşi veya örneği olarak karşı karşıya koyar.","neighbor_ref":"root_001520/B006","relation_type":"near_neighbor","shared_zone":"Bir kişinin başka bir kişinin dengi veya karşılığı sayılması iki dalda örtüşür."},{"boundary_match":"partial","distinction":"Odak dalında sayma katılımcılar arasındaki karşılıklı ilişkiyi düzenler; komşu dalda saymanın kendisi ve sayısal sonuç merkezde bulunur.","focus_only":"Sayılabilir bir değer üzerinde karşılıklı pay, paydaşlık veya denklik ilişkisi kurar.","gloss":"karşılıklı pay ve genel sayma","neighbor_only":"Varlıkları tek tek sayıp miktarını belirler ve bir topluluğa dahil sayar.","neighbor_ref":"root_000989/B001","relation_type":"near_neighbor","shared_zone":"Kişilerin başkalarıyla birlikte değerlendirilip sayılması iki dal arasında bağlantı kurar."},{"boundary_match":"partial","distinction":"Odak dalındaki denklik farklı ilişki ve paylaşım bağlamlarına açıktır; komşu dal dengeyi özellikle yaş ve mücadele gücü ekseninde kurar.","focus_only":"Pay, ortaklık ve genel biçimde bir başkasına denk sayılmayı kapsar.","gloss":"genel denk ve güç bakımından denk","neighbor_only":"Özellikle yaş, yiğitlik, güç veya dayanıklılık bakımından birbirine denk rakibi bildirir.","neighbor_ref":"root_001221/B003","relation_type":"near_neighbor","shared_zone":"Bir kişinin başka bir kişiye denk veya eş sayılması ortak alandır."}],"source_phrase_ar":"هم يتعادون إذا اشتركوا فيما يعدد به بعضهم على بعض (ayn;tahdhib)؛ العدائد النظراء (tahdhib)؛ العدائد الحصص (tahdhib)؛ من يعاده في الميراث (sihah)؛ فلان عد فلان أي قرنه (tahdhib)","source_summary":"Toplu tanıklık, karşılıklı paydaş olmayı; pay, mirastaki paydaş ve iki kişi arasında kurulan denklik ya da karşılıklılık kullanımlarıyla aynı ilişki alanında birleştirir.","sources":["AY","SI","TA"],"what_is_ar":"المشاركة والمقارنة والحصة أو النظير حين يعد الشيء مع غيره أو يقابل به","what_is_not_ar":"ليس مجرد كثرة العدد ولا الاستعداد ولا العداد الزماني"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["19:84:1"],"branch_refs":[],"candidate_id":"cand_7630833594e7889570f3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:84:1:consequential-prohibition-link","source_type":"word_analysis","support_ids":["sup_5b8ec22beaa0ebdc670a","sup_cf5a103066233fa864b8"],"title":"consequential prohibition link","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:1","qac_refs":["19:84:1:1"],"status":"accepted"}},{"anchor_refs":["19:84:2"],"branch_refs":[],"candidate_id":"cand_b09c3f1e0d77935ceabb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:84:2:prohibitive-jussive-scope","source_type":"word_analysis","support_ids":["sup_297720c9346df4e4884f","sup_65fd1b0a7786113bc9e1"],"title":"prohibitive jussive scope","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:2","qac_refs":["19:84:1:2"],"status":"accepted"}},{"anchor_refs":["19:84:3"],"branch_refs":[],"candidate_id":"cand_881097eb3e2882097427","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000987"],"scope":"focus_ayah","source_local_id":"19:84:3:against-them-direction","source_type":"word_analysis","support_ids":["sup_273d5c38b20f18abcb12","sup_e667e17ede0932be8771"],"title":"against-them direction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:3","qac_refs":["19:84:2:1"],"status":"accepted"}},{"anchor_refs":["19:84:3"],"branch_refs":[],"candidate_id":"cand_d19d73bb521576ad7e07","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000987"],"scope":"focus_ayah","source_local_id":"19:84:3:halted-sound-boundary","source_type":"word_analysis","support_ids":["sup_273d5c38b20f18abcb12","sup_6b9eea453bdef156f11c"],"title":"halted sound boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:3","qac_refs":["19:84:2:1"],"status":"accepted"}},{"anchor_refs":["19:84:3"],"branch_refs":[],"candidate_id":"cand_be100953b81498005a55","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000987"],"scope":"focus_ayah","source_local_id":"19:84:3:haste-counting-correction","source_type":"word_analysis","support_ids":["sup_273d5c38b20f18abcb12","sup_b80b727c7a71579c303a"],"title":"haste-counting correction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:3","qac_refs":["19:84:2:1"],"status":"accepted"}},{"anchor_refs":["19:84:3"],"branch_refs":[],"candidate_id":"cand_bc6e4c82f82e22f4c951","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000987"],"scope":"focus_ayah","source_local_id":"19:84:3:jussive-direct-restraint","source_type":"word_analysis","support_ids":["sup_273d5c38b20f18abcb12","sup_8b150b750251caead017"],"title":"visible direct restraint","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:3","qac_refs":["19:84:2:1"],"status":"accepted"}},{"anchor_refs":["19:84:3"],"branch_refs":[],"candidate_id":"cand_da64e98c73a3c82b5c4b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000987"],"scope":"focus_ayah","source_local_id":"19:84:3:premature-pressure-root","source_type":"word_analysis","support_ids":["sup_273d5c38b20f18abcb12","sup_b603f5a732e860926196"],"title":"premature pressure root","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:3","qac_refs":["19:84:2:1"],"status":"accepted"}},{"anchor_refs":["19:84:4"],"branch_refs":[],"candidate_id":"cand_01ccafae93e6f921733e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:84:4:continuing-plural-referent","source_type":"word_analysis","support_ids":["sup_33bcb7a93bb70034c604","sup_ec9708788dabdbffc9ed"],"title":"continuing plural referent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:4","qac_refs":["19:84:3:1","19:84:3:2"],"status":"accepted"}},{"anchor_refs":["19:84:4"],"branch_refs":[],"candidate_id":"cand_0c2ce9f938df17f4438f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:84:4:oblique-adversarial-target","source_type":"word_analysis","support_ids":["sup_06b20a8691467d32acd9","sup_ec9708788dabdbffc9ed"],"title":"oblique adversarial target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:4","qac_refs":["19:84:3:1","19:84:3:2"],"status":"accepted"}},{"anchor_refs":["19:84:4"],"branch_refs":[],"candidate_id":"cand_e507e69adbec8b37c621","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:84:4:preposition-contrast-with-lahum","source_type":"word_analysis","support_ids":["sup_ba3a8005aeaf98f12d77","sup_ec9708788dabdbffc9ed"],"title":"preposition contrast with {{tr:lahum}}","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:4","qac_refs":["19:84:3:1","19:84:3:2"],"status":"accepted"}},{"anchor_refs":["19:84:5"],"branch_refs":[],"candidate_id":"cand_d9c48bc8ac7244f0a443","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:84:5:exclusive-divine-counting","source_type":"word_analysis","support_ids":["sup_4740f1f9732f9b3d7133","sup_7d33e6c030f802713536"],"title":"exclusive divine counting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:5","qac_refs":["19:84:4:1","19:84:4:2"],"status":"accepted"}},{"anchor_refs":["19:84:5"],"branch_refs":[],"candidate_id":"cand_2962e430ffc3b22dbf78","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:84:5:kaffa-makfufa-restriction","source_type":"word_analysis","support_ids":["sup_2010d226fceafa937337","sup_7d33e6c030f802713536"],"title":"fused restrictive particle","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:5","qac_refs":["19:84:4:1","19:84:4:2"],"status":"accepted"}},{"anchor_refs":["19:84:6"],"branch_refs":[],"candidate_id":"cand_c18989ec08f00b645505","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:84:6:account-assigned-to-them","source_type":"word_analysis","support_ids":["sup_46067507c6bcac0f18b0","sup_7084f49895f0d797ee56"],"title":"account assigned to them","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:6","qac_refs":["19:84:5:1"],"status":"accepted"}},{"anchor_refs":["19:84:6"],"branch_refs":[],"candidate_id":"cand_c645eff33b477f2ec348","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:84:6:cognate-and-sound-convergence","source_type":"word_analysis","support_ids":["sup_7084f49895f0d797ee56","sup_b984e1e90775ea63fc7a"],"title":"cognate and sound convergence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:6","qac_refs":["19:84:5:1"],"status":"accepted"}},{"anchor_refs":["19:84:6"],"branch_refs":[],"candidate_id":"cand_c50886c5e5cfe0c5030e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:84:6:haste-counting-and-surah-accounting","source_type":"word_analysis","support_ids":["sup_7084f49895f0d797ee56","sup_a3e84ada136cd2bc85ab"],"title":"haste-counting and surah accounting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:6","qac_refs":["19:84:5:1"],"status":"accepted"}},{"anchor_refs":["19:84:6"],"branch_refs":[],"candidate_id":"cand_f90d84e4c64aaf837c58","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:84:6:live-tally-with-hidden-object","source_type":"word_analysis","support_ids":["sup_5631458d6f2b04192b84","sup_7084f49895f0d797ee56"],"title":"live tally with hidden object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:6","qac_refs":["19:84:5:1"],"status":"accepted"}},{"anchor_refs":["19:84:6"],"branch_refs":[],"candidate_id":"cand_24dff663c1369aace093","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:84:6:restricted-divine-imperfect","source_type":"word_analysis","support_ids":["sup_4039281d0fd22d39da46","sup_7084f49895f0d797ee56"],"title":"restricted divine imperfect","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:6","qac_refs":["19:84:5:1"],"status":"accepted"}},{"anchor_refs":["19:84:7"],"branch_refs":[],"candidate_id":"cand_b1e3c25579bc6c0fa4d7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:84:7:dative-account-holder","source_type":"word_analysis","support_ids":["sup_0fb35948b9ca149e3035","sup_374467812e8024a124c8"],"title":"dative account-holder","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:7","qac_refs":["19:84:6:1"],"status":"accepted"}},{"anchor_refs":["19:84:7"],"branch_refs":[],"candidate_id":"cand_51fbc55984f188b16660","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:84:7:prepositional-relation-shift","source_type":"word_analysis","support_ids":["sup_374467812e8024a124c8","sup_a5c4640486bd39c6129e"],"title":"prepositional relation shift","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:7","qac_refs":["19:84:6:1"],"status":"accepted"}},{"anchor_refs":["19:84:8"],"branch_refs":[],"candidate_id":"cand_19e83287de3490b701f4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:84:8:bound-prepositional-complement","source_type":"word_analysis","support_ids":["sup_3288869c07a0a0dce6f5","sup_f0cb5d8f586139e3ddfe"],"title":"bound prepositional complement","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:8","qac_refs":["19:84:6:2"],"status":"accepted"}},{"anchor_refs":["19:84:8"],"branch_refs":[],"candidate_id":"cand_71b0cd4eeee838834f91","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:84:8:persistent-known-referent","source_type":"word_analysis","support_ids":["sup_3288869c07a0a0dce6f5","sup_ed2ea8f66e6db21c4a23"],"title":"persistent known referent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:8","qac_refs":["19:84:6:2"],"status":"accepted"}},{"anchor_refs":["19:84:9"],"branch_refs":[],"candidate_id":"cand_afb8544fde8be005ed45","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:84:9:closure-weighted-count","source_type":"word_analysis","support_ids":["sup_409c5810e37868486665","sup_567f10198694ca34f456"],"title":"closure-weighted count","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:9","qac_refs":["19:84:7:1"],"status":"accepted"}},{"anchor_refs":["19:84:9"],"branch_refs":[],"candidate_id":"cand_924d20fc5124a72485c4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:84:9:cognate-process-intensifier","source_type":"word_analysis","support_ids":["sup_567f10198694ca34f456","sup_867a04f63c2b813bea5b"],"title":"cognate process intensifier","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:9","qac_refs":["19:84:7:1"],"status":"accepted"}},{"anchor_refs":["19:84:9"],"branch_refs":[],"candidate_id":"cand_144ea9a02e38fd0b3cb0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:84:9:finite-accounting-root-field","source_type":"word_analysis","support_ids":["sup_567f10198694ca34f456","sup_f0db64b634e921ec2b7e"],"title":"finite accounting root field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:9","qac_refs":["19:84:7:1"],"status":"accepted"}},{"anchor_refs":["19:84:9"],"branch_refs":[],"candidate_id":"cand_355c7134d499a66dc5cd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:84:9:indefinite-undisclosed-count","source_type":"word_analysis","support_ids":["sup_567f10198694ca34f456","sup_ddd505cf021b972b2b8e"],"title":"indefinite undisclosed count","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:9","qac_refs":["19:84:7:1"],"status":"accepted"}},{"anchor_refs":["19:84:9"],"branch_refs":[],"candidate_id":"cand_0c1a412dab65fb478f66","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:84:9:root-echo-and-audible-tally","source_type":"word_analysis","support_ids":["sup_567f10198694ca34f456","sup_c9a71a2e651df5b372cd"],"title":"root echo and audible tally","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:84:9","qac_refs":["19:84:7:1"],"status":"accepted"}},{"anchor_refs":["19:84:2"],"branch_refs":[],"candidate_id":"cand_77333dbb4abde8f141c8","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000987"],"scope":"focus_ayah","source_local_id":"19:84:2:1","source_type":"qac_morpheme","support_ids":["sup_f23543f312749928eedc"],"title":"QAC root occurrence: ع ج ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["19:84:5"],"branch_refs":[],"candidate_id":"cand_ced014b3e5b463513b47","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:84:5:1","source_type":"qac_morpheme","support_ids":["sup_f7ff4d0c5fe6f79111e1"],"title":"QAC root occurrence: ع د د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["19:84"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:84","branch_refs":["root_000987/B001","root_000989/B001"],"candidate_id":"cand_e8951a749458e7274089","commentary_obligation":"review","hft_ref":"hft_b983c4761a3dfb9df5af","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:B84_measured_deferral","source_type":"hft","support_ids":["sup_67b0aea7184f667db74d"],"title":"B84_measured_deferral","trust":"legacy_unbound"},{"anchor_refs":["19:84"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:84","branch_refs":["root_000987/B001","root_000989/B003","root_000989/B005"],"candidate_id":"cand_9a4bdfe69dab05fb7c63","commentary_obligation":"review","hft_ref":"hft_409145fe521b5193c901","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:B84_counted_interval","source_type":"hft","support_ids":["sup_a25935cdfd85ffb5f624"],"title":"B84_counted_interval","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَلَا تَعْجَلْ عَلَيْهِمْ ۖ إِنَّمَا نَعُدُّ لَهُمْ عَدًّۭا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"19:84:1:1","qac_word_ref":"19:84:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:PRO|LEM:laA","morpheme_role":"STEM","pos":"PRO","qac_ref":"19:84:1:2","qac_word_ref":"19:84:1","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"عَجِلَ","morph_features":"STEM|POS:V|IMPF|LEM:Eajila|ROOT:Ejl|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:2:1","qac_word_ref":"19:84:2","root_ar":"ع ج ل","surface_ar":"تَعْجَلْ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"19:84:3:1","qac_word_ref":"19:84:3","root_ar":"","surface_ar":"عَلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"19:84:3:2","qac_word_ref":"19:84:3","root_ar":"","surface_ar":"هِمْ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"19:84:4:1","qac_word_ref":"19:84:4","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:PREV|LEM:maA","morpheme_role":"STEM","pos":"PREV","qac_ref":"19:84:4:2","qac_word_ref":"19:84:4","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|IMPF|LEM:Ead~a|ROOT:Edd|1P","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:5:1","qac_word_ref":"19:84:5","root_ar":"ع د د","surface_ar":"نَعُدُّ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"19:84:6:1","qac_word_ref":"19:84:6","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MP","morpheme_role":"STEM","pos":"PRON","qac_ref":"19:84:6:2","qac_word_ref":"19:84:6","root_ar":"","surface_ar":"هُمْ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:84:7:1","qac_word_ref":"19:84:7","root_ar":"ع د د","surface_ar":"عَدًّا"}],"word_analysis_qac_refs":[["19:84:1:1"],["19:84:1:2"],["19:84:2:1"],["19:84:3:1","19:84:3:2"],["19:84:4:1","19:84:4:2"],["19:84:5:1"],["19:84:6:1"],["19:84:6:2"],["19:84:7:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["19:84:1","19:84:2","19:84:3","19:84:4","19:84:5","19:84:6","19:84:7","19:84:8","19:84:9"]},"focus_surface_evidence":{"arabic_uthmani":"فَلَا تَعْجَلْ عَلَيْهِمْ ۖ إِنَّمَا نَعُدُّ لَهُمْ عَدًّۭا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"19:84:1:1","qac_word_ref":"19:84:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:PRO|LEM:laA","morpheme_role":"STEM","pos":"PRO","qac_ref":"19:84:1:2","qac_word_ref":"19:84:1","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"عَجِلَ","morph_features":"STEM|POS:V|IMPF|LEM:Eajila|ROOT:Ejl|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:2:1","qac_word_ref":"19:84:2","root_ar":"ع ج ل","surface_ar":"تَعْجَلْ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"19:84:3:1","qac_word_ref":"19:84:3","root_ar":"","surface_ar":"عَلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"19:84:3:2","qac_word_ref":"19:84:3","root_ar":"","surface_ar":"هِمْ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"19:84:4:1","qac_word_ref":"19:84:4","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:PREV|LEM:maA","morpheme_role":"STEM","pos":"PREV","qac_ref":"19:84:4:2","qac_word_ref":"19:84:4","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|IMPF|LEM:Ead~a|ROOT:Edd|1P","morpheme_role":"STEM","pos":"V","qac_ref":"19:84:5:1","qac_word_ref":"19:84:5","root_ar":"ع د د","surface_ar":"نَعُدُّ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"19:84:6:1","qac_word_ref":"19:84:6","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MP","morpheme_role":"STEM","pos":"PRON","qac_ref":"19:84:6:2","qac_word_ref":"19:84:6","root_ar":"","surface_ar":"هُمْ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:84:7:1","qac_word_ref":"19:84:7","root_ar":"ع د د","surface_ar":"عَدًّا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["19:84:1:1"],["19:84:1:2"],["19:84:2:1"],["19:84:3:1","19:84:3:2"],["19:84:4:1","19:84:4:2"],["19:84:5:1"],["19:84:6:1"],["19:84:6:2"],["19:84:7:1"]],"word_analysis_refs":["19:84:1","19:84:2","19:84:3","19:84:4","19:84:5","19:84:6","19:84:7","19:84:8","19:84:9"],"word_rows":[{"analysis_record_ref":"19:84:1","analytic_gloss_range_en":"consequential conjunction that carries the prior ayah into the prohibition clause","analytic_root_gloss_range_en":null,"qac_refs":["19:84:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"19:84:2","analytic_gloss_range_en":"prohibitive negation governing a jussive verb, with scope limited to the first clause","analytic_root_gloss_range_en":null,"qac_refs":["19:84:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَا","transliteration":"la"}},{"analysis_record_ref":"19:84:3","analytic_gloss_range_en":"prohibited haste or premature pressure, locally directed through {{ar:عَلَى}} ({{tr:ʿala}}) toward the plural group","analytic_root_gloss_range_en":"haste, immediacy, premature action, and quick movement; local grammar selects restrained premature pressure, not unrelated root branches","qac_refs":["19:84:2:1"],"root":{"arabic":"ع ج ل","transliteration":"ʿ-j-l"},"surface":{"arabic":"تَعْجَلْ","transliteration":"taʿjal"}},{"analysis_record_ref":"19:84:4","analytic_gloss_range_en":"preposition {{ar:عَلَى}} ({{tr:ʿala}}) with third-person plural suffix, marking the target of prohibited pressure","analytic_root_gloss_range_en":null,"qac_refs":["19:84:3:1","19:84:3:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"عَلَيْهِمْ","transliteration":"ʿalayhim"}},{"analysis_record_ref":"19:84:5","analytic_gloss_range_en":"restrictive particle opening the explanatory counting clause","analytic_root_gloss_range_en":null,"qac_refs":["19:84:4:1","19:84:4:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"إِنَّمَا","transliteration":"innama"}},{"analysis_record_ref":"19:84:6","analytic_gloss_range_en":"ongoing divine counting, with the counted item unexpressed and the account assigned by {{ar:لَهُمْ}} ({{tr:lahum}})","analytic_root_gloss_range_en":"counting, enumerating, reckoning, preparing, and timed recurrence; local form selects active enumeration/reckoning in progress","qac_refs":["19:84:5:1"],"root":{"arabic":"ع د د","transliteration":"ʿ-d-d"},"surface":{"arabic":"نَعُدُّ","transliteration":"naʿuddu"}},{"analysis_record_ref":"19:84:7","analytic_gloss_range_en":"preposition forming {{ar:لَهُمْ}} ({{tr:lahum}}), marking the group as the referenced account-holder","analytic_root_gloss_range_en":null,"qac_refs":["19:84:6:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَ","transliteration":"la"}},{"analysis_record_ref":"19:84:8","analytic_gloss_range_en":"third-person plural pronoun governed by {{ar:لَ}} ({{tr:la}}), continuing the known disbelieving group","analytic_root_gloss_range_en":null,"qac_refs":["19:84:6:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"هُمْ","transliteration":"hum"}},{"analysis_record_ref":"19:84:9","analytic_gloss_range_en":"indefinite verbal noun functioning as cognate accusative, intensifying the counting while withholding the counted contents","analytic_root_gloss_range_en":"counting, number, reckoning, preparation, counted time, and recurrence; local form selects the counting process as a cognate verbal noun","qac_refs":["19:84:7:1"],"root":{"arabic":"ع د د","transliteration":"ʿ-d-d"},"surface":{"arabic":"عَدًّا","transliteration":"ʿadda"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":9,"words_total":9,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":2,"assigned_records":[{"anchor_refs":["19:84"],"branch_refs":["root_000987/B001","root_000989/B001"],"candidate_id":"cand_e8951a749458e7274089","evidence_scope":"focus_ayah","hft_ref":"hft_b983c4761a3dfb9df5af","item_id":"B84_measured_deferral","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:B84_measured_deferral","support_id":"sup_67b0aea7184f667db74d"},{"anchor_refs":["19:84"],"branch_refs":["root_000987/B001","root_000989/B003","root_000989/B005"],"candidate_id":"cand_9a4bdfe69dab05fb7c63","evidence_scope":"focus_ayah","hft_ref":"hft_409145fe521b5193c901","item_id":"B84_counted_interval","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:B84_counted_interval","support_id":"sup_a25935cdfd85ffb5f624"}],"diagnostics":[],"lane_counts":{"global":7,"macro":5,"micro":2},"packet_summary":{"ayah_count":22,"focus_ref":"19:84","protocol":"focus-trace-pericope-lean-v1","split_root_mappings":[],"window":["19:77","19:78","19:79","19:80","19:81","19:82","19:83","19:84","19:85","19:86","19:87","19:88","19:89","19:90","19:91","19:92","19:93","19:94","19:95","19:96","19:97","19:98"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"valid_pericope_packet_unbound_response"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"19:84","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":7,"unstructured_record_count":0},"identity":{"ayah_ref":"19:84","lane":"micro","linguistic_source_ref":"19:84","surface_ref":"19:84","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"19:84","target_tokens":[["Onlar",["19:84:1"]],["hakkında",["19:84:1","19:84:2"]],["acele",["19:84:2","19:84:3"]],["etme",["19:84:3"]],["Biz",["19:84:3","19:84:4"]],["onlar",["19:84:4","19:84:5"]],["için",["19:84:5"]],["yalnızca",["19:84:5","19:84:6"]],["sayıp",["19:84:6","19:84:7"]],["duruyoruz",["19:84:7"]]],"text":"Onlar hakkında acele etme. Biz onlar için yalnızca sayıp duruyoruz."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":2,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":77,"ayah_to":98,"id":"s019-p05-077-098","label":"Boastful deniers and divine inheritance","number":5,"refs":["19:77","19:78","19:79","19:80","19:81","19:82","19:83","19:84","19:85","19:86","19:87","19:88","19:89","19:90","19:91","19:92","19:93","19:94","19:95","19:96","19:97","19:98"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:4:oblique-adversarial-target","source_type":"word_analysis","support_id":"sup_06b20a8691467d32acd9","text":"{\"blocking_evidence\":null,\"headline\":\"oblique adversarial target\",\"reader_payoff\":\"The reader notices that the prohibited haste is directed against the group through a preposition, not imposed as a direct verbal object or duty toward them.\",\"reason\":\"The attachment marks {{ar:عَلَيْهِمْ}} ({{tr:ʿalayhim}}) as the prepositional complement of {{ar:تَعْجَلْ}} ({{tr:taʿjal}}), narrowing broader {{ar:عَلَى}} ({{tr:ʿala}}) possibilities to adversarial direction here.\",\"representative_source_ids\":[\"QG-c803ef3c\",\"QG-e130f9be\",\"MG-b7141410\",\"MS-0d7dc4a6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:7:dative-account-holder","source_type":"word_analysis","support_id":"sup_0fb35948b9ca149e3035","text":"{\"blocking_evidence\":null,\"headline\":\"dative account-holder\",\"reader_payoff\":\"The reader notices that the group is indexed as the holder of the account before the final counting noun lands.\",\"reason\":\"Attachment evidence makes {{ar:هُمْ}} ({{tr:hum}}) governed by {{ar:لَ}} ({{tr:la}}) and the resulting phrase a complement of {{ar:نَعُدُّ}} ({{tr:naʿuddu}}).\",\"representative_source_ids\":[\"QG-8462c1a7\",\"MG-d723733a\",\"QF-fd888ca9\",\"QT-70706f2f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:5:kaffa-makfufa-restriction","source_type":"word_analysis","support_id":"sup_2010d226fceafa937337","text":"{\"blocking_evidence\":null,\"headline\":\"fused restrictive particle\",\"reader_payoff\":\"The reader notices that {{ar:إِنَّمَا}} ({{tr:innama}}) creates restriction while leaving the following counting verb as a verbal clause.\",\"reason\":\"QAC identifies the particle as {{tr:kaffa-makfufa}}, supporting the CRITICAL claim that the fused surface unit restricts rather than governing a following accusative noun.\",\"representative_source_ids\":[\"QG-43491c02\",\"MG-bb24fa62\",\"QF-5202d7a6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:3","source_type":"word_analysis","support_id":"sup_273d5c38b20f18abcb12","text":"{\"gloss_range\":\"prohibited haste or premature pressure, locally directed through {{ar:عَلَى}} ({{tr:ʿala}}) toward the plural group\",\"prose\":\"{{ar:تَعْجَلْ}} ({{tr:taʿjal}}) is visibly jussive after the prohibition, and its second-person singular form keeps one addressee distinct from the plural target. The root makes the blocked act a premature push, while the following {{ar:عَلَيْهِمْ}} ({{tr:ʿalayhim}}) directs that impatience against them. The tight consonantal rush of {{ar:تَعْجَلْ}} ({{tr:taʿjal}}) is stopped by {{ar:لَا}} ({{tr:la}}) before it reaches that adversarial phrase. The broader haste field is narrowed here: this is not a request that God hasten events, but the addressee's own urgency being halted. That local restraint also meets larger haste scenes, including prophetic restraint at 20:114 and 75:16 and the haste-counting contrast at 22:47.\",\"root_display\":\"{{ar:ع ج ل}} ({{tr:ʿ-j-l}})\",\"root_gloss_range\":\"haste, immediacy, premature action, and quick movement; local grammar selects restrained premature pressure, not unrelated root branches\",\"surface_display\":\"{{ar:تَعْجَلْ}} ({{tr:taʿjal}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:2","source_type":"word_analysis","support_id":"sup_297720c9346df4e4884f","text":"{\"gloss_range\":\"prohibitive negation governing a jussive verb, with scope limited to the first clause\",\"prose\":\"{{ar:لَا}} ({{tr:la}}) is the prohibitive particle, so the clause commands non-hastening rather than reporting that haste does not occur. Its force stops at {{ar:تَعْجَلْ}} ({{tr:taʿjal}}); the later {{ar:إِنَّمَا نَعُدُّ}} ({{tr:innama naʿuddu}}) remains an affirmative restricted explanation for the command.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَا}} ({{tr:la}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:8","source_type":"word_analysis","support_id":"sup_3288869c07a0a0dce6f5","text":"{\"gloss_range\":\"third-person plural pronoun governed by {{ar:لَ}} ({{tr:la}}), continuing the known disbelieving group\",\"prose\":\"{{ar:هُمْ}} ({{tr:hum}}) supplies the same plural group inside {{ar:لَهُمْ}} ({{tr:lahum}}). It is not an independent subject; it is the prepositional complement that makes the count belong to a known referent carried over from 19:83. The repeated pronoun lets the ayah contrast two relations to the same group: pressure upon them is forbidden, but accounting for them proceeds.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:هُمْ}} ({{tr:hum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:4:continuing-plural-referent","source_type":"word_analysis","support_id":"sup_33bcb7a93bb70034c604","text":"{\"blocking_evidence\":null,\"headline\":\"continuing plural referent\",\"reader_payoff\":\"The reader notices that the pronoun does not introduce a new target; it carries forward the group named in 19:83.\",\"reason\":\"Attachment cross-reference evidence resolves the suffixes in {{ar:عَلَيْهِمْ}} ({{tr:ʿalayhim}}) and {{ar:لَهُمْ}} ({{tr:lahum}}) back to the disbelievers just mentioned.\",\"representative_source_ids\":[\"QG-ab566827\",\"MG-e1e3df7a\",\"QB-e54dc27f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:7","source_type":"word_analysis","support_id":"sup_374467812e8024a124c8","text":"{\"gloss_range\":\"preposition forming {{ar:لَهُمْ}} ({{tr:lahum}}), marking the group as the referenced account-holder\",\"prose\":\"{{ar:لَ}} ({{tr:la}}) is the preposition that makes the tally theirs without making them the direct object counted. It forms {{ar:لَهُمْ}} ({{tr:lahum}}), placing the account-holder between the counting verb and the final cognate noun. The form can sound like for-them reference, but context makes the assigned account ominous rather than beneficial.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَ}} ({{tr:la}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:6:restricted-divine-imperfect","source_type":"word_analysis","support_id":"sup_4039281d0fd22d39da46","text":"{\"blocking_evidence\":null,\"headline\":\"restricted divine imperfect\",\"reader_payoff\":\"The reader notices that divine counting is presented as an ongoing first-person act, contrasted with the addressee's jussive restraint.\",\"reason\":\"QAC marks {{ar:نَعُدُّ}} ({{tr:naʿuddu}}) as a first-person plural imperfect indicative, and the preceding restrictive particle makes that implicit subject the restricted counting agent.\",\"representative_source_ids\":[\"QG-217fa3f0\",\"QG-f1533be4\",\"MG-434f3947\",\"QF-83480230\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:9:closure-weighted-count","source_type":"word_analysis","support_id":"sup_409c5810e37868486665","text":"{\"blocking_evidence\":null,\"headline\":\"closure-weighted count\",\"reader_payoff\":\"The reader notices that the ayah lands on counting itself, after identifying the account-holder first.\",\"reason\":\"The word is final and follows {{ar:لَهُمْ}} ({{tr:lahum}}), so the CRITICAL closure and delayed-intensification rows are supported by local order.\",\"representative_source_ids\":[\"QI-51f58dd6\",\"QT-6ddf147f\",\"QT-f3ff69fc\",\"QY-99497243\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:6:account-assigned-to-them","source_type":"word_analysis","support_id":"sup_46067507c6bcac0f18b0","text":"{\"blocking_evidence\":null,\"headline\":\"account assigned to them\",\"reader_payoff\":\"The reader notices that the group is not the direct object but the account-holder to whom the tally is assigned.\",\"reason\":\"{{ar:لَهُمْ}} ({{tr:lahum}}) is attached as a prepositional complement of {{ar:نَعُدُّ}} ({{tr:naʿuddu}}), so the benefactive/adverse tension survives as dative reference rather than a direct counted object.\",\"representative_source_ids\":[\"QS-3783353b\",\"MS-ac4ac9b2\",\"QT-28d3cf64\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:5:exclusive-divine-counting","source_type":"word_analysis","support_id":"sup_4740f1f9732f9b3d7133","text":"{\"blocking_evidence\":null,\"headline\":\"exclusive divine counting\",\"reader_payoff\":\"The reader notices that the reason for restraint is not delay or neglect, but restricted divine agency already engaged in counting.\",\"reason\":\"The second clause is explicitly linked as the explanation for the first, and {{ar:إِنَّمَا}} ({{tr:innama}}) scopes over {{ar:نَعُدُّ}} ({{tr:naʿuddu}}), so the agency-and-justification rows are locally licensed.\",\"representative_source_ids\":[\"QG-fd53ae74\",\"QS-b03b1df0\",\"MS-a9384506\",\"QI-b4e11827\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:6:live-tally-with-hidden-object","source_type":"word_analysis","support_id":"sup_5631458d6f2b04192b84","text":"{\"blocking_evidence\":null,\"headline\":\"live tally with hidden object\",\"reader_payoff\":\"The reader notices that the ayah asserts the reality of counting while withholding what exactly is being counted.\",\"reason\":\"The attachment frame marks no expressed counted object for the verb while the cognate accusative appears later, so transitivity claims must be narrowed to an absolute counting process intensified by {{ar:عَدًّا}} ({{tr:ʿadda}}).\",\"representative_source_ids\":[\"QG-d69554fa\",\"MG-2836b83e\",\"QS-86bc737a\",\"QS-ac479b22\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:9","source_type":"word_analysis","support_id":"sup_567f10198694ca34f456","text":"{\"gloss_range\":\"indefinite verbal noun functioning as cognate accusative, intensifying the counting while withholding the counted contents\",\"prose\":\"{{ar:عَدًّا}} ({{tr:ʿadda}}) closes the ayah with the noun of counting. As an indefinite cognate accusative of {{ar:نَعُدُّ}} ({{tr:naʿuddu}}), it confirms and intensifies the act without revealing the counted contents or final total. The maṣdar form selects process rather than a finished number, while the same-root echo and doubled sound make the close feel like tallying in motion. The broader root can include prepared provision and counted time, but here those branches are narrowed to an active reckoning whose finitude is echoed by counted-days references such as 2:184 and 3:24 and by the return of counting in 19:94.\",\"root_display\":\"{{ar:ع د د}} ({{tr:ʿ-d-d}})\",\"root_gloss_range\":\"counting, number, reckoning, preparation, counted time, and recurrence; local form selects the counting process as a cognate verbal noun\",\"surface_display\":\"{{ar:عَدًّا}} ({{tr:ʿadda}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:1:consequential-prohibition-link","source_type":"word_analysis","support_id":"sup_5b8ec22beaa0ebdc670a","text":"{\"blocking_evidence\":null,\"headline\":\"consequential prohibition link\",\"reader_payoff\":\"The reader notices that the command not to hasten is the immediate consequence of the prior scene in 19:83, not a free-standing moral maxim.\",\"reason\":\"QAC marks {{ar:فَ}} ({{tr:fa}}) as a conjunction introducing a consequential clause, and attachment evidence makes words 1-4 the prohibitive verbal clause linked to the following explanation.\",\"representative_source_ids\":[\"QG-27abe4f1\",\"QG-fd8346da\",\"MG-831e7a45\",\"QT-f4f51c2c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:2:prohibitive-jussive-scope","source_type":"word_analysis","support_id":"sup_65fd1b0a7786113bc9e1","text":"{\"blocking_evidence\":null,\"headline\":\"prohibitive jussive scope\",\"reader_payoff\":\"The reader notices a direct restraint command whose negation governs only the haste clause while the counting clause stays positively asserted.\",\"reason\":\"QAC identifies {{ar:لَا}} ({{tr:la}}) as a jussive negation particle, and attachment evidence defines words 1-4 as the prohibitive clause with words 5-9 as its explanation.\",\"representative_source_ids\":[\"QG-4a13edca\",\"QG-6faa8535\",\"MG-967254ba\",\"QT-5f34e19a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:3:halted-sound-boundary","source_type":"word_analysis","support_id":"sup_6b9eea453bdef156f11c","text":"{\"blocking_evidence\":null,\"headline\":\"halted sound boundary\",\"reader_payoff\":\"The reader hears the quick consonantal pressure of {{ar:تَعْجَلْ}} ({{tr:taʿjal}}) being stopped by the prohibition before it reaches the group.\",\"reason\":\"The sound-texture rows are locally tied to the surface form and to the boundary from 19:83 into the prohibition, so they can remain as a secondary payoff.\",\"representative_source_ids\":[\"MS-59612192\",\"QP-1262983c\",\"QB-b2381b2c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:6","source_type":"word_analysis","support_id":"sup_7084f49895f0d797ee56","text":"{\"gloss_range\":\"ongoing divine counting, with the counted item unexpressed and the account assigned by {{ar:لَهُمْ}} ({{tr:lahum}})\",\"prose\":\"{{ar:نَعُدُّ}} ({{tr:naʿuddu}}) shifts the ayah from what the addressee must not do to what the divine speaker is already doing. The first-person plural imperfect makes the count ongoing and restricted by {{ar:إِنَّمَا}} ({{tr:innama}}), while the actual counted item remains unspoken. The verb therefore presents a live tally assigned to them through {{ar:لَهُمْ}} ({{tr:lahum}}), not a disclosed final number. Its doubled sound is picked up by the same-root closure {{ar:عَدًّا}} ({{tr:ʿadda}}), making the counting feel compact, repeated, and active. It answers {{ar:تَعْجَلْ}} ({{tr:taʿjal}}) within the ayah and also meets the haste-counting field at 22:47 and the same-surah counting return at 19:94.\",\"root_display\":\"{{ar:ع د د}} ({{tr:ʿ-d-d}})\",\"root_gloss_range\":\"counting, enumerating, reckoning, preparing, and timed recurrence; local form selects active enumeration/reckoning in progress\",\"surface_display\":\"{{ar:نَعُدُّ}} ({{tr:naʿuddu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:5","source_type":"word_analysis","support_id":"sup_7d33e6c030f802713536","text":"{\"gloss_range\":\"restrictive particle opening the explanatory counting clause\",\"prose\":\"{{ar:إِنَّمَا}} ({{tr:innama}}) pivots from the prohibition into a restricted explanation. As a fused restrictive particle, it does not set up an ordinary governed noun after {{ar:إِنَّ}} ({{tr:inna}}); it lets {{ar:نَعُدُّ}} ({{tr:naʿuddu}}) stand as the restricted verbal assertion. The payoff is agency: the addressee must not force the timing because the divine speaker is already the one counting.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِنَّمَا}} ({{tr:innama}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:9:cognate-process-intensifier","source_type":"word_analysis","support_id":"sup_867a04f63c2b813bea5b","text":"{\"blocking_evidence\":null,\"headline\":\"cognate process intensifier\",\"reader_payoff\":\"The reader notices that the final noun is not the hidden thing counted; it is the verb's own noun intensifying the act of enumeration.\",\"reason\":\"Attachment evidence explicitly marks {{ar:عَدًّا}} ({{tr:ʿadda}}) as a same-root cognate accusative of {{ar:نَعُدُّ}} ({{tr:naʿuddu}}), narrowing wider root senses such as regarding or considering to actual enumeration here.\",\"representative_source_ids\":[\"QG-5a9083ac\",\"MG-a5b28f0f\",\"QS-03fa3813\",\"QS-d10752e8\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:3:jussive-direct-restraint","source_type":"word_analysis","support_id":"sup_8b150b750251caead017","text":"{\"blocking_evidence\":null,\"headline\":\"visible direct restraint\",\"reader_payoff\":\"The reader notices that the form itself issues a direct singular command, not a general statement about haste.\",\"reason\":\"QAC tags the word as an imperfect jussive second-person masculine singular verb, and the prohibitive particle before it supplies the command force.\",\"representative_source_ids\":[\"QG-9a3424e7\",\"QG-c37a2310\",\"MG-e6222073\",\"QF-8e815386\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:6:haste-counting-and-surah-accounting","source_type":"word_analysis","support_id":"sup_a3e84ada136cd2bc85ab","text":"{\"blocking_evidence\":null,\"headline\":\"haste-counting and surah accounting\",\"reader_payoff\":\"The reader sees divine enumeration replacing human urgency, with concrete echoes at 22:47 and 19:94.\",\"reason\":\"The CRITICAL inter-ayah rows provide concrete references and are compatible with the local root and clause structure when used as echoes rather than replacements for the local parse.\",\"representative_source_ids\":[\"QI-15fb7c09\",\"QI-3482d52b\",\"QI-b582f2ab\",\"MI-ef0df1b8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:7:prepositional-relation-shift","source_type":"word_analysis","support_id":"sup_a5c4640486bd39c6129e","text":"{\"blocking_evidence\":null,\"headline\":\"prepositional relation shift\",\"reader_payoff\":\"The reader notices the shift from pressure against them to an account assigned to them, with the apparent for-them form carrying adverse force in context.\",\"reason\":\"The contrast with {{ar:عَلَيْهِمْ}} ({{tr:ʿalayhim}}) is syntactically licensed, but the benefactive wording is narrowed by context to dative reference for an ominous tally.\",\"representative_source_ids\":[\"QS-09dc1cf5\",\"QS-81060597\",\"MS-7267b162\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:3:premature-pressure-root","source_type":"word_analysis","support_id":"sup_b603f5a732e860926196","text":"{\"blocking_evidence\":null,\"headline\":\"premature pressure root\",\"reader_payoff\":\"The reader notices that the prohibited haste is premature timing-pressure rather than ordinary speed.\",\"reason\":\"The root field supports haste before its proper time, but local grammar narrows the broader concrete and timing branches to prohibited premature pressure in the ayah.\",\"representative_source_ids\":[\"QS-18b2ba5e\",\"QS-3ae42248\",\"QS-f9fa7f44\",\"MS-afe583d3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:3:haste-counting-correction","source_type":"word_analysis","support_id":"sup_b80b727c7a71579c303a","text":"{\"blocking_evidence\":null,\"headline\":\"haste-counting correction\",\"reader_payoff\":\"The reader notices that the halted haste is answered by divine counting, with 22:47 providing a concrete cross-reference where hastening and counting meet.\",\"reason\":\"The CRITICAL rows give concrete prophetic-restraint and haste-counting references, and no guardrail evidence contradicts using them as parallels rather than as controllers of the local parse.\",\"representative_source_ids\":[\"QI-27c3297e\",\"QI-5c2867a5\",\"QE-d45881d3\",\"ME-7a765042\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:6:cognate-and-sound-convergence","source_type":"word_analysis","support_id":"sup_b984e1e90775ea63fc7a","text":"{\"blocking_evidence\":null,\"headline\":\"cognate and sound convergence\",\"reader_payoff\":\"The reader notices that the doubled sound and same-root closure make the counting feel repeated and active.\",\"reason\":\"The later verbal noun is confirmed as a same-root cognate accusative, so the verb's sound and root repetition can be kept as a local form payoff.\",\"representative_source_ids\":[\"ME-de277057\",\"QP-1da00118\",\"QY-f456cd3a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:4:preposition-contrast-with-lahum","source_type":"word_analysis","support_id":"sup_ba3a8005aeaf98f12d77","text":"{\"blocking_evidence\":null,\"headline\":\"preposition contrast with {{tr:lahum}}\",\"reader_payoff\":\"The reader notices a structural contrast: human pressure is blocked against them, while divine accounting is later marked for them.\",\"reason\":\"Both prepositional phrases are syntactically attached to their verbs, allowing the CRITICAL contrast between {{ar:عَلَيْهِمْ}} ({{tr:ʿalayhim}}) and {{ar:لَهُمْ}} ({{tr:lahum}}) to survive.\",\"representative_source_ids\":[\"QS-472cabf0\",\"QT-6f46ddbd\",\"QB-8713a0ed\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:9:root-echo-and-audible-tally","source_type":"word_analysis","support_id":"sup_c9a71a2e651df5b372cd","text":"{\"blocking_evidence\":null,\"headline\":\"root echo and audible tally\",\"reader_payoff\":\"The reader hears the repeated root and doubled consonant turn the final word into an audible tally.\",\"reason\":\"The verb and final verbal noun share the same root, and the surface form supports the sound-texture rows as local secondary payoff.\",\"representative_source_ids\":[\"QE-5f9bc3f7\",\"QE-d5f2b581\",\"ME-30a6b21d\",\"QP-e420a20b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:1","source_type":"word_analysis","support_id":"sup_cf5a103066233fa864b8","text":"{\"gloss_range\":\"consequential conjunction that carries the prior ayah into the prohibition clause\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) makes the opening prohibition a consequence, not a detached command. It brings the agitation of 19:83 into the new ayah and launches the whole complex {{ar:فَلَا تَعْجَلْ عَلَيْهِمْ}} ({{tr:fa-la taʿjal ʿalayhim}}), so the reader hears the restraint as the commanded response to what has just been disclosed.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:9:indefinite-undisclosed-count","source_type":"word_analysis","support_id":"sup_ddd505cf021b972b2b8e","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite undisclosed count\",\"reader_payoff\":\"The reader notices that the count is real but its total remains undisclosed.\",\"reason\":\"QAC and noun-instance evidence identify the word as an indefinite verbal noun, supporting the unspecified-count payoff.\",\"representative_source_ids\":[\"QG-02cbea19\",\"MG-d1bfcdf1\",\"QF-0b9a437b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:3:against-them-direction","source_type":"word_analysis","support_id":"sup_e667e17ede0932be8771","text":"{\"blocking_evidence\":null,\"headline\":\"against-them direction\",\"reader_payoff\":\"The reader notices that the haste is not merely internal impatience; it is pointed through {{ar:عَلَيْهِمْ}} ({{tr:ʿalayhim}}) toward the same group.\",\"reason\":\"Attachment evidence makes {{ar:عَلَيْهِمْ}} ({{tr:ʿalayhim}}) a prepositional complement of the verb, so mixed transitivity claims survive only as outward pressure through {{ar:عَلَى}} ({{tr:ʿala}}), not as a direct-object construction.\",\"representative_source_ids\":[\"MG-2e81448e\",\"MS-a5ff830c\",\"QT-428e92c9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:4","source_type":"word_analysis","support_id":"sup_ec9708788dabdbffc9ed","text":"{\"gloss_range\":\"preposition {{ar:عَلَى}} ({{tr:ʿala}}) with third-person plural suffix, marking the target of prohibited pressure\",\"prose\":\"{{ar:عَلَيْهِمْ}} ({{tr:ʿalayhim}}) keeps the disbelieving group from 19:83 in view, but it makes them an oblique prepositional target rather than a direct object. The relation is pressure upon or against them; the obligation sense of {{ar:عَلَى}} ({{tr:ʿala}}) is not the local reading. This first preposition later contrasts with {{ar:لَهُمْ}} ({{tr:lahum}}): haste toward them is forbidden, while a tally is assigned to them.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:عَلَيْهِمْ}} ({{tr:ʿalayhim}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:8:persistent-known-referent","source_type":"word_analysis","support_id":"sup_ed2ea8f66e6db21c4a23","text":"{\"blocking_evidence\":null,\"headline\":\"persistent known referent\",\"reader_payoff\":\"The reader notices that the counted party is not newly introduced; the pronoun carries the group from 19:83 into divine accounting.\",\"reason\":\"The attachment cross-reference resolves the pronoun chain to the disbelievers just mentioned, supporting the continuity claim.\",\"representative_source_ids\":[\"QG-e86963c6\",\"QB-b60dff67\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:8:bound-prepositional-complement","source_type":"word_analysis","support_id":"sup_f0cb5d8f586139e3ddfe","text":"{\"blocking_evidence\":null,\"headline\":\"bound prepositional complement\",\"reader_payoff\":\"The reader notices that the pronoun's role is created by its prepositional host, so the same group can be governed differently in the two clauses.\",\"reason\":\"QAC identifies the word as a third-person plural pronoun and attachment evidence makes it the complement of {{ar:لَ}} ({{tr:la}}), not an independent subject.\",\"representative_source_ids\":[\"QG-f46e6cb7\",\"QF-a1bc7d8f\",\"QT-41fdd795\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:84:9:finite-accounting-root-field","source_type":"word_analysis","support_id":"sup_f0db64b634e921ec2b7e","text":"{\"blocking_evidence\":null,\"headline\":\"finite accounting root field\",\"reader_payoff\":\"The reader notices that broader counted-time and preparation associations add finitude and readiness to the account, while local grammar keeps enumeration as the selected sense.\",\"reason\":\"V4 preserves broader {{ar:ع د د}} ({{tr:ʿ-d-d}}) branches, but the cognate-accusative grammar anchors the local word in counting while allowing finitude echoes at 2:184, 3:24, and 19:94.\",\"representative_source_ids\":[\"QS-1103eb88\",\"QI-a6abc46c\",\"QI-b6a1555c\",\"MI-4fbc7499\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"19:84:2:1","source_type":"qac_morpheme","support_id":"sup_f23543f312749928eedc","text":"{\"lemma_ar\":\"عَجِلَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:Eajila|ROOT:Ejl|2MS|MOOD:JUS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"19:84:2:1\",\"qac_word_ref\":\"19:84:2\",\"root_ar\":\"ع ج ل\",\"surface_ar\":\"تَعْجَلْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"19:84:5:1","source_type":"qac_morpheme","support_id":"sup_f7ff4d0c5fe6f79111e1","text":"{\"lemma_ar\":\"عَدَّ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:Ead~a|ROOT:Edd|1P\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"19:84:5:1\",\"qac_word_ref\":\"19:84:5\",\"root_ar\":\"ع د د\",\"surface_ar\":\"نَعُدُّ\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَلَا تَعْجَلْ عَلَيْهِمْ ۖ إِنَّمَا نَعُدُّ لَهُمْ عَدًّۭا","ayah_ref":"19:84"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000987/B001","root_000989/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000987","role":"Its speeding and advancing-before-time image supplies the human tempo being blocked.","root":"ع ج ل","source_ref":"19:84","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000989","role":"Its exact-enumeration image supplies the measured process that replaces haste.","root":"ع د د","source_ref":"19:84","source_word_indices":["5","7"]}],"changed_reading":{"after":"Do not advance their outcome yourself: an exact process is already running for them, so delay is active rather than empty.","before":"Do not hurry what will happen to them."},"confidence":"strong","focus_anchor":"تَعْجَلْ at word 2 is opposed to نَعُدُّ...عَدًّا at words 5 and 7.","mechanism":"The prohibition blocks advancing an outcome before its time, while إِنَّمَا redirects agency from the addressee's haste to a presently operating exact enumeration.","model_id":"B84_measured_deferral"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:B84_measured_deferral","source_type":"hft","support_id":"sup_67b0aea7184f667db74d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَلَا تَعْجَلْ عَلَيْهِمْ ۖ إِنَّمَا نَعُدُّ لَهُمْ عَدًّۭا","ayah_ref":"19:84"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000987/B001","root_000989/B003","root_000989/B005"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000987","role":"Its before-the-appointed-time image creates the need for a term that must not be preempted.","root":"ع ج ل","source_ref":"19:84","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000989","role":"Its counted-duration image turns enumeration into an allotted waiting period.","root":"ع د د","source_ref":"19:84","source_word_indices":["5","7"]},{"branch_id":"B005","mapped_root_id":"root_000989","role":"Its fixed-time image gives that period a scheduled endpoint.","root":"ع د د","source_ref":"19:84","source_word_indices":["5","7"]}],"changed_reading":{"after":"We are counting out their allotted interval to completion; the ban on haste preserves that measured term.","before":"We are tallying their deeds or persons."},"confidence":"medium","focus_anchor":"The prohibition of premature speed and the cognate نَعُدُّ...عَدًّا construction jointly foreground timing.","mechanism":"The counted-duration and scheduled-time branches let the count sound like a finite allotted interval being run to completion, not only objects being tallied.","model_id":"B84_counted_interval"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:B84_counted_interval","source_type":"hft","support_id":"sup_a25935cdfd85ffb5f624","trust":"legacy_unbound"}]}
</lane_packet_json>
