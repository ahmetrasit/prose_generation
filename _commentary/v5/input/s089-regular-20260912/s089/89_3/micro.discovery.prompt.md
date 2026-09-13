# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **89:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_3/micro.discovery.json` and modify nothing
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
  "ayah_ref": "89:3",
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
{"branch_registry":[{"boundary":"Genel çekirdek eşini ekleyerek çift yapmadır; kuşluk ibadetine ilişkin kullanım yalnızca kendi kalıbında geçerlidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000802/B001","candidate_links":[{"candidate_id":"cand_50bafa7848e9ad2dab7d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَّفْع","morph_features":"STEM|POS:N|LEM:$~afoE|ROOT:$fE|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:1:3","qac_word_ref":"89:3:1","surface_ar":"شَّفْعِ"}],"gloss":"benzerini ekleyerek çiftleştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tek duran bir şeye bir benzerini ekleyip onu çift duruma getirmeyi ve bu yolla artırmayı anlatır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sayı alanında tekliğin karşıtı olan çiftliği belirtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir kuşluk ibadeti kalıbında iki bölümlük uygulamayı adlandırır."}}],"root_ar":"ش ف ع","root_id":"root_000802","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir tekliğin eşdeğer bir eklemeyle çift duruma getirildiği genel çekirdeği karşılar.","boundary_detail":"Genel çekirdek eşini ekleyerek çift yapmadır; kuşluk ibadetine ilişkin kullanım yalnızca kendi kalıbında geçerlidir.","branch_image_ar":"ضمّ الشيء إلى مثله","concept_gloss":"benzerini ekleyerek çiftleştirme","contextual_glosses":[{"applicability":"Söz konusu olan sayının tek değil çift olmasıysa doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sayı alanındaki çift olma durumunu eksiksiz biçimde korur."},"facet_ids":["F002"],"text":"çift sayı","usage_role":"contextual"},{"applicability":"Tek duran bir şeyin ikinci bir benzeri eklenerek çift yapılmasını açıklar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başlangıçtaki tekliği, ekleme işlemini ve çift sonucu korur."},"facet_ids":["F001"],"text":"bir benzerini ekleyip çift yapmak","usage_role":"explanatory"},{"applicability":"Yalnızca kuşluk vaktindeki ibadetin iki bölümlük özel kullanımı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İbadet bağlamını ve iki bölümlük uygulama sınırını korur."},"facet_ids":["F003"],"text":"kuşluk namazının iki bölümü","usage_role":"contextual"}],"definition":"Tek duran bir şeye onun benzerini ekleyerek onu çift duruma getirme ve böylece bir artış oluşturmadır. Sayılarda çift olma bu çekirdeğin durumu, kuşluk ibadetinin iki bölümü ise kalıba bağlı özel bir gerçekleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tek duran bir şeye bir benzerini ekleyip onu çift duruma getirmeyi ve bu yolla artırmayı anlatır."},{"facet_id":"F002","role":"specialization","statement":"Sayı alanında tekliğin karşıtı olan çiftliği belirtir."},{"facet_id":"F003","role":"associated_use","statement":"Belirli bir kuşluk ibadeti kalıbında iki bölümlük uygulamayı adlandırır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bir başkası adına istekte bulunma anlamını ekler.","collision":"Aynı kökün kişi adına yardım ve istekte bulunma dalıyla karışır.","fit":"displacement","loses":"Benzerini ekleyerek tek olanı çift yapma işlemini ve çiftlik sonucunu kaybeder.","preserves":"Bir başkasına katılma düşüncesinin yalnızca uzak bir izini korur."},"text":"aracılık"}],"identity_rationale":"Kaynak ifadesi, tek olan bir şeye benzerini ekleyerek onu çift duruma getirme çekirdeğini; bunun sayıdaki çiftlik, artış ve kuşluk ibadetinin iki bölümü gibi gerçekleşmelerini birlikte doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"çift olan veya bir benzeri eklenerek çift yapılmış şey"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tek olana bir benzerini ekleyip çift yapmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kuşluk namazının iki bölümü"}],"lexicalization_note":"Çiftlik ve çift yapma genel çekirdeği oluşturur; kuşluk ibadetinin iki bölümü ise yalnızca belirtilen kalıba bağlıdır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; teklik, ikileştirme, katlama ve genel birleştirme sınırı açıklayan en yararlı dört karşıtlık seçildi, yalnızca sayı alanını ya da uzak temaları paylaşanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu dal eşini ekleyip çiftliğe ulaşır; karşı dal ise eşsiz kalmayı ya da bir şeyi tek duruma getirmeyi anlatır.","focus_only":"Benzerini ekleyerek çift oluşturma ve çift olma bu dala özgüdür.","gloss":"çiftlik ile teklik karşıtlığı","neighbor_only":"Bir şeyi tek bırakma veya tek duruma getirme karşı dala özgüdür.","neighbor_ref":"root_001621/B001","relation_type":"polarity_pair","shared_zone":"İki dal da sayı ve sayılabilir şeylerdeki çiftlik eksenini düzenler."},{"boundary_match":"partial","distinction":"Komşu dal genel olarak iki olmayı ve ikinci sırayı kapsarken bu dal benzer bir eş ekleyerek tekliği çiftliğe dönüştürmeye odaklanır.","focus_only":"Eklemenin sonucu özellikle tekliğin çiftliğe dönüşmesidir.","gloss":"ikinciyi ekleyerek iki yapma","neighbor_only":"İki sayısı, ikincilik ve ikişerli düzen gibi daha geniş iki olma alanını kapsar.","neighbor_ref":"root_000208/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de bir birime ikinci bir birim eklenmesiyle iki parçalı sonuç doğurabilir."},{"boundary_match":"partial","distinction":"Bu dalın ayırt edici sonucu çiftliktir; komşu dal ise eş kurma şartı olmadan miktarın iki veya daha çok katına çıkmasını anlatabilir.","focus_only":"Ekleme, eş oluşturup tekliği çiftliğe çevirmekle sınırlıdır.","gloss":"benzeriyle artırma","neighbor_only":"Bir miktarı kendi katlarıyla çoğaltma ve çok katlı artışları da kapsar.","neighbor_ref":"root_000909/B002","relation_type":"near_neighbor","shared_zone":"Bir şeyin benzeri eklenerek başlangıç miktarının artırılması iki alanda da bulunur."},{"boundary_match":"partial","distinction":"Komşu dal genel bağlama ve bir araya getirmeyi anlatır; bu dalda eklenen şey bir eş işlevi görür ve sonuç çiftliktir.","focus_only":"Bir benzerin eklenmesiyle çift olma sonucunu gerektirir.","gloss":"bir şeyi başka bir şeye katma","neighbor_only":"Bağlama, ip ile birleştirme ve farklı türden şeyleri birlikte yürütme kapsamına sahiptir.","neighbor_ref":"root_001221/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da ayrı bir şey başka bir şeye eklenip birlikte tutulur."}],"source_phrase_ar":"الشفع خلاف الوتر (maqayis;sihah)؛ الشفع ما كان من العدد أزواجا (ayn)؛ الشفع الزيادة (tahdhib)؛ ضم الشيء إلى مثله (mufradat)؛ شفعة الضحى ركعتا الضحى (tahdhib)","source_summary":"Ortak anlatım, tek olanın benzeri eklenince çiftleşmesini temel alır; çift sayı, artış ve iki bölümlük ibadet kullanımları bu temel üzerinde ayrışır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الزوجية بعد الوتر؛ الزيادة بضم شيء إلى شيء؛ الشفع في العدد والركعات","what_is_not_ar":"ليست الشفاعة الكلامية ولا الشفعة في الدار إلا من جهة الاشتقاق"},"support_links":["sup_6582a111224fc4c38fd0"]},{"boundary":"Bu dal salt birlikte bulunmayı değil, başka biri adına isteme, destek olma veya ona karşı düşmanlığı güçlendirme işlevini gerektirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000802/B002","candidate_links":[{"candidate_id":"cand_10766f5b280be74cfdca","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَّفْع","morph_features":"STEM|POS:N|LEM:$~afoE|ROOT:$fE|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:1:3","qac_word_ref":"89:3:1","surface_ar":"شَّفْعِ"}],"gloss":"başkası adına aracılık edip destek olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir başkasının gereksinimi için onun adına istekte bulunmayı ve ona destek olmayı anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birine yararlı veya zararlı bir işte katılarak onun eylemini güçlendirmeyi kapsar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Düşmanlık kalıbında birine karşı yardım etmeyi veya ona hasım olarak karşı koymayı belirtir."}}],"root_ar":"ش ف ع","root_id":"root_000802","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin başka biri adına istekte bulunduğu veya ona etkin destek verdiği genel çekirdeğe uygundur.","boundary_detail":"Bu dal salt birlikte bulunmayı değil, başka biri adına isteme, destek olma veya ona karşı düşmanlığı güçlendirme işlevini gerektirir.","branch_image_ar":"انضمام الشفيع إلى غيره","concept_gloss":"başkası adına aracılık edip destek olma","contextual_glosses":[{"applicability":"Bir kişinin gereksiniminin karar verebilecek birine sunulduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başka biri adına istekte bulunma eylemini ve üçüncü kişi yönünü korur."},"facet_ids":["F001"],"text":"birinin dileğini yetkiliye iletmek","usage_role":"contextual"},{"applicability":"Yararlı veya zararlı bir işte bir tarafa etkin destek verilmesini karşılar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Katılma ve eylemi güçlendirme yönlerini bağlam sınırı içinde korur."},"facet_ids":["F002"],"text":"birine katılıp onu güçlendirmek","usage_role":"contextual"},{"applicability":"Desteğin bir kişiye karşı düşmanlık veya karşı koyma yönünde olduğu özel kalıba uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Düşmanlık yönünü ve birine karşı başka tarafa yardım etme ilişkisini korur."},"facet_ids":["F003"],"text":"düşmanlıkta karşı tarafa destek vermek","usage_role":"contextual"}],"definition":"Bir kişinin başkasına katılıp onun gereksinimi için üçüncü bir kişiden istekte bulunması veya onu desteklemesidir. Bu katılım yararlı ya da zararlı bir işte güç verme biçimini alabilir; düşmanlık kalıbında ise birine karşı yardım etme ya da karşı koyma yönüne döner.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir başkasının gereksinimi için onun adına istekte bulunmayı ve ona destek olmayı anlatır."},{"facet_id":"F002","role":"extension","statement":"Birine yararlı veya zararlı bir işte katılarak onun eylemini güçlendirmeyi kapsar."},{"facet_id":"F003","role":"associated_use","statement":"Düşmanlık kalıbında birine karşı yardım etmeyi veya ona hasım olarak karşı koymayı belirtir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sayısal çiftlik veya eş oluşturma sonucunu ekler.","collision":"Aynı kökün tekliği çifte dönüştürme dalıyla karışır.","fit":"displacement","loses":"Başka biri adına isteme ve destek verme işlevlerini kaybeder.","preserves":"Bir kişinin başka birine katılması düşüncesinin biçimsel izini korur."},"text":"çiftleştirme"}],"identity_rationale":"Kaynak ifadesi, bir kişinin başkasına katılarak onun adına istekte bulunması veya onu desteklemesi çekirdeğini açıkça verir; desteğin yararlı bir işte de düşmanlık yoluyla zararlı bir işte de görülebileceğini ayrıca korur.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"başkası adına aracılık etme ve ona destek olma"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"başkası adına istekte bulunan aracı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"birinin işi için aracılık eden destekçi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini aracı kılıp yardımını istemek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"birinin işi için başkasına aracılık etmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"aracılığını kabul edip isteğini yerine getirmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"iyi ya da kötü bir işte birine katılıp onu güçlendirmek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"düşmanlıkta birine karşı yardım etmek veya ona karşı koymak"}],"lexicalization_note":"Genel aracılık rolleri ile iyi iş, kötü iş ve düşmanlık kalıpları ayrı tutulur; özel kalıpların kapsamı tüm dala yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel aracılık, bir araçla hedefe ulaşma, haksızlık için başvuru ve elçilik en yakın sınırları verdi, yalnızca iyilik veya ilişki düzeltme temasını paylaşan uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal taraflar arasındaki genel aracılığı anlatır; bu dal ise belirli bir kişiye katılıp onun isteğini iletme veya gücünü artırma yönü taşır.","focus_only":"Bir taraf adına istekte bulunmayı ve o tarafı desteklemeyi gerektirir.","gloss":"bir taraf adına aracılık","neighbor_only":"Taraflar arasında orta yerde durup iletişim kurmayı daha genel biçimde kapsar.","neighbor_ref":"root_001646/B005","relation_type":"near_synonym","shared_zone":"Her iki dalda da kişiler arasındaki bir işin üçüncü kişi yardımıyla yürütülmesi vardır."},{"boundary_match":"partial","distinction":"Bu dal aracının başkası adına katılımını anlatır; komşu dal ise istekte bulunanın hedefe ulaşmak için kullandığı yolu daha geniş biçimde kavrar.","focus_only":"Aracı kişinin başkası adına konuşması veya ona destek vermesi öne çıkar.","gloss":"bir aracı üzerinden sonuca ulaşma","neighbor_only":"Arayan kişinin bir araç, bağ, kanıt veya kişi üzerinden amacına ulaşması öne çıkar.","neighbor_ref":"root_000485/B004","relation_type":"near_neighbor","shared_zone":"Bir isteğin doğrudan değil, aradaki bir kişi veya araç yoluyla gerçekleştirilmesi ortaktır."},{"boundary_match":"partial","distinction":"Komşu dal haksızlığın giderilmesine bağlı özel bir başvurudur; bu dalın isteği ve desteği böyle bir haksızlık koşuluna bağlı değildir.","focus_only":"Her türlü gereksinim için başkası adına isteme veya destek olma kapsamına sahiptir.","gloss":"yetkiliden başkası için yardım isteme","neighbor_only":"Uğranan haksızlık için yönetici ya da yargıçtan yardım ve öç istemekle sınırlıdır.","neighbor_ref":"root_000993/B005","relation_type":"near_neighbor","shared_zone":"Bir kişinin işi için yetkili bir üçüncü kişiden yardım istenmesi iki dalda da görülebilir."},{"boundary_match":"partial","distinction":"Komşu dal ara konumu ve elçiliği anlatır; bu dal ise bir tarafa katılıp onun adına isteme veya onu güçlendirme işlevini gerektirir.","focus_only":"Aracı bir tarafın isteğini üstlenir ve ona destek olur.","gloss":"iki kişi arasında aracı olma","neighbor_only":"İki kişi arasında elçi veya ayırıcı bir ara konumda bulunmayı belirtir.","neighbor_ref":"root_000674/B005","relation_type":"near_neighbor","shared_zone":"İki alan da doğrudan ilişki kurmayan kişiler arasında üçüncü bir rol içerir."}],"source_phrase_ar":"شفع فلان لفلان إذا جاء ثانية ملتمسا مطلبه ومعينا له (maqayis)؛ الشافع الطالب لغيره (ayn;tahdhib)؛ الشفاعة كلام الشفيع للملك في حاجة يسألها لغيره (tahdhib)؛ الانضمام إلى آخر ناصرا له وسائلا عنه (mufradat)؛ يشفع لي بالعداوة أي يعين علي (maqayis)؛ يشفع لي بعداوة أي يضادني (tahdhib)","source_summary":"Ortak çekirdek, bir kişinin başka birinin yanına katılıp onun adına istemesi ya da onu güçlendirmesidir; yararlı ve zararlı destek ile düşmanlık kullanımı bu katılımın yönlerini gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الشفاعة والسؤال للغير والمعونة له في خير أو شر؛ الدعاء والكلام لصاحب الحاجة؛ الإعانة بالعداوة","what_is_not_ar":"ليست مجرد الزوجية العددية ولا حق الشفعة في الملك"},"support_links":["sup_6f8a39509bae87541e7c"]},{"boundary":"Anlam genel mülk edinme değil, ev veya arazi satışında bağlantı nedeniyle doğan öncelikli alım hakkıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000802/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَّفْع","morph_features":"STEM|POS:N|LEM:$~afoE|ROOT:$fE|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:1:3","qac_word_ref":"89:3:1","surface_ar":"شَّفْعِ"}],"gloss":"taşınmaz satışında öncelikli alım hakkı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ev veya arazi satışında bağlantısı bulunan isteklinin öncelikli alım hakkını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hakkın kullanılması, satılanı isteklinin elindeki mülke katması ve daha sonraki isteklilerin önüne geçmesi sonucunu doğurur."}}],"root_ar":"ش ف ع","root_id":"root_000802","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ev veya arazi satışında bağlantılı isteklinin başkalarından önce satın alma hakkını eksiksiz karşılar.","boundary_detail":"Anlam genel mülk edinme değil, ev veya arazi satışında bağlantı nedeniyle doğan öncelikli alım hakkıdır.","branch_image_ar":"ضمّ الجار نصيبه إلى ملكه","concept_gloss":"taşınmaz satışında öncelikli alım hakkı","contextual_glosses":[{"applicability":"Hakkın teknik adından çok, satıştaki işlemin açıkça anlatılması gereken bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Önceliğin satışla bağlantılı kişiye ait bir hak olması koşulunu açıkça söylemez.","preserves":"Taşınmaz satışında başkalarından önce satın alma sonucunu korur."},"facet_ids":["F001","F002"],"text":"satılan taşınmazı öncelikle alma","usage_role":"general"}],"definition":"Bir ev ya da arazinin satışında, satışla geçerli bağlantısı bulunan isteklinin satılanı kendi mülküne katabilmesi için sonraki isteklilere göre öncelik kazanmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ev veya arazi satışında bağlantısı bulunan isteklinin öncelikli alım hakkını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Hakkın kullanılması, satılanı isteklinin elindeki mülke katması ve daha sonraki isteklilerin önüne geçmesi sonucunu doğurur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Halen elde bulunan bölünmüş veya bölünmemiş bir pay anlamını ekler.","collision":"Mevcut ortaklık payı ile satıştan doğan öncelik hakkını karıştırır.","fit":"displacement","loses":"Satış anında doğan öncelikli alım işlemini ve sonraki alıcıların önüne geçmeyi kaybeder.","preserves":"Taşınmaz ve mülkiyet alanıyla bağlantıyı korur."},"text":"mülkiyet payı"}],"identity_rationale":"Kaynak ifadesi ev veya arazi satışında, satışla bağlantılı kişinin satın alınanı kendi malına katmak üzere sonraki isteklilerden önce gelmesini doğrular. Ancak geçici çerçevedeki komşu ve pay vurgusu bütün ifadelerde kurucu şart olarak açık değildir; güvenli sınır, geçerli bir bağlantıya dayanan öncelikli alımdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ev veya arazi satışında öncelikli alım hakkı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"öncelikli alım hakkını isteyen kişi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"satılanı öncelikle alma yetkisini ona vermek"}],"lexicalization_note":"Ad biçimleri taşınmazdaki hakkı, eylem ise belirli bir satışta öncelik vermeyi anlatır; bunlar genel bir katma anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar incelendi; ortak pay, taşınmazdaki sabit hak ve ortaklar arası satın alma en açıklayıcı karşılaştırmalardı, rehin, yaşam boyu bağış ve genel izin gibi farklı çekirdekler yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal mevcut ortak payı anlatır; bu dal ise satışın doğurduğu, satılanı başkalarından önce alma yetkisini anlatır.","focus_only":"Bir satış gerçekleştiğinde bağlantılı kişinin öncelikle satın alma hakkını belirtir.","gloss":"ortak mülkte öncelikli alım","neighbor_only":"Henüz bölünmemiş ortak mülkiyet payının mevcut durumunu belirtir.","neighbor_ref":"root_000836/B004","relation_type":"near_neighbor","shared_zone":"İki dal da ev veya arazi üzerindeki birden çok kişinin mülkiyet ilgisiyle bağlantılıdır."},{"boundary_match":"field_only","distinction":"Komşu dal sabit bir hak veya payın varlığıdır; bu dalın çekirdeği ise satış sırasında kullanılabilen öncelikli satın alma yetkisidir.","focus_only":"Satış olayıyla işleyen ve alıcıya sıra önceliği veren bir haktır.","gloss":"taşınmazdaki hak","neighbor_only":"Bir evde önceden var olan sabit hak veya payı belirtir.","neighbor_ref":"root_001045/B003","relation_type":"same_field","shared_zone":"Her iki dal da bir ev veya arazi üzerinde kişiye tanınan mülkiyet ilgisini anlatır."},{"boundary_match":"partial","distinction":"Komşu dal ortakların kendi aralarındaki fiyatlama ve satın alma sürecidir; bu dal ise belirli bağlantıya dayanarak satışta sıra önceliği sağlar.","focus_only":"Bağlantılı istekliyi dışarıdaki sonraki alıcılardan önce getirir.","gloss":"ortaklar arasında payı satın alma","neighbor_only":"Ortaklar arasında değer biçme veya artırma yoluyla bir ortağın diğer payları satın almasını düzenler.","neighbor_ref":"root_001274/B004","relation_type":"near_neighbor","shared_zone":"Ortaklık veya bağlantı içindeki bir kişinin taşınmazın daha büyük bölümünü satın alması iki alanda da görülebilir."}],"source_phrase_ar":"الشفعة في الدار (maqayis)؛ الشفعة في الدار والأرض (sihah)؛ الشفعة الزيادة حتى تضمه إلى ما عندك (tahdhib)؛ فشفعه وجعله أولى ممن بعد سببه (tahdhib)","source_summary":"Ortak anlatım ev ve arazi alanındaki öncelikli alımı öne çıkarır; istekli, satışla olan bağlantısı nedeniyle sonraki kişilerin önüne geçirilir ve satılanı kendi mülküne katabilir.","sources":["MQ","SI","TA"],"what_is_ar":"الشفعة في الدار والأرض؛ أولوية الطالب في المبيع ليضمه إلى ما عنده","what_is_not_ar":"ليست الشفاعة في الحاجة ولا مطلق الزوجية"},"support_links":[]},{"boundary":"Niteleme bütün dişi hayvanlara yayılmaz; kanıt yalnızca belirtilen koyun ve dişi deve durumlarını kapsar.","branch_kind":"non_bare","branch_ref":"root_000802/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَّفْع","morph_features":"STEM|POS:N|LEM:$~afoE|ROOT:$fE|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:1:3","qac_word_ref":"89:3:1","surface_ar":"شَّفْعِ"}],"gloss":"yavrulu koyun veya iki yavru durumundaki dişi deve","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yavrusu yanında bulunan koyunu niteler."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karnında yavru taşıyan ve başka bir yavrusu da ardından gelen dişi deveyi niteler."}}],"root_ar":"ش ف ع","root_id":"root_000802","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Koyundaki eşlik eden yavruyu ve dişi devedeki iki ayrı yavru ilişkisini birlikte kapsar.","boundary_detail":"Niteleme bütün dişi hayvanlara yayılmaz; kanıt yalnızca belirtilen koyun ve dişi deve durumlarını kapsar.","branch_image_ar":"الأنثى المشفوعة بولدها","concept_gloss":"yavrulu koyun veya iki yavru durumundaki dişi deve","contextual_glosses":[{"applicability":"Yavrunun koyunun yanında bulunduğu özel hayvancılık bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Koyun türünü ve yavrunun anne yanında bulunmasını korur."},"facet_ids":["F001"],"text":"yavrusu yanındaki koyun","usage_role":"contextual"},{"applicability":"Dişi devenin hem karnında yavru taşıdığı hem de başka yavrusunun onu izlediği bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gebeliği, eşlik eden öteki yavruyu ve dişi deve sınırını korur."},"facet_ids":["F002"],"text":"gebe ve başka yavrusu da ardınca gelen dişi deve","usage_role":"explanatory"}],"definition":"Yavrusu yanında bulunan koyunu veya karnında yavru taşıyan ve başka bir yavrusu da ardından gelen dişi deveyi niteleyen, yavrunun anneye eşlik etmesi temelli kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yavrusu yanında bulunan koyunu niteler."},{"facet_id":"F002","role":"specialization","statement":"Karnında yavru taşıyan ve başka bir yavrusu da ardından gelen dişi deveyi niteler."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Bütün hayvan türlerini ve yanında başka yavru bulunmayan gebelikleri kapsama ekler.","collision":"Yalnız gebeliği bildiren komşu hayvan nitelemeleriyle karışır.","fit":"broadening","loses":null,"preserves":"Dişi devenin karnında yavru taşıması yönünü kısmen korur."},"text":"gebe dişi hayvan"}],"identity_rationale":"Kaynak ifadesi iki bağlı hayvan kullanımını açıkça destekler: yavrusu yanında olan koyun ve karnında yavru taşıyıp başka bir yavrusu da ardından gelen dişi deve. Geçici çerçeve bu iki özel durumu doğru biçimde bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yavrusu yanında bulunan koyun"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"karnında yavru taşıyan veya ardından başka yavrusu gelen dişi deve"}],"lexicalization_note":"Anlam yalnızca koyun ve dişi deveyle kurulan niteleme kalıplarında geçerlidir; bağımsız ve genel bir yavrululuk anlamı değildir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel yavrululuk, görünür gebelik, gebe deve topluluğu ve gebe kalmama en açıklayıcı sınırları sağladı, yavrunun adı veya çiftleşme gibi yalnızca aynı yaşam döngüsünü paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal tür bakımından geniş bir yavrululuk alanıdır; bu dal koyuna ve karnındaki yavruyla birlikte başka yavrusu izleyen dişi deveye bağlıdır.","focus_only":"Koyunla ve özel iki yavru ilişkisi içindeki dişi deveyle sınırlıdır.","gloss":"yavrusu yanında olan dişi","neighbor_only":"Kadın, ceylan ve çeşitli evcil hayvanlarda yavrulu olmayı daha geniş biçimde kapsar.","neighbor_ref":"root_000942/B002","relation_type":"near_synonym","shared_zone":"Anne durumundaki bir dişiye yavrusunun eşlik etmesi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Komşu dal gebeliğin görünür belirtilerine odaklanır; bu dal ise yavrunun anneyle birlikteliğini ve dişi devedeki ek yavruyu öne çıkarır.","focus_only":"Yavrunun yanında bulunmasını veya dişi devedeki iki yavru ilişkisini belirtir.","gloss":"gebeliği görünen hayvan","neighbor_only":"Gebeliğin dışarıdan görünür hale gelmesini ve memenin büyümesini belirtir.","neighbor_ref":"root_000531/B010","relation_type":"near_neighbor","shared_zone":"Dişi koyun veya devenin yavru taşıması iki kullanımda da kesişebilir."},{"boundary_match":"field_only","distinction":"Komşu dal gebe develerin topluluğunu adlandırır; bu dal tek hayvanı, yavrunun eşliği ve özel iki yavru düzeni bakımından niteler.","focus_only":"Tek bir koyun veya dişi devenin yavru ilişkisine göre nitelenmesidir.","gloss":"gebe dişi develer","neighbor_only":"Gebe dişi develerden oluşan topluluğun adıdır.","neighbor_ref":"root_001406/B003","relation_type":"same_field","shared_zone":"Her iki dal dişi devenin gebeliği ve yavru taşıması alanında yer alır."},{"boundary_match":"partial","distinction":"Bu dal yavruyla kurulan fiilî birlikteliği içerir; komşu dal ise gebeliğin bulunmadığı dönemi belirtir ve koyun kullanımına uzanmaz.","focus_only":"Yavru taşıyan veya yavrusu yanında bulunan anne durumunu anlatır.","gloss":"yavrulu olma ile boş kalma karşılaştırması","neighbor_only":"Bir yıl ya da daha uzun süre gebe kalmamış dişi deve durumunu anlatır.","neighbor_ref":"root_000373/B007","relation_type":"near_neighbor","shared_zone":"İki dal da dişi devenin üreme durumunu niteleyen hayvancılık söz varlığıdır."}],"source_phrase_ar":"الشاة الشافع التي معها ولدها (maqayis)؛ ناقة شافع في بطنها ولد ويتبعها آخر (sihah)؛ الشافع التي معها ولدها (tahdhib)؛ ناقة شافع إذا كان في بطنها ولد يتلوها آخر (tahdhib)","source_summary":"Anlam, anne hayvana eşlik eden yavru üzerinden kurulur; koyunda yavrunun yanında bulunması, dişi devede ise karnındaki yavruya ek olarak başka bir yavrunun ardından gelmesi belirtilir.","sources":["MQ","SI","TA"],"what_is_ar":"الشاة أو الناقة التي معها ولدها أو في بطنها ولد ويتلوه آخر","what_is_not_ar":"ليست مطلق الشفاعة ولا الشفعة في الملك"},"support_links":[]},{"boundary":"Anlam genel süt bolluğu değil, tek sağımda iki kabı doldurma ölçüsüne bağlı dişi deve niteliğidir.","branch_kind":"non_bare","branch_ref":"root_000802/B005","candidate_links":[{"candidate_id":"cand_fda41ca5d856dae9acc1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَّفْع","morph_features":"STEM|POS:N|LEM:$~afoE|ROOT:$fE|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:1:3","qac_word_ref":"89:3:1","surface_ar":"شَّفْعِ"}],"gloss":"tek sağımda iki kap dolduran dişi deve","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi devenin tek sağımda iki ayrı sağım kabını dolduracak süt vermesini belirtir."}}],"root_ar":"ش ف ع","root_id":"root_000802","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi devenin tek sağımda iki kabı dolduracak süt vermesini tam olarak karşılar.","boundary_detail":"Anlam genel süt bolluğu değil, tek sağımda iki kabı doldurma ölçüsüne bağlı dişi deve niteliğidir.","branch_image_ar":"جمع محلبين في حلبة","concept_gloss":"tek sağımda iki kap dolduran dişi deve","contextual_glosses":[{"applicability":"Tek sağım koşulunun bağlamdan zaten açık olduğu hayvancılık anlatımında kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki kabın aynı sağım sırasında doldurulması koşulunu açıkça belirtmez.","preserves":"Dişi deveyi ve iki kaplık süt verimini korur."},"facet_ids":["F001"],"text":"iki kaplık süt veren dişi deve","usage_role":"general"}],"definition":"Tek sağımda iki sağım kabını dolduracak kadar süt veren dişi deveyi niteleyen özel bir hayvancılık kullanımıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi devenin tek sağımda iki ayrı sağım kabını dolduracak süt vermesini belirtir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"İki kap ve tek sağım ölçüsüne uymayan her türlü süt bolluğunu kapsama alır.","collision":"Genel süt bolluğunu anlatan başka hayvan nitelemeleriyle karışır.","fit":"broadening","loses":null,"preserves":"Dişi devenin yüksek süt verimini genel olarak korur."},"text":"bol sütlü dişi deve"}],"identity_rationale":"Kaynak ifadesi, tek sağımda iki sağım kabını bir araya getirecek ölçüde süt veren dişi deveyi açık ve tutarlı biçimde tanımlar. Geçici çerçeve bu özel hayvancılık niteliğini doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"tek sağımda iki kap dolduracak süt veren dişi deve"}],"lexicalization_note":"Anlam yalnızca dişi deveyle kurulan hayvancılık nitelemesinde geçerlidir ve bağımsız bir birleştirme anlamına genişletilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çok kaplı sağım, üçlü sağım ölçüsü, genel süt bolluğu ve sağım zamanı sınırı açıklayan adaylar seçildi, mera ve sağım çağrısı gibi yalnızca hayvancılık ortamını paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal iki veya üç kaplık verime ve başka bir duruş özelliğine uzanır; bu dal yalnızca tek sağımda iki kaplık ölçüyü bildirir.","focus_only":"Ölçü tam olarak tek sağımda iki kabın doldurulmasıdır.","gloss":"bir sağımda birden çok kap dolduran dişi deve","neighbor_only":"İki veya üç kabı kapsayabilir ve sağımda ön ayakların dizilişini de anlatabilir.","neighbor_ref":"root_000871/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir sağımda birden fazla kabı dolduran dişi deveyi niteleyebilir."},{"boundary_match":"partial","distinction":"Bu dalın belirleyici sayısı iki ve koşulu tek sağımdır; komşu dal üçlü ölçüler ile meme uçlarına ilişkin farklı durumları bir araya getirir.","focus_only":"Tek sağımda iki kabı doldurma ölçüsüne bağlıdır.","gloss":"sağımda üçlü ölçü taşıyan dişi deve","neighbor_only":"Üç kap doldurma, üç meme ucundan sağılma veya üçünün kuruması gibi farklı üçlü durumları kapsar.","neighbor_ref":"root_000203/B005","relation_type":"near_neighbor","shared_zone":"İki dal da dişi deveyi sağım kabı sayısı veya sağım düzeni üzerinden niteler."},{"boundary_match":"partial","distinction":"Komşu dal farklı hayvanlara yayılan genel bir akış bolluğudur; bu dal dişi deveye ve iki kaplık tek sağım ölçüsüne bağlıdır.","focus_only":"Süt verimini iki kap ve tek sağım ölçüsüyle belirler.","gloss":"bol süt veren hayvan","neighbor_only":"Atın teri veya deve ve koyunun sütü için genel, taşkın bir bolluk niteliğidir.","neighbor_ref":"root_001591/B004","relation_type":"near_neighbor","shared_zone":"Dişi devenin yüksek miktarda süt vermesi iki dalda da bulunabilir."},{"boundary_match":"field_only","distinction":"Komşu dal sağımın duruşuna ve zamanına bağlı sütü anlatır; bu dal sağım biçiminden çok tek seferdeki iki kaplık miktarı ölçer.","focus_only":"Bir sağımda elde edilen sütün iki kabı dolduracak miktarda olmasını anlatır.","gloss":"sağım zamanı ve süt miktarı","neighbor_only":"Dişi deve çökmüşken sağılan veya gece memede birikip sabah alınan sütü anlatır.","neighbor_ref":"root_000109/B007","relation_type":"same_field","shared_zone":"İki dal da dişi devenin sağılması ve memede biriken sütün alınması alanındadır."}],"source_phrase_ar":"ناقة شفوع وهي التي تجمع بين محلبين في حلبة واحدة (maqayis;sihah)؛ ناقة شفوع تجمع بين محلبين في حلبة (tahdhib)","source_summary":"Ortak anlatım, dişi devenin bir sağımda elde edilen sütü iki sağım kabında toplayacak ölçüde verimli oluşuna dayanır.","sources":["MQ","SI","TA"],"what_is_ar":"الناقة الشفوع التي تجمع بين محلبين في حلبة واحدة","what_is_not_ar":"ليست الناقة الشافع ذات الولد ولا الشفاعة في الطلب"},"support_links":["sup_81845ed399f451dce7cf"]},{"boundary":"Anlam genel görme zayıflığı değil, tek bir nesne veya kişinin iki görüntü halinde algılanmasıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000802/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَّفْع","morph_features":"STEM|POS:N|LEM:$~afoE|ROOT:$fE|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:1:3","qac_word_ref":"89:3:1","surface_ar":"شَّفْعِ"}],"gloss":"tek nesneyi çift görme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Görme zayıflığı tek bir nesnenin ya da kişinin iki ayrı görüntü gibi algılanmasına yol açar."}}],"root_ar":"ش ف ع","root_id":"root_000802","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Görme zayıflığı nedeniyle bir kişi veya nesnenin iki görüntü halinde algılanmasını karşılar.","boundary_detail":"Anlam genel görme zayıflığı değil, tek bir nesne veya kişinin iki görüntü halinde algılanmasıdır.","branch_image_ar":"رؤية الواحد اثنين","concept_gloss":"tek nesneyi çift görme","contextual_glosses":[{"applicability":"Bağlamda tek nesnenin iki görüntü olarak algılandığı zaten açıksa doğal kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tek görüntünün çift algılanması biçimindeki temel görme belirtisini korur."},"facet_ids":["F001"],"text":"çift görme","usage_role":"general"},{"applicability":"Belirtinin kişi görüntüsü üzerinden açıklandığı örnek bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tek kişiyi iki ayrı kişi gibi algılama örneğini eksiksiz korur."},"facet_ids":["F001"],"text":"bir kişiyi iki kişi gibi görmek","usage_role":"explanatory"}],"definition":"Görme zayıflığı yüzünden tek bir nesne veya kişinin iki ayrı görüntü halinde algılanmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Görme zayıflığı tek bir nesnenin ya da kişinin iki ayrı görüntü gibi algılanmasına yol açar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Çift görüntü oluşturmayan bütün görme yetersizliklerini kapsama alır.","collision":"Gece görememe, bulanıklık ve göz yorgunluğu gibi komşu bozukluklarla karışır.","fit":"broadening","loses":null,"preserves":"Görme gücündeki bozulmayı genel düzeyde korur."},"text":"görme zayıflığı"}],"identity_rationale":"Kaynak ifadesi, görme zayıflığı nedeniyle tek bir kişinin iki kişi gibi algılanmasını ve gözün çift görüntü üretmesini doğrudan belirtir. Geçici çerçeve bu belirli görme bozukluğunu doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"tek nesneyi çift gören göz"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"bir kişiyi iki kişi gibi gösteren görme bozukluğu"}],"lexicalization_note":"Göz nitelemesi ile görme bozukluğunun adı aynı çift görme çekirdeğinde tutulur; anlam genel görme zayıflığına yayılmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; gece görme zayıflığı, bulanıklık, bakış sapması ve baş dönmesi okuyucunun en kolay karıştıracağı sınırlardı, normal görme ve ışığa özgü bozukluklar daha uzak kaldığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal görme gücünün, özellikle karanlıkta, azalmasıdır; bu dalın ayırt edici belirtisi tek nesnenin iki görünmesidir.","focus_only":"Tek bir nesnenin iki görüntü halinde algılanmasını gerektirir.","gloss":"görme zayıflığı","neighbor_only":"Özellikle gece görememe veya ışık azalınca görmenin zayıflamasını kapsar.","neighbor_ref":"root_001017/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da görme yetisinin zayıflamasından doğan algı güçlüğünü anlatır."},{"boundary_match":"partial","distinction":"Komşu dal görüntüyü puslu ve belirsiz kılar; bu dal ise tek nesneyi iki ayrı görüntüye böler.","focus_only":"Görüntüyü iki ayrı kopya halinde algılatır.","gloss":"bulanık görme ile çift görme","neighbor_only":"Gözde perde, pus veya keskinlik kaybı biçiminde bulanık görmeye yol açar.","neighbor_ref":"root_001094/B002","relation_type":"near_neighbor","shared_zone":"İki dal da gözdeki bir bozukluk nedeniyle görüntünün olağan açıklığını yitirmesidir."},{"boundary_match":"partial","distinction":"Komşu dal bakışın yönelimi veya yorgunluğu üzerindedir; bu dal ise görme zayıflığı nedeniyle tek hedefin iki görüntü olarak algılanmasıyla tanımlanır.","focus_only":"Sonuç tek hedefin iki görüntü olarak görülmesidir.","gloss":"bakış sapması ve çift görüntü","neighbor_only":"Bakışın yönünden sapmasını veya gözün yorulup güçten düşmesini anlatır.","neighbor_ref":"root_000658/B002","relation_type":"near_neighbor","shared_zone":"Gözün olağan bakışı sürdürememesi iki durumda da görsel algıyı bozabilir."},{"boundary_match":"field_only","distinction":"Komşu dal dönme ve baygınlık hissiyle tanımlanır; bu dalda baş dönmesi gerekmez, belirleyici olan çift görüntüdür.","focus_only":"Belirli görsel sonuç, tek nesnenin çift algılanmasıdır.","gloss":"baş dönmesi sırasında bozulan algı","neighbor_only":"Baş dönmesi ve kimi zaman bilinç bulanmasıyla seyreden genel bir baş rahatsızlığıdır.","neighbor_ref":"root_000499/B005","relation_type":"same_field","shared_zone":"Baş veya göz kaynaklı rahatsızlıklar kişinin görsel çevreyi olağandışı algılamasına yol açabilir."}],"source_phrase_ar":"عين شافعة تنظر نظرين (tahdhib)؛ أرى الشخص الواحد شخصين لضعف بصري (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek başına tanıklanan kullanım, zayıf görmenin bir kişiyi iki kişi gibi göstermesini açıkça belirtir."}],"source_summary":"Anlam, görme zayıflığının tek bir kişi veya nesneyi iki ayrı görüntüye ayırmasıyla tanımlanan özel bir algı bozukluğudur.","sources":["TA"],"what_is_ar":"العين الشافعة وضعف البصر حتى يرى الشخص الواحد شخصين","what_is_not_ar":"ليست الزوجية العددية ولا الشفاعة في الحاجة"},"support_links":[]},{"boundary":"Bu dal yalnız sayısal tekliği ve bir toplamı tek sayıya getiren kullanımları kapsar; öç, hak eksiltme ve yay kirişi anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001621/B001","candidate_links":[{"candidate_id":"cand_50bafa7848e9ad2dab7d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَتْر","morph_features":"STEM|POS:N|LEM:wator|ROOT:wtr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:2:3","qac_word_ref":"89:3:2","surface_ar":"وَتْرِ"}],"gloss":"tek sayı ve tekleştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir sayının çiftin karşıtı olan tek durumda bulunması veya sayılabilir bir bütünün tek sayıya getirilmesi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gece ibadetine bir bölüm ekleyerek toplam bölüm sayısını tek kılma."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Taşla temizlenirken üç, beş veya yedi gibi tek sayıda taş kullanma."}}],"root_ar":"و ت ر","root_id":"root_001621","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sayıdaki tekliği ve sayılabilir bir bütünü tek sayıya getirme işlemini birlikte anlatan genel karşılıktır.","boundary_detail":"Bu dal yalnız sayısal tekliği ve bir toplamı tek sayıya getiren kullanımları kapsar; öç, hak eksiltme ve yay kirişi anlamlarını kapsamaz.","branch_image_ar":"فرد لا شفع معه","concept_gloss":"tek sayı ve tekleştirme","contextual_glosses":[{"applicability":"Toplam bölüm sayısını son bir bölümle tek kılmayı anlatan ibadet bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İbadet toplamını tek sayıya getirme işlemini eksiksiz korur."},"facet_ids":["F002"],"text":"gece ibadetini tek sayıda bitirmek","usage_role":"contextual"},{"applicability":"Taşla temizlenme sırasında üç, beş veya yedi taş kullanılması bağlamında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Temizlenme aracının sayısını tek tutma koşulunu açıkça korur."},"facet_ids":["F003"],"text":"tek sayıda taş kullanmak","usage_role":"contextual"}],"definition":"Bir sayının ya da sayılabilir bir bütünün çift olmayıp tek olması veya bir bütünün tek sayıya getirilmesidir. Gece ibadetini tek sayıda bitirme ve temizlenirken tek sayıda taş kullanma bunun kalıba bağlı uygulamalarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir sayının çiftin karşıtı olan tek durumda bulunması veya sayılabilir bir bütünün tek sayıya getirilmesi."},{"facet_id":"F002","role":"specialization","statement":"Gece ibadetine bir bölüm ekleyerek toplam bölüm sayısını tek kılma."},{"facet_id":"F003","role":"specialization","statement":"Taşla temizlenirken üç, beş veya yedi gibi tek sayıda taş kullanma."}],"identity_rationale":"Kaynak ifadesi, sayıdaki tekliği çiftliğin karşıtı olarak verir; ayrıca bir şeyi tek kılma eylemini ve gece ibadeti ile taşla temizlenmedeki tek sayılı uygulamaları açıkça kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tek sayı; çiftin karşıtı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tek kılmak veya tek sayıya çevirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"gece ibadetini tek sayıda bitirmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"temizlenirken tek sayıda taş kullanmak"}],"lexicalization_note":"Çıplak biçim sayıdaki tekliği, eylem biçimi tek kılmayı anlatır; gece ibadeti ve taşla temizlenme anlamları yalnız kendi kalıpları içinde geçerlidir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sayısal tekliğin sınırını en açık gösteren çiftleştirme karşıtlığı yayımlandı, yalnız aynı kökü veya uzak bir sayısal alanı paylaşan adaylar elendi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu dalın sonucu tek sayıdır; komşu dalın sonucu ise bir eş daha eklenmesiyle oluşan çift sayıdır. Bu nedenle aynı sayısal eksenin karşıt uçlarındadırlar.","focus_only":"Bu dal sayının tek kalmasını veya bir toplamın tek sayıya getirilmesini anlatır.","gloss":"tekleştirme ve çiftleştirme karşıtlığı","neighbor_only":"Komşu dal, benzer bir öğe ekleyerek tek olanı çift duruma getirmeyi anlatır.","neighbor_ref":"root_000802/B001","relation_type":"antonym","shared_zone":"Her iki dal da sayılabilir bir bütünün tek ya da çift oluşunu ve bu durumun değiştirilmesini konu edinir."}],"source_phrase_ar":"الوتر والوتر الفرد (maqayis)؛ الوتر الفرد ضد الشفع (jamhara)؛ الوتر بالكسر الفرد (sihah)؛ الوتر في العدد ولغتا وتر ووتر وأوتر صلاته (tahdhib)؛ الوتر في العدد خلاف الشفع وأوتر في الصلاة (mufradat)","source_summary":"Kaynaklar sayıdaki tekliği çiftliğin karşıtı olarak ortaklaşa tanımlar ve bir şeyi tek kılma eylemini bu çekirdeğe bağlar. Gece ibadetini tek sayıda bitirme ile temizlenirken tek sayıda taş kullanma, aynı sayısal işlemin belirli bağlamlardaki uygulamalarıdır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الوتر في العدد خلاف الشفع، وإيتار الشيء أو الصلاة أو الاستجمار بجعله فردا.","what_is_not_ar":"لا يدخل فيه الذحل أو نقص الحق، ولا توتير القوس."},"support_links":["sup_6582a111224fc4c38fd0"]},{"boundary":"Dal, sıradan eksilmeyi değil, uğranan ağır zararın doğurduğu öç alacağını ve bu alacağı taşıyan kişinin durumunu kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001621/B002","candidate_links":[{"candidate_id":"cand_10766f5b280be74cfdca","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَتْر","morph_features":"STEM|POS:N|LEM:wator|ROOT:wtr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:2:3","qac_word_ref":"89:3:2","surface_ar":"وَتْرِ"}],"gloss":"öç gerektiren karşılıksız ağır zarar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Öldürme, mal alma veya ağır kötülük sonucunda doğan ve karşılığı henüz alınmamış öç alacağı."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birini ağır zarara uğratarak öç talep eder duruma getirme ve bu talebi henüz karşılanmamış mağdur olma."}}],"root_ar":"و ت ر","root_id":"root_001621","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir öldürme, mal alma veya ağır kötülükten doğan ve henüz karşılığı alınmamış talebin genel karşılığıdır.","boundary_detail":"Dal, sıradan eksilmeyi değil, uğranan ağır zararın doğurduğu öç alacağını ve bu alacağı taşıyan kişinin durumunu kapsar.","branch_image_ar":"ذحل يطلب بثأر","concept_gloss":"öç gerektiren karşılıksız ağır zarar","contextual_glosses":[{"applicability":"Yakını öldürülen veya hakkı alınan kişinin henüz karşılık alamadığı kişi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mağdurun ağır kaybını ve öç talebinin karşılanmamış durumunu korur."},"facet_ids":["F002"],"text":"öcü alınmamış mağdur","usage_role":"contextual"}],"definition":"Bir yakının öldürülmesi, malın alınması veya ağır bir kötülük yapılmasıyla doğan ve karşılığı henüz alınmamış öç alacağıdır. Aynı alan, bu zararı verme eylemini ve öç alacağı bulunan mağdurun durumunu da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Öldürme, mal alma veya ağır kötülük sonucunda doğan ve karşılığı henüz alınmamış öç alacağı."},{"facet_id":"F002","role":"extension","statement":"Birini ağır zarara uğratarak öç talep eder duruma getirme ve bu talebi henüz karşılanmamış mağdur olma."}],"identity_rationale":"Kaynak ifadesi, bir yakının öldürülmesi, malın alınması veya ağır bir kötülük yapılmasıyla doğan ve karşılığı henüz alınmamış öç talebini açıkça anlatır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"öç alınmasını gerektiren ağır zarar"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"öç gerektiren suç veya zarar"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini ağır zarara uğratıp öç ister duruma getirmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"öcünü henüz alamamış mağdur"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"alınması beklenen öçler ve karşılıksız kalmış zararlar"}],"lexicalization_note":"Ad biçimleri öç gerektiren ağır zararı, eylem biçimi birini böyle bir zarara uğratmayı, kişi biçimi ise öcünü henüz alamamış mağduru anlatır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öç talebine en yakın sınır kan davası dalıyla gösterildi, ceza, bedel ödeme ve genel hak eksiltme dalları farklı sonuçlar kurdukları için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekleri öç talebinde örtüşür; ancak bu dal mal kaybı ve genel ağır kötülüğü de kapsarken komşu dal düşmanlık ile öldürmeye bağlı kan davasında yoğunlaşır.","focus_only":"Bu dal öldürmenin yanında mal alma ve başka ağır kötülüklerden doğan öç alacağını da kapsar.","gloss":"öç alacağı ve kan davası","neighbor_only":"Komşu dal açık düşmanlığı ve özellikle öldürülen biri için sürdürülen kan davasını öne çıkarır.","neighbor_ref":"root_000959/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da ağır bir zararın ardından karşılık verme veya öç alma talebinin sürmesini anlatır."}],"source_phrase_ar":"الوتر الذحل (maqayis)؛ الوتر الترة... قتلت له ولدا أو قريبا (jamhara)؛ الوتر بالفتح الذحل والموتور الذي قتل له قتيل (sihah)؛ الأوتار والذحول... قتل له قتيلا أو أخذت له مالا (tahdhib)؛ الوتر والترة الذحل وقد وترته إذا أصبته بمكروه (mufradat)","source_summary":"Kaynaklar anlamı, öldürme veya başka ağır bir zarar yüzünden doğan öç alacağı çevresinde birleştirir. Yakını öldürülen ya da malı alınan kişinin karşılığı henüz elde edememesi, mağdurun durumunu belirleyen ortak unsurdur.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الترة والذحل، وأن يصاب المرء بقتل قريب أو أخذ مال أو أهل أو مكروه يجعله موتورا.","what_is_not_ar":"لا يدخل فيه النقص المجرد في الثواب أو العمل إلا حيث فسر بالنقص والسلب."},"support_links":["sup_6f8a39509bae87541e7c"]},{"boundary":"Anlam yalnız hak ve yapılan işlerin karşılığıyla kurulan kalıplarda geçerlidir; her türlü nicelik azalmasına genellenemez.","branch_kind":"collocation","branch_ref":"root_001621/B003","candidate_links":[{"candidate_id":"cand_10766f5b280be74cfdca","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَتْر","morph_features":"STEM|POS:N|LEM:wator|ROOT:wtr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:2:3","qac_word_ref":"89:3:2","surface_ar":"وَتْرِ"}],"gloss":"hakkını veya karşılığını eksiltmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin hakkını ya da yaptığı işlerin karşılığını eksiltme veya elinden alma."}}],"root_ar":"و ت ر","root_id":"root_001621","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye ait hak ya da yaptığı işlerden doğan karşılık azaltıldığında kullanılan kalıba bağlı karşılıktır.","boundary_detail":"Anlam yalnız hak ve yapılan işlerin karşılığıyla kurulan kalıplarda geçerlidir; her türlü nicelik azalmasına genellenemez.","branch_image_ar":"نقص يسلب حقا أو عملا","concept_gloss":"hakkını veya karşılığını eksiltmek","contextual_glosses":[{"applicability":"Bir kimsenin mal, aile veya başka bir hak bakımından payı azaltıldığında doğal bir bağlamsal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hak sahibinin payında yapılan eksiltmeyi açıkça korur."},"facet_ids":["F001"],"text":"hakkını kısmak","usage_role":"contextual"}],"definition":"Bir kimsenin hakkını elinden almak veya eksiltmek ya da yaptığı işlerin karşılığından bir bölüm azaltmaktır. Anlam, hak ve iş karşılığı bildiren tamamlayıcılarla sınırlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin hakkını ya da yaptığı işlerin karşılığını eksiltme veya elinden alma."}],"identity_rationale":"Kaynak ifadesi anlamı belirli nesnelerle kurar: birinin hakkını eksiltmek veya kişiyi yaptığı işlerin karşılığından yoksun bırakmak. Bu nedenle dal bağımsız bir genel eksilme anlamı değildir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"hakkını eksiltmek veya elinden almak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"işlerinizi veya karşılığını eksiltmeyecek"}],"lexicalization_note":"Dal bütünüyle kalıba bağlıdır: kişinin hakkını eksiltme ve yaptığı işlerin karşılığını azaltmama kullanımları, çıplak biçime taşınmadan tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel eksilme dalı kalıba bağlı sınırı en iyi gösterdi, yoksun bırakma, hakkın varlığı ve yok etme adayları farklı işlemler anlattığı için elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda eksilen şey bir kişiye ait hak edilmiş paydır ve anlam belirli kalıplarda gerçekleşir; komşu dal ise nesne ve bağlam bakımından genel eksilmeyi kapsar.","focus_only":"Bu dal eksiltmeyi bir hak sahibine ve onun hakkına veya iş karşılığına bağlayan belirli kalıplarla sınırlar.","gloss":"hak eksiltme ve genel azalma","neighbor_only":"Komşu dal bir işin, hakkın veya herhangi bir şeyin azalmasını daha genel bir kapsamda anlatır.","neighbor_ref":"root_000044/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da mevcut bir miktardan bir bölümün azaltılması ortak anlam alanını oluşturur."}],"source_phrase_ar":"وتره حقه أي نقصه وقوله ولن يتركم أعمالكم أي لن يتنقصكم (sihah)؛ وتر أهله وماله أي نقص أهله وماله... لن ينقصكم من ثوابكم شيئا (tahdhib)","source_summary":"Kaynaklar, kişinin hakkını eksiltme ile yaptığı işlerin karşılığından hiçbir şey azaltmama kullanımlarını aynı kalıba bağlı anlamda birleştirir. Ortak çekirdek, hak edilmiş payın sahibinden eksiltilmesidir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه وتره حقه أو أهله وماله بمعنى أنقصه، وتفسير لن يتركم بأنه لا ينقصكم.","what_is_not_ar":"لا يدخل فيه مجرد الفردية، ولا طلب الثأر إلا حيث فسر بالسلب أو النقص."},"support_links":["sup_6f8a39509bae87541e7c"]},{"boundary":"Kesintisiz ve bitişik devamlılık bu dala girmez; öğeler tek tek birbirini izler ve aralarında bir süre bulunur.","branch_kind":"mixed_non_bare","branch_ref":"root_001621/B004","candidate_links":[{"candidate_id":"cand_fda41ca5d856dae9acc1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَتْر","morph_features":"STEM|POS:N|LEM:wator|ROOT:wtr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:2:3","qac_word_ref":"89:3:2","surface_ar":"وَتْرِ"}],"gloss":"aralıklı tek tek ardışıklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Öğelerin kesintisiz bir yığın oluşturmadan, aralarında süre bulunacak biçimde birer birer ardışık gelmesi."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir hayvanın çökerken uzuvlarını bekleyerek sırayla yere koyması."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Haber veya yazıları kısa aralarla peş peşe gönderme ve oruç günlerini ara günlerle dönüşümlü sürdürme."}}],"root_ar":"و ت ر","root_id":"root_001621","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Öğeler veya olaylar birer birer gelip aralarında süre bıraktığında kullanılan en kapsamlı karşılıktır.","boundary_detail":"Kesintisiz ve bitişik devamlılık bu dala girmez; öğeler tek tek birbirini izler ve aralarında bir süre bulunur.","branch_image_ar":"تعاقب فرادى بينهما فترات","concept_gloss":"aralıklı tek tek ardışıklık","contextual_glosses":[{"applicability":"Haberlerin veya yazıların biri diğerini izleyecek, fakat aralarında kısa süre bulunacak biçimde gönderilmesinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gönderilerin ardışıklığını ve aralarındaki kısa süreyi birlikte korur."},"facet_ids":["F003"],"text":"ara vererek peş peşe göndermek","usage_role":"contextual"},{"applicability":"Bir veya iki günlük oruç dönemlerinin benzer uzunlukta ara dönemleriyle dönüşümlü tutulması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uygulama dönemleri arasında düzenli ara bırakılmasını korur."},"facet_ids":["F003"],"text":"gün aşırı sürdürmek","usage_role":"contextual"}],"definition":"Aynı türden olay veya öğelerin, aralarında kısa ya da belirgin bir süre bulunarak birer birer birbirini izlemesidir. Hayvanın uzuvlarını sırayla yere koyması, haberlerin aralıklı gönderilmesi ve günler arasında ara verilen oruç düzeni bu çekirdeğin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Öğelerin kesintisiz bir yığın oluşturmadan, aralarında süre bulunacak biçimde birer birer ardışık gelmesi."},{"facet_id":"F002","role":"example","statement":"Bir hayvanın çökerken uzuvlarını bekleyerek sırayla yere koyması."},{"facet_id":"F003","role":"specialization","statement":"Haber veya yazıları kısa aralarla peş peşe gönderme ve oruç günlerini ara günlerle dönüşümlü sürdürme."}],"identity_rationale":"Kaynak ifadesi yalnız ardışıklığı değil, öğelerin birer birer gelmesini ve aralarında kısa da olsa süre bulunmasını kurucu koşul olarak belirtir. Örnekler bu aralıklı düzeni doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"aralarında süre bulunan tek tek ardışıklık"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"birer birer peş peşe gelme"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"aralıklı olarak birbiri ardından"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"çökerken uzuvlarını bekleyerek sırayla yere koyan dişi deve"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"haberleri veya yazıları kısa aralarla peş peşe göndermek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir veya iki gün tutup aynı süre ara vererek oruç tutmak"}],"lexicalization_note":"Ad ve eylem biçimleri aralıklı tek tek ardışıklığı taşır; hayvanın çökmesi, haber iletme ve oruç düzeni yalnız kendi kalıplarındaki örneklerdir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel izleme dalı aralık koşulunu en iyi görünür kıldığı için seçildi, başlangıç, zaman sorusu ve yalnız aynı kökü taşıyan dallar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal genel ardışıklığın daha dar bir türüdür: gelenler tek tek ilerler ve aralarında süre vardır. Komşu dal kesintisiz ya da yalnızca sıraya dayalı izlemeyi de kapsayabilir.","focus_only":"Bu dalda öğelerin tek tek gelmesi ve aralarında bir süre bulunması zorunludur.","gloss":"aralıklı ve genel ardışıklık","neighbor_only":"Komşu dal genel izleme ve art arda gelmeyi kapsar; aralık bulunmasını kurucu koşul yapmaz.","neighbor_ref":"root_000556/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir olayın veya öğenin başka bir olay ya da öğenin ardından gelmesini anlatır."}],"source_phrase_ar":"لا تكون مواترة إلا إذا وقعت بينهما فترة (maqayis)؛ المواترة المتابعة... وقعت بينهم فترة... تترى من الوتر أي واحدا بعد واحد (sihah)؛ واترت الخبر أتبعت بعضه بعضا وبين الخبرين هنيهة... تترى متقطعة متفاوتة الأوقات (tahdhib)؛ التواتر تتابع الشيء وترا وفرادى وجاءوا تترى (mufradat)","source_summary":"Kaynaklar, bir şeyin ardından benzerinin gelmesini tek başına yeterli görmez; arada bir süre bulunmasını ve gelişin tek tek olmasını anlamın parçası sayar. Çökme, haber gönderme ve oruç düzeni örnekleri bu aralıklı ardışıklığı farklı alanlarda gösterir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه المواترة والتواتر وتترى: مجيء الشيء بعد الشيء فرادى، مع فترة أو هنيهة، لا على المواصلة التامة.","what_is_not_ar":"لا يدخل فيه المداركة والمواصلة بلا فترة، ولا وتيرة العادة الثابتة إلا بعلاقة الاشتقاق."},"support_links":["sup_81845ed399f451dce7cf"]},{"boundary":"Dal, işteki veya gidişteki duraksamayı değil, davranışın ya da durumun aynı düzen üzerinde sürmesini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001621/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَتْر","morph_features":"STEM|POS:N|LEM:wator|ROOT:wtr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:2:3","qac_word_ref":"89:3:2","surface_ar":"وَتْرِ"}],"gloss":"değişmeyen düzen ve süreklilik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş veya durumun aynı yol, düzen ve doğrultu üzerinde değişmeden sürmesi."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sürekli tekrarlanan yolun kişide yerleşik alışkanlık veya huy durumuna gelmesi."}}],"root_ar":"و ت ر","root_id":"root_001621","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin, davranışın veya durumun aynı çizgide kararlı biçimde sürmesini genel olarak karşılar.","boundary_detail":"Dal, işteki veya gidişteki duraksamayı değil, davranışın ya da durumun aynı düzen üzerinde sürmesini anlatır.","branch_image_ar":"طريقة ثابتة على نسق واحد","concept_gloss":"değişmeyen düzen ve süreklilik","contextual_glosses":[{"applicability":"Bir kişinin işinde veya durumunda yön ve yöntem değiştirmeden devam etmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kararlı yöntemi ve zaman içindeki kesintisiz sürmeyi korur."},"facet_ids":["F001"],"text":"aynı çizgide sürmek","usage_role":"contextual"}],"definition":"Bir işin, davranışın veya durumun değişmeden aynı yol ve düzen üzerinde sürmesi; bunun sürekli uygulamaya ya da yerleşik huya dönüşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş veya durumun aynı yol, düzen ve doğrultu üzerinde değişmeden sürmesi."},{"facet_id":"F002","role":"extension","statement":"Sürekli tekrarlanan yolun kişide yerleşik alışkanlık veya huy durumuna gelmesi."}],"identity_rationale":"Kaynak ifadesi aynı yol veya düzen üzerinde değişmeden sürmeyi, bir işi sürekli yapmayı ve yerleşik yaradılış özelliğini ortak bir kararlılık çekirdeğinde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"değişmeyen yol, süreklilik ve yerleşik huy"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"aynı yöntem ve doğrultuda değişmeden"}],"lexicalization_note":"Ad biçimi yerleşik yöntem, süreklilik ve huyu kapsar; aynı çizgide sürme anlamı ayrıca belirli bir kalıpla somutlaşır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; alışılmış yöntem dalı süreklilik sınırını en iyi gösterdi, huy, yaşam tarzı ve direnme adayları daha uzak kapsamlar taşıdığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeğinde zaman boyunca aynı çizgiyi koruma vardır. Komşu dalda ise bir yolun alışılmış olması yeterlidir; o yolun her durumda kesintisiz sürmesi gerekmez.","focus_only":"Bu dal aynı düzenin değişmeden sürmesini ve devamlılığın yerleşik huya dönüşmesini özellikle vurgular.","gloss":"süreklilik ve alışılmış yöntem","neighbor_only":"Komşu dal alışılmış yol veya yöntemi kapsar; uygulamanın kesintisiz ve değişmez sürmesini zorunlu kılmaz.","neighbor_ref":"root_000240/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin izlediği yerleşik yol, yöntem veya davranış biçimini anlatır."}],"source_phrase_ar":"الوتيرة المداومة على الشيء (maqayis)؛ على وتيرة من أمره أي على طريقة واحدة واستقامة (jamhara)؛ الوتيرة الطريقة... على وتيرة واحدة (sihah)؛ على وتيرة واحدة... المداومة على الشيء (tahdhib)؛ الوتيرة السجية من التواتر (mufradat)","source_summary":"Kaynaklar aynı yol üzerinde sürme, bir işi devamlı yapma ve yerleşik huy anlamlarını birbirine bağlı verir. Ortak nokta, davranış veya durumun değişmeden kararlı bir düzen izlemesidir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الوتيرة بمعنى الطريقة الواحدة والاستقامة والمداومة والسجية في العمل أو الحال.","what_is_not_ar":"لا يدخل فيه الفتور أو الفترة المسماة وتيرة في غير هذا السياق، ولا الشريط الأرضي المحسوس."},"support_links":[]},{"boundary":"Dal yerleşik tembellik ya da değişmeyen yöntem değil, belirli bir iş veya gidiş içinde ortaya çıkan duraklama ve hız düşüşüdür.","branch_kind":"mixed_non_bare","branch_ref":"root_001621/B006","candidate_links":[{"candidate_id":"cand_fda41ca5d856dae9acc1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَتْر","morph_features":"STEM|POS:N|LEM:wator|ROOT:wtr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:2:3","qac_word_ref":"89:3:2","surface_ar":"وَتْرِ"}],"gloss":"işte veya gidişte duraksama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sürmekte olan iş veya gidiş içinde ortaya çıkan geçici ara, gevşeme veya hız düşüşü."}}],"root_ar":"و ت ر","root_id":"root_001621","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sürmekte olan çalışma, hareket veya yol alış sırasında geçici bir gevşeme ya da ara oluştuğunda kullanılır.","boundary_detail":"Dal yerleşik tembellik ya da değişmeyen yöntem değil, belirli bir iş veya gidiş içinde ortaya çıkan duraklama ve hız düşüşüdür.","branch_image_ar":"فتور يقع في العمل أو السير","concept_gloss":"işte veya gidişte duraksama","contextual_glosses":[{"applicability":"Bir işte veya gidişte hiçbir ara, gevşeme ya da hız düşüşü bulunmadığını bildiren olumsuz kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duraksama ve hız düşüşünün yokluğunu doğal bir olumsuz anlatımla korur."},"facet_ids":["F001"],"text":"hiç hız kesmeden","usage_role":"contextual"}],"definition":"Bir iş, hareket veya gidiş sürerken ortaya çıkan geçici gevşeme, ara verme ya da hız düşüşüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sürmekte olan iş veya gidiş içinde ortaya çıkan geçici ara, gevşeme veya hız düşüşü."}],"identity_rationale":"Kaynak ifadesi bir işten geri kalma, iş sırasında gevşeme veya gidişte hızın düşmesi biçimindeki duraksamayı açıkça verir ve bunu sürekli yöntem anlamından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"işten veya gidişten geri kalma, duraksama"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"hiç gevşeme veya duraksama yok"}],"lexicalization_note":"Ad biçimi işte veya gidişteki duraksamayı taşır; olumsuz kalıp ise böyle bir gevşeme ya da ara bulunmadığını bildirir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gevşeklik dalı geçici akış kesintisini en iyi sınırladı, yorulma, aşırı çaba, yere çökme ve canlılık adayları farklı neden veya sonuçlara dayandığı için elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bir etkinliğin akışındaki geçici kesilmeyi anlatır; komşu dal ise kişinin bedenine veya yürüyüşüne yerleşen tembellik ve ağırlaşmayı da kapsayan daha geniş bir durumdur.","focus_only":"Bu dal belirli bir iş veya gidiş sürerken ortaya çıkan geçici ara ya da hız düşüşüne odaklanır.","gloss":"geçici duraksama ve genel ağırlaşma","neighbor_only":"Komşu dal bedensel tembellik, gevşeklik veya hastalığa bağlı genel ağırlaşmayı da kapsar.","neighbor_ref":"root_000392/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da hareketin veya çalışmanın canlılığını ve hızını yitirmesi alanında örtüşür."}],"source_phrase_ar":"الوتيرة أيضا الفترة... سير ليست فيه وتيرة أي فتور (sihah)؛ الوتيرة في غير هذا الفترة عن الشيء والعمل (tahdhib)","source_summary":"Kaynaklar anlamı, çalışma ya da gidiş sırasında oluşan ara ve gevşeme çevresinde birleştirir. Olumsuz kalıp, işte veya yürüyüşte hiçbir duraksama bulunmadığını söyleyerek aynı çekirdeği doğrular.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الوتيرة بمعنى الفترة والفتور عن الشيء والعمل أو في السير.","what_is_not_ar":"لا يدخل فيه الوتيرة بمعنى المداومة والطريقة الواحدة."},"support_links":["sup_81845ed399f451dce7cf"]},{"boundary":"Anlam yayla kurulan ad ve eylem kalıplarına bağlıdır; başka ipler, atış araçları veya sayısal kullanımlar bu dala girmez.","branch_kind":"collocation","branch_ref":"root_001621/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَتْر","morph_features":"STEM|POS:N|LEM:wator|ROOT:wtr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:2:3","qac_word_ref":"89:3:2","surface_ar":"وَتْرِ"}],"gloss":"yay kirişi ve yayı kirişleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yayın iki ucuna bağlanıp onu gerili tutan kiriş."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yayın iki ucuna kiriş takıp yayı germe ve kullanıma hazırlama eylemi."}}],"root_ar":"و ت ر","root_id":"root_001621","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yayın gerili ipini ve bu ipi yaya takma eylemini birlikte temsil eden kalıba bağlı karşılıktır.","boundary_detail":"Anlam yayla kurulan ad ve eylem kalıplarına bağlıdır; başka ipler, atış araçları veya sayısal kullanımlar bu dala girmez.","branch_image_ar":"وتر يشد القوس","concept_gloss":"yay kirişi ve yayı kirişleme","contextual_glosses":[{"applicability":"Yayın iki ucuna gerili ip bağlanarak atışa hazır duruma getirilmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kirişi yaya takma ve yayı germe eylemlerini açıkça korur."},"facet_ids":["F002"],"text":"yaya kiriş takmak","usage_role":"contextual"}],"definition":"Yayı iki ucundan gerili tutan kiriş ve yayı bu kirişi takarak atışa hazır duruma getirme eylemidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yayın iki ucuna bağlanıp onu gerili tutan kiriş."},{"facet_id":"F002","role":"associated_use","statement":"Yayın iki ucuna kiriş takıp yayı germe ve kullanıma hazırlama eylemi."}],"identity_rationale":"Kaynak ifadesi hem yayı gerili tutan kirişi hem de yayı bu kirişle donatma eylemini açıkça verir. Dal, sayısal tekliği veya öç anlamındaki çoğul biçimi kapsamaz.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yay kirişi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yaya kiriş takıp germek"}],"lexicalization_note":"Dal yalnız yayla kurulan kalıplarda geçerlidir: bir kullanım yayın kirişi olan nesneyi, diğeri yaya kiriş takma eylemini anlatır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayın bütünüyle kurulan tematik ilişki parça sınırını en iyi gösterdi, ok, uç, yapıştırıcı ve yay türleri yalnız aynı araç alanına ait daha uzak adaylardır.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Bu dal yayın belirli bir parçası ve o parçayı takma eylemidir; komşu dal ise parçayı taşıyan atış aracının bütünüdür. Aynı sahneye aittirler, fakat anlam çekirdekleri örtüşmez.","focus_only":"Bu dal yayı geren kiriş ile kirişi yaya takma eylemini anlatır.","gloss":"yay kirişi ve yay","neighbor_only":"Komşu dal, okun fırlatıldığı yay aracının kendisini ve ona bağlı genel adları anlatır.","neighbor_ref":"root_001269/B003","relation_type":"thematic","shared_zone":"Her iki dal da ok atmada kullanılan yayın parçaları ve hazırlanmasıyla aynı araç alanına katılır."}],"source_phrase_ar":"وتر القوس معروف... وترتها وأوترتها (maqayis)؛ الوتر وتر القوس معروف (jamhara)؛ الوتر بالتحريك واحد أوتار القوس... أوتر قوسه ووترها (sihah)؛ أوتار القسي... قلدوا الخيل ولا تقلدوها الأوتار (tahdhib)","source_summary":"Kaynaklar yayın kirişi olan nesneyi ortaklaşa tanır ve aynı biçim ailesini yaya kiriş takma eylemi için de kullanır. Nesne ile eylem aynı yay kalıbına bağlıdır.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه وتر القوس وأوتار القسي، وفعل وتر القوس أو أوترها.","what_is_not_ar":"لا يدخل فيه الوتر العددي ولا الأوتار بمعنى الذحول."},"support_links":[]},{"boundary":"Çekirdek yuvarlak alıştırma hedefidir; beden lekeleri, yara ve çiçek adları yalnız biçim benzerliğine dayalı uzantılardır.","branch_kind":"bare","branch_ref":"root_001621/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَتْر","morph_features":"STEM|POS:N|LEM:wator|ROOT:wtr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:2:3","qac_word_ref":"89:3:2","surface_ar":"وَتْرِ"}],"gloss":"halka hedef ve benzeri yuvarlak iz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Saplama veya atış çalışmasında hedef olarak kullanılan halka biçimli nesne."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Halkaya benzetilen yuvarlak at alın lekesi, yara ve beyaz ya da küçük gül."}}],"root_ar":"و ت ر","root_id":"root_001621","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Alıştırma halkasını çekirdek, aynı yuvarlak biçime benzetilen işaretleri uzantı olarak birlikte temsil eder.","boundary_detail":"Çekirdek yuvarlak alıştırma hedefidir; beden lekeleri, yara ve çiçek adları yalnız biçim benzerliğine dayalı uzantılardır.","branch_image_ar":"حلقة أو علامة مستديرة يتدرب عليها","concept_gloss":"halka hedef ve benzeri yuvarlak iz","contextual_glosses":[{"applicability":"Saplama ya da atış becerisini geliştirmek için hedef alınan halka biçimli nesne bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin halka biçimini ve alıştırma hedefi olma işlevini korur."},"facet_ids":["F001"],"text":"halka biçimli alıştırma hedefi","usage_role":"general"},{"applicability":"Atın alnındaki yuvarlak işaret veya halka biçimine benzetilen yara ve benzeri görünüşler için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşaretin yuvarlaklığını ve halka hedeften kurulan benzetme ilişkisini korur."},"facet_ids":["F002"],"text":"halkaya benzeyen yuvarlak leke","usage_role":"explanatory"}],"definition":"Saplama veya atış çalışmasında hedef olarak kullanılan halka biçimli nesnedir; halkaya benzeyen yuvarlak at alın lekesi, yara ve beyaz ya da küçük gül de benzetme yoluyla aynı adla anılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Saplama veya atış çalışmasında hedef olarak kullanılan halka biçimli nesne."},{"facet_id":"F002","role":"extension","statement":"Halkaya benzetilen yuvarlak at alın lekesi, yara ve beyaz ya da küçük gül."}],"identity_rationale":"Kaynak ifadesi saplama veya atış çalışmasında kullanılan halkayı çekirdek yapar; atın yuvarlak alın lekesi, yuvarlak yara ve beyaz ya da küçük gül adlarını halka benzerliğine bağlı uzantılar olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"saplama veya atış çalışması için halka biçimli hedef"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"halkaya benzetilen yuvarlak alın lekesi, yara veya çiçek"}],"lexicalization_note":"Dal çıplak biçimin kendi anlamını tanımlar: halka biçimli alıştırma hedefi çekirdektir ve yuvarlak işaret adları bu çekirdeğin benzetmeye dayalı uzantılarıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel halka dalı işlevsel uzmanlaşmayı en iyi gösterdi, yara izi, hayvan damgası ve başka yuvarlak işaret adayları çekirdeğin yalnız birer biçim komşusudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal işlev ve adlandırma bakımından özelleşmiştir: çekirdek bir alıştırma hedefidir, diğer kullanımlar ona benzetilir. Komşu dal ise halka ve yuvarlaklığı nesne türü bakımından genişçe kapsar.","focus_only":"Bu dal özel olarak alıştırma hedefi olan halkayı ve ona benzetilen belirli yuvarlak işaretleri adlandırır.","gloss":"alıştırma halkası ve genel halka","neighbor_only":"Komşu dal metal, kapı, topluluk, zırh ve gök cismi gibi alanlardaki halkayı ve dönüklüğü genel olarak kapsar.","neighbor_ref":"root_000350/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalın ortak alanı kapalı, yuvarlak veya halka biçimli nesne ve işaretlerdir."}],"source_phrase_ar":"الوتيرة غرة الفرس مستديرة وشيء يتعلم عليه الطعن (maqayis)؛ الوتيرة حلقة يتعلم عليها الطعن... قرحة الفرس... الوردة البيضاء (jamhara)؛ الوتيرة حلقة من عقب يتعلم فيها الطعن (sihah)؛ غرة الفرس إذا كانت مستديرة... الحلقة التي يتعلم عليها الطعن... الوردة البيضاء والوردة الصغيرة (tahdhib)؛ الحلقة التي يتعلم عليها الرمي الوتيرة (mufradat)","source_summary":"Kaynaklar halka biçimli alıştırma hedefinde birleşir ve saplama ya da atış çalışmasını işlev olarak belirtir. Yuvarlak at alın lekesi, yara ve çiçek adları, bu halkanın biçimine benzetilen ikincil kullanımlardır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الوتيرة حلقة التدريب على الطعن أو الرمي، وما شبه بها من غرة الفرس المستديرة أو القرحة أو الوردة البيضاء/الصغيرة.","what_is_not_ar":"لا يدخل فيه وتر القوس نفسه، ولا الحاجز الأنفي أو الأوتار التشريحية."},"support_links":[]},{"boundary":"Dal burun bölmesini merkez alır, fakat başka beden yerlerindeki ince deri veya kıkırdak ayırıcıları ve nesne kenarlarını da kapsar.","branch_kind":"bare","branch_ref":"root_001621/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَتْر","morph_features":"STEM|POS:N|LEM:wator|ROOT:wtr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:2:3","qac_word_ref":"89:3:2","surface_ar":"وَتْرِ"}],"gloss":"burun bölmesi ve benzeri ince ayırıcı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Burun delikleri arasındaki ayırıcı bölme veya burun ucu."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki parmak arasındaki ince deri, kulak içindeki kıkırdak veya bir şeyin ayırıcı kenarı."}}],"root_ar":"و ت ر","root_id":"root_001621","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Burundaki merkezi anatomik kullanımı ve başka yerlerdeki ince deri, kıkırdak veya kenar uzantılarını birlikte karşılar.","boundary_detail":"Dal burun bölmesini merkez alır, fakat başka beden yerlerindeki ince deri veya kıkırdak ayırıcıları ve nesne kenarlarını da kapsar.","branch_image_ar":"حاجز رقيق بين شقين","concept_gloss":"burun bölmesi ve benzeri ince ayırıcı","contextual_glosses":[{"applicability":"Burun içindeki iki deliği birbirinden ayıran anatomik yapı söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapının burundaki yerini ve iki deliği ayırma işlevini korur."},"facet_ids":["F001"],"text":"burun delikleri arasındaki bölme","usage_role":"general"},{"applicability":"Parmak arası deri, kulak içi kıkırdak veya benzer ince anatomik ayırıcılar söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnce doku yapısını ve iki konum arasında ayırıcı olmasını korur."},"facet_ids":["F002"],"text":"ince ayırıcı deri veya kıkırdak","usage_role":"explanatory"}],"definition":"Başta burun delikleri arasındaki bölme veya burun ucu olmak üzere, iki yeri ayıran ince deri, kıkırdak ya da sınır oluşturan kenardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Burun delikleri arasındaki ayırıcı bölme veya burun ucu."},{"facet_id":"F002","role":"extension","statement":"İki parmak arasındaki ince deri, kulak içindeki kıkırdak veya bir şeyin ayırıcı kenarı."}],"identity_rationale":"Burun delikleri arasındaki bölme kaynak ifadesinin merkezidir; ancak kaynak ayrıca burun ucunu, iki parmak arasındaki ince deriyi, kulak içindeki kıkırdağı ve bir şeyin kenarını da kapsar. Bu nedenle yalnız iki yarık arasındaki ince engel çerçevesi dar kalır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"burun delikleri arasındaki bölme veya burun ucu"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"iki yeri ayıran ince deri, kıkırdak veya kenar"}],"lexicalization_note":"Dal çıplak biçimin anatomik bölme ve kenar anlamını tanımlar; burun bölmesi çekirdektir, benzer ince deri, kıkırdak ve kenarlar kapsam uzantılarıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel engel dalı anatomik ve ince yapı sınırını en iyi gösterdi, burun, kemik derisi, eklem ve karın zarı adayları yalnız komşu beden bölümleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal küçük ve somut bir anatomik bölme ya da ince kenar türüdür. Komşu dalın kapsamı ise maddi engellerden soyut önleyicilere kadar geniştir ve belirli bir doku yapısı gerektirmez.","focus_only":"Bu dal burun bölmesi başta olmak üzere ince anatomik doku, kıkırdak ve nesne kenarıyla sınırlı fiziksel ayırıcıları anlatır.","gloss":"ince anatomik bölme ve genel engel","neighbor_only":"Komşu dal iki şey arasındaki her türlü fiziksel veya soyut engeli, sınırı ve uzaklığı genel olarak kapsar.","neighbor_ref":"root_000106/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da iki konum veya şeyi birbirinden ayıran bir sınır ya da aracı yapı anlamında örtüşür."}],"source_phrase_ar":"الوترة طرف الأنف (maqayis)؛ الوترة الحائلة بين المنخرين في الأنف (jamhara)؛ وترة الأنف حجاب ما بين المنخرين... وترة كل شيء حتاره (sihah)؛ الوترة جليدة بين الإبهام والسبابة... الحاجز بين المنخرين... غريضيف في جوف الأذن... حتار كل شيء وتره (tahdhib)؛ الوتيرة الحاجز بين المنخرين (mufradat)","source_summary":"Kaynaklar burun delikleri arasındaki bölmeyi ortak merkez olarak verir. Burun ucu, iki parmak arasındaki ince deri, kulak içindeki kıkırdak ve nesnenin ayırıcı kenarı, ince bölme veya sınır işlevinin beden ve nesnelere yayılan kullanımlarıdır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الوترة أو الوتيرة للحاجز بين المنخرين، وطرف الأنف، والجليدة أو الغريضيف أو الحتار في أعضاء أو أشياء.","what_is_not_ar":"لا يدخل فيه وتر القوس، ولا حلقة التدريب المستديرة."},"support_links":[]},{"boundary":"Dal yalnız fiziksel arazi şeridi ve aynı doğrultuda kurulmuş sıra için geçerlidir; soyut yöntem veya alışkanlık anlamına genişletilemez.","branch_kind":"mixed_non_bare","branch_ref":"root_001621/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَتْر","morph_features":"STEM|POS:N|LEM:wator|ROOT:wtr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:2:3","qac_word_ref":"89:3:2","surface_ar":"وَتْرِ"}],"gloss":"uzun arazi şeridi ve doğrusal sıra","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Arazide uzunlamasına uzanan parça, şerit veya yol."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Evlerin aynı çizgi üzerinde uzanan tek bir sıra hâlinde kurulması."}}],"root_ar":"و ت ر","root_id":"root_001621","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Uzunlamasına uzanan toprak parçasını ve aynı çizgide kurulmuş yapı sırasını birlikte temsil eder.","boundary_detail":"Dal yalnız fiziksel arazi şeridi ve aynı doğrultuda kurulmuş sıra için geçerlidir; soyut yöntem veya alışkanlık anlamına genişletilemez.","branch_image_ar":"شريط أرض أو صف ممتد","concept_gloss":"uzun arazi şeridi ve doğrusal sıra","contextual_glosses":[{"applicability":"Çevresinden bir yol veya parça gibi ayrılan, uzun ve dar arazi kesimi söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Arazinin fiziksel oluşunu ve uzunlamasına uzanan şerit biçimini korur."},"facet_ids":["F001"],"text":"uzunlamasına toprak şeridi","usage_role":"general"},{"applicability":"Evlerin yan yana ve tek bir doğrultu üzerinde uzanan sıra hâlinde kurulması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapıların tek bir doğrultu üzerinde sıralanmasını korur."},"facet_ids":["F002"],"text":"aynı çizgi üzerinde sıra","usage_role":"contextual"}],"definition":"Yerde uzunlamasına uzanan parça, şerit veya yoldur; evlerin aynı çizgi üzerinde bir sıra hâlinde kurulması da bu doğrusal biçimin kalıba bağlı uygulamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Arazide uzunlamasına uzanan parça, şerit veya yol."},{"facet_id":"F002","role":"specialization","statement":"Evlerin aynı çizgi üzerinde uzanan tek bir sıra hâlinde kurulması."}],"identity_rationale":"Kaynak ifadesi yerde uzanan uzun bir parça veya yol ile evlerin aynı çizgi üzerinde kurulmasını açıkça birleştirir. Buradaki yol, davranış yöntemi değil fiziksel arazi şerididir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"uzunlamasına uzanan toprak parçası veya yol"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"aynı çizgi üzerinde uzanan sıra"}],"lexicalization_note":"Ad biçimi uzun arazi parçasını veya yolunu anlatır; evlerin bir çizgide kurulması ise yalnız sıra bildiren kalıpta geçerli özel kullanımdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel arazi parçası dalı uzun şerit sınırını en iyi gösterdi, kum çizgisi, geniş alan, yerleşim yeri ve karşılıklı yapılar başka fiziksel düzenleri anlattığı için elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın ayırıcı niteliği uzunlamasına ve şerit biçiminde uzanıştır. Komşu dalda ise parçanın çevresinden farklı olması yeterlidir; biçimi yuvarlak, geniş veya düzensiz olabilir.","focus_only":"Bu dal arazi parçasının uzun ve dar biçimde tek bir doğrultu üzerinde uzanmasını gerektirir.","gloss":"uzun şerit ve genel arazi parçası","neighbor_only":"Komşu dal çevresinden farklılaşan herhangi bir arazi parçasını kapsar ve uzunluk ya da doğrultu koşulu koymaz.","neighbor_ref":"root_000140/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da çevresinden ayrılabilen belirli bir toprak veya arazi kesimini anlatır."}],"source_phrase_ar":"الوتيرة قطعة تغلظ وتستحق من الأرض وتستطيل... على وتيرة أي على سطر (jamhara)؛ الوتيرة من الأرض الطريقة (sihah)؛ الوتيرة من الأرض ولم يحدها (tahdhib)؛ الأرض المنقادة (mufradat)","source_summary":"Kaynaklar yerde uzanan parça veya yol anlamında birleşir ve bu arazi biçiminin uzunlamasına olduğunu belirtir. Evlerin aynı çizgi üzerinde kurulması, doğrusal uzanışın yapı düzenine aktarılan özel kullanımıdır.","sources":["JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الوتيرة من الأرض: طريقة أو قطعة مستطيلة، وبناء البيوت على سطر.","what_is_not_ar":"لا يدخل فيه الطريقة المجازية في السلوك أو الحال إلا إذا كان السياق أرضا أو صفا حسيا."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["89:3:1"],"branch_refs":[],"candidate_id":"cand_e2c8aac33cff46ead398","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:3:1:bound-surface","source_type":"word_analysis","support_ids":["sup_5e77fe68cc6df4bd2584","sup_705f26e5a77ce011ae5a"],"title":"bound particle-noun onset","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:1","qac_refs":["89:3:1:1"],"status":"accepted"}},{"anchor_refs":["89:3:1"],"branch_refs":[],"candidate_id":"cand_d281d2c21a1720797401","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:3:1:chain-continuation","source_type":"word_analysis","support_ids":["sup_5e77fe68cc6df4bd2584","sup_ec5c8c3f93c1a4512928"],"title":"continued oath chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:1","qac_refs":["89:3:1:1"],"status":"accepted"}},{"anchor_refs":["89:3:1"],"branch_refs":[],"candidate_id":"cand_75a7cda16fc00d8dba59","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:3:1:oath-governance","source_type":"word_analysis","support_ids":["sup_00dec68a31ff3aa12c34","sup_5e77fe68cc6df4bd2584"],"title":"oath governance over pairedness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:1","qac_refs":["89:3:1:1"],"status":"accepted"}},{"anchor_refs":["89:3:1"],"branch_refs":[],"candidate_id":"cand_e14b51b3aba13b51ae58","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:3:1:refrain-frame","source_type":"word_analysis","support_ids":["sup_5e77fe68cc6df4bd2584","sup_62bc79144f2e3abde33c"],"title":"first beat of doubled refrain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:1","qac_refs":["89:3:1:1"],"status":"accepted"}},{"anchor_refs":["89:3:2"],"branch_refs":[],"candidate_id":"cand_0a4b688d7b42fbc1ab71","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000802"],"scope":"focus_ayah","source_local_id":"89:3:2:convergence","source_type":"word_analysis","support_ids":["sup_53819df61dae28c2a98a","sup_ad24ddd0bf7001863e29"],"title":"converging parity witness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:2","qac_refs":["89:3:1:2","89:3:1:3"],"status":"accepted"}},{"anchor_refs":["89:3:2"],"branch_refs":[],"candidate_id":"cand_9ff0d440e9a89571fc74","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000802"],"scope":"focus_ayah","source_local_id":"89:3:2:definite-oath-category","source_type":"word_analysis","support_ids":["sup_8cc37dd1cf066eb5d383","sup_ad24ddd0bf7001863e29"],"title":"definite oath category","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:2","qac_refs":["89:3:1:2","89:3:1:3"],"status":"accepted"}},{"anchor_refs":["89:3:2"],"branch_refs":[],"candidate_id":"cand_06be6994952c50aecb2f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000802"],"scope":"focus_ayah","source_local_id":"89:3:2:form-selection","source_type":"word_analysis","support_ids":["sup_837464135c4793249bee","sup_ad24ddd0bf7001863e29"],"title":"abstract noun over actor or process","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:2","qac_refs":["89:3:1:2","89:3:1:3"],"status":"accepted"}},{"anchor_refs":["89:3:2"],"branch_refs":[],"candidate_id":"cand_4aa5594e1cddb90767a5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000802"],"scope":"focus_ayah","source_local_id":"89:3:2:intercession-recurrence","source_type":"word_analysis","support_ids":["sup_5338abf15d1559c5b58d","sup_ad24ddd0bf7001863e29"],"title":"intercession recurrence in the background","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:2","qac_refs":["89:3:1:2","89:3:1:3"],"status":"accepted"}},{"anchor_refs":["89:3:2"],"branch_refs":[],"candidate_id":"cand_4b73ae0f80fcd9186c50","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000802"],"scope":"focus_ayah","source_local_id":"89:3:2:joining-support-pressure","source_type":"word_analysis","support_ids":["sup_9d513ce4710dfc87f409","sup_ad24ddd0bf7001863e29"],"title":"joining and support pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:2","qac_refs":["89:3:1:2","89:3:1:3"],"status":"accepted"}},{"anchor_refs":["89:3:2"],"branch_refs":[],"candidate_id":"cand_7e7858df7f0b462e1b51","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000802"],"scope":"focus_ayah","source_local_id":"89:3:2:paired-odd-binary","source_type":"word_analysis","support_ids":["sup_82de70f64188e60aa22b","sup_ad24ddd0bf7001863e29"],"title":"first pole of exhaustive parity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:2","qac_refs":["89:3:1:2","89:3:1:3"],"status":"accepted"}},{"anchor_refs":["89:3:2"],"branch_refs":[],"candidate_id":"cand_f940dd8a1707d914d4df","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000802"],"scope":"focus_ayah","source_local_id":"89:3:2:prior-count-boundary","source_type":"word_analysis","support_ids":["sup_06087083d0115bac9843","sup_ad24ddd0bf7001863e29"],"title":"count becomes category","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:2","qac_refs":["89:3:1:2","89:3:1:3"],"status":"accepted"}},{"anchor_refs":["89:3:2"],"branch_refs":[],"candidate_id":"cand_b3f7321c67aaa30b489f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000802"],"scope":"focus_ayah","source_local_id":"89:3:2:sound-and-cadence","source_type":"word_analysis","support_ids":["sup_1aa001fd22f6a4f7db21","sup_ad24ddd0bf7001863e29"],"title":"compact sound in matched cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:2","qac_refs":["89:3:1:2","89:3:1:3"],"status":"accepted"}},{"anchor_refs":["89:3:3"],"branch_refs":[],"candidate_id":"cand_d36e0205aa319d9da5c5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:3:3:convergence","source_type":"word_analysis","support_ids":["sup_4d00ddfef2feb1aaea0d","sup_6cf96f1cf1041b3d96e0"],"title":"balanced binary mechanism","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:3","qac_refs":["89:3:2:1"],"status":"accepted"}},{"anchor_refs":["89:3:3"],"branch_refs":[],"candidate_id":"cand_963253dc658496a1c436","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:3:3:coordination-and-renewal","source_type":"word_analysis","support_ids":["sup_4602710fcfd57fa51f18","sup_4d00ddfef2feb1aaea0d"],"title":"coordination with renewed oath scope","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:3","qac_refs":["89:3:2:1"],"status":"accepted"}},{"anchor_refs":["89:3:3"],"branch_refs":[],"candidate_id":"cand_9cb179a0e8b01b9fe5cf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:3:3:hinge-pivot","source_type":"word_analysis","support_ids":["sup_4d00ddfef2feb1aaea0d","sup_8fa4ad40d91a3761ea77"],"title":"pivot from pair to singleton","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:3","qac_refs":["89:3:2:1"],"status":"accepted"}},{"anchor_refs":["89:3:3"],"branch_refs":[],"candidate_id":"cand_6d8c01b42287f4c3473d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:3:3:mirrored-cadence","source_type":"word_analysis","support_ids":["sup_4d00ddfef2feb1aaea0d","sup_67a2188a2eb8743e3454"],"title":"mirrored two-beat frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:3","qac_refs":["89:3:2:1"],"status":"accepted"}},{"anchor_refs":["89:3:4"],"branch_refs":[],"candidate_id":"cand_240d077f0cf4e45dc0ea","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001621"],"scope":"focus_ayah","source_local_id":"89:3:4:closing-sound","source_type":"word_analysis","support_ids":["sup_8a4597e321eee765b15c","sup_cffbf90bb082a79eb08b"],"title":"clipped final closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:4","qac_refs":["89:3:2:2","89:3:2:3"],"status":"accepted"}},{"anchor_refs":["89:3:4"],"branch_refs":[],"candidate_id":"cand_417673e1c1a3d214b359","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001621"],"scope":"focus_ayah","source_local_id":"89:3:4:convergence","source_type":"word_analysis","support_ids":["sup_8a4597e321eee765b15c","sup_add9b46436454e295ab4"],"title":"concentrated endpoint","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:4","qac_refs":["89:3:2:2","89:3:2:3"],"status":"accepted"}},{"anchor_refs":["89:3:4"],"branch_refs":[],"candidate_id":"cand_b775c968fbc948469296","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001621"],"scope":"focus_ayah","source_local_id":"89:3:4:definite-oath-counterpart","source_type":"word_analysis","support_ids":["sup_10dcb10327248ba322dd","sup_8a4597e321eee765b15c"],"title":"definite sworn counterpart","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:4","qac_refs":["89:3:2:2","89:3:2:3"],"status":"accepted"}},{"anchor_refs":["89:3:4"],"branch_refs":[],"candidate_id":"cand_5c6e3ea04f89520e27bc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001621"],"scope":"focus_ayah","source_local_id":"89:3:4:deprivation-pressure","source_type":"word_analysis","support_ids":["sup_8a4597e321eee765b15c","sup_b6ecec4794aa7ae9aa00"],"title":"deprivation shadow on unpairedness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:4","qac_refs":["89:3:2:2","89:3:2:3"],"status":"accepted"}},{"anchor_refs":["89:3:4"],"branch_refs":[],"candidate_id":"cand_b9ffaa0b75947a475ba1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001621"],"scope":"focus_ayah","source_local_id":"89:3:4:interval-and-strand-pressure","source_type":"word_analysis","support_ids":["sup_8a4597e321eee765b15c","sup_afbc032923c06f8abe46"],"title":"taut single-strand and interval pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:4","qac_refs":["89:3:2:2","89:3:2:3"],"status":"accepted"}},{"anchor_refs":["89:3:4"],"branch_refs":[],"candidate_id":"cand_b0ba979b29397f08c23b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001621"],"scope":"focus_ayah","source_local_id":"89:3:4:known-category","source_type":"word_analysis","support_ids":["sup_13bdea8964a83d69c39a","sup_8a4597e321eee765b15c"],"title":"known oddness category","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:4","qac_refs":["89:3:2:2","89:3:2:3"],"status":"accepted"}},{"anchor_refs":["89:3:4"],"branch_refs":[],"candidate_id":"cand_1de74442c6ed552046bd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001621"],"scope":"focus_ayah","source_local_id":"89:3:4:odd-pole-totality","source_type":"word_analysis","support_ids":["sup_226ed29c575390d84345","sup_8a4597e321eee765b15c"],"title":"odd pole completes totality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:4","qac_refs":["89:3:2:2","89:3:2:3"],"status":"accepted"}},{"anchor_refs":["89:3:4"],"branch_refs":[],"candidate_id":"cand_10ce3ac788c2b6c34efd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001621"],"scope":"focus_ayah","source_local_id":"89:3:4:qiraat-vowel-pressure","source_type":"word_analysis","support_ids":["sup_37bc8e3587047aa8d57f","sup_8a4597e321eee765b15c"],"title":"variant vowel pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:4","qac_refs":["89:3:2:2","89:3:2:3"],"status":"accepted"}},{"anchor_refs":["89:3:4"],"branch_refs":[],"candidate_id":"cand_5ff1779365bd7bb8685a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001621"],"scope":"focus_ayah","source_local_id":"89:3:4:rare-root-concentration","source_type":"word_analysis","support_ids":["sup_794e35127d1104cc85a7","sup_8a4597e321eee765b15c"],"title":"rare root concentration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:4","qac_refs":["89:3:2:2","89:3:2:3"],"status":"accepted"}},{"anchor_refs":["89:3:4"],"branch_refs":[],"candidate_id":"cand_7058b4df43e52c1fa111","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001621"],"scope":"focus_ayah","source_local_id":"89:3:4:state-not-event","source_type":"word_analysis","support_ids":["sup_2574b3230d7f2f9da0fb","sup_8a4597e321eee765b15c"],"title":"state rather than making-odd event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:3:4","qac_refs":["89:3:2:2","89:3:2:3"],"status":"accepted"}},{"anchor_refs":["89:3:1"],"branch_refs":[],"candidate_id":"cand_d849753779575e93e2f9","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000802"],"scope":"focus_ayah","source_local_id":"89:3:1:3","source_type":"qac_morpheme","support_ids":["sup_89102135663b9a9eedd3"],"title":"QAC root occurrence: ش ف ع","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:3:2"],"branch_refs":[],"candidate_id":"cand_3ade771f9e8e79f0c518","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001621"],"scope":"focus_ayah","source_local_id":"89:3:2:3","source_type":"qac_morpheme","support_ids":["sup_f29652eff17795a57f1b"],"title":"QAC root occurrence: و ت ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:3","branch_refs":["root_000802/B001","root_001621/B001"],"candidate_id":"cand_50bafa7848e9ad2dab7d","commentary_obligation":"review","hft_ref":"hft_9aa2cbcb2498f53ca7d4","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-parity-operation","source_type":"hft","support_ids":["sup_6582a111224fc4c38fd0"],"title":"baseline-parity-operation","trust":"legacy_unbound"},{"anchor_refs":["89:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:3","branch_refs":["root_000802/B002","root_001621/B002","root_001621/B003"],"candidate_id":"cand_10766f5b280be74cfdca","commentary_obligation":"review","hft_ref":"hft_317ee736dacec5d5fad3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-advocate-and-wronged","source_type":"hft","support_ids":["sup_6f8a39509bae87541e7c"],"title":"baseline-advocate-and-wronged","trust":"legacy_unbound"},{"anchor_refs":["89:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:3","branch_refs":["root_000802/B005","root_001621/B004","root_001621/B006"],"candidate_id":"cand_fda41ca5d856dae9acc1","commentary_obligation":"review","hft_ref":"hft_fad4c88b50e683b0b397","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-clustered-and-spaced-cadence","source_type":"hft","support_ids":["sup_81845ed399f451dce7cf"],"title":"baseline-clustered-and-spaced-cadence","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱلشَّفْعِ وَٱلْوَتْرِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:3:1:1","qac_word_ref":"89:3:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:3:1:2","qac_word_ref":"89:3:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"شَّفْع","morph_features":"STEM|POS:N|LEM:$~afoE|ROOT:$fE|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:1:3","qac_word_ref":"89:3:1","root_ar":"ش ف ع","surface_ar":"شَّفْعِ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:3:2:1","qac_word_ref":"89:3:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:3:2:2","qac_word_ref":"89:3:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"وَتْر","morph_features":"STEM|POS:N|LEM:wator|ROOT:wtr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:2:3","qac_word_ref":"89:3:2","root_ar":"و ت ر","surface_ar":"وَتْرِ"}],"word_analysis_qac_refs":[["89:3:1:1"],["89:3:1:2","89:3:1:3"],["89:3:2:1"],["89:3:2:2","89:3:2:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:3:1","89:3:2","89:3:3","89:3:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلشَّفْعِ وَٱلْوَتْرِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:3:1:1","qac_word_ref":"89:3:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:3:1:2","qac_word_ref":"89:3:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"شَّفْع","morph_features":"STEM|POS:N|LEM:$~afoE|ROOT:$fE|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:1:3","qac_word_ref":"89:3:1","root_ar":"ش ف ع","surface_ar":"شَّفْعِ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:3:2:1","qac_word_ref":"89:3:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:3:2:2","qac_word_ref":"89:3:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"وَتْر","morph_features":"STEM|POS:N|LEM:wator|ROOT:wtr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:3:2:3","qac_word_ref":"89:3:2","root_ar":"و ت ر","surface_ar":"وَتْرِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:3:1:1"],["89:3:1:2","89:3:1:3"],["89:3:2:1"],["89:3:2:2","89:3:2:3"]],"word_analysis_refs":["89:3:1","89:3:2","89:3:3","89:3:4"],"word_rows":[{"analysis_record_ref":"89:3:1","analytic_gloss_range_en":"oath-bearing connective before the pairedness noun; it continues the surrounding oath chain while opening a local even-odd unit","analytic_root_gloss_range_en":null,"qac_refs":["89:3:1:1"],"root":{"note":"-"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"89:3:2","analytic_gloss_range_en":"the definite paired or even category under oath; locally selected by contrast with oddness while retaining joining and support pressure","analytic_root_gloss_range_en":"root range includes making one thing joined to another, evenness after singleness, intercession or seconding support, and other specialized joining branches; locally the parity sense is selected and the support/intercession field survives as narrowed pressure","qac_refs":["89:3:1:2","89:3:1:3"],"root":{"arabic":"ش ف ع","transliteration":"sh-f-ʿ"},"surface":{"arabic":"ٱلشَّفْعِ","transliteration":"al-shafʿi"}},{"analysis_record_ref":"89:3:3","analytic_gloss_range_en":"repeated oath-bearing connective before the oddness noun; it both coordinates the second pole with the first and renews oath force for it","analytic_root_gloss_range_en":null,"qac_refs":["89:3:2:1"],"root":{"note":"-"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"89:3:4","analytic_gloss_range_en":"the definite odd or unpaired category under oath; locally selected as the counterpart to pairedness, with deprivation, taut single-strand, and interval pressure narrowed into the sense of an unpaired remainder","analytic_root_gloss_range_en":"root range includes oddness, making odd, deprivation or wronged loss, intervallic recurrence, bowstring tension, and other concrete extensions; locally oddness is selected while the loss, interval, and taut-single fields survive as narrowed pressure","qac_refs":["89:3:2:2","89:3:2:3"],"root":{"arabic":"و ت ر","transliteration":"w-t-r"},"surface":{"arabic":"ٱلْوَتْرِ","transliteration":"al-watri"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["89:3"],"branch_refs":["root_000802/B001","root_001621/B001"],"candidate_id":"cand_50bafa7848e9ad2dab7d","evidence_scope":"focus_ayah","hft_ref":"hft_9aa2cbcb2498f53ca7d4","item_id":"baseline-parity-operation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-parity-operation","support_id":"sup_6582a111224fc4c38fd0"},{"anchor_refs":["89:3"],"branch_refs":["root_000802/B002","root_001621/B002","root_001621/B003"],"candidate_id":"cand_10766f5b280be74cfdca","evidence_scope":"focus_ayah","hft_ref":"hft_317ee736dacec5d5fad3","item_id":"baseline-advocate-and-wronged","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-advocate-and-wronged","support_id":"sup_6f8a39509bae87541e7c"},{"anchor_refs":["89:3"],"branch_refs":["root_000802/B005","root_001621/B004","root_001621/B006"],"candidate_id":"cand_fda41ca5d856dae9acc1","evidence_scope":"focus_ayah","hft_ref":"hft_fad4c88b50e683b0b397","item_id":"baseline-clustered-and-spaced-cadence","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-clustered-and-spaced-cadence","support_id":"sup_81845ed399f451dce7cf"}],"diagnostics":[],"lane_counts":{"global":14,"macro":3,"micro":3},"packet_summary":{"ayah_count":30,"focus_ref":"89:3","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":12,"unstructured_record_count":0},"identity":{"ayah_ref":"89:3","lane":"micro","linguistic_source_ref":"89:3","surface_ref":"89:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:3","target_tokens":[["Çifte",["89:3:1"]],["ve",["89:3:2"]],["teke",["89:3:2"]],["andolsun",["89:3:1","89:3:2"]]],"text":"Çifte ve teke andolsun!"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":14,"id":"s089-p01-001-014","label":"Oaths and the downfall of tyrants","number":1,"refs":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:1:oath-governance","source_type":"word_analysis","support_id":"sup_00dec68a31ff3aa12c34","text":"{\"blocking_evidence\":null,\"headline\":\"oath governance over pairedness\",\"reader_payoff\":\"The reader hears pairedness introduced as sworn evidence, not as a bare abstract topic.\",\"reason\":\"QAC and attachment evidence identify the particle as governing the following genitive noun in the compressed oath frame.\",\"representative_source_ids\":[\"QG-ca957aa0\",\"MG-495f6cd9\",\"QI-4b146de8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:2:prior-count-boundary","source_type":"word_analysis","support_id":"sup_06087083d0115bac9843","text":"{\"blocking_evidence\":null,\"headline\":\"count becomes category\",\"reader_payoff\":\"The reader notices the movement from a measured example in 89:2 to the category that classifies measured things in 89:3.\",\"reason\":\"The local oath sequence places the parity term immediately after the counted nights, allowing the boundary row's classification payoff to survive.\",\"representative_source_ids\":[\"QS-c643ead1\",\"QE-d111a2d4\",\"QB-c3ba7c7e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:4:definite-oath-counterpart","source_type":"word_analysis","support_id":"sup_10dcb10327248ba322dd","text":"{\"blocking_evidence\":null,\"headline\":\"definite sworn counterpart\",\"reader_payoff\":\"The reader sees oddness made to testify directly as the second sworn object.\",\"reason\":\"QAC and attachment evidence mark the word as a definite genitive noun governed by the repeated oath particle and coordinated with the first noun.\",\"representative_source_ids\":[\"QG-048ae291\",\"QG-14ea9580\",\"QG-ef933af5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:4:known-category","source_type":"word_analysis","support_id":"sup_13bdea8964a83d69c39a","text":"{\"blocking_evidence\":null,\"headline\":\"known oddness category\",\"reader_payoff\":\"The reader notices that the oath invokes oddness as a known category, not a stray unmatched item.\",\"reason\":\"The local form is definite singular and abstract, and the tanwīn contrast makes the received definiteness meaningful without displacing it.\",\"representative_source_ids\":[\"QG-9a569579\",\"QG-e655b00a\",\"QF-1b68773d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:2:sound-and-cadence","source_type":"word_analysis","support_id":"sup_1aa001fd22f6a4f7db21","text":"{\"blocking_evidence\":null,\"headline\":\"compact sound in matched cadence\",\"reader_payoff\":\"The reader hears the pairedness term as compact and formally balanced before the odd counterpart arrives.\",\"reason\":\"The two nouns share a short definite-genitive pattern, and the sound rows describe local recitational compression tied to the surface form.\",\"representative_source_ids\":[\"QP-9839434d\",\"QP-c97553e9\",\"QP-d6c679af\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:4:odd-pole-totality","source_type":"word_analysis","support_id":"sup_226ed29c575390d84345","text":"{\"blocking_evidence\":null,\"headline\":\"odd pole completes totality\",\"reader_payoff\":\"The reader sees the second noun complete the field of countability by naming what remains outside pairing.\",\"reason\":\"The noun is coordinated with the pairedness term, and V4 gives oddness as an accepted branch for the root.\",\"representative_source_ids\":[\"QS-2f9eb1a2\",\"QI-b9c1c085\",\"QT-ff377277\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:4:state-not-event","source_type":"word_analysis","support_id":"sup_2574b3230d7f2f9da0fb","text":"{\"blocking_evidence\":null,\"headline\":\"state rather than making-odd event\",\"reader_payoff\":\"The reader notices that the oath presents unpairedness as a standing category, not as an event with an actor.\",\"reason\":\"The surface is a noun in the oath frame, so verbal branches about making odd or depriving remain background rather than local predication.\",\"representative_source_ids\":[\"QS-ce7508dc\",\"QF-f4876314\",\"QF-a1980f8a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:4:qiraat-vowel-pressure","source_type":"word_analysis","support_id":"sup_37bc8e3587047aa8d57f","text":"{\"blocking_evidence\":null,\"headline\":\"variant vowel pressure\",\"reader_payoff\":\"The reader hears the same root frame tilt toward familiar odd-numbered singularity without losing the received word's category force.\",\"reason\":\"The variant rows keep the same root and oath frame; they clarify sound and register rather than overriding the local received form.\",\"representative_source_ids\":[\"QS-b853a661\",\"QF-684d2462\",\"MF-659c0c1e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:3:coordination-and-renewal","source_type":"word_analysis","support_id":"sup_4602710fcfd57fa51f18","text":"{\"blocking_evidence\":null,\"headline\":\"coordination with renewed oath scope\",\"reader_payoff\":\"The reader sees the odd pole joined to the first term without losing its own sworn status.\",\"reason\":\"Attachment evidence marks the repeated particle as governing the second genitive noun and coordinating it with the first noun.\",\"representative_source_ids\":[\"QG-65e484ec\",\"QG-8de5efed\",\"QS-073bc28b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:3","source_type":"word_analysis","support_id":"sup_4d00ddfef2feb1aaea0d","text":"{\"gloss_range\":\"repeated oath-bearing connective before the oddness noun; it both coordinates the second pole with the first and renews oath force for it\",\"prose\":\"The second {{ar:وَ}} ({{tr:wa}}) is the hinge of 89:3. As coordination, it binds {{ar:ٱلْوَتْرِ}} ({{tr:al-watri}}) to {{ar:ٱلشَّفْعِ}} ({{tr:al-shafʿi}}); as a renewed oath particle, it gives the unpaired pole its own genitive oath frame. The repeated particle keeps the two nouns unified but not collapsed, producing a mirrored onset and a two-beat cadence in which the verse turns from pair to singleton.\",\"root_display\":\"-\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:2:intercession-recurrence","source_type":"word_analysis","support_id":"sup_5338abf15d1559c5b58d","text":"{\"blocking_evidence\":null,\"headline\":\"intercession recurrence in the background\",\"reader_payoff\":\"The reader can sense the support field without turning this oath noun into a claim that intercession is being granted here.\",\"reason\":\"The cited intercession passages at 2:255 and 74:48 belong to the broader root field, while local grammar keeps 89:3 as an abstract oath noun.\",\"representative_source_ids\":[\"QI-421918b3\",\"MI-25e794b2\",\"MI-3b92b44f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:2:convergence","source_type":"word_analysis","support_id":"sup_53819df61dae28c2a98a","text":"{\"blocking_evidence\":null,\"headline\":\"converging parity witness\",\"reader_payoff\":\"The reader sees why this short noun is load-bearing: form, root field, order, and sequence all make pairedness a principle of relation.\",\"reason\":\"The convergence rows synthesize already licensed features: definite oath form, root joining pressure, contrast with the second noun, and transition from counted time.\",\"representative_source_ids\":[\"QH-81c2e5dc\",\"QB-aa87f3d1\",\"QY-3abb2921\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:1","source_type":"word_analysis","support_id":"sup_5e77fe68cc6df4bd2584","text":"{\"gloss_range\":\"oath-bearing connective before the pairedness noun; it continues the surrounding oath chain while opening a local even-odd unit\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) opens 89:3 as both connector and oath particle. It carries the earlier oath sequence forward while governing {{ar:ٱلشَّفْعِ}} ({{tr:al-shafʿi}}) as a genitive sworn object, so pairedness enters as evidence rather than as a neutral list item, and the oath answer remains delayed beyond this compact ayah. Because the particle is split analytically but bound in the recited surface, the oath force arrives in one tight onset with the definite noun. Its repetition later in the ayah turns this first onset into the beginning of a doubled particle frame, so the first sound already prepares the balanced two-beat parity witness.\",\"root_display\":\"-\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:1:refrain-frame","source_type":"word_analysis","support_id":"sup_62bc79144f2e3abde33c","text":"{\"blocking_evidence\":null,\"headline\":\"first beat of doubled refrain\",\"reader_payoff\":\"The reader hears the first particle prepare the balanced two-beat frame that will carry both parity poles.\",\"reason\":\"The same particle recurs before the second noun, producing a repeated onset that matches the binary content.\",\"representative_source_ids\":[\"MT-08ec66fd\",\"QE-1927e4b7\",\"QB-a23e4033\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:3:mirrored-cadence","source_type":"word_analysis","support_id":"sup_67a2188a2eb8743e3454","text":"{\"blocking_evidence\":null,\"headline\":\"mirrored two-beat frame\",\"reader_payoff\":\"The reader hears formal equality before the meanings split into paired and unpaired.\",\"reason\":\"The two oath objects are each introduced by the same particle before an article-bearing genitive noun.\",\"representative_source_ids\":[\"QF-56d5a332\",\"MT-6a03cfeb\",\"QP-365aab7d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:3:convergence","source_type":"word_analysis","support_id":"sup_6cf96f1cf1041b3d96e0","text":"{\"blocking_evidence\":null,\"headline\":\"balanced binary mechanism\",\"reader_payoff\":\"The reader notices that this small particle is the mechanism that makes the binary balanced rather than collapsed into one noun phrase.\",\"reason\":\"The convergence row combines locally supported features: renewed oath governance, coordination, hinge position, and repeated onset.\",\"representative_source_ids\":[\"MG-178010d4\",\"QI-5d46e1a4\",\"QY-45e8b676\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:1:bound-surface","source_type":"word_analysis","support_id":"sup_705f26e5a77ce011ae5a","text":"{\"blocking_evidence\":null,\"headline\":\"bound particle-noun onset\",\"reader_payoff\":\"The reader can feel the oath particle and its witness arrive as one compact opening unit.\",\"reason\":\"The word is segmented as a prefixed particle while the local phrase binds it directly to the article-bearing genitive noun.\",\"representative_source_ids\":[\"QF-05913f52\",\"QF-b0cd2949\",\"QP-3d3964b4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:4:rare-root-concentration","source_type":"word_analysis","support_id":"sup_794e35127d1104cc85a7","text":"{\"blocking_evidence\":null,\"headline\":\"rare root concentration\",\"reader_payoff\":\"The reader notices that this compact oath noun is unusually load-bearing for the root's Quranic profile.\",\"reason\":\"The contextual profile marks the exact root-form as low occurrence, and the CRITICAL rows tie that rarity to the local oath noun.\",\"representative_source_ids\":[\"QI-2ef8b845\",\"QH-aa024101\",\"MH-2715036b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:2:paired-odd-binary","source_type":"word_analysis","support_id":"sup_82de70f64188e60aa22b","text":"{\"blocking_evidence\":null,\"headline\":\"first pole of exhaustive parity\",\"reader_payoff\":\"The reader notices that the verse frames countable reality through two opposed parity poles rather than through a loose pair of nouns.\",\"reason\":\"The second noun is coordinated with this one, and the V4 branch for the root includes evenness after oddness or pairing.\",\"representative_source_ids\":[\"QS-191cfbfe\",\"QI-c46fd6cc\",\"QT-0bd45d46\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:2:form-selection","source_type":"word_analysis","support_id":"sup_837464135c4793249bee","text":"{\"blocking_evidence\":null,\"headline\":\"abstract noun over actor or process\",\"reader_payoff\":\"The reader notices that the oath invokes the category itself, leaving agents and petitioners outside the ayah.\",\"reason\":\"The surface is a definite singular abstract noun, not a plural agent form or a derived verbal pattern.\",\"representative_source_ids\":[\"QF-37f133f1\",\"QF-6663333d\",\"MF-6eca4f4a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:3:1:3","source_type":"qac_morpheme","support_id":"sup_89102135663b9a9eedd3","text":"{\"lemma_ar\":\"شَّفْع\",\"morph_features\":\"STEM|POS:N|LEM:$~afoE|ROOT:$fE|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:3:1:3\",\"qac_word_ref\":\"89:3:1\",\"root_ar\":\"ش ف ع\",\"surface_ar\":\"شَّفْعِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:4","source_type":"word_analysis","support_id":"sup_8a4597e321eee765b15c","text":"{\"gloss_range\":\"the definite odd or unpaired category under oath; locally selected as the counterpart to pairedness, with deprivation, taut single-strand, and interval pressure narrowed into the sense of an unpaired remainder\",\"prose\":\"{{ar:ٱلْوَتْرِ}} ({{tr:al-watri}}) is the second definite genitive oath noun, coordinated with {{ar:ٱلشَّفْعِ}} ({{tr:al-shafʿi}}) but given its own renewed particle-governance. The local contrast selects oddness or unpairedness, completing the parity binary and making the singleton pole testify directly. The root's deprivation field narrows into the felt pressure of what is left without its counterpart, with deprivation of deeds in 47:35 giving that loss-register concrete provenance. The bowstring and interval fields make the singleness feel taut and separated, and the sparse recurrence evidence at 23:44 lets separated instances recur without becoming a matched pair. Variant vowel and tanwīn rows sharpen what the received form does: it keeps a definite category, not an indefinite instance, and lets familiar odd-numbered singularity color the same consonantal frame. The abstract noun presents unpairedness as a standing state rather than an event of making odd or depriving. As the final word, it closes the ayah on the unpaired remainder, with clipped sound matching the compactness it names.\",\"root_display\":\"{{ar:و ت ر}} ({{tr:w-t-r}})\",\"root_gloss_range\":\"root range includes oddness, making odd, deprivation or wronged loss, intervallic recurrence, bowstring tension, and other concrete extensions; locally oddness is selected while the loss, interval, and taut-single fields survive as narrowed pressure\",\"surface_display\":\"{{ar:ٱلْوَتْرِ}} ({{tr:al-watri}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:2:definite-oath-category","source_type":"word_analysis","support_id":"sup_8cc37dd1cf066eb5d383","text":"{\"blocking_evidence\":null,\"headline\":\"definite oath category\",\"reader_payoff\":\"The reader sees pairedness treated as a recognized witness under oath, not as one example of a pair.\",\"reason\":\"QAC and attachment evidence show a definite singular abstract noun governed by the oath particle in genitive case.\",\"representative_source_ids\":[\"QG-2e4fe95f\",\"QG-30efe9da\",\"MG-d28a485d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:3:hinge-pivot","source_type":"word_analysis","support_id":"sup_8fa4ad40d91a3761ea77","text":"{\"blocking_evidence\":null,\"headline\":\"pivot from pair to singleton\",\"reader_payoff\":\"The reader feels the ayah move by pivot, not by list-like accumulation.\",\"reason\":\"The particle stands between the two opposed nouns and both links and restarts the phrase.\",\"representative_source_ids\":[\"QT-1e8f2827\",\"QT-a65f0023\",\"QE-2486a7d6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:2:joining-support-pressure","source_type":"word_analysis","support_id":"sup_9d513ce4710dfc87f409","text":"{\"blocking_evidence\":null,\"headline\":\"joining and support pressure\",\"reader_payoff\":\"The reader hears the even term as a state of being seconded or supported, not as a flat arithmetic label only.\",\"reason\":\"The local contrast selects parity, while accepted root branches also include joining as advocate or helper; that branch survives as pressure without replacing the selected parity sense.\",\"representative_source_ids\":[\"QS-81890ab0\",\"QS-a60804de\",\"MS-2bcf860a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:2","source_type":"word_analysis","support_id":"sup_ad24ddd0bf7001863e29","text":"{\"gloss_range\":\"the definite paired or even category under oath; locally selected by contrast with oddness while retaining joining and support pressure\",\"prose\":\"{{ar:ٱلشَّفْعِ}} ({{tr:al-shafʿi}}) is a definite genitive oath noun, so pairedness itself is made a witness rather than explained as a predicate. Its local contrast with {{ar:ٱلْوَتْرِ}} ({{tr:al-watri}}) selects the even or paired side of the binary, while the root's joining and intercession field keeps the arithmetic term relational: a second element can be support, not just quantity. That support field is not granted as entitlement here; intercession is restricted by permission (2:255) and denied benefit in another scene (74:48), so 89:3 abstracts seconding before any claimant appears. The short abstract noun avoids naming an agent, petitioner, or act of making even; it presents the achieved category under oath. Coming after the concrete count of ten nights in 89:2, the word turns a measured example into the wider principle by which countable things are classified. Its compact sound and matched definite-genitive shape prepare the balanced opposition that the next noun completes.\",\"root_display\":\"{{ar:ش ف ع}} ({{tr:sh-f-ʿ}})\",\"root_gloss_range\":\"root range includes making one thing joined to another, evenness after singleness, intercession or seconding support, and other specialized joining branches; locally the parity sense is selected and the support/intercession field survives as narrowed pressure\",\"surface_display\":\"{{ar:ٱلشَّفْعِ}} ({{tr:al-shafʿi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:4:convergence","source_type":"word_analysis","support_id":"sup_add9b46436454e295ab4","text":"{\"blocking_evidence\":null,\"headline\":\"concentrated endpoint\",\"reader_payoff\":\"The reader sees the final word as the ayah's concentrated endpoint, gathering category, tension, rarity, variant pressure, and sound.\",\"reason\":\"The convergence rows synthesize locally licensed features already present in the grammar, variant, semantic, distributional, and sound evidence.\",\"representative_source_ids\":[\"QE-9ff96ada\",\"QH-d6c78bc7\",\"QY-b9d89866\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:4:interval-and-strand-pressure","source_type":"word_analysis","support_id":"sup_afbc032923c06f8abe46","text":"{\"blocking_evidence\":null,\"headline\":\"taut single-strand and interval pressure\",\"reader_payoff\":\"The reader can feel the singleton as taut, separated, and capable of recurring as separated units.\",\"reason\":\"Accepted V4 branches include bowstring tension and successive singles with intervals; they survive as image-pressure under the locally selected oddness sense.\",\"representative_source_ids\":[\"QS-0c7ad43c\",\"QS-16499e9e\",\"QS-9ac4dc37\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:4:deprivation-pressure","source_type":"word_analysis","support_id":"sup_b6ecec4794aa7ae9aa00","text":"{\"blocking_evidence\":null,\"headline\":\"deprivation shadow on unpairedness\",\"reader_payoff\":\"The reader hears oddness as unpairedness with moral or existential pressure, not as number alone.\",\"reason\":\"V4 lists deprivation and wronged loss as accepted root branches, while the local even-odd opposition keeps oddness as the selected sense.\",\"representative_source_ids\":[\"QS-270cae0c\",\"QS-6511cfa5\",\"MS-7483a588\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:4:closing-sound","source_type":"word_analysis","support_id":"sup_cffbf90bb082a79eb08b","text":"{\"blocking_evidence\":null,\"headline\":\"clipped final closure\",\"reader_payoff\":\"The reader feels the verse close on the compact pressure of the singleton rather than returning to the pair.\",\"reason\":\"The word is the ayah's final noun and its local sound rows tie the clipped ending to the semantic field of unpaired compression.\",\"representative_source_ids\":[\"QT-6f375d66\",\"QP-17be788a\",\"QP-21901e69\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:3:1:chain-continuation","source_type":"word_analysis","support_id":"sup_ec5c8c3f93c1a4512928","text":"{\"blocking_evidence\":null,\"headline\":\"continued oath chain\",\"reader_payoff\":\"The reader notices that the ayah does not restart from zero; it adds a new parity witness inside the existing oath sequence.\",\"reason\":\"The bundle marks the oath formula as compressed across the surrounding sequence and the first particle as continuing that chain.\",\"representative_source_ids\":[\"QG-6ea0af13\",\"QT-89e99594\",\"QT-98f62df9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:3:2:3","source_type":"qac_morpheme","support_id":"sup_f29652eff17795a57f1b","text":"{\"lemma_ar\":\"وَتْر\",\"morph_features\":\"STEM|POS:N|LEM:wator|ROOT:wtr|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:3:2:3\",\"qac_word_ref\":\"89:3:2\",\"root_ar\":\"و ت ر\",\"surface_ar\":\"وَتْرِ\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلشَّفْعِ وَٱلْوَتْرِ","ayah_ref":"89:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000802/B001","root_001621/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000802","role":"Joining a unit to one like it supplies the operation that produces evenness, increase, and paired ritual units.","root":"ش ف ع","source_ref":"89:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001621","role":"The single without a mate supplies the contrasting residue and the ordinary numerical or ritual odd state.","root":"و ت ر","source_ref":"89:3","source_word_indices":["2"]}],"changed_reading":{"after":"The verse swears by complementary outcomes of one operation: the unit made paired by addition and the unit left unpaired.","before":"The verse merely lists even and odd numbers."},"confidence":"strong","focus_anchor":"Word 1, al-shaf', and word 2, al-watr, are coordinated oath objects naming opposed states.","mechanism":"Joining one unit to another like it produces a pair and an increase, while leaving a unit without a mate produces oddness. The contrast is therefore dynamic as well as classificatory: add one and a pair appears; withhold one and a singleton remains.","model_id":"baseline-parity-operation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-parity-operation","source_type":"hft","support_id":"sup_6582a111224fc4c38fd0","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلشَّفْعِ وَٱلْوَتْرِ","ayah_ref":"89:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000802/B002","root_001621/B002","root_001621/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000802","role":"A helper who joins another supplies the relational act that converts an isolated party into an advocated one.","root":"ش ف ع","source_ref":"89:3","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001621","role":"A loss that leaves someone with a claim for redress supplies the injured and socially exposed singleton.","root":"و ت ر","source_ref":"89:3","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001621","role":"Deprivation of a due supplies the subtractive result that can make one party deficient while another gains.","root":"و ت ر","source_ref":"89:3","source_word_indices":["2"]}],"changed_reading":{"after":"Shaf' can name accompaniment or advocacy, while watr can name the one left injured, deprived, and awaiting redress.","before":"Even and odd are impersonal quantities."},"confidence":"medium","focus_anchor":"The same two focus nouns at words 1 and 2 carry relational branches beyond arithmetic.","mechanism":"Shaf' can be a second party who joins another as advocate or helper. Watr can be the condition of one bereft by injury or deprived of a due. The pair/single contrast can thus encode whether a vulnerable claim remains alone or gains an effective ally.","model_id":"baseline-advocate-and-wronged"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-advocate-and-wronged","source_type":"hft","support_id":"sup_6f8a39509bae87541e7c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلشَّفْعِ وَٱلْوَتْرِ","ayah_ref":"89:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000802/B005","root_001621/B004","root_001621/B006"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000802","role":"Combining two yields in one collection supplies temporal and productive clustering.","root":"ش ف ع","source_ref":"89:3","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_001621","role":"Successive single arrivals separated by gaps supply a punctuated serial cadence.","root":"و ت ر","source_ref":"89:3","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_001621","role":"A slackening interval in work or travel supplies the pause that distinguishes spaced sequence from continuous pairing.","root":"و ت ر","source_ref":"89:3","source_word_indices":["2"]}],"changed_reading":{"after":"They can mark clustered production and interval-separated succession, two rhythms by which units arrive.","before":"Pair and odd are simultaneous numerical classes."},"confidence":"medium","focus_anchor":"Word 1 has a branch of combining two yields in one event, while word 2 has branches of serial singles and intervening slack.","mechanism":"The focus can contrast two organizations of time and production: paired yields gathered into one occasion versus single arrivals separated by intervals. Pair and odd then describe clustering and cadence, not only totals.","model_id":"baseline-clustered-and-spaced-cadence"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-clustered-and-spaced-cadence","source_type":"hft","support_id":"sup_81845ed399f451dce7cf","trust":"legacy_unbound"}]}
</lane_packet_json>
