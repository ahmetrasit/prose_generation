# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **90:14**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s090-regular-20260912/s090/90_14/micro.discovery.json` and modify nothing
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
  "ayah_ref": "90:14",
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
{"analysis_context":{"analysis_id":"s090-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"90:14","host_surah":90,"lane_context_refs":[],"ordered_context_refs":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:11","90:12","90:13","90:15","90:16","90:17","90:18","90:19","90:20","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, yalın açlığı da kapsar; yorgunluğu her kullanım için zorunlu saymaz ve kıtlık anlamını türemiş adın uzmanlaşmış kullanımında tutar.","branch_kind":"bare","branch_ref":"root_000710/B001","candidate_links":[{"candidate_id":"cand_5c192969d199fe40effc","lane":"micro"},{"candidate_id":"cand_edda19c25e4e912dccb4","lane":"micro"},{"candidate_id":"cand_05c3e0aa40dccce35b30","lane":"micro"},{"candidate_id":"cand_3a5ec2be6facaa151d47","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَسْغَبَة","morph_features":"STEM|POS:N|LEM:masogabap|ROOT:sgb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:6:1","qac_word_ref":"90:14:6","surface_ar":"مَسْغَبَةٍ"}],"gloss":"açlık; özellikle yorgunlukla ağırlaşan açlık ve kıtlık","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, yiyecek gereksinimi duyan kişinin aç olması veya acıkmasıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı kaynaklar açlığı, kişiyi yoran veya bitkin bırakan açlıkla sınırlar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Türemiş bir ad, şiddetli ve yaygın açlık durumunu, yani kıtlığı belirtir."}}],"root_ar":"س غ ب","root_id":"root_000710","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın genel açlık çekirdeğini, bazı kaynaklardaki yorgunluk kısıtını ve türemiş addaki kıtlık uzmanlaşmasını birlikte özetler.","boundary_detail":"Dal, yalın açlığı da kapsar; yorgunluğu her kullanım için zorunlu saymaz ve kıtlık anlamını türemiş adın uzmanlaşmış kullanımında tutar.","branch_image_ar":"الجوع مع التعب والمجاعة","concept_gloss":"açlık; özellikle yorgunlukla ağırlaşan açlık ve kıtlık","contextual_glosses":[{"applicability":"Bir kişinin aç duruma girmesini bildiren yalın eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yorgunlukla ağırlaşan açlık değişkesini ve kıtlık bildiren türemiş ad kullanımını kapsamaz.","preserves":"Aç duruma girme ve yiyecek gereksinimi duyma çekirdeğini korur."},"facet_ids":["F001"],"text":"acıkmak","usage_role":"general"},{"applicability":"Açlığın yorgunluk veya bitkinlikle birlikte özellikle vurgulandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yorgunluk koşulu taşımayan genel açlığı ve kıtlık bildiren türemiş ad kullanımını kapsamaz.","preserves":"Açlık ile ondan doğan yorgunluğun birlikte bulunmasını korur."},"facet_ids":["F002"],"text":"açlıktan bitkin düşmek","usage_role":"contextual"},{"applicability":"Türemiş adın şiddetli ve yaygın açlık durumunu bildirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir kişinin aç olması veya acıkması biçimindeki genel çekirdeği kapsamaz.","preserves":"Şiddetli ve yaygın açlık uzmanlaşmasını korur."},"facet_ids":["F003"],"text":"kıtlık","usage_role":"contextual"}],"definition":"Bir kimsenin aç olması ya da acıkmasıdır; bazı kaynaklarda bu açlığın yorgunlukla birlikte bulunması özellikle belirtilir. Aynı kökten türeyen bir ad, şiddetli ve yaygın açlık olan kıtlığı da anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, yiyecek gereksinimi duyan kişinin aç olması veya acıkmasıdır."},{"facet_id":"F002","role":"source_variant","statement":"Bazı kaynaklar açlığı, kişiyi yoran veya bitkin bırakan açlıkla sınırlar."},{"facet_id":"F003","role":"specialization","statement":"Türemiş bir ad, şiddetli ve yaygın açlık durumunu, yani kıtlığı belirtir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yiyecek yerine su gereksinimini anlamın merkezine getirir.","collision":"Açlıkla aynı bedensel sıkıntı alanında bulunsa da ayrı bir gereksinimi adlandırır.","fit":"displacement","loses":"Yiyecek gereksinimine dayalı açlık çekirdeğini ve kıtlık uzmanlaşmasını bütünüyle yitirir.","preserves":"Bedensel gereksinim ve buna eşlik edebilen yorgunluk düşüncesini kısmen korur."},"text":"susuzluk"}],"identity_rationale":"Kaynak ifadesinin ortak çekirdeği açlık ve acıkmadır. Yorgunluk bütün kaynaklarda zorunlu bir koşul değildir; bazı kaynaklar anlamı yorgunlukla birlikte yaşanan açlıkla sınırlar. Kıtlık ise aynı anlam alanındaki türemiş adın belirginleşmiş kullanımını oluşturur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"acıkmak; bazı kullanımlarda açlıktan yorulmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kıtlık, şiddetli açlık"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"aç, acıkmış kimse"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"çok aç, açlıktan bitkin"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"açlık; bazı kaynaklarda yorgunlukla birlikte açlık"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"açlık"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"açlık"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"aç kadın"}],"lexicalization_note":"Tanım, çıplak kökün açlık ve acıkma çekirdeğini esas alır; yorgunluk kısıtını kaynak değişkesi, kıtlığı ise türemiş bir uzmanlaşma olarak ayırır.","neighbor_coverage_note":"Sekiz adayın tümü karşılaştırıldı. En güçlü beş sınır yayımlandı; yoksulluk dalı daha geniş bir geçim sıkıntısı alanına, şiddet ve açlık dalı çok sonuçlu bir sıkıntı kümesine, hayvanları yemeden sürme dalı ise yalnızca aç bırakma sonucuyla bağlantılı ayrı bir eyleme dayandığı için eklenmedi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek düzeyinde iki dal da aç olma ve yiyecek gereksinimi duyma durumunu adlandırır; odak daldaki yorgunluk kaydı kaynak değişkesi, kıtlık ise türemiş kullanım düzeyinde kalır.","focus_only":null,"gloss":"yalın açlık","neighbor_only":null,"neighbor_ref":"root_000278/B001","relation_type":"synonym","shared_zone":"Her iki dal da kişinin yiyecek gereksinimi duyması ve aç olması çekirdeğinde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın kimi kaynaklarındaki ek koşul yorgunluktur ve bu koşul bütün kullanımlara yayılmaz. Karşı dal ise açlığı soğukla birlikte tanımlar; bu nedenle yalnız iki sıkıntının aynı anda bulunduğu bağlamlarda yaklaşırlar.","focus_only":"Odak dalda soğuk zorunlu değildir; genel açlık, yorgunlukla ağırlaşan açlık ve kıtlık uzmanlaşması bulunur.","gloss":"soğukla birlikte açlık","neighbor_only":"Karşı dalda açlığa soğuk ve üşüme koşulu eşlik eder.","neighbor_ref":"root_000403/B005","relation_type":"near_synonym","shared_zone":"İki dal da açlığın başka bir bedensel sıkıntıyla birleştiği durumları kapsayabilir."},{"boundary_match":"partial","distinction":"Karşı dalın kapsamı topluluk katılımcısıyla sınırlıdır. Odak dalda topluluk koşulu yoktur; kişi düzeyindeki açlık temel anlamdır ve kaynaklara göre yorgunluk kısıtı veya kıtlık uzmanlaşması eklenebilir.","focus_only":"Odak dal bireysel açlığı, kimi kaynaklardaki yorgunluk kısıtını ve kıtlık uzmanlaşmasını da kapsar.","gloss":"bir topluluğun aç kalması","neighbor_only":"Karşı dal, açlığın bir topluluğun başına gelmesini bildiren kullanıma bağlıdır.","neighbor_ref":"root_001670/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da insanların aç duruma gelmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal öncelikle açlık durumunu, uzmanlaşmış kullanımında ise kıtlığı anlatır. Karşı dal durumun kendisini değil, genel açlığın yaşandığı zamanı merkezine aldığı için olağan bağlamlarda birbirinin yerine geçmez.","focus_only":"Odak dal kişinin aç olması veya acıkması durumunu ve kimi kaynaklarda yorgunluğu kapsar.","gloss":"genel açlık dönemi","neighbor_only":"Karşı dal açlığın genelleştiği yılı veya dönemi adlandırır.","neighbor_ref":"root_000278/B002","relation_type":"near_neighbor","shared_zone":"Türemiş addaki kıtlık anlamı, toplum çapındaki açlık dönemiyle aynı olay alanına girer."},{"boundary_match":"partial","distinction":"Odak dal yiyecek gereksinimi ve aç olma durumunu adlandırır; yorgunluk yalnız bazı kaynaklarda kısıtlayıcıdır. Karşı dal ise azalma ve zayıflama sonucunu öne çıkarır, bu yüzden açlığın henüz bedensel eksilmeye yol açmadığı yerde örtüşme sona erer.","focus_only":"Odak dalda açlık temel anlamdır; bedensel zayıflama zorunlu bir sonuç değildir.","gloss":"açlığa bağlı zayıflama","neighbor_only":"Karşı dal bedenin veya yiyeceğin azalmasını ve açlığa bağlı zayıflamayı merkezine alır.","neighbor_ref":"root_000410/B005","relation_type":"near_neighbor","shared_zone":"Açlık kişiyi güçten düşürdüğünde iki dal aynı durumun neden ve sonucuna temas eder."}],"source_phrase_ar":"أصل واحد يدل على الجوع والمسغبة المجاعة وسغب يسغب سغوبا وهو ساغب وسغبان (maqayis)؛ الساغب الجائع وسغب يسغب سغوبا ومسغبة (ayn)؛ سغب الرجل إذا جاع ولا يكون السغب إلا الجوع مع التعب والمصدر السغابة والسغوب والسغب (jamhara)؛ سغب أي جاع فهو ساغب وسغبان وامرأة سغبى ويتيم ذو مسغبة أي ذو مجاعة (sihah)؛ السغب وهو الجوع مع التعب ويقال سغب سغبا وسغوبا وهو ساغب وسغبان (mufradat)","source_summary":"Kaynaklar açlık ve acıkma çekirdeğinde birleşir; aç kişiyi bildiren biçimleri ve açlık bildiren adları da bu çekirdeğe bağlar. Bununla birlikte bazı tanımlar açlığı genel bırakırken bazıları yorgunluğu ayırt edici bir koşul sayar; türemiş ad ise kıtlık ve şiddetli açlık anlamını taşır. Jamhara kaynağa özgü ek mastar biçimini, Sihah ise kaynağa özgü dişil sıfat biçimini ayrıca kaydeder.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه السغب بمعنى الجوع والجوع مع التعب والمسغبة بمعنى المجاعة وحال الساغب والسغبان","what_is_not_ar":"العطش مع التعب مذكور على جهة القيل أو غير المستعمل"},"support_links":["sup_2ffe64fb429baf2af6ba","sup_9d0b5164baa90d1667b0","sup_b110c9558e06989965d5","sup_c0b563797e6464b0e9a6"]},{"boundary":"Anlam, konuşmaya başlatma, mecazi geçim, meyvenin olgunlaşması ve başka özel dallara taşınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000934/B001","candidate_links":[{"candidate_id":"cand_05c3e0aa40dccce35b30","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","surface_ar":"إِطْعَٰمٌ"}],"gloss":"tatma, yeme ve yenilen besin","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin tadını duyuyla algılama ve ondan tat alma."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyi yeme veya besin olarak tüketme."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yenilen, açlığı gideren ve kimi bağlamlarda içeceği de kapsayan besin."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bazı kullanımlarda besin adının özellikle buğdaya ayrılması."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duyusal tatma, tüketme ve açlığı gideren besin çekirdeğini birlikte anlatan genel açıklamadır.","boundary_detail":"Anlam, konuşmaya başlatma, mecazi geçim, meyvenin olgunlaşması ve başka özel dallara taşınmaz.","branch_image_ar":"ذوق الشيء وتناوله","concept_gloss":"tatma, yeme ve yenilen besin","contextual_glosses":[{"applicability":"Bir yiyecek ya da içeceğin tadının duyuyla algılandığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yeme ve besin adı olma anlamlarını kapsamaz.","preserves":"Duyusal tat alma eylemini doğal biçimde korur."},"facet_ids":["F001"],"text":"tadına bakmak","usage_role":"contextual"},{"applicability":"Yenilen ve açlığı gideren şeyin adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tat alma eylemini ve içeceğin sınırlı kapsamını dışarıda bırakır.","preserves":"Yenilen besin ve açlığı giderme yönünü korur."},"facet_ids":["F003"],"text":"yiyecek","usage_role":"contextual"}],"definition":"Bir şeyin tadını duyuyla algılamak veya onu yemek; ayrıca yenilen ve açlığı gideren besin. İçecek, tadına bakılması ya da besleyici olması bakımından bu kapsama girebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin tadını duyuyla algılama ve ondan tat alma."},{"facet_id":"F002","role":"core","statement":"Bir şeyi yeme veya besin olarak tüketme."},{"facet_id":"F003","role":"extension","statement":"Yenilen, açlığı gideren ve kimi bağlamlarda içeceği de kapsayan besin."},{"facet_id":"F004","role":"specialization","statement":"Bazı kullanımlarda besin adının özellikle buğdaya ayrılması."}],"identity_rationale":"Kaynak ifadesi duyusal tatmayı, bir şeyi yemeyi ve yenilen besini aynı çekirdekte toplar; içecek de tadına bakılan veya besleyen bir şey olduğunda bu alana girer. Bu çerçeve, buğdaya özgü kullanımı ve doyurucu yiyecek ya da su kalıbını çekirdeğin özel gerçekleşmeleri olarak tutmayı gerektirir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tat, lezzet"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yemek veya tadına bakmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yiyecek, besin"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"özellikle buğday"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"tadına bakma ve iştahını yoklama"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"doyuran ve besleyen yiyecek ya da su"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yeme isteği veya iştah çekici şey"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"çok yiyen, obur"}],"lexicalization_note":"Tanım yalın tatma, yeme ve besin anlamlarını kapsar; buğdaya özgü adlandırma ile doyurup besleyen yiyecek ya da su kullanımı ayrıca sınırlandırılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yararlı ayrım, tatma ve tüketme çekirdeğinin başkasını besleme eylemiyle karıştırılmasını önleyen iç komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Buradaki çekirdek tüketenin deneyimi ve tüketilen besindir; komşuda ise veren ya da isteyen ikinci bir katılımcı vardır, bu yüzden olağan bağlamda birbirlerinin yerine geçmezler.","focus_only":"Bu dal kişinin tatması, yemesi veya besinin kendisiyle ilgilidir.","gloss":"tüketme ile yedirme ayrımı","neighbor_only":"Komşu dal besini bir başkasına verme ya da ondan besin isteme eylemini içerir.","neighbor_ref":"root_000934/B002","relation_type":"near_neighbor","shared_zone":"İki dal da yiyecek ve beslenme çevresinde buluşur."}],"source_phrase_ar":"أصل في تذوق الشيء والطعام هو المأكول والإطعام يقع حتى الماء (maqayis)؛ الطعم ذوقه والطعام اسم جامع لكل ما يؤكل (ayn)؛ طعم إذا أكل أو ذاق ومن لم يطعمه أي لم يذقه (sihah)؛ الطعم تناول الغذاء ويستعمل في الشراب (mufradat)","source_summary":"Kaynakların ortak çizgisi tat duyusu, yeme eylemi ve yenilen besindir; içecek ise tadılan veya besleyen şey olarak bu çizgiye bağlanır. Bazı kullanımlarda genel besin adı özellikle buğdayı gösterebilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الطعم بمعنى الذوق والأكل والطعام وما يسد الجوع، ويدخل استعماله في الشراب إذا جعل ذوقا أو غذاء","what_is_not_ar":"ليس منه الاستفتاح في القراءة ولا الرزق المجازي ولا نضج الثمر إلا بفرع مخصوص"},"support_links":["sup_c0b563797e6464b0e9a6"]},{"boundary":"Konuşma ya da okuma sırasında söz isteme anlamı ve yalnızca iyi geçim içinde olma durumu bu dala girmez.","branch_kind":"bare","branch_ref":"root_000934/B002","candidate_links":[{"candidate_id":"cand_5c192969d199fe40effc","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","surface_ar":"إِطْعَٰمٌ"}],"gloss":"başkasını beslemek veya beslenmeyi istemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir başkasına yiyecek ya da besleyici bir şey vererek onu doyurma."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir başkasından yiyecek vermesini ve kendisini doyurmasını isteme."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Besini verme ve karşı taraftan besin talep etme yönlerini birlikte gösteren tam kapsamlı açıklamadır.","boundary_detail":"Konuşma ya da okuma sırasında söz isteme anlamı ve yalnızca iyi geçim içinde olma durumu bu dala girmez.","branch_image_ar":"إطعام الغير وطلب الطعام","concept_gloss":"başkasını beslemek veya beslenmeyi istemek","contextual_glosses":[{"applicability":"Birine yiyecek ya da besleyici içecek verildiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karşı taraftan besin isteme yönünü göstermez.","preserves":"Başkasına besin verme yönünü doğal biçimde korur."},"facet_ids":["F001"],"text":"doyurmak","usage_role":"contextual"}],"definition":"Bir başkasına yiyecek veya yenilip içilebilen besleyici bir şey vermek; ayrıca bir başkasından kendisini beslemesini istemek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir başkasına yiyecek ya da besleyici bir şey vererek onu doyurma."},{"facet_id":"F002","role":"extension","statement":"Bir başkasından yiyecek vermesini ve kendisini doyurmasını isteme."}],"identity_rationale":"Kaynak ifadesi bir başkasına yenilecek şey verme ile bir başkasından kendisini doyurmasını isteme yönlerini açıkça birlikte taşır. Dalın kimliği, kişinin kendisinin yemesinden değil besini veren ile alan arasındaki aktarım ilişkisinden doğar.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yiyecek vermek, doyurmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kendisini doyurmasını istemek"}],"lexicalization_note":"Tanım, başkasını besleme ve beslenmeyi isteme eylemlerini yalın dal kapsamı içinde verir; özel konuşma kalıplarını içeri almaz.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; genel isteme alanıyla kurulan ayrım, besin aktarımına özgü katılımcı yapısını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Buradaki isteme besinle sınırlıdır ve besin verme karşılığını da kapsar; komşu ise nesnesi sınırlanmamış genel bir arama ve isteme alanıdır.","focus_only":"Bu dalda istenen şey özellikle beslenmedir ve ayrıca başkasını doyurma eylemi de bulunur.","gloss":"besin isteme ile genel isteme","neighbor_only":"Komşu dal herhangi bir şeyi arama, isteme veya onun peşine düşme anlamını taşır.","neighbor_ref":"root_000138/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da bir gereksinimin karşı taraftan istenmesi bulunabilir."}],"source_phrase_ar":"الإطعام يقع في كل ما يطعم (maqayis)؛ استطعمه سأله أن يطعمه وأطعمته الطعام (sihah)؛ استطعمه فأطعمه وأطعموا القانع ويطعمون الطعام (mufradat)","source_summary":"Kaynaklar, yenilip içilebilen bir şeyi başkasına vermeyi ve bunun istenmesini aynı aktarım alanında birleştirir. İhtiyaç sahibini doyurma bu temel ilişkinin belirgin uygulamasıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه أطعمته الطعام واستطعمه أي سأله أن يطعمه وإطعام المحتاج","what_is_not_ar":"ليس منه تلقين الإمام عند الارتياج ولا مجرد حسن الحال في المطعم"},"support_links":["sup_b110c9558e06989965d5"]},{"boundary":"Bu dal yalnızca belirtilen konuşma ve okuma kalıplarına bağlıdır; gerçek yiyecek istemeye veya duyusal tatmaya genellenmez.","branch_kind":"collocation","branch_ref":"root_000934/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","surface_ar":"إِطْعَٰمٌ"}],"gloss":"söz istemek veya takılan imama söz vermek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiden konuşmasını veya anlatıyı sürdürmesini isteme."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Okuyuşta takılan imama unuttuğu bölümü söyleyip yol gösterme."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kaynakta verilen konuşma isteme ve okuyuşta takılan imama söz verme kalıplarının ortak işlevini açıklar.","boundary_detail":"Bu dal yalnızca belirtilen konuşma ve okuma kalıplarına bağlıdır; gerçek yiyecek istemeye veya duyusal tatmaya genellenmez.","branch_image_ar":"استطعام الكلام وفتح القراءة","concept_gloss":"söz istemek veya takılan imama söz vermek","contextual_glosses":[{"applicability":"İmam okuyuşta durakladığında unuttuğu sözün söylenerek devamının sağlandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Birinden konuşmasını isteme kalıbını kapsamaz.","preserves":"İmama gerekli sözü vererek yol gösterme işlevini korur."},"facet_ids":["F002"],"text":"imama sözü hatırlatmak","usage_role":"contextual"}],"definition":"Belirli söz kalıplarında birinden konuşmasını istemek veya imam okuyuşta takıldığında ona gerekli sözü söyleyerek devam etmesini sağlamak.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiden konuşmasını veya anlatıyı sürdürmesini isteme."},{"facet_id":"F002","role":"associated_use","statement":"Okuyuşta takılan imama unuttuğu bölümü söyleyip yol gösterme."}],"identity_rationale":"Kaynak ifadesi iki sözlü yardım kalıbını bir araya getirir: birinden konuşmasını istemek ve okuyuşta takılan imama gerekli ifadeyi söyleyerek yol göstermek. Her ikisinde de gerçek yiyecek değil, sözün karşı taraftan sağlanması belirleyicidir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"benden konuşmamı istedi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"imam okuyuşta takılırsa sözü hatırlatın"}],"lexicalization_note":"Tanım yalnızca söz isteme ve okuyana unuttuğu bölümü söyleme kalıplarını kapsar; yalın köke bağımsız bir konuşma anlamı yüklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın karışma, aynı isteme ve sağlama yapısını gerçek besinle kuran iç daldadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Buradaki kullanım yalnızca belirli sözlü yardım kalıplarına aittir; komşu dal ise gerçek besin aktarımını anlatır ve konuşma alanına taşınmaz.","focus_only":"Bu dalda sağlanan şey konuşma ya da okumayı sürdüren sözdür.","gloss":"söz sağlama ile besin sağlama","neighbor_only":"Komşu dalda sağlanan veya istenen şey gerçek yiyecek ya da besleyici içecektir.","neighbor_ref":"root_000934/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da bir kişinin ötekinden eksik olan şeyi sağlaması istenir."}],"source_phrase_ar":"استطعمني فلان الحديث إذا أرادك على أن تحدثه وإذا استطعمكم الإمام فأطعموه (maqayis)؛ إذا استفتح فافتحوا عليه (sihah)؛ إذا استفتحكم عند الارتياج فلقنوه (mufradat)","source_summary":"Kaynaklar iki kalıplaşmış söz eylemini bildirir: konuşma talep etmek ve okuyuşta takılan imama gerekli ifadeyi vererek devamını açmak. Bu kullanımlarda besin aktarımı yalnızca biçimsel çağrışım düzeyindedir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه استطعمني الحديث وإذا استطعمكم الإمام فأطعموه أي استفتح فافتحوا عليه أو لقنوه","what_is_not_ar":"ليس منه سؤال الطعام الحقيقي ولا الذوق الحسي"},"support_links":[]},{"boundary":"Dal, yemek yeme olayını değil geçim durumu, kazancın niteliği, konuk ağırlama bolluğu ve tahsis edilmiş gelir kaynağını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000934/B004","candidate_links":[{"candidate_id":"cand_edda19c25e4e912dccb4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","surface_ar":"إِطْعَٰمٌ"}],"gloss":"geçim, bol ikram ve tahsis edilmiş gelir","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Geçim, kazanç veya gelir bakımından iyi ve elverişli durumda olma."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanlara ve konuklara sıkça, bolca yiyecek sunan kişi olma."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kazanç yolu, arazi geliri, vergi payı veya kamu gelirinin birine geçim kaynağı olarak ayrılması."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kazancın temiz, uygun ya da kötü oluşunun nitelenmesi."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İyi geçim durumunu, bol yiyecek sunmayı ve kişiye ayrılan gelir kaynağını birlikte kapsayan açıklamadır.","boundary_detail":"Dal, yemek yeme olayını değil geçim durumu, kazancın niteliği, konuk ağırlama bolluğu ve tahsis edilmiş gelir kaynağını anlatır.","branch_image_ar":"رزق ومعاش وحسن حال","concept_gloss":"geçim, bol ikram ve tahsis edilmiş gelir","contextual_glosses":[{"applicability":"Bir arazi, yöre geliri veya kamu payı bir kişiye kazanç kaynağı olarak ayrıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İyi durum, bol ikram ve kazancın niteliği yönlerini kapsamaz.","preserves":"Birine ayrılan gelir ve geçim kaynağı yönünü korur."},"facet_ids":["F003"],"text":"geçim payı","usage_role":"contextual"}],"definition":"Kişinin geçim ve kazanç bakımından iyi durumda veya payına düşen gelir bakımından talihli olması; ayrıca bol yiyecek sunması ya da bir gelir kaynağının birine geçim payı olarak ayrılması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Geçim, kazanç veya gelir bakımından iyi ve elverişli durumda olma."},{"facet_id":"F002","role":"specialization","statement":"İnsanlara ve konuklara sıkça, bolca yiyecek sunan kişi olma."},{"facet_id":"F003","role":"extension","statement":"Bir kazanç yolu, arazi geliri, vergi payı veya kamu gelirinin birine geçim kaynağı olarak ayrılması."},{"facet_id":"F004","role":"associated_use","statement":"Kazancın temiz, uygun ya da kötü oluşunun nitelenmesi."}],"identity_rationale":"Kaynak ifadesi iyi geçim içinde olma, rızkı açık olma, insanlara bolca yiyecek sunma ve gelir sağlayan pay ya da mülk anlamlarını ortak geçim alanında toplar. Yeme eylemi bu dalın özü değil, geçimin sağladığı maddi dayanağın arka planıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"geçimi yerinde"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"rızkı açık, kazançlı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"çok ikram eden"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"geçim veya kazanç kaynağı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kazancı temiz veya kötü"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"araziyi birine geçim payı olarak ayırdı"}],"lexicalization_note":"Yalın nitelemeler iyi durum, rızık ve bol ikramı; kalıplaşmış kullanımlar ise kazancın niteliğini ve bir yerin gelir kaynağı olarak tahsisini gösterir.","neighbor_coverage_note":"Bütün komşular değerlendirildi; ayrılmış geçim payı komşusu, dalın gelir tahsisi ile kişisel geçim ve ikram yönleri arasındaki sınırı en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme tahsis edilmiş geçim payındadır; buradaki dal kişinin iyi geçimi ve ikramcılığına kadar uzanırken komşu, ayrılan pay ve bağışın kendisine daha geniş biçimde odaklanır.","focus_only":"Bu dal iyi geçim durumunu, bol ikramı ve kazancın niteliğini de kapsar.","gloss":"geçim kaynağı ve ayrılmış pay","neighbor_only":"Komşu dal daha genel biçimde birine ayrılan pay, yiyecek veya hükümdar bağışını adlandırır.","neighbor_ref":"root_000043/B003","relation_type":"near_synonym","shared_zone":"Her iki dal bir kişiye düşen rızık veya gelir payını anlatabilir."}],"source_phrase_ar":"رجل طاعم حسن الحال ومطعام كثير القرى ومطعم مرزوق والطعمة المأكلة (maqayis)؛ حسن المطعم وحسن الطعمة (ayn)؛ الطعمة وجه المكسب وجعلت الضيعة طعمة (sihah)؛ ناحية كذا طعمة والخراج والإتاوات والفيء والخراج (tahdhib)","source_summary":"Ortak alan kişinin geçim durumu ve elde ettiği rızıktır; bol ikram eden kişi, kazancın iyi ya da kötü niteliği ve tahsis edilmiş arazi veya gelir bu alanın farklı gerçekleşmeleridir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الطاعم حسن الحال والمطعم المرزوق والمطعام كثير القرى والطعمة مأكلة أو وجه مكسب أو ضيعة أو فيء وخراج","what_is_not_ar":"ليس منه نفس أكل الطعام إلا من جهة أنه مادة الرزق"},"support_links":["sup_2ffe64fb429baf2af6ba"]},{"boundary":"Anlam insan yiyeceğinin genel adı değildir ve kaynakta desteklenmeyen bütün nesnelerin tat kazanmasına genellenmez.","branch_kind":"collocation","branch_ref":"root_000934/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","surface_ar":"إِطْعَٰمٌ"}],"gloss":"olgunlaşıp tat kazanmak","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Meyvenin olgunlaşıp yenilebilir ve belirgin bir tat kazanması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hurma ağacı veya hurma meyvesi olgunlaştığında tadı belirginleşir."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Meyvenin olgunlaşmasını ve belirli süt kalıbındaki tat kazanımını ortak sonuç üzerinden anlatır.","boundary_detail":"Anlam insan yiyeceğinin genel adı değildir ve kaynakta desteklenmeyen bütün nesnelerin tat kazanmasına genellenmez.","branch_image_ar":"إدراك الثمر وأخذ الطعم","concept_gloss":"olgunlaşıp tat kazanmak","contextual_glosses":[{"applicability":"Hurma ağacı veya başka bir meyvenin yenilecek olgunluğa eriştiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tulumdaki sütün hoş tat kazanması kullanımını kapsamaz.","preserves":"Meyvenin olgunlaşıp tat kazanma sürecini korur."},"facet_ids":["F001"],"text":"meyvesi olgunlaşmak","usage_role":"contextual"}],"definition":"Meyvenin, özellikle hurma ağacının ürünü olgunlaşarak yenilebilir ve belirgin bir tat kazanmış duruma gelmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Meyvenin olgunlaşıp yenilebilir ve belirgin bir tat kazanması."},{"facet_id":"F002","role":"specialization","statement":"Hurma ağacı veya hurma meyvesi olgunlaştığında tadı belirginleşir."}],"identity_rationale":"Kaynak ifadesi genel olarak her şeyin tadının bulunmasını değil, hurma ağacı veya meyvenin olgunlaşıp belirgin tat kazanmasını bildirir. Bu nedenle dal, meyvenin olgunlaşması ve tat kazanmasıyla sınırlı biçimde yeniden çerçevelenmiştir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ağacın meyvesi olgunlaşıp tat kazandı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"tulumda hoş tat kazanmış süt"}],"lexicalization_note":"Tanım yalnızca meyve veya hurma ağacının olgunlaşıp tat kazanması kalıbına bağlıdır.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; genel meyve olgunlaşması komşusu, bu dalın tat kazanma koşulunu en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Meyve bağlamında büyük ölçüde örtüşürler; buradaki dalın ayırıcı yanı olgunluğun tat kazanma olarak kavranmasıdır.","focus_only":"Bu dal meyvenin olgunlaşmasını özellikle yenilebilir tat kazanması bakımından kurar.","gloss":"tat kazanma ile genel olgunlaşma","neighbor_only":"Komşu dal meyve ve ağacın olgunlaşmasını tat vurgusu olmadan daha genel biçimde anlatır.","neighbor_ref":"root_001699/B001","relation_type":"near_synonym","shared_zone":"Her iki dal meyvenin olgunluğa erişmesini anlatır."}],"source_phrase_ar":"للنخلة إذا أدرك ثمرها قد أطعمت (maqayis)؛ أطعمت النخلة واطعمت البسرة صار لها طعم وأخذت الطعم (sihah)؛ الشجر المثمر الذي يؤكل ثمره واطعمت الثمرة أخذت الطعم (tahdhib)","source_summary":"Kaynakların ortak çekirdeği meyvenin, özellikle hurma meyvesinin, olgunlaşıp tat kazanmasıdır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه أطعمت النخلة أو الثمرة إذا أدرك ثمرها أو أخذت الطعم، وكل شيء وجد طعمه، واللبن المطعم والشجر المثمر","what_is_not_ar":"ليس منه طعام الإنسان مطلقا ولا الرزق المالي"},"support_links":[]},{"boundary":"Genel insan besleme anlamı ile hayvanın semizliği bu av alanına dahil değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000934/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","surface_ar":"إِطْعَٰمٌ"}],"gloss":"avı kazandıran araç, uzuv veya kişi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Avı ele geçirerek avcıya yiyecek veya kazanç sağlayan araç olma."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Avcı kuşun avı kavramaya yarayan öndeki kalın parmağı."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Avda sıkça başarı gösteren ve avdan yana payı açık kişi."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Avın ele geçirilmesini sağlayan yay ve kuş parmağı ile avda başarılı kişiyi ortak işlev altında kapsar.","boundary_detail":"Genel insan besleme anlamı ile hayvanın semizliği bu av alanına dahil değildir.","branch_image_ar":"آلة الصيد التي تطعم صاحبها","concept_gloss":"avı kazandıran araç, uzuv veya kişi","contextual_glosses":[{"applicability":"Avı vurarak sahibine yiyecek veya kazanç sağlayan yayın nitelenmesinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kuş parmağını ve avda talihli kişi anlamını kapsamaz.","preserves":"Yayın avı sahibine kazandırma işlevini korur."},"facet_ids":["F001"],"text":"av getiren yay","usage_role":"contextual"}],"definition":"Avı yakalayıp sahibine kazandıran yay veya avcı kuş uzvu; ayrıca avda sıkça başarılı olup avdan pay alan kişi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Avı ele geçirerek avcıya yiyecek veya kazanç sağlayan araç olma."},{"facet_id":"F002","role":"specialization","statement":"Avcı kuşun avı kavramaya yarayan öndeki kalın parmağı."},{"facet_id":"F003","role":"extension","statement":"Avda sıkça başarı gösteren ve avdan yana payı açık kişi."}],"identity_rationale":"Kaynak ifadesi yalnızca bir av aracını değil, avı sahibine kazandıran yayı, avcı kuşun öndeki kalın parmağını ve avdan yana talihli kişiyi birlikte verir. Dal bu yüzden tek bir araç olarak değil, avı ele geçirmeye ve avdan pay almaya yarayan araç, uzuv ve kişi nitelemeleri olarak kurulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"av getiren yay"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"avcı kuşun öndeki kalın parmağı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"avdan yana talihli, avı bol"}],"lexicalization_note":"Tanım yay ve av başarısı kalıplarını ayrı tutarken avcı kuşun parmak adını yalın, bedensel bir alt anlam olarak gösterir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel avlanma dalı, buradaki işlevsel araç ve başarı nitelemelerinin dar kapsamını en iyi ortaya koyar.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Buradaki dar nitelemeler avı sahibine kazandırma sonucuna bağlıdır; komşu ise avlanma etkinliğinin ve nesnelerinin genel söz varlığıdır.","focus_only":"Bu dal avı kazandıran belirli yay, kuş parmağı ve başarılı avcı nitelemelerini adlandırır.","gloss":"av başarısı ile genel avlanma","neighbor_only":"Komşu dal avlanma eylemini, avı, av aracını ve av köpeğini genel bir alan olarak kapsar.","neighbor_ref":"root_000896/B001","relation_type":"same_field","shared_zone":"Her iki dal avın ele geçirilmesi ve av araçları alanındadır."}],"source_phrase_ar":"قوس مطعمة تطعم صاحبها الصيد والإصبع المتقدمة من الجارحة مطعمة (maqayis)؛ المطعمة القوس والمطعمتان في رجل كل طائر (sihah)؛ مطعم للصيد وقوس مطعمة والمطعمة من الجوارح (tahdhib)","source_summary":"Kaynaklar yayı, kuşun öndeki avcı parmağını ve avda başarılı kişiyi avın sahibine kazandırılması bağıyla birleştirir. Bunlar sırasıyla araç, beden bölümü ve kişi niteliğidir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه القوس المطعمة والجوارح أو الإصبع المطعمة وما يطعم صاحبه الصيد أو يكون مرزوقا منه","what_is_not_ar":"ليس منه الإطعام الآدمي العام ولا سمن الحيوان"},"support_links":[]},{"boundary":"Dal genel tat alma veya her türlü beden yağı değil, hayvanın belirli derecedeki semizliği ve ilikteki yağ belirtisiyle sınırlıdır.","branch_kind":"bare","branch_ref":"root_000934/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","surface_ar":"إِطْعَٰمٌ"}],"gloss":"ilikte yağı beliren, biraz semiz hayvan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hayvanın iliğinde yağ tadı ve belirtisi bulunması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanın biraz semiz veya zayıfla semiz arasında olması."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın ilik yağını ve zayıfla semiz arasındaki beden durumunu birlikte ifade eder.","boundary_detail":"Dal genel tat alma veya her türlü beden yağı değil, hayvanın belirli derecedeki semizliği ve ilikteki yağ belirtisiyle sınırlıdır.","branch_image_ar":"سمن الحيوان وطعم الشحم","concept_gloss":"ilikte yağı beliren, biraz semiz hayvan","contextual_glosses":[{"applicability":"Koyun veya devenin zayıfla tam semiz arasında bulunduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İlikte yağ tadı bulunması ölçütünü açıkça göstermez.","preserves":"Hayvanın kısmi semizlik derecesini korur."},"facet_ids":["F002"],"text":"biraz semiz","usage_role":"contextual"}],"definition":"Bir hayvanın iliğinde yağ tadı bulunacak kadar semiz olması veya zayıf ile tam semiz arasında bir miktar yağ tutmuş bulunması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hayvanın iliğinde yağ tadı ve belirtisi bulunması."},{"facet_id":"F002","role":"specialization","statement":"Hayvanın biraz semiz veya zayıfla semiz arasında olması."}],"identity_rationale":"Kaynak ifadesi hayvanın iliğinde yağ tadı bulunmasını ve koyun, deve ya da kesimlik hayvanın bir miktar semiz veya zayıfla semiz arasında olmasını bildirir. Duyusal tat burada bağımsız amaç değil, beden yağının saptanma belirtisidir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"iliğinde yağ bulunan deve"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"biraz semiz, orta yağlı"}],"lexicalization_note":"Tanım hayvanın ilik ve beden yağından anlaşılan semizlik derecesini yalın dal anlamı olarak verir; başka alanlardaki özel kalıpları içeri almaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel yağlılık komşusu, bu dalın hayvana ve ilik belirtisine bağlı dar sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Buradaki anlam hayvanla ve belirli bir semizlik derecesiyle sınırlıdır; komşu ise bedenin genel yağlanmasını daha geniş katılımcı kapsamıyla anlatır.","focus_only":"Bu dal hayvana özgüdür ve kısmi semizliği ilikteki yağ belirtisiyle birlikte tanımlar.","gloss":"kısmi hayvan semizliği ve genel yağlılık","neighbor_only":"Komşu dal insanı veya hayvanı kapsayan genel yağlılık ve bedenin yağla dolması anlamındadır.","neighbor_ref":"root_000779/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bedende yağ bulunması ve semizlik alanında örtüşür."}],"source_phrase_ar":"المطعم من الإبل الذي يوجد في مخه طعم الشحم وشاة طعوم فيها بعض السمن (maqayis)؛ جزور طعوم وطعيم بين الغثة والسمينة (sihah)؛ ناقة طعوم وجزور طعوم وطعيم (tahdhib)","source_summary":"Kaynaklar hayvandaki semizliği, ilikte algılanan yağ belirtisi ve zayıflıkla tam semizlik arasındaki beden durumu üzerinden tanımlar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه المطعم من الإبل إذا وجد في مخه طعم الشحم وشاة أو ناقة أو جزور طعوم أو طعيم في السمن","what_is_not_ar":"ليس منه الطعم بمعنى الذوق إلا باعتبار أثر السمن"},"support_links":[]},{"boundary":"Bu dal duyusal lezzeti veya yiyeceği değil, belirli kişi niteleme kalıplarında akıl, değer ve düzelmeye açıklık değerlendirmesini anlatır.","branch_kind":"collocation","branch_ref":"root_000934/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","surface_ar":"إِطْعَٰمٌ"}],"gloss":"akıl, değer ve düzelmeye açıklık niteliği","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Akıl, sağlam yargı ve ölçülü karar gücü taşıma."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olumsuz kalıpta akıl, devinim, değer veya dolgunluktan yoksun olma."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Öğüt, eğitim veya düzeltmeden yararlanmayıp uslanmama."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Olumlu ve olumsuz kişi niteleme kalıplarındaki değerlendirme eksenini birlikte gösterir.","boundary_detail":"Bu dal duyusal lezzeti veya yiyeceği değil, belirli kişi niteleme kalıplarında akıl, değer ve düzelmeye açıklık değerlendirmesini anlatır.","branch_image_ar":"طعم العقل والقيمة","concept_gloss":"akıl, değer ve düzelmeye açıklık niteliği","contextual_glosses":[{"applicability":"Kişinin akıllı ve sağlam yargılı olduğunun olumlu biçimde belirtildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Olumsuz değer, devinim ve eğitilemezlik kullanımlarını kapsamaz.","preserves":"Akıl ve sağlam yargı niteliğini korur."},"facet_ids":["F001"],"text":"aklı başında","usage_role":"contextual"}],"definition":"Belirli kişi nitelemelerinde akıl, sağlam yargı veya dikkate değer bir nitelik taşıma; olumsuz biçimlerde bunlardan yoksun, cılız, devinimsiz ya da düzeltilemez olma.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Akıl, sağlam yargı ve ölçülü karar gücü taşıma."},{"facet_id":"F002","role":"source_variant","statement":"Olumsuz kalıpta akıl, devinim, değer veya dolgunluktan yoksun olma."},{"facet_id":"F003","role":"associated_use","statement":"Öğüt, eğitim veya düzeltmeden yararlanmayıp uslanmama."}],"identity_rationale":"Kaynak ifadesi olumlu olarak akıl ve sağlam yargıyı, olumsuz kalıplarda ise akılsızlık, devinimsizlik, değersizlik, eğitilemezlik veya cılızlığı bildirir. Dalın 'akıl ve değer' çerçevesi kullanılabilir, ancak olumsuz biçimlerin her zaman yalnızca akıl yokluğu demediği açıkça korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"akıllı ve sağlam yargılı"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"aklı, devinimi veya değeri yok"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"terbiye kabul etmez, uslanmaz"}],"lexicalization_note":"Anlam yalnızca akıllı olma, akıl ya da değer yokluğu ve terbiyeden yararlanmama bildiren kişi niteleme kalıplarında geçerlidir.","neighbor_coverage_note":"Adayların tümü değerlendirildi; engelleyici akıl komşusu ortak çekirdeği gösterirken bu dalın değer ve eğitilebilirlik uzantılarını ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme akıl niteliğindedir; burada anlam olumlu ve olumsuz kişi değerlendirmelerine yayılırken komşuda aklın davranışı dizginleyen işlevi belirleyicidir.","focus_only":"Bu dal kalıplaşmış kişi nitelemelerinde değer, devinim ve eğitilebilirliği de akılla birlikte değerlendirir.","gloss":"kişi değeri ile engelleyici akıl","neighbor_only":"Komşu dal aklı özellikle kişiyi uygunsuz davranıştan alıkoyan iç engel olarak tanımlar.","neighbor_ref":"root_000296/B002","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin akıllı ve ölçülü oluşunu anlatabilir."}],"source_phrase_ar":"ما فلان بذي طعم إذا كان غثا (sihah)؛ رجل ذو طعم أي ذو عقل وحزم وما بفلان طعم ولا نويص ولا يطعم أي لا يتأدب ولا يعقل (tahdhib)","source_summary":"Kaynaklar kişi hakkında olumlu bir akıl ve yargı niteliği ile bunun olumsuzlanmasını verir; olumsuzlama bağlama göre akılsızlık, devinimsizlik, değersizlik, cılızlık veya eğitilemezlik biçiminde açılır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه ذو طعم أي ذو عقل وحزم، وما بفلان طعم أي لا عقل ولا حراك أو لا قيمة، ولا يطعم أي لا يتأدب ولا ينجع فيه الإصلاح","what_is_not_ar":"ليس منه حسن الطعم الحسي ولا الطعام"},"support_links":[]},{"boundary":"Ağız bölümü ile koşma talebi ayrı tutulur; yiyecek, kuş ayağı veya atın fiilen koşması bu dalın doğrudan anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000934/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","surface_ar":"إِطْعَٰمٌ"}],"gloss":"atın ağız bölümü ve koşma talebi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Atın burun altı ile dudak uçları arasındaki ağız bölümü."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Attan hızlanmasını veya koşmasını isteme."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"At anatomisine ait adlandırmayı ve yalnızca ata yöneltilen koşma isteğini ayrı yönleriyle kapsar.","boundary_detail":"Ağız bölümü ile koşma talebi ayrı tutulur; yiyecek, kuş ayağı veya atın fiilen koşması bu dalın doğrudan anlamı değildir.","branch_image_ar":"مستطعم الفرس وطلب جريه","concept_gloss":"atın ağız bölümü ve koşma talebi","contextual_glosses":[{"applicability":"Binicinin attan koşmasını veya hızlanmasını istediği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Atın ağız bölümü adlandırmasını kapsamaz.","preserves":"Ata yöneltilen koşma talebini korur."},"facet_ids":["F002"],"text":"atı koşturmaya çağırmak","usage_role":"contextual"}],"definition":"Atın burun altından dudaklarının uçlarına kadar uzanan ağız bölümü; ayrıca belirli bir kalıpta attan koşmasını isteme.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Atın burun altı ile dudak uçları arasındaki ağız bölümü."},{"facet_id":"F002","role":"associated_use","statement":"Attan hızlanmasını veya koşmasını isteme."}],"identity_rationale":"Kaynak ifadesi atın burun altından dudak uçlarına uzanan ağız bölümünü ve attan koşmasını isteme eylemini ayrı fakat aynı at alanında verir. Dalın kimliği bu iki alt alanı kaynaştırmadan birlikte koruduğunda kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"atın burun altı ve dudak çevresi"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"attan koşmasını istedi"}],"lexicalization_note":"Atın ağız bölümü yalın adlandırma, koşmasını isteme ise yalnızca belirtilen kalıp olarak tanımlanır; ikisi tek bir eylem anlamında birleştirilmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; atın fiili koşusunu anlatan komşu, bu dalın koşmayı isteme yönünü en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Burada eylem binicinin ata yönelttiği taleptir; komşuda ise atın gerçekleştirdiği hızlı koşu ve bunun yere etkisi öne çıkar.","focus_only":"Bu dal koşmanın kendisini değil, attan koşmasını istemeyi ve ayrıca atın ağız bölümünü bildirir.","gloss":"koşma talebi ile atın koşusu","neighbor_only":"Komşu dal atın fiili koşusunu, hızını ve toynağıyla yeri güçlü biçimde eşmesini anlatır.","neighbor_ref":"root_001599/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal atın koşması çevresindeki aynı hareket sahnesine katılır."}],"source_phrase_ar":"مستطعم الفرس جحافله (sihah)؛ مستطعم الفرس ما تحت مرسنه إلى أطراف جحافله واستطعمت الفرس إذا طلبت جريه (tahdhib)","source_summary":"Kaynaklar atın ağız ve dudak çevresindeki belirli bölgesini adlandırır; ayrıca ayrı bir söz kalıbında binicinin attan koşmasını istemesini bildirir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه مستطعم الفرس وهو ما تحت مرسنه إلى جحافله أو جحافله، واستطعمت الفرس إذا طلبت جريه","what_is_not_ar":"ليس منه الطعام ولا مطعمة الطائر"},"support_links":[]},{"boundary":"Anlam besleme değildir; yalnızca eklenen dalın birleşmeyi kabul etmesi ve gözün içine giren yabancı cismi tutması kalıplarıyla sınırlıdır.","branch_kind":"collocation","branch_ref":"root_000934/B010","candidate_links":[{"candidate_id":"cand_3a5ec2be6facaa151d47","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","surface_ar":"إِطْعَٰمٌ"}],"gloss":"eklenen şeyin tutması","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başka ağaçtan eklenen dalın ana dalla birleşmeyi kabul edip tutması."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Göze giren küçük yabancı cismin göz tarafından tutulması."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Aşı dalının birleşmesi ve göze giren yabancı cismin kalması kullanımlarındaki ortak tutunma sonucunu açıklar.","boundary_detail":"Anlam besleme değildir; yalnızca eklenen dalın birleşmeyi kabul etmesi ve gözün içine giren yabancı cismi tutması kalıplarıyla sınırlıdır.","branch_image_ar":"إطعام الغصن وقبول الوصل","concept_gloss":"eklenen şeyin tutması","contextual_glosses":[{"applicability":"Başka ağaçtan eklenen dalın ana dala kaynayıp gelişebildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Göze giren yabancı cismin gözde kalması kullanımını kapsamaz.","preserves":"Eklenen dalın birleşmeyi kabul edip tutmasını korur."},"facet_ids":["F001"],"text":"aşı tutmak","usage_role":"contextual"}],"definition":"Bir ağaca eklenen başka bir dalın birleşip tutması; ayrıca göze giren küçük yabancı cismin gözde kalması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başka ağaçtan eklenen dalın ana dalla birleşmeyi kabul edip tutması."},{"facet_id":"F002","role":"source_variant","statement":"Göze giren küçük yabancı cismin göz tarafından tutulması."}],"identity_rationale":"Kaynak ifadesi iki kabul ilişkisini birlikte verir: bir dala başka ağaçtan parça eklenmesi ve birleşmenin tutması, ayrıca göze çöp girip gözün onu içinde tutması. Dalın dal aşılama çerçevesi kullanılabilir, ancak gözde yabancı cismin tutunması bağımsız ikinci kalıp olarak açıkça korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"dala aşı yaptı ve aşı tuttu"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"gözüne küçük bir yabancı cisim girdi"}],"lexicalization_note":"Tanım, dal aşılama ve göze yabancı cisim girme kalıplarındaki kabul veya tutunma sonucuna bağlıdır; yalın köke genel birleşme anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel birleştirme komşusu, bu dalın tutunma ve kabul sonucu gerektiren dar yapısını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Burada eklenen unsurun alıcıda tutunması ve kabul edilmesi gerekir; komşuda ise genel katma veya toplama yeterlidir ve böyle bir sonuç koşulu yoktur.","focus_only":"Bu dal yalnızca aşı dalının veya gözdeki yabancı cismin tutunması sonucuna bağlıdır.","gloss":"tutunan ek ile genel birleştirme","neighbor_only":"Komşu dal nesneleri genel olarak birbirine katma, toplama ve birlikte bulundurma eylemlerini kapsar.","neighbor_ref":"root_000915/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal ayrı bir şeyin başka bir şeye katılması sahnesini içerir."}],"source_phrase_ar":"أطعمت الغصن إذا وصلت به غصنا فقبل الوصل وأطعمت عينه قذى فطعمته (tahdhib)","source_summary":"Tek kaynak, eklenen dalın ağaçta tutması ile küçük bir yabancı cismin gözde kalmasını kabul ve tutunma sonucu altında yan yana getirir.","sources":["TA"],"what_is_ar":"يدخل فيه إطعام الغصن إذا وصل به غصن من غير شجره فقبل الوصل، وإطعام العين قذى فطعمته","what_is_not_ar":"ليس منه الإطعام بمعنى التغذية"},"support_links":["sup_9d0b5164baa90d1667b0"]},{"boundary":"Anlam yalnızca belirtilen kalıpta bir şeye gücü yetmeyi anlatır; genel egemenlik, mülkiyet veya duyusal tat bu dala eklenmez.","branch_kind":"collocation","branch_ref":"root_000934/B011","candidate_links":[{"candidate_id":"cand_05c3e0aa40dccce35b30","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","surface_ar":"إِطْعَٰمٌ"}],"gloss":"gücü yetmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işi yapabilecek ya da bir şeyin üstesinden gelebilecek güce sahip olma."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakta verilen kalıpta bir işi yapabilme veya bir şeyin üstesinden gelebilme anlamını tam karşılar.","boundary_detail":"Anlam yalnızca belirtilen kalıpta bir şeye gücü yetmeyi anlatır; genel egemenlik, mülkiyet veya duyusal tat bu dala eklenmez.","branch_image_ar":"القدرة على الشيء","concept_gloss":"gücü yetmek","contextual_glosses":[{"applicability":"Gücün belirli bir işi başarmaya veya engeli aşmaya yöneldiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir şeye yeten güç ve başarı imkanını korur."},"facet_ids":["F001"],"text":"üstesinden gelebilmek","usage_role":"contextual"}],"definition":"Belirli bir söz kalıbında bir şeyi yapmaya veya onun üstesinden gelmeye gücü yetmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işi yapabilecek ya da bir şeyin üstesinden gelebilecek güce sahip olma."}],"identity_rationale":"Kaynak ifadesi belirli bir edatlı kalıpta kişinin bir şey üzerinde gücü bulunmasını ve onu yapabilmesini doğrudan bildirir. Tatma ve yeme alanlarıyla biçim ortaklığı dışında bir anlam bağı kurulmaz.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"ona gücü yetti"}],"lexicalization_note":"Tanım yalnızca bir şey üzerinde gücü bulunma kalıbına bağlıdır ve yalın köke genel bir yeterlik anlamı vermez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel yeterlik komşusu, anlam yakınlığını ve bu dalın kalıba bağlı olma sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Anlamsal çekirdek büyük ölçüde aynıdır; buradaki dalın sınırı tek bir kalıba bağlı olması, komşunun ise genel yeterlik alanını kapsamasıdır.","focus_only":"Bu dal yeterliği yalnızca belirli bir edatlı söz kalıbında ve yöneldiği şeyle birlikte ifade eder.","gloss":"kalıba bağlı ve genel yeterlik","neighbor_only":"Komşu dal yapabilme ve güç yetirme anlamını daha genel söz biçimleriyle taşır.","neighbor_ref":"root_000048/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir işi yapabilecek güç ve yeterliğe sahip olmayı anlatır."}],"source_phrase_ar":"الطعم أيضا القدرة يقال طعمت عليه أي قدرت عليه (tahdhib)","source_summary":"Tek kaynak bu kullanımı, belirli bir kalıp içinde bir şeye gücü yetme ve onun üzerinde yeterli olma anlamıyla verir.","sources":["TA"],"what_is_ar":"يدخل فيه الطعم بمعنى القدرة، طعمت عليه أي قدرت عليه","what_is_not_ar":"ليس منه الذوق ولا الأكل"},"support_links":["sup_c0b563797e6464b0e9a6"]},{"boundary":"Dal genel tutma eylemini değil, boğma ve kavga sırasında boğazı kavrayıp sıkma hareketini anlatır.","branch_kind":"collocation","branch_ref":"root_000934/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","surface_ar":"إِطْعَٰمٌ"}],"gloss":"boğazından yakalayıp sıkmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin boğazını elle kavrayıp sıkarak nefesini baskılama."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemin yalnızca boğma veya dövüş bağlamında gerçekleştirilmesi."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Boğma ya da dövüşte boğazın kavranıp baskı altına alındığı hareketi doğrudan karşılar.","boundary_detail":"Dal genel tutma eylemini değil, boğma ve kavga sırasında boğazı kavrayıp sıkma hareketini anlatır.","branch_image_ar":"الأخذ بالمطعمة عند الخنق","concept_gloss":"boğazından yakalayıp sıkmak","contextual_glosses":[{"applicability":"Kavga sırasında karşı tarafın boğazının elle kavrandığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıkmanın nefesi baskılama sonucunu zorunlu olarak belirtmez.","preserves":"Boğazı doğrudan kavrama hareketini korur."},"facet_ids":["F001","F002"],"text":"boğazına sarılmak","usage_role":"contextual"}],"definition":"Boğma veya dövüş sırasında bir kişiyi boğazından kavrayıp baskı uygulayarak sıkmak.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin boğazını elle kavrayıp sıkarak nefesini baskılama."},{"facet_id":"F002","role":"specialization","statement":"Eylemin yalnızca boğma veya dövüş bağlamında gerçekleştirilmesi."}],"identity_rationale":"Kaynak ifadesi bir kişiyi boğma veya dövüş sırasında boğazından yakalayıp sıkmayı, yalnızca bu şiddet bağlamına özgü bir kalıpla bildirir. Beden bölümü, avcı kuşun parmağı ya da geçim anlamlarıyla karıştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"boğazından yakalayıp sıktı"}],"lexicalization_note":"Tanım yalnızca boğma veya dövüş bağlamındaki boğazdan yakalama kalıbıyla sınırlıdır; yalın bir tutma anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel boğma komşusu, bu dalın boğazdan elle yakalama ve kavga koşulunu en iyi sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Buradaki anlam belirli bir elle yakalama kalıbı ve şiddet bağlamıdır; komşu dal yapanı, aracı ve kendiliğinden boğulmayı da içeren daha geniş boğma alanıdır.","focus_only":"Bu dal boğma veya kavga sırasında boğazı elle kavrayıp sıkma kalıbıyla sınırlıdır.","gloss":"boğazdan yakalama ve genel boğma","neighbor_only":"Komşu dal boğazı elle veya araçla sıkmayı, boğulmayı ve boğma aracını genel olarak kapsar.","neighbor_ref":"root_000444/B001","relation_type":"near_synonym","shared_zone":"Her iki dal boyun veya boğaza baskı uygulayarak boğma alanında örtüşür."}],"source_phrase_ar":"أخذ فلان بمطعمة فلان إذا أخذ بحلقه يعصره ولا يقولونها إلا عند الخنق والقتال (tahdhib)","source_summary":"Tek kaynak kalıbı, boğma veya kavga sırasında karşı tarafın boğazını yakalayıp sıkma eylemine özgüler.","sources":["TA"],"what_is_ar":"يدخل فيه أخذ بمطعمة فلان أي أخذ بحلقه يعصره عند الخنق والقتال","what_is_not_ar":"ليس منه مطعمة الجارحة ولا المطعم بمعنى الرزق"},"support_links":[]},{"boundary":"Dal genel öpme, sarılma veya ağızla yeme anlamına değil, ağızların doğrudan birbirine geçirilmesi biçimindeki karşılıklı temasa bağlıdır.","branch_kind":"bare","branch_ref":"root_000934/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","surface_ar":"إِطْعَٰمٌ"}],"gloss":"ağız ağıza temas etmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki tarafın ağızlarını doğrudan ve karşılıklı olarak birbirine geçirmesi."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güvercinlerin öpüşmeye benzeyen ağız teması kurması."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ağızların karşılıklı olarak birbirine değdirilip geçirilmesi biçimindeki bedensel teması açıklar.","boundary_detail":"Dal genel öpme, sarılma veya ağızla yeme anlamına değil, ağızların doğrudan birbirine geçirilmesi biçimindeki karşılıklı temasa bağlıdır.","branch_image_ar":"التطاعم بالفم","concept_gloss":"ağız ağıza temas etmek","contextual_glosses":[{"applicability":"Temasın öpüşme benzeri karşılıklı bir hareket olarak anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":"Türkçedeki öpüşme sözü, kaynakta zorunlu olmayan duygusal veya insani bir çağrışım ekleyebilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Ağızların karşılıklı ve doğrudan temasını korur."},"facet_ids":["F001","F002"],"text":"ağız ağıza öpüşmek","usage_role":"contextual"}],"definition":"İki canlının ağızlarını doğrudan birbirine değdirip birinin ağzını ötekininkine sokması; öpüşmeye benzeyen karşılıklı ağız teması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki tarafın ağızlarını doğrudan ve karşılıklı olarak birbirine geçirmesi."},{"facet_id":"F002","role":"example","statement":"Güvercinlerin öpüşmeye benzeyen ağız teması kurması."}],"identity_rationale":"Kaynak ifadesi iki canlının ağızlarını birbirine değdirip birinin ağzını ötekininkine sokmasını, güvercin davranışıyla örneklenen öpüşme benzeri bir temas olarak verir. Burada ağızla yiyecek tüketme değil, karşılıklı bedensel temas esastır.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"ağız ağıza temas etme"}],"lexicalization_note":"Tanım ağızların karşılıklı doğrudan temasını yalın dal anlamı olarak korur ve yiyecek tüketme alanını dışarıda bırakır.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel öpme komşusu, bu dalın karşılıklı ağız ağıza temas koşulunu en belirgin biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Buradaki anlam karşılıklı ağız ağıza geçme biçimiyle daralır; komşu dal ise temasın bu özel biçimini zorunlu kılmadan genel öpmeyi anlatır.","focus_only":"Bu dal ağızların karşılıklı olarak birbirine geçirilmesini ve iki taraflı teması gerektirir.","gloss":"ağız ağıza temas ve genel öpme","neighbor_only":"Komşu dal tek yönlü veya karşılıklı olabilen genel öpme eylemini kapsar.","neighbor_ref":"root_001198/B006","relation_type":"near_synonym","shared_zone":"Her iki dal ağız çevresindeki öpüşme benzeri bedensel teması anlatabilir."}],"source_phrase_ar":"التطاعم إدخال الفم في الفم كما يفعل الحمام عند التقبيل (tahdhib)","source_summary":"Tek kaynak ağızların birbirine geçirilmesi biçimindeki karşılıklı teması tanımlar ve bunu güvercinlerin öpüşmeye benzeyen davranışıyla örnekler.","sources":["TA"],"what_is_ar":"يدخل فيه التطاعم أي إدخال الفم في الفم كما يفعل الحمام عند التقبيل","what_is_not_ar":"ليس منه تناول الطعام بالفم"},"support_links":[]},{"boundary":"Dal yalnızca oluşumun ardışık düzenini anlatır; genel zaman sürekliliğine, sonsuzluğa veya yiyecek alanına taşınmaz.","branch_kind":"collocation","branch_ref":"root_000934/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","surface_ar":"إِطْعَٰمٌ"}],"gloss":"oluşumu ardışık olmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Oluşumun parçalarının kesintisiz bir sıra içinde birbirini izlemesi."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir varlığın yapısal oluşumunda parçaların birbirini izlediği düzeni tam olarak açıklar.","boundary_detail":"Dal yalnızca oluşumun ardışık düzenini anlatır; genel zaman sürekliliğine, sonsuzluğa veya yiyecek alanına taşınmaz.","branch_image_ar":"تتابع الخلق","concept_gloss":"oluşumu ardışık olmak","contextual_glosses":[{"applicability":"Oluşumun evre veya parçalarının sırayla meydana geldiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Parçaların sırayla meydana gelmesi ve takip ilişkisini korur."},"facet_ids":["F001"],"text":"birbiri ardınca oluşmak","usage_role":"contextual"}],"definition":"Bir varlığın oluşumunun veya yapısının parçalarının birbirini izleyerek ardışık ve bağlantılı biçimde meydana gelmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Oluşumun parçalarının kesintisiz bir sıra içinde birbirini izlemesi."}],"identity_rationale":"Kaynak ifadesi oluşumun veya yaratılışın bölümlerinin birbirini izleyerek ardışık biçimde kurulmasını bildirir. Süreklilik ya da sonsuzluk değil, meydana gelişteki sıra ve takip ilişkisi belirleyicidir.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"oluşumu birbirini izleyen bölümlerden kurulu"}],"lexicalization_note":"Tanım yalnızca oluşum veya yaratılışın birbirini izleyen bölümler halinde kurulmasını bildiren kalıba bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ardışıklık komşusu, bu dalın oluşum yapısına bağlı özel kapsamını en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ardışıklık çekirdeği ortaktır; buradaki dal bunu oluşum yapısına bağlar, komşu ise her türlü nesne ve eylem dizisine uygulanabilen genel bir anlam taşır.","focus_only":"Bu dal ardışıklığı bir varlığın oluşumuna veya yapısının kurulmasına özgüler.","gloss":"oluşumdaki ve genel ardışıklık","neighbor_only":"Komşu dal nesnelerin veya eylemlerin ara vermeden art arda gelmesini genel olarak kapsar.","neighbor_ref":"root_000175/B004","relation_type":"near_synonym","shared_zone":"Her iki dal parçaların ya da olayların birbirini aralıksız izlemesini anlatır."}],"source_phrase_ar":"متطاعم الخلق أي متتابع الخلق (tahdhib)","source_summary":"Tek kaynak bu kalıbı, oluşumun parçalarının birbiri ardından gelmesi ve yapının ardışık biçimde kurulması olarak açıklar.","sources":["TA"],"what_is_ar":"يدخل فيه متطاعم الخلق أي متتابع الخلق","what_is_not_ar":"ليس منه الطعام ولا الطعم الحسي"},"support_links":[]},{"boundary":"Bu dal yalnızca sınırları gün doğumu ve gün batımıyla belirlenen gündüz süresini kapsar; belirsiz süre, devir ve olay anlamları ayrı dallardadır.","branch_kind":"bare","branch_ref":"root_001700/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَوْم","morph_features":"STEM|POS:N|LEM:yawom|ROOT:ywm|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:4:1","qac_word_ref":"90:14:4","surface_ar":"يَوْمٍ"}],"gloss":"güneşin doğuşundan batışına kadarki gün","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başlangıcı güneşin doğuşu, sonu güneşin batışıdır; aynı zamanda sayılabilen günlerden biridir."}}],"root_ar":"ي و م","root_id":"root_001700","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Günün geceyi dışarıda bırakan, doğal ışık sınırlarıyla belirlenmiş tek bir zaman birimi olarak kastedildiği kullanımlara uygundur.","boundary_detail":"Bu dal yalnızca sınırları gün doğumu ve gün batımıyla belirlenen gündüz süresini kapsar; belirsiz süre, devir ve olay anlamları ayrı dallardadır.","branch_image_ar":"وقت النهار المحدود","concept_gloss":"güneşin doğuşundan batışına kadarki gün","contextual_glosses":[{"applicability":"Karşıtlığın geceyle kurulduğu ve sayılabilir birim özelliğinin bağlamdan zaten anlaşıldığı cümlelerde doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güneşin doğuşu ile batışı arasındaki aydınlık zaman aralığını korur."},"facet_ids":["F001"],"text":"gündüz vakti","usage_role":"contextual"},{"applicability":"Hem doğal gündüz sınırının hem de bunun tek bir sayılabilir birim olduğunun açıkça belirtilmesi gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sınırlandırılmış gündüz süresini ve onun tek bir gün birimi oluşunu birlikte korur."},"facet_ids":["F001"],"text":"bir günlük gündüz süresi","usage_role":"explanatory"}],"definition":"Güneşin doğuşundan batışına kadar uzanan bilinen zaman aralığı ve bu aralıklardan oluşan dizinin tek bir birimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başlangıcı güneşin doğuşu, sonu güneşin batışıdır; aynı zamanda sayılabilen günlerden biridir."}],"identity_rationale":"Kaynak ifadesi, bilinen günü güneşin doğuşundan batışına kadar süren zaman olarak tanımlar ve onu günler dizisinin tek bir birimi sayar. Verilen dal çerçevesi bu iki kurucu özelliği de doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"güneşin doğuşundan batışına kadarki gün"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bu anlamdaki günlerin çoğulu"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"gün gün veya gündelik esasa göre yapılan işlem"}],"lexicalization_note":"Dal yalın kullanımı tanımlar; günlük işlem bildiren türemiş kullanım, temel gün anlamının yerine geçirilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca gündüz sınırı, belirsiz süre ve olay günüyle doğrudan karışabilecek üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, başlangıcı güneşin doğuşu olan sayılabilir günü tanımlar. Komşu dal ise şafaktan başlayan gündüzü ve onun ışığını öne çıkarır; bu yüzden sınırları tam örtüşmez.","focus_only":"Gün doğumunu kesin başlangıç sayar ve aralığı sayılabilir tek bir gün birimi olarak kurar.","gloss":"gün ile gündüz","neighbor_only":"Gündüz ışığını ve şafaktan gün batımına uzanan süreyi kapsar; ayrıca gündüzle ilişkili başka kullanımları da içerir.","neighbor_ref":"root_001559/B002","relation_type":"near_synonym","shared_zone":"İkisi de gecenin karşısındaki aydınlık zaman kesitini gün batımına kadar anlatır."},{"boundary_match":"partial","distinction":"Bu dal doğal göksel sınırları olan bilinen gündür; komşu dalın süresi belirlenmemiştir ve devir kadar genişleyebilir.","focus_only":"Süreyi gün doğumu ile gün batımı arasında kesin olarak sınırlar.","gloss":"sınırlı gün ile belirsiz süre","neighbor_only":"Her uzunluktaki bir zaman dilimini ve bazı bağlamlarda bir devri anlatabilir.","neighbor_ref":"root_001700/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir zaman kesitini gün sözü üzerinden kavramlaştırır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği zamansal sınırdır. Komşu dalda gün, olayın büyüklüğünü veya çetinliğini taşıyan mecazî ve bağlama bağlı bir anlatıma dönüşür.","focus_only":"Olayın niteliğinden bağımsız, gerçek bir gündüz zaman aralığını belirtir.","gloss":"zaman birimi ile olay günü","neighbor_only":"Büyük veya çetin bir olayı, onun yaşandığı kritik günü ya da çoğulda olayları belirtir.","neighbor_ref":"root_001700/B003","relation_type":"near_neighbor","shared_zone":"Olay dalındaki kullanımlar, bir gün içinde yaşananlardan hareketle bu zaman birimiyle ilişki kurar."}],"source_phrase_ar":"اليوم: الواحد من الأيام (maqayis)؛ اليوم مقداره من طلوع الشمس إلى غروبها (ayn;tahdhib)؛ اليوم معروف والجمع أيام (sihah)؛ اليوم يعبر به عن وقت طلوع الشمس إلى غروبها (mufradat)","source_summary":"Kaynaklar, bilinen günün güneşin doğuşuyla başlayıp batışıyla bittiği ve çoğulu bulunan sayılabilir bir zaman birimi olduğu konusunda birleşir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"اليوم المعروف: وقت من طلوع الشمس إلى غروبها، وهو الواحد من الأيام وجمعه أيام.","what_is_not_ar":"ليس المراد هنا مطلق الدهر، ولا الوقائع والنعم، ولا تركيب يومئذ."},"support_links":[]},{"boundary":"Bu dal, uzunluğu önceden belirlenmeyen süreyi ve bağlama bağlı devir anlamını kapsar; belirli gündüz aralığını veya olayın kendisini tanımlamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001700/B002","candidate_links":[{"candidate_id":"cand_edda19c25e4e912dccb4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَوْم","morph_features":"STEM|POS:N|LEM:yawom|ROOT:ywm|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:4:1","qac_word_ref":"90:14:4","surface_ar":"يَوْمٍ"}],"gloss":"herhangi bir zaman dilimi; bağlama göre devir","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Herhangi bir uzunluktaki zaman süresini belirtir ve bilinen gündüz sınırlarına bağlı değildir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlama göre uzun bir devir veya bir varlığın yaşadığı dönemler anlamına genişleyebilir."}}],"root_ar":"ي و م","root_id":"root_001700","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sürenin gün doğumu ve gün batımıyla sınırlandırılmadığı, kısa veya uzun bir dönem ya da bütün bir devir olarak yorumlandığı kullanımlara uygundur.","boundary_detail":"Bu dal, uzunluğu önceden belirlenmeyen süreyi ve bağlama bağlı devir anlamını kapsar; belirli gündüz aralığını veya olayın kendisini tanımlamaz.","branch_image_ar":"مدة من الزمان","concept_gloss":"herhangi bir zaman dilimi; bağlama göre devir","contextual_glosses":[{"applicability":"Sürenin sınırlarının önem taşımadığı ve yalnızca belirsiz bir zaman kesitinin anlatıldığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uzunluğu belirtilmemiş bir zaman dilimi olma özelliğini korur."},"facet_ids":["F001"],"text":"bir zaman","usage_role":"contextual"},{"applicability":"Bağlam sözün tek bir günü değil, uzun bir hayat veya tarih dönemini anlattığını gösterdiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözün uzun bir döneme genişleyen bağlamsal kullanımını korur."},"facet_ids":["F002"],"text":"devir","usage_role":"contextual"}],"definition":"Uzunluğu önceden sınırlandırılmamış bir zaman dilimidir; bazı bağlamlarda kişinin veya bir şeyin devri kadar geniş bir süreyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Herhangi bir uzunluktaki zaman süresini belirtir ve bilinen gündüz sınırlarına bağlı değildir."},{"facet_id":"F002","role":"extension","statement":"Bağlama göre uzun bir devir veya bir varlığın yaşadığı dönemler anlamına genişleyebilir."}],"identity_rationale":"Kaynak ifadesi sözü herhangi bir uzunluktaki zaman süresi için genişletir ve bazı kullanımlarda devir anlamına geldiğini açıkça belirtir. Dal çerçevesi, sınırlı gündüz anlamından bu geniş zamansal kullanıma geçişi doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"herhangi bir zaman dilimi; bağlama göre devir"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"iki devri veya bollukla sıkıntı, cömertlikle savaş gibi iki karşıt hali"}],"lexicalization_note":"Yalın biçimin belirsiz süre ve devir kullanımı, iki karşıt hayat durumunu anlatan özel söz öbeğinden ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; süre, devir, zaman parçası ve aynı kökün literal ya da olay odaklı dallarıyla sınırı açıklayan beş komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gün sözünün süre ve devir anlamındaki genişlemesidir. Komşu dal daha genel olarak vakti, anı ve dönemi kapsadığı için bütün bağlamlarda birbirinin yerine geçmez.","focus_only":"Gün sözünün herhangi bir süreye ve bağlama göre bütün bir devre genişlemesini içerir.","gloss":"zaman dilimi ile vakit","neighbor_only":"Bir şeyin vakti, yakın veya gerçekleşmiş anı ve bağlama bağlanan o sırada anlamlarını da içerir.","neighbor_ref":"root_000382/B001","relation_type":"near_synonym","shared_zone":"İki dal da uzunluğu kesin olmayan bir zamanı veya dönemi anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın uzunluk bakımından üst sınırı yoktur. Komşu dal daha sınırlı bir zaman parçasına yönelir ve yerleşme anlamı da taşır.","focus_only":"Süreyi herhangi bir uzunlukta bırakabilir ve onu devir anlamına kadar genişletebilir.","gloss":"serbest süre ile sınırlı zaman parçası","neighbor_only":"Devreden daha kısa belirli bir zaman parçasını ve bir yerde kalmayı da anlatır.","neighbor_ref":"root_000307/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de günün doğal sınırlarına bağlı olmayan bir zaman parçasını belirtebilir."},{"boundary_match":"partial","distinction":"Odak dal çok kısa süreden devre kadar geniştir; komşu dal ise parçalanmış veya birkaç gün süren daha sınırlı bir kesiti öne çıkarır.","focus_only":"Her uzunluktaki süreyi ve bir devri kapsayabilir.","gloss":"belirsiz süre ile zaman parçası","neighbor_only":"Bir parça zaman, birkaç gün süren ara dönem veya devam eden durumla sınırlıdır.","neighbor_ref":"root_000664/B005","relation_type":"near_synonym","shared_zone":"İki dal da kesin başlangıç ve bitişi verilmeyen bir süreyi anlatır."},{"boundary_match":"partial","distinction":"Bu dalın süresi bağlamca belirlenir; komşu dalın sınırları ise güneşin hareketine göre sabittir.","focus_only":"Süreyi doğal gündüz sınırlarından bağımsız bırakır ve devir anlamına genişletebilir.","gloss":"belirsiz süre ile bilinen gün","neighbor_only":"Güneşin doğuşundan batışına kadar kesin sınırlı tek bir gün birimidir.","neighbor_ref":"root_001700/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da gün sözünün bir zaman kesitini anlatan kullanımlarıdır."},{"boundary_match":"partial","distinction":"Odak dal zamansal niceliği korur. Komşu dal zamanı, olayın kendisine veya onun çetinliğine aktaran bir kullanımdır.","focus_only":"Yalnızca zamanın uzunluğunu veya bir devri belirtir.","gloss":"süre ile olay","neighbor_only":"Büyük ya da çetin olayı, olayın yaşandığı kritik günü veya çoğulda olayları anlatır.","neighbor_ref":"root_001700/B003","relation_type":"near_neighbor","shared_zone":"Her iki genişleme de literal gün anlamından hareket eder ve tek bir gündüzü aşabilir."}],"source_phrase_ar":"مدة من الزمان أي مدة كانت (mufradat)؛ اليوم ها هنا بمعنى الدهر (tahdhib)؛ شر أيام دهرها (tahdhib)","source_summary":"Kaynaklar bu kullanımda gün sözünün sabit gündüz süresinden çıkarak herhangi bir zaman dilimini, özel bağlamlarda ise bir devri anlatabildiğini gösterir.","sources":["TA","MU"],"what_is_ar":"اليوم بمعنى مدة من الزمان أي مدة كانت، أو بمعنى الدهر في بعض الاستعمال.","what_is_not_ar":"ليس محصورا في النهار من طلوع الشمس إلى غروبها، ولا هو خصوص الوقائع أو النعم."},"support_links":["sup_2ffe64fb429baf2af6ba"]},{"boundary":"Dal, büyük veya çetin olayla bağlantılı mecazî ve kalıplaşmış kullanımlarla sınırlıdır; literal zaman süresi ve yalnızca Tanrı'ya bağlanan anma günleri dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_001700/B003","candidate_links":[{"candidate_id":"cand_5c192969d199fe40effc","lane":"micro"},{"candidate_id":"cand_3a5ec2be6facaa151d47","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَوْم","morph_features":"STEM|POS:N|LEM:yawom|ROOT:ywm|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:4:1","qac_word_ref":"90:14:4","surface_ar":"يَوْمٍ"}],"gloss":"büyük olayın yaşandığı çetin gün veya olay","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gün sözü, büyük bir olay gerçekleştiğinde o kritik zamanı veya gerçekleşen olayı anlatmak üzere aktarılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli kalıplarda günün çok çetin, ağır ve etkisi uzun süren bir gün olduğu vurgulanır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çoğul biçim, bilinen günlerde gerçekleşmiş önemli olayları veya tarihî vakaları anlatabilir."}}],"root_ar":"ي و م","root_id":"root_001700","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözün sıradan bir zaman biriminden çok büyük olayın gerçekleşmesini, olayın kendisini ya da çetinliğini öne çıkardığı kullanımlara uygundur.","boundary_detail":"Dal, büyük veya çetin olayla bağlantılı mecazî ve kalıplaşmış kullanımlarla sınırlıdır; literal zaman süresi ve yalnızca Tanrı'ya bağlanan anma günleri dışarıda kalır.","branch_image_ar":"كائنة اليوم وشدته","concept_gloss":"büyük olayın yaşandığı çetin gün veya olay","contextual_glosses":[{"applicability":"Büyük bir olayın meydana geldiği zamanın, olayla özdeşleşmiş bir dönüm noktası olarak anlatıldığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Büyük olayın gerçekleşmesiyle belirlenen kritik zaman özelliğini korur."},"facet_ids":["F001"],"text":"kritik olay anı","usage_role":"contextual"},{"applicability":"Olayın niteliğinden çok, o günün insanlar üzerindeki ağır ve uzayan etkisinin vurgulandığı kalıplarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günün şiddetini ve etkisinin uzamasını belirten özel yüzü korur."},"facet_ids":["F002"],"text":"çok çetin gün","usage_role":"contextual"},{"applicability":"Çoğul biçimin günlerin sürelerini değil, o günlerde gerçekleşmiş bilinen olayları anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çoğul gün biçiminin olaylar toplamına aktarılmasını korur."},"facet_ids":["F003"],"text":"tarihî olaylar","usage_role":"contextual"}],"definition":"Büyük veya çetin bir olayın gerçekleştiği kritik günü ya da olayın kendisini anlatan aktarmalı kullanımdır. Bazı kalıplarda çok ağır bir gün, çoğul biçimde ise yaşanmış önemli olaylar anlamı taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gün sözü, büyük bir olay gerçekleştiğinde o kritik zamanı veya gerçekleşen olayı anlatmak üzere aktarılır."},{"facet_id":"F002","role":"specialization","statement":"Belirli kalıplarda günün çok çetin, ağır ve etkisi uzun süren bir gün olduğu vurgulanır."},{"facet_id":"F003","role":"extension","statement":"Çoğul biçim, bilinen günlerde gerçekleşmiş önemli olayları veya tarihî vakaları anlatabilir."}],"identity_rationale":"Kaynak ifadesi büyük olay, olayın gerçekleşmesi, şiddetli gün ve çoğulda yaşanmış olaylar kullanımlarını aynı dalda toplar. Bu çerçeve kullanılabilir, ancak bunların tek bir yalın anlam değil, gün ile olay arasındaki aktarmaya dayanan bağlı kullanımlar olduğu açıkça belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"büyük olay, olayın gerçekleştiği kritik gün veya çetin gün"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"çok çetin gün veya savaş günü"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bilinen günlerde gerçekleşmiş olaylar"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"çok çetin gün"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kötülüğü insanlar üzerinde uzun süren çetin gün"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kötülüğü insanlar üzerinde uzun süren çetin gün"}],"lexicalization_note":"Olayı anlatan biçimsel genişleme, şiddetli gün bildiren kalıplar ve çoğul olay anlamı ayrı yüzler olarak korunur; kalıp anlamları yalın kullanıma genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; olay, felaket ve şiddet alanındaki en yakın üç aday ile aynı kökün literal gün ve süre dalları sınırı en iyi açıkladığı için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal olayın bir günle ilişkilendirilmesine dayanır. Komşu dal ise olayı ya da felaketi doğrudan adlandırır ve günle kurulmuş bu aktarmayı gerektirmez.","focus_only":"Gün sözünün kritik zamana, çetin güne ve çoğulda olaylara aktarılmasını içerir.","gloss":"olay günü ile sonradan çıkan olay","neighbor_only":"Zaman adından bağımsız olarak sonradan ortaya çıkan olay, felaket ve devrin sıkıntısını doğrudan adlandırır.","neighbor_ref":"root_000299/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir devrin önemli, ağır veya beklenmedik olayını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalda şiddet bir güne yüklenebilir ve olay-zaman bağı kurucudur. Komşu dalın çekirdeği ise gün kavramından bağımsız felaket ve sıkıntıdır.","focus_only":"Kritik gün, büyük olay ve çoğul olaylar arasında gün temelli bir aktarım kurar.","gloss":"çetin gün ile felaket","neighbor_only":"Felaketi, sıkıntıyı ve devrin değişen darbelerini doğrudan anlatır.","neighbor_ref":"root_001378/B006","relation_type":"near_neighbor","shared_zone":"İki dal da insanları etkileyen ağır bir olay veya sıkıntı alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı yönü zaman ile olay arasındaki aktarmadır. Komşu dal olayın kapanmış ve aşırı şiddetli niteliğine odaklanır.","focus_only":"Olayı yaşandığı kritik gün üzerinden anlatır ve çoğulda olaylar anlamına geçebilir.","gloss":"çetin gün ile şiddetli felaket","neighbor_only":"Çıkış yolu bulunmayan şiddetli iş, fitne veya felaketi doğrudan niteler.","neighbor_ref":"root_000884/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da ağır, korkutucu ve insanları zorlayan olayları anlatır."},{"boundary_match":"partial","distinction":"Odak dalda gün, olayın kendisini ya da niteliğini taşır. Komşu dal yalnızca doğal sınırları bulunan zaman aralığıdır.","focus_only":"Günü olayın büyüklüğüne veya çetinliğine aktarır.","gloss":"olay günü ile literal gün","neighbor_only":"Olaydan bağımsız olarak gün doğumu ile gün batımı arasındaki zaman birimini belirtir.","neighbor_ref":"root_001700/B001","relation_type":"near_neighbor","shared_zone":"Kritik olay, literal bir gün içinde gerçekleşebildiği için iki kullanım aynı zaman zeminini paylaşır."},{"boundary_match":"partial","distinction":"Odak dalda belirleyici unsur olaydır; komşu dalda ise yalnızca zamanın uzunluğu veya dönem oluşu korunur.","focus_only":"Büyük olayın gerçekleşmesini, çetinliği veya olaylar toplamını anlatır.","gloss":"olay odaklı gün ile süre","neighbor_only":"Olay niteliği eklemeden herhangi bir zaman dilimini ya da devri belirtir.","neighbor_ref":"root_001700/B002","relation_type":"near_neighbor","shared_zone":"İki dal da literal tek gün sınırını aşan kullanımlardır."}],"source_phrase_ar":"يستعيرونه في الأمر العظيم ويقولون نعم فلان في اليوم إذا نزل (maqayis)؛ اليوم: الكون، الكائنة من الكون إذا نزلت أو حدثت (ayn;tahdhib)؛ الشدة باليوم (sihah)؛ اليوم الشديد: يوم ذو أيام (ayn;tahdhib)؛ الأيام في معنى الوقائع (tahdhib)","source_summary":"Kaynaklar gün sözünün büyük bir olayın gerçekleşmesine aktarılmasını, çetin gün anlatımında kullanılmasını ve çoğul biçimin olayları belirtmesini aynı anlamsal aile içinde verir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه استعارة اليوم للأمر العظيم، والكائنة إذا نزلت، واليوم الشديد، والأيام بمعنى الوقائع.","what_is_not_ar":"لا يدخل فيه اليوم الزمني المحض، ولا خصوص أيام الله من جهة النعم والعذاب، ولا أسماء يام."},"support_links":["sup_9d0b5164baa90d1667b0","sup_b110c9558e06989965d5"]},{"boundary":"Dal yalnızca Tanrı'ya bağlanarak nimet, bağışlama, ceza veya ibret verici olayla anılan günleri kapsar; her önemli ya da çetin gün buraya girmez.","branch_kind":"collocation","branch_ref":"root_001700/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَوْم","morph_features":"STEM|POS:N|LEM:yawom|ROOT:ywm|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:4:1","qac_word_ref":"90:14:4","surface_ar":"يَوْمٍ"}],"gloss":"Tanrı'nın nimet ve ibret verici işleriyle anılan günler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Günler, Tanrı'nın insanlara yönelik etkili ve hatırlanmaya değer işleriyle ilişkilendirilir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anılan işler nimet verme ve bağışlamanın yanı sıra bir topluluğa inen cezayı da kapsayabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Günlerin Tanrı'ya bağlanması, o günlerde verilen nimetler ve gerçekleşen işler nedeniyle onlara özel değer kazandırır."}}],"root_ar":"ي و م","root_id":"root_001700","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Günlerin Tanrı'ya bağlanarak nimet, bağışlama, ceza veya unutulmaması gereken toplumsal olayları hatırlattığı özel ifadeye uygundur.","boundary_detail":"Dal yalnızca Tanrı'ya bağlanarak nimet, bağışlama, ceza veya ibret verici olayla anılan günleri kapsar; her önemli ya da çetin gün buraya girmez.","branch_image_ar":"أيام النعم والوقائع الإلهية","concept_gloss":"Tanrı'nın nimet ve ibret verici işleriyle anılan günler","contextual_glosses":[{"applicability":"Bağlam özellikle verilen nimetleri ve bağışlamayı hatırlatıyorsa kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tanrı'ya bağlanan günlerin nimet ve bağışlama yönünü korur."},"facet_ids":["F001","F002"],"text":"Tanrı'nın nimet günleri","usage_role":"contextual"},{"applicability":"Bağlam geçmiş bir topluluğa inen ceza veya hatırlanması gereken sarsıcı olayı öne çıkarıyorsa uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tanrı'ya bağlanan günlerin ceza ve ibret verici olay yönünü korur."},"facet_ids":["F001","F002"],"text":"Tanrı'nın ibret günleri","usage_role":"contextual"}],"definition":"Tanrı'nın nimet, bağışlama veya cezalandırma gibi unutulmaması gereken etkileriyle anılan günlerdir. Bu bağlama, söz konusu günlerin önemini ve hatırlatıcı değerini yükseltir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Günler, Tanrı'nın insanlara yönelik etkili ve hatırlanmaya değer işleriyle ilişkilendirilir."},{"facet_id":"F002","role":"example","statement":"Anılan işler nimet verme ve bağışlamanın yanı sıra bir topluluğa inen cezayı da kapsayabilir."},{"facet_id":"F003","role":"associated_use","statement":"Günlerin Tanrı'ya bağlanması, o günlerde verilen nimetler ve gerçekleşen işler nedeniyle onlara özel değer kazandırır."}],"identity_rationale":"Kaynak ifadesi, Tanrı'ya bağlanan günleri insanlara hatırlatılan nimet, bağışlama, ceza ve toplumsal olaylarla açıklar; bu bağlamanın günlere özel değer kazandırdığını da belirtir. Verilen dal çerçevesi bu sınırlı ifadeyi doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"Tanrı'nın nimet, bağışlama ve cezalandırma olaylarıyla anılan günleri"}],"lexicalization_note":"Anlam yalnızca Tanrı'ya bağlanan günler ifadesine aittir; nimet, ceza ve anma içeriği yalın gün sözüne genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca olay günü, literal gün ve belirsiz süre dalları okuyucu açısından gerçek sınır karşılaştırması sunduğu için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir Tanrı'ya bağlama ifadesiyle sınırlıdır ve nimet ile cezayı anma amacı taşır. Komşu dal genel olay ve çetinlik aktarımıdır.","focus_only":"Günleri Tanrı'nın nimeti, bağışlaması veya cezasıyla ilişkilendirir ve hatırlatıcı değer taşır.","gloss":"ilahi anma günleri ile olay günleri","neighbor_only":"Herhangi bir büyük veya çetin olayı, kritik günü ya da çoğulda olayları Tanrı'ya bağlama şartı olmadan anlatır.","neighbor_ref":"root_001700/B003","relation_type":"near_neighbor","shared_zone":"İki dal da önemli veya sarsıcı olayların gerçekleştiği günleri olay üzerinden anlamlandırır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği özel bağlama ve hatırlatılan ilahi iştir; komşu dal yalnızca gündüz süresidir.","focus_only":"Günü Tanrı'nın hatırlanmaya değer işi ve verdiği özel değer üzerinden niteler.","gloss":"anma günü ile literal gün","neighbor_only":"Herhangi bir olay veya değer yüklemeden gün doğumu ile gün batımı arasındaki zaman birimini belirtir.","neighbor_ref":"root_001700/B001","relation_type":"near_neighbor","shared_zone":"Anılan olayların gerçekleştiği günler literal zaman birimlerinden oluşur."},{"boundary_match":"thematic_only","distinction":"Odak dal olay ve kutsal bağlama dayalı özel bir ifadedir; komşu dal nötr bir süre veya devir anlamıdır ve anlamsal çekirdekleri örtüşmez.","focus_only":"Tanrı'ya bağlanan, nimet veya ceza olaylarıyla anılan günleri belirtir.","gloss":"anılan günler ile süre","neighbor_only":"Herhangi bir olay veya ilahi bağ kurmadan uzunluğu belirsiz süreyi ya da devri belirtir.","neighbor_ref":"root_001700/B002","relation_type":"thematic","shared_zone":"Her iki dal da gün sözünden hareketle tek bir literal gündüzü aşan zaman anlatımlarına katılır."}],"source_phrase_ar":"وذكرهم بأيام الله: بما نزل بعاد وثمود وغيرهم من العذاب، وبالعفو عن آخرين (tahdhib)؛ جاءت الأيام بمعنى الوقائع والنعم (tahdhib)؛ أيامه: نعمه (tahdhib)؛ إضافة الأيام إلى الله تشريف لأمرها لما أفاض الله عليهم من نعمه فيها (mufradat)","source_summary":"Kaynaklar, Tanrı'ya bağlanan günlerin nimetleri ve önemli işleri hatırlattığını; bu işlerin bağışlama kadar cezayı da içerebildiğini ve bağlamanın günleri yücelttiğini gösterir.","sources":["TA","MU"],"what_is_ar":"يدخل فيه أيام الله وما في معناها من أيام النعم والوقائع التي يذكر بها، من عفو أو نعمة أو عذاب نزل بقوم.","what_is_not_ar":"ليس كل جمع أيام، ولا كل يوم شديد، ولا مجرد مدة زمانية."},"support_links":[]},{"boundary":"Bu dal bağımsız bir gün anlamı değil, bağlamda daha önce veya sonra belirlenen güne gönderme yapan birleşik yapıdır.","branch_kind":"non_bare","branch_ref":"root_001700/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَوْم","morph_features":"STEM|POS:N|LEM:yawom|ROOT:ywm|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:4:1","qac_word_ref":"90:14:4","surface_ar":"يَوْمٍ"}],"gloss":"bağlamda işaret edilen o gün veya o sırada","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birleşik yapı, hangi gün olduğu bağlamdan belirlenen zamana gönderme yapar."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yapı, birleşmenin dilbilgisel değerlendirilmesine göre çekimli veya değişmez biçimde gerçekleşebilir."}}],"root_ar":"ي و م","root_id":"root_001700","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Konuşma veya metin bağlamının belirli bir günü önceden ya da sonradan tanımladığı ve birleşik yapının o zamana gönderme yaptığı kullanımlara uygundur.","boundary_detail":"Bu dal bağımsız bir gün anlamı değil, bağlamda daha önce veya sonra belirlenen güne gönderme yapan birleşik yapıdır.","branch_image_ar":"يوم مضاف إلى إذ","concept_gloss":"bağlamda işaret edilen o gün veya o sırada","contextual_glosses":[{"applicability":"Bağlamın belirli bir takvim gününü veya olay gününü açıkça belirlediği cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlamda belirlenen tek bir güne geriye veya ileriye dönük gönderimi korur."},"facet_ids":["F001"],"text":"o gün","usage_role":"contextual"},{"applicability":"Gönderimin takvim gününden çok anlatılan olayın gerçekleştiği zamana yöneldiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlamda işaret edilen zamana gönderim işlevini korur."},"facet_ids":["F001"],"text":"o sırada","usage_role":"contextual"}],"definition":"Gün sözü bağlamda işaret edilen zamana gönderme yapan bir belirteçle birleşir ve o gün veya o sırada anlamını verir. Birleşik yapı, kuruluşuna göre çekimli ya da değişmez biçimde kullanılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birleşik yapı, hangi gün olduğu bağlamdan belirlenen zamana gönderme yapar."},{"facet_id":"F002","role":"associated_use","statement":"Yapı, birleşmenin dilbilgisel değerlendirilmesine göre çekimli veya değişmez biçimde gerçekleşebilir."}],"identity_rationale":"Kaynak ifadesi gün sözünün bağlamda işaret edilen zamanı gösteren bir belirteçle birleştiğini, ortaya çıkan yapının o gün anlamına geldiğini ve yapıya göre çekimli ya da değişmez olabildiğini belirtir. Dal çerçevesi bu dilbilgisel ve gönderimsel yapıyı doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"o gün; o sırada"}],"lexicalization_note":"Anlam yalnızca gün ile bağlama işaret eden belirtecin birleşik yapısına aittir; yalın gün sözüne yeni bir kök anlamı olarak aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bağlama bağlı yapıyla doğrudan karşılaştırılabilen literal gün ve belirsiz süre dalları dışında yararlı bir anlamsal komşu bulunmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bağlama bağımlı ve dilbilgisel olarak birleşik bir gösterimdir. Komşu dal ise bağlamdan bağımsız temel zaman birimidir.","focus_only":"Hangi günün kastedildiğini bağlamdan alan birleşik bir gönderim yapısıdır.","gloss":"o gün yapısı ile literal gün","neighbor_only":"Gün doğumu ile gün batımı arasındaki zaman birimini kendi başına tanımlar.","neighbor_ref":"root_001700/B001","relation_type":"near_neighbor","shared_zone":"Birleşik yapı, gönderimde bulunduğu zamanı literal gün kavramı üzerinden kurar."},{"boundary_match":"thematic_only","distinction":"Odak dalın görevi belirli bir zamana işaret etmektir; komşu dal ise zamanın süresini belirsiz bırakır ve gönderim yapısı kurmaz.","focus_only":"Bağlamın belirlediği tek bir güne veya ana gönderme yapar.","gloss":"işaret edilen gün ile belirsiz süre","neighbor_only":"Uzunluğu belirsiz herhangi bir zaman dilimini ve bağlama göre bir devri anlatır.","neighbor_ref":"root_001700/B002","relation_type":"thematic","shared_zone":"İki dal da bağlamın zaman yorumunu belirlemesine izin veren gün temelli anlatımlardır."}],"source_phrase_ar":"يركب يوم مع إذ، فيقال: يومئذ؛ وربما يعرب ويبنى، وإذا بني فللإضافة إلى إذ (mufradat)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak, gün sözünün işaret belirteciyle birleşmesini ve bu yapının çekimli ya da değişmez kullanılabilmesini birlikte kaydeder."}],"source_summary":"Dal, bağımsız bir kök anlamından çok bağlamca belirlenen güne gönderme yapan birleşik bir zaman gösterimidir.","sources":["MU"],"what_is_ar":"تركيب يوم مع إذ في يومئذ للدلالة على وقت مشار إليه في السياق، مع جواز الإعراب أو البناء بحسب الإضافة.","what_is_not_ar":"ليس أصلا دلاليا جديدا لليوم، ولا أسماء يام، ولا اليوم الشديد."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["90:14:1"],"branch_refs":[],"candidate_id":"cand_466c6dda3cbfb6a5868a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:1:deed-before-cost","source_type":"word_analysis","support_ids":["sup_681062493106ff96d859","sup_e6630199c4b55f55e708"],"title":"deed installed before circumstance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:1","qac_refs":["90:14:1:1"],"status":"accepted"}},{"anchor_refs":["90:14:1"],"branch_refs":[],"candidate_id":"cand_c400334b6d739f9e0e64","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:1:dependent-continuation","source_type":"word_analysis","support_ids":["sup_681062493106ff96d859","sup_76257d8d1b1cac32d99f"],"title":"dependent continuation across the ayah boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:1","qac_refs":["90:14:1:1"],"status":"accepted"}},{"anchor_refs":["90:14:1"],"branch_refs":[],"candidate_id":"cand_9bda907be92eb915e121","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:1:nonexclusive-alternative","source_type":"word_analysis","support_ids":["sup_681062493106ff96d859","sup_f3a53855db715026f326"],"title":"alternative of kinds, not exclusion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:1","qac_refs":["90:14:1:1"],"status":"accepted"}},{"anchor_refs":["90:14:1"],"branch_refs":[],"candidate_id":"cand_c7a9810abadf7ccaf3b5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:1:parallel-nominal-deed","source_type":"word_analysis","support_ids":["sup_681062493106ff96d859","sup_6c69916fa72bdb35b862"],"title":"parallel nominal deed rather than finite-clause shift","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:1","qac_refs":["90:14:1:1"],"status":"accepted"}},{"anchor_refs":["90:14:2"],"branch_refs":[],"candidate_id":"cand_9bd34fedaa671c6d9199","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"90:14:2:body-rescue-boundary","source_type":"word_analysis","support_ids":["sup_0261e37ea13fc07716e5","sup_406a778a14dd403f6774"],"title":"from bodily liberation to bodily nourishment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:2","qac_refs":["90:14:2:1"],"status":"accepted"}},{"anchor_refs":["90:14:2"],"branch_refs":[],"candidate_id":"cand_ec7bd509510874f4bdbb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"90:14:2:delayed-recipient","source_type":"word_analysis","support_ids":["sup_406a778a14dd403f6774","sup_b23c7eae5f2f80a77a8c"],"title":"recipient withheld until the next ayahs","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:2","qac_refs":["90:14:2:1"],"status":"accepted"}},{"anchor_refs":["90:14:2"],"branch_refs":[],"candidate_id":"cand_acaf0e98a0a67bb1bbac","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"90:14:2:famine-time-cost","source_type":"word_analysis","support_ids":["sup_23c02b6c67dcb161f1d4","sup_406a778a14dd403f6774"],"title":"feeding tested by scarcity-time","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:2","qac_refs":["90:14:2:1"],"status":"accepted"}},{"anchor_refs":["90:14:2"],"branch_refs":[],"candidate_id":"cand_4191a632dd3204c8bc87","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"90:14:2:form-iv-provision","source_type":"word_analysis","support_ids":["sup_406a778a14dd403f6774","sup_4cdb769a1810cdea36b5"],"title":"causing another to eat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:2","qac_refs":["90:14:2:1"],"status":"accepted"}},{"anchor_refs":["90:14:2"],"branch_refs":[],"candidate_id":"cand_f23503346c37b51bc370","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"90:14:2:interayah-feeding-echoes","source_type":"word_analysis","support_ids":["sup_406a778a14dd403f6774","sup_c8bc66647a39137f0be9"],"title":"feeding echoes intensified by local famine","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:2","qac_refs":["90:14:2:1"],"status":"accepted"}},{"anchor_refs":["90:14:2"],"branch_refs":[],"candidate_id":"cand_917651b332267acd19f5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"90:14:2:material-food-pressure","source_type":"word_analysis","support_ids":["sup_406a778a14dd403f6774","sup_73a972e64b154e0366d0"],"title":"material food field made outward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:2","qac_refs":["90:14:2:1"],"status":"accepted"}},{"anchor_refs":["90:14:2"],"branch_refs":[],"candidate_id":"cand_5f0c9ead6ad579f5d52c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"90:14:2:nominal-deed-category","source_type":"word_analysis","support_ids":["sup_406a778a14dd403f6774","sup_f06e2b12e43e5a53b2ce"],"title":"indefinite nominal deed-category","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:2","qac_refs":["90:14:2:1"],"status":"accepted"}},{"anchor_refs":["90:14:2"],"branch_refs":[],"candidate_id":"cand_2d9aa4f1c55423c04f0c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"90:14:2:rare-duty-register","source_type":"word_analysis","support_ids":["sup_406a778a14dd403f6774","sup_bcd7ace7eac45151fba3"],"title":"rare verbal-noun register in structured duty contexts","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:2","qac_refs":["90:14:2:1"],"status":"accepted"}},{"anchor_refs":["90:14:2"],"branch_refs":[],"candidate_id":"cand_6a77e379cfd158f68a29","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"90:14:2:role-reversal-and-transfer","source_type":"word_analysis","support_ids":["sup_406a778a14dd403f6774","sup_afd88e1ee9b093a6a088"],"title":"supplier role before needy recipients appear","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:2","qac_refs":["90:14:2:1"],"status":"accepted"}},{"anchor_refs":["90:14:2"],"branch_refs":[],"candidate_id":"cand_1f5f3e9997b58ae7f040","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"90:14:2:sequence-sound-body","source_type":"word_analysis","support_ids":["sup_406a778a14dd403f6774","sup_c11768d6114bafd9f6b5"],"title":"act beat, cadence, and embodied sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:2","qac_refs":["90:14:2:1"],"status":"accepted"}},{"anchor_refs":["90:14:2"],"branch_refs":[],"candidate_id":"cand_be06d7dbba507b7b9955","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"90:14:2:variant-agency","source_type":"word_analysis","support_ids":["sup_0f6c7f3b8ee88aa90b30","sup_406a778a14dd403f6774"],"title":"accepted variant shifts posture to performed feeding","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:2","qac_refs":["90:14:2:1"],"status":"accepted"}},{"anchor_refs":["90:14:3"],"branch_refs":[],"candidate_id":"cand_9784890a1c3cdeec0963","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:3:beat-pivot","source_type":"word_analysis","support_ids":["sup_80ba7c9a9c5c183af320","sup_89aeae9610e910c29548"],"title":"short pivot from deed to setting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:3","qac_refs":["90:14:3:1"],"status":"accepted"}},{"anchor_refs":["90:14:3"],"branch_refs":[],"candidate_id":"cand_fe49b1eb7b9bfb9c4a44","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:3:scope-over-feeding","source_type":"word_analysis","support_ids":["sup_789fa7993049f03a873b","sup_89aeae9610e910c29548"],"title":"scarcity phrase scopes over the act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:3","qac_refs":["90:14:3:1"],"status":"accepted"}},{"anchor_refs":["90:14:3"],"branch_refs":[],"candidate_id":"cand_e6f3a1953e1eb88401d7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:3:temporal-circumstantial-double-value","source_type":"word_analysis","support_ids":["sup_1f75cafc759f9411b2b4","sup_89aeae9610e910c29548"],"title":"during a day and within a condition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:3","qac_refs":["90:14:3:1"],"status":"accepted"}},{"anchor_refs":["90:14:3"],"branch_refs":[],"candidate_id":"cand_0d26b0f74c663b67fe53","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:3:temporal-containment","source_type":"word_analysis","support_ids":["sup_89aeae9610e910c29548","sup_97565bf03822b13f4dae"],"title":"day governed as temporal container","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:3","qac_refs":["90:14:3:1"],"status":"accepted"}},{"anchor_refs":["90:14:4"],"branch_refs":[],"candidate_id":"cand_e299bfcd46e2ea842963","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"90:14:4:boundary-expansion-to-event-time","source_type":"word_analysis","support_ids":["sup_a7ea427aa66bbb3597c4","sup_ccfb4c165d0582f3087e"],"title":"from bare act to occasion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:4","qac_refs":["90:14:4:1"],"status":"accepted"}},{"anchor_refs":["90:14:4"],"branch_refs":[],"candidate_id":"cand_e303de405308bedbf6a7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"90:14:4:collocated-time-host","source_type":"word_analysis","support_ids":["sup_c9119c79803815e078a2","sup_ccfb4c165d0582f3087e"],"title":"time paired with feeding and possession","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:4","qac_refs":["90:14:4:1"],"status":"accepted"}},{"anchor_refs":["90:14:4"],"branch_refs":[],"candidate_id":"cand_9a6e758df9662c968d36","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"90:14:4:delayed-scarcity-cadence","source_type":"word_analysis","support_ids":["sup_8481f18c5d67181f7548","sup_ccfb4c165d0582f3087e"],"title":"day delays the scarcity landing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:4","qac_refs":["90:14:4:1"],"status":"accepted"}},{"anchor_refs":["90:14:4"],"branch_refs":[],"candidate_id":"cand_28946fab63dc1a824b08","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"90:14:4:evaluative-day-field","source_type":"word_analysis","support_ids":["sup_ccfb4c165d0582f3087e","sup_ea374210e25da30f80dc"],"title":"evaluative day field localized to famine","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:4","qac_refs":["90:14:4:1"],"status":"accepted"}},{"anchor_refs":["90:14:4"],"branch_refs":[],"candidate_id":"cand_e83c6bbbe98e6182542f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"90:14:4:event-time-not-mere-date","source_type":"word_analysis","support_ids":["sup_ccfb4c165d0582f3087e","sup_d2bb6f3b015baa74a99d"],"title":"event-time rather than mere daylight span","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:4","qac_refs":["90:14:4:1"],"status":"accepted"}},{"anchor_refs":["90:14:4"],"branch_refs":[],"candidate_id":"cand_6638643e231afd52f66e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"90:14:4:indefinite-crisis-day","source_type":"word_analysis","support_ids":["sup_4c6f389ab3ed050370ff","sup_ccfb4c165d0582f3087e"],"title":"indefinite type of crisis-day","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:4","qac_refs":["90:14:4:1"],"status":"accepted"}},{"anchor_refs":["90:14:4"],"branch_refs":[],"candidate_id":"cand_83940489906fff5f190f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"90:14:4:mediated-characterization","source_type":"word_analysis","support_ids":["sup_0a848971a962ed83171f","sup_ccfb4c165d0582f3087e"],"title":"day characterized through possession phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:4","qac_refs":["90:14:4:1"],"status":"accepted"}},{"anchor_refs":["90:14:4"],"branch_refs":[],"candidate_id":"cand_56aa6855f7e8e420f060","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"90:14:4:singular-concentrated-interval","source_type":"word_analysis","support_ids":["sup_0aede42a0932f4764e18","sup_ccfb4c165d0582f3087e"],"title":"singular interval concentrates the demand","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:4","qac_refs":["90:14:4:1"],"status":"accepted"}},{"anchor_refs":["90:14:5"],"branch_refs":[],"candidate_id":"cand_d4937edfc93bbc12c5d8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:5:case-variant","source_type":"word_analysis","support_ids":["sup_0ac33b45ab71d12b5197","sup_7cbcce1acfd9a79b29ba"],"title":"variant shifts case posture but keeps attachment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:5","qac_refs":["90:14:5:1"],"status":"accepted"}},{"anchor_refs":["90:14:5"],"branch_refs":[],"candidate_id":"cand_2650ee0aec19d72c2cbd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:5:characterization-not-ownership","source_type":"word_analysis","support_ids":["sup_734954cbfc9e0d76b6c6","sup_7cbcce1acfd9a79b29ba"],"title":"possession as characterization","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:5","qac_refs":["90:14:5:1"],"status":"accepted"}},{"anchor_refs":["90:14:5"],"branch_refs":[],"candidate_id":"cand_48772be6c11d237b6aa1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:5:charity-possession-shift","source_type":"word_analysis","support_ids":["sup_7cbcce1acfd9a79b29ba","sup_f9de1f0648c7bd0ad549"],"title":"possession-language shifts from recipients to time","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:5","qac_refs":["90:14:5:1"],"status":"accepted"}},{"anchor_refs":["90:14:5"],"branch_refs":[],"candidate_id":"cand_51f1f0a30b1b15d34f35","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:5:essence-pressure-limited","source_type":"word_analysis","support_ids":["sup_7cbcce1acfd9a79b29ba","sup_a15c1642ba69a550ba6a"],"title":"identity-like pressure within construct bounds","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:5","qac_refs":["90:14:5:1"],"status":"accepted"}},{"anchor_refs":["90:14:5"],"branch_refs":[],"candidate_id":"cand_189b32dc1c4b10583733","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:5:forward-possessive-skeleton","source_type":"word_analysis","support_ids":["sup_3f860a00340f889b49fb","sup_7cbcce1acfd9a79b29ba"],"title":"possessive skeleton carries into recipient descriptions","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:5","qac_refs":["90:14:5:1"],"status":"accepted"}},{"anchor_refs":["90:14:5"],"branch_refs":[],"candidate_id":"cand_599ff9af21e468018d01","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:5:hinge-and-cadence","source_type":"word_analysis","support_ids":["sup_7cbcce1acfd9a79b29ba","sup_93af703aa190192a8771"],"title":"hinge from time noun to scarcity noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:5","qac_refs":["90:14:5:1"],"status":"accepted"}},{"anchor_refs":["90:14:5"],"branch_refs":[],"candidate_id":"cand_c2b7f24fd2a7028ca863","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:14:5:possessive-construct","source_type":"word_analysis","support_ids":["sup_60ce2b3351f50194906c","sup_7cbcce1acfd9a79b29ba"],"title":"possessive construct attaches scarcity to the day","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:5","qac_refs":["90:14:5:1"],"status":"accepted"}},{"anchor_refs":["90:14:6"],"branch_refs":[],"candidate_id":"cand_3ac536425f75082906ff","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000710"],"scope":"focus_ayah","source_local_id":"90:14:6:ambient-scarcity-before-recipient","source_type":"word_analysis","support_ids":["sup_74e088e6f8470538e7c6","sup_c21a14187e3f3986141a"],"title":"ambient scarcity before named recipient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:6","qac_refs":["90:14:6:1"],"status":"accepted"}},{"anchor_refs":["90:14:6"],"branch_refs":[],"candidate_id":"cand_bddda37067699af38fc6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000710"],"scope":"focus_ayah","source_local_id":"90:14:6:boundary-body-rescue","source_type":"word_analysis","support_ids":["sup_7f0e783561c4f9115305","sup_c21a14187e3f3986141a"],"title":"from bodily constraint to bodily deprivation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:6","qac_refs":["90:14:6:1"],"status":"accepted"}},{"anchor_refs":["90:14:6"],"branch_refs":[],"candidate_id":"cand_b17db9ed1b8810818a27","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000710"],"scope":"focus_ayah","source_local_id":"90:14:6:contrast-with-hunger-formula","source_type":"word_analysis","support_ids":["sup_80bde38441590e6cd1ec","sup_c21a14187e3f3986141a"],"title":"rarer famine term contrasted with divine feeding formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:6","qac_refs":["90:14:6:1"],"status":"accepted"}},{"anchor_refs":["90:14:6"],"branch_refs":[],"candidate_id":"cand_203ca826cf10ee1256b4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000710"],"scope":"focus_ayah","source_local_id":"90:14:6:convergent-final-crisis-state","source_type":"word_analysis","support_ids":["sup_b77b9bdef22d747f4e54","sup_c21a14187e3f3986141a"],"title":"hapax rarity, bodily hunger, and sound converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:6","qac_refs":["90:14:6:1"],"status":"accepted"}},{"anchor_refs":["90:14:6"],"branch_refs":[],"candidate_id":"cand_454457915b7f3d9cbfff","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000710"],"scope":"focus_ayah","source_local_id":"90:14:6:delayed-final-revelation","source_type":"word_analysis","support_ids":["sup_c21a14187e3f3986141a","sup_dff7695c7dc31c847d15"],"title":"scarcity delayed to ayah closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:6","qac_refs":["90:14:6:1"],"status":"accepted"}},{"anchor_refs":["90:14:6"],"branch_refs":[],"candidate_id":"cand_ce82e89097ff539541a2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000710"],"scope":"focus_ayah","source_local_id":"90:14:6:genitive-scarcity-complement","source_type":"word_analysis","support_ids":["sup_4bba047cd3b0f2d3717f","sup_c21a14187e3f3986141a"],"title":"scarcity possessed by the day","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:6","qac_refs":["90:14:6:1"],"status":"accepted"}},{"anchor_refs":["90:14:6"],"branch_refs":[],"candidate_id":"cand_1524a59fff9ab018b43f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000710"],"scope":"focus_ayah","source_local_id":"90:14:6:indefinite-state-condition","source_type":"word_analysis","support_ids":["sup_c21a14187e3f3986141a","sup_d3e1321d2f81c20bd9cb"],"title":"indefinite state rather than known famine event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:6","qac_refs":["90:14:6:1"],"status":"accepted"}},{"anchor_refs":["90:14:6"],"branch_refs":[],"candidate_id":"cand_7b5fc42c3dc3c372297c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000710"],"scope":"focus_ayah","source_local_id":"90:14:6:layered-personal-social-crisis","source_type":"word_analysis","support_ids":["sup_a799923f72dea9e38a47","sup_c21a14187e3f3986141a"],"title":"personal hunger expands into social crisis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:6","qac_refs":["90:14:6:1"],"status":"accepted"}},{"anchor_refs":["90:14:6"],"branch_refs":[],"candidate_id":"cand_5945f5c58cae41c13478","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000710"],"scope":"focus_ayah","source_local_id":"90:14:6:provision-against-famine","source_type":"word_analysis","support_ids":["sup_65568d2d854bc7b5e3f3","sup_c21a14187e3f3986141a"],"title":"feeding answers exactly the famine condition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:6","qac_refs":["90:14:6:1"],"status":"accepted"}},{"anchor_refs":["90:14:6"],"branch_refs":[],"candidate_id":"cand_127ba4299cf15bd6fcdc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000710"],"scope":"focus_ayah","source_local_id":"90:14:6:rare-final-word","source_type":"word_analysis","support_ids":["sup_c21a14187e3f3986141a","sup_d3cbbe69157294783e6f"],"title":"rare famine word bears final load","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:6","qac_refs":["90:14:6:1"],"status":"accepted"}},{"anchor_refs":["90:14:6"],"branch_refs":[],"candidate_id":"cand_14f0277019b0022796f3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000710"],"scope":"focus_ayah","source_local_id":"90:14:6:severe-hunger-not-appetite","source_type":"word_analysis","support_ids":["sup_acd65de21da5b845a9fe","sup_c21a14187e3f3986141a"],"title":"severe hunger and bodily weakening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:6","qac_refs":["90:14:6:1"],"status":"accepted"}},{"anchor_refs":["90:14:6"],"branch_refs":[],"candidate_id":"cand_9b44c6857ac60cd52460","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000710"],"scope":"focus_ayah","source_local_id":"90:14:6:sound-and-indefinite-chain","source_type":"word_analysis","support_ids":["sup_982299a4821e887775e4","sup_c21a14187e3f3986141a"],"title":"heavy closure and indefinite cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:6","qac_refs":["90:14:6:1"],"status":"accepted"}},{"anchor_refs":["90:14:6"],"branch_refs":[],"candidate_id":"cand_fda5f123cd3a80ccb549","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000710"],"scope":"focus_ayah","source_local_id":"90:14:6:state-locus-environment","source_type":"word_analysis","support_ids":["sup_0d4730a87899a221dad3","sup_c21a14187e3f3986141a"],"title":"hunger as inhabitable crisis environment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:14:6","qac_refs":["90:14:6:1"],"status":"accepted"}},{"anchor_refs":["90:14:2"],"branch_refs":[],"candidate_id":"cand_a815deeb79ffbad8ce4f","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"90:14:2:1","source_type":"qac_morpheme","support_ids":["sup_ce80fdfbd8ca07bd752a"],"title":"QAC root occurrence: ط ع م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:14:4"],"branch_refs":[],"candidate_id":"cand_670341a3ad3f24479e4a","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001700"],"scope":"focus_ayah","source_local_id":"90:14:4:1","source_type":"qac_morpheme","support_ids":["sup_eac2f9b28edb3dd951ab"],"title":"QAC root occurrence: ي و م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:14:6"],"branch_refs":[],"candidate_id":"cand_77d5d087cfe53ec2472e","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000710"],"scope":"focus_ayah","source_local_id":"90:14:6:1","source_type":"qac_morpheme","support_ids":["sup_c2a785ea2fb97ee034d9"],"title":"QAC root occurrence: س غ ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:14"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:14","branch_refs":["root_000710/B001","root_000934/B002","root_001700/B003"],"candidate_id":"cand_5c192969d199fe40effc","commentary_obligation":"review","hft_ref":"hft_1be7752841505dccf310","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:B01_CRISIS_TRANSFER","source_type":"hft","support_ids":["sup_b110c9558e06989965d5"],"title":"B01_CRISIS_TRANSFER","trust":"legacy_unbound"},{"anchor_refs":["90:14"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:14","branch_refs":["root_000710/B001","root_000934/B004","root_001700/B002"],"candidate_id":"cand_edda19c25e4e912dccb4","commentary_obligation":"review","hft_ref":"hft_2bbb84f992b04714db96","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:B02_FAMINE_MAINTENANCE","source_type":"hft","support_ids":["sup_2ffe64fb429baf2af6ba"],"title":"B02_FAMINE_MAINTENANCE","trust":"legacy_unbound"},{"anchor_refs":["90:14"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:14","branch_refs":["root_000710/B001","root_000934/B001","root_000934/B011"],"candidate_id":"cand_05c3e0aa40dccce35b30","commentary_obligation":"review","hft_ref":"hft_d7d26a3379644a0a3c33","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:B03_CAPACITY_RESTORATION","source_type":"hft","support_ids":["sup_c0b563797e6464b0e9a6"],"title":"B03_CAPACITY_RESTORATION","trust":"legacy_unbound"},{"anchor_refs":["90:14"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:14","branch_refs":["root_000710/B001","root_000934/B010","root_001700/B003"],"candidate_id":"cand_3a5ec2be6facaa151d47","commentary_obligation":"review","hft_ref":"hft_a3382815bf4f1843319d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:B04_SUPPORT_THAT_TAKES","source_type":"hft","support_ids":["sup_9d0b5164baa90d1667b0"],"title":"B04_SUPPORT_THAT_TAKES","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ","qac_morphemes":[{"lemma_ar":"أَو","morph_features":"STEM|POS:CONJ|LEM:>aw","morpheme_role":"STEM","pos":"CONJ","qac_ref":"90:14:1:1","qac_word_ref":"90:14:1","root_ar":"","surface_ar":"أَوْ"},{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","root_ar":"ط ع م","surface_ar":"إِطْعَٰمٌ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"90:14:3:1","qac_word_ref":"90:14:3","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"يَوْم","morph_features":"STEM|POS:N|LEM:yawom|ROOT:ywm|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:4:1","qac_word_ref":"90:14:4","root_ar":"ي و م","surface_ar":"يَوْمٍ"},{"lemma_ar":"ذُو","morph_features":"STEM|POS:N|LEM:*uw|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:5:1","qac_word_ref":"90:14:5","root_ar":"","surface_ar":"ذِى"},{"lemma_ar":"مَسْغَبَة","morph_features":"STEM|POS:N|LEM:masogabap|ROOT:sgb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:6:1","qac_word_ref":"90:14:6","root_ar":"س غ ب","surface_ar":"مَسْغَبَةٍ"}],"word_analysis_qac_refs":[["90:14:1:1"],["90:14:2:1"],["90:14:3:1"],["90:14:4:1"],["90:14:5:1"],["90:14:6:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["90:14:1","90:14:2","90:14:3","90:14:4","90:14:5","90:14:6"]},"focus_surface_evidence":{"arabic_uthmani":"أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ","qac_morphemes":[{"lemma_ar":"أَو","morph_features":"STEM|POS:CONJ|LEM:>aw","morpheme_role":"STEM","pos":"CONJ","qac_ref":"90:14:1:1","qac_word_ref":"90:14:1","root_ar":"","surface_ar":"أَوْ"},{"lemma_ar":"إِطْعَٰم","morph_features":"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:2:1","qac_word_ref":"90:14:2","root_ar":"ط ع م","surface_ar":"إِطْعَٰمٌ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"90:14:3:1","qac_word_ref":"90:14:3","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"يَوْم","morph_features":"STEM|POS:N|LEM:yawom|ROOT:ywm|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:4:1","qac_word_ref":"90:14:4","root_ar":"ي و م","surface_ar":"يَوْمٍ"},{"lemma_ar":"ذُو","morph_features":"STEM|POS:N|LEM:*uw|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:5:1","qac_word_ref":"90:14:5","root_ar":"","surface_ar":"ذِى"},{"lemma_ar":"مَسْغَبَة","morph_features":"STEM|POS:N|LEM:masogabap|ROOT:sgb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:14:6:1","qac_word_ref":"90:14:6","root_ar":"س غ ب","surface_ar":"مَسْغَبَةٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["90:14:1:1"],["90:14:2:1"],["90:14:3:1"],["90:14:4:1"],["90:14:5:1"],["90:14:6:1"]],"word_analysis_refs":["90:14:1","90:14:2","90:14:3","90:14:4","90:14:5","90:14:6"],"word_rows":[{"analysis_record_ref":"90:14:1","analytic_gloss_range_en":"coordinating alternative particle that carries the prior ascent-definition forward and introduces a parallel nominal deed","analytic_root_gloss_range_en":null,"qac_refs":["90:14:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"أَوْ","transliteration":"aw"}},{"analysis_record_ref":"90:14:2","analytic_gloss_range_en":"indefinite Form IV verbal noun naming the deed-category of causing another to eat, with the recipient delayed and the famine-time setting making the act costly","analytic_root_gloss_range_en":"taste, eating, food, causing to eat, provision, edible share, livelihood, and construction-bound extensions; the local Form IV verbal noun selects outward provisioning","qac_refs":["90:14:2:1"],"root":{"arabic":"ط ع م","transliteration":"ṭ-ʿ-m"},"surface":{"arabic":"إِطْعَٰمٌۭ","transliteration":"iṭʿāmun"}},{"analysis_record_ref":"90:14:3","analytic_gloss_range_en":"preposition of temporal and circumstantial containment governing the day phrase as the setting inside which feeding is evaluated","analytic_root_gloss_range_en":null,"qac_refs":["90:14:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فِى","transliteration":"fī"}},{"analysis_record_ref":"90:14:4","analytic_gloss_range_en":"indefinite singular crisis-day or event-time governed by the preposition and characterized by the following scarcity possession phrase","analytic_root_gloss_range_en":"day, daylight span, period, occasion, event-time, and marked evaluative day; local grammar selects an indefinite scarcity-marked interval","qac_refs":["90:14:4:1"],"root":{"arabic":"ي و م","transliteration":"y-w-m"},"surface":{"arabic":"يَوْمٍۢ","transliteration":"yawmin"}},{"analysis_record_ref":"90:14:5","analytic_gloss_range_en":"genitive five-noun possessive adjective meaning possessed of or characterized by, modifying the day and governing the scarcity complement","analytic_root_gloss_range_en":"possessor, one characterized by a following noun, bearer of an attribute, and related demonstrative or essence-family branches; local five-noun construct selects attributed possession","qac_refs":["90:14:5:1"],"root":{"arabic":"ذ و و","transliteration":"dh-w-w"},"surface":{"arabic":"ذِى","transliteration":"dhī"}},{"analysis_record_ref":"90:14:6","analytic_gloss_range_en":"indefinite genitive mīm state noun naming severe hunger, famine, or scarcity-condition possessed by the day and closing the ayah as the cost of feeding","analytic_root_gloss_range_en":"hunger, famine, food-scarcity, severe want, and bodily weakening from lack of food; local mīm state noun selects a crisis condition rather than ordinary appetite","qac_refs":["90:14:6:1"],"root":{"arabic":"س غ ب","transliteration":"s-gh-b"},"surface":{"arabic":"مَسْغَبَةٍۢ","transliteration":"masghabatin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["90:14"],"branch_refs":["root_000710/B001","root_000934/B002","root_001700/B003"],"candidate_id":"cand_5c192969d199fe40effc","evidence_scope":"focus_ayah","hft_ref":"hft_1be7752841505dccf310","item_id":"B01_CRISIS_TRANSFER","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:B01_CRISIS_TRANSFER","support_id":"sup_b110c9558e06989965d5"},{"anchor_refs":["90:14"],"branch_refs":["root_000710/B001","root_000934/B004","root_001700/B002"],"candidate_id":"cand_edda19c25e4e912dccb4","evidence_scope":"focus_ayah","hft_ref":"hft_2bbb84f992b04714db96","item_id":"B02_FAMINE_MAINTENANCE","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:B02_FAMINE_MAINTENANCE","support_id":"sup_2ffe64fb429baf2af6ba"},{"anchor_refs":["90:14"],"branch_refs":["root_000710/B001","root_000934/B001","root_000934/B011"],"candidate_id":"cand_05c3e0aa40dccce35b30","evidence_scope":"focus_ayah","hft_ref":"hft_d7d26a3379644a0a3c33","item_id":"B03_CAPACITY_RESTORATION","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:B03_CAPACITY_RESTORATION","support_id":"sup_c0b563797e6464b0e9a6"},{"anchor_refs":["90:14"],"branch_refs":["root_000710/B001","root_000934/B010","root_001700/B003"],"candidate_id":"cand_3a5ec2be6facaa151d47","evidence_scope":"focus_ayah","hft_ref":"hft_a3382815bf4f1843319d","item_id":"B04_SUPPORT_THAT_TAKES","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:B04_SUPPORT_THAT_TAKES","support_id":"sup_9d0b5164baa90d1667b0"}],"diagnostics":[],"lane_counts":{"global":17,"macro":6,"micro":4},"packet_summary":{"ayah_count":20,"focus_ref":"90:14","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ح ل ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000351","furuq_root_norm":"ح ل ل","furuq_source_root_norm":"ح ل ل","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000353","furuq_root_norm":"ح ل ي","furuq_source_root_norm":"ح ل ي","is_dominant":false,"target_occurrences":6,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"90:14","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":17,"unstructured_record_count":0},"identity":{"ayah_ref":"90:14","lane":"micro","linguistic_source_ref":"90:14","surface_ref":"90:14","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"90:14","target_tokens":[["Ya",["90:14:1"]],["da",["90:14:1"]],["açlık",["90:14:6"]],["yaşanan",["90:14:5","90:14:6"]],["bir",["90:14:4"]],["günde",["90:14:3","90:14:4"]],["yemek",["90:14:2"]],["yedirmektir",["90:14:2"]]],"text":"Ya da açlık yaşanan bir günde yemek yedirmektir:"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":11,"ayah_to":20,"id":"s090-p02-011-020","label":"The steep path and the two companies","number":2,"refs":["90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:2:body-rescue-boundary","source_type":"word_analysis","support_id":"sup_0261e37ea13fc07716e5","text":"{\"blocking_evidence\":null,\"headline\":\"from bodily liberation to bodily nourishment\",\"reader_payoff\":\"The reader sees the ascent move from unfastening a constrained body in 90:13 to sustaining a hungry body in 90:14.\",\"reason\":\"The coordinated nominal deeds across 90:13-14 form a concrete rescue pair.\",\"representative_source_ids\":[\"QE-1871797c\",\"QB-8b02a7f2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:4:mediated-characterization","source_type":"word_analysis","support_id":"sup_0a848971a962ed83171f","text":"{\"blocking_evidence\":null,\"headline\":\"day characterized through possession phrase\",\"reader_payoff\":\"The reader sees hunger attached to time through a relation of possession, not collapsed into a bare famine label.\",\"reason\":\"The grammar makes the day the head modified by the five-noun possessive construction and its scarcity complement.\",\"representative_source_ids\":[\"QG-9e1baf6d\",\"QG-bf2c0282\",\"MT-ed2661f9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:5:case-variant","source_type":"word_analysis","support_id":"sup_0ac33b45ab71d12b5197","text":"{\"blocking_evidence\":null,\"headline\":\"variant shifts case posture but keeps attachment\",\"reader_payoff\":\"The reader sees that the variant may make the phrase more circumstantial while still anchoring hunger to the day.\",\"reason\":\"The canonical output follows the genitive local form; the variant is retained as case contrast because it does not move scarcity away from the day.\",\"representative_source_ids\":[\"QG-56a516d9\",\"QG-99dc5568\",\"MF-7eec1c95\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:4:singular-concentrated-interval","source_type":"word_analysis","support_id":"sup_0aede42a0932f4764e18","text":"{\"blocking_evidence\":null,\"headline\":\"singular interval concentrates the demand\",\"reader_payoff\":\"The reader notices that the demand can fall within a single crisis interval, without waiting for a broader season.\",\"reason\":\"The local form is singular and indefinite, not plural.\",\"representative_source_ids\":[\"QF-8461a88c\",\"MF-9a86e4cf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:6:state-locus-environment","source_type":"word_analysis","support_id":"sup_0d4730a87899a221dad3","text":"{\"blocking_evidence\":null,\"headline\":\"hunger as inhabitable crisis environment\",\"reader_payoff\":\"The reader feels scarcity as an environment one suffers within, while the local phrase keeps it attached to a day.\",\"reason\":\"The mīm formation and place-time pressure survive because the word is embedded in a day phrase, but the selected local function remains condition possessed by the day.\",\"representative_source_ids\":[\"QS-09eac795\",\"QS-6ca2c87e\",\"QF-e33182ff\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:2:variant-agency","source_type":"word_analysis","support_id":"sup_0f6c7f3b8ee88aa90b30","text":"{\"blocking_evidence\":null,\"headline\":\"accepted variant shifts posture to performed feeding\",\"reader_payoff\":\"The reader notices that the variant can make the feeder more explicit while preserving the same act inside the steep-path definition.\",\"reason\":\"The local output remains anchored to the canonical nominal surface, while the variant is kept as case and agency evidence rather than allowed to replace the aligned form.\",\"representative_source_ids\":[\"QG-46749e7f\",\"QF-a940b8b5\",\"QF-ef6031a2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:3:temporal-circumstantial-double-value","source_type":"word_analysis","support_id":"sup_1f75cafc759f9411b2b4","text":"{\"blocking_evidence\":null,\"headline\":\"during a day and within a condition\",\"reader_payoff\":\"The reader feels the day both as time and as an enclosing condition of scarcity.\",\"reason\":\"The local governed noun is a day, while the following qualifier makes that time a condition-bearing environment.\",\"representative_source_ids\":[\"QS-8c36bbaf\",\"QS-c1408cd8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:2:famine-time-cost","source_type":"word_analysis","support_id":"sup_23c02b6c67dcb161f1d4","text":"{\"blocking_evidence\":null,\"headline\":\"feeding tested by scarcity-time\",\"reader_payoff\":\"The reader notices that feeding is evaluated by when it happens: it becomes costly provision during hunger-bearing time.\",\"reason\":\"Attachment evidence makes the day phrase the temporal complement of the feeding noun, so timing belongs to the deed's value.\",\"representative_source_ids\":[\"QG-56c8adac\",\"QS-cb6ffd11\",\"MT-2a1cecbc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:5:forward-possessive-skeleton","source_type":"word_analysis","support_id":"sup_3f860a00340f889b49fb","text":"{\"blocking_evidence\":null,\"headline\":\"possessive skeleton carries into recipient descriptions\",\"reader_payoff\":\"The reader sees one possessive pattern move from crisis-time to the vulnerable recipients of 90:15-16.\",\"reason\":\"The same possessive lexeme appears in the adjacent recipient descriptions, linking condition of time with condition of persons.\",\"representative_source_ids\":[\"QI-251e7d33\",\"MT-6c8337c4\",\"QE-eca6d83b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:2","source_type":"word_analysis","support_id":"sup_406a778a14dd403f6774","text":"{\"gloss_range\":\"indefinite Form IV verbal noun naming the deed-category of causing another to eat, with the recipient delayed and the famine-time setting making the act costly\",\"prose\":\"{{ar:إِطْعَٰمٌۭ}} ({{tr:iṭʿāmun}}) is an indefinite Form IV verbal noun, so the ayah names feeding as a deed-category before it names agent or recipient. The form turns the root's eating and food field outward: the ascent is causing another to eat, not private eating or a mere food object, and it creates a giver-receiver transfer before either identity is filled in. Its object is withheld until the orphan recipient appears in 90:15, while the present ayah first makes the deed happen in {{ar:مَسْغَبَةٍۢ}} ({{tr:masghabatin}}). That order matters: the reader hears provision before discovering that food is being released under scarcity, with feeding as the first content beat in the chain of deed, day, and famine. The low-occurrence verbal-noun register makes the deed sound like structured ascent-content rather than casual generosity. The accepted perfect-verb variant preserves the same ascent-act while making human agency more explicit, and the echoes with divine feeding from hunger (106:4) and feeding despite attachment to food (76:8) sharpen the human crisis-deed here. Across the boundary from 90:13, the ascent moves from unfastening a constrained body to sustaining a hungry one.\",\"root_display\":\"{{ar:ط ع م}} ({{tr:ṭ-ʿ-m}})\",\"root_gloss_range\":\"taste, eating, food, causing to eat, provision, edible share, livelihood, and construction-bound extensions; the local Form IV verbal noun selects outward provisioning\",\"surface_display\":\"{{ar:إِطْعَٰمٌۭ}} ({{tr:iṭʿāmun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:6:genitive-scarcity-complement","source_type":"word_analysis","support_id":"sup_4bba047cd3b0f2d3717f","text":"{\"blocking_evidence\":null,\"headline\":\"scarcity possessed by the day\",\"reader_payoff\":\"The reader sees famine defining the temporal setting from inside the syntax.\",\"reason\":\"The word is the genitive complement governed by the construct head, so scarcity is syntactically attached to the day.\",\"representative_source_ids\":[\"QG-10b6485f\",\"QG-bf7fe3ab\",\"MG-efae5f42\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:4:indefinite-crisis-day","source_type":"word_analysis","support_id":"sup_4c6f389ab3ed050370ff","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite type of crisis-day\",\"reader_payoff\":\"The reader notices that the ayah defines any such hunger-bearing day as the proving interval, not one known date.\",\"reason\":\"The word is indefinite, genitive under the preposition, and immediately qualified by the possessive scarcity phrase.\",\"representative_source_ids\":[\"QG-419a9689\",\"MG-a30bded2\",\"QF-a428fb95\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:2:form-iv-provision","source_type":"word_analysis","support_id":"sup_4cdb769a1810cdea36b5","text":"{\"blocking_evidence\":null,\"headline\":\"causing another to eat\",\"reader_payoff\":\"The reader notices that the word is about transferred sustenance, so the ascent moves outward toward another body.\",\"reason\":\"The Form IV verbal noun selects causative provision and blocks reducing the word to private eating or a food object.\",\"representative_source_ids\":[\"QS-07c4264b\",\"QF-5d353128\",\"MF-9e0eb9bc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:5:possessive-construct","source_type":"word_analysis","support_id":"sup_60ce2b3351f50194906c","text":"{\"blocking_evidence\":null,\"headline\":\"possessive construct attaches scarcity to the day\",\"reader_payoff\":\"The reader notices that scarcity is grammatically made the day's possession, not a detachable background condition.\",\"reason\":\"The five-noun form modifies the day and governs the following scarcity noun as its genitive complement.\",\"representative_source_ids\":[\"QG-67731b04\",\"QG-cc2e3cdc\",\"MG-0c555a87\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:6:provision-against-famine","source_type":"word_analysis","support_id":"sup_65568d2d854bc7b5e3f3","text":"{\"blocking_evidence\":null,\"headline\":\"feeding answers exactly the famine condition\",\"reader_payoff\":\"The reader sees provision and famine set against each other in one phrase, making the deed costly rather than surplus.\",\"reason\":\"The first content noun names feeding and the final content noun names food-scarcity, creating the local provision-deprivation opposition.\",\"representative_source_ids\":[\"QS-1d76ca2c\",\"QS-95ec8cb5\",\"ME-e7ef2bd5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:1","source_type":"word_analysis","support_id":"sup_681062493106ff96d859","text":"{\"gloss_range\":\"coordinating alternative particle that carries the prior ascent-definition forward and introduces a parallel nominal deed\",\"prose\":\"{{ar:أَوْ}} ({{tr:aw}}) opens the ayah in mid-definition, so the reader carries the prior freeing deed from 90:13 into the next alternative. The particle links another nominal deed, {{ar:إِطْعَٰمٌۭ}} ({{tr:iṭʿāmun}}), to the same ascent-frame rather than starting a detached sentence. Its alternative force is classificatory, not exclusionary: freeing and feeding become distinct bodily forms of the same moral climb. Because the particle comes before the famine-time phrase, the deed is named first and then made costly by its setting.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَوْ}} ({{tr:aw}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:1:parallel-nominal-deed","source_type":"word_analysis","support_id":"sup_6c69916fa72bdb35b862","text":"{\"blocking_evidence\":null,\"headline\":\"parallel nominal deed rather than finite-clause shift\",\"reader_payoff\":\"The reader sees feeding as grammatically parallel to the prior compressed deed, so the ascent is defined by concrete deed-categories.\",\"reason\":\"The following word is an indefinite nominative verbal noun, so the particle coordinates predicate-like nominal action rather than introducing a finite narrative clause.\",\"representative_source_ids\":[\"QG-ea565c3d\",\"MG-63770f51\",\"QE-82f7c74a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:5:characterization-not-ownership","source_type":"word_analysis","support_id":"sup_734954cbfc9e0d76b6c6","text":"{\"blocking_evidence\":null,\"headline\":\"possession as characterization\",\"reader_payoff\":\"The reader feels hunger as the day's defining mark while avoiding a literal ownership reading.\",\"reason\":\"The construct makes the day a bearer of scarcity, but local semantics require attributed characterization rather than property ownership.\",\"representative_source_ids\":[\"QS-4f3664fc\",\"QS-af726959\",\"MS-af17ecc3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:2:material-food-pressure","source_type":"word_analysis","support_id":"sup_73a972e64b154e0366d0","text":"{\"blocking_evidence\":null,\"headline\":\"material food field made outward\",\"reader_payoff\":\"The reader feels that the deed is concrete transfer of edible provision rather than abstract kindness.\",\"reason\":\"The broader root field of taste, food, morsel, and livelihood survives as material pressure, while local Form IV grammar keeps outward feeding as the selected sense.\",\"representative_source_ids\":[\"QS-47b79ad2\",\"QS-73dd3557\",\"MS-218aa719\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:6:ambient-scarcity-before-recipient","source_type":"word_analysis","support_id":"sup_74e088e6f8470538e7c6","text":"{\"blocking_evidence\":null,\"headline\":\"ambient scarcity before named recipient\",\"reader_payoff\":\"The reader notices that the condition is named before the hungry recipients, so deprivation fills the scene before bodies are specified.\",\"reason\":\"The phrase attributes hunger to the day, and the next ayahs then name the recipient bodies.\",\"representative_source_ids\":[\"QS-2b6897d1\",\"QS-ea7d5455\",\"QE-59d0107a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:1:dependent-continuation","source_type":"word_analysis","support_id":"sup_76257d8d1b1cac32d99f","text":"{\"blocking_evidence\":null,\"headline\":\"dependent continuation across the ayah boundary\",\"reader_payoff\":\"The reader notices that the ayah begins by carrying the previous answer forward, not by opening a new independent sentence.\",\"reason\":\"The aligned particle is a coordinating conjunction, and the local clause evidence keeps the ayah inside the nominal answer sequence begun at 90:13.\",\"representative_source_ids\":[\"QG-180bd551\",\"QT-5150617a\",\"QB-863191ed\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:3:scope-over-feeding","source_type":"word_analysis","support_id":"sup_789fa7993049f03a873b","text":"{\"blocking_evidence\":null,\"headline\":\"scarcity phrase scopes over the act\",\"reader_payoff\":\"The reader sees the whole feeding scene narrowed into crisis-feeding, not a generic charitable act.\",\"reason\":\"The prepositional phrase modifies the feeding action and adds situational density to the second ascent act.\",\"representative_source_ids\":[\"QG-7dab8173\",\"MT-558cb61a\",\"QB-ffa70951\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:5","source_type":"word_analysis","support_id":"sup_7cbcce1acfd9a79b29ba","text":"{\"gloss_range\":\"genitive five-noun possessive adjective meaning possessed of or characterized by, modifying the day and governing the scarcity complement\",\"prose\":\"{{ar:ذِى}} ({{tr:dhī}}) is the hinge between day and scarcity. It agrees with {{ar:يَوْمٍۢ}} ({{tr:yawmin}}) and governs {{ar:مَسْغَبَةٍۢ}} ({{tr:masghabatin}}), so hunger is not a loose background noun; it is what the day is characterized by. The possession is descriptive rather than literal ownership, with enough identity pressure to make scarcity cling to the day without turning the word into an independent essence claim. The accepted variant can shift case posture toward a more circumstantial reading but does not detach hunger from the day. This possessive skeleton then prepares the nearness-marked recipient in 90:15 and the recipient description in 90:16. Compared with kinship-recipient possession in 2:177, possession-language is applied first to the day itself before returning to persons.\",\"root_display\":\"{{ar:ذ و و}} ({{tr:dh-w-w}})\",\"root_gloss_range\":\"possessor, one characterized by a following noun, bearer of an attribute, and related demonstrative or essence-family branches; local five-noun construct selects attributed possession\",\"surface_display\":\"{{ar:ذِى}} ({{tr:dhī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:6:boundary-body-rescue","source_type":"word_analysis","support_id":"sup_7f0e783561c4f9115305","text":"{\"blocking_evidence\":null,\"headline\":\"from bodily constraint to bodily deprivation\",\"reader_payoff\":\"The reader sees the steep path as costly intervention in bodily need: release from constraint, then rescue from starvation.\",\"reason\":\"The boundary rows connect the famine closure with the previous liberation deed and the following beneficiary focus.\",\"representative_source_ids\":[\"QB-4718692e\",\"QB-5115ca81\",\"QY-aed77c9d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:3:beat-pivot","source_type":"word_analysis","support_id":"sup_80ba7c9a9c5c183af320","text":"{\"blocking_evidence\":null,\"headline\":\"short pivot from deed to setting\",\"reader_payoff\":\"The reader hears a compact turn immediately after the deed, as the line moves into its temporal setting without delay.\",\"reason\":\"The preposition begins the second beat and flows directly into the day noun.\",\"representative_source_ids\":[\"QT-e131165f\",\"QT-f8740630\",\"QP-b3ca11c6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:6:contrast-with-hunger-formula","source_type":"word_analysis","support_id":"sup_80bde38441590e6cd1ec","text":"{\"blocking_evidence\":null,\"headline\":\"rarer famine term contrasted with divine feeding formula\",\"reader_payoff\":\"The reader compares divine feeding from hunger (106:4) with this rarer term for a human crisis-deed in 90:14.\",\"reason\":\"The concrete reference (106:4) is retained as contrast without replacing the local word's famine-condition sense.\",\"representative_source_ids\":[\"QI-fbf1ac8d\",\"MI-836996db\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:4:delayed-scarcity-cadence","source_type":"word_analysis","support_id":"sup_8481f18c5d67181f7548","text":"{\"blocking_evidence\":null,\"headline\":\"day delays the scarcity landing\",\"reader_payoff\":\"The reader hears the day as the middle link between deed and crisis, with scarcity arriving as the delayed final disclosure.\",\"reason\":\"The word stands between the feeding noun and final scarcity noun, and the indefinite cadence links the major nouns.\",\"representative_source_ids\":[\"QT-db27712f\",\"QE-6b12f485\",\"QP-dcdff40f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:3","source_type":"word_analysis","support_id":"sup_89aeae9610e910c29548","text":"{\"gloss_range\":\"preposition of temporal and circumstantial containment governing the day phrase as the setting inside which feeding is evaluated\",\"prose\":\"{{ar:فِى}} ({{tr:fī}}) governs {{ar:يَوْمٍۢ}} ({{tr:yawmin}}), making the following day phrase the container in which feeding is evaluated. The particle therefore does more than add a date: because the day is defined by {{ar:مَسْغَبَةٍۢ}} ({{tr:masghabatin}}), temporal placement becomes circumstantial pressure. After the feeding noun, this small preposition pivots the line from deed to setting, so the act is judged inside hunger-time rather than after scarcity has passed.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِى}} ({{tr:fī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:5:hinge-and-cadence","source_type":"word_analysis","support_id":"sup_93af703aa190192a8771","text":"{\"blocking_evidence\":null,\"headline\":\"hinge from time noun to scarcity noun\",\"reader_payoff\":\"The reader hears the word as the hinge that turns a bare day into a hunger-bearing day.\",\"reason\":\"The word opens the final qualifier beat and links the preceding day noun to the following scarcity noun.\",\"representative_source_ids\":[\"QT-403f4abc\",\"QT-c9832b2a\",\"QP-890389b8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:3:temporal-containment","source_type":"word_analysis","support_id":"sup_97565bf03822b13f4dae","text":"{\"blocking_evidence\":null,\"headline\":\"day governed as temporal container\",\"reader_payoff\":\"The reader notices that feeding is placed inside a pressure-bearing interval, not merely next to a date.\",\"reason\":\"QAC and attachment evidence make the preposition govern the day as the temporal complement of the feeding noun.\",\"representative_source_ids\":[\"QG-d2ad73f3\",\"MG-2433cb9b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:6:sound-and-indefinite-chain","source_type":"word_analysis","support_id":"sup_982299a4821e887775e4","text":"{\"blocking_evidence\":null,\"headline\":\"heavy closure and indefinite cadence\",\"reader_payoff\":\"The reader hears the line move from open feeding into the heavier, constricted sound of famine.\",\"reason\":\"The final word closes the indefinite noun chain and carries the CRITICAL sound observation about constricted scarcity.\",\"representative_source_ids\":[\"QP-2ec11c2d\",\"QP-b4105abd\",\"MP-8852db43\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:5:essence-pressure-limited","source_type":"word_analysis","support_id":"sup_a15c1642ba69a550ba6a","text":"{\"blocking_evidence\":null,\"headline\":\"identity-like pressure within construct bounds\",\"reader_payoff\":\"The reader notices that scarcity becomes part of how the day is constituted in the phrase, not an incidental side note.\",\"reason\":\"The essence-family pressure is preserved as characterization force, while local grammar keeps the selected function as possessive adjective.\",\"representative_source_ids\":[\"QS-afae925f\",\"QS-b84b9b4c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:6:layered-personal-social-crisis","source_type":"word_analysis","support_id":"sup_a799923f72dea9e38a47","text":"{\"blocking_evidence\":null,\"headline\":\"personal hunger expands into social crisis\",\"reader_payoff\":\"The reader sees bodily hunger broaden into a social emergency that prepares concrete poverty in 90:16.\",\"reason\":\"The final noun names a scarcity condition that becomes socially concrete in the following recipient descriptions.\",\"representative_source_ids\":[\"QS-f024394a\",\"QB-59d14617\",\"QB-6a31af7f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:4:boundary-expansion-to-event-time","source_type":"word_analysis","support_id":"sup_a7ea427aa66bbb3597c4","text":"{\"blocking_evidence\":null,\"headline\":\"from bare act to occasion\",\"reader_payoff\":\"The reader sees the steep-path definition expand from the act itself to the occasion in which the act becomes weighty.\",\"reason\":\"The day noun adds occasion and moral setting to the already named feeding deed.\",\"representative_source_ids\":[\"QI-4ee7544a\",\"QB-7be09802\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:6:severe-hunger-not-appetite","source_type":"word_analysis","support_id":"sup_acd65de21da5b845a9fe","text":"{\"blocking_evidence\":null,\"headline\":\"severe hunger and bodily weakening\",\"reader_payoff\":\"The reader understands feeding as an answer to bodily danger and deprivation, not preference or ordinary appetite.\",\"reason\":\"The root and local noun select severe hunger, famine, and bodily weakness rather than a mild desire for food.\",\"representative_source_ids\":[\"QS-1ddaa99c\",\"QS-396ce50d\",\"MS-dc7c0a61\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:2:role-reversal-and-transfer","source_type":"word_analysis","support_id":"sup_afd88e1ee9b093a6a088","text":"{\"blocking_evidence\":null,\"headline\":\"supplier role before needy recipients appear\",\"reader_payoff\":\"The reader notices transfer before identities: the act creates a giver-receiver relation even while both parties remain unnamed.\",\"reason\":\"Derivative pressure about seeking food is kept as role contrast only; the local surface names giving food, not asking for it.\",\"representative_source_ids\":[\"QS-847657fd\",\"QS-a8e93291\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:2:delayed-recipient","source_type":"word_analysis","support_id":"sup_b23c7eae5f2f80a77a8c","text":"{\"blocking_evidence\":null,\"headline\":\"recipient withheld until the next ayahs\",\"reader_payoff\":\"The reader hears the deed and its scarcity-setting before the vulnerable bodies in 90:15-16 are named.\",\"reason\":\"The local noun is grammatically complete but semantically awaits the recipients named immediately after this ayah.\",\"representative_source_ids\":[\"QG-b7e0127e\",\"MI-404fb0da\",\"QE-cb4aa6ee\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:6:convergent-final-crisis-state","source_type":"word_analysis","support_id":"sup_b77b9bdef22d747f4e54","text":"{\"blocking_evidence\":null,\"headline\":\"hapax rarity, bodily hunger, and sound converge\",\"reader_payoff\":\"The reader recognizes the final word as a concentrated crisis-state, not an interchangeable time-label.\",\"reason\":\"The convergence row combines low occurrence, severe hunger semantics, and heavy closure into one locally coherent payoff.\",\"representative_source_ids\":[\"QH-7a03e6b1\",\"QY-d7c3ddfa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:2:rare-duty-register","source_type":"word_analysis","support_id":"sup_bcd7ace7eac45151fba3","text":"{\"blocking_evidence\":null,\"headline\":\"rare verbal-noun register in structured duty contexts\",\"reader_payoff\":\"The reader notices the conspicuous deed-form, which makes feeding sound like structured ascent-content rather than casual generosity.\",\"reason\":\"The contextual profile marks this exact root-form as low occurrence, and the CRITICAL rows tie that rarity to structured deed language.\",\"representative_source_ids\":[\"QI-a0e6d68a\",\"QI-c6775b8b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:2:sequence-sound-body","source_type":"word_analysis","support_id":"sup_c11768d6114bafd9f6b5","text":"{\"blocking_evidence\":null,\"headline\":\"act beat, cadence, and embodied sound\",\"reader_payoff\":\"The reader hears feeding as the first content beat in a chain that binds deed, day, and famine.\",\"reason\":\"The sequence places the feeding noun before the setting, and the repeated indefinite endings bind the major nouns audibly.\",\"representative_source_ids\":[\"QT-80144aa7\",\"QP-b9ca8af9\",\"QP-fb2d2cac\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:6","source_type":"word_analysis","support_id":"sup_c21a14187e3f3986141a","text":"{\"gloss_range\":\"indefinite genitive mīm state noun naming severe hunger, famine, or scarcity-condition possessed by the day and closing the ayah as the cost of feeding\",\"prose\":\"{{ar:مَسْغَبَةٍۢ}} ({{tr:masghabatin}}) is the ayah's final landing word. As the genitive complement of {{ar:ذِى}} ({{tr:dhī}}), it makes scarcity the defining condition of the day, not a detached background. Its root and mīm state-form point to severe hunger, famine, and bodily weakening, so {{ar:إِطْعَٰمٌۭ}} ({{tr:iṭʿāmun}}) answers danger rather than appetite. The mīm state-form also makes scarcity feel like an environment suffered within, while local grammar keeps that environment attached to the day. The word is indefinite, rare in the supplied evidence, and delayed until the end; the listener first hears feeding and day, then discovers that the deed happens inside deprivation. Its heavier, constricted final sound and indefinite closure make the famine word feel like the chain's tightened landing. The contrast with divine feeding from hunger (106:4) sharpens the local human crisis-deed, and the closure prepares the vulnerable recipients named in 90:15-16, including the concrete poverty named in 90:16. Across 90:13-14, release from bodily constraint gives way to rescue from bodily deprivation.\",\"root_display\":\"{{ar:س غ ب}} ({{tr:s-gh-b}})\",\"root_gloss_range\":\"hunger, famine, food-scarcity, severe want, and bodily weakening from lack of food; local mīm state noun selects a crisis condition rather than ordinary appetite\",\"surface_display\":\"{{ar:مَسْغَبَةٍۢ}} ({{tr:masghabatin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:14:6:1","source_type":"qac_morpheme","support_id":"sup_c2a785ea2fb97ee034d9","text":"{\"lemma_ar\":\"مَسْغَبَة\",\"morph_features\":\"STEM|POS:N|LEM:masogabap|ROOT:sgb|F|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:14:6:1\",\"qac_word_ref\":\"90:14:6\",\"root_ar\":\"س غ ب\",\"surface_ar\":\"مَسْغَبَةٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:2:interayah-feeding-echoes","source_type":"word_analysis","support_id":"sup_c8bc66647a39137f0be9","text":"{\"blocking_evidence\":null,\"headline\":\"feeding echoes intensified by local famine\",\"reader_payoff\":\"The reader can compare divine feeding from hunger (106:4) and feeding despite love of food (76:8) with this human act inside famine-time.\",\"reason\":\"The referenced parallels are concrete and do not override the local parse; they sharpen the cost of human provision in 90:14.\",\"representative_source_ids\":[\"QI-73cb84c9\",\"QI-98f0c497\",\"MI-df828333\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:4:collocated-time-host","source_type":"word_analysis","support_id":"sup_c9119c79803815e078a2","text":"{\"blocking_evidence\":null,\"headline\":\"time paired with feeding and possession\",\"reader_payoff\":\"The reader sees the day as the syntactic host that binds feeding to the scarcity it possesses.\",\"reason\":\"The local construction pairs the day with the possessive qualifier and places it as the temporal complement of feeding.\",\"representative_source_ids\":[\"QI-75b51040\",\"QI-c48a185b\",\"QT-3aa7478d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:4","source_type":"word_analysis","support_id":"sup_ccfb4c165d0582f3087e","text":"{\"gloss_range\":\"indefinite singular crisis-day or event-time governed by the preposition and characterized by the following scarcity possession phrase\",\"prose\":\"{{ar:يَوْمٍۢ}} ({{tr:yawmin}}) is an indefinite singular day governed by {{ar:فِى}} ({{tr:fī}}), but it is not merely a calendar label. The following {{ar:ذِى مَسْغَبَةٍۢ}} ({{tr:dhī masghabatin}}) makes it a type of crisis interval, a day characterized by the scarcity it bears. The singular indefinite form concentrates the test into any one such occasion, while the broader day-field lets the word function as event-time. The listener hears feeding in a day before the final word discloses what the day possesses, so time becomes the host and moral instructor of scarcity; the lesson-bearing days of God (14:5) remain an echo, while the local phrase stays a famine-day.\",\"root_display\":\"{{ar:ي و م}} ({{tr:y-w-m}})\",\"root_gloss_range\":\"day, daylight span, period, occasion, event-time, and marked evaluative day; local grammar selects an indefinite scarcity-marked interval\",\"surface_display\":\"{{ar:يَوْمٍۢ}} ({{tr:yawmin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:14:2:1","source_type":"qac_morpheme","support_id":"sup_ce80fdfbd8ca07bd752a","text":"{\"lemma_ar\":\"إِطْعَٰم\",\"morph_features\":\"STEM|POS:N|VN|(IV)|LEM:<iToEa`m|ROOT:TEm|M|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:14:2:1\",\"qac_word_ref\":\"90:14:2\",\"root_ar\":\"ط ع م\",\"surface_ar\":\"إِطْعَٰمٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:4:event-time-not-mere-date","source_type":"word_analysis","support_id":"sup_d2bb6f3b015baa74a99d","text":"{\"blocking_evidence\":null,\"headline\":\"event-time rather than mere daylight span\",\"reader_payoff\":\"The reader treats the day as the occasion that tests feeding, not as a neutral measure of duration.\",\"reason\":\"The broader day range includes event-time, and local grammar narrows that range to a scarcity-marked temporal circumstance.\",\"representative_source_ids\":[\"QG-d99c449b\",\"QS-b446504d\",\"MS-bcfc35c8\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:6:rare-final-word","source_type":"word_analysis","support_id":"sup_d3cbbe69157294783e6f","text":"{\"blocking_evidence\":null,\"headline\":\"rare famine word bears final load\",\"reader_payoff\":\"The reader notices that the ayah saves a rare, severe scarcity word for its closing pressure.\",\"reason\":\"The contextual evidence marks the exact root-form as low occurrence, and the CRITICAL rows tie that rarity to the final semantic landing.\",\"representative_source_ids\":[\"QI-c4f9eb3e\",\"QH-dfa16f99\",\"MH-d03b664e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:6:indefinite-state-condition","source_type":"word_analysis","support_id":"sup_d3e1321d2f81c20bd9cb","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite state rather than known famine event\",\"reader_payoff\":\"The reader notices that the ayah names a kind of scarcity condition that can mark any qualifying day.\",\"reason\":\"The local noun is indefinite genitive and closes the construct as a named condition, not a proper event label.\",\"representative_source_ids\":[\"QG-1b86f48e\",\"QF-c04e7422\",\"QF-e8b8a5a5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:6:delayed-final-revelation","source_type":"word_analysis","support_id":"sup_dff7695c7dc31c847d15","text":"{\"blocking_evidence\":null,\"headline\":\"scarcity delayed to ayah closure\",\"reader_payoff\":\"The reader first hears feeding and day, then the last word reveals the full cost of that feeding.\",\"reason\":\"The scarcity noun is the final word of the ayah and retroactively qualifies the preceding deed and time.\",\"representative_source_ids\":[\"QT-42a61f7a\",\"QT-53de3ac7\",\"QT-e75afe31\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:1:deed-before-cost","source_type":"word_analysis","support_id":"sup_e6630199c4b55f55e708","text":"{\"blocking_evidence\":null,\"headline\":\"deed installed before circumstance\",\"reader_payoff\":\"The reader first hears the alternative deed itself and only then discovers the scarcity that makes it demanding.\",\"reason\":\"The particle immediately releases into the feeding noun before the temporal-scarcity phrase appears.\",\"representative_source_ids\":[\"QT-70b53991\",\"QP-0cda06be\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:4:evaluative-day-field","source_type":"word_analysis","support_id":"sup_ea374210e25da30f80dc","text":"{\"blocking_evidence\":null,\"headline\":\"evaluative day field localized to famine\",\"reader_payoff\":\"The reader feels time as morally instructive here, while the local qualifier specifies hunger rather than judgment or divine-days language.\",\"reason\":\"The echo with lesson-bearing days (14:5) survives as contrast, but the local construct phrase selects a hunger-bearing day.\",\"representative_source_ids\":[\"QS-4497758e\",\"QS-5aa10d80\",\"MI-66789ac6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:14:4:1","source_type":"qac_morpheme","support_id":"sup_eac2f9b28edb3dd951ab","text":"{\"lemma_ar\":\"يَوْم\",\"morph_features\":\"STEM|POS:N|LEM:yawom|ROOT:ywm|M|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:14:4:1\",\"qac_word_ref\":\"90:14:4\",\"root_ar\":\"ي و م\",\"surface_ar\":\"يَوْمٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:2:nominal-deed-category","source_type":"word_analysis","support_id":"sup_f06e2b12e43e5a53b2ce","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite nominal deed-category\",\"reader_payoff\":\"The reader sees feeding as a defining ascent-category, not just one narrated incident or a ritual label.\",\"reason\":\"QAC identifies the word as an indefinite Form IV verbal noun coordinated in the nominal answer phrase.\",\"representative_source_ids\":[\"QG-1d577bf7\",\"QG-644c2879\",\"QF-023de982\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:1:nonexclusive-alternative","source_type":"word_analysis","support_id":"sup_f3a53855db715026f326","text":"{\"blocking_evidence\":null,\"headline\":\"alternative of kinds, not exclusion\",\"reader_payoff\":\"The reader notices that the alternatives classify different forms of ascent instead of making one bodily rescue cancel the other.\",\"reason\":\"The coordinated answer frame supports an alternative-list reading in which freeing and feeding remain parallel ascent acts.\",\"representative_source_ids\":[\"QS-3337bc15\",\"QS-edd3f1c5\",\"MT-53b9d624\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:14:5:charity-possession-shift","source_type":"word_analysis","support_id":"sup_f9de1f0648c7bd0ad549","text":"{\"blocking_evidence\":null,\"headline\":\"possession-language shifts from recipients to time\",\"reader_payoff\":\"The reader notices charity-style possession language applied first to the day itself before it returns to recipients.\",\"reason\":\"The contrast with kinship possession in 2:177 remains a valid reference, while the local syntax makes time the bearer here.\",\"representative_source_ids\":[\"QI-7033aa9e\",\"MI-66b14c8e\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ","ayah_ref":"90:14"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000710/B001","root_000934/B002","root_001700/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000934","role":"Giving food to another anchors an outward transfer rather than the feeder's own eating.","root":"ط ع م","source_ref":"90:14","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001700","role":"The severe event-day makes the transfer a response to an acute occasion.","root":"ي و م","source_ref":"90:14","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000710","role":"Hunger with exhaustion and famine supplies the recipient's bodily and collective emergency.","root":"س غ ب","source_ref":"90:14","source_word_indices":["6"]}],"changed_reading":{"after":"Move nourishment outward precisely when famine makes both the need and the cost of giving acute.","before":"Give someone food."},"confidence":"strong","focus_anchor":"The focus construction joins the verbal noun إطعام to a severe hunger-event through في يوم ذي مسغبة.","mechanism":"Nourishment crosses from a possessor to another person exactly when hunger has become exhausting and socially extensive; timing under scarcity, not food in the abstract, gives the act its force.","model_id":"B01_CRISIS_TRANSFER"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:B01_CRISIS_TRANSFER","source_type":"hft","support_id":"sup_b110c9558e06989965d5","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ","ayah_ref":"90:14"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000710/B001","root_000934/B004","root_001700/B002"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000934","role":"Provision and livelihood widen feeding from a meal to material maintenance.","root":"ط ع م","source_ref":"90:14","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001700","role":"An open span of time lets the hungry period exceed a single daylight interval.","root":"ي و م","source_ref":"90:14","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000710","role":"Famine and exhausted hunger make maintenance recurrent rather than episodic.","root":"س غ ب","source_ref":"90:14","source_word_indices":["6"]}],"changed_reading":{"after":"Keep another person provisioned across the duration of an exhausting scarcity.","before":"Offer one emergency meal."},"confidence":"medium","focus_anchor":"إطعام, يوم, and مسغبة can be read as provision sustained across a duration of famine.","mechanism":"The provision/livelihood branch and the open-span branch stretch the act beyond one plate: feeding maintains another's viable condition through an interval in which hunger repeatedly returns.","model_id":"B02_FAMINE_MAINTENANCE"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:B02_FAMINE_MAINTENANCE","source_type":"hft","support_id":"sup_2ffe64fb429baf2af6ba","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ","ayah_ref":"90:14"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000710/B001","root_000934/B001","root_000934/B011"],"payload":{"activation_trace":[{"branch_id":"B011","mapped_root_id":"root_000934","role":"The ability branch supplies restored capability as feeding's functional result.","root":"ط ع م","source_ref":"90:14","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000934","role":"Taking in nourishment supplies the bodily means by which capability can return.","root":"ط ع م","source_ref":"90:14","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000710","role":"Hunger joined to exhaustion identifies the incapacity that nourishment reverses.","root":"س غ ب","source_ref":"90:14","source_word_indices":["6"]}],"changed_reading":{"after":"Restore a hunger-exhausted person's power to act.","before":"Fill an empty stomach."},"confidence":"medium","focus_anchor":"The ability branch of ط ع م remains attached to إطعام and meets the exhaustion named by مسغبة.","mechanism":"Food intake interrupts hunger's depletion and returns capacity for motion, judgment, and action; the relevant outcome is not merely possession of calories but restored agency.","model_id":"B03_CAPACITY_RESTORATION"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:B03_CAPACITY_RESTORATION","source_type":"hft","support_id":"sup_c0b563797e6464b0e9a6","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ","ayah_ref":"90:14"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000710/B001","root_000934/B010","root_001700/B003"],"payload":{"activation_trace":[{"branch_id":"B010","mapped_root_id":"root_000934","role":"A graft that accepts an insertion supplies the image of aid entering and taking hold.","root":"ط ع م","source_ref":"90:14","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001700","role":"The severe occasion supplies the stressed environment in which successful uptake matters.","root":"ي و م","source_ref":"90:14","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000710","role":"Famine supplies the damaged condition into which sustaining support must take.","root":"س غ ب","source_ref":"90:14","source_word_indices":["6"]}],"changed_reading":{"after":"Introduce sustenance in a form the famine-stressed recipient can actually receive and incorporate.","before":"Hand over a food object."},"confidence":"exploratory","focus_anchor":"The grafting and receptive-insertion branch belongs to the focus root ط ع م itself.","mechanism":"Feeding is imagined as introducing support into a stressed living system so that the support is received and becomes operative, not merely placing an object beside a need.","model_id":"B04_SUPPORT_THAT_TAKES"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:B04_SUPPORT_THAT_TAKES","source_type":"hft","support_id":"sup_9d0b5164baa90d1667b0","trust":"legacy_unbound"}]}
</lane_packet_json>
