# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **105:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s105-regular-20260911/s105/105_3/micro.discovery.json` and modify nothing
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
  "ayah_ref": "105:3",
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
{"analysis_context":{"analysis_id":"s105-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"105:3","host_surah":105,"lane_context_refs":[],"ordered_context_refs":["105:0","105:1","105:2","105:4","105:5","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Deve topluluğu çekirdektir; edinme, sahiplik ve bakım ustalığı buna bağlı kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000006/B001","candidate_links":[{"candidate_id":"cand_d85c77f21ae6775397f9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَبَابِيل","morph_features":"STEM|POS:ADJ|LEM:>abaAbiyl|ROOT:Abl|MP|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"105:3:4:1","qac_word_ref":"105:3:4","surface_ar":"أَبَابِيلَ"}],"gloss":"deve topluluğu, sahipliği ve bakım ustalığı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tekili aynı sözcükten yapılmayan, toplu develeri bildiren ad."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Develerin çok olması, edinilmesi veya elde tutulan topluluklar halinde bulunması."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Deve sahibi olma, deve bakımında usta olma ve onların yanında kalıp bakımı sürdürme."}}],"root_ar":"ء ب ل","root_id":"root_000006","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın topluluk çekirdeğini ve ona bağlı sahiplik ile bakım kullanımlarını birlikte gösteren üst karşılıktır.","boundary_detail":"Deve topluluğu çekirdektir; edinme, sahiplik ve bakım ustalığı buna bağlı kullanımlardır.","branch_image_ar":"الإبل ورعايتها","concept_gloss":"deve topluluğu, sahipliği ve bakım ustalığı","contextual_glosses":[{"applicability":"Yalnızca toplu hayvan adının geçtiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Edinme, sahiplik, bakım ustalığı ve bakımda süreklilik kullanımlarını göstermez.","preserves":"Toplu deve adı çekirdeğini doğal biçimde korur."},"facet_ids":["F001"],"text":"develer","usage_role":"general"},{"applicability":"Bir kişinin hayvanların bakımını iyi bilmesini anlatan kuruluşlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Topluluk adı, çokluk, edinme ve sahiplik yönlerini kapsamaz.","preserves":"Bakım bilgisini ve ustalığını açıkça korur."},"facet_ids":["F003"],"text":"deve bakımında usta olmak","usage_role":"contextual"}],"definition":"Develeri topluca adlandıran çekirdeğin çevresinde, çok sayıda deve edinip elde tutma, onların sahibi olma, bakımlarını iyi bilme ve bu bakımı sürdürme anlamları yer alır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tekili aynı sözcükten yapılmayan, toplu develeri bildiren ad."},{"facet_id":"F002","role":"extension","statement":"Develerin çok olması, edinilmesi veya elde tutulan topluluklar halinde bulunması."},{"facet_id":"F003","role":"associated_use","statement":"Deve sahibi olma, deve bakımında usta olma ve onların yanında kalıp bakımı sürdürme."}],"identity_rationale":"Kaynak ifadesi yalnızca develeri ve deve topluluğunu değil, bunları edinmeyi, çokluğunu, sahibini ve bakımlarında usta olmayı da kapsar. Bu nedenle dal, hayvan adından ibaret olmayan bir deve sahipliği ve bakımı alanı olarak sınırlandırılmıştır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"develer; tekili aynı kökten olmayan topluluk adı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"çok sayıda ya da elde tutulan toplu develer"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"deve sahibi veya deve bakımında usta kimse"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"deve ve koyun bakımını iyi bilmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"develerin yanında durmamak ya da bakımlarını sürdürmemek"}],"lexicalization_note":"Tanım, yalın topluluk adını ayrı tutar; edinme, sahiplik, ustalık ve bakımda sebat anlamlarını yalnızca ilgili biçim ve kuruluşlara bağlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yararlı sınır karşılaştırması bakım ustalığı alanındaki yakın komşuyla verildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal deve topluluğundan türeyen sahiplik ve bakım kullanımlarını bir araya getirir; komşu ise iyi yöneticiyi, deve dışındaki malı da içine alan kişi niteliği olarak tanımlar.","focus_only":"Develerin toplu adı, edinilmesi, çokluğu ve sahibi olma anlamları da bu daldadır.","gloss":"deve ve mal bakımını iyi bilen kimse","neighbor_only":"Komşu dal, kişinin genel malını iyi yönetmesini de kapsar.","neighbor_ref":"root_000853/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da develerin bakımını ve bu bakım konusundaki bilgiyi içerir."}],"source_phrase_ar":"الإبل معروفة ورجل آبل ومال مؤبل (maqayis)؛ الإبل لا واحد لها وإبل مؤبلة ورجل إبلي وأبل الرجل اتخذ إبلا (sihah)؛ إبل مؤبلة كثيرة وأبل الرجل إذا كثرت إبله وتأبل فلان إبلا (tahdhib)؛ الإبل يقع على البعران الكثيرة وأبل الرجل كثرت إبله ورجل آبل وأبل (mufradat)","source_summary":"Kaynaklar, toplu deve adında birleşir ve bu çekirdeğe develerin çokluğu veya edinilmesi ile sahibin bakım bilgisi ve bakımda sürekliliğini bağlar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه اسم الإبل وجماعتها وقطعانها وكثرتها واقتناؤها وصاحبها والحذق برعايتها والثبات عليها","what_is_not_ar":"ليس الاجتزاء عن الماء ولا الطير الأبابيل ولا حزمة الحطب ولا الراهب"},"support_links":["sup_630a2304256207d9379f"]},{"boundary":"Susuz kalma çekirdeği hayvana özgüdür; cinsel uzak durma yalnızca benzetmeli kuruluşa bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000006/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبَابِيل","morph_features":"STEM|POS:ADJ|LEM:>abaAbiyl|ROOT:Abl|MP|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"105:3:4:1","qac_word_ref":"105:3:4","surface_ar":"أَبَابِيلَ"}],"gloss":"yaş otla yetinip sudan uzak durma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Deve veya yaban hayvanının yaş otla yetinip su içmeye gerek duymaması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sudan bağımsız kalan hayvanın bulunduğu yerden ayrılmaması."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Erkeğin kadına yaklaşmaktan kaçınmasının hayvanın sudan uzak durmasına benzetilmesi."}}],"root_ar":"ء ب ل","root_id":"root_000006","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvana ilişkin çekirdeği doğrudan karşılar; insana ilişkin benzetmeli kullanım açıklama gerektirir.","boundary_detail":"Susuz kalma çekirdeği hayvana özgüdür; cinsel uzak durma yalnızca benzetmeli kuruluşa bağlıdır.","branch_image_ar":"الاجتزاء عن الماء","concept_gloss":"yaş otla yetinip sudan uzak durma","contextual_glosses":[{"applicability":"Yalnızca erkeğin kadınla cinsel yakınlıktan kaçınmasını anlatan kuruluşa uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanın yaş otla yetinip su içmemesi olan temel görüntüyü vermez.","preserves":"İnsana aktarılan uzak durma sonucunu açıkça korur."},"facet_ids":["F003"],"text":"kadına yaklaşmaktan uzak durmak","usage_role":"contextual"}],"definition":"Deve veya yaban hayvanının yaş otla yetinip su içmeden bulunduğu yerde kalmasıdır. Buna benzetilerek, bir erkeğin kadına yaklaşmaktan kaçınması da belirli bir kuruluşta anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Deve veya yaban hayvanının yaş otla yetinip su içmeye gerek duymaması."},{"facet_id":"F002","role":"specialization","statement":"Sudan bağımsız kalan hayvanın bulunduğu yerden ayrılmaması."},{"facet_id":"F003","role":"extension","statement":"Erkeğin kadına yaklaşmaktan kaçınmasının hayvanın sudan uzak durmasına benzetilmesi."}],"identity_rationale":"Kaynak ifadesi, deve veya yaban hayvanının yaş otla yetinerek suya ihtiyaç duymamasını çekirdek anlam yapar ve erkeğin kadına yaklaşmamasını buna benzetilen ayrı bir kullanım olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"develerin veya yaban hayvanlarının yaş otla yetinip su içmemesi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"suya gerek duymadan bulunduğu yerde kalan hayvan"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yaş otla yetinip su içmeyen develer veya yaban hayvanları"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"erkeğin kadına yaklaşmaktan kaçınması"}],"lexicalization_note":"Hayvanın yaş otla sudan bağımsız kalması ile erkeğin kadından uzak durduğu kuruluş birbirine karıştırılmadan ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; su içmeme ile suya götürmeyi geciktirme arasındaki ayrım en açıklayıcı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal doğal bir yeterlilik ve ihtiyaç duymama durumudur; komşu dal ise suya erişimin bir veya daha çok gün geciktirilmesi işlemidir.","focus_only":"Hayvan yaş ottan yeterli nemi aldığı için suya ihtiyaç duymaz.","gloss":"hayvanı sudan bir süre daha alıkoyma","neighbor_only":"Hayvanın suya götürülmesi, susuzluk süresi uzatılarak bilerek geciktirilir.","neighbor_ref":"root_001493/B004","relation_type":"same_field","shared_zone":"Her iki dal da develerin su içmeden geçirdiği süreyle ilgilidir."}],"source_phrase_ar":"بعير آبل في موضع لا يبرح يجتزئ عن الماء وتأبل الرجل عن المرأة (maqayis)؛ أبلت الإبل والوحش اجتزأت بالرطب عن الماء وأبل الرجل عن امرأته (sihah)؛ أبلت الوحش إذا جزأت بالرطب عن الماء وإبل أوابل قد جزأت (tahdhib)؛ أبل الوحشي اجتزأ عن الماء وتأبل الرجل عن امرأته (mufradat)","source_summary":"Kaynaklar, hayvanın yaş ot sayesinde su içmeden yetinmesinde birleşir; ayrıca kadına yaklaşmaktan uzak durmayı bu duruma benzetilen kullanım olarak aktarır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه اجتزاء الإبل أو الوحش بالرطب عن الماء وما شبه به من ترك مقاربة المرأة","what_is_not_ar":"ليس أصل اسم الإبل ولا كثرتها ولا جماعات الطير"},"support_links":[]},{"boundary":"Belirleyici özellik tek bir topluluk olmak değil, ayrı kümeler halinde dağılmak veya art arda gelmektir.","branch_kind":"bare","branch_ref":"root_000006/B003","candidate_links":[{"candidate_id":"cand_ab8f894712f8f7114996","lane":"micro"},{"candidate_id":"cand_b75059b67363bfe60022","lane":"micro"},{"candidate_id":"cand_9a0e4e7327fa2b496ecf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَبَابِيل","morph_features":"STEM|POS:ADJ|LEM:>abaAbiyl|ROOT:Abl|MP|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"105:3:4:1","qac_word_ref":"105:3:4","surface_ar":"أَبَابِيلَ"}],"gloss":"ayrı ayrı veya art arda gelen topluluklar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birbirinden ayrı ve dağınık kümeler halinde bulunan topluluklar."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kümenin ardından başka bir kümenin geldiği art arda topluluklar."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kuşların veya develerin ayrı kümeler halinde tasvir edilmesi."}}],"root_ar":"ء ب ل","root_id":"root_000006","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dağınıklık ve ardışıklık açıklamalarını birlikte taşıyan en geniş doğal karşılıktır.","boundary_detail":"Belirleyici özellik tek bir topluluk olmak değil, ayrı kümeler halinde dağılmak veya art arda gelmektir.","branch_image_ar":"الجماعات الأبابيل","concept_gloss":"ayrı ayrı veya art arda gelen topluluklar","contextual_glosses":[{"applicability":"Hayvanların ayrı kümeler veya peş peşe topluluklar halinde geldiği anlatımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayrı kümeler halindeki çokluğu ve art arda gelişi bağlam içinde korur."},"facet_ids":["F001","F002","F003"],"text":"sürü sürü","usage_role":"contextual"}],"definition":"Birbirinden ayrı kümeler halinde bulunan veya bir küme ötekini izleyecek biçimde art arda gelen topluluklardır; kullanım özellikle kuşlar, ayrıca develer için görülür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birbirinden ayrı ve dağınık kümeler halinde bulunan topluluklar."},{"facet_id":"F002","role":"source_variant","statement":"Bir kümenin ardından başka bir kümenin geldiği art arda topluluklar."},{"facet_id":"F003","role":"example","statement":"Kuşların veya develerin ayrı kümeler halinde tasvir edilmesi."}],"identity_rationale":"Kaynak ifadesi, özellikle kuşlar için kullanılan fakat deve topluluklarına da uygulanabilen, birbirinden ayrı kümeler veya art arda gelen topluluklar anlamını açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ayrı kümeler halinde veya birbiri ardınca gelen topluluklar"}],"lexicalization_note":"Tanım yalın biçimin dağınık ya da birbirini izleyen topluluklar anlamıyla sınırlıdır ve başka dalların kuruluş anlamlarını almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ayrı kümeler ile zorunlu art arda geliş arasındaki sınır en yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ayrılığı hem dağınıklık hem ardışıklık olarak kapsar; komşu dalda art arda geliş veya gönderiliş temel sınırdır.","focus_only":"Topluluklar ayrı ve dağınık kümeler olarak da bulunabilir; ardışıklık zorunlu değildir.","gloss":"küme küme, birbiri ardınca gelme","neighbor_only":"Komşu dal, insanların veya hayvanların bir küme ardından öteki gelecek biçimde gönderilmesini ya da gelişini vurgular.","neighbor_ref":"root_000563/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da tek bir yığın yerine birden çok ayrı topluluğu anlatabilir."}],"source_phrase_ar":"طيرا أبابيل أي يتبع بعضها بعضا (maqayis)؛ جاءت إبلك أبابيل أي فرقا وطير أبابيل (sihah)؛ طيرا أبابيل جماعات وقيل يتبع بعضها بعضا إبيلا إبيلا (tahdhib)؛ طيرا أبابيل أي متفرقة كقطعات إبل (mufradat)","source_summary":"Kaynaklar sözü çoğul topluluklar için verir; açıklamalar bu toplulukların ayrı ve dağınık olması ile birbiri ardınca gelmesi arasında değişir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه أبابيل للطير أو الجماعات المتفرقة أو المتتابعة بعضا بعد بعض","what_is_not_ar":"ليس اسم الإبل نفسه ولا اجتزاءها عن الماء"},"support_links":["sup_30f767751a30a01b43e7","sup_3bb8eb72d603fbb2a398","sup_d5bf3c1aefa3e3bb9755"]},{"boundary":"Ağırlık ortak görüntüdür; hukuki-ahlaki yük, ayıp, ihtiyaç ve üstün gelme ayrı kullanımlar olarak korunur.","branch_kind":"mixed_non_bare","branch_ref":"root_000006/B004","candidate_links":[{"candidate_id":"cand_eefb4ed317c3cc5e44e9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَبَابِيل","morph_features":"STEM|POS:ADJ|LEM:>abaAbiyl|ROOT:Abl|MP|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"105:3:4:1","qac_word_ref":"105:3:4","surface_ar":"أَبَابِيلَ"}],"gloss":"ağırlık, yükümlülük veya ayıp","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağırlık veya yiyeceğin bedene ağır gelmesi."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin üzerinden çıkabileceği bir yükümlülük, kınanma veya ayıp."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Giderilecek ihtiyaç veya öç ile üstün gelip direnme anlamları."}}],"root_ar":"ء ب ل","root_id":"root_000006","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın temel ad kullanımlarını kapsar; ihtiyaç, öç ve üstün gelme kuruluşları ayrıca belirtilmelidir.","boundary_detail":"Ağırlık ortak görüntüdür; hukuki-ahlaki yük, ayıp, ihtiyaç ve üstün gelme ayrı kullanımlar olarak korunur.","branch_image_ar":"الثقل والتبعة","concept_gloss":"ağırlık, yükümlülük veya ayıp","contextual_glosses":[{"applicability":"Yalnızca bir kişinin üstün gelmesi ve boyun eğmemesi anlatılan fiil kuruluşunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ağırlık, yükümlülük, kınanma, ayıp, ihtiyaç ve öç anlamlarını dışarıda bırakır.","preserves":"Üstünlük kazanma ve direnme sonucunu korur."},"facet_ids":["F003"],"text":"üstün gelip direnmek","usage_role":"contextual"}],"definition":"Bir şeyin ağır veya sindirimi güç olması ve kişinin üzerinde yükümlülük, kınanma ya da ayıp bırakmasıdır. Belirli biçim ve kuruluşlarda giderilecek bir ihtiyaç veya öç ile üstün gelip direnme de anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağırlık veya yiyeceğin bedene ağır gelmesi."},{"facet_id":"F002","role":"extension","statement":"Kişinin üzerinden çıkabileceği bir yükümlülük, kınanma veya ayıp."},{"facet_id":"F003","role":"associated_use","statement":"Giderilecek ihtiyaç veya öç ile üstün gelip direnme anlamları."}],"identity_rationale":"Kaynak ifadesi ağırlık ve yiyeceğin ağır gelmesi çekirdeğine yükümlülük, kınanma, ayıp, giderilecek ihtiyaç veya öç ile üstün gelip direnme kullanımlarını ekler. Bunlar tek bir yalın eşdeğere indirgenemeyecek bağlı yönlerdir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ağırlık, ağır gelme, yükümlülük veya kınanma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"üstün gelip direnmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bunda senin için bir ayıp yok"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"giderilecek ihtiyaç veya öç"}],"lexicalization_note":"Yalın biçimlerin ağırlık ve yük anlamları, yalnızca belirli kuruluşlarda görülen ayıpsızlık, ihtiyaç, öç ve üstün gelme anlamlarından ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ağır yük ile daha geniş ağırlık ve ayıp alanı arasındaki karşılaştırma sınırı en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal fiziksel ağırlıktan ayıp ve kınanmaya uzanan daha dağınık kullanımlara sahiptir; komşu dal taşınan yük ve bağlayıcı sorumlulukta yoğunlaşır.","focus_only":"Yiyeceğin ağır gelmesi, ayıp, kınanma, ihtiyaç, öç ve üstün gelip direnme kullanımları vardır.","gloss":"taşınan ağır yük veya bağlayıcı sorumluluk","neighbor_only":"Komşu dal özellikle taşınan yükü, günahı veya bağlayıcı ağır sözü anlatır.","neighbor_ref":"root_000037/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin üzerinde bulunan ağır yük veya sorumluluk görüntüsünü paylaşır."}],"source_phrase_ar":"أبل الرجل إذا غلب وامتنع والأبلة الثقل وذهبت أبلته (maqayis)؛ الأبلة الوخامة والثقل من الطعام وذهبت أبلته (sihah)؛ ما عليك فيه أبلة ولا أبنة أي لا عيب وخرجت من أبلته أي من تبعته ومذمته (tahdhib)","source_summary":"Kaynaklar ağırlık ekseninde birleşir; toplu kanıt yiyeceğin ağır gelmesini, yükümlülük ve kınanmayı, ayıbı, ihtiyaç veya öcü ve üstün gelip direnmeyi farklı kullanımlar halinde gösterir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الأبلة بمعنى الثقل أو الوخامة أو التبعة أو المذمة أو العيب ويدخل فيه الغلبة والامتناع إذا حمل على ثقل الأمر","what_is_not_ar":"ليس حزمة الحطب ولا الفدرة من التمر ولا القبيلة"},"support_links":["sup_8bdbc1e3ecbdfcad74d9"]},{"boundary":"Yakacak odun demeti nesne anlamıdır; sıkıntı üstüne sıkıntı yalnızca kalıplaşmış söze bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000006/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبَابِيل","morph_features":"STEM|POS:ADJ|LEM:>abaAbiyl|ROOT:Abl|MP|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"105:3:4:1","qac_word_ref":"105:3:4","surface_ar":"أَبَابِيلَ"}],"gloss":"yakacak odun demeti","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir araya bağlanmış yakacak odun demeti."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir sıkıntının üstüne başka bir sıkıntı gelmesini anlatan kalıplaşmış söz."}}],"root_ar":"ء ب ل","root_id":"root_000006","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesne anlamını tam karşılar; kalıplaşmış sıkıntı anlatımı bağlam içinde ayrıca çevrilir.","boundary_detail":"Yakacak odun demeti nesne anlamıdır; sıkıntı üstüne sıkıntı yalnızca kalıplaşmış söze bağlıdır.","branch_image_ar":"إبالة الحطب","concept_gloss":"yakacak odun demeti","contextual_glosses":[{"applicability":"Yalnızca küçük demetin odun demeti üzerine konmasına dayanan kalıplaşmış söz için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Somut yakacak odun demeti anlamını göstermez.","preserves":"Bir olumsuzluğa yenisinin eklenmesi sonucunu korur."},"facet_ids":["F002"],"text":"sıkıntı üstüne sıkıntı","usage_role":"contextual"}],"definition":"Bir araya bağlanmış yakacak odun demetidir. Bu demetin üstüne başka bir küçük demet koyma görüntüsü, kalıplaşmış bir sözde sıkıntı üstüne sıkıntı gelmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir araya bağlanmış yakacak odun demeti."},{"facet_id":"F002","role":"associated_use","statement":"Bir sıkıntının üstüne başka bir sıkıntı gelmesini anlatan kalıplaşmış söz."}],"identity_rationale":"Kaynak ifadesi bir demet yakacak odunu açık çekirdek olarak verir ve bunun üzerine bir küçük demet eklenmesi görüntüsünden, bir sıkıntının üstüne başka sıkıntı gelmesi sözünü kurar.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yakacak odun demeti"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"sıkıntı üstüne sıkıntı"}],"lexicalization_note":"Yalın biçimin yakacak odun demeti anlamı ile kalıplaşmış sözün üst üste gelen sıkıntı anlamı ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; malzeme bakımından en yakın demet adıyla yapılan karşılaştırma yayımlanmaya değer bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal malzemeyi yakacak odunla sınırlar ve deyimleşmiş bir uzantı taşır; komşu dal başka bitkisel malzemelerden yapılan demeti adlandırır.","focus_only":"Demet özellikle yakacak odundan oluşur ve kalıplaşmış sıkıntı sözüne temel olur.","gloss":"ot veya yem bitkisi demeti","neighbor_only":"Komşu dal yemlik bitkiler ve benzeri otların demetini de bildirir.","neighbor_ref":"root_000236/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da uzun bitkisel parçaların bir araya getirilmiş demetini anlatır."}],"source_phrase_ar":"الإبالة الحزمة من الحطب (maqayis)؛ الإبالة الحزمة من الحطب وضغث على إبالة (sihah)؛ ضغث على إبالة (tahdhib)؛ الإبالة الحزمة من الحطب (mufradat)","source_summary":"Kaynaklar yakacak odun demeti anlamında birleşir ve demetin üzerine küçük bir demet ekleme görüntüsünü üst üste gelen sıkıntılar için kullanılan sözle ilişkilendirir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الإبالة للحزمة من الحطب والمثل ضغث على إبالة","what_is_not_ar":"ليس جماعة الإبل ولا الجماعات الأبابيل"},"support_links":[]},{"boundary":"Hristiyan din görevlisi ortak çekirdektir; yöneticilik ve çan çalma kaynaklarda görülen görev ayrıntılarıdır.","branch_kind":"bare","branch_ref":"root_000006/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبَابِيل","morph_features":"STEM|POS:ADJ|LEM:>abaAbiyl|ROOT:Abl|MP|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"105:3:4:1","qac_word_ref":"105:3:4","surface_ar":"أَبَابِيلَ"}],"gloss":"Hristiyan manastır din görevlisi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hristiyanlar arasında manastır yaşamı süren veya din hizmeti gören kişi."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üst düzey bir din görevlisi veya çanı çalmakla görevli kişi olarak açıklanması."}}],"root_ar":"ء ب ل","root_id":"root_000006","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ortak görev alanını karşılar; yöneticilik veya çan çalma ayrıntısı gerektiğinde bağlamla belirtilir.","boundary_detail":"Hristiyan din görevlisi ortak çekirdektir; yöneticilik ve çan çalma kaynaklarda görülen görev ayrıntılarıdır.","branch_image_ar":"الأبيل الراهب","concept_gloss":"Hristiyan manastır din görevlisi","contextual_glosses":[{"applicability":"Kaynağın kişiyi din topluluğunun yöneticilerinden biri olarak sunduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıradan manastır görevlisi ve çan çalan görevli açıklamalarını kapsamaz.","preserves":"Din görevliliğini ve yönetici konumunu korur."},"facet_ids":["F001","F002"],"text":"üst düzey Hristiyan din görevlisi","usage_role":"contextual"}],"definition":"Hristiyanlar arasında manastır yaşamı süren veya din hizmeti gören kişi; bazı açıklamalarda üst düzey görevli, bazılarında çanı çalan görevli olarak belirginleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hristiyanlar arasında manastır yaşamı süren veya din hizmeti gören kişi."},{"facet_id":"F002","role":"source_variant","statement":"Üst düzey bir din görevlisi veya çanı çalmakla görevli kişi olarak açıklanması."}],"identity_rationale":"Kaynaklar Hristiyan din görevlisi üzerinde birleşmekle birlikte onun manastır yaşamındaki görevli, üst düzey görevli veya çan çalan kişi oluşunu farklı biçimlerde açıklar. Tanım bu görev çeşitlerini tek bir zorunlu makam saymaz.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"Hristiyan manastır görevlisi, üst düzey din görevlisi veya çan çalan görevli"}],"lexicalization_note":"Tanım yalın görev adını kapsar ve komşu din görevlisi adlarının özel makam sınırlarını bu dala taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın görev adıyla makam ve işlev farkını gösteren karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal manastır, yöneticilik veya çan görevi çevresinde tanımlanır; komşu dal öğrenim ve ibadet niteliğini öne çıkaran başka bir görev adıdır.","focus_only":"Manastır görevliliği ve çan çalma açıklamaları bu dala özgü olabilir.","gloss":"bilgili ve ibadet eden Hristiyan din adamı","neighbor_only":"Komşu dal bilgili ve ibadet eden Hristiyan din adamını, kendi görev adlarıyla belirtir.","neighbor_ref":"root_001223/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da Hristiyan topluluğundaki din görevlilerini ve kimi yöneticileri adlandırır."}],"source_phrase_ar":"الأبيل من رؤوس النصارى وهو الأبيلى (maqayis)؛ الأبيل الذي يضرب بالناقوس (jamhara)؛ الأبيل راهب النصارى (sihah)؛ الأبيل الراهب الرئيس وهم الأبيلون (tahdhib)","source_summary":"Kaynaklar Hristiyan din görevlisi çekirdeğini paylaşır; görev derecesini manastır görevlisi, yönetici veya çan çalan kişi olarak farklı biçimlerde ayrıntılandırır.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه الأبيل أو الأبيلي لراهب النصارى أو رئيسهم ومن يضرب بالناقوس","what_is_not_ar":"ليس صاحب الإبل ولا حاذق رعايتها"},"support_links":[]},{"boundary":"Anlam yalnızca hurmadan oluşan ayrılmış bir parçadır; başka maddelerin parçaları bu dalın kapsamında değildir.","branch_kind":"bare","branch_ref":"root_000006/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبَابِيل","morph_features":"STEM|POS:ADJ|LEM:>abaAbiyl|ROOT:Abl|MP|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"105:3:4:1","qac_word_ref":"105:3:4","surface_ar":"أَبَابِيلَ"}],"gloss":"iri bir hurma parçası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hurmadan oluşan ayrılmış, sıkı veya iri parça."}}],"root_ar":"ء ب ل","root_id":"root_000006","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hurmadan ayrılmış sıkı veya iri parçayı doğal Türkçeyle tam olarak karşılar.","boundary_detail":"Anlam yalnızca hurmadan oluşan ayrılmış bir parçadır; başka maddelerin parçaları bu dalın kapsamında değildir.","branch_image_ar":"الأُبُلَّة من التمر","concept_gloss":"iri bir hurma parçası","definition":"Hurmadan ayrılmış, sıkı veya iri bir parça.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hurmadan oluşan ayrılmış, sıkı veya iri parça."}],"identity_rationale":"Kaynak ifadesi, hurmadan ayrılmış sıkı veya iri bir parçayı tek ve açık anlam olarak verir; ağırlık, yer adı ve odun demeti dallarıyla karıştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"iri bir hurma parçası"}],"lexicalization_note":"Tanım yalın biçimin hurma parçası anlamıyla sınırlıdır ve benzer sesli öteki dalların anlamlarını içermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; parça biçimini paylaşan fakat maddesi farklı olan komşu, sınırı en açık gösteren adaydır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Biçimsel benzerliğe rağmen odak dal hurmayla, komşu dal ise katı yağla sınırlıdır; bağlamlar arasında doğrudan yer değiştiremezler.","focus_only":"Parçanın maddesi hurmadır.","gloss":"katı yağ parçası","neighbor_only":"Komşu dal katılaşmış, az kalmış veya topak biçimindeki yağı anlatır.","neighbor_ref":"root_001304/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da yenebilir bir maddenin ayrılmış, sıkı parçasını anlatır."}],"source_phrase_ar":"الأبلة الفدرة من التمر (maqayis)؛ الأُبُلَّة الفدرة من التمر (sihah)؛ الأبلة الفدرة من التمر (tahdhib)","source_summary":"Kaynaklar, sözü herhangi bir yiyecek parçası olarak değil, özellikle hurmadan ayrılmış bir parça olarak tanımlar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الأُبُلَّة للفدرة من التمر","what_is_not_ar":"ليس الأبلة للثقل ولا الأبلة للموضع"},"support_links":[]},{"boundary":"Bu dal yalnızca kanıtlanan iki yer adıyla sınırlıdır; benzer biçimli hurma parçası veya ağırlık anlamlarını içermez.","branch_kind":"non_bare","branch_ref":"root_000006/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبَابِيل","morph_features":"STEM|POS:ADJ|LEM:>abaAbiyl|ROOT:Abl|MP|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"105:3:4:1","qac_word_ref":"105:3:4","surface_ar":"أَبَابِيلَ"}],"gloss":"Basra yakınındaki kent ve ayrı bir yer adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Basra yakınında bulunan kentin sözlüksel yer adı."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynakta yalnızca bir yer adı olduğu belirtilen ikinci sözlüksel biçim."}}],"root_ar":"ء ب ل","root_id":"root_000006","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın iki ad kaydını, doğrulanmamış bir ortak ad biçimi üretmeden birlikte özetler.","boundary_detail":"Bu dal yalnızca kanıtlanan iki yer adıyla sınırlıdır; benzer biçimli hurma parçası veya ağırlık anlamlarını içermez.","branch_image_ar":"الموضع المسمى أبلة أو أبلى","concept_gloss":"Basra yakınındaki kent ve ayrı bir yer adı","definition":"Kökle ilişkili iki ayrı yer adı: Basra yakınında bir kent ve kaynakta yalnızca bir yer olduğu belirtilen başka bir ad.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Basra yakınında bulunan kentin sözlüksel yer adı."},{"facet_id":"F002","role":"source_variant","statement":"Kaynakta yalnızca bir yer adı olduğu belirtilen ikinci sözlüksel biçim."}],"identity_rationale":"Kaynak ifadesi iki yer adını aynı dalda toplar: biri Basra yakınındaki kent, diğeri yalnızca bir yer olarak belirtilen ayrı addır. Dal ortak bir kavram değil, kökle ilişkili yer adı kayıtlarının sınırlı kümesidir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"Basra yakınındaki kent"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir yer adı"}],"lexicalization_note":"Tanım iki sözlüksel yer adıyla sınırlıdır; bunlardan hareketle yalın kök için genel bir yer veya kent anlamı kurulmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yer adı türündeki ortaklığı ve gönderim ayrılığını gösteren aday yeterli görüldü.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Dalların ortaklığı yalnızca ad türündedir; gösterdikleri yerler ve sözlüksel biçimler ayrıdır, dolayısıyla birbirlerinin yerine kullanılamaz.","focus_only":"Odak dal, biri Basra yakınındaki kent olan iki belirli yer adı kaydını içerir.","gloss":"başka sözlüksel yer adları","neighbor_only":"Komşu dal başka belirli yer adlarını kendi sözlüksel biçimleriyle kaydeder.","neighbor_ref":"root_000227/B014","relation_type":"same_field","shared_zone":"Her iki dalın birimleri de ortak bir genel nesne türünden çok yer adı olarak işlev görür."}],"source_phrase_ar":"أبلى موضع (maqayis)؛ الأبلة مدينة إلى جنب البصرة (sihah)؛ الأبلة لأبلة البصرة (tahdhib)","source_summary":"Toplu kanıt, kökle ilişkili iki ayrı yer adı kaydeder; bunlardan biri Basra yakınındaki kent olarak belirlenirken öteki yalnızca bir yer olarak tanıtılır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه أبلة الموضع وأبلى الموضع","what_is_not_ar":"ليس الأُبُلَّة من التمر ولا الأبلة بمعنى الثقل"},"support_links":[]},{"boundary":"Anlam yalnızca kişinin kendi boyu içinde gelmesini bildiren kuruluşta geçerlidir.","branch_kind":"collocation","branch_ref":"root_000006/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبَابِيل","morph_features":"STEM|POS:ADJ|LEM:>abaAbiyl|ROOT:Abl|MP|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"105:3:4:1","qac_word_ref":"105:3:4","surface_ar":"أَبَابِيلَ"}],"gloss":"kendi boyuyla birlikte gelmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin kendi boyu veya soy topluluğu içinde, onlarla birlikte gelmesi."}}],"root_ar":"ء ب ل","root_id":"root_000006","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kanıtlanan kuruluşun kişi ve soy topluluğu ilişkisini karşılar.","boundary_detail":"Anlam yalnızca kişinin kendi boyu içinde gelmesini bildiren kuruluşta geçerlidir.","branch_image_ar":"الأبلة القبيلة","concept_gloss":"kendi boyuyla birlikte gelmek","definition":"Bir kişinin kendi boyunun veya soy topluluğunun içinde, onlarla birlikte gelmesini anlatan kuruluş.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin kendi boyu veya soy topluluğu içinde, onlarla birlikte gelmesi."}],"identity_rationale":"Tek kaynak ifadesi, bir kişinin kendi boyu veya soy topluluğu içinde gelmesini anlatan kuruluşu açıkça verir. Bu kanıt, yalın biçime genel bir boy anlamı yüklemek için yeterli değildir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kendi boyunun içinde, onlarla birlikte"}],"lexicalization_note":"Tanım tam olarak verilen kuruluşla sınırlıdır; yalın köke boy, soy veya topluluk anlamı genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kuruluş anlamı ile topluluk adını ayıran karşılaştırma en gerekli sınırı gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal topluluğun adı değildir, kişinin o topluluk içinde gelme durumudur; komşu dal ise topluluğun kendisini adlandırır.","focus_only":"Odak anlam, kişinin kendi boyuyla birlikte gelmesini bildiren tam bir kuruluşa bağlıdır.","gloss":"soy topluluğu veya boy","neighbor_only":"Komşu dal bir soy topluluğunun veya boyun kendisini adlandırır.","neighbor_ref":"root_000383/B010","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişiyi ait olduğu soy topluluğuyla ilişkilendirir."}],"source_phrase_ar":"جاء فلان في أبلته وإبالته أي في قبيلته (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu kuruluş yalnızca tek sözlükte, kişinin kendi boyu içinde gelmesi anlamıyla tanıklanmıştır."}],"source_summary":"Kanıt, kuruluşu kişinin kendi boyunun veya soy topluluğunun içinde gelmesi anlamıyla sınırlar.","sources":["TA"],"what_is_ar":"يدخل فيه المجيء في أبلته أو إبالته أي في قبيلته","what_is_not_ar":"ليس قطعان الإبل ولا جماعات الطير"},"support_links":[]},{"boundary":"Ölüm sonrası övgü ve ölüm sonrası üzüntü ayrı kuruluşlardır; yalnızca ağlama veya gömme anlamı yoktur.","branch_kind":"collocation","branch_ref":"root_000006/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبَابِيل","morph_features":"STEM|POS:ADJ|LEM:>abaAbiyl|ROOT:Abl|MP|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"105:3:4:1","qac_word_ref":"105:3:4","surface_ar":"أَبَابِيلَ"}],"gloss":"öleni övgüyle anmak veya ardından üzülmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ölen kişiyi ölümünden sonra övgüyle anmak."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ölen kişinin ardından üzüntü duymak."}}],"root_ar":"ء ب ل","root_id":"root_000006","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın ölüm sonrasındaki iki kuruluşunu, aralarındaki eylem farkını koruyarak birlikte karşılar.","boundary_detail":"Ölüm sonrası övgü ve ölüm sonrası üzüntü ayrı kuruluşlardır; yalnızca ağlama veya gömme anlamı yoktur.","branch_image_ar":"تأبيل الميت","concept_gloss":"öleni övgüyle anmak veya ardından üzülmek","contextual_glosses":[{"applicability":"Ölen kişinin iyi yönlerini ölümünden sonra dile getiren kuruluş için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ölen kişinin ardından duyulan üzüntü kullanımını kapsamaz.","preserves":"Ölen kişiye yönelik ölüm sonrası övgüyü korur."},"facet_ids":["F001"],"text":"ölümünden sonra övgüyle anmak","usage_role":"contextual"},{"applicability":"Ölen kişi için duyulan üzüntüyü bildiren ayrı kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öleni ölümünden sonra övgüyle anma eylemini kapsamaz.","preserves":"Ölümün ardından duyulan üzüntüyü korur."},"facet_ids":["F002"],"text":"ölenin ardından üzülmek","usage_role":"contextual"}],"definition":"Ölen kişiyi ölümünden sonra övgüyle anmak veya onun ardından üzülmek; iki eylem ayrı kuruluşlarla ifade edilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ölen kişiyi ölümünden sonra övgüyle anmak."},{"facet_id":"F002","role":"associated_use","statement":"Ölen kişinin ardından üzüntü duymak."}],"identity_rationale":"Kaynak ifadesi ölüm sonrasında iki ilişkili fakat özdeş olmayan eylemi kapsar: öleni övgüyle anmak ve onun ardından üzülmek. Tanım bunları tek bir yas eyleminde eritmeden birlikte tutar.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"öleni ölümünden sonra övgüyle anmak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"ölen kişinin ardından üzülmek"}],"lexicalization_note":"Tanım yalnızca ölen kişiyle kurulan iki söz öbeğine bağlıdır; yalın köke genel övgü veya genel üzüntü anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ölüm sonrası üzüntü ile genel ağlama alanını ayıran komşu en yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ölüm sonrası övgü ile üzüntüyü iki kuruluşta toplar; komşu dalın çekirdeği ağlama, gözyaşı ve ağlama sesidir.","focus_only":"Öleni ölümünden sonra övgüyle anma eylemi de dala dahildir.","gloss":"ağlama ve üzüntü","neighbor_only":"Komşu dal genel ağlama, gözyaşı dökme ve ağlama sesini de kapsar.","neighbor_ref":"root_000146/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da ölen kişi ardından duyulan üzüntü bağlamında kullanılabilir."}],"source_phrase_ar":"تأبل على الميت حزن عليه وأبلت الميت مثل أبنت (maqayis)؛ أبنت الميت تأبينا وأبلته تأبيلا إذا أثنيت عليه بعد وفاته (tahdhib)","source_summary":"Kaynak kanıtı, ölen kişiyi ölümünden sonra övgüyle anma ile onun ardından üzülmeyi, ayrı kuruluşlarda görülen iki ilişkili eylem olarak bir araya getirir.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه أبلت الميت تأبيلا أو تأبل على الميت إذا أثني عليه أو حزن عليه بعد موته","what_is_not_ar":"ليس الثقل ولا الإبل ولا الأبيل الراهب"},"support_links":[]},{"boundary":"Dal, gönderme ve serbest bırakmayı kapsar; yalnızca yavaşlık, süt veya sürü bildiren eşsesli kullanımları kapsamaz.","branch_kind":"bare","branch_ref":"root_000563/B001","candidate_links":[{"candidate_id":"cand_ab8f894712f8f7114996","lane":"micro"},{"candidate_id":"cand_eefb4ed317c3cc5e44e9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْسَلَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>arosala|ROOT:rsl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"105:3:1:2","qac_word_ref":"105:3:1","surface_ar":"أَرْسَلَ"}],"gloss":"bir şeyi gönderme veya serbest bırakma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel işlem, bir varlığı durduğu veya tutulduğu konumdan çıkarıp ileri yöneltmektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi görev veya haber için, rüzgar ve yağmur gibi güçler de etkilerini göstermek üzere gönderilebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tutmanın karşıtı olarak kullanım, eldeki canlıyı ya da denetlenen gücü salıvermeyi anlatır."}}],"root_ar":"ر س ل","root_id":"root_000563","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın görevle yollama ile tutmayı bırakıp salıverme biçimlerinin ikisini de birlikte temsil eder.","boundary_detail":"Dal, gönderme ve serbest bırakmayı kapsar; yalnızca yavaşlık, süt veya sürü bildiren eşsesli kullanımları kapsamaz.","branch_image_ar":"الإرسال والانبعاث","concept_gloss":"bir şeyi gönderme veya serbest bırakma","contextual_glosses":[{"applicability":"Bir kişi, elçi, rüzgar veya yağmur bir hedefe yöneltildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Elde tutulanı yalnızca serbest bırakma anlamını tek başına göstermez.","preserves":"Bir varlığı harekete geçirip bir yöne yollamayı korur."},"facet_ids":["F001","F002"],"text":"göndermek","usage_role":"general"},{"applicability":"Tutulan bir canlı veya denetlenen bir güç üzerindeki engel kaldırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Görevle veya haber taşımak üzere gönderme yönünü kapsamaz.","preserves":"Tutmayı bırakıp serbest hareket imkanı verme yönünü korur."},"facet_ids":["F001","F003"],"text":"salıvermek","usage_role":"contextual"}],"definition":"Bir insanı, canlıyı, doğal gücü ya da başka bir şeyi bulunduğu yerden harekete geçirip bir yöne göndermek; kimi bağlamlarda elde tutmayı bırakıp serbestçe gitmesine izin vermektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel işlem, bir varlığı durduğu veya tutulduğu konumdan çıkarıp ileri yöneltmektir."},{"facet_id":"F002","role":"specialization","statement":"Bir kişi görev veya haber için, rüzgar ve yağmur gibi güçler de etkilerini göstermek üzere gönderilebilir."},{"facet_id":"F003","role":"extension","statement":"Tutmanın karşıtı olarak kullanım, eldeki canlıyı ya da denetlenen gücü salıvermeyi anlatır."}],"identity_rationale":"Kaynak ifadesi, ortak çekirdeği bir varlığı harekete geçirip göndermek ya da elde tutmayı bırakıp salmak olarak kurar. İnsan, elçi, rüzgar, yağmur ve başka güçler bu işlemin farklı nesneleridir; bunlar ayrı birer çekirdek anlam değildir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"göndermek veya salıvermek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"gönderme, yöneltme veya serbest bırakma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"gönderilmiş rüzgarlar veya görevlendirilmiş melekler"}],"lexicalization_note":"Tanım yalın dalın gönderme ve salıverme çekirdeğiyle sınırlıdır; öteki dallardaki kalıba bağlı anlamlar buraya taşınmaz.","neighbor_coverage_note":"Sekiz dış aday ile on kardeş dalın tümü değerlendirildi; yalnızca gönderme, serbest bırakma ve gönderilen öğe sınırlarını doğrudan açıklayan üç karşıtlık seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın serbest bırakma ve doğal güçleri gönderme alanı daha geniştir; komşu dalın çekirdeği ise amaçlı görevlendirmedir.","focus_only":"Odak dal, doğal güçlerin yöneltilmesini ve tutulan bir şeyin salıverilmesini de kapsar.","gloss":"görevlendirip yollama","neighbor_only":"Komşu dal, bir kişi, hayvan veya topluluğun belirli bir ihtiyaç ya da hedef için görevlendirilerek yollanmasına bağlıdır.","neighbor_ref":"root_000129/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığın bir hedefe doğru hareket ettirilmesini anlatır."},{"boundary_match":"partial","distinction":"Odakta gönderme işlemi kurucudur; komşuda asıl vurgu hareketi engelleyen bağı kaldırmaktır.","focus_only":"Odak dal, haber veya görev için yollamayı da açıkça içerir.","gloss":"engelsiz bırakma","neighbor_only":"Komşu dal, engeli kaldırma, yol açma ve çözme gibi daha genel kolaylaştırma biçimlerine uzanır.","neighbor_ref":"root_000694/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de bir varlığın tutulmadan hareket etmesine imkan verebilir."},{"boundary_match":"field_only","distinction":"Eylem ile o eylemin taşıyıcısı veya içeriği birbirinin yerine kullanılamaz.","focus_only":"Odak dal gönderme veya salıverme eylemini adlandırır.","gloss":"gönderme ile gönderilen","neighbor_only":"Komşu dal gönderilen haber taşıyıcısını ya da taşınan haberin kendisini adlandırır.","neighbor_ref":"root_000563/B002","relation_type":"near_neighbor","shared_zone":"İki dal aynı gönderici, taşıma ve hedef senaryosunda buluşur."}],"source_phrase_ar":"أصل واحد يدل على الانبعاث والامتداد (maqayis)؛ أرسلت فلانا في رسالة والمرسلات الرياح ويقال الملائكة (sihah)؛ إرسال الله أنبياءه وإرسال الشياطين تخليتهم وإياهم (tahdhib)؛ الإرسال يقابل الإمساك (mufradat)","source_summary":"Kaynaklar, harekete geçirip yollama çekirdeğinde birleşir; görevle gönderme, doğal güçleri yöneltme ve tutulanı serbest bırakma bu çekirdeğin kapsam içi gerçekleşmeleridir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه إرسال الإنسان وغيره وبعث الرسل والرياح والمطر والتخلية والإطلاق في مقابل الإمساك","what_is_not_ar":"ليس هو مجرد التمهل ولا اللبن ولا القطيع"},"support_links":["sup_8bdbc1e3ecbdfcad74d9","sup_d5bf3c1aefa3e3bb9755"]},{"boundary":"Dal, haber taşıyıcısı ile taşınan iletiyi kapsar; gönderme eylemini, sürüyü veya kolay yürüyüşü kapsamaz.","branch_kind":"bare","branch_ref":"root_000563/B002","candidate_links":[{"candidate_id":"cand_9a0e4e7327fa2b496ecf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْسَلَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>arosala|ROOT:rsl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"105:3:1:2","qac_word_ref":"105:3:1","surface_ar":"أَرْسَلَ"}],"gloss":"haber taşıyıcısı veya taşınan haber","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, bir gönderenden bir alıcıya içerik taşıyan ileti bağını kurar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi okumasında, taşıyıcı gönderen adına haberleri izleyen ve aktaran görevlidir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İçerik okumasında sözcük, taşıyıcının götürdüğü sözün veya haberin kendisini belirtir."}}],"root_ar":"ر س ل","root_id":"root_000563","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kişi ile içerik arasında kurduğu iki yönlü adlandırmayı en kısa biçimde birlikte verir.","boundary_detail":"Dal, haber taşıyıcısı ile taşınan iletiyi kapsar; gönderme eylemini, sürüyü veya kolay yürüyüşü kapsamaz.","branch_image_ar":"الرسول والرسالة","concept_gloss":"haber taşıyıcısı veya taşınan haber","contextual_glosses":[{"applicability":"Söz veya haber taşıyan kişinin kastedildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Taşınan sözün veya haberin kendisini adlandırmaz.","preserves":"Gönderen adına haber taşıyan kişi yönünü korur."},"facet_ids":["F001","F002"],"text":"elçi","usage_role":"contextual"},{"applicability":"Taşınan sözün veya haberin kendisi kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İçeriği taşıyan kişiyi adlandırmaz.","preserves":"Göndericiden alıcıya taşınan içerik yönünü korur."},"facet_ids":["F001","F003"],"text":"ileti","usage_role":"contextual"}],"definition":"Bir gönderenin sözünü veya haberini başka birine götüren kişi ya da bu kişinin taşıdığı söz, haber ve iletidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, bir gönderenden bir alıcıya içerik taşıyan ileti bağını kurar."},{"facet_id":"F002","role":"specialization","statement":"Kişi okumasında, taşıyıcı gönderen adına haberleri izleyen ve aktaran görevlidir."},{"facet_id":"F003","role":"source_variant","statement":"İçerik okumasında sözcük, taşıyıcının götürdüğü sözün veya haberin kendisini belirtir."}],"identity_rationale":"Kaynak ifadesi aynı dal içinde iki açık gönderim öğesi verir: gönderenin sözünü taşıyan kişi ve taşınan söz ya da haber. Çerçeve bu düzenli kişi-içerik ayrımını doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"elçi veya haberci"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"taşınan ileti veya haber"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ileti veya taşınan haber"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"iletiler veya taşınan haberler"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"elçiler veya haberciler"}],"lexicalization_note":"Tanım yalın dalda haber taşıyan kişi ile taşınan içeriği birlikte gösterir; özel kalıplardaki eşsesli anlamlar eklenmez.","neighbor_coverage_note":"Sekiz dış aday ile on kardeş dalın tümü değerlendirildi; taşıyıcı, ileti ve iletme eylemi arasındaki sınırı en iyi gösteren üç aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odakta taşıyıcı veya içerik, komşuda ise başarıyla ulaştırma eylemi kurucudur.","focus_only":"Odak dal, haber taşıyan kişi ile taşınan içeriği adlandırır.","gloss":"ileti ile iletme","neighbor_only":"Komşu dal, iletinin alıcıya ulaştırılması ve bildirilmesi işlemini adlandırır.","neighbor_ref":"root_000151/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir haberin göndericiden alıcıya ulaşması senaryosundadır."},{"boundary_match":"partial","distinction":"Odak haber taşıma ve ileti içeriğine bağlıdır; komşu temsil ve güvence rollerini de kapsar.","focus_only":"Odak dal, taşınan sözün kendisini de adlandırabilir.","gloss":"haberci ve vekil","neighbor_only":"Komşu dalın kişi anlamı vekillik ve güvence üstlenme rollerine de uzanır.","neighbor_ref":"root_000240/B003","relation_type":"near_synonym","shared_zone":"Her iki dalda da başkası adına iş gören veya haber taşıyan bir kişi bulunur."},{"boundary_match":"field_only","distinction":"Birinde katılımcı veya içerik, ötekinde eylem anlamın merkezindedir.","focus_only":"Odak dal taşıyıcı kişiyi veya taşınan haberi adlandırır.","gloss":"gönderilen öğe ve gönderme","neighbor_only":"Komşu dal bunları yola çıkarma ya da başka bir şeyi salıverme eylemini adlandırır.","neighbor_ref":"root_000563/B001","relation_type":"near_neighbor","shared_zone":"İki dal gönderici, hedef ve hareket bağlantısını paylaşır."}],"source_phrase_ar":"الرسول معروف (maqayis)؛ الرسول بمعنى الرسالة والرسائل جمع الرسالة (ayn)؛ أرسلت فلانا في رسالة فهو مرسل ورسول والرسول أيضا الرسالة (sihah)؛ الرسول معناه الذي يتابع أخبار الذي بعثه (tahdhib)؛ الرسول يقال للقول المتحمل وتارة لمتحمل القول والرسالة (mufradat)","source_summary":"Kaynakların ortak anlatımı, gönderici ile alıcı arasındaki aktarımı hem taşıyıcı kişi hem de taşınan söz bakımından kurar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الرسول والرسل والرسالة والرسائل والقول المحمول وحامل القول","what_is_not_ar":"ليس هو القطيع ولا اللبن ولا مجرد السير السهل"},"support_links":["sup_30f767751a30a01b43e7"]},{"boundary":"Dal, harekette ve uzanışta yumuşak akıcılığı kapsar; gönderme, süt ve ardışık topluluk anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000563/B003","candidate_links":[{"candidate_id":"cand_d85c77f21ae6775397f9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْسَلَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>arosala|ROOT:rsl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"105:3:1:2","qac_word_ref":"105:3:1","surface_ar":"أَرْسَلَ"}],"gloss":"harekette veya uzanışta yumuşak akıcılık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ortak nitelik, direnç ve sertlik göstermeyen rahat bir akış veya uzanıştır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yürüyüşte bu nitelik, hayvanı zorlamayan kolay ve akıcı ilerleyiş olarak görünür."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bacaklar ve eklemler için yumuşaklık, saç için düz ve salık uzanma anlatılır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Deve topluluğuna uygulandığında hızlı ya da kolayca harekete geçen sürüler kastedilebilir."}}],"root_ar":"ر س ل","root_id":"root_000563","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yürüyüş, uzuv ve saç gerçekleşmelerini tek bir fiziksel nitelik altında kapsayan kavramsal karşılıktır.","boundary_detail":"Dal, harekette ve uzanışta yumuşak akıcılığı kapsar; gönderme, süt ve ardışık topluluk anlamlarını kapsamaz.","branch_image_ar":"السير السهل واللين","concept_gloss":"harekette veya uzanışta yumuşak akıcılık","contextual_glosses":[{"applicability":"Bir hayvanın veya topluluğun zorlanmadan ilerlemesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Saçın veya uzuvların yumuşak ve salık oluşunu kapsamaz.","preserves":"Dirençsiz ve kolay hareket niteliğini korur."},"facet_ids":["F001","F002","F004"],"text":"rahat ve akıcı yürüyüş","usage_role":"contextual"},{"applicability":"Saçın sertçe kıvrılmadan aşağı doğru uzanması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kolay yürüyüş ve yumuşak eklem yönlerini kapsamaz.","preserves":"Yumuşak ve serbest uzanma niteliğini korur."},"facet_ids":["F001","F003"],"text":"düz ve salık","usage_role":"contextual"}],"definition":"Hareketin zorlamasız, rahat ve akıcı olması ya da bir uzvun veya saçın sertçe kıvrılmadan yumuşakça uzanmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ortak nitelik, direnç ve sertlik göstermeyen rahat bir akış veya uzanıştır."},{"facet_id":"F002","role":"specialization","statement":"Yürüyüşte bu nitelik, hayvanı zorlamayan kolay ve akıcı ilerleyiş olarak görünür."},{"facet_id":"F003","role":"extension","statement":"Bacaklar ve eklemler için yumuşaklık, saç için düz ve salık uzanma anlatılır."},{"facet_id":"F004","role":"example","statement":"Deve topluluğuna uygulandığında hızlı ya da kolayca harekete geçen sürüler kastedilebilir."}],"identity_rationale":"Kaynak ifadesi, kolay ve zorlamasız ilerleyişi; yumuşak eklem ve bacakları; düz, salık saçı aynı akıcılık niteliği çevresinde toplar. Çerçeve, yürüyüşü tek başına bütün dal saymadan bu ortak niteliği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"rahat ve yumuşak ilerleyiş"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"rahat yürüyen, bacakları ve eklemleri yumuşak dişi deve"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"rahat yürüyen deve"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"düz ve salık saç"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"saçın düzleşip salık duruma gelmesi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"hızlı veya rahatça ilerleyen deve sürüleri"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"uzun ya da yumuşak ve rahat hareketli bacaklar"}],"lexicalization_note":"Tanım ortak akıcılık niteliğini verir; yürüyüş, hayvan bacakları, saç ve uzun bacak anlatımları kendi sözcük veya kalıp sınırlarında ayrı tutulur.","neighbor_coverage_note":"Sekiz dış aday ile on kardeş dalın tümü değerlendirildi; yürüyüş, genel yumuşaklık ve karşıt çaba düzeyini açıklayan üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yalnız yürüyüş eylemine bağlıdır; odak dal aynı niteliği beden yapısına ve saça da taşır.","focus_only":"Odak dal, kolay yürüyüşün yanında yumuşak uzuvları ve salık saçı da kapsar.","gloss":"yumuşak yürüyüş","neighbor_only":null,"neighbor_ref":"root_000664/B013","relation_type":"near_synonym","shared_zone":"İki dal da zorlamasız ve yumuşak ilerleyişi anlatır."},{"boundary_match":"partial","distinction":"Odak fiziksel hareket ve biçimle sınırlıyken komşu daha genel nitelik ve davranış alanını kapsar.","focus_only":"Odak dal, özellikle yürüyüşün akıcılığını ve saçın salık uzanmasını içerir.","gloss":"akıcılık ve yumuşaklık","neighbor_only":"Komşu dal, huyda yumuşaklık, kolaylaştırma ve insanlarla hoşgörülü davranma gibi soyut alanlara da uzanır.","neighbor_ref":"root_000753/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal sertliğin yokluğunu ve kolaylığı ifade eder."},{"boundary_match":"opposed","distinction":"Aynı çaba ekseninde odak düşük direnç ve rahatlığı, komşu yüksek yük ve zorlamayı kodlar.","focus_only":"Odak dal, bedeni zorlamayan rahat ilerleyişi belirtir.","gloss":"rahat ve yorucu yürüyüş","neighbor_only":"Komşu dal, sırtı yoran ve güçsüzü kapasitesinin üstünde zorlayan sert ilerleyişi belirtir.","neighbor_ref":"root_000347/B012","relation_type":"polarity_pair","shared_zone":"İki dal yürüyüşü harcanan güç ve bedensel yük bakımından değerlendirir."}],"source_phrase_ar":"فالرسل السير السهل وناقة رسلة لينة المفاصل وشعر رسل (maqayis)؛ ناقة رسلة القوائم سلسة لينة المفاصل (ayn)؛ شعر رسل وبعير رسل وناقة رسلة وإبل مراسيل (sihah)؛ الرسل الذي فيه لين واسترخاء وناقة مرسال رسلة القوائم (tahdhib)؛ ناقة رسلة سهلة السير وإبل مراسيل منبعثة انبعاثا سهلا (mufradat)","source_summary":"Kaynaklar kolay yürüyüş, yumuşak eklem ve bacaklar, salık saç ve rahatça ilerleyen deve topluluklarını dirençsiz akıcılık çevresinde birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السير السهل ولين القوائم والمفاصل والشعر المسترسل والإبل المراسيل والبعير السهل","what_is_not_ar":"ليس هو إرسال الرسالة ولا اللبن ولا القطيع"},"support_links":["sup_630a2304256207d9379f"]},{"boundary":"Dal, acele etmeden ölçülü davranma ve okumayı kapsar; ardışık topluluk veya taşınan ileti anlamını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000563/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْسَلَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>arosala|ROOT:rsl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"105:3:1:2","qac_word_ref":"105:3:1","surface_ar":"أَرْسَلَ"}],"gloss":"acele etmeden ölçülü ilerleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, aceleyi bırakıp ölçülü ve denetimli ilerlemektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İş ve konuşmada sakinlik, ağırbaşlılık ve karar vermeden önce sağlamlaştırma öne çıkar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Okumada metni acele etmeden açık, belirgin ve dikkatli söyleme kastedilir."}}],"root_ar":"ر س ل","root_id":"root_000563","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İş, konuşma ve okuma alanlarında ortak olan sakinlik ve denetim niteliğini verir.","boundary_detail":"Dal, acele etmeden ölçülü davranma ve okumayı kapsar; ardışık topluluk veya taşınan ileti anlamını kapsamaz.","branch_image_ar":"الرفق والتؤدة","concept_gloss":"acele etmeden ölçülü ilerleme","contextual_glosses":[{"applicability":"Bir kişiye yavaşlaması ve işi ölçülü yürütmesi söylendiğinde doğal buyruktur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Okumadaki açık söyleyiş ve işteki sağlamlaştırma ayrıntılarını belirtmez.","preserves":"Acele etmeme ve sakin davranma isteğini korur."},"facet_ids":["F001","F002"],"text":"Acele etme, sakin ol","usage_role":"contextual"},{"applicability":"Metnin acele edilmeden açık ve belirgin biçimde okunması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İş ve genel konuşmadaki ağırbaşlı tutumu kapsamaz.","preserves":"Okumada yavaşlık, açıklık ve denetimi korur."},"facet_ids":["F001","F003"],"text":"tane tane okumak","usage_role":"contextual"}],"definition":"Bir işi, konuşmayı veya okumayı aceleye getirmeden; sakinlik, ağırbaşlılık, dikkat ve denetimle yürütmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, aceleyi bırakıp ölçülü ve denetimli ilerlemektir."},{"facet_id":"F002","role":"specialization","statement":"İş ve konuşmada sakinlik, ağırbaşlılık ve karar vermeden önce sağlamlaştırma öne çıkar."},{"facet_id":"F003","role":"specialization","statement":"Okumada metni acele etmeden açık, belirgin ve dikkatli söyleme kastedilir."}],"identity_rationale":"Kaynak ifadesi iş, konuşma ve okumada aceleyi bırakıp sakin, ölçülü ve denetimli ilerlemeyi ortak çekirdek yapar. Çerçevedeki yavaşlık, ağırbaşlılık ve dikkat bu çekirdeğin birbirini tamamlayan yönleridir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"Acele etme; yavaş ve sakin ol"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"işte veya konuşmada sakin, ağırbaşlı ve temkinli davranma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"metni acele etmeden açık seçik okuma"}],"lexicalization_note":"Genel temkin niteliği korunur; yavaş ol buyruğu, iş ve konuşmadaki tutum ile okumadaki açık söyleyiş kendi kullanım sınırlarında ayrılır.","neighbor_coverage_note":"Sekiz dış aday ile on kardeş dalın tümü değerlendirildi; acele etmeme çekirdeğini gecikme, bekleme ve fiziksel yumuşaklıktan ayıran üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak etkinliğin nasıl yürütüldüğünü belirtir; komşu zaman tanıma ve durağanlık alanını daha geniş kapsar.","focus_only":"Odak dal, konuşma ve okumayı açık, denetimli biçimde sürdürme kullanımını özellikle içerir.","gloss":"ölçülülük ve acele etmeme","neighbor_only":"Komşu dal, bekletme, süre verme, durgunluk ve gevşeklik anlamlarına da uzanır.","neighbor_ref":"root_001452/B001","relation_type":"near_synonym","shared_zone":"İki dal da aceleyi bırakma, sakinlik ve ağırbaşlılık alanında örtüşür."},{"boundary_match":"partial","distinction":"Odakta ölçülü yapış biçimi, komşuda ise gecikme veya bekleme süresi daha belirgindir.","focus_only":"Odak dal, işte sağlamlaştırma ve okumada açık söyleyiş gibi kontrollü icra özelliklerini taşır.","gloss":"temkin ve gecikme","neighbor_only":"Komşu dal, gecikme, bekleme ve yavaşlatmayı sonuç olarak da adlandırır.","neighbor_ref":"root_000063/B001","relation_type":"near_synonym","shared_zone":"Her ikisi acele etmeme ve yavaş ilerleme anlamını paylaşır."},{"boundary_match":"partial","distinction":"Odak zihinsel ve sözlü denetime bağlıdır; komşu fiziksel hareket ve yumuşaklık alanına da yayılır.","focus_only":"Odak dal, konuşma ve okumadaki temkinli, açık icrayı içerir.","gloss":"yavaş ve nazik ilerleme","neighbor_only":"Komşu dal, yumuşak yürüyüşü ve sert esmeyen rüzgarı da kapsar.","neighbor_ref":"root_000610/B005","relation_type":"near_synonym","shared_zone":"İki dal da yavaşlama ve sertlikten kaçınma buyruğunda buluşur."}],"source_phrase_ar":"على رسلك أي على هينتك (maqayis)؛ تكلم على رسلك والترسل في الأمر والمنطق كالتمهل والتوقر والتثبت (ayn)؛ على رسلك أي اتئد فيه وترسل في قراءته (sihah)؛ الترسل من الرسل في الأمور والمنطق كالتمهل والتوقر والتثبت والترسيل التحقيق بلا عجلة (tahdhib)؛ على رسلك إذا أمرته بالرفق (mufradat)","source_summary":"Kaynaklar, acele etmeme buyruğunu ve iş, konuşma, okuma alanlarındaki sakin, dikkatli ilerleyişi ortak bir ölçülülük çekirdeğinde birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه قولهم على رسلك والترسل في الأمر والمنطق والقراءة والتمهل والتوقر والتثبت","what_is_not_ar":"ليس هو القطيع المتتابع ولا الرسالة المحمولة"},"support_links":[]},{"boundary":"Dal, peş peşe gelen ayrı toplulukları ve sürüleri kapsar; haber taşıyıcısını veya sütün kendisini kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000563/B005","candidate_links":[{"candidate_id":"cand_b75059b67363bfe60022","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْسَلَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>arosala|ROOT:rsl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"105:3:1:2","qac_word_ref":"105:3:1","surface_ar":"أَرْسَلَ"}],"gloss":"peş peşe gelen topluluklar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kurucu yapı, birbirini izleyen ayrı toplulukların oluşturduğu ardışıklıktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanlar söz konusu olduğunda her küme bir sürü, otlağa veya suya salınan topluluk olabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsan ve at topluluklarında da grup grup, biri diğerinin ardından gelme anlatılır."}}],"root_ar":"ر س ل","root_id":"root_000563","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Topluluk birimlerini ve bu birimlerin ardışık gelişini birlikte taşıyan en doğal kısa karşılıktır.","boundary_detail":"Dal, peş peşe gelen ayrı toplulukları ve sürüleri kapsar; haber taşıyıcısını veya sütün kendisini kapsamaz.","branch_image_ar":"التتابع والقطع","concept_gloss":"peş peşe gelen topluluklar","contextual_glosses":[{"applicability":"İnsanların, atların veya başka varlıkların ayrı kümeler halinde art arda gelişi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Her kümenin kalıcı bir sürü adı olabilmesini açıkça göstermez.","preserves":"Ayrı kümeler halinde birbirini izlemeyi korur."},"facet_ids":["F001","F003"],"text":"grup grup, peş peşe","usage_role":"general"},{"applicability":"Deve veya koyunlardan oluşan tek bir topluluk adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir sürünün ardından bir başkasının gelmesi düzenini tek başına göstermez.","preserves":"Hayvan topluluğu birimini korur."},"facet_ids":["F002"],"text":"sürü","usage_role":"contextual"}],"definition":"İnsanların, develerin, koyunların veya başka varlıkların ayrı topluluklar halinde, bir küme ötekinin ardından gelecek biçimde ilerlemesi ya da bu kümelerin her biridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kurucu yapı, birbirini izleyen ayrı toplulukların oluşturduğu ardışıklıktır."},{"facet_id":"F002","role":"specialization","statement":"Hayvanlar söz konusu olduğunda her küme bir sürü, otlağa veya suya salınan topluluk olabilir."},{"facet_id":"F003","role":"extension","statement":"İnsan ve at topluluklarında da grup grup, biri diğerinin ardından gelme anlatılır."}],"identity_rationale":"Kaynak ifadesi, insan veya hayvanların tek bir kütle halinde değil, biri ötekinin ardından gelen ayrı kümeler halinde gelişini ve bu kümelerin her birini anlatır. Çerçeve, topluluk ile ardışıklık bileşenlerini birlikte korur.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"deve, koyun veya başka varlıklardan oluşan sürü"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"gruplar halinde, birbirinin ardından"}],"lexicalization_note":"Tanım ardışık topluluk çekirdeğini korur; tek sürü adı ile grup grup gelme anlatımı kendi sözcük biçimlerinde ayrılır.","neighbor_coverage_note":"Sekiz dış aday ile on kardeş dalın tümü değerlendirildi; ardışık sürü, dağınık geliş ve nöbetleşme sınırlarını açıklayan üç aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak daha geniş bir katılımcı alanında grup grup gelişi kurar; komşu deve dizisinin sürekliliğine bağlıdır.","focus_only":"Odak dal, insanları, atları ve küçükbaş hayvanları da kapsar ve ayrı kümeleri adlandırabilir.","gloss":"ardışık sürüler","neighbor_only":"Komşu dal, özellikle develerin aynı iz üzerinde birbirini izlemesine bağlıdır.","neighbor_ref":"root_000427/B008","relation_type":"near_synonym","shared_zone":"İki dal da develerin birbirinin ardından gelmesini anlatır."},{"boundary_match":"partial","distinction":"Odakta grup birimleri ve peş peşelik birlikte bulunur; komşuda dağılma seçeneği bu sınırı aşar.","focus_only":"Odak dalda ayrı topluluklar ve bunların ardışıklığı zorunludur.","gloss":"dağınık veya ardışık geliş","neighbor_only":"Komşu dal, topluluğun dağınık biçimde gitmesini ardışıklık olmadan da anlatabilir.","neighbor_ref":"root_001012/B011","relation_type":"near_synonym","shared_zone":"İki dal, insanların ya da develerin birbirinin ardından gelmesini kapsayabilir."},{"boundary_match":"partial","distinction":"Odakta toplulukların seri gelişi, komşuda ise yer değiştiren veya nöbetleşen öğelerin sırası kurucudur.","focus_only":"Odak dal, aynı türden toplulukların grup grup ilerlemesini anlatır.","gloss":"ardışıklık ve dönüşüm","neighbor_only":"Komşu dal, gece ile gündüz gibi iki öğenin dönüşümlü yer değiştirmesini de kapsar.","neighbor_ref":"root_000433/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir öğe veya küme diğerinin ardından gelir."}],"source_phrase_ar":"الرسل ما أرسل من الغنم إلى الرعي وجاء القوم أرسالا يتبع بعضهم بعضا (maqayis)؛ الرسل القطيع من كل شيء وجمعه أرسال (ayn)؛ الرسل القطيع من الإبل والغنم وجاءت الخيل أرسالا قطيعا قطيعا (sihah)؛ جاءت الإبل أرسالا رسل بعد رسل والرسل قطيع من الإبل (tahdhib)؛ جاءوا أرسالا أي متتابعين (mufradat)","source_summary":"Kaynaklar, deve, koyun, at veya insan kümelerinin ayrı gruplar halinde birbirini izlemesini ve her bir hayvan kümesinin sürü olarak adlandırılmasını birlikte verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه مجيء الإبل والخيل والناس أرسالا والقطيع بعد القطيع وما أرسل إلى الرعي أو الماء","what_is_not_ar":"ليس هو رسول الرسالة ولا اللبن نفسه إلا من جهة الدر المتتابع"},"support_links":["sup_3bb8eb72d603fbb2a398"]},{"boundary":"Dal sütü, özellikle bol ve sürekli gelen sütü kapsar; sürü, ileti veya genel bolluk anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000563/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْسَلَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>arosala|ROOT:rsl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"105:3:1:2","qac_word_ref":"105:3:1","surface_ar":"أَرْسَلَ"}],"gloss":"bol ve sürekli gelen süt","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dalın somut çekirdeği hayvandan elde edilen süttür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sütün bol olması ve memeden kesintisiz ya da art arda gelmesi özellikle vurgulanabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Topluluğa uygulanan kullanım, hayvanlarının süt vermesi sayesinde süt sahibi duruma gelmelerini anlatır."}}],"root_ar":"ر س ل","root_id":"root_000563","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın süt maddesini ve özellikle belirtilen ardışık akış niteliğini birlikte temsil eder.","boundary_detail":"Dal sütü, özellikle bol ve sürekli gelen sütü kapsar; sürü, ileti veya genel bolluk anlamlarını kapsamaz.","branch_image_ar":"اللبن والدر المتتابع","concept_gloss":"bol ve sürekli gelen süt","contextual_glosses":[{"applicability":"Maddenin kendisi kastedildiğinde en yalın doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bolluk, sürekli akış ve topluluğun süt sahibi oluşu ayrıntılarını göstermez.","preserves":"Dalın somut süt çekirdeğini korur."},"facet_ids":["F001"],"text":"süt","usage_role":"general"},{"applicability":"Bir topluluğun hayvanları süt vermeye başladığında kullanılan yapıyı açıklar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sütün bol ve sürekli akması niteliğini zorunlu kılmaz.","preserves":"Topluluğun süt sahibi duruma gelmesi uzantısını korur."},"facet_ids":["F003"],"text":"hayvanlarından süt elde etmek","usage_role":"explanatory"}],"definition":"Hayvandan elde edilen süt, özellikle memeden bol ve art arda gelen süt; ayrıca bir topluluğun hayvanlarından süt elde eder duruma gelmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dalın somut çekirdeği hayvandan elde edilen süttür."},{"facet_id":"F002","role":"specialization","statement":"Sütün bol olması ve memeden kesintisiz ya da art arda gelmesi özellikle vurgulanabilir."},{"facet_id":"F003","role":"extension","statement":"Topluluğa uygulanan kullanım, hayvanlarının süt vermesi sayesinde süt sahibi duruma gelmelerini anlatır."}],"identity_rationale":"Kaynak ifadesi sözcüğü süt için kullanır, bol ve art arda meme akışını bu adlandırmanın gerekçesi olarak verir ve bir topluluğun hayvanlarından süt elde etmesini aynı dala bağlar. Çerçeve madde, akış ve elde edilebilirlik ayrımlarını korur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"süt; özellikle bol ve sürekli gelen süt"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"hayvanlarından süt elde eder duruma gelmek"}],"lexicalization_note":"Tanım süt çekirdeğini korur; sütün bolluğu ile bir topluluğun hayvanlarından süt elde eder hale gelmesi ayrı sözcük kullanımları olarak tutulur.","neighbor_coverage_note":"Sekiz dış aday ile on kardeş dalın tümü değerlendirildi; genel süt, kaynaktan çıkış ve verimin kesilmesiyle kurulan üç sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bolluk ve süreklilik niteliğine bağlanır; komşu süt maddesinin daha genel kullanım alanıdır.","focus_only":"Odak dal, bol ve art arda meme akışını ve topluluğun süt sahibi oluşunu özellikle içerir.","gloss":"süt ve sürekli süt akışı","neighbor_only":"Komşu dal, içilen sütü, onunla beslenmeyi ve sütle ilgili daha genel durumları kapsar.","neighbor_ref":"root_001342/B001","relation_type":"near_synonym","shared_zone":"İki dalın somut merkezinde hayvansal süt bulunur."},{"boundary_match":"partial","distinction":"Odak çıkan maddenin kendisine ve süt sahipliğine, komşu ise farklı maddelerde görülen çıkış olayına odaklanır.","focus_only":"Odak dal sütü bir madde ve elde edilen ürün olarak adlandırır.","gloss":"süt ve kaynaktan bol çıkış","neighbor_only":"Komşu dal yağmur, gözyaşı, kan ve gelir gibi birçok şeyin kaynağından bolca çıkmasına uzanır.","neighbor_ref":"root_000469/B001","relation_type":"near_neighbor","shared_zone":"İki dal memeden sütün bolca gelmesi durumunda kesişir."},{"boundary_match":"opposed","distinction":"Odak yüksek ve sürekli verimi, komşu düşük ya da kesintiye uğramış verimi kodlar.","focus_only":"Odak dal sütün bolluğunu ve art arda gelişini belirtir.","gloss":"bol akış ve kesilen verim","neighbor_only":"Komşu dal süt veriminin veya yağmurun azalmasını ve kesilmesini belirtir.","neighbor_ref":"root_000305/B005","relation_type":"polarity_pair","shared_zone":"İki dal süt verimini miktar ve süreklilik bakımından değerlendirir."}],"source_phrase_ar":"الرِّسل اللبن لأنه يترسل من الضرع (maqayis)؛ والرسل اللبن (ayn)؛ والرسل أيضا اللبن وقد أرسل القوم أي صار لهم اللبن (sihah)؛ كثر الرسل العام أي كثر اللبن (tahdhib)؛ الرسل اللبن الكثير المتتابع الدر (mufradat)","source_summary":"Kaynaklar sözcüğü süt için verir; bolluk ve memeden sürekli geliş niteliğini belirtir, ayrıca hayvanlarından süt elde etmeye başlayan topluluğu aynı anlam alanına bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الرِّسل بمعنى اللبن وكثرة اللبن والدر المتتابع وقولهم أرسل القوم إذا صار لهم لبن","what_is_not_ar":"ليس هو القطيع ولا الرسالة ولا الرسل بمعنى الرخاء"},"support_links":[]},{"boundary":"Dal, birine veya bir şeye ısınıp yanında rahatça açılmayı kapsar; yavaş okuma veya genel gönderme anlamını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000563/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْسَلَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>arosala|ROOT:rsl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"105:3:1:2","qac_word_ref":"105:3:1","surface_ar":"أَرْسَلَ"}],"gloss":"ısınıp güvenerek açılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin iç yönelişi, yabancılıktan yakınlık ve güvene geçiş oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu güvenin görünür sonucu, karşısındakinin yanında rahat ve açık davranmaktır."}}],"root_ar":"ر س ل","root_id":"root_000563","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İç yöneliş, güven ve rahat dışa açılma aşamalarını birlikte taşıyan kısa karşılıktır.","boundary_detail":"Dal, birine veya bir şeye ısınıp yanında rahatça açılmayı kapsar; yavaş okuma veya genel gönderme anlamını kapsamaz.","branch_image_ar":"الاستئناس والانبساط","concept_gloss":"ısınıp güvenerek açılma","contextual_glosses":[{"applicability":"İlk yabancılık duygusunun kalkıp yakınlık doğduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yerleşmiş güven ve çekinmeden açılma sonucunu tam belirtmez.","preserves":"İçten yönelme ve yakınlık kazanma yönünü korur."},"facet_ids":["F001"],"text":"birine ısınmak","usage_role":"contextual"},{"applicability":"Kişinin karşısındakinin yanında çekinmeden konuşup davranması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir şeye yönelik ilk iç çekimi ayrıca göstermez.","preserves":"Güven ve rahat dışa açılma sonucunu korur."},"facet_ids":["F001","F002"],"text":"güvenip rahatça açılmak","usage_role":"contextual"}],"definition":"Bir kimseye veya şeye içten yönelip yabancılık duymamak; ona güvenerek yanında rahatlamak ve kendini çekinmeden açmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin iç yönelişi, yabancılıktan yakınlık ve güvene geçiş oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Bu güvenin görünür sonucu, karşısındakinin yanında rahat ve açık davranmaktır."}],"identity_rationale":"Kaynak ifadesi, kişinin iç dünyasının birine veya bir şeye yönelmesini; yabancılık duygusunun kalkıp güven, rahatlık ve açıklık doğmasını anlatır. Çerçeve bu iç yöneliş ile dışa açılma sonucunu doğru bağlar.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"birine veya bir şeye ısınıp güvenmek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"sana güvenip yanında rahat davranan kimse"}],"lexicalization_note":"Anlam, birine ya da bir şeye yönelmeyi belirten yapılarla sınırlıdır; yalın köke genel bir yakınlık anlamı yüklenmez.","neighbor_coverage_note":"Sekiz dış aday ile on kardeş dalın tümü değerlendirildi; güven, yakınlık ve dışa dönük davranış arasındaki ayrımı açıklayan üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak yakınlaşmanın doğurduğu açıklığı, komşu ise güven ve dayanmayı daha güçlü öne çıkarır.","focus_only":"Odak dal, içten yönelme ve karşısındakine çekinmeden açılma aşamalarını içerir.","gloss":"güvenerek yakınlaşma","neighbor_only":"Komşu dal, güvenip dayanma ve karar kılma yönünü daha belirgin taşır.","neighbor_ref":"root_001568/B005","relation_type":"near_synonym","shared_zone":"İki dal birine veya bir şeye güvenip yanında iç rahatlığı bulmayı anlatır."},{"boundary_match":"partial","distinction":"Odak yönelme ve açılma sürecidir; komşu yakınlığın kişisini, nesnesini ve sonucunu daha geniş adlandırır.","focus_only":"Odak dal, belirli bir kişiye veya şeye yönelip kendini açma yapısına bağlıdır.","gloss":"yabancılığı gideren yakınlık","neighbor_only":"Komşu dal sohbetten duyulan sevinci, yakınlık sağlayan varlığı ve insana alışkın hayvanı da kapsar.","neighbor_ref":"root_000059/B003","relation_type":"near_synonym","shared_zone":"Her ikisi yabancılık ve yalnızlık duygusunun yakınlıkla kalkmasını anlatır."},{"boundary_match":"field_only","distinction":"Odakta içsel güven ilişkisi kurucudur; komşuda görünür toplumsal davranış kurucudur.","focus_only":"Odak dal, güven ve yakınlık duygusundan doğan rahatlığı içerir.","gloss":"iç güven ve dışa dönüklük","neighbor_only":"Komşu dal, konuşkanlık, güler yüz ve toplumsal çekingenliği bırakma gibi dış davranışları içerir.","neighbor_ref":"root_000116/B005","relation_type":"near_neighbor","shared_zone":"İki dal da kişinin başkalarının yanında rahat ve açık görünmesine yol açabilir."}],"source_phrase_ar":"استرسلت إلى الشيء إذا انبعثت نفسك إليه وأنست (maqayis)؛ الاسترسال إلى شيء كالاستئناس والطمأنينة (ayn)؛ استرسل إليه أي انبسط واستأنس (sihah)؛ الاسترسال إلى الإنسان كالاستئناس والطمأنينة (tahdhib)","source_summary":"Kaynaklar, kişinin birine veya bir şeye içten yönelmesini; onun yanında güven, yakınlık, rahatlık ve açıklık kazanmasını ortak biçimde anlatır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الاسترسال إلى الإنسان أو الشيء بمعنى الأنس والطمأنينة والانبساط","what_is_not_ar":"ليس هو الترسل في القراءة ولا إرسال الرسالة"},"support_links":[]},{"boundary":"Dal, karşılıklı iletişim ve ortak uğraşta eşlik edip izlemeyi kapsar; tek yönlü gönderiyi veya yalnızca taşınan iletiyi kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000563/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْسَلَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>arosala|ROOT:rsl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"105:3:1:2","qac_word_ref":"105:3:1","surface_ar":"أَرْسَلَ"}],"gloss":"karşılıklı iletişim ve eşlik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, iki taraf arasında karşılıklı gönderim veya birinin ötekini izlemesiyle kurulan eşgüdümdür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atışma veya başka bir uğraşta kişinin yanında duran ve onunla birlikte ilerleyen eşlikçi kastedilebilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Şarkı veya işte bir öncekinin sesini ya da eylemini izleyerek sürdüren kişi kastedilebilir."}}],"root_ar":"ر س ل","root_id":"root_000563","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Haber alışverişi ile ortak uğraşta yan yana veya art arda ilerleme biçimlerini birlikte temsil eder.","boundary_detail":"Dal, karşılıklı iletişim ve ortak uğraşta eşlik edip izlemeyi kapsar; tek yönlü gönderiyi veya yalnızca taşınan iletiyi kapsamaz.","branch_image_ar":"المراسلة والمسايرة","concept_gloss":"karşılıklı iletişim ve eşlik","contextual_glosses":[{"applicability":"İki taraf birbirine ileti gönderdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Atışma, şarkı veya işteki fiziksel ve sıralı eşliği kapsamaz.","preserves":"Karşılıklı gönderim ve iletişim yönünü korur."},"facet_ids":["F001"],"text":"karşılıklı haberleşmek","usage_role":"contextual"},{"applicability":"Bir uğraşta, şarkıda veya işte başkasını izleyen kişi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karşılıklı ileti gönderme anlamını göstermez.","preserves":"Ortak uğraşta ayak uydurma ve izleme yönünü korur."},"facet_ids":["F001","F002","F003"],"text":"eşlik edip ardından gitmek","usage_role":"explanatory"}],"definition":"İki kişinin karşılıklı haberleşmesi veya ortak bir uğraşta birbirine ayak uydurması; özellikle atışma gibi bir işte yanında durması ya da şarkı ve çalışmada öncekinin ardından gitmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, iki taraf arasında karşılıklı gönderim veya birinin ötekini izlemesiyle kurulan eşgüdümdür."},{"facet_id":"F002","role":"specialization","statement":"Atışma veya başka bir uğraşta kişinin yanında duran ve onunla birlikte ilerleyen eşlikçi kastedilebilir."},{"facet_id":"F003","role":"specialization","statement":"Şarkı veya işte bir öncekinin sesini ya da eylemini izleyerek sürdüren kişi kastedilebilir."}],"identity_rationale":"Kaynak ifadesi karşılıklı haberleşmeyi, atışma gibi bir uğraşta kişinin yanında duran eşliği ve şarkı ya da işte öncekinin ardından gitmeyi aynı karşılıklılık ve izleme alanında toplar. Çerçeve bu özel katılımcı rollerini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"karşılıklı haberleşmek veya birbirine ayak uydurmak"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"atışmada veya başka bir uğraşta eşlik eden kişi"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"şarkıda veya işte bir öncekinin ardından giden eşlikçi"}],"lexicalization_note":"Tanım karşılıklı haberleşme, yarışma eşliği ve şarkı ya da işte izleme biçimlerini kendi yapılara bağlı tutar; yalın köke genel arkadaşlık anlamı verilmez.","neighbor_coverage_note":"Sekiz dış aday ile on kardeş dalın tümü değerlendirildi; genel ayak uydurma, sesle izleme ve sürekli yandaşlıkla kurulan üç sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak karşılıklı gönderim ve belirli eşlikçi rollerine bağlıdır; komşu genel birlikte ilerleme eylemidir.","focus_only":"Odak dal, karşılıklı ileti gönderme ile atışma, şarkı ve işteki özel eşlikçi rollerini içerir.","gloss":"ayak uydurma ve karşılıklı eşlik","neighbor_only":"Komşu dal, bir şeyle birlikte koşmayı ve konuşmada onun çizgisini izlemeyi daha genel anlatır.","neighbor_ref":"root_000240/B007","relation_type":"near_synonym","shared_zone":"İki dal bir başkasının hareketine veya sözüne uyum sağlayarak onunla ilerlemeyi anlatır."},{"boundary_match":"partial","distinction":"Komşu, odak dalın yalnızca şarkıya özgü bir gerçekleşmesidir ve bütün dalın yerine geçmez.","focus_only":"Odak dal karşılıklı haberleşmeyi ve çalışma ya da yarışma eşliğini de kapsar.","gloss":"ardından sesle eşlik","neighbor_only":"Komşu dal yalnızca şarkıcının sesini ardından gelen başka bir sesle sürdürme olayına bağlıdır.","neighbor_ref":"root_000186/B007","relation_type":"near_neighbor","shared_zone":"İki dal şarkıda bir sesin başka bir ses tarafından izlenmesi durumunda kesişir."},{"boundary_match":"field_only","distinction":"Odak eşgüdümlü değiş tokuş ya da izlemeyi, komşu ise süreklilik gösteren yakın destek ve yandaşlığı kurar.","focus_only":"Odak dalda karşılıklı gönderim veya birinin eylemini sırayla izleme bulunur.","gloss":"eşgüdüm ve yandaşlık","neighbor_only":"Komşu dalda kişinin yanında durma, onu destekleme ve sürekli beraber olma bulunur.","neighbor_ref":"root_001346/B002","relation_type":"same_field","shared_zone":"İki dal ortak bir işte kişilerin birbirinin yanında bulunması alanını paylaşır."}],"source_phrase_ar":"رسيل الرجل الذي يقف معه في نضال أو غيره (maqayis)؛ راسله مراسلة فهو مراسل ورسيل الرجل الذي يراسله في نضال أو غيره (sihah)؛ العرب تسمي المراسل في الغناء والعمل المتالي (tahdhib)","source_summary":"Kaynaklar karşılıklı haberleşme, ortak uğraşta yan yana durma ve şarkı ya da işte bir öncekinin ardından gitme biçimlerini eşgüdümlü eşlik alanında verir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه راسله مراسلة ورسيل الرجل في النضال أو غيره والمراسل في الغناء والعمل","what_is_not_ar":"ليس هو الرسول النبوي ولا الرسالة المحمولة وحدها"},"support_links":[]},{"boundary":"Dal yalnız bu kadın durumuna ve taliplerin ileti kurmasına bağlıdır; genel haberleşmeyi veya bütün dul kadınları koşulsuz biçimde kapsamaz.","branch_kind":"collocation","branch_ref":"root_000563/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْسَلَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>arosala|ROOT:rsl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"105:3:1:2","qac_word_ref":"105:3:1","surface_ar":"أَرْسَلَ"}],"gloss":"taliplerin haber gönderdiği dul veya ayrılmak üzere olan kadın","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın, mevcut veya yaklaşan eş kaybı nedeniyle yeni taliplerin ileti kurabildiği kişi olarak nitelenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koşul, eşin ölmesi veya boşanmanın gerçekleşmesi olabileceği gibi boşanma niyetinin kadınca sezilmesi de olabilir."}}],"root_ar":"ر س ل","root_id":"root_000563","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gerçekleşmiş eş kaybı ile beklenen boşanmayı ve taliplerin ileti kurmasını birlikte taşır.","boundary_detail":"Dal yalnız bu kadın durumuna ve taliplerin ileti kurmasına bağlıdır; genel haberleşmeyi veya bütün dul kadınları koşulsuz biçimde kapsamaz.","branch_image_ar":"المرأة المراسل","concept_gloss":"taliplerin haber gönderdiği dul veya ayrılmak üzere olan kadın","contextual_glosses":[{"applicability":"Terimin özel evlilik ve ileti koşulunu okura açıklamak gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Önceki eşin ölmesi, boşanma veya beklenen boşanma koşullarını tek başına belirtmez.","preserves":"Taliplerin kadınla yeni evlilik amacıyla ileti kurmasını korur."},"facet_ids":["F001"],"text":"kendisine evlenme önerileri iletilen kadın","usage_role":"explanatory"}],"definition":"Eşi ölmüş, boşanmış ya da eşinin kendisini boşayacağını sezmiş olduğu için taliplerin kendisine evlenme önerileri ilettiği kadındır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın, mevcut veya yaklaşan eş kaybı nedeniyle yeni taliplerin ileti kurabildiği kişi olarak nitelenir."},{"facet_id":"F002","role":"source_variant","statement":"Koşul, eşin ölmesi veya boşanmanın gerçekleşmesi olabileceği gibi boşanma niyetinin kadınca sezilmesi de olabilir."}],"identity_rationale":"Kaynak ifadesi, eşi ölmüş veya kendisinden ayrılmış kadını ve ayrılığın yaklaştığını sezen kadını, taliplerin kendisine evlenme önerisi iletmesi bakımından birleştirir. Çerçeve hem gerçekleşmiş hem beklenen ayrılık koşulunu açıkça korur.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"eşi ölmüş, boşanmış veya ayrılmak üzere olduğu için taliplerin haber gönderdiği kadın"}],"lexicalization_note":"Tanım yalnız verilen kadın nitelemesine bağlıdır; genel haberleşme veya genel evlilik durumu anlamı olarak yalınlaştırılmaz.","neighbor_coverage_note":"Sekiz dış aday ile on kardeş dalın tümü değerlendirildi; evlenme önerisi, önceki evlilik ve askıda kalan evlilik durumlarıyla kurulan üç sınır seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odakta önerinin alıcısı ve onun durumu, komşuda ise öneri eylemi ve öneriyi yapan kişi kurucudur.","focus_only":"Odak dal, önerinin yöneldiği kadını önceki evlilik durumu bakımından niteler.","gloss":"evlenme önerisi alan kadın","neighbor_only":"Komşu dal, evlenme amacıyla eş isteme ve öneride bulunma eylemini ve bunu yapan kişiyi adlandırır.","neighbor_ref":"root_000421/B002","relation_type":"near_neighbor","shared_zone":"İki dal yeni bir evlilik için ileti kurulması senaryosunu paylaşır."},{"boundary_match":"partial","distinction":"Odak yeni taliplerle ileti ve olası ayrılık koşuluna bağlıdır; komşu cinsiyet ve evlilik deneyimi bakımından daha geniştir.","focus_only":"Odak dal yalnız kadına uygulanır, beklenen boşanmayı da kapsar ve taliplerin ileti kurmasını gerektirir.","gloss":"önceki evlilikten ayrılan kadın","neighbor_only":"Komşu dal erkek veya kadına uygulanabilir ve evlilik yaşamış olmayı ya da bekaretin kalkmasını daha geniş biçimde belirtir.","neighbor_ref":"root_000209/B005","relation_type":"near_synonym","shared_zone":"İki dal önceki eşinden ayrılmış bir kadını adlandırabilir."},{"boundary_match":"field_only","distinction":"Odak yeni evliliğe yönelik iletiye açılan ayrılık eşiğini, komşu ise boşanma gerçekleşmeden süren edilgen sıkışmışlığı anlatır.","focus_only":"Odak dalda evlilik bağı bitmiş veya bitmek üzeredir ve yeni talipler ileti kurar.","gloss":"ayrılık eşiği ve evlilikte askıda kalma","neighbor_only":"Komşu dalda eş ne geçim sağlar ne de boşar; kadın evli ile bekar arasında askıda tutulur.","neighbor_ref":"root_001039/B008","relation_type":"same_field","shared_zone":"İki dal evlilik bağının belirsizleştiği kadın durumlarını ele alır."}],"source_phrase_ar":"المرأة المراسل التي مات بعلها فالخطاب يراسلونها (maqayis)؛ امرأة مراسل كان لها زوج والخطاب يراسلونها الخطبة (ayn)؛ امرأة مراسل يموت زوجها أو أحست منه أنه يريد تطليقها (sihah)؛ امرأة مراسل وهي التي مات عنها زوجها أو طلقها (tahdhib)","source_summary":"Kaynaklar, önceki evlilik bağının sona ermesi veya sona ereceğinin sezilmesi üzerine taliplerin kendisine evlenme önerileri gönderdiği kadını anlatır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه المرأة المراسل التي مات زوجها أو طلقها أو أحست بطلاقه فيراسلها الخطاب","what_is_not_ar":"ليس هو المراسلة العامة ولا الرسول والرسالة"},"support_links":[]},{"boundary":"Dal yalnız verilen yapılarda rahatlık ve gönül hoşluğuyla vermeyi kapsar; genel süt, sürü veya bütün refah adlandırmalarına genişletilemez.","branch_kind":"collocation","branch_ref":"root_000563/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْسَلَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>arosala|ROOT:rsl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"105:3:1:2","qac_word_ref":"105:3:1","surface_ar":"أَرْسَلَ"}],"gloss":"rahatlık ve gönül hoşluğuyla verme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel karşıtlık, sıkıntılı ve sert durum karşısındaki rahatlık ve ferahlıktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Verme bağlamında rahatlık, isteksizlik veya zorlama olmadan gönülden vermek olarak gerçekleşir."}}],"root_ar":"ر س ل","root_id":"root_000563","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Verilen yapıdaki durum karşıtlığını ve verme bağlamındaki özel uzantıyı birlikte gösterir.","boundary_detail":"Dal yalnız verilen yapılarda rahatlık ve gönül hoşluğuyla vermeyi kapsar; genel süt, sürü veya bütün refah adlandırmalarına genişletilemez.","branch_image_ar":"الرخاء وطيب الإعطاء","concept_gloss":"rahatlık ve gönül hoşluğuyla verme","contextual_glosses":[{"applicability":"Sıkıntılı dönem ile rahat dönem karşı karşıya getirildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gönül hoşluğuyla verme uzantısını kapsamaz.","preserves":"Sıkıntının karşıtı olan rahat durum yönünü korur."},"facet_ids":["F001"],"text":"rahatlık ve bolluk zamanı","usage_role":"contextual"},{"applicability":"Bir şeyin zorlanmadan ve içtenlikle verildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıkıntının karşıtı genel rahatlık durumunu kapsamaz.","preserves":"Verişte isteklilik ve iç rahatlığını korur."},"facet_ids":["F002"],"text":"gönül hoşluğuyla vermek","usage_role":"contextual"}],"definition":"Belirli söz yapılarında sıkıntı ve sertliğin karşıtı olan rahatlık ile bir şeyi zorlanmadan, gönül hoşluğuyla verme durumunu anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel karşıtlık, sıkıntılı ve sert durum karşısındaki rahatlık ve ferahlıktır."},{"facet_id":"F002","role":"extension","statement":"Verme bağlamında rahatlık, isteksizlik veya zorlama olmadan gönülden vermek olarak gerçekleşir."}],"identity_rationale":"Kaynak ifadesi bir kullanımda sıkıntının karşıtı olan rahatlığı, başka bir kullanımda ise bir şeyi içten ve isteyerek vermeyi gösterir. Çerçeve kullanılabilir, ancak gönüllü veriş rahatlık çekirdeğinin bağımsız eş anlamlısı değil, belirli verme bağlamındaki uzantısı olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"sıkıntısında ve rahatlığında; gönül hoşluğuyla verirken"}],"lexicalization_note":"Tanım yalnız sıkıntı-rahatlık karşıtlığını ve gönül hoşluğuyla verme kullanımını taşıyan belirtilmiş yapıya bağlıdır; yalın bir kök anlamı çıkarılmaz.","neighbor_coverage_note":"Sekiz dış aday ile on kardeş dalın tümü değerlendirildi; genel rahatlık, fiziksel yumuşaklık ve cömertlikten ayrımı gösteren üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak yapı bağımlıdır ve verme tutumuna uzanır; komşu genel yaşam ve durum rahatlığıdır.","focus_only":"Odak dal, gönül hoşluğuyla verme uzantısını içerir ve belirli söz yapısına bağlıdır.","gloss":"rahat durum","neighbor_only":"Komşu dal, sıkıntıdan sonra durumun düzelmesini ve gönül rahatlığını daha genel adlandırır.","neighbor_ref":"root_000553/B002","relation_type":"near_synonym","shared_zone":"İki dal sıkıntının karşıtı olan rahat ve iyi hali anlatır."},{"boundary_match":"partial","distinction":"Odak belirli durum ve verme yapısına bağlıdır; komşu yaşam, yolculuk ve yerleşme alanlarına yayılır.","focus_only":"Odak dal, sıkıntı karşıtlığını ve isteyerek verme biçimini içerir.","gloss":"rahatlık ve yumuşaklık","neighbor_only":"Komşu dal, yumuşak yürüyüşü, kolay yolu ve su başında sakin konaklamayı da kapsar.","neighbor_ref":"root_000426/B002","relation_type":"near_synonym","shared_zone":"Her iki dal rahatlık, kolaylık ve sıkıntısız olma alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak tek verişteki iç rahatlığını, komşu ise kişinin sürekli cömertlik niteliğini ve bol bağışını kurar.","focus_only":"Odak dal, verişin zorlamasız ve gönülden oluş biçimini belirtir.","gloss":"isteyerek verme ve cömertlik","neighbor_only":"Komşu dal, cömertlik niteliğini ve çokça bağışta bulunmayı başlı başına adlandırır.","neighbor_ref":"root_001487/B008","relation_type":"near_neighbor","shared_zone":"İki dal isteyerek başkasına bir şey verme durumunda kesişir."}],"source_phrase_ar":"النجدة الشدة والرسل الرخاء (maqayis)؛ في نجدتها ورسلها يريد الشدة والرخاء (sihah)؛ إلا من أعطى في رسلها أي بطيب نفس منه (tahdhib)","source_summary":"Kaynakların ortak malzemesi rahatlığı sıkıntının karşısına koyar; verme bağlamında bu rahatlık, kişinin içinden gelerek ve isteyerek vermesi biçiminde açıklanır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الرسل في مقابلة النجدة والشدة والرسل بمعنى الرخاء أو الإعطاء بطيب نفس","what_is_not_ar":"ليس هو اللبن ولا القطيع وإن اشترك اللفظ"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000563/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْسَلَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>arosala|ROOT:rsl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"105:3:1:2","qac_word_ref":"105:3:1","surface_ar":"أَرْسَلَ"}],"gloss":"özel adlandırma kümesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dalın tek ortak özelliği, ortak anlamı bulunmayan özel adlandırmaların geçici olarak aynı yapısal kapta toplanmış olmasıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kullanım birlikte anılan iki damarı adlandırır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kullanım belirli bir topluluğun damızlık erkek devesini adlandırır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kullanım aktarım zinciri kesintili olan bir sözü niteler."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bir kullanım boncuk ve başka parçalardan oluşan kolyeyi adlandırır."}},{"facet_id":"F006","role":"source_variant","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Bir kullanım henüz başını örtmeyen küçük kızı niteler."}},{"facet_id":"F007","role":"source_variant","source_fields":["distinctive_facets[F007]"],"statements":{"statement":"Bir kullanım kısa bir ok türünü adlandırır."}}],"root_ar":"ر س ل","root_id":"root_000563","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"تسميات مفردة مخصوصة","concept_gloss":"özel adlandırma kümesi","definition":"Bu dal ortak bir anlam çekirdeği göstermeyen altı ayrı adlandırmayı bir arada tutmaktadır; kısa ok, iki damar, damızlık erkek deve, aktarım zinciri kopuk söz, boncuklu kolye ve başını örtmeyen küçük kız ayrı ayrı ele alınmalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dalın tek ortak özelliği, ortak anlamı bulunmayan özel adlandırmaların geçici olarak aynı yapısal kapta toplanmış olmasıdır."},{"facet_id":"F002","role":"source_variant","statement":"Bir kullanım birlikte anılan iki damarı adlandırır."},{"facet_id":"F003","role":"source_variant","statement":"Bir kullanım belirli bir topluluğun damızlık erkek devesini adlandırır."},{"facet_id":"F004","role":"source_variant","statement":"Bir kullanım aktarım zinciri kesintili olan bir sözü niteler."},{"facet_id":"F005","role":"source_variant","statement":"Bir kullanım boncuk ve başka parçalardan oluşan kolyeyi adlandırır."},{"facet_id":"F006","role":"source_variant","statement":"Bir kullanım henüz başını örtmeyen küçük kızı niteler."},{"facet_id":"F007","role":"source_variant","statement":"Bir kullanım kısa bir ok türünü adlandırır."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"kısa ok"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"iki damar"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"belirli bir topluluğun damızlık erkek devesi"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"aktarım zinciri kesintili söz"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"boncuklu kolye"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"başını henüz örtmeyen küçük kız"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"الراسلان عرقان (maqayis)؛ المرسال سهم قصير (sihah)؛ هذا رسيل بني فلان أي فحل إبلهم وحديث مرسل والمرسلة القلادة وجارية رسل (tahdhib)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه المرسال للسهم القصير والمرسلة للقلادة والراسلان للعرقين والحديث المرسل والجارية الرسل ورسيل الفحل","what_is_not_ar":"ليس هو المعنى العام للرسول ولا القطيع ولا اللبن"},"support_links":[]},{"boundary":"Dal gerçek kuşu ve uçuşu temel alır; hız, at niteliği, kuş deseni ve kuş bolluğu buna bağlı özel kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000962/B001","candidate_links":[{"candidate_id":"cand_ab8f894712f8f7114996","lane":"micro"},{"candidate_id":"cand_9a0e4e7327fa2b496ecf","lane":"micro"},{"candidate_id":"cand_eefb4ed317c3cc5e44e9","lane":"micro"},{"candidate_id":"cand_d85c77f21ae6775397f9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَيْر","morph_features":"STEM|POS:N|LEM:Tayor|ROOT:Tyr|MP|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:3:3:1","qac_word_ref":"105:3:3","surface_ar":"طَيْرًا"}],"gloss":"kanatlı canlı ve uçuş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kanatlı canlı ve onun havada ilerleme hareketi dalın ortak çekirdeğidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hafifçe veya olağanüstü hızlı ilerleme, uçuş hareketine benzetilerek anlatılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir canlıyı ya da nesneyi havalanmaya yöneltme, uçuşun ettirgen biçimidir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"At için kullanılan özel birliktelik hız ve yürek pekliğini bildirir."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Kumaştaki kuş resimleri ile bir yerdeki kuş bolluğu, kuşa bağlı niteleme kullanımlarıdır."}}],"root_ar":"ط ي ر","root_id":"root_000962","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın canlı ile hareketten oluşan ortak çekirdeğini birlikte karşılar.","boundary_detail":"Dal gerçek kuşu ve uçuşu temel alır; hız, at niteliği, kuş deseni ve kuş bolluğu buna bağlı özel kullanımlardır.","branch_image_ar":"خفة الطيران والطير","concept_gloss":"kanatlı canlı ve uçuş","contextual_glosses":[{"applicability":"Gerçek uçuşta ve uçuşa benzetilen çok hızlı ilerlemede kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Havada ilerleme ile hız benzetmesini bağlama göre korur."},"facet_ids":["F001","F002"],"text":"uçmak; hızla gitmek","usage_role":"contextual"},{"applicability":"Bir şeyi ya da canlıyı uçmaya yöneltme bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uçuş hareketinin ettirgen katılımcı düzenini açıkça korur."},"facet_ids":["F003"],"text":"uçurmak","usage_role":"contextual"}],"definition":"Kanatlı bir canlının havada ilerlemesi ve bu hareketi yapan canlıdır. Hafifçe ya da çok hızlı gitme, bir şeyi uçurma, hızlı ve atılgan at, kuş desenli kumaş ve kuşu bol yer kullanımları bu çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kanatlı canlı ve onun havada ilerleme hareketi dalın ortak çekirdeğidir."},{"facet_id":"F002","role":"extension","statement":"Hafifçe veya olağanüstü hızlı ilerleme, uçuş hareketine benzetilerek anlatılır."},{"facet_id":"F003","role":"specialization","statement":"Bir canlıyı ya da nesneyi havalanmaya yöneltme, uçuşun ettirgen biçimidir."},{"facet_id":"F004","role":"associated_use","statement":"At için kullanılan özel birliktelik hız ve yürek pekliğini bildirir."},{"facet_id":"F005","role":"associated_use","statement":"Kumaştaki kuş resimleri ile bir yerdeki kuş bolluğu, kuşa bağlı niteleme kullanımlarıdır."}],"identity_rationale":"Kaynak ifadesi kanatlı canlıyı ve uçma eylemini merkeze alırken hafiflik, hız, uçurma, kuş desenli kumaş ve kuşu bol yer gibi açıkça belirtilen kullanımları da aynı dalda toplar. Verilen çerçeve bu çekirdek ile ona bağlı kullanımları doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kuşlar; kuş türünden kanatlı canlı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kuş; havada uçan kanatlı canlı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kuşlar"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"uçmak; uçmuşçasına hızlanmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"uçma, uçuş"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"uçurmak, uçmaya yöneltmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"hızlı at"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kuş desenli dokuma veya giysi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kuşu bol arazi"}],"lexicalization_note":"Tanım yalın kuş ve uçuş biçimleriyle bunlardan türeyen at, kumaş ve yer birlikteliklerini ayırır; özel birliktelikleri yalın kök anlamına genellemez.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; yayımlanan üçü uçuş, kanat hareketi ve hız sınırlarını doğrudan aydınlatır, kalanlar yalnızca kuş parçası, yavaş yürüyüş ya da öteki dalların uzak temalarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta belirleyici hareket kanatlı canlının uçuşudur; komşuda ise ortam içinde yüzme veya akıcı koşma daha geniş bir hareket örüntüsüdür.","focus_only":"Odak dal kanatlı canlıyı, gerçek uçuşu ve uçurmayı kapsar.","gloss":"uçuş ile akıcı ilerleme","neighbor_only":"Komşu dal yüzmeyi, koşuyu ve gök cisimlerinin ilerleyişini de kapsar.","neighbor_ref":"root_000666/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal havada ya da bir ortam içinde akıcı ilerlemeyi anlatabilir."},{"boundary_match":"partial","distinction":"Kanat çırpmak uçuşun bir hareket parçası olabilir, fakat odak dalın bütünü olan havada ilerlemeyle her durumda aynı değildir.","focus_only":"Odak, havada yer değiştirmeyle sonuçlanan bütün uçuş hareketini bildirir.","gloss":"uçmak ile kanat çırpmak","neighbor_only":"Komşu, yer değiştirme gerektirmeyen kanat çırpma hareketini özellikle bildirir.","neighbor_ref":"root_000581/B001","relation_type":"near_neighbor","shared_zone":"İki dal da kuşun kanatlarını kullanmasına dayanan hareket alanındadır."},{"boundary_match":"partial","distinction":"Odak hızın kendisini uçuşa benzetir; komşu ise belirli ve sürdürülen bir yürüyüş ya da ilerleme biçimini adlandırır.","focus_only":"Odakta hız, uçuş imgesinden doğan bağlı bir genişlemedir.","gloss":"uçacak gibi hızlanmak","neighbor_only":"Komşuda hız ve öne geçme, özellikle bineklerin uzun süreli yürüyüş biçimidir.","neighbor_ref":"root_001053/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal binek hayvanının hızlı ve ileri yönlü gidişini anlatabilir."}],"source_phrase_ar":"الطير جمع طائر (maqayis;sihah;mufradat); الطائر كل ذي جناح يسبح في الهواء (mufradat); الطيران مصدر طار يطير (ayn;sihah); لكل من خف قد طار وكل سرعة (maqayis); فرس مطار للسريع وحديد الفؤاد (mufradat;ayn); المطير من البرود والثياب ما صور فيه صور الطيور (ayn); أرض مطارة كثيرة الطير (sihah)","source_summary":"Kaynakların toplu anlatımı kuşu, uçuşu ve uçurmayı temel alır; hız benzetmesini, hızlı atı, kuş desenli dokumayı ve kuşu bol araziyi de buna bağlı kullanımlar olarak verir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الطير والطائر والطيران وما دل على الخفة في الهواء أو السرعة أو الإطارة وما نسب إلى صور الطير وكثرته","what_is_not_ar":"ليس التشاؤم ولا العمل الملازم ولا تفرق الشيء بعد انفصاله"},"support_links":["sup_30f767751a30a01b43e7","sup_630a2304256207d9379f","sup_8bdbc1e3ecbdfcad74d9","sup_d5bf3c1aefa3e3bb9755"]},{"boundary":"Dal yalın hızdan değil, parçaların ayrılması, çevreye yayılması veya uzayan bir şeyin dağınık görünmesinden oluşur.","branch_kind":"mixed_non_bare","branch_ref":"root_000962/B002","candidate_links":[{"candidate_id":"cand_b75059b67363bfe60022","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَيْر","morph_features":"STEM|POS:N|LEM:Tayor|ROOT:Tyr|MP|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:3:3:1","qac_word_ref":"105:3:3","surface_ar":"طَيْرًا"}],"gloss":"dağılıp yayılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünün parçaları ayrılır, dağılır ve başlangıç yerinden uzaklaşabilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Işık, kötülük veya toz, geniş bir alana ya da havaya yayılan şey olarak nitelenir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Saçın ya da hörgüç ucunun uzayıp çevreye dağılması, uçuş benzeri görünüşle anlatılır."}}],"root_ar":"ط ي ر","root_id":"root_000962","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Parçaların ayrılması, uzaklaşması ve çevreye yayılması biçimindeki ortak çekirdeğe uygundur.","boundary_detail":"Dal yalın hızdan değil, parçaların ayrılması, çevreye yayılması veya uzayan bir şeyin dağınık görünmesinden oluşur.","branch_image_ar":"انتشار بعد خفة","concept_gloss":"dağılıp yayılma","contextual_glosses":[{"applicability":"Tan ışığının ufuk boyunca genişlemesi bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Işığın ufukta geniş bir alana yayılmasını tam olarak korur."},"facet_ids":["F002"],"text":"ufka yayılmak","usage_role":"contextual"},{"applicability":"Tozun parçacıklar hâlinde havaya dağıldığı bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tozun ayrılıp havanın içinde çevreye dağılmasını korur."},"facet_ids":["F001","F002"],"text":"havaya savrulmak","usage_role":"contextual"},{"applicability":"Saç veya hörgüç ucu gibi uzayan ve çevreye yayılan şeylerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uzama ile çevreye dağınık biçimde yayılmayı birlikte korur."},"facet_ids":["F003"],"text":"uzayıp dağılmak","usage_role":"contextual"}],"definition":"Bir şeyin parçalarının birbirinden ayrılarak dağılması, uzaklaşması ya da çevreye yayılmasıdır. Tan ışığı, kötülük ve tozun yayılması ile saçın veya hörgüç ucunun uzayıp dağınık görünmesi bu çekirdeğin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünün parçaları ayrılır, dağılır ve başlangıç yerinden uzaklaşabilir."},{"facet_id":"F002","role":"specialization","statement":"Işık, kötülük veya toz, geniş bir alana ya da havaya yayılan şey olarak nitelenir."},{"facet_id":"F003","role":"extension","statement":"Saçın ya da hörgüç ucunun uzayıp çevreye dağılması, uçuş benzeri görünüşle anlatılır."}],"identity_rationale":"Kaynak ifadesi bir şeyin dağılıp gitmesini açık çekirdek olarak verir ve tan ışığının, kötülüğün, tozun ya da saçın çevreye yayılması veya uzaması gibi görünüşleri bu çekirdeğe bağlar. Verilen dal çerçevesi bu ayrılma ve yayılma düzenini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"dağılmak, ayrılıp gitmek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ışığı ufka yayılmış tan"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"her yana yayılmış kötülük"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"havaya yayılmış toz"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"uzayıp dağılan saç"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"uzayıp yayılmış hörgüç ucu"}],"lexicalization_note":"Tan, kötülük, toz, saç ve hörgüç kullanımları kendi birlikteliklerine bağlı tutulur; ortak dağılıp yayılma çekirdeği bunlarla karıştırılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen üç karşılaştırma dağılma, ettirgen dağıtma ve havada uzanma sınırlarını gösterir, ötekiler yalnızca tek bir örneği ya da uzak bir hareket alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak ayrılma, uzaklaşma ve uçuş benzeri hafif yayılmayı öne çıkarır; komşu ise duyulma, yaygınlaşma ve çoğalma alanlarında daha geniştir.","focus_only":"Odakta bir şeyin parçalarının ayrılıp gitmesi ve hafifçe yayılması belirgindir.","gloss":"dağılmak ve yayılmak","neighbor_only":"Komşu, haberin insanlar arasında duyulmasını ve bir şeyin çoğalmasını da kapsar.","neighbor_ref":"root_000836/B003","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyin başlangıç sınırını aşarak çevreye yayılmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dağılan şeyin geçirdiği durumu bildirir; komşu ise çoğu kullanımda bu sonucu doğuran ettirgen dağıtma eylemini kapsar.","focus_only":"Odak çoğunlukla dağılan şeyin kendiliğinden ayrılıp yayılmasını anlatır.","gloss":"dağılmak ile dağıtmak","neighbor_only":"Komşu bir etkenin nesneleri dağıtması, saçması veya sermesi eylemini de merkezine alır.","neighbor_ref":"root_000083/B001","relation_type":"near_neighbor","shared_zone":"İki dal da parçaların geniş bir alana ayrılarak yayılması sonucunu paylaşır."},{"boundary_match":"partial","distinction":"Odak genel dağılma çekirdeğinden özel yayılma örneklerine gider; komşu yükselme ve havada uzanmayı kendi başına kapsayan daha yönlü bir alan taşır.","focus_only":"Odak parçalanma, dağılma ve başlangıç yerinden uzaklaşmayı da içerir.","gloss":"havaya ya da ufka yayılmak","neighbor_only":"Komşu ışık, koku, ok veya tozun yükselmesini ve uzanmasını özellikle içerir.","neighbor_ref":"root_000706/B001","relation_type":"near_synonym","shared_zone":"Işık ve tozun bir alan boyunca uzanıp yayılması iki dalda da bulunur."}],"source_phrase_ar":"تطاير الشيء تفرق (maqayis;sihah); التطاير التفرق والذهاب (ayn); فجر مستطير إذا انتشر ضوؤه في الأفق (ayn); فجر مستطير أي فاش وغبار مستطار (mufradat); خذ ما طار من شعر رأسك أي ما انتشر (mufradat;sihah)","source_summary":"Toplu kaynak anlatımı dağılma, ayrılma ve uzaklaşmayı birleştirir; ufka yayılan tan ışığını, yayılan kötülüğü, havadaki tozu ve uzayıp dağılan saç benzeri görünümleri bunun altında toplar.","sources":["MQ","AY","SI","MU"],"what_is_ar":"تفرق الشيء وذهابه وانتشار الفجر والشر والغبار وامتداد الشعر حتى كأنه طار","what_is_not_ar":"ليس ذات الطير ولا الزجر والتشاؤم ولا السرعة المجردة"},"support_links":["sup_3bb8eb72d603fbb2a398"]},{"boundary":"Uğur yorumu dalın çekirdeğidir; kişiye yüklenen iş veya uğursuz pay, aynı sözcük alanındaki bağlı fakat ayrı bir genişlemedir.","branch_kind":"mixed_non_bare","branch_ref":"root_000962/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَيْر","morph_features":"STEM|POS:N|LEM:Tayor|ROOT:Tyr|MP|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:3:3:1","qac_word_ref":"105:3:3","surface_ar":"طَيْرًا"}],"gloss":"belirtiyi uğur ya da uğursuzluk sayma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işaret gelecek için iyi veya kötü belirti sayılarak ondan sonuç çıkarılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuşu ürkütüp hareketinin yönünü yorumlama, belirti çıkarmanın kaynaklarda belirtilen özel biçimidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişinin kendisine yüklenen işi veya peşini bırakmayan uğursuz payı da aynı söz alanıyla anlatılır."}}],"root_ar":"ط ي ر","root_id":"root_000962","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın işaret yorumlama ve bundan iyi ya da kötü sonuç çıkarma çekirdeğini karşılar.","boundary_detail":"Uğur yorumu dalın çekirdeğidir; kişiye yüklenen iş veya uğursuz pay, aynı sözcük alanındaki bağlı fakat ayrı bir genişlemedir.","branch_image_ar":"تطيّر وطائر ملازم","concept_gloss":"belirtiyi uğur ya da uğursuzluk sayma","contextual_glosses":[{"applicability":"Bir olay veya nesne geleceğe ilişkin belirti kabul edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşarete iyi veya kötü gelecek değeri yükleme eylemini korur."},"facet_ids":["F001"],"text":"uğurlu ya da uğursuz saymak","usage_role":"general"},{"applicability":"Kişinin kendi işi ya da ona bağlanan uğursuz yazgı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye bağlanma ile iş ve uğursuz pay seçeneklerini birlikte korur."},"facet_ids":["F003"],"text":"kişiye yüklenen iş veya uğursuz pay","usage_role":"explanatory"}],"definition":"Bir işareti, başlangıçta özellikle kuş davranışını, olacaklar için iyi ya da kötü belirti sayma ve buna göre uğur veya uğursuzluk çıkarma eylemidir. Kişinin kendisine yüklenen işi ya da uğursuz payı bildiren kullanım, bu belirti anlayışından gelişmiş bağlı bir genişlemedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işaret gelecek için iyi veya kötü belirti sayılarak ondan sonuç çıkarılır."},{"facet_id":"F002","role":"specialization","statement":"Kuşu ürkütüp hareketinin yönünü yorumlama, belirti çıkarmanın kaynaklarda belirtilen özel biçimidir."},{"facet_id":"F003","role":"extension","statement":"Kişinin kendisine yüklenen işi veya peşini bırakmayan uğursuz payı da aynı söz alanıyla anlatılır."}],"identity_rationale":"Kaynak ifadesi belirtilerden uğur veya uğursuzluk çıkarma ile kişiye bağlanan iş ya da uğursuz payı aynı tarihsel imge altında sunar. Dal korunabilir, ancak iş ve yazgı kullanımı doğrudan belirti yorumlama eylemi değildir; çekirdek ile bu bağlı genişleme tanımda açıkça ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir şeyi uğurlu ya da uğursuz saymak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"uğursuzluk çıkarma; kötü sayılan belirti"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kişiye yüklenen işi veya uğursuz payı"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kuş hareketinden uğur ya da uğursuzluk çıkarma"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"uğursuzluk çıkarmayı reddeden söz"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"seni uğursuz saydık; ayrıca kaçırdık ya da kurtardık diye de açıklanır"}],"lexicalization_note":"Tanım belirti yorumlayan biçimleri, kişiye bağlanan iş veya yazgı birlikteliklerini ve tartışmalı özel sözü ayrı tutar; hiçbirini yalın uçuş anlamına taşımaz.","neighbor_coverage_note":"Adayların hepsi değerlendirildi; yayımlanan iki iç karşılaştırma gerçek kuş ve taşkınlıkla karışma olasılığını açıklar, diğer adayların hastalık, yaralanma veya durgunluk alanları anlam çekirdeği paylaşmaz.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta kuş, olayları yorumlamaya yarayan bir belirtidir; komşuda ise kuşun kendisi ve gerçek uçuş hareketi anlamın merkezindedir.","focus_only":"Odak kuş davranışı veya başka bir işaretten gelecek hakkında sonuç çıkarır.","gloss":"kuştan belirti çıkarmak","neighbor_only":"Komşu gerçek kanatlı canlıyı, uçmayı ve uçurmayı doğrudan anlatır.","neighbor_ref":"root_000962/B001","relation_type":"near_neighbor","shared_zone":"İki dal kuş imgesini ve bu imgeye bağlı söz varlığını paylaşır."},{"boundary_match":"field_only","distinction":"Belirti yorumlama bilişsel ve geleneksel bir işlemdir; öfke ya da taşkınlık ise canlıdaki huy ve davranış durumudur.","focus_only":"Odak bir işarete iyi veya kötü gelecek değeri yüklemeyi anlatır.","gloss":"uğursuzluk ile taşkınlık","neighbor_only":"Komşu insan ya da hayvandaki öfke, taşkınlık ve ölçüsüz atılganlığı anlatır.","neighbor_ref":"root_000962/B005","relation_type":"same_field","shared_zone":"İki dal aynı söz ailesinde olumsuz insan deneyimleriyle ilişkilendirilebilir."}],"source_phrase_ar":"تطير من الشيء فاشتقاقه من الطير (maqayis); الطيرة مصدر قولك اطيرت أي تطيرت (ayn); الطائر من الزجر في التشؤم والتسعد (ayn); طائر الإنسان عمله الذي قلده (ayn;sihah); ألا إنما طائرهم عند الله أي شؤمهم (mufradat); كل إنسان ألزمناه طائره في عنقه أي عمله (mufradat)","source_summary":"Toplu anlatım kuşlardan ya da başka belirtilerden iyi veya kötü sonuç çıkarma geleneğini verir; ayrıca kişinin kendisine bağlanan işini ve uğursuz payını aynı söz alanının genişlemesi olarak gösterir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"التطير والزجر بالفأل أو الشؤم والطائر بمعنى عمل الإنسان أو شؤمه الملازم له","what_is_not_ar":"ليس الطيران الحسي ولا انتشار الضوء والغبار ولا الغضب المجرد"},"support_links":[]},{"boundary":"Anlam kuyu veya kuyu çukuru adlarıyla kurulan birlikteliklere bağlıdır; genel genişlik ya da genel açıklık anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000962/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَيْر","morph_features":"STEM|POS:N|LEM:Tayor|ROOT:Tyr|MP|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:3:3:1","qac_word_ref":"105:3:3","surface_ar":"طَيْرًا"}],"gloss":"ağzı geniş kuyu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Niteliğin taşıyıcısı bir kuyu ya da kuyu çukurudur ve belirleyici özellik üst ağzının genişliğidir."}}],"root_ar":"ط ي ر","root_id":"root_000962","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca verilen kuyu ve kuyu çukuru birlikteliklerinin biçim niteliğini karşılar.","boundary_detail":"Anlam kuyu veya kuyu çukuru adlarıyla kurulan birlikteliklere bağlıdır; genel genişlik ya da genel açıklık anlamı değildir.","branch_image_ar":"فم واسع مفتوح","concept_gloss":"ağzı geniş kuyu","contextual_glosses":[{"applicability":"Kuyu yerine daha genel bir kazılmış çukur adı kullanılan birlikteliğe uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kazılmış çukuru ve üst ağzının genişliği koşulunu korur."},"facet_ids":["F001"],"text":"geniş ağızlı kuyu çukuru","usage_role":"contextual"}],"definition":"Kuyu veya kuyu çukuru için, üst açıklığının geniş olduğunu bildiren iki söz birlikteliğine özgü nitelemedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Niteliğin taşıyıcısı bir kuyu ya da kuyu çukurudur ve belirleyici özellik üst ağzının genişliğidir."}],"identity_rationale":"Kaynak ifadesi yalnızca ağzı geniş kuyu veya kuyu çukurunu niteleyen iki sabit birlikteliği verir. Dal çerçevesi bu somut biçim özelliğini doğru yakalar ve kuş bolluğu ya da kuş desenli kumaş gibi başka dallardaki kullanımları içeri almaz.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ağzı geniş kuyu"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"geniş ağızlı kuyu çukuru"}],"lexicalization_note":"Tanım yalnızca verilen kuyu ve kuyu çukuru birlikteliklerinde ağız açıklığını bildirir; niteleyiciyi bağımsız ve genel bir anlam gibi sunmaz.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; kuyu adı ve genel açıklıkla olan iki sınır yayımlandı, diğer çukur, kaya oyuğu, kazma ve su tutma dalları yalnızca aynı fiziksel çevreyi paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bağımsız kuyu adı değil, yalnızca geniş ağızlı kuyu birlikteliğidir; komşu ise kuyuyu veya çukuru doğrudan adlandırır.","focus_only":"Odak kuyunun üst ağzının geniş olmasını zorunlu bir nitelik yapar.","gloss":"geniş ağızlı kuyu","neighbor_only":"Komşu kuyu ve çeşitli amaçlarla kazılmış çukurları genişlik koşulu olmadan kapsar.","neighbor_ref":"root_000078/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal kuyu ya da kazılmış çukur türünden bir yapıyı gösterebilir."},{"boundary_match":"partial","distinction":"Odak kuyu adıyla kurulan dar bir nitelemedir; komşu ise taşıyıcı türünü sınırlamayan genel açıklık ve boşluk alanıdır.","focus_only":"Odak belirli bir kuyunun üst ağzındaki genişliği bildirir.","gloss":"kuyu ağzı ile genel açıklık","neighbor_only":"Komşu yer, bulut veya dağ içindeki genel boşluğu ve açılmış aralığı kapsar.","neighbor_ref":"root_000273/B004","relation_type":"near_neighbor","shared_zone":"İki dal bir mekândaki açıklık veya geniş boşluk görünümünde kesişir."}],"source_phrase_ar":"بئر مطارة إذا كانت واسعة الفم (maqayis); بئر مطارة واسعة الفم (sihah); جفر مطار (maqayis;sihah)","source_summary":"Kaynaklar kuyu ve kuyu çukuru adlarıyla kullanılan niteleyicinin, bu yapıların üst ağzının geniş olmasını bildirdiğinde birleşir.","sources":["MQ","SI"],"what_is_ar":"البئر أو الجفر الواسع الفم المسمى مطارا أو مطارة","what_is_not_ar":"ليس كثرة الطير في الأرض ولا صور الطير في الثياب"},"support_links":[]},{"boundary":"Dal insan ve hayvandaki öfkeli ya da ölçüsüz taşkınlıktır; salt hız, gerçek uçuş ve uğursuzluk yorumu değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000962/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَيْر","morph_features":"STEM|POS:N|LEM:Tayor|ROOT:Tyr|MP|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:3:3:1","qac_word_ref":"105:3:3","surface_ar":"طَيْرًا"}],"gloss":"öfkeli taşkınlık ve ölçüsüz atılganlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlıdaki öfke ve iç huzursuzluğu, davranışı ölçüsüz ve taşkın hâle getirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanda hafiflik, düşünmeden davranma ve kendini tutamama biçiminde görünür."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Köpek veya damızlık erkek hayvanda coşma ve saldırgan hareketlilik biçimini alır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"At için yürek pekliği, atılganlık ve hızlı gidiş birlikte öne çıkar."}}],"root_ar":"ط ي ر","root_id":"root_000962","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve hayvandaki öfke, huzursuzluk ve kendini tutmadan ileri atılma çekirdeğini karşılar.","boundary_detail":"Dal insan ve hayvandaki öfkeli ya da ölçüsüz taşkınlıktır; salt hız, gerçek uçuş ve uğursuzluk yorumu değildir.","branch_image_ar":"حدّة وطيش منطلق","concept_gloss":"öfkeli taşkınlık ve ölçüsüz atılganlık","contextual_glosses":[{"applicability":"Bir insanın öfkeli, hafif ve kendini tutamayan davranışı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öfke ile düşüncesiz ve ölçüsüz davranış eğilimini korur."},"facet_ids":["F001","F002"],"text":"çabuk öfkelenen ve düşünmeden atılan","usage_role":"contextual"},{"applicability":"Köpek veya damızlık erkek hayvanın taşkın hareketliliğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvandaki coşma ve saldırgan taşkınlık durumunu korur."},"facet_ids":["F003"],"text":"coşmuş ve saldırgan","usage_role":"contextual"},{"applicability":"Atın yürek pekliğiyle birleşen hızlı ve ileri atılan gidişini karşılar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ata özgü yürek pekliği, atılganlık ve hız birlikteliğini korur."},"facet_ids":["F004"],"text":"yürekli, atılgan ve hızlı","usage_role":"contextual"}],"definition":"İnsan ya da hayvanda öfke, iç huzursuzluğu, düşünmeden atılma ve coşkun hareket olarak görülen taşkın durumdur. Köpek ve damızlık erkekte coşma, atta ise yürek pekliğiyle birleşen hızlı ve atılgan gidiş bu durumun özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlıdaki öfke ve iç huzursuzluğu, davranışı ölçüsüz ve taşkın hâle getirir."},{"facet_id":"F002","role":"specialization","statement":"İnsanda hafiflik, düşünmeden davranma ve kendini tutamama biçiminde görünür."},{"facet_id":"F003","role":"specialization","statement":"Köpek veya damızlık erkek hayvanda coşma ve saldırgan hareketlilik biçimini alır."},{"facet_id":"F004","role":"extension","statement":"At için yürek pekliği, atılganlık ve hızlı gidiş birlikte öne çıkar."}],"identity_rationale":"Kaynak ifadesi insandaki öfke, hafiflik ve düşünmeden atılma ile hayvandaki coşkunluk, sert yüreklilik ve hızlı gidişi aynı taşkın hareket imgesi altında verir. Dal çerçevesi bu duygu ve davranış alanını doğru yansıtır; uğur yorumu veya gerçek uçuşu buna katmaz.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"öfke ve öfkeli taşkınlık"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"hafif ve düşünmeden davranan"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"taşkınlığının ve düşüncesizliğinin yanları"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"coşmuş, saldırgan köpek"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"yürekli, atılgan ve hızlı at"}],"lexicalization_note":"İnsandaki öfke ve düşüncesiz atılma, hayvandaki coşkunluk ve ata özgü yürek pekliği ayrı biçimlerde gösterilir; özel birliktelikler yalın bir hız anlamına çevrilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma öfke, coşkunluk ve ürkme sınırlarını gösterir, kalanlar yalnızca tek başına öfke, hareket ettirme veya aynı söz ailesindeki uzak dallardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak uçuş benzeri taşkın hareketi insan ve hayvan davranışına bağlar; komşu ise sertlik ve güç alanına, içki niteliğine kadar genişler.","focus_only":"Odak insanın yanı sıra köpek, damızlık erkek ve at gibi hayvanlardaki taşkınlığı kapsar.","gloss":"öfke, sertlik ve atılganlık","neighbor_only":"Komşu içkinin sertliğini ve kişinin güçlü, etkili oluşunu da aynı alan içinde kapsar.","neighbor_ref":"root_000002/B006","relation_type":"near_synonym","shared_zone":"İki dal insandaki öfke, acelecilik, düşüncesizlik ve sert davranışta örtüşür."},{"boundary_match":"partial","distinction":"Odak canlıdaki huy ve taşkın davranış üzerinde yoğunlaşır; komşu ise diretme, sürüp gitme ve olayların büyümesi gibi daha geniş süreçlere uzanır.","focus_only":"Odak hafiflik, çabuk öfkelenme ve hayvandaki coşkunluğu birlikte kapsar.","gloss":"taşkın öfke ve coşkunluk","neighbor_only":"Komşu bir işte diretme, kesintisiz ilerleme ve hareketlerin art arda gelmesini de kapsar.","neighbor_ref":"root_000792/B008","relation_type":"near_synonym","shared_zone":"Şiddetli öfke, coşma ve durgunluktan çıkan hareketlilik iki dalda da bulunur."},{"boundary_match":"partial","distinction":"Odak öfke, hiddet, hayvan coşkusu ve atta yürek pekliğine uzanır; komşu ise insandaki düşüncesiz taşkınlık ile darbe veya ürkme sonrası hayvan sıçramasını kapsar.","focus_only":"Odak öfke, hiddet, hayvan coşkusu ve atta yürek pekliği gibi iç durumları içerir.","gloss":"taşkınlık ile ürküp sıçrama","neighbor_only":"Komşu insandaki düşüncesiz taşkınlığı ve hayvanın vurulma veya ürkme üzerine sıçramasını bildirir.","neighbor_ref":"root_000651/B006","relation_type":"near_neighbor","shared_zone":"İki dal canlıdaki huzursuz, denetimsiz ve birden hızlanan hareketi paylaşır."}],"source_phrase_ar":"الطيرة الغضب وسمي كذا لأنه يستطار له الإنسان (maqayis); في فلان طيرة وطيرورة أي خفة وطيش (sihah); ازجر أحناء طيرك أي جوانب خفتك وطيشك (sihah); كلب مستطير كما يقال للفحل هائج (ayn); فرس مستطار أي حديد الفؤاد ماض طيار (ayn); فرس مطار للسريع ولحديد الفؤاد (mufradat)","source_summary":"Toplu kaynak anlatımı öfkeyi, düşünmeden atılmayı ve iç huzursuzluğunu bir araya getirir; hayvanlarda coşkunluk, atta ise yürek pekliği ve hız bu taşkınlığın özel görünüşleridir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الغضب والطيش والخفة النفسية والحدة والهياج في الإنسان أو الحيوان","what_is_not_ar":"ليس الفأل والتشاؤم ولا انتشار الضوء والغبار ولا الطير الجارح نفسه"},"support_links":[]},{"boundary":"Bu dal genel durgunluk veya genel bolluk değildir; her anlam yalnızca kendisine ait sabit kuşlu kalıpta geçerlidir.","branch_kind":"collocation","branch_ref":"root_000962/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَيْر","morph_features":"STEM|POS:N|LEM:Tayor|ROOT:Tyr|MP|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:3:3:1","qac_word_ref":"105:3:3","surface_ar":"طَيْرًا"}],"gloss":"kuşun durgunluğuyla anlatılan heybet veya bolluk","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki kalıp da kuşun kımıldamaması ya da bulunduğu yerden uçmaması imgesine dayanır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başlarda kuş varmış gibi durma kalıbı, heybet karşısında tam sessizliği ve hareketsizliği anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Karganın uçmaması kalıbı, bulunduğu yerde bolluk ve iyiliğin çok olmasını anlatır."}}],"root_ar":"ط ي ر","root_id":"root_000962","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca iki sabit kalıbın ortak imgesini ve birbirinden ayrı sonuçlarını birlikte açıklar.","boundary_detail":"Bu dal genel durgunluk veya genel bolluk değildir; her anlam yalnızca kendisine ait sabit kuşlu kalıpta geçerlidir.","branch_image_ar":"طير ساكن في المثل","concept_gloss":"kuşun durgunluğuyla anlatılan heybet veya bolluk","contextual_glosses":[{"applicability":"Bir topluluğun güçlü bir saygı veya korkuyla sessiz ve hareketsiz kaldığı bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Heybet nedenini, toplu sessizliği ve hareketsiz duruşu birlikte korur."},"facet_ids":["F002"],"text":"heybetten çıt çıkarmadan durmak","usage_role":"contextual"},{"applicability":"Bir yerin verimli, varlıklı ve çokça iyilik barındırdığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerdeki bolluk ile iyiliğin çokluğu anlamını birlikte korur."},"facet_ids":["F003"],"text":"bolluk ve iyilik içinde olmak","usage_role":"contextual"}],"definition":"Kuşun kımıldamaması veya uçmaması imgesiyle kurulan iki sabit anlatımdır. Birincisi insanların heybetten hiç ses çıkarmadan durmasını, ikincisi ise bir yerdeki bolluk ve iyiliğin çokluğunu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki kalıp da kuşun kımıldamaması ya da bulunduğu yerden uçmaması imgesine dayanır."},{"facet_id":"F002","role":"specialization","statement":"Başlarda kuş varmış gibi durma kalıbı, heybet karşısında tam sessizliği ve hareketsizliği anlatır."},{"facet_id":"F003","role":"specialization","statement":"Karganın uçmaması kalıbı, bulunduğu yerde bolluk ve iyiliğin çok olmasını anlatır."}],"identity_rationale":"Kaynak ifadesi iki ayrı kalıbı birlikte verir: biri heybet karşısındaki tam sessizlik ve durgunluğu, diğeri ise bolluk ve iyiliği anlatır. Dal ancak kuşun kımıldamaması ya da uçmaması imgesine dayanan bu iki kalıpla sınırlı bir söz öbeği kümesi olarak korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"heybetten çıt çıkarmadan durmak"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"bolluk ve iyilik içinde olmak"}],"lexicalization_note":"Tanım iki sabit kalıbı ayrı ayrı korur: kuşun başta durması heybetten sessizliği, karganın uçmaması ise bolluğu anlatır; bunlardan yalın anlam çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; yayımlanan iki ayrım durgunluk ve ürün bolluğu sınırlarını açıklar, diğerleri verimsizlik, bahçe, uyku ya da bitki gelişmesi gibi yalnızca tematik komşuluklar sunar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta durgunluk heybetin sonucu ve kuş imgesine bağlı bir anlatımdır; komşuda ise durma, kendi başına fiziksel durumdur.","focus_only":"Odak sabit bir kalıpta insanların heybetten sessiz ve hareketsiz kalmasını anlatır.","gloss":"heybetten donup kalmak","neighbor_only":"Komşu neden ve anlatım kalıbı aramadan bir şeyin durmasını veya az hareket etmesini anlatır.","neighbor_ref":"root_000114/B003","relation_type":"near_neighbor","shared_zone":"İki dal hareketin durması ve belirgin bir durgunluk görünümünde kesişir."},{"boundary_match":"field_only","distinction":"Odak kuşun uçmaması imgesiyle genel bolluk bildirir; komşu ise bolluğun kaynağı olan meyve veya ürünü doğrudan gösterir.","focus_only":"Odak sabit bir kalıpla bir yerdeki genel bolluk ve iyiliği anlatır.","gloss":"bolluk ile ürün","neighbor_only":"Komşu ağaç, ekin veya toprağın verdiği ürünü doğrudan adlandırır.","neighbor_ref":"root_000043/B002","relation_type":"same_field","shared_zone":"İki dal verimli yer, çok ürün ve geçim bolluğu alanında ilişkilidir."}],"source_phrase_ar":"كأن على رؤوسهم الطير إذا سكنوا من هيبة (sihah); في الخصب وكثرة الخير قولهم في شيء لا يطير غرابه (sihah)","source_summary":"Tek kaynak anlatımı kuşun durgunluğu üzerine kurulmuş iki ayrı kalıp aktarır: biri heybetten doğan toplu sessizliği, öteki bolluk ve iyiliği bildirir.","sources":["SI"],"what_is_ar":"الأمثال التي تجعل سكون الطير أو عدم طيرانه علامة على الهيبة أو الخصب","what_is_not_ar":"ليس طيرانا حقيقيا ولا تطيرا بفأل"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["105:3:1"],"branch_refs":[],"candidate_id":"cand_91616e37744cc1a25414","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:1:coordination-without-fixed-timing","source_type":"word_analysis","support_ids":["sup_66297e314055abda77a8","sup_72250032122b8f94d1e8"],"title":"coordination continues the prior action without fixing timing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:1","qac_refs":["105:3:1:1"],"status":"accepted"}},{"anchor_refs":["105:3:1"],"branch_refs":[],"candidate_id":"cand_4ab8485d5269c6053ed4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:1:fused-sound-boundary","source_type":"word_analysis","support_ids":["sup_66297e314055abda77a8","sup_828deb1b352c816bf856"],"title":"fused onset joins boundary and action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:1","qac_refs":["105:3:1:1"],"status":"accepted"}},{"anchor_refs":["105:3:1"],"branch_refs":[],"candidate_id":"cand_c10f2bc0ccbd168dba09","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:1:resumptive-operational-launch","source_type":"word_analysis","support_ids":["sup_66297e314055abda77a8","sup_ec5dc6aff3031276f2c1"],"title":"opening connector launches the concrete report","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:1","qac_refs":["105:3:1:1"],"status":"accepted"}},{"anchor_refs":["105:3:2"],"branch_refs":[],"candidate_id":"cand_afc70da937fc8febb8a8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000563"],"scope":"focus_ayah","source_local_id":"105:3:2:boundary-execution-arc","source_type":"word_analysis","support_ids":["sup_61cd42debbcc4a5987ef","sup_c5c73cd9e5b11b3e99d9"],"title":"abstract verdict becomes concrete deployment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:2","qac_refs":["105:3:1:2"],"status":"accepted"}},{"anchor_refs":["105:3:2"],"branch_refs":[],"candidate_id":"cand_281205824e911a4a3044","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000563"],"scope":"focus_ayah","source_local_id":"105:3:2:form-bound-agency-limit","source_type":"word_analysis","support_ids":["sup_61cd42debbcc4a5987ef","sup_f47e783d215c927d531e"],"title":"actual form blocks reflexive request framing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:2","qac_refs":["105:3:1:2"],"status":"accepted"}},{"anchor_refs":["105:3:2"],"branch_refs":[],"candidate_id":"cand_12db566f8c6ff1805215","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000563"],"scope":"focus_ayah","source_local_id":"105:3:2:hamza-dispatch-onset","source_type":"word_analysis","support_ids":["sup_61cd42debbcc4a5987ef","sup_f0a99569fdde3d3f68ba"],"title":"hamza onset marks decisive action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:2","qac_refs":["105:3:1:2"],"status":"accepted"}},{"anchor_refs":["105:3:2"],"branch_refs":[],"candidate_id":"cand_4e34ee333521a4cfbc84","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000563"],"scope":"focus_ayah","source_local_id":"105:3:2:hostile-dispatch-frame","source_type":"word_analysis","support_ids":["sup_49bb99a295e6d1eecd6a","sup_61cd42debbcc4a5987ef"],"title":"verb governs target and object in a hostile frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:2","qac_refs":["105:3:1:2"],"status":"accepted"}},{"anchor_refs":["105:3:2"],"branch_refs":[],"candidate_id":"cand_8c9f873faa3b415ce32a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000563"],"scope":"focus_ayah","source_local_id":"105:3:2:perfect-divine-causative","source_type":"word_analysis","support_ids":["sup_61cd42debbcc4a5987ef","sup_9f369debb2910b9f21eb"],"title":"completed Form IV dispatch keeps divine agency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:2","qac_refs":["105:3:1:2"],"status":"accepted"}},{"anchor_refs":["105:3:2"],"branch_refs":[],"candidate_id":"cand_79d17326fdc68b2a0f21","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000563"],"scope":"focus_ayah","source_local_id":"105:3:2:release-not-message","source_type":"word_analysis","support_ids":["sup_61cd42debbcc4a5987ef","sup_fa0c0042b4ede0b78aaf"],"title":"release pressure survives while message sense is not selected","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:2","qac_refs":["105:3:1:2"],"status":"accepted"}},{"anchor_refs":["105:3:2"],"branch_refs":[],"candidate_id":"cand_fc1ee2a079086a4b5385","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000563"],"scope":"focus_ayah","source_local_id":"105:3:2:unusual-bird-dispatch-pairing","source_type":"word_analysis","support_ids":["sup_4a64ea0e861bad736a59","sup_61cd42debbcc4a5987ef"],"title":"common sending root receives unusual flying object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:2","qac_refs":["105:3:1:2"],"status":"accepted"}},{"anchor_refs":["105:3:3"],"branch_refs":[],"candidate_id":"cand_e0140409e57eedafbd53","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:3:case-role-reversal","source_type":"word_analysis","support_ids":["sup_7930a5b8d6a7cf438134","sup_aaaae9d59a8e1d7bdf3f"],"title":"schemers become governed patients","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:3","qac_refs":["105:3:2:1","105:3:2:2"],"status":"accepted"}},{"anchor_refs":["105:3:3"],"branch_refs":[],"candidate_id":"cand_06de7a3429f2c87e2e21","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:3:fused-position-before-object","source_type":"word_analysis","support_ids":["sup_7930a5b8d6a7cf438134","sup_be22bb9ef684ce471906"],"title":"target is sealed before the instrument appears","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:3","qac_refs":["105:3:2:1","105:3:2:2"],"status":"accepted"}},{"anchor_refs":["105:3:3"],"branch_refs":[],"candidate_id":"cand_732fd505b8ea0faf81a8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:3:known-pronoun-target","source_type":"word_analysis","support_ids":["sup_7930a5b8d6a7cf438134","sup_e069f7f8817fdbac6eb0"],"title":"attached suffix identifies the known target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:3","qac_refs":["105:3:2:1","105:3:2:2"],"status":"accepted"}},{"anchor_refs":["105:3:3"],"branch_refs":[],"candidate_id":"cand_c5083f759d505f461e0a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:3:upon-against-targeting","source_type":"word_analysis","support_ids":["sup_7930a5b8d6a7cf438134","sup_fa3c202b92369edf9bb0"],"title":"preposition gives descent and hostility","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:3","qac_refs":["105:3:2:1","105:3:2:2"],"status":"accepted"}},{"anchor_refs":["105:3:4"],"branch_refs":[],"candidate_id":"cand_29382828787a7c3644e7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000962"],"scope":"focus_ayah","source_local_id":"105:3:4:descriptor-agreement","source_type":"word_analysis","support_ids":["sup_bd2f5b6c0ae7508dbb18","sup_c886a986003be6d42038"],"title":"following descriptor is locked to the birds","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:4","qac_refs":["105:3:3:1"],"status":"accepted"}},{"anchor_refs":["105:3:4"],"branch_refs":[],"candidate_id":"cand_154da6be320906638965","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000962"],"scope":"focus_ayah","source_local_id":"105:3:4:direct-object-instrument","source_type":"word_analysis","support_ids":["sup_b22156df965c7a730253","sup_c886a986003be6d42038"],"title":"flying agents are the explicit object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:4","qac_refs":["105:3:3:1"],"status":"accepted"}},{"anchor_refs":["105:3:4"],"branch_refs":[],"candidate_id":"cand_8644a2545284588ee17f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000962"],"scope":"focus_ayah","source_local_id":"105:3:4:flight-and-fate-pressure","source_type":"word_analysis","support_ids":["sup_8c4d99649f47a1f42922","sup_c886a986003be6d42038"],"title":"fate pressure shadows concrete flying agents","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:4","qac_refs":["105:3:3:1"],"status":"accepted"}},{"anchor_refs":["105:3:4"],"branch_refs":[],"candidate_id":"cand_6509af5a1327cfb259de","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000962"],"scope":"focus_ayah","source_local_id":"105:3:4:flight-downward-agent-arc","source_type":"word_analysis","support_ids":["sup_c886a986003be6d42038","sup_df3e945675ba5a9d2b10"],"title":"literal flight becomes downward hostile action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:4","qac_refs":["105:3:3:1"],"status":"accepted"}},{"anchor_refs":["105:3:4"],"branch_refs":[],"candidate_id":"cand_09336ce86ed6e33f55c0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000962"],"scope":"focus_ayah","source_local_id":"105:3:4:indefinite-collective-unspecified","source_type":"word_analysis","support_ids":["sup_15f6cf0f267d71b71523","sup_c886a986003be6d42038"],"title":"indefinite collective withholds species identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:4","qac_refs":["105:3:3:1"],"status":"accepted"}},{"anchor_refs":["105:3:4"],"branch_refs":[],"candidate_id":"cand_81a73fa02a089c7fb152","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000962"],"scope":"focus_ayah","source_local_id":"105:3:4:rare-dispatch-flight-field","source_type":"word_analysis","support_ids":["sup_6a123d49f70418e4429e","sup_c886a986003be6d42038"],"title":"dispatch and flying form a marked pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:4","qac_refs":["105:3:3:1"],"status":"accepted"}},{"anchor_refs":["105:3:4"],"branch_refs":[],"candidate_id":"cand_5c5f244ccfe8642ea701","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000962"],"scope":"focus_ayah","source_local_id":"105:3:4:sound-of-flight","source_type":"word_analysis","support_ids":["sup_2c55ba052c9a982f191b","sup_c886a986003be6d42038"],"title":"sound moves from heavy onset to flight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:4","qac_refs":["105:3:3:1"],"status":"accepted"}},{"anchor_refs":["105:3:5"],"branch_refs":[],"candidate_id":"cand_96c5d9adf628e69eaae8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:5:derivation-and-loanword-dispute","source_type":"word_analysis","support_ids":["sup_03c44a0149ca71d0443f","sup_67dd4310aee8f1c459ab"],"title":"derivational dispute stays as background","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:5","qac_refs":["105:3:4:1"],"status":"accepted"}},{"anchor_refs":["105:3:5"],"branch_refs":[],"candidate_id":"cand_08e2b2f11d3023f6e65c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:5:forward-projectile-arc","source_type":"word_analysis","support_ids":["sup_67dd4310aee8f1c459ab","sup_82519bdf18c272e1c6c3"],"title":"flock formation anticipates distributed stones","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:5","qac_refs":["105:3:4:1"],"status":"accepted"}},{"anchor_refs":["105:3:5"],"branch_refs":[],"candidate_id":"cand_2545dfb29cf868e25c44","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:5:hapax-closure-weight","source_type":"word_analysis","support_ids":["sup_49aa166e2fa9365fb041","sup_67dd4310aee8f1c459ab"],"title":"rare descriptor lands at ayah closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:5","qac_refs":["105:3:4:1"],"status":"accepted"}},{"anchor_refs":["105:3:5"],"branch_refs":[],"candidate_id":"cand_61d1824a8b3ba2eae2bb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:5:herd-root-transfer","source_type":"word_analysis","support_ids":["sup_2adca5bda88474f2c184","sup_67dd4310aee8f1c459ab"],"title":"herd-field pressure is transferred to airborne groups","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:5","qac_refs":["105:3:4:1"],"status":"accepted"}},{"anchor_refs":["105:3:5"],"branch_refs":[],"candidate_id":"cand_14c6052edef04efe3b1f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:5:marked-plural-not-species","source_type":"word_analysis","support_ids":["sup_67dd4310aee8f1c459ab","sup_d2c778bb66ba84dc6dc9"],"title":"marked form avoids a settled species label","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:5","qac_refs":["105:3:4:1"],"status":"accepted"}},{"anchor_refs":["105:3:5"],"branch_refs":[],"candidate_id":"cand_70e44590c308f2aa297d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:5:qualifier-or-manner","source_type":"word_analysis","support_ids":["sup_67dd4310aee8f1c459ab","sup_f019ff055586c5b1ee8b"],"title":"final word qualifies the sent birds","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:5","qac_refs":["105:3:4:1"],"status":"accepted"}},{"anchor_refs":["105:3:5"],"branch_refs":[],"candidate_id":"cand_44178e687a98e30ac472","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:5:sound-and-boundary-force","source_type":"word_analysis","support_ids":["sup_5d578ed484ff7f9825b7","sup_67dd4310aee8f1c459ab"],"title":"pulsing sound matches multiplied arrivals","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:5","qac_refs":["105:3:4:1"],"status":"accepted"}},{"anchor_refs":["105:3:5"],"branch_refs":[],"candidate_id":"cand_78b12f9e8f21188f15da","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:3:5:wave-like-grouping","source_type":"word_analysis","support_ids":["sup_20b27f088df231ef8697","sup_67dd4310aee8f1c459ab"],"title":"successive scattered groups control the image","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:3:5","qac_refs":["105:3:4:1"],"status":"accepted"}},{"anchor_refs":["105:3:1"],"branch_refs":[],"candidate_id":"cand_2943277a0e4d238c08f1","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000563"],"scope":"focus_ayah","source_local_id":"105:3:1:2","source_type":"qac_morpheme","support_ids":["sup_dcf534a2c45bbc34a176"],"title":"QAC root occurrence: ر س ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["105:3:3"],"branch_refs":[],"candidate_id":"cand_6b28e18459c665273d60","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000962"],"scope":"focus_ayah","source_local_id":"105:3:3:1","source_type":"qac_morpheme","support_ids":["sup_27f9463c4b7e074fa992"],"title":"QAC root occurrence: ط ي ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["105:3:4"],"branch_refs":[],"candidate_id":"cand_4e5cc56dc3b297200acf","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000006"],"scope":"focus_ayah","source_local_id":"105:3:4:1","source_type":"qac_morpheme","support_ids":["sup_bdcff7df698bae73fe56"],"title":"QAC root occurrence: ء ب ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["105:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"105:3","branch_refs":["root_000006/B003","root_000563/B001","root_000962/B001"],"candidate_id":"cand_ab8f894712f8f7114996","commentary_obligation":"review","hft_ref":"hft_8d3423b39c15cf3e17cb","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_dispatched_airborne_agency","source_type":"hft","support_ids":["sup_d5bf3c1aefa3e3bb9755"],"title":"base_dispatched_airborne_agency","trust":"legacy_unbound"},{"anchor_refs":["105:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"105:3","branch_refs":["root_000006/B003","root_000563/B005","root_000962/B002"],"candidate_id":"cand_b75059b67363bfe60022","commentary_obligation":"review","hft_ref":"hft_4d52f4d4de64aecd4423","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_pulsed_distributed_swarm","source_type":"hft","support_ids":["sup_3bb8eb72d603fbb2a398"],"title":"base_pulsed_distributed_swarm","trust":"legacy_unbound"},{"anchor_refs":["105:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"105:3","branch_refs":["root_000006/B003","root_000563/B002","root_000962/B001"],"candidate_id":"cand_9a0e4e7327fa2b496ecf","commentary_obligation":"review","hft_ref":"hft_2eb71a4b2f5deadf2d11","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_embodied_message","source_type":"hft","support_ids":["sup_30f767751a30a01b43e7"],"title":"base_embodied_message","trust":"legacy_unbound"},{"anchor_refs":["105:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"105:3","branch_refs":["root_000006/B004","root_000563/B001","root_000962/B001"],"candidate_id":"cand_eefb4ed317c3cc5e44e9","commentary_obligation":"review","hft_ref":"hft_876a4df468b6fe6d957d","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:out_light_medium_heavy_burden","source_type":"hft","support_ids":["sup_8bdbc1e3ecbdfcad74d9"],"title":"out_light_medium_heavy_burden","trust":"legacy_unbound"},{"anchor_refs":["105:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"105:3","branch_refs":["root_000006/B001","root_000563/B003","root_000962/B001"],"candidate_id":"cand_d85c77f21ae6775397f9","commentary_obligation":"review","hft_ref":"hft_fe0f2acbb5bbebe4a4f9","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:out_airborne_herd_logic","source_type":"hft","support_ids":["sup_630a2304256207d9379f"],"title":"out_airborne_herd_logic","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"105:3:1:1","qac_word_ref":"105:3:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَرْسَلَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>arosala|ROOT:rsl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"105:3:1:2","qac_word_ref":"105:3:1","root_ar":"ر س ل","surface_ar":"أَرْسَلَ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"105:3:2:1","qac_word_ref":"105:3:2","root_ar":"","surface_ar":"عَلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"105:3:2:2","qac_word_ref":"105:3:2","root_ar":"","surface_ar":"هِمْ"},{"lemma_ar":"طَيْر","morph_features":"STEM|POS:N|LEM:Tayor|ROOT:Tyr|MP|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:3:3:1","qac_word_ref":"105:3:3","root_ar":"ط ي ر","surface_ar":"طَيْرًا"},{"lemma_ar":"أَبَابِيل","morph_features":"STEM|POS:ADJ|LEM:>abaAbiyl|ROOT:Abl|MP|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"105:3:4:1","qac_word_ref":"105:3:4","root_ar":"ء ب ل","surface_ar":"أَبَابِيلَ"}],"word_analysis_qac_refs":[["105:3:1:1"],["105:3:1:2"],["105:3:2:1","105:3:2:2"],["105:3:3:1"],["105:3:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["105:3:1","105:3:2","105:3:3","105:3:4","105:3:5"]},"focus_surface_evidence":{"arabic_uthmani":"وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"105:3:1:1","qac_word_ref":"105:3:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَرْسَلَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>arosala|ROOT:rsl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"105:3:1:2","qac_word_ref":"105:3:1","root_ar":"ر س ل","surface_ar":"أَرْسَلَ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"105:3:2:1","qac_word_ref":"105:3:2","root_ar":"","surface_ar":"عَلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"105:3:2:2","qac_word_ref":"105:3:2","root_ar":"","surface_ar":"هِمْ"},{"lemma_ar":"طَيْر","morph_features":"STEM|POS:N|LEM:Tayor|ROOT:Tyr|MP|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"105:3:3:1","qac_word_ref":"105:3:3","root_ar":"ط ي ر","surface_ar":"طَيْرًا"},{"lemma_ar":"أَبَابِيل","morph_features":"STEM|POS:ADJ|LEM:>abaAbiyl|ROOT:Abl|MP|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"105:3:4:1","qac_word_ref":"105:3:4","root_ar":"ء ب ل","surface_ar":"أَبَابِيلَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["105:3:1:1"],["105:3:1:2"],["105:3:2:1","105:3:2:2"],["105:3:3:1"],["105:3:4:1"]],"word_analysis_refs":["105:3:1","105:3:2","105:3:3","105:3:4","105:3:5"],"word_rows":[{"analysis_record_ref":"105:3:1","analytic_gloss_range_en":"coordinating ayah-opening connector that continues the prior divine-action report while opening the concrete dispatch scene without fixing exact timing","analytic_root_gloss_range_en":null,"qac_refs":["105:3:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"105:3:2","analytic_gloss_range_en":"completed causative dispatch or release of an explicit airborne object against a marked target; message-bearing associations are backgrounded rather than selected","analytic_root_gloss_range_en":"broad range around sending forth, dispatch, release, messengers and messages, easy flow, and successive groups; the local Form IV frame selects caused hostile deployment","qac_refs":["105:3:1:2"],"root":{"arabic":"ر س ل","transliteration":"r-s-l"},"surface":{"arabic":"أَرْسَلَ","transliteration":"arsala"}},{"analysis_record_ref":"105:3:3","analytic_gloss_range_en":"prepositional target phrase meaning upon or against them, with a definite suffix referring back to the elephant people and marking them as exposed recipients of hostile dispatch","analytic_root_gloss_range_en":null,"qac_refs":["105:3:2:1","105:3:2:2"],"root":{},"surface":{"arabic":"عَلَيْهِمْ","transliteration":"ʿalayhim"}},{"analysis_record_ref":"105:3:4","analytic_gloss_range_en":"indefinite collective flying agents, the explicit object of dispatch, left taxonomically unspecified and prepared for distribution by the following descriptor and action in 105:4","analytic_root_gloss_range_en":"range around flying, birds or flying creatures, movement through the air, and omen or fate associations; the local noun selects concrete flying agents while secondary fate pressure remains only a shadow","qac_refs":["105:3:3:1"],"root":{"arabic":"ط ي ر","transliteration":"ṭ-y-r"},"surface":{"arabic":"طَيْرًا","transliteration":"ṭayran"}},{"analysis_record_ref":"105:3:5","analytic_gloss_range_en":"rare final descriptor for the sent flying agents as separated, successive, or clustered groups; it functions as qualifier or circumstantial state rather than a detached species label","analytic_root_gloss_range_en":"sparse root field associated elsewhere with camel or herd language; the local hapax-like descriptor transfers grouping and drove pressure to airborne agents, while loanword proposals remain possible background rather than controlling the parse","qac_refs":["105:3:4:1"],"root":{"arabic":"أ ب ل","transliteration":"ʾ-b-l"},"surface":{"arabic":"أَبَابِيلَ","transliteration":"abābīl"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["105:3"],"branch_refs":["root_000006/B003","root_000563/B001","root_000962/B001"],"candidate_id":"cand_ab8f894712f8f7114996","evidence_scope":"focus_ayah","hft_ref":"hft_8d3423b39c15cf3e17cb","item_id":"base_dispatched_airborne_agency","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_dispatched_airborne_agency","support_id":"sup_d5bf3c1aefa3e3bb9755"},{"anchor_refs":["105:3"],"branch_refs":["root_000006/B003","root_000563/B005","root_000962/B002"],"candidate_id":"cand_b75059b67363bfe60022","evidence_scope":"focus_ayah","hft_ref":"hft_4d52f4d4de64aecd4423","item_id":"base_pulsed_distributed_swarm","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_pulsed_distributed_swarm","support_id":"sup_3bb8eb72d603fbb2a398"},{"anchor_refs":["105:3"],"branch_refs":["root_000006/B003","root_000563/B002","root_000962/B001"],"candidate_id":"cand_9a0e4e7327fa2b496ecf","evidence_scope":"focus_ayah","hft_ref":"hft_2eb71a4b2f5deadf2d11","item_id":"base_embodied_message","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_embodied_message","support_id":"sup_30f767751a30a01b43e7"},{"anchor_refs":["105:3"],"branch_refs":["root_000006/B004","root_000563/B001","root_000962/B001"],"candidate_id":"cand_eefb4ed317c3cc5e44e9","evidence_scope":"focus_ayah","hft_ref":"hft_876a4df468b6fe6d957d","item_id":"out_light_medium_heavy_burden","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:out_light_medium_heavy_burden","support_id":"sup_8bdbc1e3ecbdfcad74d9"},{"anchor_refs":["105:3"],"branch_refs":["root_000006/B001","root_000563/B003","root_000962/B001"],"candidate_id":"cand_d85c77f21ae6775397f9","evidence_scope":"focus_ayah","hft_ref":"hft_fe0f2acbb5bbebe4a4f9","item_id":"out_airborne_herd_logic","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:out_airborne_herd_logic","support_id":"sup_630a2304256207d9379f"}],"diagnostics":[],"lane_counts":{"global":9,"macro":12,"micro":5},"packet_summary":{"ayah_count":5,"focus_ref":"105:3","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]}],"window":["105:1","105:2","105:3","105:4","105:5"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"105:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":17,"unstructured_record_count":0},"identity":{"ayah_ref":"105:3","lane":"micro","linguistic_source_ref":"105:3","surface_ref":"105:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"105:3","target_tokens":[["Ve",["105:3:1"]],["üzerlerine",["105:3:2"]],["sürü",["105:3:4"]],["sürü",["105:3:4"]],["kuşlar",["105:3:3"]],["gönderdi",["105:3:1"]]],"text":"Ve üzerlerine sürü sürü kuşlar gönderdi."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":5,"id":"s105-p01-001-005","label":"Whole surah","number":1,"refs":["105:1","105:2","105:3","105:4","105:5"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:5:derivation-and-loanword-dispute","source_type":"word_analysis","support_id":"sup_03c44a0149ca71d0443f","text":"{\"blocking_evidence\":null,\"headline\":\"derivational dispute stays as background\",\"reader_payoff\":\"The reader notices that the debated origin of the word explains why the final descriptor feels lexically strange, while local grammar still reads it through grouped arrival.\",\"reason\":\"The loanword proposal and Arabic derivation dispute are valid lexical background, but neither replaces the local qualifier or manner function.\",\"representative_source_ids\":[\"QS-ac920e0d\",\"MH-d4870ad5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:4:indefinite-collective-unspecified","source_type":"word_analysis","support_id":"sup_15f6cf0f267d71b71523","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite collective withholds species identity\",\"reader_payoff\":\"The reader notices that the wording gives an unspecified collective of flying agents, not a definite known species or a single individual flyer.\",\"reason\":\"The noun is indefinite accusative and collective, and the following descriptor can distribute that collective rather than count one bird at a time.\",\"representative_source_ids\":[\"QG-43ce4486\",\"QF-7d861d48\",\"QF-b972c6ca\",\"QF-cd1f986c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:5:wave-like-grouping","source_type":"word_analysis","support_id":"sup_20b27f088df231ef8697","text":"{\"blocking_evidence\":null,\"headline\":\"successive scattered groups control the image\",\"reader_payoff\":\"The reader sees the birds as arrivals in separated waves or clusters rather than as one undifferentiated mass.\",\"reason\":\"The CRITICAL rows consistently define the descriptor through successive groups, dispersal, and formations, and the local noun it modifies is collective.\",\"representative_source_ids\":[\"QS-13b14877\",\"QS-984bd4c0\",\"QS-cd5d77aa\",\"QF-30322def\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"105:3:3:1","source_type":"qac_morpheme","support_id":"sup_27f9463c4b7e074fa992","text":"{\"lemma_ar\":\"طَيْر\",\"morph_features\":\"STEM|POS:N|LEM:Tayor|ROOT:Tyr|MP|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"105:3:3:1\",\"qac_word_ref\":\"105:3:3\",\"root_ar\":\"ط ي ر\",\"surface_ar\":\"طَيْرًا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:5:herd-root-transfer","source_type":"word_analysis","support_id":"sup_2adca5bda88474f2c184","text":"{\"blocking_evidence\":null,\"headline\":\"herd-field pressure is transferred to airborne groups\",\"reader_payoff\":\"The reader notices a lexical reversal in which earthbound herd language from 6:144 and 88:17 sharpens the image of managed or driven airborne groups.\",\"reason\":\"The supplied root evidence for the same field points to camel contexts in 6:144 and 88:17, but the local word qualifies birds, so the herd pressure is image-transfer rather than a replacement sense.\",\"representative_source_ids\":[\"QS-3b1a0c5a\",\"QS-ee1f8a32\",\"QI-436efa4f\",\"QE-3f563263\",\"QE-7acd32cd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:4:sound-of-flight","source_type":"word_analysis","support_id":"sup_2c55ba052c9a982f191b","text":"{\"blocking_evidence\":null,\"headline\":\"sound moves from heavy onset to flight\",\"reader_payoff\":\"The reader hears a compact movement from emphatic onset into a lighter ending, matching the lexical move into airborne motion.\",\"reason\":\"The phonetic observation stays subordinate to the concrete noun and its syntactic role.\",\"representative_source_ids\":[\"QP-e96d8747\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:5:hapax-closure-weight","source_type":"word_analysis","support_id":"sup_49aa166e2fa9365fb041","text":"{\"blocking_evidence\":null,\"headline\":\"rare descriptor lands at ayah closure\",\"reader_payoff\":\"The reader leaves 105:3 with the strange grouped mode of arrival as the closing impression, not merely with the fact that birds were sent.\",\"reason\":\"The word is the final modifier and exact lexeme at ayah closure, with limited distributional support outside the local context.\",\"representative_source_ids\":[\"QI-5cbcc976\",\"QT-4160bfdd\",\"QT-ba9d9ff5\",\"QH-242594cb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:2:hostile-dispatch-frame","source_type":"word_analysis","support_id":"sup_49bb99a295e6d1eecd6a","text":"{\"blocking_evidence\":null,\"headline\":\"verb governs target and object in a hostile frame\",\"reader_payoff\":\"The reader notices that the verb does not merely say something was sent; it controls a target phrase and an explicit object, making the dispatch visibly aimed.\",\"reason\":\"The attachment evidence gives the verb an explicit direct object and a governed prepositional complement with target force.\",\"representative_source_ids\":[\"QG-24b8c8fe\",\"QG-87dcbf5d\",\"QT-b6df822e\",\"QY-613f3c9b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:2:unusual-bird-dispatch-pairing","source_type":"word_analysis","support_id":"sup_4a64ea0e861bad736a59","text":"{\"blocking_evidence\":null,\"headline\":\"common sending root receives unusual flying object\",\"reader_payoff\":\"The reader notices a familiar sending vocabulary redirected into a rare pairing with flying agents, including a contrast with the bird-sign context of 3:49.\",\"reason\":\"The contextual evidence marks the root as common but the object pairing with flying creatures as narrow; the 3:49 contrast remains useful without controlling the local parse.\",\"representative_source_ids\":[\"QI-30d1fe72\",\"QI-a4c0087b\",\"QI-fbf0bedd\",\"QE-6462858a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:5:sound-and-boundary-force","source_type":"word_analysis","support_id":"sup_5d578ed484ff7f9825b7","text":"{\"blocking_evidence\":null,\"headline\":\"pulsing sound matches multiplied arrivals\",\"reader_payoff\":\"The reader hears repeated stop-release pulses at the close, reinforcing the sense of multiplied wave-like arrivals.\",\"reason\":\"The sound claim supports the already established grouped-arrival meaning and remains tied to the closing surface form.\",\"representative_source_ids\":[\"QP-00d62db8\",\"QP-d2f1c00a\",\"QY-f0e80fae\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:2","source_type":"word_analysis","support_id":"sup_61cd42debbcc4a5987ef","text":"{\"gloss_range\":\"completed causative dispatch or release of an explicit airborne object against a marked target; message-bearing associations are backgrounded rather than selected\",\"prose\":\"{{ar:أَرْسَلَ}} ({{tr:arsala}}) is the first lexical action of the ayah, and its perfect Form IV shape reports the dispatch as a completed act caused by the continued divine subject. That actual form keeps agency with the sender rather than making the birds request or initiate their own dispatch. The verb governs both {{ar:عَلَيْهِمْ}} ({{tr:ʿalayhim}}) and {{ar:طَيْرًا}} ({{tr:ṭayran}}), so the scene is not neutral sending-to: the target is marked first, then the instrument is named. The {{ar:ر س ل}} ({{tr:r-s-l}}) field can carry messenger and message associations, but here the object is not speech or a human envoy; the familiar sending frame is redirected into released airborne agents. Its hamzated onset makes the dispatch verb stand out exactly where the joined boundary becomes action. The word also turns the abstract outcome of 105:2 into operational deployment, and it leaves the sent object waiting for its action in 105:4.\",\"root_display\":\"{{ar:ر س ل}} ({{tr:r-s-l}})\",\"root_gloss_range\":\"broad range around sending forth, dispatch, release, messengers and messages, easy flow, and successive groups; the local Form IV frame selects caused hostile deployment\",\"surface_display\":\"{{ar:أَرْسَلَ}} ({{tr:arsala}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:1","source_type":"word_analysis","support_id":"sup_66297e314055abda77a8","text":"{\"gloss_range\":\"coordinating ayah-opening connector that continues the prior divine-action report while opening the concrete dispatch scene without fixing exact timing\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) keeps the new report joined to the preceding verdict while letting this ayah begin a fresh operational scene. It does not force a later-than relation the way a sharper sequencing particle would; the sending can be heard as coordinated with, or as the means by which, the prior nullification becomes visible. Because the connector is fused directly to the dispatch verb, the boundary-link and the action arrive in one onset: the listener moves from the acknowledged verdict of 105:2 into the concrete mechanism of 105:3 without a hard break.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:5","source_type":"word_analysis","support_id":"sup_67dd4310aee8f1c459ab","text":"{\"gloss_range\":\"rare final descriptor for the sent flying agents as separated, successive, or clustered groups; it functions as qualifier or circumstantial state rather than a detached species label\",\"prose\":\"{{ar:أَبَابِيلَ}} ({{tr:abābīl}}) closes the ayah by turning the collective {{ar:طَيْرًا}} ({{tr:ṭayran}}) into visible formation. The word can be read as a descriptor or as a circumstantial state, but either way it remains tied to the birds: it names their grouped manner of arrival, not an unrelated noun. Its force is not just many birds; the supplied evidence presses successive groups and scattered clusters together, so the image is wave-like arrival from separated formations. The sparse {{ar:أ ب ل}} ({{tr:ʾ-b-l}}) field and the camel-herd echoes in 6:144 and 88:17 make the airborne grouping feel lexically exceptional, while the Ethiopic loan proposal remains a possible background explanation rather than a local replacement for the grouping sense. As the final word, its broken-plural-like shape, repeated bilabial pulses, and hapax weight make the strangeness of the divine counter-force land at the ayah boundary, ready for the distributed stones named in 105:4.\",\"root_display\":\"{{ar:أ ب ل}} ({{tr:ʾ-b-l}})\",\"root_gloss_range\":\"sparse root field associated elsewhere with camel or herd language; the local hapax-like descriptor transfers grouping and drove pressure to airborne agents, while loanword proposals remain possible background rather than controlling the parse\",\"surface_display\":\"{{ar:أَبَابِيلَ}} ({{tr:abābīl}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:4:rare-dispatch-flight-field","source_type":"word_analysis","support_id":"sup_6a123d49f70418e4429e","text":"{\"blocking_evidence\":null,\"headline\":\"dispatch and flying form a marked pair\",\"reader_payoff\":\"The reader notices that the familiar flight field is specialized into punitive dispatch, with 3:49 providing a sign-context contrast.\",\"reason\":\"The supplied co-occurrence evidence makes the dispatch-plus-flying-creatures relation narrow, and the 3:49 contrast does not override the local hostile frame.\",\"representative_source_ids\":[\"QI-3028aebf\",\"QI-9ccf4839\",\"QE-79739b4d\",\"QY-a589029d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:1:coordination-without-fixed-timing","source_type":"word_analysis","support_id":"sup_72250032122b8f94d1e8","text":"{\"blocking_evidence\":null,\"headline\":\"coordination continues the prior action without fixing timing\",\"reader_payoff\":\"The reader notices that the sending belongs to the same divine-action chain as 105:2, while the connector does not require a precise later sequence.\",\"reason\":\"The local particle is a coordinating conjunction at the ayah opening; the circumstantial or means-like force is possible as a reading of the coordination, but the grammar does not force it as the only relation.\",\"representative_source_ids\":[\"QG-299398ea\",\"MG-d48f271c\",\"QS-15d818ff\",\"QB-6b0d91bd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:3","source_type":"word_analysis","support_id":"sup_7930a5b8d6a7cf438134","text":"{\"gloss_range\":\"prepositional target phrase meaning upon or against them, with a definite suffix referring back to the elephant people and marking them as exposed recipients of hostile dispatch\",\"prose\":\"{{ar:عَلَيْهِمْ}} ({{tr:ʿalayhim}}) gives the dispatch its target before the object is named. The suffix points back to the elephant people of 105:1 and continues the third-person plural chain from 105:2, but it does so without renaming them; the known planners have become the governed target. The preposition keeps both vertical and adversative force active: the birds are sent upon them and against them, not merely to them as recipients. Its fused preposition-suffix form and final nasal close make the target feel fixed before {{ar:طَيْرًا}} ({{tr:ṭayran}}) opens the next beat with the instrument of that exposure.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:عَلَيْهِمْ}} ({{tr:ʿalayhim}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:5:forward-projectile-arc","source_type":"word_analysis","support_id":"sup_82519bdf18c272e1c6c3","text":"{\"blocking_evidence\":null,\"headline\":\"flock formation anticipates distributed stones\",\"reader_payoff\":\"The reader notices that grouped aerial formation prepares for the distributed projectile action named in 105:4.\",\"reason\":\"The boundary evidence coherently connects the rare closing descriptor of 105:3 with the stones and throwing action of 105:4.\",\"representative_source_ids\":[\"QB-3184f72a\",\"QB-b297d794\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:1:fused-sound-boundary","source_type":"word_analysis","support_id":"sup_828deb1b352c816bf856","text":"{\"blocking_evidence\":null,\"headline\":\"fused onset joins boundary and action\",\"reader_payoff\":\"The reader hears the continuation particle attached to the action onset, so the new report starts under a joined boundary rather than after an isolated pause.\",\"reason\":\"The surface form places the conjunction directly before the hamzated verb, making the linked start visible and audible without changing the syntax.\",\"representative_source_ids\":[\"QF-f43d16ff\",\"QP-b252e89a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:4:flight-and-fate-pressure","source_type":"word_analysis","support_id":"sup_8c4d99649f47a1f42922","text":"{\"blocking_evidence\":null,\"headline\":\"fate pressure shadows concrete flying agents\",\"reader_payoff\":\"The reader notices a secondary portent or fate edge around the flying agents, while the local noun remains concrete rather than abstract destiny.\",\"reason\":\"The root family includes omen and fate associations, but the local surface is a concrete noun serving as the object of dispatch.\",\"representative_source_ids\":[\"QS-26523603\",\"QS-e7fbcf74\",\"QS-f9a86c20\",\"MS-9938ab65\",\"QI-81401444\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:2:perfect-divine-causative","source_type":"word_analysis","support_id":"sup_9f369debb2910b9f21eb","text":"{\"blocking_evidence\":null,\"headline\":\"completed Form IV dispatch keeps divine agency\",\"reader_payoff\":\"The reader notices that the form presents the sending as completed narrative fact and as caused by the same divine subject carried from 105:1.\",\"reason\":\"The local form is a third-person masculine singular perfect Form IV verb, with an implicit subject supplied by the discourse link to 105:1.\",\"representative_source_ids\":[\"QG-57c9c7a2\",\"QG-eb45b0be\",\"QF-4f673f8d\",\"QF-5e9ce7ad\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:3:case-role-reversal","source_type":"word_analysis","support_id":"sup_aaaae9d59a8e1d7bdf3f","text":"{\"blocking_evidence\":null,\"headline\":\"schemers become governed patients\",\"reader_payoff\":\"The reader notices the same group move from owning a scheme in 105:2 to being grammatically governed under hostile force in 105:3.\",\"reason\":\"The suffix is governed by the preposition here, while the prior discourse made the group possessors of the scheme.\",\"representative_source_ids\":[\"QG-fed42665\",\"QB-6c2ae560\",\"QB-bd48b66b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:4:direct-object-instrument","source_type":"word_analysis","support_id":"sup_b22156df965c7a730253","text":"{\"blocking_evidence\":null,\"headline\":\"flying agents are the explicit object\",\"reader_payoff\":\"The reader notices that the birds are introduced as the dispatched instrument after the target has already been fixed.\",\"reason\":\"The noun is accusative and is syntactically forced as the direct object of the dispatch verb.\",\"representative_source_ids\":[\"QG-39b66fae\",\"QT-2e27ecf5\",\"QT-be7566dc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:4:descriptor-agreement","source_type":"word_analysis","support_id":"sup_bd2f5b6c0ae7508dbb18","text":"{\"blocking_evidence\":null,\"headline\":\"following descriptor is locked to the birds\",\"reader_payoff\":\"The reader notices that the unusual final word qualifies the sent flying agents rather than floating free of them.\",\"reason\":\"The supplied syntax allows the final word as either adjective or circumstantial state tied to this accusative noun.\",\"representative_source_ids\":[\"QG-41736b1b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"105:3:4:1","source_type":"qac_morpheme","support_id":"sup_bdcff7df698bae73fe56","text":"{\"lemma_ar\":\"أَبَابِيل\",\"morph_features\":\"STEM|POS:ADJ|LEM:>abaAbiyl|ROOT:Abl|MP|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"105:3:4:1\",\"qac_word_ref\":\"105:3:4\",\"root_ar\":\"ء ب ل\",\"surface_ar\":\"أَبَابِيلَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:3:fused-position-before-object","source_type":"word_analysis","support_id":"sup_be22bb9ef684ce471906","text":"{\"blocking_evidence\":null,\"headline\":\"target is sealed before the instrument appears\",\"reader_payoff\":\"The reader feels the target fixed and closed before the indefinite flying object opens the next beat.\",\"reason\":\"The preposition and suffix are fused in one surface form, and the phrase stands between the verb and the direct object.\",\"representative_source_ids\":[\"QF-560d8898\",\"QT-492f1d14\",\"QP-e1f6b308\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:2:boundary-execution-arc","source_type":"word_analysis","support_id":"sup_c5c73cd9e5b11b3e99d9","text":"{\"blocking_evidence\":null,\"headline\":\"abstract verdict becomes concrete deployment\",\"reader_payoff\":\"The reader notices that 105:3 begins to unpack the action implied by 105:1 and the verdict of 105:2 by naming the mechanism of execution.\",\"reason\":\"The verb launches the verbal clause after the opening connector and anticipates the thrown action supplied in 105:4.\",\"representative_source_ids\":[\"MI-c0294124\",\"QT-7d5c7498\",\"QE-09a9df21\",\"QB-39c2a6a6\",\"QB-88db0c4c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:4","source_type":"word_analysis","support_id":"sup_c886a986003be6d42038","text":"{\"gloss_range\":\"indefinite collective flying agents, the explicit object of dispatch, left taxonomically unspecified and prepared for distribution by the following descriptor and action in 105:4\",\"prose\":\"{{ar:طَيْرًا}} ({{tr:ṭayran}}) is the explicit object of {{ar:أَرْسَلَ}} ({{tr:arsala}}): the thing sent, not a background circumstance or an independent actor yet. Its indefinite collective form withholds species identity while still allowing a mass of flying agents, so the next word can distribute that mass into formations. The {{ar:ط ي ر}} ({{tr:ṭ-y-r}}) root keeps literal flight active, and the sound contour moves from an emphatic heavy onset into a lighter flowing ending, matching the lexical motion into flight. The local frame bends that flight downward against the target and 105:4 will make the same referent the thrower. Omen or fate associations can shadow the noun, but they do not replace the concrete flying agents selected here. The rare pairing with the dispatch root, including the contrast with the bird-sign context of 3:49, makes the birds identifiable by function and sequence more than by taxonomy.\",\"root_display\":\"{{ar:ط ي ر}} ({{tr:ṭ-y-r}})\",\"root_gloss_range\":\"range around flying, birds or flying creatures, movement through the air, and omen or fate associations; the local noun selects concrete flying agents while secondary fate pressure remains only a shadow\",\"surface_display\":\"{{ar:طَيْرًا}} ({{tr:ṭayran}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:5:marked-plural-not-species","source_type":"word_analysis","support_id":"sup_d2c778bb66ba84dc6dc9","text":"{\"blocking_evidence\":null,\"headline\":\"marked form avoids a settled species label\",\"reader_payoff\":\"The reader notices that the form foregrounds grouped multiplicity and non-default shape more than a countable known species.\",\"reason\":\"The word is indefinite, has a disputed or absent singular in the supplied evidence, and V4 has no resolved same-form corpus support for this root.\",\"representative_source_ids\":[\"QG-86b3f079\",\"QF-64c9f39a\",\"QF-b3a717ad\",\"QI-51cfb3d8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"105:3:1:2","source_type":"qac_morpheme","support_id":"sup_dcf534a2c45bbc34a176","text":"{\"lemma_ar\":\"أَرْسَلَ\",\"morph_features\":\"STEM|POS:V|PERF|(IV)|LEM:>arosala|ROOT:rsl|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"105:3:1:2\",\"qac_word_ref\":\"105:3:1\",\"root_ar\":\"ر س ل\",\"surface_ar\":\"أَرْسَلَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:4:flight-downward-agent-arc","source_type":"word_analysis","support_id":"sup_df3e945675ba5a9d2b10","text":"{\"blocking_evidence\":null,\"headline\":\"literal flight becomes downward hostile action\",\"reader_payoff\":\"The reader notices the role shift: what is first the object of sending becomes the acting force whose throwing is named in 105:4.\",\"reason\":\"The local object is sent against the target, and the immediate next ayah supplies the throwing action for the same referent.\",\"representative_source_ids\":[\"QS-1940991d\",\"QS-99a8234a\",\"QE-1abdfcd0\",\"QB-0d761bf0\",\"QB-3fc1df95\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:3:known-pronoun-target","source_type":"word_analysis","support_id":"sup_e069f7f8817fdbac6eb0","text":"{\"blocking_evidence\":null,\"headline\":\"attached suffix identifies the known target\",\"reader_payoff\":\"The reader notices that the target is already familiar from 105:1 and 105:2, so the clause can move quickly toward the instrument.\",\"reason\":\"The cross-reference evidence links the suffix to the elephant people from 105:1 and the prior plural chain.\",\"representative_source_ids\":[\"QG-3e9c48d8\",\"QG-91f383bc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:1:resumptive-operational-launch","source_type":"word_analysis","support_id":"sup_ec5dc6aff3031276f2c1","text":"{\"blocking_evidence\":null,\"headline\":\"opening connector launches the concrete report\",\"reader_payoff\":\"The reader notices the mode shift from the prior question-frame into declarative narration while the discourse remains joined.\",\"reason\":\"The particle stands first in the ayah and connects the verbal clause to the previous ayah while the following verb begins the narrated mechanism.\",\"representative_source_ids\":[\"QS-78799bac\",\"QT-519721c5\",\"QT-721304ba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:5:qualifier-or-manner","source_type":"word_analysis","support_id":"sup_f019ff055586c5b1ee8b","text":"{\"blocking_evidence\":null,\"headline\":\"final word qualifies the sent birds\",\"reader_payoff\":\"The reader notices that the final word is grammatically tied to the sent birds as their qualifier or arrival-state, not as a detached label.\",\"reason\":\"The supplied syntax allows adjective or circumstantial readings, and both attach the final word to the accusative flying agents.\",\"representative_source_ids\":[\"QG-5b656edf\",\"QG-8d4dd555\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:2:hamza-dispatch-onset","source_type":"word_analysis","support_id":"sup_f0a99569fdde3d3f68ba","text":"{\"blocking_evidence\":null,\"headline\":\"hamza onset marks decisive action\",\"reader_payoff\":\"The reader hears the dispatch verb stand out at the point where the joined boundary becomes action.\",\"reason\":\"The sound observation follows the visible hamzated onset and supports the action-launch effect without adding a separate lexical sense.\",\"representative_source_ids\":[\"QP-483f01b6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:2:form-bound-agency-limit","source_type":"word_analysis","support_id":"sup_f47e783d215c927d531e","text":"{\"blocking_evidence\":null,\"headline\":\"actual form blocks reflexive request framing\",\"reader_payoff\":\"The reader notices that agency remains with the sender; the birds are not requesting or initiating dispatch for themselves.\",\"reason\":\"The aligned local surface is Form IV, so the causative dispatch form is the operative morphology.\",\"representative_source_ids\":[\"QF-7c729ef9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:2:release-not-message","source_type":"word_analysis","support_id":"sup_fa0c0042b4ede0b78aaf","text":"{\"blocking_evidence\":null,\"headline\":\"release pressure survives while message sense is not selected\",\"reader_payoff\":\"The reader feels the dispatch as release or unleashing toward a target, while the local object keeps messenger-message meanings in the background.\",\"reason\":\"The root has accepted branches for dispatch, release, and messenger-message meanings, but the local object is flying agents rather than a messenger or message bearer.\",\"representative_source_ids\":[\"QS-2c810d68\",\"QS-71930f17\",\"QS-f06a5e24\",\"MF-0d810c70\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:3:3:upon-against-targeting","source_type":"word_analysis","support_id":"sup_fa3c202b92369edf9bb0","text":"{\"blocking_evidence\":null,\"headline\":\"preposition gives descent and hostility\",\"reader_payoff\":\"The reader notices that the preposition gives the dispatch both downward exposure and adversative aim, not neutral delivery.\",\"reason\":\"The phrase is the governed complement of the dispatch verb and the supplied support explicitly warns against flattening it to a merely spatial or neutral recipient relation.\",\"representative_source_ids\":[\"QG-92262076\",\"MG-f4c88990\",\"QS-d02486e7\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ","ayah_ref":"105:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000006/B003","root_000563/B001","root_000962/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000563","role":"Release and dispatch supply the initiating transfer from sender to target.","root":"ر س ل","source_ref":"105:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000962","role":"Airborne lightness supplies the mobile medium of the intervention.","root":"ط ي ر","source_ref":"105:3","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000006","role":"Separate or successive bands organize the airborne collective into deployable units.","root":"ء ب ل","source_ref":"105:3","source_word_indices":["4"]}],"changed_reading":{"after":"He released an airborne agency against them in organized bands, so deployment geometry belongs to the act itself.","before":"He simply sent birds against them."},"confidence":"strong","focus_anchor":"The causative dispatch verb, the adversarial/overhead relation in عَلَيْهِمْ, and the collective bird expression make agency, vector, and formation visible inside 105:3.","mechanism":"A sender releases a light airborne collective against a target, while the banded modifier prevents the birds from reading as an undifferentiated mass.","model_id":"base_dispatched_airborne_agency"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_dispatched_airborne_agency","source_type":"hft","support_id":"sup_d5bf3c1aefa3e3bb9755","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ","ayah_ref":"105:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000006/B003","root_000563/B005","root_000962/B002"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000563","role":"Successive batches give the dispatch a pulsed temporal structure.","root":"ر س ل","source_ref":"105:3","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000962","role":"Light scattering gives each pulse a spreading spatial behavior.","root":"ط ي ر","source_ref":"105:3","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000006","role":"Scattered and successive groups couple the temporal and spatial readings.","root":"ء ب ل","source_ref":"105:3","source_word_indices":["4"]}],"changed_reading":{"after":"The intervention unfolds as repeated, distributed swarm pulses whose sequence and spread are both operative.","before":"A single flock arrives as one event."},"confidence":"medium","focus_anchor":"The focus verse combines a dispatch root that can mark batch succession, a flight root that can mark scattering, and an adjective of separate or successive groups.","mechanism":"Temporal succession and spatial dispersion coexist: fresh bands can arrive one after another while each band spreads, producing resilient coverage rather than one concentrated flock.","model_id":"base_pulsed_distributed_swarm"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_pulsed_distributed_swarm","source_type":"hft","support_id":"sup_3bb8eb72d603fbb2a398","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ","ayah_ref":"105:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000006/B003","root_000563/B002","root_000962/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000563","role":"Messenger and carried-message imagery opens a communicative dimension within dispatch.","root":"ر س ل","source_ref":"105:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000962","role":"Visible airborne movement gives the communication an embodied carrier.","root":"ط ي ر","source_ref":"105:3","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000006","role":"Ordered bands make the carried sign repeatable and publicly patterned.","root":"ء ب ل","source_ref":"105:3","source_word_indices":["4"]}],"changed_reading":{"after":"The birds are instruments whose patterned arrival also bears a message of the sender's intervention.","before":"The birds are only instruments sent to act."},"confidence":"exploratory","focus_anchor":"The same focus verb that dispatches forces also carries messenger/message imagery, and its object is a conspicuously patterned airborne collective.","mechanism":"The birds can remain physical agents while their ordered arrival also functions as a carried communication: the intervention makes the sender's agency legible through embodied messengers.","model_id":"base_embodied_message"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_embodied_message","source_type":"hft","support_id":"sup_30f767751a30a01b43e7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ","ayah_ref":"105:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000006/B004","root_000563/B001","root_000962/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000563","role":"Dispatch transfers the paradoxical force onto the target.","root":"ر س ل","source_ref":"105:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000962","role":"Flight supplies physical lightness and mobility.","root":"ط ي ر","source_ref":"105:3","source_word_indices":["3"]},{"branch_id":"B004","mapped_root_id":"root_000006","role":"Heaviness, liability, and oppressive burden supply the effect imposed by the light medium.","root":"ء ب ل","source_ref":"105:3","source_word_indices":["4"]}],"changed_reading":{"after":"The verse stages a reversal in which what is physically light becomes an oppressive weight upon the target.","before":"Light birds are unlikely carriers of overwhelming force."},"confidence":"medium","containment":"The collision is surprising because flight contributes lightness while a distant branch of the banding adjective contributes oppressive weight or liability. It remains anchored in two explicit focus inventories and in عَلَيْهِمْ, but downstream prose should present it as a paradoxical force-image, not as an alternate lexical gloss for the adjective.","focus_anchor":"The focus places a light airborne collective over/against the target and qualifies it with a root whose inventory includes heaviness and burden.","outlier_id":"out_light_medium_heavy_burden"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:out_light_medium_heavy_burden","source_type":"hft","support_id":"sup_8bdbc1e3ecbdfcad74d9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ","ayah_ref":"105:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000006/B001","root_000563/B003","root_000962/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000563","role":"Smooth-moving animals supply coordinated, easy collective motion.","root":"ر س ل","source_ref":"105:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000962","role":"Bird flight relocates that collective-motion analogy into the air.","root":"ط ي ر","source_ref":"105:3","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000006","role":"Herd abundance and skilled tending supply convoy-like organization.","root":"ء ب ل","source_ref":"105:3","source_word_indices":["4"]}],"changed_reading":{"after":"The airborne bands can be imagined as a herded convoy in the sky, released with the coordinated logic of tended animal groups.","before":"The birds form exceptional but otherwise ordinary flocks."},"confidence":"exploratory","containment":"This is surprising because camel-herd and smooth-animal branches are transferred into an avian scene. It remains focus-anchored through the mapped inventory of أبابيل and the dispatch verb, but it should be rendered only as an organizational analogy—birds moving with herd or convoy logic—not as an identification of the birds with camels.","focus_anchor":"All three focus roots converge on mobile animals organized and released as collectives.","outlier_id":"out_airborne_herd_logic"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:out_airborne_herd_logic","source_type":"hft","support_id":"sup_630a2304256207d9379f","trust":"legacy_unbound"}]}
</lane_packet_json>
