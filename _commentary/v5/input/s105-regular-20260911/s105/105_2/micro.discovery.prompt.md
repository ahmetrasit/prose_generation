# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **105:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s105-regular-20260911/s105/105_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "105:2",
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
{"analysis_context":{"analysis_id":"s105-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"105:2","host_surah":105,"lane_context_refs":[],"ordered_context_refs":["105:0","105:1","105:3","105:4","105:5","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal, var olan bir şeyi başka bir duruma sokmayı, adlandırmayı ya da bir eyleme başlamayı kapsamaz.","branch_kind":"bare","branch_ref":"root_000248/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"105:2:2:1","qac_word_ref":"105:2:2","surface_ar":"يَجْعَلْ"}],"gloss":"bir şeyi yapıp var etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığın yapılmasını, üretilmesini veya varlığa çıkarılmasını bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin üretilmesi, yaratılması veya yokken ortaya çıkarılması anlatıldığında dalın bütün çekirdeğini karşılar.","boundary_detail":"Bu dal, var olan bir şeyi başka bir duruma sokmayı, adlandırmayı ya da bir eyleme başlamayı kapsamaz.","branch_image_ar":"إحداث الشيء وصنعه","concept_gloss":"bir şeyi yapıp var etme","contextual_glosses":[{"applicability":"Bir nesnenin veya varlığın ortaya çıkarılışını bildiren tamamlanmış eylem bağlamlarında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapma ile var etme arasındaki çekirdek anlam genişliğini korur."},"facet_ids":["F001"],"text":"onu yaptı ya da var etti","usage_role":"contextual"}],"definition":"Bir şeyi yapmak, üretmek, yaratmak ya da daha önce yokken var etmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığın yapılmasını, üretilmesini veya varlığa çıkarılmasını bildirir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi yapma, üretme, yaratma veya yokken var etme anlamlarını açıkça aynı çekirdekte toplar. Geçici dal çerçevesi bu üretici ve var edici işlemi doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi yapmak, yaratmak veya var etmek"}],"lexicalization_note":"Dal yalın kullanıma dayanır; tanım herhangi bir özel söz öbeğine bağlı değildir.","neighbor_coverage_note":"Bütün adaylar incelendi; en güçlü karışma noktaları durum değiştirme dalı ile daha geniş yapma ve iş görme dalıdır, öteki adaylar aynı sınırı daha az açıklayıcı biçimde yineler.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sonucu bir şeyin yapılması ya da var edilmesidir; komşu dalda ise var olan katılımcı korunur ve yalnızca onun durumu veya niteliği değiştirilir.","focus_only":"Yeni bir şeyi üretme veya yokken varlığa çıkarma işlemini anlatır.","gloss":"bir duruma sokma","neighbor_only":"Var olan bir kişi ya da şeyi belirli bir duruma, niteliğe veya konuma getirir.","neighbor_ref":"root_000248/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir etkenin yol açtığı sonuç ve değişiklik bulunur."},{"boundary_match":"partial","distinction":"Odak dal nesnenin yapılması veya var edilmesinde yoğunlaşırken komşu dal, ortaya bir nesne çıkarmayan genel eylem ve davranışları da içine alır.","focus_only":"Bir şeyi üretme, yaratma veya varlığa çıkarma yönü belirgindir.","gloss":"yapma ve iş görme","neighbor_only":"İyi ya da kötü her türlü işi ve davranışı da kapsayan daha geniş bir eylem alanına sahiptir.","neighbor_ref":"root_000885/B001","relation_type":"near_synonym","shared_zone":"Bir şeyi yapma ve ortaya çıkarma anlamlarında iki dal geniş ölçüde örtüşür."}],"source_phrase_ar":"جعلت الشيء صنعته (maqayis)؛ جعل جعلا صنع صنعا (ayn)؛ جعل خلق؛ خلقنا (tahdhib)؛ يجري مجرى أوجد (mufradat)","source_summary":"Kaynaklar, bir şeyi yapma ile onu yaratıp var etme yönlerini ortak bir üretici eylem altında birleştirir.","sources":["MQ","AY","TA","MU"],"what_is_ar":"يدخل فيه جعل الشيء بمعنى صنعه أو خلقه أو أوجده.","what_is_not_ar":"لا يدخل فيه التصيير إلى حال، ولا التسمية والقول، ولا الشروع في الفعل."},"support_links":[]},{"boundary":"Burada katılımcı varlığını sürdürür ve durumu değişir; onu yoktan üretme, adlandırma veya eyleme başlatma anlamı yoktur.","branch_kind":"bare","branch_ref":"root_000248/B002","candidate_links":[{"candidate_id":"cand_cd12b0497cfc75141387","lane":"micro"},{"candidate_id":"cand_69fbd896ba3111dec9f5","lane":"micro"},{"candidate_id":"cand_2ad3883413768226114c","lane":"micro"},{"candidate_id":"cand_a018f14db3aaf5929f90","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"105:2:2:1","qac_word_ref":"105:2:2","surface_ar":"يَجْعَلْ"}],"gloss":"birini veya şeyi belirli bir duruma getirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Var olan bir katılımcının durumunu, niteliğini veya konumunu değiştiren ettirici işlemi bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Katılımcının varlığı korunurken niteliği, görevi, konumu veya durumu değiştirildiğinde eksiksiz karşılık verir.","boundary_detail":"Burada katılımcı varlığını sürdürür ve durumu değişir; onu yoktan üretme, adlandırma veya eyleme başlatma anlamı yoktur.","branch_image_ar":"تصيير الشيء على حال","concept_gloss":"birini veya şeyi belirli bir duruma getirme","contextual_glosses":[{"applicability":"Bir kişinin veya şeyin yeni bir nitelik, görev ya da duruma geçirilmesini anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Var olan katılımcının ettirici bir işlemle yeni duruma geçmesini korur."},"facet_ids":["F001"],"text":"onu bu duruma getirdi","usage_role":"contextual"}],"definition":"Bir kişi veya şeyi belirli bir duruma, niteliğe ya da konuma getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Var olan bir katılımcının durumunu, niteliğini veya konumunu değiştiren ettirici işlemi bildirir."}],"identity_rationale":"Kaynak ifadesi, bir kişi veya şeyi belirli bir duruma, niteliğe ya da konuma getirme işlemini doğrudan bildirir. Verilen örnekler hem görev ve konum kazandırmayı hem de üstün bir niteliğe ulaştırmayı destekler.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi belirli bir duruma, niteliğe veya konuma getirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyi belirli bir duruma getirmek"}],"lexicalization_note":"Dal yalın kullanıma dayanır; özel bir söz öbeğinin anlamı genel tanıma taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; üretme ile ettirici olmayan duruma gelme, bu dalın katılımcı yapısını en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda sonuç, aynı katılımcının yeni durumudur; komşu dalda ise sonuç yapılan veya var edilen şeyin kendisidir.","focus_only":"Var olan katılımcıyı koruyup onun durumunu veya niteliğini değiştirir.","gloss":"bir şeyi var etme","neighbor_only":"Bir şeyi yapma, üretme ya da yokken varlığa çıkarma işlemini anlatır.","neighbor_ref":"root_000248/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de bir etkenin ortaya çıkardığı yeni sonucu ifade eder."},{"boundary_match":"partial","distinction":"Odak dal ettirici ve etkilenen olmak üzere iki katılımcılıdır; komşu dalda durum değişimi öznenin başına gelir ve ayrı bir ettirici zorunlu değildir.","focus_only":"Bir etkenin başka bir katılımcıyı yeni duruma soktuğu geçişli yapıyı gerektirir.","gloss":"bir duruma gelme","neighbor_only":"Öznenin bir dış ettirici belirtilmeden kendisinin yeni bir duruma gelmesini bildirir.","neighbor_ref":"root_000839/B010","relation_type":"near_neighbor","shared_zone":"İki dal da önceki durumdan farklı bir sonuç durumuna geçişi anlatır."}],"source_phrase_ar":"جعله الله نبيا أي صيره (sihah)؛ جعل صير؛ جعلته أحذق الناس؛ صيرهم؛ صيرته (tahdhib)","source_summary":"Kaynaklar, birini bir göreve veya üstün bir niteliğe getirmenin aynı durum değiştirme çekirdeğine bağlı olduğunu gösterir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه جعل الشيء أو الشخص على صفة أو منزلة، كتصييره نبيا أو جعله أحذق الناس.","what_is_not_ar":"لا يدخل فيه الخلق والإيجاد المجرد، ولا التسمية، ولا جعل بمعنى أخذ يفعل."},"support_links":["sup_42d4c5fd159c0d49ffad","sup_700eab952f67d317e573","sup_7981bcc602ead38ea3eb","sup_a2c64243a9915c58da2b"]},{"boundary":"Çekirdek adlandırma ve söylemedir; aynı söz dizimine ilişkin durum değiştirme yorumu ayrı bir kaynak değişkesi olarak tutulur.","branch_kind":"unresolved","branch_ref":"root_000248/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"105:2:2:1","qac_word_ref":"105:2:2","surface_ar":"يَجْعَلْ"}],"gloss":"öyle adlandırma ya da öyle olduğunu söyleme; başka yorumda öyle kılma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığı belli bir adla veya nitelikle anmayı ve onun öyle olduğunu söylemeyi bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı tanıklık için, varlığı söylenen duruma gerçekten getirme biçiminde rakip bir yorum da aktarılır."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem baskın adlandırma ve söyleme çözümünü hem de aynı tanıklığa ilişkin durum değiştirme yorumunu birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Çekirdek adlandırma ve söylemedir; aynı söz dizimine ilişkin durum değiştirme yorumu ayrı bir kaynak değişkesi olarak tutulur.","branch_image_ar":"قول الشيء أو تسميته","concept_gloss":"öyle adlandırma ya da öyle olduğunu söyleme; başka yorumda öyle kılma","contextual_glosses":[{"applicability":"Sözün bir varlığa ad veya nitelik yükleyen anlatım olarak çözüldüğü bağlamda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı ifadenin varlığı gerçekten o duruma getirme biçimindeki rakip yorumunu dışarıda bırakır.","preserves":"Adlandırma ve sözle niteleme çözümünü açık biçimde korur."},"facet_ids":["F001"],"text":"onları öyle adlandırdılar","usage_role":"contextual"},{"applicability":"Tanıklığın gerçek bir durum değişikliği olarak yorumlandığı bağlamda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Baskın adlandırma ve söyleme çözümünü dışarıda bırakır.","preserves":"Rakip durum değiştirme yorumunu doğrudan korur."},"facet_ids":["F002"],"text":"onları öyle yaptılar","usage_role":"contextual"}],"definition":"Bir varlığı belirli bir ad veya nitelikle anmak ya da onun öyle olduğunu söylemektir; aynı ifadenin bir yorumunda ise varlığı gerçekten o duruma getirme anlamı vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığı belli bir adla veya nitelikle anmayı ve onun öyle olduğunu söylemeyi bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı tanıklık için, varlığı söylenen duruma gerçekten getirme biçiminde rakip bir yorum da aktarılır."}],"identity_rationale":"Kaynak ifadesinin baskın açıklaması bir varlığı belirli bir ad veya nitelikle anma ve onun öyle olduğunu söylemedir. Bununla birlikte aynı ifadenin bir başka yorumda o varlığı gerçekten söz konusu duruma getirme diye açıklandığı da kaydedilir; bu yüzden dal ancak bu yorum ayrılığı belirtilerek korunabilir.","lexicalization_note":"Kullanımın yalın olup olmadığı mekanik olarak çözümlenmemiştir; tanım bağımsız bir yalın anlam varsaymaz.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; en yararlı ayrımlar geniş sözlü anma alanı ile aynı tanıklığa rakip olan gerçek durum değişikliğidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir yüklemeyi adlandırma veya söyleme olarak çözer; komşu dal ise sözlü anmayı ve hakkında konuşmayı daha geniş biçimde kapsar.","focus_only":"Belirli bir nesneyi veya varlığı belli bir ad ya da nitelikle anma yapısına bağlıdır.","gloss":"dilde anma ve adlandırma","neighbor_only":"Bir şeyi dilde anma, açığa vurma ve insanlar hakkında iyi ya da kötü söz söyleme alanlarına da uzanır.","neighbor_ref":"root_000516/B004","relation_type":"near_synonym","shared_zone":"Bir şeyi sözle belirtme ve adlandırma bölgesinde iki dal örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın baskın okuması dilsel bir yüklemedir; komşu dal gerçek dünyadaki durum değişikliğini anlatır ve odak dalda yalnızca rakip yorum olarak görünür.","focus_only":"Çekirdeğinde sözle adlandırma veya bir niteliği söyleme vardır.","gloss":"bir duruma sokma","neighbor_only":"Var olan katılımcının durumunu gerçekten değiştiren ettirici işlemdir.","neighbor_ref":"root_000248/B002","relation_type":"near_neighbor","shared_zone":"Aynı yüzey yapısı, aktarılan yorum ayrılığı nedeniyle iki anlam alanına yaklaşabilir."}],"source_phrase_ar":"جعلوا الملائكة إناثا أي سموهم (sihah)؛ جعل قال؛ أي قلناه؛ وقال غيره صيرناه (tahdhib)","source_summary":"Toplu tanıklık adlandırma ve söyleme açıklamasını verirken, aynı ifadenin durum değiştirme diye yorumlandığını da kaynak adı yüklemeden kaydeder.","sources":["SI","TA"],"what_is_ar":"يدخل فيه جعل بمعنى قال أو سمى بحسب النصوص التي صرحت بذلك.","what_is_not_ar":"لا يدخل فيه التصيير إلا حيث اختلف المصدر في العبارة نفسها."},"support_links":[]},{"boundary":"Anlam yalnızca ardından bir eylem gelen yapıya bağlıdır ve genel yapma, üretme ya da kesintisiz sürdürme anlamına genişletilemez.","branch_kind":"non_bare","branch_ref":"root_000248/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"105:2:2:1","qac_word_ref":"105:2:2","surface_ar":"يَجْعَلْ"}],"gloss":"bir eylemi yapmaya başlama","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Öznenin belirtilen eyleme başlamasını veya girişmesini anlatan yapı bağımlı bir kullanımdır."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca öznenin hemen ardından belirtilen eyleme giriştiğini bildiren yapı bağımlı kullanımı karşılar.","boundary_detail":"Anlam yalnızca ardından bir eylem gelen yapıya bağlıdır ve genel yapma, üretme ya da kesintisiz sürdürme anlamına genişletilemez.","branch_image_ar":"الشروع في الفعل أو ملازمته","concept_gloss":"bir eylemi yapmaya başlama","contextual_glosses":[{"applicability":"Ardından gelen eylemin özne tarafından başlatıldığını bildiren geçmiş zamanlı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öznenin belirtilen eyleme giriştiği başlangıç aşamasını korur."},"facet_ids":["F001"],"text":"yapmaya başladı","usage_role":"contextual"}],"definition":"Yalnızca ardından çekimli bir eylem gelen yapıda, öznenin o eylemi yapmaya başlamasını veya ona girişmesini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Öznenin belirtilen eyleme başlamasını veya girişmesini anlatan yapı bağımlı bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi, çekimli bir eylemden önce gelen yapının o eyleme girişme veya başlamayı bildirdiğini gösterir. Geçici çerçevedeki genel bağlı kalma ve sürdürme yönü kaynak cümlesinde kurucu bir koşul değildir; tanım bu nedenle başlangıç anlamına göre yeniden kurulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyi yapmaya başlamak"}],"lexicalization_note":"Dal yalnızca ardından çekimli bir eylem gelen özel yapıda geçerlidir; yalın kök anlamı olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; başlangıçla sürdürmeyi birlikte taşıyan yakın yapı ile yalnız devam bildiren yapı, sınırı en iyi görünür kılar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın güvenli çekirdeği başlangıçtır; komşu dalda ise başlangıçla birlikte sürdürme veya bağlı kalma yönü de açıkça yer alır.","focus_only":"Kaynak tanıklığı çekirdek olarak bir eyleme girişmeyi bildirir.","gloss":"bir eyleme başlayıp sürdürme","neighbor_only":"Başlangıcın yanında eyleme bağlı kalma ve onu sürdürme yönünü de taşıyabilir.","neighbor_ref":"root_000941/B001","relation_type":"near_synonym","shared_zone":"Ardından eylem gelen yapılarda başlangıç bildirme bakımından güçlü bir örtüşme vardır."},{"boundary_match":"partial","distinction":"Odak dal başlangıç aşamasını seçer; komşu dal başlangıcı değil, önceden süren durumun devamını ve özel bir olumsuz kuruluşu gerektirir.","focus_only":"Eylemin başlangıç sınırını ve ona girişmeyi bildirir.","gloss":"eylemi sürdürme","neighbor_only":"Olumsuz kuruluşta eylemin ya da haberin kesintisiz sürmesini bildirir.","neighbor_ref":"root_000659/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bir öznenin bir eylemle zaman içinde ilişkisini kurar."}],"source_phrase_ar":"تقول جعل يقول ولا تقول صنع يقول (maqayis)؛ جعل يأكل وجعل يصنع كذا (ayn)؛ جعل فلان يصنع كذا كقولك طفق وعلق يفعل (tahdhib)؛ يجري مجرى صار وطفق فلا يتعدى نحو جعل زيد يقول (mufradat)","source_summary":"Kaynaklar, bu yapıyı ardından gelen eyleme başlama veya girişme anlamında ve nesne almayan bir kuruluş olarak ortaklaştırır.","sources":["MQ","AY","TA","MU"],"what_is_ar":"يدخل فيه جعل يفعل كذا، أي أخذ أو طفق أو علق بالفعل.","what_is_not_ar":"لا يدخل فيه صنع الشيء ولا تصييره ولا جعله أجرا."},"support_links":[]},{"boundary":"Bu dal iş veya görev karşılığında belirlenen ödemedir; genel armağanı, yapılan işi, durum değiştirmeyi ve tencere bezini kapsamaz.","branch_kind":"bare","branch_ref":"root_000248/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"105:2:2:1","qac_word_ref":"105:2:2","surface_ar":"يَجْعَلْ"}],"gloss":"iş karşılığı belirlenen ücret veya ortaklaşa kararlaştırılan ödeme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir iş veya görevin yapılması karşılığında bir kişiye ayrılan ücret, ödeme ya da armağandır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğun sefer veya önemli bir iş sırasında kendi arasında kararlaştırdığı ortak ödemeleri de kapsar."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem bir kişiye iş için ayrılan karşılığı hem de bir topluluğun önemli iş için kararlaştırdığı ödeme biçimini kapsar.","boundary_detail":"Bu dal iş veya görev karşılığında belirlenen ödemedir; genel armağanı, yapılan işi, durum değiştirmeyi ve tencere bezini kapsamaz.","branch_image_ar":"أجر مجعول على عمل","concept_gloss":"iş karşılığı belirlenen ücret veya ortaklaşa kararlaştırılan ödeme","contextual_glosses":[{"applicability":"Belirli bir işi üstlenecek kişiye vaat edilen ücret veya ödülün anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir topluluğun kendi arasında kararlaştırdığı ortak ödeme özel durumunu dışarıda bırakır.","preserves":"Bir işin yapılmasına bağlanan bireysel ücret veya ödül çekirdeğini korur."},"facet_ids":["F001"],"text":"bu işi yapana verilecek ücret","usage_role":"contextual"},{"applicability":"Bir sefer veya önemli iş için insanların aralarında ödeme belirlediği topluluk bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir kişiye belirli bir işi yapması için ayrılan bireysel ücret biçimini dışarıda bırakır.","preserves":"Topluluğun karşılıklı olarak ödeme kararlaştırması yönünü korur."},"facet_ids":["F002"],"text":"ortaklaşa kararlaştırılan ödeme","usage_role":"contextual"}],"definition":"Bir kişinin yapacağı iş veya görev karşılığında ona verilmek üzere belirlenen ücret, ödeme ya da armağandır. Bir topluluğun sefer veya önemli bir iş için aralarında kararlaştırdığı ödemeler de bu çekirdeğin özel bir gerçekleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir iş veya görevin yapılması karşılığında bir kişiye ayrılan ücret, ödeme ya da armağandır."},{"facet_id":"F002","role":"specialization","statement":"Bir topluluğun sefer veya önemli bir iş sırasında kendi arasında kararlaştırdığı ortak ödemeleri de kapsar."}],"identity_rationale":"Kaynak ifadesi, bir kişiye yapacağı iş veya yerine getireceği görev karşılığında ayrılan ücret, ödeme ya da armağanı açıkça tanımlar. İnsanların bir sefer veya önemli iş için aralarında kararlaştırdıkları ortak ödemeler de aynı karşılık belirleme çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir iş karşılığında belirlenen ücret, ödeme veya ödül"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"önemli bir iş için ortaklaşa kararlaştırılan ödemeler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ona bir ödeme veya armağan ayırmak"}],"lexicalization_note":"Dal yalın ad alanına dayanır; özel bir söz öbeğiyle sınırlı değildir.","neighbor_coverage_note":"Bütün adaylar incelendi; genel emek karşılığı ile düzenli çalışan ücreti, bu dalın önceden belirlenen görev karşılığı sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir işi yaptırmak için konan veya kararlaştırılan karşılıktır; komşu dalın karşılık alanı daha geniştir ve önceden konma koşulu taşımaz.","focus_only":"Belirli bir iş yapılmadan önce veya onun için konan karşılığı öne çıkarır.","gloss":"emek karşılığı ve kira","neighbor_only":"Yapılmış işin karşılığını, kirayı, manevi ödülü ve evlilikte verilen bedeli de kapsar.","neighbor_ref":"root_000015/B001","relation_type":"near_synonym","shared_zone":"Bir iş ya da hizmet karşılığında verilen maddi bedel alanında örtüşürler."},{"boundary_match":"partial","distinction":"Odak dal görev koşuluna bağlı vaat veya belirlemedir; komşu dal düzenli çalışma karşılığındaki ücret ve geçim payı alanında daha özeldir.","focus_only":"Tek bir görev için vaat edilen ödülü ve topluca kararlaştırılan ödemeyi de kapsar.","gloss":"çalışanın ücreti","neighbor_only":"Bir çalışanın düzenli iş ücreti veya geçim payı olmasına odaklanır.","neighbor_ref":"root_001046/B004","relation_type":"near_synonym","shared_zone":"Yapılan emek karşılığında bir kişiye verilen maddi ödemede örtüşürler."}],"source_phrase_ar":"الجعل والجعالة والجعلية ما يجعل للإنسان على الأمر يفعله (maqayis)؛ الجعل ما جعلت لإنسان أجرا له على عمل يعمله؛ الجعالات ما يتجاعل الناس بينهم (ayn)؛ الجعل ما جعل للانسان من شئ على الشئ يفعله؛ الجعالة؛ الجعيلة مثله (sihah)؛ الجعل في العطية؛ الجعالة بالفتح من الشيء تجعله للإنسان؛ ما جعلته للإنسان أجرا على عمله (tahdhib)","source_summary":"Kaynaklar iş karşılığında önceden ayrılan ücret veya armağanda birleşir; topluca kararlaştırılan ödemeler bu çekirdeğin özel biçimi olarak aktarılır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الجعل والجعلية والجعالة والجعيلة وما يتجاعله الناس أجرا أو عطية على عمل أو أمر.","what_is_not_ar":"لا يدخل فيه فعل جعل بمعنى صنع أو صير، ولا الجعال خرقة القدر."},"support_links":[]},{"boundary":"Dal yalnızca kısa veya küçük hurma ağaçlarına ilişkindir; yer adı, böcek ve genel bitki kısalığı anlamlarına uzanmaz.","branch_kind":"bare","branch_ref":"root_000248/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"105:2:2:1","qac_word_ref":"105:2:2","surface_ar":"يَجْعَلْ"}],"gloss":"kısa veya küçük hurma ağaçları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kısa veya küçük hurma ağaçlarını topluluk olarak, tekil biçimiyle de bunlardan birini adlandırır."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hurma ağaçlarının boyca kısa ya da küçük oluşuna göre topluca adlandırıldığı kullanımların bütün çekirdeğini karşılar.","boundary_detail":"Dal yalnızca kısa veya küçük hurma ağaçlarına ilişkindir; yer adı, böcek ve genel bitki kısalığı anlamlarına uzanmaz.","branch_image_ar":"النخل الصغار أو القصار","concept_gloss":"kısa veya küçük hurma ağaçları","contextual_glosses":[{"applicability":"Birden çok kısa veya küçük hurma ağacının topluca anıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kısa hurma ağaçlarını topluluk olarak adlandırma yönünü korur."},"facet_ids":["F001"],"text":"kısa hurma ağaçları topluluğu","usage_role":"contextual"}],"definition":"Kısa veya küçük hurma ağaçlarının topluluk adı ve bu topluluktaki tek bir ağacın adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kısa veya küçük hurma ağaçlarını topluluk olarak, tekil biçimiyle de bunlardan birini adlandırır."}],"identity_rationale":"Kaynak ifadesi, kısa veya küçük hurma ağaçlarını topluluk olarak ve bunlardan birini tekil biçimde tanımlar. Geçici çerçeve hem boy hem küçüklük yönünü ve tekil ayrımını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kısa veya küçük hurma ağaçları; tekili bu ağaçlardan biri"}],"lexicalization_note":"Dal yalın ad kullanımına dayanır; özel bir söz öbeğinden türetilmiş değildir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı küçük hurma alanındaki yakın ad ile özellikle genç sürgünü anlatan ad, sınırı açıklamak için yeterlidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hem küçük hem kısa ağaçlara uzanır; komşu dalın verilen sınırı yalnız küçüklüktür, bu nedenle tam ikame her bağlamda güvenli değildir.","focus_only":"Küçüklüğün yanında boyca kısalığı da açıkça kapsar.","gloss":"küçük hurma ağaçları","neighbor_only":"Yalnız küçük hurma ağaçlarını bildirir ve ayrı bir söz ailesine dayanır.","neighbor_ref":"root_000832/B006","relation_type":"near_synonym","shared_zone":"Küçük hurma ağaçlarını topluca adlandırmada iki dal doğrudan örtüşür."},{"boundary_match":"partial","distinction":"Odak dal boy veya genel küçüklük ölçütüne dayanır; komşu dal ise bitkinin sürgün ve dikim evresini seçer.","focus_only":"Kısa veya küçük hurma ağaçlarının kendisini topluluk olarak adlandırır.","gloss":"genç hurma sürgünleri","neighbor_only":"Özellikle yeni dikilmiş küçük sürgünleri ve bunların tekil ile çoğul biçimlerini adlandırır.","neighbor_ref":"root_001637/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal hurmanın küçük ve henüz gelişmemiş örnekleriyle ilişkilidir."}],"source_phrase_ar":"الجعل النخل يفوت اليد والواحدة جعلة (maqayis)؛ الجعل واحدها جعلة وهي النخل الصغار (ayn)؛ الجعل النخل القصار الواحدة جعلة (sihah)؛ الجعل قصار النخل (tahdhib)","source_summary":"Kaynaklar kısa veya küçük hurma ağaçları anlamında ve topluluk ile tek ağaç arasındaki biçim ayrımında birleşir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الجعل للنخل الصغار أو القصار، والواحدة جعلة.","what_is_not_ar":"لا يدخل فيه جعلة اسم المكان ولا الجعل الدويبة."},"support_links":[]},{"boundary":"Dal tencereyi indirmeye yarayan ısı koruyucu bez ve onunla yapılan eylemle sınırlıdır; ücret anlamındaki benzer biçim buna girmez.","branch_kind":"bare","branch_ref":"root_000248/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"105:2:2:1","qac_word_ref":"105:2:2","surface_ar":"يَجْعَلْ"}],"gloss":"sıcak tencereyi indirme bezi ve onunla indirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sıcak tencereyi ocaktan indirirken tutmaya yarayan ve eli sıcaktan koruyan bezdir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tencereyi bu bez aracılığıyla ateşten indirme eylemini de bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem ısıdan koruyan araç adı hem de tencereyi bu araçla ocaktan indirme eylemi birlikte gösterileceğinde kullanılır.","boundary_detail":"Dal tencereyi indirmeye yarayan ısı koruyucu bez ve onunla yapılan eylemle sınırlıdır; ücret anlamındaki benzer biçim buna girmez.","branch_image_ar":"خرقة إنزال القدر","concept_gloss":"sıcak tencereyi indirme bezi ve onunla indirme","contextual_glosses":[{"applicability":"Sıcak tencereyi tutup ocaktan indirmeye yarayan bez nesne olarak anıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı bezle tencereyi indirmeyi bildiren eylem kullanımını dışarıda bırakır.","preserves":"Aracın tencereyi indirme ve eli ısıdan koruma işlevini korur."},"facet_ids":["F001"],"text":"tencereyi ateşten indirme bezi","usage_role":"contextual"},{"applicability":"Tencerenin özel bez kullanılarak ocaktan indirilmesi eylem olarak anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bezin bağımsız araç adı olarak kullanılmasını dışarıda bırakır.","preserves":"Tencereyi koruyucu bez aracılığıyla indirme işlemini korur."},"facet_ids":["F002"],"text":"tencereyi bezle ateşten indirmek","usage_role":"contextual"}],"definition":"Sıcak tencereyi ateşten veya dayandığı taşlardan indirirken kullanılan ve eli sıcaktan koruyan bezdir; bu bezle tencereyi indirme eylemi de aynı dala bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sıcak tencereyi ocaktan indirirken tutmaya yarayan ve eli sıcaktan koruyan bezdir."},{"facet_id":"F002","role":"associated_use","statement":"Tencereyi bu bez aracılığıyla ateşten indirme eylemini de bildirir."}],"identity_rationale":"Kaynak ifadesi, sıcak tencereyi ateşten veya onu taşıyan taşlardan indirirken kullanılan ve eli sıcaktan koruyan bezi açıkça tanımlar. Aynı tanıklık, tencereyi bu bezle indirme eylemini de ayrı bir türemiş kullanım olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sıcak tencereyi ateşten indirmeye yarayan koruyucu bez"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"tencereyi koruyucu bezle ateşten indirmek"}],"lexicalization_note":"Dal yalın ad ve ona bağlı eylem biçimlerini kapsar; başka dallardaki benzer sesli adlar tanıma alınmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; tencereyi yönetmeye yarayan çubuk ile onu ateşte taşıyan taş, aracın özgül işlevini en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak araç tencerenin dışından tutulmasını ve ocaktan indirilmesini sağlar; komşu araç tencerenin içine sokularak kaynamayı yatıştırır.","focus_only":"Tencereyi ocaktan indirirken kullanılan ve eli sıcaktan koruyan bir bezdir.","gloss":"tencere karıştırma çubuğu","neighbor_only":"Tencerenin içini karıştırıp kaynamasını yatıştırmak için kullanılan bir çubuktur.","neighbor_ref":"root_001676/B011","relation_type":"same_field","shared_zone":"İki araç da sıcak tencereyi güvenli biçimde yönetmeye yarayan ev gereçleridir."},{"boundary_match":"thematic_only","distinction":"Odak dal kaldırma sırasında kullanılan koruyucu aracı, komşu dal ise pişirme sırasında tencereyi taşıyan yapısal desteği adlandırır.","focus_only":"Eli koruyarak tencereyi ateşten indirmeye yarayan taşınabilir bir bezdir.","gloss":"tencereyi taşıyan üçüncü taş","neighbor_only":"Tencereyi ateş üzerinde taşımak için iki taşa eklenen üçüncü sabit destektir.","neighbor_ref":"root_000203/B007","relation_type":"thematic","shared_zone":"Her ikisi de ateş üzerindeki tencerenin kurulması ve kaldırılması senaryosunda yer alır."}],"source_phrase_ar":"الجعال الخرقة التي تنزل بها القدر عن الأثافي (maqayis)؛ الجعال والجعالة خرقة تنزل بها القدر عن رأس النار يتقى بها من الحر (ayn)؛ الجعال الخرقة التي تنزل بها القدر عن النار؛ أجعلت القدر (sihah)؛ الجعال الخرقة التي تنزل بها القدور؛ أجعلت القدر إجعالا إذا أنزلتها بالجعال (tahdhib)","source_summary":"Kaynaklar bezin tencereyi ateşten indirirken ısıdan koruma işlevinde birleşir ve aynı araçla yapılan indirme eylemini de aktarır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الجعال أو الجعالة، وهي خرقة تنزل بها القدر عن النار أو الأثافي ويتقى بها الحر.","what_is_not_ar":"لا يدخل فيه الجعالة بمعنى الأجر."},"support_links":[]},{"boundary":"Hayvanın kendisi yalın çekirdektir; suya ilişkin anlam yalnız bu hayvanların suda çok bulunmasını bildiren özel kuruluşta geçerlidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000248/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"105:2:2:1","qac_word_ref":"105:2:2","surface_ar":"يَجْعَلْ"}],"gloss":"kara küçük yer hayvanı ve bunlarla dolu su","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kara renkli küçük bir yer hayvanını adlandırır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yalnız suyla kurulan kullanımda, bu hayvanların suyun içinde çokça bulunmasını bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın hayvan adı ile yalnız bu hayvanların çokça bulunduğu suyu anlatan bağlı kullanım birlikte gösterileceğinde uygundur.","boundary_detail":"Hayvanın kendisi yalın çekirdektir; suya ilişkin anlam yalnız bu hayvanların suda çok bulunmasını bildiren özel kuruluşta geçerlidir.","branch_image_ar":"دويبة الجعلان","concept_gloss":"kara küçük yer hayvanı ve bunlarla dolu su","contextual_glosses":[{"applicability":"Canlının kendisi yalın bir ad olarak anıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu hayvanların çok bulunduğu suyu anlatan bağlı kullanımı dışarıda bırakır.","preserves":"Kara renkli küçük yer hayvanı çekirdeğini korur."},"facet_ids":["F001"],"text":"kara renkli küçük yer hayvanı","usage_role":"contextual"},{"applicability":"Suyun içinde söz konusu hayvanların çokça bulunduğu özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanın bağımsız yalın ad olarak kullanılmasını dışarıda bırakır.","preserves":"Suya bağlı hayvan çokluğu ve doluluk yönünü korur."},"facet_ids":["F002"],"text":"bu hayvanlarla dolu su","usage_role":"contextual"}],"definition":"Kara renkli küçük bir yer hayvanıdır. Buna bağlı söz öbeği, bu hayvanların içine çokça düştüğü veya içinde çoğaldığı suyu niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kara renkli küçük bir yer hayvanını adlandırır."},{"facet_id":"F002","role":"associated_use","statement":"Yalnız suyla kurulan kullanımda, bu hayvanların suyun içinde çokça bulunmasını bildirir."}],"identity_rationale":"Kaynak ifadesi, küçük bir yer hayvanını ve onun kara renkli oluşunu bildirir; ayrıca bu hayvanların çokça bulunduğu suyu niteleyen bağlı kullanımı verir. Geçici çerçeve bu iki kapsamı doğru ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kara renkli küçük bir yer hayvanı"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bu hayvanların çokça bulunduğu su"}],"lexicalization_note":"Yalın hayvan adı ile yalnız bu hayvanların çokça bulunduğu suyu niteleyen söz öbeği ayrı facetlerde tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel küçük yer hayvanları sınıfı, odak canlının belirli bir ad oluşunu açıklayan en yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir hayvan adıdır ve suya özgü türemiş kullanımı vardır; komşu dal ise birçok farklı küçük hayvanı içine alan üst sınıftır.","focus_only":"Kara renkli belirli bir küçük yer hayvanını ve ona bağlı su niteliğini adlandırır.","gloss":"küçük yer hayvanları","neighbor_only":"Küçük yer hayvanlarının pek çok türünü topluca kapsayan genel bir sınıf adıdır.","neighbor_ref":"root_000324/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal küçük ve yerde yaşayan hayvanlar alanında buluşur."}],"source_phrase_ar":"الجعل دابة من هوام الأرض (ayn)؛ الجعل دويبة؛ جعل الماء بالكسر أي كثر فيه الجعلان (sihah)؛ الجعل دابة سوداء من دواب الأرض تجمع جعلانا؛ ماء مجعل وجعل إذا تهافتت فيه الجعلان (tahdhib)","source_summary":"Kaynaklar küçük yer hayvanı anlamında birleşir; kara renk niteliğini ve hayvanların çok bulunduğu suya özgü kullanımı da topluca destekler.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه الجعل دابة أو دويبة من هوام الأرض، وجمعها جعلان، وما وصف به الماء إذا كثرت فيه الجعلان.","what_is_not_ar":"لا يدخل فيه الجعل بمعنى الأجر أو النخل."},"support_links":[]},{"boundary":"Dal dişi köpek ve benzeri yırtıcı dişilerin çiftleşme isteğiyle sınırlıdır; erkeğin isteğini veya çiftleşmenin gerçekleşmesini bildirmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000248/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"105:2:2:1","qac_word_ref":"105:2:2","surface_ar":"يَجْعَلْ"}],"gloss":"dişinin çiftleşmek için erkeği istemesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"specialization","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi köpeği, çiftleşmek için erkeği isteyen durumda niteleyen söz öbeğidir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi köpek ve diğer yırtıcı dişilerin erkeği istemesi durumunu çekimli biçimlerle bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi köpek veya benzeri yırtıcı dişinin çiftleşme isteğini bildiren hem niteleme hem eylem biçimlerini karşılar.","boundary_detail":"Dal dişi köpek ve benzeri yırtıcı dişilerin çiftleşme isteğiyle sınırlıdır; erkeğin isteğini veya çiftleşmenin gerçekleşmesini bildirmez.","branch_image_ar":"اشتهاء الأنثى للفحل","concept_gloss":"dişinin çiftleşmek için erkeği istemesi","contextual_glosses":[{"applicability":"Dişi köpek veya benzeri bir yırtıcı dişinin erkeği istediği durum niteleme olarak verildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişi hayvanın çiftleşmeye yönelik erkek isteğini korur."},"facet_ids":["F001","F002"],"text":"çiftleşmek isteyen dişi","usage_role":"contextual"}],"definition":"Dişi köpeğin veya benzeri yırtıcı bir dişinin çiftleşmek için erkeği istemesidir; hem belirli bir söz öbeği hem de çekimli biçimler bu durumu anlatır.","distinctive_facets":[{"facet_id":"F001","role":"specialization","statement":"Dişi köpeği, çiftleşmek için erkeği isteyen durumda niteleyen söz öbeğidir."},{"facet_id":"F002","role":"core","statement":"Dişi köpek ve diğer yırtıcı dişilerin erkeği istemesi durumunu çekimli biçimlerle bildirir."}],"identity_rationale":"Kaynak ifadesi, dişi köpeğin ve diğer yırtıcı dişilerin çiftleşmek üzere erkeği istemesini açıkça bildirir. Hem dişi köpekle kurulan söz öbeği hem de çekimli biçimler aynı üreme isteği durumuna bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"çiftleşmek isteyen dişi köpek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"dişinin çiftleşmek için erkeği istemesi"}],"lexicalization_note":"Dişi köpekle kurulan söz öbeği ile dişinin isteğini bildiren çekimli biçimler ayrı tutulur; kapsam genel bir yalın kök anlamına çevrilmez.","neighbor_coverage_note":"Bütün adaylar incelendi; daha geniş hayvan kapsamlı yakın ad ile dişi deveye özgü ad, tür sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın tür sınırı köpek ve benzeri yırtıcılardır; komşu dal aynı durumu daha geniş bir hayvan listesinde adlandırır.","focus_only":"Dişi köpek ve benzeri yırtıcı dişiler için belirli niteleme ve eylem biçimlerine dayanır.","gloss":"dişi hayvanın erkeği istemesi","neighbor_only":"Koyun, sığır ve keçi gibi daha geniş evcil hayvan sınıflarına da uzanır.","neighbor_ref":"root_000860/B010","relation_type":"near_synonym","shared_zone":"Dişi köpek ve yırtıcı dişilerin çiftleşme isteğinde iki dal doğrudan örtüşür."},{"boundary_match":"partial","distinction":"Çekirdek durum aynıdır, ancak tür kapsamları ayrıdır: odak dal köpek ve yırtıcı dişilere, komşu dal dişi deveye bağlıdır.","focus_only":"Dişi köpek ve diğer yırtıcı dişilerin çiftleşme isteğine özgüdür.","gloss":"dişi devenin erkeği istemesi","neighbor_only":"Aynı isteği yalnız dişi deve için adlandırır.","neighbor_ref":"root_000009/B012","relation_type":"near_synonym","shared_zone":"Her iki dal dişi hayvanın çiftleşmek üzere erkeği istemesini anlatır."}],"source_phrase_ar":"كلبة مجعل إذا أرادت السفاد (maqayis)؛ أجعلت الكبة واستجعلت فهي مجعل إذا أرادت السفاد وكذلك سائر السباع (sihah)؛ أجعلت الكلبة والسباع كلها إذا اشتهت الفحل؛ استجعلت أيضا بمعناه (tahdhib)","source_summary":"Kaynaklar dişi köpeğin ve diğer yırtıcı dişilerin çiftleşme isteğinde birleşir ve söz öbeği ile çekimli biçimleri aynı duruma bağlar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه مجعل وأجعلت واستجعلت للكلبة والسباع إذا أرادت السفاد أو اشتهت الفحل.","what_is_not_ar":"لا يدخل فيه الجعل الدويبة ولا الفعل العام جعل."},"support_links":[]},{"boundary":"Dal yalnız deve kuşunun yavrusunu adlandırır; genel yavru, başka kuş yavrusu veya deve yavrusu anlamına genişlemez.","branch_kind":"bare","branch_ref":"root_000248/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"105:2:2:1","qac_word_ref":"105:2:2","surface_ar":"يَجْعَلْ"}],"gloss":"deve kuşu yavrusu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Türü deve kuşu olan genç yavruyu bildirir."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız deve kuşunun genç yavrusu adlandırıldığında eksiksiz ve doğal karşılıktır.","boundary_detail":"Dal yalnız deve kuşunun yavrusunu adlandırır; genel yavru, başka kuş yavrusu veya deve yavrusu anlamına genişlemez.","branch_image_ar":"فرخ النعام","concept_gloss":"deve kuşu yavrusu","contextual_glosses":[{"applicability":"Canlı bir cümlede deve kuşunun yavrusundan söz edilirken doğal sözcük sırasını sağlar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Deve kuşu türünü ve yavruluk durumunu eksiksiz korur."},"facet_ids":["F001"],"text":"yavru deve kuşu","usage_role":"contextual"}],"definition":"Deve kuşunun yavrusunu adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Türü deve kuşu olan genç yavruyu bildirir."}],"identity_rationale":"Kaynak ifadesi söz konusu biçimi doğrudan deve kuşunun yavrusu olarak açıklar. Geçici çerçeve bu hayvan türü ve yaşam evresi ayrımını eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"deve kuşu yavrusu"}],"lexicalization_note":"Dal yalın ad kullanımına dayanır ve herhangi bir özel söz öbeğiyle sınırlı değildir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çok anlamlı yakın ad ile genel yavru adı, tür ve kapsam sınırlarını en yararlı biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bütünüyle deve kuşu yavrusuna bağlıdır; komşu dal aynı karşılığın yanında tür ve insan bakımından başka anlamlara da uzanır.","focus_only":"Yalnız deve kuşu yavrusunu adlandıran tek anlamlı kullanım burada esastır.","gloss":"deve kuşu yavruları ve başka topluluklar","neighbor_only":"Deve kuşu yavrusunun yanında küçük develeri ve hizmetçileri de kapsayan daha geniş bir anlam kümesi vardır.","neighbor_ref":"root_000343/B008","relation_type":"near_synonym","shared_zone":"Deve kuşunun yavrusunu adlandırma alanında iki dal örtüşür."},{"boundary_match":"partial","distinction":"Odak dal tür bakımından özeldir; komşu dal pek çok canlı türünün yavrusunu içine alan genel sınıf adıdır.","focus_only":"Yavruluğu özellikle deve kuşu türüne bağlayan özel bir addır.","gloss":"küçük yavru","neighbor_only":"İnsan, evcil hayvan ve yabanıl hayvan yavrularını genel olarak kapsar.","neighbor_ref":"root_000942/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal doğumdan sonraki genç ve küçük yaşam evresini anlatır."}],"source_phrase_ar":"الجعول ولد النعام (maqayis)؛ الجعول الرأل ولد النعام (tahdhib)","source_summary":"Kaynaklar bu adın deve kuşunun yavrusunu bildirdiği konusunda birleşir.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه الجعول بمعنى الرأل، ولد النعام.","what_is_not_ar":"لا يدخل فيه الجعل الدويبة ولا الجعل النخل."},"support_links":[]},{"boundary":"Adın gösterdiği belirli yer açıklanmadığı için tanım bir yer kimliği uydurmaz ve sözü genel yer anlamına dönüştürmez.","branch_kind":"non_bare","branch_ref":"root_000248/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"105:2:2:1","qac_word_ref":"105:2:2","surface_ar":"يَجْعَلْ"}],"gloss":"belirtilmemiş bir yer adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kimliği belirtilmeyen bir yer için kullanılan özel addır."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynağın belirli yer kimliğini açıklamadan yalnızca yer adı diye sınıflandırdığı bu özel kullanım için uygundur.","boundary_detail":"Adın gösterdiği belirli yer açıklanmadığı için tanım bir yer kimliği uydurmaz ve sözü genel yer anlamına dönüştürmez.","branch_image_ar":"الجَعْلة اسم مكان","concept_gloss":"belirtilmemiş bir yer adı","contextual_glosses":[{"applicability":"Sözün genel yer anlamı taşımadığı, yalnız özel ad olarak kullanıldığı açıklanırken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözü kimliği belirtilmemiş özel bir yer adı olarak korur."},"facet_ids":["F001"],"text":"bir yerin adı","usage_role":"explanatory"}],"definition":"Kaynağın yalnızca bir yer adı olduğunu bildirdiği, gösterdiği yer açıklanmayan özel kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kimliği belirtilmeyen bir yer için kullanılan özel addır."}],"identity_rationale":"Tek kaynak ifadesi, sözün bir yer adı olduğunu açıkça bildirir ve bundan başka bir yer kimliği veya genel anlam vermez. Geçici çerçeve bu sınırlı tanıklığı doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kimliği belirtilmemiş bir yer adı"}],"lexicalization_note":"Dal yalnız belirli ad biçimine bağlıdır; genel veya yalın bir yer anlamı olarak genişletilemez.","neighbor_coverage_note":"Bütün adaylar incelendi; adayların her biri başka ve belirli bir yer adını veya genel yer alanını gösterir, ancak odak adın hangi yerle özdeş olduğunu kanıtlamaz; bu yüzden yayımlanabilir bir karşıtlık seçilmedi.","source_phrase_ar":"الجَعْلة اسم مكان (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık sözü bir yer adı olarak sınıflandırır, fakat hangi yeri gösterdiğini açıklamaz."}],"source_summary":"Bu kullanım tek bir tanıklıkla sınırlıdır ve yerin kimliğine ilişkin ek bir ortak açıklama bulunmaz.","sources":["MQ"],"what_is_ar":"يدخل فيه الجعلة حين يصرح المصدر بأنها اسم مكان.","what_is_not_ar":"لا يدخل فيه الجعلة الواحدة من النخل الصغار."},"support_links":[]},{"boundary":"Üç nitelik birlikte kurucudur; yalnız kısa, yalnız şişman veya yalnız inatçı olan biri bu dalın tam kapsamına girmez.","branch_kind":"bare","branch_ref":"root_000248/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"105:2:2:1","qac_word_ref":"105:2:2","surface_ar":"يَجْعَلْ"}],"gloss":"kısa, şişman ve inatçı olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kısa, şişman ve tartışmada inatla direnen kişiyi üç niteliği birlikte taşıyarak betimler."}}],"root_ar":"ج ع ل","root_id":"root_000248","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişide beden kısalığı, şişmanlık ve inatçı çekişkenlik birlikte anlatıldığında tam karşılık verir.","boundary_detail":"Üç nitelik birlikte kurucudur; yalnız kısa, yalnız şişman veya yalnız inatçı olan biri bu dalın tam kapsamına girmez.","branch_image_ar":"قصر مع سمن ولجاج","concept_gloss":"kısa, şişman ve inatçı olma","contextual_glosses":[{"applicability":"Üç niteliği birlikte taşıyan bir kişiyi doğal cümle içinde nitelemek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiyi belirleyen üç kurucu niteliğin tümünü birlikte korur."},"facet_ids":["F001"],"text":"kısa, şişman ve inatçı biri","usage_role":"contextual"}],"definition":"Bir kişide kısalık, şişmanlık ve inatçı çekişkenliğin birlikte bulunmasını anlatan nitelemedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kısa, şişman ve tartışmada inatla direnen kişiyi üç niteliği birlikte taşıyarak betimler."}],"identity_rationale":"Tek kaynak ifadesi, bir kişide kısalık, şişmanlık ve inatçı çekişkenliğin birlikte bulunmasını tek bir betimleyici anlam olarak verir. Geçici çerçeve bu üç kurucu niteliği doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kısa, şişman ve inatçı kişi"}],"lexicalization_note":"Dal yalın betimleyici kullanıma dayanır ve özel bir söz öbeğiyle sınırlı değildir.","neighbor_coverage_note":"Bütün adaylar incelendi; kısa ve toplu kişi betimi ile genel beden dolgunluğu, üç niteliğin birlikte bulunması koşulunu en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bedensel kısalık ve şişmanlığa davranışsal inatçılığı ekler; komşu dal ise bedensel kalınlık ve gücü öne çıkarır.","focus_only":"Şişmanlık ile tartışmada inatla direnme niteliklerini kısalıkla birlikte gerektirir.","gloss":"kısa, kalın ve güçlü kişi","neighbor_only":"Kalın, güçlü ve toplu beden yapısını bildirir, fakat inatçılığı gerektirmez.","neighbor_ref":"root_001315/B008","relation_type":"near_synonym","shared_zone":"Kısa ve toplu beden yapısına sahip kişiyi betimlemede iki dal örtüşür."},{"boundary_match":"partial","distinction":"Odak dal üçlü bir kişi niteliğidir; komşu dal yalnız bedensel dolgunluğu seçer ve farklı canlı türlerine de uygulanabilir.","focus_only":"Kısalık ve inatçı çekişkenliği şişmanlıkla birlikte zorunlu kılar.","gloss":"bedenin dolgun ve şişman olması","neighbor_only":"İnsan veya hayvanda bedenin dolgunlaşıp yağlanmasını anlatır, boy ve huy koşulu taşımaz.","neighbor_ref":"root_000352/B006","relation_type":"near_neighbor","shared_zone":"Şişmanlık ve beden dolgunluğu anlam alanında iki dal buluşur."}],"source_phrase_ar":"الجعل القصر مع السمن واللجاج (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık üç niteliği ayırmadan kısa, şişman ve inatçı kişi betimlemesinde birleştirir."}],"source_summary":"Bu birleşik kişi betimlemesi tek bir tanıklığa dayanır; kısalık, şişmanlık ve inatçı çekişkenlik birlikte verilir.","sources":["TA"],"what_is_ar":"يدخل فيه الجعل بمعنى اجتماع القصر والسمن واللجاج في وصف الشخص.","what_is_not_ar":"لا يدخل فيه قصر النخل ولا الدويبة المسماة جعلا."},"support_links":[]},{"boundary":"Bu dal fiziksel olarak gözden yitme, bir şeyi kaybetme, unutma ya da kayıp hayvan adı olma anlamlarını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_000913/B001","candidate_links":[{"candidate_id":"cand_cd12b0497cfc75141387","lane":"micro"},{"candidate_id":"cand_a018f14db3aaf5929f90","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَضْلِيل","morph_features":"STEM|POS:N|VN|(II)|LEM:taDoliyl|ROOT:Dll|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:5:1","qac_word_ref":"105:2:5","surface_ar":"تَضْلِيلٍ"}],"gloss":"doğru yoldan ve amaçtan sapma ya da başkasını saptırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Amaçtan, doğru yoldan veya doğruluktan ayrılma ve uygun yönü bulamama anlamın temelidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yanlış, asılsız veya boş işlere yönelme, yönsel sapmanın düşünce ve davranış alanındaki uzantısıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, başka birini doğru yoldan veya amaçtan uzaklaştırmayı bildirir."}}],"root_ar":"ض ل ل","root_id":"root_000913","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yönsel, düşünsel ve davranışsal çekirdeği ile buna bağlı ettirgen kullanımı birlikte anlatır.","boundary_detail":"Bu dal fiziksel olarak gözden yitme, bir şeyi kaybetme, unutma ya da kayıp hayvan adı olma anlamlarını içermez.","branch_image_ar":"الضلال عن الهدى والقصد","concept_gloss":"doğru yoldan ve amaçtan sapma ya da başkasını saptırma","contextual_glosses":[{"applicability":"Bir kişinin yol, amaç, doğruluk veya sağduyu bakımından uygun yönden ayrıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasını saptıran ettirgen kullanımı tek başına anlatmaz.","preserves":"Kişinin doğru yön veya amaçtan ayrılması çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"doğru yoldan sapmak","usage_role":"general"},{"applicability":"Bir öznenin başka birini doğru yoldan, amaçtan veya doğruluktan uzaklaştırdığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendisinin sapması ve yolunu bulamaması anlamlarını dışarıda bırakır.","preserves":"Başkasını doğru doğrultudan uzaklaştıran ettirgen ilişkiyi korur."},"facet_ids":["F003"],"text":"saptırmak","usage_role":"contextual"},{"applicability":"Gerçek bir yerde doğru yolu bulamama anlatıldığında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Düşünsel ve ahlaki sapmayı, yanlış işlere yönelmeyi ve ettirgen kullanımı kapsamaz.","preserves":"Uygun yönü bulamama unsurunu korur."},"facet_ids":["F001"],"text":"yolunu şaşırmak","usage_role":"contextual"}],"definition":"Bir kimsenin amaçtan, doğru yoldan veya doğruluktan ayrılması, yolunu bulamaması ya da yanlış ve boş olana yönelmesidir. Ettirgen kullanımda başka biri bu doğrultudan uzaklaştırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Amaçtan, doğru yoldan veya doğruluktan ayrılma ve uygun yönü bulamama anlamın temelidir."},{"facet_id":"F002","role":"extension","statement":"Yanlış, asılsız veya boş işlere yönelme, yönsel sapmanın düşünce ve davranış alanındaki uzantısıdır."},{"facet_id":"F003","role":"associated_use","statement":"Ettirgen kullanım, başka birini doğru yoldan veya amaçtan uzaklaştırmayı bildirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Tek bir istemsiz hata anlamıyla karışabilir.","fit":"narrowing","loses":"Yoldan veya amaçtan ayrılma durumunu, boş işlere yönelmeyi ve ettirgen anlamı kaybeder.","preserves":"Doğru sonuca ulaşamama yönünü kısmen korur."},"text":"yanılmak"}],"identity_rationale":"Kaynak ifadesi, anlamın çekirdeğini amaçtan, doğru yoldan ve doğruluktan ayrılma olarak kurar; hem yolunu bulamama hem de yanlış ve boş işlere yönelme bu çekirdeğin gerçekleşmeleridir. Başkasını doğru yoldan uzaklaştıran ettirgen kullanım da aynı anlam alanına bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"doğru yoldan, amaçtan veya doğruluktan sapmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"doğru yoldan ve doğruluktan sapma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"doğru yoldan veya amaçtan sapmış kimse"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sapmada direnen, çok sapmış kimse"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"iyilikten uzak, yanlış ve boş işlere dalmış kimse"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"asılsız ve yanlış düşünceler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini doğru yoldan saptırmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir kimseyi sapmış saymak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yanlışlığın ve sapmanın içine düşülen yer"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yolun bulunamadığı şaşırtıcı arazi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"o işi yanlış ve sağduyusuz bir tutumla yapmak"}],"lexicalization_note":"Tanım yalın sapma çekirdeğini korur; yol, arazi, kişiyi sapmış sayma ve bir işi yanlış tutumla yapma gibi kalıba bağlı kullanımları ayrı yüzler olarak sınırlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en güçlü karşıtlık ve sınır karışıklıkları seçildi, yalnızca ortak konuya dayanan ya da seçilen ayrımları yineleyen adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal uygun doğrultudan uzaklaşmayı, komşu dal ise o doğrultuyu bulup izlemeyi veya göstermeyi anlatır.","focus_only":"Doğru yön ve amaçtan ayrılmayı bildirir.","gloss":"sapma ile doğru yönü bulma karşıtlığı","neighbor_only":"Doğru yönü bulmayı, o yönde ilerlemeyi ve başkasına yol göstermeyi bildirir.","neighbor_ref":"root_000565/B001","relation_type":"antonym","shared_zone":"İki dal da yön, amaç ve doğruluk ekseninde kişinin konumunu anlatır."},{"boundary_match":"partial","distinction":"Odak dal yön ve amaçtan ayrılmayı daha geniş kurarken komşu dal bilgisizlik ve yanlışta derinleşme tonunu belirginleştirir.","focus_only":"Gerçek bir yolda yön bulamamayı ve amaçtan sapmayı da kapsar.","gloss":"sapma ile yanlışta koyulaşma","neighbor_only":"Bilgisizliği, yanlışta koyulaşmayı ve yanlış yola sürüklemeyi özellikle öne çıkarır.","neighbor_ref":"root_001116/B001","relation_type":"near_synonym","shared_zone":"Her iki dal doğruluktan uzaklaşma ve yanlış olana yönelme alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Hata tek bir eylem veya yargının yanlış çıkması olabilir; odak dal ise kişinin yöneldiği doğrultunun bozulmasını anlatır.","focus_only":"Süreğen yön, amaç veya doğruluk kaybını ve başkasını saptırmayı kapsar.","gloss":"sapma ile hata yapma","neighbor_only":"Bir eylemin istenen sonuca uymadan, çoğu kez istemsiz biçimde yanlış gerçekleşmesini kapsar.","neighbor_ref":"root_000420/B001","relation_type":"near_neighbor","shared_zone":"İki dal da doğru olanı tutturamama sonucunda kesişir."},{"boundary_match":"partial","distinction":"Odak dal yönsel ayrılmayı düşünce ve davranış alanına taşır; komşu dalın çekirdeği ise doğrultudan yana eğilmedir.","focus_only":"Yol bulamamayı, yanlış ve boş olana yönelmeyi ve başkasını saptırmayı kapsar.","gloss":"sapma ile yana eğilme","neighbor_only":"Doğrultudan yana doğru eğilme veya salınma biçimindeki hareketi öne çıkarır.","neighbor_ref":"root_000658/B001","relation_type":"near_synonym","shared_zone":"Her iki dal düz veya doğru kabul edilen doğrultudan ayrılmayı anlatır."}],"source_phrase_ar":"كل جائر عن القصد ضال؛ الضلال والضلالة بمعنى (maqayis); ضل إذا جار عن القصد؛ لا يوفق لخير صاحب غوايات وبطالات (ayn); الضلال ضد الهدى؛ ضل في الأمر إذا لم يهتد له؛ ضل في الأرض إذا لم يهتد للسبيل (jamhara); الضلال والضلالة ضد الرشاد؛ رجل ضليل ومضلل أي ضال جدا (sihah); الإضلال في كلام العرب ضد الهداية والإرشاد؛ ضل الكافر غاب عن الحجة؛ ضل فلان عن القصد إذا جار (tahdhib)","source_summary":"Ortak anlatım, doğru yönün ve amacın dışına çıkmayı doğruluk ve kılavuzluk karşıtı bir durum olarak verir; yol bulamama, yoğun sapma, yanlış işlere dalma ve başkasını saptırma bu alan içinde yer alır.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"الجور عن القصد وترك الهدى والرشد والوقوع في الغواية والباطل والتيه عن الطريق","what_is_not_ar":"ليس خصوص الغيبوبة والخفاء ولا خصوص النسيان ولا خصوص الضالّة من الإبل"},"support_links":["sup_700eab952f67d317e573","sup_a2c64243a9915c58da2b"]},{"boundary":"Burada belirleyici olan görünmez hale gelmedir; sahibinden yitme, yerini bulamama ve bellekte tutamama ayrı dallara aittir.","branch_kind":"mixed_non_bare","branch_ref":"root_000913/B002","candidate_links":[{"candidate_id":"cand_2ad3883413768226114c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَضْلِيل","morph_features":"STEM|POS:N|VN|(II)|LEM:taDoliyl|ROOT:Dll|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:5:1","qac_word_ref":"105:2:5","surface_ar":"تَضْلِيلٍ"}],"gloss":"gizlenerek, karışıp eriyerek veya gömülerek gözden yitme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin gizlenmesi ve algılanamaz biçimde gözden yitmesi temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir sıvının başka bir sıvı içinde eriyip seçilemez hale gelmesi özel bir gerçekleşmedir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ölüyü toprağa gömerek gözden kaldırmak, görünmez kılma sonucuna dayanan ettirgen kullanımdır."}}],"root_ar":"ض ل ل","root_id":"root_000913","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın genel görünmez olma çekirdeğini, madde içinde seçilemez hale gelmeyi ve gömme kullanımını birlikte karşılar.","boundary_detail":"Burada belirleyici olan görünmez hale gelmedir; sahibinden yitme, yerini bulamama ve bellekte tutamama ayrı dallara aittir.","branch_image_ar":"الغيبوبة والخفاء","concept_gloss":"gizlenerek, karışıp eriyerek veya gömülerek gözden yitme","contextual_glosses":[{"applicability":"Bir şeyin gizlenip artık görünmez olduğu genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıvı içinde erime biçimini ve ölüyü gömen ettirgen kullanımı açıkça göstermez.","preserves":"Görünür alandan çıkıp algılanamaz olma çekirdeğini korur."},"facet_ids":["F001"],"text":"gözden yitmek","usage_role":"general"},{"applicability":"Bir sıvının başka bir sıvıya karışarak seçilemez hale geldiği bağlama özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel gizlenmeyi ve gömme kullanımını kapsamaz.","preserves":"Bir madde içinde tüketilip seçilemez hale gelme sonucunu korur."},"facet_ids":["F002"],"text":"içinde eriyip kaybolmak","usage_role":"contextual"},{"applicability":"Bir ölünün toprağa verilerek görünmez kılındığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kendiliğinden gizlenme ve başka bir madde içinde erime anlamlarını dışarıda bırakır.","preserves":"Gömme yoluyla görünmez kılma ilişkisini korur."},"facet_ids":["F003"],"text":"gömüp gözden kaldırmak","usage_role":"contextual"}],"definition":"Bir şeyin gizlenerek, toprağa karışarak ya da başka bir maddenin içinde seçilemez hale gelerek gözden yitmesidir. Ölüyü gömmek, onu görünmez kılan özel bir ettirgen kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin gizlenmesi ve algılanamaz biçimde gözden yitmesi temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Bir sıvının başka bir sıvı içinde eriyip seçilemez hale gelmesi özel bir gerçekleşmedir."},{"facet_id":"F003","role":"associated_use","statement":"Ölüyü toprağa gömerek gözden kaldırmak, görünmez kılma sonucuna dayanan ettirgen kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sahibinden yitme, yerini bulamama ve ortadan kalkma gibi görünmezlik dışındaki durumları da çağırır.","collision":"Bir şeyi yitirme dalıyla kolayca karışır.","fit":"broadening","loses":null,"preserves":"Bir şeyin artık görülememesi sonucunu korur."},"text":"kaybolmak"}],"identity_rationale":"Kaynak ifadesi doğrudan gizlenme ve gözden yitme çekirdeğini verir; toprağa karışıp görünmez olma, bir sıvı içinde eriyip seçilemez hale gelme ve ölüyü gömme bu çekirdeğin farklı gerçekleşmeleridir. Bu nedenle geçici dal çerçevesi kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"gizlenip gözden kaybolmak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ölüyü gömüp gözden kaldırmak"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir sıvının ötekine karışıp içinde kaybolması"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"kaya altında güneş görmeyen su"}],"lexicalization_note":"Tanım genel gizlenme çekirdeğiyle birlikte yalnız belirli yapılarda görülen sıvı içinde erime ve ölüyü gömme anlamlarını birbirine karıştırmadan belirtir.","neighbor_coverage_note":"Tüm adaylar gözden geçirildi; gizlenme, gömme ve yitirme sınırlarını en açık biçimde gösterenler seçildi, yalnızca uzak konu ortaklığı taşıyanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal nesnenin görünmez hale gelişini, komşu dal ise sahiplik veya konum bilgisinin yitmesini temel alır.","focus_only":"Bir şeyin toprağa veya başka bir maddeye karışarak görünmez hale gelmesini kapsar.","gloss":"gözden yitme ile elden yitirme","neighbor_only":"Bir şeyin sahibinden gitmesini ya da bulunduğu yerin bilinememesini kapsar.","neighbor_ref":"root_000913/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir şeye erişilememesi veya onun bulunamaması sonucunda kesişebilir."},{"boundary_match":"partial","distinction":"Odak dal karışma ve gömülme yoluyla iz bırakmadan yitmeyi öne çıkarırken komşu dal genel olarak göz önünde olmamayı kapsar.","focus_only":"Madde içinde eriyip seçilemez olmayı ve ölünün gömülmesini kapsar.","gloss":"gizlenme ile görünür alandan çıkma","neighbor_only":"Güneşin batması, kişinin ortada olmaması ve bilginin dışında kalma gibi daha geniş görünmezlik durumlarını kapsar.","neighbor_ref":"root_001117/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyin gözden ve kimi kullanımlarda bilgiden uzak kalmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal gömmenin doğurduğu görünmezlik sonucunu anlatır; komşu dalın çekirdeği toprağı nesnenin üzerine yığma eylemidir.","focus_only":"Gizlenme ve madde içinde seçilemez olma gibi gömmeden bağımsız durumları da kapsar.","gloss":"görünmez olma ile gömme","neighbor_only":"Üzerine toprak yığma ve toprağı bastırma eylemini kendi başına belirtir.","neighbor_ref":"root_000482/B003","relation_type":"near_neighbor","shared_zone":"Ölünün toprağa verilmesi bağlamında iki dal aynı olaya katılır."},{"boundary_match":"partial","distinction":"Odak dal görünürlük ve seçilebilirlik kaybına dayanır; komşu dal ise şeyin yokluğu veya elden çıkması üzerinde durur.","focus_only":"Bir şeyin başka bir şey içinde gizlenip seçilemez hale gelmesini kapsar.","gloss":"gizlenme ile yokluk","neighbor_only":"Önceden var veya hazır olan bir şeyin artık elde ya da mevcut olmamasını kapsar.","neighbor_ref":"root_001168/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal daha önce erişilebilir olan bir şeyin artık bulunamaması sonucunda yaklaşır."}],"source_phrase_ar":"أضل الميت إذا دفن؛ ضل اللبن في الماء ثم استهلك (maqayis); ضل الشيء إذا خفي وغاب؛ أئذا ضللنا في الأرض أي خفينا وغبنا (jamhara); أضل الميت إذا دفن؛ أضل عنه أي أخفى عليه وأغيب؛ أئذا ضللنا في الأرض أي خفينا وغبنا (sihah); أصل الضلال الغيبوبة؛ ضل الماء في اللبن؛ أضلت بنو قيس عميدها أي دفنته (tahdhib)","source_summary":"Ortak anlatım, bir şeyin görünür alandan çıkıp gizlenmesini temel alır; toprağa karışıp seçilemez olma, sıvı içinde erime ve ölünün gömülerek görünmez kılınması bu çekirdeğe bağlanır. Bir şeyi bir başkasından gizleyip uzak tutma da aynı ettirgen sonuçla açıklanır.","sources":["MQ","JA","SI","TA"],"what_is_ar":"خفاء الشيء وغيبوبته واندثاره في غيره أو في الأرض ودفن الميت حتى يغيب","what_is_not_ar":"ليس الجور عن الهدى ولا نسيان الحفظ ولا الضالّة المملوكة"},"support_links":["sup_42d4c5fd159c0d49ffad"]},{"boundary":"Bu dal nesnenin görünmez oluşunu veya bellekteki bilginin silinmesini değil, elden çıkmayı ve yerini bulamamayı temel alır.","branch_kind":"mixed_non_bare","branch_ref":"root_000913/B003","candidate_links":[{"candidate_id":"cand_69fbd896ba3111dec9f5","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَضْلِيل","morph_features":"STEM|POS:N|VN|(II)|LEM:taDoliyl|ROOT:Dll|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:5:1","qac_word_ref":"105:2:5","surface_ar":"تَضْلِيلٍ"}],"gloss":"bir şeyi yitirme veya yerini bulamama; özel olarak kanın karşılıksız kalması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin sahibinden gitmesi ve nerede olduğunun bilinememesi temel yitirme ilişkisidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ev, ibadet yeri veya başka sabit bir yerin konumuna ulaşamamak, nesneyi değil yolu bulamama biçimidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir işin elden kaçması ve ona erişecek yolun bulunamaması, yitirme ilişkisinin soyut uzantısıdır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Öldürülen kişinin kanının öç alınmadan kalması, kaybı karşılıksız kalma sonucuna bağlayan özel kullanımdır."}}],"root_ar":"ض ل ل","root_id":"root_000913","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın sahiplikten çıkma, konuma ulaşamama ve kanın öçsüz kalması yüzlerini birlikte açıklar.","boundary_detail":"Bu dal nesnenin görünmez oluşunu veya bellekteki bilginin silinmesini değil, elden çıkmayı ve yerini bulamamayı temel alır.","branch_image_ar":"فقدان الشيء","concept_gloss":"bir şeyi yitirme veya yerini bulamama; özel olarak kanın karşılıksız kalması","contextual_glosses":[{"applicability":"Bir hayvanın veya başka bir şeyin sahibinin elinden çıktığı ve yerinin bilinmediği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sabit bir yerin yolunu bulamama, işin elden kaçması ve kanın öçsüz kalması yüzlerini açıkça vermez.","preserves":"Bir şeyin elden çıkması ve yerinin bilinememesi çekirdeğini korur."},"facet_ids":["F001"],"text":"kaybetmek","usage_role":"general"},{"applicability":"Ev, ibadet yeri veya başka sabit bir konuma nasıl ulaşılacağının bilinmediği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir nesnenin sahibinden gitmesini, soyut işi ve karşılıksız kalan kanı kapsamaz.","preserves":"Sabit bir konuma ulaşamama unsurunu korur."},"facet_ids":["F002"],"text":"yerini bulamamak","usage_role":"contextual"},{"applicability":"Öldürülen bir kimse için öç veya başka bir karşılık alınmadığı özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesne kaybını, konum bulamamayı ve işin elden kaçmasını dışarıda bırakır.","preserves":"Öldürülen kişinin kanının karşılıksız kalması sonucunu korur."},"facet_ids":["F004"],"text":"kanı yerde kalmak","usage_role":"contextual"}],"definition":"Bir şeyin sahibinin elinden çıkması veya kişinin hareketli bir şeyi ya da sabit bir yerin konumunu bulamamasıdır. Özel bir kullanımda öldürülen kişinin kanı öç alınmadan ve karşılık aranmadan kalır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin sahibinden gitmesi ve nerede olduğunun bilinememesi temel yitirme ilişkisidir."},{"facet_id":"F002","role":"specialization","statement":"Ev, ibadet yeri veya başka sabit bir yerin konumuna ulaşamamak, nesneyi değil yolu bulamama biçimidir."},{"facet_id":"F003","role":"extension","statement":"Bir işin elden kaçması ve ona erişecek yolun bulunamaması, yitirme ilişkisinin soyut uzantısıdır."},{"facet_id":"F004","role":"associated_use","statement":"Öldürülen kişinin kanının öç alınmadan kalması, kaybı karşılıksız kalma sonucuna bağlayan özel kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Şeyin bütünüyle varlıktan kalktığı anlamını gereksiz biçimde öne çıkarır.","collision":"Gözden yitme dalıyla da karışabilir.","fit":"displacement","loses":"Sahiplik ilişkisini, konumun bilinememesini ve kanın karşılıksız kalması kullanımını kaybeder.","preserves":"Bir şeyin artık elde bulunmaması sonucunu kısmen korur."},"text":"yok olmak"}],"identity_rationale":"Kaynak ifadesi, hareketli bir şeyin sahibinden gitmesini ve sabit bir yerin konumuna ulaşamamayı aynı bulamama alanında toplar. Kanın öçsüz kalması ise kaybın sahiplik değil karşılık ve talep bakımından kurulduğu özel, kalıba bağlı bir uzantıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bir şeyin kaybolması, yitip gitmesi veya yok olması"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"devesini ya da başka bir hayvanını kaybetmek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"evin, ibadet yerinin ya da başka bir yerin konumunu bulamamak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bir işin elinden kaçması ve ona güç yetirememek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kanı yerde kalmak, öcü alınmamak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yitme veya yok olma"}],"lexicalization_note":"Tanım genel yitirme çekirdeğini, hareketli bir şeyi kaybetme, sabit bir yerin konumunu bulamama ve kanın karşılıksız kalması gibi yapıya bağlı yüzlerden ayırır.","neighbor_coverage_note":"Adayların tamamı karşılaştırıldı; genel yitirme, görünmez olma ve öçsüz kan ayrımlarını keskinleştirenler seçildi, yalnızca uzak çağrışım taşıyanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sahiplik ve konum ilişkilerini özel olarak kurar; komşu dal bir şeyin sonradan yokluğunu daha genel biçimde anlatır.","focus_only":"Sabit bir yerin konumunu bulamamayı ve kanın öçsüz kalmasını kapsar.","gloss":"yitirme ile bulunmayış","neighbor_only":"Önceden var olan bir şeyin yokluğu ve bulunmayışı üzerinde daha genel biçimde durur.","neighbor_ref":"root_001168/B001","relation_type":"near_synonym","shared_zone":"Her iki dal daha önce elde veya erişilebilir olan bir şeyin artık bulunmamasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal sahiplik ve yer bilgisi kaybına, komşu dal ise nesnenin görünmez ve seçilemez hale gelmesine dayanır.","focus_only":"Bir şeyin sahibinden gitmesini veya konumunun bulunamamasını kapsar.","gloss":"elden yitirme ile gözden yitme","neighbor_only":"Bir şeyin toprağa ya da başka bir maddeye karışarak görünmez olmasını kapsar.","neighbor_ref":"root_000913/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal bir şeyin artık erişilebilir veya bulunabilir olmaması sonucunda kesişir."},{"boundary_match":"partial","distinction":"Odak dalda kanın karşılıksız kalması özel bir uzantıdır; komşu dal yalnızca bu hukuk ve öç durumunu merkez alır.","focus_only":"Hayvan, nesne ve yer kaybını da kapsayan daha geniş bir yitirme alanına sahiptir.","gloss":"öçsüz kalan kan","neighbor_only":"Öldürmenin ardından ne öç ne de bedel alınmasını kan bağlamının çekirdeği olarak kurar.","neighbor_ref":"root_000127/B006","relation_type":"near_neighbor","shared_zone":"İki dal, öldürülen kişinin kanı için karşılık alınmaması kullanımında doğrudan buluşur."}],"source_phrase_ar":"أضللت بعيري إذا ذهب منك؛ ضللت المسجد والدار إذا لم تهتد لهما (maqayis); ضللت مكاني إذا لم تهتد له؛ أضل بعيره إذا أفلت فذهب (ayn); ذهب فلان ضلة إذا لم يدر أين ذهب؛ ذهب دمه ضلة إذا لم يثأر به (jamhara); أضللت بعيري إذا ذهب منك؛ ضللت المسجد والدار إذا لم تعرف موضعهما (sihah); أضللت الشيء إذا ضاع منك؛ ضللت الشيء أضله إذا جعلته في مكان ولم تدر أين هو (tahdhib)","source_summary":"Ortak anlatım, bir hayvanın veya başka bir şeyin sahibinden gitmesini, bir kimsenin nereye gittiğinin bilinememesini ve kişinin sabit bir yerin konumunu bulamamasını aynı erişememe alanında birleştirir; işin elden kaçması ve kanın öçsüz kalması özel uzantılardır.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"ذهاب الشيء من صاحبه أو عدم الاهتداء إلى موضعه في المتحرك والثابت والمكان وذهاب الدم بلا ثأر","what_is_not_ar":"ليس الضلال عن الرشاد في نفسه ولا الغيبوبة المحضة ولا النسيان"},"support_links":["sup_7981bcc602ead38ea3eb"]},{"boundary":"Dal yalnızca belirtilen unutma yapısına bağlıdır; fiziksel yitirme, görünmez olma veya doğruluktan sapma anlamına genellenemez.","branch_kind":"collocation","branch_ref":"root_000913/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَضْلِيل","morph_features":"STEM|POS:N|VN|(II)|LEM:taDoliyl|ROOT:Dll|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:5:1","qac_word_ref":"105:2:5","surface_ar":"تَضْلِيلٍ"}],"gloss":"bir şeyi unutmak veya bellekte tutamamak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin bilgisinin bellekten uzaklaşması ve gerektiğinde hatırlanamaması temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir tanığın bildiğini belleğinde tutamaması, genel unutma ilişkisinin belirli bir uygulamasıdır."}}],"root_ar":"ض ل ل","root_id":"root_000913","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca bir bilginin bellekten uzaklaşmasını bildiren yapıya bağlı dalı tam olarak karşılar.","boundary_detail":"Dal yalnızca belirtilen unutma yapısına bağlıdır; fiziksel yitirme, görünmez olma veya doğruluktan sapma anlamına genellenemez.","branch_image_ar":"ضياع الحفظ","concept_gloss":"bir şeyi unutmak veya bellekte tutamamak","contextual_glosses":[{"applicability":"Bir şeyin bilgisinin artık hatırlanamadığı sıradan bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir bilginin bellekten uzaklaşıp hatırlanamaması anlamını eksiksiz korur."},"facet_ids":["F001","F002"],"text":"unutmak","usage_role":"general"},{"applicability":"Bilginin bellekte korunamadığını ve gerektiğinde geri getirilemediğini açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bellekte koruma ve hatırlama başarısızlığını birlikte korur."},"facet_ids":["F001","F002"],"text":"aklında tutamamak","usage_role":"explanatory"}],"definition":"Bir şeyi unutmak, yani onun bilgisini bellekte hazır tutamamak veya gerektiğinde hatırlayamamaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin bilgisinin bellekten uzaklaşması ve gerektiğinde hatırlanamaması temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Bir tanığın bildiğini belleğinde tutamaması, genel unutma ilişkisinin belirli bir uygulamasıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Fiziksel bir nesnenin elden çıkması veya yerinin bilinmemesi anlamını getirir.","collision":"Fiziksel yitirme dalıyla karışır.","fit":"displacement","loses":"Bellek ve hatırlama ilişkisini bütünüyle siler.","preserves":"Bir şeye artık erişememe sonucunu çok genel düzeyde korur."},"text":"kaybetmek"}],"identity_rationale":"Kaynak ifadesi açıkça bir şeyi unutmayı ve bilginin bellekte hazır bulunmamasını bildirir. Bu çerçeve, fiziksel nesnenin kaybından veya yolun bulunamamasından farklı olarak zihinsel korumanın kesilmesine dayanır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir şeyi unutmak ya da belleğinde tutamamak"}],"lexicalization_note":"Tanım, anlamı bir şeyi unutma ve bellekte tutamama yapısına bağlar; bunu yalın kökün genel anlamı gibi sunmaz.","neighbor_coverage_note":"Tüm komşular değerlendirildi; en yakın unutma eşdeğeri, iki açık karşıt ve fiziksel yitirme sınırı seçildi, daha uzak bilgi ve dikkat adayları dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir nesneyi unutma yapısıyla sınırlıdır; komşu dal unutmayı daha bağımsız bir anlam ve kişi niteliği olarak sunar.","focus_only":"Belirli bir şeyi unutma yapısına ve tanığın bellekte tutamaması uygulamasına bağlıdır.","gloss":"unutma ile unutkanlık","neighbor_only":"Unutkanlığı yalın anlam olarak ve aklı yerinde olmayan kişiye uzanan bir nitelemeyle kapsar.","neighbor_ref":"root_000055/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bilginin bellekten uzaklaşması ve hatırlanamaması çekirdeğinde örtüşür."},{"boundary_match":"opposed","distinction":"Odak dal bilginin hazır olmayışını, komşu dal ise korunmasını veya yeniden hatırlanmasını anlatır.","focus_only":"Bilginin bellekten uzaklaşıp geri getirilememesini bildirir.","gloss":"unutma ile hatırlama karşıtlığı","neighbor_only":"Bilginin bellekte tutulmasını veya unutulduktan sonra yeniden hazır hale getirilmesini bildirir.","neighbor_ref":"root_000516/B003","relation_type":"antonym","shared_zone":"İki dal aynı bilginin bellekte hazır olup olmaması eksenini paylaşır."},{"boundary_match":"opposed","distinction":"Odak dal korumanın başarısızlığını, komşu dal ise bilginin zihinde sabit ve erişilebilir kalmasını anlatır.","focus_only":"Bellekteki içeriğin yitmesini ve gerektiğinde bulunamamasını bildirir.","gloss":"unutma ile bellekte koruma","neighbor_only":"İçeriğin bellekte sağlam biçimde tutulmasını ve öğrenilmiş olarak korunmasını bildirir.","neighbor_ref":"root_000342/B002","relation_type":"antonym","shared_zone":"Her iki dal bilginin bellekte korunma durumunu konu edinir."},{"boundary_match":"partial","distinction":"Odak dal zihinsel koruma ve hatırlamaya, komşu dal ise sahiplik ve konum bilgisine dayanır.","focus_only":"Bilginin bellekte bulunmamasını ve hatırlanamamasını kapsar.","gloss":"bellekte yitirme ile fiziksel yitirme","neighbor_only":"Fiziksel bir şeyin elden gitmesini veya bir konumun bulunamamasını kapsar.","neighbor_ref":"root_000913/B003","relation_type":"near_neighbor","shared_zone":"İki dal kişinin aradığı şeye erişememesi sonucunda benzeşir."}],"source_phrase_ar":"ضللت الشيء أنسيته (jamhara); إن تضل أي إن تنس؛ أن تضل إحداهما أي تغيب عن حفظها أو يغيب حفظها عنها (tahdhib)","source_summary":"Ortak içerik bir şeyi unutmayı, bilginin bellekten uzak kalması veya belleğin o bilgiyi hazır tutamaması biçiminde açıklar.","sources":["JA","TA"],"what_is_ar":"نسيان الشيء وغياب الحفظ عن صاحبه أو غياب الشيء عن الحفظ","what_is_not_ar":"ليس فقدان الموضع ولا الجور عن القصد ولا الخفاء الحسي"},"support_links":[]},{"boundary":"Anlam herhangi bir kayıp şeyi değil, sahibinden ayrılmış ve sahibi bilinmeyen hayvanı kapsar; deve en belirgin uygulamadır.","branch_kind":"bare","branch_ref":"root_000913/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَضْلِيل","morph_features":"STEM|POS:N|VN|(II)|LEM:taDoliyl|ROOT:Dll|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:5:1","qac_word_ref":"105:2:5","surface_ar":"تَضْلِيلٍ"}],"gloss":"sahibi bilinmeyen kayıp hayvan, özellikle deve","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sahibinden ayrılmış ve sahibinin kim olduğu bilinmeyen kayıp hayvanı adlandırır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Deve, bu hayvan adının özellikle belirtilen ve öne çıkan uygulamasıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adlandırma hayvanın erkek veya dişi oluşuna göre değişmez ve her iki cinsi de kapsar."}}],"root_ar":"ض ل ل","root_id":"root_000913","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın sahibinden ayrıldığı, sahibinin bilinmediği ve devenin başlıca örnek olduğu adlandırmayı karşılar.","boundary_detail":"Anlam herhangi bir kayıp şeyi değil, sahibinden ayrılmış ve sahibi bilinmeyen hayvanı kapsar; deve en belirgin uygulamadır.","branch_image_ar":"الضالّة في المضيعة","concept_gloss":"sahibi bilinmeyen kayıp hayvan, özellikle deve","contextual_glosses":[{"applicability":"Türü belirtilmeyen, sahibinden ayrılmış ve sahibinin kim olduğu bilinmeyen hayvan için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan olma, kayıp bulunma ve sahibinin bilinmeme koşullarını birlikte korur."},"facet_ids":["F001","F003"],"text":"sahibi bilinmeyen kayıp hayvan","usage_role":"general"},{"applicability":"Kayıp hayvanın özellikle deve olduğu bağlamlarda daha kesin karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deve dışındaki hayvanlara uzanan genel kapsamı dışarıda bırakır.","preserves":"Sahibi bilinmeyen kayıp hayvan koşullarını ve deve uygulamasını korur."},"facet_ids":["F001","F002","F003"],"text":"sahibi bilinmeyen kayıp deve","usage_role":"contextual"}],"definition":"Sahibinden ayrılmış, ortada kalmış ve sahibinin kim olduğu bilinmeyen hayvandır; özellikle deve için kullanılır ve hayvanın erkek ya da dişi olması adı değiştirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sahibinden ayrılmış ve sahibinin kim olduğu bilinmeyen kayıp hayvanı adlandırır."},{"facet_id":"F002","role":"specialization","statement":"Deve, bu hayvan adının özellikle belirtilen ve öne çıkan uygulamasıdır."},{"facet_id":"F003","role":"source_variant","statement":"Adlandırma hayvanın erkek veya dişi oluşuna göre değişmez ve her iki cinsi de kapsar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sahibi bilinen fakat serbest bırakılmış veya sahipsiz doğmuş hayvanları da kapsayabilir.","collision":"Kayıp olma ve sahibinin bilinmeme koşullarını belirsizleştirir.","fit":"broadening","loses":null,"preserves":"Hayvanın gözetimsiz ve sahibinden ayrı bulunması durumunu korur."},"text":"başıboş hayvan"}],"identity_rationale":"Kaynak ifadesi, sahibinin kim olduğu bilinmeyen kayıp hayvanı, özellikle deveyi adlandırır ve adın erkek ile dişi için aynı biçimde kullanılabildiğini belirtir. Bu nedenle dal genel kayıp olayını değil, belirli durumdaki hayvanı gösteren adlandırmayı temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"sahibi bilinmeyen kayıp hayvan, özellikle deve"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"sahibi bilinmeyen kayıp hayvanlar veya develer"}],"lexicalization_note":"Tanım, yalın adın sahibi bilinmeyen kayıp hayvanı gösteren kapsamını verir ve bunu genel yitirme olayına genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kayıp hayvan adını kaybetme olayından ve genel deve adlarından ayıran komşular seçildi, yalnızca başka deve niteliklerini paylaşan uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kayıp durumundaki hayvanın adıdır; komşu dal ise sahibin yaşadığı yitirme ilişkisini veya bulamama olayını anlatır.","focus_only":"Kayıp ve sahibi bilinmeyen hayvanı bir varlık türü olarak adlandırır.","gloss":"kayıp hayvan ile kaybetme olayı","neighbor_only":"Bir hayvanı ya da başka bir şeyi kaybetme olayını ve yer bulamama durumunu anlatır.","neighbor_ref":"root_000913/B003","relation_type":"near_neighbor","shared_zone":"İki dal sahibinden ayrılmış ve yeri bilinmeyen hayvan bağlamında doğrudan kesişir."},{"boundary_match":"field_only","distinction":"Odak dal devenin kayıp ve sahibi bilinmeyen durumda olmasını gerektirir; komşu dal yalnızca hayvan türünü adlandırır.","focus_only":"Hayvanın kayıp olması ve sahibinin bilinmemesi koşullarını getirir.","gloss":"kayıp deve ile genel deve adı","neighbor_only":"Deveyi cinsiyet ve kayıp durumundan bağımsız bir hayvan adı olarak gösterir.","neighbor_ref":"root_000132/B001","relation_type":"same_field","shared_zone":"İki dal özellikle deveyi gösterebilir."},{"boundary_match":"field_only","distinction":"Odak dal sahibinden ayrılmış hayvanın özel durum adıdır; komşu dal deveyi ve onun toplu bakım alanını genel olarak anlatır.","focus_only":"Tek bir kayıp hayvanı sahibinin bilinmemesi durumuyla niteler.","gloss":"kayıp hayvan ile deve topluluğu","neighbor_only":"Develeri topluluk, sürü, çokluk, sahiplik ve bakım alanlarıyla birlikte kapsar.","neighbor_ref":"root_000006/B001","relation_type":"same_field","shared_zone":"Her iki dal deve ve hayvancılık alanında yer alır."}],"source_phrase_ar":"الضالة من الإبل ما يبقى بمضيعة لا يعرف ربها الذكر والأنثى فيه سواء (ayn); الضالة ما ضل من البهيمة للذكر والأنثى (sihah); الضالة من الإبل التي بمضيعة لا يعرف لها مالك؛ الجميع الضوال (tahdhib)","source_summary":"Ortak tanım, sahibinden ayrılıp ortada kalmış ve sahibi bilinmeyen hayvanı, özellikle deveyi adlandırır; ad erkek ve dişi hayvan için aynıdır ve çoğul biçimi de belirtilir.","sources":["AY","SI","TA"],"what_is_ar":"البهيمة ولا سيما الإبل إذا بقيت في مضيعة لا يعرف ربها والذكر والأنثى فيها سواء","what_is_not_ar":"ليس كل ضياع ولا كل ضلال عن الهدى بل اسم مخصوص للحيوان الضائع"},"support_links":[]},{"boundary":"Anlam genel ve yalındır; belirli bir amaç, nesne türü ya da kalıpla sınırlı değildir.","branch_kind":"bare","branch_ref":"root_001334/B001","candidate_links":[{"candidate_id":"cand_69fbd896ba3111dec9f5","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَيْد","morph_features":"STEM|POS:N|LEM:kayod|ROOT:kyd|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:3:1","qac_word_ref":"105:2:3","surface_ar":"كَيْدَ"}],"gloss":"bir şeyi yoğun çabayla işleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey, sıradan bir dokunuşla değil, yoğun çaba ve uğraşla ele alınıp işlenir."}}],"root_ar":"ك ي د","root_id":"root_001334","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesne veya iş üzerinde ısrarlı ve güçlü biçimde uğraşmayı anlatan genel kullanıma uygundur.","boundary_detail":"Anlam genel ve yalındır; belirli bir amaç, nesne türü ya da kalıpla sınırlı değildir.","branch_image_ar":"معالجة الشيء بشدة","concept_gloss":"bir şeyi yoğun çabayla işleme","contextual_glosses":[{"applicability":"Eylemin nesnesi ve bağlamı belli olduğunda akıcı bir metin içi karşılık olarak kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uğraşmayı ve nesne üzerinde etkin işlem yapmayı korur."},"facet_ids":["F001"],"text":"uğraşarak işlemek","usage_role":"contextual"}],"definition":"Bir şeyi yoğun çaba harcayarak ele almak, onun üzerinde uğraşmak ve onu işlemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey, sıradan bir dokunuşla değil, yoğun çaba ve uğraşla ele alınıp işlenir."}],"identity_rationale":"Kaynak ifadesi, anlamı bir şeyi yoğun çaba göstererek ele alma, onunla uğraşma ve onu işleme olarak kurar. Bu çekirdek anlam aldatma, savaş veya başka özel kullanımlarla sınırlandırılmamıştır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi yoğun çabayla işleme ve onunla uğraşma"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"onu yoğun çabayla ele alıp işlemek"}],"lexicalization_note":"Tanım yalın kullanımı karşılar ve öteki dallardaki kalıba bağlı özel anlamları bu dala taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanmayanlar genel çaba alanını yineliyor, daha uzak bir uygulama alanında kalıyor ya da öteki kök içi dallarla yalnızca konu bağı kuruyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel yoğun uğraşmayı bildirir; komşu dal ise güçlük taşıyan ve kimi zaman sökme ya da çıkarma sonucu veren işlemlere yönelir.","focus_only":"Bu dal, ele alınan şeyin mutlaka güç ya da belirli türden olmasını gerektirmez.","gloss":"güç bir şeyi işleyip çözme","neighbor_only":"Komşu dal güç bir şeyi çözme, et sıyırma veya tıpa çıkarma gibi özel işlemleri de kapsar.","neighbor_ref":"root_000999/B007","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir şey doğrudan çaba gösterilerek ele alınır ve üzerinde işlem yapılır."},{"boundary_match":"partial","distinction":"Odak dal çabayı bir şeyi ele alıp işleme ilişkisi içinde kurar; komşu dalın çekirdeği ise çabanın kendisidir.","focus_only":"Çabanın belirli bir şey üzerinde işleme ve uğraşma olarak gerçekleşmesini gerektirir.","gloss":"çaba gösterme","neighbor_only":"Çabayı, üzerinde işlem yapılan belirli bir nesne bulunmadan da genel olarak anlatabilir.","neighbor_ref":"root_000076/B010","relation_type":"near_neighbor","shared_zone":"İki dal da güçlü emek ve gayret bileşenini taşır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği yoğun işlemedir; komşu dalın çekirdeği ise bir başkasını dolaylı yollarla etkilemeye yönelik düzen kurmadır.","focus_only":"Aldatma veya gizli amaç olmaksızın bir şeyi yoğun çabayla ele almayı kapsar.","gloss":"yoğun uğraşma ile gizli düzen","neighbor_only":"Birini yönlendirmek ya da alt etmek için gizli ve dolaylı bir düzen kurmayı gerektirir.","neighbor_ref":"root_001334/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir amaca yönelik, tasarlanmış bir uğraş bulunabilir."}],"source_phrase_ar":"يدل على معالجة لشيء بشدة (maqayis)؛ الكيد المعالجة (maqayis)؛ كل شيء تعالجه فأنت تكيده (maqayis;sihah)","source_summary":"Kaynaklar, çekirdeği bir şeyi yoğun biçimde ele alma ve onunla uğraşma olarak ortaklaşa verir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه أصل المعالجة الشديدة للشيء وكل ما يرجع إلى تكلف الشيء ومزاولته بشدة","what_is_not_ar":"ليس مخصوصا بالمكر ولا بالحرب ولا بصيغ كاد الدالة على مقاربة الفعل"},"support_links":["sup_7981bcc602ead38ea3eb"]},{"boundary":"Çekirdek dolaylı ve tasarlanmış yönlendirmedir; yoğun uğraşma tek başına bu anlamı oluşturmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001334/B002","candidate_links":[{"candidate_id":"cand_cd12b0497cfc75141387","lane":"micro"},{"candidate_id":"cand_2ad3883413768226114c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَيْد","morph_features":"STEM|POS:N|LEM:kayod|ROOT:kyd|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:3:1","qac_word_ref":"105:2:3","surface_ar":"كَيْدَ"}],"gloss":"dolaylı ve gizli düzen kurma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da taraf, amacına ulaşmak için dolaylı ve önceden tasarlanmış bir düzen kurar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki taraf birbirini alt etmek amacıyla karşılıklı olarak düzen kurabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir söz içinde, hedefe kötülük etmeye yönelik kesin niyeti anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Başka bir özel kullanımda, kişiye sonunda cezaya varacak biçimde süre tanıyıp onu adım adım sonuca çekmeyi anlatır."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Kurulan düzen amacına ve sonucuna göre kötülenebileceği gibi yerinde de görülebilir."}}],"root_ar":"ك ي د","root_id":"root_001334","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Birini yönlendirme, yanıltma veya alt etme amacıyla tasarlanan genel çekirdeği karşılar.","boundary_detail":"Çekirdek dolaylı ve tasarlanmış yönlendirmedir; yoğun uğraşma tek başına bu anlamı oluşturmaz.","branch_image_ar":"المكيدة والاحتيال","concept_gloss":"dolaylı ve gizli düzen kurma","contextual_glosses":[{"applicability":"Düzenin karşı tarafı yanıltma veya zarara uğratma amacı açık olduğunda doğal bir eylem karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yerinde görülebilen veya doğrudan zarar amacı taşımayan düzenleri dışarıda bırakır.","preserves":"Gizli düzeni ve bir hedefe yönelmeyi korur."},"facet_ids":["F001","F003"],"text":"tuzak kurmak","usage_role":"contextual"},{"applicability":"İki tarafın birbirini alt etmek için karşılıklı olarak gizli planlar kurduğu kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklılığı, tasarlamayı ve üstün gelme amacını korur."},"facet_ids":["F002"],"text":"karşılıklı düzen yarışı","usage_role":"explanatory"},{"applicability":"Süre vermenin görünürde rahatlık sağladığı, fakat kişiyi sonunda cezaya yaklaştırdığı özel söz bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ertelemeyi, aşamalı ilerleyişi ve ceza sonucunu birlikte korur."},"facet_ids":["F004"],"text":"cezaya götüren süre tanıma","usage_role":"explanatory"}],"definition":"Birini yönlendirmek, yanıltmak ya da alt etmek amacıyla açık edilmeyen, dolaylı bir düzen kurmaktır. Bağlama göre bu düzen övülebilir veya yerilebilir; karşılıklı çekişme, kötülük tasarlama ve cezaya götüren süre tanıma biçimlerinde gerçekleşebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da taraf, amacına ulaşmak için dolaylı ve önceden tasarlanmış bir düzen kurar."},{"facet_id":"F002","role":"extension","statement":"İki taraf birbirini alt etmek amacıyla karşılıklı olarak düzen kurabilir."},{"facet_id":"F003","role":"associated_use","statement":"Belirli bir söz içinde, hedefe kötülük etmeye yönelik kesin niyeti anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Başka bir özel kullanımda, kişiye sonunda cezaya varacak biçimde süre tanıyıp onu adım adım sonuca çekmeyi anlatır."},{"facet_id":"F005","role":"source_variant","statement":"Kurulan düzen amacına ve sonucuna göre kötülenebileceği gibi yerinde de görülebilir."}],"identity_rationale":"Kaynak ifadesi, birini dolaylı yollarla etkilemek için düzen kurma çekirdeğini; karşılıklı düzen kurma, kötülük isteme, adım adım çekme ve cezaya götüren süre tanıma kullanımlarıyla birlikte açıkça destekler. Bu düzen hem kötü hem de yerinde görülen amaçlarla kurulabilir.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"dolaylı düzen ve tuzak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"gizli ve aldatıcı düzen"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"birine tuzak kurmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"karşılıklı tuzak kurma yarışı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"onlara kötülük etmeye kesin karar vermek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"cezaya götüren süre tanıma ve erteleme"}],"lexicalization_note":"Yalın ad ve eylem biçimlerindeki gizli düzen anlamı, belirli söz öbeklerinde kötülük isteme veya cezaya götüren erteleme olarak gerçekleşen özel kullanımlardan ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanmayanlar zararı, ödülü veya genel düşmanlığı sonuç alanında tutuyor, yalnız tek bir tuzak örneğini yineliyor ya da kök içindeki ayrı anlamlarla uzak bağ kuruyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kullanım alanı daha geniştir; komşu dal gizlilik içinde bir şeye ulaşma veya onu alma sonucuna daha sıkı bağlıdır.","focus_only":"Yerinde görülebilen düzenleri, karşılıklı düzen yarışını ve cezaya götüren ertelemeyi de kapsayabilir.","gloss":"gizli yoldan amaca ulaşma","neighbor_only":"Bir şeye gizlice ulaşma veya onu ele geçirme yönünü özellikle öne çıkarır.","neighbor_ref":"root_000021/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da amaca dolaylı ve gizli bir düzen yoluyla ulaşmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dal gizli düzen çekirdeğinde kalırken komşu dal karşılıklı düşmanlık ve çekişme alanını daha belirgin biçimde içerir.","focus_only":"Cezaya götüren süre tanıma ve kötülük isteme gibi özel gerçekleşmeleri içerir.","gloss":"düzen kurma ve çekişme","neighbor_only":"Düşmanlık, çekişme ve haklı ya da haksız karşı koyma alanına açıkça uzanır.","neighbor_ref":"root_001402/B003","relation_type":"near_synonym","shared_zone":"İki dal da karşı tarafı dolaylı yollarla alt etmeye yönelik düzen kurmayı kapsar."},{"boundary_match":"partial","distinction":"Odak dal her türlü dolaylı düzeni kapsar; komşu dal özellikle söylenen veya gösterilen ile istenen arasındaki karşıtlığa dayanır.","focus_only":"Gizli niyetin dışarıya ters bir görünüş verilmeden de kurulabildiği daha geniş düzen alanını kapsar.","gloss":"başka görünerek yanıltma","neighbor_only":"Bir şeyi gösterirken başka bir şeyi isteme ve görünüşle niyeti ayırma kalıbına bağlıdır.","neighbor_ref":"root_000439/B008","relation_type":"near_neighbor","shared_zone":"Her iki dalda da gerçek amaç saklanarak karşı tarafın algısı yönlendirilir."}],"source_phrase_ar":"يسمون المكر كيدا (maqayis)؛ الكيد من المكيدة وقد كاده يكيده مكيدة (ayn)؛ الكيد المكر وكاده يكيده كيدا ومكيدة وكذلك المكايدة (sihah)؛ الكيد ضرب من الاحتيال وقد يكون مذموما وممدوحا والاستدراج والمكر (mufradat)؛ لأريدن بها سوءا (mufradat)؛ الإملاء والإمهال المؤدي إلى العقاب (mufradat)","source_summary":"Toplu kaynak anlatımı, dolaylı düzen kurma çekirdeğini paylaşır; bunun karşılıklı yapılabileceğini, kötü ya da yerinde amaç taşıyabileceğini ve bazı bağlamlarda adım adım çekme, kötülük isteme veya cezaya götüren erteleme olarak yorumlandığını belirtir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه المكر والمكيدة والمكايدة والاحتيال والاستدراج وإرادة السوء والإمهال المؤدي إلى العقاب","what_is_not_ar":"ليس مجرد معالجة حسية ولا كاد الموضوعة لمقاربة الفعل"},"support_links":["sup_42d4c5fd159c0d49ffad","sup_700eab952f67d317e573"]},{"boundary":"Anlam yalnız kişiyle ve can verme bağlamıyla kurulan söz öbeğine bağlıdır.","branch_kind":"collocation","branch_ref":"root_001334/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَيْد","morph_features":"STEM|POS:N|LEM:kayod|ROOT:kyd|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:3:1","qac_word_ref":"105:2:3","surface_ar":"كَيْدَ"}],"gloss":"can çekişerek can verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi ölümün son aşamasında canını vermekte ve yaşamı bedenden ayrılmaktadır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak anlatımları aynı süreci canı verme ve ölümün son sıkıntısından geçme yönleriyle ifade eder."}}],"root_ar":"ك ي د","root_id":"root_001334","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız ölümün son aşamasındaki kişi için kullanılan söz öbeğinin bütün çekirdeğini karşılar.","boundary_detail":"Anlam yalnız kişiyle ve can verme bağlamıyla kurulan söz öbeğine bağlıdır.","branch_image_ar":"مكابدة خروج النفس","concept_gloss":"can çekişerek can verme","contextual_glosses":[{"applicability":"Kişinin ölümün son aşamasında bulunduğu bağlamda doğal ve kısa bir metin içi karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin ölmek üzere oluşunu ve son aşamadaki sıkıntılı süreci korur."},"facet_ids":["F001","F002"],"text":"can çekişmek","usage_role":"contextual"}],"definition":"Bir kişinin ölümün son aşamasında can çekişmesi ve canını vermek üzere olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi ölümün son aşamasında canını vermekte ve yaşamı bedenden ayrılmaktadır."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak anlatımları aynı süreci canı verme ve ölümün son sıkıntısından geçme yönleriyle ifade eder."}],"identity_rationale":"Kaynak ifadesi, kişinin canını vermekte oluşunu ve ölümün son aşamasından geçmesini anlatan kalıplaşmış kullanımı destekler. Burada çekirdek, genel bir zorluk değil, ölüm sırasında canın çıkış sürecidir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"can çekişmek ve canını vermek üzere olmak"}],"lexicalization_note":"Tanım yalnız canla kurulan söz öbeğini karşılar; yalın biçime genel ölme veya zorluk anlamı yüklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanmayanlar soluğu, yaşam gücünü, uykuyu veya ölümü başka bir sonuç ve bakış açısından kurduğu için aynı ayrımı yinelemeden ek yarar sağlamaz.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal can verme yönünü kalıba bağlı biçimde kurar; komşu dal ölüm sırasındaki dışa vuran çekişmeyi daha belirginleştirir.","focus_only":"Canın verilmesini belirli bir söz öbeği içinde süreç olarak anlatır.","gloss":"ölümün son çekişmesi","neighbor_only":"Ölüm sırasındaki çekişme ve son nefes belirtilerini daha doğrudan öne çıkarır.","neighbor_ref":"root_001489/B016","relation_type":"near_synonym","shared_zone":"İki dal da ölümün hemen öncesindeki can çekişme sürecini anlatır."},{"boundary_match":"partial","distinction":"Odak dal can verme sürecini, komşu dal ise bu sürecin sonunda kalan son soluk durumunu öne çıkarır.","focus_only":"Canın çıkışını süren bir can çekişme ve can verme olayı olarak anlatır.","gloss":"son soluğunda olma","neighbor_only":"Kişinin yaşamdan kalan en son soluğa ulaştığı durumu bildirir.","neighbor_ref":"root_000186/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal ölümden hemen önceki son yaşam evresine aittir."},{"boundary_match":"partial","distinction":"Odak dal ölmekte olan kişinin sürecine, komşu dal ise ölümün yaşamın alınması olarak kavranmasına odaklanır.","focus_only":"Ölmekte olan kişinin yaşadığı can çekişme sürecini anlatır.","gloss":"yaşamın alınmasıyla ölüm","neighbor_only":"Ölümü, yaşam gücünün alınması veya kişinin alınmış olması sonucu üzerinden kurar.","neighbor_ref":"root_001197/B007","relation_type":"near_neighbor","shared_zone":"İki dal da yaşamın sona ermesini ve canın bedenden ayrılmasını konu edinir."}],"source_phrase_ar":"هو يكيد بنفسه أي يجود بها (maqayis;sihah;mufradat)؛ رأيته يكيد بنفسه أي يسوق سياقا (ayn)","source_summary":"Kaynaklar, kalıbı can çekişme ve canını verme süreci üzerinde birleştirir; anlatım farkı bu son aşamanın hangi yönünün öne çıkarıldığıyla ilgilidir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه قولهم يكيد بنفسه إذا جاد بها أو ساقها سياقا","what_is_not_ar":"ليس مكيدة ولا حربا ولا قيئا"},"support_links":[]},{"boundary":"Anlam, savaşla karşılaşmayı bildiren olumsuz söz kalıbına bağlıdır.","branch_kind":"collocation","branch_ref":"root_001334/B004","candidate_links":[{"candidate_id":"cand_a018f14db3aaf5929f90","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَيْد","morph_features":"STEM|POS:N|LEM:kayod|ROOT:kyd|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:3:1","qac_word_ref":"105:2:3","surface_ar":"كَيْدَ"}],"gloss":"karşılaşılmayan savaş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz kalıbındaki nesne, yola çıkanların karşılaşmadığı savaş veya silahlı çatışmadır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tipik kullanım, sefere çıkıp hiçbir savaşla karşılaşmama durumunu bildirir."}}],"root_ar":"ك ي د","root_id":"root_001334","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sefere çıkan birinin savaşla karşılaşmadığını bildiren kalıba bağlı anlamı eksiksiz karşılar.","boundary_detail":"Anlam, savaşla karşılaşmayı bildiren olumsuz söz kalıbına bağlıdır.","branch_image_ar":"الحرب والقتال","concept_gloss":"karşılaşılmayan savaş","contextual_glosses":[{"applicability":"Özne sefere veya çatışma alanına çıkmışken hiçbir savaş görmediğini anlatan cümlede doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Savaş olayını ve onunla karşılaşılmamasını birlikte korur."},"facet_ids":["F001","F002"],"text":"savaşla karşılaşmamak","usage_role":"contextual"}],"definition":"Sefere ya da çatışmaya çıkan birinin savaşla karşılaşmamasını bildiren kalıpta, karşılaşılması beklenen savaş veya çarpışmadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz kalıbındaki nesne, yola çıkanların karşılaşmadığı savaş veya silahlı çatışmadır."},{"facet_id":"F002","role":"example","statement":"Tipik kullanım, sefere çıkıp hiçbir savaşla karşılaşmama durumunu bildirir."}],"identity_rationale":"Kaynak ifadesi, sefere çıkanların savaşla karşılaşıp karşılaşmadığını bildiren belirli bir kalıpta sözcüğün doğrudan savaş anlamına geldiğini gösterir. Bu, genel gizli düzen anlamıyla birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"savaşla karşılaşmamak"}],"lexicalization_note":"Tanım yalnız savaşla karşılaşmama söz kalıbını kapsar ve yalın biçime genel savaş anlamı vermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanmayanlar düşmanlığı, savaşa direnerek katılmayı, çatışmada kalmayı veya savaşın ölümcül şiddetini öne çıkararak seçilen ayrımları tekrarlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kalıba bağlı ve dar bir savaş karşılığıdır; komşu dal savaş alanını yalın ve daha geniş bir söz varlığıyla kapsar.","focus_only":"Savaş anlamını yalnız karşılaşmama bildiren belirli söz kalıbında taşır.","gloss":"savaş ve düşmanlık","neighbor_only":"Savaşı, savaşmayı, düşmanlığı ve bunlarla ilgili kişi ve yerleri daha geniş biçimde kapsar.","neighbor_ref":"root_000302/B002","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak çekirdeğinde savaş ve silahlı çatışma bulunur."},{"boundary_match":"partial","distinction":"Odak dal karşılaşılması mümkün genel savaşı adlandırır; komşu dal fiilen başlayan ve kızışan çarpışmayı anlatır.","focus_only":"Savaşın gerçekleşmediği karşılaşma bağlamında savaş kavramını adlandırır.","gloss":"kızışmış çarpışma","neighbor_only":"Savaşın kızışmasını, tarafların çarpışmasını ve savaşçı kargaşayı öne çıkarır.","neighbor_ref":"root_001612/B003","relation_type":"near_neighbor","shared_zone":"İki dal da savaş ve karşı karşıya gelen taraflar alanındadır."},{"boundary_match":"partial","distinction":"Odak dal genel savaş kavramını kalıba bağlı olarak verir; komşu dal savaş içindeki saldırı ve karşılıklı çarpışma olayına yönelir.","focus_only":"Savaşın kendisini, onunla karşılaşmama kalıbında nesne olarak kurar.","gloss":"savaşta çarpışma ve saldırı","neighbor_only":"Savaş içindeki çarpışma anını ve bir topluluğun düşmana saldırmasını anlatır.","neighbor_ref":"root_001675/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal savaş alanındaki silahlı karşılaşmayı konu edinir."}],"source_phrase_ar":"الكيد الحرب يقال خرجوا ولم يلقوا كيدا أي حربا (maqayis)؛ ربما سمي الحرب كيدا يقال غزا فلان فلم يلق كيدا (sihah)","source_summary":"Kaynaklar, belirli olumsuz karşılaşma kalıbında sözcüğün savaş veya çarpışma anlamına geldiğinde birleşir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه إطلاق الكيد على الحرب في قولهم لم يلقوا كيدا","what_is_not_ar":"ليس مكرا مجردا ولا معالجة عامة"},"support_links":["sup_a2c64243a9915c58da2b"]},{"boundary":"Anlam karganın sesine ve bu sesi var gücüyle çıkarmasına özgüdür.","branch_kind":"bare","branch_ref":"root_001334/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَيْد","morph_features":"STEM|POS:N|LEM:kayod|ROOT:kyd|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:3:1","qac_word_ref":"105:2:3","surface_ar":"كَيْدَ"}],"gloss":"karganın var gücüyle bağırması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sesi çıkaran kargadır ve ses güçlü bir bağırış biçimindedir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağırış, yoğun çaba harcanarak ve var güçle çıkarılır."}}],"root_ar":"ك ي د","root_id":"root_001334","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karga sesi ile bu sesi çıkarırken gösterilen yoğun çabayı birlikte anlatan kullanıma uygundur.","boundary_detail":"Anlam karganın sesine ve bu sesi var gücüyle çıkarmasına özgüdür.","branch_image_ar":"صياح بجهد","concept_gloss":"karganın var gücüyle bağırması","contextual_glosses":[{"applicability":"Karganın güçlü ve çabalı ses çıkarmasını anlatan akıcı metinlerde kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kargaya özgü sesi ve bu sesin var güçle çıkarılmasını korur."},"facet_ids":["F001","F002"],"text":"var gücüyle gaklamak","usage_role":"contextual"}],"definition":"Karganın sesini çıkarmak için büyük çaba harcayarak var gücüyle bağırmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sesi çıkaran kargadır ve ses güçlü bir bağırış biçimindedir."},{"facet_id":"F002","role":"core","statement":"Bağırış, yoğun çaba harcanarak ve var güçle çıkarılır."}],"identity_rationale":"Kaynak ifadesi, genel bir seslenmeyi değil, karganın büyük çaba harcayarak bağırmasını ve ses çıkarmadaki yoğun uğraşını adlandırır. Tür ve çaba koşulları anlamın kurucu parçalarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"karganın var gücüyle bağırması"}],"lexicalization_note":"Tanım yalın kullanımı karşılar, fakat anlamı bütün yüksek seslere veya başka hayvan seslerine genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanmayanlar başka kuş veya kedi seslerini yineliyor, genel ses ve ıslık alanında kalıyor ya da yalnız ses yükseltme yönünü paylaşıyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal karga ile çaba koşulunu birlikte gerektirir; komşu dal farklı hayvanların yüksek bağırışına yönelir ve çabayı zorunlu kılmaz.","focus_only":"Kargaya ve sesi çıkarmak için harcanan yoğun çabaya özgüdür.","gloss":"hayvanın yüksek sesle bağırması","neighbor_only":"Sığır, boğa ve yaban hayvanlarının yüksek bağırışlarını daha geniş biçimde kapsar.","neighbor_ref":"root_000213/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir hayvanın güçlü ve işitilir biçimde bağırmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal belirli bir kuşun çabalı bağırışıdır; komşu dal türden bağımsız yüksek ses ve çağrı alanıdır.","focus_only":"Sesin kargadan çıkmasını ve yoğun çabayla üretilmesini gerektirir.","gloss":"yüksek ses ve çağrı","neighbor_only":"İnsan çağrısını, seslenmeyi ve sesin uzaklara yayılmasını da kapsar.","neighbor_ref":"root_001486/B002","relation_type":"near_neighbor","shared_zone":"İki dal da yükseltilmiş, belirgin ve güçlü sesi kapsar."},{"boundary_match":"field_only","distinction":"Ortaklık yalnız hayvan sesi alanındadır; sesin sahibi, niteliği ve odak daldaki çaba koşulu farklıdır.","focus_only":"Karganın yoğun çabayla çıkardığı bağırışı anlatır.","gloss":"kedi sesi","neighbor_only":"Kedinin çıkardığı sesi ve miyavlamayı anlatır.","neighbor_ref":"root_000056/B004","relation_type":"same_field","shared_zone":"Her iki dal belirli bir hayvan türünün çıkardığı sesi adlandırır."}],"source_phrase_ar":"صياح الغراب بجهد (maqayis)؛ يسمى اجتهاد العرب في صياحه كيدا (sihah)","source_summary":"Kaynaklar, karganın bağırışını ve bu sesi çıkarmak için gösterdiği yoğun çabayı aynı anlamın parçaları olarak verir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه صياح الغراب بجهد والاجتهاد في الصياح","what_is_not_ar":"ليس مكرا ولا حربا ولا قيئا"},"support_links":[]},{"boundary":"Anlam yalnız çakmak taşı ile kurulan söz öbeğine ve gecikmiş ateş çıkarma olayına bağlıdır.","branch_kind":"collocation","branch_ref":"root_001334/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَيْد","morph_features":"STEM|POS:N|LEM:kayod|ROOT:kyd|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:3:1","qac_word_ref":"105:2:3","surface_ar":"كَيْدَ"}],"gloss":"ateşi yavaş ve güçlükle çıkarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çakmak taşı ateş çıkarır, ancak bu sonuç olağan hızda gerçekleşmez."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ateşin çıkışı yavaş, gecikmeli ve güçlükle olur."}}],"root_ar":"ك ي د","root_id":"root_001334","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çakmak taşının sonunda ateş çıkardığı, fakat bunun gecikmeli ve güç olduğu söz öbeğine uygundur.","boundary_detail":"Anlam yalnız çakmak taşı ile kurulan söz öbeğine ve gecikmiş ateş çıkarma olayına bağlıdır.","branch_image_ar":"إبطاء الزند في النار","concept_gloss":"ateşi yavaş ve güçlükle çıkarma","contextual_glosses":[{"applicability":"Çakmak taşının vurulduktan sonra ancak gecikerek ateş çıkardığı bağlamda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ateş çıkarma sonucunu ve bunun gecikmeli gerçekleşmesini korur."},"facet_ids":["F001","F002"],"text":"gecikerek kıvılcım vermek","usage_role":"contextual"}],"definition":"Çakmak taşının ateşi hemen değil, yavaşça ve güçlükle çıkarmasıdır; gecikmeye rağmen ateş sonunda çıkar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çakmak taşı ateş çıkarır, ancak bu sonuç olağan hızda gerçekleşmez."},{"facet_id":"F002","role":"core","statement":"Ateşin çıkışı yavaş, gecikmeli ve güçlükle olur."}],"identity_rationale":"Kaynak ifadesi, çakmak taşının ateşi hiç çıkarmamasını değil, onu yavaş ve güçlükle çıkarmasını anlatır. Yavaşlık, güçlük ve sonunda ateşin çıkması birlikte korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"çakmak taşının ateşi yavaşça ve güçlükle çıkarması"}],"lexicalization_note":"Tanım yalnız çakmak taşının ateş çıkarmasıyla kurulan söz öbeğini kapsar; yalın biçime yaklaşma veya genel gecikme anlamı vermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanmayan ateş vermeyen taşlar seçilen karşıtlığı yineliyor, öbürleri ise ateş yakma, besleme veya karıştırma alanında daha uzakta kalıyor.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal gecikmiş başarıyı, komşu dal ise ateş çıkarma bakımından tam başarısızlığı anlatır.","focus_only":"Ateş gecikmeli ve güçlükle de olsa sonunda çıkar.","gloss":"gecikmiş çıkış ile hiç çıkmama","neighbor_only":"Çakmak taşı vurulduğu halde hiç ateş çıkarmaz.","neighbor_ref":"root_001335/B002","relation_type":"polarity_pair","shared_zone":"İki dal da çakmak taşının vurulması sonrasında ateş çıkarma başarısı eksenindedir."},{"boundary_match":"partial","distinction":"Odak dal çıkışın gecikmeli ve güç oluşunu anlatır; komşu dal yalnız ateş verme niteliğini öne çıkarır.","focus_only":"Ateşin çıkışındaki yavaşlık ve güçlüğü kurucu koşul sayar.","gloss":"ateş veren çakmak taşı","neighbor_only":"Çakmak taşının yanar veya ateş çıkarır nitelikte olmasını, gecikme koşulu olmadan bildirir.","neighbor_ref":"root_001471/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalda da çakmak taşından ateş çıkması gerçekleşir."},{"boundary_match":"partial","distinction":"Odak dal çıkış biçimini gecikme ve güçlükle sınırlar; komşu dal ateş çıkarma ve yakma sürecinin genel alanını kapsar.","focus_only":"Çakmak taşının ateşi yavaş ve güçlükle çıkarmasını gerektirir.","gloss":"çakmak taşından ateş çıkarma","neighbor_only":"Gizli ateşin çakmak taşından çıkmasını, ateşin yakılmasını ve canlandırılmasını daha geniş biçimde kapsar.","neighbor_ref":"root_001642/B002","relation_type":"near_neighbor","shared_zone":"İki dal da saklı ateşin çakmak taşından ortaya çıkması olayını paylaşır."}],"source_phrase_ar":"أن يخرج الزند النار ببطء وشدة (maqayis)؛ كاد الزند إذا تباطأ بإخراج ناره (mufradat)","source_summary":"Kaynaklar, çakmak taşının ateşini yavaş ve güçlükle çıkarmasında birleşir; tam başarısızlık değil, gecikmiş çıkış söz konusudur.","sources":["MQ","MU"],"what_is_ar":"يدخل فيه تباطؤ الزند في إخراج ناره بشدة","what_is_not_ar":"ليس مقاربة الفعل في كاد ولا مكيدة"},"support_links":[]},{"boundary":"Çekirdek kusma olayı veya ağızdan çıkarılan mide içeriğidir; yalnız bulantı değildir.","branch_kind":"bare","branch_ref":"root_001334/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَيْد","morph_features":"STEM|POS:N|LEM:kayod|ROOT:kyd|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:3:1","qac_word_ref":"105:2:3","surface_ar":"كَيْدَ"}],"gloss":"kusma ve kusmuk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Mide içeriği ağız yoluyla dışarı çıkarılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad, çıkarma olayının yanı sıra dışarı çıkarılan mide içeriğini de karşılayabilir."}}],"root_ar":"ك ي د","root_id":"root_001334","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem mide içeriğini ağızdan çıkarma olayını hem de çıkarılan maddeyi kapsayan en kısa genel karşılıktır.","boundary_detail":"Çekirdek kusma olayı veya ağızdan çıkarılan mide içeriğidir; yalnız bulantı değildir.","branch_image_ar":"القيء","concept_gloss":"kusma ve kusmuk","contextual_glosses":[{"applicability":"Bağlam dışarı çıkarma olayını eylem olarak anlattığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dışarı çıkarılan maddenin ad olarak karşılandığı kullanımı dışarıda bırakır.","preserves":"Mide içeriğini ağızdan dışarı çıkarma olayını korur."},"facet_ids":["F001"],"text":"kusmak","usage_role":"contextual"},{"applicability":"Bağlam çıkarma olayını değil, ağızdan çıkarılan maddeyi adlandırdığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kusma olayının süreç olarak anlatıldığı kullanımı dışarıda bırakır.","preserves":"Ağızdan çıkarılan mide içeriği yönünü korur."},"facet_ids":["F002"],"text":"kusmuk","usage_role":"contextual"}],"definition":"Mide içeriğinin ağızdan dışarı çıkarılması olayı veya bu olayda çıkarılan maddedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Mide içeriği ağız yoluyla dışarı çıkarılır."},{"facet_id":"F002","role":"extension","statement":"Ad, çıkarma olayının yanı sıra dışarı çıkarılan mide içeriğini de karşılayabilir."}],"identity_rationale":"Kaynak ifadesi yalın biçimde doğrudan kusma veya çıkarılan kusmuk anlamını verir. Bu anlam bulantı, bağırsak boşalması, can verme veya aybaşı görme ile karıştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kusma veya kusmuk"}],"lexicalization_note":"Tanım yalın kullanımı karşılar ve anlamı yalnız belirli bir söz öbeğine ya da başka bir bedensel boşalmaya bağlamaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanmayanlar kusmanın özel biçimlerini, gebelik bulantısını, genel bulantıyı, bağırsak boşalmasını veya seçilen yakın ayrımları yineler.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen sınırlar içinde çekirdek anlam ayrımı yoktur; iki dal aynı kusma alanını doğrudan adlandırır.","focus_only":null,"gloss":"kusma ve kusmuk","neighbor_only":null,"neighbor_ref":"root_000945/B011","relation_type":"synonym","shared_zone":"Her iki dal da kusma olayını ve ağızdan çıkarılan mide içeriğini karşılar."},{"boundary_match":"partial","distinction":"Odak dal olay ile maddeyi genel biçimde adlandırır; komşu dal dışarı atılma hareketini ve çıkış yönünü öne çıkarır.","focus_only":"Kusma olayının yanında çıkarılan maddeyi de ad olarak karşılayabilir.","gloss":"kusmuğun karından dışarı atılması","neighbor_only":"Kusmuğun karından dışarı fırlatılması ve hareket yönü özellikle belirtilir.","neighbor_ref":"root_001209/B007","relation_type":"near_synonym","shared_zone":"Her iki dal mide içeriğinin kusma yoluyla dışarı çıkmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal gerçekleşmiş çıkarma olayıdır; komşu dal kusmadan önce kalabilen bulantı ve mide kabarması durumudur.","focus_only":"Mide içeriğinin gerçekten ağızdan dışarı çıkmasını gerektirir.","gloss":"bulantı ve midenin kabarması","neighbor_only":"Kişinin içinin bulanmasını ve midesinin kabarmasını, kusma gerçekleşmeden de anlatır.","neighbor_ref":"root_001073/B003","relation_type":"near_neighbor","shared_zone":"İki dal kusma çevresindeki mide rahatsızlığı sürecine aittir."}],"source_phrase_ar":"الكيد القيء (maqayis)؛ وكذلك القيء (sihah)","source_summary":"Kaynaklar, yalın biçimin kusma anlamında kullanıldığında birleşir; anlam hem olayı hem de çıkarılan maddeyi bağlama göre karşılayabilir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه تسمية القيء كيدا","what_is_not_ar":"ليس الحيض ولا خروج النفس ولا المكيدة"},"support_links":[]},{"boundary":"Bu, aybaşı görmenin seyrek veya bağlama bağlı bir adıdır; başka kanamalarla karıştırılmaz.","branch_kind":"bare","branch_ref":"root_001334/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَيْد","morph_features":"STEM|POS:N|LEM:kayod|ROOT:kyd|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:3:1","qac_word_ref":"105:2:3","surface_ar":"كَيْدَ"}],"gloss":"aybaşı görme için seyrek bir ad","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan bedensel olay aybaşı görmedir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu adlandırma sürekli ve genel değil, kimi zaman görülen bir kullanımdır."}}],"root_ar":"ك ي د","root_id":"root_001334","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynağın bildirdiği aybaşı görme anlamını ve kullanımın olağan olmayışını birlikte karşılar.","boundary_detail":"Bu, aybaşı görmenin seyrek veya bağlama bağlı bir adıdır; başka kanamalarla karıştırılmaz.","branch_image_ar":"الحيض","concept_gloss":"aybaşı görme için seyrek bir ad","contextual_glosses":[{"applicability":"Bağlamın seyrek adlandırma bilgisini ayrıca taşıdığı yerde doğal metin içi karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu adın yalnız kimi zaman kullanıldığına ilişkin kullanım sınırını tek başına göstermez.","preserves":"Adlandırılan bedensel olayı doğru biçimde korur."},"facet_ids":["F001"],"text":"aybaşı görme","usage_role":"contextual"}],"definition":"Aybaşı görme olayına kimi zaman verilen, yaygınlığı sınırlı bir addır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan bedensel olay aybaşı görmedir."},{"facet_id":"F002","role":"source_variant","statement":"Bu adlandırma sürekli ve genel değil, kimi zaman görülen bir kullanımdır."}],"identity_rationale":"Tek kaynak ifadesi, yalın biçimin aybaşı görme için kimi zaman kullanılan bir ad olduğunu bildirir. Bu nedenle anlam korunmalı, fakat olağan ve sınırsız bir adlandırma gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kimi zaman aybaşı görme anlamında kullanılan ad"}],"lexicalization_note":"Tanım yalın kullanımı karşılar, ancak kaynakta belirtilen kimi zaman kullanılma sınırını korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanmayanlar aybaşı belirtisini, genel kanı, arınma denetimini, koyu kırmızılığı veya durmayan akışı konu edinerek seçilen sınırları keskinleştirmiyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sınırlı bir başka adlandırmadır; komşu dal aybaşı görmenin olağan adını ve ona bağlı kan, zaman ve yer kullanımlarını kapsar.","focus_only":"Aybaşı görmeyi yalnız kimi zaman kullanılan başka bir adla karşılar.","gloss":"aybaşı görme ve aybaşı kanı","neighbor_only":"Aybaşı kanını, zamanını ve yerini, ayrıca benzetmeli bazı kullanımları daha geniş biçimde kapsar.","neighbor_ref":"root_000379/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın temel konusu aybaşı görme olayıdır."},{"boundary_match":"partial","distinction":"Odak dal aybaşı görmedir; komşu dal olağan dönemin dışına taşan ve durmayan kanamadır.","focus_only":"Düzenli aybaşı görme olayını adlandırır.","gloss":"süren düzensiz kanama","neighbor_only":"Olağan günlerden sonra süren ve kesilmeyen düzensiz kanamayı anlatır.","neighbor_ref":"root_000379/B002","relation_type":"near_neighbor","shared_zone":"İki dal kadınlarda görülen rahim kaynaklı kanama alanındadır."},{"boundary_match":"partial","distinction":"Odak dal seyrek bir adlandırmadır; komşu dal olayın yanında kanı ve ilk gerçekleşmeyi içeren daha geniş bir alan sunar.","focus_only":"Yalnız kimi zaman kullanılan başka bir ad olma sınırını taşır.","gloss":"aybaşı görme, kanı ve ilk aybaşı","neighbor_only":"Aybaşı kanını ve özellikle ilk aybaşı görmeyi de açıkça kapsar.","neighbor_ref":"root_000949/B003","relation_type":"near_synonym","shared_zone":"Her iki dal aybaşı görme olayını doğrudan karşılar."}],"source_phrase_ar":"ربما سموا الحيض كيدا (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Aybaşı görme anlamı tek kaynakta ve kimi zaman kullanılan bir adlandırma olarak tanıklanır."}],"source_summary":"Tek kaynak, yalın biçimin aybaşı görme için kimi zaman kullanıldığını bildirir ve kullanımın sınırlı olduğunu gösterir.","sources":["MQ"],"what_is_ar":"يدخل فيه ما روي من تسمية الحيض كيدا","what_is_not_ar":"ليس القيء ولا المكيدة"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["105:2:1"],"branch_refs":[],"candidate_id":"cand_c778d8a6e58e0e99c638","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:2:1:abrupt-question-onset","source_type":"word_analysis","support_ids":["sup_63d1e726441b602b6637","sup_f5fcecfde485c644bf35"],"title":"hamza gives an audible onset","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:1","qac_refs":["105:2:1:1","105:2:1:2"],"status":"accepted"}},{"anchor_refs":["105:2:1"],"branch_refs":[],"candidate_id":"cand_105002ec1d4b3d04712f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:2:1:jussive-completed-negation","source_type":"word_analysis","support_ids":["sup_63d1e726441b602b6637","sup_bfbf9ed1d3e136bafc2c"],"title":"jussive negation makes the action completed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:1","qac_refs":["105:2:1:1","105:2:1:2"],"status":"accepted"}},{"anchor_refs":["105:2:1"],"branch_refs":[],"candidate_id":"cand_d28e203e0a7ace5aa87f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:2:1:paired-question-frame","source_type":"word_analysis","support_ids":["sup_63d1e726441b602b6637","sup_b7d8dd4a73b81f610e71"],"title":"second opening repeats the question frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:1","qac_refs":["105:2:1:1","105:2:1:2"],"status":"accepted"}},{"anchor_refs":["105:2:1"],"branch_refs":[],"candidate_id":"cand_3dc0de605373bf3bde83","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:2:1:rhetorical-confirmation","source_type":"word_analysis","support_ids":["sup_63d1e726441b602b6637","sup_7985dfa34f1d2a5588f8"],"title":"negative question demands acknowledgment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:1","qac_refs":["105:2:1:1","105:2:1:2"],"status":"accepted"}},{"anchor_refs":["105:2:1"],"branch_refs":[],"candidate_id":"cand_dada8f08de9b371569a4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:2:1:same-surah-making-escalation","source_type":"word_analysis","support_ids":["sup_63d1e726441b602b6637","sup_951425d87736463909a0"],"title":"the plot-to-people escalation begins here","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:1","qac_refs":["105:2:1:1","105:2:1:2"],"status":"accepted"}},{"anchor_refs":["105:2:2"],"branch_refs":[],"candidate_id":"cand_5ccba95162d3b3376e04","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"105:2:2:implicit-rabbuka-subject","source_type":"word_analysis","support_ids":["sup_3b129960cc13fb14e539","sup_acd5a2c4c18c82545ffa"],"title":"the subject is carried from the prior ayah","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:2","qac_refs":["105:2:2:1"],"status":"accepted"}},{"anchor_refs":["105:2:2"],"branch_refs":[],"candidate_id":"cand_5ae3e23b1521da34f2aa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"105:2:2:jussive-verb-trace","source_type":"word_analysis","support_ids":["sup_55b131be207a2142348d","sup_acd5a2c4c18c82545ffa"],"title":"the verb bears the particle's governance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:2","qac_refs":["105:2:2:1"],"status":"accepted"}},{"anchor_refs":["105:2:2"],"branch_refs":[],"candidate_id":"cand_76fda6df41306e5701da","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"105:2:2:locative-resultative-frame","source_type":"word_analysis","support_ids":["sup_acd5a2c4c18c82545ffa","sup_fd7747598dd24256bb1f"],"title":"object and result-state define the verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:2","qac_refs":["105:2:2:1"],"status":"accepted"}},{"anchor_refs":["105:2:2"],"branch_refs":[],"candidate_id":"cand_c0a3866c318ef7fbdf9d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"105:2:2:make-plot-loss-pairing","source_type":"word_analysis","support_ids":["sup_4d85fd9c277ae5add1b1","sup_acd5a2c4c18c82545ffa"],"title":"making is fused with plot and loss vocabulary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:2","qac_refs":["105:2:2:1"],"status":"accepted"}},{"anchor_refs":["105:2:2"],"branch_refs":[],"candidate_id":"cand_f92de1574c8e24ca7cfa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"105:2:2:prior-action-specified","source_type":"word_analysis","support_ids":["sup_38b9d01f9bbc328528d2","sup_acd5a2c4c18c82545ffa"],"title":"the prior broad act becomes specific","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:2","qac_refs":["105:2:2:1"],"status":"accepted"}},{"anchor_refs":["105:2:2"],"branch_refs":[],"candidate_id":"cand_b3681d0652fdeb70afbc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"105:2:2:root-range-narrowed-to-rendering","source_type":"word_analysis","support_ids":["sup_acd5a2c4c18c82545ffa","sup_e9fe5cda7d2b39b463a5"],"title":"broad making range narrows locally","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:2","qac_refs":["105:2:2:1"],"status":"accepted"}},{"anchor_refs":["105:2:2"],"branch_refs":[],"candidate_id":"cand_38f4452de4ef99ae7bc9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"105:2:2:scheme-before-schemers","source_type":"word_analysis","support_ids":["sup_ac54cb192b14251b68f8","sup_acd5a2c4c18c82545ffa"],"title":"the plot is targeted before the people","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:2","qac_refs":["105:2:2:1"],"status":"accepted"}},{"anchor_refs":["105:2:2"],"branch_refs":[],"candidate_id":"cand_e847ceacb06153ba65eb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"105:2:2:weighted-verb-sound","source_type":"word_analysis","support_ids":["sup_30b148c6a0c4c40639ad","sup_acd5a2c4c18c82545ffa"],"title":"the rendering verb has audible weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:2","qac_refs":["105:2:2:1"],"status":"accepted"}},{"anchor_refs":["105:2:3"],"branch_refs":[],"candidate_id":"cand_af66a39b8b269680133b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001334"],"scope":"focus_ayah","source_local_id":"105:2:3:compact-plot-sound","source_type":"word_analysis","support_ids":["sup_3f49f59988b46d9c033c","sup_a0c6d713e8c1577d6676"],"title":"hard plot-sound turns toward liquid loss","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:3","qac_refs":["105:2:3:1","105:2:3:2"],"status":"accepted"}},{"anchor_refs":["105:2:3"],"branch_refs":[],"candidate_id":"cand_7aa5fd3bcf9422ee28a7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001334"],"scope":"focus_ayah","source_local_id":"105:2:3:cross-surah-and-pronoun-echo","source_type":"word_analysis","support_ids":["sup_3f49f59988b46d9c033c","sup_5338f5be87c197465d29"],"title":"the plot-loss pattern and pronoun return","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:3","qac_refs":["105:2:3:1","105:2:3:2"],"status":"accepted"}},{"anchor_refs":["105:2:3"],"branch_refs":[],"candidate_id":"cand_59ce5d23b34f1563f6b2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001334"],"scope":"focus_ayah","source_local_id":"105:2:3:hostile-effort-not-neutral-plan","source_type":"word_analysis","support_ids":["sup_3f49f59988b46d9c033c","sup_9eeeada63a2da0b5bc4d"],"title":"kayd is worked hostile contrivance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:3","qac_refs":["105:2:3:1","105:2:3:2"],"status":"accepted"}},{"anchor_refs":["105:2:3"],"branch_refs":[],"candidate_id":"cand_57447610ead35f170a2c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001334"],"scope":"focus_ayah","source_local_id":"105:2:3:kayd-makr-contrast","source_type":"word_analysis","support_ids":["sup_3f49f59988b46d9c033c","sup_605d94379c8702dbe78d"],"title":"open hostile effort is not only hidden trickery","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:3","qac_refs":["105:2:3:1","105:2:3:2"],"status":"accepted"}},{"anchor_refs":["105:2:3"],"branch_refs":[],"candidate_id":"cand_35ba8e8d2432b58a2b41","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001334"],"scope":"focus_ayah","source_local_id":"105:2:3:masdar-object-pivot","source_type":"word_analysis","support_ids":["sup_3f49f59988b46d9c033c","sup_e1d8639b797f5f4cc051"],"title":"the plotted action becomes the object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:3","qac_refs":["105:2:3:1","105:2:3:2"],"status":"accepted"}},{"anchor_refs":["105:2:3"],"branch_refs":[],"candidate_id":"cand_f88955fe960de2877a91","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001334"],"scope":"focus_ayah","source_local_id":"105:2:3:possessive-antecedent-compression","source_type":"word_analysis","support_ids":["sup_2b577ad2f14e2abc8f02","sup_3f49f59988b46d9c033c"],"title":"the suffix carries and compresses the prior group","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:3","qac_refs":["105:2:3:1","105:2:3:2"],"status":"accepted"}},{"anchor_refs":["105:2:3"],"branch_refs":[],"candidate_id":"cand_ab0673abfc08da6a78f4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001334"],"scope":"focus_ayah","source_local_id":"105:2:3:reversal-pairings","source_type":"word_analysis","support_ids":["sup_3f49f59988b46d9c033c","sup_789003367480e3cd442f"],"title":"plotting is paired with making and loss","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:3","qac_refs":["105:2:3:1","105:2:3:2"],"status":"accepted"}},{"anchor_refs":["105:2:3"],"branch_refs":[],"candidate_id":"cand_6511e8c2c5ad3e199c43","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001334"],"scope":"focus_ayah","source_local_id":"105:2:3:scheme-before-people-boundary","source_type":"word_analysis","support_ids":["sup_3f49f59988b46d9c033c","sup_eab68b24b2bddaf12318"],"title":"the verse zooms from actors to scheme","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:3","qac_refs":["105:2:3:1","105:2:3:2"],"status":"accepted"}},{"anchor_refs":["105:2:4"],"branch_refs":[],"candidate_id":"cand_92704d3f76fb35454976","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:2:4:abstract-result-containment","source_type":"word_analysis","support_ids":["sup_9b3b8ecacbbe6ef8f8b0","sup_d667103fa7d13e531586"],"title":"fī makes loss a containing result","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:4","qac_refs":["105:2:4:1"],"status":"accepted"}},{"anchor_refs":["105:2:4"],"branch_refs":[],"candidate_id":"cand_4bb33c3eaf73f6001034","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:2:4:clause-landing-without-apposition","source_type":"word_analysis","support_ids":["sup_6343595ef86c7970c01f","sup_9b3b8ecacbbe6ef8f8b0"],"title":"the preposition prevents noun collapse","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:4","qac_refs":["105:2:4:1"],"status":"accepted"}},{"anchor_refs":["105:2:4"],"branch_refs":[],"candidate_id":"cand_be14a387c029e3040c43","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:2:4:compact-result-cadence","source_type":"word_analysis","support_ids":["sup_9b3b8ecacbbe6ef8f8b0","sup_d4b3fe345a499cf16e6c"],"title":"the preposition binds into the result sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:4","qac_refs":["105:2:4:1"],"status":"accepted"}},{"anchor_refs":["105:2:4"],"branch_refs":[],"candidate_id":"cand_8a227f84c771a4725f9d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:2:4:preposition-boundary-arc","source_type":"word_analysis","support_ids":["sup_7745cac56c295caa5800","sup_9b3b8ecacbbe6ef8f8b0"],"title":"prepositions move from target to outcome","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:4","qac_refs":["105:2:4:1"],"status":"accepted"}},{"anchor_refs":["105:2:5"],"branch_refs":[],"candidate_id":"cand_322d2ff1d4bc2ac1b86d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000913"],"scope":"focus_ayah","source_local_id":"105:2:5:composite-overclaim-narrowed","source_type":"word_analysis","support_ids":["sup_1fc0af82f270313e1f26","sup_946350198fcd808110f1"],"title":"hapax, nullifying, and sound claims need limits","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:5","qac_refs":["105:2:5:1"],"status":"accepted"}},{"anchor_refs":["105:2:5"],"branch_refs":[],"candidate_id":"cand_60939a2cc3e3e36b1d40","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000913"],"scope":"focus_ayah","source_local_id":"105:2:5:dissolution-image-pressure","source_type":"word_analysis","support_ids":["sup_1fc0af82f270313e1f26","sup_4c2d7674edecd75f900a"],"title":"loss can feel like losing shape","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:5","qac_refs":["105:2:5:1"],"status":"accepted"}},{"anchor_refs":["105:2:5"],"branch_refs":[],"candidate_id":"cand_562f9d8c828a19277802","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000913"],"scope":"focus_ayah","source_local_id":"105:2:5:final-closure-and-sound-field","source_type":"word_analysis","support_ids":["sup_1fc0af82f270313e1f26","sup_e525a9aec8ecabbe47a7"],"title":"the final word becomes semantic and acoustic seal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:5","qac_refs":["105:2:5:1"],"status":"accepted"}},{"anchor_refs":["105:2:5"],"branch_refs":[],"candidate_id":"cand_e6bef962be8cbe58f56f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000913"],"scope":"focus_ayah","source_local_id":"105:2:5:following-means-bridge","source_type":"word_analysis","support_ids":["sup_1fc0af82f270313e1f26","sup_acd8a96d7fb98d14cc56"],"title":"the result is picked up by later means","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:5","qac_refs":["105:2:5:1"],"status":"accepted"}},{"anchor_refs":["105:2:5"],"branch_refs":[],"candidate_id":"cand_c368ca232b229e47cb8b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000913"],"scope":"focus_ayah","source_local_id":"105:2:5:form-choice-rarity","source_type":"word_analysis","support_ids":["sup_1fc0af82f270313e1f26","sup_eb49f38a7c40303473b7"],"title":"the selected maṣdar is non-default","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:5","qac_refs":["105:2:5:1"],"status":"accepted"}},{"anchor_refs":["105:2:5"],"branch_refs":[],"candidate_id":"cand_2da4edaff5f991cf0ef2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000913"],"scope":"focus_ayah","source_local_id":"105:2:5:form-ii-causative-process","source_type":"word_analysis","support_ids":["sup_1fc0af82f270313e1f26","sup_b2338973829794c1b902"],"title":"Form II makes loss processive and causative","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:5","qac_refs":["105:2:5:1"],"status":"accepted"}},{"anchor_refs":["105:2:5"],"branch_refs":[],"candidate_id":"cand_25abb7e765226923fdf1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000913"],"scope":"focus_ayah","source_local_id":"105:2:5:indefinite-result-state","source_type":"word_analysis","support_ids":["sup_1fc0af82f270313e1f26","sup_2cad6949735722452925"],"title":"the final noun is an unbounded result-state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:5","qac_refs":["105:2:5:1"],"status":"accepted"}},{"anchor_refs":["105:2:5"],"branch_refs":[],"candidate_id":"cand_acae99c16efee6411560","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000913"],"scope":"focus_ayah","source_local_id":"105:2:5:liquid-loss-sound","source_type":"word_analysis","support_ids":["sup_1fc0af82f270313e1f26","sup_8a86a6e82a78b2026b4b"],"title":"liquid repetition suits dispersive loss","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:5","qac_refs":["105:2:5:1"],"status":"accepted"}},{"anchor_refs":["105:2:5"],"branch_refs":[],"candidate_id":"cand_0c56957a893c4eeb90e9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000913"],"scope":"focus_ayah","source_local_id":"105:2:5:local-pairings-and-cross-passage","source_type":"word_analysis","support_ids":["sup_02e23008c3d8b99b0f45","sup_1fc0af82f270313e1f26"],"title":"loss vocabulary answers making and plotting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:5","qac_refs":["105:2:5:1"],"status":"accepted"}},{"anchor_refs":["105:2:5"],"branch_refs":[],"candidate_id":"cand_319b8fe1e3fa5045f993","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000913"],"scope":"focus_ayah","source_local_id":"105:2:5:loss-misdirection-polysemy","source_type":"word_analysis","support_ids":["sup_1fc0af82f270313e1f26","sup_416aec3d1e0e1f5d0aa1"],"title":"misdirection and futility remain together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:5","qac_refs":["105:2:5:1"],"status":"accepted"}},{"anchor_refs":["105:2:5"],"branch_refs":[],"candidate_id":"cand_dffb2b2f8af0473398e7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000913"],"scope":"focus_ayah","source_local_id":"105:2:5:masdar-not-person-label","source_type":"word_analysis","support_ids":["sup_1fc0af82f270313e1f26","sup_69be0d6d9b6e061ae43e"],"title":"the process is named, not the people","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:5","qac_refs":["105:2:5:1"],"status":"accepted"}},{"anchor_refs":["105:2:5"],"branch_refs":[],"candidate_id":"cand_c27f186e3d035fe23737","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000913"],"scope":"focus_ayah","source_local_id":"105:2:5:surah-rhyme-thread","source_type":"word_analysis","support_ids":["sup_1fc0af82f270313e1f26","sup_234fd3dc11298daebcd3"],"title":"the ending anticipates later closures","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:2:5","qac_refs":["105:2:5:1"],"status":"accepted"}},{"anchor_refs":["105:2:2"],"branch_refs":[],"candidate_id":"cand_8de1e8a5b2f6382e3f29","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000248"],"scope":"focus_ayah","source_local_id":"105:2:2:1","source_type":"qac_morpheme","support_ids":["sup_fb40accbab3723645e4e"],"title":"QAC root occurrence: ج ع ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["105:2:3"],"branch_refs":[],"candidate_id":"cand_52b98b4a7e80d6a2fe26","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001334"],"scope":"focus_ayah","source_local_id":"105:2:3:1","source_type":"qac_morpheme","support_ids":["sup_9d473395b693023d44b3"],"title":"QAC root occurrence: ك ي د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["105:2:5"],"branch_refs":[],"candidate_id":"cand_0e05600880e6cf729e7f","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000913"],"scope":"focus_ayah","source_local_id":"105:2:5:1","source_type":"qac_morpheme","support_ids":["sup_20b0ef4dddb3bb3e7db6"],"title":"QAC root occurrence: ض ل ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["105:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"105:2","branch_refs":["root_000248/B002","root_000913/B001","root_001334/B002"],"candidate_id":"cand_cd12b0497cfc75141387","commentary_obligation":"review","hft_ref":"hft_47a8da7bf887ea1ae38b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01-purpose-reversal","source_type":"hft","support_ids":["sup_700eab952f67d317e573"],"title":"b01-purpose-reversal","trust":"legacy_unbound"},{"anchor_refs":["105:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"105:2","branch_refs":["root_000248/B002","root_000913/B003","root_001334/B001"],"candidate_id":"cand_69fbd896ba3111dec9f5","commentary_obligation":"review","hft_ref":"hft_4632e9c9541c2e5a130f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02-spent-effort-lost","source_type":"hft","support_ids":["sup_7981bcc602ead38ea3eb"],"title":"b02-spent-effort-lost","trust":"legacy_unbound"},{"anchor_refs":["105:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"105:2","branch_refs":["root_000248/B002","root_000913/B002","root_001334/B002"],"candidate_id":"cand_2ad3883413768226114c","commentary_obligation":"review","hft_ref":"hft_88d71f2d0eded55ab344","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03-operative-disappearance","source_type":"hft","support_ids":["sup_42d4c5fd159c0d49ffad"],"title":"b03-operative-disappearance","trust":"legacy_unbound"},{"anchor_refs":["105:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"105:2","branch_refs":["root_000248/B002","root_000913/B001","root_001334/B004"],"candidate_id":"cand_a018f14db3aaf5929f90","commentary_obligation":"review","hft_ref":"hft_37e0aac59c45a973990b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b04-battle-capacity-derailed","source_type":"hft","support_ids":["sup_a2c64243a9915c58da2b"],"title":"b04-battle-capacity-derailed","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍۢ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|A:INTG+","morpheme_role":"PREFIX","pos":"INTG","qac_ref":"105:2:1:1","qac_word_ref":"105:2:1","root_ar":"","surface_ar":"أَ"},{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"105:2:1:2","qac_word_ref":"105:2:1","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"105:2:2:1","qac_word_ref":"105:2:2","root_ar":"ج ع ل","surface_ar":"يَجْعَلْ"},{"lemma_ar":"كَيْد","morph_features":"STEM|POS:N|LEM:kayod|ROOT:kyd|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:3:1","qac_word_ref":"105:2:3","root_ar":"ك ي د","surface_ar":"كَيْدَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"105:2:3:2","qac_word_ref":"105:2:3","root_ar":"","surface_ar":"هُمْ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"105:2:4:1","qac_word_ref":"105:2:4","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"تَضْلِيل","morph_features":"STEM|POS:N|VN|(II)|LEM:taDoliyl|ROOT:Dll|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:5:1","qac_word_ref":"105:2:5","root_ar":"ض ل ل","surface_ar":"تَضْلِيلٍ"}],"word_analysis_qac_refs":[["105:2:1:1","105:2:1:2"],["105:2:2:1"],["105:2:3:1","105:2:3:2"],["105:2:4:1"],["105:2:5:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["105:2:1","105:2:2","105:2:3","105:2:4","105:2:5"]},"focus_surface_evidence":{"arabic_uthmani":"أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍۢ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|A:INTG+","morpheme_role":"PREFIX","pos":"INTG","qac_ref":"105:2:1:1","qac_word_ref":"105:2:1","root_ar":"","surface_ar":"أَ"},{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"105:2:1:2","qac_word_ref":"105:2:1","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"جَعَلَ","morph_features":"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"105:2:2:1","qac_word_ref":"105:2:2","root_ar":"ج ع ل","surface_ar":"يَجْعَلْ"},{"lemma_ar":"كَيْد","morph_features":"STEM|POS:N|LEM:kayod|ROOT:kyd|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:3:1","qac_word_ref":"105:2:3","root_ar":"ك ي د","surface_ar":"كَيْدَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"105:2:3:2","qac_word_ref":"105:2:3","root_ar":"","surface_ar":"هُمْ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"105:2:4:1","qac_word_ref":"105:2:4","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"تَضْلِيل","morph_features":"STEM|POS:N|VN|(II)|LEM:taDoliyl|ROOT:Dll|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:2:5:1","qac_word_ref":"105:2:5","root_ar":"ض ل ل","surface_ar":"تَضْلِيلٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["105:2:1:1","105:2:1:2"],["105:2:2:1"],["105:2:3:1","105:2:3:2"],["105:2:4:1"],["105:2:5:1"]],"word_analysis_refs":["105:2:1","105:2:2","105:2:3","105:2:4","105:2:5"],"word_rows":[{"analysis_record_ref":"105:2:1","analytic_gloss_range_en":"compound negative interrogative particle with rhetorical confirmatory force, governing the following jussive verb and framing the whole clause as acknowledged completed action","analytic_root_gloss_range_en":null,"qac_refs":["105:2:1:1","105:2:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"أَلَمْ","transliteration":"alam"}},{"analysis_record_ref":"105:2:2","analytic_gloss_range_en":"lam-governed jussive rendering verb, with the local construction selecting an object plus result-state complement rather than a bare making or beginning sense","analytic_root_gloss_range_en":"broad root range of making, placing, rendering, appointing, creating, and beginning; local grammar selects the placing-rendering branch with an explicit object and a prepositional result state","qac_refs":["105:2:2:1"],"root":{"arabic":"ج ع ل","transliteration":"j-ʿ-l"},"surface":{"arabic":"يَجْعَلْ","transliteration":"yajʿal"}},{"analysis_record_ref":"105:2:3","analytic_gloss_range_en":"their specific hostile scheme or contrivance, packaged as a verbal noun, possessed by the prior group and serving as the direct object being rendered into loss","analytic_root_gloss_range_en":"root field of working on something, plotting, stratagem, hostile effort, and some construction-bound marginal branches; local grammar selects the plotted hostile effort branch","qac_refs":["105:2:3:1","105:2:3:2"],"root":{"arabic":"ك ي د","transliteration":"k-y-d"},"surface":{"arabic":"كَيْدَهُمْ","transliteration":"kaydahum"}},{"analysis_record_ref":"105:2:4","analytic_gloss_range_en":"preposition governing the final verbal noun as an abstract locative-resultative state, making the plot placed inside loss rather than simply equated with it","analytic_root_gloss_range_en":null,"qac_refs":["105:2:4:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فِى","transliteration":"fī"}},{"analysis_record_ref":"105:2:5","analytic_gloss_range_en":"indefinite Form II verbal noun governed by the preposition as the result-state of the plot, combining causative misdirection, futility, and loss of direction without naming a separate patient","analytic_root_gloss_range_en":"root field of straying, error, loss, disappearance, perishing, and going missing; local Form II maṣdar selects causative or intensive misdirection and futility as the plot's enclosing state","qac_refs":["105:2:5:1"],"root":{"arabic":"ض ل ل","transliteration":"ḍ-l-l"},"surface":{"arabic":"تَضْلِيلٍ","transliteration":"taḍlīlin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["105:2"],"branch_refs":["root_000248/B002","root_000913/B001","root_001334/B002"],"candidate_id":"cand_cd12b0497cfc75141387","evidence_scope":"focus_ayah","hft_ref":"hft_47a8da7bf887ea1ae38b","item_id":"b01-purpose-reversal","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01-purpose-reversal","support_id":"sup_700eab952f67d317e573"},{"anchor_refs":["105:2"],"branch_refs":["root_000248/B002","root_000913/B003","root_001334/B001"],"candidate_id":"cand_69fbd896ba3111dec9f5","evidence_scope":"focus_ayah","hft_ref":"hft_4632e9c9541c2e5a130f","item_id":"b02-spent-effort-lost","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02-spent-effort-lost","support_id":"sup_7981bcc602ead38ea3eb"},{"anchor_refs":["105:2"],"branch_refs":["root_000248/B002","root_000913/B002","root_001334/B002"],"candidate_id":"cand_2ad3883413768226114c","evidence_scope":"focus_ayah","hft_ref":"hft_88d71f2d0eded55ab344","item_id":"b03-operative-disappearance","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03-operative-disappearance","support_id":"sup_42d4c5fd159c0d49ffad"},{"anchor_refs":["105:2"],"branch_refs":["root_000248/B002","root_000913/B001","root_001334/B004"],"candidate_id":"cand_a018f14db3aaf5929f90","evidence_scope":"focus_ayah","hft_ref":"hft_37e0aac59c45a973990b","item_id":"b04-battle-capacity-derailed","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b04-battle-capacity-derailed","support_id":"sup_a2c64243a9915c58da2b"}],"diagnostics":[],"lane_counts":{"global":9,"macro":14,"micro":4},"packet_summary":{"ayah_count":5,"focus_ref":"105:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]}],"window":["105:1","105:2","105:3","105:4","105:5"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"105:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":18,"unstructured_record_count":0},"identity":{"ayah_ref":"105:2","lane":"micro","linguistic_source_ref":"105:2","surface_ref":"105:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"105:2","target_tokens":[["Onların",["105:2:3"]],["planını",["105:2:3"]],["boşa",["105:2:4","105:2:5"]],["çıkarmadı",["105:2:2","105:2:5"]],["mı",["105:2:1"]]],"text":"Onların planını boşa çıkarmadı mı?"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":5,"id":"s105-p01-001-005","label":"Whole surah","number":1,"refs":["105:1","105:2","105:3","105:4","105:5"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:5:local-pairings-and-cross-passage","source_type":"word_analysis","support_id":"sup_02e23008c3d8b99b0f45","text":"{\"blocking_evidence\":null,\"headline\":\"loss vocabulary answers making and plotting\",\"reader_payoff\":\"The reader notices that {{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}) is the specific answer to both {{ar:يَجْعَلْ}} ({{tr:yajʿal}}) and {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}), with the hostile plotting plus loss-field at 40:25 sharpening the pattern.\",\"reason\":\"The local grammar directly ties the result noun to the rendering verb and plot object, and the CRITICAL rows provide a concrete cross-passage comparison at 40:25.\",\"representative_source_ids\":[\"QI-0544e7b1\",\"QI-379cee18\",\"QI-fbe90ddd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:5","source_type":"word_analysis","support_id":"sup_1fc0af82f270313e1f26","text":"{\"gloss_range\":\"indefinite Form II verbal noun governed by the preposition as the result-state of the plot, combining causative misdirection, futility, and loss of direction without naming a separate patient\",\"prose\":\"{{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}) is the ayah's landing word. Governed by {{ar:فِى}} ({{tr:fī}}), it is not a new event beside the plot but the state into which {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) is placed by {{ar:يَجْعَلْ}} ({{tr:yajʿal}}). Its indefiniteness leaves that state qualitative and open-ended. As a marked Form II maṣdar rather than a simple person-label or static error term, it keeps causative and intensive pressure alive: the scheme is made to lose direction, its path is nullified into futility, and no explicit patient is named. The root field of {{ar:ض ل ل}} ({{tr:ḍ-l-l}}) lets misdirection, futility, and loss of coherence work together; the decomposition image cited at 32:10 survives only as image-pressure for the plot losing shape, not as a literal bodily scene. The sparse plot-loss field at 40:25 strengthens the local formula, while the final -īlin cadence carries the verdict toward the later terminal sounds in 105:3, 105:4, and 105:5. The repeated lām and long vowel make the final loss word sound looser after the compact plot noun, so semantic loss and acoustic dispersal converge at the close.\",\"root_display\":\"{{ar:ض ل ل}} ({{tr:ḍ-l-l}})\",\"root_gloss_range\":\"root field of straying, error, loss, disappearance, perishing, and going missing; local Form II maṣdar selects causative or intensive misdirection and futility as the plot's enclosing state\",\"surface_display\":\"{{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"105:2:5:1","source_type":"qac_morpheme","support_id":"sup_20b0ef4dddb3bb3e7db6","text":"{\"lemma_ar\":\"تَضْلِيل\",\"morph_features\":\"STEM|POS:N|VN|(II)|LEM:taDoliyl|ROOT:Dll|M|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"105:2:5:1\",\"qac_word_ref\":\"105:2:5\",\"root_ar\":\"ض ل ل\",\"surface_ar\":\"تَضْلِيلٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:5:surah-rhyme-thread","source_type":"word_analysis","support_id":"sup_234fd3dc11298daebcd3","text":"{\"blocking_evidence\":null,\"headline\":\"the ending anticipates later closures\",\"reader_payoff\":\"The reader notices that the -īlin ending of {{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}) prepares the surah's later terminal sound field in 105:3, 105:4, and 105:5.\",\"reason\":\"The sound rows are anchored in concrete same-surah surfaces and are kept as cadence payoff, not as independent lexical argument.\",\"representative_source_ids\":[\"QE-578ea2fd\",\"QP-6e53b24b\",\"QP-ea751667\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:3:possessive-antecedent-compression","source_type":"word_analysis","support_id":"sup_2b577ad2f14e2abc8f02","text":"{\"blocking_evidence\":null,\"headline\":\"the suffix carries and compresses the prior group\",\"reader_payoff\":\"The reader notices that the suffix in {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) both recalls the prior group from 105:1 and reduces them to owners of a plot now being judged.\",\"reason\":\"Attachment evidence links the suffix to the prior plural group and treats it as the genitive possessor. The broader universalizing claim in one source row is narrowed to a local discourse effect, not made a replacement for the antecedent.\",\"representative_source_ids\":[\"QG-1cf14ce2\",\"QG-fce209dc\",\"QY-9d558ab4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:5:indefinite-result-state","source_type":"word_analysis","support_id":"sup_2cad6949735722452925","text":"{\"blocking_evidence\":null,\"headline\":\"the final noun is an unbounded result-state\",\"reader_payoff\":\"The reader notices that {{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}) is the governed state where the plot lands, and its indefiniteness makes that loss qualitative rather than bounded.\",\"reason\":\"QAC marks the word as genitive under {{ar:فِى}} ({{tr:fī}}), and attachment evidence makes it the result-state complement of {{ar:يَجْعَلْ}} ({{tr:yajʿal}}).\",\"representative_source_ids\":[\"QG-59aff61c\",\"QG-78e11bb2\",\"QG-a3b7252c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:2:weighted-verb-sound","source_type":"word_analysis","support_id":"sup_30b148c6a0c4c40639ad","text":"{\"blocking_evidence\":null,\"headline\":\"the rendering verb has audible weight\",\"reader_payoff\":\"The reader notices the dense throat-and-stop texture of {{ar:يَجْعَلْ}} ({{tr:yajʿal}}) before the clause turns to the compact plot noun and the liquid loss ending.\",\"reason\":\"The sound observation is tied to the actual local surface and kept as an acoustic payoff, not as independent semantic proof.\",\"representative_source_ids\":[\"QP-1feed2e6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:2:prior-action-specified","source_type":"word_analysis","support_id":"sup_38b9d01f9bbc328528d2","text":"{\"blocking_evidence\":null,\"headline\":\"the prior broad act becomes specific\",\"reader_payoff\":\"The reader notices that {{ar:يَجْعَلْ}} ({{tr:yajʿal}}) gives specific content to the broad question about what was done in 105:1, then anticipates the later making in 105:5.\",\"reason\":\"Attachment evidence treats 105:2 as one compact verbal clause, and the same-surah rows show how this verb answers the prior broad action and prepares the later perfect form.\",\"representative_source_ids\":[\"QT-3e41d17b\",\"QT-e418534c\",\"QE-b45bc8b1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:2:implicit-rabbuka-subject","source_type":"word_analysis","support_id":"sup_3b129960cc13fb14e539","text":"{\"blocking_evidence\":null,\"headline\":\"the subject is carried from the prior ayah\",\"reader_payoff\":\"The reader notices that the agent is not newly introduced; the verb agreement resumes the prior explicit subject from 105:1.\",\"reason\":\"Attachment evidence marks a syntactically forced implicit 3ms subject whose discourse candidate is the prior explicit subject in 105:1.\",\"representative_source_ids\":[\"QG-543ec7eb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:3","source_type":"word_analysis","support_id":"sup_3f49f59988b46d9c033c","text":"{\"gloss_range\":\"their specific hostile scheme or contrivance, packaged as a verbal noun, possessed by the prior group and serving as the direct object being rendered into loss\",\"prose\":\"{{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) is the ayah's pivot: a hostile act of plotting is packaged as a maṣdar noun, possessed by the prior group, and placed as the direct object of {{ar:يَجْعَلْ}} ({{tr:yajʿal}}). The suffix does not leave the owners vague in context; it carries the prior group from 105:1 while reducing them here to possessors of a scheme. The root range makes the noun more than a neutral plan: {{ar:ك ي د}} ({{tr:k-y-d}}) brings organized hostile contrivance and exerted effort, and the contrast with a concealment-centered plotting term helps keep the open, worked campaign from being treated as only hidden trickery. Structurally, the plot receives the verdict before the people do; {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) enters {{ar:فِى تَضْلِيلٍ}} ({{tr:fī taḍlīlin}}), and 105:5 later shifts from the scheme to the people. The same plot-and-loss pattern is sharpened by the nearby field at 40:25. In sound, the compact hard shape of {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) gives way to the looser liquids of {{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}), so the movement from contrivance toward dispersive loss is also heard.\",\"root_display\":\"{{ar:ك ي د}} ({{tr:k-y-d}})\",\"root_gloss_range\":\"root field of working on something, plotting, stratagem, hostile effort, and some construction-bound marginal branches; local grammar selects the plotted hostile effort branch\",\"surface_display\":\"{{ar:كَيْدَهُمْ}} ({{tr:kaydahum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:5:loss-misdirection-polysemy","source_type":"word_analysis","support_id":"sup_416aec3d1e0e1f5d0aa1","text":"{\"blocking_evidence\":null,\"headline\":\"misdirection and futility remain together\",\"reader_payoff\":\"The reader notices that the final word can hold misguiding, futility, and directional ruin together, so the scheme's path collapses rather than merely failing tactically.\",\"reason\":\"V4 supports error, deviation, loss, and disappearance branches for {{ar:ض ل ل}} ({{tr:ḍ-l-l}}), while the local Form II result-state keeps those pressures tied to the scheme's fate rather than activating every dictionary branch independently.\",\"representative_source_ids\":[\"QS-3e873ece\",\"QS-641642e4\",\"QS-c0b5779d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:5:dissolution-image-pressure","source_type":"word_analysis","support_id":"sup_4c2d7674edecd75f900a","text":"{\"blocking_evidence\":null,\"headline\":\"loss can feel like losing shape\",\"reader_payoff\":\"The reader notices a concrete image-pressure behind the verdict: the plotted path does not just miss its goal but loses coherence inside its ruin.\",\"reason\":\"The image associated with the cited expression at 32:10 is retained as lexical image-pressure, but local grammar does not turn the plot into a literal decomposition scene.\",\"representative_source_ids\":[\"QS-10b24c43\",\"QS-a4371dd5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:2:make-plot-loss-pairing","source_type":"word_analysis","support_id":"sup_4d85fd9c277ae5add1b1","text":"{\"blocking_evidence\":null,\"headline\":\"making is fused with plot and loss vocabulary\",\"reader_payoff\":\"The reader notices that the verb's making is not neutral production; in this clause it is tied directly to hostile plotting and the loss-field of {{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}).\",\"reason\":\"The CRITICAL co-occurrence rows are locally realized by the actual object {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) and the actual result complement {{ar:فِى تَضْلِيلٍ}} ({{tr:fī taḍlīlin}}).\",\"representative_source_ids\":[\"QI-48863687\",\"QI-6ffe7ddf\",\"QE-c6799970\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:3:cross-surah-and-pronoun-echo","source_type":"word_analysis","support_id":"sup_5338f5be87c197465d29","text":"{\"blocking_evidence\":null,\"headline\":\"the plot-loss pattern and pronoun return\",\"reader_payoff\":\"The reader notices two echoes: a hostile plotting plus loss-field at 40:25, and a same-surah shift from the suffix in {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) to the people as object in 105:5.\",\"reason\":\"The CRITICAL rows provide concrete reference points, and the local pronoun and plot-loss construction make both echoes relevant without letting them override the local parse.\",\"representative_source_ids\":[\"QE-c354954c\",\"QE-e0ce1fd1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:2:jussive-verb-trace","source_type":"word_analysis","support_id":"sup_55b131be207a2142348d","text":"{\"blocking_evidence\":null,\"headline\":\"the verb bears the particle's governance\",\"reader_payoff\":\"The reader notices that {{ar:يَجْعَلْ}} ({{tr:yajʿal}}) visibly carries the effect of {{ar:أَلَمْ}} ({{tr:alam}}), so the assertion is grammatically closed rather than freely imperfect.\",\"reason\":\"QAC marks the verb as jussive under the particle, and the attachment table forces the particle-complement relation.\",\"representative_source_ids\":[\"QG-17a9a949\",\"QF-df83a1c7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:3:kayd-makr-contrast","source_type":"word_analysis","support_id":"sup_605d94379c8702dbe78d","text":"{\"blocking_evidence\":null,\"headline\":\"open hostile effort is not only hidden trickery\",\"reader_payoff\":\"The reader notices why the word can fit an organized open campaign: the local scheme does not need to be reduced to concealment-centered hidden trickery.\",\"reason\":\"The contrast with a concealment-centered plotting term survives as a lexical distinction, while historical specificity and universal application claims are narrowed because the local grammar only gives a possessive scheme tied to 105:1.\",\"representative_source_ids\":[\"QS-d743fc1b\",\"MS-7878d978\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:4:clause-landing-without-apposition","source_type":"word_analysis","support_id":"sup_6343595ef86c7970c01f","text":"{\"blocking_evidence\":null,\"headline\":\"the preposition prevents noun collapse\",\"reader_payoff\":\"The reader notices the two-step architecture: action, object, then governed outcome, instead of two adjacent nouns being treated as apposition.\",\"reason\":\"The clause is headed by {{ar:يَجْعَلْ}} ({{tr:yajʿal}}), with {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) as object and {{ar:فِى تَضْلِيلٍ}} ({{tr:fī taḍlīlin}}) as the structural landing.\",\"representative_source_ids\":[\"QT-7ee0d035\",\"QT-a7faea6f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:1","source_type":"word_analysis","support_id":"sup_63d1e726441b602b6637","text":"{\"gloss_range\":\"compound negative interrogative particle with rhetorical confirmatory force, governing the following jussive verb and framing the whole clause as acknowledged completed action\",\"prose\":\"{{ar:أَلَمْ}} ({{tr:alam}}) opens the ayah as a question whose force is confirmation, not information-seeking. Its lām governs {{ar:يَجْعَلْ}} ({{tr:yajʿal}}) as a jussive and gives the action completed-past force, so the listener is pressed to acknowledge what has already been done. The repeated particle frame also binds this verse to the opening question in 105:1: the first question asks the addressee to notice the event, while the second names the decisive mechanism. The same-surah movement then looks ahead to 105:5, where the making shifts from the plot to the people themselves. Even the opening hamza gives the clause an audible catch before the governed verb takes over.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَلَمْ}} ({{tr:alam}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:5:masdar-not-person-label","source_type":"word_analysis","support_id":"sup_69be0d6d9b6e061ae43e","text":"{\"blocking_evidence\":null,\"headline\":\"the process is named, not the people\",\"reader_payoff\":\"The reader notices that the ayah names the scheme's enclosing process-state rather than labeling people with an active participle.\",\"reason\":\"QAC identifies a maṣdar governed by {{ar:فِى}} ({{tr:fī}}), not a participial form naming astray persons.\",\"representative_source_ids\":[\"QF-f9fe1bb4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:4:preposition-boundary-arc","source_type":"word_analysis","support_id":"sup_7745cac56c295caa5800","text":"{\"blocking_evidence\":null,\"headline\":\"prepositions move from target to outcome\",\"reader_payoff\":\"The reader notices the boundary movement from the preposition in 105:1, which introduces those acted against, to {{ar:فِى}} ({{tr:fī}}) in 105:2, which contains the fate of their scheme.\",\"reason\":\"The row names a concrete local preposition arc, and the local attachment confirms that {{ar:فِى}} ({{tr:fī}}) marks the result-state complement.\",\"representative_source_ids\":[\"QB-ece98b05\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:3:reversal-pairings","source_type":"word_analysis","support_id":"sup_789003367480e3cd442f","text":"{\"blocking_evidence\":null,\"headline\":\"plotting is paired with making and loss\",\"reader_payoff\":\"The reader notices that {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) is not free-floating; it is bound to the rendering verb and the loss vocabulary that reverse it.\",\"reason\":\"The local clause directly realizes the pairings: {{ar:يَجْعَلْ}} ({{tr:yajʿal}}) governs {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}), and the plot is followed by {{ar:فِى تَضْلِيلٍ}} ({{tr:fī taḍlīlin}}).\",\"representative_source_ids\":[\"QI-4e28961c\",\"QI-624568a3\",\"QI-90f126b0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:1:rhetorical-confirmation","source_type":"word_analysis","support_id":"sup_7985dfa34f1d2a5588f8","text":"{\"blocking_evidence\":null,\"headline\":\"negative question demands acknowledgment\",\"reader_payoff\":\"The reader notices that the ayah is framed as compelled acknowledgment, where the apparent negated question means that the divine act is already known and must be conceded.\",\"reason\":\"The word table explicitly identifies an interrogative hamza plus jussive negator with rhetorical confirmatory force, matching the CRITICAL rows on acknowledgment.\",\"representative_source_ids\":[\"QG-7e08bd35\",\"MG-92c08187\",\"QS-be500632\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:5:liquid-loss-sound","source_type":"word_analysis","support_id":"sup_8a86a6e82a78b2026b4b","text":"{\"blocking_evidence\":null,\"headline\":\"liquid repetition suits dispersive loss\",\"reader_payoff\":\"The reader notices the repeated lām and long vowel in {{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}), which makes the final loss word sound looser after the compact plot noun.\",\"reason\":\"The sound claim is tied to the local surface and carefully framed as iconic suitability, not proof of meaning.\",\"representative_source_ids\":[\"QP-8d75c88f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:5:composite-overclaim-narrowed","source_type":"word_analysis","support_id":"sup_946350198fcd808110f1","text":"{\"blocking_evidence\":null,\"headline\":\"hapax, nullifying, and sound claims need limits\",\"reader_payoff\":\"The reader notices a real convergence: the rare Form II noun, plot-loss pairing, nullifying sense, and cadence all reinforce the final verdict, while the local grammar keeps them from becoming uncontrolled claims.\",\"reason\":\"The convergence survives, but claims of violent intensity, Quranic reservation, or sound enacting meaning are narrowed to locally supported salience, causative or intensive Form II force, and acoustic reinforcement.\",\"representative_source_ids\":[\"QE-d235ff13\",\"QH-cda6ffae\",\"MH-fb3b38fe\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:1:same-surah-making-escalation","source_type":"word_analysis","support_id":"sup_951425d87736463909a0","text":"{\"blocking_evidence\":null,\"headline\":\"the plot-to-people escalation begins here\",\"reader_payoff\":\"The reader notices a same-surah progression: 105:2 asks about the rendering of their plot, while 105:5 later makes the people themselves the object.\",\"reason\":\"The cross-ayah comparison is real, but it is narrowed because these rows are more directly about the repeated making verb than about the particle itself.\",\"representative_source_ids\":[\"MI-c9922c5f\",\"MT-70330685\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:4","source_type":"word_analysis","support_id":"sup_9b3b8ecacbbe6ef8f8b0","text":"{\"gloss_range\":\"preposition governing the final verbal noun as an abstract locative-resultative state, making the plot placed inside loss rather than simply equated with it\",\"prose\":\"{{ar:فِى}} ({{tr:fī}}) is small but decisive. It governs {{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}) and completes {{ar:يَجْعَلْ}} ({{tr:yajʿal}}) as a result phrase, so {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) is not simply renamed as loss; it is located inside a loss-state. That keeps the spatial image of containment alive while remaining abstract, and it prevents the two nouns from collapsing into apposition. Its long ī also binds audibly to {{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}). Across the boundary, the movement from the preposition in 105:1 to {{ar:فِى}} ({{tr:fī}}) in 105:2 moves from the group acted against to the result enclosing their scheme.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِى}} ({{tr:fī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"105:2:3:1","source_type":"qac_morpheme","support_id":"sup_9d473395b693023d44b3","text":"{\"lemma_ar\":\"كَيْد\",\"morph_features\":\"STEM|POS:N|LEM:kayod|ROOT:kyd|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"105:2:3:1\",\"qac_word_ref\":\"105:2:3\",\"root_ar\":\"ك ي د\",\"surface_ar\":\"كَيْدَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:3:hostile-effort-not-neutral-plan","source_type":"word_analysis","support_id":"sup_9eeeada63a2da0b5bc4d","text":"{\"blocking_evidence\":null,\"headline\":\"kayd is worked hostile contrivance\",\"reader_payoff\":\"The reader notices that {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) is not a neutral plan but organized hostile effort that is made to spend itself in loss.\",\"reason\":\"V4 supports the plotting, stratagem, and forceful working branches for {{ar:ك ي د}} ({{tr:k-y-d}}). Construction-bound branches such as death-throes, battle idioms, or unrelated bodily senses are not imported into the local noun.\",\"representative_source_ids\":[\"QS-11e34837\",\"QS-968c7fe4\",\"QS-ba80a107\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:3:compact-plot-sound","source_type":"word_analysis","support_id":"sup_a0c6d713e8c1577d6676","text":"{\"blocking_evidence\":null,\"headline\":\"hard plot-sound turns toward liquid loss\",\"reader_payoff\":\"The reader notices the sound movement from the compact consonants of {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) into the looser repeated liquids of {{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}).\",\"reason\":\"The sound claim is tied to the actual adjacent surfaces and is kept as acoustic reinforcement, not semantic proof.\",\"representative_source_ids\":[\"QP-8cb43963\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:2:scheme-before-schemers","source_type":"word_analysis","support_id":"sup_ac54cb192b14251b68f8","text":"{\"blocking_evidence\":null,\"headline\":\"the plot is targeted before the people\",\"reader_payoff\":\"The reader notices the surah's order of reversal: 105:2 makes the plot the object, and 105:5 later makes the people the object.\",\"reason\":\"QAC and attachment evidence make {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) the object in 105:2, while the cited same-surah row points to the later object pronoun in 105:5.\",\"representative_source_ids\":[\"QS-d45cb97d\",\"QF-c3bb8bac\",\"QI-b4c8fdf0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:2","source_type":"word_analysis","support_id":"sup_acd5a2c4c18c82545ffa","text":"{\"gloss_range\":\"lam-governed jussive rendering verb, with the local construction selecting an object plus result-state complement rather than a bare making or beginning sense\",\"prose\":\"{{ar:يَجْعَلْ}} ({{tr:yajʿal}}) is the verb where the opening question becomes a specific act. Governed by {{ar:أَلَمْ}} ({{tr:alam}}), it is jussive and grammatically closed, while its unspoken subject carries forward the prior explicit subject from 105:1. Locally the verb is not a vague making: it takes {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) as the object and {{ar:فِى تَضْلِيلٍ}} ({{tr:fī taḍlīlin}}) as a result-state complement, so the plot is rendered by being placed inside loss. The making is therefore not neutral production; it is tied directly to hostile plotting and the loss-field that reverses it. That makes the scheme the first target before 105:5, where the people themselves become the object. The broad range of {{ar:ج ع ل}} ({{tr:j-ʿ-l}}) remains behind the wording, but the local construction selects placing and rendering rather than creation, appointment, reward, or beginning. Its voiced throat consonant and final stopped lām give the rendering verb audible weight before the clause turns to the compact plot noun and the liquid loss ending.\",\"root_display\":\"{{ar:ج ع ل}} ({{tr:j-ʿ-l}})\",\"root_gloss_range\":\"broad root range of making, placing, rendering, appointing, creating, and beginning; local grammar selects the placing-rendering branch with an explicit object and a prepositional result state\",\"surface_display\":\"{{ar:يَجْعَلْ}} ({{tr:yajʿal}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:5:following-means-bridge","source_type":"word_analysis","support_id":"sup_acd8a96d7fb98d14cc56","text":"{\"blocking_evidence\":null,\"headline\":\"the result is picked up by later means\",\"reader_payoff\":\"The reader notices that 105:2 states the result-state first, while the following ayahs specify the means and continue the sound field.\",\"reason\":\"The bridge is retained because it ties the final result word to concrete next-ayah surfaces rather than to generic topic continuity.\",\"representative_source_ids\":[\"QB-25a58320\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:5:form-ii-causative-process","source_type":"word_analysis","support_id":"sup_b2338973829794c1b902","text":"{\"blocking_evidence\":null,\"headline\":\"Form II makes loss processive and causative\",\"reader_payoff\":\"The reader notices that the Form II maṣdar makes the plot's fate feel like causative misdirection and ongoing futility, not a simple static error label.\",\"reason\":\"QAC identifies {{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}) as a Form II verbal noun with causative or intensive force, and the local clause leaves the caused-to-stray patient unexpressed.\",\"representative_source_ids\":[\"QG-98a0dfe0\",\"QF-42f40278\",\"QF-6e3392d9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:1:paired-question-frame","source_type":"word_analysis","support_id":"sup_b7d8dd4a73b81f610e71","text":"{\"blocking_evidence\":null,\"headline\":\"second opening repeats the question frame\",\"reader_payoff\":\"The reader notices that {{ar:أَلَمْ}} ({{tr:alam}}) in 105:2 reprises the opening question of 105:1, moving from perception of the event to acknowledgment of its verdict.\",\"reason\":\"The local surface repeats the same negative-question frame used at the start of 105:1, and translation support warns against flattening 105:2 into a simple information question.\",\"representative_source_ids\":[\"QT-e4c02055\",\"QE-08b4e722\",\"QB-b1f13885\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:1:jussive-completed-negation","source_type":"word_analysis","support_id":"sup_bfbf9ed1d3e136bafc2c","text":"{\"blocking_evidence\":null,\"headline\":\"jussive negation makes the action completed\",\"reader_payoff\":\"The reader notices that {{ar:أَلَمْ}} ({{tr:alam}}) does not leave {{ar:يَجْعَلْ}} ({{tr:yajʿal}}) as an open imperfect; it grammatically closes the action as completed and decisive.\",\"reason\":\"QAC and attachment evidence confirm that the lām inside {{ar:أَلَمْ}} ({{tr:alam}}) governs {{ar:يَجْعَلْ}} ({{tr:yajʿal}}) in the jussive. The source row's stronger claim that the shortened form enacts the scheme's cutting off is kept only as sound-color, not as grammatical proof.\",\"representative_source_ids\":[\"QG-48d3be96\",\"MG-616e5039\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:4:compact-result-cadence","source_type":"word_analysis","support_id":"sup_d4b3fe345a499cf16e6c","text":"{\"blocking_evidence\":null,\"headline\":\"the preposition binds into the result sound\",\"reader_payoff\":\"The reader notices that the long ī of {{ar:فِى}} ({{tr:fī}}) pulls the ear directly into {{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}), making the result phrase feel compact.\",\"reason\":\"The cadence claim is anchored in the adjacent local surfaces and treated as an audible binding of syntax.\",\"representative_source_ids\":[\"QP-0aa9f732\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:4:abstract-result-containment","source_type":"word_analysis","support_id":"sup_d667103fa7d13e531586","text":"{\"blocking_evidence\":null,\"headline\":\"fī makes loss a containing result\",\"reader_payoff\":\"The reader notices that {{ar:فِى}} ({{tr:fī}}) makes the plot sit inside an abstract state of loss rather than merely becoming a second predicate.\",\"reason\":\"Attachment evidence makes {{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}) the prepositional result complement. The stronger source imagery of an unbounded ocean is narrowed to abstract containment because the local grammar gives a state, not a literal space.\",\"representative_source_ids\":[\"QG-4049ab21\",\"MG-ae1b6e2c\",\"QS-7f4be1ed\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:3:masdar-object-pivot","source_type":"word_analysis","support_id":"sup_e1d8639b797f5f4cc051","text":"{\"blocking_evidence\":null,\"headline\":\"the plotted action becomes the object\",\"reader_payoff\":\"The reader notices that the thing acted on is not first the army or the people but the verbal noun naming their scheme.\",\"reason\":\"QAC identifies {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) as a maṣdar in accusative case, and attachment evidence makes it the direct object of {{ar:يَجْعَلْ}} ({{tr:yajʿal}}).\",\"representative_source_ids\":[\"QG-7b7c06cc\",\"QF-4e617787\",\"QT-0289ef36\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:5:final-closure-and-sound-field","source_type":"word_analysis","support_id":"sup_e525a9aec8ecabbe47a7","text":"{\"blocking_evidence\":null,\"headline\":\"the final word becomes semantic and acoustic seal\",\"reader_payoff\":\"The reader notices that the ayah withholds its verdict until {{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}), where semantic loss and closing cadence arrive together.\",\"reason\":\"The word is the final content term of the clause and supplies the state into which the plot is placed.\",\"representative_source_ids\":[\"QT-c0558404\",\"QT-ce1faef4\",\"QY-5ed8ce8a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:2:root-range-narrowed-to-rendering","source_type":"word_analysis","support_id":"sup_e9fe5cda7d2b39b463a5","text":"{\"blocking_evidence\":null,\"headline\":\"broad making range narrows locally\",\"reader_payoff\":\"The reader notices that the broad {{ar:ج ع ل}} ({{tr:j-ʿ-l}}) range sharpens here into placing and rendering a plot inside a result, not into every available branch of making.\",\"reason\":\"V4 lists broad branches for {{ar:ج ع ل}} ({{tr:j-ʿ-l}}), but the local {{ar:جَعَلَ}} ({{tr:jaʿala}}) X {{ar:فِى}} ({{tr:fī}}) Y construction selects the placing-rendering branch. Reward, creature-name, and beginning branches are not licensed here.\",\"representative_source_ids\":[\"MG-265f5f32\",\"QS-6d87e0d2\",\"QS-ee017072\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:3:scheme-before-people-boundary","source_type":"word_analysis","support_id":"sup_eab68b24b2bddaf12318","text":"{\"blocking_evidence\":null,\"headline\":\"the verse zooms from actors to scheme\",\"reader_payoff\":\"The reader notices the ayah's forensic zoom: after the group is named in 105:1, 105:2 isolates their intention-system and gives that scheme the first verdict.\",\"reason\":\"The suffix depends on the 105:1 antecedent, while the local object role makes the plot itself the focus of the verdict.\",\"representative_source_ids\":[\"QT-658fd753\",\"QB-12b40359\",\"QB-4a0c817e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:5:form-choice-rarity","source_type":"word_analysis","support_id":"sup_eb49f38a7c40303473b7","text":"{\"blocking_evidence\":null,\"headline\":\"the selected maṣdar is non-default\",\"reader_payoff\":\"The reader notices that common {{ar:ض ل ل}} ({{tr:ḍ-l-l}}) language was available, yet this ayah closes on the marked Form II maṣdar {{ar:تَضْلِيلٍ}} ({{tr:taḍlīlin}}).\",\"reason\":\"The rarity claim survives as distributional salience, while stronger claims about absolute reservation or violent intensity are narrowed to the locally supported Form II causative or intensive pressure.\",\"representative_source_ids\":[\"QF-388820bc\",\"QI-f3be77ee\",\"QH-c5634fd1\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:1:abrupt-question-onset","source_type":"word_analysis","support_id":"sup_f5fcecfde485c644bf35","text":"{\"blocking_evidence\":null,\"headline\":\"hamza gives an audible onset\",\"reader_payoff\":\"The reader notices that question-force and negation arrive fused in one compact opening token, with the hamza making the demand for acknowledgment audible from the first sound.\",\"reason\":\"The surface is a fused interrogative-negative particle, and QAC identifies the interrogative hamza as part of the local grammar.\",\"representative_source_ids\":[\"QF-a22cc64f\",\"QI-ce825343\",\"QP-b0393340\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"105:2:2:1","source_type":"qac_morpheme","support_id":"sup_fb40accbab3723645e4e","text":"{\"lemma_ar\":\"جَعَلَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:jaEala|ROOT:jEl|3MS|MOOD:JUS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"105:2:2:1\",\"qac_word_ref\":\"105:2:2\",\"root_ar\":\"ج ع ل\",\"surface_ar\":\"يَجْعَلْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:2:2:locative-resultative-frame","source_type":"word_analysis","support_id":"sup_fd7747598dd24256bb1f","text":"{\"blocking_evidence\":null,\"headline\":\"object and result-state define the verb\",\"reader_payoff\":\"The reader notices that {{ar:يَجْعَلْ}} ({{tr:yajʿal}}) does not merely say the plot became loss; it renders the plot by placing it into the state named by {{ar:فِى تَضْلِيلٍ}} ({{tr:fī taḍlīlin}}).\",\"reason\":\"The local frame is object plus prepositional complement: {{ar:كَيْدَهُمْ}} ({{tr:kaydahum}}) is the direct object and {{ar:فِى تَضْلِيلٍ}} ({{tr:fī taḍlīlin}}) is the result-state complement.\",\"representative_source_ids\":[\"QG-6d9ad300\",\"QG-8adff4ef\",\"QS-ef95c6b3\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍۢ","ayah_ref":"105:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000248/B002","root_000913/B001","root_001334/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000248","role":"Supplies conversion into a resultant state, making the scheme rather than only its owners the patient of change.","root":"ج ع ل","source_ref":"105:2","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001334","role":"Supplies a calculated stratagem with an intended causal route that can be turned against its own aim.","root":"ك ي د","source_ref":"105:2","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000913","role":"Supplies deviation from guidance and intended course as the state imposed on the stratagem.","root":"ض ل ل","source_ref":"105:2","source_word_indices":["5"]}],"changed_reading":{"after":"Their plan was made to enact its own failure by departing from the very aim for which it had been designed.","before":"Their plan was simply foiled."},"confidence":"strong","focus_anchor":"The scheme is the direct object of a state-changing verb and is placed inside a result state by the construction كَيْدَهُمْ فِي تَضْلِيلٍ.","mechanism":"A deliberately contrived path toward an aim is itself converted into deviation from that aim. The failure is therefore internal to the scheme's operation: its means continue as means that no longer conduct their owners to their intended end.","model_id":"b01-purpose-reversal"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01-purpose-reversal","source_type":"hft","support_id":"sup_700eab952f67d317e573","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍۢ","ayah_ref":"105:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000248/B002","root_000913/B003","root_001334/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000248","role":"Supplies an imposed change of condition from usable operation to lost expenditure.","root":"ج ع ل","source_ref":"105:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001334","role":"Supplies strenuous working of a matter, allowing the scheme to include effort and operational investment.","root":"ك ي د","source_ref":"105:2","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000913","role":"Supplies loss from an owner and failure to locate what was possessed, making the invested operation unrecoverable.","root":"ض ل ل","source_ref":"105:2","source_word_indices":["5"]}],"changed_reading":{"after":"The whole investment of force became lost output: theirs in expenditure, but no longer theirs as a recoverable instrument.","before":"The intended result was denied."},"confidence":"medium","focus_anchor":"The possessive in كَيْدَهُمْ makes the operation theirs, while فِي تَضْلِيلٍ can hold that owned operation inside a condition of loss.","mechanism":"The scheme is not only an idea but strenuous handling and exertion. Making it lost or unlocatable turns invested labor, coordination, and force into expenditure that cannot be recovered by its owners.","model_id":"b02-spent-effort-lost"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02-spent-effort-lost","source_type":"hft","support_id":"sup_7981bcc602ead38ea3eb","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍۢ","ayah_ref":"105:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000248/B002","root_000913/B002","root_001334/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000248","role":"Supplies entry into a transformed condition rather than a bare declaration of failure.","root":"ج ع ل","source_ref":"105:2","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001334","role":"Supplies the hidden, organized contrivance whose coherence can be erased.","root":"ك ي د","source_ref":"105:2","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000913","role":"Supplies disappearance, concealment, and absorption into something else as a distinct result from directional error.","root":"ض ل ل","source_ref":"105:2","source_word_indices":["5"]}],"changed_reading":{"after":"The scheme was put into an absorptive loss in which its coherence and causal visibility disappeared.","before":"The scheme remained identifiable but unsuccessful."},"confidence":"medium","focus_anchor":"The preposition فِي permits a container-like reading of the scheme being put within تضليل rather than merely receiving an external verdict.","mechanism":"The contrivance is made to disappear or become absorbed into an outcome that erases its operative identity. It does not merely miss; it ceases to remain legible as a coherent causal instrument.","model_id":"b03-operative-disappearance"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03-operative-disappearance","source_type":"hft","support_id":"sup_42d4c5fd159c0d49ffad","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍۢ","ayah_ref":"105:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000248/B002","root_000913/B001","root_001334/B004"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000248","role":"Supplies the conversion of an active campaign capacity into a disabled condition.","root":"ج ع ل","source_ref":"105:2","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001334","role":"Supplies war and battle as a live scope for the possessed operation.","root":"ك ي د","source_ref":"105:2","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000913","role":"Supplies departure from the intended course, here applied to martial deployment.","root":"ض ل ل","source_ref":"105:2","source_word_indices":["5"]}],"changed_reading":{"after":"An entire capacity to wage the campaign was made unable to travel its intended operational course.","before":"A private stratagem was mentally confused."},"confidence":"exploratory","focus_anchor":"The noun كَيْد can activate an attested battle domain, while the possessed plural pronoun allows the focus to encompass collective campaign capacity.","mechanism":"The object being transformed can be the expedition's capacity for battle, not only a secret design. Its martial force is made directionless and unable to arrive as effective combat.","model_id":"b04-battle-capacity-derailed"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b04-battle-capacity-derailed","source_type":"hft","support_id":"sup_a2c64243a9915c58da2b","trust":"legacy_unbound"}]}
</lane_packet_json>
