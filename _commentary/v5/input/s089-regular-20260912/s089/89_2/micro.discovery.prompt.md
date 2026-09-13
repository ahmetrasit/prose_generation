# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **89:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "89:2",
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
{"branch_registry":[{"boundary":"Dal sayı adlarıyla sınırlıdır; onda bir payı, vergi almayı veya akraba topluluğunu kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001016/B001","candidate_links":[{"candidate_id":"cand_46c2cc47efe07d2c117e","lane":"micro"},{"candidate_id":"cand_90f1d9915b840660e983","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"on ve yirmi sayı adları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"On sayısı, sayılan adın dilbilgisel cinsiyetine göre iki ayrı biçimle kullanılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı sayı söz varlığı yirmi adını ve on bir bileşiğini de içerir."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Onun cinsiyete bağlı biçimleriyle yirmiyi ve on bir bileşiğini birlikte anlatan üst düzey karşılıktır.","boundary_detail":"Dal sayı adlarıyla sınırlıdır; onda bir payı, vergi almayı veya akraba topluluğunu kapsamaz.","branch_image_ar":"عدد العشرة","concept_gloss":"on ve yirmi sayı adları","contextual_glosses":[{"applicability":"Tek tek sayı biçimlerinin metin içinde çevrilmesi gerektiğinde bağlama göre bu doğal Türkçe sayı adlarından biri seçilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Her sayı biçiminin bağlamdaki sayısal değerini korur."},"facet_ids":["F001","F002"],"text":"on; yirmi; on bir","usage_role":"contextual"}],"definition":"On sayısının eril ve dişil adlarla kullanılan biçimlerini, yirmi sayısını ve on bir bileşiğini kapsayan sayı adları alanıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"On sayısı, sayılan adın dilbilgisel cinsiyetine göre iki ayrı biçimle kullanılır."},{"facet_id":"F002","role":"extension","statement":"Aynı sayı söz varlığı yirmi adını ve on bir bileşiğini de içerir."}],"identity_rationale":"Kaynak ifadesi, on sayısının eril ve dişil adlarla kullanılan ayrı biçimlerini, yirmiyi ve on bir bileşiğini aynı sayı adları alanında toplar. Bu çerçeve sayı değerini, dilbilgisel kullanım ayrımını ve bileşik biçimi birlikte korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"eril adlarla kullanılan on sayısı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"dişil adlarla kullanılan on sayısı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yirmi sayısı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"on bir sayısı"}],"lexicalization_note":"Tanım yalın sayı biçimleriyle on bir bileşiğini ayırır; bileşik kullanım yalın kökün bütün anlamı sayılmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; sayı alanındaki en açık karşılaştırma farklı bir temel sayı dalıyla verildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortak alan sayı söz varlığıdır; ancak sayısal değerler ve türeyen biçim dizileri farklı olduğu için birbirlerinin yerine kullanılamazlar.","focus_only":"On, yirmi ve on bir çevresindeki sayı biçimlerini kapsar.","gloss":"üç sayısı","neighbor_only":"Üç sayısını ve ondan türeyen dağıtma, sıra ve büyük sayı biçimlerini kapsar.","neighbor_ref":"root_000203/B001","relation_type":"same_field","shared_zone":"Her iki dal da temel sayı adlarını ve bunların dilbilgisel biçimlerini konu edinir."}],"source_phrase_ar":"العشرة والعشر في المؤنث (maqayis); العشر عدد المؤنث والعشرة عدد المذكر (ayn;tahdhib); عشرة رجال وعشر نسوة (sihah); العشرة والعشر والعشرون معروفة (mufradat)","source_summary":"Kaynaklar on sayısının eril ve dişil kullanımlarını ayırır, yirmiyi aynı sayı dizisinde anar ve on bir bileşiğini örnekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"العشرة والعشرون وما جاورهما من ألفاظ العدد للمذكر والمؤنث","what_is_not_ar":"ليس أخذ العشر من المال ولا العشيرة"},"support_links":["sup_44dddc7785b037632ef0","sup_f2a570e4fb54e4c414db"]},{"boundary":"Anlam, dokuzu ona tamamlama işlemiyle sınırlıdır; yalnızca on sayısını söylemek veya maldan pay almak değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001016/B002","candidate_links":[{"candidate_id":"cand_809bd424b88544b7c33f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"dokuzu ona tamamlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dokuz kişilik bir gruba katılan kişi grubun onuncusu olur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dokuz olan bir toplama bir öğe eklenerek toplam on yapılır."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin onuncu olması ile bir ekleme sonucunda toplamın ona çıkması birlikte kastedildiğinde kullanılır.","boundary_detail":"Anlam, dokuzu ona tamamlama işlemiyle sınırlıdır; yalnızca on sayısını söylemek veya maldan pay almak değildir.","branch_image_ar":"تمام التسعة بعاشر","concept_gloss":"dokuzu ona tamamlama","contextual_glosses":[{"applicability":"Dokuz kişilik bir gruba katılan kişinin yeni gruptaki konumunu anlatan cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişi dışındaki öğeleri bir eklemeyle ona tamamlama kapsamını vermez.","preserves":"Katılan kişinin grubun onuncu üyesi olması sonucunu korur."},"facet_ids":["F001"],"text":"onuncuları olmak","usage_role":"contextual"},{"applicability":"Dokuz kişiye veya öğeye bir tane daha ekleyerek toplamı on yapma bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dokuzdan ona geçiren ekleme işlemini ve sonucu korur."},"facet_ids":["F001","F002"],"text":"ona tamamlamak","usage_role":"contextual"}],"definition":"Dokuz kişilik ya da dokuz öğelik bir kümeye bir kişi veya öğe ekleyip toplamı ona tamamlamak; eklenen kişi bakımından da grubun onuncusu olmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dokuz kişilik bir gruba katılan kişi grubun onuncusu olur."},{"facet_id":"F002","role":"core","statement":"Dokuz olan bir toplama bir öğe eklenerek toplam on yapılır."}],"identity_rationale":"Kaynak ifadesinin çekirdeği, dokuz kişilik veya dokuz öğelik bir kümeye bir kişi ya da öğe ekleyerek toplamı ona çıkarma ve eklenen kişinin onuncu olmasıdır. Verilen dal çerçevesi bu işlem ile katılımcı değişimini doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"dokuz kişiyi ona tamamlayan onuncu kişi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir topluluğun onuncu kişisi olmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"dokuz kişiyi veya şeyi bir ekleyerek ona tamamlamak"}],"lexicalization_note":"Tanım, onuncu kişi olan birimi ve dokuzu ona çıkaran yapıları ayrı tutar; kalıp kullanımlar yalın anlama genellenmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; en yararlı sınır karşılaştırması aynı işlemi dokuz sayısında yapan dal ile kuruldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İşlem yapısı aynıdır, fakat başlangıç ve sonuç sayıları farklıdır: odak dal dokuzdan ona, komşu dal sekizden dokuza geçer.","focus_only":"Dokuz olan kümeyi bir eklemeyle ona tamamlar.","gloss":"sekizi dokuza tamamlama","neighbor_only":"Sekiz olan kümeyi bir eklemeyle dokuza tamamlar.","neighbor_ref":"root_000181/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda bir kişi veya öğe eklenerek grup bir sonraki sayıya tamamlanır."}],"source_phrase_ar":"عشرت القوم إذا صرت عاشرهم (maqayis;ayn;tahdhib); كانوا تسعة فتموا بي عشرة (maqayis;ayn); أعشر القوم صاروا عشرة (sihah); عشرتهم صيرت مالهم عشرة (mufradat)","source_summary":"Kaynaklar hem kişinin dokuz kişilik bir gruba katılıp onuncu olmasını hem de dokuz öğeyi bir eklemeyle ona tamamlamayı bildirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"صيرورة المرء عاشر القوم وإتمام التسعة بواحد حتى تصير عشرة","what_is_not_ar":"ليس العشر المأخوذ من المال"},"support_links":["sup_5d9251092f03fba7b9dd"]},{"boundary":"Bu dal yalnızca bütünün on eşit parçasından biridir; herhangi bir parça veya on öğelik küme değildir.","branch_kind":"bare","branch_ref":"root_001016/B003","candidate_links":[{"candidate_id":"cand_40afa86f1401f728fb8e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"onda bir","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bütün on eşit parçaya ayrılır ve anlam bu parçalardan tek birini gösterir."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bütünün on eşit bölümünden tek bir bölümü gösteren kesir karşılığıdır.","boundary_detail":"Bu dal yalnızca bütünün on eşit parçasından biridir; herhangi bir parça veya on öğelik küme değildir.","branch_image_ar":"جزء من عشرة","concept_gloss":"onda bir","contextual_glosses":[{"applicability":"Kesir teriminin açık bir anlatımla verilmesi gereken bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bölme sayısını, parçaların eşitliğini ve tek parçayı korur."},"facet_ids":["F001"],"text":"on eşit parçadan biri","usage_role":"explanatory"}],"definition":"Bir bütünün on eşit parçaya ayrılmasıyla elde edilen parçalardan biridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bütün on eşit parçaya ayrılır ve anlam bu parçalardan tek birini gösterir."}],"identity_rationale":"Kaynak ifadesi bütünü on eşit parçaya bölünmüş kabul eder ve bu parçalardan tek birini gösterir. Dal çerçevesi payın oranını açıkça korur ve onu benzer sesli topluluk ya da bitki anlamlarından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"onda bir"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"onda bir"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir şeyin onda biri"}],"lexicalization_note":"Tanım yalın kesir anlamını verir ve vergi alma gibi yalnızca belirli yapılarda görülen eylemleri bu dala katmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; en yakın karışma olasılığı aynı yapıda farklı payda taşıyan kesir dalıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kesir yapısı ortaktır, ancak paydalar farklıdır; odak dal onda biri, komşu dal dokuzda biri bildirir.","focus_only":"Bütünü on eşit parçaya bölerek bir parçayı gösterir.","gloss":"dokuzda bir","neighbor_only":"Bütünü dokuz eşit parçaya bölerek bir parçayı gösterir.","neighbor_ref":"root_000181/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da eşit bölümlenmiş bir bütünün tek parçasını gösteren kesir anlamındadır."}],"source_phrase_ar":"العشر جزء من الأجزاء العشرة وهو العشير والمعشار (maqayis); العشر جزء من عشرة أجزاء وهو العشير والمعشار (ayn); معشار الشيء عشره (sihah;mufradat); العشير والعشر واحد (tahdhib)","source_summary":"Kaynaklar farklı sözcük biçimlerini aynı kesir değerinde birleştirir: bütünün on eşit bölümünden bir bölüm.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"العشر والعشير والمعشار بمعنى جزء واحد من عشرة","what_is_not_ar":"ليس جماعة العشيرة ولا العشر الشجر"},"support_links":["sup_be953e6fe08f22a2b8a8"]},{"boundary":"Anlam maldan onda birlik pay alma ile sınırlıdır; dokuzu ona tamamlama veya genel mal toplama değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001016/B004","candidate_links":[{"candidate_id":"cand_40afa86f1401f728fb8e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"maldan onda bir alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Malların onda birlik bölümü sahiplerinden alınır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu onda birlik payı alan kişi için özel bir görevli adı kullanılır."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem alınan payın oranını hem de mal sahibi ile alan kişi arasındaki işlemi gösteren genel karşılıktır.","boundary_detail":"Anlam maldan onda birlik pay alma ile sınırlıdır; dokuzu ona tamamlama veya genel mal toplama değildir.","branch_image_ar":"أخذ العشر من المال","concept_gloss":"maldan onda bir alma","contextual_glosses":[{"applicability":"Eylemin doğrudan bir topluluğun malına yöneldiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mal sahiplerini, alınan onda birlik payı ve alma eylemini korur."},"facet_ids":["F001"],"text":"mallarının onda birini almak","usage_role":"contextual"}],"definition":"Bir kişinin ya da topluluğun mallarından onda birlik payı almak ve bu payı alan görevliyi adlandırmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Malların onda birlik bölümü sahiplerinden alınır."},{"facet_id":"F002","role":"associated_use","statement":"Bu onda birlik payı alan kişi için özel bir görevli adı kullanılır."}],"identity_rationale":"Kaynak ifadesi, bir topluluğun mallarından onda birlik payı alma eylemini ve bu işi yapan kişiyi birlikte gösterir. Dal çerçevesi eylemi, alınan oranı ve görevliyi doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"mallarının onda birini almak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"mallardan onda bir alan görevli"}],"lexicalization_note":"Tanım, mal nesnesiyle kurulan alma yapısını ve bu işlemi yapan adını ayırır; bunlar yalın sayı anlamına genellenmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; oran dışındaki yapısı aynı olan dokuzda birlik alma dalı en keskin karşılaştırmayı sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Katılımcılar ve alma işlemi örtüşür, fakat alınan oran farklıdır: odakta onda bir, komşuda dokuzda bir.","focus_only":"Maldan onda birlik pay alma eylemini bildirir.","gloss":"maldan dokuzda bir alma","neighbor_only":"Maldan dokuzda birlik pay alma eylemini bildirir.","neighbor_ref":"root_000181/B003","relation_type":"near_synonym","shared_zone":"Her iki dalda bir topluluğun malından belirli bir kesir payı alınır."}],"source_phrase_ar":"عشرت القوم إذا أخذت عشر أموالهم (maqayis); عشرتهم تعشيرا أخذت العشر من أموالهم (ayn); إذا أخذت منهم عشر أموالهم ومنه العاشر والعشار (sihah); عشرت أموالهم إذا أخذت منهم العشر (tahdhib); عشرهم أخذ عشر مالهم (mufradat)","source_summary":"Kaynaklar mallardan onda bir alma eyleminde birleşir ve bu payı alan kişiyi eylemden türeyen bir adla belirtir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"أخذ واحد من عشرة من الأموال واسم الآخذ العاشر أو العشار","what_is_not_ar":"ليس صيرورة القوم عشرة ولا المعاشرة"},"support_links":["sup_be953e6fe08f22a2b8a8"]},{"boundary":"Bu anlam yalnızca yinelemeli dağıtma biçimlerine bağlıdır; yalın on sayısını veya genel kalabalığı göstermez.","branch_kind":"non_bare","branch_ref":"root_001016/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"onar onar gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çokluk tek tek değil, her biri on üyeli yinelemeli kümeler biçiminde düzenlenir."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir çokluğun ardışık onlu kümeler hâlinde gelişi veya düzenlenişi anlatıldığında kullanılır.","boundary_detail":"Bu anlam yalnızca yinelemeli dağıtma biçimlerine bağlıdır; yalın on sayısını veya genel kalabalığı göstermez.","branch_image_ar":"عشرة عشرة","concept_gloss":"onar onar gelme","contextual_glosses":[{"applicability":"İnsanların geliş ya da sıralanış biçimini doğal Türkçe bir zarf öbeğiyle vermek için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan dışındaki şeylerin onar öğelik kümeler hâlinde gelişini kapsamaz.","preserves":"Yinelenen on kişilik kümeler hâlinde düzenlenmeyi korur."},"facet_ids":["F001"],"text":"onar kişilik gruplar hâlinde","usage_role":"contextual"}],"definition":"İnsanların ya da şeylerin onar kişilik veya onar öğelik kümeler hâlinde gelmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çokluk tek tek değil, her biri on üyeli yinelemeli kümeler biçiminde düzenlenir."}],"identity_rationale":"Kaynak ifadesi insanların ya da şeylerin tek bir onluk sayı olarak değil, art arda onar kişilik veya onar öğelik kümeler hâlinde gelişini bildirir. Dal çerçevesi dağıtmalı çoğulluğu doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"onar onar"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"onar onar"}],"lexicalization_note":"Tanım yalnızca verilen ikilemeli dağıtma biçimlerine bağlanır ve bunlardan bağımsız bir yalın kök anlamı çıkarmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; genel topluluk dalı, onluk dağıtım koşulunu görünür kılan en yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda onluk dağıtım kurucu koşuldur; komşu dal yalnızca topluluk olmayı bildirir ve belirli bir küme büyüklüğü gerektirmez.","focus_only":"Her kümenin tam on üyeli olmasını gerektirir.","gloss":"ardışık topluluk","neighbor_only":"Üye sayısı belirtilmeyen genel bir insan topluluğunu veya kafileyi gösterir.","neighbor_ref":"root_000643/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da insanların birden çok küme hâlinde gelmesini veya bulunmasını anlatabilir."}],"source_phrase_ar":"جاء القوم عشار عشار ومعشر معشر أي عشرة عشرة (maqayis;ayn;tahdhib); عشار بالضم معدول من عشرة (sihah); جاءوا عشارى عشرة عشرة (mufradat)","source_summary":"Kaynaklar iki yinelemeli biçimi de insanların onar onar gelmesini anlatan dağıtmalı kullanım olarak açıklar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"مجيء الأشياء أو القوم على هيئة عشرة عشرة","what_is_not_ar":"ليس العدد المفرد وحده ولا العشيرة"},"support_links":[]},{"boundary":"Dal deve sulama düzenine özgüdür; onuncu gün gelişi ile iki sulama arasındaki aralık ayrı görünümler olarak tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_001016/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"develerin onuncu gün sulanması","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Develer sulama döngüsünün onuncu gününde suya gelir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir anlatım aynı terimi iki sulama arasındaki süre olarak tanımlar."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Deve sulama döngüsünün temel görünümünü anlatır; aralık anlamı gerektiğinde ayrıca açıklanmalıdır.","boundary_detail":"Dal deve sulama düzenine özgüdür; onuncu gün gelişi ile iki sulama arasındaki aralık ayrı görünümler olarak tutulur.","branch_image_ar":"ورد الإبل في العاشر","concept_gloss":"develerin onuncu gün sulanması","contextual_glosses":[{"applicability":"Develerin düzenli sulama sırasını eylem olarak anlatan cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki sulama arasındaki sürenin ad olarak kullanılmasını açıkça vermez.","preserves":"Develerin onlu sulama döngüsüyle suya gelişini korur."},"facet_ids":["F001"],"text":"her on günde bir suya gelmek","usage_role":"contextual"}],"definition":"Develerin belirli bir susuz bırakma düzeninde onuncu gün suya getirilmesi; bir kaynak anlatımında ise iki sulama arasındaki süredir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Develer sulama döngüsünün onuncu gününde suya gelir."},{"facet_id":"F002","role":"source_variant","statement":"Bir anlatım aynı terimi iki sulama arasındaki süre olarak tanımlar."}],"identity_rationale":"Kaynak ifadesi deve sulama düzeninde onuncu gün suya gelmeyi ortak çekirdek yapar, fakat bir anlatım aynı biçimi iki sulama arasındaki süre olarak verir. Dal korunabilir, ancak gün olayı ile aralık ölçüsü birbirine eşitlenmeden belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"develerin onuncu gün suya gelmesi veya iki sulama arası"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"her on günde bir suya gelen develer"}],"lexicalization_note":"Tanım yalın sulama düzeni adını ve develeri niteleyen kalıbı ayırır; bu hayvancılık kullanımı genel onuncu gün anlamına yayılmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; dokuzlu sulama döngüsü, sayısal sınırı en doğrudan gösteren komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Hayvan, eylem ve düzen aynıdır; ayırıcı sınır sulama döngüsünün dokuzlu ya da onlu olmasıdır.","focus_only":"Develerin onlu sulama döngüsünü ve onuncu gün gelişini bildirir.","gloss":"develerin dokuzlu sulama döngüsü","neighbor_only":"Develerin dokuzlu sulama döngüsünü bildirir.","neighbor_ref":"root_000181/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da develerin susuz bırakılıp belirli bir günde suya getirilme düzenini adlandırır."}],"source_phrase_ar":"العشر ورد الإبل يوم العاشر (maqayis;ayn;tahdhib); العشر بالكسر ما بين الوردين (sihah); العشر في الإظماء وإبل عواشر (mufradat)","source_summary":"Kaynakların çoğu onuncu gün suya gelişi öne çıkarırken toplu ifade, aynı adın iki sulama arasındaki süre için de verildiğini gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"العشر في الإظماء وورد الإبل يوم العاشر أو ما بين الوردين","what_is_not_ar":"ليس عاشوراء ولا حمل الناقة"},"support_links":[]},{"boundary":"Çekirdek on aylık deve gebeliğidir; doğumu yaklaşan başka hayvanlar ve yeni doğurmuş ceylan kullanımı bu çekirdekle özdeş değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001016/B007","candidate_links":[{"candidate_id":"cand_6903c6a189fa549479a1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"gebeliği on aya ulaşmış deve","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi devenin gebeliği on ayını tamamlamış ve doğum zamanı yaklaşmıştır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı söz varlığı bir kaynakta yakın zamanda doğurmuş ceylanlar için de kullanılır."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kaynaklarca ortaklaşa desteklenen deve gebeliği çekirdeğini en kısa ve doğal biçimde karşılar.","boundary_detail":"Çekirdek on aylık deve gebeliğidir; doğumu yaklaşan başka hayvanlar ve yeni doğurmuş ceylan kullanımı bu çekirdekle özdeş değildir.","branch_image_ar":"حمل الناقة عشرة أشهر","concept_gloss":"gebeliği on aya ulaşmış deve","contextual_glosses":[{"applicability":"Gebelik süresi ile doğumun yakınlığının birlikte açıkça belirtilmesi gereken bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yeni doğurmuş ceylanlara özgü yan kullanımı vermez.","preserves":"Hayvan türünü, on aylık gebeliği ve yaklaşan doğumu korur."},"facet_ids":["F001"],"text":"doğumu yaklaşmış on aylık gebe deve","usage_role":"explanatory"}],"definition":"Gebeliği on aya ulaşmış ve bu nedenle doğumu yaklaşmış deveyi ya da bu durumdaki develeri bildirir; ayrıca yeni doğurmuş ceylanlar için sınırlı bir kaynak çeşitlemesi vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi devenin gebeliği on ayını tamamlamış ve doğum zamanı yaklaşmıştır."},{"facet_id":"F002","role":"source_variant","statement":"Aynı söz varlığı bir kaynakta yakın zamanda doğurmuş ceylanlar için de kullanılır."}],"identity_rationale":"Kaynak ifadesinin baskın çekirdeği gebeliği on aya ulaşmış ve doğumu yaklaşmış devedir. Aynı toplu iddiada yeni doğurmuş ceylanlar için ayrı bir kullanım da bulunur; bu, deve gebeliğinin tanımına katılmamalı ve kaynak çeşitlemesi olarak bağımlı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"gebeliği on aya ulaşmış deve"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"gebeliği on aya ulaşmış veya doğumu yaklaşmış develer"}],"lexicalization_note":"Tanım deveyle kurulan gebelik kalıbını ve çoğul adı ayırır; hayvan türü ile on aylık süre yalın kökün genel anlamına dönüştürülmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; genel yakın doğum dalı, on aylık deve koşulunu en iyi görünür kılar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hayvanı baskın olarak deveyle ve gebeliği on ayla sınırlar; komşu dal daha genel yakın doğum durumudur.","focus_only":"Devede gebeliğin özellikle on aya ulaşmasını kurucu koşul yapar.","gloss":"doğumu yaklaşmış hayvan","neighbor_only":"Deve veya kısrakta doğumun yaklaşmasını belirli bir gebelik ayı şartı olmadan bildirir.","neighbor_ref":"root_000493/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da gebe bir hayvanda doğum zamanının yaklaşmasını anlatabilir."}],"source_phrase_ar":"ناقة عشراء وهي التي أقربت سميت عشراء لتمام عشرة أشهر لحملها (maqayis); الناقة التي أتت عليها عشرة أشهر (sihah); إذا بلغت الناقة في حملها عشرة أشهر فهي عشراء (tahdhib); ناقة عشراء مرت من حملها عشرة أشهر وجمعها عشار (mufradat); الظباء الحديثات العهد بالنتاج (tahdhib)","source_summary":"Ortak anlatım on aylık gebeliğe ulaşan deveyi temel alır; toplu iddia ayrıca yeni doğurmuş ceylanlara uzanan farklı bir hayvan kullanımını kaydeder.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الناقة العشراء والنوق العشار إذا بلغ حملها عشرة أشهر وما لحق بذلك من قرب النتاج","what_is_not_ar":"ليس ورد الإبل في اليوم العاشر"},"support_links":["sup_3993560859560d7e1c34"]},{"boundary":"Bu dal eşek anırmasına ve onlu ses dizisine bağlıdır; genel yüksek ses veya herhangi bir yineleme değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001016/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"eşeğin on kez yinelenen anırması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eşek güçlü ve art arda anırır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anırma dizisi on ses veya yineleme olarak sayılır."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvan, ses türü ve onlu yineleme birlikte kastedildiğinde dalın tam çekirdeğini karşılar.","boundary_detail":"Bu dal eşek anırmasına ve onlu ses dizisine bağlıdır; genel yüksek ses veya herhangi bir yineleme değildir.","branch_image_ar":"نهيق بعشر ترجيعات","concept_gloss":"eşeğin on kez yinelenen anırması","contextual_glosses":[{"applicability":"Eşeğin çıkardığı ses dizisini eylem olarak çevirmek gereken cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Anırma eylemini, onlu sayıyı ve art arda oluşu korur."},"facet_ids":["F001","F002"],"text":"on kez art arda anırmak","usage_role":"contextual"}],"definition":"Eşeğin art arda ve güçlü biçimde anırması, özellikle bu dizinin on ayrı ses ya da yineleme oluşturmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eşek güçlü ve art arda anırır."},{"facet_id":"F002","role":"specialization","statement":"Anırma dizisi on ses veya yineleme olarak sayılır."}],"identity_rationale":"Kaynak ifadesi çok ve güçlü biçimde anıran eşeği, özellikle on ses ya da yineleme sayısıyla tanımlanan anırma dizisine bağlar. Dal çerçevesi hayvanı, ses türünü, yinelemeyi ve sayıyı doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"çok ve art arda anıran eşek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"eşeğin on kez anırması"}],"lexicalization_note":"Tanım çok anıran eşeğin adını ve eşekle kurulan onlu anırma kalıbını ayırır; ses anlamı başka hayvanlara genellenmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; genel şiddetli ses dalı, odaktaki onlu yineleme koşulunu en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda onlu yineleme ve eşek anırması kurucudur; komşu dalda temel özellik ses şiddetidir ve hayvan kapsamı daha geniştir.","focus_only":"Eşek anırmasını on seslik veya on yinelemeli bir dizi olarak sınırlar.","gloss":"şiddetli hayvan sesi","neighbor_only":"Eşek ya da boğanın sesindeki genel şiddeti, belirli bir yineleme sayısı olmadan bildirir.","neighbor_ref":"root_000864/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal yüksek ve dikkat çekici eşek anırmasını kapsayabilir."}],"source_phrase_ar":"المعشر الحمار الشديد النهيق (maqayis;ayn;tahdhib); تعشير الحمار نهيقه عشرة أصوات (sihah); التعشير نهاق الحمير لكونه عشرة أصوات (mufradat)","source_summary":"Kaynaklar çok ve güçlü anıran eşek ile on seslik anırma dizisini aynı kullanım alanının kişi ve olay görünümleri olarak sunar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"تعشير الحمار ونهيقه المتتابع حتى يبلغ عشر نهقات أو ترجيعات","what_is_not_ar":"ليس العدد المجرد ولا التعشير في المصاحف"},"support_links":[]},{"boundary":"Çekirdek bütünden ayrılan parçalardır; paylar ve dağılmış insan kümeleri bu çekirdeğin bağımlı uzantılarıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001016/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"parçalara, paylara veya dağınık kümelere ayrılma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kap veya benzeri bir bütün kırılarak ayrı parçalara dönüşür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrılmış bölümler, kesilmiş bir hayvanın bölüşüm paylarını da gösterebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Parçalanma görüntüsü insanlara aktarılarak her yöne dağılmış kümeleri anlatır."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel kırılma çekirdeği ile pay ve dağılmış topluluk uzantılarını birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Çekirdek bütünden ayrılan parçalardır; paylar ve dağılmış insan kümeleri bu çekirdeğin bağımlı uzantılarıdır.","branch_image_ar":"قطع وأعشار","concept_gloss":"parçalara, paylara veya dağınık kümelere ayrılma","contextual_glosses":[{"applicability":"Bir kabın veya başka bir nesnenin kırık durumunu niteleyen cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bölüşüm paylarını ve her yöne dağılmış insan kümelerini kapsamaz.","preserves":"Fiziksel bütünün kırık ve ayrı parçalara dönüşmesini korur."},"facet_ids":["F001"],"text":"parça parça kırılmış","usage_role":"contextual"},{"applicability":"İnsan topluluklarının farklı yönlere ayrılmasını anlatan cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Fiziksel kırık parça ve bölüşüm payı anlamlarını kapsamaz.","preserves":"Toplulukların birbirinden ayrılıp farklı yönlere gitmesini korur."},"facet_ids":["F003"],"text":"her yana dağılmış","usage_role":"contextual"}],"definition":"Bir bütünün kırılma ya da ayırma sonucunda parçalara ayrılmasıdır; bu parçalar pay olarak bölüştürülebilir, insan topluluklarına aktarıldığında ise her yana dağılmış kümeleri anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kap veya benzeri bir bütün kırılarak ayrı parçalara dönüşür."},{"facet_id":"F002","role":"extension","statement":"Ayrılmış bölümler, kesilmiş bir hayvanın bölüşüm paylarını da gösterebilir."},{"facet_id":"F003","role":"extension","statement":"Parçalanma görüntüsü insanlara aktarılarak her yöne dağılmış kümeleri anlatır."}],"identity_rationale":"Kaynak ifadesi kırılarak ayrılmış parçaları çekirdek alır, fakat kesilmiş hayvan paylarını, herhangi bir parçayı ve her yana dağılmış toplulukları da aynı dalda toplar. Dal kullanılabilir; fiziksel kırık parça, bölüşüm payı ve dağılma uzantıları birbirine özdeş sayılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kırık parçalar veya bölüşülmüş paylar"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"parça parça kırılmış çömlek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"herhangi bir şeyden ayrılmış parça"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"her yana dağılmış topluluklar"}],"lexicalization_note":"Tanım yalın parça biçimlerini, kırık çömlek kalıbını ve dağılma biçimini ayrı yüzlerde tutar; kalıp anlamı bütüne yayılmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; kırılma sonucu oluşan parçaları anlatan komşu, çekirdek örtüşmesini ve odaktaki uzantıları en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Fiziksel kırık parça çekirdeği örtüşür; odak dal paylara ve dağılmış topluluklara uzanırken komşu dal küçük kırıntı türlerine yoğunlaşır.","focus_only":"Kırık kap parçalarının yanında bölüşüm paylarını ve dağılmış insan kümelerini de kapsar.","gloss":"kırılıp ayrılmış küçük parçalar","neighbor_only":"Özellikle kırılma sonucu oluşan küçük metal, taş veya başka madde parçalarını kapsar.","neighbor_ref":"root_000230/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir bütünün kırılmasıyla oluşan ayrı parçaları adlandırır."}],"source_phrase_ar":"العشر القطعة تنكسر من القدح أو البرمة (maqayis); برمة أعشار إذا انكسرت قطعا قطعا (sihah;tahdhib); أعشار الجزور الأنصباء (sihah); قدح أعشار منكسر (mufradat); العشارة القطعة من كل شيء (tahdhib); ذهب القوم عشاريات متفرقين في كل وجه (tahdhib)","source_summary":"Toplu kaynak anlatımı kırık kap parçalarını, bölüşülen payları, herhangi bir şeyden ayrılan parçayı ve farklı yönlere dağılan insan kümelerini tek bir ayrılma görüntüsü çevresinde birleştirir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الأعشار في القدح والبرمة والقلب والجزور والقطعة والفرق المتفرقة","what_is_not_ar":"ليس جزء العشر الحسابي وحده"},"support_links":[]},{"boundary":"Anlam yalnızca on arşınlık uzunluğu bildirir; genel uzunluk, ölçme eylemi veya beş arşınlık nesne değildir.","branch_kind":"bare","branch_ref":"root_001016/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"on arşın uzunluğunda olan şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesnenin uzunluğu on arşın olarak belirlenir."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Türü belirtilmeyen bir nesnenin sabit uzunluk niteliğini ifade etmek için uygundur.","boundary_detail":"Anlam yalnızca on arşınlık uzunluğu bildirir; genel uzunluk, ölçme eylemi veya beş arşınlık nesne değildir.","branch_image_ar":"طول عشر أذرع","concept_gloss":"on arşın uzunluğunda olan şey","contextual_glosses":[{"applicability":"Bir nesnenin boyunu sıfat öbeğiyle doğal biçimde vermek gereken cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uzunluk niteliğini ve on arşınlık sabit ölçüyü korur."},"facet_ids":["F001"],"text":"on arşın uzunluğunda","usage_role":"contextual"}],"definition":"Uzunluğu on arşına ulaşan ya da tam on arşın olan şeyi niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesnenin uzunluğu on arşın olarak belirlenir."}],"identity_rationale":"Kaynak ifadesi bir nesnenin uzunluğunun tam on arşına ulaşmasını tek ve açık ölçü koşulu olarak verir. Dal çerçevesi nesne türü eklemeden bu sabit uzunluğu doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"on arşın uzunluğunda olan şey"}],"lexicalization_note":"Tanım yalın niteleme anlamını verir ve herhangi bir özel nesne ya da ölçme kalıbını dışarıdan eklemez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; arşınla ölçme dalı, sabit sonuç ile ölçme işlemi arasındaki sınırı en açık gösterir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal sabit bir on arşınlık niteliği adlandırır; komşu dal ise ölçme işlemini ve değişebilen arşın miktarını anlatır.","focus_only":"Ölçüm sonucunun tam on arşın olmasını bildirir.","gloss":"arşınla ölçme","neighbor_only":"Kumaş, duvar veya başka bir şeyi arşın birimiyle ölçme eylemini ve sonucunu kapsar.","neighbor_ref":"root_000512/B002","relation_type":"same_field","shared_zone":"Her iki dal uzunluğu arşın birimiyle ifade eder."}],"source_phrase_ar":"العشاري ما بلغ طوله عشر أذرع (maqayis); العشارى ما يقع طوله عشرة أذرع (sihah); العشاري ما طوله عشرة أذرع (mufradat)","source_summary":"Kaynaklar bu nitelemeyi uzunluğu on arşın olan şey için ortak ve tutarlı biçimde verir.","sources":["MQ","SI","MU"],"what_is_ar":"العشاري لما بلغ طوله عشر أذرع","what_is_not_ar":"ليس العشار للنوق ولا العشار عشرة عشرة"},"support_links":[]},{"boundary":"Dal yalnızca Muharrem ayının onuncu gününü gösterir; genel onuncu gün veya deve sulama günü değildir.","branch_kind":"bare","branch_ref":"root_001016/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"Muharrem ayının onuncu günü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan gün Muharrem ayı içindeki onuncu gündür."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli takvim gününün açıklayıcı ve doğrudan Türkçe karşılığıdır.","boundary_detail":"Dal yalnızca Muharrem ayının onuncu gününü gösterir; genel onuncu gün veya deve sulama günü değildir.","branch_image_ar":"اليوم العاشر من المحرم","concept_gloss":"Muharrem ayının onuncu günü","contextual_glosses":[{"applicability":"Gün adının cümle içinde açıklayıcı bir tarih öbeği olarak çevrilmesinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Takvim ayını ve onuncu gün sırasını korur."},"facet_ids":["F001"],"text":"Muharrem'in onuncu günü","usage_role":"contextual"}],"definition":"Muharrem ayının onuncu günü için kullanılan gündür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan gün Muharrem ayı içindeki onuncu gündür."}],"identity_rationale":"Kaynak ifadesi iki söz biçimini de Muharrem ayının onuncu günü için ad olarak verir. Dal çerçevesi takvim gününü, ayı ve sıra sayısını eksiksiz korur.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"Muharrem ayının onuncu günü"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"Muharrem ayının onuncu günü"}],"lexicalization_note":"Tanım, iki yalın gün adını aynı takvim gününe bağlar ve başka ay ya da hafta günü anlamı eklemez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; başka bir adlandırılmış takvim günü, ay tarihi ile hafta günü ayrımını açıklaştırır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal ay içindeki tarihe, komşu dal haftalık döngüdeki güne bağlıdır; takvimsel gönderimleri farklıdır.","focus_only":"Belirli bir ayın onuncu tarihini adlandırır.","gloss":"salı günü","neighbor_only":"Haftanın salı gününü ve onun ad biçimlerini gösterir.","neighbor_ref":"root_000203/B006","relation_type":"same_field","shared_zone":"Her iki dal takvimde belirli bir günü adlandırır."}],"source_phrase_ar":"عاشوراء اليوم العاشر من المحرم (maqayis); يوم عاشوراء وعشوراء أيضا (sihah); يوم عاشوراء هو اليوم العاشر من المحرم (tahdhib)","source_summary":"Kaynaklar iki biçimin de aynı takvim gününü, Muharrem ayının onuncu gününü adlandırdığını bildirir.","sources":["MQ","SI","TA"],"what_is_ar":"عاشوراء وعشوراء اسمان لليوم العاشر من المحرم","what_is_not_ar":"ليس العشر في ورد الإبل"},"support_links":[]},{"boundary":"Dal kişiler arası yakın ilişki ve birlikte yaşamadır; akraba topluluğu, kabile veya yalnızca evli olma durumu değildir.","branch_kind":"bare","branch_ref":"root_001016/B012","candidate_links":[{"candidate_id":"cand_379e070e1a67a84d2312","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"yakın ilişki ve birlikte yaşama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki ya da daha çok kişi yakın ilişki kurar ve hayatı birlikte paylaşır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yakın ilişki kurulan kimse, özellikle eş, bu ilişki üzerinden adlandırılır."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşılıklı yakınlık eylemini ve süreklilik taşıyan ortak yaşamı birlikte anlatan genel karşılıktır.","boundary_detail":"Dal kişiler arası yakın ilişki ve birlikte yaşamadır; akraba topluluğu, kabile veya yalnızca evli olma durumu değildir.","branch_image_ar":"مداخلة ومعاشرة","concept_gloss":"yakın ilişki ve birlikte yaşama","contextual_glosses":[{"applicability":"Kişilerin süreklilik taşıyan birlikteliğini eylem olarak anlatan cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiler arası yakınlığı ve birlikte yaşama sürecini korur."},"facet_ids":["F001","F002"],"text":"yakın ilişki içinde yaşamak","usage_role":"contextual"}],"definition":"İnsanların yakın ilişki içinde bulunması, birbirleriyle birlikte yaşaması ve bu ilişki içindeki kimsenin, özellikle eşin, ilişki kurulan kişi olarak adlandırılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki ya da daha çok kişi yakın ilişki kurar ve hayatı birlikte paylaşır."},{"facet_id":"F002","role":"associated_use","statement":"Yakın ilişki kurulan kimse, özellikle eş, bu ilişki üzerinden adlandırılır."}],"identity_rationale":"Kaynak ifadesi birlikte bulunma, yakın ilişki kurma ve hayatı paylaşma çekirdeğinden eş ya da yakın ilişki kurulan kişi adına uzanır. Dal çerçevesi ilişkiyi ve katılımcı adını birbirine bağlı fakat ayrı görünümler olarak doğru sunar.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"birlikte yaşama ve yakın ilişki"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"yakın ilişki içinde birlikte yaşama"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"yakın ilişki kurulan kimse veya eş"}],"lexicalization_note":"Tanım yalın ilişki, karşılıklı birlikte yaşama ve ilişki kurulan kişi anlamlarını kapsar; belirli bir kalıba bağımlı değildir.","neighbor_coverage_note":"Adayların tümü değerlendirildi; yakın beraberlik dalı ortak çekirdeği ve kapsam farkını en iyi ortaya koyar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği karşılıklı ilişki ve ortak yaşamdır; komşu dal temas, içli dışlı olma ve bedensel beraberlik gibi ek kapsamlar taşır.","focus_only":"Yakın ilişkiyi genel olarak ve bu ilişki içindeki eş ya da kişiyi adlandırır.","gloss":"yakın beraberlik","neighbor_only":"Birlikte bulunmanın yanında iç yüzü bilme, eşlerin bedensel yakınlığı ve belirli süreli beraberliği de kapsar.","neighbor_ref":"root_001341/B004","relation_type":"near_synonym","shared_zone":"Her iki dal kişiler arasında yakınlık, birlikte bulunma ve eş ilişkisi bağlamlarını kapsayabilir."}],"source_phrase_ar":"المخالطة والمداخلة فالعشرة والمعاشرة وعشيرك الذي يعاشرك (maqayis); المعاشرة المخالطة وكذلك التعاشر (sihah); العشير الزوج سمي عشيرا لأنه يعاشرها وتعاشره (tahdhib); عاشرته صرت له كعشرة في المصاهرة والعشير المعاشر (mufradat)","source_summary":"Kaynaklar yakın ilişki ve birlikte yaşamayı ortak çekirdek yapar; ilişki kurulan kişiyi ve özellikle eşi de bu çekirdekten adlandırır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"المعاشرة والتعاشر والعشير بمعنى المخالطة والصحبة والزوج والمعاشر","what_is_not_ar":"ليس العشيرة بمعنى القبيلة ولا العدد عشرة"},"support_links":["sup_b9f9f9502109324eb98c"]},{"boundary":"Çekirdek kişinin ailesi ve yakın akraba topluluğudur; ortak işi olan daha genel topluluk bunun kapsam uzantısıdır.","branch_kind":"bare","branch_ref":"root_001016/B013","candidate_links":[{"candidate_id":"cand_379e070e1a67a84d2312","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"akraba topluluğu veya ortak amaçlı topluluk","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin ailesi, yakın akrabaları veya kabilesi birbirine bağlı bir topluluk oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad, üyeleri ortak bir iş veya amaçta birleşen daha genel topluluklara genişler."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Soy bağına dayalı çekirdeği ve ortak iş üzerinden genişleyen topluluk kapsamını birlikte gösterir.","boundary_detail":"Çekirdek kişinin ailesi ve yakın akraba topluluğudur; ortak işi olan daha genel topluluk bunun kapsam uzantısıdır.","branch_image_ar":"جماعة وعشيرة","concept_gloss":"akraba topluluğu veya ortak amaçlı topluluk","contextual_glosses":[{"applicability":"Bir kişinin destek aldığı aile ve soy çevresini anlatan cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Soy bağı taşımadan ortak bir işte birleşen genel topluluk kapsamını vermez.","preserves":"Kişiye bağlı yakın aile ve akraba topluluğunu korur."},"facet_ids":["F001"],"text":"yakınları ve akrabaları","usage_role":"contextual"},{"applicability":"Üyelerin soy bağından çok ortak işiyle tanımlandığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin ailesi, akrabaları ve kabilesi çekirdeğini vermez.","preserves":"Ortak iş veya amaç çevresinde oluşan topluluk uzantısını korur."},"facet_ids":["F002"],"text":"aynı amaçta birleşen topluluk","usage_role":"contextual"}],"definition":"Kişinin yakın ailesi, akrabaları veya kabilesinden oluşan ve ona dayanışma sağlayan topluluktur; daha geniş kullanımda ortak bir işi olan herhangi bir topluluğu da gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin ailesi, yakın akrabaları veya kabilesi birbirine bağlı bir topluluk oluşturur."},{"facet_id":"F002","role":"extension","statement":"Ad, üyeleri ortak bir iş veya amaçta birleşen daha genel topluluklara genişler."}],"identity_rationale":"Kaynak ifadesi kişinin dayanıştığı yakın ailesi veya kabilesini temel alırken, ortak işi olan herhangi bir topluluğu da daha geniş bir adla kapsar. Dal korunabilir, ancak soy bağına dayalı topluluk ile yalnızca ortak amaçta birleşen topluluk aynı sınırda tanımlanmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"kişinin ailesi, yakın akrabaları veya kabilesi"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"ortak bir işte birleşen topluluk"}],"lexicalization_note":"Tanım yalın akraba topluluğu ile ortak işte birleşen genel topluluk biçimlerini iki ayrı yüz olarak korur.","neighbor_coverage_note":"Adayların tümü değerlendirildi; soy topluluğu dalı, akrabalık çekirdeği ile ortak amaç uzantısının sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Soy topluluğu alanında yakınlaşırlar; odak dal ortak amaçlı soy dışı topluluklara da uzanırken komşu dal soy ve kabile örgüsünde kalır.","focus_only":"Yakın aile ve kabile yanında ortak işi olan genel toplulukları da kapsar.","gloss":"soy ve kabile topluluğu","neighbor_only":"Soydan gelen küçük ya da büyük insan birliğini, özellikle kabile bölümünü gösterir.","neighbor_ref":"root_000383/B010","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin soy bağıyla bağlı akraba veya kabile topluluğunu gösterebilir."}],"source_phrase_ar":"عشيرة الرجل لمعاشرة بعضهم بعضا (maqayis); المعشر كل جماعة أمرهم واحد (maqayis;tahdhib); العشيرة القبيلة (sihah); العشيرة أهل الرجل الذين يتكثر بهم (mufradat)","source_summary":"Toplu anlatım kişinin yakın ailesi ve kabilesi ile ortak işi bulunan herhangi bir topluluğu aynı birliktelik alanında, fakat farklı kapsamlarla verir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"العشيرة والقبيلة والمعشر والجماعة ذات الأمر الواحد","what_is_not_ar":"ليس الزوج العشير وحده ولا العدد عشرة"},"support_links":["sup_b9f9f9502109324eb98c"]},{"boundary":"Dal belirli bir ağaç veya bitki türüdür; sayı, kesir ya da başka ağaç türlerinin genel adı değildir.","branch_kind":"bare","branch_ref":"root_001016/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"tatlı özsulu iri bir ağaç","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir ağaç veya bitki türünü adlandırır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağaç iri olabilir ve tatlı bir özsu verir."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitki türünü ayırt edici büyüklük ve özsu özellikleriyle birlikte açıklayan karşılıktır.","boundary_detail":"Dal belirli bir ağaç veya bitki türüdür; sayı, kesir ya da başka ağaç türlerinin genel adı değildir.","branch_image_ar":"شجر العشر","concept_gloss":"tatlı özsulu iri bir ağaç","contextual_glosses":[{"applicability":"Tür adının hedef dilde açıklayıcı bir betimlemeyle verilmesi gereken bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bitkiyi, büyüklüğünü ve özsu niteliğini korur."},"facet_ids":["F001","F002"],"text":"tatlı özsu veren iri ağaç","usage_role":"explanatory"}],"definition":"İri büyüyebilen ve tatlı bir özsu çıkaran belirli bir ağaç ya da bitki türüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir ağaç veya bitki türünü adlandırır."},{"facet_id":"F002","role":"specialization","statement":"Ağaç iri olabilir ve tatlı bir özsu verir."}],"identity_rationale":"Kaynak ifadesi belirli bir iri ağaç ya da bitkiyi, ondan çıkan tatlı özsuyla birlikte tanımlar. Dal çerçevesi canlı türünü ve ayırt edici salgısını doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"tatlı özsuyu olan iri ağaç veya bitki"}],"lexicalization_note":"Tanım yalın bitki adını verir ve komşu ağaç adlarını ya da sayı temelli anlamları bu dala katmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; farklı bir tanımlı ağaç türü, alan ortaklığına rağmen tür sınırının ayrı olduğunu gösterir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortaklık yalnızca bitki alanındadır; özsu, gövde ve benzerlik özellikleri farklı türlere işaret eder, bu yüzden adlar yer değiştiremez.","focus_only":"Tatlı özsu veren belirli ve iri bir ağaç türünü gösterir.","gloss":"kalın köklü başka bir ağaç","neighbor_only":"Kalın köklü, iyi odunlu ve başka bir ağaca benzeyen farklı bir ağaç türünü gösterir.","neighbor_ref":"root_000012/B002","relation_type":"same_field","shared_zone":"Her iki dal belirli bir ağaç türünün sözlük anlamını verir."}],"source_phrase_ar":"العشر نبت (maqayis); العشر شجر له صمغ (sihah); العشر من كبار الشجر وله صمغ حلو (tahdhib)","source_summary":"Kaynaklar bunun bir ağaç ya da bitki olduğunu bildirir; ayrıntılı anlatım iri oluşunu ve tatlı özsu vermesini ekler.","sources":["MQ","SI","TA"],"what_is_ar":"العشر شجر أو نبت له صمغ","what_is_not_ar":"ليس العدد عشرة ولا العشير المعاشر"},"support_links":[]},{"boundary":"Dal kutsal metin nüshalarındaki on ayetlik bölüm işaretlerine özgüdür; genel sayma, hayvan sesi veya çizik izi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001016/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"her on ayeti gösteren işaretleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Metin nüshasında her on ayetlik bölümün sınırı bir işaretle gösterilir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşaretleme işlemi sonucunda oluşan halkalar veya göstergeler ayrıca adlandırılır."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Metin nüshasındaki işlemi ve on ayetlik aralık sonucunu birlikte anlatan genel karşılıktır.","boundary_detail":"Dal kutsal metin nüshalarındaki on ayetlik bölüm işaretlerine özgüdür; genel sayma, hayvan sesi veya çizik izi değildir.","branch_image_ar":"علامة كل عشر آيات","concept_gloss":"her on ayeti gösteren işaretleme","contextual_glosses":[{"applicability":"Metin nüshasını bölümlere ayırma işleminin eylem olarak anlatıldığı cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"On ayetlik aralığı ve bu aralıkta işaret koyma işlemini korur."},"facet_ids":["F001","F002"],"text":"her on ayette bir işaret koymak","usage_role":"contextual"}],"definition":"Kutsal metin nüshasında her on ayetlik bölümü göstermek üzere işaret koymak ve bu işaretleri adlandırmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Metin nüshasında her on ayetlik bölümün sınırı bir işaretle gösterilir."},{"facet_id":"F002","role":"associated_use","statement":"İşaretleme işlemi sonucunda oluşan halkalar veya göstergeler ayrıca adlandırılır."}],"identity_rationale":"Kaynak ifadesi kutsal metin nüshalarında her on ayetlik bölüm için işaret koyma işlemini ve ortaya çıkan işaretleri bildirir. Dal çerçevesi işlem, nesne, onlu aralık ve işaret sonucunu doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"kutsal metin nüshasında her on ayete işaret koyma"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"kutsal metin nüshasında her on ayeti gösteren işaretler"}],"lexicalization_note":"Tanım metin nüshasıyla kurulan işaretleme kalıbını ve işaret adını ayırır; bu özel kullanım yalın kök anlamına genellenmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; fiziksel iz dalı, amaçlı bölüm göstergesi ile rastlantısal iz arasındaki farkı açıklaştırır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal düzenleme amacıyla konmuş sayısal bir göstergedir; komşu dal fiziksel temas veya zarar sonucunda oluşan izdir.","focus_only":"Metin nüshasında düzenli olarak her on ayeti gösteren amaçlı işarettir.","gloss":"çizik veya ısırık izi","neighbor_only":"Deri veya başka bir yüzeyde çizme, ısırma, taş ya da toynakla oluşan zarar izidir.","neighbor_ref":"root_001287/B002","relation_type":"same_field","shared_zone":"Her iki dal bir yüzeyde görülen belirgin bir izi konu edinir."}],"source_phrase_ar":"تعشير المصاحف جعل العواشر فيها (sihah); العاشرة حلقة التعشير من عواشر المصحف (tahdhib); العشور في المصاحف علامة العشر الآيات (mufradat)","source_summary":"Kaynaklar metin nüshasına her on ayette bir işaret koyma işlemi ile on ayetlik bölümleri gösteren işaretleri birlikte kaydeder.","sources":["SI","TA","MU"],"what_is_ar":"تعشير المصاحف والعواشر والعشور علامات لعشر الآيات","what_is_not_ar":"ليس تعشير الحمار ولا أخذ العشر من المال"},"support_links":[]},{"boundary":"Dal herhangi on geceyi değil, ay içindeki dokuzlu gecelerden sonraki özel üç gecelik kümeyi gösterir ve tek kaynakla sınırlıdır.","branch_kind":"bare","branch_ref":"root_001016/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"dokuzlu gecelerden sonraki üç gece","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ay içindeki üç gecelik küme, dokuzlu diye adlandırılan önceki üç gecenin ardından gelir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aktarılan değerlendirme, bu gece adlandırmalarını yalnızca bilinen örneklerle sınırlı kabul eder."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ay gecelerinin özel üçlü adlandırma dizgesindeki konumu açıkça belirtmek için kullanılır.","boundary_detail":"Dal herhangi on geceyi değil, ay içindeki dokuzlu gecelerden sonraki özel üç gecelik kümeyi gösterir ve tek kaynakla sınırlıdır.","branch_image_ar":"عشر بعد التسع","concept_gloss":"dokuzlu gecelerden sonraki üç gece","contextual_glosses":[{"applicability":"Özel gece kümesi adını anlaşılır bir takvim açıklamasıyla vermek gereken bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ay bağlamını, üç geceyi ve önceki kümeye göre konumu korur."},"facet_ids":["F001"],"text":"ayın dokuzlu gecelerinden sonraki üç gece","usage_role":"explanatory"}],"definition":"Ayın gecelerini üçlü kümelerle adlandıran özel dizgede, dokuz diye adlandırılan üç geceden sonra gelen üç gecelik kümedir; kullanımın geçerliliği kaynak içinde sınırlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ay içindeki üç gecelik küme, dokuzlu diye adlandırılan önceki üç gecenin ardından gelir."},{"facet_id":"F002","role":"source_variant","statement":"Aktarılan değerlendirme, bu gece adlandırmalarını yalnızca bilinen örneklerle sınırlı kabul eder."}],"identity_rationale":"Kaynak ifadesi ay gecelerini üçlü kümelerle adlandıran özel dizgede, dokuz diye adlandırılan üç geceden sonra gelen üç geceyi gösterir. Aynı tek kaynak bu adlandırma dizgesinin geneline itiraz edildiğini de kaydeder; anlam bu sınırlı ve tartışmalı kullanım olarak korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"ayın dokuzlu gecelerinden sonraki üç gece"}],"lexicalization_note":"Tanım yalın gece kümesi adını verir, ancak onu genel on sayısına veya ayın herhangi üç gecesine genişletmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; hemen önceki üç gecelik küme, odak dalın takvim sırasını en kesin biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kümeler aynı dizgenin ardışık bölümleridir; komşu küme dokuzuncu gecede biter, odak küme onun ardından başlar.","focus_only":"Dokuzlu diye adlandırılan üç geceden sonra gelen sonraki üç geceyi gösterir.","gloss":"dokuzuncu gecede biten üç gece","neighbor_only":"Sonuncusu ayın dokuzuncu gecesi olan önceki üç gecelik kümeyi gösterir.","neighbor_ref":"root_000181/B005","relation_type":"near_synonym","shared_zone":"Her iki dal ay gecelerini ardışık üç gecelik özel kümeler hâlinde adlandırır."}],"source_phrase_ar":"يقال أيضا لثلاث ليال من ليالى الشهر عشر وهي بعد التسع (sihah); كان أبو عبيدة يبطل التسع والعشر إلا أشياء منه معروفة (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Ay gecelerinin bu üçlü adı tek tanıklığa dayanır; tanıklık aynı zamanda adlandırmanın kapsamına yönelik bir çekince aktarır."}],"source_summary":"Bu kullanım tek bir kaynakta, dokuzlu gecelerin ardından gelen üç gecelik küme olarak aktarılır ve aynı aktarım adlandırmanın ancak bilinen örneklerde kabul edildiğini belirtir.","sources":["SI"],"what_is_ar":"ثلاث ليال من ليالي الشهر بعد التسع تسمى عشرا","what_is_not_ar":"ليس اليوم العاشر من المحرم ولا عشر ليال مطلقا"},"support_links":[]},{"boundary":"Dal yalnızca kuşun öndeki uçuş teleklerini gösterir; bütün tüy örtüsü, kanadın tamamı veya kırık parçalar değildir.","branch_kind":"bare","branch_ref":"root_001016/B017","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","surface_ar":"عَشْرٍ"}],"gloss":"kuşun öndeki uçuş telekleri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kuş kanadının ön bölümündeki başlıca uçuş teleklerini gösterir."}}],"root_ar":"ع ش ر","root_id":"root_001016","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel tüy örtüsünden ayrılan belirli kanat teleklerini açıklayan doğrudan karşılıktır.","boundary_detail":"Dal yalnızca kuşun öndeki uçuş teleklerini gösterir; bütün tüy örtüsü, kanadın tamamı veya kırık parçalar değildir.","branch_image_ar":"قوادم الريش","concept_gloss":"kuşun öndeki uçuş telekleri","contextual_glosses":[{"applicability":"Kuşun hangi tüylerinin kastedildiği bağlamdan belliyken daha kısa bir karşılık olarak uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kanat bölgesini, ön konumu ve uçuş teleği niteliğini korur."},"facet_ids":["F001"],"text":"kanadın ön uçuş telekleri","usage_role":"contextual"}],"definition":"Kuşun kanadında önde bulunan ve uçuşta görev alan başlıca teleklerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kuş kanadının ön bölümündeki başlıca uçuş teleklerini gösterir."}],"identity_rationale":"Kaynak ifadesi kuş kanadındaki önde gelen uçuş teleklerini doğrudan adlandırır. Dal çerçevesi bunları genel tüy örtüsünden ve kırık parçalardan ayırarak doğru anatomik sınıra yerleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"kuşun öndeki uçuş telekleri"}],"lexicalization_note":"Tanım yalın kuş tüyü adını belirli bir kanat bölümüyle sınırlar ve genel tüy anlamına genişletmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; genel kuş tüyü dalı, öndeki uçuş teleklerinin alt küme sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel tüy sınıfının konum ve görev bakımından sınırlı bir alt kümesidir; komşu dal bütün tüy örtüsüne kadar genişler.","focus_only":"Yalnızca kanadın ön bölümündeki başlıca uçuş teleklerini gösterir.","gloss":"kuş tüyü","neighbor_only":"Kuşun bütün tüy örtüsünü, tek bir tüyü veya kimi anlatımda genel olarak kanat tüylerini kapsar.","neighbor_ref":"root_000617/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal kuşun tüylerini, özellikle kanat çevresindeki tüyleri gösterebilir."}],"source_phrase_ar":"الأعشار قوادم ريش الطائر (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Kuş kanadının ön uçuş telekleri anlamı tek sözlük tanıklığıyla aktarılır."}],"source_summary":"Tek kaynak kullanımı, sözcüğü kuşun kanadındaki önde gelen uçuş telekleriyle sınırlar.","sources":["SI"],"what_is_ar":"الأعشار قوادم ريش الطائر","what_is_not_ar":"ليس أعشار القدح ولا أعشار الجزور"},"support_links":[]},{"boundary":"Dal genel gece zamanını ve karanlığını kapsar; şiddet, uzunluk ve ayın son gecesi anlamları yalnız ilgili söz öbeklerine bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001392/B001","candidate_links":[{"candidate_id":"cand_46c2cc47efe07d2c117e","lane":"micro"},{"candidate_id":"cand_809bd424b88544b7c33f","lane":"micro"},{"candidate_id":"cand_40afa86f1401f728fb8e","lane":"micro"},{"candidate_id":"cand_6903c6a189fa549479a1","lane":"micro"},{"candidate_id":"cand_379e070e1a67a84d2312","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:2:1:2","qac_word_ref":"89:2:1","surface_ar":"لَيَالٍ"}],"gloss":"gündüzün karşıtı olan gece ve onun karanlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gündüzün karşıtı olan zaman bölümü gecedir; tek bir gece veya birden çok gece olarak sayılabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gece adı, bu zaman bölümüne özgü karanlığı da anlatabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli niteleme kalıpları çok karanlık veya çetin bir geceyi anlatır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir başka pekiştirme kalıbı gecenin uzunluğunu veya şiddetini özellikle öne çıkarır."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Özel bir söz öbeği, ayın hem en karanlık hem de son gecesini belirtir."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel gece zamanını ve bu zamana bağlı karanlık anlamını birlikte temsil eder; özel nitelemeler ayrıca bağlama göre çevrilir.","boundary_detail":"Dal genel gece zamanını ve karanlığını kapsar; şiddet, uzunluk ve ayın son gecesi anlamları yalnız ilgili söz öbeklerine bağlıdır.","branch_image_ar":"الليل خلاف النهار وظلمته","concept_gloss":"gündüzün karşıtı olan gece ve onun karanlığı","contextual_glosses":[{"applicability":"Zaman bölümünden çok o zamandaki karanlığın anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geceye özgü karanlık görünümünü doğrudan korur."},"facet_ids":["F002"],"text":"gece karanlığı","usage_role":"contextual"},{"applicability":"Yalnız karanlığın şiddetini veya gecenin çetinliğini pekiştiren söz öbeklerinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gecenin yoğun karanlığını ve çetinlik vurgusunu korur."},"facet_ids":["F003"],"text":"çok karanlık ve çetin gece","usage_role":"contextual"},{"applicability":"Uzunluk ile genel şiddet arasında değişebilen özel pekiştirme kalıbını açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalıbın uzunluk ve pekiştirilmiş şiddet seçeneklerini birlikte korur."},"facet_ids":["F004"],"text":"uzun ya da şiddeti pekiştirilmiş gece","usage_role":"explanatory"},{"applicability":"Yalnız ay içindeki özel konumu ve olağanüstü karanlığı birlikte belirten söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayın son gecesi olma koşulunu ve en yoğun karanlığı korur."},"facet_ids":["F005"],"text":"ayın en karanlık ve son gecesi","usage_role":"contextual"}],"definition":"Gündüzün karşıtı olan gece zamanı ve bu zamana özgü karanlıktır. Belirli söz öbekleri, temel anlamı değiştirmeden gecenin çok karanlık, çetin ya da uzun oluşunu veya ayın en karanlık son gecesini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gündüzün karşıtı olan zaman bölümü gecedir; tek bir gece veya birden çok gece olarak sayılabilir."},{"facet_id":"F002","role":"extension","statement":"Gece adı, bu zaman bölümüne özgü karanlığı da anlatabilir."},{"facet_id":"F003","role":"specialization","statement":"Belirli niteleme kalıpları çok karanlık veya çetin bir geceyi anlatır."},{"facet_id":"F004","role":"specialization","statement":"Bir başka pekiştirme kalıbı gecenin uzunluğunu veya şiddetini özellikle öne çıkarır."},{"facet_id":"F005","role":"source_variant","statement":"Özel bir söz öbeği, ayın hem en karanlık hem de son gecesini belirtir."}],"identity_rationale":"Kaynak ifadesi, gündüzün karşıtı olan gece zamanını ve gece karanlığını açıkça temel anlam olarak verir; tekil ve çoğul biçimlerin yanında karanlığın şiddetini, gecenin uzunluğunu veya belirli bir ay gecesini anlatan kalıpları da ayrıca tanıklar. Bu nedenle dal kimliği korunabilir, ancak kalıba bağlı nitelemeler temel gece anlamıyla bir tutulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"gündüzün karşıtı olan gece"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"gece karanlığı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tek bir gece"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"geceler"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"geceler"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"geceler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"çok karanlık ve çetin gece"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"çok karanlık gece"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"uzun ya da şiddeti pekiştirilmiş gece"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ayın en karanlık ve son gecesi"}],"lexicalization_note":"Dal hem genel gece adını hem de yalnız belirli söz öbeklerinde ortaya çıkan karanlık, zorluk, uzunluk ve ay sonu nitelemelerini içerir; tanım bu iki düzeyi ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece, geceleyin eylem, bugüne bağlı gece, yoğunlaşan karanlık ve adlandırma arasındaki sınırı en açık gösteren dört komşu seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal gecenin kendisini ve karanlığını gösterir; komşu dal ise geceyi bir eylemin gerçekleşme zamanı veya yönü olarak kodlar.","focus_only":"Geceyi bir zaman bölümü ve karanlık olarak adlandırır.","gloss":"gece ile geceleyin yapılan iş arasındaki ayrım","neighbor_only":"Geceye girme, geceleyin işlem yapma veya gece yol alma eylemlerini anlatır.","neighbor_ref":"root_001392/B002","relation_type":"same_field","shared_zone":"Her iki dal da geceyi zaman bakımından ortak eksen olarak kullanır."},{"boundary_match":"partial","distinction":"Bu dalda bugüne göre yakınlık zorunlu değildir; komşu dalın anlamı konuşma gününe ve gün içindeki söyleme anına bağlı bir gece seçimi gerektirir.","focus_only":"Herhangi bir geceyi genel zaman türü olarak kapsar.","gloss":"genel gece ile bugüne bağlı gece arasındaki ayrım","neighbor_only":"Konuşma gününe göre en yakın, geçen veya girilecek geceyi seçer.","neighbor_ref":"root_001392/B003","relation_type":"near_neighbor","shared_zone":"İki dal da gece zamanını gösterir ve belirli bağlamlarda aynı zaman dilimine işaret edebilir."},{"boundary_match":"partial","distinction":"Bu dal geceyi veya mevcut karanlığını adlandırabilir; komşu dal ise karanlığın şiddetlenmesi durumunu öne çıkarır ve genel gece adı yerine geçmez.","focus_only":"Gece zamanını, karanlığını ve bazı kalıplarda yoğun karanlık niteliğini kapsar.","gloss":"gece karanlığı ile karanlığın şiddetlenmesi arasındaki ayrım","neighbor_only":"Gecenin giderek koyulaşmasını veya karanlığının şiddetlenmesini merkez alır.","neighbor_ref":"root_001015/B004","relation_type":"near_neighbor","shared_zone":"Her ikisi de gecenin yoğun karanlığını anlatan bağlamlarda buluşur."},{"boundary_match":"thematic_only","distinction":"Bu dalın çekirdeği bir zaman bölümü ve karanlıktır; komşu dalda biçim bir kişiyi adlandırır veya daha geniş bir söz öbeği içinde şarabı örtülü biçimde anar.","focus_only":"Gece zamanını ve onun karanlığını anlatır.","gloss":"gece anlamı ile adlandırma kullanımı arasındaki ayrım","neighbor_only":"Bir kadın adını ve ayrı bir söz öbeğinde şarabın örtülü adını anlatır.","neighbor_ref":"root_001392/B004","relation_type":"thematic","shared_zone":"Dallar aynı biçim ailesiyle bağlantılıdır, fakat kavramsal alanları örtüşmez."}],"source_phrase_ar":"الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)","source_summary":"Kaynakların ortak çekirdeği geceyi gündüzün karşıtı bir zaman ve ona bağlı karanlık olarak tanımlar. Toplu kanıt ayrıca tek ve çok gece biçimlerini, karanlığı ya da uzunluğu pekiştiren kullanımları ve ayın en karanlık son gecesine özgü ifadeyi birlikte gösterir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الليل والليلة والليالي، وضده النهار، وظلام الليل وشدته وطوله في نحو ليلة ليلاء وليل أليل وليل لائل وليلة ليلى","what_is_not_ar":"لا يدخل فيه النهار ولا اليوم إلا من جهة المقابلة، ولا التسمية بليلى، ولا ولد الطائر المختلف فيه"},"support_links":["sup_3993560859560d7e1c34","sup_44dddc7785b037632ef0","sup_5d9251092f03fba7b9dd","sup_b9f9f9502109324eb98c","sup_be953e6fe08f22a2b8a8"]},{"boundary":"Dal gecenin kendisini değil, geceye geçişi veya geceyi zaman ve yön olarak alan işlem ile yolculuk kullanımlarını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001392/B002","candidate_links":[{"candidate_id":"cand_90f1d9915b840660e983","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:2:1:2","qac_word_ref":"89:2:1","surface_ar":"لَيَالٍ"}],"gloss":"geceye girme ya da geceleyin iş görüp yol alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş veya karşılıklı işlem, gündüz yerine geceye göre yürütülür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zaman akışı içinde geceye girme veya gece vaktine ulaşma anlatılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Geceleyin yol alan veya gece yolculuğuna dayanabilen kişi anlatılır."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın geceye geçiş, geceye göre işlem ve gece yolculuğu alt görünümlerini birlikte açıklayan üst karşılıktır.","boundary_detail":"Dal gecenin kendisini değil, geceye geçişi veya geceyi zaman ve yön olarak alan işlem ile yolculuk kullanımlarını kapsar.","branch_image_ar":"مزاولة الأمر في الليل","concept_gloss":"geceye girme ya da geceleyin iş görüp yol alma","contextual_glosses":[{"applicability":"Bir işlemin gündüze göre yapılan benzeriyle karşılaştırılarak gece üzerinden yürütüldüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı işlemin özellikle geceye göre yürütülmesini korur."},"facet_ids":["F001"],"text":"geceye göre karşılıklı işlem yapmak","usage_role":"contextual"},{"applicability":"Bir kişinin veya durumun gece vaktine ulaştığını bildiren kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gündüzden gece vaktine geçiş ilişkisini doğrudan korur."},"facet_ids":["F002"],"text":"geceye girmek","usage_role":"contextual"},{"applicability":"Gece yolculuğu yapan veya böyle bir yolculuğa dayanabilen kişinin anlatıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gece yolculuğu yapan kişiyi ve bu yolculuğa güç yetirme koşulunu korur."},"facet_ids":["F003"],"text":"gece yol alan kimse","usage_role":"contextual"}],"definition":"Geceye girmek ya da bir işi, karşılıklı işlemi veya yolculuğu geceyi zaman ve yön olarak alarak gerçekleştirmektir. Gece yolculuğuna dayanabilen kişi de bu eylem alanına bağlı olarak adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş veya karşılıklı işlem, gündüz yerine geceye göre yürütülür."},{"facet_id":"F002","role":"core","statement":"Zaman akışı içinde geceye girme veya gece vaktine ulaşma anlatılır."},{"facet_id":"F003","role":"specialization","statement":"Geceleyin yol alan veya gece yolculuğuna dayanabilen kişi anlatılır."}],"identity_rationale":"Kaynak ifadesi geceyi yalın bir zaman adı olarak değil, karşılıklı bir işlemin geceye göre yapılması, geceye girilmesi ve gece yolculuğu yapılması ya da buna güç yetirilmesi üzerinden verir. Geçici dal çerçevesi bu ortak eylem yönelimini doğru yakalar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"geceye göre karşılıklı işlem yapma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"geceye girmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"gece yol alan veya gece yolculuğuna dayanabilen kimse"}],"lexicalization_note":"Anlam yalnız türemiş biçimlerde ve belirli kullanım kalıplarında tanıklanır; karşılıklı işlem, geceye giriş ve gece yolculuğu ayrı alt görünümler olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece anlamı ile gece yolculuğunun bağımsız, zorlu veya gündüzden geceye kesintisiz türleri en yararlı dört karşılaştırmayı verdi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dalda gece, girişin, işlemin veya yolculuğun yönünü belirler; komşu dalda ise eylem değil, doğrudan zaman bölümü ve karanlık adlandırılır.","focus_only":"Geceye girme veya geceyi bir eylemin zamanı olarak kullanma anlamlarını taşır.","gloss":"geceleyin eylem ile gece zamanının ayrımı","neighbor_only":"Gece zamanını ve ona bağlı karanlığı adlandırır.","neighbor_ref":"root_001392/B001","relation_type":"same_field","shared_zone":"Her iki dalın ortak zaman ekseni gecedir."},{"boundary_match":"partial","distinction":"Bu dalın yolculuk görünümü yanında geceye giriş ve işlem anlamları vardır; komşu dal ise gece yolculuğunu kendi başına merkezî bir hareket alanı olarak kurar.","focus_only":"Geceye giriş ve geceye göre karşılıklı işlem yapma anlamlarını da kapsar.","gloss":"geniş gece eylemi ile gece yolculuğu arasındaki ayrım","neighbor_only":"Gece yolculuğunu bağımsız bir hareket olarak ve yol alan topluluğu da kapsayacak biçimde merkezleştirir.","neighbor_ref":"root_000702/B001","relation_type":"near_neighbor","shared_zone":"İki dal geceleyin yol alma anlamında belirgin biçimde örtüşür."},{"boundary_match":"partial","distinction":"Bu dal için sürekli çaba ve güçlük kurucu değildir; komşu dal gece boyunca ısrarlı ilerlemeyi ve yolculuğun zahmetini anlamın merkezine alır.","focus_only":"Geceyle bağlantılı işlemi, geçişi ve olağan yolculuk yetisini kapsar.","gloss":"gece yol alma ile gece boyunca çabalayarak ilerleme ayrımı","neighbor_only":"Gece boyunca yolculuğu sürdürme ve bunun güçlüğüne katlanma yönünü özellikle öne çıkarır.","neighbor_ref":"root_001422/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal gece yolculuğu ve bu yolculuğa dayanma alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dalda gündüzden geceye kesintisiz devam şartı yoktur; komşu dalın ayırt edici sınırı, yolculuğun bir gündüz ile bir gece boyunca sürdürülmesidir.","focus_only":"Eylemin yalnız geceye göre yapılmasını veya geceye girilmesini anlatabilir.","gloss":"geceye bağlı eylem ile kesintisiz gündüz gece yolculuğu ayrımı","neighbor_only":"Yolculuğun gündüz ile gece arasında kesintisiz sürdürülmesini zorunlu kılar.","neighbor_ref":"root_001670/B006","relation_type":"near_neighbor","shared_zone":"İki dalın kesişiminde gece boyunca yol alma bulunur."}],"source_phrase_ar":"عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)","source_summary":"Toplu kanıt geceye göre yapılan karşılıklı işlemi, gece vaktine girmeyi ve gece yolculuğu yapabilen kişiyi aynı eylem alanında birleştirir. Bu kullanımların hiçbiri yalın gece zamanını tek başına adlandırmaz.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الفعل أو المعاملة على جهة الليل، مثل الملايلة، والدخول في الليل، والسير أو السرى في الليل","what_is_not_ar":"لا يدخل فيه اسم الليل نفسه ولا الليلة بوصفها زمنا مجردا"},"support_links":["sup_f2a570e4fb54e4c414db"]},{"boundary":"Dal yalnız konuşma gününe göre belirlenen en yakın geceyi kapsar; yönelim, cümlenin zamanı ve gün içindeki söyleme anına göre geçmişe veya geleceğe dönebilir.","branch_kind":"non_bare","branch_ref":"root_001392/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:2:1:2","qac_word_ref":"89:2:1","surface_ar":"لَيَالٍ"}],"gloss":"bugüne göre belirlenen en yakın gece","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gece, konuşmacının içinde bulunduğu güne göre en yakın gece olarak belirlenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gündüz söylenen ileri yönelimli kullanım, konuşmacının gireceği yaklaşan geceyi gösterir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tamamlanmış bir eylem günün ilk yarısında anlatılırken ifade önceki geceye dönebilir; gün ilerleyince geçmiş gece için başka bir zaman sözü seçilir."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Geçmiş veya gelecek yönelimi cümle bağlamından anlaşılan, konuşma gününe en yakın geceyi üst düzeyde karşılar.","boundary_detail":"Dal yalnız konuşma gününe göre belirlenen en yakın geceyi kapsar; yönelim, cümlenin zamanı ve gün içindeki söyleme anına göre geçmişe veya geleceğe dönebilir.","branch_image_ar":"الليلة القريبة من اليوم","concept_gloss":"bugüne göre belirlenen en yakın gece","contextual_glosses":[{"applicability":"Gündüz söylenip konuşmacının gireceği yaklaşan geceye yönelen bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşma gününe en yakın yaklaşan gece yönelimini korur."},"facet_ids":["F001","F002"],"text":"bu gece","usage_role":"contextual"},{"applicability":"Günün ilk yarısında tamamlanmış bir eylemi en yakın önceki geceye bağlayan Türkçe anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tamamlanmış eylemin konuşma gününden önceki en yakın geceye bağlanmasını korur."},"facet_ids":["F001","F003"],"text":"dün gece","usage_role":"contextual"}],"definition":"Konuşma gününe en yakın olan ve bağlama göre bir önceki ya da girilecek olan gecedir. Geçmiş bir eylem anlatılırken günün ilk yarısında önceki geceyi gösterebilir; gündüzden yaklaşan gece anlatılırken sonraki geceyi seçer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gece, konuşmacının içinde bulunduğu güne göre en yakın gece olarak belirlenir."},{"facet_id":"F002","role":"specialization","statement":"Gündüz söylenen ileri yönelimli kullanım, konuşmacının gireceği yaklaşan geceyi gösterir."},{"facet_id":"F003","role":"specialization","statement":"Tamamlanmış bir eylem günün ilk yarısında anlatılırken ifade önceki geceye dönebilir; gün ilerleyince geçmiş gece için başka bir zaman sözü seçilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Bugünle ilişkisi bulunmayan herhangi bir geceyi de kapsar.","collision":null,"fit":"broadening","loses":"Konuşma gününe göre yakınlık ve bağlama bağlı zaman yönelimini belirtmez.","preserves":"Gece zamanına yapılan temel gönderimi korur."},"text":"gece"}],"identity_rationale":"Kaynak ifadesi, genel gece türünü değil konuşma gününe en yakın geceyi seçen bağlamsal bir kullanımı açıkça tanımlar. Gündüz konuşulurken girilecek geceye yönelim ile günün ilk yarısında tamamlanmış bir eylemin önceki geceye bağlanması, geçici çerçevede belirtilen yakınlık ve söyleme zamanı sınırını doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece"}],"lexicalization_note":"Anlam belirli bir gece ifadesinin konuşma gününe göre yorumlanmasına bağlıdır; genel ve bağlamsız gece anlamına genişletilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece, geceleyin eylem, ertesi gün ve bitişik zaman sınırı karşılaştırmaları dalın bugüne bağlı gönderimini en açık biçimde ayırdı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın gönderimi konuşma gününe göre hesaplanır; komşu dal genel gece adıdır ve bugüne yakınlık, söyleme anı veya geçmiş gelecek yönelimi gerektirmez.","focus_only":"Konuşma gününe en yakın geceyi ve bağlama bağlı geçmiş ya da gelecek yönelimini zorunlu kılar.","gloss":"bugüne en yakın gece ile genel gece arasındaki ayrım","neighbor_only":"Herhangi bir geceyi, geceleri ve gece karanlığını bağlamsız olarak kapsayabilir.","neighbor_ref":"root_001392/B001","relation_type":"near_synonym","shared_zone":"İki dal da tek bir gece zamanını gösterebilir ve uygun bağlamda aynı zaman aralığına işaret edebilir."},{"boundary_match":"field_only","distinction":"Bu dalın çekirdeği bağlam içinde seçilen gecedir; komşu dalda gece bir geçişin, işlemin veya yolculuğun gerçekleşme zamanı ve yönüdür.","focus_only":"Bugüne göre seçilen belirli bir gece zamanını gösterir.","gloss":"yakın gece göndergesi ile geceleyin eylem arasındaki ayrım","neighbor_only":"Geceye girme, geceleyin işlem yapma veya gece yolculuğu gerçekleştirme eylemini gösterir.","neighbor_ref":"root_001392/B002","relation_type":"same_field","shared_zone":"Her iki dal da geceyi konuşma veya eylem için zaman çerçevesi yapar."},{"boundary_match":"field_only","distinction":"Bu dal geceyi seçer ve yönelimi bağlama göre değişebilir; komşu dal ise gün birimini seçer ve zorunlu olarak konuşma gününün sonrasına yönelir.","focus_only":"Bugüne komşu geceyi, cümle yönelimine göre geçmişte veya gelecekte seçebilir.","gloss":"en yakın gece ile ertesi gün arasındaki ayrım","neighbor_only":"Yalnız konuşma gününden sonraki günü, yani gelecek gündüzlü zaman birimini seçer.","neighbor_ref":"root_001076/B002","relation_type":"same_field","shared_zone":"İki dal da konuşma gününü merkez alan yakın zaman ifadeleridir."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir gece göndergesini seçer; komşu dal ise geceyi seçmekten çok iki zaman bölümünün birbirine değen başlangıç veya bitiş sınırını adlandırır.","focus_only":"Konuşma gününe göre en yakın gecenin hangisi olduğunu belirler.","gloss":"yakın gece seçimi ile zaman sınırı arasındaki ayrım","neighbor_only":"Bir zaman parçasının başlangıç veya bitiş sınırında başka bir zamanla karşı karşıya gelmesini anlatır.","neighbor_ref":"root_001479/B006","relation_type":"same_field","shared_zone":"Her ikisi de komşu zaman parçaları arasındaki ilişkiyi konu eder."}],"source_phrase_ar":"إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, günün ilk yarısında tamamlanmış bir eylem için önceki gecenin bu ifadeyle anılabildiğini, gün ilerleyince başka bir geçmiş zaman sözünün seçildiğini ve gündüzden bakıldığında yaklaşan gecenin de aynı yakınlık ilkesiyle belirlendiğini bildirir."}],"source_summary":"Kanıt, bu kullanımın genel gece adından farklı olarak konuşma gününe ve gün içindeki söyleme anına göre çözüldüğünü gösterir. Yaklaşan gece ile henüz yakın geçmiş sayılan önceki gece, cümlenin yönelimine göre ayrılır.","sources":["TA"],"what_is_ar":"يدخل فيه إطلاق الليلة على أقرب الليالي من اليوم أو على الليلة الداخلة، والفصل بينها وبين البارحة بحسب وقت الكلام","what_is_not_ar":"لا يدخل فيه مطلق الليل ولا الليالي المجموعة ولا أوصاف شدة الظلمة"},"support_links":[]},{"boundary":"Kadın adı temel adlandırma kullanımıdır; şarap anlamı yalnız ayrı ve tam bir söz öbeğinin örtülü ad işlevine aittir.","branch_kind":"non_bare","branch_ref":"root_001392/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:2:1:2","qac_word_ref":"89:2:1","surface_ar":"لَيَالٍ"}],"gloss":"bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz konusu biçim bir kadını adlandıran kişi adı olarak kullanılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu adı içeren ayrı bir söz öbeği, şarabı doğrudan söylemeden anan örtülü bir ad olarak kullanılır."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kişi adı çekirdeğini ve yalnız tam söz öbeğine bağlı şarap adlandırmasını sınırlarıyla birlikte açıklar.","boundary_detail":"Kadın adı temel adlandırma kullanımıdır; şarap anlamı yalnız ayrı ve tam bir söz öbeğinin örtülü ad işlevine aittir.","branch_image_ar":"التسمية بليلى","concept_gloss":"bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı","contextual_glosses":[{"applicability":"Biçimin bir kadını adlandırdığı kişi adı kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Biçimin kadın kişi adı olma işlevini korur."},"facet_ids":["F001"],"text":"bir kadın adı","usage_role":"contextual"},{"applicability":"Yalnız kadın adını içeren tam söz öbeğinin şarabı dolaylı biçimde andığı kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tam söz öbeğinin şarabı örterek adlandırma işlevini korur."},"facet_ids":["F002"],"text":"şarap için kullanılan örtülü ad","usage_role":"contextual"}],"definition":"Bir biçimin kadın adı olarak kullanılmasıdır; aynı adı içeren ayrı bir söz öbeği ise şarabı anan örtülü bir ad işlevi görür. İki kullanım aynı dalda bulunsa da kadın adı ile içki anlamı birbirine eşit değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz konusu biçim bir kadını adlandıran kişi adı olarak kullanılır."},{"facet_id":"F002","role":"associated_use","statement":"Bu adı içeren ayrı bir söz öbeği, şarabı doğrudan söylemeden anan örtülü bir ad olarak kullanılır."}],"identity_rationale":"Kaynak ifadesi bir biçimin kadın adı olduğunu ve bu adı içeren ayrı bir söz öbeğinin şarabı örtülü biçimde anlattığını doğrular. Dal bir adlandırma kümesi olarak korunabilir; ancak kadın adının kendi başına şarap anlamına geldiği sanılmamalı, şarap anlamı yalnız tam söz öbeğine bağlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bir kadın adı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"şarap için kullanılan örtülü ad"}],"lexicalization_note":"Dal yalnız ad olarak kullanılan biçimi ve şarabı anan tam söz öbeğini kapsar; bunlar genel gece veya karanlık anlamına genişletilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece dalı ile iki ayrı kişi adı dalı, adlandırma işlevini biçimsel yakınlıktan ve farklı ad kimliklerinden ayırmak için seçildi.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Bu dalın anlamı kişi ve içki adlandırmasıdır; komşu dal ise bir zaman bölümünü ve karanlığı gösterir, dolayısıyla iki dal olağan kullanımda birbirinin yerine geçmez.","focus_only":"Bir kadın adını ve ayrı bir söz öbeğinde şarabın örtülü adını kapsar.","gloss":"adlandırma ile gece anlamı arasındaki ayrım","neighbor_only":"Gece zamanını ve gece karanlığını anlatır.","neighbor_ref":"root_001392/B001","relation_type":"thematic","shared_zone":"Dallar aynı biçim ailesiyle bağlantılıdır, fakat yalnız tarihsel ve biçimsel bir çağrışım paylaşır."},{"boundary_match":"field_only","distinction":"Adlandırma işlevleri aynı alandadır, fakat adların kimlikleri ayrıdır; ayrıca bu dalda belirli bir söz öbeğine bağlı şarap kullanımı bulunur.","focus_only":"Farklı bir kadın adını ve bu adı içeren örtülü şarap sözünü kapsar.","gloss":"iki ayrı kadın adının anlam alanı","neighbor_only":"Başka ve ayrı bir kadın adını kapsar.","neighbor_ref":"root_000848/B009","relation_type":"same_field","shared_zone":"Her iki dal da bir biçimin kadın kişi adı olarak kullanılmasını tanıklar."},{"boundary_match":"field_only","distinction":"Ortak alan adlandırmadır; ancak gösterilen adlar farklıdır ve komşu dalın erkek adı ile lakap kapsamı bu dalda bulunmaz, bu dalın şarap söz öbeği de komşuda yoktur.","focus_only":"Bir kadın adı ile ona bağlı örtülü şarap sözünü içerir.","gloss":"ayrı kişi adları ve lakaplar alanı","neighbor_only":"Başka biçimlerin erkek adı, kadın adı veya lakap olarak kullanılmasını içerir.","neighbor_ref":"root_000799/B007","relation_type":"same_field","shared_zone":"İki dal da sözlük biçimlerinin kişi adı olarak aktarılmasını konu eder."}],"source_phrase_ar":"وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)","source_summary":"Toplu kanıt kadın adı kullanımını ortak biçimde destekler ve ayrıca bu adı içeren tam bir söz öbeğinin şarabı örten bir ad olduğunu bildirir. İkinci kullanım bağımsız söz öbeğine bağlı tutulmalıdır.","sources":["JA","SI","TA"],"what_is_ar":"يدخل فيه ليلى اسما لامرأة، وأم ليلى كنية للخمر","what_is_not_ar":"لا يدخل فيه الليل زمنا ولا الظلمة ولا المعاملة بالليل"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["89:2:1"],"branch_refs":[],"candidate_id":"cand_9f53ea2c9e83d9c02ab3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:2:1:boundary-and-oath-beat","source_type":"word_analysis","support_ids":["sup_349d018fb410ec4fcb6b","sup_8db18c6f03112aec89af"],"title":"boundary and oath beat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:1","qac_refs":["89:2:1:1"],"status":"accepted"}},{"anchor_refs":["89:2:1"],"branch_refs":[],"candidate_id":"cand_95d3c64fa98d509eafd2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:2:1:compressed-verbless-oath","source_type":"word_analysis","support_ids":["sup_2decaeb4f7f20a46b786","sup_8db18c6f03112aec89af"],"title":"compressed verbless oath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:1","qac_refs":["89:2:1:1"],"status":"accepted"}},{"anchor_refs":["89:2:1"],"branch_refs":[],"candidate_id":"cand_1a0832ed2c51a76a533d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:2:1:oath-governance-and-coordination","source_type":"word_analysis","support_ids":["sup_8db18c6f03112aec89af","sup_9f5ce5dff0774e03dba3"],"title":"oath governance and coordination","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:1","qac_refs":["89:2:1:1"],"status":"accepted"}},{"anchor_refs":["89:2:1"],"branch_refs":[],"candidate_id":"cand_061f6588b9663318beb4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:2:1:recitational-onset","source_type":"word_analysis","support_ids":["sup_551ef401edbd319c949d","sup_8db18c6f03112aec89af"],"title":"repeated open onset","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:1","qac_refs":["89:2:1:1"],"status":"accepted"}},{"anchor_refs":["89:2:2"],"branch_refs":[],"candidate_id":"cand_ea46f39cedd266de90cb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:2:2:cadence-and-soft-extension","source_type":"word_analysis","support_ids":["sup_924255c8db22f7d7f01f","sup_de1074cbb4bb302c0c0b"],"title":"soft extension and paired cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:2","qac_refs":["89:2:1:2"],"status":"accepted"}},{"anchor_refs":["89:2:2"],"branch_refs":[],"candidate_id":"cand_19889561c2acd2a17574","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:2:2:countable-night-head","source_type":"word_analysis","support_ids":["sup_906d09cdf2d8c77bdbfa","sup_de1074cbb4bb302c0c0b"],"title":"night noun receives the count","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:2","qac_refs":["89:2:1:2"],"status":"accepted"}},{"anchor_refs":["89:2:2"],"branch_refs":[],"candidate_id":"cand_6b0974f361de135f45a3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:2:2:indefinite-oath-object","source_type":"word_analysis","support_ids":["sup_27d24ed09e97b9e1cd39","sup_de1074cbb4bb302c0c0b"],"title":"unnamed nights under oath scope","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:2","qac_refs":["89:2:1:2"],"status":"accepted"}},{"anchor_refs":["89:2:2"],"branch_refs":[],"candidate_id":"cand_cb11eb07323d82415285","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:2:2:inter-ayah-night-field","source_type":"word_analysis","support_ids":["sup_10f21c8c2909a387dc1d","sup_de1074cbb4bb302c0c0b"],"title":"counted-night echoes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:2","qac_refs":["89:2:1:2"],"status":"accepted"}},{"anchor_refs":["89:2:2"],"branch_refs":[],"candidate_id":"cand_9c6606236005d2997f38","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:2:2:marked-plural-form","source_type":"word_analysis","support_ids":["sup_4e48912320e019549c4a","sup_de1074cbb4bb302c0c0b"],"title":"marked plural form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:2","qac_refs":["89:2:1:2"],"status":"accepted"}},{"anchor_refs":["89:2:2"],"branch_refs":[],"candidate_id":"cand_951fd6100fd5ceb2e84b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:2:2:night-darkness-as-repeated-interval","source_type":"word_analysis","support_ids":["sup_2b86012ae106f2a27d85","sup_de1074cbb4bb302c0c0b"],"title":"darkness made countable","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:2","qac_refs":["89:2:1:2"],"status":"accepted"}},{"anchor_refs":["89:2:2"],"branch_refs":[],"candidate_id":"cand_0f8702ffc49c92e9bd4c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:2:2:oath-sequence-bridge","source_type":"word_analysis","support_ids":["sup_74e0105645dde39dbc6c","sup_de1074cbb4bb302c0c0b"],"title":"from dawn point to night span","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:2","qac_refs":["89:2:1:2"],"status":"accepted"}},{"anchor_refs":["89:2:3"],"branch_refs":[],"candidate_id":"cand_c572a136b416d4b0e6d4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001016"],"scope":"focus_ayah","source_local_id":"89:2:3:exact-count-and-completion","source_type":"word_analysis","support_ids":["sup_a9193bc8c75ba7c46efc","sup_aacab509ad02070ab116"],"title":"exact ten with completion pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:3","qac_refs":["89:2:2:1"],"status":"accepted"}},{"anchor_refs":["89:2:3"],"branch_refs":[],"candidate_id":"cand_526035c4c857a81e4f6b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001016"],"scope":"focus_ayah","source_local_id":"89:2:3:final-measure-closure","source_type":"word_analysis","support_ids":["sup_a9193bc8c75ba7c46efc","sup_f1d5de3e1ee20a31e532"],"title":"measure arrives as closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:3","qac_refs":["89:2:2:1"],"status":"accepted"}},{"anchor_refs":["89:2:3"],"branch_refs":[],"candidate_id":"cand_3eb0458fdbb2da377512","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001016"],"scope":"focus_ayah","source_local_id":"89:2:3:fraction-fullness-contrast","source_type":"word_analysis","support_ids":["sup_06c1a7595a1dd3a9b2d8","sup_a9193bc8c75ba7c46efc"],"title":"fraction contrast becomes fullness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:3","qac_refs":["89:2:2:1"],"status":"accepted"}},{"anchor_refs":["89:2:3"],"branch_refs":[],"candidate_id":"cand_385b03a312e6086b2307","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001016"],"scope":"focus_ayah","source_local_id":"89:2:3:night-count-and-parity-field","source_type":"word_analysis","support_ids":["sup_a9193bc8c75ba7c46efc","sup_c1e65bf2d219f26d0d2c"],"title":"night-count and parity field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:3","qac_refs":["89:2:2:1"],"status":"accepted"}},{"anchor_refs":["89:2:3"],"branch_refs":[],"candidate_id":"cand_50e411d314fc9bcdbbad","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001016"],"scope":"focus_ayah","source_local_id":"89:2:3:numeral-qualifier","source_type":"word_analysis","support_ids":["sup_907e1f33b0c40201c9a2","sup_a9193bc8c75ba7c46efc"],"title":"genitive numeral qualifier","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:3","qac_refs":["89:2:2:1"],"status":"accepted"}},{"anchor_refs":["89:2:3"],"branch_refs":[],"candidate_id":"cand_65383d40e3c1d0710e4b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001016"],"scope":"focus_ayah","source_local_id":"89:2:3:sound-and-visible-ending","source_type":"word_analysis","support_ids":["sup_860056727ebb3f707feb","sup_a9193bc8c75ba7c46efc"],"title":"visible and audible ending","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:2:3","qac_refs":["89:2:2:1"],"status":"accepted"}},{"anchor_refs":["89:2:1"],"branch_refs":[],"candidate_id":"cand_0d00443d8427a6119ed4","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:2:1:2","source_type":"qac_morpheme","support_ids":["sup_e1520981fa93d703b0f0"],"title":"QAC root occurrence: ل ي ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:2:2"],"branch_refs":[],"candidate_id":"cand_0c39a182fa0e3a12e332","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001016"],"scope":"focus_ayah","source_local_id":"89:2:2:1","source_type":"qac_morpheme","support_ids":["sup_00883e72893702516eee"],"title":"QAC root occurrence: ع ش ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:2","branch_refs":["root_001016/B001","root_001392/B001"],"candidate_id":"cand_46c2cc47efe07d2c117e","commentary_obligation":"review","hft_ref":"hft_4ae013ec4224d00052fe","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_counted_darkness","source_type":"hft","support_ids":["sup_44dddc7785b037632ef0"],"title":"baseline_counted_darkness","trust":"legacy_unbound"},{"anchor_refs":["89:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:2","branch_refs":["root_001016/B002","root_001392/B001"],"candidate_id":"cand_809bd424b88544b7c33f","commentary_obligation":"review","hft_ref":"hft_dc70251a233a119316e3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_tenth_closure","source_type":"hft","support_ids":["sup_5d9251092f03fba7b9dd"],"title":"baseline_tenth_closure","trust":"legacy_unbound"},{"anchor_refs":["89:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:2","branch_refs":["root_001016/B001","root_001392/B002"],"candidate_id":"cand_90f1d9915b840660e983","commentary_obligation":"review","hft_ref":"hft_291b366ba6e9501ba07b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_nightwork_iterations","source_type":"hft","support_ids":["sup_f2a570e4fb54e4c414db"],"title":"baseline_nightwork_iterations","trust":"legacy_unbound"},{"anchor_refs":["89:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:2","branch_refs":["root_001016/B003","root_001016/B004","root_001392/B001"],"candidate_id":"cand_40afa86f1401f728fb8e","commentary_obligation":"review","hft_ref":"hft_79e9e7e44e4f17c2841d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_apportionable_time","source_type":"hft","support_ids":["sup_be953e6fe08f22a2b8a8"],"title":"baseline_apportionable_time","trust":"legacy_unbound"},{"anchor_refs":["89:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:2","branch_refs":["root_001016/B007","root_001392/B001"],"candidate_id":"cand_6903c6a189fa549479a1","commentary_obligation":"review","hft_ref":"hft_1ab12b95c70ff36e33b5","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_near_delivery_count","source_type":"hft","support_ids":["sup_3993560859560d7e1c34"],"title":"baseline_near_delivery_count","trust":"legacy_unbound"},{"anchor_refs":["89:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:2","branch_refs":["root_001016/B012","root_001016/B013","root_001392/B001"],"candidate_id":"cand_379e070e1a67a84d2312","commentary_obligation":"review","hft_ref":"hft_ac0c32b17c47c7d3020a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_night_company","source_type":"hft","support_ids":["sup_b9f9f9502109324eb98c"],"title":"baseline_night_company","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَلَيَالٍ عَشْرٍۢ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:2:1:1","qac_word_ref":"89:2:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:2:1:2","qac_word_ref":"89:2:1","root_ar":"ل ي ل","surface_ar":"لَيَالٍ"},{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","root_ar":"ع ش ر","surface_ar":"عَشْرٍ"}],"word_analysis_qac_refs":[["89:2:1:1"],["89:2:1:2"],["89:2:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:2:1","89:2:2","89:2:3"]},"focus_surface_evidence":{"arabic_uthmani":"وَلَيَالٍ عَشْرٍۢ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:2:1:1","qac_word_ref":"89:2:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:2:1:2","qac_word_ref":"89:2:1","root_ar":"ل ي ل","surface_ar":"لَيَالٍ"},{"lemma_ar":"عَشْر","morph_features":"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:2:2:1","qac_word_ref":"89:2:2","root_ar":"ع ش ر","surface_ar":"عَشْرٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:2:1:1"],["89:2:1:2"],["89:2:2:1"]],"word_analysis_refs":["89:2:1","89:2:2","89:2:3"],"word_rows":[{"analysis_record_ref":"89:2:1","analytic_gloss_range_en":"prefixed oath and coordination particle governing the following genitive oath object while carrying the ayah across the boundary from the previous oath","analytic_root_gloss_range_en":null,"qac_refs":["89:2:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"89:2:2","analytic_gloss_range_en":"indefinite plural night-units under oath scope, selected as repeated dark intervals that remain unnamed while the following numeral bounds them","analytic_root_gloss_range_en":"root range centers on night as the opposite of day and its darkness, with extensions for entering or doing something by night and naming material; this ayah selects countable nights as repeated dark spans, not deictic or naming branches","qac_refs":["89:2:1:2"],"root":{"arabic":"ل ي ل","transliteration":"l-y-l"},"surface":{"arabic":"لَيَالٍ","transliteration":"layālin"}},{"analysis_record_ref":"89:2:3","analytic_gloss_range_en":"indefinite genitive cardinal ten functioning as the postposed numeral qualifier that bounds the preceding night plural and closes the oath phrase","analytic_root_gloss_range_en":"root range includes cardinal ten, becoming or making a tenth, tenth shares and tithing, grouping and association, and specialized lexical branches; this ayah selects cardinal ten with locally licensed completion and gathered-set pressure, not the specialized fraction, tithe, animal, plant, or naming branches","qac_refs":["89:2:2:1"],"root":{"arabic":"ع ش ر","transliteration":"ʿ-sh-r"},"surface":{"arabic":"عَشْرٍۢ","transliteration":"ʿashrin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":6,"assigned_records":[{"anchor_refs":["89:2"],"branch_refs":["root_001016/B001","root_001392/B001"],"candidate_id":"cand_46c2cc47efe07d2c117e","evidence_scope":"focus_ayah","hft_ref":"hft_4ae013ec4224d00052fe","item_id":"baseline_counted_darkness","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_counted_darkness","support_id":"sup_44dddc7785b037632ef0"},{"anchor_refs":["89:2"],"branch_refs":["root_001016/B002","root_001392/B001"],"candidate_id":"cand_809bd424b88544b7c33f","evidence_scope":"focus_ayah","hft_ref":"hft_dc70251a233a119316e3","item_id":"baseline_tenth_closure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_tenth_closure","support_id":"sup_5d9251092f03fba7b9dd"},{"anchor_refs":["89:2"],"branch_refs":["root_001016/B001","root_001392/B002"],"candidate_id":"cand_90f1d9915b840660e983","evidence_scope":"focus_ayah","hft_ref":"hft_291b366ba6e9501ba07b","item_id":"baseline_nightwork_iterations","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_nightwork_iterations","support_id":"sup_f2a570e4fb54e4c414db"},{"anchor_refs":["89:2"],"branch_refs":["root_001016/B003","root_001016/B004","root_001392/B001"],"candidate_id":"cand_40afa86f1401f728fb8e","evidence_scope":"focus_ayah","hft_ref":"hft_79e9e7e44e4f17c2841d","item_id":"baseline_apportionable_time","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_apportionable_time","support_id":"sup_be953e6fe08f22a2b8a8"},{"anchor_refs":["89:2"],"branch_refs":["root_001016/B007","root_001392/B001"],"candidate_id":"cand_6903c6a189fa549479a1","evidence_scope":"focus_ayah","hft_ref":"hft_1ab12b95c70ff36e33b5","item_id":"baseline_near_delivery_count","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_near_delivery_count","support_id":"sup_3993560859560d7e1c34"},{"anchor_refs":["89:2"],"branch_refs":["root_001016/B012","root_001016/B013","root_001392/B001"],"candidate_id":"cand_379e070e1a67a84d2312","evidence_scope":"focus_ayah","hft_ref":"hft_ac0c32b17c47c7d3020a","item_id":"baseline_night_company","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_night_company","support_id":"sup_b9f9f9502109324eb98c"}],"diagnostics":[],"lane_counts":{"global":16,"macro":2,"micro":6},"packet_summary":{"ayah_count":30,"focus_ref":"89:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"89:2","lane":"micro","linguistic_source_ref":"89:2","surface_ref":"89:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:2","target_tokens":[["On",["89:2:2"]],["geceye",["89:2:1"]],["andolsun",["89:2:1","89:2:2"]]],"text":"On geceye andolsun!"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":6,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":14,"id":"s089-p01-001-014","label":"Oaths and the downfall of tyrants","number":1,"refs":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:2:2:1","source_type":"qac_morpheme","support_id":"sup_00883e72893702516eee","text":"{\"lemma_ar\":\"عَشْر\",\"morph_features\":\"STEM|POS:ADJ|LEM:Ea$or|ROOT:E$r|MP|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"89:2:2:1\",\"qac_word_ref\":\"89:2:2\",\"root_ar\":\"ع ش ر\",\"surface_ar\":\"عَشْرٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:3:fraction-fullness-contrast","source_type":"word_analysis","support_id":"sup_06c1a7595a1dd3a9b2d8","text":"{\"blocking_evidence\":null,\"headline\":\"fraction contrast becomes fullness\",\"reader_payoff\":\"The reader notices the same root family can mark fractional diminishment in 34:45, while here the selected count moves toward completed fullness.\",\"reason\":\"The fraction branch is real in the root family, but local grammar selects cardinal ten; the 34:45 reference is retained as contrast, not as local fraction sense.\",\"representative_source_ids\":[\"QI-4be28253\",\"MI-65fd1064\",\"QI-2c79a856\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:2:inter-ayah-night-field","source_type":"word_analysis","support_id":"sup_10f21c8c2909a387dc1d","text":"{\"blocking_evidence\":null,\"headline\":\"counted-night echoes\",\"reader_payoff\":\"The reader notices that this counted night phrase sits in a Quranic night-field: active covering in 92:1, another ten-night frame in 7:142, and a same-surah shift to moving night in 89:4.\",\"reason\":\"The CRITICAL rows provide concrete references, and the local grammar allows them as echo and contrast without importing a narrative explanation into 89:2.\",\"representative_source_ids\":[\"QI-ebae4f47\",\"QI-feb1eee1\",\"QE-44dfbf02\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:2:indefinite-oath-object","source_type":"word_analysis","support_id":"sup_27d24ed09e97b9e1cd39","text":"{\"blocking_evidence\":null,\"headline\":\"unnamed nights under oath scope\",\"reader_payoff\":\"The reader notices that the oath gives the nights gravity while their indefiniteness withholds calendrical identification.\",\"reason\":\"The standard surface is plural, indefinite, and genitive under the oath particle; the nasal-ending-loss variant is useful as contrast, but it does not replace the standard indefinite reading.\",\"representative_source_ids\":[\"QG-36744be4\",\"QG-e6b8b1e4\",\"QF-feb07b59\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:2:night-darkness-as-repeated-interval","source_type":"word_analysis","support_id":"sup_2b86012ae106f2a27d85","text":"{\"blocking_evidence\":null,\"headline\":\"darkness made countable\",\"reader_payoff\":\"The reader notices that the word does not reduce night to arithmetic dates; it makes repeated dark intervals countable evidence.\",\"reason\":\"V4 supports night and darkness as the selected branch, while local plural counting excludes deictic, travel-by-night, and naming branches as governing the local sense.\",\"representative_source_ids\":[\"QS-10b5ab3b\",\"QS-8376d30b\",\"MS-d50d41f5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:1:compressed-verbless-oath","source_type":"word_analysis","support_id":"sup_2decaeb4f7f20a46b786","text":"{\"blocking_evidence\":null,\"headline\":\"compressed verbless oath\",\"reader_payoff\":\"The reader notices that the oath force is carried by particle governance and ellipsis, not by a local verb of swearing.\",\"reason\":\"Attachment evidence marks formulaic ellipsis before the governed noun, supporting the CRITICAL claim that the phrase remains compact rather than becoming a full verbal clause.\",\"representative_source_ids\":[\"QG-afc7b048\",\"QF-528ace21\",\"MT-45174bbf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:1:boundary-and-oath-beat","source_type":"word_analysis","support_id":"sup_349d018fb410ec4fcb6b","text":"{\"blocking_evidence\":null,\"headline\":\"boundary and oath beat\",\"reader_payoff\":\"The reader notices the ayah boundary as continuous: the same particle carries the scene from the dawn oath into the counted-night oath.\",\"reason\":\"The particle opens 89:2, links the oath object to 89:1, and fits the surrounding oath-chain window of 89:1-5.\",\"representative_source_ids\":[\"QT-133f11af\",\"QB-5dd6ef4f\",\"QY-edcd5a00\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:2:marked-plural-form","source_type":"word_analysis","support_id":"sup_4e48912320e019549c4a","text":"{\"blocking_evidence\":null,\"headline\":\"marked plural form\",\"reader_payoff\":\"The reader notices that a common root appears in a marked plural shape, making the sworn nights an exceptional counted set rather than ordinary night in general.\",\"reason\":\"The local noun is a plural indefinite genitive form; contextual data show the root is common, so the retained payoff is about the chosen plural silhouette rather than root rarity.\",\"representative_source_ids\":[\"QF-9dd78390\",\"QI-bd917664\",\"QH-97d3433c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:1:recitational-onset","source_type":"word_analysis","support_id":"sup_551ef401edbd319c949d","text":"{\"blocking_evidence\":null,\"headline\":\"repeated open onset\",\"reader_payoff\":\"The reader notices that the short opening sound makes the oath chain audible before the individual oath objects are parsed.\",\"reason\":\"The sound rows are compatible with the local particle and with the repeated particle openings around 89:2-3.\",\"representative_source_ids\":[\"QP-ca65e268\",\"QB-a3521cdb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:2:oath-sequence-bridge","source_type":"word_analysis","support_id":"sup_74e0105645dde39dbc6c","text":"{\"blocking_evidence\":null,\"headline\":\"from dawn point to night span\",\"reader_payoff\":\"The reader notices the oath sequence widening from a named dawn threshold in 89:1 to unnamed repeated nights in 89:2 before the next numerical field in 89:3.\",\"reason\":\"The ayah is linked to the oath chain in 89:1-5, and the local noun carries the shift in number, definiteness, and temporal scale.\",\"representative_source_ids\":[\"QB-0b071609\",\"QB-54ba59ac\",\"QY-cfa0bb7b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:3:sound-and-visible-ending","source_type":"word_analysis","support_id":"sup_860056727ebb3f707feb","text":"{\"blocking_evidence\":null,\"headline\":\"visible and audible ending\",\"reader_payoff\":\"The reader notices that the final nasalized ending and firmer sound texture make the numerical boundary perceptible as well as semantic.\",\"reason\":\"The sound and orthographic rows match the local final word and reinforce, rather than replace, the grammatical closure.\",\"representative_source_ids\":[\"QF-48238bbc\",\"QP-6dbdbb6f\",\"MP-e51f73d9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:1","source_type":"word_analysis","support_id":"sup_8db18c6f03112aec89af","text":"{\"gloss_range\":\"prefixed oath and coordination particle governing the following genitive oath object while carrying the ayah across the boundary from the previous oath\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) is doing more than adding another phrase. It governs {{ar:لَيَالٍ}} ({{tr:layālin}}) as a sworn-by object and coordinates it with the prior dawn oath in 89:1, so 89:2 enters as the next item in the same evidentiary inventory. Because the ayah has no finite verb, the particle carries the compressed oath architecture itself: the proof is invoked through governance, coordination, and ellipsis rather than narrated as an event. Its opening position also makes the boundary audible: the first move is a continuation marker before the listener reaches the night noun. That same small onset crosses from the dawn point into counted nights and prepares the repeated oath openings of 89:3, so the chain is heard before each object is parsed.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:2:countable-night-head","source_type":"word_analysis","support_id":"sup_906d09cdf2d8c77bdbfa","text":"{\"blocking_evidence\":null,\"headline\":\"night noun receives the count\",\"reader_payoff\":\"The reader notices that the nights remain the oath object and that the number bounds them afterward instead of taking over as the head of the phrase.\",\"reason\":\"Attachment evidence strongly licenses the following numeral as the qualifier of the night noun, preserving the noun-first movement from open plurality to exact closure.\",\"representative_source_ids\":[\"QG-4250ab3a\",\"QG-b25844a3\",\"QT-54dfe567\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:3:numeral-qualifier","source_type":"word_analysis","support_id":"sup_907e1f33b0c40201c9a2","text":"{\"blocking_evidence\":null,\"headline\":\"genitive numeral qualifier\",\"reader_payoff\":\"The reader notices that the number qualifies the nights from within the phrase, so night remains the sworn object while count supplies the limit.\",\"reason\":\"QAC and attachment evidence mark the word as a genitive numeral qualifying the preceding night noun, not a separate head or independent clause element.\",\"representative_source_ids\":[\"QG-418075ac\",\"QG-daf7b831\",\"QF-dd2b2d5d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:2:cadence-and-soft-extension","source_type":"word_analysis","support_id":"sup_924255c8db22f7d7f01f","text":"{\"blocking_evidence\":null,\"headline\":\"soft extension and paired cadence\",\"reader_payoff\":\"The reader notices that the word's extended sound and paired nasal ending let the open plural feel stretched before the count closes it.\",\"reason\":\"The phonetic rows match the local two-word phrase and remain secondary to the grammar of plural noun plus numeral.\",\"representative_source_ids\":[\"QP-c62224f6\",\"QP-d790d581\",\"MP-cec9accf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:1:oath-governance-and-coordination","source_type":"word_analysis","support_id":"sup_9f5ce5dff0774e03dba3","text":"{\"blocking_evidence\":null,\"headline\":\"oath governance and coordination\",\"reader_payoff\":\"The reader notices that the particle both makes the nights sworn evidence and joins them to the prior oath object, rather than merely adding a time phrase.\",\"reason\":\"The QAC row identifies a prefixed oath and coordination marker, and attachment evidence strongly licenses the following night noun as the particle's oath complement.\",\"representative_source_ids\":[\"QG-89f9c92c\",\"QG-b8089382\",\"QS-a331052b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:3","source_type":"word_analysis","support_id":"sup_a9193bc8c75ba7c46efc","text":"{\"gloss_range\":\"indefinite genitive cardinal ten functioning as the postposed numeral qualifier that bounds the preceding night plural and closes the oath phrase\",\"prose\":\"{{ar:عَشْرٍۢ}} ({{tr:ʿashrin}}) gives the phrase its final measure. It is genitive and indefinite with {{ar:لَيَالٍ}} ({{tr:layālin}}), so the number serves the night noun as a qualifier rather than replacing it as the oath object; its bare numeral form with a feminine plural also confirms that counted-noun relation from inside the phrase. The word supplies exact measure while still withholding which ten nights are meant, so the local sense is cardinal ten without turning the phrase into the known ten. Exact count replaces vague plurality, and the final position makes that exactness arrive as closure. The broader {{ar:ع ش ر}} ({{tr:ʿ-sh-r}}) family adds useful pressure only where it stays subordinate to that local count; association, tenth-stage arrival, and decimal organization make the nights feel like a gathered full set, while fraction or tithe branches remain outside the local construction. This is why the contrast with {{ar:مِعْشَار}} ({{tr:miʿshār}}) in 34:45 works as reversal from fraction to fullness rather than as the local sense. The number also pushes the oath sequence forward: the ten-night frame resonates with 7:142 and prepares the even-and-odd vocabulary of 89:3. As the last word, its written nasal marker, final cadence, and firmer sound texture make bounded measure both visible and audible.\",\"root_display\":\"{{ar:ع ش ر}} ({{tr:ʿ-sh-r}})\",\"root_gloss_range\":\"root range includes cardinal ten, becoming or making a tenth, tenth shares and tithing, grouping and association, and specialized lexical branches; this ayah selects cardinal ten with locally licensed completion and gathered-set pressure, not the specialized fraction, tithe, animal, plant, or naming branches\",\"surface_display\":\"{{ar:عَشْرٍۢ}} ({{tr:ʿashrin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:3:exact-count-and-completion","source_type":"word_analysis","support_id":"sup_aacab509ad02070ab116","text":"{\"blocking_evidence\":null,\"headline\":\"exact ten with completion pressure\",\"reader_payoff\":\"The reader notices that the numeral does more than say many: it completes the night-plural as an exact gathered set, while cardinal ten remains the selected local sense.\",\"reason\":\"V4 supports cardinal ten and related tenth-stage or grouping branches, but the local noun-number construction selects the cardinal count and keeps derivative stage, fraction, and association senses as pressure rather than governing senses.\",\"representative_source_ids\":[\"QS-0688f925\",\"QS-3bb490ae\",\"QS-7ebaced0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:3:night-count-and-parity-field","source_type":"word_analysis","support_id":"sup_c1e65bf2d219f26d0d2c","text":"{\"blocking_evidence\":null,\"headline\":\"night-count and parity field\",\"reader_payoff\":\"The reader notices that the number belongs to a larger numerical field: another ten-night surface in 7:142 and the even-and-odd categories in 89:3.\",\"reason\":\"The CRITICAL rows provide concrete references to 7:142 and 89:3; local grammar allows these as recurrence and sequence signals without importing a full narrative frame.\",\"representative_source_ids\":[\"QI-5128493c\",\"QE-aafba376\",\"QE-994f1c88\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:2","source_type":"word_analysis","support_id":"sup_de1074cbb4bb302c0c0b","text":"{\"gloss_range\":\"indefinite plural night-units under oath scope, selected as repeated dark intervals that remain unnamed while the following numeral bounds them\",\"prose\":\"{{ar:لَيَالٍ}} ({{tr:layālin}}) is the oath object, but it remains indefinite: the wording swears by nights without naming which nights. A no-nasal-ending variant pulls the phrase toward a construct-like \\\"nights of ten\\\" shape, which highlights how the standard wording keeps the noun indefinite and the numeral adjectival. Its broken plural form makes night appear as repeated units rather than one mass of darkness; the root is common, but this plural silhouette is marked, so the sworn nights feel like an exceptional counted set. The following {{ar:عَشْرٍۢ}} ({{tr:ʿashrin}}) closes that spread into a count, leaving the noun between solemn scope from the particle and exact measure from the numeral. Lexically, the selected range is still night and darkness, but the countable plural keeps concealment and duration together: repeated dark intervals become evidence. The same root-field is handled differently elsewhere, so the counted oath contrasts with active covering in 92:1, resonates with another ten-night frame in 7:142, and later compresses inside the surah from unnamed plural nights to the definite singular moving night in 89:4. Sound and form support the same movement: the clipped indefinite ending and paired nasal cadence let the open plural land before the final count seals it.\",\"root_display\":\"{{ar:ل ي ل}} ({{tr:l-y-l}})\",\"root_gloss_range\":\"root range centers on night as the opposite of day and its darkness, with extensions for entering or doing something by night and naming material; this ayah selects countable nights as repeated dark spans, not deictic or naming branches\",\"surface_display\":\"{{ar:لَيَالٍ}} ({{tr:layālin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:2:1:2","source_type":"qac_morpheme","support_id":"sup_e1520981fa93d703b0f0","text":"{\"lemma_ar\":\"لَيْل\",\"morph_features\":\"STEM|POS:N|LEM:layol|ROOT:lyl|MP|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:2:1:2\",\"qac_word_ref\":\"89:2:1\",\"root_ar\":\"ل ي ل\",\"surface_ar\":\"لَيَالٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:2:3:final-measure-closure","source_type":"word_analysis","support_id":"sup_f1d5de3e1ee20a31e532","text":"{\"blocking_evidence\":null,\"headline\":\"measure arrives as closure\",\"reader_payoff\":\"The reader notices that exact measure is delayed until the final word, so the ayah lands on bounded completion.\",\"reason\":\"The word is the final token of the ayah and the qualifier of the open plural, so position, grammar, and meaning converge as closure.\",\"representative_source_ids\":[\"QT-99adc89d\",\"QT-f1727df0\",\"QY-30104fad\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَلَيَالٍ عَشْرٍۢ","ayah_ref":"89:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001016/B001","root_001392/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001392","role":"The branch supplies night as a darkness-period opposed to day, providing the substance being counted.","root":"ل ي ل","source_ref":"89:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001016","role":"The cardinal branch fixes the plural periods at ten and makes them a bounded whole.","root":"ع ش ر","source_ref":"89:2","source_word_indices":["2"]}],"changed_reading":{"after":"Ten individuated darkness-periods form a closed and countable whole.","before":"An unspecified stretch of nighttime."},"confidence":"strong","focus_anchor":"The plural night noun at word 1 is directly delimited by the cardinal adjective at word 2.","mechanism":"Night supplies recurring periods of darkness, while ten closes those periods into a finite, countable set.","model_id":"baseline_counted_darkness"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_counted_darkness","source_type":"hft","support_id":"sup_44dddc7785b037632ef0","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَيَالٍ عَشْرٍۢ","ayah_ref":"89:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001016/B002","root_001392/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001392","role":"The branch supplies distinct night-periods through which the sequence can advance.","root":"ل ي ل","source_ref":"89:2","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001016","role":"The branch makes the tenth an arriving unit that completes the preceding nine.","root":"ع ش ر","source_ref":"89:2","source_word_indices":["2"]}],"changed_reading":{"after":"The sequence presses toward its tenth night as the act of completion.","before":"Ten is only a cardinal label attached to nights."},"confidence":"medium","focus_anchor":"The word عشر can activate not only a total of ten but the completion of nine by a tenth.","mechanism":"The final unit has an operation: it converts an incomplete nine into ten. The phrase therefore leans toward a terminal night that closes a sequence.","model_id":"baseline_tenth_closure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_tenth_closure","source_type":"hft","support_id":"sup_5d9251092f03fba7b9dd","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَيَالٍ عَشْرٍۢ","ayah_ref":"89:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001016/B001","root_001392/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001392","role":"The branch supplies doing, entering, or traveling in the night, making each night an active interval.","root":"ل ي ل","source_ref":"89:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001016","role":"The cardinal branch turns the nocturnal activity into ten iterations.","root":"ع ش ر","source_ref":"89:2","source_word_indices":["2"]}],"changed_reading":{"after":"Ten recurring occasions are entered and worked through under night conditions.","before":"Ten dates are merely named."},"confidence":"exploratory","focus_anchor":"The night root at word 1 includes activity undertaken or entered by night.","mechanism":"Night becomes an arena of enactment rather than passive clock time, and ten counts repeated occasions of that nocturnal enactment.","model_id":"baseline_nightwork_iterations"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_nightwork_iterations","source_type":"hft","support_id":"sup_f2a570e4fb54e4c414db","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَيَالٍ عَشْرٍۢ","ayah_ref":"89:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001016/B003","root_001016/B004","root_001392/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001392","role":"The branch provides the temporal material that can be divided into night-sized portions.","root":"ل ي ل","source_ref":"89:2","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001016","role":"The one-tenth branch recasts a unit within ten as a share of the whole.","root":"ع ش ر","source_ref":"89:2","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001016","role":"The tithe branch adds the possibility that a tenth is due, transferred, or withheld.","root":"ع ش ر","source_ref":"89:2","source_word_indices":["2"]}],"changed_reading":{"after":"The ten-night whole is apportioned, so each unit can bear a claim within the total.","before":"The ten nights are elapsed as an undivided block."},"confidence":"exploratory","focus_anchor":"The ten-root at word 2 also carries one-tenth and tithe branches.","mechanism":"A ten-unit temporal whole can be divided into accountable shares, with one night functioning conceptually as a tenth rather than every night dissolving into duration.","model_id":"baseline_apportionable_time"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_apportionable_time","source_type":"hft","support_id":"sup_be953e6fe08f22a2b8a8","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَيَالٍ عَشْرٍۢ","ayah_ref":"89:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001016/B007","root_001392/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001392","role":"The darkness-period supplies an enclosing interval in which maturation can remain unseen.","root":"ل ي ل","source_ref":"89:2","source_word_indices":["1"]},{"branch_id":"B007","mapped_root_id":"root_001016","role":"The late-pregnancy branch supplies a ten-count whose terminal significance is imminent delivery.","root":"ع ش ر","source_ref":"89:2","source_word_indices":["2"]}],"changed_reading":{"after":"Ten nights form a late-maturation interval under pressure of imminent emergence.","before":"Ten is a neutral quantity of nights."},"confidence":"exploratory","focus_anchor":"The ten-root at word 2 includes a ten-month pregnancy at the edge of delivery.","mechanism":"The branch transfers late-term pressure to the shorter night count: darkness becomes an interval of maturation poised to issue into another state.","model_id":"baseline_near_delivery_count"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_near_delivery_count","source_type":"hft","support_id":"sup_3993560859560d7e1c34","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَيَالٍ عَشْرٍۢ","ayah_ref":"89:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001016/B012","root_001016/B013","root_001392/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001392","role":"The plural darkness-periods supply the members of the proposed temporal company.","root":"ل ي ل","source_ref":"89:2","source_word_indices":["1"]},{"branch_id":"B012","mapped_root_id":"root_001016","role":"The companionship branch supplies intermingling and close relation among the counted members.","root":"ع ش ر","source_ref":"89:2","source_word_indices":["2"]},{"branch_id":"B013","mapped_root_id":"root_001016","role":"The community branch lets the ten be imagined as a group with a shared affair.","root":"ع ش ر","source_ref":"89:2","source_word_indices":["2"]}],"changed_reading":{"after":"The nights constitute a related company whose joining and isolation can matter.","before":"The nights are ten interchangeable units."},"confidence":"exploratory","focus_anchor":"The plural nights are modified by a root that also carries companionship, intermingling, and community.","mechanism":"The counted nights can be heard as a company whose meaning lies in relations among its members, not merely in their sum.","model_id":"baseline_night_company"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_night_company","source_type":"hft","support_id":"sup_b9f9f9502109324eb98c","trust":"legacy_unbound"}]}
</lane_packet_json>
