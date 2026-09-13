# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **91:11**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s091-regular-20260912/s091/91_11/micro.discovery.json` and modify nothing
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
  "ayah_ref": "91:11",
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
{"branch_registry":[{"boundary":"Bu dal, fiziksel taşmayı, belirli bir saptırıcı varlığın adını ve aynı kökün bağımsız sözlükleşmiş anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_000936/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","surface_ar":"طَغْوَىٰ"}],"gloss":"başkaldırıda sınırı aşma ve buna sürükleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başlıca anlam, başkaldırı ve karşı gelmede ölçüyü ya da sınırı aşmaktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgen biçimde bir etken, başka birini sınırı aşan başkaldırıya sürükler veya öyle biri haline getirir."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu ifade hem sınırı aşan öznenin temel eylemini hem de başka bir özneyi aynı duruma götüren ettirgen katmanı birlikte anlatır.","boundary_detail":"Bu dal, fiziksel taşmayı, belirli bir saptırıcı varlığın adını ve aynı kökün bağımsız sözlükleşmiş anlamlarını kapsamaz.","branch_image_ar":"مجاوزة الحد في العصيان","concept_gloss":"başkaldırıda sınırı aşma ve buna sürükleme","contextual_glosses":[{"applicability":"Bir kişinin başkaldırıda ölçüyü aşmış durumunu adlandıran bağlamlarda doğal ve kısa bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir başkasını bu duruma sürükleyen ettirgen katılımcı değişimini tek başına göstermez.","preserves":"Ölçüyü aşan başkaldırı ve taşkın davranış çekirdeğini korur."},"facet_ids":["F001"],"text":"azgınlık","usage_role":"contextual"},{"applicability":"Bir etkenin başka birini başkaldırıda sınırı aşar hale getirdiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öznenin kendiliğinden sınırı aşmasını anlatan yalın kullanım kapsam dışında kalır.","preserves":"Başka birini aşırılığa sürükleyen ettirgen ilişkiyi korur."},"facet_ids":["F002"],"text":"azdırmak","usage_role":"contextual"}],"definition":"Bir kişi ya da şeyin başkaldırı ve karşı gelmede olağan veya meşru sınırı aşmasıdır; ettirgen kullanımda ise bir etken başkasını bu aşırılığa sürükler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başlıca anlam, başkaldırı ve karşı gelmede ölçüyü ya da sınırı aşmaktır."},{"facet_id":"F002","role":"extension","statement":"Ettirgen biçimde bir etken, başka birini sınırı aşan başkaldırıya sürükler veya öyle biri haline getirir."}],"identity_rationale":"Kaynak ifadesi, başkaldırı ve karşı gelmede sınırı ya da ölçüyü aşmayı çekirdek anlam olarak verir; ayrıca bir etkenin başkasını bu aşırılığa sürüklediği ettirgen kullanımı açıkça ayırır. Geçici çerçeve bu iki katmanı doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"başkaldırıda sınırı aşmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"başkaldırıda sınırı aşan"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"başkaldırıda sınırı aşma"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"azdırmak; sınırı aşmaya sürüklemek"}],"lexicalization_note":"Tanım yalın dalın sınır aşan başkaldırı çekirdeğini ve onun ettirgen katılımcı değişimini kapsar; başka dallardaki kalıba bağlı anlamları içeri almaz.","neighbor_coverage_note":"Listelenen bütün komşu adayları değerlendirildi; yalnızca çekirdekle güçlü biçimde örtüşüp sınırı açıklayan iki karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekler büyük ölçüde örtüşür; ancak komşunun zorba kişiyi de kapsayan daha geniş sınırı, odak dalın eylem ve ettirgenlik merkezli sınırıyla tam örtüşmez.","focus_only":"Odak dal, bir etkenin başkasını sınır aşan başkaldırıya sürüklemesini açıkça ayrı bir katman olarak düzenler.","gloss":"sınırı aşan başkaldırı","neighbor_only":"Komşu dal, zorba kişiyi de aynı dalın içinde sayarak kişi adlandırmasını eylem alanına katar.","neighbor_ref":"root_000937/B001","relation_type":"near_synonym","shared_zone":"İki dal da başkaldırıda ölçüyü aşma çekirdeğini ve bu duruma götüren ettirgen kullanımı paylaşır."},{"boundary_match":"partial","distinction":"Komşu genel ve eylem alanları bakımından geniş bir ölçüsüzlük kavramıdır; odak ise bunun başkaldırıya özgü türüdür.","focus_only":"Odak dal, sınır aşmayı özellikle başkaldırı ve karşı gelme alanıyla sınırlar.","gloss":"ölçüyü aşma","neighbor_only":"Komşu dal, para harcama, öldürme, yeme ve su kullanma gibi birçok alandaki ölçüsüzlüğü de kapsar.","neighbor_ref":"root_000699/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da belirlenmiş bir sınırı ya da uygun ölçüyü aşma düşüncesi vardır."}],"source_phrase_ar":"مجاوزة الحد في العصيان (maqayis;sihah;mufradat)؛ كل شيء جاوز القدر فقد طغا (tahdhib)؛ أطغاه المال أي جعله طاغيا وأطغاه كذا حمله على الطغيان (sihah;mufradat)","source_summary":"Kaynaklar, başkaldırıda ölçüyü aşma anlamında birleşir ve ettirgen biçimin para ya da başka bir etken yoluyla birini bu duruma getirdiğini belirtir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الطغيان والطغوان والطغوى، وطغا بمعنى جاوز الحد أو القدر في العصيان، وأطغاه غيره إذا جعله أو حمله على الطغيان.","what_is_not_ar":"لا يدخل فيه فيض الماء والبحر، ولا اسم الطاغوت الخاص، ولا شواذ الطغية والطغيا."},"support_links":[]},{"boundary":"Anlam yalnızca belirtilen su, kan, ses ve rüzgar kalıplarında geçerlidir; insanın başkaldırısını anlatan yalın dala genellenmez.","branch_kind":"collocation","branch_ref":"root_000936/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","surface_ar":"طَغْوَىٰ"}],"gloss":"su, kan, ses ya da rüzgarın sınırını aşıp baskınlaşması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Suya ilişkin kullanımlarda sel bol su getirir, deniz kabarır veya su olağan düzeyini aşıp sürükleyici olur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kan için kullanım, kanın şiddetle coşup olağan durumunu aşmasını anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ses ve rüzgar için kullanım, bunların güçlenip baskın hale gelmesine uzanır."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu açıklama yalnızca kanıtlanan adlarla kurulan kalıplarda, olağan düzeyin aşılması ve gücün baskın hale gelmesi anlamını verir.","boundary_detail":"Anlam yalnızca belirtilen su, kan, ses ve rüzgar kalıplarında geçerlidir; insanın başkaldırısını anlatan yalın dala genellenmez.","branch_image_ar":"طغيان الماء وما يجري مجراه","concept_gloss":"su, kan, ses ya da rüzgarın sınırını aşıp baskınlaşması","contextual_glosses":[{"applicability":"Su ya da selin olağan sınırını aşıp çevreye yayılması anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Denizin kabarmasını, kanın coşmasını ve ses ile rüzgarın baskınlaşmasını tek başına kapsamaz.","preserves":"Suyun olağan düzeyi aşarak yayılması çekirdeğini korur."},"facet_ids":["F001"],"text":"taşmak","usage_role":"contextual"},{"applicability":"Deniz dalgalarının ya da kanın şiddetle kabarıp olağan durumunu aşması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Suyun sürükleyiciliğini ve ses ile rüzgarın üstün gelmesini açıkça göstermez.","preserves":"Denizin veya kanın şiddetlenip olağan durumunu aşmasını korur."},"facet_ids":["F001","F002"],"text":"coşmak","usage_role":"contextual"},{"applicability":"Sesin ya da rüzgarın gücünün ötekileri bastırdığı bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Su ve kanın fiziksel olarak kabarıp sınırı aşması kapsam dışında kalır.","preserves":"Ses veya rüzgarın güçlenerek üstün duruma gelmesini korur."},"facet_ids":["F003"],"text":"baskın gelmek","usage_role":"contextual"}],"definition":"Sel, deniz ya da suyun olağan düzeyini aşıp kabarması ve kimi zaman önüne geleni sürüklemesi; kanın coşması veya ses ile rüzgarın baskınlaşmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Suya ilişkin kullanımlarda sel bol su getirir, deniz kabarır veya su olağan düzeyini aşıp sürükleyici olur."},{"facet_id":"F002","role":"extension","statement":"Kan için kullanım, kanın şiddetle coşup olağan durumunu aşmasını anlatır."},{"facet_id":"F003","role":"extension","statement":"Ses ve rüzgar için kullanım, bunların güçlenip baskın hale gelmesine uzanır."}],"identity_rationale":"Kaynak ifadesi selin bol su getirmesini, denizin kabarıp dalgalanmasını, suyun yükselip sürüklemesini ve kanın taşkınlaşmasını aynı fiziksel sınır aşımı altında toplar; ses ile rüzgarın üstün gelmesi de buna bağlı bir genişlemedir. Geçici çerçeve bu yapıyı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"sel bol suyla taşmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"deniz kabarıp sürükleyici olmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"su olağan düzeyini aşmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kan coşmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ses ya da rüzgar baskın gelmek"}],"lexicalization_note":"Tanım, yalnızca sel, deniz, su, kan, ses ve rüzgarla kurulan belirtilmiş kalıplara bağlıdır; bunlardan bağımsız bir yalın kök anlamı olarak sunulmaz.","neighbor_coverage_note":"Bütün adaylar kapsam ve çekirdek bakımından karşılaştırıldı; eş anlamlı dal ile taşma, kuşatma ve doluluk sınırını açıklayan iki yakın alan yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kanıtlanan çekirdek, örnek alanları ve kapsam sınırı bakımından anlamlı bir ayrım yoktur.","focus_only":null,"gloss":"taşkın fiziksel güç","neighbor_only":null,"neighbor_ref":"root_000937/B002","relation_type":"synonym","shared_zone":"İki dal da su, sel, deniz ve kanın yükselmesini; ses ile rüzgarın da baskınlaşmasını aynı sınırla kapsar."},{"boundary_match":"partial","distinction":"Odak için belirleyici olan olağan ölçünün aşılmasıdır; komşuda ise çevreyi bütünüyle kaplama ve kuşatma öne çıkar.","focus_only":"Odak dal, suyun yanı sıra kan, ses ve rüzgarın ölçüyü aşıp baskınlaşmasını da içerir.","gloss":"çevreyi kaplayan büyük sel","neighbor_only":"Komşu dal, kuşatıp her yanı kaplayan yağmur, karanlık ve genel olayları da kapsar.","neighbor_ref":"root_000957/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da çok miktardaki suyun çevreye üstün gelmesi ve yıkıcı hale gelebilmesi vardır."},{"boundary_match":"field_only","distinction":"Doluluk bir ortamın içeriğinin tamamlanmasını anlatır; odak ise sınır aşan ve baskınlaşan hareketli gücü anlatır.","focus_only":"Odak dalda su veya benzeri güç olağan sınırını aşıp kabarır ve bazen sürükler.","gloss":"suyla dolma","neighbor_only":"Komşu dalda temel işlem bir kabın, yatağın ya da başka bir ortamın suyla dolmasıdır.","neighbor_ref":"root_000676/B001","relation_type":"same_field","shared_zone":"Her iki dal su miktarının artması ve bulunduğu alanda belirgin hale gelmesiyle ilgilidir."}],"source_phrase_ar":"طغى السيل إذا جاء بماء كثير (maqayis;sihah)؛ طغى البحر هاجت أمواجه (maqayis;sihah)؛ طغا البحر والماء إذا علا كل شيء فاجترفه (tahdhib)؛ استعير الطغيان فيه لتجاوز الماء الحد (mufradat)","source_summary":"Kaynaklar suyun olağan ölçüyü aşarak çoğalması, kabarması veya sürükleyici biçimde yükselmesi üzerinde birleşir; aynı fiziksel taşkınlık kan, ses ve rüzgar için de aktarılır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه طغيان السيل والبحر والماء والدم إذا كثر أو هاج أو علا القدر، واستعارة الطغيان لما يجاوز حده من القوى المادية.","what_is_not_ar":"لا يدخل فيه عصيان الإنسان نفسه، ولا الطاغوت، ولا الطغية بمعنى الصفاة أو أعلى الجبل."},"support_links":[]},{"boundary":"Bu dal yalnızca sıradan bir sınır aşma niteliğini veya zalim kişi sıfatını değil, saptırıcı önder ya da yanlış tapınma odağı olan varlığı adlandırır.","branch_kind":"bare","branch_ref":"root_000936/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","surface_ar":"طَغْوَىٰ"}],"gloss":"hak sınırını aşan saptırıcı veya Tanrı dışında tapınılan varlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hak sınırını aşarak sapmayı yöneten veya insanları doğru yoldan uzaklaştıran önder ya da varlıktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Falcı, büyücü ve başkaldıran görünmez varlık, saptırıcı baş olma yönüyle bu kapsama girer."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanrı dışında kendisine tapınılan her varlık da bu adla anılır."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, hem sapmayı yöneten varlığı hem de yanlış tapınmanın yöneldiği varlığı kapsayan sözlükleşmiş ad için kullanılır.","boundary_detail":"Bu dal yalnızca sıradan bir sınır aşma niteliğini veya zalim kişi sıfatını değil, saptırıcı önder ya da yanlış tapınma odağı olan varlığı adlandırır.","branch_image_ar":"الطاغوت رأس الضلالة والطغيان","concept_gloss":"hak sınırını aşan saptırıcı veya Tanrı dışında tapınılan varlık","contextual_glosses":[{"applicability":"İnsanları doğru yoldan uzaklaştıran önder ya da güçlü varlık vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tanrı dışında tapınılan her varlığı kapsayan tapınma ölçütünü tek başına göstermez.","preserves":"Sapmayı yöneten ve başkalarını doğru yoldan uzaklaştıran önderlik yönünü korur."},"facet_ids":["F001","F002"],"text":"sapmanın başı","usage_role":"contextual"},{"applicability":"Tanrı dışında kendisine tapınılan bir varlığın işlevi öne çıkarıldığında açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Saptırıcı önder, falcı veya büyücü gibi tapınma dışındaki örnekleri kapsamaz.","preserves":"Yanlış tapınmanın yöneldiği varlık olma ölçütünü korur."},"facet_ids":["F003"],"text":"sahte tapınma odağı","usage_role":"contextual"}],"definition":"Hak sınırını aşan, insanları doğru yoldan saptıran bir önder ya da varlık; ayrıca Tanrı dışında kendisine tapınılan her türlü varlıktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hak sınırını aşarak sapmayı yöneten veya insanları doğru yoldan uzaklaştıran önder ya da varlıktır."},{"facet_id":"F002","role":"specialization","statement":"Falcı, büyücü ve başkaldıran görünmez varlık, saptırıcı baş olma yönüyle bu kapsama girer."},{"facet_id":"F003","role":"extension","statement":"Tanrı dışında kendisine tapınılan her varlık da bu adla anılır."}],"identity_rationale":"Kaynak ifadesi hak sınırını aşan ve insanları saptıran önderleri, büyücüyü, falcıyı ve başkaldıran görünmez varlığı; ayrıca Tanrı dışında tapınılan her varlığı aynı ad altında toplar. Geçici çerçeve bu kapsayıcı kişi ve tapınma nesnesi anlamını doğru verir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"hak sınırını aşan saptırıcı veya Tanrı dışında tapınılan varlık"}],"lexicalization_note":"Tanım, bu sözlükleşmiş adın saptırıcı ve kendisine tapılan varlık kapsamını korur; başka dallardaki sıfat ve olay anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar incelendi; tam örtüşen dal, genel sınıf ile özel ad ayrımı ve doğru yoldan sapma alanındaki tematik karşıtlık yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek, kapsam ve örnek türleri bakımından yayımlanacak bir anlam ayrımı yoktur.","focus_only":null,"gloss":"sapmanın başı","neighbor_only":null,"neighbor_ref":"root_000937/B003","relation_type":"synonym","shared_zone":"İki dal da sınırı aşan saptırıcı önderleri ve Tanrı dışında tapınılan varlıkları kapsar."},{"boundary_match":"partial","distinction":"Odak genel ve işlevsel bir sınıf adıdır; komşu ise bu sınıfa girebilecek tek bir varlığın özel adıdır.","focus_only":"Odak dal, saptırıcı önderleri ve Tanrı dışında tapınılan bütün varlık türlerini kapsayan genel bir sınıftır.","gloss":"belirli bir put adı","neighbor_only":"Komşu dal, belirli bir puta verilmiş özel addan ibarettir.","neighbor_ref":"root_000760/B003","relation_type":"near_neighbor","shared_zone":"İki dal da Tanrı dışında tapınılan bir varlıkla ilgili olabilir."},{"boundary_match":"thematic_only","distinction":"Karşıt yönleri çağrıştırsalar da biri varlık sınıfı, öteki yön gösterme sürecidir; bu nedenle doğrudan karşıt anlamlı değildirler.","focus_only":"Odak dal doğru yoldan saptıran, sınırı aşan varlığı veya yanlış tapınma odağını adlandırır.","gloss":"doğru yolu gösterme","neighbor_only":"Komşu dal doğru yolu gösterme, açıklama, ona yönelme ve bu yönelişi kabul etme sürecini anlatır.","neighbor_ref":"root_001583/B001","relation_type":"thematic","shared_zone":"İki dal da kişinin doğru yol ile ilişkisini ve yönelişini konu edinir."}],"source_phrase_ar":"الطاغوت الكاهن والشيطان وكل رأس في الضلالة (sihah)؛ كل معبود من دون الله جبت وطاغوت (tahdhib)؛ عبارة عن كل متعد وكل معبود من دون الله والساحر والكاهن والمارد من الجن (mufradat)","source_summary":"Kaynaklar, hak sınırını aşan ve sapmayı yöneten önderleri çeşitli örneklerle açıklar; kapsamı Tanrı dışında tapınılan her türlü varlığa kadar genişletir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه الطاغوت للكاهن والشيطان وكل رأس في الضلالة وكل معبود من دون الله، ويستعمل للواحد والجمع.","what_is_not_ar":"لا يدخل فيه مجرد صفة الطاغي، ولا الطاغية بمعنى الصاعقة أو صيحة العذاب."},"support_links":[]},{"boundary":"Bu kişi adı, aynı biçimin yıldırım, yıkıcı çığlık ya da başka bir felaket anlamından ve saptırıcı varlık sınıfından ayrıdır.","branch_kind":"bare","branch_ref":"root_000936/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","surface_ar":"طَغْوَىٰ"}],"gloss":"pervasız ve ezici zorba","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnatçı, kendini büyük gören ve insanları baskıyla ezen zalim kişi ya da hükümdardır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yaptığı kötülüğü önemsemeyen ve insanları yiyip bitirircesine ezen pervasız zorba tipini belirtir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir aktarımda belirli bir ülkenin hükümdarı için kullanılan bir unvan olarak verilir."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanları baskı altında tutan, yaptığı kötülüğü umursamayan ve kendini büyük gören kişi ya da hükümdar için kullanılır.","boundary_detail":"Bu kişi adı, aynı biçimin yıldırım, yıkıcı çığlık ya da başka bir felaket anlamından ve saptırıcı varlık sınıfından ayrıdır.","branch_image_ar":"الطاغية المتجبر","concept_gloss":"pervasız ve ezici zorba","contextual_glosses":[{"applicability":"Siyasi güç sahibi zalim ve baskıcı kişi özellikle vurgulandığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hükümdar olmayan zorba kişileri ve pervasızlık ayrıntısını tek başına kapsamaz.","preserves":"İnsanları ezen zalim yönetici olma yönünü korur."},"facet_ids":["F001","F003"],"text":"zorba hükümdar","usage_role":"contextual"}],"definition":"İnsanları ezen, yaptığı kötülüğü umursamayan, inatçı, kendini büyük gören zalim hükümdar ya da zorbaya verilen addır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnatçı, kendini büyük gören ve insanları baskıyla ezen zalim kişi ya da hükümdardır."},{"facet_id":"F002","role":"specialization","statement":"Yaptığı kötülüğü önemsemeyen ve insanları yiyip bitirircesine ezen pervasız zorba tipini belirtir."},{"facet_id":"F003","role":"source_variant","statement":"Bir aktarımda belirli bir ülkenin hükümdarı için kullanılan bir unvan olarak verilir."}],"identity_rationale":"Kaynak ifadesi bu adı, inatçı ve kendini büyük gören; yaptıklarını umursamadan insanları yiyip bitirircesine ezen hükümdar veya zorba için verir. Geçici çerçeve kişi türünü ve baskıcı davranışı doğru biçimde sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"pervasız, kendini büyük gören ve insanları ezen zorba"}],"lexicalization_note":"Tanım, sözlükleşmiş kişi adını yalın dal olarak korur ve aynı biçimin felaket anlamını bu dala taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; zorbanın kişi niteliğini, büyüklük taslama tutumundan ve zorla boyun eğdirme eyleminden ayıran iki karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu bir tutum ve davranış alanıdır; odak ise bu tutumu baskı ve pervasızlıkla birleştiren zorba kişiyi adlandırır.","focus_only":"Odak dal, kendini büyük görmesini insanları ezen belirli bir zalim kişi tipinde somutlaştırır.","gloss":"büyüklük taslama","neighbor_only":"Komşu dal, kişi adı olmaktan çok yeryüzünde büyüklük taslama ve başkalarına üstünlük arama tutumunu anlatır.","neighbor_ref":"root_001042/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kendini başkalarından üstün görme ve kınanan taşkınlık vardır."},{"boundary_match":"field_only","distinction":"Odak baskıcı failin kalıcı niteliğini ve kişi türünü, komşu ise baskı kurma eylemi ile sonucunu merkez alır.","focus_only":"Odak dal, baskıyı uygulayan inatçı ve pervasız zorba kişi tipini adlandırır.","gloss":"zorla boyun eğdirme","neighbor_only":"Komşu dal, üstün gelme, zorla alma, boyun eğdirme ve başka birini baskı altına sokma işlemini anlatır.","neighbor_ref":"root_001266/B001","relation_type":"same_field","shared_zone":"İki dal da güç kullanarak başkalarını ezme ve iradelerini kırma alanındadır."}],"source_phrase_ar":"الطاغية ملك الروم (sihah)؛ الطاغية الجبار العنيد (tahdhib)؛ الذي لا يبالي ما أتى يأكل الناس ويقهرهم (tahdhib)؛ الأحمق المستكبر الظالم (tahdhib)","source_summary":"Kaynakların toplu anlatımı, sözcüğü zalim, inatçı, kendini büyük gören ve insanları pervasızca ezen bir hükümdar ya da zorba adı olarak açıklar; bir aktarım onu belirli bir hükümdarlık unvanına bağlar.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الطاغية للملك أو الجبار العنيد أو المستكبر الظالم الذي يقهر الناس ولا يتحرج.","what_is_not_ar":"لا يدخل فيه الطاغية بمعنى الصاعقة أو صيحة العذاب، ولا الطاغوت بوصفه اسما جامعا للمعبود أو رأس الضلالة."},"support_links":[]},{"boundary":"Tanım, yıldırım veya yıkıcı çığlık, insanların kendi sınır aşımı ve büyük sel yorumlarını seçenekler olarak ayırır; zorba kişi anlamını dışarıda tutar.","branch_kind":"bare","branch_ref":"root_000936/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","surface_ar":"طَغْوَىٰ"}],"gloss":"yıkıcı yıldırım ya da çığlık, sınır aşımı veya büyük sel","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yorumda yıkıcı yıldırım ya da öldürücü ceza çığlığıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir başka yorumda, yok edilen insanların kendi sınır aşımını adlaştırır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir açıklama sözcüğü suyun ölçüyü aşmasıyla oluşan büyük sele bağlar."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu çok parçalı karşılık, kaynakların aynı sözlükleşmiş ad için verdiği birbirinden ayrılan yorumları seçenekler halinde korur.","boundary_detail":"Tanım, yıldırım veya yıkıcı çığlık, insanların kendi sınır aşımı ve büyük sel yorumlarını seçenekler olarak ayırır; zorba kişi anlamını dışarıda tutar.","branch_image_ar":"الطاغية عقوبة غالبة","concept_gloss":"yıkıcı yıldırım ya da çığlık, sınır aşımı veya büyük sel","contextual_glosses":[{"applicability":"Sözcüğün gökten gelen yıkıcı olay olarak yorumlandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öldürücü çığlık, insanların kendi sınır aşımı ve büyük sel yorumlarını dışarıda bırakır.","preserves":"Yıkıma yol açan göksel olay yorumunu korur."},"facet_ids":["F001"],"text":"yıkıcı yıldırım","usage_role":"contextual"},{"applicability":"Yıkımın güçlü ve öldürücü bir sesle gerçekleştiği yorumda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yıldırım, insanların kendi sınır aşımı ve büyük sel yorumlarını kapsamaz.","preserves":"Yıkıcı ve öldürücü ses yorumunu açık biçimde korur."},"facet_ids":["F001"],"text":"öldürücü çığlık","usage_role":"contextual"},{"applicability":"Sözcüğün suyun ölçüyü aşmasına bağlandığı yorumda kullanılabilecek doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yıldırım, öldürücü çığlık ve insanların kendi sınır aşımı yorumlarını dışarıda bırakır.","preserves":"Suyun sınırı aşmasıyla oluşan büyük sel yorumunu korur."},"facet_ids":["F003"],"text":"büyük sel","usage_role":"contextual"}],"definition":"Yıkıma yol açan yıldırım ya da öldürücü çığlık için kullanılan bir ad olarak açıklanır; başka yorumlarda insanların kendi sınır aşımını veya büyük seli belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yorumda yıkıcı yıldırım ya da öldürücü ceza çığlığıdır."},{"facet_id":"F002","role":"source_variant","statement":"Bir başka yorumda, yok edilen insanların kendi sınır aşımını adlaştırır."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir açıklama sözcüğü suyun ölçüyü aşmasıyla oluşan büyük sele bağlar."}],"identity_rationale":"Geçici çerçevedeki baskın ceza fikri, yıldırım ve yıkıcı çığlık yorumlarını karşılar; ancak kaynak ifadesi aynı biçimi insanların kendi sınır aşımı olarak adlaştıran ve büyük sele bağlayan ayrı yorumlar da verir. Dal korunabilir, fakat tek ve birleşik bir ceza türü gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yıkıcı yıldırım ya da çığlık; sınır aşımı veya büyük sel"}],"lexicalization_note":"Tanım, sözlükleşmiş yalın adın birbirinden ayrılan yorumlarını korur; bunları genel bir ceza ya da genel başkaldırı anlamına yaymaz.","neighbor_coverage_note":"Bütün adaylar kaynak yorumları ayrı tutularak değerlendirildi; yıldırım, çığlık ve genel ceza ile kurulan üç yararlı sınır karşılaştırması yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yıldırım yalnızca odak dalın yorumlarından biridir; komşu ise göksel çarpma olayının kendi daha geniş doğa olayı sınırına sahiptir.","focus_only":"Odak dal, yıldırımın yanı sıra öldürücü çığlık, insanların kendi sınır aşımı ve büyük sel yorumlarını da içerir.","gloss":"göksel çarpma ve yıldırım","neighbor_only":"Komşu dal, gökteki şiddetli ses veya çarpma olayını, ateş, ölüm ve ceza olasılıklarıyla genel olarak anlatır.","neighbor_ref":"root_000864/B002","relation_type":"near_synonym","shared_zone":"İki dal, gökten gelen şiddetli ve yıkıcı bir olayın yıldırım olarak anlaşılabildiği alanda örtüşür."},{"boundary_match":"partial","distinction":"Odaktaki ses belirli bir yıkım yorumudur; komşu ise yıkım gerektirmeyen çeşitli ürkütücü çığlıkları da kapsar.","focus_only":"Odak dalda öldürücü çığlık yalnızca bir yorumdur; yıldırım, sınır aşımı ve büyük sel seçenekleri de vardır.","gloss":"ürkütücü çığlık","neighbor_only":"Komşu dal saldırı, ağıt, ani kötülük ve korku gibi bağlamlardaki ürkütücü çığlıkları da kapsar.","neighbor_ref":"root_000895/B002","relation_type":"near_synonym","shared_zone":"İki dal, güçlü bir çığlığın korku veya yıkımla ilişkilendirildiği kullanımda örtüşür."},{"boundary_match":"partial","distinction":"Komşu genel ceza kavramıdır; odak ise yalnızca bazı yorumlarda ceza sayılan, başka yorumlarda eylem veya sel olan özel bir addır.","focus_only":"Odak dal, belirli bir sözlükleşmiş adın yıldırım, çığlık, sınır aşımı ve büyük sel biçimindeki yorumlarını taşır.","gloss":"acı veren ceza","neighbor_only":"Komşu dal, acı verme ve karşılık olarak uygulanan her türlü cezayı genel bir kavram halinde kapsar.","neighbor_ref":"root_000994/B005","relation_type":"near_neighbor","shared_zone":"Yıldırım veya öldürücü çığlık yorumu, yıkıcı bir ceza olarak anlaşılabildiğinde iki alan kesişir."}],"source_phrase_ar":"الطاغية الصاعقة ويعني صيحة العذاب (sihah)؛ طغت الصيحة على ثمود (tahdhib)؛ أهلكوا بالطاغية أي بطغيانهم مصدر على فاعلة (tahdhib)؛ إشارة إلى الطوفان المعبر عنه بإنا لما طغى الماء (mufradat)","source_summary":"Toplu kaynak kaydı tek bir açıklamada birleşmez: sözcük yıkıcı yıldırım veya öldürücü çığlık, yok edilenlerin kendi sınır aşımı ya da suyun ölçüyü aşmasıyla oluşan büyük sel olarak yorumlanır.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه إطلاق الطاغية على الصاعقة أو صيحة العذاب أو العقوبة الغالبة المتصلة بطغيان أو بطوفان.","what_is_not_ar":"لا يدخل فيه الطاغية بمعنى الجبار العنيد، ولا الطاغوت، ولا مطلق الطغيان المعنوي."},"support_links":[]},{"boundary":"Bu dal, aynı biçimin küçük parça anlamını ve kökün sınır aşma anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_000936/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","surface_ar":"طَغْوَىٰ"}],"gloss":"düz ve pürüzsüz kaya, dağ doruğu ya da yüksek yer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Düz ve pürüzsüz kaya anlamına gelir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı biçim bir aktarımda dağın en yüksek yeri anlamındadır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İlgili başka biçim, genel olarak yüksek bir yeri adlandırır."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşılık, iki sözlük biçiminin kaya niteliğini ve yükseltiye dayalı yer anlamlarını seçenekler halinde birlikte gösterir.","boundary_detail":"Bu dal, aynı biçimin küçük parça anlamını ve kökün sınır aşma anlamlarını kapsamaz.","branch_image_ar":"الطغية الصفاة أو الموضع المرتفع","concept_gloss":"düz ve pürüzsüz kaya, dağ doruğu ya da yüksek yer","contextual_glosses":[{"applicability":"Taşın düz ve pürüzsüz yüzeyi öne çıktığında kullanılabilecek açıklayıcı karşılıktır.","error_profile":{"adds":"Yalçın sözü, kaynakta zorunlu olmayan diklik ve aşılması güçlük çağrışımı ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Düz ve pürüzsüz kaya olma niteliğini korur."},"facet_ids":["F001"],"text":"yalçın düz kaya","usage_role":"contextual"},{"applicability":"Dağın en yüksek bölümünü gösteren aktarım söz konusu olduğunda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Pürüzsüz kaya ve dağla sınırlı olmayan yüksek yer anlamlarını kapsamaz.","preserves":"Dağın en yüksek yeri olma yorumunu korur."},"facet_ids":["F002"],"text":"dağ doruğu","usage_role":"contextual"}],"definition":"Düz ve pürüzsüz bir kaya ya da dağın en yüksek yeri; ilgili başka bir biçimde ise herhangi bir yüksek yerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Düz ve pürüzsüz kaya anlamına gelir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı biçim bir aktarımda dağın en yüksek yeri anlamındadır."},{"facet_id":"F003","role":"extension","statement":"İlgili başka biçim, genel olarak yüksek bir yeri adlandırır."}],"identity_rationale":"Kaynak ifadesi bir biçim için düz ve pürüzsüz kaya ile dağ doruğunu, ikinci biçim için de her yüksek yeri verir. Geçici çerçeve taşın niteliğini ve yükselti kapsamını birbirinden ayırarak doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"düz ve pürüzsüz kaya ya da dağ doruğu"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yüksek yer"}],"lexicalization_note":"Tanım, iki yalın sözlük biçiminin düz kaya, dağ doruğu ve yüksek yer anlamlarını korur; eylem dallarına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eş dal ile pürüzsüz kaya anlamında örtüşen fakat maddi nitelikleri farklı komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve kapsam sınırları tam örtüştüğü için yayımlanacak bir anlam ayrımı yoktur.","focus_only":null,"gloss":"pürüzsüz kaya ve yüksek yer","neighbor_only":null,"neighbor_ref":"root_000937/B005","relation_type":"synonym","shared_zone":"İki dal da düz ve pürüzsüz kaya, dağın en yüksek yeri ve genel yüksek yer anlamlarını kapsar."},{"boundary_match":"partial","distinction":"Odak yükselti anlamlarına da açılır; komşu ise kayanın maddi yüzey ve temizlik özelliklerini daha sıkı tanımlar.","focus_only":"Odak dal, pürüzsüz kayanın yanı sıra dağ doruğu ve genel yüksek yer anlamlarını da taşır.","gloss":"düz ve temiz kaya","neighbor_only":"Komşu dal, kayanın geniş, sert ve toprak ile çamurdan arınmış olmasını daha ayrıntılı biçimde belirtir.","neighbor_ref":"root_000873/B006","relation_type":"near_synonym","shared_zone":"İki dal düz, sert ve pürüzsüz bir kaya parçasını adlandırma alanında örtüşür."}],"source_phrase_ar":"الطغية الصفاة الملساء (maqayis;tahdhib)؛ الطغية أعلى الجبل وكل مكان مرتفع طغوة (sihah)","source_summary":"Kaynak kaydı düz ve pürüzsüz kaya anlamını paylaşır; ayrıca dağın en yüksek yeri yorumunu ve ilgili biçimin herhangi bir yüksek yere verilen ad olduğunu korur.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الطغية للصفاة الملساء أو أعلى الجبل، والطغوة للمكان المرتفع.","what_is_not_ar":"لا يدخل فيه الطغيان بمعنى مجاوزة الحد، ولا الطغية بمعنى النبذة، ولا الطغيا للبقرة."},"support_links":[]},{"boundary":"Bu dal belirli bir kesri, büyük bir bölümü, kaya veya yüksek yer anlamını ya da sınır aşma eylemini kapsamaz.","branch_kind":"bare","branch_ref":"root_000936/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","surface_ar":"طَغْوَىٰ"}],"gloss":"bir şeyden küçük parça","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünün türü belirtilmeksizin, ondan küçük bir parça veya az bir miktar anlatılır."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bütünün türü belirtilmeden ondan ayrılan veya geriye kalan küçük parçayı anlatan genel karşılıktır.","boundary_detail":"Bu dal belirli bir kesri, büyük bir bölümü, kaya veya yüksek yer anlamını ya da sınır aşma eylemini kapsamaz.","branch_image_ar":"الطغية نبذة من الشيء","concept_gloss":"bir şeyden küçük parça","contextual_glosses":[{"applicability":"Maddenin veya bütünün türünün önemli olmadığı gündelik bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütünden küçük ve belirsiz miktarda bir parça olma anlamını korur."},"facet_ids":["F001"],"text":"ufak bir parça","usage_role":"general"}],"definition":"Herhangi bir şeyden ayrılmış, alınmış ya da kalmış küçük bir parçadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünün türü belirtilmeksizin, ondan küçük bir parça veya az bir miktar anlatılır."}],"identity_rationale":"Kaynak ifadesi, herhangi bir şeyden alınan ya da kalan küçük bir parçayı tek ve açık anlam olarak verir. Geçici çerçeve bu nicelik ve parça sınırını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"herhangi bir şeyden küçük parça"}],"lexicalization_note":"Tanım, yalın sözlük biçiminin herhangi bir şeyden küçük parça anlamıyla sınırlıdır ve başka biçimlerin anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel küçük parça anlamını belirli maddelerdeki az miktardan ve kesilmiş parçadan ayıran iki karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bütünü tümüyle açık bırakır; komşu ise azlığı belirli madde ve parça türleri üzerinden sözlükleştirir.","focus_only":"Odak dal, herhangi bir şeyden alınan küçük parçayı hiçbir madde türüyle sınırlamaz.","gloss":"az miktar","neighbor_only":"Komşu dal, mal, ot, yağmur ve yaş ürün gibi belirli maddelerin az miktarlarını ve bazı özel parçaları sayar.","neighbor_ref":"root_001466/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir bütüne göre küçük kalan parça veya miktarı anlatır."},{"boundary_match":"partial","distinction":"Odakta küçüklük ve belirsiz bütün esastır; komşuda kesilip ayrılma ilişkisi öne çıkar.","focus_only":"Odak dal, parçanın küçük olmasını ve herhangi bir bütünden gelebilmesini öne çıkarır.","gloss":"kesilmiş parça","neighbor_only":"Komşu dal, meyve gibi bir nesneden kesilip ayrılmış parçayı anlatır; küçüklük zorunlu değildir.","neighbor_ref":"root_000786/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir bütünden ayrılmış parçayı adlandırabilir."}],"source_phrase_ar":"الطغية من كل شيء نبذة منه (sihah)","source_summary":"Tek kaynaklı kayıt, sözcüğü herhangi bir şeyden küçük bir parça ya da az miktar olarak açıklar ve ek bir kapsam koşulu vermez.","sources":["SI"],"what_is_ar":"يدخل فيه الطغية من كل شيء بمعنى نبذة منه.","what_is_not_ar":"لا يدخل فيه الصفاة الملساء أو المكان المرتفع، ولا الطغيان، ولا الطغيا للبقرة."},"support_links":[]},{"boundary":"Bu dal genel ses kavramı değildir; yalnızca belirtilen kişi veya topluluk kalıbındaki ağız kullanımını kapsar.","branch_kind":"collocation","branch_ref":"root_000936/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","surface_ar":"طَغْوَىٰ"}],"gloss":"bir kimsenin ya da topluluğun sesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalıp, adı geçen kişinin veya topluluğun işitilen sesini belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanım genel dil değil, kaynakta özellikle belirtilen bir ağızla sınırlıdır."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık yalnızca kaynakta belirtilen ağızda kişi veya toplulukla kurulan özel kalıp için geçerlidir.","boundary_detail":"Bu dal genel ses kavramı değildir; yalnızca belirtilen kişi veya topluluk kalıbındaki ağız kullanımını kapsar.","branch_image_ar":"طغي القوم صوتهم","concept_gloss":"bir kimsenin ya da topluluğun sesi","contextual_glosses":[{"applicability":"Kalıpta tek kişi yerine bir topluluğun çıkardığı veya ondan işitilen ses söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir kişinin sesini anlatan kullanım ile ağız kaydını tek başına göstermez.","preserves":"Sesin adı geçen topluluğa ait olması ilişkisini korur."},"facet_ids":["F001"],"text":"topluluğun sesi","usage_role":"contextual"}],"definition":"Belirli bir ağızda, bir kişi ya da toplulukla kurulan kalıp içinde o kişi veya topluluktan işitilen ses demektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalıp, adı geçen kişinin veya topluluğun işitilen sesini belirtir."},{"facet_id":"F002","role":"specialization","statement":"Kullanım genel dil değil, kaynakta özellikle belirtilen bir ağızla sınırlıdır."}],"identity_rationale":"Kaynak ifadesi belirli bir ağız kullanımında, bir kişi ya da toplulukla kurulan kalıbın o kişi veya topluluğun sesi anlamına geldiğini açıkça bildirir. Geçici çerçeve hem anlamı hem de ağız kaydını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir kimsenin ya da topluluğun sesi"}],"lexicalization_note":"Tanım, bir kişi ya da topluluğun sesi anlamındaki belirtilmiş ağız kalıbına bağlıdır ve yalın köke genel ses anlamı yüklemez.","neighbor_coverage_note":"Bütün adaylar kalıp ve ağız sınırı gözetilerek değerlendirildi; doğrudan ses adı, genel ses kavramı ve karışık topluluk gürültüsüyle üç ayrım yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Anlamsal çekirdek yakın olsa da odak dalın kişi veya toplulukla kurulan kalıp ve ağız sınırı komşuda yoktur.","focus_only":"Odak dal, sesi kişi ya da toplulukla kurulan belirli bir ağız kalıbı içinde anlatır.","gloss":"ses","neighbor_only":"Komşu dal, başka bir sözlük biçimini doğrudan ses adı olarak verir ve kişi ya da topluluk kalıbı şartı koymaz.","neighbor_ref":"root_000450/B007","relation_type":"near_synonym","shared_zone":"İki dalın çekirdeği de işitilen sesi adlandırmaktır."},{"boundary_match":"partial","distinction":"Komşu genel ses alanıdır; odak ise sahibi belirtilmiş ses için kalıba ve ağız kullanımına bağlı dar bir adlandırmadır.","focus_only":"Odak dal, belirli bir kişi ya da topluluğa ait sesi özel bir ağız kalıbında adlandırır.","gloss":"işitilen ses","neighbor_only":"Komşu dal, kulağa ulaşan her türlü sesi; bağırma, ezgi, gürültü ve yardım çağrısı gibi türleriyle kapsar.","neighbor_ref":"root_000890/B001","relation_type":"near_synonym","shared_zone":"Her iki dal insan veya topluluktan işitilebilen sesi kapsayabilir."},{"boundary_match":"partial","distinction":"Odakta sesin topluluğa ait olması yeterlidir; komşuda çoklu seslerin yükselmesi ve birbirine karışması belirleyicidir.","focus_only":"Odak dal, kişi veya topluluğun sesini yüksek, karışık ya da gürültülü olma şartı olmadan belirtir.","gloss":"karışık topluluk gürültüsü","neighbor_only":"Komşu dal, topluluk seslerinin yükselip karışmasını, gürültüyü ve uğultuyu özellikle içerir.","neighbor_ref":"root_001344/B005","relation_type":"near_neighbor","shared_zone":"İki dal da bir topluluktan çıkan ses için kullanılabilir."}],"source_phrase_ar":"سمعت طغي فلان أي صوته هذلية؛ سمعت طغي القوم وطهيهم ووغيهم أي صوتهم (tahdhib)","source_summary":"Tek kaynaklı kayıt, belirtilen ağızda kişi veya toplulukla kurulan kalıbı onların işitilen sesi olarak açıklar ve benzer ses adlarıyla birlikte aktarır.","sources":["TA"],"what_is_ar":"يدخل فيه طغي فلان أو طغي القوم بمعنى الصوت في النقل الهذلي.","what_is_not_ar":"لا يدخل فيه الطغيان، ولا طغيان الماء، ولا أسماء الطاغوت والطاغية."},"support_links":[]},{"boundary":"Ana anlam yabani sığır yavrusudur; böğüren inek aktarımı ayrı tutulur ve dal evcil sığır yavrusuna ya da genel sığır adına genişletilmez.","branch_kind":"bare","branch_ref":"root_000936/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","surface_ar":"طَغْوَىٰ"}],"gloss":"yabani sığır yavrusu; bir aktarımda böğüren inek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yabani sığırın küçük yavrusunu adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başka bir aktarım, sözcüğü böğüren bir inek için de verir."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık ana hayvan adı anlamını öne alır ve kaynaklardaki farklı böğüren inek aktarımını ayrı bir seçenek olarak saklar.","boundary_detail":"Ana anlam yabani sığır yavrusudur; böğüren inek aktarımı ayrı tutulur ve dal evcil sığır yavrusuna ya da genel sığır adına genişletilmez.","branch_image_ar":"الطغيا الصغير من بقر الوحش","concept_gloss":"yabani sığır yavrusu; bir aktarımda böğüren inek","contextual_glosses":[{"applicability":"Hayvanın türü ve küçük yaşı açıkça kastedildiğinde ana ve en doğrudan karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Böğüren inek biçimindeki ayrı ve daha az belirli aktarımı kapsamaz.","preserves":"Yabani sığırın küçük yavrusu olma ana anlamını eksiksiz korur."},"facet_ids":["F001"],"text":"yabani sığır yavrusu","usage_role":"general"},{"applicability":"Kaynağın yaş ve yabanilik belirtmeden böğürme özelliğiyle verdiği ayrı aktarımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yabani sığırın küçük yavrusu olma ana anlamını kapsamaz.","preserves":"İneğin böğürmesiyle tanımlanan ayrı kaynak aktarımını korur."},"facet_ids":["F002"],"text":"böğüren inek","usage_role":"contextual"}],"definition":"Başlıca aktarımda yabani sığır yavrusuna verilen addır; başka bir aktarımda böğüren bir inek için de kullanıldığı bildirilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yabani sığırın küçük yavrusunu adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Başka bir aktarım, sözcüğü böğüren bir inek için de verir."}],"identity_rationale":"Bir kaynak ifadesi sözcüğü açıkça yabani sığır yavrusu olarak verir; diğer aktarım ise böğüren bir inekle birlikte anarak yaş ve yabanilik sınırını belirsizleştirir. Geçici çerçeve ana aktarımı korur, ancak ikinci aktarım ayrı bir kaynak değişkesi olarak belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yabani sığır yavrusu; bir aktarımda böğüren inek"}],"lexicalization_note":"Tanım, yalın hayvan adının yabani sığır yavrusu anlamını ve ayrı böğüren inek aktarımını korur; başka hayvan adlarına genellenmez.","neighbor_coverage_note":"Bütün adaylar tür, yaş ve evcillik sınırları bakımından değerlendirildi; yabani sığır yavrusuyla örtüşen çok anlamlı ad ve evcil sığır yavrusu karşılaştırıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bu hayvanı ana anlam yapar; komşu ise onu çeşitli hafif ya da genç hayvanlardan biri olarak daha geniş bir ad altında kapsar.","focus_only":"Odak dalın ana anlamı özellikle yabani sığır yavrusudur ve ayrıca böğüren inek aktarımı vardır.","gloss":"yabani sığır yavrusu ve benzer hayvanlar","neighbor_only":"Komşu dal yavru geyik, yaban keçisi ve hafif eşek gibi başka hayvanlara da uzanan çok anlamlı bir hayvan adıdır.","neighbor_ref":"root_001030/B004","relation_type":"near_synonym","shared_zone":"İki dal da yabani sığır yavrusunu adlandırabilir."},{"boundary_match":"partial","distinction":"Odakta yabanilik belirleyicidir; komşu evcil sığır yavrusuyla sınırlıdır ve böğüren yetişkin inek aktarımını taşımaz.","focus_only":"Odak dal yabani sığır yavrusunu ve ayrı bir böğüren inek aktarımını içerir.","gloss":"evcil sığır yavrusu","neighbor_only":"Komşu dal evcil sığırın yavrusunu ve onun dişi biçimini adlandırır.","neighbor_ref":"root_000987/B002","relation_type":"near_synonym","shared_zone":"Her iki dal sığır türünden bir hayvanın yavrusunu adlandırır."}],"source_phrase_ar":"طغيا وهو الصغير من بقر الوحش (sihah)؛ يقال للبقرة الخائرة والطغيا (tahdhib)","source_summary":"Toplu kaynak kaydı, ana anlamı yabani sığırın küçük yavrusu olarak verir; ayrıca yaş ve yabanilik sınırını aynı açıklıkla taşımayan böğüren inek aktarımını korur.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الطغيا اسما للصغير من بقر الوحش.","what_is_not_ar":"لا يدخل فيه الطغية للصفاة أو النبذة، ولا الطغيان، ولا الطاغوت."},"support_links":[]},{"boundary":"Dalın çekirdeği sınır veya ölçü aşımıdır; suyun taşması, sapmanın önderi ve pürüzsüz kaya anlamları bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000937/B001","candidate_links":[{"candidate_id":"cand_41a3ca2ecaf0356b829c","lane":"micro"},{"candidate_id":"cand_c7a4d4d9fc5856f19727","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","surface_ar":"طَغْوَىٰ"}],"gloss":"itaatsizlikte veya ölçüde sınırı aşma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığın kendisi için geçerli sınırı veya uygun ölçüyü aşması çekirdek anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan davranışında bu aşım, özellikle itaatsizlik ve başkaldırı içinde sınır tanımama biçiminde gerçekleşir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, bir kimseyi sınır aşan ve taşkın davranışa sürükleme sonucunu bildirir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişi adı olarak türemiş kullanım, yaptığını umursamayan, insanları ezen, inatçı ve kibirli zorbayı niteler."}}],"root_ar":"ط غ ي","root_id":"root_000937","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çekirdek eylemi hem insanın itaatsizliği hem de herhangi bir şeyin kendi ölçüsünü aşması için karşılar.","boundary_detail":"Dalın çekirdeği sınır veya ölçü aşımıdır; suyun taşması, sapmanın önderi ve pürüzsüz kaya anlamları bu dala girmez.","branch_image_ar":"مجاوزة الحد في العصيان","concept_gloss":"itaatsizlikte veya ölçüde sınırı aşma","contextual_glosses":[{"applicability":"Bir kişinin itaatsizlik ve başkaldırı içinde kabul edilen sınırı aşmasını anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan dışındaki şeylerin kendi ölçüsünü aşabilmesi kapsamını dışarıda bırakır.","preserves":"İnsan davranışındaki itaatsiz sınır aşımını doğal biçimde korur."},"facet_ids":["F001","F002"],"text":"azıp sınırı aştı","usage_role":"contextual"},{"applicability":"Bir etkenin başka bir kişiyi sınır tanımaz davranışa yönelttiği ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın biçimde öznenin kendi sınırını aşması ve zorba kişi kullanımı bu karşılıkta yer almaz.","preserves":"Başka bir katılımcıyı aşırılığa sürükleyen ettirgen ilişkiyi korur."},"facet_ids":["F003"],"text":"onu azdırıp sınır aşmaya sürükledi","usage_role":"contextual"},{"applicability":"İnsanları ezen, yaptığı kötülüğü umursamayan inatçı ve kibirli kişiyi niteleyen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eylem olarak sınırı aşma ve başkasını bu eyleme sürükleme anlamlarını dışarıda bırakır.","preserves":"Kişiye yüklenen zorbalık, inat ve sınır tanımazlık özelliklerini korur."},"facet_ids":["F004"],"text":"sınır tanımaz zorba","usage_role":"contextual"}],"definition":"Bir kimsenin itaatsizlikte ya da herhangi bir şeyin kendi ölçüsünde belirlenmiş sınırı aşmasıdır. Türemiş kullanımlar, birini böyle bir aşırılığa sürüklemeyi ve sınır tanımayan inatçı zorba kişiyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığın kendisi için geçerli sınırı veya uygun ölçüyü aşması çekirdek anlamdır."},{"facet_id":"F002","role":"specialization","statement":"İnsan davranışında bu aşım, özellikle itaatsizlik ve başkaldırı içinde sınır tanımama biçiminde gerçekleşir."},{"facet_id":"F003","role":"extension","statement":"Ettirgen kullanım, bir kimseyi sınır aşan ve taşkın davranışa sürükleme sonucunu bildirir."},{"facet_id":"F004","role":"specialization","statement":"Kişi adı olarak türemiş kullanım, yaptığını umursamayan, insanları ezen, inatçı ve kibirli zorbayı niteler."}],"identity_rationale":"Kaynak ifadesi, çekirdeği itaatsizlikte sınırı aşma olarak verirken ölçüsünü aşan her şeyi de kapsar; ayrıca başkasını bu duruma sürükleyen ettirgen kullanımı ve sınır tanımaz zorba kişiyi bildiren türemiş kullanımı belirtir. Bu nedenle dal korunabilir, ancak yalnızca insanın itaatsizliğiyle sınırlandırılmamalı ve türemiş kullanımlar çekirdek eylemle özdeşleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sınırı veya ölçüyü aşmak, azmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"itaatsizlikte sınırı aşan, azgın"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"itaatsizlikte sınır tanımazlık ve azgınlık"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sınırı aşma ve azgınlık"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"sınırı aşma durumu, azgınlık"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onu azdırdı veya sınır aşmaya sürükledi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"inatçı, kibirli ve sınır tanımaz zorba"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"Roma hükümdarına verilen unvan"}],"lexicalization_note":"Tanım yalın sınır aşma çekirdeğini, birini sınır aşmaya sürükleyen ettirgen kullanımdan ve zorba kişiyi bildiren türemiş kullanımdan ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı kapsamlı dal ile sınır aşımı, nimet karşısında şımarma ve maddi taşkınlık arasındaki en yararlı dört karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda çekirdek, kapsam ve türemiş kullanımlar bakımından anlamlı bir sınır farkı görünmez.","focus_only":null,"gloss":"sınırı aşma ve azgınlık","neighbor_only":null,"neighbor_ref":"root_000936/B001","relation_type":"synonym","shared_zone":"Her iki dal da sınırın veya ölçünün aşılmasını, itaatsizliği ve birini bu duruma sürükleyen kullanımı kapsar."},{"boundary_match":"partial","distinction":"Odak dal itaatsizlik ve azgınlık ekseninde kişisel ve ettirgen türevler kurar; komşu dal ise amaçsız veya haksız kullanım ve savurganlık alanlarına uzanır.","focus_only":"İtaatsizlikte azgınlaşmayı, birini azdırmayı ve sınır tanımaz zorba kişiyi de kapsar.","gloss":"ölçüsüzce sınırı aşma","neighbor_only":"Harcama, öldürme, yeme ve su kullanımı gibi alanlarda bir şeyi hak veya yarar dışında kullanmayı özellikle kapsar.","neighbor_ref":"root_000699/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı, geçerli sınırı veya uygun ölçüyü aşan davranıştır."},{"boundary_match":"partial","distinction":"Komşu dalın ayırt edici koşulu nimet karşısındaki şımarma ve coşkudur; odak dal için böyle bir neden veya duygu gerekli değildir.","focus_only":"Nimet veya sevinç koşulu olmadan genel sınır aşımını ve itaatsizliği kapsar.","gloss":"şımararak ölçüyü aşma","neighbor_only":"Özellikle nimet karşısındaki aşırı sevinç, şımarıklık ve nimeti küçümseme durumunu kapsar.","neighbor_ref":"root_000125/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin davranışta ölçüyü aşarak taşkınlaşmasını içerebilir."},{"boundary_match":"partial","distinction":"Odak dal davranışsal ve ahlaki sınır aşımıdır; komşu dal yalnızca belirli maddi güçlerle kurulan söz öbeklerinde kabarma ve bastırma olayını anlatır.","focus_only":"İtaatsizlikte davranış sınırını aşmayı ve bundan türeyen zorba kişi anlamını taşır.","gloss":"sınırı aşan taşkınlık","neighbor_only":"Su, sel, deniz, kan, ses veya rüzgarın miktar ya da güç bakımından kabarıp bastırmasını bildirir.","neighbor_ref":"root_000937/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da olağan sınırın veya ölçünün aşılması ortak bir kavramsal zemin oluşturur."}],"source_phrase_ar":"مجاوزة الحد في العصيان (maqayis;mufradat); جاوز الحد وكل مجاوز حده في العصيان (sihah); كل شيء جاوز القدر فقد طغا (tahdhib); أطغاه المال أي جعله طاغيا (sihah); الطاغية الجبار العنيد (tahdhib)","source_summary":"Kaynakların birleşen anlatımı, temel anlamı sınırın veya belirlenmiş ölçünün aşılması olarak kurar ve insan davranışında itaatsizliği öne çıkarır. Aynı kanıt, başkasını bu duruma sürükleme ile sınır tanımaz zorba kişiyi bildiren türemiş kullanımları da içerir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه طغى وطاغ والطغيان والطغوان والطغوى وأطغاه إذا حمله على الطغيان والطاغية بمعنى الجبار","what_is_not_ar":"ليس فيضان الماء ولا الطاغوت ولا الصخرة الملساء"},"support_links":["sup_2eb24e1ef5474661de6d","sup_f960e33e9b5593b03180"]},{"boundary":"Bu dal yalın bir kök anlamı değil, su, sel, deniz, kan, ses veya rüzgar öznesiyle kurulan taşma ve bastırma kullanımlarıdır.","branch_kind":"collocation","branch_ref":"root_000937/B002","candidate_links":[{"candidate_id":"cand_816617fd62e44f6be880","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","surface_ar":"طَغْوَىٰ"}],"gloss":"ölçüyü aşarak kabarıp bastırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su veya sel, olağan miktarı ve düzeyi aşacak ölçüde çoğalır ve yükselir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Deniz kullanımında dalgaların şiddetle kabarıp yükselmesi ve önündekileri sürüklemesi öne çıkar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kan kullanımında sıvının coşması ve basınçla kabarması anlatılır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Ses veya rüzgar kullanımında olağan ölçüyü aşan kuvvetin üstün gelip bastırması anlatılır."}}],"root_ar":"ط غ ي","root_id":"root_000937","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kanıtlanan su, sel, deniz, kan, ses ve rüzgar söz öbeklerinin ortak taşma ve baskın gelme yapısını karşılar.","boundary_detail":"Bu dal yalın bir kök anlamı değil, su, sel, deniz, kan, ses veya rüzgar öznesiyle kurulan taşma ve bastırma kullanımlarıdır.","branch_image_ar":"علو الماء والقوة الجارفة","concept_gloss":"ölçüyü aşarak kabarıp bastırma","contextual_glosses":[{"applicability":"Selin olağan miktardan çok su taşıyarak yükseldiği bağlamlarda doğal bir cümle karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deniz, kan, ses ve rüzgarla kurulan diğer söz öbeği kullanımlarını kapsamaz.","preserves":"Sel suyunun çokluğunu, yükselmesini ve taşmasını korur."},"facet_ids":["F001"],"text":"sel bol suyla kabarıp taştı","usage_role":"contextual"},{"applicability":"Deniz dalgalarının yükseldiği ve kuvvetle sürüklediği olay bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sel, su, kan, ses ve rüzgarla kurulan diğer kullanımlar bu karşılıkta yer almaz.","preserves":"Denizin dalga kabarmasını, yükselmesini ve sürükleyici gücünü korur."},"facet_ids":["F002"],"text":"deniz coşup önündekileri sürükledi","usage_role":"contextual"},{"applicability":"Kanın basınçla kabardığını ve şiddetle hareketlendiğini anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Su, sel, deniz, ses ve rüzgarla kurulan kullanımları dışarıda bırakır.","preserves":"Kanla sınırlı coşma ve kabarma görünümünü korur."},"facet_ids":["F003"],"text":"kan kabarıp coştu","usage_role":"contextual"},{"applicability":"Sesin veya rüzgarın olağan ölçüyü aşan bir güçle her şeye üstün geldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıvıların çoğalma, kabarma ve sürükleme görünümlerini kapsamaz.","preserves":"Ses ve rüzgarın ölçüyü aşan baskın kuvvetini korur."},"facet_ids":["F004"],"text":"çığlık ya da rüzgar baskın geldi","usage_role":"contextual"}],"definition":"Su, sel, deniz veya kanın olağan miktarını ya da düzeyini aşarak kabarması, coşması ve kimi bağlamlarda önündekileri sürüklemesidir. Ses ve rüzgarla kurulan kullanımlarda, ölçüyü aşan gücün baskın gelmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su veya sel, olağan miktarı ve düzeyi aşacak ölçüde çoğalır ve yükselir."},{"facet_id":"F002","role":"specialization","statement":"Deniz kullanımında dalgaların şiddetle kabarıp yükselmesi ve önündekileri sürüklemesi öne çıkar."},{"facet_id":"F003","role":"specialization","statement":"Kan kullanımında sıvının coşması ve basınçla kabarması anlatılır."},{"facet_id":"F004","role":"extension","statement":"Ses veya rüzgar kullanımında olağan ölçüyü aşan kuvvetin üstün gelip bastırması anlatılır."}],"identity_rationale":"Kaynak ifadesi, selin bol suyla gelmesini, suyun belirlenmiş miktarı aşmasını, deniz dalgalarının kabarmasını, kanın coşmasını ve su ya da denizin yükselip önündekileri sürüklemesini açıkça bir arada verir. Ses ve rüzgarın ölçüyü aşan güçle bastırması da aynı maddi kuvvet uzantısı içinde desteklenir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"sel bol suyla geldi ve kabardı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"su olağan düzeyi aşıp yükseldi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"denizin dalgaları kabarıp yükseldi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kan kabarıp coştu"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"çığlık ya da rüzgar ölçüyü aşan güçle baskın geldi"}],"lexicalization_note":"Tanım yalnızca kanıtlanan söz öbeklerine bağlıdır; kabarma ve bastırma anlamı yalın biçime genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşleşen dal ile itici sel gücü, deniz dalgası ve doğa olaylarının şiddetlenmesi arasındaki dört sınır karşılaştırması yeterli bulundu.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda çekirdek, katılımcılar ve maddi kuvvet uzantısı bakımından anlamlı bir sınır farkı görünmez.","focus_only":null,"gloss":"maddi gücün ölçüyü aşması","neighbor_only":null,"neighbor_ref":"root_000936/B002","relation_type":"synonym","shared_zone":"Her iki dal su, sel, deniz ve kanın olağan miktarı aşarak kabarmasını ve benzer maddi güç uzantılarını kapsar."},{"boundary_match":"partial","distinction":"Odak dalda temel sınır olağan miktar veya gücün aşılmasıdır; komşu dalda ise ögelerin birbirini iterek ilerlemesi ve kalabalık hareketi belirleyicidir.","focus_only":"Suyun düzeyi aşmasını, deniz dalgalarının kabarmasını, kanın coşmasını ve ses ya da rüzgarın bastırmasını kapsar.","gloss":"itici taşkın güç","neighbor_only":"Büyük sel ve dalga yanında insanların, yürüyüşün veya koşan atın birbirini iten yoğun hareketini de kapsar.","neighbor_ref":"root_000480/B005","relation_type":"near_synonym","shared_zone":"Büyük selin veya dalganın yoğun ve itici hareketi iki dalın ortak alanıdır."},{"boundary_match":"field_only","distinction":"Komşu dal su biçiminin adı ve betimidir; odak dal ise yalnız belirli söz öbeklerinde dalganın olağan ölçüyü aşarak coşmasını bildirir.","focus_only":"Denizin dışında sel, su, kan, ses ve rüzgarı da kapsar; olağan ölçüyü aşan güç belirleyicidir.","gloss":"deniz dalgası","neighbor_only":"Deniz dalgasını veya rüzgarın su yüzeyinde kaldırdığı tabakaları, ölçü aşımı şartı olmadan adlandırır.","neighbor_ref":"root_000023/B003","relation_type":"same_field","shared_zone":"İki dal da deniz yüzeyinde yükselen ve hareketlenen suyu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal sınırı aşan kabarma ve baskın gelmeye bağlı söz öbekleridir; komşu dal daha genel biçimde hava olaylarının ve sıcaklık koşullarının şiddetlenmesini anlatır.","focus_only":"Sıvının miktar ve düzey aşımını, ayrıca sesin baskın gelmesini içerir.","gloss":"şiddetlenip coşma","neighbor_only":"Yağmurun düşüşü ile sıcak, soğuk ve rüzgarın şiddetlenmesini ölçü aşımı veya sürükleme şartı olmadan anlatır.","neighbor_ref":"root_000810/B005","relation_type":"near_neighbor","shared_zone":"Rüzgarın kuvvetlenmesi ve doğa olaylarının olağanın üstünde şiddet kazanması ortak alandır."}],"source_phrase_ar":"طغى السيل إذا جاء بماء كثير (maqayis;sihah); طغى الماء خروجه عن المقدار (maqayis); طغى البحر هاجت أمواجه (maqayis;sihah); طغى الدم تبيغ (maqayis;sihah); طغا البحر والماء إذا علا كل شيء فاجترفه (tahdhib); استعير الطغيان فيه لتجاوز الماء الحد (mufradat)","source_summary":"Toplu kanıt, söz öbeği içindeki öznenin olağan miktarı veya gücü aşmasını ortaklaştırır. Suda ve selde çokluk ile yükselme, denizde dalga kabarması ve sürükleme, kanda coşma, ses ve rüzgarda ise baskın güç bu çekirdeğin ayrı gerçekleşmeleridir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه طغيان الماء والسيل والبحر والدم وما علا فاجترف من صيحة أو ريح","what_is_not_ar":"ليس العصيان المجرد ولا الطاغوت ولا الصخرة الملساء"},"support_links":["sup_80adfaa6f7c0e8ecf39a"]},{"boundary":"Bu kategori sınır aşan kişiyi bağımsız olarak kapsar; ancak her zorbayı veya yalnızca azgın niteliği taşıyan kişiyi otomatik olarak kapsamaz. Yanlış yola önderlik eden, tapınılan veya iyilikten saptıran kişi ya da güç de bu kapsamdadır.","branch_kind":"bare","branch_ref":"root_000937/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","surface_ar":"طَغْوَىٰ"}],"gloss":"yanlış yolun önderi, tapınılan sahte varlık veya saptırıcı zorba güç","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yanlış yola önderlik eden ve başkalarını iyilik yolundan çeviren kişi, varlık veya güç temel kategoriyi oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tanrı dışında kendisine tapınılan herhangi bir varlık bu kategoriye girer."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Falcı, büyücü ve kötücül ya da başkaldıran doğaüstü varlıklar, saptırıcı işlevleriyle bu kategorinin örnekleridir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Sınırı aşan kişi ile başkalarını iyi yoldan uzaklaştıran kişi ya da güç, birbirine bağlanmadan aynı kategori adıyla anılabilir."}}],"root_ar":"ط غ ي","root_id":"root_000937","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kategorinin önderlik, Tanrı dışında tapınılma ve iyilikten saptırma biçimindeki üç temel gerçekleşmesini birlikte karşılar.","boundary_detail":"Bu kategori sınır aşan kişiyi bağımsız olarak kapsar; ancak her zorbayı veya yalnızca azgın niteliği taşıyan kişiyi otomatik olarak kapsamaz. Yanlış yola önderlik eden, tapınılan veya iyilikten saptıran kişi ya da güç de bu kapsamdadır.","branch_image_ar":"الطاغوت رأس الضلالة","concept_gloss":"yanlış yolun önderi, tapınılan sahte varlık veya saptırıcı zorba güç","contextual_glosses":[{"applicability":"Bir kişinin veya varlığın sapmayı yönetip başkalarını iyilikten uzaklaştırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Önderlik etmeyen tapınma nesneleri ile falcı, büyücü ve doğaüstü varlık örneklerini bütünüyle kapsamaz.","preserves":"Saptırıcı önderlik ve iyilik yolundan çevirme işlevini korur."},"facet_ids":["F001","F004"],"text":"yanlış yolun önderi","usage_role":"contextual"},{"applicability":"Sözcüğün Tanrı yerine bağlılık ve tapınma yöneltilen herhangi bir varlığı anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tapınılmadan da insanları iyilikten saptıran önder, falcı, büyücü veya zorba kişi kullanımlarını dışarıda bırakır.","preserves":"Tanrı dışında tapınılma ölçütünü açık ve doğal biçimde korur."},"facet_ids":["F002"],"text":"Tanrı dışında tapınılan varlık","usage_role":"explanatory"},{"applicability":"Kötücül doğaüstü bir varlığın veya zorlayıcı gücün insanı iyi yoldan uzaklaştırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tapınılan varlık ve insan olan falcı, büyücü ya da yanlış yol önderinin bütün kullanımlarını kapsamaz.","preserves":"Kötücül güç ve iyilik yolundan saptırma işlevini korur."},"facet_ids":["F001","F003","F004"],"text":"iyilikten saptıran kötücül güç","usage_role":"contextual"}],"definition":"Yanlış yolun başı sayılan, sınır aşan, insanları iyilikten çeviren veya Tanrı dışında kendisine tapınılan kişi, varlık ya da güçtür. Falcı, büyücü ve kötücül doğaüstü varlıklar bu işlevleri taşıdıklarında kategoriye girer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yanlış yola önderlik eden ve başkalarını iyilik yolundan çeviren kişi, varlık veya güç temel kategoriyi oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Tanrı dışında kendisine tapınılan herhangi bir varlık bu kategoriye girer."},{"facet_id":"F003","role":"example","statement":"Falcı, büyücü ve kötücül ya da başkaldıran doğaüstü varlıklar, saptırıcı işlevleriyle bu kategorinin örnekleridir."},{"facet_id":"F004","role":"extension","statement":"Sınırı aşan kişi ile başkalarını iyi yoldan uzaklaştıran kişi ya da güç, birbirine bağlanmadan aynı kategori adıyla anılabilir."}],"identity_rationale":"Kaynak ifadesi yanlış yolun önderini merkezde tutmakla birlikte kapsamı tek bir önder türüne indirmez; falcıyı, büyücüyü, kötücül doğaüstü varlığı, Tanrı dışında tapınılan varlığı, sınır aşan kişiyi ve iyilik yolundan çevireni de aynı ad altında toplar. Dal bu geniş ve işlevsel sınır açıkça korunursa geçerlidir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yanlış yolun önderi, Tanrı dışında tapınılan varlık veya iyilikten saptıran zorba güç"}],"lexicalization_note":"Tanım, sözlük biriminin yalın kategori anlamını verir ve başka dallardaki su taşkınlığı ya da yıkıcı olay anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşleşen dal ile sınır aşan zorba, belirli tapınma nesnesi ve kibir alanı arasındaki dört karşılaştırma kategori sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak alan geniştir; ancak odak dalın sınır aşan kişiyi ve iyilikten çevireni bağımsız olarak kapsaması tam ikameyi engeller.","focus_only":"Odak dal, her sınır aşan kişiyi ve iyilik yolundan çevireni ayrıca kapsar.","gloss":"sapmanın önderi ve tapınılan varlık","neighbor_only":null,"neighbor_ref":"root_000936/B003","relation_type":"near_synonym","shared_zone":"Her iki dal yanlış yolun önderini, Tanrı dışında tapınılan varlığı ve falcı ya da kötücül güç gibi örnekleri kapsar."},{"boundary_match":"partial","distinction":"Odak dal saptırıcı veya tapınılan bir varlık kategorisidir; komşu dal ise böyle bir dini ya da yönlendirici işlev gerektirmeyen sınır aşımıdır.","focus_only":"Tapınılan varlığı, yanlış yolun önderini ve iyilikten saptıran doğaüstü ya da beşeri gücü kapsar.","gloss":"sınır tanımaz saptırıcı güç","neighbor_only":"Genel sınır veya ölçü aşımını, itaatsizliği ve bundan türeyen zorba kişi niteliğini kapsar.","neighbor_ref":"root_000937/B001","relation_type":"near_neighbor","shared_zone":"Sınır tanımayan zorba bir kişi aynı zamanda başkalarını yanlış yola sürüklediğinde iki kategori kesişebilir."},{"boundary_match":"field_only","distinction":"Komşu dal belirli bir nesnenin özel adıdır; odak dal ise ad, tür ve tekillik ayrımı yapmadan işlevsel bir genel kategori kurar.","focus_only":"Herhangi bir yanlış yol önderini, saptırıcı gücü veya Tanrı dışında tapınılan varlığı kapsayan genel kategoridir.","gloss":"tapınılan belirli nesne","neighbor_only":"Belirli bir topluluğa ait tek bir tapınma nesnesinin özel adını ve ona ilişkin anlatıyı kapsar.","neighbor_ref":"root_000032/B005","relation_type":"same_field","shared_zone":"İki dal da Tanrı dışında kendisine tapınılan bir varlığa uygulanabilir."},{"boundary_match":"partial","distinction":"Komşu dal bir büyüklük veya kibir niteliğidir; odak dal ise yanlış yola yönelten ya da tapınılan kişi, varlık veya güç kategorisidir.","focus_only":"Yanlış yola önderlik, tapınılma ve başkalarını iyilikten çevirme işlevlerini gerektirir.","gloss":"kibirli saptırıcı","neighbor_only":"Büyüklük, yücelik ve kişinin gerçeği kabul etmeyen kibri üzerinde durur; saptırma veya tapınılma gerektirmez.","neighbor_ref":"root_001281/B006","relation_type":"near_neighbor","shared_zone":"Kibirli ve gerçeğe direnen bir zorba, aynı zamanda başkalarını saptırdığında iki alan kesişebilir."}],"source_phrase_ar":"الطاغوت الكاهن والشيطان وكل رأس في الضلالة (sihah); كل معبود من دون الله جبت وطاغوت (tahdhib); الطاغوت الشيطان (tahdhib); الطاغوت عبارة عن كل متعد وكل معبود من دون الله (mufradat); الساحر والكاهن والمارد من الجن والصارف عن طريق الخير طاغوتا (mufradat)","source_summary":"Toplu kaynak anlatımı tek bir kişi türünden daha geniş bir işlevsel kategori kurar: yanlış yolun önderi, Tanrı dışında tapınılan varlık, kötücül doğaüstü güç, falcı, büyücü, sınır aşan kişi ve iyilikten saptıran kişi bu kapsamda birleşir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه الطاغوت للكاهن والشيطان وكل رأس في الضلالة وكل معبود من دون الله والمتعدي الصارف عن طريق الخير","what_is_not_ar":"ليس كل طاغ ولا طغيان الماء ولا الصاعقة المسماة بالطاغية"},"support_links":[]},{"boundary":"Dal yalnızca zorba kişiyi anlatmaz; yıkıcı olayı veya kimi yorumda yıkıma neden olan sınır aşımını bildirir.","branch_kind":"bare","branch_ref":"root_000937/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","surface_ar":"طَغْوَىٰ"}],"gloss":"yıkıma götüren ezici olay veya sınır aşımı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ortak eksen, bir topluluğun yok oluşuna bağlanan ezici olay veya nedendir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yorum, yıkım aracını şiddetli yıldırım ya da ceza bildiren öldürücü çığlık olarak belirler."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir yorum, sözcüğü insanları yok eden büyük su baskınına gönderme sayar."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir diğer yorum, sözcüğü yıkım aracı değil, insanların yıkıma yol açan kendi sınır aşımının adlaşmış biçimi sayar."}}],"root_ar":"ط غ ي","root_id":"root_000937","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yıkıcı yıldırım, ceza çığlığı, büyük su baskını ve yıkıma neden olan davranış yorumu birlikte söz konusu olduğunda kullanılır.","boundary_detail":"Dal yalnızca zorba kişiyi anlatmaz; yıkıcı olayı veya kimi yorumda yıkıma neden olan sınır aşımını bildirir.","branch_image_ar":"الطاغية عذاب غالب","concept_gloss":"yıkıma götüren ezici olay veya sınır aşımı","contextual_glosses":[{"applicability":"Yok edici olayın gökten gelen şiddetli bir vuruş veya öldürücü bir ses olarak yorumlandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Büyük su baskını ve insanların kendi sınır aşımı biçimindeki diğer yorumları dışarıda bırakır.","preserves":"Yıldırım ve öldürücü ses yoluyla gerçekleşen ezici yıkım yorumunu korur."},"facet_ids":["F001","F002"],"text":"yıkıcı yıldırım ya da ceza çığlığı","usage_role":"explanatory"},{"applicability":"Yıkım aracının geniş çaplı ve ezici bir su baskını olarak yorumlandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yıldırım, öldürücü ses ve davranışsal sınır aşımı yorumlarını kapsamaz.","preserves":"Topluluğu yok eden büyük su baskını yorumunu açıkça korur."},"facet_ids":["F001","F003"],"text":"yok eden büyük su baskını","usage_role":"explanatory"},{"applicability":"Sözcüğün yıkım aracını değil, toplumun kendi taşkın davranışını adlandırdığı yorumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yıldırım, ceza çığlığı ve büyük su baskını biçimindeki yıkıcı olay yorumlarını dışarıda bırakır.","preserves":"İnsanların kendi sınır aşımının yıkıma neden olması ilişkisini korur."},"facet_ids":["F001","F004"],"text":"yıkıma yol açan sınır aşımı","usage_role":"explanatory"}],"definition":"Bir topluluğu yok eden ezici olay veya yıkıma götüren sınır aşımıdır. Kaynak yorumlarında olay, yıkıcı yıldırım ya da ceza çığlığı veya büyük su baskını olarak; neden ise insanların kendi taşkın davranışı olarak açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ortak eksen, bir topluluğun yok oluşuna bağlanan ezici olay veya nedendir."},{"facet_id":"F002","role":"source_variant","statement":"Bir yorum, yıkım aracını şiddetli yıldırım ya da ceza bildiren öldürücü çığlık olarak belirler."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir yorum, sözcüğü insanları yok eden büyük su baskınına gönderme sayar."},{"facet_id":"F004","role":"source_variant","statement":"Bir diğer yorum, sözcüğü yıkım aracı değil, insanların yıkıma yol açan kendi sınır aşımının adlaşmış biçimi sayar."}],"identity_rationale":"Kaynak ifadesi tek ve bütünüyle birleşmiş bir ceza türü vermez; aynı biçimi yıkıcı yıldırım veya ceza çığlığı, büyük su baskını ve insanların yıkıma yol açan kendi sınır aşımı olarak ayrı biçimlerde açıklar. Dal, bu yorum farklarını ezici bir yıkım ekseni altında koruduğu sürece kullanılabilir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yıkıcı yıldırım veya ceza çığlığı, büyük su baskını ya da yıkıma yol açan sınır aşımı"}],"lexicalization_note":"Tanım, yalın sözlük biriminin kaynaklarda verilen olay ve neden yorumlarını korur; zorba kişi anlamını bu dala taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yakın eşleşen ceza dalı ile yıldırım, yok oluş ve kapsayıcı bela alanları arasındaki dört karşılaştırma yorum farklarını yeterince gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, yıkıcı olay yorumlarının yanında dilbilgisel olarak insanların kendi sınır aşımını bildiren neden yorumunu açıkça ayrı tutar.","focus_only":"Sözcüğü kimi yorumda insanların yıkıma yol açan kendi sınır aşımının adı sayar.","gloss":"ezici yıkım veya nedeni","neighbor_only":"Bütün kapsamı baskın ceza başlığı altında toplar ve olay ile neden arasındaki yorum farkını daha az belirgin bırakır.","neighbor_ref":"root_000936/B005","relation_type":"near_synonym","shared_zone":"İki dal da yıkıcı yıldırım, ceza çığlığı ve büyük su baskınıyla bağlantılı ezici yok oluşu kapsar."},{"boundary_match":"partial","distinction":"Komşu dal yıldırım olayının genel alanıdır; odak dal belirli bir yıkım anlatısındaki sözcüğün yıldırım yanında su baskını ve davranışsal neden yorumlarını da taşır.","focus_only":"Büyük su baskınını ve yıkıma neden olan davranışsal sınır aşımını da kapsar.","gloss":"yıkıcı göksel vuruş","neighbor_only":"Göksel gürültü, şiddetli vuruş, ateş, ölüm veya ceza içerebilen yıldırım olayının kendisini daha genel biçimde anlatır.","neighbor_ref":"root_000864/B002","relation_type":"near_neighbor","shared_zone":"Yok edici yıldırım veya şiddetli göksel ses iki dalın kesiştiği olaydır."},{"boundary_match":"partial","distinction":"Odak dal yıkımın ezici aracını veya nedenini öne çıkarır; komşu dal ise yok oluş ve bozulma sonucunun kendisini daha geniş biçimde adlandırır.","focus_only":"Yok oluşa yol açan yıldırım, ses, su baskını veya sınır aşımı biçimindeki araç ya da nedeni bildirir.","gloss":"yok oluş ve bozulma","neighbor_only":"Bir şeyin veya kişinin yok olmuş, bozulmuş ya da geçersiz hale gelmiş durumunu ve bu duruma ilişkin yargıyı kapsar.","neighbor_ref":"root_000164/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal yıkım, yok olma ve ağır ceza sonucuyla ilişkilidir."},{"boundary_match":"field_only","distinction":"Komşu dalın çekirdeği kapsayıp örtmedir; odak dalın çekirdeği ise yıkıma bağlanan ezici olay veya davranışsal nedendir.","focus_only":"Yıldırım, öldürücü ses, büyük su baskını veya davranışsal neden gibi belirli yıkım yorumlarını taşır.","gloss":"her yanı kaplayan bela","neighbor_only":"İnsanları bütünüyle kaplayan kıyamet, bela, yaygın sıkıntı veya kişiyi tutan hastalık alanlarını kapsar.","neighbor_ref":"root_001088/B002","relation_type":"same_field","shared_zone":"İki dal da topluluğu kuşatan ağır bir ceza veya yıkıcı olay bağlamında kullanılabilir."}],"source_phrase_ar":"الطاغية الصاعقة ويعني صيحة العذاب (sihah); أهلكوا بالطاغية أي بطغيانهم مصدر على فاعلة (tahdhib); فأهلكوا بالطاغية فإشارة إلى الطوفان (mufradat)","source_summary":"Kanıt aynı kullanım için üç açıklama sunar: öldürücü yıldırım veya ceza çığlığı, yıkıcı büyük su baskını ve insanların kendi sınır aşımı. Bunlar yıkım bağlantısında birleşir, fakat olayın aracı ile yıkımın davranışsal nedeni aynılaştırılmamalıdır.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه الطاغية إذا أريد بها الصاعقة أو صيحة العذاب أو الطوفان أو مصدر الطغيان في الهلاك","what_is_not_ar":"ليس الطاغية بمعنى الجبار ولا مطلق الطاغوت"},"support_links":[]},{"boundary":"Dal kaya yüzeyi, dağ doruğu ve yüksek yer adlarıyla sınırlıdır; sınır aşımı, su taşkınlığı ve saptırıcı güç anlamlarını içermez.","branch_kind":"bare","branch_ref":"root_000937/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","surface_ar":"طَغْوَىٰ"}],"gloss":"pürüzsüz kaya yüzeyi, dağ doruğu veya yüksek yer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adın bir kullanımı, yüzeyi düz ve kaygan olan kaya parçasını bildirir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kayanın pürüzsüzlüğü, üzerine konmaya çalışan yırtıcı kuşun pençesini geri sektirecek kadar belirgindir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı adın başka bir kullanımı dağın en yüksek bölümünü, yani doruğunu bildirir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Aynı kökten farklı bir ad biçimi, türü belirtilmeyen herhangi bir yüksek yeri bildirir."}}],"root_ar":"ط غ ي","root_id":"root_000937","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dal içindeki iki ad biçiminin pürüzsüz kaya, dağın en yüksek bölümü ve genel yüksek yer anlamlarını birlikte gösterir.","boundary_detail":"Dal kaya yüzeyi, dağ doruğu ve yüksek yer adlarıyla sınırlıdır; sınır aşımı, su taşkınlığı ve saptırıcı güç anlamlarını içermez.","branch_image_ar":"الطغية الصفاة الملساء","concept_gloss":"pürüzsüz kaya yüzeyi, dağ doruğu veya yüksek yer","contextual_glosses":[{"applicability":"Yüzeyinin düzgünlüğü ve kayganlığı nedeniyle pençenin tutunamadığı kaya anlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dağın doruğu ve genel yüksek yer anlamlarını dışarıda bırakır.","preserves":"Kayanın pürüzsüz ve kaygan yüzey niteliğini korur."},"facet_ids":["F001","F002"],"text":"pürüzsüz kaya yüzeyi","usage_role":"contextual"},{"applicability":"Aynı ad biçiminin dağın en yüksek bölümünü anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Pürüzsüz kaya yüzeyi ve türü belirtilmeyen yüksek yer anlamlarını kapsamaz.","preserves":"Dağın en yüksek bölümü olma niteliğini açıkça korur."},"facet_ids":["F003"],"text":"dağın doruğu","usage_role":"contextual"},{"applicability":"Aynı kökten farklı ad biçiminin genel olarak çevresinden yüksek bir yeri anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Pürüzsüz kaya yüzeyi ve özel olarak dağın doruğu olan diğer ad kullanımlarını dışarıda bırakır.","preserves":"Türü belirtilmeyen bir yerin çevresine göre yüksek olmasını korur."},"facet_ids":["F004"],"text":"yüksek yer","usage_role":"contextual"}],"definition":"Pürüzsüz bir kaya yüzeyi ya da dağın en yüksek bölümüdür; aynı kökten başka bir ad biçimi ise herhangi bir yüksek yeri bildirir. Kaya anlamında yüzey öylesine kaygandır ki yırtıcı kuşun pençesi geri seker.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adın bir kullanımı, yüzeyi düz ve kaygan olan kaya parçasını bildirir."},{"facet_id":"F002","role":"example","statement":"Kayanın pürüzsüzlüğü, üzerine konmaya çalışan yırtıcı kuşun pençesini geri sektirecek kadar belirgindir."},{"facet_id":"F003","role":"source_variant","statement":"Aynı adın başka bir kullanımı dağın en yüksek bölümünü, yani doruğunu bildirir."},{"facet_id":"F004","role":"source_variant","statement":"Aynı kökten farklı bir ad biçimi, türü belirtilmeyen herhangi bir yüksek yeri bildirir."}],"identity_rationale":"Kaynak ifadesi pürüzsüz kaya yüzeyini, dağın en yüksek bölümünü ve aynı kökten başka bir biçimle herhangi bir yüksek yeri açıkça sıralar; kayanın kayganlığına yırtıcı kuş pençesinin tutunamaması da pürüzsüzlük niteliğini doğrular. Sağlanan dal çerçevesi bu üç kullanımı ayrıştırmaya elverişlidir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"pürüzsüz ve kaygan kaya yüzeyi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"dağın doruğu"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yüksek yer"}],"lexicalization_note":"Tanım yalın ad biçimlerinin üç yer ve yüzey anlamını korur; bunları sınır aşma çekirdeğinden türetmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşleşen dal ile pürüzsüz kaya, dağ bölümü, yerden yükselti ve sert yüksek arazi arasındaki beş karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda çekirdek, ad biçimleri ve yer kapsamı bakımından anlamlı bir sınır farkı görünmez.","focus_only":null,"gloss":"pürüzsüz kaya veya yüksek yer","neighbor_only":null,"neighbor_ref":"root_000936/B006","relation_type":"synonym","shared_zone":"Her iki dal pürüzsüz kaya yüzeyini, dağın en yüksek bölümünü ve aynı kökten adla yüksek yeri kapsar."},{"boundary_match":"partial","distinction":"Odak dal kaya yüzeyi yanında dağ doruğu ve yüksek yer anlamlarını taşır; komşu dal ise kayanın sertliği, genişliği ve yüzey temizliği üzerinde daha ayrıntılıdır.","focus_only":"Dağın doruğu ve genel yüksek yer anlamlarını da kapsar.","gloss":"pürüzsüz sert kaya","neighbor_only":"Geniş, sert ve pürüzsüz kayanın kumdan, çamurdan ve topraktan arınmış olmasını ve adı verilen belirli bir yeri de kapsar.","neighbor_ref":"root_000873/B006","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı yüzeyi pürüzsüz olan sert kaya parçasıdır."},{"boundary_match":"partial","distinction":"Odak dalda dağa ilişkin bölüm doruktur; komşu dal ise dağın bütününü veya özellikle orta kısmını bildirir.","focus_only":"Dağın yalnız en yüksek bölümünü, ayrıca pürüzsüz kaya ve genel yüksek yeri kapsar.","gloss":"dağ ve orta bölümü","neighbor_only":"Dağın bütünü ile dağların orta bölümünü adlandırır.","neighbor_ref":"root_000840/B017","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir dağın bölümü veya dağlık yükseltiyle ilişkilidir."},{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği zeminden yükselmiş biçimdir; odak dal ise belirli ad biçimleriyle pürüzsüz kaya, dağ doruğu veya yüksek yer kategorilerini taşır.","focus_only":"Pürüzsüz kaya yüzeyini ve özellikle dağın doruğunu adlandırabilir.","gloss":"yerden yükselen tümsek","neighbor_only":"Toprağın tümsek, tepecik, kum sırtı veya rüzgarla oluşmuş kabarıklık gibi yükselen biçimlerini kapsar.","neighbor_ref":"root_000298/B001","relation_type":"near_neighbor","shared_zone":"Çevresindeki zeminden yüksek olan bir yer iki dalın ortak alanına girebilir."},{"boundary_match":"partial","distinction":"Odak dalın ayırt edici özellikleri pürüzsüz kaya yüzeyi ile doruk konumudur; komşu dal sert ve yüksek arazi türlerini daha genel biçimde toplar.","focus_only":"Kayada pürüzsüz yüzeyi ve dağda en yüksek bölümü özellikle ayırt eder.","gloss":"sert yüksek arazi","neighbor_only":"Sert veya kaba yüksek araziyi, küçük tepeyi, taşları ve belirgin arazi işaretlerini daha geniş biçimde kapsar.","neighbor_ref":"root_000258/B004","relation_type":"near_neighbor","shared_zone":"Sert, taşlık ve çevresine göre yüksek bir yer iki dalın kapsamında kesişebilir."}],"source_phrase_ar":"الطغية الصفاة الملساء (maqayis;tahdhib); الطغية أعلى الجبل (sihah); كل مكان مرتفع طغوة (sihah); تنبي العقاب لملاستها (sihah)","source_summary":"Toplu kanıt, pürüzsüz kaya ile dağın doruğunu aynı ad biçiminin iki kullanımı olarak, herhangi bir yüksek yeri ise aynı kökten başka bir ad biçiminin anlamı olarak verir. Yırtıcı kuşun pençesinin geri sekmesi, kaya yüzeyinin kayganlığına ilişkin açıklayıcı örnektir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الطغية للصفاة الملساء وأعلى الجبل والطغوة للمكان المرتفع","what_is_not_ar":"ليس مجاوزة الحد ولا الطغيان ولا الطاغوت"},"support_links":[]},{"boundary":"Dal, gerçeğe aykırı söz ve davranışı kapsar; başkasını yalancılıkla niteleme eylemini ya da özel kalıpların bağımsız anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001290/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"91:11:1:1","qac_word_ref":"91:11:1","surface_ar":"كَذَّبَتْ"}],"gloss":"sözde veya davranışta doğruluğa aykırılık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğruluğa aykırılık hem söylenen bir sözde hem de yapılan bir davranışta gerçekleşebilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu niteliği taşıyan veya onu sıkça gösteren kişi, yalan söyleyen kişi olarak adlandırılır."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem söz hem davranış alanındaki bütün yalın anlam çekirdeğini karşılayan açıklayıcı üst karşılıktır.","boundary_detail":"Dal, gerçeğe aykırı söz ve davranışı kapsar; başkasını yalancılıkla niteleme eylemini ya da özel kalıpların bağımsız anlamlarını kapsamaz.","branch_image_ar":"خلاف الصدق","concept_gloss":"sözde veya davranışta doğruluğa aykırılık","contextual_glosses":[{"applicability":"Bağlamın söz veya davranıştaki doğruluğa aykırılığı zaten belirginleştirdiği doğal kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğruluğa aykırılık çekirdeğini ve kişiye yüklenebilen niteliği doğal Türkçeyle korur."},"facet_ids":["F001","F002"],"text":"yalan","usage_role":"general"}],"definition":"Bir sözün veya davranışın doğruluğa aykırı olmasıdır. Bu niteliği taşıyan kişi, yalan söyleyen ya da yalanı çokça tekrarlayan biri olarak betimlenebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğruluğa aykırılık hem söylenen bir sözde hem de yapılan bir davranışta gerçekleşebilir."},{"facet_id":"F002","role":"specialization","statement":"Bu niteliği taşıyan veya onu sıkça gösteren kişi, yalan söyleyen kişi olarak adlandırılır."}],"identity_rationale":"Kaynak ifadesi anlamı doğruluğun karşıtı olarak kurar ve bu karşıtlığın hem sözde hem davranışta gerçekleşebildiğini açıkça belirtir. Kişiyi bu nitelikle betimleyen biçimler aynı çekirdeğe bağlıdır; birini yalancı sayma eylemi ise ayrı dalın konusudur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sözde veya davranışta doğruluğa aykırılık; yalan"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yalancı; çok yalan söyleyen kişi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"uydurma söz; yalanlar"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"özürlere kaçınılmaz olarak yalan karışır"}],"lexicalization_note":"Tanım yalın anlam çekirdeğini verir; kişi betimleyen türevler ile özürlere ilişkin kalıp yalnız kendi sözcüksel karşılıklarında gösterilir ve yalın anlama eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yalanla en kolay karışan beş anlam yayımlandı, yalnızca aynı senaryoda bulunan özel kalıplar ve uzak tematik adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gerçeğe aykırı içeriğin ya da davranışın niteliğidir; komşu dal ise bir kişi veya söz hakkında bu yönde hüküm verme işlemidir.","focus_only":"Doğruluğa aykırı sözün veya davranışın kendisini bildirir.","gloss":"yalan ile yalan sayma ayrımı","neighbor_only":"Bir sözü yalan sayma, birini yalancı bulma veya ona yalancılık yükleme işlemini bildirir.","neighbor_ref":"root_001290/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da doğruluk ile gerçeğe aykırılık arasındaki değerlendirme alanındadır."},{"boundary_match":"partial","distinction":"Odak dal genel doğruluğa aykırılıktır; komşu dal bunun daha ağır, saptırılmış veya başkalarını yanlış yöne sevk eden türünü belirginleştirir.","focus_only":"Sıradan ölçekteki söz ve davranış yalanlarını da kapsar.","gloss":"yalan ile saptırıcı büyük yalan","neighbor_only":"Doğrudan sapmış, büyük veya başkalarını yanlış yöne çeken ağır bir yalan alanını da öne çıkarır.","neighbor_ref":"root_000041/B002","relation_type":"near_synonym","shared_zone":"İki dal da doğruluğa aykırı söz ve aldatıcı içerik alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal söz ve davranıştaki genel doğruluğa aykırılıktır; komşu dal özellikle bilgi yerine tahmine dayanarak asılsız söz üretmeyi de içerir.","focus_only":"Söz dışındaki davranışlarda görülen doğruluğa aykırılığı da kapsar.","gloss":"yalan ile bilgisizce söyleme","neighbor_only":"Bilgiye dayanmadan tahmin yürütme ve doğrulanmamış söz söyleme alanını da kapsar.","neighbor_ref":"root_000403/B002","relation_type":"near_synonym","shared_zone":"Gerçek dışı veya dayanaksız söz söyleme bağlamlarında iki anlam birbirine yaklaşır."},{"boundary_match":"partial","distinction":"Odak dal genel yalan niteliğidir; komşu dal yalanı özellikle haktan sapma, yalancı tanıklık ve batıllık çevresinde örgütler.","focus_only":"Her türlü sözsel veya davranışsal doğruluğa aykırılığı kapsar.","gloss":"genel yalan ile haktan sapmış söz","neighbor_only":"Yalancı tanıklık, haktan sapma ve batıl sayılan nesneler gibi özel alanlara uzanır.","neighbor_ref":"root_000654/B002","relation_type":"near_neighbor","shared_zone":"İki dal da gerçek ve hakikate aykırı söz alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal doğruluğa aykırılığı temel alır; komşu dal ise sözün kesinlik ve güven düzeyine odaklanır, bu nedenle her kuşkulu aktarım yalan değildir.","focus_only":"Sözün ya da davranışın doğruluğa aykırı olmasını doğrudan bildirir.","gloss":"yalan ile kuşkulu aktarım","neighbor_only":"Kesinlik bulunmadan aktarılan, kuşkulu veya doğruluğu güven vermeyen sözü de kapsar.","neighbor_ref":"root_000633/B001","relation_type":"near_neighbor","shared_zone":"Kuşkulu bir iddianın gerçek dışı çıkması durumunda iki alan kesişebilir."}],"source_phrase_ar":"الكذب خلاف الصدق (maqayis;jamhara); الكذاب لغة في الكذب (ayn); كذب كذبا فهو كاذب وكذاب وكذوب (sihah); يقال في المقال والفعال (mufradat)","source_summary":"Kaynaklar, doğruluğa aykırılığı ortak çekirdek sayar; kullanım alanını söz ve davranış olarak verir ve bu niteliği taşıyan kişiye yönelik adlandırmaları aynı anlam çevresinde toplar.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الكذب في القول والفعل، ووصف صاحبه بالكاذب والكذاب والكذوب، وجمع الأكاذيب والمكاذب","what_is_not_ar":"لا يدخل فيه فعل التكذيب والنسبة إلى الكذب، ولا إغراء كذب عليك، ولا الألفاظ الاصطلاحية الخاصة بالحملة واللبن والثوب"},"support_links":[]},{"boundary":"Dal yalan üretmeyi değil, kişi veya söz hakkında yalan hükmü vermeyi ve belirli türevlerde bu hükmü bulguya dayandırmayı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001290/B002","candidate_links":[{"candidate_id":"cand_41a3ca2ecaf0356b829c","lane":"micro"},{"candidate_id":"cand_816617fd62e44f6be880","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"91:11:1:1","qac_word_ref":"91:11:1","surface_ar":"كَذَّبَتْ"}],"gloss":"yalan sayma veya yalancı bulma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya söz, yalan olduğu söylenerek doğruluk bakımından olumsuz değerlendirilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli türemiş biçimler, kişiyi yalancı bulmayı veya onun yalanını ortaya çıkarmayı bildirir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hüküm verme çekirdeği ile belirli türevlerdeki bulma ve açığa çıkarma ayrımını birlikte karşılar.","boundary_detail":"Dal yalan üretmeyi değil, kişi veya söz hakkında yalan hükmü vermeyi ve belirli türevlerde bu hükmü bulguya dayandırmayı kapsar.","branch_image_ar":"نسبة الشيء أو صاحبه إلى الكذب","concept_gloss":"yalan sayma veya yalancı bulma","contextual_glosses":[{"applicability":"Bir sözün veya kişinin söylediğinin yalan olduğunu bildiren bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiyi yalancı bulma ve yalanını ortaya çıkarma sonucunu tek başına göstermez.","preserves":"Kişi veya söz hakkında yalan hükmü verme işlemini korur."},"facet_ids":["F001"],"text":"yalanlamak","usage_role":"contextual"},{"applicability":"Değerlendirme sonucunda bir kişinin yalan söylediğinin anlaşıldığı türemiş biçimler için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir sözü doğrudan yalan sayma ve muhataba yalan söylediğini bildirme işlemini kapsamaz.","preserves":"Kişiyi yalancı bulma veya yalanını açığa çıkarma sonucunu korur."},"facet_ids":["F002"],"text":"yalancı bulmak","usage_role":"contextual"}],"definition":"Bir kişiyi veya sözü yalanla ilişkilendirerek yalan olduğunu söylemektir. Bazı türemiş biçimlerde işlem, kişiyi yalancı bulma ya da yalanını ortaya çıkarma sonucunu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya söz, yalan olduğu söylenerek doğruluk bakımından olumsuz değerlendirilir."},{"facet_id":"F002","role":"source_variant","statement":"Belirli türemiş biçimler, kişiyi yalancı bulmayı veya onun yalanını ortaya çıkarmayı bildirir."}],"identity_rationale":"Kaynak ifadesi tek bir işlemi değil, birbirine bağlı iki işlemi içerir: bir kişiyi veya sözü yalanla nitelemek ve bazı türemiş biçimlerde kişiyi yalancı bulmak ya da yalanını açığa çıkarmak. Dal korunabilir, ancak bu ayrım tek bir genel 'yalan yükleme' anlatımı içinde eritilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yalanlama; yalan sayma"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"birini yalancı saymak veya ona yalan söylediğini bildirmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini yalancı bulmak veya yalanını ortaya çıkarmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"seni yalancı saymıyorum"}],"lexicalization_note":"Tanım, türemiş ve nesne alan biçimlerinin farklı işlemlerini ayırır; bunlardan hiçbiri yalın biçimin genel yalan anlamı olarak sunulmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalanın kendisi, genel suçlama ve benzer isnat işlemleriyle sınırı gösteren dört aday seçildi, daha uzak söz ve özel kalıp alanları yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalan olduğuna hükmetme işlemidir; komşu dal ise bu hükmün konusu olan gerçeğe aykırı söz veya davranıştır.","focus_only":"Bir kişi veya söz hakkında yalan hükmü verme işlemini bildirir.","gloss":"yalan sayma ile yalan ayrımı","neighbor_only":"Doğruluğa aykırı sözün veya davranışın kendisini bildirir.","neighbor_ref":"root_001290/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da doğruluk değerlendirmesi ve yalan alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal yalnız doğruluk ve yalan eksenindeki hükme bağlıdır; komşu dalın suçlama ve kuşku alanı daha geniştir.","focus_only":"Yüklenen nitelik özellikle yalan söyleme veya sözün yalan olmasıdır.","gloss":"yalancılıkla niteleme ile suçlama","neighbor_only":"Kişiye herhangi bir suçlama ya da kuşku iliştirmeyi, hatta onda bulunmayan olumlu bir niteliği yakıştırmayı kapsayabilir.","neighbor_ref":"root_001607/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir kişi hakkında olumsuz bir niteleme veya iddia yöneltme işlemini içerebilir."},{"boundary_match":"field_only","distinction":"İşlemin yapısı benzerdir, ancak odak dalın hükmü yalanla, komşu dalın hükmü hırsızlıkla sınırlıdır; anlam çekirdekleri birbirinin yerine geçmez.","focus_only":"Kişiyi yalancılıkla veya sözünü yalan olmakla niteler.","gloss":"farklı fiillerle suçlayıcı niteleme","neighbor_only":"Kişiyi hırsızlık yapmakla niteler.","neighbor_ref":"root_000700/B005","relation_type":"same_field","shared_zone":"İki dal da bir kişiye belirli bir olumsuz eylemi yükleyen dilsel işlemlerdir."},{"boundary_match":"partial","distinction":"Odak dal doğruluk hakkında verilen hükümdür; komşu dal ise gerçekleşmemiş belirli bir eylemin kişiye isnat edilmesidir.","focus_only":"Bir kişiyi genel olarak yalancı sayabilir veya belirli bir sözü yalanlayabilir.","gloss":"yalan sayma ile yapılmamışı yükleme","neighbor_only":"Kişinin yapmadığı belirli bir içme eylemini ona yükleme iddiasıyla sınırlıdır.","neighbor_ref":"root_000783/B010","relation_type":"near_neighbor","shared_zone":"Bir kişiye gerçekleşmemiş bir eylem yüklenince bu iddiayı yalanlama bağlamında iki alan kesişir."}],"source_phrase_ar":"كذبت فلانا نسبته إلى الكذب وأكذبته وجدته كاذبا (maqayis); كذبته جعلته كاذبا (ayn); كذبت بالحديث كذابا وتكذيبا (jamhara); أكذبت الرجل ألفيته كاذبا وكذبته إذا قلت له كذبت (sihah); كذبته نسبته إلى الكذب (mufradat)","source_summary":"Kaynaklar, birini ya da bir sözü yalanla niteleme konusunda birleşir; aynı toplu kanıt, ayrı bir türemiş biçimde kişiyi yalancı bulma veya yalanı açığa çıkarma yorumunu da taşır.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه كذبت فلانا، وأكذبته، والتكذيب، والمكاذبة، ولا مكذبة بمعنى لا أكذبك، وقراءة لا يكذبونك في معنى لا يجدونك كاذبا أو لا ينسبونك إلى الكذب","what_is_not_ar":"لا يدخل فيه إنشاء الكذب نفسه، ولا الإغراء بقول كذب عليك، ولا كذب الحملة أو اللبن"},"support_links":["sup_80adfaa6f7c0e8ecf39a","sup_f960e33e9b5593b03180"]},{"boundary":"Dal, belirli kalıbın 'sana düşer, onu yap' anlamıyla sınırlıdır; yalın köke genel bir zorunluluk veya özendirme anlamı vermez.","branch_kind":"collocation","branch_ref":"root_001290/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"91:11:1:1","qac_word_ref":"91:11:1","surface_ar":"كَذَّبَتْ"}],"gloss":"onu üstlen; sana düşer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalıp, söz konusu işin muhataba düşen bir yükümlülük olduğunu bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı kalıp, muhatabı o işi üstlenmeye yönelten güçlü bir özendirme olarak kullanılabilir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıbın hem yükümlülük bildiren hem de eyleme yönelten iki işlevini birlikte veren karşılıktır.","boundary_detail":"Dal, belirli kalıbın 'sana düşer, onu yap' anlamıyla sınırlıdır; yalın köke genel bir zorunluluk veya özendirme anlamı vermez.","branch_image_ar":"كذب عليك بمعنى الزم وعليك به","concept_gloss":"onu üstlen; sana düşer","contextual_glosses":[{"applicability":"Kalıbın yükümlülük bildiren yönünün öne çıktığı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Buyruk ve güçlü özendirme tonunu tek başına tam olarak göstermez.","preserves":"İşin muhataba düşen bir yükümlülük oluşunu açıkça korur."},"facet_ids":["F001"],"text":"onu yapmalısın","usage_role":"contextual"},{"applicability":"Kalıbın muhatabı işe yönelten özendirme işlevinin baskın olduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşin önceden var olan bir yükümlülük olarak muhataba düştüğünü zorunlu biçimde bildirmez.","preserves":"Muhatabı söz konusu işi yapmaya yönelten güçlü çağrıyı korur."},"facet_ids":["F002"],"text":"haydi, onu üstlen","usage_role":"contextual"}],"definition":"Belirli bir kalıp içinde, bir şeyin kişiye düşen bir yükümlülük olduğunu bildirmek veya kişiyi onu yapmaya yöneltmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalıp, söz konusu işin muhataba düşen bir yükümlülük olduğunu bildirir."},{"facet_id":"F002","role":"extension","statement":"Aynı kalıp, muhatabı o işi üstlenmeye yönelten güçlü bir özendirme olarak kullanılabilir."}],"identity_rationale":"Kaynak ifadesi belirli bir kalıbı zorunluluk bildirme ve bir işi yapmaya yöneltme anlamlarıyla açıklar. Bu anlamın yalan söylemeyle doğrudan bir bileşeni yoktur ve yalnız söz konusu kalıp içinde geçerlidir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"şunu üstlen; sana düşer veya onu yapmalısın"}],"lexicalization_note":"Tanım yalnızca verilen kalıplaşmış söyleyişi açıklar; zorunluluk ve yöneltme anlamları yalın biçime taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yükümlülük, özendirme ve bağlayıcılıkla doğrudan sınır kuran üç aday seçildi, yalnızca çalışma azmi veya uzak kök dallarıyla ilişkili adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli kalıbın 'sana düşer, onu yap' değeridir; komşu dal genel emir ve buyurma sistemidir.","focus_only":"Zorunluluk ile güçlü yöneltmeyi yalnız belirli bir kalıplaşmış söyleyişte birleştirir.","gloss":"kalıplaşmış yükümlülük ile genel buyruk","neighbor_only":"Genel buyruk, yasak karşıtı emir ve buyruğa uyma alanlarını kapsar.","neighbor_ref":"root_000051/B002","relation_type":"near_synonym","shared_zone":"İki dal da muhataptan bir eylemi gerçekleştirmesini isteme veya bunu gerekli kılma alanındadır."},{"boundary_match":"partial","distinction":"Odak dal yükümlülük bildirimini de taşır ve belirli bir kalıba bağlıdır; komşu dalın çekirdeği genel teşvik ve kışkırtmadır.","focus_only":"Bir işin muhataba düşen yükümlülük olduğunu da bildirebilir.","gloss":"üstlenmeye yöneltme ile kışkırtma","neighbor_only":"Özellikle çatışmaya yönelik kışkırtma, teşvik ve harekete geçirme anlamlarını kapsar.","neighbor_ref":"root_000309/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da muhatabı bir eyleme kuvvetle yöneltme işlevinde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal kalıplaşmış bir çağrı ve yükümlülük bildirimidir; komşu dal dışsal bir hüküm veya güçle bağlayıcılık kurma işlemidir.","focus_only":"Söyleyiş yoluyla muhatabı işi üstlenmeye çağırır.","gloss":"sözel yöneltme ile bağlayıcı kılma","neighbor_only":"Bir şeyi hüküm, kanıt, yönetim veya zor kullanmayla kişiye bağlayıp kaçınılmaz kılar.","neighbor_ref":"root_001354/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir işin kişi için gerekli veya bağlayıcı hale gelmesi alanında kesişir."}],"source_phrase_ar":"كذب عليك كذا بمعنى الإغراء أي عليك به أو قد وجب عليك (maqayis); كذب عليكم الحج أي وجب عليكم ودونكم الحج (ayn); كذب عليك كذا وكذا في معنى الإغراء (jamhara); كذب عليكم الحج أي وجب (sihah); كذب عليك الحج قيل معناه وجب فعليك به (mufradat)","source_summary":"Kaynaklar bu kalıplaşmış söyleyişi, bir işin muhataba düşmesi ve muhatabın o işi yapmaya yöneltilmesi anlamlarında ortaklaşa açıklar.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه كذب عليك الحج والجهاد والعسل ونحوها إذا أريد الوجوب أو الإغراء أو دونك الشيء","what_is_not_ar":"لا يدخل فيه الإخبار بالكذب، ولا تكذيب المخاطب، ولا كذب الحملة أو اللبن"},"support_links":[]},{"boundary":"Anlam yalnız saldırı hamlesi bağlamında ve olumlu-olumsuz biçimlerin karşıtlığıyla geçerlidir; genel yalan veya genel cesaret anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001290/B004","candidate_links":[{"candidate_id":"cand_c7a4d4d9fc5856f19727","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"91:11:1:1","qac_word_ref":"91:11:1","surface_ar":"كَذَّبَتْ"}],"gloss":"hamlede duraksamak; olumsuzda sonuna kadar ilerlemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olumlu kalıp, saldırıya geçtikten sonra durmayı, geri kalmayı veya korkaklık göstermeyi bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olumsuz kalıp, saldırganın durmadan ilerleyerek vuruşa kadar hamleyi sürdürdüğünü bildirir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Savaş hamlesine bağlı olumlu duraksama ile olumsuz kalıptaki kesintisiz ilerlemeyi birlikte karşılar.","boundary_detail":"Anlam yalnız saldırı hamlesi bağlamında ve olumlu-olumsuz biçimlerin karşıtlığıyla geçerlidir; genel yalan veya genel cesaret anlamı değildir.","branch_image_ar":"صدق الحملة أو كذبها","concept_gloss":"hamlede duraksamak; olumsuzda sonuna kadar ilerlemek","contextual_glosses":[{"applicability":"Saldırıya başladıktan sonra geri duran veya korkaklık gösteren kişi için olumlu kalıpta uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Olumsuz kalıbın durmaksızın ilerleyip vuruşa ulaşma anlamını kapsamaz.","preserves":"Hamleyi tamamlamadan geri durma ve cesaret yitirme yönünü korur."},"facet_ids":["F001"],"text":"hamleden caymak","usage_role":"contextual"},{"applicability":"Olumsuz kalıpta saldırganın vuruşa kadar ilerlemeyi sürdürdüğü bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Olumlu kalıptaki duraksama ve korkaklık anlamını kapsamaz.","preserves":"Hamlede durmama, korkmama ve saldırıyı vuruşa kadar sürdürme yönünü korur."},"facet_ids":["F002"],"text":"geri durmadan saldırmak","usage_role":"contextual"}],"definition":"Bir saldırı hamlesinde geri durup hamleyi tamamlamamak veya korkaklık göstermektir; olumsuz kalıpta ise durmadan ilerleyip vuruncaya kadar hamleyi sürdürmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olumlu kalıp, saldırıya geçtikten sonra durmayı, geri kalmayı veya korkaklık göstermeyi bildirir."},{"facet_id":"F002","role":"specialization","statement":"Olumsuz kalıp, saldırganın durmadan ilerleyerek vuruşa kadar hamleyi sürdürdüğünü bildirir."}],"identity_rationale":"Kaynak ifadesi savaş hamlesindeki iki karşıt kalıbı birlikte verir: olumlu biçim hamlede durma, geri çekilme veya korkaklık; olumsuz biçim ise durmadan ilerleyip vuruşa ulaşmadır. Dalın kimliği bu kutuplu kalıp düzenine uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"saldırıya geçti ama duraksadı veya korktu"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"saldırıya geçti ve vuruncaya kadar durmadı; korkmadı"}],"lexicalization_note":"Tanım savaş hamlesine bağlı iki kalıbı korur; duraksama ve kararlılıkla ilerleme anlamları yalın biçime genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hamlede durma, saldırının kendisi, cesaret ve kesintisiz hamlenin sonucu ile doğrudan sınır kuran dört aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir hamlenin seyri ve onun olumsuz karşıt kalıbıdır; komşu dal kişinin daha genel korkaklık niteliğidir.","focus_only":"Başlatılmış bir saldırı hamlesinin sürdürülüp sürdürülmediğini kalıp içinde değerlendirir.","gloss":"hamlede geri durma ile korkaklık","neighbor_only":"Kişinin genel olarak atılganlıktan kesilmiş ve korkak oluşunu betimler.","neighbor_ref":"root_001150/B008","relation_type":"near_neighbor","shared_zone":"Saldırıya devam etmeme, geri kalma ve korkaklık bağlamlarında iki alan kesişir."},{"boundary_match":"field_only","distinction":"Odak dal saldırının sürdürülme niteliğini bildirir; komşu dal saldırı ve koşu hareketinin kendisidir.","focus_only":"Hamlenin duraksama veya sonuna kadar sürme bakımından sonucunu değerlendirir.","gloss":"hamlenin seyri ile hücum eylemi","neighbor_only":"Düşmana saldırma, hücum etme ve koşma eyleminin kendisini bildirir.","neighbor_ref":"root_000782/B003","relation_type":"same_field","shared_zone":"İki dal da savaşta düşmana yönelen saldırı hamlesi alanındadır."},{"boundary_match":"partial","distinction":"Odak dal belirli saldırı kalıbında gerçekleşen davranışı değerlendirir; komşu dal daha genel bir cesaret ve atılganlık niteliğidir.","focus_only":"Olumlu ve olumsuz kalıplarla tek bir hamlede durma ya da sürdürme karşıtlığını kurar.","gloss":"hamleyi sürdürme ile cesaret","neighbor_only":"Genel cesaret, atılganlık ve düşmana doğru öne çıkma niteliğini bildirir.","neighbor_ref":"root_001207/B006","relation_type":"near_neighbor","shared_zone":"Hamleyi korkmadan sürdürme bağlamında iki anlam birbirine yaklaşır."},{"boundary_match":"partial","distinction":"Odak dal hamlenin kesintisiz sürmesini yeterli görür; komşu dal buna düşmanı yenme sonucunu da ekler.","focus_only":"Hamlede durma ile durmadan sürdürme karşıtlığını, zafer şartı aramadan bildirir.","gloss":"kesintisiz hamle ile yenilgiye uğratma","neighbor_only":"Kesintisiz bir saldırıyla karşı tarafı yenme sonucunu özellikle içerir.","neighbor_ref":"root_000003/B007","relation_type":"near_neighbor","shared_zone":"Duraksamadan yapılan saldırı hamlesi iki dalın ortak sahnesidir."}],"source_phrase_ar":"حمل فلان ثم كذب أي لم يصدق في الحملة (maqayis); حمل فلان على فلان فما كذب حتى طعن أو ضرب أي ما وقف (jamhara); حمل فلان فما كذب أي ما جبن (sihah); حمل فلان على قرنه فكذب (mufradat)","source_summary":"Kaynaklar saldırı hamlesini sürdürmeme ile korkaklık arasında bağ kurar; olumsuz kalıp ise durmayıp vuruşa kadar ilerleme anlamını verir.","sources":["MQ","JA","SI","MU"],"what_is_ar":"يدخل فيه كذب في الحملة إذا لم يصدقها أو جبن، ونفي الكذب عن الحملة إذا مضى فيها ولم يقف حتى يطعن أو يضرب","what_is_not_ar":"لا يدخل فيه الكذب في الخبر، ولا الإغراء، ولا وقوف الوحشي بعد شوط"},"support_links":["sup_2eb24e1ef5474661de6d"]},{"boundary":"Dal, 'yapmakta gecikmedi' değerindeki kalıpla sınırlıdır; genel hız, acele veya yalan anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001290/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"91:11:1:1","qac_word_ref":"91:11:1","surface_ar":"كَذَّبَتْ"}],"gloss":"gecikmeden yapmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, belirtilen işi yapmadan önce beklemez veya oyalanmaz."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Beklememenin sonucu, işin gecikmeden gerçekleştirilmesidir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıbın hem oyalanmama aşamasını hem de işi gecikmeden gerçekleştirme sonucunu özlü biçimde karşılar.","boundary_detail":"Dal, 'yapmakta gecikmedi' değerindeki kalıpla sınırlıdır; genel hız, acele veya yalan anlamı değildir.","branch_image_ar":"ما كذب أن فعل أي ما لبث","concept_gloss":"gecikmeden yapmak","contextual_glosses":[{"applicability":"Söz konusu işin beklenmeden gerçekleştiği geçmiş zaman anlatımlarında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Oyalanmama aşamasını ve işin gecikmeden gerçekleşmesini doğal kullanımda korur."},"facet_ids":["F001","F002"],"text":"hemen yaptı","usage_role":"contextual"}],"definition":"Belirli bir olumsuz kalıp içinde, bir kişinin söz konusu işi yapmakta oyalanmadığını ve gecikmeden yaptığını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, belirtilen işi yapmadan önce beklemez veya oyalanmaz."},{"facet_id":"F002","role":"extension","statement":"Beklememenin sonucu, işin gecikmeden gerçekleştirilmesidir."}],"identity_rationale":"Kaynak ifadesi yalnız belirli bir olumsuz kalıp içinde kişinin bir işi yapmakta oyalanmadığını ve gecikmediğini bildirir. Geçici dal çerçevesi bu yapıyı ve anlamı doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yapmakta gecikmedi; hemen yaptı"}],"lexicalization_note":"Tanım yalnız verilen olumsuz kalıbın gecikmeme anlamını açıklar; hız ve çabukluk yalın kökün anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gecikmeme, ilk anda yapma ve genel acele arasındaki sınırı en iyi gösteren üç aday seçildi, yalnız zaman veya tekrar alanını paylaşan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız kalıplaşmış gecikmeme anlamıdır; komşu dal benzer kalıbın yanında koşma hızına ilişkin ayrı bir alan da taşır.","focus_only":"Gecikmemeyi yalnız belirli bir 'yapmakta oyalanmadı' kalıbında bildirir.","gloss":"gecikmeme ile az bekleme","neighbor_only":"Ayrı bir kullanımda koşmanın görece hızlı oluşunu da kapsar.","neighbor_ref":"root_000973/B009","relation_type":"near_synonym","shared_zone":"Bir işi yapmakta az bekleme veya hiç oyalanmama anlamında iki dal büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal bekleme süresinin yokluğuna odaklanır; komşu dal eylemin durumun ilk anındaki oluşunu ayrıca şart koşar.","focus_only":"Bir işi yapmak öncesindeki gecikmenin bulunmadığını kalıplaşmış biçimde bildirir.","gloss":"gecikmeden yapma ile ilk anda yapma","neighbor_only":"Eylemin ilk anda, durum henüz yatışmadan veya olayın başlangıç itkisiyle yapılmasını vurgular.","neighbor_ref":"root_001185/B002","relation_type":"near_synonym","shared_zone":"Bir eylemin beklenmeden ve hemen gerçekleşmesi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal yalnız gecikmenin yokluğunu bildirir; komşu dal hızlandırma, öne alma ve vaktinden önce isteme gibi ek yönler taşır.","focus_only":"Belirli bir işin yapılmasında gecikme olmadığını bildirir.","gloss":"gecikmeme ile acele etme","neighbor_only":"Bir şeyi vaktinden önce isteme, öne alma ve genel acele ettirme alanlarını kapsar.","neighbor_ref":"root_000987/B001","relation_type":"near_neighbor","shared_zone":"İşin kısa sürede veya beklenmeden yapılması bağlamında iki anlam kesişebilir."}],"source_phrase_ar":"ما كذب فلان أن فعل كذا أي ما لبث (maqayis;sihah)","source_summary":"Kaynakların ortak açıklaması, belirli kalıbın kişinin bir işi yapmakta beklemediğini ve gecikmediğini bildirmesidir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه قولهم ما كذب فلان أن فعل كذا إذا لم يلبث ولم يتأخر","what_is_not_ar":"لا يدخل فيه الكذب في الخبر، ولا وجوب كذب عليك، ولا كذب اللبن"},"support_links":[]},{"boundary":"Anlam yalnız dişi devenin sütüne ilişkin kalıpta, sütün kaybolması veya beklenen süre boyunca devam etmemesiyle sınırlıdır.","branch_kind":"collocation","branch_ref":"root_001290/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"91:11:1:1","qac_word_ref":"91:11:1","surface_ar":"كَذَّبَتْ"}],"gloss":"sütün kesilmesi veya beklenenden önce tükenmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi devenin sütü gider veya kesilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir açıklamada süt bir süre sürecek sanılır, fakat bu beklentinin tersine devam etmez."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi devenin sütüne bağlı kaybolma çekirdeğini ve devam beklentisinin boşa çıkmasını birlikte karşılar.","boundary_detail":"Anlam yalnız dişi devenin sütüne ilişkin kalıpta, sütün kaybolması veya beklenen süre boyunca devam etmemesiyle sınırlıdır.","branch_image_ar":"كذب لبن الناقة إذا ذهب ولم يدم","concept_gloss":"sütün kesilmesi veya beklenenden önce tükenmesi","contextual_glosses":[{"applicability":"Sütün artık gelmediği ve önceki üretimin sona erdiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sütün süreceği beklentisinin özellikle boşa çıkmış olduğunu tek başına bildirmez.","preserves":"Dişi devenin sütünün gitmesi veya sona ermesi çekirdeğini korur."},"facet_ids":["F001"],"text":"sütü kesildi","usage_role":"contextual"},{"applicability":"Sütün belirli bir süre devam edeceği beklentisinin gerçekleşmediği açıklayıcı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sütün devamına ilişkin beklentiyi ve beklenenden önce kesilmesini birlikte korur."},"facet_ids":["F001","F002"],"text":"sütü umulduğu kadar sürmedi","usage_role":"explanatory"}],"definition":"Dişi devenin sütünün kaybolması veya bir süre devam edeceği sanıldığı halde beklenenden önce kesilmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi devenin sütü gider veya kesilir."},{"facet_id":"F002","role":"source_variant","statement":"Bir açıklamada süt bir süre sürecek sanılır, fakat bu beklentinin tersine devam etmez."}],"identity_rationale":"Kaynak ifadesi dişi devenin sütünün gitmesini ortak çekirdek olarak verir; toplu kanıttaki ek açıklama, bir süre devam edeceği sanılan sütün beklenenden önce kesilmesini belirtir. Geçici çerçeve iki yönü de doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"dişi devenin sütü kesildi veya umulduğu kadar sürmedi"}],"lexicalization_note":"Tanım yalnız dişi devenin sütünü konu alan kalıba bağlıdır; genel tükenme veya genel beklenti boşa çıkması anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; süt kesilmesi, geri dönüş beklentisi ve süt bolluğu eksenini açıklayan üç aday seçildi, yalnız başka sıvıları veya hayvan özelliklerini paylaşan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dişi devenin sütüne ve kimi kullanımda boşa çıkan süreklilik beklentisine bağlıdır; komşu dal süt veriminin azalmasını ve yağmuru da kapsar.","focus_only":"Dişi devenin sütünün gitmesini ve beklenen süre boyunca devam etmemesini bildirir.","gloss":"sütün beklenmedik kesilmesi ile verimin azalması","neighbor_only":"Sütün azalmasını veya kesilmesini yağmurun azalması ve kesilmesiyle aynı anlam alanında kapsar.","neighbor_ref":"root_000305/B005","relation_type":"near_synonym","shared_zone":"Sütün azalması veya bütünüyle kesilmesi iki dalın doğrudan ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal gerçekleşen kaybı ve boşa çıkan devam beklentisini anlatır; komşu dal kayıptan sonraki geri dönüş umuduna odaklanır.","focus_only":"Sütün fiilen gittiğini veya beklenen süre boyunca devam etmediğini bildirir.","gloss":"sütün kesilmesi ile geri dönme umudu","neighbor_only":"Sütü kesilen ya da sütü kuşkulu olan hayvanda sütün geri dönmesi umudunu bildirir.","neighbor_ref":"root_001015/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da kesilmiş veya belirsiz hale gelmiş süt verimi durumunu konu alır."},{"boundary_match":"opposed","distinction":"Odak dal süt veriminin sona eren kutbundadır; komşu dal aynı alanın bol ve güçlü verim kutbundadır.","focus_only":"Sütün kaybolmasını, kesilmesini veya beklenenden az sürmesini bildirir.","gloss":"süt kesilmesi ile süt bolluğu","neighbor_only":"Dişi devenin süt bakımından çok verimli ve bol oluşunu bildirir.","neighbor_ref":"root_000200/B005","relation_type":"polarity_pair","shared_zone":"İki dal da dişi devenin süt veriminin durumu üzerinde ortak bir nicelik ekseni kurar."}],"source_phrase_ar":"كذب لبن الناقة ذهب وفيه نظر وقياسه صحيح (maqayis); كذب لبن الناقة أي ذهب (sihah); كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم (mufradat)","source_summary":"Toplu kanıt sütün gitmesi çekirdeğinde birleşir; bunun yanında, devam edeceği sanılan sütün beklenen süreyi tamamlamadan kesilmesi biçiminde daha ayrıntılı bir yorum da verir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه كذب لبن الناقة إذا ذهب أو ظن دوامه فلم يدم","what_is_not_ar":"لا يدخل فيه كذب الخبر، ولا كذب الحملة، ولا كذب عليك في الإغراء"},"support_links":[]},{"boundary":"Dal yalnız yaban hayvanının koşma, durma ve arkasına bakma dizisine bağlıdır; genel durma ya da genel koşu anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001290/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"91:11:1:1","qac_word_ref":"91:11:1","surface_ar":"كَذَّبَتْ"}],"gloss":"koşup arkasına bakmak için durmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yaban hayvanı önce belirli bir mesafe koşar, ardından hareketini durdurur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Durmanın amacı hayvanın arkasında kalan yere veya şeye bakmasıdır."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaban hayvanını, koşudan sonraki durmayı ve durmanın geriye bakma amacını birlikte karşılar.","boundary_detail":"Dal yalnız yaban hayvanının koşma, durma ve arkasına bakma dizisine bağlıdır; genel durma ya da genel koşu anlamı değildir.","branch_image_ar":"كذب الوحشي إذا جرى ثم وقف","concept_gloss":"koşup arkasına bakmak için durmak","contextual_glosses":[{"applicability":"Yaban hayvanının hareket dizisinin anlatı içinde doğal bir cümleyle çevrildiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önce koşmayı, sonra durup geride kalana bakmayı doğal anlatım sırasıyla korur."},"facet_ids":["F001","F002"],"text":"bir süre koştu, sonra dönüp baktı","usage_role":"contextual"}],"definition":"Bir yaban hayvanının belirli bir mesafe koştuktan sonra arkasında ne olduğunu görmek için durmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yaban hayvanı önce belirli bir mesafe koşar, ardından hareketini durdurur."},{"facet_id":"F002","role":"specialization","statement":"Durmanın amacı hayvanın arkasında kalan yere veya şeye bakmasıdır."}],"identity_rationale":"Tek kaynaklı ifade, yaban hayvanının belirli bir mesafe koşmasından sonra arkasına bakmak için durduğu aşamalı hareketi eksiksiz biçimde tanımlar. Geçici dal çerçevesi katılımcıyı, hareket sırasını ve amacı korur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yaban hayvanı bir mesafe koşup arkasına bakmak için durdu"}],"lexicalization_note":"Tanım yalnız yaban hayvanını özne alan kalıba ve belirtilen hareket dizisine bağlıdır; yalın biçime bir hareket anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hayvanda hareketin kesilmesi, ileri hareket ve bakış amacıyla doğrudan karşılaştırma sağlayan dört aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın katılımcısı yaban hayvanıdır ve amaç arkasına bakmaktır; komşu dal av köpeğinin ilgisini veya takibini kesmesine odaklanır.","focus_only":"Yaban hayvanı koşusunu geriye bakmak amacıyla durdurur.","gloss":"koşudan sonra durma ile avdan vazgeçme","neighbor_only":"Köpek avını yakaladıktan sonra gevşer, ondan döner veya başka şeyle oyalanır.","neighbor_ref":"root_001084/B005","relation_type":"near_synonym","shared_zone":"Bir hayvanın koşu veya takip hareketini bir aşamadan sonra kesmesi iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Odak dal belirli bir koşu-sonrası bakış dizisidir; komşu dal daha genel durdurma, kalma ve konaklama ilişkilerini kapsar.","focus_only":"Koşudan sonra özellikle geriye bakmak için gerçekleşen kısa durmayı bildirir.","gloss":"geriye bakmak için durma ile konaklama","neighbor_only":"Binek hayvanını tutmayı, bir yerde kalmayı, inmeyi veya bir kişiye yönelmeyi kapsar.","neighbor_ref":"root_000997/B003","relation_type":"near_neighbor","shared_zone":"Hareket halindeki bir canlının ilerlemeyi kesmesi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal koşu sonrasındaki durmayı temel alır; komşu dal kesintisiz ve güçlü ileri hareketi temel alır.","focus_only":"Koşunun ardından hareketin kesilmesini ve geriye bakmayı içerir.","gloss":"koşuyu kesme ile hızla ileri atılma","neighbor_only":"Binek hayvanının hızla ileri atılmasını ve kendini öne fırlatır gibi ilerlemesini bildirir.","neighbor_ref":"root_001209/B005","relation_type":"near_neighbor","shared_zone":"İki dal da hayvanın hızlı ilerleyişini konu alan hareket sahnesindedir."},{"boundary_match":"thematic_only","distinction":"Odak dalın çekirdeği koşu sonrasında durma dizisidir; komşu dal ise önceki bir hareket gerektirmeyen bakış eylemidir.","focus_only":"Bakışı, öncesindeki koşu ve durma dizisinin amacı olarak içerir.","gloss":"hareket dizisi ile dikkatli bakış","neighbor_only":"Baş veya gözleri kaldırarak bir şeye dikkatle bakma eylemini doğrudan bildirir.","neighbor_ref":"root_000256/B008","relation_type":"thematic","shared_zone":"Bir şeyi görmek üzere yöneltilen bakış, iki anlamın aynı sahnede bulunabilen unsurudur."}],"source_phrase_ar":"كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Yaban hayvanı bir mesafe koştuktan sonra arkasına bakmak için durur."}],"source_summary":"Bu özel kullanım tek bir kaynakta, yaban hayvanının koşu sonrasında arkasına bakmak amacıyla durduğu ardışık hareket olarak tanıklanır.","sources":["JA"],"what_is_ar":"يدخل فيه كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه","what_is_not_ar":"لا يدخل فيه كذب الحملة، ولا كذب اللبن، ولا الكذب في القول"},"support_links":[]},{"boundary":"Dal, ilgili yalın biçimin 'kişinin iç benliği' adını taşımasıyla sınırlıdır; kişinin yalan söylemesi veya benliğin aldatıcılığı anlamını içermez.","branch_kind":"bare","branch_ref":"root_001290/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"91:11:1:1","qac_word_ref":"91:11:1","surface_ar":"كَذَّبَتْ"}],"gloss":"iç benlik","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, bir yalan niteliği yüklemeden doğrudan kişinin iç benliğini adlandırır."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynak ifadesindeki doğrudan adlandırmayı, yalan söyleme niteliği eklemeden karşılar.","boundary_detail":"Dal, ilgili yalın biçimin 'kişinin iç benliği' adını taşımasıyla sınırlıdır; kişinin yalan söylemesi veya benliğin aldatıcılığı anlamını içermez.","branch_image_ar":"النفس الكذوب","concept_gloss":"iç benlik","contextual_glosses":[{"applicability":"Eski ve tek kaynaklı adlandırmanın modern Türkçede açıklanması gereken bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözcüğün kişiyi içeriden kuran benliği adlandırmasını açık biçimde korur."},"facet_ids":["F001"],"text":"kişinin kendi iç benliği","usage_role":"explanatory"}],"definition":"İlgili sözcüğün, kişideki iç benliği veya kendi olma bilincini doğrudan adlandıran bir isim olarak kullanılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, bir yalan niteliği yüklemeden doğrudan kişinin iç benliğini adlandırır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kaynak ifadesinde bulunmayan yalan söyleme veya aldatma niteliğini benliğe yükler.","collision":"Kişiyi yalan söyleyen biri olarak betimleyen başka daldaki sıfat anlamıyla karışır.","fit":"broadening","loses":null,"preserves":"Benliği konu alan bir adlandırma bulunduğu izlenimini kısmen korur."},"text":"yalancı benlik"}],"identity_rationale":"Kaynak ifadesi iç benliği 'yalancı' diye niteleyen bir söz öbeği kurmaz; ilgili sözcüğü doğrudan iç benliğin adı olarak eşitler. Dal korunabilir, ancak tanım bir ahlak niteliği değil, bağımsız bir adlandırma olarak yeniden çerçevelenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"iç benlik; kişinin kendisi"}],"lexicalization_note":"Tanım sözcüğün yalın biçimde doğrudan iç benliği adlandırmasını verir; başka dallardaki kişi sıfatları veya özel kalıplar bu anlama alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; iç benliği doğrudan adlandıran veya onun işlevini konu alan üç yararlı karşılaştırma seçildi, yalnız kişilik değişimi ve uzak tematik kullanımlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız iç benliği adlandırır; komşu dal iç benliği bedenin yaşamsal özü, kanı ve kalbiyle bir araya getiren daha geniş bir anlam kümesidir.","focus_only":"Tek bir sözcüğün doğrudan iç benlik adı olarak kullanımını bildirir.","gloss":"iç benlik ile yaşam özü","neighbor_only":"İç benliğin yanında kan, yaşam özü ve kalp gibi birbiriyle ilişkili adlandırmaları da kapsar.","neighbor_ref":"root_000187/B004","relation_type":"near_synonym","shared_zone":"Kişinin iç varlığı veya kendisi anlamında iki dal büyük ölçüde örtüşebilir."},{"boundary_match":"partial","distinction":"Odak dal bağımsız iç benlik adıdır; komşu dal bu değeri belirli bir kalıp içinde verir ve ayrıca yakın dost anlamına genişler.","focus_only":"Yalın bir sözcükle kişinin iç benliğini doğrudan adlandırır.","gloss":"iç benlik ile kişinin kendisi","neighbor_only":"Belirli bir soru kalıbında kişinin kendisini, başka kullanımda ise yakın ve seçkin dostu bildirir.","neighbor_ref":"root_000059/B006","relation_type":"near_synonym","shared_zone":"Kişinin kendisini veya iç benliğini gösteren kullanımlarda iki dal örtüşür."},{"boundary_match":"thematic_only","distinction":"Odak dal varlığın adıdır; komşu dal bu varlığa yüklenen süsleme ve yanıltıcı yönlendirme eylemidir.","focus_only":"İç benliği yalnızca bir varlık olarak adlandırır.","gloss":"iç benlik ile benliğin yönlendirmesi","neighbor_only":"İç benliğin veya kötülüğe yönelten bir gücün bir işi süsleyip kişiye çekici göstermesini bildirir.","neighbor_ref":"root_000763/B002","relation_type":"thematic","shared_zone":"İç benlik iki anlamın aynı düşünsel sahnesinde yer alır."}],"source_phrase_ar":"الكذوب النفس (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Sözcük herhangi bir ahlak niteliği eklenmeden doğrudan kişinin iç benliğini adlandırır."}],"source_summary":"Bu yalın adlandırma tek bir kaynakta, ilgili sözcüğün doğrudan kişinin iç benliğiyle eşitlenmesi biçiminde tanıklanır.","sources":["JA"],"what_is_ar":"يدخل فيه إطلاق الكذوب على النفس","what_is_not_ar":"لا يدخل فيه وصف الرجل بالكذاب أو الكذوب، ولا أكاذيب الأخبار"},"support_links":[]},{"boundary":"Dal, boyası veya deseni gerçek dokuma bezemesi sanısı veren kumaşla sınırlıdır; genel yalan, her desenli kumaş veya kişi adı değildir.","branch_kind":"bare","branch_ref":"root_001290/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"91:11:1:1","qac_word_ref":"91:11:1","surface_ar":"كَذَّبَتْ"}],"gloss":"dokuma bezemesi sanısı veren boyalı kumaş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, çeşitli boya renkleriyle renklendirilmiş veya yüzeyine desen işlenmiş bir kumaştır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Boya ve desen, kumaşın dokuma yoluyla bezenmiş olduğu izlenimini verir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin kumaş oluşunu, boya veya deseni ve gerçek dokuma bezemesi gibi görünmesini birlikte karşılar.","boundary_detail":"Dal, boyası veya deseni gerçek dokuma bezemesi sanısı veren kumaşla sınırlıdır; genel yalan, her desenli kumaş veya kişi adı değildir.","branch_image_ar":"الكذابة ثوب يكذب بحاله","concept_gloss":"dokuma bezemesi sanısı veren boyalı kumaş","contextual_glosses":[{"applicability":"Kumaş türünün üretim görünüşüyle birlikte açıkça anlatılması gereken bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Boyama veya yüzey deseniyle oluşturulan dokuma bezemesi izlenimini korur."},"facet_ids":["F001","F002"],"text":"dokuma desenli gibi görünen boyalı kumaş","usage_role":"explanatory"}],"definition":"Çeşitli renklerle boyanmış veya desenlenmiş, bu yüzden dokuma yoluyla bezenmiş gibi görünen bir kumaş ya da giysidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, çeşitli boya renkleriyle renklendirilmiş veya yüzeyine desen işlenmiş bir kumaştır."},{"facet_id":"F002","role":"specialization","statement":"Boya ve desen, kumaşın dokuma yoluyla bezenmiş olduğu izlenimini verir."}],"identity_rationale":"Kaynak ifadesi çeşitli renklerle boyanmış veya desenlenmiş bir kumaşı, dokuma yoluyla bezenmiş gibi görünmesi üzerinden tanımlar; bir açıklama bu yanıltıcı görünüşü adlandırmanın gerekçesi yapar. Geçici çerçeve nesneyi ve görünüş ilişkisini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"dokuma bezemesi sanısı veren boyalı veya desenli kumaş"}],"lexicalization_note":"Tanım yalın bir kumaş adını ve onu ayıran görünüş özelliğini verir; genel aldatıcı görünüş anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dokuma bezemesi, renk etkisi, boyama, resimli kumaş ve yüzeyle yanıltma sınırlarını gösteren beş aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal boya veya desenin dokuma bezemesi sanısı vermesine dayanır; komşu dal gerçek dokuma bezemesi ve onun üretimiyle ilgilidir.","focus_only":"Boya veya yüzey deseniyle gerçek dokuma bezemesi varmış izlenimi veren kumaşı adlandırır.","gloss":"bezemeye benzeyen boya ile gerçek dokuma bezemesi","neighbor_only":"Kumaştaki gerçek dokuma bezemesini, kenar süslemesini ve bu işi yapanları kapsar.","neighbor_ref":"root_000340/B004","relation_type":"near_neighbor","shared_zone":"Kumaş yüzeyindeki bezeme görünüşü iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal dokuma bezemesi sanısına dayanır; komşu dal kumaş renginin bakışa göre değişmesine dayanır.","focus_only":"Birden çok boya veya desenle dokunmuş gibi görünen kumaşı bildirir.","gloss":"boyalı desen yanılsaması ile değişken renk görünüşü","neighbor_only":"Bakış açısına göre renkleri değişiyormuş gibi görünen belirli bir kumaş türünü bildirir.","neighbor_ref":"root_001252/B010","relation_type":"near_neighbor","shared_zone":"Renkli bir kumaşın görünüşünün algıda özel bir etki oluşturması iki dalda ortaktır."},{"boundary_match":"field_only","distinction":"Odak dal bezeme sanısı veren tasarlanmış görünüşü adlandırır; komşu dal belirli renkleri ve boyanın düzensiz tutmasını konu alır.","focus_only":"Çok renkli boya veya desenin dokuma bezemesi izlenimi vermesini temel alır.","gloss":"yanıltıcı bezeme ile alacalı boya","neighbor_only":"Sarı boya, belirli bitkisel renkler ve boyanın alacalı ya da iyi tutmamış çıkmasını kapsar.","neighbor_ref":"root_001428/B005","relation_type":"same_field","shared_zone":"Her iki dal da boyanmış kumaşın renk ve yüzey görünüşü alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal üretim biçimini olduğundan farklı gösteren genel bezeme izlenimine dayanır; komşu dal belirli resim motifleriyle tanımlanır.","focus_only":"Boyanmış veya desenlenmiş yüzeyin dokuma bezemesi sanısı vermesini bildirir.","gloss":"bezeme sanısı veren kumaş ile resimli kumaş","neighbor_only":"Üzerinde kule biçimleri veya başka resimler bulunan belirli bir süslü kumaşı bildirir.","neighbor_ref":"root_000101/B005","relation_type":"same_field","shared_zone":"İki dal da yüzeyi resim veya desenle süslenmiş kumaşları konu alır."},{"boundary_match":"thematic_only","distinction":"Odak dal yalnız kumaş ve dokuma bezemesi görünüşüne bağlıdır; komşu dal metal kaplama işleminden genel yanıltıcı gösterime uzanır.","focus_only":"Kumaşta boya veya desenin dokuma bezemesi sanısı uyandırmasını bildirir.","gloss":"kumaş görünüşü ile kaplama yoluyla yanıltma","neighbor_only":"Bir metali altın veya gümüşle kaplamayı ve bir şeyi gerçek niteliğinden farklı göstermeyi bildirir.","neighbor_ref":"root_001458/B005","relation_type":"thematic","shared_zone":"Bir nesnenin yüzey işlemiyle üretim veya madde niteliğinden farklı görünmesi iki alanda ortaktır."}],"source_phrase_ar":"الكذابة ثوب يصبغ بألوان الصبغ كأنه موشي (ayn); الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله (mufradat)","source_summary":"Kaynaklar, çeşitli renklerle boyanıp desenlenen ve böylece dokuma bezemesi varmış gibi görünen bir kumaş üzerinde birleşir; toplu kanıt bu yanıltıcı görünüşü adlandırmanın gerekçesi olarak açıklar.","sources":["AY","MU"],"what_is_ar":"يدخل فيه الكذابة للثوب المصبوغ بألوان أو المنقوش كأنه موشى لأنه يكذب بحاله","what_is_not_ar":"لا يدخل فيه الكذب في القول، ولا التكذيب، ولا أسماء الأشخاص"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["91:11:1"],"branch_refs":[],"candidate_id":"cand_c1a21e626f5d363b00d9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"91:11:1:agency-and-cause-kept-distinct","source_type":"word_analysis","support_ids":["sup_1c0c4d7ccca6db2a3e05","sup_483335a1ad2de7fad6f8"],"title":"agent distinct from cause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:1","qac_refs":["91:11:1:1"],"status":"accepted"}},{"anchor_refs":["91:11:1"],"branch_refs":[],"candidate_id":"cand_4c3e15147bfb91cc0e83","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"91:11:1:completed-corporate-denial","source_type":"word_analysis","support_ids":["sup_1c0c4d7ccca6db2a3e05","sup_6eba132ab2043569ca7c"],"title":"completed corporate denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:1","qac_refs":["91:11:1:1"],"status":"accepted"}},{"anchor_refs":["91:11:1"],"branch_refs":[],"candidate_id":"cand_bc2a1a5825f313452155","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"91:11:1:narrative-launch-and-forward-dependence","source_type":"word_analysis","support_ids":["sup_1c0c4d7ccca6db2a3e05","sup_630ed058f05ee720150f"],"title":"narrative launch after maxim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:1","qac_refs":["91:11:1:1"],"status":"accepted"}},{"anchor_refs":["91:11:1"],"branch_refs":[],"candidate_id":"cand_94c533ce23c9fda0fd77","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"91:11:1:objectless-compression","source_type":"word_analysis","support_ids":["sup_1c0c4d7ccca6db2a3e05","sup_77f1ee20c5cacfa16487"],"title":"objectless denial clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:1","qac_refs":["91:11:1:1"],"status":"accepted"}},{"anchor_refs":["91:11:1"],"branch_refs":[],"candidate_id":"cand_81c3b80bda8e83c8d154","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"91:11:1:sound-weight","source_type":"word_analysis","support_ids":["sup_1c0c4d7ccca6db2a3e05","sup_a9df07ecc7ef89ecf92c"],"title":"heavy denial sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:1","qac_refs":["91:11:1:1"],"status":"accepted"}},{"anchor_refs":["91:11:1"],"branch_refs":[],"candidate_id":"cand_d023319f2e98d90f90db","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"91:11:1:thamud-denial-formula","source_type":"word_analysis","support_ids":["sup_1c0c4d7ccca6db2a3e05","sup_5d345dc980584c05789c"],"title":"formulaic Thamud denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:1","qac_refs":["91:11:1:1"],"status":"accepted"}},{"anchor_refs":["91:11:1"],"branch_refs":[],"candidate_id":"cand_0ec675d9181b693c1a8e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"91:11:1:truth-falsehood-range","source_type":"word_analysis","support_ids":["sup_1c0c4d7ccca6db2a3e05","sup_961fbe4039de0bb0141d"],"title":"denial with falsifying pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:1","qac_refs":["91:11:1:1"],"status":"accepted"}},{"anchor_refs":["91:11:2"],"branch_refs":[],"candidate_id":"cand_3db353305649d28a18e8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:2:collective-grammar-and-owned-transgression","source_type":"word_analysis","support_ids":["sup_3c0ecceeb32a6044a5e7","sup_3e2d08a65606a9ff8f40"],"title":"collective responsibility chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:2","qac_refs":["91:11:2:1"],"status":"accepted"}},{"anchor_refs":["91:11:2"],"branch_refs":[],"candidate_id":"cand_b70f2ea31fe83f5c9741","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:2:denial-paired-identity","source_type":"word_analysis","support_ids":["sup_3c0ecceeb32a6044a5e7","sup_4ea6acc5d4260567f157"],"title":"denial-paired identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:2","qac_refs":["91:11:2:1"],"status":"accepted"}},{"anchor_refs":["91:11:2"],"branch_refs":[],"candidate_id":"cand_a17232e85357529389b4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:2:exemplum-and-forward-bridge","source_type":"word_analysis","support_ids":["sup_3c0ecceeb32a6044a5e7","sup_c59564dfb6506be57a55"],"title":"from maxim to narrative agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:2","qac_refs":["91:11:2:1"],"status":"accepted"}},{"anchor_refs":["91:11:2"],"branch_refs":[],"candidate_id":"cand_f467a07ee1c138fed830","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:2:name-declension-variant","source_type":"word_analysis","support_ids":["sup_3c0ecceeb32a6044a5e7","sup_7378ea10458254c93810"],"title":"proper-name declension variant","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:2","qac_refs":["91:11:2:1"],"status":"accepted"}},{"anchor_refs":["91:11:2"],"branch_refs":[],"candidate_id":"cand_28ef3b29964994518906","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:2:named-nominative-subject","source_type":"word_analysis","support_ids":["sup_3c0ecceeb32a6044a5e7","sup_9814ff74dafdaf6a792e"],"title":"named nominative subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:2","qac_refs":["91:11:2:1"],"status":"accepted"}},{"anchor_refs":["91:11:2"],"branch_refs":[],"candidate_id":"cand_f740ca81207c1c31106f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:2:scarcity-excess-etymological-pressure","source_type":"word_analysis","support_ids":["sup_3c0ecceeb32a6044a5e7","sup_8ac445ce264a2260afff"],"title":"scarcity beside excess","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:2","qac_refs":["91:11:2:1"],"status":"accepted"}},{"anchor_refs":["91:11:3"],"branch_refs":[],"candidate_id":"cand_6795d44a71eddd4b62d8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:3:associative-characterization","source_type":"word_analysis","support_ids":["sup_6b055744d70e31f4a22a","sup_ff976e22fa106d8f815c"],"title":"association and characterization","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:3","qac_refs":["91:11:3:1"],"status":"accepted"}},{"anchor_refs":["91:11:3"],"branch_refs":[],"candidate_id":"cand_4a6f012d55109de5a247","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:3:audible-fusion-with-rare-noun","source_type":"word_analysis","support_ids":["sup_d52ef7af0d5971b651d0","sup_ff976e22fa106d8f815c"],"title":"audible fusion with final noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:3","qac_refs":["91:11:3:1"],"status":"accepted"}},{"anchor_refs":["91:11:3"],"branch_refs":[],"candidate_id":"cand_edf424f592fce716e8f7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:3:causal-instrumental-mechanism","source_type":"word_analysis","support_ids":["sup_fc5cf293fb3edc688ec3","sup_ff976e22fa106d8f815c"],"title":"cause and means of denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:3","qac_refs":["91:11:3:1"],"status":"accepted"}},{"anchor_refs":["91:11:3"],"branch_refs":[],"candidate_id":"cand_7140f16bf1f60665605f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:3:forward-time-frame","source_type":"word_analysis","support_ids":["sup_b5c4912e604fbe683a1a","sup_ff976e22fa106d8f815c"],"title":"cause before time frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:3","qac_refs":["91:11:3:1"],"status":"accepted"}},{"anchor_refs":["91:11:3"],"branch_refs":[],"candidate_id":"cand_4e167db89aa45e4a6231","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:3:live-semantic-pivot","source_type":"word_analysis","support_ids":["sup_a364d6ac9bb8ff43906d","sup_ff976e22fa106d8f815c"],"title":"live relation pivot","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:3","qac_refs":["91:11:3:1"],"status":"accepted"}},{"anchor_refs":["91:11:3"],"branch_refs":[],"candidate_id":"cand_dba5ea0edcb49b868656","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:3:postponed-explanatory-tail","source_type":"word_analysis","support_ids":["sup_a7b482dd7d59c81c46e4","sup_ff976e22fa106d8f815c"],"title":"postponed explanation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:3","qac_refs":["91:11:3:1"],"status":"accepted"}},{"anchor_refs":["91:11:3"],"branch_refs":[],"candidate_id":"cand_feb5f0cfbcb43e760556","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:3:scope-and-bound-governance","source_type":"word_analysis","support_ids":["sup_9338da69a0972a46201a","sup_ff976e22fa106d8f815c"],"title":"bound scope controller","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:3","qac_refs":["91:11:3:1"],"status":"accepted"}},{"anchor_refs":["91:11:4"],"branch_refs":[],"candidate_id":"cand_6091c8b75c8cebe82bf6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:4:ayah-final-sound-and-cadence","source_type":"word_analysis","support_ids":["sup_10ebb8998147d973e58d","sup_8b7aed20761c4184f6dc"],"title":"load-bearing final cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:4","qac_refs":["91:11:3:2","91:11:3:3"],"status":"accepted"}},{"anchor_refs":["91:11:4"],"branch_refs":[],"candidate_id":"cand_a09470b5f8c32988b0a1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:4:collective-and-intertextual-boundary-scenes","source_type":"word_analysis","support_ids":["sup_8b7aed20761c4184f6dc","sup_b34688593ec991541207"],"title":"collective boundary scenes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:4","qac_refs":["91:11:3:2","91:11:3:3"],"status":"accepted"}},{"anchor_refs":["91:11:4"],"branch_refs":[],"candidate_id":"cand_d2cf815b1e4b7158a541","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:4:forward-and-backward-narrative-bridge","source_type":"word_analysis","support_ids":["sup_8b7aed20761c4184f6dc","sup_fc878f1e6190ad0ec8f8"],"title":"from buried soul to acting agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:4","qac_refs":["91:11:3:2","91:11:3:3"],"status":"accepted"}},{"anchor_refs":["91:11:4"],"branch_refs":[],"candidate_id":"cand_4f0bded60bc092c18d40","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:4:governed-explanatory-verbal-noun","source_type":"word_analysis","support_ids":["sup_2eba989eb1219966bbf0","sup_8b7aed20761c4184f6dc"],"title":"governed explanatory noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:4","qac_refs":["91:11:3:2","91:11:3:3"],"status":"accepted"}},{"anchor_refs":["91:11:4"],"branch_refs":[],"candidate_id":"cand_26de77ca202181be36d3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:4:overflow-moral-transgression","source_type":"word_analysis","support_ids":["sup_8b7aed20761c4184f6dc","sup_aaf1e83bcdb16a7594ae"],"title":"moral overflow image","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:4","qac_refs":["91:11:3:2","91:11:3:3"],"status":"accepted"}},{"anchor_refs":["91:11:4"],"branch_refs":[],"candidate_id":"cand_33a792f592cb4fd3eb38","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:4:overreach-family-pressure","source_type":"word_analysis","support_ids":["sup_067785e2584e807c792b","sup_8b7aed20761c4184f6dc"],"title":"overreach family pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:4","qac_refs":["91:11:3:2","91:11:3:3"],"status":"accepted"}},{"anchor_refs":["91:11:4"],"branch_refs":[],"candidate_id":"cand_aaf7c6484c1a1debf5ce","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:4:owned-collective-transgression","source_type":"word_analysis","support_ids":["sup_411d8fd03ef493abad2c","sup_8b7aed20761c4184f6dc"],"title":"owned collective excess","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:4","qac_refs":["91:11:3:2","91:11:3:3"],"status":"accepted"}},{"anchor_refs":["91:11:4"],"branch_refs":[],"candidate_id":"cand_ef40f5fae2dabe441bd9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:4:pronoun-referent-shift","source_type":"word_analysis","support_ids":["sup_52a386dee7cb8984d89f","sup_8b7aed20761c4184f6dc"],"title":"suffix referent shift","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:4","qac_refs":["91:11:3:2","91:11:3:3"],"status":"accepted"}},{"anchor_refs":["91:11:4"],"branch_refs":[],"candidate_id":"cand_43ed77833624bd968786","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:11:4:rare-form-and-vowel-variant","source_type":"word_analysis","support_ids":["sup_360cb8cc020a48e98d33","sup_8b7aed20761c4184f6dc"],"title":"rare final form and variant","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:11:4","qac_refs":["91:11:3:2","91:11:3:3"],"status":"accepted"}},{"anchor_refs":["91:11:1"],"branch_refs":[],"candidate_id":"cand_b29b4aac046f49f3767f","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"91:11:1:1","source_type":"qac_morpheme","support_ids":["sup_2ae8d494e307434ed0da"],"title":"QAC root occurrence: ك ذ ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:11:3"],"branch_refs":[],"candidate_id":"cand_bfd2af9b0912fa919c7b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"91:11:3:2","source_type":"qac_morpheme","support_ids":["sup_ead1765d6718b9b5fc71"],"title":"QAC root occurrence: ط غ ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:11","branch_refs":["root_000937/B001","root_001290/B002"],"candidate_id":"cand_41a3ca2ecaf0356b829c","commentary_obligation":"review","hft_ref":"hft_ddedc2f791738264138c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_collective_falsification","source_type":"hft","support_ids":["sup_f960e33e9b5593b03180"],"title":"baseline_collective_falsification","trust":"legacy_unbound"},{"anchor_refs":["91:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:11","branch_refs":["root_000937/B001","root_001290/B004"],"candidate_id":"cand_c7a4d4d9fc5856f19727","commentary_obligation":"review","hft_ref":"hft_e32b0811153ab43dc364","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_failed_charge","source_type":"hft","support_ids":["sup_2eb24e1ef5474661de6d"],"title":"baseline_failed_charge","trust":"legacy_unbound"},{"anchor_refs":["91:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:11","branch_refs":["root_000937/B002","root_001290/B002"],"candidate_id":"cand_816617fd62e44f6be880","commentary_obligation":"review","hft_ref":"hft_930a9ec67e4dbd10d251","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_denial_as_overflow","source_type":"hft","support_ids":["sup_80adfaa6f7c0e8ecf39a"],"title":"baseline_denial_as_overflow","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ","qac_morphemes":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"91:11:1:1","qac_word_ref":"91:11:1","root_ar":"ك ذ ب","surface_ar":"كَذَّبَتْ"},{"lemma_ar":"ثَمُود","morph_features":"STEM|POS:PN|LEM:vamuwd|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"91:11:2:1","qac_word_ref":"91:11:2","root_ar":"","surface_ar":"ثَمُودُ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"91:11:3:1","qac_word_ref":"91:11:3","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","root_ar":"ط غ ي","surface_ar":"طَغْوَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:11:3:3","qac_word_ref":"91:11:3","root_ar":"","surface_ar":"هَآ"}],"word_analysis_qac_refs":[["91:11:1:1"],["91:11:2:1"],["91:11:3:1"],["91:11:3:2","91:11:3:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["91:11:1","91:11:2","91:11:3","91:11:4"]},"focus_surface_evidence":{"arabic_uthmani":"كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ","qac_morphemes":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"91:11:1:1","qac_word_ref":"91:11:1","root_ar":"ك ذ ب","surface_ar":"كَذَّبَتْ"},{"lemma_ar":"ثَمُود","morph_features":"STEM|POS:PN|LEM:vamuwd|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"91:11:2:1","qac_word_ref":"91:11:2","root_ar":"","surface_ar":"ثَمُودُ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"91:11:3:1","qac_word_ref":"91:11:3","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"طَغْوَىٰ","morph_features":"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:11:3:2","qac_word_ref":"91:11:3","root_ar":"ط غ ي","surface_ar":"طَغْوَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:11:3:3","qac_word_ref":"91:11:3","root_ar":"","surface_ar":"هَآ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["91:11:1:1"],["91:11:2:1"],["91:11:3:1"],["91:11:3:2","91:11:3:3"]],"word_analysis_refs":["91:11:1","91:11:2","91:11:3","91:11:4"],"word_rows":[{"analysis_record_ref":"91:11:1","analytic_gloss_range_en":"completed active Form II denial or declaring false; locally objectless, emphatic, and assigned to the named collective rather than to an explicit object","analytic_root_gloss_range_en":"truth-falsehood range spanning lying, denial, declaring false, and derived falsehood labels; local grammar selects Form II denial of truth, not unrelated idiomatic branches","qac_refs":["91:11:1:1"],"root":{"arabic":"ك ذ ب","transliteration":"k-dh-b"},"surface":{"arabic":"كَذَّبَتْ","transliteration":"kadhdhabat"}},{"analysis_record_ref":"91:11:2","analytic_gloss_range_en":"the named historical collective functioning as the nominative subject and antecedent for the possessed transgression; locally evaluated through denial rather than lineage or geography","analytic_root_gloss_range_en":"proper-name field for Thamud with possible contested scarce-water derivation; local use selects the people-name, not inscriptional, geographic, or reconstructed etymological senses","qac_refs":["91:11:2:1"],"root":{"arabic":"ث م و د","transliteration":"th-m-w-d"},"surface":{"arabic":"ثَمُودُ","transliteration":"Thamudu"}},{"analysis_record_ref":"91:11:3","analytic_gloss_range_en":"bound preposition linking denial to the possessed transgression as cause, instrument, accompaniment, or characterization; locally it makes the final noun a governed explanatory phrase","analytic_root_gloss_range_en":null,"qac_refs":["91:11:3:1"],"root":{},"surface":{"arabic":"بِ","transliteration":"bi"}},{"analysis_record_ref":"91:11:4","analytic_gloss_range_en":"their owned transgressive excess as a governed verbal noun explaining the denial; locally moral boundary-crossing with overflow image-pressure, not a free physical flood sense","analytic_root_gloss_range_en":"root range includes exceeding limits, moral rebellion, surging overflow, transgressive false authority, tyrannical overreach, and other remote lexical branches; local use selects owned moral transgression while retaining boundary-overflow imagery","qac_refs":["91:11:3:2","91:11:3:3"],"root":{"arabic":"ط غ و","transliteration":"ṭ-gh-w"},"surface":{"arabic":"طَغْوَىٰهَآ","transliteration":"ṭaghwāhā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["91:11"],"branch_refs":["root_000937/B001","root_001290/B002"],"candidate_id":"cand_41a3ca2ecaf0356b829c","evidence_scope":"focus_ayah","hft_ref":"hft_ddedc2f791738264138c","item_id":"baseline_collective_falsification","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_collective_falsification","support_id":"sup_f960e33e9b5593b03180"},{"anchor_refs":["91:11"],"branch_refs":["root_000937/B001","root_001290/B004"],"candidate_id":"cand_c7a4d4d9fc5856f19727","evidence_scope":"focus_ayah","hft_ref":"hft_e32b0811153ab43dc364","item_id":"baseline_failed_charge","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_failed_charge","support_id":"sup_2eb24e1ef5474661de6d"},{"anchor_refs":["91:11"],"branch_refs":["root_000937/B002","root_001290/B002"],"candidate_id":"cand_816617fd62e44f6be880","evidence_scope":"focus_ayah","hft_ref":"hft_930a9ec67e4dbd10d251","item_id":"baseline_denial_as_overflow","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_denial_as_overflow","support_id":"sup_80adfaa6f7c0e8ecf39a"}],"diagnostics":[],"lane_counts":{"global":9,"macro":12,"micro":3},"packet_summary":{"ayah_count":15,"focus_ref":"91:11","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ت ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000186","furuq_root_norm":"ت ل و","furuq_source_root_norm":"ت ل و","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000185","furuq_root_norm":"ت ل ل","furuq_source_root_norm":"ت ل ل","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"91:11","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"91:11","lane":"micro","linguistic_source_ref":"91:11","surface_ref":"91:11","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"91:11","target_tokens":[["Semud",["91:11:2"]],["azgınlığı",["91:11:3"]],["yüzünden",["91:11:3"]],["yalanladı",["91:11:1"]]],"text":"Semud, azgınlığı yüzünden yalanladı."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":15,"id":"s091-p01-001-015","label":"Whole surah","number":1,"refs":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:4:overreach-family-pressure","source_type":"word_analysis","support_id":"sup_067785e2584e807c792b","text":"{\"blocking_evidence\":null,\"headline\":\"overreach family pressure\",\"reader_payoff\":\"The reader sees the transgression as limit-breaking overreach with wider moral force, while the local word remains the possessed verbal noun.\",\"reason\":\"Related accepted branches can supply root-family pressure, but the local form does not activate false-authority or tyrant nouns as direct senses.\",\"representative_source_ids\":[\"QS-a1fc0a63\",\"QS-bf513ee7\",\"QS-a06f3660\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:4:ayah-final-sound-and-cadence","source_type":"word_analysis","support_id":"sup_10ebb8998147d973e58d","text":"{\"blocking_evidence\":null,\"headline\":\"load-bearing final cadence\",\"reader_payoff\":\"The reader hears the causal noun expand at the ayah's close, where sound and meaning land together.\",\"reason\":\"The word is final in the ayah, and the CRITICAL rows tie its sound, rare form, and semantic load to the closing position.\",\"representative_source_ids\":[\"QP-1da5539d\",\"QP-848ddd4e\",\"QY-0f4cca68\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:1","source_type":"word_analysis","support_id":"sup_1c0c4d7ccca6db2a3e05","text":"{\"gloss_range\":\"completed active Form II denial or declaring false; locally objectless, emphatic, and assigned to the named collective rather than to an explicit object\",\"prose\":\"{{ar:كَذَّبَتْ}} ({{tr:kadhdhabat}}) opens the exemplum with a completed active denial: the act is already decisive, emphatic in Form II, and assigned to {{ar:ثَمُودُ}} ({{tr:Thamudu}}) as one collective body. The verb does not name an object, so the denial stays compressed until the later narrative specifies the messenger and sign; that omission lets the first word carry a broad falsifying posture rather than a single stated target. The following transgression phrase can drive the denial without becoming its grammatical agent, so responsibility stays on the people while the cause or means is diagnosed after them. The root field keeps lying and declaring false close to denial, while the local form selects rejection of truth rather than a mere report that they lied or a proof that someone else lied. As the first narrative beat after 91:9-10, the word turns the moral maxim into a historical case; it also participates in the Thamud-denial formula (26:141; 54:23; 91:11), and 91:14 moves from corporate denial to directed denial of the messenger. Its dense sound and adjacency to {{ar:طَغْوَىٰهَآ}} ({{tr:ṭaghwāhā}}) make denial and transgressive excess feel like the two heavy poles of the ayah.\",\"root_display\":\"{{ar:ك ذ ب}} ({{tr:k-dh-b}})\",\"root_gloss_range\":\"truth-falsehood range spanning lying, denial, declaring false, and derived falsehood labels; local grammar selects Form II denial of truth, not unrelated idiomatic branches\",\"surface_display\":\"{{ar:كَذَّبَتْ}} ({{tr:kadhdhabat}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:11:1:1","source_type":"qac_morpheme","support_id":"sup_2ae8d494e307434ed0da","text":"{\"lemma_ar\":\"كَذَّبَ\",\"morph_features\":\"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3FS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"91:11:1:1\",\"qac_word_ref\":\"91:11:1\",\"root_ar\":\"ك ذ ب\",\"surface_ar\":\"كَذَّبَتْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:4:governed-explanatory-verbal-noun","source_type":"word_analysis","support_id":"sup_2eba989eb1219966bbf0","text":"{\"blocking_evidence\":null,\"headline\":\"governed explanatory noun\",\"reader_payoff\":\"The reader notices that the final word tells how the denial operates, not merely what else Thamud did.\",\"reason\":\"QAC marks a verbal noun, and attachment evidence makes it the governed complement of {{ar:بِ}} ({{tr:bi}}).\",\"representative_source_ids\":[\"QG-69e18678\",\"QG-dbef97f4\",\"QY-e90209e0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:4:rare-form-and-vowel-variant","source_type":"word_analysis","support_id":"sup_360cb8cc020a48e98d33","text":"{\"blocking_evidence\":null,\"headline\":\"rare final form and variant\",\"reader_payoff\":\"The reader notices that the final noun is not a routine term; its form and variant make the ayah's causal close unusually concentrated.\",\"reason\":\"Contextual evidence marks the exact form as low occurrence, and the variant functions as form pressure rather than a replacement of the aligned surface.\",\"representative_source_ids\":[\"QF-82841baa\",\"QF-9ac1463c\",\"QH-9defc062\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:2","source_type":"word_analysis","support_id":"sup_3c0ecceeb32a6044a5e7","text":"{\"gloss_range\":\"the named historical collective functioning as the nominative subject and antecedent for the possessed transgression; locally evaluated through denial rather than lineage or geography\",\"prose\":\"{{ar:ثَمُودُ}} ({{tr:Thamudu}}) is not a generic crowd label; it is the nominative proper-name subject that turns the preceding moral rule into a named historical proof-case. The grammar treats the people as one collective actor: the verb agrees with them as a unit, and the final suffix in {{ar:طَغْوَىٰهَآ}} ({{tr:ṭaghwāhā}}) routes the transgression back to that same collective. The diptote/triptote variant keeps the name's morphological status audible as resistant proper-name behavior versus full declension, while the local syntax still selects the acting people, not an inscription, region, or archaeological label. A possible scarce-water derivation may add scarcity-versus-overflow pressure beside the ayah's overflow term and the camel-water sign in 91:13, but it remains etymological pressure rather than the local sense. The name also arrives loaded by the Quranic Thamud-denial pattern, and 91:12-13 carry the collective subject forward toward the individual agent and the messenger.\",\"root_display\":\"{{ar:ث م و د}} ({{tr:th-m-w-d}})\",\"root_gloss_range\":\"proper-name field for Thamud with possible contested scarce-water derivation; local use selects the people-name, not inscriptional, geographic, or reconstructed etymological senses\",\"surface_display\":\"{{ar:ثَمُودُ}} ({{tr:Thamudu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:2:collective-grammar-and-owned-transgression","source_type":"word_analysis","support_id":"sup_3e2d08a65606a9ff8f40","text":"{\"blocking_evidence\":null,\"headline\":\"collective responsibility chain\",\"reader_payoff\":\"The reader notices that the ayah's responsibility logic is grammatical: the denier and the owner of the transgression are the same collective.\",\"reason\":\"Attachment cross-references strongly license the final possessive suffix as referring back to the collective subject.\",\"representative_source_ids\":[\"QG-56b34035\",\"QG-f0deac22\",\"QY-c4e3f453\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:4:owned-collective-transgression","source_type":"word_analysis","support_id":"sup_411d8fd03ef493abad2c","text":"{\"blocking_evidence\":null,\"headline\":\"owned collective excess\",\"reader_payoff\":\"The reader sees that the denial is explained by their own excess, not by a general moral category detached from them.\",\"reason\":\"Attachment evidence strongly licenses the final suffix as referring back to {{ar:ثَمُودُ}} ({{tr:Thamudu}}), making the transgression possessed by the collective subject.\",\"representative_source_ids\":[\"QG-4479cbcf\",\"QG-4e17571a\",\"QF-44dfc107\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:1:agency-and-cause-kept-distinct","source_type":"word_analysis","support_id":"sup_483335a1ad2de7fad6f8","text":"{\"blocking_evidence\":null,\"headline\":\"agent distinct from cause\",\"reader_payoff\":\"The reader sees that transgression explains the denial without replacing the people as the responsible agent.\",\"reason\":\"The subject relation and the governed explanatory phrase are both syntactically forced.\",\"representative_source_ids\":[\"QS-5ca28c9c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:2:denial-paired-identity","source_type":"word_analysis","support_id":"sup_4ea6acc5d4260567f157","text":"{\"blocking_evidence\":null,\"headline\":\"denial-paired identity\",\"reader_payoff\":\"The reader recognizes that the people-name is not neutral in this clause; it is activated through a recurring denial frame.\",\"reason\":\"The contextual profiles and CRITICAL rows support repeated Thamud-denial pairing, while the local ayah adds the explanatory phrase.\",\"representative_source_ids\":[\"QI-80794f31\",\"QI-cd613324\",\"MI-8c3e9c22\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:4:pronoun-referent-shift","source_type":"word_analysis","support_id":"sup_52a386dee7cb8984d89f","text":"{\"blocking_evidence\":null,\"headline\":\"suffix referent shift\",\"reader_payoff\":\"The reader tracks the shift from individual soul-failure in 91:10 to collective owned transgression in 91:11.\",\"reason\":\"The local cross-reference strongly licenses the suffix as referring to {{ar:ثَمُودُ}} ({{tr:Thamudu}}), not carrying over the prior referent.\",\"representative_source_ids\":[\"QG-e956ee8b\",\"QE-7dcc1337\",\"QB-b2777518\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:1:thamud-denial-formula","source_type":"word_analysis","support_id":"sup_5d345dc980584c05789c","text":"{\"blocking_evidence\":null,\"headline\":\"formulaic Thamud denial\",\"reader_payoff\":\"The reader recognizes the local clause as part of a familiar Thamud-denial pattern, while 91:14 gives the local reprise.\",\"reason\":\"Contextual profiles show recurring Thamud references, and the CRITICAL rows give concrete formula references including 26:141, 54:23, 91:11, and the same-surah reprise at 91:14.\",\"representative_source_ids\":[\"QI-d5a17281\",\"MI-f6ec37ae\",\"QE-27d9bce9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:1:narrative-launch-and-forward-dependence","source_type":"word_analysis","support_id":"sup_630ed058f05ee720150f","text":"{\"blocking_evidence\":null,\"headline\":\"narrative launch after maxim\",\"reader_payoff\":\"The reader hears the word as the hinge from 91:9-10's moral rule into a narrated proof-case that 91:12-14 continues.\",\"reason\":\"The clause begins with the verb before the named subject and remains a complete narrative opening that the following ayahs specify further.\",\"representative_source_ids\":[\"QT-30cbe750\",\"QT-5e2d5339\",\"QB-5872b0b8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:3:associative-characterization","source_type":"word_analysis","support_id":"sup_6b055744d70e31f4a22a","text":"{\"blocking_evidence\":null,\"headline\":\"association and characterization\",\"reader_payoff\":\"The reader notices that the phrase can describe the moral condition of the deniers as well as the mechanism of their denial.\",\"reason\":\"The local guardrail allows a cause-or-manner range; the associative reading is kept as a live nuance without overturning the governed complement.\",\"representative_source_ids\":[\"QG-4dfae24c\",\"QG-e631c365\",\"QS-c03810cf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:1:completed-corporate-denial","source_type":"word_analysis","support_id":"sup_6eba132ab2043569ca7c","text":"{\"blocking_evidence\":null,\"headline\":\"completed corporate denial\",\"reader_payoff\":\"The reader notices that the ayah begins with a decisive corporate rejection, not an open-ended disposition or unnamed passive event.\",\"reason\":\"QAC and attachment evidence identify an active perfect Form II verb with {{ar:ثَمُودُ}} ({{tr:Thamudu}}) as the explicit subject.\",\"representative_source_ids\":[\"QG-1e60ef94\",\"QG-2088e9f5\",\"QG-3e7c4d3a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:2:name-declension-variant","source_type":"word_analysis","support_id":"sup_7378ea10458254c93810","text":"{\"blocking_evidence\":null,\"headline\":\"proper-name declension variant\",\"reader_payoff\":\"The reader notices that the name's morphology is part of the recited texture, even though both readings keep the same people as subject.\",\"reason\":\"The variant is useful as form evidence; it does not replace the aligned local subject parse.\",\"representative_source_ids\":[\"MG-ef6a4d3d\",\"QF-44db96e9\",\"QF-94cbc506\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:1:objectless-compression","source_type":"word_analysis","support_id":"sup_77f1ee20c5cacfa16487","text":"{\"blocking_evidence\":null,\"headline\":\"objectless denial clause\",\"reader_payoff\":\"The reader feels denial as the headline act before the messenger, sign, or truth-target is specified.\",\"reason\":\"The local frame is marked obj=none_absolute with a following governed prepositional complement, so target recovery remains contextual.\",\"representative_source_ids\":[\"QG-fe8d5053\",\"MG-677f0efb\",\"QT-6fea2bf3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:2:scarcity-excess-etymological-pressure","source_type":"word_analysis","support_id":"sup_8ac445ce264a2260afff","text":"{\"blocking_evidence\":null,\"headline\":\"scarcity beside excess\",\"reader_payoff\":\"The reader can register a scarcity-versus-excess pressure without turning a contested derivation into the meaning of the proper noun.\",\"reason\":\"Local grammar selects the proper-name people sense, while the contested derivation remains only a cautious contrast with {{ar:طَغْوَىٰهَآ}} ({{tr:ṭaghwāhā}}).\",\"representative_source_ids\":[\"QS-ad0e6a3d\",\"QS-d505242f\",\"MS-f9ddb764\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:4","source_type":"word_analysis","support_id":"sup_8b7aed20761c4184f6dc","text":"{\"gloss_range\":\"their owned transgressive excess as a governed verbal noun explaining the denial; locally moral boundary-crossing with overflow image-pressure, not a free physical flood sense\",\"prose\":\"{{ar:طَغْوَىٰهَآ}} ({{tr:ṭaghwāhā}}) is the ayah's load-bearing close: a governed verbal noun, possessed by the same collective that denied, and placed after {{ar:بِ}} ({{tr:bi}}) as the explanation of the act. The suffix makes the excess their own, so the cause is internal to {{ar:ثَمُودُ}} ({{tr:Thamudu}}), not an abstract vice floating outside the story. The root selects moral transgression here, but its overflow field keeps the image of a boundary breached; 69:11 supplies the literal water contrast, while 91:11 turns that force into social and moral overrun. The wider overreach family sharpens the sense toward false authority, tyranny, and excess that drives further denial, while those derivative branches stay as pressure rather than direct local senses. The rare exact form, against the more familiar verbal-noun pattern, and the accepted vowel variant make the final noun unusually exposed, hovering between an act of overstepping and a settled condition of excess without changing the local governed phrase. Its long closing sound joins nearby endings and carries the scene from the buried failure of 91:10 toward the individual who emerges in 91:12 and the divine camel in 91:13.\",\"root_display\":\"{{ar:ط غ و}} ({{tr:ṭ-gh-w}})\",\"root_gloss_range\":\"root range includes exceeding limits, moral rebellion, surging overflow, transgressive false authority, tyrannical overreach, and other remote lexical branches; local use selects owned moral transgression while retaining boundary-overflow imagery\",\"surface_display\":\"{{ar:طَغْوَىٰهَآ}} ({{tr:ṭaghwāhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:3:scope-and-bound-governance","source_type":"word_analysis","support_id":"sup_9338da69a0972a46201a","text":"{\"blocking_evidence\":null,\"headline\":\"bound scope controller\",\"reader_payoff\":\"The reader sees that a one-letter particle supplies the ayah's explanatory architecture.\",\"reason\":\"QAC marks a preposition, and attachment evidence makes the final noun governed by it as the complement.\",\"representative_source_ids\":[\"QG-283f5d59\",\"QF-a765e5d0\",\"QT-3b13abe7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:1:truth-falsehood-range","source_type":"word_analysis","support_id":"sup_961fbe4039de0bb0141d","text":"{\"blocking_evidence\":null,\"headline\":\"denial with falsifying pressure\",\"reader_payoff\":\"The reader notices that the act is more than nonacceptance: it is a posture of treating truth as false.\",\"reason\":\"V4 separates general falsehood from declaring something false; local Form II and the objectless narrative frame select the declaring-false branch while retaining falsehood pressure.\",\"representative_source_ids\":[\"MG-d2aa4e44\",\"QS-ab7f2232\",\"QF-48d2b16e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:2:named-nominative-subject","source_type":"word_analysis","support_id":"sup_9814ff74dafdaf6a792e","text":"{\"blocking_evidence\":null,\"headline\":\"named nominative subject\",\"reader_payoff\":\"The reader sees the universal moral verdict anchored in a specific responsible community.\",\"reason\":\"QAC marks a proper noun, and attachment evidence makes it the nominative explicit subject of {{ar:كَذَّبَتْ}} ({{tr:kadhdhabat}}).\",\"representative_source_ids\":[\"QG-23a79adf\",\"QG-b8bd9e50\",\"QS-29dab7ab\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:3:live-semantic-pivot","source_type":"word_analysis","support_id":"sup_a364d6ac9bb8ff43906d","text":"{\"blocking_evidence\":null,\"headline\":\"live relation pivot\",\"reader_payoff\":\"The reader notices that the ayah's precision comes from a compressed relation, not from spelling out one flat causal term.\",\"reason\":\"The local grammar licenses a governed explanatory phrase, while translation support warns that target language may force a choice between values.\",\"representative_source_ids\":[\"MG-e2390ecf\",\"QY-f936713f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:3:postponed-explanatory-tail","source_type":"word_analysis","support_id":"sup_a7b482dd7d59c81c46e4","text":"{\"blocking_evidence\":null,\"headline\":\"postponed explanation\",\"reader_payoff\":\"The reader experiences the ayah first as act and actor, then as diagnosis.\",\"reason\":\"The clause order is verb, subject, then prepositional complement.\",\"representative_source_ids\":[\"QT-201efb7c\",\"MT-428abe17\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:1:sound-weight","source_type":"word_analysis","support_id":"sup_a9df07ecc7ef89ecf92c","text":"{\"blocking_evidence\":null,\"headline\":\"heavy denial sound\",\"reader_payoff\":\"The reader hears the denial as stressed and compact rather than light, matching its moral force.\",\"reason\":\"The sound observation is kept modestly tied to the visible Form II surface and its pairing with the ayah-final transgression noun.\",\"representative_source_ids\":[\"QP-050c7ef4\",\"QP-cbb6371e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:4:overflow-moral-transgression","source_type":"word_analysis","support_id":"sup_aaf1e83bcdb16a7594ae","text":"{\"blocking_evidence\":null,\"headline\":\"moral overflow image\",\"reader_payoff\":\"The reader feels Thamud's denial as conduct breaching its banks, not just as a flat moral label.\",\"reason\":\"V4 supports both overstepping-limit and surging-beyond-bounds branches; local grammar selects moral transgression while the overflow branch survives as image pressure, including the contrast with 69:11.\",\"representative_source_ids\":[\"QS-770ba842\",\"QS-db0a1d67\",\"MS-0522ba9c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:4:collective-and-intertextual-boundary-scenes","source_type":"word_analysis","support_id":"sup_b34688593ec991541207","text":"{\"blocking_evidence\":null,\"headline\":\"collective boundary scenes\",\"reader_payoff\":\"The reader sees 91:11 as moral overflow by a people, in contrast with literal water overflow in 69:11.\",\"reason\":\"The CRITICAL rows give the concrete 69:11 contrast, while local reference and grammar keep 91:11 focused on the named collective.\",\"representative_source_ids\":[\"QI-99e560bd\",\"QI-9c04c989\",\"MI-b21b548b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:3:forward-time-frame","source_type":"word_analysis","support_id":"sup_b5c4912e604fbe683a1a","text":"{\"blocking_evidence\":null,\"headline\":\"cause before time frame\",\"reader_payoff\":\"The reader sees that the ayah diagnoses why or how before the next ayah tells when it broke into action.\",\"reason\":\"The local clause is complete, while the following ayah supplies the temporal scene.\",\"representative_source_ids\":[\"QB-51b279f5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:2:exemplum-and-forward-bridge","source_type":"word_analysis","support_id":"sup_c59564dfb6506be57a55","text":"{\"blocking_evidence\":null,\"headline\":\"from maxim to narrative agent\",\"reader_payoff\":\"The reader sees how a universal moral warning becomes a named communal scene that 91:12-13 develops.\",\"reason\":\"The named subject completes the 91:11 clause and provides the referential base for the following narrative development.\",\"representative_source_ids\":[\"QT-ca990d9c\",\"MT-d4e8c380\",\"QB-015ecf1d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:3:audible-fusion-with-rare-noun","source_type":"word_analysis","support_id":"sup_d52ef7af0d5971b651d0","text":"{\"blocking_evidence\":null,\"headline\":\"audible fusion with final noun\",\"reader_payoff\":\"The reader hears the causal bridge as fused to the word that carries the ayah's distinctive semantic load.\",\"reason\":\"The particle is a bound preposition attached to the following governed noun in the surface phrase.\",\"representative_source_ids\":[\"QE-937bbd97\",\"QP-e97508be\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:11:3:2","source_type":"qac_morpheme","support_id":"sup_ead1765d6718b9b5fc71","text":"{\"lemma_ar\":\"طَغْوَىٰ\",\"morph_features\":\"STEM|POS:N|LEM:TagowaY`|ROOT:Tgy|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"91:11:3:2\",\"qac_word_ref\":\"91:11:3\",\"root_ar\":\"ط غ ي\",\"surface_ar\":\"طَغْوَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:3:causal-instrumental-mechanism","source_type":"word_analysis","support_id":"sup_fc5cf293fb3edc688ec3","text":"{\"blocking_evidence\":null,\"headline\":\"cause and means of denial\",\"reader_payoff\":\"The reader sees transgression operating inside the denial as its cause or means, not merely appearing beside it.\",\"reason\":\"Attachment evidence marks the governed phrase as completing the denial, with translation support preserving both cause and manner possibilities.\",\"representative_source_ids\":[\"QG-0bca7751\",\"QS-b7b81713\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:4:forward-and-backward-narrative-bridge","source_type":"word_analysis","support_id":"sup_fc878f1e6190ad0ec8f8","text":"{\"blocking_evidence\":null,\"headline\":\"from buried soul to acting agent\",\"reader_payoff\":\"The reader follows the scale shift from inward failure to collective overflow and then to the person who embodies it.\",\"reason\":\"The final suffix resolves to the collective in 91:11, while the following ayahs carry that collective frame into the individual actor and the divine sign.\",\"representative_source_ids\":[\"QE-0a84ed89\",\"QB-1d884d23\",\"QB-ac4e37a2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:11:3","source_type":"word_analysis","support_id":"sup_ff976e22fa106d8f815c","text":"{\"gloss_range\":\"bound preposition linking denial to the possessed transgression as cause, instrument, accompaniment, or characterization; locally it makes the final noun a governed explanatory phrase\",\"prose\":\"{{ar:بِ}} ({{tr:bi}}) is the small hinge that prevents denial and transgression from standing as two loose assertions. It can make {{ar:طَغْوَىٰهَآ}} ({{tr:ṭaghwāhā}}) the cause, means, accompaniment, or characterizing condition of {{ar:كَذَّبَتْ}} ({{tr:kadhdhabat}}), including the sharper associative possibility that they denied in relation to their own transgression. The ayah therefore keeps causation and characterization close rather than forcing only one English relation. Because it is bound to the following noun, the particle makes the final word a governed explanatory phrase, not a new subject or separate event. Its position after verb and subject delays the explanation until the end of the ayah, and its recitational fusion with the rare final noun lets the causal bridge be heard as one compact phrase. That explanatory phrase then waits for 91:12 to supply the time at which the denial became concrete.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:بِ}} ({{tr:bi}})\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ","ayah_ref":"91:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000937/B001","root_001290/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001290","role":"Declaring a report or its bearer false supplies the core collective verdict.","root":"ك ذ ب","source_ref":"91:11","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000937","role":"Overstepping a proper bound in rebellion supplies the cause and manner of that verdict.","root":"ط غ ي","source_ref":"91:11","source_word_indices":["3"]}],"changed_reading":{"after":"Thamud collectively pronounced truth false, with its own limit-breaking condition functioning as both pressure behind and vehicle of the pronouncement.","before":"Thamud simply disbelieved because it was rebellious."},"confidence":"strong","focus_anchor":"The verb at word 1 makes Thamud the collective agent of declaring false, while the bi-phrase attached to word 3 ties that act to the collective's own excess.","mechanism":"The collective does more than hold an incorrect belief: it issues a verdict that marks a claim or claimant false. The prefixed bi-phrase can carry cause or instrument, so boundary-crossing is both a motive for the verdict and a medium through which it is enforced.","model_id":"baseline_collective_falsification"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_collective_falsification","source_type":"hft","support_id":"sup_f960e33e9b5593b03180","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ","ayah_ref":"91:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000937/B001","root_001290/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001290","role":"A charge that proves false by not being carried through supplies a performance test for denial.","root":"ك ذ ب","source_ref":"91:11","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000937","role":"Rebellious boundary-breaking supplies the failure condition for the entrusted charge.","root":"ط غ ي","source_ref":"91:11","source_word_indices":["3"]}],"changed_reading":{"after":"Denial is also conduct that makes an entrusted charge come out false by refusing to carry it through within its bounds.","before":"Denial is a proposition stated or believed."},"confidence":"medium","focus_anchor":"The same word-1 act can concern whether a charge proves true in performance, and word 3 names the force that pushes performance beyond its proper limit.","mechanism":"Truth and falsehood can be tested by whether an undertaking is carried through. Joined to transgressive overflow, denial can therefore name a failed charge or betrayed obligation, not speech alone.","model_id":"baseline_failed_charge"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_failed_charge","source_type":"hft","support_id":"sup_2eb24e1ef5474661de6d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ","ayah_ref":"91:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000937/B002","root_001290/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001290","role":"Attributing falsehood supplies the judgment imposed by the collective.","root":"ك ذ ب","source_ref":"91:11","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000937","role":"Water or force surging beyond measure supplies a physical model for how the judgment becomes socially overwhelming.","root":"ط غ ي","source_ref":"91:11","source_word_indices":["3"]}],"changed_reading":{"after":"The cause is a surging collective force that overruns a boundary and gives a false verdict practical dominance.","before":"The stated cause is generic moral arrogance."},"confidence":"medium","focus_anchor":"The bi-phrase directly couples the word-1 falsifying act to the word-3 noun whose inventory includes a force rising beyond measure.","mechanism":"The verdict of falsehood is driven by a flood-like social force. Once the collective rises beyond a boundary, denial becomes an overwhelming pressure that can make falsehood operative even without changing what is true.","model_id":"baseline_denial_as_overflow"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_denial_as_overflow","source_type":"hft","support_id":"sup_80adfaa6f7c0e8ecf39a","trust":"legacy_unbound"}]}
</lane_packet_json>
