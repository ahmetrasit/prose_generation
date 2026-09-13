# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **92:4**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s092-regular-20260912/s092/92_4/micro.discovery.json` and modify nothing
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
  "ayah_ref": "92:4",
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
{"branch_registry":[{"boundary":"Şiddetli koşmayla sınırlandırılmamalı; genel hareket ile belirli ibadet yürüyüşü birbirine karıştırılmamalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000709/B001","candidate_links":[{"candidate_id":"cand_1b9c6cc07f42b00bc5d6","lane":"micro"},{"candidate_id":"cand_aa84bba46016ab5a89bd","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","surface_ar":"سَعْيَ"}],"gloss":"hedefe doğru hızlı ve amaçlı ilerleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hedefe doğru isteyerek ilerleme, bağlama göre hızlı yürüme, hafif koşma, gitme veya yönelme biçiminde gerçekleşir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli iki kutsal durak arasındaki özel yürüyüş, hareket çekirdeğinin ibadet alanındaki yerleşik uygulamasıdır."}}],"root_ar":"س ع ي","root_id":"root_000709","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yalın hareket çekirdeğini, hızın şiddetli koşu düzeyine çıkması gerekmeden ve amaçlı yönelişi koruyarak karşılar.","boundary_detail":"Şiddetli koşmayla sınırlandırılmamalı; genel hareket ile belirli ibadet yürüyüşü birbirine karıştırılmamalıdır.","branch_image_ar":"حركة مقصودة إلى المطلوب","concept_gloss":"hedefe doğru hızlı ve amaçlı ilerleme","contextual_glosses":[{"applicability":"Bir çağrıya, amaca veya yapılacak işe doğru gitmenin öne çıktığı bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Amaçlı yönelme ve olağandan hızlı hareket korunur."},"facet_ids":["F001"],"text":"aceleyle yönelmek","usage_role":"contextual"},{"applicability":"Yalnız belirli ibadet uygulamasının söz konusu olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özel güzergah, yürüyüş ve ibadet bağlamı korunur."},"facet_ids":["F002"],"text":"iki kutsal durak arasında yürümek","usage_role":"explanatory"}],"definition":"Bir hedefe doğru isteyerek ilerlemek; bağlama göre hızlı yürümek, şiddetli olmayan biçimde koşmak, gitmek ya da yönelmektir. Belirli iki kutsal durak arasındaki özel yürüyüş bu hareket çekirdeğinin yerleşik bir uygulamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hedefe doğru isteyerek ilerleme, bağlama göre hızlı yürüme, hafif koşma, gitme veya yönelme biçiminde gerçekleşir."},{"facet_id":"F002","role":"specialization","statement":"Belirli iki kutsal durak arasındaki özel yürüyüş, hareket çekirdeğinin ibadet alanındaki yerleşik uygulamasıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bağlama göre koşma, gitme, amaçlı yönelme ve özel ibadet uygulamasını dışarıda bırakır.","preserves":"Hızlı fakat şiddetli olmayan yaya hareketini korur."},"text":"hızlı yürüme"}],"identity_rationale":"Kaynak ifadesi, dalı hedefe yönelik hareket olarak kurar; hızlı yürüme, şiddetli olmayan koşma, gitme ve yönelme bağlama göre bu çekirdeğin gerçekleşmeleridir. Belirli iki kutsal durak arasındaki özel yürüyüş ise genel hareket anlamıyla bağlantılı, yerleşik bir uygulamadır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"hızlı yürüme, hafif koşma veya amaçlı gidiş"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"hızlı yürümek, hafifçe koşmak veya yönelmek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"anma çağrısına yönelmek veya gitmek"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"iki kutsal durak arasındaki özel ibadet yürüyüşü"}],"lexicalization_note":"Tanım, yalın hareket anlamını korurken belirli söyleyişlere bağlı yönelme ve ibadet kullanımlarını ayrı uzmanlaşmalar olarak gösterir.","neighbor_coverage_note":"Bütün adaylar hareket, amaç, hız, kalabalık, yolculuk ve aynı kökün öteki dalları bakımından değerlendirildi; sınırı en açık gösteren üç karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, yürümenin genel adından daha belirgin biçimde hedefe yönelmiş ve hızlı ilerlemeyi anlatır; komşu dal ise sıradan yürümeyi de kapsar.","focus_only":"Hedefe yönelme ve olağandan hızlı, fakat şiddetli olmayan ilerleme odağı vardır.","gloss":"amaçlı hızlı ilerleme ile genel yürüme","neighbor_only":"Her türlü istemli yürüme ve yer değiştirme, hız veya belirli hedef şartı olmadan kapsanır.","neighbor_ref":"root_001427/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da insanın istemli biçimde yaya hareket etmesini kapsar."},{"boundary_match":"partial","distinction":"Odak dal hareketi veya gidişi öne çıkarır; komşu dalın çekirdeği ise hareketten bağımsız biçimde amaç edinme ve yöneltmedir.","focus_only":"Yöneliş çoğu kullanımda gerçek bir gidiş veya hızlı hareket olarak gerçekleşir.","gloss":"ilerleyerek yönelme ile salt amaçlama","neighbor_only":"Bir şeyi amaçlama, bedensel yer değiştirme gerçekleşmeden de var olabilir.","neighbor_ref":"root_000053/B012","relation_type":"near_synonym","shared_zone":"İki dal da belirli bir hedefe bilinçli yöneliş taşır."},{"boundary_match":"partial","distinction":"Odak dal hedefin türünü sınırlamaz ve hareket tarzını öne çıkarır; komşu dal hedefin yüceliği ile ziyaret eylemini çekirdeğe alır.","focus_only":"Hızlı ilerleme ve farklı hedeflere yönelme genel olarak kapsanır.","gloss":"hedefe ilerleme ile yüce hedefi ziyaret","neighbor_only":"Özellikle yüce sayılan bir hedefe gitme ve o hedefi ziyaret etme anlamı vardır.","neighbor_ref":"root_000295/B001","relation_type":"near_neighbor","shared_zone":"Her ikisinde de belirli bir amaca doğru gitme ve varma yönelimi bulunur."}],"source_phrase_ar":"السعي عدو ليس بشديد (ayn)؛ سعى الرجل يسعى سعيا أي عدا (sihah)؛ السعي والذهاب بمعنى واحد وليس هذا باشتداد؛ سعى إذا مشى وسعى إذا عدا وسعى إذا قصد (tahdhib)؛ السعي المشي السريع وهو دون العدو؛ وخص المشي فيما بين الصفا والمروة بالسعي (mufradat)","source_summary":"Kaynaklar, hareketin şiddetli koşu olmadığında ve yürüme, hafif koşma, gitme ya da amaçlı yönelme olarak bağlama göre değişebildiğinde birleşir. Özel ibadet yürüyüşü de bu hareket alanına bağlıdır.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه المشي السريع دون العدو، والذهاب، والمشي أو العدو أو القصد بحسب السياق، ومنه السعي الخاص بين الصفا والمروة.","what_is_not_ar":"ليس محصورا في العدو الشديد، ولا يدخل فيه سعو الليل المختلف فيه."},"support_links":["sup_a17bf6be0bbab470b6f2","sup_af08b2229429b6768fce"]},{"boundary":"Genel iş ve kazanç çekirdeği korunmalı; makam, ihbar ve özgürlüğe bağlı özel kazanç anlamları bu dala taşınmamalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000709/B002","candidate_links":[{"candidate_id":"cand_18ee035e8c50b918aa23","lane":"micro"},{"candidate_id":"cand_4679a76eb54d6973f21e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","surface_ar":"سَعْيَ"}],"gloss":"bir işte çalışıp kazanma ve çaba gösterme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İyi veya kötü herhangi bir işte çalışmak, kazanç sağlamak ve işi etkin biçimde yürütmek temel anlamdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir mesele için ciddi çaba göstermek, iş ve kazanç çekirdeğinin gayret yönünü öne çıkarır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir ailenin geçimi için çalışıp işlerini yürütmek, genel çalışma ve kazanç anlamının belirli bir kullanım alanıdır."}}],"root_ar":"س ع ي","root_id":"root_000709","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İş, kazanç ve ciddi uğraşı birlikte görünür kıldığı için dalın bütün temel bileşenlerini karşılar.","boundary_detail":"Genel iş ve kazanç çekirdeği korunmalı; makam, ihbar ve özgürlüğe bağlı özel kazanç anlamları bu dala taşınmamalıdır.","branch_image_ar":"عمل وكسب وتصرف","concept_gloss":"bir işte çalışıp kazanma ve çaba gösterme","contextual_glosses":[{"applicability":"Eylemin iş yapma ve geçim ya da başka bir amaç için kazanç sağlama yönü baskın olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İş yapma ile bu işten kazanç sağlama birlikte korunur."},"facet_ids":["F001"],"text":"çalışıp kazanmak","usage_role":"general"},{"applicability":"Kazançtan çok bir işin ciddiyetle izlenmesi ve sonuçlandırılması öne çıktığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir işe etkin biçimde yönelme ve ciddi uğraş korunur."},"facet_ids":["F002"],"text":"bir iş için çaba göstermek","usage_role":"contextual"},{"applicability":"Çalışmanın aile bireylerinin geçimini sağlama amacıyla yapıldığı özel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çalışma, kazanç ve aile geçimini üstlenme korunur."},"facet_ids":["F003"],"text":"ailesinin geçimi için çalışmak","usage_role":"explanatory"}],"definition":"İyi ya da kötü bir işte etkin biçimde çalışmak, kazanç sağlamak veya işi yürütmek ve o iş için ciddi çaba göstermektir. Birilerinin geçimini sağlamak bu genel çekirdeğin belirli bir uygulamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İyi veya kötü herhangi bir işte çalışmak, kazanç sağlamak ve işi etkin biçimde yürütmek temel anlamdır."},{"facet_id":"F002","role":"extension","statement":"Bir mesele için ciddi çaba göstermek, iş ve kazanç çekirdeğinin gayret yönünü öne çıkarır."},{"facet_id":"F003","role":"associated_use","statement":"Bir ailenin geçimi için çalışıp işlerini yürütmek, genel çalışma ve kazanç anlamının belirli bir kullanım alanıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kazanç sağlama, işi yürütme ve ciddi çaba gösterme bileşenlerini açıkça taşımaz.","preserves":"Bir işte etkin biçimde bulunma bileşenini korur."},"text":"çalışma"}],"identity_rationale":"Kaynak ifadesi, iyi veya kötü her türlü işte bulunmayı, çalışıp kazanmayı, bir işi yürütmeyi ve o işte ciddi çaba göstermeyi aynı dalda toplar. Bu çerçeve görev makamı, ihbar veya özgürlük bedeline bağlı özel çalışma gibi ayrı dalları gerektirmez.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"iş, kazanç ve ciddi çaba"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"çalışmak, kazanmak ve bir işi yürütmek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"ailesinin geçimi için çalışmak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"çalışma ve iş yürütme"}],"lexicalization_note":"Yalın iş ve kazanç anlamı ile aile geçimi gibi belirli yapılara bağlı kullanımlar ayrı facetlerde tutulur.","neighbor_coverage_note":"Bütün adaylar iş, kazanç, amaçlı eylem, güç yetirme, savsaklama ve aynı kökün özel dalları bakımından karşılaştırıldı; en açıklayıcı dört sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal işi kazanç ve ciddi uğraş yönleriyle kurar; komşu dal ise amaçlı eylemin daha genel adıdır.","focus_only":"Kazanç sağlama, işi yürütme ve ciddi gayret anlamları belirgindir.","gloss":"çalışıp kazanma ile amaçlı eylem","neighbor_only":"Canlıların amaçlı bütün eylemleri, kazanç veya yoğun çaba gerekmeksizin kapsanabilir.","neighbor_ref":"root_001046/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bilinçli biçimde yapılan iyi veya kötü işleri kapsar."},{"boundary_match":"partial","distinction":"Odak dal kazanç kadar genel işi ve gayreti de içerir; komşu dal toplama, üretme ve gelir elde etme yönünde daha belirgindir.","focus_only":"İyi veya kötü her işte çaba ve etkin yürütme, maddi kazanç olmasa da kapsanır.","gloss":"genel çaba ile kazanç üretme","neighbor_only":"Mal toplama, tarımsal üretim ve meslek sahibi olma gibi kazanç alanları ayrıca belirgindir.","neighbor_ref":"root_000303/B001","relation_type":"near_synonym","shared_zone":"İki dal da çalışmayı, kazanmayı ve aile geçimi için uğraşmayı kapsar."},{"boundary_match":"opposed","distinction":"Odak dal etkin çalışma ve gayreti, komşu dal ise aynı sorumluluk ekseninde yetersiz kalma veya geri durmayı anlatır.","focus_only":"İşi etkin biçimde üstlenme, yürütme ve ciddi çaba gösterme vardır.","gloss":"çaba gösterme ile işi savsaklama","neighbor_only":"İşi savsaklama, gevşeklik, ilgisizlik ve yerine getirmede eksiklik vardır.","neighbor_ref":"root_000902/B003","relation_type":"polarity_pair","shared_zone":"İki dal da kişinin bir işi ne ölçüde üstlenip yürüttüğünü değerlendirir."},{"boundary_match":"partial","distinction":"Odak dal genel çalışma ve kazançtır; komşu dal bu faaliyeti belirli bir hukuki durum ve özgürleşme sonucuyla sınırlar.","focus_only":"Çalışma ve kazanç herhangi bir iş veya amaç için olabilir.","gloss":"genel kazanç ile özgürlük bedeli kazanma","neighbor_only":"Kazanç, köleleştirilmiş kişinin özgürlüğü için belirlenmiş bedeli ödemesine bağlıdır.","neighbor_ref":"root_000709/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin çalışarak bir karşılık elde etmesini içerir."}],"source_phrase_ar":"كل عمل من خير أو شر فهو السعي؛ السعي العمل أي الكسب (ayn)؛ إذا عمل وكسب (sihah)؛ أصل السعي التصرف في كل عمل؛ السعي يكون في الصلاح ويكون في الفساد؛ المرء يسعى لغاريه أي يكسب (tahdhib)؛ يستعمل للجد في الأمر خيرا كان أو شرا (mufradat)","source_summary":"Kaynaklar bu dalda işi, kazancı ve bir meselede ciddi çabayı birlikte verir; yapılan işin iyi ya da kötü olması anlamın parçası değildir. Aile geçimi için çalışma, genel çekirdeğin belirli bir uygulamasıdır.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه كل عمل من خير أو شر، والكسب، والتصرف في كل عمل، والجد في الأمر، والسعي على العيال أو في الصلاح والفساد.","what_is_not_ar":"لا يدخل فيه منصب الساعي، ولا الوشاية، ولا كسب العبد لفكاك رقبته، ولا المساعاة بالفجور؛ فهذه فروع مصطلحية مفصولة."},"support_links":["sup_621eb756d39cf4d9bdbe","sup_84c4210b369b365a8586"]},{"boundary":"Görev ve yetki ilişkisi zorunludur; genel çalışma veya üst makama zarar verici bilgi taşıma bu dala dahil değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000709/B003","candidate_links":[{"candidate_id":"cand_18ee035e8c50b918aa23","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","surface_ar":"سَعْيَ"}],"gloss":"bir topluluğun işini yürüten yetkili görevli","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun belirli bir işini yürütmek üzere görevlendirilmiş ve o işten sorumlu kişi temel kimliktir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Vergi veya toplumsal yükümlülükleri toplamakla görevli kişi, dalın en belirgin uzmanlaşmasıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir topluluğun başkanı veya üst makam karşısındaki yetkili temsilcisi de görev ve sorumluluk çekirdeğine dayanır."}}],"root_ar":"س ع ي","root_id":"root_000709","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel görev ilişkisini, topluluğa karşı sorumluluğu ve vergi toplama gibi uzmanlaşmalara açık yapıyı birlikte karşılar.","boundary_detail":"Görev ve yetki ilişkisi zorunludur; genel çalışma veya üst makama zarar verici bilgi taşıma bu dala dahil değildir.","branch_image_ar":"ولاية وسعاية على القوم","concept_gloss":"bir topluluğun işini yürüten yetkili görevli","contextual_glosses":[{"applicability":"Görevin toplumsal yükümlülükleri veya vergiyi toplamak olduğu bağlamlarda doğal ve doğrudan karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Atanmış görevli olma ve vergi toplama sorumluluğu korunur."},"facet_ids":["F002"],"text":"vergi memuru","usage_role":"contextual"},{"applicability":"Kişinin topluluğun karar ve temsil makamı olduğu özel kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluğa başkanlık etme ve onu yetkiyle temsil etme korunur."},"facet_ids":["F003"],"text":"topluluk başkanı","usage_role":"contextual"}],"definition":"Bir topluluk adına bir işi yürütmek üzere yetkilendirilmiş görevli veya başkandır; özellikle vergi toplamakla görevlendirilen kişi için kullanılır. Yetki, yalnız çalışmaktan değil topluluğun işini üstlenmekten doğar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun belirli bir işini yürütmek üzere görevlendirilmiş ve o işten sorumlu kişi temel kimliktir."},{"facet_id":"F002","role":"specialization","statement":"Vergi veya toplumsal yükümlülükleri toplamakla görevli kişi, dalın en belirgin uzmanlaşmasıdır."},{"facet_id":"F003","role":"extension","statement":"Bir topluluğun başkanı veya üst makam karşısındaki yetkili temsilcisi de görev ve sorumluluk çekirdeğine dayanır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka topluluk işlerini üstlenen görevliyi, başkanı ve yetkili temsilciyi dışarıda bırakır.","preserves":"Dalın en yaygın uzmanlaşması olan vergi toplama görevini korur."},"text":"vergi toplama görevlisi"}],"identity_rationale":"Kaynak ifadesi, bir topluluğun işini yürütmek üzere görevlendirilen kişiyi merkeze alır ve vergi toplama görevini en yaygın uzmanlaşma olarak gösterir. Topluluk başkanı veya yetkili temsilcisi de makamın kapsamındaki bir uzantıdır; ihbar eden kişi bu kimliğe girmez.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"vergi toplama görevi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"atanmış yönetici veya vergi toplama görevlisi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"atanmış yöneticiler veya vergi toplama görevlileri"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"vergi toplamakla görevlendirilmek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"bir din topluluğunun başkanı ve yetkili temsilcisi"}],"lexicalization_note":"Genel görevli anlamı, vergi toplama uzmanlaşması ve belirli topluluklardaki başkanlık kullanımı birbirine karıştırılmadan korunur.","neighbor_coverage_note":"Bütün adaylar görevden alma, yönetim, kamu işi, başkanlık, temsil ve aynı kökün öteki anlamları bakımından değerlendirildi; görev sınırını en iyi gösteren üçü yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal görevlinin topluluk karşısındaki kimliğini anlatır; komşu dal işin kendisini, görevlendirmeyi ve kamu hizmetine atanmayı daha geniş işler.","focus_only":"Topluluk üzerinde görev alma ve özellikle vergi toplama kimliği öne çıkar.","gloss":"topluluk görevlisi ile kamu işine atanma","neighbor_only":"Devlet işine atanma eylemi ve görevi birine verme süreci ayrıca kapsanır.","neighbor_ref":"root_001046/B003","relation_type":"near_synonym","shared_zone":"İki dal da kamu işi üstlenen görevlileri ve vergi toplayan kişileri kapsar."},{"boundary_match":"field_only","distinction":"Odak dal belirli işi yürüten görevliyi, komşu dal ise daha genel yönetim ve buyurma makamını tanımlar.","focus_only":"Belirli bir topluluk işini yürütme ve vergi toplama gibi görev sorumluluğu vardır.","gloss":"görevli ile yönetim makamı","neighbor_only":"Genel yönetme, buyurma ve yönetici atama yetkisi çekirdektedir.","neighbor_ref":"root_000051/B003","relation_type":"same_field","shared_zone":"Her iki dal da topluluk üzerinde tanınmış bir yetki ve sorumluluk konumunu anlatır."},{"boundary_match":"partial","distinction":"Odak dal iş yürütme ve toplama yetkisine dayanır; komşu dal topluluğu tanıma, gözetme ve onun hakkında bilgi verme rolüne dayanır.","focus_only":"Vergi toplama veya topluluk adına belirli işi yürütme görevi bulunur.","gloss":"yetkili görevli ile yerel temsilci","neighbor_only":"İnsanları tanıyan, durumlarını üst makama bildiren daha alt düzey temsilci kimliği bulunur.","neighbor_ref":"root_001002/B006","relation_type":"near_neighbor","shared_zone":"İki dal da bir topluluk ile üst yönetim arasında sorumlu bir görevliyi konu alır."}],"source_phrase_ar":"السعاية في أخذ الصدقات (maqayis)؛ الساعي الذي يولى قبض الصدقات والجمع سعاة (ayn)؛ من ولى شيئا على قوم فهو ساع عليهم وأكثر ما يقال ذلك في ولاة الصدقة (sihah)؛ الساعي الذي يقوم بأمر أصحابه عند السلطان؛ عامل الصدقات ساع؛ ساعي اليهود والنصارى هو رئيسهم؛ من ولى عملا على قوم فهو ساع عليهم (tahdhib)؛ خصت السعاية بأخذ الصدقة (mufradat)","source_summary":"Kaynaklar, bir topluluk üzerinde iş üstlenen görevliyi ve özellikle vergi toplayıcısını ortak biçimde tanımlar. Kimi kullanımlarda bu görevli topluluk başkanı veya üst makam karşısındaki temsilci düzeyine genişler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الساعي الذي يلي أمرا على قوم، وعامل الصدقات، والرئيس أو الوالي الذي يصدر عنه القوم.","what_is_not_ar":"ليس هو الوشاية إلى السلطان، ولا مطلق السعي والعمل."},"support_links":["sup_84c4210b369b365a8586"]},{"boundary":"Bir kişi, onun aleyhindeki bildirim ve daha yüksek bir yetkili arasındaki yönlü ilişki korunmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000709/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","surface_ar":"سَعْيَ"}],"gloss":"birini üst makama kötüleyerek ihbar etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi hakkında onun üstündeki yetkiliye zarar verici bildirimde bulunmak temel eylemdir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Söz taşıma ve ihbarcılık, bildirilen kişiyi yıkıma sürükleyen sonuçlarıyla birlikte bu çekirdekten gelişir."}}],"root_ar":"س ع ي","root_id":"root_000709","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hakkında bilgi taşınan kişiyi, üst makamı ve zarar verici bildirimi aynı ifadede koruduğu için dalın tam çekirdeğini verir.","boundary_detail":"Bir kişi, onun aleyhindeki bildirim ve daha yüksek bir yetkili arasındaki yönlü ilişki korunmalıdır.","branch_image_ar":"وشاية إلى السلطان","concept_gloss":"birini üst makama kötüleyerek ihbar etme","contextual_glosses":[{"applicability":"Bir kişi hakkındaki zarar verici bilginin ondan daha yetkili bir makama taşındığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hedef kişi, üst makam ve yönlü bildirim ilişkisi korunur."},"facet_ids":["F001"],"text":"yetkiliye ihbar etmek","usage_role":"general"},{"applicability":"İhbarın söz taşıma ve kişiyi zor durumda bırakma yönü öne çıktığında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilginin hedef kişiye karşı ve zarar verici biçimde taşınması korunur."},"facet_ids":["F002"],"text":"aleyhine bilgi taşımak","usage_role":"contextual"}],"definition":"Bir kişiyi zarara uğratmak üzere onun hakkında daha yüksek bir yetkiliye bilgi taşımak veya ihbarda bulunmaktır. Söz taşıma, bu yönlü bildirim ve zarar sonucu bulunduğunda dalın parçasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi hakkında onun üstündeki yetkiliye zarar verici bildirimde bulunmak temel eylemdir."},{"facet_id":"F002","role":"extension","statement":"Söz taşıma ve ihbarcılık, bildirilen kişiyi yıkıma sürükleyen sonuçlarıyla birlikte bu çekirdekten gelişir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yetkiliye yönelmeyen gündelik söylenti ve konuşmaları da kapsar.","collision":"Gündelik konuşma anlamı, özel ihbar ilişkisini görünmez kılar.","fit":"displacement","loses":"Bilginin daha yüksek bir yetkiliye yönelmesini ve hedef kişiye somut zarar verme amacını siler.","preserves":"Başkası hakkında olumsuz bilgi aktarma yönünü kısmen korur."},"text":"dedikodu"}],"identity_rationale":"Kaynak ifadesi, bir kişi hakkında üst makama zarar verici bilgi taşımayı ve bunu yapan muhbiri açıkça tanımlar. Dedikodu ve söz taşıma ancak bu ihbar ilişkisine bağlandığında dala girer; meşru görev yürütme veya yalnız tehdit etme aynı kimlik değildir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"üst makama kötüleyerek ihbar etme"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birini yöneticiye kötüleyerek ihbar etmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"üst makama söz taşıyan ihbarcı"}],"lexicalization_note":"Ad biçimindeki ihbar anlamı ile birini üst makama bildiren belirli yapı ayrı gösterilir; genel dedikoduya genişletilmez.","neighbor_coverage_note":"Bütün adaylar ihbar, söz taşıma, tehdit, yardım isteme ve aynı kökün görev anlamı bakımından değerlendirildi; gerçek anlam örtüşmesi taşıyan iki komşu ile temel iç karşıtlık seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekler büyük ölçüde örtüşür; odak dal ihbarcı rolünü ve üst makama yönelişi belirginleştirirken komşu dal zarar verici suçlama alanına biraz daha genişler.","focus_only":"Üst makama bilgi taşıyan kişi ve bu eylemin yıkıcı sonucu ayrıca adlandırılır.","gloss":"üst makama ihbar ile zarar verici suçlama","neighbor_only":"Birini kötü duruma düşürecek biçimde hakkında tanıklık kurdurma uzantısı da bulunur.","neighbor_ref":"root_001402/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da birini yöneticiye kötüleyerek zarar verici bilgi aktarmayı kapsar."},{"boundary_match":"partial","distinction":"Odak dal yönü üst makama sabitlenmiş ihbardır; komşu dal ise alıcısı herhangi biri olabilen daha genel söz taşıma alanıdır.","focus_only":"Söz mutlaka hedef kişinin üstündeki yetkiliye ve onun zararına taşınır.","gloss":"yetkiliye ihbar ile genel söz taşıma","neighbor_only":"İnsanlar arasında dolaşan söz taşıma, belirli bir yetkili hedefi olmadan da kapsanır.","neighbor_ref":"root_001557/B002","relation_type":"near_synonym","shared_zone":"İki dal da başkası hakkında zarar verici söz taşımayı ve bunu yapan kişiyi anlatır."},{"boundary_match":"field_only","distinction":"Odak dal zarar verici ihbara, komşu dal ise tanınmış görev ve topluluk adına iş yürütmeye dayanır.","focus_only":"Bir kişi aleyhinde üst makama zarar verici bilgi taşıma vardır.","gloss":"ihbarcı ile yetkili görevli","neighbor_only":"Bir topluluğun işini yetkiyle yürütme ve vergi toplama gibi meşru görevler vardır.","neighbor_ref":"root_000709/B003","relation_type":"same_field","shared_zone":"Her iki dalda da bir üst makamla ilişki kuran ve başkaları hakkında işlem yapan kişi bulunabilir."}],"source_phrase_ar":"السعاية أن تسعى بصاحبك إلى وال أو من فوقه (ayn)؛ سعى به إلى الوالي إذا وشى به (sihah)؛ الساعي الذي يسعى بصاحبه إلى سلطانه؛ القتات والساعي والماحل واحد؛ الساعي مثلث بإهلاكه ثلاثة نفر (tahdhib)؛ خصت السعاية بالنميمة (mufradat)","source_summary":"Kaynaklar, birini üst makama bildirme ile söz taşıma ve ihbarcılığı aynı zarar verici eylem alanında birleştirir. Eylemin ayırt edici yönü, bilginin hakkında konuşulan kişiden daha yetkili birine taşınmasıdır.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أن يسعى بصاحبه إلى وال أو سلطان، والنميمة والماحلة والقتاتة التي تهلك المسعي به.","what_is_not_ar":"ليس هو ولاية الصدقة أو القيام المشروع بأمر القوم."},"support_links":[]},{"boundary":"Çalışan kişinin bağlı durumu, ödenecek özgürlük bedeli ve çalışma ile özgürleşme arasındaki sonuç ilişkisi korunmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000709/B005","candidate_links":[{"candidate_id":"cand_382375fffd93a2d4b8a4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","surface_ar":"سَعْيَ"}],"gloss":"özgürlük bedelini çalışarak ödeme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Köleleştirilmiş kişi, özgürlüğü için belirlenen bedeli karşılamak üzere çalışır ve kazancını ödemeye ayırır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özgürlük sözleşmesi bulunan kişi, kararlaştırılmış bedeli kazanıp ödeyerek bağlılığını sona erdirmeye çalışır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kısmen özgür bırakılan kişi, bağlılığının kalan payına karşılık gelen değeri çalışarak ödemekle yükümlü tutulabilir."}}],"root_ar":"س ع ي","root_id":"root_000709","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çalışma, bedel ödeme ve bunun sonucunda bağlılıktan kurtulma aşamalarını tek bir doğal ifadede korur.","boundary_detail":"Çalışan kişinin bağlı durumu, ödenecek özgürlük bedeli ve çalışma ile özgürleşme arasındaki sonuç ilişkisi korunmalıdır.","branch_image_ar":"كسب العبد لفكاك رقبته","concept_gloss":"özgürlük bedelini çalışarak ödeme","contextual_glosses":[{"applicability":"Kişinin bağlılıktan kurtulmak için kendi emeğiyle belirli bir bedeli kazandığı ve ödediği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çalışma, ödeme amacı ve özgürlüğe ulaşma sonucu korunur."},"facet_ids":["F001","F002"],"text":"özgürlüğü için çalışıp ödeme yapmak","usage_role":"general"},{"applicability":"Kısmen özgür bırakılmış kişinin bağlılığından kalan payın değerini emekle tamamladığı durumda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kısmi özgürleşme, kalan değer ve çalışarak ödeme korunur."},"facet_ids":["F003"],"text":"kalan bedelini çalışarak ödemek","usage_role":"contextual"}],"definition":"Köleleştirilmiş kişinin özgürlüğünü elde etmek için belirlenmiş bedeli çalışıp kazanarak ödemesi veya kısmen özgür bırakıldığında kalan değerini çalışarak tamamlamasıdır. Süreç, genel kazançtan farklı olarak özgürleşme sonucuna bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Köleleştirilmiş kişi, özgürlüğü için belirlenen bedeli karşılamak üzere çalışır ve kazancını ödemeye ayırır."},{"facet_id":"F002","role":"specialization","statement":"Özgürlük sözleşmesi bulunan kişi, kararlaştırılmış bedeli kazanıp ödeyerek bağlılığını sona erdirmeye çalışır."},{"facet_id":"F003","role":"source_variant","statement":"Kısmen özgür bırakılan kişi, bağlılığının kalan payına karşılık gelen değeri çalışarak ödemekle yükümlü tutulabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bedelin çalışma yoluyla kazanılmasını, ödenmesini ve kısmi özgürleşmedeki kalan payı siler.","preserves":"Sürecin özgürleşme sonucunu korur."},"text":"kölelikten kurtulma"}],"identity_rationale":"Kaynak ifadesi, köleleştirilmiş kişinin özgürlük bedelini çalışarak kazanmasını ve kısmen özgür bırakılan kişinin kalan değer için çalıştırılmasını aynı hukuki-ekonomik süreçte toplar. Genel kazanç değil, çalışmanın özgürleşme bedeline bağlanması dalı kurar.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"köleleştirilmiş kişinin özgürlüğü için çalışması"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"özgürlük bedelini çalışarak kazanma"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"özgürlük sözleşmesinin bedelini çalışarak ödemek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"köleleştirilmiş kişiyi kendi bedeli için çalıştırmak"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kalan özgürlük bedelini çalışarak ödeyen kişi"}],"lexicalization_note":"Özgürlük bedeli için çalışma çekirdeği ile sözleşmeli ve kısmi özgürleşme durumlarına bağlı yapılar ayrı facetlerde gösterilir.","neighbor_coverage_note":"Bütün adaylar özgür bırakma, özgürlük sözleşmesi, beden değeri, iş karşılığı, kaçış ve zorunlu emek bakımından değerlendirildi; süreç, araç ve sonuç ayrımını gösteren üçü seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sözleşmenin yerine getirilmesi için çalışmayı, komşu dal ise özgürleşmeyi düzenleyen anlaşmanın kendisini tanımlar.","focus_only":"Kararlaştırılmış bedeli fiilen çalışıp kazanma ve ödeme süreci anlatılır.","gloss":"bedeli kazanma ile özgürlük sözleşmesi","neighbor_only":"Özgürleşme için bedel ve taksitleri belirleyen sözleşmenin kurulması anlatılır.","neighbor_ref":"root_001283/B005","relation_type":"near_neighbor","shared_zone":"İki dal da köleleştirilmiş kişinin belirli bir bedel karşılığında özgürleşmesini konu alır."},{"boundary_match":"thematic_only","distinction":"Odak dal araç ve ödeme sürecidir; komşu dal bu sürecin sağlayabileceği durum değişikliğini veya özgürlüğün kendisini anlatır.","focus_only":"Özgürlüğe varmak için bedeli emekle kazanıp ödeme süreci vardır.","gloss":"özgürlük bedeli süreci ile özgürlük durumu","neighbor_only":"Bağlılığın karşıtı olan özgür durum ve serbest bırakma sonucu doğrudan anlatılır.","neighbor_ref":"root_000306/B002","relation_type":"thematic","shared_zone":"Odak dalın amaçlanan sonucu, komşu dalın doğrudan anlattığı özgür durumdur."},{"boundary_match":"field_only","distinction":"Odak dal emeği özgürlük bedeline ve sona erecek bağlılığa bağlar; komşu dalın çekirdeği karşılıksız ve zorunlu emektir.","focus_only":"Çalışma belirli bir bedeli ödeyip özgürleşmeye yönelir.","gloss":"özgürlük için çalışma ile karşılıksız zorla çalışma","neighbor_only":"Çalışan ücretsiz ve zorunlu emeğe koşulur; özgürleşme bedeli kurucu değildir.","neighbor_ref":"root_000685/B002","relation_type":"same_field","shared_zone":"Her iki dal da bağlı veya güçsüz durumdaki kişinin çalıştırılmasını konu alır."}],"source_phrase_ar":"سعاية العبد إذا كوتب أن يسعى فيما يفك رقبته (maqayis)؛ السعاية ما يستسعى فيه العبد من ثمن رقبته (ayn)؛ سعى المكاتب في عتق رقبته سعاية؛ استسعيت العبد في قيمته (sihah)؛ استسعاء العبد إذا عتق بعضه ورق بعضه؛ يستسعى في ثلثي رقبته (tahdhib)؛ خصت السعاية بكسب المكاتب لعتق رقبته (mufradat)","source_summary":"Kaynaklar, çalışmayı özgürlük için ödenecek bedele bağlar. Süreç hem sözleşmeli kişinin kendi bedelini kazanmasını hem de kısmi özgürleşmeden sonra kalan payın değerini çalışarak ödemesini kapsar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه سعاية المكاتب أو العبد في ثمن رقبته، واستسعاؤه في قيمته أو فيما بقي من رقه حتى يعتق.","what_is_not_ar":"لا يدخل فيه مطلق الكسب، ولا المساعاة بالفجور."},"support_links":["sup_f39832ef1db403a51296"]},{"boundary":"Yalnız cömertlik duygusu değil, kişiye veya topluluğa kalıcı onur sağlayan eylem ve başarı anlatılmalıdır.","branch_kind":"bare","branch_ref":"root_000709/B006","candidate_links":[{"candidate_id":"cand_18ee035e8c50b918aa23","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","surface_ar":"سَعْيَ"}],"gloss":"övünç getiren soylu ve cömert iş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Cömertlik ve iyilikle gerçekleştirilen, sahibine onur ve övünç kazandıran değerli iş temel anlamdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu tür işlerin toplulukça anılan başarılar ve övünç kaynakları olarak kalması, çekirdeğin sonuç yönüdür."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çatışmayı sona erdirmek ve can kaybını önlemek için bedel üstlenen kişilerin işi, onurlu eylemin belirgin bir örneğidir."}}],"root_ar":"س ع ي","root_id":"root_000709","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylemi, cömertlik değerini ve kalıcı onur sonucunu birlikte taşıdığı için dalın tam çekirdeğini karşılar.","boundary_detail":"Yalnız cömertlik duygusu değil, kişiye veya topluluğa kalıcı onur sağlayan eylem ve başarı anlatılmalıdır.","branch_image_ar":"مسعاة المكارم","concept_gloss":"övünç getiren soylu ve cömert iş","contextual_glosses":[{"applicability":"Bir kişinin veya topluluğun geçmişteki değerli eylemlerinden ve kalıcı başarılarından söz edilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Değerli eylemler, toplumsal onur ve kalıcı övünç korunur."},"facet_ids":["F001","F002"],"text":"övünç kaynağı soylu işler","usage_role":"general"},{"applicability":"Çatışan tarafları uzlaştırmak ve can kaybını önlemek için maddi yük üstlenildiği özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uzlaştırma, bedel üstlenme ve toplum yararına onurlu girişim korunur."},"facet_ids":["F003"],"text":"barış için bedel üstlenmek","usage_role":"explanatory"}],"definition":"Cömertlik, iyilik veya toplum yararına girişim yoluyla kişiye ya da topluluğa onur ve övünç kazandıran değerli iş veya başarıdır. Çatışmayı bitirmek için bedel üstlenmek bunun toplumsal bir örneğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Cömertlik ve iyilikle gerçekleştirilen, sahibine onur ve övünç kazandıran değerli iş temel anlamdır."},{"facet_id":"F002","role":"extension","statement":"Bu tür işlerin toplulukça anılan başarılar ve övünç kaynakları olarak kalması, çekirdeğin sonuç yönüdür."},{"facet_id":"F003","role":"example","statement":"Çatışmayı sona erdirmek ve can kaybını önlemek için bedel üstlenen kişilerin işi, onurlu eylemin belirgin bir örneğidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Somut değerli eylemi, kalıcı başarıyı, toplumsal onuru ve barış için yük üstlenme örneğini siler.","preserves":"Dalın değer temelini oluşturan eli açıklığı ve iyilik yönünü korur."},"text":"cömertlik"}],"identity_rationale":"Kaynak ifadesi, cömertlik ve iyilik yoluyla kazanılan övünç verici işleri ve onurlu başarıları dalın çekirdeği yapar. Barış sağlamak için bedel üstlenme ve çatışmayı söndürme, bu çekirdeğin toplumsal bir örneğidir; genel çalışma anlamı değildir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"cömertlikle kazanılan onurlu iş ve başarı"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"övünç veren onurlu işler ve başarılar"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"barış için bedel üstlenen uzlaştırıcılar"}],"lexicalization_note":"Tanım yalın olarak onur kazandıran cömert eylem ve başarıyı verir; barış için bedel üstlenmeyi yalnız destekleyici örnek sayar.","neighbor_coverage_note":"Bütün adaylar saygınlık, cömertlik, kişilik, ayıplama, uzlaştırma ve aynı kökün genel çalışma anlamı bakımından değerlendirildi; çekirdek ile örneği ayıran üç karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal somut, cömert ve yararlı eyleme dayanır; komşu dal eylem dışında soy, servet ve kişilik gibi daha geniş saygınlık kaynaklarını da içerir.","focus_only":"Cömertlik veya toplum yararı için yapılmış belirli eylem ve başarı çekirdektedir.","gloss":"onurlu iş ile genel övünç mirası","neighbor_only":"Soydan gelen saygınlık, mal, kişilik ve din gibi eylem dışı övünç kaynakları da kapsanır.","neighbor_ref":"root_000318/B004","relation_type":"near_synonym","shared_zone":"İki dal da kişi veya topluluğa saygınlık kazandıran ve övünçle anılan değerleri kapsar."},{"boundary_match":"partial","distinction":"Odak dal cömert eylem ve toplumsal yararı öne çıkarır; komşu dal övgüye değer özellik ve başarıların daha genel adıdır.","focus_only":"Cömertlik, iyilik ve barış için yük üstlenme yoluyla kazanılan onur belirgindir.","gloss":"cömert onurlu iş ile övgüye değer özellik","neighbor_only":"Her türlü güzel kişilik özelliği ve yiğitçe başarı, cömertlik şartı olmadan kapsanır.","neighbor_ref":"root_001539/B010","relation_type":"near_synonym","shared_zone":"Her ikisi de kişiyi övgüye ve onura değer kılan iyi eylem ve başarıları anlatır."},{"boundary_match":"partial","distinction":"Odak dal uzlaştırmayı onurlu ve cömert işlerden biri sayar; komşu dalın doğrudan anlamı ilişkileri düzeltme ve dayanışmadır.","focus_only":"Uzlaştırma, onur kazandıran eylemin bir örneğidir ve maddi yük üstlenmeyi içerebilir.","gloss":"onurlu girişim ile uzlaştırma","neighbor_only":"Bozulan ilişkileri düzeltme ve başkalarına mal veya canla destek olma doğrudan çekirdektir.","neighbor_ref":"root_000034/B002","relation_type":"near_neighbor","shared_zone":"İki dal toplum yararına çatışmayı giderme ve insanlara destek olma durumunda buluşur."}],"source_phrase_ar":"المسعاة في الكرم والجود (maqayis)؛ المسعاة في الكرم والجود (ayn)؛ المسعاة واحدة المساعي في الكرم والجود (sihah)؛ أصحاب الحمالات لحقن الدماء وإطفاء النائرة سعاة؛ مآثر أهل الشرف والفضل مساعي واحدتها مسعاة (tahdhib)؛ المسعاة بطلب المكرمة (mufradat)","source_summary":"Kaynaklar, cömertlik ve iyilikle bağlantılı onurlu eylemi ve bunun bıraktığı övünç verici başarıyı ortaklaştırır. Barış sağlamak, çatışmayı söndürmek ve bunun için bedel üstlenmek bu değerin somut örnekleridir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه المسعاة والمساعي بمعنى المآثر والمكارم والكرم والجود وطلب المكرمة، ومنه السعي في الصلح وحمل الحمالات لحقن الدماء.","what_is_not_ar":"لا يدخل فيه مطلق العمل والكسب إذا خلا من صورة المكرمة أو المأثرة."},"support_links":["sup_84c4210b369b365a8586"]},{"boundary":"Köleleştirilmiş kadın katılımcı sınırı korunmalı; sahibin zorlayıcı ve kazanç sağlayıcı rolü karşılıklı ilişki kullanımından ayrılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000709/B007","candidate_links":[{"candidate_id":"cand_382375fffd93a2d4b8a4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","surface_ar":"سَعْيَ"}],"gloss":"köleleştirilmiş kadınla ilişki veya onu cinsel kazanca zorlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir erkeğin köleleştirilmiş bir kadınla evlilik dışı cinsel ilişkiye girmesi, belirli katılımcılarla sınırlı kullanımdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kadının sahibi, ondan belirli bir kazanç bekleyerek onu para karşılığında cinsel ilişkiye zorlar."}}],"root_ar":"س ع ي","root_id":"root_000709","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Katılımcı sınırını ve sahibin kazanç için uyguladığı zorlamayı, karşılıklı ilişki kullanımından ayırarak birlikte taşır.","boundary_detail":"Köleleştirilmiş kadın katılımcı sınırı korunmalı; sahibin zorlayıcı ve kazanç sağlayıcı rolü karşılıklı ilişki kullanımından ayrılmalıdır.","branch_image_ar":"مساعاة الإماء بالفجور","concept_gloss":"köleleştirilmiş kadınla ilişki veya onu cinsel kazanca zorlama","contextual_glosses":[{"applicability":"Bir erkeğin köleleştirilmiş bir kadınla cinsel ilişkiye girmesini anlatan karşılıklı yapı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Erkek ile köleleştirilmiş kadın arasındaki evlilik dışı cinsel ilişki korunur."},"facet_ids":["F001"],"text":"köleleştirilmiş bir kadınla evlilik dışı ilişkiye girmek","usage_role":"contextual"},{"applicability":"Sahibin kadına, para karşılığındaki cinsel ilişkilerden karşılanacak bir ödeme yüklediği kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sahibin zorlaması, cinsel sömürü ve kazanç yükümlülüğü korunur."},"facet_ids":["F002"],"text":"köleleştirilmiş kadını cinsel kazanca zorlamak","usage_role":"explanatory"}],"definition":"Yalnız köleleştirilmiş kadınlarla ilgili olarak, bir erkeğin böyle bir kadınla evlilik dışı cinsel ilişkiye girmesi veya sahibinin onu para karşılığında cinsel ilişkiye zorlamasıdır. İkinci durumda sahibin koyduğu kazanç yükümlülüğü kurucu bir unsurdur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir erkeğin köleleştirilmiş bir kadınla evlilik dışı cinsel ilişkiye girmesi, belirli katılımcılarla sınırlı kullanımdır."},{"facet_id":"F002","role":"specialization","statement":"Kadının sahibi, ondan belirli bir kazanç bekleyerek onu para karşılığında cinsel ilişkiye zorlar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Özgür kadınlar dahil her katılımcıyla gerçekleşen ilişkileri kapsama alır.","collision":"Genel cinsel ilişki anlamı, tarihsel katılımcı ve sömürü sınırını görünmez kılar.","fit":"displacement","loses":"Köleleştirilmiş kadınlarla sınırlılığı ve sahibin kazanç için uyguladığı zorlamayı siler.","preserves":"Evlilik bağı dışındaki cinsel ilişki bileşenini korur."},"text":"evlilik dışı cinsel ilişki"}],"identity_rationale":"Kaynak ifadesi iki bağlı durumu açıkça verir: bir erkeğin köleleştirilmiş bir kadınla evlilik dışı cinsel ilişkiye girmesi ve sahibin böyle bir kadını ödeme getiren cinsel ilişkilere zorlaması. Her iki kullanım da özellikle köleleştirilmiş kadınlarla sınırlıdır; genel cinsel suç anlamına genişletilemez.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"köleleştirilmiş bir kadınla evlilik dışı cinsel ilişkiye girmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"köleleştirilmiş kadınlarla sınırlı evlilik dışı ilişki veya onları cinsel kazanca zorlama"}],"lexicalization_note":"Belirli katılımcıları gösteren ilişki yapısı ile cinsel sömürü adı ayrı facetlerde tutulur ve bütün kadınlara genellenmez.","neighbor_coverage_note":"Bütün adaylar genel evlilik dışı ilişki, cinsel suç, zorla çalıştırma, katılımcı kimliği, kazanç ve korunma bakımından değerlendirildi; katılımcı ile sömürü sınırını gösteren dört karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal katılımcıyı köleleştirilmiş kadınla sınırlar ve sahibin kazanç amaçlı zorlamasını içerebilir; komşu dal genel cinsel davranış alanıdır.","focus_only":"Köleleştirilmiş kadınla sınırlı karşılıklı yapı ve sahibin kazanç için zorlaması vardır.","gloss":"sınırlı cinsel sömürü ile genel evlilik dışı ilişki","neighbor_only":"Evlilik dışı cinsel ilişki, kadının bağlılık durumu veya bir sahibin kazanç yükümlülüğü olmadan genel biçimde kapsanır.","neighbor_ref":"root_000138/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da evlilik dışı cinsel ilişkiyi ve bundan doğan toplumsal kınamayı konu alır."},{"boundary_match":"partial","distinction":"Odak dal tarihsel olarak belirli kadınlarla ve kimi zaman ekonomik zorlamayla sınırlıdır; komşu dalın çekirdeği yalnız evlilik bağının yokluğudur.","focus_only":"Kadının bağlı durumu ve bazı kullanımlarda sahibin para beklentisi kurucudur.","gloss":"köleleştirilmiş kadınla ilişki ile evlilik bağı olmayan ilişki","neighbor_only":"Geçerli evlilik bağı olmadan sürdürülen cinsel ilişki, katılımcıların bağlılık durumu gözetilmeden kapsanır.","neighbor_ref":"root_000711/B002","relation_type":"near_neighbor","shared_zone":"İki dal da geçerli evlilik bağı dışında gerçekleşen cinsel ilişkiyi kapsar."},{"boundary_match":"thematic_only","distinction":"Odak dal cinsel sömürü ve kazanç yükümlülüğüne özgüdür; komşu dal cinsel olmayan karşılıksız zorunlu emeği anlatır.","focus_only":"Zorlama, para karşılığındaki cinsel ilişkilerden kazanç elde etmeye yönelir.","gloss":"cinsel kazanca zorlama ile karşılıksız zorla çalıştırma","neighbor_only":"Zorlama, herhangi bir işin karşılıksız yaptırılmasına yönelir ve cinsel içerik taşımaz.","neighbor_ref":"root_000685/B002","relation_type":"thematic","shared_zone":"Her iki dalda da güç sahibi kişi bağlı durumdaki birini kendi yararı için zorla çalıştırır."},{"boundary_match":"thematic_only","distinction":"Odak dal bu kişiyi içeren belirli bir cinsel eylemi ve sömürüyü anlatır; komşu dal yalnız katılımcının toplumsal durumunu adlandırır.","focus_only":"Köleleştirilmiş kadınla kurulan cinsel ilişki veya ona uygulanan cinsel kazanç zorlaması anlatılır.","gloss":"kadına yönelik eylem ile kadın kimliği","neighbor_only":"Köleleştirilmiş kadın yalnız kişi türü olarak adlandırılır; herhangi bir eylem veya sömürü ilişkisi kurulmaz.","neighbor_ref":"root_000053/B014","relation_type":"thematic","shared_zone":"Köleleştirilmiş kadın, odak dalın zorunlu katılımcısı ve komşu dalın doğrudan adlandırdığı kişidir."}],"source_phrase_ar":"ساعي الرجل الأمة إذا فجر بها؛ لا تكون المساعاة إلا في الإماء خاصة (maqayis)؛ يقال في الأمة خاصة قد ساعاها؛ لا تكون المساعاة إلا في الإماء؛ إماء ساعين في الجاهلية (sihah)؛ المساعاة الزنى؛ لا تكون في الحرائر إنما تكون في الإماء؛ مساعاة الأمة إذ ساعاها مالكها فضرب عليها ضريبة تؤديها بالزنى (tahdhib)؛ خصت المساعاة بالفجور (mufradat)","source_summary":"Kaynaklar, anlamı özellikle köleleştirilmiş kadınlarla sınırlar. Malzeme hem bir erkeğin böyle bir kadınla evlilik dışı ilişkisini hem de sahibin kadına cinsel yoldan karşılanacak bir kazanç yükümlülüğü koymasını kapsar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه المساعاة الخاصة بالإماء: أن يساعي الرجل الأمة أو يضرب عليها ضريبة تؤديها بالزنى، وما ورد في إماء ساعين.","what_is_not_ar":"لا يدخل فيه الزنى مطلقا في الحرائر والنساء، ولا كسب العبد لفكاك رقبته."},"support_links":["sup_f39832ef1db403a51296"]},{"boundary":"Karşılıklı uğraş, aynı etkinlik alanı ve sonuçta rakibe üstün gelme birlikte korunmalıdır.","branch_kind":"non_bare","branch_ref":"root_000709/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","surface_ar":"سَعْيَ"}],"gloss":"aynı uğraşta rakibini yenme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki kişi aynı uğraşta karşılıklı olarak birbirini geçmeye çalışır ve biri sonunda ötekine üstün gelir."}}],"root_ar":"س ع ي","root_id":"root_000709","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşılıklı yarışmayı, ortak uğraş alanını ve sonuçta elde edilen üstünlüğü birlikte korur.","boundary_detail":"Karşılıklı uğraş, aynı etkinlik alanı ve sonuçta rakibe üstün gelme birlikte korunmalıdır.","branch_image_ar":"مغالبة في السعي","concept_gloss":"aynı uğraşta rakibini yenme","contextual_glosses":[{"applicability":"İki kişinin aynı işi veya uğraşı karşılıklı denediği ve birinin ötekinden üstün çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ortak iş, karşılıklı yarışma ve rakibi geçme sonucu korunur."},"facet_ids":["F001"],"text":"aynı işte rakibini geçmek","usage_role":"general"}],"definition":"Birinin aynı uğraşta kendisiyle yarışan kişiyi geride bırakıp ona üstün gelmesidir. Anlam yalnız yarışmaya değil, karşılıklı denemenin konuşan lehine sonuçlanmasına dayanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki kişi aynı uğraşta karşılıklı olarak birbirini geçmeye çalışır ve biri sonunda ötekine üstün gelir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Henüz sonuçlanmamış veya kimsenin üstün gelmediği karşılaşmaları da kapsar.","collision":"Genel yarış adı, belirli karşılıklı yapı ile sonuçlanan üstünlüğü belirsizleştirir.","fit":"displacement","loses":"Konuşanın rakibine gerçekten üstün geldiği sonucu açıkça taşımaz.","preserves":"İki tarafın karşılıklı olarak birbirini geçmeye çalışmasını korur."},"text":"yarış"}],"identity_rationale":"Kaynak ifadesi, iki kişinin aynı uğraşta birbirini geçmeye çalışmasını ve konuşanın rakibine üstün gelmesini anlatan belirli bir karşılıklı yapıyı verir. Genel yarışma veya genel zafer, bu kalıp ve uğraş ilişkisi olmadan dalı tam karşılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"benimle aynı uğraşta yarıştı, ben de onu yendim"}],"lexicalization_note":"Tanım yalnız karşılıklı yarışmayı ve ardından üstün gelmeyi bildiren belirli söz dizisine bağlıdır; yalın köke genellenmez.","neighbor_coverage_note":"Bütün adaylar karşılıklı eylem, tartışma, boy ölçüşme, koşu yarışı, cömertlik yarışı ve genel zafer bakımından değerlendirildi; kalıp, alan ve sonuç sınırını gösteren dört karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Sonuç yapısı aynıdır; odak dal belirli bir uğraşta ilerleme ve çaba alanına, komşu dal ise karşılıklı ele alınan işe bağlıdır.","focus_only":"Üstünlük, aynı uğraşta gösterilen çaba ve ilerleme üzerinden kurulur.","gloss":"uğraşta üstün gelme ile karşılıklı işte üstün gelme","neighbor_only":"Üstünlük, bir şeyi karşılıklı yapma veya ele alma alanında daha genel biçimde kurulabilir.","neighbor_ref":"root_001028/B007","relation_type":"near_synonym","shared_zone":"İki dal da karşılıklı bir etkinlikte rakibi geçip üstün gelmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal uğraş ve çabaya bağlıdır; komşu dal aynı üstün gelme yapısını gelme eyleminin çokluğuna sınırlar.","focus_only":"Yarışın alanı aynı uğraşta çaba gösterme ve ilerlemedir.","gloss":"uğraşta üstün gelme ile gelişte üstün gelme","neighbor_only":"Yarışın alanı tekrar tekrar gelme ve geliş sayısında öne geçmedir.","neighbor_ref":"root_000281/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da karşılıklı yapılan bir eylemde rakibi geride bırakma kalıbını taşır."},{"boundary_match":"partial","distinction":"Odak dal sonucu, yani rakibi geçmeyi bildirir; komşu dal karşılaşma ve boy ölçüşme sürecini sonuçtan bağımsız anlatabilir.","focus_only":"Karşılaşmanın bir tarafın rakibine üstün gelmesiyle sonuçlanması zorunludur.","gloss":"rakibi yenme ile boy ölçüşme","neighbor_only":"Boy ölçüşme, övünme ve yarışma sonucunda açık bir kazanan bulunmadan da gerçekleşebilir.","neighbor_ref":"root_000745/B007","relation_type":"near_neighbor","shared_zone":"İki dalda da kişiler aynı alanda birbirleriyle yarışır ve kendilerini karşılaştırır."},{"boundary_match":"partial","distinction":"Odak dal belirli karşılıklı uğraş kalıbına bağlıdır; komşu dal üstün gelmenin araç ve alanını sınırlamayan genel sonuç adıdır.","focus_only":"Zafer, aynı uğraşta gerçekleşen belirli bir karşılıklı denemenin sonucudur.","gloss":"uğraşta rakibi yenme ile genel zafer","neighbor_only":"Her türlü çatışma veya yarışta elde edilen genel zafer ve egemenlik kapsanır.","neighbor_ref":"root_000965/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir rakibe karşı üstünlük elde edilmesini ve kazanmayı içerir."}],"source_phrase_ar":"ساعانى فلان فسعيته أسعيه إذا غلبته فيه (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, aynı uğraşta karşılıklı yarışmayı ve konuşanın rakibini geçerek üstün gelmesini bildirir."}],"source_summary":"Ortaklaştırılacak çoklu kaynak malzemesi yoktur; kanıt tek ve belirli bir karşılıklı üstün gelme yapısıyla sınırlıdır.","sources":["SI"],"what_is_ar":"يدخل فيه قولهم ساعاني فلان فسعيته إذا غلبته فيه.","what_is_not_ar":"لا يدخل فيه مطلق السباق أو الحركة إلا حيث وردت صيغة المغالبة هذه."},"support_links":[]},{"boundary":"Dalın çekirdeği zamanın sürmesi ve belirli bir zaman kesitidir; gece içindeki gecikme, birim zamana göre işlem ve çetin zaman anlatımları yalnızca kendi yapılarında geçerlidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000760/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","surface_ar":"سَعْيَ"}],"gloss":"zamanın sürmesi ve belirli bir zaman kesiti","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlamın temeli bir şeyin kesintisiz sürmesi ve zaman içinde geçmesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözcük şimdiki zamanı veya gece ile gündüzden belirli bir bölümü gösterir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dünyanın sona erip insanların yeniden dirileceği gün de bu zaman adıyla belirtilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Belirli gece söz öbeklerinde gecenin sakinleşmesinden sonra geçen bir süre anlatılır."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Türemiş kullanımlar bir işlemi veya işçi tutmayı zaman dilimi başına yapmayı anlatır."}},{"facet_id":"F006","role":"associated_use","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Belirli bir niteleme yapısı, yaşanan zaman kesitinin çetin olduğunu bildirir."}}],"root_ar":"س ع ي","root_id":"root_000760","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın sürüp geçme temelini ve zamanın sınırlı bir bölümü olma çekirdeğini birlikte karşılar.","boundary_detail":"Dalın çekirdeği zamanın sürmesi ve belirli bir zaman kesitidir; gece içindeki gecikme, birim zamana göre işlem ve çetin zaman anlatımları yalnızca kendi yapılarında geçerlidir.","branch_image_ar":"مرور الوقت واستمراره","concept_gloss":"zamanın sürmesi ve belirli bir zaman kesiti","contextual_glosses":[{"applicability":"Söz konusu biçim içinde bulunulan zamanı gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Şimdiki zaman kesitine gönderimi eksiksiz korur."},"facet_ids":["F002"],"text":"şimdiki zaman","usage_role":"contextual"},{"applicability":"Sözcük gece veya gündüz içindeki sınırlı bir zaman parçasını belirttiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Zaman parçasının gece veya gündüz içinde sınırlı oluşunu korur."},"facet_ids":["F002"],"text":"gece ya da gündüzden bir bölüm","usage_role":"explanatory"},{"applicability":"Sözcük insanlığın yeniden dirileceği son günü adlandırdığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dünyanın sona ermesi ile yeniden diriliş gününü birlikte korur."},"facet_ids":["F003"],"text":"dünyanın sonu ve diriliş günü","usage_role":"explanatory"},{"applicability":"İşlem veya işçi tutma belirli zaman dilimleri üzerinden yinelendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşlemin belirli zaman dilimleri temelinde yapılmasını korur."},"facet_ids":["F005"],"text":"zaman dilimi başına","usage_role":"contextual"}],"definition":"Bu dal, bir şeyin sürüp geçmesi düşüncesinden hareketle şimdiki zamanı veya gece ile gündüzün belirli bir bölümünü anlatır; ayrıca dünyanın sona erip insanların yeniden dirileceği günü belirtir. Yapıya bağlı kullanımlar gecenin sakinleşmesinden sonraki aralığı, zaman dilimi başına işlem ya da işçi tutmayı ve çetin bir zaman kesitini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlamın temeli bir şeyin kesintisiz sürmesi ve zaman içinde geçmesidir."},{"facet_id":"F002","role":"specialization","statement":"Sözcük şimdiki zamanı veya gece ile gündüzden belirli bir bölümü gösterir."},{"facet_id":"F003","role":"extension","statement":"Dünyanın sona erip insanların yeniden dirileceği gün de bu zaman adıyla belirtilir."},{"facet_id":"F004","role":"associated_use","statement":"Belirli gece söz öbeklerinde gecenin sakinleşmesinden sonra geçen bir süre anlatılır."},{"facet_id":"F005","role":"associated_use","statement":"Türemiş kullanımlar bir işlemi veya işçi tutmayı zaman dilimi başına yapmayı anlatır."},{"facet_id":"F006","role":"associated_use","statement":"Belirli bir niteleme yapısı, yaşanan zaman kesitinin çetin olduğunu bildirir."}],"identity_rationale":"Kaynak ifadesi, bir şeyin sürüp geçmesi temelini zamanın şimdiki kesiti, gece ve gündüzün bir bölümü ve dünyanın sonundaki diriliş günüyle ilişkilendirir. Bu nedenle geçici çerçeve doğrudur; ancak dal yalnızca soyut zaman akışı değildir ve yapıya bağlı zaman, işlem, kiralama ve güçlük kullanımları ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"şimdiki zaman ya da gece ve gündüzden bir bölüm"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"dünyanın sona erip insanların yeniden dirileceği gün"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"zaman bölümleri"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kısacık bir zaman"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"gecenin sakinleşmesinden bir süre sonra"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"gecenin sakinleşmesinden bir süre sonra"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"zaman dilimi başına işlem yapma"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir çalışanı zaman dilimi başına tutmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"çetin bir zaman kesiti"}],"lexicalization_note":"Çıplak zaman anlamları ile belirli söz öbeklerine bağlı anlamlar birlikte bulunduğundan tanım bunları birbirine karıştırmadan ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört komşu son gün, tek seferlik oluş, ardıllık ve bekleme sınırlarını açıklar. Öteki adaylar yalnızca geniş bir zaman alanını paylaşır veya bu dalın diğer bağımsız anlamlarına aittir.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Odak dal olayın gerçekleşeceği günü adlandırır; komşu dal ise o günden önce görülen belirtileri ve hazırlayıcı gelişmeleri anlatır.","focus_only":"Odak dal son günü adlandırır ve ayrıca genel zaman anlamları taşır.","gloss":"son gün ile onun ön belirtileri","neighbor_only":"Komşu dal son günün öncesindeki belirtileri, başlangıçları ve nedenleri anlatır.","neighbor_ref":"root_000788/B002","relation_type":"thematic","shared_zone":"İki dal da dünyanın sonuyla ilgili zaman anlatımında buluşur."},{"boundary_match":"partial","distinction":"Odak dal süreyi veya zaman bölümünü öne çıkarırken komşu dal süreden bağımsız biçimde olayın tek hamlede gerçekleşmesini öne çıkarır.","focus_only":"Odak dal zamanın sürmesini ve sınırlı bir zaman bölümünü içerir.","gloss":"zaman kesiti ile tek seferlik oluş","neighbor_only":"Komşu dal bir olayın tek seferde veya birden gerçekleşmesini içerir.","neighbor_ref":"root_000481/B002","relation_type":"near_neighbor","shared_zone":"İki dal da olayların zamansal biçimini belirginleştirir."},{"boundary_match":"partial","distinction":"Odak dal zamanın kendisinin sürmesine yönelir; komşu dalda ise ayrı öğelerin sırayla birbirini izlemesi kurucu ilişkidir.","focus_only":"Odak dal zamanın sürüp geçmesini ve zaman kesitini anlatır.","gloss":"süreklilik ile ardıllık","neighbor_only":"Komşu dal bir varlığın diğerinin ardından gelmesini veya onun yerini almasını anlatır.","neighbor_ref":"root_001033/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda da zaman içinde devam eden bir düzen vardır."},{"boundary_match":"partial","distinction":"Odak dal zamanın devam edip geçmesini adlandırır; komşu dal ise hareketin ya da işin durmasını ve gecikmesini adlandırır.","focus_only":"Odak dal sürüp geçen zamanı veya onun bir bölümünü bildirir.","gloss":"zamanın geçişi ile bekleme","neighbor_only":"Komşu dal durma, bekleme ve yavaşlamayı bildirir.","neighbor_ref":"root_001339/B002","relation_type":"near_neighbor","shared_zone":"İki dal da sürenin nasıl yaşandığıyla ilgilidir."}],"source_phrase_ar":"استمرار الشيء ومضيه (maqayis)؛ الساعة سميت بذلك (maqayis)؛ الساعة الوقت الحاضر (sihah)؛ الساعة القيامة (ayn;sihah;tahdhib)؛ الساعة جزء من آخر الليل والنهار (tahdhib)؛ جاءنا بعد سوع من الليل وبعد سواع (maqayis;sihah;tahdhib)؛ عاملته مساوعة (maqayis;sihah)؛ ساوعت الأجير إذا استأجرته ساعة بعد ساعة (tahdhib)؛ ساعة سوعاء أي شديدة (sihah)","source_summary":"Kaynakların ortak çizgisi, sürüp geçen zaman temelinden şimdiki zaman ve sınırlı zaman bölümü anlamlarının doğmasıdır. Dünyanın sonundaki diriliş günü, gece içindeki bir aralık, zaman dilimi başına işlem ve çetin bir zaman kullanımları bu çekirdeğin farklı kapsamlarıdır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"الساعة والوقت والجزء من الليل والنهار، وسوع الليل وسواعه، والمعاملة أو الاستئجار ساعة بعد ساعة، والساعة الشديدة، والقيامة من جهة تسميتها ساعة","what_is_not_ar":"اسم الصنم؛ المذي؛ الطين بالتبن؛ إهمال الإبل وذهابها"},"support_links":[]},{"boundary":"Çekirdek, hayvanı gözetimsiz bırakıp başıboş gitmesine yol açmaktır; genel kayıp ve mal savurma anlamları bunun kapsam genişlemeleridir.","branch_kind":"mixed_non_bare","branch_ref":"root_000760/B002","candidate_links":[{"candidate_id":"cand_aa84bba46016ab5a89bd","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","surface_ar":"سَعْيَ"}],"gloss":"gözetimsiz bırakıp başıboş gitmesine yol açma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hayvanlar gözetimsiz bırakılır ve bunun sonucu kendi yönlerine gidip başıboş kalırlar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gözetimsiz bırakma düşüncesi bir şeyi kaybetme veya malı savurma anlamına genişler."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir dişi hayvan nitelemesi, otlakta kendi başına uzaklaşan hayvanı gösterir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Aynı hayvan nitelemesi, yavrusunu yırtıcının yiyebileceği biçimde gözetimsiz bırakan anayı da gösterir."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"İnsan nitelemelerinde malını sürekli savuran ve ziyan eden kişi anlatılır."}}],"root_ar":"س ع ي","root_id":"root_000760","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın gözetimden çıkarılması ile kendi yönüne gitmesi arasındaki çekirdek ilişki için uygundur.","boundary_detail":"Çekirdek, hayvanı gözetimsiz bırakıp başıboş gitmesine yol açmaktır; genel kayıp ve mal savurma anlamları bunun kapsam genişlemeleridir.","branch_image_ar":"الإهمال والذهاب على الوجه","concept_gloss":"gözetimsiz bırakıp başıboş gitmesine yol açma","contextual_glosses":[{"applicability":"Hayvanların gözetimsiz bırakılarak kendi yönlerine gitmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözetimsiz bırakma eylemini ve başıboşluk sonucunu birlikte korur."},"facet_ids":["F001"],"text":"başıboş bırakmak","usage_role":"general"},{"applicability":"Hayvan dışındaki bir şeyin gözetimsizlik yüzünden elden çıkması anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyin elden çıkması sonucunu korur."},"facet_ids":["F002"],"text":"kaybetmek","usage_role":"contextual"},{"applicability":"Bir kişinin malını dikkatsizce tüketip ziyan etmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Malın savurganlıkla elden çıkarılması anlamını korur."},"facet_ids":["F002","F005"],"text":"malı savurmak","usage_role":"contextual"},{"applicability":"Ana hayvan yavrusunu yırtıcı tehlikesine açık biçimde bıraktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ana hayvanı, yavruyu ve gözetimsiz bırakma ilişkisini korur."},"facet_ids":["F004"],"text":"yavrusunu gözetimsiz bırakmak","usage_role":"explanatory"}],"definition":"Bu dal, develeri veya bir dişi hayvanı gözetimsiz bırakıp kendi yönlerine gitmelerine yol açmayı anlatır. Bu çekirdekten bir şeyi kaybetme, malı savurma, otlakta başıboş dolaşma ve bir ana hayvanın yavrusunu yırtıcıya açık biçimde bırakması anlamları gelişir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hayvanlar gözetimsiz bırakılır ve bunun sonucu kendi yönlerine gidip başıboş kalırlar."},{"facet_id":"F002","role":"extension","statement":"Gözetimsiz bırakma düşüncesi bir şeyi kaybetme veya malı savurma anlamına genişler."},{"facet_id":"F003","role":"specialization","statement":"Belirli bir dişi hayvan nitelemesi, otlakta kendi başına uzaklaşan hayvanı gösterir."},{"facet_id":"F004","role":"specialization","statement":"Aynı hayvan nitelemesi, yavrusunu yırtıcının yiyebileceği biçimde gözetimsiz bırakan anayı da gösterir."},{"facet_id":"F005","role":"associated_use","statement":"İnsan nitelemelerinde malını sürekli savuran ve ziyan eden kişi anlatılır."}],"identity_rationale":"Kaynak ifadesi, develeri gözetimsiz bırakınca kendi yönlerine gitmelerini, bir dişi hayvanın otlakta dolaşmasını, yavrusunu terk etmesini ve malı ziyan etmeyi açıkça bir araya getirir. Geçici çerçeve bu çekirdeği doğru yansıtır ve hayvan ile mal arasındaki katılımcı ayrımları koruyarak kullanılabilir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"develeri kendi yönlerine gidecek biçimde gözetimsiz bırakmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bir şeyi kaybetmek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"gözetimsiz kaldığı için kendi yönüne gitmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"başıboş gitmek veya yavrusunu gözetimsiz bırakmak"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kaybolmuş ve gözetimsiz kalmış"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"otlakta kendi başına uzaklaşan dişi deve"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yavrusunu yırtıcıya açık biçimde bırakan dişi deve"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"malını savuran adam"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"malı savuran kişi"}],"lexicalization_note":"Çekirdek eylem ile hayvan, yavru ve malı belirten yapılara bağlı kullanımlar ayrı gösterilir; yapıların özel anlamı çıplak köke yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dört seçim genel kayıp, terk, amaçlı otlatma ve gece yayılmasıyla olan başlıca karışmaları gösterir. Kalan adaylar yalnızca uzak bir senaryoyu paylaşır ya da bu kökün başka bağımsız dallarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda hayvanın bırakılması ve kendi yönüne gitmesi kurucudur; komşu dal ise sebebi veya katılımcısı ne olursa olsun genel kayıp ve yok oluş alanına yayılır.","focus_only":"Odak dal hayvanı gözetimsiz bırakıp başıboş gitmesine yol açmayı çekirdek edinir.","gloss":"başıboş bırakma ile genel kayıp","neighbor_only":"Komşu dal çok çeşitli varlıkların, değerlerin ve emeğin kaybını ya da yok olmasını kapsar.","neighbor_ref":"root_000923/B001","relation_type":"near_neighbor","shared_zone":"İki dal da gözetimsizlik yüzünden bir şeyin elden çıkmasını kapsayabilir."},{"boundary_match":"partial","distinction":"Odak dal hayvanın kendi yönüne gitmesi sonucuyla ve ziyan uzantısıyla sınırlıdır; komşu dal bu sonuçları gerektirmeyen genel bırakma ve terk etme eylemidir.","focus_only":"Odak dal bırakılan hayvanın başıboş gitmesi ile malın ziyanı sonuçlarını öne çıkarır.","gloss":"gözetimsiz bırakma ile genel terk","neighbor_only":"Komşu dal bırakma, kesme ve terk etmeyi canlı veya cansız çok daha geniş bir nesne alanında anlatır.","neighbor_ref":"root_001635/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir varlığı gözetim ve müdahale dışında bırakmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dal denetimsizliği ve ziyan ihtimalini bildirir; komşu dal hayvanın beslenmesi için bilinçli biçimde otlağa salınmasını bildirir.","focus_only":"Odak dalda salma gözetimsizlik ve kayıp riski taşır.","gloss":"başıboş bırakma ile otlatmaya salma","neighbor_only":"Komşu dalda hayvanı otlamaya bırakma amaçlı ve olağan bir yetiştiricilik eylemidir.","neighbor_ref":"root_000764/B003","relation_type":"near_neighbor","shared_zone":"İki dal da hayvanın otlakta serbestçe dolaşmasına yol açabilir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeğinde genel ihmal vardır; komşu dal zaman koşulu olarak geceyi ve sürünün yayılmasını öne çıkarır.","focus_only":"Odak dal gündüz veya gece ayrımı olmadan gözetimsiz bırakmayı ve ziyan uzantısını kapsar.","gloss":"genel başıboşluk ile gece yayılması","neighbor_only":"Komşu dal özellikle sürünün geceleyin çobansız yayılması veya otlamasıdır.","neighbor_ref":"root_001534/B003","relation_type":"near_neighbor","shared_zone":"İki dal da gözetimsiz hayvanların otlakta dağılmasını anlatır."}],"source_phrase_ar":"أسعت الإبل إساعة إذا أهملتها (maqayis;sihah;tahdhib)؛ ساعت فهي تسوع (maqayis;sihah;tahdhib)؛ ضائع سائع (maqayis;sihah;tahdhib)؛ ناقة مسياع تذهب في المرعى (maqayis;sihah;tahdhib)؛ رجل مسياع مضياع للمال (sihah;tahdhib)؛ ناقة مسياع تدع ولدها حتى يأكله السبع (tahdhib)","source_summary":"Kaynakların ortak anlatımı hayvanı gözetimsiz bırakma, hayvanın kendi yönüne gitmesi ve bu ilişkiden doğan kayıp düşüncesidir. Otlakta uzaklaşan dişi hayvan, yavrusunu bırakan ana ve malını savuran kişi bu çekirdeğin özel katılımcılarla kurulmuş görünümleridir.","sources":["MQ","SI","TA"],"what_is_ar":"إهمال الإبل حتى تمضي على وجهها، وذهاب الناقة في المرعى، والضياع والسياع، ومضياع المال","what_is_not_ar":"الساعة والقيامة؛ اسم الصنم؛ المذي؛ الطين بالتبن"},"support_links":["sup_af08b2229429b6768fce"]},{"boundary":"Bu dal genel put kavramını değil, eski anlatılarda geçen belirli bir putun özel adını gösterir.","branch_kind":"non_bare","branch_ref":"root_000760/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","surface_ar":"سَعْيَ"}],"gloss":"eski anlatılarda geçen belirli bir putun özel adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük eski anlatılarda tapınılan belirli bir putun özel adıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aktarımlardan biri, putun ilk topluluktan sonra başka bir topluluğa geçtiğini belirtir."}}],"root_ar":"س ع ي","root_id":"root_000760","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kaynaklarda belirtilen tek putun ad işlevini açıklamak için kullanılır.","boundary_detail":"Bu dal genel put kavramını değil, eski anlatılarda geçen belirli bir putun özel adını gösterir.","branch_image_ar":"اسم الصنم سواع","concept_gloss":"eski anlatılarda geçen belirli bir putun özel adı","contextual_glosses":[{"applicability":"Özel adın hangi tür varlığı gösterdiğinin açıklanması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir putu gösteren özel ad işlevini korur."},"facet_ids":["F001"],"text":"belirli bir putun adı","usage_role":"explanatory"}],"definition":"Eski anlatılarda bir topluluğun tapındığı, daha sonra başka bir topluluğa geçtiği bildirilen belirli bir putun özel adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük eski anlatılarda tapınılan belirli bir putun özel adıdır."},{"facet_id":"F002","role":"source_variant","statement":"Aktarımlardan biri, putun ilk topluluktan sonra başka bir topluluğa geçtiğini belirtir."}],"identity_rationale":"Kaynak ifadesi, sözcüğün eski bir anlatıda tapınılan belirli bir putun özel adı olduğunu ve daha sonra başka bir topluluğa geçtiğini açıkça bildirir. Geçici çerçeve bu ad olma işlevini ve tarihsel aktarımı doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"eski anlatılarda tapınılan belirli bir putun özel adı"}],"lexicalization_note":"Anlam yalnızca belirli bir sözlük biriminin özel ad işlevine bağlıdır ve genel kök anlamı olarak genişletilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler özel ad ile genel put sınıfını, başka put adlarını ve dikili tapınma taşını ayırır. Öteki adaylar tapınma senaryosunu paylaşsa da gönderge sınırını daha fazla keskinleştirmez veya bu kökün başka dallarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bir bireyi özel adla gösterir; komşu dal ise aynı türdeki varlıkların ortak adını ve genel sınıfını verir.","focus_only":"Odak dal tek ve belirli bir putun özel adıdır.","gloss":"özel put adı ile genel put türü","neighbor_only":"Komşu dal putları ve tapınılan taşları genel bir varlık türü olarak adlandırır.","neighbor_ref":"root_001624/B001","relation_type":"near_neighbor","shared_zone":"İki dal da tapınılan insan yapımı varlıklarla ilgilidir."},{"boundary_match":"field_only","distinction":"Adlandırma işlevleri aynıdır, fakat göndergeleri farklı iki puttur; bu nedenle birbirlerinin yerine kullanılamazlar.","focus_only":"Odak dal kaynaklarda belirtilen putun kendine özgü adıdır.","gloss":"iki ayrı put adı","neighbor_only":"Komşu dal başka bir putun kendine özgü adıdır.","neighbor_ref":"root_001634/B005","relation_type":"same_field","shared_zone":"Her iki dal da eski anlatılardaki bir putu özel adla gösterir."},{"boundary_match":"field_only","distinction":"Ortak alan yalnızca putlara ad verme işlevidir; her dal farklı bir bireysel göndergeyi belirttiği için anlam özdeşliği yoktur.","focus_only":"Odak dal bir anlatı çevresindeki belirli putun adıdır.","gloss":"farklı putlara ait özel adlar","neighbor_only":"Komşu dal başka bir topluluğa ait farklı bir putun adıdır.","neighbor_ref":"root_000032/B005","relation_type":"same_field","shared_zone":"İki dal da belirli bir puta verilmiş özel ad niteliğindedir."},{"boundary_match":"field_only","distinction":"Odak dal tek bir putu adlandırır; komşu dal ise işleviyle tanımlanan dikili taş türünü kapsar.","focus_only":"Odak dal belirli bir putun özel adıdır.","gloss":"put adı ile dikili tapınma taşı","neighbor_only":"Komşu dal tapınma veya kesim için dikilmiş taşları ortak adla anlatır.","neighbor_ref":"root_001507/B002","relation_type":"same_field","shared_zone":"İki dal da eski tapınma uygulamalarındaki nesneler alanına girer."}],"source_phrase_ar":"سواع اسم صنم في زمن نوح (ayn;tahdhib)؛ سواع اسم صنم كان لقوم نوح ثم صار لهذيل (sihah)","source_summary":"Kaynaklar sözcüğü eski anlatılarda tapınılan belirli bir putun özel adı olarak ortaklaşa tanımlar. Bir aktarım bu putun daha sonraki bir topluluğa geçtiğini de belirtir.","sources":["AY","SI","TA"],"what_is_ar":"سواع اسم صنم عبد في زمن نوح ثم عبدته الجاهلية أو صار لهذيل","what_is_not_ar":"الساعة والوقت؛ السواع من الليل؛ السواع المذي؛ السياع الطين بالتبن"},"support_links":[]},{"boundary":"Dal, saman katılmış çamur malzemesidir; genel çamur, çamur sıvama eylemi veya kurutulmuş yapı parçası değildir.","branch_kind":"bare","branch_ref":"root_000760/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","surface_ar":"سَعْيَ"}],"gloss":"saman karıştırılmış çamur","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Malzemenin çamur kısmı kurucu öğedir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çamurun içinde saman bulunması bu malzemeyi genel çamurdan ayırır."}}],"root_ar":"س ع ي","root_id":"root_000760","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çamur ile samanın birlikte kurucu olduğu malzemeyi doğrudan karşılar.","boundary_detail":"Dal, saman katılmış çamur malzemesidir; genel çamur, çamur sıvama eylemi veya kurutulmuş yapı parçası değildir.","branch_image_ar":"الطين بالتبن","concept_gloss":"saman karıştırılmış çamur","contextual_glosses":[{"applicability":"Malzemenin kısa ve doğal bir adla anılması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çamuru ve onun saman içermesini birlikte korur."},"facet_ids":["F001","F002"],"text":"samanlı çamur","usage_role":"general"}],"definition":"İçine saman katılmış çamurdur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Malzemenin çamur kısmı kurucu öğedir."},{"facet_id":"F002","role":"specialization","statement":"Çamurun içinde saman bulunması bu malzemeyi genel çamurdan ayırır."}],"identity_rationale":"Kaynak ifadesi sözcüğü doğrudan içinde saman bulunan çamur olarak tanımlar. Geçici çerçeve malzemenin iki kurucu bileşenini de korur ve onu genel çamurdan ya da bu malzemeyle yapılan üründen ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"saman karıştırılmış çamur"}],"lexicalization_note":"Tanım çıplak biçimin saman içeren çamur anlamıyla sınırlıdır ve komşu yapı malzemelerinin özelliklerini içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler genel çamur, biçimlendirilmiş yapı parçası, çamurla kaplama eylemi ve doğal tortuyla sınırı gösterir. Kalan adaylar yalnızca yapı veya toprak alanını paylaşır ya da bu kökün ayrı dallarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel çamurun saman katılmış özel bir türüdür; komşu dal saman bulunmasını gerektirmeyen üst malzeme sınıfıdır.","focus_only":"Odak dalda çamurun saman içermesi zorunludur.","gloss":"samanlı çamur ile genel çamur","neighbor_only":"Komşu dal su ile toprağın karışımından oluşan genel çamur türünü kapsar.","neighbor_ref":"root_000963/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın temel maddesi suyla karışmış topraktır."},{"boundary_match":"partial","distinction":"Odak dal karışımın kendisidir; komşu dal ise biçimlendirme sonucunda elde edilen ve yapı kurmada kullanılan ayrı parçadır.","focus_only":"Odak dal biçim verilmemiş samanlı çamur karışımıdır.","gloss":"çamur karışımı ile yapı parçası","neighbor_only":"Komşu dal çamura biçim verilip kurutularak elde edilen yapı parçasıdır.","neighbor_ref":"root_001342/B003","relation_type":"near_neighbor","shared_zone":"İki dal da çamur kökenli geleneksel yapı malzemelerini anlatır."},{"boundary_match":"thematic_only","distinction":"Odak dal bir maddeyi adlandırır; komşu dal ise bu tür bir maddenin yüzeye uygulanmasıyla gerçekleşen eylemdir.","focus_only":"Odak dal saman içeren çamur malzemesidir.","gloss":"malzeme ile çamurla kaplama","neighbor_only":"Komşu dal bir yüzeyi çamurla kaplama eylemini ve bu işi anlatır.","neighbor_ref":"root_000963/B002","relation_type":"thematic","shared_zone":"Çamur malzemesi iki dalın ortak katılımcısıdır."},{"boundary_match":"field_only","distinction":"Odak dal saman içeren hazırlanmış bir karışımdır; komşu dal ise suda çöken doğal tortu ve balçık niteliğindedir.","focus_only":"Odak dal saman katılmış çamurdur.","gloss":"samanlı çamur ile su tortusu","neighbor_only":"Komşu dal koyu su tortusu, balçık ve bunun toprağa verilmesi anlamlarını taşır.","neighbor_ref":"root_000184/B002","relation_type":"same_field","shared_zone":"İki dal da yoğun toprak ve su karışımları alanındadır."}],"source_phrase_ar":"السياع الطين فيه التبن (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Malzeme, içinde saman bulunan çamur olarak tanımlanır."}],"source_summary":"Tek kaynaklı kanıt, bu malzemeyi içinde saman bulunan çamur olarak sınırlar.","sources":["MQ"],"what_is_ar":"السياع طين فيه تبن","what_is_not_ar":"الساعة؛ إهمال الإبل؛ المذي؛ اسم الصنم"},"support_links":[]},{"boundary":"Çekirdek boşalma sıvısından önce çıkan salgıdır; bu salgıyla ilgilenme buyruğu ayrı bir sözlük birimine bağlı ilişkili kullanımdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000760/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","surface_ar":"سَعْيَ"}],"gloss":"boşalma öncesi salgı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan şey boşalma sıvısından önce çıkan bedensel bir salgıdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir buyruk biçimi, kişiden bu salgıyla ilgilenmesini ister."}}],"root_ar":"س ع ي","root_id":"root_000760","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın bedensel sıvı çekirdeğini doğal ve kısa biçimde karşılar.","boundary_detail":"Çekirdek boşalma sıvısından önce çıkan salgıdır; bu salgıyla ilgilenme buyruğu ayrı bir sözlük birimine bağlı ilişkili kullanımdır.","branch_image_ar":"المذي والسوعاء","concept_gloss":"boşalma öncesi salgı","contextual_glosses":[{"applicability":"Salgının çıkış sırasını açıkça belirtmek gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel salgıyı ve boşalmadan önce çıkmasını eksiksiz korur."},"facet_ids":["F001"],"text":"boşalmadan önce çıkan salgı","usage_role":"explanatory"},{"applicability":"Ayrı sözlük birimi bir kişiye salgıyla ilgilenmesini buyurduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Buyruk kipini ve salgıya yönelen ilgilenme eylemini korur."},"facet_ids":["F002"],"text":"bu salgıyla ilgilen","usage_role":"contextual"}],"definition":"Boşalma sıvısından önce çıkan bedensel salgıyı adlandırır. Ayrı bir buyruk biçiminde kişiden bu salgıyla ilgilenmesi istenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan şey boşalma sıvısından önce çıkan bedensel bir salgıdır."},{"facet_id":"F002","role":"associated_use","statement":"Ayrı bir buyruk biçimi, kişiden bu salgıyla ilgilenmesini ister."}],"identity_rationale":"Kaynak ifadesi iki ad biçimini boşalma sıvısından önce çıkan salgıyla eşleştirir ve ayrı bir buyruk biçimini kişinin bu salgıyla ilgilenmesiyle ilişkilendirir. Geçici çerçeve hem bedensel sıvıyı hem de ona yönelik buyruk kullanımını doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"boşalma öncesi salgı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"boşalmadan önce çıkan salgı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"boşalma öncesi salgıyla ilgilenme buyruğu"}],"lexicalization_note":"Salgıyı adlandıran biçimler ile ona yönelik buyruğu taşıyan ayrı sözlük birimi birbirine karıştırılmadan tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler üreme sıvısı, işeme sonrası sıvı, çeşitli sızıntılar ve arınma işlemiyle olan temel sınırları açıklar. Kalan adaylar yalnızca bedensel sıvı alanını paylaşır veya bu kökün başka bağımsız dallarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal zaman bakımından boşalmadan önce çıkar ve ayrı bir salgıdır; komşu dal ise boşalma olayında çıkan üreme sıvısını adlandırır.","focus_only":"Odak dal boşalma sıvısından önce çıkan ayrı bir salgıdır.","gloss":"boşalma öncesi salgı ile üreme sıvısı","neighbor_only":"Komşu dal boşalma sırasında çıkan üreme sıvısının kendisidir.","neighbor_ref":"root_001492/B009","relation_type":"near_neighbor","shared_zone":"İki dal da erkek üreme sistemiyle ilişkili bedensel sıvıları anlatır."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı koşulu boşalmadan önce çıkmasıdır; komşu dalın ayırıcı koşulu ise işemeden sonra çıkmasıdır.","focus_only":"Odak dal boşalmadan önce çıkan salgıdır.","gloss":"boşalma öncesi salgı ile işeme sonrası sıvı","neighbor_only":"Komşu dal özellikle işemeden sonra çıkan sıvıyı ve başka bedensel durumları kapsar.","neighbor_ref":"root_001637/B001","relation_type":"near_neighbor","shared_zone":"İki dal da üreme organından çıkan, üreme sıvısından farklı bedensel salgıları içerir."},{"boundary_match":"field_only","distinction":"Odak dal kaynağı ve çıkış sırası belirli bir salgıdır; komşu dal çok farklı kaynaklardan sızma ve damlamaları ortak bir alanda toplar.","focus_only":"Odak dal belirli sırada çıkan tek bir insan salgısıdır.","gloss":"belirli salgı ile çeşitli sızıntılar","neighbor_only":"Komşu dal burun, hayvan üreme organı, meme ve bitki gibi farklı kaynaklardan sızan sıvıları kapsar.","neighbor_ref":"root_000520/B005","relation_type":"same_field","shared_zone":"Her iki dal da bedenden veya bir yüzeyden çıkan sıvılar alanındadır."},{"boundary_match":"thematic_only","distinction":"Odak dal öncelikle bir sıvının adıdır; komşu dal ise bir sıvıyı adlandırmaktan çok bedenin veya durumun temiz olduğunun anlaşılmasına yönelik işlemdir.","focus_only":"Odak dal salgının kendisini ve onunla ilgilenme buyruğunu içerir.","gloss":"salgı ile arınma işlemi","neighbor_only":"Komşu dal ilişki öncesi bekleme ve işeme sonrası temizlenme işlemlerini içerir.","neighbor_ref":"root_000099/B005","relation_type":"thematic","shared_zone":"İki dal bedensel sıvılarla bağlantılı bakım ve temizlenme senaryosunda buluşur."}],"source_phrase_ar":"السواعي مأخوذ من السواع وهو المذي وهو السوعاء (tahdhib)؛ السوعاء المذي الذي يخرج قبل النطفة (tahdhib)؛ سع سع إذا أمرته أن يتعهد سوعاءه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"İki biçim boşalma öncesi salgıyı adlandırır; ayrı bir biçim bu salgıyla ilgilenme buyruğudur."}],"source_summary":"Tek kaynaklı kanıt iki ad biçimini boşalma öncesinde çıkan salgı için verir ve ayrı bir buyruk biçimini bu salgıyla ilgilenme isteği olarak açıklar.","sources":["TA"],"what_is_ar":"السواع والسوعاء بمعنى المذي الخارج قبل النطفة، والأمر بتعهد السوعاء","what_is_not_ar":"الساعة؛ سواع الصنم؛ السياع الطين بالتبن؛ إهمال الإبل"},"support_links":[]},{"boundary":"Dal ölüm ya da yok oluş olayını değil, bu sonuca uğramış kimseleri topluca gösterir.","branch_kind":"bare","branch_ref":"root_000760/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","surface_ar":"سَعْيَ"}],"gloss":"ölüp yok olanlar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, ölüm veya yok oluş sonucuna uğramış kimselerden oluşur."}}],"root_ar":"س ع ي","root_id":"root_000760","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölüm veya yok oluş sonucuna uğramış kimseleri topluca karşılar.","boundary_detail":"Dal ölüm ya da yok oluş olayını değil, bu sonuca uğramış kimseleri topluca gösterir.","branch_image_ar":"الهلكى","concept_gloss":"ölüp yok olanlar","contextual_glosses":[{"applicability":"Bağlam yok oluş yerine doğrudan ölümü öne çıkardığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ölüm dışındaki yok oluş yorumunu dışarıda bırakır.","preserves":"Ölüm sonucuna uğramış insan göndergesini korur."},"facet_ids":["F001"],"text":"ölenler","usage_role":"contextual"},{"applicability":"Bağlam kişilerin ortadan kalkması ve geride kalmaması yönünü öne çıkardığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan göndergesini ve yok oluş sonucunu birlikte korur."},"facet_ids":["F001"],"text":"yok olup gidenler","usage_role":"contextual"}],"definition":"Ölüp yok olmuş kimseleri topluca gösteren bir addır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, ölüm veya yok oluş sonucuna uğramış kimselerden oluşur."}],"identity_rationale":"Kısa kaynak ifadesi sözcüğü ölüp yok olmuş kimseleri gösteren bir adla doğrudan eşler. Geçici çerçeve bu insan göndergesini doğru korur ve onu ölüm olayı, öldürme eylemi veya genel yok oluş düşüncesiyle karıştırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"ölüp yok olmuş kimseler"}],"lexicalization_note":"Tanım çıplak biçimin ölüp yok olmuş kimseler anlamıyla sınırlıdır; ilişkili ölüm ve yıkım olayları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler ölen kişiler ile ölüm olayı, yok olma, art arda ölüm ve geniş yıkım alanı arasındaki sınırları gösterir. Kalan adaylar aynı sonucu başka sözcüklerle anlatır veya bu kökün ayrı dallarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal olaydan etkilenen kişileri adlandırır; komşu dal ise kişinin ölmesi sürecini veya gerçekleşen olayı anlatır.","focus_only":"Odak dal ölmüş kimseleri topluca gösterir.","gloss":"ölen kişiler ile ölüm olayı","neighbor_only":"Komşu dal bir kişinin ölmesi veya dünyadan ayrılması olayını anlatır.","neighbor_ref":"root_001186/B002","relation_type":"near_neighbor","shared_zone":"İki dal da insan ölümünün sonucu çevresinde yer alır."},{"boundary_match":"partial","distinction":"Odak dal sonuçtaki insan topluluğuna gönderimde bulunur; komşu dal ise canlı veya cansız bir varlığın yok olmasını olay olarak kurar.","focus_only":"Odak dal ölüm veya yok oluş sonucuna uğramış insanları gösterir.","gloss":"yok olmuş kişiler ile yok olma","neighbor_only":"Komşu dal bir kişinin ya da şeyin yok olması ve zamanın onu yok etmesi eylemini anlatır.","neighbor_ref":"root_001637/B004","relation_type":"near_neighbor","shared_zone":"İki dal ölüm ve yok oluş sonucu bakımından örtüşür."},{"boundary_match":"thematic_only","distinction":"Odak dal kişilerden oluşan sonucu adlandırır; komşu dalda kurucu özellik ölümlerin art arda gerçekleşmesidir.","focus_only":"Odak dal ölenleri tek bir toplu gönderge olarak sunar.","gloss":"ölenler ile art arda ölüm","neighbor_only":"Komşu dal kişilerin birbiri ardınca ölmesini ve olayların sırasını anlatır.","neighbor_ref":"root_000021/B009","relation_type":"thematic","shared_zone":"İki dal birden çok kişinin ölümüyle ilgili olabilir."},{"boundary_match":"field_only","distinction":"Odak dal yalnızca sonuca uğrayan insanları gösterir; komşu dal ise farklı katılımcılara gelebilen geniş bir yıkım ve zarar olayları kümesidir.","focus_only":"Odak dal ölüp yok olmuş kişileri adlandırır.","gloss":"ölmüş kişiler ile yıkıcı olay","neighbor_only":"Komşu dal kişiye veya mala gelen ölüm, ağır dert, kırılma, öldürme ve yıkım olaylarını kapsar.","neighbor_ref":"root_000009/B011","relation_type":"same_field","shared_zone":"Her iki dal ölüm ve yok oluş alanına girer."}],"source_phrase_ar":"الساعة الهلكى (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Sözcük ölüp yok olmuş kimseleri topluca gösterir."}],"source_summary":"Tek kaynaklı kanıt sözcüğü ölüp yok olmuş kimseleri gösteren adla eşler.","sources":["TA"],"what_is_ar":"إطلاق الساعة على الهلكى في نقل ابن الأعرابي","what_is_not_ar":"الساعة بمعنى الوقت والقيامة؛ سواع الصنم؛ المذي؛ الطين بالتبن"},"support_links":[]},{"boundary":"Bu dal dişler arasındaki aralığı veya iki şey arasındaki büyük farkı bildiren kalıplaşmış sözü kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000775/B001","candidate_links":[{"candidate_id":"cand_1b9c6cc07f42b00bc5d6","lane":"micro"},{"candidate_id":"cand_18ee035e8c50b918aa23","lane":"micro"},{"candidate_id":"cand_aa84bba46016ab5a89bd","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَتَّىٰ","morph_features":"STEM|POS:N|LEM:$at~aY`|ROOT:$tt|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:3:2","qac_word_ref":"92:4:3","surface_ar":"شَتَّىٰ"}],"gloss":"dağılma ve dağıtma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir arada bulunan kişilerin veya parçaların birlik düzenini yitirip birbirinden ayrılmasıdır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğu, işi veya bütünü birbirinden ayrı unsurlara dağıtma eylemini de kapsar."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dağılmanın sonucu olarak kişilerin ayrı gruplar halinde gelmesi veya bir işin dağınık durumda bulunması anlatılabilir."}}],"root_ar":"ش ت ت","root_id":"root_000775","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bütünün kendiliğinden çözülmesini ve bir bütünün başkası tarafından dağıtılmasını birlikte temsil eden genel karşılıktır.","boundary_detail":"Bu dal dişler arasındaki aralığı veya iki şey arasındaki büyük farkı bildiren kalıplaşmış sözü kapsamaz.","branch_image_ar":"التفرق والشتات","concept_gloss":"dağılma ve dağıtma","contextual_glosses":[{"applicability":"Bir topluluk veya düzenli bütünün birliğini yitirip ayrı yönlere dağıldığı bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir başkasının dağıtma eylemini doğrudan karşılamaz.","preserves":"Birlik halinin çözülerek dağılmasını güçlü biçimde korur."},"facet_ids":["F001","F003"],"text":"darmadağın olmak","usage_role":"contextual"},{"applicability":"İnsanların tek bir düzenli topluluk halinde değil, birbirinden ayrı kişiler veya gruplar halinde geldiği bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dağılma sürecini ve etkin biçimde dağıtma anlamını dışarıda bırakır.","preserves":"Dağılmış unsurların ayrı gruplar halinde görünmesini korur."},"facet_ids":["F003"],"text":"ayrı ayrı gelmek","usage_role":"contextual"}],"definition":"Bir topluluğun ya da bütünün bir aradalığını yitirerek ayrı kişilere veya parçalara dağılması yahut bir şeyin böyle dağınık hale getirilmesidir. Dağılmış unsurların ayrı ayrı bulunması veya ayrı gruplar halinde gelmesi bu sürecin sonucudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir arada bulunan kişilerin veya parçaların birlik düzenini yitirip birbirinden ayrılmasıdır."},{"facet_id":"F002","role":"core","statement":"Bir topluluğu, işi veya bütünü birbirinden ayrı unsurlara dağıtma eylemini de kapsar."},{"facet_id":"F003","role":"extension","statement":"Dağılmanın sonucu olarak kişilerin ayrı gruplar halinde gelmesi veya bir işin dağınık durumda bulunması anlatılabilir."}],"identity_rationale":"Kaynak ifadesi, bir topluluğun ya da bütünün bir aradalığını yitirip dağılmasını ve bir şeyi dağıtma eylemini ortak çekirdek olarak açıkça verir. Ayrı ayrı gelme ve dağınık durumda bulunma örnekleri de bu çekirdeğin sonuç görünümleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"dağılmak; dağılma"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"dağıtmak, dağınık hale getirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"topluluğum işimi dağıttı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"şu şey gönlümü dağıttı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yayılıp dağılmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"dağılıp yayılmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ayrı kişiler veya dağınık parçalar halinde"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dağınıklık ve ayrılık"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"dağılmış, dağınık"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"dağınık bir iş veya durum"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çeşitli, birbirinden farklı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"aynı soydan olmayan insanlar"}],"lexicalization_note":"Dal hem yalın dağılma ve dağıtma biçimlerini hem de yalnız belirli söz öbeklerinde gerçekleşen kullanımları içerir; söz öbeklerine özgü anlamlar genel çekirdeğe taşınmaz.","neighbor_coverage_note":"On adayın tamamı değerlendirildi. En yakın dağılma, etkin ayırma, çatışmalı bölünme, parça ve karşılaştırmalı ayrılık adayları yayımlandı; yönlere saçılma veya dağınık gruplar gibi kalan adaylar aynı ayrımı tekrarladığı için eklenmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hem geçişsiz dağılmayı hem de dağıtmayı aynı çekirdekte tutar; komşu dal ise etkin ayırma ve dağıtma işlemini, bunun farklı uygulamalarını öne çıkarır.","focus_only":"Odak dal kendiliğinden dağılma durumunu ve dağılmış halde bulunmayı da kapsar.","gloss":"dağılma ile etkin ayırma","neighbor_only":"Komşu dal ayırma işlemini dağıtım, uzaklaştırma ve belirli ilişkileri çözme yönleriyle daha geniş işler.","neighbor_ref":"root_001148/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir topluluğun veya bütünün birliği çözülür ve unsurlar birbirinden ayrılır."},{"boundary_match":"partial","distinction":"Ortak çekirdek güçlüdür; ancak odak dal süreç, ettirme ve dağınık durum arasında dolaşırken komşu dal belirli toplulukların ve parçaların ayrılmasına daha sıkı bağlıdır.","focus_only":"Odak dal bir işi dağıtmayı ve kişilerin ayrı ayrı gelmesini de kapsar.","gloss":"topluluğun dağılması","neighbor_only":"Komşu dal ayrılmış toplulukları ve hayvan gruplarını parça ya da sürü görünümüyle özelleştirir.","neighbor_ref":"root_000850/B005","relation_type":"near_synonym","shared_zone":"İki dal da toplulukların veya parçaların birbirinden ayrılıp dağılmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal ayrılmanın kendisini nötr biçimde bildirir; komşu dal ise bu ayrılığı çatışma ve karşıtlıkla gerekçelendirerek farklı bir çekirdek kurar.","focus_only":"Odak dalda dağılma için anlaşmazlık veya düşmanlık şart değildir.","gloss":"dağılma ile anlaşmazlık","neighbor_only":"Komşu dal topluluğun anlaşmazlık, karşıtlık ve düşmanlık yüzünden bölünmesini gerektirir.","neighbor_ref":"root_000807/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal bir topluluğun birlik halini yitirip ayrılabildiği durumu içerir."},{"boundary_match":"field_only","distinction":"Odak dal ayrılma sürecine ve dağınık sonuca yönelir; komşu dal ise ayrılmış ya da birleşmiş olmasına bakmadan parçanın kendisini kavramlaştırır.","focus_only":"Odak dal bütünün birlik halini yitirip unsurlarının dağılması sürecini anlatır.","gloss":"dağılma ve parça","neighbor_only":"Komşu dal bir bütünü oluşturan parçayı, bölümü veya topluluğu adlandırır.","neighbor_ref":"root_000241/B002","relation_type":"same_field","shared_zone":"İki dal da bütün ile onun ayrılabilir unsurları arasındaki ilişkiyi konu edinir."},{"boundary_match":"partial","distinction":"Odak dal bir çözülme ve dağılma sürecidir; komşu dal ise iki şeyin karşılaştırmalı uzaklığını ya da uyuşmazlığını bildiren sözlü bir yargıdır.","focus_only":"Odak dal çok sayıda unsurun birlikten çıkıp dağılmasını veya dağıtılmasını kapsar.","gloss":"dağılma ve uzak ayrılık","neighbor_only":"Komşu dal iki şey arasındaki büyük uzaklık veya uyuşmazlığı kalıplaşmış bir sözle bildirir.","neighbor_ref":"root_000775/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da önceki veya beklenen bir yakınlık ve birlik ilişkisinin bulunmaması vardır."}],"source_phrase_ar":"أصل يدل على تفرق وتزيل (maqayis)؛ الشت مصدر الشيء الشتيت وهو المتفرق (ayn)؛ شت يشت شتاتا وهو التفرق (jamhara)؛ أمر شت أي متفرق (sihah)؛ يصدر الناس أشتاتا أي متفرقين (tahdhib)؛ الشت تفريق الشعب (mufradat)","source_summary":"Kaynaklar, anlamı birlik halinin çözülmesi, unsurların birbirinden ayrılması ve bir topluluğun dağıtılması çevresinde birleştirir. Ayrı ayrı gelen insanlar ile dağınık bir iş, bu ortak anlamın durum ve sonuç örnekleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه تفرق الجمع والشعب؛ وتفريق الأمر والقوم؛ ومجيء الناس أشتاتا؛ واختلاف الأنواع والقلوب","what_is_not_ar":"ليس ثغرا مفلجا؛ وليس صيغة شتان للمباعدة بين شيئين"},"support_links":["sup_84c4210b369b365a8586","sup_a17bf6be0bbab470b6f2","sup_af08b2229429b6768fce"]},{"boundary":"Anlam yalnız diş dizisini niteleyen kalıplaşmış kullanıma bağlıdır; genel boşluk, dağılma veya uzaklık anlamına genişletilemez.","branch_kind":"collocation","branch_ref":"root_000775/B002","candidate_links":[{"candidate_id":"cand_4679a76eb54d6973f21e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَتَّىٰ","morph_features":"STEM|POS:N|LEM:$at~aY`|ROOT:$tt|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:3:2","qac_word_ref":"92:4:3","surface_ar":"شَتَّىٰ"}],"gloss":"güzel ve aralıklı diş dizisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişler birbirinin üzerine binmez ve aralarında görünür aralıklar bulunur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aralıklı diziliş, dişlerin güzel ve düzgün görünmesini sağlayan olumlu bir nitelik olarak sunulur."}}],"root_ar":"ش ت ت","root_id":"root_000775","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişler arasındaki düzenli açıklığı, üst üste binmeme durumunu ve bunun olumlu görünüşünü birlikte karşılar.","boundary_detail":"Anlam yalnız diş dizisini niteleyen kalıplaşmış kullanıma bağlıdır; genel boşluk, dağılma veya uzaklık anlamına genişletilemez.","branch_image_ar":"الثغر الشتيت","concept_gloss":"güzel ve aralıklı diş dizisi","contextual_glosses":[{"applicability":"Bir kişinin dişlerinin birbirine binmeden aralıklı ve güzel dizildiğini doğal Türkçe ile nitelemek için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişler arasındaki açıklığı, düzenli dizilişi ve beğenilen görünüşü korur."},"facet_ids":["F001","F002"],"text":"seyrek ve düzgün dişli","usage_role":"contextual"}],"definition":"Dişlerin üst üste binmediği, aralarında belirgin ve düzenli aralıkların bulunduğu güzel bir diş dizisini niteleyen kalıplaşmış kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişler birbirinin üzerine binmez ve aralarında görünür aralıklar bulunur."},{"facet_id":"F002","role":"specialization","statement":"Aralıklı diziliş, dişlerin güzel ve düzgün görünmesini sağlayan olumlu bir nitelik olarak sunulur."}],"identity_rationale":"Kaynak ifadesi, nitelemeyi açıkça güzel ve aralıklı bir diş dizisine bağlar. Ek açıklama dişlerin üst üste binmemesini verdiğinden, dalın kimliği genel ayrılma değil yalnız bu görünüş özelliğidir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"dişleri güzel, düzgün ve aralıklı ağız"}],"lexicalization_note":"Dal yalnız diş dizisini niteleyen söz öbeğinde sözlüksel hale gelir; bu kullanımdaki aralılık yalın kökün genel anlamı sayılmaz.","neighbor_coverage_note":"On adayın tamamı değerlendirildi. Diş güzelliği, diş sıralanışı, fiziksel açılma, boşluk bırakma ve genel dağılma ile kurulan en açıklayıcı beş karşıtlık yayımlandı; ağız bölümü ve yüz görünüşüyle yalnız tematik bağ kuran adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırt edici niteliği dişler arasındaki açıklıktır; komşu dalın güzellik alanı daha geniştir ve açıklık bulunmadan da gerçekleşebilir.","focus_only":"Odak dal özellikle dişler arasındaki düzenli açıklığı ve üst üste binmemeyi gerektirir.","gloss":"aralıklı güzel dişler","neighbor_only":"Komşu dal beyazlık, parlaklık, düzgün çıkış ve sıralanma gibi başka beğenilen diş özelliklerini de kapsar.","neighbor_ref":"root_000540/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal güzel ve düzgün görünen diş dizisini niteleyen olumlu kullanımlardır."},{"boundary_match":"field_only","distinction":"Odak dal açıklık ve çakışmama üzerinden, komşu dal ise sıkı sıralanma ve beyaz parlaklık üzerinden güzellik kurar.","focus_only":"Odak dal dişler arasındaki aralıkları olumlu görünüşün temel öğesi yapar.","gloss":"aralık ve inci gibi diziliş","neighbor_only":"Komşu dal dişlerin inci gibi sıralanmasını ve üzerlerindeki beyaz parlaklığı öne çıkarır.","neighbor_ref":"root_000286/B009","relation_type":"same_field","shared_zone":"İki dal da diş dizisinin düzenli ve güzel görünüşünü tasvir eder."},{"boundary_match":"partial","distinction":"Odak dal yalnız diş dizisine ve olumlu estetik yargıya bağlıdır; komşu dal çeşitli beden uçları ve genişlikler için kullanılan genel bir açılma kavramıdır.","focus_only":"Odak dal dişler arasındaki düzenli açıklığı güzel bir görünüş niteliği olarak değerlendirir.","gloss":"diş aralığı ve açılma","neighbor_only":"Komşu dal kol, bacak veya başka uçlar arasındaki fiziksel açılma ve geniş mesafeyi anlatır.","neighbor_ref":"root_000092/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal iki fiziksel unsur arasındaki açıklık ve birbirinden uzak durma görünümünü içerir."},{"boundary_match":"partial","distinction":"Odak dal belirli bir beden bölümündeki görünüş niteliğidir; komşu dal ise nesne ve beden parçaları arasında boşluk bırakmaya ilişkin genel bir ilişkidir.","focus_only":"Odak dal aralığı diş dizisinin kalıcı ve beğenilen bir niteliği olarak sunar.","gloss":"diş aralığı ve boşluk bırakma","neighbor_only":"Komşu dal iki şeyi birbirine değdirmeyip aralarında boşluk bırakma eylemini veya durumunu anlatır.","neighbor_ref":"root_000450/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da yan yana unsurların birbirine bitişmemesi ve arada boşluk bulunması vardır."},{"boundary_match":"partial","distinction":"Odak dalda unsurlar düzenli bir sıra içinde kalır ve ayrılık olumlu bir görünüş niteliğidir; komşu dalda ise birlik düzeni çözülür.","focus_only":"Odak dal dişlerin birbirine binmeden aralıklı dizilmesini ve güzel görünmesini anlatır.","gloss":"aralıklı diziliş ve dağılma","neighbor_only":"Komşu dal toplulukların veya bütünlerin birlik halini yitirip dağılması ya da dağıtılması sürecini anlatır.","neighbor_ref":"root_000775/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda unsurların birbirinden ayrı bulunması biçimsel bir ortaklık oluşturur."}],"source_phrase_ar":"ثغر شتيت مفلج حسن (maqayis)؛ ثغر شتيت مفلج حسن (ayn)؛ ثغر شتيت أي مفلج (sihah)","source_summary":"Kaynaklar, bu kullanımı dişlerin üst üste binmeden aralıklı dizildiği güzel bir ağız görünümü olarak ortaklaşa tanımlar.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه الثغر الشتيت المفلج الحسن؛ وانفراج الأسنان وعدم تراكمها","what_is_not_ar":"ليس شتات القوم ولا اختلاف الأنواع؛ وليس صيغة شتان"},"support_links":["sup_621eb756d39cf4d9bdbe"]},{"boundary":"Dal iki şey hakkında kullanılan kalıplaşmış bildirimle sınırlıdır; her türlü fiziksel uzaklık veya çok unsurlu dağılma bunun kapsamına girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000775/B003","candidate_links":[{"candidate_id":"cand_1b9c6cc07f42b00bc5d6","lane":"micro"},{"candidate_id":"cand_382375fffd93a2d4b8a4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَتَّىٰ","morph_features":"STEM|POS:N|LEM:$at~aY`|ROOT:$tt|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:3:2","qac_word_ref":"92:4:3","surface_ar":"شَتَّىٰ"}],"gloss":"iki şey arasındaki büyük uzaklık ve uyuşmazlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki şey arasındaki uzaklığın veya ayrılığın çok büyük olduğu bildirilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uzaklık, iki şey arasında uyum veya bağ bulunmaması biçiminde soyut bir karşılaştırmayı da kapsar."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yargı, doğrudan iki şeyi karşılaştıran veya aralarındaki mesafeyi konu eden iki kalıplaşmış kuruluşla dile getirilir."}}],"root_ar":"ش ت ت","root_id":"root_000775","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki şeyin gerek mesafe gerek nitelik veya uyum bakımından birbirinden belirgin biçimde ayrı olduğunu bildiren tam açıklayıcı karşılıktır.","boundary_detail":"Dal iki şey hakkında kullanılan kalıplaşmış bildirimle sınırlıdır; her türlü fiziksel uzaklık veya çok unsurlu dağılma bunun kapsamına girmez.","branch_image_ar":"بُعد ما بين الشيئين","concept_gloss":"iki şey arasındaki büyük uzaklık ve uyuşmazlık","contextual_glosses":[{"applicability":"İki kişi, görüş veya durum arasındaki büyük nitelik farkını etkili ve doğal bir karşılaştırmayla belirtmek için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğrudan fiziksel mesafe okumasını geri plana iter.","preserves":"İki şey arasındaki farkın çok büyük olduğunu ve yakın bir uyum bulunmadığını korur."},"facet_ids":["F001","F002"],"text":"aralarında dağlar kadar fark var","usage_role":"contextual"},{"applicability":"İki şey arasındaki fiziksel veya soyut uzaklığın güçlü bir yargıyla bildirildiği cümlelerde kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uyumsuzluk ve nitelik farkı yorumunu tek başına zorunlu kılmaz.","preserves":"Karşılaştırılan iki şey arasındaki büyük uzaklığı güçlü biçimde bildirir."},"facet_ids":["F001","F003"],"text":"birbirlerinden ne kadar uzaklar","usage_role":"contextual"}],"definition":"İki şeyin birbirinden çok uzak, belirgin biçimde farklı veya birbiriyle uyuşmaz olduğunu bildiren kalıplaşmış bir sözdür. Bir yakınlığın ya da uyum bağının bulunmadığını karşılaştırmalı ve güçlü bir yargıyla belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki şey arasındaki uzaklığın veya ayrılığın çok büyük olduğu bildirilir."},{"facet_id":"F002","role":"extension","statement":"Uzaklık, iki şey arasında uyum veya bağ bulunmaması biçiminde soyut bir karşılaştırmayı da kapsar."},{"facet_id":"F003","role":"source_variant","statement":"Yargı, doğrudan iki şeyi karşılaştıran veya aralarındaki mesafeyi konu eden iki kalıplaşmış kuruluşla dile getirilir."}],"identity_rationale":"Kaynak ifadesi iki kalıplaşmış kuruluşla iki şey arasındaki uzaklığın arttığını ve uyum bağının kalktığını bildirmeyi ortak anlam olarak verir. Bu nedenle dal, genel dağılmadan ayrı bir karşılaştırmalı uzaklık ve uyuşmazlık yargısıdır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"ne kadar uzak ve farklılar"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ikisi birbirinden ne kadar uzak ve farklı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"aralarında ne büyük uzaklık ve ayrılık var"}],"lexicalization_note":"Dal tek başına kullanılan kalıplaşmış bildirim birimi ile ona bağlı iki söz öbeğini içerir; söz öbeklerinin kuruluş farkı ortak karşılaştırma anlamını değiştirmez.","neighbor_coverage_note":"On adayın tamamı değerlendirildi. Anlamsal fark, genel uzaklık, uzaklaşma ve karşıt yakınlık eksenlerini en iyi açıklayan beş aday yayımlandı; yolculuk mesafesi, geniş yarık ve nicelik derecesi gibi daha özel adaylar aynı sınırı keskinleştirmediği için eklenmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kalıplaşmış bir karşılaştırma yargısı ve uyum yokluğu taşır; komşu dal ise nitelikler arasındaki eşitsizliği veya kusuru yargı kalıbına bağlı olmadan belirtir.","focus_only":"Odak dal iki şey arasındaki büyük ayrılığı kalıplaşmış ve güçlü bir bildirimle sunar.","gloss":"büyük fark ve nitelik eşitsizliği","neighbor_only":"Komşu dal iki şeyin niteliklerindeki eşitsizlik, düzensizlik veya kusuru da genel anlam alanına alır.","neighbor_ref":"root_001183/B002","relation_type":"near_synonym","shared_zone":"Her iki dal iki şey arasındaki uzaklığı ve belirgin nitelik farkını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal iki karşılaştırma öğesi ve kalıplaşmış bir bildirim gerektirir; komşu dal ise karşılaştırma kalıbı olmadan genel fiziksel veya soyut uzaklığı anlatır.","focus_only":"Odak dal daima iki şey arasında güçlü bir karşılaştırma yapar ve soyut uyuşmazlığı da kapsar.","gloss":"karşılaştırmalı ve genel uzaklık","neighbor_only":"Komşu dal tek bir şeyin uzak yerde bulunmasını, uzaklaşmasını veya yakın olmamasını genel biçimde anlatabilir.","neighbor_ref":"root_000131/B001","relation_type":"near_neighbor","shared_zone":"İki dal da şeylerin birbirine yakın olmaması ve aralarında mesafe bulunması alanında kesişir."},{"boundary_match":"partial","distinction":"Odak dal karşılaştırmalı bir yargıdır ve ettirgen hareket bildirmez; komşu dal ise uzaklaşma ile uzaklaştırma süreçlerini de kavramın merkezine alır.","focus_only":"Odak dal iki şeyin zaten uzak veya uyuşmaz olduğunu güçlü bir karşılaştırmayla bildirir.","gloss":"büyük ayrılık ve uzaklaşma","neighbor_only":"Komşu dal bir şeyin uzaklaşması, uzaklaştırılması veya uzak bir yerde bulunması sürecini de kapsar.","neighbor_ref":"root_001463/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal uzak olma ve birbirinden ayrı bulunma durumunu ifade edebilir."},{"boundary_match":"opposed","distinction":"Odak dal eksenin uzaklık ve ayrılık ucundadır; komşu dal aynı eksenin yakınlık ve yaklaşma ucundadır.","focus_only":"Odak dal iki şey arasındaki büyük uzaklığı veya uyuşmazlığı bildirir.","gloss":"uzaklık ve yakınlık","neighbor_only":"Komşu dal bir kişinin ya da şeyin yaklaşmasını ve yakın konuma gelmesini bildirir.","neighbor_ref":"root_001267/B006","relation_type":"polarity_pair","shared_zone":"İki dal ortak mesafe ekseninde öğelerin birbirine göre konumunu değerlendirir."},{"boundary_match":"opposed","distinction":"Odak dal karşılaştırmayı büyük ayrılık yönünde kurar; komşu dal ise görece yakınlık veya bir sınıra erişememe yönünde kurar.","focus_only":"Odak dal iki şey arasındaki belirgin uzaklığı ve uyuşmazlığı güçlü biçimde öne çıkarır.","gloss":"büyük uzaklık ve görece yakınlık","neighbor_only":"Komşu dal bir şeyin başkasına göre daha yakın olmasını, fakat son sınıra erişmemesini de kapsar.","neighbor_ref":"root_000502/B001","relation_type":"polarity_pair","shared_zone":"Her iki dal iki öğeyi konum veya derece bakımından karşılaştırabilir."}],"source_phrase_ar":"شتان ما هما (maqayis;ayn;sihah;tahdhib;mufradat)؛ شتان ما بينهما (maqayis;sihah;mufradat)؛ تباعد ما بينهما (tahdhib)؛ ارتفاع الالتئام بينهما (mufradat)","source_summary":"Kaynaklar, iki şeyin birbirinden uzaklığını ve aralarındaki uyumun kalkmasını güçlü bir karşılaştırma yargısıyla bildirme konusunda birleşir. Doğrudan iki şeyi karşılaştıran kuruluş ile aralarındaki mesafeyi konu eden kuruluş aynı ortak anlama bağlanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه شتان ما هما؛ وشتان ما بينهما؛ والإخبار عن تباعد الشيئين وارتفاع الالتئام بينهما","what_is_not_ar":"ليس تفرق جماعة ولا ثغرا شتيتا"},"support_links":["sup_a17bf6be0bbab470b6f2","sup_f39832ef1db403a51296"]}],"candidate_inventory":[{"anchor_refs":["92:4:1"],"branch_refs":[],"candidate_id":"cand_878c48e1db6eadfa709e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:4:1:direct-address-turn","source_type":"word_analysis","support_ids":["sup_1c87bffeaef3246bc905","sup_8c39a87f8b688cb68833"],"title":"oath register turns toward the audience","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:1","qac_refs":["92:4:1:1"],"status":"accepted"}},{"anchor_refs":["92:4:1"],"branch_refs":[],"candidate_id":"cand_51ffa0e6a74a92c32819","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:4:1:double-emphasis-frame","source_type":"word_analysis","support_ids":["sup_08f6438740e058697162","sup_8c39a87f8b688cb68833"],"title":"double emphasis around the claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:1","qac_refs":["92:4:1:1"],"status":"accepted"}},{"anchor_refs":["92:4:1"],"branch_refs":[],"candidate_id":"cand_a270f2c1d128cdcf609c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:4:1:governed-emphatic-oath-answer","source_type":"word_analysis","support_ids":["sup_32d274f1889577c349f4","sup_8c39a87f8b688cb68833"],"title":"governed oath-answer assertion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:1","qac_refs":["92:4:1:1"],"status":"accepted"}},{"anchor_refs":["92:4:1"],"branch_refs":[],"candidate_id":"cand_b8932b4700ec8ad41289","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:4:1:rootless-particle-form-pressure","source_type":"word_analysis","support_ids":["sup_08f7e912bd5f84e4eb68","sup_8c39a87f8b688cb68833"],"title":"rootless form with audible force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:1","qac_refs":["92:4:1:1"],"status":"accepted"}},{"anchor_refs":["92:4:1"],"branch_refs":[],"candidate_id":"cand_c7bf12aebb8062256262","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:4:1:sound-binding-opening","source_type":"word_analysis","support_ids":["sup_45acda6d4c0c3c8896fb","sup_8c39a87f8b688cb68833"],"title":"nasal opening binds into the subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:1","qac_refs":["92:4:1:1"],"status":"accepted"}},{"anchor_refs":["92:4:2"],"branch_refs":[],"candidate_id":"cand_256790c01e922ea9e65b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000709","root_000760"],"scope":"focus_ayah","source_local_id":"92:4:2:boundary-pivot-to-human-action","source_type":"word_analysis","support_ids":["sup_100536fd1e8d4cef2cd9","sup_33db8d6ccbd2024c5fdc"],"title":"created signs pivot into human action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:2","qac_refs":["92:4:2:1","92:4:2:2"],"status":"accepted"}},{"anchor_refs":["92:4:2"],"branch_refs":[],"candidate_id":"cand_bfe55a9161ca7aa06385","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000709","root_000760"],"scope":"focus_ayah","source_local_id":"92:4:2:bracketed-center-of-assertion","source_type":"word_analysis","support_ids":["sup_0b64e8e026039cabeeb3","sup_33db8d6ccbd2024c5fdc"],"title":"human effort bracketed by emphasis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:2","qac_refs":["92:4:2:1","92:4:2:2"],"status":"accepted"}},{"anchor_refs":["92:4:2"],"branch_refs":[],"candidate_id":"cand_0bca6b9f19a524bf8b0b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000709","root_000760"],"scope":"focus_ayah","source_local_id":"92:4:2:governed-owned-striving","source_type":"word_analysis","support_ids":["sup_33db8d6ccbd2024c5fdc","sup_60f0458c94e16af4f831"],"title":"owned striving under emphatic governance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:2","qac_refs":["92:4:2:1","92:4:2:2"],"status":"accepted"}},{"anchor_refs":["92:4:2"],"branch_refs":[],"candidate_id":"cand_27259d454fc395ac854e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000709","root_000760"],"scope":"focus_ayah","source_local_id":"92:4:2:possessive-ending-audible-address","source_type":"word_analysis","support_ids":["sup_33db8d6ccbd2024c5fdc","sup_7fc5eb2fa7262b17c2a9"],"title":"suffix makes the collective audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:2","qac_refs":["92:4:2:1","92:4:2:2"],"status":"accepted"}},{"anchor_refs":["92:4:2"],"branch_refs":[],"candidate_id":"cand_76aea66ea85e3f7a7165","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000709","root_000760"],"scope":"focus_ayah","source_local_id":"92:4:2:purposeful-effort-range","source_type":"word_analysis","support_ids":["sup_05636b92b38ceede1d76","sup_33db8d6ccbd2024c5fdc"],"title":"movement, work, and endeavor in one noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:2","qac_refs":["92:4:2:1","92:4:2:2"],"status":"accepted"}},{"anchor_refs":["92:4:2"],"branch_refs":[],"candidate_id":"cand_65520e87e32341cc4cf9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000709","root_000760"],"scope":"focus_ayah","source_local_id":"92:4:2:singular-collective-masdar","source_type":"word_analysis","support_ids":["sup_33db8d6ccbd2024c5fdc","sup_c8d7e2881bdc10d30689"],"title":"one category holding many efforts","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:2","qac_refs":["92:4:2:1","92:4:2:2"],"status":"accepted"}},{"anchor_refs":["92:4:2"],"branch_refs":[],"candidate_id":"cand_8d35ceed6c51dee07660","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000709","root_000760"],"scope":"focus_ayah","source_local_id":"92:4:2:sound-and-semantic-tension","source_type":"word_analysis","support_ids":["sup_33db8d6ccbd2024c5fdc","sup_e14c7c9833742f53a46e"],"title":"directed sound beside scattered outcome","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:2","qac_refs":["92:4:2:1","92:4:2:2"],"status":"accepted"}},{"anchor_refs":["92:4:2"],"branch_refs":[],"candidate_id":"cand_ecddc743913905299555","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000709","root_000760"],"scope":"focus_ayah","source_local_id":"92:4:2:subjective-idafa-selected","source_type":"word_analysis","support_ids":["sup_33db8d6ccbd2024c5fdc","sup_b93dcb7d68921145b99d"],"title":"subjective possession over objective pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:2","qac_refs":["92:4:2:1","92:4:2:2"],"status":"accepted"}},{"anchor_refs":["92:4:2"],"branch_refs":[],"candidate_id":"cand_aea27b00c08f71c85d25","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000709","root_000760"],"scope":"focus_ayah","source_local_id":"92:4:2:surah-sorting-domain","source_type":"word_analysis","support_ids":["sup_33db8d6ccbd2024c5fdc","sup_c61b6ba76419184fd20a"],"title":"domain prepared for the next sorting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:2","qac_refs":["92:4:2:1","92:4:2:2"],"status":"accepted"}},{"anchor_refs":["92:4:3"],"branch_refs":[],"candidate_id":"cand_8f2b622b770ee847b2bf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:4:3:double-emphasis-completion","source_type":"word_analysis","support_ids":["sup_9201ee2d6d2700d0a9e7","sup_fa0d0dc394d189d76a3b"],"title":"completion of inna...la emphasis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:3","qac_refs":["92:4:3:1"],"status":"accepted"}},{"anchor_refs":["92:4:3"],"branch_refs":[],"candidate_id":"cand_1c5da713816f76bead15","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:4:3:hinge-and-final-beat","source_type":"word_analysis","support_ids":["sup_240b52abcfaef9f1f42d","sup_9201ee2d6d2700d0a9e7"],"title":"hinge before the compact landing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:3","qac_refs":["92:4:3:1"],"status":"accepted"}},{"anchor_refs":["92:4:3"],"branch_refs":[],"candidate_id":"cand_2b32bcddb6304ded3960","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:4:3:minimal-form-large-function","source_type":"word_analysis","support_ids":["sup_081fbc93567a53f165b1","sup_9201ee2d6d2700d0a9e7"],"title":"single letter with clause-level force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:3","qac_refs":["92:4:3:1"],"status":"accepted"}},{"anchor_refs":["92:4:3"],"branch_refs":[],"candidate_id":"cand_8b8409c514e393bb3f55","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:4:3:predicate-emphatic-lam","source_type":"word_analysis","support_ids":["sup_7feffb6ecf4f468bdd62","sup_9201ee2d6d2700d0a9e7"],"title":"predicate lām, not preposition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:3","qac_refs":["92:4:3:1"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_a3e537de80c0274e0d63","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:directed-dispersion-paradox","source_type":"word_analysis","support_ids":["sup_17d4ae2029eb48ff5669","sup_a88ae66382aaea2876de"],"title":"directed striving becomes non-convergent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_4ebb237c7613df28511d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:final-predicate-completion","source_type":"word_analysis","support_ids":["sup_17d4ae2029eb48ff5669","sup_19fca3dd8dbb70caeae0"],"title":"final predicate carries the thesis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_4e1406a628cc5a09ed6e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:immediate-two-path-sorting","source_type":"word_analysis","support_ids":["sup_17d4ae2029eb48ff5669","sup_25b694e2b860db1693a5"],"title":"diverse field immediately sorted","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_c2922ac09c6433a43ba1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:intertext-natural-diversity","source_type":"word_analysis","support_ids":["sup_17d4ae2029eb48ff5669","sup_4cc9f81b86baaa17fff5"],"title":"same-word natural diversity kept as contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_c9532d8600213651cf69","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:oath-binaries-to-many-paths","source_type":"word_analysis","support_ids":["sup_17d4ae2029eb48ff5669","sup_4bc38bd36d94120e1db7"],"title":"binary oaths become many-path thesis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_f5e96035d45004076e99","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:plural-predicate-over-singular-masdar","source_type":"word_analysis","support_ids":["sup_17d4ae2029eb48ff5669","sup_322a3ac1e29f2f8f222a"],"title":"singular effort made pluralized","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_f84fec387cfec075891a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:predicate-state-not-causative-agent","source_type":"word_analysis","support_ids":["sup_17d4ae2029eb48ff5669","sup_799bf0ce4829e931d3e6"],"title":"state of divergence, not caused scattering","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_c3b6fbce8ab569e767d9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:qualitative-classification","source_type":"word_analysis","support_ids":["sup_17d4ae2029eb48ff5669","sup_bd3c69a2f9f4ea345af0"],"title":"qualitative classification of striving","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_b35391d1ed422c4c9e75","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:rare-or-short-distribution-emphasized","source_type":"word_analysis","support_ids":["sup_17d4ae2029eb48ff5669","sup_9c72d52ff3fa502977d0"],"title":"marked predicate under maximum emphasis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_f4a09a49eb082ec9bce5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:scattered-diverse-not-mild-variety","source_type":"word_analysis","support_ids":["sup_17d4ae2029eb48ff5669","sup_84690af7f0312d6ef767"],"title":"diversity with separation pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_83777f3e50b325da50be","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:scene-shift-created-to-human-plurality","source_type":"word_analysis","support_ids":["sup_17d4ae2029eb48ff5669","sup_1bccf4a7d818edd1dce2"],"title":"created differentiation becomes human plurality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_7e51ce6a6b34791e84db","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:seasonal-and-social-images-narrowed","source_type":"word_analysis","support_ids":["sup_17d4ae2029eb48ff5669","sup_42a91c52e81862e2f145"],"title":"social dispersion kept, seasonal image restrained","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_198605524dbdbf5bef43","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:second-beat-maxim","source_type":"word_analysis","support_ids":["sup_17d4ae2029eb48ff5669","sup_59505a6a9a18c9fc1ca2"],"title":"compact second beat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_ca95701f1fa077654cda","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:sound-of-fracture-and-release","source_type":"word_analysis","support_ids":["sup_170213c3fcfeb85fd20a","sup_17d4ae2029eb48ff5669"],"title":"doubled stop and open ending","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4:2"],"branch_refs":[],"candidate_id":"cand_3d5a6c567a9d6eee5a10","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000709","root_000760"],"scope":"focus_ayah","source_local_id":"92:4:2:1","source_type":"qac_morpheme","support_ids":["sup_3f054498c27bb0d7a6f9"],"title":"QAC root occurrence: س ع ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:4:3"],"branch_refs":[],"candidate_id":"cand_b3d9b2ac5d06881964f4","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:3:2","source_type":"qac_morpheme","support_ids":["sup_abf79322c98eba97bac6"],"title":"QAC root occurrence: ش ت ت","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:4:2"],"branch_refs":[],"candidate_id":"cand_8e7badd426b4da943a0e","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000709","root_000760"],"scope":"focus_ayah","source_local_id":"92:4:2:cooccurrence-background-no-local-payoff","source_type":"word_analysis","support_ids":["sup_33db8d6ccbd2024c5fdc","sup_6d871966cdb6f14f2656"],"title":"co-occurrence background without local payoff","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:2","qac_refs":["92:4:2:1","92:4:2:2"],"status":"accepted"}},{"anchor_refs":["92:4:4"],"branch_refs":[],"candidate_id":"cand_04c7a7e7793501099695","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000775"],"scope":"focus_ayah","source_local_id":"92:4:4:cooccurrence-background-no-local-payoff","source_type":"word_analysis","support_ids":["sup_17d4ae2029eb48ff5669","sup_67a1b73c92b77df0ee83"],"title":"co-occurrence note without distinct local payoff","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:4:4","qac_refs":["92:4:3:2"],"status":"accepted"}},{"anchor_refs":["92:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:4","branch_refs":["root_000709/B001","root_000775/B001","root_000775/B003"],"candidate_id":"cand_1b9c6cc07f42b00bc5d6","commentary_obligation":"review","hft_ref":"hft_800f593d664d46296f28","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_directed_divergence","source_type":"hft","support_ids":["sup_a17bf6be0bbab470b6f2"],"title":"baseline_directed_divergence","trust":"legacy_unbound"},{"anchor_refs":["92:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:4","branch_refs":["root_000709/B002","root_000709/B003","root_000709/B006","root_000775/B001"],"candidate_id":"cand_18ee035e8c50b918aa23","commentary_obligation":"review","hft_ref":"hft_b71511d1c9cac397fe60","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_social_economies","source_type":"hft","support_ids":["sup_84c4210b369b365a8586"],"title":"baseline_social_economies","trust":"legacy_unbound"},{"anchor_refs":["92:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:4","branch_refs":["root_000709/B005","root_000709/B007","root_000775/B003"],"candidate_id":"cand_382375fffd93a2d4b8a4","commentary_obligation":"review","hft_ref":"hft_1f3dacfd911b6ae38286","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_agency_polarity","source_type":"hft","support_ids":["sup_f39832ef1db403a51296"],"title":"baseline_agency_polarity","trust":"legacy_unbound"},{"anchor_refs":["92:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:4","branch_refs":["root_000709/B001","root_000760/B002","root_000775/B001"],"candidate_id":"cand_aa84bba46016ab5a89bd","commentary_obligation":"review","hft_ref":"hft_bfc76349f701d3dba1a0","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_aim_and_drift","source_type":"hft","support_ids":["sup_af08b2229429b6768fce"],"title":"baseline_aim_and_drift","trust":"legacy_unbound"},{"anchor_refs":["92:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:4","branch_refs":["root_000709/B002","root_000775/B002"],"candidate_id":"cand_4679a76eb54d6973f21e","commentary_obligation":"review","hft_ref":"hft_54bfbe4ed191dd4a8efd","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_constructive_spacing","source_type":"hft","support_ids":["sup_621eb756d39cf4d9bdbe"],"title":"baseline_constructive_spacing","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"إِنَّ سَعْيَكُمْ لَشَتَّىٰ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"92:4:1:1","qac_word_ref":"92:4:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","root_ar":"س ع ي","surface_ar":"سَعْيَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"92:4:2:2","qac_word_ref":"92:4:2","root_ar":"","surface_ar":"كُمْ"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"92:4:3:1","qac_word_ref":"92:4:3","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"شَتَّىٰ","morph_features":"STEM|POS:N|LEM:$at~aY`|ROOT:$tt|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:3:2","qac_word_ref":"92:4:3","root_ar":"ش ت ت","surface_ar":"شَتَّىٰ"}],"word_analysis_qac_refs":[["92:4:1:1"],["92:4:2:1","92:4:2:2"],["92:4:3:1"],["92:4:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["92:4:1","92:4:2","92:4:3","92:4:4"]},"focus_surface_evidence":{"arabic_uthmani":"إِنَّ سَعْيَكُمْ لَشَتَّىٰ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"92:4:1:1","qac_word_ref":"92:4:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"سَعْي","morph_features":"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:2:1","qac_word_ref":"92:4:2","root_ar":"س ع ي","surface_ar":"سَعْيَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"92:4:2:2","qac_word_ref":"92:4:2","root_ar":"","surface_ar":"كُمْ"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"92:4:3:1","qac_word_ref":"92:4:3","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"شَتَّىٰ","morph_features":"STEM|POS:N|LEM:$at~aY`|ROOT:$tt|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:4:3:2","qac_word_ref":"92:4:3","root_ar":"ش ت ت","surface_ar":"شَتَّىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["92:4:1:1"],["92:4:2:1","92:4:2:2"],["92:4:3:1"],["92:4:3:2"]],"word_analysis_refs":["92:4:1","92:4:2","92:4:3","92:4:4"],"word_rows":[{"analysis_record_ref":"92:4:1","analytic_gloss_range_en":"emphatic annulling particle governing the clause; not a lexical noun or verb","analytic_root_gloss_range_en":null,"qac_refs":["92:4:1:1"],"root":{},"surface":{"arabic":"إِنَّ","transliteration":"inna"}},{"analysis_record_ref":"92:4:2","analytic_gloss_range_en":"your striving, active effort, or purposeful exertion; locally the addressees' own endeavor rather than striving directed toward them","analytic_root_gloss_range_en":"broad range of purposeful going, work, earning, and active endeavor; technical office, tale-bearing, manumission earning, and specialized illicit branches remain inactive here","qac_refs":["92:4:2:1","92:4:2:2"],"root":{"arabic":"س ع ي","transliteration":"s-ayn-y"},"surface":{"arabic":"سَعْيَكُمْ","transliteration":"sa'yakum"}},{"analysis_record_ref":"92:4:3","analytic_gloss_range_en":"emphatic predicate lām; not the preposition for, to, or belonging to","analytic_root_gloss_range_en":null,"qac_refs":["92:4:3:1"],"root":{},"surface":{"arabic":"لَ","transliteration":"la"}},{"analysis_record_ref":"92:4:4","analytic_gloss_range_en":"diverse, scattered, divergent, or non-convergent as a predicate state; not an active causative scattering verb","analytic_root_gloss_range_en":"accepted local branch centers on scattering and separation; gapped-teeth and distance-formula branches remain lexical background, and seasonal imagery is not locally activated","qac_refs":["92:4:3:2"],"root":{"arabic":"ش ت ت","transliteration":"sh-t-t"},"surface":{"arabic":"شَتَّىٰ","transliteration":"shattā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["92:4"],"branch_refs":["root_000709/B001","root_000775/B001","root_000775/B003"],"candidate_id":"cand_1b9c6cc07f42b00bc5d6","evidence_scope":"focus_ayah","hft_ref":"hft_800f593d664d46296f28","item_id":"baseline_directed_divergence","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_directed_divergence","support_id":"sup_a17bf6be0bbab470b6f2"},{"anchor_refs":["92:4"],"branch_refs":["root_000709/B002","root_000709/B003","root_000709/B006","root_000775/B001"],"candidate_id":"cand_18ee035e8c50b918aa23","evidence_scope":"focus_ayah","hft_ref":"hft_b71511d1c9cac397fe60","item_id":"baseline_social_economies","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_social_economies","support_id":"sup_84c4210b369b365a8586"},{"anchor_refs":["92:4"],"branch_refs":["root_000709/B005","root_000709/B007","root_000775/B003"],"candidate_id":"cand_382375fffd93a2d4b8a4","evidence_scope":"focus_ayah","hft_ref":"hft_1f3dacfd911b6ae38286","item_id":"baseline_agency_polarity","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_agency_polarity","support_id":"sup_f39832ef1db403a51296"},{"anchor_refs":["92:4"],"branch_refs":["root_000709/B001","root_000760/B002","root_000775/B001"],"candidate_id":"cand_aa84bba46016ab5a89bd","evidence_scope":"focus_ayah","hft_ref":"hft_bfc76349f701d3dba1a0","item_id":"baseline_aim_and_drift","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_aim_and_drift","support_id":"sup_af08b2229429b6768fce"},{"anchor_refs":["92:4"],"branch_refs":["root_000709/B002","root_000775/B002"],"candidate_id":"cand_4679a76eb54d6973f21e","evidence_scope":"focus_ayah","hft_ref":"hft_54bfbe4ed191dd4a8efd","item_id":"baseline_constructive_spacing","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_constructive_spacing","support_id":"sup_621eb756d39cf4d9bdbe"}],"diagnostics":[],"lane_counts":{"global":20,"macro":7,"micro":5},"packet_summary":{"ayah_count":21,"focus_ref":"92:4","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ج ز ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000244","furuq_root_norm":"ج ز ي","furuq_source_root_norm":"ج ز ي","is_dominant":true,"target_occurrences":97,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000242","furuq_root_norm":"ج ز ز","furuq_source_root_norm":"ج ز ز","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11","92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"92:4","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":21,"unstructured_record_count":0},"identity":{"ayah_ref":"92:4","lane":"micro","linguistic_source_ref":"92:4","surface_ref":"92:4","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"92:4","target_tokens":[["Çabanız",["92:4:2"]],["elbette",["92:4:1","92:4:3"]],["çeşit",["92:4:3"]],["çeşittir",["92:4:3"]]],"text":"Çabanız elbette çeşit çeşittir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s092-p01-001-011","label":"Contrasting forms of striving","number":1,"refs":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:2:purposeful-effort-range","source_type":"word_analysis","support_id":"sup_05636b92b38ceede1d76","text":"{\"blocking_evidence\":null,\"headline\":\"movement, work, and endeavor in one noun\",\"reader_payoff\":\"The reader notices that the ayah speaks about directed human exertion broadly, not only inward intention or ritual devotion.\",\"reason\":\"V4 accepts purposeful going and active work/earning branches for {{ar:س ع ي}} ({{tr:s-ayn-y}}), but the local maṣdar with possessive suffix does not activate technical agent, denunciation, manumission, or specialized illicit idioms.\",\"representative_source_ids\":[\"QS-076c138a\",\"QS-3031ca21\",\"QS-5dd6f348\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:3:minimal-form-large-function","source_type":"word_analysis","support_id":"sup_081fbc93567a53f165b1","text":"{\"blocking_evidence\":null,\"headline\":\"single letter with clause-level force\",\"reader_payoff\":\"The reader notices that a minimal particle supplies a major grammatical bridge inside the short ayah.\",\"reason\":\"The word has no lexical root, but its syntactic position and emphatic function affect the whole predicate.\",\"representative_source_ids\":[\"QF-ef26f21d\",\"QT-55c9f9fa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:1:double-emphasis-frame","source_type":"word_analysis","support_id":"sup_08f6438740e058697162","text":"{\"blocking_evidence\":null,\"headline\":\"double emphasis around the claim\",\"reader_payoff\":\"The reader hears the diversity claim as doubly asserted: the subject is governed at the start and the predicate is reinforced at the landing.\",\"reason\":\"The local construction is explicitly analyzed as {{ar:إِنَّ}} ({{tr:inna}}) plus predicate {{ar:لَ}} ({{tr:la}}), with {{ar:سَعْيَكُمْ}} ({{tr:sa'yakum}}) as the governed ism and {{ar:شَتَّىٰ}} ({{tr:shattā}}) as the emphasized predicate.\",\"representative_source_ids\":[\"MG-07a12dd8\",\"QI-7bebe96f\",\"QY-8ad1d764\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:1:rootless-particle-form-pressure","source_type":"word_analysis","support_id":"sup_08f7e912bd5f84e4eb68","text":"{\"blocking_evidence\":null,\"headline\":\"rootless form with audible force\",\"reader_payoff\":\"The reader notices that a function word, not a lexical image, supplies the first force of certainty and governance.\",\"reason\":\"The source rows correctly tie the word's force to its annulling and emphatic function; there is no root branch to activate.\",\"representative_source_ids\":[\"QS-6c804943\",\"QF-2479f856\",\"QF-71fddff3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:2:bracketed-center-of-assertion","source_type":"word_analysis","support_id":"sup_0b64e8e026039cabeeb3","text":"{\"blocking_evidence\":null,\"headline\":\"human effort bracketed by emphasis\",\"reader_payoff\":\"The reader notices that the double-emphatic frame does not float above the verse; it encloses the audience's own striving.\",\"reason\":\"The local word order places {{ar:سَعْيَكُمْ}} ({{tr:sa'yakum}}) between the two emphatic particles.\",\"representative_source_ids\":[\"QI-f123f18a\",\"QT-e131dc04\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:2:boundary-pivot-to-human-action","source_type":"word_analysis","support_id":"sup_100536fd1e8d4cef2cd9","text":"{\"blocking_evidence\":null,\"headline\":\"created signs pivot into human action\",\"reader_payoff\":\"The reader feels the boundary move from witnessed creation to accountable human activity.\",\"reason\":\"The suffix supplies direct plural address after the third-person oath material of 92:1-3.\",\"representative_source_ids\":[\"QT-c8b6163c\",\"QB-07938205\",\"QB-bbe685d3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:sound-of-fracture-and-release","source_type":"word_analysis","support_id":"sup_170213c3fcfeb85fd20a","text":"{\"blocking_evidence\":null,\"headline\":\"doubled stop and open ending\",\"reader_payoff\":\"The reader hears the final word tighten at its center and then open outward, matching the dispersive predicate without replacing lexical evidence.\",\"reason\":\"The phonetic rows are retained as secondary support because they are tied to the local written and recited form of {{ar:شَتَّىٰ}} ({{tr:shattā}}).\",\"representative_source_ids\":[\"QF-1ee2d84f\",\"QF-7fc222a5\",\"QP-65ac44ac\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4","source_type":"word_analysis","support_id":"sup_17d4ae2029eb48ff5669","text":"{\"gloss_range\":\"diverse, scattered, divergent, or non-convergent as a predicate state; not an active causative scattering verb\",\"prose\":\"{{ar:شَتَّىٰ}} ({{tr:shattā}}) is the ayah's landing word: the delayed predicate that completes the assertion about {{ar:سَعْيَكُمْ}} ({{tr:sa'yakum}}). It does more than say that efforts are varied; the root field presses toward scattering, separation, and non-convergence. The form is adjectival and predicative, so the ayah states a condition of divergence without naming a scattering agent. Its feminine-pattern predicate can describe the singular maṣdar as a pluralized field, turning one owned category of striving into many scattered kinds. The preceding oath pairs in 92:1-3, including created differentiation in 92:3, arrive here as a many-path thesis, which 92:5-10 immediately begins to sort. The emphatic frame spends its force on this short-distribution dispersal predicate; same-word natural diversity in 20:53 confirms the range, while 92:4 applies it to human effort. Social dispersion can sharpen the separation image, while the winter association remains background rather than a local sense. Its doubled middle stop and long open ending let the compact final beat tighten, break, and release outward.\",\"root_display\":\"{{ar:ش ت ت}} ({{tr:sh-t-t}})\",\"root_gloss_range\":\"accepted local branch centers on scattering and separation; gapped-teeth and distance-formula branches remain lexical background, and seasonal imagery is not locally activated\",\"surface_display\":\"{{ar:شَتَّىٰ}} ({{tr:shattā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:final-predicate-completion","source_type":"word_analysis","support_id":"sup_19fca3dd8dbb70caeae0","text":"{\"blocking_evidence\":null,\"headline\":\"final predicate carries the thesis\",\"reader_payoff\":\"The reader waits until the last word to learn the thesis the oath has been building toward.\",\"reason\":\"Attachment evidence makes {{ar:شَتَّىٰ}} ({{tr:shattā}}) the khabar of {{ar:إِنَّ}} ({{tr:inna}}), reinforced by the emphatic lām rather than governed by it as a prepositional complement.\",\"representative_source_ids\":[\"QG-531b0c0d\",\"QT-0e412de3\",\"QI-f05dce08\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:scene-shift-created-to-human-plurality","source_type":"word_analysis","support_id":"sup_1bccf4a7d818edd1dce2","text":"{\"blocking_evidence\":null,\"headline\":\"created differentiation becomes human plurality\",\"reader_payoff\":\"The reader sees the created differentiation of 92:3 handed into the scattered human plurality of 92:4.\",\"reason\":\"Boundary rows connect 92:3's created categories to the human-effort predicate in 92:4.\",\"representative_source_ids\":[\"QB-5fe10950\",\"QB-b1952911\",\"QB-b8c38d53\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:1:direct-address-turn","source_type":"word_analysis","support_id":"sup_1c87bffeaef3246bc905","text":"{\"blocking_evidence\":null,\"headline\":\"oath register turns toward the audience\",\"reader_payoff\":\"The reader feels the surah move from witnessed signs to a proposition aimed at the audience.\",\"reason\":\"The clause follows the oath formulas in 92:1-3 and introduces the second-person possessed subject {{ar:سَعْيَكُمْ}} ({{tr:sa'yakum}}).\",\"representative_source_ids\":[\"QI-556823ed\",\"QB-68d5a8c9\",\"QT-f73e33b8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:3:hinge-and-final-beat","source_type":"word_analysis","support_id":"sup_240b52abcfaef9f1f42d","text":"{\"blocking_evidence\":null,\"headline\":\"hinge before the compact landing\",\"reader_payoff\":\"The reader feels the short second beat as a compressed landing on the predicate.\",\"reason\":\"The particle stands between the subject and predicate while being phonologically heard with {{ar:شَتَّىٰ}} ({{tr:shattā}}).\",\"representative_source_ids\":[\"QT-c0f3f2ce\",\"MT-4dea4420\",\"QP-e7d29626\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:immediate-two-path-sorting","source_type":"word_analysis","support_id":"sup_25b694e2b860db1693a5","text":"{\"blocking_evidence\":null,\"headline\":\"diverse field immediately sorted\",\"reader_payoff\":\"The reader sees 92:5 and 92:8 as concrete sorting of the diverse field named in 92:4.\",\"reason\":\"The rows explicitly connect {{ar:شَتَّىٰ}} ({{tr:shattā}}) to the paired behavioral branches introduced at 92:5 and 92:8.\",\"representative_source_ids\":[\"QI-6c70d56a\",\"QB-3413d3ea\",\"QB-fcd59c5c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:plural-predicate-over-singular-masdar","source_type":"word_analysis","support_id":"sup_322a3ac1e29f2f8f222a","text":"{\"blocking_evidence\":null,\"headline\":\"singular effort made pluralized\",\"reader_payoff\":\"The reader sees one category of striving grammatically opened into many scattered kinds.\",\"reason\":\"QAC describes {{ar:شَتَّىٰ}} ({{tr:shattā}}) as a feminine-pattern adjective functioning as a plural adjective for the singular maṣdar {{ar:سَعْي}} ({{tr:sa'y}}).\",\"representative_source_ids\":[\"QG-09c4c425\",\"MG-cb825f4f\",\"QF-dbeed6ab\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:1:governed-emphatic-oath-answer","source_type":"word_analysis","support_id":"sup_32d274f1889577c349f4","text":"{\"blocking_evidence\":null,\"headline\":\"governed oath-answer assertion\",\"reader_payoff\":\"The reader notices that the oath sequence resolves into a syntactically governed thesis, not a free-standing observation.\",\"reason\":\"QAC and attachment evidence identify {{ar:إِنَّ}} ({{tr:inna}}) as governing {{ar:سَعْيَكُمْ}} ({{tr:sa'yakum}}) and introducing the emphatic nominal predication after the oaths.\",\"representative_source_ids\":[\"QG-0e9eb9f8\",\"QI-87db7631\",\"MT-c5d49d8e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:2","source_type":"word_analysis","support_id":"sup_33db8d6ccbd2024c5fdc","text":"{\"gloss_range\":\"your striving, active effort, or purposeful exertion; locally the addressees' own endeavor rather than striving directed toward them\",\"prose\":\"{{ar:سَعْيَكُمْ}} ({{tr:sa'yakum}}) names the field being judged: not people in the abstract, but the addressees' owned striving. The construct suffix makes the effort personally assigned, while the accusative position shows it has been drawn under {{ar:إِنَّ}} ({{tr:inna}}). It also sits between the opening particle and the predicate lām, so the double-emphatic frame encloses the audience's own striving before the predicate lands. The root keeps purposeful motion, labor and earning, moral exertion, and broader pursuit together as one domain, but the local predicate favors the subjective reading: these are the addressees' own efforts that diverge. The singular maṣdar gathers many actions under one category, and the final possessive ending makes the plural address audible at the end of the noun. Its directed-motion sense and sibilant proximity to {{ar:شَتَّىٰ}} ({{tr:shattā}}) sharpen the paradox: purposeful efforts can still become non-convergent. This is why the next sorting in 92:5-10 can divide the field without changing subjects.\",\"root_display\":\"{{ar:س ع ي}} ({{tr:s-ayn-y}})\",\"root_gloss_range\":\"broad range of purposeful going, work, earning, and active endeavor; technical office, tale-bearing, manumission earning, and specialized illicit branches remain inactive here\",\"surface_display\":\"{{ar:سَعْيَكُمْ}} ({{tr:sa'yakum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:4:2:1","source_type":"qac_morpheme","support_id":"sup_3f054498c27bb0d7a6f9","text":"{\"lemma_ar\":\"سَعْي\",\"morph_features\":\"STEM|POS:N|LEM:saEoy|ROOT:sEy|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"92:4:2:1\",\"qac_word_ref\":\"92:4:2\",\"root_ar\":\"س ع ي\",\"surface_ar\":\"سَعْيَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:seasonal-and-social-images-narrowed","source_type":"word_analysis","support_id":"sup_42a91c52e81862e2f145","text":"{\"blocking_evidence\":null,\"headline\":\"social dispersion kept, seasonal image restrained\",\"reader_payoff\":\"The reader may hear separation as socially concrete, while avoiding an unsupported seasonal reading of the ayah.\",\"reason\":\"V4 supports scattering and separation for {{ar:ش ت ت}} ({{tr:sh-t-t}}), but its available branches do not require activating a winter/season branch in this local predicate.\",\"representative_source_ids\":[\"QS-7b42191d\",\"QS-bc6824ce\",\"MS-a07dff8b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:1:sound-binding-opening","source_type":"word_analysis","support_id":"sup_45acda6d4c0c3c8896fb","text":"{\"blocking_evidence\":null,\"headline\":\"nasal opening binds into the subject\",\"reader_payoff\":\"The reader hears the assertion begin as a tight particle-subject unit before the predicate arrives.\",\"reason\":\"The sound observation is retained as local acoustic support for the opening particle's grammatical attachment to the following governed noun.\",\"representative_source_ids\":[\"QP-3e556747\",\"QP-52442595\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:oath-binaries-to-many-paths","source_type":"word_analysis","support_id":"sup_4bc38bd36d94120e1db7","text":"{\"blocking_evidence\":null,\"headline\":\"binary oaths become many-path thesis\",\"reader_payoff\":\"The reader sees the ordered pairs of 92:1-3 certify a more complex moral field rather than a simple binary slogan.\",\"reason\":\"Boundary rows tie the oath sequence in 92:1-3 to the pluralizing predicate in 92:4.\",\"representative_source_ids\":[\"QS-3d2bae71\",\"QT-630b54c6\",\"MT-24c3ea58\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:intertext-natural-diversity","source_type":"word_analysis","support_id":"sup_4cc9f81b86baaa17fff5","text":"{\"blocking_evidence\":null,\"headline\":\"same-word natural diversity kept as contrast\",\"reader_payoff\":\"The reader sees that the word can describe kinds in creation (20:53), while 92:4 applies the dispersive predicate to human effort.\",\"reason\":\"The useful concrete parallel is the same word in 20:53; the row's additional reference is kept only as broad context because the local evidence here is the predicate over {{ar:سَعْيَكُمْ}} ({{tr:sa'yakum}}).\",\"representative_source_ids\":[\"MI-6ddfac5e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:second-beat-maxim","source_type":"word_analysis","support_id":"sup_59505a6a9a18c9fc1ca2","text":"{\"blocking_evidence\":null,\"headline\":\"compact second beat\",\"reader_payoff\":\"The reader hears the ayah close in a compressed emphatic unit.\",\"reason\":\"The particle and predicate form the short second beat {{ar:لَشَتَّىٰ}} ({{tr:la-shattā}}), with the predicate as the landing word.\",\"representative_source_ids\":[\"QT-6df6a773\",\"QP-21ec521c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:2:governed-owned-striving","source_type":"word_analysis","support_id":"sup_60f0458c94e16af4f831","text":"{\"blocking_evidence\":null,\"headline\":\"owned striving under emphatic governance\",\"reader_payoff\":\"The reader notices that the assertion is aimed at the addressees' own field of action, not at an abstract category of effort.\",\"reason\":\"Attachment evidence makes {{ar:سَعْيَكُمْ}} ({{tr:sa'yakum}}) the governed complement of {{ar:إِنَّ}} ({{tr:inna}}) and identifies the suffix as the direct plural addressees.\",\"representative_source_ids\":[\"QG-d9af3be4\",\"QG-aedb243c\",\"QG-c915332e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:cooccurrence-background-no-local-payoff","source_type":"word_analysis","support_id":"sup_67a1b73c92b77df0ee83","text":"{\"blocking_evidence\":null,\"headline\":\"co-occurrence note without distinct local payoff\",\"reader_payoff\":null,\"reason\":\"No local attachment or sense evidence requires a separate co-occurrence topic for {{ar:شَتَّىٰ}} ({{tr:shattā}}).\",\"representative_source_ids\":[\"ME-f92d298a\"],\"status\":\"dropped_filler\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:2:cooccurrence-background-no-local-payoff","source_type":"word_analysis","support_id":"sup_6d871966cdb6f14f2656","text":"{\"blocking_evidence\":null,\"headline\":\"co-occurrence background without local payoff\",\"reader_payoff\":null,\"reason\":\"The local bundle's collocation profile does not make this co-occurrence claim necessary for interpreting {{ar:سَعْيَكُمْ}} ({{tr:sa'yakum}}) in 92:4.\",\"representative_source_ids\":[\"ME-3a4582ee\"],\"status\":\"dropped_filler\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:predicate-state-not-causative-agent","source_type":"word_analysis","support_id":"sup_799bf0ce4829e931d3e6","text":"{\"blocking_evidence\":null,\"headline\":\"state of divergence, not caused scattering\",\"reader_payoff\":\"The reader notices the condition of divergent efforts without importing an unstated agent who scatters them.\",\"reason\":\"The root family includes causative scattering language, but the local form is a predicate noun/adjective, not a finite causative verb.\",\"representative_source_ids\":[\"QS-ff5f9c58\",\"QF-e5409314\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:2:possessive-ending-audible-address","source_type":"word_analysis","support_id":"sup_7fc5eb2fa7262b17c2a9","text":"{\"blocking_evidence\":null,\"headline\":\"suffix makes the collective audible\",\"reader_payoff\":\"The reader hears the addressees attached to the very noun being evaluated.\",\"reason\":\"Attachment evidence treats the suffix as the possessor and direct plural addressee, while the surface form carries that suffix at the end of the noun.\",\"representative_source_ids\":[\"QF-3663d344\",\"QF-b9073030\",\"QP-b64f9b91\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:3:predicate-emphatic-lam","source_type":"word_analysis","support_id":"sup_7feffb6ecf4f468bdd62","text":"{\"blocking_evidence\":null,\"headline\":\"predicate lām, not preposition\",\"reader_payoff\":\"The reader avoids a false directional reading and keeps the clause centered on emphatic assertion.\",\"reason\":\"QAC and attachment evidence identify this {{ar:لَ}} ({{tr:la}}) as emphatic on the predicate, not genitive or prepositional.\",\"representative_source_ids\":[\"QG-8f8d31f7\",\"QS-a1abd472\",\"QF-04bf0409\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:scattered-diverse-not-mild-variety","source_type":"word_analysis","support_id":"sup_84690af7f0312d6ef767","text":"{\"blocking_evidence\":null,\"headline\":\"diversity with separation pressure\",\"reader_payoff\":\"The reader notices that the efforts are not merely many styles; they move apart into divergent directions.\",\"reason\":\"V4 branch B001 for {{ar:ش ت ت}} ({{tr:sh-t-t}}) supports scattering, separation, and difference among kinds or hearts, which fits the predicate over human striving.\",\"representative_source_ids\":[\"QS-236be2d8\",\"QS-e3b64956\",\"QS-f35df773\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:1","source_type":"word_analysis","support_id":"sup_8c39a87f8b688cb68833","text":"{\"gloss_range\":\"emphatic annulling particle governing the clause; not a lexical noun or verb\",\"prose\":\"{{ar:إِنَّ}} ({{tr:inna}}) turns the oath sequence into a governed assertion rather than a loose observation. It takes {{ar:سَعْيَكُمْ}} ({{tr:sa'yakum}}) under its governance and works with the later {{ar:لَ}} ({{tr:la}}) to make the final predicate the certified thesis of the oath answer. The particle has no lexical root, so its pressure comes from function: assertion, case government, and opening placement. Its doubled nasal form gives the first beat audible weight and closes into the following governed noun as a tight particle-subject sound unit, while the move from cosmic oath objects to a second-person claim begins here.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِنَّ}} ({{tr:inna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:3","source_type":"word_analysis","support_id":"sup_9201ee2d6d2700d0a9e7","text":"{\"gloss_range\":\"emphatic predicate lām; not the preposition for, to, or belonging to\",\"prose\":\"{{ar:لَ}} ({{tr:la}}) is the second emphatic stroke of the clause. Its fatḥa and position before {{ar:شَتَّىٰ}} ({{tr:shattā}}) keep it from being read as a preposition; it reinforces the predicate rather than introducing a for/to phrase. Together with the opening particle, it completes the double-emphasis answer to 92:1-3, so the final predicate is the oath answer's landing and not a secondary modifier. Because it sits between {{ar:سَعْيَكُمْ}} ({{tr:sa'yakum}}) and {{ar:شَتَّىٰ}} ({{tr:shattā}}), the listener crosses a marked hinge before the decisive word lands. In recitation it fuses with the predicate as {{ar:لَشَتَّىٰ}} ({{tr:la-shattā}}), making the grammar audible as a compact final beat.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَ}} ({{tr:la}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:rare-or-short-distribution-emphasized","source_type":"word_analysis","support_id":"sup_9c72d52ff3fa502977d0","text":"{\"blocking_evidence\":null,\"headline\":\"marked predicate under maximum emphasis\",\"reader_payoff\":\"The reader notices that the emphatic frame spends its force on a marked dispersal predicate.\",\"reason\":\"The contextual profile lists five exact-root/form instances and does not mark low occurrence, so the row's rarity language is narrowed to a short, marked distribution rather than an absolute rarity claim.\",\"representative_source_ids\":[\"QI-4d14d101\",\"QI-a1ac5a77\",\"QH-86cac2ec\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:directed-dispersion-paradox","source_type":"word_analysis","support_id":"sup_a88ae66382aaea2876de","text":"{\"blocking_evidence\":null,\"headline\":\"directed striving becomes non-convergent\",\"reader_payoff\":\"The reader feels the paradox that purposeful efforts can still scatter away from one another.\",\"reason\":\"The singular possessed maṣdar gathers effort into one owned field, while {{ar:شَتَّىٰ}} ({{tr:shattā}}) predicates divergence of that field.\",\"representative_source_ids\":[\"QE-8cfe9c36\",\"QY-e3e3235d\",\"QY-6dea0951\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:4:3:2","source_type":"qac_morpheme","support_id":"sup_abf79322c98eba97bac6","text":"{\"lemma_ar\":\"شَتَّىٰ\",\"morph_features\":\"STEM|POS:N|LEM:$at~aY`|ROOT:$tt|MS|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"92:4:3:2\",\"qac_word_ref\":\"92:4:3\",\"root_ar\":\"ش ت ت\",\"surface_ar\":\"شَتَّىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:2:subjective-idafa-selected","source_type":"word_analysis","support_id":"sup_b93dcb7d68921145b99d","text":"{\"blocking_evidence\":null,\"headline\":\"subjective possession over objective pressure\",\"reader_payoff\":\"The reader sees the audience as accountable agents whose own pursuits are being described as divergent.\",\"reason\":\"The objective possibility is preserved only as a pressure; {{ar:شَتَّىٰ}} ({{tr:shattā}}) most naturally predicates divergence of activities owned by the addressees.\",\"representative_source_ids\":[\"QG-c294cf6f\",\"QS-4ad40192\",\"QG-1811780d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:4:qualitative-classification","source_type":"word_analysis","support_id":"sup_bd3c69a2f9f4ea345af0","text":"{\"blocking_evidence\":null,\"headline\":\"qualitative classification of striving\",\"reader_payoff\":\"The reader takes the word as the clause's classification of the striving itself, not as a loose modifier or object.\",\"reason\":\"The attachment data identifies a predication relation, and the lām is emphatic rather than a governing preposition.\",\"representative_source_ids\":[\"QG-68d1ffcb\",\"QG-2b8b71db\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:2:surah-sorting-domain","source_type":"word_analysis","support_id":"sup_c61b6ba76419184fd20a","text":"{\"blocking_evidence\":null,\"headline\":\"domain prepared for the next sorting\",\"reader_payoff\":\"The reader sees 92:5-10 as the parsing of the diverse striving announced in 92:4, not as a disconnected new topic.\",\"reason\":\"Rows tie {{ar:سَعْيَكُمْ}} ({{tr:sa'yakum}}) to the immediate split in 92:5-10, with a later contrast to wealth in 92:11 and an effort-as-defining parallel in 53:39, 17:19, 20:66, and 21:94.\",\"representative_source_ids\":[\"QI-ce4a7fbf\",\"MT-762a6964\",\"QB-83591263\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:2:singular-collective-masdar","source_type":"word_analysis","support_id":"sup_c8d7e2881bdc10d30689","text":"{\"blocking_evidence\":null,\"headline\":\"one category holding many efforts\",\"reader_payoff\":\"The reader notices the paradoxical setup: one owned category is immediately opened into many divergent instances.\",\"reason\":\"The local form is a singular verbal noun with a plural possessive suffix, and {{ar:شَتَّىٰ}} ({{tr:shattā}}) predicates dispersive plurality over that noun.\",\"representative_source_ids\":[\"QF-e2574363\",\"QF-eb206044\",\"QF-f5415b24\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:2:sound-and-semantic-tension","source_type":"word_analysis","support_id":"sup_e14c7c9833742f53a46e","text":"{\"blocking_evidence\":null,\"headline\":\"directed sound beside scattered outcome\",\"reader_payoff\":\"The reader hears and sees the paradox: striving implies direction, while the predicate says those directions do not converge.\",\"reason\":\"The topic survives when kept local to the contrast between {{ar:سَعْيَكُمْ}} ({{tr:sa'yakum}}) and {{ar:شَتَّىٰ}} ({{tr:shattā}}), rather than made into an independent phonetic proof.\",\"representative_source_ids\":[\"MS-eacafbad\",\"QE-0997b45b\",\"QE-f2e3bae2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:4:3:double-emphasis-completion","source_type":"word_analysis","support_id":"sup_fa0d0dc394d189d76a3b","text":"{\"blocking_evidence\":null,\"headline\":\"completion of inna...la emphasis\",\"reader_payoff\":\"The reader hears the final predicate as the emphatic answer to the oath series, not as a secondary modifier.\",\"reason\":\"The local construction combines {{ar:إِنَّ}} ({{tr:inna}}) and predicate {{ar:لَ}} ({{tr:la}}) as the double-emphasis answer to 92:1-3.\",\"representative_source_ids\":[\"MG-78c2ef0a\",\"QI-fd6faa44\",\"QB-b9883488\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ سَعْيَكُمْ لَشَتَّىٰ","ayah_ref":"92:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000709/B001","root_000775/B001","root_000775/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000709","role":"Purposeful going supplies the directed motion that makes each striving a vector rather than static effort.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000775","role":"Scattering separates the plural vectors into distinct courses.","root":"ش ت ت","source_ref":"92:4","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000775","role":"Distance between two things turns difference of course into potentially radical separation of ends.","root":"ش ت ت","source_ref":"92:4","source_word_indices":["3"]}],"changed_reading":{"after":"The addressees are already moving toward sought ends, but their trajectories fan apart and may finish very far from one another.","before":"The addressees perform different kinds of work."},"confidence":"strong","focus_anchor":"The plural possessive in 'your striving' joins purposeful motion to a predicate of scattering and far-apartness.","mechanism":"Each striving is a vector toward something sought, while the collective field fans into separated courses and endpoints. Diversity therefore concerns direction and destination, not merely a list of unlike activities.","model_id":"baseline_directed_divergence"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_directed_divergence","source_type":"hft","support_id":"sup_a17bf6be0bbab470b6f2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ سَعْيَكُمْ لَشَتَّىٰ","ayah_ref":"92:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000709/B002","root_000709/B003","root_000709/B006","root_000775/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000709","role":"Work, earning, and active conduct supply the economic substrate of the plural striving.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000709","role":"Agency or office over a group makes some striving an entrusted public function.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_000709","role":"Noble generosity and peacemaking supply a reparative social use of effort.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000775","role":"Separation keeps these social deployments from collapsing into a morally neutral category of busyness.","root":"ش ت ت","source_ref":"92:4","source_word_indices":["3"]}],"changed_reading":{"after":"People inhabit divergent economies of effort: earning, governing, reconciling, and giving organize communal life in materially different ways.","before":"People expend unequal amounts of individual effort."},"confidence":"medium","focus_anchor":"The noun for striving can name earning, public agency, and noble social undertakings, all gathered under the plural 'your.'","mechanism":"The verse can inventory rival social economies: ordinary acquisition, administration over people and resources, and generosity or peacemaking. Their separation is institutional as well as personal because each mode distributes power, wealth, and repair differently.","model_id":"baseline_social_economies"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_social_economies","source_type":"hft","support_id":"sup_84c4210b369b365a8586","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ سَعْيَكُمْ لَشَتَّىٰ","ayah_ref":"92:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000709/B005","root_000709/B007","root_000775/B003"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000709","role":"Earning toward manumission makes striving a labor process whose sought end is recovered freedom.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]},{"branch_id":"B007","mapped_root_id":"root_000709","role":"The specialized coercive arrangement makes striving an imposed revenue mechanism over an enslaved woman's body.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000775","role":"Far-apartness holds emancipation and extraction as opposed agency regimes rather than adjacent examples.","root":"ش ت ت","source_ref":"92:4","source_word_indices":["3"]}],"changed_reading":{"after":"Strivings can differ at the deeper level of who owns the laboring body and whether effort releases agency or extracts it.","before":"Strivings differ because people choose different objects."},"confidence":"exploratory","focus_anchor":"Two specialized branches of the focus noun place labor for release beside coerced sexual extraction, while the predicate marks distance.","mechanism":"The same lexical field can hold opposite ownership structures. One laborer earns toward release from bondage; another captive body is made to earn for an owner. The verse can therefore expose not only different deeds but radically different possession of agency within work.","model_id":"baseline_agency_polarity"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_agency_polarity","source_type":"hft","support_id":"sup_f39832ef1db403a51296","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ سَعْيَكُمْ لَشَتَّىٰ","ayah_ref":"92:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000709/B001","root_000760/B002","root_000775/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000709","role":"Purposeful movement supplies the strongly oriented pole of striving.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000760","role":"The non-dominant branch of neglect and wandering loose supplies an exploratory pole of unguided motion and wasted holdings.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000775","role":"Scattering describes what motion becomes when a common orientation no longer holds it together.","root":"ش ت ت","source_ref":"92:4","source_word_indices":["3"]}],"changed_reading":{"after":"The field ranges from deliberate pursuit to neglected drift; difference can arise from the presence or failure of orientation itself.","before":"Every striving is equally intentional but aimed at a different target."},"confidence":"exploratory","focus_anchor":"The split mapping of the focus root juxtaposes purposeful going with neglected wandering, and the predicate supplies scattering.","mechanism":"A live tension appears between directed pursuit and motion released without care. Some striving is governed by an aim; some becomes drift because its bearer or resources are left loose. Diversity may thus register different degrees of orientation, not only different chosen goals.","model_id":"baseline_aim_and_drift"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_aim_and_drift","source_type":"hft","support_id":"sup_af08b2229429b6768fce","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ سَعْيَكُمْ لَشَتَّىٰ","ayah_ref":"92:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000709/B002","root_000775/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000709","role":"The broad field of work supplies the multiple units whose relation is being patterned.","root":"س ع ي","source_ref":"92:4","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000775","role":"Gapped teeth supply a bodily image in which non-overlap creates ordered and potentially attractive spacing.","root":"ش ت ت","source_ref":"92:4","source_word_indices":["3"]}],"changed_reading":{"after":"Some plurality may be productively spaced: distinct acts can avoid overlap and become clearer precisely because they do not merge.","before":"Scattered striving is necessarily chaotic fragmentation."},"confidence":"exploratory","focus_anchor":"The predicate's specialized image of well-spaced teeth permits separation without disorder.","mechanism":"Difference need not mean collision or ruin. As spacing prevents overlap and can produce a fine ordered row, distinct works may remain non-identical yet become mutually legible. The verse can describe a patterned plurality as well as a moral bifurcation.","model_id":"baseline_constructive_spacing"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_constructive_spacing","source_type":"hft","support_id":"sup_621eb756d39cf4d9bdbe","trust":"legacy_unbound"}]}
</lane_packet_json>
