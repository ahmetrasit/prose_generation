# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **94:4**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s094-regular-20260912/s094/94_4/micro.discovery.json` and modify nothing
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
  "ayah_ref": "94:4",
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
{"branch_registry":[{"boundary":"Dalın çekirdeği biyolojik erkeklik karşıtlığıdır; doğum ve benzetme anlatımları ancak kendi sözlüksel yapıları içinde geçerlidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذِكْر","morph_features":"STEM|POS:N|VN|LEM:*ikor|ROOT:*kr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:4:3:1","qac_word_ref":"94:4:3","surface_ar":"ذِكْرَ"}],"gloss":"erkek cinsiyet ve erkek yavru doğurma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan ve hayvanlarda dişinin karşıtı olan erkek cinsiyet kategorisini belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Erkek bireylerin çoğulunu ve erkek olma durumunu adlandıran biçimleri kapsar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli çekimli biçimlerde bir dişinin erkek yavru doğurmasını veya çoğunlukla erkek yavru doğurmasını anlatır."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Erkeklik karşıtlığını ve buna bağlı doğurma türetimlerini birlikte göstermek gereken genel açıklamalarda kullanılır.","boundary_detail":"Dalın çekirdeği biyolojik erkeklik karşıtlığıdır; doğum ve benzetme anlatımları ancak kendi sözlüksel yapıları içinde geçerlidir.","branch_image_ar":"الذكر خلاف الأنثى","concept_gloss":"erkek cinsiyet ve erkek yavru doğurma","contextual_glosses":[{"applicability":"Bir insanın ya da hayvanın dişinin karşıtı olan cinsiyeti belirtilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Erkek yavru doğurmaya ilişkin türemiş kullanım alanını dışarıda bırakır.","preserves":"Bireyin erkek cinsiyetinden olması anlamını korur."},"facet_ids":["F001","F002"],"text":"erkek","usage_role":"general"},{"applicability":"Bir dişinin doğurduğu yavrunun erkek olduğunu bildiren çekimli yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel erkek cinsiyet kategorisini ve çoğul adlandırmaları kapsamaz.","preserves":"Doğum sonucunun erkek yavru olması anlamını korur."},"facet_ids":["F003"],"text":"erkek yavru doğurmak","usage_role":"contextual"}],"definition":"Canlıların dişinin karşısında yer alan erkek cinsiyetinden olmasıdır. Bu çekirdeğe bağlı biçimler, erkek yavru dünyaya getirmeyi veya bunu alışkanlıkla yapmayı da anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan ve hayvanlarda dişinin karşıtı olan erkek cinsiyet kategorisini belirtir."},{"facet_id":"F002","role":"extension","statement":"Erkek bireylerin çoğulunu ve erkek olma durumunu adlandıran biçimleri kapsar."},{"facet_id":"F003","role":"specialization","statement":"Belirli çekimli biçimlerde bir dişinin erkek yavru doğurmasını veya çoğunlukla erkek yavru doğurmasını anlatır."}],"identity_rationale":"Kaynak ifadesi dalın merkezini dişinin karşıtı olan erkek cinsiyet olarak kurar; çoğul adları ve erkek yavru doğurma anlatımları bu merkeze bağlı türetimlerdir. Ayrı sözlüksel birimlerde görülen anatomi ve erkeğe benzetme kullanımları çekirdek tanımı genişletmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"erkek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"erkek üreme organı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"erkeğin üreme organı çevresindeki organlar"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"erkekler veya erkeklik"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"erkek yavru doğurdu"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"çoğunlukla erkek yavru doğuran dişi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"erkek yapılı kadın veya dişi deve"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"gebe için kolay doğum ve erkek çocuk dileği"}],"lexicalization_note":"Tanım erkek cinsiyet çekirdeğini korur; doğurma, anatomi ve benzetme anlamları yalnız ilgili çekimli biçim ya da söz öbeğiyle sınırlandırılır.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; dört belirgin karşıtlık veya sınır ilişkisi seçildi, kalanlar anatomi, gelişim, bellek, söz ve belge alanlarında uzak ya da yinelenen eşleşmelerdi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Aynı cinsiyet ekseninde doğrudan karşıttırlar; biri erkek, öteki dişi tarafını seçer.","focus_only":"Odak dalı erkek cinsiyetini ve ona bağlı erkek yavru doğurma biçimlerini anlatır.","gloss":"erkek ile dişi","neighbor_only":"Komşu dal dişi cinsiyetini ve dişiliğe bağlı biçimleri anlatır.","neighbor_ref":"root_000058/B001","relation_type":"antonym","shared_zone":"İki dal canlıların biyolojik cinsiyet ayrımının karşıt uçlarını adlandırır."},{"boundary_match":"partial","distinction":"Odak biyolojik kategoridir ve hayvanları da kapsar; komşu ise insan kişisini ve toplumsal nitelendirmeleri öne çıkarır.","focus_only":"Odak, insanlarla sınırlı olmayan erkek cinsiyet kategorisini belirtir.","gloss":"erkek cinsiyet ile erkek kişi","neighbor_only":"Komşu, yetişkin erkek kişiyi ve ona yüklenen erkekçe nitelikleri belirtir.","neighbor_ref":"root_000546/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal insan söz konusu olduğunda erkek olma alanında buluşur."},{"boundary_match":"partial","distinction":"Cinsiyet kategorisi bir bütün olarak bireyi sınıflandırır; komşu ifade yalnız belirli bir organı adlandırır.","focus_only":"Odak dalı canlı bireyin erkek cinsiyetinden olmasını temel alır.","gloss":"erkeklik ile erkek anatomisi","neighbor_only":"Komşu dal yalnız erkek üreme organı için kullanılan örtmeceli bir adı verir.","neighbor_ref":"root_000597/B007","relation_type":"near_neighbor","shared_zone":"İki dal erkek cinsiyetle ilişkili bedensel alana temas eder."},{"boundary_match":"field_only","distinction":"Birinci dal cinsiyet sınıflamasıdır; ikinci dal ise cinsiyetten bağımsız varlıklara aktarılabilen güç ve sertlik niteliğidir.","focus_only":"Odak dalı gerçek erkek cinsiyetini ve buna bağlı doğum biçimlerini anlatır.","gloss":"erkeklik ile güçlü sertlik","neighbor_only":"Komşu dal nesne, bitki, insan veya olaylara yüklenen sertlik ve güç niteliğini anlatır.","neighbor_ref":"root_000516/B002","relation_type":"same_field","shared_zone":"Aynı kökten gelen iki dal bazı niteleme biçimlerinde erkeklik çağrışımını paylaşır."}],"source_phrase_ar":"الذكر خلاف الأنثى (sihah;tahdhib;mufradat)؛ الذكورة والذكور والذكران جمع الذكر (ayn;tahdhib;mufradat)؛ أذكرت ولدت ذكرا والمذكار تلد الذكور (maqayis;ayn;sihah;tahdhib;mufradat)","source_summary":"Kaynaklar erkek ile dişi arasındaki temel karşıtlıkta birleşir; ayrıca erkekler için kullanılan çoğul biçimleri ve erkek yavru doğurmaya ilişkin türetimleri aynı anlam alanına bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الذكر والذكورة والذكران وولادة الذكور والمذكار وما شبه بالذكر في الخلقة.","what_is_not_ar":"لا يدخل فيه مجرد التذكر أو الذكر باللسان ولا الصيت والشرف."},"support_links":[]},{"boundary":"Anlam bir cinsiyet adı değil, yalnız belirli söz öbeklerinde nesneye veya duruma yüklenen sertlik, keskinlik ve güç niteliğidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذِكْر","morph_features":"STEM|POS:N|VN|LEM:*ikor|ROOT:*kr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:4:3:1","qac_word_ref":"94:4:3","surface_ar":"ذِكْرَ"}],"gloss":"sert, keskin ve güçlü olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığa güçlü sertlik, keskinlik veya çetinlik niteliği yükler."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Demirin en sert ve kuru türünü, kılıcın keskinliğini ve bitkinin kalın sert yapısını belirtir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişi, gün, yol, felaket, yağmur, söz ve şiir için güç, şiddet veya zorluk anlatan aktarmalı bir niteleme olur."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel sertlik ile kişi ve durumlara aktarılan yoğun güç anlamlarını birlikte açıklarken kullanılır.","boundary_detail":"Anlam bir cinsiyet adı değil, yalnız belirli söz öbeklerinde nesneye veya duruma yüklenen sertlik, keskinlik ve güç niteliğidir.","branch_image_ar":"صلابة الذكر وحدته وشدته","concept_gloss":"sert, keskin ve güçlü olma","contextual_glosses":[{"applicability":"Demir, bitki veya benzeri maddi bir varlığın kuru, kalın ve dayanıklı yapısı anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kılıçtaki keskinliği ve kişi ya da olaylara aktarılan güç anlamını dışarıda bırakır.","preserves":"Maddi varlıktaki güçlü sertlik ve dayanıklılık niteliğini korur."},"facet_ids":["F001","F002"],"text":"çok sert ve dayanıklı","usage_role":"contextual"},{"applicability":"Kişi, gün, yol, felaket, yağmur, söz veya şiir yoğunluk ve zorluk bakımından nitelenirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Metal ve bitkideki somut sertlik ile kılıçtaki keskinliği kapsamaz.","preserves":"Aktarmalı güç, şiddet ve zorluk anlamını korur."},"facet_ids":["F001","F003"],"text":"çetin ve güçlü","usage_role":"contextual"}],"definition":"Belirli varlıkların sert, kuru, keskin, güçlü veya çetin oluşunu bildiren bir nitelemedir. Metal ve bitkide fiziksel dayanıklılığı, kişi, olay, hava ve sözde ise yoğun güç ya da zorluğu anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığa güçlü sertlik, keskinlik veya çetinlik niteliği yükler."},{"facet_id":"F002","role":"specialization","statement":"Demirin en sert ve kuru türünü, kılıcın keskinliğini ve bitkinin kalın sert yapısını belirtir."},{"facet_id":"F003","role":"extension","statement":"Kişi, gün, yol, felaket, yağmur, söz ve şiir için güç, şiddet veya zorluk anlatan aktarmalı bir niteleme olur."}],"identity_rationale":"Kaynak ifadesi demir, kılıç ve sert bitkilerdeki somut sertlik ile insan, gün, yol, felaket, yağmur, söz ve şiire aktarılan güç ve şiddeti aynı niteleme dalında toplar. Geçici çerçeve bu yapıyı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"demirin en sert ve kuru türü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"keskin ve sağlam kılıç"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kılıcın veya erkeğin keskinliği"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kalın ve sert otlar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"güçlü, yiğit ve onurlu adam"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"çetin ve korkutucu gün, yol veya felaket"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"şiddetli yağmur, sağlam söz veya güçlü şiir"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"tehlikeli, yalnız erkeklerin geçtiği veya sert ot bitiren ıssız ova"}],"lexicalization_note":"Somut ve aktarmalı nitelikler ayrı yüzler olarak korunur; hiçbiri bağlamdan bağımsız genel bir kök anlamı gibi sunulmaz.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; en açıklayıcı beş karşıt veya yakın sınır seçildi, öteki adaylar hava, madde ve kardeş dallar bakımından daha uzak ya da yinelenendi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak güçlü ve keskin ucu, komşu ise yumuşak ve zayıf ucu seçtiği için doğrudan karşıttırlar.","focus_only":"Odak dalı sertlik, keskinlik, güç ve çetinlik niteliğini taşır.","gloss":"sertlik ile yumuşaklık","neighbor_only":"Komşu dal yumuşaklık, kesmeyiş, zayıflık ve edilgenlik niteliğini taşır.","neighbor_ref":"root_000058/B002","relation_type":"antonym","shared_zone":"İki dal nesne ve kişilerin güç ile dayanıklılık eksenindeki karşıt uçlarını niteler."},{"boundary_match":"partial","distinction":"Odak keskinlik ve şiddetli durumlara daha açıktır; komşu sıkılık ve darbeye dayanma yeteneğine daha belirgin biçimde bağlıdır.","focus_only":"Odak, keskinlik ile gün, yol, yağmur, söz ve şiirdeki aktarmalı şiddeti de kapsar.","gloss":"çetin sertlik ile dayanıklılık","neighbor_only":"Komşu, darbeye dayanma ve sıkı dokulu sağlamlık gibi bedensel veya maddi dayanıklılığı öne çıkarır.","neighbor_ref":"root_000253/B002","relation_type":"near_synonym","shared_zone":"Her iki dal güçlü, sağlam ve kolay bozulmayan bir niteliği anlatabilir."},{"boundary_match":"partial","distinction":"Komşu kılıca özgü dar bir nitelemedir; odak ise aynı özelliği daha geniş bir varlık ve durum dizisine taşır.","focus_only":"Odak metal dışındaki varlıkları ve aktarmalı güç nitelemelerini de kapsar.","gloss":"genel sertlik ile keskin kılıç","neighbor_only":"Komşu yalnız bir kılıcın keskin ve kesici olmasını niteler.","neighbor_ref":"root_000258/B009","relation_type":"near_synonym","shared_zone":"Kılıç söz konusu olduğunda iki dal keskinlik ve güçlü kesme niteliğinde buluşur."},{"boundary_match":"partial","distinction":"Odak keskin ve çetin oluşa, komşu ise gücün sürmesi ve maddi sağlamlığa doğru ayrışır.","focus_only":"Odak keskinliği ve belirli söz öbeklerindeki çetinlik nitelemesini içerir.","gloss":"sert güç ile kalıcı sağlamlık","neighbor_only":"Komşu kalıcılık, semizlik ve kumaş dayanıklılığı gibi ek gelişmeleri içerir.","neighbor_ref":"root_000973/B007","relation_type":"near_synonym","shared_zone":"Her iki dal güç, sertlik ve dayanıklılık alanında önemli ölçüde örtüşür."},{"boundary_match":"field_only","distinction":"Sertlik niteliği cinsiyet bildirmez; erkek cinsiyet dalı da tek başına güç veya keskinlik yüklemez.","focus_only":"Odak çeşitli varlıklara yüklenen sertlik, güç ve keskinliği anlatır.","gloss":"güç niteliği ile erkek cinsiyet","neighbor_only":"Komşu erkek ile dişi arasındaki biyolojik cinsiyet karşıtlığını anlatır.","neighbor_ref":"root_000516/B001","relation_type":"same_field","shared_zone":"İki dal aynı kökten gelen ve kimi tarihsel nitelemelerde ilişkilenen anlam alanlarına aittir."}],"source_phrase_ar":"سيف مذكر ذو ماء وذو ذكر صارم (maqayis;sihah;mufradat)؛ الذكر من الحديد أيبسه وأشده (ayn;sihah;tahdhib)؛ ذكور البقل ما غلظ منه (maqayis;sihah;tahdhib;mufradat)؛ رجل ذكر قوي شجاع ويوم وطريق وداهية ومطر ذكر للشدة (tahdhib)","source_summary":"Kaynaklar sert demir, keskin kılıç ve kalın bitki örneklerini temel alır; aynı niteliği güçlü kişiye ve şiddetli ya da çetin olay, yol, hava ve söz anlatımlarına genişletir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الحديد الذكر والسيف المذكر وذكور البقل وما وصف بالشدة والقوة كالرجل الذكر واليوم والطريق والداهية والمطر.","what_is_not_ar":"لا يدخل فيه الذكر بمعنى الحفظ أو الكلام أو الكتاب."},"support_links":[]},{"boundary":"Bu dal zihindeki koruma ve geri çağırmayla sınırlıdır; bir sözü yalnız ağızdan söylemek veya kamuya duyurmak bu çekirdeğe girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B003","candidate_links":[{"candidate_id":"cand_d69b0821b2f5deaa9ae7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ذِكْر","morph_features":"STEM|POS:N|VN|LEM:*ikor|ROOT:*kr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:4:3:1","qac_word_ref":"94:4:3","surface_ar":"ذِكْرَ"}],"gloss":"akılda tutma ve yeniden hatırlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bilginin zihinde korunması ve unutmanın karşıtı olarak hazır bulunmasıdır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Unutulmuş veya gözden uzaklaşmış bir bilgiyi yeniden bilince getirme eylemidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaybolan bilgiyi zihinde arama ve öğrenileni bellekte tutmak için çalışma süreçlerini kapsar."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem bellekte koruma durumunu hem de unutulanı etkin biçimde geri çağırma sürecini birlikte anlatır.","boundary_detail":"Bu dal zihindeki koruma ve geri çağırmayla sınırlıdır; bir sözü yalnız ağızdan söylemek veya kamuya duyurmak bu çekirdeğe girmez.","branch_image_ar":"استحضار الشيء بعد النسيان أو مع الحفظ","concept_gloss":"akılda tutma ve yeniden hatırlama","contextual_glosses":[{"applicability":"Unutulmuş veya o sırada düşünülmeyen bir şey yeniden bilince geldiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bilgiyi sürekli akılda tutma ve ezber için çalışma yüzlerini dışarıda bırakır.","preserves":"Bilgiyi yeniden bilince getirme eylemini doğal biçimde korur."},"facet_ids":["F002"],"text":"hatırlamak","usage_role":"general"},{"applicability":"Bir bilgi ya da yükümlülüğün unutulmadan bellekte korunması istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Unutulanı etkin olarak geri çağırma ve arama sürecini kapsamaz.","preserves":"Bilginin bellekte hazır ve korunmuş bulunması anlamını korur."},"facet_ids":["F001"],"text":"aklında tutmak","usage_role":"contextual"}],"definition":"Bir şeyi unutmayacak biçimde zihinde tutmak veya unutulan bilgiyi yeniden bilince getirmektir. Buna bağlı kullanımlar, kayıp bilgiyi aramayı ve belleği korumak için çalışmayı da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bilginin zihinde korunması ve unutmanın karşıtı olarak hazır bulunmasıdır."},{"facet_id":"F002","role":"core","statement":"Unutulmuş veya gözden uzaklaşmış bir bilgiyi yeniden bilince getirme eylemidir."},{"facet_id":"F003","role":"specialization","statement":"Kaybolan bilgiyi zihinde arama ve öğrenileni bellekte tutmak için çalışma süreçlerini kapsar."}],"identity_rationale":"Kaynak ifadesi unutmanın karşıtı olarak bir şeyi zihinde tutmayı, unutulanı yeniden bilince getirmeyi ve kaybolan bilgiyi arayıp bulmayı birlikte verir. Geçici çerçeve zihinsel süreç ile korunmuş bellek durumunu doğru biçimde birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"hatırladı veya aklında tuttu"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"aklında"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"hatırlama"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ezberlemek için çalışma"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"belleği güçlü, yiğit veya iyi anılan adam"}],"lexicalization_note":"Zihinsel çekirdek korunur; akılda olma, yeniden hatırlama, ezber çalışması ve iyi bellek nitelemeleri kendi yapılarına bağlı yüzlerdir.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; bellek eksenini en iyi açıklayan beş ilişki seçildi, tanıma, düşünme, eski tanışıklık ve diğer kardeş dallar daha uzak veya yinelenen kaldı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak bellekte varlık ve erişimi, komşu ise aynı varlık ve erişimin kaybını bildirir.","focus_only":"Odak bir bilginin bellekte bulunmasını veya yeniden bilince gelmesini anlatır.","gloss":"hatırlama ile unutma","neighbor_only":"Komşu bir bilginin bellekten kaybolmasını ve sahibince erişilememesini anlatır.","neighbor_ref":"root_000913/B004","relation_type":"antonym","shared_zone":"İki dal bilginin bellekte bulunup bulunmaması ekseninde karşı karşıya gelir."},{"boundary_match":"partial","distinction":"Komşu daha çok bilginin yerleşik korunmasına, odak ise hem korumaya hem yeniden geri çağırmaya uzanır.","focus_only":"Odak unutulan bilgiyi etkin biçimde geri çağırma sürecini de içerir.","gloss":"hatırlama ile bellekte saklama","neighbor_only":"Komşu işitilen veya öğrenilen şeyin zihinde sağlam biçimde yerleşmesini öne çıkarır.","neighbor_ref":"root_000342/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bilginin unutulmadan zihinde bulunması alanında örtüşür."},{"boundary_match":"partial","distinction":"Ezbere bilme dış kaynağa ihtiyaç duymayan yerleşik öğrenmeyi gerektirir; odak böyle bir öğrenme koşulu olmadan da hatırlamayı kapsar.","focus_only":"Odak genel olarak akılda tutmayı ve unutulanı hatırlamayı kapsar.","gloss":"hatırlama ile ezbere bilme","neighbor_only":"Komşu bir metne bakmadan ezbere bilme durumuyla sınırlıdır.","neighbor_ref":"root_000970/B019","relation_type":"near_neighbor","shared_zone":"İki dal bilginin zihinde hazır bulunması bakımından buluşur."},{"boundary_match":"partial","distinction":"Komşu bir çalışma yöntemi ve yineleme sürecidir; odak ise yönteme bağlı olmadan bellek durumu ile geri çağırmayı anlatır.","focus_only":"Odak bilginin zihinde bulunması veya geri çağrılması sonucunu içerir.","gloss":"hatırlama ile zihinsel yineleme","neighbor_only":"Komşu bir sözü belleğe yerleştirmek için içten yineleme eylemini öne çıkarır.","neighbor_ref":"root_000562/B006","relation_type":"near_neighbor","shared_zone":"İçten yineleme, bilginin hatırlanmasını ve bellekte tutulmasını destekleyebilir."},{"boundary_match":"partial","distinction":"Odak zihinsel sonuç ve süreçtir; komşu bu sonucu meydana getiren neden veya hatırlatıcıdır.","focus_only":"Odak kişinin zihninde gerçekleşen hatırlama ve akılda tutma durumudur.","gloss":"hatırlama ile hatırlatma","neighbor_only":"Komşu bir başkasında ya da kişinin kendisinde hatırlamayı doğuran uyarı, araç veya eylemdir.","neighbor_ref":"root_000516/B009","relation_type":"near_neighbor","shared_zone":"İki dal unutulan bilginin yeniden zihinde hazır olması sonucunda buluşur."}],"source_phrase_ar":"ذكرت الشيء خلاف نسيته (maqayis;sihah)؛ الذكر الحفظ للشيء وهو مني على ذكر (ayn;tahdhib)؛ ذكر بالقلب والتذكر طلب ما فات (ayn;tahdhib;mufradat)","source_summary":"Kaynaklar unutmanın karşıtı olan zihinsel korumayı, unutulanı geri çağırmayı ve kaybolan bilgiyi yeniden bulma çabasını tek bir bellek alanında toplar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الحفظ والاستحضار بالقلب والتذكر والاستذكار وما يكون خلاف النسيان.","what_is_not_ar":"لا يدخل فيه مجرد جريان اللفظ على اللسان إذا لم يقصد حضور المعنى في النفس."},"support_links":["sup_96e23b245baec5fb564b"]},{"boundary":"Dal yalnız sözle anma yapısı içinde geçerlidir; içten hatırlama, genel konuşma yetisi ve anılmanın doğurduğu ün ayrı dallardır.","branch_kind":"collocation","branch_ref":"root_000516/B004","candidate_links":[{"candidate_id":"cand_2fe037f63489e9959902","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ذِكْر","morph_features":"STEM|POS:N|VN|LEM:*ikor|ROOT:*kr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:4:3:1","qac_word_ref":"94:4:3","surface_ar":"ذِكْرَ"}],"gloss":"bir şeyi sözle anma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi, nesne veya konuyu dilde söz olarak geçirmek ve adını söylemektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Söz aracılığıyla bir şeyi bildirme veya görünür kılma yönünü taşır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsanların kusurlarından arkalarında söz etme bağlamında çekiştirme anlamına gelir."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi, nesne veya konunun dilde adlandırılması ve söz konusu edilmesi gereken yapılarda kullanılır.","boundary_detail":"Dal yalnız sözle anma yapısı içinde geçerlidir; içten hatırlama, genel konuşma yetisi ve anılmanın doğurduğu ün ayrı dallardır.","branch_image_ar":"جريان الذكر على اللسان","concept_gloss":"bir şeyi sözle anma","contextual_glosses":[{"applicability":"Bir kişi ya da şeyin adı konuşma içinde geçirildiğinde doğal karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Her türlü söz sayılabilen geniş kaynak açıklamasını ve özel çekiştirme kullanımını belirtmez.","preserves":"Bir şeyi söz içinde adlandırma ve söz konusu etme eylemini korur."},"facet_ids":["F001","F002"],"text":"anmak","usage_role":"general"},{"applicability":"Bir insanın eksik ve kusurlarından o yokken söz etme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tarafsız veya olumlu sözle anma çekirdeğini dışarıda bırakır.","preserves":"İnsanları kusurlarıyla anma biçimindeki olumsuz özel kullanımı korur."},"facet_ids":["F003"],"text":"arkasından kusurlarını söylemek","usage_role":"contextual"}],"definition":"Bir şeyi dil aracılığıyla söz konusu etmek, adını söylemek veya sözle görünür kılmaktır. İnsanların kusurlarını arkalarından söyleme, bu eylemin olumsuz bağlama bağlı bir türüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi, nesne veya konuyu dilde söz olarak geçirmek ve adını söylemektir."},{"facet_id":"F002","role":"extension","statement":"Söz aracılığıyla bir şeyi bildirme veya görünür kılma yönünü taşır."},{"facet_id":"F003","role":"associated_use","statement":"İnsanların kusurlarından arkalarında söz etme bağlamında çekiştirme anlamına gelir."}],"identity_rationale":"Kaynak ifadesi bir şeyin dilde söz olarak geçirilmesini merkeze alır ve kusur söyleyerek çekiştirmeyi bağlama bağlı bir alt kullanım olarak verir. Her sözün bu adla anılabileceği geniş açıklama, dalı bütün konuşma eylemleriyle özdeşleştirmeden yorumlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"sözle anma"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"insanların arkasından kusurlarını söyleme"}],"lexicalization_note":"Tanım açıkça sözle anma yapısına bağlı tutulur; çekiştirme anlamı yalnız insanlardan kusurlarıyla söz etme bağlamında verilir.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; konuşma, övgü, yerme, hatırlama ve ünle en yararlı beş sınır seçildi, diğerleri özel konuşma türleri veya uzak kardeş anlamlardı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Dile getirme genel bir konuşma eylemidir; sözle anma ise belirli bir içeriği adlandırıp konu etmeye bağlıdır.","focus_only":"Odak belirli bir kişi, nesne veya konuyu söz içinde anmayı gerektirir.","gloss":"sözle anma ile dile getirme","neighbor_only":"Komşu, belirli bir içeriği anma koşulu olmadan konuşma seslerini dışa vurmayı anlatır.","neighbor_ref":"root_001364/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal düşüncenin dil ve ses aracılığıyla dışarı çıkarılmasını içerir."},{"boundary_match":"partial","distinction":"Övme zorunlu olarak olumlu değer yükler; odak dalı ise değer yönü taşımadan yalnız söz konusu etmeyi de kapsar.","focus_only":"Odak olumlu, tarafsız veya olumsuz olabilen genel sözle anmayı kapsar.","gloss":"anma ile övme","neighbor_only":"Komşu bir kişiyi en iyi nitelikleriyle överek yüceltme eylemidir.","neighbor_ref":"root_000933/B002","relation_type":"near_neighbor","shared_zone":"Övme sırasında kişi olumlu özellikleriyle söz içinde anılır."},{"boundary_match":"partial","distinction":"Odaktaki olumsuz kullanım arkadan kusur söylemeyle sınırlıdır; komşu daha geniş yerme ve saldırı davranışlarını içerir.","focus_only":"Odak tarafsız ve olumlu sözle anmayı da kapsayan daha geniş bir eylemdir.","gloss":"kusurla anma ile yerme","neighbor_only":"Komşu kusur arama, küçümseme ve gizli ya da açık saldırı yollarını içerir.","neighbor_ref":"root_001376/B001","relation_type":"near_neighbor","shared_zone":"İki dal bir kişiyi kusurları üzerinden söz konusu etme bağlamında örtüşebilir."},{"boundary_match":"partial","distinction":"Hatırlama zihinsel bir durum veya süreçtir; sözle anma ise dışa vurulan dilsel eylemdir.","focus_only":"Odak içeriğin dil aracılığıyla dışa vurulmasını gerektirir.","gloss":"sözle anma ile hatırlama","neighbor_only":"Komşu içerik söylenmese bile onun zihinde korunması veya geri çağrılmasıdır.","neighbor_ref":"root_000516/B003","relation_type":"near_neighbor","shared_zone":"Bir şeyi hatırlamak, onun daha sonra sözle anılmasına eşlik edebilir."},{"boundary_match":"partial","distinction":"Odak tekil dilsel eylemdir; komşu bu tür anmaların toplumsal sonucu olan kalıcı itibardır.","focus_only":"Odak bir kişi veya şeyden söz etme eylemini anlatır.","gloss":"anma eylemi ile iyi ün","neighbor_only":"Komşu sürekli ve olumlu anılmanın doğurduğu iyi ün, onur ve saygınlığı anlatır.","neighbor_ref":"root_000516/B007","relation_type":"near_neighbor","shared_zone":"Bir kişinin toplum içinde anılması onun ününün oluşmasına katkı sağlayabilir."}],"source_phrase_ar":"ثم حمل عليه الذكر باللسان (maqayis)؛ الذكر جري الشيء على لسانك (ayn;tahdhib)؛ ذكرته بلساني وبقلبي (sihah)؛ كل قول يقال له ذكر وذكر باللسان (mufradat)؛ يذكر الناس أي يغتابهم ويذكر عيوبهم (tahdhib)","source_summary":"Kaynaklar bir şeyin dilde söz olarak geçirilmesini ortak çekirdek sayar; insanları kusurlarıyla anmayı ise bağlama bağlı olumsuz bir kullanım olarak ekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه ذكر الشيء باللسان والقول والإظهار والتسمية، ومنه ذكر الناس بخير أو بسوء إذا دل السياق.","what_is_not_ar":"لا يدخل فيه الحفظ القلبي وحده ولا الشرف والصيت الناتج عن الذكر."},"support_links":["sup_b1ac507966f3e5c68cdd"]},{"boundary":"Her sözlü anma bu dala girmez; eylemin Tanrı'ya yönelmiş bir kulluk, övgü, yakarış veya itaat niteliği taşıması gerekir.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذِكْر","morph_features":"STEM|POS:N|VN|LEM:*ikor|ROOT:*kr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:4:3:1","qac_word_ref":"94:4:3","surface_ar":"ذِكْرَ"}],"gloss":"Tanrı'yı kulluk amacıyla anma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tanrı'ya yönelmiş bir kulluk ve bilinçli anma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yakarış, övgü, yüceltme ve şükretme bu kulluk yöneliminin sözlü veya içsel biçimleridir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Buyruklara uyma ve dinî metni bu amaçla okuma da aynı kulluk alanında değerlendirilir."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tanrı'ya yönelen yakarış, övgü, şükür, itaat ve dinî okuma eylemlerini ortak bir kulluk kavramında toplar.","boundary_detail":"Her sözlü anma bu dala girmez; eylemin Tanrı'ya yönelmiş bir kulluk, övgü, yakarış veya itaat niteliği taşıması gerekir.","branch_image_ar":"ذكر الله عبادة وثناء ودعاء","concept_gloss":"Tanrı'yı kulluk amacıyla anma","contextual_glosses":[{"applicability":"Tanrı'ya bilinçli biçimde yönelen övgü, yakarış veya kulluk eylemi genel olarak belirtilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Buyruklara uyma ve dinî metin okuma gibi davranışsal gerçekleşmeleri açıkça belirtmez.","preserves":"Tanrı'ya yönelen bilinçli anma ve kulluk çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"Tanrı'yı anmak","usage_role":"general"},{"applicability":"Kulluğun sözlü yakarış, övgü ve yüceltme yönü bağlamda baskın olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Şükretme, itaat ve dinî okuma gibi öteki gerçekleşmeleri kapsamaz.","preserves":"Yakarış, övgü ve yüceltme biçimindeki kulluk eylemlerini korur."},"facet_ids":["F002"],"text":"yakarışta ve övgüde bulunmak","usage_role":"contextual"}],"definition":"Tanrı'yı kulluk amacıyla anmak; ona yönelen yakarış, övgü, yüceltme, şükretme, buyruklara uyma ve dinî metin okuma eylemlerini yerine getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tanrı'ya yönelmiş bir kulluk ve bilinçli anma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Yakarış, övgü, yüceltme ve şükretme bu kulluk yöneliminin sözlü veya içsel biçimleridir."},{"facet_id":"F003","role":"extension","statement":"Buyruklara uyma ve dinî metni bu amaçla okuma da aynı kulluk alanında değerlendirilir."}],"identity_rationale":"Kaynak ifadesi Tanrı'yı anmaya yönelen kulluk eylemlerini; yakarış, övgü, yüceltme, şükretme, buyruklara uyma ve dinî metin okuma örnekleriyle açıklar. Geçici çerçeve bu ibadet odaklı kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kulluk amacıyla anma, yakarış, övgü, şükretme ve itaat"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"Tanrı'yı kulluk, övgü ve yakarışla anma"}],"lexicalization_note":"Genel kulluk anlamı ile Tanrı'yı anma söz öbeği ayrılır; dinî metin okuma ancak bu kulluk yönelimi içinde değerlendirilir.","neighbor_coverage_note":"Sunulan on beş adayın tümü değerlendirildi; genel anma, belirli yakarışlar ve ibadet sessizliğiyle ilgili dört ilişki seçildi, kalan adaylar aynı sahnenin daha uzak parçalarıydı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Genel sözle anma yalnız dilsel eylemdir; odak dalı ise belirli bir yöneliş ve kulluk amacı gerektirir.","focus_only":"Odak Tanrı'ya yönelmiş kulluk, yakarış, övgü ve itaat koşulunu taşır.","gloss":"kulluk amacıyla anma ile sözle anma","neighbor_only":"Komşu herhangi bir kişi, nesne veya konuyu söz içinde anmayı kapsar.","neighbor_ref":"root_000516/B004","relation_type":"near_neighbor","shared_zone":"Tanrı'yı sözle anma, her iki dalın kesişebildiği bir gerçekleşmedir."},{"boundary_match":"thematic_only","distinction":"Belirli kabul dileği kendi kalıplaşmış işlevine sahiptir; odak ise tek bir söz kalıbına bağlı olmayan geniş kulluk alanıdır.","focus_only":"Odak çok sayıda sözlü ve davranışsal kulluk biçimini kapsar.","gloss":"genel kulluk ile kabul dileği","neighbor_only":"Komşu yakarışın kabulü için söylenen belirli bir karşılıkla sınırlıdır.","neighbor_ref":"root_000054/B003","relation_type":"thematic","shared_zone":"İki dal yakarış ve dinsel söz eylemi bağlamında aynı sahnede yer alabilir."},{"boundary_match":"thematic_only","distinction":"Komşu isteğin konusunu su ve yağmurla sınırlar; odak ise konu sınırlaması olmayan kulluk yönelimidir.","focus_only":"Odak övgü, şükür, itaat ve farklı yakarış türlerini birlikte kapsar.","gloss":"kulluk ile yağmur dileği","neighbor_only":"Komşu özellikle su ve yağmur istemeye yönelik yakarıştır.","neighbor_ref":"root_000722/B006","relation_type":"thematic","shared_zone":"Yağmur isteme eylemi Tanrı'ya yönelen bir yakarış olarak odak alanında gerçekleşebilir."},{"boundary_match":"thematic_only","distinction":"Sessizlik ibadetin düzenleyici bir koşuludur; odak ise Tanrı'ya yönelen anma ve kulluk eyleminin kendisidir.","focus_only":"Odak anma, yakarış, övgü, okuma ve itaat gibi etkin kulluk biçimleridir.","gloss":"kulluk eylemi ile ibadet sessizliği","neighbor_only":"Komşu ibadet sırasında sıradan konuşmayı bırakıp susma davranışıdır.","neighbor_ref":"root_001260/B004","relation_type":"thematic","shared_zone":"İki dal aynı ibadet ortamında birlikte bulunabilir."}],"source_phrase_ar":"الذكر الصلاة والدعاء والثناء (ayn;tahdhib)؛ الذكر قراءة القرآن والتسبيح والدعاء والشكر والطاعة (tahdhib)؛ ولذكر الله أكبر واذكروا الله (mufradat)","source_summary":"Kaynaklar Tanrı'yı anmayı ibadet, yakarış ve övgü ekseninde birleştirir; yüceltme, şükretme, itaat ve dinî metin okumayı bu yönelimin farklı gerçekleşmeleri sayar.","sources":["AY","TA","MU"],"what_is_ar":"يدخل فيه الصلاة والدعاء والثناء والتسبيح والشكر والطاعة وقراءة القرآن من حيث هي ذكر لله.","what_is_not_ar":"لا يدخل فيه كل ذكر لساني عام ولا الكتاب المسمى ذكرا إلا من جهة القراءة والعبادة."},"support_links":[]},{"boundary":"Dal kutsal veya vahyedilmiş sayılan kitabın kendisidir; okuma, çalışma, ibadet ya da zihinsel hatırlama eylemi değildir.","branch_kind":"bare","branch_ref":"root_000516/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذِكْر","morph_features":"STEM|POS:N|VN|LEM:*ikor|ROOT:*kr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:4:3:1","qac_word_ref":"94:4:3","surface_ar":"ذِكْرَ"}],"gloss":"indirildiğine inanılan kutsal kitap","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dinin ayrıntılarını bildiren ve ilahi kaynaklı kabul edilen kitaptır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kur'an ile ondan önceki peygamberlere bağlanan kutsal kitapları kapsayan bir üst ad olabilir."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dinin hükümlerini içeren peygamber kitabı genel bir tür olarak anlatılırken kullanılır.","boundary_detail":"Dal kutsal veya vahyedilmiş sayılan kitabın kendisidir; okuma, çalışma, ibadet ya da zihinsel hatırlama eylemi değildir.","branch_image_ar":"الذكر كتاب منزل أو كتاب دين","concept_gloss":"indirildiğine inanılan kutsal kitap","contextual_glosses":[{"applicability":"Bağlam kitabın dini ve vahyedilmiş niteliğini zaten açıkça gösterdiğinde doğal kısa karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Peygambere indirilme ve önceki kitapları kapsayan üst ad olma ayrıntısını açıkça belirtmez.","preserves":"Dini içerikli ve kutsal kabul edilen kitap olma çekirdeğini korur."},"facet_ids":["F001"],"text":"kutsal kitap","usage_role":"general"}],"definition":"Dinin hükümlerini ve açıklamalarını içeren, bir peygambere indirildiğine inanılan kutsal kitaptır. Kapsam hem Kur'an'ı hem de daha önceki kutsal kitapları içine alabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dinin ayrıntılarını bildiren ve ilahi kaynaklı kabul edilen kitaptır."},{"facet_id":"F002","role":"extension","statement":"Kur'an ile ondan önceki peygamberlere bağlanan kutsal kitapları kapsayan bir üst ad olabilir."}],"identity_rationale":"Kaynak ifadesi dini açıklayan kitabı, peygamberlere indirildiğine inanılan kitapları, Kur'an'ı ve önceki kutsal kitapları aynı dalda toplar. Geçici çerçeve metinsel nesneyi doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"dinin ayrıntılarını bildiren kutsal kitap"}],"lexicalization_note":"Tanım yalın dalın kutsal kitap anlamını verir; okuma veya ibadetle ilgili söz öbeklerinden yeni bir genel anlam aktarılmaz.","neighbor_coverage_note":"Sunulan on beş adayın tümü değerlendirildi; kitap bölümü, okuma ve çalışmayla ilgili üç sınır seçildi, öteki adaylar ad, görünme, kulluk veya gizli haber alanlarında uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bütün kitap veya kitap türünü, komşu ise onun çevrelenmiş bölümünü adlandırır.","focus_only":"Odak kutsal kitabın bütünü veya kutsal kitap türüdür.","gloss":"kutsal kitap ile kitap bölümü","neighbor_only":"Komşu kutsal metnin sınırları belirlenmiş bir bölümü ve ayrıca yüksek konum anlamıdır.","neighbor_ref":"root_000758/B003","relation_type":"near_neighbor","shared_zone":"Kutsal kitabın belirli bölümleri, bütün metnin yapısal parçalarıdır."},{"boundary_match":"thematic_only","distinction":"Kitap bir nesnedir; okuma ise yalnız kutsal kitaplarla sınırlı olmayan bir eylemdir.","focus_only":"Odak okunan kutsal metinsel nesnenin kendisidir.","gloss":"kutsal kitap ile okuma","neighbor_only":"Komşu metni sesli veya sessiz okuma, başkasına okutma ve birlikte çalışma eylemleridir.","neighbor_ref":"root_001210/B002","relation_type":"thematic","shared_zone":"Kutsal kitap, okuma eyleminin önemli bir nesnesi olabilir."},{"boundary_match":"thematic_only","distinction":"Odak metinsel nesnedir; komşu farklı kitaplara da uygulanabilen öğrenme etkinliğidir.","focus_only":"Odak dini içeriği taşıyan kitabın kendisini adlandırır.","gloss":"kutsal kitap ile metin çalışması","neighbor_only":"Komşu bir kitabı okuyup yineleyerek öğrenme ve belleğe yerleştirme sürecidir.","neighbor_ref":"root_000470/B002","relation_type":"thematic","shared_zone":"Kutsal kitap üzerinde okuma ve öğrenme çalışması yapılabilir."}],"source_phrase_ar":"الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر (ayn;tahdhib)؛ القرآن والكتب المتقدمة والزبور من بعد الذكر (mufradat)","source_summary":"Kaynaklar dini açıklayan peygamber kitaplarını ortak çekirdek olarak verir ve kapsamı Kur'an ile önceki kutsal kitaplara kadar genişletir.","sources":["AY","TA","MU"],"what_is_ar":"يدخل فيه الكتاب الذي فيه تفصيل الدين وكل كتاب للأنبياء والقرآن والكتب المتقدمة.","what_is_not_ar":"لا يدخل فيه فعل التذكر ولا مطلق الصلاة والدعاء إلا إذا كان اللفظ يدل على الكتاب أو القرآن."},"support_links":[]},{"boundary":"Dal anma eyleminin kendisi değil, kişinin olumlu biçimde anılmasıyla bağlantılı onur, iyi ün ve saygınlıktır.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B007","candidate_links":[{"candidate_id":"cand_fa9f99008a6f5deb3672","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ذِكْر","morph_features":"STEM|POS:N|VN|LEM:*ikor|ROOT:*kr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:4:3:1","qac_word_ref":"94:4:3","surface_ar":"ذِكْرَ"}],"gloss":"onur, iyi ün ve saygınlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin toplum içinde taşıdığı onur ve yüksek saygınlıktır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin olumlu biçimde anılmasıyla yayılan iyi ün ve övgüdür."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin olumlu tanınması ile toplumsal yüksekliğini birlikte anlatmak gereken bağlamlarda kullanılır.","boundary_detail":"Dal anma eyleminin kendisi değil, kişinin olumlu biçimde anılmasıyla bağlantılı onur, iyi ün ve saygınlıktır.","branch_image_ar":"ذكر المرء شرف وصيت","concept_gloss":"onur, iyi ün ve saygınlık","contextual_glosses":[{"applicability":"Kişinin insanlar arasında olumlu biçimde tanınıp anılması bağlamda öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yüksek konum ve onur bileşenini tek başına açıkça belirtmez.","preserves":"Olumlu tanınma ve insanlar arasında yayılan övgü yönünü korur."},"facet_ids":["F002"],"text":"iyi ün","usage_role":"general"},{"applicability":"Toplumdaki yüksek değer ve itibar, yaygın tanınmadan daha önemli olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Adının yayılması ve övgüyle anılması yönünü açıkça kapsamaz.","preserves":"Kişinin yüksek toplumsal değeri ve saygınlığı anlamını korur."},"facet_ids":["F001"],"text":"onur ve saygınlık","usage_role":"contextual"}],"definition":"Bir kişinin insanlar arasında olumlu biçimde tanınmasından doğan iyi ün, onur, övgü ve yüksek saygınlıktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin toplum içinde taşıdığı onur ve yüksek saygınlıktır."},{"facet_id":"F002","role":"core","statement":"Kişinin olumlu biçimde anılmasıyla yayılan iyi ün ve övgüdür."}],"identity_rationale":"Kaynak ifadesi bir kişinin toplum içindeki yüksek konumunu, iyi ününü, övgüyle anılmasını ve saygınlığını ortak bir sonuç alanında toplar. Geçici çerçeve bu toplumsal değer ve yayılmış tanınma bileşimini doğru verir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"onur, iyi ün ve övgü"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"belleği güçlü, yiğit veya iyi anılan adam"}],"lexicalization_note":"Yalın iyi ün ve onur anlamı korunur; kişi niteleyen söz öbeği bellek gücü ile iyi anılmayı kendi bağlamında birleştirir.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; iyi ün, güzel anılma, yüce saygınlık, tanınmışlık ve övgüyle ilgili beş sınır seçildi, kalan adaylar daha dar statü türleri veya kardeş dallardı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu yayılan iyi üne daha dardır; odak bu üne onur ve toplumsal yükseklik bileşenini de ekler.","focus_only":"Odak iyi üne ek olarak onur ve yüksek toplumsal konumu da kapsar.","gloss":"onurlu ün ile iyi ün","neighbor_only":"Komşu özellikle insanlar arasında yayılmış güzel ve olumlu ünle sınırlıdır.","neighbor_ref":"root_000890/B002","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin insanlar arasında olumlu biçimde tanınıp anılmasını anlatır."},{"boundary_match":"partial","distinction":"Komşu güzel söz ve övgü sonucuna daha yakındır; odak bunun yanında onur ve yüksek konumu da kurucu sayar.","focus_only":"Odak kişinin yüksek konumunu ve saygınlığını da içerir.","gloss":"saygınlık ile güzel anılma","neighbor_only":"Komşu kişinin insanlar arasında güzel sözle anılması ve övülmesine odaklanır.","neighbor_ref":"root_000804/B004","relation_type":"near_synonym","shared_zone":"İki dal olumlu anılma ve iyi ün alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak iyi anılma ve ünle bağlantılıdır; komşu ün bulunmasa da büyüklük ve otoriteyi ifade edebilir.","focus_only":"Odak yaygın olumlu anılma ve iyi ün bileşenini taşır.","gloss":"iyi ün ile yüce saygınlık","neighbor_only":"Komşu kutsallık, büyüklük, önderlik ve görüş üstünlüğü gibi ek toplumsal boyutlar içerir.","neighbor_ref":"root_001029/B010","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin toplumdaki onur ve yüksek değerini anlatabilir."},{"boundary_match":"partial","distinction":"Tanınmışlık değer bakımından yansız olabilir; odak dalı ise olumlu değerlendirme ve onur taşır.","focus_only":"Odak ünün olumlu, övgüye değer ve onurlu olmasını gerektirir.","gloss":"iyi ün ile tanınmışlık","neighbor_only":"Komşu bir topluluğun veya kişinin olumlu ya da olumsuz değer belirtilmeden tanınır hale gelmesini anlatabilir.","neighbor_ref":"root_000500/B004","relation_type":"near_neighbor","shared_zone":"İki dal bir adın insanlar arasında yayılması ve tanınması alanında buluşur."},{"boundary_match":"partial","distinction":"Komşu bir söz eylemi, odak ise bu ve benzeri değerlendirmelerin toplumsal sonucu olan itibardır.","focus_only":"Odak kişinin kazandığı kalıcı iyi ün ve toplumsal değerdir.","gloss":"iyi ün ile övme","neighbor_only":"Komşu kişiyi iyi özellikleriyle övme eylemidir.","neighbor_ref":"root_000933/B002","relation_type":"near_neighbor","shared_zone":"Övgü eylemi kişinin iyi ününün oluşmasına veya güçlenmesine katkı verebilir."}],"source_phrase_ar":"الذكر العلاء والشرف (maqayis)؛ الذكر الشرف والصوت (ayn;tahdhib)؛ الذكر الصيت والثناء وذي الذكر أي ذي الشرف (sihah)؛ وإنه لذكر لك ولقومك أي شرف (mufradat)","source_summary":"Kaynaklar onur ve yüksek konumu, insanlar arasında yayılan iyi ün ve övgüyle birlikte tek bir olumlu toplumsal itibar alanında birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الشرف والعلاء والصيت والثناء وحسن الذكر.","what_is_not_ar":"لا يدخل فيه مجرد التلفظ باسم الشيء ولا الذكر بمعنى الكتاب إلا إذا صرح بالشرف أو الصيت."},"support_links":["sup_621173ed951ad333045e"]},{"boundary":"Anlam bağımsız bir kitap adı değildir; bir hakkı gösteren yazılı belgeyi adlandıran belirli söz öbeğiyle sınırlıdır.","branch_kind":"collocation","branch_ref":"root_000516/B008","candidate_links":[{"candidate_id":"cand_b35c09b0db7500dc5371","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ذِكْر","morph_features":"STEM|POS:N|VN|LEM:*ikor|ROOT:*kr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:4:3:1","qac_word_ref":"94:4:3","surface_ar":"ذِكْرَ"}],"gloss":"hakkı gösteren yazılı belge","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hakkı yazılı biçimde kayda geçirip kanıtlayan belgedir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı yapının çoğul biçimi birden çok hak belgesini topluca adlandırır."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir hakkın yazıyla kayda geçirildiği belgeyi veya bu belgelerin çoğulunu açıklarken kullanılır.","boundary_detail":"Anlam bağımsız bir kitap adı değildir; bir hakkı gösteren yazılı belgeyi adlandıran belirli söz öbeğiyle sınırlıdır.","branch_image_ar":"ذكر الحق صك ووثيقة حق","concept_gloss":"hakkı gösteren yazılı belge","contextual_glosses":[{"applicability":"Bağlam belgenin yazılı olduğunu açıkça gösterdiğinde kısa ve doğal karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yazılı olma niteliğini ve çoğul biçimin tarihsel yapısını açıkça belirtmez.","preserves":"Belgenin belirli bir hakkı gösterme ve kanıtlama işlevini korur."},"facet_ids":["F001"],"text":"hak belgesi","usage_role":"general"},{"applicability":"Birden çok hakkı veya birden çok yazılı kanıtı topluca adlandıran çoğul yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tekil belge kullanımını dışarıda bırakır.","preserves":"Birden çok yazılı hak belgesinin topluca adlandırılmasını korur."},"facet_ids":["F002"],"text":"hak belgeleri","usage_role":"contextual"}],"definition":"Bir hakkın varlığını, sahibini veya koşullarını yazılı olarak gösteren belge ve bu tür belgelerin çoğul adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hakkı yazılı biçimde kayda geçirip kanıtlayan belgedir."},{"facet_id":"F002","role":"extension","statement":"Aynı yapının çoğul biçimi birden çok hak belgesini topluca adlandırır."}],"identity_rationale":"Kaynak ifadesi yalnız belirli hak söz öbeğinde bir hakkı kayda geçiren yazılı belgeyi ve bu belgelerin çoğulunu verir. Geçici çerçeve yapıya bağlı belge anlamını eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"hakkı gösteren yazılı belge"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yazılı hak belgeleri"}],"lexicalization_note":"Tanım yalnız hak belgesi yapısına ve onun çoğul biçimine bağlanır; yalın köke genel belge anlamı yüklenmez.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; eş belge, geniş kayıt, genel yazılı kâğıt, hakkın kendisi ve vasiyetle ilgili beş sınır seçildi, kalan adaylar yazma eylemi, pay veya kardeş anlamlarda daha uzaktı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak belgenin belirli bir hakkı göstermesini gerektirir; komşu ise bu koşul olmadan daha genel yazılı belgeleri de kapsar.","focus_only":"Odak yalnız bir hakkı gösteren yazılı belge yapısıyla sınırlıdır.","gloss":"hak belgesi ile yazılı senet","neighbor_only":"Komşu hak bağlantısı zorunlu olmadan yazılı kitap veya senetleri kapsar.","neighbor_ref":"root_000874/B006","relation_type":"near_synonym","shared_zone":"İki dal yazılı senet veya belgeyi adlandırdıklarında örtüşür."},{"boundary_match":"partial","distinction":"Odak hak belgesine daralır; komşu belge türlerini ve resmi kayıt eylemini daha geniş biçimde kapsar.","focus_only":"Odak özellikle bir hakkı gösteren belge yapısıyla sınırlıdır.","gloss":"hak belgesi ile resmi kayıt","neighbor_only":"Komşu kayıt defteri, yükümlülük belgesi, yazılı sayfa ve yargıcın kayda geçirmesi gibi daha geniş kullanımları kapsar.","neighbor_ref":"root_000677/B004","relation_type":"near_synonym","shared_zone":"Her iki dal hakkı veya yükümlülüğü yazılı biçimde güvence altına alan belgeyi anlatabilir."},{"boundary_match":"partial","distinction":"Odak hak ilişkisine bağlıdır; komşu daha genel yazılı nesneyi ve belge dışındaki pay anlamını da içerir.","focus_only":"Odak belgenin belirli bir hakkı kanıtlama işlevini zorunlu kılar.","gloss":"hak belgesi ile yazılı kâğıt","neighbor_only":"Komşu yazılı belge yanında ayrılmış pay ve ödül gibi belge dışı anlamlara da uzanır.","neighbor_ref":"root_001239/B002","relation_type":"near_synonym","shared_zone":"İki dal yazılı bir belge veya kayıt nesnesini adlandırabilir."},{"boundary_match":"field_only","distinction":"Hak hukuki veya toplumsal ilişkidir; belge ise o ilişkinin varlığını gösteren ayrı bir nesnedir.","focus_only":"Odak hakkı kanıtlayan yazılı belgedir.","gloss":"hak belgesi ile hakkın kendisi","neighbor_only":"Komşu kişinin sahip olduğu hakkın veya hak iddiasının kendisidir.","neighbor_ref":"root_000347/B003","relation_type":"same_field","shared_zone":"Belge, kişinin sahip olduğu hakkı kayda geçirir ve kanıtlar."},{"boundary_match":"partial","distinction":"Odak bir hakkı kanıtlar; komşu ise bir kişiye yapılacak işi önceden bildirip emanet eder.","focus_only":"Odak mevcut bir hakkı gösteren yazılı kanıt işlevidir.","gloss":"hak belgesi ile yazılı vasiyet","neighbor_only":"Komşu gelecekte uyulması gereken buyruk veya görevi emanet eden vasiyet ve talimattır.","neighbor_ref":"root_001055/B002","relation_type":"near_neighbor","shared_zone":"İki dal yükümlülük doğurabilen ve korunması gereken yazılı belgeler alanında buluşur."}],"source_phrase_ar":"ذكر الحق الصك وجمعه ذكور حقوق (ayn;tahdhib)؛ يقال ذكور حق (ayn;tahdhib)","source_summary":"Kaynaklar belirli hak söz öbeğini yazılı hak belgesi olarak açıklar ve çoğul biçimin birden çok hak belgesini gösterdiğinde birleşir.","sources":["AY","TA"],"what_is_ar":"يدخل فيه ذكر الحق بمعنى الصك وجمعه ذكور حقوق أو ذكور حق.","what_is_not_ar":"لا يدخل فيه الكتاب الديني المسمى ذكرا ولا التذكرة العامة."},"support_links":["sup_058f9716ab94eb420ec9"]},{"boundary":"Dal hatırlamanın kendisi değil, onu doğuran eylem veya araçtır; sık anma anlamı da yalnız kaynakta belirtilen biçime bağlı bir yoğunluk yüzüdür.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B009","candidate_links":[{"candidate_id":"cand_d69b0821b2f5deaa9ae7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ذِكْر","morph_features":"STEM|POS:N|VN|LEM:*ikor|ROOT:*kr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:4:3:1","qac_word_ref":"94:4:3","surface_ar":"ذِكْرَ"}],"gloss":"hatırlatma, hatırlamayı sağlayan araç ve sıkça anma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir başkasında veya kişinin kendisinde unutulmuş bilginin yeniden hatırlanmasını sağlar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir ihtiyacı veya bilgiyi hatırlamaya yarayan işaret, not ya da araç olarak gerçekleşir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir ad biçiminde bir şeyi sık ve yoğun biçimde anma anlamı taşır."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hatırlamayı doğuran eylemi, buna yarayan işaret veya nesneyi ve belirli biçime bağlı sık anmayı birlikte açıklamak gereken genel bağlamlarda kullanılır.","boundary_detail":"Dal hatırlamanın kendisi değil, onu doğuran eylem veya araçtır; sık anma anlamı da yalnız kaynakta belirtilen biçime bağlı bir yoğunluk yüzüdür.","branch_image_ar":"الذكرى والتذكرة ما يذكّر","concept_gloss":"hatırlatma, hatırlamayı sağlayan araç ve sıkça anma","contextual_glosses":[{"applicability":"Bir kişide unutulmuş bilginin yeniden zihne gelmesini sağlayan eylem anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hatırlatıcı nesne ve sık anma yüzlerini dışarıda bırakır.","preserves":"Hatırlamayı başka bir kişide meydana getiren geçişli eylemi korur."},"facet_ids":["F001"],"text":"hatırlatmak","usage_role":"general"},{"applicability":"Bir ihtiyaç veya bilginin unutulmamasını sağlayan not, işaret ya da nesne anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hatırlatma eylemini ve sık anma yoğunluğunu kapsamaz.","preserves":"Hatırlamaya yarayan araç ve işaret işlevini korur."},"facet_ids":["F002"],"text":"hatırlatıcı","usage_role":"contextual"},{"applicability":"Kaynakta yoğunluk bildiren belirli ad biçimi bir şeyi çok kez anmayı anlattığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasına hatırlatma ve hatırlatıcı araç anlamlarını dışarıda bırakır.","preserves":"Bir şeyi çok ve yinelenen biçimde anma yoğunluğunu korur."},"facet_ids":["F003"],"text":"sıkça anma","usage_role":"explanatory"}],"definition":"Bir bilginin yeniden zihinde belirmesini sağlamak veya buna yarayan bir işaret ya da araç sunmaktır. Belirli bir biçim ayrıca bir şeyi sıkça anmayı anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir başkasında veya kişinin kendisinde unutulmuş bilginin yeniden hatırlanmasını sağlar."},{"facet_id":"F002","role":"specialization","statement":"Bir ihtiyacı veya bilgiyi hatırlamaya yarayan işaret, not ya da araç olarak gerçekleşir."},{"facet_id":"F003","role":"source_variant","statement":"Belirli bir ad biçiminde bir şeyi sık ve yoğun biçimde anma anlamı taşır."}],"identity_rationale":"Kaynak ifadesi yalnız hatırlatan bir nesneyi değil, başkasında hatırlamayı meydana getirme eylemini, hatırlamaya yarayan aracı ve bazı biçimlerde sık anmayı birlikte verir. Dal korunabilir, ancak geçici nesne merkezli çerçeve bu süreç ve yoğunluk yüzlerini açıkça kapsayacak biçimde genişletilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"hatırlatma, öğüt alma veya sıkça anma"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"hatırlatıcı"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"hatırlatma"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"ona o şeyi hatırlattı"}],"lexicalization_note":"Hatırlatma eylemi, hatırlatıcı araç ve sık anma ayrı yüzler olarak tutulur; bu yapıların hiçbiri yalın zihinsel hatırlamayla özdeşleştirilmez.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; öğüt, uyarı, dikkat çekme, hatırlama ve sözle anmayla ilgili beş sınır seçildi, kalan adaylar öğretme, aktarma, yazı veya yergi alanlarında daha uzaktı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu ahlaki yönlendirme ve duygusal etki taşır; odak bunları gerektirmeyen genel hatırlatma alanıdır.","focus_only":"Odak her tür bilgiyi hatırlatabilir ve bir araç ya da işaret biçiminde gerçekleşebilir.","gloss":"genel hatırlatma ile öğüt","neighbor_only":"Komşu korkutma, sakındırma ve iyi sonuca yöneltme yoluyla kalbi etkileyen öğütle sınırlıdır.","neighbor_ref":"root_001663/B001","relation_type":"near_synonym","shared_zone":"Öğüt, kişiye unuttuğu değer veya sonucu yeniden hatırlatabilir."},{"boundary_match":"partial","distinction":"Uyarma risk ve sakınma yönelimi gerektirir; hatırlatma ise böyle bir değer ve tehlike koşulu taşımaz.","focus_only":"Odak tarafsız, olumlu veya olumsuz herhangi bir bilgiyi yeniden zihne getirebilir.","gloss":"hatırlatma ile uyarma","neighbor_only":"Komşu kişide tehlikeye karşı dikkat ve sakınma meydana getirmeyi amaçlar.","neighbor_ref":"root_000301/B002","relation_type":"near_neighbor","shared_zone":"Bir tehlikeyi hatırlatmak aynı zamanda kişinin dikkatli olmasını sağlayabilir."},{"boundary_match":"partial","distinction":"Komşu soru ve bilgi isteme işlevi taşır; odak ise önceden bilinen içeriğin yeniden hatırlanmasını hedefler.","focus_only":"Odak önceden bilinen bir içeriği yeniden zihne getirmeyi sağlar.","gloss":"hatırlatma ile dikkat çekme","neighbor_only":"Komşu karşıdakinin dikkatini çekip ondan bilgi istemeye yarayan bir söyleyiş kalıbıdır.","neighbor_ref":"root_000531/B013","relation_type":"near_neighbor","shared_zone":"Dikkat çekme, dinleyiciyi belirli bir konuya zihinsel olarak yöneltebilir."},{"boundary_match":"partial","distinction":"Odak sonuç doğuran uyarıcı eylem veya araçtır; komşu ise ortaya çıkan zihinsel durum ve süreçtir.","focus_only":"Odak hatırlamayı meydana getiren dış veya geçişli neden ile aracı anlatır.","gloss":"hatırlatma ile hatırlama","neighbor_only":"Komşu kişinin zihninde bilginin korunması veya yeniden bulunması sürecidir.","neighbor_ref":"root_000516/B003","relation_type":"near_neighbor","shared_zone":"İki dal unutulmuş bilginin yeniden zihinde hazır bulunması sonucunda birleşir."},{"boundary_match":"partial","distinction":"Sözle anma dilsel biçimi gerektirir fakat hatırlatma amacı taşımaz; odak farklı araçlarla gerçekleşebilir ve hatırlama sonucu hedefler.","focus_only":"Odak sözlü olmak zorunda değildir ve temel işlevi bilgiyi yeniden zihne getirmektir.","gloss":"hatırlatma ile sözle anma","neighbor_only":"Komşu belirli bir kişi veya şeyi söz içinde adlandırıp konu etmektir.","neighbor_ref":"root_000516/B004","relation_type":"near_neighbor","shared_zone":"Bir şeyi sözle anmak dinleyene o şeyi hatırlatabilir."}],"source_phrase_ar":"الذكرى اسم للتذكير والتذكير مجاوز (ayn)؛ التذكرة ما تستذكر به الحاجة (sihah)؛ الذكرى بمعنى الذكر وبمعنى التذكير (tahdhib)؛ التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر (mufradat)","source_summary":"Kaynaklar hatırlatmayı başkasında hatırlama meydana getiren geçişli eylem ve hatırlamaya yarayan araç olarak verir; ayrıca belirli biçimde sık anma yoğunluğunu kaydeder.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الذكرى والتذكير والتذكرة وما يجعل الشيء مذكورا أو يعيد حضوره.","what_is_not_ar":"لا يدخل فيه نفس الحفظ القلبي إلا من حيث النتيجة، ولا الذكر بمعنى الذكران والذكورة."},"support_links":["sup_96e23b245baec5fb564b"]},{"boundary":"Dal fiziksel yükseltme çekirdeğini kapsar; saygınlık, haber yayma ve özel yürüyüş anlamları bu sınıra girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B001","candidate_links":[{"candidate_id":"cand_d69b0821b2f5deaa9ae7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَفَعَ","morph_features":"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P","morpheme_role":"STEM","pos":"V","qac_ref":"94:4:1:2","qac_word_ref":"94:4:1","surface_ar":"رَفَعْ"}],"gloss":"bir şeyi yukarı kaldırmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi bulunduğu konumdan yukarı taşımak ve böylece yüksekliğini artırmak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yapıyı daha yüksek olacak biçimde uzatmak."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin bulunduğu yerden daha yüksek bir konuma taşındığı genel fiziksel kullanım için uygundur.","boundary_detail":"Dal fiziksel yükseltme çekirdeğini kapsar; saygınlık, haber yayma ve özel yürüyüş anlamları bu sınıra girmez.","branch_image_ar":"إعلاء الشيء","concept_gloss":"bir şeyi yukarı kaldırmak","contextual_glosses":[{"applicability":"Bir binanın boyunun artırıldığı yapı bağlamındaki özel kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapının yüksekliğini artırma ve uzatma sonucunu korur."},"facet_ids":["F002"],"text":"yapıyı yükseltmek","usage_role":"contextual"}],"definition":"Bir şeyi bulunduğu yerden daha yukarı bir konuma taşımak, aşağı indirme yönünün tersine hareket ettirmektir. Yapı bağlamında bu çekirdek, yapıyı yükseltip uzatma biçiminde gerçekleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi bulunduğu konumdan yukarı taşımak ve böylece yüksekliğini artırmak."},{"facet_id":"F002","role":"specialization","statement":"Yapıyı daha yüksek olacak biçimde uzatmak."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca kendiliğinden gerçekleşen bir hareket gibi anlaşılabilir.","fit":"narrowing","loses":"Bir etkileyenin nesneyi yukarı taşıması ve yapı yükseltme ayrıntısını kaybeder.","preserves":"Daha yüksek bir konuma geçme yönünü korur."},"text":"yükselmek"}],"identity_rationale":"Kaynak ifadesi, bir şeyi bulunduğu yerden yukarı taşımayı aşağı indirmenin karşıtı olarak verir; yapı söz konusu olduğunda yükseltip uzatmayı da bu çekirdeğe bağlı özel bir kullanım olarak gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi bulunduğu yerden yukarı kaldırmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kendiliğinden yükselmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yapıyı yükseltip uzatmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"üst üste serilmiş döşekler"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"onu göğe çıkarmak veya onurlandırmak"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"bir şeyi eliyle kaldırmak"}],"lexicalization_note":"Çıplak kullanım fiziksel olarak yukarı kaldırmayı anlatır; yapı, döşek ve başka kalıplara bağlı kullanımlar bu çekirdeğin özel gerçekleşmeleri olarak ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; düşey hareketin karşıtı, genel yükselme ve üstte bulunma ile sınırı en açık gösteren üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal konumu yukarı doğru değiştirirken komşu dal nesneyi elden yere veya daha aşağı, kararlaştırılmış bir konuma bırakır.","focus_only":"Nesneyi daha yüksek bir konuma taşır.","gloss":"yukarı kaldırmak ve aşağı bırakmak","neighbor_only":"Nesneyi daha alçak ya da belirlenmiş bir yere bırakır.","neighbor_ref":"root_001657/B001","relation_type":"antonym","shared_zone":"İki dal da bir nesnenin düşey konumunu değiştiren hareketleri anlatır."},{"boundary_match":"partial","distinction":"Odak dal özellikle fiziksel bir nesnenin yukarı alınmasına dayanır; komşu dal ise ettirgenlik aramadan genel yükselme ve yücelmeyi daha geniş biçimde kapsar.","focus_only":"Bir nesneyi yerinden yukarı taşıma eylemini ve yapı yükseltmeyi belirginleştirir.","gloss":"kaldırmak ve yükselmek","neighbor_only":"Bulutun yükselmesi gibi daha geniş kendiliğinden yükselme ve yücelme durumlarını da kapsar.","neighbor_ref":"root_001502/B001","relation_type":"near_synonym","shared_zone":"Her ikisinin çekirdeğinde daha yüksek bir konuma geçiş veya geçirme bulunur."},{"boundary_match":"partial","distinction":"Odak dal bir konum değişikliği eylemidir; komşu dal ise hareket gerektirmeyen bir yer ve yön ilişkisini belirtir.","focus_only":"Daha yüksek konuma götüren hareketi anlatır.","gloss":"yukarı kaldırmak ve üstte olmak","neighbor_only":"Bir şeyin üstte veya yukarı yönde bulunma ilişkisini anlatır.","neighbor_ref":"root_001188/B001","relation_type":"near_neighbor","shared_zone":"İki dal da düşey yükseklik ve üst-alt eksenini paylaşır."}],"source_phrase_ar":"رفعت الشيء رفعا وهو خلاف الخفض (maqayis;ayn); الرفع ضد الخفض (tahdhib); الرفع يقال في الأجسام الموضوعة إذا أعليتها عن مقرها (mufradat); في البناء إذا طولته (mufradat)","source_summary":"Kanıtlar fiziksel yukarı taşıma ile aşağı indirme arasındaki karşıtlıkta birleşir ve yapı yükseltmeyi bu yönlü değişimin özel bir uygulaması olarak gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"إعلاء الأجسام أو البناء وإزالة الشيء عن موضعه إلى علو","what_is_not_ar":"ليس رفع القدر ولا الإبلاغ ولا السير الخاص"},"support_links":["sup_96e23b245baec5fb564b"]},{"boundary":"Dal toplumsal veya simgesel değerin yükselmesini kapsar; fiziksel taşıma ve yalnızca ün kazanma bu çekirdeğin yerini tutmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B002","candidate_links":[{"candidate_id":"cand_fa9f99008a6f5deb3672","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَفَعَ","morph_features":"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P","morpheme_role":"STEM","pos":"V","qac_ref":"94:4:1:2","qac_word_ref":"94:4:1","surface_ar":"رَفَعْ"}],"gloss":"saygınlığı yüksek olmak veya yükseltmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin yüksek saygınlığa ve onurlu bir konuma sahip olması."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin, anılışın veya konumun saygınlığını artırıp onu yüceltmek."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem onurlu ve yüksek konumlu olma durumunu hem de birine ya da bir şeye bu değeri kazandırmayı kapsar.","boundary_detail":"Dal toplumsal veya simgesel değerin yükselmesini kapsar; fiziksel taşıma ve yalnızca ün kazanma bu çekirdeğin yerini tutmaz.","branch_image_ar":"علو القدر","concept_gloss":"saygınlığı yüksek olmak veya yükseltmek","contextual_glosses":[{"applicability":"Bir kişinin sahip olduğu saygın konumu niteleyen durum kullanımı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin saygınlığını ve yüksek toplumsal değerini korur."},"facet_ids":["F001"],"text":"onurlu ve yüksek konumlu","usage_role":"contextual"},{"applicability":"Bir kişinin, anılışın, belgenin veya yerin saygınlığının artırıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Değeri ve saygınlığı etkin biçimde artırma yönünü korur."},"facet_ids":["F002"],"text":"değerini yüceltmek","usage_role":"contextual"}],"definition":"Bir kişinin, anılışın veya konumun değer ve saygınlık bakımından yüksek olması ya da bu yüksek konuma çıkarılmasıdır. Aşağılanmanın karşıtıdır ve fiziksel yükseklik bildirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin yüksek saygınlığa ve onurlu bir konuma sahip olması."},{"facet_id":"F002","role":"extension","statement":"Bir kişinin, anılışın veya konumun saygınlığını artırıp onu yüceltmek."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Saygınlık gerektirmeyen sıradan tanınmışlık anlamını ekler.","collision":"Kötü bir nedenle tanınmış kişi de ünlü olabilir.","fit":"displacement","loses":"Onur, yüksek değer ve aşağılanmaya karşıt saygınlık çekirdeğini kaybeder.","preserves":"Bir kişinin başkalarınca tanınması ihtimalini korur."},"text":"ünlü olmak"}],"identity_rationale":"Kaynak ifadesi kişinin onurlu ve yüksek konumlu oluşunu, aşağılanmanın karşıtı olan saygınlığı ve bir anılışın ya da konumun yüceltilmesini aynı değer ekseninde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"değerli ve onurlu döşekler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"anılışını yüceltmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"konumunu ve saygınlığını yükseltmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"saygın ve yüksek konumlu"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yüksek saygınlık ve onur"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bir topluluğu alçaltıp diğerini yükselten"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"onu göğe çıkarmak veya onurlandırmak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"değerli ve onurlandırılmış sayfalar"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"evleri onurlandırıp yüceltmek"}],"lexicalization_note":"Çıplak biçimler yüksek saygınlık durumunu anlatır; anılışı, konumu, belgeleri veya yapıları yüceltmeye bağlı kalıplar ayrı bağlamsal gerçekleşmelerdir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; onur alanındaki en yakın komşu, karşıt değer yönü ve iyi ünle karışma riski sınırı açıklayan üç ilişki olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hem yüksek saygınlık durumunu hem de onu artırma eylemini işler; komşu dal yüksek onur alanını ve seçkinlik adlarını daha geniş biçimde kapsar.","focus_only":"Saygınlığı artıran eylemi ve anılış ya da konum gibi nesnelerin yüceltilmesini de kapsar.","gloss":"saygınlığı yükseltmek ve yüksek onur","neighbor_only":"Yüksek toplumsal tabakayı ve seçkin kişileri adlandıran daha geniş kullanımları kapsar.","neighbor_ref":"root_001042/B002","relation_type":"near_synonym","shared_zone":"Her iki dalın merkezinde yüksek değer, onur ve saygınlık bulunur."},{"boundary_match":"opposed","distinction":"Odak dal değer ve onur kazandırırken komşu dal bunları azaltan küçümseme yönünde işler.","focus_only":"Kişinin veya konumun değerini ve saygınlığını yükseltir.","gloss":"yüceltmek ve küçümsemek","neighbor_only":"Kişiyi küçümseyip değerini düşürür.","neighbor_ref":"root_000414/B006","relation_type":"antonym","shared_zone":"İki dal da bir kişiye verilen toplumsal değerin yönünü belirler."},{"boundary_match":"partial","distinction":"Odak dal kişinin değer ve onur düzeyine ilişkindir; komşu dal ise bu değerin toplumda yayılmış iyi bir ün olarak görünmesine odaklanır.","focus_only":"Saygınlığın kendisini ve onu yükseltme eylemini anlatır.","gloss":"yüksek saygınlık ve iyi ün","neighbor_only":"İnsanlar arasında yayılan iyi ünü ve olumlu tanınmışlığı anlatır.","neighbor_ref":"root_000890/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal olumlu toplumsal değerlendirme alanında buluşur."}],"source_phrase_ar":"رفع الرجل يرفع رفاعة فهو رفيع إذا شرف (ayn;tahdhib); رجل رفيع أي شريف (sihah); الرفعة نقيض الذلة (tahdhib); في الذكر إذا نوهته (mufradat); في المنزلة إذا شرفتها (mufradat)","source_summary":"Kanıtlar yüksek saygınlık ile aşağılanma arasındaki karşıtlığı temel alır; kişinin onurlu oluşunu ve anılış ya da konumun yüceltilmesini bu temel çevresinde birleştirir.","sources":["AY","SI","TA","MU"],"what_is_ar":"تشريف الشخص أو الذكر أو المنزلة وعلو القدر","what_is_not_ar":"ليس النقل الحسي ولا رفع الزرع ولا رفع الخبر"},"support_links":["sup_621173ed951ad333045e"]},{"boundary":"Dal genel hız kavramı değil, binek hayvanının belirli yoğunluk ve aralıkta gerçekleşen yürüyüş biçimidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَفَعَ","morph_features":"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P","morpheme_role":"STEM","pos":"V","qac_ref":"94:4:1:2","qac_word_ref":"94:4:1","surface_ar":"رَفَعْ"}],"gloss":"bineğin orta-üst hızda ilerlemesi veya ilerletilmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Binek hayvanının ağır yürüyüş ile tam koşu arasında güçlü ve hızlı ilerlemesi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bineğin yürüyüşünü olağandan daha güçlü ve hızlı hale getirmek."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Binek hayvanının ağır yürüyüş ile tam koşu arasındaki güçlü gidişini ve bu gidişe yöneltilmesini birlikte anlatır.","boundary_detail":"Dal genel hız kavramı değil, binek hayvanının belirli yoğunluk ve aralıkta gerçekleşen yürüyüş biçimidir.","branch_image_ar":"رفع السير","concept_gloss":"bineğin orta-üst hızda ilerlemesi veya ilerletilmesi","contextual_glosses":[{"applicability":"Hayvanın gidiş biçiminin anlatıldığı, tam koşuya varmayan hızlı yürüyüş bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hızın ağır yürüyüş ile tam koşu arasındaki özel yerini açıkça belirtmez.","preserves":"İlerleyişin güçlü ve hızlı niteliğini korur."},"facet_ids":["F001"],"text":"güçlü ve hızlı ilerlemek","usage_role":"contextual"}],"definition":"Bir binek hayvanının ağır yürüyüşten hızlı, tam koşudan daha düşük bir hızla güçlü biçimde ilerlemesidir. Aynı alan, hayvanın yürüyüşünü bu yoğunluğa çıkarma eylemini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Binek hayvanının ağır yürüyüş ile tam koşu arasında güçlü ve hızlı ilerlemesi."},{"facet_id":"F002","role":"specialization","statement":"Bineğin yürüyüşünü olağandan daha güçlü ve hızlı hale getirmek."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Tam koşuyu ve binek dışındaki her türlü koşuyu sınırsız biçimde kapsar.","collision":"Kaynakta belirtilen ara yürüyüş düzeyini en üst hızla karıştırır.","fit":"broadening","loses":null,"preserves":"Hızlı ilerleme yönünü korur."},"text":"koşmak"}],"identity_rationale":"Kaynak ifadesi, bineğin ağır yürüyüşten daha hızlı fakat tam koşudan daha düşük bir gidişini ve hayvanın yürüyüşünü belirgin biçimde hızlandırmayı birlikte gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"devenin yürüyüşünü hızlandırmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ağır yürüyüşle tam koşu arasında hızlı gidiş"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"hızı yer yer artan koşu"}],"lexicalization_note":"Biçim birimleri belirli bir yürüyüş türünü adlandırır; kalıba bağlı kullanım ise bineğin yürüyüşünü bu düzeye çıkarma eylemini ayrı tutar.","neighbor_coverage_note":"Bütün aday yürüyüş kartları karşılaştırıldı; hız aralığı, deveye özgü atılganlık ve beden duruşu bakımından en açıklayıcı üç sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hızın alt ve üst sınırını belirli bir aralıkta tutar; komşu dal ise belirli bir aralık şartı olmadan hızlı binek yürüyüşlerini kapsar.","focus_only":"Ağır yürüyüş ile tam koşu arasında belirli bir hız düzeyi kurar.","gloss":"ara hızlı yürüyüş ve hızlı binek gidişi","neighbor_only":"Binek hayvanının çeşitli hızlı yürüyüşlerini ve onu genel olarak hızlandırmayı kapsar.","neighbor_ref":"root_001628/B001","relation_type":"near_synonym","shared_zone":"İki dal da binek hayvanının hızlı ilerlemesi ve sürücünün onu hızlandırmasıyla ilgilidir."},{"boundary_match":"partial","distinction":"Odak dal hız derecesini ağır yürüyüş ile tam koşu arasında tanımlar; komşu dal develerin peş peşe atılgan ilerleyiş biçimine odaklanır.","focus_only":"Binek türleri arasında kullanılabilen ve tam koşunun altında kalan bir hız düzeyidir.","gloss":"güçlü binek yürüyüşü ve atılgan deve gidişi","neighbor_only":"Özellikle develerin ardışık ve atılgan ilerleyişini öne çıkarır.","neighbor_ref":"root_000676/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da devenin olağandan hızlı ve güçlü yürüyüşünü anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı yönü hız derecesidir; komşu dalın ayırıcı yönü ise hızlı gidişe eşlik eden alçak boyun duruşudur.","focus_only":"Yürüyüşü hız aralığıyla tanımlar.","gloss":"hız derecesi ve boyun alçaltarak gidiş","neighbor_only":"Boyunların alçaltılması gibi belirli bir beden duruşunu ve ciddi gidişi şart koşar.","neighbor_ref":"root_000419/B004","relation_type":"near_neighbor","shared_zone":"İki dal da binek hayvanlarının güçlü ve hızlı ilerleyişini betimler."}],"source_phrase_ar":"مرفوع الناقة في سيرها خلاف الموضوع (maqayis); المرفوع من حضر الفرس والبرذون دون الحضر وفوق الموضوع (ayn;tahdhib); رفع البعير في السير أي بالغ (sihah); مرفوع السير شديدة (mufradat)","source_summary":"Kanıtlar bu yürüyüşü ağır gidişin üstünde, tam koşunun altında konumlandırır; bazı ifadeler hız aralığını, bazıları ise yürüyüşü artırma eylemini öne çıkarır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"اشتداد سير الدابة بين البطء والحضر ورفع البعير في سيره","what_is_not_ar":"ليس علو المنزلة ولا حمل الزرع"},"support_links":[]},{"boundary":"Dal bir şeyi yaklaştırma veya yetkili önüne sunma eylemidir; haberin kamuya yayılması ayrı bir anlamdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B004","candidate_links":[{"candidate_id":"cand_b35c09b0db7500dc5371","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَفَعَ","morph_features":"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P","morpheme_role":"STEM","pos":"V","qac_ref":"94:4:1:2","qac_word_ref":"94:4:1","surface_ar":"رَفَعْ"}],"gloss":"yaklaştırmak veya yetkili önüne sunmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi bulunduğu yere göre yakına getirmek veya öne almak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiyi, davayı veya anlatılan işi karar verecek yetkilinin önüne sunmak."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem genel öne getirme eylemini hem de kişi ya da işin karar verecek makama sunulmasını kapsar.","boundary_detail":"Dal bir şeyi yaklaştırma veya yetkili önüne sunma eylemidir; haberin kamuya yayılması ayrı bir anlamdır.","branch_image_ar":"التقريب والتقديم","concept_gloss":"yaklaştırmak veya yetkili önüne sunmak","contextual_glosses":[{"applicability":"Bir kişi veya işin yönetici ya da yargıç tarafından görülmek üzere sunulduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yetkiliye doğru yaklaştırma ve değerlendirmeye sunma işlemini korur."},"facet_ids":["F002"],"text":"önüne getirmek","usage_role":"contextual"}],"definition":"Bir şeyi daha yakına getirmek veya öne almaktır. Yönetim ve yargı bağlamında kişi, dava ya da anlatılan iş yetkili önüne çıkarılarak değerlendirmeye sunulur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi bulunduğu yere göre yakına getirmek veya öne almak."},{"facet_id":"F002","role":"specialization","statement":"Bir kişiyi, davayı veya anlatılan işi karar verecek yetkilinin önüne sunmak."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yalnızca sözlü ya da yazılı bilgi verme anlamını ekler.","collision":"Haber yayma dalıyla kolayca karışır.","fit":"displacement","loses":"Kişiyi veya işi yaklaştırıp yetkili önüne çıkarma işlemini kaybeder.","preserves":"Bir işin yetkiliye ulaşması sonucunu kısmen korur."},"text":"bildirmek"}],"identity_rationale":"Kaynak ifadesi genel yaklaştırma çekirdeğini açıkça verir ve kişi ya da anlatılan bir işi yönetici veya yargı yetkisi olan kimsenin önüne getirmeyi bunun kurumsal özel kullanımı olarak gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kullanacaklara yaklaştırılmış döşekler"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yaklaştırma"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yönetici veya yargıç önüne sunmak"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yargılanması için yetkili önüne çıkarmak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"dilekçesini veya şikayetini sunmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"onu iki perdenin bulunduğu yere kadar ilerletmek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"bir topluluğu savaşta öne sürmek"}],"lexicalization_note":"Çıplak biçim yaklaştırmayı anlatır; kişiyi, davayı veya anlatılan işi bir yetkilinin önüne sunan kalıplar bu çekirdeğin kurumsal özel kullanımlarıdır.","neighbor_coverage_note":"Bütün adaylar incelendi; haber yayma, genel yakınlık ve bir sonuca araçla ulaşma dalları sunma eyleminin sınırını en iyi gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın hedefi karar verecek belirli bir yetkilidir ve sunma işlemi öne çıkar; komşu dalın çekirdeği ise haberin görünür ve yaygın hale gelmesidir.","focus_only":"Kişi veya işi belirli bir yetkilinin önüne getirir.","gloss":"yetkiliye sunmak ve haberi yaymak","neighbor_only":"Haberi belirli bir karar makamıyla sınırlamadan açığa çıkarıp yayar.","neighbor_ref":"root_000582/B005","relation_type":"near_neighbor","shared_zone":"İki dalda da bir içeriğin başka kişilere ulaştırılması görülebilir."},{"boundary_match":"partial","distinction":"Odak dal genel yaklaştırmaya ek olarak kurumsal sunmayı içerir; komşu dal ise fiziksel ve ilişkisel yakınlığın daha geniş alanına yayılır.","focus_only":"Yetkili önüne kişi, dava veya anlatılan iş sunma kullanımını içerir.","gloss":"yaklaştırmak ve yakın olmak","neighbor_only":"Yakınlık, akrabalık ve iki şey arasında yakınlaşma gibi daha geniş ilişkileri kapsar.","neighbor_ref":"root_000493/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyi daha yakın konuma getirme anlamında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal sunulan kişi ya da işin yetkiliye yaklaştırılmasına dayanır; komşu dal ise sonuca götüren bir aracın veya dayanağın kullanılmasına dayanır.","focus_only":"Kişiyi veya işi bizzat yetkilinin önüne çıkarır.","gloss":"yetkili önüne sunmak ve araç ileri sürmek","neighbor_only":"Bir sonuca ulaşmak için kanıt, hak, mal veya aracı ileri sürer.","neighbor_ref":"root_000485/B004","relation_type":"near_neighbor","shared_zone":"İki dal da bir hüküm veya istenen sonuç karşısında bir şeyi öne getirmeyi içerir."}],"source_phrase_ar":"الرفع تقريب الشيء (maqayis;sihah); رفعته للسلطان (maqayis); رفعته إلى السلطان (sihah); رفعت فلانا إلى الحاكم أي قدمته إليه (tahdhib); رفعت قصتي قدمتها (tahdhib)","source_summary":"Kanıtlar genel yaklaştırma ile yönetici ya da yargıç önüne sunmayı aynı öne getirme yönünde birleştirir; kurumsal örnek çekirdeği bütünüyle daraltmaz.","sources":["MQ","SI","TA"],"what_is_ar":"تقريب الشيء أو تقديم الشخص أو القصة إلى سلطان أو حاكم","what_is_not_ar":"ليس إذاعة الخبر ولا علو المكان"},"support_links":["sup_058f9716ab94eb420ec9"]},{"boundary":"Dal haberin görünür ve yaygın hale gelmesini gerektirir; yalnızca bir yetkiliye sunmak veya haber istemek yeterli değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B005","candidate_links":[{"candidate_id":"cand_2fe037f63489e9959902","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَفَعَ","morph_features":"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P","morpheme_role":"STEM","pos":"V","qac_ref":"94:4:1:2","qac_word_ref":"94:4:1","surface_ar":"رَفَعْ"}],"gloss":"haberi açığa çıkarıp yaymak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir haberi açığa çıkarıp insanlar arasında yaymak."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aktardığı haberi başkalarına ulaştırıp yayan topluluk."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir haberin gizli veya dar çevrede kalmaktan çıkıp başkalarına duyurulduğu bağlamlarda uygundur.","boundary_detail":"Dal haberin görünür ve yaygın hale gelmesini gerektirir; yalnızca bir yetkiliye sunmak veya haber istemek yeterli değildir.","branch_image_ar":"إذاعة الخبر","concept_gloss":"haberi açığa çıkarıp yaymak","contextual_glosses":[{"applicability":"Haberin bir topluluk aracılığıyla birçok kişiye ulaştırıldığı akıcı metin bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Daha önce gizli olan içeriği açığa çıkarma ayrıntısını açıkça söylemez.","preserves":"Haberi başkalarına ulaştırma ve yayma işlemini korur."},"facet_ids":["F001","F002"],"text":"duyurup yaymak","usage_role":"contextual"}],"definition":"Bir haberi gizli veya sınırlı kaldığı durumdan çıkararak başkalarının bilgisine açmak ve yaymaktır. Haberi taşıyıp duyuran topluluk bu eyleme bağlı bir kullanım oluşturur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir haberi açığa çıkarıp insanlar arasında yaymak."},{"facet_id":"F002","role":"associated_use","statement":"Aktardığı haberi başkalarına ulaştırıp yayan topluluk."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Tek kişiye özel ve yayılmayan her türlü bilgilendirmeyi de kapsar.","collision":"Açığa çıkarma ve yayma koşulları görünmez hale gelir.","fit":"broadening","loses":null,"preserves":"Bir içeriği başkasının bilgisine ulaştırmayı korur."},"text":"haber vermek"}],"identity_rationale":"Kaynak ifadesi bir şeyi, özellikle gizli kalmış bir haberi açığa çıkarıp yaymayı ve bunu aktaran bir topluluğu açıkça aynı duyurma alanında toplar.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"açığa çıkarıp yayma"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"birinin yönetici hakkındaki haberini yaymak"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"iletileni duyurup yayan topluluk"}],"lexicalization_note":"Çıplak biçim açığa çıkarıp yaymayı anlatır; belirli kişi ve yönetici ilişkisine bağlı kalıp ile haber taşıyan topluluk adı ayrı gerçekleşmeler olarak korunur.","neighbor_coverage_note":"Bütün aday haber ve iletişim kartları değerlendirildi; yayılma durumu, haberin kendisi ve yetkiliye sunma eylemi en yararlı üç sınır olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal duyuran kişinin veya topluluğun etkin yayma eylemine dayanır; komşu dal ise haberin yaygınlaşma durumunu ve konuşmanın genişlemesini de kapsar.","focus_only":"Bir haberi etkin biçimde açığa çıkarıp yaymayı anlatır.","gloss":"haberi yaymak ve haberin yayılması","neighbor_only":"Sözün veya haberin taşarcasına kendiliğinden yayılmasını ve konuşmaya dalmayı da kapsar.","neighbor_ref":"root_001192/B003","relation_type":"near_synonym","shared_zone":"İki dalda da haberin başlangıçtaki dar çevresinin dışına çıkması bulunur."},{"boundary_match":"partial","distinction":"Odak dal içeriğin yaygın hale getirilmesine odaklanır; komşu dal ise haber türündeki içeriği ve bildirme ilişkisini, yayılma şartı olmadan kapsar.","focus_only":"Haberin açığa çıkarılıp yayılma sürecini anlatır.","gloss":"haberi yaymak ve haber","neighbor_only":"Haberin kendisini ve onu bildirme ya da öğrenme ilişkilerini anlatır.","neighbor_ref":"root_001464/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal haberin kişiler arasında bilgi olarak aktarılması alanındadır."},{"boundary_match":"partial","distinction":"Odak dalda amaç haberin görünür ve yaygın olmasıdır; komşu dalda amaç belirli kişi veya işin yetkili tarafından değerlendirilmesidir.","focus_only":"Haberi geniş bir çevrenin bilgisine açar.","gloss":"haberi yaymak ve yetkiliye sunmak","neighbor_only":"Kişi veya işi karar verecek belirli bir yetkili önüne getirir.","neighbor_ref":"root_000582/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da bir içerik ilk sahibinden başka bir alıcıya ulaştırılır."}],"source_phrase_ar":"الرفع إذاعة الشيء وإظهاره (maqayis); كل رافعة رفعت علينا من البلاغ (maqayis;sihah;tahdhib); رفع فلان على العامل إذا أذاع خبره (maqayis;tahdhib); أذاع خبر ما احتجبه (mufradat)","source_summary":"Kanıtlar haberin gizlilikten çıkarılıp yayılmasında birleşir; haberi duyuran topluluk, temel yayma eyleminin katılımcısı olarak ayrıca belirtilir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"إظهار الخبر وإشاعته والتبليغ عن القائل","what_is_not_ar":"ليس مجرد تقديم الخصومة إلى الحاكم"},"support_links":["sup_b1ac507966f3e5c68cdd"]},{"boundary":"Dal hasat sonrası taşıma aşamasına bağlıdır; ekini biçme, ürünün kendisi veya genel kaldırma anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَفَعَ","morph_features":"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P","morpheme_role":"STEM","pos":"V","qac_ref":"94:4:1:2","qac_word_ref":"94:4:1","surface_ar":"رَفَعْ"}],"gloss":"hasat ürününü harman yerine taşımak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hasat edilmiş ürünü harman yerine taşımak."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ürünün harman yerine taşındığı zamanı veya bu taşıma işini adlandırmak."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Biçilmiş ürünün hasattan sonra tarladan harman yerine götürüldüğü tarımsal aşama için uygundur.","boundary_detail":"Dal hasat sonrası taşıma aşamasına bağlıdır; ekini biçme, ürünün kendisi veya genel kaldırma anlamına genişletilmez.","branch_image_ar":"رفع الزرع","concept_gloss":"hasat ürününü harman yerine taşımak","contextual_glosses":[{"applicability":"İşlemin kendisinden çok hasat ürününün harman yerine taşındığı zaman diliminin adlandırıldığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli tarımsal işlemin gerçekleştiği zaman dilimini korur."},"facet_ids":["F002"],"text":"ürün taşıma dönemi","usage_role":"contextual"}],"definition":"Hasat edilen ürünü tarladan alıp harman yerine taşımaktır. Aynı kullanım bu taşıma işinin yapıldığı dönemi de adlandırabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hasat edilmiş ürünü harman yerine taşımak."},{"facet_id":"F002","role":"extension","statement":"Ürünün harman yerine taşındığı zamanı veya bu taşıma işini adlandırmak."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ürünü kesip toplama biçimindeki önceki aşamayı ekler.","collision":"Taşıma işlemini biçme işlemiyle karıştırır.","fit":"displacement","loses":"Biçilmiş ürünü harman yerine taşıma aşamasını kaybeder.","preserves":"Aynı tarımsal üretim çevrimini korur."},"text":"hasat etmek"}],"identity_rationale":"Kaynak ifadesi, ürünü hasattan sonra harman yerine taşıma işlemini açıkça tanımlar ve aynı adın bu işin yapıldığı dönem için de kullanıldığını gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"hasat edilen ürünü harman yerine taşımak"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"ürünün harman yerine taşındığı dönem veya bu iş"}],"lexicalization_note":"Kalıba bağlı kullanım hasat edilmiş ürünü harman yerine taşımayı anlatır; biçim birimi ise bu işlemle onun zamanını adlandırır ve genel fiziksel kaldırma anlamına açılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; biçme aşaması, taşımanın varış yeri ve genel fiziksel kaldırma bu tarımsal kullanımın sınırlarını en açık gösteren ilişkilerdir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal ürünü tarlada kesme aşamasıdır; odak dal ise kesilmiş ürünü bundan sonra harman yerine götürme aşamasıdır.","focus_only":"Biçilmiş ürünü harman yerine taşır.","gloss":"ürünü taşımak ve ürünü biçmek","neighbor_only":"Tarladaki ürünü kesip hasat eder ve hasat zamanını da kapsar.","neighbor_ref":"root_000327/B001","relation_type":"near_neighbor","shared_zone":"İki dal aynı hasat sürecinin art arda gelen aşamalarını anlatır."},{"boundary_match":"thematic_only","distinction":"Odak dal bir işlem ve dönemdir; komşu dal bu işlemin ulaştığı, ürünün biriktirildiği veya işlendiği mekandır.","focus_only":"Ürünü belirli yere götüren taşıma işlemini anlatır.","gloss":"harman yerine taşımak ve harman yeri","neighbor_only":"Ürünün toplandığı veya dövüldüğü yerin kendisini anlatır.","neighbor_ref":"root_000093/B007","relation_type":"thematic","shared_zone":"Harman yeri odak daldaki taşımanın varış noktasıdır."},{"boundary_match":"partial","distinction":"Odak dalda yönün yukarı olması gerekmez; tarımsal nesne, hasat sonrası zaman ve harman yeri zorunludur. Komşu dalda ise ayırıcı unsur yukarı yöndür.","focus_only":"Hasat edilmiş ürünü harman yerine götürme aşamasına bağlıdır.","gloss":"ürünü harman yerine taşımak ve yukarı kaldırmak","neighbor_only":"Herhangi bir fiziksel nesneyi daha yüksek konuma taşımayı anlatır.","neighbor_ref":"root_000582/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal fiziksel bir nesnenin bulunduğu yerden taşınmasını içerebilir."}],"source_phrase_ar":"رفع الزرع أن يحمل بعد الحصاد إلى البيدر (maqayis;sihah); جاء زمن الرفاع إذا رفع الزرع (tahdhib); الرفاع أن يحصد الزرع ويرفع (tahdhib)","source_summary":"Kanıtlar hasattan sonraki ürün taşıma aşamasında birleşir; işlem ile bu işlemin zamanı aynı tarımsal çevrim içinde birbirine bağlı iki görünüm olarak sunulur.","sources":["MQ","SI","TA"],"what_is_ar":"حمل الزرع بعد حصاده إلى البيدر وزمن ذلك","what_is_not_ar":"ليس رفع الجسم مطلقا ولا رفع القدر"},"support_links":[]},{"boundary":"Dal yalnızca dişi devenin sütü memede tutması ve süt vermemesi kalıbına bağlıdır; genel süt birikmesi veya sağım anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000582/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَفَعَ","morph_features":"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P","morpheme_role":"STEM","pos":"V","qac_ref":"94:4:1:2","qac_word_ref":"94:4:1","surface_ar":"رَفَعْ"}],"gloss":"dişi devenin sütünü memesinde tutması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi devenin memedeki sütü tutup sağım sırasında vermemesi."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi devenin sütü bulunduğu halde onu vermediği özel hayvancılık bağlamı için uygundur.","boundary_detail":"Dal yalnızca dişi devenin sütü memede tutması ve süt vermemesi kalıbına bağlıdır; genel süt birikmesi veya sağım anlamı değildir.","branch_image_ar":"رفع اللبن في الضرع","concept_gloss":"dişi devenin sütünü memesinde tutması","contextual_glosses":[{"applicability":"Özne dişi deve ve bağlam memedeki sütün tutulması olduğunu zaten açıkça gösterdiğinde kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sütün memede tutulması işlemini ve ilk süt ayrıntısını açıkça söylemez.","preserves":"Sağımda sütün verilmemesi sonucunu korur."},"facet_ids":["F001"],"text":"sütünü vermemek","usage_role":"contextual"}],"definition":"Dişi devenin sütünü veya doğumdan sonraki ilk sütünü memesinde tutması ve bu nedenle süt vermemesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi devenin memedeki sütü tutup sağım sırasında vermemesi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sütün tutulmadığı ve olağan biçimde sağılabildiği her türlü doluluğu da kapsar.","collision":"Etkin biçimde süt vermeme sınırını sıradan dolulukla karıştırır.","fit":"broadening","loses":null,"preserves":"Sütün memede bulunması durumunu korur."},"text":"sütü birikmek"}],"identity_rationale":"Kaynak ifadesi, dişi devenin sütünü veya doğumdan sonraki ilk sütünü memesinde tutup vermemesini açıkça tanımlar; geçici doluluk tek başına yeterli değildir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"sütünü veya ilk sütünü memesinde tutup vermeyen dişi deve"}],"lexicalization_note":"Tanım yalnızca sütünü veya ilk sütünü memesinde tutup vermeyen dişi deve kalıbına bağlıdır ve çıplak kök anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sütü salma karşıtlığı, uyarı gerektiren sağım ve ilk sütün koyulaşması dalın sınırını en açık gösteren üç karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal sütün tutulduğu uçtadır; komşu dal ise sütün herhangi bir sağım olmadan dışarı çıktığı karşı uçtadır.","focus_only":"Sütü memede tutar ve dışarı vermemeyi belirtir.","gloss":"sütü tutmak ve sütün kendiliğinden çıkması","neighbor_only":"Sütün sağım olmadan kendiliğinden dışarı çıkmasını belirtir.","neighbor_ref":"root_001528/B005","relation_type":"polarity_pair","shared_zone":"İki dal memedeki sütün dışarı çıkıp çıkmaması eksenini paylaşır."},{"boundary_match":"partial","distinction":"Odak dal memedeki sütü tutma durumuna dayanır; komşu dal ise süt akışını başlatmak için gereken özel burun uyarısını ayırıcı özellik yapar.","focus_only":"Sütü memede tutma durumunu doğrudan adlandırır.","gloss":"sütü tutan deve ve uyarılınca süt veren deve","neighbor_only":"Süt vermesi için burnuna dokunulması gereken özel bir dişi deve türünü anlatır.","neighbor_ref":"root_001482/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal sütü olağan sağımda hemen vermeyen dişi deveyi anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal sütün dışarı verilmemesine ilişkindir; komşu dal ise sütün kıvamındaki değişimi anlatır ve süt vermeme davranışını zorunlu kılmaz.","focus_only":"Hayvanın sütü vermemesi davranışını belirtir.","gloss":"sütü tutmak ve ilk sütün koyulaşması","neighbor_only":"İlk sütün memede koyulaşıp bağlanmasını belirtir.","neighbor_ref":"root_001625/B010","relation_type":"near_neighbor","shared_zone":"İki dal da dişi devenin memesindeki ilk sütle ilgili bir durumu anlatır."}],"source_phrase_ar":"ناقة رافع إذا رفعت اللبأ في ضرعها (maqayis;sihah); التي رفعت لبنها فلم تدر رافع (tahdhib)","source_summary":"Kanıtlar memedeki sütün, özellikle ilk sütün tutulması ile hayvanın süt vermemesi sonucunu aynı yapı içinde birleştirir.","sources":["MQ","SI","TA"],"what_is_ar":"حبس الناقة لبنها أو لبأها في ضرعها فلا تدر","what_is_not_ar":"ليس دفع اللبأ في الضرع"},"support_links":[]},{"boundary":"Dal kalçayı büyük gösterme amacıyla kullanılan dolgu nesnesidir; genel giysi astarı veya beden niteliği değildir.","branch_kind":"bare","branch_ref":"root_000582/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَفَعَ","morph_features":"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P","morpheme_role":"STEM","pos":"V","qac_ref":"94:4:1:2","qac_word_ref":"94:4:1","surface_ar":"رَفَعْ"}],"gloss":"kalçayı büyük gösteren dolgu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadının kalçasını daha büyük göstermek amacıyla kullanılan dolgu nesnesi."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Giysi altında kullanılarak kadının kalçasını daha büyük göstermeye yarayan nesneyi adlandırır.","boundary_detail":"Dal kalçayı büyük gösterme amacıyla kullanılan dolgu nesnesidir; genel giysi astarı veya beden niteliği değildir.","branch_image_ar":"الرِفاعة للمرأة","concept_gloss":"kalçayı büyük gösteren dolgu","contextual_glosses":[{"applicability":"Nesnenin giysi altındaki işlevini açıkça belirtmek gereken açıklayıcı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalçayı daha büyük gösteren destek nesnesi işlevini korur."},"facet_ids":["F001"],"text":"beden biçimlendirici kalça dolgusu","usage_role":"explanatory"}],"definition":"Bir kadının kalçasını gerçekte olduğundan daha büyük göstermek için giysisinin altında kullandığı dolgu veya destek nesnesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadının kalçasını daha büyük göstermek amacıyla kullanılan dolgu nesnesi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Giysinin iç yüzünü kaplayan her türlü astar işlevini ekler.","collision":"Yapısal giysi parçasıyla görünüm değiştirici dolguyu karıştırır.","fit":"displacement","loses":"Kalçayı daha büyük gösterme işlevini ve beden bölgesini kaybeder.","preserves":"Giysinin altında yer alan bir malzeme olabilmesini korur."},"text":"giysi astarı"}],"identity_rationale":"Kaynak ifadesi, bir kadının kalçasını daha büyük göstermek için kullandığı nesneyi doğrudan tanımlar ve bu işlevi nesnenin kurucu özelliği yapar.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"kadının kalçasını büyük göstermek için kullandığı dolgu"}],"lexicalization_note":"Dal, tek başına adlandırılan beden biçimlendirici nesneyi tanımlar; başka kalıplardan anlam aktarılmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; tam eşleşen beden dolgusu ile yalnızca yer bakımından yakın olan giysi astarı yayıma değer iki sınır olarak seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kartlarda görülen çekirdek, kullanıcı, beden bölgesi ve amaç bakımından aynıdır; olağan kullanımda birbirlerinin yerine geçebilirler.","focus_only":null,"gloss":"kalçayı büyük gösteren dolgu","neighbor_only":null,"neighbor_ref":"root_001029/B008","relation_type":"synonym","shared_zone":"İki dal da kadının kalçasını daha büyük göstermek için yastık benzeri bir destek nesnesi kullanmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalın zorunlu işlevi beden görünümünü değiştirmektir; komşu dal ise giysiyi içten kaplar ve kalçayı büyütme amacı taşımaz.","focus_only":"Kalçanın görünümünü büyütmek için belirli bir yere yerleştirilir.","gloss":"kalça dolgusu ve giysi astarı","neighbor_only":"Giysinin veya örtünün iç yüzünü kaplayan genel bir katmandır.","neighbor_ref":"root_000128/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal giysinin dış katmanının altında bulunan bir malzemeyi anlatabilir."}],"source_phrase_ar":"الرفاعة ما تتعظم به المرأة الرسحاء (sihah); الرفاعة شيء تعظم به المرأة عجيزتها (tahdhib); الرفاعة ما ترفع به المرأة عجيزتها (mufradat)","source_summary":"Kanıtlar nesnenin kim tarafından ve hangi beden bölgesini büyük göstermek için kullanıldığı konusunda birleşir; biçimlendirme işlevi tanımın merkezindedir.","sources":["SI","TA","MU"],"what_is_ar":"الرِفاعة التي تعظم بها المرأة عجيزتها","what_is_not_ar":"ليس حبل القيد ولا رفعة القدر"},"support_links":[]},{"boundary":"Dal bağın kendisi değil, bağlı kişinin o bağı yukarı kaldırmasına yarayan yardımcı iptir.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَفَعَ","morph_features":"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P","morpheme_role":"STEM","pos":"V","qac_ref":"94:4:1:2","qac_word_ref":"94:4:1","surface_ar":"رَفَعْ"}],"gloss":"bağı yukarı çekmeye yarayan ip","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bağlı kişinin bağını eline doğru yukarı kaldırmasını sağlayan ip."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bağlı kişinin kendi bağını eline doğru kaldırmak için kullandığı özel yardımcı ipi adlandırır.","boundary_detail":"Dal bağın kendisi değil, bağlı kişinin o bağı yukarı kaldırmasına yarayan yardımcı iptir.","branch_image_ar":"رِفاع القيد","concept_gloss":"bağı yukarı çekmeye yarayan ip","contextual_glosses":[{"applicability":"Kullanıcının bağlı olduğu ve ipin bağın ağırlığını yukarı almak için kullanıldığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İpin bağ kaldırma işlevini kısa biçimde korur."},"facet_ids":["F001"],"text":"bağ kaldırma ipi","usage_role":"contextual"}],"definition":"Bağlı bir kişinin elinde tutup ayağındaki veya bedenindeki bağı kendine doğru yukarı çekmek için kullandığı yardımcı iptir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bağlı kişinin bağını eline doğru yukarı kaldırmasını sağlayan ip."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kişiyi doğrudan kısıtlayan asıl bağ veya demir halka anlamını ekler.","collision":"Yardımcı ipi kaldırdığı bağın kendisiyle karıştırır.","fit":"displacement","loses":"Bağı yukarı çekmeye yarayan yardımcı ip işlevini kaybeder.","preserves":"Bağlı kişinin kısıtlanmasıyla ilgili nesne alanını korur."},"text":"pranga"}],"identity_rationale":"Kaynak ifadesi, bağlı kişinin elinde tutarak bağını veya prangasını kendine doğru yukarı çektiği ipi açıkça tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"bağlı kişinin bağını yukarı çekmekte kullandığı ip"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bağlı kişinin elinde tutup bağını kaldırdığı ip"}],"lexicalization_note":"Biçim birimi yardımcı ipi adlandırır; bağlı kişiye özgü kalıp aynı nesnenin kullanımını açıklar ve genel ip ya da bağ anlamına genişletilmez.","neighbor_coverage_note":"Bütün bağ ve ip adayları karşılaştırıldı; asıl bağ, yapısıyla tanımlanan deri bağ ve bağlama eylemi yardımcı ipin işlevsel sınırını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kısıtlamayı kurmaz, asıl bağın taşınmasını kolaylaştırır; komşu dal ise doğrudan bağlama ve kısıtlama aracıdır.","focus_only":"Var olan bağı yukarı çekmeye yarayan yardımcı iptir.","gloss":"bağ kaldırma ipi ve bağ","neighbor_only":"Hayvanı veya başka bir varlığı doğrudan kısıtlayan bağın kendisidir.","neighbor_ref":"root_000813/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bağlama düzeninde kullanılan ip veya kordon türü nesnelerle ilgilidir."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı yönü kullanım işlevidir; komşu dalın ayırıcı yönü ise doğrudan bağ oluşu ile deri ve sıkı büküm özellikleridir.","focus_only":"Bağlı kişinin kendi bağını eline doğru kaldırma işleviyle tanımlanır.","gloss":"yardımcı kaldırma ipi ve deri bağ","neighbor_only":"Deriden yapılmış kısa ve sıkı bükümlü bir bağ türü olarak malzemesi ve yapısıyla tanımlanır.","neighbor_ref":"root_000946/B012","relation_type":"near_neighbor","shared_zone":"Her iki dal kısıtlama düzeninde kullanılan kısa ip veya bağ nesnelerini anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dal mevcut kısıtlama içindeki yardımcı bir nesnedir; komşu dal ise kısıtlamayı kuran bağlama eylemi ve araçlarına odaklanır.","focus_only":"Bağlı kişinin hareketini kolaylaştırmak için bağı yukarı alır.","gloss":"bağı kaldıran ip ve bağlayıp kısıtlama","neighbor_only":"Esiri bağlayıp hareketini sınırlama eylemini ve bağlama araçlarını anlatır.","neighbor_ref":"root_000868/B002","relation_type":"same_field","shared_zone":"İki dal bağlı kişi, bağ ve kısıtlama düzeni alanını paylaşır."}],"source_phrase_ar":"رفاعة المقيد خيط يرفع به قيده إليه (sihah); الرفاع حبل القيد يأخذه المقيد بيده يرفعه إليه (tahdhib)","source_summary":"Kanıtlar ipin bağlı kişi tarafından elde tutulması ve bağın yukarı çekilmesini sağlaması konusunda birleşir; nesne doğrudan bağın kendisi olarak tanımlanmaz.","sources":["SI","TA"],"what_is_ar":"حبل أو خيط يرفع به المقيد قيده","what_is_not_ar":"ليس رِفاعة المرأة ولا رفع الحصاد"},"support_links":[]},{"boundary":"Dal yalnızca sesin yüksekliğini adlandıran kalıba bağlıdır; genel ses, konuşma ve toplumsal yücelik anlamlarını kapsamaz.","branch_kind":"collocation","branch_ref":"root_000582/B010","candidate_links":[{"candidate_id":"cand_2fe037f63489e9959902","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَفَعَ","morph_features":"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P","morpheme_role":"STEM","pos":"V","qac_ref":"94:4:1:2","qac_word_ref":"94:4:1","surface_ar":"رَفَعْ"}],"gloss":"sesin yüksekliği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sesin güçlü ve yüksek düzeyde işitilmesi niteliği."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir sesin işitilebilir güç düzeyinin yüksek oluşunu adlandıran bağlam için uygundur.","boundary_detail":"Dal yalnızca sesin yüksekliğini adlandıran kalıba bağlıdır; genel ses, konuşma ve toplumsal yücelik anlamlarını kapsamaz.","branch_image_ar":"رِفاعة الصوت","concept_gloss":"sesin yüksekliği","contextual_glosses":[{"applicability":"Sesin belirgin ve güçlü işitildiği niteliği daha doğal bir sıfatlaştırmayla vermek için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yükseklik derecesini doğrudan adlandırmak yerine sesin dolgunluğunu öne çıkarabilir.","preserves":"Sesin güçlü ve belirgin işitilmesini korur."},"facet_ids":["F001"],"text":"gür seslilik","usage_role":"contextual"}],"definition":"Bir sesin işitilebilir güç bakımından yüksek olma niteliğidir; ses çıkarma eyleminden çok ses düzeyini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sesin güçlü ve yüksek düzeyde işitilmesi niteliği."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İstemli bir ses çıkarma eylemini ve çoğu kez öfke ya da çağrı bağlamını ekler.","collision":"Ses düzeyi niteliğini belirli bir insan eylemiyle karıştırır.","fit":"broadening","loses":null,"preserves":"Yüksek ses çıkarılabilmesini korur."},"text":"bağırma"}],"identity_rationale":"Kaynak ifadesi bu dalı sesin yüksek olması niteliğiyle sınırlar; bağırma eylemi veya belirli bir çağrı türü tanımın zorunlu parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"sesin yüksekliği"}],"lexicalization_note":"Tanım sesin yüksekliğini belirten kalıba bağlı tutulur ve çıplak biçime ya da her türlü yüksekliğe genellenmez.","neighbor_coverage_note":"Bütün ses adayları değerlendirildi; bağırma, çağrıda sesi yükseltme ve sesin gövdeli oluşu yüksek ses niteliğinin üç yararlı sınırı olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ses düzeyinin niteliğidir; komşu dal ise yüksek sesin çıkarıldığı bağırma ve seslenme eylemlerine kadar uzanır.","focus_only":"Sesin yüksek olma niteliğini eylemden bağımsız adlandırır.","gloss":"yüksek ses ve bağırma","neighbor_only":"Bağırma, haykırma ve karşılıklı seslenme eylemlerini de kapsar.","neighbor_ref":"root_000895/B001","relation_type":"near_synonym","shared_zone":"Her iki dal güçlü ve yüksek işitilen ses alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal bağlamdan bağımsız bir ses niteliğidir; komşu dal ise çağrı amacı ve sesi yükseltme eylemiyle sınırlıdır.","focus_only":"Herhangi bir sesin yüksekliğini belirtir.","gloss":"ses yüksekliği ve yüksek sesle çağırma","neighbor_only":"Özellikle çağrı sırasında sesi yükseltme ve abartılı seslenme eylemini belirtir.","neighbor_ref":"root_001484/B004","relation_type":"near_synonym","shared_zone":"İki dal da sesin olağandan yüksek düzeye çıkmasıyla ilgilidir."},{"boundary_match":"partial","distinction":"Odak dal yalnızca yükseklik derecesine dayanır; komşu dal sesin gövdesi ya da çıkışı gibi farklı ve daha tartışmalı bir niteliğe dayanır.","focus_only":"Sesin yüksek işitilme derecesini güvenli biçimde anlatır.","gloss":"ses yüksekliği ve sesin gövdesi","neighbor_only":"Sesin gövdeli oluşunu veya dışarı çıkmasını, kaynakların çekincesi bulunan özel bir kullanımla anlatır.","neighbor_ref":"root_000239/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal sesin belirgin ve güçlü algılanan yönüyle ilgilidir."}],"source_phrase_ar":"في صوته رفاعة ورفاعة (sihah;tahdhib); إذا كان رفيع الصوت (tahdhib)","source_summary":"Kanıtlar kullanımın sesle kurulan özel bir kalıba bağlı olduğu ve yüksek ses niteliğini anlattığı konusunda birleşir.","sources":["SI","TA"],"what_is_ar":"علو الصوت المسمى رِفاعة أو رَفاعة","what_is_not_ar":"ليس رفعة القدر ولا إعلاء الجسم"},"support_links":["sup_b1ac507966f3e5c68cdd"]},{"boundary":"Dal toplulukların ülke içinde ilerlemesini anlatan özel seyahat kullanımıdır; binek yürüyüşü ve genel fiziksel kaldırma değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَفَعَ","morph_features":"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P","morpheme_role":"STEM","pos":"V","qac_ref":"94:4:1:2","qac_word_ref":"94:4:1","surface_ar":"رَفَعْ"}],"gloss":"toplulukça ülke içinde ilerlemek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun ülke içinde yola koyulup ilerlemesi."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir topluluğun ülke içinde yola koyulup ilerlediği özel kullanım için uygundur.","boundary_detail":"Dal toplulukların ülke içinde ilerlemesini anlatan özel seyahat kullanımıdır; binek yürüyüşü ve genel fiziksel kaldırma değildir.","branch_image_ar":"الإصعاد في البلاد","concept_gloss":"toplulukça ülke içinde ilerlemek","contextual_glosses":[{"applicability":"Toplulukların ülke içinde yola koyulmasını açıkça belirtmek gereken açıklayıcı veya sözlük bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluğun yola çıkmasını ve ülke içindeki ilerleyişini korur."},"facet_ids":["F001"],"text":"toplulukça ülke içinde yola koyulmak","usage_role":"explanatory"}],"definition":"Bir topluluğun ülke içinde yola koyulup ilerlemesidir. Kullanım her türlü yolculuğa genişletilmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun ülke içinde yola koyulup ilerlemesi."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Tek kişinin yolculuğunu, her yönü ve her türlü seyahat amacını sınırsız biçimde kapsar.","collision":"Topluluk ve özel yön çerçevesi görünmez olur.","fit":"broadening","loses":null,"preserves":"Bir yerden başka yere hareket etme alanını korur."},"text":"seyahat etmek"}],"identity_rationale":"Kaynak ifadesi toplulukların ülke içinde yola koyulup ilerlemesini yukarı yönelme sözüyle anlatır; bunu her türlü yolculuğa veya zorunlu bir yükseklik kazanımına yaymak kanıtı aşar.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"topluluğun ülke içinde yola koyulup ilerlemesi"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"yolculukta ilerleyenler"}],"lexicalization_note":"Topluluğa bağlı kalıp ülke içinde yola koyulmayı anlatır; biçim birimi bu ilerleyen topluluğu adlandırır ve anlam genel seyahate genişletilmez.","neighbor_coverage_note":"Bütün yolculuk adayları değerlendirildi; genel yola çıkma, binek yürüyüşü ve ufuklarda dolaşma bu özel topluluk kullanımının sınırlarını en açık gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal topluluk öznesiyle ülke içindeki ilerlemeyi anlatır; komşu dal ise özne, yolculuğa başlama ve güzergah bakımından daha genel bir hareket alanına sahiptir.","focus_only":"Topluluk öznesine ve ülke içindeki ilerlemeye bağlı özel kullanımdır.","gloss":"toplulukça ilerlemek ve yolculuğa çıkmak","neighbor_only":"Tekil veya çoğul yolcuları, yolculuğa başlama ve ülke ya da vadi içinde her yönde ilerlemeyi daha geniş biçimde kapsar.","neighbor_ref":"root_000862/B002","relation_type":"near_synonym","shared_zone":"İki dal ülke içinde yola koyulma ve ilerleme anlamında geniş ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği topluluğun yer değiştirmesidir; komşu dalın çekirdeği ise binek hayvanının yürüyüş hızı ve biçimidir.","focus_only":"Toplulukların ülke içindeki yolculuğunu anlatır.","gloss":"ülkede ilerlemek ve bineği hızlı yürütmek","neighbor_only":"Binek hayvanının ağır yürüyüş ile tam koşu arasındaki belirli hız biçimini anlatır.","neighbor_ref":"root_000582/B003","relation_type":"near_neighbor","shared_zone":"İki dal yolculuk ve ilerleme sahnesinde görülebilir."},{"boundary_match":"partial","distinction":"Odak dal topluluk öznesiyle ülke içindeki ilerleyişe bağlıdır; komşu dal ise uzaklık, dolaşma ve kazanç amacı gibi geniş yolculuk kullanımlarını içerir.","focus_only":"Toplulukların ülke içinde ilerlemesini anlatır.","gloss":"ülke içinde ilerlemek ve uzaklarda dolaşmak","neighbor_only":"Ufuklara yayılma, kazanç için dolaşma ve uzak yerlerden gelip gitme gibi daha geniş amaçları kapsar.","neighbor_ref":"root_000040/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal ülke içinde veya ülkeler arasında yol alma alanındadır."}],"source_phrase_ar":"رفع القوم فهم رافعون إذا أصعدوا في البلاد (tahdhib); الروافع إذا رفعوا في سيرهم (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı tanıklık, ülke içinde yola koyulan toplulukları ve yolculuktaki ilerleyişlerini adlandırır."}],"source_summary":"Kanıt, toplulukların ülke içinde veya yolculukta ilerlemesini anlatan özel bir kullanım sunar; anlam her türlü seyahate genişletilmemelidir.","sources":["TA"],"what_is_ar":"إصعاد القوم في البلاد أو في السير","what_is_not_ar":"ليس سير الدابة الخاص ولا رفع الشيء باليد"},"support_links":[]},{"boundary":"Dal yalnızca dil bilgisel çekim durumudur; fiziksel yükseltme veya toplumsal yücelik anlamı taşımaz.","branch_kind":"non_bare","branch_ref":"root_000582/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَفَعَ","morph_features":"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P","morpheme_role":"STEM","pos":"V","qac_ref":"94:4:1:2","qac_word_ref":"94:4:1","surface_ar":"رَفَعْ"}],"gloss":"dil bilgisinde ötreye karşılık gelen çekim durumu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcüğün, sabit biçimlerdeki ötreye karşılık gelen dil bilgisel çekim durumunda bulunması."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir sözcüğün çekim düzenindeki bu özel dil bilgisel durumu doğal Türkçe ile adlandırmak için uygundur.","boundary_detail":"Dal yalnızca dil bilgisel çekim durumudur; fiziksel yükseltme veya toplumsal yücelik anlamı taşımaz.","branch_image_ar":"الرفع في الإعراب","concept_gloss":"dil bilgisinde ötreye karşılık gelen çekim durumu","contextual_glosses":[{"applicability":"Terimin sözcük çekimindeki yerini ve sabit biçimlerdeki ötreyle karşılığını açıklayan öğretici bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözcük çekimi ile sabit biçimlerdeki ötre arasındaki karşılığı korur."},"facet_ids":["F001"],"text":"çekimde ötreye karşılık gelen durum","usage_role":"explanatory"}],"definition":"Çekimli bir sözcüğün, sabit biçimlerdeki ötreye karşılık gelen dil bilgisel çekim durumunda bulunmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcüğün, sabit biçimlerdeki ötreye karşılık gelen dil bilgisel çekim durumunda bulunması."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Fiziksel veya toplumsal bir şeyi daha yüksek hale getirme eylemini ekler.","collision":"Dil bilgisi dalını fiziksel kaldırma dalıyla karıştırır.","fit":"displacement","loses":"Dil bilgisel çekim durumu ve uzmanlık terimi olma niteliğini kaybeder.","preserves":"Kaynak kavramdaki yukarı yönlü adlandırma çağrışımını korur."},"text":"yükseltme"}],"identity_rationale":"Kaynak ifadesi dalı dil bilgisi uzmanlarının koyduğu çekim terimi olarak açıkça sınırlar ve çekimli sözcüklerdeki bu durumu sabit biçimlerdeki belirli son ses işaretiyle karşılaştırır.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"dil bilgisinde ötreye karşılık gelen çekim durumu"}],"lexicalization_note":"Anlam yalnızca dil bilgisi terimi olan özel sözlük birimine bağlıdır ve çıplak kökün fiziksel ya da değer bildiren anlamlarına genişletilmez.","neighbor_coverage_note":"Bütün dil bilgisi adayları incelendi; karşı çekim durumu, çekime açıklık ve tümce ögeleri terimin yerini en açık gösteren üç komşu olarak seçildi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal sabit biçimlerdeki ötreye karşılık gelen çekim durumudur; komşu dal ise üstünle ilişkilendirilen karşıt çekim durumunu anlatır.","focus_only":"Sözcüğün ötreyle ilişkilendirilen çekim durumunu belirtir.","gloss":"ötreye ve üstüne karşılık gelen çekim durumları","neighbor_only":"Sözcüğün üstünle ilişkilendirilen karşı çekim durumunu belirtir.","neighbor_ref":"root_001507/B007","relation_type":"antonym","shared_zone":"İki dal aynı dil bilgisel çekim düzeninde birbirine karşıt konumları belirtir."},{"boundary_match":"field_only","distinction":"Odak dal çekim içindeki tek bir konumdur; komşu dal ise sözcüğün böyle konum değişikliklerini alabilme yeteneğini sınıflandırır.","focus_only":"Çekimli sözcüğün belirli bir durumunu adlandırır.","gloss":"belirli çekim durumu ve çekime açıklık","neighbor_only":"Bir adın genel olarak çekime açık, değişebilir veya sabit olma özelliğini adlandırır.","neighbor_ref":"root_001439/B006","relation_type":"same_field","shared_zone":"İki dal adların çekim düzenindeki davranışını konu edinir."},{"boundary_match":"field_only","distinction":"Odak dal biçimsel bir çekim konumudur; komşu dal ise anlam ve görev bakımından farklı nesne türlerini sayar.","focus_only":"Sözcük biçiminin çekim durumunu belirtir.","gloss":"çekim durumu ve tümce ögeleri","neighbor_only":"Tümcede eyleme çeşitli yönlerden bağlanan nesne ve tamamlayıcı türlerini sınıflandırır.","neighbor_ref":"root_001167/B007","relation_type":"same_field","shared_zone":"İki dal dil bilgisinde sözcüklerin tümce içindeki görevleriyle ilgilidir."}],"source_phrase_ar":"الرفع في الإعراب كالضم في البناء (sihah); وهو من أوضاع النحويين (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı tanıklık, terimin uzmanlarca konduğunu ve çekim durumu ile sabit son ses işareti arasında karşılık kurduğunu belirtir."}],"source_summary":"Kanıt bu anlamı uzmanların belirlediği bir çekim terimi olarak sunar ve çekimli sözcükteki durum ile sabit biçimdeki son ses işareti arasında karşılaştırma kurar.","sources":["SI"],"what_is_ar":"الرفع النحوي في الإعراب كالضم في البناء","what_is_not_ar":"ليس الرفع اللغوي للأجسام ولا رفع المنزلة"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["94:4:1"],"branch_refs":[],"candidate_id":"cand_355f652ffa09e69e16d5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:4:1:bound-launch-before-verb","source_type":"word_analysis","support_ids":["sup_06bbf2a092c6a655ce68","sup_d8d4ee2b3ef1cf4d2d07"],"title":"connection is front-loaded","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:1","qac_refs":["94:4:1:1"],"status":"accepted"}},{"anchor_refs":["94:4:1"],"branch_refs":[],"candidate_id":"cand_dff309c6ec100ce2b0e6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:4:1:full-clause-favor-coordination","source_type":"word_analysis","support_ids":["sup_06bbf2a092c6a655ce68","sup_c11fbef0ab484615f108"],"title":"whole clause joined to the favor-chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:1","qac_refs":["94:4:1:1"],"status":"accepted"}},{"anchor_refs":["94:4:1"],"branch_refs":[],"candidate_id":"cand_01f0df3433669e652c9b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:4:1:rhetorical-escalation-and-echo","source_type":"word_analysis","support_ids":["sup_06bbf2a092c6a655ce68","sup_11946e3ee10146c6c9c2"],"title":"repeated connector marks escalation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:1","qac_refs":["94:4:1:1"],"status":"accepted"}},{"anchor_refs":["94:4:2"],"branch_refs":[],"candidate_id":"cand_b7e79336bd5801593800","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"94:4:2:completed-divine-active-agency","source_type":"word_analysis","support_ids":["sup_2647bae280bc02bbd667","sup_d806bbb727f16fdb76ca"],"title":"completed active divine raising","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:2","qac_refs":["94:4:1:2","94:4:1:3"],"status":"accepted"}},{"anchor_refs":["94:4:2"],"branch_refs":[],"candidate_id":"cand_2df086bb427368100c3a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"94:4:2:down-up-reversal-from-burden","source_type":"word_analysis","support_ids":["sup_86a72346fca60263eb47","sup_d806bbb727f16fdb76ca"],"title":"burden lowered, mention raised","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:2","qac_refs":["94:4:1:2","94:4:1:3"],"status":"accepted"}},{"anchor_refs":["94:4:2"],"branch_refs":[],"candidate_id":"cand_e820b043a25892e1e830","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"94:4:2:elevation-exaltation-publicity-range","source_type":"word_analysis","support_ids":["sup_a453aeae46c5b3782793","sup_d806bbb727f16fdb76ca"],"title":"elevation becomes honor and public audibility","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:2","qac_refs":["94:4:1:2","94:4:1:3"],"status":"accepted"}},{"anchor_refs":["94:4:2"],"branch_refs":[],"candidate_id":"cand_324290ed90a95b40cbb1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"94:4:2:form-echo-with-prior-act","source_type":"word_analysis","support_ids":["sup_1ead9bfa409de0ca2453","sup_d806bbb727f16fdb76ca"],"title":"matched form with reversed direction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:2","qac_refs":["94:4:1:2","94:4:1:3"],"status":"accepted"}},{"anchor_refs":["94:4:2"],"branch_refs":[],"candidate_id":"cand_64b6c29884d2afbb52ff","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"94:4:2:form-i-decisive-transitive","source_type":"word_analysis","support_ids":["sup_9f3fa0287d2d1cca13b9","sup_d806bbb727f16fdb76ca"],"title":"simple transitive form avoids passive or self-rise","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:2","qac_refs":["94:4:1:2","94:4:1:3"],"status":"accepted"}},{"anchor_refs":["94:4:2"],"branch_refs":[],"candidate_id":"cand_04fb1ac1960c61ef14ea","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"94:4:2:lowering-raising-intertext","source_type":"word_analysis","support_ids":["sup_156629621f5453995601","sup_d806bbb727f16fdb76ca"],"title":"Quranic lowering-raising polarity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:2","qac_refs":["94:4:1:2","94:4:1:3"],"status":"accepted"}},{"anchor_refs":["94:4:2"],"branch_refs":[],"candidate_id":"cand_0849fc5dd62c6e137e42","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"94:4:2:sound-and-beatline-upturn","source_type":"word_analysis","support_ids":["sup_31b336ab1884f721be2f","sup_d806bbb727f16fdb76ca"],"title":"sound stages release before closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:2","qac_refs":["94:4:1:2","94:4:1:3"],"status":"accepted"}},{"anchor_refs":["94:4:2"],"branch_refs":[],"candidate_id":"cand_ea593b4ca50b321bcd95","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"94:4:2:transitive-benefactive-frame","source_type":"word_analysis","support_ids":["sup_4c0a1a2171abad5923ed","sup_d806bbb727f16fdb76ca"],"title":"raised object kept distinct from beneficiary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:2","qac_refs":["94:4:1:2","94:4:1:3"],"status":"accepted"}},{"anchor_refs":["94:4:3"],"branch_refs":[],"candidate_id":"cand_91e8f75a4d8b82c52112","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:4:3:addressee-convergence","source_type":"word_analysis","support_ids":["sup_3971f226aeceb6a158c3","sup_c7b2744b4e64ed621ffb"],"title":"same addressee as beneficiary and possessor","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:3","qac_refs":["94:4:2:1","94:4:2:2"],"status":"accepted"}},{"anchor_refs":["94:4:3"],"branch_refs":[],"candidate_id":"cand_15e071dbd4cb4a532c66","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:4:3:beneficiary-before-object","source_type":"word_analysis","support_ids":["sup_2a2d466ba93f0c8a976d","sup_3971f226aeceb6a158c3"],"title":"beneficiary foregrounded before object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:3","qac_refs":["94:4:2:1","94:4:2:2"],"status":"accepted"}},{"anchor_refs":["94:4:3"],"branch_refs":[],"candidate_id":"cand_a5b2779786fc87f02bf1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:4:3:beneficiary-not-object","source_type":"word_analysis","support_ids":["sup_3971f226aeceb6a158c3","sup_ac239962decb1eb8620e"],"title":"beneficiary distinct from object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:3","qac_refs":["94:4:2:1","94:4:2:2"],"status":"accepted"}},{"anchor_refs":["94:4:3"],"branch_refs":[],"candidate_id":"cand_9424ca598ee36be5b787","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:4:3:compressed-bound-address","source_type":"word_analysis","support_ids":["sup_3971f226aeceb6a158c3","sup_efdd76f3becc1c267715"],"title":"bound suffix compresses personal address","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:3","qac_refs":["94:4:2:1","94:4:2:2"],"status":"accepted"}},{"anchor_refs":["94:4:3"],"branch_refs":[],"candidate_id":"cand_7d38baf2cb4eea42c550","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:4:3:from-you-for-you-reversal","source_type":"word_analysis","support_ids":["sup_3971f226aeceb6a158c3","sup_b7e1b1f1ddccfeea224d"],"title":"from-you becomes for-you","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:3","qac_refs":["94:4:2:1","94:4:2:2"],"status":"accepted"}},{"anchor_refs":["94:4:4"],"branch_refs":[],"candidate_id":"cand_c05cb9391158f4e90c2e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"94:4:4:addressee-bound-definiteness","source_type":"word_analysis","support_ids":["sup_605d0dd72730a210ca29","sup_aa6ac3a917960182a5b9"],"title":"final suffix binds object to the addressee","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:4","qac_refs":["94:4:3:1","94:4:3:2"],"status":"accepted"}},{"anchor_refs":["94:4:4"],"branch_refs":[],"candidate_id":"cand_d5605a907a9cf684257b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"94:4:4:boundary-shift-to-public-remembrance","source_type":"word_analysis","support_ids":["sup_541ab44ef5d9b5147d98","sup_aa6ac3a917960182a5b9"],"title":"body burden becomes abstract remembrance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:4","qac_refs":["94:4:3:1","94:4:3:2"],"status":"accepted"}},{"anchor_refs":["94:4:4"],"branch_refs":[],"candidate_id":"cand_5f0915f4dab5042956af","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"94:4:4:derived-reminding-pressure","source_type":"word_analysis","support_ids":["sup_62de2dfda44a734d9b2a","sup_aa6ac3a917960182a5b9"],"title":"remembering and reminding derivatives color the noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:4","qac_refs":["94:4:3:1","94:4:3:2"],"status":"accepted"}},{"anchor_refs":["94:4:4"],"branch_refs":[],"candidate_id":"cand_758833b77edd1b0eddc8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"94:4:4:dhikr-semantic-field","source_type":"word_analysis","support_ids":["sup_3fe70f546f49f13ea7c1","sup_aa6ac3a917960182a5b9"],"title":"mention, remembrance, renown, reminder, and scripture pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:4","qac_refs":["94:4:3:1","94:4:3:2"],"status":"accepted"}},{"anchor_refs":["94:4:4"],"branch_refs":[],"candidate_id":"cand_bd2541fa14dcf077395a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"94:4:4:direct-object-of-raising","source_type":"word_analysis","support_ids":["sup_286e586aae943695dcbb","sup_aa6ac3a917960182a5b9"],"title":"the raised entity is the possessed verbal noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:4","qac_refs":["94:4:3:1","94:4:3:2"],"status":"accepted"}},{"anchor_refs":["94:4:4"],"branch_refs":[],"candidate_id":"cand_de59ea21f70be7562e8e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"94:4:4:gender-branch-narrowed","source_type":"word_analysis","support_ids":["sup_1add8dea7c7b52b827c4","sup_aa6ac3a917960182a5b9"],"title":"male-branch tension stays root-level","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:4","qac_refs":["94:4:3:1","94:4:3:2"],"status":"accepted"}},{"anchor_refs":["94:4:4"],"branch_refs":[],"candidate_id":"cand_1a815fada4fdb13316ac","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"94:4:4:gerund-not-alternate-form","source_type":"word_analysis","support_ids":["sup_8dfa276bddaf69c9c6f1","sup_aa6ac3a917960182a5b9"],"title":"possessed gerund chosen over finite or status forms","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:4","qac_refs":["94:4:3:1","94:4:3:2"],"status":"accepted"}},{"anchor_refs":["94:4:4"],"branch_refs":[],"candidate_id":"cand_ac02dce9acdb26b34e53","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"94:4:4:object-delay-and-closure","source_type":"word_analysis","support_ids":["sup_aa6ac3a917960182a5b9","sup_fe1d3cfeaf1bcafef849"],"title":"final object carries closure weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:4","qac_refs":["94:4:3:1","94:4:3:2"],"status":"accepted"}},{"anchor_refs":["94:4:4"],"branch_refs":[],"candidate_id":"cand_fef1a0e6125377ae806b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"94:4:4:phonetic-texture-of-closure","source_type":"word_analysis","support_ids":["sup_aa6ac3a917960182a5b9","sup_d5846d1cfb29023aa888"],"title":"sound arc makes the ending distinct","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:4","qac_refs":["94:4:3:1","94:4:3:2"],"status":"accepted"}},{"anchor_refs":["94:4:4"],"branch_refs":[],"candidate_id":"cand_b147487b993d27a27c6f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"94:4:4:possessive-masdar-ambiguity","source_type":"word_analysis","support_ids":["sup_aa6ac3a917960182a5b9","sup_cc187fe4c23ef91ad271"],"title":"definite object with active-passive possessive range","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:4","qac_refs":["94:4:3:1","94:4:3:2"],"status":"accepted"}},{"anchor_refs":["94:4:4"],"branch_refs":[],"candidate_id":"cand_7a2910af56582595e546","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"94:4:4:scripture-and-record-pressure","source_type":"word_analysis","support_ids":["sup_aa6ac3a917960182a5b9","sup_c5aa6f62462895259cb3"],"title":"revelatory and record register remains available","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:4","qac_refs":["94:4:3:1","94:4:3:2"],"status":"accepted"}},{"anchor_refs":["94:4:4"],"branch_refs":[],"candidate_id":"cand_652d5e40add01180ce8d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"94:4:4:wizr-dhikr-sound-inversion","source_type":"word_analysis","support_ids":["sup_1add1abb261dae5c5940","sup_aa6ac3a917960182a5b9"],"title":"burden sound turns into mention sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:4:4","qac_refs":["94:4:3:1","94:4:3:2"],"status":"accepted"}},{"anchor_refs":["94:4:1"],"branch_refs":[],"candidate_id":"cand_8fd31abe3dfe7988d7d7","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"94:4:1:2","source_type":"qac_morpheme","support_ids":["sup_336ad07f6e667fc01cb5"],"title":"QAC root occurrence: ر ف ع","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["94:4:3"],"branch_refs":[],"candidate_id":"cand_e14d8ec84e98a4213bb9","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"94:4:3:1","source_type":"qac_morpheme","support_ids":["sup_992b00542ea3c3583cf5"],"title":"QAC root occurrence: ذ ك ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["94:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:4","branch_refs":["root_000516/B007","root_000582/B002"],"candidate_id":"cand_fa9f99008a6f5deb3672","commentary_obligation":"review","hft_ref":"hft_c11f45a31a16fb248c1d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_exalted_renown","source_type":"hft","support_ids":["sup_621173ed951ad333045e"],"title":"baseline_exalted_renown","trust":"legacy_unbound"},{"anchor_refs":["94:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:4","branch_refs":["root_000516/B004","root_000582/B005","root_000582/B010"],"candidate_id":"cand_2fe037f63489e9959902","commentary_obligation":"review","hft_ref":"hft_ca8998dd88710fa5a361","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_public_circulation","source_type":"hft","support_ids":["sup_b1ac507966f3e5c68cdd"],"title":"baseline_public_circulation","trust":"legacy_unbound"},{"anchor_refs":["94:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:4","branch_refs":["root_000516/B003","root_000516/B009","root_000582/B001"],"candidate_id":"cand_d69b0821b2f5deaa9ae7","commentary_obligation":"review","hft_ref":"hft_e53466e59f0cbf3e889b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_retrievable_remembrance","source_type":"hft","support_ids":["sup_96e23b245baec5fb564b"],"title":"baseline_retrievable_remembrance","trust":"legacy_unbound"},{"anchor_refs":["94:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:4","branch_refs":["root_000516/B008","root_000582/B004"],"candidate_id":"cand_b35c09b0db7500dc5371","commentary_obligation":"review","hft_ref":"hft_0804103437dea5b7d2e0","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier_juridical_attestation","source_type":"hft","support_ids":["sup_058f9716ab94eb420ec9"],"title":"outlier_juridical_attestation","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَرَفَعْنَا لَكَ ذِكْرَكَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"94:4:1:1","qac_word_ref":"94:4:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"رَفَعَ","morph_features":"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P","morpheme_role":"STEM","pos":"V","qac_ref":"94:4:1:2","qac_word_ref":"94:4:1","root_ar":"ر ف ع","surface_ar":"رَفَعْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"94:4:1:3","qac_word_ref":"94:4:1","root_ar":"","surface_ar":"نَا"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"94:4:2:1","qac_word_ref":"94:4:2","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|2MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"94:4:2:2","qac_word_ref":"94:4:2","root_ar":"","surface_ar":"كَ"},{"lemma_ar":"ذِكْر","morph_features":"STEM|POS:N|VN|LEM:*ikor|ROOT:*kr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:4:3:1","qac_word_ref":"94:4:3","root_ar":"ذ ك ر","surface_ar":"ذِكْرَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"94:4:3:2","qac_word_ref":"94:4:3","root_ar":"","surface_ar":"كَ"}],"word_analysis_qac_refs":[["94:4:1:1"],["94:4:1:2","94:4:1:3"],["94:4:2:1","94:4:2:2"],["94:4:3:1","94:4:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["94:4:1","94:4:2","94:4:3","94:4:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَرَفَعْنَا لَكَ ذِكْرَكَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"94:4:1:1","qac_word_ref":"94:4:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"رَفَعَ","morph_features":"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P","morpheme_role":"STEM","pos":"V","qac_ref":"94:4:1:2","qac_word_ref":"94:4:1","root_ar":"ر ف ع","surface_ar":"رَفَعْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"94:4:1:3","qac_word_ref":"94:4:1","root_ar":"","surface_ar":"نَا"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"94:4:2:1","qac_word_ref":"94:4:2","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|2MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"94:4:2:2","qac_word_ref":"94:4:2","root_ar":"","surface_ar":"كَ"},{"lemma_ar":"ذِكْر","morph_features":"STEM|POS:N|VN|LEM:*ikor|ROOT:*kr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:4:3:1","qac_word_ref":"94:4:3","root_ar":"ذ ك ر","surface_ar":"ذِكْرَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"94:4:3:2","qac_word_ref":"94:4:3","root_ar":"","surface_ar":"كَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["94:4:1:1"],["94:4:1:2","94:4:1:3"],["94:4:2:1","94:4:2:2"],["94:4:3:1","94:4:3:2"]],"word_analysis_refs":["94:4:1","94:4:2","94:4:3","94:4:4"],"word_rows":[{"analysis_record_ref":"94:4:1","analytic_gloss_range_en":"bound coordinating opening that attaches the whole clause to the preceding favor-chain while launching a fresh divine-act assertion","analytic_root_gloss_range_en":null,"qac_refs":["94:4:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"94:4:2","analytic_gloss_range_en":"completed active divine raising or exaltation of an explicit object, with the addressee marked separately as beneficiary","analytic_root_gloss_range_en":"root range includes physical raising, high rank, presentation or making public, raised voice, travel ascent, grammatical raising, and other branch-specific uses; the local clause selects active transitive elevation and exaltation of the addressee-linked mention","qac_refs":["94:4:1:2","94:4:1:3"],"root":{"arabic":"ر ف ع","transliteration":"r-f-ʿ"},"surface":{"arabic":"رَفَعْنَا","transliteration":"rafaʿnā"}},{"analysis_record_ref":"94:4:3","analytic_gloss_range_en":"prepositional phrase marking the addressed beneficiary or specification of the raising, not the raised object","analytic_root_gloss_range_en":null,"qac_refs":["94:4:2:1","94:4:2:2"],"root":{},"surface":{"arabic":"لَكَ","transliteration":"laka"}},{"analysis_record_ref":"94:4:4","analytic_gloss_range_en":"the addressee-bound mention, remembrance, renown, or memorial/revelatory remembrance raised as the direct object, with the possessive verbal noun leaving active and passive directions open","analytic_root_gloss_range_en":"root range includes bringing to mind, mention on the tongue, worshipful remembrance, scripture, honorable renown, reminder or admonition, record/document uses, and separate male or forceful branches; the local possessed gerund selects mention/remembrance/renown while other branches remain only narrowed pressure","qac_refs":["94:4:3:1","94:4:3:2"],"root":{"arabic":"ذ ك ر","transliteration":"dh-k-r"},"surface":{"arabic":"ذِكْرَكَ","transliteration":"dhikraka"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["94:4"],"branch_refs":["root_000516/B007","root_000582/B002"],"candidate_id":"cand_fa9f99008a6f5deb3672","evidence_scope":"focus_ayah","hft_ref":"hft_c11f45a31a16fb248c1d","item_id":"baseline_exalted_renown","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_exalted_renown","support_id":"sup_621173ed951ad333045e"},{"anchor_refs":["94:4"],"branch_refs":["root_000516/B004","root_000582/B005","root_000582/B010"],"candidate_id":"cand_2fe037f63489e9959902","evidence_scope":"focus_ayah","hft_ref":"hft_ca8998dd88710fa5a361","item_id":"baseline_public_circulation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_public_circulation","support_id":"sup_b1ac507966f3e5c68cdd"},{"anchor_refs":["94:4"],"branch_refs":["root_000516/B003","root_000516/B009","root_000582/B001"],"candidate_id":"cand_d69b0821b2f5deaa9ae7","evidence_scope":"focus_ayah","hft_ref":"hft_e53466e59f0cbf3e889b","item_id":"baseline_retrievable_remembrance","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_retrievable_remembrance","support_id":"sup_96e23b245baec5fb564b"},{"anchor_refs":["94:4"],"branch_refs":["root_000516/B008","root_000582/B004"],"candidate_id":"cand_b35c09b0db7500dc5371","evidence_scope":"focus_ayah","hft_ref":"hft_0804103437dea5b7d2e0","item_id":"outlier_juridical_attestation","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_juridical_attestation","support_id":"sup_058f9716ab94eb420ec9"}],"diagnostics":[],"lane_counts":{"global":9,"macro":8,"micro":4},"packet_summary":{"ayah_count":8,"focus_ref":"94:4","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"و ز ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001643","furuq_root_norm":"و ز ر","furuq_source_root_norm":"و ز ر","is_dominant":true,"target_occurrences":24,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000654","furuq_root_norm":"ز و ر","furuq_source_root_norm":"ز و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["94:1","94:2","94:3","94:4","94:5","94:6","94:7","94:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"94:4","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":12,"unstructured_record_count":0},"identity":{"ayah_ref":"94:4","lane":"micro","linguistic_source_ref":"94:4","surface_ref":"94:4","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"94:4","target_tokens":[["Ve",["94:4:1"]],["senin",["94:4:2","94:4:3"]],["anılmanı",["94:4:3"]],["yücelttik",["94:4:1"]]],"text":"Ve senin anılmanı yücelttik."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":8,"id":"s094-p01-001-008","label":"Whole surah","number":1,"refs":["94:1","94:2","94:3","94:4","94:5","94:6","94:7","94:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:1","source_type":"word_analysis","support_id":"sup_06bbf2a092c6a655ce68","text":"{\"gloss_range\":\"bound coordinating opening that attaches the whole clause to the preceding favor-chain while launching a fresh divine-act assertion\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) makes the whole clause arrive already attached to the prior sequence. It is not only a decorative \\\"and\\\": it carries the scope of the raising clause as another completed divine favor after the putting-down act in 94:2. Because the connector is a single bound proclitic at the ayah opening, the reader hears connection before the verb, and the movement from question to successive assertions reaches a new climactic clause.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:1:rhetorical-escalation-and-echo","source_type":"word_analysis","support_id":"sup_11946e3ee10146c6c9c2","text":"{\"blocking_evidence\":null,\"headline\":\"repeated connector marks escalation\",\"reader_payoff\":\"The reader notices the local echo between the earlier burden-removal clause and the present elevation clause, with the same connector carrying the sequence forward.\",\"reason\":\"The concrete same-surah rows compare the repeated connective pattern around 94:2-4, and no local evidence blocks the sequence-level observation.\",\"representative_source_ids\":[\"MT-89da5b43\",\"QE-9b5af28b\",\"QB-754fd9c1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:2:lowering-raising-intertext","source_type":"word_analysis","support_id":"sup_156629621f5453995601","text":"{\"blocking_evidence\":null,\"headline\":\"Quranic lowering-raising polarity\",\"reader_payoff\":\"The reader notices that the local down/up movement belongs to a recognizable Quranic polarity of lowering and raising (56:3).\",\"reason\":\"The source rows give the concrete reference 56:3, and the local ayah itself contains the same semantic opposition through 94:2-4.\",\"representative_source_ids\":[\"QI-1fdeb27f\",\"MI-29534536\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:4:wizr-dhikr-sound-inversion","source_type":"word_analysis","support_id":"sup_1add1abb261dae5c5940","text":"{\"blocking_evidence\":null,\"headline\":\"burden sound turns into mention sound\",\"reader_payoff\":\"The reader notices that the sound of the earlier burden word in 94:2-3 returns in altered form as the word for raised mention.\",\"reason\":\"The rows give the concrete same-surah sound relation between {{ar:وِزْرَكَ}} ({{tr:wizraka}}) in 94:2-3 and {{ar:ذِكْرَكَ}} ({{tr:dhikraka}}) in 94:4.\",\"representative_source_ids\":[\"QE-4bcb53f0\",\"QE-8f4dfda3\",\"ME-c0a2e1a1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:4:gender-branch-narrowed","source_type":"word_analysis","support_id":"sup_1add8dea7c7b52b827c4","text":"{\"blocking_evidence\":null,\"headline\":\"male-branch tension stays root-level\",\"reader_payoff\":\"The reader notices that Arabic places remembrance and male-marked social presence in the same root space, while the ayah's chosen gerund keeps the local object abstract.\",\"reason\":\"V4 accepts male and forceful branches for {{ar:ذ ك ر}} ({{tr:dh-k-r}}), but local grammar selects the verbal noun of mention/remembrance rather than the concrete noun {{ar:ٱلذَّكَرُ}} ({{tr:al-dhakar}}).\",\"representative_source_ids\":[\"QS-fe7ce3ad\",\"MS-e16d84ee\",\"QF-84c14413\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:2:form-echo-with-prior-act","source_type":"word_analysis","support_id":"sup_1ead9bfa409de0ca2453","text":"{\"blocking_evidence\":null,\"headline\":\"matched form with reversed direction\",\"reader_payoff\":\"The reader notices that the similar ending and first-person perfect shape make the lowering and raising acts sound paired even as their directions reverse.\",\"reason\":\"Both verbs in the comparison are same-surah first-person perfect forms, so the sound-form echo is locally anchored rather than free association.\",\"representative_source_ids\":[\"QE-b54ed42e\",\"ME-438b2536\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:2:completed-divine-active-agency","source_type":"word_analysis","support_id":"sup_2647bae280bc02bbd667","text":"{\"blocking_evidence\":null,\"headline\":\"completed active divine raising\",\"reader_payoff\":\"The reader notices that the elevation is framed as an accomplished divine act with the actor carried in the verb itself.\",\"reason\":\"QAC and attachment identify the verb as perfect active 1cp, and the contextual profile shows this root-form commonly carries implicit subject agreement rather than requiring an external subject noun.\",\"representative_source_ids\":[\"QG-d3ecb248\",\"QG-eba78d7d\",\"MG-f4d331e5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:4:direct-object-of-raising","source_type":"word_analysis","support_id":"sup_286e586aae943695dcbb","text":"{\"blocking_evidence\":null,\"headline\":\"the raised entity is the possessed verbal noun\",\"reader_payoff\":\"The reader notices that what is raised is the addressee's mention or remembrance, not the addressee himself and not the beneficiary phrase.\",\"reason\":\"Attachment evidence marks {{ar:ذِكْرَكَ}} ({{tr:dhikraka}}) as the explicit direct object of {{ar:رَفَعْنَا}} ({{tr:rafaʿnā}}), with the suffix internal to the noun phrase.\",\"representative_source_ids\":[\"QG-65173d11\",\"QG-75cf24a4\",\"QG-99f5988c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:3:beneficiary-before-object","source_type":"word_analysis","support_id":"sup_2a2d466ba93f0c8a976d","text":"{\"blocking_evidence\":null,\"headline\":\"beneficiary foregrounded before object\",\"reader_payoff\":\"The reader notices that the clause first names who receives the favor, then lets the raised object land in final position.\",\"reason\":\"The local word order places {{ar:لَكَ}} ({{tr:laka}}) between the verb and {{ar:ذِكْرَكَ}} ({{tr:dhikraka}}), with the object still syntactically forced after it.\",\"representative_source_ids\":[\"QT-8e827ee8\",\"QT-eb521b4b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:2:sound-and-beatline-upturn","source_type":"word_analysis","support_id":"sup_31b336ab1884f721be2f","text":"{\"blocking_evidence\":null,\"headline\":\"sound stages release before closure\",\"reader_payoff\":\"The reader notices an audible release and balance: the first beatline carries action and beneficiary before the object lands.\",\"reason\":\"The phonetic and beatline observations remain tied to the local surface sequence {{ar:رَفَعْنَا لَكَ}} ({{tr:rafaʿnā laka}}) before the final object.\",\"representative_source_ids\":[\"QP-3b512b51\",\"QP-5d6ab077\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"94:4:1:2","source_type":"qac_morpheme","support_id":"sup_336ad07f6e667fc01cb5","text":"{\"lemma_ar\":\"رَفَعَ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:rafaEa|ROOT:rfE|1P\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"94:4:1:2\",\"qac_word_ref\":\"94:4:1\",\"root_ar\":\"ر ف ع\",\"surface_ar\":\"رَفَعْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:3","source_type":"word_analysis","support_id":"sup_3971f226aeceb6a158c3","text":"{\"gloss_range\":\"prepositional phrase marking the addressed beneficiary or specification of the raising, not the raised object\",\"prose\":\"{{ar:لَكَ}} ({{tr:laka}}) is the small prepositional phrase that makes the raising personally directed. Attachment evidence keeps it governed by {{ar:رَفَعْنَا}} ({{tr:rafaʿnā}}), so the addressee is beneficiary or specified recipient, while {{ar:ذِكْرَكَ}} ({{tr:dhikraka}}) remains the thing raised. Its fused {{ar:كَ}} ({{tr:-ka}}) makes the beneficiary singular and directly addressed, and that same addressee is repeated in the possessive ending of the object. Placed before the object, {{ar:لَكَ}} ({{tr:laka}}) lets the clause answer \\\"for whom\\\" before disclosing \\\"what\\\"; it also reverses the prior \\\"from you\\\" phrase of 94:2, moving from removal from you to benefit for you.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَكَ}} ({{tr:laka}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:4:dhikr-semantic-field","source_type":"word_analysis","support_id":"sup_3fe70f546f49f13ea7c1","text":"{\"blocking_evidence\":null,\"headline\":\"mention, remembrance, renown, reminder, and scripture pressure\",\"reader_payoff\":\"The reader notices that the raised object is richer than social fame: it carries remembrance, verbal mention, honorable renown, reminder, and revelatory-scriptural pressure.\",\"reason\":\"V4 supports mention, remembrance, scripture, honorable renown, worshipful remembrance, and reminder branches for {{ar:ذ ك ر}} ({{tr:dh-k-r}}), while the local direct-object frame narrows the selected value to the addressee-linked mention/remembrance being raised.\",\"representative_source_ids\":[\"QS-b7da27d3\",\"QS-f1efb507\",\"MS-cf9b1e24\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:2:transitive-benefactive-frame","source_type":"word_analysis","support_id":"sup_4c0a1a2171abad5923ed","text":"{\"blocking_evidence\":null,\"headline\":\"raised object kept distinct from beneficiary\",\"reader_payoff\":\"The reader notices that the clause raises the addressee's mention for him, rather than raising the addressee directly or leaving the object vague.\",\"reason\":\"Attachment evidence gives {{ar:ذِكْرَكَ}} ({{tr:dhikraka}}) as the direct object and {{ar:لَكَ}} ({{tr:laka}}) as the governed beneficiary complement.\",\"representative_source_ids\":[\"QG-88ac1dfc\",\"QT-ff3dcf1e\",\"QI-f57759e7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:4:boundary-shift-to-public-remembrance","source_type":"word_analysis","support_id":"sup_541ab44ef5d9b5147d98","text":"{\"blocking_evidence\":null,\"headline\":\"body burden becomes abstract remembrance\",\"reader_payoff\":\"The reader notices the scene shift from the addressee's burdened body to the addressee's public and cosmic remembrance.\",\"reason\":\"The same second-person suffix links the earlier body scene to the final possessed noun, while the noun's abstraction changes the register.\",\"representative_source_ids\":[\"QB-8715016d\",\"QB-f7cf8321\",\"QB-fe2b8c3d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:4:addressee-bound-definiteness","source_type":"word_analysis","support_id":"sup_605d0dd72730a210ca29","text":"{\"blocking_evidence\":null,\"headline\":\"final suffix binds object to the addressee\",\"reader_payoff\":\"The reader notices that the final word is not generic remembrance but a compact, definite object tied to the addressed person.\",\"reason\":\"The possessive suffix is syntactically forced and coreferential with the addressee, making the object definite and personally bound.\",\"representative_source_ids\":[\"QG-5e26a238\",\"QF-beb94e7f\",\"QF-de565258\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:4:derived-reminding-pressure","source_type":"word_analysis","support_id":"sup_62de2dfda44a734d9b2a","text":"{\"blocking_evidence\":null,\"headline\":\"remembering and reminding derivatives color the noun\",\"reader_payoff\":\"The reader notices a live recollection and admonition edge around the noun, while the surface still remains a raised object rather than a command or causative verb.\",\"reason\":\"Derivative evidence supports recollecting, taking heed, and causing remembrance in the wider family, but the local form is the possessed gerund {{ar:ذِكْرَكَ}} ({{tr:dhikraka}}), not those finite or derived forms.\",\"representative_source_ids\":[\"QS-a103fbbb\",\"QS-ca36d3c1\",\"QS-f4b9d4a3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:2:down-up-reversal-from-burden","source_type":"word_analysis","support_id":"sup_86a72346fca60263eb47","text":"{\"blocking_evidence\":null,\"headline\":\"burden lowered, mention raised\",\"reader_payoff\":\"The reader notices the embodied reversal: after the back is strained under burden in 94:3, the next divine act lifts the addressee's mention.\",\"reason\":\"The CRITICAL rows give concrete same-surah contrasts with 94:2-3, and the local root branch of raising supports the vertical reversal.\",\"representative_source_ids\":[\"QS-6b998f3f\",\"MT-c7631a25\",\"QE-66ca6e07\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:4:gerund-not-alternate-form","source_type":"word_analysis","support_id":"sup_8dfa276bddaf69c9c6f1","text":"{\"blocking_evidence\":null,\"headline\":\"possessed gerund chosen over finite or status forms\",\"reader_payoff\":\"The reader notices that the ayah raises a compact state/object of remembrance, not a command to remember, a passive status label, or a generalized reminder-form.\",\"reason\":\"QAC identifies the local word as a possessed gerund, and contextual profiles show the same root-form is frequent enough for the specific nominal choice to be meaningful.\",\"representative_source_ids\":[\"QF-3d5fefc2\",\"QF-5fb5fe26\",\"QF-674b5956\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"94:4:3:1","source_type":"qac_morpheme","support_id":"sup_992b00542ea3c3583cf5","text":"{\"lemma_ar\":\"ذِكْر\",\"morph_features\":\"STEM|POS:N|VN|LEM:*ikor|ROOT:*kr|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"94:4:3:1\",\"qac_word_ref\":\"94:4:3\",\"root_ar\":\"ذ ك ر\",\"surface_ar\":\"ذِكْرَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:2:form-i-decisive-transitive","source_type":"word_analysis","support_id":"sup_9f3fa0287d2d1cca13b9","text":"{\"blocking_evidence\":null,\"headline\":\"simple transitive form avoids passive or self-rise\",\"reader_payoff\":\"The reader notices a decisive bestowed raising, not a passive reputation event, a self-ascent, or a stepwise intensive process.\",\"reason\":\"The local surface is active Form I with an explicit object and beneficiary complement, so passive and intransitive alternatives remain contrastive rather than local parses.\",\"representative_source_ids\":[\"QF-bacae6fb\",\"QF-f153095a\",\"MF-6d693e03\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:2:elevation-exaltation-publicity-range","source_type":"word_analysis","support_id":"sup_a453aeae46c5b3782793","text":"{\"blocking_evidence\":null,\"headline\":\"elevation becomes honor and public audibility\",\"reader_payoff\":\"The reader notices that the raised object is not merely moved upward; because it is mention, the raising shades into exalted standing, public carrying, and record-like honor.\",\"reason\":\"V4 supports rank, presentation, public-report, voice-height, and grammatical branches for {{ar:ر ف ع}} ({{tr:r-f-ʿ}}), while local grammar narrows the selected sense to transitive exaltation of {{ar:ذِكْرَكَ}} ({{tr:dhikraka}}).\",\"representative_source_ids\":[\"QS-0641c6c7\",\"QS-2e71ebf5\",\"QS-559c22a2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:4","source_type":"word_analysis","support_id":"sup_aa6ac3a917960182a5b9","text":"{\"gloss_range\":\"the addressee-bound mention, remembrance, renown, or memorial/revelatory remembrance raised as the direct object, with the possessive verbal noun leaving active and passive directions open\",\"prose\":\"{{ar:ذِكْرَكَ}} ({{tr:dhikraka}}) is the clause's final object and payoff. Attachment evidence keeps the whole possessed verbal noun as the accusative object of {{ar:رَفَعْنَا}} ({{tr:rafaʿnā}}), so possession does not make it dependent on {{ar:لَكَ}} ({{tr:laka}}). The final {{ar:كَ}} ({{tr:-ka}}) makes the object definite and addressee-bound, but because {{ar:ذِكْر}} ({{tr:dhikr}}) is a verbal noun, the possessive can still lean both ways: your remembering and your being mentioned. Locally, the governing verb selects raised mention, renown, and remembrance; record, reminder, devotional, and scripture senses remain meaningful pressure, especially because the Reminder names revelation in 15:9 and 38:1, but they do not replace the direct-object grammar. Reflective recollection, sudden retrieval into awareness, and causative reminding/admonition stay as root-family pressure around the noun rather than becoming the main predication. The chosen gerund is not a finite command to remember, not a passive-participle status label, not a generalized reminder-form, and not the concrete male noun from the same root; that male-marked branch remains root-level tension while the local object stays abstract. It compresses many possible acts of remembrance into one possessed object. Its final position and sound echo the earlier burden word in 94:2-3: the scene leaves the addressee's burdened body and lands in public remembrance, where the addressee's mention becomes what is raised. The final dh-k-r-k sound path moves from soft onset through tightening and release, giving the closure audible prominence.\",\"root_display\":\"{{ar:ذ ك ر}} ({{tr:dh-k-r}})\",\"root_gloss_range\":\"root range includes bringing to mind, mention on the tongue, worshipful remembrance, scripture, honorable renown, reminder or admonition, record/document uses, and separate male or forceful branches; the local possessed gerund selects mention/remembrance/renown while other branches remain only narrowed pressure\",\"surface_display\":\"{{ar:ذِكْرَكَ}} ({{tr:dhikraka}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:3:beneficiary-not-object","source_type":"word_analysis","support_id":"sup_ac239962decb1eb8620e","text":"{\"blocking_evidence\":null,\"headline\":\"beneficiary distinct from object\",\"reader_payoff\":\"The reader notices that the addressee is the beneficiary of the raising, while the addressee's mention is the raised object.\",\"reason\":\"Attachment evidence identifies {{ar:لَكَ}} ({{tr:laka}}) as the prepositional complement of {{ar:رَفَعْنَا}} ({{tr:rafaʿnā}}), not as the direct object.\",\"representative_source_ids\":[\"QG-6549d18a\",\"QG-8feede4a\",\"MG-089ad190\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:3:from-you-for-you-reversal","source_type":"word_analysis","support_id":"sup_b7e1b1f1ddccfeea224d","text":"{\"blocking_evidence\":null,\"headline\":\"from-you becomes for-you\",\"reader_payoff\":\"The reader notices the same addressee carried from removal in 94:2 into benefit in 94:4, with the preposition reversing direction.\",\"reason\":\"The CRITICAL rows give the concrete contrast between {{ar:عَنكَ}} ({{tr:ʿanka}}) in 94:2 and {{ar:لَكَ}} ({{tr:laka}}) in 94:4, and the suffix evidence keeps the addressee continuous.\",\"representative_source_ids\":[\"MT-b319e48c\",\"QE-64ab82a5\",\"QB-79be0170\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:1:full-clause-favor-coordination","source_type":"word_analysis","support_id":"sup_c11fbef0ab484615f108","text":"{\"blocking_evidence\":null,\"headline\":\"whole clause joined to the favor-chain\",\"reader_payoff\":\"The reader notices that 94:4 is heard as another divine favor in the same accumulating sequence, not as an isolated new sentence.\",\"reason\":\"QAC identifies {{ar:وَ}} ({{tr:wa}}) as coordination, and attachment evidence treats words 1-4 as one verbal clause headed by {{ar:رَفَعْنَا}} ({{tr:rafaʿnā}}).\",\"representative_source_ids\":[\"QG-a9c96481\",\"MG-0efde394\",\"QT-e3169d1c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:4:scripture-and-record-pressure","source_type":"word_analysis","support_id":"sup_c5aa6f62462895259cb3","text":"{\"blocking_evidence\":null,\"headline\":\"revelatory and record register remains available\",\"reader_payoff\":\"The reader notices that the word can point beyond reputation toward an elevated memorial or revelatory register, with Quranic self-designation in view (15:9; 38:1).\",\"reason\":\"The source rows cite {{ar:ٱلذِّكْر}} ({{tr:al-dhikr}}) as revelation in 15:9 and 38:1; local grammar permits this as pressure but does not force a replacement of mention or remembrance.\",\"representative_source_ids\":[\"QS-66807c94\",\"QI-e6323af4\",\"MI-e5acc244\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:3:addressee-convergence","source_type":"word_analysis","support_id":"sup_c7b2744b4e64ed621ffb","text":"{\"blocking_evidence\":null,\"headline\":\"same addressee as beneficiary and possessor\",\"reader_payoff\":\"The reader notices that one addressee is targeted twice: first as beneficiary, then as possessor of the mention.\",\"reason\":\"The cross-reference evidence marks the suffix in {{ar:لَكَ}} ({{tr:laka}}) and the suffix in {{ar:ذِكْرَكَ}} ({{tr:dhikraka}}) as the same direct addressee.\",\"representative_source_ids\":[\"QG-a36e3d60\",\"QS-f1231aed\",\"QY-7972428d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:4:possessive-masdar-ambiguity","source_type":"word_analysis","support_id":"sup_cc187fe4c23ef91ad271","text":"{\"blocking_evidence\":null,\"headline\":\"definite object with active-passive possessive range\",\"reader_payoff\":\"The reader notices that the same possessive form can hold both the addressee's remembering and the addressee's being mentioned.\",\"reason\":\"QAC and attachment identify the word as a possessed maṣdar, and the noun-instance note explicitly preserves subjective and objective possessive possibilities.\",\"representative_source_ids\":[\"QG-2a88ff13\",\"QG-61e77a65\",\"QS-14e5427d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:4:phonetic-texture-of-closure","source_type":"word_analysis","support_id":"sup_d5846d1cfb29023aa888","text":"{\"blocking_evidence\":null,\"headline\":\"sound arc makes the ending distinct\",\"reader_payoff\":\"The reader notices that the final word's sound moves from soft onset through tightening and release, giving the closure audible prominence.\",\"reason\":\"The sound claim is tied to the actual final surface {{ar:ذِكْرَكَ}} ({{tr:dhikraka}}) and its closure position.\",\"representative_source_ids\":[\"QP-4d631736\",\"QP-8a20fdd8\",\"MP-c0c70c1c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:2","source_type":"word_analysis","support_id":"sup_d806bbb727f16fdb76ca","text":"{\"gloss_range\":\"completed active divine raising or exaltation of an explicit object, with the addressee marked separately as beneficiary\",\"prose\":\"{{ar:رَفَعْنَا}} ({{tr:rafaʿnā}}) gives the ayah its completed divine action. The perfect active Form I makes the raising accomplished and agentive: the embedded {{ar:نَا}} ({{tr:-nā}}) keeps the divine actor inside the verb, while {{ar:ذِكْرَكَ}} ({{tr:dhikraka}}) remains the object and {{ar:لَكَ}} ({{tr:laka}}) names the beneficiary. That Form I transitive shape gives a decisive bestowed raising, not a passive reputation event, self-ascent, or stepwise intensive elevation. The root's upward and rank senses converge here as exaltation of the addressee's mention; presentation, voice-raising, record-register, and grammatical-raising branches add publicity and elevation pressure only insofar as the raised object is mention. The verb also answers the earlier lowering/removal of burden in 94:2: that act moves the weight down, while {{ar:رَفَعْنَا}} ({{tr:rafaʿnā}}) in 94:4 lifts the mention up, a polarity also made legible by the lowering/raising pair in 56:3. Its sound and cadence stage that upturn: the longer first beatline carries action and beneficiary before the compact object {{ar:ذِكْرَكَ}} ({{tr:dhikraka}}) lands at closure.\",\"root_display\":\"{{ar:ر ف ع}} ({{tr:r-f-ʿ}})\",\"root_gloss_range\":\"root range includes physical raising, high rank, presentation or making public, raised voice, travel ascent, grammatical raising, and other branch-specific uses; the local clause selects active transitive elevation and exaltation of the addressee-linked mention\",\"surface_display\":\"{{ar:رَفَعْنَا}} ({{tr:rafaʿnā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:1:bound-launch-before-verb","source_type":"word_analysis","support_id":"sup_d8d4ee2b3ef1cf4d2d07","text":"{\"blocking_evidence\":null,\"headline\":\"connection is front-loaded\",\"reader_payoff\":\"The reader notices that the ayah begins by installing relation before it gives the new verbal content.\",\"reason\":\"The particle is a bound proclitic at the very beginning of the ayah, so the form itself supports a compressed connective launch.\",\"representative_source_ids\":[\"QF-de803fb6\",\"QT-24ced126\",\"QY-9bdf99b3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:3:compressed-bound-address","source_type":"word_analysis","support_id":"sup_efdd76f3becc1c267715","text":"{\"blocking_evidence\":null,\"headline\":\"bound suffix compresses personal address\",\"reader_payoff\":\"The reader notices how a very small bound form carries governance, benefaction, and precise second-person address together.\",\"reason\":\"QAC identifies the word as a preposition plus 2ms suffix, and attachment evidence keeps that suffix inside the governed beneficiary phrase.\",\"representative_source_ids\":[\"QF-8a4c46a9\",\"QF-eb016290\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:4:4:object-delay-and-closure","source_type":"word_analysis","support_id":"sup_fe1d3cfeaf1bcafef849","text":"{\"blocking_evidence\":null,\"headline\":\"final object carries closure weight\",\"reader_payoff\":\"The reader notices that the ayah resolves only at the final word, where the raised entity is disclosed and isolated.\",\"reason\":\"The object follows the benefactive phrase and closes the ayah, while attachment evidence keeps it as the direct object of the raising.\",\"representative_source_ids\":[\"QT-1018e449\",\"QT-3c50d59d\",\"QY-1b28a7be\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَرَفَعْنَا لَكَ ذِكْرَكَ","ayah_ref":"94:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000516/B007","root_000582/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000582","role":"Elevation of rank supplies the vertical value-axis on which the addressee's standing is raised.","root":"ر ف ع","source_ref":"94:4","source_word_indices":["1"]},{"branch_id":"B007","mapped_root_id":"root_000516","role":"Honorable reputation supplies the social object that can occupy the higher rank.","root":"ذ ك ر","source_ref":"94:4","source_word_indices":["3"]}],"changed_reading":{"after":"We elevated the standing inhering in your very mention, making each mention bear heightened honor for you.","before":"We caused people to mention you favorably."},"confidence":"strong","focus_anchor":"The raising action directly governs the possessed mention, while لَكَ marks the addressee as beneficiary.","mechanism":"A status-elevation branch of ر ف ع and a renown branch of ذ ك ر converge on a social-valuational lift: the thing raised is not the body but the standing carried whenever the addressee is mentioned.","model_id":"baseline_exalted_renown"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_exalted_renown","source_type":"hft","support_id":"sup_621173ed951ad333045e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَرَفَعْنَا لَكَ ذِكْرَكَ","ayah_ref":"94:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000516/B004","root_000582/B005","root_000582/B010"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000582","role":"Publicizing and relaying a report turns upward movement into outward circulation.","root":"ر ف ع","source_ref":"94:4","source_word_indices":["1"]},{"branch_id":"B010","mapped_root_id":"root_000582","role":"Vocal height gives the circulation an audible register rather than a purely reputational one.","root":"ر ف ع","source_ref":"94:4","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000516","role":"Mention running on tongues supplies the transmissible content whose reach and audibility increase.","root":"ذ ك ر","source_ref":"94:4","source_word_indices":["3"]}],"changed_reading":{"after":"We caused your mention to travel outward and remain publicly audible, multiplying the occasions on which it is voiced.","before":"We increased your reputation."},"confidence":"strong","focus_anchor":"The direct object ذِكْرَكَ can denote voiced mention, and the governing رفع has branches of public transmission and vocal height.","mechanism":"Elevation becomes propagation rather than only prestige: mention is made public, carried onward, and given greater audibility across speakers.","model_id":"baseline_public_circulation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_public_circulation","source_type":"hft","support_id":"sup_b1ac507966f3e5c68cdd","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَرَفَعْنَا لَكَ ذِكْرَكَ","ayah_ref":"94:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000516/B003","root_000516/B009","root_000582/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000582","role":"Literal upward displacement supplies a cognitive topology from latent depth to accessible prominence.","root":"ر ف ع","source_ref":"94:4","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000516","role":"Recall after or against forgetting identifies the raised object as renewed mental presence.","root":"ذ ك ر","source_ref":"94:4","source_word_indices":["3"]},{"branch_id":"B009","mapped_root_id":"root_000516","role":"The reminder branch makes that mental presence reproducible through cues, not merely a one-time recollection.","root":"ذ ك ر","source_ref":"94:4","source_word_indices":["3"]}],"changed_reading":{"after":"We lifted remembrance of you into durable cognitive reach, so it can be recalled and reactivated rather than sink into forgetting.","before":"We granted you high renown."},"confidence":"medium","focus_anchor":"ذِكْرَكَ remains the object of raising, but its recall and reminder branches permit a cognitive rather than social verticality.","mechanism":"What lies low or latent is lifted into availability: remembrance is brought above the threshold of forgetting and made easy to recover in mind.","model_id":"baseline_retrievable_remembrance"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_retrievable_remembrance","source_type":"hft","support_id":"sup_96e23b245baec5fb564b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَرَفَعْنَا لَكَ ذِكْرَكَ","ayah_ref":"94:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000516/B008","root_000582/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000582","role":"Bringing a person or case before authority supplies the act of formal presentation.","root":"ر ف ع","source_ref":"94:4","source_word_indices":["1"]},{"branch_id":"B008","mapped_root_id":"root_000516","role":"A documentary instrument of right supplies the presented object and its claim-bearing force.","root":"ذ ك ر","source_ref":"94:4","source_word_indices":["3"]}],"changed_reading":{"after":"We advanced for you a claim-bearing memorial into recognized standing, as though your mention were formally presented and attested.","before":"We made your reputation higher."},"confidence":"exploratory","containment":"This is surprising because it combines two peripheral focus-root branches and the verse names no court or document. It remains anchored in the governing رفع, the direct object ذِكْرَكَ, and beneficiary لَكَ, which can sustain an analogy of presenting a claim for recognition. Downstream prose should label it a juridical image, not a lexical translation.","focus_anchor":"The construction raises a possessed ذكر for the addressee, permitting the raised object to be modeled as a claim or instrument presented on the beneficiary's behalf.","outlier_id":"outlier_juridical_attestation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier_juridical_attestation","source_type":"hft","support_id":"sup_058f9716ab94eb420ec9","trust":"legacy_unbound"}]}
</lane_packet_json>
