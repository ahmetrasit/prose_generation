# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **91:8**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s091-regular-20260912/s091/91_8/micro.discovery.json` and modify nothing
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
  "ayah_ref": "91:8",
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
{"branch_registry":[{"boundary":"Anlam, sabah aydınlığını, ahlaki sapmayı ve eli açıklığı değil; fiziksel açılma ile dışarı akışı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001132/B001","candidate_links":[{"candidate_id":"cand_112d51b7c16ffada0528","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فُجُور","morph_features":"STEM|POS:N|LEM:fujuwr|ROOT:fjr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:2:1","qac_word_ref":"91:8:2","surface_ar":"فُجُورَ"}],"gloss":"genişçe yarılma ve içinden suyun akıp çıkması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey genişçe yarılarak içinde bir açıklık oluşturulur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özellikle su, açılan yerden dışarı çıkıp akmaya başlar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Suyun açılıp çıktığı ağızlar ve vadi boşaltımları sonuç ya da yer bildiren kullanımlardır."}}],"root_ar":"ف ج ر","root_id":"root_001132","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel açılma, suyun dışarı akması ve bu akışın çıkış yerleri birlikte kastedildiğinde en kapsamlı karşılıktır.","boundary_detail":"Anlam, sabah aydınlığını, ahlaki sapmayı ve eli açıklığı değil; fiziksel açılma ile dışarı akışı kapsar.","branch_image_ar":"انشقاق واسع وانبعاث","concept_gloss":"genişçe yarılma ve içinden suyun akıp çıkması","contextual_glosses":[{"applicability":"Bir su kaynağının ya da birikmiş suyun açılan yerden güçlü biçimde çıkışını anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel yarma eylemini ve çıkış yeri ya da güzergah bildiren kullanımları dışarıda bırakır.","preserves":"Açılma sonucunda suyun dışarı çıkıp akmasını açıkça korur."},"facet_ids":["F002"],"text":"su yarılan yerden fışkırıp aktı","usage_role":"contextual"}],"definition":"Bir şeyi genişçe yararak açmak ya da böyle bir açıklıktan özellikle suyun akıp çıkmasıdır. Suyun çıktığı ağız, alçak alan ve akış yolu bu sürecin yer bildiren özelleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey genişçe yarılarak içinde bir açıklık oluşturulur."},{"facet_id":"F002","role":"core","statement":"Özellikle su, açılan yerden dışarı çıkıp akmaya başlar."},{"facet_id":"F003","role":"specialization","statement":"Suyun açılıp çıktığı ağızlar ve vadi boşaltımları sonuç ya da yer bildiren kullanımlardır."}],"identity_rationale":"Kaynak ifadesi, bir şeyin genişçe yarılmasını ve özellikle suyun açılan yerden akıp çıkmasını aynı çekirdekte birleştirir. Suyun çıktığı ağızlar ve vadi boşaltım yerleri bu açılma ve akışın yer bildiren özelleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"suyu yarıp akıtma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"su açılıp akmaya başladı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"suyu yarıp dışarı akıttı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çokça açılıp fışkırdı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"suyun açılıp çıktığı yer"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"suyun çıktığı ağız"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"suların ve vadilerin açılıp çıktığı alçak alan"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"vadinin su boşaltım ağızları"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kum içindeki yol"}],"lexicalization_note":"Tanım hem genişçe yarılma çekirdeğini hem de suyla, çıkış yeriyle veya güzergahla sınırlı kullanımları ayrı katmanlar halinde korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma genel açılma, yerden su çıkışı ve doğal su yolu sınırlarını en yararlı biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yarma, akıtma, kendiliğinden akış ve çıkış yerlerini daha geniş biçimde kapsarken komşu dal suyun özellikle yerden pınar olarak çıkışını adlandırır.","focus_only":"Odak dal, geniş yarma eylemini ve suyun çıktığı ağızlarla akış yollarını da kapsar.","gloss":"yerden pınarların açılıp çıkması","neighbor_only":"Komşu dal, yeryüzünün pınarlar halinde açılıp su vermesine özgüdür.","neighbor_ref":"root_001150/B005","relation_type":"near_synonym","shared_zone":"İki dalda da yerin açılması ve suyun bu açıklıktan dışarı çıkması bulunur."},{"boundary_match":"partial","distinction":"Komşu dal genel çatlama ve açılmayı öne çıkarır; odak dal ise geniş yarılmayı suyun çıkışı, akışı ve akış yerleriyle bütünleştirir.","focus_only":"Odak dalda geniş yarılmadan sonra özellikle suyun akıp çıkması kurucu bir sonuçtur.","gloss":"bir şeyin çatlayıp açılması","neighbor_only":"Komşu dal deri, yer, dağ, diş ve sabah gibi çok farklı şeylerin çatlayıp açılmasını kapsar.","neighbor_ref":"root_000807/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal fiziksel bütünlüğün bozulup bir açıklık oluşmasını anlatır."},{"boundary_match":"field_only","distinction":"Odak dal bir yarılma ve dışarı çıkma sürecinden hareket eder; komşu dal ise arazi üzerindeki geçit ya da ayırıcı hattı başlı başına adlandırır.","focus_only":"Odak dalın çekirdeği açıklığın oluşması ve suyun oradan çıkıp akmasıdır.","gloss":"dağ ya da kum arasındaki su geçidi","neighbor_only":"Komşu dal dağlar veya kum arasındaki mevcut geçidi ve suyun izlediği arazi çizgisini adlandırır.","neighbor_ref":"root_001159/B006","relation_type":"same_field","shared_zone":"İki dal suyun geçtiği arazi açıklıkları ve doğal akış yolları alanında buluşur."}],"source_phrase_ar":"التفتح في الشيء (maqayis)؛ انفجر الماء انفجارا تفتح (maqayis)؛ الفجر تفجيرك الماء (ayn;tahdhib)؛ وانفجر الماء وغيره انفجارا إذا انبعث سائلا (jamhara)؛ فجرت الماء فانفجر أي بجسته فانبجس (sihah)؛ شق الشيء شقا واسعا (mufradat)؛ المفجر الموضع الذي ينفجر منه الماء (ayn;tahdhib)؛ الفجرة موضع تفتح الماء (maqayis;sihah)؛ مفاجر الوادي مرافضه (maqayis;sihah)","source_summary":"Kaynaklar genişçe yarılma ile suyun açılıp akmasını ortak çekirdek olarak verir; su çıkışları ve vadi boşaltım yerleri de bu çekirdeğin yer uzantılarıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه شق الشيء شقا واسعا وتفجير الماء وانفجاره وتفجره ومواضع انفتاح الماء ومجاريه","what_is_not_ar":"ليس ضوء الصبح ولا الفجور ولا الجود"},"support_links":["sup_d4164de075e7caa1b4b6"]},{"boundary":"Bu dal fiziksel su çıkışından değil, gecenin sonunda sabah ışığının ortaya çıkmasından söz eder.","branch_kind":"mixed_non_bare","branch_ref":"root_001132/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فُجُور","morph_features":"STEM|POS:N|LEM:fujuwr|ROOT:fjr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:2:1","qac_word_ref":"91:8:2","surface_ar":"فُجُورَ"}],"gloss":"sabah aydınlığının gece karanlığını yararak belirmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sabah aydınlığı, gecenin sonundaki karanlığın içinden belirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu aydınlığın birbirinden ayrılan iki tan görünümü bulunur."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı ışık ve zaman çekirdeği, ufukta yayılan gerçek tan ile dikey görünüp dağılan yalancı tan ayrımında korunur."}}],"root_ar":"ف ج ر","root_id":"root_001132","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tan vaktini yalnız bir saat aralığı olarak değil, ışığın geceden açılıp görünmesi olarak anlatan en kapsamlı karşılıktır.","boundary_detail":"Bu dal fiziksel su çıkışından değil, gecenin sonunda sabah ışığının ortaya çıkmasından söz eder.","branch_image_ar":"انبلاج الصبح من الليل","concept_gloss":"sabah aydınlığının gece karanlığını yararak belirmesi","contextual_glosses":[{"applicability":"Gecenin sona erip sabah aydınlığının görünmeye başladığı doğal bağlamlarda kısa ve akıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karanlığın yarılması imgesini, iki tan görünümünü ve vakte girme kullanımını açıkça söylemez.","preserves":"Sabah ışığının gecenin ardından görünmeye başlamasını doğal biçimde korur."},"facet_ids":["F001"],"text":"tan söktü","usage_role":"general"}],"definition":"Gecenin sonunda karanlığın açılmasıyla sabah aydınlığının belirmesidir. Ufukta yayılan gerçek tan ile dikey görünüp dağılan yalancı tan, bu belirişin ayırt edilen iki görünümüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sabah aydınlığı, gecenin sonundaki karanlığın içinden belirir."},{"facet_id":"F002","role":"specialization","statement":"Bu aydınlığın birbirinden ayrılan iki tan görünümü bulunur."},{"facet_id":"F003","role":"associated_use","statement":"Aynı ışık ve zaman çekirdeği, ufukta yayılan gerçek tan ile dikey görünüp dağılan yalancı tan ayrımında korunur."}],"identity_rationale":"Kaynak ifadesi, gecenin sonundaki karanlığın açılmasıyla sabah aydınlığının belirmesini doğrudan anlatır. İki ayrı tan görünümü bu zaman ve ışık çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tan aydınlığı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ufka yayılan gerçek tan"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"dikey görünüp dağılan yalancı tan"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"tan vaktine girdik"}],"lexicalization_note":"Tanım sabah aydınlığı çekirdeğini korur; iki tan türünü bu çekirdek içinde, başka kullanımları ise kendi sözlüksel birimleriyle sınırlı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen karşılaştırmalar sabahın açılmasıyla güçlü örtüşmeyi ve yalnız zaman bildiren komşu anlamdan farkı gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Doğal sabah bağlamında anlamlar büyük ölçüde örtüşür; odak dal tanın iki görünümünü ayırırken komşu dal açıklık imgesini gerçeğin belirginleşmesine kadar genişletir.","focus_only":"Odak dal sabah aydınlığının iki ayrı tan görünümünü de kapsar.","gloss":"sabahın açılması ve belirginleşmesi","neighbor_only":"Komşu dal sabahın açılmasını, karışık bir konudan sonra gerçeğin belirginleşmesine de aktarır.","neighbor_ref":"root_001176/B002","relation_type":"near_synonym","shared_zone":"İki dalın ortak çekirdeği sabah ışığının gecenin karanlığından açılarak görünmesidir."},{"boundary_match":"partial","distinction":"Komşu dal görünürlük ve aydınlanma durumunu öne çıkarır; odak dal ise bu belirişi gecenin sonundaki tan vakti ve tan türleriyle sınırlar.","focus_only":"Odak dal gecenin sonundaki vakti ve birbirinden ayrılan iki tan görünümünü içerir.","gloss":"sabahın karanlıkta belirip aydınlanması","neighbor_only":"Komşu dalın odağı sabahın karanlık içinde görünür, aydınlık ve seçilir hale gelmesidir.","neighbor_ref":"root_001161/B002","relation_type":"near_synonym","shared_zone":"Her iki dal sabah ışığının gece karanlığı içinde görünmeye başlamasını anlatır."},{"boundary_match":"field_only","distinction":"Odak dal kurucu olarak bir ışık belirişidir; komşu dal ise aynı döneme yakın bir gece vaktinin adıdır ve aydınlanma gerektirmez.","focus_only":"Odak dal sabah ışığının karanlığı açarak görünmesini bildirir.","gloss":"gecenin sabah öncesi son vakti","neighbor_only":"Komşu dal ışığın belirmesini değil, gecenin sabah öncesindeki son zaman bölümünü bildirir.","neighbor_ref":"root_000682/B004","relation_type":"same_field","shared_zone":"İki dal gecenin sonu ile sabahın başlangıcı arasındaki zaman alanında buluşur."}],"source_phrase_ar":"الفجر انفجار الظلمة عن الصبح (maqayis)؛ الفجر ضوء الصباح والفجر الصبح (ayn)؛ الفجر حمرة الشمس في سواد الليل وهما فجران (jamhara)؛ الفجر في آخر الليل كالشفق في أوله (sihah)؛ الفجر ضوء الصبح وقد انفجر الصبح (tahdhib)؛ قيل للصبح فجر لكونه فجر الليل (mufradat)","source_summary":"Kaynaklar sabah ışığının gecenin sonundaki karanlığı açarak görünmesini ortak anlam olarak verir; iki tan görünümü de bu çekirdeğe bağlıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الفجر بمعنى ضوء الصبح وآخر الليل والصبح الصادق والكاذب","what_is_not_ar":"ليس تفجير الماء ولا الفجور ولا الجود"},"support_links":[]},{"boundary":"Dal her türlü sürprizi değil, insanların veya belaların çokluk halinde birilerinin üzerine gelmesini anlatır.","branch_kind":"collocation","branch_ref":"root_001132/B003","candidate_links":[{"candidate_id":"cand_2e321606e0614a7f1ce4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فُجُور","morph_features":"STEM|POS:N|LEM:fujuwr|ROOT:fjr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:2:1","qac_word_ref":"91:8:2","surface_ar":"فُجُورَ"}],"gloss":"kalabalığın ya da çok sayıda belanın ansızın üzerlerine gelmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çokluk halinde bulunan bir küme, etkilenen topluluğun üzerine beklenmedik biçimde gelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gelen küme kalabalık bir insan topluluğu ya da art arda gelen çok sayıda bela olabilir."}}],"root_ar":"ف ج ر","root_id":"root_001132","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirtilen üzerine gelme kuruluşunda hem insan kalabalığını hem de çok sayıdaki belayı kapsayan eksiksiz karşılıktır.","boundary_detail":"Dal her türlü sürprizi değil, insanların veya belaların çokluk halinde birilerinin üzerine gelmesini anlatır.","branch_image_ar":"اندفاع الكثير بغتة","concept_gloss":"kalabalığın ya da çok sayıda belanın ansızın üzerlerine gelmesi","contextual_glosses":[{"applicability":"Çok sayıda insanın bir topluluğa beklenmedik biçimde yöneldiği anlatılarda doğal bir cümle karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı kuruluşun çok sayıda bela için kullanılabilmesini dışarıda bırakır.","preserves":"Kalabalığın birilerinin üzerine ansızın ve topluca gelişini korur."},"facet_ids":["F001","F002"],"text":"kalabalık ansızın üzerlerine üşüştü","usage_role":"contextual"}],"definition":"Çok sayıda insanın ya da çok sayıda belanın bir topluluğun üzerine ansızın gelmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çokluk halinde bulunan bir küme, etkilenen topluluğun üzerine beklenmedik biçimde gelir."},{"facet_id":"F002","role":"specialization","statement":"Gelen küme kalabalık bir insan topluluğu ya da art arda gelen çok sayıda bela olabilir."}],"identity_rationale":"Kaynak ifadesi, çok sayıda insanın ya da belanın bir topluluğun üzerine ansızın gelmesini açıkça kurar. Miktar, beklenmedik geliş ve etkilenen topluluk birlikte korunması gereken anlam bileşenleridir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kalabalık ansızın üzerlerine geldi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"çok sayıda bela ansızın başlarına geldi"}],"lexicalization_note":"Tanım yalnız belirtilen üzerine gelme kuruluşuna bağlıdır; bu anlam tek başına genel bir gelme ya da patlama anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen üç ilişki genel sürpriz, ani varış ve bastırıcı toplu geliş arasındaki temel sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel sürpriz oluşu anlatır; odak dal ise sürprize ek olarak çokluğu ve insanların ya da belaların birilerinin üzerine yönelmesini gerektirir.","focus_only":"Odak dal çok sayıda insanı veya belayı ve bunların bir topluluğun üzerine gelişini şart koşar.","gloss":"beklenmedik anda karşısına çıkma","neighbor_only":"Komşu dal herhangi bir şeyin beklenmedik gelişini kapsar; çokluk ya da belirli bir etkilenen taraf gerektirmez.","neighbor_ref":"root_000135/B001","relation_type":"near_synonym","shared_zone":"İki dalda da önceden beklenmeyen, ansızın gerçekleşen bir karşılaşma veya geliş vardır."},{"boundary_match":"partial","distinction":"Komşu dalın öznesi ve sahnesi geniştir; odak dal ise çokluk halindeki insanların veya belaların bir topluluğun üzerine gelmesiyle sınırlıdır.","focus_only":"Odak dal, insan kalabalığına veya çok sayıdaki belaya ve bunlardan etkilenen topluluğa bağlıdır.","gloss":"bir şeyin ansızın ortaya çıkıp gelmesi","neighbor_only":"Komşu dal tek bir kişinin, uzaktan gelen selin ya da bir gök cisminin ansızın görünmesini de kapsar.","neighbor_ref":"root_000466/B004","relation_type":"near_synonym","shared_zone":"Her iki dal beklenmedik bir ortaya çıkış veya varış hareketi taşır."},{"boundary_match":"partial","distinction":"Odak dal beklenmedik varış anına odaklanır; komşu dal ise gelen şeyin topluluğu kaplaması, yayılması ve baskın etkisini öne çıkarır.","focus_only":"Odak dalda ansızın geliş ve çok sayıda insan ya da bela bulunması kurucu koşuldur.","gloss":"kalabalığın ya da ağır bir olayın bastırması","neighbor_only":"Komşu dal atların, insanların ya da ağır bir olayın bir topluluğu kaplayıp bastırmasını ve yayılmasını öne çıkarır.","neighbor_ref":"root_000496/B003","relation_type":"near_neighbor","shared_zone":"İki dal bir topluluğun dışarıdan gelen çokluk veya ağır bir olay karşısında baskı altında kalmasını anlatabilir."}],"source_phrase_ar":"انفجر عليهم القوم وانفجرت عليهم الدواهي إذا جاءهم الكثير منها بغتة (ayn)؛ انفجرت عليهم الدواهي إذا جاءهم الكثير منها بغته (tahdhib)","source_summary":"Kaynaklar, kalabalık bir insan topluluğunun veya çok sayıda belanın birilerinin üzerine beklenmedik biçimde gelmesinde birleşir; çokluk ve ansızın geliş birlikte zorunludur.","sources":["AY","TA"],"what_is_ar":"يدخل فيه مجيء القوم أو الدواهي الكثيرة بغتة على قوم","what_is_not_ar":"ليس انفجار الماء حقيقة ولا الفجور"},"support_links":["sup_b110be56511440060846"]},{"boundary":"Dalın çekirdeği ahlaki ve inançsal sınırları çiğnemektir; fiziksel eğrilik yalnız ilgili söz öbeğinin ayrı sözlüksel karşılığında kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_001132/B004","candidate_links":[{"candidate_id":"cand_daba8183049900fc31ab","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فُجُور","morph_features":"STEM|POS:N|LEM:fujuwr|ROOT:fjr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:2:1","qac_word_ref":"91:8:2","surface_ar":"فُجُورَ"}],"gloss":"doğruluk sınırını çiğneyerek kötülüğe sapma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi doğruluk ve inanç sınırlarını çiğneyerek doğru yoldan sapar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yalan söylemek, kötülüklere dalmak, başkaldırmak, inancı reddetmek ve cinsel sınırı çiğnemek bu sapmanın özel görünümleridir."}}],"root_ar":"ف ج ر","root_id":"root_001132","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalan ve başkaldırı gibi özel eylemlerin bağlı olduğu geniş ahlaki sapma çekirdeği kastedildiğinde kullanılır.","boundary_detail":"Dalın çekirdeği ahlaki ve inançsal sınırları çiğnemektir; fiziksel eğrilik yalnız ilgili söz öbeğinin ayrı sözlüksel karşılığında kalır.","branch_image_ar":"انحراف عن الحق وخرق الستر","concept_gloss":"doğruluk sınırını çiğneyerek kötülüğe sapma","contextual_glosses":[{"applicability":"Bir kişinin geniş ve belirgin ahlaki sapmasını doğal bir yüklemle anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalan, inancı reddetme, başkaldırı ve cinsel sınır çiğneme gibi özel görünümleri tek tek belirtmez.","preserves":"Doğruluktan ayrılma ve kötülüklere yönelme çekirdeğini korur."},"facet_ids":["F001"],"text":"doğru yoldan sapıp kötülüğe daldı","usage_role":"general"}],"definition":"Doğruluk ve inanç sınırlarını yarıp kötülüklere yönelmek, böylece doğru yoldan belirgin biçimde sapmaktır. Yalan, taşkın kötülük, başkaldırı, inancı reddetme ve cinsel sınır çiğneme bunun özel görünümleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi doğruluk ve inanç sınırlarını çiğneyerek doğru yoldan sapar."},{"facet_id":"F002","role":"specialization","statement":"Yalan söylemek, kötülüklere dalmak, başkaldırmak, inancı reddetmek ve cinsel sınırı çiğnemek bu sapmanın özel görünümleridir."}],"identity_rationale":"Kaynak ifadesi, doğruluktan sapıp kötülüklere açılmayı; yalanı, başkaldırıyı, inancı reddetmeyi ve cinsel sınır çiğnemeyi bunun görünümleri olarak destekler. Geçici çerçevedeki fiziksel yana yatma ise dalın kurucu ahlaki anlamı değil, ayrı bir söz öbeğinde görülen sınırlı bir uzantıdır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"taşkın kötülük, başkaldırı ve yalan"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"doğru yoldan sapıp kötülüklere daldı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yalan söyledi"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yalan söyledi, cinsel sınırı çiğnedi ya da inancı reddetti"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"doğru yoldan sapmış kimse"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"terkin oturma yeri yana yatıktır"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kötülük, kuşku ve yalan"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"ey doğru yoldan sapmış kadın"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"sana yalan söyleyen, karşı gelen ya da sözünden çıkan kişi"}],"lexicalization_note":"Tanım ahlaki sapma çekirdeğini verir; yalan, başkaldırı ve benzeri kullanımlar ile fiziksel eğiklik bildiren söz öbeği birbirine karıştırılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen ilişkiler genel suç, yalan, hükümde eğrilik ve başkasını saptırma ile olan temel kapsam ve katılımcı farklarını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal geniş ahlaki taşkınlığı ve belirli ağır görünümleri kapsar; komşu dal ise özellikle karar, yöneliş ve hükümdeki eğriliği öne çıkarır.","focus_only":"Odak dal kötülüklere dalmayı, yalanı, başkaldırıyı ve inancı reddetmeyi geniş bir sapma alanında toplar.","gloss":"hükümde ve amaçta doğruluktan eğilme","neighbor_only":"Komşu dal özellikle hüküm, niyet ve işte doğruluktan yana eğilmeyi veya haksızlığa yönelmeyi kapsar.","neighbor_ref":"root_000265/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak çekirdeği doğruluktan ayrılma ve yanlış yöne eğilmedir."},{"boundary_match":"partial","distinction":"Komşu dal işlenen yanlışı suç veya kusur olarak adlandırır; odak dal ise kişinin doğruluktan kopup kötülüğe yönelme durumunu ve bunun çeşitli görünümlerini öne çıkarır.","focus_only":"Odak dal yalanı, inançtan uzaklaşmayı ve kötülüklere açılmayı da kapsar.","gloss":"yanlış davranış ve suç işleme","neighbor_only":"Komşu dal yanlış fiili suç, saldırı veya sorumluluk doğuran edim yönüyle adlandırır.","neighbor_ref":"root_000239/B004","relation_type":"near_synonym","shared_zone":"İki dal da kişinin kınanan bir yanlış yapmasını ve doğru sınırı aşmasını anlatır."},{"boundary_match":"partial","distinction":"Komşu dal doğrudan yalan ve gerçek dışılığı adlandırır; odak dalda yalan daha geniş bir doğruluktan sapma ve kötülüğe açılma bütününün yalnız bir parçasıdır.","focus_only":"Odak dal yalanın yanı sıra başkaldırı, kötülük, inancı reddetme ve başka sınır çiğnemelerini kapsar.","gloss":"yalan ve gerçek dışı söz","neighbor_only":"Komşu dal yalan söz, yalancı tanıklık ve gerçek dışı sayılan şeylere özgüdür.","neighbor_ref":"root_000654/B002","relation_type":"near_neighbor","shared_zone":"Yalan söylemek odak daldaki geniş ahlaki sapmanın açıkça belirtilen bir görünümüdür."},{"boundary_match":"partial","distinction":"Odak dal sapan kişinin durumunu ve davranışını kurar; komşu dal ise katılımcı rolünü değiştirerek sapmaya yol açan kişi veya etkiyi kurucu hale getirir.","focus_only":"Odak dal kişinin kendisinin doğru yoldan sapmasını ve sınırları çiğnemesini anlatır.","gloss":"başkasını doğru yoldan uzaklaştırma","neighbor_only":"Komşu dal başka birini doğru yoldan uzaklaştıran, kandıran veya yanlış davranışı çekici gösteren etkene odaklanır.","neighbor_ref":"root_001128/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal doğru yoldan ayrılma ve yanlış yöne dönme senaryosuna bağlıdır."}],"source_phrase_ar":"الانبعاث والتفتح في المعاصي فجورا (maqayis)؛ سمي الكذب فجورا (maqayis)؛ كل مائل عن الحق فاجر (maqayis)؛ الفجور الريبة والكذب (ayn;tahdhib)؛ انبعاثه في المعاصي (jamhara)؛ فجر فجورا أي فسق وفجر أي كذب وأصله الميل (sihah)؛ الفجور شق ستر الديانة (mufradat)؛ سمي الكاذب فاجرا لكون الكذب بعض الفجور (mufradat)؛ أفجر إذا كذب وأفجر إذا عصى بفرجه وأفجر إذا كفر (tahdhib)","source_summary":"Kaynaklar doğruluktan sapma ve inanç sınırını çiğneme çekirdeğinde birleşir; yalan, kötülüklere dalma, başkaldırı, inancı reddetme ve cinsel yanlış bu geniş sapmanın belirtilen görünümleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الفجور والفسق والمعاصي والريبة والكذب والكفر والعصيان والميل عن الحق وما لحق به من ميل حسي","what_is_not_ar":"ليس الفجر الصباحي ولا تفجير الماء ولا الجود"},"support_links":["sup_18176688d1b7ccdf56c6"]},{"boundary":"Bu dal fiziksel su akışını ya da ahlaki sapmayı değil, iyilik ve vermedeki geniş bolluğu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001132/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فُجُور","morph_features":"STEM|POS:N|LEM:fujuwr|ROOT:fjr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:2:1","qac_word_ref":"91:8:2","surface_ar":"فُجُورَ"}],"gloss":"taşarcasına bol iyilik ve eli açıklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İyilik ve verme, taşarcasına geniş ve bol biçimde gerçekleşir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin yaptığı yardımın çokluğu ve çokça varlık getirmesi bu bolluğun özel görünümleridir."}}],"root_ar":"ف ج ر","root_id":"root_001132","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Geniş verme eğilimi ile iyiliğin bolluğunu aynı anda anlatmak için en kapsamlı doğal karşılıktır.","boundary_detail":"Bu dal fiziksel su akışını ya da ahlaki sapmayı değil, iyilik ve vermedeki geniş bolluğu anlatır.","branch_image_ar":"جود متفجر واسع","concept_gloss":"taşarcasına bol iyilik ve eli açıklık","contextual_glosses":[{"applicability":"Bir kişinin sürekli ve bol yardımını doğal bir kişi betimlemesi içinde anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çokça varlık getirme kullanımını ve iyiliğin taşarak yayılması imgesini açıkça belirtmez.","preserves":"Eli açıklığı ve kişiden gelen iyiliğin bolluğunu doğal biçimde korur."},"facet_ids":["F001"],"text":"eli açık, yaptığı iyilik de boldur","usage_role":"general"}],"definition":"İyiliğin taşarcasına bol olması ve kişinin geniş bir eli açıklıkla vermesidir. Yapılan yardımın çokluğu ve kişinin çokça varlık getirmesi bu bolluğun belirtilen görünümleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İyilik ve verme, taşarcasına geniş ve bol biçimde gerçekleşir."},{"facet_id":"F002","role":"specialization","statement":"Kişinin yaptığı yardımın çokluğu ve çokça varlık getirmesi bu bolluğun özel görünümleridir."}],"identity_rationale":"Kaynak ifadesi eli açıklığı, geniş ve taşarcasına bol iyiliği, yapılan yardımı ve çokça varlık getirmeyi aynı bolluk çekirdeği çevresinde toplar. Geçici dal çerçevesi bu olumlu taşma ve verme yönünü doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bol iyilik ve eli açıklık"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"iyiliği ve yardımı"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"iyiliği taşarcasına bol kimse"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"iyiliğin taşıp yayılması"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"çokça varlık getirdi"}],"lexicalization_note":"Tanım eli açıklık çekirdeğini verir; kişinin iyiliğinin bolluğu ve çokça varlık getirmesi yalnız belirtilen yapılara bağlı özelleşmelerdir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan ilişkiler genel eli açıklık, karşılıksız verme, sırf çokluk ve esirgeme karşıtlığıyla olan sınırları kapsar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal verme eyleminin nesnelerini daha açık ve genel biçimde kapsar; odak dal ise iyiliğin içeriden taşarcasına bol oluşu imgesini ve belirli bolluk kullanımlarını öne çıkarır.","focus_only":"Odak dal iyiliğin taşarcasına yayılmasını, yapılan yardımın çokluğunu ve çokça varlık getirmeyi içerir.","gloss":"eli açıklık ve çokça verme","neighbor_only":"Komşu dal para ya da bilgi vermeyi ve kişiyi veren kimse olarak nitelemeyi açıkça kapsar.","neighbor_ref":"root_000274/B001","relation_type":"near_synonym","shared_zone":"İki dal da eli açıklığı, yardım etmeyi ve çokça vermeyi olumlu bir özellik olarak anlatır."},{"boundary_match":"partial","distinction":"Odak dal taşma ve geniş iyilik imgesine dayanır; komşu dal ise vermenin serbest ve karşılıksız oluşunu, bazı kullanımlarda sözü de içine alacak biçimde öne çıkarır.","focus_only":"Odak dal yapılan iyiliğin ve yardımın taşarcasına bolluğunu, ayrıca çokça varlık getirmeyi kapsar.","gloss":"karşılıksız ve bol verme","neighbor_only":"Komşu dal karşılıksız ve kısıtsız genel vermeyi, hatta engellenmeden söylenen sözü de kapsar.","neighbor_ref":"root_000677/B003","relation_type":"near_synonym","shared_zone":"İki dalda da iyiliğin ve vermenin bol, açık ve kısıtlanmamış oluşu bulunur."},{"boundary_match":"opposed","distinction":"Odak dal aynı eksenin bolca verme ucunu, komşu dal ise vermeme ve esirgeme ucunu kurar; bu nedenle yönleri doğrudan karşıttır.","focus_only":"Odak dal iyiliği bolca verme, yardım etme ve eli açık olma yönündedir.","gloss":"vermeyi kesme ve iyiliği esirgeme","neighbor_only":"Komşu dal vermeyi durdurma, iyiliği esirgeme ve eli sıkı davranma yönündedir.","neighbor_ref":"root_001448/B001","relation_type":"antonym","shared_zone":"İki dal kişinin elindeki iyiliği veya varlığı başkasına verip vermemesi ekseninde karşılaşır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği taşarcasına iyilik ve eli açıklıktır; komşu dalın çekirdeği daha genel çokluk olup bol verme bunun yalnız bir uygulamasıdır.","focus_only":"Odak dal bolluğu özellikle iyilik, yardım ve eli açıklıkla sınırlar.","gloss":"çokluk ve bol verme","neighbor_only":"Komşu dal yükün veya herhangi bir şeyin çokluğunu da kapsar ve yalnız bol verme anlamına bağlı değildir.","neighbor_ref":"root_001624/B003","relation_type":"near_synonym","shared_zone":"Bol ve çokça verme bağlamında iki dal güçlü biçimde örtüşür."}],"source_phrase_ar":"الفجر وهو الكرم والتفجر بالخير (maqayis)؛ وما أكثر فجره أي معروفه (ayn)؛ رجل ذو فجر إذا كان يتفجر بالخير (jamhara)؛ الفجر الكرم والتفجر في الخير (sihah)؛ الفجر الجود الواسع والكرم (tahdhib)؛ أفجر الرجل إذا جاء بالفجر وهو المال الكثير (tahdhib)","source_summary":"Kaynaklar geniş eli açıklık, taşarcasına bol iyilik ve yapılan yardımın çokluğu üzerinde birleşir; çokça varlık getirme de bu bolluğun özel bir eylem görünümüdür.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الكرم والجود الواسع والمعروف والمال الكثير والتفجر بالخير","what_is_not_ar":"ليس الفجور ولا الفجر الصباحي ولا تفجير الماء"},"support_links":[]},{"boundary":"Dal, dokunulmazlığın çiğnendiği belirli savaş günlerinin yerleşik adlandırmasıyla sınırlıdır.","branch_kind":"non_bare","branch_ref":"root_001132/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فُجُور","morph_features":"STEM|POS:N|LEM:fujuwr|ROOT:fjr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:2:1","qac_word_ref":"91:8:2","surface_ar":"فُجُورَ"}],"gloss":"dokunulmazlığın çiğnenmesiyle adlandırılan belirli savaş günleri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli savaş olayları, birlikte anılan yerleşik bir tarihsel günler kümesini oluşturur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu savaşların ortak adı, dokunulmaz sayılan aylarda ve yerde sınırların çiğnenmesine dayanır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yerleşik adlandırma, birbiriyle bağlantılı dört ayrı çatışma olayını kapsar."}}],"root_ar":"ف ج ر","root_id":"root_001132","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız bu yerleşik tarihsel savaş günleri kümesini, adlandırılma gerekçesiyle birlikte belirtmek için kullanılır.","boundary_detail":"Dal, dokunulmazlığın çiğnendiği belirli savaş günlerinin yerleşik adlandırmasıyla sınırlıdır.","branch_image_ar":"وقائع الفجار لانتهاك الحرمة","concept_gloss":"dokunulmazlığın çiğnenmesiyle adlandırılan belirli savaş günleri","contextual_glosses":[{"applicability":"Yerleşik savaş adı okura açıklanırken, olayların ayırt edici gerekçesini kısa biçimde vermek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bunların dört bağlantılı olaydan oluşan yerleşik ve sınırlı bir adlandırma olduğunu açıkça söylemez.","preserves":"Savaş günleri ile dokunulmazlığın çiğnenmesi arasındaki bağı korur."},"facet_ids":["F001","F002"],"text":"dokunulmazlığın çiğnendiği savaş günleri","usage_role":"explanatory"}],"definition":"Dokunulmaz sayılan aylarda ve yerde sınırların çiğnenmesi nedeniyle ortak bir adla anılan belirli savaş günleridir. Bunlar birbiriyle bağlantılı dört ayrı çatışma olayı olarak aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli savaş olayları, birlikte anılan yerleşik bir tarihsel günler kümesini oluşturur."},{"facet_id":"F002","role":"core","statement":"Bu savaşların ortak adı, dokunulmaz sayılan aylarda ve yerde sınırların çiğnenmesine dayanır."},{"facet_id":"F003","role":"specialization","statement":"Yerleşik adlandırma, birbiriyle bağlantılı dört ayrı çatışma olayını kapsar."}],"identity_rationale":"Kaynak ifadesi, belirli eski savaş olaylarını ve bunların dokunulmaz sayılan zaman ve sınırların çiğnenmesi nedeniyle ortak bir adla anılmasını açıkça destekler. Bu nedenle anlam ne her savaşa ne de her türlü sınır çiğnemeye genellenebilir.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"dokunulmazlığın çiğnendiği belirli savaş günleri"}],"lexicalization_note":"Tanım yalnız belirli savaş günlerini bildiren yerleşik birime bağlıdır; yalın biçime genel savaş ya da kötülük anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen ilişkiler şiddetli savaş, yinelenen savaş, adlandırılmış başka bir savaş günü ve yanlış davranışla olan sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal yerleşik bir tarihsel olaylar kümesinin adıdır ve ayırt edici ölçütü dokunulmazlık ihlalidir; komşu dal ise savaşın şiddet derecesini niteler.","focus_only":"Odak dal dokunulmazlığın çiğnenmesiyle adlandırılan belirli ve sınırlı savaş olaylarını bildirir.","gloss":"çok şiddetli ve öldürücü savaş","neighbor_only":"Komşu dal, daha önceki bir çatışmaya bağlı olmaksızın çok şiddetli ve öldürücü herhangi bir savaşı anlatır.","neighbor_ref":"root_001037/B005","relation_type":"same_field","shared_zone":"İki dal savaş, çatışma ve yoğun şiddet alanında buluşur."},{"boundary_match":"field_only","distinction":"Odak dal dört belirli olayı ortak ad ve ihlal gerekçesiyle birleştirir; komşu dal ise herhangi bir savaşın ilk olmayıp yinelenmiş olmasını anlatır.","focus_only":"Odak dalın kimliği belirli olaylara ve dokunulmazlığın çiğnenmesine bağlıdır.","gloss":"daha önce de yapılmış yinelenen savaş","neighbor_only":"Komşu dal daha önce de savaşılmış olmasını, yani çatışmanın yinelenmesini kurucu özellik yapar.","neighbor_ref":"root_001064/B003","relation_type":"same_field","shared_zone":"Her iki dal birden fazla çatışmayla ilişkilendirilebilen savaş anlatılarıdır."},{"boundary_match":"thematic_only","distinction":"Aralarında kurucu anlam ortaklığı yoktur; odak dal ihlal gerekçesiyle birleşen olaylar kümesini, komşu dal ise başka bir yer ve ona bağlı günü bildirir.","focus_only":"Odak dal dokunulmazlığın çiğnendiği dört bağlantılı savaş olayının yerleşik adıdır.","gloss":"belirli bir yer ve ona bağlı savaş günü","neighbor_only":"Komşu dal belirli bir yer adını ve o yere bağlı tek bir savaş gününü adlandırır.","neighbor_ref":"root_000040/B009","relation_type":"thematic","shared_zone":"İki dal eski toplulukların belirli ve adlandırılmış savaş günleri senaryosunda buluşur."},{"boundary_match":"thematic_only","distinction":"Komşu dal yanlış davranışın kendisini adlandırır; odak dal ise bu yanlışın gerçekleştiği belirli savaş günlerinin yerleşik adıdır.","focus_only":"Odak dal belirli savaş olaylarını ve bunların ortak tarihsel adını bildirir.","gloss":"yanlış davranış ve suçluluk","neighbor_only":"Komşu dal doğrudan yanlış davranış, suçluluk ve kişinin sakındığı kötülüğü bildirir.","neighbor_ref":"root_000365/B001","relation_type":"thematic","shared_zone":"Dokunulmazlığın çiğnenmesi, odak daldaki savaşların adlandırılma gerekçesi olarak yanlış davranış alanına bağlanır."}],"source_phrase_ar":"يوم الفجار يوم للعرب استحلت فيه الحرمة (maqayis)؛ انفجار من وقعات العرب بعكاظ (ayn)؛ أيام الفجار أربعة أفجرة (jamhara;sihah)؛ وإنما سمت قريش هذه الحرب فجارا لأنها كانت في الأشهر الحرم (sihah)؛ أيام الفجار أيام وقائع كانت بعكاظ واستحلوا الحرمات (tahdhib)؛ أيام الفجار وقائع اشتدت بين العرب (mufradat)","source_summary":"Kaynaklar, belirli savaş günlerinin dokunulmaz sayılan aylarda ve yerde sınırların çiğnenmesi nedeniyle adlandırıldığını ve dört bağlantılı olay olarak anıldığını birlikte bildirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه اسم أيام الفجار ووقائعها بين العرب وتسميتها بما وقع فيها من استحلال الحرمات","what_is_not_ar":"ليس كل فجور ولا كل حرب"},"support_links":[]},{"boundary":"Dal, içe doğan düşünceyi değil, gerçek anlamda yutma, yeme veya emerek tüketme eylemini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001381/B001","candidate_links":[{"candidate_id":"cand_daba8183049900fc31ab","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَلْهَمَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>alohama|ROOT:lhm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:8:1:2","qac_word_ref":"91:8:1","surface_ar":"أَلْهَمَ"}],"gloss":"bir şeyi bütünüyle yutup tüketme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi bir kerede yutarak içine alma ve bütünüyle tüketme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yeme bağlamında şiddetle ve geride bir şey bırakmadan yeme."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yavrunun annesinin memesindeki sütü emerek tümüyle bitirmesi."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kişinin çok ve oburca yiyen biri olarak nitelenmesi."}}],"root_ar":"ل ه م","root_id":"root_001381","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın tek seferde yutma ve geride bırakmadan tüketme biçimindeki ortak çekirdeğini karşılar.","boundary_detail":"Dal, içe doğan düşünceyi değil, gerçek anlamda yutma, yeme veya emerek tüketme eylemini kapsar.","branch_image_ar":"ابتلاع الشيء واستيفاؤه","concept_gloss":"bir şeyi bütünüyle yutup tüketme","contextual_glosses":[{"applicability":"Bir nesnenin tek seferde yutularak içeri alınmasını anlatan somut bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tek seferde yutarak içeri alma özelliğini korur."},"facet_ids":["F001"],"text":"bir lokmada yutmak","usage_role":"contextual"},{"applicability":"Yiyeceğin şiddetle ve geride hiçbir şey bırakmadan yenmesi bağlamında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yeme eyleminin yoğunluğunu ve yiyeceği bitirmeyi korur."},"facet_ids":["F002"],"text":"silip süpürmek","usage_role":"contextual"},{"applicability":"Yavrunun annesinin memesindeki sütü tümüyle tükettiği özel kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Emme yoluyla memedeki sütün tümünü bitirmeyi korur."},"facet_ids":["F003"],"text":"memedeki sütü sonuna kadar emmek","usage_role":"explanatory"},{"applicability":"Bir kişinin çok yiyen biri olarak nitelendiği kullanımda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye yüklenen çok ve aşırı yeme niteliğini korur."},"facet_ids":["F004"],"text":"oburca yiyen","usage_role":"contextual"}],"definition":"Bir şeyi bir kerede yutarak içine almak ve geride bırakmadan tüketmektir. Yiyeceği şiddetle yeme, yavrunun memedeki sütü bitirmesi ve çok yiyen kişinin nitelenmesi bu çekirdeğe bağlı özelleşmelerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi bir kerede yutarak içine alma ve bütünüyle tüketme."},{"facet_id":"F002","role":"specialization","statement":"Yeme bağlamında şiddetle ve geride bir şey bırakmadan yeme."},{"facet_id":"F003","role":"example","statement":"Yavrunun annesinin memesindeki sütü emerek tümüyle bitirmesi."},{"facet_id":"F004","role":"specialization","statement":"Bir kişinin çok ve oburca yiyen biri olarak nitelenmesi."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek seferde yutma ve hiçbir şey bırakmadan bitirme özelliklerini kaybeder.","preserves":"Yiyecek tüketme alanındaki genel eylemi korur."},"text":"yemek"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tüketilen şeyi tümüyle bitirme ve şiddetli yeme uzantılarını kaybeder.","preserves":"Bir şeyi ağızdan içeri alma eylemini korur."},"text":"yutmak"}],"identity_rationale":"Kaynak ifadesi, bir şeyi bir kerede yutup içine alma çekirdeğini; şiddetle yeme, memedekini tümüyle emme ve çok yiyen kişi kullanımlarıyla birlikte açıkça destekler. Verilen dal çerçevesi bu somut tüketme ve geride bir şey bırakmama ortaklığını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi bir kerede yutmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi yutup tümüyle tüketmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yavrunun memedeki sütü sonuna kadar emmesi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"çok yiyen, obur"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çok yiyen adam"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir şeyi yutma"}],"lexicalization_note":"Tanım, biçimlerin taşıdığı yutma çekirdeğiyle kalıp kullanımlardaki sütü tüketme ve çok yeme özelleşmelerini birbirine karıştırmadan birlikte gösterir.","neighbor_coverage_note":"Bütün adaylar değerlendirilmiş; yutma, lokma alma ve genel yeme sınırını en açık gösteren dört komşu seçilmiştir. İç dallar ile içkiyi geçirme ve doluluk adayları, bu ayrımları keskinleştirmediği için yayımlanmamıştır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeği yutarak içine alma ve tüketmeyi tamamlamadır; komşu dal ise yiyenin hiçbir şey bırakmayan iştahını ve yıkıcı yeme biçimini öne çıkarır.","focus_only":"Tek seferde yutma ve yavrunun memedeki sütü tüketmesi bu dala özgüdür.","gloss":"geride bırakmadan yeme","neighbor_only":"Her şeyi yiyen kişi veya bitkileri kırıp yiyen hayvan nitelemesi komşuda belirgindir.","neighbor_ref":"root_000236/B003","relation_type":"near_synonym","shared_zone":"İki dal da güçlü yeme eylemini ve tüketilen şeyden geriye bir şey bırakmamayı anlatır."},{"boundary_match":"partial","distinction":"Bu dal tamamıyla tüketme sonucuna odaklanırken komşu dal yutulan şeyin geçiş sırasında kaybolmasına ve yutma kolaylığına odaklanır.","focus_only":"Tüketilen şeyi bitirme ve sütü tümüyle emme sonucu bu dalda bulunur.","gloss":"yutup gözden kaybetme","neighbor_only":"Yutulanın geçişte kaybolması, kolay yutma ve boğaz genişliği komşuya özgüdür.","neighbor_ref":"root_000858/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin yutularak ağızdan içeri geçirilmesini anlatır."},{"boundary_match":"partial","distinction":"Komşu dal lokmanın alınışını ve verilmesini düzenler; bu dal ise alınan şeyin yutularak bütünüyle tüketilmesini öne çıkarır.","focus_only":"Bir şeyi bütünüyle tüketme ve şiddetle yeme anlamı bu dalda belirgindir.","gloss":"lokma alıp yeme","neighbor_only":"Lokma alma, başkasına lokma verme ve lokma sayısının çokluğu komşuya özgüdür.","neighbor_ref":"root_001371/B002","relation_type":"near_neighbor","shared_zone":"İki dal da yiyeceğin ağız yoluyla alınması ve yutulması alanında buluşur."},{"boundary_match":"partial","distinction":"Komşu dal yemenin genel adıdır; bu dal genel yeme eylemini değil, yutma ve tüketmeyi sonuna kadar götürme biçimini belirtir.","focus_only":"Tek seferde yutma ve hiçbir şey bırakmadan tüketme sınırı bu dala özgüdür.","gloss":"genel olarak yeme","neighbor_only":"Yiyecek, öğün, yedirme ve birlikte yeme gibi genel alanlar komşuda yer alır.","neighbor_ref":"root_000043/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da yiyecek tüketme eylemini kapsayan ortak bir alana girer."}],"source_phrase_ar":"أصل صحيح يدل على ابتلاع شيء (maqayis)؛ لهمت الشيء وقلما يقال إلا التهمت وهو ابتلاعه بمرة (ayn;tahdhib)؛ اللهم الابتلاع وقد لهمه بالكسر إذا ابتلعه (sihah)؛ التهم الفصيل ما في ضرع أمه استوفاه (maqayis;sihah;mufradat)؛ الملهم الكثير الأكل ورجل لهوم أكول (tahdhib)","source_summary":"Kaynakların ortak çizgisi, tek seferde yutma ile bir şeyi tümüyle tüketmeyi birleştirir. Bu çizgi, şiddetli yemeyi, yavrunun memedeki sütü bitirmesini ve çok yiyen kişi nitelemesini de kapsar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه لهم الشيء والتهمه، والأكل الشديد، واستيفاء الفصيل ما في الضرع.","what_is_not_ar":"لا يدخل فيه الإلهام إلا من جهة القياس على شيء يلقى في الروع فيتلقاه الباطن."},"support_links":["sup_18176688d1b7ccdf56c6"]},{"boundary":"Çekirdek, açık öğretimden çok iç dünyada beliren yönlendirmedir; Tanrı kaynaklı iyilik ve doğru yol bunun belirgin bir özelleşmesidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001381/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَلْهَمَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>alohama|ROOT:lhm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:8:1:2","qac_word_ref":"91:8:1","surface_ar":"أَلْهَمَ"}],"gloss":"içe doğan yönlendirme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir düşünce veya yönlendirmenin kişinin iç dünyasına bırakılması ve orada belirmesi."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İçsel yönlendirmenin özellikle Tanrı'dan geldiğini kabul eden kaynak sınırı."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanrı'nın kişiye iyiliği veya doğru yolu içten bildirmesi."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Tanrı'dan sabır veya doğru yol hakkında içsel bir yönlendirme dilemeyi anlatan kullanım."}}],"root_ar":"ل ه م","root_id":"root_001381","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dışarıdan açıklanmış bir öğretim olmadan iç dünyada beliren düşünce veya yönlendirme çekirdeğini karşılar.","boundary_detail":"Çekirdek, açık öğretimden çok iç dünyada beliren yönlendirmedir; Tanrı kaynaklı iyilik ve doğru yol bunun belirgin bir özelleşmesidir.","branch_image_ar":"إلقاء في الروع وتلقين الباطن","concept_gloss":"içe doğan yönlendirme","contextual_glosses":[{"applicability":"Bir düşüncenin açık bir öğretim olmadan kişinin iç dünyasında belirmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Düşüncenin içeriden ve kendiliğinden belirir görünmesini korur."},"facet_ids":["F001"],"text":"içine doğmak","usage_role":"general"},{"applicability":"Tanrı'nın bir kişiye iyiliği iç dünyasında bildirdiği kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tanrı kaynaklı iyilik yönlendirmesinin içsel oluşunu korur."},"facet_ids":["F002","F003"],"text":"iyiliği içine doğurmak","usage_role":"contextual"},{"applicability":"Tanrı'dan doğru yol hakkında içsel yönlendirme istemeyi anlatan kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İçsel yönlendirmenin Tanrı'dan dilenmesi özelliğini korur."},"facet_ids":["F004"],"text":"doğru yolu içine doğurmasını dilemek","usage_role":"explanatory"}],"definition":"Bir düşünce veya yönlendirmenin dıştan açıklanan öğretim yoluyla değil, kişinin iç dünyasında belirmesi ya da oraya bırakılmasıdır. Bazı kullanımlarda bu, Tanrı'nın iyiliği veya doğru yolu içten bildirmesiyle sınırlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir düşünce veya yönlendirmenin kişinin iç dünyasına bırakılması ve orada belirmesi."},{"facet_id":"F002","role":"source_variant","statement":"İçsel yönlendirmenin özellikle Tanrı'dan geldiğini kabul eden kaynak sınırı."},{"facet_id":"F003","role":"specialization","statement":"Tanrı'nın kişiye iyiliği veya doğru yolu içten bildirmesi."},{"facet_id":"F004","role":"associated_use","statement":"Tanrı'dan sabır veya doğru yol hakkında içsel bir yönlendirme dilemeyi anlatan kullanım."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Güncel kullanımda yaratıcı üretimi harekete geçiren esin çağrışımını ekleyebilir.","collision":"Sanatsal yaratıcılık ve fikir bulma anlamlarıyla kolayca karışır.","fit":"drifted_loanword","loses":"İç dünyaya bırakılan yönlendirmenin kabul edilmesi ve tanrısal sınır ihtimalini belirsizleştirir.","preserves":"Düşüncenin insanın içinde belirmesi yönünü korur."},"text":"ilham"},{"category":"alternative","error_profile":{"adds":null,"collision":"Sanatsal ve düşünsel üretim bağlamındaki yaygın anlamla çakışabilir.","fit":"narrowing","loses":"İyilik veya doğru yol hakkında yönlendirme ve Tanrı kaynaklı olma özelleşmesini kaybeder.","preserves":"Bir düşüncenin içeriden belirmesi yönünü korur."},"text":"esin"}],"identity_rationale":"Kaynak ifadesi ortak olarak bir düşünce veya yönlendirmenin iç dünyaya bırakılmasını anlatır; bazı parçalar bunu genel söylerken bir parça özellikle Tanrı kaynaklı oluşla sınırlar. Bu nedenle dal korunabilir, fakat yalnızca iyilik veya doğru yol hakkındaki tanrısal telkine indirgenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"içe doğuş, içten gelen yönlendirme"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"Tanrı'nın ona iyiliği içten bildirmesi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"Tanrı'dan sabrı içine doğurmasını dilemek"}],"lexicalization_note":"Tanım, ad biçiminin genel içsel yönlendirme alanını, Tanrı'nın iyiliği içten bildirmesi ve böyle bir yönlendirme dileme kullanımlarından ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirilmiş; somut içe alma benzetmesini, yönelişi ve doğru yolu bulma eksenini açıklayan dört aday seçilmiştir. Toplanma, geri dönme, yükselme ve dışsal dönme adayları yalnızca uzak senaryo ortaklığı taşıdığı için yayımlanmamıştır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal içsel ve zihinsel bir kabulü anlatır; komşu dal ise gerçek bir nesnenin ağız yoluyla yutulup tüketilmesini anlatır.","focus_only":"Soyut bir düşüncenin veya yönlendirmenin iç dünyada belirmesi bu dala özgüdür.","gloss":"içten gelen yönlendirme","neighbor_only":"Somut bir nesneyi yutmak ve geride bırakmadan tüketmek komşu dala özgüdür.","neighbor_ref":"root_001381/B001","relation_type":"near_neighbor","shared_zone":"İki dal, dışarıdan gelen bir şeyin içeride alınması tasarımında buluşur."},{"boundary_match":"partial","distinction":"Komşu dal kişinin mevcut eğilimini veya yön değiştirmesini anlatır; bu dal ise yönlendirici düşüncenin kişinin içine doğmasını anlatır.","focus_only":"Bir düşüncenin iç dünyaya bırakılması ve orada belirmesi bu dala özgüdür.","gloss":"bir yöne eğilme","neighbor_only":"Bir yöne, kişiye veya görüşe eğilme ve ona uyma komşu dala özgüdür.","neighbor_ref":"root_000263/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin içsel yönelişini ve bir doğrultuya çekilmesini ilgilendirir."},{"boundary_match":"opposed","distinction":"Bu dal kişiye içeriden bir yön verilmesini anlatırken komşu dal iç görüşün kaybını ve doğruya ulaşamamayı anlatır.","focus_only":"İç dünyada beliren ve kişiye yön gösteren bir düşünce bu dalın ayırt edici yanıdır.","gloss":"içsel yönlendirme ve yönsüzlük","neighbor_only":"Doğruyu görmeme, bilgisizlik ve yolun karışması komşu dalın ayırt edici yanıdır.","neighbor_ref":"root_001049/B002","relation_type":"polarity_pair","shared_zone":"İki dal, kişinin doğruyu bulmasını sağlayan ya da engelleyen içsel kavrayış alanında karşı karşıya gelir."},{"boundary_match":"opposed","distinction":"Bu dal özellikle içten gelen yönlendirmeyi anlatır; komşu dal ise bu yönlendirmenin yokluğunu değil, doğru yoldan fiilen sapmayı anlatır.","focus_only":"İyilik veya doğru yol yönünde içsel bir bildirim alma bu dalda bulunur.","gloss":"doğruya yönelme ve sapma","neighbor_only":"Doğru yoldan sapma ve yanlışta kaybolma komşu dalda bulunur.","neighbor_ref":"root_000913/B001","relation_type":"polarity_pair","shared_zone":"İki dal da doğru yol ekseninde yön bulma veya yönü kaybetme durumuyla ilgilidir."}],"source_phrase_ar":"الإلهام كأنه شيء ألقى في الروع فالتهمه (maqayis)؛ الإلهام ما يلقى في الروع يقال ألهمه الله (sihah)؛ ألهمه الله خيرا أي لقنه خيرا ونستلهم الله الرشاد (tahdhib)؛ الإلهام إلقاء الشيء في الروع ويختص بما كان من جهة الله تعالى (mufradat)","source_summary":"Ortak anlam, bir düşünce veya yönlendirmenin insanın iç dünyasına bırakılmasıdır. Kaynak anlatımı bunun Tanrı'dan gelen iyilik ve doğru yol telkini olarak kullanımını verir; bir yorum bu kaynak sınırını kavramın ayırt edici şartı sayar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الإلهام وما يلقى في الروع، والتلقين الإلهي للخير أو الرشاد.","what_is_not_ar":"لا يدخل فيه مطلق الكلام أو التعليم الظاهر بلا معنى الإلقاء في الروع."},"support_links":[]},{"boundary":"Dal yalnızca belirtilen at ve deve nitelemelerine bağlıdır; genel bir hız veya hareket anlamı çıkarılamaz.","branch_kind":"collocation","branch_ref":"root_001381/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَلْهَمَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>alohama|ROOT:lhm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:8:1:2","qac_word_ref":"91:8:1","surface_ar":"أَلْهَمَ"}],"gloss":"öne geçecek kadar hızlı veya çok yürüyen","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir atın yarışta öne geçecek kadar hızlı koşması."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atın koşusunun yeri yutarcasına ilerleme imgesiyle anlatılması."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Develerin hız zorunluluğu olmadan çok yürüyen hayvanlar olarak nitelenmesi."}}],"root_ar":"ل ه م","root_id":"root_001381","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca verilen at nitelemelerinde yarış hızını, deve nitelemesinde ise çok yürümeyi karşılayan toplu açıklamadır.","boundary_detail":"Dal yalnızca belirtilen at ve deve nitelemelerine bağlıdır; genel bir hız veya hareket anlamı çıkarılamaz.","branch_image_ar":"عدو يلتهم الأرض","concept_gloss":"öne geçecek kadar hızlı veya çok yürüyen","contextual_glosses":[{"applicability":"Yarışta öne geçen atın hızlı koşusunu canlı bir benzetmeyle anlatan bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Atın hızını ve yeri yutma benzetmesini birlikte korur."},"facet_ids":["F001","F002"],"text":"yeri yutarcasına koşan","usage_role":"contextual"},{"applicability":"Atın diğer atların önünde koştuğunu bildiren daha düz anlatımlı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Atın yarışta diğer atların önüne geçmesini korur."},"facet_ids":["F001"],"text":"yarışta öne geçen","usage_role":"contextual"},{"applicability":"Develerin çok yürüme özelliğiyle nitelendiği, hızın belirtilmediği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Develere yüklenen çok yürüme özelliğini korur."},"facet_ids":["F003"],"text":"çok yürüyen","usage_role":"contextual"}],"definition":"Atı niteleyen kullanımlarda yarışta öne geçecek kadar hızlı koşmayı ve yeri yutarcasına ilerlemeyi anlatır. Deve nitelemesinde ise hız şartı koymadan çok yürümeyi belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir atın yarışta öne geçecek kadar hızlı koşması."},{"facet_id":"F002","role":"associated_use","statement":"Atın koşusunun yeri yutarcasına ilerleme imgesiyle anlatılması."},{"facet_id":"F003","role":"source_variant","statement":"Develerin hız zorunluluğu olmadan çok yürüyen hayvanlar olarak nitelenmesi."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yarışta öne geçme, yeri yutma benzetmesi ve devenin çok yürümesi özelliklerini kaybeder.","preserves":"Yarış atının süratli oluşunu korur."},"text":"hızlı"}],"identity_rationale":"Kaynak ifadesi yarışta öne geçen atı yeri yutarcasına koşma imgesiyle, develeri ise çok yürüme özelliğiyle niteler. Verilen hareket çerçevesi kullanılabilir; ancak kaynak, bu nitelemeyi her türlü harekete genelleştirmeyi değil, yalnızca belirtilen at ve deve kullanımlarını destekler.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yeri yutarcasına koşan yarış atı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yarışta önden koşan at"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"çok yürüyen develer"}],"lexicalization_note":"Tanım, anlamı at ve deve için verilen niteleme kalıplarına bağlar; bunlardan bağımsız genel bir hareket ya da hız anlamı kurmaz.","neighbor_coverage_note":"Bütün hız ve yürüyüş adayları değerlendirilmiş; at yarışı, genel koşu hızı, deve yürüyüşü ve somut yutma benzetmesini ayıran dört aday seçilmiştir. Diğer hız adayları aynı ayrımları yinelediği için yayımlanmamıştır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli at nitelemelerinde yeri yutarcasına koşmayı ve ayrıca çok yürüyen develeri kapsar; komşu dal atın genel niteliği ile koşu hızını birlikte ele alır.","focus_only":"Yeri yutma benzetmesi ve develerin çok yürümesi bu dala özgüdür.","gloss":"hızlı yarış atı","neighbor_only":"Atın genel olarak iyi ve nitelikli oluşu komşu dalda ayrıca yer alır.","neighbor_ref":"root_000274/B004","relation_type":"near_synonym","shared_zone":"İki dal da yarış atının hızlı koşmasını ve öne çıkmasını anlatır."},{"boundary_match":"partial","distinction":"Komşu dal koşu hızını doğrudan bildirir; bu dal hızı yarışta öne geçme ve yeri yutma imgesiyle sınırlar, ayrıca çok yürüyen develere uzanır.","focus_only":"Yarışta öne geçme imgesi ve deve nitelemesi bu dala özgüdür.","gloss":"koşuda hızlı olma","neighbor_only":"Koşudaki hızın doğrudan adlandırılması komşu dalın merkezidir.","neighbor_ref":"root_001079/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da atın koşudaki süratini niteleyen kullanımlara sahiptir."},{"boundary_match":"partial","distinction":"Bu dal develer için çok yürümeyi söyler ve hız şartı koymaz; komşu dal ise deve yürüyüşünün hızlı oluşunu doğrudan belirtir.","focus_only":"Atın yarışta öne geçmesi ve develerde yürüyüşün çokluğu bu dala özgüdür.","gloss":"develerin hızlı ilerlemesi","neighbor_only":"Deve yürüyüşünün belirli biçimde hızlı olması komşu dalın merkezidir.","neighbor_ref":"root_001521/B003","relation_type":"near_synonym","shared_zone":"İki dal da develerin belirgin yürüyüş ve ilerleyiş özelliğini anlatır."},{"boundary_match":"partial","distinction":"Bu dal yalnızca hayvan nitelemelerinde hareketi anlatır; komşu dal gerçek yutma ve tüketme eylemini anlatır.","focus_only":"Hareketin yeri yutarcasına ilerleme benzetmesiyle anlatılması bu dala özgüdür.","gloss":"yeri yutarcasına ilerleme","neighbor_only":"Gerçek bir nesneyi yutarak tümüyle tüketme komşu dala özgüdür.","neighbor_ref":"root_001381/B001","relation_type":"near_neighbor","shared_zone":"Hızlı ilerleme, somut yutma eyleminin tüketici görünümünden alınan bir benzetmeyle anlatılır."}],"source_phrase_ar":"فرس لهم سباق كأنه يلتهم الأرض (maqayis;sihah;mufradat)؛ فرس لهم ولهميم سابق يجري أمام الخيل لالتهامه الأرض (tahdhib)؛ إبل لهاميم إذا كانت كثيرة المشي (tahdhib)","source_summary":"Kaynak anlatımı, yarışta öne geçen atı yeri yutarcasına koşma imgesiyle verir. Aynı niteleme alanı develer için çok yürüme özelliğine uzanır, fakat bu ikinci kullanım açıkça hız bildirmez.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الفرس اللهم أو اللهميم السابق، والإبل الكثيرة المشي، وكل وصف للحركة كأنها تبتلع الأرض.","what_is_not_ar":"لا يدخل فيه مجرد الغزارة أو الجود أو كثرة الجيش إلا إذا كان الوصف للحركة والمشي."},"support_links":[]},{"boundary":"Büyüklük, çokluk, süt bolluğu ve cömertlik birbirine indirgenmez; her biri kendi biçim veya niteleme bağlamında geçerlidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001381/B004","candidate_links":[{"candidate_id":"cand_112d51b7c16ffada0528","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَلْهَمَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>alohama|ROOT:lhm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:8:1:2","qac_word_ref":"91:8:1","surface_ar":"أَلْهَمَ"}],"gloss":"büyüklük ve bolluk","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığın büyüklük, genişlik veya yeterlilik bakımından belirgin olması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan veya atın cömert ve çok veren olarak nitelenmesi."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dişi devenin çok süt veren, sütü bol bir hayvan olarak nitelenmesi."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Ordunun sayıca çok olup ortasında bulunanları görünmez kılacak yoğunlukta olması."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Dağ keçisinin ve ayrıca yaban sığırının iri veya büyük oluşunun nitelenmesi."}}],"root_ar":"ل ه م","root_id":"root_001381","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın büyüklük, genişlik, çokluk, bol verme ve bol süt sağlama kullanımlarını birleştiren üst çekirdeğidir.","boundary_detail":"Büyüklük, çokluk, süt bolluğu ve cömertlik birbirine indirgenmez; her biri kendi biçim veya niteleme bağlamında geçerlidir.","branch_image_ar":"عظم وسعة وغزارة وجوادية","concept_gloss":"büyüklük ve bolluk","contextual_glosses":[{"applicability":"Bir varlığın büyüklük ve yeterlilik bakımından öne çıktığı kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Büyüklük ve yeterlilik özelliklerini birlikte korur."},"facet_ids":["F001"],"text":"iri ve yeterli","usage_role":"contextual"},{"applicability":"İnsan veya atın cömertlik ve bol verme bakımından nitelendiği kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Cömertliği ve verilen şeyin çokluğunu korur."},"facet_ids":["F002"],"text":"eli açık, çok veren","usage_role":"contextual"},{"applicability":"Dişi devenin çok süt vermesiyle nitelendiği hayvan bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişi devenin süt bolluğu özelliğini korur."},"facet_ids":["F003"],"text":"bol sütlü","usage_role":"contextual"},{"applicability":"Ordunun sayıca çokluğu yüzünden ortasındakileri görünmez kıldığı kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ordunun çokluğunu ve içindekini görünmez kılmasını korur."},"facet_ids":["F004"],"text":"kalabalık ve kuşatıcı","usage_role":"explanatory"}],"definition":"Büyüklük, genişlik veya bolluğun bağlama göre yeterince büyük olma, çok verme, bol süt sağlama, sayıca çok olup içindekini görünmez kılma ya da iri hayvan olma biçiminde gerçekleşmesidir. Bu gerçekleşmeler ortak bir fazlalık ekseninde buluşur, fakat birbirinin yerine geçmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığın büyüklük, genişlik veya yeterlilik bakımından belirgin olması."},{"facet_id":"F002","role":"specialization","statement":"İnsan veya atın cömert ve çok veren olarak nitelenmesi."},{"facet_id":"F003","role":"specialization","statement":"Dişi devenin çok süt veren, sütü bol bir hayvan olarak nitelenmesi."},{"facet_id":"F004","role":"specialization","statement":"Ordunun sayıca çok olup ortasında bulunanları görünmez kılacak yoğunlukta olması."},{"facet_id":"F005","role":"extension","statement":"Dağ keçisinin ve ayrıca yaban sığırının iri veya büyük oluşunun nitelenmesi."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Cömertlik, çok verme, süt bolluğu ve ordu çokluğu kullanımlarını kaybeder.","preserves":"Fiziksel büyüklük ve irilik yönünü korur."},"text":"büyük"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yeterince büyük olma, hayvanın iriliği ve cömert kişi nitelemesini tek başına karşılamaz.","preserves":"Nicelikçe fazlalık ve bolluk yönünü korur."},"text":"bol"}],"identity_rationale":"Kaynak ifadesi büyüklük ve genişlik eksenini; yeterince büyük olan, bol veren, sütü bol, sayıca çok ordu ve iri hayvan kullanımlarıyla destekler. Dal korunabilir, ancak bu kullanımlar tek bir nesne türünün eş anlamlı adları değil, büyüklük veya bolluğun farklı bağlamlardaki gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bol sütlü dişi deve"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"cömert insan veya at"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"çok veren adam"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"iri ve yeterli olan"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ortasındakileri görünmez kılacak kadar kalabalık ordu"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"iri dağ keçisi; ayrıca iri yaban sığırı"}],"lexicalization_note":"Tanım, biçimlerdeki büyüklük ve cömertliği; hayvan, insan ve ordu nitelemelerindeki bağlama bağlı bolluk ve çokluk kullanımlarından ayırır.","neighbor_coverage_note":"Bütün büyüklük, bolluk ve armağan adayları değerlendirilmiş; genel büyüklük, çok verme, kalabalık ordu ve bol armağan sınırlarını en iyi gösteren dört aday seçilmiştir. Yaşam genişliği ve refah adayları daha uzak kaldığı için yayımlanmamıştır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal büyüklük ile çokluğun genel adlandırmasıdır; bu dal bunları cömertlik, süt bolluğu, ordu yoğunluğu ve iri hayvan gibi belirli kullanımlarda gerçekleştirir.","focus_only":"Süt bolluğu ve cömertlik yoluyla çok verme bu dala özgü belirgin gerçekleşmelerdir.","gloss":"büyük ve çok","neighbor_only":"Büyük ile küçük, çok ile az arasındaki genel karşıtlık komşu dalda daha geniştir.","neighbor_ref":"root_000255/B002","relation_type":"near_synonym","shared_zone":"İki dal da fiziksel büyüklük ve nicelikçe çokluk alanlarını kapsar."},{"boundary_match":"partial","distinction":"Bu dal çokluğu farklı varlıkların niteliği olarak verir; komşu dal ise çoklaştırma eylemini ve bol miktarda armağan vermeyi merkezine alır.","focus_only":"Fiziksel irilik, süt bolluğu ve kalabalık ordu bu dalda ayrıca bulunur.","gloss":"çokluk ve bol verme","neighbor_only":"Yükün veya malın çoğaltılması eylemi komşu dalda ayrıca bulunur.","neighbor_ref":"root_001624/B003","relation_type":"near_synonym","shared_zone":"İki dal da nicelikçe fazlalığı ve cömertçe çok vermeyi anlatır."},{"boundary_match":"partial","distinction":"Bu dal büyüklük ve bolluğun çeşitli gerçekleşmelerini toplar; komşu dal büyük veya kalabalık kitlenin ardındakini sürüklemesi tasarımıyla sınırlıdır.","focus_only":"Cömert insan veya at ile bol sütlü dişi deve nitelemeleri bu dala özgüdür.","gloss":"kalabalık ordu ve iri hayvan","neighbor_only":"Büyüklük veya çokluğun ardındakini sürükleme tasarımı komşu dala özgüdür.","neighbor_ref":"root_000235/B012","relation_type":"near_synonym","shared_zone":"İki dal da kalabalık orduyu ve büyük ya da çok sayıdaki hayvanları niteleyebilir."},{"boundary_match":"partial","distinction":"Komşu dal bol armağanın miktarıyla birlikte arzu edilirliğini kapsar; bu dal çok vermeyi daha geniş büyüklük ve bolluk ağının bir gerçekleşmesi olarak sunar.","focus_only":"Fiziksel büyüklük, süt bolluğu ve ordu çokluğu bu dalda yer alır.","gloss":"bol ve geniş armağan","neighbor_only":"Verilen şeyin arzu edilir olması komşu dalda ayrıca öne çıkar.","neighbor_ref":"root_000575/B004","relation_type":"near_synonym","shared_zone":"İki dal da cömertliği ve verilen şeyin çok ya da geniş olmasını anlatır."}],"source_phrase_ar":"العظيم الكافي اللهم واللهموم الرجل الجواد وهذا على العظم والسعة (maqayis)؛ اللهموم من النوق الغزيرة اللبن واللهموم الجواد من الناس والخيل واللهام الجيش الكثير واللهم العظيم ورجل لهم كثير العطاء (sihah)؛ إبل لهاميم إذا كانت غزارا وإذا كبر الوعل فهو لهم ويقال ذلك لبقر الوحش أيضا (tahdhib)","source_summary":"Kaynak anlatımı büyüklük ve genişliği, cömertlik ve çok verme ile ilişkilendirir; ayrıca bol sütlü dişi deveyi, kalabalık orduyu ve iri dağ keçisi ile yaban sığırını bu fazlalık alanına bağlar. Her kullanım kendi varlık türü ve niteliğiyle sınırlıdır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العظيم الكافي، والجواد كثير العطاء، والناقة الغزيرة اللبن، والجيش الكثير، والحيوان العظيم أو الكبير.","what_is_not_ar":"لا يدخل فيه اللهم بمعنى يا الله، ولا ملهم الموضع أو يوم ملهم، ولا الداهية إذا أريد بها المصيبة نفسها."},"support_links":["sup_d4164de075e7caa1b4b6"]},{"boundary":"Felaket temel adlandırmadır; ateşli hastalık ve ölüm kalıp biçime bağlıdır, herkesi alıp götürme gerekçesi de yalnızca ölüm kullanımını açıklar.","branch_kind":"mixed_non_bare","branch_ref":"root_001381/B005","candidate_links":[{"candidate_id":"cand_2e321606e0614a7f1ce4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَلْهَمَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>alohama|ROOT:lhm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:8:1:2","qac_word_ref":"91:8:1","surface_ar":"أَلْهَمَ"}],"gloss":"felaket; ateşli hastalık veya ölüm adı","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Büyük ve yıkıcı bir felaketin adlandırılması."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalıp biçimin ateşli hastalık için kullanılan bir ad olması."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kalıp biçimin ölüm için kullanılan bir ad olması."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Ölüm adının, ölümün herkesi alıp götürmesi düşüncesiyle açıklanması."}}],"root_ar":"ل ه م","root_id":"root_001381","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın biçimdeki felaket anlamını ve kalıp biçimdeki ateşli hastalık ile ölüm adlandırmalarını birlikte gösterir.","boundary_detail":"Felaket temel adlandırmadır; ateşli hastalık ve ölüm kalıp biçime bağlıdır, herkesi alıp götürme gerekçesi de yalnızca ölüm kullanımını açıklar.","branch_image_ar":"داهية تلتهم ما تلقى","concept_gloss":"felaket; ateşli hastalık veya ölüm adı","contextual_glosses":[{"applicability":"Yalın veya kalıp biçimin büyük bir felaketi adlandırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Felaketin büyüklüğünü ve yıkıcı niteliğini korur."},"facet_ids":["F001"],"text":"yıkıcı felaket","usage_role":"general"},{"applicability":"Kalıp biçimin hastalık adı olarak kullanıldığı özel bağlam için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hastalık adlandırmasının ateş ve nöbet yönünü korur."},"facet_ids":["F002"],"text":"ateşli hastalık","usage_role":"contextual"},{"applicability":"Kalıp biçimin ölüm adı olarak kullanılıp ölümün herkesi kapsamasıyla açıklandığı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölüm adını ve herkesi alıp götürme gerekçesini korur."},"facet_ids":["F003","F004"],"text":"herkesi alıp götüren ölüm","usage_role":"explanatory"}],"definition":"Yalın biçimde büyük ve yıkıcı bir felaketi adlandırır. Kalıp biçimde yine felaket için kullanılabildiği gibi ateşli hastalığın veya herkesi alıp götürdüğü düşünülen ölümün adı da olur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Büyük ve yıkıcı bir felaketin adlandırılması."},{"facet_id":"F002","role":"source_variant","statement":"Kalıp biçimin ateşli hastalık için kullanılan bir ad olması."},{"facet_id":"F003","role":"source_variant","statement":"Kalıp biçimin ölüm için kullanılan bir ad olması."},{"facet_id":"F004","role":"associated_use","statement":"Ölüm adının, ölümün herkesi alıp götürmesi düşüncesiyle açıklanması."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın biçimdeki felaket anlamını ve kalıp biçimin ateşli hastalık adını kaybeder.","preserves":"Kalıp biçimin ölüm adı olarak kullanımını korur."},"text":"ölüm"}],"identity_rationale":"Kaynak ifadesi yalın biçimi doğrudan büyük bir felaket, kalıp biçimi ise felaketin yanı sıra ateşli hastalık ve ölüm için kullanılan bir ad olarak verir. Her şeyi yutma gerekçesi yalnızca ölüm adlandırması için açıklandığından, geçici çerçevenin bütün dalı yutan felaket olarak sunması düzeltilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"büyük ve yıkıcı felaket"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"felaket, ateşli hastalık veya herkesi alıp götüren ölüm için kullanılan ad"}],"lexicalization_note":"Tanım, yalın biçimdeki felaket anlamını kalıp biçimin felaket, ateşli hastalık ve ölüm adlandırmalarından ayırır.","neighbor_coverage_note":"Bütün felaket, ölüm, ateşli hastalık ve yıkım adayları değerlendirilmiş; adlandırma sınırını en iyi gösteren dört komşu seçilmiştir. Diğer musibet ve güçten düşürme adayları aynı ayrımları yinelediği için yayımlanmamıştır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal felaketin yanında ateşli hastalık ve ölüm için özel bir ad taşır; komşu dal ise felaketin veya ölümün insana tutunması tasarımını öne çıkarır.","focus_only":"Ateşli hastalık adı ve ölümün herkesi alıp götürmesi açıklaması bu dala özgüdür.","gloss":"felaket veya ölüm","neighbor_only":"Felaket veya ölümün insana tutunması tasarımı komşu dala özgüdür.","neighbor_ref":"root_001039/B014","relation_type":"near_synonym","shared_zone":"İki dal da büyük felaketi ve insanın ölümle karşılaşmasını adlandırabilir."},{"boundary_match":"partial","distinction":"Komşu dal başa gelen olay veya felaket olmayı merkezine alır; bu dal belirli biçimlerin felaket, ateşli hastalık ve ölüm adı olmasını anlatır.","focus_only":"Ölüm adı ve herkesi alıp götürme gerekçesi bu dalda belirgindir.","gloss":"başa gelen felaket","neighbor_only":"İnsanın başına gelen olayın veya felaketin zaman zaman yinelenmesi komşu dalda bulunur.","neighbor_ref":"root_001562/B004","relation_type":"near_synonym","shared_zone":"İki dal da insanın başına gelen felaketi ve ateşli hastalığı kapsayabilir."},{"boundary_match":"partial","distinction":"Komşu dal felaketin insanları veya malı silip süpüren etkisini anlatır; bu dal felaketi adlandırır ve ayrıca ateşli hastalık ile ölümü kapsar.","focus_only":"Ateşli hastalık ve herkesi alan ölüm için özel adlandırmalar bu dala özgüdür.","gloss":"süpürücü yıkım","neighbor_only":"Salgın, sel veya kötü kazançla insanları ya da malı yıkıma uğratma komşuya özgüdür.","neighbor_ref":"root_000238/B003","relation_type":"near_synonym","shared_zone":"İki dal da geniş etkili, yıkıcı bir felaket düşüncesinde buluşur."},{"boundary_match":"partial","distinction":"Komşu dal zamanın getirdiği olay ve musibetleri genel olarak belirtir; bu dal belirli biçimlerle felaket, ateşli hastalık ve ölümü adlandırır.","focus_only":"Ateşli hastalık ve ölüm için kalıplaşmış adlandırma bu dala özgüdür.","gloss":"zamanın felaketi","neighbor_only":"Zaman içinde ortaya çıkan olay ve dönemsel musibet olma özelliği komşuya özgüdür.","neighbor_ref":"root_000299/B005","relation_type":"near_synonym","shared_zone":"İki dal da beklenmedik büyük olayları ve insanın başına gelen felaketleri anlatır."}],"source_phrase_ar":"اللهيم الداهية وكذلك أم اللهيم (maqayis;sihah)؛ أم اللهيم هي الحمى (tahdhib)؛ أم اللهيم كنية الموت لأنه يلتهم كل أحد (tahdhib)","source_summary":"Kaynak anlatımı yalın ve kalıp biçimleri felaket adı olarak verir. Kalıp biçim ayrıca ateşli hastalığı ve ölümü adlandırır; ölüm kullanımı, ölümün herkesi alıp götürmesi düşüncesiyle gerekçelendirilir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه اللهيم وأم اللهيم للداهية، والحمى، وكنية الموت من جهة أنه يلتهم كل أحد.","what_is_not_ar":"لا يدخل فيه مطلق العظم أو كثرة العطاء، ولا أسماء المواضع والأيام."},"support_links":["sup_b110be56511440060846"]},{"boundary":"Dal genel koruma işlemini ve koruyucu aracı kapsar; kişinin kendini sakınması, ağırlık ölçüsü, hayvanın aksaması ve kuş adı bu sınıra girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B001","candidate_links":[{"candidate_id":"cand_112d51b7c16ffada0528","lane":"micro"},{"candidate_id":"cand_2e321606e0614a7f1ce4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَقْوَى","morph_features":"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:3:2","qac_word_ref":"91:8:3","surface_ar":"تَقْوَىٰ"}],"gloss":"araya engel koyarak zarardan koruma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Korunan şeyden zarar verici etkiyi uzak tutma ve onu incinmekten ya da bozulmaktan saklama işlemidir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koruma, zarar ile korunacak şey arasına başka bir araç, katman veya engel koyularak gerçekleştirilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kadının saçı ile dış örtüsü arasına koyduğu bez, bu koruyucu ara katmanın özel bir örneğidir."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel eylem ile koruyucu aracın ortak çekirdeğini, herhangi bir özel kullanım alanına bağlamadan karşılar.","boundary_detail":"Dal genel koruma işlemini ve koruyucu aracı kapsar; kişinin kendini sakınması, ağırlık ölçüsü, hayvanın aksaması ve kuş adı bu sınıra girmez.","branch_image_ar":"دفع الضرر بوقاية","concept_gloss":"araya engel koyarak zarardan koruma","contextual_glosses":[{"applicability":"Eylemden çok, zarar ile korunacak şey arasına koyulan araç veya katman kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Araya koyulan unsurun koruyucu işlevini ve zararı kesen konumunu korur."},"facet_ids":["F002"],"text":"koruyucu engel","usage_role":"contextual"},{"applicability":"Kadına ait özel bez kullanımını açıkça anlatan bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bezin yerini, maddi niteliğini ve koruyucu ara katman işlevini korur."},"facet_ids":["F003"],"text":"saç ile dış örtü arasındaki koruyucu bez","usage_role":"explanatory"}],"definition":"Bir şeyi ona zarar verecek başka bir şeyden korumak için araya bir araç ya da engel koyma ve böylece zararı ondan uzak tutma. Bu işlevi gören araç veya engel de aynı kavram alanında adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Korunan şeyden zarar verici etkiyi uzak tutma ve onu incinmekten ya da bozulmaktan saklama işlemidir."},{"facet_id":"F002","role":"core","statement":"Koruma, zarar ile korunacak şey arasına başka bir araç, katman veya engel koyularak gerçekleştirilir."},{"facet_id":"F003","role":"example","statement":"Kadının saçı ile dış örtüsü arasına koyduğu bez, bu koruyucu ara katmanın özel bir örneğidir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi ona zarar verecek başka bir şeyden korumayı ve bunun için araya koruyucu bir unsur koymayı ortak çekirdek olarak verir. Koruyucu bez örneği bu genel işlemin özel bir gerçekleşmesidir ve dalın kimliğini değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi koruyucu bir engelle zarardan saklamak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"koruma; zararı önleyen araç veya engel"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyi korumaya yarayan araç ya da engel"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"zarardan koruyan şey"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"zararı savan koruyucu"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kadının saçı ile dış örtüsü arasına koyduğu koruyucu bez"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"koruyucu şeyler"}],"lexicalization_note":"Tanım, genel koruma çekirdeğini özel ad ve kalıplardan ayırır; kadına ait koruyucu bez yalnızca yapıya bağlı bir örnek olarak tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlanan beş ilişki koruma çekirdeğine en yakın sınırları gösterir. Kale, bekçilik, tutunarak korunma, üstü açıklık ve öteki kök içi dallar ya daha uzak alan ortaklığı kurar ya da ayrı adlandırmalardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda ayırt edici unsur, başka bir şeyi koruyucu engel olarak araya koymaktır; komşu dalın çekirdeği ise etkiyi bulunduğu yerden itmek veya doğrudan savmaktır.","focus_only":"Koruma, zarar ile hedef arasına başka bir unsur koyma mekanizmasıyla tanımlanır.","gloss":"koruma ile itip uzaklaştırma","neighbor_only":"Öteki dal yer değiştirtmeyi, karşılıklı itişmeyi ve kötülüğü doğrudan savmayı da kapsar.","neighbor_ref":"root_000480/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da zararlı veya istenmeyen bir etkinin hedefe ulaşmasını engeller."},{"boundary_match":"partial","distinction":"Bu dal koruyucu engel üzerinden zararı savmaya odaklanır; komşu dal ise engel gerektirmeyen bakım, gözetim ve süreklilik taşıyan kollamayı da içerir.","focus_only":"Zararı kesen bir araç ya da engelin araya girmesi açıkça kurucu unsurdur.","gloss":"koruma ile gözetip kollama","neighbor_only":"Sürekli gözetme, bakım, kollama ve bir şeyi iyi durumda tutma süreçlerini de kapsar.","neighbor_ref":"root_000372/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi zarar ve bozulmadan uzak tutma alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal genel koruma işlemi ile onun aracını birlikte kapsar; komşu dal belirli bir koruyucu engel veya dayanak kavramında yoğunlaşır.","focus_only":"Koruma eylemi her tür araç veya katmanla gerçekleştirilebilir ve araç da adlandırılabilir.","gloss":"koruyucu araç ile koruyan engel","neighbor_only":"Koruyan ve çevreleyen belirli bir engel ya da dayanak adı merkezde yer alır.","neighbor_ref":"root_000071/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda bir engel, dış etkiden koruma ve çevreleyerek güvence sağlama işlevi görür."},{"boundary_match":"partial","distinction":"Komşu dal giysilerin birbirini koruduğu özel uygulamayı adlandırır; bu dal ise aynı araya koyma mekanizmasını her tür korunacak şeye açar.","focus_only":"Korunacak varlık ve zarar türü bakımından genel bir koruma şeması sunar.","gloss":"genel koruma ile giysiyi örtüyle koruma","neighbor_only":"Bir giysiyi başka bir giysiyle örtüp yıpranmaktan koruyan özel uygulamaya bağlıdır.","neighbor_ref":"root_001635/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir katman, başka bir şeyi yıpranma veya zarardan korur."},{"boundary_match":"partial","distinction":"Bu dal genel ve çoğu kez maddi koruma ilişkisini anlatır; komşu dal aynı şemayı kişinin kendi davranışını ve güvenliğini gözetmesine özgüler.","focus_only":"Korunan katılımcı herhangi bir nesne veya canlı olabilir ve maddi bir engel kullanılabilir.","gloss":"bir şeyi koruma ile kendini sakınma","neighbor_only":"Korunan katılımcı kişinin kendisidir; korkulan şeyden ve yanlış davranıştan sakınma öne çıkar.","neighbor_ref":"root_001677/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da zarar ile korunacak taraf arasına koruyucu bir mesafe veya önlem koyar."}],"source_phrase_ar":"دفع شيء عن شيء بغيره (maqayis)؛ كل ما وقى شيئا فهو وقاء له ووقاية (ayn;jamhara;tahdhib)؛ حفظ الشيء مما يؤذيه ويضره (mufradat)؛ وقاية المرأة وهي الخرقة التي بين جلبابها وشعرها (jamhara)","source_summary":"Kaynakların ortak anlatımı, korumayı zararlı etkiyi başka bir şey aracılığıyla savma olarak kurar; hem koruma eylemini hem de bu işte kullanılan engeli kapsar. Kadının saçını dış örtüden ayıran bez, bu mekanizmanın özel bir örneğidir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه وقى الشيء وحفظه مما يؤذيه، والوقاء والوقاية والواقية وما يجعل حاجزا بين الشيء والضرر، ووقاية المرأة","what_is_not_ar":"لا يدخل فيه اسم الوزن أوقية ولا اسم الصرد ولا الظلع اليسير إلا من جهة الصورة العامة للاتقاء"},"support_links":["sup_b110be56511440060846","sup_d4164de075e7caa1b4b6"]},{"boundary":"Dal kişinin kendisini koruması ve sakınmasıyla sınırlıdır; herhangi bir nesneyi koruma, yalnız başına iyi iş yapma veya işlenmiş yanlıştan dönme anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B002","candidate_links":[{"candidate_id":"cand_daba8183049900fc31ab","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَقْوَى","morph_features":"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:3:2","qac_word_ref":"91:8:3","surface_ar":"تَقْوَىٰ"}],"gloss":"korkulan şeyden ya da yanlış davranıştan kendini koruma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, korkulan ya da zarar verecek şey ile kendi arasına koruyucu bir önlem koyar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Öz-koruma, kişiyi suç doğuran ve yanlış sayılan davranışlardan uzak tutma biçimini alabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanrı'ya karşı gelmekten sakınma, kişi ile sakınılan sonuç arasına koruyucu bir tutum koymak olarak düşünülür."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem genel öz-koruma çekirdeğini hem de kişiyi yanlış davranıştan uzak tutan yönünü birlikte verir.","boundary_detail":"Dal kişinin kendisini koruması ve sakınmasıyla sınırlıdır; herhangi bir nesneyi koruma, yalnız başına iyi iş yapma veya işlenmiş yanlıştan dönme anlamına genişletilmez.","branch_image_ar":"جعل النفس في وقاية","concept_gloss":"korkulan şeyden ya da yanlış davranıştan kendini koruma","contextual_glosses":[{"applicability":"Korunulan tehlike veya yanlış davranış bağlamdan açıkça anlaşıldığında doğal ve kısa bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Korkulan şeyin veya yanlış davranışın türünü ve araya önlem koyma şemasını açıkça söylemez.","preserves":"Kişinin kendi güvenliğini ve davranışını gözeten öz-koruma yönünü korur."},"facet_ids":["F001","F002"],"text":"kendini sakınma","usage_role":"general"},{"applicability":"İnanç ve sorumluluk bağlamında, kişinin davranışını yasak olandan uzak tutması kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnanç bağlamındaki muhatabı, sakınma tutumunu ve yanlış davranıştan uzak durmayı korur."},"facet_ids":["F003"],"text":"Tanrı'ya karşı gelmekten sakınma","usage_role":"contextual"}],"definition":"Kişinin kendisini korktuğu veya zarar beklediği şeyden koruyacak bir önlem altına alması ve yanlış davranıştan uzak tutması. Tanrı'ya karşı gelmekten sakınma, bu öz-koruma tutumunun inanç alanındaki özel biçimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, korkulan ya da zarar verecek şey ile kendi arasına koruyucu bir önlem koyar."},{"facet_id":"F002","role":"specialization","statement":"Öz-koruma, kişiyi suç doğuran ve yanlış sayılan davranışlardan uzak tutma biçimini alabilir."},{"facet_id":"F003","role":"specialization","statement":"Tanrı'ya karşı gelmekten sakınma, kişi ile sakınılan sonuç arasına koruyucu bir tutum koymak olarak düşünülür."}],"identity_rationale":"Kaynak ifadesi, kişinin kendisini korktuğu şeyden koruma altına almasını ve yanlış davranıştan uzak tutmasını aynı öz-koruma şemasında birleştirir. Tanrı'ya karşı gelmekten sakınma bu çekirdeğin inanç alanındaki belirgin gerçekleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kendini korkulan ya da zarar verecek şeyden korumak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyi kendine koruyucu yapmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"Tanrı'ya karşı gelmekten sakınmak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kişinin kendini korktuğu şeyden ve yanlış davranıştan koruması"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"sakınma ve kendini koruma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sakınan ve kendini yanlış davranıştan koruyan kimse"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"sakınma; kendini kötülükten koruma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"sakınıp kendini koruma"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kendini yanlış davranışlardan koruyan kimse"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"sakınan ve kendini yanlış davranıştan koruyan kimse"}],"lexicalization_note":"Genel öz-koruma anlamı ile bir aracı kendine koruyucu yapma ve Tanrı'ya karşı gelmekten sakınma kalıpları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler genel koruma, yanlıştan uzak durma, iyi davranış, suç korkusu ve tapınma sınırlarını en açık biçimde gösterir. Bağışlanma, tövbeye çağırma, benlik ve örtü adayları daha dolaylıdır; öteki kök içi dallar ayrı anlamlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal genel koruma şemasını kişinin kendi güvenliğine ve davranışına taşır; komşu dal katılımcıyı ve zarar türünü sınırlandırmayan genel korumadır.","focus_only":"Korunan taraf zorunlu olarak kişinin kendisidir ve davranışsal sakınma da kapsama girer.","gloss":"kendini sakınma ile genel koruma","neighbor_only":"Herhangi bir nesne veya canlı, maddi bir araç ya da engel kullanılarak korunabilir.","neighbor_ref":"root_001677/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da zarar ile korunacak taraf arasına koruyucu bir önlem koyma şeması vardır."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği önleyici öz-korumadır; komşu dal ise yanlış karşısında çekinmenin yanında işlenmiş bir yanlıştan çıkma sonucunu da kapsar.","focus_only":"Henüz gerçekleşmemiş tehlikeden ve yanlış davranıştan önleyici biçimde korunmayı da kapsar.","gloss":"yanlıştan sakınma ile yanlışın yükünden çıkma","neighbor_only":"İşlenmiş bir yanlışın yükünden çıkma ve ondan dönmüş olma anlamına kadar uzanabilir.","neighbor_ref":"root_000013/B002","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin yanlış davranıştan uzak durmasını ve suç doğuran eylemi işlememesini anlatabilir."},{"boundary_match":"partial","distinction":"Bu dal koruyucu ve kaçınmacı tutumu tanımlar; komşu dal ise sakınmanın ötesinde olumlu iyilik ve itaat eylemlerini geniş biçimde kapsar.","focus_only":"Korkulan sonuç ile kişi arasına koruyucu bir sakınma tutumu koymak merkezde yer alır.","gloss":"sakınma ile iyilik ve itaat","neighbor_only":"İyi olma, itaat ve çok çeşitli yararlı işleri yapma yönünde olumlu bir eylem alanı sunar.","neighbor_ref":"root_000104/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal doğru davranışa yönelmeyi ve yanlış olandan uzak kalmayı destekler."},{"boundary_match":"partial","distinction":"Bu dal koruyucu davranış ve uzak durma eylemidir; komşu dal ise suç durumunu ve ona düşme korkusunu merkeze alır.","focus_only":"Kişinin korkulan veya suç doğuran durumdan kendini etkin biçimde korumasını anlatır.","gloss":"suçtan korunma ile suç korkusu","neighbor_only":"Suçun kendisini, suç kazanmayı ve kötü davranışa düşme korkusunu adlandırır.","neighbor_ref":"root_001051/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da yanlış davranış, onun doğuracağı yük ve bundan duyulan korku bulunur."},{"boundary_match":"field_only","distinction":"Ortak alan inanç ve sorumluluktur; bu dal sakınma yoluyla öz-korumayı, komşu dal ise tapınma ve yakınlık arama eylemini tanımlar.","focus_only":"Yanlış davranıştan uzak durarak kişinin kendisini koruması öne çıkar.","gloss":"sakınma ile tapınma","neighbor_only":"Tapınma, yakınlık arama ve kulluk eylemlerini olumlu uygulamalar olarak adlandırır.","neighbor_ref":"root_001498/B001","relation_type":"same_field","shared_zone":"İki dal inanç alanında kişinin Tanrı karşısındaki davranışını konu edinir."}],"source_phrase_ar":"اتق الله توقه أي اجعل بينك وبينه كالوقاية (maqayis)؛ التقوى في الأصل وقوى فعلى من وقيت (ayn;tahdhib)؛ التقوى جعل النفس في وقاية مما يخاف (mufradat)؛ حفظ النفس عما يؤثم (mufradat)؛ اتقى تقية وتقاة (sihah)","source_summary":"Kaynaklar bu dalı, kişinin kendisini korkulan şey karşısında koruma altına alması ve yanlış davranıştan uzak tutması olarak açıklar. İnanç bağlamındaki kullanım, Tanrı'ya karşı gelmekten sakınmayı kişi ile kötü sonuç arasındaki koruyucu tutum şeklinde somutlaştırır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اتقى واتقاء وتقوى وتقى وتقاة وتقية وتقي، أي توقي الله أو النار أو المعاصي أو ما يخاف","what_is_not_ar":"لا يدخل فيه مطلق الوقاية المادية إلا إذا صار اتقاء للنفس"},"support_links":["sup_18176688d1b7ccdf56c6"]},{"boundary":"Çekirdek hafif topallama ve ağrılı ya da hassas toynak yüzünden sakınarak yürümedir; eyer, emir ve sert zemin kullanımları bağımlı yan kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَقْوَى","morph_features":"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:3:2","qac_word_ref":"91:8:3","surface_ar":"تَقْوَىٰ"}],"gloss":"hafif topallama ve toynak ağrısıyla yürümekten çekinme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tek sözcüklü temel anlam, hayvanın yürüyüşündeki hafif topallamadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"At, topalladığı veya toynağındaki ağrı yüzünden yürümekten çekindiği ve sert zeminde ayağını sakındığı için bu nitelemeyi alır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvana yönelik emir kalıbı, onun aksayışını gözeterek yürümeyi sürdürme ve kendini zorlamama anlamı taşır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Eyer için kullanıldığında hayvanın sırtını yaralamayan veya berelenmesine yol açmayan eyer anlatılır."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Sert ve engebeli zeminle kurulan olumsuz emir, arazinin güçlüğünden yakınmama anlamına gelir."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın tek sözcüklü çekirdeğini ve atın ağrılı ya da hassas toynak nedeniyle gösterdiği sakınan yürüyüşü birlikte karşılar.","boundary_detail":"Çekirdek hafif topallama ve ağrılı ya da hassas toynak yüzünden sakınarak yürümedir; eyer, emir ve sert zemin kullanımları bağımlı yan kullanımlardır.","branch_image_ar":"توقي الدابة من وجع الحافر","concept_gloss":"hafif topallama ve toynak ağrısıyla yürümekten çekinme","contextual_glosses":[{"applicability":"Tek sözcüklü durum adı, neden veya hayvanın türü ayrıca belirtilmeden kullanıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aksamanın hafif derecesini ve yürüyüş bozukluğu olmasını doğrudan korur."},"facet_ids":["F001"],"text":"hafif topallama","usage_role":"general"},{"applicability":"Atın topallaması veya toynak acısı yüzünden adım atmaktan çekinmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan türünü, toynaktaki ağrıyı ve bunun yol açtığı çekingen yürüyüşü korur."},"facet_ids":["F002"],"text":"toynak ağrısıyla yürümekten çekinen at","usage_role":"explanatory"},{"applicability":"Topallayan hayvana ya da biniciye, mevcut aksamayı gözeterek yürümeyi sürdürmesi söylendiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aksamayı sürdürme, onu hesaba katma ve hareketi zorlamama yönündeki emri korur."},"facet_ids":["F003"],"text":"aksayışını gözet ve ağırdan al","usage_role":"contextual"},{"applicability":"Eyerin hayvanın sırtında yara veya bere oluşturmadığı belirtilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eyerin türünü ve hayvanın sırtını yaralamama sonucunu açıkça korur."},"facet_ids":["F004"],"text":"yara açmayan eyer","usage_role":"contextual"}],"definition":"Hafif topallama ile, özellikle toynak ağrısı veya hassasiyeti yüzünden yürümekten çekinen ya da sert zeminde ayağını sakınan atın durumu. Aynı kullanım kümesi, hayvanın aksamasına göre davranmayı, sert zeminden yakınmamayı ve hayvanda yara açmayan eyeri de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tek sözcüklü temel anlam, hayvanın yürüyüşündeki hafif topallamadır."},{"facet_id":"F002","role":"specialization","statement":"At, topalladığı veya toynağındaki ağrı yüzünden yürümekten çekindiği ve sert zeminde ayağını sakındığı için bu nitelemeyi alır."},{"facet_id":"F003","role":"associated_use","statement":"Hayvana yönelik emir kalıbı, onun aksayışını gözeterek yürümeyi sürdürme ve kendini zorlamama anlamı taşır."},{"facet_id":"F004","role":"associated_use","statement":"Eyer için kullanıldığında hayvanın sırtını yaralamayan veya berelenmesine yol açmayan eyer anlatılır."},{"facet_id":"F005","role":"associated_use","statement":"Sert ve engebeli zeminle kurulan olumsuz emir, arazinin güçlüğünden yakınmama anlamına gelir."}],"identity_rationale":"Kaynak ifadesi yalnızca toynak ağrısından kaçınmayı değil, hafif topallamayı, topallayan atın davranışını, hayvanda yara açmayan eyeri ve aksayışa göre davranma sözünü birlikte verir. Bu nedenle dal korunabilir, fakat geçici hayvanın kendini koruması çerçevesi bütün malzemeyi taşıyacak biçimde aksama ve ona bağlı kullanımlar olarak yeniden kurulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"hafif topallama"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"topallayan, toynak ağrısıyla yürümekten çekinen veya ayağını sert zeminden sakınan at"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"hayvanın sırtında yara açmayan eyer"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"aksayışını gözet ve ağırdan al"}],"lexicalization_note":"Tek sözcüklü hafif topallama anlamı, atın yürüyüşü ile eyer ve emir kalıplarına bağlı anlamlardan açıkça ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan ilişkiler genel aksama, uzuv hastalığı, toynak anatomisi ve koruma bağlantısını ayırır. Keçi hastalıkları, düzensiz yürüyüş, binme ve öteki kök içi dallar daha uzak alan ortaklıklarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal hafif dereceyi ve toynak ağrısına bağlı çekingen yürüyüşü belirginleştirir; komşu dal daha genel aksama durumunda kalır.","focus_only":"Toynak ağrısıyla yürümekten çekinme ile yara açmayan eyer ve emir gibi bağımlı kullanımları da kapsar.","gloss":"hafif topallama ile hayvandaki genel aksama","neighbor_only":"Hayvandaki aksama veya eziklik daha genel bir durum adı olarak verilir ve koruyucu yan kullanımlar taşımaz.","neighbor_ref":"root_000448/B009","relation_type":"near_synonym","shared_zone":"Her iki dal hayvanın, özellikle atın, aksayan veya topallayan yürüyüşünü anlatır."},{"boundary_match":"partial","distinction":"Bu dal ağrının yürüyüşteki belirtisini ve sakınma davranışını anlatır; komşu dal ise ağrıyı doğuran hastalık veya yaralanmanın kendisini adlandırır.","focus_only":"Ağrıya verilen topallama ve yürümekten çekinme tepkisi ile ona bağlı kullanımlar merkezde yer alır.","gloss":"ağrılı yürüyüş ile uzuvdaki hastalık","neighbor_only":"Omuz veya toynağı etkileyen hastalığı ve taşın tırnak ya da toynağı çizmesini doğrudan adlandırır.","neighbor_ref":"root_001546/B006","relation_type":"near_neighbor","shared_zone":"İki dal toynak veya başka bir uzuvdaki ağrı ve bunun hayvan üzerindeki etkisiyle ilgilidir."},{"boundary_match":"field_only","distinction":"Ortak alan toynaktır; bu dal toynağa bağlı ağrı ve yürüyüş davranışını, komşu dal ise anatomik uzvun kendisini tanımlar.","focus_only":"Toynak ağrısının yol açtığı topallama ve sakınan yürüyüşü anlatır.","gloss":"toynak ağrısıyla yürüme ile toynak","neighbor_only":"Toynağın kendisini, biçimini ve zeminde iz açan uzuv olmasını adlandırır.","neighbor_ref":"root_000341/B002","relation_type":"same_field","shared_zone":"Her iki dal atın veya başka bir hayvanın toynağını ortak katılımcı olarak içerir."},{"boundary_match":"field_only","distinction":"Bu dal bir yürüyüş durumu ve ağrı tepkisidir; komşu dal ise toynağın sağ ve sol yanlarını gösteren anatomik addır.","focus_only":"Hayvanın ağrı nedeniyle aksaması ve sert zeminde ayağını sakınması bulunur.","gloss":"toynak ağrısı ile toynağın yanları","neighbor_only":"Toynağın iki yanındaki belirli anatomik bölümleri adlandırır.","neighbor_ref":"root_000358/B010","relation_type":"same_field","shared_zone":"Her iki dal toynak yapısı ve hayvanın ayağı çevresindeki aynı somut alana bağlıdır."},{"boundary_match":"thematic_only","distinction":"Koruma bu dalda yalnızca bazı at ve eyer kullanımlarının bağımlı yönüdür; komşu dalda ise bütün kavramın genel çekirdeğidir.","focus_only":"Hafif topallama ve ağrı yüzünden sakınarak yürüme, dalın temel kimliğini oluşturur.","gloss":"aksayarak sakınma ile genel koruma","neighbor_only":"Her tür varlığı zarardan korumak için araya araç veya engel koyan genel işlemi tanımlar.","neighbor_ref":"root_001677/B001","relation_type":"thematic","shared_zone":"Atın ayağını sert zeminden sakınması ve eyerin yara açmaması koruma düşüncesiyle ilişki kurar."}],"source_phrase_ar":"الوقى هو الظلع اليسير (maqayis)؛ فرس واق إذا كان ظالعا (ayn)؛ ق على ظلعك أي الزمه (sihah)؛ فرس واق إذا كان يهاب المشي من وجع يجده في حافره (sihah)؛ سرج واق إذا لم يكن معقرا (sihah;tahdhib)؛ لا تقي بالجدجد أي لا تشتكي حزونة الأرض (tahdhib)","source_summary":"Toplu kaynak ifadesi hafif topallamayı çekirdek yapar ve bunu topallayan, toynak ağrısı yüzünden yürümekten çekinen ya da sert zeminde ayağını sakınan atla açımlar. Aksamaya göre davranma, sert zeminden yakınmama ve yara açmayan eyer kullanımları aynı kümede yer alan fakat çekirdeğe bağımlı yan kullanımlardır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الوَقَى بمعنى الظلع اليسير، والفرس الواقي إذا يهاب المشي أو يقي حافره الموضع الغليظ، والسرج الواقي غير المعقر","what_is_not_ar":"لا يدخل فيه الوقاية العامة ولا التقوى ولا اسم الصرد"},"support_links":[]},{"boundary":"Dal yalnızca bu adlandırılmış ağırlık ölçüsü ve onun biçimleriyle sınırlıdır; genel tartma eylemine, her türlü miktara veya modern bir ölçü adına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَقْوَى","morph_features":"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:3:2","qac_word_ref":"91:8:3","surface_ar":"تَقْوَىٰ"}],"gloss":"kırk gümüş para ağırlığındaki, yağda yedi birimlik biçimi bulunan ölçü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel biçim, belirli bir ağırlık ölçüsüdür ve para hesabında kırk gümüş paranın ağırlığına eşitlenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başındaki ses düşmüş biçim, yağ ölçümünde kullanılan ve yedi temel ağırlık birimine eşit sayılan ayrı bir değeri bildirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başlangıç sesini koruyan biçim daha düzgün kabul edilir ve ölçü adının iki çoğul söylenişi kaydedilir."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölçü ailesinin iki bağlama göre değişen değerini tek açıklayıcı karşılıkta birlikte göstermenin gerektiği yerlerde kullanılır.","boundary_detail":"Dal yalnızca bu adlandırılmış ağırlık ölçüsü ve onun biçimleriyle sınırlıdır; genel tartma eylemine, her türlü miktara veya modern bir ölçü adına genişletilmez.","branch_image_ar":"الأوقية وزن معلوم","concept_gloss":"kırk gümüş para ağırlığındaki, yağda yedi birimlik biçimi bulunan ölçü","contextual_glosses":[{"applicability":"Para ağırlığının esas alındığı ilk biçim ve kullanım kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölçünün ağırlık niteliğini ve kırk gümüş para ağırlığına eşit değerini korur."},"facet_ids":["F001"],"text":"kırk gümüş para ağırlığına denk ölçü","usage_role":"contextual"},{"applicability":"Başındaki ses düşmüş biçimin yağ ölçümündeki özel değeri açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağ bağlamını, ağırlık ölçüsü olmasını ve yedi temel birime eşit değeri korur."},"facet_ids":["F002"],"text":"yağ için yedi temel birimlik ağırlık ölçüsü","usage_role":"explanatory"},{"applicability":"Ölçü adının birden fazla çoğul söylenişi bulunduğu açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Söz konusu biçimlerin aynı ağırlık ölçüsü adının çoğulları olmasını korur."},"facet_ids":["F003"],"text":"bu ağırlık ölçüsünün çoğul biçimleri","usage_role":"explanatory"}],"definition":"Bir kullanımda kırk gümüş paranın ağırlığına, başındaki ses düşmüş başka bir biçim ve kullanımda ise yağ için yedi temel ağırlık birimine eşit kabul edilen ölçü. İlk biçim daha düzgün sayılır ve birden çok çoğul biçimi vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel biçim, belirli bir ağırlık ölçüsüdür ve para hesabında kırk gümüş paranın ağırlığına eşitlenir."},{"facet_id":"F002","role":"source_variant","statement":"Başındaki ses düşmüş biçim, yağ ölçümünde kullanılan ve yedi temel ağırlık birimine eşit sayılan ayrı bir değeri bildirir."},{"facet_id":"F003","role":"source_variant","statement":"Başlangıç sesini koruyan biçim daha düzgün kabul edilir ve ölçü adının iki çoğul söylenişi kaydedilir."}],"identity_rationale":"Kaynak ifadesi dalı bilinen bir ağırlık ölçüsü olarak doğrular, ancak tek ve değişmez bir nicelik vermez. Bir kullanım kırk gümüş para ağırlığını, başındaki ses düşmüş başka bir biçim ise yağ için yedi temel ağırlık birimini gösterir; tanım bu bağlam farkını açıkça korumalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kırk gümüş para ağırlığına eşit bilinen ölçü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yağ için yedi temel ağırlık birimine eşit ölçü"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bu ağırlık ölçüsü adının çoğul biçimleri"}],"lexicalization_note":"Tanım, iki sözcük biçimine bağlı farklı ölçü değerlerini ve çoğul biçimleri ayırır; bunlardan genel bir kök anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlananlar genel ağırlık, küçük para ölçüsü, başka geleneksel birim, hacim-miktar ölçüsü ve ayar standardı sınırlarını gösterir. Artış ve çok büyük tahıl ölçüsü daha uzaktır; öteki kök içi dallar anlamsal olarak ayrıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal değerleri ve sözcük biçimleri belirlenmiş tek bir geleneksel ölçüyü adlandırır; komşu dal ağırlık ve tartma alanının genel kavramıdır.","focus_only":"Bağlama göre kırk gümüş para veya yedi temel birim değerini taşıyan belirli bir ölçü adıdır.","gloss":"özel ağırlık ölçüsü ile genel tartma","neighbor_only":"Ağırlık, tartı aracı ve bir şeye ağırlığını verme gibi genel ölçme alanını kapsar.","neighbor_ref":"root_000202/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal belirlenmiş ağırlık ve ölçme düşüncesinde buluşur."},{"boundary_match":"partial","distinction":"Ölçülerin adları ve değerleri ayrıdır: bu dal kırk paralık değeri ve yağdaki değişkeyi taşırken komşu dal çoğunlukla beş paralık küçük miktarı bildirir.","focus_only":"Para hesabında kırk gümüş para ağırlığına veya yağda yedi birime bağlanan ölçüdür.","gloss":"kırk paralık ölçü ile beş paralık ölçü","neighbor_only":"Altın veya gümüş için kullanılan, çoğunlukla beş gümüş para ağırlığıyla açıklanan daha küçük ölçüdür.","neighbor_ref":"root_001570/B004","relation_type":"near_neighbor","shared_zone":"İki dal da değerli maden veya para üzerinden açıklanan geleneksel ağırlık ölçüleridir."},{"boundary_match":"partial","distinction":"Bu dalın ölçü adı ve verilen değerleri kendine özgüdür; komşu dal başka birim adını ve ağırlığın yanında hacim kullanımını kapsar.","focus_only":"İki sözcük biçimi ve iki bağlamsal değeri bulunan belirli bir ağırlık ölçüsüdür.","gloss":"iki ayrı geleneksel ölçü adı","neighbor_only":"Başka bir adla anılan, hem ağırlık hem hacim ölçüsü olabilen ayrı bir geleneksel birimdir.","neighbor_ref":"root_001449/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli adları, tekil ve çoğul biçimleri bulunan geleneksel ölçü birimleridir."},{"boundary_match":"partial","distinction":"Bu dal ağırlığa ve belirli değerlere bağlıdır; komşu dal hacim ile para miktarı arasında daha geniş bir ölçüm alanına yayılır.","focus_only":"Öncelikle ağırlık ölçüsüdür ve iki özel sayısal değere bağlanır.","gloss":"ağırlık ölçüsü ile hacim ve miktar ölçüsü","neighbor_only":"Hacim ölçüsünü, yarım başka bir hacim ölçüsünü ve para miktarını birlikte kapsayabilir.","neighbor_ref":"root_001224/B007","relation_type":"near_neighbor","shared_zone":"İki dal da sayılabilir veya ölçülebilir bir miktarı geleneksel birimle belirtir."},{"boundary_match":"field_only","distinction":"Bu dal ölçülen miktarı bildiren birimdir; komşu dal ise ölçü araçlarının ve paraların doğruluğunu belirleyen ayar standardıdır.","focus_only":"Kendi adı, biçimleri ve geleneksel değerleri bulunan ölçü birimini tanımlar.","gloss":"ölçü birimi ile ölçü ayarı","neighbor_only":"Ölçekleri ve paraları denetlemeye yarayan ayarı veya ölçünleme işlemini tanımlar.","neighbor_ref":"root_001066/B013","relation_type":"same_field","shared_zone":"Her iki dal doğru ağırlık ve ölçü değerinin belirlenmesi alanındadır."}],"source_phrase_ar":"الأوقية في الحديث أربعون درهما (sihah;tahdhib)؛ الوقية وزن من أوزان الدهن وهي سبعة مثاقيل (tahdhib)؛ اللغة الجيدة أوقية وجمعها أواقي وأواق (tahdhib)","source_summary":"Toplu kaynak anlatımı, aynı ölçü ailesinde bağlama ve sözcük biçimine göre iki değer aktarır: para hesabında kırk gümüş para ağırlığı ve yağ hesabında yedi temel ağırlık birimi. Başlangıç sesini taşıyan biçim daha düzgün kabul edilir; ölçü adının iki çoğul biçimi de verilir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الأوقية والأواقي بوصفها وزنا معلوما للدراهم أو الدهن","what_is_not_ar":"لا يدخل فيه الوقاية ولا التقوى ولا الواقي بمعنى الصرد"},"support_links":[]},{"boundary":"Dal yalnızca örümcek kuşunun bu iki adına ve adlandırma açıklamasına aittir; koruyan kişi, topallayan at veya yara açmayan eyer anlamlarına geçmez.","branch_kind":"non_bare","branch_ref":"root_001677/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَقْوَى","morph_features":"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:3:2","qac_word_ref":"91:8:3","surface_ar":"تَقْوَىٰ"}],"gloss":"örümcek kuşu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, örümcek kuşunu adlandıran özel bir kuş adıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuş adı, son sesi bulunan daha uzun ve bu sesin düştüğü daha kısa iki biçimde kullanılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adın kuşa verilmesi, yürürken adımlarını fazla açmayan kısa adımlı yürüyüşüyle açıklanır."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kuş türünün Türkçedeki doğal adı olarak dalın adlandırma çekirdeğini doğrudan karşılar.","boundary_detail":"Dal yalnızca örümcek kuşunun bu iki adına ve adlandırma açıklamasına aittir; koruyan kişi, topallayan at veya yara açmayan eyer anlamlarına geçmez.","branch_image_ar":"الواقي اسم للصرد","concept_gloss":"örümcek kuşu","contextual_glosses":[{"applicability":"Kuş adının yürüyüş biçimiyle ilişkilendirilen açıklaması da bağlamda görünür kılınmak istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuş türünü ve adlandırmaya gerekçe gösterilen kısa adımlı yürüyüş özelliğini birlikte korur."},"facet_ids":["F001","F003"],"text":"kısa adımlarla yürüyen örümcek kuşu","usage_role":"explanatory"}],"definition":"Örümcek kuşunun, biri son sesi koruyan diğeri bu sesi düşüren iki biçimde söylenen adı. Adlandırma, kuşun yürürken adımlarını fazla açmamasıyla açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, örümcek kuşunu adlandıran özel bir kuş adıdır."},{"facet_id":"F002","role":"source_variant","statement":"Kuş adı, son sesi bulunan daha uzun ve bu sesin düştüğü daha kısa iki biçimde kullanılır."},{"facet_id":"F003","role":"associated_use","statement":"Adın kuşa verilmesi, yürürken adımlarını fazla açmayan kısa adımlı yürüyüşüyle açıklanır."}],"identity_rationale":"Kaynak ifadesi dalı doğrudan örümcek kuşunun adı olarak verir, adın son sesi bulunan ve düşmüş iki biçimini kaydeder ve adlandırmayı kuşun yürürken adımlarını fazla açmamasına bağlar. Geçici çerçeve bu sınırı doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"örümcek kuşu; aynı kuş adının uzun ve kısalmış biçimleri"}],"lexicalization_note":"Tanım, kuşa verilmiş iki özel ad biçimiyle sınırlı tutulur ve bunlardan genel bir koruma ya da yürüme anlamı türetilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan dört karşılaştırma kuş adları arasındaki tür ayrımını yeterince gösterir. Öteki kuş adayları da yalnızca aynı alanı paylaşır; kurt adı ile koruma, ağırlık ve hayvan yürüyüşü dalları farklı kimliklerdir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortaklık yalnızca kuş adı olmalarıdır; bu dal örümcek kuşunu, komşu dal ise ibibiği adlandırır ve türler birbirinin yerine geçmez.","focus_only":"Örümcek kuşunu ve onun kısa adımlı yürüyüşüne bağlanan adını belirtir.","gloss":"örümcek kuşu ile ibibik","neighbor_only":"İbibik kuşunu ve o kuşa ait ad biçimlerini belirtir.","neighbor_ref":"root_001580/B005","relation_type":"same_field","shared_zone":"Her iki dal belirli bir kuş türünü doğrudan adlandıran sözleri içerir."},{"boundary_match":"field_only","distinction":"Bu dal örümcek kuşunun adıdır; komşu dal tarla kuşunun adıdır. Aynı üst alanda bulunsalar da tür kimlikleri ayrıdır.","focus_only":"Kısa adımlı yürüyüşüyle açıklanan örümcek kuşu adı merkezde yer alır.","gloss":"örümcek kuşu ile tarla kuşu","neighbor_only":"Tarla kuşunu ve ona ait farklı ad biçimlerini belirtir.","neighbor_ref":"root_001195/B003","relation_type":"same_field","shared_zone":"İki dal da küçük kuş türlerine verilmiş adları ve bu adların biçimlerini ele alır."},{"boundary_match":"field_only","distinction":"Anlamsal ortaklık kuş kategorisiyle sınırlıdır; dallar büyüklük, yapı ve tür bakımından bütünüyle farklı kuşları adlandırır.","focus_only":"Örümcek kuşunun özel adını bildirir.","gloss":"örümcek kuşu ile deve kuşu","neighbor_only":"Çok daha büyük ve uçamayan deve kuşunun tür adını bildirir.","neighbor_ref":"root_001525/B006","relation_type":"same_field","shared_zone":"Her iki dal bir kuş türünün doğrudan adı olarak kullanılır."},{"boundary_match":"field_only","distinction":"Bu dalın göndergesi örümcek kuşudur; komşu dal başka bir küçük kuş türünü adlandırır ve ortak kuş alanı tür özdeşliği oluşturmaz.","focus_only":"Örümcek kuşunu adlandırır ve adını kuşun yürüyüşüyle ilişkilendirir.","gloss":"örümcek kuşu ile bir serçe türü","neighbor_only":"Serçelere benzeyen başka bir küçük kuş türünün adını bildirir.","neighbor_ref":"root_000465/B008","relation_type":"same_field","shared_zone":"İki dal da küçük kuşlardan birine verilmiş sözlü adları taşır."}],"source_phrase_ar":"الواقي الصرد (sihah;tahdhib)؛ الواق بكسر القاف بلا ياء (sihah)؛ قيل للصرد واق لأنه لا ينبسط في مشيه (tahdhib)","source_summary":"Kaynakların ortak anlatımı bu sözcüğü örümcek kuşunun adı olarak tanımlar ve son sesi bulunan biçimin yanında o sesin düştüğü kısa biçimi de kaydeder. Adın nedeni, kuşun yürürken adımlarını fazla açmaması olarak açıklanır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الواقي والواق اسما للصرد","what_is_not_ar":"لا يدخل فيه الواقي بمعنى الدافع ولا الفرس الواقي ولا السرج الواقي"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["91:8:1"],"branch_refs":[],"candidate_id":"cand_a36e4fbed80bd1f669ad","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:8:1:bound-pivot-pacing","source_type":"word_analysis","support_ids":["sup_74f634003135fd0b50e6","sup_a7c12d388506ad5ae408"],"title":"bound particle as audible pivot","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:1","qac_refs":["91:8:1:1"],"status":"accepted"}},{"anchor_refs":["91:8:1"],"branch_refs":[],"candidate_id":"cand_074210540913493507c8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:8:1:oath-answer-sequence","source_type":"word_analysis","support_ids":["sup_12c6fc5bf84fcfdd4a44","sup_74f634003135fd0b50e6"],"title":"oath answer and immediate sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:1","qac_refs":["91:8:1:1"],"status":"accepted"}},{"anchor_refs":["91:8:1"],"branch_refs":[],"candidate_id":"cand_8fc91ddcfc7bccea803c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:8:1:whole-clause-scope","source_type":"word_analysis","support_ids":["sup_600b779bcc446e3ce3a2","sup_74f634003135fd0b50e6"],"title":"scope over one inspired pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:1","qac_refs":["91:8:1:1"],"status":"accepted"}},{"anchor_refs":["91:8:2"],"branch_refs":[],"candidate_id":"cand_768e35cd4fc25a18ee8d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001381"],"scope":"focus_ayah","source_local_id":"91:8:2:completed-causative-frame","source_type":"word_analysis","support_ids":["sup_f03c923d4f43fa957ed7","sup_fe87792f18fd61175fd7"],"title":"completed causative inspiration frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:2","qac_refs":["91:8:1:2","91:8:1:3"],"status":"accepted"}},{"anchor_refs":["91:8:2"],"branch_refs":[],"candidate_id":"cand_c24b0f1df6ef6adfb09b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001381"],"scope":"focus_ayah","source_local_id":"91:8:2:formation-to-cultivation-bridge","source_type":"word_analysis","support_ids":["sup_fa3688f3ef22600558e8","sup_fe87792f18fd61175fd7"],"title":"formation becomes moral internalization","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:2","qac_refs":["91:8:1:2","91:8:1:3"],"status":"accepted"}},{"anchor_refs":["91:8:2"],"branch_refs":[],"candidate_id":"cand_68eb40c0429d38ce492e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001381"],"scope":"focus_ayah","source_local_id":"91:8:2:internalization-pressure","source_type":"word_analysis","support_ids":["sup_420ae1f4c7301425f9ba","sup_fe87792f18fd61175fd7"],"title":"swallowing image as inward uptake","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:2","qac_refs":["91:8:1:2","91:8:1:3"],"status":"accepted"}},{"anchor_refs":["91:8:2"],"branch_refs":[],"candidate_id":"cand_79dba36c19b203f60a15","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001381"],"scope":"focus_ayah","source_local_id":"91:8:2:rare-ilham-channel","source_type":"word_analysis","support_ids":["sup_b8515bcf6972cd075ba9","sup_fe87792f18fd61175fd7"],"title":"rare inward inspiration channel","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:2","qac_refs":["91:8:1:2","91:8:1:3"],"status":"accepted"}},{"anchor_refs":["91:8:2"],"branch_refs":[],"candidate_id":"cand_b0e70179bb45b49151ff","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001381"],"scope":"focus_ayah","source_local_id":"91:8:2:recipient-suffix-chain","source_type":"word_analysis","support_ids":["sup_46613efd0b697ade9bb4","sup_fe87792f18fd61175fd7"],"title":"recipient suffix begins self-reference","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:2","qac_refs":["91:8:1:2","91:8:1:3"],"status":"accepted"}},{"anchor_refs":["91:8:2"],"branch_refs":[],"candidate_id":"cand_45b0b0ca6ebbb70dea3c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001381"],"scope":"focus_ayah","source_local_id":"91:8:2:sound-internalization","source_type":"word_analysis","support_ids":["sup_ed264f771c25989bbadb","sup_fe87792f18fd61175fd7"],"title":"contained sound texture","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:2","qac_refs":["91:8:1:2","91:8:1:3"],"status":"accepted"}},{"anchor_refs":["91:8:3"],"branch_refs":[],"candidate_id":"cand_3d9f9f4a2461adf7b7be","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"91:8:3:abstract-capacity-not-event","source_type":"word_analysis","support_ids":["sup_8e5b7a481b9d696be8c4","sup_d077a1a22d6caf75e0dd"],"title":"maṣdar names breach-capacity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:3","qac_refs":["91:8:2:1","91:8:2:2"],"status":"accepted"}},{"anchor_refs":["91:8:3"],"branch_refs":[],"candidate_id":"cand_e6e8e4dd02d3a19aea09","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"91:8:3:corpus-actualization","source_type":"word_analysis","support_ids":["sup_02f294100dbde78a5ff3","sup_8e5b7a481b9d696be8c4"],"title":"later actualized breach field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:3","qac_refs":["91:8:2:1","91:8:2:2"],"status":"accepted"}},{"anchor_refs":["91:8:3"],"branch_refs":[],"candidate_id":"cand_6c9d336a60149dc22356","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"91:8:3:paired-moral-pole","source_type":"word_analysis","support_ids":["sup_4cd5287862ab45d21931","sup_8e5b7a481b9d696be8c4"],"title":"first pole of moral merism","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:3","qac_refs":["91:8:2:1","91:8:2:2"],"status":"accepted"}},{"anchor_refs":["91:8:3"],"branch_refs":[],"candidate_id":"cand_51f5c9ee995068b12408","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"91:8:3:possessed-content-object","source_type":"word_analysis","support_ids":["sup_36f3bb2d4048427f8f33","sup_8e5b7a481b9d696be8c4"],"title":"possessed breach as inspired content","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:3","qac_refs":["91:8:2:1","91:8:2:2"],"status":"accepted"}},{"anchor_refs":["91:8:3"],"branch_refs":[],"candidate_id":"cand_824f04939ceb4040ac7e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"91:8:3:rupture-image","source_type":"word_analysis","support_ids":["sup_464c2aba99634c96a7ec","sup_8e5b7a481b9d696be8c4"],"title":"rupture image under moral breach","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:3","qac_refs":["91:8:2:1","91:8:2:2"],"status":"accepted"}},{"anchor_refs":["91:8:3"],"branch_refs":[],"candidate_id":"cand_122e58d9b3562cc19b4b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"91:8:3:sound-and-cadence","source_type":"word_analysis","support_ids":["sup_8e5b7a481b9d696be8c4","sup_d69232446ff972d07fa6"],"title":"breach sound beside shared suffix","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:3","qac_refs":["91:8:2:1","91:8:2:2"],"status":"accepted"}},{"anchor_refs":["91:8:4"],"branch_refs":[],"candidate_id":"cand_2b144c32ba042abae858","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:8:4:affixal-rhythm-and-particle-frame","source_type":"word_analysis","support_ids":["sup_3e48aa15b34318f5cb3d","sup_9daec33be032fbc3738b"],"title":"joined surface and particle control","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:4","qac_refs":["91:8:3:1"],"status":"accepted"}},{"anchor_refs":["91:8:4"],"branch_refs":[],"candidate_id":"cand_a7316a95129e0f72d11f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:8:4:coequal-coordination","source_type":"word_analysis","support_ids":["sup_9daec33be032fbc3738b","sup_f2fd3830ece689267260"],"title":"co-equal moral objects","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:4","qac_refs":["91:8:3:1"],"status":"accepted"}},{"anchor_refs":["91:8:4"],"branch_refs":[],"candidate_id":"cand_5d4056d018d5a669495a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:8:4:moral-merism","source_type":"word_analysis","support_ids":["sup_5fd5e8206d86b8c5cc15","sup_9daec33be032fbc3738b"],"title":"binary merism mechanism","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:4","qac_refs":["91:8:3:1"],"status":"accepted"}},{"anchor_refs":["91:8:5"],"branch_refs":[],"candidate_id":"cand_0cb4eeda74676879f87d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"91:8:5:abstract-noun-not-command","source_type":"word_analysis","support_ids":["sup_4f49e8eda8e5b2a6677d","sup_bab949b099fd9c2d242f"],"title":"capacity rather than command or label","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:5","qac_refs":["91:8:3:2","91:8:3:3"],"status":"accepted"}},{"anchor_refs":["91:8:5"],"branch_refs":[],"candidate_id":"cand_7474dc60264b1b40bfad","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"91:8:5:closure-and-nearby-enactment","source_type":"word_analysis","support_ids":["sup_30fb120c6a9a73aa1643","sup_4f49e8eda8e5b2a6677d"],"title":"closing pole before enactment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:5","qac_refs":["91:8:3:2","91:8:3:3"],"status":"accepted"}},{"anchor_refs":["91:8:5"],"branch_refs":[],"candidate_id":"cand_676ff27a53eb4d7b761b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"91:8:5:cosmic-oath-resonance","source_type":"word_analysis","support_ids":["sup_4f49e8eda8e5b2a6677d","sup_feaeddf01934aed8cd5f"],"title":"oath-field resonance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:5","qac_refs":["91:8:3:2","91:8:3:3"],"status":"accepted"}},{"anchor_refs":["91:8:5"],"branch_refs":[],"candidate_id":"cand_4b9368a4e32dd2106932","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"91:8:5:major-corpus-concept","source_type":"word_analysis","support_ids":["sup_4f49e8eda8e5b2a6677d","sup_8f95c1e6e123cfadf88d"],"title":"pervasive taqwā concept internalized","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:5","qac_refs":["91:8:3:2","91:8:3:3"],"status":"accepted"}},{"anchor_refs":["91:8:5"],"branch_refs":[],"candidate_id":"cand_db5e74918e3bf61989f9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"91:8:5:possessed-final-content","source_type":"word_analysis","support_ids":["sup_4f49e8eda8e5b2a6677d","sup_b2f8456860379951eda6"],"title":"possessed guarding as final content","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:5","qac_refs":["91:8:3:2","91:8:3:3"],"status":"accepted"}},{"anchor_refs":["91:8:5"],"branch_refs":[],"candidate_id":"cand_49f7fd7b6262942b0d87","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"91:8:5:protective-self-guarding","source_type":"word_analysis","support_ids":["sup_45b77ebaadc8fc1a69ed","sup_4f49e8eda8e5b2a6677d"],"title":"protective self-guarding image","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:5","qac_refs":["91:8:3:2","91:8:3:3"],"status":"accepted"}},{"anchor_refs":["91:8:5"],"branch_refs":[],"candidate_id":"cand_7ddfa1ca8fddee1861e9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"91:8:5:sound-and-final-cadence","source_type":"word_analysis","support_ids":["sup_4f49e8eda8e5b2a6677d","sup_523bf5c6b58b1deb06da"],"title":"contained final cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:8:5","qac_refs":["91:8:3:2","91:8:3:3"],"status":"accepted"}},{"anchor_refs":["91:8:1"],"branch_refs":[],"candidate_id":"cand_b4051fcfe6c3bd0db0eb","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001381"],"scope":"focus_ayah","source_local_id":"91:8:1:2","source_type":"qac_morpheme","support_ids":["sup_29397e8c366118deca34"],"title":"QAC root occurrence: ل ه م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:8:2"],"branch_refs":[],"candidate_id":"cand_09087b4b97c23e66b7b5","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"91:8:2:1","source_type":"qac_morpheme","support_ids":["sup_907477ec34200a1efbff"],"title":"QAC root occurrence: ف ج ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:8:3"],"branch_refs":[],"candidate_id":"cand_d04d674121ded7760205","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"91:8:3:2","source_type":"qac_morpheme","support_ids":["sup_0d4990196d2cf37043fc"],"title":"QAC root occurrence: و ق ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:8","branch_refs":["root_001132/B004","root_001381/B001","root_001677/B002"],"candidate_id":"cand_daba8183049900fc31ab","commentary_obligation":"review","hft_ref":"hft_4f43b5f776f3858cda29","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_inward_assimilation","source_type":"hft","support_ids":["sup_18176688d1b7ccdf56c6"],"title":"baseline_inward_assimilation","trust":"legacy_unbound"},{"anchor_refs":["91:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:8","branch_refs":["root_001132/B001","root_001381/B004","root_001677/B001"],"candidate_id":"cand_112d51b7c16ffada0528","commentary_obligation":"review","hft_ref":"hft_f9bf17b53d33fa5e0bc0","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_threshold_pair","source_type":"hft","support_ids":["sup_d4164de075e7caa1b4b6"],"title":"baseline_threshold_pair","trust":"legacy_unbound"},{"anchor_refs":["91:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:8","branch_refs":["root_001132/B003","root_001381/B005","root_001677/B001"],"candidate_id":"cand_2e321606e0614a7f1ce4","commentary_obligation":"review","hft_ref":"hft_daa782fe09aa3e2f752a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_asymmetric_hazard","source_type":"hft","support_ids":["sup_b110be56511440060846"],"title":"baseline_asymmetric_hazard","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:8:1:1","qac_word_ref":"91:8:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أَلْهَمَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>alohama|ROOT:lhm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:8:1:2","qac_word_ref":"91:8:1","root_ar":"ل ه م","surface_ar":"أَلْهَمَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:8:1:3","qac_word_ref":"91:8:1","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"فُجُور","morph_features":"STEM|POS:N|LEM:fujuwr|ROOT:fjr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:2:1","qac_word_ref":"91:8:2","root_ar":"ف ج ر","surface_ar":"فُجُورَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:8:2:2","qac_word_ref":"91:8:2","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:8:3:1","qac_word_ref":"91:8:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"تَقْوَى","morph_features":"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:3:2","qac_word_ref":"91:8:3","root_ar":"و ق ي","surface_ar":"تَقْوَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:8:3:3","qac_word_ref":"91:8:3","root_ar":"","surface_ar":"هَا"}],"word_analysis_qac_refs":[["91:8:1:1"],["91:8:1:2","91:8:1:3"],["91:8:2:1","91:8:2:2"],["91:8:3:1"],["91:8:3:2","91:8:3:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["91:8:1","91:8:2","91:8:3","91:8:4","91:8:5"]},"focus_surface_evidence":{"arabic_uthmani":"فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:8:1:1","qac_word_ref":"91:8:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أَلْهَمَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>alohama|ROOT:lhm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:8:1:2","qac_word_ref":"91:8:1","root_ar":"ل ه م","surface_ar":"أَلْهَمَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:8:1:3","qac_word_ref":"91:8:1","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"فُجُور","morph_features":"STEM|POS:N|LEM:fujuwr|ROOT:fjr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:2:1","qac_word_ref":"91:8:2","root_ar":"ف ج ر","surface_ar":"فُجُورَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:8:2:2","qac_word_ref":"91:8:2","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:8:3:1","qac_word_ref":"91:8:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"تَقْوَى","morph_features":"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:8:3:2","qac_word_ref":"91:8:3","root_ar":"و ق ي","surface_ar":"تَقْوَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:8:3:3","qac_word_ref":"91:8:3","root_ar":"","surface_ar":"هَا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["91:8:1:1"],["91:8:1:2","91:8:1:3"],["91:8:2:1","91:8:2:2"],["91:8:3:1"],["91:8:3:2","91:8:3:3"]],"word_analysis_refs":["91:8:1","91:8:2","91:8:3","91:8:4","91:8:5"],"word_rows":[{"analysis_record_ref":"91:8:1","analytic_gloss_range_en":"resultative and sequential clause-linking particle that turns the oath sequence toward the completed inspiration statement","analytic_root_gloss_range_en":null,"qac_refs":["91:8:1:1"],"root":{"note":"(no root)"},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"91:8:2","analytic_gloss_range_en":"completed causative inward inspiration directed to the soul, with a recipient suffix and coordinated moral content objects","analytic_root_gloss_range_en":"root range includes swallowing or taking in, casting something into the inner mind, engulfing movement, abundance, and consuming calamity; the local Form IV verb selects caused inward inspiration while preserving internalization pressure","qac_refs":["91:8:1:2","91:8:1:3"],"root":{"arabic":"ل ه م","transliteration":"l-h-m"},"surface":{"arabic":"أَلْهَمَهَا","transliteration":"alhamahā"}},{"analysis_record_ref":"91:8:3","analytic_gloss_range_en":"the soul's possessed abstract capacity for moral breach, named as the first inspired content object and paired with guarding","analytic_root_gloss_range_en":"root range includes splitting, bursting out, dawn breaking, sudden irruption, breach of restraint, generosity, and named violated sanctity; the local noun selects moral breach while preserving rupture imagery","qac_refs":["91:8:2:1","91:8:2:2"],"root":{"arabic":"ف ج ر","transliteration":"f-j-r"},"surface":{"arabic":"فُجُورَهَا","transliteration":"fujūrahā"}},{"analysis_record_ref":"91:8:4","analytic_gloss_range_en":"coordinating conjunction that joins the two possessed moral nouns as co-equal content objects, not alternates or sequence steps","analytic_root_gloss_range_en":null,"qac_refs":["91:8:3:1"],"root":{"note":"(no root)"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"91:8:5","analytic_gloss_range_en":"the soul's possessed abstract guarding or protective moral awareness, named as the second co-equal inspired content object","analytic_root_gloss_range_en":"root range includes protection by barrier, self-protective caution, guarded gait, a measure-name, and a bird-name; the local noun selects moral self-guarding and protective awareness","qac_refs":["91:8:3:2","91:8:3:3"],"root":{"arabic":"و ق ي","transliteration":"w-q-y"},"surface":{"arabic":"تَقْوَىٰهَا","transliteration":"taqwāhā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["91:8"],"branch_refs":["root_001132/B004","root_001381/B001","root_001677/B002"],"candidate_id":"cand_daba8183049900fc31ab","evidence_scope":"focus_ayah","hft_ref":"hft_4f43b5f776f3858cda29","item_id":"baseline_inward_assimilation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_inward_assimilation","support_id":"sup_18176688d1b7ccdf56c6"},{"anchor_refs":["91:8"],"branch_refs":["root_001132/B001","root_001381/B004","root_001677/B001"],"candidate_id":"cand_112d51b7c16ffada0528","evidence_scope":"focus_ayah","hft_ref":"hft_f9bf17b53d33fa5e0bc0","item_id":"baseline_threshold_pair","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_threshold_pair","support_id":"sup_d4164de075e7caa1b4b6"},{"anchor_refs":["91:8"],"branch_refs":["root_001132/B003","root_001381/B005","root_001677/B001"],"candidate_id":"cand_2e321606e0614a7f1ce4","evidence_scope":"focus_ayah","hft_ref":"hft_daa782fe09aa3e2f752a","item_id":"baseline_asymmetric_hazard","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_asymmetric_hazard","support_id":"sup_b110be56511440060846"}],"diagnostics":[],"lane_counts":{"global":9,"macro":13,"micro":3},"packet_summary":{"ayah_count":15,"focus_ref":"91:8","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ت ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000186","furuq_root_norm":"ت ل و","furuq_source_root_norm":"ت ل و","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000185","furuq_root_norm":"ت ل ل","furuq_source_root_norm":"ت ل ل","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"91:8","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"91:8","lane":"micro","linguistic_source_ref":"91:8","surface_ref":"91:8","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"91:8","target_tokens":[["Sonra",["91:8:1"]],["ona",["91:8:1"]],["kötülüğünü",["91:8:2"]],["ve",["91:8:3"]],["sakınmasını",["91:8:3"]],["ilham",["91:8:1"]],["edene",["91:8:1"]]],"text":"Sonra ona kötülüğünü ve sakınmasını ilham edene,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":15,"id":"s091-p01-001-015","label":"Whole surah","number":1,"refs":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:3:corpus-actualization","source_type":"word_analysis","support_id":"sup_02f294100dbde78a5ff3","text":"{\"blocking_evidence\":null,\"headline\":\"later actualized breach field\",\"reader_payoff\":\"The reader notices that the soul's known breach-capacity in 91:8 stands before later depictions of wicked actors, continuing desire, and the buried soul (82:14; 75:5; 91:10).\",\"reason\":\"The CRITICAL rows give concrete references for related moral uses and a same-surah outcome, and none conflicts with the local noun-as-inspired-content frame.\",\"representative_source_ids\":[\"QI-37d482c4\",\"MI-322d53ee\",\"MI-3e2b3ec3\",\"QB-7cbb707d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:8:3:2","source_type":"qac_morpheme","support_id":"sup_0d4990196d2cf37043fc","text":"{\"lemma_ar\":\"تَقْوَى\",\"morph_features\":\"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"91:8:3:2\",\"qac_word_ref\":\"91:8:3\",\"root_ar\":\"و ق ي\",\"surface_ar\":\"تَقْوَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:1:oath-answer-sequence","source_type":"word_analysis","support_id":"sup_12c6fc5bf84fcfdd4a44","text":"{\"blocking_evidence\":null,\"headline\":\"oath answer and immediate sequence\",\"reader_payoff\":\"The reader notices that 91:8 is both the answer to the oath sequence of 91:1-7 and the next movement after the soul's proportioning in 91:7.\",\"reason\":\"The particle is tagged as resultative or sequential, and the clause evidence shows one verbal statement beginning after the oath sequence, so the CRITICAL claim about oath resolution plus immediate continuation is locally licensed.\",\"representative_source_ids\":[\"QG-cc8ad4ec\",\"QS-20d6674d\",\"QI-e01e668b\",\"QY-6eca21ef\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:8:1:2","source_type":"qac_morpheme","support_id":"sup_29397e8c366118deca34","text":"{\"lemma_ar\":\"أَلْهَمَ\",\"morph_features\":\"STEM|POS:V|PERF|(IV)|LEM:>alohama|ROOT:lhm|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"91:8:1:2\",\"qac_word_ref\":\"91:8:1\",\"root_ar\":\"ل ه م\",\"surface_ar\":\"أَلْهَمَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:5:closure-and-nearby-enactment","source_type":"word_analysis","support_id":"sup_30fb120c6a9a73aa1643","text":"{\"blocking_evidence\":null,\"headline\":\"closing pole before enactment\",\"reader_payoff\":\"The reader notices that the ayah closes on guarding capacity before that capacity is cultivated or enacted in nearby movement (91:9; 92:5).\",\"reason\":\"Final word position, suffix continuity, and the cited nearby references support an arc from known guarding capacity in 91:8 to purification and enacted guarding (91:9; 92:5).\",\"representative_source_ids\":[\"QT-f864bddf\",\"MT-3692a93d\",\"QE-2e31a2e1\",\"QB-21164ffe\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:3:possessed-content-object","source_type":"word_analysis","support_id":"sup_36f3bb2d4048427f8f33","text":"{\"blocking_evidence\":null,\"headline\":\"possessed breach as inspired content\",\"reader_payoff\":\"The reader notices that the soul is made to know its own breach-capacity, not an abstract moral label detached from the soul.\",\"reason\":\"Attachment evidence marks the noun as explicit inspired content and its suffix as possessive, while cross-reference evidence ties the suffix to the soul in 91:7.\",\"representative_source_ids\":[\"QG-0688741b\",\"QG-b1d68b1c\",\"QG-f3b38db7\",\"MS-45848492\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:4:affixal-rhythm-and-particle-frame","source_type":"word_analysis","support_id":"sup_3e48aa15b34318f5cb3d","text":"{\"blocking_evidence\":null,\"headline\":\"joined surface and particle control\",\"reader_payoff\":\"The reader notices how the medial conjunction attaches to the second noun and helps organize the ayah's rhythm, while that sound effect remains secondary to coordination.\",\"reason\":\"The surface fusion and two-particle frame are visible, but the topic is narrowed to form and pacing so it does not overstate a separate semantic value beyond coordination.\",\"representative_source_ids\":[\"QF-62f357d8\",\"QE-da9dd621\",\"QP-33ae95e5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:2:internalization-pressure","source_type":"word_analysis","support_id":"sup_420ae1f4c7301425f9ba","text":"{\"blocking_evidence\":null,\"headline\":\"swallowing image as inward uptake\",\"reader_payoff\":\"The reader notices that inspiration is pictured as deep inward uptake, while the local Form IV prevents turning that image into appetite, self-engulfing, or an independent swallowing event.\",\"reason\":\"V4 supports both swallowing and inner-prompting branches for the root, but the local surface is Form IV inspiration, so the physical image survives as internalization pressure rather than replacing the selected sense.\",\"representative_source_ids\":[\"QS-7e085d6f\",\"QS-9902fd98\",\"MS-c0c28d79\",\"QF-80a9f7f9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:5:protective-self-guarding","source_type":"word_analysis","support_id":"sup_45b77ebaadc8fc1a69ed","text":"{\"blocking_evidence\":null,\"headline\":\"protective self-guarding image\",\"reader_payoff\":\"The reader notices taqwā as protective moral awareness and self-guarding, while unrelated root branches such as measure-name or bird-name stay outside the local sense.\",\"reason\":\"V4 supports protection and self-protective caution as relevant branches for this lexical field, while the local abstract noun and moral pair exclude unrelated branches from activation.\",\"representative_source_ids\":[\"QS-19f510b4\",\"QS-93c36640\",\"QF-f6b64ffa\",\"QY-beab60c9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:3:rupture-image","source_type":"word_analysis","support_id":"sup_464c2aba99634c96a7ec","text":"{\"blocking_evidence\":null,\"headline\":\"rupture image under moral breach\",\"reader_payoff\":\"The reader notices moral wrong as a breach or rupture of containment, while dawn, water-bursting, and other branches do not replace the selected moral sense.\",\"reason\":\"V4 separates physical bursting, dawn-breaking, and moral breach branches; the local abstract moral noun selects breach of restraint, with rupture imagery retained as lexical pressure.\",\"representative_source_ids\":[\"QS-2115731f\",\"QS-a05354de\",\"QS-a122179e\",\"QI-5190a1af\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:2:recipient-suffix-chain","source_type":"word_analysis","support_id":"sup_46613efd0b697ade9bb4","text":"{\"blocking_evidence\":null,\"headline\":\"recipient suffix begins self-reference\",\"reader_payoff\":\"The reader notices that the same soul from 91:7 is first the recipient of inspiration and then the possessor of both moral capacities.\",\"reason\":\"Cross-reference evidence resolves the feminine object suffix to the preceding soul in 91:7, and the later possessed nouns repeat that same suffix pattern.\",\"representative_source_ids\":[\"QG-d0faf15f\",\"QE-a5850b45\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:3:paired-moral-pole","source_type":"word_analysis","support_id":"sup_4cd5287862ab45d21931","text":"{\"blocking_evidence\":null,\"headline\":\"first pole of moral merism\",\"reader_payoff\":\"The reader notices that breach and guarding are grammatically parallel poles of one inspired moral spectrum.\",\"reason\":\"Local coordination makes the two possessed nouns co-equal objects under one verb, supporting the merism without subordinating either pole.\",\"representative_source_ids\":[\"QS-6f079a76\",\"QE-370a4411\",\"ME-5a140b2d\",\"QY-26b3b0ff\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:5","source_type":"word_analysis","support_id":"sup_4f49e8eda8e5b2a6677d","text":"{\"gloss_range\":\"the soul's possessed abstract guarding or protective moral awareness, named as the second co-equal inspired content object\",\"prose\":\"{{ar:تَقْوَىٰهَا}} ({{tr:taqwāhā}}) closes the inspired pair with the soul's own guarding capacity. The suffix keeps the soul from 91:7 as the referential center, and the coordination makes this word the second content object under the same act of inspiration, not a later achievement. The root's protection and barrier field makes taqwā more concrete than a flat label for piety: it is protective moral awareness, a self-guarding posture placed opposite the breach image of {{ar:فُجُورَهَا}} ({{tr:fujūrahā}}). Because the surface is a possessed abstract noun, the ayah is not yet commanding the soul with imperative guarding forms or labeling it as already pious; it describes a capacity made known within it. Against the cosmic oath frame of 91:1-7, the soul's own guarding capacity answers the larger order without making taqwā itself a cosmic-function term. The final position lets guarding have the ayah's closing sound, while later and nearby references show the capacity becoming decisive in provision, honor, enacted guarding, and purification (2:197; 49:13; 92:5; 91:9).\",\"root_display\":\"{{ar:و ق ي}} ({{tr:w-q-y}})\",\"root_gloss_range\":\"root range includes protection by barrier, self-protective caution, guarded gait, a measure-name, and a bird-name; the local noun selects moral self-guarding and protective awareness\",\"surface_display\":\"{{ar:تَقْوَىٰهَا}} ({{tr:taqwāhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:5:sound-and-final-cadence","source_type":"word_analysis","support_id":"sup_523bf5c6b58b1deb06da","text":"{\"blocking_evidence\":null,\"headline\":\"contained final cadence\",\"reader_payoff\":\"The reader notices that the final word mirrors the earlier suffix cadence while its internal sound suits the guarding pole, with sound kept secondary to grammar and root evidence.\",\"reason\":\"The repeated suffix is grammatically visible, and the sound observation is retained only as cadence that reinforces, rather than proves, the protective meaning.\",\"representative_source_ids\":[\"QP-7bb9067f\",\"QP-ddbc6c8f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:4:moral-merism","source_type":"word_analysis","support_id":"sup_5fd5e8206d86b8c5cc15","text":"{\"blocking_evidence\":null,\"headline\":\"binary merism mechanism\",\"reader_payoff\":\"The reader notices that the conjunction makes two opposed capacities express the soul's full moral spectrum rather than a loose list.\",\"reason\":\"The two morally opposed possessed nouns are coordinated as one content pair, so the merism claim is supported by local syntax rather than only by thematic inference.\",\"representative_source_ids\":[\"QS-6ffe359a\",\"QS-f7f26824\",\"QT-7de7ff31\",\"MT-7d1edd96\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:1:whole-clause-scope","source_type":"word_analysis","support_id":"sup_600b779bcc446e3ce3a2","text":"{\"blocking_evidence\":null,\"headline\":\"scope over one inspired pair\",\"reader_payoff\":\"The reader notices that the particle introduces one complete disclosure whose verb governs both moral objects together.\",\"reason\":\"Attachment evidence marks a single verbal clause from word 1 through word 5, with the explicit content object spanning the coordinated pair.\",\"representative_source_ids\":[\"QT-1b6575eb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:1","source_type":"word_analysis","support_id":"sup_74f634003135fd0b50e6","text":"{\"gloss_range\":\"resultative and sequential clause-linking particle that turns the oath sequence toward the completed inspiration statement\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) is the hinge that makes 91:8 answer and continue the oath sequence of 91:1-7. It is not a loose sentence opener: it carries the movement from the sworn, proportioned soul (91:7) into the completed act of inspiration. Because the following verb governs both moral contents, the particle frames the whole ayah as one consequent disclosure, not two separate installations. Its one-letter surface also matters at the level of pacing: it is split analytically but recited into {{ar:أَلْهَمَهَا}} ({{tr:alhamahā}}), so the transition is heard as attached to the inspiration event itself.\",\"root_display\":\"(no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:3","source_type":"word_analysis","support_id":"sup_8e5b7a481b9d696be8c4","text":"{\"gloss_range\":\"the soul's possessed abstract capacity for moral breach, named as the first inspired content object and paired with guarding\",\"prose\":\"{{ar:فُجُورَهَا}} ({{tr:fujūrahā}}) is the first explicit content object of {{ar:أَلْهَمَهَا}} ({{tr:alhamahā}}): the soul is made to know its own breach-capacity. The attached suffix makes the noun definite by relation to the soul from 91:7, so this is not wickedness floating as a general category. As a maṣdar, it names a category or capacity of boundary-breaking rather than one isolated sin-event or a label for an evildoer. The root's splitting, gushing, and dawn-breaking field gives the moral term a rupture image, like pressure breaking containment, while the local noun keeps that image in the moral breach branch. Paired with {{ar:تَقْوَىٰهَا}} ({{tr:taqwāhā}}), it forms one pole of the soul's moral spectrum, and the same field is later actualized in wicked persons or continuing desire (82:14; 75:5) and in the negative outcome of 91:10. Its cadence also shares the final hā with the guarding term while its internal ū-r flow sounds more released, so the paired suffix does not erase the contrast between breach and guarding.\",\"root_display\":\"{{ar:ف ج ر}} ({{tr:f-j-r}})\",\"root_gloss_range\":\"root range includes splitting, bursting out, dawn breaking, sudden irruption, breach of restraint, generosity, and named violated sanctity; the local noun selects moral breach while preserving rupture imagery\",\"surface_display\":\"{{ar:فُجُورَهَا}} ({{tr:fujūrahā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:5:major-corpus-concept","source_type":"word_analysis","support_id":"sup_8f95c1e6e123cfadf88d","text":"{\"blocking_evidence\":null,\"headline\":\"pervasive taqwā concept internalized\",\"reader_payoff\":\"The reader notices that a major Quranic moral differentiator appears here as an innate soul-linked capacity before later evaluations such as provision and honor (2:197; 49:13).\",\"reason\":\"The contextual profile shows this root as common in the corpus, while the local clause uniquely places the concept inside the rare inward-inspiration frame.\",\"representative_source_ids\":[\"MS-94fad453\",\"QI-751e581e\",\"QI-ba99eeb3\",\"MI-c362229e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:8:2:1","source_type":"qac_morpheme","support_id":"sup_907477ec34200a1efbff","text":"{\"lemma_ar\":\"فُجُور\",\"morph_features\":\"STEM|POS:N|LEM:fujuwr|ROOT:fjr|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"91:8:2:1\",\"qac_word_ref\":\"91:8:2\",\"root_ar\":\"ف ج ر\",\"surface_ar\":\"فُجُورَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:4","source_type":"word_analysis","support_id":"sup_9daec33be032fbc3738b","text":"{\"gloss_range\":\"coordinating conjunction that joins the two possessed moral nouns as co-equal content objects, not alternates or sequence steps\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) is small but structurally decisive. It coordinates {{ar:تَقْوَىٰهَا}} ({{tr:taqwāhā}}) with {{ar:فُجُورَهَا}} ({{tr:fujūrahā}}) as the same kind of content under {{ar:أَلْهَمَهَا}} ({{tr:alhamahā}}). That blocks an either-or reading, an appositional replacement, or a sequence in which one moral pole arrives later than the other. The conjunction is therefore the surface mechanism that turns breach and guarding into a co-present moral merism. At the level of form and pacing, it is fused to the second noun and gives the listener a short reset before the final pole, while the opening particle and this medial conjunction divide the ayah's organization between clause-linking and object-linking.\",\"root_display\":\"(no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:1:bound-pivot-pacing","source_type":"word_analysis","support_id":"sup_a7c12d388506ad5ae408","text":"{\"blocking_evidence\":null,\"headline\":\"bound particle as audible pivot\",\"reader_payoff\":\"The reader notices the sharp audible turn from the oath register into the finite verb without treating sound as independent proof of meaning.\",\"reason\":\"The written analysis separates the particle, while the surface phrase binds it to the following perfect verb; the sound observation is kept as pacing and register shift, not a separate lexical sense.\",\"representative_source_ids\":[\"QF-acd30cf2\",\"QT-c164aa35\",\"QP-aa09ef4a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:5:possessed-final-content","source_type":"word_analysis","support_id":"sup_b2f8456860379951eda6","text":"{\"blocking_evidence\":null,\"headline\":\"possessed guarding as final content\",\"reader_payoff\":\"The reader notices that the ayah ends with the soul's own guarding capacity, bound by suffix to the same referent that received inspiration.\",\"reason\":\"Attachment evidence marks the noun as conjoined inspired content with a possessive suffix, and cross-reference evidence ties that suffix to the soul from 91:7.\",\"representative_source_ids\":[\"QG-0d6fb658\",\"QG-134e7e24\",\"QG-949938d3\",\"QY-fc9b5675\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:2:rare-ilham-channel","source_type":"word_analysis","support_id":"sup_b8515bcf6972cd075ba9","text":"{\"blocking_evidence\":null,\"headline\":\"rare inward inspiration channel\",\"reader_payoff\":\"The reader notices that the ayah uses a rare inward-inspiration channel for universal moral awareness rather than ordinary prophetic revelation vocabulary.\",\"reason\":\"The contextual profile marks the exact Form IV occurrence as unique in this dataset, and the CRITICAL contrast with revelation vocabulary is coherent with the local inward-recipient frame.\",\"representative_source_ids\":[\"QS-a631b15c\",\"QI-3f4986d3\",\"QH-65a4f48b\",\"MH-30679ad1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:5:abstract-noun-not-command","source_type":"word_analysis","support_id":"sup_bab949b099fd9c2d242f","text":"{\"blocking_evidence\":null,\"headline\":\"capacity rather than command or label\",\"reader_payoff\":\"The reader notices that the ayah describes an already-known guarding capacity rather than issuing an imperative or labeling the soul as already pious.\",\"reason\":\"The local form is a possessed abstract noun, and the distributional profile allows contrast with common command-heavy uses without converting those forms into the local parse.\",\"representative_source_ids\":[\"QF-53eb5e29\",\"QF-75daa6a6\",\"QF-934c24ae\",\"QI-d0eaad74\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:3:abstract-capacity-not-event","source_type":"word_analysis","support_id":"sup_d077a1a22d6caf75e0dd","text":"{\"blocking_evidence\":null,\"headline\":\"maṣdar names breach-capacity\",\"reader_payoff\":\"The reader notices that the inspired content is a structural moral capacity, not one narrated act or a person-label.\",\"reason\":\"The local form is a verbal noun functioning as object content; related eventive and active-participle uses remain contrasts rather than the local parse.\",\"representative_source_ids\":[\"MG-cb71a880\",\"QF-80f5a9c3\",\"QF-89a5c149\",\"QF-8fb13e78\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:3:sound-and-cadence","source_type":"word_analysis","support_id":"sup_d69232446ff972d07fa6","text":"{\"blocking_evidence\":null,\"headline\":\"breach sound beside shared suffix\",\"reader_payoff\":\"The reader notices that the word shares the suffix cadence with the guarding term while its internal sound keeps the breach pole distinct.\",\"reason\":\"The repeated suffix is morphologically grounded, while the sound contrast is kept as secondary cadence rather than semantic proof.\",\"representative_source_ids\":[\"QP-2972c59e\",\"QP-45e1cc70\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:2:sound-internalization","source_type":"word_analysis","support_id":"sup_ed264f771c25989bbadb","text":"{\"blocking_evidence\":null,\"headline\":\"contained sound texture\",\"reader_payoff\":\"The reader notices that the word's compact sound can reinforce the inward-taking feel, but only as surface texture beside the grammar and root evidence.\",\"reason\":\"The phonetic rows align with the internalization image, but sound is treated as a secondary surface effect rather than primary proof of meaning.\",\"representative_source_ids\":[\"QP-b3afd0b7\",\"QP-b4d4bc85\",\"MP-6e24f368\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:2:completed-causative-frame","source_type":"word_analysis","support_id":"sup_f03c923d4f43fa957ed7","text":"{\"blocking_evidence\":null,\"headline\":\"completed causative inspiration frame\",\"reader_payoff\":\"The reader notices that the verb encodes a completed caused act with a recipient and content, not a vague statement that morality exists.\",\"reason\":\"QAC and attachment evidence identify a perfect Form IV verb with an attached first object and explicit coordinated content, while the subject is morphologically present but not overtly named in this ayah.\",\"representative_source_ids\":[\"QG-42f2eb82\",\"QG-f91e0cd0\",\"QF-06591b86\",\"QY-61acadd6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:4:coequal-coordination","source_type":"word_analysis","support_id":"sup_f2fd3830ece689267260","text":"{\"blocking_evidence\":null,\"headline\":\"co-equal moral objects\",\"reader_payoff\":\"The reader notices that breach and guarding are both included under one inspiration act, with no grammatical hint of alternation, apposition, hierarchy, or delay.\",\"reason\":\"QAC identifies the particle as coordination, and attachment evidence marks the second noun as conjoined with the first inside the same explicit content object.\",\"representative_source_ids\":[\"QG-d2bea2b7\",\"QG-eda32a57\",\"QI-7196a7e2\",\"QT-91c777c9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:2:formation-to-cultivation-bridge","source_type":"word_analysis","support_id":"sup_fa3688f3ef22600558e8","text":"{\"blocking_evidence\":null,\"headline\":\"formation becomes moral internalization\",\"reader_payoff\":\"The reader notices that the soul's formation in 91:7 is immediately filled with moral knowledge in 91:8 before cultivation is tested in 91:9.\",\"reason\":\"The pronoun chain and neighboring ayah sequence support a local arc from the formed soul in 91:7 to inspired recipient in 91:8 and cultivated object in 91:9.\",\"representative_source_ids\":[\"QB-56b0ab66\",\"QB-e13e40d0\",\"QB-b239bbef\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:2","source_type":"word_analysis","support_id":"sup_fe87792f18fd61175fd7","text":"{\"gloss_range\":\"completed causative inward inspiration directed to the soul, with a recipient suffix and coordinated moral content objects\",\"prose\":\"{{ar:أَلْهَمَهَا}} ({{tr:alhamahā}}) compresses the ayah's main event into one perfect Form IV verb: an agent is grammatically present, the soul is the attached recipient, and {{ar:فُجُورَهَا وَتَقْوَىٰهَا}} ({{tr:fujūrahā wa-taqwāhā}}) are the contents made known. The perfect aspect makes the moral endowment an accomplished feature of the soul's formation, not a later lesson waiting to begin. The root's swallowing and inward-taking field gives the inspiration a concrete uptake pressure, while the local Form IV keeps the action causative rather than making the soul engulf itself. The word is also distributionally marked as the ayah's rare inward-inspiration channel: a universal divine-to-soul disclosure of moral polarity, contrasted by the CRITICAL rows with prophet-specific revelation vocabulary. Across the boundary, the soul proportioned in 91:7 becomes the recipient here, and the same suffix chain carries it toward purification in 91:9.\",\"root_display\":\"{{ar:ل ه م}} ({{tr:l-h-m}})\",\"root_gloss_range\":\"root range includes swallowing or taking in, casting something into the inner mind, engulfing movement, abundance, and consuming calamity; the local Form IV verb selects caused inward inspiration while preserving internalization pressure\",\"surface_display\":\"{{ar:أَلْهَمَهَا}} ({{tr:alhamahā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:8:5:cosmic-oath-resonance","source_type":"word_analysis","support_id":"sup_feaeddf01934aed8cd5f","text":"{\"blocking_evidence\":null,\"headline\":\"oath-field resonance\",\"reader_payoff\":\"The reader notices a thematic resonance between the cosmic oath frame of 91:1-7 and the soul's own guarding capacity, without making that resonance a separate lexical sense.\",\"reason\":\"The oath-frame comparison can survive as thematic resonance because 91:8 answers 91:1-7, but it is narrowed so it does not claim that the word itself names cosmic protective functions.\",\"representative_source_ids\":[\"ME-a705e0e3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا","ayah_ref":"91:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001132/B004","root_001381/B001","root_001677/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001381","role":"Complete swallowing supplies the intake image and makes the causative act an inward assimilation of the pair.","root":"ل ه م","source_ref":"91:8","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_001132","role":"Departure from right through breached restraint supplies the outwardly transgressive orientation taken into the soul.","root":"ف ج ر","source_ref":"91:8","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001677","role":"Placing oneself in protective caution supplies the counter-orientation as an enacted self-positioning.","root":"و ق ي","source_ref":"91:8","source_word_indices":["3"]}],"changed_reading":{"after":"The verse depicts a soul made to internalize two executable orientations—breaching restraint and taking protective position—as capacities belonging to its own constitution.","before":"The verse reports that the soul is informed which abstract category is wickedness and which is piety."},"confidence":"strong","focus_anchor":"The causative verb at word 1 governs the two coordinated, soul-possessed nouns at words 2 and 3.","mechanism":"The soul is made to take in a paired interior repertoire: one mode breaches restraint and the other places the self within protection. Inspiration is therefore embodied assimilation of actionable orientations, not merely receipt of two definitions.","model_id":"baseline_inward_assimilation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_inward_assimilation","source_type":"hft","support_id":"sup_18176688d1b7ccdf56c6","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا","ayah_ref":"91:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001132/B001","root_001381/B004","root_001677/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001132","role":"Wide splitting and outflow provide the opening operation and its capacity to release what was contained.","root":"ف ج ر","source_ref":"91:8","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001677","role":"A barrier that wards off harm provides the opposed operation of preserving a boundary.","root":"و ق ي","source_ref":"91:8","source_word_indices":["3"]},{"branch_id":"B004","mapped_root_id":"root_001381","role":"Breadth and abundance make the inspired endowment capacious enough to contain both opposed boundary operations.","root":"ل ه م","source_ref":"91:8","source_word_indices":["1"]}],"changed_reading":{"after":"They are opposed operations on a shared threshold—rupture/outflow and protective interposition—installed within one capacious soul.","before":"Fujur and taqwa are two static moral labels deposited side by side."},"confidence":"strong","focus_anchor":"The juxtaposition of the two possessive nouns at words 2–3 makes their opposed root mechanics operate on one interior boundary.","mechanism":"Fujur opens a wide rupture through which stored pressure can issue; taqwa interposes a guard against harm. Their coordination models moral agency as regulation of permeability: whether an interior force becomes uncontrolled outflow or remains behind a protective threshold.","model_id":"baseline_threshold_pair"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_threshold_pair","source_type":"hft","support_id":"sup_d4164de075e7caa1b4b6","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا","ayah_ref":"91:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001132/B003","root_001381/B005","root_001677/B001"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001381","role":"An engulfing calamity supplies the hazard horizon within which inspiration includes recognition of what can consume the agent.","root":"ل ه م","source_ref":"91:8","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001132","role":"A sudden bursting-in of many supplies the nonlinear escalation associated with the hazardous orientation.","root":"ف ج ر","source_ref":"91:8","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001677","role":"Warding harm with a barrier supplies the anticipatory countermeasure rather than a second kind of eruption.","root":"و ق ي","source_ref":"91:8","source_word_indices":["3"]}],"changed_reading":{"after":"The construction may encode an asymmetric risk topology: an eruptive capacity that can engulf and a protective capacity meant to precede and contain it.","before":"The two inspired possibilities are balanced items in a neutral inventory."},"confidence":"exploratory","focus_anchor":"The singular act of inspiration at word 1 contains both the potentially eruptive noun at word 2 and the protective noun at word 3.","mechanism":"The pair is not dynamically symmetrical. Fujur can arrive as sudden multiplying pressure, while taqwa functions as prior protection against engulfment; the verse can thus map an internal hazard and its countermeasure rather than two equally placid options.","model_id":"baseline_asymmetric_hazard"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_asymmetric_hazard","source_type":"hft","support_id":"sup_b110be56511440060846","trust":"legacy_unbound"}]}
</lane_packet_json>
