# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **92:16**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s092-regular-20260912/s092/92_16/micro.discovery.json` and modify nothing
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
  "ayah_ref": "92:16",
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
{"branch_registry":[{"boundary":"Dal, gerçeğe aykırı söz ve davranışı kapsar; başkasını yalancılıkla niteleme eylemini ya da özel kalıpların bağımsız anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001290/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:2:1","qac_word_ref":"92:16:2","surface_ar":"كَذَّبَ"}],"gloss":"sözde veya davranışta doğruluğa aykırılık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğruluğa aykırılık hem söylenen bir sözde hem de yapılan bir davranışta gerçekleşebilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu niteliği taşıyan veya onu sıkça gösteren kişi, yalan söyleyen kişi olarak adlandırılır."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem söz hem davranış alanındaki bütün yalın anlam çekirdeğini karşılayan açıklayıcı üst karşılıktır.","boundary_detail":"Dal, gerçeğe aykırı söz ve davranışı kapsar; başkasını yalancılıkla niteleme eylemini ya da özel kalıpların bağımsız anlamlarını kapsamaz.","branch_image_ar":"خلاف الصدق","concept_gloss":"sözde veya davranışta doğruluğa aykırılık","contextual_glosses":[{"applicability":"Bağlamın söz veya davranıştaki doğruluğa aykırılığı zaten belirginleştirdiği doğal kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğruluğa aykırılık çekirdeğini ve kişiye yüklenebilen niteliği doğal Türkçeyle korur."},"facet_ids":["F001","F002"],"text":"yalan","usage_role":"general"}],"definition":"Bir sözün veya davranışın doğruluğa aykırı olmasıdır. Bu niteliği taşıyan kişi, yalan söyleyen ya da yalanı çokça tekrarlayan biri olarak betimlenebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğruluğa aykırılık hem söylenen bir sözde hem de yapılan bir davranışta gerçekleşebilir."},{"facet_id":"F002","role":"specialization","statement":"Bu niteliği taşıyan veya onu sıkça gösteren kişi, yalan söyleyen kişi olarak adlandırılır."}],"identity_rationale":"Kaynak ifadesi anlamı doğruluğun karşıtı olarak kurar ve bu karşıtlığın hem sözde hem davranışta gerçekleşebildiğini açıkça belirtir. Kişiyi bu nitelikle betimleyen biçimler aynı çekirdeğe bağlıdır; birini yalancı sayma eylemi ise ayrı dalın konusudur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sözde veya davranışta doğruluğa aykırılık; yalan"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yalancı; çok yalan söyleyen kişi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"uydurma söz; yalanlar"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"özürlere kaçınılmaz olarak yalan karışır"}],"lexicalization_note":"Tanım yalın anlam çekirdeğini verir; kişi betimleyen türevler ile özürlere ilişkin kalıp yalnız kendi sözcüksel karşılıklarında gösterilir ve yalın anlama eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yalanla en kolay karışan beş anlam yayımlandı, yalnızca aynı senaryoda bulunan özel kalıplar ve uzak tematik adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gerçeğe aykırı içeriğin ya da davranışın niteliğidir; komşu dal ise bir kişi veya söz hakkında bu yönde hüküm verme işlemidir.","focus_only":"Doğruluğa aykırı sözün veya davranışın kendisini bildirir.","gloss":"yalan ile yalan sayma ayrımı","neighbor_only":"Bir sözü yalan sayma, birini yalancı bulma veya ona yalancılık yükleme işlemini bildirir.","neighbor_ref":"root_001290/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da doğruluk ile gerçeğe aykırılık arasındaki değerlendirme alanındadır."},{"boundary_match":"partial","distinction":"Odak dal genel doğruluğa aykırılıktır; komşu dal bunun daha ağır, saptırılmış veya başkalarını yanlış yöne sevk eden türünü belirginleştirir.","focus_only":"Sıradan ölçekteki söz ve davranış yalanlarını da kapsar.","gloss":"yalan ile saptırıcı büyük yalan","neighbor_only":"Doğrudan sapmış, büyük veya başkalarını yanlış yöne çeken ağır bir yalan alanını da öne çıkarır.","neighbor_ref":"root_000041/B002","relation_type":"near_synonym","shared_zone":"İki dal da doğruluğa aykırı söz ve aldatıcı içerik alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal söz ve davranıştaki genel doğruluğa aykırılıktır; komşu dal özellikle bilgi yerine tahmine dayanarak asılsız söz üretmeyi de içerir.","focus_only":"Söz dışındaki davranışlarda görülen doğruluğa aykırılığı da kapsar.","gloss":"yalan ile bilgisizce söyleme","neighbor_only":"Bilgiye dayanmadan tahmin yürütme ve doğrulanmamış söz söyleme alanını da kapsar.","neighbor_ref":"root_000403/B002","relation_type":"near_synonym","shared_zone":"Gerçek dışı veya dayanaksız söz söyleme bağlamlarında iki anlam birbirine yaklaşır."},{"boundary_match":"partial","distinction":"Odak dal genel yalan niteliğidir; komşu dal yalanı özellikle haktan sapma, yalancı tanıklık ve batıllık çevresinde örgütler.","focus_only":"Her türlü sözsel veya davranışsal doğruluğa aykırılığı kapsar.","gloss":"genel yalan ile haktan sapmış söz","neighbor_only":"Yalancı tanıklık, haktan sapma ve batıl sayılan nesneler gibi özel alanlara uzanır.","neighbor_ref":"root_000654/B002","relation_type":"near_neighbor","shared_zone":"İki dal da gerçek ve hakikate aykırı söz alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal doğruluğa aykırılığı temel alır; komşu dal ise sözün kesinlik ve güven düzeyine odaklanır, bu nedenle her kuşkulu aktarım yalan değildir.","focus_only":"Sözün ya da davranışın doğruluğa aykırı olmasını doğrudan bildirir.","gloss":"yalan ile kuşkulu aktarım","neighbor_only":"Kesinlik bulunmadan aktarılan, kuşkulu veya doğruluğu güven vermeyen sözü de kapsar.","neighbor_ref":"root_000633/B001","relation_type":"near_neighbor","shared_zone":"Kuşkulu bir iddianın gerçek dışı çıkması durumunda iki alan kesişebilir."}],"source_phrase_ar":"الكذب خلاف الصدق (maqayis;jamhara); الكذاب لغة في الكذب (ayn); كذب كذبا فهو كاذب وكذاب وكذوب (sihah); يقال في المقال والفعال (mufradat)","source_summary":"Kaynaklar, doğruluğa aykırılığı ortak çekirdek sayar; kullanım alanını söz ve davranış olarak verir ve bu niteliği taşıyan kişiye yönelik adlandırmaları aynı anlam çevresinde toplar.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الكذب في القول والفعل، ووصف صاحبه بالكاذب والكذاب والكذوب، وجمع الأكاذيب والمكاذب","what_is_not_ar":"لا يدخل فيه فعل التكذيب والنسبة إلى الكذب، ولا إغراء كذب عليك، ولا الألفاظ الاصطلاحية الخاصة بالحملة واللبن والثوب"},"support_links":[]},{"boundary":"Dal yalan üretmeyi değil, kişi veya söz hakkında yalan hükmü vermeyi ve belirli türevlerde bu hükmü bulguya dayandırmayı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001290/B002","candidate_links":[{"candidate_id":"cand_ecbc550fc1c947233fc7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:2:1","qac_word_ref":"92:16:2","surface_ar":"كَذَّبَ"}],"gloss":"yalan sayma veya yalancı bulma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya söz, yalan olduğu söylenerek doğruluk bakımından olumsuz değerlendirilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli türemiş biçimler, kişiyi yalancı bulmayı veya onun yalanını ortaya çıkarmayı bildirir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hüküm verme çekirdeği ile belirli türevlerdeki bulma ve açığa çıkarma ayrımını birlikte karşılar.","boundary_detail":"Dal yalan üretmeyi değil, kişi veya söz hakkında yalan hükmü vermeyi ve belirli türevlerde bu hükmü bulguya dayandırmayı kapsar.","branch_image_ar":"نسبة الشيء أو صاحبه إلى الكذب","concept_gloss":"yalan sayma veya yalancı bulma","contextual_glosses":[{"applicability":"Bir sözün veya kişinin söylediğinin yalan olduğunu bildiren bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiyi yalancı bulma ve yalanını ortaya çıkarma sonucunu tek başına göstermez.","preserves":"Kişi veya söz hakkında yalan hükmü verme işlemini korur."},"facet_ids":["F001"],"text":"yalanlamak","usage_role":"contextual"},{"applicability":"Değerlendirme sonucunda bir kişinin yalan söylediğinin anlaşıldığı türemiş biçimler için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir sözü doğrudan yalan sayma ve muhataba yalan söylediğini bildirme işlemini kapsamaz.","preserves":"Kişiyi yalancı bulma veya yalanını açığa çıkarma sonucunu korur."},"facet_ids":["F002"],"text":"yalancı bulmak","usage_role":"contextual"}],"definition":"Bir kişiyi veya sözü yalanla ilişkilendirerek yalan olduğunu söylemektir. Bazı türemiş biçimlerde işlem, kişiyi yalancı bulma ya da yalanını ortaya çıkarma sonucunu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya söz, yalan olduğu söylenerek doğruluk bakımından olumsuz değerlendirilir."},{"facet_id":"F002","role":"source_variant","statement":"Belirli türemiş biçimler, kişiyi yalancı bulmayı veya onun yalanını ortaya çıkarmayı bildirir."}],"identity_rationale":"Kaynak ifadesi tek bir işlemi değil, birbirine bağlı iki işlemi içerir: bir kişiyi veya sözü yalanla nitelemek ve bazı türemiş biçimlerde kişiyi yalancı bulmak ya da yalanını açığa çıkarmak. Dal korunabilir, ancak bu ayrım tek bir genel 'yalan yükleme' anlatımı içinde eritilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yalanlama; yalan sayma"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"birini yalancı saymak veya ona yalan söylediğini bildirmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini yalancı bulmak veya yalanını ortaya çıkarmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"seni yalancı saymıyorum"}],"lexicalization_note":"Tanım, türemiş ve nesne alan biçimlerinin farklı işlemlerini ayırır; bunlardan hiçbiri yalın biçimin genel yalan anlamı olarak sunulmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalanın kendisi, genel suçlama ve benzer isnat işlemleriyle sınırı gösteren dört aday seçildi, daha uzak söz ve özel kalıp alanları yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalan olduğuna hükmetme işlemidir; komşu dal ise bu hükmün konusu olan gerçeğe aykırı söz veya davranıştır.","focus_only":"Bir kişi veya söz hakkında yalan hükmü verme işlemini bildirir.","gloss":"yalan sayma ile yalan ayrımı","neighbor_only":"Doğruluğa aykırı sözün veya davranışın kendisini bildirir.","neighbor_ref":"root_001290/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da doğruluk değerlendirmesi ve yalan alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal yalnız doğruluk ve yalan eksenindeki hükme bağlıdır; komşu dalın suçlama ve kuşku alanı daha geniştir.","focus_only":"Yüklenen nitelik özellikle yalan söyleme veya sözün yalan olmasıdır.","gloss":"yalancılıkla niteleme ile suçlama","neighbor_only":"Kişiye herhangi bir suçlama ya da kuşku iliştirmeyi, hatta onda bulunmayan olumlu bir niteliği yakıştırmayı kapsayabilir.","neighbor_ref":"root_001607/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir kişi hakkında olumsuz bir niteleme veya iddia yöneltme işlemini içerebilir."},{"boundary_match":"field_only","distinction":"İşlemin yapısı benzerdir, ancak odak dalın hükmü yalanla, komşu dalın hükmü hırsızlıkla sınırlıdır; anlam çekirdekleri birbirinin yerine geçmez.","focus_only":"Kişiyi yalancılıkla veya sözünü yalan olmakla niteler.","gloss":"farklı fiillerle suçlayıcı niteleme","neighbor_only":"Kişiyi hırsızlık yapmakla niteler.","neighbor_ref":"root_000700/B005","relation_type":"same_field","shared_zone":"İki dal da bir kişiye belirli bir olumsuz eylemi yükleyen dilsel işlemlerdir."},{"boundary_match":"partial","distinction":"Odak dal doğruluk hakkında verilen hükümdür; komşu dal ise gerçekleşmemiş belirli bir eylemin kişiye isnat edilmesidir.","focus_only":"Bir kişiyi genel olarak yalancı sayabilir veya belirli bir sözü yalanlayabilir.","gloss":"yalan sayma ile yapılmamışı yükleme","neighbor_only":"Kişinin yapmadığı belirli bir içme eylemini ona yükleme iddiasıyla sınırlıdır.","neighbor_ref":"root_000783/B010","relation_type":"near_neighbor","shared_zone":"Bir kişiye gerçekleşmemiş bir eylem yüklenince bu iddiayı yalanlama bağlamında iki alan kesişir."}],"source_phrase_ar":"كذبت فلانا نسبته إلى الكذب وأكذبته وجدته كاذبا (maqayis); كذبته جعلته كاذبا (ayn); كذبت بالحديث كذابا وتكذيبا (jamhara); أكذبت الرجل ألفيته كاذبا وكذبته إذا قلت له كذبت (sihah); كذبته نسبته إلى الكذب (mufradat)","source_summary":"Kaynaklar, birini ya da bir sözü yalanla niteleme konusunda birleşir; aynı toplu kanıt, ayrı bir türemiş biçimde kişiyi yalancı bulma veya yalanı açığa çıkarma yorumunu da taşır.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه كذبت فلانا، وأكذبته، والتكذيب، والمكاذبة، ولا مكذبة بمعنى لا أكذبك، وقراءة لا يكذبونك في معنى لا يجدونك كاذبا أو لا ينسبونك إلى الكذب","what_is_not_ar":"لا يدخل فيه إنشاء الكذب نفسه، ولا الإغراء بقول كذب عليك، ولا كذب الحملة أو اللبن"},"support_links":["sup_453f8fd81af0401ce204"]},{"boundary":"Dal, belirli kalıbın 'sana düşer, onu yap' anlamıyla sınırlıdır; yalın köke genel bir zorunluluk veya özendirme anlamı vermez.","branch_kind":"collocation","branch_ref":"root_001290/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:2:1","qac_word_ref":"92:16:2","surface_ar":"كَذَّبَ"}],"gloss":"onu üstlen; sana düşer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalıp, söz konusu işin muhataba düşen bir yükümlülük olduğunu bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı kalıp, muhatabı o işi üstlenmeye yönelten güçlü bir özendirme olarak kullanılabilir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıbın hem yükümlülük bildiren hem de eyleme yönelten iki işlevini birlikte veren karşılıktır.","boundary_detail":"Dal, belirli kalıbın 'sana düşer, onu yap' anlamıyla sınırlıdır; yalın köke genel bir zorunluluk veya özendirme anlamı vermez.","branch_image_ar":"كذب عليك بمعنى الزم وعليك به","concept_gloss":"onu üstlen; sana düşer","contextual_glosses":[{"applicability":"Kalıbın yükümlülük bildiren yönünün öne çıktığı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Buyruk ve güçlü özendirme tonunu tek başına tam olarak göstermez.","preserves":"İşin muhataba düşen bir yükümlülük oluşunu açıkça korur."},"facet_ids":["F001"],"text":"onu yapmalısın","usage_role":"contextual"},{"applicability":"Kalıbın muhatabı işe yönelten özendirme işlevinin baskın olduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşin önceden var olan bir yükümlülük olarak muhataba düştüğünü zorunlu biçimde bildirmez.","preserves":"Muhatabı söz konusu işi yapmaya yönelten güçlü çağrıyı korur."},"facet_ids":["F002"],"text":"haydi, onu üstlen","usage_role":"contextual"}],"definition":"Belirli bir kalıp içinde, bir şeyin kişiye düşen bir yükümlülük olduğunu bildirmek veya kişiyi onu yapmaya yöneltmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalıp, söz konusu işin muhataba düşen bir yükümlülük olduğunu bildirir."},{"facet_id":"F002","role":"extension","statement":"Aynı kalıp, muhatabı o işi üstlenmeye yönelten güçlü bir özendirme olarak kullanılabilir."}],"identity_rationale":"Kaynak ifadesi belirli bir kalıbı zorunluluk bildirme ve bir işi yapmaya yöneltme anlamlarıyla açıklar. Bu anlamın yalan söylemeyle doğrudan bir bileşeni yoktur ve yalnız söz konusu kalıp içinde geçerlidir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"şunu üstlen; sana düşer veya onu yapmalısın"}],"lexicalization_note":"Tanım yalnızca verilen kalıplaşmış söyleyişi açıklar; zorunluluk ve yöneltme anlamları yalın biçime taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yükümlülük, özendirme ve bağlayıcılıkla doğrudan sınır kuran üç aday seçildi, yalnızca çalışma azmi veya uzak kök dallarıyla ilişkili adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli kalıbın 'sana düşer, onu yap' değeridir; komşu dal genel emir ve buyurma sistemidir.","focus_only":"Zorunluluk ile güçlü yöneltmeyi yalnız belirli bir kalıplaşmış söyleyişte birleştirir.","gloss":"kalıplaşmış yükümlülük ile genel buyruk","neighbor_only":"Genel buyruk, yasak karşıtı emir ve buyruğa uyma alanlarını kapsar.","neighbor_ref":"root_000051/B002","relation_type":"near_synonym","shared_zone":"İki dal da muhataptan bir eylemi gerçekleştirmesini isteme veya bunu gerekli kılma alanındadır."},{"boundary_match":"partial","distinction":"Odak dal yükümlülük bildirimini de taşır ve belirli bir kalıba bağlıdır; komşu dalın çekirdeği genel teşvik ve kışkırtmadır.","focus_only":"Bir işin muhataba düşen yükümlülük olduğunu da bildirebilir.","gloss":"üstlenmeye yöneltme ile kışkırtma","neighbor_only":"Özellikle çatışmaya yönelik kışkırtma, teşvik ve harekete geçirme anlamlarını kapsar.","neighbor_ref":"root_000309/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da muhatabı bir eyleme kuvvetle yöneltme işlevinde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal kalıplaşmış bir çağrı ve yükümlülük bildirimidir; komşu dal dışsal bir hüküm veya güçle bağlayıcılık kurma işlemidir.","focus_only":"Söyleyiş yoluyla muhatabı işi üstlenmeye çağırır.","gloss":"sözel yöneltme ile bağlayıcı kılma","neighbor_only":"Bir şeyi hüküm, kanıt, yönetim veya zor kullanmayla kişiye bağlayıp kaçınılmaz kılar.","neighbor_ref":"root_001354/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir işin kişi için gerekli veya bağlayıcı hale gelmesi alanında kesişir."}],"source_phrase_ar":"كذب عليك كذا بمعنى الإغراء أي عليك به أو قد وجب عليك (maqayis); كذب عليكم الحج أي وجب عليكم ودونكم الحج (ayn); كذب عليك كذا وكذا في معنى الإغراء (jamhara); كذب عليكم الحج أي وجب (sihah); كذب عليك الحج قيل معناه وجب فعليك به (mufradat)","source_summary":"Kaynaklar bu kalıplaşmış söyleyişi, bir işin muhataba düşmesi ve muhatabın o işi yapmaya yöneltilmesi anlamlarında ortaklaşa açıklar.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه كذب عليك الحج والجهاد والعسل ونحوها إذا أريد الوجوب أو الإغراء أو دونك الشيء","what_is_not_ar":"لا يدخل فيه الإخبار بالكذب، ولا تكذيب المخاطب، ولا كذب الحملة أو اللبن"},"support_links":[]},{"boundary":"Anlam yalnız saldırı hamlesi bağlamında ve olumlu-olumsuz biçimlerin karşıtlığıyla geçerlidir; genel yalan veya genel cesaret anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001290/B004","candidate_links":[{"candidate_id":"cand_8968e623c23f2317dc57","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:2:1","qac_word_ref":"92:16:2","surface_ar":"كَذَّبَ"}],"gloss":"hamlede duraksamak; olumsuzda sonuna kadar ilerlemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olumlu kalıp, saldırıya geçtikten sonra durmayı, geri kalmayı veya korkaklık göstermeyi bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olumsuz kalıp, saldırganın durmadan ilerleyerek vuruşa kadar hamleyi sürdürdüğünü bildirir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Savaş hamlesine bağlı olumlu duraksama ile olumsuz kalıptaki kesintisiz ilerlemeyi birlikte karşılar.","boundary_detail":"Anlam yalnız saldırı hamlesi bağlamında ve olumlu-olumsuz biçimlerin karşıtlığıyla geçerlidir; genel yalan veya genel cesaret anlamı değildir.","branch_image_ar":"صدق الحملة أو كذبها","concept_gloss":"hamlede duraksamak; olumsuzda sonuna kadar ilerlemek","contextual_glosses":[{"applicability":"Saldırıya başladıktan sonra geri duran veya korkaklık gösteren kişi için olumlu kalıpta uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Olumsuz kalıbın durmaksızın ilerleyip vuruşa ulaşma anlamını kapsamaz.","preserves":"Hamleyi tamamlamadan geri durma ve cesaret yitirme yönünü korur."},"facet_ids":["F001"],"text":"hamleden caymak","usage_role":"contextual"},{"applicability":"Olumsuz kalıpta saldırganın vuruşa kadar ilerlemeyi sürdürdüğü bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Olumlu kalıptaki duraksama ve korkaklık anlamını kapsamaz.","preserves":"Hamlede durmama, korkmama ve saldırıyı vuruşa kadar sürdürme yönünü korur."},"facet_ids":["F002"],"text":"geri durmadan saldırmak","usage_role":"contextual"}],"definition":"Bir saldırı hamlesinde geri durup hamleyi tamamlamamak veya korkaklık göstermektir; olumsuz kalıpta ise durmadan ilerleyip vuruncaya kadar hamleyi sürdürmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olumlu kalıp, saldırıya geçtikten sonra durmayı, geri kalmayı veya korkaklık göstermeyi bildirir."},{"facet_id":"F002","role":"specialization","statement":"Olumsuz kalıp, saldırganın durmadan ilerleyerek vuruşa kadar hamleyi sürdürdüğünü bildirir."}],"identity_rationale":"Kaynak ifadesi savaş hamlesindeki iki karşıt kalıbı birlikte verir: olumlu biçim hamlede durma, geri çekilme veya korkaklık; olumsuz biçim ise durmadan ilerleyip vuruşa ulaşmadır. Dalın kimliği bu kutuplu kalıp düzenine uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"saldırıya geçti ama duraksadı veya korktu"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"saldırıya geçti ve vuruncaya kadar durmadı; korkmadı"}],"lexicalization_note":"Tanım savaş hamlesine bağlı iki kalıbı korur; duraksama ve kararlılıkla ilerleme anlamları yalın biçime genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hamlede durma, saldırının kendisi, cesaret ve kesintisiz hamlenin sonucu ile doğrudan sınır kuran dört aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir hamlenin seyri ve onun olumsuz karşıt kalıbıdır; komşu dal kişinin daha genel korkaklık niteliğidir.","focus_only":"Başlatılmış bir saldırı hamlesinin sürdürülüp sürdürülmediğini kalıp içinde değerlendirir.","gloss":"hamlede geri durma ile korkaklık","neighbor_only":"Kişinin genel olarak atılganlıktan kesilmiş ve korkak oluşunu betimler.","neighbor_ref":"root_001150/B008","relation_type":"near_neighbor","shared_zone":"Saldırıya devam etmeme, geri kalma ve korkaklık bağlamlarında iki alan kesişir."},{"boundary_match":"field_only","distinction":"Odak dal saldırının sürdürülme niteliğini bildirir; komşu dal saldırı ve koşu hareketinin kendisidir.","focus_only":"Hamlenin duraksama veya sonuna kadar sürme bakımından sonucunu değerlendirir.","gloss":"hamlenin seyri ile hücum eylemi","neighbor_only":"Düşmana saldırma, hücum etme ve koşma eyleminin kendisini bildirir.","neighbor_ref":"root_000782/B003","relation_type":"same_field","shared_zone":"İki dal da savaşta düşmana yönelen saldırı hamlesi alanındadır."},{"boundary_match":"partial","distinction":"Odak dal belirli saldırı kalıbında gerçekleşen davranışı değerlendirir; komşu dal daha genel bir cesaret ve atılganlık niteliğidir.","focus_only":"Olumlu ve olumsuz kalıplarla tek bir hamlede durma ya da sürdürme karşıtlığını kurar.","gloss":"hamleyi sürdürme ile cesaret","neighbor_only":"Genel cesaret, atılganlık ve düşmana doğru öne çıkma niteliğini bildirir.","neighbor_ref":"root_001207/B006","relation_type":"near_neighbor","shared_zone":"Hamleyi korkmadan sürdürme bağlamında iki anlam birbirine yaklaşır."},{"boundary_match":"partial","distinction":"Odak dal hamlenin kesintisiz sürmesini yeterli görür; komşu dal buna düşmanı yenme sonucunu da ekler.","focus_only":"Hamlede durma ile durmadan sürdürme karşıtlığını, zafer şartı aramadan bildirir.","gloss":"kesintisiz hamle ile yenilgiye uğratma","neighbor_only":"Kesintisiz bir saldırıyla karşı tarafı yenme sonucunu özellikle içerir.","neighbor_ref":"root_000003/B007","relation_type":"near_neighbor","shared_zone":"Duraksamadan yapılan saldırı hamlesi iki dalın ortak sahnesidir."}],"source_phrase_ar":"حمل فلان ثم كذب أي لم يصدق في الحملة (maqayis); حمل فلان على فلان فما كذب حتى طعن أو ضرب أي ما وقف (jamhara); حمل فلان فما كذب أي ما جبن (sihah); حمل فلان على قرنه فكذب (mufradat)","source_summary":"Kaynaklar saldırı hamlesini sürdürmeme ile korkaklık arasında bağ kurar; olumsuz kalıp ise durmayıp vuruşa kadar ilerleme anlamını verir.","sources":["MQ","JA","SI","MU"],"what_is_ar":"يدخل فيه كذب في الحملة إذا لم يصدقها أو جبن، ونفي الكذب عن الحملة إذا مضى فيها ولم يقف حتى يطعن أو يضرب","what_is_not_ar":"لا يدخل فيه الكذب في الخبر، ولا الإغراء، ولا وقوف الوحشي بعد شوط"},"support_links":["sup_a92207de518e12feb0c1"]},{"boundary":"Dal, 'yapmakta gecikmedi' değerindeki kalıpla sınırlıdır; genel hız, acele veya yalan anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001290/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:2:1","qac_word_ref":"92:16:2","surface_ar":"كَذَّبَ"}],"gloss":"gecikmeden yapmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, belirtilen işi yapmadan önce beklemez veya oyalanmaz."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Beklememenin sonucu, işin gecikmeden gerçekleştirilmesidir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıbın hem oyalanmama aşamasını hem de işi gecikmeden gerçekleştirme sonucunu özlü biçimde karşılar.","boundary_detail":"Dal, 'yapmakta gecikmedi' değerindeki kalıpla sınırlıdır; genel hız, acele veya yalan anlamı değildir.","branch_image_ar":"ما كذب أن فعل أي ما لبث","concept_gloss":"gecikmeden yapmak","contextual_glosses":[{"applicability":"Söz konusu işin beklenmeden gerçekleştiği geçmiş zaman anlatımlarında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Oyalanmama aşamasını ve işin gecikmeden gerçekleşmesini doğal kullanımda korur."},"facet_ids":["F001","F002"],"text":"hemen yaptı","usage_role":"contextual"}],"definition":"Belirli bir olumsuz kalıp içinde, bir kişinin söz konusu işi yapmakta oyalanmadığını ve gecikmeden yaptığını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, belirtilen işi yapmadan önce beklemez veya oyalanmaz."},{"facet_id":"F002","role":"extension","statement":"Beklememenin sonucu, işin gecikmeden gerçekleştirilmesidir."}],"identity_rationale":"Kaynak ifadesi yalnız belirli bir olumsuz kalıp içinde kişinin bir işi yapmakta oyalanmadığını ve gecikmediğini bildirir. Geçici dal çerçevesi bu yapıyı ve anlamı doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yapmakta gecikmedi; hemen yaptı"}],"lexicalization_note":"Tanım yalnız verilen olumsuz kalıbın gecikmeme anlamını açıklar; hız ve çabukluk yalın kökün anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gecikmeme, ilk anda yapma ve genel acele arasındaki sınırı en iyi gösteren üç aday seçildi, yalnız zaman veya tekrar alanını paylaşan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız kalıplaşmış gecikmeme anlamıdır; komşu dal benzer kalıbın yanında koşma hızına ilişkin ayrı bir alan da taşır.","focus_only":"Gecikmemeyi yalnız belirli bir 'yapmakta oyalanmadı' kalıbında bildirir.","gloss":"gecikmeme ile az bekleme","neighbor_only":"Ayrı bir kullanımda koşmanın görece hızlı oluşunu da kapsar.","neighbor_ref":"root_000973/B009","relation_type":"near_synonym","shared_zone":"Bir işi yapmakta az bekleme veya hiç oyalanmama anlamında iki dal büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal bekleme süresinin yokluğuna odaklanır; komşu dal eylemin durumun ilk anındaki oluşunu ayrıca şart koşar.","focus_only":"Bir işi yapmak öncesindeki gecikmenin bulunmadığını kalıplaşmış biçimde bildirir.","gloss":"gecikmeden yapma ile ilk anda yapma","neighbor_only":"Eylemin ilk anda, durum henüz yatışmadan veya olayın başlangıç itkisiyle yapılmasını vurgular.","neighbor_ref":"root_001185/B002","relation_type":"near_synonym","shared_zone":"Bir eylemin beklenmeden ve hemen gerçekleşmesi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal yalnız gecikmenin yokluğunu bildirir; komşu dal hızlandırma, öne alma ve vaktinden önce isteme gibi ek yönler taşır.","focus_only":"Belirli bir işin yapılmasında gecikme olmadığını bildirir.","gloss":"gecikmeme ile acele etme","neighbor_only":"Bir şeyi vaktinden önce isteme, öne alma ve genel acele ettirme alanlarını kapsar.","neighbor_ref":"root_000987/B001","relation_type":"near_neighbor","shared_zone":"İşin kısa sürede veya beklenmeden yapılması bağlamında iki anlam kesişebilir."}],"source_phrase_ar":"ما كذب فلان أن فعل كذا أي ما لبث (maqayis;sihah)","source_summary":"Kaynakların ortak açıklaması, belirli kalıbın kişinin bir işi yapmakta beklemediğini ve gecikmediğini bildirmesidir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه قولهم ما كذب فلان أن فعل كذا إذا لم يلبث ولم يتأخر","what_is_not_ar":"لا يدخل فيه الكذب في الخبر، ولا وجوب كذب عليك، ولا كذب اللبن"},"support_links":[]},{"boundary":"Anlam yalnız dişi devenin sütüne ilişkin kalıpta, sütün kaybolması veya beklenen süre boyunca devam etmemesiyle sınırlıdır.","branch_kind":"collocation","branch_ref":"root_001290/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:2:1","qac_word_ref":"92:16:2","surface_ar":"كَذَّبَ"}],"gloss":"sütün kesilmesi veya beklenenden önce tükenmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi devenin sütü gider veya kesilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir açıklamada süt bir süre sürecek sanılır, fakat bu beklentinin tersine devam etmez."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi devenin sütüne bağlı kaybolma çekirdeğini ve devam beklentisinin boşa çıkmasını birlikte karşılar.","boundary_detail":"Anlam yalnız dişi devenin sütüne ilişkin kalıpta, sütün kaybolması veya beklenen süre boyunca devam etmemesiyle sınırlıdır.","branch_image_ar":"كذب لبن الناقة إذا ذهب ولم يدم","concept_gloss":"sütün kesilmesi veya beklenenden önce tükenmesi","contextual_glosses":[{"applicability":"Sütün artık gelmediği ve önceki üretimin sona erdiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sütün süreceği beklentisinin özellikle boşa çıkmış olduğunu tek başına bildirmez.","preserves":"Dişi devenin sütünün gitmesi veya sona ermesi çekirdeğini korur."},"facet_ids":["F001"],"text":"sütü kesildi","usage_role":"contextual"},{"applicability":"Sütün belirli bir süre devam edeceği beklentisinin gerçekleşmediği açıklayıcı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sütün devamına ilişkin beklentiyi ve beklenenden önce kesilmesini birlikte korur."},"facet_ids":["F001","F002"],"text":"sütü umulduğu kadar sürmedi","usage_role":"explanatory"}],"definition":"Dişi devenin sütünün kaybolması veya bir süre devam edeceği sanıldığı halde beklenenden önce kesilmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi devenin sütü gider veya kesilir."},{"facet_id":"F002","role":"source_variant","statement":"Bir açıklamada süt bir süre sürecek sanılır, fakat bu beklentinin tersine devam etmez."}],"identity_rationale":"Kaynak ifadesi dişi devenin sütünün gitmesini ortak çekirdek olarak verir; toplu kanıttaki ek açıklama, bir süre devam edeceği sanılan sütün beklenenden önce kesilmesini belirtir. Geçici çerçeve iki yönü de doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"dişi devenin sütü kesildi veya umulduğu kadar sürmedi"}],"lexicalization_note":"Tanım yalnız dişi devenin sütünü konu alan kalıba bağlıdır; genel tükenme veya genel beklenti boşa çıkması anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; süt kesilmesi, geri dönüş beklentisi ve süt bolluğu eksenini açıklayan üç aday seçildi, yalnız başka sıvıları veya hayvan özelliklerini paylaşan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dişi devenin sütüne ve kimi kullanımda boşa çıkan süreklilik beklentisine bağlıdır; komşu dal süt veriminin azalmasını ve yağmuru da kapsar.","focus_only":"Dişi devenin sütünün gitmesini ve beklenen süre boyunca devam etmemesini bildirir.","gloss":"sütün beklenmedik kesilmesi ile verimin azalması","neighbor_only":"Sütün azalmasını veya kesilmesini yağmurun azalması ve kesilmesiyle aynı anlam alanında kapsar.","neighbor_ref":"root_000305/B005","relation_type":"near_synonym","shared_zone":"Sütün azalması veya bütünüyle kesilmesi iki dalın doğrudan ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal gerçekleşen kaybı ve boşa çıkan devam beklentisini anlatır; komşu dal kayıptan sonraki geri dönüş umuduna odaklanır.","focus_only":"Sütün fiilen gittiğini veya beklenen süre boyunca devam etmediğini bildirir.","gloss":"sütün kesilmesi ile geri dönme umudu","neighbor_only":"Sütü kesilen ya da sütü kuşkulu olan hayvanda sütün geri dönmesi umudunu bildirir.","neighbor_ref":"root_001015/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da kesilmiş veya belirsiz hale gelmiş süt verimi durumunu konu alır."},{"boundary_match":"opposed","distinction":"Odak dal süt veriminin sona eren kutbundadır; komşu dal aynı alanın bol ve güçlü verim kutbundadır.","focus_only":"Sütün kaybolmasını, kesilmesini veya beklenenden az sürmesini bildirir.","gloss":"süt kesilmesi ile süt bolluğu","neighbor_only":"Dişi devenin süt bakımından çok verimli ve bol oluşunu bildirir.","neighbor_ref":"root_000200/B005","relation_type":"polarity_pair","shared_zone":"İki dal da dişi devenin süt veriminin durumu üzerinde ortak bir nicelik ekseni kurar."}],"source_phrase_ar":"كذب لبن الناقة ذهب وفيه نظر وقياسه صحيح (maqayis); كذب لبن الناقة أي ذهب (sihah); كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم (mufradat)","source_summary":"Toplu kanıt sütün gitmesi çekirdeğinde birleşir; bunun yanında, devam edeceği sanılan sütün beklenen süreyi tamamlamadan kesilmesi biçiminde daha ayrıntılı bir yorum da verir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه كذب لبن الناقة إذا ذهب أو ظن دوامه فلم يدم","what_is_not_ar":"لا يدخل فيه كذب الخبر، ولا كذب الحملة، ولا كذب عليك في الإغراء"},"support_links":[]},{"boundary":"Dal yalnız yaban hayvanının koşma, durma ve arkasına bakma dizisine bağlıdır; genel durma ya da genel koşu anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001290/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:2:1","qac_word_ref":"92:16:2","surface_ar":"كَذَّبَ"}],"gloss":"koşup arkasına bakmak için durmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yaban hayvanı önce belirli bir mesafe koşar, ardından hareketini durdurur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Durmanın amacı hayvanın arkasında kalan yere veya şeye bakmasıdır."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaban hayvanını, koşudan sonraki durmayı ve durmanın geriye bakma amacını birlikte karşılar.","boundary_detail":"Dal yalnız yaban hayvanının koşma, durma ve arkasına bakma dizisine bağlıdır; genel durma ya da genel koşu anlamı değildir.","branch_image_ar":"كذب الوحشي إذا جرى ثم وقف","concept_gloss":"koşup arkasına bakmak için durmak","contextual_glosses":[{"applicability":"Yaban hayvanının hareket dizisinin anlatı içinde doğal bir cümleyle çevrildiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önce koşmayı, sonra durup geride kalana bakmayı doğal anlatım sırasıyla korur."},"facet_ids":["F001","F002"],"text":"bir süre koştu, sonra dönüp baktı","usage_role":"contextual"}],"definition":"Bir yaban hayvanının belirli bir mesafe koştuktan sonra arkasında ne olduğunu görmek için durmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yaban hayvanı önce belirli bir mesafe koşar, ardından hareketini durdurur."},{"facet_id":"F002","role":"specialization","statement":"Durmanın amacı hayvanın arkasında kalan yere veya şeye bakmasıdır."}],"identity_rationale":"Tek kaynaklı ifade, yaban hayvanının belirli bir mesafe koşmasından sonra arkasına bakmak için durduğu aşamalı hareketi eksiksiz biçimde tanımlar. Geçici dal çerçevesi katılımcıyı, hareket sırasını ve amacı korur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yaban hayvanı bir mesafe koşup arkasına bakmak için durdu"}],"lexicalization_note":"Tanım yalnız yaban hayvanını özne alan kalıba ve belirtilen hareket dizisine bağlıdır; yalın biçime bir hareket anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hayvanda hareketin kesilmesi, ileri hareket ve bakış amacıyla doğrudan karşılaştırma sağlayan dört aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın katılımcısı yaban hayvanıdır ve amaç arkasına bakmaktır; komşu dal av köpeğinin ilgisini veya takibini kesmesine odaklanır.","focus_only":"Yaban hayvanı koşusunu geriye bakmak amacıyla durdurur.","gloss":"koşudan sonra durma ile avdan vazgeçme","neighbor_only":"Köpek avını yakaladıktan sonra gevşer, ondan döner veya başka şeyle oyalanır.","neighbor_ref":"root_001084/B005","relation_type":"near_synonym","shared_zone":"Bir hayvanın koşu veya takip hareketini bir aşamadan sonra kesmesi iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Odak dal belirli bir koşu-sonrası bakış dizisidir; komşu dal daha genel durdurma, kalma ve konaklama ilişkilerini kapsar.","focus_only":"Koşudan sonra özellikle geriye bakmak için gerçekleşen kısa durmayı bildirir.","gloss":"geriye bakmak için durma ile konaklama","neighbor_only":"Binek hayvanını tutmayı, bir yerde kalmayı, inmeyi veya bir kişiye yönelmeyi kapsar.","neighbor_ref":"root_000997/B003","relation_type":"near_neighbor","shared_zone":"Hareket halindeki bir canlının ilerlemeyi kesmesi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal koşu sonrasındaki durmayı temel alır; komşu dal kesintisiz ve güçlü ileri hareketi temel alır.","focus_only":"Koşunun ardından hareketin kesilmesini ve geriye bakmayı içerir.","gloss":"koşuyu kesme ile hızla ileri atılma","neighbor_only":"Binek hayvanının hızla ileri atılmasını ve kendini öne fırlatır gibi ilerlemesini bildirir.","neighbor_ref":"root_001209/B005","relation_type":"near_neighbor","shared_zone":"İki dal da hayvanın hızlı ilerleyişini konu alan hareket sahnesindedir."},{"boundary_match":"thematic_only","distinction":"Odak dalın çekirdeği koşu sonrasında durma dizisidir; komşu dal ise önceki bir hareket gerektirmeyen bakış eylemidir.","focus_only":"Bakışı, öncesindeki koşu ve durma dizisinin amacı olarak içerir.","gloss":"hareket dizisi ile dikkatli bakış","neighbor_only":"Baş veya gözleri kaldırarak bir şeye dikkatle bakma eylemini doğrudan bildirir.","neighbor_ref":"root_000256/B008","relation_type":"thematic","shared_zone":"Bir şeyi görmek üzere yöneltilen bakış, iki anlamın aynı sahnede bulunabilen unsurudur."}],"source_phrase_ar":"كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Yaban hayvanı bir mesafe koştuktan sonra arkasına bakmak için durur."}],"source_summary":"Bu özel kullanım tek bir kaynakta, yaban hayvanının koşu sonrasında arkasına bakmak amacıyla durduğu ardışık hareket olarak tanıklanır.","sources":["JA"],"what_is_ar":"يدخل فيه كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه","what_is_not_ar":"لا يدخل فيه كذب الحملة، ولا كذب اللبن، ولا الكذب في القول"},"support_links":[]},{"boundary":"Dal, ilgili yalın biçimin 'kişinin iç benliği' adını taşımasıyla sınırlıdır; kişinin yalan söylemesi veya benliğin aldatıcılığı anlamını içermez.","branch_kind":"bare","branch_ref":"root_001290/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:2:1","qac_word_ref":"92:16:2","surface_ar":"كَذَّبَ"}],"gloss":"iç benlik","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, bir yalan niteliği yüklemeden doğrudan kişinin iç benliğini adlandırır."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynak ifadesindeki doğrudan adlandırmayı, yalan söyleme niteliği eklemeden karşılar.","boundary_detail":"Dal, ilgili yalın biçimin 'kişinin iç benliği' adını taşımasıyla sınırlıdır; kişinin yalan söylemesi veya benliğin aldatıcılığı anlamını içermez.","branch_image_ar":"النفس الكذوب","concept_gloss":"iç benlik","contextual_glosses":[{"applicability":"Eski ve tek kaynaklı adlandırmanın modern Türkçede açıklanması gereken bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözcüğün kişiyi içeriden kuran benliği adlandırmasını açık biçimde korur."},"facet_ids":["F001"],"text":"kişinin kendi iç benliği","usage_role":"explanatory"}],"definition":"İlgili sözcüğün, kişideki iç benliği veya kendi olma bilincini doğrudan adlandıran bir isim olarak kullanılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, bir yalan niteliği yüklemeden doğrudan kişinin iç benliğini adlandırır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kaynak ifadesinde bulunmayan yalan söyleme veya aldatma niteliğini benliğe yükler.","collision":"Kişiyi yalan söyleyen biri olarak betimleyen başka daldaki sıfat anlamıyla karışır.","fit":"broadening","loses":null,"preserves":"Benliği konu alan bir adlandırma bulunduğu izlenimini kısmen korur."},"text":"yalancı benlik"}],"identity_rationale":"Kaynak ifadesi iç benliği 'yalancı' diye niteleyen bir söz öbeği kurmaz; ilgili sözcüğü doğrudan iç benliğin adı olarak eşitler. Dal korunabilir, ancak tanım bir ahlak niteliği değil, bağımsız bir adlandırma olarak yeniden çerçevelenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"iç benlik; kişinin kendisi"}],"lexicalization_note":"Tanım sözcüğün yalın biçimde doğrudan iç benliği adlandırmasını verir; başka dallardaki kişi sıfatları veya özel kalıplar bu anlama alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; iç benliği doğrudan adlandıran veya onun işlevini konu alan üç yararlı karşılaştırma seçildi, yalnız kişilik değişimi ve uzak tematik kullanımlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız iç benliği adlandırır; komşu dal iç benliği bedenin yaşamsal özü, kanı ve kalbiyle bir araya getiren daha geniş bir anlam kümesidir.","focus_only":"Tek bir sözcüğün doğrudan iç benlik adı olarak kullanımını bildirir.","gloss":"iç benlik ile yaşam özü","neighbor_only":"İç benliğin yanında kan, yaşam özü ve kalp gibi birbiriyle ilişkili adlandırmaları da kapsar.","neighbor_ref":"root_000187/B004","relation_type":"near_synonym","shared_zone":"Kişinin iç varlığı veya kendisi anlamında iki dal büyük ölçüde örtüşebilir."},{"boundary_match":"partial","distinction":"Odak dal bağımsız iç benlik adıdır; komşu dal bu değeri belirli bir kalıp içinde verir ve ayrıca yakın dost anlamına genişler.","focus_only":"Yalın bir sözcükle kişinin iç benliğini doğrudan adlandırır.","gloss":"iç benlik ile kişinin kendisi","neighbor_only":"Belirli bir soru kalıbında kişinin kendisini, başka kullanımda ise yakın ve seçkin dostu bildirir.","neighbor_ref":"root_000059/B006","relation_type":"near_synonym","shared_zone":"Kişinin kendisini veya iç benliğini gösteren kullanımlarda iki dal örtüşür."},{"boundary_match":"thematic_only","distinction":"Odak dal varlığın adıdır; komşu dal bu varlığa yüklenen süsleme ve yanıltıcı yönlendirme eylemidir.","focus_only":"İç benliği yalnızca bir varlık olarak adlandırır.","gloss":"iç benlik ile benliğin yönlendirmesi","neighbor_only":"İç benliğin veya kötülüğe yönelten bir gücün bir işi süsleyip kişiye çekici göstermesini bildirir.","neighbor_ref":"root_000763/B002","relation_type":"thematic","shared_zone":"İç benlik iki anlamın aynı düşünsel sahnesinde yer alır."}],"source_phrase_ar":"الكذوب النفس (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Sözcük herhangi bir ahlak niteliği eklenmeden doğrudan kişinin iç benliğini adlandırır."}],"source_summary":"Bu yalın adlandırma tek bir kaynakta, ilgili sözcüğün doğrudan kişinin iç benliğiyle eşitlenmesi biçiminde tanıklanır.","sources":["JA"],"what_is_ar":"يدخل فيه إطلاق الكذوب على النفس","what_is_not_ar":"لا يدخل فيه وصف الرجل بالكذاب أو الكذوب، ولا أكاذيب الأخبار"},"support_links":[]},{"boundary":"Dal, boyası veya deseni gerçek dokuma bezemesi sanısı veren kumaşla sınırlıdır; genel yalan, her desenli kumaş veya kişi adı değildir.","branch_kind":"bare","branch_ref":"root_001290/B009","candidate_links":[{"candidate_id":"cand_4c49c7f5485dfdf858d9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:2:1","qac_word_ref":"92:16:2","surface_ar":"كَذَّبَ"}],"gloss":"dokuma bezemesi sanısı veren boyalı kumaş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, çeşitli boya renkleriyle renklendirilmiş veya yüzeyine desen işlenmiş bir kumaştır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Boya ve desen, kumaşın dokuma yoluyla bezenmiş olduğu izlenimini verir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin kumaş oluşunu, boya veya deseni ve gerçek dokuma bezemesi gibi görünmesini birlikte karşılar.","boundary_detail":"Dal, boyası veya deseni gerçek dokuma bezemesi sanısı veren kumaşla sınırlıdır; genel yalan, her desenli kumaş veya kişi adı değildir.","branch_image_ar":"الكذابة ثوب يكذب بحاله","concept_gloss":"dokuma bezemesi sanısı veren boyalı kumaş","contextual_glosses":[{"applicability":"Kumaş türünün üretim görünüşüyle birlikte açıkça anlatılması gereken bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Boyama veya yüzey deseniyle oluşturulan dokuma bezemesi izlenimini korur."},"facet_ids":["F001","F002"],"text":"dokuma desenli gibi görünen boyalı kumaş","usage_role":"explanatory"}],"definition":"Çeşitli renklerle boyanmış veya desenlenmiş, bu yüzden dokuma yoluyla bezenmiş gibi görünen bir kumaş ya da giysidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, çeşitli boya renkleriyle renklendirilmiş veya yüzeyine desen işlenmiş bir kumaştır."},{"facet_id":"F002","role":"specialization","statement":"Boya ve desen, kumaşın dokuma yoluyla bezenmiş olduğu izlenimini verir."}],"identity_rationale":"Kaynak ifadesi çeşitli renklerle boyanmış veya desenlenmiş bir kumaşı, dokuma yoluyla bezenmiş gibi görünmesi üzerinden tanımlar; bir açıklama bu yanıltıcı görünüşü adlandırmanın gerekçesi yapar. Geçici çerçeve nesneyi ve görünüş ilişkisini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"dokuma bezemesi sanısı veren boyalı veya desenli kumaş"}],"lexicalization_note":"Tanım yalın bir kumaş adını ve onu ayıran görünüş özelliğini verir; genel aldatıcı görünüş anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dokuma bezemesi, renk etkisi, boyama, resimli kumaş ve yüzeyle yanıltma sınırlarını gösteren beş aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal boya veya desenin dokuma bezemesi sanısı vermesine dayanır; komşu dal gerçek dokuma bezemesi ve onun üretimiyle ilgilidir.","focus_only":"Boya veya yüzey deseniyle gerçek dokuma bezemesi varmış izlenimi veren kumaşı adlandırır.","gloss":"bezemeye benzeyen boya ile gerçek dokuma bezemesi","neighbor_only":"Kumaştaki gerçek dokuma bezemesini, kenar süslemesini ve bu işi yapanları kapsar.","neighbor_ref":"root_000340/B004","relation_type":"near_neighbor","shared_zone":"Kumaş yüzeyindeki bezeme görünüşü iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal dokuma bezemesi sanısına dayanır; komşu dal kumaş renginin bakışa göre değişmesine dayanır.","focus_only":"Birden çok boya veya desenle dokunmuş gibi görünen kumaşı bildirir.","gloss":"boyalı desen yanılsaması ile değişken renk görünüşü","neighbor_only":"Bakış açısına göre renkleri değişiyormuş gibi görünen belirli bir kumaş türünü bildirir.","neighbor_ref":"root_001252/B010","relation_type":"near_neighbor","shared_zone":"Renkli bir kumaşın görünüşünün algıda özel bir etki oluşturması iki dalda ortaktır."},{"boundary_match":"field_only","distinction":"Odak dal bezeme sanısı veren tasarlanmış görünüşü adlandırır; komşu dal belirli renkleri ve boyanın düzensiz tutmasını konu alır.","focus_only":"Çok renkli boya veya desenin dokuma bezemesi izlenimi vermesini temel alır.","gloss":"yanıltıcı bezeme ile alacalı boya","neighbor_only":"Sarı boya, belirli bitkisel renkler ve boyanın alacalı ya da iyi tutmamış çıkmasını kapsar.","neighbor_ref":"root_001428/B005","relation_type":"same_field","shared_zone":"Her iki dal da boyanmış kumaşın renk ve yüzey görünüşü alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal üretim biçimini olduğundan farklı gösteren genel bezeme izlenimine dayanır; komşu dal belirli resim motifleriyle tanımlanır.","focus_only":"Boyanmış veya desenlenmiş yüzeyin dokuma bezemesi sanısı vermesini bildirir.","gloss":"bezeme sanısı veren kumaş ile resimli kumaş","neighbor_only":"Üzerinde kule biçimleri veya başka resimler bulunan belirli bir süslü kumaşı bildirir.","neighbor_ref":"root_000101/B005","relation_type":"same_field","shared_zone":"İki dal da yüzeyi resim veya desenle süslenmiş kumaşları konu alır."},{"boundary_match":"thematic_only","distinction":"Odak dal yalnız kumaş ve dokuma bezemesi görünüşüne bağlıdır; komşu dal metal kaplama işleminden genel yanıltıcı gösterime uzanır.","focus_only":"Kumaşta boya veya desenin dokuma bezemesi sanısı uyandırmasını bildirir.","gloss":"kumaş görünüşü ile kaplama yoluyla yanıltma","neighbor_only":"Bir metali altın veya gümüşle kaplamayı ve bir şeyi gerçek niteliğinden farklı göstermeyi bildirir.","neighbor_ref":"root_001458/B005","relation_type":"thematic","shared_zone":"Bir nesnenin yüzey işlemiyle üretim veya madde niteliğinden farklı görünmesi iki alanda ortaktır."}],"source_phrase_ar":"الكذابة ثوب يصبغ بألوان الصبغ كأنه موشي (ayn); الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله (mufradat)","source_summary":"Kaynaklar, çeşitli renklerle boyanıp desenlenen ve böylece dokuma bezemesi varmış gibi görünen bir kumaş üzerinde birleşir; toplu kanıt bu yanıltıcı görünüşü adlandırmanın gerekçesi olarak açıklar.","sources":["AY","MU"],"what_is_ar":"يدخل فيه الكذابة للثوب المصبوغ بألوان أو المنقوش كأنه موشى لأنه يكذب بحاله","what_is_not_ar":"لا يدخل فيه الكذب في القول، ولا التكذيب، ولا أسماء الأشخاص"},"support_links":["sup_bd3ee6a142530b3ed89d"]},{"boundary":"Dal, zamansal sıralanma veya yönetim anlamını değil, yakınlık ve bitişiklik sınırını taşır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"aralıksız yakınlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Arada ayırıcı unsur olmadan yakın, bitişik veya yanında olma."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin başka bir şeye bitişik ya da hemen yakın olduğunu anlatan genel çekirdek için uygundur.","boundary_detail":"Dal, zamansal sıralanma veya yönetim anlamını değil, yakınlık ve bitişiklik sınırını taşır.","concept_gloss":"aralıksız yakınlık","contextual_glosses":[{"applicability":"Bir kişinin hemen yanında veya yakınında bulunan şeyi doğal Türkçe bağlamda karşılar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yanındalık ve yakın bulunma değerini korur."},"facet_ids":["F001"],"text":"yanında bulunan","usage_role":"contextual"},{"applicability":"Ev veya yer örneklerinde arada mesafe bırakmayan komşuluğu verir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bitişiklik ve yakın komşuluk sınırını korur."},"facet_ids":["F001"],"text":"bitişik komşu","usage_role":"contextual"}],"definition":"Bir şeyin başka bir şeye araya yabancı bir unsur girmeden yakın, bitişik veya yanında olmasıdır. Bu yakınlık yer bakımından olabileceği gibi ilişki bakımından da kurulabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Arada ayırıcı unsur olmadan yakın, bitişik veya yanında olma."}],"identity_rationale":"Kaynak ifadesi, dalın temelini arada yabancı bir unsur bulunmadan yakın olma, bitişik durma veya yanında bulunma olarak verir. Yer, ilişki ve bir evin başka bir eve bitişik olması gibi kullanımlar bu aynı yakınlık çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yakınlık ve bitişiklik"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sana yakın veya yanında olan şey"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir eve bitişik olan ev"}],"lexicalization_note":"Çıplak yakınlık değeri ile kalıp içindeki ev veya yanındalık kullanımları ayrılarak korunur.","neighbor_coverage_note":"Tüm aday komşular yakınlık, yanındalık veya aynı kökün diğer dalları bakımından değerlendirildi; yalnız sınırı gerçekten keskinleştirenler yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda yakınlık çoğu kez şeyin hemen yanında veya onu izleyen konumda bulunmasıyla sınırlanır; komşu dal daha genel yakınlaşma ve yaklaştırma eylemlerine de açıktır.","focus_only":"Arada yabancı bir unsur bulunmaması ve bitişik yanındalık daha belirgindir.","gloss":"yakınlık","neighbor_only":"Genel yaklaşma, yakınlaştırma ve iki şey arasında yakınlık kurma alanı daha geniştir.","neighbor_ref":"root_000493/B001","relation_type":"near_synonym","shared_zone":"İki dal da yakın olma ve mesafenin azlığı alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği bitişik yakınlıktır; B002 aynı kesintisizlik fikrini zamansal veya eylemsel sıra halinde gerçekleşen öğelere uygular.","focus_only":"Yakınlık yer veya ilişki bakımından yan yana durma olarak kurulur.","gloss":"yakınlık ile ardışıklık","neighbor_only":"Ardışıklıkta bir şeyin başka bir şeyden sonra gelmesi ve sıra düzeni öne çıkar.","neighbor_ref":"root_001684/B002","relation_type":"near_neighbor","shared_zone":"İkisinde de araya yabancı bir unsur girmemesi önemlidir."}],"source_summary":"Kaynakların ortak anlatımı, bu dalı yakınlık ve bitişiklik çekirdeği etrafında toplar; kişinin yanındaki şey ve birbirine komşu ev örnekleri bu çekirdeğin uygulamalarıdır."},"support_links":[]},{"boundary":"Dal, mekansal yakınlık veya dostça destek anlamına genişletilmeden ardışık gerçekleşme ile sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"kesintisiz ardışıklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Şeylerin veya eylemlerin kesintisiz biçimde peş peşe gerçekleşmesi."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Peş peşe gelen şeyler, eylemler veya dönemler için dalın bütün çekirdeğini verir.","boundary_detail":"Dal, mekansal yakınlık veya dostça destek anlamına genişletilmeden ardışık gerçekleşme ile sınırlıdır.","concept_gloss":"kesintisiz ardışıklık","contextual_glosses":[{"applicability":"Atış, iş veya haberlerin ardı ardına geldiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sıra ve kesintisiz takip anlamını korur."},"facet_ids":["F001"],"text":"peş peşe","usage_role":"contextual"},{"applicability":"İki iş veya iki nesne arasında ardışık düzen kuran eylem bağlamına uyar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemler arasında sıra kurma değerini korur."},"facet_ids":["F001"],"text":"art arda yapmak","usage_role":"contextual"}],"definition":"İki veya daha çok şeyin ya da eylemin araya ilgisiz bir kesinti girmeden peş peşe gerçekleşmesidir. Düzen, art arda geliş ve süreklilik çekirdeği birlikte korunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Şeylerin veya eylemlerin kesintisiz biçimde peş peşe gerçekleşmesi."}],"identity_rationale":"Kaynak ifadesi, iki veya daha çok şeyin araya başka bir şey girmeden biri diğerinin ardından gelmesini anlatır. Atış, iş, ay ve yazıların peş peşe gelişi örnekleri bu sıra ve kesintisizlik çekirdeğini doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kesintisiz sıra"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"araya kesinti girmeden peş peşe oluş"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"şeyleri veya işleri peş peşe getirme"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"iki şeyi peş peşe getirmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"peş peşe isabet eden üç ok"}],"lexicalization_note":"Çıplak sıralanma değeri ile iki şey arasında kurulan veya örneklerdeki kalıplı kullanım ayrı tutulur.","neighbor_coverage_note":"Adaylar ardışıklık, takip ve aynı kökün yakın dalları açısından denetlendi; örnek tekrarı yapan adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal, aynı kökün yakınlık fikrinden gelen aralıksız sıra değerini taşır; komşu dal daha genel takip ve düzenli akış alanını kapsar.","focus_only":"Araya aynı diziden olmayan bir unsur girmemesi özellikle vurgulanır.","gloss":"kesintisiz takip","neighbor_only":"Okuma, konuşma veya ayların akışı gibi süreklilik örnekleri daha geniştir.","neighbor_ref":"root_000695/B001","relation_type":"near_synonym","shared_zone":"İki dal da şeylerin biri diğerinin ardından gelmesine dayanır."},{"boundary_match":"field_only","distinction":"B002 nesne ya da eylemlerin sıra halinde gelişiyle ilgilidir; B004 kişiler veya topluluklar arasında destekleyici bağlılık kurar.","focus_only":"Peş peşe gerçekleşme ve düzen anlamı vardır.","gloss":"sıra ile destek","neighbor_only":"Dostça yakınlık, sevgi, destek ve karşıtlığa karşı taraf tutma anlamı vardır.","neighbor_ref":"root_001684/B004","relation_type":"same_field","shared_zone":"İkisi de yakınlık veya bağ kurma alanında aynı kökten ayrılır."}],"source_summary":"Kaynakların ortak anlatımı, dalı şeyin şeyden sonra gelmesi, işlerin düzenli biçimde sıralanması ve araya yabancı bir kesinti girmemesi etrafında birleştirir."},"support_links":[]},{"boundary":"Dal, yalnız sevgi ve yardım anlamı değil, bir işin başına geçip onu yürütme anlamıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B003","candidate_links":[{"candidate_id":"cand_8968e623c23f2317dc57","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"bir işi üstlenip yönetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işi veya başkasının durumunu üstlenip yönetme ve yürütme."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yönetim, görev alma ve başkasının işini yürütme bağlamlarının hepsine uygulanabilir.","boundary_detail":"Dal, yalnız sevgi ve yardım anlamı değil, bir işin başına geçip onu yürütme anlamıdır.","concept_gloss":"bir işi üstlenip yönetme","contextual_glosses":[{"applicability":"Bir yer, iş veya görevin başına geçme bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başına geçme ve yürütme değerini korur."},"facet_ids":["F001"],"text":"yönetimini üstlenmek","usage_role":"contextual"},{"applicability":"Yetim, kadın veya başka bir kişinin işini gözetme bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sorumluluk ve gözetim değerini korur."},"facet_ids":["F001"],"text":"işlerine bakmak","usage_role":"contextual"}],"definition":"Bir işin, yerin veya başkasına ait durumun sorumluluğunu üstlenip onu yönetmek ve yürütmektir. Bu, resmi yönetimden bakım ve gözetim sorumluluğuna kadar uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işi veya başkasının durumunu üstlenip yönetme ve yürütme."}],"identity_rationale":"Kaynak ifadesi, bir işin, yerin veya kişinin işlerinin sorumluluğunu üstlenip yürütmeyi açıkça verir. Yönetim, yetki, görev üstlenme ve yetim ya da kadınla ilgili sorumluluk örnekleri aynı idare etme çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yönetim ve yetki alanı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir yeri veya işi yöneten kişi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"başkasının işlerinden sorumlu kişi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bir işi üstlenmek"}],"lexicalization_note":"Yönetim adı, görevli kişi ve işi üstlenme kalıbı aynı dalda ama kapsamları ayrılarak tutulur.","neighbor_coverage_note":"Yönetim, yetki, yardım ve aynı kökün ilişki dalları karşılaştırıldı; yalnız gerçek kapsam ayrımı veren komşular seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal görev üstlenme ve gözetimi birlikte içerir; komşu dal daha çok emir ve resmi yönetici konumunu öne çıkarır.","focus_only":"Gözetim ve başkasının işlerini yürütme gibi resmi olmayan sorumlulukları da kapsar.","gloss":"yönetim yetkisi","neighbor_only":"Buyruk sahibi yönetici ve resmen yönetici kılma alanı daha baskındır.","neighbor_ref":"root_000051/B003","relation_type":"near_synonym","shared_zone":"İki dal da yönetim ve işlerin başında bulunma alanında örtüşür."},{"boundary_match":"field_only","distinction":"B003 sorumluluk ve idare çekirdeğindedir; B004 birini sevmek, desteklemek veya onun yanında yer almakla sınırlıdır.","focus_only":"İşin başına geçme ve onu yürütme vardır.","gloss":"yönetim ile destek","neighbor_only":"Sevgi, dostluk ve yardım ederek taraf olma vardır.","neighbor_ref":"root_001684/B004","relation_type":"same_field","shared_zone":"İkisi de insanlar arası bağlılık ve yakın ilişki alanına dokunur."}],"source_summary":"Kaynakların ortak anlatımı, bu dalı yönetme, sorumluluk alma, bir yerin veya işin başına geçme ve korunmaya muhtaç kişinin işini yürütme alanında toplar."},"support_links":["sup_a92207de518e12feb0c1"]},{"boundary":"Dal, resmi yönetim veya özgür bırakmaya bağlı hukuki bağ anlamına indirgenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"yakın durup destek olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sevgi, dostluk, inanç veya yardım bağıyla birinin yanında yer alma."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sevgi, dostluk, inanç veya yardım bağıyla bir tarafı tutma bağlamlarında uygundur.","boundary_detail":"Dal, resmi yönetim veya özgür bırakmaya bağlı hukuki bağ anlamına indirgenmez.","concept_gloss":"yakın durup destek olma","contextual_glosses":[{"applicability":"Kişi veya topluluk için düşmanın karşıtı olan yakın destekçi bağlamına uyar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dostluk ve destek değerini korur."},"facet_ids":["F001"],"text":"dost ve destekçi","usage_role":"contextual"},{"applicability":"Birini sevme, kayırma veya yardım ederek destekleme eyleminde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taraf olma ve destekleme anlamını korur."},"facet_ids":["F001"],"text":"yanında yer almak","usage_role":"contextual"}],"definition":"Bir kişi veya topluluğa sevgi, dostluk, inanç ya da yardım bağıyla yakın durup onun yanında yer almaktır. Karşıtlık ekseninde düşmanın değil desteklenen tarafın yanında olma anlamı taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sevgi, dostluk, inanç veya yardım bağıyla birinin yanında yer alma."}],"identity_rationale":"Kaynak ifadesi, düşmanın karşıtı olan yakın tarafı, sevgi, destek, dostluk, inanç veya anlaşma bağıyla yanında olmayı birlikte verir. Bu dalda yakınlık, yönetim değil, taraf tutan ve yardım eden ilişki olarak işler.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"dost, seven veya destekleyen kişi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"destekçi, anlaşmalı dost veya yakın yoldaş"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"birini sevip destekleme veya kayırma"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birini sevmek, desteklemek veya kayırmak"}],"lexicalization_note":"Kişi adı, destek ilişkisi ve birini destekleme kalıbı karıştırılmadan aynı ilişki alanında açıklanır.","neighbor_coverage_note":"Sevgi, dostluk, destek ve akrabalık adayları karşılaştırıldı; yalnız okuyucunun karıştırabileceği sınırlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal sevgi bağını destek ve taraf olma ile birlikte kurar; komşu dal daha çok dostluğun içtenlik yönünü anlatır.","focus_only":"Sevgiyle birlikte yardım, taraf tutma ve düşmanın karşıtı olma vardır.","gloss":"dostluk ve destek","neighbor_only":"İçten dostluk ve sevgi bağı daha baskındır; yardım veya taraf tutma zorunlu değildir.","neighbor_ref":"root_000435/B003","relation_type":"near_neighbor","shared_zone":"İki dal da yakın dostluk ve sevgi ilişkisine dokunur."},{"boundary_match":"partial","distinction":"B004 yardım eden dost tarafı anlatır; B005 hukuki, soyla ilgili veya toplumsal statüden doğan özel bağı anlatır.","focus_only":"Destek, sevgi ve taraf olma ilişkisi öne çıkar.","gloss":"destek bağı ile statü bağı","neighbor_only":"Soy, özgür bırakma, komşuluk veya miras bağlantısı gibi statü bağı öne çıkar.","neighbor_ref":"root_001684/B005","relation_type":"near_neighbor","shared_zone":"İki dal da insanlar arasında yakın bağ ve karşılıklı yükümlülük alanına girer."}],"source_summary":"Kaynakların ortak anlatımı, dalı düşmana karşı yakın taraf olmak, sevmek, desteklemek, dost veya anlaşmalı yardımcı olmak ve inanç yahut arkadaşlık bakımından yakınlaşmak etrafında toplar."},"support_links":[]},{"boundary":"Dal, dostça destekten ayrılır; soy, özgür bırakma, komşuluk veya özel bağlılık ilişkisi ister.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"özel yakınlık ve bağlılık bağı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Soy, özgür bırakma, komşuluk veya hısımlıktan doğan özel bağlılık."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Soy, özgür bırakma, komşuluk veya hısımlıkla kurulan toplumsal ve hukuki bağlar için uygundur.","boundary_detail":"Dal, dostça destekten ayrılır; soy, özgür bırakma, komşuluk veya özel bağlılık ilişkisi ister.","concept_gloss":"özel yakınlık ve bağlılık bağı","contextual_glosses":[{"applicability":"Akrabalık ve özgür bırakmadan doğan özel ilişkiyi açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soy ve özgür bırakma kaynaklı bağı korur."},"facet_ids":["F001"],"text":"soy veya özgür bırakma bağı","usage_role":"explanatory"},{"applicability":"Soydan, anlaşmadan veya özel statüden bağlı kişiler topluluğu için doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlı kişiler ve yakınlık değerini korur."},"facet_ids":["F001"],"text":"yakın bağlılar","usage_role":"contextual"}],"definition":"Soy, özgür bırakma, komşuluk, hısımlık veya özel bağlılık sebebiyle kişileri birbirine bağlayan toplumsal ve hukuki yakınlık ilişkisidir. Bağ, miras, destek veya mensubiyet sonucunu doğurabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Soy, özgür bırakma, komşuluk veya hısımlıktan doğan özel bağlılık."}],"identity_rationale":"Kaynak ifadesi, özgür bırakan ve özgür bırakılan kişi, soy yakınları, destek veren anlaşmalı kişi, komşu, hısım ve bunlardan doğan özel bağları birlikte sayar. Bu dalda anlam genel yardım değil, belirli sosyal veya hukuki yakınlık statüsüdür.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"özgür bırakan, özgür bırakılan, soy yakını veya komşu gibi bağlı kişi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"özgür bırakma ilişkisine bağlı özel hak ve mensubiyet"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"soy yakınları veya özgür bırakma bağıyla bağlı kişiler"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"nimet veya özgür bırakma bağı kuran kişi"}],"lexicalization_note":"Çeşitli kişi adları ve özel bağ adı aynı statü alanında tutulur, genel destek anlamına yayılmaz.","neighbor_coverage_note":"Soy, hısımlık, özgür bırakma ve aynı kökün destek dalları denetlendi; genel destek adayları ayrı tutuldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal, belirli sözlük birimleriyle özgür bırakma ve statü adlarını da içerir; komşu dal daha genel soy ve bağlılık dokusunu anlatır.","focus_only":"Özgür bırakan ve özgür bırakılan kişi, komşu ve çeşitli bağlı kişi adları da sayılır.","gloss":"bağlılık bağı","neighbor_only":"Soy ve bağlılığın dokusu daha genel bir ilişki alanı olarak verilir.","neighbor_ref":"root_001348/B007","relation_type":"near_synonym","shared_zone":"İki dal da soy veya benzeri bağlılık ilişkisinin insanları birbirine bağlamasına dayanır."},{"boundary_match":"field_only","distinction":"B005 soy yakınlığını aşarak özgür bırakma ve komşuluk gibi statü bağlarını da içerir; komşu dal kan ve rahim yakınlığına odaklanır.","focus_only":"Özgür bırakma, komşuluk ve özel mensubiyet bağları da kapsamdadır.","gloss":"özel bağ ile akrabalık","neighbor_only":"Rahim ve kan bağına dayalı akrabalık çekirdeği öne çıkar.","neighbor_ref":"root_000552/B002","relation_type":"same_field","shared_zone":"İki dal da kişiler arasındaki yakın bağ alanındadır."}],"source_summary":"Kaynaklar bu dalı, soy yakınlığı, özgür bırakma ilişkisi, komşuluk, hısımlık, anlaşmalı bağlılık ve bunlara eşlik eden destek veya miras yükümlülüğü etrafında toplar."},"support_links":[]},{"boundary":"Dal, iş üstlenme veya yüz çevirme anlamına değil, bir şeye yönelme ve ona dönme anlamına bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B006","candidate_links":[{"candidate_id":"cand_4c49c7f5485dfdf858d9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"yüzünü veya dikkatini yöneltme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüz, duyu veya dikkati bir şeye doğru çevirip ona yönelme."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel yöneliş, dinleme veya dikkat verme bağlamlarını birlikte karşılar.","boundary_detail":"Dal, iş üstlenme veya yüz çevirme anlamına değil, bir şeye yönelme ve ona dönme anlamına bağlıdır.","concept_gloss":"yüzünü veya dikkatini yöneltme","contextual_glosses":[{"applicability":"Yüzün belirli bir yöne çevrildiği bağlamda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüzle yönelme değerini korur."},"facet_ids":["F001"],"text":"yüzünü çevirmek","usage_role":"contextual"},{"applicability":"İşitme, görme veya ilginin bir şeye yöneldiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duyu ve dikkat yönelişini korur."},"facet_ids":["F001"],"text":"dikkatini vermek","usage_role":"contextual"}],"definition":"Yüzü, gözü, kulağı veya dikkati bir şeye çevirip ona yönelmektir. Bazı kullanımlarda bu yönelme takip etme ya da razı olma tutumunu da taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüz, duyu veya dikkati bir şeye doğru çevirip ona yönelme."}],"identity_rationale":"Kaynak ifadesi, yüzü, kulağı veya gözü bir şeye yöneltmeyi ve ona dönük kabul, takip veya razı oluşu verir. Bu dal açıkça uzaklaşma değil, bedensel ya da dikkat yönünden yönelmedir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yüzünü bir şeye çevirmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yüzünü o yöne dönmüş veya ona uyan kişi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kulağını veya dikkatini bir şeye vermek"}],"lexicalization_note":"Yüz, işitme ve dikkat kalıpları yönelme çekirdeğinde tutulur; çıplak yönetim anlamı içeri alınmaz.","neighbor_coverage_note":"Yönelme, işitme, karşıya dönme ve yüz çevirme adayları değerlendirildi; ters kutup özellikle yayımlandı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"B006 yönelişi ve karşıya dönmeyi anlatır; B007 aynı eksenin tersinde, dönüp gitme veya ilgiyi kesme anlamını taşır.","focus_only":"Bir şeye doğru dönme, kabul veya dikkat verme vardır.","gloss":"yönelme ile yüz çevirme","neighbor_only":"Bir şeyden dönüp uzaklaşma, yüz çevirme veya dinlemeyi bırakma vardır.","neighbor_ref":"root_001684/B007","relation_type":"polarity_pair","shared_zone":"İki dal da yön değiştirme ve tutum alma ekseninde durur."},{"boundary_match":"partial","distinction":"Bu dal duyu ve dikkat yönelişini de içerir; komşu dal daha genel karşı karşıya oluş ve cephe yönünü anlatır.","focus_only":"Yüzün yanında işitme, göz ve razı oluş gibi tutum yönelişleri de kapsamdadır.","gloss":"yönelme","neighbor_only":"Karşı karşıya gelme ve genel cephe oluşturma alanı daha geniştir.","neighbor_ref":"root_001198/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeye yüzünü veya yönünü çevirme alanında örtüşür."}],"source_summary":"Kaynakların ortak anlatımı, dalı yüze, işitmeye veya göze yön verme, bir şeyi karşıya alıp ona dönme ve bu yönelişten doğan takip ya da razı oluş ile açıklar."},"support_links":["sup_bd3ee6a142530b3ed89d"]},{"boundary":"Dal yalnız bedensel dönüp gitme değildir; bedensel uzaklaşma ile tutum olarak yüz çevirme birlikte bulunur.","branch_kind":"collocation","branch_ref":"root_001684/B007","candidate_links":[{"candidate_id":"cand_ecbc550fc1c947233fc7","lane":"micro"},{"candidate_id":"cand_8968e623c23f2317dc57","lane":"micro"},{"candidate_id":"cand_4c49c7f5485dfdf858d9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"dönüp yüz çevirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dönüp uzaklaşma, yüz çevirme veya dinleme ve uyma bağını kesme."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel uzaklaşma ve tutum olarak ilgiyi kesme bağlamlarını birlikte karşılar.","boundary_detail":"Dal yalnız bedensel dönüp gitme değildir; bedensel uzaklaşma ile tutum olarak yüz çevirme birlikte bulunur.","concept_gloss":"dönüp yüz çevirme","contextual_glosses":[{"applicability":"Kaçış veya bedensel uzaklaşma bağlamlarında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dönüp gitme ve uzaklaşma değerini korur."},"facet_ids":["F001"],"text":"arkasını dönüp kaçmak","usage_role":"contextual"},{"applicability":"Birinden, bir işten veya buyruktan ilgiyi kesme bağlamına uyar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İlgiyi kesme ve reddedici uzaklaşmayı korur."},"facet_ids":["F001"],"text":"yüz çevirmek","usage_role":"contextual"}],"definition":"Bir şeyden bedenen dönüp uzaklaşmak veya ona kulak vermeyi ve uymayı bırakarak yüz çevirmektir. Kaçış, ayrılma ve ilgiyi kesme aynı sınır içinde kalır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dönüp uzaklaşma, yüz çevirme veya dinleme ve uyma bağını kesme."}],"identity_rationale":"Kaynak ifadesi, kişinin dönüp gitmesini, kaçarken arkasını dönmesini, birinden yüz çevirmesini ve dinleme ya da buyruğa uymayı bırakmasını verir. Bu nedenle dal, yönelmenin karşıtı olan uzaklaşma ve ilgiyi kesme anlamındadır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"arkasını dönüp kaçarak uzaklaşmak"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"birinden yüz çevirmek ve ilgiyi kesmek"}],"lexicalization_note":"Anlam kalıplı kullanımlara bağlıdır; çıplak köke yönetim veya destek anlamı yüklenmez.","neighbor_coverage_note":"Kaçış, reddetme, ilgiyi kesme ve aynı kökün yönelme dalı denetlendi; en keskin karşıtlıklar yayımlandı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"B007 uzaklaşma ve reddedici yön değişimini anlatır; B006 kabul edici veya dikkat veren yönelişi anlatır.","focus_only":"Bir şeyden dönüp uzaklaşma ve ilgiyi kesme vardır.","gloss":"yüz çevirme ile yönelme","neighbor_only":"Bir şeye doğru dönme, dikkat verme veya razı oluş vardır.","neighbor_ref":"root_001684/B006","relation_type":"polarity_pair","shared_zone":"İki dal da bedenin veya tutumun yön değiştirmesiyle ilgilidir."},{"boundary_match":"partial","distinction":"Bu dal bedensel uzaklaşmayı tutum olarak ilgiyi kesmeyle birleştirir; komşu dal arka taraf ve bozgun görüntüsünü daha açık taşır.","focus_only":"Dinlemeyi ve buyruğa uymayı bırakma gibi iç tutum boyutu da vardır.","gloss":"dönüp uzaklaşma","neighbor_only":"Savaşta arkayı dönme, bozgun ve arka yön vurgusu daha belirgindir.","neighbor_ref":"root_000458/B003","relation_type":"near_synonym","shared_zone":"İki dal da arkasını dönme, uzaklaşma ve yüz çevirme alanında örtüşür."}],"source_summary":"Kaynakların ortak anlatımı, dalı kaçışla dönüp gitme, birinden yüz çevirme ve dinleme ya da buyruğa uyma bağını kesme biçimlerinde açıklar."},"support_links":["sup_453f8fd81af0401ce204","sup_a92207de518e12feb0c1","sup_bd3ee6a142530b3ed89d"]},{"boundary":"Dal, kötü sonuç tehdidi taşıyan kalıptan ayrılır; burada uygunluk ve haklı öncelik vardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"daha uygun ve hak sahibi olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeye daha uygun, daha layık veya daha hak sahibi olma."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işe, şeye veya konuma en layık olanı belirtme bağlamlarında uygundur.","boundary_detail":"Dal, kötü sonuç tehdidi taşıyan kalıptan ayrılır; burada uygunluk ve haklı öncelik vardır.","concept_gloss":"daha uygun ve hak sahibi olma","contextual_glosses":[{"applicability":"Kişinin bir iş veya konuma başkasından daha uygun olduğu bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Layık olma ve öncelik değerini korur."},"facet_ids":["F001"],"text":"daha layık","usage_role":"contextual"},{"applicability":"Bir şey üzerinde haklı öncelik veya sahiplik önceliği belirtilirken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Haklı öncelik ve uygunluk anlamını korur."},"facet_ids":["F001"],"text":"daha hak sahibi","usage_role":"contextual"}],"definition":"Bir kişinin veya tarafın bir şeye başkasından daha uygun, daha layık ya da daha hak sahibi olmasıdır. Anlam bir tehdit değil, uygunluk ve öncelik yargısıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeye daha uygun, daha layık veya daha hak sahibi olma."}],"identity_rationale":"Kaynak ifadesi, bir kişinin bir şeye daha uygun, daha layık veya daha hak sahibi olmasını anlatır. Dal, tehdit kalıbıyla değil, öncelik ve yerindelik karşılaştırmasıyla tanımlanır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bir şeye daha uygun, daha layık veya daha hak sahibi olmak"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"iki daha haklı veya daha uygun kişi"}],"lexicalization_note":"Karşılaştırmalı uygunluk kalıbı ile iki kişinin daha haklı olması biçimi aynı öncelik sınırında tutulur.","neighbor_coverage_note":"Hak, uygunluk, öncelik ve aynı yüzey kalıbı adayları denetlendi; tehdit anlamı ayrı dalda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bir şeye en layık veya daha hak sahibi olmayı karşılaştırmalı verir; komşu dal hakkın kendisini ve ona sahip olmayı daha özel anlatır.","focus_only":"Karşılaştırmalı olarak daha layık veya daha uygun olma vurgusu vardır.","gloss":"haklı öncelik","neighbor_only":"Belirli bir hakkın mülk veya talep olarak sabit olması daha baskındır.","neighbor_ref":"root_000347/B003","relation_type":"near_synonym","shared_zone":"İki dal da hak, uygunluk ve öncelik alanında örtüşür."},{"boundary_match":"partial","distinction":"B008 uygunluğu öncelik ve haklılık karşılaştırmasıyla kurar; komşu dal genel ehillik ve yaraşırlık alanında kalabilir.","focus_only":"Hak sahibi olma ve öncelik karşılaştırması açıkça bulunur.","gloss":"uygun olma","neighbor_only":"Bir kişi veya şeyin uygun, ehil ya da yaraşır olması daha genel verilir.","neighbor_ref":"root_000064/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir şeye yaraşma ve uygunluk alanında buluşur."}],"source_summary":"Kaynakların ortak anlatımı, dalı bir işe veya nesneye daha layık, daha uygun ve daha hak sahibi olma karşılaştırması olarak verir; iki kişinin en haklı olması da bu kapsamdadır."},"support_links":[]},{"boundary":"Dal yalnız belirli tehdit ve uyarı kalıbında geçerlidir; uygunluk karşılaştırması değildir.","branch_kind":"non_bare","branch_ref":"root_001684/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"yaklaşan kötü sonuç tehdidi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yaklaşan kötü sonuçla tehdit etme, uyarma veya kaçırılana hayıflandırma."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Muhataba kötü akıbetin yaklaştığını bildiren uyarı ve tehdit sözü için uygundur.","boundary_detail":"Dal yalnız belirli tehdit ve uyarı kalıbında geçerlidir; uygunluk karşılaştırması değildir.","concept_gloss":"yaklaşan kötü sonuç tehdidi","contextual_glosses":[{"applicability":"Kötü sonucun yaklaştığını sezdiren tehditli hitap bağlamlarında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tehdit ve yaklaşan kötü sonuç değerini korur."},"facet_ids":["F001"],"text":"yazık sana, başına gelecek var","usage_role":"contextual"},{"applicability":"Kaçırılan şey üzerine acı hatırlatma anlamı öne çıktığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayıflandırma ve uyarı değerini korur."},"facet_ids":["F001"],"text":"kaçırdığına hayıflanma","usage_role":"explanatory"}],"definition":"Muhataba kötü bir sonucun yaklaştığını bildiren tehdit ya da uyarı kalıbıdır. Bazı kullanımlarda kaçırılan şey için acı bir hatırlatma veya hayıflanma da taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yaklaşan kötü sonuçla tehdit etme, uyarma veya kaçırılana hayıflandırma."}],"identity_rationale":"Kaynak ifadesi, kalıbın tehdit, uyarı, yaklaşan kötü sonuç veya kaçırılan şey için acı hatırlatma değeri taşıdığını söyler. Bu nedenle dal, B008'deki uygunluk ve hak sahibi olma anlamından ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"tehdit ve uyarı sözü; sana kötü şey yaklaştı"}],"lexicalization_note":"Anlam belirli sözlü kalıba bağlıdır; çıplak öncelik veya yakınlık anlamı olarak genellenmez.","neighbor_coverage_note":"Tehdit, yıkım ve aynı kalıptan doğan uygunluk adayı denetlendi; söz kalıbı dışındaki zarar dalları ayrı tutuldu.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"B009 kalıplaşmış bir uyarı ve tehdit sözüdür; B008 uygunluk ve haklı öncelik yargısıdır.","focus_only":"Tehdit, kötü sonuç ve hayıflanma kalıbı vardır.","gloss":"tehdit ile öncelik","neighbor_only":"Bir şeye daha layık, daha uygun veya daha hak sahibi olma vardır.","neighbor_ref":"root_001684/B008","relation_type":"other","shared_zone":"Aynı yüzey kalıbı okuyucuda karışıklık yaratabilir."},{"boundary_match":"partial","distinction":"Bu dal zararın kendisini değil, muhataba yaklaşan zararı bildiren kalıbı anlatır; komşu dal yıkım veya yok oluşun kendisidir.","focus_only":"Kötü sonucun yaklaştığını söyleyen sözlü tehdit vardır.","gloss":"tehdit ve yıkım","neighbor_only":"Gerçek yıkım, yok etme veya bozma eylemi anlatılır.","neighbor_ref":"root_000174/B001","relation_type":"near_neighbor","shared_zone":"İki dal da kötü sonuç ve zarar alanına dokunur."}],"source_summary":"Kaynakların ortak anlatımı, dalı muhataba kötü ya da yıkıcı bir şeyin yaklaştığını sezdiren tehdit ve uyarı sözü olarak verir; ayrıca kaçırılan şey üzerine acı hatırlatma değeri bulunur."},"support_links":[]},{"boundary":"Dal genel yağmur adı değildir; önceki yağmuru izleyen özel yağmurla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"önceki yağmuru izleyen yağmur","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Önceki veya erken mevsim yağmurunu izleyen yağmur."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yağmurun özel ad olarak bir önceki yağmurdan sonra gelişini anlatan bağlamlarda uygundur.","boundary_detail":"Dal genel yağmur adı değildir; önceki yağmuru izleyen özel yağmurla sınırlıdır.","concept_gloss":"önceki yağmuru izleyen yağmur","contextual_glosses":[{"applicability":"Önceki mevsim yağmurunu izleyen yağmur bağlamında doğal ve kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İzleyen yağmur anlamını korur."},"facet_ids":["F001"],"text":"sonraki yağmur","usage_role":"contextual"},{"applicability":"Toprağın özel izleyen yağmurla ıslanması bağlamında açıklayıcıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Toprağın izleyen yağmuru alması değerini korur."},"facet_ids":["F001"],"text":"toprak bu yağmuru aldı","usage_role":"explanatory"}],"definition":"İlk mevsim yağmurundan ya da önceki yağmurdan sonra gelen yağmurdur. Toprağın bu yağmuru alması ve iyiliğin iyilik ardınca gelmesi gibi özel kullanımlar bu izleme fikrine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Önceki veya erken mevsim yağmurunu izleyen yağmur."}],"identity_rationale":"Kaynak ifadesi, bu dalı erken mevsim yağmurundan veya önceki yağmurdan sonra gelen yağmur adı olarak verir. Toprağın bu yağmuru alması ve dua kalıbındaki ardışık iyilik ifadesi de aynı izleme ilişkisine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"önceki yağmurdan sonra gelen yağmur"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"erken mevsim yağmurunu izleyen yağmur adı"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"toprağa izleyen yağmurun yağması"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"iyilik ardından gelen yağmur veya iyilik"}],"lexicalization_note":"Yağmur adı, toprağın bu yağmuru alması ve dua kalıbındaki özel kullanım ayrı ayrı korunur.","neighbor_coverage_note":"Yağmur adayları sıralanma, miktar ve toprakla ilişki bakımından değerlendirildi; genel yağmur adları yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal adlandırmayı önceki yağmurun ardından gelmeye bağlar; komşu dal toprağın tekrar yağmur alması veya erken mevsim zamanı yönünden daha geniştir.","focus_only":"Özellikle erken mevsim yağmurunu veya önceki yağmuru izleyen yağmur adı olarak verilir.","gloss":"izleyen yağmur","neighbor_only":"Daha önce ıslanmış toprağı tekrar yoklayan yağmur veya erken mevsim yağmuru alanı daha geniştir.","neighbor_ref":"root_001055/B007","relation_type":"near_synonym","shared_zone":"İki dal da önceki yağmurla ilişkili sonraki yağmur alanında örtüşür."},{"boundary_match":"field_only","distinction":"B010 yağmurun sırasını ve önceki yağmurla ilişkisini tanımlar; komşu dal yağmurun miktarı ve bolluğunu tanımlar.","focus_only":"Yağmurun önceki yağmuru izlemesi belirleyicidir.","gloss":"sonraki yağmur ile bol yağmur","neighbor_only":"Yağmurun çokluğu ve bereketli oluşu belirleyicidir.","neighbor_ref":"root_000274/B002","relation_type":"same_field","shared_zone":"İki dal da yağmur adlandırması alanındadır."}],"source_summary":"Kaynakların ortak anlatımı, dalı önceki yağmuru veya erken mevsim yağmurunu izleyen yağmur olarak açıklar; toprağın bu yağmuru alması da aynı adlandırmaya bağlanır."},"support_links":[]},{"boundary":"Dal çıplak somut addır; yönetim, yağmur veya başka aynı sesli kullanımlar buna taşınmaz.","branch_kind":"bare","branch_ref":"root_001684/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"deve sırtı alt örtüsü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Deve sırtında semer veya yük takımı altında kullanılan örtü ya da altlık."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Devenin sırtında semer veya yük takımı altında kullanılan örtü için uygundur.","boundary_detail":"Dal çıplak somut addır; yönetim, yağmur veya başka aynı sesli kullanımlar buna taşınmaz.","concept_gloss":"deve sırtı alt örtüsü","contextual_glosses":[{"applicability":"Deve veya yük hayvanı takımının altında kullanılan örtü bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alt örtü ve semerle ilişkiyi korur."},"facet_ids":["F001"],"text":"semer altı örtüsü","usage_role":"contextual"}],"definition":"Devenin sırtına, semer ya da yük takımı altına konan örtü, keçe veya benzeri altlıktır. Tekil ve çoğul biçimler aynı eşya sınıfına bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Deve sırtında semer veya yük takımı altında kullanılan örtü ya da altlık."}],"identity_rationale":"Kaynak ifadesi, dalı devenin sırtına konan, semer veya yük altındaki örtü ya da benzeri parça olarak verir. Bu somut eşya anlamı yönetim, yağmur veya yakınlık dallarından ayrı tutulur.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"deve sırtında semer altında kullanılan örtü"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"semer altı örtüleri"}],"lexicalization_note":"Çıplak eşya adı tanımlanır; kalıp dışı soyut anlamlar bu dala alınmaz.","neighbor_coverage_note":"Deve takımı, örtü, yastık ve taşıma araçları adayları denetlendi; nesnenin altlık işlevini ayıranlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal altlık olarak kullanılan örtüyü tanımlar; komşu dal deve sırtındaki daha genel binek veya örtü takımını kapsar.","focus_only":"Örtünün semer veya takım altında yer alması belirleyicidir.","gloss":"semer altı örtüsü","neighbor_only":"Deve sırtındaki daha genel örtü, küçük semer veya takım parçası alanı vardır.","neighbor_ref":"root_000766/B010","relation_type":"near_neighbor","shared_zone":"İki dal da deve sırtında kullanılan örtü veya takım parçası alanındadır."},{"boundary_match":"field_only","distinction":"B011 asıl takımın altında kalan örtüyü belirtir; komşu dal semer veya binek takımının kendisini anlatır.","focus_only":"Semerin altında kalan örtü veya altlık nesnedir.","gloss":"alt örtü ile semer","neighbor_only":"Devenin asıl binek takımı veya semeri anlatılır.","neighbor_ref":"root_000551/B002","relation_type":"same_field","shared_zone":"İki dal da deve üzerinde kullanılan binek takımı alanındadır."}],"source_summary":"Kaynakların ortak anlatımı, dalı devenin sırtında semer veya benzeri takım altında kullanılan örtü, keçe ya da altlık olarak verir; çoğul biçim aynı nesnenin çoğuludur."},"support_links":[]},{"boundary":"Dal, görev üstlenme değil, kalıplı olarak bir şeyi ele geçirme veya hedefe varmadır.","branch_kind":"collocation","branch_ref":"root_001684/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"ele geçirip hedefe ulaşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi ele geçirip ona üstün gelme veya yarış hedefine ulaşma."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyi kontrol altına alma veya yarışta son noktaya varma bağlamlarında uygundur.","boundary_detail":"Dal, görev üstlenme değil, kalıplı olarak bir şeyi ele geçirme veya hedefe varmadır.","concept_gloss":"ele geçirip hedefe ulaşma","contextual_glosses":[{"applicability":"Mal veya nesne üzerinde üstünlük kurma bağlamlarında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ele geçirme ve kontrol değerini korur."},"facet_ids":["F001"],"text":"eline geçirmek","usage_role":"contextual"},{"applicability":"Yarış veya mesafe sonuna ulaşma bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hedefe ulaşma değerini korur."},"facet_ids":["F001"],"text":"hedefe varmak","usage_role":"contextual"}],"definition":"Bir şeyin kişinin eline geçmesi, onun üzerinde üstünlük kurması veya yarışta hedefe varıp onu elde etmesidir. Sahip olma, galip gelme ve hedefe ulaşma sonuçları birlikte korunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi ele geçirip ona üstün gelme veya yarış hedefine ulaşma."}],"identity_rationale":"Kaynak ifadesi, bir şeyin kişinin eline geçmesini veya onun üzerinde üstün gelmesini ve yarış bağlamında son noktaya varıp onu geçerek elde etmesini verir. Dalda ele geçirme ile hedefe varma aynı üstün gelme sonucuna bağlanır.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"bir şeyi ele geçirmek veya ona üstün gelmek"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"hedefe varmak veya ona önce ulaşmak"}],"lexicalization_note":"Anlam belirli kalıplara bağlıdır; çıplak yönetim veya yakınlık anlamına genellenmez.","neighbor_coverage_note":"Ele geçirme, üstünlük, hedefe varma ve yönetim adayları denetlendi; görev üstlenme dalları ayrı tutuldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B012 ele geçirmeyi hedefe varma kullanımıyla birlikte verir; komşu dal daha genel üstünlük, kuşatma ve toplama alanını kapsar.","focus_only":"Yarış hedefine varma ve hedefi önde alma kullanımı da vardır.","gloss":"ele geçirme","neighbor_only":"Toplama, kuşatma ve geniş anlamda kontrol altına alma alanı daha geniştir.","neighbor_ref":"root_000368/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir şey üzerinde üstünlük ve kontrol kurma alanında örtüşür."},{"boundary_match":"field_only","distinction":"B012 sonuç olarak elde etme veya hedefe ulaşmayı ister; komşu dal üstünlük ve galiplik alanında daha geniştir.","focus_only":"Bir şeyin elde edilmesi veya hedefe varılması belirleyicidir.","gloss":"ele geçirme ile üstünlük","neighbor_only":"Üstünlük, yükseklik veya galiplik niteliği daha genel anlatılır.","neighbor_ref":"root_000104/B008","relation_type":"same_field","shared_zone":"İki dal da galip gelme ve üstün konuma geçme alanına dokunur."}],"source_summary":"Kaynakların ortak anlatımı, dalı bir şeyin ele geçmesi, mal üzerinde üstünlük kurulması ve yarış ya da mesafe bağlamında hedefe varılıp orada üstün gelinmesi olarak açıklar."},"support_links":[]},{"boundary":"Dal kalıplı verme ve yöneltme anlamındadır; yönetim veya öncelik anlamına genellenmez.","branch_kind":"collocation","branch_ref":"root_001684/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"birine iyi ya da kötü şey yöneltme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birine iyi veya kötü bir şeyi yöneltip ulaştırma ya da payına kılma."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye yarar, iyilik, zarar veya başka bir şeyi ulaştırma bağlamlarında uygundur.","boundary_detail":"Dal kalıplı verme ve yöneltme anlamındadır; yönetim veya öncelik anlamına genellenmez.","concept_gloss":"birine iyi ya da kötü şey yöneltme","contextual_glosses":[{"applicability":"Birine iyilik ulaştırma bağlamında doğal Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İyiliği kişiye ulaştırma değerini korur."},"facet_ids":["F001"],"text":"iyilikte bulunmak","usage_role":"contextual"},{"applicability":"Birine kötü bir şey yöneltme bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kötü şeyi kişiye yöneltme değerini korur."},"facet_ids":["F001"],"text":"zarar yöneltmek","usage_role":"contextual"}],"definition":"Bir şeyi, iyiliği, yararı veya kötülüğü bir kişiye yöneltip ona ulaştırmak ya da onun payına kılmaktır. Verilen şeyin iyi veya kötü olması dalın kapsamını değiştirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birine iyi veya kötü bir şeyi yöneltip ulaştırma ya da payına kılma."}],"identity_rationale":"Kaynak ifadesi, birine bir şey, iyilik, kötülük veya yarar yöneltmeyi ve onu o kişiye ulaştırmayı verir. Dal, görevi üstlenmek veya daha haklı olmak değil, bir şeyi birine tahsis edip ulaştırmaktır.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"birine iyilik yapmak veya bir şeyi ona ulaştırmak"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"birine iyilik veya kötülük yöneltmek"}],"lexicalization_note":"Anlam birine bir şey, iyilik veya kötülük yöneltme kalıbına bağlı tutulur.","neighbor_coverage_note":"Verme, ulaştırma, kazandırma ve satış adayları değerlendirildi; yalnız yöneltme çekirdeğini aydınlatanlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B013 verilen şeyin kişiye yöneltilmesini ve iyilik ya da kötülük olabilmesini vurgular; komşu dal genel verme ve getirme anlamındadır.","focus_only":"İyi ya da kötü bir şeyin belirli kişiye yöneltilmesi vurgulanır.","gloss":"birine verme","neighbor_only":"Genel verme, getirme veya bir şeyi birine sunma alanı daha geniştir.","neighbor_ref":"root_000009/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi bir kişiye ulaştırma alanında örtüşür."},{"boundary_match":"partial","distinction":"B013 iyi ve kötü yöneltmeyi birlikte kapsar; komşu dal başkasına yarar veya mal kazandırmaya odaklanır.","focus_only":"Kötülük veya zarar yöneltme de kapsam içindedir.","gloss":"yarar ulaştırma","neighbor_only":"Başkasına mal veya yarar kazandırma daha özel ve olumlu yöndedir.","neighbor_ref":"root_001296/B002","relation_type":"near_neighbor","shared_zone":"İki dal da kişiye bir yarar veya şey kazandırma alanına yaklaşır."}],"source_summary":"Kaynakların ortak anlatımı, dalı bir kişiye iyilik, yarar, kötülük veya herhangi bir şeyi ulaştırma ve onun üzerine yöneltme olarak açıklar."},"support_links":[]},{"boundary":"Dal yalnız satıştaki özel devir işlemidir; genel alım satım veya bağış anlamına genişletilmez.","branch_kind":"non_bare","branch_ref":"root_001684/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"aldığı fiyatla devretme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Satın alınan malı bilinen aynı fiyatla başka birine devretme."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Alım satımda malın satın alındığı bilinen fiyat üzerinden devredildiği özel işlem için uygundur.","boundary_detail":"Dal yalnız satıştaki özel devir işlemidir; genel alım satım veya bağış anlamına genişletilmez.","concept_gloss":"aldığı fiyatla devretme","contextual_glosses":[{"applicability":"Ticari işlem bağlamında malın alındığı fiyatla başkasına geçirilmesini doğal biçimde verir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aynı fiyatla devir şartını korur."},"facet_ids":["F001"],"text":"maliyet fiyatına devretmek","usage_role":"contextual"}],"definition":"Bir malı bilinen bir fiyatla satın aldıktan sonra aynı fiyatla başka birine devretme işlemidir. Anlam, satış içindeki özel fiyat ve devir şartına bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Satın alınan malı bilinen aynı fiyatla başka birine devretme."}],"identity_rationale":"Kaynak ifadesi, bir malı bilinen bir fiyatla satın aldıktan sonra aynı fiyatla başka birine devretme işlemini açıkça verir. Bu tekil ticaret terimi, yönetim veya genel verme anlamlarından ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"satın alınan malı bilinen aynı fiyatla başkasına devretme"}],"lexicalization_note":"Anlam satış alanındaki belirli terime bağlıdır; çıplak kök anlamına taşınmaz.","neighbor_coverage_note":"Satış, fiyat, devir ve genel verme adayları denetlendi; yalnız ticari işlem sınırını gösterenler yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"B014 genel satış değil, alınmış malı alış fiyatıyla devretme terimidir; komşu dal satış ve satın alma işlemini genel olarak anlatır.","focus_only":"Malın önce alınması ve aynı bilinen fiyatla devredilmesi şarttır.","gloss":"özel devir ile alım satım","neighbor_only":"Alım ve satımın genel karşılıklı işlem alanı vardır.","neighbor_ref":"root_000169/B001","relation_type":"same_field","shared_zone":"İki dal da ticari alım satım alanındadır."},{"boundary_match":"field_only","distinction":"B014 fiyatı şart olarak kullanan bir işlem adıdır; komşu dal bedel veya fiyat kavramının kendisini verir.","focus_only":"Aynı fiyatla başka kişiye devir işlemi anlatılır.","gloss":"devir işlemi ile fiyat","neighbor_only":"Fiyatın, bedelin veya değerin kendisi anlatılır.","neighbor_ref":"root_000206/B001","relation_type":"same_field","shared_zone":"İki dal da satışta bedel ve fiyat alanına dokunur."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanık, bu kullanımı bilinen fiyatla alınan malın aynı fiyatla başka kişiye devri olarak verir."}],"source_summary":"Bu dal, satış alanında belirli bir işlem adı olarak sunulur; malın önce bilinen fiyatla alınması ve sonra aynı fiyatla başka kişiye devredilmesi şartı belirleyicidir."},"support_links":[]},{"boundary":"Dal hayvan sürüsündeki ayırma ve sütten kesme uygulamasına bağlıdır; genel ardışıklık değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"küçük sürü hayvanlarını ayırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Küçük sürü hayvanlarını büyüklerinden veya yavruları analarından ayırma."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Küçük hayvanları büyüklerinden veya yavruları analarından ayırma bağlamlarında uygundur.","boundary_detail":"Dal hayvan sürüsündeki ayırma ve sütten kesme uygulamasına bağlıdır; genel ardışıklık değildir.","concept_gloss":"küçük sürü hayvanlarını ayırma","contextual_glosses":[{"applicability":"Yavru develerin analarından kesilmesi ve alıştırılması bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Anadan ayırma ve alıştırma değerini korur."},"facet_ids":["F001"],"text":"yavruları anadan ayırmak","usage_role":"contextual"},{"applicability":"Sürü içindeki küçük hayvanların büyüklerden ayrıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sürü içinde ayırma değerini korur."},"facet_ids":["F001"],"text":"küçükleri büyüklerden ayırmak","usage_role":"contextual"}],"definition":"Küçük sürü hayvanlarını büyüklerinden veya yavruları analarından ayırarak bağımsızlaşmaya ve yola gelmeye alıştırmaktır. Anlam, hayvancılıktaki ayırma ve sütten kesme uygulamasına bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Küçük sürü hayvanlarını büyüklerinden veya yavruları analarından ayırma."}],"identity_rationale":"Kaynak ifadesi, küçük sürü hayvanlarını büyüklerinden ayırmayı ve yavru develeri analarından keserek alıştırmayı verir. Bu dal, peş peşe geliş veya dostça destek anlamından farklı, hayvancılıkta ayırma ve alıştırma işlemidir.","lexical_glosses":[{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"küçük sürü hayvanlarını büyüklerinden ayırmak"},{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"yavru develeri analarından ayırıp alıştırma"}],"lexicalization_note":"Kalıplı sürü ayırma ve yavruyu anadan kesme kullanımları birlikte ama hayvancılık alanıyla sınırlı tutulur.","neighbor_coverage_note":"Küçük hayvan adları, buzağı ve deve yavrusu adayları ile aynı kökün ardışıklık dalı denetlendi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"B015 hayvancılık uygulaması olarak ayırmayı anlatır; komşu dal küçük hayvanların kendisini adlandırır.","focus_only":"Küçüklerin büyüklerden ayrılması veya yavruların anadan kesilmesi eylemi vardır.","gloss":"ayırma ile küçük hayvan adı","neighbor_only":"Küçük hayvanların adlandırılması ve sınıflanması öne çıkar.","neighbor_ref":"root_000160/B004","relation_type":"same_field","shared_zone":"İki dal da küçük sürü hayvanları alanındadır."},{"boundary_match":"field_only","distinction":"B015 sürüde ayırma işlemidir; B002 herhangi bir hayvancılık işlemi gerektirmeyen ardışık sıra anlamıdır.","focus_only":"Hayvanları ayırma ve alıştırma uygulamasıdır.","gloss":"ayırma ile ardışıklık","neighbor_only":"Şeylerin peş peşe gelişi ve kesintisiz sıra anlamıdır.","neighbor_ref":"root_001684/B002","relation_type":"other","shared_zone":"Aynı kökteki benzer yüzey biçimi karışıklık yaratabilir."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanık, kullanımı küçük hayvanları büyüklerden ve yavruları analarından ayırma uygulaması olarak verir."}],"source_summary":"Bu dal, sürü hayvanlarında küçükleri büyüklerden ayırma ve yavru develeri analarından kesip alışmalarını sağlama biçimindeki özel uygulamayı özetler."},"support_links":[]},{"boundary":"Dal bitki ve meyve olgunlaşma evresine bağlıdır; insana ait uzaklaşma anlamı buraya taşınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001684/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","surface_ar":"تَوَلَّىٰ"}],"gloss":"taze hurmanın kurumaya dönmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taze hurmanın solup açık renge dönerek kurumaya başlaması."}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Taze hurmanın solgunlaşıp kurumaya yöneldiği olgunluk sonrası evre için uygundur.","boundary_detail":"Dal bitki ve meyve olgunlaşma evresine bağlıdır; insana ait uzaklaşma anlamı buraya taşınmaz.","concept_gloss":"taze hurmanın kurumaya dönmesi","contextual_glosses":[{"applicability":"Taze hurmanın açık renkli kuruma evresine girmesi bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Solma ve kurumaya başlama değerini korur."},"facet_ids":["F001"],"text":"solup kurumaya başlamak","usage_role":"contextual"},{"applicability":"Evrenin rengini veya solgunluğunu açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Renk değişimi ve solgunluk değerini korur."},"facet_ids":["F001"],"text":"solgun kuruma rengi","usage_role":"explanatory"}],"definition":"Taze hurmanın olgunluk sonrası solup açık renge dönerek kurumaya yönelen evreye girmesidir. Bu evrenin belirgin rengi veya solgunluğu da adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taze hurmanın solup açık renge dönerek kurumaya başlaması."}],"identity_rationale":"Kaynak ifadesi, taze hurmanın solma, sararma veya kurumaya dönme evresine girmesini ve bu evrenin açık rengini verir. Dal, yüz çevirme değil, meyvenin olgunluk sonrası değişim aşamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"taze hurmanın solup kurumaya başlaması"},{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"taze hurmadaki solgun kuruma rengi"}],"lexicalization_note":"Meyvenin evreye girmesi ve bu evrenin adı birlikte korunur; soyut yüz çevirme anlamına yayılmaz.","neighbor_coverage_note":"Hurma, meyve olgunlaşması, sararma ve kuruma adayları değerlendirildi; uzaklaşma anlamlı dallar ayrı tutuldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B016 taze hurmanın özel geçiş evresini anlatır; komşu dal bitki ve sapların daha genel sararıp kuruma durumunu verir.","focus_only":"Taze hurmanın belirli solgun kuruma evresine bağlıdır.","gloss":"sararıp kurumaya dönme","neighbor_only":"Bitkinin veya sapın sararıp kuruması daha genel bir bitki evresidir.","neighbor_ref":"root_001033/B015","relation_type":"near_synonym","shared_zone":"İki dal da bitkisel ürünün sararma veya kuruma evresine girmesi alanında örtüşür."},{"boundary_match":"partial","distinction":"B016 geçiş evresidir; komşu dal kurumuş olma durumunu daha doğrudan anlatır.","focus_only":"Kurumaya başlama ve solgun renk evresi vurgulanır.","gloss":"kurumaya başlama ile kurumuşluk","neighbor_only":"Hurmanın kurumuş olması veya kuruluk durumu öne çıkar.","neighbor_ref":"root_000242/B005","relation_type":"near_neighbor","shared_zone":"İki dal da hurma veya meyve kuruması alanına yaklaşır."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanık, kullanımı taze hurmanın kurumaya dönerken aldığı solgun ve açık renkli evre olarak verir."}],"source_summary":"Bu dal, taze hurmanın solma ve açık renge dönme yoluyla kurumaya başladığı evreyi ve bu evrenin rengini özetler."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["92:16:1"],"branch_refs":[],"candidate_id":"cand_92ec4519660b99a31007","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:16:1:antecedent-lock","source_type":"word_analysis","support_ids":["sup_3a17a52b40e5efdd2f7e","sup_3a6f6449a9fd3b972997"],"title":"relative pronoun locks onto the prior singular figure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:1","qac_refs":["92:16:1:1"],"status":"accepted"}},{"anchor_refs":["92:16:1"],"branch_refs":[],"candidate_id":"cand_043e4d45354f1ee7863d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:16:1:boundary-cause","source_type":"word_analysis","support_ids":["sup_3a6f6449a9fd3b972997","sup_f1a5f3dfb585463636c7"],"title":"boundary reverses from consequence to cause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:1","qac_refs":["92:16:1:1"],"status":"accepted"}},{"anchor_refs":["92:16:1"],"branch_refs":[],"candidate_id":"cand_7c7aed72123a084fd278","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:16:1:relative-definition","source_type":"word_analysis","support_ids":["sup_3a6f6449a9fd3b972997","sup_3b2490a0d8882320f742"],"title":"full relative clause defines the label by deeds","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:1","qac_refs":["92:16:1:1"],"status":"accepted"}},{"anchor_refs":["92:16:1"],"branch_refs":[],"candidate_id":"cand_5dd5f01078409b7994a0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:16:1:restricted-class-bridge","source_type":"word_analysis","support_ids":["sup_3a6f6449a9fd3b972997","sup_fa7a2036e8d2ba59a086"],"title":"restricted fire-bound class is unpacked","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:1","qac_refs":["92:16:1:1"],"status":"accepted"}},{"anchor_refs":["92:16:2"],"branch_refs":[],"candidate_id":"cand_4deacf69381f3fe5ec97","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"92:16:2:boundary-moral-contrast","source_type":"word_analysis","support_ids":["sup_0b08da1734280ec8ce31","sup_8881c0261d13d22b83d9"],"title":"denial grounds the prior verdict and faces the next contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:2","qac_refs":["92:16:2:1"],"status":"accepted"}},{"anchor_refs":["92:16:2"],"branch_refs":[],"candidate_id":"cand_2e8bac852cfc228d26df","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"92:16:2:completed-active-agent","source_type":"word_analysis","support_ids":["sup_3fadeba00376b0658439","sup_8881c0261d13d22b83d9"],"title":"completed active deed defines the figure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:2","qac_refs":["92:16:2:1"],"status":"accepted"}},{"anchor_refs":["92:16:2"],"branch_refs":[],"candidate_id":"cand_a8a26e1285a78aeed2ed","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"92:16:2:denial-withdrawal-formula","source_type":"word_analysis","support_ids":["sup_8881c0261d13d22b83d9","sup_fb6b3294761dfb5bed91"],"title":"denial pairs with withdrawal as a formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:2","qac_refs":["92:16:2:1"],"status":"accepted"}},{"anchor_refs":["92:16:2"],"branch_refs":[],"candidate_id":"cand_8f442daccc7aa504096a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"92:16:2:form-ii-declaring-false","source_type":"word_analysis","support_ids":["sup_8881c0261d13d22b83d9","sup_955ec971cfc396d78dc1"],"title":"Form II makes denial an emphatic verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:2","qac_refs":["92:16:2:1"],"status":"accepted"}},{"anchor_refs":["92:16:2"],"branch_refs":[],"candidate_id":"cand_7d51431964de2432f830","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"92:16:2:object-open-denial","source_type":"word_analysis","support_ids":["sup_6d01406fa647d22e9a36","sup_8881c0261d13d22b83d9"],"title":"object omission keeps denial broad","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:2","qac_refs":["92:16:2:1"],"status":"accepted"}},{"anchor_refs":["92:16:2"],"branch_refs":[],"candidate_id":"cand_9535950a31da431e9ac6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"92:16:2:same-surah-denial-echo","source_type":"word_analysis","support_ids":["sup_8881c0261d13d22b83d9","sup_a590a4ee86ab6fae6ffb"],"title":"bare denial recalls the earlier expressed object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:2","qac_refs":["92:16:2:1"],"status":"accepted"}},{"anchor_refs":["92:16:2"],"branch_refs":[],"candidate_id":"cand_c760dbf8c797994357e7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"92:16:2:sound-and-compression","source_type":"word_analysis","support_ids":["sup_267cccd847c2d2355785","sup_8881c0261d13d22b83d9"],"title":"doubled consonant concentrates the denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:2","qac_refs":["92:16:2:1"],"status":"accepted"}},{"anchor_refs":["92:16:3"],"branch_refs":[],"candidate_id":"cand_229f7fc6ca2a01b27b94","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:16:3:cadential-hinge","source_type":"word_analysis","support_ids":["sup_733bf3c0722256b5f638","sup_cae6b6e7de4c3a008d81"],"title":"short connector resets the cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:3","qac_refs":["92:16:3:1"],"status":"accepted"}},{"anchor_refs":["92:16:3"],"branch_refs":[],"candidate_id":"cand_a02a8d9bef235311d584","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:16:3:denier-turner-profile","source_type":"word_analysis","support_ids":["sup_93635da634a48629a6c2","sup_cae6b6e7de4c3a008d81"],"title":"hinge forms a two-step moral profile","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:3","qac_refs":["92:16:3:1"],"status":"accepted"}},{"anchor_refs":["92:16:3"],"branch_refs":[],"candidate_id":"cand_146fbb33bd5dd0893280","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:16:3:equal-coordination","source_type":"word_analysis","support_ids":["sup_5a4bdcef444c68d04a4a","sup_cae6b6e7de4c3a008d81"],"title":"two perfect verbs share one subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:3","qac_refs":["92:16:3:1"],"status":"accepted"}},{"anchor_refs":["92:16:3"],"branch_refs":[],"candidate_id":"cand_cab02121223b82128d3d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:16:3:local-coordination-not-oath","source_type":"word_analysis","support_ids":["sup_58b869d67f5585ff4665","sup_cae6b6e7de4c3a008d81"],"title":"verb-to-verb position excludes oath force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:3","qac_refs":["92:16:3:1"],"status":"accepted"}},{"anchor_refs":["92:16:3"],"branch_refs":[],"candidate_id":"cand_65d9f09e9b09c4185f03","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:16:3:visible-segmentation","source_type":"word_analysis","support_ids":["sup_cae6b6e7de4c3a008d81","sup_d9e66437e6cd826bb007"],"title":"separate word slot makes the join visible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:3","qac_refs":["92:16:3:1"],"status":"accepted"}},{"anchor_refs":["92:16:4"],"branch_refs":[],"candidate_id":"cand_1ddd63d4dbcc83f7b52d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001684"],"scope":"focus_ayah","source_local_id":"92:16:4:authority-tension","source_type":"word_analysis","support_ids":["sup_5bf8000d04c3a2d55f04","sup_ecc26025dc1f5380a10f"],"title":"taking-charge sense sharpens arrogant withdrawal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:4","qac_refs":["92:16:3:2"],"status":"accepted"}},{"anchor_refs":["92:16:4"],"branch_refs":[],"candidate_id":"cand_3e0341254b21ad26c558","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001684"],"scope":"focus_ayah","source_local_id":"92:16:4:final-position-closure","source_type":"word_analysis","support_ids":["sup_5bf8000d04c3a2d55f04","sup_c5d1ec3d4eac215e2cc7"],"title":"ayah closes on withdrawal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:4","qac_refs":["92:16:3:2"],"status":"accepted"}},{"anchor_refs":["92:16:4"],"branch_refs":[],"candidate_id":"cand_83f250f2d474950d2275","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001684"],"scope":"focus_ayah","source_local_id":"92:16:4:formulaic-completion","source_type":"word_analysis","support_ids":["sup_34d715fb14e8791b6705","sup_5bf8000d04c3a2d55f04"],"title":"final verb completes the denial-withdrawal formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:4","qac_refs":["92:16:3:2"],"status":"accepted"}},{"anchor_refs":["92:16:4"],"branch_refs":[],"candidate_id":"cand_cd381dcc39264700d500","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001684"],"scope":"focus_ayah","source_local_id":"92:16:4:forward-distance-contrast","source_type":"word_analysis","support_ids":["sup_5bf8000d04c3a2d55f04","sup_8fd2d7cd8ecdb8749646"],"title":"self-withdrawal contrasts with being kept away","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:4","qac_refs":["92:16:3:2"],"status":"accepted"}},{"anchor_refs":["92:16:4"],"branch_refs":[],"candidate_id":"cand_b766c49d8b8a0e403213","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001684"],"scope":"focus_ayah","source_local_id":"92:16:4:omitted-complement","source_type":"word_analysis","support_ids":["sup_5bf8000d04c3a2d55f04","sup_bd3d16bd83e94f0eb873"],"title":"no object makes withdrawal a posture","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:4","qac_refs":["92:16:3:2"],"status":"accepted"}},{"anchor_refs":["92:16:4"],"branch_refs":[],"candidate_id":"cand_2bbb17a08e9ecf844ed5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001684"],"scope":"focus_ayah","source_local_id":"92:16:4:prosodic-release","source_type":"word_analysis","support_ids":["sup_5bf8000d04c3a2d55f04","sup_d4df26b54dd173cb6558"],"title":"long final sound lets withdrawal linger","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:4","qac_refs":["92:16:3:2"],"status":"accepted"}},{"anchor_refs":["92:16:4"],"branch_refs":[],"candidate_id":"cand_fc1e9ae49205d43ee914","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001684"],"scope":"focus_ayah","source_local_id":"92:16:4:root-field-narrowed-to-withdrawal","source_type":"word_analysis","support_ids":["sup_5bf8000d04c3a2d55f04","sup_f50083ef5261bf3e3992"],"title":"proximity and authority field is bent into departure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:4","qac_refs":["92:16:3:2"],"status":"accepted"}},{"anchor_refs":["92:16:4"],"branch_refs":[],"candidate_id":"cand_a27970ad1d271f4771ec","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001684"],"scope":"focus_ayah","source_local_id":"92:16:4:same-surah-relational-contrast","source_type":"word_analysis","support_ids":["sup_5568f7f9b56ebba6db26","sup_5bf8000d04c3a2d55f04"],"title":"same-surah contrasts sharpen the withdrawal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:4","qac_refs":["92:16:3:2"],"status":"accepted"}},{"anchor_refs":["92:16:4"],"branch_refs":[],"candidate_id":"cand_228e5a0394340f75b956","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001684"],"scope":"focus_ayah","source_local_id":"92:16:4:self-directed-form-v","source_type":"word_analysis","support_ids":["sup_5bf8000d04c3a2d55f04","sup_f75ece11b821c575281e"],"title":"Form V marks self-involving withdrawal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:4","qac_refs":["92:16:3:2"],"status":"accepted"}},{"anchor_refs":["92:16:4"],"branch_refs":[],"candidate_id":"cand_ec56e1b00454b96785c3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001684"],"scope":"focus_ayah","source_local_id":"92:16:4:shared-active-perfect","source_type":"word_analysis","support_ids":["sup_5bf8000d04c3a2d55f04","sup_688c3aaff28c89c67a25"],"title":"same figure completes the second perfect act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:16:4","qac_refs":["92:16:3:2"],"status":"accepted"}},{"anchor_refs":["92:16:2"],"branch_refs":[],"candidate_id":"cand_655a81921981d97e553b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"92:16:2:1","source_type":"qac_morpheme","support_ids":["sup_e9f9cc3cdfcc8f3792f8"],"title":"QAC root occurrence: ك ذ ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:16:3"],"branch_refs":[],"candidate_id":"cand_41c2105a36ef292190db","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001684"],"scope":"focus_ayah","source_local_id":"92:16:3:2","source_type":"qac_morpheme","support_ids":["sup_79b681967ac6af3865be"],"title":"QAC root occurrence: و ل ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:16","branch_refs":["root_001290/B002","root_001684/B007"],"candidate_id":"cand_ecbc550fc1c947233fc7","commentary_obligation":"review","hft_ref":"hft_cffd94c982cfaa8da8b0","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:B92_16_VERDICT_WITHDRAWAL","source_type":"hft","support_ids":["sup_453f8fd81af0401ce204"],"title":"B92_16_VERDICT_WITHDRAWAL","trust":"legacy_unbound"},{"anchor_refs":["92:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:16","branch_refs":["root_001290/B004","root_001684/B003","root_001684/B007"],"candidate_id":"cand_8968e623c23f2317dc57","commentary_obligation":"review","hft_ref":"hft_d055988993fcbd259c94","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:B92_16_FAILED_CHARGE","source_type":"hft","support_ids":["sup_a92207de518e12feb0c1"],"title":"B92_16_FAILED_CHARGE","trust":"legacy_unbound"},{"anchor_refs":["92:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:16","branch_refs":["root_001290/B009","root_001684/B006","root_001684/B007"],"candidate_id":"cand_4c49c7f5485dfdf858d9","commentary_obligation":"review","hft_ref":"hft_3c01cd944674a9291503","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:B92_16_COUNTER_ORIENTATION","source_type":"hft","support_ids":["sup_bd3ee6a142530b3ed89d"],"title":"B92_16_COUNTER_ORIENTATION","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"92:16:1:1","qac_word_ref":"92:16:1","root_ar":"","surface_ar":"ٱلَّذِى"},{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:2:1","qac_word_ref":"92:16:2","root_ar":"ك ذ ب","surface_ar":"كَذَّبَ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:16:3:1","qac_word_ref":"92:16:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","root_ar":"و ل ي","surface_ar":"تَوَلَّىٰ"}],"word_analysis_qac_refs":[["92:16:1:1"],["92:16:2:1"],["92:16:3:1"],["92:16:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["92:16:1","92:16:2","92:16:3","92:16:4"]},"focus_surface_evidence":{"arabic_uthmani":"ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"92:16:1:1","qac_word_ref":"92:16:1","root_ar":"","surface_ar":"ٱلَّذِى"},{"lemma_ar":"كَذَّبَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:2:1","qac_word_ref":"92:16:2","root_ar":"ك ذ ب","surface_ar":"كَذَّبَ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:16:3:1","qac_word_ref":"92:16:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"تَوَلَّىٰ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:16:3:2","qac_word_ref":"92:16:3","root_ar":"و ل ي","surface_ar":"تَوَلَّىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["92:16:1:1"],["92:16:2:1"],["92:16:3:1"],["92:16:3:2"]],"word_analysis_refs":["92:16:1","92:16:2","92:16:3","92:16:4"],"word_rows":[{"analysis_record_ref":"92:16:1","analytic_gloss_range_en":"masculine singular definite relative pronoun that resumes the prior fire-bound figure and opens the defining clause","analytic_root_gloss_range_en":null,"qac_refs":["92:16:1:1"],"root":{},"surface":{"arabic":"ٱلَّذِى","transliteration":"alladhī"}},{"analysis_record_ref":"92:16:2","analytic_gloss_range_en":"Form II perfect active declaring false, locally absolute with no expressed object","analytic_root_gloss_range_en":"falsehood, lying, attributing falsehood, denial, disproving, and related failure-to-hold branches; the local Form II verb selects emphatic declaring-false while the omitted object keeps the denied field open","qac_refs":["92:16:2:1"],"root":{"arabic":"ك ذ ب","transliteration":"k-dh-b"},"surface":{"arabic":"كَذَّبَ","transliteration":"kadhdhaba"}},{"analysis_record_ref":"92:16:3","analytic_gloss_range_en":"coordinating conjunction between two perfect verbs, locally binding equal predicates rather than opening an oath","analytic_root_gloss_range_en":null,"qac_refs":["92:16:3:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"92:16:4","analytic_gloss_range_en":"Form V perfect active turning away, locally intransitive and self-involving, with no expressed complement","analytic_root_gloss_range_en":"nearness, succession, authority, alliance, support, facing, turning away, entitlement, and other branches; the local Form V verb selects withdrawal while the proximity and authority field sharpens what is being severed","qac_refs":["92:16:3:2"],"root":{"arabic":"و ل ي","transliteration":"w-l-y"},"surface":{"arabic":"تَوَلَّىٰ","transliteration":"tawallā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["92:16"],"branch_refs":["root_001290/B002","root_001684/B007"],"candidate_id":"cand_ecbc550fc1c947233fc7","evidence_scope":"focus_ayah","hft_ref":"hft_cffd94c982cfaa8da8b0","item_id":"B92_16_VERDICT_WITHDRAWAL","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:B92_16_VERDICT_WITHDRAWAL","support_id":"sup_453f8fd81af0401ce204"},{"anchor_refs":["92:16"],"branch_refs":["root_001290/B004","root_001684/B003","root_001684/B007"],"candidate_id":"cand_8968e623c23f2317dc57","evidence_scope":"focus_ayah","hft_ref":"hft_d055988993fcbd259c94","item_id":"B92_16_FAILED_CHARGE","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:B92_16_FAILED_CHARGE","support_id":"sup_a92207de518e12feb0c1"},{"anchor_refs":["92:16"],"branch_refs":["root_001290/B009","root_001684/B006","root_001684/B007"],"candidate_id":"cand_4c49c7f5485dfdf858d9","evidence_scope":"focus_ayah","hft_ref":"hft_3c01cd944674a9291503","item_id":"B92_16_COUNTER_ORIENTATION","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:B92_16_COUNTER_ORIENTATION","support_id":"sup_bd3ee6a142530b3ed89d"}],"diagnostics":[],"lane_counts":{"global":16,"macro":7,"micro":3},"packet_summary":{"ayah_count":21,"focus_ref":"92:16","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ج ز ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000244","furuq_root_norm":"ج ز ي","furuq_source_root_norm":"ج ز ي","is_dominant":true,"target_occurrences":97,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000242","furuq_root_norm":"ج ز ز","furuq_source_root_norm":"ج ز ز","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11","92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"92:16","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":17,"unstructured_record_count":0},"identity":{"ayah_ref":"92:16","lane":"micro","linguistic_source_ref":"92:16","surface_ref":"92:16","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"92:16","target_tokens":[["O",["92:16:1"]],["yalanlayan",["92:16:2"]],["ve",["92:16:3"]],["yüz",["92:16:3"]],["çevirendir",["92:16:1","92:16:3"]]],"text":"O, yalanlayan ve yüz çevirendir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":12,"ayah_to":21,"id":"s092-p02-012-021","label":"Guidance, fire, and generous salvation","number":2,"refs":["92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:2:boundary-moral-contrast","source_type":"word_analysis","support_id":"sup_0b08da1734280ec8ce31","text":"{\"blocking_evidence\":null,\"headline\":\"denial grounds the prior verdict and faces the next contrast\",\"reader_payoff\":\"The reader sees the fire-bound label explained by falsification before the next ayah contrasts it with guarded awareness.\",\"reason\":\"The verb is the first action in the relative definition of the prior label and sits immediately before the contrasting figure in 92:17.\",\"representative_source_ids\":[\"QB-1e2222cf\",\"QB-4031d61b\",\"QB-4f97cbed\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:2:sound-and-compression","source_type":"word_analysis","support_id":"sup_267cccd847c2d2355785","text":"{\"blocking_evidence\":null,\"headline\":\"doubled consonant concentrates the denial\",\"reader_payoff\":\"The reader hears the compact verb carry forceful falsification in one sharp, doubled form.\",\"reason\":\"The written and recited doubling belongs to the local Form II surface, so the sound observation is anchored in the actual word.\",\"representative_source_ids\":[\"QF-44683489\",\"QP-90e46218\",\"QH-46bbc57e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:4:formulaic-completion","source_type":"word_analysis","support_id":"sup_34d715fb14e8791b6705","text":"{\"blocking_evidence\":null,\"headline\":\"final verb completes the denial-withdrawal formula\",\"reader_payoff\":\"The reader sees the last word as the behavioral half of a recognized rejecter portrait, including the exact formula at 75:32.\",\"reason\":\"The local verb is coordinated with the denial verb, and the supplied row explicitly gives the exact recurrence at 75:32.\",\"representative_source_ids\":[\"QI-48f942d3\",\"QI-e8326b6d\",\"MI-5037f358\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:1:antecedent-lock","source_type":"word_analysis","support_id":"sup_3a17a52b40e5efdd2f7e","text":"{\"blocking_evidence\":null,\"headline\":\"relative pronoun locks onto the prior singular figure\",\"reader_payoff\":\"The reader sees that the ayah identifies the already named fire-bound figure from 92:15 rather than introducing a new indefinite actor.\",\"reason\":\"QAC marks the word as a masculine singular definite relative pronoun, and attachment evidence explicitly links it to the preceding masculine singular antecedent in 92:15.\",\"representative_source_ids\":[\"QG-0a9d8b6e\",\"QG-49c08179\",\"QG-4a99c9e3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:1","source_type":"word_analysis","support_id":"sup_3a6f6449a9fd3b972997","text":"{\"gloss_range\":\"masculine singular definite relative pronoun that resumes the prior fire-bound figure and opens the defining clause\",\"prose\":\"{{ar:ٱلَّذِى}} ({{tr:alladhī}}) makes 92:16 dependent on the prior label, not a fresh standalone subject. Its masculine singular definiteness points back to the fire-bound category named in 92:15, so that category is now specified by the deeds that follow. As a full relative pronoun, it gives room for the whole verb pair {{ar:كَذَّبَ وَتَوَلَّىٰ}} ({{tr:kadhdhaba wa-tawallā}}) to define that figure rather than merely resume him with a short suffix. The ayah boundary therefore moves backward from consequence to cause: the named wretched one is unpacked as the one who declared false and turned away. That concrete negative definition also arrives before the opposite figure appears in 92:17, keeping the contrast from remaining abstract.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ٱلَّذِى}} ({{tr:alladhī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:1:relative-definition","source_type":"word_analysis","support_id":"sup_3b2490a0d8882320f742","text":"{\"blocking_evidence\":null,\"headline\":\"full relative clause defines the label by deeds\",\"reader_payoff\":\"The reader notices that the prior label becomes an action-defined identity through the following two verbs.\",\"reason\":\"The local clause spans the relative pronoun through the two coordinated verbs, so either attributive or appositional analysis still makes the clause define the prior figure.\",\"representative_source_ids\":[\"QG-863900fc\",\"QS-835ffe02\",\"QF-562ee867\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:2:completed-active-agent","source_type":"word_analysis","support_id":"sup_3fadeba00376b0658439","text":"{\"blocking_evidence\":null,\"headline\":\"completed active deed defines the figure\",\"reader_payoff\":\"The reader sees denial as the performed deed of the same prior figure, not as a vague state or a new actor.\",\"reason\":\"QAC and attachment evidence identify the verb as perfect active 3ms with {{ar:ٱلَّذِى}} ({{tr:alladhī}}) as its subject.\",\"representative_source_ids\":[\"QG-923fc580\",\"QG-c1c2cc70\",\"QG-f87a81e1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:4:same-surah-relational-contrast","source_type":"word_analysis","support_id":"sup_5568f7f9b56ebba6db26","text":"{\"blocking_evidence\":null,\"headline\":\"same-surah contrasts sharpen the withdrawal\",\"reader_payoff\":\"The reader places this turning away against nearby surah contrasts: divine ownership in 92:13, self-sufficiency in 92:8, and guarding in 92:5.\",\"reason\":\"The CRITICAL rows provide the concrete same-surah references, and the local root-form remains the negative withdrawal endpoint.\",\"representative_source_ids\":[\"QI-a6dcf4e5\",\"MI-f7b22489\",\"ME-ae0df12a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:3:local-coordination-not-oath","source_type":"word_analysis","support_id":"sup_58b869d67f5585ff4665","text":"{\"blocking_evidence\":null,\"headline\":\"verb-to-verb position excludes oath force\",\"reader_payoff\":\"The reader keeps the particle's local force as deed-binding coordination while still hearing sequence within the pair.\",\"reason\":\"Although the particle has wider Arabic uses, the local position between two perfect verbs and the attachment analysis narrow it to coordination.\",\"representative_source_ids\":[\"QS-16f15ae1\",\"QS-972e58ed\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:3:equal-coordination","source_type":"word_analysis","support_id":"sup_5a4bdcef444c68d04a4a","text":"{\"blocking_evidence\":null,\"headline\":\"two perfect verbs share one subject\",\"reader_payoff\":\"The reader sees denial and turning as co-equal defining acts of one figure, not as separate biographies or a main act with a subordinate aside.\",\"reason\":\"QAC tags the word as a conjunction, and attachment evidence coordinates the two perfect verbs while assigning both to the same relative subject.\",\"representative_source_ids\":[\"QG-fb386952\",\"MG-2494406b\",\"QT-c6fcf729\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:4","source_type":"word_analysis","support_id":"sup_5bf8000d04c3a2d55f04","text":"{\"gloss_range\":\"Form V perfect active turning away, locally intransitive and self-involving, with no expressed complement\",\"prose\":\"{{ar:تَوَلَّىٰ}} ({{tr:tawallā}}) completes the profile by making denial become departure. The verb is perfect active 3ms like {{ar:كَذَّبَ}} ({{tr:kadhdhaba}}), and the shared subject remains the one defined by {{ar:ٱلَّذِى}} ({{tr:alladhī}}), so the same figure performs both acts. Its Form V shape gives the withdrawal self-involving force: he turns himself away, not merely is moved aside. The broad {{ar:و ل ي}} ({{tr:w-l-y}}) field includes nearness, authority, alliance, and support, but local context selects turning away; that makes the word more than motion, because it sounds like a severing of proximity and allegiance. The secondary authority sense adds arrogance without taking over the translation: he withdraws as though his own stance were sufficient. With no expressed complement, the posture remains open across guidance, responsibility, and relation. As the final word, it leaves the ayah on self-made distance, and the doubled middle with the final long vowel lets that withdrawal linger at the boundary. The word also completes the exact denial-withdrawal formula attested at 75:32, while nearby surah contrasts sharpen the act against divine ownership in 92:13, self-sufficiency in 92:8, and guarding in 92:5. The next ayah, 92:17, reverses the distance when the guarded one is passively kept away from the fire.\",\"root_display\":\"{{ar:و ل ي}} ({{tr:w-l-y}})\",\"root_gloss_range\":\"nearness, succession, authority, alliance, support, facing, turning away, entitlement, and other branches; the local Form V verb selects withdrawal while the proximity and authority field sharpens what is being severed\",\"surface_display\":\"{{ar:تَوَلَّىٰ}} ({{tr:tawallā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:4:shared-active-perfect","source_type":"word_analysis","support_id":"sup_688c3aaff28c89c67a25","text":"{\"blocking_evidence\":null,\"headline\":\"same figure completes the second perfect act\",\"reader_payoff\":\"The reader sees withdrawal as the same person's completed act, matched to the denial verb in person, voice, and aspect.\",\"reason\":\"QAC identifies the verb as perfect active 3ms, and attachment evidence gives it the same relative subject as the first verb.\",\"representative_source_ids\":[\"QG-308a07b3\",\"QG-c10dcb28\",\"QG-ef289858\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:2:object-open-denial","source_type":"word_analysis","support_id":"sup_6d01406fa647d22e9a36","text":"{\"blocking_evidence\":null,\"headline\":\"object omission keeps denial broad\",\"reader_payoff\":\"The reader feels the denial as a whole stance because the ayah does not narrow it to one explicit object.\",\"reason\":\"The local frame is obj=none_absolute; contextual profiles show absolute use is common for this exact root-form, so the omission is licensed and meaningful.\",\"representative_source_ids\":[\"QG-de3ac2c8\",\"MG-5c873052\",\"QT-59d9a050\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:3:cadential-hinge","source_type":"word_analysis","support_id":"sup_733bf3c0722256b5f638","text":"{\"blocking_evidence\":null,\"headline\":\"short connector resets the cadence\",\"reader_payoff\":\"The reader hears a brief beat separating two heavy verbs while keeping them in one compact clause.\",\"reason\":\"The one-letter conjunction is locally positioned between the two larger perfect verbs, so the rhythmic observation is anchored in the surface.\",\"representative_source_ids\":[\"QP-6692a6da\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:16:3:2","source_type":"qac_morpheme","support_id":"sup_79b681967ac6af3865be","text":"{\"lemma_ar\":\"تَوَلَّىٰ\",\"morph_features\":\"STEM|POS:V|PERF|(V)|LEM:tawal~aY`|ROOT:wly|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"92:16:3:2\",\"qac_word_ref\":\"92:16:3\",\"root_ar\":\"و ل ي\",\"surface_ar\":\"تَوَلَّىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:2","source_type":"word_analysis","support_id":"sup_8881c0261d13d22b83d9","text":"{\"gloss_range\":\"Form II perfect active declaring false, locally absolute with no expressed object\",\"prose\":\"{{ar:كَذَّبَ}} ({{tr:kadhdhaba}}) is the first finite predicate in the definition of the prior fire-bound figure. Its perfect active Form II makes the figure a completed agent of emphatic declaring-false, not merely someone associated with a lie. The verb can take an object, but none is expressed here; that compression lets the denial remain broad while still recalling the earlier expressed object in 92:9. The doubled middle consonant gives the act audible pressure, and the following {{ar:وَتَوَلَّىٰ}} ({{tr:wa-tawallā}}) turns the verdict into a recognizable denial-then-withdrawal profile, also heard in the exact formula at 75:32. As the cause behind the prior verdict, this falsification also faces the guarded awareness of the contrasting figure in 92:17.\",\"root_display\":\"{{ar:ك ذ ب}} ({{tr:k-dh-b}})\",\"root_gloss_range\":\"falsehood, lying, attributing falsehood, denial, disproving, and related failure-to-hold branches; the local Form II verb selects emphatic declaring-false while the omitted object keeps the denied field open\",\"surface_display\":\"{{ar:كَذَّبَ}} ({{tr:kadhdhaba}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:4:forward-distance-contrast","source_type":"word_analysis","support_id":"sup_8fd2d7cd8ecdb8749646","text":"{\"blocking_evidence\":null,\"headline\":\"self-withdrawal contrasts with being kept away\",\"reader_payoff\":\"The reader sees distance split morally: the wretched one creates distance from guidance, while the guarded one in 92:17 receives distance from harm.\",\"reason\":\"The local verb is active self-withdrawal, and the supplied boundary rows contrast it with the following passive distancing in 92:17.\",\"representative_source_ids\":[\"QB-d9caad2a\",\"QB-b5932614\",\"QY-b07a5743\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:3:denier-turner-profile","source_type":"word_analysis","support_id":"sup_93635da634a48629a6c2","text":"{\"blocking_evidence\":null,\"headline\":\"hinge forms a two-step moral profile\",\"reader_payoff\":\"The reader notices a movement from verdict to withdrawal, not a flat list of unrelated sins.\",\"reason\":\"The conjunction sits between the denial and withdrawal verbs, and contextual pair data supports the local co-occurrence profile without creating a new topic by itself.\",\"representative_source_ids\":[\"QI-7026920a\",\"QT-8a3d0bd3\",\"QY-c2b01646\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:2:form-ii-declaring-false","source_type":"word_analysis","support_id":"sup_955ec971cfc396d78dc1","text":"{\"blocking_evidence\":null,\"headline\":\"Form II makes denial an emphatic verdict\",\"reader_payoff\":\"The reader notices that the verb frames the subject as one who rules truth false, not simply as one who tells a lie.\",\"reason\":\"V4 preserves both falsehood and attributing-falsehood branches, while the local Form II perfect and syntax select declaring false as the primary local sense.\",\"representative_source_ids\":[\"QS-66e03049\",\"QF-db1d8304\",\"MF-8635e32e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:2:same-surah-denial-echo","source_type":"word_analysis","support_id":"sup_a590a4ee86ab6fae6ffb","text":"{\"blocking_evidence\":null,\"headline\":\"bare denial recalls the earlier expressed object\",\"reader_payoff\":\"The reader connects the bare denial here with the earlier expressed denial object in 92:9 without forcing that object to be restated.\",\"reason\":\"The CRITICAL rows provide the same-surah echo, and the local object omission allows the earlier object to resonate without becoming an inserted object.\",\"representative_source_ids\":[\"QI-9fdeb9e2\",\"QE-af15659e\",\"QY-9758eb40\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:4:omitted-complement","source_type":"word_analysis","support_id":"sup_bd3d16bd83e94f0eb873","text":"{\"blocking_evidence\":null,\"headline\":\"no object makes withdrawal a posture\",\"reader_payoff\":\"The reader senses withdrawal itself as the defining posture because the ayah does not specify only one thing from which he turns.\",\"reason\":\"The local frame is none_intransitive with no preposition or complement, and contextual profiles support intransitive use for this exact root-form.\",\"representative_source_ids\":[\"QG-56952a28\",\"QT-b29821af\",\"QY-6f8aaa73\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:4:final-position-closure","source_type":"word_analysis","support_id":"sup_c5d1ec3d4eac215e2cc7","text":"{\"blocking_evidence\":null,\"headline\":\"ayah closes on withdrawal\",\"reader_payoff\":\"The reader leaves the ayah with visible departure as the last impression, not with denial as an isolated inner verdict.\",\"reason\":\"The word is the final predicate of the relative clause, so the ayah's closure lands on turning away.\",\"representative_source_ids\":[\"QT-1babc4eb\",\"QT-2daed8a0\",\"QT-c4a5f6e8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:3","source_type":"word_analysis","support_id":"sup_cae6b6e7de4c3a008d81","text":"{\"gloss_range\":\"coordinating conjunction between two perfect verbs, locally binding equal predicates rather than opening an oath\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) is small, but it is the hinge that makes the definition double. It coordinates {{ar:كَذَّبَ}} ({{tr:kadhdhaba}}) and {{ar:تَوَلَّىٰ}} ({{tr:tawallā}}) as equal predicates under the same relative subject, so the figure is not merely a denier and not a second actor appears. The particle's broader possibilities are locally narrowed by its verb-to-verb position: here it binds deeds, not an oath. It also preserves the order of the profile, letting declared falsification issue into visible withdrawal while keeping both acts independently constitutive. Because the conjunction is segmented as its own word, it makes the exact denial-withdrawal formula visible instead of letting the two verbs collapse into an unmarked cluster.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:4:prosodic-release","source_type":"word_analysis","support_id":"sup_d4df26b54dd173cb6558","text":"{\"blocking_evidence\":null,\"headline\":\"long final sound lets withdrawal linger\",\"reader_payoff\":\"The reader hears the doubled middle and final long vowel make the withdrawal feel held and spatially extended at the boundary.\",\"reason\":\"The local surface has the doubled middle consonant and final long vowel, and it occupies the ayah-final position.\",\"representative_source_ids\":[\"QF-41ef6662\",\"QP-c894c885\",\"QP-e6d5c37a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:3:visible-segmentation","source_type":"word_analysis","support_id":"sup_d9e66437e6cd826bb007","text":"{\"blocking_evidence\":null,\"headline\":\"separate word slot makes the join visible\",\"reader_payoff\":\"The reader sees the conjunction as the mechanism preserving the exact {{ar:كَذَّبَ وَتَوَلَّىٰ}} ({{tr:kadhdhaba wa-tawallā}}) formula.\",\"reason\":\"The input treats the conjunction as its own analytical word between the two verbs, making the formulaic join explicit.\",\"representative_source_ids\":[\"QF-5ce808d1\",\"QE-83a06cbc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:16:2:1","source_type":"qac_morpheme","support_id":"sup_e9f9cc3cdfcc8f3792f8","text":"{\"lemma_ar\":\"كَذَّبَ\",\"morph_features\":\"STEM|POS:V|PERF|(II)|LEM:ka*~aba|ROOT:k*b|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"92:16:2:1\",\"qac_word_ref\":\"92:16:2\",\"root_ar\":\"ك ذ ب\",\"surface_ar\":\"كَذَّبَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:4:authority-tension","source_type":"word_analysis","support_id":"sup_ecc26025dc1f5380a10f","text":"{\"blocking_evidence\":null,\"headline\":\"taking-charge sense sharpens arrogant withdrawal\",\"reader_payoff\":\"The reader can hear a secondary arrogance in the withdrawal: the denier turns away as though taking his own stance as sufficient.\",\"reason\":\"The local primary sense remains turning away, but the accepted authority branch can qualify the posture as arrogant self-assumption without becoming the main translation.\",\"representative_source_ids\":[\"QS-7eb3c437\",\"MS-97c23dba\",\"QY-6f8aaa73\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:1:boundary-cause","source_type":"word_analysis","support_id":"sup_f1a5f3dfb585463636c7","text":"{\"blocking_evidence\":null,\"headline\":\"boundary reverses from consequence to cause\",\"reader_payoff\":\"The reader feels the ayah break as continuation: the previous verdict is immediately explained by prior choices.\",\"reason\":\"There is no new conjunction at the opening; the relative pronoun begins the explanation of the preceding final noun.\",\"representative_source_ids\":[\"QT-01b1957a\",\"QT-b19ace3f\",\"QB-c8c87e8c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:4:root-field-narrowed-to-withdrawal","source_type":"word_analysis","support_id":"sup_f50083ef5261bf3e3992","text":"{\"blocking_evidence\":null,\"headline\":\"proximity and authority field is bent into departure\",\"reader_payoff\":\"The reader feels the local turning away as severed nearness and allegiance, while not replacing the selected sense with unrelated authority branches.\",\"reason\":\"V4 preserves nearness, authority, support, and withdrawal branches; the local sequence after denial selects withdrawal, with the relational branches retained as pressure on what is being abandoned.\",\"representative_source_ids\":[\"QS-114f7198\",\"QS-4c4d6f7a\",\"QS-ca3ee2cc\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:4:self-directed-form-v","source_type":"word_analysis","support_id":"sup_f75ece11b821c575281e","text":"{\"blocking_evidence\":null,\"headline\":\"Form V marks self-involving withdrawal\",\"reader_payoff\":\"The reader notices that the word makes the subject participate in his own distancing rather than being externally displaced.\",\"reason\":\"The local Form V surface and active voice support a self-involving reading of the withdrawal.\",\"representative_source_ids\":[\"QF-6a52cb56\",\"QF-bece2c2a\",\"MF-547bafc4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:1:restricted-class-bridge","source_type":"word_analysis","support_id":"sup_fa7a2036e8d2ba59a086","text":"{\"blocking_evidence\":null,\"headline\":\"restricted fire-bound class is unpacked\",\"reader_payoff\":\"The reader sees the exception from 92:15 filled with concrete moral content before the opposite figure appears in 92:17.\",\"reason\":\"The word opens a dependent relative explanation across the ayah boundary, preserving the prior restriction while preparing the next contrast.\",\"representative_source_ids\":[\"QI-bb6f40a7\",\"QE-36ff7543\",\"QY-63ce0146\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:16:2:denial-withdrawal-formula","source_type":"word_analysis","support_id":"sup_fb6b3294761dfb5bed91","text":"{\"blocking_evidence\":null,\"headline\":\"denial pairs with withdrawal as a formula\",\"reader_payoff\":\"The reader sees the verb as the first half of a recognizable rejecter profile: false judgment followed by departure.\",\"reason\":\"The verb is locally coordinated with {{ar:تَوَلَّىٰ}} ({{tr:tawallā}}), and the supplied rows identify the exact recurrence at 75:32.\",\"representative_source_ids\":[\"QI-53ae9103\",\"MT-a58799a0\",\"QE-bf71839f\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ","ayah_ref":"92:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001290/B002","root_001684/B007"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001290","role":"Attribution of falsehood supplies the verbal verdict that licenses disengagement.","root":"ك ذ ب","source_ref":"92:16","source_word_indices":["2"]},{"branch_id":"B007","mapped_root_id":"root_001684","role":"Averting and retreating make the verdict operative as refusal of attention or compliance.","root":"و ل ي","source_ref":"92:16","source_word_indices":["3"]}],"changed_reading":{"after":"The clause depicts one coupled refusal: he invalidates what addresses him and then embodies that judgment by withdrawing.","before":"Two adjacent predicates report that he denied and then turned away."},"confidence":"strong","focus_anchor":"The coordinated Form II كَذَّبَ and Form V تَوَلَّىٰ join a verdict to a bodily or social response.","mechanism":"Declaring the claim or its bearer false licenses withdrawal from attention and compliance; the second verb enacts the first rather than merely adding another fault.","model_id":"B92_16_VERDICT_WITHDRAWAL"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:B92_16_VERDICT_WITHDRAWAL","source_type":"hft","support_id":"sup_453f8fd81af0401ce204","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ","ayah_ref":"92:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001290/B004","root_001684/B003","root_001684/B007"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001290","role":"A charge that fails because it is not carried through supplies the performative sense of falsification.","root":"ك ذ ب","source_ref":"92:16","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001684","role":"Assuming management or charge keeps live the responsibility from which the subject can defect.","root":"و ل ي","source_ref":"92:16","source_word_indices":["3"]},{"branch_id":"B007","mapped_root_id":"root_001684","role":"Withdrawal supplies the act by which the charge is left unfulfilled.","root":"و ل ي","source_ref":"92:16","source_word_indices":["3"]}],"changed_reading":{"after":"Denial can also be a failed performance: he makes his own charge or undertaking false by abandoning it.","before":"Denial is chiefly a false judgment, followed by retreat."},"confidence":"medium","focus_anchor":"كَذَّبَ can activate failure to make a charge true in performance, while تَوَلَّىٰ can hold both taking charge and abandoning it.","mechanism":"The person proves an entrusted undertaking false by not carrying it through; withdrawal can therefore be read as abdication from a charge, not only departure from a proposition.","model_id":"B92_16_FAILED_CHARGE"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:B92_16_FAILED_CHARGE","source_type":"hft","support_id":"sup_a92207de518e12feb0c1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ","ayah_ref":"92:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001290/B009","root_001684/B006","root_001684/B007"],"payload":{"activation_trace":[{"branch_id":"B009","mapped_root_id":"root_001290","role":"A deceptive appearance supplies nonverbal falsification by the state one presents.","root":"ك ذ ب","source_ref":"92:16","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_001684","role":"Turning the face or attention toward something supplies the usually unstated destination of reorientation.","root":"و ل ي","source_ref":"92:16","source_word_indices":["3"]},{"branch_id":"B007","mapped_root_id":"root_001684","role":"Averting supplies the explicit departure pole of the same directional movement.","root":"و ل ي","source_ref":"92:16","source_word_indices":["3"]}],"changed_reading":{"after":"He performs a counter-reality and reorients himself: away from the address, but implicitly toward another face, object, or allegiance.","before":"He rejects an assertion and leaves it."},"confidence":"exploratory","focus_anchor":"The two focus roots permit deception by displayed state and a directional polarity between facing and averting.","mechanism":"A stance can falsify reality without a spoken lie, and turning away from one address necessarily redirects face, attention, or allegiance elsewhere.","model_id":"B92_16_COUNTER_ORIENTATION"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:B92_16_COUNTER_ORIENTATION","source_type":"hft","support_id":"sup_bd3ee6a142530b3ed89d","trust":"legacy_unbound"}]}
</lane_packet_json>
