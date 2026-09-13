# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **90:8**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s090-regular-20260912/s090/90_8/micro.discovery.json` and modify nothing
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
  "ayah_ref": "90:8",
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
{"branch_registry":[{"boundary":"Bu dal, var olan bir şeyi başka bir duruma sokmayı, adlandırmayı ya da bir eyleme başlamayı kapsamaz.","branch_kind":"bare","branch_ref":"root_000248/B001","candidate_links":[{"candidate_id":"cand_916eaf91310dddbb4892","lane":"micro"},{"candidate_id":"cand_9d5f774fa1f2635c73d0","lane":"micro"},{"candidate_id":"cand_edb46130327df37696aa","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"90:8:2:1","qac_word_ref":"90:8:2","surface_ar":"نَجْعَل"}],"gloss":"bir şeyi yapıp var etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığın yapılmasını, üretilmesini veya varlığa çıkarılmasını bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin üretilmesi, yaratılması veya yokken ortaya çıkarılması anlatıldığında dalın bütün çekirdeğini karşılar.","boundary_detail":"Bu dal, var olan bir şeyi başka bir duruma sokmayı, adlandırmayı ya da bir eyleme başlamayı kapsamaz.","branch_image_ar":"إحداث الشيء وصنعه","concept_gloss":"bir şeyi yapıp var etme","contextual_glosses":[{"applicability":"Bir nesnenin veya varlığın ortaya çıkarılışını bildiren tamamlanmış eylem bağlamlarında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapma ile var etme arasındaki çekirdek anlam genişliğini korur."},"facet_ids":["F001"],"text":"onu yaptı ya da var etti","usage_role":"contextual"}],"definition":"Bir şeyi yapmak, üretmek, yaratmak ya da daha önce yokken var etmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığın yapılmasını, üretilmesini veya varlığa çıkarılmasını bildirir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi yapma, üretme, yaratma veya yokken var etme anlamlarını açıkça aynı çekirdekte toplar. Geçici dal çerçevesi bu üretici ve var edici işlemi doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi yapmak, yaratmak veya var etmek"}],"lexicalization_note":"Dal yalın kullanıma dayanır; tanım herhangi bir özel söz öbeğine bağlı değildir.","neighbor_coverage_note":"Bütün adaylar incelendi; en güçlü karışma noktaları durum değiştirme dalı ile daha geniş yapma ve iş görme dalıdır, öteki adaylar aynı sınırı daha az açıklayıcı biçimde yineler.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sonucu bir şeyin yapılması ya da var edilmesidir; komşu dalda ise var olan katılımcı korunur ve yalnızca onun durumu veya niteliği değiştirilir.","focus_only":"Yeni bir şeyi üretme veya yokken varlığa çıkarma işlemini anlatır.","gloss":"bir duruma sokma","neighbor_only":"Var olan bir kişi ya da şeyi belirli bir duruma, niteliğe veya konuma getirir.","neighbor_ref":"root_000248/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir etkenin yol açtığı sonuç ve değişiklik bulunur."},{"boundary_match":"partial","distinction":"Odak dal nesnenin yapılması veya var edilmesinde yoğunlaşırken komşu dal, ortaya bir nesne çıkarmayan genel eylem ve davranışları da içine alır.","focus_only":"Bir şeyi üretme, yaratma veya varlığa çıkarma yönü belirgindir.","gloss":"yapma ve iş görme","neighbor_only":"İyi ya da kötü her türlü işi ve davranışı da kapsayan daha geniş bir eylem alanına sahiptir.","neighbor_ref":"root_000885/B001","relation_type":"near_synonym","shared_zone":"Bir şeyi yapma ve ortaya çıkarma anlamlarında iki dal geniş ölçüde örtüşür."}],"source_phrase_ar":"جعلت الشيء صنعته (maqayis)؛ جعل جعلا صنع صنعا (ayn)؛ جعل خلق؛ خلقنا (tahdhib)؛ يجري مجرى أوجد (mufradat)","source_summary":"Kaynaklar, bir şeyi yapma ile onu yaratıp var etme yönlerini ortak bir üretici eylem altında birleştirir.","sources":["MQ","AY","TA","MU"],"what_is_ar":"يدخل فيه جعل الشيء بمعنى صنعه أو خلقه أو أوجده.","what_is_not_ar":"لا يدخل فيه التصيير إلى حال، ولا التسمية والقول، ولا الشروع في الفعل."},"support_links":["sup_38d621ad8676a270d8de","sup_7f724a8aedb1f4c92909","sup_f8422ab530e8f2864f3f"]},{"boundary":"Burada katılımcı varlığını sürdürür ve durumu değişir; onu yoktan üretme, adlandırma veya eyleme başlatma anlamı yoktur.","branch_kind":"bare","branch_ref":"root_000248/B002","candidate_links":[{"candidate_id":"cand_f4758956817b3008e886","lane":"micro"},{"candidate_id":"cand_8d5784c74959bf315ac2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"90:8:2:1","qac_word_ref":"90:8:2","surface_ar":"نَجْعَل"}],"gloss":"birini veya şeyi belirli bir duruma getirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Var olan bir katılımcının durumunu, niteliğini veya konumunu değiştiren ettirici işlemi bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Katılımcının varlığı korunurken niteliği, görevi, konumu veya durumu değiştirildiğinde eksiksiz karşılık verir.","boundary_detail":"Burada katılımcı varlığını sürdürür ve durumu değişir; onu yoktan üretme, adlandırma veya eyleme başlatma anlamı yoktur.","branch_image_ar":"تصيير الشيء على حال","concept_gloss":"birini veya şeyi belirli bir duruma getirme","contextual_glosses":[{"applicability":"Bir kişinin veya şeyin yeni bir nitelik, görev ya da duruma geçirilmesini anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Var olan katılımcının ettirici bir işlemle yeni duruma geçmesini korur."},"facet_ids":["F001"],"text":"onu bu duruma getirdi","usage_role":"contextual"}],"definition":"Bir kişi veya şeyi belirli bir duruma, niteliğe ya da konuma getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Var olan bir katılımcının durumunu, niteliğini veya konumunu değiştiren ettirici işlemi bildirir."}],"identity_rationale":"Kaynak ifadesi, bir kişi veya şeyi belirli bir duruma, niteliğe ya da konuma getirme işlemini doğrudan bildirir. Verilen örnekler hem görev ve konum kazandırmayı hem de üstün bir niteliğe ulaştırmayı destekler.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi belirli bir duruma, niteliğe veya konuma getirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyi belirli bir duruma getirmek"}],"lexicalization_note":"Dal yalın kullanıma dayanır; özel bir söz öbeğinin anlamı genel tanıma taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; üretme ile ettirici olmayan duruma gelme, bu dalın katılımcı yapısını en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda sonuç, aynı katılımcının yeni durumudur; komşu dalda ise sonuç yapılan veya var edilen şeyin kendisidir.","focus_only":"Var olan katılımcıyı koruyup onun durumunu veya niteliğini değiştirir.","gloss":"bir şeyi var etme","neighbor_only":"Bir şeyi yapma, üretme ya da yokken varlığa çıkarma işlemini anlatır.","neighbor_ref":"root_000248/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de bir etkenin ortaya çıkardığı yeni sonucu ifade eder."},{"boundary_match":"partial","distinction":"Odak dal ettirici ve etkilenen olmak üzere iki katılımcılıdır; komşu dalda durum değişimi öznenin başına gelir ve ayrı bir ettirici zorunlu değildir.","focus_only":"Bir etkenin başka bir katılımcıyı yeni duruma soktuğu geçişli yapıyı gerektirir.","gloss":"bir duruma gelme","neighbor_only":"Öznenin bir dış ettirici belirtilmeden kendisinin yeni bir duruma gelmesini bildirir.","neighbor_ref":"root_000839/B010","relation_type":"near_neighbor","shared_zone":"İki dal da önceki durumdan farklı bir sonuç durumuna geçişi anlatır."}],"source_phrase_ar":"جعله الله نبيا أي صيره (sihah)؛ جعل صير؛ جعلته أحذق الناس؛ صيرهم؛ صيرته (tahdhib)","source_summary":"Kaynaklar, birini bir göreve veya üstün bir niteliğe getirmenin aynı durum değiştirme çekirdeğine bağlı olduğunu gösterir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه جعل الشيء أو الشخص على صفة أو منزلة، كتصييره نبيا أو جعله أحذق الناس.","what_is_not_ar":"لا يدخل فيه الخلق والإيجاد المجرد، ولا التسمية، ولا جعل بمعنى أخذ يفعل."},"support_links":["sup_77c357c1835b3de67c27","sup_f1fa3b6b909f8161d7f3"]},{"boundary":"Çekirdek adlandırma ve söylemedir; aynı söz dizimine ilişkin durum değiştirme yorumu ayrı bir kaynak değişkesi olarak tutulur.","branch_kind":"unresolved","branch_ref":"root_000248/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"90:8:2:1","qac_word_ref":"90:8:2","surface_ar":"نَجْعَل"}],"gloss":"öyle adlandırma ya da öyle olduğunu söyleme; başka yorumda öyle kılma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığı belli bir adla veya nitelikle anmayı ve onun öyle olduğunu söylemeyi bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı tanıklık için, varlığı söylenen duruma gerçekten getirme biçiminde rakip bir yorum da aktarılır."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem baskın adlandırma ve söyleme çözümünü hem de aynı tanıklığa ilişkin durum değiştirme yorumunu birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Çekirdek adlandırma ve söylemedir; aynı söz dizimine ilişkin durum değiştirme yorumu ayrı bir kaynak değişkesi olarak tutulur.","branch_image_ar":"قول الشيء أو تسميته","concept_gloss":"öyle adlandırma ya da öyle olduğunu söyleme; başka yorumda öyle kılma","contextual_glosses":[{"applicability":"Sözün bir varlığa ad veya nitelik yükleyen anlatım olarak çözüldüğü bağlamda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı ifadenin varlığı gerçekten o duruma getirme biçimindeki rakip yorumunu dışarıda bırakır.","preserves":"Adlandırma ve sözle niteleme çözümünü açık biçimde korur."},"facet_ids":["F001"],"text":"onları öyle adlandırdılar","usage_role":"contextual"},{"applicability":"Tanıklığın gerçek bir durum değişikliği olarak yorumlandığı bağlamda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Baskın adlandırma ve söyleme çözümünü dışarıda bırakır.","preserves":"Rakip durum değiştirme yorumunu doğrudan korur."},"facet_ids":["F002"],"text":"onları öyle yaptılar","usage_role":"contextual"}],"definition":"Bir varlığı belirli bir ad veya nitelikle anmak ya da onun öyle olduğunu söylemektir; aynı ifadenin bir yorumunda ise varlığı gerçekten o duruma getirme anlamı vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığı belli bir adla veya nitelikle anmayı ve onun öyle olduğunu söylemeyi bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı tanıklık için, varlığı söylenen duruma gerçekten getirme biçiminde rakip bir yorum da aktarılır."}],"identity_rationale":"Kaynak ifadesinin baskın açıklaması bir varlığı belirli bir ad veya nitelikle anma ve onun öyle olduğunu söylemedir. Bununla birlikte aynı ifadenin bir başka yorumda o varlığı gerçekten söz konusu duruma getirme diye açıklandığı da kaydedilir; bu yüzden dal ancak bu yorum ayrılığı belirtilerek korunabilir.","lexicalization_note":"Kullanımın yalın olup olmadığı mekanik olarak çözümlenmemiştir; tanım bağımsız bir yalın anlam varsaymaz.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; en yararlı ayrımlar geniş sözlü anma alanı ile aynı tanıklığa rakip olan gerçek durum değişikliğidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir yüklemeyi adlandırma veya söyleme olarak çözer; komşu dal ise sözlü anmayı ve hakkında konuşmayı daha geniş biçimde kapsar.","focus_only":"Belirli bir nesneyi veya varlığı belli bir ad ya da nitelikle anma yapısına bağlıdır.","gloss":"dilde anma ve adlandırma","neighbor_only":"Bir şeyi dilde anma, açığa vurma ve insanlar hakkında iyi ya da kötü söz söyleme alanlarına da uzanır.","neighbor_ref":"root_000516/B004","relation_type":"near_synonym","shared_zone":"Bir şeyi sözle belirtme ve adlandırma bölgesinde iki dal örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın baskın okuması dilsel bir yüklemedir; komşu dal gerçek dünyadaki durum değişikliğini anlatır ve odak dalda yalnızca rakip yorum olarak görünür.","focus_only":"Çekirdeğinde sözle adlandırma veya bir niteliği söyleme vardır.","gloss":"bir duruma sokma","neighbor_only":"Var olan katılımcının durumunu gerçekten değiştiren ettirici işlemdir.","neighbor_ref":"root_000248/B002","relation_type":"near_neighbor","shared_zone":"Aynı yüzey yapısı, aktarılan yorum ayrılığı nedeniyle iki anlam alanına yaklaşabilir."}],"source_phrase_ar":"جعلوا الملائكة إناثا أي سموهم (sihah)؛ جعل قال؛ أي قلناه؛ وقال غيره صيرناه (tahdhib)","source_summary":"Toplu tanıklık adlandırma ve söyleme açıklamasını verirken, aynı ifadenin durum değiştirme diye yorumlandığını da kaynak adı yüklemeden kaydeder.","sources":["SI","TA"],"what_is_ar":"يدخل فيه جعل بمعنى قال أو سمى بحسب النصوص التي صرحت بذلك.","what_is_not_ar":"لا يدخل فيه التصيير إلا حيث اختلف المصدر في العبارة نفسها."},"support_links":[]},{"boundary":"Anlam yalnızca ardından bir eylem gelen yapıya bağlıdır ve genel yapma, üretme ya da kesintisiz sürdürme anlamına genişletilemez.","branch_kind":"non_bare","branch_ref":"root_000248/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"90:8:2:1","qac_word_ref":"90:8:2","surface_ar":"نَجْعَل"}],"gloss":"bir eylemi yapmaya başlama","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Öznenin belirtilen eyleme başlamasını veya girişmesini anlatan yapı bağımlı bir kullanımdır."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca öznenin hemen ardından belirtilen eyleme giriştiğini bildiren yapı bağımlı kullanımı karşılar.","boundary_detail":"Anlam yalnızca ardından bir eylem gelen yapıya bağlıdır ve genel yapma, üretme ya da kesintisiz sürdürme anlamına genişletilemez.","branch_image_ar":"الشروع في الفعل أو ملازمته","concept_gloss":"bir eylemi yapmaya başlama","contextual_glosses":[{"applicability":"Ardından gelen eylemin özne tarafından başlatıldığını bildiren geçmiş zamanlı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öznenin belirtilen eyleme giriştiği başlangıç aşamasını korur."},"facet_ids":["F001"],"text":"yapmaya başladı","usage_role":"contextual"}],"definition":"Yalnızca ardından çekimli bir eylem gelen yapıda, öznenin o eylemi yapmaya başlamasını veya ona girişmesini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Öznenin belirtilen eyleme başlamasını veya girişmesini anlatan yapı bağımlı bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi, çekimli bir eylemden önce gelen yapının o eyleme girişme veya başlamayı bildirdiğini gösterir. Geçici çerçevedeki genel bağlı kalma ve sürdürme yönü kaynak cümlesinde kurucu bir koşul değildir; tanım bu nedenle başlangıç anlamına göre yeniden kurulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyi yapmaya başlamak"}],"lexicalization_note":"Dal yalnızca ardından çekimli bir eylem gelen özel yapıda geçerlidir; yalın kök anlamı olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; başlangıçla sürdürmeyi birlikte taşıyan yakın yapı ile yalnız devam bildiren yapı, sınırı en iyi görünür kılar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın güvenli çekirdeği başlangıçtır; komşu dalda ise başlangıçla birlikte sürdürme veya bağlı kalma yönü de açıkça yer alır.","focus_only":"Kaynak tanıklığı çekirdek olarak bir eyleme girişmeyi bildirir.","gloss":"bir eyleme başlayıp sürdürme","neighbor_only":"Başlangıcın yanında eyleme bağlı kalma ve onu sürdürme yönünü de taşıyabilir.","neighbor_ref":"root_000941/B001","relation_type":"near_synonym","shared_zone":"Ardından eylem gelen yapılarda başlangıç bildirme bakımından güçlü bir örtüşme vardır."},{"boundary_match":"partial","distinction":"Odak dal başlangıç aşamasını seçer; komşu dal başlangıcı değil, önceden süren durumun devamını ve özel bir olumsuz kuruluşu gerektirir.","focus_only":"Eylemin başlangıç sınırını ve ona girişmeyi bildirir.","gloss":"eylemi sürdürme","neighbor_only":"Olumsuz kuruluşta eylemin ya da haberin kesintisiz sürmesini bildirir.","neighbor_ref":"root_000659/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bir öznenin bir eylemle zaman içinde ilişkisini kurar."}],"source_phrase_ar":"تقول جعل يقول ولا تقول صنع يقول (maqayis)؛ جعل يأكل وجعل يصنع كذا (ayn)؛ جعل فلان يصنع كذا كقولك طفق وعلق يفعل (tahdhib)؛ يجري مجرى صار وطفق فلا يتعدى نحو جعل زيد يقول (mufradat)","source_summary":"Kaynaklar, bu yapıyı ardından gelen eyleme başlama veya girişme anlamında ve nesne almayan bir kuruluş olarak ortaklaştırır.","sources":["MQ","AY","TA","MU"],"what_is_ar":"يدخل فيه جعل يفعل كذا، أي أخذ أو طفق أو علق بالفعل.","what_is_not_ar":"لا يدخل فيه صنع الشيء ولا تصييره ولا جعله أجرا."},"support_links":[]},{"boundary":"Bu dal iş veya görev karşılığında belirlenen ödemedir; genel armağanı, yapılan işi, durum değiştirmeyi ve tencere bezini kapsamaz.","branch_kind":"bare","branch_ref":"root_000248/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"90:8:2:1","qac_word_ref":"90:8:2","surface_ar":"نَجْعَل"}],"gloss":"iş karşılığı belirlenen ücret veya ortaklaşa kararlaştırılan ödeme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir iş veya görevin yapılması karşılığında bir kişiye ayrılan ücret, ödeme ya da armağandır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğun sefer veya önemli bir iş sırasında kendi arasında kararlaştırdığı ortak ödemeleri de kapsar."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem bir kişiye iş için ayrılan karşılığı hem de bir topluluğun önemli iş için kararlaştırdığı ödeme biçimini kapsar.","boundary_detail":"Bu dal iş veya görev karşılığında belirlenen ödemedir; genel armağanı, yapılan işi, durum değiştirmeyi ve tencere bezini kapsamaz.","branch_image_ar":"أجر مجعول على عمل","concept_gloss":"iş karşılığı belirlenen ücret veya ortaklaşa kararlaştırılan ödeme","contextual_glosses":[{"applicability":"Belirli bir işi üstlenecek kişiye vaat edilen ücret veya ödülün anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir topluluğun kendi arasında kararlaştırdığı ortak ödeme özel durumunu dışarıda bırakır.","preserves":"Bir işin yapılmasına bağlanan bireysel ücret veya ödül çekirdeğini korur."},"facet_ids":["F001"],"text":"bu işi yapana verilecek ücret","usage_role":"contextual"},{"applicability":"Bir sefer veya önemli iş için insanların aralarında ödeme belirlediği topluluk bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir kişiye belirli bir işi yapması için ayrılan bireysel ücret biçimini dışarıda bırakır.","preserves":"Topluluğun karşılıklı olarak ödeme kararlaştırması yönünü korur."},"facet_ids":["F002"],"text":"ortaklaşa kararlaştırılan ödeme","usage_role":"contextual"}],"definition":"Bir kişinin yapacağı iş veya görev karşılığında ona verilmek üzere belirlenen ücret, ödeme ya da armağandır. Bir topluluğun sefer veya önemli bir iş için aralarında kararlaştırdığı ödemeler de bu çekirdeğin özel bir gerçekleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir iş veya görevin yapılması karşılığında bir kişiye ayrılan ücret, ödeme ya da armağandır."},{"facet_id":"F002","role":"specialization","statement":"Bir topluluğun sefer veya önemli bir iş sırasında kendi arasında kararlaştırdığı ortak ödemeleri de kapsar."}],"identity_rationale":"Kaynak ifadesi, bir kişiye yapacağı iş veya yerine getireceği görev karşılığında ayrılan ücret, ödeme ya da armağanı açıkça tanımlar. İnsanların bir sefer veya önemli iş için aralarında kararlaştırdıkları ortak ödemeler de aynı karşılık belirleme çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir iş karşılığında belirlenen ücret, ödeme veya ödül"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"önemli bir iş için ortaklaşa kararlaştırılan ödemeler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ona bir ödeme veya armağan ayırmak"}],"lexicalization_note":"Dal yalın ad alanına dayanır; özel bir söz öbeğiyle sınırlı değildir.","neighbor_coverage_note":"Bütün adaylar incelendi; genel emek karşılığı ile düzenli çalışan ücreti, bu dalın önceden belirlenen görev karşılığı sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir işi yaptırmak için konan veya kararlaştırılan karşılıktır; komşu dalın karşılık alanı daha geniştir ve önceden konma koşulu taşımaz.","focus_only":"Belirli bir iş yapılmadan önce veya onun için konan karşılığı öne çıkarır.","gloss":"emek karşılığı ve kira","neighbor_only":"Yapılmış işin karşılığını, kirayı, manevi ödülü ve evlilikte verilen bedeli de kapsar.","neighbor_ref":"root_000015/B001","relation_type":"near_synonym","shared_zone":"Bir iş ya da hizmet karşılığında verilen maddi bedel alanında örtüşürler."},{"boundary_match":"partial","distinction":"Odak dal görev koşuluna bağlı vaat veya belirlemedir; komşu dal düzenli çalışma karşılığındaki ücret ve geçim payı alanında daha özeldir.","focus_only":"Tek bir görev için vaat edilen ödülü ve topluca kararlaştırılan ödemeyi de kapsar.","gloss":"çalışanın ücreti","neighbor_only":"Bir çalışanın düzenli iş ücreti veya geçim payı olmasına odaklanır.","neighbor_ref":"root_001046/B004","relation_type":"near_synonym","shared_zone":"Yapılan emek karşılığında bir kişiye verilen maddi ödemede örtüşürler."}],"source_phrase_ar":"الجعل والجعالة والجعلية ما يجعل للإنسان على الأمر يفعله (maqayis)؛ الجعل ما جعلت لإنسان أجرا له على عمل يعمله؛ الجعالات ما يتجاعل الناس بينهم (ayn)؛ الجعل ما جعل للانسان من شئ على الشئ يفعله؛ الجعالة؛ الجعيلة مثله (sihah)؛ الجعل في العطية؛ الجعالة بالفتح من الشيء تجعله للإنسان؛ ما جعلته للإنسان أجرا على عمله (tahdhib)","source_summary":"Kaynaklar iş karşılığında önceden ayrılan ücret veya armağanda birleşir; topluca kararlaştırılan ödemeler bu çekirdeğin özel biçimi olarak aktarılır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الجعل والجعلية والجعالة والجعيلة وما يتجاعله الناس أجرا أو عطية على عمل أو أمر.","what_is_not_ar":"لا يدخل فيه فعل جعل بمعنى صنع أو صير، ولا الجعال خرقة القدر."},"support_links":[]},{"boundary":"Dal yalnızca kısa veya küçük hurma ağaçlarına ilişkindir; yer adı, böcek ve genel bitki kısalığı anlamlarına uzanmaz.","branch_kind":"bare","branch_ref":"root_000248/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"90:8:2:1","qac_word_ref":"90:8:2","surface_ar":"نَجْعَل"}],"gloss":"kısa veya küçük hurma ağaçları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kısa veya küçük hurma ağaçlarını topluluk olarak, tekil biçimiyle de bunlardan birini adlandırır."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hurma ağaçlarının boyca kısa ya da küçük oluşuna göre topluca adlandırıldığı kullanımların bütün çekirdeğini karşılar.","boundary_detail":"Dal yalnızca kısa veya küçük hurma ağaçlarına ilişkindir; yer adı, böcek ve genel bitki kısalığı anlamlarına uzanmaz.","branch_image_ar":"النخل الصغار أو القصار","concept_gloss":"kısa veya küçük hurma ağaçları","contextual_glosses":[{"applicability":"Birden çok kısa veya küçük hurma ağacının topluca anıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kısa hurma ağaçlarını topluluk olarak adlandırma yönünü korur."},"facet_ids":["F001"],"text":"kısa hurma ağaçları topluluğu","usage_role":"contextual"}],"definition":"Kısa veya küçük hurma ağaçlarının topluluk adı ve bu topluluktaki tek bir ağacın adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kısa veya küçük hurma ağaçlarını topluluk olarak, tekil biçimiyle de bunlardan birini adlandırır."}],"identity_rationale":"Kaynak ifadesi, kısa veya küçük hurma ağaçlarını topluluk olarak ve bunlardan birini tekil biçimde tanımlar. Geçici çerçeve hem boy hem küçüklük yönünü ve tekil ayrımını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kısa veya küçük hurma ağaçları; tekili bu ağaçlardan biri"}],"lexicalization_note":"Dal yalın ad kullanımına dayanır; özel bir söz öbeğinden türetilmiş değildir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı küçük hurma alanındaki yakın ad ile özellikle genç sürgünü anlatan ad, sınırı açıklamak için yeterlidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hem küçük hem kısa ağaçlara uzanır; komşu dalın verilen sınırı yalnız küçüklüktür, bu nedenle tam ikame her bağlamda güvenli değildir.","focus_only":"Küçüklüğün yanında boyca kısalığı da açıkça kapsar.","gloss":"küçük hurma ağaçları","neighbor_only":"Yalnız küçük hurma ağaçlarını bildirir ve ayrı bir söz ailesine dayanır.","neighbor_ref":"root_000832/B006","relation_type":"near_synonym","shared_zone":"Küçük hurma ağaçlarını topluca adlandırmada iki dal doğrudan örtüşür."},{"boundary_match":"partial","distinction":"Odak dal boy veya genel küçüklük ölçütüne dayanır; komşu dal ise bitkinin sürgün ve dikim evresini seçer.","focus_only":"Kısa veya küçük hurma ağaçlarının kendisini topluluk olarak adlandırır.","gloss":"genç hurma sürgünleri","neighbor_only":"Özellikle yeni dikilmiş küçük sürgünleri ve bunların tekil ile çoğul biçimlerini adlandırır.","neighbor_ref":"root_001637/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal hurmanın küçük ve henüz gelişmemiş örnekleriyle ilişkilidir."}],"source_phrase_ar":"الجعل النخل يفوت اليد والواحدة جعلة (maqayis)؛ الجعل واحدها جعلة وهي النخل الصغار (ayn)؛ الجعل النخل القصار الواحدة جعلة (sihah)؛ الجعل قصار النخل (tahdhib)","source_summary":"Kaynaklar kısa veya küçük hurma ağaçları anlamında ve topluluk ile tek ağaç arasındaki biçim ayrımında birleşir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الجعل للنخل الصغار أو القصار، والواحدة جعلة.","what_is_not_ar":"لا يدخل فيه جعلة اسم المكان ولا الجعل الدويبة."},"support_links":[]},{"boundary":"Dal tencereyi indirmeye yarayan ısı koruyucu bez ve onunla yapılan eylemle sınırlıdır; ücret anlamındaki benzer biçim buna girmez.","branch_kind":"bare","branch_ref":"root_000248/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"90:8:2:1","qac_word_ref":"90:8:2","surface_ar":"نَجْعَل"}],"gloss":"sıcak tencereyi indirme bezi ve onunla indirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sıcak tencereyi ocaktan indirirken tutmaya yarayan ve eli sıcaktan koruyan bezdir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tencereyi bu bez aracılığıyla ateşten indirme eylemini de bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem ısıdan koruyan araç adı hem de tencereyi bu araçla ocaktan indirme eylemi birlikte gösterileceğinde kullanılır.","boundary_detail":"Dal tencereyi indirmeye yarayan ısı koruyucu bez ve onunla yapılan eylemle sınırlıdır; ücret anlamındaki benzer biçim buna girmez.","branch_image_ar":"خرقة إنزال القدر","concept_gloss":"sıcak tencereyi indirme bezi ve onunla indirme","contextual_glosses":[{"applicability":"Sıcak tencereyi tutup ocaktan indirmeye yarayan bez nesne olarak anıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı bezle tencereyi indirmeyi bildiren eylem kullanımını dışarıda bırakır.","preserves":"Aracın tencereyi indirme ve eli ısıdan koruma işlevini korur."},"facet_ids":["F001"],"text":"tencereyi ateşten indirme bezi","usage_role":"contextual"},{"applicability":"Tencerenin özel bez kullanılarak ocaktan indirilmesi eylem olarak anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bezin bağımsız araç adı olarak kullanılmasını dışarıda bırakır.","preserves":"Tencereyi koruyucu bez aracılığıyla indirme işlemini korur."},"facet_ids":["F002"],"text":"tencereyi bezle ateşten indirmek","usage_role":"contextual"}],"definition":"Sıcak tencereyi ateşten veya dayandığı taşlardan indirirken kullanılan ve eli sıcaktan koruyan bezdir; bu bezle tencereyi indirme eylemi de aynı dala bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sıcak tencereyi ocaktan indirirken tutmaya yarayan ve eli sıcaktan koruyan bezdir."},{"facet_id":"F002","role":"associated_use","statement":"Tencereyi bu bez aracılığıyla ateşten indirme eylemini de bildirir."}],"identity_rationale":"Kaynak ifadesi, sıcak tencereyi ateşten veya onu taşıyan taşlardan indirirken kullanılan ve eli sıcaktan koruyan bezi açıkça tanımlar. Aynı tanıklık, tencereyi bu bezle indirme eylemini de ayrı bir türemiş kullanım olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sıcak tencereyi ateşten indirmeye yarayan koruyucu bez"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"tencereyi koruyucu bezle ateşten indirmek"}],"lexicalization_note":"Dal yalın ad ve ona bağlı eylem biçimlerini kapsar; başka dallardaki benzer sesli adlar tanıma alınmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; tencereyi yönetmeye yarayan çubuk ile onu ateşte taşıyan taş, aracın özgül işlevini en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak araç tencerenin dışından tutulmasını ve ocaktan indirilmesini sağlar; komşu araç tencerenin içine sokularak kaynamayı yatıştırır.","focus_only":"Tencereyi ocaktan indirirken kullanılan ve eli sıcaktan koruyan bir bezdir.","gloss":"tencere karıştırma çubuğu","neighbor_only":"Tencerenin içini karıştırıp kaynamasını yatıştırmak için kullanılan bir çubuktur.","neighbor_ref":"root_001676/B011","relation_type":"same_field","shared_zone":"İki araç da sıcak tencereyi güvenli biçimde yönetmeye yarayan ev gereçleridir."},{"boundary_match":"thematic_only","distinction":"Odak dal kaldırma sırasında kullanılan koruyucu aracı, komşu dal ise pişirme sırasında tencereyi taşıyan yapısal desteği adlandırır.","focus_only":"Eli koruyarak tencereyi ateşten indirmeye yarayan taşınabilir bir bezdir.","gloss":"tencereyi taşıyan üçüncü taş","neighbor_only":"Tencereyi ateş üzerinde taşımak için iki taşa eklenen üçüncü sabit destektir.","neighbor_ref":"root_000203/B007","relation_type":"thematic","shared_zone":"Her ikisi de ateş üzerindeki tencerenin kurulması ve kaldırılması senaryosunda yer alır."}],"source_phrase_ar":"الجعال الخرقة التي تنزل بها القدر عن الأثافي (maqayis)؛ الجعال والجعالة خرقة تنزل بها القدر عن رأس النار يتقى بها من الحر (ayn)؛ الجعال الخرقة التي تنزل بها القدر عن النار؛ أجعلت القدر (sihah)؛ الجعال الخرقة التي تنزل بها القدور؛ أجعلت القدر إجعالا إذا أنزلتها بالجعال (tahdhib)","source_summary":"Kaynaklar bezin tencereyi ateşten indirirken ısıdan koruma işlevinde birleşir ve aynı araçla yapılan indirme eylemini de aktarır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الجعال أو الجعالة، وهي خرقة تنزل بها القدر عن النار أو الأثافي ويتقى بها الحر.","what_is_not_ar":"لا يدخل فيه الجعالة بمعنى الأجر."},"support_links":[]},{"boundary":"Hayvanın kendisi yalın çekirdektir; suya ilişkin anlam yalnız bu hayvanların suda çok bulunmasını bildiren özel kuruluşta geçerlidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000248/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"90:8:2:1","qac_word_ref":"90:8:2","surface_ar":"نَجْعَل"}],"gloss":"kara küçük yer hayvanı ve bunlarla dolu su","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kara renkli küçük bir yer hayvanını adlandırır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yalnız suyla kurulan kullanımda, bu hayvanların suyun içinde çokça bulunmasını bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın hayvan adı ile yalnız bu hayvanların çokça bulunduğu suyu anlatan bağlı kullanım birlikte gösterileceğinde uygundur.","boundary_detail":"Hayvanın kendisi yalın çekirdektir; suya ilişkin anlam yalnız bu hayvanların suda çok bulunmasını bildiren özel kuruluşta geçerlidir.","branch_image_ar":"دويبة الجعلان","concept_gloss":"kara küçük yer hayvanı ve bunlarla dolu su","contextual_glosses":[{"applicability":"Canlının kendisi yalın bir ad olarak anıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu hayvanların çok bulunduğu suyu anlatan bağlı kullanımı dışarıda bırakır.","preserves":"Kara renkli küçük yer hayvanı çekirdeğini korur."},"facet_ids":["F001"],"text":"kara renkli küçük yer hayvanı","usage_role":"contextual"},{"applicability":"Suyun içinde söz konusu hayvanların çokça bulunduğu özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanın bağımsız yalın ad olarak kullanılmasını dışarıda bırakır.","preserves":"Suya bağlı hayvan çokluğu ve doluluk yönünü korur."},"facet_ids":["F002"],"text":"bu hayvanlarla dolu su","usage_role":"contextual"}],"definition":"Kara renkli küçük bir yer hayvanıdır. Buna bağlı söz öbeği, bu hayvanların içine çokça düştüğü veya içinde çoğaldığı suyu niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kara renkli küçük bir yer hayvanını adlandırır."},{"facet_id":"F002","role":"associated_use","statement":"Yalnız suyla kurulan kullanımda, bu hayvanların suyun içinde çokça bulunmasını bildirir."}],"identity_rationale":"Kaynak ifadesi, küçük bir yer hayvanını ve onun kara renkli oluşunu bildirir; ayrıca bu hayvanların çokça bulunduğu suyu niteleyen bağlı kullanımı verir. Geçici çerçeve bu iki kapsamı doğru ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kara renkli küçük bir yer hayvanı"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bu hayvanların çokça bulunduğu su"}],"lexicalization_note":"Yalın hayvan adı ile yalnız bu hayvanların çokça bulunduğu suyu niteleyen söz öbeği ayrı facetlerde tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel küçük yer hayvanları sınıfı, odak canlının belirli bir ad oluşunu açıklayan en yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir hayvan adıdır ve suya özgü türemiş kullanımı vardır; komşu dal ise birçok farklı küçük hayvanı içine alan üst sınıftır.","focus_only":"Kara renkli belirli bir küçük yer hayvanını ve ona bağlı su niteliğini adlandırır.","gloss":"küçük yer hayvanları","neighbor_only":"Küçük yer hayvanlarının pek çok türünü topluca kapsayan genel bir sınıf adıdır.","neighbor_ref":"root_000324/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal küçük ve yerde yaşayan hayvanlar alanında buluşur."}],"source_phrase_ar":"الجعل دابة من هوام الأرض (ayn)؛ الجعل دويبة؛ جعل الماء بالكسر أي كثر فيه الجعلان (sihah)؛ الجعل دابة سوداء من دواب الأرض تجمع جعلانا؛ ماء مجعل وجعل إذا تهافتت فيه الجعلان (tahdhib)","source_summary":"Kaynaklar küçük yer hayvanı anlamında birleşir; kara renk niteliğini ve hayvanların çok bulunduğu suya özgü kullanımı da topluca destekler.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه الجعل دابة أو دويبة من هوام الأرض، وجمعها جعلان، وما وصف به الماء إذا كثرت فيه الجعلان.","what_is_not_ar":"لا يدخل فيه الجعل بمعنى الأجر أو النخل."},"support_links":[]},{"boundary":"Dal dişi köpek ve benzeri yırtıcı dişilerin çiftleşme isteğiyle sınırlıdır; erkeğin isteğini veya çiftleşmenin gerçekleşmesini bildirmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000248/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"90:8:2:1","qac_word_ref":"90:8:2","surface_ar":"نَجْعَل"}],"gloss":"dişinin çiftleşmek için erkeği istemesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"specialization","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi köpeği, çiftleşmek için erkeği isteyen durumda niteleyen söz öbeğidir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi köpek ve diğer yırtıcı dişilerin erkeği istemesi durumunu çekimli biçimlerle bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi köpek veya benzeri yırtıcı dişinin çiftleşme isteğini bildiren hem niteleme hem eylem biçimlerini karşılar.","boundary_detail":"Dal dişi köpek ve benzeri yırtıcı dişilerin çiftleşme isteğiyle sınırlıdır; erkeğin isteğini veya çiftleşmenin gerçekleşmesini bildirmez.","branch_image_ar":"اشتهاء الأنثى للفحل","concept_gloss":"dişinin çiftleşmek için erkeği istemesi","contextual_glosses":[{"applicability":"Dişi köpek veya benzeri bir yırtıcı dişinin erkeği istediği durum niteleme olarak verildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişi hayvanın çiftleşmeye yönelik erkek isteğini korur."},"facet_ids":["F001","F002"],"text":"çiftleşmek isteyen dişi","usage_role":"contextual"}],"definition":"Dişi köpeğin veya benzeri yırtıcı bir dişinin çiftleşmek için erkeği istemesidir; hem belirli bir söz öbeği hem de çekimli biçimler bu durumu anlatır.","distinctive_facets":[{"facet_id":"F001","role":"specialization","statement":"Dişi köpeği, çiftleşmek için erkeği isteyen durumda niteleyen söz öbeğidir."},{"facet_id":"F002","role":"core","statement":"Dişi köpek ve diğer yırtıcı dişilerin erkeği istemesi durumunu çekimli biçimlerle bildirir."}],"identity_rationale":"Kaynak ifadesi, dişi köpeğin ve diğer yırtıcı dişilerin çiftleşmek üzere erkeği istemesini açıkça bildirir. Hem dişi köpekle kurulan söz öbeği hem de çekimli biçimler aynı üreme isteği durumuna bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"çiftleşmek isteyen dişi köpek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"dişinin çiftleşmek için erkeği istemesi"}],"lexicalization_note":"Dişi köpekle kurulan söz öbeği ile dişinin isteğini bildiren çekimli biçimler ayrı tutulur; kapsam genel bir yalın kök anlamına çevrilmez.","neighbor_coverage_note":"Bütün adaylar incelendi; daha geniş hayvan kapsamlı yakın ad ile dişi deveye özgü ad, tür sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın tür sınırı köpek ve benzeri yırtıcılardır; komşu dal aynı durumu daha geniş bir hayvan listesinde adlandırır.","focus_only":"Dişi köpek ve benzeri yırtıcı dişiler için belirli niteleme ve eylem biçimlerine dayanır.","gloss":"dişi hayvanın erkeği istemesi","neighbor_only":"Koyun, sığır ve keçi gibi daha geniş evcil hayvan sınıflarına da uzanır.","neighbor_ref":"root_000860/B010","relation_type":"near_synonym","shared_zone":"Dişi köpek ve yırtıcı dişilerin çiftleşme isteğinde iki dal doğrudan örtüşür."},{"boundary_match":"partial","distinction":"Çekirdek durum aynıdır, ancak tür kapsamları ayrıdır: odak dal köpek ve yırtıcı dişilere, komşu dal dişi deveye bağlıdır.","focus_only":"Dişi köpek ve diğer yırtıcı dişilerin çiftleşme isteğine özgüdür.","gloss":"dişi devenin erkeği istemesi","neighbor_only":"Aynı isteği yalnız dişi deve için adlandırır.","neighbor_ref":"root_000009/B012","relation_type":"near_synonym","shared_zone":"Her iki dal dişi hayvanın çiftleşmek üzere erkeği istemesini anlatır."}],"source_phrase_ar":"كلبة مجعل إذا أرادت السفاد (maqayis)؛ أجعلت الكبة واستجعلت فهي مجعل إذا أرادت السفاد وكذلك سائر السباع (sihah)؛ أجعلت الكلبة والسباع كلها إذا اشتهت الفحل؛ استجعلت أيضا بمعناه (tahdhib)","source_summary":"Kaynaklar dişi köpeğin ve diğer yırtıcı dişilerin çiftleşme isteğinde birleşir ve söz öbeği ile çekimli biçimleri aynı duruma bağlar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه مجعل وأجعلت واستجعلت للكلبة والسباع إذا أرادت السفاد أو اشتهت الفحل.","what_is_not_ar":"لا يدخل فيه الجعل الدويبة ولا الفعل العام جعل."},"support_links":[]},{"boundary":"Dal yalnız deve kuşunun yavrusunu adlandırır; genel yavru, başka kuş yavrusu veya deve yavrusu anlamına genişlemez.","branch_kind":"bare","branch_ref":"root_000248/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"90:8:2:1","qac_word_ref":"90:8:2","surface_ar":"نَجْعَل"}],"gloss":"deve kuşu yavrusu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Türü deve kuşu olan genç yavruyu bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız deve kuşunun genç yavrusu adlandırıldığında eksiksiz ve doğal karşılıktır.","boundary_detail":"Dal yalnız deve kuşunun yavrusunu adlandırır; genel yavru, başka kuş yavrusu veya deve yavrusu anlamına genişlemez.","branch_image_ar":"فرخ النعام","concept_gloss":"deve kuşu yavrusu","contextual_glosses":[{"applicability":"Canlı bir cümlede deve kuşunun yavrusundan söz edilirken doğal sözcük sırasını sağlar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Deve kuşu türünü ve yavruluk durumunu eksiksiz korur."},"facet_ids":["F001"],"text":"yavru deve kuşu","usage_role":"contextual"}],"definition":"Deve kuşunun yavrusunu adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Türü deve kuşu olan genç yavruyu bildirir."}],"identity_rationale":"Kaynak ifadesi söz konusu biçimi doğrudan deve kuşunun yavrusu olarak açıklar. Geçici çerçeve bu hayvan türü ve yaşam evresi ayrımını eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"deve kuşu yavrusu"}],"lexicalization_note":"Dal yalın ad kullanımına dayanır ve herhangi bir özel söz öbeğiyle sınırlı değildir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çok anlamlı yakın ad ile genel yavru adı, tür ve kapsam sınırlarını en yararlı biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bütünüyle deve kuşu yavrusuna bağlıdır; komşu dal aynı karşılığın yanında tür ve insan bakımından başka anlamlara da uzanır.","focus_only":"Yalnız deve kuşu yavrusunu adlandıran tek anlamlı kullanım burada esastır.","gloss":"deve kuşu yavruları ve başka topluluklar","neighbor_only":"Deve kuşu yavrusunun yanında küçük develeri ve hizmetçileri de kapsayan daha geniş bir anlam kümesi vardır.","neighbor_ref":"root_000343/B008","relation_type":"near_synonym","shared_zone":"Deve kuşunun yavrusunu adlandırma alanında iki dal örtüşür."},{"boundary_match":"partial","distinction":"Odak dal tür bakımından özeldir; komşu dal pek çok canlı türünün yavrusunu içine alan genel sınıf adıdır.","focus_only":"Yavruluğu özellikle deve kuşu türüne bağlayan özel bir addır.","gloss":"küçük yavru","neighbor_only":"İnsan, evcil hayvan ve yabanıl hayvan yavrularını genel olarak kapsar.","neighbor_ref":"root_000942/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal doğumdan sonraki genç ve küçük yaşam evresini anlatır."}],"source_phrase_ar":"الجعول ولد النعام (maqayis)؛ الجعول الرأل ولد النعام (tahdhib)","source_summary":"Kaynaklar bu adın deve kuşunun yavrusunu bildirdiği konusunda birleşir.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه الجعول بمعنى الرأل، ولد النعام.","what_is_not_ar":"لا يدخل فيه الجعل الدويبة ولا الجعل النخل."},"support_links":[]},{"boundary":"Adın gösterdiği belirli yer açıklanmadığı için tanım bir yer kimliği uydurmaz ve sözü genel yer anlamına dönüştürmez.","branch_kind":"non_bare","branch_ref":"root_000248/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"90:8:2:1","qac_word_ref":"90:8:2","surface_ar":"نَجْعَل"}],"gloss":"belirtilmemiş bir yer adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kimliği belirtilmeyen bir yer için kullanılan özel addır."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynağın belirli yer kimliğini açıklamadan yalnızca yer adı diye sınıflandırdığı bu özel kullanım için uygundur.","boundary_detail":"Adın gösterdiği belirli yer açıklanmadığı için tanım bir yer kimliği uydurmaz ve sözü genel yer anlamına dönüştürmez.","branch_image_ar":"الجَعْلة اسم مكان","concept_gloss":"belirtilmemiş bir yer adı","contextual_glosses":[{"applicability":"Sözün genel yer anlamı taşımadığı, yalnız özel ad olarak kullanıldığı açıklanırken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözü kimliği belirtilmemiş özel bir yer adı olarak korur."},"facet_ids":["F001"],"text":"bir yerin adı","usage_role":"explanatory"}],"definition":"Kaynağın yalnızca bir yer adı olduğunu bildirdiği, gösterdiği yer açıklanmayan özel kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kimliği belirtilmeyen bir yer için kullanılan özel addır."}],"identity_rationale":"Tek kaynak ifadesi, sözün bir yer adı olduğunu açıkça bildirir ve bundan başka bir yer kimliği veya genel anlam vermez. Geçici çerçeve bu sınırlı tanıklığı doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kimliği belirtilmemiş bir yer adı"}],"lexicalization_note":"Dal yalnız belirli ad biçimine bağlıdır; genel veya yalın bir yer anlamı olarak genişletilemez.","neighbor_coverage_note":"Bütün adaylar incelendi; adayların her biri başka ve belirli bir yer adını veya genel yer alanını gösterir, ancak odak adın hangi yerle özdeş olduğunu kanıtlamaz; bu yüzden yayımlanabilir bir karşıtlık seçilmedi.","source_phrase_ar":"الجَعْلة اسم مكان (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık sözü bir yer adı olarak sınıflandırır, fakat hangi yeri gösterdiğini açıklamaz."}],"source_summary":"Bu kullanım tek bir tanıklıkla sınırlıdır ve yerin kimliğine ilişkin ek bir ortak açıklama bulunmaz.","sources":["MQ"],"what_is_ar":"يدخل فيه الجعلة حين يصرح المصدر بأنها اسم مكان.","what_is_not_ar":"لا يدخل فيه الجعلة الواحدة من النخل الصغار."},"support_links":[]},{"boundary":"Üç nitelik birlikte kurucudur; yalnız kısa, yalnız şişman veya yalnız inatçı olan biri bu dalın tam kapsamına girmez.","branch_kind":"bare","branch_ref":"root_000248/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"90:8:2:1","qac_word_ref":"90:8:2","surface_ar":"نَجْعَل"}],"gloss":"kısa, şişman ve inatçı olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kısa, şişman ve tartışmada inatla direnen kişiyi üç niteliği birlikte taşıyarak betimler."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişide beden kısalığı, şişmanlık ve inatçı çekişkenlik birlikte anlatıldığında tam karşılık verir.","boundary_detail":"Üç nitelik birlikte kurucudur; yalnız kısa, yalnız şişman veya yalnız inatçı olan biri bu dalın tam kapsamına girmez.","branch_image_ar":"قصر مع سمن ولجاج","concept_gloss":"kısa, şişman ve inatçı olma","contextual_glosses":[{"applicability":"Üç niteliği birlikte taşıyan bir kişiyi doğal cümle içinde nitelemek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiyi belirleyen üç kurucu niteliğin tümünü birlikte korur."},"facet_ids":["F001"],"text":"kısa, şişman ve inatçı biri","usage_role":"contextual"}],"definition":"Bir kişide kısalık, şişmanlık ve inatçı çekişkenliğin birlikte bulunmasını anlatan nitelemedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kısa, şişman ve tartışmada inatla direnen kişiyi üç niteliği birlikte taşıyarak betimler."}],"identity_rationale":"Tek kaynak ifadesi, bir kişide kısalık, şişmanlık ve inatçı çekişkenliğin birlikte bulunmasını tek bir betimleyici anlam olarak verir. Geçici çerçeve bu üç kurucu niteliği doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kısa, şişman ve inatçı kişi"}],"lexicalization_note":"Dal yalın betimleyici kullanıma dayanır ve özel bir söz öbeğiyle sınırlı değildir.","neighbor_coverage_note":"Bütün adaylar incelendi; kısa ve toplu kişi betimi ile genel beden dolgunluğu, üç niteliğin birlikte bulunması koşulunu en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bedensel kısalık ve şişmanlığa davranışsal inatçılığı ekler; komşu dal ise bedensel kalınlık ve gücü öne çıkarır.","focus_only":"Şişmanlık ile tartışmada inatla direnme niteliklerini kısalıkla birlikte gerektirir.","gloss":"kısa, kalın ve güçlü kişi","neighbor_only":"Kalın, güçlü ve toplu beden yapısını bildirir, fakat inatçılığı gerektirmez.","neighbor_ref":"root_001315/B008","relation_type":"near_synonym","shared_zone":"Kısa ve toplu beden yapısına sahip kişiyi betimlemede iki dal örtüşür."},{"boundary_match":"partial","distinction":"Odak dal üçlü bir kişi niteliğidir; komşu dal yalnız bedensel dolgunluğu seçer ve farklı canlı türlerine de uygulanabilir.","focus_only":"Kısalık ve inatçı çekişkenliği şişmanlıkla birlikte zorunlu kılar.","gloss":"bedenin dolgun ve şişman olması","neighbor_only":"İnsan veya hayvanda bedenin dolgunlaşıp yağlanmasını anlatır, boy ve huy koşulu taşımaz.","neighbor_ref":"root_000352/B006","relation_type":"near_neighbor","shared_zone":"Şişmanlık ve beden dolgunluğu anlam alanında iki dal buluşur."}],"source_phrase_ar":"الجعل القصر مع السمن واللجاج (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık üç niteliği ayırmadan kısa, şişman ve inatçı kişi betimlemesinde birleştirir."}],"source_summary":"Bu birleşik kişi betimlemesi tek bir tanıklığa dayanır; kısalık, şişmanlık ve inatçı çekişkenlik birlikte verilir.","sources":["TA"],"what_is_ar":"يدخل فيه الجعل بمعنى اجتماع القصر والسمن واللجاج في وصف الشخص.","what_is_not_ar":"لا يدخل فيه قصر النخل ولا الدويبة المسماة جعلا."},"support_links":[]},{"boundary":"Bu dal organın kendisi ve görme işleviyle sınırlıdır; doğrudan görme olayı, gözetme, zarar veren bakış ve benzetmeli kullanımlar ayrı dallardadır.","branch_kind":"bare","branch_ref":"root_001069/B001","candidate_links":[{"candidate_id":"cand_916eaf91310dddbb4892","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"gören göz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Görme yetisinin bedendeki organını ve bu organla gerçekleşen görmeyi belirtir."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Görme organının kendisini ve temel görme işlevini birlikte anlatan genel karşılıktır.","boundary_detail":"Bu dal organın kendisi ve görme işleviyle sınırlıdır; doğrudan görme olayı, gözetme, zarar veren bakış ve benzetmeli kullanımlar ayrı dallardadır.","branch_image_ar":"العين الناظرة","concept_gloss":"gören göz","definition":"Canlının çevresini görmesini sağlayan beden organı ve bu organın görme işlevidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Görme yetisinin bedendeki organını ve bu organla gerçekleşen görmeyi belirtir."}],"identity_rationale":"Kaynak sözü, gören canlının görmesini sağlayan beden organını ve onun görme işlevini açıkça bildirir; dalın sunulan kimliği bu çekirdeği doğru biçimde karşılar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"göz, görme organı"}],"lexicalization_note":"Tanım yalın dalın ortak anlamıyla sınırlıdır; yalnızca belirli bir söz kalıbına bağlı okuma eklenmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; organ ile görme olayının karışmasını en doğrudan giderdiği için yalnızca doğrudan görme dalı seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal gözü bir organ olarak gösterir; komşu dal ise organı değil, gözle gerçekleşen doğrudan görme ve karşılaşma olayını öne çıkarır.","focus_only":"Beden organının kendisini ve o organa bağlı görme yetisini adlandırır.","gloss":"göz ile doğrudan görme","neighbor_only":"Bir şeyi doğrudan gözle görme ya da yüz yüze karşılaşma olayını adlandırır.","neighbor_ref":"root_001069/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da görme deneyimine ve gören kişinin doğrudan algısına dayanır."}],"source_phrase_ar":"العين الناظرة لكل ذي بصر (maqayis;ayn); العين: حاسة الرؤية (sihah); العين: التي يبصر بها الناظر (tahdhib); العين الجارحة (mufradat)","source_summary":"Kaynaklar, anlamı gören canlının görme duyusunu taşıyan beden organında birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"العين الجارحة التي يبصر بها الناظر، وجمعها أعين وعيون وأعيان، وما يتصل بها من البصر والنظر.","what_is_not_ar":"ليس هذا فرع الإصابة بالعين، ولا الجاسوس، ولا عين الماء إلا من جهة التشبيه."},"support_links":["sup_38d621ad8676a270d8de"]},{"boundary":"Doğrudan görme çekirdektir; bilerek yapma ve görgüden sonra iz aramama yalnızca kaynakta verilen söz kalıplarına bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001069/B002","candidate_links":[{"candidate_id":"cand_f4758956817b3008e886","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"gözle görüp kesin biçimde tanıma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi aracısız biçimde gözle görmeyi veya onunla yüz yüze karşılaşmayı belirtir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli söz kalıplarında bilerek ve kesinlik içinde davranmayı ya da gördükten sonra ayrıca iz aramamayı belirtir."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Doğrudan görme çekirdeğini ve bundan doğan kesinliği birlikte anlatır; kalıba bağlı bilinçli davranış okumasını da dışlamaz.","boundary_detail":"Doğrudan görme çekirdektir; bilerek yapma ve görgüden sonra iz aramama yalnızca kaynakta verilen söz kalıplarına bağlıdır.","branch_image_ar":"المشاهدة بالعين","concept_gloss":"gözle görüp kesin biçimde tanıma","contextual_glosses":[{"applicability":"Bir şeyin dolaylı haberle değil doğrudan görülerek bilindiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğrudan görme ve görgüye dayalı kesinlik anlamını korur."},"facet_ids":["F001"],"text":"gözümle gördüm","usage_role":"contextual"}],"definition":"Bir şeyi gözle doğrudan görme, onunla yüz yüze gelme ve böylece dolaylı bilgiye gerek bırakmayan kesinlik edinmedir. Belirli söz kalıplarında işi bilerek ve emin olarak yapmayı da anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi aracısız biçimde gözle görmeyi veya onunla yüz yüze karşılaşmayı belirtir."},{"facet_id":"F002","role":"associated_use","statement":"Belirli söz kalıplarında bilerek ve kesinlik içinde davranmayı ya da gördükten sonra ayrıca iz aramamayı belirtir."}],"identity_rationale":"Kaynak sözü gözle doğrudan görmeyi ve yüz yüze karşılaşmayı çekirdek yapar; ayrıca belirli sözlerde bilerek, kesinlik içinde davranmayı ve gördükten sonra dolaylı iz aramamayı bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"gözle görerek, yüz yüze"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yüz yüze görerek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bilerek, görüp emin olarak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"gördükten sonra ayrıca iz aramam"}],"lexicalization_note":"Tanım, genel doğrudan görme anlamını söz kalıplarındaki bilerek yapma ve kesinlik uzantılarından ayırır; kalıba özgü kapsamı bütüne yaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; olay ile organ arasındaki temel sınırı en iyi gösterdiği için görme organı dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bir algılama ve karşılaşma olayıdır; komşu dal ise bu olayı gerçekleştiren beden organını adlandırır.","focus_only":"Gözle görme, yüz yüze gelme ve bundan doğan kesinlik olayını anlatır.","gloss":"doğrudan görme","neighbor_only":"Görmeyi sağlayan beden organının kendisini ve temel işlevini anlatır.","neighbor_ref":"root_001069/B001","relation_type":"near_neighbor","shared_zone":"İki dalın ortak alanı görme duyusu ve gören kişinin algısıdır."}],"source_phrase_ar":"رأيت الشيء عيانا أي معاينة (maqayis); لا أطلب أثرا بعد عين أي بعد معاينة (ayn;sihah;tahdhib); عيانا أي مواجهة (tahdhib); فعلت ذلك عمد عين (sihah)","source_summary":"Kaynaklar doğrudan görme ve yüz yüze gelmede birleşir; toplu kanıt ayrıca kesinlik ve bilinçli davranış bildiren kalıpları kapsar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"العيان والمعاينة والرؤية بالعين، ولقاء الشيء أو فعله على عين ويقين.","what_is_not_ar":"لا يدخل فيه حفظ المرء ورعايته، ولا الجاسوس، ولا العين الجارحة من حيث هي عضو فقط."},"support_links":["sup_77c357c1835b3de67c27"]},{"boundary":"Bu dal koruyucu gözetimle sınırlıdır; beden organı, gizlice haber toplama ve zarar veren bakış anlamlarını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_001069/B003","candidate_links":[{"candidate_id":"cand_9d5f774fa1f2635c73d0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"koruyup gözetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiyi göz önünde bulundurarak korumayı, kollamayı ve gözetmeyi belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Korunan kişiye değer verme, şefkat gösterme ve onu esirgeme tonunu taşır."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiyi göz önünde tutarak koruma, kollama ve ona özen gösterme alanının genel karşılığıdır.","boundary_detail":"Bu dal koruyucu gözetimle sınırlıdır; beden organı, gizlice haber toplama ve zarar veren bakış anlamlarını içermez.","branch_image_ar":"عين الحفظ والرعاية","concept_gloss":"koruyup gözetme","definition":"Birini göz önünde tutarak koruma, kollama ve sürekli gözetmedir; kimi sözlerde ona değer verip özen gösterme anlamı da taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiyi göz önünde bulundurarak korumayı, kollamayı ve gözetmeyi belirtir."},{"facet_id":"F002","role":"extension","statement":"Korunan kişiye değer verme, şefkat gösterme ve onu esirgeme tonunu taşır."}],"identity_rationale":"Kaynak sözü birini göz önünde tutarak koruma, kollama ve gözetmeyi bildirir; bazı kullanımlarda bu korumaya değer verme ve esirgeme de eşlik eder.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"korumam altında, özenle gözeterek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"gözümün önünde, korumam altında"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gözetimimiz ve korumamız altında"}],"lexicalization_note":"Tanım koruma çekirdeğiyle söz kalıplarındaki özen ve değer verme tonunu ayırır; kalıba bağlı tonu bütün kullanımlara yüklemez.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; koruyucu gözetim ile gizli bilgi toplama arasındaki amaç farkını gösteren dal seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dalın amacı gözetilen kişiyi korumaktır; komşu dalın amacı ise çevre hakkında bilgi toplayıp haber getirmektir.","focus_only":"Gözetilen kişiyi koruma, kollama ve ona özen gösterme amacı taşır.","gloss":"koruyucu gözetim","neighbor_only":"Gizlice bilgi toplamak ve başkalarına haber götürmek amacı taşır.","neighbor_ref":"root_001069/B005","relation_type":"same_field","shared_zone":"Her iki dalda da birini ya da çevreyi dikkatle izleme düşüncesi bulunur."}],"source_phrase_ar":"أنت على عيني، في الإكرام والحفظ جميعا (sihah); على عيني قصدت زيدا يريدون الإشفاق (tahdhib); فلان بعيني أي أحفظه وأراعيه (mufradat); بحيث نرى ونحفظ (mufradat)","source_summary":"Kaynaklar koruyup gözetme çekirdeğinde birleşir ve bazı kullanımlarda buna özen ile değer vermeyi ekler.","sources":["SI","TA","MU"],"what_is_ar":"استعمال العين في الحفظ والرعاية والمراقبة والإكرام، كقولهم فلان بعيني وعلى عيني.","what_is_not_ar":"ليس المراد هنا الجارحة المجردة، ولا عين الماء، ولا إصابة الحسد."},"support_links":["sup_f8422ab530e8f2864f3f"]},{"boundary":"Zarar veren etki kurucudur; yalnızca bakmak, doğrudan görmek ya da gözü beden organı olarak anmak bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001069/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"kötü bakışla zarar verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir insana veya nesneye belirli bir bakışla zarar verme ve onu olumsuz etkileme eylemidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemi yapanı, bu etkiden zarar göreni ve bu etkiyi sık doğuran kişiyi de kapsar."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bakışın bir kişiye ya da nesneye zarar verdiğinin düşünüldüğü eylem ve katılımcı alanının genel karşılığıdır.","boundary_detail":"Zarar veren etki kurucudur; yalnızca bakmak, doğrudan görmek ya da gözü beden organı olarak anmak bu dala girmez.","branch_image_ar":"الإصابة بالعين","concept_gloss":"kötü bakışla zarar verme","contextual_glosses":[{"applicability":"Bir bakışın kişiye ya da nesneye zarar verdiğine inanılan doğal anlatım bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bakıştan doğduğu düşünülen zarar verici etkiyi korur."},"facet_ids":["F001"],"text":"gözü değmek","usage_role":"contextual"}],"definition":"Bir insana veya nesneye kıskanç ya da kötü sayılan bakışla zarar verme ve onu olumsuz etkilemedir; bu eylemi yapan, ona uğrayan ve bunu sık yapan kişiler de aynı anlam alanında adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir insana veya nesneye belirli bir bakışla zarar verme ve onu olumsuz etkileme eylemidir."},{"facet_id":"F002","role":"extension","statement":"Eylemi yapanı, bu etkiden zarar göreni ve bu etkiyi sık doğuran kişiyi de kapsar."}],"identity_rationale":"Kaynak sözü bir insanı veya şeyi zarar verdiğine inanılan bakışla etkileme eylemini, bu eylemi yapanı, ona uğrayanı ve bunu sık yapan kişiyi birlikte tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"gözüyle zarar verdi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"gözü değen kimse"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"göz değmiş kimse"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"gözü sık değen kimse"}],"lexicalization_note":"Tanım eylem çekirdeğini yapan, etkilenen ve yatkın kişi biçimlerinden ayırır; türemiş kişi adlarını yalın anlam yerine geçirmez.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; zarar veren etkiyi sıradan görme organından ayıran karşılaştırma en yararlı sınırı verdi.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Bu dalda göz, zarar verdiği düşünülen bir etkinin kaynağıdır; komşu dalda ise yalnızca görmeyi sağlayan beden organıdır.","focus_only":"Bakışın başka bir kişiye ya da nesneye zarar verdiği düşünülen etkiyi anlatır.","gloss":"zarar veren bakış","neighbor_only":"Canlının çevresini görmesini sağlayan beden organını ve onun işlevini anlatır.","neighbor_ref":"root_001069/B001","relation_type":"thematic","shared_zone":"İki dal da göz ve bakma düşüncesini içeren aynı genel olay çevresinde bulunur."}],"source_phrase_ar":"عنت الرجل إذا أصبته بعينك (maqayis); عنت الشيء بعينه فأنا أعينه عينا وهو معيون (ayn); عنت الرجل: أصبته بعينى، فأنا عائن (sihah); عان الرجل فلانا يعينه عينا إذا ما أصابه بالعين (tahdhib); عنته: أصبته بعيني (mufradat)","source_summary":"Kaynaklar zarar verdiğine inanılan bakış eyleminde birleşir ve yapan ile etkilenen için türemiş kişi biçimlerini destekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"إصابة الإنسان أو الشيء بالعين، والعائن والمعيون والمعين وخبث العين.","what_is_not_ar":"لا يدخل فيه مجرد النظر أو المعاينة بلا إصابة."},"support_links":[]},{"boundary":"Bilgi toplama ve haber getirme amacı zorunludur; sıradan göz, koruyucu gözetim ve yalnızca bakma bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001069/B005","candidate_links":[{"candidate_id":"cand_8d5784c74959bf315ac2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"haber toplayan gizli gözcü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluk için gizlice bilgi toplamak ve haber getirmek üzere gönderilen gözcüyü belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çevreyi önceden yoklayarak uygun yeri araştırma ve topluluğa haber getirme eylemini kapsar."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir topluluk adına çevreyi araştıran, bilgi toplayan ve haber getiren kişi ile görevini kapsar.","boundary_detail":"Bilgi toplama ve haber getirme amacı zorunludur; sıradan göz, koruyucu gözetim ve yalnızca bakma bu dala girmez.","branch_image_ar":"العين الجاسوسة","concept_gloss":"haber toplayan gizli gözcü","definition":"Bilgi toplamak, çevreyi yoklamak ve haber getirmek üzere gönderilen gizli gözcü ya da öncüdür; ayrıca bu görevi üstlenip çevreyi araştırma eylemini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluk için gizlice bilgi toplamak ve haber getirmek üzere gönderilen gözcüyü belirtir."},{"facet_id":"F002","role":"extension","statement":"Çevreyi önceden yoklayarak uygun yeri araştırma ve topluluğa haber getirme eylemini kapsar."}],"identity_rationale":"Kaynak sözü haber toplamak üzere gönderilen gizli gözcü, öncü veya gözetmeni ve çevreyi yoklayıp haber getirme eylemini açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"gizli gözcü veya öncü"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"gizli gözcü"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bizim için çevreyi yoklayıp haber getirdi"}],"lexicalization_note":"Tanım görevli kişi anlamıyla çevreyi yoklayıp haber getirme eylemini ayrı tutar; türemiş eylemi yalın kişi anlamına genellemez.","neighbor_coverage_note":"Bütün adaylar incelendi; gizli bilgi toplama ile koruyucu gözetimi ayıran dal en açıklayıcı karşılaştırma olarak seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal bilgi edinmeye ve haber taşımaya yöneliktir; komşu dal ise bir kişiyi korumaya ve ona özen göstermeye yöneliktir.","focus_only":"Çevreyi araştırıp bilgi toplama ve başkalarına haber götürme amacı taşır.","gloss":"gizli haber gözcüsü","neighbor_only":"Gözetilen kişiyi koruma, kollama ve ona özen gösterme amacı taşır.","neighbor_ref":"root_001069/B003","relation_type":"same_field","shared_zone":"Her iki dalda da dikkatle izleme ve göz önünde bulundurma düşüncesi vardır."}],"source_phrase_ar":"العين الذي تبعثه يتجسس الخبر (maqayis); العين الذي تبعثه لتجسس الخبر (ayn); العين: الديدبان، والجاسوس (sihah); بعثنا عينا أي طليعة (tahdhib); قيل للمتجسس عين (mufradat)","source_summary":"Kaynaklar gizli gözcü veya öncü kişi anlamında birleşir ve bu kişinin çevreyi araştırıp haber getirme görevini de belirtir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"العين بمعنى الجاسوس أو الطليعة أو الرقيب الذي يبعث لتجسس الخبر والنظر للقوم.","what_is_not_ar":"لا يدخل فيه مطلق العين الجارحة ولا الحفظ الإكرامي إلا إن كان خبرا وتجسسا."},"support_links":["sup_f1fa3b6b909f8161d7f3"]},{"boundary":"Doğal su kaynağı ve ondan çıkan görünür akış esastır; su kabındaki delik, bulut ve yağmur bu dala dahil değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001069/B006","candidate_links":[{"candidate_id":"cand_edb46130327df37696aa","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"akan su kaynağı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yerden doğup akan suyun doğal çıkış yerini ve kaynağını belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynağa bağlı olarak gözle görülen akan suyu ve suyun akıp görünür olmasını kapsar."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yerden çıkan doğal su kaynağını, görünür akışını ve suyun ortaya çıkarak akmasını birlikte karşılar.","boundary_detail":"Doğal su kaynağı ve ondan çıkan görünür akış esastır; su kabındaki delik, bulut ve yağmur bu dala dahil değildir.","branch_image_ar":"منبع الماء الجاري","concept_gloss":"akan su kaynağı","definition":"Yerden çıkıp akan ve gözle görülen suyun doğal kaynağıdır; buna bağlı olarak görünür akan suyu ve suyun akıp ortaya çıkmasını da anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yerden doğup akan suyun doğal çıkış yerini ve kaynağını belirtir."},{"facet_id":"F002","role":"extension","statement":"Kaynağa bağlı olarak gözle görülen akan suyu ve suyun akıp görünür olmasını kapsar."}],"identity_rationale":"Kaynak sözü yerden çıkıp akan suyun kaynağını çekirdek yapar; görünür akan su ve suyun akması bu çekirdeğe bağlı biçimler olarak desteklenir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"akan su kaynağı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"göz önünde akan su"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"su aktı veya kaynağı ortaya çıktı"}],"lexicalization_note":"Tanım doğal kaynak çekirdeğiyle görünür akan su ve akma eylemini ayırır; türemiş akış anlamını bütün kullanımlara yaymaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; doğal su çıkışı ile kaptaki sızıntı deliğinin karışmasını önleyen karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal doğal bir su çıkışını adlandırır; komşu dal ise yapılmış bir kapta aşınma sonucu oluşan ve istenmeyen su sızıntısına yol açan yeri adlandırır.","focus_only":"Yerden doğal olarak çıkan ve akmaya başlayan suyun kaynağını anlatır.","gloss":"doğal su kaynağı","neighbor_only":"İncelmiş deri ya da su kabında su kaçıran bir delik veya zayıf yer anlatır.","neighbor_ref":"root_001069/B007","relation_type":"near_neighbor","shared_zone":"İki dalda da bir açıklıktan suyun çıkması ve göz benzeri bir yer düşüncesi bulunur."}],"source_phrase_ar":"العين الجارية النابعة من عيون الماء (maqayis); عين الماء (ayn;sihah); العين الينبوع الذي ينبع من الأرض ويجري (tahdhib); لمنبع الماء: عين (mufradat); ماء معين أي ظاهر للعيون (mufradat)","source_summary":"Kaynaklar yerden doğup akan suyun çıkış yerinde birleşir; toplu kanıt görünür suyu ve akma eylemini de bu çekirdeğe bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"عين الماء والينبوع والمنبع الجاري أو الظاهر للعيون، وما اشتق منه من ماء معين وعين القطر.","what_is_not_ar":"لا يدخل فيه السحاب أو المطر من جهة القبلة إلا إذا كان المقصود منبع الماء نفسه."},"support_links":["sup_7f724a8aedb1f4c92909"]},{"boundary":"İnsan yapımı deri ya da kaptaki incelme ve sızıntı esastır; doğal su kaynağı ve beden gözü yalnızca benzetme zeminidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001069/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"su sızdıran ince delik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Deri veya su kabında incelmiş, delinmiş ve suyu tutamayan yeri belirtir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaba su dökerek dikiş deliklerinin şişip kapanmasını sağlama işlemini belirtir."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Deri veya su kabındaki incelmiş sızıntı yerini ve onu suyla kapatma işlemine temel olan açıklığı anlatır.","boundary_detail":"İnsan yapımı deri ya da kaptaki incelme ve sızıntı esastır; doğal su kaynağı ve beden gözü yalnızca benzetme zeminidir.","branch_image_ar":"عين الجلد والسقاء","concept_gloss":"su sızdıran ince delik","definition":"Deri ya da su kabında incelip su sızdıran yuvarlak yer veya deliktir; ayrıca kaba su dökerek dikiş deliklerini şişirip kapatma işlemini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Deri veya su kabında incelmiş, delinmiş ve suyu tutamayan yeri belirtir."},{"facet_id":"F002","role":"associated_use","statement":"Kaba su dökerek dikiş deliklerinin şişip kapanmasını sağlama işlemini belirtir."}],"identity_rationale":"Kaynak sözü deri veya su kabındaki incelmiş yuvarlak yer ile su sızdıran deliği açıklar; kaba su dökerek dikiş deliklerini kapatma eylemi de buna bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"su kabındaki ince veya delik sızıntı yeri"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"incelip su tutamaz olmuş su kabı"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"dikiş delikleri kapansın diye kaba su döktü"}],"lexicalization_note":"Tanım kusurlu yer anlamıyla su dökerek dikiş deliklerini kapatma eylemini ayırır; eyleme özgü sonucu yalın anlam saymaz.","neighbor_coverage_note":"Adayların tamamı karşılaştırıldı; kap kusurunu doğal su kaynağından ayıran komşu en yararlı sınırı sundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bir kapta aşınma sonucu oluşan kusur ve sızıntıdır; komşu dal ise suyun doğal olarak doğduğu kaynak yeridir.","focus_only":"İncelmiş deri ya da su kabında oluşan ve su kaçıran kusurlu yeri anlatır.","gloss":"kaptaki sızıntı deliği","neighbor_only":"Yerden doğal biçimde çıkan ve akan suyun kaynağını anlatır.","neighbor_ref":"root_001069/B006","relation_type":"near_neighbor","shared_zone":"İki dal da bir açıklıktan su çıkması ve göz biçimli bir yer düşüncesini paylaşır."}],"source_phrase_ar":"عين السقاء (maqayis); تعين السقاء أي بلي ورق منه مواضع (ayn); بالجلد عين، وهي دوائر رقيقة (sihah); سقاء عين إذا رق فلم يمسك الماء (tahdhib); الثقب في المزادة تشبيها بها في الهيئة وفي سيلان الماء (mufradat)","source_summary":"Kaynaklar deri ve su kabındaki ince ya da delik yerde birleşir; toplu kanıt su dökerek bu açıklıkları kapatma işlemini de bildirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الثقب أو الموضع الرقيق في السقاء أو الجلد أو القربة، وما يسيل منه الماء أو ينسد بصب الماء.","what_is_not_ar":"ليس هو منبع ماء طبيعي ولا عين الإنسان إلا بالتشبيه في الهيئة والسيلان."},"support_links":[]},{"boundary":"Bu dal güneşin gövdesiyle sınırlıdır; insanın görme organı ve görme eylemi tanıma dahil değildir.","branch_kind":"bare","branch_ref":"root_001069/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"güneş yuvarlağı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güneşi ve onun yuvarlak görünen gövdesini adlandırır."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Güneşin gökte görünen yuvarlak gövdesini ve bu gövde üzerinden güneşin kendisini anlatır.","boundary_detail":"Bu dal güneşin gövdesiyle sınırlıdır; insanın görme organı ve görme eylemi tanıma dahil değildir.","branch_image_ar":"عين الشمس","concept_gloss":"güneş yuvarlağı","definition":"Güneşin kendisi, özellikle gökte yuvarlak görünen gövdesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güneşi ve onun yuvarlak görünen gövdesini adlandırır."}],"identity_rationale":"Kaynak sözü güneşin kendisini ve özellikle yuvarlak görünen gövdesini belirtir; insan gözüne benzerlik yalnızca adlandırmanın dayanağıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"güneşin gövdesi veya yuvarlağı"}],"lexicalization_note":"Tanım yalın dalın güneş gövdesi anlamıyla sınırlıdır ve yalnızca belirli bir söz kalıbından ek anlam çıkarmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; güneş gövdesi ile insan gözü arasındaki benzetme sınırını gösteren dal seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal benzetme yoluyla gökteki güneş gövdesini gösterir; komşu dal ise benzetmenin kaynağı olan görme organını anlatır.","focus_only":"Güneşin gökte yuvarlak görünen gövdesini adlandırır.","gloss":"güneşin yuvarlak gövdesi","neighbor_only":"Canlının görmesini sağlayan beden organını ve görme işlevini adlandırır.","neighbor_ref":"root_001069/B001","relation_type":"near_neighbor","shared_zone":"Güneş gövdesinin yuvarlak görünümü ile gözün biçimi arasında benzetme ilişkisi vardır."}],"source_phrase_ar":"عين الشمس مشبه بعين الإنسان (maqayis); عين الشمس صيخدها (ayn); العين: عين الشمس (sihah); طلعت العين وغابت العين، أي الشمس (tahdhib)","source_summary":"Kaynaklar güneşin kendisini ve yuvarlak gövdesini bu ad altında birleştirir; göz benzerliği adlandırmayı açıklar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"عين الشمس، أي جرمها أو مستديرها وصيخدها كما نصت المصادر.","what_is_not_ar":"ليس المراد الرؤية البشرية ولا عين الماء."},"support_links":[]},{"boundary":"Göz biçimli belirgin bir yer, çukur ya da eğim gereklidir; su kabındaki sızıntı deliği ve doğal su kaynağı kendi dallarında kalır.","branch_kind":"bare","branch_ref":"root_001069/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"göze benzer çukur, yer veya eğim","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesnede göz biçimine benzetilen çukur, belirgin nokta veya küçük eğimi belirtir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Diz, kuyu, terazi ve yay üzerindeki ayrı yerler bu biçimsel adlandırmanın örnekleridir."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Farklı nesnelerde biçimi ya da belirginliği gözle ilişkilendirilen yerlerin tamamını kapsayan açıklayıcı karşılıktır.","boundary_detail":"Göz biçimli belirgin bir yer, çukur ya da eğim gereklidir; su kabındaki sızıntı deliği ve doğal su kaynağı kendi dallarında kalır.","branch_image_ar":"النقرة أو الموضع العيني","concept_gloss":"göze benzer çukur, yer veya eğim","definition":"Bir nesnede göze benzetilen çukur, belirgin yer veya küçük eğimdir; dizin önündeki çukuru, kuyunun kaynak yerini, terazideki eğimi ve yayın mermi yatağını kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesnede göz biçimine benzetilen çukur, belirgin nokta veya küçük eğimi belirtir."},{"facet_id":"F002","role":"example","statement":"Diz, kuyu, terazi ve yay üzerindeki ayrı yerler bu biçimsel adlandırmanın örnekleridir."}],"identity_rationale":"Kaynak sözü farklı nesnelerde göze benzetilen çukur, yer veya küçük eğimi toplar; diz önü, kuyu, terazi ve yay örnekleri bu biçimsel çekirdeği somutlaştırır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"dizin önündeki çukur"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kuyunun kaynak yeri veya çukuru"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"terazideki küçük eğim veya dengesizlik"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"yayda merminin yerleştiği bölüm"}],"lexicalization_note":"Tanım yalın dalın nesnelerdeki göz benzeri yer anlamını korur; örneklerden herhangi birini bütün dalın tek anlamı yapmaz.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; genel göz biçimli yer ile su sızdıran kap kusuru arasındaki sınırı gösteren dal seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal su sızdırma koşulu olmadan çeşitli nesnelerdeki biçimsel yerleri kapsar; komşu dal yalnızca deri ve kaplardaki incelmiş sızıntı kusurudur.","focus_only":"Çeşitli nesnelerde göze benzetilen çukur, belirgin yer veya küçük eğimi kapsar.","gloss":"nesnedeki göz benzeri yer","neighbor_only":"Özellikle deri ya da su kabında incelerek su sızdıran kusurlu yeri kapsar.","neighbor_ref":"root_001069/B007","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir nesne üzerindeki yuvarlak veya çukur yer göz biçimine benzetilir."}],"source_phrase_ar":"عين الركية وهما عينان كأنهما نقرتان في مقدمها (maqayis); عين الركبة (ayn;sihah;tahdhib); في الميزان عين إذا رجحت إحدى كفتيه (tahdhib); عين القوس التي يقع فيها البندق (tahdhib)","source_summary":"Toplu kaynak kanıtı diz, kuyu, terazi ve yay üzerindeki göz benzeri çukur, yer veya eğimleri aynı biçimsel başlık altında toplar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"العين في الركبة والركية والقوس والميزان من جهة النقرة أو الموضع أو الميل الظاهر المشبه بالعين.","what_is_not_ar":"لا يدخل فيه ثقب السقاء السائل، ولا منبع الماء الجاري."},"support_links":[]},{"boundary":"Yönü belirli bulut ile uzun süren yağmur ayrı alt anlamlardır; doğal su kaynağı veya genel yağmur anlamı bütüne eklenmez.","branch_kind":"bare","branch_ref":"root_001069/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"belirli yönden gelen bulut veya dinmeyen yağmur","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Irak yönelimine göre kıblenin sağından veya kıble yönünden gelen bulutu belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Günlerce kesilmeden süren yağmuru ayrı bir hava durumu anlamı olarak belirtir."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yönle tanımlanan bulut anlamını ve günlerce kesilmeyen yağmur anlamını birbirine karıştırmadan birlikte gösterir.","boundary_detail":"Yönü belirli bulut ile uzun süren yağmur ayrı alt anlamlardır; doğal su kaynağı veya genel yağmur anlamı bütüne eklenmez.","branch_image_ar":"عين السحاب والمطر","concept_gloss":"belirli yönden gelen bulut veya dinmeyen yağmur","definition":"Belirli bir yönden gelen bulut ya da günlerce dinmeden süren yağmurdur; yönlü bulut ile uzun süreli yağış aynı dalın ayrı hava durumu görünümleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Irak yönelimine göre kıblenin sağından veya kıble yönünden gelen bulutu belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Günlerce kesilmeden süren yağmuru ayrı bir hava durumu anlamı olarak belirtir."}],"identity_rationale":"Kaynak sözü belirli bir yönden gelen bulutu ve günlerce kesilmeyen yağmuru aynı hava olayı alanında verir; sunulan dal iki alt kapsamı da doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kıblenin sağından gelen bulut"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"günlerce dinmeyen yağmur"}],"lexicalization_note":"Tanım yalın dalın yönlü bulut ve sürekli yağmur kapsamını korur; bunları başka su veya hava olaylarına genellemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hava kaynaklı su ile yer kaynağını ayıran karşılaştırma temel alan sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal gökten gelen bulut ve yağışı anlatır; komşu dal ise suyun yerden çıktığı doğal kaynağı anlatır.","focus_only":"Bulutun geliş yönünü veya yağmurun günlerce sürmesini anlatır.","gloss":"yönlü bulut ve sürekli yağmur","neighbor_only":"Suyun yerden doğal olarak çıkıp akmaya başladığı kaynak yerini anlatır.","neighbor_ref":"root_001069/B006","relation_type":"same_field","shared_zone":"Her iki dal suyun doğadaki görünümü ve hareketiyle ilgili aynı geniş alan içindedir."}],"source_phrase_ar":"العين السحاب ما جاء من ناحية القبلة (maqayis); العين من السحاب ما أقبل عن يمين القبلة (ayn); العين: ما عن يمين قبلة العراق (sihah;tahdhib); العين: مطر أيام لا يقلع (sihah;tahdhib)","source_summary":"Toplu kanıt, belirli yönden gelen bulut anlatımıyla günlerce kesilmeyen yağmur anlatımını aynı dalda fakat ayrı alt kapsamlar olarak verir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"العين من السحاب أو الجهة عن يمين قبلة العراق، وما يتصل بها من مطر العين أو المطر الدائم أياما.","what_is_not_ar":"ليس المراد عين الماء ولا عين الإنسان إلا بتشبيه بعيد كما في Maqayis."},"support_links":[]},{"boundary":"Elde bulunma ve para olma koşulları esastır; bu parayı sağlamak için kurulan satış işlemi ve genel olarak en iyi şey anlamı ayrı dallardadır.","branch_kind":"bare","branch_ref":"root_001069/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"hemen elde bulunan para","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Borçtan ayrılan, hemen elde bulunan ve kullanılmaya hazır parayı belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Altın ve altın parayı eldeki paranın özel gerçekleşmeleri olarak kapsar."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Borç veya uzaktaki mal karşısında hazır bulunan parayı, altın ve altın para örnekleriyle birlikte anlatır.","boundary_detail":"Elde bulunma ve para olma koşulları esastır; bu parayı sağlamak için kurulan satış işlemi ve genel olarak en iyi şey anlamı ayrı dallardadır.","branch_image_ar":"النقد الحاضر","concept_gloss":"hemen elde bulunan para","definition":"Borç ya da uzaktaki mal karşısında hemen elde bulunan para veya hazır servettir; altın ve altın para bu anlamın özel örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Borçtan ayrılan, hemen elde bulunan ve kullanılmaya hazır parayı belirtir."},{"facet_id":"F002","role":"specialization","statement":"Altın ve altın parayı eldeki paranın özel gerçekleşmeleri olarak kapsar."}],"identity_rationale":"Kaynak sözü borç veya uzaktaki mal karşısında hemen elde bulunan parayı çekirdek yapar; altın ve altın para bunun desteklenen özel gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"elde hazır bulunan para"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"altın para, eldeki para"}],"lexicalization_note":"Tanım yalın dalın eldeki para anlamını korur; belirli bir satış işlemine veya yalnızca altın paraya indirgenmez.","neighbor_coverage_note":"Adaylar arasında para varlığı ile para sağlama işlemini ayıran komşu, okuyucu için en olası karışmayı giderdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal hazır paranın kendisidir; komşu dal ise kişiye para sağlamak amacıyla kurulan belirli borçlandırma ve alım işlemidir.","focus_only":"Bir işlemden bağımsız olarak hemen elde bulunan para veya hazır serveti anlatır.","gloss":"eldeki hazır para","neighbor_only":"Ödemesi ertelenmiş bir alım veya satış yoluyla para sağlama işlemini anlatır.","neighbor_ref":"root_001069/B012","relation_type":"near_neighbor","shared_zone":"Her iki dal para elde etme ve borç ilişkilerinin bulunduğu alışveriş alanına girer."}],"source_phrase_ar":"العين وهو المال العتيد الحاضر (maqayis); عين غير دين أي مال حاضر (ayn); العين: الدينار؛ العين: المال الناض (sihah); العين: النقد (tahdhib); قيل للذهب: عين (mufradat)","source_summary":"Kaynaklar elde hazır bulunan para anlamında birleşir; toplu kanıt altın ve altın parayı bu genel anlamın özel örnekleri olarak verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"العين بمعنى المال الحاضر أو النقد أو الدينار أو الذهب، في مقابلة الدين والغائب.","what_is_not_ar":"لا يدخل فيه بيع العينة الخاص إلا من جهة حصول النقد، ولا يدخل خيار الشيء."},"support_links":[]},{"boundary":"Önceden verme veya ertelenmiş ödemeli alım yoluyla para sağlama işlemi zorunludur; yalnızca elde para bulunması bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001069/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"ertelenmiş ödemeli alımla para edinme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Önceden para verme veya bir satış düzeni yoluyla kişiye hemen para sağlama işlemini belirtir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin bir malı ödemesi sonraya bırakılmış biçimde satın almasını belirtir."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Önceden verilen parayı ve malın ödemesini sonraya bırakarak hemen para sağlama işlemini birlikte karşılar.","boundary_detail":"Önceden verme veya ertelenmiş ödemeli alım yoluyla para sağlama işlemi zorunludur; yalnızca elde para bulunması bu dala girmez.","branch_image_ar":"العينة والسلف","concept_gloss":"ertelenmiş ödemeli alımla para edinme","definition":"Bir kişiye önceden para verme ya da o kişinin ödemesi ertelenmiş biçimde mal alarak hemen para edinmesini sağlayan alışveriş düzenidir; ayrıca bu yolla mal alma eylemini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Önceden para verme veya bir satış düzeni yoluyla kişiye hemen para sağlama işlemini belirtir."},{"facet_id":"F002","role":"associated_use","statement":"Kişinin bir malı ödemesi sonraya bırakılmış biçimde satın almasını belirtir."}],"identity_rationale":"Kaynak sözü önceden verilen para ile bir malı ödemesi ertelenmiş biçimde alıp hemen para sağlama işlemini kapsar; adlandırmanın para elde etme sonucuna dayandığı da açıkça belirtilir.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"önceden verilen para veya para sağlamak için yapılan satış"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"malı ödemesi ertelenmiş olarak satın aldı"}],"lexicalization_note":"Tanım işlem adıyla ödemesi ertelenmiş alım eylemini ayırır; işleme özgü para sağlama sonucunu genel para anlamına yaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; işlem ile işlemin sağlayabildiği hazır para arasındaki farkı gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal parayı sağlayan belirli işlem ve alımdır; komşu dal ise işlemden bağımsız olarak elde hazır bulunan paranın kendisidir.","focus_only":"Ödemesi ertelenmiş alım veya önceden verme yoluyla para sağlama işlemini anlatır.","gloss":"alışveriş yoluyla para sağlama","neighbor_only":"Bir işlemden bağımsız olarak hemen elde bulunan parayı anlatır.","neighbor_ref":"root_001069/B011","relation_type":"near_neighbor","shared_zone":"Her iki dal eldeki para ile borç ve alışveriş arasındaki ilişkiyi konu edinir."}],"source_phrase_ar":"العينة السلف (maqayis;ayn;sihah); تعين فلان من فلان عينة (ayn); اعتان الرجل، إذا اشترى الشئ بنسيئة (sihah); عين التاجر يعين تعيينا وعينة قبيحة (tahdhib); سميت عينة لحصول النقد لطالب العينة (tahdhib)","source_summary":"Kaynaklar önceden para verme ve ertelenmiş ödemeli alım yoluyla para sağlama alanını birleştirir; adın hemen para elde etme sonucuna bağlandığını bildirir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"العينة والسلف والشراء بنسيئة أو بيع العينة الذي يحصل به النقد لطالبه.","what_is_not_ar":"لا يدخل فيه مطلق المال الحاضر إلا إذا كان في صيغة العينة أو السلف."},"support_links":[]},{"boundary":"Bire bir özdeşlik veya topluluktan belirleme zorunludur; şeyin üstün nitelikli bölümü ve önde gelen kişiler bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001069/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"şeyin bizzat kendisi ve belirlenmiş olanı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin yerine başkası olmayan kendi varlığını ve bire bir özdeşliğini belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyi bulunduğu topluluk içinden özel olarak belirleyip ayırma eylemini kapsar."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir varlığın kendi özdeşliğini, yerine başkasının geçmemesini ve topluluk içinden tek tek belirlenmesini birlikte anlatır.","boundary_detail":"Bire bir özdeşlik veya topluluktan belirleme zorunludur; şeyin üstün nitelikli bölümü ve önde gelen kişiler bu dala girmez.","branch_image_ar":"عين الشيء نفسه","concept_gloss":"şeyin bizzat kendisi ve belirlenmiş olanı","definition":"Bir varlığın başka örneği ya da karşılığı değil bizzat kendisi ve kendi özdeşliğidir; ayrıca onu bir topluluk içinden tek tek belirleyip ayırmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin yerine başkası olmayan kendi varlığını ve bire bir özdeşliğini belirtir."},{"facet_id":"F002","role":"extension","statement":"Bir şeyi bulunduğu topluluk içinden özel olarak belirleyip ayırma eylemini kapsar."}],"identity_rationale":"Kaynak sözü bir şeyin başka örneği veya karşılığı değil bizzat kendisini ve o şeyi bir topluluk içinden özel olarak belirlemeyi açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"şeyin bizzat kendisi"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"tam kendisi, yerine başkası değil"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"bir şeyi topluluk içinden belirleyip ayırma"}],"lexicalization_note":"Tanım şeyin kendisi anlamıyla söz kalıbındaki yerine başkası olmama ve belirleme eylemini ayırır; kalıp kapsamını bütüne yaymaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; özdeşlik ile üstün nitelik arasındaki temel ayrımı gösteren dal seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dalın ayrımı özdeşliğe dayanır ve değer yargısı taşımaz; komşu dalın ayrımı üstünlük ve seçkinlik değerlendirmesine dayanır.","focus_only":"Bir varlığın kendi özdeşliğini veya topluluk içinden belirlenmiş tek örneğini anlatır.","gloss":"bizzat kendisi","neighbor_only":"Bir şeyin ötekilerden daha iyi ve daha değerli olan bölümünü anlatır.","neighbor_ref":"root_001069/B014","relation_type":"same_field","shared_zone":"Her iki dal bir şeyi bulunduğu topluluktan ayırıp belirgin kılma düşüncesine yaklaşır."}],"source_phrase_ar":"عين الشيء نفسه (maqayis;sihah;tahdhib); خذ درهمك بعينه (maqayis); تعيين الشئ: تخصيصه من الجملة (sihah); دراهمك بأعيانها وهي أعيان دراهمك (tahdhib); ذات الشيء (mufradat)","source_summary":"Kaynaklar şeyin bizzat kendisi ve kendi özdeşliği anlamında birleşir; toplu kanıt bu özdeşliği bir kümeden belirleme eylemine bağlar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"عين الشيء بمعنى ذاته ونفسه وتخصيصه من الجملة، كدرهمك بعينه وأعيان الدراهم.","what_is_not_ar":"لا يدخل فيه خيار الشيء وجودته إلا إذا كان المراد الذات المعينة."},"support_links":[]},{"boundary":"Üstünlük ve seçilmiş iyi bölüm anlamı zorunludur; yalnızca şeyin kendisi olmak veya toplumsal olarak önde gelmek tek başına yeterli değildir.","branch_kind":"bare","branch_ref":"root_001069/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"bir şeyin en iyi ve seçkin bölümü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin içinden nitelikçe üstün, en iyi ve seçkin olanı belirtir."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Herhangi bir şeyin içinden nitelik ve değer bakımından üstün sayılan bölüm veya örnek için kullanılır.","boundary_detail":"Üstünlük ve seçilmiş iyi bölüm anlamı zorunludur; yalnızca şeyin kendisi olmak veya toplumsal olarak önde gelmek tek başına yeterli değildir.","branch_image_ar":"العين خيار الشيء","concept_gloss":"bir şeyin en iyi ve seçkin bölümü","definition":"Bir şeyin ötekilerden daha iyi, daha değerli ve seçkin olan bölümü veya örneğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin içinden nitelikçe üstün, en iyi ve seçkin olanı belirtir."}],"identity_rationale":"Kaynak sözü bir şeyin en iyi, seçkin ve değerli bölümünü ortak çekirdek olarak verir; sunulan dal kimliği bu nitelik üstünlüğünü doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"bir şeyin en iyi ve seçkin bölümü"}],"lexicalization_note":"Tanım yalın dalın en iyi bölüm anlamıyla sınırlıdır; belirli bir nesne, kişi topluluğu veya söz kalıbına daraltılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel nitelik üstünlüğü ile kişiler için yerleşmiş toplumsal ve akrabalık anlamlarını ayıran dal seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal her tür şeyde nitelikçe en iyi bölümü gösterir; komşu dal kişi topluluğundaki önderleri ve ayrı bir kardeşlik sınıfını adlandırır.","focus_only":"Herhangi bir şeyin nitelikçe en iyi ve seçkin bölümünü anlatır.","gloss":"en iyi seçilmiş bölüm","neighbor_only":"Bir topluluğun önde gelen kişilerini ve ayrıca belirli kardeşlik bağlarını anlatır.","neighbor_ref":"root_001069/B015","relation_type":"near_neighbor","shared_zone":"İki dalda da bir topluluk içinden öne çıkan veya üstün görülenleri ayırma düşüncesi vardır."}],"source_phrase_ar":"عينة كل شيء خياره (maqayis); العينة: خيار الشيء (tahdhib); عين الشئ: خياره (sihah); عينة المال أيضا: خياره (sihah); العين تشبيها بها في كونها أفضل الجواهر (mufradat)","source_summary":"Kaynaklar bir şeyin nitelikçe üstün, en iyi ve seçkin bölümü anlamında birleşir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"العين والعينة بمعنى خيار الشيء وجودته وأفضله.","what_is_not_ar":"لا يدخل فيه ذات الشيء المعينة ولا أعيان القوم إلا إذا كان المقصود الفضل والخيار."},"support_links":[]},{"boundary":"Toplumsal önderlik ile tam kardeşlik sınıfı birbirinden ayrılmalıdır; genel olarak en iyi mal veya herhangi bir şeyin kendisi bu dala girmez.","branch_kind":"bare","branch_ref":"root_001069/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"önde gelen kişiler veya anne baba bir kardeşler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun önde gelen, saygın ve seçkin kişilerini belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı anne ve babadan olan kardeşleri veya aynı kadının çocuklarını belirli bir akrabalık sınıfı olarak belirtir."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Toplumsal seçkinlik anlamını ve ayrı akrabalık kullanımındaki tam kardeşlik sınıfını birlikte, fakat ayrıştırarak gösterir.","boundary_detail":"Toplumsal önderlik ile tam kardeşlik sınıfı birbirinden ayrılmalıdır; genel olarak en iyi mal veya herhangi bir şeyin kendisi bu dala girmez.","branch_image_ar":"أعيان القوم والإخوة","concept_gloss":"önde gelen kişiler veya anne baba bir kardeşler","definition":"Bir topluluğun önde gelen ve saygın kişilerini belirtir. Ayrı bir akrabalık kullanımında aynı anne ve babadan olan kardeşleri ya da aynı kadının çocuklarını adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun önde gelen, saygın ve seçkin kişilerini belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı anne ve babadan olan kardeşleri veya aynı kadının çocuklarını belirli bir akrabalık sınıfı olarak belirtir."}],"identity_rationale":"Kaynak sözü bir topluluğun önde gelen seçkin kişileri ile aynı anne ve babadan olan kardeşleri ya da aynı kadının çocuklarını açıkça ayrı alt anlamlar olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"topluluğun önde gelen seçkin kişileri"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"anne baba bir kardeşler veya aynı kadının çocukları"}],"lexicalization_note":"Tanım yalın dalın iki kaynak alt anlamını ayrı tutar; toplumsal seçkinlik ile kardeşlik sınıfını tek bir genel üstünlük anlamında eritmez.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; kişi sınıfı ile genel nitelik üstünlüğü arasındaki sınırı en iyi gösteren dal yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın seçkinlik alt anlamı kişilere ve toplumsal konuma bağlıdır, ayrıca kardeşlik alt anlamı taşır; komşu dal her tür şeyin en iyi bölümüdür.","focus_only":"Kişiler için toplumsal önderlik ve ayrıca belirli bir kardeşlik sınıfı anlamlarını taşır.","gloss":"önde gelen kişiler","neighbor_only":"Herhangi bir şeyin nitelikçe en iyi ve seçkin bölümünü anlatır.","neighbor_ref":"root_001069/B014","relation_type":"near_neighbor","shared_zone":"İki dalda da bir bütün içinden öne çıkan veya seçkin görülenlerin ayrılması düşüncesi vardır."}],"source_phrase_ar":"أعيان القوم أي أشرافهم (maqayis;sihah;tahdhib); هؤلاء أعيان إخوتهم (maqayis); الأعيان: الأخوة بنو أب واحد وأم واحدة (sihah); أعيان بني الأم يتوارثون (tahdhib); أعيان القوم لأفاضلهم، وأعيان الإخوة (mufradat)","source_summary":"Toplu kanıt önde gelen kişiler anlamıyla aynı anne babadan kardeşler veya aynı kadının çocukları anlamını ayrı alt kapsamlar olarak sunar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"أعيان القوم أي أشرافهم، وأعيان الإخوة أو بني الأعيان لمن يجمعهم أب وأم أو امرأة واحدة بحسب نص المصدر.","what_is_not_ar":"لا يدخل فيه خيار المتاع ولا ذات الشيء، وإن كان القياس متقاربا في المصادر."},"support_links":[]},{"boundary":"Gözün genişliği ve güzelliği kurucudur; sıradan görme organı bu nitelikler olmadan dala girmez, kumaş örneği ise yalnızca ayrı sözlük biriminde işlenir.","branch_kind":"bare","branch_ref":"root_001069/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"geniş ve güzel gözlü olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gözün genişliğini, büyüklüğünü ve bu görünüşe bağlanan güzelliği belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu göz niteliğini taşıyan insanları ve yaban sığırını adlandırmaya uzanır."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gözün genişlik ve güzellik niteliğini, bu niteliği taşıyan insan ve hayvanları kapsayacak biçimde anlatır.","boundary_detail":"Gözün genişliği ve güzelliği kurucudur; sıradan görme organı bu nitelikler olmadan dala girmez, kumaş örneği ise yalnızca ayrı sözlük biriminde işlenir.","branch_image_ar":"سعة العين وحسنها","concept_gloss":"geniş ve güzel gözlü olma","definition":"İnsan veya hayvanda gözün geniş, büyük ve güzel olmasıdır; bu niteliği belirgin taşıyan kişileri ve yaban sığırını da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gözün genişliğini, büyüklüğünü ve bu görünüşe bağlanan güzelliği belirtir."},{"facet_id":"F002","role":"extension","statement":"Bu göz niteliğini taşıyan insanları ve yaban sığırını adlandırmaya uzanır."}],"identity_rationale":"Kaynak sözü insan veya hayvanda gözün geniş ve güzel olmasını temel alır; yaban sığırı ve geniş gözlü kadınlar bu niteliğe göre adlandırılan taşıyıcılardır.","lexical_glosses":[{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"geniş ve güzel gözlü"},{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"gözlerinin güzelliğiyle adlandırılan yaban sığırı"},{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"geniş ve güzel gözlü kadınlar"},{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"göz benzeri küçük kare desenli kumaş"}],"lexicalization_note":"Tanım yalın dalın geniş ve güzel göz niteliğini korur; ayrı sözlük birimindeki kumaş desenini dal çekirdeğine taşımaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; nitelikli göz görünüşünü genel görme organından ayıran komşu en temel sınırı sundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal gözün belirli genişlik ve güzellik niteliğini şart koşar; komşu dal ise bu nitelikler bulunmasa da görme organının genel adıdır.","focus_only":"Gözün geniş ve güzel oluşunu ve bu niteliği taşıyan varlıkları anlatır.","gloss":"geniş ve güzel gözlü","neighbor_only":"Gözün niteliklerinden bağımsız olarak görme organının kendisini anlatır.","neighbor_ref":"root_001069/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da aynı beden organına dayanır ve gözün fiziksel varlığını gerektirir."}],"source_phrase_ar":"توصف البقرة بسعة العين فيقال بقرة عيناء (maqayis); العين بقر الوحش (ayn;sihah;tahdhib); العين عظم سواد العين في سعتها (ayn); رجل أعين واسع العين (sihah;tahdhib); قاصرات الطرف عين؛ وحور عين (mufradat)","source_summary":"Kaynaklar geniş ve güzel göz niteliğinde birleşir; bu nitelik insanlara ve yaban sığırına bağlı adlandırmaları destekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"العين والعيناء والأعين وما دل على سعة العين وحسنها، ومنه بقر الوحش والحور العين بحسب نصوص المصادر.","what_is_not_ar":"لا يدخل فيه العين الجارحة مطلقا بلا وصف السعة والحسن، ولا الجاسوس."},"support_links":[]},{"boundary":"Herhangi bir kişi, ev halkı veya hazır topluluk anlamı esastır; seçkin kişiler ve gizli haber toplayan gözcü bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001069/B017","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","surface_ar":"عَيْنَيْنِ"}],"gloss":"kimse veya orada bulunan insanlar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"associated_use","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olumsuz anlatım içinde o yerde tek bir kimsenin bile bulunmadığını belirtir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir evin halkını veya bir arada bulunan insan topluluğunu belirtir."}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Olumsuz anlatımdaki herhangi bir kişiyi, ev halkını ve hazır bulunan topluluğu birlikte kapsar.","boundary_detail":"Herhangi bir kişi, ev halkı veya hazır topluluk anlamı esastır; seçkin kişiler ve gizli haber toplayan gözcü bu dala girmez.","branch_image_ar":"العين بمعنى الناس الحاضرون","concept_gloss":"kimse veya orada bulunan insanlar","definition":"Olumsuz bir söz kalıbında herhangi bir kimseyi belirtir; ayrıca bir evin halkını veya bir arada hazır bulunan insan topluluğunu adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"associated_use","statement":"Olumsuz anlatım içinde o yerde tek bir kimsenin bile bulunmadığını belirtir."},{"facet_id":"F002","role":"core","statement":"Bir evin halkını veya bir arada bulunan insan topluluğunu belirtir."}],"identity_rationale":"Kaynak sözü olumsuz anlatımda herhangi bir kimseyi, ayrıca ev halkını ve hazır bulunan bir topluluğu açıkça verir; sunulan dal bu insan kapsamlarını doğru toplar.","lexical_glosses":[{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"orada hiç kimse yok"},{"lexical_unit_id":"lu_044","rendering_kind":"ordinary","target_gloss":"ev halkı veya orada bulunanlar"},{"lexical_unit_id":"lu_045","rendering_kind":"ordinary","target_gloss":"bir topluluk içinde"}],"lexicalization_note":"Tanım olumsuz söz kalıbındaki herhangi bir kimse anlamıyla ev halkı ve topluluk anlamlarını ayırır; kalıp kapsamını yalın kullanıma yaymaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; sıradan hazır topluluk ile seçkin veya akrabalıkla belirlenmiş kişi grubunu ayıran dal seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal hazır bulunan insanları toplumsal derece gözetmeden kapsar; komşu dal önde gelen kişileri veya özel bir kardeşlik sınıfını seçer.","focus_only":"Herhangi bir kimseyi, ev halkını veya hazır bulunan insan topluluğunu anlatır.","gloss":"orada bulunan insanlar","neighbor_only":"Topluluğun önde gelen kişilerini ve ayrıca belirli kardeşlik bağlarını anlatır.","neighbor_ref":"root_001069/B015","relation_type":"same_field","shared_zone":"Her iki dal kişi topluluklarını ve bir grubun üyelerini adlandıran aynı geniş alandadır."}],"source_phrase_ar":"ما بها عين متحركة الياء تريد أحدا له عين (maqayis); ما بها عائن، وكذلك ما بها عين، أي أحد (sihah); العين، بالتحريك: أهل الدار (sihah); العين: أهل الدار (tahdhib); جاء فلان في عين، أي في جماعة (sihah)","source_summary":"Kaynaklar olumsuz anlatımdaki herhangi bir kimse anlamını ev halkı ve hazır topluluk anlamlarıyla birlikte insan varlığı ekseninde sunar.","sources":["MQ","SI","TA"],"what_is_ar":"العين بمعنى أحد أو إنسان أو أهل الدار أو جماعة حاضرة، كقولهم ما بها عين وجاء في عين.","what_is_not_ar":"لا يدخل فيه أعيان القوم بمعنى الأشراف، ولا العين الجاسوسة."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["90:8:1"],"branch_refs":[],"candidate_id":"cand_11705fb741aacbeab5ce","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:8:1:confirmatory-negative-question","source_type":"word_analysis","support_ids":["sup_56e7cf9f07b542321b4c","sup_6dc68a0579e0efc52a54"],"title":"confirmatory negative question","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:1","qac_refs":["90:8:1:1","90:8:1:2"],"status":"accepted"}},{"anchor_refs":["90:8:1"],"branch_refs":[],"candidate_id":"cand_897b16edabdb846a2458","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:8:1:discourse-boundary-and-forward-list","source_type":"word_analysis","support_ids":["sup_6dc68a0579e0efc52a54","sup_6fab52c918d811e65ec1"],"title":"challenge launches the faculty audit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:1","qac_refs":["90:8:1:1","90:8:1:2"],"status":"accepted"}},{"anchor_refs":["90:8:1"],"branch_refs":[],"candidate_id":"cand_5344cacb5c0e035c317e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:8:1:fused-form-and-audible-onset","source_type":"word_analysis","support_ids":["sup_6dc68a0579e0efc52a54","sup_f345ea069808db948299"],"title":"compact form makes challenge immediate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:1","qac_refs":["90:8:1:1","90:8:1:2"],"status":"accepted"}},{"anchor_refs":["90:8:1"],"branch_refs":[],"candidate_id":"cand_27f8db7853afb5b392c2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:8:1:jussive-scope-over-clause","source_type":"word_analysis","support_ids":["sup_6dc68a0579e0efc52a54","sup_b8c351b20d73f9bc75e3"],"title":"particle governs the whole evidentiary clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:1","qac_refs":["90:8:1:1","90:8:1:2"],"status":"accepted"}},{"anchor_refs":["90:8:2"],"branch_refs":[],"candidate_id":"cand_30819b38bcaf82e5790b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"90:8:2:beneficiary-object-valency","source_type":"word_analysis","support_ids":["sup_0e45ccf6274e96fe9181","sup_393e6847ede3459d3c16"],"title":"provider, recipient, and faculty relation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:2","qac_refs":["90:8:2:1"],"status":"accepted"}},{"anchor_refs":["90:8:2"],"branch_refs":[],"candidate_id":"cand_5b974a723aba33ac03dd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"90:8:2:divine-agency-active-form","source_type":"word_analysis","support_ids":["sup_0e45ccf6274e96fe9181","sup_83f23224ea6640973fd5"],"title":"active divine agency inside the verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:2","qac_refs":["90:8:2:1"],"status":"accepted"}},{"anchor_refs":["90:8:2"],"branch_refs":[],"candidate_id":"cand_a1a8d42f5c56a72ca3b4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"90:8:2:faculty-sequence-and-intertext","source_type":"word_analysis","support_ids":["sup_0e45ccf6274e96fe9181","sup_52584757b09490801d3a"],"title":"bodily provision opens toward guidance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:2","qac_refs":["90:8:2:1"],"status":"accepted"}},{"anchor_refs":["90:8:2"],"branch_refs":[],"candidate_id":"cand_db39e40aa0e49af534a4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"90:8:2:lam-governed-imperfect-challenge","source_type":"word_analysis","support_ids":["sup_0e45ccf6274e96fe9181","sup_809bb0564651b60db6e2"],"title":"completed provision as live challenge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:2","qac_refs":["90:8:2:1"],"status":"accepted"}},{"anchor_refs":["90:8:2"],"branch_refs":[],"candidate_id":"cand_7efe97e1d2090da9d37b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"90:8:2:make-place-appoint-provision","source_type":"word_analysis","support_ids":["sup_0e45ccf6274e96fe9181","sup_aa9ad38f040a58b3d6ad"],"title":"make-place-appoint range narrowed to provision","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:2","qac_refs":["90:8:2:1"],"status":"accepted"}},{"anchor_refs":["90:8:2"],"branch_refs":[],"candidate_id":"cand_014ba7554836e0bebfe7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"90:8:2:sound-and-boundary-link","source_type":"word_analysis","support_ids":["sup_0e45ccf6274e96fe9181","sup_a940413c58704cf79353"],"title":"making answers denied seeing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:2","qac_refs":["90:8:2:1"],"status":"accepted"}},{"anchor_refs":["90:8:2"],"branch_refs":[],"candidate_id":"cand_1e471a62e084f838ec22","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"90:8:2:staged-compact-governance","source_type":"word_analysis","support_ids":["sup_0e45ccf6274e96fe9181","sup_2a6903162eacb90e38c2"],"title":"verb stages dependence before the object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:2","qac_refs":["90:8:2:1"],"status":"accepted"}},{"anchor_refs":["90:8:3"],"branch_refs":[],"candidate_id":"cand_a7b497cff2c2c9badb7a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:8:3:beneficiary-assignment","source_type":"word_analysis","support_ids":["sup_996a9fe7925b982c180f","sup_af306c59c649dd678851"],"title":"benefit and assignment before the object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:3","qac_refs":["90:8:3:1","90:8:3:2"],"status":"accepted"}},{"anchor_refs":["90:8:3"],"branch_refs":[],"candidate_id":"cand_14ee82a82c77f5745823","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:8:3:clause-middle-hinge","source_type":"word_analysis","support_ids":["sup_996a9fe7925b982c180f","sup_c544b14117145109b510"],"title":"human placed between giver and gift","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:3","qac_refs":["90:8:3:1","90:8:3:2"],"status":"accepted"}},{"anchor_refs":["90:8:3"],"branch_refs":[],"candidate_id":"cand_362e1c21f58833419eca","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:8:3:compressed-bound-form","source_type":"word_analysis","support_ids":["sup_996a9fe7925b982c180f","sup_ff1b51a122f8e83a18db"],"title":"relation and recipient fused audibly","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:3","qac_refs":["90:8:3:1","90:8:3:2"],"status":"accepted"}},{"anchor_refs":["90:8:3"],"branch_refs":[],"candidate_id":"cand_ce1b35d1190f11785447","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:8:3:mediated-recipient-not-object","source_type":"word_analysis","support_ids":["sup_75991c5d0eae3fbc6678","sup_996a9fe7925b982c180f"],"title":"recipient role, not made object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:3","qac_refs":["90:8:3:1","90:8:3:2"],"status":"accepted"}},{"anchor_refs":["90:8:3"],"branch_refs":[],"candidate_id":"cand_7fa80f10b3c008513233","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:8:3:pronoun-bridge-through-discourse","source_type":"word_analysis","support_ids":["sup_394d6b5c87adae621986","sup_996a9fe7925b982c180f"],"title":"recipient bridges seeing and guidance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:3","qac_refs":["90:8:3:1","90:8:3:2"],"status":"accepted"}},{"anchor_refs":["90:8:3"],"branch_refs":[],"candidate_id":"cand_7ad5858a6df099f57bd4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:8:3:specific-pronoun-continuity","source_type":"word_analysis","support_ids":["sup_996a9fe7925b982c180f","sup_b363aac953b4edbfb0f1"],"title":"specific human carried by suffix","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:3","qac_refs":["90:8:3:1","90:8:3:2"],"status":"accepted"}},{"anchor_refs":["90:8:4"],"branch_refs":[],"candidate_id":"cand_e2cae1576f56397ad2f3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001069"],"scope":"focus_ayah","source_local_id":"90:8:4:assigned-not-instrumental-or-possessive","source_type":"word_analysis","support_ids":["sup_397a98ff2e52574db3fb","sup_afe00739005ad3abb7d4"],"title":"assigned gift rather than incidental tool","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:4","qac_refs":["90:8:4:1"],"status":"accepted"}},{"anchor_refs":["90:8:4"],"branch_refs":[],"candidate_id":"cand_010e39df9d0bc13f4185","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001069"],"scope":"focus_ayah","source_local_id":"90:8:4:audible-pairing-and-closure","source_type":"word_analysis","support_ids":["sup_afe00739005ad3abb7d4","sup_ced760c98e71b36b6179"],"title":"sound reinforces paired closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:4","qac_refs":["90:8:4:1"],"status":"accepted"}},{"anchor_refs":["90:8:4"],"branch_refs":[],"candidate_id":"cand_376cc1a4996ff95449e7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001069"],"scope":"focus_ayah","source_local_id":"90:8:4:boundary-from-concealment-to-evidence","source_type":"word_analysis","support_ids":["sup_afe00739005ad3abb7d4","sup_d327ec3c939f4eb8e70b"],"title":"denied seeing answered by eye-pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:4","qac_refs":["90:8:4:1"],"status":"accepted"}},{"anchor_refs":["90:8:4"],"branch_refs":[],"candidate_id":"cand_90101f5ae8cf2f7c6ecc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001069"],"scope":"focus_ayah","source_local_id":"90:8:4:dual-accusative-object","source_type":"word_analysis","support_ids":["sup_0ae5a566ccef9c3850fb","sup_afe00739005ad3abb7d4"],"title":"dual object made for the human","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:4","qac_refs":["90:8:4:1"],"status":"accepted"}},{"anchor_refs":["90:8:4"],"branch_refs":[],"candidate_id":"cand_2aa52fb7b941127c8587","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001069"],"scope":"focus_ayah","source_local_id":"90:8:4:dual-faculty-sequence","source_type":"word_analysis","support_ids":["sup_07390d0c9c79dbbb2019","sup_afe00739005ad3abb7d4"],"title":"paired faculty opens a dual sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:4","qac_refs":["90:8:4:1"],"status":"accepted"}},{"anchor_refs":["90:8:4"],"branch_refs":[],"candidate_id":"cand_280e97b554c66a33861c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001069"],"scope":"focus_ayah","source_local_id":"90:8:4:faculty-before-action","source_type":"word_analysis","support_ids":["sup_8ec1cfab31abf47447c7","sup_afe00739005ad3abb7d4"],"title":"faculty made before human seeing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:4","qac_refs":["90:8:4:1"],"status":"accepted"}},{"anchor_refs":["90:8:4"],"branch_refs":[],"candidate_id":"cand_f3d7eaee793ee2c50a5e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001069"],"scope":"focus_ayah","source_local_id":"90:8:4:faculty-intertexts","source_type":"word_analysis","support_ids":["sup_12c7c41a6b7d67697079","sup_afe00739005ad3abb7d4"],"title":"accountable endowment parallels","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:4","qac_refs":["90:8:4:1"],"status":"accepted"}},{"anchor_refs":["90:8:4"],"branch_refs":[],"candidate_id":"cand_b345a572fd733808a309","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001069"],"scope":"focus_ayah","source_local_id":"90:8:4:final-exhibit-placement","source_type":"word_analysis","support_ids":["sup_7e15632bcec0f9acaf4d","sup_afe00739005ad3abb7d4"],"title":"final word lands as proof","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:4","qac_refs":["90:8:4:1"],"status":"accepted"}},{"anchor_refs":["90:8:4"],"branch_refs":[],"candidate_id":"cand_9ebd5fa324d4d1df579e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001069"],"scope":"focus_ayah","source_local_id":"90:8:4:indefinite-concrete-pair","source_type":"word_analysis","support_ids":["sup_329534b3ee2120a368e9","sup_afe00739005ad3abb7d4"],"title":"ordinary pair made rhetorically sharp","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:4","qac_refs":["90:8:4:1"],"status":"accepted"}},{"anchor_refs":["90:8:4"],"branch_refs":[],"candidate_id":"cand_496f8d269125fdfbe83d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001069"],"scope":"focus_ayah","source_local_id":"90:8:4:root-field-narrowed-to-witnessing-eyes","source_type":"word_analysis","support_ids":["sup_57384d56adf5012d22da","sup_afe00739005ad3abb7d4"],"title":"eye sense with source and witness pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:8:4","qac_refs":["90:8:4:1"],"status":"accepted"}},{"anchor_refs":["90:8:2"],"branch_refs":[],"candidate_id":"cand_da4c451669ab0a09cf29","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"90:8:2:1","source_type":"qac_morpheme","support_ids":["sup_f12f904c11cf34014b9a"],"title":"QAC root occurrence: ج ع ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:8:4"],"branch_refs":[],"candidate_id":"cand_44e9b6180eeb5871828e","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001069"],"scope":"focus_ayah","source_local_id":"90:8:4:1","source_type":"qac_morpheme","support_ids":["sup_e1618ce107bafd8d7235"],"title":"QAC root occurrence: ع ي ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:8","branch_refs":["root_000248/B001","root_001069/B001"],"candidate_id":"cand_916eaf91310dddbb4892","commentary_obligation":"review","hft_ref":"hft_c08af13cdec19d3c6c82","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_made_pair_of_sight","source_type":"hft","support_ids":["sup_38d621ad8676a270d8de"],"title":"baseline_made_pair_of_sight","trust":"legacy_unbound"},{"anchor_refs":["90:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:8","branch_refs":["root_000248/B002","root_001069/B002"],"candidate_id":"cand_f4758956817b3008e886","commentary_obligation":"review","hft_ref":"hft_1c2dc3866c94a0ffb17f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_capacity_for_direct_presence","source_type":"hft","support_ids":["sup_77c357c1835b3de67c27"],"title":"baseline_capacity_for_direct_presence","trust":"legacy_unbound"},{"anchor_refs":["90:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:8","branch_refs":["root_000248/B001","root_001069/B003"],"candidate_id":"cand_9d5f774fa1f2635c73d0","commentary_obligation":"review","hft_ref":"hft_5fb27a2e4858b1dcaa8d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_pair_of_watchful_care","source_type":"hft","support_ids":["sup_f8422ab530e8f2864f3f"],"title":"baseline_pair_of_watchful_care","trust":"legacy_unbound"},{"anchor_refs":["90:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:8","branch_refs":["root_000248/B002","root_001069/B005"],"candidate_id":"cand_8d5784c74959bf315ac2","commentary_obligation":"review","hft_ref":"hft_7f7fae446214f1a540db","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_two_forward_sentinels","source_type":"hft","support_ids":["sup_f1fa3b6b909f8161d7f3"],"title":"baseline_two_forward_sentinels","trust":"legacy_unbound"},{"anchor_refs":["90:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:8","branch_refs":["root_000248/B001","root_001069/B006"],"candidate_id":"cand_edb46130327df37696aa","commentary_obligation":"review","hft_ref":"hft_4d9b10deb4f767bc6016","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_twin_visible_sources","source_type":"hft","support_ids":["sup_7f724a8aedb1f4c92909"],"title":"baseline_twin_visible_sources","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|A:INTG+","morpheme_role":"PREFIX","pos":"INTG","qac_ref":"90:8:1:1","qac_word_ref":"90:8:1","root_ar":"","surface_ar":"أَ"},{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"90:8:1:2","qac_word_ref":"90:8:1","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"90:8:2:1","qac_word_ref":"90:8:2","root_ar":"ج ع ل","surface_ar":"نَجْعَل"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"90:8:3:1","qac_word_ref":"90:8:3","root_ar":"","surface_ar":"لَّ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"90:8:3:2","qac_word_ref":"90:8:3","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","root_ar":"ع ي ن","surface_ar":"عَيْنَيْنِ"}],"word_analysis_qac_refs":[["90:8:1:1","90:8:1:2"],["90:8:2:1"],["90:8:3:1","90:8:3:2"],["90:8:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["90:8:1","90:8:2","90:8:3","90:8:4"]},"focus_surface_evidence":{"arabic_uthmani":"أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|A:INTG+","morpheme_role":"PREFIX","pos":"INTG","qac_ref":"90:8:1:1","qac_word_ref":"90:8:1","root_ar":"","surface_ar":"أَ"},{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"90:8:1:2","qac_word_ref":"90:8:1","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"90:8:2:1","qac_word_ref":"90:8:2","root_ar":"ج ع ل","surface_ar":"نَجْعَل"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"90:8:3:1","qac_word_ref":"90:8:3","root_ar":"","surface_ar":"لَّ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"90:8:3:2","qac_word_ref":"90:8:3","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"عَيْن","morph_features":"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:8:4:1","qac_word_ref":"90:8:4","root_ar":"ع ي ن","surface_ar":"عَيْنَيْنِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["90:8:1:1","90:8:1:2"],["90:8:2:1"],["90:8:3:1","90:8:3:2"],["90:8:4:1"]],"word_analysis_refs":["90:8:1","90:8:2","90:8:3","90:8:4"],"word_rows":[{"analysis_record_ref":"90:8:1","analytic_gloss_range_en":"interrogative hamza fused with negative jussive lam, forming a confirmatory challenge rather than an information-seeking question","analytic_root_gloss_range_en":null,"qac_refs":["90:8:1:1","90:8:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"أَلَمْ","transliteration":"a-lam"}},{"analysis_record_ref":"90:8:2","analytic_gloss_range_en":"divine making as provision and assignment: a completed endowment pressed as a present challenge, with the human marked as beneficiary and the eyes as concrete object","analytic_root_gloss_range_en":"range of making, placing, appointing, assigning, rendering, and setting into a state; local grammar selects provision and assignment, not naming, reward, auxiliary beginning, or unrelated nominal branches","qac_refs":["90:8:2:1"],"root":{"arabic":"ج ع ل","transliteration":"j-ʿ-l"},"surface":{"arabic":"نَجْعَل","transliteration":"najʿal"}},{"analysis_record_ref":"90:8:3","analytic_gloss_range_en":"lām phrase with third-person masculine singular suffix marking the same human as beneficiary, possessor, assigned recipient, and accountable user","analytic_root_gloss_range_en":null,"qac_refs":["90:8:3:1","90:8:3:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَّهُۥ","transliteration":"lahu"}},{"analysis_record_ref":"90:8:4","analytic_gloss_range_en":"two concrete eyes as the dual accusative object made for the human; an ordinary paired faculty that carries source, watching, and direct-witness pressure without leaving the bodily eye sense","analytic_root_gloss_range_en":"range around eye, spring or source, watching point, essence, specification, and direct beholding; local dual bodily context selects eyes while allowing source and witness pressure to remain rhetorically live","qac_refs":["90:8:4:1"],"root":{"arabic":"ع ي ن","transliteration":"ʿ-y-n"},"surface":{"arabic":"عَيْنَيْنِ","transliteration":"ʿaynayni"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["90:8"],"branch_refs":["root_000248/B001","root_001069/B001"],"candidate_id":"cand_916eaf91310dddbb4892","evidence_scope":"focus_ayah","hft_ref":"hft_c08af13cdec19d3c6c82","item_id":"baseline_made_pair_of_sight","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_made_pair_of_sight","support_id":"sup_38d621ad8676a270d8de"},{"anchor_refs":["90:8"],"branch_refs":["root_000248/B002","root_001069/B002"],"candidate_id":"cand_f4758956817b3008e886","evidence_scope":"focus_ayah","hft_ref":"hft_1c2dc3866c94a0ffb17f","item_id":"baseline_capacity_for_direct_presence","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_capacity_for_direct_presence","support_id":"sup_77c357c1835b3de67c27"},{"anchor_refs":["90:8"],"branch_refs":["root_000248/B001","root_001069/B003"],"candidate_id":"cand_9d5f774fa1f2635c73d0","evidence_scope":"focus_ayah","hft_ref":"hft_5fb27a2e4858b1dcaa8d","item_id":"baseline_pair_of_watchful_care","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_pair_of_watchful_care","support_id":"sup_f8422ab530e8f2864f3f"},{"anchor_refs":["90:8"],"branch_refs":["root_000248/B002","root_001069/B005"],"candidate_id":"cand_8d5784c74959bf315ac2","evidence_scope":"focus_ayah","hft_ref":"hft_7f7fae446214f1a540db","item_id":"baseline_two_forward_sentinels","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_two_forward_sentinels","support_id":"sup_f1fa3b6b909f8161d7f3"},{"anchor_refs":["90:8"],"branch_refs":["root_000248/B001","root_001069/B006"],"candidate_id":"cand_edb46130327df37696aa","evidence_scope":"focus_ayah","hft_ref":"hft_4d9b10deb4f767bc6016","item_id":"baseline_twin_visible_sources","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_twin_visible_sources","support_id":"sup_7f724a8aedb1f4c92909"}],"diagnostics":[],"lane_counts":{"global":19,"macro":6,"micro":5},"packet_summary":{"ayah_count":20,"focus_ref":"90:8","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ح ل ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000351","furuq_root_norm":"ح ل ل","furuq_source_root_norm":"ح ل ل","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000353","furuq_root_norm":"ح ل ي","furuq_source_root_norm":"ح ل ي","is_dominant":false,"target_occurrences":6,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"90:8","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":20,"unstructured_record_count":0},"identity":{"ayah_ref":"90:8","lane":"micro","linguistic_source_ref":"90:8","surface_ref":"90:8","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"90:8","target_tokens":[["Ona",["90:8:3"]],["iki",["90:8:4"]],["göz",["90:8:4"]],["vermedik",["90:8:1","90:8:2"]],["mi",["90:8:1"]]],"text":"Ona iki göz vermedik mi?"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":10,"id":"s090-p01-001-010","label":"Human toil and the two paths","number":1,"refs":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:4:dual-faculty-sequence","source_type":"word_analysis","support_id":"sup_07390d0c9c79dbbb2019","text":"{\"blocking_evidence\":null,\"headline\":\"paired faculty opens a dual sequence\",\"reader_payoff\":\"The reader notices a repeated pair-logic: two eyes lead to paired speech boundaries (90:9) and then two routes (90:10).\",\"reason\":\"The CRITICAL rows explicitly connect the dual eye pair to the following faculty inventory and the two-route ending in adjacent ayahs.\",\"representative_source_ids\":[\"QI-1caadd2a\",\"QT-7ce65e14\",\"QY-5767148f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:4:dual-accusative-object","source_type":"word_analysis","support_id":"sup_0ae5a566ccef9c3850fb","text":"{\"blocking_evidence\":null,\"headline\":\"dual object made for the human\",\"reader_payoff\":\"The reader notices that the proof is a countable pair governed as the direct object of the making verb.\",\"reason\":\"The local noun is dual accusative and is syntactically forced as the explicit direct object of the making verb.\",\"representative_source_ids\":[\"QG-210ded21\",\"QG-36c407ae\",\"MG-eede557f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:2","source_type":"word_analysis","support_id":"sup_0e45ccf6274e96fe9181","text":"{\"gloss_range\":\"divine making as provision and assignment: a completed endowment pressed as a present challenge, with the human marked as beneficiary and the eyes as concrete object\",\"prose\":\"{{ar:نَجْعَل}} ({{tr:najʿal}}) keeps the giver inside the verb: the first-person plural subject is fused into the active form, while {{ar:لَّهُۥ}} ({{tr:lahu}}) and {{ar:عَيْنَيْنِ}} ({{tr:ʿaynayni}}) make a three-part relation of provider, recipient, and faculty. Under {{ar:أَلَمْ}} ({{tr:a-lam}}), the formally imperfect verb carries a completed provision as a live premise for rebuke. The root's make-place-appoint range matters because the eyes are not treated as bare anatomy; they are installed and assigned for use. The shared ʿ sound links the making act to the eye object, and the discourse moves from the human's claim that no one saw him to the divine act that furnished seeing equipment. That bodily provision belongs to a wider endowment pattern: sensory and inner faculties are made in 67:23, the human is formed hearing-seeing in 76:2, and this sequence moves from organs to guidance in 90:10.\",\"root_display\":\"{{ar:ج ع ل}} ({{tr:j-ʿ-l}})\",\"root_gloss_range\":\"range of making, placing, appointing, assigning, rendering, and setting into a state; local grammar selects provision and assignment, not naming, reward, auxiliary beginning, or unrelated nominal branches\",\"surface_display\":\"{{ar:نَجْعَل}} ({{tr:najʿal}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:4:faculty-intertexts","source_type":"word_analysis","support_id":"sup_12c7c41a6b7d67697079","text":"{\"blocking_evidence\":null,\"headline\":\"accountable endowment parallels\",\"reader_payoff\":\"The reader sees 90:8 as part of a broader accountability pattern in which sensory faculties are made or granted, while this ayah isolates the eye pair as the first exhibit.\",\"reason\":\"The rows cite 67:23 and 90:9 as concrete parallels for made faculties and adjacent body-part sequencing.\",\"representative_source_ids\":[\"QI-32c81f9c\",\"MI-abe61cad\",\"ME-8097f9bd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:2:staged-compact-governance","source_type":"word_analysis","support_id":"sup_2a6903162eacb90e38c2","text":"{\"blocking_evidence\":null,\"headline\":\"verb stages dependence before the object\",\"reader_payoff\":\"The reader watches the clause move from giver to recipient to proof, so dependence is staged before the eyes are named.\",\"reason\":\"The verb heads the clause, precedes the beneficiary phrase, and governs the delayed direct object.\",\"representative_source_ids\":[\"QT-5d10495d\",\"QT-80b91132\",\"MT-e74467d1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:4:indefinite-concrete-pair","source_type":"word_analysis","support_id":"sup_329534b3ee2120a368e9","text":"{\"blocking_evidence\":null,\"headline\":\"ordinary pair made rhetorically sharp\",\"reader_payoff\":\"The reader notices that the ayah does not name abstract sight; it fixes attention on the ordinary human pair as a bestowed exhibit.\",\"reason\":\"The noun is concrete, dual, indefinite, and locally specified by the beneficiary relation that precedes it.\",\"representative_source_ids\":[\"QG-2973dbd5\",\"QG-82b854e8\",\"QF-1c249792\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:2:beneficiary-object-valency","source_type":"word_analysis","support_id":"sup_393e6847ede3459d3c16","text":"{\"blocking_evidence\":null,\"headline\":\"provider, recipient, and faculty relation\",\"reader_payoff\":\"The reader sees the eyes arrive already framed as provision for the human rather than as neutral organs simply mentioned in the world.\",\"reason\":\"The local frame has an explicit direct object and a lām prepositional complement governed by the making verb.\",\"representative_source_ids\":[\"QG-210209a5\",\"QG-f8f5c2a2\",\"QS-5319c0b9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:3:pronoun-bridge-through-discourse","source_type":"word_analysis","support_id":"sup_394d6b5c87adae621986","text":"{\"blocking_evidence\":null,\"headline\":\"recipient bridges seeing and guidance\",\"reader_payoff\":\"The reader follows the same human from imagining unseen privacy to receiving sight and then being guided toward two routes (90:10).\",\"reason\":\"The suffix resumes the prior human referent, and the CRITICAL rows explicitly connect the pronoun chain to the later guidance clause in 90:10.\",\"representative_source_ids\":[\"QB-0edc5bf5\",\"QB-ca6b225d\",\"QY-d64599ff\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:4:assigned-not-instrumental-or-possessive","source_type":"word_analysis","support_id":"sup_397a98ff2e52574db3fb","text":"{\"blocking_evidence\":null,\"headline\":\"assigned gift rather than incidental tool\",\"reader_payoff\":\"The reader sees the eyes first as an assigned endowment for the human, not as self-contained possession or a later instrument of use.\",\"reason\":\"The object is directly governed by the making verb, while possession or benefit is mediated through the preceding lām phrase.\",\"representative_source_ids\":[\"QG-2aa87e81\",\"QG-426be4f7\",\"QF-6a0e2b88\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:2:faculty-sequence-and-intertext","source_type":"word_analysis","support_id":"sup_52584757b09490801d3a","text":"{\"blocking_evidence\":null,\"headline\":\"bodily provision opens toward guidance\",\"reader_payoff\":\"The reader notices that this making verb begins an endowment sequence: eyes here, speech equipment next (90:9), and moral direction after that (90:10).\",\"reason\":\"The input explicitly marks the reading window across 90:8-10, and the CRITICAL rows give concrete parallels to 67:23, 76:2, and 90:10.\",\"representative_source_ids\":[\"QI-a4683ca0\",\"QI-b1481c58\",\"ME-9290940c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:1:confirmatory-negative-question","source_type":"word_analysis","support_id":"sup_56e7cf9f07b542321b4c","text":"{\"blocking_evidence\":null,\"headline\":\"confirmatory negative question\",\"reader_payoff\":\"The reader notices that the ayah is pressing acknowledgment of an evident gift, not asking for new information.\",\"reason\":\"The QAC and attachment evidence identify the opening as an interrogative plus negative jussive particle with rhetorical force.\",\"representative_source_ids\":[\"QG-38cf1937\",\"QS-00511d21\",\"QI-60fe04f1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:4:root-field-narrowed-to-witnessing-eyes","source_type":"word_analysis","support_id":"sup_57384d56adf5012d22da","text":"{\"blocking_evidence\":null,\"headline\":\"eye sense with source and witness pressure\",\"reader_payoff\":\"The reader hears the local eyes as bodily organs that also answer the denied-seeing scene with source, watching, and direct-witness pressure.\",\"reason\":\"The dual bodily context selects the eye sense, while the root family's source, watcher, specification, and direct-beholding associations survive as rhetorical pressure rather than alternate local referents.\",\"representative_source_ids\":[\"QS-21cb5ede\",\"QS-619470bf\",\"QS-f1c9246a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:1","source_type":"word_analysis","support_id":"sup_6dc68a0579e0efc52a54","text":"{\"gloss_range\":\"interrogative hamza fused with negative jussive lam, forming a confirmatory challenge rather than an information-seeking question\",\"prose\":\"{{ar:أَلَمْ}} ({{tr:a-lam}}) opens with challenge, not neutral report. The fused question-and-negation makes the hearer concede a provision already evident, and its compact onset checks the listener before any proof is named. Its force governs the making verb and reaches the final object, so the eyes are inside the question rather than outside it. Because the proof is withheld until the end of the clause, the opening particle turns the body-faculty list into an audit that begins here and continues into the next ayah (90:9).\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَلَمْ}} ({{tr:a-lam}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:1:discourse-boundary-and-forward-list","source_type":"word_analysis","support_id":"sup_6fab52c918d811e65ec1","text":"{\"blocking_evidence\":null,\"headline\":\"challenge launches the faculty audit\",\"reader_payoff\":\"The reader notices the shift from the human's private reckoning to a divine evidentiary challenge that spills into the next body-faculty item (90:9).\",\"reason\":\"The opening particle introduces the challenge, while the input marks the following ayah as continuing the same inventory without a new verb.\",\"representative_source_ids\":[\"QB-2b99935b\",\"QB-3496e1d1\",\"QY-fc37c0d9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:3:mediated-recipient-not-object","source_type":"word_analysis","support_id":"sup_75991c5d0eae3fbc6678","text":"{\"blocking_evidence\":null,\"headline\":\"recipient role, not made object\",\"reader_payoff\":\"The reader sees the human as dependent recipient rather than source or product of the making act.\",\"reason\":\"The prepositional phrase marks the beneficiary while the following dual noun is the explicit direct object.\",\"representative_source_ids\":[\"QG-f7211a1b\",\"MG-98b5caf8\",\"QI-7d67b622\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:4:final-exhibit-placement","source_type":"word_analysis","support_id":"sup_7e15632bcec0f9acaf4d","text":"{\"blocking_evidence\":null,\"headline\":\"final word lands as proof\",\"reader_payoff\":\"The reader feels the question withhold its evidence until the final word, where the eye pair becomes visible as the answer.\",\"reason\":\"The object follows the question particle, verb, and beneficiary phrase, so the concrete pair closes the ayah.\",\"representative_source_ids\":[\"QT-55d6db1f\",\"QT-7041053f\",\"MT-1ed29e62\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:2:lam-governed-imperfect-challenge","source_type":"word_analysis","support_id":"sup_809bb0564651b60db6e2","text":"{\"blocking_evidence\":null,\"headline\":\"completed provision as live challenge\",\"reader_payoff\":\"The reader notices that past provision is being activated now as an argument the hearer must answer.\",\"reason\":\"The imperfect verb is governed by the negative jussive particle, giving past-denial force inside a rhetorical question.\",\"representative_source_ids\":[\"QG-70909a46\",\"QF-660c4f3e\",\"MF-9f6b0828\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:2:divine-agency-active-form","source_type":"word_analysis","support_id":"sup_83f23224ea6640973fd5","text":"{\"blocking_evidence\":null,\"headline\":\"active divine agency inside the verb\",\"reader_payoff\":\"The reader notices that the proof is tied to the divine speaker's agency, not to an anonymous made-state.\",\"reason\":\"The verb carries first-person common plural subject agreement and active voice, with no overt subject noun needed.\",\"representative_source_ids\":[\"QG-e4df4171\",\"QG-f871578d\",\"QF-46ddb5fa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:4:faculty-before-action","source_type":"word_analysis","support_id":"sup_8ec1cfab31abf47447c7","text":"{\"blocking_evidence\":null,\"headline\":\"faculty made before human seeing\",\"reader_payoff\":\"The reader notices that the organ of seeing is first the patient of divine making before it becomes an instrument of human perception.\",\"reason\":\"The noun is the object of the making verb, and the surface chooses an anatomical noun rather than a perception verb.\",\"representative_source_ids\":[\"QS-9460b8b2\",\"QF-42167be7\",\"QB-75023510\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:3","source_type":"word_analysis","support_id":"sup_996a9fe7925b982c180f","text":"{\"gloss_range\":\"lām phrase with third-person masculine singular suffix marking the same human as beneficiary, possessor, assigned recipient, and accountable user\",\"prose\":\"{{ar:لَّهُۥ}} ({{tr:lahu}}) is the hinge between making and eyes. The lām phrase makes the faculty for him and within his sphere, while the suffix keeps the same singular human from the surrounding indictment in view. Its position before the object means the reader receives relation before anatomy: the eyes are already assigned to an accountable recipient before they are named. The compact preposition-suffix form and doubled lām make the short beneficiary marker carry audible weight, so relation and recipient are heard as one fused unit. The same pronoun chain also bridges from the denied seeing of the prior scene to guided direction later in the sequence (90:10).\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَّهُۥ}} ({{tr:lahu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:2:sound-and-boundary-link","source_type":"word_analysis","support_id":"sup_a940413c58704cf79353","text":"{\"blocking_evidence\":null,\"headline\":\"making answers denied seeing\",\"reader_payoff\":\"The reader hears and sees the movement from the human's claim that no one saw him to the divine act that furnished seeing equipment.\",\"reason\":\"The local wording links the making verb to the eye object, and the discourse boundary shifts from human reckoning to divine provision.\",\"representative_source_ids\":[\"QP-7f82ddf4\",\"QB-6910e237\",\"QY-33889dbf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:2:make-place-appoint-provision","source_type":"word_analysis","support_id":"sup_aa9ad38f040a58b3d6ad","text":"{\"blocking_evidence\":null,\"headline\":\"make-place-appoint range narrowed to provision\",\"reader_payoff\":\"The reader feels sight as a capacity placed and assigned for use, while the local object keeps the selected sense within bodily provision.\",\"reason\":\"V4 supports making, placing, assigning, and rendering branches for the root, but the local concrete object and beneficiary complement select provision of eyes rather than unrelated branches.\",\"representative_source_ids\":[\"QS-36e11d9c\",\"QS-42160ce4\",\"QS-82df68d5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:3:beneficiary-assignment","source_type":"word_analysis","support_id":"sup_af306c59c649dd678851","text":"{\"blocking_evidence\":null,\"headline\":\"benefit and assignment before the object\",\"reader_payoff\":\"The reader notices that the eyes are not abstract faculties; they are made for the human and assigned within his sphere of use.\",\"reason\":\"The attachment evidence treats the lām phrase as beneficiary, possession, or assignment complement of the making verb.\",\"representative_source_ids\":[\"QG-924080e4\",\"QG-a5a7c1d1\",\"QS-6238eb0b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:4","source_type":"word_analysis","support_id":"sup_afe00739005ad3abb7d4","text":"{\"gloss_range\":\"two concrete eyes as the dual accusative object made for the human; an ordinary paired faculty that carries source, watching, and direct-witness pressure without leaving the bodily eye sense\",\"prose\":\"{{ar:عَيْنَيْنِ}} ({{tr:ʿaynayni}}) lands as the concrete exhibit at the end of the question. Its dual accusative form makes the proof countable and governed: two eyes are the thing made for him, not merely instruments mentioned after the fact, and not a self-contained possession apart from the preceding beneficiary phrase. The wider root field narrows to the bodily eye sense here, but source, watcher, specification, and direct-witness pressure remain useful because the previous ayah had denied being seen. The pair also starts a repeated dual architecture: perception is followed by speech equipment (90:9) and then by two routes (90:10), with the -ayni cadence binding the sequence audibly. As in the faculty-endowment pattern of 67:23, ordinary anatomy becomes accountable provision, but this ayah isolates the eye pair as the first concrete exhibit.\",\"root_display\":\"{{ar:ع ي ن}} ({{tr:ʿ-y-n}})\",\"root_gloss_range\":\"range around eye, spring or source, watching point, essence, specification, and direct beholding; local dual bodily context selects eyes while allowing source and witness pressure to remain rhetorically live\",\"surface_display\":\"{{ar:عَيْنَيْنِ}} ({{tr:ʿaynayni}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:3:specific-pronoun-continuity","source_type":"word_analysis","support_id":"sup_b363aac953b4edbfb0f1","text":"{\"blocking_evidence\":null,\"headline\":\"specific human carried by suffix\",\"reader_payoff\":\"The reader keeps one accountable human in view instead of resetting the line into a generic statement about humanity.\",\"reason\":\"The third-person masculine singular suffix is strongly licensed as resuming the ongoing singular human referent.\",\"representative_source_ids\":[\"QG-097eebc2\",\"QG-ab2d82b5\",\"QG-c7b4e825\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:1:jussive-scope-over-clause","source_type":"word_analysis","support_id":"sup_b8c351b20d73f9bc75e3","text":"{\"blocking_evidence\":null,\"headline\":\"particle governs the whole evidentiary clause\",\"reader_payoff\":\"The reader sees the eyes as inside the challenge's scope, so the final object becomes the evidence by which assent is forced.\",\"reason\":\"The particle governs the following imperfect verb as jussive in force, and the verb governs the object at the end of the clause.\",\"representative_source_ids\":[\"QG-6113d1bd\",\"QG-721f9c4a\",\"QG-90d583d2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:3:clause-middle-hinge","source_type":"word_analysis","support_id":"sup_c544b14117145109b510","text":"{\"blocking_evidence\":null,\"headline\":\"human placed between giver and gift\",\"reader_payoff\":\"The reader experiences the human enclosed between divine act and bodily proof before any claim of autonomy can stand.\",\"reason\":\"The word sits between the governing verb and the delayed direct object, functioning as the clause's relational middle.\",\"representative_source_ids\":[\"QT-3155e0c5\",\"QT-712e08ee\",\"MT-70e6f510\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:4:audible-pairing-and-closure","source_type":"word_analysis","support_id":"sup_ced760c98e71b36b6179","text":"{\"blocking_evidence\":null,\"headline\":\"sound reinforces paired closure\",\"reader_payoff\":\"The reader hears the pair-shape through cadence as well as morphology, binding eyes, lips, and paths into one audible sequence (90:8-10).\",\"reason\":\"The rows identify repeated dual closure and internal cadence across the local word and adjacent ayah endings.\",\"representative_source_ids\":[\"QP-65f332f2\",\"QP-8931356f\",\"QH-21a20a34\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:4:boundary-from-concealment-to-evidence","source_type":"word_analysis","support_id":"sup_d327ec3c939f4eb8e70b","text":"{\"blocking_evidence\":null,\"headline\":\"denied seeing answered by eye-pair\",\"reader_payoff\":\"The reader sees the prior claim of being unseen answered by the displayed faculty through which seeing and witnessing happen.\",\"reason\":\"The previous ayah's denied seeing is answered by a concrete eye pair whose root field includes watching and direct witnessing pressure.\",\"representative_source_ids\":[\"QB-27bf5021\",\"QB-740ac2eb\",\"QY-829acf84\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:8:4:1","source_type":"qac_morpheme","support_id":"sup_e1618ce107bafd8d7235","text":"{\"lemma_ar\":\"عَيْن\",\"morph_features\":\"STEM|POS:N|LEM:Eayon|ROOT:Eyn|FD|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:8:4:1\",\"qac_word_ref\":\"90:8:4\",\"root_ar\":\"ع ي ن\",\"surface_ar\":\"عَيْنَيْنِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:8:2:1","source_type":"qac_morpheme","support_id":"sup_f12f904c11cf34014b9a","text":"{\"lemma_ar\":\"جَعَلَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|1P|MOOD:JUS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"90:8:2:1\",\"qac_word_ref\":\"90:8:2\",\"root_ar\":\"ج ع ل\",\"surface_ar\":\"نَجْعَل\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:1:fused-form-and-audible-onset","source_type":"word_analysis","support_id":"sup_f345ea069808db948299","text":"{\"blocking_evidence\":null,\"headline\":\"compact form makes challenge immediate\",\"reader_payoff\":\"The reader hears interrogation and negation arrive as one compact onset before any lexical proof is named.\",\"reason\":\"The surface word combines the interrogative entry with the negative particle, and the recitational onset supports the abrupt challenge.\",\"representative_source_ids\":[\"QF-359bc656\",\"QF-a808215b\",\"QP-02e1fc32\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:8:3:compressed-bound-form","source_type":"word_analysis","support_id":"sup_ff1b51a122f8e83a18db","text":"{\"blocking_evidence\":null,\"headline\":\"relation and recipient fused audibly\",\"reader_payoff\":\"The reader hears the short beneficiary marker carry unusual weight because relation and recipient are fused in one compact word.\",\"reason\":\"The word combines the preposition and suffix, and the doubled lām is part of the local recited form.\",\"representative_source_ids\":[\"QF-3bac75ca\",\"QF-579e3927\",\"QP-81841584\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ","ayah_ref":"90:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000248/B001","root_001069/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000248","role":"Bringing something into being supplies the deliberate production of the endowment.","root":"ج ع ل","source_ref":"90:8","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001069","role":"The bodily seeing eye identifies the made pair as organs of sight.","root":"ع ي ن","source_ref":"90:8","source_word_indices":["4"]}],"changed_reading":{"after":"The question points to an intentionally produced, beneficiary-directed pair of seeing organs.","before":"The question recalls an unspecified benefit given to the person."},"confidence":"strong","focus_anchor":"The first-person plural verb نَجْعَل, the beneficiary phrase لَّهُ, and the dual noun عَيْنَيْنِ.","mechanism":"Making or bringing into being is directed toward the bodily organ of sight, while the dual fixes the endowment as a coordinated pair rather than an abstract faculty.","model_id":"baseline_made_pair_of_sight"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_made_pair_of_sight","source_type":"hft","support_id":"sup_38d621ad8676a270d8de","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ","ayah_ref":"90:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000248/B002","root_001069/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000248","role":"Turning something into a state supplies the installation of an enduring perceptual condition.","root":"ج ع ل","source_ref":"90:8","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001069","role":"Seeing face to face turns the eyes from anatomy alone into access to manifest encounter.","root":"ع ي ن","source_ref":"90:8","source_word_indices":["4"]}],"changed_reading":{"after":"The two eyes are an installed capacity to stand in direct, eyewitness relation to what confronts the person.","before":"The two eyes are anatomical possessions."},"confidence":"medium","focus_anchor":"نَجْعَل can install a state, and عَيْنَيْنِ names a dual capacity for direct visual encounter.","mechanism":"The making is read as equipping the person with a standing condition of eyewitness access: the person is not merely alive but made able to meet what is present face to face.","model_id":"baseline_capacity_for_direct_presence"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_capacity_for_direct_presence","source_type":"hft","support_id":"sup_77c357c1835b3de67c27","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ","ayah_ref":"90:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000248/B001","root_001069/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000248","role":"Deliberate making keeps the custodial capacity grounded as a created endowment.","root":"ج ع ل","source_ref":"90:8","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001069","role":"The eye of watchful care supplies protection, supervision, and attentive regard as live functions of the pair.","root":"ع ي ن","source_ref":"90:8","source_word_indices":["4"]}],"changed_reading":{"after":"The eyes also stage a relation of care and custody, ambiguously received by and required from their beneficiary.","before":"The eyes are neutral instruments for receiving images."},"confidence":"medium","focus_anchor":"The dual عَيْنَيْنِ remains bodily while activating the eye's branch of watchful care and supervision.","mechanism":"The pair can carry a custodial reading in two directions at once: signs of care under which the person was made, and a capacity entrusted to the person for attentive care.","model_id":"baseline_pair_of_watchful_care"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_pair_of_watchful_care","source_type":"hft","support_id":"sup_f8422ab530e8f2864f3f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ","ayah_ref":"90:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000248/B002","root_001069/B005"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000248","role":"Making something assume a state supplies the body's equipment as a guarded, reconnaissance-capable condition.","root":"ج ع ل","source_ref":"90:8","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_001069","role":"The seeing scout makes each eye a forward sentinel serving the embodied person.","root":"ع ي ن","source_ref":"90:8","source_word_indices":["4"]}],"changed_reading":{"after":"The two eyes actively reconnoiter the world ahead of the person's movement and choice.","before":"The eyes register whatever happens to enter view."},"confidence":"medium","focus_anchor":"The pair عَيْنَيْنِ activates the eye as a scout or sentinel while remaining attached to the body's literal eyes.","mechanism":"The body is configured as a small protected domain whose two eyes go ahead of action, detecting approach, exposure, route, and risk.","model_id":"baseline_two_forward_sentinels"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_two_forward_sentinels","source_type":"hft","support_id":"sup_f1fa3b6b909f8161d7f3","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ","ayah_ref":"90:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000248/B001","root_001069/B006"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000248","role":"Bringing into being supplies the establishment of two embodied sources.","root":"ج ع ل","source_ref":"90:8","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_001069","role":"The springing water-eye makes flow and visible emergence latent within the bodily pair.","root":"ع ي ن","source_ref":"90:8","source_word_indices":["4"]}],"changed_reading":{"after":"The eyes can also be twin outward sources through which an inner response becomes visible.","before":"The eyes only take the visible world inward."},"confidence":"exploratory","focus_anchor":"The anatomical dual عَيْنَيْنِ also carries the root's image of a springing, visible water-source.","mechanism":"Without replacing the bodily sense, the paired eyes become two potential sources from which an inward condition can emerge outward, most concretely through tears.","model_id":"baseline_twin_visible_sources"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_twin_visible_sources","source_type":"hft","support_id":"sup_7f724a8aedb1f4c92909","trust":"legacy_unbound"}]}
</lane_packet_json>
