# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **92:12**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s092-regular-20260912/s092/92_12/micro.discovery.json` and modify nothing
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
  "ayah_ref": "92:12",
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
{"branch_registry":[{"boundary":"Kapsam yapisal kirma ve yikmadir; duyulan gurultu ancak ayri ses dalinda ele alinir.","branch_kind":"mixed_non_bare","branch_ref":"root_001580/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"agir kirip yikma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir seyin yapisal butunlugunu agir bicimde kirip yikma veya cokertme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Duvar, bina ve dag gibi kutleli varliklarda parcalanma veya yikilma olarak gerceklesir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yer cokmesi ya da yikima benzeyen agir olaylar ayni bozulma alanina girer."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir felaket kisiye yoneldiginde onu gucsuz dusurup dayanagini kirmis gibi anlatir."}}],"root_ar":"ه د ي","root_id":"root_001580","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Cekirdek anlamda yapisal butunlugu bozan sert kirma ve yikma etkisini dogrudan karsilar.","boundary_detail":"Kapsam yapisal kirma ve yikmadir; duyulan gurultu ancak ayri ses dalinda ele alinir.","concept_gloss":"agir kirip yikma","contextual_glosses":[{"applicability":"Felaketin kisi uzerindeki sarsici ve dayanagi zedeleyen etkisini anlatan baglamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yapi, duvar, dag veya yer cokmesi gibi maddi yikim alani disarida kalir.","preserves":"Kisiye yonelen kirici ve gucsuz dusurucu etki korunur."},"facet_ids":["F004"],"text":"gucunu kirmak","usage_role":"contextual"},{"applicability":"Yapi veya zeminin ayakta kalma durumunu kaybettigi baglamlarda dogal bir karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kirma ve ezme yonu ile kisi uzerindeki mecazi etki acik kalmaz.","preserves":"Yikilma ve dayanagin kaybolmasi korunur."},"facet_ids":["F001","F002","F003"],"text":"cokertmek","usage_role":"contextual"}],"definition":"Bu dal, bir varligin dayanak ve butunlugunu agir bicimde kirip yikma, cokertme veya bu duruma dusme anlamindadir. Felaketin kisiyi sarsip gucunu kirmasi bunun kisi uzerindeki ozel kullanimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir seyin yapisal butunlugunu agir bicimde kirip yikma veya cokertme."},{"facet_id":"F002","role":"specialization","statement":"Duvar, bina ve dag gibi kutleli varliklarda parcalanma veya yikilma olarak gerceklesir."},{"facet_id":"F003","role":"extension","statement":"Yer cokmesi ya da yikima benzeyen agir olaylar ayni bozulma alanina girer."},{"facet_id":"F004","role":"associated_use","statement":"Bir felaket kisiye yoneldiginde onu gucsuz dusurup dayanagini kirmis gibi anlatir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ayri ses dalina ait isitsel anlam eklenir.","collision":"Ses dalinin karsiligi ile karisir.","fit":"displacement","loses":"Kirma, yikma ve cokertme cekirdegi kaybolur.","preserves":"Yikimla birlikte ortaya cikabilecek isitsel etkiyi korur."},"text":"gurultu"}],"identity_rationale":"Kaynak sozu cekirdegi agir kirma, ezme ve yikma olarak verir; duvar, yapi, dag ve cokme olaylari bu cekirdegi acar. Felaketin kisiyi dayanaksiz birakmasi ayni kirici etkiyi kisi uzerine tasiyan ozel kullanimdir, ses dalina ait degildir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kirip yikmak, sarsip bozmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"agir yikim ve kirilma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kirilip yikilmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir felaketin kisiyi sarsip gucunu kirmasi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yer cokmesi ya da yikima benzer agir olay"}],"lexicalization_note":"Mekanik tur mixed_non_bare; tanim ciplak kirma-yikma cekirdegini ve felaketli kalip kullanimini ayri tutar.","neighbor_coverage_note":"Yikim, dusme ve ses adaylari gozden gecirildi; en yakin olanlar secildi. Kus, ovgu, korkutma ve diger es sesli dallar bu siniri keskinlestirmedigi icin yayimlanmadi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda agir kirma ve yikma islemi cekirdektir; komsu dal ise yikilmanin ardindan gelen dusme, zayiflama veya itibarin gitmesi gibi sonuclara daha genis acilir.","focus_only":"Odak dal agir kirma ve cokertmeyi duvar, yapi, dag ve felaket etkisiyle verir.","gloss":"agir yikma ile dusurme","neighbor_only":"Karsi dal dusme, onurun gitmesi ve isin dagilmasi gibi sonuclari da tasir.","neighbor_ref":"root_000204/B004","relation_type":"near_synonym","shared_zone":"Ikisi de bir duzenin veya yapinin ayakta kalma halini bozan yikim alanindadir."},{"boundary_match":"partial","distinction":"Odak dal etkin kirma ve cokertme yonuyle okunur; komsu dalda ise dusme ve yikilma sonucu daha belirgin oldugundan tam yerine gecmez.","focus_only":"Odak dal kirici ve yikici etkiyi belirtir.","gloss":"yikma ile yikilma","neighbor_only":"Karsi dal seyin dusmesi veya kendiliginden yikilmasi sonucunu one cikarir.","neighbor_ref":"root_000450/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da ayakta duran bir seyin duzenini kaybetmesi bulunur."},{"boundary_match":"thematic_only","distinction":"Bu dal isitsel olayi degil, kirilip yikilma olayini anlatir; ses dalinda ise yapinin bozulmasi degil duyulan siddetli ses cekirdektir.","focus_only":"Odak dal yikimin kendisini ve yapisal kirilmayi adlandirir.","gloss":"yikim ile yikim sesi","neighbor_only":"Karsi dal yikim, gok gurlemesi veya hayvan sesi gibi duyulan siddetli sesi adlandirir.","neighbor_ref":"root_001580/B004","relation_type":"thematic","shared_zone":"Bir duvarin veya dag parcasinin dusmesi ayni sahnede hem yikim hem ses dogurabilir."}],"source_summary":"Kaynaklar dali agir kirma, yikma ve cokertme cekirdeginde birlestirir. Yapilarin yikilmasi, dagin kirilmasi, yer cokmesi ve felaketin kisiyi dayanaktan dusurmesi bu cekirdegin farkli gerceklesmeleridir."},"support_links":[]},{"boundary":"Kapsam insan icin zayiflik veya korkakliktir; fiziksel yikim ve olumlu guc nitelemesi disaridadir.","branch_kind":"mixed_non_bare","branch_ref":"root_001580/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"zayif ve korkak kisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir erkegi zayif, gucsuz veya korkak diye niteleme."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak anlatimi zayiflik ve korkakligi birlikte ya da ayri sozcuklerle verir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birini zayif gormek veya zayif saymak bu nitelemenin eylemli kullanimidir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Olumsuz kalipta kullanildiginda kisinin zayif olmadigini bildirir."}}],"root_ar":"ه د ي","root_id":"root_001580","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kisi nitelemesinde zayiflik ve korkaklik birlikte anlatilmak istendiginde en kapsayici karsiliktir.","boundary_detail":"Kapsam insan icin zayiflik veya korkakliktir; fiziksel yikim ve olumlu guc nitelemesi disaridadir.","concept_gloss":"zayif ve korkak kisi","contextual_glosses":[{"applicability":"Korkakliktan cok beden veya karakter zayifligi vurgulanan baglamlarda dogaldir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Korkaklik yonu acikca gorunmez.","preserves":"Kisiye yonelik zayiflik nitelemesi korunur."},"facet_ids":["F001"],"text":"gucsuz adam","usage_role":"contextual"},{"applicability":"Bir kisinin gucsuz goruldugu veya kucumsendigi kalip kullanim icin uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kisi sifatinin yalniz ad olarak kullanimi ve korkaklik yonu disarida kalir.","preserves":"Zayiflik yargisinin bir baskasina yonelmesi korunur."},"facet_ids":["F003"],"text":"zayif saymak","usage_role":"contextual"}],"definition":"Bu dal, erkek kisi icin zayif, korkak veya gucsuz olma nitelemesini anlatir. Birini zayif sayma ya da zayif olmadigini bildiren kaliplar bu kisi nitelemesine bagli ozel kullanimlardir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir erkegi zayif, gucsuz veya korkak diye niteleme."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak anlatimi zayiflik ve korkakligi birlikte ya da ayri sozcuklerle verir."},{"facet_id":"F003","role":"associated_use","statement":"Birini zayif gormek veya zayif saymak bu nitelemenin eylemli kullanimidir."},{"facet_id":"F004","role":"associated_use","statement":"Olumsuz kalipta kullanildiginda kisinin zayif olmadigini bildirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Maddi yikilma veya zarar gormus nesne anlami eklenir.","collision":"Yikma dalinin maddi alaniyla karisir.","fit":"displacement","loses":"Insana yonelik zayiflik ve korkaklik nitelemesi kaybolur.","preserves":"Kirilmislik benzetmesini sezdirir."},"text":"yikik"}],"identity_rationale":"Kaynak sozu dali erkek kisi icin zayiflik ve korkaklik nitelemesi olarak kurar; birini zayif sayma ve olumsuz kalipta zayif olmama da bu sinir icindedir. Bu dal, kirma-yikma cekirdeginden yalniz benzetme yoluyla uzak bir bag tasir ve ovgu dalinin gucluluk anlamiyla karistirilmamalidir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"zayif veya korkak adam"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"korkak veya zayif adam"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"korkak adam"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"korkak topluluk"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"birini zayif saymak"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"zayif olmayan"}],"lexicalization_note":"Mekanik tur mixed_non_bare; tanim kisi nitelemesini, zayif sayma kalibini ve olumsuz zayiflik kalibini ayri tutar.","neighbor_coverage_note":"Zayiflik, korkaklik, guc ve savasla ilgili adaylar karsilastirildi. Yikim, ses, kus ve diger es sesli dallar yalniz uzak kok ici ayrimlar oldugu icin secilmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal daha leksik bir kisi nitelemesi ve zayif sayma kalibi sunar; komsu dal korkunun ortaya ciktigi durum ve savas baglamina daha aciktir.","focus_only":"Odak dal erkek kisi icin ad veya sifat olarak zayif ve korkak nitelemeyi verir.","gloss":"zayiflik ile korkaklik","neighbor_only":"Karsi dal ozellikle savas ve siddet aninda gucun gitmesi, korku ve urkme alanini tasir.","neighbor_ref":"root_001157/B001","relation_type":"near_synonym","shared_zone":"Iki dalda da insanin guc ve cesaret eksikligi bulunur."},{"boundary_match":"partial","distinction":"Odak dalda korkaklik temel ayirt edici unsurdur; komsu dal bedenin incelmesi veya caresizlikle zayif dusme gibi daha somut durumlari da kapsar.","focus_only":"Odak dal korkaklikla birlikte ahlaki veya ruhsal gucsuzlugu da niteleyebilir.","gloss":"korkak zayiflik ile bitkinlik","neighbor_only":"Karsi dal zayiflikla birlikte incelme, zayif dusme ve ihtiyac yuzunden tukeniş alanlarini tasir.","neighbor_ref":"root_000908/B003","relation_type":"near_synonym","shared_zone":"Her iki dal kisi veya canli icin guc eksikligi alanina girer."},{"boundary_match":"opposed","distinction":"Bu dal guc ve cesaret eksikligini bildirirken komsu dal savas gucu, cesaret ve sert mucadele yonunde karsit kutupta durur.","focus_only":"Odak dal zayif, korkak ve gucsuz kisiyi anlatir.","gloss":"korkaklik ile cesaret","neighbor_only":"Karsi dal savasta siddet, cesaret ve guclu mucadele alanini anlatir.","neighbor_ref":"root_000079/B001","relation_type":"polarity_pair","shared_zone":"Ikisi de guc, savas ve cesaret ekseninde insan durumunu degerlendirir."}],"source_summary":"Kaynaklar dali insan icin zayiflik ve korkaklik alaninda toplar. Ayrica bir kisiyi zayif sayma ve zayif olmadigini bildiren kaliplar, cekirdek nitelemenin bagimli kullanimlari olarak durur."},"support_links":[]},{"boundary":"Kapsam ovulen erkegin cömertligi ve gucudur; genel ovgu kalibi ayri dalda kalir.","branch_kind":"mixed_non_bare","branch_ref":"root_001580/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"cömert ve guclu kisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir erkegi cömert, degerli ve guclu diye niteleme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Cömertlik, malini harcayan eli acik kisi goruntusuyle aciklanir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Guc ve dayaniklilik, ovgu sozu icinde erkegin saglamligi olarak verilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kalipli kullanimda kisi, gucu veya dayanikliligi sebebiyle ovulur."}}],"root_ar":"ه د ي","root_id":"root_001580","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Cekirdekteki olumlu kisi nitelemesini, cömertlik ve dayaniklilik eksenleriyle birlikte verir.","boundary_detail":"Kapsam ovulen erkegin cömertligi ve gucudur; genel ovgu kalibi ayri dalda kalir.","concept_gloss":"cömert ve guclu kisi","contextual_glosses":[{"applicability":"Guc, sertlik ve saglamlikla ovulen kisi baglaminda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Cömertlik ve eli aciklik yonu gorunmez.","preserves":"Guclu ve dayanikli kisi nitelemesi korunur."},"facet_ids":["F003","F004"],"text":"dayanikli adam","usage_role":"contextual"},{"applicability":"Cömertlik ve degerli kisi vurgusu one cikan baglamlarda dogaldir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gucluluk ve dayaniklilik yonu acikca gorunmez.","preserves":"Cömert ve degerli kisi nitelemesi korunur."},"facet_ids":["F001","F002"],"text":"eli acik soylu kisi","usage_role":"contextual"}],"definition":"Bu dal, erkek kisi icin cömert, soylu, guclu veya dayanikli olma nitelemesini anlatir. Birinin gucu ve sertligiyle ovulmesi, bu olumlu kisi nitelemesinin kalipli kullanimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir erkegi cömert, degerli ve guclu diye niteleme."},{"facet_id":"F002","role":"specialization","statement":"Cömertlik, malini harcayan eli acik kisi goruntusuyle aciklanir."},{"facet_id":"F003","role":"specialization","statement":"Guc ve dayaniklilik, ovgu sozu icinde erkegin saglamligi olarak verilir."},{"facet_id":"F004","role":"associated_use","statement":"Kalipli kullanimda kisi, gucu veya dayanikliligi sebebiyle ovulur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gucluluk, dayaniklilik ve ovgu kalibi eksik kalir.","preserves":"Eli aciklik ve degerli kisi yonu korunur."},"text":"sadece cömert"}],"identity_rationale":"Kaynak sozu erkek kisi icin cömertlik, asillik, gucluluk ve ovguyle anilan dayaniklilik nitelemelerini ayni dalda toplar. Bu dal zayiflik dalinin karsit nitelik alanidir; yikma veya ses anlamlariyla semantik cekirdek paylasmaz.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"cömert, degerli veya guclu adam"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"adam gucu ve dayanikliligiyla ovulmek"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"adami dayanikli diye ovmek"}],"lexicalization_note":"Mekanik tur mixed_non_bare; tanim kisi sifatini ve ovgu kalibinda guc belirtmeyi ayri ama bagli tutar.","neighbor_coverage_note":"Cömertlik, guc ve ovgu adaylari degerlendirildi. Yikim, ses ve diger kok ici dallar yalniz es sesli uzak ayrimlar sundugu icin alinmadi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal cömertligi guc ve dayaniklilikla beraber tasir; komsu dalda cömertlik belirli bir adlandirma icinde daralir.","focus_only":"Odak dal cömertligi gucluluk ve ovguyle birlikte verir.","gloss":"cömert adam ile belirli cömert tip","neighbor_only":"Karsi dal cömert kisi adina daha dar ve belirli bir kisi tipine baglidir.","neighbor_ref":"root_001326/B006","relation_type":"near_synonym","shared_zone":"Ikisi de eli acik ve degerli insan nitelemesi alanindadir."},{"boundary_match":"field_only","distinction":"Bu dal insan icin degerlendirici bir sifat alanidir; komsu dalda ise sertlesme ve kuvvetlenme daha genel dogal sureclerle ilgilidir.","focus_only":"Odak dal insani olumlu bicimde cömert ve guclu diye niteleyebilir.","gloss":"kisi gucu ile sertlesme","neighbor_only":"Karsi dal genclik, hayvan veya bitkide sertlesme ve saglamlasma alanina yayilir.","neighbor_ref":"root_000229/B007","relation_type":"same_field","shared_zone":"Her iki dalda guc, saglamlik ve dayaniklilik fikri bulunur."},{"boundary_match":"field_only","distinction":"Bu dal kisinin niteligi olarak cömertlik ve gucu verir; komsu dal ise o degeri gosteren isler ve cabalar alanina yonelir.","focus_only":"Odak dal erkegin cömert, guclu veya ovulen kisi olmasini niteleyebilir.","gloss":"cömert kisi ile erdemli isler","neighbor_only":"Karsi dal iyi isler, arabuluculuk, cömertlik ve onur arayisi gibi erdemli cabalari kapsar.","neighbor_ref":"root_000709/B006","relation_type":"same_field","shared_zone":"Ikisi de cömertlik, iyilik ve olumlu toplumsal deger alanindadir."},{"boundary_match":"field_only","distinction":"Bu dal cömertlik veya guc gibi niteligin kendisidir; komsu dal niteligi ayrintilamaz, yalniz kalipli bir ovgu sozu kurar.","focus_only":"Odak dal kisinin olumlu sifatlarini adlandirir.","gloss":"ovulen nitelik ile ovgu kalibi","neighbor_only":"Karsi dal belirli bir ovgu kalibinin yeterlik anlatimini adlandirir.","neighbor_ref":"root_001580/B007","relation_type":"same_field","shared_zone":"Her ikisi de kisi hakkinda olumlu degerlendirme yapar."}],"source_summary":"Kaynaklar dali olumlu insan nitelemesi olarak verir: cömert ve degerli kisi ile guclu, dayanikli ve ovulen kisi ayni alanda durur. Ovgu kaliplari bu sifat cekirdegine bagli kullanimlardir."},"support_links":[]},{"boundary":"Kapsam siddetli ses ve ugultudur; yikma eylemi ve kus adi ayri dallardadir.","branch_kind":"mixed_non_bare","branch_ref":"root_001580/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"siddetli ugultu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Siddetli duyulan ses, ugultu veya gurleme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Duvar, kose veya dag parcasinin dusmesinden gelen carpici ses olabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Deniz kiyisi tarafindan duyulan siddetli ugultu veya gok gurultusu olarak kullanilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kumru, erkek deve veya benzer hayvanin boguk gurlemesi icin de kullanilir."}}],"root_ar":"ه د ي","root_id":"root_001580","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sesin guclu, uzaktan duyulur ve gurleyen niteligini genel olarak karsilar.","boundary_detail":"Kapsam siddetli ses ve ugultudur; yikma eylemi ve kus adi ayri dallardadir.","concept_gloss":"siddetli ugultu","contextual_glosses":[{"applicability":"Duvar, kose veya dag parcasinin dusmesiyle duyulan ses baglaminda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deniz ugultusu, gok gurultusu ve hayvan sesi alanlari disarida kalir.","preserves":"Dusme veya yikilma kaynakli siddetli ses korunur."},"facet_ids":["F001","F002"],"text":"cokme sesi","usage_role":"contextual"},{"applicability":"Gok gurultusu veya hayvanin boguk ve guclu sesi icin dogaldir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yikilan yapiya ozgu carpma sesi ve denizden gelen ugultu daralir.","preserves":"Guclu ve titresemeli ses etkisi korunur."},"facet_ids":["F001","F003","F004"],"text":"gurleme","usage_role":"contextual"}],"definition":"Bu dal, dusme, cokme, deniz yonu, gok gurultusu veya hayvan bogazindan gelen siddetli ses, ugultu ve gurleme anlamindadir. Duyulan etki cekirdektir; yikimin kendisi veya kus adi degildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Siddetli duyulan ses, ugultu veya gurleme."},{"facet_id":"F002","role":"specialization","statement":"Duvar, kose veya dag parcasinin dusmesinden gelen carpici ses olabilir."},{"facet_id":"F003","role":"extension","statement":"Deniz kiyisi tarafindan duyulan siddetli ugultu veya gok gurultusu olarak kullanilir."},{"facet_id":"F004","role":"associated_use","statement":"Kumru, erkek deve veya benzer hayvanin boguk gurlemesi icin de kullanilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yikma ve cokertme eylemi eklenir.","collision":"Kirma-yikma daliyla karisir.","fit":"displacement","loses":"Duyulan siddetli ses cekirdegi kaybolur.","preserves":"Sesin cikabilecegi olay alanini korur."},"text":"yikim"}],"identity_rationale":"Kaynak sozu bu dali dusen duvar veya dag parcasinin sesi, deniz yonunden duyulan siddetli ugultu, gok gurultusu ve hayvan sesleri gibi isitsel olaylar etrafinda kurar. Yikimin kendisi degil, yikim veya dogal varliklardan duyulan ses cekirdektir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"duvar, kose veya dag dusmesinin siddetli sesi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"deniz tarafindan duyulan siddetli ugultu"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gok gurultusu"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ses ve ugultu"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kumru veya erkek devenin gurleyis ugultusu"}],"lexicalization_note":"Mekanik tur mixed_non_bare; tanim ciplak ses adlarini ve hayvan sesi kalibini ayni ses cekirdeginde ayirir.","neighbor_coverage_note":"Siddetli ses, yankili ses, carpma sesi ve kok ici yikim adaylari degerlendirildi. Kus adi, uyutma hareketi ve ovgu dallari yalniz ad benzerligi tasir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda dusme ve yikim kaynakli sesler belirgin bir alt alan olusturur; komsu dal daha genel yankili ve gurleyen ses ailesidir.","focus_only":"Odak dal yikilan yapi sesi, deniz ugultusu, gok gurultusu ve belirli hayvan seslerini birlikte verir.","gloss":"siddetli ugultular","neighbor_only":"Karsi dal bulut, dalga, deve ve benzeri yankili sesleri daha genel ses alaninda toplar.","neighbor_ref":"root_000543/B004","relation_type":"near_synonym","shared_zone":"Ikisi de uzaktan veya guclu bicimde duyulan titresemeli sesleri anlatir."},{"boundary_match":"partial","distinction":"Odak dal sadece carpma izine bagli degildir; komsu dal ise darbeyle olusan ses ve iz alanina daha yakindir.","focus_only":"Odak dal deniz ugultusu, gok gurultusu ve hayvan gurlemesi gibi kaynaklara da acilir.","gloss":"dusme sesi ile carpma sesi","neighbor_only":"Karsi dal darbe, yagmur, toynak ve demir gibi carpma kaynakli sesleri de icerir.","neighbor_ref":"root_001675/B004","relation_type":"near_synonym","shared_zone":"Her iki dal siddetli dusus veya carpma sonucunda duyulan sesi kapsar."},{"boundary_match":"thematic_only","distinction":"Bu dalda isitsel sonuc cekirdektir; komsu dalda ses zorunlu degil, yapisal kirilma cekirdektir.","focus_only":"Odak dal olaydan duyulan siddetli sesi anlatir.","gloss":"yikim sesi ile yikim","neighbor_only":"Karsi dal olayda gerceklesen kirma, yikma veya cokertmeyi anlatir.","neighbor_ref":"root_001580/B001","relation_type":"thematic","shared_zone":"Yikilan duvar veya dag parcasinda hem bozucu olay hem de siddetli ses bulunabilir."}],"source_summary":"Kaynaklar dali siddetli ses alaninda toplar: yikilan yapi veya dagdan cikan ses, deniz kiyisinden duyulan ugultu, gok gurultusu ve hayvan gurlemesi ayni isitsel cekirdege baglanir."},"support_links":[]},{"boundary":"Kapsam kus adidir; ses cikarma, sallama ve insan toplulugu adi disarida kalir.","branch_kind":"bare","branch_ref":"root_001580/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"ibibik kusu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bilinen ibibik kusunu adlandirma."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Benzer veya guvercine benzetilen kus adlari icin de kullanilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaynaklar tekil kus adini ve kucultmeli ya da cogul adlandirmalari birlikte verir."}}],"root_ar":"ه د ي","root_id":"root_001580","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Cekirdek kus adini dogrudan ve dogal Turkce adla karsilar.","boundary_detail":"Kapsam kus adidir; ses cikarma, sallama ve insan toplulugu adi disarida kalir.","concept_gloss":"ibibik kusu","contextual_glosses":[{"applicability":"Benzer veya ayni ad ailesine sokulan kuslar anlatildiginda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bilinen ibibik kusunun tam kendisi oldugu anlam daralir.","preserves":"Kus adi ve benzerlik alani korunur."},"facet_ids":["F002","F003"],"text":"ibibige benzer kus","usage_role":"contextual"}],"definition":"Bu dal, ibibik diye bilinen kusun adi ve ona benzetilen kimi kus adlari icindir. Anlam, kus turu veya kus adi alaninda kalir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bilinen ibibik kusunu adlandirma."},{"facet_id":"F002","role":"extension","statement":"Benzer veya guvercine benzetilen kus adlari icin de kullanilir."},{"facet_id":"F003","role":"source_variant","statement":"Kaynaklar tekil kus adini ve kucultmeli ya da cogul adlandirmalari birlikte verir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Baska bir kus turunun adi eklenir.","collision":"Benzer kus ornegi asil ad yerine gecmis olur.","fit":"displacement","loses":"Ibibik kusu cekirdegi kaybolur.","preserves":"Kus olma alanini korur."},"text":"guvercin"}],"identity_rationale":"Kaynak sozu bu dali bilinen ibibik kusu ve ona benzeyen kus adlari olarak verir. Ses, uyutma hareketi veya kabile adi bu dalin cekirdegi degildir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ibibik kusu"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ibibik veya guvercine benzetilen kus adlari"}],"lexicalization_note":"Mekanik tur bare; tanim kus adini ciplak ad olarak verir ve ses ya da hareket anlamini ithal etmez.","neighbor_coverage_note":"Kus adlari ve kok ici ses-hareket adaylari incelendi. Uzak hayvan adlari ayni alan disinda ek ayrim saglamadigi icin sinirli sayida komsu secildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalin siniri benzer kus adlarina da acilir; komsu dal daha cok ibibik adinin kendisi ve ona bagli ad bicimleriyle sinirlidir.","focus_only":"Odak dal ibibik kusu yaninda ona benzeyen kus adlarini da icerir.","gloss":"ibibik kusu adlari","neighbor_only":"Karsi dal ibibik kusu adina ve onunla iliskili adlandirmalara daha dar odaklanir.","neighbor_ref":"root_001582/B002","relation_type":"near_synonym","shared_zone":"Ikisi de bilinen ibibik kusunu adlandirma alanindadir."},{"boundary_match":"field_only","distinction":"Bu dal tek bir kus adinin etrafindadir; komsu dal ise birbirinden ayri hayvan adlarini genel bir adlandirma alaninda toplar.","focus_only":"Odak dal belirli ibibik kusu ve ona yakin kus adlarini verir.","gloss":"belirli kus adi ile hayvan adlari","neighbor_only":"Karsi dal balik ve farkli kucuk kus adlari gibi daha genis hayvan adlarini kapsar.","neighbor_ref":"root_000260/B007","relation_type":"same_field","shared_zone":"Her ikisi de hayvan veya kus adi alaninda yer alir."},{"boundary_match":"thematic_only","distinction":"Bu dal bir canliyi adlandirir; komsu dal canlinin ya da baska kaynagin cikardigi sesi adlandirir.","focus_only":"Odak dal kusun adidir.","gloss":"kus adi ile kus sesi","neighbor_only":"Karsi dal kumru veya baska hayvanlardan gelen gurleme ve ugultu sesidir.","neighbor_ref":"root_001580/B004","relation_type":"thematic","shared_zone":"Kus veya hayvan sahnesi ayni kokte ad ve ses kullanimlarini yanyana getirir."}],"source_summary":"Kaynaklar dali ibibik kusunun adi olarak paylasir. Bazi kayitlar benzer kus adlarini ve kucultmeli bicimi de ayni adlandirma alanina ekler."},"support_links":[]},{"boundary":"Kapsam cocugu uyutmak icin sallama veya hareket ettirmedir; sesle ninni ve hayvan sesi disaridadir.","branch_kind":"collocation","branch_ref":"root_001580/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"uyutmak icin sallama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Cocugu uyutmak icin onu hafifce hareket ettirme veya sallama."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem anne veya kadin tarafindan cocuga yoneltilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Uyuma sonucu hedeflenir, fakat anlam cocugun uyumasi degil uyutma hareketidir."}}],"root_ar":"ه د ي","root_id":"root_001580","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Cocugu uykuya hazirlamak icin yapilan hareketi ve amaci birlikte verir.","boundary_detail":"Kapsam cocugu uyutmak icin sallama veya hareket ettirmedir; sesle ninni ve hayvan sesi disaridadir.","concept_gloss":"uyutmak icin sallama","contextual_glosses":[{"applicability":"Turkce akista eylemin nesnesi cocuk oldugunda dogal ve acik bir karsiliktir.","error_profile":{"adds":"Ifade cocugun gercekten uyudugu sonucunu cagristirabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Cocuga yonelik sallama ve uyutma amaci korunur."},"facet_ids":["F001","F003"],"text":"cocugu sallayip uyutmak","usage_role":"contextual"}],"definition":"Bu dal, bir kadinin, annenin veya bakicinin cocugu uyusun diye onu sallayip hareket ettirmesi anlamindadir. Uyutma amaci kurucudur; yalniz ses cikarma anlamina genisletilmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Cocugu uyutmak icin onu hafifce hareket ettirme veya sallama."},{"facet_id":"F002","role":"specialization","statement":"Eylem anne veya kadin tarafindan cocuga yoneltilir."},{"facet_id":"F003","role":"associated_use","statement":"Uyuma sonucu hedeflenir, fakat anlam cocugun uyumasi degil uyutma hareketidir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sesli soyleme eylemi eklenir.","collision":"Sesle uyutma komsusu ile karisir.","fit":"displacement","loses":"Cocugu hareket ettirme ve sallama cekirdegi kaybolur.","preserves":"Uyutma amacini korur."},"text":"ninni soylemek"}],"identity_rationale":"Kaynak sozu kadinin veya annenin cocugu uyusun diye hareket ettirmesini verir. Sesle uyutma veya hayvan gurlemesi bu dalda kaynak cekirdegi degildir; tanim hareket ve uyutma amaciyla sinirlanmalidir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"cocugu uyusun diye sallamak"}],"lexicalization_note":"Mekanik tur collocation; tanim yalniz cocugu uyutmak icin hareket ettirme yapisina baglidir.","neighbor_coverage_note":"Uyutma, anne-cocuk bakimi, uyku yeri ve ses adaylari degerlendirildi. Uzak yikim, kus, ovgu ve korkutma dallari yayimli ayrim icin gerekli gorulmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda kurucu unsur hareket ettirmedir; komsu dalda uyutma araci sestir, bu yuzden birbirinin yerine dogrudan gecmez.","focus_only":"Odak dal cocugu bedensel olarak hareket ettirme veya sallamadir.","gloss":"sallayarak uyutma ile sesle uyutma","neighbor_only":"Karsi dal cocugu ince ve yumusak sesle uyutma alanidir.","neighbor_ref":"root_001602/B009","relation_type":"near_neighbor","shared_zone":"Ikisi de cocugu uyutmaya yonelik bakim eylemidir."},{"boundary_match":"thematic_only","distinction":"Bu dal hareketi anlatir; komsu dal uyumanin gerceklestigi hazir yeri adlandirir.","focus_only":"Odak dal cocuk uzerinde yapilan uyutma hareketidir.","gloss":"sallama eylemi ile uyku yeri","neighbor_only":"Karsi dal cocugun yatmasi icin hazirlanan yer veya besiktir.","neighbor_ref":"root_001451/B001","relation_type":"thematic","shared_zone":"Ikisi de cocugun uykuya hazirlanmasi sahnesindedir."},{"boundary_match":"thematic_only","distinction":"Bu dalda ses kurucu degildir; komsu dalda ise hareket degil duyulan ugultu ve gurleme cekirdektir.","focus_only":"Odak dal cocugu uyutmak icin hareket ettirmedir.","gloss":"uyutma hareketi ile ses","neighbor_only":"Karsi dal hayvan veya yikim kaynakli siddetli sestir.","neighbor_ref":"root_001580/B004","relation_type":"thematic","shared_zone":"Ayni kokte hareket ve ses kullanimlari bicimce yakindir."}],"source_summary":"Kaynaklar dali cocugu uyutma amaciyla hareket ettirme anlaminda birlestirir. Hareketi yapan kisi anne veya kadin olarak gosterilir; anlam sesli uyutmaya degil bedensel sallamaya baglidir."},"support_links":[]},{"boundary":"Kapsam yalniz kalipli ovgu ifadesidir; ciplak cömertlik, guc ve yikim anlamlari disaridadir.","branch_kind":"non_bare","branch_ref":"root_001580/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"ovgu yeterlik kalibi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir erkegi yeter derecede ovmeye yarayan kalipli soz."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalip, 'ona yeter' veya 'ustune yok' degerinde olumlu yargı kurar."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yorum, ovulen kisinin iyi yanlarini saymanin agirligina bagli aciklama verir."}}],"root_ar":"ه د ي","root_id":"root_001580","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli soz dizisinin bir kisiyi yeterli derecede ovme islevini kisa bicimde anlatir.","boundary_detail":"Kapsam yalniz kalipli ovgu ifadesidir; ciplak cömertlik, guc ve yikim anlamlari disaridadir.","concept_gloss":"ovgu yeterlik kalibi","contextual_glosses":[{"applicability":"Bir kisiyi yeterli ve ustun gostererek ovme baglaminda dogal Turkce karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Erkek kisiye bagli ozel kalip bicimi acik kalmaz.","preserves":"Yeterlik uzerinden ovme islevi korunur."},"facet_ids":["F001","F002"],"text":"ona diyecek yok","usage_role":"contextual"},{"applicability":"Akici ceviride hayranlik ve ovgu vurgusunu vermek icin kullanilabilir.","error_profile":{"adds":"Modern unlem tonu ve hayranlik derecesi eklenebilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Erkek kisiye yonelik guclu ovgu korunur."},"facet_ids":["F001","F002"],"text":"ne adam ama","usage_role":"contextual"}],"definition":"Bu dal, bir erkek hakkinda 'ona diyecek yok, ne iyi adam' degerinde kullanilan kalipli ovgu sozudur. Anlam, kisinin niteliginin kendisi degil, o kisiyi yeter derecede ovme kalibidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir erkegi yeter derecede ovmeye yarayan kalipli soz."},{"facet_id":"F002","role":"specialization","statement":"Kalip, 'ona yeter' veya 'ustune yok' degerinde olumlu yargı kurar."},{"facet_id":"F003","role":"source_variant","statement":"Bir yorum, ovulen kisinin iyi yanlarini saymanin agirligina bagli aciklama verir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Cömertlik niteliginin kendisi eklenir.","collision":"Cömert ve guclu kisi daliyla karisir.","fit":"displacement","loses":"Kalipli yeterlik sozu ve ifade islevi kaybolur.","preserves":"Ovguyle iliskili olumlu kisi degerini korur."},"text":"cömert adam"}],"identity_rationale":"Kaynak sozu belirli bir ovgu kalibinin 'ona yetisir, ne kadar iyi adam' degerinde kullanildigini bildirir. Bu dal kisinin cömert veya guclu olmasini dogrudan adlandirmaz; o niteliklere yonelen kalipli ovgu sozunu adlandirir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bir erkegi 'ona diyecek yok' anlaminda oven kalip"}],"lexicalization_note":"Mekanik tur non_bare; tanim korunmus ovgu kalibina baglidir ve ciplak kok anlami gibi genisletilmez.","neighbor_coverage_note":"Ovgu kalibi, genel ovme ve olumlu kisi niteligi adaylari secildi. Diger kok ici dallar yalniz es sesli uzak ayrimlar oldugundan yayimlanmadi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Supplied cards show the same pragmatic function: bir kisiyi 'ona yeter, ustune yok' degeriyle ovme. Bu nedenle sinir farki yayimlanacak duzeyde degildir.","focus_only":null,"gloss":"ovgu yeterlik kalibi","neighbor_only":null,"neighbor_ref":"root_001602/B013","relation_type":"synonym","shared_zone":"Iki dal da bir erkek hakkinda yeterlik degerinde kalipli ovgu sozu kurar."},{"boundary_match":"field_only","distinction":"Bu dal belirli soz kalibinin anlamidir; komsu dal ovme eyleminin genel ve yinelenen bicimini anlatir.","focus_only":"Odak dal tek kalipla yeterlik ve ustunluk ovgusu kurar.","gloss":"kalipli ovgu ile ovme eylemi","neighbor_only":"Karsi dal kisinin iyi yanlarini tekrar tekrar anma ve ovme eylemidir.","neighbor_ref":"root_000208/B010","relation_type":"same_field","shared_zone":"Her ikisi de kisi hakkinda olumlu soz soyleme alanindadir."},{"boundary_match":"field_only","distinction":"Bu dal tek bir yeterlik ovgusu kalibina dardir; komsu dal farkli ovgu ve begeni kaliplarini daha genis bicimde kapsar.","focus_only":"Odak dal bir erkek icin yeterlik degerinde belirli ovgu kalibidir.","gloss":"belirli ovgu kalibi ile genel ovgu kaliplari","neighbor_only":"Karsi dal genel ovgu, begeni ve istek bildirilen daha genis kaliplar alanidir.","neighbor_ref":"root_000286/B003","relation_type":"same_field","shared_zone":"Ikisi de kalipli soyleyisle olumlu degerlendirme kurar."}],"source_summary":"Kaynaklar dali kalipli bir ovgu sozu olarak birlestirir: bir erkekten soz ederken 'ona yeter, ustune yok' degerinde olumlu yargı kurar. Bir aciklama bu ovgunun kisinin iyi yanlarini saymaya dayandigini belirtir."},"support_links":[]},{"boundary":"Kapsam yuruyuste yere sert basmadir; genel agirlik, yikim ve adim sesi disaridadir.","branch_kind":"collocation","branch_ref":"root_001580/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"agir basarak yurume","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yururken zemine agir ve sert bicimde basma."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem kisinin yuruyus tarzi olarak anlatilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yerin etkilenmesi vurgulanir, fakat cekirdek yuruyuste basma eylemidir."}}],"root_ar":"ه د ي","root_id":"root_001580","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yuruyus sirasinda zemine sert ve yuk bindiren basma hareketini dogal bicimde verir.","boundary_detail":"Kapsam yuruyuste yere sert basmadir; genel agirlik, yikim ve adim sesi disaridadir.","concept_gloss":"agir basarak yurume","contextual_glosses":[{"applicability":"Yuruyusun kendisi zaten baglamda belliyse daha kisa ve akici karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yuruyus sirasinda olma kosulu acikca gorunmez.","preserves":"Zemine sert basma etkisi korunur."},"facet_ids":["F001","F003"],"text":"yere sert basmak","usage_role":"contextual"}],"definition":"Bu dal, bir kisinin yuruyusu sirasinda yere agir ve sert basmasi anlamindadir. Anlam zemine basma eylemine baglidir; yalniz ses cikarma veya yikma sonucu degildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yururken zemine agir ve sert bicimde basma."},{"facet_id":"F002","role":"specialization","statement":"Eylem kisinin yuruyus tarzi olarak anlatilir."},{"facet_id":"F003","role":"associated_use","statement":"Yerin etkilenmesi vurgulanir, fakat cekirdek yuruyuste basma eylemidir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Duyulan ses anlamini ekler.","collision":"Siddetli ses daliyla karisir.","fit":"displacement","loses":"Yere basma eylemi ve yuruyus tarzi kaybolur.","preserves":"Sert basmanin dogurabilecegi isitsel sonucu korur."},"text":"adim sesi"}],"identity_rationale":"Kaynak sozu tek kalipta, birinin yururken yere cok sert basmasini anlatir. Bu dal agirlik etkisini hareket ve yerle temas uzerinden kurar; yikim, ses veya korkutma alanlarina genisletilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yururken yere cok sert basmak"}],"lexicalization_note":"Mekanik tur collocation; tanim yalniz yururken yeri sert bicimde basma yapisina baglidir.","neighbor_coverage_note":"Yere temas, yuruyus, ayak vurusu ve adim sesi adaylari degerlendirildi. Yikim ve kok ici uzak dallar yalniz bicimsel yakinlik tasidigi icin secilmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yuruyusun sert basma niteligine dardir; komsu dal yerin icinden gecme veya dolasma eylemine daha genis acilir.","focus_only":"Odak dal yuruyuste yere agir ve sert basmayi anlatir.","gloss":"sert basma ile dolasip cigneyis","neighbor_only":"Karsi dal bir yeri dolasma, icine girme, cigneyip gecme ve basip dolasma alanini tasir.","neighbor_ref":"root_000277/B003","relation_type":"near_neighbor","shared_zone":"Ikisi de yerle ayak veya hareket temasini icerir."},{"boundary_match":"field_only","distinction":"Odak dal yurumeye bagli basma tarzidir; komsu dal ayak ve bacakla yapilan vurma veya hareketlerin genel alanidir.","focus_only":"Odak dal yuruyus sirasinda agir basmayi belirtir.","gloss":"agir yuruyus ile ayak vurusu","neighbor_only":"Karsi dal ayagin vurmasi, ayakla binite vurma ve genel ayak hareketlerini kapsar.","neighbor_ref":"root_000593/B001","relation_type":"same_field","shared_zone":"Her iki dalda ayakla yere veya bir nesneye temas vardir."},{"boundary_match":"partial","distinction":"Bu dal hareket ve temas tarzidir; komsu dal o temas sonucunda duyulan sesi cekirdek yapar.","focus_only":"Odak dal zemine sert basma eylemini anlatir.","gloss":"sert basma ile basma sesi","neighbor_only":"Karsi dal ozellikle agir basistan duyulan siddetli sesi anlatir.","neighbor_ref":"root_001615/B003","relation_type":"near_neighbor","shared_zone":"Sert ayak basisi ayni sahnede hem hareket hem ses uretebilir."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Kullanim, kisinin yuruyuste yere cok sert basmasiyla sinirlidir."}],"source_summary":"Ortak cok kaynakli sentez yoktur; dal tek kayittaki kalipli yuruyus anlatimina dayanir. Bu kayit, kisinin yururken zemine agir ve sert basmasiyla sinirlidir."},"support_links":[]},{"boundary":"Kapsam sarp inisli tepe veya zor gecittir; genel daglik alan ve yikilma olayi disaridadir.","branch_kind":"bare","branch_ref":"root_001580/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"sarp inisli gecit","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Inisi zor ve sarp olan arazi cikintisi veya gecit."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tepe veya yokus gibi yuksek arazi bicimi olabilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Develerin boyle yerden yuvarlanmasi zorluk ve tehlike ornegidir."}}],"root_ar":"ه د ي","root_id":"root_001580","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zorlu gecis ve inis kosulunu birlikte karsilar.","boundary_detail":"Kapsam sarp inisli tepe veya zor gecittir; genel daglik alan ve yikilma olayi disaridadir.","concept_gloss":"sarp inisli gecit","contextual_glosses":[{"applicability":"Tepe veya yokus niteligindeki arazi baglaminda dogal Turkce karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Inisin ozellikle sarp ve tehlikeli olmasi tam acilmaz.","preserves":"Zorlu arazi ve egim fikri korunur."},"facet_ids":["F001","F002"],"text":"zorlu yokus","usage_role":"contextual"}],"definition":"Bu dal, inisi zor, sarp ve gecisi zahmetli tepe, yokus veya gecit anlamindadir. Tehlike, uzerinden inen canlinin yuvarlanabilecek kadar zor bir arazi olmasindan gelir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Inisi zor ve sarp olan arazi cikintisi veya gecit."},{"facet_id":"F002","role":"specialization","statement":"Tepe veya yokus gibi yuksek arazi bicimi olabilir."},{"facet_id":"F003","role":"example","statement":"Develerin boyle yerden yuvarlanmasi zorluk ve tehlike ornegidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Genel dag anlamini ekleyerek gecit ve sarp inis kosulunu belirsizlestirir.","collision":null,"fit":"broadening","loses":null,"preserves":"Yuksek arazi fikrini korur."},"text":"dag"}],"identity_rationale":"Kaynak sozu dali inisi zor ve sarp olan tepe ya da gecit olarak verir; develerin oradan yuvarlanabilmesi orneklenen tehlikedir. Anlam kisi zayifligi, yikim veya ses degil, arazinin zorlu inis niteligidir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"sarp inisli tepe veya zorlu gecit"}],"lexicalization_note":"Mekanik tur bare; tanim ciplak arazi adini korur ve hareket ya da yikim anlamini eklemez.","neighbor_coverage_note":"Sarp gecit, inis, engebeli arazi ve duzluk adaylari karsilastirildi. Kok ici yikim, ses ve yuruyus dallari semantik siniri keskinlestirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda zor inis belirginlestirilir; komsu dal sarp gecit ve tepe alanini daha genel zorluk adlariyla verir.","focus_only":"Odak dal inisi zor tepe veya gecitte yuvarlanma tehlikesini ozellikle sezdirir.","gloss":"sarp gecitler","neighbor_only":"Karsi dal zorlu tepe ve gecit adlarini baska arazi adlariyla genisletir.","neighbor_ref":"root_001051/B005","relation_type":"near_synonym","shared_zone":"Ikisi de gecisi zor, sarp arazi veya gecit anlam alanindadir."},{"boundary_match":"partial","distinction":"Bu dal belirli olarak zor inisli tepe veya gecittir; komsu dal engebeli ve cikintili yerleri daha genis bicimde toplar.","focus_only":"Odak dal tepe veya gecidin sarp inisine odaklanir.","gloss":"sarp gecit ile engebeli cikinti","neighbor_only":"Karsi dal dag yolu, cikinti kaya, kuyu ici tas ve yapi cikintisi gibi daha genis engebeleri kapsar.","neighbor_ref":"root_001033/B012","relation_type":"near_synonym","shared_zone":"Her iki dal zor gecilen veya yukselen arazi bicimleriyle ilgilidir."},{"boundary_match":"partial","distinction":"Odak dalda zorluk ve tehlike kurucudur; komsu dalda sadece inis veya alcaliş bulunabilir.","focus_only":"Odak dal inisin sarp ve zahmetli olmasini sart kosar.","gloss":"sarp inis ile genel inis","neighbor_only":"Karsi dal yol, yer veya su icin genel inis ve alcaliş alanini anlatir.","neighbor_ref":"root_000838/B002","relation_type":"near_neighbor","shared_zone":"Ikisi de egim ve asagi yonlu arazi hareketiyle ilgilidir."},{"boundary_match":"opposed","distinction":"Bu dal zorlu ve sarp gecise, komsu dal ise kolay veya duz zemine yonelir; arazi niteligi bakimindan karsitlik kurarlar.","focus_only":"Odak dal sarp, zor ve tehlikeli araziyi anlatir.","gloss":"sarp arazi ile kolay duzluk","neighbor_only":"Karsi dal duz, kolay, alcak veya engebesiz araziyi anlatir.","neighbor_ref":"root_001544/B007","relation_type":"polarity_pair","shared_zone":"Ikisi de arazinin gecilebilirlik ve engebe niteligini degerlendirir."}],"source_summary":"Kaynaklar dali sarp, inisi zor ve zahmetli arazi olarak verir. Bir anlatim bu zorlugu, develerin oradan yuvarlanabilmesiyle ornekler."},"support_links":[]},{"boundary":"Kapsam korkutma ve gozdagi vermedir; salt korku hali, ses ve yikim disaridadir.","branch_kind":"bare","branch_ref":"root_001580/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"gozdagi vererek korkutma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birini korkutmak icin zarar veya kotuluk ihtimali bildirme."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Korkutma ve gozdagi verme ayni dal icinde birlikte verilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Uzaktan veya dolayli bicimde savrulan korkutucu soz de bu alandadir."}}],"root_ar":"ه د ي","root_id":"root_001580","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zarar ihtimali bildirip baskasinda korku uyandirma cekirdegini acik bicimde karsilar.","boundary_detail":"Kapsam korkutma ve gozdagi vermedir; salt korku hali, ses ve yikim disaridadir.","concept_gloss":"gozdagi vererek korkutma","contextual_glosses":[{"applicability":"Zarar tehdidi ayrintisi baglamdan anlasiliyorsa en sade akici karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gozdagi ve kotuluk bildiren soz yonu acikca gorunmez.","preserves":"Baskasinda korku uyandirma korunur."},"facet_ids":["F001"],"text":"korkutmak","usage_role":"general"},{"applicability":"Dolayli veya uzak mesafeden gelen korkutucu soz baglaminda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel korkutma adlari disarida kalir.","preserves":"Uzaktan gelen korkutucu soz ve gozdagi korunur."},"facet_ids":["F003"],"text":"uzaktan gozdagi savurmak","usage_role":"contextual"}],"definition":"Bu dal, birine zarar veya kotuluk gelecegini sezdirerek korkutma ve gozdagi verme anlamindadir. Uzaktan veya dolayli savrulan korkutucu sozler de bu alana baglanir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birini korkutmak icin zarar veya kotuluk ihtimali bildirme."},{"facet_id":"F002","role":"source_variant","statement":"Korkutma ve gozdagi verme ayni dal icinde birlikte verilir."},{"facet_id":"F003","role":"associated_use","statement":"Uzaktan veya dolayli bicimde savrulan korkutucu soz de bu alandadir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Korkuyu yasayan kisinin ic hali eklenir.","collision":"Salt korku ve urkme dallariyla karisir.","fit":"displacement","loses":"Baskasini korkutma ve gozdagi verme eylemi kaybolur.","preserves":"Korku alanini korur."},"text":"korku"}],"identity_rationale":"Kaynak sozu dali korkutma, gozdagi verme ve uzaktan savrulan kotu soz alaninda kurar. Bu dal ses, yikim veya ovgu degildir; alicida korku dogurmayi hedefleyen sozlu tutum cekirdektir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"gozdagi verme ve korkutma"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"korkutma ve gozdagi verme"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"gozdagi verme"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"uzaktan savrulan gozdagi"}],"lexicalization_note":"Mekanik tur bare; tanim genel korkutma ve gozdagi cekirdegini verir, belirli kaliba baglamaz.","neighbor_coverage_note":"Korkutma, uyari, korku hali ve gosterisli gozdagi adaylari degerlendirildi. Ses ve yikim dallari yalniz bicimsel yakinlik tasidigi icin secilmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal daha genel korkutma ve dolayli gozdagi alanini verir; komsu dal zarar turu ve kotuluk yonelimiyle daha belirgin sinirlanir.","focus_only":"Odak dal genel korkutma, gozdagi ve uzaktan savrulan korkutucu sozu kapsar.","gloss":"gozdagi verme","neighbor_only":"Karsi dal kotuluk veya dayak gibi belirli zarar yonelimli gozdagi alanini daha acik tasir.","neighbor_ref":"root_001662/B002","relation_type":"near_synonym","shared_zone":"Ikisi de baskasina kotu bir sonuc sezdirerek korkutma alanindadir."},{"boundary_match":"partial","distinction":"Bu dal gozdagi vererek korkutur; komsu dalda amac her zaman gozdagi degil, tehlikeden sakindirma veya uyarmadir.","focus_only":"Odak dal korkutucu sozle baski kurar.","gloss":"korkutma ile uyari","neighbor_only":"Karsi dal uyari, sakindirma ve dikkatli olmaya cagirma islevini de kapsar.","neighbor_ref":"root_000301/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal baskasinda cekinme veya dikkat dogurabilir."},{"boundary_match":"partial","distinction":"Bu dal korku uyandiran eyleme aittir; komsu dal korkunun kendisi ve korkuyla olusan durumlara daha genistir.","focus_only":"Odak dal korkuyu dogurmak icin soylenen veya yapilan gozdagidir.","gloss":"korkutma ile korku hali","neighbor_only":"Karsi dal korku ve panik halini, korkakligi ve urkutulme sonucunu da kapsar.","neighbor_ref":"root_000572/B001","relation_type":"near_neighbor","shared_zone":"Ikisi de korku alaninda bulusur."},{"boundary_match":"partial","distinction":"Bu dal korkutma adinin kendisidir; komsu dal korkutmayi gosterisli dogal isaretler gibi davranma imgesiyle kurar.","focus_only":"Odak dal korkutma anlamini dogrudan verir.","gloss":"dogrudan gozdagi ile gosterisli gozdagi","neighbor_only":"Karsi dal simsek ve gok gurultusu imgesiyle sert gozdagi gostermeyi anlatir.","neighbor_ref":"root_000108/B003","relation_type":"near_neighbor","shared_zone":"Ikisi de sert korkutma veya gozdagi verme alanindadir."}],"source_summary":"Kaynaklar dali korkutma ve gozdagi verme alaninda birlestirir. Bir kayit, uzaktan veya dolayli bicimde savrulan korkutucu sozu de ayni alana baglar."},"support_links":[]},{"boundary":"Kapsam zihinde beliren kesinlesmemis sanidir; kanitli bilgi ve acik gorunme disaridadir.","branch_kind":"collocation","branch_ref":"root_001580/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"kesinlesmemis sani","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir dusuncenin kisi icinde kesin olmayan sani olarak belirmesi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Beliren sey kanitlanmis veya sabitlenmis degildir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Benzetme veya tasavvur zihinde kalir, kesin hukum haline getirilmez."}}],"root_ar":"ه د ي","root_id":"root_001580","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zihinde beliren ama kanitlanmayan ve sabitlenmeyen yargi adayini karsilar.","boundary_detail":"Kapsam zihinde beliren kesinlesmemis sanidir; kanitli bilgi ve acik gorunme disaridadir.","concept_gloss":"kesinlesmemis sani","contextual_glosses":[{"applicability":"Kesin yargi kurmadan zihne dogan belirsiz dusunceyi akici Turkceyle verir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ic belirme, kesin olmama ve sani niteligini korur."},"facet_ids":["F001","F002"],"text":"icine oyle gelir gibi olmak","usage_role":"contextual"}],"definition":"Bu dal, bir seyin kisinin icinde sani gibi belirmesi, fakat onun kesinlestirilmemesi ve sabit bir benzetme yargisina baglanmamasi anlamindadir. Anlam, belirsiz zihinsel yoklama ile sinirlidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir dusuncenin kisi icinde kesin olmayan sani olarak belirmesi."},{"facet_id":"F002","role":"specialization","statement":"Beliren sey kanitlanmis veya sabitlenmis degildir."},{"facet_id":"F003","role":"specialization","statement":"Benzetme veya tasavvur zihinde kalir, kesin hukum haline getirilmez."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kanitli kesin bilgi anlami eklenir.","collision":"Acik bilgi ve ortaya cikma alanlariyla karisir.","fit":"displacement","loses":"Kesinlesmemis sani ve sabitlenmemislik kaybolur.","preserves":"Zihinsel yargi alanini korur."},"text":"bilmek"}],"identity_rationale":"Kaynak sozu, bir seyin kisinin icinde sani yoluyla belirmesini fakat onun kesinlestirilmemesini ve sabit bir benzetmeye baglanmamasini anlatir. Bu dal kesin bilgi, acik ortaya cikma veya yerlesmis inanc degildir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kisinin icine kesinlesmemis bir sani gibi belirmek"}],"lexicalization_note":"Mekanik tur collocation; tanim yalniz kisiye icten beliren kesinlesmemis sani yapisina baglidir.","neighbor_coverage_note":"Sani, tahmin, kusku ve acik belirme adaylari degerlendirildi. Kok ici yikim, ses, kus ve ovgu dallari anlamsal sinir icin yararli olmadigindan secilmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda dusunce icte belirir ama baglayici hale gelmez; komsu dal sanma ve hesap etmeyi daha genel bir eylem olarak verir.","focus_only":"Odak dal saninin kisinin icinde belirmesini ve sabitlenmemesini sart kosar.","gloss":"beliren sani ile genel sanma","neighbor_only":"Karsi dal genel sanma, tahmin etme ve zihinde deger bicme alanini daha genis kapsar.","neighbor_ref":"root_000318/B002","relation_type":"near_synonym","shared_zone":"Ikisi de kesin bilgi olmayan zihinsel yargi alanindadir."},{"boundary_match":"partial","distinction":"Bu dal zihinsel belirme surecidir; komsu dal tahminin soz halinde ortaya konmasina daha yakindir.","focus_only":"Odak dal kisinin icinde beliren ve kanitlanmayan sezgiye dardir.","gloss":"ic sanı ile tahmini soz","neighbor_only":"Karsi dal bilinmeyen hakkinda tahminle soz soyleme ve kesin olmayan iddiayi kapsar.","neighbor_ref":"root_000547/B004","relation_type":"near_synonym","shared_zone":"Her iki dal kesin bilgiye dayanmayan tahmin alanindadir."},{"boundary_match":"partial","distinction":"Bu dalda bir icerik zihinde belirir; komsu dalda karar verememe veya kusku hali cekirdektir.","focus_only":"Odak dal kesinlesmemis bir benzetme veya saninin belirmesidir.","gloss":"sani ile kusku","neighbor_only":"Karsi dal kararsizlik, kusku ve tereddut halini anlatir.","neighbor_ref":"root_001416/B004","relation_type":"near_neighbor","shared_zone":"Ikisi de kesinlikten uzak zihinsel durumlar alanindadir."},{"boundary_match":"opposed","distinction":"Bu dal kesinlikten uzak ic sezdirme alanindadir; komsu dal aciklik ve belirgin bilgi yonunde karsit kutupta durur.","focus_only":"Odak dal kesinlesmeyen ve icte kalan saniyi anlatir.","gloss":"belirsiz sani ile acik belirme","neighbor_only":"Karsi dal seyin acikca ortaya cikmasi ve belirginlesmesini anlatir.","neighbor_ref":"root_000170/B004","relation_type":"polarity_pair","shared_zone":"Ikisi de bir seyin zihne veya goruse gelmesi ekseninde karsilastirilabilir."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Kullanim, kisinin icinde kesinlesmemis bir saninin belirmesini anlatir."}],"source_summary":"Ortak cok kaynakli sentez yoktur; dal tek kayittaki zihinsel belirme anlatimina dayanir. Kullanim, kesinlestirilmemis ve baglayici benzetme haline getirilmemis saniyla sinirlidir."},"support_links":[]},{"boundary":"Kapsam uzun boylu adamdir; genel yukseklik, kisa boy ve baska beden kusurlari disaridadir.","branch_kind":"bare","branch_ref":"root_001580/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"uzun boylu adam","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Erkek kisiyi uzun boylu diye niteleme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nitelik yalniz beden boyuna iliskindir, ahlaki veya guc degeri tasimaz."}}],"root_ar":"ه د ي","root_id":"root_001580","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Erkek kisiye yonelik beden boyu nitelemesini dogrudan karsilar.","boundary_detail":"Kapsam uzun boylu adamdir; genel yukseklik, kisa boy ve baska beden kusurlari disaridadir.","concept_gloss":"uzun boylu adam","contextual_glosses":[{"applicability":"Erkek kisi oldugu baglamda kisa ve dogal karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Erkek kisi oldugu acikca belirtilmez.","preserves":"Uzun boy nitelemesi korunur."},"facet_ids":["F001"],"text":"uzun adam","usage_role":"contextual"}],"definition":"Bu dal, erkek kisi icin uzun boylu olma nitelemesidir. Kapsam beden boyuna daralir; guc, ovgu, ses veya yikim anlamlari buna katilmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Erkek kisiyi uzun boylu diye niteleme."},{"facet_id":"F002","role":"specialization","statement":"Nitelik yalniz beden boyuna iliskindir, ahlaki veya guc degeri tasimaz."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"En, hacim veya guc iriligi anlamini ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Bedensel buyukluk izlenimini korur."},"text":"iri adam"}],"identity_rationale":"Kaynak sozu tek kayitta bu dali uzun boylu erkek kisi olarak verir. Anlam, yikim, ses veya korkutma alanina degil, beden boyu nitelemesine aittir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"uzun boylu adam"}],"lexicalization_note":"Mekanik tur bare; tanim ciplak kisi nitelemesini verir ve baska kok ici anlamlari eklemez.","neighbor_coverage_note":"Uzunluk, kisa boy, beden yapisi ve belirgin yukseklik adaylari degerlendirildi. Kok ici ses, yikim ve korkutma dallari anlamsal iliski kurmadigi icin secilmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal tek kisi sifatidir; komsu dal boyun olcusu ve beden durusu hakkinda daha genis bir adlandirma alanina sahiptir.","focus_only":"Odak dal erkek kisi icin yalniz uzun boy nitelemesidir.","gloss":"uzun adam ile boy yapisi","neighbor_only":"Karsi dal boy olcusu, beden durusu ve duzgun boy gibi daha genis beden yapisini kapsar.","neighbor_ref":"root_001273/B011","relation_type":"near_synonym","shared_zone":"Ikisi de insan bedeninin boy ve diklik niteligini anlatir."},{"boundary_match":"partial","distinction":"Odak dal yalniz insana ve boya dardir; komsu dal bitki ve baska varliklarda belirgin yukseklik alanina genisler.","focus_only":"Odak dal uzun boylu erkek kisiyi anlatir.","gloss":"uzun adam ile belirgin yukseklik","neighbor_only":"Karsi dal cevresinden yuksege cikan agac veya uzun kisi gibi belirgin yukseklikleri kapsar.","neighbor_ref":"root_000945/B012","relation_type":"near_synonym","shared_zone":"Her iki dal uzunluk veya cevresinden yuksekte olma izlenimi verir."},{"boundary_match":"opposed","distinction":"Bu dal uzunluk ucunda durur; komsu dal ayni olcu ekseninin kisa boy ucunu bildirir.","focus_only":"Odak dal uzun boylu erkegi anlatir.","gloss":"uzun boy ile kisa boy","neighbor_only":"Karsi dal kisa boylu olma ve kisa yapilma alanini anlatir.","neighbor_ref":"root_001231/B001","relation_type":"polarity_pair","shared_zone":"Ikisi de beden veya nesne boyunun uzunluk eksenindedir."},{"boundary_match":"field_only","distinction":"Bu dal insan icin kullanilan dar bir sifatken komsu dal canli ve bitkilerde uzun govde adlandirmalarina acilir.","focus_only":"Odak dal erkek kisiye yonelik uzun boy sifatidir.","gloss":"insan boyu ile hayvan ve agac boyu","neighbor_only":"Karsi dal hurma agaci, esek veya baska hayvanlarda uzun boyluluk adlarini kapsar.","neighbor_ref":"root_000683/B003","relation_type":"same_field","shared_zone":"Her iki dal uzun boy veya yuksek govde nitelemesi alanindadir."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek kayit, kelimeyi uzun boylu erkek kisi icin verir."}],"source_summary":"Ortak cok kaynakli sentez yoktur; dal tek kayitta uzun boylu erkek kisi nitelemesi olarak durur. Kayit baska bir bedensel veya ahlaki nitelik eklemez."},"support_links":[]},{"boundary":"Dal, sıradan bir armağanı ya da yalnızca yolun kendisini değil, doğru yönü bildirme ve ona yönelme ilişkisini anlatır.","branch_kind":"bare","branch_ref":"root_001583/B001","candidate_links":[{"candidate_id":"cand_9d574cf3d66e6f969ffd","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"doğru yolu gösterme ve doğruya yönelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğru yönü, yolu veya gerçeği incelikle göstermek, açıklamak ve tanıtmaktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gösterilen doğru yönü isteyerek kabul etme ve ona ulaşma sürecini de kapsar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dinsel doğruya yöneltme ve bu yönelişi mümkün kılan ilahi başarı desteği özel bir gerçekleşmedir."}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yolun veya gerçeğin bildirilmesiyle başlayıp gösterilen doğru yönün benimsenmesine uzanan bütün çekirdek için uygundur.","boundary_detail":"Dal, sıradan bir armağanı ya da yalnızca yolun kendisini değil, doğru yönü bildirme ve ona yönelme ilişkisini anlatır.","branch_image_ar":"دلالة بلطف إلى الطريق والحق","concept_gloss":"doğru yolu gösterme ve doğruya yönelme","contextual_glosses":[{"applicability":"Bir kişiye somut ya da düşünsel bir yolun tanıtıldığı geçişlerde doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gösterileni benimseme ve ilahi başarı desteği yönlerini tek başına anlatmaz.","preserves":"Yolu bildirme ve kişiyi doğru yöne sevk etme yönünü korur."},"facet_ids":["F001"],"text":"yolu göstermek","usage_role":"contextual"},{"applicability":"Gösterilen yönü kabul edip doğruya ulaşan kişinin durumunu anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasının yolu gösterme eylemini ve ilahi başarı desteğini belirtmez.","preserves":"Doğru yönü benimseyerek ona ulaşma sonucunu açıkça korur."},"facet_ids":["F002"],"text":"doğru yolu bulmak","usage_role":"contextual"}],"definition":"Bir kimseye yolu, doğruyu ya da benimsenmesi gereken yönü incelikle göstermek ve tanıtmak; gösterilen yönü kabul ederek doğruya ulaşmak, ayrıca bunun ilahi başarı desteğiyle gerçekleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğru yönü, yolu veya gerçeği incelikle göstermek, açıklamak ve tanıtmaktır."},{"facet_id":"F002","role":"extension","statement":"Gösterilen doğru yönü isteyerek kabul etme ve ona ulaşma sürecini de kapsar."},{"facet_id":"F003","role":"specialization","statement":"Dinsel doğruya yöneltme ve bu yönelişi mümkün kılan ilahi başarı desteği özel bir gerçekleşmedir."}],"identity_rationale":"Kaynak sözü, yanılgının karşıtı olan doğru yönelişi, yolu veya doğruyu incelikle gösterip tanıtmayı, gösterileni benimsemeyi ve ilahi başarı desteğini birlikte kapsar. Verilen dal çerçevesi bu çekirdeği doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"doğru yol, doğruyu gösterme ve açıklama"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ona yolu gösterip tanıttım"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"doğru yolu kabul edip buldu"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yol gösteren, doğruya çağıran kimse"}],"lexicalization_note":"Çıplak dal anlamı tanımlanır; başka dallardaki armağan, adanmış sunu ve özel kullanım anlamları buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğru yolu bulma alanındaki en yakın örtüşme ve açık karşıtlık sınırı en iyi belirlediği için iki ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeği bir yönü gösterme ve gösterilen yönü benimseme ilişkisidir; komşu dal ise doğru olma ve doğru yolda bulunma niteliğini daha geniş biçimde taşır.","focus_only":"Doğru yönü incelikle tanıtma, gösterileni kabul etme ve ilahi başarı desteği bu dalın sınırındadır.","gloss":"doğru yolu gösterme ve bulma","neighbor_only":"Komşu dal doğruluk ve doğru yol niteliğini, ayrıca yanlıştan uzak duran olgun kararı öne çıkarır.","neighbor_ref":"root_000565/B001","relation_type":"near_synonym","shared_zone":"İki dal da yanılgıdan uzaklaşıp doğru yola veya doğru karara ulaşma alanını paylaşır."},{"boundary_match":"opposed","distinction":"Bu dal yönün bulunmasını ve benimsenmesini bildirirken komşu dal o yönden ayrılmayı ve yolunu yitirmeyi bildirir.","focus_only":"Doğru yönü bildirme, benimseme ve ona ulaşma vardır.","gloss":"doğruya yönelme karşısında sapma","neighbor_only":"Doğru amaçtan sapma, yanlışa düşme ve yolunu yitirme vardır.","neighbor_ref":"root_000913/B001","relation_type":"antonym","shared_zone":"İki dal aynı doğru yön ile ondan uzaklaşma ekseninin karşıt uçlarında yer alır."}],"source_phrase_ar":"الهدى نقيض الضلالة؛ هدي فاهتدى (ayn;tahdhib)؛ الهدى الرشاد والدلالة؛ هداه الله للدين هدى؛ أولم يبين لهم؛ هديته الطريق والبيت هداية أي عرفته (sihah)؛ الهدى البيان وإخراج شيء إلى شيء والطاعة والورع؛ دله على الطريق (tahdhib)؛ الهداية دلالة بلطف؛ تعريف الطرق؛ التوفيق (mufradat)؛ التقدم للإرشاد؛ هديته الطريق هداية؛ الهدى خلاف الضلالة (maqayis)","source_summary":"Kaynaklar doğru yönü gösterme, yolu tanıtma ve yanılgının karşıtı olan doğruya erişme çekirdeğinde birleşir; anlatım, insanın gösterileni seçip benimsemesini ve ilahi başarı desteğini de içerir. Bir kaynakta itaat ve sakınma da bu anlam alanındaki gerçekleşmeler arasında sayılır.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الهدى والهداية بمعنى الرشاد والدلالة والبيان وتعريف الطريق أو الحق والدين والاهتداء والتوفيق الإلهي وقبول الهدى","what_is_not_ar":"لا يدخل فيه الهدية بمعنى العطاء ولا الهدي المهدى إلى الحرم ولا مجرد أول الشيء إلا إذا كان للتقدم والإرشاد"},"support_links":["sup_d259aa07f2ddd220c4c7"]},{"boundary":"Dal yalnızca genel bir yaşam tarzı değildir; yön ve amaç bildiren kullanımlarla belirli bir işte veya söylemde kalma kullanımını da içerir.","branch_kind":"mixed_non_bare","branch_ref":"root_001583/B002","candidate_links":[{"candidate_id":"cand_5462ebbc0cb2049a7c1e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"yön, izlenen yol ve tutum","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işin yönünü, hedefini ve izlenen doğrultusunu bildirir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kimsenin gidişini, görünür tutumunu ve izlediği yöntemi anlatır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sürmekte olan söz veya işi bırakmama ve başkasının izlediği yolu izleme kullanımını içerir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Özel bir söyleyişte benzerini verme veya aynı işi yeniden yapma anlamı taşır."}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin doğrultusunu ve bir kişinin davranış biçimini birlikte karşılayan genel kavram haritasında kullanılır.","boundary_detail":"Dal yalnızca genel bir yaşam tarzı değildir; yön ve amaç bildiren kullanımlarla belirli bir işte veya söylemde kalma kullanımını da içerir.","branch_image_ar":"جهة الأمر وسيرته وقصده","concept_gloss":"yön, izlenen yol ve tutum","contextual_glosses":[{"applicability":"Bir işin hangi doğrultuya baktığı veya hangi amaçla yürütüldüğü sorulduğunda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin tutumunu, yöntemini ve özel benzerlik ya da yineleme kullanımlarını dışarıda bırakır.","preserves":"İşin yönünü, hedefini ve izlenen doğrultusunu açıkça korur."},"facet_ids":["F001"],"text":"işin yönü ve amacı","usage_role":"contextual"},{"applicability":"Bir kimsenin davranış biçiminin veya yönteminin örnek alınıp sürdürüldüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işin soyut yönünü ve benzerini verme ya da yineleme kullanımını belirtmez.","preserves":"Başkasının gidişini ve yöntemini izleme yönünü korur."},"facet_ids":["F002","F003"],"text":"onun izlediği yoldan gitmek","usage_role":"contextual"}],"definition":"Bir işin yönü, amacı ve izlenen doğrultusu ile bir kimsenin gidişi, görünür tutumu ve yöntemidir. Belirli anlatımlarda yürütülen söz ya da işten sapmama, başkasının yolunu izleme, ona benzeme veya aynı karşılığı yineleme anlamı kazanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işin yönünü, hedefini ve izlenen doğrultusunu bildirir."},{"facet_id":"F002","role":"core","statement":"Bir kimsenin gidişini, görünür tutumunu ve izlediği yöntemi anlatır."},{"facet_id":"F003","role":"associated_use","statement":"Sürmekte olan söz veya işi bırakmama ve başkasının izlediği yolu izleme kullanımını içerir."},{"facet_id":"F004","role":"source_variant","statement":"Özel bir söyleyişte benzerini verme veya aynı işi yeniden yapma anlamı taşır."}],"identity_rationale":"Kaynak sözü bir işin yönünü ve amacını, kişinin gidişini, görünür tutumunu ve yöntemini, ayrıca sürmekte olan söz veya işi bırakmamayı birlikte verir. Verilen çerçeve bu çok parçalı fakat bağlantılı kullanımı korur.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"işin yönü, doğrultusu ve amacı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir kimsenin gidişi, tutumu ve yöntemi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"onun benzeri veya onu yeniden yapma"}],"lexicalization_note":"Yön, gidiş ve tutum bildiren biçimler ile kalıplaşmış benzerlik ve yineleme kullanımları ayrı yüzler olarak tutulur; özel kullanımlar çıplak kökün tümüne yayılmaz.","neighbor_coverage_note":"Tüm yön, yöntem, alışkanlık ve benzerlik adayları değerlendirildi; kapsam ayrımını en açık gösteren tek yakın anlamlı ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yön ve amaç ile izleme ilişkisini de içerir; komşu dal ise yöntem anlamından başka genel durum ve eski duruma dönüş kullanımlarına uzanır.","focus_only":"Bir işin yönü ve amacı ile yürütülen söz veya işten sapmama bu dalda yer alır.","gloss":"izlenen yol ve davranış biçimi","neighbor_only":"Bir varlığın içinde bulunduğu durum ve eski durumuna dönmesi komşu dalın daha geniş kapsamındadır.","neighbor_ref":"root_000769/B002","relation_type":"near_synonym","shared_zone":"İki dal da kişinin yerleşik gidişini, yöntemini ve davranış biçimini anlatabilir."}],"source_phrase_ar":"خذ في هديتك أي فيما كنت فيه من الحديث أو العمل ولا تعدل عنه؛ هدية أمره وسيرته؛ هدى هدي فلان أي سار سيرته (sihah)؛ هدية أمره أي جهة أمره؛ هديت به أي قصدت به؛ هديه أي سمته؛ ليس لهذا الأمر هدية ولا قبلة ولا دبرة ولا وجهة؛ هدياها أي مثلها أو أعاودك (tahdhib)؛ هدية فلان وهديه أي طريقته (mufradat)؛ نظر فلان هدي أمره أي جهته؛ ما أحسن هديته أي هديه؛ رميت بآخر هدياه أي قصده (maqayis)","source_summary":"Kaynak anlatımı yön ve amaç ile kişinin izlediği yol ve görünür tutumu aynı kavramsal alanda toplar; sürmekte olan işten sapmama, başkasının yolunu izleme ve özel bir söyleyişte benzerini ya da tekrarını yapma kullanımları buna bağlıdır.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه هدي الأمر أو هديته بمعنى جهته ووجهته وقصده وسيرته وطريقته وسمته وما يلازم ذلك من لزوم الحديث أو العمل والمماثلة في هدياها","what_is_not_ar":"لا يدخل فيه الهدى بمعنى الإرشاد الديني وحده ولا الهدية العطية ولا مشي التمايل المعتمد على اثنين"},"support_links":["sup_527740d1bef15cc9c667"]},{"boundary":"Çekirdek öncülük etmek değil, önde veya ilk sırada bulunmaktır; yol gösterme yalnızca uygun örneklerde buna bağlanır.","branch_kind":"mixed_non_bare","branch_ref":"root_001583/B003","candidate_links":[{"candidate_id":"cand_79f2718663f70ccaed6c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"bir şeyin ilk veya öndeki bölümü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünün ilk veya önde bulunan bölümü ya da üyesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atların boyunlarını veya ilk sırasını ve yaban hayvanlarının önde gidenlerini adlandırır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Okun ucunu ve koyunun boynunu, öndeki parçalar olmaları bakımından adlandırır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Önden ilerleyen değnek veya kılavuz, önde bulunma yoluyla başkasına yön gösterir."}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel konumsal çekirdeği ve hayvan, araç ya da nesnelerdeki özel ön bölüm adlarını birlikte temsil eder.","boundary_detail":"Çekirdek öncülük etmek değil, önde veya ilk sırada bulunmaktır; yol gösterme yalnızca uygun örneklerde buna bağlanır.","branch_image_ar":"المتقدم الهادي وأوائل الشيء","concept_gloss":"bir şeyin ilk veya öndeki bölümü","contextual_glosses":[{"applicability":"Bir hayvan topluluğunun ilk sırasını veya önde ilerleyen üyelerini anlatan bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir nesnenin ön parçasını ve ok ucu ya da boyun gibi özel adları kapsamaz.","preserves":"Topluluğun önünde bulunma ve ilk sırayı oluşturma yönünü korur."},"facet_ids":["F002"],"text":"önde gidenler","usage_role":"contextual"},{"applicability":"Bir nesne veya hayvan gövdesindeki önde bulunan parçanın adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öncü grup ve önden giderek yol gösterme kullanımını belirtmez.","preserves":"Bir bütünün önde bulunan parçası olma yönünü korur."},"facet_ids":["F001","F003"],"text":"ön bölüm","usage_role":"contextual"}],"definition":"Bir şeyin ilk, önde bulunan veya öne çıkan bölümü ya da üyesidir. Atların boyunları veya ilk sırası, yaban hayvanlarının öncüleri, okun ucu, koyunun boynu ve sahibinin önünde ilerleyen değnek bu konumsal çekirdeğin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünün ilk veya önde bulunan bölümü ya da üyesidir."},{"facet_id":"F002","role":"specialization","statement":"Atların boyunlarını veya ilk sırasını ve yaban hayvanlarının önde gidenlerini adlandırır."},{"facet_id":"F003","role":"specialization","statement":"Okun ucunu ve koyunun boynunu, öndeki parçalar olmaları bakımından adlandırır."},{"facet_id":"F004","role":"associated_use","statement":"Önden ilerleyen değnek veya kılavuz, önde bulunma yoluyla başkasına yön gösterir."}],"identity_rationale":"Kaynak sözü temel olarak bir şeyin ilk veya önde bulunan bölümünü bildirir; yol gösterme, bazı öndekilerin başkalarına öncülük etmesinden doğan bağlı bir açıklamadır. Bu nedenle dal korunabilir, ancak her öndeki parçanın yol gösterdiği düşünülmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyin ilki veya öndeki bölümü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"atların boyunları ya da ilk sırası; yaban hayvanlarının öncüleri"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"okun ucu ve koyunun boynu"}],"lexicalization_note":"Genel olarak ilk veya öndeki şey anlamı ile atların, yaban hayvanlarının, okun ve koyunun belirli ön parçalarını adlandıran kullanımlar ayrı tutulur.","neighbor_coverage_note":"Bütün öncülük, ilk sıra ve ön bölüm adayları değerlendirildi; genel ön bölüm komşusu sınırı en doğrudan açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal önde giden üyeleri ve kaynakta sayılan özel ön parçaları toplar; komşu dal ise ön, üst ve başlangıç konumunu daha genel biçimde kapsar.","focus_only":"Önde bulunmanın bazı örneklerde gruba öncülük etmesi ve belirli hayvan parçalarını adlandırması bu dala özgüdür.","gloss":"ilk ve öndeki bölüm","neighbor_only":"Önün yanı sıra üst bölüm ve bir yarışta göğüsle öne geçme komşu dalın daha geniş alanındadır.","neighbor_ref":"root_000849/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir bütünün başlangıçta veya ön tarafta bulunan bölümünü adlandırır."}],"source_phrase_ar":"الهادي من كل شيء أوله؛ هوادي الخيل أعناقها أو أول رعيل؛ العصا هاديا لأنها تتقدمه؛ الدليل يسمى هاديا لتقدمه (ayn)؛ هادي السهم نصله؛ الهادي العنق؛ هوادي الخيل أعناقها أو أول رعيل؛ الهاديات أوائل الوحش (sihah)؛ الهادية من كل شيء أوله وما تقدم منه؛ هادية الشاة الرقبة؛ هوادي الخيل أعناقها أو أول رعيل؛ هاديات الوحش أوائلها (tahdhib)؛ هوادي الوحش متقدماتها الهادية لغيرها (mufradat)؛ كل متقدم لذلك هاد؛ هوادي الخيل أعناقها؛ هاديها أول رعيل؛ الهادية العصا لأنها تتقدم ممسكها (maqayis)","source_summary":"Kaynaklar bir şeyin ilk ve öndeki bölümünde birleşir; atların boynu ya da ilk sırası, yaban hayvanlarının öncüleri, koyun boynu, ok ucu ve önde ilerleyen değnek bu konumsal çekirdeği farklı nesnelerde gerçekleştirir. Önden giden kılavuz da aynı konumsal ilişkiyle adlandırılır.","sources":["SI","AY","TA","MU","MQ"],"what_is_ar":"يدخل فيه الهادي أو الهادية بمعنى أول الشيء وما تقدم منه كأعناق الخيل وأول رعيلها وأوائل الوحش ورقبة الشاة ونصل السهم والعصا أو الدليل حين يتقدمان","what_is_not_ar":"لا يدخل فيه الهدى المجرد عن معنى التقدم ولا الهدية العطية ولا الهادي الراكس في البيدر"},"support_links":["sup_b60be82479842d337453"]},{"boundary":"Sıradan mal aktarımı değil, incelik ve yakınlık işareti olan armağan esastır; kutsal yere adanan sunu ayrı daldadır.","branch_kind":"bare","branch_ref":"root_001583/B004","candidate_links":[{"candidate_id":"cand_94c435b3c376f3dd357e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"incelik göstergesi armağan verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sevgi veya yakınlık duyulan birine incelik göstergesi olarak verilen şeydir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Böyle bir armağanı birine göndermek veya vermek eylemidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsanların birbirlerine karşılıklı armağan vermesini kapsar."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Armağanın üzerine konduğu tabağı ve sık armağan veren kişiyi adlandırır."}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Armağanın kendisini, verilmesini ve yakınlık kuran karşılıklı değişimi birlikte temsil eden genel karşılıktır.","boundary_detail":"Sıradan mal aktarımı değil, incelik ve yakınlık işareti olan armağan esastır; kutsal yere adanan sunu ayrı daldadır.","branch_image_ar":"بعثة لطف وهدية إلى ذي مودة","concept_gloss":"incelik göstergesi armağan verme","contextual_glosses":[{"applicability":"Yakınlık ve incelik göstergesi olarak verilen nesnenin adlandırıldığı bağlamlarda en doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Verme eylemini, karşılıklılığı, sunma tabağını ve sık veren kişi anlamını kapsamaz.","preserves":"İncelik amacıyla verilen şey olma çekirdeğini korur."},"facet_ids":["F001"],"text":"armağan","usage_role":"general"},{"applicability":"İnsanların birbirlerine karşılıklı olarak armağan verdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek armağanın adını, sunma tabağını ve sık veren kişi anlamını belirtmez.","preserves":"Karşılıklı armağan verme ilişkisini ve yakınlık yönünü korur."},"facet_ids":["F002","F003"],"text":"armağanlaşmak","usage_role":"contextual"}],"definition":"Sevgi veya yakınlık duyulan birine incelik ve iyilik göstergesi olarak bir şey gönderme ya da verme ve verilen şeydir. Karşılıklı armağanlaşma, sunma tabağı ve bunu sık yapan kişi bu çekirdeğe bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sevgi veya yakınlık duyulan birine incelik göstergesi olarak verilen şeydir."},{"facet_id":"F002","role":"core","statement":"Böyle bir armağanı birine göndermek veya vermek eylemidir."},{"facet_id":"F003","role":"extension","statement":"İnsanların birbirlerine karşılıklı armağan vermesini kapsar."},{"facet_id":"F004","role":"associated_use","statement":"Armağanın üzerine konduğu tabağı ve sık armağan veren kişiyi adlandırır."}],"identity_rationale":"Kaynak sözü sevgi bağı bulunan birine incelik ve iyilik amacıyla gönderilen armağanı, karşılıklı armağan vermeyi, armağanın sunulduğu tabağı ve sık armağan veren kişiyi açıkça kapsar. Dal çerçevesi bütün bu türevleri doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yakınlık ve incelik göstergesi armağan"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"armağan gönderdi veya verdi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"karşılıklı armağanlaşma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"armağanın sunulduğu tabak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sık sık armağan veren kimse"}],"lexicalization_note":"Çıplak armağan ve armağan verme alanı tanımlanır; kutsal amaçlı sunu, gelini eşine götürme ve şiirsel atışma anlamları içeri alınmaz.","neighbor_coverage_note":"Bütün armağan, bağış ve iyilik adayları değerlendirildi; incelik amaçlı armağana en yakın sınırı veren aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal armağan verme olayını ve ona bağlı karşılıklılık ile araç ve kişi adlarını geliştirir; komşu dal sunulan seçkin nesne veya iyilik yönünde daha dardır.","focus_only":"Karşılıklı verme, armağan tabağı ve sık armağan veren kişi bu dalın türev alanındadır.","gloss":"incelikle verilen armağan","neighbor_only":"Seçkin veya ender bulunan bir nesne ve birine iyilikte bulunma vurgusu komşu dalda öne çıkar.","neighbor_ref":"root_001356/B003","relation_type":"near_synonym","shared_zone":"İki dal da birine yakınlık ve iyilik göstergesi olarak sunulan armağanı anlatır."}],"source_phrase_ar":"الهدية ما أهديت إلى ذي مودة من بر (ayn)؛ الهدية واحدة الهدايا؛ أهديت له وإليه؛ المهدى ما يهدى فيه؛ التهادي أن يهدي بعضهم إلى بعض؛ المهداء الذي من عادته أن يهدي (sihah)؛ أهديت الهدية إهداء؛ امرأة مهداء؛ المهدى الطبق الذي يهدى عليه (tahdhib)؛ الهدية مختصة باللطف؛ المهدى الطبق؛ المهداء من يكثر إهداء الهدية (mufradat)؛ الهدية ما أهديت من لطف إلى ذي مودة؛ المهدي الطبق تهدى عليه (maqayis)","source_summary":"Kaynaklar armağanı yakınlık duyulan kişiye incelik ve iyilik amacıyla verilen şey olarak tanımlar; verme eylemi, karşılıklı verme, sunma tabağı ve sık veren kişi bu ortak çekirdeğin bağlı türevleridir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الهدية والهدايا والإهداء بمعنى العطية اللطيفة إلى ذي مودة والتهادي بين الناس والمهدى الطبق والمهداء كثير الإهداء","what_is_not_ar":"لا يدخل فيه الهدي المهدى إلى الحرم ولا العروس المهدية إلى زوجها ولا المهاداة الشعرية إذا أريدت مهاجاة متبادلة"},"support_links":["sup_19695251bcf7eaf75cc5"]},{"boundary":"Bu dal insanlar arasındaki sıradan armağanı değil, kutsal bir hedefe yaklaşma amacıyla ayrılıp gönderilen sunuyu anlatır.","branch_kind":"bare","branch_ref":"root_001583/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"kutsal yere adanan hayvan, mal veya eşya","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kutsal bir hedefe yakınlık amacıyla ayrılıp gönderilen sunudur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sununun kapsamı kimi anlatımlarda büyükbaş hayvanlarla sınırlı, kimilerinde mal ve eşyayı da içerecek kadar geniştir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Develerin genel olarak bu adla anılması, kutsal yere gönderilen deve sunusundan gelişen bir genişlemedir."}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yakınlık amacıyla kutsal hedefe gönderilen sununun kaynaklardaki dar ve geniş kapsamlarını birlikte karşılar.","boundary_detail":"Bu dal insanlar arasındaki sıradan armağanı değil, kutsal bir hedefe yaklaşma amacıyla ayrılıp gönderilen sunuyu anlatır.","branch_image_ar":"الهدي المهدى إلى الحرم","concept_gloss":"kutsal yere adanan hayvan, mal veya eşya","contextual_glosses":[{"applicability":"Kutsal bölgeye gönderilen sununun özellikle büyükbaş bir hayvan olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mal ve eşyanın da sunu olabildiği geniş kaynak kapsamını dışarıda bırakır.","preserves":"Kutsal hedefe yakınlık amacıyla ayrılan hayvan yönünü korur."},"facet_ids":["F001","F002"],"text":"adanmış sunu hayvanı","usage_role":"contextual"},{"applicability":"Adın kutsal sunu bağından genişleyerek genel deve topluluğunu anlattığı kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kutsal hedef, adama amacı ve başka tür sunular bu kısa karşılıkta görünmez.","preserves":"Develere uzanan adlandırma genişlemesini doğrudan korur."},"facet_ids":["F003"],"text":"develer","usage_role":"contextual"}],"definition":"Kutsal eve veya bölgeye yakınlık kazanma amacıyla ayrılıp gönderilen hayvan, mal ya da eşyadır. Kimi anlatımlar bunu özellikle büyükbaş hayvanlara bağlar; develerin genel olarak aynı adla anılması ise bu kullanımdan genişlemedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kutsal bir hedefe yakınlık amacıyla ayrılıp gönderilen sunudur."},{"facet_id":"F002","role":"source_variant","statement":"Sununun kapsamı kimi anlatımlarda büyükbaş hayvanlarla sınırlı, kimilerinde mal ve eşyayı da içerecek kadar geniştir."},{"facet_id":"F003","role":"extension","statement":"Develerin genel olarak bu adla anılması, kutsal yere gönderilen deve sunusundan gelişen bir genişlemedir."}],"identity_rationale":"Kaynak sözü kutsal eve veya bölgeye yakınlaşma amacıyla gönderilen hayvanı, malı ya da eşyayı bildirir; bazı anlatımlar alanı özellikle büyükbaş hayvanlarla sınırlar, bazıları daha geniş tutar. Dal çerçevesi bu kapsam değişkenliğini ve deveye uzanan kullanımı korur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kutsal bölgeye adanan hayvan, mal veya eşya"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"adanmış sunu adından genişleyen deve adı"}],"lexicalization_note":"Çıplak adanmış sunu anlamı tanımlanır; sıradan armağan, ibadete giriş ve kutsal yolculuğun kendisi bu dala katılmaz.","neighbor_coverage_note":"İbadet, ziyaret, kesim, sunu ve hazırlık adaylarının tümü değerlendirildi; en açıklayıcı genel amaç ile somut sunu ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal gönderilen somut sunuyu ve hedefini sınırlar; komşu dal ise aynı amaçla yapılan eylemleri ve kullanılan araçları genel olarak kapsar.","focus_only":"Kutsal hedefe gönderilen belirli hayvan, mal veya eşya ve bundan gelişen deve adı bu dala özgüdür.","gloss":"kutsal yere adanmış sunu","neighbor_only":"Yakınlık amacıyla yapılan her türlü eylem ve kullanılan her türlü araç komşu dalın daha geniş alanındadır.","neighbor_ref":"root_001212/B005","relation_type":"near_neighbor","shared_zone":"İki dal da kutsal yakınlık elde etmek amacıyla sunulan veya yapılan şeyi kapsar."}],"source_phrase_ar":"الهدي والهدي ما أهديت إلى مكة؛ كل شيء تهديه من مال أو متاع فهو هدي (ayn)؛ الهدي ما يهدى إلى الحرم من النعم؛ مالى هدي؛ حتى يبلغ الهدى محله (sihah)؛ أهديت الهدي إلى بيت الله؛ الهدي خفيف وعليه هدية أي بدنة؛ ما يهدى إلى مكة من النعم وغيره من مال أو متاع؛ العرب تسمي الإبل هديا (tahdhib)؛ الهدي مختص بما يهدى إلى البيت؛ فما استيسر من الهدي؛ هديا بالغ الكعبة (mufradat)؛ الهدي والهدي ما أهدي من النعم إلى الحرم قربة إلى الله تعالى (maqayis)","source_summary":"Kaynaklar kutsal hedefe yakınlık amacıyla gönderilen sunuda birleşir; kapsamın yalnızca büyükbaş hayvanlar mı yoksa mal ve eşya da mı olduğu değişir, develerin genel adı olarak kullanım da bu çekirdekten genişler.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الهدي أو الهدي المشدد والمخفف بمعنى ما يهدى إلى مكة أو الحرم أو بيت الله من النعم أو المال أو المتاع قربة وما توسع منه إلى البدنة والإبل","what_is_not_ar":"لا يدخل فيه الهدية العادية بين الناس ولا مجرد الدلالة والإرشاد"},"support_links":[]},{"boundary":"Dal evliliğin tamamını veya eş olma durumunu değil, gelinin eşinin yanına götürülmesi aşamasını anlatır.","branch_kind":"bare","branch_ref":"root_001583/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"gelini eşinin yanına götürme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gelini eşinin yanına götürme ve onunla bir araya getirme eylemidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gelinin eşine götürülmesi olayının adı olarak kullanılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eşinin yanına götürülen gelinin kendisini adlandırır."}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Götürme eylemini, olayın adını ve götürülen gelin katılımcısını aynı çekirdek altında temsil eder.","boundary_detail":"Dal evliliğin tamamını veya eş olma durumunu değil, gelinin eşinin yanına götürülmesi aşamasını anlatır.","branch_image_ar":"العروس المهدية إلى زوجها","concept_gloss":"gelini eşinin yanına götürme","contextual_glosses":[{"applicability":"Eylemin kendisinin anlatıldığı etkin cümlelerde doğal Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Olay adını ve götürülen gelinin adlandırılmasını tek başına karşılamaz.","preserves":"Gelinin eşinin yanına götürülmesi eylemini açıkça korur."},"facet_ids":["F001"],"text":"gelini eşine götürmek","usage_role":"contextual"},{"applicability":"Eylemden etkilenen gelinin adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Götürme eylemini ve olayın adını doğrudan ifade etmez.","preserves":"Götürülen gelin katılımcısını ve varış ilişkisini korur."},"facet_ids":["F003"],"text":"eşine götürülen gelin","usage_role":"contextual"}],"definition":"Bir gelini eşinin yanına götürmek, onunla bir araya getirip ona katmak ve bu götürülme olayıdır. Aynı alan, eşine götürülen gelinin kendisini de adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gelini eşinin yanına götürme ve onunla bir araya getirme eylemidir."},{"facet_id":"F002","role":"extension","statement":"Gelinin eşine götürülmesi olayının adı olarak kullanılır."},{"facet_id":"F003","role":"extension","statement":"Eşinin yanına götürülen gelinin kendisini adlandırır."}],"identity_rationale":"Kaynak sözü gelini eşinin yanına götürme, bir araya getirip katma eylemini, bu eylemin adını ve götürülen gelinin adlandırılmasını birlikte verir. Verilen dal çerçevesi bu olay ve katılımcı ayrımını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"gelini eşinin yanına götürdü"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"gelinin eşinin yanına götürülmesi"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"eşine götürülen gelin"}],"lexicalization_note":"Gelini eşine götürme ve götürülen gelin anlamları tanımlanır; armağan verme ya da düğünün bütün aşamaları bu dala taşınmaz.","neighbor_coverage_note":"Eş, evlilik, düğün, gelin taşıma ve evliliksizlik adayları değerlendirildi; aynı olay aşamasını paylaşan en yakın komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal götürme eylemi ile gelin katılımcısını adlandırır; komşu dal aynı olayın tören, taşıma ve taşıt yönlerini daha ayrıntılı kapsar.","focus_only":"Eşine götürülen gelinin edilgen adla anılması ve birleştirme ilişkisi bu dalda belirgindir.","gloss":"gelini eşine götürme","neighbor_only":"Düğün alayı, gelini taşıma ve gelinin taşındığı kapalı taşıt komşu dalın alanındadır.","neighbor_ref":"root_000635/B002","relation_type":"near_synonym","shared_zone":"İki dal da gelinin eşinin yanına götürülmesi aşamasını anlatır."}],"source_phrase_ar":"الهداء مصدر قولك هديت المرأة إلى زوجها؛ وهي مهدية وهدي (sihah)؛ هديت العروس فأنا أهديها هداء؛ أهدى الرجل امرأته جمعها إليه وضمها؛ المرأة سميت هديا لأنها كالأسيرة عند زوجها أو لأنها تهدى إلى زوجها (tahdhib)؛ الهدي يقال في العروس؛ هديت العروس إلى زوجها (mufradat)؛ الهدى العروس وقد هديت إلى بعلها هداء (maqayis)","source_summary":"Kaynaklar gelini eşine götürme ve onunla birleştirme eyleminde birleşir; eylem adı ile götürülen gelini belirten edilgen adlandırma aynı olay yapısına bağlanır. Gelin adının eşine götürülmeden veya kocasının yanında tutsak benzeri sayılmasından doğduğu yönünde iki açıklama aktarılır.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه هديت المرأة أو العروس إلى زوجها وهداؤها وكونها مهدية أو هدي في معنى مفعول","what_is_not_ar":"لا يدخل فيه الهدية العادية ولا الهدي إلى الحرم إلا من جهة أصل الإرسال"},"support_links":[]},{"boundary":"Dokunulmaz sığınmacı çekirdektir; tutsak anlamı ortak bir tanım değil, açıkça ayrılması gereken kaynak varyantıdır.","branch_kind":"bare","branch_ref":"root_001583/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"dokunulmaz sığınmacı; kimi açıklamalarda tutsak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğa sığınan veya onlardan güvence alan, dokunulmazlığı bulunan erkektir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı kaynak açıklamalarında aynı ad tutsak erkek için kullanılır."}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ana kişi türünü ve onunla birleştirilmemesi gereken tutsak varyantını birlikte görünür kılar.","boundary_detail":"Dokunulmaz sığınmacı çekirdektir; tutsak anlamı ortak bir tanım değil, açıkça ayrılması gereken kaynak varyantıdır.","branch_image_ar":"هدي الحرمة والأسير","concept_gloss":"dokunulmaz sığınmacı; kimi açıklamalarda tutsak","contextual_glosses":[{"applicability":"Bir topluluğa sığınıp onlardan güvence isteyen kişinin anlatıldığı ana kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı ad için aktarılan tutsak açıklamasını dışarıda bırakır.","preserves":"Sığınan kişinin güvence istemesini ve dokunulmaz sayılmasını korur."},"facet_ids":["F001"],"text":"güvence isteyen dokunulmaz sığınmacı","usage_role":"explanatory"},{"applicability":"Yalnızca bazı kaynak açıklamalarının aynı kişi adını tutsak için kullandığı bağlamda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dokunulmaz sığınmacı ve güvence ilişkisini bütünüyle dışarıda bırakır.","preserves":"Ayrı kaynak varyantındaki tutsak kişi anlamını korur."},"facet_ids":["F002"],"text":"tutsak","usage_role":"contextual"}],"definition":"Bir topluluktan sığınma veya güvence isteyen ve bu yüzden dokunulmaz sayılan erkektir. Bazı kaynak açıklamalarında aynı ad tutsak erkek için de kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğa sığınan veya onlardan güvence alan, dokunulmazlığı bulunan erkektir."},{"facet_id":"F002","role":"source_variant","statement":"Bazı kaynak açıklamalarında aynı ad tutsak erkek için kullanılır."}],"identity_rationale":"Kaynak sözü öncelikle bir topluluktan sığınma veya güvence isteyen ve kutsal sunuya benzer dokunulmazlığı bulunan erkeği anlatır; bazı açıklamalar aynı biçimi tutsak için de verir. Dal korunabilir, ancak sığınmacı ile tutsak tek bir durum gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"dokunulmaz sığınmacı; kimi açıklamalarda tutsak"}],"lexicalization_note":"Çıplak kişi adı, dokunulmaz sığınmacı çekirdeği ve tutsak varyantıyla tanımlanır; kutsal sunu veya gelin anlamı buraya alınmaz.","neighbor_coverage_note":"Dokunulmazlık, güvence, sığınma, korunma ve tutsaklık adayları değerlendirildi; kişi adı ile koruma olayı arasındaki en açıklayıcı ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal olayın dokunulmaz kişi katılımcısını adlandırır; komşu dal ise sığınma ve koruma ilişkisinin eylem ve durum yapısını kapsar.","focus_only":"Bu dal güvence isteyen dokunulmaz kişiyi adlandırır ve ayrıca tutsak varyantı taşır.","gloss":"koruma altındaki sığınmacı","neighbor_only":"Komşu dal sığınma isteme, güvence verme, koruma ve zulümden kurtarma olayının bütününü anlatır.","neighbor_ref":"root_000275/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişinin bir topluluktan güvence istemesi ve onların korumasına girmesi alanını paylaşır."}],"source_phrase_ar":"الرجل الذي له حرمة كحرمة هدي البيت؛ يقال للأسير أيضا هدي (sihah)؛ الهدي الرجل ذو الحرمة وهو أن يأتي القوم يستجيرهم أو يأخذ منهم عهدا؛ يقال للأسير أيضا الهدي (tahdhib)؛ وقيل الهدي الأسير (maqayis)","source_summary":"Toplu kaynak anlatımı, güvence isteyen ve kutsal sunuya benzer dokunulmazlığı bulunan erkeği öne çıkarır; tutsak anlamı ise aynı ad için aktarılan ayrı bir açıklama olarak korunur.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه الهدي للرجل ذي الحرمة المستجير أو الآخذ عهدا قبل أن يجار وللأسير في بعض الأقوال","what_is_not_ar":"لا يدخل فيه الهدي القرباني إلا من جهة التشبيه بحرمة هدي البيت ولا العروس إلا في تفسير محتمل عند تهذيب اللغة"},"support_links":[]},{"boundary":"Çekirdek sallantılı yürüyüştür; iki kişiye dayanma güçsüzlük koşuluna bağlı özel bir yapıdır ve armağan alışverişiyle ilişkili değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001583/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"sallanarak, gerektiğinde başkalarına dayanarak yürüme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yürüyüş sırasında sağa sola sallanma ve yalpalama hareketidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güçsüz kişinin iki kişi arasında yürüyerek her ikisine dayanması özel yapıdır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kadınların ve ağır develerin sallantılı yürüyüşü bu hareketin örnekleri olarak verilir."}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel yalpalama hareketini ve güçsüzlüğe bağlı iki kişiden destek alma yapısını birlikte karşılar.","boundary_detail":"Çekirdek sallantılı yürüyüştür; iki kişiye dayanma güçsüzlük koşuluna bağlı özel bir yapıdır ve armağan alışverişiyle ilişkili değildir.","branch_image_ar":"مشي التهادي مع الاعتماد والتمايل","concept_gloss":"sallanarak, gerektiğinde başkalarına dayanarak yürüme","contextual_glosses":[{"applicability":"Sağa sola sallanan yürüyüş biçiminin genel olarak anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güçsüzlük nedeniyle iki kişiye dayanma yapısını belirtmez.","preserves":"Yürüyüşte sağa sola sallanma ve dengesiz ilerleme yönünü korur."},"facet_ids":["F001","F003"],"text":"yalpalayarak yürümek","usage_role":"general"},{"applicability":"Güçsüz kişinin iki destekçi arasında ilerlediği özel söz diziminde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Desteksiz sallantılı yürüyüşün genel kapsamını dışarıda bırakır.","preserves":"İki kişiden destek almayı ve güçsüzlük koşulunu açıkça korur."},"facet_ids":["F002"],"text":"iki kişiye dayanarak yürümek","usage_role":"contextual"}],"definition":"Yürürken sağa sola sallanmak veya yalpalamaktır. Güçsüz bir kişinin iki kişi arasında ilerleyip ikisine dayanması bunun özel yapısıdır; kadınların ve ağır develerin yürüyüşü örneklenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yürüyüş sırasında sağa sola sallanma ve yalpalama hareketidir."},{"facet_id":"F002","role":"specialization","statement":"Güçsüz kişinin iki kişi arasında yürüyerek her ikisine dayanması özel yapıdır."},{"facet_id":"F003","role":"example","statement":"Kadınların ve ağır develerin sallantılı yürüyüşü bu hareketin örnekleri olarak verilir."}],"identity_rationale":"Kaynak sözü sağa sola sallanarak yürümeyi ve güçsüz kişinin iki kişiye dayanarak yürümesini açıkça ayırır; kadınların ve ağır develerin yürüyüşü örnek olarak verilir. Dal çerçevesi hareket, dayanak ve neden ayrımlarını korur.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"güçsüzlükten iki kişiye dayanarak yürümek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yürürken sağa sola sallandı"}],"lexicalization_note":"Sallanarak yürüme biçimi ile iki kişi arasında onlara dayanarak yürüme kalıbı ayrı yüzler olarak tanımlanır; dayanak koşulu bütün kullanımlara yayılmaz.","neighbor_coverage_note":"Güçsüzlük, sallanma, aksak yürüyüş, yaslanma ve beden duruşu adayları değerlendirildi; hareket biçimi ile destek ilişkisini en iyi ayıran iki komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal desteğe ihtiyaç duyulan güçsüz yürüyüşü de kapsayan fiziksel hareket biçimidir; komşu dal hareketi gösteriş ve kırıtma çağrışımıyla sınırlar.","focus_only":"Güçsüzlükten iki kişiye dayanma ve ağır develerin sallantılı yürüyüşü bu dalın kapsamındadır.","gloss":"sallanarak yürüme","neighbor_only":"Gösterişli kırıtma ve ahlaki yargı taşıyan kadın betimlemesi komşu dalın özel alanındadır.","neighbor_ref":"root_001596/B003","relation_type":"near_neighbor","shared_zone":"İki dal da yürürken bedenin sağa sola salınmasını veya kıvrılarak ilerlemesini anlatır."},{"boundary_match":"partial","distinction":"Bu dal desteği sallantılı ilerleyişin içinde kurar; komşu dal ise hareketten bağımsız genel yaslanma ve dayanma durumunu anlatır.","focus_only":"Yürüyüş sırasında sallanma ve iki kişinin arasında ilerleme bu dala özgüdür.","gloss":"yürürken desteğe dayanma","neighbor_only":"Yürüme gerektirmeyen genel yaslanma, değneğe yüklenme ve dayanma düzeni komşu dalın alanındadır.","neighbor_ref":"root_001678/B004","relation_type":"near_neighbor","shared_zone":"İki dal da beden ağırlığını bir dış desteğe vererek dengede kalmayı içerebilir."}],"source_phrase_ar":"التهادي مشي في تمايل يمينا وشمالا كمشي النساء والإبل الثقال (ayn)؛ يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله؛ المرأة إذا تمايلت في مشيتها قيل تهادى (sihah)؛ يهادى بين اثنين معناه يعتمد عليهما من ضعفه وتمايله؛ هي تهادى إذا تمايلت في مشيها (tahdhib)؛ يهادي بين اثنين إذا مشى بينهما معتمدا عليهما؛ تهادت المرأة إذا مشت مشي الهدي (mufradat)؛ جاء فلان يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما (maqayis)","source_summary":"Kaynaklar sallantılı yürüyüş ile güçsüzlük yüzünden iki kişiye dayanarak ilerleme yapısında birleşir; kadın ve ağır deve yürüyüşleri çekirdeği açıklayan örneklerdir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه يهادي بين اثنين إذا مشى معتمدا عليهما من ضعف وتمايل وتهادت المرأة إذا تمايلت في مشيتها ومشي النساء والإبل الثقال","what_is_not_ar":"لا يدخل فيه التهادي بمعنى تبادل الهدايا ولا الهدي بمعنى السكون دون تمايل"},"support_links":[]},{"boundary":"Bu dal bir kişiye yönelik olumsuz nitelemedir; gelini eşine götürme olay adıyla veya sakin ve düzgün tutumla karıştırılmaz.","branch_kind":"bare","branch_ref":"root_001583/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"bön, güçsüz ve ağır kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir erkeği bön ve kavrayışı yavaş olarak niteler."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı kişiyi güçsüz, ağır ve uyuşuk olarak niteler."}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin zihinsel yavaşlığını, bedensel güçsüzlüğünü ve uyuşuk ağırlığını birlikte nitelemek için uygundur.","boundary_detail":"Bu dal bir kişiye yönelik olumsuz nitelemedir; gelini eşine götürme olay adıyla veya sakin ve düzgün tutumla karıştırılmaz.","branch_image_ar":"الهداء البليد الضعيف","concept_gloss":"bön, güçsüz ve ağır kimse","contextual_glosses":[{"applicability":"Kişinin hareket ve tepki bakımından ağır oluşunun öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bönlük ve güçsüzlük özelliklerini bütünüyle belirtmez.","preserves":"Kişiye yüklenen ağırlık ve uyuşukluk nitelemesini korur."},"facet_ids":["F002"],"text":"ağır ve uyuşuk adam","usage_role":"contextual"}],"definition":"Bön, güçsüz, ağır ve uyuşuk erkek için kullanılan olumsuz bir nitelemedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir erkeği bön ve kavrayışı yavaş olarak niteler."},{"facet_id":"F002","role":"core","statement":"Aynı kişiyi güçsüz, ağır ve uyuşuk olarak niteler."}],"identity_rationale":"Kaynak sözü bir erkeği bön ve güçsüz, ayrıca ağır ve uyuşuk olarak niteleyen kişi adlarını verir. Dal çerçevesi zihinsel yavaşlık, bedensel güçsüzlük ve ağırlık özelliklerini doğru biçimde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bön, güçsüz, ağır ve uyuşuk adam"}],"lexicalization_note":"Çıplak kişi nitelemesi tanımlanır; aynı ses yapısındaki gelin götürme olay adı ve sakinlik anlamı buraya taşınmaz.","neighbor_coverage_note":"Ağırlık, güçsüzlük, bönlük, tembellik ve gevşeklik adayları değerlendirildi; kişi nitelemesiyle genel ağırlığı ayıran komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal özellikleri bön ve güçsüz bir erkek nitelemesinde birleştirir; komşu dal ağırlık ve yavaşlığı kişiden başka durumlara da yayar.","focus_only":"Bönlük ve güçsüzlükle birlikte belirli bir erkeği adlandıran kalıcı niteleme bu dala özgüdür.","gloss":"ağır ve uyuşuk kişi","neighbor_only":"Yemek, hastalık, uyku, beden veya genel hareket için kullanılan ağırlık ve yavaşlık komşu dalın geniş alanındadır.","neighbor_ref":"root_000202/B006","relation_type":"near_neighbor","shared_zone":"İki dal da bedensel veya davranışsal ağırlık, yavaşlık ve uyuşukluk özelliklerini paylaşır."}],"source_phrase_ar":"الهداء الرجل البليد الضعيف (ayn)؛ رجل هداء وهدان للثقيل الوخم (tahdhib)","source_summary":"Kaynak anlatımı olumsuz bir erkek nitelemesinde bönlük ve güçsüzlüğü, ağırlık ve uyuşuklukla birlikte verir.","sources":["AY","TA"],"what_is_ar":"يدخل فيه الهداء أو الهدان للرجل البليد الضعيف أو الثقيل الوخم","what_is_not_ar":"لا يدخل فيه الهداء مصدر هديت المرأة إلى زوجها ولا الهدي بمعنى السكون"},"support_links":[]},{"boundary":"Bu dal salt hareketsizlik değildir; telaşsız ilerleme ve düzgün görünür tutum birlikte bulunur.","branch_kind":"bare","branch_ref":"root_001583/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"sakin, ölçülü ve düzgün ilerleyiş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hareket ve tutumda sakinlik ve telaşsızlık bildirir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sakinliğe düzgün ve güzel bir görünür tutum eşlik eder."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bozguna uğramış kişinin acele kaçışı, bu sakin ilerleyişin karşı örneğidir."}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Telasşsız hareketi ve buna eşlik eden güzel görünür tutumu birlikte anlatan bütün çekirdek için uygundur.","boundary_detail":"Bu dal salt hareketsizlik değildir; telaşsız ilerleme ve düzgün görünür tutum birlikte bulunur.","branch_image_ar":"هدي السكون وحسن الهيئة","concept_gloss":"sakin, ölçülü ve düzgün ilerleyiş","contextual_glosses":[{"applicability":"Bir kişinin acele etmeden, görünüşünü bozmadan ilerlediği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yürüyüş dışındaki genel davranış ve tutum kapsamını daraltır.","preserves":"Sakin ilerlemeyi ve güzel görünür tutumu birlikte korur."},"facet_ids":["F001","F002","F003"],"text":"telaşsız ve düzgün yürümek","usage_role":"contextual"}],"definition":"Bozguna uğramış birinin telaşlı kaçışına benzemeyen sakin, ölçülü ve düzgün ilerleyiş ya da görünür tutumdur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hareket ve tutumda sakinlik ve telaşsızlık bildirir."},{"facet_id":"F002","role":"core","statement":"Sakinliğe düzgün ve güzel bir görünür tutum eşlik eder."},{"facet_id":"F003","role":"example","statement":"Bozguna uğramış kişinin acele kaçışı, bu sakin ilerleyişin karşı örneğidir."}],"identity_rationale":"Kaynak sözü sakinlik ile bozgun halinde kaçan kişinin telaşlı hızından uzak, düzgün ve güzel bir yürüyüş ya da tutumu birlikte verir. Dal çerçevesi sakinliği tek başına bırakmayıp görünüş ve davranış niteliğiyle bağlar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"sakinlik ve güzel, telaşsız tutum"}],"lexicalization_note":"Çıplak sakin ve düzgün tutum anlamı tanımlanır; başka kökteki durulma eylemi veya genel yaşam tarzı anlamları eklenmez.","neighbor_coverage_note":"Sakinlik, yumuşaklık, ağırbaşlılık, rahatlık ve güzel görünüş adayları değerlendirildi; hareket ve tutum sınırını en iyi gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal sakinliği kişinin düzgün ilerleyişi ve görünür tutumuyla sınırlar; komşu dal sakinliği doğaya, yaşama ve türlü eylemlere yayar.","focus_only":"Bozgun kaçışının tersine ölçülü ilerleme ve güzel görünür tutum bu dalın belirgin sınırıdır.","gloss":"sakin ve telaşsız tutum","neighbor_only":"Denizin durgunluğu ile yaşam veya eylemin sıkıntısız, sertliksiz oluşu komşu dalın daha geniş kapsamındadır.","neighbor_ref":"root_000608/B001","relation_type":"near_synonym","shared_zone":"İki dal da acele, sertlik ve kaygıdan uzak sakin bir hareket ya da davranışı anlatır."}],"source_phrase_ar":"الهدي السكون؛ ما هدى هدي مهزوم؛ لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن (ayn)؛ الهدي السكون؛ لم يسرع إسراع المنهزم ولكن على سكون وحسن هدي (tahdhib)","source_summary":"Kaynaklar sakinlik ve güzel tutumu birlikte verir; bozgun halinde kaçan kişinin aceleci yürüyüşünün reddi, bu telaşsız ve düzgün ilerleyişi belirginleştirir.","sources":["AY","TA"],"what_is_ar":"يدخل فيه الهدي بمعنى السكون وترك إسراع المنهزم مع حسن الهدي أو الهيئة","what_is_not_ar":"لا يدخل فيه المهموز هدأ إذا أريد باب السكون في أصل ه د ء ولا السيرة العامة إلا إذا نص المصدر على السكون"},"support_links":[]},{"boundary":"Dal yalnızca şiir gönderme ve şiirle karşılıklı yergileşme yapılarıyla sınırlıdır; maddi armağan veya genel sözlü tartışma değildir.","branch_kind":"non_bare","branch_ref":"root_001583/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","surface_ar":"هُدَىٰ"}],"gloss":"övgü veya yergi şiiri sunma ve şiirle yergileşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye övgü veya yergi içeren şiir sunma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki kişinin şiir yoluyla karşılıklı olarak birbirini yermesini anlatır."}}],"root_ar":"ه د ي","root_id":"root_001583","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek yönlü şiir sunma ile karşılıklı şiirsel yergiyi birlikte görünür kılan yapı bağlı karşılıktır.","boundary_detail":"Dal yalnızca şiir gönderme ve şiirle karşılıklı yergileşme yapılarıyla sınırlıdır; maddi armağan veya genel sözlü tartışma değildir.","branch_image_ar":"إهداء الشعر ومهاداته","concept_gloss":"övgü veya yergi şiiri sunma ve şiirle yergileşme","contextual_glosses":[{"applicability":"Şiirin tek bir alıcıya övgü veya yergi amacıyla yöneltildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki tarafın karşılıklı şiirle yergileşmesi kullanımını dışarıda bırakır.","preserves":"Şiiri belirli kişiye yöneltme ile övgü ve yergi seçeneklerini korur."},"facet_ids":["F001"],"text":"birine övgü ya da yergi şiiri sunmak","usage_role":"contextual"},{"applicability":"İki kişinin şiir yoluyla birbirine karşılık verip birbirini yerdiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek yönlü övgü şiiri sunma kullanımını kapsamaz.","preserves":"Karşılıklılığı, şiir aracını ve yergi eylemini korur."},"facet_ids":["F002"],"text":"şiirle karşılıklı yergileşmek","usage_role":"contextual"}],"definition":"Bir kişiye övgü veya yergi içeren bir şiir sunmak ya da iki kişinin şiirle karşılıklı olarak birbirini yermesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye övgü veya yergi içeren şiir sunma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"İki kişinin şiir yoluyla karşılıklı olarak birbirini yermesini anlatır."}],"identity_rationale":"Kaynak sözü bir kişiye övgü veya yergi şiiri sunmayı ve şiir yoluyla karşılıklı yergileşmeyi açıkça ayırır. Verilen dal çerçevesi tek yönlü şiir sunma ile karşılıklı şiirsel atışma arasındaki katılımcı farkını korur.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"birine övgü veya yergi şiiri sunma"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"şiirle karşılıklı yergileşme"}],"lexicalization_note":"Anlam yalnızca belirtilen şiir sunma ve karşılıklı şiirsel yergileşme birimlerine bağlıdır; çıplak kök için genel bir anlam sayılmaz.","neighbor_coverage_note":"Şiir türü, uyak, söz yöneltme, karşılıklılık, yergi ve çok konuşma adayları değerlendirildi; şiire bağlı yöneltme sınırını en iyi açıklayan ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal araç olarak şiiri ve içerik olarak övgü ya da yergiyi şart koşar; komşu dal hedefe yöneltmeyi şiir ve karşılıklılık koşulu olmadan anlatır.","focus_only":"Şiirin övgü veya yergi olarak sunulması ve şiirle karşılıklı yergileşme bu dalın özel sınırıdır.","gloss":"şiiri bir kişiye yöneltme","neighbor_only":"Genel konuşmayı, övgüyü veya yönelişi herhangi bir kişiye ya da yöne çevirmek komşu dalın kapsamındadır.","neighbor_ref":"root_000766/B008","relation_type":"near_neighbor","shared_zone":"İki dal da sözlü bir ürünü, özellikle övgüyü, belirli bir kişiye yöneltme ilişkisini paylaşır."}],"source_phrase_ar":"الإهداء أن تهدي إلى إنسان مديحا أو هجاء شعرا (ayn)؛ هاداني فلان الشعر وهاديته أي هاجاني وهاجيته (tahdhib)","source_summary":"Kaynak anlatımı şiiri bir kişiye yöneltilen övgü veya yergi olarak sunma ile şiir üzerinden karşılıklı yergileşme kullanımlarını aynı özel alanda toplar.","sources":["AY","TA"],"what_is_ar":"يدخل فيه إهداء المديح أو الهجاء شعرا إلى إنسان ومهاداته الشعر بمعنى مهاجاته","what_is_not_ar":"لا يدخل فيه الهدية المادية ولا مطلق المهاجاة إذا لم ترد بلفظ هادى أو أهدى"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["92:12:1"],"branch_refs":[],"candidate_id":"cand_3d9cec2a83a6114a183d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:1:boundary-pivot","source_type":"word_analysis","support_ids":["sup_38de991c276af306f0d0","sup_4663694547c3be0ebed6"],"title":"collapse scene turns into direct divine claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:1","qac_refs":["92:12:1:1"],"status":"accepted"}},{"anchor_refs":["92:12:1"],"branch_refs":[],"candidate_id":"cand_b435dd56b31df641222a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:1:confirmed-news","source_type":"word_analysis","support_ids":["sup_38de991c276af306f0d0","sup_7a177e11d621c82592fd"],"title":"confirmed news with resisted weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:1","qac_refs":["92:12:1:1"],"status":"accepted"}},{"anchor_refs":["92:12:1"],"branch_refs":[],"candidate_id":"cand_0c9e88203803d1d63383","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:1:initial-nasal-weight","source_type":"word_analysis","support_ids":["sup_38de991c276af306f0d0","sup_50ee867352b17cd8770f"],"title":"doubled nasal makes assertion audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:1","qac_refs":["92:12:1:1"],"status":"accepted"}},{"anchor_refs":["92:12:1"],"branch_refs":[],"candidate_id":"cand_17c989785d6be857dc96","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:1:inna-governed-clause","source_type":"word_analysis","support_ids":["sup_15165183e9979b706a95","sup_38de991c276af306f0d0"],"title":"particle governs the fronted and delayed clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:1","qac_refs":["92:12:1:1"],"status":"accepted"}},{"anchor_refs":["92:12:1"],"branch_refs":[],"candidate_id":"cand_b264390673622abc47bb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:1:standing-nominal-commitment","source_type":"word_analysis","support_ids":["sup_38de991c276af306f0d0","sup_ae492fbe1130dc55830b"],"title":"nominal clause makes the relation standing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:1","qac_refs":["92:12:1:1"],"status":"accepted"}},{"anchor_refs":["92:12:2"],"branch_refs":[],"candidate_id":"cand_12fd46e7f3e3cafc5268","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:2:bound-divine-pronoun","source_type":"word_analysis","support_ids":["sup_c1c8c5d9431b99fca059","sup_ce63f249f3fe1c91440b"],"title":"attached plural pronoun carries agency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:2","qac_refs":["92:12:2:1","92:12:2:2"],"status":"accepted"}},{"anchor_refs":["92:12:2"],"branch_refs":[],"candidate_id":"cand_6b2b11e8d93f82d35ac5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:2:fronted-responsibility-focus","source_type":"word_analysis","support_ids":["sup_ce63f249f3fe1c91440b","sup_d0f441d34dd1d87d23d4"],"title":"fronting foregrounds the responsible locus","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:2","qac_refs":["92:12:2:1","92:12:2:2"],"status":"accepted"}},{"anchor_refs":["92:12:2"],"branch_refs":[],"candidate_id":"cand_e0a60fd8e0093e339b49","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:2:person-shift-presence","source_type":"word_analysis","support_ids":["sup_ce63f249f3fe1c91440b","sup_f406aaa74db1a3500df4"],"title":"warning frame shifts into first-person presence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:2","qac_refs":["92:12:2:1","92:12:2:2"],"status":"accepted"}},{"anchor_refs":["92:12:2"],"branch_refs":[],"candidate_id":"cand_0350a86e0aca875257b8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:2:reported-proper-name-variant","source_type":"word_analysis","support_ids":["sup_65fb9801bd2cadc5a5d9","sup_ce63f249f3fe1c91440b"],"title":"reported variant shows a different parse","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:2","qac_refs":["92:12:2:1","92:12:2:2"],"status":"accepted"}},{"anchor_refs":["92:12:2"],"branch_refs":[],"candidate_id":"cand_71554361769aa5537acb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:2:responsibility-before-ownership","source_type":"word_analysis","support_ids":["sup_1ea035f9da4cee49b36b","sup_ce63f249f3fe1c91440b"],"title":"obligation contrasts with later possession","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:2","qac_refs":["92:12:2:1","92:12:2:2"],"status":"accepted"}},{"anchor_refs":["92:12:2"],"branch_refs":[],"candidate_id":"cand_6e3d710ed7a627c59a4c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:2:self-obligation-upon","source_type":"word_analysis","support_ids":["sup_3edafef59cf5ffd6a851","sup_ce63f249f3fe1c91440b"],"title":"upon-frame selects self-obligation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:2","qac_refs":["92:12:2:1","92:12:2:2"],"status":"accepted"}},{"anchor_refs":["92:12:3"],"branch_refs":[],"candidate_id":"cand_e1080dceb4df250ac08c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:3:emphatic-not-governing","source_type":"word_analysis","support_ids":["sup_71c43fd3aab73d935f36","sup_e1999e48158857b6f1dc"],"title":"emphasis without prepositional governance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:3","qac_refs":["92:12:3:1"],"status":"accepted"}},{"anchor_refs":["92:12:3"],"branch_refs":[],"candidate_id":"cand_5adbed281addd68d066f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:3:forward-lam-bridge","source_type":"word_analysis","support_ids":["sup_9a7058aa2703b5e99b44","sup_e1999e48158857b6f1dc"],"title":"emphasis bridges to the following claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:3","qac_refs":["92:12:3:1"],"status":"accepted"}},{"anchor_refs":["92:12:3"],"branch_refs":[],"candidate_id":"cand_9e1e3203a0eb197efd9c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:3:fused-emphatic-closure","source_type":"word_analysis","support_ids":["sup_baaa2a27690573534c65","sup_e1999e48158857b6f1dc"],"title":"lām and article compress into one closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:3","qac_refs":["92:12:3:1"],"status":"accepted"}},{"anchor_refs":["92:12:3"],"branch_refs":[],"candidate_id":"cand_a246805f0deb2427ab17","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:3:slid-lam-placement","source_type":"word_analysis","support_ids":["sup_0dd23059afd829ef2f18","sup_e1999e48158857b6f1dc"],"title":"slid placement after the fronted predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:3","qac_refs":["92:12:3:1"],"status":"accepted"}},{"anchor_refs":["92:12:3"],"branch_refs":[],"candidate_id":"cand_4ee3302329df69717cf2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:3:stacked-emphasis","source_type":"word_analysis","support_ids":["sup_0dea94f2f724e35d5b7e","sup_e1999e48158857b6f1dc"],"title":"double assertion in four words","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:3","qac_refs":["92:12:3:1"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_061468b4808e715e7cc0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:articulation-release","source_type":"word_analysis","support_ids":["sup_f0c9dc6a496cd35bf05b","sup_fcf26bd5387c139de9f7"],"title":"guidance word releases into open sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_9c0bc68071f82e511bea","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:claim-expands-to-ownership","source_type":"word_analysis","support_ids":["sup_f302cdc367bc084faa83","sup_fcf26bd5387c139de9f7"],"title":"guidance claim expands in the next ayah","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_6d5b48e5608a2dbb03ad","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:definite-comprehensive-guidance","source_type":"word_analysis","support_ids":["sup_b6418ef77a5566bdf0b3","sup_fcf26bd5387c139de9f7"],"title":"definite singular guidance is comprehensive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_d560f56923225b3eb381","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:delayed-governed-closure","source_type":"word_analysis","support_ids":["sup_1461a56f63ecd55ddb31","sup_fcf26bd5387c139de9f7"],"title":"delayed governed noun closes the clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_061c14a58648ee5e133b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:derivative-branch-pressure","source_type":"word_analysis","support_ids":["sup_2312bd8975e65850e029","sup_fcf26bd5387c139de9f7"],"title":"gift, offering, and response derivatives add pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_7b8a8c071106c58d8646","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:emphatic-definite-load","source_type":"word_analysis","support_ids":["sup_0fb1ffd8ed0120a8aa37","sup_fcf26bd5387c139de9f7"],"title":"emphasis and definiteness converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_19c137cb573aa9f62eca","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:exclusive-divine-source","source_type":"word_analysis","support_ids":["sup_35d02e54489d1543d2f6","sup_fcf26bd5387c139de9f7"],"title":"fronting plus definiteness restricts source","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_e6a1370af2828cb7e428","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:failed-sufficiency-pivot","source_type":"word_analysis","support_ids":["sup_fc38f667143e3e4664d9","sup_fcf26bd5387c139de9f7"],"title":"falling self-sufficiency turns to orientation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_b833e9692f3a269a77eb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:form-choice-standing-reality","source_type":"word_analysis","support_ids":["sup_b2b18d419a14ebfa0727","sup_fcf26bd5387c139de9f7"],"title":"nominal masdar avoids agent label and finite event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_a4be2e1bddbc6dbf2aa8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:form-i-core-guidance","source_type":"word_analysis","support_ids":["sup_ea375929ebd27f9cfb37","sup_fcf26bd5387c139de9f7"],"title":"Form I foregrounds core guidance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_c665753ee764b1a69c4f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:implicit-human-recipients","source_type":"word_analysis","support_ids":["sup_b2cacc05e1d26c8c8ae7","sup_fcf26bd5387c139de9f7"],"title":"guidance points toward recipients","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_f3bbe3d2409a81c3fe4b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:information-and-capability","source_type":"word_analysis","support_ids":["sup_78f9d009abf2ebe30a8e","sup_fcf26bd5387c139de9f7"],"title":"guidance informs and enables orientation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_33f48786a56ebee39aec","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:long-a-cadence","source_type":"word_analysis","support_ids":["sup_35f063639ff6e9130cc0","sup_fcf26bd5387c139de9f7"],"title":"open final cadence carries closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_2a83f26de70c76bcc4b4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:process-and-content","source_type":"word_analysis","support_ids":["sup_345fd7832deb8767a93d","sup_fcf26bd5387c139de9f7"],"title":"masdar holds act and supplied content","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_8327a65fbf239e783b40","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:quranic-guidance-echo","source_type":"word_analysis","support_ids":["sup_bedff124c2ce7ac3cacf","sup_fcf26bd5387c139de9f7"],"title":"book-guidance parallels remain contrastive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_e579e8e60c95f7446a3a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:route-guidance-valence","source_type":"word_analysis","support_ids":["sup_e44fcff656dadf611748","sup_fcf26bd5387c139de9f7"],"title":"guidance is route-making against error","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:4"],"branch_refs":[],"candidate_id":"cand_6523829c9977c2585fb3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:4:surah-local-answer","source_type":"word_analysis","support_ids":["sup_8a042beae75fb4624931","sup_fcf26bd5387c139de9f7"],"title":"guidance answers prior human paths","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:4","qac_refs":["92:12:3:2","92:12:3:3"],"status":"accepted"}},{"anchor_refs":["92:12:3"],"branch_refs":[],"candidate_id":"cand_2847639adfff5d9e894a","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001580","root_001583"],"scope":"focus_ayah","source_local_id":"92:12:3:3","source_type":"qac_morpheme","support_ids":["sup_9437904ead87fb6462a9"],"title":"QAC root occurrence: ه د ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:12:1"],"branch_refs":[],"candidate_id":"cand_9a0e24c76e9e80976546","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:1:claimed-surah-anaphora","source_type":"word_analysis","support_ids":["sup_38de991c276af306f0d0","sup_890f61e25b66278194d4"],"title":"claimed fourth matching particle sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:1","qac_refs":["92:12:1:1"],"status":"accepted"}},{"anchor_refs":["92:12:3"],"branch_refs":[],"candidate_id":"cand_6c243f7468819d52a52f","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:12:3:mismatched-root-claim","source_type":"word_analysis","support_ids":["sup_cf19a37392e5cce9a286","sup_e1999e48158857b6f1dc"],"title":"root-bearing analysis assigned to a particle","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:12:3","qac_refs":["92:12:3:1"],"status":"accepted"}},{"anchor_refs":["92:12"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:12","branch_refs":["root_001583/B001"],"candidate_id":"cand_9d574cf3d66e6f969ffd","commentary_obligation":"review","hft_ref":"hft_bdb698427e6e0fc510bd","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_assumed_orientation","source_type":"hft","support_ids":["sup_d259aa07f2ddd220c4c7"],"title":"b_assumed_orientation","trust":"legacy_unbound"},{"anchor_refs":["92:12"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:12","branch_refs":["root_001583/B002"],"candidate_id":"cand_5462ebbc0cb2049a7c1e","commentary_obligation":"review","hft_ref":"hft_ef6a836f6d6dea077341","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_course_not_map","source_type":"hft","support_ids":["sup_527740d1bef15cc9c667"],"title":"b_course_not_map","trust":"legacy_unbound"},{"anchor_refs":["92:12"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:12","branch_refs":["root_001583/B003"],"candidate_id":"cand_79f2718663f70ccaed6c","commentary_obligation":"review","hft_ref":"hft_95325335745e63166c2e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_preceding_lead","source_type":"hft","support_ids":["sup_b60be82479842d337453"],"title":"b_preceding_lead","trust":"legacy_unbound"},{"anchor_refs":["92:12"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:12","branch_refs":["root_001583/B004"],"candidate_id":"cand_94c435b3c376f3dd357e","commentary_obligation":"review","hft_ref":"hft_38ae39766025433ba09b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_gracious_dispatch","source_type":"hft","support_ids":["sup_19695251bcf7eaf75cc5"],"title":"b_gracious_dispatch","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"إِنَّ عَلَيْنَا لَلْهُدَىٰ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"92:12:1:1","qac_word_ref":"92:12:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"92:12:2:1","qac_word_ref":"92:12:2","root_ar":"","surface_ar":"عَلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"92:12:2:2","qac_word_ref":"92:12:2","root_ar":"","surface_ar":"نَا"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"92:12:3:1","qac_word_ref":"92:12:3","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"92:12:3:2","qac_word_ref":"92:12:3","root_ar":"","surface_ar":"لْ"},{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","root_ar":"ه د ي","surface_ar":"هُدَىٰ"}],"word_analysis_qac_refs":[["92:12:1:1"],["92:12:2:1","92:12:2:2"],["92:12:3:1"],["92:12:3:2","92:12:3:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["92:12:1","92:12:2","92:12:3","92:12:4"]},"focus_surface_evidence":{"arabic_uthmani":"إِنَّ عَلَيْنَا لَلْهُدَىٰ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"92:12:1:1","qac_word_ref":"92:12:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"92:12:2:1","qac_word_ref":"92:12:2","root_ar":"","surface_ar":"عَلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"92:12:2:2","qac_word_ref":"92:12:2","root_ar":"","surface_ar":"نَا"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"92:12:3:1","qac_word_ref":"92:12:3","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"92:12:3:2","qac_word_ref":"92:12:3","root_ar":"","surface_ar":"لْ"},{"lemma_ar":"هُدًى","morph_features":"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:12:3:3","qac_word_ref":"92:12:3","root_ar":"ه د ي","surface_ar":"هُدَىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["92:12:1:1"],["92:12:2:1","92:12:2:2"],["92:12:3:1"],["92:12:3:2","92:12:3:3"]],"word_analysis_refs":["92:12:1","92:12:2","92:12:3","92:12:4"],"word_rows":[{"analysis_record_ref":"92:12:1","analytic_gloss_range_en":"emphatic asseverative particle that turns the short nominal clause into confirmed news and governs the delayed guidance-subject with its fronted predicate","analytic_root_gloss_range_en":null,"qac_refs":["92:12:1:1"],"root":{},"surface":{"arabic":"إِنَّ","transliteration":"inna"}},{"analysis_record_ref":"92:12:2","analytic_gloss_range_en":"fronted preposition-plus-first-person-plural pronoun, locally marking self-ascribed divine responsibility for guidance rather than a mere locative or possession relation","analytic_root_gloss_range_en":null,"qac_refs":["92:12:2:1","92:12:2:2"],"root":{},"surface":{"arabic":"عَلَيْنَا","transliteration":"ʿalaynā"}},{"analysis_record_ref":"92:12:3","analytic_gloss_range_en":"emphatic lām fused before the definite guidance noun, reinforcing the confirmed clause without acting as a preposition or case governor","analytic_root_gloss_range_en":null,"qac_refs":["92:12:3:1"],"root":{},"surface":{"arabic":"لَ","transliteration":"la"}},{"analysis_record_ref":"92:12:4","analytic_gloss_range_en":"definite singular masdar naming assured guidance as both guiding act and supplied right orientation, clause-final after the responsibility phrase and reinforced by emphasis","analytic_root_gloss_range_en":"right guidance, showing the way, direction or manner, leading-front imagery, gifting, sanctuary offering, and other accepted branches; this ayah selects the guidance and direction field while derivative gift, route, and offering branches remain only narrowed image-pressure","qac_refs":["92:12:3:2","92:12:3:3"],"root":{"arabic":"ه د ي","transliteration":"h-d-y"},"surface":{"arabic":"ٱلْهُدَىٰ","transliteration":"al-hudā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["92:12"],"branch_refs":["root_001583/B001"],"candidate_id":"cand_9d574cf3d66e6f969ffd","evidence_scope":"focus_ayah","hft_ref":"hft_bdb698427e6e0fc510bd","item_id":"b_assumed_orientation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_assumed_orientation","support_id":"sup_d259aa07f2ddd220c4c7"},{"anchor_refs":["92:12"],"branch_refs":["root_001583/B002"],"candidate_id":"cand_5462ebbc0cb2049a7c1e","evidence_scope":"focus_ayah","hft_ref":"hft_ef6a836f6d6dea077341","item_id":"b_course_not_map","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_course_not_map","support_id":"sup_527740d1bef15cc9c667"},{"anchor_refs":["92:12"],"branch_refs":["root_001583/B003"],"candidate_id":"cand_79f2718663f70ccaed6c","evidence_scope":"focus_ayah","hft_ref":"hft_95325335745e63166c2e","item_id":"b_preceding_lead","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_preceding_lead","support_id":"sup_b60be82479842d337453"},{"anchor_refs":["92:12"],"branch_refs":["root_001583/B004"],"candidate_id":"cand_94c435b3c376f3dd357e","evidence_scope":"focus_ayah","hft_ref":"hft_38ae39766025433ba09b","item_id":"b_gracious_dispatch","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_gracious_dispatch","support_id":"sup_19695251bcf7eaf75cc5"}],"diagnostics":[],"lane_counts":{"global":17,"macro":7,"micro":4},"packet_summary":{"ayah_count":21,"focus_ref":"92:12","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ج ز ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000244","furuq_root_norm":"ج ز ي","furuq_source_root_norm":"ج ز ي","is_dominant":true,"target_occurrences":97,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000242","furuq_root_norm":"ج ز ز","furuq_source_root_norm":"ج ز ز","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11","92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"92:12","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":18,"unstructured_record_count":0},"identity":{"ayah_ref":"92:12","lane":"micro","linguistic_source_ref":"92:12","surface_ref":"92:12","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"92:12","target_tokens":[["Doğru",["92:12:3"]],["yolu",["92:12:3"]],["göstermek",["92:12:3"]],["elbette",["92:12:1","92:12:3"]],["bize",["92:12:2"]],["aittir",["92:12:2"]]],"text":"Doğru yolu göstermek elbette bize aittir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":12,"ayah_to":21,"id":"s092-p02-012-021","label":"Guidance, fire, and generous salvation","number":2,"refs":["92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:3:slid-lam-placement","source_type":"word_analysis","support_id":"sup_0dd23059afd829ef2f18","text":"{\"blocking_evidence\":null,\"headline\":\"slid placement after the fronted predicate\",\"reader_payoff\":\"The reader sees why the emphatic particle appears after the responsibility phrase while still reinforcing the central guidance claim.\",\"reason\":\"The inna-clause has a fronted predicate and a delayed governed noun, so the emphatic lām appears on the later guidance term rather than next to the opening particle.\",\"representative_source_ids\":[\"QG-ea1d3921\",\"MG-60c39721\",\"QS-4501a3b1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:3:stacked-emphasis","source_type":"word_analysis","support_id":"sup_0dea94f2f724e35d5b7e","text":"{\"blocking_evidence\":null,\"headline\":\"double assertion in four words\",\"reader_payoff\":\"The reader notices the unusually dense certainty produced by the opening particle plus this lām inside a four-word ayah.\",\"reason\":\"The clause contains two emphatic particles, and the translation support specifically says the construction should preserve that assertion force.\",\"representative_source_ids\":[\"QI-b2b88b31\",\"MT-d29f9296\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:emphatic-definite-load","source_type":"word_analysis","support_id":"sup_0fb1ffd8ed0120a8aa37","text":"{\"blocking_evidence\":null,\"headline\":\"emphasis and definiteness converge\",\"reader_payoff\":\"The reader hears the guidance noun as the explicitly confirmed center of the ayah, with emphasis layered onto definiteness.\",\"reason\":\"The emphatic lām intensifies the noun without changing its dependency, and the definite article keeps the noun semantically specified.\",\"representative_source_ids\":[\"QG-69113b63\",\"QF-9b7af488\",\"QI-4e17c052\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:delayed-governed-closure","source_type":"word_analysis","support_id":"sup_1461a56f63ecd55ddb31","text":"{\"blocking_evidence\":null,\"headline\":\"delayed governed noun closes the clause\",\"reader_payoff\":\"The reader sees guidance as the clause-final thing guaranteed after responsibility has already been fixed.\",\"reason\":\"Attachment evidence identifies the word as the delayed governed noun of the opening particle, while word 2 is the fronted predicate.\",\"representative_source_ids\":[\"QG-0e2abba9\",\"QG-3ae7b10f\",\"QT-a9f6d2b9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:1:inna-governed-clause","source_type":"word_analysis","support_id":"sup_15165183e9979b706a95","text":"{\"blocking_evidence\":null,\"headline\":\"particle governs the fronted and delayed clause\",\"reader_payoff\":\"The reader sees the obligation phrase and guidance noun as one particle-governed assertion rather than as loose word order.\",\"reason\":\"QAC and attachment evidence identify an emphatic particle governing an inna-clause whose fronted predicate is word 2 and whose delayed governed noun is word 4.\",\"representative_source_ids\":[\"QG-3b9b001e\",\"QG-c74dd6bc\",\"MG-bc781ce9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:2:responsibility-before-ownership","source_type":"word_analysis","support_id":"sup_1ea035f9da4cee49b36b","text":"{\"blocking_evidence\":null,\"headline\":\"obligation contrasts with later possession\",\"reader_payoff\":\"The reader can distinguish the ayah's responsibility claim from the following ayah's ownership claim (92:13).\",\"reason\":\"The local word uses a preposition-plus-pronoun obligation frame, while the following ayah uses a possession frame at 92:13.\",\"representative_source_ids\":[\"QG-8fc4982e\",\"QB-fa1b054f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:derivative-branch-pressure","source_type":"word_analysis","support_id":"sup_2312bd8975e65850e029","text":"{\"blocking_evidence\":null,\"headline\":\"gift, offering, and response derivatives add pressure\",\"reader_payoff\":\"The reader feels guidance as bestowed direction toward a destination while still keeping right guidance as the selected local sense.\",\"reason\":\"V4 keeps gift, sanctuary offering, and response-related derivatives in distinct accepted branches or forms, so they may supply image-pressure but may not replace the local right-guidance masdar.\",\"representative_source_ids\":[\"QS-180faf22\",\"QS-7b5ef6fc\",\"QS-8b29bc05\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:process-and-content","source_type":"word_analysis","support_id":"sup_345fd7832deb8767a93d","text":"{\"blocking_evidence\":null,\"headline\":\"masdar holds act and supplied content\",\"reader_payoff\":\"The reader can hold both divine guiding activity and the provided right direction without reducing the word to only one side.\",\"reason\":\"QAC marks a verbal noun, and V4's local guidance branch includes both indication or clarification and right guidance as a named reality.\",\"representative_source_ids\":[\"QS-1ad928fd\",\"QS-21b01411\",\"MS-ddbcc91f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:exclusive-divine-source","source_type":"word_analysis","support_id":"sup_35d02e54489d1543d2f6","text":"{\"blocking_evidence\":null,\"headline\":\"fronting plus definiteness restricts source\",\"reader_payoff\":\"The reader sees the ayah assign ultimate guaranteed guidance to the divine speaker with syntactic, semantic, emphatic, and acoustic convergence.\",\"reason\":\"The fronted responsibility phrase, definite delayed noun, emphatic lām, masdar form, and final cadence all converge on the guidance term.\",\"representative_source_ids\":[\"QI-d2e545f2\",\"QY-94ae5079\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:long-a-cadence","source_type":"word_analysis","support_id":"sup_35f063639ff6e9130cc0","text":"{\"blocking_evidence\":null,\"headline\":\"open final cadence carries closure\",\"reader_payoff\":\"The reader hears the guidance noun close with the same long -ā pressure that pairs it with the obligation phrase and the surrounding rhyme.\",\"reason\":\"The final alif maqṣūra creates an open -ā closure that pairs with word 2 and participates in the nearby rhyme through 92:13 and 92:14.\",\"representative_source_ids\":[\"QF-f265486e\",\"QP-e50de753\",\"MP-a781c162\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:1","source_type":"word_analysis","support_id":"sup_38de991c276af306f0d0","text":"{\"gloss_range\":\"emphatic asseverative particle that turns the short nominal clause into confirmed news and governs the delayed guidance-subject with its fronted predicate\",\"prose\":\"{{ar:إِنَّ}} ({{tr:inna}}) opens the ayah as confirmed news, not as a bare continuation, command, or question, and it gives the guidance claim the feel of a proposition that may need to resist an assumed contrary. Its governance holds the whole assertion together: the fronted responsibility phrase {{ar:عَلَيْنَا}} ({{tr:ʿalaynā}}) and the delayed guidance-subject {{ar:لَلْهُدَىٰ}} ({{tr:la-l-hudā}}) are heard as one emphatic claim. Because the sentence is nominal, the commitment is framed as a standing relation rather than a timed event. The opening also pivots from the preceding collapse scene into direct divine self-assertion, while the doubled nasal gives the certainty audible weight at the first word.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِنَّ}} ({{tr:inna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:2:self-obligation-upon","source_type":"word_analysis","support_id":"sup_3edafef59cf5ffd6a851","text":"{\"blocking_evidence\":null,\"headline\":\"upon-frame selects self-obligation\",\"reader_payoff\":\"The reader feels guidance as a responsibility taken upon the divine speaker, not merely as something located with Him.\",\"reason\":\"Attachment evidence marks the phrase as the fronted predicate, and translation support warns that the preposition should preserve the argument role of obligation rather than be treated as a locative adjunct.\",\"representative_source_ids\":[\"QG-9fc531cc\",\"MG-1a69ee13\",\"QS-e6436f7b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:1:boundary-pivot","source_type":"word_analysis","support_id":"sup_4663694547c3be0ebed6","text":"{\"blocking_evidence\":null,\"headline\":\"collapse scene turns into direct divine claim\",\"reader_payoff\":\"The reader notices the discourse turn from an observed failed figure to the divine speaker claiming responsibility for orientation.\",\"reason\":\"The next clause begins with direct emphatic assertion and word 2 carries first-person plural divine self-reference, contrasting with the prior third-person warning frame.\",\"representative_source_ids\":[\"QB-19e27091\",\"QB-8addc3e9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:1:initial-nasal-weight","source_type":"word_analysis","support_id":"sup_50ee867352b17cd8770f","text":"{\"blocking_evidence\":null,\"headline\":\"doubled nasal makes assertion audible\",\"reader_payoff\":\"The reader hears the first word carry pressure before the semantic content of the clause unfolds.\",\"reason\":\"The surface form contains the strengthened nasal of the emphatic particle, a local sound feature secondary to the syntactic force.\",\"representative_source_ids\":[\"QP-445a5089\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:2:reported-proper-name-variant","source_type":"word_analysis","support_id":"sup_65fb9801bd2cadc5a5d9","text":"{\"blocking_evidence\":null,\"headline\":\"reported variant shows a different parse\",\"reader_payoff\":\"The reader sees by contrast that the standard reading depends on the fused preposition-plus-pronoun word rather than on a named referent.\",\"reason\":\"The variant can clarify the structural contrast, but it cannot govern the canonical local parse, where QAC aligns the word as a preposition plus first-person plural pronoun.\",\"representative_source_ids\":[\"MG-97516ea1\",\"QS-8656661b\",\"QF-7cb4ef20\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:3:emphatic-not-governing","source_type":"word_analysis","support_id":"sup_71c43fd3aab73d935f36","text":"{\"blocking_evidence\":null,\"headline\":\"emphasis without prepositional governance\",\"reader_payoff\":\"The reader avoids misreading the lām as a benefactive or governing preposition and hears it as confirmation.\",\"reason\":\"QAC identifies the word as an emphatic lām, and attachment evidence keeps word 4 as the delayed governed noun under the opening particle rather than under this lām.\",\"representative_source_ids\":[\"QG-6ae6034a\",\"QG-d6f1296e\",\"QF-20ac5c6d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:information-and-capability","source_type":"word_analysis","support_id":"sup_78f9d009abf2ebe30a8e","text":"{\"blocking_evidence\":null,\"headline\":\"guidance informs and enables orientation\",\"reader_payoff\":\"The reader notices that the guidance claim can include telling the way and enabling movement along it.\",\"reason\":\"The accepted guidance branch includes showing and clarifying the road, while the local obligation frame lets the provision of orientation remain more than bare data.\",\"representative_source_ids\":[\"QS-eb89505a\",\"MS-31ed4d52\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:1:confirmed-news","source_type":"word_analysis","support_id":"sup_7a177e11d621c82592fd","text":"{\"blocking_evidence\":null,\"headline\":\"confirmed news with resisted weight\",\"reader_payoff\":\"The reader feels the guidance claim as explicitly confirmed news, with pressure against treating it as ordinary description.\",\"reason\":\"The word is tagged as an emphatic asseverative particle, and the translation support warns against flattening the emphatic construction into a neutral nominal sentence.\",\"representative_source_ids\":[\"QS-fddc5031\",\"QI-3d400cb3\",\"QT-92a32066\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:1:claimed-surah-anaphora","source_type":"word_analysis","support_id":"sup_890f61e25b66278194d4","text":"{\"blocking_evidence\":\"The cited sequence cannot be used as stated because the named references 92:6, 92:7, and 92:10 do not supply the same local opening particle pattern for this word.\",\"headline\":\"claimed fourth matching particle sequence\",\"reader_payoff\":null,\"reason\":\"The row overstates a recurring particle pattern and names references that do not match the local surface evidence for this word.\",\"representative_source_ids\":[\"MT-b03d3a8f\"],\"status\":\"rejected\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:surah-local-answer","source_type":"word_analysis","support_id":"sup_8a042beae75fb4624931","text":"{\"blocking_evidence\":null,\"headline\":\"guidance answers prior human paths\",\"reader_payoff\":\"The reader sees divine guidance in 92:12 answer the positive path of giving and guarding in 92:5 and confirmation in 92:6.\",\"reason\":\"The row family gives concrete surah-local references, and the guidance claim coherently responds to the earlier positive human profile in 92:5 and 92:6.\",\"representative_source_ids\":[\"MI-2226dbb4\",\"QE-3a41bb9a\",\"ME-d3fb44b7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:12:3:3","source_type":"qac_morpheme","support_id":"sup_9437904ead87fb6462a9","text":"{\"lemma_ar\":\"هُدًى\",\"morph_features\":\"STEM|POS:N|LEM:hudFY|ROOT:hdy|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"92:12:3:3\",\"qac_word_ref\":\"92:12:3\",\"root_ar\":\"ه د ي\",\"surface_ar\":\"هُدَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:3:forward-lam-bridge","source_type":"word_analysis","support_id":"sup_9a7058aa2703b5e99b44","text":"{\"blocking_evidence\":null,\"headline\":\"emphasis bridges to the following claim\",\"reader_payoff\":\"The reader can hear the emphatic particle link the guidance guarantee to the dominion statement that follows (92:13).\",\"reason\":\"The local emphatic lām participates in a nearby sequence of emphatic divine claims, with the concrete adjacent reference at 92:13.\",\"representative_source_ids\":[\"QB-5f154396\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:1:standing-nominal-commitment","source_type":"word_analysis","support_id":"sup_ae492fbe1130dc55830b","text":"{\"blocking_evidence\":null,\"headline\":\"nominal clause makes the relation standing\",\"reader_payoff\":\"The reader notices that the claim is presented as an abiding relation rather than as a single event of guidance beginning or ending.\",\"reason\":\"The local clause is analyzed as an inna nominal clause rather than a finite verbal predication.\",\"representative_source_ids\":[\"QT-96c102af\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:form-choice-standing-reality","source_type":"word_analysis","support_id":"sup_b2b18d419a14ebfa0727","text":"{\"blocking_evidence\":null,\"headline\":\"nominal masdar avoids agent label and finite event\",\"reader_payoff\":\"The reader sees the claim centered on guidance itself as a standing guaranteed reality, not on a guide-label or a bounded verb.\",\"reason\":\"The surface is a definite Form I masdar rather than an active participle, Form IV masdar, or finite guiding verb.\",\"representative_source_ids\":[\"QF-1de7acb2\",\"QF-ca46c7d5\",\"MF-64b65dad\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:implicit-human-recipients","source_type":"word_analysis","support_id":"sup_b2cacc05e1d26c8c8ae7","text":"{\"blocking_evidence\":null,\"headline\":\"guidance points toward recipients\",\"reader_payoff\":\"The reader notices that the grammatical noun is not a sealed abstraction; it implies recipients who need orientation.\",\"reason\":\"The word is grammatically the delayed governed noun, while contextual profiles show the guidance masdar commonly relates to human recipients.\",\"representative_source_ids\":[\"QS-9c7814de\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:definite-comprehensive-guidance","source_type":"word_analysis","support_id":"sup_b6418ef77a5566bdf0b3","text":"{\"blocking_evidence\":null,\"headline\":\"definite singular guidance is comprehensive\",\"reader_payoff\":\"The reader notices that the word presents guidance as the identifiable comprehensive guidance, not as one indefinite instance.\",\"reason\":\"QAC and noun-instance evidence identify a definite singular verbal noun, supporting a comprehensive local guidance category.\",\"representative_source_ids\":[\"QG-123525f1\",\"MG-09fbc425\",\"QF-a801d3b2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:3:fused-emphatic-closure","source_type":"word_analysis","support_id":"sup_baaa2a27690573534c65","text":"{\"blocking_evidence\":null,\"headline\":\"lām and article compress into one closure\",\"reader_payoff\":\"The reader hears emphasis and definiteness arrive together at the guidance word instead of as two isolated particles.\",\"reason\":\"The particle is orthographically and phonologically tied to the following definite noun, with the preceding nasal sequence leading into that closure.\",\"representative_source_ids\":[\"QF-5653ab1d\",\"QP-db7e0b59\",\"QP-f993f16b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:quranic-guidance-echo","source_type":"word_analysis","support_id":"sup_bedff124c2ce7ac3cacf","text":"{\"blocking_evidence\":null,\"headline\":\"book-guidance parallels remain contrastive\",\"reader_payoff\":\"The reader can compare guidance as a book-attribute elsewhere with guidance as divine responsibility here, without collapsing the constructions.\",\"reason\":\"The references 2:2 and 31:3-4 can illuminate the Quranic guidance field, but the local construction is the delayed governed noun in an obligation frame, not the same book-description construction.\",\"representative_source_ids\":[\"MI-416315c2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:2:bound-divine-pronoun","source_type":"word_analysis","support_id":"sup_c1c8c5d9431b99fca059","text":"{\"blocking_evidence\":null,\"headline\":\"attached plural pronoun carries agency\",\"reader_payoff\":\"The reader sees divine agency encoded inside the bound word itself, without an added explanatory noun.\",\"reason\":\"The cross-reference evidence treats the first-person plural suffix as a surface-form divine speech role and warns against adding a named antecedent.\",\"representative_source_ids\":[\"QG-49b5153e\",\"QF-56e8d4ea\",\"QF-a43f8563\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:2","source_type":"word_analysis","support_id":"sup_ce63f249f3fe1c91440b","text":"{\"gloss_range\":\"fronted preposition-plus-first-person-plural pronoun, locally marking self-ascribed divine responsibility for guidance rather than a mere locative or possession relation\",\"prose\":\"{{ar:عَلَيْنَا}} ({{tr:ʿalaynā}}) is not a locative aside; it is the fronted predicate of the clause, so the ayah first fixes where the responsibility lies, excludes rival ultimate sources of guaranteed guidance, and only then names {{ar:ٱلْهُدَىٰ}} ({{tr:al-hudā}}). The preposition keeps the concrete pressure of something being upon the speaker while the rational-agent frame selects obligation, making guidance a self-ascribed divine burden. The attached plural pronoun makes that agency inseparable from the preposition and brings the voice from third-person warning into direct divine self-reference. The next ayah changes the relation to a possession frame (92:13), so this word's governor contrast matters: guidance is stated as responsibility here before dominion is stated as ownership there. The reported proper-name variant is useful only as apparatus: it would restructure the predication around a named figure as guidance, which shows how much the standard reading depends on the fused preposition-plus-pronoun structure.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:عَلَيْنَا}} ({{tr:ʿalaynā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:3:mismatched-root-claim","source_type":"word_analysis","support_id":"sup_cf19a37392e5cce9a286","text":"{\"blocking_evidence\":\"QAC identifies word 3 as a rootless emphatic particle, so a root-based lexical comparison cannot be assigned to this word.\",\"headline\":\"root-bearing analysis assigned to a particle\",\"reader_payoff\":null,\"reason\":\"The row's contrast between obligation and ownership is meaningful elsewhere in the ayah pair, but its root-bearing assignment conflicts with the aligned local particle.\",\"representative_source_ids\":[\"MI-0a46fec0\"],\"status\":\"rejected\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:2:fronted-responsibility-focus","source_type":"word_analysis","support_id":"sup_d0f441d34dd1d87d23d4","text":"{\"blocking_evidence\":null,\"headline\":\"fronting foregrounds the responsible locus\",\"reader_payoff\":\"The reader notices that the clause names the responsible divine side before it names the guidance itself.\",\"reason\":\"The predicate phrase precedes the delayed governed noun, so the structure foregrounds the locus of responsibility before the guidance term.\",\"representative_source_ids\":[\"QI-f9fca03e\",\"QT-9020c817\",\"MT-1f82670a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:3","source_type":"word_analysis","support_id":"sup_e1999e48158857b6f1dc","text":"{\"gloss_range\":\"emphatic lām fused before the definite guidance noun, reinforcing the confirmed clause without acting as a preposition or case governor\",\"prose\":\"{{ar:لَ}} ({{tr:la}}) is an emphatic lām, not a preposition governing the following noun. Its open vowel and placement keep it from being read as benefactive {{ar:لِ}} ({{tr:li}}), while its force reinforces the same assertion already opened by {{ar:إِنَّ}} ({{tr:inna}}); together they create double news-emphasis inside a four-word ayah. Because the predicate has been fronted, the lām lands after the responsibility phrase and on the delayed guidance term, so the clause first foregrounds responsibility and then locks emphasis onto {{ar:ٱلْهُدَىٰ}} ({{tr:al-hudā}}) without placing the two emphatic particles side by side. Its fusion with the article makes the recited closure {{ar:لَلْهُدَىٰ}} ({{tr:la-l-hudā}}) sound like a single emphatic-definite unit, after the n/nā nasal thread has carried the opening assertion through the divine pronoun. The repeated emphatic lām also points forward to the next ownership claim (92:13), but the local word remains a particle, not a root-bearing lexical item.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَ}} ({{tr:la}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:route-guidance-valence","source_type":"word_analysis","support_id":"sup_e44fcff656dadf611748","text":"{\"blocking_evidence\":null,\"headline\":\"guidance is route-making against error\",\"reader_payoff\":\"The reader feels guidance as morally positive orientation and navigable route-making, not as detached information.\",\"reason\":\"V4 accepts the right-guidance and showing-the-road branch for {{ar:ه د ي}} ({{tr:h-d-y}}), and the local ayah selects that field through the guidance masdar.\",\"representative_source_ids\":[\"QS-19ebded2\",\"QS-784f8309\",\"QS-f651278c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:form-i-core-guidance","source_type":"word_analysis","support_id":"sup_ea375929ebd27f9cfb37","text":"{\"blocking_evidence\":null,\"headline\":\"Form I foregrounds core guidance\",\"reader_payoff\":\"The reader notices that the word foregrounds the core guidance field rather than a more explicitly causative giving-of-guidance form.\",\"reason\":\"The local form is the guidance masdar associated with the selected branch rather than a separate causative verbal noun.\",\"representative_source_ids\":[\"QF-a2154b97\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:articulation-release","source_type":"word_analysis","support_id":"sup_f0c9dc6a496cd35bf05b","text":"{\"blocking_evidence\":null,\"headline\":\"guidance word releases into open sound\",\"reader_payoff\":\"The reader hears the word move from breathy onset through a dental stop into an open release at the verse close.\",\"reason\":\"The phonetic observation is locally anchored in the surface shape of the final word, though it remains secondary to syntax and semantics.\",\"representative_source_ids\":[\"QP-29aca5eb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:claim-expands-to-ownership","source_type":"word_analysis","support_id":"sup_f302cdc367bc084faa83","text":"{\"blocking_evidence\":null,\"headline\":\"guidance claim expands in the next ayah\",\"reader_payoff\":\"The reader sees the claim move from guidance in 92:12 to ownership of the final and first life in 92:13.\",\"reason\":\"The concrete adjacent reference at 92:13 broadens the field of divine claim after the guidance guarantee.\",\"representative_source_ids\":[\"ME-18aec4a2\",\"QB-76170c88\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:2:person-shift-presence","source_type":"word_analysis","support_id":"sup_f406aaa74db1a3500df4","text":"{\"blocking_evidence\":null,\"headline\":\"warning frame shifts into first-person presence\",\"reader_payoff\":\"The reader notices that the discourse leaves the third-person field of the failed person and hears a direct divine claim.\",\"reason\":\"The suffix supplies first-person plural speech role after the preceding discourse described another figure in third person.\",\"representative_source_ids\":[\"QI-d8db8b09\",\"QB-e49e7bdc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4:failed-sufficiency-pivot","source_type":"word_analysis","support_id":"sup_fc38f667143e3e4664d9","text":"{\"blocking_evidence\":null,\"headline\":\"falling self-sufficiency turns to orientation\",\"reader_payoff\":\"The reader notices that the guidance claim fills the void left by wealth's failure and the prior fall in 92:11.\",\"reason\":\"The boundary rows tie the clause to the immediately preceding failure scene, and the local guidance noun supplies the contrasting orientation term.\",\"representative_source_ids\":[\"QB-4c60d144\",\"QB-eca73011\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:12:4","source_type":"word_analysis","support_id":"sup_fcf26bd5387c139de9f7","text":"{\"gloss_range\":\"definite singular masdar naming assured guidance as both guiding act and supplied right orientation, clause-final after the responsibility phrase and reinforced by emphasis\",\"prose\":\"{{ar:ٱلْهُدَىٰ}} ({{tr:al-hudā}}) is the landing word of the clause: its case is not visually shown on the final alif maqṣūra, but particle governance makes it the delayed governed noun after {{ar:عَلَيْنَا}} ({{tr:ʿalaynā}}). Definiteness, singular masdar form, and the attached emphatic {{ar:لَ}} ({{tr:la}}) gather the claim into assuredly the exhaustive guidance, not one guidance among rivals. The root's selected field is right guidance and showing the way, so the word is more than neutral information: it is direction against error, a route made navigable after the prior fall, both telling the way and enabling movement along it. As a masdar it can hold both the act of guiding and the supplied guidance-content, while the nominal form makes that orientation a standing guaranteed reality rather than a timed finite action or an agent label. The Form I shape foregrounds the core guidance act or state rather than a separate causative giving-of-guidance form. Related branches add narrowed pressure without replacing the local sense: gift language within the surah's earlier giving frame makes the direction feel bestowed, sanctuary-driving language reinforces movement toward a consecrated destination, and reflexive or seeking derivatives highlight that this ayah states supply before recipient response or petition. The long final -ā pairs the obligation phrase with the guidance noun and closes the ayah in the rhyme pattern that continues through 92:13 and 92:14. Within the surah, the word answers the failure of wealth in 92:11, responds to the positive path of giving, fearing, and confirming in 92:5 and 92:6, and prepares the expansion from guidance to full ownership in 92:13. The broader Quranic guidance pattern remains contrastive: elsewhere guidance can describe the Book (2:2; 31:3-4), while here it is placed in the divine responsibility frame.\",\"root_display\":\"{{ar:ه د ي}} ({{tr:h-d-y}})\",\"root_gloss_range\":\"right guidance, showing the way, direction or manner, leading-front imagery, gifting, sanctuary offering, and other accepted branches; this ayah selects the guidance and direction field while derivative gift, route, and offering branches remain only narrowed image-pressure\",\"surface_display\":\"{{ar:ٱلْهُدَىٰ}} ({{tr:al-hudā}})\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ عَلَيْنَا لَلْهُدَىٰ","ayah_ref":"92:12"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001583/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001583","role":"Gentle indication and enabling toward a true way supplies the clause's core orienting action and makes عَلَيْنَا sound responsibility-bearing.","root":"ه د ي","source_ref":"92:12","source_word_indices":["3"]}],"changed_reading":{"after":"The speaker emphatically assumes responsibility for making a truth-directed way discernible and traversable.","before":"Guidance is simply said to belong to the speaker."},"confidence":"strong","focus_anchor":"The emphatic construction إِنَّ عَلَيْنَا لَلْهُدَىٰ places the nominal هُدَىٰ under عَلَيْنَا rather than merely announcing that guidance exists.","mechanism":"The guidance branch supplies gentle indication, clarification, and enabling toward a way or truth; the syntax presents that orienting work as an emphatically assumed responsibility.","model_id":"b_assumed_orientation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_assumed_orientation","source_type":"hft","support_id":"sup_d259aa07f2ddd220c4c7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ عَلَيْنَا لَلْهُدَىٰ","ayah_ref":"92:12"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001583/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001583","role":"The course, manner, and intended-direction image turns guidance into the practical bearing of a journey and assigns that bearing to the clause's عَلَيْنَا.","root":"ه د ي","source_ref":"92:12","source_word_indices":["3"]}],"changed_reading":{"after":"Guidance is the directed course and practical bearing of travel, whose orientation the speaker undertakes.","before":"Guidance is information that points toward a road."},"confidence":"strong","focus_anchor":"The definite nominal لَلْهُدَىٰ can anchor not only an act of telling but the course, bearing, or intended direction carried by ه د ي.","mechanism":"If هُدَىٰ profiles a course and manner of proceeding, the clause concerns governance of trajectory: what is 'upon us' is the directional shape of the movement, not merely delivery of a map.","model_id":"b_course_not_map"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_course_not_map","source_type":"hft","support_id":"sup_527740d1bef15cc9c667","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ عَلَيْنَا لَلْهُدَىٰ","ayah_ref":"92:12"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001583/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001583","role":"The leading-front image supplies an advance presence whose going-before makes the route followable.","root":"ه د ي","source_ref":"92:12","source_word_indices":["3"]}],"changed_reading":{"after":"What is undertaken is to go ahead as a leading edge, so the traveler follows an already opened line.","before":"The traveler receives directions while remaining the first to enter the route."},"confidence":"medium","focus_anchor":"The focus noun هُدَىٰ is visibly tied to a branch in which the guide or foremost part goes ahead.","mechanism":"Guidance can operate from in front: an advance edge enters the route first and thereby gives following motion its line. The clause then promises precedential presence rather than rearward instruction.","model_id":"b_preceding_lead"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_preceding_lead","source_type":"hft","support_id":"sup_b60be82479842d337453","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ عَلَيْنَا لَلْهُدَىٰ","ayah_ref":"92:12"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001583/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001583","role":"The graciously sent gift supplies a source-to-recipient trajectory and recasts guidance as beneficent transmission.","root":"ه د ي","source_ref":"92:12","source_word_indices":["3"]}],"changed_reading":{"after":"Guidance is a gracious dispatch whose movement toward the addressee is undertaken at the source.","before":"Guidance is a stock of knowledge located with the speaker."},"confidence":"medium","focus_anchor":"The same focus root permits هُدَىٰ to resonate with something graciously sent toward a recipient.","mechanism":"Guidance becomes a directed transfer rather than a possession held at the source. عَلَيْنَا marks source-side commitment to dispatch the gift; it does not make the recipient a creditor.","model_id":"b_gracious_dispatch"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_gracious_dispatch","source_type":"hft","support_id":"sup_19695251bcf7eaf75cc5","trust":"legacy_unbound"}]}
</lane_packet_json>
